"""Paradigms for the verbs Marāḥ al-Arwāḥ (part one) brings to the lexicon, through the project's sarf generator.
usage: python3 tools/authoring/marah/sarf_marah.py tools/authoring/marah/morph_extra.json   (run from arabic-app)"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path("tools/authoring").resolve()))
import sarf_gen as g
from sarf_gen import sound1, derived, B3, W3, B5, W5
V = {}
# وَصَمَ يَصِمُ — the matn's «عَمَّا يَصِمُ»: the wāw falls between the yāʾ and the kasra, as in يَعِدُ
V["wasama"] = sound1("daraba", "وَصَم", "صِم", "صِم", "وَصْم", "وَاصِم", "مَوْصُوم", "وُصِمَ", "يُوصَمُ",
                     note="مِثَالٌ وَاوِيٌّ: تُحْذَفُ الْوَاوُ فِي الْمُضَارِعِ وَالْأَمْرِ لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ — يَصِمُ، صِمْ.", cls="مِثَالٌ وَاوِيٌّ")
# جَبَذَ يَجْبِذُ — the matn's example of the «great» derivation (جَبَذَ مِنَ الْجَذْبِ)
V["jabadha"] = sound1("daraba", "جَبَذ", "جْبِذ", "اِجْبِذ", "جَبْذ", "جَابِذ", "مَجْبُوذ", "جُبِذَ", "يُجْبَذُ")
# نَعَقَ يَنْعِقُ — the matn's example of the «greatest» derivation (نَعَقَ مِنَ النَّهْقِ)
V["naaqa"] = sound1("daraba", "نَعَق", "نْعِق", "اِنْعِق", "نَعِيق (نَعْق)", "نَاعِق")
# قَاوَمَ يُقَاوِمُ — the wāw stands sound in فَاعَلَ, which is why its maṣdar قِوَام keeps it too
V["qawama"] = derived(B3, W3, "ُ", "قَاوَم", "قَاوِم", "قَاوِم", "مُقَاوَمَة (قِوَام)", "مُقَاوِم", "مُقَاوَم", "قُووِمَ", "يُقَاوَمُ",
                      note="أَجْوَفُ عَلَى فَاعَلَ: تَصِحُّ الْوَاوُ فِيهِ وَفِي مَصْدَرِهِ — قَاوَمَ قِوَامًا.")
# تَوَلَّدَ يَتَوَلَّدُ
V["tawallada"] = derived(B5, W5, "َ", "تَوَلَّد", "تَوَلَّد", "تَوَلَّد", "تَوَلُّد", "مُتَوَلِّد")
out = sys.argv[1]
json.dump({"verbs": {k: g.nfc(V[k]) for k in sorted(V)}}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(V)} paradigms → {out}")
