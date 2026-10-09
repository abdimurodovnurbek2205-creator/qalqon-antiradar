import json
import math
import urllib.request
from pathlib import Path

# 1. OpenStreetMap dan O'zbekistonning barcha 576 ta kamerasini yuklab olish
url = "https://raw.githubusercontent.com/muminoff/uzbspeedcameradb/main/data/cameras.json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    osm_data = json.loads(r.read().decode("utf-8"))

# 2. Mavjud bazamizni ochish
json_path = Path("src/data/speedcams.json")
with open(json_path, "r", encoding="utf-8") as f:
    existing = json.load(f)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # radius in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

merged = list(existing)
added = 0

for item in osm_data:
    lat = item["latitude"]
    lng = item["longitude"]
    limit = item.get("speed_limit") or 60
    
    # 80 metr masofada takrorlanish (dublikat) bor-yo'qligini tekshirish
    dup = False
    for ex in existing:
        if haversine(lat, lng, ex["lat"], ex["lng"]) < 80:
            dup = True
            break
            
    if not dup:
        added += 1
        road = item.get("road_direction") or "O'zbekiston trassasi"
        cam_id = f"uz-osm-{item['id']}"
        cam_type = "lochin"
        if limit == 60 and ("chorraha" in road.lower() or "kesishma" in road.lower()):
            cam_type = "traffic_light"
        elif limit >= 100:
            cam_type = "lochin"
            
        merged.append({
            "id": cam_id,
            "name": f"Lochin {limit} - {road}",
            "lat": round(lat, 6),
            "lng": round(lng, 6),
            "type": cam_type,
            "speedLimit": limit,
            "azimuth": -1,
            "roadName": road,
            "distanceAlertThreshold": 750 if limit >= 100 else (650 if limit >= 70 else 500)
        })

# 3. Yangilangan barcha kameralarni speedcams.json ga saqlash
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Oldingi kameralar soni: {len(existing)}")
print(f"OpenStreetMap-dan yangi qo'shilgan: {added}")
print(f"JAMI O'ZBEKISTON BO'YICHA BIRLASHGAN RADARLAR: {len(merged)}")
