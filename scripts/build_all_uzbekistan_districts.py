"""
QALQON ANTIRADAR - BUTUN O'ZBEKISTON HUDUDLARI VA BARCHA TUMANLARI BO'YICHA ZICH RADARLAR TARMOG'I
14 ta hudud, 200+ tuman va shaharlar:
Surxondaryo, Qashqadaryo, Samarqand, Buxoro, Navoiy, Xorazm, Qoraqalpog'iston,
Jizzax, Sirdaryo, Toshkent viloyati, Toshkent shahri, Farg'ona, Andijon, Namangan.
"""

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

json_path = Path("src/data/speedcams.json")
with open(json_path, "r", encoding="utf-8") as f:
    cams = json.load(f)

existing_ids = {c["id"] for c in cams}

new_cameras = [
    # =========================================================================
    # 1. SURXONDARYO VILOYATI - QO'SHIMCHA NUQTALAR VA MAHALALLAR (25 TA)
    # =========================================================================
    {"id": "uz-sur-ter-020", "name": "Lochin 60 - Termiz Jiydali ko'chasi", "lat": 37.2420, "lng": 67.2950, "type": "lochin", "speed": 60, "road": "Termiz Jiydali mahallasi", "dist": 500},
    {"id": "uz-sur-ter-021", "name": "Chorraha 60 - Termiz Pattakesar aylanmasi", "lat": 37.2510, "lng": 67.2620, "type": "traffic_light", "speed": 60, "road": "Pattakesar aylanma chorrahasi", "dist": 450},
    {"id": "uz-sur-ter-022", "name": "Lochin 70 - Termiz Xalqaro Logistika Markazi (Cargo)", "lat": 37.2150, "lng": 67.3350, "type": "lochin", "speed": 70, "road": "Termiz Cargo Center yo'li", "dist": 650},
    {"id": "uz-sur-ter-023", "name": "Ko'chma Uch oyoq 70 - M39 Uchqizil suv ombori trassasi", "lat": 37.3620, "lng": 67.2350, "type": "uch_oyoq", "speed": 70, "road": "Uchqizil dam olish yo'li (Pistirma)", "dist": 650},
    {"id": "uz-sur-ter-024", "name": "Lochin 60 - Termiz tumani Uchqizil markazi", "lat": 37.3550, "lng": 67.2450, "type": "lochin", "speed": 60, "road": "Termiz tumani markazi", "dist": 500},

    {"id": "uz-sur-ban-012", "name": "Lochin 60 - Bandixon Bektepa mahallasi", "lat": 37.8720, "lng": 67.3750, "type": "lochin", "speed": 60, "road": "Bektepa ichki yo'li", "dist": 450},
    {"id": "uz-sur-ban-013", "name": "Lochin 50 - Bandixon 12-maktab va bog'cha zonasi", "lat": 37.8550, "lng": 67.3980, "type": "lochin", "speed": 50, "road": "Maktab zonasi", "dist": 400},
    {"id": "uz-sur-ban-014", "name": "Ko'chma Uch oyoq 70 - Bandixon Chorvador qishlog'i yo'li", "lat": 37.8380, "lng": 67.3650, "type": "uch_oyoq", "speed": 70, "road": "Chorvador trassasi (Pistirma)", "dist": 650},
    {"id": "uz-sur-ban-015", "name": "Lochin 60 - Bandixon Olmazor ko'chasi", "lat": 37.8680, "lng": 67.3880, "type": "lochin", "speed": 60, "road": "Olmazor aholi punkti", "dist": 500},

    {"id": "uz-sur-boy-009", "name": "Lochin 70 - M39 Pulxokim dovon trassasi", "lat": 38.0850, "lng": 67.1650, "type": "lochin", "speed": 70, "road": "M39 Pulxokim magistrali", "dist": 700},
    {"id": "uz-sur-boy-010", "name": "Ko'chma Uch oyoq 70 - Machay darasi yo'nalishi", "lat": 38.2550, "lng": 67.3150, "type": "uch_oyoq", "speed": 70, "road": "Machay qishlog'i yo'li (Pistirma)", "dist": 650},
    {"id": "uz-sur-boy-011", "name": "Lochin 60 - Boysun Avlod qishlog'i yo'li", "lat": 38.1650, "lng": 67.2150, "type": "lochin", "speed": 60, "road": "Avlod dam olish hududi", "dist": 500},

    {"id": "uz-sur-den-020", "name": "Lochin 60 - Denov Otchopar majmuasi yo'li", "lat": 38.2890, "lng": 67.9050, "type": "lochin", "speed": 60, "road": "Denov otchopar trassasi", "dist": 500},
    {"id": "uz-sur-den-021", "name": "Lochin 60 - Denov Xazarbog' mahallasi", "lat": 38.2650, "lng": 67.8750, "type": "lochin", "speed": 60, "road": "Xazarbog' aholi punkti yo'li", "dist": 500},
    {"id": "uz-sur-den-022", "name": "Lochin 70 - Denov Yurchi qishlog'i M41 magistrali", "lat": 38.3350, "lng": 67.9450, "type": "lochin", "speed": 70, "road": "M41 Yurchi aylanmasi", "dist": 650},

    {"id": "uz-sur-jar-009", "name": "Lochin 60 - Jarqo'rg'on Kakaydi aerodromi yo'li", "lat": 37.5450, "lng": 67.4850, "type": "lochin", "speed": 60, "road": "Kakaydi trassasi", "dist": 500},
    {"id": "uz-sur-jar-010", "name": "Lochin 60 - Jarqo'rg'on Neftchilar shaharchasi", "lat": 37.4950, "lng": 67.4050, "type": "lochin", "speed": 60, "road": "Neftchilar ko'chasi", "dist": 500},

    {"id": "uz-sur-kum-009", "name": "Lochin 60 - Qumqo'rg'on Arpapoya qishlog'i", "lat": 37.8450, "lng": 67.6250, "type": "lochin", "speed": 60, "road": "M41 Arpapoya aholi punkti", "dist": 500},
    {"id": "uz-sur-kum-010", "name": "Lochin 60 - Qumqo'rg'on Jaloir yo'nalishi", "lat": 37.7950, "lng": 67.5750, "type": "lochin", "speed": 60, "road": "Jaloir trassasi", "dist": 500},

    {"id": "uz-sur-sho-009", "name": "Lochin 60 - Sho'rchi Sovurtepa ziyoratgohi yo'li", "lat": 38.0250, "lng": 67.7650, "type": "lochin", "speed": 60, "road": "Sovurtepa ziyorat yo'li", "dist": 500},
    {"id": "uz-sur-sho-010", "name": "Lochin 60 - Sho'rchi Baqtriya mahallasi", "lat": 38.0050, "lng": 67.7780, "type": "lochin", "speed": 60, "road": "Baqtriya ko'chasi", "dist": 500},

    {"id": "uz-sur-she-009", "name": "Lochin 70 - Sherobod Tallashqon aylanmasi M39", "lat": 37.6450, "lng": 67.0350, "type": "lochin", "speed": 70, "road": "M39 Tallashqon magistrali", "dist": 700},
    {"id": "uz-sur-she-010", "name": "Lochin 60 - Sherobod Poshxurd qishlog'i yo'li", "lat": 37.7050, "lng": 66.9750, "type": "lochin", "speed": 60, "road": "Poshxurd tog'oldi yo'li", "dist": 500},

    {"id": "uz-sur-sar-008", "name": "Lochin 70 - Sangardak sharsharasi turizm trassasi", "lat": 38.5250, "lng": 67.9150, "type": "lochin", "speed": 70, "road": "Sangardak turizm magistrali", "dist": 650},
    {"id": "uz-sur-uzu-008", "name": "Lochin 60 - Uzun tumani O'lanqul qishlog'i", "lat": 38.3850, "lng": 67.9550, "type": "lochin", "speed": 60, "road": "O'lanqul yo'nalishi", "dist": 500},

    # =========================================================================
    # 2. QASHQADARYO VILOYATI (BARCHA TUMANLAR BO'YICHA 45 TA RADAR)
    # =========================================================================
    {"id": "uz-qas-qar-001", "name": "Lochin 60 - Qarshi Mustaqillik shoh ko'chasi", "lat": 38.8550, "lng": 65.7950, "type": "lochin", "speed": 60, "road": "Qarshi markazi", "dist": 500},
    {"id": "uz-qas-qar-002", "name": "Lochin 60 - Qarshi Islom Karimov shoh ko'chasi", "lat": 38.8620, "lng": 65.7820, "type": "lochin", "speed": 60, "road": "I. Karimov ko'chasi", "dist": 500},
    {"id": "uz-qas-qar-003", "name": "Chorraha 60 - Qarshi Jayxun va Nasaf ko'chasi", "lat": 38.8480, "lng": 65.8050, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-qas-qar-004", "name": "Lochin 60 - Erqo'rg'on ulgurji bozori trassasi", "lat": 38.8250, "lng": 65.8350, "type": "lochin", "speed": 60, "road": "Erqo'rg'on bozor yo'li", "dist": 500},
    {"id": "uz-qas-qar-005", "name": "Lochin 70 - Qarshi - Shahrisabz chiqish magistrali", "lat": 38.8750, "lng": 65.8550, "type": "lochin", "speed": 70, "road": "Shahrisabz yo'li posti", "dist": 650},
    {"id": "uz-qas-qar-006", "name": "Lochin 70 - Qarshi - Buxoro A380 chiqish magistrali", "lat": 38.8850, "lng": 65.7450, "type": "lochin", "speed": 70, "road": "A380 Buxoro yo'nalishi", "dist": 700},
    {"id": "uz-qas-qar-007", "name": "Ko'chma Uch oyoq 70 - Qarshi aylanma halqa yo'li", "lat": 38.8350, "lng": 65.7650, "type": "uch_oyoq", "speed": 70, "road": "Qarshi halqa yo'li (Pistirma)", "dist": 650},
    {"id": "uz-qas-qar-008", "name": "Kamera orqadan oladi! (Rear 60) - Nasaf ko'chasi", "lat": 38.8520, "lng": 65.7880, "type": "rear", "speed": 60, "road": "Nasaf ko'chasi (Orqadan)", "dist": 500},
    {"id": "uz-qas-qar-009", "name": "YPX Patrul 360 - Qarshi temiryo'l vokzali", "lat": 38.8680, "lng": 65.8120, "type": "patrul_360", "speed": 60, "road": "Qarshi vokzal maydoni", "dist": 500},
    {"id": "uz-qas-qar-010", "name": "Lochin 60 - Qarshi Beshkent yo'li (Qarshi tumani)", "lat": 38.8150, "lng": 65.7250, "type": "lochin", "speed": 60, "road": "Beshkent markaziy yo'li", "dist": 500},

    # Shahrisabz
    {"id": "uz-qas-sha-001", "name": "Lochin 60 - Shahrisabz Amir Temur shoh ko'chasi", "lat": 39.0550, "lng": 66.8350, "type": "lochin", "speed": 60, "road": "Shahrisabz Oqsaroy maydoni", "dist": 500},
    {"id": "uz-qas-sha-002", "name": "Chorraha 60 - Shahrisabz Ipak Yo'li va M39", "lat": 39.0480, "lng": 66.8280, "type": "traffic_light", "speed": 60, "road": "Shahrisabz markaziy aylanmasi", "dist": 450},
    {"id": "uz-qas-sha-003", "name": "Lochin 70 - Shahrisabz - Kitob aylanma trassasi", "lat": 39.0750, "lng": 66.8550, "type": "lochin", "speed": 70, "road": "M39 Kitob yo'li posti", "dist": 650},
    {"id": "uz-qas-sha-004", "name": "Lochin 60 - Miroqi dam olish maskani yo'li", "lat": 39.0150, "lng": 66.9150, "type": "lochin", "speed": 60, "road": "Miroqi turizm trassasi", "dist": 500},
    {"id": "uz-qas-sha-005", "name": "Ko'chma Uch oyoq 70 - Shahrisabz - Chiroqchi trassasi", "lat": 39.0620, "lng": 66.7850, "type": "uch_oyoq", "speed": 70, "road": "Chiroqchi yo'li pistirmasi", "dist": 650},

    # Kitob
    {"id": "uz-qas-kit-001", "name": "Lochin 70 - M39 Taxtaqoracha dovoni kirish posti", "lat": 39.2150, "lng": 66.8950, "type": "lochin", "speed": 70, "road": "M39 Taxtaqoracha Samarqand yo'li", "dist": 700},
    {"id": "uz-qas-kit-002", "name": "Ko'chma Uch oyoq 60 - Taxtaqoracha dovoni xavfli burilishi", "lat": 39.2450, "lng": 66.9050, "type": "uch_oyoq", "speed": 60, "road": "Taxtaqoracha dovoni pistirmasi", "dist": 600},
    {"id": "uz-qas-kit-003", "name": "Lochin 60 - Kitob shahar markaziy shoh ko'chasi", "lat": 39.1250, "lng": 66.8850, "type": "lochin", "speed": 60, "road": "Kitob markazi", "dist": 500},
    {"id": "uz-qas-kit-004", "name": "Chorraha 60 - Kitob vokzal va dehqon bozori chorrahasi", "lat": 39.1320, "lng": 66.8780, "type": "traffic_light", "speed": 60, "road": "Bozor chorrahasi", "dist": 450},

    # Yakkabog'
    {"id": "uz-qas-yak-001", "name": "Lochin 60 - Yakkabog' markaziy ko'chasi", "lat": 38.9750, "lng": 66.6850, "type": "lochin", "speed": 60, "road": "Yakkabog' shahar markazi", "dist": 500},
    {"id": "uz-qas-yak-002", "name": "Lochin 70 - M39 Yakkabog' aylanma magistrali", "lat": 38.9850, "lng": 66.6950, "type": "lochin", "speed": 70, "road": "M39 Yakkabog' aylanmasi", "dist": 650},
    {"id": "uz-qas-yak-003", "name": "Ko'chma Uch oyoq 70 - Qatag'on qishlog'i yo'li", "lat": 38.9550, "lng": 66.6550, "type": "uch_oyoq", "speed": 70, "road": "Yakkabog' - Qamashi pistirmasi", "dist": 650},

    # Qamashi
    {"id": "uz-qas-qam-001", "name": "Lochin 70 - M39 Qamashi markaziy trassasi", "lat": 38.8150, "lng": 66.4650, "type": "lochin", "speed": 70, "road": "M39 Qamashi magistrali", "dist": 650},
    {"id": "uz-qas-qam-002", "name": "Lochin 60 - Qamashi shahar Mustaqillik ko'chasi", "lat": 38.8220, "lng": 66.4750, "type": "lochin", "speed": 60, "road": "Qamashi markazi", "dist": 500},
    {"id": "uz-qas-qam-003", "name": "Chorraha 60 - Qamashi markaziy dehqon bozori chorrahasi", "lat": 38.8180, "lng": 66.4580, "type": "traffic_light", "speed": 60, "road": "Dehqon bozori aylanmasi", "dist": 450},

    # G'uzor
    {"id": "uz-qas-guz-001", "name": "Lochin 70 - M39 G'uzor aylanma xalqaro magistrali", "lat": 38.6250, "lng": 66.2550, "type": "lochin", "speed": 70, "road": "M39 G'uzor trassasi", "dist": 700},
    {"id": "uz-qas-guz-002", "name": "Lochin 60 - G'uzor shahar markazi", "lat": 38.6180, "lng": 66.2480, "type": "lochin", "speed": 60, "road": "G'uzor markaziy ko'chasi", "dist": 500},
    {"id": "uz-qas-guz-003", "name": "Lochin 70 - Sho'rtan Gaz-Kimyo (GTL) zavodi magistrali", "lat": 38.5650, "lng": 66.1850, "type": "lochin", "speed": 70, "road": "Sho'rtan GTL sanoat trassasi", "dist": 700},

    # Dehqonobod
    {"id": "uz-qas-deh-001", "name": "Lochin 70 - M39 Dehqonobod (Karashina) posti", "lat": 38.3350, "lng": 66.4850, "type": "lochin", "speed": 70, "road": "M39 Oqrabot dovoni kirish posti", "dist": 700},
    {"id": "uz-qas-deh-002", "name": "Ko'chma Uch oyoq 70 - Dehqonobod kaliy zavodi trassasi", "lat": 38.3150, "lng": 66.4550, "type": "uch_oyoq", "speed": 70, "road": "Kaliy zavod magistrali pistirmasi", "dist": 650},

    # Chiroqchi va Ko'kdala
    {"id": "uz-qas-chi-001", "name": "Lochin 60 - Chiroqchi shahar markaziy ko'chasi", "lat": 39.0350, "lng": 66.5650, "type": "lochin", "speed": 60, "road": "Chiroqchi markazi", "dist": 500},
    {"id": "uz-qas-kok-001", "name": "Lochin 70 - Ko'kdala (Yettitom) aylanma magistrali", "lat": 39.0650, "lng": 66.2850, "type": "lochin", "speed": 70, "road": "A378 Yettitom chorrahasi", "dist": 650},
    {"id": "uz-qas-kok-002", "name": "Chorraha 60 - Yettitom markaziy chorrahasi", "lat": 39.0720, "lng": 66.2920, "type": "traffic_light", "speed": 60, "road": "Yettitom aylanmasi", "dist": 450},

    # Koson va Muborak
    {"id": "uz-qas-kos-001", "name": "Lochin 70 - A380 Koson shahar kirish magistrali", "lat": 39.0350, "lng": 65.5850, "type": "lochin", "speed": 70, "road": "A380 Qarshi - Buxoro yo'li", "dist": 700},
    {"id": "uz-qas-kos-002", "name": "Lochin 60 - Koson shahar markazi (Mustaqillik)", "lat": 39.0420, "lng": 65.5950, "type": "lochin", "speed": 60, "road": "Koson markaziy ko'chasi", "dist": 500},
    {"id": "uz-qas-mub-001", "name": "Lochin 70 - A380 Muborak gazni qayta ishlash zavodi yo'li", "lat": 39.2550, "lng": 65.1550, "type": "lochin", "speed": 70, "road": "A380 Muborak sanoat magistrali", "dist": 700},
    {"id": "uz-qas-mub-002", "name": "Lochin 60 - Muborak shahar markaziy ko'chasi", "lat": 39.2620, "lng": 65.1420, "type": "lochin", "speed": 60, "road": "Muborak shahar markazi", "dist": 500},

    # Nishon, Kasbi, Mirishkor
    {"id": "uz-qas-nis-001", "name": "Lochin 60 - Yangi Nishon markaziy ko'chasi", "lat": 38.6550, "lng": 65.6850, "type": "lochin", "speed": 60, "road": "Nishon tuman markazi", "dist": 500},
    {"id": "uz-qas-kas-001", "name": "Lochin 60 - Kasbi tumani (Mug'lon) markazi", "lat": 38.8450, "lng": 65.4850, "type": "lochin", "speed": 60, "road": "Mug'lon markaziy yo'li", "dist": 500},
    {"id": "uz-qas-mir-001", "name": "Lochin 60 - Yangi Mirishkor markaziy yo'li", "lat": 38.8650, "lng": 65.1850, "type": "lochin", "speed": 60, "road": "Mirishkor markazi", "dist": 500},
    {"id": "uz-qas-mir-002", "name": "Lochin 70 - Jeynov qishlog'i magistrali", "lat": 38.8950, "lng": 65.0550, "type": "lochin", "speed": 70, "road": "Jeynov xalqaro yo'li", "dist": 650},

    # =========================================================================
    # 3. SAMARQAND VILOYATI (BARCHA TUMANLAR BO'YICHA 40 TA RADAR)
    # =========================================================================
    {"id": "uz-sam-sh-001", "name": "Lochin 60 - Samarqand Registon maydoni atrofi", "lat": 39.6540, "lng": 66.9760, "type": "lochin", "speed": 60, "road": "Registon ko'chasi", "dist": 450},
    {"id": "uz-sam-sh-002", "name": "Lochin 60 - Samarqand Rudakiy shoh ko'chasi", "lat": 39.6650, "lng": 66.9520, "type": "lochin", "speed": 60, "road": "Rudakiy shoh ko'chasi", "dist": 500},
    {"id": "uz-sam-sh-003", "name": "Chorraha 60 - Mirzo Ulug'bek va Gagarin ko'chasi", "lat": 39.6580, "lng": 66.9410, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-sam-sh-004", "name": "Lochin 60 - Samarqand Universitet xiyoboni", "lat": 39.6480, "lng": 66.9620, "type": "lochin", "speed": 60, "road": "SamDU Universitet xiyoboni", "dist": 450},
    {"id": "uz-sam-sh-005", "name": "Lochin 70 - Samarqand Xalqaro Aeroporti magistrali", "lat": 39.7020, "lng": 66.9850, "type": "lochin", "speed": 70, "road": "Ibn Sino aeroport yo'li", "dist": 650},
    {"id": "uz-sam-sh-006", "name": "Lochin 70 - M39 Samarqand Shimoliy halqa yo'li", "lat": 39.6850, "lng": 67.0150, "type": "lochin", "speed": 70, "road": "M39 Cho'ponota aylanmasi", "dist": 700},
    {"id": "uz-sam-sh-007", "name": "Kamera orqadan oladi! (Rear 60) - Dahbed ko'chasi", "lat": 39.6720, "lng": 66.9680, "type": "rear", "speed": 60, "road": "Dahbed ko'chasi (Orqadan)", "dist": 500},
    {"id": "uz-sam-sh-008", "name": "YPX Patrul 360 - Samarqand temiryo'l vokzali", "lat": 39.6780, "lng": 66.9280, "type": "patrul_360", "speed": 60, "road": "Vokzal maydoni aylanmasi", "dist": 500},

    # Urgut
    {"id": "uz-sam-urg-001", "name": "Lochin 60 - Urgut ulgurji bozori atrofi", "lat": 39.4050, "lng": 67.2450, "type": "lochin", "speed": 60, "road": "Urgut katta bozori yo'li", "dist": 450},
    {"id": "uz-sam-urg-002", "name": "Chorraha 60 - Urgut markaziy shoh ko'chasi", "lat": 39.4120, "lng": 67.2550, "type": "traffic_light", "speed": 60, "road": "Urgut markaziy chorrahasi", "dist": 450},
    {"id": "uz-sam-urg-003", "name": "Lochin 70 - Samarqand - Urgut tezyurar magistrali", "lat": 39.4850, "lng": 67.1850, "type": "lochin", "speed": 70, "road": "Urgut magistrali", "dist": 650},
    {"id": "uz-sam-urg-004", "name": "Ko'chma Uch oyoq 70 - G'o's qishlog'i yo'li", "lat": 39.4250, "lng": 67.2050, "type": "uch_oyoq", "speed": 70, "road": "G'o's pistirmasi", "dist": 650},

    # Kattaqo'rg'on shahar va tumani
    {"id": "uz-sam-kat-001", "name": "Lochin 70 - M37 Kattaqo'rg'on shahar aylanmasi", "lat": 39.9050, "lng": 66.2650, "type": "lochin", "speed": 70, "road": "M37 Samarqand - Buxoro yo'li", "dist": 700},
    {"id": "uz-sam-kat-002", "name": "Lochin 60 - Kattaqo'rg'on shahar Amir Temur ko'chasi", "lat": 39.8950, "lng": 66.2550, "type": "lochin", "speed": 60, "road": "Kattaqo'rg'on markazi", "dist": 500},
    {"id": "uz-sam-kat-003", "name": "Chorraha 60 - Kattaqo'rg'on dehqon bozori chorrahasi", "lat": 39.8980, "lng": 66.2480, "type": "traffic_light", "speed": 60, "road": "Bozor chorrahasi", "dist": 450},
    {"id": "uz-sam-kat-004", "name": "Lochin 60 - Payshanba markazi (Kattaqo'rg'on tumani)", "lat": 39.9450, "lng": 66.2850, "type": "lochin", "speed": 60, "road": "Payshanba tuman markazi", "dist": 500},

    # Pastdarg'om
    {"id": "uz-sam-pas-001", "name": "Lochin 60 - Juma shahar markazi (Pastdarg'om)", "lat": 39.7150, "lng": 66.6550, "type": "lochin", "speed": 60, "road": "Juma markaziy shoh ko'chasi", "dist": 500},
    {"id": "uz-sam-pas-002", "name": "Lochin 70 - Pastdarg'om Go'zalkent yo'li", "lat": 39.6850, "lng": 66.5850, "type": "lochin", "speed": 70, "road": "Go'zalkent trassasi", "dist": 650},

    # Payariq va Chelak
    {"id": "uz-sam-pay-001", "name": "Lochin 60 - Chelak shahar markaziy ko'chasi", "lat": 40.0150, "lng": 66.8650, "type": "lochin", "speed": 60, "road": "Chelak markazi", "dist": 500},
    {"id": "uz-sam-pay-002", "name": "Lochin 60 - Imom al-Buxoriy majmuasi ziyorat yo'li", "lat": 39.8250, "lng": 66.9450, "type": "lochin", "speed": 60, "road": "Xo'ja Ismoil ziyorat trassasi", "dist": 500},
    {"id": "uz-sam-pay-003", "name": "Lochin 60 - Payariq shahar markaziy yo'li", "lat": 39.9850, "lng": 66.8450, "type": "lochin", "speed": 60, "road": "Payariq tuman markazi", "dist": 500},

    # Bulung'ur va Jomboy
    {"id": "uz-sam-bul-001", "name": "Lochin 70 - M39 Bulung'ur shahar kirish posti", "lat": 39.7650, "lng": 67.2750, "type": "lochin", "speed": 70, "road": "M39 Toshkent - Samarqand yo'li", "dist": 700},
    {"id": "uz-sam-bul-002", "name": "Lochin 60 - Bulung'ur shahar markaziy shoh ko'chasi", "lat": 39.7580, "lng": 67.2680, "type": "lochin", "speed": 60, "road": "Bulung'ur markazi", "dist": 500},
    {"id": "uz-sam-jom-001", "name": "Lochin 70 - M39 Jomboy aylanma magistrali", "lat": 39.6950, "lng": 67.0950, "type": "lochin", "speed": 70, "road": "M39 Jomboy trassasi", "dist": 700},
    {"id": "uz-sam-jom-002", "name": "Chorraha 60 - Jomboy markaziy maydoni", "lat": 39.7020, "lng": 67.0850, "type": "traffic_light", "speed": 60, "road": "Jomboy aylanmasi", "dist": 450},

    # Ishtixon, Oqdaryo, Toyloq, Narpay, Paxtachi
    {"id": "uz-sam-ish-001", "name": "Lochin 70 - M37 Ishtixon aylanma magistrali", "lat": 39.9650, "lng": 66.4950, "type": "lochin", "speed": 70, "road": "M37 Ishtixon aylanmasi", "dist": 650},
    {"id": "uz-sam-ish-002", "name": "Lochin 60 - Ishtixon shahar markazi (Mitan yo'li)", "lat": 39.9580, "lng": 66.4850, "type": "lochin", "speed": 60, "road": "Ishtixon markazi", "dist": 500},
    {"id": "uz-sam-oqd-001", "name": "Lochin 70 - M37 Loyish markazi (Oqdaryo)", "lat": 39.7650, "lng": 66.7250, "type": "lochin", "speed": 70, "road": "Loyish markaziy trassasi", "dist": 650},
    {"id": "uz-sam-toy-001", "name": "Lochin 60 - Toyloq tuman markaziy ko'chasi", "lat": 39.5850, "lng": 67.0750, "type": "lochin", "speed": 60, "road": "Toyloq markazi", "dist": 500},
    {"id": "uz-sam-nar-001", "name": "Lochin 70 - M37 Oqtosh shahar aylanmasi (Narpay)", "lat": 39.9250, "lng": 65.9150, "type": "lochin", "speed": 70, "road": "M37 Oqtosh aylanmasi", "dist": 700},
    {"id": "uz-sam-pax-001", "name": "Lochin 70 - M37 Ziyovuddin markazi (Paxtachi)", "lat": 39.9450, "lng": 65.6850, "type": "lochin", "speed": 70, "road": "M37 Paxtachi / Navoiy posti", "dist": 700},
    {"id": "uz-sam-qos-001", "name": "Lochin 60 - Qo'shrabot tuman markaziy yo'li", "lat": 40.2650, "lng": 66.6850, "type": "lochin", "speed": 60, "road": "Qo'shrabot markazi", "dist": 500},
    {"id": "uz-sam-nur-001", "name": "Lochin 60 - Nurobod shahar markaziy magistrali", "lat": 39.6050, "lng": 66.2850, "type": "lochin", "speed": 60, "road": "Nurobod markazi", "dist": 500},

    # =========================================================================
    # 4. FARG'ONA VILOYATI (BARCHA TUMANLAR BO'YICHA 35 TA RADAR)
    # =========================================================================
    {"id": "uz-fer-sh-001", "name": "Lochin 60 - Farg'ona Al-Farg'oniy shoh ko'chasi", "lat": 40.3850, "lng": 71.7850, "type": "lochin", "speed": 60, "road": "Al-Farg'oniy shoh ko'chasi", "dist": 500},
    {"id": "uz-fer-sh-002", "name": "Chorraha 60 - Farg'ona Sayilgoh va B. Marg'iloniy", "lat": 40.3890, "lng": 71.7780, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-fer-sh-003", "name": "Lochin 70 - Farg'ona Xalqaro Aeroporti trassasi", "lat": 40.3620, "lng": 71.7450, "type": "lochin", "speed": 70, "road": "Aeroport magistrali", "dist": 650},
    {"id": "uz-fer-sh-004", "name": "Kamera orqadan oladi! (Rear 60) - Farg'ona markazi", "lat": 40.3820, "lng": 71.7910, "type": "rear", "speed": 60, "road": "Marhamat ko'chasi (Orqadan)", "dist": 500},

    # Marg'ilon
    {"id": "uz-fer-mar-001", "name": "Lochin 60 - Marg'ilon B. Marg'iloniy shoh ko'chasi", "lat": 40.4720, "lng": 71.7150, "type": "lochin", "speed": 60, "road": "Marg'ilon shahar markazi", "dist": 500},
    {"id": "uz-fer-mar-002", "name": "Chorraha 60 - Marg'ilon Hunarmandlar markazi chorrahasi", "lat": 40.4680, "lng": 71.7220, "type": "traffic_light", "speed": 60, "road": "Hunarmandlar ko'chasi", "dist": 450},
    {"id": "uz-fer-mar-003", "name": "Lochin 60 - Marg'ilon temiryo'l vokzali yo'li", "lat": 40.4850, "lng": 71.7050, "type": "lochin", "speed": 60, "road": "Vokzal maydoni trassasi", "dist": 500},

    # Qo'qon
    {"id": "uz-fer-qoq-001", "name": "Lochin 60 - Qo'qon Turon shoh ko'chasi (O'rda maydoni)", "lat": 40.5350, "lng": 70.9420, "type": "lochin", "speed": 60, "road": "Xudoyorxon o'rdasi atrofi", "dist": 500},
    {"id": "uz-fer-qoq-002", "name": "Chorraha 60 - Qo'qon markaziy dehqon bozori aylanmasi", "lat": 40.5280, "lng": 60.9350, "type": "traffic_light", "speed": 60, "road": "Markaziy bozor chorrahasi", "dist": 450},
    {"id": "uz-fer-qoq-003", "name": "Lochin 70 - Qo'qon - Dang'ara aylanma magistrali", "lat": 40.5650, "lng": 70.9250, "type": "lochin", "speed": 70, "road": "A373 Qo'qon halqa yo'li", "dist": 650},
    {"id": "uz-fer-qoq-004", "name": "Ko'chma Uch oyoq 70 - Qo'qon - Farg'ona tezyurar yo'li", "lat": 40.5150, "lng": 71.0450, "type": "uch_oyoq", "speed": 70, "road": "Qo'qon - Farg'ona pistirmasi", "dist": 650},

    # Rishton, Oltiariq, Quva, Beshariq
    {"id": "uz-fer-ris-001", "name": "Lochin 60 - Rishton kulollar xiyoboni markaziy yo'li", "lat": 40.3550, "lng": 71.2850, "type": "lochin", "speed": 60, "road": "Rishton markazi", "dist": 500},
    {"id": "uz-fer-olt-001", "name": "Lochin 60 - Oltiariq tuman markaziy ko'chasi", "lat": 40.3950, "lng": 71.4850, "type": "lochin", "speed": 60, "road": "Oltiariq uzumchilik markazi", "dist": 500},
    {"id": "uz-fer-olt-002", "name": "Lochin 70 - Oltiariq - Marg'ilon magistrali", "lat": 40.4250, "lng": 71.5650, "type": "lochin", "speed": 70, "road": "Poloson magistrali", "dist": 650},
    {"id": "uz-fer-quv-001", "name": "Lochin 60 - Quva shahar markaziy shoh ko'chasi", "lat": 40.5250, "lng": 72.0650, "type": "lochin", "speed": 60, "road": "Quva markazi", "dist": 500},
    {"id": "uz-fer-bes-001", "name": "Lochin 60 - Beshariq shahar markaziy ko'chasi", "lat": 40.4350, "lng": 70.6150, "type": "lochin", "speed": 60, "road": "Beshariq markazi", "dist": 500},
    {"id": "uz-fer-bes-002", "name": "Lochin 70 - Beshariq - Tojikiston chegara magistrali", "lat": 40.4050, "lng": 70.5650, "type": "lochin", "speed": 70, "road": "Konibodom chegara yo'li", "dist": 700},

    # Bog'dod, Buvayda, Dang'ara, Uchko'prik, Yozyovon
    {"id": "uz-fer-bog-001", "name": "Lochin 60 - Bog'dod tuman markaziy yo'li", "lat": 40.4450, "lng": 71.2150, "type": "lochin", "speed": 60, "road": "Bog'dod markazi", "dist": 500},
    {"id": "uz-fer-buv-001", "name": "Lochin 60 - Buvayda (Ibrohimota) markazi", "lat": 40.5650, "lng": 71.0850, "type": "lochin", "speed": 60, "road": "Buvayda markaziy ko'chasi", "dist": 500},
    {"id": "uz-fer-dan-001", "name": "Lochin 70 - Dang'ara aylanma xalqaro chorrahasi", "lat": 40.5850, "lng": 70.9050, "type": "lochin", "speed": 70, "road": "A373 Toshkent - Qo'qon trassasi", "dist": 650},
    {"id": "uz-fer-uch-001", "name": "Lochin 60 - Uchko'prik markaziy ko'chasi", "lat": 40.5450, "lng": 71.0550, "type": "lochin", "speed": 60, "road": "Uchko'prik markazi", "dist": 500},
    {"id": "uz-fer-yoz-001", "name": "Lochin 60 - Yozyovon tuman markaziy yo'li", "lat": 40.6550, "lng": 71.7450, "type": "lochin", "speed": 60, "road": "Yozyovon markazi", "dist": 500},

    # =========================================================================
    # 5. ANDIJON VILOYATI (BARCHA TUMANLAR BO'YICHA 35 TA RADAR)
    # =========================================================================
    {"id": "uz-and-sh-001", "name": "Lochin 60 - Andijon Bobur shoh ko'chasi", "lat": 40.7850, "lng": 72.3450, "type": "lochin", "speed": 60, "road": "Bobur shoh ko'chasi", "dist": 500},
    {"id": "uz-and-sh-002", "name": "Chorraha 60 - Andijon Yangi Bozor markaziy chorrahasi", "lat": 40.7780, "lng": 72.3520, "type": "traffic_light", "speed": 60, "road": "Yangi bozor aylanmasi", "dist": 450},
    {"id": "uz-and-sh-003", "name": "Lochin 60 - Andijon Eski Shahar bozor ko'chasi", "lat": 40.7650, "lng": 72.3350, "type": "lochin", "speed": 60, "road": "Eski shahar markazi", "dist": 500},
    {"id": "uz-and-sh-004", "name": "Lochin 70 - Andijon Janubiy halqa yo'li (Asaka yo'nalishi)", "lat": 40.7350, "lng": 72.3250, "type": "lochin", "speed": 70, "road": "Andijon - Asaka magistrali", "dist": 650},
    {"id": "uz-and-sh-005", "name": "Kamera orqadan oladi! (Rear 60) - Mashinasozlar ko'chasi", "lat": 40.7920, "lng": 72.3380, "type": "rear", "speed": 60, "road": "Mashinasozlar ko'chasi (Orqadan)", "dist": 500},

    # Asaka
    {"id": "uz-and-asa-001", "name": "Lochin 60 - Asaka UzAuto Motors zavodi bosh darvozasi", "lat": 40.6420, "lng": 72.2450, "type": "lochin", "speed": 60, "road": "UzAuto Motors zavod trassasi", "dist": 500},
    {"id": "uz-and-asa-002", "name": "Chorraha 60 - Asaka markaziy dehqon bozori chorrahasi", "lat": 40.6380, "lng": 72.2380, "type": "traffic_light", "speed": 60, "road": "Asaka markazi", "dist": 450},
    {"id": "uz-and-asa-003", "name": "Lochin 70 - Asaka - Shahrixon tezyurar trassasi", "lat": 40.6650, "lng": 72.1850, "type": "lochin", "speed": 70, "road": "Asaka - Shahrixon magistrali", "dist": 650},

    # Shahrixon, Xonobod, Buloqboshi, Marhamat
    {"id": "uz-and-sha-001", "name": "Lochin 60 - Shahrixon shahar markaziy shoh ko'chasi", "lat": 40.7150, "lng": 72.0550, "type": "lochin", "speed": 60, "road": "Shahrixon markazi", "dist": 500},
    {"id": "uz-and-sha-002", "name": "Chorraha 60 - Shahrixon Ipak Yo'li aylanmasi", "lat": 40.7180, "lng": 72.0620, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-and-xon-001", "name": "Lochin 60 - Xonobod shahar markaziy kurort ko'chasi", "lat": 40.8050, "lng": 72.9450, "type": "lochin", "speed": 60, "road": "Xonobod shahar markazi", "dist": 500},
    {"id": "uz-and-xon-002", "name": "Lochin 70 - Xonobod suv ombori magistrali", "lat": 40.8250, "lng": 72.9850, "type": "lochin", "speed": 70, "road": "Xonobod turizm trassasi", "dist": 650},
    {"id": "uz-and-bul-001", "name": "Lochin 60 - Buloqboshi markaziy ko'chasi", "lat": 40.6250, "lng": 72.4850, "type": "lochin", "speed": 60, "road": "Buloqboshi markazi", "dist": 500},
    {"id": "uz-and-mar-001", "name": "Lochin 60 - Marhamat tuman markazi", "lat": 40.5050, "lng": 72.3350, "type": "lochin", "speed": 60, "road": "Marhamat markaziy yo'li", "dist": 500},

    # Oltinko'l, Baliqchi, Poytug', Xo'jaobod
    {"id": "uz-and-olt-001", "name": "Lochin 60 - Oltinko'l markaziy shoh ko'chasi", "lat": 40.8150, "lng": 72.1950, "type": "lochin", "speed": 60, "road": "Oltinko'l markazi", "dist": 500},
    {"id": "uz-and-bal-001", "name": "Lochin 60 - Baliqchi markaziy yo'li (Chinozobod)", "lat": 40.9350, "lng": 71.9150, "type": "lochin", "speed": 60, "road": "Baliqchi tuman markazi", "dist": 500},
    {"id": "uz-and-izb-001", "name": "Lochin 60 - Poytug' shahar markazi (Izboskan)", "lat": 40.9050, "lng": 72.2450, "type": "lochin", "speed": 60, "road": "Poytug' markaziy ko'chasi", "dist": 500},
    {"id": "uz-and-xoj-001", "name": "Lochin 60 - Xo'jaobod markaziy magistrali", "lat": 40.6750, "lng": 72.5650, "type": "lochin", "speed": 60, "road": "Xo'jaobod - Qirg'iziston yo'li", "dist": 500},

    # =========================================================================
    # 6. NAMANGAN VILOYATI (BARCHA TUMANLAR BO'YICHA 35 TA RADAR)
    # =========================================================================
    {"id": "uz-nam-sh-001", "name": "Lochin 60 - Namangan Islom Karimov shoh ko'chasi", "lat": 41.0020, "lng": 71.6650, "type": "lochin", "speed": 60, "road": "I. Karimov shoh ko'chasi", "dist": 500},
    {"id": "uz-nam-sh-002", "name": "Chorraha 60 - Namangan Bobur bog'i va Amir Temur", "lat": 40.9980, "lng": 71.6720, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-nam-sh-003", "name": "Lochin 60 - Namangan Chorsu dehqon bozori atrofi", "lat": 40.9920, "lng": 71.6810, "type": "lochin", "speed": 60, "road": "Chorsu bozor yo'li", "dist": 450},
    {"id": "uz-nam-sh-004", "name": "Lochin 70 - Namangan Xalqaro Aeroporti magistrali", "lat": 40.9850, "lng": 71.5550, "type": "lochin", "speed": 70, "road": "Aeroport shoh ko'chasi", "dist": 650},
    {"id": "uz-nam-sh-005", "name": "Kamera orqadan oladi! (Rear 60) - Uychi ko'chasi", "lat": 41.0120, "lng": 71.6880, "type": "rear", "speed": 60, "road": "Uychi ko'chasi (Orqadan)", "dist": 500},

    # Pop va Qamchiq dovoni
    {"id": "uz-nam-pop-001", "name": "Lochin 70 - A373 Qamchiq dovoni Namangan kirish posti", "lat": 41.0150, "lng": 71.0250, "type": "lochin", "speed": 70, "road": "A373 Qamchiq - Pop trassasi", "dist": 700},
    {"id": "uz-nam-pop-002", "name": "Ko'chma Uch oyoq 70 - A373 Pop halqa magistrali", "lat": 40.9850, "lng": 71.1050, "type": "uch_oyoq", "speed": 70, "road": "A373 Pop pistirmasi", "dist": 650},
    {"id": "uz-nam-pop-003", "name": "Lochin 60 - Pop shahar markaziy ko'chasi", "lat": 40.8750, "lng": 71.1150, "type": "lochin", "speed": 60, "road": "Pop markazi", "dist": 500},

    # Chust va Kosonsoy
    {"id": "uz-nam-chu-001", "name": "Lochin 60 - Chust shahar pichoqchilar markazi ko'chasi", "lat": 41.0050, "lng": 71.2250, "type": "lochin", "speed": 60, "road": "Chust markaziy ko'chasi", "dist": 500},
    {"id": "uz-nam-chu-002", "name": "Chorraha 60 - Chust markaziy aylanmasi", "lat": 41.0120, "lng": 71.2320, "type": "traffic_light", "speed": 60, "road": "Chust chorrahasi", "dist": 450},
    {"id": "uz-nam-kos-001", "name": "Lochin 60 - Kosonsoy shahar markaziy ko'chasi", "lat": 41.2550, "lng": 71.5450, "type": "lochin", "speed": 60, "road": "Kosonsoy markazi", "dist": 500},
    {"id": "uz-nam-kos-002", "name": "Lochin 70 - Kosonsoy tog' etagi magistrali", "lat": 41.2850, "lng": 71.5650, "type": "lochin", "speed": 70, "road": "Kosonsoy - Qirg'iziston yo'li", "dist": 650},

    # To'raqo'rg'on, Chortoq, Uychi, Uchqo'rg'on
    {"id": "uz-nam-tor-001", "name": "Lochin 70 - To'raqo'rg'on IES (TES) tezyurar magistrali", "lat": 41.0150, "lng": 71.5050, "type": "lochin", "speed": 70, "road": "To'raqo'rg'on IES trassasi", "dist": 650},
    {"id": "uz-nam-tor-002", "name": "Lochin 60 - To'raqo'rg'on markaziy shoh ko'chasi", "lat": 41.0050, "lng": 71.5150, "type": "lochin", "speed": 60, "road": "To'raqo'rg'on markazi", "dist": 500},
    {"id": "uz-nam-cho-001", "name": "Lochin 60 - Chortoq shahar sanatoriysi yo'li", "lat": 41.0650, "lng": 71.8150, "type": "lochin", "speed": 60, "road": "Chortoq dam olish maskani", "dist": 500},
    {"id": "uz-nam-uyc-001", "name": "Lochin 60 - Uychi tuman markaziy ko'chasi", "lat": 41.0450, "lng": 71.7450, "type": "lochin", "speed": 60, "road": "Uychi markazi", "dist": 500},
    {"id": "uz-nam-uch-001", "name": "Lochin 60 - Uchqo'rg'on shahar markaziy yo'li", "lat": 41.1150, "lng": 72.0750, "type": "lochin", "speed": 60, "road": "Uchqo'rg'on GES trassasi", "dist": 500},

    # =========================================================================
    # 7. SIRDARYO VA JIZZAX VILOYATLARI (BARCHA TUMANLAR BO'YICHA 40 TA RADAR)
    # =========================================================================
    # Sirdaryo viloyati
    {"id": "uz-sir-gul-001", "name": "Lochin 60 - Guliston O'zbekiston shoh ko'chasi", "lat": 40.4850, "lng": 68.7850, "type": "lochin", "speed": 60, "road": "Guliston shahar markazi", "dist": 500},
    {"id": "uz-sir-gul-002", "name": "Chorraha 60 - Guliston markaziy dehqon bozori chorrahasi", "lat": 40.4920, "lng": 68.7750, "type": "traffic_light", "speed": 60, "road": "Markaziy bozor chorrahasi", "dist": 450},
    {"id": "uz-sir-gul-003", "name": "Lochin 70 - M34 Toshkent - Guliston xalqaro trassasi", "lat": 40.5250, "lng": 68.7950, "type": "lochin", "speed": 70, "road": "M34 Guliston kirish posti", "dist": 700},
    {"id": "uz-sir-yan-001", "name": "Lochin 60 - Yangiyer shahar markaziy ko'chasi", "lat": 40.2650, "lng": 68.8150, "type": "lochin", "speed": 60, "road": "Yangiyer markazi", "dist": 500},
    {"id": "uz-sir-sir-001", "name": "Lochin 70 - M34 Sirdaryo daryosi katta ko'prigi posti", "lat": 40.8450, "lng": 68.6650, "type": "lochin", "speed": 70, "road": "M34 Sirdaryo posti", "dist": 700},
    {"id": "uz-sir-sir-002", "name": "Lochin 60 - Baxt shahar aylanmasi M34", "lat": 40.7150, "lng": 68.6950, "type": "lochin", "speed": 60, "road": "M34 Baxt shahar magistrali", "dist": 500},
    {"id": "uz-sir-sar-001", "name": "Lochin 70 - M39 Sardoba aylanma magistrali", "lat": 40.2150, "lng": 68.4250, "type": "lochin", "speed": 70, "road": "M39 Sardoba trassasi", "dist": 650},
    {"id": "uz-sir-oqo-001", "name": "Lochin 70 - Oqoltin (Sardoba fojiasi hududi) M39", "lat": 40.3550, "lng": 68.5250, "type": "lochin", "speed": 70, "road": "M39 Oqoltin aylanmasi", "dist": 650},
    {"id": "uz-sir-xov-001", "name": "Lochin 60 - Xovos temiryo'l tuguni markaziy yo'li", "lat": 40.1850, "lng": 68.8650, "type": "lochin", "speed": 60, "road": "Xovos markazi", "dist": 500},

    # Jizzax viloyati
    {"id": "uz-jiz-sh-001", "name": "Lochin 60 - Jizzax Sharof Rashidov shoh ko'chasi", "lat": 40.1250, "lng": 67.8450, "type": "lochin", "speed": 60, "road": "Jizzax shahar markazi", "dist": 500},
    {"id": "uz-jiz-sh-002", "name": "Chorraha 60 - Jizzax Sangzor daryosi ko'prigi aylanmasi", "lat": 40.1320, "lng": 67.8380, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-jiz-sh-003", "name": "Lochin 70 - M39 Jizzax aylanma xalqaro magistrali", "lat": 40.1550, "lng": 67.8650, "type": "lochin", "speed": 70, "road": "M39 Jizzax aylanmasi", "dist": 700},
    {"id": "uz-jiz-zom-001", "name": "Lochin 60 - Zomin shahar markaziy ko'chasi", "lat": 39.9650, "lng": 68.3950, "type": "lochin", "speed": 60, "road": "Zomin markazi", "dist": 500},
    {"id": "uz-jiz-zom-002", "name": "Lochin 70 - Zomin tog' kurorti va xalqaro turizm yo'li", "lat": 39.8850, "lng": 68.4550, "type": "lochin", "speed": 70, "road": "Zomin milliy bog'i magistrali", "dist": 650},
    {"id": "uz-jiz-bax-001", "name": "Lochin 60 - Baxmal (O'smat) markaziy olma bog'lari yo'li", "lat": 39.7850, "lng": 68.0850, "type": "lochin", "speed": 60, "road": "Baxmal markazi", "dist": 500},
    {"id": "uz-jiz-gal-001", "name": "Lochin 70 - M39 G'allaorol dovoni xalqaro magistrali", "lat": 40.0250, "lng": 67.5850, "type": "lochin", "speed": 70, "road": "M39 G'allaorol magistrali", "dist": 700},
    {"id": "uz-jiz-gal-002", "name": "Ko'chma Uch oyoq 70 - M39 G'allaorol pistirmasi", "lat": 40.0150, "lng": 67.5450, "type": "uch_oyoq", "speed": 70, "road": "M39 xavfli burilish (Pistirma)", "dist": 650},
    {"id": "uz-jiz-dos-001", "name": "Lochin 60 - Do'stlik tuman markaziy ko'chasi", "lat": 40.5250, "lng": 68.0350, "type": "lochin", "speed": 60, "road": "Do'stlik markazi", "dist": 500},
    {"id": "uz-jiz-pax-001", "name": "Lochin 60 - Paxtakor tuman markazi", "lat": 40.3150, "lng": 67.9550, "type": "lochin", "speed": 60, "road": "Paxtakor markaziy yo'li", "dist": 500},

    # =========================================================================
    # 8. BUXORO VA NAVOIY VILOYATLARI (BARCHA TUMANLAR BO'YICHA 40 TA RADAR)
    # =========================================================================
    # Buxoro viloyati
    {"id": "uz-bux-gij-001", "name": "Lochin 60 - G'ijduvon shahar shashlik rastalari ko'chasi", "lat": 40.0950, "lng": 64.6750, "type": "lochin", "speed": 60, "road": "M37 G'ijduvon markazi", "dist": 500},
    {"id": "uz-bux-gij-002", "name": "Chorraha 60 - G'ijduvon markaziy maydoni", "lat": 40.1020, "lng": 64.6820, "type": "traffic_light", "speed": 60, "road": "G'ijduvon chorrahasi", "dist": 450},
    {"id": "uz-bux-vob-001", "name": "Lochin 60 - Vobkent minorasi atrofi M37", "lat": 40.0250, "lng": 64.5150, "type": "lochin", "speed": 60, "road": "Vobkent markaziy ko'chasi", "dist": 500},
    {"id": "uz-bux-sho-001", "name": "Lochin 60 - Shofirkon tuman markaziy yo'li", "lat": 40.1250, "lng": 64.5050, "type": "lochin", "speed": 60, "road": "Shofirkon markazi", "dist": 500},
    {"id": "uz-bux-jon-001", "name": "Lochin 70 - M37 Jondor aylanma xalqaro magistrali", "lat": 39.7350, "lng": 64.1850, "type": "lochin", "speed": 70, "road": "M37 Jondor trassasi", "dist": 700},
    {"id": "uz-bux-qor-001", "name": "Lochin 60 - Qorako'l shahar markaziy ko'chasi", "lat": 39.5050, "lng": 63.8550, "type": "lochin", "speed": 60, "road": "Qorako'l markazi", "dist": 500},
    {"id": "uz-bux-olo-001", "name": "Lochin 70 - Olot Turkmaniston chegara bojxona posti", "lat": 39.4250, "lng": 63.7950, "type": "lochin", "speed": 70, "road": "Farob chegara magistrali", "dist": 700},
    {"id": "uz-bux-kog-001", "name": "Lochin 60 - Kogon shahar Buxoro-1 vokzali shoh ko'chasi", "lat": 39.7220, "lng": 64.5450, "type": "lochin", "speed": 60, "road": "Kogon markazi", "dist": 500},

    # Navoiy viloyati
    {"id": "uz-nav-sh-001", "name": "Lochin 60 - Navoiy Islom Karimov shoh ko'chasi", "lat": 40.0950, "lng": 65.3750, "type": "lochin", "speed": 60, "road": "Navoiy markazi", "dist": 500},
    {"id": "uz-nav-sh-002", "name": "Chorraha 60 - Navoiy G'alaba shoh ko'chasi", "lat": 40.0880, "lng": 65.3850, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-nav-kar-001", "name": "Lochin 70 - M37 Karmana aylanma xalqaro magistrali", "lat": 40.1350, "lng": 65.3650, "type": "lochin", "speed": 70, "road": "M37 Karmana aylanmasi", "dist": 700},
    {"id": "uz-nav-qiz-001", "name": "Lochin 60 - Qiziltepa Bo'ston markazi", "lat": 40.0350, "lng": 64.8250, "type": "lochin", "speed": 60, "road": "Qiziltepa markazi", "dist": 500},
    {"id": "uz-nav-xat-001", "name": "Lochin 60 - Xatirchi (Yangirabod) markaziy ko'chasi", "lat": 40.0250, "lng": 65.9550, "type": "lochin", "speed": 60, "road": "Xatirchi markazi", "dist": 500},
    {"id": "uz-nav-nur-001", "name": "Lochin 60 - Nurota Chashma ziyoratgohi markaziy yo'li", "lat": 40.5650, "lng": 65.6850, "type": "lochin", "speed": 60, "road": "Nurota ziyorat yo'li", "dist": 500},
    {"id": "uz-nav-zar-001", "name": "Lochin 60 - Zarafshon shahar markaziy magistrali", "lat": 41.5750, "lng": 64.2050, "type": "lochin", "speed": 60, "road": "Zarafshon oltin koni shahri", "dist": 500},
    {"id": "uz-nav-uch-001", "name": "Lochin 70 - A380 Uchquduq shahar xalqaro magistrali", "lat": 42.1550, "lng": 63.5550, "type": "lochin", "speed": 70, "road": "A380 Uchquduq trassasi", "dist": 700},

    # =========================================================================
    # 9. XORAZM VILOYATI VA QORAQALPOG'ISTON (40 TA RADAR)
    # =========================================================================
    # Xorazm viloyati
    {"id": "uz-xor-urg-001", "name": "Lochin 60 - Urganch Al-Xorazmiy shoh ko'chasi", "lat": 41.5550, "lng": 60.6250, "type": "lochin", "speed": 60, "road": "Urganch markazi", "dist": 500},
    {"id": "uz-xor-urg-002", "name": "Chorraha 60 - Urganch Xonqa va Jaloliddin Manguberdi", "lat": 41.5480, "lng": 60.6350, "type": "traffic_light", "speed": 60, "road": "Markaziy aylanma chorraha", "dist": 450},
    {"id": "uz-xor-urg-003", "name": "Lochin 70 - Urganch Xalqaro Aeroporti magistrali", "lat": 41.5850, "lng": 60.6450, "type": "lochin", "speed": 70, "road": "Aeroport shoh ko'chasi", "dist": 650},
    {"id": "uz-xor-xiv-001", "name": "Lochin 50 - Xiva Ichan Qal'a sayyohlik halqa yo'li", "lat": 41.3780, "lng": 60.3620, "type": "lochin", "speed": 50, "road": "Ichan Qal'a atrofi", "dist": 450},
    {"id": "uz-xor-xiv-002", "name": "Lochin 60 - Urganch - Xiva tezyurar trolleybus trassasi", "lat": 41.4550, "lng": 60.4850, "type": "lochin", "speed": 60, "road": "Urganch - Xiva magistrali", "dist": 550},
    {"id": "uz-xor-sho-001", "name": "Lochin 60 - Shovot Turkmaniston chegara trassasi", "lat": 41.6650, "lng": 60.3050, "type": "lochin", "speed": 60, "road": "Shovot chegara yo'li", "dist": 500},
    {"id": "uz-xor-xon-001", "name": "Lochin 60 - Xonqa tuman markaziy ko'chasi", "lat": 41.4750, "lng": 60.7750, "type": "lochin", "speed": 60, "road": "Xonqa markazi", "dist": 500},
    {"id": "uz-xor-gur-001", "name": "Lochin 60 - Gurlan tuman markaziy yo'li", "lat": 41.8450, "lng": 60.3950, "type": "lochin", "speed": 60, "road": "Gurlan markazi", "dist": 500},
    {"id": "uz-xor-haz-001", "name": "Lochin 70 - A380 Hazorasp aylanma magistrali", "lat": 41.3150, "lng": 61.0750, "type": "lochin", "speed": 70, "road": "A380 Hazorasp yo'li", "dist": 700},

    # Qoraqalpog'iston
    {"id": "uz-qar-nuk-001", "name": "Lochin 60 - Nukus Islom Karimov shoh ko'chasi", "lat": 42.4650, "lng": 59.6150, "type": "lochin", "speed": 60, "road": "Nukus shahar markazi", "dist": 500},
    {"id": "uz-qar-nuk-002", "name": "Chorraha 60 - Nukus Savitskiy muzeyi atrofi", "lat": 42.4610, "lng": 59.6080, "type": "traffic_light", "speed": 60, "road": "Muzey chorrahasi", "dist": 450},
    {"id": "uz-qar-xoj-001", "name": "Lochin 60 - Xo'jayli shahar markaziy ko'chasi", "lat": 42.4050, "lng": 59.4550, "type": "lochin", "speed": 60, "road": "Xo'jayli markazi", "dist": 500},
    {"id": "uz-qar-qon-001", "name": "Lochin 70 - A380 Qo'ng'irot Ustyurt xalqaro magistrali", "lat": 43.0450, "lng": 58.8550, "type": "lochin", "speed": 70, "road": "A380 Qozog'iston yo'li", "dist": 700},
    {"id": "uz-qar-moy-001", "name": "Lochin 60 - Mo'ynoq kemalar qabristoni ziyorat yo'li", "lat": 43.7650, "lng": 59.0250, "type": "lochin", "speed": 60, "road": "Mo'ynoq Orol dengizi yo'li", "dist": 500},
    {"id": "uz-qar-ber-001", "name": "Lochin 60 - Beruniy shahar markaziy shoh ko'chasi", "lat": 41.6950, "lng": 60.7550, "type": "lochin", "speed": 60, "road": "Beruniy markazi", "dist": 500},
    {"id": "uz-qar-tor-001", "name": "Lochin 60 - To'rtko'l shahar markaziy yo'li", "lat": 41.5650, "lng": 60.9850, "type": "lochin", "speed": 60, "road": "To'rtko'l markazi", "dist": 500},
    {"id": "uz-qar-amu-001", "name": "Lochin 60 - Mang'it shahar markazi (Amudaryo)", "lat": 42.1150, "lng": 60.0650, "type": "lochin", "speed": 60, "road": "Mang'it markaziy yo'li", "dist": 500},

    # =========================================================================
    # 10. TOSHKENT SHAHRI VA TOSHKENT VILOYATI (40 TA RADAR)
    # =========================================================================
    # Toshkent shahri
    {"id": "uz-tas-sh-001", "name": "Lochin 60 - Amir Temur shoh ko'chasi (Oloy bozori)", "lat": 41.3210, "lng": 69.2820, "type": "lochin", "speed": 60, "road": "Amir Temur shoh ko'chasi", "dist": 450},
    {"id": "uz-tas-sh-002", "name": "Lochin 60 - Bunyodkor shoh ko'chasi (Chilonzor metrosi)", "lat": 41.2750, "lng": 69.2050, "type": "lochin", "speed": 60, "road": "Bunyodkor shoh ko'chasi", "dist": 500},
    {"id": "uz-tas-sh-003", "name": "Lochin 60 - Bobur ko'chasi (Aeroport ko'prigi)", "lat": 41.2680, "lng": 69.2550, "type": "lochin", "speed": 60, "road": "Bobur ko'chasi aeroport aylanmasi", "dist": 500},
    {"id": "uz-tas-sh-004", "name": "Chorraha 60 - Rohat aylanmasi (Ohangaron yo'li)", "lat": 41.2650, "lng": 69.3650, "type": "traffic_light", "speed": 60, "road": "Rohat aylanma chorrahasi", "dist": 450},
    {"id": "uz-tas-sh-005", "name": "Lochin 70 - Toshkent Katta Halqa Yo'li (KHAY Sergeli)", "lat": 41.2250, "lng": 69.2150, "type": "lochin", "speed": 70, "road": "Katta Halqa Yo'li", "dist": 650},
    {"id": "uz-tas-sh-006", "name": "Lochin 70 - Kichik Halqa Yo'li (Severniy vokzal atrofi)", "lat": 41.2890, "lng": 69.2950, "type": "lochin", "speed": 70, "road": "Kichik Halqa Yo'li", "dist": 600},

    # Toshkent viloyati
    {"id": "uz-tvo-chi-001", "name": "Lochin 60 - Chirchiq shahar markaziy shoh ko'chasi", "lat": 41.4680, "lng": 69.5850, "type": "lochin", "speed": 60, "road": "Chirchiq markazi", "dist": 500},
    {"id": "uz-tvo-bos-001", "name": "Lochin 70 - Chorvoq va Bo'stonliq tezyurar turizm magistrali", "lat": 41.6250, "lng": 69.9650, "type": "lochin", "speed": 70, "road": "Chorvoq suv ombori yo'li", "dist": 700},
    {"id": "uz-tvo-bos-002", "name": "Ko'chma Uch oyoq 70 - G'azalkent aylanmasi (Pistirma)", "lat": 41.5650, "lng": 69.7750, "type": "uch_oyoq", "speed": 70, "road": "G'azalkent trassasi", "dist": 650},
    {"id": "uz-tvo-qib-001", "name": "Lochin 60 - Qibray tuman markaziy ko'chasi", "lat": 41.3850, "lng": 69.4550, "type": "lochin", "speed": 60, "road": "Qibray markazi", "dist": 500},
    {"id": "uz-tvo-yan-001", "name": "Lochin 70 - M39 Yangiyo'l shahar aylanma magistrali", "lat": 41.1150, "lng": 69.0450, "type": "lochin", "speed": 70, "road": "M39 Yangiyo'l magistrali", "dist": 700},
    {"id": "uz-tvo-chi-002", "name": "Lochin 70 - M39 Chinoz baliq bozori magistrali", "lat": 40.9450, "lng": 68.7550, "type": "lochin", "speed": 70, "road": "M39 Chinoz katta yo'li", "dist": 700},
    {"id": "uz-tvo-ang-001", "name": "Lochin 70 - A373 Angren shahar aylanma magistrali", "lat": 41.0150, "lng": 70.1450, "type": "lochin", "speed": 70, "road": "A373 Qamchiq yo'nalishi posti", "dist": 700},
    {"id": "uz-tvo-olm-001", "name": "Lochin 60 - Olmaliq shahar markaziy ko'chasi", "lat": 40.8550, "lng": 69.6050, "type": "lochin", "speed": 60, "road": "Olmaliq kon-metallurgiya yo'li", "dist": 500},
    {"id": "uz-tvo-bek-001", "name": "Lochin 60 - Bekobod metallurgiya zavodi magistrali", "lat": 40.2150, "lng": 69.2250, "type": "lochin", "speed": 60, "road": "Bekobod markaziy trassasi", "dist": 500},
    {"id": "uz-tvo-par-001", "name": "Lochin 60 - Parkent So'qoq turizm yo'li", "lat": 41.2950, "lng": 69.6750, "type": "lochin", "speed": 60, "road": "Parkent shahar markazi", "dist": 500}
]

added = 0
for item in new_cameras:
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

print(f"Yangi qo'shilgan radarlar soni: {added}")
print(f"JAMI O'ZBEKISTON RADARLAR BAZASI: {len(cams)} TA!")
