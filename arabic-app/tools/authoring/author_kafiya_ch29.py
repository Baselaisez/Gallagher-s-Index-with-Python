# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 29: THE PARTICLE AND THE JARR LETTERS (I). The ḥarf defined in the notebook's Arabic and shown needing a noun or a
verb; the jarr letter defined; the governed noun explicit or in taʾwīl (9:118); the «verb-meaning» words; the twenty letters; why «jarr»
and why «iḍāfa»; مِنْ for beginning (place, time; the إِلَى test), for explanation (the relative test; 22:30), for partition (the بَعْض
test), and redundant in non-affirmative speech (the Kufans' and al-Akhfash's قَدْ كَانَ مِنْ مَطَرٍ and the author's taʾwīl).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~331-332 of the transcription.

  VERBATIM: s1, s3. COMMENTARY (the notebook): s2, s4-s10 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch29.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-harf-wa-huruf-al-jarr-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "الْحَرْفُ وَحُرُوفُ الْجَرِّ: مِنْ", "en": "The particle and the jarr letters — the twenty, and the four senses of min", "tr": "Harf ve cer harfleri — yirmi harf ve min'in dört mânâsı"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "part"), seg(inner, lex, pos)]))
def jw(full): return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full

HJ = "huruf-jarr"
def JL(full, lex, en, tr, punct=None, inner=None, wa=True, tags=()):
    if wa: return cited_wa("وَ" + full, lex, "prep", [K, HJ] + list(tags), full + " مَعْطُوفٌ — حَرْفٌ مَحْكِيٌّ.", en, tr, full, punct=punct)
    return cited(full, lex, "prep", [K, HJ, "mubtada-khabar"] + list(tags), "خَبَرٌ — حَرْفٌ مَحْكِيٌّ.", en, tr, punct=punct)
def LN(full, lex, en, tr, inner, punct=None, extra=None):
    return cited_wa("وَ" + full, lex, "noun", [K, HJ], full + " مَعْطُوفٌ مَرْفُوعٌ — اسْمُ الْحَرْفِ.", en, tr, inner, punct=punct, extra_segs=extra)

S.append({"id": "s1", "translation": {
 "en": "The particle: what signifies a meaning in something other than itself.",
 "tr": "Harf: kendi dışındaki bir şeyde bulunan bir mânâya delâlet eden kelimedir."},
 "tokens": [
  W("الْحَرْفُ", "harf", "noun", ["mubtada-khabar", "al-kalima-wal-kalam"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the particle».", "«harf».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("دَلَّ", "dalla", "verb", ["ism-mawsul", "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«signifies».", "«delâlet eden»."),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«a».", "«-e»."),
  W("مَعْنًى", "mana", "noun", [HJ, "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«meaning».", "«mânâya»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("غَيْرِهِ", "ghayr", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«something other than itself».", "«kendi dışındaki bir şeyde».", punct=".", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And the particle, to be a part of speech, needs a noun or a verb: in قَدْ ظَهَرَ نُورُ الْإِسْلَامِ مِنْ مَكَّةَ, قَدْ needs the verb ظَهَرَ to signify certainty, and مِنْ needs the noun مَكَّةَ to signify a beginning." + C_EN,
 "tr": "Harf, kelâmın bir cüz'ü olmak için bir isme ya da fiile muhtaçtır: قَدْ ظَهَرَ نُورُ الْإِسْلَامِ مِنْ مَكَّةَ'de قَدْ tahkik mânâsına delâlette ظَهَرَ fiiline, مِنْ ibtidâ mânâsına delâlette مَكَّةَ ismine muhtaçtır." + C_TR},
 "tokens": [
  atf_wa("وَالْحَرْفُ", "harf", "noun", ["mubtada-khabar"], "الْحَرْفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the particle».", "«ve harf».", "الْحَرْفُ"),
  W("يَحْتَاجُ", "ihtaja", "verb", ["mubtada-khabar", "fail", "form-viii-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«needs».", "«muhtaçtır»."),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«a».", "«-e»."),
  W("اسْمٍ", "ism", "noun", [HJ], "مَجْرُورٌ.", "«noun».", "«isme»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("فِعْلٍ", "fil", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«verb».", "«fiile»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("كَوْنِهِ", "kawn", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ كَانَ النَّاقِصَةِ.", "«its being».", "«olmasında».", segments=[seg("كَوْنِ", "kawn", "noun"), pr3msi()]),
  W("جُزْءًا", "juz", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَوْنِ مَنْصُوبٌ.", "«a part».", "«bir cüz'ü»."),
  W("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of».", "«-ın»."),
  W("الْكَلَامِ", "kalam", "noun", [HJ, "al-kalima-wal-kalam"], "مَجْرُورٌ.", "«speech».", "«kelâmın».", punct=":"),
  W("فَفِي", "fi", "prep", [HJ, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«in».", "«-de».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  cited("قَدْ", "qad", "part", [HJ], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — قَدْ حَرْفُ تَحْقِيقٍ.", "«qad».", "«kad»."),
  cited("ظَهَرَ", "zahara", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«has appeared».", "«zuhûr etti»."),
  cited("نُورُ", "nur", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the light of».", "«nuru»."),
  cited("الْإِسْلَامِ", "islam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Islam».", "«İslâm'ın»."),
  cited("مِنْ", "min", "prep", [HJ, K], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.", "«from».", "«-den»."),
  cited("مَكَّةَ", "makka", "propn", [HJ, "mamnu-min-sarf"], "مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Mecca».", "«Mekke».", punct="،"),
  cited("قَدْ", "qad", "part", ["mubtada-khabar"], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«qad».", "«kad»."),
  W("يَحْتَاجُ", "ihtaja", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«needs».", "«muhtaçtır»."),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«the».", "«-e»."),
  cited("ظَهَرَ", "zahara", "verb", [HJ], "فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«ẓahara».", "«zahere»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("دَلَالَتِهِ", "dalala", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«signifying».", "«delâletinde».", segments=[seg("دَلَالَتِ", "dalala", "noun"), pr3msi()]),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«-».", "«-e»."),
  W("التَّحْقِيقِ", "tahqiq", "noun", [HJ], "مَجْرُورٌ.", "«certainty».", "«tahkik».", punct="،"),
  cited_wa("وَمِنْ", "min", "part", ["mubtada-khabar", K], "مِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and min».", "«ve min».", "مِنْ"),
  W("يَحْتَاجُ", "ihtaja", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«needs».", "«muhtaçtır»."),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«the».", "«-e»."),
  cited("مَكَّةَ", "makka", "propn", [HJ, "mamnu-min-sarf"], "فِي مَحَلِّ جَرٍّ — الِاسْمُ مَحْكِيٌّ.", "«Makka».", "«Mekke»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("دَلَالَتِهِ", "dalala", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«signifying».", "«delâletinde».", segments=[seg("دَلَالَتِ", "dalala", "noun"), pr3msi()]),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«-».", "«-e»."),
  W("الِابْتِدَاءِ", "ibtida-start", "noun", [HJ, K], "مَجْرُورٌ.", "«a beginning».", "«ibtidâ».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "The jarr letter: what was set down to carry a verb, or its meaning, over to what follows it.",
 "tr": "Cer harfi: bir fiili ya da fiilin mânâsını, kendini takip edene ulaştırmak için konulan harftir."},
 "tokens": [
  W("حَرْفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letter of».", "«harfi»."),
  W("الْجَرِّ", "jarr", "noun", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«was set down».", "«konulan»."),
  li_("لِلْإِفْضَاءِ", "ifda", "noun", [], "الْإِفْضَاءِ مَجْرُورٌ — مَصْدَرُ أَفْضَى.", "«to carry over».", "«ulaştırmak için».", "الْإِفْضَاءِ", segs=[seg("لِ", "li", "prep"), seg("لْإِفْضَاءِ", "ifda", "noun")]),
  bi_("بِفِعْلٍ", "fil", "noun", [], "فِعْلٍ مَجْرُورٌ.", "«a verb».", "«bir fiili».", "فِعْلٍ"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَعْنَاهُ", "mana", "noun", ["atf-nasaq", "idafa-definiteness", "ism-maqsur-manqus", "mana-al-fil"], "مَعْطُوفٌ عَلَى فِعْلٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its meaning».", "«fiilin mânâsını».", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("مَا", "ma-mawsula", "pron", [HJ, "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what».", "«... -ene»."),
  W("يَلِيهِ", "waliya", "verb", ["ism-mawsul", "fail", "maful-bihi", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ صِلَةٌ.", "«follows it».", "«kendini takip eden».", punct=".", segments=[seg("يَلِي", "waliya", "verb"), pr3msi()]),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the noun that follows the jarr letter may be explicit, as in مَرَرْتُ بِزَيْدٍ, or a noun in taʾwīl, as in حَتَّى إِذَا ضَاقَتْ عَلَيْهِمُ الْأَرْضُ بِمَا رَحُبَتْ — where بِمَا رَحُبَتْ is in the taʾwīl of بِرُحْبِهَا." + C_EN,
 "tr": "Cer harfini takip eden isim, مَرَرْتُ بِزَيْدٍ'deki gibi sarih olabilir ya da حَتَّى إِذَا ضَاقَتْ عَلَيْهِمُ الْأَرْضُ بِمَا رَحُبَتْ âyetindeki gibi te'vilen isim olabilir — oradaki بِمَا رَحُبَتْ, بِرُحْبِهَا te'vilindedir." + C_TR},
 "tokens": [
  atf_wa("وَالِاسْمُ", "ism", "noun", ["mubtada-khabar"], "الِاسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the noun».", "«ve isim».", "الِاسْمُ"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonraki»."),
  W("حَرْفِ", "harf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the letter of».", "«harfi»."),
  W("الْجَرِّ", "jarr", "noun", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer»."),
  W("إِمَّا", "imma", "part", ["atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  W("صَرِيحٌ", "sarih", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«explicit».", "«sarihtir».", punct="،"),
  ka_("كَزَيْدٍ", "zayd", "propn", [HJ], "زَيْدٍ مَجْرُورٌ.", "«as Zayd».", "«Zeyd gibi».", "زَيْدٍ"),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("مَرَرْتُ", "marra", "verb", [HJ, "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«I passed».", "«uğradım».", segments=[seg("مَرَرْ", "marra", "verb"), prT()]),
  bi_("بِزَيْدٍ", "zayd", "propn", [HJ, K], "زَيْدٍ مَجْرُورٌ — الِاسْمُ الصَّرِيحُ.", "«by Zayd».", "«Zeyd'e».", "زَيْدٍ", punct="،"),
  atf_wa("وَإِمَّا", "imma", "part", ["atf-nasaq"], "إِمَّا حَرْفُ تَفْصِيلٍ.", "«or».", "«ya da».", "إِمَّا"),
  W("اسْمٌ", "ism", "noun", ["atf-nasaq"], "مَعْطُوفٌ عَلَى صَرِيحٌ مَرْفُوعٌ.", "«a noun».", "«isimdir»."),
  bi_("بِالتَّأْوِيلِ", "tawil", "noun", [], "التَّأْوِيلِ مَجْرُورٌ.", "«in taʾwīl».", "«te'vilen».", "التَّأْوِيلِ", punct="،"),
  ka_("كَمَا", "ma-mawsula", "pron", ["ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«as in».", "«... gibi».", "مَا"),
  W("فِي", "fi", "prep", [HJ, "ism-mawsul"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«in».", "«-deki»."),
  cited("حَتَّى", "hatta", "part", [HJ], "الْآيَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — حَتَّى ابْتِدَائِيَّةٌ.", "«until».", "«nihayet»."),
  cited("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  cited("ضَاقَتْ", "daqa", "verb", ["idha-shartiyya", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«became narrow».", "«daraldığında».", segments=[seg("ضَاقَ", "daqa", "verb"), seg("تْ", "ta-tanith", "part")]),
  cited("عَلَيْهِمُ", "ala", "prep", [HJ], "عَلَى حَرْفُ جَرٍّ، وَهُمْ مَجْرُورٌ، ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«upon them».", "«onlara».", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِمُ", "pron-3mp", "pron")]),
  cited("الْأَرْضُ", "ard", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the earth».", "«yeryüzü»."),
  cited("بِمَا", "ma-masdariyya", "part", [HJ, K, "anwa-ma", "an-masdariyya"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«for all its».", "«bütün».", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  cited("رَحُبَتْ", "rahuba", "verb", ["fail", "an-masdariyya"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْبَاءِ.", "«breadth».", "«genişliğine rağmen».", punct="،", segments=[seg("رَحُبَ", "rahuba", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«zira».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")]),
  cited("بِمَا", "ma-masdariyya", "part", ["inna-wa-akhawatuha"], "الْمُرَكَّبُ مَحْكِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«bi-mā».", "«bimâ».", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  cited("رَحُبَتْ", "rahuba", "verb", [], "تَمَامُ الْمَحْكِيِّ.", "«raḥubat».", "«rahubet».", segments=[seg("رَحُبَ", "rahuba", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("فِي", "fi", "prep", [HJ, "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — خَبَرُ إِنَّ.", "«is in».", "«-dedir»."),
  W("تَأْوِيلِ", "tawil", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the taʾwīl of».", "«te'vilin»."),
  cited("بِرُحْبِهَا", "rahb", "noun", ["idafa-definiteness", HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَرُحْبِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — الِاسْمُ الْمُؤَوَّلُ.", "«bi-ruḥbihā, «for its breadth»».", "«bi-ruhbihâ, «genişliğine rağmen»».", punct=".", segments=[seg("بِ", "bi", "prep"), seg("رُحْبِ", "rahb", "noun"), pr3fs()]),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And «verb-meanings» are every word from which the meaning of a verb is understood — such as the ism fāʿil, the ism mafʿūl and the ṣifa mushabbaha." + C_EN,
 "tr": "«Fiil mânâları», ism-i fâil, ism-i mef'ûl ve sıfat-ı müşebbehe gibi, kendisinden fiil mânâsı anlaşılan her lafızdır." + C_TR},
 "tokens": [
  atf_wa("وَمَعَانِي", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "mana-al-fil", "jam-taksir"], "مَعَانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ — جَمْعُ مَعْنًى.", "«and «verb-meanings»».", "«ve «fiil mânâları»».", "مَعَانِي"),
  W("الْأَفْعَالِ", "fil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of verbs».", "«fiillerin»."),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«are every».", "«her»."),
  W("لَفْظٍ", "lafz", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«word».", "«lafızdır»."),
  W("يُفْهَمُ", "fahima", "verb", ["naat-sifa", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِفَةٌ لِلَفْظٍ.", "«is understood».", "«anlaşılan»."),
  W("مِنْهُ", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«from which».", "«kendisinden».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  W("مَعْنَى", "mana", "noun", ["naib-al-fail", "idafa-definiteness", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the meaning of».", "«mânâsı»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«fiil».", punct="،"),
  ka_("كَاسْمِ", "ism", "noun", ["idafa-definiteness", "ism-fail"], "اسْمِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«such as the ism».", "«ism-i».", "اسْمِ"),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«fāʿil».", "«fâil»."),
  atf_wa("وَاسْمِ", "ism", "noun", ["idafa-definiteness", "ism-maful"], "اسْمِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the ism».", "«ism-i».", "اسْمِ"),
  W("الْمَفْعُولِ", "maful-noun", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«mafʿūl».", "«mef'ûl»."),
  atf_wa("وَالصِّفَةِ", "sifa", "noun", ["atf-nasaq", "sifa-mushabbaha"], "الصِّفَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the ṣifa».", "«ve sıfat-ı».", "الصِّفَةِ"),
  W("الْمُشَبَّهَةِ", "mushabbah", "noun", ["naat-sifa", "sifa-mushabbaha", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«mushabbaha».", "«müşebbehe».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And the jarr letters are: مِنْ, إِلَى, حَتَّى, فِي, the bāʾ, the lām, رُبَّ, the wāw after which رُبَّ is understood, the wāw of the oath, its tāʾ, its bāʾ, عَنْ, عَلَى, the kāf, مُذْ, مُنْذُ, خَلَا, عَدَا and حَاشَا." + C_EN,
 "tr": "Cer harfleri: مِنْ, إِلَى, حَتَّى, فِي, bâ, lâm, رُبَّ, ardında رُبَّ takdir olunan vâv, kasem vâvı, kasem tâsı, kasem bâsı, عَنْ, عَلَى, kâf, مُذْ, مُنْذُ, خَلَا, عَدَا ve حَاشَا'dır." + C_TR},
 "tokens": [
  atf_wa("وَحُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "حُرُوفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the letters of».", "«ve harfleri».", "حُرُوفُ"),
  W("الْجَرِّ", "jarr", "noun", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer».", punct=":"),
  JL("مِنْ", "min", "«min».", "«min».", wa=False),
  JL("إِلَى", "ila", "«ilā».", "«ilâ»."),
  JL("حَتَّى", "hatta", "«ḥattā».", "«hattâ»."),
  JL("فِي", "fi", "«fī».", "«fî»."),
  LN("الْبَاءُ", "ba-harf", "«the bāʾ».", "«bâ».", "الْبَاءُ"),
  LN("اللَّامُ", "lam-letter", "«the lām».", "«lâm».", "اللَّامُ"),
  JL("رُبَّ", "rubba", "«rubba».", "«rubbe»."),
  LN("الْوَاوُ", "waw-letter", "«the wāw».", "«vâv».", "الْوَاوُ"),
  W("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِلْوَاوِ.", "«after which».", "«ardında»."),
  W("تُقَدَّرُ", "qaddara", "verb", ["ism-mawsul", "naib-al-fail", "hadhf-wa-taqdir", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.", "«is understood».", "«takdir olunan»."),
  cited("رُبَّ", "rubba", "prep", ["naib-al-fail", K, HJ], "نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", "«rubba».", "«rubbe»."),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ardında».", punct="،", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  LN("وَاوُ", "waw-letter", "«the wāw of».", "«vâvı».", "وَاوُ"),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", "huruf-jarr"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasem»."),
  LN("تَاؤُهُ", "ta-letter", "«its tāʾ».", "«tâsı».", "تَاؤُ", extra=[seg("تَاؤُ", "ta-letter", "noun"), pr3ms()]),
  LN("بَاؤُهُ", "ba-harf", "«and its bāʾ».", "«ve bâsı».", "بَاؤُ", extra=[seg("بَاؤُ", "ba-harf", "noun"), pr3ms()]),
  JL("عَنْ", "an-jarr", "«ʿan».", "«an»."),
  JL("عَلَى", "ala", "«ʿalā».", "«alâ»."),
  LN("الْكَافُ", "kaf-letter", "«the kāf».", "«kâf».", "الْكَافُ"),
  JL("مُذْ", "mudh", "«mudh».", "«müz»."),
  JL("مُنْذُ", "mundhu", "«mundhu».", "«münzü»."),
  JL("خَلَا", "khala-except", "«khalā».", "«halâ»."),
  JL("عَدَا", "ada-except", "«ʿadā».", "«adâ»."),
  JL("حَاشَا", "hasha", "«and ḥāshā».", "«ve hâşâ».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And they were called jarr letters because they put the noun after them into jarr; and iḍāfa letters because they annex the verb, or its meaning, to the noun that follows it." + C_EN,
 "tr": "Önlerindeki ismi cer ettikleri için cer harfleri; fiili ya da fiilin mânâsını kendini takip eden isme izâfe ettikleri için de izâfet harfleri denilmiştir." + C_TR},
 "tokens": [
  atf_wa("وَسُمِّيَتْ", "samma", "verb", ["naib-al-fail", "form-ii-verbs"], "سُمِّيَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and they were called».", "«ve adlandırıldılar».", "سُمِّيَتْ"),
  W("حُرُوفَ", "harf", "noun", ["mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«letters of».", "«harfleri»."),
  W("الْجَرِّ", "jarr", "noun", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer»."),
  W("لِأَنَّهَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because they».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("تَجُرُّ", "jarra", "verb", ["inna-wa-akhawatuha", "fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«put into jarr».", "«cer ederler»."),
  W("الِاسْمَ", "ism", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the noun».", "«ismi»."),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after them».", "«önlerindeki».", punct="؛", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  atf_wa("وَحُرُوفَ", "harf", "noun", ["atf-nasaq", "idafa-definiteness"], "حُرُوفَ مَعْطُوفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and letters of».", "«ve harfleri».", "حُرُوفَ"),
  W("الْإِضَافَةِ", "idafa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iḍāfa».", "«izâfet»."),
  W("لِأَنَّهَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because they».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("تُضِيفُ", "adafa", "verb", ["inna-wa-akhawatuha", "fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«annex».", "«izâfe ederler»."),
  W("الْفِعْلَ", "fil", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the verb».", "«fiili»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَعْنَاهُ", "mana", "noun", ["atf-nasaq", "idafa-definiteness", "mana-al-fil"], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its meaning».", "«mânâsını».", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الِاسْمِ", "ism", "noun", [HJ], "مَجْرُورٌ.", "«the noun».", "«isme»."),
  W("بَعْدَهُ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«that follows it».", "«ondan sonraki».", punct=".", segments=[seg("بَعْدَ", "bada", "noun"), pr3ms()]),
 ]})

S.append({"id": "s8", "translation": {
 "en": "مِنْ is for beginning — in place, as سِرْتُ مِنَ الْبَصْرَةِ, or in time, as صُمْتُ مِنْ يَوْمِ الْجُمُعَةِ; and its sign is that إِلَى may stand opposite it, as سِرْتُ مِنَ الْبَصْرَةِ إِلَى الْكُوفَةِ." + C_EN,
 "tr": "مِنْ ibtidâ içindir — سِرْتُ مِنَ الْبَصْرَةِ gibi mekânda ya da صُمْتُ مِنْ يَوْمِ الْجُمُعَةِ gibi zamanda; alâmeti, سِرْتُ مِنَ الْبَصْرَةِ إِلَى الْكُوفَةِ gibi karşısına إِلَى getirmenin sahih olmasıdır." + C_TR},
 "tokens": [
  cited("مِنْ", "min", "prep", ["mubtada-khabar", K, HJ], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«min».", "«min»."),
  li_("لِلِابْتِدَاءِ", "ibtida-start", "noun", ["mubtada-khabar", K], "الِابْتِدَاءِ مَجْرُورٌ — خَبَرٌ.", "«is for beginning».", "«ibtidâ içindir».", "الِابْتِدَاءِ", segs=[seg("لِ", "li", "prep"), seg("لِابْتِدَاءِ", "ibtida-start", "noun")], punct="،"),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمَكَانِ", "makan", "noun", [HJ], "مَجْرُورٌ.", "«place».", "«mekânda»."),
  ka_("كَسِرْتُ", "sara-travel", "verb", [HJ, "fail", "hollow-verbs"], "سِرْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«as «I travelled»».", "««yola çıktım» gibi».", "سِرْ", segs=[seg("كَ", "ka", "part"), seg("سِرْ", "sara-travel", "verb"), prT()]),
  cited("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ، حُرِّكَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  cited("الْبَصْرَةِ", "basra", "propn", [HJ], "مَجْرُورٌ — مَبْدَأُ السَّيْرِ.", "«Basra».", "«Basra».", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الزَّمَانِ", "zaman", "noun", [HJ], "مَجْرُورٌ.", "«time».", "«zamanda»."),
  ka_("كَصُمْتُ", "saama", "verb", [HJ, "fail", "hollow-verbs"], "صُمْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْجُمْلَةُ مَحْكِيَّةٌ.", "«as «I fasted»».", "««oruç tuttum» gibi».", "صُمْ", segs=[seg("كَ", "ka", "part"), seg("صُمْ", "saama", "verb"), prT()]),
  cited("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.", "«from».", "«-den»."),
  cited("يَوْمِ", "yawm", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ — مَبْدَأُ الصَّوْمِ.", "«the day of».", "«günü»."),
  cited("الْجُمُعَةِ", "juma", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Friday».", "«cuma».", punct="؛"),
  atf_wa("وَعَلَامَتُهَا", "alama", "noun", ["mubtada-khabar", "idafa-definiteness"], "عَلَامَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its sign».", "«ve alâmeti».", "عَلَامَتُ", extra_segs=[seg("عَلَامَتُ", "alama", "noun"), pr3fs()]),
  W("صِحَّةُ", "sihha", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the soundness of».", "«sahih olmasıdır»."),
  W("إِلَى", "ila", "prep", ["idafa-definiteness", K, HJ], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«ilā».", "«ilâ»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مُقَابَلَتِهَا", "muqabala", "noun", [HJ, "idafa-definiteness", "form-iii-verbs"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — مَصْدَرُ قَابَلَ.", "«standing opposite it».", "«karşısında».", punct="،", segments=[seg("مُقَابَلَتِ", "muqabala", "noun"), pr3fs()]),
  nahwu(),
  cited("سِرْتُ", "sara-travel", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I travelled».", "«yola çıktım».", segments=[seg("سِرْ", "sara-travel", "verb"), prT()]),
  cited("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.", "«from».", "«-den»."),
  cited("الْبَصْرَةِ", "basra", "propn", [HJ], "مَجْرُورٌ.", "«Basra».", "«Basra»."),
  cited("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِانْتِهَاءِ — مُقَابِلُ مِنْ.", "«to».", "«-e»."),
  cited("الْكُوفَةِ", "kufa", "propn", [HJ], "مَجْرُورٌ.", "«Kufa».", "«Kûfe».", punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And مِنْ is for explanation — its sign being that a relative may replace it — as فَاجْتَنِبُوا الرِّجْسَ مِنَ الْأَوْثَانِ; and for partition — its sign being that بَعْض may replace it — as أَخَذْتُ مِنَ الدَّرَاهِمِ, that is, بَعْضَ الدَّرَاهِمِ." + C_EN,
 "tr": "مِنْ tebyîn içindir — alâmeti, yerine ism-i mevsûl getirmenin sahih olmasıdır — فَاجْتَنِبُوا الرِّجْسَ مِنَ الْأَوْثَانِ gibi; ve teb'îz içindir — alâmeti, yerine بَعْض getirmenin sahih olmasıdır — أَخَذْتُ مِنَ الدَّرَاهِمِ gibi, yani بَعْضَ الدَّرَاهِمِ." + C_TR},
 "tokens": [
  cited_wa("وَمِنْ", "min", "prep", ["mubtada-khabar", K, HJ], "مِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and min».", "«ve min».", "مِنْ"),
  li_("لِلتَّبْيِينِ", "tabyin", "noun", ["mubtada-khabar", K], "التَّبْيِينِ مَجْرُورٌ — خَبَرٌ.", "«is for explanation».", "«tebyîn içindir».", "التَّبْيِينِ", segs=[seg("لِ", "li", "prep"), seg("لتَّبْيِينِ", "tabyin", "noun")], punct="،"),
  atf_wa("وَعَلَامَتُهَا", "alama", "noun", ["mubtada-khabar", "idafa-definiteness"], "عَلَامَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its sign being».", "«alâmeti».", "عَلَامَتُ", extra_segs=[seg("عَلَامَتُ", "alama", "noun"), pr3fs()]),
  W("صِحَّةُ", "sihha", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the soundness of».", "«sahih olması»."),
  W("الْمَوْصُولِ", "mawsul", "noun", ["idafa-definiteness", "ism-mawsul"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a relative».", "«ism-i mevsûl»."),
  W("مَكَانَهَا", "makan", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«in its place».", "«yerine».", punct="،", segments=[seg("مَكَانَ", "makan", "noun"), pr3fs()]),
  nahwu(),
  cited("فَاجْتَنِبُوا", "ijtanaba", "verb", ["fail", "form-viii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَاجْتَنِبُوا فِعْلُ أَمْرٍ، وَالْوَاوُ فَاعِلٌ.", "«so shun».", "«kaçının».", segments=[seg("فَ", "fa", "conj"), seg("اجْتَنِبُ", "ijtanaba", "verb"), seg("وا", "pron-2mp", "pron")]),
  cited("الرِّجْسَ", "rijs", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the filth».", "«pisliğe»."),
  cited("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلتَّبْيِينِ — أَيِ الرِّجْسَ الَّذِي هُوَ الْأَوْثَانُ.", "«namely».", "«yani»."),
  cited("الْأَوْثَانِ", "wathan", "noun", [HJ, "jam-taksir"], "مَجْرُورٌ — جَمْعُ وَثَنٍ.", "«idols».", "«putlardan».", punct="؛"),
  cited_wa("وَمِنْ", "min", "prep", ["mubtada-khabar", K, HJ], "مِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and min».", "«ve min».", "مِنْ"),
  li_("لِلتَّبْعِيضِ", "tabid", "noun", ["mubtada-khabar", K], "التَّبْعِيضِ مَجْرُورٌ — خَبَرٌ.", "«is for partition».", "«teb'îz içindir».", "التَّبْعِيضِ", segs=[seg("لِ", "li", "prep"), seg("لتَّبْعِيضِ", "tabid", "noun")], punct="،"),
  atf_wa("وَعَلَامَتُهَا", "alama", "noun", ["mubtada-khabar", "idafa-definiteness"], "عَلَامَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its sign being».", "«alâmeti».", "عَلَامَتُ", extra_segs=[seg("عَلَامَتُ", "alama", "noun"), pr3fs()]),
  W("صِحَّةُ", "sihha", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the soundness of».", "«sahih olması»."),
  cited("بَعْضٍ", "bad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«baʿḍ».", "«ba'z»."),
  W("مَكَانَهَا", "makan", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«in its place».", "«yerine».", punct="،", segments=[seg("مَكَانَ", "makan", "noun"), pr3fs()]),
  nahwu(),
  cited("أَخَذْتُ", "akhadha", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I took».", "«aldım».", segments=[seg("أَخَذْ", "akhadha", "verb"), prT()]),
  cited("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.", "«some of».", "«-den»."),
  cited("الدَّرَاهِمِ", "dirham", "noun", [HJ, "jam-taksir", "mamnu-min-sarf"], "مَجْرُورٌ بِالْكَسْرَةِ لِأَجْلِ اللَّامِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«the dirhams».", "«dirhemlerden».", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("بَعْضَ", "bad", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ — التَّقْدِيرُ.", "«some of».", "«bazısını»."),
  cited("الدَّرَاهِمِ", "dirham", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dirhams».", "«dirhemlerin».", punct="."),
 ]})

S.append({"id": "s10", "translation": {
 "en": "And مِنْ is redundant in non-affirmative speech — as مَا جَاءَنِي مِنْ أَحَدٍ; the Kufans and al-Akhfash allowed it redundant in affirmative speech too, from the Arabs' قَدْ كَانَ مِنْ مَطَرٍ, but for the author that is in taʾwīl: either for partition, قَدْ كَانَ بَعْضُ مَطَرٍ, or for explanation, قَدْ كَانَ شَيْءٌ مِنْ مَطَرٍ." + C_EN,
 "tr": "مِنْ gayr-i mûcib kelâmda zâid olur — مَا جَاءَنِي مِنْ أَحَدٍ gibi; Kûfeliler ve Ahfeş, Arapların قَدْ كَانَ مِنْ مَطَرٍ sözünden hareketle mûcib kelâmda da zâid olmasına cevaz verdiler; musannife göre ise bu te'villidir: ya teb'îz için, قَدْ كَانَ بَعْضُ مَطَرٍ, ya da tebyîn için, قَدْ كَانَ شَيْءٌ مِنْ مَطَرٍ." + C_TR},
 "tokens": [
  cited_wa("وَمِنْ", "min", "prep", ["mubtada-khabar", K, HJ], "مِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and min».", "«ve min».", "مِنْ"),
  W("زَائِدَةٌ", "zaid", "noun", ["mubtada-khabar", K], "خَبَرٌ مَرْفُوعٌ.", "«is redundant».", "«zâid olur»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("غَيْرِ", "ghayr", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«non-».", "«gayr-i»."),
  W("الْمُوجَبِ", "mujab", "noun", ["idafa-definiteness", "ism-maful", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْكَلَامُ الَّذِي فِيهِ نَفْيٌ أَوْ نَهْيٌ أَوِ اسْتِفْهَامٌ.", "«affirmative speech».", "«mûcib kelâmda».", punct="،"),
  nahwu(),
  cited("مَا", "ma-nafiya", "part", ["anwa-ma", "la-nafiya"], "نَافِيَةٌ.", "«not».", "«-medi»."),
  cited("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  cited("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ زَائِدٌ.", "«any».", "«hiç»."),
  cited("أَحَدٍ", "ahad", "noun", [HJ, "fail"], "مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا فَاعِلٌ.", "«one».", "«kimse».", punct="؛"),
  atf_wa("وَجَوَّزَ", "jawwaza", "verb", ["fail", "form-ii-verbs"], "جَوَّزَ فِعْلٌ مَاضٍ.", "«and allowed».", "«ve cevaz verdiler».", "جَوَّزَ"),
  W("الْكُوفِيُّونَ", "kufi", "noun", ["fail", "jam-mudhakkar-salim"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ.", "«the Kufans».", "«Kûfeliler»."),
  atf_wa("وَالْأَخْفَشُ", "akhfash", "propn", ["atf-nasaq"], "الْأَخْفَشُ مَعْطُوفٌ مَرْفُوعٌ.", "«and al-Akhfash».", "«ve Ahfeş».", "الْأَخْفَشُ"),
  W("زِيَادَتَهَا", "ziyada", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its redundancy».", "«zâid olmasına».", segments=[seg("زِيَادَتَ", "ziyada", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمُوجَبِ", "mujab", "noun", [HJ, "ism-maful"], "مَجْرُورٌ.", "«affirmative speech».", "«mûcib kelâmda»."),
  W("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ.", "«too».", "«da»."),
  li_("لِقَوْلِ", "qawl", "noun", ["idafa-definiteness", "lam-taleel"], "قَوْلِ مَجْرُورٌ — لَامُ التَّعْلِيلِ، وَهُوَ مُضَافٌ.", "«from the saying of».", "«... sözünden hareketle».", "قَوْلِ"),
  W("الْعَرَبِ", "arab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Arabs».", "«Arapların»."),
  cited("قَدْ", "qad", "part", [], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«muhakkak»."),
  cited("كَانَ", "kana", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ.", "«there was».", "«oldu»."),
  cited("مِنْ", "min", "prep", [K, HJ], "زَائِدَةٌ عِنْدَهُمْ.", "«min».", "«min»."),
  cited("مَطَرٍ", "matar", "noun", [HJ, "fail"], "مَجْرُورٌ لَفْظًا فَاعِلٌ مَحَلًّا.", "«rain».", "«yağmur».", punct="،"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«but for».", "«... göre ise».", "عِنْدَ"),
  W("الْمُصَنِّفِ", "musannif", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the author».", "«musannife»."),
  W("هُوَ", "huwa", "pron", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ.", "«that is».", "«bu»."),
  W("مُؤَوَّلٌ", "muawwal", "noun", ["mubtada-khabar", "ism-maful", "form-ii-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«in taʾwīl».", "«te'villidir».", punct=":"),
  W("إِمَّا", "imma", "part", ["atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  li_("لِلتَّبْعِيضِ", "tabid", "noun", [K], "التَّبْعِيضِ مَجْرُورٌ.", "«for partition».", "«teb'îz için».", "التَّبْعِيضِ", segs=[seg("لِ", "li", "prep"), seg("لتَّبْعِيضِ", "tabid", "noun")], punct="،"),
  cited("قَدْ", "qad", "part", [], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«muhakkak»."),
  cited("كَانَ", "kana", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ.", "«there was».", "«oldu»."),
  cited("بَعْضُ", "bad", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — التَّقْدِيرُ.", "«some».", "«bir miktar»."),
  cited("مَطَرٍ", "matar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rain».", "«yağmur».", punct="،"),
  atf_wa("وَإِمَّا", "imma", "part", ["atf-nasaq"], "إِمَّا حَرْفُ تَفْصِيلٍ.", "«or».", "«ya da».", "إِمَّا"),
  li_("لِلتَّبْيِينِ", "tabyin", "noun", [K], "التَّبْيِينِ مَجْرُورٌ.", "«for explanation».", "«tebyîn için».", "التَّبْيِينِ", segs=[seg("لِ", "li", "prep"), seg("لتَّبْيِينِ", "tabyin", "noun")], punct="،"),
  cited("قَدْ", "qad", "part", [], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«muhakkak»."),
  cited("كَانَ", "kana", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ.", "«there was».", "«oldu»."),
  cited("شَيْءٌ", "shay", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ — التَّقْدِيرُ.", "«something».", "«bir şey»."),
  cited("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلتَّبْيِينِ.", "«of».", "«-den»."),
  cited("مَطَرٍ", "matar", "noun", [HJ], "مَجْرُورٌ.", "«rain».", "«yağmur».", punct="."),
 ]})

def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "ifda": need("ifda", "إِفْضَاء", "ف ض و", "noun", "carrying over, conveying — the maṣdar of أَفْضَى; a jarr letter carries the verb's reach over to its noun", "ulaştırma, eriştirme — efdâ'nın masdarı; cer harfi fiilin ulaşımını ismine taşır", 5),
 "tabyin": need("tabyin", "تَبْيِين", "ب ي ن", "noun", "explanation — min stating what a vague word meant (the relative test)", "tebyîn, açıklama — min'in mübhem bir kelimenin ne olduğunu bildirmesi (ism-i mevsûl testi)", 4),
 "tabid": need("tabid", "تَبْعِيض", "ب ع ض", "noun", "partition — min meaning «some of» (the baʿḍ test)", "teb'îz, kısmîlik — «bazısı» mânâsındaki min (ba'z testi)", 4),
 "rijs": need("rijs", "رِجْس", "ر ج س", "noun", "filth, abomination", "pislik, murdarlık", 4),
 "wathan": need("wathan", "وَثَن", "و ث ن", "noun", "an idol; plural أَوْثَان", "put; cem'i أَوْثَان", 3),
 "mujab": need("mujab", "مُوجَب", "و ج ب", "noun", "affirmative (of speech) — the ism mafʿūl of أَوْجَبَ; its opposite holds a negation, a prohibition or a question", "mûcib, olumlu (kelâm için) — evcebe'nin ism-i mef'ûlü; karşıtı nefy, nehy ya da istifham taşır", 4),
 "muawwal": need("muawwal", "مُؤَوَّل", "أ و ل", "noun", "interpreted, read in taʾwīl — the ism mafʿūl of أَوَّلَ", "te'villi, te'vil edilmiş — evvele'nin ism-i mef'ûlü", 4),
 "sihha": need("sihha", "صِحَّة", "ص ح ح", "noun", "soundness, validity — the maṣdar of صَحَّ", "sıhhat, geçerlilik — sahha'nın masdarı", 3),
 "muqabala": need("muqabala", "مُقَابَلَة", "ق ب ل", "noun", "standing opposite, correspondence — the maṣdar of قَابَلَ", "mukâbele, karşılık — kâbele'nin masdarı", 3),
}
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch29 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْحَرْفُ وَحُرُوفُ الْجَرِّ فِي الْكَافِيَةِ: مِنْ", "en": "The particle and the jarr letters in the Kafiya: the two definitions, the governed noun in taʾwīl, the twenty letters, the two names, and min's four senses with their tests", "tr": "Kâfiye'de harf ve cer harfleri: iki tarif, te'villi mecrûr, yirmi harf, iki ad ve min'in testleriyle dört mânâsı"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الحرف: ما دل على معنى في غيره؛ حرف الجر: ما وضع للإفضاء بفعل أو معناه إلى ما يليه؛ وهي من وإلى وحتى وفي والباء واللام ورب والواو وواو القسم وتاؤه وباؤه وعن وعلى والكاف ومذ ومنذ وخلا وعدا وحاشا", "ضياء صونغور اوغلى — دفتر الكافية: الحرف يحتاج إلى اسم أو فعل؛ المجرور صريحا وبالتأويل؛ معاني الأفعال؛ وجه التسمية؛ من للابتداء والتبيين والتبعيض والزيادة وعلاماتها؛ الكوفيون والأخفش في قد كان من مطر"],
 "question": {
  "en": ["What is a particle? A word whose meaning lives in another word: مِنْ means nothing until مَكَّةَ follows it, and قَدْ nothing until ظَهَرَ does. That is why a particle can never be a sentence on its own and always needs a noun or a verb beside it.",
         "What is a jarr letter? A particle set down to carry a verb's reach — or the reach of a verb-like word, an ism fāʿil, an ism mafʿūl, a ṣifa mushabbaha — over to the noun after it. The noun may be explicit (بِزَيْدٍ) or a clause read as a noun (بِمَا رَحُبَتْ = بِرُحْبِهَا).",
         "How many are they, and why two names? Twenty: the sixteen plain letters plus the wāw of rubba and the three oath letters. «Jarr letters» for what they do to the noun; «iḍāfa letters» for what they do to the verb — they annex it to its noun. The Iẓhār teaches the same twenty under the first name.",
         "What does مِنْ mean? Four things, each with a test the madrasah hands you. Beginning, in place or time — test: can إِلَى stand opposite it? Explanation — test: can a relative replace it (الرِّجْسَ الَّذِي هُوَ الْأَوْثَانُ)? Partition — test: can بَعْض replace it (بَعْضَ الدَّرَاهِمِ)? And redundant — only in speech that is not affirmative (مَا جَاءَنِي مِنْ أَحَدٍ).",
         "May مِنْ be redundant in an affirmative sentence? The Kufans and al-Akhfash said yes, from قَدْ كَانَ مِنْ مَطَرٍ. Ibn al-Ḥājib says no: read it as partition (بَعْضُ مَطَرٍ) or as explanation (شَيْءٌ مِنْ مَطَرٍ). Where a reading saves the rule, the rule is kept.",
         "What does the engine do? The kernel's PARTICLES table carries all twenty with their government, the TaalluqEngine hangs every jarr phrase on the nearest verb or verb-meaning (the Qawāʿid's rule, now the Kafiya's definition), and the Jarr lab lists min's senses with these very tests."],
  "tr": ["Harf nedir? Mânâsı başka bir kelimede yaşayan kelime: مِنْ, ardından مَكَّةَ gelene kadar hiçbir şey demektir; قَدْ de ظَهَرَ gelene kadar. Bu yüzden harf tek başına asla cümle olamaz ve daima yanında bir isim ya da fiile muhtaçtır.",
         "Cer harfi nedir? Bir fiilin — ya da fiil benzeri bir kelimenin, ism-i fâilin, ism-i mef'ûlün, sıfat-ı müşebbehenin — ulaşımını ardındaki isme taşımak için konulan harf. İsim sarih olabilir (بِزَيْدٍ) ya da isim sayılan bir cümle (بِمَا رَحُبَتْ = بِرُحْبِهَا).",
         "Kaç tanedir ve neden iki ad? Yirmi: on altı düz harf artı rubbe vâvı ve üç kasem harfi. İsme yaptıkları için «cer harfleri»; fiile yaptıkları için «izâfet harfleri» — onu ismine izâfe ederler. İzhar aynı yirmiyi birinci adla öğretir.",
         "مِنْ ne demektir? Dört şey, her biri medresenin eline verdiği bir testle. İbtidâ, mekânda ya da zamanda — test: karşısına إِلَى konabilir mi? Tebyîn — test: yerine ism-i mevsûl konabilir mi (الرِّجْسَ الَّذِي هُوَ الْأَوْثَانُ)? Teb'îz — test: yerine بَعْض konabilir mi (بَعْضَ الدَّرَاهِمِ)? Ve zâid — yalnız olumlu olmayan kelâmda (مَا جَاءَنِي مِنْ أَحَدٍ).",
         "مِنْ olumlu cümlede zâid olabilir mi? Kûfeliler ve Ahfeş قَدْ كَانَ مِنْ مَطَرٍ'den hareketle evet dedi. İbnü'l-Hâcib hayır der: teb'îz (بَعْضُ مَطَرٍ) ya da tebyîn (شَيْءٌ مِنْ مَطَرٍ) olarak oku. Bir okuyuş kuralı kurtarıyorsa kural korunur.",
         "Motor ne yapar? Çekirdeğin PARTICLES tablosu yirmisini amelleriyle taşır, TaalluqEngine her cer ibaresini en yakın fiile ya da fiil mânâsına asar (Kavâid'in kuralı, şimdi Kâfiye'nin tarifi) ve Cer laboratuvarı min'in mânâlarını tam bu testlerle listeler."]},
 "plain": {
  "en": "A particle means something only next to another word, and a jarr letter is the particle that links a verb to the noun it reaches: «I travelled FROM Basra». Arabic has twenty. The first, min, can mean «from», «namely», «some of», or nothing at all in a negative sentence, and each sense has a quick test.",
  "tr": "Harf, yalnız başka bir kelimenin yanında bir şey ifade eden kelimedir; cer harfi, fiili ulaştığı isme bağlayan harftir: «Basra'DAN yola çıktım». Arapçada yirmi tane vardır. İlki min, «-den», «yani», «bazısı» ya da olumsuz cümlede hiçbir şey demek olabilir ve her mânânın hızlı bir testi vardır."},
 "explanation": {
  "en": "The Kafiya's third part opens with the particle, and the notebook gives both definitions verbatim before glossing them. The ḥarf's definition is tested on one sentence, قَدْ ظَهَرَ نُورُ الْإِسْلَامِ مِنْ مَكَّةَ, in which each particle is shown reaching for the word that completes it. The jarr letter's definition carries the whole TaalluqEngine in one line — a letter conveys a verb, or a verb's meaning, to a noun — and the notebook's two glosses are exactly the engine's two edge cases: the noun may be a clause in taʾwīl (the aya of 9:118), and the «verb-meaning» words are the participles and the ṣifa mushabbaha that the glossary flags as verbal. The list of twenty is given as the notebook gives it, with the wāw of rubba and the three oath letters counted separately, and the double naming (jarr / iḍāfa) is explained from the two ends of the relation. Then مِنْ, the first and busiest letter, with the madrasah's substitution tests — إِلَى opposite it, a relative in its place, بَعْض in its place — and the one dispute, redundancy in affirmative speech, where the Kufans and al-Akhfash cite قَدْ كَانَ مِنْ مَطَرٍ and the author answers with two taʾwīls. The remaining letters follow in the next chapters.",
  "tr": "Kâfiye'nin üçüncü kısmı harfle açılır ve defter iki tarifi de şerh etmeden önce aynen verir. Harfin tarifi tek cümlede, قَدْ ظَهَرَ نُورُ الْإِسْلَامِ مِنْ مَكَّةَ'de sınanır; orada her harfin kendini tamamlayan kelimeye uzandığı gösterilir. Cer harfinin tarifi bütün TaalluqEngine'i tek satırda taşır — harf bir fiili ya da fiilin mânâsını bir isme ulaştırır — ve defterin iki şerhi tam olarak motorun iki sınır hâlidir: isim te'villi bir cümle olabilir (9:118 âyeti) ve «fiil mânâsı» kelimeleri sözlüğün fiilî diye işaretlediği ism-i fâil, ism-i mef'ûl ve sıfat-ı müşebbehedir. Yirmilik liste defterin verdiği gibi verilir, rubbe vâvı ve üç kasem harfi ayrı sayılır; çifte ad (cer / izâfet) ilişkinin iki ucundan açıklanır. Sonra ilk ve en meşgul harf مِنْ, medresenin yerine koyma testleriyle — karşısına إِلَى, yerine ism-i mevsûl, yerine بَعْض — ve tek ihtilâf, olumlu kelâmda zâidlik; orada Kûfeliler ve Ahfeş قَدْ كَانَ مِنْ مَطَرٍ'i delil getirir, musannif iki te'ville cevap verir. Kalan harfler sonraki bâblarda gelir."},
 "examples": [
  {"ar": "الْحَرْفُ: مَا دَلَّ عَلَى مَعْنًى فِي غَيْرِهِ", "en": "The particle defined.", "tr": "Harfin tarifi.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "حَرْفُ الْجَرِّ: مَا وُضِعَ لِلْإِفْضَاءِ بِفِعْلٍ أَوْ مَعْنَاهُ إِلَى مَا يَلِيهِ", "en": "The jarr letter defined.", "tr": "Cer harfinin tarifi.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "حَتَّى إِذَا ضَاقَتْ عَلَيْهِمُ الْأَرْضُ بِمَا رَحُبَتْ", "en": "The governed noun in taʾwīl.", "tr": "Te'villi mecrûr.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "سِرْتُ مِنَ الْبَصْرَةِ إِلَى الْكُوفَةِ", "en": "min for beginning, with its ilā test.", "tr": "İbtidâ için min, ilâ testiyle.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "فَاجْتَنِبُوا الرِّجْسَ مِنَ الْأَوْثَانِ — أَخَذْتُ مِنَ الدَّرَاهِمِ", "en": "Explanation and partition.", "tr": "Tebyîn ve teb'îz.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "مَا جَاءَنِي مِنْ أَحَدٍ — قَدْ كَانَ مِنْ مَطَرٍ", "en": "Redundant min, and the disputed affirmative case.", "tr": "Zâid min ve ihtilâflı olumlu hâl.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«مِنْ tek başına bir kelâmdır»",
   "right": "«harf, kelâmın cüz'ü olmak için isme ya da fiile muhtaçtır»",
   "why": {"en": "A particle's meaning lives in another word; alone it says nothing.", "tr": "Harfin mânâsı başka kelimede yaşar; tek başına hiçbir şey söylemez."}},
  {"wrong": "«جَاءَنِي مِنْ أَحَدٍ — zâid min»",
   "right": "«مَا جَاءَنِي مِنْ أَحَدٍ — zâid min yalnız olumlu olmayan kelâmda»",
   "why": {"en": "Redundancy needs a negation, prohibition or question before it, on the author's view.", "tr": "Musannife göre zâidlik öncesinde nefy, nehy ya da istifham ister."}},
  {"wrong": "«أَخَذْتُ مِنَ الدَّرَاهِمِ — ibtidâ için min»",
   "right": "«teb'îz için min — بَعْضَ الدَّرَاهِمِ yerine konabilir»",
   "why": {"en": "Run the substitution test: baʿḍ fits, ilā does not.", "tr": "Yerine koyma testini uygula: ba'z uyar, ilâ uymaz."}},
  {"wrong": "«cer harfleri on altıdır»",
   "right": "«yirmidir — rubbe vâvı ve kasemin vâvı, tâsı, bâsı ayrı sayılır»",
   "why": {"en": "The notebook counts the oath letters and the wāw of rubba as separate letters.", "tr": "Defter kasem harflerini ve rubbe vâvını ayrı harfler sayar."}}],
 "relatedNotes": ["huruf-jarr", "huruf-jarr-nawadir", "al-kalima-wal-kalam", "mana-al-fil", "anwa-ma"]}

ADD_EN = (" Chapter 29 (notebook lines ~331-332): the particle and the jarr letter defined in the notebook's own Arabic (s1, s3); the particle's need of a noun or verb, the governed noun in taʾwīl (9:118), the verb-meaning words, the twenty letters, the two names, and min's four senses with their tests (22:30; the Kufans' قَدْ كَانَ مِنْ مَطَرٍ) — the notebook's exposition, kept as commentary (s2, s4-s10). Qurʾānic text as the source prints it.")
ADD_TR = (" Yirmi dokuzuncu bâb (defter satırları ~331-332): harf ve cer harfi defterin kendi Arapçasıyla tarif edilir (s1, s3); harfin isim ya da fiile ihtiyacı, te'villi mecrûr (9:118), fiil mânâsı kelimeleri, yirmi harf, iki ad ve min'in testleriyle dört mânâsı (22:30; Kûfelilerin قَدْ كَانَ مِنْ مَطَرٍ'i) — defterin açıklaması, şerh olarak (s2, s4-s10). Kur'ân metni kaynağın bastığı gibi.")
write_out(29, S, TITLE, ADD_EN, ADD_TR, "331-332", GLOSS_ADD, notes=(NOTE,),
          related=(("huruf-jarr", [K]), ("al-kalima-wal-kalam", [K])))
report(29, S, GLOSS_ADD, (NOTE,))
