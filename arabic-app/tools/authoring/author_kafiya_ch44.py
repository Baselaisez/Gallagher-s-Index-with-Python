# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 44: كَلَّا the letter of rebuke (and in the sense of حَقًّا, 96:6); the quiescent tāʾ of femininity on the māḍī when the
musnad ilayh is feminine (ضَرَبَتْ هِنْدٌ), optional for a non-real feminine apparent noun (طَلَعَ / طَلَعَتِ الشَّمْسُ), the dual/plural sign on
the governor weak; the tanwīn defined (a quiescent nūn following the last vowel, not for emphasis) and its five kinds — tamakkun,
tankīr, ʿiwaḍ (يَوْمَئِذٍ), muqābala (مُسْلِمَاتٌ), tarannum; and the tanwīn dropped from a proper name described by ابْن (زَيْدُ بْنُ عَمْرٍو).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~348-353 of the transcription.

  COMMENTARY (the notebook): s1-s9 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch44.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "kalla-wa-ta-al-tanith-wal-tanwin-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "كَلَّا وَتَاءُ التَّأْنِيثِ وَالتَّنْوِينُ", "en": "Kallā, the tāʾ of femininity, and the five tanwīns", "tr": "Kellâ, te'nîs tâ'sı ve beş tenvin"}
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

AT = "atf-nasaq"
TN = "ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh"
TT = "al-fail-al-muzhar-wa-tanith-amilih"
def KALLA(tags=(), ar="حَرْفُ رَدْعٍ وَزَجْرٍ.", en="«kallā — no!».", tr="«kellâ — hayır!».", punct=None): return cited("كَلَّا", "kalla", "part", [K] + list(tags), ar, en, tr, punct=punct)
def FAQULTA(): return W("فَقُلْتَ", "qala", "verb", ["fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ، وَقُلْتَ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and you say».", "«ve sen dersen».", punct=":", segments=[seg("فَ", "fa", "conj"), seg("قُلْ", "qala", "verb"), prTa()])
def FAMANAHU(): return W("فَمَعْنَاهُ", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ، وَمَعْنَى مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its meaning is».", "«mânâsı şudur».", punct=":", segments=[seg("فَ", "fa", "conj"), seg("مَعْنَا", "mana", "noun"), pr3ms()])
def IDHA_QILA(): return [W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«so when».", "«... zaman».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]), W("قِيلَ", "qala", "verb", ["idha-shartiyya", "naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«it is said».", "«denildiği».", punct=":")]
def TANWIN(full, tags, ar, en, tr, punct=None): return W(full, "tanwin", "noun", tags + [TN, K], ar, en, tr, punct=punct)
def MUSNAD_ILAYH(tags, ar): return [W("الْمُسْنَدُ", "musnad", "noun", tags + ["ism-maful", "form-iv-verbs"], ar, "«the subject».", "«müsnedün ileyh»."), W("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — مُتَعَلِّقٌ بِالْمُسْنَدِ.", "«(to it)».", "«(ona)».", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()])]
def HIND(punct=None): return cited("هِنْدٌ", "hind", "propn", ["fail", TT], "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ حَقِيقِيٌّ.", "«Hind».", "«Hind».", punct=punct)
def SHAMS(punct=None, ar="فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ غَيْرُ حَقِيقِيٍّ."): return cited("الشَّمْسُ", "shams", "noun", ["fail", TT], ar, "«the sun».", "«güneş».", punct=punct)

S.append({"id": "s1", "translation": {
 "en": "And the letter of rebuke is كَلَّا: when it is said «so-and-so hates you» and you say كَلَّا, its meaning is «no — he does not hate me»." + C_EN,
 "tr": "Red harfi كَلَّا'dır: «filân sana buğzediyor» denildiğinde كَلَّا dersen mânâsı «hayır, o bana buğzetmez» demektir." + C_TR},
 "tokens": [
  atf_wa("وَحَرْفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness"], "حَرْفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the letter of».", "«ve ... harfi».", "حَرْفُ"),
  W("الرَّدْعِ", "rad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rebuke».", "«red»."),
  KALLA(tags=("mubtada-khabar",), ar="لَفْظٌ مَحْكِيٌّ — خَبَرٌ.", en="«is kallā».", tr="«kellâ'dır».", punct="؛"),
  *IDHA_QILA(),
  cited("فُلَانٌ", "fulan", "noun", ["mubtada-khabar", "naib-al-fail"], "مُبْتَدَأٌ مَرْفُوعٌ — الْجُمْلَةُ الْمَقُولَةُ نَائِبُ فَاعِلٍ.", "«so-and-so».", "«filân»."),
  cited("يُبْغِضُكَ", "abghada", "verb", ["mubtada-khabar", "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْكَافُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرٌ.", "«hates you».", "«sana buğzediyor».", punct="،", segments=[seg("يُبْغِضُ", "abghada", "verb"), pr2ms()]),
  FAQULTA(),
  KALLA(tags=("maful-bihi",), ar="حَرْفُ رَدْعٍ — الْمَقُولُ.", punct="،"),
  FAMANAHU(),
  cited("لَا", "la", "part", ["mubtada-khabar"], "حَرْفُ جَوَابٍ — خَبَرٌ، مَحْكِيٌّ.", "«no».", "«hayır».", punct="،"),
  cited("هُوَ", "huwa", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«he».", "«o»."),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mez»."),
  cited("يُبْغِضُنِي", "abghada", "verb", ["mubtada-khabar", "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرٌ.", "«does hate me».", "«bana buğzet-».", punct=".", segments=[seg("يُبْغِضُ", "abghada", "verb"), pr1s()]),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And كَلَّا after a command is to refuse compliance: when it is said «come!» and you say كَلَّا, its meaning is «no — I am not coming»." + C_EN,
 "tr": "Emirden sonra gelen كَلَّا icabeti reddetmek içindir: «gel!» denildiğinde كَلَّا dersen mânâsı «hayır, gelmiyorum» demektir." + C_TR},
 "tokens": [
  cited_wa("وَكَلَّا", "kalla", "part", ["mubtada-khabar", K], "كَلَّا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and kallā».", "«ve kellâ».", "كَلَّا"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonra»."),
  W("الْأَمْرِ", "amr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a command».", "«emir»."),
  li_("لِرَدِّ", "radd", "noun", ["mubtada-khabar", "idafa-definiteness"], "رَدِّ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is to refuse».", "«reddetmek içindir».", "رَدِّ"),
  W("الْإِجَابَةِ", "ijaba", "noun", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«compliance».", "«icabeti».", punct="؛"),
  *IDHA_QILA(),
  cited("تَعَالَ", "taala-come", "part", ["naib-al-fail"], "فِعْلُ أَمْرٍ لَا مَاضِيَ لَهُ فِي الِاسْتِعْمَالِ — الْمَقُولُ نَائِبُ فَاعِلٍ.", "«come!».", "«gel!».", punct="،"),
  FAQULTA(),
  KALLA(tags=("maful-bihi",), ar="حَرْفُ رَدْعٍ — الْمَقُولُ.", punct="،"),
  FAMANAHU(),
  cited("لَا", "la", "part", ["mubtada-khabar"], "حَرْفُ جَوَابٍ — خَبَرٌ.", "«no».", "«hayır».", punct="،"),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mi-»."),
  cited("آتِي", "ata", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«am I coming».", "«gel-yorum».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And كَلَّا may be in the sense of حَقًّا, «truly» — as «كَلَّا إِنَّ الْإِنْسَانَ لَيَطْغَى»." + C_EN,
 "tr": "كَلَّا bazen حَقًّا «gerçekten» mânâsına gelir — «كَلَّا إِنَّ الْإِنْسَانَ لَيَطْغَى» gibi." + C_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and may».", "«ve bazen».", "قَدْ"),
  W("تَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«be».", "«olur»."),
  KALLA(tags=("kana-wa-akhawatuha",), ar="اسْمُ تَكُونُ — اللَّفْظُ مَحْكِيٌّ.", en="«kallā».", tr="«kellâ»."),
  bi_("بِمَعْنَى", "mana", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "مَعْنَى مَجْرُورٌ مُضَافٌ — خَبَرُ تَكُونُ.", "«in the sense of».", "«... mânâsına».", "مَعْنَى"),
  cited("حَقًّا", "haqqan", "adv", ["idafa-definiteness", "maful-mutlaq"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ: مَفْعُولٌ مُطْلَقٌ فِي أَصْلِهِ.", "«truly».", "«hakkan».", punct="،"),
  nahwu(),
  KALLA(tags=("insha-wa-tamanni",), ar="حَرْفُ تَحْقِيقٍ بِمَعْنَى حَقًّا.", en="«truly».", tr="«gerçekten»."),
  cited("إِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«muhakkak»."),
  cited("الْإِنْسَانَ", "insan", "noun", ["inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«man».", "«insan»."),
  cited("لَيَطْغَى", "tagha", "verb", ["inna-wa-akhawatuha", "fail", "naqis-verbs"], "اللَّامُ الْمُزَحْلَقَةُ، وَيَطْغَى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — الْجُمْلَةُ خَبَرُ إِنَّ.", "«transgresses».", "«azar».", punct=".", segments=[seg("لَ", "lam-ibtida", "part"), seg("يَطْغَى", "tagha", "verb")]),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the quiescent tāʾ of femininity attaches to the end of the past verb when its subject is feminine — as ضَرَبَتْ هِنْدٌ and ضُرِبَتْ هِنْدٌ: the tāʾ at the end of the verb tells that Hind, the subject, is feminine." + C_EN,
 "tr": "Sâkin te'nîs tâ'sı, müsnedün ileyh müennes olduğunda mâzî fiilin sonuna lâhik olur — ضَرَبَتْ هِنْدٌ ve ضُرِبَتْ هِنْدٌ gibi: fiilin sonundaki tâ, müsnedün ileyh olan Hind'in müennes olduğunu bildirir." + C_TR},
 "tokens": [
  atf_wa("وَتَاءُ", "ta-tanith", "part", ["mubtada-khabar", "idafa-definiteness", TT], "تَاءُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the tāʾ of».", "«ve ... tâ'sı».", "تَاءُ"),
  W("التَّأْنِيثِ", "tanith", "noun", ["idafa-definiteness", "al-muannath-wa-alamatuh"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«femininity».", "«te'nîs»."),
  W("السَّاكِنَةُ", "sakin", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَرْفُوعَةٌ.", "«quiescent».", "«sâkin»."),
  W("تَلْحَقُ", "lahiqa", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ — الْجُمْلَةُ خَبَرٌ.", "«attaches to».", "«lâhik olur»."),
  W("آخِرَ", "akhir", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the end of».", "«sonuna»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb».", "«fiilin»."),
  W("الْمَاضِي", "madi", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«past».", "«mâzî»."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«... olduğunda»."),
  W("كَانَ", "kana", "verb", ["idha-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«olduğunda»."),
  *MUSNAD_ILAYH(["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ — الْفَاعِلُ أَوْ نَائِبُهُ."),
  W("مُؤَنَّثًا", "muannath", "noun", ["kana-wa-akhawatuha", "ism-maful", "form-ii-verbs"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«feminine».", "«müennes».", punct="،"),
  nahwu(),
  cited("ضَرَبَتْ", "daraba", "verb", ["fail", TT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ لَا مَحَلَّ لَهَا.", "«struck».", "«dövdü».", segments=[seg("ضَرَبَ", "daraba", "verb"), seg("تْ", "ta-tanith", "part")]),
  HIND(punct="،"),
  cited_wa("وَضُرِبَتْ", "daraba", "verb", ["naib-al-fail", TT], "ضُرِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and was struck».", "«ve dövüldü».", "ضُرِبَتْ", extra_segs=[seg("ضُرِبَ", "daraba", "verb"), seg("تْ", "ta-tanith", "part")]),
  cited("هِنْدٌ", "hind", "propn", ["naib-al-fail", TT], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«Hind».", "«Hind».", punct=":"),
  W("فَالتَّاءُ", "ta-tanith", "part", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالتَّاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the tāʾ».", "«tâ».", segments=[seg("فَ", "fa", "conj"), seg("التَّاءُ", "ta-tanith", "part")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-deki»."),
  W("آخِرِ", "akhir", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the end of».", "«sonundaki»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb».", "«fiilin»."),
  W("تُفِيدُ", "afada", "verb", ["mubtada-khabar", "fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ — الْجُمْلَةُ خَبَرٌ.", "«tells».", "«bildirir»."),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ مَفْعُولُ تُفِيدُ.", "«that».", "«-ini»."),
  cited("هِنْدًا", "hind", "propn", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ — صُرِفَ لِسُكُونِ وَسَطِهِ.", "«Hind».", "«Hind'in»."),
  *MUSNAD_ILAYH(["badal"], "بَدَلٌ مِنْ هِنْدًا مَنْصُوبٌ."),
  W("مُؤَنَّثٌ", "muannath", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is feminine».", "«müennes olduğunu».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And if the subject is an apparent noun that is feminine not by nature, you have the choice — as طَلَعَ الشَّمْسُ and طَلَعَتِ الشَّمْسُ; and attaching the sign of the dual or the plural to the governor, when the apparent noun is dual or plural, is weak." + C_EN,
 "tr": "Müsnedün ileyh, hakikî olmayan müennes bir ism-i zâhir olursa muhayyersin — طَلَعَ الشَّمْسُ ve طَلَعَتِ الشَّمْسُ gibi; ism-i zâhir tesniye ya da cemi iken âmile tesniye ya da cemi alâmeti getirmek ise zayıftır." + C_TR},
 "tokens": [
  W("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«... olursa».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«is».", "«olursa»."),
  *MUSNAD_ILAYH(["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ."),
  W("اسْمًا", "ism", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a noun».", "«bir isim»."),
  W("ظَاهِرًا", "zahir", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَنْصُوبَةٌ.", "«apparent».", "«zâhir»."),
  W("مُؤَنَّثًا", "muannath", "noun", ["naat-sifa"], "صِفَةٌ ثَانِيَةٌ مَنْصُوبَةٌ.", "«feminine».", "«müennes»."),
  W("غَيْرَ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ ثَالِثَةٌ مَنْصُوبَةٌ، وَهُوَ مُضَافٌ.", "«not».", "«... olmayan»."),
  W("حَقِيقِيٍّ", "haqiqi", "noun", ["idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«by nature».", "«hakikî»."),
  W("فَأَنْتَ", "anta", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَأَنْتَ مُبْتَدَأٌ.", "«you».", "«sen».", segments=[seg("فَ", "fa", "conj"), seg("أَنْتَ", "anta", "pron")]),
  W("مُخَيَّرٌ", "mukhayyar", "noun", ["mubtada-khabar", "ism-maful", "form-ii-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«have the choice».", "«muhayyersin».", punct="،"),
  nahwu(),
  cited("طَلَعَ", "talaa", "verb", ["fail", TT], "فِعْلٌ مَاضٍ بِلَا تَاءٍ — جَائِزٌ.", "«rose».", "«doğdu»."),
  SHAMS(punct="،"),
  cited_wa("وَطَلَعَتِ", "talaa", "verb", ["fail", TT], "طَلَعَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — جَائِزٌ أَيْضًا.", "«and rose».", "«ve doğdu».", "طَلَعَتِ", extra_segs=[seg("طَلَعَ", "talaa", "verb"), seg("تِ", "ta-tanith", "part")]),
  SHAMS(punct="؛"),
  atf_wa("وَإِلْحَاقُ", "ilhaq", "noun", ["mubtada-khabar", "idafa-definiteness", "form-iv-verbs"], "إِلْحَاقُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and attaching».", "«ve ... getirmek».", "إِلْحَاقُ"),
  W("عَلَامَةِ", "alama", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the sign of».", "«alâmetini»."),
  W("التَّثْنِيَةِ", "tathniya", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dual».", "«tesniye»."),
  atf_wa("وَالْجَمْعِ", "jam", "noun", [AT, "al-jumu-wa-tanith-amiliha"], "الْجَمْعِ مَعْطُوفٌ مَجْرُورٌ.", "«or the plural».", "«ya da cemi».", "الْجَمْعِ"),
  bi_("بِالْعَامِلِ", "amil", "noun", ["al-amil-wa-aqsamuh"], "الْعَامِلِ مَجْرُورٌ.", "«to the governor».", "«âmile».", "الْعَامِلِ", segs=[seg("بِ", "bi", "prep"), seg("الْعَامِلِ", "amil", "noun")]),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«... iken»."),
  W("كَانَ", "kana", "verb", ["idha-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«iken»."),
  W("الِاسْمُ", "ism", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the noun».", "«isim»."),
  W("الظَّاهِرُ", "zahir", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«apparent».", "«zâhir»."),
  W("مُثَنًّى", "muthanna", "noun", ["kana-wa-akhawatuha", "ism-maful", "al-muthanna"], "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«dual».", "«tesniye»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَجْمُوعًا", "majmu", "noun", [AT, "ism-maful"], "مَعْطُوفٌ مَنْصُوبٌ.", "«plural».", "«cemi»."),
  W("ضَعِيفٌ", "daif", "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرُ إِلْحَاقُ مَرْفُوعٌ.", "«is weak».", "«zayıftır».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And the tanwīn is a quiescent nūn that follows the vowel of the last letter — not for the emphasis of a verb; and it is of five kinds." + C_EN,
 "tr": "Tenvin, fiili te'kid için olmayıp sonun harekesine tâbi olan sâkin bir nûndur; beş kısımdır." + C_TR},
 "tokens": [
  TANWIN("وَالتَّنْوِينُ", ["mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالتَّنْوِينُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the tanwīn».", "«tenvin».", punct=":"),
  W("نُونٌ", "nun-letter", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a nūn».", "«bir nûndur»."),
  W("سَاكِنَةٌ", "sakin", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَرْفُوعَةٌ.", "«quiescent».", "«sâkin»."),
  W("تَتْبَعُ", "tabia-follow", "verb", ["naat-sifa", "fail"], "فِعْلٌ مُضَارِعٌ — الْجُمْلَةُ صِفَةٌ ثَانِيَةٌ.", "«that follows».", "«tâbi olan»."),
  W("حَرَكَةَ", "haraka", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the vowel of».", "«harekesine»."),
  W("الْآخِرِ", "akhir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the last letter».", "«sonun»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«... olmayıp»."),
  li_("لِتَأْكِيدِ", "takid", "noun", ["idafa-definiteness", "lam-taleel"], "تَأْكِيدِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَرَجَتْ بِهِ نُونُ التَّوْكِيدِ الْخَفِيفَةُ.", "«for the emphasis of».", "«te'kid için».", "تَأْكِيدِ"),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«fiili».", punct="؛"),
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هُوَ"),
  W("خَمْسَةُ", "khamsa", "noun", ["mubtada-khabar", "idafa-definiteness", "asma-al-adad-fil-kafiya"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is five».", "«beş»."),
  W("أَقْسَامٍ", "qism", "noun", ["idafa-definiteness", "jam-taksir", "tamyiz"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَمْيِيزُ الْعَدَدِ.", "«kinds».", "«kısımdır».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "The tanwīn of tamakkun is that which shows the word to be fully declinable — as زَيْدٌ; and the tanwīn of tankīr is that which separates the definite from the indefinite — as رَجُلٌ." + C_EN,
 "tr": "Temekkün tenvini, kelimenin munsarif olduğuna delâlet eden tenvindir — زَيْدٌ gibi; tenkir tenvini, ma'rife ile nekirenin arasını ayıran tenvindir — رَجُلٌ gibi." + C_TR},
 "tokens": [
  TANWIN("تَنْوِينُ", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the tanwīn of».", "«... tenvini»."),
  W("التَّمَكُّنِ", "tamakkun", "noun", ["idafa-definiteness", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«tamakkun».", "«temekkün».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«is that which».", "«... -dir»."),
  W("يَدُلُّ", "dalla", "verb", ["ism-mawsul", "fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ — صِلَةٌ.", "«shows».", "«delâlet eden»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«(on)».", "«-e»."),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — الْمَصْدَرُ مَجْرُورٌ بِعَلَى.", "«that».", "«-duğuna»."),
  W("الْكَلِمَةَ", "kalima", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the word».", "«kelimenin»."),
  W("مُنْصَرِفَةٌ", "munsarif", "noun", ["inna-wa-akhawatuha", "ism-fail", "form-vii-verbs", TN], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is fully declinable».", "«munsarif olduğuna».", punct="،"),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", [TN, K], "عَلَمٌ مُنْصَرِفٌ — تَنْوِينُهُ لِلتَّمَكُّنِ.", "«Zayd».", "«Zeyd».", punct="؛"),
  TANWIN("وَتَنْوِينُ", ["mubtada-khabar", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَتَنْوِينُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the tanwīn of».", "«... tenvini»."),
  W("التَّنْكِيرِ", "tankir", "noun", ["idafa-definiteness", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«tankīr».", "«tenkir».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«is that which».", "«... -dir»."),
  W("يُفَرِّقُ", "farraqa", "verb", ["ism-mawsul", "fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ — صِلَةٌ.", "«separates».", "«ayıran»."),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasını»."),
  W("الْمَعْرِفَةِ", "marifa", "noun", ["idafa-definiteness", "al-marifa-wal-nakira-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the definite».", "«ma'rife»."),
  atf_wa("وَالنَّكِرَةِ", "nakira", "noun", [AT, "al-marifa-wal-nakira-fil-kafiya"], "النَّكِرَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the indefinite».", "«ile nekirenin».", "النَّكِرَةِ", punct="،"),
  nahwu(),
  cited("رَجُلٌ", "rajul", "noun", [TN, K], "نَكِرَةٌ — تَنْوِينُهُ لِلتَّنْكِيرِ.", "«a man».", "«bir adam».", punct="."),
 ]})

S.append({"id": "s8", "translation": {
 "en": "The tanwīn of ʿiwaḍ attaches to the end of the noun as a substitute for the muḍāf ilayh — as يَوْمَئِذٍ, whose origin is يَوْمَ إِذْ كَانَ كَذَا; the tanwīn of muqābala is the one in the feminine plural facing the nūn of the masculine plural — as مُسْلِمَاتٌ; and the tanwīn of tarannum is the one at the ends of hemistichs and verses." + C_EN,
 "tr": "İvaz tenvini, muzâfun ileyhten bedel olarak ismin sonuna gelen tenvindir — aslı يَوْمَ إِذْ كَانَ كَذَا olan يَوْمَئِذٍ gibi; mukabele tenvini, cemi müzekker nûnuna mukabil cemi müenneste bulunan tenvindir — مُسْلِمَاتٌ gibi; terennüm tenvini ise mısraların ve beyitlerin sonlarında bulunan tenvindir." + C_TR},
 "tokens": [
  TANWIN("وَتَنْوِينُ", ["mubtada-khabar", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَتَنْوِينُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«and the tanwīn of».", "«... tenvini»."),
  W("الْعِوَضِ", "iwad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ʿiwaḍ».", "«ivaz».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«is that which».", "«... -dir»."),
  W("يَلْحَقُ", "lahiqa", "verb", ["ism-mawsul", "fail"], "فِعْلٌ مُضَارِعٌ — صِلَةٌ.", "«attaches to».", "«gelen»."),
  W("آخِرَ", "akhir", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the end of».", "«sonuna»."),
  W("الِاسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the noun».", "«ismin»."),
  W("عِوَضًا", "iwad", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«as a substitute».", "«bedel olarak»."),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-ten»."),
  W("الْمُضَافِ", "mudaf", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ.", "«the muḍāf».", "«muzâfun»."),
  W("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«ilayh».", "«ileyh».", punct="،", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  nahwu(),
  cited("يَوْمَئِذٍ", "yawmaidhin", "noun", ["maful-fih", TN, K], "ظَرْفٌ مَنْصُوبٌ، وَإِذٍ مُضَافٌ إِلَيْهِ، وَتَنْوِينُهُ عِوَضٌ عَنِ الْجُمْلَةِ الْمُضَافِ إِلَيْهَا.", "«on that day».", "«o gün».", punct="،"),
  atf_wa("وَأَصْلُهُ", "asl", "noun", ["mubtada-khabar", "idafa-definiteness"], "أَصْلُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its origin is».", "«aslı».", "أَصْلُهُ", punct=":", extra_segs=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  cited("يَوْمَ", "yawm", "noun", ["mubtada-khabar", "maful-fih", "idafa-definiteness"], "الْجُمْلَةُ الْمَحْكِيَّةُ خَبَرٌ: يَوْمَ ظَرْفٌ مُضَافٌ.", "«the day».", "«gün»."),
  cited("إِذْ", "idh", "noun", ["idafa-definiteness", "maful-fih"], "ظَرْفٌ مُضَافٌ إِلَيْهِ مَبْنِيٌّ، وَهُوَ مُضَافٌ إِلَى الْجُمْلَةِ.", "«when».", "«-diğinde»."),
  cited("كَانَ", "kana", "verb", ["idafa-definiteness", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ — الْجُمْلَةُ مُضَافٌ إِلَيْهَا.", "«was».", "«olduğu»."),
  cited("كَذَا", "kadha", "pron", ["kana-wa-akhawatuha", "asma-al-ishara-wal-mawsulat"], "خَبَرُ كَانَ — كِنَايَةٌ عَنِ الشَّيْءِ.", "«such-and-such».", "«şöyle».", punct="؛"),
  TANWIN("وَتَنْوِينُ", ["mubtada-khabar", "idafa-definiteness"], "تَنْوِينُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«and the tanwīn of».", "«... tenvini»."),
  W("الْمُقَابَلَةِ", "muqabala", "noun", ["idafa-definiteness", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«muqābala».", "«mukabele».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«is the one».", "«... -dir»."),
  W("فِي", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«in».", "«-te»."),
  W("جَمْعِ", "jam", "noun", ["huruf-jarr", "idafa-definiteness", "jam-muannath-salim"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cemi»."),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müenneste»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«(in)».", "«-e»."),
  W("مُقَابَلَةِ", "muqabala", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«facing».", "«mukabil»."),
  W("نُونِ", "nun-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnuna»."),
  W("جَمْعِ", "jam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cemi»."),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine».", "«müzekker».", punct="،"),
  nahwu(),
  cited("مُسْلِمَاتٌ", "muslima", "noun", ["jam-muannath-salim", TN, K], "جَمْعُ مُؤَنَّثٍ سَالِمٌ — تَنْوِينُهُ لِلْمُقَابَلَةِ.", "«Muslim women».", "«Müslüman kadınlar».", punct="؛"),
  TANWIN("وَتَنْوِينُ", ["mubtada-khabar", "idafa-definiteness"], "تَنْوِينُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«and the tanwīn of».", "«... tenvini»."),
  W("التَّرَنُّمِ", "tarannum", "noun", ["idafa-definiteness", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«tarannum».", "«terennüm».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«is the one».", "«... -dir»."),
  W("فِي", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — صِلَةٌ.", "«at».", "«-da»."),
  W("أَوَاخِرِ", "akhir", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ، وَهُوَ مُضَافٌ.", "«the ends of».", "«sonlarında»."),
  W("الْمَصَارِيعِ", "misra", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«hemistichs».", "«mısraların»."),
  atf_wa("وَالْأَبْيَاتِ", "bayt", "noun", [AT, "jam-taksir"], "الْأَبْيَاتِ مَعْطُوفٌ مَجْرُورٌ.", "«and verses».", "«ve beyitlerin».", "الْأَبْيَاتِ", punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And the tanwīn is dropped obligatorily from a proper name described by ابْن annexed to another proper name — as جَاءَنِي زَيْدُ بْنُ عَمْرٍو; for ابْن is much used between two names, so for lightness its alif was dropped from the attribute and the tanwīn from the described." + C_EN,
 "tr": "Başka bir aleme muzâf ابْن ile vasıflanan alemden tenvin vücûben hazfedilir — جَاءَنِي زَيْدُ بْنُ عَمْرٍو gibi; zira ابْن iki alem arasında çok kullanıldığından hafiflik için sıfattan elif, mevsuftan tenvin hazfedilmiştir." + C_TR},
 "tokens": [
  atf_wa("وَيُحْذَفُ", "hadhafa", "verb", ["naib-al-fail"], "يُحْذَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is dropped».", "«ve hazfedilir».", "يُحْذَفُ"),
  TANWIN("التَّنْوِينُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the tanwīn».", "«tenvin»."),
  W("وُجُوبًا", "wujuban", "adv", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِعَامِلٍ مَحْذُوفٍ — أَوْ حَالٌ.", "«obligatorily».", "«vücûben»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الْعَلَمِ", "alam-name", "noun", ["huruf-jarr", "al-marifa-wal-nakira-fil-kafiya"], "مَجْرُورٌ.", "«a proper name».", "«alemden»."),
  W("الْمَوْصُوفِ", "mawsuf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«described».", "«vasıflanan»."),
  bi_("بِابْنٍ", "ibn", "noun", [], "ابْنٍ مَجْرُورٌ — اللَّفْظُ مَحْكِيٌّ.", "«by ibn».", "«ibn ile».", "ابْنٍ"),
  W("مُضَافٍ", "mudaf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ لِابْنٍ مَجْرُورَةٌ.", "«annexed».", "«muzâf»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("عَلَمٍ", "alam-name", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a proper name».", "«bir aleme»."),
  W("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "صِفَةٌ مَجْرُورَةٌ بِالْفَتْحَةِ — غَيْرُ مُنْصَرِفٍ.", "«another».", "«başka».", punct="،"),
  nahwu(),
  cited("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  cited("زَيْدُ", "zayd", "propn", ["fail", TN, K], "فَاعِلٌ مَرْفُوعٌ — حُذِفَ تَنْوِينُهُ لِوَصْفِهِ بِابْنٍ.", "«Zayd».", "«Zeyd»."),
  cited("بْنُ", "ibn", "noun", ["naat-sifa", "idafa-definiteness", K], "صِفَةٌ مَرْفُوعَةٌ — حُذِفَتْ أَلِفُهُ، وَهُوَ مُضَافٌ.", "«son of».", "«oğlu»."),
  cited("عَمْرٍو", "amr-name", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ʿAmr».", "«Amr».", punct="؛"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«zira».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  cited("ابْنًا", "ibn", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ — اللَّفْظُ مَحْكِيٌّ.", "«ibn».", "«ibn»."),
  W("كَثُرَ", "kathura", "verb", ["inna-wa-akhawatuha", "fail"], "فِعْلٌ مَاضٍ — الْجُمْلَةُ خَبَرُ أَنَّ.", "«is much».", "«çok»."),
  W("اسْتِعْمَالُهُ", "istimal", "noun", ["fail", "idafa-definiteness", "form-x-verbs"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its use».", "«kullanıldığından».", segments=[seg("اسْتِعْمَالُ", "istimal", "noun"), pr3ms()]),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasında»."),
  W("عَلَمَيْنِ", "alam-name", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two names».", "«iki alem».", punct="،"),
  W("فَحُذِفَتْ", "hadhafa", "verb", ["naib-al-fail"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَحُذِفَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«so was dropped».", "«hazfedilmiştir».", segments=[seg("فَ", "fa", "conj"), seg("حُذِفَ", "hadhafa", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("أَلِفُهُ", "alif-letter", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its alif».", "«elifi».", segments=[seg("أَلِفُ", "alif-letter", "noun"), pr3ms()]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-tan»."),
  W("الصِّفَةِ", "sifa", "noun", ["huruf-jarr", "naat-sifa"], "مَجْرُورٌ.", "«the attribute».", "«sıfattan»."),
  TANWIN("وَالتَّنْوِينُ", [AT, "naib-al-fail"], "الْوَاوُ عَاطِفَةٌ، وَالتَّنْوِينُ مَعْطُوفٌ عَلَى أَلِفُهُ.", "«and the tanwīn».", "«ve tenvin»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-tan»."),
  W("الْمَوْصُوفِ", "mawsuf", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«the described».", "«mevsuftan»."),
  li_("لِلتَّخْفِيفِ", "takhfif", "noun", ["lam-taleel", "form-ii-verbs"], "التَّخْفِيفِ مَجْرُورٌ — اللَّامُ لِلتَّعْلِيلِ.", "«for lightness».", "«hafiflik için».", "التَّخْفِيفِ", punct=".", segs=[seg("لِ", "li", "prep"), seg("لتَّخْفِيفِ", "takhfif", "noun")]),
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
 "rad": need("rad", "رَدْع", "ر د ع", "noun", "rebuke, checking — the sense of كَلَّا (masdar)", "red, men, zecr — كَلَّا'nın mânâsı (masdar)", 4),
 "abghada": need("abghada", "أَبْغَضَ", "ب غ ض", "verb", "to hate, to detest (Form IV)", "buğzetmek, nefret etmek (ifʿâl)", 3),
 "ijaba": need("ijaba", "إِجَابَة", "ج و ب", "noun", "answering, compliance (masdar of أَجَابَ)", "icabet, cevap verme (ecâbe'nin masdarı)", 3),
 "haqqan": need("haqqan", "حَقًّا", "ح ق ق", "adv", "truly, in truth (an accusative of حَقّ used as an adverb)", "hakkan, gerçekten (حَقّ'ın zarf olarak mansubu)", 2),
 "taala-come": need("taala-come", "تَعَالَ", "ع ل و", "part", "come! — a fixed imperative used only in this form", "gel! — yalnız bu şekilde kullanılan donmuş bir emir", 2),
 "tarannum": need("tarannum", "تَرَنُّم", "ر ن م", "noun", "chanting, singing — the tanwīn at the end of a verse (masdar, Form V)", "terennüm, nağme — beyit sonundaki tenvin (tefeʿʿul masdarı)", 4),
 "ilhaq": need("ilhaq", "إِلْحَاق", "ل ح ق", "noun", "attaching, appending (masdar of أَلْحَقَ)", "ilhak, ekleme (elhaka'nın masdarı)", 4),
 "wujuban": need("wujuban", "وُجُوبًا", "و ج ب", "adv", "obligatorily, of necessity (an accusative of وُجُوب used as an adverb)", "vücûben, zorunlu olarak (وُجُوب'un zarf olarak mansubu)", 4),
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
put_morph(mo, "abghada", _nfc(_sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْغَض", "بْغِض", "أَبْغِض", "إِبْغَاض", "مُبْغِض", "مُبْغَض", "أُبْغِضَ", "يُبْغَضُ", "أَبْغَضَهُ: كَرِهَهُ أَشَدَّ الْكَرَاهَةِ — بَابُ الْإِفْعَالِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "كَلَّا وَتَاءُ التَّأْنِيثِ وَالتَّنْوِينُ فِي الْكَافِيَةِ", "en": "Kallā, the tāʾ of femininity and the tanwīn in the Kafiya: rebuke and «truly», the quiescent tāʾ and when it is optional, the five tanwīns, and the tanwīn dropped before ibn", "tr": "Kâfiye'de kellâ, te'nîs tâ'sı ve tenvin: red ve «gerçekten», sâkin tâ ve ne zaman ihtiyarî olduğu, beş tenvin ve ibn'den önce düşen tenvin"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — حرف الردع كلا؛ تاء التأنيث الساكنة؛ التنوين نون ساكنة تتبع حركة الآخر لا لتأكيد الفعل، وهو خمسة", "ضياء صونغور اوغلى — دفتر الكافية: كلا بعد الأمر لرد الإجابة وبمعنى حقا؛ طلع الشمس وطلعت الشمس؛ تنوين التمكن والتنكير والعوض والمقابلة والترنم؛ زيد بن عمرو"],
 "question": {
  "en": ["What does كَلَّا answer? A claim or a command, with a flat «no»: to «so-and-so hates you» it means «he does not»; to «come!» it means «I am not coming». In the Qur'an it can instead mean «truly» (كَلَّا إِنَّ الْإِنْسَانَ لَيَطْغَى), and the reader decides by what precedes it.",
         "When must the past verb take the quiescent tāʾ? When its subject is feminine by nature (ضَرَبَتْ هِنْدٌ, ضُرِبَتْ هِنْدٌ). When the subject is an apparent noun feminine only by convention (الشَّمْس), either form is allowed — طَلَعَ الشَّمْسُ or طَلَعَتِ الشَّمْسُ. The split is lexical: whether a noun is feminine by nature is a fact of the glossary, not of the surface.",
         "May the verb take a dual or plural sign to match a following apparent noun (أَكَلُونِي الْبَرَاغِيثُ)? The notebook calls it weak: the apparent noun is the doer and the verb stays singular.",
         "What is the tanwīn, and what is it NOT? A quiescent nūn pronounced after the last vowel and not written as a letter; it is not the light nūn of emphasis (اِضْرِبَنْ), which the definition excludes by its last clause.",
         "What are the five kinds? Tamakkun (declinability: زَيْدٌ), tankīr (indefiniteness: رَجُلٌ), ʿiwaḍ (standing in for a dropped muḍāf ilayh: يَوْمَئِذٍ, originally يَوْمَ إِذْ كَانَ كَذَا), muqābala (the feminine sound plural's counterpart to the masculine plural's nūn: مُسْلِمَاتٌ) and tarannum (the chanting tanwīn at the end of a verse). The sign engine reads the tanwīn as the mark of the fully declinable noun; the ʿiwaḍ tanwīn is the one that survives on مَعَانٍ in the mamnūʿ chapter.",
         "Why زَيْدُ بْنُ عَمْرٍو with no tanwīn and no alif? Because ابْن between two proper names is so common that the language lightened it twice: the described name drops its tanwīn and the attribute drops its alif. The iʿrāb lines here apply this rule where a name is followed by ibn."],
  "tr": ["كَلَّا neye cevap verir? Bir iddiaya ya da emre düz bir «hayır» ile: «filân sana buğzediyor»a «etmez» demektir; «gel!»e «gelmiyorum» demektir. Kur'ân'da ise «gerçekten» demek olabilir (كَلَّا إِنَّ الْإِنْسَانَ لَيَطْغَى) ve okuyucu öncesine bakarak karar verir.",
         "Mâzî fiil sâkin tâ'yı ne zaman almalıdır? Faili hakikî müennes olunca (ضَرَبَتْ هِنْدٌ, ضُرِبَتْ هِنْدٌ). Fail yalnız itibarî olarak müennes bir ism-i zâhir olunca (الشَّمْس) iki şekil de câizdir — طَلَعَ الشَّمْسُ ya da طَلَعَتِ الشَّمْسُ. Ayrım lügavîdir: bir ismin hakikî müennes olup olmadığı yüzeyin değil sözlüğün bilgisidir.",
         "Fiil, ardındaki ism-i zâhire uymak için tesniye ya da cemi alâmeti alabilir mi (أَكَلُونِي الْبَرَاغِيثُ)? Defter buna zayıf der: ism-i zâhir faildir ve fiil müfred kalır.",
         "Tenvin nedir, ne DEĞİLDİR? Son harekeden sonra okunan ve harf olarak yazılmayan sâkin bir nûndur; tarifin son cümlesinin dışarıda bıraktığı hafif te'kid nûnu (اِضْرِبَنْ) değildir.",
         "Beş kısım nedir? Temekkün (munsariflik: زَيْدٌ), tenkir (nekrelik: رَجُلٌ), ivaz (düşmüş muzâfun ileyhin yerini tutma: يَوْمَئِذٍ, aslı يَوْمَ إِذْ كَانَ كَذَا), mukabele (cemi müennes sâlimin cemi müzekker nûnuna karşılığı: مُسْلِمَاتٌ) ve terennüm (beyit sonundaki nağme tenvini). Alâmet motoru tenvini munsarif ismin alâmeti olarak okur; ivaz tenvini gayr-i munsarif bâbında مَعَانٍ üzerinde kalan tenvindir.",
         "Niçin tenvinsiz ve elifsiz زَيْدُ بْنُ عَمْرٍو? Çünkü iki alem arasındaki ابْن o kadar yaygındır ki dil onu iki kez hafifletmiştir: mevsuf alem tenvinini, sıfat elifini düşürür. Buradaki i'râb satırları bir ismi ibn izlediği yerde bu kuralı uygular."]},
 "plain": {
  "en": "Three small things. Kallā is a hard «no» (in the Qur'an sometimes «truly»). A past verb gets a silent t when its subject is female; with words like «the sun» you may add it or not. The tanwīn is the little nūn you hear at a word's end and never write; it has five jobs, and it falls off a name followed by «son of».",
  "tr": "Üç küçük şey. Kellâ sert bir «hayır»dır (Kur'ân'da bazen «gerçekten»). Mâzî fiil, faili dişi olunca sessiz bir t alır; «güneş» gibi kelimelerde eklersin ya da eklemezsin. Tenvin, kelime sonunda duyduğun ve hiç yazmadığın küçük nûndur; beş işi vardır ve ardından «oğlu» gelen addan düşer."},
 "explanation": {
  "en": "Three short bābs the Kafiya sets at the end of its ḥurūf: the letter of rebuke, the tāʾ of femininity on the verb and the tanwīn. The notebook's additions are the usable ones — كَلَّا answered to a claim and to a command, the Qur'anic «truly» sense, the optional tāʾ with a non-real feminine, the weakness of a dual or plural mark on the verb, the five tanwīns each with its one example and the ʿiwaḍ origin spelled out (يَوْمَ إِذْ كَانَ كَذَا), and the lightening of زَيْدُ بْنُ عَمْرٍو explained by frequency. The tanwīn definition's last clause (لَا لِتَأْكِيدِ الْفِعْلِ) is the bridge to the next chapter, the nūn of emphasis.",
  "tr": "Kâfiye'nin harflerinin sonuna koyduğu üç kısa bâb: red harfi, fiildeki te'nîs tâ'sı ve tenvin. Defterin ekleri kullanılabilir olanlardır — iddiaya ve emre cevap olarak كَلَّا, Kur'ânî «gerçekten» mânâsı, hakikî olmayan müennesle ihtiyarî tâ, fiilde tesniye ya da cemi alâmetinin zayıflığı, her biri tek örnekli beş tenvin ve açıkça yazılmış ivaz aslı (يَوْمَ إِذْ كَانَ كَذَا) ve sıklıkla açıklanan زَيْدُ بْنُ عَمْرٍو hafifletmesi. Tenvin tarifinin son cümlesi (لَا لِتَأْكِيدِ الْفِعْلِ) bir sonraki bâba, te'kid nûnuna köprüdür."},
 "examples": [
  {"ar": "فُلَانٌ يُبْغِضُكَ — كَلَّا", "en": "Kallā rebuking a claim.", "tr": "Bir iddiayı reddeden kellâ.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "كَلَّا إِنَّ الْإِنْسَانَ لَيَطْغَى", "en": "Kallā in the sense of «truly».", "tr": "«Gerçekten» mânâsında kellâ.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "ضَرَبَتْ هِنْدٌ — طَلَعَ الشَّمْسُ / طَلَعَتِ الشَّمْسُ", "en": "The obligatory and the optional tāʾ.", "tr": "Vâcip ve ihtiyarî tâ.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "زَيْدٌ — رَجُلٌ — يَوْمَئِذٍ — مُسْلِمَاتٌ", "en": "Four of the five tanwīns.", "tr": "Beş tenvinden dördü.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "جَاءَنِي زَيْدُ بْنُ عَمْرٍو", "en": "The tanwīn dropped before ibn.", "tr": "İbn'den önce düşen tenvin.", "sourceStory": "al-kafiya", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«جَاءَنِي زَيْدٌ ابْنُ عَمْرٍو»",
   "right": "«جَاءَنِي زَيْدُ بْنُ عَمْرٍو — iki alem arasında ibn: tenvin ve elif düşer»",
   "why": {"en": "Frequency lightened the phrase twice; both drops are obligatory.", "tr": "Sıklık terkibi iki kez hafifletti; iki düşme de vâciptir."}},
  {"wrong": "«طَلَعَ الشَّمْسُ hatalıdır»",
   "right": "«câizdir — gayr-i hakikî müenneste tâ ihtiyarîdir»",
   "why": {"en": "Only a real feminine subject forces the tāʾ.", "tr": "Yalnız hakikî müennes fail tâ'yı zorunlu kılar."}},
  {"wrong": "«مُسْلِمَاتٌ'taki tenvin tenkir içindir»",
   "right": "«mukabele içindir — مُسْلِمُونَ'nin nûnuna karşılık»",
   "why": {"en": "The feminine sound plural keeps this tanwīn even when definite by idafa is not at issue; it answers the masculine plural's nūn.", "tr": "Cemi müennes sâlim bu tenvini müzekker ceminin nûnuna karşılık taşır."}}],
 "relatedNotes": ["al-fail-al-muzhar-wa-tanith-amilih", "al-jumu-wa-tanith-amiliha", "al-muannath-wa-alamatuh", "ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh", "nun-tawkid"]}

ADD_EN = (" Chapter 44 (notebook lines ~348-353): kallā (rebuke, refusal after a command, «truly» in 96:6), the tāʾ of femininity (obligatory with a real feminine, optional with a non-real one, the dual/plural mark on the verb weak), the tanwīn defined and its five kinds, and the tanwīn dropped before ibn — the notebook's exposition, kept as commentary (s1-s9).")
ADD_TR = (" Kırk dördüncü bâb (defter satırları ~348-353): kellâ (red, emirden sonra ret, 96:6'da «gerçekten»), te'nîs tâ'sı (hakikî müennesle vâcip, gayr-i hakikîyle ihtiyarî, fiilde tesniye/cemi alâmeti zayıf), tenvinin tarifi ve beş kısmı ve ibn'den önce düşen tenvin — defterin açıklaması, şerh olarak (s1-s9).")
write_out(44, S, TITLE, ADD_EN, ADD_TR, "348-353", GLOSS_ADD, notes=(NOTE,),
          related=(("al-fail-al-muzhar-wa-tanith-amilih", [K]), ("ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh", [K])))
report(44, S, GLOSS_ADD, (NOTE,))
