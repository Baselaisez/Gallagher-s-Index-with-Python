# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 22: THE JĀZIMS AND THE AMR. Jazm by لَمْ، لَمَّا, the lām of command, لَا of prohibition and the word of requital;
the notebook on لَمْ against لَمَّا (both negate and turn the sense to the past; لَمَّا is narrower — it denies the whole past up to now —
نَدِمَ آدَمُ وَلَمْ يَنْفَعْهُ النَّدَمُ / نَدِمَ الشَّيْطَانُ وَلَمَّا يَنْفَعْهُ النَّدَمُ; the verb after لَمَّا may be dropped on a clue, قَارَبْتُ الْمَدِينَةَ
وَلَمَّا; the conditional particles enter on لَمْ, not on لَمَّا); the lām of command with its kasra and its sukūn after و ف ثُمَّ; لَا of
prohibition; the word of requital on two verbs, condition and answer; the fāʾ (or إِذَا of surprise) in the answer; the hidden إِنْ after the
five requests, with the Kisāʾī dispute; and the amr defined in the notebook's own Arabic with the Basran–Kufan views of its ending.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~302-306 of the transcription.

  VERBATIM: s10. RESTORED (received matn, marked): s1, s6, s7, s8. COMMENTARY (the notebook): s2-s5, s9, s11.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch22.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "jawazim-al-mudari-wal-amr-fil-kafiya"
NJ = "nawasib-wa-jawazim-al-mudari"
SH = "al-majzum-wal-shart-wal-jaza"
JT = "jawab-al-talab"
TITLE = {"ar": "جَوَازِمُ الْمُضَارِعِ وَالْأَمْرُ", "en": "The jāzims of the muḍāriʿ, and the amr", "tr": "Muzârinin cezm edicileri ve emir"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
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
def JAZM_V(full, lex, en, tr, punct=None, segs=None, extra=" بِالسُّكُونِ", tags=()):
    return cited(full, lex, "verb", [NJ, "fail"] + list(tags), "فِعْلٌ مُضَارِعٌ مَجْزُومٌ" + extra + ".", en, tr, punct=punct, segments=segs)
def JANNA(punct=None): return cited("الْجَنَّةَ", "janna", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Paradise».", "«cennete».", punct=punct)
def NAR(punct=None): return cited("النَّارَ", "nar", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the Fire».", "«cehenneme».", punct=punct)
def TADKHULI(punct=None): return JAZM_V("تَدْخُلِ", "dakhala", "«you enter».", "«girersin».", punct=punct, extra=" بِالسُّكُونِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ — جَوَابُ الطَّلَبِ بِإِنْ مُضْمَرَةٍ", tags=[JT, SH])

# ----------- s1 (RESTORED): the jāzims
S.append({"id": "s1", "translation": {
 "en": "And it takes jazm by لَمْ, لَمَّا, the lām of command, لَا in prohibition, and the word of requital." + R_EN,
 "tr": "لَمْ, لَمَّا, emir lâmı, nehiyde لَا ve mücâzât kelimesiyle meczûm olur." + R_TR},
 "tokens": [
  atf_wa("وَيُجْزَمُ", "jazama", "verb", ["naib-al-fail", NJ], "يُجْزَمُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: الْمُضَارِعُ.", "«and it takes jazm».", "«ve meczûm olur».", "يُجْزَمُ"),
  bi_("بِلَمْ", "lam-jazima", "part", [NJ], "لَمْ فِي مَحَلِّ جَرٍّ.", "«by lam».", "«lem ile».", "لَمْ"),
  cited_wa("وَلَمَّا", "lamma", "part", [NJ], "لَمَّا مَعْطُوفٌ.", "«and lammā».", "«ve lemmâ».", "لَمَّا"),
  atf_wa("وَلَامِ", "lam-letter", "noun", ["idafa-definiteness", NJ], "لَامِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the lām of».", "«ve lâmı».", "لَامِ"),
  W("الْأَمْرِ", "amr-noun", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«command».", "«emir»."),
  cited_wa("وَلَا", "la-nahiya", "part", [NJ, "la-nahiya"], "لَا مَعْطُوفٌ.", "«and lā».", "«ve lâ».", "لَا"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("النَّهْيِ", "nahy", "noun", ["huruf-jarr", "la-nahiya"], "مَجْرُورٌ.", "«prohibition».", "«nehiy»."),
  atf_wa("وَكَلِمَةِ", "kalima", "noun", ["idafa-definiteness", SH], "كَلِمَةِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the word of».", "«ve kelimesiyle».", "كَلِمَةِ"),
  W("الْمُجَازَاةِ", "mujazat", "noun", ["idafa-definiteness", SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَدَوَاتُ الشَّرْطِ.", "«requital» — the conditional particles.", "«mücâzât» — şart edatları.", punct="."),
 ]})

# ----------- s2 (COMMENTARY): لَمْ and لَمَّا
S.append({"id": "s2", "translation": {
 "en": "So لَمْ negates the muḍāriʿ and turns its sense to the past, and لَمَّا is like it in negating and turning, except that it is narrower, since it conveys exhaustion: لَمْ is for absolute negation, لَمَّا for negating the whole of the past up to now." + C_EN,
 "tr": "لَمْ muzâriyi nefy eder ve mânâsını mâzîye çevirir; لَمَّا nefy ve kalbde onun gibidir, ancak istiğrak ifade ettiğinden daha hususîdir: لَمْ mutlak nefy içindir, لَمَّا şimdiye kadar bütün mâzîyi nefy içindir." + C_TR},
 "tokens": [
  cited("فَلَمْ", "lam-jazima", "part", ["mubtada-khabar", NJ, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَمْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so lam».", "«lem».", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  W("تَنْفِي", "nafa", "verb", ["fail", "mubtada-khabar", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْجُمْلَةُ خَبَرٌ.", "«negates».", "«nefy eder»."),
  W("الْمُضَارِعَ", "mudari", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the muḍāriʿ».", "«muzâriyi»."),
  atf_wa("وَتَقْلِبُ", "qalaba", "verb", ["fail"], "تَقْلِبُ فِعْلٌ مُضَارِعٌ مَعْطُوفٌ.", "«and turns».", "«ve çevirir».", "تَقْلِبُ"),
  W("مَعْنَاهُ", "mana", "noun", ["maful-bihi", "idafa-definiteness", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its sense».", "«mânâsını».", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past».", "«mâzîye».", punct="،"),
  cited_wa("وَلَمَّا", "lamma", "part", ["mubtada-khabar", NJ], "لَمَّا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and lammā».", "«ve lemmâ».", "لَمَّا"),
  W("مِثْلُهَا", "mithl", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is like it».", "«onun gibidir».", segments=[seg("مِثْلُ", "mithl", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("النَّفْيِ", "nafy", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«negating».", "«nefy»."),
  atf_wa("وَالْقَلْبِ", "qalb-reversal", "noun", [], "الْقَلْبِ مَعْطُوفٌ مَجْرُورٌ.", "«and turning».", "«ve kalb».", "الْقَلْبِ"),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«ancak»."),
  W("أَنَّهَا", "anna", "part", ["inna-wa-akhawatuha", "istithna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا — وَالْمَصْدَرُ مُسْتَثْنًى.", "«that it».", "«onun».", segments=[seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("أَخَصُّ", "akhass", "noun", ["inna-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is narrower».", "«daha hususîdir»."),
  li_("لِإِفَادَةِ", "ifada", "noun", ["idafa-definiteness"], "إِفَادَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«since it conveys».", "«ifade ettiğinden».", "إِفَادَةِ"),
  W("الِاسْتِغْرَاقِ", "istighraq", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«exhaustion».", "«istiğrak».", punct=":"),
  cited("فَلَمْ", "lam-jazima", "part", ["mubtada-khabar", NJ, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَمْ مُبْتَدَأٌ.", "«so lam».", "«lem».", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  li_("لِلنَّفْيِ", "nafy", "noun", ["mubtada-khabar"], "النَّفْيِ مَجْرُورٌ — خَبَرٌ.", "«is for negation».", "«nefy içindir».", "النَّفْيِ", segs=[seg("لِ", "li", "prep"), seg("لنَّفْيِ", "nafy", "noun")]),
  W("الْمُطْلَقِ", "mutlaq", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«absolute».", "«mutlak».", punct="،"),
  cited_wa("وَلَمَّا", "lamma", "part", ["mubtada-khabar", NJ], "لَمَّا مُبْتَدَأٌ.", "«and lammā».", "«ve lemmâ».", "لَمَّا"),
  li_("لِنَفْيِ", "nafy", "noun", ["mubtada-khabar", "idafa-definiteness"], "نَفْيِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«for negating».", "«nefy içindir».", "نَفْيِ"),
  W("جَمِيعِ", "jami", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the whole of».", "«bütün»."),
  W("الْمَاضِي", "madi", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past».", "«mâzîyi»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«up to».", "«-e kadar»."),
  W("الْآنَ", "al-an", "noun", ["huruf-jarr", "al-mabni-wal-mudmar"], "مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ.", "«now».", "«şimdiye».", punct="."),
 ]})

# ----------- s3 (COMMENTARY): the two examples
S.append({"id": "s3", "translation": {
 "en": "As in: Adam regretted, and regret did not avail him (then — though it did later); and Satan regretted, and regret has not availed him yet." + C_EN,
 "tr": "Meselâ: Âdem pişman oldu ve pişmanlık ona (o anda) fayda vermedi (ama sonra verdi); Şeytan pişman oldu ve pişmanlık ona şimdiye kadar fayda vermedi." + C_TR},
 "tokens": [
  nahwu(),
  cited("نَدِمَ", "nadima", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«regretted».", "«pişman oldu»."),
  cited("آدَمُ", "adam-prophet", "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ.", "«Adam».", "«Âdem»."),
  cited_wa("وَلَمْ", "lam-jazima", "part", [NJ], "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — نَفْيٌ مُطْلَقٌ.", "«and not».", "«ve -medi».", "لَمْ"),
  JAZM_V("يَنْفَعْهُ", "nafaa", "«did … avail him».", "«ona fayda vermedi».", segs=[seg("يَنْفَعْ", "nafaa", "verb"), pr3ms()], extra=" بِالسُّكُونِ، وَالْهَاءُ مَفْعُولٌ بِهِ"),
  cited("النَّدَمُ", "nadam", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«regret».", "«pişmanlık».", punct="،"),
  cited_wa("وَنَدِمَ", "nadima", "verb", ["fail"], "نَدِمَ فِعْلٌ مَاضٍ.", "«and regretted».", "«ve pişman oldu».", "نَدِمَ"),
  cited("الشَّيْطَانُ", "shaytan", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Satan».", "«Şeytan»."),
  cited_wa("وَلَمَّا", "lamma", "part", [NJ], "لَمَّا حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — نَفْيٌ مُسْتَغْرِقٌ إِلَى الْآنَ.", "«and not yet».", "«ve henüz -medi».", "لَمَّا"),
  JAZM_V("يَنْفَعْهُ", "nafaa", "«has … availed him».", "«ona fayda vermedi».", segs=[seg("يَنْفَعْ", "nafaa", "verb"), pr3ms()], extra=" بِالسُّكُونِ، وَالْهَاءُ مَفْعُولٌ بِهِ"),
  cited("النَّدَمُ", "nadam", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«regret».", "«pişmanlık».", punct="."),
 ]})

# ----------- s4 (COMMENTARY): dropping and the conditional particles
S.append({"id": "s4", "translation": {
 "en": "And the verb negated by لَمَّا may be dropped on a clue — as قَارَبْتُ الْمَدِينَةَ وَلَمَّا, that is, وَلَمَّا أَدْخُلْهَا — but not with لَمْ; and the particles of condition enter on لَمْ, not on لَمَّا: one says إِنْ لَمْ يَضْرِبْ and not إِنْ لَمَّا يَضْرِبْ." + C_EN,
 "tr": "لَمَّا ile nefy edilen fiil karîne ile hazfedilebilir — قَارَبْتُ الْمَدِينَةَ وَلَمَّا gibi, yani وَلَمَّا أَدْخُلْهَا — لَمْ ile hazfedilemez; şart edatları لَمْ'in başına gelir, لَمَّا'nın başına gelmez: إِنْ لَمْ يَضْرِبْ denir, إِنْ لَمَّا يَضْرِبْ denmez." + C_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted».", "«ve câizdir».", "يَجُوزُ"),
  W("حَذْفُ", "hadhf", "noun", ["fail", "idafa-definiteness", "hadhf-wa-taqdir"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«dropping».", "«hazfi»."),
  W("الْمَنْفِيِّ", "manfi", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb negated».", "«nefy edilenin»."),
  bi_("بِلَمَّا", "lamma", "part", [NJ], "لَمَّا فِي مَحَلِّ جَرٍّ.", "«by lammā».", "«lemmâ ile».", "لَمَّا"),
  li_("لِقَرِينَةٍ", "qarina", "noun", [], "قَرِينَةٍ مَجْرُورٌ.", "«on a clue».", "«karîne ile».", "قَرِينَةٍ"),
  nahwu(),
  cited("قَارَبْتُ", "qaraba-near", "verb", ["fail", "form-iii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I drew near».", "«yaklaştım».", segments=[seg("قَارَبْ", "qaraba-near", "verb"), prT()]),
  cited("الْمَدِينَةَ", "madina", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the city».", "«şehre»."),
  cited_wa("وَلَمَّا", "lamma", "part", [NJ, "hadhf-wa-taqdir"], "لَمَّا حَرْفُ نَفْيٍ وَجَزْمٍ، وَمَجْزُومُهَا مَحْذُوفٌ.", "«and not yet» — its verb dropped.", "«ve henüz» — fiili mahzûf.", "لَمَّا", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["al-mabni-wal-mudmar"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».", punct=":"),
  cited_wa("وَلَمَّا", "lamma", "part", [NJ], "لَمَّا حَرْفُ نَفْيٍ وَجَزْمٍ.", "«and not yet».", "«ve henüz».", "لَمَّا"),
  JAZM_V("أَدْخُلْهَا", "dakhala", "«have I entered it».", "«girmedim».", punct="،", segs=[seg("أَدْخُلْ", "dakhala", "verb"), pr3fs()], extra=" بِالسُّكُونِ، وَهَا مَفْعُولٌ بِهِ — الْمَحْذُوفُ الْمُقَدَّرُ", tags=["hadhf-wa-taqdir"]),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«but not».", "«ama -mez».", "لَا"),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: الْحَذْفُ.", "«is it permitted».", "«câiz olur»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  cited("لَمْ", "lam-jazima", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«lam».", "«lem».", punct="؛"),
  atf_wa("وَتَدْخُلُ", "dakhala", "verb", ["fail"], "تَدْخُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and enter».", "«ve gelir».", "تَدْخُلُ"),
  W("أَدَوَاتُ", "adat", "noun", ["fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the particles of».", "«edatları»."),
  W("الشَّرْطِ", "shart", "noun", ["idafa-definiteness", SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«condition».", "«şart»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«başına»."),
  cited("لَمْ", "lam-jazima", "part", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«lam».", "«lem'in»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«değil»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "atf-nasaq"], "حَرْفُ جَرٍّ.", "«on».", "«başına»."),
  cited("لَمَّا", "lamma", "part", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«lammā».", "«lemmâ'nın».", punct=":"),
  W("فَيُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«so one says».", "«denir».", segments=[seg("فَ", "fa", "conj"), seg("يُقَالُ", "qala", "verb")]),
  cited("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  cited("لَمْ", "lam-jazima", "part", [NJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me-»."),
  JAZM_V("يَضْرِبْ", "daraba", "«he strikes».", "«vurmazsa»."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -mez».", "لَا"),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«does one say».", "«denmez»."),
  cited("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  cited("لَمَّا", "lamma", "part", [NJ], "حَرْفُ نَفْيٍ وَجَزْمٍ — لَا يَدْخُلُ عَلَيْهَا الشَّرْطُ.", "«not yet».", "«henüz -me-»."),
  JAZM_V("يَضْرِبْ", "daraba", "«he strikes».", "«vurmazsa».", punct="."),
 ]})

# ----------- s5 (COMMENTARY): the lām of command and لَا of prohibition
S.append({"id": "s5", "translation": {
 "en": "And the lām of command carries a kasra and the act is asked for by it — as لِيَنْصُرْ — and it is made quiescent after the wāw, the fāʾ and ثُمَّ for lightness — as وَلْتَأْتِ طَائِفَةٌ أُخْرَى and فَلْيُصَلُّوا; and the لَا of prohibition is that by which leaving the act is asked — as لَا يَنْصُرْ and لَا تَنْصُرْ." + C_EN,
 "tr": "Emir lâmı meksûrdur ve onunla fiil talep edilir — لِيَنْصُرْ gibi — vâv, fâ ve ثُمَّ'den sonra hafiflik için sâkin kılınır — وَلْتَأْتِ طَائِفَةٌ أُخْرَى ve فَلْيُصَلُّوا gibi; nehiy lâ'sı, onunla fiilin terki talep edilendir — لَا يَنْصُرْ ve لَا تَنْصُرْ gibi." + C_TR},
 "tokens": [
  atf_wa("وَلَامُ", "lam-letter", "noun", ["mubtada-khabar", "idafa-definiteness", NJ], "لَامُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the lām of».", "«ve lâmı».", "لَامُ"),
  W("الْأَمْرِ", "amr-noun", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«command».", "«emir»."),
  W("مَكْسُورَةٌ", "maksur", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«carries a kasra».", "«meksûrdur»."),
  W("يُطْلَبُ", "talaba", "verb", ["naib-al-fail", "naat-sifa"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ حَالٌ أَوْ خَبَرٌ ثَانٍ.", "«is asked for».", "«talep edilir»."),
  bi_("بِهَا", "bi", "prep", [], "هَا مَجْرُورٌ.", "«by it».", "«onunla».", "هَا", segs=[seg("بِ", "bi", "prep"), pr3fs()]),
  W("الْفِعْلُ", "fil", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the act».", "«fiil»."),
  nahwu(),
  cited("لِيَنْصُرْ", "nasara", "verb", [NJ, "fail"], "اللَّامُ لَامُ الْأَمْرِ، وَيَنْصُرْ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ.", "«let him help».", "«yardım etsin».", punct="،", segments=[seg("لِ", "lam-amr", "part"), seg("يَنْصُرْ", "nasara", "verb")]),
  atf_wa("وَتُسَكَّنُ", "sakkana", "verb", ["naib-al-fail", "form-ii-verbs"], "تُسَكَّنُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«and it is made quiescent».", "«ve sâkin kılınır».", "تُسَكَّنُ"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... -den sonra»."),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wāw».", "«vâv»."),
  atf_wa("وَالْفَاءِ", "fa", "conj", [], "الْفَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«the fāʾ».", "«fâ».", "الْفَاءِ"),
  cited_wa("وَثُمَّ", "thumma", "conj", [], "ثُمَّ مَعْطُوفٌ.", "«and thumma».", "«ve sümme».", "ثُمَّ"),
  W("تَخْفِيفًا", "takhfif", "noun", ["maful-lah"], "مَفْعُولٌ لَهُ مَنْصُوبٌ.", "«for lightness».", "«hafiflik için»."),
  nahwu(),
  cited_wa("وَلْتَأْتِ", "ata", "verb", [NJ, "fail", "ism-maqsur-manqus"], "اللَّامُ لَامُ الْأَمْرِ سُكِّنَتْ بَعْدَ الْوَاوِ، وَتَأْتِ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ الْيَاءِ.", "«and let … come».", "«ve gelsin».", "لْ", extra_segs=[seg("لْ", "lam-amr", "part"), seg("تَأْتِ", "ata", "verb")]),
  cited("طَائِفَةٌ", "taifa", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a party».", "«bir grup»."),
  cited("أُخْرَى", "ukhra", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«another».", "«başka».", punct="،"),
  cited("فَلْيُصَلُّوا", "salla", "verb", [NJ, "fail"], "الْفَاءُ عَاطِفَةٌ، وَاللَّامُ لَامُ الْأَمْرِ سَاكِنَةٌ، وَيُصَلُّوا مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَكَذَا بَعْدَ ثُمَّ.", "«then let them pray» — and likewise after ثُمَّ.", "«sonra namaz kılsınlar» — ثُمَّ'den sonra da öyle.", punct="؛", segments=[seg("فَ", "fa", "conj"), seg("لْ", "lam-amr", "part"), seg("يُصَلُّوا", "salla", "verb")]),
  cited_wa("وَلَا", "la-nahiya", "part", ["mubtada-khabar", NJ, "la-nahiya"], "لَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and lā».", "«ve lâ».", "لَا"),
  W("النَّاهِيَةُ", "nahiya-la", "noun", ["naat-sifa", "la-nahiya"], "صِفَةٌ مَرْفُوعَةٌ.", "«of prohibition».", "«nâhiye»."),
  W("يُطْلَبُ", "talaba", "verb", ["naib-al-fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ خَبَرٌ.", "«is that by which … is asked».", "«talep edilir»."),
  bi_("بِهَا", "bi", "prep", [], "هَا مَجْرُورٌ.", "«by it».", "«onunla».", "هَا", segs=[seg("بِ", "bi", "prep"), pr3fs()]),
  W("تَرْكُ", "tark", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«leaving».", "«terki»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the act».", "«fiilin»."),
  nahwu(),
  cited("لَا", "la-nahiya", "part", [NJ, "la-nahiya"], "نَاهِيَةٌ جَازِمَةٌ.", "«let … not».", "«-mesin»."),
  JAZM_V("يَنْصُرْ", "nasara", "«him help».", "«yardım etmesin»."),
  cited_wa("وَلَا", "la-nahiya", "part", [NJ, "la-nahiya"], "لَا نَاهِيَةٌ جَازِمَةٌ.", "«and do not».", "«ve -me».", "لَا"),
  JAZM_V("تَنْصُرْ", "nasara", "«you help».", "«yardım etme».", punct="."),
 ]})

# ----------- s6 (RESTORED): the word of requital
S.append({"id": "s6", "translation": {
 "en": "And the word of requital enters on two verbs so that the first is a cause and the second its effect, and they are named condition and answer — as إِنْ تَزُرْنِي أَزُرْكَ." + R_EN,
 "tr": "Mücâzât kelimesi, birincisi sebep ikincisi müsebbeb olmak üzere iki fiilin üzerine girer; bu ikisi şart ve cezâ diye adlandırılır — إِنْ تَزُرْنِي أَزُرْكَ gibi." + R_TR},
 "tokens": [
  atf_wa("وَكَلِمَةُ", "kalima", "noun", ["mubtada-khabar", "idafa-definiteness", SH], "كَلِمَةُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the word of».", "«ve kelimesi».", "كَلِمَةُ"),
  W("الْمُجَازَاةِ", "mujazat", "noun", ["idafa-definiteness", SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«requital».", "«mücâzât»."),
  W("تَدْخُلُ", "dakhala", "verb", ["fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«enters».", "«girer»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("فِعْلَيْنِ", "fil", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ.", "«two verbs».", "«iki fiilin»."),
  li_("لِكَوْنِ", "kawn", "noun", ["idafa-definiteness"], "كَوْنِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«so that … is».", "«olması için».", "كَوْنِ"),
  W("الْأَوَّلِ", "awwal", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَصْدَرِ.", "«the first».", "«birincisi»."),
  W("سَبَبًا", "sabab", "noun", ["kana-wa-akhawatuha", SH], "خَبَرُ الْمَصْدَرِ مَنْصُوبٌ.", "«a cause».", "«sebep»."),
  atf_wa("وَالثَّانِي", "thani", "noun", ["ism-maqsur-manqus"], "الثَّانِي مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«and the second».", "«ve ikincisi».", "الثَّانِي"),
  W("مُسَبَّبًا", "musabbab", "noun", ["kana-wa-akhawatuha", SH], "مَعْطُوفٌ مَنْصُوبٌ.", "«its effect».", "«müsebbeb».", punct="،"),
  atf_wa("وَيُسَمَّيَانِ", "samma", "verb", ["naib-al-fail", "al-muthanna", "form-ii-verbs"], "يُسَمَّيَانِ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ.", "«and they are named».", "«ve adlandırılırlar».", "يُسَمَّيَانِ"),
  W("شَرْطًا", "shart", "noun", ["mafulayn", SH], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«condition».", "«şart»."),
  atf_wa("وَجَزَاءً", "jaza-answer", "noun", [SH], "جَزَاءً مَعْطُوفٌ مَنْصُوبٌ.", "«and answer».", "«ve cezâ».", "جَزَاءً", punct="،"),
  nahwu(),
  cited("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ.", "«if».", "«eğer»."),
  JAZM_V("تَزُرْنِي", "zara", "«you visit me».", "«beni ziyaret edersen».", segs=[seg("تَزُرْ", "zara", "verb"), pr1s()], extra=" بِالسُّكُونِ — فِعْلُ الشَّرْطِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ", tags=[SH, "hollow-verbs"]),
  JAZM_V("أَزُرْكَ", "zara", "«I visit you».", "«seni ziyaret ederim».", punct=".", segs=[seg("أَزُرْ", "zara", "verb"), pr2ms()], extra=" بِالسُّكُونِ — جَوَابُ الشَّرْطِ، وَالْكَافُ مَفْعُولٌ بِهِ", tags=[SH, "hollow-verbs"]),
 ]})

# ----------- s7 (RESTORED): the fāʾ and إِذَا in the answer
S.append({"id": "s7", "translation": {
 "en": "And when the answer is a nominal sentence, or a muḍāriʿ negated by مَا or لَنْ, the fāʾ is required, and إِذَا of surprise may stand in its place in the nominal — as وَإِنْ تُصِبْهُمْ سَيِّئَةٌ بِمَا قَدَّمَتْ أَيْدِيهِمْ إِذَا هُمْ يَقْنَطُونَ." + R_EN,
 "tr": "Cezâ isim cümlesi ya da مَا veya لَنْ ile menfî muzâri olduğunda fâ lâzım gelir; isim cümlesinde onun yerine mufâcee izâsı da gelebilir — وَإِنْ تُصِبْهُمْ سَيِّئَةٌ بِمَا قَدَّمَتْ أَيْدِيهِمْ إِذَا هُمْ يَقْنَطُونَ gibi." + R_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... olduğunda».", "إِذَا"),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«olursa»."),
  W("الْجَزَاءُ", "jaza-answer", "noun", ["kana-wa-akhawatuha", SH], "اسْمُ كَانَ مَرْفُوعٌ.", "«the answer».", "«cezâ»."),
  W("جُمْلَةً", "jumla", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a sentence».", "«cümle»."),
  W("اسْمِيَّةً", "ismiyya", "noun", ["naat-sifa", "al-fa-fi-jawab-al-shart"], "صِفَةٌ مَنْصُوبَةٌ.", "«nominal».", "«isim»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("مُضَارِعًا", "mudari", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«a muḍāriʿ».", "«muzâri»."),
  W("مَنْفِيًّا", "manfi", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَنْصُوبَةٌ.", "«negated».", "«menfî»."),
  bi_("بِمَا", "ma-nafiya", "part", ["ma-la-laysa-wa-la-al-jins"], "مَا فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«by mā».", "«mâ ile».", "مَا"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  cited("لَنْ", "lan", "part", ["atf-nasaq", NJ], "مَعْطُوفٌ.", "«lan».", "«len»."),
  W("لَزِمَتِ", "lazima", "verb", ["fail", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — جَوَابُ إِذَا.", "«is required».", "«lâzım gelir»."),
  W("الْفَاءُ", "fa", "conj", ["fail", "al-fa-fi-jawab-al-shart"], "فَاعِلٌ مَرْفُوعٌ.", "«the fāʾ».", "«fâ».", punct="،"),
  atf_wa("وَتَقُومُ", "qama", "verb", ["fail", "hollow-verbs"], "تَقُومُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and … may stand».", "«ve gelebilir».", "تَقُومُ"),
  cited("إِذَا", "idha", "part", ["fail", "al-fa-fi-jawab-al-shart"], "فِي مَحَلِّ رَفْعٍ فَاعِلٌ — الْحَرْفُ مَحْكِيٌّ.", "«idhā».", "«izâ»."),
  W("الْمُفَاجَأَةِ", "mufajaa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of surprise».", "«mufâcee»."),
  W("مَقَامَهَا", "maqam", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«in its place».", "«onun yerine».", segments=[seg("مَقَامَ", "maqam", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الِاسْمِيَّةِ", "ismiyya", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the nominal».", "«isim cümlesinde».", punct="،"),
  nahwu(),
  cited_wa("وَإِنْ", "in-shartiyya", "part", [SH, "in-shartiyya"], "إِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«ve eğer».", "إِنْ"),
  JAZM_V("تُصِبْهُمْ", "asaba", "«befalls them».", "«onlara isabet ederse».", segs=[seg("تُصِبْ", "asaba", "verb"), pr3mp()], extra=" بِالسُّكُونِ — فِعْلُ الشَّرْطِ، حُذِفَتْ عَيْنُهُ، وَهُمْ مَفْعُولٌ بِهِ", tags=[SH, "form-iv-verbs", "hollow-verbs"]),
  cited("سَيِّئَةٌ", "sayyia", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«an evil».", "«bir kötülük»."),
  cited("بِمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "الْبَاءُ لِلسَّبَبِيَّةِ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«because of what».", "«... sebebiyle».", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  cited("قَدَّمَتْ", "qaddama", "verb", ["ism-mawsul", "fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — صِلَةُ مَا.", "«have sent ahead».", "«işlediği»."),
  cited("أَيْدِيهِمْ", "yad", "noun", ["fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their hands».", "«elleri».", segments=[seg("أَيْدِي", "yad", "noun"), pr3mp()]),
  cited("إِذَا", "idha", "part", [SH, "al-fa-fi-jawab-al-shart"], "إِذَا الْمُفَاجَأَةِ، قَامَتْ مَقَامَ الْفَاءِ فِي جَوَابِ الشَّرْطِ.", "«at once» — in the fāʾ's place.", "«hemen» — fânın yerinde."),
  cited("هُمْ", "huwa", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«they».", "«onlar»."),
  cited("يَقْنَطُونَ", "qanita", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ جَوَابُ الشَّرْطِ.", "«despair».", "«ümit keserler».", punct="."),
 ]})

# ----------- s8 (RESTORED): the hidden إِنْ after the five
S.append({"id": "s8", "translation": {
 "en": "And the muḍāriʿ takes jazm by a hidden إِنْ after a command, a prohibition, a question, a wish and an offer when cause is intended — as أَسْلِمْ تَدْخُلِ الْجَنَّةَ, لَا تَكْفُرْ تَدْخُلِ الْجَنَّةَ, هَلْ عِنْدَكُمْ مَاءٌ أَشْرَبْهُ, لَيْتَ لِي مَالًا أُنْفِقْهُ, أَلَا تَنْزِلُ تُصِبْ خَيْرًا." + R_EN,
 "tr": "Sebebiyet kastedildiğinde muzâri emir, nehiy, istifhâm, temennî ve arzdan sonra gizli bir إِنْ ile meczûm olur — أَسْلِمْ تَدْخُلِ الْجَنَّةَ, لَا تَكْفُرْ تَدْخُلِ الْجَنَّةَ, هَلْ عِنْدَكُمْ مَاءٌ أَشْرَبْهُ, لَيْتَ لِي مَالًا أُنْفِقْهُ, أَلَا تَنْزِلُ تُصِبْ خَيْرًا gibi." + R_TR},
 "tokens": [
  atf_wa("وَيُجْزَمُ", "jazama", "verb", ["naib-al-fail", NJ], "يُجْزَمُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … takes jazm».", "«ve meczûm olur».", "يُجْزَمُ"),
  W("الْمُضَارِعُ", "mudari", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the muḍāriʿ».", "«muzâri»."),
  bi_("بِإِنْ", "in-shartiyya", "part", [SH, JT, "hadhf-wa-taqdir"], "إِنْ فِي مَحَلِّ جَرٍّ.", "«by in».", "«in ile».", "إِنْ"),
  W("مُضْمَرَةٍ", "mudmar", "noun", ["naat-sifa", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«hidden».", "«gizli»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... -den sonra»."),
  W("الْأَمْرِ", "amr-noun", "noun", ["idafa-definiteness", JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a command».", "«emir»."),
  atf_wa("وَالنَّهْيِ", "nahy", "noun", [JT], "النَّهْيِ مَعْطُوفٌ.", "«a prohibition».", "«nehiy».", "النَّهْيِ"),
  atf_wa("وَالِاسْتِفْهَامِ", "istifham", "noun", [JT], "الِاسْتِفْهَامِ مَعْطُوفٌ.", "«a question».", "«istifhâm».", "الِاسْتِفْهَامِ"),
  atf_wa("وَالتَّمَنِّي", "tamanni", "noun", [JT, "ism-maqsur-manqus"], "التَّمَنِّي مَعْطُوفٌ.", "«a wish».", "«temennî».", "التَّمَنِّي"),
  atf_wa("وَالْعَرْضِ", "ard-offer", "noun", [JT], "الْعَرْضِ مَعْطُوفٌ.", "«and an offer».", "«ve arz».", "الْعَرْضِ"),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("قُصِدَتِ", "qasada", "verb", ["naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«is intended».", "«kastedildiğinde»."),
  W("السَّبَبِيَّةُ", "sababiyya", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«cause».", "«sebebiyet».", punct="،"),
  nahwu(),
  cited("أَسْلِمْ", "aslama", "verb", ["fail", JT, "form-iv-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«become Muslim».", "«müslüman ol»."),
  TADKHULI(),
  JANNA(punct="،"),
  cited("لَا", "la-nahiya", "part", ["la-nahiya", JT], "نَاهِيَةٌ جَازِمَةٌ.", "«do not».", "«-me»."),
  JAZM_V("تَكْفُرْ", "kafara", "«disbelieve».", "«inkâr etme».", tags=["la-nahiya", JT]),
  TADKHULI(),
  JANNA(punct="،"),
  cited("هَلْ", "hal-istifham", "part", ["adawat-al-tasawwur", JT], "حَرْفُ اسْتِفْهَامٍ.", "«is there».", "«var mı»."),
  cited("عِنْدَكُمْ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَكُمْ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«with you».", "«sizde».", segments=[seg("عِنْدَ", "inda", "noun"), pr2mp()]),
  cited("مَاءٌ", "ma-water", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«water».", "«su»."),
  JAZM_V("أَشْرَبْهُ", "shariba", "«that I may drink».", "«içeyim».", punct="،", segs=[seg("أَشْرَبْ", "shariba", "verb"), pr3ms()], extra=" بِالسُّكُونِ — جَوَابُ الِاسْتِفْهَامِ بِإِنْ مُضْمَرَةٍ، وَالْهَاءُ مَفْعُولٌ بِهِ", tags=[JT, SH]),
  cited("لَيْتَ", "layta", "part", ["inna-wa-akhawatuha", JT], "حَرْفُ تَمَنٍّ وَنَصْبٍ.", "«would that».", "«keşke»."),
  cited("لِي", "li", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ — خَبَرُ لَيْتَ.", "«I had».", "«benim».", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  cited("مَالًا", "mal", "noun", ["inna-wa-akhawatuha"], "اسْمُ لَيْتَ مَنْصُوبٌ.", "«wealth».", "«malım olsa»."),
  JAZM_V("أُنْفِقْهُ", "anfaqa", "«I would spend it».", "«harcayayım».", punct="،", segs=[seg("أُنْفِقْ", "anfaqa", "verb"), pr3ms()], extra=" بِالسُّكُونِ — جَوَابُ التَّمَنِّي بِإِنْ مُضْمَرَةٍ، وَالْهَاءُ مَفْعُولٌ بِهِ", tags=[JT, SH, "form-iv-verbs"]),
  cited("أَلَا", "ala-tanbih", "part", [JT], "حَرْفُ عَرْضٍ.", "«won't you».", "«-mez misin»."),
  cited("تَنْزِلُ", "nazala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«come down».", "«inmez misin»."),
  JAZM_V("تُصِبْ", "asaba", "«you would find».", "«erişirsin».", extra=" بِالسُّكُونِ — جَوَابُ الْعَرْضِ بِإِنْ مُضْمَرَةٍ، حُذِفَتْ عَيْنُهُ", tags=[JT, SH, "form-iv-verbs", "hollow-verbs"]),
  cited("خَيْرًا", "khayr", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«good».", "«hayra».", punct="."),
 ]})

# ----------- s9 (COMMENTARY): the Kisāʾī dispute
S.append({"id": "s9", "translation": {
 "en": "And for the majority لَا تَكْفُرْ تَدْخُلِ النَّارَ is not said, since its supplied form is إِنْ لَا تَكْفُرْ تَدْخُلِ النَّارَ; and it is permitted for al-Kisāʾī, since its sense by usage is: if you disbelieve you enter the Fire." + C_EN,
 "tr": "Cumhûra göre لَا تَكْفُرْ تَدْخُلِ النَّارَ denmez, çünkü takdîri إِنْ لَا تَكْفُرْ تَدْخُلِ النَّارَ'dır; Kisâî'ye göre câizdir, çünkü örfen mânâsı: inkâr edersen cehenneme girersin." + C_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -mez».", "لَا"),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is it said».", "«denir»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْجُمْهُورِ", "jumhur", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the majority».", "«cumhûra»."),
  cited("لَا", "la-nahiya", "part", ["la-nahiya", JT], "نَاهِيَةٌ.", "«do not».", "«-me»."),
  JAZM_V("تَكْفُرْ", "kafara", "«disbelieve».", "«inkâr etme».", tags=["la-nahiya"]),
  TADKHULI(),
  NAR(punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«since».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("تَقْدِيرَهُ", "taqdir", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "hadhf-wa-taqdir"], "اسْمُ أَنَّ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its supplied form».", "«takdîri».", punct=":", segments=[seg("تَقْدِيرَ", "taqdir", "noun"), pr3ms()]),
  cited("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya", "inna-wa-akhawatuha"], "حَرْفُ شَرْطٍ — وَالْجُمْلَةُ الْمَحْكِيَّةُ خَبَرُ أَنَّ.", "«if».", "«eğer»."),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-me-»."),
  JAZM_V("تَكْفُرْ", "kafara", "«you disbelieve».", "«inkâr etmezsen».", tags=[SH]),
  TADKHULI(),
  NAR(punct="؛"),
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هُوَ"),
  W("جَائِزٌ", "jaiz", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«permitted».", "«câizdir»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْكِسَائِيِّ", "kisai", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Kisāʾī».", "«Kisâî'ye».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«since».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("مَعْنَاهُ", "mana", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "اسْمُ أَنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its sense».", "«mânâsı».", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  W("عُرْفًا", "urf", "noun", ["hal"], "حَالٌ مَنْصُوبٌ، أَوْ تَمْيِيزٌ.", "«by usage».", "«örfen».", punct=":"),
  cited("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya", "inna-wa-akhawatuha"], "حَرْفُ شَرْطٍ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«if».", "«eğer»."),
  JAZM_V("تَكْفُرْ", "kafara", "«you disbelieve».", "«inkâr edersen».", tags=[SH]),
  TADKHULI(),
  NAR(punct="."),
 ]})

# ----------- s10 (VERBATIM): the amr
S.append({"id": "s10", "translation": {
 "en": "The amr: a form by which the act is asked of the addressed doer, by dropping the letter of muḍāraʿa.",
 "tr": "Emir: muzâraat harfinin hazfiyle, muhâtab olan fâilden kendisiyle fiil talep edilen sîgadır."},
 "tokens": [
  W("الْأَمْرُ", "amr-noun", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the amr».", "«emir».", punct=":"),
  W("صِيغَةٌ", "sigha", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a form».", "«sîga»."),
  W("يُطْلَبُ", "talaba", "verb", ["naib-al-fail", "naat-sifa"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِفَةٌ لِصِيغَةٌ.", "«is asked».", "«talep edilen»."),
  bi_("بِهَا", "bi", "prep", [], "هَا مَجْرُورٌ.", "«by which».", "«kendisiyle».", "هَا", segs=[seg("بِ", "bi", "prep"), pr3fs()]),
  W("الْفِعْلُ", "fil", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the act».", "«fiil»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the doer».", "«fâilden»."),
  W("الْمُخَاطَبِ", "mukhatab", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«addressed».", "«muhâtab»."),
  bi_("بِحَذْفِ", "hadhf", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"], "حَذْفِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by dropping».", "«hazfiyle».", "حَذْفِ"),
  W("حَرْفِ", "harf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the letter of».", "«harfinin»."),
  W("الْمُضَارَعَةِ", "mudaraa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«muḍāraʿa».", "«muzâraat».", punct="."),
 ]})

# ----------- s11 (COMMENTARY): the ending
S.append({"id": "s11", "translation": {
 "en": "And the ruling of its ending for the Basrans is the ruling of the muḍāriʿ in jazm — so it is built on the pause and is like a jazm in form — and for the Kufans it is declined, in jazm by a supplied lām." + C_EN,
 "tr": "Sonunun hükmü Basralılara göre meczûm muzârinin hükmüdür — vakf üzere mebnîdir, lafızda meczûm gibidir — Kûfelilere göre ise mu'rebdir, mukadder bir lâm ile meczûmdur." + C_TR},
 "tokens": [
  atf_wa("وَحُكْمُ", "hukm", "noun", ["mubtada-khabar", "idafa-definiteness"], "حُكْمُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the ruling of».", "«ve hükmü».", "حُكْمُ"),
  W("آخِرِهِ", "akhir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its ending».", "«sonunun».", segments=[seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْبَصْرِيِّينَ", "basri", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Basrans».", "«Basralılara»."),
  W("حُكْمُ", "hukm", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the ruling of».", "«hükmüdür»."),
  W("الْمُضَارِعِ", "mudari", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāriʿ».", "«muzârinin»."),
  W("الْمَجْزُومِ", "majzum", "noun", ["naat-sifa", "ism-maful", NJ], "صِفَةٌ مَجْرُورَةٌ.", "«in jazm».", "«meczûm».", punct="،"),
  W("فَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ.", "«so it».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  W("مَبْنِيٌّ", "mabni", "noun", ["mubtada-khabar", "al-mabni-wal-mudmar"], "خَبَرٌ مَرْفُوعٌ.", "«is built».", "«mebnîdir»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْوَقْفِ", "waqf", "noun", ["huruf-jarr", "al-mabni-wal-mudmar"], "مَجْرُورٌ — السُّكُونُ.", "«the pause» — the sukūn.", "«vakf» — sükûn."),
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هُوَ"),
  W("كَالْمَجْزُومِ", "majzum", "noun", ["huruf-jarr", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَالْمَجْزُومِ مَجْرُورٌ — خَبَرٌ.", "«is like a jazm».", "«meczûm gibidir».", segments=[seg("كَ", "ka", "prep"), seg("الْمَجْزُومِ", "majzum", "noun")]),
  W("لَفْظًا", "lafz", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in form».", "«lafzan».", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْكُوفِيِّينَ", "kufi", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Kufans».", "«Kûfelilere»."),
  W("هُوَ", "huwa", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«it».", "«o»."),
  W("مُعْرَبٌ", "murab", "noun", ["mubtada-khabar", "al-murab-wal-mabni-wal-irab"], "خَبَرٌ مَرْفُوعٌ.", "«is declined».", "«mu'rebdir»."),
  W("مَجْزُومٌ", "majzum", "noun", ["naat-sifa", NJ], "صِفَةٌ مَرْفُوعَةٌ، أَوْ خَبَرٌ ثَانٍ.", "«in jazm».", "«meczûm»."),
  bi_("بِلَامٍ", "lam-letter", "noun", [], "لَامٍ مَجْرُورٌ.", "«by a lām».", "«bir lâm ile».", "لَامٍ"),
  W("مُقَدَّرَةٍ", "muqaddar", "noun", ["naat-sifa", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«supplied».", "«mukadder».", punct="."),
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
 "mujazat": need("mujazat", "مُجَازَاة", "ج ز ي", "noun", "requital — the Kafiya's name for the conditional construction and its particles", "mücâzât — Kâfiye'nin şart yapısına ve edatlarına verdiği ad", 5),
 "istighraq": need("istighraq", "اِسْتِغْرَاق", "غ ر ق", "noun", "exhaustion of a span — the sense that makes لَمَّا narrower than لَمْ", "istiğrak, bir süreyi bütünüyle kaplama — لَمَّا'yı لَمْ'den hususî kılan mânâ", 5),
 "ifada": need("ifada", "إِفَادَة", "ف ي د", "noun", "conveying, giving a meaning — the maṣdar of أَفَادَ", "ifade, bir mânâ verme — efâde'nin masdarı", 4),
 "nadima": need("nadima", "نَدِمَ", "ن د م", "verb", "to regret", "pişman olmak", 3),
 "nadam": need("nadam", "نَدَم", "ن د م", "noun", "regret", "pişmanlık", 3),
 "qaraba-near": need("qaraba-near", "قَارَبَ", "ق ر ب", "verb", "to draw near to (Form III)", "yaklaşmak (III. bâb)", 4),
 "ismiyya": need("ismiyya", "اِسْمِيَّة", "س م و", "noun", "nominal (of a sentence) — one opening with a noun", "ismiyye (cümle için) — isimle başlayan", 3),
 "sakkana": need("sakkana", "سَكَّنَ", "س ك ن", "verb", "to make quiescent, to put a sukūn on (Form II)", "sâkin kılmak, sükûn vermek (II. bâb)", 4),
 "nahiya-la": need("nahiya-la", "نَاهِيَة", "ن ه ي", "noun", "prohibiting — the لَا that asks for an act to be left", "nâhiye — fiilin terkini isteyen لَا", 3),
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
put_morph(mo, "nadima", _sg.sound1("samia", "نَدِم", "نْدَم", "اِنْدَم", "نَدَم", "نَادِم", None, None, None, "نَدِمَ عَلَى الشَّيْءِ يَنْدَمُ نَدَمًا: أَسِفَ عَلَيْهِ — مِنْ بَابِ سَمِعَ، لَازِمٌ."))
put_morph(mo, "sakkana", _sg.derived(_sg.B2, _sg.W2, "ُ", "سَكَّن", "سَكِّن", "سَكِّن", "تَسْكِين", "مُسَكِّن", "مُسَكَّن", "سُكِّنَ", "يُسَكَّنُ", "سَكَّنَ الْحَرْفَ يُسَكِّنُهُ تَسْكِينًا: جَعَلَهُ سَاكِنًا — الْبَابُ الثَّانِي."))
put_morph(mo, "qaraba-near", _sg.derived(_sg.B3, _sg.W3, "ُ", "قَارَب", "قَارِب", "قَارِب", "مُقَارَبَة", "مُقَارِب", "مُقَارَب", "قُورِبَ", "يُقَارَبُ", "قَارَبَ الشَّيْءَ يُقَارِبُهُ مُقَارَبَةً: دَنَا مِنْهُ — بَابُ الْمُفَاعَلَةِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch22 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "جَوَازِمُ الْمُضَارِعِ وَالْأَمْرُ فِي الْكَافِيَةِ", "en": "The jāzims of the muḍāriʿ in the Kafiya — لَمْ against لَمَّا, the lām of command, لَا of prohibition, the word of requital with its fāʾ and its hidden إِنْ — and the amr with its disputed ending", "tr": "Kâfiye'de muzârinin cezm edicileri — لَمْ ile لَمَّا, emir lâmı, nehiy lâ'sı, fâsı ve gizli إِنْ'iyle mücâzât kelimesi — ve ihtilâflı sonuyla emir"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الجزم بلم ولما ولام الأمر ولا في النهي وكلمة المجازاة؛ كلمة المجازاة تدخل على فعلين؛ الفاء وإذا المفاجأة في الجزاء؛ الجزم بإن مضمرة بعد الأمر والنهي والاستفهام والتمني والعرض؛ الأمر: صيغة يطلب بها الفعل من الفاعل المخاطب بحذف حرف المضارعة", "ضياء صونغور اوغلى — دفتر الكافية: لم ولما، الاستغراق، ندم آدم وندم الشيطان، قاربت المدينة ولما، إن لم لا إن لما؛ لام الأمر وتسكينها؛ لا تكفر تدخل النار بين الجمهور والكسائي؛ آخر الأمر بين البصريين والكوفيين"],
 "question": {
  "en": ["What puts a muḍāriʿ in JAZM? Five things: لَمْ, لَمَّا, the lām of command, لَا of prohibition, and the «word of requital» — the conditional particles, إِنْ chief among them.",
         "How do لَمْ and لَمَّا differ? Both negate and both turn the verb's time to the past. لَمَّا adds exhaustion — «not up to this moment» — so it is narrower: نَدِمَ آدَمُ وَلَمْ يَنْفَعْهُ النَّدَمُ leaves room for later help; نَدِمَ الشَّيْطَانُ وَلَمَّا يَنْفَعْهُ النَّدَمُ closes it. Two consequences: the verb after لَمَّا may be dropped on a clue (قَارَبْتُ الْمَدِينَةَ وَلَمَّا), never after لَمْ; and إِنْ may enter on لَمْ, never on لَمَّا.",
         "What of the lām of command? It takes a kasra (لِيَنْصُرْ) and goes quiescent after وَ, فَ and ثُمَّ (وَلْتَأْتِ، فَلْيُصَلُّوا). The لَا of prohibition asks for the act to be LEFT (لَا تَنْصُرْ) — same jazm, opposite request.",
         "How does the condition work? The particle enters on two verbs and makes the first the cause of the second — condition and answer, both in jazm: إِنْ تَزُرْنِي أَزُرْكَ. When the answer cannot carry jazm — a nominal sentence, or a verb negated by مَا or لَنْ — the fāʾ must introduce it, and in a nominal answer إِذَا of surprise may replace the fāʾ (وَإِنْ تُصِبْهُمْ سَيِّئَةٌ … إِذَا هُمْ يَقْنَطُونَ).",
         "Where is the hidden إِنْ? After a command, prohibition, question, wish or offer, when cause is meant: أَسْلِمْ تَدْخُلِ الْجَنَّةَ — «become Muslim [and if you do] you enter». These are the same five that let the fāʾ govern naṣb; here, without the fāʾ, the verb is in jazm instead.",
         "Why does لَا تَكْفُرْ تَدْخُلِ النَّارَ fail? Because the supplied إِنْ carries the negation with it — «if you do not disbelieve you enter the Fire» — which is false. Al-Kisāʾī allows it on the strength of what usage means, and the notebook records both.",
         "What is the AMR, and is its ending built or declined? A form that asks the addressee for the act, made by dropping the muḍāriʿ prefix. The Basrans build it on the pause (its sukūn is bināʾ, like the māḍī's); the Kufans decline it, in jazm by a supplied lām — which is why the IrabSign reads an imperative's sukūn by its OPENING vowel and never calls it jazm."],
  "tr": ["Muzâriyi CEZM eden nedir? Beş şey: لَمْ, لَمَّا, emir lâmı, nehiy lâ'sı ve «mücâzât kelimesi» — şart edatları, başta إِنْ.",
         "لَمْ ile لَمَّا nasıl ayrılır? İkisi de nefy eder, ikisi de fiilin zamanını mâzîye çevirir. لَمَّا istiğrak ekler — «şu âna kadar değil» — bu yüzden daha hususîdir: نَدِمَ آدَمُ وَلَمْ يَنْفَعْهُ النَّدَمُ sonraki faydaya yer bırakır; نَدِمَ الشَّيْطَانُ وَلَمَّا يَنْفَعْهُ النَّدَمُ kapatır. İki sonuç: لَمَّا'dan sonraki fiil karîne ile düşebilir (قَارَبْتُ الْمَدِينَةَ وَلَمَّا), لَمْ'den sonra asla; إِنْ, لَمْ'in başına gelebilir, لَمَّا'nın asla.",
         "Emir lâmı? Kesre alır (لِيَنْصُرْ) ve وَ, فَ, ثُمَّ'den sonra sâkin olur (وَلْتَأْتِ، فَلْيُصَلُّوا). Nehiy lâ'sı fiilin TERKİNİ ister (لَا تَنْصُرْ) — aynı cezm, zıt istek.",
         "Şart nasıl çalışır? Edat iki fiilin üzerine girer ve birinciyi ikincinin sebebi yapar — şart ve cezâ, ikisi de meczûm: إِنْ تَزُرْنِي أَزُرْكَ. Cezâ cezm taşıyamadığında — isim cümlesi ya da مَا veya لَنْ ile menfî fiil — fâ onu getirmelidir; isim cümlesi cezâda mufâcee izâsı fânın yerini alabilir (وَإِنْ تُصِبْهُمْ سَيِّئَةٌ … إِذَا هُمْ يَقْنَطُونَ).",
         "Gizli إِنْ nerededir? Sebep kastedildiğinde emir, nehiy, soru, dilek ya da teklifin ardından: أَسْلِمْ تَدْخُلِ الْجَنَّةَ — «müslüman ol [olursan] cennete girersin». Bunlar fâya nasb ettiren aynı beştir; burada fâsız fiil cezmdedir.",
         "لَا تَكْفُرْ تَدْخُلِ النَّارَ neden bozuktur? Çünkü takdîr edilen إِنْ nefyi yanında taşır — «inkâr etmezsen cehenneme girersin» — ki yanlıştır. Kisâî örfî mânâya dayanarak izin verir; defter ikisini de kaydeder.",
         "EMİR nedir, sonu mebnî mi mu'reb mi? Muhâtabdan fiili isteyen, muzâri ön eki düşürülerek yapılan sîga. Basralılar onu vakf üzere binâ eder (sükûnu mâzîninki gibi binâdır); Kûfeliler mukadder bir lâm ile meczûm sayıp i'râb eder — IrabSign'ın emrin sükûnunu AÇILIŞ harekesinden okuyup asla cezm dememesinin sebebi budur."]},
 "plain": {
  "en": "Five things make a present-future verb end in sukūn: لَمْ and لَمَّا («did not», «not yet»), the lām that commands, the لَا that forbids, and «if». An «if» takes two verbs, cause and consequence; a request can hide its own «if» (become Muslim, you enter). The imperative's sukūn is not this jazm but its built form.",
  "tr": "Beş şey şimdiki-gelecek fiili sükûnla bitirir: لَمْ ve لَمَّا («-medi», «henüz -medi»), emreden lâm, yasaklayan لَا ve «eğer». Bir «eğer» cümlesi sebep ve sonuç olarak iki fiil alır; bir istek kendi «eğer»ini gizleyebilir (müslüman ol, cennete girersin). Emrin sükûnu bu cezm değil, kendi binâsıdır."},
 "explanation": {
  "en": "The chapter is the mirror of the previous one: where naṣb had four open governors and six seats for a hidden أَنْ, jazm has five open governors and five seats for a hidden إِنْ, and the five seats are the same five requests. The notebook's exposition of لَمْ and لَمَّا is kept whole because it is the kind of distinction examiners ask: both particles negate and both push the verb into the past, but لَمَّا adds that the negation runs up to the present, and from that one difference follow the two rules of usage — the verb after لَمَّا can be left unsaid when the hearer can supply it, and a conditional particle cannot sit on لَمَّا because a span that reaches the present cannot be made hypothetical. The lām of command and the لَا of prohibition are the two faces of request, and the lām's sukūn after a conjunction is recorded with its Qurʾānic instances. The word of requital is the Kafiya's name for the conditional, defined by what it does — it makes two verbs cause and effect — and the chapter keeps the three refinements the matn attaches: the fāʾ where the answer cannot show jazm, إِذَا of surprise as the fāʾ's substitute in a nominal answer, and the hidden إِنْ after the five requests, with the Kisāʾī dispute over the prohibition case, where the hidden particle would carry the negation into the condition and reverse the sense. The amr closes the verb's three tenses, defined in the notebook's own Arabic by the dropping of the prefix, and its ending is given both ways — built for the Basrans, declined for the Kufans — because the app's own rule that an imperative's sukūn is bināʾ is the Basran one and should be known as a choice.",
  "tr": "Bâb öncekinin aynasıdır: nasbın dört açık âmili ve gizli أَنْ için altı yeri varken cezmin beş açık âmili ve gizli إِنْ için beş yeri vardır ve bu beş yer aynı beş taleptir. Defterin لَمْ ve لَمَّا açıklaması bütünüyle tutulmuştur, çünkü sınavlarda sorulan türden bir ayrımdır: iki edat da nefy eder, ikisi de fiili mâzîye iter; ama لَمَّا nefyin şimdiye kadar sürdüğünü ekler ve bu tek farktan iki kullanım kuralı çıkar — لَمَّا'dan sonraki fiil dinleyen tamamlayabildiğinde söylenmeyebilir; şart edatı لَمَّا'ya binemez, çünkü şimdiye uzanan bir süre farazî kılınamaz. Emir lâmı ile nehiy lâ'sı talebin iki yüzüdür ve lâmın atıf harfinden sonraki sükûnu Kur'ânî örnekleriyle kaydedilir. Mücâzât kelimesi Kâfiye'nin şarta verdiği addır, yaptığı şeyle tarif edilir — iki fiili sebep ve sonuç yapar — ve bâb metnin eklediği üç inceliği tutar: cezânın cezm gösteremediği yerde fâ, isim cümlesi cezâda fânın yerini tutan mufâcee izâsı ve beş talepten sonra gizli إِنْ; nehiy hâlindeki Kisâî ihtilâfıyla birlikte, ki orada gizli edat nefyi şarta taşıyıp mânâyı tersine çevirir. Emir fiilin üç zamanını kapatır; defterin kendi Arapçasıyla ön ekin düşürülmesiyle tarif edilir ve sonu iki türlü verilir — Basralılar için mebnî, Kûfeliler için mu'reb — çünkü uygulamanın emrin sükûnunu binâ sayan kendi kuralı Basra görüşüdür ve bir tercih olarak bilinmelidir."},
 "examples": [
  {"ar": "يُجْزَمُ بِلَمْ وَلَمَّا وَلَامِ الْأَمْرِ وَلَا فِي النَّهْيِ وَكَلِمَةِ الْمُجَازَاةِ", "en": "The five jāzims.", "tr": "Beş cezm edici.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "نَدِمَ آدَمُ وَلَمْ يَنْفَعْهُ النَّدَمُ — نَدِمَ الشَّيْطَانُ وَلَمَّا يَنْفَعْهُ النَّدَمُ", "en": "لَمْ against لَمَّا.", "tr": "لَمْ ile لَمَّا.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "قَارَبْتُ الْمَدِينَةَ وَلَمَّا — إِنْ لَمْ يَضْرِبْ", "en": "Dropping after لَمَّا; إِنْ on لَمْ.", "tr": "لَمَّا'dan sonra hazf; لَمْ üzerine إِنْ.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "لِيَنْصُرْ — وَلْتَأْتِ طَائِفَةٌ أُخْرَى — لَا تَنْصُرْ", "en": "The lām of command and the لَا of prohibition.", "tr": "Emir lâmı ve nehiy lâ'sı.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "إِنْ تَزُرْنِي أَزُرْكَ", "en": "Condition and answer.", "tr": "Şart ve cezâ.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَإِنْ تُصِبْهُمْ سَيِّئَةٌ بِمَا قَدَّمَتْ أَيْدِيهِمْ إِذَا هُمْ يَقْنَطُونَ", "en": "إِذَا of surprise in the answer.", "tr": "Cezâda mufâcee izâsı.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "أَسْلِمْ تَدْخُلِ الْجَنَّةَ", "en": "The hidden إِنْ after a command.", "tr": "Emirden sonra gizli إِنْ.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "الْأَمْرُ: صِيغَةٌ يُطْلَبُ بِهَا الْفِعْلُ مِنَ الْفَاعِلِ الْمُخَاطَبِ بِحَذْفِ حَرْفِ الْمُضَارَعَةِ", "en": "The amr.", "tr": "Emir.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«إِنْ لَمَّا يَضْرِبْ»",
   "right": "«إِنْ لَمْ يَضْرِبْ — şart edatı لَمْ'in başına gelir, لَمَّا'nın değil»",
   "why": {"en": "A negation that runs up to the present cannot be made a hypothesis.", "tr": "Şimdiye uzanan nefy faraziye kılınamaz."}},
  {"wrong": "«وَلِتَأْتِ طَائِفَةٌ»",
   "right": "«وَلْتَأْتِ طَائِفَةٌ — vâvdan sonra emir lâmı sâkin kılınır»",
   "why": {"en": "The kasra is the lām's own; after و، ف، ثُمَّ it drops for lightness.", "tr": "Kesre lâmın kendi harekesidir; و، ف، ثُمَّ'den sonra hafiflik için düşer."}},
  {"wrong": "«إِنْ تَزُرْنِي مَا أَزُورُكَ»",
   "right": "«إِنْ تَزُرْنِي فَمَا أَزُورُكَ — مَا ile menfî cezâya fâ lâzımdır»",
   "why": {"en": "An answer that cannot show jazm must be introduced by the fāʾ.", "tr": "Cezm gösteremeyen cezâ fâ ile getirilmelidir."}},
  {"wrong": "«لَا تَكْفُرْ تَدْخُلِ النَّارَ»",
   "right": "«لَا تَكْفُرْ تَدْخُلِ الْجَنَّةَ — gizli إِنْ nefyi de taşır: inkâr etmezsen cennete girersin»",
   "why": {"en": "The majority reject the Fire version because the supplied condition would read «if you do not disbelieve»; al-Kisāʾī allows it by usage.", "tr": "Cumhûr cehennem hâlini reddeder, çünkü takdîr edilen şart «inkâr etmezsen» olur; Kisâî örfe göre izin verir."}},
  {"wrong": "«اُنْصُرْ — cezm ile sükûn»",
   "right": "«اُنْصُرْ — vakf üzere mebnî (Basra); Kûfe'ye göre mukadder lâm ile meczûm»",
   "why": {"en": "No jāzim is present; the app follows the Basran reading and names the sukūn a bināʾ.", "tr": "Cezm edici yoktur; uygulama Basra okuyuşunu izler ve sükûna binâ der."}}],
 "relatedNotes": [NJ, SH, JT, "la-nahiya", "in-shartiyya", "al-fa-fi-jawab-al-shart", "nawasib-al-mudari-fil-kafiya", "al-fil-wal-madi-wal-mudari-fil-kafiya"]}

ADD_EN = (" Chapter 22 (notebook lines ~302-306): the list of jāzims, the word of requital, the fāʾ and إِذَا in the answer, and the hidden إِنْ after the five requests restored from the received matn and marked (s1, s6-s8); the amr defined in the notebook's own Arabic (s10); "
          "لَمْ against لَمَّا with the notebook's examples and the two usage rules, the lām of command and لَا of prohibition, the Kisāʾī dispute and the Basran–Kufan views of the amr's ending as commentary (s2-s5, s9, s11).")
ADD_TR = (" Yirmi ikinci bâb (defter satırları ~302-306): cezm edicilerin listesi, mücâzât kelimesi, cezâda fâ ve إِذَا, beş talepten sonra gizli إِنْ alınan metinden geri yazılmış ve işaretlenmiştir (s1, s6-s8); emir defterin kendi Arapçasıyla tarif edilir (s10); "
          "defterin örnekleri ve iki kullanım kuralıyla لَمْ ile لَمَّا, emir lâmı ve nehiy lâ'sı, Kisâî ihtilâfı ve emrin sonu hakkında Basra–Kûfe görüşleri şerh olarak (s2-s5, s9, s11).")
write_out(22, S, TITLE, ADD_EN, ADD_TR, "302-306", GLOSS_ADD, notes=(NOTE,),
          related=((NJ, [K]), (SH, [K]), (JT, [K])))
report(22, S, GLOSS_ADD, (NOTE,))
