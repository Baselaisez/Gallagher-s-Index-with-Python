"""(v352-A) Ibn ʿAqīl's ledger → content/rules/coverage_ibn_aqil.json (+ research/book-coverage-2026-11-27.ibn-aqil.md).

  python3 tools/ledger/aqil_ledger.py            # cut, join, prove in prototype/reader.html (tools/ledger/aqil_prove.js), write
  python3 tools/ledger/aqil_ledger.py --no-prove # reuse tools/ledger/.aqil-proof-cache.json

One entry per RULE STATEMENT of the commentary: a sentence of Ibn ʿAqīl's prose (not the naẓm, not a shāhid, not the editor's
notes or appendix) that states a ruling (يجب / يجوز / يمتنع / يلزم / يرفع / ينصب / … / لا تقول) and gives its example (نحو / تقول /
كقولك). Its status, in this order:
  joined           — the SAME rule in the Shudhūr / Qawāʿid / Iẓhār / Kāfiya ledgers (same topic — commentary_links.json — and the
                     same example, or ≥ 3 shared content words and a Jaccard ≥ .3): it inherits that entry's status, not re-proved;
  not-automatable  — a ruling of usage the engine does not decide: poetic licence / rarity, a school's view, a dialect, a matter of
                     meaning (the marker is named in `reason`);
  open (ṣarf)      — a bāb of word-form: for the ṣarf ledgers, not read by the iʿrāb probe;
  applied          — the book's own example through SentenceAnalyzer + Murib.line names the ruling (the word the sentence names, or
                     the bāb's construction on some word); applied-offered when the line gives it beside another reading;
  open ⚠           — the engine misreads the book's example: its line is kept beside the book's (`got`);
  open             — no construction the iʿrāb line names.
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import aqil_common as A  # noqa: E402
from aqil_map import B, EDITOR, NAMED  # noqa: E402

ROOT = A.ROOT
OUT = ROOT / "content/rules/coverage_ibn_aqil.json"
# (v355) the engine round's triage, row by row: tools/ledger/aqil_overrides*.json (one file per agent, merged here) —
#   {"A561.1": {"cls": "a|b|c|d", "why": "…", "probes": [{s, sv?, w?, re? | any?}], "status"?, "reason"?}}.
#   s stays the book's example AS PRINTED (verbatim in the sentence); sv is the same example vowelled — the vowels are OURS, for the
#   test only, never shown to a learner (taken from the editor's iʿrāb where he gives one). A row whose printed probe fails and whose
#   vowelled probe passes counts «applied-vowelled». cls c = the probe's expectation or the cut was wrong (the probe is replaced, the
#   reason in `why`); cls d = not decidable from the letters / not an example (status + reason).
OVR = {}
for _f in sorted(HERE.glob("aqil_overrides*.json")):
    OVR.update(json.loads(_f.read_text(encoding="utf-8")))
# (v355-N1) the pillars' triage keeps its own file shape (tools/ledger/aqil_triage_*.json: {"rows": {id: {class, why, probes | reason}}} —
#   the check «v355-N1 — the work order's triage» reads it); it is the same judgement and goes through the same road
for _f in sorted(HERE.glob("aqil_triage_*.json")):
    for _k, _v in json.loads(_f.read_text(encoding="utf-8"))["rows"].items():
        assert _k not in OVR, "two triage files claim " + _k
        OVR[_k] = ({"cls": "d", "status": "not-automatable", "reason": _v["reason"]} if _v["class"] == "d"
                   else {"cls": _v["class"], "why": _v.get("why", ""), "probes": _v["probes"], "free": True})
CACHE = HERE / ".aqil-proof-cache.json"
CACHE_SV = HERE / ".aqil-proof-cache-sv.json"   # (v355) the vowelled probes, proved in a page of their own: a page that has read the
#   printed letters first answers the vowelled reading of the same letters differently (a state the engine keeps — named in v355-N2)
LEDGERS = {"shudhur": "coverage_shudhur.json", "qawaid": "coverage_qawaid_al_irab.json", "izhar": "coverage_izhar.json",
           "kafiya": "coverage_kafiya.json"}

RUL = re.compile(r"يجب|وجب|يجوز|جاز|يمتنع|امتنع|يلزم|لزم|يشترط|شرط|حكم|يرفع|ترفع|ينصب|تنصب|يجر|تجر|يجزم|تجزم|يبني|تبني|"
                 r"مبني|يعرب|تعرب|معرب|يعمل|تعمل|يتعين|تعين|يحذف|حذف|يقدم|تقديم|يؤخر|تاخير|لا تقول|فلا تقول|رفع|نصب|جر|جزم")
EXM = re.compile(r"(?:^|\s)(?:و?نحو|و?كقولك|فتقول|وتقول|تقول)\s*:?\s+")
NA = [(re.compile(r"ضروره|الشعر|شذوذا|شاذ|نادر|قليل|يحفظ ولا يقاس"), "a report of usage — poetic licence / rarity: the engine reads, it does not decide what is rare"),
      (re.compile(r"الكوفي|البصري|سيبويه|الاخفش|الفراء|الكسايي|المبرد|مذهب|خلاف|زعم|اجاز|منع "), "a school's view (khilāf): the engine follows no school here"),
      (re.compile(r"لغه|لغات|بني تميم|الحجازيين|تميم|طيي"), "a dialect report"),
      (re.compile(r"المعني|معناه|بمعني|قصدت|اردت|يقصد|اريد"), "a matter of meaning: the choice is the writer's")]
STOPW = {"اي", "فان", "فلا", "وهو", "وهي", "وكذلك", "لان", "ف", "وقد", "فهو", "فهي", "فتقول", "وتقول", "واحترز", "فليس", "فالاول",
         "والثاني", "فيجب", "فيجوز", "ولا", "وكذا", "كذلك", "فيه", "بخلاف"}
FUNC = {"في", "من", "علي", "الي", "عن", "ان", "او", "ثم", "لا", "ما", "لم", "قد", "هو", "هي", "ذلك", "هذا", "التي", "الذي", "كان", "نحو",
        "كقولك", "تقول", "قوله", "وهو", "وقد", "فان", "اذا", "لان", "بل", "مع", "كل", "غير", "اي", "به", "له", "الا", "ولا", "او", "اذ"}


def toks(s):
    return re.sub(r"[^ء-ي ]", " ", A.norm(s)).split()


TERM = {"مبتدا", "خبر", "خبره", "خبرها", "فاعل", "فاعله", "مفعول", "مفعوله", "رفع", "نصب", "جر", "جزم", "الرفع", "النصب", "الجر",
        "الجزم", "المختار", "منه", "قولهم", "قوله", "قول", "اشار", "الا", "لكن", "الاصل", "غير", "الامر", "الماضي", "المضارع", "التقدير",
        "يتعين", "كون", "تقديره", "اصله", "اصلها", "المصنف", "الشاعر", "تعالي", "اسم", "حرف", "فعل", "الفعل", "الاسم", "عطف",
        "حال", "نعت", "تمييز", "بدل", "توكيد", "اليه", "يجوز", "يجب", "جاز", "وجب", "امتنع", "يمتنع", "مثال", "الاول", "الثاني",
        "مذهب", "عند", "فيمن", "فيما", "لغه", "يقال", "قيل", "ذلك", "هذا", "هذه", "اذ", "لانه", "لانها", "فانه",
        "مثل", "كقولك", "تقول", "نحو", "ومنه", "النون", "الالف", "الياء", "الواو", "التاء", "الهمزه", "الضمه", "الفتحه", "الكسره"}


def _bare_tok(n):
    for pre in ("و", "ف", "ب"):
        if n.startswith(pre) and n[1:] in TERM:
            return n[1:]
    return n


def cut_example(seg):
    """the example as printed, cut where the commentary resumes («فزيد مبتدأ», «أي», «فإن» …) — a verbatim prefix of seg."""
    words = seg.split()
    out, seen = [], set()
    for w in words:
        n = A.norm(re.sub(r"[^ء-يً-ْ]", "", w))
        if out and (_bare_tok(n) in TERM or n in ("او", "ام")):
            break
        if not n or n in STOPW or (n.startswith(("ف", "و")) and n[1:] in seen) or re.search(r"[.،؛:{}()\[\]«»\"]", w) and out:
            if re.search(r"[.،؛:]$", w) and n and n not in STOPW:
                out.append(w.rstrip(".،؛:"))
            break
        out.append(w)
        seen.add(n)
        if len(out) >= 8:
            break
    s = " ".join(out).strip(" ،.:")
    return s if seg.startswith(s) else None


def examples(sent):
    out = []
    for m in EXM.finditer(sent):
        e = cut_example(sent[m.end():])
        if e and len(toks(e)) >= 1 and not e.startswith(("قوله", "قول")):
            out.append(e)
    return out


def named_probes(sent, exs):
    """«فزيد مبتدأ وقائم خبره» → [(word, engine regex)] for words of the example."""
    out = []
    ex_words = {A.norm(w): w for e in exs for w in e.split()}
    tail = A.norm(sent)
    for rn, eng in NAMED:
        for m in re.finditer(r"(?:^|\s)(?:ف([ء-ي]+)\s*:?|([ء-ي]+)\s*:)\s*(?:%s)(?:[^ء-ي]|$)" % rn, tail):
            w = m.group(1) or m.group(2)
            for c in (w, w[1:] if w[:1] in "فو" and not m.group(1) else None):
                if c and c in ex_words and c not in FUNC:
                    out.append((ex_words[c], eng))
                    break
    return out


def load_ledgers():
    links = json.loads((ROOT / "content/rules/commentary_links.json").read_text(encoding="utf-8"))["links"]
    tp = {x["topic"]: x["topics"] for x in links if x["topic"].startswith("ledger:")}
    out = []
    for k, f in LEDGERS.items():
        d = json.loads((ROOT / "content/rules" / f).read_text(encoding="utf-8"))
        kk = {"qawaid": "qawaid"}.get(k, k)
        for e in d["entries"]:
            if e["status"] in ("heading", "fragment", "example"):
                continue
            txt = e["ar"] + " " + " ".join(p.get("s", "") for p in e.get("probes", []))
            out.append({"book": k, "id": e["id"], "status": e["status"], "topics": set(tp.get("ledger:%s:%s" % (kk, e["id"]), [])),
                        "norm": " ".join(toks(txt)), "words": {w for w in toks(e["ar"]) if len(w) >= 3 and w not in FUNC}})
    return out


RANK = {"applied": 0, "noted": 1, "not-automatable": 2, "open": 3}


def join(ent, topics, ledgers):
    best = None
    ex = [" ".join(toks(e)) for e in ent["ex"] if len(toks(e)) >= 2]
    mine = {w for w in toks(ent["ar"]) if len(w) >= 3 and w not in FUNC}
    for L in ledgers:
        if not (L["topics"] & set(topics)):
            continue
        sc = 0
        if any(e and (" " + e + " ") in (" " + L["norm"] + " ") for e in ex):
            sc = 2
        else:
            sh = mine & L["words"]
            if len(sh) >= 3 and len(sh) / len(mine | L["words"]) >= 0.3:
                sc = 1
        if sc and (best is None or (sc, -RANK.get(L["status"], 9)) > (best[0], -RANK.get(best[1]["status"], 9))):
            best = (sc, L)
    return best


def cut_entries():
    t, ps = A.pages()
    rows = A.matn_lines(t, ps)
    cls = A.classify(rows)
    ents = []
    for i, (p, off, ln) in enumerate(rows):
        if cls[i] or not ln.strip() or p["sec"] in EDITOR or p["sec"] not in B or ln.startswith("="):
            continue
        k = 0
        for a, s in A.sentences(ln):
            ns = A.norm(s)
            if not RUL.search(ns) or not EXM.search(s):
                continue
            exs = examples(s)
            if not exs:
                continue
            k += 1
            assert t[off + a: off + a + len(s)] == s
            ents.append({"id": "A%d.%d" % (p["sp"], len([e for e in ents if e["shamela"] == p["sp"]]) + 1), "bab": p["sec"],
                         "page": "%d:%d" % (p["vol"], p["pp"]), "shamela": p["sp"], "ar": s, "ex": exs})
    return ents


def main():
    prove = "--no-prove" not in sys.argv
    ents = cut_entries()
    ledgers = load_ledgers()
    probes, svprobes = [], []
    for e in ents:
        m = B[e["bab"]]
        e["topics"] = m["topics"]
        j = join(e, m["topics"], ledgers)
        ns = A.norm(e["ar"])
        if j:
            e["status"], e["joined"] = j[1]["status"], {"book": j[1]["book"], "id": j[1]["id"], "by": "example" if j[0] == 2 else "words"}
            continue
        na = next((r for rx, r in NA if rx.search(ns)), None)
        if m["sarf"]:
            e["status"], e["reason"] = "open", "ṣarf — a bāb of word-form, for the ṣarf ledgers (not read by the iʿrāb probe)"
            e["sarf"] = True
            continue
        if na:
            e["status"], e["reason"] = "not-automatable", na
            continue
        if not m["role"]:
            e["status"], e["reason"] = "open", "no construction the iʿrāb line names"
            continue
        nm = named_probes(e["ar"], e["ex"])
        multi = [x for x in e["ex"] if len(x.split()) >= 2]
        if not nm and not multi:
            e["status"], e["reason"] = "open", "a single word cited — the ruling is on its form, no sentence for the iʿrāb probe"
            continue
        ex0 = (multi or e["ex"])[0]
        if nm:
            e["probes"] = [{"s": next((x for x in e["ex"] if w in x.split()), ex0), "w": w, "re": rg} for w, rg in nm[:3]]
        else:
            e["probes"] = [{"s": ex0, "any": m["role"]}]
        o = OVR.get(e["id"])
        if o:
            e["triage"] = {"cls": o["cls"], "why": o.get("why", "")}
            if o.get("status"):
                e["status"], e["reason"] = o["status"], o["reason"]
                e.pop("probes", None)
                continue
            if o.get("probes"):
                e["probes"] = [dict(p) for p in o["probes"]]
            elif o.get("sv"):
                for p in e["probes"]:
                    p["sv"] = o["sv"]
            for p in e["probes"]:   # an override's sentence is the entry's own words; a triage file's corrected probe (class c) may be the
                assert o.get("free") or p["s"] in e["ar"], (e["id"], p["s"])   # book's fuller sentence from the same page — its `why` says so
        for p in e["probes"]:
            p["_k"] = len(probes)
            probes.append({k: v for k, v in p.items() if k not in ("_k", "sv")})
            if p.get("sv"):
                p["_kv"] = len(svprobes)
                svprobes.append(dict({k: v for k, v in p.items() if k not in ("_k", "_kv", "sv")}, s=p["sv"]))
    if prove:
        pin = HERE / ".aqil-probes.json"
        pin.write_text(json.dumps(probes, ensure_ascii=False), encoding="utf-8")
        subprocess.run(["node", str(HERE / "aqil_prove.js"), str(pin), str(CACHE)], check=True)
        pin.write_text(json.dumps(svprobes, ensure_ascii=False), encoding="utf-8")
        subprocess.run(["node", str(HERE / "aqil_prove.js"), str(pin), str(CACHE_SV)], check=True)
        pin.unlink()
    res = json.loads(CACHE.read_text(encoding="utf-8"))
    ress = json.loads(CACHE_SV.read_text(encoding="utf-8")) if svprobes else []
    assert len(res) == len(probes) and len(ress) == len(svprobes), "proof cache is stale: run without --no-prove"
    for e in ents:
        if "probes" not in e:
            continue
        for p in e["probes"]:
            r = res[p.pop("_k")]
            p["ok"], p["got"] = r["ok"], r["got"][:200]
            if r.get("offered"):
                p["offered"] = True
            if "_kv" in p:
                rv = ress[p.pop("_kv")]
                p["svok"], p["svgot"] = rv["ok"], rv["got"][:200]
                if not r["ok"] and rv["ok"]:
                    p["vowelled"] = True
                    p.pop("offered", None)
                    if rv.get("offered"):
                        p["offered"] = True
        if all(p["ok"] or p.get("svok") for p in e["probes"]):
            e["status"] = "applied"
            if any(p.get("offered") for p in e["probes"]):
                e["offered"] = True
            if any(p.get("vowelled") for p in e["probes"]):
                e["vowelled"] = True
        else:
            e["status"], e["warn"] = "open", True
    counts = Counter()
    by = defaultdict(Counter)
    for e in ents:
        k = "joined" if "joined" in e else ("warn" if e.get("warn") else e["status"] + ("-offered" if e.get("offered") else "") + ("-vowelled" if e.get("vowelled") else ""))
        counts[k] += 1
        counts["status:" + e["status"]] += 1
        by[e["bab"]][k] += 1
        by[e["bab"]]["entries"] += 1
    doc = {"book": "Sharḥ Ibn ʿAqīl ʿalā Alfiyyat Ibn Mālik", "source_file": A.REL, "built_by": "tools/ledger/aqil_ledger.py",
           "about": __doc__.split("\n\n", 1)[1].strip(),
           "counts": dict(sorted(counts.items())), "by_bab": {k: dict(v) for k, v in by.items()}, "entries": ents}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(ents), json.dumps(doc["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
