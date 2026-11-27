"""(v352-U) item 5, step a — cut al-Khaṣāʾiṣ's taʿlīl sentences BY SCRIPT and join each to the app's topics (tools/ilal/concepts.py:
a topic's Arabic regex on the sentence's own words, letters-only), the v348-F way. Writes research/usul/khasais_candidates.json
(every sentence with a taʿlīl marker and a topic, with its page, bāb and offset; the 44 topics v348-F left without a reason first).
The HAND reading is tools/usul/kept_khasais.json; tools/usul/append_ilal.py appends the kept ones to content/rules/ilal.json.
Run: python3 tools/usul/cut_khasais.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ilal"))
from src import ROOT, norm, pages  # noqa: E402
from concepts import C  # noqa: E402

MARK = re.compile(r"(?:^|\s)(?:و|ف)?(?:لان|لانه|لانها|لانهم|وانما|انما|فرقا|للفرق|حملا|لشبه|لمشابهه|لمضارعه|لييلا|لئلا|كراهيه|كراهه|استثقالا|"
                  r"لاستثقال|لثقل|عوضا|تخفيفا|للتخفيف|استخفافا|لكون|لاجل|من اجل|لعله|والعله|علته|العله في)(?=\s|$)")
UNCOVERED = set("abniya alam asma-afal badal five-verbs hadhf hikaya imala ishara ishtighal ism-fail-amal istithna law maani-abwab madh "
                "maful-fih maful-lah maful-mutlaq maqsur-mamdud masdar masdar-amal muarraf mudari-abwab mudmar muqaraba mushtaqqat naib-fail "
                "nasab nida nun-tawkid sakinayn sifa-mushabbaha tafdil tajjub taksir tanazu tanith tasghir tathniya tawkid waqf zaid zann "
                "zawaid".split())


def main():
    t, ps = pages("khasais")
    toc = json.loads((ROOT / "content/rules/toc_khasais.json").read_text(encoding="utf-8"))["babs"]
    bab = lambda sp: next((b for b in toc if b["from"]["shamela"] <= sp <= b["to"]["shamela"]), None)
    rx = [(c["id"], re.compile(c["ar"])) for c in C if c.get("ar")]
    out = []
    for p in ps:
        if p["sp"] > 1265:
            break
        raw = t[p["start"]:p["matn_end"]]
        for m in re.finditer(r"[^.؟!\n]+[.؟!]?", raw):
            s = m.group(0).strip()
            n = norm(s)
            w = len(re.findall(r"[ء-ي]+", n))
            if w < 8 or w > 50 or not MARK.search(n):
                continue
            tops = [cid for cid, r in rx if r.search(n)][:3]
            if not tops:
                continue
            b = bab(p["sp"])
            out.append({"cid": f"khasais:{p['sp']}:{m.start() + (len(m.group(0)) - len(m.group(0).lstrip()))}", "shamela": p["sp"],
                        "vol_page": f"{p['vol']}:{p['pp']}", "bab_n": b and b["n"], "bab": b and b["ar"], "topics": tops,
                        "uncovered": [x for x in tops if x in UNCOVERED], "words": w, "ar": s})
    out.sort(key=lambda c: (not c["uncovered"], c["shamela"]))
    from collections import Counter
    cnt = Counter(x for c in out for x in c["topics"])
    (ROOT / "research/usul").mkdir(parents=True, exist_ok=True)
    (ROOT / "research/usul/khasais_candidates.json").write_text(json.dumps(
        {"built_by": "tools/usul/cut_khasais.py (v352-U)", "counts": {"candidates": len(out), "with_uncovered": sum(1 for c in out if c["uncovered"]),
                                                                     "by_topic": dict(cnt.most_common())}, "candidates": out},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(out), sum(1 for c in out if c["uncovered"]), cnt.most_common(70))


if __name__ == "__main__":
    main()
