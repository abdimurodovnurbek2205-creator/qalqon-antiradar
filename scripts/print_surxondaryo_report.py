import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


json_path = Path("src/data/speedcams.json")
with open(json_path, "r", encoding="utf-8") as f:
    cams = json.load(f)

districts = {
    "1. Termiz shahri va Termiz tumani": ["uz-sur-ter", "Termiz"],
    "2. Bandixon tumani": ["uz-sur-ban", "Bandixon"],
    "3. Denov tumani": ["uz-sur-den", "Denov"],
    "4. Boysun tumani": ["uz-sur-boy", "Boysun"],
    "5. Jarqo'rg'on tumani": ["uz-sur-jar", "Jarqo"],
    "6. Qumqo'rg'on tumani": ["uz-sur-kum", "Qumqo"],
    "7. Sho'rchi tumani": ["uz-sur-sho", "Sho'r"],
    "8. Sherobod tumani": ["uz-sur-she", "Sherobod"],
    "9. Sariosiyo va Sharg'un": ["uz-sur-sar", "Sariosiyo", "Sharg'un"],
    "10. Uzun tumani": ["uz-sur-uzu", "Uzun"],
    "11. Oltinsoy tumani": ["uz-sur-olt", "Oltinsoy", "Qarluq"],
    "12. Angor tumani": ["uz-sur-ang", "Angor"],
    "13. Muzrabot tumani": ["uz-sur-muz", "Muzrabot", "Xalqobod"],
    "14. Qiziriq tumani": ["uz-sur-qiz", "Qiziriq", "Sariq"]
}

assigned = set()
total_matched = 0

for dname, keys in districts.items():
    matched = []
    for c in cams:
        if c["id"] in assigned:
            continue
        hit = False
        for k in keys:
            if k.lower() in c["id"].lower() or k.lower() in c["name"].lower() or k.lower() in c.get("roadName", "").lower():
                hit = True
                break
        if hit:
            matched.append(c)
            assigned.add(c["id"])
    total_matched += len(matched)
    print(f"\n========================================================")
    print(f"📍 {dname} ({len(matched)} ta radar)")
    print(f"========================================================")
    for idx, c in enumerate(matched, 1):
        icon = "🦅"
        if c["type"] == "uch_oyoq": icon = "📐"
        elif c["type"] == "traffic_light": icon = "🚦"
        elif c["type"] == "patrul_360": icon = "🚨"
        elif c["type"] == "rear": icon = "🔄"
        print(f" {idx}. {icon} {c['name']} [{c['speedLimit']} km/h] -> {c.get('roadName', '')} (Masofa: {c.get('distanceAlertThreshold', 500)}m)")

print(f"\n========================================================")
print(f"SURXONDARYO BO'YICHA JAMI RADARLAR: {total_matched} TA")
print(f"O'ZBEKISTON BO'YICHA JAMI RADARLAR BAZASI: {len(cams)} TA")
print(f"========================================================")
