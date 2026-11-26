"""(v352-A) Ibn ʿAqīl structured by script → content/rules/toc_ibn_aqil.json.

  python3 tools/ledger/aqil_toc.py

Every bāb (the page headers' [section]) with its page span; inside it the Alfiyya's verses (numbered 1… in book order), the
commentary units (a group of consecutive verses + the prose that follows it up to the next group: its page span and its
examples), the shawāhid (the edition's number, or null where the line carries none — the 2nd verse of a shāhid, a verse brought
without a number) and the examples «نحو …». Every `ar` is a verbatim substring of the source (the smoke check proves it)."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aqil_common as A  # noqa: E402

OUT = A.ROOT / "content/rules/toc_ibn_aqil.json"
EX = re.compile(r"(?:^|\s)نحو:?\s+([^.،؛:\n()\[\]{}«»\"]+)")
STOP = re.compile(r"\s(?:و?نحو|و?كذلك|و?كذا|فإن|فلا|ولا تقول|وقد|وهو|وهي|أي|لأن|وإن|ف[ـ]?)\s")


def examples(prose, base, sp):
    out = []
    for m in EX.finditer(prose):
        s = m.group(1)
        c = STOP.search(" " + s + " ")
        if c:
            s = (" " + s)[:c.start()].strip()
        w = s.split()
        if not w:
            continue
        s = " ".join(w[:8])
        a = prose.find(s, m.start(1))
        if a < 0:
            continue
        out.append({"ar": s, "sp": sp, "off": base + a})
    return out


def main():
    t, ps = A.pages()
    rows = A.matn_lines(t, ps)
    cls = A.classify(rows)
    expected = 1002
    babs, cur, unit = [], None, None
    n_v = 0
    for i, (p, off, ln) in enumerate(rows):
        if cur is None or (cur["bab"] != p["sec"] and cur["bab"] != "مقدمة الناظم"):
            cur = {"bab": p["sec"], "from": {"shamela": p["sp"], "page": "%d:%d" % (p["vol"], p["pp"])}, "verses": [],
                   "units": [], "shawahid": [], "examples": []}
            cur["to"] = dict(cur["from"])
            babs.append(cur)
            unit = None
        cur["to"] = {"shamela": p["sp"], "page": "%d:%d" % (p["vol"], p["pp"])}
        c = cls[i]
        if c == "alf" and n_v == 0 and not cur["verses"] and "كلامنا لفظ" not in ln and cur["bab"] != "مقدمة الناظم":
            cur["bab"] = "مقدمة الناظم"   # the khuṭba's verses, before «كلامنا لفظ مفيد»: the page header names the first bāb
        if c == "alf" and cur["bab"] == "مقدمة الناظم" and "كلامنا لفظ" in ln:
            cur = {"bab": p["sec"], "from": {"shamela": p["sp"], "page": "%d:%d" % (p["vol"], p["pp"])}, "verses": [],
                   "units": [], "shawahid": [], "examples": []}
            cur["to"] = dict(cur["from"])
            babs.append(cur)
            unit = None
        if c == "alf":
            ar, o = A.verse_text(rows, cls, i)
            ar = re.sub(r"\s*\([٠-٩]+\)\s*$", "", ar)
            n_v += 1
            v = {"n": n_v, "ar": ar, "sp": p["sp"], "page": "%d:%d" % (p["vol"], p["pp"]), "off": o}
            cur["verses"].append(v)
            if unit is None or unit.get("_prose"):
                unit = {"verses": [], "from": p["sp"], "to": p["sp"], "examples": 0, "chars": 0}
                cur["units"].append(unit)
            unit["verses"].append(n_v)
        elif c in ("shahid", "shahid+"):
            m = re.match(r"^([٠-٩]+)\s*-\s*", ln)
            ar = ln[m.end():].strip() if m else ln.strip()
            cur["shawahid"].append({"n": int(m.group(1).translate(A.A2L)) if m else None, "ar": ar, "sp": p["sp"]})
        elif c is None and ln.strip():
            ex = examples(ln, off, p["sp"])
            cur["examples"].extend(ex)
            if unit is not None:
                unit["_prose"] = True
                unit["to"] = p["sp"]
                unit["examples"] += len(ex)
                unit["chars"] += len(ln)
    for b in babs:
        for u in b["units"]:
            u.pop("_prose", None)
        for e in b["examples"]:
            e.pop("off", None)
        for v in b["verses"]:
            v.pop("off", None)
    babs = [b for b in babs if b["verses"] or b["examples"] or b["shawahid"]]
    nv = sum(len(b["verses"]) for b in babs)
    doc = {
        "book": "Sharḥ Ibn ʿAqīl ʿalā Alfiyyat Ibn Mālik (ed. Muḥammad Muḥyī al-Dīn ʿAbd al-Ḥamīd)",
        "source_file": A.REL, "built_by": "tools/ledger/aqil_toc.py",
        "about": "bāb = the page headers' [section]; verses = the Alfiyya's naẓm told from the prose and the shawāhid by script "
                 "(tools/ledger/aqil_common.py: «…» lines, the editor's footnote mark, the edition's shāhid numbers, the rajaz's "
                 "inner rhyme, six verses read by hand); n = the verse's place in the book. units = a verse group and the "
                 "commentary that follows it. Every ar is a verbatim substring of the source.",
        "counts": {"babs": len(babs), "verses": nv, "alfiyya_expected": expected, "gap": nv - expected,
                   "units": sum(len(b["units"]) for b in babs),
                   "shawahid": sum(len(b["shawahid"]) for b in babs),
                   "shawahid_numbered": len({s["n"] for b in babs for s in b["shawahid"] if s["n"]}),
                   "examples": sum(len(b["examples"]) for b in babs)},
        "gap_note": "the e-text gives %d verse lines against the Alfiyya's received 1,002 (+%d). Where a line of the e-text holds the end "
                    "of one verse and the start of the next (pp. 708–709, 841, 1106, 1130, 1255) the count follows the lines; "
                    "the Shamela text's verse lines were not checked against a printed Alfiyya." % (nv, nv - expected),
        "babs": babs,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(doc["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
