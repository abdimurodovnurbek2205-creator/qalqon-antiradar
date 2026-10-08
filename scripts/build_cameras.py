import json
import os

cams = [
    # ==================== SAMARQAND SHAHRI VA VILOYATI ====================
    {
        "id": "uz-sam-001",
        "name": "Lochin 60 - Registon ko'chasi",
        "lat": 39.6548, "lng": 66.9752,
        "type": "lochin", "speedLimit": 60, "azimuth": 90,
        "roadName": "Registon ko'chasi (Samarqand)", "distanceAlertThreshold": 500
    },
    {
        "id": "uz-sam-002",
        "name": "Chorraha kamerasi - Rudakiy va Gagarin",
        "lat": 39.6580, "lng": 66.9550,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 45,
        "roadName": "Rudakiy va Gagarin chorrahasi", "distanceAlertThreshold": 450
    },
    {
        "id": "uz-sam-003",
        "name": "Kamera orqadan oladi! - Beruniy ko'chasi",
        "lat": 39.6640, "lng": 66.9420,
        "type": "rear", "speedLimit": 60, "azimuth": 315,
        "roadName": "Beruniy ko'chasi (Orqadan uradi)", "distanceAlertThreshold": 500
    },
    {
        "id": "uz-sam-004",
        "name": "Lochin 60 - Spitamen shoh ko'chasi",
        "lat": 39.6450, "lng": 66.9380,
        "type": "lochin", "speedLimit": 60, "azimuth": 180,
        "roadName": "Spitamen shoh ko'chasi", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-sam-005",
        "name": "Chorraha kamerasi - Dahbed va Registon",
        "lat": 39.6610, "lng": 66.9790,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 0,
        "roadName": "Dahbed ko'chasi chorrahasi", "distanceAlertThreshold": 450
    },
    {
        "id": "uz-sam-006",
        "name": "Ko'chma Uch oyoq 70 - Ulug'bek rasadxonasi",
        "lat": 39.6740, "lng": 66.9950,
        "type": "uch_oyoq", "speedLimit": 70, "azimuth": 45,
        "roadName": "M39 Toshkent yo'nalishi (Pistirma)", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-sam-007",
        "name": "Lochin 70 - Samarqand Katta halqa yo'li",
        "lat": 39.6850, "lng": 66.9250,
        "type": "lochin", "speedLimit": 70, "azimuth": 270,
        "roadName": "Samarqand aylanma halqa yo'li", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-sam-008",
        "name": "YPX Patrul 360 - Samarqand Vokzal maydoni",
        "lat": 39.6680, "lng": 66.9280,
        "type": "patrul_360", "speedLimit": 60, "azimuth": 220,
        "roadName": "Temiryo'l vokzali atrofi", "distanceAlertThreshold": 500
    },
    {
        "id": "uz-sam-009",
        "name": "Lochin 100 - M39 Samarqand - Jizzax trassasi",
        "lat": 39.7250, "lng": 67.0450,
        "type": "lochin", "speedLimit": 100, "azimuth": 50,
        "roadName": "M39 Xalqaro trassa (Bulung'ur)", "distanceAlertThreshold": 850
    },
    {
        "id": "uz-sam-010",
        "name": "Lochin 100 - M37 Samarqand - Navoiy trassasi",
        "lat": 39.6950, "lng": 66.8250,
        "type": "lochin", "speedLimit": 100, "azimuth": 290,
        "roadName": "M37 Kattaqo'rg'on yo'nalishi", "distanceAlertThreshold": 850
    },
    {
        "id": "uz-sam-011",
        "name": "Lochin 60 - Mirzo Ulug'bek shoh ko'chasi",
        "lat": 39.6505, "lng": 66.9602,
        "type": "lochin", "speedLimit": 60, "azimuth": 320,
        "roadName": "Mirzo Ulug'bek shoh ko'chasi", "distanceAlertThreshold": 500
    },
    {
        "id": "uz-sam-012",
        "name": "Chorraha kamerasi - Beruniy va Spitamen",
        "lat": 39.6595, "lng": 66.9315,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 110,
        "roadName": "Beruniy-Spitamen kesishmasi", "distanceAlertThreshold": 450
    },
    {
        "id": "uz-sam-013",
        "name": "Lochin 60 - Dahbed ko'chasi (Siyob bozori)",
        "lat": 39.6645, "lng": 66.9830,
        "type": "lochin", "speedLimit": 60, "azimuth": 20,
        "roadName": "Dahbed ko'chasi", "distanceAlertThreshold": 500
    },
    {
        "id": "uz-sam-014",
        "name": "Ko'chma Uch oyoq 60 - Motrid mavzesi",
        "lat": 39.6820, "lng": 66.9610,
        "type": "uch_oyoq", "speedLimit": 60, "azimuth": 0,
        "roadName": "Motrid shahar chiqish yo'li", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-sam-015",
        "name": "Lochin 60 - Samarqand Xalqaro Aeroport yo'li",
        "lat": 39.6925, "lng": 66.9880,
        "type": "lochin", "speedLimit": 60, "azimuth": 60,
        "roadName": "Aeroport shoh ko'chasi", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-sam-016",
        "name": "Lochin 70 - Samarqand - Urgut yo'li (A377)",
        "lat": 39.6050, "lng": 67.0250,
        "type": "lochin", "speedLimit": 70, "azimuth": 135,
        "roadName": "A377 Urgut trassasi", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-sam-017",
        "name": "Lochin 70 - Samarqand - Juma / Pastdarg'om yo'li",
        "lat": 39.6380, "lng": 66.8650,
        "type": "lochin", "speedLimit": 70, "azimuth": 250,
        "roadName": "Pastdarg'om yo'nalishi", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-sam-018",
        "name": "YPX Patrul 360 - Kattaqo'rg'on aylanmasi",
        "lat": 39.8850, "lng": 66.2550,
        "type": "patrul_360", "speedLimit": 70, "azimuth": 280,
        "roadName": "M37 Kattaqo'rg'on shahri", "distanceAlertThreshold": 600
    },

    # ==================== TOSHKENT SHAHRI VA VILOYATI ====================
    {
        "id": "uz-tas-001",
        "name": "Lochin 60 - Amir Temur (Oloy bozori)",
        "lat": 41.3195, "lng": 69.2812,
        "type": "lochin", "speedLimit": 60, "azimuth": 25,
        "roadName": "Amir Temur shoh ko'chasi (Toshkent)", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-tas-002",
        "name": "Chorraha kamerasi - A.Qodiriy (Stop-liniya)",
        "lat": 41.3258, "lng": 69.2835,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 25,
        "roadName": "Abdulla Qodiriy va Amir Temur", "distanceAlertThreshold": 450
    },
    {
        "id": "uz-tas-003",
        "name": "A-yo'lak - Alisher Navoiy ko'chasi",
        "lat": 41.3182, "lng": 69.2554,
        "type": "bus_lane", "speedLimit": 60, "azimuth": 105,
        "roadName": "Alisher Navoiy ko'chasi", "distanceAlertThreshold": 380
    },
    {
        "id": "uz-tas-004",
        "name": "Kamera orqadan oladi! - THAY Oqtepa",
        "lat": 41.2854, "lng": 69.1985,
        "type": "rear", "speedLimit": 70, "azimuth": 180,
        "roadName": "THAY Katta halqa yo'li", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-tas-005",
        "name": "AutoCon Koridor - Yangi O'zbekiston Kirish",
        "lat": 41.3450, "lng": 69.3750,
        "type": "avg_start", "speedLimit": 70, "azimuth": 65,
        "roadName": "Yangi O'zbekiston shoh ko'chasi", "distanceAlertThreshold": 700
    },
    {
        "id": "uz-tas-006",
        "name": "AutoCon Koridor - Yangi O'zbekiston Chiqish",
        "lat": 41.3580, "lng": 69.4100,
        "type": "avg_end", "speedLimit": 70, "azimuth": 65,
        "roadName": "Yangi O'zbekiston shoh ko'chasi", "distanceAlertThreshold": 700
    },
    {
        "id": "uz-tas-007",
        "name": "YPX Patrul 360 - Bunyodkor shoh ko'chasi",
        "lat": 41.2785, "lng": 69.2155,
        "type": "patrul_360", "speedLimit": 60, "azimuth": 220,
        "roadName": "Bunyodkor (Mirzo Ulug'bek metrosi)", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-tas-008",
        "name": "Lochin 70 - M39 Toshkent chiqish posti",
        "lat": 41.2350, "lng": 69.1550,
        "type": "lochin", "speedLimit": 70, "azimuth": 240,
        "roadName": "M39 Erkin YPX Posti", "distanceAlertThreshold": 700
    },
    {
        "id": "uz-tas-009",
        "name": "Ko'chma Uch oyoq 100 - M39 Yangiyo'l",
        "lat": 41.1350, "lng": 69.0450,
        "type": "uch_oyoq", "speedLimit": 100, "azimuth": 235,
        "roadName": "M39 Yangiyo'l aylanmasi (Trinoga)", "distanceAlertThreshold": 850
    },
    {
        "id": "uz-tas-010",
        "name": "Lochin 100 - Chorvoq trassasi (4R12)",
        "lat": 41.4350, "lng": 69.5250,
        "type": "lochin", "speedLimit": 100, "azimuth": 50,
        "roadName": "4R12 Chorvoq yo'li", "distanceAlertThreshold": 850
    },
    {
        "id": "uz-tas-011",
        "name": "Lochin 70 - THAY Qo'yliq bozori",
        "lat": 41.2370, "lng": 69.3350,
        "type": "lochin", "speedLimit": 70, "azimuth": 90,
        "roadName": "Toshkent Katta Halqa Yo'li (Qo'yliq)", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-tas-012",
        "name": "Chorraha kamerasi - Shahrisabz va Navoiy",
        "lat": 41.3120, "lng": 69.2780,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 0,
        "roadName": "Shahrisabz ko'chasi", "distanceAlertThreshold": 450
    },

    # ==================== JIZZAX VA SIRDARYO ====================
    {
        "id": "uz-jiz-001",
        "name": "Lochin 70 - Jizzax shahar kirish posti",
        "lat": 40.1150, "lng": 67.8420,
        "type": "lochin", "speedLimit": 70, "azimuth": 250,
        "roadName": "M39 Jizzax aylanma yo'li", "distanceAlertThreshold": 700
    },
    {
        "id": "uz-jiz-002",
        "name": "Ko'chma Uch oyoq 100 - Sangzor daryosi bo'yi",
        "lat": 40.0650, "lng": 67.7250,
        "type": "uch_oyoq", "speedLimit": 100, "azimuth": 240,
        "roadName": "M39 Gallaorol trassasi", "distanceAlertThreshold": 850
    },
    {
        "id": "uz-sir-001",
        "name": "Lochin 70 - Baxt shahri M39",
        "lat": 40.7150, "lng": 68.6950,
        "type": "lochin", "speedLimit": 70, "azimuth": 225,
        "roadName": "M39 Sirdaryo Baxt shahri", "distanceAlertThreshold": 700
    },
    {
        "id": "uz-sir-002",
        "name": "Lochin 100 - Guliston yo'li aylanmasi",
        "lat": 40.5050, "lng": 68.7850,
        "type": "lochin", "speedLimit": 100, "azimuth": 180,
        "roadName": "M34 Guliston trassasi", "distanceAlertThreshold": 850
    },

    # ==================== NAVOIY VA BUXORO ====================
    {
        "id": "uz-nav-001",
        "name": "Lochin 70 - Karmana shahar kirish posti",
        "lat": 40.1380, "lng": 65.3650,
        "type": "lochin", "speedLimit": 70, "azimuth": 285,
        "roadName": "M37 Navoiy Karmana yo'li", "distanceAlertThreshold": 700
    },
    {
        "id": "uz-nav-002",
        "name": "Lochin 100 - M37 Navoiy - Buxoro trassasi",
        "lat": 40.1150, "lng": 65.1850,
        "type": "lochin", "speedLimit": 100, "azimuth": 270,
        "roadName": "M37 Xalqaro magistral", "distanceAlertThreshold": 850
    },
    {
        "id": "uz-bux-001",
        "name": "Lochin 60 - Buxoro Naqshbandiy ko'chasi",
        "lat": 39.7745, "lng": 64.4286,
        "type": "lochin", "speedLimit": 60, "azimuth": 90,
        "roadName": "Bahouddin Naqshbandiy ko'chasi", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-bux-002",
        "name": "Chorraha kamerasi - Buxoro Ibrohim Mo'minov",
        "lat": 39.7680, "lng": 64.4420,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 45,
        "roadName": "Buxoro shahar markazi", "distanceAlertThreshold": 450
    },
    {
        "id": "uz-bux-003",
        "name": "Ko'chma Uch oyoq 70 - G'ijduvon shahar aylanmasi",
        "lat": 40.0950, "lng": 64.6750,
        "type": "uch_oyoq", "speedLimit": 70, "azimuth": 260,
        "roadName": "M37 G'ijduvon trassasi", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-bux-004",
        "name": "Lochin 100 - A380 Gazli - Urganch trassasi",
        "lat": 39.9550, "lng": 63.8500,
        "type": "lochin", "speedLimit": 100, "azimuth": 310,
        "roadName": "A380 Qizilqum magistrali", "distanceAlertThreshold": 850
    },

    # ==================== QASHQADARYO VA SURXONDARYO ====================
    {
        "id": "uz-qar-001",
        "name": "Lochin 60 - Qarshi Mustaqillik shoh ko'chasi",
        "lat": 38.8612, "lng": 65.7891,
        "type": "lochin", "speedLimit": 60, "azimuth": 180,
        "roadName": "Mustaqillik shoh ko'chasi (Qarshi)", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-qar-002",
        "name": "Lochin 70 - Qarshi aylanma yo'li",
        "lat": 38.8950, "lng": 65.8150,
        "type": "lochin", "speedLimit": 70, "azimuth": 130,
        "roadName": "A378 Samarqand - Qarshi yo'li", "distanceAlertThreshold": 650
    },
    {
        "id": "uz-qar-003",
        "name": "Lochin 60 - Kitob - Shahrisabz Taxtaqoracha dovoni",
        "lat": 39.3150, "lng": 66.8950,
        "type": "lochin", "speedLimit": 60, "azimuth": 195,
        "roadName": "M39 Taxtaqoracha dovoni", "distanceAlertThreshold": 600
    },
    {
        "id": "uz-sur-001",
        "name": "Lochin 70 - Termiz shahar kirish posti (M39)",
        "lat": 37.2850, "lng": 67.2950,
        "type": "lochin", "speedLimit": 70, "azimuth": 170,
        "roadName": "M39 Termiz xalqaro yo'li", "distanceAlertThreshold": 700
    },

    # ==================== FARG'ONA VODIYSI ====================
    {
        "id": "uz-nam-001",
        "name": "Lochin 60 - Namangan Islom Karimov shoh ko'chasi",
        "lat": 40.9985, "lng": 71.6725,
        "type": "lochin", "speedLimit": 60, "azimuth": 90,
        "roadName": "Namangan shahar markazi", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-and-001",
        "name": "Lochin 60 - Andijon Bobur shoh ko'chasi",
        "lat": 40.7821, "lng": 72.3442,
        "type": "lochin", "speedLimit": 60, "azimuth": 45,
        "roadName": "Bobur shoh ko'chasi (Andijon)", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-and-002",
        "name": "Chorraha kamerasi - Andijon Fitrat ko'chasi",
        "lat": 40.7710, "lng": 72.3580,
        "type": "traffic_light", "speedLimit": 60, "azimuth": 180,
        "roadName": "Fitrat va Bobur chorrahasi", "distanceAlertThreshold": 450
    },
    {
        "id": "uz-fer-001",
        "name": "Lochin 60 - Farg'ona Al-Farg'oniy ko'chasi",
        "lat": 40.3842, "lng": 71.7843,
        "type": "lochin", "speedLimit": 60, "azimuth": 90,
        "roadName": "Al-Farg'oniy shoh ko'chasi", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-fer-002",
        "name": "AutoCon Koridor 60 - Qamchiq dovoni A373",
        "lat": 41.1650, "lng": 70.4850,
        "type": "avg_start", "speedLimit": 60, "azimuth": 105,
        "roadName": "A373 Qamchiq xalqaro dovoni", "distanceAlertThreshold": 750
    },

    # ==================== XORAZM VA QORAQALPOG'ISTON ====================
    {
        "id": "uz-xor-001",
        "name": "Lochin 60 - Urganch Al-Xorazmiy shoh ko'chasi",
        "lat": 41.5510, "lng": 60.6315,
        "type": "lochin", "speedLimit": 60, "azimuth": 90,
        "roadName": "Al-Xorazmiy shoh ko'chasi (Urganch)", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-xor-002",
        "name": "Lochin 60 - Xiva shahar kirish yo'li",
        "lat": 41.3850, "lng": 60.3750,
        "type": "lochin", "speedLimit": 60, "azimuth": 225,
        "roadName": "Urganch - Xiva trassasi", "distanceAlertThreshold": 550
    },
    {
        "id": "uz-nuk-001",
        "name": "Lochin 60 - Nukus Qoraqalpog'iston shoh ko'chasi",
        "lat": 42.4602, "lng": 59.6166,
        "type": "lochin", "speedLimit": 60, "azimuth": 90,
        "roadName": "Nukus shahar markazi", "distanceAlertThreshold": 550
    }
]

os.makedirs('src/data', exist_ok=True)
with open('src/data/speedcams.json', 'w', encoding='utf-8') as f:
    json.dump(cams, f, ensure_ascii=False, indent=2)

print(f"Jami {len(cams)} ta kamera muvaffaqiyatli saqlandi!")
