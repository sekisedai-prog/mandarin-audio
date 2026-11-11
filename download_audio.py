"""Download every MP3 listed in mandarin_audio_qr_links.csv.

Usage:  python download_audio.py [path/to/mandarin_audio_qr_links.csv]
Output: ./audio/001_谢谢.mp3, 002_再见.mp3, ...
Only needs Python 3 (no extra packages).
"""
import csv, sys, time, urllib.request
from pathlib import Path

# Force stdout to UTF-8 to handle Chinese characters in Windows terminal output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

csv_path = Path(sys.argv[1] if len(sys.argv) > 1 else "mandarin_audio_qr_links.csv")
out_dir = Path("audio")
out_dir.mkdir(exist_ok=True)

with open(csv_path, newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

failed = []
for row in rows:
    name = Path(row["QR PNG"]).stem + ".mp3"      # e.g. 001_谢谢.mp3
    dest = out_dir / name
    if dest.exists() and dest.stat().st_size > 0:
        continue
    for attempt in range(3):
        try:
            req = urllib.request.Request(row["Audio URL"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                dest.write_bytes(r.read())
            print("OK  ", name)
            break
        except Exception as e:
            if attempt == 2:
                print("FAIL", name, e)
                failed.append(name)
            else:
                time.sleep(1.5)

print(f"\nDone: {len(rows) - len(failed)}/{len(rows)} downloaded into '{out_dir}/'")
if failed:
    print("Failed:", ", ".join(failed))
