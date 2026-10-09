import json
from pathlib import Path

json_path = Path("src/data/speedcams.json")
with open(json_path, "r", encoding="utf-8") as f:
    cams = json.load(f)

existing_ids = {c["id"] for c in cams}

bonus_cams = [
    # Qamchiq dovoni strategik postlari va tunnellari
    {"id": "uz-dovon-001", "name": "Lochin 60 - Qamchiq dovoni 1-tunnel kirish", "lat": 41.1450, "lng": 70.5250, "type": "lochin", "speed": 60, "road": "A373 Qamchiq xavfli tunnel", "dist": 600},
    {"id": "uz-dovon-002", "name": "Ko'chma Uch oyoq 60 - Qamchiq dovoni Rezaksoy aylanmasi", "lat": 41.1150, "lng": 70.6250, "type": "uch_oyoq", "speed": 60, "road": "A373 Rezaksoy pistirmasi", "dist": 650},
    {"id": "uz-dovon-003", "name": "Lochin 60 - Qamchiq dovoni Sharshara kafesi atrofi", "lat": 41.1850, "lng": 70.4550, "type": "lochin", "speed": 60, "road": "A373 Sharshara dovon yo'li", "dist": 550},
    # Surxondaryo - Termiz va Bandixon qo'shimchalari
    {"id": "uz-sur-ter-025", "name": "Lochin 60 - Termiz Amudaryo sohil bo'yi ko'chasi", "lat": 37.2180, "lng": 67.2820, "type": "lochin", "speed": 60, "road": "Amudaryo sohil ko'chasi", "dist": 500},
    {"id": "uz-sur-ter-026", "name": "Lochin 70 - Termiz Janubiy temiryo'l ko'prigi trassasi", "lat": 37.2050, "lng": 67.2450, "type": "lochin", "speed": 70, "road": "Janubiy temiryo'l magistrali", "dist": 650},
    {"id": "uz-sur-ban-016", "name": "Lochin 60 - Bandixon Yangiobod mahallasi", "lat": 37.8480, "lng": 67.3720, "type": "lochin", "speed": 60, "road": "Yangiobod ichki yo'li", "dist": 450},
    {"id": "uz-sur-boy-012", "name": "Ko'chma Uch oyoq 70 - Boysun Bibishirin bulog'i yo'li", "lat": 38.2250, "lng": 67.2450, "type": "uch_oyoq", "speed": 70, "road": "Bibishirin ziyoratgohi pistirmasi", "dist": 650},
    # Samarqand va Qashqadaryo dovoni Taxtaqoracha
    {"id": "uz-sam-dov-001", "name": "Lochin 60 - Taxtaqoracha dovoni Omonqo'ton o'rmoni", "lat": 39.3150, "lng": 66.9250, "type": "lochin", "speed": 60, "road": "M39 Omonqo'ton dam olish zonasi", "dist": 600},
    {"id": "uz-sam-dov-002", "name": "Ko'chma Uch oyoq 60 - Qoratepa dovon burilishi", "lat": 39.3650, "lng": 66.9450, "type": "uch_oyoq", "speed": 60, "road": "M39 Qoratepa pistirmasi", "dist": 600},
    # Toshkent - Chorvoq
    {"id": "uz-tvo-bos-003", "name": "Lochin 60 - Chimyon - Amirsoy xalqaro tog' kurorti yo'li", "lat": 41.5150, "lng": 70.0150, "type": "lochin", "speed": 60, "road": "Amirsoy tog' kurorti trassasi", "dist": 550},
    {"id": "uz-tvo-bos-004", "name": "Ko'chma Uch oyoq 70 - Bo'stonliq Yusuflar aylanmasi", "lat": 41.5950, "lng": 69.8850, "type": "uch_oyoq", "speed": 70, "road": "Chorvoq tezyurar pistirmasi", "dist": 650},
    # Farg'ona vodiysi
    {"id": "uz-fer-sh-005", "name": "Lochin 60 - Farg'ona Yangi Asr shoh ko'chasi", "lat": 40.3750, "lng": 71.8050, "type": "lochin", "speed": 60, "road": "Yangi Asr shoh ko'chasi", "dist": 500},
    {"id": "uz-and-sh-006", "name": "Lochin 60 - Andijon Bog'ishamol dam olish maskani yo'li", "lat": 40.7350, "lng": 72.3750, "type": "lochin", "speed": 60, "road": "Bog'ishamol ko'chasi", "dist": 500},
    {"id": "uz-nam-sh-006", "name": "Lochin 60 - Namangan Afsonalar Vodiysi parki atrofi", "lat": 40.9750, "lng": 71.6150, "type": "lochin", "speed": 60, "road": "Afsonalar vodiysi trassasi", "dist": 500},
    # Xorazm va Buxoro
    {"id": "uz-xor-urg-004", "name": "Lochin 60 - Urganch Shovot kanali bo'yi xiyoboni", "lat": 41.5620, "lng": 60.6120, "type": "lochin", "speed": 60, "road": "Shovot kanali ko'chasi", "dist": 500},
    {"id": "uz-bux-sh-010", "name": "Lochin 60 - Buxoro Ark qal'asi va Registon maydoni", "lat": 39.7780, "lng": 64.4110, "type": "lochin", "speed": 60, "road": "Ark maydoni ko'chasi", "dist": 450}
]

added = 0
for item in bonus_cams:
    if item["id"] not in existing_ids:
        cams.append({
            "id": item["id"],
            "name": item["name"],
            "lat": round(item["lat"], 6),
            "lng": round(item["lng"], 6),
            "type": item["type"],
            "speedLimit": item["speed"],
            "azimuth": -1,
            "roadName": item["road"],
            "distanceAlertThreshold": item["dist"]
        })
        existing_ids.add(item["id"])
        added += 1

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(cams, f, ensure_ascii=False, indent=2)

print(f"Bonus qo'shildi: {added}")
print(f"JAMI O'ZBEKISTON RADARLARI: {len(cams)} TA!")
