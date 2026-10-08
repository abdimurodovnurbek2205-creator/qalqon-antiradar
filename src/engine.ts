/**
 * Antiradar Qalqon - GeoSpatial & Detection Engine
 * ContraCam uslubidagi burchakli va dinamik masofali filtr
 */

import { CameraType, SpeedCamera, UserPosition, RadarAlert } from './types';

export class RadarEngine {
  private cameras: SpeedCamera[] = [];
  
  // O'rtacha tezlik o'lchash (Section Control) holati
  private activeSection: {
    startCamera: SpeedCamera;
    startTimestamp: number;
    startLat: number;
    startLng: number;
    totalDistanceMeters: number;
  } | null = null;

  // Oxirgi ogohlantirilgan kameralar (qayta-qayta baqirmaslik uchun cooldown)
  private notifiedCameraIds: Map<string, number> = new Map();

  constructor(cameras: SpeedCamera[] = []) {
    this.cameras = cameras;
  }

  public setCameras(cameras: SpeedCamera[]) {
    this.cameras = cameras;
  }

  public addCamera(camera: SpeedCamera) {
    this.cameras.push(camera);
  }

  public getCameras(): SpeedCamera[] {
    return this.cameras;
  }

  /**
   * Ikki nuqta orasidagi masofani hisoblash (Haversine formulasi, metrda)
   */
  public static calculateDistance(
    lat1: number,
    lon1: number,
    lat2: number,
    lon2: number
  ): number {
    const R = 6371000; // Yer radiusi metrda
    const dLat = this.deg2rad(lat2 - lat1);
    const dLon = this.deg2rad(lon2 - lon1);
    const a =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(this.deg2rad(lat1)) *
        Math.cos(this.deg2rad(lat2)) *
        Math.sin(dLon / 2) *
        Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  }

  /**
   * Avtomobildan kameraga bo'lgan azimut (bearing) burchagi (0..360 daraja)
   */
  public static calculateBearing(
    lat1: number,
    lon1: number,
    lat2: number,
    lon2: number
  ): number {
    const φ1 = this.deg2rad(lat1);
    const φ2 = this.deg2rad(lat2);
    const Δλ = this.deg2rad(lon2 - lon1);

    const y = Math.sin(Δλ) * Math.cos(φ2);
    const x =
      Math.cos(φ1) * Math.sin(φ2) -
      Math.sin(φ1) * Math.cos(φ2) * Math.cos(Δλ);
    const θ = Math.atan2(y, x);
    const bearing = (this.rad2deg(θ) + 360) % 360;
    return bearing;
  }

  /**
   * Ikki burchak orasidagi eng kichik farq (-180..+180 daraja)
   */
  public static angleDifference(angle1: number, angle2: number): number {
    let diff = (angle1 - angle2 + 180) % 360 - 180;
    return Math.abs(diff < -180 ? diff + 360 : diff);
  }

  /**
   * Tezlikka bog'liq dinamik ogohlantirish masofasi (metrda)
   * Sekin haydaganda 300m, tez haydaganda 1000m gacha oldin ogohlantiradi
   */
  public static getDynamicAlertDistance(speedKmH: number): number {
    if (speedKmH <= 40) return 300;
    if (speedKmH <= 60) return 450;
    if (speedKmH <= 80) return 600;
    if (speedKmH <= 100) return 800;
    return 1000;
  }

  /**
   * Asosiy tahlil funksiyasi:
   * Haydovchining joriy nuqtasi va tezligi asosida eng xavfli/yaqin kameralarni aniqlaydi.
   */
  public processPosition(userPos: UserPosition): RadarAlert[] {
    const alerts: RadarAlert[] = [];
    const maxLookaheadDistance = RadarEngine.getDynamicAlertDistance(userPos.speed);

    for (const camera of this.cameras) {
      const distance = RadarEngine.calculateDistance(
        userPos.lat,
        userPos.lng,
        camera.lat,
        camera.lng
      );

      // Belgilangan masofadan uzoqda bo'lsa tekshirmaymiz
      const alertThreshold = camera.distanceAlertThreshold || maxLookaheadDistance;
      if (distance > alertThreshold) {
        continue;
      }

      // Harakat yo'nalishi (bearing) tahlili
      const bearingToCamera = RadarEngine.calculateBearing(
        userPos.lat,
        userPos.lng,
        camera.lat,
        camera.lng
      );

      // 1. Haydovchi kamera tomonga harakatlanmoqdami?
      // Agar avtomobil yo'nalishi (heading) va kamera tomon yo'nalish farqi > 50 daraja bo'lsa,
      // demak haydovchi boshqa tomonga ketmoqda yoki kamera ortda qolgan.
      const headingDiff = RadarEngine.angleDifference(userPos.heading, bearingToCamera);
      const isHeadingTowardsCamera = headingDiff <= 45;

      if (!isHeadingTowardsCamera && distance > 50) {
        // 50 metrdan uzoq bo'lsa va yo'nalish to'g'ri kelmasa o'tkazib yuboramiz
        continue;
      }

      // 2. Kamera aynan shu yo'nalishga qaratilganmi?
      // Azimuth 0..360 bo'lib, kamera suratga oladigan oqim yo'nalishini ko'rsatadi.
      // (Agar azimuth -1 bo'lsa, barcha yo'nalishlar uchun 360 darajali kamera)
      let matchesDirection = true;
      if (camera.azimuth >= 0) {
        const cameraCoverage = camera.angleCoverage || 45;
        // Kamera old tomondan (lobi) yoki orqa tomondan (ortidan) oladi.
        // Odatda kamera azimuti mashina kelayotgan yo'nalishga qarshi yoki mos keladi.
        const angleDiffDirect = RadarEngine.angleDifference(userPos.heading, camera.azimuth);
        const angleDiffReverse = RadarEngine.angleDifference((userPos.heading + 180) % 360, camera.azimuth);
        
        // Agar to'g'ridan yoki orqa tomondan oladigan burchakka mos tushmasa
        matchesDirection = angleDiffDirect <= cameraCoverage || angleDiffReverse <= cameraCoverage;
      }

      if (!matchesDirection) {
        continue; // Qarama-qarshi yoki parallel ko'chadagi kamera
      }

      // 3. Tezlik buzilishini baholash
      const isOverSpeed = camera.speedLimit > 0 && userPos.speed > camera.speedLimit;
      const speedDiff = camera.speedLimit > 0 ? Math.round(userPos.speed - camera.speedLimit) : 0;

      let alertLevel: 'info' | 'warning' | 'danger' = 'info';
      if (isOverSpeed) {
        alertLevel = 'danger';
      } else if (camera.speedLimit > 0 && userPos.speed >= camera.speedLimit - 5) {
        alertLevel = 'warning';
      }

      // O'zbekcha ogohlantirish xabari shakllantirish
      const message = this.buildAlertMessage(camera, Math.round(distance), userPos.speed, isOverSpeed);

      alerts.push({
        camera,
        distance: Math.round(distance),
        isApproaching: isHeadingTowardsCamera,
        isOverSpeed,
        speedDiff,
        alertLevel,
        message
      });
    }

    // Eng yaqin va eng xavfli radar bo'yicha saralash
    alerts.sort((a, b) => {
      if (a.alertLevel === 'danger' && b.alertLevel !== 'danger') return -1;
      if (b.alertLevel === 'danger' && a.alertLevel !== 'danger') return 1;
      return a.distance - b.distance;
    });

    return alerts;
  }

  /**
   * O'zbek tilidagi tushunarli ovozli/matnli xabar matnini tuzish
   */
  private buildAlertMessage(
    camera: SpeedCamera,
    distanceM: number,
    currentSpeed: number,
    isOverSpeed: boolean
  ): string {
    const distText = `${distanceM} metr`;
    let typeName = 'Kamera';

    switch (camera.type) {
      case CameraType.STATIC:
        typeName = camera.speedLimit > 0 ? `Tezlik kamerasi ${camera.speedLimit}` : 'Statsionar radar';
        break;
      case CameraType.MOBILE_AMBUSH:
        typeName = `Mobil pistirma radari ${camera.speedLimit > 0 ? camera.speedLimit : ''}`;
        break;
      case CameraType.TRAFFIC_LIGHT:
        typeName = 'Svetofor va stop-liniya nazorati';
        break;
      case CameraType.BUS_LANE:
        typeName = 'A-yo‘lak avtobus kamerasi';
        break;
      case CameraType.AVERAGE_SPEED_START:
        typeName = `O‘rtacha tezlik nazorati boshlandi: cheklov ${camera.speedLimit}`;
        break;
      case CameraType.AVERAGE_SPEED_END:
        typeName = 'O‘rtacha tezlik nazorati yakunlandi';
        break;
      case CameraType.SPEED_BUMP:
        typeName = 'Sun’iy notekislik';
        break;
      case CameraType.DANGER_ZONE:
        typeName = 'Xavfli burilish yoki avariya zonasi';
        break;
    }

    if (isOverSpeed) {
      return `Diqqat! ${distText} oldinda ${typeName}! Tezlikni tushiring!`;
    } else {
      return `${distText} oldinda ${typeName}`;
    }
  }

  private static deg2rad(deg: number): number {
    return deg * (Math.PI / 180);
  }

  private static rad2deg(rad: number): number {
    return rad * (180 / Math.PI);
  }
}
