#!/usr/bin/env python3
"""build_android.py — ONE COMMAND from the repository reader to the Android project's web assets (wave 69).

    python3 tools/build_android.py            # split the reader into dist/android-www, stamp the version, cap sync
    python3 tools/build_android.py --no-sync  # only write dist/android-www (no node, no Capacitor)
    python3 tools/build_android.py --gradle   # …and then ./gradlew assembleDebug bundleRelease (needs the Android SDK)

What it does, and why each step exists (research/APP_STORE_STRATEGY.md §2):
1. `tools/pubsplit.py` splits the self-contained reader into reader.html + data/d1–d3.js — the same split the
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
import argparse, json, pathlib, re, shutil, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
PROTO = ROOT / "prototype"; WWW = ROOT / "dist/android-www"; ANDROID = ROOT / "android"

def sw_version():
    m = re.search(r"const CACHE = 'qissa-v(\d+)';", (PROTO / "sw.js").read_text(encoding="utf-8"))
    if not m: sys.exit("cannot read the cache version from prototype/sw.js")
    return int(m.group(1))

def write_www():
    if WWW.exists(): shutil.rmtree(WWW)
    WWW.mkdir(parents=True)
    out = subprocess.run([sys.executable, str(ROOT / "tools/pubsplit.py"), str(PROTO / "reader.html"), str(WWW)],
                         check=True, capture_output=True, text=True).stdout
    print(out.strip().splitlines()[-2])
    shutil.copy(WWW / "reader.html", WWW / "index.html")          # Capacitor loads index.html and nothing else
    shutil.copy(PROTO / "manifest.webmanifest", WWW / "manifest.webmanifest")
    shutil.copytree(PROTO / "icons", WWW / "icons")
    if (PROTO / "privacy.html").exists(): shutil.copy(PROTO / "privacy.html", WWW / "privacy.html")   # the privacy page travels with the shell (wave 71)
    # the data files are classic scripts sharing one global scope with the page (pubsplit's contract); assert the
    # page really references all three, or a WebView would show an empty library with no error anyone can see
    page = (WWW / "index.html").read_text(encoding="utf-8")
    for n in ("data/d1.js", "data/d2.js", "data/d3.js"):
        if f'<script src="{n}"></script>' not in page: sys.exit(f"split page does not load {n}")
        if not (WWW / n).exists(): sys.exit(f"missing {n}")
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
    a = ap.parse_args()
    v = sw_version(); www = write_www(); print("web assets:", www.relative_to(ROOT), "build", v)
    if not ANDROID.exists(): sys.exit("android/ is missing — it is committed; run `npx cap add android` only to recreate it")
    stamp_version(v)
    if a.no_sync: return
    subprocess.run(["npx", "cap", "sync", "android"], cwd=ROOT, check=True)
    pub = ANDROID / "app/src/main/assets/public"
    for n in ("index.html", "data/d1.js", "data/d2.js", "data/d3.js", "icons/icon-512.png"):
        if not (pub / n).exists(): sys.exit(f"cap sync did not deliver {n}")
    print("assets:", sum(p.stat().st_size for p in pub.rglob("*") if p.is_file()) // 1_000_000, "MB in", pub.relative_to(ROOT))
    if a.gradle:
        subprocess.run(["./gradlew", "assembleDebug", "bundleRelease"], cwd=ANDROID, check=True)
        for p in sorted(ANDROID.glob("app/build/outputs/**/*.a[pa][kb]")): print("built", p.relative_to(ROOT), p.stat().st_size // 1_000_000, "MB")
if __name__ == "__main__": main()
