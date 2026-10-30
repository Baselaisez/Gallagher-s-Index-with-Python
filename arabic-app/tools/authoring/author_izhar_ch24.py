# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 24: the APPARENT ATTACHED pronoun — found in the second of the verbs (the dual), the alif:
# ضَرَبَا وَضَرَبَتَا وَضَرَبْتُمَا وَيَضْرِبَانِ وَتَضْرِبَانِ وَلِيَضْرِبَا وَلِتَضْرِبَا وَاضْرِبَا وَلَا يَضْرِبَا وَلَا تَضْرِبَا; its masculine plural, the wāw:
# ضَرَبُوا وَضَرَبْتُمْ (its origin ضَرَبْتُمُوا) وَيَضْرِبُونَ وَتَضْرِبُونَ وَلِيَضْرِبُوا; its feminine plural, the nūn: ضَرَبْنَ وَضَرَبْتُنَّ وَيَضْرِبْنَ
# وَتَضْرِبْنَ وَلِيَضْرِبْنَ وَاضْرِبْنَ وَلَا يَضْرِبْنَ وَلَا تَضْرِبْنَ; the single addressee, masculine or feminine, and the speaker alone in the
# past, the tāʾ: ضَرَبْتَ with the tāʾ's vowels; the speaker with others in the past, نَا: ضَرَبْنَا; the single feminine addressee outside
# the past, the yāʾ: تَضْرِبِينَ وَاضْرِبِي وَلَا تَضْرِبِي. Print pp. 124–125.
#   python3 author_izhar_ch24.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-bariz-al-muttasil"
K22 = "al-fail-al-mudmar-al-mustatir-wujuban"; K23 = "al-mustatir-jawazan"
TITLE = {"ar": "الضَّمِيرُ الْبَارِزُ الْمُتَّصِلُ", "en": "The apparent attached pronoun", "tr": "Bâriz muttasıl zamir"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; LN = "la-nafiya"; MR = "mudari-marfu"; JMS = "jam-mudhakkar-salim"; JMA = "jam-muannath-salim"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; MSD = "masdar"
LA = "lam-amr"; LNH = "la-nahiya"; JZ = "nawasib-wa-jawazim-al-mudari"; AMR = "imperative-amr"; MH = "mahall-al-majrur"; F8 = "form-viii-verbs"; YM = "ya-al-mutakallim"; QLB = "al-mutaaddi-wa-afal-al-qulub"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)
def wahuwa(): return tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الضَّمِيرُ.", "«and it is» — the pronoun.", "«o da» — zamir.", segments=wa("هُوَ", "huwa", "pron"))
def V(form, ar, en, tr, first=False, punct=None, segs=None):
    """a cited conjugation of ضَرَبَ, joined by wāw unless first"""
    g = [K, FL, MH] if first else [K, AT, FL, MH]
    if segs is None and not first: segs = wa(form[1:], "daraba", "verb")
    return tok(form, "daraba", "verb", g, ("لَفْظٌ مَحْكِيٌّ: " if first else "الْوَاوُ عَاطِفَةٌ، وَ") + ar, en, tr, punct=punct, segments=segs)
def LV(form, ar, en, tr, punct=None, neg=False):
    """وَلِيَضْرِبَا — the lām of command joined by wāw"""
    return tok(form, "daraba", "verb", [K, AT, FL, LA, JZ, MH], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لَامُ الْأَمْرِ، وَ" + ar, en, tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لِ", "lam-amr", "part"), seg(form[4:], "daraba", "verb")])
def LAA(): return tok("وَلَا", "la-nahiya", "part", [K, AT, LNH, JZ], "الْوَاوُ عَاطِفَةٌ، وَلَا النَّاهِيَةُ.", "«and let … not»", "«ve -masın»", segments=wa("لَا", "la-nahiya", "part"))
def NV(form, ar, en, tr, punct=None): return tok(form, "daraba", "verb", [K, FL, LNH, JZ, MH], ar, en, tr, punct=punct)

# ----------- s1 — the apparent attached: the alif of the dual
S.append({"id": "s1", "translation": {"en": "As for the apparent attached pronoun, it is found in the second of the verbs — and that is the alif — as in «they two struck», «they two (f.) struck», «you two struck», «they two strike», «you two strike», «let them two strike», «let you two strike», «strike, you two!», «let them two not strike», «let you two not strike»;", "tr": "Bâriz muttasıl zamire gelince, fiillerin ikincisinde bulunur — o da eliftir: «o ikisi vurdu», «o ikisi (dişi) vurdu», «siz ikiniz vurdunuz», «o ikisi vurur», «siz ikiniz vurursunuz», «o ikisi vursun», «siz ikiniz vurun», «vurun ikiniz!», «o ikisi vurmasın», «siz ikiniz vurmayın» gibi;"},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْبَارِزُ", "bariz", "noun", [K, MK, IFA], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the apparent» — the mubtada.", "«bâriz» — mübtedâ."),
  tok("الْمُتَّصِلُ", "muttasil", "noun", [K, NA, F8, IFA], "نَعْتٌ مَرْفُوعٌ — الَّذِي لَا يُبْتَدَأُ بِهِ وَلَا يَقَعُ بَعْدَ إِلَّا.", "«attached» — never clause-initial, never after illā.", "«muttasıl» — başta ve illâ'dan sonra gelmeyen."),
  tok("فَوُجِدَ", "wajada", "verb", [K, MK, NF, "mithal-verbs"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَوُجِدَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«is found» — the khabar after ammā's fāʾ.", "«bulunur» — emmâ'nın fâsından sonra haber.", segments=fa("وُجِدَ", "wajada", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("ثَانِي", "thani", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، مُضَافٌ — الصِّيغَةُ الثَّانِيَةُ: الْمُثَنَّى.", "«the second of» — the second form: the dual.", "«ikincisi» — ikinci sîga: tesniye."),
  tok("الْأَفْعَالِ", "afal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَفْعَالُ التَّصْرِيفِ.", "«the verbs» — the conjugation's forms.", "«fiiller» — tasrîf sîgaları.", punct="،"),
  wahuwa(),
  tok("الْأَلِفُ", "alif-letter", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ — أَلِفُ الِاثْنَيْنِ.", "«the alif» — the dual's alif.", "«elif» — tesniye elifi.", punct="،"),
  nahw(),
  V("ضَرَبَا", "فِعْلٌ مَاضٍ، وَالْأَلِفُ ضَمِيرُ الِاثْنَيْنِ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«they two struck» — the alif the doer.", "«o ikisi vurdu» — elif fâil.", first=True),
  V("وَضَرَبَتَا", "ضَرَبَتَا فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْأَلِفُ فَاعِلٌ.", "«they two (f.) struck»", "«o ikisi (dişi) vurdu»"),
  V("وَضَرَبْتُمَا", "ضَرَبْتُمَا فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَمَا لِلتَّثْنِيَةِ.", "«you two struck» — the tāʾ the doer, mā the dual's sign.", "«siz ikiniz vurdunuz» — tâ fâil."),
  V("وَيَضْرِبَانِ", "يَضْرِبَانِ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«they two strike»", "«o ikisi vurur»"),
  V("وَتَضْرِبَانِ", "تَضْرِبَانِ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«you two strike»", "«siz ikiniz vurursunuz»"),
  LV("وَلِيَضْرِبَا", "يَضْرِبَا مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«let them two strike»", "«o ikisi vursun»"),
  LV("وَلِتَضْرِبَا", "تَضْرِبَا مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«let you two strike»", "«siz ikiniz vurun»"),
  tok("وَاضْرِبَا", "daraba", "verb", [K, AT, FL, AMR, MH], "الْوَاوُ عَاطِفَةٌ، وَاضْرِبَا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«strike, you two!»", "«vurun ikiniz!»", segments=wa("اضْرِبَا", "daraba", "verb")),
  LAA(),
  NV("يَضْرِبَا", "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«them two strike»", "«o ikisi vursun»"),
  LAA(),
  NV("تَضْرِبَا", "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«you two strike»", "«siz ikiniz vurun»", punct="؛"),
 ]})
# ----------- s2 — its masculine plural, the wāw
S.append({"id": "s2", "translation": {"en": "and in its masculine plural — and that is the wāw — as in «they struck», «you struck» (since its origin is ḍarabtumū), «they strike», «you strike», «let them strike»;", "tr": "ve onun müzekker cem'inde — o da vâvdır: «onlar vurdu», «siz vurdunuz» (aslı darabtümû olduğundan), «onlar vurur», «siz vurursunuz», «onlar vursun» gibi;"},
 "tokens": [
  tok("وَجَمْعِهَا", "jam", "noun", [K, AT, ID, JMS], "الْوَاوُ عَاطِفَةٌ، وَجَمْعِهَا مَعْطُوفٌ عَلَى ثَانِي مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعِ الْأَفْعَالِ.", "«and its plural» — the verbs' plural.", "«ve cem'i» — fiillerin cem'i.", segments=[seg("وَ", "wa", "conj"), seg("جَمْعِ", "jam", "noun"), pr3fs()]),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, NA, JMS], "نَعْتٌ مَجْرُورٌ.", "«masculine»", "«müzekker»", punct="،"),
  wahuwa(),
  tok("الْوَاوُ", "waw-letter", "noun", [K, MK, JMS], "خَبَرٌ مَرْفُوعٌ — وَاوُ الْجَمَاعَةِ.", "«the wāw» — the plural's wāw.", "«vâv» — cemâat vâvı.", punct="،"),
  nahw(),
  V("ضَرَبُوا", "فِعْلٌ مَاضٍ، وَالْوَاوُ ضَمِيرُ الْجَمَاعَةِ فَاعِلٌ فِي مَحَلِّ رَفْعٍ، وَالْأَلِفُ فَارِقَةٌ.", "«they struck» — the wāw the doer.", "«onlar vurdu» — vâv fâil.", first=True),
  V("وَضَرَبْتُمْ", "ضَرَبْتُمْ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ عَلَامَةُ الْجَمْعِ.", "«you struck»", "«siz vurdunuz»"),
  tok("إِذْ", "idh", "part", [K, MF], "حَرْفُ تَعْلِيلٍ.", "«since»", "«çünkü»"),
  tok("أَصْلُهُ", "asl", "noun", [K, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its origin» — the mubtada.", "«aslı» — mübtedâ.", segments=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  tok("ضَرَبْتُمُوا", "daraba", "verb", [K, MK, FL, MH, JMS], "لَفْظٌ مَحْكِيٌّ خَبَرٌ فِي مَحَلِّ رَفْعٍ — التَّاءُ فَاعِلٌ، وَالْمِيمُ وَالْوَاوُ لِلْجَمْعِ: حُذِفَتِ الْوَاوُ تَخْفِيفًا.", "«ḍarabtumū» — the wāw later dropped for lightness.", "«darabtümû» — vâv hafiflik için düştü.", punct="،"),
  V("وَيَضْرِبُونَ", "يَضْرِبُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«they strike»", "«onlar vurur»"),
  V("وَتَضْرِبُونَ", "تَضْرِبُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«you strike»", "«siz vurursunuz»"),
  LV("وَلِيَضْرِبُوا", "يَضْرِبُوا مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«let them strike»", "«onlar vursun»", punct="؛"),
 ]})
# ----------- s3 — its feminine plural, the nūn
S.append({"id": "s3", "translation": {"en": "and in its feminine plural — and that is the nūn — as in «they (f.) struck», «you (f.) struck», «they (f.) strike», «you (f.) strike», «let them (f.) strike», «strike, you (f.)!», «let them (f.) not strike», «let you (f.) not strike»;", "tr": "ve onun müennes cem'inde — o da nûndur: «onlar (dişi) vurdu», «siz (dişi) vurdunuz», «onlar (dişi) vurur», «siz (dişi) vurursunuz», «onlar (dişi) vursun», «vurun (dişi)!», «onlar (dişi) vurmasın», «siz (dişi) vurmayın» gibi;"},
 "tokens": [
  tok("وَجَمْعِهَا", "jam", "noun", [K, AT, ID, JMA], "الْوَاوُ عَاطِفَةٌ، وَجَمْعِهَا مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its plural»", "«ve cem'i»", segments=[seg("وَ", "wa", "conj"), seg("جَمْعِ", "jam", "noun"), pr3fs()]),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, NA, JMA], "نَعْتٌ مَجْرُورٌ.", "«feminine»", "«müennes»", punct="،"),
  wahuwa(),
  tok("النُّونُ", "nun-letter", "noun", [K, MK, JMA], "خَبَرٌ مَرْفُوعٌ — نُونُ النِّسْوَةِ.", "«the nūn» — the women's nūn.", "«nûn» — nisve nûnu.", punct="،"),
  nahw(),
  V("ضَرَبْنَ", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ ضَمِيرُ النِّسْوَةِ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«they (f.) struck» — the nūn the doer.", "«onlar (dişi) vurdu» — nûn fâil.", first=True),
  V("وَضَرَبْتُنَّ", "ضَرَبْتُنَّ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ عَلَامَةُ جَمْعِ الْمُؤَنَّثِ.", "«you (f.) struck»", "«siz (dişi) vurdunuz»"),
  V("وَيَضْرِبْنَ", "يَضْرِبْنَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ فَاعِلٌ.", "«they (f.) strike» — built on the sukūn for the nūn.", "«onlar (dişi) vurur» — nisve nûnu ile sükûn üzere mebnî."),
  V("وَتَضْرِبْنَ", "تَضْرِبْنَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ فَاعِلٌ.", "«you (f.) strike»", "«siz (dişi) vurursunuz»"),
  LV("وَلِيَضْرِبْنَ", "يَضْرِبْنَ فِي مَحَلِّ جَزْمٍ، وَالنُّونُ فَاعِلٌ.", "«let them (f.) strike»", "«onlar (dişi) vursun»"),
  tok("وَاضْرِبْنَ", "daraba", "verb", [K, AT, FL, AMR, MH], "الْوَاوُ عَاطِفَةٌ، وَاضْرِبْنَ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ فَاعِلٌ.", "«strike, you (f.)!»", "«vurun (dişi)!»", segments=wa("اضْرِبْنَ", "daraba", "verb")),
  LAA(),
  NV("يَضْرِبْنَ", "فِعْلٌ مُضَارِعٌ فِي مَحَلِّ جَزْمٍ بِلَا، وَالنُّونُ فَاعِلٌ.", "«them (f.) strike»", "«onlar (dişi) vursun»"),
  LAA(),
  NV("تَضْرِبْنَ", "فِعْلٌ مُضَارِعٌ فِي مَحَلِّ جَزْمٍ بِلَا، وَالنُّونُ فَاعِلٌ.", "«you (f.) strike»", "«siz (dişi) vurun»", punct="؛"),
 ]})
# ----------- s4 — the single addressee and the speaker alone in the past: the tāʾ
S.append({"id": "s4", "translation": {"en": "and in the single addressee, masculine or feminine, and the speaker alone, in the past — and that is the tāʾ — as in «you struck», with the tāʾ's vowels;", "tr": "ve mâzîde müfred muhâtabda — müzekker olsun müennes olsun — ve tek başına mütekellimde — o da tâdır: «vurdun», tânın harekeleriyle;"},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى فِي ثَانِي الْأَفْعَالِ.", "«and in»", "«ve -de»", segments=wa("فِي", "fi", "prep")),
  tok("الْمُخَاطَبِ", "mukhatab", "noun", [K, HJ, IMF], "مَجْرُورٌ بِفِي.", "«the addressee»", "«muhâtab»"),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«single»", "«müfred»"),
  tok("مُذَكَّرًا", "mudhakkar", "noun", [K, KN, HL], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ — وَالْجُمْلَةُ حَالٌ.", "«masculine» — kāna's khabar put first.", "«müzekker» — öne alınmış kâne haberi."),
  tok("كَانَ", "kana", "verb", [K, KN], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمُخَاطَبُ.", "«it be» — kāna, its ism the addressee.", "«olsun» — kâne, ismi muhâtab."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مُؤَنَّثًا", "muannath", "noun", [K, AT, KN], "مَعْطُوفٌ عَلَى مُذَكَّرًا مَنْصُوبٌ.", "«feminine»", "«müennes»"),
  tok("وَالْمُتَكَلِّمِ", "mutakallim", "noun", [K, AT, IFA], "الْوَاوُ عَاطِفَةٌ، وَالْمُتَكَلِّمِ مَعْطُوفٌ عَلَى الْمُخَاطَبِ مَجْرُورٌ.", "«and the speaker»", "«ve mütekellim»", segments=wa("الْمُتَكَلِّمِ", "mutakallim", "noun")),
  tok("وَحْدَهُ", "wahda", "noun", [K, HL, ID], "حَالٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُنْفَرِدًا.", "«alone» — a ḥāl.", "«tek başına» — hâl.", segments=[seg("وَحْدَ", "wahda", "noun"), pr3ms()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمَاضِي", "madi", "noun", [K, HJ], "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past»", "«mâzî»", punct="،"),
  wahuwa(),
  tok("التَّاءُ", "ta-letter", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ — تَاءُ الْفَاعِلِ.", "«the tāʾ» — the doer's tāʾ.", "«tâ» — fâil tâsı.", punct="،"),
  nahw(),
  V("ضَرَبْتَ", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ ضَمِيرٌ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«you struck» — the tāʾ the doer.", "«vurdun» — tâ fâil.", first=True),
  tok("بِحَرَكَاتِ", "haraka", "noun", [K, HJ, ID, JMA], "الْبَاءُ حَرْفُ جَرٍّ، وَحَرَكَاتِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ.", "«with the vowels of» — fatḥa for the masculine, kasra for the feminine, ḍamma for the speaker.", "«harekeleriyle» — müzekkere fetha, müennese kesre, mütekellime zamme.", segments=[seg("بِ", "bi", "prep"), seg("حَرَكَاتِ", "haraka", "noun")]),
  tok("التَّاءِ", "ta-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tāʾ»", "«tânın»", punct="؛"),
 ]})
# ----------- s5 — the speaker with others in the past: نَا
S.append({"id": "s5", "translation": {"en": "and in the speaker with others, in the past — and that is nā — as in «we struck»;", "tr": "ve mâzîde başkalarıyla birlikte mütekellimde — o da nâ'dır: «vurduk» gibi;"},
 "tokens": [
  tok("وَالْمُتَكَلِّمِ", "mutakallim", "noun", [K, AT, IFA], "الْوَاوُ عَاطِفَةٌ، وَالْمُتَكَلِّمِ مَعْطُوفٌ مَجْرُورٌ.", "«and the speaker»", "«ve mütekellim»", segments=wa("الْمُتَكَلِّمِ", "mutakallim", "noun")),
  tok("مَعَهُ", "maa", "noun", [K, MF, ID, MK], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ حَالٌ.", "«with whom» — the fronted khabar of a ḥāl clause.", "«beraberinde» — hâl cümlesinin öne alınmış haberi.", segments=[seg("مَعَ", "maa", "noun"), pr3ms()]),
  tok("غَيْرُهُ", "ghayr", "noun", [K, MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«others» — the mubtada put after.", "«başkası» — sonraya bırakılmış mübtedâ.", segments=[seg("غَيْرُ", "ghayr", "noun"), pr3ms()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمَاضِي", "madi", "noun", [K, HJ], "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past»", "«mâzî»", punct="،"),
  wahuwa(),
  tok("نَا", "pron-1p", "pron", [K, MK], "لَفْظٌ مَحْكِيٌّ خَبَرٌ فِي مَحَلِّ رَفْعٍ — ضَمِيرُ الْمُتَكَلِّمِ مَعَ الْغَيْرِ.", "«nā» — the pronoun of the speaker with others.", "«nâ» — başkalarıyla mütekellim zamiri.", punct="،"),
  nahw(),
  V("ضَرَبْنَا", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا ضَمِيرٌ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«we struck» — nā the doer.", "«vurduk» — nâ fâil.", first=True, punct="؛"),
 ]})
# ----------- s6 — the single feminine addressee outside the past: the yāʾ
S.append({"id": "s6", "translation": {"en": "and in the single feminine addressee outside the past — and that is the yāʾ — as in «you (f.) strike», «strike, you (f.)!», «do not strike, you (f.)!».", "tr": "ve mâzî dışında müfred müennes muhâtabada — o da yâdır: «vurursun (dişi)», «vur (dişi)!», «vurma (dişi)!» gibi."},
 "tokens": [
  tok("وَالْمُخَاطَبَةِ", "mukhataba-fem", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَالْمُخَاطَبَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the feminine addressee»", "«ve muhâtaba»", segments=wa("الْمُخَاطَبَةِ", "mukhataba-fem", "noun")),
  tok("الْمُفْرَدَةِ", "mufrad", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«single»", "«müfrede»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("الْمَاضِي", "madi", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past»", "«mâzî»", punct="،"),
  wahuwa(),
  tok("الْيَاءُ", "ya-letter", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ — يَاءُ الْمُخَاطَبَةِ.", "«the yāʾ» — the feminine addressee's yāʾ.", "«yâ» — muhâtaba yâsı.", punct="،"),
  nahw(),
  V("تَضْرِبِينَ", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْيَاءُ ضَمِيرٌ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«you (f.) strike» — the yāʾ the doer.", "«vurursun (dişi)» — yâ fâil.", first=True),
  tok("وَاضْرِبِي", "daraba", "verb", [K, AT, FL, AMR, MH], "الْوَاوُ عَاطِفَةٌ، وَاضْرِبِي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ فَاعِلٌ.", "«strike, you (f.)!»", "«vur (dişi)!»", segments=wa("اضْرِبِي", "daraba", "verb")),
  LAA(),
  NV("تَضْرِبِي", "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا بِحَذْفِ النُّونِ، وَالْيَاءُ فَاعِلٌ.", "«you (f.) strike»", "«vur (dişi)»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "mukhataba-fem": G("mukhataba-fem", "مُخَاطَبَة", "خ ط ب", "noun", "the feminine addressee — the second person singular feminine (ism mafʿūl of خَاطَبَ)", "muhâtaba — ikinci tekil şahıs dişi (hâtabe'nin ism-i mef'ûlü)", 4, form="III"),
}
used = set()
for s in S:
    for t in s["tokens"]:
        used.add(t["lex"])
        for sg_ in t.get("segments", []): used.add(sg_["lex"])
CAND = {}
for k in sorted(used):
    if k in TG: continue
    if k in NEW: CAND[k] = NEW[k]
    elif _ic.has_gloss(k): CAND[k] = find_gloss(k)
    else: raise SystemExit(f"no gloss anywhere for {k}")
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch24 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("daraba", "wajada", "kana") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الضَّمِيرُ الْبَارِزُ الْمُتَّصِلُ الْمَرْفُوعُ: الْأَلِفُ وَالْوَاوُ وَالنُّونُ وَالتَّاءُ وَنَا وَالْيَاءُ", "en": "The apparent attached pronoun in rafʿ: the alif, the wāw, the nūn, the tāʾ, nā and the yāʾ", "tr": "Merfû bâriz muttasıl zamir: elif, vâv, nûn, tâ, nâ ve yâ"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الفاعل: البارز المتصل", "الكافية لابن الحاجب — المضمر المتصل المرفوع", "شرح قطر الندى لابن هشام — الضمائر المتصلة"],
 "amil": "the apparent attached pronoun as doer is the alif of the dual (second of the verbs: ضَرَبَا، ضَرَبَتَا، ضَرَبْتُمَا، يَضْرِبَانِ، تَضْرِبَانِ، لِيَضْرِبَا، لِتَضْرِبَا، اضْرِبَا، لَا يَضْرِبَا، لَا تَضْرِبَا), the wāw of the masculine plural (ضَرَبُوا، ضَرَبْتُمْ from ضَرَبْتُمُوا، يَضْرِبُونَ، تَضْرِبُونَ، لِيَضْرِبُوا), the nūn of the feminine plural (ضَرَبْنَ، ضَرَبْتُنَّ، يَضْرِبْنَ، تَضْرِبْنَ، لِيَضْرِبْنَ، اضْرِبْنَ، لَا يَضْرِبْنَ، لَا تَضْرِبْنَ), the tāʾ of the single addressee and the speaker alone in the past (ضَرَبْتَ with its vowels), nā of the speaker with others in the past (ضَرَبْنَا), and the yāʾ of the single feminine addressee outside the past (تَضْرِبِينَ، اضْرِبِي، لَا تَضْرِبِي)",
 "question": {
  "en": ["Where is the apparent attached pronoun found as doer? In the second of the verbs — the dual — and it is the alif: ضَرَبَا، ضَرَبَتَا، ضَرَبْتُمَا، يَضْرِبَانِ، تَضْرِبَانِ، لِيَضْرِبَا، لِتَضْرِبَا، اضْرِبَا، لَا يَضْرِبَا، لَا تَضْرِبَا.",
         "And in the masculine plural? The wāw: ضَرَبُوا، ضَرَبْتُمْ — whose origin is ضَرَبْتُمُوا — يَضْرِبُونَ، تَضْرِبُونَ، لِيَضْرِبُوا.",
         "And in the feminine plural? The nūn: ضَرَبْنَ، ضَرَبْتُنَّ، يَضْرِبْنَ، تَضْرِبْنَ، لِيَضْرِبْنَ، اضْرِبْنَ، لَا يَضْرِبْنَ، لَا تَضْرِبْنَ.",
         "What is the tāʾ? The doer of the single addressee, masculine or feminine, and of the speaker alone, in the past: ضَرَبْتَ، ضَرَبْتِ، ضَرَبْتُ — told apart by the tāʾ's vowels.",
         "And nā and the yāʾ? nā is the speaker with others in the past (ضَرَبْنَا); the yāʾ is the single feminine addressee outside the past (تَضْرِبِينَ، اضْرِبِي، لَا تَضْرِبِي).",
         "Why does ضَرَبْتُمْ belong to the wāw? Because its origin is ضَرَبْتُمُوا: the wāw of the plural was dropped for lightness and the mīm keeps its trace.",
         "What does the engine READ here? The DabtEngine keeps every cited conjugation as quoted wording, writes the five verbs with their nūn in rafʿ and without it after the lām of command and the prohibitive lā, and reads the letter names as the khabars of «and it is»."],
  "tr": ["Bâriz muttasıl zamir fâil olarak nerede bulunur? Fiillerin ikincisinde — tesniyede — o da eliftir: darabâ, darabetâ, darabtümâ, yadribâni, tadribâni, li-yadribâ, li-tadribâ, idribâ, lâ yadribâ, lâ tadribâ.",
         "Müzekker cem'inde? Vâv: darabû, darabtüm — aslı darabtümû — yadribûne, tadribûne, li-yadribû.",
         "Müennes cem'inde? Nûn: darabne, darabtünne, yadribne, tadribne, li-yadribne, idribne, lâ yadribne, lâ tadribne.",
         "Tâ nedir? Mâzîde müfred muhâtabın — müzekker ya da müennes — ve tek başına mütekellimin fâili: darabte, darabti, darabtü — tânın harekeleriyle ayrılır.",
         "Nâ ve yâ? Nâ mâzîde başkalarıyla mütekellimdir (darabnâ); yâ mâzî dışında müfred müennes muhâtabadır (tadribîne, idribî, lâ tadribî).",
         "Darabtüm niçin vâva âittir? Çünkü aslı darabtümû'dur: cem' vâvı hafiflik için düşmüş, mîm izini korumuştur.",
         "Motor burada neyi OKUR? DabtEngine zikredilen her çekimi nakledilmiş lafız olarak tutar, beş fiili ref'de nûnlu, emir lâmı ve nehiy lâsından sonra nûnsuz yazar ve harf adlarını «o da»nın haberi olarak okur."],
 },
 "plain": {"en": "Some subjects are letters stuck to the verb: the alif for «they two», the wāw for «they», the nūn for «they (women)», the tāʾ for «you» and «I» in the past, nā for «we», and the yāʾ for «you (woman)». This chapter lists them with every form of «strike», including the command and prohibition forms.",
           "tr": "Bazı özneler fiile yapışık harflerdir: «o ikisi» için elif, «onlar» için vâv, «onlar (kadınlar)» için nûn, mâzîde «sen» ve «ben» için tâ, «biz» için nâ, «sen (kadın)» için yâ. Bu bölüm onları «vurmak» fiilinin her sîgasıyla, emir ve nehiy sîgaları dahil, sayar."},
 "explanation": {"en": "As for the apparent attached pronoun, it is found in the second of the verbs, the dual, and that is the alif (ضَرَبَا، ضَرَبَتَا، ضَرَبْتُمَا، يَضْرِبَانِ، تَضْرِبَانِ، لِيَضْرِبَا، لِتَضْرِبَا، اضْرِبَا، لَا يَضْرِبَا، لَا تَضْرِبَا); in its masculine plural, the wāw (ضَرَبُوا، ضَرَبْتُمْ — since its origin is ضَرَبْتُمُوا — يَضْرِبُونَ، تَضْرِبُونَ، لِيَضْرِبُوا); in its feminine plural, the nūn (ضَرَبْنَ، ضَرَبْتُنَّ، يَضْرِبْنَ، تَضْرِبْنَ، لِيَضْرِبْنَ، اضْرِبْنَ، لَا يَضْرِبْنَ، لَا تَضْرِبْنَ); in the single addressee, masculine or feminine, and the speaker alone in the past, the tāʾ (ضَرَبْتَ with the tāʾ's vowels); in the speaker with others in the past, nā (ضَرَبْنَا); and in the single feminine addressee outside the past, the yāʾ (تَضْرِبِينَ، اضْرِبِي، لَا تَضْرِبِي).",
                 "tr": "Bâriz muttasıl zamire gelince, fiillerin ikincisinde, tesniyede bulunur ve o eliftir (darabâ, darabetâ, darabtümâ, yadribâni, tadribâni, li-yadribâ, li-tadribâ, idribâ, lâ yadribâ, lâ tadribâ); müzekker cem'inde vâv (darabû, darabtüm — aslı darabtümû — yadribûne, tadribûne, li-yadribû); müennes cem'inde nûn (darabne, darabtünne, yadribne, tadribne, li-yadribne, idribne, lâ yadribne, lâ tadribne); mâzîde müfred muhâtab — müzekker ya da müennes — ve tek başına mütekellimde tâ (darabte, tânın harekeleriyle); mâzîde başkalarıyla mütekellimde nâ (darabnâ); mâzî dışında müfred müennes muhâtabada yâ (tadribîne, idribî, lâ tadribî)."},
 "examples": [
  {"ar": "ضَرَبَا وَضَرَبَتَا وَضَرَبْتُمَا وَيَضْرِبَانِ وَتَضْرِبَانِ", "en": "the dual's alif", "tr": "tesniye elifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "ضَرَبُوا وَضَرَبْتُمْ إِذْ أَصْلُهُ ضَرَبْتُمُوا", "en": "the plural's wāw and the dropped wāw of ḍarabtum", "tr": "cem' vâvı ve darabtüm'ün düşen vâvı", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "ضَرَبْنَ وَضَرَبْتُنَّ وَيَضْرِبْنَ وَتَضْرِبْنَ", "en": "the women's nūn", "tr": "nisve nûnu", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "ضَرَبْتَ بِحَرَكَاتِ التَّاءِ", "en": "the doer's tāʾ with its three vowels", "tr": "üç harekesiyle fâil tâsı", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "ضَرَبْنَا", "en": "nā of the speaker with others", "tr": "başkalarıyla mütekellimin nâsı", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "تَضْرِبِينَ وَاضْرِبِي وَلَا تَضْرِبِي", "en": "the feminine addressee's yāʾ", "tr": "muhâtaba yâsı", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "لِيَضْرِبَانِ", "right": "لِيَضْرِبَا", "why": {"en": "after the lām of command the dual loses its nūn: jazm by the dropped nūn", "tr": "emir lâmından sonra tesniye nûnunu kaybeder: nûnun hazfi ile cezm"}},
  {"wrong": "ضَرَبْتُمُوا (as the current form)", "right": "ضَرَبْتُمْ", "why": {"en": "the wāw is the origin's; it is dropped for lightness, the mīm keeps its trace", "tr": "vâv aslındır; hafiflik için düşer, mîm izini korur"}},
  {"wrong": "لَا تَضْرِبِينَ (as a prohibition)", "right": "لَا تَضْرِبِي", "why": {"en": "the prohibitive lā drops the nūn of the five verbs", "tr": "nehiy lâsı beş fiilin nûnunu düşürür"}},
 ],
}
ADD_EN = (" Chapter 24 (print pp. 124-125): the apparent attached pronoun — the dual's alif (s1), the masculine plural's wāw with the origin ḍarabtumū (s2), the feminine plural's nūn (s3), the tāʾ of the single addressee and the speaker alone in the past (s4), nā of the speaker with others (s5), the yāʾ of the single feminine addressee outside the past (s6).")
ADD_TR = (" Yirmi dördüncü bab (baskı s. 124-125): bâriz muttasıl zamir — tesniye elifi (s1), aslı darabtümû olan müzekker cem' vâvı (s2), müennes cem' nûnu (s3), mâzîde müfred muhâtab ve tek mütekellimin tâsı (s4), başkalarıyla mütekellimin nâsı (s5), mâzî dışında müfred muhâtabanın yâsı (s6).")
write_out(24, S, TITLE, ADD_EN, ADD_TR, "pp. 124-125", GLOSS_ADD, notes=(NOTE,),
          related=((K22, [K]), (K23, [K]), (FL, [K]), (LA, [K]), (LNH, [K]), (AMR, [K]), (JMS, [K]), (JMA, [K]), (MTH, [K])))
report(24, S, GLOSS_ADD, (NOTE,))
