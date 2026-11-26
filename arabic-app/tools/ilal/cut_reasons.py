"""(v348-F) step 3a — cut BY SCRIPT the sentences of the joined sections that give a reason (taʿlīl), each with the sentence before
it for context, verbatim, anchored by book, volume:page and Shamela page. Shaykhzāde whole; from Ibn Mālik and al-Raḍī the sections
of the topics in WAVE (the commonest roles and forms of the corpus). Output: research/ilal/candidates.json (every cut; the hand
reading in tools/ilal/kept.json picks from it by `cid`). Run: python3 tools/ilal/cut_reasons.py [--show TOPIC [N]]"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, norm, pages  # noqa: E402

WAVE = {
    "ibn-malik": ["fail", "naib-fail", "mubtada", "khabar", "maful-bih", "hal", "tamyiz", "idafa", "signs-dual-plural", "five-verbs",
                  "five-nouns", "muqaddar", "irab-bina", "mamnu", "mudmar", "mawsul", "ishara", "kana", "inna", "jarr", "irab-fil", "jazm"],
    "radi": ["ilal", "idgham", "hamza"],
}
MARK = re.compile(r"(^|[^ا-ي])(لان|لانه|لانها|وانما|فانما|لييلا|العله|عله|علل|وجهه|وذلك ان|وذلك لان|فان قيل|فان قلت|اجيب|لكونه|لكونها|"
                  r"حملا علي|تشبيها ب|للفرق بين|فرقا بين|ليفرق|للتخفيف|لثقل|للثقل|استثقال|كراهه|لشبهه|لمشابهته|لمشابهه|للتعذر|لتعذر|لخفته|لخفه)($|[^ا-ي])")
OBJ = re.compile(r"(^|[^ا-ي])(فان قيل|فان قلت|ان قيل)($|[^ا-ي])")
ANS = re.compile(r"^\s*(\(?\d+\)?\s*)?(قلت|قلنا|اجيب|فالجواب|الجواب|والجواب|اجيب)")
SPLIT = re.compile(r"(?<=[.!؟?])\s+|\n")


def sentences(t, s, e):
    """[(start, end)] of the sentences between offsets s and e (verbatim slices of t)."""
    out, i = [], s
    for m in SPLIT.finditer(t, s, e):
        if m.start() > i:
            out.append((i, m.start()))
        i = m.end()
    if e > i:
        out.append((i, e))
    return [(a, b) for a, b in out if t[a:b].strip()]


def section_topics(book, links):
    """section title → [topics] for the sections joined by heading; and, for Shaykhzāde, page → the Qawāʿid entries joined by matn."""
    sec, page = {}, {}
    for k, v in links["topics"].items():
        for r in v["sections"]:
            if r["book"] == book:
                sec.setdefault(r["n"], []).append(k)
    for x in links["links"]:
        for r in x["commentary"]:
            if r["book"] == book and r["via"] == "matn":
                page.setdefault(int(r["shamela"]), []).append(x["topic"])
    return sec, page


def cut():
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))
    out = []
    for book in ("shaykhzade", "ibn-malik", "radi"):
        toc = json.loads((ROOT / f"content/rules/toc_{book}.json").read_text(encoding="utf-8"))
        sec_t, page_t = section_topics(book, links)
        t, ps = pages(book)
        by_sp = {}
        for s in toc["sections"]:
            for sp in range(s["from"]["shamela"], s["to"]["shamela"] + 1):
                by_sp[sp] = s
        for p in ps:
            s = by_sp.get(p["sp"])
            if not s or s["part"] != "text":
                continue
            tops = sec_t.get(s["n"], [])
            if book != "shaykhzade":
                tops = [x for x in tops if x in WAVE[book]]
                if not tops:
                    continue
            ss = sentences(t, p["start"], p["matn_end"])
            k = 0
            for i, (a, b) in enumerate(ss):
                n = norm(t[a:b])
                if not MARK.search(n):
                    continue
                if book == "ibn-malik" and " ... " in t[a:b]:
                    continue   # a verse of the naẓm: the reason is in the prose
                a0 = ss[i - 1][0] if i and len(t[ss[i - 1][0]:b]) < 700 else a
                e = b
                if OBJ.search(n):
                    for a2, b2 in ss[i + 1:i + 3]:
                        if ANS.search(norm(t[a2:b2])):
                            e = b2
                            break
                k += 1
                m = MARK.search(n).group(2)
                out.append({"cid": f"{book}:{p['sp']}:{k}", "book": book, "shamela_page": p["sp"], "vol_page": f"{p['vol']}:{p['pp']}",
                            "section": s["title"], "topics": tops + page_t.get(p["sp"], []), "marker": m,
                            "objection": bool(OBJ.search(n)), "reason": t[a:e], "ar": t[a0:e]})
    return out


def main():
    c = cut()
    d = ROOT / "research/ilal"
    d.mkdir(parents=True, exist_ok=True)
    (d / "candidates.json").write_text(json.dumps({"built_by": "tools/ilal/cut_reasons.py (v348-F)", "n": len(c), "candidates": c},
                                                  ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    from collections import Counter
    print(len(c), Counter(x["book"] for x in c))
    if "--show" in sys.argv:
        tp = sys.argv[sys.argv.index("--show") + 1]
        lim = int(sys.argv[sys.argv.index("--show") + 2]) if len(sys.argv) > sys.argv.index("--show") + 2 else 30
        sel = [x for x in c if tp in x["topics"] or x["section"] == tp]
        sel.sort(key=lambda x: (not x["objection"], x["marker"] not in ("وانما", "العله", "عله", "لان", "لانه"), len(x["reason"])))
        for x in sel[:lim]:
            print(x["cid"], "|", x["reason"][:230].replace("\n", " "))


if __name__ == "__main__":
    main()
