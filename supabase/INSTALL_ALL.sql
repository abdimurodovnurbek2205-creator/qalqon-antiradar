-- ============================================================
-- QALQON ANTIRADAR - SUPABASE POSTGRESQL STRUKTURASI
-- ============================================================

-- 1. Barcha Radarlar va Kameralar Jadvali
CREATE TABLE IF NOT EXISTS public.speed_cameras (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    lat DOUBLE PRECISION NOT NULL,
    lng DOUBLE PRECISION NOT NULL,
    type TEXT NOT NULL, -- 'lochin', 'rear', 'uch_oyoq', 'patrul_360', 'traffic_light', 'bus_lane', 'avg_start', 'avg_end'
    speed_limit INT NOT NULL,
    azimuth INT DEFAULT -1,
    road_name TEXT,
    distance_alert_threshold INT DEFAULT 600,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Indekslar (Tezkor geodezik qidiruv uchun)
CREATE INDEX IF NOT EXISTS idx_cameras_lat_lng ON public.speed_cameras (lat, lng);
CREATE INDEX IF NOT EXISTS idx_cameras_type ON public.speed_cameras (type);

-- 2. Haydovchilar Belgilagan Yangi Radarlar (Waze / ContraCam uslubi)
CREATE TABLE IF NOT EXISTS public.community_reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lat DOUBLE PRECISION NOT NULL,
    lng DOUBLE PRECISION NOT NULL,
    type TEXT NOT NULL,
    speed_limit INT DEFAULT 70,
    road_name TEXT,
    description TEXT,
    reported_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    confirmations INT DEFAULT 1,
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE INDEX IF NOT EXISTS idx_reports_lat_lng ON public.community_reports (lat, lng);

-- RLS (Row Level Security) - Ochiq o'qish va belgilash uchun
ALTER TABLE public.speed_cameras ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.community_reports ENABLE ROW LEVEL SECURITY;

-- Hammaga o'qishga ruxsat
CREATE POLICY "Public read speed_cameras" ON public.speed_cameras
    FOR SELECT USING (true);

CREATE POLICY "Public read community_reports" ON public.community_reports
    FOR SELECT USING (true);

-- Haydovchilar yangi radar belgilashi uchun INSERT ruxsati
CREATE POLICY "Public insert community_reports" ON public.community_reports
    FOR INSERT WITH CHECK (true);


-- 3. Barcha Ozbekiston tumanlari va trassalarini yuklash
-- ============================================================
-- QALQON ANTIRADAR - O'ZBEKISTON RADARLAR BAZASI (58 TA KAMERA)
-- Ushbu kodni Supabase SQL Editorga tashlab 'RUN' bosing
-- ============================================================

INSERT INTO public.speed_cameras (id, name, lat, lng, type, speed_limit, azimuth, road_name, distance_alert_threshold, is_active)
VALUES
  ('uz-sur-ban-001', 'Lochin 60 - Bandixon markaziy ko''chasi', 37.8608, 67.3883, 'lochin', 60, -1, 'Mustaqillik shoh ko''chasi (Bandixon)', 500, TRUE),
  ('uz-sur-ban-002', 'Ko''chma Uch oyoq 70 - Bandixon - Boysun trassasi', 37.885, 67.372, 'uch_oyoq', 70, -1, '4R100 Bandixon - Boysun yo''li (Pistirma)', 650, TRUE),
  ('uz-sur-ban-003', 'Lochin 70 - Bandixon - Qiziriq yo''li', 37.832, 67.398, 'lochin', 70, -1, '4R100 Qiziriq yo''nalishi', 600, TRUE),
  ('uz-sur-ban-004', 'Chorraha kamerasi - Bandixon markaz', 37.8625, 67.3855, 'traffic_light', 60, -1, 'Bandixon markaziy chorrahasi', 450, TRUE),
  ('uz-sur-ban-005', 'YPX Patrul 360 - Bandixon aylanmasi', 37.848, 67.391, 'patrul_360', 60, -1, 'Bandixon kirish aylanma yo''li', 500, TRUE),
  ('uz-sur-ban-006', 'Kamera orqadan oladi! - Bandixon - Jarqo''rg''on yo''li', 37.855, 67.412, 'rear', 60, -1, '4R105 Jarqo''rg''on yo''li (Orqadan)', 500, TRUE),
  ('uz-sur-ter-001', 'Lochin 60 - At-Termiziy shoh ko''chasi', 37.235, 67.28, 'lochin', 60, -1, 'At-Termiziy ko''chasi (Termiz)', 500, TRUE),
  ('uz-sur-ter-002', 'Lochin 100 - M39 Termiz kirish trassasi', 37.285, 67.315, 'lochin', 100, -1, 'M39 Termiz aylanma xalqaro yo''li', 850, TRUE),
  ('uz-sur-ter-003', 'YPX Patrul 360 - Termiz xalqaro porti (Ayritom)', 37.215, 67.31, 'patrul_360', 60, -1, 'Ayritom chegara bojxona yo''li', 500, TRUE),
  ('uz-sur-boy-001', 'Lochin 70 - Boysun kirish posti', 38.205, 67.205, 'lochin', 70, -1, 'M39 Darband - Boysun trassasi', 650, TRUE),
  ('uz-sur-boy-002', 'Ko''chma Uch oyoq 70 - Sayrob archasi trassasi', 38.015, 67.145, 'uch_oyoq', 70, -1, 'M39 Sayrob dovoni (Pistirma)', 650, TRUE),
  ('uz-sur-den-001', 'Lochin 60 - Denov Sh. Rashidov shoh ko''chasi', 38.275, 67.895, 'lochin', 60, -1, 'Denov shahar markazi', 500, TRUE),
  ('uz-sur-den-002', 'Chorraha kamerasi - Denov Buyuk Ipak Yo''li', 38.282, 67.882, 'traffic_light', 60, -1, 'Denov markaziy aylanmasi', 450, TRUE),
  ('uz-sur-kum-001', 'Lochin 70 - Qumqo''rg''on M41 trassasi', 37.815, 67.585, 'lochin', 70, -1, 'M41 Termiz - Denov yo''li (Qumqo''rg''on)', 650, TRUE),
  ('uz-sur-jar-001', 'Lochin 70 - Jarqo''rg''on aylanma yo''li', 37.505, 67.415, 'lochin', 70, -1, 'M41 Jarqo''rg''on Surxon daryosi ko''prigi', 650, TRUE),
  ('uz-sur-sho-001', 'Lochin 60 - Sho''rchi markaziy ko''chasi', 38.012, 67.785, 'lochin', 60, -1, 'M41 Sho''rchi shahar markazi', 500, TRUE),
  ('uz-sur-sar-001', 'Lochin 60 - Sariosiyo markazi', 38.412, 67.945, 'lochin', 60, -1, 'Sariosiyo - Tojikiston yo''li', 500, TRUE),
  ('uz-sur-uzu-001', 'Lochin 70 - Uzun tumani M41 yo''li', 38.355, 67.925, 'lochin', 70, -1, 'M41 Uzun tuman trassasi', 600, TRUE),
  ('uz-sur-olt-001', 'Lochin 60 - Oltinsoy (Qarluq) markazi', 38.185, 67.685, 'lochin', 60, -1, 'Oltinsoy markaziy yo''li', 500, TRUE),
  ('uz-sur-she-001', 'Lochin 70 - Sherobod M39 xalqaro trassasi', 37.672, 67.012, 'lochin', 70, -1, 'M39 Sherobod aylanma yo''li', 700, TRUE),
  ('uz-sur-ang-001', 'Lochin 70 - Angor tuman markazi M39 yo''li', 37.472, 67.145, 'lochin', 70, -1, 'M39 Angor yo''nalishi', 600, TRUE),
  ('uz-sur-muz-001', 'Lochin 70 - Muzrabot (Xalqobod) markazi', 37.355, 66.885, 'lochin', 70, -1, 'Muzrabot tumanlararo trassasi', 600, TRUE),
  ('uz-sur-qiz-001', 'Lochin 60 - Qiziriq (Sariq) markaziy ko''chasi', 37.658, 67.285, 'lochin', 60, -1, '4R100 Qiziriq shahar markazi', 500, TRUE),
  ('uz-qar-001', 'Lochin 60 - Qarshi O''zbekiston shoh ko''chasi', 38.855, 65.795, 'lochin', 60, -1, 'O''zbekiston shoh ko''chasi (Qarshi)', 500, TRUE),
  ('uz-qar-002', 'Lochin 100 - Qarshi - Shahrisabz yo''li', 38.89, 65.885, 'lochin', 100, -1, 'A378 Shahrisabz yo''nalishi', 850, TRUE),
  ('uz-qar-003', 'Chorraha kamerasi - Qarshi Islom Karimov va Nasaf', 38.865, 65.782, 'traffic_light', 60, -1, 'Islom Karimov shoh ko''chasi', 450, TRUE),
  ('uz-qar-sha-001', 'Lochin 60 - Shahrisabz Ipak Yo''li ko''chasi', 39.055, 66.835, 'lochin', 60, -1, 'Shahrisabz shahar markazi (Oqsaroy)', 500, TRUE),
  ('uz-qar-kit-001', 'Lochin 70 - Kitob tuman posti (M39)', 39.125, 66.885, 'lochin', 70, -1, 'M39 Samarqand - Taxtaqoracha dovoni yo''li', 650, TRUE),
  ('uz-qar-yak-001', 'Lochin 60 - Yakkabog'' markaziy yo''li', 38.975, 66.685, 'lochin', 60, -1, 'A378 Yakkabog'' tuman markazi', 500, TRUE),
  ('uz-qar-qam-001', 'Lochin 70 - Qamashi A378 trassasi', 38.825, 66.475, 'lochin', 70, -1, 'A378 Qamashi aylanma yo''li', 650, TRUE),
  ('uz-qar-guz-001', 'Lochin 70 - G''uzor M39 va A380 aylanmasi', 38.625, 66.255, 'lochin', 70, -1, 'M39 G''uzor xalqaro chorrahasi', 700, TRUE),
  ('uz-qar-deh-001', 'Lochin 70 - Dehqonobod (Karashina) posti', 38.345, 66.495, 'lochin', 70, -1, 'M39 Surxondaryo - Termiz yo''li (Oqrabot)', 700, TRUE),
  ('uz-qar-kos-001', 'Lochin 70 - Koson A380 Buxoro trassasi', 39.035, 65.585, 'lochin', 70, -1, 'A380 Koson aylanma yo''li', 700, TRUE),
  ('uz-qar-mub-001', 'Lochin 70 - Muborak gaz sanoati trassasi', 39.265, 65.155, 'lochin', 70, -1, 'A380 Muborak magistrali', 700, TRUE),
  ('uz-qar-chi-001', 'Lochin 60 - Chiroqchi markazi', 39.025, 66.575, 'lochin', 60, -1, 'Chiroqchi shahar markaziy yo''li', 500, TRUE),
  ('uz-qar-kok-001', 'Ko''chma Uch oyoq 70 - Ko''kdala (Yettitom) aylanmasi', 38.985, 66.125, 'uch_oyoq', 70, -1, 'A378 Yettitom chorrahasi (Pistirma)', 650, TRUE),
  ('uz-qar-kas-001', 'Lochin 60 - Kasbi (Mug''lon) markazi', 38.745, 65.555, 'lochin', 60, -1, 'Kasbi tumanlararo yo''li', 500, TRUE),
  ('uz-qar-nis-001', 'Lochin 60 - Yangi Nishon markazi', 38.655, 65.685, 'lochin', 60, -1, 'Nishon shahar markazi', 500, TRUE),
  ('uz-sam-001', 'Lochin 60 - Registon ko''chasi', 39.6548, 66.9752, 'lochin', 60, -1, 'Registon ko''chasi (Samarqand)', 500, TRUE),
  ('uz-sam-002', 'Chorraha kamerasi - Rudakiy va Gagarin', 39.658, 66.955, 'traffic_light', 60, -1, 'Rudakiy va Gagarin chorrahasi', 450, TRUE),
  ('uz-sam-003', 'Kamera orqadan oladi! - Beruniy ko''chasi', 39.664, 66.942, 'rear', 60, -1, 'Beruniy ko''chasi (Orqadan uradi)', 500, TRUE),
  ('uz-sam-004', 'Lochin 60 - Spitamen shoh ko''chasi', 39.645, 66.938, 'lochin', 60, -1, 'Spitamen shoh ko''chasi', 550, TRUE),
  ('uz-sam-005', 'Chorraha kamerasi - Dahbed va Registon', 39.661, 66.979, 'traffic_light', 60, -1, 'Dahbed ko''chasi chorrahasi', 450, TRUE),
  ('uz-sam-006', 'Ko''chma Uch oyoq 70 - Ulug''bek rasadxonasi', 39.674, 66.995, 'uch_oyoq', 70, -1, 'M39 Toshkent yo''nalishi (Pistirma)', 650, TRUE),
  ('uz-sam-007', 'Lochin 70 - Samarqand Katta halqa yo''li', 39.685, 66.925, 'lochin', 70, -1, 'Samarqand aylanma halqa yo''li', 650, TRUE),
  ('uz-sam-008', 'YPX Patrul 360 - Samarqand Vokzal maydoni', 39.668, 66.928, 'patrul_360', 60, -1, 'Temiryo''l vokzali atrofi', 500, TRUE),
  ('uz-sam-009', 'Lochin 100 - M39 Samarqand - Jizzax trassasi', 39.725, 67.045, 'lochin', 100, -1, 'M39 Xalqaro trassa (Bulung''ur)', 850, TRUE),
  ('uz-sam-010', 'Lochin 100 - M37 Samarqand - Navoiy trassasi', 39.695, 66.825, 'lochin', 100, -1, 'M37 Kattaqo''rg''on yo''nalishi', 850, TRUE),
  ('uz-sam-urg-001', 'Lochin 60 - Urgut shahar Pochvon ko''chasi', 39.405, 67.245, 'lochin', 60, -1, 'Urgut markaziy bozor yo''li', 500, TRUE),
  ('uz-sam-kat-001', 'Lochin 60 - Kattaqo''rg''on Amir Temur ko''chasi', 39.895, 66.255, 'lochin', 60, -1, 'Kattaqo''rg''on shahar markazi', 500, TRUE),
  ('uz-sam-kat-002', 'Lochin 100 - M37 Kattaqo''rg''on aylanmasi', 39.925, 66.285, 'lochin', 100, -1, 'M37 Xalqaro trassa', 850, TRUE),
  ('uz-sam-pas-001', 'Lochin 60 - Pastdarg''om (Juma sh.) markazi', 39.715, 66.655, 'lochin', 60, -1, 'Juma shahar markaziy yo''li', 500, TRUE),
  ('uz-sam-jom-001', 'Lochin 70 - Jomboy M39 trassasi', 39.702, 67.095, 'lochin', 70, -1, 'M39 Jomboy aylanma yo''li', 650, TRUE),
  ('uz-sam-ish-001', 'Lochin 70 - Ishtixon M37 yo''li', 39.965, 66.485, 'lochin', 70, -1, 'M37 Ishtixon aylanmasi', 650, TRUE),
  ('uz-sam-oqd-001', 'Lochin 70 - Oqdaryo (Loyish) M37 yo''li', 39.785, 66.725, 'lochin', 70, -1, 'M37 Loyish aylanma yo''li', 650, TRUE),
  ('uz-sam-pay-001', 'Lochin 60 - Payariq (Chelak sh.) markazi', 39.925, 66.855, 'lochin', 60, -1, 'Chelak markaziy yo''li', 500, TRUE),
  ('uz-sam-toy-001', 'Lochin 60 - Toyloq markaziy yo''li', 39.585, 67.085, 'lochin', 60, -1, 'Samarqand - Urgut trassasi (Toyloq)', 500, TRUE),
  ('uz-sam-nar-001', 'Lochin 70 - Narpay (Oqtosh sh.) M37 yo''li', 40.045, 65.935, 'lochin', 70, -1, 'M37 Oqtosh magistrali', 650, TRUE),
  ('uz-sam-pax-001', 'Lochin 70 - Paxtachi (Ziyovuddin) posti', 40.035, 65.655, 'lochin', 70, -1, 'M37 Navoiy viloyat chegarasi', 650, TRUE),
  ('uz-bux-001', 'Lochin 60 - B. Naqshband ko''chasi', 39.7745, 64.428, 'lochin', 60, -1, 'Bahouddin Naqshband ko''chasi (Buxoro)', 500, TRUE),
  ('uz-bux-002', 'Lochin 60 - I. Somoniy ko''chasi', 39.768, 64.415, 'lochin', 60, -1, 'Ismoil Somoniy ko''chasi', 500, TRUE),
  ('uz-bux-003', 'Chorraha kamerasi - Navoiy va Naqshband', 39.772, 64.435, 'traffic_light', 60, -1, 'Markaziy chorraha', 450, TRUE),
  ('uz-bux-004', 'Lochin 100 - M37 Buxoro - Navoiy trassasi', 39.81, 64.52, 'lochin', 100, -1, 'M37 Katta trassa', 850, TRUE),
  ('uz-bux-005', 'Uch oyoq 70 - Buxoro aylanma yo''li', 39.75, 64.46, 'uch_oyoq', 70, -1, 'A380 yo''nalishi', 650, TRUE),
  ('uz-bux-gij-001', 'Lochin 60 - G''ijduvon Yusuf Hamadoniy ko''chasi', 40.102, 64.675, 'lochin', 60, -1, 'M37 G''ijduvon markaziy trassasi', 500, TRUE),
  ('uz-bux-kog-001', 'Lochin 60 - Kogon temiryo''l vokzali yo''li', 39.725, 64.545, 'lochin', 60, -1, 'Buxoro - Kogon trassasi', 500, TRUE),
  ('uz-bux-vob-001', 'Lochin 70 - Vobkent M37 aylanmasi', 39.955, 64.515, 'lochin', 70, -1, 'M37 Vobkent xalqaro yo''li', 650, TRUE),
  ('uz-bux-sho-001', 'Lochin 60 - Shofirkon tuman markazi', 40.125, 64.505, 'lochin', 60, -1, 'Shofirkon markaziy shoh ko''chasi', 500, TRUE),
  ('uz-bux-rom-001', 'Lochin 70 - Romitan A380 Gazli yo''li', 39.935, 64.385, 'lochin', 70, -1, 'A380 Xorazm yo''nalishi (Romitan)', 650, TRUE),
  ('uz-bux-jon-001', 'Lochin 70 - Jondor M37 magistrali', 39.735, 64.185, 'lochin', 70, -1, 'M37 Turkmaniston trassasi (Jondor)', 650, TRUE),
  ('uz-bux-qor-001', 'Lochin 60 - Qorako''l shahar markazi', 39.505, 63.855, 'lochin', 60, -1, 'Qorako''l shahar magistrali', 500, TRUE),
  ('uz-bux-olo-001', 'Lochin 70 - Olot chegara posti (Farob)', 39.415, 63.805, 'lochin', 70, -1, 'M37 Olot xalqaro bojxona yo''li', 700, TRUE),
  ('uz-bux-qrv-001', 'Lochin 70 - Qorovulbozor neft zavodi yo''li', 39.502, 64.795, 'lochin', 70, -1, 'A380 Qarshi yo''nalishi (Qorovulbozor)', 650, TRUE),
  ('uz-tas-001', 'Lochin 60 - Amir Temur shoh ko''chasi', 41.315, 69.282, 'lochin', 60, -1, 'Amir Temur shoh ko''chasi (Toshkent)', 500, TRUE),
  ('uz-tas-002', 'Lochin 60 - Mustaqillik shoh ko''chasi', 41.322, 69.295, 'lochin', 60, -1, 'Mustaqillik shoh ko''chasi', 500, TRUE),
  ('uz-tas-003', 'Chorraha kamerasi - Buyuk Ipak Yo''li', 41.328, 69.335, 'traffic_light', 60, -1, 'Buyuk Ipak Yo''li metro atrofi', 450, TRUE),
  ('uz-tas-004', 'Kamera orqadan oladi! - Bunyodkor ko''chasi', 41.275, 69.215, 'rear', 60, -1, 'Bunyodkor shoh ko''chasi (Orqadan)', 550, TRUE),
  ('uz-tas-005', 'Avtobus tasmasi - Alisher Navoiy ko''chasi', 41.318, 69.255, 'bus_lane', 60, -1, 'A. Navoiy shoh ko''chasi', 400, TRUE),
  ('uz-tas-006', 'Lochin 70 - Toshkent Kichik Halqa Yo''li (TKHY)', 41.345, 69.265, 'lochin', 70, -1, 'Shimoliy aylanma yo''l', 600, TRUE),
  ('uz-tas-007', 'Lochin 100 - Toshkent Katta Halqa Yo''li (THYo)', 41.235, 69.295, 'lochin', 100, -1, 'Sergeli THYo aylanmasi', 800, TRUE),
  ('uz-tas-008', 'YPX Patrul 360 - Chilonzor Oqtepa maydoni', 41.295, 69.22, 'patrul_360', 60, -1, 'Oqtepa aylanma yo''li', 500, TRUE),
  ('uz-tas-009', 'Lochin 100 - Yangi O''zbekiston ko''chasi', 41.365, 69.385, 'lochin', 100, -1, 'Yangi O''zbekiston bog''i trassasi', 850, TRUE),
  ('uz-tas-010', 'Ko''chma Uch oyoq 70 - Rohat aylanmasi', 41.265, 69.355, 'uch_oyoq', 70, -1, 'Ohangaron yo''li (Pistirma)', 650, TRUE),
  ('uz-tvo-chi-001', 'Lochin 60 - Chirchiq shahar A. Navoiy ko''chasi', 41.468, 69.585, 'lochin', 60, -1, 'Chirchiq shahar markazi', 500, TRUE),
  ('uz-tvo-bos-001', 'Lochin 70 - Bo''stonliq (G''azalkent - Chorvoq) yo''li', 41.565, 69.775, 'lochin', 70, -1, 'Chorvoq suv ombori trassasi', 650, TRUE),
  ('uz-tvo-ang-001', 'Lochin 70 - Angren sh. A373 Qamchiq dovoni posti', 41.015, 70.145, 'lochin', 70, -1, 'A373 Qamchiq dovoni kirish yo''li', 700, TRUE),
  ('uz-tvo-olm-001', 'Lochin 60 - Olmaliq Metallurglar shoh ko''chasi', 40.845, 69.605, 'lochin', 60, -1, 'Olmaliq markaziy shoh ko''chasi', 500, TRUE),
  ('uz-tvo-yan-001', 'Lochin 70 - Yangiyo''l M39 Samarqand trassasi', 41.115, 69.045, 'lochin', 70, -1, 'M39 Yangiyo''l aylanmasi', 650, TRUE),
  ('uz-tvo-chn-001', 'Lochin 70 - Chinoz ko''prigi M39 posti', 40.935, 68.755, 'lochin', 70, -1, 'M39 Sirdaryo daryosi ko''prigi (Chinoz)', 700, TRUE),
  ('uz-tvo-bek-001', 'Lochin 60 - Bekobod shahar markazi', 40.215, 69.255, 'lochin', 60, -1, 'Bekobod markaziy magistrali', 500, TRUE),
  ('uz-tvo-nur-001', 'Lochin 60 - Nurafshon (To''ytepa) markazi', 41.045, 69.355, 'lochin', 60, -1, 'Toshkent viloyati ma''muriy markazi', 500, TRUE),
  ('uz-tvo-par-001', 'Lochin 60 - Parkent markaziy yo''li', 41.295, 69.675, 'lochin', 60, -1, 'Parkent - So''qoq tog'' yo''li', 500, TRUE),
  ('uz-tvo-zan-001', 'Lochin 60 - Zangiota (Eshonguzar) yo''li', 41.245, 69.155, 'lochin', 60, -1, 'Zangiota ziyoratgohi atrofi', 500, TRUE),
  ('uz-fer-001', 'Lochin 60 - Al-Farg''oniy ko''chasi', 40.385, 71.785, 'lochin', 60, -1, 'Farg''ona markaziy xiyoboni', 500, TRUE),
  ('uz-fer-002', 'Lochin 70 - Farg''ona - Marg''ilon yo''li', 40.42, 71.745, 'lochin', 70, -1, 'Marg''ilon shoh ko''chasi', 600, TRUE),
  ('uz-fer-003', 'Lochin 100 - Qo''qon aylanma trassasi', 40.54, 70.95, 'lochin', 100, -1, 'A373 Qo''qon aylanmasi', 850, TRUE),
  ('uz-fer-mar-001', 'Lochin 60 - Marg''ilon B. Marg''iloniy ko''chasi', 40.472, 71.715, 'lochin', 60, -1, 'Marg''ilon shahar markazi', 500, TRUE),
  ('uz-fer-quv-001', 'Lochin 60 - Quva tuman markazi', 40.525, 72.065, 'lochin', 60, -1, 'Quva - Andijon yo''li', 500, TRUE),
  ('uz-fer-olt-001', 'Lochin 60 - Oltiariq markazi', 40.395, 71.485, 'lochin', 60, -1, 'Oltiariq uzumchilik markazi', 500, TRUE),
  ('uz-fer-ris-001', 'Lochin 60 - Rishton kulolchilik markazi', 40.355, 71.285, 'lochin', 60, -1, 'A373 Rishton aylanmasi', 500, TRUE),
  ('uz-fer-bes-001', 'Lochin 70 - Beshariq chegara yo''li', 40.435, 70.615, 'lochin', 70, -1, 'Beshariq - Konibodom yo''nalishi', 650, TRUE),
  ('uz-and-001', 'Lochin 60 - Bobur shoh ko''chasi', 40.785, 72.345, 'lochin', 60, -1, 'Andijon shahar markazi', 500, TRUE),
  ('uz-and-002', 'Chorraha kamerasi - Amir Temur va Bobur', 40.772, 72.355, 'traffic_light', 60, -1, 'Markaziy chorraha (Andijon)', 450, TRUE),
  ('uz-and-003', 'Lochin 100 - A373 Andijon - Asaka trassasi', 40.715, 72.31, 'lochin', 100, -1, 'A373 Asaka yo''nalishi', 850, TRUE),
  ('uz-and-asa-001', 'Lochin 60 - Asaka GM zavodi yo''li', 40.642, 72.245, 'lochin', 60, -1, 'Asaka avtomobil zavodi trassasi', 500, TRUE),
  ('uz-and-sha-001', 'Lochin 60 - Shahrixon shahar markazi', 40.712, 72.055, 'lochin', 60, -1, 'Shahrixon - Farg''ona yo''li', 500, TRUE),
  ('uz-and-xoj-001', 'Lochin 70 - Xo''jaobod Do''stlik posti', 40.665, 72.565, 'lochin', 70, -1, 'O''sh - Qirg''iziston chegara trassasi', 650, TRUE),
  ('uz-and-xon-001', 'Lochin 60 - Xonobod shahar kirish yo''li', 40.805, 72.985, 'lochin', 60, -1, 'Xonobod sanatoriy magistrali', 500, TRUE),
  ('uz-and-bal-001', 'Lochin 70 - Baliqchi Namangan chegarasi', 40.935, 71.915, 'lochin', 70, -1, 'Baliqchi - Namangan daryo ko''prigi', 650, TRUE),
  ('uz-nam-001', 'Lochin 60 - Navoiy ko''chasi', 41.002, 71.675, 'lochin', 60, -1, 'Namangan shahar markazi', 500, TRUE),
  ('uz-nam-002', 'Lochin 100 - Namangan - Pop trassasi', 41.025, 71.515, 'lochin', 100, -1, 'Qamchiq dovoni yo''nalishi', 850, TRUE),
  ('uz-nam-pop-001', 'Lochin 70 - Pop tumani A373 trassasi', 40.875, 71.105, 'lochin', 70, -1, 'A373 Qamchiq dovoni etagi', 700, TRUE),
  ('uz-nam-chu-001', 'Lochin 60 - Chust shahar markazi', 41.005, 71.225, 'lochin', 60, -1, 'Chust pichoqchilar shoh ko''chasi', 500, TRUE),
  ('uz-nam-tor-001', 'Lochin 70 - To''raqo''rg''on IES trassasi', 41.015, 71.555, 'lochin', 70, -1, 'To''raqo''rg''on issiqlik elektr stansiyasi yo''li', 650, TRUE),
  ('uz-nam-cho-001', 'Lochin 60 - Chortoq sanatoriy yo''li', 41.075, 71.815, 'lochin', 60, -1, 'Chortoq dam olish maskani trassasi', 500, TRUE),
  ('uz-nam-uch-001', 'Lochin 70 - Uchqo''rg''on Norin ko''prigi', 41.115, 72.075, 'lochin', 70, -1, 'Uchqo''rg''on daryo magistrali', 650, TRUE),
  ('uz-jiz-001', 'Lochin 60 - Sh. Rashidov shoh ko''chasi', 40.125, 67.842, 'lochin', 60, -1, 'Jizzax markaziy ko''chasi', 500, TRUE),
  ('uz-jiz-002', 'Lochin 100 - M39 Jizzax aylanma trassasi', 40.165, 67.895, 'lochin', 100, -1, 'M39 Jizzax aylanmasi', 850, TRUE),
  ('uz-jiz-gal-001', 'Lochin 70 - G''allaorol Sanzar dovoni (M39)', 40.025, 67.595, 'lochin', 70, -1, 'M39 Ilonuti darasi (Pistirma)', 700, TRUE),
  ('uz-jiz-zom-001', 'Lochin 60 - Zomin markaziy yo''li', 39.965, 68.395, 'lochin', 60, -1, 'Zomin milliy bog''i tog'' yo''li', 500, TRUE),
  ('uz-jiz-das-001', 'Lochin 70 - Dashtobod M39 trassasi', 40.155, 68.345, 'lochin', 70, -1, 'M39 Sirdaryo - Jizzax yo''li', 650, TRUE),
  ('uz-jiz-pax-001', 'Lochin 60 - Paxtakor tuman markazi', 40.315, 67.955, 'lochin', 60, -1, 'Paxtakor magistrali', 500, TRUE),
  ('uz-jiz-dos-001', 'Lochin 60 - Do''stlik shahar markazi', 40.525, 68.035, 'lochin', 60, -1, 'Do''stlik tumanlararo yo''li', 500, TRUE),
  ('uz-sir-001', 'Lochin 60 - Guliston shoh ko''chasi', 40.495, 68.785, 'lochin', 60, -1, 'Guliston shahar markazi', 500, TRUE),
  ('uz-sir-002', 'Lochin 100 - M34 Toshkent - Guliston trassasi', 40.54, 68.76, 'lochin', 100, -1, 'M34 trassa (Baxt sh.)', 850, TRUE),
  ('uz-sir-yan-001', 'Lochin 60 - Yangiyer shahar markazi (M34)', 40.275, 68.815, 'lochin', 60, -1, 'M34 Yangiyer xalqaro trassasi', 500, TRUE),
  ('uz-sir-sar-001', 'Lochin 70 - Sardoba M39 aylanmasi', 40.215, 68.175, 'lochin', 70, -1, 'M39 Sardoba suv ombori yo''li', 650, TRUE),
  ('uz-sir-srd-001', 'Lochin 70 - Sirdaryo shahar M34 va M39 chorrahasi', 40.845, 68.665, 'lochin', 70, -1, 'Sirdaryo xalqaro aylanma yo''li', 650, TRUE),
  ('uz-sir-xov-001', 'Lochin 60 - Xovos temiryo''l magistrali', 40.195, 68.865, 'lochin', 60, -1, 'Xovos - Tojikiston chegara yo''li', 500, TRUE),
  ('uz-nav-001', 'Lochin 60 - G''alaba shoh ko''chasi', 40.098, 65.375, 'lochin', 60, -1, 'Navoiy shahar markazi', 500, TRUE),
  ('uz-nav-002', 'Lochin 100 - M37 Navoiy - Karmana trassasi', 40.145, 65.355, 'lochin', 100, -1, 'M37 Karmana aylanmasi', 850, TRUE),
  ('uz-nav-qiz-001', 'Lochin 70 - Qiziltepa markazi', 40.035, 64.985, 'lochin', 70, -1, 'Navoiy - Buxoro yo''li (Qiziltepa)', 600, TRUE),
  ('uz-nav-xat-001', 'Lochin 60 - Xatirchi (Yangirabot) markazi', 40.025, 65.955, 'lochin', 60, -1, 'Xatirchi tumanlararo yo''li', 500, TRUE),
  ('uz-nav-nur-001', 'Lochin 60 - Nurota Chashma ziyoratgohi yo''li', 40.565, 65.685, 'lochin', 60, -1, 'Nurota shahar markazi', 500, TRUE),
  ('uz-nav-zar-001', 'Lochin 70 - Zarafshon A380 Qizilqum trassasi', 41.575, 64.205, 'lochin', 70, -1, 'A380 Zarafshon oltin koni yo''li', 700, TRUE),
  ('uz-nav-uch-001', 'Lochin 70 - Uchquduq A380 shimoliy trassasi', 42.155, 63.555, 'lochin', 70, -1, 'A380 Uchquduq - Nukus yo''li', 700, TRUE),
  ('uz-xva-001', 'Lochin 60 - Al-Xorazmiy shoh ko''chasi', 41.555, 60.625, 'lochin', 60, -1, 'Urganch markazi', 500, TRUE),
  ('uz-xva-002', 'Lochin 60 - Xiva Ichan Qal''a kirish yo''li', 41.378, 60.365, 'lochin', 60, -1, 'Urganch - Xiva trassasi', 500, TRUE),
  ('uz-xva-xon-001', 'Lochin 60 - Xonqa tuman markazi', 41.475, 60.775, 'lochin', 60, -1, 'Xonqa shahar magistrali', 500, TRUE),
  ('uz-xva-haz-001', 'Lochin 70 - Hazorasp A380 Buxoro yo''li', 41.315, 61.075, 'lochin', 70, -1, 'A380 Hazorasp aylanmasi', 650, TRUE),
  ('uz-xva-gur-001', 'Lochin 70 - Gurlan Amudaryo ko''prigi', 41.845, 60.395, 'lochin', 70, -1, 'Gurlan - Mang''it ko''prigi', 650, TRUE),
  ('uz-xva-sho-001', 'Lochin 60 - Shovot chegara posti', 41.655, 60.305, 'lochin', 60, -1, 'Turkmaniston Toshhovuz yo''li', 500, TRUE),
  ('uz-xva-qos-001', 'Lochin 60 - Qo''shko''pir markazi', 41.535, 60.345, 'lochin', 60, -1, 'Qo''shko''pir shahar yo''li', 500, TRUE),
  ('uz-xva-tup-001', 'Lochin 70 - Tuproqqal''a (Pitnak) A380 trassasi', 41.225, 61.315, 'lochin', 70, -1, 'Pitnak GM motor zavodi trassasi', 650, TRUE),
  ('uz-qr-001', 'Lochin 60 - Berdaq shoh ko''chasi', 42.465, 59.615, 'lochin', 60, -1, 'Nukus shahar markazi', 500, TRUE),
  ('uz-qr-002', 'Lochin 100 - A380 Nukus - To''rtko''l trassasi', 42.385, 59.72, 'lochin', 100, -1, 'A380 trassasi', 850, TRUE),
  ('uz-qr-tur-001', 'Lochin 60 - To''rtko''l shahar A380 aylanmasi', 41.555, 60.985, 'lochin', 60, -1, 'A380 To''rtko''l markaziy trassasi', 500, TRUE),
  ('uz-qr-ber-001', 'Lochin 70 - Beruniy Amudaryo ko''prigi (A380)', 41.695, 60.755, 'lochin', 70, -1, 'A380 Urganch - Beruniy yangi ko''prigi', 700, TRUE),
  ('uz-qr-xoj-001', 'Lochin 60 - Xo''jayli tuman markazi', 42.405, 59.455, 'lochin', 60, -1, 'Nukus - Xo''jayli magistrali', 500, TRUE),
  ('uz-qr-qon-001', 'Lochin 70 - Qo''ng''irot Ustyurt Qozog''iston trassasi', 43.045, 58.845, 'lochin', 70, -1, 'A380 Beyneu xalqaro yo''li', 750, TRUE),
  ('uz-qr-amu-001', 'Lochin 60 - Amudaryo (Mang''it) markazi', 42.115, 60.055, 'lochin', 60, -1, 'Mang''it shahar magistrali', 500, TRUE),
  ('uz-qr-chi-001', 'Lochin 60 - Chimboy shahar markazi', 42.945, 59.775, 'lochin', 60, -1, 'Chimboy markaziy yo''li', 500, TRUE),
  ('uz-qr-moy-001', 'Lochin 60 - Mo''ynoq kemalar qabristoni yo''li', 43.765, 59.025, 'lochin', 60, -1, 'Mo''ynoq Orol dengizi magistrali', 500, TRUE)
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  lat = EXCLUDED.lat,
  lng = EXCLUDED.lng,
  type = EXCLUDED.type,
  speed_limit = EXCLUDED.speed_limit,
  azimuth = EXCLUDED.azimuth,
  road_name = EXCLUDED.road_name,
  distance_alert_threshold = EXCLUDED.distance_alert_threshold,
  is_active = TRUE;
