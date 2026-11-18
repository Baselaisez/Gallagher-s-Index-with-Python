#!/usr/bin/env python3
"""precheck_apply.py — write the checked AI-ONAY corrections into the content (precheck branch only).

    python3 tools/precheck_apply.py [batch …] [--write]

Reads review/ai-precheck/checked/<batch>.jsonl (the output of `precheck.py check`). For every AI-ONAY:
  - the token is found by package / chapter / sentence / index, and must still carry the value the finding was made
    on (for an iʿrāb field: the Arabic line as it stood; for `surface`: the vowelled word). A token that has moved
    or was already changed is skipped and reported, never guessed at;
  - an iʿrāb correction replaces the token's {ar, en, tr} together; a `surface` correction replaces surface.full
    only when its letters are the same (the validator's bare/full invariant);
  - every change is appended to review/ai-precheck/applied.jsonl (id, where, before, after, source).
AI-RET lines go to review/ai-precheck/ai-rejections.jsonl, marked `"confirmed_by_human": false` — they are the AI's
opinion only and no tool may treat them as the scholar's rejections (review_batch.py --learn-from-rejections reads
the human log reports/review-false-positives.jsonl alone).
Without --write nothing is written; the dry run prints what would change.
"""
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "review/ai-precheck"
N = lambda s: unicodedata.normalize("NFC", s or "")
bare = lambda s: re.sub(r"[ً-ْٰـ]", "", N(s))


def quoted(q, line):
    """The finding quoted the line, perhaps shortened with «…»: every quoted piece must stand in the line, in order."""
    q, line = bare(q).replace("...", "…"), bare(line)
    pos = 0
    for piece in [x.strip(" ،.") for x in q.split("…")]:
        if not piece: continue
        k = line.find(piece, pos)
        if k < 0: return False
        pos = k + len(piece)
    return True


MA_KEYS = [("مَوْصُولٌ", "ma-mawsula"), ("اسْتِفْهَامٍ", "ma-istifham"), ("الْحِجَازِيَّةُ", "ma-hijaziyya"), ("مَصْدَرِيَّةٌ", "ma-masdariyya"), ("نَافِيَةٌ", "ma-nafiya")]


def relex_ma(root, write):
    """«One key, one word»: a مَا whose line was corrected to another face must carry that face's lexicon key (on the
    token and on its segment), and the package's glossary must own the key — copied from the shelf, where every مَا
    face is already defined once. Returns the list of changes."""
    import review_batch as rb
    shelf = {}
    for p in rb.pending_packages():
        g = json.loads((p / "glossary.json").read_text(encoding="utf-8")) if (p / "glossary.json").is_file() else {}
        for k, v in (g.get("entries") or {}).items():
            if k.startswith("ma-") and k not in shelf: shelf[k] = v
    touched = set()                        # only lines a correction changed: the authored rest keeps the key its author chose
    for name in ("applied.jsonl", "rule-applied.jsonl"):
        fp = D / name
        if fp.is_file():
            for l in fp.read_text(encoding="utf-8").splitlines():
                if l.strip(): a = json.loads(l); touched.add((a["package"], a["where"]))
    out = []
    for p in rb.pending_packages():
        pk = json.loads((p / "manifest.json").read_text(encoding="utf-8"))["id"]
        gp = p / "glossary.json"; gl = json.loads(gp.read_text(encoding="utf-8")); ent = gl.get("entries") or {}; gchanged = False
        for f in (p / "chapters").glob("*.json"):
            ch = json.loads(f.read_text(encoding="utf-8")); changed = False
            for sen in ch["sentences"]:
                for i, t in enumerate(sen["tokens"]):
                    segs = t.get("segments") or []
                    holders = [t] if (t.get("lex") or "").startswith("ma-") else [x for x in segs if (x.get("lex") or "").startswith("ma-")]
                    if not holders or bare((t.get("surface") or {}).get("full")).lstrip("وف") != "ما": continue
                    if (pk, f"{ch.get('chapter', f.stem)}:{sen['id']}:{i}") not in touched: continue
                    line = N((t.get("irab") or {}).get("ar")); want = None
                    for mark, key in MA_KEYS:
                        if mark in line: want = key; break
                    if not want: continue
                    for h in holders:
                        if h.get("lex") != want and want in shelf:
                            out.append((p.name, f.stem, sen["id"], i, h.get("lex"), want)); h["lex"] = want; changed = True
                            if want not in ent: ent[want] = shelf[want]; gchanged = True
            if write and changed: f.write_text(json.dumps(ch, ensure_ascii=False, indent=1), encoding="utf-8")
        if write and gchanged: gl["entries"] = ent; gp.write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def main():
    write = "--write" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = sorted((D / "checked").glob("*.jsonl"))
    if names: files = [f for f in files if f.stem in names]
    F = {f["id"]: f for f in json.loads((D / "findings-critical.json").read_text(encoding="utf-8"))}
    folders = {}
    import review_batch as rb
    for p in rb.pending_packages():
        folders[json.loads((p / "manifest.json").read_text(encoding="utf-8"))["id"]] = p
    applied_ids = set()
    ap = D / "applied.jsonl"
    if ap.is_file():
        applied_ids = {json.loads(l)["id"] for l in ap.read_text(encoding="utf-8").splitlines() if l.strip()}
    rej = D / "ai-rejections.jsonl"
    rej_ids = {json.loads(l)["id"] for l in rej.read_text(encoding="utf-8").splitlines() if l.strip()} if rej.is_file() else set()
    chapters = {}
    changes, skipped, new_rej = [], [], []
    for vf in files:
        for line in vf.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            v = json.loads(line); f = F[v["id"]]
            if v["verdict"] == "AI-RET" and v["id"] not in rej_ids:
                new_rej.append({"id": v["id"], "package": f["package"], "where": f"{f['chapter']}:{f['sentence']}:{f['token']}",
                                "surface": f["surface"], "current": f["current"], "suggested": f["suggested"],
                                "note_tr": v.get("note_tr"), "note_en": v.get("note_en"), "batch": vf.stem,
                                "by": "ai", "confirmed_by_human": False})
            if v["verdict"] != "AI-ONAY" or v["id"] in applied_ids: continue
            p = folders.get(f["package"])
            cf = p / "chapters" / f"{f['chapter']}.json" if p else None
            if not cf or not cf.is_file(): skipped.append((v["id"], "chapter file not found")); continue
            if cf not in chapters: chapters[cf] = json.loads(cf.read_text(encoding="utf-8"))
            sen = next((s for s in chapters[cf]["sentences"] if s["id"] == f["sentence"]), None)
            if not sen or not (0 <= int(f["token"]) < len(sen["tokens"])): skipped.append((v["id"], "token not found")); continue
            t = sen["tokens"][int(f["token"])]
            c = v["corrected"]; fld = f["field"]
            if fld.startswith("irab"):
                ir = t.get("irab") or {}
                if fld == "irab.ar" and not quoted(f["current"], ir.get("ar")):
                    skipped.append((v["id"], "the line no longer reads as the finding quoted it")); continue
                if not all(c.get(k) for k in ("ar", "en", "tr")):
                    skipped.append((v["id"], "corrected iʿrāb is not trilingual")); continue
                before = dict(ir); t["irab"] = {"ar": N(c["ar"]), "en": c["en"], "tr": c["tr"]}
            elif fld == "surface":
                val = N(c.get("value") or c.get("ar"))
                if bare(val) != bare((t.get("surface") or {}).get("full")):
                    skipped.append((v["id"], "corrected vowelling changes the letters")); continue
                before = dict(t["surface"]); t["surface"]["full"] = val
            else:
                skipped.append((v["id"], f"field {fld} is applied by hand")); continue
            changes.append({"id": v["id"], "package": f["package"], "where": f"{f['chapter']}:{f['sentence']}:{f['token']}",
                            "surface": f["surface"], "field": fld, "before": before,
                            "after": t["irab"] if fld.startswith("irab") else t["surface"], "source": v.get("source"),
                            "batch": vf.stem})
    for c in changes:
        print(f"{c['id']} {c['package']} {c['where']} {c['surface']}\n   - {json.dumps(c['before'], ensure_ascii=False)[:180]}\n   + {json.dumps(c['after'], ensure_ascii=False)[:180]}")
    for i, why in skipped: print(f"SKIP {i}: {why}")
    print(f"{len(changes)} corrections, {len(skipped)} skipped, {len(new_rej)} AI rejections logged" + ("" if write else " — dry run"))
    if not write: return
    for cf, ch in chapters.items():
        cf.write_text(json.dumps(ch, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in relex_ma(ROOT, True): print("RELEX", *r)
    with open(ap, "a", encoding="utf-8") as fh:
        for c in changes: fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    with open(rej, "a", encoding="utf-8") as fh:
        for r in new_rej: fh.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    if "--relex" in sys.argv:
        for r in relex_ma(ROOT, "--write" in sys.argv): print("RELEX", *r)
    else:
        main()
