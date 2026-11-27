# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 36: the ḥāl as a declarative SENTENCE — a binder is a must: the pronoun alone in the affirmed muḍāriʿ
# (جَاءَنِي زَيْدٌ يَرْكَبُ), the pronoun with the wāw or the wāw alone elsewhere, the wāw prevailing in the nominal clause (لَا يَرْكَبُ، وَلَا يَرْكَبُ،
# وَلَا يَرْكَبُ عَمْرٌو؛ رَكِبَ، وَرَكِبَ، وَرَكِبَ عَمْرٌو؛ هُوَ رَاكِبٌ، وَهُوَ رَاكِبٌ، وَعَمْرٌو رَاكِبٌ); the ḥāl multiplied (رَاكِبًا ضَاحِكًا); its governor
# dropped on a clue (رَاشِدًا مَهْدِيًّا to one who said أُرِيدُ السَّفَرَ). Print p. 134. The lithograph's line skips «أَوْ وَلَا يَرْكَبُ» in the
# negative-muḍāriʿ triplet; the text follows the Ottoman commentary (izhar-full-corrected l. 1325-1326), which prints all three.
#   python3 author_izhar_ch36.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"; AMS = "an-masdariyya"
NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; INS = "in-shartiyya"; JZ = "nawasib-wa-jawazim-al-mudari"; YM = "ya-al-mutakallim"; DF = "damir-fasl"
HL = "hal"; AW = "anwa-al-waw"; JS = "jumla-sifa"; AJ = "anwa-al-jumal"; IMP = "imperative-amr"
K = "al-hal-jumla-wa-rabituha"
K35 = "al-maful-maah-wal-hal"
TITLE = {"ar": "الْحَالُ جُمْلَةً: رَابِطُهَا وَتَعَدُّدُهَا وَحَذْفُ عَامِلِهَا", "en": "The ḥāl as a sentence: its binder, its multiplicity and the dropping of its governor", "tr": "Cümle olarak hâl: râbıtı, taaddüdü ve âmilinin hazfi"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def jaani(): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV, HL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")])
def zaydun(): return tok("زَيْدٌ", "zayd", "propn", [K, FL, HL], "فَاعِلٌ مَرْفُوعٌ — ذُو الْحَالِ.", "«Zayd» — the doer, owner of the ḥāl.", "«Zeyd» — fâil, hâl sahibi.")
def amrun(punct="،"): return tok("عَمْرٌو", "amr-name", "propn", [K, FL, HL], "فَاعِلٌ مَرْفُوعٌ — وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ؛ لَا ضَمِيرَ فِي الْجُمْلَةِ، فَالرَّابِطُ الْوَاوُ وَحْدَهُ.", "«ʿAmr» — no pronoun in the clause: the wāw alone binds.", "«Amr» — cümlede zamir yok: yalnız vâv bağlar.", punct=punct)

# ----------- s1 — a declarative sentence: a binder is a must
S.append({"id": "s1", "translation": {"en": "And it may be a declarative sentence, and then a binder in it is a must;", "tr": "Haber cümlesi de olur; o zaman içinde bir râbıt zorunludur;"},
 "tokens": [
  tok("وَتَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْوَاوُ عَاطِفَةٌ، وَتَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — الْحَالُ.", "«and it may be» — the ḥāl.", "«ve olur» — hâl.", segments=wa("تَكُونُ", "kana", "verb")),
  tok("جُمْلَةً", "jumla", "noun", [K, KN, AJ], "خَبَرُ تَكُونُ مَنْصُوبٌ.", "«a sentence»", "«bir cümle»"),
  tok("خَبَرِيَّةً", "khabariyya", "noun", [K, NA, NSB, AJ], "نَعْتٌ مَنْصُوبٌ — لَا إِنْشَائِيَّةً.", "«declarative» — not performative.", "«haber cümlesi» — inşâ değil.", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, AT, LN], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«so no»", "«o halde … yok»", segments=fa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, LN, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«escape» — it must.", "«çâre» — zorunlu."),
  tok("فِيهَا", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — فِي الْجُمْلَةِ.", "«in it» — in the sentence.", "«onda» — cümlede.", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("رَابِطٍ", "rabit", "noun", [K, HJ, IFA, HL], "مَجْرُورٌ بِمِنْ — مَا يَرْبِطُ الْجُمْلَةَ بِذِي الْحَالِ.", "«a binder» — what ties the clause to the owner.", "«bir râbıt» — cümleyi sahibine bağlayan.", punct="،"),
 ]})
# ----------- s2 — the pronoun alone in the affirmed muḍāriʿ
S.append({"id": "s2", "translation": {"en": "and that is the pronoun only, in the affirmed muḍāriʿ — as in «Zayd came to me riding»;", "tr": "o, müsbet muzâride yalnız zamirdir — «Zeyd bana biner hâlde geldi» gibi;"},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الرَّابِطُ.", "«and that is» — the binder.", "«o da» — râbıt.", segments=wa("هُوَ", "huwa", "pron")),
  tok("الضَّمِيرُ", "damir", "noun", [K, MK, HL], "خَبَرٌ مَرْفُوعٌ.", "«the pronoun» — the khabar.", "«zamir» — haber."),
  tok("فَقَطْ", "faqat", "adv", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ اسْمٌ بِمَعْنَى حَسْبُ مَبْنِيٌّ عَلَى السُّكُونِ.", "«only»", "«yalnız»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, HJ, MR], "مَجْرُورٌ بِفِي.", "«the muḍāriʿ»", "«muzâri»"),
  tok("الْمُثْبَتِ", "muthbat", "noun", [K, NA, IMF, F4], "نَعْتٌ مَجْرُورٌ — غَيْرِ الْمَنْفِيِّ.", "«affirmed» — not negated.", "«müsbet» — menfî olmayan.", punct="،"),
  nahw(),
  jaani(), zaydun(),
  tok("يَرْكَبُ", "rakiba", "verb", [K, MR, FL, HL, JS], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الرَّابِطُ؛ وَالْجُمْلَةُ حَالٌ.", "«riding» — its hidden pronoun binds; the clause is the ḥāl.", "«biner hâlde» — gizli zamiri bağlar; cümle hâldir.", punct="،"),
 ]})
# ----------- s3 — with the wāw, or the wāw alone, elsewhere; the nominal prefers the wāw
S.append({"id": "s3", "translation": {"en": "or with the wāw, or the wāw alone, in other than it — but the prevailing in the nominal sentence is the wāw;", "tr": "diğerlerinde ise vâv ile birlikte zamir ya da yalnız vâv — fakat isim cümlesinde galip olan vâv'dır;"},
 "tokens": [
  aw(),
  tok("مَعَ", "maa", "noun", [K, MF, ID, MK], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: الرَّابِطُ الضَّمِيرُ مَعَ الْوَاوِ.", "«with» — the pronoun together with the wāw.", "«ile» — zamir vâv ile birlikte."),
  tok("الْوَاوِ", "waw-letter", "noun", [K, ID, AW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَاوُ الْحَالِ.", "«the wāw» — of the ḥāl.", "«vâv» — hâl vâvı.", punct="،"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("الْوَاوُ", "waw-letter", "noun", [K, AT, MK, AW], "مُبْتَدَأٌ مَرْفُوعٌ — وَخَبَرُهُ مَحْذُوفٌ: الرَّابِطُ.", "«the wāw» — alone the binder.", "«vâv» — tek başına râbıt."),
  tok("وَحْدَهُ", "wahda", "noun", [K, "hal", ID], "حَالٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«alone»", "«yalnız»", segments=[seg("وَحْدَ", "wahda", "noun"), pr3ms()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِهِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — غَيْرِ الْمُضَارِعِ الْمُثْبَتِ.", "«other than it» — the negated muḍāriʿ, the māḍī, the nominal.", "«onun dışında» — menfî muzâri, mâzî, isim cümlesi.", punct="،", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("لٰكِنِ", "lakin", "part", [K, AT], "حَرْفُ اسْتِدْرَاكٍ.", "«but»", "«fakat»"),
  tok("الْغَالِبُ", "ghalib", "noun", [K, MK, IFA], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the prevailing»", "«galip olan»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الِاسْمِيَّةِ", "ismiyya", "noun", [K, HJ, AJ, NSB], "مَجْرُورٌ بِفِي — الْجُمْلَةِ الِاسْمِيَّةِ.", "«the nominal» — the nominal sentence.", "«isim cümlesinde»"),
  tok("الْوَاوُ", "waw-letter", "noun", [K, MK, AW], "خَبَرٌ مَرْفُوعٌ.", "«the wāw» — the khabar.", "«vâv» — haber.", punct="،"),
 ]})
# ----------- s4 — the negated muḍāriʿ triplet
S.append({"id": "s4", "translation": {"en": "as in «Zayd came to me not riding», or «and not riding», or «and ʿAmr not riding»;", "tr": "«Zeyd bana binmez hâlde geldi», veya «ve binmezken», veya «ve Amr binmezken» gibi;"},
 "tokens": [
  nahw(),
  jaani(), zaydun(),
  tok("لَا", "la-nafiya", "part", [K, LN, HL], "حَرْفُ نَفْيٍ.", "«not»", "«-mez»"),
  tok("يَرْكَبُ", "rakiba", "verb", [K, LN, MR, FL, HL, JS], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الرَّابِطُ الضَّمِيرُ وَحْدَهُ.", "«riding» — the pronoun alone binds.", "«biner» — yalnız zamir bağlar.", punct="،"),
  aw(),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN, HL, AW], "الْوَاوُ لِلْحَالِ، وَلَا نَافِيَةٌ.", "«and not» — the wāw of the ḥāl.", "«ve … -mez» — hâl vâvı.", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَرْكَبُ", "rakiba", "verb", [K, LN, MR, FL, HL, JS], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الرَّابِطُ الْوَاوُ مَعَ الضَّمِيرِ.", "«riding» — the wāw with the pronoun binds.", "«biner» — vâv ile zamir bağlar.", punct="،"),
  aw(),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN, HL, AW], "الْوَاوُ لِلْحَالِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَرْكَبُ", "rakiba", "verb", [K, LN, MR, FL, HL, JS], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«riding»", "«biner»"),
  amrun(),
 ]})
# ----------- s5 — the māḍī triplet
S.append({"id": "s5", "translation": {"en": "or «he rode», or «and he rode», or «and ʿAmr rode»;", "tr": "veya «bindi», veya «ve bindi», veya «ve Amr bindi»;"},
 "tokens": [
  aw(),
  tok("رَكِبَ", "rakiba", "verb", [K, FL, HL, JS], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — الرَّابِطُ الضَّمِيرُ وَحْدَهُ.", "«he rode» — the pronoun alone binds.", "«bindi» — yalnız zamir bağlar.", punct="،"),
  aw(),
  tok("وَرَكِبَ", "rakiba", "verb", [K, AT, FL, HL, JS, AW], "الْوَاوُ لِلْحَالِ، وَرَكِبَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — الرَّابِطُ الْوَاوُ مَعَ الضَّمِيرِ.", "«and he rode» — the wāw with the pronoun.", "«ve bindi» — vâv ile zamir.", punct="،", segments=wa("رَكِبَ", "rakiba", "verb")),
  aw(),
  tok("وَرَكِبَ", "rakiba", "verb", [K, AT, FL, HL, JS, AW], "الْوَاوُ لِلْحَالِ، وَرَكِبَ فِعْلٌ مَاضٍ.", "«and rode»", "«ve bindi»", segments=wa("رَكِبَ", "rakiba", "verb")),
  amrun(),
 ]})
# ----------- s6 — the nominal triplet
S.append({"id": "s6", "translation": {"en": "or «he riding», or «and he riding», or «and ʿAmr riding»;", "tr": "veya «o binici», veya «ve o binici», veya «ve Amr binici»;"},
 "tokens": [
  aw(),
  tok("هُوَ", "huwa", "pron", [K, MK, HL], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الرَّابِطُ الضَّمِيرُ وَحْدَهُ.", "«he» — the pronoun alone binds.", "«o» — yalnız zamir bağlar."),
  tok("رَاكِبٌ", "rakib", "noun", [K, MK, IFA, HL], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ حَالٌ.", "«riding» — the khabar; the clause the ḥāl.", "«binici» — haber; cümle hâl.", punct="،"),
  aw(),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK, HL, AW], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الرَّابِطُ الْوَاوُ مَعَ الضَّمِيرِ.", "«and he» — the wāw with the pronoun.", "«ve o» — vâv ile zamir.", segments=wa("هُوَ", "huwa", "pron")),
  tok("رَاكِبٌ", "rakib", "noun", [K, MK, IFA, HL], "خَبَرٌ مَرْفُوعٌ.", "«riding»", "«binici»", punct="،"),
  aw(),
  tok("وَعَمْرٌو", "amr-name", "propn", [K, AT, MK, HL, AW], "الْوَاوُ لِلْحَالِ، وَعَمْرٌو مُبْتَدَأٌ مَرْفُوعٌ — الرَّابِطُ الْوَاوُ وَحْدَهُ.", "«and ʿAmr» — the wāw alone binds.", "«ve Amr» — yalnız vâv bağlar.", segments=wa("عَمْرٌو", "amr-name", "propn")),
  tok("رَاكِبٌ", "rakib", "noun", [K, MK, IFA, HL], "خَبَرٌ مَرْفُوعٌ.", "«riding»", "«binici»", punct="،"),
 ]})
# ----------- s7 — the ḥāl multiplied
S.append({"id": "s7", "translation": {"en": "and the multiplication of the ḥāl is allowed — as in «Zayd came to me riding, laughing» —", "tr": "hâlin taaddüdü câizdir — «Zeyd bana binmiş, güler hâlde geldi» gibi —"},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("تَعَدُّدُ", "taaddud", "noun", [K, FL, ID, MSD, F5], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the multiplication of»", "«taaddüdü»"),
  tok("الْحَالِ", "hal", "noun", [K, ID, HL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ḥāl»", "«hâlin»", punct="،"),
  nahw(),
  jaani(), zaydun(),
  tok("رَاكِبًا", "rakib", "noun", [K, HL, IFA], "حَالٌ أَوَّلُ مَنْصُوبٌ.", "«riding» — the first ḥāl.", "«binmiş» — ilk hâl."),
  tok("ضَاحِكًا", "dahik-laughing", "noun", [K, HL, IFA], "حَالٌ ثَانٍ مَنْصُوبٌ.", "«laughing» — the second ḥāl.", "«güler hâlde» — ikinci hâl.", punct="،"),
 ]})
# ----------- s8 — its governor dropped on a clue
S.append({"id": "s8", "translation": {"en": "and the dropping of its governor by a clue — as in «rightly guided, well directed» to one who said «I intend the journey».", "tr": "âmilinin karîne ile hazfi de — «yolculuğa niyetliyim» diyene «doğru yolda, hidâyet üzere (git)» gibi."},
 "tokens": [
  tok("وَحَذْفُ", "hadhf", "noun", [K, AT, FL, ID, MSD, HT], "الْوَاوُ عَاطِفَةٌ، وَحَذْفُ مَعْطُوفٌ عَلَى تَعَدُّدُ مَرْفُوعٌ، مُضَافٌ.", "«and the dropping of»", "«ve … hazfi»", segments=wa("حَذْفُ", "hadhf", "noun")),
  tok("عَامِلِهِ", "amil", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  tok("بِقَرِينَةٍ", "qarina", "noun", [K, HJ, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَقَرِينَةٍ مَجْرُورٌ.", "«by a clue»", "«karîne ile»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("قَرِينَةٍ", "qarina", "noun")]),
  nahw(),
  tok("رَاشِدًا", "rashid-upright", "noun", [K, HL, IFA, HT], "لَفْظٌ مَحْكِيٌّ: حَالٌ مَنْصُوبٌ لِعَامِلٍ مَحْذُوفٍ: سِرْ.", "«rightly guided» — the ḥāl of a dropped «go».", "«doğru yolda» — hazfedilmiş «git»in hâli."),
  tok("مَهْدِيًّا", "mahdi", "noun", [K, HL, IMF, HT], "حَالٌ ثَانٍ مَنْصُوبٌ.", "«well directed» — the second ḥāl.", "«hidâyet üzere» — ikinci hâl."),
  tok("لِمَنْ", "man", "pron", [K, HJ, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who»", "«… diyene»", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man", "pron")]),
  tok("قَالَ", "qala", "verb", [K, FL, HV, MAW], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ مَنْ.", "«said»", "«diyen»", punct=":"),
  tok("أُرِيدُ", "arada", "verb", [K, MR, FL, HV, F4], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I intend»", "«niyetliyim»"),
  tok("السَّفَرَ", "safar", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the journey»", "«yolculuğa»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "rabit": G("rabit", "رَابِط", "ر ب ط", "noun", "a binder — the pronoun or wāw tying a clause to its owner", "râbıt — cümleyi sahibine bağlayan zamir veya vâv", 4, plural="رَوَابِط"),
 "khabariyya": G("khabariyya", "خَبَرِيَّة", "خ ب ر", "noun", "declarative (of a sentence) — stating, not performing", "haber cümlesi (sıfat) — inşâ değil, bildirme", 4),
 "dahik-laughing": G("dahik-laughing", "ضَاحِك", "ض ح ك", "noun", "laughing (active participle)", "gülen (ism-i fâil)", 2),
 "mahdi": G("mahdi", "مَهْدِيّ", "ه د ي", "noun", "rightly directed, guided (passive participle)", "hidâyete erdirilmiş, doğru yola iletilmiş (ism-i mef'ûl)", 3),
 "safar": G("safar", "سَفَر", "س ف ر", "noun", "a journey, travel", "yolculuk, sefer", 2, plural="أَسْفَار"),
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
print("izhar ch36 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "jaa", "rakiba", "arada", "qala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْحَالُ جُمْلَةً وَرَابِطُهَا، وَتَعَدُّدُ الْحَالِ، وَحَذْفُ عَامِلِهَا", "en": "The ḥāl as a sentence and its binder; the ḥāl multiplied; its governor dropped", "tr": "Cümle olarak hâl ve râbıtı; hâlin taaddüdü; âmilinin hazfi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: الحال جملةً", "الكافية لابن الحاجب — الحال", "شرح قطر الندى لابن هشام — الجملة الحالية ورابطها"],
 "amil": "the ḥāl may be a declarative sentence, and then a binder is a must: in the affirmed muḍāriʿ the pronoun alone (جَاءَنِي زَيْدٌ يَرْكَبُ — never وَيَرْكَبُ); elsewhere the pronoun with the wāw or the wāw alone, the wāw prevailing in the nominal clause (لَا يَرْكَبُ، وَلَا يَرْكَبُ، وَلَا يَرْكَبُ عَمْرٌو؛ رَكِبَ، وَرَكِبَ، وَرَكِبَ عَمْرٌو؛ هُوَ رَاكِبٌ، وَهُوَ رَاكِبٌ، وَعَمْرٌو رَاكِبٌ); the ḥāl may be multiplied (جَاءَنِي زَيْدٌ رَاكِبًا ضَاحِكًا) and its governor dropped by a clue (رَاشِدًا مَهْدِيًّا to one who said أُرِيدُ السَّفَرَ: the dropped governor سِرْ)",
 "question": {
  "en": ["May the ḥāl be a sentence? Yes, a declarative one — and then a binder tying the clause to the owner of the ḥāl is a must.",
         "What binds the affirmed muḍāriʿ? The pronoun only: جَاءَنِي زَيْدٌ يَرْكَبُ — the hidden هُوَ; the wāw is refused here (not وَيَرْكَبُ).",
         "And the other clauses? The pronoun with the wāw, or the wāw alone: the negated muḍāriʿ (لَا يَرْكَبُ، وَلَا يَرْكَبُ، وَلَا يَرْكَبُ عَمْرٌو), the māḍī (رَكِبَ، وَرَكِبَ، وَرَكِبَ عَمْرٌو), the nominal (هُوَ رَاكِبٌ، وَهُوَ رَاكِبٌ، وَعَمْرٌو رَاكِبٌ).",
         "Which binder prevails in the nominal clause? The wāw — وَهُوَ رَاكِبٌ is the usual; هُوَ رَاكِبٌ with the pronoun alone is rarer.",
         "May the ḥāl be multiplied? Yes: جَاءَنِي زَيْدٌ رَاكِبًا ضَاحِكًا — two ḥāls of one owner.",
         "May its governor be dropped? By a clue: رَاشِدًا مَهْدِيًّا to one who said أُرِيدُ السَّفَرَ — the governor سِرْ «go» is understood from the state of the speaker.",
         "What does the engine READ here? The DabtEngine reads the muḍāriʿ after a doer as its ḥāl-clause, the wāw-initial verb or pronoun after the doer as a ḥāl-clause with its wāw, the أَوْ-list of cited clauses word by word, the two tanwīn-fatḥ participles after the doer as ḥāls, and the cited رَاشِدًا مَهْدِيًّا without a governor as ḥāls."],
  "tr": ["Hâl cümle olabilir mi? Evet, haber cümlesi — o zaman cümleyi hâl sahibine bağlayan bir râbıt zorunludur.",
         "Müsbet muzâriyi ne bağlar? Yalnız zamir: câenî Zeydün yerkebu — gizli hüve; burada vâv reddedilir (ve-yerkebu değil).",
         "Diğer cümleler? Vâv ile zamir ya da yalnız vâv: menfî muzâri (lâ yerkebu, ve-lâ yerkebu, ve-lâ yerkebu Amrun), mâzî (rakibe, ve-rakibe, ve-rakibe Amrun), isim cümlesi (hüve râkibün, ve-hüve râkibün, ve-Amrun râkibün).",
         "İsim cümlesinde hangi râbıt galiptir? Vâv — ve-hüve râkibün olağandır; yalnız zamirli hüve râkibün daha seyrektir.",
         "Hâl taaddüd eder mi? Evet: câenî Zeydün râkiben dâhiken — bir sahibin iki hâli.",
         "Âmili hazfedilir mi? Karîne ile: ürîdü's-sefera diyene râşiden mehdiyyen — âmil sir «git» konuşanın hâlinden anlaşılır.",
         "Motor burada neyi OKUR? DabtEngine fâilden sonraki muzâriyi hâl cümlesi; fâilden sonraki vâv'lı fiil veya zamiri vâv'ıyla hâl cümlesi; ev ile sıralanan alıntı cümleleri kelime kelime; fâilden sonraki iki tenvîn-fethalı ism-i fâili hâl; âmilsiz alıntılanan râşiden mehdiyyen'i hâl okur."],
 },
 "plain": {"en": "A state-word may be a whole clause, but then a pronoun, an «and», or both must tie it to its owner. A plain present-tense clause takes the pronoun only («Zayd came to me riding»); other clauses take «and» too, noun-clauses usually «and». Two state-words may stack, and the verb may be left unsaid when obvious.",
           "tr": "Hâl bütün bir cümle olabilir, ama o zaman onu sahibine bağlayan bir şey gerekir: zamir, «ve» ya da ikisi. Düz bir muzâri cümlesi yalnız zamir alır («Zeyd bana biner hâlde geldi»); diğerleri «ve» de alır, isim cümleleri çoğunlukla «ve» alır. İki hâl üst üste gelebilir («binmiş, gülerek»), fiil belliyse söylenmeyebilir."},
 "explanation": {"en": "The ḥāl may be a declarative sentence, and then a binder is a must. In the affirmed muḍāriʿ the binder is the pronoun only (جَاءَنِي زَيْدٌ يَرْكَبُ — the hidden هُوَ; the wāw is not added, since the muḍāriʿ already stands for the participle). Elsewhere — the negated muḍāriʿ, the māḍī, the nominal clause — the binder is the pronoun with the wāw or the wāw alone, though in the nominal clause the wāw prevails: لَا يَرْكَبُ، وَلَا يَرْكَبُ، وَلَا يَرْكَبُ عَمْرٌو؛ رَكِبَ، وَرَكِبَ، وَرَكِبَ عَمْرٌو؛ هُوَ رَاكِبٌ، وَهُوَ رَاكِبٌ، وَعَمْرٌو رَاكِبٌ. The ḥāl may be multiplied (جَاءَنِي زَيْدٌ رَاكِبًا ضَاحِكًا), and its governor dropped by a clue: رَاشِدًا مَهْدِيًّا said to one who announced أُرِيدُ السَّفَرَ, the governor سِرْ understood. The lithograph's line skips the middle member of the negated-muḍāriʿ triplet; the Ottoman commentary prints all three, and the chapter follows it.",
                 "tr": "Hâl haber cümlesi olabilir; o zaman râbıt zorunludur. Müsbet muzâride râbıt yalnız zamirdir (câenî Zeydün yerkebu — gizli hüve; muzâri zaten ism-i fâilin yerini tuttuğundan vâv eklenmez). Diğerlerinde — menfî muzâri, mâzî, isim cümlesi — râbıt vâv ile zamir ya da yalnız vâv'dır; isim cümlesinde ise vâv galiptir: lâ yerkebu, ve-lâ yerkebu, ve-lâ yerkebu Amrun; rakibe, ve-rakibe, ve-rakibe Amrun; hüve râkibün, ve-hüve râkibün, ve-Amrun râkibün. Hâl taaddüd edebilir (câenî Zeydün râkiben dâhiken); âmili de karîne ile hazfedilir: ürîdü's-sefera diyene râşiden mehdiyyen; âmil sir anlaşılır. Taşbaskının satırı menfî muzâri üçlüsünün ortadaki üyesini atlar; Osmanlıca şerh üçünü de basar, bab onu izler."},
 "examples": [
  {"ar": "وَتَكُونُ جُمْلَةً خَبَرِيَّةً فَلَا بُدَّ فِيهَا مِنْ رَابِطٍ", "en": "the ḥāl-sentence needs a binder", "tr": "hâl cümlesi râbıt ister", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "جَاءَنِي زَيْدٌ يَرْكَبُ", "en": "the affirmed muḍāriʿ bound by the pronoun alone", "tr": "yalnız zamirle bağlı müsbet muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "لَا يَرْكَبُ، أَوْ وَلَا يَرْكَبُ، أَوْ وَلَا يَرْكَبُ عَمْرٌو", "en": "the negated muḍāriʿ triplet", "tr": "menfî muzâri üçlüsü", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "هُوَ رَاكِبٌ، أَوْ وَهُوَ رَاكِبٌ، أَوْ وَعَمْرٌو رَاكِبٌ", "en": "the nominal triplet, the wāw prevailing", "tr": "isim cümlesi üçlüsü, vâv galip", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "جَاءَنِي زَيْدٌ رَاكِبًا ضَاحِكًا", "en": "the ḥāl multiplied", "tr": "hâlin taaddüdü", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "رَاشِدًا مَهْدِيًّا لِمَنْ قَالَ أُرِيدُ السَّفَرَ", "en": "the governor dropped by a clue", "tr": "karîne ile hazfedilen âmil", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي زَيْدٌ وَيَرْكَبُ", "right": "جَاءَنِي زَيْدٌ يَرْكَبُ", "why": {"en": "the affirmed muḍāriʿ takes the pronoun alone as its binder — no wāw", "tr": "müsbet muzâri yalnız zamirle bağlanır — vâv yok"}},
  {"wrong": "جَاءَنِي زَيْدٌ عَمْرٌو رَاكِبٌ", "right": "جَاءَنِي زَيْدٌ وَعَمْرٌو رَاكِبٌ", "why": {"en": "a nominal clause with no pronoun of the owner needs the wāw to bind it", "tr": "sahibin zamirini taşımayan isim cümlesi vâv ile bağlanır"}},
  {"wrong": "رَاشِدٌ مَهْدِيٌّ (as the answer)", "right": "رَاشِدًا مَهْدِيًّا", "why": {"en": "the answer is the ḥāl of a dropped سِرْ and keeps its naṣb", "tr": "cevap hazfedilmiş sir'in hâlidir ve nasbını korur"}},
 ],
}
ADD_EN = (" Chapter 36 (print p. 134): the ḥāl as a declarative sentence with its binder (s1), the affirmed muḍāriʿ bound by the pronoun alone (s2), the wāw elsewhere (s3), the negated-muḍāriʿ, māḍī and nominal triplets (s4-s6), the ḥāl multiplied (s7), its governor dropped by a clue (s8).")
ADD_TR = (" Otuz altıncı bab (baskı s. 134): râbıtıyla haber cümlesi olarak hâl (s1), yalnız zamirle bağlı müsbet muzâri (s2), diğerlerinde vâv (s3), menfî muzâri, mâzî ve isim cümlesi üçlüleri (s4-s6), hâlin taaddüdü (s7), âmilinin karîne ile hazfi (s8).")
write_out(36, S, TITLE, ADD_EN, ADD_TR, "p. 134", GLOSS_ADD, notes=(NOTE,),
          related=((K35, [K]), (HL, [K]), (AW, [K]), (AJ, [K]), (JS, [K]), (HT, [K])))
report(36, S, GLOSS_ADD, (NOTE,))
