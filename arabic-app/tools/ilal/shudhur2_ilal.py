"""(v360-Sh) APPEND the Sharḥ Shudhūr's own reasons (tools/ilal/shudhur2_kept.json — the hand reading of the unread half's «لأن …»
sentences) to content/rules/ilal.json in its exact shape. Idempotent: the rows it wrote before (id «ilal-shudhur2-…») are replaced at
the end, every other row is kept in place and in order (append only). Refuses any `ar` that is not on its Shamela page of
research/sources/sharh-shudhur-al-dhahab-src.txt. Run AFTER tools/ilal/build_ilal.py and tools/ilal/aqil_ilal.py.
Run: python3 tools/ilal/shudhur2_ilal.py"""
import json, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ledger"))
import shudhur2_common as C  # noqa: E402
from build_ilal import why_at  # noqa: E402

ROOT = Path(C.ROOT)
REL = "research/sources/sharh-shudhur-al-dhahab-src.txt"
BOOKS = {"shudhur-sharh": {"ar": "شرح شذور الذهب في معرفة كلام العرب لابن هشام الأنصاري (تحقيق عبد الغني الدقر)",
                           "en": "Ibn Hishām, Sharḥ Shudhūr al-Dhahab", "tr": "İbn Hişâm, Şerhu Şüzûri'z-Zeheb",
                           "short_en": "Ibn Hishām (Shudhūr)", "short_tr": "İbn Hişâm (Şüzûr)", "file": REL}}
KINDS = ("why-state", "why-sign", "why-built", "why-form", "why-order", "objection")


def main():
    p = ROOT / "content/rules/ilal.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    kept = json.loads((ROOT / "tools/ilal/shudhur2_kept.json").read_text(encoding="utf-8"))["kept"]
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))["links"]
    led = json.loads((ROOT / "content/rules/coverage_shudhur_sharh.json").read_text(encoding="utf-8"))["entries"]
    notes_of = {}
    for x in links:
        if x["topic"].startswith("note:"):
            for t in x["topics"]:
                notes_of.setdefault(t, []).append(x["topic"][5:])
    pages = {sh: (pr, sec, "\n".join(ls)) for sh, pr, sec, ls in C.P()}
    rows, bad, seen = [], [], Counter()
    for k in kept:
        assert k["kind"] in KINDS, k
        pr, sec, body = pages[k["shamela"]]
        if k["ar"] not in body or pr != k["web_page"]:
            bad.append("p.%d: ar is not on its page — %s" % (k["shamela"], k["ar"][:40])); continue
        seen[k["shamela"]] += 1
        words = len(re.findall(r"[ء-ي]+", k["ar"]))
        r = {"id": "ilal-shudhur2-%d-%d" % (k["shamela"], seen[k["shamela"]]), "topic": k["topic"], "kind": k["kind"], "ar": k["ar"],
             "book": "shudhur-sharh", "vol_page": str(pr), "shamela_page": k["shamela"], "section": sec, "en": k["en"], "tr": k["tr"]}
        r["notes"] = notes_of.get(k["topic"], [])[:8]
        r["ledger"] = ["shudhur-sharh:" + e["id"] for e in led if e["shamela"] == k["shamela"]][:8]
        r["words"] = words
        w = why_at(k["ar"])
        if w is not None:
            r["why_at"] = w
        r["short"] = words <= 25
        rows.append(r)
    if bad:
        raise SystemExit("shudhur2_ilal: refused —\n  " + "\n  ".join(bad))
    doc["reasons"] = [r for r in doc["reasons"] if not r["id"].startswith("ilal-shudhur2-")] + rows
    doc["books"].update(BOOKS)
    out = doc["reasons"]
    doc["counts"] = {"reasons": len(out), "by_book": dict(Counter(r["book"] for r in out)), "by_kind": dict(Counter(r["kind"] for r in out)),
                     "rendered": sum(1 for r in out if "en" in r), "short": sum(1 for r in out if r.get("short")),
                     "topics": len({r["topic"] for r in out}), "notes_reached": len({n for r in out for n in r.get("notes", [])})}
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(rows), "appended;", json.dumps(doc["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
