/**
 * QALQON ANTIRADAR - SERVICE WORKER (OFFLINE PWA)
 * Barcha radarlar, audio ovozlar, xarita va interfeysni internetsiz ishlashi uchun keshlaydi
 */

const CACHE_NAME = 'qalqon-v2-1017';
const STATIC_ASSETS = [
  './',
  './index.html',
  './style.css',
  './app.js',
  './manifest.json',
  './src/data/speedcams.json',
  './src/supabaseClient.js',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
  'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2',
  './sounds/lochin_60.mp3',
  './sounds/lochin_70.mp3',
  './sounds/lochin_100.mp3',
  './sounds/uch_oyoq.mp3',
  './sounds/uch_oyoq_70.mp3',
  './sounds/uch_oyoq_100.mp3',
  './sounds/patrul_360.mp3',
  './sounds/rear_60.mp3',
  './sounds/rear_70.mp3',
  './sounds/rear_100.mp3',
  './sounds/chorraha.mp3',
  './sounds/slowdown.mp3',
  './sounds/bus_lane.mp3',
  './sounds/autocon_start.mp3',
  './sounds/autocon_end.mp3',
  './sounds/cleared.mp3',
  './sounds/speed_bump.mp3',
  './sounds/radar_alert.wav',
  './sounds/geiger.wav',
  './sounds/overspeed_alarm.wav',
  './sounds/pass.wav',
  './sounds/neoline_chirp.wav',
  './sounds/neoline_click.wav',
  './sounds/real_neoline_geiger.wav'
];

// O'rnatilganda barcha asosiy fayllarni keshga yozish
self.addEventListener('install', (evt) => {
  evt.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('📦 Qalqon Service Worker: Offline kesh yuklanmoqda...');
      return cache.addAll(STATIC_ASSETS).catch((err) => {
        console.warn('⚠️ Ayrim fayllarni keshga olishda ogohlantirish:', err);
      });
    }).then(() => self.skipWaiting())
  );
});

// Eski kesh versiyalarini tozalash
self.addEventListener('activate', (evt) => {
  evt.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((k) => {
          if (k !== CACHE_NAME) {
            console.log('🗑️ Eski kesh tozalandi:', k);
            return caches.delete(k);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Tarmoq so'rovlarini ushlab qolish (Stale-While-Revalidate & Cache-First)
self.addEventListener('fetch', (evt) => {
  const req = evt.request;
  const url = new URL(req.url);

  // Faqat GET so'rovlarni keshdan xizmat qilamiz
  if (req.method !== 'GET') return;

  // Supabase API so'rovlari jonli ketsin (agar oflayn bo'lsa xato beradi yoki keshdan oladi)
  if (url.hostname.includes('supabase.co')) {
    return;
  }

  // Xarita plitkalari (Google / OSM tiles) - Network-first, lekin oflayn uchun keshlanadi
  if (url.hostname.includes('tile.openstreetmap.org') || url.hostname.includes('google.com')) {
    evt.respondWith(
      caches.open(CACHE_NAME).then((cache) => {
        return fetch(req).then((networkRes) => {
          if (networkRes && networkRes.status === 200) {
            cache.put(req, networkRes.clone());
          }
          return networkRes;
        }).catch(() => {
          return cache.match(req);
        });
      })
    );
    return;
  }

  // Boshqa barcha statik fayllar (HTML, JS, CSS, JSON, MP3) - Cache-first, orqada yangilash
  evt.respondWith(
    caches.match(req).then((cachedRes) => {
      if (cachedRes) {
        // Fon rejimida yangilab qo'yish
        fetch(req).then((networkRes) => {
          if (networkRes && networkRes.status === 200) {
            caches.open(CACHE_NAME).then((c) => c.put(req, networkRes));
          }
        }).catch(() => {});
        return cachedRes;
      }

      return fetch(req).then((networkRes) => {
        if (networkRes && networkRes.status === 200) {
          const resClone = networkRes.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, resClone));
        }
        return networkRes;
      }).catch(() => {
        // Agar umuman internetsiz bo'lsa va sahifa ochilayotgan bo'lsa:
        if (req.headers.get('accept') && req.headers.get('accept').includes('text/html')) {
          return caches.match('./index.html');
        }
      });
    })
  );
});
