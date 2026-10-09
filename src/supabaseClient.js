/**
 * QALQON ANTIRADAR - SUPABASE REAL-TIME CLOUD CLIENT
 * O'zbekiston radarlarini bulut bilan sinxronlash va haydovchilar hamjamiyati (Community)
 */

const SUPABASE_STORAGE_KEY_URL = 'qalqon_supabase_url';
const SUPABASE_STORAGE_KEY_KEY = 'qalqon_supabase_anon_key';
const LOCAL_CAMERAS_CACHE_KEY = 'qalqon_cached_cameras';
const PENDING_REPORTS_KEY = 'qalqon_pending_reports';

// Standart konfiguratsiya (Settings orqali o'zgartirish mumkin)
const DEFAULT_SUPABASE_URL = 'https://khfpsjlelicajcycjrag.supabase.co';
let currentSupabaseUrl = localStorage.getItem(SUPABASE_STORAGE_KEY_URL) || DEFAULT_SUPABASE_URL;
let currentSupabaseKey = localStorage.getItem(SUPABASE_STORAGE_KEY_KEY) || '';

let supabaseClient = null;
let realtimeChannel = null;

/**
 * Supabase mijozini ishga tushirish
 */
function initSupabaseClient(url, key) {
  if (url && key && window.supabase) {
    try {
      supabaseClient = window.supabase.createClient(url, key, {
        auth: { persistSession: false }
      });
      console.log('✅ Supabase mijozi muvaffaqiyatli ishga tushirildi:', url);
      return true;
    } catch (err) {
      console.warn('⚠️ Supabase initsializatsiya xatosi:', err);
      supabaseClient = null;
      return false;
    }
  }
  return false;
}

// Sahifa yuklanganda mavjud kalitlar bo'lsa ishga tushirish
if (currentSupabaseUrl && currentSupabaseKey) {
  initSupabaseClient(currentSupabaseUrl, currentSupabaseKey);
}

/**
 * Supabase sozlamalarini saqlash
 */
function configureSupabase(url, key) {
  currentSupabaseUrl = (url || '').trim();
  currentSupabaseKey = (key || '').trim();
  
  if (currentSupabaseUrl) localStorage.setItem(SUPABASE_STORAGE_KEY_URL, currentSupabaseUrl);
  else localStorage.removeItem(SUPABASE_STORAGE_KEY_URL);
  
  if (currentSupabaseKey) localStorage.setItem(SUPABASE_STORAGE_KEY_KEY, currentSupabaseKey);
  else localStorage.removeItem(SUPABASE_STORAGE_KEY_KEY);
  
  return initSupabaseClient(currentSupabaseUrl, currentSupabaseKey);
}

/**
 * Bulutdan radarlarni yuklab olish (Supabase speed_cameras + community_reports)
 * @returns {Promise<Array>} Radarlar ro'yxati
 */
async function fetchCamerasFromCloud() {
  if (!supabaseClient) {
    // Agar bulut ulanmagan bo'lsa, lokal kesh yoki speedcams.json qaytariladi
    return getCachedCameras();
  }

  try {
    // 1. Asosiy statsionar radarlar
    const { data: mainCams, error: mainErr } = await supabaseClient
      .from('speed_cameras')
      .select('*')
      .eq('is_active', true);

    if (mainErr) throw mainErr;

    // 2. Haydovchilar belgilagan yangi radarlar
    const { data: communityCams, error: commErr } = await supabaseClient
      .from('community_reports')
      .select('*')
      .order('reported_at', { ascending: false })
      .limit(100);

    const formattedMain = (mainCams || []).map(c => ({
      id: c.id,
      name: c.name,
      lat: c.lat,
      lng: c.lng,
      type: c.type,
      speedLimit: c.speed_limit,
      azimuth: c.azimuth,
      roadName: c.road_name,
      distanceAlertThreshold: c.distance_alert_threshold || 600
    }));

    const formattedCommunity = (communityCams || []).map(c => ({
      id: `comm-${c.id}`,
      name: `⚠️ ${c.type === 'uch_oyoq' ? 'Uch oyoq radar' : c.type === 'patrul_360' ? 'Patrul 360' : 'Yangi radar'}`,
      lat: c.lat,
      lng: c.lng,
      type: c.type || 'uch_oyoq',
      speedLimit: c.speed_limit || 60,
      azimuth: -1,
      roadName: c.road_name || 'Haydovchilar belgilagan',
      distanceAlertThreshold: 550,
      isCommunity: true
    }));

    const combined = [...formattedMain, ...formattedCommunity];
    
    // Offline uchun keshga saqlash
    if (combined.length > 0) {
      localStorage.setItem(LOCAL_CAMERAS_CACHE_KEY, JSON.stringify(combined));
    }

    // Navbatda qolgan offline hisobotlarni yuborish
    flushPendingReports();

    return combined;
  } catch (error) {
    console.warn('⚠️ Supabase-dan olishda xatolik, keshdan foydalaniladi:', error.message);
    return getCachedCameras();
  }
}

/**
 * Lokal keshdagi radarlarni olish
 */
function getCachedCameras() {
  const cached = localStorage.getItem(LOCAL_CAMERAS_CACHE_KEY);
  if (cached) {
    try {
      return JSON.parse(cached);
    } catch (e) {
      // ignore
    }
  }
  return null;
}

/**
 * Haydovchi tomonidan yangi radar yoki patrul belgilash
 */
async function reportCameraToCloud(reportData) {
  const payload = {
    lat: reportData.lat,
    lng: reportData.lng,
    type: reportData.type || 'uch_oyoq',
    speed_limit: reportData.speedLimit || 60,
    road_name: reportData.roadName || 'Aniqlanmagan yo\'l',
    description: reportData.description || 'Haydovchi tomonidan belgilandi'
  };

  if (!supabaseClient) {
    // Bulut ulanmagan bo'lsa, navbatga saqlash
    savePendingReport(payload);
    return { success: true, offline: true, message: "Lokal navbatga saqlandi (Internet ulanganda yuboriladi)" };
  }

  try {
    const { data, error } = await supabaseClient
      .from('community_reports')
      .insert([payload])
      .select();

    if (error) throw error;
    return { success: true, offline: false, data: data[0] };
  } catch (err) {
    console.warn('⚠️ Belgilashda xatolik, navbatga saqlandi:', err.message);
    savePendingReport(payload);
    return { success: true, offline: true, error: err.message };
  }
}

/**
 * Navbatdagi hisobotlarni saqlash va sinxronlash
 */
function savePendingReport(report) {
  try {
    const pending = JSON.parse(localStorage.getItem(PENDING_REPORTS_KEY) || '[]');
    pending.push(report);
    localStorage.setItem(PENDING_REPORTS_KEY, JSON.stringify(pending));
  } catch (e) {}
}

async function flushPendingReports() {
  if (!supabaseClient) return;
  try {
    const pending = JSON.parse(localStorage.getItem(PENDING_REPORTS_KEY) || '[]');
    if (pending.length === 0) return;

    const { error } = await supabaseClient.from('community_reports').insert(pending);
    if (!error) {
      console.log(`✅ ${pending.length} ta navbatdagi radar bulutga yuklandi!`);
      localStorage.removeItem(PENDING_REPORTS_KEY);
    }
  } catch (e) {
    console.warn('Navbatni yuklashda xatolik:', e);
  }
}

/**
 * Real-vaqt hodisalariga obuna bo'lish (Yangi radar paydo bo'lganda darhol xabardor qilish)
 */
function subscribeToCommunityUpdates(onNewRadarCallback) {
  if (!supabaseClient) return;

  if (realtimeChannel) {
    realtimeChannel.unsubscribe();
  }

  realtimeChannel = supabaseClient
    .channel('public:community_reports')
    .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'community_reports' }, payload => {
      console.log('🚨 Jonli yangi radar keldi:', payload.new);
      if (onNewRadarCallback && typeof onNewRadarCallback === 'function') {
        const item = payload.new;
        onNewRadarCallback({
          id: `comm-${item.id}`,
          name: `⚠️ ${item.type === 'uch_oyoq' ? 'Uch oyoq radar' : 'Yangi radar'}`,
          lat: item.lat,
          lng: item.lng,
          type: item.type,
          speedLimit: item.speed_limit,
          roadName: item.road_name,
          distanceAlertThreshold: 550,
          isCommunity: true
        });
      }
    })
    .subscribe();
}

// Global obyektga eksport qilish
window.QalqonCloud = {
  init: initSupabaseClient,
  configure: configureSupabase,
  fetchCameras: fetchCamerasFromCloud,
  reportCamera: reportCameraToCloud,
  subscribe: subscribeToCommunityUpdates,
  getCached: getCachedCameras,
  isConfigured: () => Boolean(supabaseClient),
  getConfig: () => ({
    url: currentSupabaseUrl,
    key: currentSupabaseKey
  })
};
