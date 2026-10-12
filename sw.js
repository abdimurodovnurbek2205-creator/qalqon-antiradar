/**
 * QALQON ANTIRADAR - ULTRA TEZKOR SERVICE WORKER (OFFLINE PWA)
 * Qotib qolishlarni bartaraf etuvchi, tezkor reload va offline himoya
 */

const CACHE_NAME = 'qalqon-v2-1028';
const CORE_ASSETS = [
  './',
  './index.html',
  './style.css',
  './style.css?v=2.1026',
  './app.js',
  './app.js?v=2.1026',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './screenshot.png',
  './src/data/speedcams.json',
  './src/supabaseClient.js'
];

// 1. O'rnatish: Faqat asosiy kerakli fayllarni tezkor (0.5 soniyada) keshga olamiz
self.addEventListener('install', (evt) => {
  evt.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(CORE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// 2. Aktivatsiya: Eski kesh versiyalarini bir zumda tozalash
self.addEventListener('activate', (evt) => {
  evt.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((k) => {
          if (k !== CACHE_NAME) {
            return caches.delete(k);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. Tarmoq so'rovlarini boshqarish: Hech qachon sahifani qotirib qo'ymaydi
self.addEventListener('fetch', (evt) => {
  const req = evt.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // Supabase API so'rovlari to'g'ridan-to'g'ri ketsin
  if (url.hostname.includes('supabase.co')) return;

  // HTML va sahifani yangilash (Reload / Refresh) - Tezkor Network-First va Cache Fallback
  const isHtml = req.mode === 'navigate' || 
                 (req.headers.get('accept') && req.headers.get('accept').includes('text/html'));

  if (isHtml) {
    evt.respondWith(
      // Tarmoqdan yuklash, agar 2 soniyada javob kelmasa darhol keshdan ochish
      Promise.race([
        fetch(req).then((networkRes) => {
          if (networkRes && networkRes.status === 200) {
            const clone = networkRes.clone();
            caches.open(CACHE_NAME).then((c) => c.put(req, clone));
          }
          return networkRes;
        }),
        new Promise((_, reject) => setTimeout(() => reject(new Error('Network timeout')), 2000))
      ]).catch(() => {
        return caches.match('./index.html').then((fallback) => {
          return fallback || caches.match('./');
        });
      })
    );
    return;
  }

  // Boshqa resurslar (CSS, JS, JSON, MP3, rasmlar, xarita): Stale-While-Revalidate
  evt.respondWith(
    caches.match(req).then((cachedRes) => {
      // Fon rejimida yangilab borish
      const fetchPromise = fetch(req).then((networkRes) => {
        if (networkRes && networkRes.status === 200) {
          const clone = networkRes.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, clone));
        }
        return networkRes;
      }).catch(() => null);

      // Agar keshda bo'lsa darhol uzatish, bo'lmasa tarmoqdan kutish
      return cachedRes || fetchPromise;
    })
  );
});
