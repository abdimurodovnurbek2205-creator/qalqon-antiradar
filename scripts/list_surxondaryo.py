import json
from pathlib import Path

json_path = Path("src/data/speedcams.json")
with open(json_path, "r", encoding="utf-8") as f:
    cams = json.load(f)

# Surxondaryo hududi: Lat 37.15 - 38.55, Lng 66.5 - 68.35
sur_cams = []
for c in cams:
    if c["id"].startswith("uz-sur"):
        sur_cams.append(c)
    elif 37.15 <= c["lat"] <= 38.55 and 66.5 <= c["lng"] <= 68.35:
        sur_cams.append(c)

seen = set()
unique_sur = []
for c in sur_cams:
    if c["id"] not in seen:
        seen.add(c["id"])
        unique_sur.append(c)

print(f"Jami Surxondaryo kameralari: {len(unique_sur)}")
print("-" * 60)
for i, c in enumerate(unique_sur, 1):
    print(f"{i}. ID: {c['id']} | [{c['type'].upper()}] {c['name']} | Tezlik: {c['speedLimit']} km/h | Manzil: {c['roadName']} ({c['lat']}, {c['lng']})")
