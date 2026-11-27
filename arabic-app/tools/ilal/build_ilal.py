"""(v348-F) step 3b — content/rules/ilal.json from the hand reading (tools/ilal/kept.json) over the script's cut
(research/ilal/candidates.json). Every `ar` (and `pre`) must be a verbatim substring of its book's page — else the build stops.
Each reason: {id, topic, kind, ar, book, vol_page, shamela_page, en, tr, role?, cls?, notes[], ledger[], words, short}.
Run: python3 tools/ilal/build_ilal.py"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import BOOKS, ROOT, pages  # noqa: E402

WHY = ["لأن", "لان", "لأنه", "لكون", "حملا", "حملًا", "لتعذر", "لعدم", "لشبه", "لاستثقال", "فرقًا", "لثقل", "لسد", "لموازنته", "لفرط"]
_D = "[\u064B-\u065F\u0670\u0640]*"
WHY_RE = re.compile("(?:^|(?<=[\\s(؛،]))(?:" + "|".join(_D.join(map(re.escape, w)) + _D for w in WHY) + ")")


def why_at(ar):
    """the offset in `ar` where its reason clause begins (the first taʿlīl marker after the rule's own words) — the game shows
    ar[why_at:], still a verbatim slice; None when the reason opens the sentence or no marker is found."""
    m = WHY_RE.search(ar, 6)
    return m.start() if m and len(re.findall(r"[\u0621-\u064A]+", ar[:m.start()])) >= 2 else None


KINDS = ("why-state", "why-sign", "why-built", "why-form", "why-order", "objection")


def main():
    cand = {c["cid"]: c for c in json.loads((ROOT / "research/ilal/candidates.json").read_text(encoding="utf-8"))["candidates"]}
    kept = json.loads((ROOT / "tools/ilal/kept.json").read_text(encoding="utf-8"))["kept"]
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))
    notes_of, ledger_of = {}, {}
    for x in links["links"]:
        for t in x["topics"]:
            if x["topic"].startswith("note:"):
                notes_of.setdefault(t, []).append(x["topic"][5:])
            elif x["status"] not in ("heading", "fragment", "not-automatable", "example"):
                ledger_of.setdefault(t, []).append(x["topic"][7:])
    matn = {}
    for x in links["links"]:
        for r in x["commentary"]:
            if r["via"] == "matn":
                matn.setdefault((r["book"], int(r["shamela"])), []).append(x["topic"][7:])
    texts = {b: pages(b) for b in BOOKS}
    out, bad = [], []
    for k in kept:
        c = cand.get(k["cid"])
        if not c:
            bad.append(f"{k['cid']}: no such candidate")
            continue
        assert k["kind"] in KINDS, k
        t, ps = texts[c["book"]]
        i = next(j for j, p in enumerate(ps) if p["sp"] == c["shamela_page"])
        page = t[ps[i]["start"]:ps[i]["end"]]
        if k["ar"] not in page:
            bad.append(f"{k['cid']}: ar is not on its page")
            continue
        if k.get("pre") and not t[ps[i - 1]["start"]:ps[i - 1]["matn_end"]].rstrip().endswith(k["pre"]):
            bad.append(f"{k['cid']}: pre is not the end of the page before")
            continue
        words = len(re.findall(r"[ء-ي]+", k["ar"]))
        r = {"id": "ilal-" + k["cid"].replace(":", "-"), "topic": k["topic"], "kind": k["kind"], "ar": k["ar"],
             "book": c["book"], "vol_page": c["vol_page"], "shamela_page": c["shamela_page"], "section": c["section"]}
        if k.get("pre"):
            r["pre"] = k["pre"]
        for f in ("role", "cls", "case"):
            if k.get(f):
                r[f] = k[f]
        if k.get("en") and k.get("tr"):
            r["en"], r["tr"] = k["en"], k["tr"]
        r["notes"] = notes_of.get(k["topic"], [])[:8]
        r["ledger"] = (matn.get((c["book"], c["shamela_page"])) or ledger_of.get(k["topic"], []))[:8]
        r["words"] = words
        w = why_at(k["ar"])
        if w is not None:
            r["why_at"] = w
        r["short"] = words <= 25 and "en" in r
        out.append(r)
    if bad:
        raise SystemExit("ilal: refused —\n  " + "\n  ".join(bad))
    books = {b: {"ar": v["ar"], "en": v["en"], "tr": v["tr"], "short_en": v["short_en"], "short_tr": v["short_tr"],
                 "file": "research/sources/" + v["file"]} for b, v in BOOKS.items()}
    counts = {"reasons": len(out), "by_book": dict(Counter(r["book"] for r in out)), "by_kind": dict(Counter(r["kind"] for r in out)),
              "rendered": sum(1 for r in out if "en" in r), "short": sum(1 for r in out if r["short"]),
              "topics": len({r["topic"] for r in out}), "notes_reached": len({n for r in out for n in r["notes"]})}
    doc = {"built_by": "tools/ilal/build_ilal.py (v348-F) from tools/ilal/kept.json over research/ilal/candidates.json",
           "about": "the grammarians' own reasons (taʿlīl), verbatim and unvowelled as printed, anchored by book, vol:page and "
                    "Shamela page. en/tr are our renderings — «çeviri · hoca onayı bekliyor».", "books": books, "counts": counts,
           "reasons": out}
    (ROOT / "content/rules/ilal.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
