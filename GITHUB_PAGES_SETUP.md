# 🎯 GitHub Pages Setup Guide for Mandarin Audio

## Quick Setup (5 minutes)

### 1. Create a GitHub Repository
1. Go to [github.com/new](https://github.com/new)
2. **Repository name**: `mandarin-audio` (or any name you like)
3. Set to **Public** (required for free GitHub Pages)
4. Don't initialize with README/license/.gitignore (we have files already)
5. Click **Create repository**

### 2. Push Files from Your Computer
```bash
# Open terminal/command prompt in this folder
cd C:\Users\brian\Downloads\audio

# Initialize git and push
git init
git add .
git commit -m "Add Mandarin audio cards + web player"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mandarin-audio.git
git push -u origin main
```
> Replace `YOUR_USERNAME` with your actual GitHub username.

### 3. Enable GitHub Pages
1. Go to your repo on GitHub → **Settings** tab
2. Scroll to **Pages** in the left sidebar
3. **Source**: "Deploy from a branch"
4. **Branch**: `main` / `(root)` → **Save**
5. Wait 1-2 minutes for deployment

### 4. Your Live URLs
- **Web Player**: `https://YOUR_USERNAME.github.io/mandarin-audio/?id=1`
- **Direct Audio**: `https://YOUR_USERNAME.github.io/mandarin-audio/audio/001_%E8%B0%A2%E8%B0%A2.mp3`

---

## ✅ What You Get

| Feature | Description |
|---------|-------------|
| 🎵 **Web Player** | Beautiful mobile-first page showing Chinese word + play button + prev/next navigation |
| 🔗 **Permanent URLs** | Never expire, served via GitHub's global CDN |
| 📱 **Mobile Optimized** | Works perfectly on iPhone/Android when scanning QR codes |
| 🌓 **Dark Mode** | Auto-adapts to phone's system theme |
| 🔁 **Auto Navigation** | Swipe or tap to go to next/previous card |

---

## 📸 Generating QR Codes

Once you know your GitHub username and repo name, run:

```bash
python generate_qrcodes.py --username YOUR_USERNAME --repo mandarin-audio
```

This creates 100 high-res QR code PNGs in `./qr_codes/` folder pointing to your live web player pages.

---

## 📁 Files in This Folder

```
audio/
├── index.html           # Web player (embed this on your own site too!)
├── audio/               # 100 MP3 files
│   ├── 001_谢谢.mp3
│   ├── 002_再见.mp3
│   └── ...
├── generate_qrcodes.py  # Run after GitHub Pages is live
├── mandarin_audio_qr_links.csv
└── download_audio.py
```

---

## 🔧 Customization

Edit `index.html` to:
- Change colors (CSS variables in `:root`)
- Add pinyin/English translations to the card data
- Add more cards by extending the `CARDS` array

---

## ⚡ One-Command Deploy (Optional)

If you have [GitHub CLI](https://cli.github.com/) installed:
```bash
gh repo create mandarin-audio --public --source=. --push
gh pages create --branch main --path /
```