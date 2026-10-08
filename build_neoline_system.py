import asyncio
import os
import subprocess
import edge_tts
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
OUTPUT_DIR = r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds"
os.makedirs(OUTPUT_DIR, exist_ok=True)

VOICE = "uz-UZ-MadinaNeural"
RATE = "+3%"       # Neoline diktori kabi dadil va tushunarli
PITCH = "-2Hz"     # Neoline diktori kabi yoqimli studiya tembri

# O'zbekistondagi barcha radarlar uchun to'liq e'lonlar
VOICE_SCRIPTS = {
    # 1. Lochin kameralari (60, 70, 100)
    "lochin_60.mp3": "Lochin. Oltmish.",
    "lochin_70.mp3": "Lochin. Yetmish.",
    "lochin_100.mp3": "Lochin. Yuz.",

    # 2. Orqadan oladigan radar (В спину)
    "rear_60.mp3": "Kamera orqadan oladi. Cheklov oltmish.",
    "rear_70.mp3": "Kamera orqadan oladi. Cheklov yetmish.",
    "rear_100.mp3": "Kamera orqadan oladi. Cheklov yuz.",

    # 3. Ko'chma uch oyoq radari (Trinoga / Kordon-M)
    "uch_oyoq.mp3": "Ko‘chma uch oyoq radari.",
    "uch_oyoq_70.mp3": "Ko‘chma uch oyoq radari. Yetmish.",
    "uch_oyoq_100.mp3": "Ko‘chma uch oyoq radari. Yuz.",

    # 4. YPX Patrul xizmati 360 darajali mashina radari (E-Patrul)
    "patrul_360.mp3": "Yo‘l patrul xizmati, uch yuz oltmish darajali radar.",

    # 5. Chorraha kamerasi (Svetofor, stop-liniya va qizil chiroq)
    "chorraha.mp3": "Chorraha kamerasi. Stop-liniya va qizil chiroq nazorati.",

    # 6. AutoCon O'rtacha tezlik koridori
    "autocon_start.mp3": "O‘rtacha tezlik koridori boshlandi. Cheklov yetmish.",
    "autocon_end.mp3": "O‘rtacha tezlik koridori yakunlandi.",

    # 7. A-yo'lak (Jamoat transporti tasmasi)
    "bus_lane.mp3": "Jamoat transporti, A-yo‘lak kamerasi.",

    # 8. Sun'iy notekislik ("Lejaщiy politseyskiy")
    "speed_bump.mp3": "Oldinda sun’iy notekislik.",

    # 9. Tezlik oshganda shoshilinch xavf
    "slowdown.mp3": "Tezlikni tushiring! Tezlikni tushiring!",

    # 10. Kamera ortda qolganda
    "cleared.mp3": "Kamera ortda qoldi."
}

async def generate_and_master_voices():
    print("1. O'zbekistonning barcha radarlari uchun Neoline studiya ovozlarini yaratish...")
    for filename, text in VOICE_SCRIPTS.items():
        raw_path = os.path.join(OUTPUT_DIR, "raw_" + filename)
        final_path = os.path.join(OUTPUT_DIR, filename)
        
        # 1. Edge-TTS orqali generatsiya
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(raw_path)

        # 2. FFmpeg orqali avtomobil studiya masteringi (Loudnorm + EQ + Presence)
        # Avtomobil shovqinida aniq, baland va yoqimli eshitilishi uchun
        cmd = [
            ffmpeg_exe, "-y",
            "-i", raw_path,
            "-af", "loudnorm=I=-14:LRA=7:tp=-1.0,highpass=f=120,volume=1.3",
            final_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(raw_path):
            os.remove(raw_path)
            
        print(f" [OK] {filename} -> '{text}'")

def prepare_radar_tones():
    print("\n2. Videodagi Neoline radar detektori tovushlarini sozlash...")
    wav_video = os.path.join(OUTPUT_DIR, "neoline_full_audio.wav")
    
    # Videodagi aniq Neoline Geyger chertkisi (daraja 1, 2, 3, 4, 5)
    # A. Neoline radar lock signali
    cmd_lock = [
        ffmpeg_exe, "-y",
        "-ss", "00:00:04.35", "-to", "00:00:04.85",
        "-i", wav_video,
        "-af", "volume=2.2",
        os.path.join(OUTPUT_DIR, "neoline_chirp.wav")
    ]
    subprocess.run(cmd_lock, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # B. Videodagi haqiqiy Neoline bitta chertki (Click)
    cmd_click = [
        ffmpeg_exe, "-y",
        "-ss", "00:00:04.45", "-to", "00:00:04.68",
        "-i", wav_video,
        "-af", "volume=2.5",
        os.path.join(OUTPUT_DIR, "neoline_click.wav")
    ]
    subprocess.run(cmd_click, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(" [OK] neoline_chirp.wav va neoline_click.wav tayyorlandi!")

if __name__ == "__main__":
    asyncio.run(generate_and_master_voices())
    prepare_radar_tones()
    print("\nBARCHA OVOZ VA RADAR TOVUSHLARI TO'LIQ NEOLINE STANDARTIGA MOSLANDI!")
