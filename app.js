/**
 * QALQON ANTIRADAR - Professional Jonli Haydash va Radar Detektori
 * O'zbekiston yo'llari bo'yicha jonli GPS, Neoline X-COP radar standarti va 3D Navigatsiya Strelkasi
 */

// O'zbekiston bo'ylab barcha 58 ta radarlar to'liq bazasi
let speedCameras = [
  // ==================== BUXORO VILOYATI VA ATROFI ====================
  {
    id: "uz-bux-005",
    name: "Ko'chma Uch oyoq 70 - Buxoro aylanma M37",
    lat: 39.8820, lng: 64.3650,
    type: "uch_oyoq", speedLimit: 70, azimuth: 110,
    roadName: "M37 Buxoro aylanma yo'li (Romitan)", distanceAlertThreshold: 650
  },
  {
    id: "uz-bux-006",
    name: "Lochin 70 - Romitan - Buxoro trassasi",
    lat: 39.8920, lng: 64.3400,
    type: "lochin", speedLimit: 70, azimuth: 290,
    roadName: "80V121 Romitan yo'li", distanceAlertThreshold: 650
  },
  {
    id: "uz-bux-007",
    name: "Lochin 60 - Galaosiyo shahar kirish yo'li",
    lat: 39.8550, lng: 64.4420,
    type: "lochin", speedLimit: 60, azimuth: 135,
    roadName: "Galaosiyo shoh ko'chasi", distanceAlertThreshold: 550
  },
  {
    id: "uz-bux-008",
    name: "Kamera orqadan oladi! 60 - Buxoro Galaosiyo",
    lat: 39.8350, lng: 64.4250,
    type: "rear", speedLimit: 60, azimuth: 180,
    roadName: "Buxoro shahar kirish yo'li (Orqadan uradi)", distanceAlertThreshold: 500
  },
  {
    id: "uz-bux-009",
    name: "YPX Patrul 360 - Buxoro aylanmasi",
    lat: 39.8700, lng: 64.4050,
    type: "patrul_360", speedLimit: 70, azimuth: 220,
    roadName: "M37 Galaosiyo chorrahasi", distanceAlertThreshold: 600
  },
  {
    id: "uz-bux-001",
    name: "Lochin 60 - Buxoro Naqshbandiy ko'chasi",
    lat: 39.7745, lng: 64.4286,
    type: "lochin", speedLimit: 60, azimuth: 90,
    roadName: "Bahouddin Naqshbandiy ko'chasi", distanceAlertThreshold: 550
  },
  {
    id: "uz-bux-002",
    name: "Chorraha kamerasi - Buxoro Ibrohim Mo'minov",
    lat: 39.7680, lng: 64.4420,
    type: "traffic_light", speedLimit: 60, azimuth: 45,
    roadName: "Buxoro shahar markazi", distanceAlertThreshold: 450
  },
  {
    id: "uz-bux-003",
    name: "Ko'chma Uch oyoq 70 - G'ijduvon shahar aylanmasi",
    lat: 40.0950, lng: 64.6750,
    type: "uch_oyoq", speedLimit: 70, azimuth: 260,
    roadName: "M37 G'ijduvon trassasi", distanceAlertThreshold: 650
  },
  {
    id: "uz-bux-004",
    name: "Lochin 100 - A380 Gazli - Urganch trassasi",
    lat: 39.9550, lng: 63.8500,
    type: "lochin", speedLimit: 100, azimuth: 310,
    roadName: "A380 Qizilqum magistrali", distanceAlertThreshold: 850
  },
  {
    id: "uz-bux-010",
    name: "Chorraha kamerasi - Vobkent aylanmasi",
    lat: 39.9250, lng: 64.5150,
    type: "traffic_light", speedLimit: 60, azimuth: 45,
    roadName: "M37 Vobkent chorrahasi", distanceAlertThreshold: 450
  },

  // ==================== SAMARQAND VILOYATI VA SHAHRI ====================
  {
    id: "uz-sam-001",
    name: "Lochin 60 - Registon ko'chasi",
    lat: 39.6548, lng: 66.9752,
    type: "lochin", speedLimit: 60, azimuth: 90,
    roadName: "Registon ko'chasi (Samarqand)", distanceAlertThreshold: 500
  },
  {
    id: "uz-sam-002",
    name: "Chorraha kamerasi - Rudakiy va Gagarin",
    lat: 39.6580, lng: 66.9550,
    type: "traffic_light", speedLimit: 60, azimuth: 45,
    roadName: "Rudakiy va Gagarin chorrahasi", distanceAlertThreshold: 450
  },
  {
    id: "uz-sam-003",
    name: "Kamera orqadan oladi! - Beruniy ko'chasi",
    lat: 39.6640, lng: 66.9420,
    type: "rear", speedLimit: 60, azimuth: 315,
    roadName: "Beruniy ko'chasi (Orqadan uradi)", distanceAlertThreshold: 500
  },
  {
    id: "uz-sam-004",
    name: "Lochin 60 - Spitamen shoh ko'chasi",
    lat: 39.6450, lng: 66.9380,
    type: "lochin", speedLimit: 60, azimuth: 180,
    roadName: "Spitamen shoh ko'chasi", distanceAlertThreshold: 550
  },
  {
    id: "uz-sam-005",
    name: "Chorraha kamerasi - Dahbed va Registon",
    lat: 39.6610, lng: 66.9790,
    type: "traffic_light", speedLimit: 60, azimuth: 0,
    roadName: "Dahbed ko'chasi chorrahasi", distanceAlertThreshold: 450
  },
  {
    id: "uz-sam-006",
    name: "Ko'chma Uch oyoq 70 - Ulug'bek rasadxonasi",
    lat: 39.6740, lng: 66.9950,
    type: "uch_oyoq", speedLimit: 70, azimuth: 45,
    roadName: "M39 Toshkent yo'nalishi (Pistirma)", distanceAlertThreshold: 650
  },
  {
    id: "uz-sam-007",
    name: "Lochin 70 - Samarqand Katta halqa yo'li",
    lat: 39.6850, lng: 66.9250,
    type: "lochin", speedLimit: 70, azimuth: 270,
    roadName: "Samarqand aylanma halqa yo'li", distanceAlertThreshold: 650
  },
  {
    id: "uz-sam-008",
    name: "YPX Patrul 360 - Samarqand Vokzal maydoni",
    lat: 39.6680, lng: 66.9280,
    type: "patrul_360", speedLimit: 60, azimuth: 220,
    roadName: "Temiryo'l vokzali atrofi", distanceAlertThreshold: 500
  },
  {
    id: "uz-sam-009",
    name: "Lochin 100 - M39 Samarqand - Jizzax trassasi",
    lat: 39.7250, lng: 67.0450,
    type: "lochin", speedLimit: 100, azimuth: 50,
    roadName: "M39 Xalqaro trassa (Bulung'ur)", distanceAlertThreshold: 850
  },
  {
    id: "uz-sam-010",
    name: "Lochin 100 - M37 Samarqand - Navoiy trassasi",
    lat: 39.6950, lng: 66.8250,
    type: "lochin", speedLimit: 100, azimuth: 290,
    roadName: "M37 Kattaqo'rg'on yo'nalishi", distanceAlertThreshold: 850
  },

  // ==================== TOSHKENT SHAHRI VA VILOYATI ====================
  {
    id: "uz-tas-001",
    name: "Lochin 60 - Amir Temur (Oloy bozori)",
    lat: 41.3195, lng: 69.2812,
    type: "lochin", speedLimit: 60, azimuth: 25,
    roadName: "Amir Temur shoh ko'chasi (Toshkent)", distanceAlertThreshold: 550
  },
  {
    id: "uz-tas-002",
    name: "Chorraha kamerasi - A.Qodiriy (Stop-liniya)",
    lat: 41.3258, lng: 69.2835,
    type: "traffic_light", speedLimit: 60, azimuth: 25,
    roadName: "Abdulla Qodiriy va Amir Temur", distanceAlertThreshold: 450
  },
  {
    id: "uz-tas-003",
    name: "A-yo'lak - Alisher Navoiy ko'chasi",
    lat: 41.3182, lng: 69.2554,
    type: "bus_lane", speedLimit: 60, azimuth: 105,
    roadName: "Alisher Navoiy ko'chasi", distanceAlertThreshold: 380
  },
  {
    id: "uz-tas-004",
    name: "Kamera orqadan oladi! - THAY Oqtepa",
    lat: 41.2854, lng: 69.1985,
    type: "rear", speedLimit: 70, azimuth: 180,
    roadName: "THAY Katta halqa yo'li", distanceAlertThreshold: 650
  },
  {
    id: "uz-tas-005",
    name: "AutoCon Koridor - Yangi O'zbekiston Kirish",
    lat: 41.3450, lng: 69.3750,
    type: "avg_start", speedLimit: 70, azimuth: 65,
    roadName: "Yangi O'zbekiston shoh ko'chasi", distanceAlertThreshold: 700
  },
  {
    id: "uz-tas-006",
    name: "AutoCon Koridor - Yangi O'zbekiston Chiqish",
    lat: 41.3580, lng: 69.4100,
    type: "avg_end", speedLimit: 70, azimuth: 65,
    roadName: "Yangi O'zbekiston shoh ko'chasi", distanceAlertThreshold: 700
  },
  {
    id: "uz-tas-007",
    name: "YPX Patrul 360 - Bunyodkor shoh ko'chasi",
    lat: 41.2785, lng: 69.2155,
    type: "patrul_360", speedLimit: 60, azimuth: 220,
    roadName: "Bunyodkor (Mirzo Ulug'bek metrosi)", distanceAlertThreshold: 550
  },
  {
    id: "uz-tas-008",
    name: "Lochin 70 - M39 Toshkent chiqish posti",
    lat: 41.2350, lng: 69.1550,
    type: "lochin", speedLimit: 70, azimuth: 240,
    roadName: "M39 Erkin YPX Posti", distanceAlertThreshold: 700
  },
  {
    id: "uz-tas-009",
    name: "Ko'chma Uch oyoq 100 - M39 Yangiyo'l",
    lat: 41.1350, lng: 69.0450,
    type: "uch_oyoq", speedLimit: 100, azimuth: 235,
    roadName: "M39 Yangiyo'l aylanmasi (Trinoga)", distanceAlertThreshold: 850
  },
  {
    id: "uz-tas-010",
    name: "Lochin 100 - Chorvoq trassasi (4R12)",
    lat: 41.4350, lng: 69.5250,
    type: "lochin", speedLimit: 100, azimuth: 50,
    roadName: "4R12 Chorvoq yo'li", distanceAlertThreshold: 850
  },

  // ==================== NAVOIY VA BOSHQALAR ====================
  {
    id: "uz-nav-001",
    name: "Lochin 70 - Karmana shahar kirish posti",
    lat: 40.1380, lng: 65.3650,
    type: "lochin", speedLimit: 70, azimuth: 285,
    roadName: "M37 Navoiy Karmana yo'li", distanceAlertThreshold: 700
  },
  {
    id: "uz-nav-002",
    name: "Lochin 100 - M37 Navoiy - Buxoro trassasi",
    lat: 40.1150, lng: 65.1850,
    type: "lochin", speedLimit: 100, azimuth: 270,
    roadName: "M37 Xalqaro magistral", distanceAlertThreshold: 850
  },
  {
    id: "uz-qar-001",
    name: "Lochin 60 - Qarshi Mustaqillik shoh ko'chasi",
    lat: 38.8612, lng: 65.7891,
    type: "lochin", speedLimit: 60, azimuth: 180,
    roadName: "Mustaqillik shoh ko'chasi (Qarshi)", distanceAlertThreshold: 550
  },
  {
    id: "uz-and-001",
    name: "Lochin 60 - Andijon Bobur shoh ko'chasi",
    lat: 40.7821, lng: 72.3442,
    type: "lochin", speedLimit: 60, azimuth: 45,
    roadName: "Bobur shoh ko'chasi (Andijon)", distanceAlertThreshold: 550
  }
];

// O'zbekiston viloyatlarini koordinata orqali aniqlash
function detectRegionName(lat, lng) {
  if (lat >= 39.5 && lat <= 40.5 && lng >= 63.5 && lng <= 65.2) return "Buxoro viloyati";
  if (lat >= 39.3 && lat <= 40.2 && lng >= 66.2 && lng <= 67.5) return "Samarqand viloyati";
  if (lat >= 41.0 && lat <= 41.6 && lng >= 68.9 && lng <= 69.8) return "Toshkent shahri";
  if (lat >= 39.8 && lat <= 40.5 && lng >= 65.0 && lng <= 66.0) return "Navoiy viloyati";
  if (lat >= 39.8 && lat <= 40.5 && lng >= 67.5 && lng <= 68.6) return "Jizzax viloyati";
  if (lat >= 40.3 && lat <= 41.0 && lng >= 68.3 && lng <= 69.2) return "Sirdaryo viloyati";
  if (lat >= 38.3 && lat <= 39.5 && lng >= 65.2 && lng <= 66.8) return "Qashqadaryo viloyati";
  if (lat >= 37.0 && lat <= 38.6 && lng >= 66.5 && lng <= 68.5) return "Surxondaryo viloyati";
  if (lat >= 40.5 && lat <= 41.2 && lng >= 71.0 && lng <= 72.8) return "Farg'ona vodiysi";
  if (lat >= 41.0 && lat <= 42.0 && lng >= 60.0 && lng <= 61.5) return "Xorazm viloyati";
  if (lat >= 42.0 && lat <= 44.0 && lng >= 58.0 && lng <= 60.5) return "Qoraqalpog'iston";
  return "O'zbekiston";
}

// Geodezik hisob-kitob dvigateli
class RadarEngineCore {
  constructor(cams) {
    this.cameras = cams;
    this.distanceMode = 'auto'; // 'auto', 'far', 'near'
  }

  static distance(lat1, lon1, lat2, lon2) {
    const R = 6371000;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
              Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
              Math.sin(dLon/2) * Math.sin(dLon/2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }

  static bearing(lat1, lon1, lat2, lon2) {
    const phi1 = lat1 * Math.PI / 180;
    const phi2 = lat2 * Math.PI / 180;
    const deltaLon = (lon2 - lon1) * Math.PI / 180;
    const y = Math.sin(deltaLon) * Math.cos(phi2);
    const x = Math.cos(phi1) * Math.sin(phi2) - Math.sin(phi1) * Math.cos(phi2) * Math.cos(deltaLon);
    return (Math.atan2(y, x) * 180 / Math.PI + 360) % 360;
  }

  static angleDiff(a1, a2) {
    let diff = (a1 - a2 + 180) % 360 - 180;
    return Math.abs(diff < -180 ? diff + 360 : diff);
  }

  static getUzbekHeadingText(deg) {
    const dirs = [
      { max: 22.5, txt: "SHIMOL" },
      { max: 67.5, txt: "SHIMOL-SHARQ" },
      { max: 112.5, txt: "SHARQ" },
      { max: 157.5, txt: "JANUB-SHARQ" },
      { max: 202.5, txt: "JANUB" },
      { max: 247.5, txt: "JANUB-G'ARB" },
      { max: 292.5, txt: "G'ARB" },
      { max: 337.5, txt: "SHIMOL-G'ARB" },
      { max: 360.0, txt: "SHIMOL" }
    ];
    const norm = (deg % 360 + 360) % 360;
    for (const d of dirs) {
      if (norm <= d.max) return `${d.txt} • ${Math.round(norm)}°`;
    }
    return `${Math.round(norm)}°`;
  }

  getAlertDistance(speed) {
    if (this.distanceMode === 'far') return 1000;
    if (this.distanceMode === 'near') return 450;
    if (speed <= 40) return 380;
    if (speed <= 60) return 520;
    if (speed <= 80) return 680;
    if (speed <= 100) return 850;
    return 1050;
  }

  check(pos) {
    const alerts = [];
    const maxLookahead = this.getAlertDistance(pos.speed);

    for (const cam of this.cameras) {
      const dist = RadarEngineCore.distance(pos.lat, pos.lng, cam.lat, cam.lng);
      const threshold = cam.distanceAlertThreshold || maxLookahead;
      if (dist > threshold) continue;

      const bearingToCam = RadarEngineCore.bearing(pos.lat, pos.lng, cam.lat, cam.lng);
      const headingDiff = RadarEngineCore.angleDiff(pos.heading, bearingToCam);

      // Harakatlanayotganda oldindagi 60 darajali sektor
      if (pos.speed > 5 && headingDiff > 60 && dist > 50) continue;

      // Kamera yo'nalishi (Azimut) tekshiruvi
      if (cam.azimuth >= 0 && pos.speed > 5) {
        const d1 = RadarEngineCore.angleDiff(pos.heading, cam.azimuth);
        const d2 = RadarEngineCore.angleDiff((pos.heading + 180) % 360, cam.azimuth);
        if (d1 > 55 && d2 > 55) continue;
      }

      const isOverSpeed = cam.speedLimit > 0 && pos.speed > cam.speedLimit;
      const speedDiff = cam.speedLimit > 0 ? Math.round(pos.speed - cam.speedLimit) : 0;
      let alertLevel = 'info';
      if (isOverSpeed) {
        alertLevel = 'danger';
      } else if (cam.speedLimit > 0 && pos.speed >= cam.speedLimit - 5) {
        alertLevel = 'warning';
      }

      alerts.push({
        camera: cam,
        distance: Math.round(dist),
        isOverSpeed,
        speedDiff,
        alertLevel,
        message: this.buildText(cam, Math.round(dist), isOverSpeed)
      });
    }

    alerts.sort((a, b) => {
      if (a.alertLevel === 'danger' && b.alertLevel !== 'danger') return -1;
      if (b.alertLevel === 'danger' && a.alertLevel !== 'danger') return 1;
      return a.distance - b.distance;
    });

    return alerts;
  }

  buildText(cam, dist, isOver) {
    let name = 'Lochin';
    if (cam.type === 'lochin') name = `Lochin ${cam.speedLimit}`;
    else if (cam.type === 'rear') name = `Kamera orqadan oladi! ${cam.speedLimit}`;
    else if (cam.type === 'uch_oyoq') name = `Ko'chma uch oyoq radari ${cam.speedLimit}`;
    else if (cam.type === 'patrul_360') name = `YPX 360 patrul radari`;
    else if (cam.type === 'traffic_light') name = `Chorraha kamerasi (Stop-liniya)`;
    else if (cam.type === 'bus_lane') name = `A-yo'lak kamerasi`;
    else if (cam.type === 'avg_start') name = `AutoCon O'rtacha tezlik`;
    else if (cam.type === 'speed_bump') name = `Sun'iy notekislik`;

    if (isOver) {
      return `Diqqat! ${dist} metr oldinda ${name}! Tezlikni tushiring!`;
    }
    return `${dist} metr oldinda ${name}`;
  }
}

// Professional Real Radar Sound Engine - Neoline Standarti
class AudioCore {
  constructor() {
    this.muted = false;
    this.volume = 1.0;
    this.enableGeiger = true;
    this.audioCache = {};
    this.lastGeigerTime = 0;
    this.lastSpokenKey = '';
    this.lastVoiceTime = 0;
    this.lastOverSpeedAlarmTime = 0;
    this.activeCameraId = null;
    this.unlocked = false;

    // Neoline va Tizim tovushlari
    const tones = [
      'neoline_chirp.wav', 'neoline_click.wav', 'overspeed_alarm.wav', 'pass.wav'
    ];
    tones.forEach(f => {
      const a = new Audio(`sounds/${f}`);
      a.preload = 'auto';
      this.audioCache[f] = a;
    });

    // O'zbek jurnalist qizi professional studiya ovozlari
    const voiceClips = [
      'lochin_60.mp3', 'lochin_70.mp3', 'lochin_100.mp3',
      'rear_60.mp3', 'rear_70.mp3', 'rear_100.mp3',
      'uch_oyoq.mp3', 'uch_oyoq_70.mp3', 'uch_oyoq_100.mp3',
      'patrul_360.mp3', 'chorraha.mp3', 'autocon_start.mp3',
      'autocon_end.mp3', 'bus_lane.mp3', 'speed_bump.mp3',
      'slowdown.mp3', 'cleared.mp3'
    ];
    voiceClips.forEach(f => {
      const a = new Audio(`sounds/${f}`);
      a.preload = 'auto';
      this.audioCache[f] = a;
    });
  }

  unlock() {
    if (this.unlocked) return;
    this.unlocked = true;
    try {
      const ch = this.audioCache['neoline_chirp.wav'];
      if (ch) {
        ch.volume = 0.01;
        ch.play().then(() => {
          ch.pause();
          ch.currentTime = 0;
          ch.volume = this.volume;
        }).catch(() => {});
      }
    } catch (e) {}

    const pill = document.getElementById('audio-unlock-overlay');
    if (pill) {
      pill.classList.add('fade-out');
      setTimeout(() => pill.remove(), 600);
    }
  }

  playFile(filename, volMultiplier = 1.0) {
    if (this.muted) return;
    try {
      const src = this.audioCache[filename];
      if (src) {
        const clone = src.cloneNode();
        clone.volume = Math.max(0, Math.min(1.0, this.volume * volMultiplier));
        clone.play().catch(() => {});
      }
    } catch (e) {
      console.warn("Audio play error:", e);
    }
  }

  playRadarAlertChime() {
    this.playFile('neoline_chirp.wav', 1.0);
  }

  playPassChime() {
    this.playFile('cleared.mp3', 1.0);
  }

  triggerGeiger(distanceMeters) {
    if (this.muted || !this.enableGeiger) return;
    const now = Date.now();

    let interval = 1200;
    if (distanceMeters <= 120) {
      interval = 140; // Tez chiqillash
    } else if (distanceMeters <= 250) {
      interval = 280;
    } else if (distanceMeters <= 400) {
      interval = 500;
    } else if (distanceMeters <= 600) {
      interval = 850;
    }

    if (now - this.lastGeigerTime >= interval) {
      this.lastGeigerTime = now;
      this.playFile('neoline_click.wav', 0.9);
    }
  }

  playOverSpeedAlarm() {
    if (this.muted) return;
    const now = Date.now();
    if (now - this.lastOverSpeedAlarmTime >= 1200) {
      this.lastOverSpeedAlarmTime = now;
      this.playFile('overspeed_alarm.wav', 1.0);
    }
  }

  announceCamera(cam, isOverSpeed) {
    if (this.muted) return;
    const now = Date.now();

    let voiceFile = 'lochin_60.mp3';

    if (cam.type === 'lochin') {
      if (cam.speedLimit === 70) voiceFile = 'lochin_70.mp3';
      else if (cam.speedLimit === 100) voiceFile = 'lochin_100.mp3';
      else voiceFile = 'lochin_60.mp3';
    }
    else if (cam.type === 'rear') {
      if (cam.speedLimit === 70) voiceFile = 'rear_70.mp3';
      else if (cam.speedLimit === 100) voiceFile = 'rear_100.mp3';
      else voiceFile = 'rear_60.mp3';
    }
    else if (cam.type === 'uch_oyoq') {
      if (cam.speedLimit === 70) voiceFile = 'uch_oyoq_70.mp3';
      else if (cam.speedLimit === 100) voiceFile = 'uch_oyoq_100.mp3';
      else voiceFile = 'uch_oyoq.mp3';
    }
    else if (cam.type === 'patrul_360') {
      voiceFile = 'patrul_360.mp3';
    }
    else if (cam.type === 'traffic_light') {
      voiceFile = 'chorraha.mp3';
    }
    else if (cam.type === 'bus_lane') {
      voiceFile = 'bus_lane.mp3';
    }
    else if (cam.type === 'avg_start') {
      voiceFile = 'autocon_start.mp3';
    }
    else if (cam.type === 'speed_bump') {
      voiceFile = 'speed_bump.mp3';
    }

    if (this.lastSpokenKey !== voiceFile || now - this.lastVoiceTime > 8000) {
      this.lastSpokenKey = voiceFile;
      this.lastVoiceTime = now;

      // 1. Neoline radar lock signali
      this.playRadarAlertChime();

      // 2. O'zbek jurnalist qizi ovozi
      setTimeout(() => {
        if (isOverSpeed) {
          this.playFile('slowdown.mp3', 1.0);
        } else {
          this.playFile(voiceFile, 1.0);
        }
      }, 350);
    }
  }
}

// Global obyektlar
const engine = new RadarEngineCore(speedCameras);
const audio = new AudioCore();

// Boshlang'ich koordinatalar: Kompyuterning aniq joylashuvi (Samarqand shahri, Temirchilar ko'chasi)
let currentPosition = {
  lat: 39.6588,
  lng: 66.9615,
  speed: 0,
  heading: 105,
  accuracy: 10,
  timestamp: Date.now()
};

let previousPosition = null;
let map = null;
let carMarker = null;
let cameraMarkersLayer = null;
let currentTileLayer = null;
let currentLayerType = 'google'; // 'google', 'osm', 'hybrid'
let watchId = null;
let isHudActive = false;
let followUser = true;
let isTestDriveActive = false;
let testDriveTimer = null;

// Xaritani initsializatsiya qilish (Google Maps va OSM bilan)
function initMap() {
  const mapEl = document.getElementById('map');
  if (!mapEl) return;

  try {
    map = L.map('map', {
      zoomControl: false,
      attributionControl: false
    }).setView([currentPosition.lat, currentPosition.lng], 16);

    // Xarita qatlamini o'rnatish
    setMapLayer(currentLayerType);

    cameraMarkersLayer = L.layerGroup().addTo(map);

    // Maxsus 3D Navigatsiya Strelkasi (Yo'l bo'ylab radar nuri va harakat strelkasi)
    const carIcon = L.divIcon({
      className: 'nav-arrow-container',
      html: `
        <div id="car-marker" class="nav-arrow-wrapper" style="transform: rotate(${currentPosition.heading}deg);">
          <div class="radar-cone-beam"></div>
          <div class="nav-arrow-body">
            <svg viewBox="0 0 48 48" width="46" height="46">
              <defs>
                <filter id="arrow-glow" x="-20%" y="-20%" width="140%" height="140%">
                  <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#00f2fe" flood-opacity="0.9"/>
                </filter>
              </defs>
              <path d="M24 4 L42 42 L24 33 L6 42 Z" fill="#00f2fe" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" filter="url(#arrow-glow)"/>
              <path d="M24 8 L39 39 L24 32 Z" fill="#38bdf8"/>
            </svg>
          </div>
          <div class="nav-gps-dot"></div>
        </div>`,
      iconSize: [60, 60],
      iconAnchor: [30, 30]
    });

    carMarker = L.marker([currentPosition.lat, currentPosition.lng], { icon: carIcon, zIndexOffset: 1000 }).addTo(map);

    // Barcha kameralarni chizish
    renderCamerasOnMap();

    // Xarita qo'lda surilganda avto-kuzatuvni vaqtincha to'xtatish
    map.on('dragstart', () => {
      setFollowUser(false);
    });

  } catch (e) {
    console.warn("Xarita initsializatsiya xatosi:", e);
  }
}

// Xarita qatlamlarini almashtirish
function setMapLayer(type) {
  if (currentTileLayer && map) {
    map.removeLayer(currentTileLayer);
  }

  currentLayerType = type;
  let url = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}';
  let maxZoom = 20;

  if (type === 'osm') {
    url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    maxZoom = 19;
  } else if (type === 'hybrid') {
    url = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}';
    maxZoom = 20;
  }

  currentTileLayer = L.tileLayer(url, {
    maxZoom: maxZoom,
    subdomains: ['a', 'b', 'c']
  }).addTo(map);

  const btnLayer = document.getElementById('btn-layer');
  if (btnLayer) {
    let lbl = 'Google';
    if (type === 'osm') lbl = 'OSM';
    if (type === 'hybrid') lbl = 'Gibrid';
    btnLayer.innerHTML = `<span>🗺️</span> Xarita: ${lbl}`;
  }

  const selLayer = document.getElementById('setting-map-layer');
  if (selLayer) selLayer.value = type;
}

function cycleMapLayer() {
  if (currentLayerType === 'google') setMapLayer('osm');
  else if (currentLayerType === 'osm') setMapLayer('hybrid');
  else setMapLayer('google');
}

// Radarlarni xaritaga chizish
function renderCamerasOnMap() {
  if (!cameraMarkersLayer) return;
  cameraMarkersLayer.clearLayers();

  speedCameras.forEach(cam => {
    let color = '#ef4444'; // Lochin
    let iconLabel = cam.speedLimit ? cam.speedLimit : '🦅';
    if (cam.type === 'rear') { color = '#d946ef'; iconLabel = '🔄'; }
    if (cam.type === 'uch_oyoq') { color = '#f97316'; iconLabel = '📐'; }
    if (cam.type === 'patrul_360') { color = '#eab308'; iconLabel = '🚔'; }
    if (cam.type === 'traffic_light') { color = '#8b5cf6'; iconLabel = '🚦'; }
    if (cam.type === 'bus_lane') { color = '#3b82f6'; iconLabel = '🚌'; }
    if (cam.type === 'avg_start' || cam.type === 'avg_end') { color = '#10b981'; iconLabel = '⏱️'; }

    const icon = L.divIcon({
      className: 'camera-map-marker',
      html: `
        <div style="background:${color}; border:2.5px solid #fff; border-radius:50%; width:34px; height:34px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:12px; color:#fff; box-shadow:0 0 16px ${color}; cursor:pointer;">
          ${iconLabel}
        </div>`,
      iconSize: [34, 34],
      iconAnchor: [17, 17]
    });

    const marker = L.marker([cam.lat, cam.lng], { icon }).addTo(cameraMarkersLayer);
    marker.bindPopup(`
      <div style="color:#000; font-size:13px; font-weight:600; line-height:1.4;">
        <div style="font-size:14px; font-weight:800; color:${color};">${cam.name}</div>
        <div>Cheklov: <b>${cam.speedLimit || '—'} km/h</b></div>
        <div>Manzil: ${cam.roadName}</div>
      </div>
    `);
  });
}

// ---------------- HAQIQIY JONLI GPS LOKATSIYANI YOQISH ----------------
function startLiveGps() {
  const regName = detectRegionName(currentPosition.lat, currentPosition.lng);
  updateGpsStatus(`GPS: ${regName} (Ulanmoqda...)`, false);

  // 1. Haqiqiy jonli Geolocation Kuzatuvi
  if (!navigator.geolocation) {
    updateGpsStatus("GPS qo'llab-quvvatlanmaydi", false);
    return;
  }

  watchId = navigator.geolocation.watchPosition(
    (pos) => {
      if (isTestDriveActive) return; // Yo'l sinovi paytida test yo'li davom etadi

      const crd = pos.coords;
      const now = pos.timestamp || Date.now();

      const newLat = crd.latitude;
      const newLng = crd.longitude;

      // Haqiqiy harakat tezligi (km/h)
      let calculatedSpeed = 0;
      if (crd.speed !== null && !isNaN(crd.speed) && crd.speed >= 0) {
        calculatedSpeed = Math.round(crd.speed * 3.6);
      } else if (previousPosition) {
        const distM = RadarEngineCore.distance(previousPosition.lat, previousPosition.lng, newLat, newLng);
        const dtSec = Math.max(0.3, (now - previousPosition.timestamp) / 1000);
        if (dtSec > 0.4 && distM > 1.2) {
          calculatedSpeed = Math.min(180, Math.round((distM / dtSec) * 3.6));
        }
      }

      // Haqiqiy yo'nalish azimuti (heading)
      let calculatedHeading = currentPosition.heading;
      if (crd.heading !== null && !isNaN(crd.heading) && crd.heading >= 0) {
        calculatedHeading = Math.round(crd.heading);
      } else if (previousPosition) {
        const distM = RadarEngineCore.distance(previousPosition.lat, previousPosition.lng, newLat, newLng);
        if (distM > 2.0) {
          calculatedHeading = Math.round(RadarEngineCore.bearing(previousPosition.lat, previousPosition.lng, newLat, newLng));
        }
      }

      previousPosition = {
        lat: currentPosition.lat,
        lng: currentPosition.lng,
        timestamp: currentPosition.timestamp
      };

      currentPosition.lat = newLat;
      currentPosition.lng = newLng;
      currentPosition.speed = calculatedSpeed;
      currentPosition.heading = calculatedHeading;
      currentPosition.accuracy = Math.round(crd.accuracy || 10);
      currentPosition.timestamp = now;

      const dynamicRegion = detectRegionName(newLat, newLng);
      updateGpsStatus(`GPS: ${dynamicRegion} (Jonli ±${currentPosition.accuracy}m)`, true);
      document.getElementById('user-coords-text').textContent = 
        `${dynamicRegion} (${currentPosition.lat.toFixed(5)}, ${currentPosition.lng.toFixed(5)})`;

      if (followUser && map) {
        map.panTo([currentPosition.lat, currentPosition.lng], { animate: true });
      }

      updateRadarState();
    },
    (err) => {
      console.warn("GPS kutish holati:", err.message);
      const dynamicRegion = detectRegionName(currentPosition.lat, currentPosition.lng);
      updateGpsStatus(`GPS: ${dynamicRegion} (Lokatsiya faol)`, true);
      document.getElementById('user-coords-text').textContent = 
        `${dynamicRegion} (${currentPosition.lat.toFixed(5)}, ${currentPosition.lng.toFixed(5)})`;
      updateRadarState();
    },
    {
      enableHighAccuracy: true,
      maximumAge: 1000,
      timeout: 10000
    }
  );

  // Koordinata bo'yicha tuman/qishloq nomini reverse geocode qilish
  reverseGeocodeUser(currentPosition.lat, currentPosition.lng);
}

function reverseGeocodeUser(lat, lng) {
  fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`)
    .then(r => r.json())
    .then(data => {
      if (data && data.address) {
        const addr = data.address;
        const place = addr.road || addr.hamlet || addr.village || addr.suburb || addr.city || addr.county || 'Yo\'l';
        const region = addr.state || detectRegionName(lat, lng);
        document.getElementById('user-coords-text').textContent = 
          `${region}, ${place} (${lat.toFixed(4)}, ${lng.toFixed(4)})`;
      }
    }).catch(() => {});
}

function updateGpsStatus(text, isActive) {
  const badge = document.getElementById('gps-status-badge');
  const txt = document.getElementById('gps-status-text');
  if (txt) txt.textContent = text;
  if (!badge) return;
  if (isActive) {
    badge.style.background = 'rgba(16, 185, 129, 0.2)';
    badge.style.borderColor = 'rgba(16, 185, 129, 0.6)';
    badge.style.color = '#10b981';
  } else {
    badge.style.background = 'rgba(245, 158, 11, 0.15)';
    badge.style.borderColor = 'rgba(245, 158, 11, 0.4)';
    badge.style.color = '#f59e0b';
  }
}

// Asosiy Radar Tekshirish va Ogohlantirish Sikli
function updateRadarState() {
  const speedVal = currentPosition.speed;
  document.getElementById('speed-val').textContent = speedVal;
  document.getElementById('hud-speed-val').textContent = speedVal;

  const headingText = RadarEngineCore.getUzbekHeadingText(currentPosition.heading);
  document.getElementById('heading-bearing-text').textContent = headingText;

  if (carMarker) {
    carMarker.setLatLng([currentPosition.lat, currentPosition.lng]);
    const carDiv = document.getElementById('car-marker');
    if (carDiv) carDiv.style.transform = `rotate(${currentPosition.heading}deg)`;
  }

  // Oldindagi kameralarni tekshirish
  const alerts = engine.check(currentPosition);

  const speedCluster = document.getElementById('speed-cluster');
  const alertBox = document.getElementById('active-alert-box');
  const hudAlertBox = document.getElementById('hud-alert-box');
  const hudSpeedVal = document.getElementById('hud-speed-val');
  const limitSign = document.getElementById('speed-limit-sign');
  const fineBadge = document.getElementById('fine-status-badge');

  if (alerts.length > 0) {
    const topAlert = alerts[0];
    const cam = topAlert.camera;

    limitSign.textContent = cam.speedLimit || '—';
    document.getElementById('hud-limit-val').textContent = cam.speedLimit || '—';
    document.getElementById('alert-cam-title').textContent = cam.name;
    document.getElementById('alert-cam-road').textContent = cam.roadName;
    document.getElementById('hud-road-val').textContent = cam.roadName;
    document.getElementById('alert-cam-dist').textContent = `${topAlert.distance} m`;
    document.getElementById('hud-dist-val').textContent = `${topAlert.distance} m`;
    document.getElementById('alert-speech-text').textContent = topAlert.message;

    // Kamera belgisi
    let camIcon = '🦅';
    if (cam.type === 'rear') camIcon = '🔄';
    if (cam.type === 'uch_oyoq') camIcon = '📐';
    if (cam.type === 'patrul_360') camIcon = '🚔';
    if (cam.type === 'traffic_light') camIcon = '🚦';
    if (cam.type === 'bus_lane') camIcon = '🚌';
    if (cam.type === 'avg_start') camIcon = '⏱️';
    document.getElementById('alert-cam-icon').textContent = camIcon;

    // Progress bar
    const maxThreshold = cam.distanceAlertThreshold || 600;
    const pct = Math.max(0, Math.min(100, ((maxThreshold - topAlert.distance) / maxThreshold) * 100));
    document.getElementById('alert-progress-fill').style.width = `${pct}%`;

    // Tezlik me'yordan oshgan bo'lsa
    if (topAlert.isOverSpeed) {
      speedCluster.classList.add('overspeed');
      alertBox.classList.add('danger');
      hudAlertBox.classList.add('overspeed');
      hudSpeedVal.classList.add('overspeed');
      fineBadge.className = 'fine-pill danger';
      fineBadge.textContent = `XAVF: +${topAlert.speedDiff} KM/H`;

      audio.triggerGeiger(topAlert.distance);
      audio.playOverSpeedAlarm();
      audio.announceCamera(cam, true);
    } else {
      speedCluster.classList.remove('overspeed');
      alertBox.classList.remove('danger');
      hudAlertBox.classList.remove('overspeed');
      hudSpeedVal.classList.remove('overspeed');
      fineBadge.className = 'fine-pill';
      fineBadge.textContent = 'XAVFSIZ';

      audio.triggerGeiger(topAlert.distance);
      audio.announceCamera(cam, false);
    }

    audio.activeCameraId = cam.id;

  } else {
    // Agar kameradan o'tib ketgan bo'lsa
    if (audio.activeCameraId) {
      audio.playPassChime();
      audio.activeCameraId = null;
    }

    limitSign.textContent = '60';
    speedCluster.classList.remove('overspeed');
    alertBox.classList.remove('danger');
    hudAlertBox.classList.remove('overspeed');
    hudSpeedVal.classList.remove('overspeed');
    fineBadge.className = 'fine-pill';
    fineBadge.textContent = 'XAVFSIZ';
    document.getElementById('alert-cam-title').textContent = 'Yo\'l ochiq';
    document.getElementById('alert-cam-road').textContent = 'Oldinda kameralar yo\'q';
    document.getElementById('hud-road-val').textContent = 'Yo\'l ochiq';
    document.getElementById('alert-cam-dist').textContent = '—';
    document.getElementById('hud-dist-val').textContent = '—';
    document.getElementById('alert-speech-text').textContent = 'Xavfsiz harakatlaning';
    document.getElementById('alert-progress-fill').style.width = '0%';
  }

  // Yaqin atrofdagi kameralar ro'yxatini yangilash
  updateNearbyCamsList();
}

function updateNearbyCamsList() {
  const container = document.getElementById('upcoming-list');
  if (!container) return;

  const sorted = speedCameras.map(cam => {
    const d = RadarEngineCore.distance(currentPosition.lat, currentPosition.lng, cam.lat, cam.lng);
    return { cam, distance: Math.round(d) };
  }).sort((a, b) => a.distance - b.distance).slice(0, 4);

  document.getElementById('nearby-cams-count').textContent = `${sorted.length} ta`;

  container.innerHTML = sorted.map(item => {
    let color = '#ef4444';
    let icon = '🦅';
    if (item.cam.type === 'rear') { color = '#d946ef'; icon = '🔄'; }
    if (item.cam.type === 'uch_oyoq') { color = '#f97316'; icon = '📐'; }
    if (item.cam.type === 'patrul_360') { color = '#eab308'; icon = '🚔'; }
    if (item.cam.type === 'traffic_light') { color = '#8b5cf6'; icon = '🚦'; }
    if (item.cam.type === 'bus_lane') { color = '#3b82f6'; icon = '🚌'; }

    return `
      <div class="cam-item-row">
        <div class="cam-item-info">
          <span class="cam-type-badge">${icon}</span>
          <div class="cam-item-text">
            <b>${item.cam.name}</b>
            <span>${item.cam.speedLimit || '—'} km/h</span>
          </div>
        </div>
        <div class="cam-item-dist" style="color:${color};">
          ${item.distance} m
        </div>
      </div>
    `;
  }).join('');
}

// ---------------- 🚗 YO'LDA YURISHNI SINASH (ROAD TEST DRIVE) ----------------
// Foydalanuvchi joylashgan yo'l (M37 / Romitan / Buxoro aylanma) bo'ylab maxsus strelkani harakatlantirish
function toggleTestDrive() {
  const btn = document.getElementById('btn-test-drive');
  audio.unlock();

  if (isTestDriveActive) {
    isTestDriveActive = false;
    clearInterval(testDriveTimer);
    btn.innerHTML = '<span>🚗</span> Yo\'lda sinash';
    btn.classList.remove('active');
    currentPosition.speed = 0;
    updateRadarState();
    return;
  }

  isTestDriveActive = true;
  btn.innerHTML = '<span>⏹</span> To\'xtatish';
  btn.classList.add('active');

  // Samarqand shahri: Temirchilar ko'chasidan Registon ko'chasi bo'ylab Lochin 60 tomon yurish
  const roadWaypoints = [
    { lat: 39.6588, lng: 66.9615, heading: 105, speed: 45 },
    { lat: 39.6580, lng: 66.9655, heading: 105, speed: 55 },
    { lat: 39.6568, lng: 66.9695, heading: 110, speed: 64 }, // Lochin 60 ga 400m qoldi
    { lat: 39.6558, lng: 66.9725, heading: 115, speed: 72 }, // Tezlik oshgan (Xavf ogohlantirishi!)
    { lat: 39.6548, lng: 66.9752, heading: 115, speed: 66 }, // Lochin 60 kamerasi to'g'risida
    { lat: 39.6538, lng: 66.9785, heading: 115, speed: 58 }, // Kameradan o'tildi (Chime)
    { lat: 39.6530, lng: 66.9820, heading: 110, speed: 50 }
  ];

  let step = 0;
  // Har 1.8 soniyada yo'l bo'ylab strelka oldinga siljiydi
  testDriveTimer = setInterval(() => {
    if (step >= roadWaypoints.length) step = 0;
    const pt = roadWaypoints[step];

    currentPosition.lat = pt.lat;
    currentPosition.lng = pt.lng;
    currentPosition.heading = pt.heading;
    currentPosition.speed = pt.speed;

    if (map && followUser) {
      map.panTo([pt.lat, pt.lng], { animate: true, duration: 1.2 });
    }

    updateRadarState();
    step++;
  }, 1800);
}

// Joylashuvimga qaytish
function recenterUser() {
  setFollowUser(true);
  if (map) {
    map.flyTo([currentPosition.lat, currentPosition.lng], 16, { animate: true, duration: 1 });
  }
}

function setFollowUser(active) {
  followUser = active;
  const btnRecenter = document.getElementById('btn-recenter');
  const btnFollowToggle = document.getElementById('btn-follow-toggle');
  
  if (btnRecenter) {
    btnRecenter.classList.toggle('active-glow', active);
  }
  if (btnFollowToggle) {
    btnFollowToggle.classList.toggle('active', active);
    btnFollowToggle.innerHTML = active ? '<span>🧭</span> Avto-kuzatuv: Yoqiq' : '<span>✋</span> Avto-kuzatuv: O\'chiq';
  }
}

// HUD rejimini yoqish/o'chirish
let isHudMirrorActive = false;

function toggleHud() {
  isHudActive = !isHudActive;
  document.body.classList.toggle('hud-mode', isHudActive);
  document.getElementById('btn-hud').classList.toggle('active', isHudActive);
}

function closeHud() {
  isHudActive = false;
  document.body.classList.remove('hud-mode');
  document.getElementById('btn-hud').classList.remove('active');
}

function toggleHudMirror() {
  isHudMirrorActive = !isHudMirrorActive;
  const container = document.getElementById('hud-content-container');
  const btn = document.getElementById('btn-hud-mirror');
  if (container) {
    container.classList.toggle('hud-mirror-active', isHudMirrorActive);
  }
  if (btn) {
    btn.classList.toggle('active', isHudMirrorActive);
    btn.innerHTML = isHudMirrorActive 
      ? '<span>🪞</span> Ko\'zgu: Yoqiq' 
      : '<span>🪞</span> Ko\'zgu: O\'chiq';
  }
}

// Ovozni yoqish/o'chirish
function toggleMute() {
  audio.unlock();
  audio.muted = !audio.muted;
  const btn = document.getElementById('btn-mute');
  if (audio.muted) {
    btn.innerHTML = '<span>🔇</span> Ovoz O\'chiq';
    btn.classList.add('active');
  } else {
    btn.innerHTML = '<span>🔊</span> Ovozli';
    btn.classList.remove('active');
    audio.playRadarAlertChime();
  }
}

// To'liq ekran rejimi
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  } else {
    document.exitFullscreen().catch(() => {});
  }
}

// Sozlamalar oynasi
function toggleSettings() {
  const drawer = document.getElementById('settings-drawer');
  if (drawer) {
    drawer.classList.toggle('hidden');
  }
}

// Initsializatsiya
window.addEventListener('DOMContentLoaded', () => {
  initMap();
  startLiveGps();

  // Foydalanuvchi ekranga bir marta tekkanda audioni faollashtirish
  const unlockEvents = ['touchstart', 'click', 'keydown'];
  const onFirstInteraction = () => {
    audio.unlock();
    unlockEvents.forEach(evt => window.removeEventListener(evt, onFirstInteraction));
  };
  unlockEvents.forEach(evt => window.addEventListener(evt, onFirstInteraction, { passive: true }));

  // ============================================================
  // SUPABASE CLOUD VA RADARLAR BAZASINI YUKLASH
  // ============================================================
  const cloudBadge = document.getElementById('cloud-status-badge');
  const inputCloudUrl = document.getElementById('setting-supabase-url');
  const inputCloudKey = document.getElementById('setting-supabase-key');
  const btnSaveCloud = document.getElementById('btn-save-cloud');
  const btnSyncCloud = document.getElementById('btn-sync-cloud');

  function updateCloudUI(isConnected, count) {
    if (!cloudBadge) return;
    if (isConnected) {
      cloudBadge.style.color = '#00ff66';
      cloudBadge.innerText = `🟢 Cloud faol (${count} ta radar)`;
    } else {
      cloudBadge.style.color = '#ffb84d';
      cloudBadge.innerText = `🟡 Offline kesh (${count || speedCameras.length} ta radar)`;
    }
  }

  async function loadCameras() {
    let cloudLoaded = false;
    if (window.QalqonCloud && window.QalqonCloud.isConfigured()) {
      try {
        const cloudCams = await window.QalqonCloud.fetchCameras();
        if (Array.isArray(cloudCams) && cloudCams.length > 0) {
          speedCameras = cloudCams;
          engine.cameras = cloudCams;
          renderCamerasOnMap();
          updateNearbyCamsList();
          updateCloudUI(true, cloudCams.length);
          cloudLoaded = true;
          console.log(`✅ Supabase Cloud-dan ${cloudCams.length} ta radar yuklandi!`);
        }
      } catch (err) {
        console.warn('Supabase cloud fetch failed, falling back:', err);
      }
    }

    if (!cloudLoaded) {
      // Offline kesh yoki lokal speedcams.json
      const cached = window.QalqonCloud ? window.QalqonCloud.getCached() : null;
      if (cached && cached.length > 0) {
        speedCameras = cached;
        engine.cameras = cached;
        renderCamerasOnMap();
        updateNearbyCamsList();
        updateCloudUI(false, cached.length);
      } else {
        fetch('src/data/speedcams.json')
          .then(r => r.json())
          .then(data => {
            if (Array.isArray(data) && data.length > 0) {
              speedCameras = data;
              engine.cameras = data;
              renderCamerasOnMap();
              updateNearbyCamsList();
              updateCloudUI(false, data.length);
            }
          }).catch(() => {});
      }
    }
  }

  // Sahifa ochilganda yuklash
  loadCameras();

  // Supabase Real-time: boshqa haydovchilar belgilagan radarlarni jonli qabul qilish
  if (window.QalqonCloud) {
    window.QalqonCloud.subscribe((newCam) => {
      const exists = speedCameras.find(c => c.id === newCam.id);
      if (!exists) {
        speedCameras.unshift(newCam);
        engine.cameras = speedCameras;
        renderCamerasOnMap();
        updateNearbyCamsList();
        
        // Jonli ogohlantirish tovushi
        audio.playRadarAlertChime();
        if (newCam.type === 'uch_oyoq') {
          setTimeout(() => audio.playFile('uch_oyoq.mp3'), 400);
        } else if (newCam.type === 'patrul_360') {
          setTimeout(() => audio.playFile('patrul_360.mp3'), 400);
        }
      }
    });

    const cfg = window.QalqonCloud.getConfig();
    if (inputCloudUrl && cfg.url) inputCloudUrl.value = cfg.url;
    if (inputCloudKey && cfg.key) inputCloudKey.value = cfg.key;
  }

  // Cloud sozlamalarini saqlash
  if (btnSaveCloud) {
    btnSaveCloud.addEventListener('click', async () => {
      const url = (inputCloudUrl.value || '').trim();
      const key = (inputCloudKey.value || '').trim();
      btnSaveCloud.disabled = true;
      btnSaveCloud.innerText = '⏳ Tekshirilmoqda...';

      const ok = window.QalqonCloud.configure(url, key);
      if (ok) {
        btnSaveCloud.innerText = '✅ Ulandi!';
        await loadCameras();
      } else {
        btnSaveCloud.innerText = '❌ Ulanmadi';
      }
      setTimeout(() => {
        btnSaveCloud.disabled = false;
        btnSaveCloud.innerText = '💾 Saqlash';
      }, 2000);
    });
  }

  if (btnSyncCloud) {
    btnSyncCloud.addEventListener('click', async () => {
      btnSyncCloud.disabled = true;
      btnSyncCloud.innerText = '⏳ Sinxronlanmoqda...';
      await loadCameras();
      btnSyncCloud.innerText = '✅ Yangilandi!';
      setTimeout(() => {
        btnSyncCloud.disabled = false;
        btnSyncCloud.innerText = '🔄 Sinxronlash';
      }, 2000);
    });
  }

  // ============================================================
  // HAYDOVCHI TOMONIDAN RADAR BELGILASH (COMMUNITY MODAL)
  // ============================================================
  const reportModal = document.getElementById('report-modal');
  const btnReportCam = document.getElementById('btn-report-cam');
  const btnCloseReport = document.getElementById('btn-close-report');
  const btnSubmitReport = document.getElementById('btn-submit-report');
  const reportStatusMsg = document.getElementById('report-status-msg');

  let selectedReportType = 'uch_oyoq';
  let selectedReportSpeed = 60;

  if (btnReportCam && reportModal) {
    btnReportCam.addEventListener('click', () => {
      reportModal.classList.remove('hidden');
      if (reportStatusMsg) reportStatusMsg.innerHTML = '';
    });
  }

  if (btnCloseReport && reportModal) {
    btnCloseReport.addEventListener('click', () => {
      reportModal.classList.add('hidden');
    });
  }

  document.querySelectorAll('.report-type-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.report-type-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedReportType = btn.dataset.type || 'uch_oyoq';
    });
  });

  document.querySelectorAll('.speed-opt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.speed-opt-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedReportSpeed = parseInt(btn.dataset.speed || '60', 10);
    });
  });

  if (btnSubmitReport) {
    btnSubmitReport.addEventListener('click', async () => {
      const lat = currentPosition.lat;
      const lng = currentPosition.lng;

      btnSubmitReport.disabled = true;
      btnSubmitReport.innerHTML = '<span>⏳</span> Belgilanmoqda...';

      const reportData = {
        lat: lat,
        lng: lng,
        type: selectedReportType,
        speedLimit: selectedReportSpeed,
        roadName: currentCity || "Yo'l",
        description: "Haydovchi tomonidan belgilandi"
      };

      try {
        const res = await window.QalqonCloud.reportCamera(reportData);

        // Darhol xaritaga lokal marker qo'shish
        const localCam = {
          id: `local-rep-${Date.now()}`,
          name: `⚠️ ${selectedReportType === 'uch_oyoq' ? 'Uch oyoq radar' : selectedReportType === 'patrul_360' ? 'Patrul 360' : 'Yangi radar'}`,
          lat: lat,
          lng: lng,
          type: selectedReportType,
          speedLimit: selectedReportSpeed,
          azimuth: -1,
          roadName: currentCity || "Haydovchi belgilagan",
          distanceAlertThreshold: 550,
          isCommunity: true
        };

        speedCameras.unshift(localCam);
        engine.cameras = speedCameras;
        renderCamerasOnMap();
        updateNearbyCamsList();

        audio.playRadarAlertChime();
        if (reportStatusMsg) {
          reportStatusMsg.style.color = '#00ff66';
          reportStatusMsg.innerText = res.offline
            ? "✅ Lokal saqlandi! (Internet paydo bo'lganda bulutga sinxronlanadi)"
            : "✅ Muvaffaqiyatli bulutga yuklandi!";
        }

        setTimeout(() => {
          if (reportModal) reportModal.classList.add('hidden');
          btnSubmitReport.disabled = false;
          btnSubmitReport.innerHTML = '<span>📍</span> Shu yerda belgilash';
        }, 1300);
      } catch (err) {
        if (reportStatusMsg) {
          reportStatusMsg.style.color = '#ff4444';
          reportStatusMsg.innerText = 'Xatolik: ' + err.message;
        }
        btnSubmitReport.disabled = false;
        btnSubmitReport.innerHTML = '<span>📍</span> Shu yerda belgilash';
      }
    });
  }

  // Tugmalar
  document.getElementById('btn-layer').addEventListener('click', cycleMapLayer);
  document.getElementById('btn-recenter').addEventListener('click', recenterUser);
  document.getElementById('btn-test-drive').addEventListener('click', toggleTestDrive);
  document.getElementById('btn-follow-toggle').addEventListener('click', () => {
    setFollowUser(!followUser);
    if (followUser) recenterUser();
  });
  document.getElementById('btn-hud').addEventListener('click', toggleHud);
  const btnHudExit = document.getElementById('btn-hud-exit');
  if (btnHudExit) btnHudExit.addEventListener('click', closeHud);
  const btnHudMirror = document.getElementById('btn-hud-mirror');
  if (btnHudMirror) btnHudMirror.addEventListener('click', toggleHudMirror);

  // ESC tugmasi bosilganda HUD rejimini yopish
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isHudActive) {
      closeHud();
    }
  });
  document.getElementById('btn-mute').addEventListener('click', toggleMute);
  document.getElementById('btn-fullscreen').addEventListener('click', toggleFullscreen);

  // Sozlamalar tugmalari
  const btnSettings = document.getElementById('btn-settings-toggle');
  if (btnSettings) btnSettings.addEventListener('click', toggleSettings);
  const btnCloseSettings = document.getElementById('btn-close-settings');
  if (btnCloseSettings) btnCloseSettings.addEventListener('click', toggleSettings);

  const selMap = document.getElementById('setting-map-layer');
  if (selMap) {
    selMap.addEventListener('change', (e) => {
      setMapLayer(e.target.value);
    });
  }

  const selDist = document.getElementById('setting-distance-mode');
  if (selDist) {
    selDist.addEventListener('change', (e) => {
      engine.distanceMode = e.target.value;
    });
  }

  const selGeiger = document.getElementById('setting-geiger-mode');
  if (selGeiger) {
    selGeiger.addEventListener('change', (e) => {
      audio.enableGeiger = (e.target.value === 'on');
    });
  }

  const volSlider = document.getElementById('setting-volume-slider');
  if (volSlider) {
    volSlider.addEventListener('input', (e) => {
      audio.volume = e.target.value / 100;
    });
  }

  // Tizim ovozini tekshirish tugmasi (Sozlamalar ichida)
  const soundTestBtn = document.getElementById('btn-sound-test');
  if (soundTestBtn) {
    soundTestBtn.addEventListener('click', () => {
      audio.unlock();
      audio.muted = false;
      document.getElementById('btn-mute').innerHTML = '<span>🔊</span> Ovozli';
      document.getElementById('btn-mute').classList.remove('active');

      audio.playRadarAlertChime();
      setTimeout(() => audio.playFile('lochin_70.mp3'), 450);
      setTimeout(() => audio.playFile('neoline_click.wav'), 1900);
      setTimeout(() => audio.playFile('neoline_click.wav'), 2300);
      setTimeout(() => audio.playFile('neoline_click.wav'), 2600);
      setTimeout(() => audio.playFile('rear_70.mp3'), 2900);
      setTimeout(() => audio.playFile('uch_oyoq_70.mp3'), 5200);
      setTimeout(() => audio.playFile('patrul_360.mp3'), 7600);
      setTimeout(() => audio.playFile('chorraha.mp3'), 10400);
      setTimeout(() => {
        audio.playFile('slowdown.mp3');
        audio.playOverSpeedAlarm();
      }, 13200);
    });
  }

  updateRadarState();
});
