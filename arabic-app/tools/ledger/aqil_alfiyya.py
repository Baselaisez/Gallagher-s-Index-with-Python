"""(v352-A) the Alfiyya's verses → content/rules/alfiyya.json, joined to the grammar notes and to Ibn ʿAqīl's ledger.

  python3 tools/ledger/aqil_alfiyya.py      (after aqil_toc.py and aqil_ledger.py)

[{n, bab, ar, page, sp, notes:[note ids], rule:[ledger ids], rule_ar, rule_page, rule_sp, en?, tr?}] — every verse of the toc.
  notes    — a grammar note gains a verse when the note's topics (content/rules/commentary_links.json) are the bāb's (aqil_map.py) and
             the verse and its ruling share the note's Arabic (title, examples): 2 × the verse's shared content words + the ruling's ≥ 4. At most
             two verses a note; naḥw notes only (the Alfiyya is naḥw and ṣarf: a balāgha note is never joined).
  rule     — the ledger entries cut from the commentary unit the verse heads (aqil_ledger.py ids).
  rule_ar  — Ibn ʿAqīl's ruling for the verse: the first sentence of the unit's prose that states one (a ruling marker), verbatim.
  en / tr  — our short rendering of rule_ar (tools/ledger/aqil_alfiyya_renderings.json, by hand; «çeviri · hoca onayı bekliyor»);
             a line not rendered with certainty stays Arabic-only.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import aqil_common as A  # noqa: E402
from aqil_map import B  # noqa: E402
from aqil_ledger import RUL, FUNC, toks  # noqa: E402

ROOT = A.ROOT
OUT = ROOT / "content/rules/alfiyya.json"
REND = HERE / "aqil_alfiyya_renderings.json"
NAHW = {"nahw", "awamil"}
# the editor's notes, where the e-text lets one into the matn, write the hamza-less «الافعال / الاسماء / الاعراب»: Ibn ʿAqīl's lines here never do
EDITORISH = re.compile(r"(^|\s)(و|ف|ب|ل)?ال(افعال|اسماء|اعراب|اصل|اول|اخر|امر|ان)(\s|$|[،.:])")


def unit_prose():
    """verse n → (the prose of its unit: [(sp, vol:pp, sentence)])"""
    t, ps = A.pages()
    rows = A.matn_lines(t, ps)
    cls = A.classify(rows)
    n, cur, out = 0, [], {}
    group = []
    last, lastp = ".", None   # the last prose line read, and its page: a page's first prose line may end the last page's sentence
    for i, (p, off, ln) in enumerate(rows):
        if cls[i] == "alf":
            if cur:   # a new verse group begins after prose
                group, cur = [], []
            n += 1
            group.append(n)
            out[n] = cur
        elif cls[i] is None and ln.strip() and not ln.startswith("="):
            cont = lastp is not None and lastp != p["sp"] and not re.search(r"[.:؟!]\s*(\([٠-٩]+\))?\s*$", last)
            last, lastp = ln, p["sp"]
            if not group:
                continue
            for k, (a, s) in enumerate(A.sentences(ln)):
                if k == 0 and cont:
                    continue
                if len(s.split()) >= 5:
                    cur.append((p["sp"], "%d:%d" % (p["vol"], p["pp"]), s))
    return out


def main():
    toc = json.loads((ROOT / "content/rules/toc_ibn_aqil.json").read_text(encoding="utf-8"))
    led = json.loads((ROOT / "content/rules/coverage_ibn_aqil.json").read_text(encoding="utf-8"))["entries"]
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))["links"]
    rend = json.loads(REND.read_text(encoding="utf-8")) if REND.exists() else {}
    notes = {}
    for x in links:
        if x["topic"].startswith("note:") and x.get("group") in NAHW:
            gid = x["topic"][5:]
            g = json.loads((ROOT / "content/grammar" / (gid + ".json")).read_text(encoding="utf-8"))
            ar = g["title"]["ar"] + " " + " ".join(e.get("ar", "") for e in g.get("examples", []))
            notes[gid] = {"topics": set(x["topics"]), "words": {w for w in toks(ar) if len(w) >= 3 and w not in FUNC}}
    prose = unit_prose()
    verses = []
    for b in toc["babs"]:
        for u in b["units"]:
            for n in u["verses"]:
                v = next(v for v in b["verses"] if v["n"] == n)
                ents = [e["id"] for e in led if e["bab"] == b["bab"] and u["from"] <= e["shamela"] <= u["to"]]
                ss = prose.get(n, [])
                ok = [s for s in ss if 30 <= len(s[2]) <= 300 and not EDITORISH.search(s[2])]
                full = [s for s in ok if re.search(r"[.]\s*(\([٠-٩]+\))?\s*$", s[2])]   # a whole sentence, not one cut by the page
                r = next((s for s in full if RUL.search(A.norm(s[2]))), None) or next((s for s in ok if RUL.search(A.norm(s[2]))), None) \
                    or (full or ok or [None])[0]
                d = {"n": n, "bab": b["bab"], "ar": v["ar"], "page": v["page"], "sp": v["sp"], "notes": [], "rule": ents}
                if r:
                    d.update(rule_ar=r[2], rule_page=r[1], rule_sp=r[0])
                verses.append(d)
    byb = defaultdict(list)
    for v in verses:
        byb[v["bab"]].append(v)
    joined = 0
    for gid, nt in sorted(notes.items()):
        cands = [v for bab, vs in byb.items() if bab in B and set(B[bab]["topics"]) & nt["topics"] for v in vs]
        if not cands:
            continue
        W = lambda x: {w for w in toks(x) if len(w) >= 3 and w not in FUNC}
        # the verse's own words count double: a note is joined to the verse that names its matter, the ruling only confirms
        sc = sorted(((2 * len(W(v["ar"]) & nt["words"]) + len(W(v.get("rule_ar", "")) & nt["words"]), -v["n"], v) for v in cands),
                    key=lambda x: (x[0], x[1]), reverse=True)
        pick = [x[2] for x in sc if x[0] >= 4][:2]
        for v in pick:
            if "rule_ar" in v:
                v["notes"].append(gid)
                joined += 1
    by_rule = {v["rule_ar"]: rend[str(v["n"])] for v in verses if str(v["n"]) in rend and v.get("rule_ar")}
    for v in verses:
        r = by_rule.get(v.get("rule_ar"))   # a rendering follows its ruling: two verses of one unit share it
        if r and v.get("rule_ar"):
            v["en"], v["tr"] = r["en"], r["tr"]
    OUT.write_text(json.dumps(verses, ensure_ascii=False, indent=0), encoding="utf-8")
    nv = [v for v in verses if v["notes"]]
    print("verses", len(verses), "with notes", len(nv), "note joins", joined, "notes", len({g for v in nv for g in v["notes"]}),
          "rendered", sum(1 for v in nv if v.get("en")))


if __name__ == "__main__":
    main()
