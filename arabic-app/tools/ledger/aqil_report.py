"""(v352-A) research/book-coverage-2026-11-27.ibn-aqil.md — Ibn ʿAqīl's ledger by bāb and the engine work order (every ⚠ with its
reproducing example, the book's ruling, the engine's line and the narrowest gate the next round should try).
Run after aqil_toc.py, aqil_ledger.py, aqil_alfiyya.py and tools/ilal/aqil_ilal.py: python3 tools/ledger/aqil_report.py"""
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import aqil_common as A  # noqa: E402
from aqil_map import B  # noqa: E402

ROOT = A.ROOT
OUT = ROOT / "research/book-coverage-2026-11-27.ibn-aqil.md"

GATE = {  # the narrowest gate per bāb, in words — where the next round should look first
    "الابتداء": "MubtadaEngine: the fronted khabar / the indefinite mubtadaʾ with a musawwigh — read the sentence's order before the case",
    "كان وأخواتها": "the naqiṣ verb's ism / khabar when the khabar is fronted or the ism is a pronoun",
    "إن وأخواتها": "inna's khabar when a faṣl / lām al-ibtidāʾ / a fronted ẓarf stands between",
    "ظن وأخواتها": "the two objects of a heart verb when the second is a sentence or a ẓarf (sadd masadd)",
    "الفاعل": "the doer after a verb whose tāʾ or nūn marks gender / number — the agreement rows",
    "النائب عن الفاعل": "the passive verb unvowelled: PassiveEngine needs the written ḍamma — gate on a vowelled form only",
    "اشتغال العامل عن المعمول": "a fronted accusative noun + a verb with its pronoun (زيدا ضربته): «مفعول به لفعل محذوف يفسره المذكور»",
    "الاستثناء": "the noun after إلا: the complete positive sentence (naṣb), the negative (badal or naṣb), the emptied (by the governor)",
    "الحال": "an indefinite accusative participle after a complete sentence whose owner is definite",
    "التمييز": "the accusative after a measure / number / afʿal",
    "حروف الجر": "the jarr letter's meaning row (ابتداء / انتهاء / …) — the line names the letter only",
    "الإضافة": "the muḍāf in a nominal sentence (the jarr reading is right; the office before it is missing)",
    "التوكيد": "نفس / عين / كل / جميع with a pronoun of the noun: «توكيد معنوي»",
    "عطف النسق": "the noun after a coordinating letter whose case follows a non-adjacent noun",
    "البدل": "a noun right after a definite noun of the same case without a coordinating letter",
    "النداء": "يا + a bare name: built on ḍamma «في محل نصب»; the vocative of a muḍāf / a shabīh bil-muḍāf",
    "إعراب الفعل": "the muḍāriʿ after فاء / واو of the answer (حتى، أو) with a hidden أن",
    "عوامل الجزم": "the condition and its answer after إن / من / ما on unvowelled text",
    "التعجب": "ما أفعل + noun: «ما تعجبية … فعل ماض للتعجب … مفعول به»",
    "نعم وبئس وما جرى مجراهما": "نعم / بئس + the doer + the specified noun (المخصوص بالمدح)",
}


def main():
    toc = json.loads((ROOT / "content/rules/toc_ibn_aqil.json").read_text(encoding="utf-8"))
    led = json.loads((ROOT / "content/rules/coverage_ibn_aqil.json").read_text(encoding="utf-8"))
    alf = json.loads((ROOT / "content/rules/alfiyya.json").read_text(encoding="utf-8"))
    il = json.loads((ROOT / "content/rules/ilal.json").read_text(encoding="utf-8"))
    E = led["entries"]
    L = []
    c = toc["counts"]
    L += ["# Ibn ʿAqīl on the Alfiyya — coverage (v352-A, 2026-11-27)", "",
          "Source `%s` (Shamela 9904, 1,329 pages; the editor Muḥyī al-Dīn ʿAbd al-Ḥamīd's «منحة الجليل» in the notes of vols 1–2, his "
          "appendix «تكملة في تصريف الأفعال» kept out). Built by `tools/ledger/aqil_toc.py` → `aqil_ledger.py` → `aqil_alfiyya.py` → "
          "`tools/ilal/aqil_cut.py` / `aqil_ilal.py` → `aqil_report.py`." % A.REL, "",
          "## The book structured", "",
          "%d bābs; **%d verses of the Alfiyya** against the received 1,002 (gap %+d — %s); %d commentary units; %d shawāhid lines "
          "(%d numbers of the edition); %d examples «نحو …»." % (c["babs"], c["verses"], c["gap"], toc["gap_note"], c["units"], c["shawahid"],
                                                                c["shawahid_numbered"], c["examples"]), "",
          "## The ledger by bāb", "",
          "Statuses: **joined** = the same rule in Shudhūr / Qawāʿid / Iẓhār / Kāfiya (inherits its status); **applied** = the book's own "
          "example read right by the engines in the page (+ offered: beside another reading; + vowelled: read right once vowelled — v355); **⚠** = the engine misreads the book's "
          "example; **open** = no construction the iʿrāb line names, a single word cited, or a ṣarf bāb; **n-a** = not automatable "
          "(usage / rarity, a school's view, a dialect, a matter of meaning).", "",
          "| bāb | verses | entries | joined | applied (offered, vowelled) | ⚠ | open | n-a |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    vb = Counter({b["bab"]: len(b["verses"]) for b in toc["babs"]})
    T = Counter()
    for b in toc["babs"]:
        es = [e for e in E if e["bab"] == b["bab"]]
        k = Counter("joined" if "joined" in e else "warn" if e.get("warn") else e["status"] for e in es)
        off = sum(1 for e in es if e.get("offered") and "joined" not in e)
        vw = sum(1 for e in es if e.get("vowelled") and "joined" not in e)
        row = dict(v=vb[b["bab"]], n=len(es), j=k["joined"], a=k["applied"], o=off, vw=vw, w=k["warn"], op=k["open"], na=k["not-automatable"])
        for x, y in row.items():
            T[x] += y
        L.append("| %s | %d | %d | %d | %d (%d, %d) | %d | %d | %d |" % (b["bab"], row["v"], row["n"], row["j"], row["a"], row["o"], row["vw"], row["w"], row["op"], row["na"]))
    L.append("| **all** | %d | %d | %d | %d (%d, %d) | %d | %d | %d |" % (T["v"], T["n"], T["j"], T["a"], T["o"], T["vw"], T["w"], T["op"], T["na"]))
    jb = Counter(e["joined"]["book"] for e in E if "joined" in e)
    L += ["", "Joined to: " + ", ".join("%s %d" % kv for kv in jb.most_common()) + ". Joins need the same topic and the same example "
          "(or ≥ 3 shared content words): Ibn ʿAqīl restates the matns in his own words and examples, so most of his rule sentences stand as "
          "his own rows here.", ""]
    nv = [v for v in alf if v["notes"]]
    L += ["## The Alfiyya on the notes", "",
          "%d verses joined to %d grammar notes (`content/rules/alfiyya.json`; the «Elfiye» card: the bayt, its bāb and number, Ibn ʿAqīl's "
          "ruling verbatim, our rendering on %d of them, the rest Arabic-only). «Beyti bul» (Level 4): the ruling → its verse among three "
          "of the same bāb." % (len(nv), len({g for v in nv for g in v["notes"]}), sum(1 for v in nv if v.get("en"))), ""]
    ra = [r for r in il["reasons"] if r["book"].startswith("ibn-aqil")]
    L += ["## Reasons appended to `ilal.json`", "",
          "%d reasons (Ibn ʿAqīl %d, the editor %d) on %d topics: %s. Why the fāʿil is rafʿ and the mafʿūl naṣb: neither Ibn ʿAqīl nor his "
          "editor states it (searched: فرقا / للفرق / لأن near الفاعل / المفعول) — still open." % (
              len(ra), sum(1 for r in ra if r["book"] == "ibn-aqil"), sum(1 for r in ra if r["book"] == "ibn-aqil-editor"),
              len({r["topic"] for r in ra}), ", ".join(sorted({r["topic"] for r in ra}))), ""]
    L += ["## Engine work order — every ⚠", "",
          "Each row: the entry, the book's example as printed (unvowelled — the probe reads it as given), what the book rules (the bāb's "
          "construction, or the role the sentence names on a word), the engine's line. Per bāb the narrowest gate to try first.", ""]
    for b in toc["babs"]:
        ws = [e for e in E if e["bab"] == b["bab"] and e.get("warn")]
        if not ws:
            continue
        L += ["### %s (%d)" % (b["bab"], len(ws)), "", "Gate: " + GATE.get(b["bab"], "the bāb's construction (`aqil_map.py`: %s)" % (B.get(b["bab"], {}).get("role") or "—")), ""]
        for e in ws:
            p = [x for x in e["probes"] if not x["ok"]][0]
            want = ("«%s» on %s" % (p["re"], p["w"])) if p.get("w") else "«%s» on some word" % p["any"]
            L.append("- %s (p. %s, Shamela %d) — «%s» — wants %s — engine: %s" % (e["id"], e["page"], e["shamela"], p["s"], want, p["got"][:160].replace("|", "/"))
                     + (" — vowelled «%s»: %s" % (p["sv"], p.get("svgot", "")[:160].replace("|", "/")) if p.get("sv") else "")
                     + (" — triage %s: %s" % (e["triage"]["cls"], e["triage"]["why"]) if e.get("triage") else ""))
        L.append("")
    tri = [e for e in E if e.get("triage")]
    if tri:   # (v355) the engine round's triage of the ⚠ rows (tools/ledger/aqil_overrides*.json): a artefact, b real gap, c probe / cut wrong, d not decidable
        L += ["## The v355 triage of the ⚠ rows", "", "a = the print's artefact (read right once vowelled), b = a real gap (fixed or still ⚠), c = the probe's expectation or the cut was "
              "wrong (replaced), d = not decidable from the letters / not an example (now not-automatable or open). Counts: " + ", ".join(
              "%s %d" % kv for kv in sorted(Counter(e["triage"]["cls"] for e in tri).items())) + " — now: " + ", ".join(
              "%s %d" % kv for kv in sorted(Counter(e["triage"]["cls"] + "→" + ("⚠" if e.get("warn") else e["status"] + ("-vowelled" if e.get("vowelled") else "")) for e in tri).items())), ""]
        for e in tri:
            if e["triage"]["cls"] in "cd":
                L.append("- %s (%s) %s — %s" % (e["id"], e["bab"], e["triage"]["cls"], e["triage"]["why"]))
        L.append("")
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("wrote", OUT, len(L), "lines; totals", dict(T))


if __name__ == "__main__":
    main()
