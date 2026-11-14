"""Paradigms for the verbs Shudhūr al-Dhahab (part one) brings to the lexicon, through the project's sarf generator.
usage: python3 tools/authoring/shudhur/sarf_shudhur.py tools/authoring/shudhur/morph_extra.json   (run from arabic-app)"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path("tools/authoring").resolve()))
import sarf_gen as g
from sarf_gen import entry, mazi14, mudari14, idgham, B3, W3
V = {}

def doubled(bab, wazn, masdar, fail, v_c, v_full, yv, m_c, m_full, amr, mansub, majzum, majzum2, maful=None, pmz=None, pmd=None, note=None):
    return idgham(entry(bab + " — مُضَاعَفٌ", wazn, masdar, fail, mazi14(v_c, v_full), mudari14(yv, m_c, m_full), amr, mansub, majzum, majzum2, maful, pmz, pmd,
                        note or "مُضَاعَفٌ: يُدْغَمُ الْمِثْلَانِ مَا تَحَرَّكَ الثَّانِي، وَيُفَكُّ الْإِدْغَامُ إِذَا سَكَنَ."))

# حَاجَّ يُحَاجُّ — the matn's «تُحَاجُّونِي»: the doubled فَاعَلَ contracts where the second twin is vowelled and breaks before a sukūn (حَاجَجْتُ، يُحَاجِجْنَ)
V["hajja-argue"] = doubled(B3, W3, "مُحَاجَّة (حِجَاج)", "مُحَاجّ", "حَاجّ", "حَاجَج", "ُ", "حَاجّ", "حَاجِج",
                           ["حَاجَّ", "حَاجَّا", "حَاجُّوا", "حَاجِّي", "حَاجَّا", "حَاجِجْنَ"], "يُحَاجَّ", "يُحَاجَّ", "تُحَاجَّ", "مُحَاجّ", "حُوجَّ", "يُحَاجُّ",
                           note="مُضَاعَفٌ عَلَى فَاعَلَ: حَاجَّ يُحَاجُّ، حَاجَجْتُ.")

out = sys.argv[1]
json.dump({"verbs": {k: g.nfc(V[k]) for k in sorted(V)}}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(V)} paradigms → {out}")
