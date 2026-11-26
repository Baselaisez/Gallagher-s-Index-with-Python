"""(v352-A) APPEND Ibn ʿAqīl's reasons (tools/ilal/aqil_kept.json, the hand reading of research/ilal/candidates-ibn-aqil.json) to
content/rules/ilal.json in its exact shape. Idempotent: the rows it wrote before (id «ilal-aqil-…») are replaced, every other row is
kept in place and in order. Refuses any `ar` that is not on its Shamela page (matn + the editor's notes). Run AFTER
tools/ilal/build_ilal.py (which rewrites the file from v348-F's reading alone).
Run: python3 tools/ilal/aqil_ilal.py"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ledger"))
import aqil_common as A  # noqa: E402
from build_ilal import why_at  # noqa: E402

ROOT = A.ROOT
BOOKS = {
    "ibn-aqil": {"ar": "شرح ابن عقيل على ألفية ابن مالك", "en": "Ibn ʿAqīl, Sharḥ al-Alfiyya", "tr": "İbn Akîl, Şerhu'l-Elfiyye",
                 "short_en": "Ibn ʿAqīl", "short_tr": "İbn Akîl", "file": A.REL},
    "ibn-aqil-editor": {"ar": "منحة الجليل بتحقيق شرح ابن عقيل (محمد محيي الدين عبد الحميد)",
                        "en": "Muḥyī al-Dīn ʿAbd al-Ḥamīd, Minḥat al-Jalīl (the editor's notes on Ibn ʿAqīl)",
                        "tr": "Muhyiddin Abdülhamîd, Minhatü'l-Celîl (İbn Akîl'in muhakkiki)", "short_en": "ʿAbd al-Ḥamīd (ed.)",
                        "short_tr": "Abdülhamîd (muhakkik)", "file": A.REL},
}
KINDS = ("why-state", "why-sign", "why-built", "why-form", "why-order", "objection")


def main():
    p = ROOT / "content/rules/ilal.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    kept = json.loads((ROOT / "tools/ilal/aqil_kept.json").read_text(encoding="utf-8"))["kept"]
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))["links"]
    led = json.loads((ROOT / "content/rules/coverage_ibn_aqil.json").read_text(encoding="utf-8"))["entries"]
    notes_of = {}
    for x in links:
        if x["topic"].startswith("note:"):
            for t in x["topics"]:
                notes_of.setdefault(t, []).append(x["topic"][5:])
    t, ps = A.pages()
    bysp = {q["sp"]: q for q in ps}
    rows, bad, seen = [], [], Counter()
    for k in kept:
        assert k["kind"] in KINDS, k
        q = bysp[k["sp"]]
        part = t[q["start"]:q["matn_end"]] if k["book"] == "ibn-aqil" else t[q["matn_end"]:q["end"]]
        if k["ar"] not in part:
            bad.append("p.%d: ar is not in its page's %s — %s" % (k["sp"], "matn" if k["book"] == "ibn-aqil" else "notes", k["ar"][:40]))
            continue
        seen[k["sp"]] += 1
        words = len(re.findall(r"[ء-ي]+", k["ar"]))
        r = {"id": "ilal-aqil-%d-%d" % (k["sp"], seen[k["sp"]]), "topic": k["topic"], "kind": k["kind"], "ar": k["ar"],
             "book": k["book"], "vol_page": "%d:%d" % (q["vol"], q["pp"]), "shamela_page": k["sp"], "section": q["sec"]}
        for f in ("role", "cls", "case"):
            if k.get(f):
                r[f] = k[f]
        if k.get("en") and k.get("tr"):
            r["en"], r["tr"] = k["en"], k["tr"]
        r["notes"] = notes_of.get(k["topic"], [])[:8]
        r["ledger"] = ["ibn-aqil:" + e["id"] for e in led if e["shamela"] == k["sp"]][:8]
        r["words"] = words
        w = why_at(k["ar"])
        if w is not None:
            r["why_at"] = w
        r["short"] = words <= 25 and "en" in r
        rows.append(r)
    if bad:
        raise SystemExit("aqil_ilal: refused —\n  " + "\n  ".join(bad))
    doc["reasons"] = [r for r in doc["reasons"] if not r["id"].startswith("ilal-aqil-")] + rows
    doc["books"].update(BOOKS)
    out = doc["reasons"]
    doc["counts"] = {"reasons": len(out), "by_book": dict(Counter(r["book"] for r in out)), "by_kind": dict(Counter(r["kind"] for r in out)),
                     "rendered": sum(1 for r in out if "en" in r), "short": sum(1 for r in out if r["short"]),
                     "topics": len({r["topic"] for r in out}), "notes_reached": len({n for r in out for n in r["notes"]})}
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(rows), "appended;", json.dumps(doc["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
