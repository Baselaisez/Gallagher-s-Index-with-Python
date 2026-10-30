#!/usr/bin/env python3
"""Pack the reader as an OFFLINE REVIEW BUNDLE for friends and reviewers.

    python3 tools/build_review_bundle.py                # dist/qissa-review-<sw-version>.zip
    python3 tools/build_review_bundle.py --out <file>   # a chosen path

The reader is one self-contained HTML file (no CDN, no fonts, no API), so an
offline build is a copy with two changes: REVIEW_BUILD flipped to true — the
reviewer's notes (⚑ on every sentence, the ledger on Progress with export /
copy / import) are on from the first open and every premium story is
unlocked — and a README in English and Turkish on how to open it and how to
send the notes back. The manifest, service worker and icons travel with it so
the same folder also installs as a PWA when served over http(s).

Nothing in prototype/ is modified; the bundle is a fresh folder zipped.
"""
import argparse, pathlib, re, shutil, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROTO = ROOT / "prototype"

README = """QISSA — OFFLINE REVIEW BUILD / ÇEVRİMDIŞI İNCELEME SÜRÜMÜ
=========================================================

EN ───────────────────────────────────────────────────────
What this is
  The whole Qissa reader in one file: every story, the word-by-word analysis,
  the grammar notes, the workshop and the games. It needs no internet.

How to open it
  1. Unzip this folder anywhere (do not move reader.html out of it).
  2. Double-click reader.html — it opens in your browser (Chrome, Edge,
     Firefox or Safari). Everything works from the file, offline.
  3. On a phone: open the folder in a file manager and tap reader.html, or —
     easier — install the hosted version from the link your friend sends you
     (Chrome: ⋮ → "Add to Home screen"; Safari: Share → "Add to Home Screen").
     Once installed it works offline too.

How to review
  • Under every sentence there is a ⚑ button. Tap it, choose what is wrong
    (harakat, i'rab, translation, word meaning, spelling, other — or
    "✓ Correct" when the sentence is fine), pick the word if it concerns one,
    write the problem and what it should be, and save.
  • Tap a word for its meaning, conjugation and i'rab; the ⚑ note can point
    at that word.
  • Your notes stay on your device (in the browser's storage for this file).
  • When you are done: open the Progress tab (📈) → "Reviewer's notes" →
    write your name → "Export (.json)" and send that file back, or "Copy as
    text" and paste it into a message.

TR ───────────────────────────────────────────────────────
Bu nedir
  Qissa okuyucusunun tamamı tek dosyada: bütün hikâyeler, kelime kelime
  tahlil, gramer notları, atölye ve oyunlar. İnternet gerektirmez.

Nasıl açılır
  1. Bu klasörü istediğiniz yere açın (reader.html'i klasörden çıkarmayın).
  2. reader.html'e çift tıklayın — tarayıcıda (Chrome, Edge, Firefox ya da
     Safari) açılır. Her şey dosyadan, çevrimdışı çalışır.
  3. Telefonda: klasörü bir dosya yöneticisinde açıp reader.html'e dokunun;
     ya da — daha kolayı — arkadaşınızın gönderdiği bağlantıdan barındırılan
     sürümü kurun (Chrome: ⋮ → "Ana ekrana ekle"; Safari: Paylaş → "Ana Ekrana
     Ekle"). Kurulduktan sonra o da çevrimdışı çalışır.

Nasıl incelenir
  • Her cümlenin altında bir ⚑ düğmesi var. Dokunun, neyin yanlış olduğunu
    seçin (hareke, i'rab, çeviri, kelime anlamı, yazım, diğer — cümle doğruysa
    "✓ Doğru"), ilgiliyse kelimeyi seçin, sorunu ve doğrusunu yazın, kaydedin.
  • Bir kelimeye dokununca anlamı, çekimi ve i'rabı açılır; ⚑ notu o kelimeyi
    gösterebilir.
  • Notlarınız cihazınızda kalır (bu dosya için tarayıcı deposunda).
  • Bitirince: İlerleme sekmesi (📈) → "Hakem notları" → adınızı yazın →
    "Dışa aktar (.json)" ile dosyayı geri gönderin ya da "Metin olarak kopyala"
    ile bir mesaja yapıştırın.

Build / Sürüm: {version}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="zip path (default dist/qissa-review-<version>.zip)")
    ap.add_argument("--html", help="the reader to pack (default prototype/reader.html)")
    a = ap.parse_args()
    sw = (PROTO / "sw.js").read_text(encoding="utf-8")
    m = re.search(r"const CACHE = 'qissa-v(\d+)';", sw)
    version = "v" + m.group(1) if m else "dev"
    html = pathlib.Path(a.html if a.html else PROTO / "reader.html").read_text(encoding="utf-8")
    flag = "const REVIEW_BUILD = false;"
    if html.count(flag) != 1:
        print("reader.html carries no REVIEW_BUILD flag (expected exactly one)"); sys.exit(1)
    html = html.replace(flag, "const REVIEW_BUILD = true;   // the offline review bundle")
    out = pathlib.Path(a.out) if a.out else ROOT / "dist" / f"qissa-review-{version}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    folder = "qissa-review"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr(f"{folder}/reader.html", html)
        z.writestr(f"{folder}/README.txt", README.replace("{version}", version))
        for name in ("manifest.webmanifest", "sw.js"):
            z.write(PROTO / name, f"{folder}/{name}")
        for icon in sorted((PROTO / "icons").iterdir()):
            z.write(icon, f"{folder}/icons/{icon.name}")
    print(f"{out}  ({out.stat().st_size / 1e6:.1f} MB, reader {version}, REVIEW_BUILD on)")

if __name__ == "__main__":
    main()
