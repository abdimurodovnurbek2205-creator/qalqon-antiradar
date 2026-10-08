# 🛡️ QALQON ANTIRADAR (ContraCam muqobili)

Haydovchilar uchun mo‘ljallangan, yo‘ldagi barcha turdagi fotoradarlar, statsionar kameralar, svetofor nazoratchilari va mobil pistirmalarni (trinoga) oldindan aniqlab, ovozli ogohlantiruvchi kuchli intellektual tizim.

---

## ⚡ Asosiy Imkoniyatlar (ContraCam Funksiyalari)

1. **Aqlli Burchakli Filtr (Directional Sector Filtering)**:
   - Ko‘chadagi barcha kameralar emas, **faqat aynan sizning harakat yo‘nalishingizga (azimut) qaratilgan** kameralar ogohlantiriladi.
   - Qarama-qarshi yo‘nalishdagi yoki yon ko‘chalardagi radarlar haydovchini chalg‘itmaydi.

2. **Dinamik Masofa Hisoblagichi (Dynamic Alert Distance)**:
   - Sekin harakatlanganda ($40\text{ km/soat}$): **$300\text{ metr}$** oldin ogohlantiradi.
   - O‘rta tezlikda ($60\text{ - }70\text{ km/soat}$): **$450\text{ - }550\text{ metr}$** oldin.
   - Trassada ($100\text{ - }120\text{ km/soat}$): **$800\text{ - }1000\text{ metr}$** oldin xabar beradi.

3. **O‘zbekcha Ovozli va Tungi Rejim (HUD & Audio)**:
   - **Ovozli ogohlantirish**: *"Diqqat! 450 metr oldinda Tezlik kamerasi 60! Tezlikni tushiring!"*
   - **Tezlik oshganda signal**: Qattiq va uzluksiz bi-bi-bip xavf signali.
   - **HUD Tungi Rejim**: Tunda telefonni avtomobil old oynasining (torpeda) ustiga qo‘yganda, tasvirni ko‘zgu kabi teskari aylantirib, to‘g‘ridan-to‘g‘ri old oynada spidometr va radar belgisini proyeksiyalash.

4. **O‘rtacha Tezlik Koridorlari (Section Control / AutoCon)**:
   - Yangi O‘zbekiston va boshqa trassalardagi kirish kamerasidan chiqish kamerasigacha bo‘lgan masofada o‘rtacha tezlikni real vaqtda hisoblab borish.

5. **Ko‘p qavatli Radarlar Bazasi**:
   - 🔴 **Statsionar tezlik kameralari** (Strelka, Cordon, Hikvision, Multaradar)
   - 🟠 **Mobil pistirmalar** (Trinoga va patrul mashinalari)
   - 🟣 **Svetofor va stop-liniya kameralari**
   - 🔵 **A-yo‘lak (Avtobus yo‘lagi) kameralari**
   - 🟡 **Sun’iy notekisliklar** ("lejaщiy politseyskiy") va xavfli burilishlar.

---

## 🚀 Ilovani Ishga Tushirish

### 1. Kompyuter yoki Telefonda Brauzer orqali:
Loyihaning `index.html` faylini istalgan brauzerda oching.
- **▶️ Marshrut Sinovi**: Ofisda yoki uyda turib, mashina harakatini Toshkent ko‘chalari yoki M39 trassasi bo‘yicha sinovdan o‘tkazing.
- **Slayder (Tezlik)**: Tezlikni $55\text{ km/soat}$ dan $85\text{ km/soat}$ ga ko‘taring — tizim avtomatik tarzda qizil rangga kiradi va ovozli *"Tezlikni tushiring!"* signalini chaladi.
- **📡 Haqiqiy GPS**: Avtomobilda ketayotganda yoqilsa, telefonning ichki GPS sensoridan real koordinata va tezlikni oladi.
- **🌙 HUD**: Tungi rejimni yoqish.

---

## 📱 Android Fondagi Rejim va Suzuvchi Vidjet (Floating Bubble)

- `mobile/android/RadarForegroundService.kt` — Ekran o‘chiq bo‘lsa ham fon rejimida GPS koordinatani qabul qilib, mashina Bluetooth audio tizimiga ovozli signal beradi.
- `mobile/android/FloatingRadarOverlayService.kt` — **Yandex Navigator** yoki **Google Maps** ustida suzuvchi xavfsiz tezlik pufakchasi.
