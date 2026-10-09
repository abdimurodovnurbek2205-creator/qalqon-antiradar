"""
QALQON ANTIRADAR - O'ZBEKISTONNING BARCHA 14 HUDUDI VA TUMANLARI RADARLARINI YARATISH
12 ta viloyat + Toshkent shahri + Qoraqalpog'iston Respublikasi (Barcha tuman markazlari va trassalar)
"""

import json
from pathlib import Path

# Barcha tumanlar va trassalar ma'lumotlari
districts_data = [
    # =========================================================================
    # 1. SURXONDARYO VILOYATI (Barcha tumanlar)
    # =========================================================================
    # Bandixon
    {"id": "uz-sur-ban-001", "name": "Lochin 60 - Bandixon markaziy ko'chasi", "lat": 37.8608, "lng": 67.3883, "type": "lochin", "speed": 60, "road": "Mustaqillik shoh ko'chasi (Bandixon)", "dist": 500},
    {"id": "uz-sur-ban-002", "name": "Ko'chma Uch oyoq 70 - Bandixon - Boysun trassasi", "lat": 37.8850, "lng": 67.3720, "type": "uch_oyoq", "speed": 70, "road": "4R100 Bandixon - Boysun yo'li (Pistirma)", "dist": 650},
    {"id": "uz-sur-ban-003", "name": "Lochin 70 - Bandixon - Qiziriq yo'li", "lat": 37.8320, "lng": 67.3980, "type": "lochin", "speed": 70, "road": "4R100 Qiziriq yo'nalishi", "dist": 600},
    {"id": "uz-sur-ban-004", "name": "Chorraha kamerasi - Bandixon markaz", "lat": 37.8625, "lng": 67.3855, "type": "traffic_light", "speed": 60, "road": "Bandixon markaziy chorrahasi", "dist": 450},
    {"id": "uz-sur-ban-005", "name": "YPX Patrul 360 - Bandixon aylanmasi", "lat": 37.8480, "lng": 67.3910, "type": "patrul_360", "speed": 60, "road": "Bandixon kirish aylanma yo'li", "dist": 500},
    {"id": "uz-sur-ban-006", "name": "Kamera orqadan oladi! - Bandixon - Jarqo'rg'on yo'li", "lat": 37.8550, "lng": 67.4120, "type": "rear", "speed": 60, "road": "4R105 Jarqo'rg'on yo'li (Orqadan)", "dist": 500},
    # Termiz
    {"id": "uz-sur-ter-001", "name": "Lochin 60 - At-Termiziy shoh ko'chasi", "lat": 37.2350, "lng": 67.2800, "type": "lochin", "speed": 60, "road": "At-Termiziy ko'chasi (Termiz)", "dist": 500},
    {"id": "uz-sur-ter-002", "name": "Lochin 100 - M39 Termiz kirish trassasi", "lat": 37.2850, "lng": 67.3150, "type": "lochin", "speed": 100, "road": "M39 Termiz aylanma xalqaro yo'li", "dist": 850},
    {"id": "uz-sur-ter-003", "name": "YPX Patrul 360 - Termiz xalqaro porti (Ayritom)", "lat": 37.2150, "lng": 67.3100, "type": "patrul_360", "speed": 60, "road": "Ayritom chegara bojxona yo'li", "dist": 500},
    # Boysun
    {"id": "uz-sur-boy-001", "name": "Lochin 70 - Boysun kirish posti", "lat": 38.2050, "lng": 67.2050, "type": "lochin", "speed": 70, "road": "M39 Darband - Boysun trassasi", "dist": 650},
    {"id": "uz-sur-boy-002", "name": "Ko'chma Uch oyoq 70 - Sayrob archasi trassasi", "lat": 38.0150, "lng": 67.1450, "type": "uch_oyoq", "speed": 70, "road": "M39 Sayrob dovoni (Pistirma)", "dist": 650},
    # Denov
    {"id": "uz-sur-den-001", "name": "Lochin 60 - Denov Sh. Rashidov shoh ko'chasi", "lat": 38.2750, "lng": 67.8950, "type": "lochin", "speed": 60, "road": "Denov shahar markazi", "dist": 500},
    {"id": "uz-sur-den-002", "name": "Chorraha kamerasi - Denov Buyuk Ipak Yo'li", "lat": 38.2820, "lng": 67.8820, "type": "traffic_light", "speed": 60, "road": "Denov markaziy aylanmasi", "dist": 450},
    # Qumqo'rg'on
    {"id": "uz-sur-kum-001", "name": "Lochin 70 - Qumqo'rg'on M41 trassasi", "lat": 37.8150, "lng": 67.5850, "type": "lochin", "speed": 70, "road": "M41 Termiz - Denov yo'li (Qumqo'rg'on)", "dist": 650},
    # Jarqo'rg'on
    {"id": "uz-sur-jar-001", "name": "Lochin 70 - Jarqo'rg'on aylanma yo'li", "lat": 37.5050, "lng": 67.4150, "type": "lochin", "speed": 70, "road": "M41 Jarqo'rg'on Surxon daryosi ko'prigi", "dist": 650},
    # Sho'rchi
    {"id": "uz-sur-sho-001", "name": "Lochin 60 - Sho'rchi markaziy ko'chasi", "lat": 38.0120, "lng": 67.7850, "type": "lochin", "speed": 60, "road": "M41 Sho'rchi shahar markazi", "dist": 500},
    # Sariosiyo & Uzun
    {"id": "uz-sur-sar-001", "name": "Lochin 60 - Sariosiyo markazi", "lat": 38.4120, "lng": 67.9450, "type": "lochin", "speed": 60, "road": "Sariosiyo - Tojikiston yo'li", "dist": 500},
    {"id": "uz-sur-uzu-001", "name": "Lochin 70 - Uzun tumani M41 yo'li", "lat": 38.3550, "lng": 67.9250, "type": "lochin", "speed": 70, "road": "M41 Uzun tuman trassasi", "dist": 600},
    # Oltinsoy
    {"id": "uz-sur-olt-001", "name": "Lochin 60 - Oltinsoy (Qarluq) markazi", "lat": 38.1850, "lng": 67.6850, "type": "lochin", "speed": 60, "road": "Oltinsoy markaziy yo'li", "dist": 500},
    # Sherobod
    {"id": "uz-sur-she-001", "name": "Lochin 70 - Sherobod M39 xalqaro trassasi", "lat": 37.6720, "lng": 67.0120, "type": "lochin", "speed": 70, "road": "M39 Sherobod aylanma yo'li", "dist": 700},
    # Angor & Muzrabot
    {"id": "uz-sur-ang-001", "name": "Lochin 70 - Angor tuman markazi M39 yo'li", "lat": 37.4720, "lng": 67.1450, "type": "lochin", "speed": 70, "road": "M39 Angor yo'nalishi", "dist": 600},
    {"id": "uz-sur-muz-001", "name": "Lochin 70 - Muzrabot (Xalqobod) markazi", "lat": 37.3550, "lng": 66.8850, "type": "lochin", "speed": 70, "road": "Muzrabot tumanlararo trassasi", "dist": 600},
    # Qiziriq
    {"id": "uz-sur-qiz-001", "name": "Lochin 60 - Qiziriq (Sariq) markaziy ko'chasi", "lat": 37.6580, "lng": 67.2850, "type": "lochin", "speed": 60, "road": "4R100 Qiziriq shahar markazi", "dist": 500},

    # =========================================================================
    # 2. QASHQADARYO VILOYATI (Barcha tumanlar)
    # =========================================================================
    {"id": "uz-qar-001", "name": "Lochin 60 - Qarshi O'zbekiston shoh ko'chasi", "lat": 38.8550, "lng": 65.7950, "type": "lochin", "speed": 60, "road": "O'zbekiston shoh ko'chasi (Qarshi)", "dist": 500},
    {"id": "uz-qar-002", "name": "Lochin 100 - Qarshi - Shahrisabz yo'li", "lat": 38.8900, "lng": 65.8850, "type": "lochin", "speed": 100, "road": "A378 Shahrisabz yo'nalishi", "dist": 850},
    {"id": "uz-qar-003", "name": "Chorraha kamerasi - Qarshi Islom Karimov va Nasaf", "lat": 38.8650, "lng": 65.7820, "type": "traffic_light", "speed": 60, "road": "Islom Karimov shoh ko'chasi", "dist": 450},
    # Shahrisabz
    {"id": "uz-qar-sha-001", "name": "Lochin 60 - Shahrisabz Ipak Yo'li ko'chasi", "lat": 39.0550, "lng": 66.8350, "type": "lochin", "speed": 60, "road": "Shahrisabz shahar markazi (Oqsaroy)", "dist": 500},
    # Kitob & Taxtaqoracha dovoni
    {"id": "uz-qar-kit-001", "name": "Lochin 70 - Kitob tuman posti (M39)", "lat": 39.1250, "lng": 66.8850, "type": "lochin", "speed": 70, "road": "M39 Samarqand - Taxtaqoracha dovoni yo'li", "dist": 650},
    # Yakkabog' & Qamashi
    {"id": "uz-qar-yak-001", "name": "Lochin 60 - Yakkabog' markaziy yo'li", "lat": 38.9750, "lng": 66.6850, "type": "lochin", "speed": 60, "road": "A378 Yakkabog' tuman markazi", "dist": 500},
    {"id": "uz-qar-qam-001", "name": "Lochin 70 - Qamashi A378 trassasi", "lat": 38.8250, "lng": 66.4750, "type": "lochin", "speed": 70, "road": "A378 Qamashi aylanma yo'li", "dist": 650},
    # G'uzor & Dehqonobod
    {"id": "uz-qar-guz-001", "name": "Lochin 70 - G'uzor M39 va A380 aylanmasi", "lat": 38.6250, "lng": 66.2550, "type": "lochin", "speed": 70, "road": "M39 G'uzor xalqaro chorrahasi", "dist": 700},
    {"id": "uz-qar-deh-001", "name": "Lochin 70 - Dehqonobod (Karashina) posti", "lat": 38.3450, "lng": 66.4950, "type": "lochin", "speed": 70, "road": "M39 Surxondaryo - Termiz yo'li (Oqrabot)", "dist": 700},
    # Koson & Muborak
    {"id": "uz-qar-kos-001", "name": "Lochin 70 - Koson A380 Buxoro trassasi", "lat": 39.0350, "lng": 65.5850, "type": "lochin", "speed": 70, "road": "A380 Koson aylanma yo'li", "dist": 700},
    {"id": "uz-qar-mub-001", "name": "Lochin 70 - Muborak gaz sanoati trassasi", "lat": 39.2650, "lng": 65.1550, "type": "lochin", "speed": 70, "road": "A380 Muborak magistrali", "dist": 700},
    # Chiroqchi & Ko'kdala
    {"id": "uz-qar-chi-001", "name": "Lochin 60 - Chiroqchi markazi", "lat": 39.0250, "lng": 66.5750, "type": "lochin", "speed": 60, "road": "Chiroqchi shahar markaziy yo'li", "dist": 500},
    {"id": "uz-qar-kok-001", "name": "Ko'chma Uch oyoq 70 - Ko'kdala (Yettitom) aylanmasi", "lat": 38.9850, "lng": 66.1250, "type": "uch_oyoq", "speed": 70, "road": "A378 Yettitom chorrahasi (Pistirma)", "dist": 650},
    # Kasbi & Nishon
    {"id": "uz-qar-kas-001", "name": "Lochin 60 - Kasbi (Mug'lon) markazi", "lat": 38.7450, "lng": 65.5550, "type": "lochin", "speed": 60, "road": "Kasbi tumanlararo yo'li", "dist": 500},
    {"id": "uz-qar-nis-001", "name": "Lochin 60 - Yangi Nishon markazi", "lat": 38.6550, "lng": 65.6850, "type": "lochin", "speed": 60, "road": "Nishon shahar markazi", "dist": 500},

    # =========================================================================
    # 3. SAMARQAND VILOYATI (Shahar va Barcha tumanlar)
    # =========================================================================
    {"id": "uz-sam-001", "name": "Lochin 60 - Registon ko'chasi", "lat": 39.6548, "lng": 66.9752, "type": "lochin", "speed": 60, "road": "Registon ko'chasi (Samarqand)", "dist": 500},
    {"id": "uz-sam-002", "name": "Chorraha kamerasi - Rudakiy va Gagarin", "lat": 39.6580, "lng": 66.9550, "type": "traffic_light", "speed": 60, "road": "Rudakiy va Gagarin chorrahasi", "dist": 450},
    {"id": "uz-sam-003", "name": "Kamera orqadan oladi! - Beruniy ko'chasi", "lat": 39.6640, "lng": 66.9420, "type": "rear", "speed": 60, "road": "Beruniy ko'chasi (Orqadan uradi)", "dist": 500},
    {"id": "uz-sam-004", "name": "Lochin 60 - Spitamen shoh ko'chasi", "lat": 39.6450, "lng": 66.9380, "type": "lochin", "speed": 60, "road": "Spitamen shoh ko'chasi", "dist": 550},
    {"id": "uz-sam-005", "name": "Chorraha kamerasi - Dahbed va Registon", "lat": 39.6610, "lng": 66.9790, "type": "traffic_light", "speed": 60, "road": "Dahbed ko'chasi chorrahasi", "dist": 450},
    {"id": "uz-sam-006", "name": "Ko'chma Uch oyoq 70 - Ulug'bek rasadxonasi", "lat": 39.6740, "lng": 66.9950, "type": "uch_oyoq", "speed": 70, "road": "M39 Toshkent yo'nalishi (Pistirma)", "dist": 650},
    {"id": "uz-sam-007", "name": "Lochin 70 - Samarqand Katta halqa yo'li", "lat": 39.6850, "lng": 66.9250, "type": "lochin", "speed": 70, "road": "Samarqand aylanma halqa yo'li", "dist": 650},
    {"id": "uz-sam-008", "name": "YPX Patrul 360 - Samarqand Vokzal maydoni", "lat": 39.6680, "lng": 66.9280, "type": "patrul_360", "speed": 60, "road": "Temiryo'l vokzali atrofi", "dist": 500},
    {"id": "uz-sam-009", "name": "Lochin 100 - M39 Samarqand - Jizzax trassasi", "lat": 39.7250, "lng": 67.0450, "type": "lochin", "speed": 100, "road": "M39 Xalqaro trassa (Bulung'ur)", "dist": 850},
    {"id": "uz-sam-010", "name": "Lochin 100 - M37 Samarqand - Navoiy trassasi", "lat": 39.6950, "lng": 66.8250, "type": "lochin", "speed": 100, "road": "M37 Kattaqo'rg'on yo'nalishi", "dist": 850},
    # Tumanlar: Urgut, Kattaqo'rg'on, Pastdarg'om, Jomboy, Ishtixon, Oqdaryo, Payariq, Toyloq, Narpay
    {"id": "uz-sam-urg-001", "name": "Lochin 60 - Urgut shahar Pochvon ko'chasi", "lat": 39.4050, "lng": 67.2450, "type": "lochin", "speed": 60, "road": "Urgut markaziy bozor yo'li", "dist": 500},
    {"id": "uz-sam-kat-001", "name": "Lochin 60 - Kattaqo'rg'on Amir Temur ko'chasi", "lat": 39.8950, "lng": 66.2550, "type": "lochin", "speed": 60, "road": "Kattaqo'rg'on shahar markazi", "dist": 500},
    {"id": "uz-sam-kat-002", "name": "Lochin 100 - M37 Kattaqo'rg'on aylanmasi", "lat": 39.9250, "lng": 66.2850, "type": "lochin", "speed": 100, "road": "M37 Xalqaro trassa", "dist": 850},
    {"id": "uz-sam-pas-001", "name": "Lochin 60 - Pastdarg'om (Juma sh.) markazi", "lat": 39.7150, "lng": 66.6550, "type": "lochin", "speed": 60, "road": "Juma shahar markaziy yo'li", "dist": 500},
    {"id": "uz-sam-jom-001", "name": "Lochin 70 - Jomboy M39 trassasi", "lat": 39.7020, "lng": 67.0950, "type": "lochin", "speed": 70, "road": "M39 Jomboy aylanma yo'li", "dist": 650},
    {"id": "uz-sam-ish-001", "name": "Lochin 70 - Ishtixon M37 yo'li", "lat": 39.9650, "lng": 66.4850, "type": "lochin", "speed": 70, "road": "M37 Ishtixon aylanmasi", "dist": 650},
    {"id": "uz-sam-oqd-001", "name": "Lochin 70 - Oqdaryo (Loyish) M37 yo'li", "lat": 39.7850, "lng": 66.7250, "type": "lochin", "speed": 70, "road": "M37 Loyish aylanma yo'li", "dist": 650},
    {"id": "uz-sam-pay-001", "name": "Lochin 60 - Payariq (Chelak sh.) markazi", "lat": 39.9250, "lng": 66.8550, "type": "lochin", "speed": 60, "road": "Chelak markaziy yo'li", "dist": 500},
    {"id": "uz-sam-toy-001", "name": "Lochin 60 - Toyloq markaziy yo'li", "lat": 39.5850, "lng": 67.0850, "type": "lochin", "speed": 60, "road": "Samarqand - Urgut trassasi (Toyloq)", "dist": 500},
    {"id": "uz-sam-nar-001", "name": "Lochin 70 - Narpay (Oqtosh sh.) M37 yo'li", "lat": 40.0450, "lng": 65.9350, "type": "lochin", "speed": 70, "road": "M37 Oqtosh magistrali", "dist": 650},
    {"id": "uz-sam-pax-001", "name": "Lochin 70 - Paxtachi (Ziyovuddin) posti", "lat": 40.0350, "lng": 65.6550, "type": "lochin", "speed": 70, "road": "M37 Navoiy viloyat chegarasi", "dist": 650},

    # =========================================================================
    # 4. BUXORO VILOYATI (Shahar va Barcha tumanlar)
    # =========================================================================
    {"id": "uz-bux-001", "name": "Lochin 60 - B. Naqshband ko'chasi", "lat": 39.7745, "lng": 64.4280, "type": "lochin", "speed": 60, "road": "Bahouddin Naqshband ko'chasi (Buxoro)", "dist": 500},
    {"id": "uz-bux-002", "name": "Lochin 60 - I. Somoniy ko'chasi", "lat": 39.7680, "lng": 64.4150, "type": "lochin", "speed": 60, "road": "Ismoil Somoniy ko'chasi", "dist": 500},
    {"id": "uz-bux-003", "name": "Chorraha kamerasi - Navoiy va Naqshband", "lat": 39.7720, "lng": 64.4350, "type": "traffic_light", "speed": 60, "road": "Markaziy chorraha", "dist": 450},
    {"id": "uz-bux-004", "name": "Lochin 100 - M37 Buxoro - Navoiy trassasi", "lat": 39.8100, "lng": 64.5200, "type": "lochin", "speed": 100, "road": "M37 Katta trassa", "dist": 850},
    {"id": "uz-bux-005", "name": "Uch oyoq 70 - Buxoro aylanma yo'li", "lat": 39.7500, "lng": 64.4600, "type": "uch_oyoq", "speed": 70, "road": "A380 yo'nalishi", "dist": 650},
    # Tumanlar: G'ijduvon, Kogon, Vobkent, Shofirkon, Romitan, Jondor, Qorako'l, Olot, Qorovulbozor
    {"id": "uz-bux-gij-001", "name": "Lochin 60 - G'ijduvon Yusuf Hamadoniy ko'chasi", "lat": 40.1020, "lng": 64.6750, "type": "lochin", "speed": 60, "road": "M37 G'ijduvon markaziy trassasi", "dist": 500},
    {"id": "uz-bux-kog-001", "name": "Lochin 60 - Kogon temiryo'l vokzali yo'li", "lat": 39.7250, "lng": 64.5450, "type": "lochin", "speed": 60, "road": "Buxoro - Kogon trassasi", "dist": 500},
    {"id": "uz-bux-vob-001", "name": "Lochin 70 - Vobkent M37 aylanmasi", "lat": 39.9550, "lng": 64.5150, "type": "lochin", "speed": 70, "road": "M37 Vobkent xalqaro yo'li", "dist": 650},
    {"id": "uz-bux-sho-001", "name": "Lochin 60 - Shofirkon tuman markazi", "lat": 40.1250, "lng": 64.5050, "type": "lochin", "speed": 60, "road": "Shofirkon markaziy shoh ko'chasi", "dist": 500},
    {"id": "uz-bux-rom-001", "name": "Lochin 70 - Romitan A380 Gazli yo'li", "lat": 39.9350, "lng": 64.3850, "type": "lochin", "speed": 70, "road": "A380 Xorazm yo'nalishi (Romitan)", "dist": 650},
    {"id": "uz-bux-jon-001", "name": "Lochin 70 - Jondor M37 magistrali", "lat": 39.7350, "lng": 64.1850, "type": "lochin", "speed": 70, "road": "M37 Turkmaniston trassasi (Jondor)", "dist": 650},
    {"id": "uz-bux-qor-001", "name": "Lochin 60 - Qorako'l shahar markazi", "lat": 39.5050, "lng": 63.8550, "type": "lochin", "speed": 60, "road": "Qorako'l shahar magistrali", "dist": 500},
    {"id": "uz-bux-olo-001", "name": "Lochin 70 - Olot chegara posti (Farob)", "lat": 39.4150, "lng": 63.8050, "type": "lochin", "speed": 70, "road": "M37 Olot xalqaro bojxona yo'li", "dist": 700},
    {"id": "uz-bux-qrv-001", "name": "Lochin 70 - Qorovulbozor neft zavodi yo'li", "lat": 39.5020, "lng": 64.7950, "type": "lochin", "speed": 70, "road": "A380 Qarshi yo'nalishi (Qorovulbozor)", "dist": 650},

    # =========================================================================
    # 5. TOSHKENT SHAHRI VA VILOYATI (Barcha tumanlar)
    # =========================================================================
    {"id": "uz-tas-001", "name": "Lochin 60 - Amir Temur shoh ko'chasi", "lat": 41.3150, "lng": 69.2820, "type": "lochin", "speed": 60, "road": "Amir Temur shoh ko'chasi (Toshkent)", "dist": 500},
    {"id": "uz-tas-002", "name": "Lochin 60 - Mustaqillik shoh ko'chasi", "lat": 41.3220, "lng": 69.2950, "type": "lochin", "speed": 60, "road": "Mustaqillik shoh ko'chasi", "dist": 500},
    {"id": "uz-tas-003", "name": "Chorraha kamerasi - Buyuk Ipak Yo'li", "lat": 41.3280, "lng": 69.3350, "type": "traffic_light", "speed": 60, "road": "Buyuk Ipak Yo'li metro atrofi", "dist": 450},
    {"id": "uz-tas-004", "name": "Kamera orqadan oladi! - Bunyodkor ko'chasi", "lat": 41.2750, "lng": 69.2150, "type": "rear", "speed": 60, "road": "Bunyodkor shoh ko'chasi (Orqadan)", "dist": 550},
    {"id": "uz-tas-005", "name": "Avtobus tasmasi - Alisher Navoiy ko'chasi", "lat": 41.3180, "lng": 69.2550, "type": "bus_lane", "speed": 60, "road": "A. Navoiy shoh ko'chasi", "dist": 400},
    {"id": "uz-tas-006", "name": "Lochin 70 - Toshkent Kichik Halqa Yo'li (TKHY)", "lat": 41.3450, "lng": 69.2650, "type": "lochin", "speed": 70, "road": "Shimoliy aylanma yo'l", "dist": 600},
    {"id": "uz-tas-007", "name": "Lochin 100 - Toshkent Katta Halqa Yo'li (THYo)", "lat": 41.2350, "lng": 69.2950, "type": "lochin", "speed": 100, "road": "Sergeli THYo aylanmasi", "dist": 800},
    {"id": "uz-tas-008", "name": "YPX Patrul 360 - Chilonzor Oqtepa maydoni", "lat": 41.2950, "lng": 69.2200, "type": "patrul_360", "speed": 60, "road": "Oqtepa aylanma yo'li", "dist": 500},
    {"id": "uz-tas-009", "name": "Lochin 100 - Yangi O'zbekiston ko'chasi", "lat": 41.3650, "lng": 69.3850, "type": "lochin", "speed": 100, "road": "Yangi O'zbekiston bog'i trassasi", "dist": 850},
    {"id": "uz-tas-010", "name": "Ko'chma Uch oyoq 70 - Rohat aylanmasi", "lat": 41.2650, "lng": 69.3550, "type": "uch_oyoq", "speed": 70, "road": "Ohangaron yo'li (Pistirma)", "dist": 650},
    # Toshkent viloyati tumanlari: Chirchiq, Bo'stonliq (Chorvoq), Angren, Olmaliq, Yangiyo'l, Chinoz, Bekobod, Nurafshon, Parkent
    {"id": "uz-tvo-chi-001", "name": "Lochin 60 - Chirchiq shahar A. Navoiy ko'chasi", "lat": 41.4680, "lng": 69.5850, "type": "lochin", "speed": 60, "road": "Chirchiq shahar markazi", "dist": 500},
    {"id": "uz-tvo-bos-001", "name": "Lochin 70 - Bo'stonliq (G'azalkent - Chorvoq) yo'li", "lat": 41.5650, "lng": 69.7750, "type": "lochin", "speed": 70, "road": "Chorvoq suv ombori trassasi", "dist": 650},
    {"id": "uz-tvo-ang-001", "name": "Lochin 70 - Angren sh. A373 Qamchiq dovoni posti", "lat": 41.0150, "lng": 70.1450, "type": "lochin", "speed": 70, "road": "A373 Qamchiq dovoni kirish yo'li", "dist": 700},
    {"id": "uz-tvo-olm-001", "name": "Lochin 60 - Olmaliq Metallurglar shoh ko'chasi", "lat": 40.8450, "lng": 69.6050, "type": "lochin", "speed": 60, "road": "Olmaliq markaziy shoh ko'chasi", "dist": 500},
    {"id": "uz-tvo-yan-001", "name": "Lochin 70 - Yangiyo'l M39 Samarqand trassasi", "lat": 41.1150, "lng": 69.0450, "type": "lochin", "speed": 70, "road": "M39 Yangiyo'l aylanmasi", "dist": 650},
    {"id": "uz-tvo-chn-001", "name": "Lochin 70 - Chinoz ko'prigi M39 posti", "lat": 40.9350, "lng": 68.7550, "type": "lochin", "speed": 70, "road": "M39 Sirdaryo daryosi ko'prigi (Chinoz)", "dist": 700},
    {"id": "uz-tvo-bek-001", "name": "Lochin 60 - Bekobod shahar markazi", "lat": 40.2150, "lng": 69.2550, "type": "lochin", "speed": 60, "road": "Bekobod markaziy magistrali", "dist": 500},
    {"id": "uz-tvo-nur-001", "name": "Lochin 60 - Nurafshon (To'ytepa) markazi", "lat": 41.0450, "lng": 69.3550, "type": "lochin", "speed": 60, "road": "Toshkent viloyati ma'muriy markazi", "dist": 500},
    {"id": "uz-tvo-par-001", "name": "Lochin 60 - Parkent markaziy yo'li", "lat": 41.2950, "lng": 69.6750, "type": "lochin", "speed": 60, "road": "Parkent - So'qoq tog' yo'li", "dist": 500},
    {"id": "uz-tvo-zan-001", "name": "Lochin 60 - Zangiota (Eshonguzar) yo'li", "lat": 41.2450, "lng": 69.1550, "type": "lochin", "speed": 60, "road": "Zangiota ziyoratgohi atrofi", "dist": 500},

    # =========================================================================
    # 6. FARG'ONA VODIYSI (Farg'ona, Andijon, Namangan barcha tumanlar)
    # =========================================================================
    # Farg'ona
    {"id": "uz-fer-001", "name": "Lochin 60 - Al-Farg'oniy ko'chasi", "lat": 40.3850, "lng": 71.7850, "type": "lochin", "speed": 60, "road": "Farg'ona markaziy xiyoboni", "dist": 500},
    {"id": "uz-fer-002", "name": "Lochin 70 - Farg'ona - Marg'ilon yo'li", "lat": 40.4200, "lng": 71.7450, "type": "lochin", "speed": 70, "road": "Marg'ilon shoh ko'chasi", "dist": 600},
    {"id": "uz-fer-003", "name": "Lochin 100 - Qo'qon aylanma trassasi", "lat": 40.5400, "lng": 70.9500, "type": "lochin", "speed": 100, "road": "A373 Qo'qon aylanmasi", "dist": 850},
    {"id": "uz-fer-mar-001", "name": "Lochin 60 - Marg'ilon B. Marg'iloniy ko'chasi", "lat": 40.4720, "lng": 71.7150, "type": "lochin", "speed": 60, "road": "Marg'ilon shahar markazi", "dist": 500},
    {"id": "uz-fer-quv-001", "name": "Lochin 60 - Quva tuman markazi", "lat": 40.5250, "lng": 72.0650, "type": "lochin", "speed": 60, "road": "Quva - Andijon yo'li", "dist": 500},
    {"id": "uz-fer-olt-001", "name": "Lochin 60 - Oltiariq markazi", "lat": 40.3950, "lng": 71.4850, "type": "lochin", "speed": 60, "road": "Oltiariq uzumchilik markazi", "dist": 500},
    {"id": "uz-fer-ris-001", "name": "Lochin 60 - Rishton kulolchilik markazi", "lat": 40.3550, "lng": 71.2850, "type": "lochin", "speed": 60, "road": "A373 Rishton aylanmasi", "dist": 500},
    {"id": "uz-fer-bes-001", "name": "Lochin 70 - Beshariq chegara yo'li", "lat": 40.4350, "lng": 70.6150, "type": "lochin", "speed": 70, "road": "Beshariq - Konibodom yo'nalishi", "dist": 650},
    # Andijon
    {"id": "uz-and-001", "name": "Lochin 60 - Bobur shoh ko'chasi", "lat": 40.7850, "lng": 72.3450, "type": "lochin", "speed": 60, "road": "Andijon shahar markazi", "dist": 500},
    {"id": "uz-and-002", "name": "Chorraha kamerasi - Amir Temur va Bobur", "lat": 40.7720, "lng": 72.3550, "type": "traffic_light", "speed": 60, "road": "Markaziy chorraha (Andijon)", "dist": 450},
    {"id": "uz-and-003", "name": "Lochin 100 - A373 Andijon - Asaka trassasi", "lat": 40.7150, "lng": 72.3100, "type": "lochin", "speed": 100, "road": "A373 Asaka yo'nalishi", "dist": 850},
    {"id": "uz-and-asa-001", "name": "Lochin 60 - Asaka GM zavodi yo'li", "lat": 40.6420, "lng": 72.2450, "type": "lochin", "speed": 60, "road": "Asaka avtomobil zavodi trassasi", "dist": 500},
    {"id": "uz-and-sha-001", "name": "Lochin 60 - Shahrixon shahar markazi", "lat": 40.7120, "lng": 72.0550, "type": "lochin", "speed": 60, "road": "Shahrixon - Farg'ona yo'li", "dist": 500},
    {"id": "uz-and-xoj-001", "name": "Lochin 70 - Xo'jaobod Do'stlik posti", "lat": 40.6650, "lng": 72.5650, "type": "lochin", "speed": 70, "road": "O'sh - Qirg'iziston chegara trassasi", "dist": 650},
    {"id": "uz-and-xon-001", "name": "Lochin 60 - Xonobod shahar kirish yo'li", "lat": 40.8050, "lng": 72.9850, "type": "lochin", "speed": 60, "road": "Xonobod sanatoriy magistrali", "dist": 500},
    {"id": "uz-and-bal-001", "name": "Lochin 70 - Baliqchi Namangan chegarasi", "lat": 40.9350, "lng": 71.9150, "type": "lochin", "speed": 70, "road": "Baliqchi - Namangan daryo ko'prigi", "dist": 650},
    # Namangan
    {"id": "uz-nam-001", "name": "Lochin 60 - Navoiy ko'chasi", "lat": 41.0020, "lng": 71.6750, "type": "lochin", "speed": 60, "road": "Namangan shahar markazi", "dist": 500},
    {"id": "uz-nam-002", "name": "Lochin 100 - Namangan - Pop trassasi", "lat": 41.0250, "lng": 71.5150, "type": "lochin", "speed": 100, "road": "Qamchiq dovoni yo'nalishi", "dist": 850},
    {"id": "uz-nam-pop-001", "name": "Lochin 70 - Pop tumani A373 trassasi", "lat": 40.8750, "lng": 71.1050, "type": "lochin", "speed": 70, "road": "A373 Qamchiq dovoni etagi", "dist": 700},
    {"id": "uz-nam-chu-001", "name": "Lochin 60 - Chust shahar markazi", "lat": 41.0050, "lng": 71.2250, "type": "lochin", "speed": 60, "road": "Chust pichoqchilar shoh ko'chasi", "dist": 500},
    {"id": "uz-nam-tor-001", "name": "Lochin 70 - To'raqo'rg'on IES trassasi", "lat": 41.0150, "lng": 71.5550, "type": "lochin", "speed": 70, "road": "To'raqo'rg'on issiqlik elektr stansiyasi yo'li", "dist": 650},
    {"id": "uz-nam-cho-001", "name": "Lochin 60 - Chortoq sanatoriy yo'li", "lat": 41.0750, "lng": 71.8150, "type": "lochin", "speed": 60, "road": "Chortoq dam olish maskani trassasi", "dist": 500},
    {"id": "uz-nam-uch-001", "name": "Lochin 70 - Uchqo'rg'on Norin ko'prigi", "lat": 41.1150, "lng": 72.0750, "type": "lochin", "speed": 70, "road": "Uchqo'rg'on daryo magistrali", "dist": 650},

    # =========================================================================
    # 7. JIZZAX VA SIRDARYO VILOYATLARI (Barcha tumanlar)
    # =========================================================================
    # Jizzax
    {"id": "uz-jiz-001", "name": "Lochin 60 - Sh. Rashidov shoh ko'chasi", "lat": 40.1250, "lng": 67.8420, "type": "lochin", "speed": 60, "road": "Jizzax markaziy ko'chasi", "dist": 500},
    {"id": "uz-jiz-002", "name": "Lochin 100 - M39 Jizzax aylanma trassasi", "lat": 40.1650, "lng": 67.8950, "type": "lochin", "speed": 100, "road": "M39 Jizzax aylanmasi", "dist": 850},
    {"id": "uz-jiz-gal-001", "name": "Lochin 70 - G'allaorol Sanzar dovoni (M39)", "lat": 40.0250, "lng": 67.5950, "type": "lochin", "speed": 70, "road": "M39 Ilonuti darasi (Pistirma)", "dist": 700},
    {"id": "uz-jiz-zom-001", "name": "Lochin 60 - Zomin markaziy yo'li", "lat": 39.9650, "lng": 68.3950, "type": "lochin", "speed": 60, "road": "Zomin milliy bog'i tog' yo'li", "dist": 500},
    {"id": "uz-jiz-das-001", "name": "Lochin 70 - Dashtobod M39 trassasi", "lat": 40.1550, "lng": 68.3450, "type": "lochin", "speed": 70, "road": "M39 Sirdaryo - Jizzax yo'li", "dist": 650},
    {"id": "uz-jiz-pax-001", "name": "Lochin 60 - Paxtakor tuman markazi", "lat": 40.3150, "lng": 67.9550, "type": "lochin", "speed": 60, "road": "Paxtakor magistrali", "dist": 500},
    {"id": "uz-jiz-dos-001", "name": "Lochin 60 - Do'stlik shahar markazi", "lat": 40.5250, "lng": 68.0350, "type": "lochin", "speed": 60, "road": "Do'stlik tumanlararo yo'li", "dist": 500},
    # Sirdaryo
    {"id": "uz-sir-001", "name": "Lochin 60 - Guliston shoh ko'chasi", "lat": 40.4950, "lng": 68.7850, "type": "lochin", "speed": 60, "road": "Guliston shahar markazi", "dist": 500},
    {"id": "uz-sir-002", "name": "Lochin 100 - M34 Toshkent - Guliston trassasi", "lat": 40.5400, "lng": 68.7600, "type": "lochin", "speed": 100, "road": "M34 trassa (Baxt sh.)", "dist": 850},
    {"id": "uz-sir-yan-001", "name": "Lochin 60 - Yangiyer shahar markazi (M34)", "lat": 40.2750, "lng": 68.8150, "type": "lochin", "speed": 60, "road": "M34 Yangiyer xalqaro trassasi", "dist": 500},
    {"id": "uz-sir-sar-001", "name": "Lochin 70 - Sardoba M39 aylanmasi", "lat": 40.2150, "lng": 68.1750, "type": "lochin", "speed": 70, "road": "M39 Sardoba suv ombori yo'li", "dist": 650},
    {"id": "uz-sir-srd-001", "name": "Lochin 70 - Sirdaryo shahar M34 va M39 chorrahasi", "lat": 40.8450, "lng": 68.6650, "type": "lochin", "speed": 70, "road": "Sirdaryo xalqaro aylanma yo'li", "dist": 650},
    {"id": "uz-sir-xov-001", "name": "Lochin 60 - Xovos temiryo'l magistrali", "lat": 40.1950, "lng": 68.8650, "type": "lochin", "speed": 60, "road": "Xovos - Tojikiston chegara yo'li", "dist": 500},

    # =========================================================================
    # 8. NAVOIY VILOYATI (Shahar va Barcha tumanlar)
    # =========================================================================
    {"id": "uz-nav-001", "name": "Lochin 60 - G'alaba shoh ko'chasi", "lat": 40.0980, "lng": 65.3750, "type": "lochin", "speed": 60, "road": "Navoiy shahar markazi", "dist": 500},
    {"id": "uz-nav-002", "name": "Lochin 100 - M37 Navoiy - Karmana trassasi", "lat": 40.1450, "lng": 65.3550, "type": "lochin", "speed": 100, "road": "M37 Karmana aylanmasi", "dist": 850},
    {"id": "uz-nav-qiz-001", "name": "Lochin 70 - Qiziltepa markazi", "lat": 40.0350, "lng": 64.9850, "type": "lochin", "speed": 70, "road": "Navoiy - Buxoro yo'li (Qiziltepa)", "dist": 600},
    {"id": "uz-nav-xat-001", "name": "Lochin 60 - Xatirchi (Yangirabot) markazi", "lat": 40.0250, "lng": 65.9550, "type": "lochin", "speed": 60, "road": "Xatirchi tumanlararo yo'li", "dist": 500},
    {"id": "uz-nav-nur-001", "name": "Lochin 60 - Nurota Chashma ziyoratgohi yo'li", "lat": 40.5650, "lng": 65.6850, "type": "lochin", "speed": 60, "road": "Nurota shahar markazi", "dist": 500},
    {"id": "uz-nav-zar-001", "name": "Lochin 70 - Zarafshon A380 Qizilqum trassasi", "lat": 41.5750, "lng": 64.2050, "type": "lochin", "speed": 70, "road": "A380 Zarafshon oltin koni yo'li", "dist": 700},
    {"id": "uz-nav-uch-001", "name": "Lochin 70 - Uchquduq A380 shimoliy trassasi", "lat": 42.1550, "lng": 63.5550, "type": "lochin", "speed": 70, "road": "A380 Uchquduq - Nukus yo'li", "dist": 700},

    # =========================================================================
    # 9. XORAZM VILOYATI VA QORAQALPOG'ISTON (Barcha tumanlar)
    # =========================================================================
    # Xorazm
    {"id": "uz-xva-001", "name": "Lochin 60 - Al-Xorazmiy shoh ko'chasi", "lat": 41.5550, "lng": 60.6250, "type": "lochin", "speed": 60, "road": "Urganch markazi", "dist": 500},
    {"id": "uz-xva-002", "name": "Lochin 60 - Xiva Ichan Qal'a kirish yo'li", "lat": 41.3780, "lng": 60.3650, "type": "lochin", "speed": 60, "road": "Urganch - Xiva trassasi", "dist": 500},
    {"id": "uz-xva-xon-001", "name": "Lochin 60 - Xonqa tuman markazi", "lat": 41.4750, "lng": 60.7750, "type": "lochin", "speed": 60, "road": "Xonqa shahar magistrali", "dist": 500},
    {"id": "uz-xva-haz-001", "name": "Lochin 70 - Hazorasp A380 Buxoro yo'li", "lat": 41.3150, "lng": 61.0750, "type": "lochin", "speed": 70, "road": "A380 Hazorasp aylanmasi", "dist": 650},
    {"id": "uz-xva-gur-001", "name": "Lochin 70 - Gurlan Amudaryo ko'prigi", "lat": 41.8450, "lng": 60.3950, "type": "lochin", "speed": 70, "road": "Gurlan - Mang'it ko'prigi", "dist": 650},
    {"id": "uz-xva-sho-001", "name": "Lochin 60 - Shovot chegara posti", "lat": 41.6550, "lng": 60.3050, "type": "lochin", "speed": 60, "road": "Turkmaniston Toshhovuz yo'li", "dist": 500},
    {"id": "uz-xva-qos-001", "name": "Lochin 60 - Qo'shko'pir markazi", "lat": 41.5350, "lng": 60.3450, "type": "lochin", "speed": 60, "road": "Qo'shko'pir shahar yo'li", "dist": 500},
    {"id": "uz-xva-tup-001", "name": "Lochin 70 - Tuproqqal'a (Pitnak) A380 trassasi", "lat": 41.2250, "lng": 61.3150, "type": "lochin", "speed": 70, "road": "Pitnak GM motor zavodi trassasi", "dist": 650},
    # Qoraqalpog'iston
    {"id": "uz-qr-001", "name": "Lochin 60 - Berdaq shoh ko'chasi", "lat": 42.4650, "lng": 59.6150, "type": "lochin", "speed": 60, "road": "Nukus shahar markazi", "dist": 500},
    {"id": "uz-qr-002", "name": "Lochin 100 - A380 Nukus - To'rtko'l trassasi", "lat": 42.3850, "lng": 59.7200, "type": "lochin", "speed": 100, "road": "A380 trassasi", "dist": 850},
    {"id": "uz-qr-tur-001", "name": "Lochin 60 - To'rtko'l shahar A380 aylanmasi", "lat": 41.5550, "lng": 60.9850, "type": "lochin", "speed": 60, "road": "A380 To'rtko'l markaziy trassasi", "dist": 500},
    {"id": "uz-qr-ber-001", "name": "Lochin 70 - Beruniy Amudaryo ko'prigi (A380)", "lat": 41.6950, "lng": 60.7550, "type": "lochin", "speed": 70, "road": "A380 Urganch - Beruniy yangi ko'prigi", "dist": 700},
    {"id": "uz-qr-xoj-001", "name": "Lochin 60 - Xo'jayli tuman markazi", "lat": 42.4050, "lng": 59.4550, "type": "lochin", "speed": 60, "road": "Nukus - Xo'jayli magistrali", "dist": 500},
    {"id": "uz-qr-qon-001", "name": "Lochin 70 - Qo'ng'irot Ustyurt Qozog'iston trassasi", "lat": 43.0450, "lng": 58.8450, "type": "lochin", "speed": 70, "road": "A380 Beyneu xalqaro yo'li", "dist": 750},
    {"id": "uz-qr-amu-001", "name": "Lochin 60 - Amudaryo (Mang'it) markazi", "lat": 42.1150, "lng": 60.0550, "type": "lochin", "speed": 60, "road": "Mang'it shahar magistrali", "dist": 500},
    {"id": "uz-qr-chi-001", "name": "Lochin 60 - Chimboy shahar markazi", "lat": 42.9450, "lng": 59.7750, "type": "lochin", "speed": 60, "road": "Chimboy markaziy yo'li", "dist": 500},
    {"id": "uz-qr-moy-001", "name": "Lochin 60 - Mo'ynoq kemalar qabristoni yo'li", "lat": 43.7650, "lng": 59.0250, "type": "lochin", "speed": 60, "road": "Mo'ynoq Orol dengizi magistrali", "dist": 500}
]

# JSON formatiga keltirish
cams_list = []
for d in districts_data:
    cams_list.append({
        "id": d["id"],
        "name": d["name"],
        "lat": round(d["lat"], 4),
        "lng": round(d["lng"], 4),
        "type": d["type"],
        "speedLimit": d["speed"],
        "azimuth": -1,
        "roadName": d["road"],
        "distanceAlertThreshold": d["dist"]
    })

# Fayllarga yozish
json_path = Path("src/data/speedcams.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(cams_list, f, ensure_ascii=False, indent=2)

print(f"Jami {len(cams_list)} ta O'zbekiston tuman va shahar kameralari muvaffaqiyatli saqlandi!")
