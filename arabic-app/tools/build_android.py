#!/usr/bin/env python3
"""build_android.py — ONE COMMAND from the repository reader to the Android project's web assets (wave 69).

    python3 tools/build_android.py            # split the reader into dist/android-www, stamp the version, cap sync
    python3 tools/build_android.py --no-sync  # only write dist/android-www (no node, no Capacitor)
    python3 tools/build_android.py --gradle   # …and then ./gradlew assembleDebug bundleRelease (needs the Android SDK)
    python3 tools/build_android.py --no-sync --www DIR   # (v343) the same web assets into DIR, nothing stamped — the smoke suite's
                                                          # «the shell copy opens offline» check builds and opens exactly this

What it does, and why each step exists (research/APP_STORE_STRATEGY.md §2):
1. `tools/pubsplit.py` splits the self-contained reader into reader.html + data/d1–dN.js (four files since wave 127) — the same split the
   hosted copy uses — so the WebView parses a 3.5 MB page and streams the data files instead of parsing 32 MB
   of HTML; the split page is also written as index.html, which is the only entry Capacitor will load.
2. The PWA shell travels with it (manifest, icons); sw.js does NOT: inside the native shell the files are
   already on the device, and the reader skips service-worker registration when it finds the Capacitor bridge.
3. The build number is the service worker's cache number (`qissa-v240` → versionCode 240, versionName 0.240):
   release.py bumps it on every shippable build, so an APK is traceable to the exact reader it carries and
   two builds of one reader can never carry two version codes. Stamped into android/app/build.gradle.
4. `npx cap sync android` copies dist/android-www into android/app/src/main/assets/public (ignored by git —
   generated, 36 MB) and regenerates the Capacitor gradle glue.
5. The signed outputs come from gradle; the keystore is the owner's and never enters git:
       keytool -genkeypair -v -keystore qissa-release.jks -alias qissa -keyalg RSA -keysize 2048 -validity 10000
       # android/keystore.properties (git-ignored): storeFile=../qissa-release.jks  storePassword=…  keyAlias=qissa  keyPassword=…
       cd android && ./gradlew bundleRelease assembleRelease
   Without keystore.properties the release build is UNSIGNED (Play rejects it; the debug APK installs anywhere).
The CI workflow .github/workflows/qissa-android.yml runs steps 1–5 on demand (workflow_dispatch) and uploads the
APK/AAB as artifacts — the Android SDK is not installable in every container, but it is on every GitHub runner.
"""
import argparse, json, os, pathlib, re, shutil, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
PROTO = ROOT / "prototype"; WWW = ROOT / "dist/android-www"; ANDROID = ROOT / "android"

def sw_version():
    m = re.search(r"const CACHE = 'qissa-v(\d+)';", (PROTO / "sw.js").read_text(encoding="utf-8"))
    if not m: sys.exit("cannot read the cache version from prototype/sw.js")
    return int(m.group(1))

def voice_base():
    """(v349) where the shell fetches the app's voice: --voice-base / QISSA_VOICE_BASE, else the project's Pages site
    derived from GITHUB_REPOSITORY (owner/repo → https://owner.github.io/repo/) on a GitHub runner; '' = package it."""
    b = os.environ.get("QISSA_VOICE_BASE", "").strip()
    if not b and os.environ.get("GITHUB_REPOSITORY", "").count("/") == 1:
        owner, repo = os.environ["GITHUB_REPOSITORY"].split("/")
        b = f"https://{owner.lower()}.github.io/{repo}/"
    if b == "none":
        return ""
    return b if not b or b.endswith("/") else b + "/"


def write_www(WWW=WWW):
    if WWW.exists(): shutil.rmtree(WWW)
    WWW.mkdir(parents=True)
    out = subprocess.run([sys.executable, str(ROOT / "tools/pubsplit.py"), str(PROTO / "reader.html"), str(WWW)],
                         check=True, capture_output=True, text=True).stdout
    print(out.strip().splitlines()[-2])
    shutil.copy(WWW / "reader.html", WWW / "index.html")          # Capacitor loads index.html and nothing else
    shutil.copy(PROTO / "manifest.webmanifest", WWW / "manifest.webmanifest")
    shutil.copytree(PROTO / "icons", WWW / "icons")
    if (PROTO / "privacy.html").exists(): shutil.copy(PROTO / "privacy.html", WWW / "privacy.html")   # the privacy page travels with the shell (wave 71)
    # (v347) shipped narration (tools/narration_pack.py mirrors it to prototype/narration/<story>/audio/…): plain files beside
    # the page, fetched only when a chapter is played — never part of the data slices the WebView parses at boot
    # (v349) the app's own voice (narration/<story>/app/, tools/voice_app.py) is ~100 MB for the shelf: the APK does not carry
    # it when the hosted copy can serve it — the page then fetches a story's files from QISSA_VOICE_BASE on its first listen
    # (GitHub Pages answers any origin, so the WebView's https://localhost may fetch them) and keeps them offline. With no
    # base known (a local build), the files are packaged and the APK grows by their size (printed below).
    base = voice_base()
    if (PROTO / "narration").is_dir():
        shutil.copytree(PROTO / "narration", WWW / "narration", ignore=(lambda d, names: [n for n in names if n == "app" or n == "app-voice.json"]) if base else None)
    page_html = (WWW / "index.html").read_text(encoding="utf-8")
    if base:
        page_html = page_html.replace('<script src="app.js"></script>', f'<script>window.QISSA_VOICE_BASE={json.dumps(base)};</script><script src="app.js"></script>', 1)
        (WWW / "index.html").write_text(page_html, encoding="utf-8")
        print(f"app voice: fetched from {base} on first listen (not in the APK)")
    else:
        vb = sum(f.stat().st_size for f in (WWW / "narration").glob("*/app/*") if f.is_file()) if (WWW / "narration").is_dir() else 0
        print(f"app voice: packaged in the APK ({vb / 1e6:.1f} MB) — set QISSA_VOICE_BASE (or build on GitHub Actions) to fetch it from the hosted copy instead")
    # the data files are classic scripts sharing one global scope with the page (pubsplit's contract); assert the
    # page really references every one of them, or a WebView would show an empty library with no error anyone can see
    page = (WWW / "index.html").read_text(encoding="utf-8")
    data_files = sorted(p.name for p in (WWW / "data").glob("*.js"))   # (v341-S) the core d1-<hash>.js and the body slices b<k>-<hash>.js
    if len(data_files) < 2: sys.exit("the split wrote fewer than two data files")
    # (wave 150) the page names every data file in its loader list (not in <script> tags) and loads the code from app.js
    for name in data_files:
        n = f"data/{name}"
        if f'"{n}"' not in page: sys.exit(f"split page does not load {n}")
    # (v343-S) …and the other way: every data file the page names is in the folder (a page naming a file the split did not write —
    # yesterday's `data/d1.js` — would open an empty shelf on the phone)
    for n in sorted(set(re.findall(r'data/[\w.-]+\.js', page))):
        if not (WWW / n).exists(): sys.exit(f"split page names {n}, which is not in the web assets")
    if '<script src="app.js"></script>' not in page or not (WWW / "app.js").exists(): sys.exit("split page does not load app.js")
    return WWW

def stamp_version(v):
    g = ANDROID / "app/build.gradle"; t = g.read_text(encoding="utf-8")
    t2 = re.sub(r"versionCode \d+", f"versionCode {v}", t)
    t2 = re.sub(r'versionName "[^"]*"', f'versionName "0.{v}"', t2)
    if t2 != t: g.write_text(t2, encoding="utf-8"); print(f"android/app/build.gradle -> versionCode {v}, versionName 0.{v}")
    else: print(f"android/app/build.gradle already at versionCode {v}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-sync", action="store_true", help="write dist/android-www only")
    ap.add_argument("--gradle", action="store_true", help="also run ./gradlew assembleDebug bundleRelease")
    ap.add_argument("--www", help="(v343) write the web assets into this folder instead, stamp nothing (needs --no-sync)")
    ap.add_argument("--voice-base", help="(v349) the hosted copy the app's voice is fetched from ('none' = package it in the APK)")
    a = ap.parse_args()
    if a.voice_base: os.environ["QISSA_VOICE_BASE"] = a.voice_base
    if a.www:
        if not a.no_sync: sys.exit("--www writes a copy for inspection: use it with --no-sync")
        www = write_www(pathlib.Path(a.www).resolve()); print("web assets:", www, "build", sw_version(), "(nothing stamped)"); return
    v = sw_version(); www = write_www(); print("web assets:", www.relative_to(ROOT), "build", v)
    if not ANDROID.exists(): sys.exit("android/ is missing — it is committed; run `npx cap add android` only to recreate it")
    stamp_version(v)
    if a.no_sync: return
    subprocess.run(["npx", "cap", "sync", "android"], cwd=ROOT, check=True)
    pub = ANDROID / "app/src/main/assets/public"
    # (v341-S) the data files are named by content hash: every one the split wrote must have reached the shell
    need = ["index.html", "icons/icon-512.png"] + ["data/" + p.name for p in sorted((www / "data").glob("*.js"))]
    if len(need) < 4: sys.exit("the split wrote fewer than two data files")
    for n in need:
        if not (pub / n).exists(): sys.exit(f"cap sync did not deliver {n}")
    print("assets:", sum(p.stat().st_size for p in pub.rglob("*") if p.is_file()) // 1_000_000, "MB in", pub.relative_to(ROOT))
    if a.gradle:
        subprocess.run(["./gradlew", "assembleDebug", "bundleRelease"], cwd=ANDROID, check=True)
        for p in sorted(ANDROID.glob("app/build/outputs/**/*.a[pa][kb]")): print("built", p.relative_to(ROOT), p.stat().st_size // 1_000_000, "MB")
if __name__ == "__main__": main()
