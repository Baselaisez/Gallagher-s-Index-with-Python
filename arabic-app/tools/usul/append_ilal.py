"""(v352-U) item 5, step b — APPEND al-Khaṣāʾiṣ's kept reasons (tools/usul/kept_khasais.json, the hand reading) to the END of
content/rules/ilal.json in its exact shape (book «khasais» = الخصائص). Never reorders or rewrites another entry: it drops only its own
`ilal-khasais-*` rows (so a rerun is idempotent) and adds the book's name to `books` if absent. Refuses any `ar` that is not a verbatim
substring of its Shamela page's matn. Then rerun tools/usul/kinds.py (the kind side table). Run: python3 tools/usul/append_ilal.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import BOOKS, ROOT, on_page, pages  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ilal"))
from build_ilal import KINDS, why_at  # noqa: E402

PFX = "ilal-khasais-"


def main():
    p = ROOT / "content/rules/ilal.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    kept = json.loads((ROOT / "tools/usul/kept_khasais.json").read_text(encoding="utf-8"))["kept"]
    toc = json.loads((ROOT / "content/rules/toc_khasais.json").read_text(encoding="utf-8"))["babs"]
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))
    notes_of, ledger_of = {}, {}
    for x in links["links"]:
        for t in x["topics"]:
            if x["topic"].startswith("note:"):
                notes_of.setdefault(t, []).append(x["topic"][5:])
            elif x["status"] not in ("heading", "fragment", "not-automatable", "example"):
                ledger_of.setdefault(t, []).append(x["topic"][7:])
    t, ps = pages("khasais")
    vp = {q["sp"]: f"{q['vol']}:{q['pp']}" for q in ps}
    out, bad, n_on = [], [], {}
    for k in kept:
        if not on_page("khasais", k["sp"], k["ar"], t, ps):
            bad.append(f"{k['sp']}: ar is not on its page — {k['ar'][:40]}")
            continue
        assert k["kind"] in KINDS, k
        n_on[k["sp"]] = n_on.get(k["sp"], 0) + 1
        b = next((x for x in toc if x["from"]["shamela"] <= k["sp"] <= x["to"]["shamela"]), None)
        words = len(re.findall(r"[ء-ي]+", k["ar"]))
        r = {"id": f"{PFX}{k['sp']}-{n_on[k['sp']]}", "topic": k["topic"], "kind": k["kind"], "ar": k["ar"], "book": "khasais",
             "vol_page": vp[k["sp"]], "shamela_page": k["sp"], "section": re.sub(r"^[٠-٩]+-\s*|\s*[٠-٩]+-[٠-٩]+:?$|^\[|\]$", "", b["ar"]) if b else ""}
        for f in ("role", "cls", "case"):
            if k.get(f):
                r[f] = k[f]
        if k.get("en") and k.get("tr"):
            r["en"], r["tr"] = k["en"], k["tr"]
        r["notes"] = notes_of.get(k["topic"], [])[:8]
        r["ledger"] = ledger_of.get(k["topic"], [])[:8]
        r["words"] = words
        w = why_at(k["ar"])
        if w is not None:
            r["why_at"] = w
        r["short"] = words <= 25 and "en" in r
        out.append(r)
    if bad:
        raise SystemExit("append_ilal: refused —\n  " + "\n  ".join(bad))
    d["reasons"] = [r for r in d["reasons"] if not r["id"].startswith(PFX)] + out
    if "khasais" not in d["books"]:
        b = BOOKS["khasais"]
        d["books"]["khasais"] = {"ar": b["ar"], "en": b["en"], "tr": b["tr"], "short_en": b["short_en"], "short_tr": b["short_tr"],
                                 "file": "research/sources/" + b["file"]}
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"appended {len(out)} (topics: {sorted({r['topic'] for r in out})}); ilal.json now {len(d['reasons'])} reasons")


if __name__ == "__main__":
    main()
