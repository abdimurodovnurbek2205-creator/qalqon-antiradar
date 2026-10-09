from pathlib import Path
import subprocess

schema_path = Path("supabase/schema.sql")
seed_path = Path("supabase/seed_cameras.sql")
install_path = Path("supabase/INSTALL_ALL.sql")

schema_text = schema_path.read_text(encoding="utf-8")
seed_text = seed_path.read_text(encoding="utf-8")

combined = schema_text + "\n\n-- ==================== SPEED CAMERAS DATA ====================\n" + seed_text
install_path.write_text(combined, encoding="utf-8")
print(f"Successfully created {install_path} ({len(combined)} bytes)")

# Copy to Windows clipboard via clip.exe or powershell
try:
    process = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    process.communicate(input=combined.encode('utf-8'))
    print("Successfully copied to Windows clipboard!")
except Exception as e:
    print(f"Clipboard copy notice: {e}")
