import json
from pathlib import Path

with open("src/data/speedcams.json", "r", encoding="utf-8") as f:
    cams = json.load(f)

# Hududlar chegaralari (taxminiy bounding boxlar)
regions = {
    "Toshkent shahri": lambda c: 41.20 <= c["lat"] <= 41.40 and 69.15 <= c["lng"] <= 69.40,
    "Toshkent viloyati": lambda c: 40.5 <= c["lat"] <= 42.2 and 68.6 <= c["lng"] <= 70.8 and not (41.20 <= c["lat"] <= 41.40 and 69.15 <= c["lng"] <= 69.40),
    "Samarqand viloyati": lambda c: 39.1 <= c["lat"] <= 40.2 and 65.8 <= c["lng"] <= 67.5,
    "Farg'ona viloyati": lambda c: 40.0 <= c["lat"] <= 40.8 and 70.8 <= c["lng"] <= 72.0,
    "Andijon viloyati": lambda c: 40.5 <= c["lat"] <= 41.0 and 72.0 <= c["lng"] <= 72.7,
    "Namangan viloyati": lambda c: 40.8 <= c["lat"] <= 41.4 and 70.6 <= c["lng"] <= 71.8,
    "Qashqadaryo viloyati": lambda c: 38.2 <= c["lat"] <= 39.4 and 65.0 <= c["lng"] <= 67.2,
    "Surxondaryo viloyati": lambda c: (37.1 <= c["lat"] <= 38.6 and 66.5 <= c["lng"] <= 68.5) or c["id"].startswith("uz-sur"),
    "Buxoro viloyati": lambda c: 39.0 <= c["lat"] <= 40.5 and 63.5 <= c["lng"] <= 65.2,
    "Navoiy viloyati": lambda c: (39.8 <= c["lat"] <= 42.5 and 64.0 <= c["lng"] <= 66.2) or "nav" in c["id"],
    "Xorazm viloyati": lambda c: 41.0 <= c["lat"] <= 42.0 and 60.0 <= c["lng"] <= 61.5,
    "Qoraqalpog'iston": lambda c: 42.0 <= c["lat"] <= 45.5 and 56.0 <= c["lng"] <= 62.0,
    "Jizzax viloyati": lambda c: 39.8 <= c["lat"] <= 40.8 and 67.4 <= c["lng"] <= 68.8,
    "Sirdaryo viloyati": lambda c: 40.1 <= c["lat"] <= 40.9 and 68.4 <= c["lng"] <= 69.2
}

counts = {r: 0 for r in regions}
unmatched = 0

for c in cams:
    matched = False
    for r, fn in regions.items():
        if fn(c):
            counts[r] += 1
            matched = True
            break
    if not matched:
        unmatched += 1

print(f"Jami kameralar: {len(cams)}")
for r, cnt in sorted(counts.items(), key=lambda x: -x[1]):
    print(f"{r}: {cnt} ta radar")
print(f"Boshqa/Aniq bo'lmagan: {unmatched} ta")
