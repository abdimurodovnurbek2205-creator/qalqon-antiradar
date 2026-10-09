-- ============================================================
-- QALQON ANTIRADAR - TO'LIQ O'RNATISH (SCHEMA + 58 TA RADAR)
-- Ushbu barcha kodni Supabase SQL Editor-ga tashlab 'RUN' bosing!
-- ============================================================

-- 1. Jadvallarni yaratish
CREATE TABLE IF NOT EXISTS public.speed_cameras (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    lat DOUBLE PRECISION NOT NULL,
    lng DOUBLE PRECISION NOT NULL,
    type TEXT NOT NULL,
    speed_limit INT NOT NULL,
    azimuth INT DEFAULT -1,
    road_name TEXT,
    distance_alert_threshold INT DEFAULT 600,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_cameras_lat_lng ON public.speed_cameras (lat, lng);
CREATE INDEX IF NOT EXISTS idx_cameras_type ON public.speed_cameras (type);

-- 2. Haydovchilar belgilaydigan radarlar (Community)
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

-- 3. Xavfsizlik qoidalari (Row Level Security)
ALTER TABLE public.speed_cameras ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.community_reports ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Public read speed_cameras" ON public.speed_cameras;
CREATE POLICY "Public read speed_cameras" ON public.speed_cameras FOR SELECT USING (true);

DROP POLICY IF EXISTS "Public read community_reports" ON public.community_reports;
CREATE POLICY "Public read community_reports" ON public.community_reports FOR SELECT USING (true);

DROP POLICY IF EXISTS "Public insert community_reports" ON public.community_reports;
CREATE POLICY "Public insert community_reports" ON public.community_reports FOR INSERT WITH CHECK (true);

-- 4. O'zbekistonning barcha 58 ta radarlarini yuklash
INSERT INTO public.speed_cameras (id, name, lat, lng, type, speed_limit, azimuth, road_name, distance_alert_threshold, is_active)
VALUES
  ('uz-sam-001', 'Lochin 60 - Registon ko''chasi', 39.6548, 66.9752, 'lochin', 60, 90, 'Registon ko''chasi (Samarqand)', 500, TRUE),
  ('uz-sam-002', 'Chorraha kamerasi - Rudakiy va Gagarin', 39.658, 66.955, 'traffic_light', 60, 45, 'Rudakiy va Gagarin chorrahasi', 450, TRUE),
  ('uz-sam-003', 'Kamera orqadan oladi! - Beruniy ko''chasi', 39.664, 66.942, 'rear', 60, 315, 'Beruniy ko''chasi (Orqadan uradi)', 500, TRUE),
  ('uz-sam-004', 'Lochin 60 - Spitamen shoh ko''chasi', 39.645, 66.938, 'lochin', 60, 180, 'Spitamen shoh ko''chasi', 550, TRUE),
  ('uz-sam-005', 'Chorraha kamerasi - Dahbed va Registon', 39.661, 66.979, 'traffic_light', 60, 0, 'Dahbed ko''chasi chorrahasi', 450, TRUE),
  ('uz-sam-006', 'Ko''chma Uch oyoq 70 - Ulug''bek rasadxonasi', 39.674, 66.995, 'uch_oyoq', 70, 45, 'M39 Toshkent yo''nalishi (Pistirma)', 650, TRUE),
  ('uz-sam-007', 'Lochin 70 - Samarqand Katta halqa yo''li', 39.685, 66.925, 'lochin', 70, 270, 'Samarqand aylanma halqa yo''li', 650, TRUE),
  ('uz-sam-008', 'YPX Patrul 360 - Samarqand Vokzal maydoni', 39.668, 66.928, 'patrul_360', 60, 220, 'Temiryo''l vokzali atrofi', 500, TRUE),
  ('uz-sam-009', 'Lochin 100 - M39 Samarqand - Jizzax trassasi', 39.725, 67.045, 'lochin', 100, 50, 'M39 Xalqaro trassa (Bulung''ur)', 850, TRUE),
  ('uz-sam-010', 'Lochin 100 - M37 Samarqand - Navoiy trassasi', 39.695, 66.825, 'lochin', 100, 290, 'M37 Kattaqo''rg''on yo''nalishi', 850, TRUE),
  ('uz-sam-011', 'Lochin 60 - Mirzo Ulug''bek shoh ko''chasi', 39.6505, 66.9602, 'lochin', 60, 320, 'Mirzo Ulug''bek shoh ko''chasi', 500, TRUE),
  ('uz-sam-012', 'Chorraha kamerasi - Beruniy va Spitamen', 39.6595, 66.9315, 'traffic_light', 60, 110, 'Beruniy-Spitamen kesishmasi', 450, TRUE),
  ('uz-sam-013', 'Lochin 60 - Dahbed ko''chasi (Siyob bozori)', 39.6645, 66.983, 'lochin', 60, 20, 'Dahbed ko''chasi', 500, TRUE),
  ('uz-sam-014', 'Ko''chma Uch oyoq 60 - Narpay ko''chasi', 39.6385, 66.945, 'uch_oyoq', 60, 240, 'Narpay ko''chasi', 500, TRUE),
  ('uz-sam-015', 'Lochin 70 - Qorasuv massivi kirish yo''li', 39.678, 67.025, 'lochin', 70, 75, 'Qorasuv yangi shahar trassasi', 600, TRUE),
  ('uz-bux-001', 'Lochin 60 - B. Naqshband ko''chasi', 39.7745, 64.428, 'lochin', 60, 110, 'Bahouddin Naqshband ko''chasi (Buxoro)', 500, TRUE),
  ('uz-bux-002', 'Lochin 60 - I. Somoniy ko''chasi', 39.768, 64.415, 'lochin', 60, 200, 'Ismoil Somoniy ko''chasi', 500, TRUE),
  ('uz-bux-003', 'Chorraha kamerasi - Navoiy va Naqshband', 39.772, 64.435, 'traffic_light', 60, 85, 'Markaziy chorraha', 450, TRUE),
  ('uz-bux-004', 'Lochin 100 - M37 Buxoro - Navoiy trassasi', 39.81, 64.52, 'lochin', 100, 60, 'M37 Katta trassa', 850, TRUE),
  ('uz-bux-005', 'Uch oyoq 70 - Buxoro aylanma yo''li', 39.75, 64.46, 'uch_oyoq', 70, 140, 'A380 yo''nalishi', 650, TRUE),
  ('uz-tas-001', 'Lochin 60 - Amir Temur shoh ko''chasi', 41.315, 69.282, 'lochin', 60, 10, 'Amir Temur shoh ko''chasi (Toshkent)', 500, TRUE),
  ('uz-tas-002', 'Lochin 60 - Mustaqillik shoh ko''chasi', 41.322, 69.295, 'lochin', 60, 45, 'Mustaqillik shoh ko''chasi', 500, TRUE),
  ('uz-tas-003', 'Chorraha kamerasi - Buyuk Ipak Yo''li', 41.328, 69.335, 'traffic_light', 60, 70, 'Buyuk Ipak Yo''li metro atrofi', 450, TRUE),
  ('uz-tas-004', 'Kamera orqadan oladi! - Bunyodkor ko''chasi', 41.275, 69.215, 'rear', 60, 215, 'Bunyodkor shoh ko''chasi', 550, TRUE),
  ('uz-tas-005', 'Avtobus tasmasi - Alisher Navoiy ko''chasi', 41.318, 69.255, 'bus_lane', 60, 280, 'A. Navoiy shoh ko''chasi', 400, TRUE),
  ('uz-tas-006', 'Lochin 70 - Toshkent Kichik Halqa Yo''li (TKHY)', 41.345, 69.265, 'lochin', 70, 160, 'Shimoliy aylanma yo''l', 600, TRUE),
  ('uz-tas-007', 'Lochin 100 - Toshkent Katta Halqa Yo''li (THYo)', 41.235, 69.295, 'lochin', 100, 90, 'Sergeli THYo aylanmasi', 800, TRUE),
  ('uz-tas-008', 'YPX Patrul 360 - Chilonzor Oqtepa maydoni', 41.295, 69.22, 'patrul_360', 60, 130, 'Oqtepa aylanma yo''li', 500, TRUE),
  ('uz-tas-009', 'Lochin 100 - Yangi O''zbekiston ko''chasi', 41.365, 69.385, 'lochin', 100, 50, 'Yangi O''zbekiston bog''i trassasi', 850, TRUE),
  ('uz-tas-010', 'Ko''chma Uch oyoq 70 - Rohat aylanmasi', 41.265, 69.355, 'uch_oyoq', 70, 120, 'Ohangaron yo''li', 650, TRUE),
  ('uz-jiz-001', 'Lochin 60 - Sh. Rashidov shoh ko''chasi', 40.125, 67.842, 'lochin', 60, 30, 'Jizzax markaziy ko''chasi', 500, TRUE),
  ('uz-jiz-002', 'Lochin 100 - M39 Jizzax aylanma trassasi', 40.165, 67.895, 'lochin', 100, 75, 'M39 Jizzax aylanmasi', 850, TRUE),
  ('uz-sir-001', 'Lochin 60 - Guliston shoh ko''chasi', 40.495, 68.785, 'lochin', 60, 90, 'Guliston markazi', 500, TRUE),
  ('uz-sir-002', 'Lochin 100 - M34 Toshkent - Guliston trassasi', 40.54, 68.76, 'lochin', 100, 180, 'M34 trassa (Baxt)', 850, TRUE),
  ('uz-nav-001', 'Lochin 60 - G''alaba shoh ko''chasi', 40.098, 65.375, 'lochin', 60, 100, 'Navoiy shahar markazi', 500, TRUE),
  ('uz-nav-002', 'Lochin 100 - M37 Navoiy - Karmana trassasi', 40.145, 65.355, 'lochin', 100, 300, 'M37 Karmana aylanmasi', 850, TRUE),
  ('uz-qar-001', 'Lochin 60 - O''zbekiston ko''chasi', 38.855, 65.795, 'lochin', 60, 20, 'Qarshi markaziy ko''chasi', 500, TRUE),
  ('uz-qar-002', 'Lochin 100 - Qarshi - Shahrisabz yo''li', 38.89, 65.885, 'lochin', 100, 85, 'A378 Shahrisabz yo''nalishi', 850, TRUE),
  ('uz-ter-001', 'Lochin 60 - At-Termiziy shoh ko''chasi', 37.235, 67.28, 'lochin', 60, 110, 'Termiz shahar markazi', 500, TRUE),
  ('uz-ter-002', 'Lochin 100 - M39 Termiz aylanma yo''li', 37.285, 67.315, 'lochin', 100, 45, 'M39 Xalqaro trassa (Ayritom)', 850, TRUE),
  ('uz-and-001', 'Lochin 60 - Bobur shoh ko''chasi', 40.785, 72.345, 'lochin', 60, 40, 'Andijon shahar markazi', 500, TRUE),
  ('uz-and-002', 'Chorraha kamerasi - Amir Temur va Bobur', 40.772, 72.355, 'traffic_light', 60, 15, 'Markaziy chorraha (Andijon)', 450, TRUE),
  ('uz-and-003', 'Lochin 100 - A373 Andijon - Asaka trassasi', 40.715, 72.31, 'lochin', 100, 210, 'A373 Asaka yo''nalishi', 850, TRUE),
  ('uz-fer-001', 'Lochin 60 - Al-Farg''oniy ko''chasi', 40.385, 71.785, 'lochin', 60, 95, 'Farg''ona markaziy xiyoboni', 500, TRUE),
  ('uz-fer-002', 'Lochin 70 - Farg''ona - Marg''ilon yo''li', 40.42, 71.745, 'lochin', 70, 310, 'Marg''ilon shoh ko''chasi', 600, TRUE),
  ('uz-fer-003', 'Lochin 100 - Qo''qon aylanma trassasi', 40.54, 70.95, 'lochin', 100, 275, 'A373 Qo''qon aylanmasi', 850, TRUE),
  ('uz-nam-001', 'Lochin 60 - Navoiy ko''chasi', 41.002, 71.675, 'lochin', 60, 130, 'Namangan markazi', 500, TRUE),
  ('uz-nam-002', 'Lochin 100 - Namangan - Pop trassasi', 41.025, 71.515, 'lochin', 100, 260, 'Qamchiq dovoni yo''nalishi', 850, TRUE),
  ('uz-xva-001', 'Lochin 60 - Al-Xorazmiy shoh ko''chasi', 41.555, 60.625, 'lochin', 60, 70, 'Urganch markazi', 500, TRUE),
  ('uz-xva-002', 'Lochin 60 - Xiva Ichan Qal''a kirish yo''li', 41.378, 60.365, 'lochin', 60, 180, 'Urganch - Xiva trassasi', 500, TRUE),
  ('uz-qr-001', 'Lochin 60 - Berdaq shoh ko''chasi', 42.465, 59.615, 'lochin', 60, 5, 'Nukus shahar markazi', 500, TRUE),
  ('uz-qr-002', 'Lochin 100 - A380 Nukus - To''rtko''l trassasi', 42.385, 59.72, 'lochin', 100, 140, 'A380 trassasi', 850, TRUE),
  ('uz-sam-016', 'Lochin 70 - Samarqand Aeroport yo''li', 39.7, 66.985, 'lochin', 70, 10, 'Ibn Sino va Aeroport trassasi', 600, TRUE),
  ('uz-sam-017', 'Kamera orqadan oladi! - Gagarin ko''chasi', 39.672, 66.938, 'rear', 60, 190, 'Gagarin ko''chasi (Orqadan uradi)', 500, TRUE),
  ('uz-sam-018', 'Lochin 60 - Mir Sayyid Baraka ko''chasi', 39.6585, 66.968, 'lochin', 60, 85, 'Mir Sayyid Baraka ko''chasi', 500, TRUE),
  ('uz-sam-019', 'Lochin 60 - Firdavsiy ko''chasi', 39.648, 66.965, 'lochin', 60, 140, 'Firdavsiy ko''chasi', 500, TRUE),
  ('uz-tas-011', 'Lochin 60 - Nukus ko''chasi (Rossiya elchixonasi)', 41.298, 69.278, 'lochin', 60, 115, 'Nukus ko''chasi', 500, TRUE),
  ('uz-tas-012', 'Chorraha kamerasi - Oybek va Nukus', 41.295, 69.27, 'traffic_light', 60, 45, 'Oybek-Nukus chorrahasi', 450, TRUE)
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
