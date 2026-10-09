"""
SURXONDARYO VILOYATINING BARCHA TUMANLARI BO'YICHA TO'LIQ VA ZICH RADARLAR TARMOG'I
Har bir tuman markazi, maktab/shifoxona zonalari, gavjum chorrahalar va pistirmalar
"""

import json
from pathlib import Path

json_path = Path("src/data/speedcams.json")
with open(json_path, "r", encoding="utf-8") as f:
    cams = json.load(f)

existing_ids = {c["id"] for c in cams}

detailed_sur_cams = [
    # ==================== 1. DENOV TUMANI (15 TA) ====================
    {"id": "uz-sur-den-001", "name": "Lochin 60 - Denov Sh. Rashidov shoh ko'chasi", "lat": 38.2750, "lng": 67.8950, "type": "lochin", "speed": 60, "road": "Denov shahar markazi", "dist": 500},
    {"id": "uz-sur-den-002", "name": "Chorraha 60 - Buyuk Ipak Yo'li va Mustaqillik", "lat": 38.2820, "lng": 67.8820, "type": "traffic_light", "speed": 60, "road": "Denov markaziy aylanmasi", "dist": 450},
    {"id": "uz-sur-den-003", "name": "Lochin 50 - Denov Markaziy dehqon bozori atrofi", "lat": 38.2680, "lng": 67.9020, "type": "lochin", "speed": 50, "road": "Denov katta bozori yo'li", "dist": 450},
    {"id": "uz-sur-den-004", "name": "Lochin 60 - Alisher Navoiy ko'chasi (Vokzal yo'li)", "lat": 38.2710, "lng": 67.8880, "type": "lochin", "speed": 60, "road": "Denov temiryo'l vokzali yo'li", "dist": 500},
    {"id": "uz-sur-den-005", "name": "Lochin 70 - M41 Sho'rchi yo'nalishi kirish posti", "lat": 38.2350, "lng": 67.8650, "type": "lochin", "speed": 70, "road": "M41 Denov janubiy kirish posti", "dist": 650},
    {"id": "uz-sur-den-006", "name": "Lochin 70 - M41 Sariosiyo yo'nalishi chiqish posti", "lat": 38.3150, "lng": 67.9250, "type": "lochin", "speed": 70, "road": "M41 Sariosiyo chiqish magistrali", "dist": 650},
    {"id": "uz-sur-den-007", "name": "Kamera orqadan oladi! (Rear 60) - Sh. Rashidov ko'chasi", "lat": 38.2790, "lng": 67.8910, "type": "rear", "speed": 60, "road": "Sh. Rashidov ko'chasi (Orqadan uradi)", "dist": 500},
    {"id": "uz-sur-den-008", "name": "Ko'chma Uch oyoq 70 - Qiziljar aylanmasi M41", "lat": 38.2250, "lng": 67.8520, "type": "uch_oyoq", "speed": 70, "road": "M41 Qiziljar aylanmasi (Pistirma)", "dist": 650},
    {"id": "uz-sur-den-009", "name": "Lochin 60 - Oltinsoy yo'li (G'alaba ko'chasi)", "lat": 38.2880, "lng": 67.8650, "type": "lochin", "speed": 60, "road": "Denov - Oltinsoy tumanlararo yo'li", "dist": 500},
    {"id": "uz-sur-den-010", "name": "Chorraha 60 - Sharafiddin Ali Yazdiy ko'chasi", "lat": 38.2620, "lng": 67.8960, "type": "traffic_light", "speed": 60, "road": "Denov janubiy chorrahasi", "dist": 450},
    {"id": "uz-sur-den-011", "name": "YPX Patrul 360 - Denov aylanma halqa yo'li", "lat": 38.2950, "lng": 67.9150, "type": "patrul_360", "speed": 60, "road": "Denov shimoliy halqa yo'li", "dist": 500},
    {"id": "uz-sur-den-012", "name": "Lochin 50 - Denov Markaziy shifoxonasi oldi", "lat": 38.2580, "lng": 67.8780, "type": "lochin", "speed": 50, "road": "Tuman shifoxona zonasi", "dist": 450},
    {"id": "uz-sur-den-013", "name": "Lochin 60 - Sina qishlog'i yo'nalishi", "lat": 38.3050, "lng": 67.8450, "type": "lochin", "speed": 60, "road": "Sina tog'oldi yo'li", "dist": 500},
    {"id": "uz-sur-den-014", "name": "Lochin 70 - Denov IES va sanoat zonasi yo'li", "lat": 38.2480, "lng": 67.9250, "type": "lochin", "speed": 70, "road": "Denov sanoat magistrali", "dist": 650},
    {"id": "uz-sur-den-015", "name": "Lochin 60 - Denov pedagogika instituti oldi", "lat": 38.2730, "lng": 67.8720, "type": "lochin", "speed": 60, "road": "DenPI talabalar shaharchasi", "dist": 500},

    # ==================== 2. BOYSUN TUMANI (8 TA) ====================
    {"id": "uz-sur-boy-001", "name": "Lochin 70 - M39 Darband kirish posti", "lat": 38.2050, "lng": 67.2050, "type": "lochin", "speed": 70, "road": "M39 Darband - Boysun trassasi", "dist": 650},
    {"id": "uz-sur-boy-002", "name": "Ko'chma Uch oyoq 70 - M39 Sayrob dovoni (Sayrob archasi)", "lat": 38.0150, "lng": 67.1450, "type": "uch_oyoq", "speed": 70, "road": "M39 Sayrob dovoni (Pistirma)", "dist": 650},
    {"id": "uz-sur-boy-003", "name": "Lochin 60 - Boysun shahar markazi (Mustaqillik)", "lat": 38.2050, "lng": 67.2250, "type": "lochin", "speed": 60, "road": "Boysun markaziy ko'chasi", "dist": 500},
    {"id": "uz-sur-boy-004", "name": "Lochin 60 - Boysun san'at saroyi va Baxshilar maydoni", "lat": 38.2010, "lng": 67.2180, "type": "lochin", "speed": 60, "road": "Baxshichilik markazi yo'li", "dist": 500},
    {"id": "uz-sur-boy-005", "name": "Lochin 70 - M39 Darband - Qashqadaryo dovoni posti", "lat": 38.2450, "lng": 67.1850, "type": "lochin", "speed": 70, "road": "M39 Oqrabot / Dehqonobod yo'nalishi", "dist": 700},
    {"id": "uz-sur-boy-006", "name": "Ko'chma Uch oyoq 70 - Bandixon - Boysun 4R100 tog' etagi", "lat": 38.1450, "lng": 67.2650, "type": "uch_oyoq", "speed": 70, "road": "4R100 tog' etagi pistirmasi", "dist": 650},
    {"id": "uz-sur-boy-007", "name": "Lochin 60 - Inkobod qishlog'i yo'li", "lat": 38.1750, "lng": 67.2350, "type": "lochin", "speed": 60, "road": "Inkobod aholi punkti trassasi", "dist": 500},
    {"id": "uz-sur-boy-008", "name": "YPX Patrul 360 - Boysun Olabo'ka aylanmasi", "lat": 38.1880, "lng": 67.1950, "type": "patrul_360", "speed": 60, "road": "Olabo'ka chorrahasi", "dist": 500},

    # ==================== 3. JARQO'RG'ON TUMANI (8 TA) ====================
    {"id": "uz-sur-jar-001", "name": "Lochin 70 - M41 Jarqo'rg'on Surxon daryosi ko'prigi", "lat": 37.5050, "lng": 67.4150, "type": "lochin", "speed": 70, "road": "M41 Jarqo'rg'on ko'prigi", "dist": 650},
    {"id": "uz-sur-jar-002", "name": "Lochin 60 - Jarqo'rg'on markaziy Mustaqillik shoh ko'chasi", "lat": 37.5120, "lng": 67.4220, "type": "lochin", "speed": 60, "road": "Jarqo'rg'on shahar markazi", "dist": 500},
    {"id": "uz-sur-jar-003", "name": "Chorraha 60 - Jarqo'rg'on markaziy aylanmasi (Minor yo'li)", "lat": 37.5180, "lng": 67.4180, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-sur-jar-004", "name": "Lochin 60 - Jarqo'rg'on Minorasi ziyoratgohi yo'li", "lat": 37.5020, "lng": 67.4320, "type": "lochin", "speed": 60, "road": "12-asr Jarqo'rg'on minorasi yo'li", "dist": 500},
    {"id": "uz-sur-jar-005", "name": "Lochin 70 - M41 Qumqo'rg'on yo'nalishi chiqish posti", "lat": 37.5650, "lng": 67.4550, "type": "lochin", "speed": 70, "road": "M41 Qumqo'rg'on trassasi", "dist": 650},
    {"id": "uz-sur-jar-006", "name": "Lochin 70 - 4R105 Bandixon yo'nalishi kirish posti", "lat": 37.5450, "lng": 67.3950, "type": "lochin", "speed": 70, "road": "4R105 Bandixon trassasi", "dist": 650},
    {"id": "uz-sur-jar-007", "name": "Ko'chma Uch oyoq 70 - Surxon neft bazasi trassasi", "lat": 37.4850, "lng": 67.3850, "type": "uch_oyoq", "speed": 70, "road": "Neft bazasi yo'li pistirmasi", "dist": 650},
    {"id": "uz-sur-jar-008", "name": "Kamera orqadan oladi! (Rear 60) - Jarqo'rg'on markazi", "lat": 37.5090, "lng": 67.4250, "type": "rear", "speed": 60, "road": "Mustaqillik ko'chasi (Orqadan)", "dist": 500},

    # ==================== 4. QUMQO'RG'ON TUMANI (8 TA) ====================
    {"id": "uz-sur-kum-001", "name": "Lochin 70 - Qumqo'rg'on M41 trassasi", "lat": 37.8150, "lng": 67.5850, "type": "lochin", "speed": 70, "road": "M41 Termiz - Denov yo'li", "dist": 650},
    {"id": "uz-sur-kum-002", "name": "Lochin 60 - Qumqo'rg'on shahar Mustaqillik ko'chasi", "lat": 37.8220, "lng": 67.5920, "type": "lochin", "speed": 60, "road": "Qumqo'rg'on markazi", "dist": 500},
    {"id": "uz-sur-kum-003", "name": "Chorraha 60 - Qumqo'rg'on Sho'rchi va Bandixon yo'li ayrisi", "lat": 37.8290, "lng": 67.5810, "type": "traffic_light", "speed": 60, "road": "Tuman markazi aylanmasi", "dist": 450},
    {"id": "uz-sur-kum-004", "name": "Lochin 70 - Elbayan qishlog'i M41 trassasi", "lat": 37.8650, "lng": 67.6150, "type": "lochin", "speed": 70, "road": "M41 Elbayan qishlog'i", "dist": 650},
    {"id": "uz-sur-kum-005", "name": "Ko'chma Uch oyoq 70 - Janubiy Surxon suv ombori yo'li", "lat": 37.7650, "lng": 67.5450, "type": "uch_oyoq", "speed": 70, "road": "Suv ombori magistrali (Pistirma)", "dist": 650},
    {"id": "uz-sur-kum-006", "name": "Lochin 70 - M41 Jarqo'rg'on chegarasi posti", "lat": 37.7450, "lng": 67.5150, "type": "lochin", "speed": 70, "road": "M41 Jarqo'rg'on posti", "dist": 650},
    {"id": "uz-sur-kum-007", "name": "Lochin 60 - Qumqo'rg'on dehqon bozori atrofi", "lat": 37.8180, "lng": 67.5980, "type": "lochin", "speed": 60, "road": "Dehqon bozori ko'chasi", "dist": 450},
    {"id": "uz-sur-kum-008", "name": "YPX Patrul 360 - Qumqo'rg'on aylanma halqa yo'li", "lat": 37.8350, "lng": 67.6050, "type": "patrul_360", "speed": 60, "road": "Qumqo'rg'on halqa yo'li", "dist": 500},

    # ==================== 5. SHO'RCHI TUMANI (8 TA) ====================
    {"id": "uz-sur-sho-001", "name": "Lochin 60 - M41 Sho'rchi markaziy shoh ko'chasi", "lat": 38.0120, "lng": 67.7850, "type": "lochin", "speed": 60, "road": "Sho'rchi shahar markazi", "dist": 500},
    {"id": "uz-sur-sho-002", "name": "Chorraha 60 - Sho'rchi va Oltinsoy yo'li chorrahasi", "lat": 38.0190, "lng": 67.7780, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-sur-sho-003", "name": "Lochin 70 - M41 Denov yo'nalishi chiqish posti", "lat": 38.0550, "lng": 67.8150, "type": "lochin", "speed": 70, "road": "M41 Denov yo'nalishi", "dist": 650},
    {"id": "uz-sur-sho-004", "name": "Lochin 70 - M41 Qumqo'rg'on yo'nalishi kirish posti", "lat": 37.9650, "lng": 67.7450, "type": "lochin", "speed": 70, "road": "M41 Qumqo'rg'on yo'nalishi", "dist": 650},
    {"id": "uz-sur-sho-005", "name": "Lochin 60 - Sho'rchi dehqon bozori va vokzal yo'li", "lat": 38.0050, "lng": 67.7920, "type": "lochin", "speed": 60, "road": "Sho'rchi bozor yo'li", "dist": 500},
    {"id": "uz-sur-sho-006", "name": "Ko'chma Uch oyoq 70 - Yallachi qishlog'i M41 trassasi", "lat": 38.0350, "lng": 67.7980, "type": "uch_oyoq", "speed": 70, "road": "M41 Yallachi pistirmasi", "dist": 650},
    {"id": "uz-sur-sho-007", "name": "Kamera orqadan oladi! (Rear 60) - Sho'rchi markazi", "lat": 38.0150, "lng": 67.7810, "type": "rear", "speed": 60, "road": "Sho'rchi markazi (Orqadan)", "dist": 500},
    {"id": "uz-sur-sho-008", "name": "Lochin 50 - Sho'rchi maktab va kasalxona zonasi", "lat": 38.0080, "lng": 67.7720, "type": "lochin", "speed": 50, "road": "Sho'rchi poliklinika yo'li", "dist": 450},

    # ==================== 6. SHEROBOD TUMANI (8 TA) ====================
    {"id": "uz-sur-she-001", "name": "Lochin 70 - M39 Sherobod xalqaro aylanma yo'li", "lat": 37.6720, "lng": 67.0120, "type": "lochin", "speed": 70, "road": "M39 Sherobod magistrali", "dist": 700},
    {"id": "uz-sur-she-002", "name": "Lochin 60 - Sherobod shahar Mustaqillik shoh ko'chasi", "lat": 37.6680, "lng": 67.0250, "type": "lochin", "speed": 60, "road": "Sherobod markazi", "dist": 500},
    {"id": "uz-sur-she-003", "name": "Chorraha 60 - Sherobod markaziy bozor chorrahasi", "lat": 37.6620, "lng": 67.0180, "type": "traffic_light", "speed": 60, "road": "Markaziy bozor chorrahasi", "dist": 450},
    {"id": "uz-sur-she-004", "name": "Lochin 70 - Sherobod Sement zavodi magistrali", "lat": 37.6350, "lng": 66.9850, "type": "lochin", "speed": 70, "road": "Sement zavod trassasi", "dist": 650},
    {"id": "uz-sur-she-005", "name": "Lochin 70 - M39 Boysun dovoni yo'nalishi posti", "lat": 37.7250, "lng": 67.0450, "type": "lochin", "speed": 70, "road": "M39 Boysun chiqish yo'li", "dist": 700},
    {"id": "uz-sur-she-006", "name": "Lochin 70 - M39 Angor / Termiz yo'nalishi chiqish posti", "lat": 37.6150, "lng": 67.0350, "type": "lochin", "speed": 70, "road": "M39 Angor yo'nalishi", "dist": 700},
    {"id": "uz-sur-she-007", "name": "Ko'chma Uch oyoq 70 - Qizilolma qishlog'i M39", "lat": 37.6950, "lng": 67.0280, "type": "uch_oyoq", "speed": 70, "road": "M39 Qizilolma pistirmasi", "dist": 650},
    {"id": "uz-sur-she-008", "name": "YPX Patrul 360 - Sherobod aylanma halqa yo'li", "lat": 37.6780, "lng": 67.0050, "type": "patrul_360", "speed": 60, "road": "Sherobod aylanmasi", "dist": 500},

    # ==================== 7. SARIOSIYO TUMANI (7 TA) ====================
    {"id": "uz-sur-sar-001", "name": "Lochin 60 - Sariosiyo markaziy shoh ko'chasi", "lat": 38.4120, "lng": 67.9450, "type": "lochin", "speed": 60, "road": "Sariosiyo markazi", "dist": 500},
    {"id": "uz-sur-sar-002", "name": "Lochin 70 - Sariosiyo - Tojikiston xalqaro bojxona posti", "lat": 38.4550, "lng": 68.0250, "type": "lochin", "speed": 70, "road": "Tursunzoda chegara trassasi", "dist": 700},
    {"id": "uz-sur-sar-003", "name": "Lochin 60 - Sharg'un shahar markaziy yo'li", "lat": 38.4750, "lng": 67.9750, "type": "lochin", "speed": 60, "road": "Sharg'un shahar magistrali", "dist": 500},
    {"id": "uz-sur-sar-004", "name": "Lochin 70 - Sharg'un ko'mir koni trassasi", "lat": 38.5050, "lng": 67.9550, "type": "lochin", "speed": 70, "road": "Sharg'un kon yo'li", "dist": 650},
    {"id": "uz-sur-sar-005", "name": "Chorraha 60 - Sariosiyo va Denov yo'li kesishmasi", "lat": 38.3850, "lng": 67.9350, "type": "traffic_light", "speed": 60, "road": "Denov yo'nalishi chorrahasi", "dist": 450},
    {"id": "uz-sur-sar-006", "name": "Ko'chma Uch oyoq 70 - Dashnobod qishlog'i yo'li", "lat": 38.4350, "lng": 67.9650, "type": "uch_oyoq", "speed": 70, "road": "Dashnobod pistirmasi", "dist": 650},
    {"id": "uz-sur-sar-007", "name": "Kamera orqadan oladi! (Rear 60) - Sariosiyo markazi", "lat": 38.4080, "lng": 67.9420, "type": "rear", "speed": 60, "road": "Sariosiyo markazi (Orqadan)", "dist": 500},

    # ==================== 8. UZUN TUMANI (7 TA) ====================
    {"id": "uz-sur-uzu-001", "name": "Lochin 70 - M41 Uzun tuman markaziy magistrali", "lat": 38.3550, "lng": 67.9250, "type": "lochin", "speed": 70, "road": "M41 Uzun tuman magistrali", "dist": 650},
    {"id": "uz-sur-uzu-002", "name": "Lochin 60 - Uzun shahar markaziy ko'chasi", "lat": 38.3620, "lng": 67.9350, "type": "lochin", "speed": 60, "road": "Uzun shahar markazi", "dist": 500},
    {"id": "uz-sur-uzu-003", "name": "Chorraha 60 - Uzun vokzal va bozor chorrahasi", "lat": 38.3580, "lng": 67.9420, "type": "traffic_light", "speed": 60, "road": "Vokzal maydoni chorrahasi", "dist": 450},
    {"id": "uz-sur-uzu-004", "name": "Lochin 70 - Bobotog' yo'nalishi trassasi", "lat": 38.3350, "lng": 67.9650, "type": "lochin", "speed": 70, "road": "Bobotog' tog' trassasi", "dist": 650},
    {"id": "uz-sur-uzu-005", "name": "Lochin 60 - Chinor qishlog'i yo'li", "lat": 38.3750, "lng": 67.9150, "type": "lochin", "speed": 60, "road": "Chinor aholi punkti", "dist": 500},
    {"id": "uz-sur-uzu-006", "name": "Ko'chma Uch oyoq 70 - Uzun - Denov trassasi", "lat": 38.3380, "lng": 67.9120, "type": "uch_oyoq", "speed": 70, "road": "Denov yo'nalishi (Pistirma)", "dist": 650},
    {"id": "uz-sur-uzu-007", "name": "YPX Patrul 360 - Uzun aylanma yo'li", "lat": 38.3680, "lng": 67.9520, "type": "patrul_360", "speed": 60, "road": "Uzun aylanma yo'li", "dist": 500},

    # ==================== 9. OLTINSOY TUMANI (7 TA) ====================
    {"id": "uz-sur-olt-001", "name": "Lochin 60 - Oltinsoy (Qarluq) markaziy ko'chasi", "lat": 38.1850, "lng": 67.6850, "type": "lochin", "speed": 60, "road": "Oltinsoy markazi", "dist": 500},
    {"id": "uz-sur-olt-002", "name": "Chorraha 60 - Qarluq markaziy maydoni", "lat": 38.1890, "lng": 67.6920, "type": "traffic_light", "speed": 60, "road": "Qarluq maydoni chorrahasi", "dist": 450},
    {"id": "uz-sur-olt-003", "name": "Lochin 70 - Oltinsoy - Sho'rchi tumanlararo yo'li", "lat": 38.1450, "lng": 67.7250, "type": "lochin", "speed": 70, "road": "Sho'rchi yo'nalishi", "dist": 650},
    {"id": "uz-sur-olt-004", "name": "Lochin 70 - Oltinsoy - Denov tog'oldi trassasi", "lat": 38.2250, "lng": 67.7450, "type": "lochin", "speed": 70, "road": "Denov tog'oldi yo'li", "dist": 650},
    {"id": "uz-sur-olt-005", "name": "Lochin 60 - Xo'jasoat ziyoratgohi yo'li", "lat": 38.2050, "lng": 67.6550, "type": "lochin", "speed": 60, "road": "Xo'jasoat ziyorat yo'li", "dist": 500},
    {"id": "uz-sur-olt-006", "name": "Ko'chma Uch oyoq 70 - Katta Vaxshivor yo'nalishi", "lat": 38.1650, "lng": 67.6650, "type": "uch_oyoq", "speed": 70, "road": "Vaxshivor pistirmasi", "dist": 650},
    {"id": "uz-sur-olt-007", "name": "Kamera orqadan oladi! (Rear 60) - Qarluq markazi", "lat": 38.1820, "lng": 67.6810, "type": "rear", "speed": 60, "road": "Qarluq markazi (Orqadan)", "dist": 500},

    # ==================== 10. ANGOR TUMANI (7 TA) ====================
    {"id": "uz-sur-ang-001", "name": "Lochin 70 - M39 Angor markaziy xalqaro trassasi", "lat": 37.4720, "lng": 67.1450, "type": "lochin", "speed": 70, "road": "M39 Angor yo'nalishi", "dist": 650},
    {"id": "uz-sur-ang-002", "name": "Lochin 60 - Angor shahar markaziy shoh ko'chasi", "lat": 37.4650, "lng": 67.1550, "type": "lochin", "speed": 60, "road": "Angor shahar markazi", "dist": 500},
    {"id": "uz-sur-ang-003", "name": "Chorraha 60 - Angor va Qiziriq yo'li chorrahasi", "lat": 37.4780, "lng": 67.1480, "type": "traffic_light", "speed": 60, "road": "Qiziriq ayri yo'li", "dist": 450},
    {"id": "uz-sur-ang-004", "name": "Lochin 70 - M39 Sherobod chegarasi posti", "lat": 37.5250, "lng": 67.1150, "type": "lochin", "speed": 70, "road": "M39 Sherobod posti", "dist": 700},
    {"id": "uz-sur-ang-005", "name": "Lochin 70 - M39 Termiz yo'nalishi chiqish trassasi", "lat": 37.4150, "lng": 67.1750, "type": "lochin", "speed": 70, "road": "M39 Termiz chiqish yo'li", "dist": 700},
    {"id": "uz-sur-ang-006", "name": "Ko'chma Uch oyoq 70 - Gilambob qishlog'i M39", "lat": 37.4950, "lng": 67.1350, "type": "uch_oyoq", "speed": 70, "road": "M39 Gilambob pistirmasi", "dist": 650},
    {"id": "uz-sur-ang-007", "name": "YPX Patrul 360 - Angor aylanma halqa yo'li", "lat": 37.4580, "lng": 67.1620, "type": "patrul_360", "speed": 60, "road": "Angor aylanmasi", "dist": 500},

    # ==================== 11. MUZRABOT TUMANI (7 TA) ====================
    {"id": "uz-sur-muz-001", "name": "Lochin 70 - Muzrabot (Xalqobod) markaziy magistrali", "lat": 37.3550, "lng": 66.8850, "type": "lochin", "speed": 70, "road": "Xalqobod markazi", "dist": 650},
    {"id": "uz-sur-muz-002", "name": "Lochin 60 - Xalqobod shahar markaziy ko'chasi", "lat": 37.3620, "lng": 66.8920, "type": "lochin", "speed": 60, "road": "Tuman markazi", "dist": 500},
    {"id": "uz-sur-muz-003", "name": "Chorraha 60 - Xalqobod markaziy chorrahasi", "lat": 37.3580, "lng": 66.8810, "type": "traffic_light", "speed": 60, "road": "Markaziy chorraha", "dist": 450},
    {"id": "uz-sur-muz-004", "name": "Lochin 70 - Muzrabot - Sherobod tumanlararo yo'li", "lat": 37.4250, "lng": 66.9250, "type": "lochin", "speed": 70, "road": "Sherobod yo'nalishi", "dist": 650},
    {"id": "uz-sur-muz-005", "name": "Lochin 70 - Muzrabot - Termiz yo'nalishi trassasi", "lat": 37.3150, "lng": 66.9850, "type": "lochin", "speed": 70, "road": "Termiz yo'nalishi", "dist": 650},
    {"id": "uz-sur-muz-006", "name": "Ko'chma Uch oyoq 70 - Bo'ston qishlog'i yo'li", "lat": 37.3850, "lng": 66.8650, "type": "uch_oyoq", "speed": 70, "road": "Bo'ston pistirmasi", "dist": 650},
    {"id": "uz-sur-muz-007", "name": "Kamera orqadan oladi! (Rear 60) - Xalqobod markazi", "lat": 37.3520, "lng": 66.8890, "type": "rear", "speed": 60, "road": "Xalqobod markazi (Orqadan)", "dist": 500},

    # ==================== 12. QIZIRIQ TUMANI (7 TA) ====================
    {"id": "uz-sur-qiz-001", "name": "Lochin 60 - 4R100 Qiziriq (Sariq) shahar markazi", "lat": 37.6580, "lng": 67.2850, "type": "lochin", "speed": 60, "road": "4R100 Qiziriq markazi", "dist": 500},
    {"id": "uz-sur-qiz-002", "name": "Chorraha 60 - Sariq markaziy maydoni va bozor yo'li", "lat": 37.6620, "lng": 67.2920, "type": "traffic_light", "speed": 60, "road": "Sariq dehqon bozori chorrahasi", "dist": 450},
    {"id": "uz-sur-qiz-003", "name": "Lochin 70 - 4R100 Bandixon yo'nalishi kirish posti", "lat": 37.7150, "lng": 67.3150, "type": "lochin", "speed": 70, "road": "4R100 Bandixon yo'li posti", "dist": 650},
    {"id": "uz-sur-qiz-004", "name": "Lochin 70 - 4R100 Angor yo'nalishi chiqish posti", "lat": 37.5950, "lng": 67.2450, "type": "lochin", "speed": 70, "road": "4R100 Angor yo'li posti", "dist": 650},
    {"id": "uz-sur-qiz-005", "name": "Lochin 60 - Yangihayot qishlog'i yo'li", "lat": 37.6350, "lng": 67.2650, "type": "lochin", "speed": 60, "road": "Yangihayot aholi punkti", "dist": 500},
    {"id": "uz-sur-qiz-006", "name": "Ko'chma Uch oyoq 70 - Qiziriq dala trassasi", "lat": 37.6850, "lng": 67.3050, "type": "uch_oyoq", "speed": 70, "road": "Qiziriq pistirmasi", "dist": 650},
    {"id": "uz-sur-qiz-007", "name": "YPX Patrul 360 - Sariq aylanma yo'li", "lat": 37.6520, "lng": 67.2780, "type": "patrul_360", "speed": 60, "road": "Sariq aylanma halqa yo'li", "dist": 500},

    # ==================== 13. BANDIXON TUMANI (Qo'shimcha 5 ta, Jami 11 TA) ====================
    {"id": "uz-sur-ban-007", "name": "Lochin 50 - Bandixon poliklinika va 1-maktab oldi", "lat": 37.8640, "lng": 67.3820, "type": "lochin", "speed": 50, "road": "Bandixon maktab/shifoxona zonasi", "dist": 450},
    {"id": "uz-sur-ban-008", "name": "Lochin 60 - Bandixon Dehqon bozori chorrahasi", "lat": 37.8590, "lng": 67.3920, "type": "lochin", "speed": 60, "road": "Bandixon bozori yo'li", "dist": 450},
    {"id": "uz-sur-ban-009", "name": "Ko'chma Uch oyoq 70 - Bandixon - Qumqo'rg'on ichki yo'li", "lat": 37.8450, "lng": 67.4350, "type": "uch_oyoq", "speed": 70, "road": "Qumqo'rg'on ichki trassasi (Pistirma)", "dist": 650},
    {"id": "uz-sur-ban-010", "name": "Lochin 70 - Bandixon - Boysun chegarasi tog' etagi", "lat": 37.9150, "lng": 67.3550, "type": "lochin", "speed": 70, "road": "Boysun tog'oldi magistrali", "dist": 650},
    {"id": "uz-sur-ban-011", "name": "Lochin 60 - Bandixon tuman hokimiyati shoh ko'chasi", "lat": 37.8615, "lng": 67.3860, "type": "lochin", "speed": 60, "road": "Bandixon tuman hokimiyati oldi", "dist": 500}
]

added = 0
for item in detailed_sur_cams:
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

print(f"Yangi qo'shilgan batafsil Surxondaryo kameralari: {added}")
print(f"JAMI BAZADAGI RADARLAR SONI: {len(cams)}")
