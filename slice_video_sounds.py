import imageio_ffmpeg
import subprocess

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
wav_path = r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds\neoline_full_audio.wav"

# 1. "Lochin" voice announcement (2.5s to 4.2s)
cmd_lochin = [
    ffmpeg_exe, "-y",
    "-ss", "00:00:02.3",
    "-to", "00:00:04.1",
    "-i", wav_path,
    "-af", "volume=2.2,highpass=f=180,lowpass=f=4800",
    r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds\real_neoline_lochin.wav"
]
subprocess.run(cmd_lochin, check=True)

# 2. Extract clean Geiger chirp cycle (4.3s to 5.4s)
cmd_geiger = [
    ffmpeg_exe, "-y",
    "-ss", "00:00:04.4",
    "-to", "00:00:05.4",
    "-i", wav_path,
    "-af", "volume=2.0",
    r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds\real_neoline_geiger.wav"
]
subprocess.run(cmd_geiger, check=True)

# 3. Extract single crisp Geiger click (4.45s to 4.70s)
cmd_click = [
    ffmpeg_exe, "-y",
    "-ss", "00:00:04.45",
    "-to", "00:00:04.72",
    "-i", wav_path,
    "-af", "volume=2.4",
    r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds\real_neoline_click.wav"
]
subprocess.run(cmd_click, check=True)

print("SUCCESS: Extracted exact Neoline Lochin voice and Geiger chirps directly from your video!")
