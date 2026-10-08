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
