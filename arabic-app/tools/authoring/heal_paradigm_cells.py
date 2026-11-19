# -*- coding: utf-8 -*-
"""Heal the spelling of the STORED paradigm cells (v333 · Atölye audit A41).

Two faults of spelling sat in content/*/morphology.json, and every tool that reads
the stored tables (the Tawkīd lab, the Root Finder, the Mizan, the Sarf ledger, the
word sheet) showed them:

1. the hamza's seat where a suffix meets it — «اِقْرَأَا», «تَقْرَأِينَ», «أَأْخُذُ» for
   اِقْرَآ, تَقْرَئِينَ, آخُذُ (sarf_gen.seat_cells: the same function the generator's
   entry() now runs, so a regeneration writes what this script heals);
2. a hamzat al-waṣl written with no vowel — «انْهَ», «انْصَرَفَ», «اقْتَضَى», «اؤْمُمْنَ» —
   where every other paradigm of the shelf writes «اِ» / «اُ» (the reader's sarfAudit
   regenerates اِنْهَ and fails on the bare alif). The vowel is the rule's: ḍamma where
   the third letter carries a ḍamma (اُنْصُرْ، اُؤْمُمْنَ، and every passive: اُسْتُغْنِيَ),
   kasra otherwise.

Usage:
    python3 tools/authoring/heal_paradigm_cells.py            # dry run: list every cell
    python3 tools/authoring/heal_paradigm_cells.py --apply    # write the files
Idempotent: a second run changes nothing.
"""
import json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from sarf_gen import seat_cells

ROOT = Path(__file__).resolve().parents[2] / "content"
CELLS = ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2", "majhulMazi", "majhulMudari")
WASL = CELLS + ("masdar",)
MARK = "ًٌٍَُِّْٰ"

def wasl(s, passive=False):
    """A bare alif before a quiescent letter at the head of a cell takes the waṣl's vowel."""
    s = unicodedata.normalize("NFC", s)
    if not re.match(r"^[اٱ][ء-ي]ْ", s):
        return s
    # the vowel of the third letter (after the alif and the quiescent letter); a passive māḍī always opens on the ḍamma (اُعْتِيدَ)
    m = re.match(r"^[اٱ][ء-ي]ْ[ء-ي]([" + MARK + r"]*)", s)
    v = "ُ" if (passive or (m and "ُ" in m.group(1))) else "ِ"
    return "ا" + v + s[1:]

def heal_value(key, val):
    def one(c):
        if not isinstance(c, str): return c
        out = unicodedata.normalize("NFC", c)
        if key in CELLS: out = seat_cells(out)
        if key in WASL: out = wasl(out, passive=(key == "majhulMazi"))
        return out if out != unicodedata.normalize("NFC", c) else c   # a cell that only differs in mark order is left as stored
    return [one(c) for c in val] if isinstance(val, list) else one(val)

def main(apply=False):
    changed, files = [], 0
    for coll in ("samples", "user-uploads"):
        for p in sorted((ROOT / coll).glob("*/morphology.json")):
            data = json.loads(p.read_text(encoding="utf-8"))
            touched = False
            for lex, m in data.get("verbs", {}).items():
                for key in WASL:
                    if key not in m: continue
                    old, new = m[key], heal_value(key, m[key])
                    if old == new: continue
                    olds = old if isinstance(old, list) else [old]
                    news = new if isinstance(new, list) else [new]
                    for i, (a, b) in enumerate(zip(olds, news)):
                        if a != b: changed.append((p.parent.name, lex, key, i, a, b))
                    m[key] = new; touched = True
            if touched:
                files += 1
                if apply: p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    for pkg, lex, key, i, a, b in changed:
        print(f"{pkg}\t{lex}\t{key}[{i}]\t{a} → {b}")
    print(f"# {len(changed)} cells in {files} files" + ("" if apply else " (dry run — pass --apply to write)"), file=sys.stderr)
    return changed

if __name__ == "__main__":
    main("--apply" in sys.argv)
