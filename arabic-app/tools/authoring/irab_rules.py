#!/usr/bin/env python3
"""irab_rules.py — the AI pre-check's CONFIRMED patterns as rule objects over the shipped iʿrāb lines.

    python3 tools/authoring/irab_rules.py [--rule D03] [--write]

Every rule is a class with the same shape: an id (the pattern of the review sheets), the source it stands on (book, file,
line, the rule quoted verbatim), `candidates(sentence)` — where it applies — and `rewrite(token)` — the new trilingual
line, or None when the line is not in a shape the rule knows (then it is reported, never guessed). A rule touches only
what its condition names; everything else in the line and the sentence stays as written.

Without --write it only prints what would change. With --write the chapters are updated and every change is appended
to review/ai-precheck/rule-applied.jsonl (package, place, before, after, rule, source), so the hoca can see exactly
which unreviewed lines a rule changed. Tokens already corrected one by one (review/ai-precheck/applied.jsonl) are left
alone.
"""
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
N = lambda s: unicodedata.normalize("NFC", s or "")
bare = lambda s: re.sub(r"[ً-ْٰـ]", "", N(s))


class IrabRule:
    id = ""; title = ""; source = {}

    def candidates(self, toks):
        """Indexes of the tokens this rule speaks for, in one sentence."""
        return []

    def rewrite(self, tok):
        """The token's new {ar, en, tr}, or None if its line has a shape this rule does not know."""
        return None


class AmmaFaRule(IrabRule):
    """D03 — the fāʾ that opens the answer of أَمَّا is not a conjunction: «الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»»."""
    id = "D03"
    title = "the fāʾ answering أَمَّا"
    source = {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt",
              "locator": "line 104", "quote": "وإن كان المبتدأ بعد أما وجب دخول الفاء في خبره نحو أما زيد فمنطلق"}
    AR_HEAD = re.compile(r"^الْفَاءُ\s+(?:عَاطِفَةٌ|لِلتَّفْرِيعِ|سَبَبِيَّةٌ)\s*،\s*")
    EN_HEAD = re.compile(r"^The fa (?:conjoins|joins|is conjunctive|is causal)[^;,.]*[;,.]\s*", re.I)
    TR_HEAD = re.compile(r"^«bunun üzerine»\s*\+?\s*")

    def candidates(self, toks):
        out = []
        for i, t in enumerate(toks):
            s = bare((t.get("surface") or {}).get("full")).lstrip("وف")
            if s not in ("أما", "اما") or "ّ" not in N((t.get("surface") or {}).get("full")): continue
            for j in range(i + 1, len(toks)):
                u = toks[j]
                if u.get("quoteBefore") or u.get("quoteAfter"): continue          # a fāʾ inside a quotation is not the answer
                line = N((u.get("irab") or {}).get("ar"))
                if not bare(line).startswith("الفاء"): continue                     # فِي, فَوْقَ … are not the fāʾ
                if re.search(r"الْفَاءُ\s+(?:وَاقِعَةٌ|دَاخِلَةٌ|رَابِطَةٌ)", line): break   # already read as the answer
                if j not in out: out.append(j)
                break
        return out

    def rewrite(self, tok):
        ir = tok.get("irab") or {}
        ar, en, tr = N(ir.get("ar")), ir.get("en") or "", ir.get("tr") or ""
        if not self.AR_HEAD.match(ar): return None
        new_ar = self.AR_HEAD.sub("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، ", ar, count=1)
        new_en = self.EN_HEAD.sub("The fa answers «أَمَّا»; ", en, count=1) if self.EN_HEAD.match(en) else "The fa answers «أَمَّا»; " + en
        new_tr = self.TR_HEAD.sub("Fâ «أَمَّا»nın cevabındadır; ", tr, count=1) if self.TR_HEAD.match(tr) else "Fâ «أَمَّا»nın cevabındadır; " + tr
        return {"ar": new_ar, "en": new_en, "tr": new_tr}


RULES = [AmmaFaRule()]


def main():
    write = "--write" in sys.argv
    only = sys.argv[sys.argv.index("--rule") + 1] if "--rule" in sys.argv else None
    import review_batch as rb
    pre = ROOT / "review/ai-precheck"
    done = set()
    if (pre / "applied.jsonl").is_file():
        for l in (pre / "applied.jsonl").read_text(encoding="utf-8").splitlines():
            if l.strip():
                a = json.loads(l); done.add((a["package"], a["where"]))
    log, unknown = [], []
    for p in rb.pending_packages():
        pk = json.loads((p / "manifest.json").read_text(encoding="utf-8"))["id"]
        for f in sorted((p / "chapters").glob("*.json"), key=lambda q: int(q.stem)):
            ch = json.loads(f.read_text(encoding="utf-8")); changed = False
            for sen in ch["sentences"]:
                toks = sen.get("tokens") or []
                for r in RULES:
                    if only and r.id != only: continue
                    for j in r.candidates(toks):
                        where = f"{ch.get('chapter', f.stem)}:{sen['id']}:{j}"
                        if (pk, where) in done: continue
                        new = r.rewrite(toks[j])
                        if new is None: unknown.append((r.id, pk, where, N((toks[j].get("irab") or {}).get("ar"))[:80])); continue
                        log.append({"rule": r.id, "package": pk, "where": where, "surface": N(toks[j]["surface"]["full"]),
                                    "before": dict(toks[j].get("irab") or {}), "after": new, "source": r.source})
                        toks[j]["irab"] = new; changed = True
            if write and changed: f.write_text(json.dumps(ch, ensure_ascii=False, indent=1), encoding="utf-8")
    for c in log: print(f"{c['rule']} {c['package']} {c['where']} {c['surface']}\n   - {c['before'].get('ar', '')[:90]}\n   + {c['after']['ar'][:90]}")
    for u in unknown: print("UNKNOWN SHAPE", *u)
    print(f"{len(log)} lines rewritten, {len(unknown)} left for a reader" + ("" if write else " — dry run"))
    if write and log:
        with open(pre / "rule-applied.jsonl", "a", encoding="utf-8") as fh:
            for c in log: fh.write(json.dumps(c, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
