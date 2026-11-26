"""(v348-F) step 2 — join the app's rules to the commentaries. For every entry of the ledgers content/rules/coverage_{qawaid_al_irab,
shudhur,izhar,kafiya,marah,maqsud,izzi}.json and every grammar note, the sections of the three commentaries that treat the same rule:
- Shaykhzāde comments Ibn Hishām's Qawāʿid in order: a Qawāʿid entry is joined to the page where its matn words recur (word bigrams,
  normalised; `via: "matn"`);
- otherwise by topic (tools/ilal/concepts.py): the entry's Arabic / the note's title and id → a topic → the books' sections whose
  «bāb | title» names it (`via: "heading"`).
Writes content/rules/commentary_links.json (a NEW table; the ledgers are not rewritten). Run: python3 tools/ilal/build_links.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, norm, pages  # noqa: E402
from concepts import C  # noqa: E402

LEDGERS = [("qawaid", "coverage_qawaid_al_irab"), ("shudhur", "coverage_shudhur"), ("izhar", "coverage_izhar"),
           ("kafiya", "coverage_kafiya"), ("marah", "coverage_marah"), ("maqsud", "coverage_maqsud"), ("izzi", "coverage_izzi")]
SARF_BOOKS = {"marah", "maqsud", "izzi"}
FIRST_SARF = next(i for i, x in enumerate(C) if x["id"] == "taksir")
NAHW, SARF = C[:FIRST_SARF], C[FIRST_SARF:]
BOOKS = ("shaykhzade", "ibn-malik", "radi")


def tocs():
    out = {}
    for b in BOOKS:
        d = json.loads((ROOT / f"content/rules/toc_{b}.json").read_text(encoding="utf-8"))
        out[b] = [s for s in d["sections"] if s["part"] == "text"]
    return out


def sec_ref(book, s, via):
    return {"book": book, "section": s["title"], "n": s["n"], "page": f'{s["vol"]}:{s["from"]["page"]}–{s["to"]["page"]}',
            "shamela": f'{s["from"]["shamela"]}–{s["to"]["shamela"]}', "via": via}


def concept_secs(T):
    m = {}
    for x in C:
        refs = []
        for key, rx in x["sec"].items():
            book = key.replace("_", "-")
            for s in T[book]:
                if re.search(rx, norm((s["bab"] or "") + " | " + s["title"])):
                    refs.append(sec_ref(book, s, "heading"))
        m[x["id"]] = refs
    return m


def topics_of(text, lat, order):
    t = norm(text or "")
    got = []
    for x in order:
        if (x["ar"] and re.search(x["ar"], t)) or (lat and x["lat"] and re.search(x["lat"], lat)):
            got.append(x["id"])
        if len(got) == 2:
            break
    return got


def shaykhzade_matn(T):
    """Qawāʿid entry → the Shaykhzāde page where its matn words recur."""
    t, ps = pages("shaykhzade")
    txt = [(p, set(_bigr(norm(t[p["start"]:p["matn_end"]])))) for p in ps if p["sec"] in {s["title"] for s in T["shaykhzade"]}]
    sec_by_sp = {}
    for s in T["shaykhzade"]:
        for sp in range(s["from"]["shamela"], s["to"]["shamela"] + 1):
            sec_by_sp[sp] = s

    def find(ar):
        bg = set(_bigr(norm(ar)))
        if len(bg) < 2:
            return None
        best = max(txt, key=lambda pt: len(bg & pt[1]))
        hits = len(bg & best[1])
        if hits < max(2, 0.5 * len(bg)):
            return None
        p = best[0]
        s = sec_by_sp.get(p["sp"])
        return {"book": "shaykhzade", "section": s["title"] if s else p["sec"], "n": s["n"] if s else None,
                "page": f'{p["vol"]}:{p["pp"]}', "shamela": str(p["sp"]), "via": "matn", "hits": f"{hits}/{len(bg)}"}
    return find


def _bigr(s):
    w = re.findall(r"[ء-ي]{2,}", s)
    return [w[i] + " " + w[i + 1] for i in range(len(w) - 1)]


def main():
    T = tocs()
    CS = concept_secs(T)
    find = shaykhzade_matn(T)
    links = []
    for key, fn in LEDGERS:
        d = json.loads((ROOT / f"content/rules/{fn}.json").read_text(encoding="utf-8"))
        order = SARF + NAHW if key in SARF_BOOKS else NAHW + SARF
        for e in d["entries"]:
            com = []
            if key == "qawaid" and e.get("kind") not in ("heading",):
                m = find(e["ar"])
                if m:
                    com.append(m)
            tp = topics_of(e["ar"], None, order) if e.get("status") != "not-automatable" or key == "qawaid" else []
            for t_ in tp:
                for r in CS[t_]:
                    if not any(r["book"] == x["book"] and r["section"] == x["section"] for x in com):
                        com.append(r)
            links.append({"topic": f"ledger:{key}:{e['id']}", "status": e.get("status"), "topics": tp, "commentary": com})
    for f in sorted((ROOT / "content/grammar").glob("*.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        title = g["title"]["ar"] if isinstance(g["title"], dict) else g["title"]
        order = SARF + NAHW if g.get("group") == "sarf" else NAHW + SARF
        # the three commentaries are naḥw and ṣarf: a balāgha / badīʿ / bayān / ʿarūḍ note («الخبر والإنشاء») is not their topic
        tp = topics_of(title, g["id"], order) if g.get("group") in ("nahw", "awamil", "sarf") else []
        com = [r for t_ in tp for r in CS[t_]]
        links.append({"topic": f"note:{g['id']}", "group": g.get("group"), "topics": tp, "commentary": com})
    n_led = sum(1 for x in links if x["topic"].startswith("ledger:"))
    counts = {"ledger_entries": n_led, "ledger_joined": sum(1 for x in links if x["topic"].startswith("ledger:") and x["commentary"]),
              "notes": len(links) - n_led, "notes_joined": sum(1 for x in links if x["topic"].startswith("note:") and x["commentary"]),
              "qawaid_matn_to_shaykhzade": sum(1 for x in links for r in x["commentary"] if r["via"] == "matn"),
              "per_book_sections_joined": {b: len({r["section"] for x in links for r in x["commentary"] if r["book"] == b}) for b in BOOKS}}
    out = {"built_by": "tools/ilal/build_links.py (v348-F)", "about": "topic (ledger entry / grammar note) → the commentaries' sections "
           "that treat the same rule. via=matn: the Qawāʿid sentence's words recur on that Shaykhzāde page; via=heading: by the topic's "
           "name in the section's bāb/title (tools/ilal/concepts.py).", "counts": counts,
           "topics": {x["id"]: {"role": x["role"], "sections": CS[x["id"]]} for x in C}, "links": links}
    (ROOT / "content/rules/commentary_links.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False))
    print("topics with no section:", [k for k, v in CS.items() if not v])


if __name__ == "__main__":
    main()
