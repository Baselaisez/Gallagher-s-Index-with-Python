#!/usr/bin/env python3
"""mk_trans.py — trans_*.txt (three lines per sentence: @ch:sId / English / Turkish) → trans.json for pkg_from_engine.py --trans."""
import json, glob, sys
from pathlib import Path
H = Path(__file__).parent
out = {}; bad = []
for f in sorted(glob.glob(str(H / "trans_*.txt"))):
    L = [x.rstrip("\n") for x in open(f, encoding="utf-8") if x.strip()]
    if len(L) % 3: bad.append(f"{f}: {len(L)} lines, not a multiple of three")
    for i in range(0, len(L) - 2, 3):
        if not L[i].startswith("@") or L[i + 1].startswith("@") or L[i + 2].startswith("@"): bad.append(f"{f}: line {i + 1} {L[i][:30]}"); continue
        k = L[i][1:].strip()
        if k in out: bad.append("duplicate " + k)
        out[k] = {"en": L[i + 1].strip(), "tr": L[i + 2].strip()}
json.dump(out, open(H / "trans.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "sentences;", len(bad), "problems"); [print(" ", b) for b in bad[:20]]
sys.exit(1 if bad else 0)
