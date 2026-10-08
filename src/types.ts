/**
 * Antiradar Qalqon - Radar & Camera Types
 */

export enum CameraType {
  STATIC = 'static',             // Statsionar tezlik kamerasi (Hikvision, Cordon, Strelka)
  MOBILE_AMBUSH = 'mobile',      // Mobil pistirma / Trinoga / Patrul
  TRAFFIC_LIGHT = 'traffic_light', // Svetofor, Stop-liniya, qizil chiroq
  BUS_LANE = 'bus_lane',         // Jamoat transporti (A yo'lagi) kamerasi
  AVERAGE_SPEED_START = 'avg_start', // O'rtacha tezlik koridori boshlanishi (AutoCon)
  AVERAGE_SPEED_END = 'avg_end',     // O'rtacha tezlik koridori tugashi
  SPEED_BUMP = 'speed_bump',     // Sun'iy notekislik ("lejaщiy")
  DANGER_ZONE = 'danger_zone'    // Xavfli burilish yoki avariya o'chog'i
}

export interface SpeedCamera {
  id: string;
  name: string;
  lat: number;
  lng: number;
  type: CameraType;
  speedLimit: number; // masalan: 60, 70, 100 km/h (0 bo'lsa faqat qoidabuzarlik kamerasi)
  azimuth: number;    // Kamera qaratilgan yo'nalish (0..359 daraja)
  angleCoverage?: number; // Kameralarning qamrab olish burchagi (standart 45 daraja)
  roadName?: string;
  distanceAlertThreshold?: number; // Ogohlantirish masofasi (metrda, bo'sh bo'lsa tezlikka qarab hisoblanadi)
  pairId?: string;    // O'rtacha tezlik kamerasining juft IDsi (start <-> end)
}

export interface UserPosition {
  lat: number;
  lng: number;
  speed: number;    // km/h
  heading: number;  // 0..359 daraja (harakat yo'nalishi)
  accuracy: number; // metrda
  timestamp: number;
}

export interface RadarAlert {
  camera: SpeedCamera;
  distance: number;       // Kamera qancha masofada (metrda)
  isApproaching: boolean; // Haydovchi kamera tomon bormoqdami
  isOverSpeed: boolean;   // Tezlik chegaradan oshganmi
  speedDiff: number;      // Qancha oshgan (+15 km/h va h.k.)
  alertLevel: 'info' | 'warning' | 'danger'; // ogohlantirish darajasi
  message: string;        // O'zbekcha ovozli/matnli xabar
}
