"""(v348-F) step 1 — structure each commentary BY SCRIPT: its chapters / bābs / sections with page spans, from the page headers'
[section] plus the in-text headings; for Ibn Mālik's Kāfiya Shāfiya the naẓm's verses (lines « … ... … ») apart from the prose.
Writes content/rules/toc_<book>.json. Run: python3 tools/ilal/build_toc.py"""
import json
import re
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common import BOOKS, ROOT, pages  # noqa: E402

EDITOR = {"إهداء", "شكر", "مقدمة المحقق", "مقدمة التحقيق", "تقديم", "تعريف بالمؤلف", "تعريف ب الكافية الشافية"}
HEAD = re.compile(r"^\[?(الباب|باب|فصل|مسألة|المسألة|النوع|تنبيه|فائدة|قاعدة)\b[^\n]{0,70}$")


def part_of(book, p):
    if p["sec"] in EDITOR:
        return "editor"
    if book == "ibn-malik" and p["vol"] == 5:
        return "index"
    if book == "radi" and p["vol"] == 4:
        return "shawahid"      # al-Baghdādī's Sharḥ shawāhid al-Shāfiya, printed as vol. 4
    return "text"


def build(book):
    t, ps = pages(book)
    secs, cur, bab = [], None, None
    pend = []   # (ibn-malik) a run of verse lines; it is the naẓm only when the author's «"ش":» follows it — a shāhid in the prose is not
    for p in ps:
        part = part_of(book, p)
        if part == "text" and (p["sec"].startswith("باب") or p["sec"].startswith("الباب")):
            bab = p["sec"]
        key = (p["sec"], p["vol"], part)
        if not cur or cur["_k"] != key:
            cur = {"_k": key, "n": len(secs) + 1, "title": p["sec"], "part": part, "vol": p["vol"],
                   "bab": bab if part == "text" else None, "from": {"shamela": p["sp"], "page": p["pp"]},
                   "to": {"shamela": p["sp"], "page": p["pp"]}, "headings": [], "verses": 0, "first_verse": None}
            secs.append(cur)
        cur["to"] = {"shamela": p["sp"], "page": p["pp"]}
        body = t[p["start"]:p["matn_end"]]
        for ln in body.split("\n"):
            s = ln.strip()
            if not s:
                continue
            if book == "ibn-malik" and " ... " in s and not s.startswith('"ش"'):
                pend.append({"shamela": p["sp"], "ar": s})
                continue
            if book == "ibn-malik":
                if s.startswith('"ش"') and pend:
                    cur["verses"] += len(pend)
                    if cur["first_verse"] is None:
                        cur["first_verse"] = pend[0]
                pend = []
            if HEAD.match(s) and len(s) < 80:
                cur["headings"].append({"shamela": p["sp"], "ar": s})
    for s in secs:
        del s["_k"]
        s["pages"] = s["to"]["shamela"] - s["from"]["shamela"] + 1
        if book != "ibn-malik":
            del s["verses"], s["first_verse"]
    b = BOOKS[book]
    return {"book": book, "title": {"ar": b["ar"], "en": b["en"], "tr": b["tr"]}, "source_file": "research/sources/" + b["file"],
            "built_by": "tools/ilal/build_toc.py (v348-F)", "pages": len(ps),
            "counts": {"sections": len(secs), "text_sections": sum(1 for s in secs if s["part"] == "text"),
                       "babs": len({s["bab"] for s in secs if s["bab"]}),
                       **({"verses": sum(s["verses"] for s in secs)} if book == "ibn-malik" else {})},
            "sections": secs}


def main():
    for book in BOOKS:
        d = build(book)
        (ROOT / f"content/rules/toc_{book}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(book, d["counts"])


if __name__ == "__main__":
    main()
