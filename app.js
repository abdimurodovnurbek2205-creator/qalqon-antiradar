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
function createKeepAliveWavBlobUrl(durationSeconds = 15) {
  const sampleRate = 8000;
  const numSamples = sampleRate * durationSeconds;
  const dataSize = numSamples * 2;
  const buffer = new ArrayBuffer(44 + dataSize);
  const view = new DataView(buffer);

  const writeStr = (offset, str) => {
    for (let i = 0; i < str.length; i++) {
      view.setUint8(offset + i, str.charCodeAt(i));
    }
  };

  writeStr(0, 'RIFF');
  view.setUint32(4, 36 + dataSize, true);
  writeStr(8, 'WAVE');
  writeStr(12, 'fmt ');
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * 2, true);
  view.setUint16(32, 2, true);
  view.setUint16(34, 16, true);
  writeStr(36, 'data');
  view.setUint32(40, dataSize, true);

  // Inson qulog'iga eshitilmaydigan (-80dB), lekin Android MediaSession qulf ekranida
  // haqiqiy pleer sifatida ko'rsatishi uchun 15 soniyalik uzluksiz mikro-signal
  for (let i = 0; i < numSamples; i++) {
    const sample = (i % 2 === 0) ? 2 : -2;
    view.setInt16(44 + i * 2, sample, true);
  }

  const blob = new Blob([buffer], { type: 'audio/wav' });
  return URL.createObjectURL(blob);
}

class AudioCore {
  constructor() {
    this.muted = false;
    this.volume = 1.0;
    this.enableGeiger = true;
    this.audioCache = {};
    this.activeAudios = new Set();
    this.testTimeouts = [];
    this.lastGeigerTime = 0;
    this.lastSpokenKey = '';
    this.lastVoiceTime = 0;
    this.lastOverSpeedAlarmTime = 0;
    this.activeCameraId = null;
    this.unlocked = false;
    this.isExiting = false;
    this.keepAliveAudio = null;
    this.keepAliveBlobUrl = null;

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
    if (!this.unlocked) {
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

    // Har safar ekran bosilganda orqa fon audio va PiP video oqimi uyg'oq ekanini tekshirish
    this.startBackgroundKeepAlive();
    if (typeof PipManager !== 'undefined') {
      PipManager.ensureMediaReady();
    }
    if ('Notification' in window && Notification.permission === 'default') {
      Notification.requestPermission().catch(() => {});
    }
  }

  startBackgroundKeepAlive() {
    if (this.isExiting) return;
    try {
      if (!this.keepAliveAudio) {
        this.keepAliveBlobUrl = createKeepAliveWavBlobUrl(15);
        this.keepAliveAudio = new Audio(this.keepAliveBlobUrl);
        this.keepAliveAudio.loop = true;
        // Volume 0.85 bo'lishi shart (ovozning o'zi -80dB jimjit), shunda Android Qulf Ekranida vidjet chiqaradi!
        this.keepAliveAudio.volume = 0.85;
        this.keepAliveAudio.muted = false;

        // Telefon qulflanganda OS audioni pauza qilmoqchi bo'lsa, darhol qayta yoqish
        this.keepAliveAudio.addEventListener('pause', () => {
          if (!this.isExiting && document.visibilityState === 'hidden') {
            this.keepAliveAudio.play().catch(() => {});
          }
        });

        // Orqa fonda va ekran qulfida har 250ms da ishlaydigan taymer (GPS, PiP va LockScreen uchun)
        this.keepAliveAudio.addEventListener('timeupdate', () => {
          if (typeof PipManager !== 'undefined') {
            PipManager.draw();
            if (PipManager.video && PipManager.video.paused && !PipManager.isPaused && !this.isExiting) {
              PipManager.video.play().catch(() => {});
            }
          }
          if (typeof currentPosition !== 'undefined' && typeof engine !== 'undefined') {
            const spd = currentPosition.speed || 0;
            const al = engine.check(currentPosition);
            updateLockScreenStatus(spd, al.length > 0 ? al[0] : null, false);
          }
        });
      }

      if (this.keepAliveAudio.paused) {
        this.keepAliveAudio.play().then(() => {
          console.log('✅ 15s Qulf ekrani (LockScreen) audio oqimi faol');
          if (typeof currentPosition !== 'undefined' && typeof engine !== 'undefined') {
            const spd = currentPosition.speed || 0;
            const al = engine.check(currentPosition);
            updateLockScreenStatus(spd, al.length > 0 ? al[0] : null, true);
          }
        }).catch(() => {});
      }
    } catch (e) {
      console.warn('Keepalive audio xatosi:', e);
    }
  }

  stopKeepAlive() {
    this.isExiting = true;
    if (this.keepAliveAudio) {
      try {
        this.keepAliveAudio.pause();
        this.keepAliveAudio.src = '';
      } catch (e) {}
      this.keepAliveAudio = null;
    }
  }

  stopAll() {
    // 1. Rejalashtirilgan sinov taymerlarini bekor qilish
    if (this.testTimeouts && this.testTimeouts.length > 0) {
      this.testTimeouts.forEach(t => clearTimeout(t));
      this.testTimeouts = [];
    }

    // 2. Ayni paytda chalinayotgan barcha audio nusxalarni to'xtatish
    if (this.activeAudios) {
      this.activeAudios.forEach(a => {
        try {
          a.pause();
          a.currentTime = 0;
        } catch (e) {}
      });
      this.activeAudios.clear();
    }

    // 3. Keshdagi tovushlarni ham to'xtatish (lekin keepAliveAudio o'chirilmaydi!)
    Object.values(this.audioCache).forEach(a => {
      try {
        a.pause();
        a.currentTime = 0;
      } catch (e) {}
    });

    // 4. Test tugmasining holatini tiklash
    const soundTestBtn = document.getElementById('btn-sound-test');
    if (soundTestBtn) {
      soundTestBtn.innerHTML = '<span>⚡</span> Ovozni sinash';
      soundTestBtn.classList.remove('active');
    }
  }

  playFile(filename, volMultiplier = 1.0) {
    if (this.muted) return;
    try {
      const src = this.audioCache[filename];
      if (src) {
        const clone = src.cloneNode();
        clone.volume = Math.max(0, Math.min(1.0, this.volume * volMultiplier));
        if (this.activeAudios) {
          this.activeAudios.add(clone);
          const cleanup = () => {
            if (this.activeAudios) this.activeAudios.delete(clone);
          };
          clone.addEventListener('ended', cleanup, { once: true });
          clone.addEventListener('pause', cleanup, { once: true });
        }
        clone.play().catch(() => {
          if (this.activeAudios) this.activeAudios.delete(clone);
        });
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

// ============================================================
// ⚡ EKRAN DOIMO YONIQ VA ORQA FONDA ISHLASH (WAKE LOCK ENGINE)
// ============================================================
const WakeLockEngine = {
  sentinel: null,
  isWanted: true,

  async request() {
    this.isWanted = true;

    // Zamonaviy Screen Wake Lock API (Chrome, Safari 16.4+, Edge, Samsung Internet)
    if ('wakeLock' in navigator) {
      try {
        if (!this.sentinel || this.sentinel.released) {
          this.sentinel = await navigator.wakeLock.request('screen');
          this.sentinel.addEventListener('release', () => {
            console.log('⚡ WakeLock vaqtincha bo\'shatildi');
            this.updateUi();
          });
          console.log('✅ Ekran doimo yoniq (WakeLock faol)');
        }
      } catch (err) {
        console.warn('WakeLock ogohlantirish:', err.message);
      }
    }
    this.updateUi();
  },

  release() {
    this.isWanted = false;
    if (this.sentinel) {
      this.sentinel.release().catch(() => {});
      this.sentinel = null;
    }
    this.updateUi();
  },

  toggle() {
    if (this.isWanted && this.isActive()) {
      this.release();
    } else {
      this.request();
    }
  },

  isActive() {
    return Boolean(this.sentinel && !this.sentinel.released);
  },

  updateUi() {
    const active = this.isWanted;
    const btn = document.getElementById('btn-wakelock');
    if (btn) {
      btn.classList.toggle('active', active);
      btn.innerHTML = active ? '<span>⚡</span> Ekran: Yoniq' : '<span>💤</span> Ekran: Oddiy';
      btn.title = active ? "Ekran o‘chmaydi (Doimo yoniq)" : "Ekran telefon vaqti bilan o‘chishi mumkin";
    }
    const sel = document.getElementById('setting-wakelock-mode');
    if (sel) {
      sel.value = active ? 'always' : 'system';
    }
  }
};

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
let hasHadFirstGpsFix = false;

function startLiveGps() {
  if (typeof WakeLockEngine !== 'undefined') {
    WakeLockEngine.request();
  }
  if (audio && audio.unlocked) {
    audio.startBackgroundKeepAlive();
  }

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

      if (!hasHadFirstGpsFix) {
        hasHadFirstGpsFix = true;
        if (map) {
          map.setView([currentPosition.lat, currentPosition.lng], 16);
        }
      } else if (followUser && map) {
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
  const topAlert = alerts.length > 0 ? alerts[0] : null;

  const speedCluster = document.getElementById('speed-cluster');
  const alertBox = document.getElementById('active-alert-box');
  const hudAlertBox = document.getElementById('hud-alert-box');
  const hudSpeedVal = document.getElementById('hud-speed-val');
  const limitSign = document.getElementById('speed-limit-sign');
  const fineBadge = document.getElementById('fine-status-badge');

  if (topAlert) {
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

  // Suzuvchi vidjet va PiP oynasini harakat davomida yangilash
  if (typeof FloatingWidget !== 'undefined') {
    FloatingWidget.update();
  }
  if (typeof PipManager !== 'undefined' && PipManager.isActive) {
    PipManager.draw();
  }

  // Telefon qulflanganda qulf ekranidagi MediaSession va Bildirishnomani yangilash
  const currentSpeed = (currentPosition && currentPosition.speed) ? currentPosition.speed : 0;
  updateLockScreenStatus(currentSpeed, topAlert, false);
}

let lastLockUpdateTime = 0;
let lastLockSpeed = -1;
let lastLockAlertId = '';
let lastNotifyTime = 0;

function updateLockScreenStatus(speed, topAlert, forceUpdate = false) {
  const now = Date.now();
  const alertId = topAlert && topAlert.camera ? `${topAlert.camera.id}-${Math.floor(topAlert.distance / 15)}` : 'clear';

  if (!forceUpdate && speed === lastLockSpeed && alertId === lastLockAlertId && (now - lastLockUpdateTime < 2200)) {
    return;
  }

  lastLockUpdateTime = now;
  lastLockSpeed = speed;
  lastLockAlertId = alertId;

  let title = `🛡️ QALQON: ${speed} KM/S — Yo'l ochiq`;
  let artist = "Cheklov: 60 km/s • Jonli GPS va Ovozli Himoya Faol";
  let album = "Qalqon Antiradar O'zbekiston";
  let isDanger = false;

  if (topAlert && topAlert.camera) {
    const cam = topAlert.camera;
    isDanger = Boolean(topAlert.isOverSpeed);
    const warn = isDanger ? `🚨 XAVF +${topAlert.speedDiff} KM/S` : `⚠️ RADAR ${topAlert.distance}m`;
    title = `${warn} | ${cam.name}`;
    artist = `Tezlik: ${speed} km/s (Cheklov: ${cam.speedLimit} km/s) • ${topAlert.distance} metr`;
    album = cam.roadName || "O'zbekiston yo'llari";
  }

  // 1. Android Qulf Ekrani (Lock Screen) MediaSession Pleyer Vidjeti (Jonli Spidometr rasmi bilan!)
  if ('mediaSession' in navigator) {
    try {
      if (typeof PipManager !== 'undefined') {
        PipManager.draw();
      }
      const artworkList = [];
      if (typeof PipManager !== 'undefined' && PipManager.canvas) {
        try {
          const livePng = PipManager.canvas.toDataURL('image/png');
          artworkList.push({ src: livePng, sizes: '360x360', type: 'image/png' });
        } catch (e) {}
      }
      const icon192 = new URL('./icon-192.png', window.location.href).href;
      const icon512 = new URL('./icon-512.png', window.location.href).href;
      artworkList.push({ src: icon192, sizes: '192x192', type: 'image/png' });
      artworkList.push({ src: icon512, sizes: '512x512', type: 'image/png' });

      navigator.mediaSession.metadata = new MediaMetadata({
        title: title,
        artist: artist,
        album: album,
        artwork: artworkList
      });
      navigator.mediaSession.playbackState = 'playing';
    } catch (e) {}
  }

  // 2. Android Qulf Ekrani va Yuqori Panel (Status Bar) Tizim Bildirishnomasi
  if (forceUpdate || document.visibilityState === 'hidden' || (topAlert && (now - lastNotifyTime > 3500))) {
    lastNotifyTime = now;
    if ('serviceWorker' in navigator && 'Notification' in window && Notification.permission === 'granted') {
      navigator.serviceWorker.ready.then((reg) => {
        if (reg.active) {
          reg.active.postMessage({
            type: 'QALQON_LOCKSCREEN_NOTIFY',
            title: title,
            body: artist,
            isDanger: isDanger
          });
        } else if (reg.showNotification) {
          reg.showNotification(title, {
            body: artist,
            icon: './icon-192.png',
            badge: './icon-192.png',
            tag: 'qalqon-lockscreen-widget',
            renotify: isDanger,
            silent: !isDanger,
            requireInteraction: true
          }).catch(() => {});
        }
      }).catch(() => {});
    }
  }
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

// ============================================================
// 📌 PICTURE-IN-PICTURE VA QULF EKRANIDAN KEYIN YO'QOLMAYDIGAN MINI-OYNA
// ============================================================
function roundRect(ctx, x, y, width, height, radius, fill, stroke) {
  ctx.beginPath();
  ctx.moveTo(x + radius, y);
  ctx.lineTo(x + width - radius, y);
  ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
  ctx.lineTo(x + width, y + height - radius);
  ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
  ctx.lineTo(x + radius, y + height);
  ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
  ctx.lineTo(x, y + radius);
  ctx.quadraticCurveTo(x, y, x + radius, y);
  ctx.closePath();
  if (fill) ctx.fill();
  if (stroke) ctx.stroke();
}

function makeDraggable(el) {
  let isDragging = false;
  let startX = 0, startY = 0, initialLeft = 0, initialTop = 0;

  const onStart = (e) => {
    if (e.target.closest && e.target.closest('button')) return;
    if (e.target.tagName === 'BUTTON') return;
    isDragging = true;
    const touch = e.touches ? e.touches[0] : e;
    startX = touch.clientX;
    startY = touch.clientY;
    const rect = el.getBoundingClientRect();
    initialLeft = rect.left;
    initialTop = rect.top;
  };

  const onMove = (e) => {
    if (!isDragging) return;
    if (e.cancelable) e.preventDefault();
    const touch = e.touches ? e.touches[0] : e;
    const dx = touch.clientX - startX;
    const dy = touch.clientY - startY;
    const maxX = Math.max(8, window.innerWidth - el.offsetWidth - 8);
    const maxY = Math.max(8, window.innerHeight - el.offsetHeight - 8);
    const newX = Math.max(8, Math.min(maxX, initialLeft + dx));
    const newY = Math.max(8, Math.min(maxY, initialTop + dy));
    el.style.left = `${newX}px`;
    el.style.top = `${newY}px`;
    el.style.right = 'auto';
    el.style.bottom = 'auto';
  };

  const onEnd = () => {
    isDragging = false;
  };

  el.addEventListener('mousedown', onStart);
  window.addEventListener('mousemove', onMove);
  window.addEventListener('mouseup', onEnd);

  el.addEventListener('touchstart', onStart, { passive: true });
  window.addEventListener('touchmove', onMove, { passive: false });
  window.addEventListener('touchend', onEnd);
}

const FloatingWidget = {
  el: null,
  isPaused: false,
  isVisible: false,
  userWanted: true, // Standart holatda faol — telefon qulfdan chiqqanda doimo ko'rinib turadi!

  init() {
    this.el = document.getElementById('floating-square-widget');
    if (!this.el) return;

    makeDraggable(this.el);

    const btnClose = document.getElementById('btn-fsw-close');
    if (btnClose) {
      btnClose.addEventListener('click', (e) => {
        e.stopPropagation();
        this.userWanted = false;
        this.hide();
        if (typeof PipManager !== 'undefined') {
          PipManager.exit();
        }
      });
    }

    const btnPause = document.getElementById('btn-fsw-pause');
    if (btnPause) {
      btnPause.addEventListener('click', (e) => {
        e.stopPropagation();
        this.togglePause();
      });
    }
  },

  syncVisibility() {
    if (!this.el) return;
    const osPipOpen = Boolean(document.pictureInPictureElement);
    if (this.userWanted && !osPipOpen) {
      this.isVisible = true;
      this.el.classList.remove('hidden');
      this.update();
    } else if (osPipOpen) {
      // OS PiP ochiqligida ikkita ustma-ust oyna bo'lmasligi uchun ichkisi vaqtincha yashirin turadi,
      // lekin qulfga tushib OS PiP yopilishi bilan darhol avtomatik chiqadi!
      this.el.classList.add('hidden');
    } else {
      this.isVisible = false;
      this.el.classList.add('hidden');
    }
    if (typeof PipManager !== 'undefined') {
      PipManager.updateButtons(this.userWanted || osPipOpen);
    }
  },

  show() {
    if (!this.el) return;
    this.userWanted = true;
    this.isVisible = true;
    this.syncVisibility();
  },

  hide() {
    if (!this.el) return;
    this.userWanted = false;
    this.isVisible = false;
    this.el.classList.add('hidden');
    if (typeof PipManager !== 'undefined') {
      PipManager.updateButtons(false);
    }
  },

  toggle() {
    if (this.userWanted) this.hide();
    else this.show();
  },

  togglePause() {
    this.isPaused = !this.isPaused;
    audio.muted = this.isPaused;
    if (this.isPaused) {
      audio.stopAll();
    }
    const btnPause = document.getElementById('btn-fsw-pause');
    if (btnPause) {
      btnPause.textContent = this.isPaused ? '▶️' : '⏸️';
    }
    if (this.el) {
      this.el.classList.toggle('paused', this.isPaused);
    }
    if (typeof PipManager !== 'undefined') {
      PipManager.setPaused(this.isPaused);
    }
    this.update();
  },

  update() {
    if (!this.el || (!this.isVisible && !this.userWanted)) return;

    const speed = (currentPosition && currentPosition.speed) ? currentPosition.speed : 0;
    const speedEl = document.getElementById('fsw-speed-val');
    if (speedEl) speedEl.textContent = speed;

    const alerts = engine ? engine.check(currentPosition) : [];
    const topAlert = alerts.length > 0 ? alerts[0] : null;

    const limitEl = document.getElementById('fsw-limit-val');
    const alertBox = document.getElementById('fsw-alert-box');
    const alertIcon = document.getElementById('fsw-alert-icon');
    const alertText = document.getElementById('fsw-alert-text');

    if (this.isPaused) {
      if (alertBox) alertBox.className = 'fsw-alert-area';
      if (alertIcon) alertIcon.textContent = '⏸️';
      if (alertText) alertText.textContent = "To'xtatilgan";
      this.el.classList.remove('overspeed');
      return;
    }

    if (topAlert && topAlert.camera) {
      const cam = topAlert.camera;
      if (limitEl) limitEl.textContent = cam.speedLimit || '—';
      if (alertIcon) alertIcon.textContent = '⚠️';
      if (alertText) alertText.textContent = `${topAlert.distance}m: ${cam.name}`;

      if (topAlert.isOverSpeed) {
        this.el.classList.add('overspeed');
        if (alertBox) alertBox.className = 'fsw-alert-area danger';
      } else {
        this.el.classList.remove('overspeed');
        if (alertBox) alertBox.className = 'fsw-alert-area';
      }
    } else {
      if (limitEl) limitEl.textContent = '60';
      if (alertIcon) alertIcon.textContent = '🛡️';
      if (alertText) alertText.textContent = "Yo'l ochiq";
      this.el.classList.remove('overspeed');
      if (alertBox) alertBox.className = 'fsw-alert-area';
    }
  }
};

const PipManager = {
  canvas: null,
  ctx: null,
  video: null,
  isActive: false,
  isPaused: false,
  stream: null,
  audioCtx: null,
  drawTimer: null,
  needsReopenOnTouch: false,

  init() {
    this.canvas = document.getElementById('pip-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.video = document.getElementById('pip-video');

    if (this.video) {
      this.video.autoPictureInPicture = true;

      this.video.addEventListener('enterpictureinpicture', () => {
        this.isActive = true;
        this.needsReopenOnTouch = false;
        if (typeof FloatingWidget !== 'undefined') {
          FloatingWidget.userWanted = true;
          FloatingWidget.syncVisibility();
        }
        this.updateButtons(true);
      });

      this.video.addEventListener('leavepictureinpicture', () => {
        this.isActive = false;
        // Agar telefon qulflangani sababli OS PiP yopilgan bo'lsa, darhol ekran ichidagi Mini-oynani chiqaramiz!
        if (typeof FloatingWidget !== 'undefined' && FloatingWidget.userWanted) {
          this.needsReopenOnTouch = true;
          FloatingWidget.syncVisibility();
        } else {
          this.updateButtons(false);
        }
      });

      // Ekran qulflanganda Android videoni pauza qilib PiP-ni o'chirib qo'ymasligi uchun himoya
      this.video.addEventListener('pause', () => {
        if (!this.isPaused && typeof audio !== 'undefined' && !audio.isExiting) {
          this.video.play().catch(() => {});
        }
      });
    }

    // MediaSession (Qulf ekrani va PiP oynasi ustidagi boshqaruv tugmalari)
    if ('mediaSession' in navigator) {
      try {
        navigator.mediaSession.setActionHandler('pause', () => {
          this.setPaused(true);
        });
        navigator.mediaSession.setActionHandler('play', () => {
          this.setPaused(false);
        });
        navigator.mediaSession.setActionHandler('previoustrack', () => {
          this.setPaused(false);
        });
        navigator.mediaSession.setActionHandler('nexttrack', () => {
          this.setPaused(false);
        });
        try {
          navigator.mediaSession.setActionHandler('enterpictureinpicture', () => {
            this.enterOsPipOnly();
          });
        } catch (e) {}
      } catch (e) {}
    }

    // 1. Telefon qulflanganda (hidden) va Qulfdan ochilganda (visible) Mini-oyna va Qulf Vidjetini boshqarish
    document.addEventListener('visibilitychange', () => {
      const spd = (typeof currentPosition !== 'undefined' && currentPosition.speed) ? currentPosition.speed : 0;
      const al = (typeof engine !== 'undefined' && typeof currentPosition !== 'undefined') ? engine.check(currentPosition) : [];
      const topAl = al.length > 0 ? al[0] : null;

      if (document.visibilityState === 'hidden') {
        // Telefon qulflandi yoki fon rejimiga o'tdi:
        // Hech qachon mini-oynani yopmaymiz! Aksincha, uni yoqilgan holatda saqlaymiz:
        if (typeof FloatingWidget !== 'undefined') {
          FloatingWidget.userWanted = true;
          FloatingWidget.show();
        }
        if (typeof audio !== 'undefined' && !audio.isExiting) {
          audio.startBackgroundKeepAlive();
        }
        updateLockScreenStatus(spd, topAl, true);

        if (!this.isActive && !this.isPaused) {
          this.enterOsPipOnly();
        }
      } else if (document.visibilityState === 'visible') {
        // Telefon qulfdan ochildi! Darhol Mini-oynani ekranda ko'rsatamiz!
        if (typeof FloatingWidget !== 'undefined') {
          FloatingWidget.userWanted = true;
          FloatingWidget.show();
        }
        if (typeof WakeLockEngine !== 'undefined' && WakeLockEngine.isWanted) {
          WakeLockEngine.request();
        }
        if (typeof audio !== 'undefined' && !audio.isExiting) {
          audio.startBackgroundKeepAlive();
        }
        this.ensureMediaReady();
        updateLockScreenStatus(spd, topAl, true);
      }
    });

    // Qulf ochilgandan so'ng ekranga birinchi marta tekkan zahoti OS PiP ni ham qayta tiklash
    const onTouchAfterUnlock = () => {
      if (this.needsReopenOnTouch && FloatingWidget.userWanted && !this.isActive) {
        this.needsReopenOnTouch = false;
        this.ensureMediaReady();
      }
    };
    window.addEventListener('touchstart', onTouchAfterUnlock, { passive: true });
    window.addEventListener('click', onTouchAfterUnlock, { passive: true });

    this.draw();
    if (this.drawTimer) clearInterval(this.drawTimer);
    this.drawTimer = setInterval(() => {
      this.draw();
    }, 500);
  },

  ensureMediaReady() {
    if (!this.video || !this.canvas) return;
    try {
      this.draw();
      if (!this.stream) {
        const canvasStream = this.canvas.captureStream(15);
        const tracks = [...canvasStream.getVideoTracks()];

        // Android Chrome ekran qulflanganda videoni o'chirmasligi uchun mikro-audio trek qo'shamiz
        try {
          const AC = window.AudioContext || window.webkitAudioContext;
          if (AC) {
            if (!this.audioCtx) this.audioCtx = new AC();
            if (this.audioCtx.state === 'suspended') this.audioCtx.resume().catch(() => {});
            const dest = this.audioCtx.createMediaStreamDestination();
            const osc = this.audioCtx.createOscillator();
            const gain = this.audioCtx.createGain();
            osc.frequency.value = 25;
            gain.gain.value = 0.0001; // Inson qulog'iga mutlaqo eshitilmaydi (-80dB)
            osc.connect(gain);
            gain.connect(dest);
            osc.start();
            const audioTracks = dest.stream.getAudioTracks();
            if (audioTracks.length > 0) {
              tracks.push(audioTracks[0]);
            }
          }
        } catch (e) {}

        this.stream = new MediaStream(tracks);
        this.video.srcObject = this.stream;
        this.video.muted = false;
        this.video.volume = 0.85;
      } else if (this.audioCtx && this.audioCtx.state === 'suspended') {
        this.audioCtx.resume().catch(() => {});
      }

      if (this.video.paused && !this.isPaused) {
        this.video.play().catch(() => {});
      }
    } catch (e) {
      console.warn('Media stream tayyorlash xatosi:', e);
    }
  },

  updateButtons(active) {
    const btnBottom = document.getElementById('btn-pip-bottom');
    if (btnBottom) btnBottom.classList.toggle('active', active);
  },

  setPaused(paused) {
    this.isPaused = paused;
    audio.muted = paused;
    if (paused) {
      audio.stopAll();
    }
    this.draw();
  },

  togglePause() {
    this.setPaused(!this.isPaused);
  },

  // Faqat OS Picture-in-Picture ga kirish (FloatingWidget ni hech qachon o'chirib qo'ymaydi!)
  async enterOsPipOnly() {
    if (!this.video || !(document.pictureInPictureEnabled || this.video.webkitSupportsPresentationMode)) {
      return;
    }
    try {
      this.ensureMediaReady();
      await this.video.play();
      if (!document.pictureInPictureElement) {
        if (this.video.requestPictureInPicture) {
          await this.video.requestPictureInPicture();
        } else if (this.video.webkitSetPresentationMode) {
          this.video.webkitSetPresentationMode('picture-in-picture');
        }
      }
    } catch (err) {
      // OS PiP ruxsat bermasa, ichki FloatingWidget ekranda ko'rinib turaveradi
      if (typeof FloatingWidget !== 'undefined' && FloatingWidget.userWanted) {
        FloatingWidget.syncVisibility();
      }
    }
  },

  // Pastki "📌 Mini-oyna" tugmasi bosilganda
  async requestPip() {
    if (typeof audio !== 'undefined') {
      audio.unlock();
    }

    const currentlyOn = Boolean(document.pictureInPictureElement) || (typeof FloatingWidget !== 'undefined' && FloatingWidget.isVisible);

    if (currentlyOn) {
      // Agar mini-oyna allaqachon ochiq bo'lsa va foydalanuvchi tugmani qayta bossa:
      // Agar OS PiP hali ochilmagan bo'lsa, avval OS PiP ga chiqarib ko'ramiz, aks holda yopamiz
      if (!document.pictureInPictureElement && this.video && document.pictureInPictureEnabled) {
        try {
          this.ensureMediaReady();
          await this.video.play();
          await this.video.requestPictureInPicture();
          return;
        } catch (e) {}
      }
      this.exit();
      return;
    }

    // Mini-oynani yoqish
    if (typeof FloatingWidget !== 'undefined') {
      FloatingWidget.show();
    }
    await this.enterOsPipOnly();
  },

  exit() {
    this.needsReopenOnTouch = false;
    if (document.pictureInPictureElement) {
      document.exitPictureInPicture().catch(() => {});
    }
    if (typeof FloatingWidget !== 'undefined') {
      FloatingWidget.hide();
    }
  },

  draw() {
    const ctx = this.ctx;
    if (!ctx) return;
    const w = 360;
    const h = 360;

    // 1. To'rtburchak foni
    const bgGrad = ctx.createLinearGradient(0, 0, w, h);
    bgGrad.addColorStop(0, '#060a14');
    bgGrad.addColorStop(1, '#0e1628');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    // Hoshiya
    ctx.strokeStyle = this.isPaused ? '#f59e0b' : '#00f2fe';
    ctx.lineWidth = 4;
    ctx.strokeRect(2, 2, w - 4, h - 4);

    // 2. Sarlavha
    ctx.fillStyle = '#00f2fe';
    ctx.font = 'bold 15px sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('🛡️ QALQON RADAR', 16, 28);

    ctx.fillStyle = '#10b981';
    ctx.font = 'bold 13px sans-serif';
    ctx.textAlign = 'right';
    ctx.fillText('GPS 🟢', w - 16, 28);

    // 3. Markaziy Spidometr
    const speed = (currentPosition && currentPosition.speed) ? currentPosition.speed : 0;
    const alerts = engine ? engine.check(currentPosition) : [];
    const topAlert = alerts.length > 0 ? alerts[0] : null;
    const isOver = topAlert ? topAlert.isOverSpeed : false;

    ctx.fillStyle = isOver ? '#ff3344' : '#00ff66';
    ctx.font = '900 84px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`${speed}`, w / 2 - 24, 138);

    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 16px sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('KM/H', w / 2 + 50, 114);

    // 4. Tezlik cheklovi belgisi
    const limit = topAlert && topAlert.camera ? topAlert.camera.speedLimit : 60;
    const signX = w - 50;
    const signY = 108;
    ctx.beginPath();
    ctx.arc(signX, signY, 26, 0, Math.PI * 2);
    ctx.fillStyle = '#ffffff';
    ctx.fill();
    ctx.lineWidth = 5;
    ctx.strokeStyle = '#ff2233';
    ctx.stroke();

    ctx.fillStyle = '#000000';
    ctx.font = '900 22px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`${limit}`, signX, signY + 8);

    // 5. Radar Kartasi
    if (this.isPaused) {
      ctx.fillStyle = 'rgba(245, 158, 11, 0.2)';
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 2;
      roundRect(ctx, 16, 172, w - 32, 112, 14, true, true);

      ctx.fillStyle = '#f59e0b';
      ctx.font = '900 20px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('⏸ TO\'XTATILGAN', w / 2, 220);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '13px sans-serif';
      ctx.fillText('Radar ovozi vaqtincha to\'xtatildi', w / 2, 248);
    } else if (topAlert && topAlert.camera) {
      const cam = topAlert.camera;
      ctx.fillStyle = isOver ? 'rgba(255, 34, 51, 0.25)' : 'rgba(0, 242, 254, 0.15)';
      ctx.strokeStyle = isOver ? '#ff3344' : '#00f2fe';
      ctx.lineWidth = 2;
      roundRect(ctx, 16, 172, w - 32, 112, 14, true, true);

      ctx.fillStyle = isOver ? '#ff5566' : '#ffffff';
      ctx.font = 'bold 18px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(`⚠️ ${cam.name}`, w / 2, 208);

      ctx.fillStyle = isOver ? '#ffdd44' : '#00ff66';
      ctx.font = '900 30px sans-serif';
      ctx.fillText(`${topAlert.distance} m`, w / 2, 246);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.fillText(cam.roadName || 'Yo\'l', w / 2, 270);
    } else {
      ctx.fillStyle = 'rgba(16, 185, 129, 0.12)';
      ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
      ctx.lineWidth = 1.5;
      roundRect(ctx, 16, 172, w - 32, 112, 14, true, true);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 20px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('🛡️ YO\'L OCHIQ', w / 2, 224);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '13px sans-serif';
      ctx.fillText('Oldinda radarlar yo\'q', w / 2, 250);
    }

    // 6. Pastki Boshqaruv Qatori
    ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
    ctx.fillRect(0, h - 52, w, 52);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, h - 52);
    ctx.lineTo(w, h - 52);
    ctx.stroke();

    ctx.fillStyle = this.isPaused ? '#f59e0b' : '#38bdf8';
    ctx.font = 'bold 14px sans-serif';
    ctx.textAlign = 'center';
    const pauseTxt = this.isPaused ? '▶️ Qayta yoqish (Play)' : '🛡️ Qulf ekranida ham faol';
    ctx.fillText(pauseTxt, w / 2, h - 22);
  }
};

// Ilovani butunlay to'xtatish va yopish
function stopAndExitApp() {
  console.log("🛑 Qalqon Antiradar to'xtatilmoqda...");

  try {
    if (typeof WakeLockEngine !== 'undefined') WakeLockEngine.release();
  } catch (err) {
    console.warn("WakeLock to'xtatishda xatolik:", err);
  }

  try {
    if (typeof PipManager !== 'undefined') PipManager.exit();
  } catch (err) {
    console.warn("PiP to'xtatishda xatolik:", err);
  }

  try {
    if (typeof FloatingWidget !== 'undefined') FloatingWidget.hide();
  } catch (err) {
    console.warn("FloatingWidget to'xtatishda xatolik:", err);
  }

  try {
    if (watchId !== null && navigator.geolocation) {
      navigator.geolocation.clearWatch(watchId);
      watchId = null;
    }
  } catch (err) {
    console.warn("GPS watchId tozalashda xatolik:", err);
  }

  try {
    if (typeof audio !== 'undefined') {
      audio.stopAll();
      audio.stopKeepAlive();
      audio.muted = true;
    }
  } catch (err) {
    console.warn("Audio to'xtatishda xatolik:", err);
  }

  try {
    if ('serviceWorker' in navigator && navigator.serviceWorker.controller) {
      navigator.serviceWorker.controller.postMessage({ type: 'QALQON_CLEAR_NOTIFY' });
    }
  } catch (err) {}

  try {
    const exitModal = document.getElementById('exit-modal');
    if (exitModal) exitModal.classList.add('hidden');
  } catch (err) {}

  try {
    updateGpsStatus("Radar to'xtatildi (Chiqildi)", false);
  } catch (err) {}

  try {
    window.close();
  } catch (err) {}

  try {
    document.body.innerHTML = `
      <div style="min-height:100vh; height:100dvh; display:flex; flex-direction:column; align-items:center; justify-content:center; background:#070b14; color:#fff; font-family:sans-serif; text-align:center; padding:24px; box-sizing:border-box;">
        <div style="font-size:72px; margin-bottom:16px;">🛑</div>
        <h2 style="color:#00f2fe; margin-bottom:12px; font-size:24px; font-weight:800; letter-spacing:0.5px;">QALQON ANTIRADAR TO'XTATILDI</h2>
        <p style="color:#94a3b8; max-width:400px; line-height:1.6; font-size:14px; margin-bottom:32px;">
          Radar monitoringi, GPS kuzatuv va audio ogohlantirishlar to‘liq o‘chirildi. Safaringiz bexatar bo‘lsin!
        </p>
        <button type="button" onclick="window.location.reload()" style="background:linear-gradient(135deg, #00f2fe, #2563eb); border:none; border-radius:14px; color:#030712; font-size:16px; font-weight:800; padding:16px 36px; cursor:pointer; box-shadow:0 6px 24px rgba(0,242,254,0.45); -webkit-tap-highlight-color:transparent; user-select:none; touch-action:manipulation;">
          🔄 Qayta yoqish
        </button>
      </div>
    `;
  } catch (err) {
    console.error("Chiqish ekranini chizishda xatolik:", err);
  }
}
window.stopAndExitApp = stopAndExitApp;

// Joylashuvimga qaytish
function recenterUser() {
  setFollowUser(true);
  if (map) {
    map.flyTo([currentPosition.lat, currentPosition.lng], 16, { animate: true, duration: 1 });
  }
}

let autoFollowTimer = null;

function setFollowUser(active) {
  followUser = active;
  const btnRecenter = document.getElementById('btn-recenter');
  const btnFollowToggle = document.getElementById('btn-follow-toggle');
  const btnFloating = document.getElementById('btn-floating-recenter');
  
  if (btnRecenter) {
    btnRecenter.classList.toggle('active-glow', active);
  }
  if (btnFollowToggle) {
    btnFollowToggle.classList.toggle('active', active);
    btnFollowToggle.innerHTML = active ? '<span>🧭</span> Avto-kuzatuv: Yoqiq' : '<span>✋</span> Avto-kuzatuv: To\'xtatilgan';
  }
  if (btnFloating) {
    btnFloating.classList.toggle('hidden', active);
  }

  if (active) {
    if (autoFollowTimer) {
      clearTimeout(autoFollowTimer);
      autoFollowTimer = null;
    }
    if (map && currentPosition) {
      map.panTo([currentPosition.lat, currentPosition.lng], { animate: true });
    }
  } else {
    // Agar foydalanuvchi xaritani sursa, 8 soniyadan so'ng avtomatik yana mashinaga ergashadi!
    if (autoFollowTimer) clearTimeout(autoFollowTimer);
    autoFollowTimer = setTimeout(() => {
      setFollowUser(true);
    }, 8000);
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
    audio.stopAll();
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
  const backdrop = document.getElementById('settings-backdrop');
  if (drawer) {
    const willOpen = drawer.classList.contains('hidden');
    drawer.classList.toggle('hidden');
    if (backdrop) backdrop.classList.toggle('hidden', !willOpen);
  }
}

// Initsializatsiya
window.addEventListener('DOMContentLoaded', () => {
  initMap();

  // Foydalanuvchi ekranga tekkanda (touchend / click) audioni, Qulf Ekrani vidjetini va WakeLock-ni 100% uyg'otish
  const unlockEvents = ['touchend', 'pointerup', 'click', 'keydown'];
  const onUserInteraction = () => {
    audio.unlock();
    if (typeof WakeLockEngine !== 'undefined' && WakeLockEngine.isWanted) {
      WakeLockEngine.request();
    }
    if (typeof PipManager !== 'undefined') {
      PipManager.ensureMediaReady();
    }
  };
  unlockEvents.forEach(evt => window.addEventListener(evt, onUserInteraction, { passive: true }));

  // Xaritada erkin yurgandan so'ng markazga qaytish FAB tugmasi
  const btnFloatingRecenter = document.getElementById('btn-floating-recenter');
  if (btnFloatingRecenter) {
    btnFloatingRecenter.addEventListener('click', () => {
      setFollowUser(true);
      recenterUser();
    });
  }

  // ============================================================
  // BIRINCHI KIRISHDA GPS VA OVOZ RUXSAT MODALI
  // ============================================================
  const gpsModal = document.getElementById('gps-permission-modal');
  const btnGrantGps = document.getElementById('btn-grant-gps');
  const isGpsPreviouslyGranted = localStorage.getItem('qalqon_gps_granted');

  if (!isGpsPreviouslyGranted && gpsModal) {
    gpsModal.classList.remove('hidden');
  } else {
    startLiveGps();
    // Darhol orqa fon va qulf ekrani oqimini ishga tushirishga urinish (TWA / APK ichida avtomatik ruxsat beriladi)
    audio.startBackgroundKeepAlive();
  }

  if (btnGrantGps) {
    btnGrantGps.addEventListener('click', () => {
      audio.unlock();
      if (typeof WakeLockEngine !== 'undefined') {
        WakeLockEngine.request();
      }
      if (gpsModal) gpsModal.classList.add('hidden');
      localStorage.setItem('qalqon_gps_granted', '1');

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (pos) => {
            const crd = pos.coords;
            currentPosition.lat = crd.latitude;
            currentPosition.lng = crd.longitude;
            if (crd.heading !== null && !isNaN(crd.heading) && crd.heading >= 0) {
              currentPosition.heading = Math.round(crd.heading);
            }
            hasHadFirstGpsFix = true;
            if (map) {
              map.setView([currentPosition.lat, currentPosition.lng], 16);
            }
            if (carMarker) {
              carMarker.setLatLng([currentPosition.lat, currentPosition.lng]);
            }
            updateRadarState();
            startLiveGps();
            audio.playRadarAlertChime();
          },
          (err) => {
            console.warn("GPS ruxsat berish xatosi:", err.message);
            startLiveGps();
          },
          { enableHighAccuracy: true, timeout: 8000 }
        );
      } else {
        startLiveGps();
      }
    });
  }

  // ============================================================
  // RADARLAR BAZASINI AVTOMATIK YUKLASH (CLOUD & LOKAL KESH)
  // ============================================================
  async function loadCameras() {
    let cloudLoaded = false;
    if (window.QalqonCloud && window.QalqonCloud.isConfigured()) {
      try {
        const cloudPromise = window.QalqonCloud.fetchCameras();
        const timeoutPromise = new Promise((_, reject) => setTimeout(() => reject(new Error('Cloud timeout')), 2500));
        const cloudCams = await Promise.race([cloudPromise, timeoutPromise]);
        if (Array.isArray(cloudCams) && cloudCams.length > 0) {
          speedCameras = cloudCams;
          engine.cameras = cloudCams;
          renderCamerasOnMap();
          updateNearbyCamsList();
          cloudLoaded = true;
          console.log(`✅ Supabase Cloud-dan ${cloudCams.length} ta radar yuklandi!`);
        }
      } catch (err) {
        console.warn('Supabase cloud fetch failed or timed out, falling back:', err.message);
      }
    }

    if (!cloudLoaded) {
      // Oflayn yoki lokal bazadan 1,014 ta radarni yuklash
      fetch('src/data/speedcams.json')
        .then(r => r.json())
        .then(data => {
          if (Array.isArray(data) && data.length > 0) {
            speedCameras = data;
            engine.cameras = data;
            renderCamerasOnMap();
            updateNearbyCamsList();
            console.log(`✅ Lokal bazadan ${data.length} ta radar yuklandi!`);
          }
        }).catch(err => {
          console.warn('speedcams.json yuklashda xatolik:', err);
        });
    }
  }

  // Sahifa ochilganda bazani avtomatik yuklash
  loadCameras();

  // Jonli sinxronizatsiya: boshqa haydovchilar belgilagan radarlarni qabul qilish
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
    btnReportCam.addEventListener('click', (e) => {
      e.preventDefault();
      reportModal.classList.remove('hidden');
      if (reportStatusMsg) reportStatusMsg.innerHTML = '';
    });
  }

  if (btnCloseReport && reportModal) {
    btnCloseReport.addEventListener('click', () => {
      reportModal.classList.add('hidden');
    });
  }

  if (reportModal) {
    reportModal.addEventListener('click', (e) => {
      if (e.target === reportModal) {
        reportModal.classList.add('hidden');
      }
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
  document.getElementById('btn-follow-toggle').addEventListener('click', () => {
    setFollowUser(!followUser);
    if (followUser) recenterUser();
  });
  document.getElementById('btn-hud').addEventListener('click', toggleHud);
  const btnHudExit = document.getElementById('btn-hud-exit');
  if (btnHudExit) btnHudExit.addEventListener('click', closeHud);
  const btnHudMirror = document.getElementById('btn-hud-mirror');
  if (btnHudMirror) btnHudMirror.addEventListener('click', toggleHudMirror);

  // ESC tugmasi bosilganda HUD va Sozlamalarni yopish
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const drawer = document.getElementById('settings-drawer');
      if (drawer && !drawer.classList.contains('hidden')) {
        toggleSettings();
      }
      if (isHudActive) {
        closeHud();
      }
    }
  });
  document.getElementById('btn-mute').addEventListener('click', toggleMute);
  document.getElementById('btn-fullscreen').addEventListener('click', toggleFullscreen);

  // Sozlamalar tugmalari
  const btnSettings = document.getElementById('btn-settings-toggle');
  if (btnSettings) btnSettings.addEventListener('click', toggleSettings);
  const btnCloseSettings = document.getElementById('btn-close-settings');
  if (btnCloseSettings) btnCloseSettings.addEventListener('click', toggleSettings);
  const settingsBackdrop = document.getElementById('settings-backdrop');
  if (settingsBackdrop) settingsBackdrop.addEventListener('click', toggleSettings);

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

  // Ekran holati (WakeLock) sozlamasi va tugmasi
  const selWake = document.getElementById('setting-wakelock-mode');
  if (selWake) {
    selWake.addEventListener('change', (e) => {
      if (e.target.value === 'always') {
        WakeLockEngine.request();
      } else {
        WakeLockEngine.release();
      }
    });
  }

  const btnWake = document.getElementById('btn-wakelock');
  if (btnWake) {
    btnWake.addEventListener('click', () => {
      WakeLockEngine.toggle();
    });
  }

  // Tizim ovozini tekshirish va to'xtatish tugmalari (Sozlamalar ichida)
  const soundTestBtn = document.getElementById('btn-sound-test');
  const soundStopBtn = document.getElementById('btn-sound-stop');

  if (soundTestBtn) {
    soundTestBtn.addEventListener('click', () => {
      audio.unlock();
      audio.stopAll(); // Oldingi ovozlar yoki taymerlarni zudlik bilan tozalash
      audio.muted = false;

      const btnMute = document.getElementById('btn-mute');
      if (btnMute) {
        btnMute.innerHTML = '<span>🔊</span> Ovozli';
        btnMute.classList.remove('active');
      }

      soundTestBtn.innerHTML = '<span>🔊</span> Sinov ketyapti...';
      soundTestBtn.classList.add('active');

      audio.playRadarAlertChime();

      audio.testTimeouts = [
        setTimeout(() => audio.playFile('lochin_70.mp3'), 450),
        setTimeout(() => audio.playFile('neoline_click.wav'), 1900),
        setTimeout(() => audio.playFile('neoline_click.wav'), 2300),
        setTimeout(() => audio.playFile('rear_70.mp3'), 2800),
        setTimeout(() => audio.playFile('uch_oyoq_70.mp3'), 5200),
        setTimeout(() => audio.playFile('cleared.mp3'), 7600),
        setTimeout(() => {
          if (soundTestBtn) {
            soundTestBtn.innerHTML = '<span>⚡</span> Ovozni sinash';
            soundTestBtn.classList.remove('active');
          }
        }, 9200)
      ];
    });
  }

  if (soundStopBtn) {
    soundStopBtn.addEventListener('click', () => {
      audio.stopAll();
    });
  }

  // ============================================================
  // 📌 SUZUVCHI MINI-OYNA (PICTURE-IN-PICTURE) VA YOPISH
  // ============================================================
  if (typeof FloatingWidget !== 'undefined') {
    FloatingWidget.init();
  }

  if (typeof PipManager !== 'undefined') {
    PipManager.init();
  }

  const btnPipBottom = document.getElementById('btn-pip-bottom');
  if (btnPipBottom) {
    btnPipBottom.addEventListener('click', () => {
      PipManager.requestPip();
    });
  }

  // Ilovani To'xtatish va Yopish
  const exitModal = document.getElementById('exit-modal');
  const btnAppClose = document.getElementById('btn-app-close');
  const btnCancelExit = document.getElementById('btn-cancel-exit');
  const btnConfirmExit = document.getElementById('btn-confirm-exit');

  const openExitModal = (e) => {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    if (exitModal) exitModal.classList.remove('hidden');
  };

  const closeExitModal = (e) => {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    if (exitModal) exitModal.classList.add('hidden');
  };

  const confirmExitAction = (e) => {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    stopAndExitApp();
  };

  if (btnAppClose) {
    btnAppClose.addEventListener('click', openExitModal);
    btnAppClose.addEventListener('touchend', openExitModal, { passive: false });
  }

  if (btnCancelExit) {
    btnCancelExit.addEventListener('click', closeExitModal);
    btnCancelExit.addEventListener('touchend', closeExitModal, { passive: false });
  }

  if (exitModal) {
    exitModal.addEventListener('click', (e) => {
      if (e.target === exitModal) {
        closeExitModal(e);
      }
    });
  }

  if (btnConfirmExit) {
    btnConfirmExit.addEventListener('click', confirmExitAction);
    btnConfirmExit.addEventListener('touchend', confirmExitAction, { passive: false });
  }

  // Ekran avtomatik o‘chib qolmasligi va doimo yoniq turishi (WakeLock)
  if (typeof WakeLockEngine !== 'undefined') {
    WakeLockEngine.request();
  }

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && typeof WakeLockEngine !== 'undefined' && WakeLockEngine.isWanted) {
      WakeLockEngine.request();
    }
  });

  window.addEventListener('focus', () => {
    if (typeof WakeLockEngine !== 'undefined' && WakeLockEngine.isWanted) {
      WakeLockEngine.request();
    }
  });

  updateRadarState();
});
