import json
from pathlib import Path

json_path = Path(r"c:\Users\Karantin.uz\Desktop\Antiradar\src\data\speedcams.json")
output_path = Path(r"c:\Users\Karantin.uz\Desktop\Antiradar\supabase\seed_cameras.sql")

with open(json_path, "r", encoding="utf-8") as f:
    cameras = json.load(f)

lines = [
    "-- ============================================================",
    "-- QALQON ANTIRADAR - O'ZBEKISTON RADARLAR BAZASI (58 TA KAMERA)",
    "-- Ushbu kodni Supabase SQL Editorga tashlab 'RUN' bosing",
    "-- ============================================================",
    "",
    "INSERT INTO public.speed_cameras (id, name, lat, lng, type, speed_limit, azimuth, road_name, distance_alert_threshold, is_active)",
    "VALUES"
]

val_rows = []
for cam in cameras:
    cid = cam.get("id", "").replace("'", "''")
    name = cam.get("name", "").replace("'", "''")
    lat = cam.get("lat", 0.0)
    lng = cam.get("lng", 0.0)
    ctype = cam.get("type", "lochin").replace("'", "''")
    speed_limit = cam.get("speedLimit", 60)
    azimuth = cam.get("azimuth", -1)
    road_name = cam.get("roadName", "").replace("'", "''")
    threshold = cam.get("distanceAlertThreshold", 600)
    
    val_rows.append(f"  ('{cid}', '{name}', {lat}, {lng}, '{ctype}', {speed_limit}, {azimuth}, '{road_name}', {threshold}, TRUE)")

lines.append(",\n".join(val_rows))
lines.append("ON CONFLICT (id) DO UPDATE SET")
lines.append("  name = EXCLUDED.name,")
lines.append("  lat = EXCLUDED.lat,")
lines.append("  lng = EXCLUDED.lng,")
lines.append("  type = EXCLUDED.type,")
lines.append("  speed_limit = EXCLUDED.speed_limit,")
lines.append("  azimuth = EXCLUDED.azimuth,")
lines.append("  road_name = EXCLUDED.road_name,")
lines.append("  distance_alert_threshold = EXCLUDED.distance_alert_threshold,")
lines.append("  is_active = TRUE;")
lines.append("")

output_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Generated {len(cameras)} cameras into {output_path}")
