#!/usr/bin/env python3
"""
Generate 100 high-resolution QR codes for Mandarin audio cards.
Points to GitHub Pages web player URLs.

Usage:
  python generate_qrcodes.py --username YOUR_GITHUB_USERNAME --repo REPO_NAME
  python generate_qrcodes.py --base-url https://USERNAME.github.io/REPO_NAME
"""

import argparse
import csv
import qrcode
from pathlib import Path
from urllib.parse import quote

def generate_qrcodes(base_url: str, output_dir: Path):
    """Generate QR codes for all 100 cards."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load card data from CSV
    csv_path = Path("mandarin_audio_qr_links.csv")
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    print(f"Generating {len(rows)} QR codes for: {base_url}")
    print(f"Output directory: {output_dir}")
    print()

    for row in rows:
        card_num = int(row["Card Number"])
        word = row["Simplified Chinese"]

        # Build the web player URL (e.g., https://user.github.io/repo/?id=1)
        player_url = f"{base_url}/?id={card_num}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=3,           # 29x29 modules - good balance for URLs
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% damage recovery
            box_size=10,         # 10px per module = 290x290px base
            border=4,            # Quiet zone
        )
        qr.add_data(player_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save with filename: 001_谢谢_qr.png
        filename = f"{card_num:03d}_{word}_qr.png"
        filepath = output_dir / filename
        img.save(filepath)

        print(f"  ✓ Card {card_num:3d}: {word} → {filename}")

    print(f"\n✅ All {len(rows)} QR codes generated in '{output_dir}/'")
    print(f"   Each QR code points to: {base_url}/?id=<card_number>")
    print()
    print("Next steps:")
    print("  1. Print the QR codes on cards/stickers")
    print("  2. Anyone scanning goes directly to the web player page")
    print("  3. Page shows Chinese word + play button + prev/next navigation")

def main():
    parser = argparse.ArgumentParser(
        description="Generate QR codes for Mandarin audio cards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_qrcodes.py --username myname --repo mandarin-audio
  python generate_qrcodes.py --base-url https://myname.github.io/mandarin-audio
        """
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--username", help="GitHub username")
    group.add_argument("--base-url", help="Full base URL (e.g. https://user.github.io/repo)")

    parser.add_argument("--repo", default="mandarin-audio", help="Repository name (default: mandarin-audio)")
    parser.add_argument("--output", default="qr_codes", help="Output directory (default: qr_codes)")

    args = parser.parse_args()

    if args.username:
        base_url = f"https://{args.username}.github.io/{args.repo}"
    else:
        base_url = args.base_url.rstrip('/')

    output_dir = Path(args.output)
    generate_qrcodes(base_url, output_dir)

if __name__ == "__main__":
    main()