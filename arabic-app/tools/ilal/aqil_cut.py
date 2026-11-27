"""(v352-A) Ibn ʿAqīl's taʿlīl candidates → research/ilal/candidates-ibn-aqil.json (the v348-F way: every sentence with a reason marker,
matn = Ibn ʿAqīl, hashiya of vols 1–2 = the editor Muḥyī al-Dīn ʿAbd al-Ḥamīd's «منحة الجليل» — cited as the editor's).
Only the bābs whose topic v348-F left with no book reason, + الفاعل / تعدي الفعل (why the fāʿil is rafʿ, the mafʿūl naṣb).
Run: python3 tools/ilal/aqil_cut.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ledger"))
import aqil_common as A  # noqa: E402
from aqil_map import B, EDITOR  # noqa: E402

MARK = re.compile(r"(^|\s)(لأن|لان|لأنه|لانه|لأنها|لانها|وإنما|وانما|العلة|علة|حملا على|للفرق|فرقا|لشبه|لشبهه|لكون|لكونه|لئلا|لثقل|لاستثقال|لخفة|للخفة)(\s|$)")
WANT = set("abniya alam asma-afal badal five-verbs hadhf hikaya imala ishara ishtighal ism-fail-amal istithna law maani-abwab madh "
           "maful-fih maful-lah maful-mutlaq maqsur-mamdud masdar masdar-amal muarraf mudari-abwab mudmar muqaraba mushtaqqat naib-fail "
           "nasab nida nun-tawkid sakinayn sifa-mushabbaha tafdil tajjub taksir tanazu tanith tasghir tathniya tawkid waqf zaid zann "
           "zawaid fail maful-bih".split())


def main():
    t, ps = A.pages()
    out = []
    for p in ps:
        if p["sec"] in EDITOR or p["sec"] not in B:
            continue
        tops = [x for x in B[p["sec"]]["topics"] if x in WANT]
        if not tops:
            continue
        for part, (s0, s1) in (("matn", (p["start"], p["matn_end"])), ("hashiya", (p["matn_end"], p["end"]))):
            if part == "hashiya" and p["vol"] > 2:
                continue
            body = t[s0:s1]
            for a, s in A.sentences(body):
                if MARK.search(s) and 25 <= len(s) <= 320 and " ... " not in s:
                    out.append({"cid": "aqil:%d:%s:%d" % (p["sp"], part[0], a), "book": "ibn-aqil" if part == "matn" else "ibn-aqil-editor",
                                "shamela_page": p["sp"], "vol_page": "%d:%d" % (p["vol"], p["pp"]), "section": p["sec"],
                                "topic": tops[0], "ar": s})
    (A.ROOT / "research/ilal/candidates-ibn-aqil.json").write_text(json.dumps({"candidates": out}, ensure_ascii=False, indent=0), encoding="utf-8")
    from collections import Counter
    print(len(out), Counter(c["topic"] for c in out).most_common())


if __name__ == "__main__":
    main()
