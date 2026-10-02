#!/usr/bin/env python3
"""Report Turkish coverage of the per-token i'rab notes.

The reader shows i'rab in the selected UI language; Turkish comes from the shared
translation memory at content/i18n/irab-tr.json, keyed by the English string.
This tool lists every English i'rab string that has no Turkish yet, so the gap is
visible instead of silently falling back to English.

Usage:
    python3 tools/check_irab_tr.py            # summary + missing strings
    python3 tools/check_irab_tr.py --strict   # exit 1 if coverage is below 100%
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS = [ROOT / "content/samples", ROOT / "content/user-uploads"]
IRAB_TR = ROOT / "content/i18n/irab-tr.json"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any i'rab string lacks Turkish")
    args = ap.parse_args()

    entries = {}
    if IRAB_TR.is_file():
        entries = json.loads(IRAB_TR.read_text(encoding="utf-8")).get("entries", {})

    counts = Counter()
    per_story = {}
    for coll in COLLECTIONS:
        if not coll.is_dir():
            continue
        for pkg in sorted(coll.iterdir()):
            if not (pkg / "manifest.json").is_file():
                continue
            total = translated = 0
            for chapter in sorted((pkg / "chapters").glob("*.json")):
                data = json.loads(chapter.read_text(encoding="utf-8"))
                for sen in data.get("sentences", []):
                    for tok in sen.get("tokens", []):
                        irab = tok.get("irab") or {}
                        en = irab.get("en")
                        if not en:
                            continue
                        total += 1
                        if irab.get("tr") or en in entries:
                            translated += 1
                        else:
                            counts[en] += 1
            if total:
                per_story[pkg.name] = (translated, total)

    print("Turkish i'rab coverage by story:")
    grand_t = grand_n = 0
    for name, (t, n) in sorted(per_story.items()):
        grand_t += t
        grand_n += n
        pct = 100 * t / n if n else 100
        flag = "" if t == n else "   <-- gaps"
        print(f"  {pct:5.1f}%  {t:4d}/{n:<4d}  {name}{flag}")
    overall = 100 * grand_t / grand_n if grand_n else 100
    print(f"\nOverall: {overall:.1f}% ({grand_t}/{grand_n} tokens), "
          f"{len(entries)} phrases in the translation memory")

    if counts:
        print(f"\n{len(counts)} untranslated string(s), most frequent first:")
        for en, n in counts.most_common():
            print(f"  [{n}x] {en}")
        if args.strict:
            return 1
    else:
        print("\nAll i'rab notes have Turkish. ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
