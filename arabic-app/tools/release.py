# -*- coding: utf-8 -*-
"""One command from edited content to a shippable build.

    python3 tools/release.py            # gates + build + smoke + sw bump
    python3 tools/release.py --check    # gates only, no sw bump

Runs the whole loop CLAUDE.md describes, in order, stopping at the first
failure: validate every package -> rebuild both readers -> browser smoke
suite -> i18n gate -> canon audit -> Dart model verification -> PWA suite ->
bump the service-worker cache. This is what makes weekly/monthly content
drops routine: author a chapter, run release.py, commit what it touched.

Environment: NODE_PATH must reach a playwright-core install and
CHROMIUM_PATH a Chromium binary for the two browser suites; set QISSA_SKIP
to a comma list (e.g. "smoke,pwa,dart") to skip suites the machine cannot
run — skipped suites are reported loudly, never silently.
"""
import os, re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP = set(filter(None, os.environ.get("QISSA_SKIP", "").split(",")))
CHECK_ONLY = "--check" in sys.argv

def run(label, cmd, cwd=ROOT):
    print(f"\n=== {label} ===")
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        print(f"\nRELEASE BLOCKED at: {label}")
        sys.exit(1)

def main():
    # 1. every package validates
    pkgs = sorted((ROOT / "content/samples").iterdir()) + \
           [ROOT / "content/user-uploads/deeds-are-by-intentions"]
    for p in pkgs:
        if p.is_dir():
            run(f"validate {p.name}", [sys.executable, "tools/validate_content.py", str(p)])

    # 2. both readers rebuild
    run("build main reader", [sys.executable, "tools/build_prototype.py"])
    hadith = ROOT / "content/user-uploads/deeds-are-by-intentions"
    (hadith / "reader.html").write_bytes((ROOT / "prototype/reader.html").read_bytes())
    run("build hadith reader", [sys.executable, "tools/build_prototype.py",
                                "--package", str(hadith), "--html", str(hadith / "reader.html")])

    # 3. browser suites
    if "smoke" not in SKIP:
        run("smoke suite", ["node", "tools/smoke_test.js"])
        # The generated drill bank is a GOLDEN FILE: a pure function of the
        # engines, committed so that any change moving a single derived cell
        # shows up as a named diff rather than as silence.
        run("drill bank", ["node", "tools/gen_drills.js", "--check"])
    else:
        print("\n!!! SKIPPED smoke suite (QISSA_SKIP)")

    # 4. text gates
    run("i18n gate", [sys.executable, "tools/check_i18n.py"])
    run("canon audit", [sys.executable, "tools/check_canon.py", "--strict"])

    # 5. the Dart data layer must not drift
    if "dart" not in SKIP:
        dart = os.environ.get("DART_BIN", "dart")
        run("dart models", [dart, "flutter/tool/verify_models.dart", "content"])
    else:
        print("\n!!! SKIPPED dart models (QISSA_SKIP)")

    if "pwa" not in SKIP:
        run("pwa suite", ["node", "tools/pwa_test.js"])
    else:
        print("\n!!! SKIPPED pwa suite (QISSA_SKIP)")

    # 6. bump the service worker so every deploy invalidates the old cache
    if not CHECK_ONLY:
        sw = ROOT / "prototype/sw.js"
        text = sw.read_text(encoding="utf-8")
        m = re.search(r"const CACHE = 'qissa-v(\d+)';", text)
        if not m:
            print("cannot find CACHE version in sw.js"); sys.exit(1)
        nxt = int(m.group(1)) + 1
        sw.write_text(text.replace(m.group(0), f"const CACHE = 'qissa-v{nxt}';"),
                      encoding="utf-8")
        print(f"\nsw.js cache -> qissa-v{nxt}")

    print("\nALL GATES GREEN — commit from the repo root and push.")

if __name__ == "__main__":
    main()
