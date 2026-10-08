import asyncio
import os
import edge_tts

VOICE = "uz-UZ-MadinaNeural"
RATE = "+10%"  # Avtomobilda aniq va tez yetib borishi uchun
PITCH = "+0Hz"

OUTPUT_DIR = r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds"
os.makedirs(OUTPUT_DIR, exist_ok=True)

VOICE_PROMPTS = {
    # 1. Lochin kameralari
    "v_lochin_60.mp3": "Diqqat! Lochin kamerasi! Oltmish!",
    "v_lochin_70.mp3": "Diqqat! Lochin kamerasi! Yetmish!",
    "v_lochin_100.mp3": "Diqqat! Lochin kamerasi! Yuz!",
    
    # 2. Orqadan oladigan kameralar (Haydovchilar eng ko'p jarima to'laydigan holat!)
    "v_rear_60.mp3": "Diqqat! Kamera orqadan oladi! Cheklov oltmish!",
    "v_rear_70.mp3": "Diqqat! Kamera orqadan oladi! Cheklov yetmish!",
    "v_rear_100.mp3": "Diqqat! Kamera orqadan oladi! Cheklov yuz!",
    
    # 3. Uch oyoq (Trinoga / Ko'chma radar)
    "v_uchoyoq.mp3": "Diqqat! Ko‘chma uch oyoq radari!",
    "v_uchoyoq_70.mp3": "Diqqat! Ko‘chma uch oyoq radari! Cheklov yetmish!",
    "v_uchoyoq_100.mp3": "Diqqat! Ko‘chma uch oyoq radari! Cheklov yuz!",
    
    # 4. Patrul xizmati 360 radari (E-Patrul / Kiber-Patrul mashinasi)
    "v_patrul_360.mp3": "Diqqat! Yo‘l patrul xizmati mashinasi, uch yuz oltmish darajali radar!",
    
    # 5. Chorraha kamerasi (Stop-liniya va qizil chiroq)
    "v_chorraha.mp3": "Diqqat! Chorraha kamerasi! Stop-liniya va qizil chiroq nazorati!",
    
    # 6. O'rtacha tezlik koridori (AutoCon)
    "v_autocon_start.mp3": "Diqqat! O‘rtacha tezlik koridori boshlandi! Cheklov yetmish!",
    "v_autocon_end.mp3": "O‘rtacha tezlik koridori yakunlandi!",
    
    # 7. A-yo'lak (Jamoat transporti yo'lagi)
    "v_buslane.mp3": "Diqqat! Jamoat transporti, A-yo‘lak kamerasi!",
    
    # 8. Sun'iy notekislik ("Lejaщiy politseyskiy")
    "v_suniy_notekislik.mp3": "Diqqat! Oldinda sun’iy notekislik!",
    
    # 9. Tezlik oshganda shoshilinch ogohlantirish
    "v_tezlikni_tushiring.mp3": "Tezlikni tushiring! Tezlikni tushiring!",
    
    # 10. Kamera o'tib ketilganda
    "v_kamera_otildi.mp3": "Kamera ortda qoldi."
}

async def generate():
    print(f"Barcha professional ovozli fayllarni yaratish boshlandi ({VOICE})...")
    for filename, text in VOICE_PROMPTS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(filepath)
        print(f"[OK] Saqlandi: {filename} -> '{text}'")

if __name__ == "__main__":
    asyncio.run(generate())
    print("\nBARCHA O'ZBEK DIKTOR OVOZLARI MUVAFFAQIYATLI YARATILDI!")
