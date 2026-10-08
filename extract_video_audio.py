import subprocess
import os
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
video_path = r"C:\Users\Karantin.uz\Desktop\Antiradar\URiEqUMbBc8l3pUo5jI5+6SWXRzKzZbE.mp4"
output_wav = r"C:\Users\Karantin.uz\Desktop\Antiradar\sounds\neoline_full_audio.wav"

cmd = [
    ffmpeg_exe,
    "-y",
    "-i", video_path,
    "-vn",
    "-acodec", "pcm_s16le",
    "-ar", "44100",
    "-ac", "2",
    output_wav
]

print("Extracting full audio from video...")
subprocess.run(cmd, check=True)
print(f"Extracted: {output_wav} (Size: {os.path.getsize(output_wav)} bytes)")
