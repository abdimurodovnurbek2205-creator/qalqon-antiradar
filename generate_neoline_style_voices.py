import asyncio
import os
import edge_tts

VOICE = "uz-UZ-MadinaNeural"
RATE = "+2%"       # Neoline videosidagi kabi xotirjam va aniq
PITCH = "-2Hz"     # Neoline videosidagi kabi iliq, chuqur va professional studiya tembri

OUTPUT_DIR = r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds"

VOICE_PROMPTS = {
    # Lochin tezliklari
    "v_lochin_60.mp3": "Lochin. Oltmish.",
    "v_lochin_70.mp3": "Lochin. Yetmish.",
    "v_lochin_100.mp3": "Lochin. Yuz.",
    
    # Orqadan oladigan radar
    "v_rear_60.mp3": "Kamera orqadan oladi. Oltmish.",
    "v_rear_70.mp3": "Kamera orqadan oladi. Yetmish.",
    "v_rear_100.mp3": "Kamera orqadan oladi. Yuz.",
    
    # Uch oyoq
    "v_uchoyoq.mp3": "Ko‘chma uch oyoq radari.",
    "v_uchoyoq_70.mp3": "Ko‘chma uch oyoq radari. Yetmish.",
    "v_uchoyoq_100.mp3": "Ko‘chma uch oyoq radari. Yuz.",
    
    # YPX 360 patrul
    "v_patrul_360.mp3": "Patrul xizmati, uch yuz oltmish darajali radar.",
    
    # Chorraha
    "v_chorraha.mp3": "Chorraha kamerasi. Stop-liniya va qizil chiroq.",
    
    # AutoCon
    "v_autocon_start.mp3": "O‘rtacha tezlik koridori. Yetmish.",
    "v_autocon_end.mp3": "O‘rtacha tezlik yakunlandi.",
    
    # A-yo'lak
    "v_buslane.mp3": "A-yo‘lak kamerasi.",
    
    # Sun'iy notekislik
    "v_suniy_notekislik.mp3": "Sun’iy notekislik.",
    
    # Tezlik oshganda
    "v_tezlikni_tushiring.mp3": "Tezlikni tushiring.",
    
    # O'tib ketilganda
    "v_kamera_otildi.mp3": "Kamera ortda qoldi."
}

async def generate():
    print("Neoline uslubidagi studiya ovozlarini yaratish...")
    for filename, text in VOICE_PROMPTS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(filepath)
        print(f"[OK] {filename} -> '{text}'")

if __name__ == "__main__":
    asyncio.run(generate())
    print("\nNeoline uslubidagi barcha ovozlar tayyor!")
