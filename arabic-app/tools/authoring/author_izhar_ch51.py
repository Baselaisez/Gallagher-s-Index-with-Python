# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 51: the FOURTH follower, the badal — the one intended by the attribution rather than its matbūʿ — in four kinds:
# badal of the whole (both true of one: جَاءَنِي زَيْدٌ أَخُوكَ), of the part (a part of the mubdal minhu: ضَرَبْتُ زَيْدًا رَأْسَهُ), of inclusion (a bond with
# something other than the two, so the soul waits after the first and longs for the second: سُلِبَ زَيْدٌ ثَوْبُهُ), of error (رَأَيْتُ رَجُلًا حِمَارًا — not in
# eloquent speech, which brings بَلْ instead); the nakira standing as whole-badal of a maʿrifa must be described (﴿بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ﴾ al-ʿAlaq 96:15-16);
# the apparent noun is whole-badal only of the third-person pronoun (ضَرَبْتُهُ زَيْدًا). The FIFTH, ʿaṭf al-bayān: a follower brought to clarify its matbūʿ
# without signifying a meaning in it (أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ). Then the sum of the maʿmūls: thirty. Print pp. 146–147.
# Orthography: the lithograph prints ثلثون (the old spelling without alif); the text gives it as ثَلَاثُونَ. The Ottoman commentary (izhar-full-corrected
# l. 1620-1648) is followed for the readings of the examples.
#   python3 author_izhar_ch51.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; TRF = "tarif-al-musnad-ilayh"; BD = "badal"; AB = "atf-bayan"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; FN = "five-nouns"; IQ = "al-iqtibas-wal-tadmin"; JMS = "jam-muannath-salim"; JDS = "jam-mudhakkar-salim"
K = "al-badal-wa-aqsamuh-wa-atf-al-bayan"
K50 = "al-tawkid-al-lafzi-wal-manawi"
TITLE = {"ar": "التَّابِعُ الرَّابِعُ: الْبَدَلُ وَأَقْسَامُهُ الْأَرْبَعَةُ، وَالْخَامِسُ: عَطْفُ الْبَيَانِ، وَمَجْمُوعُ الْمَعْمُولَاتِ", "en": "The fourth follower: the badal and its four kinds; the fifth: ʿaṭf al-bayān; the sum of the maʿmūls", "tr": "Dördüncü tâbi: bedel ve dört kısmı; beşincisi: atf-ı beyân; ma'mûllerin toplamı"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def nahwqawlihi(): return [tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as in»", "«… gibi»"), tok("قَوْلِهِ", "qawl", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]), tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ.", "«exalted be He»", "«Teâlâ»", punct=":")]
def inkana(): return [tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"), tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«it is»", "«olursa»")]
def badalu(form, lex2, en, tr, first=True, punct=None, grammar_extra=()):
    ar = ("مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ." if first else "الْوَاوُ عَاطِفَةٌ، وَبَدَلُ مَعْطُوفٌ عَلَى بَدَلِ الْكُلِّ مَرْفُوعٌ، مُضَافٌ.")
    segs = None if first else wa("بَدَلُ", "badal", "noun")
    return tok(form, "badal", "noun", [K, BD, TW, ID] + ([AT] if not first else []) + list(grammar_extra), ar, en, tr, punct=punct, segments=segs)

# ----------- s1 — the fourth: the badal, its definition, four kinds
S.append({"id": "s1", "translation": {"en": "And the fourth is the badal, and it is the one intended by the attribution rather than it [the matbūʿ]; and its kinds are four:", "tr": "Dördüncüsü bedeldir; o, nisbet bakımından metbûu değil kendisi kastedilen tâbidir; kısımları dörttür:"},
 "tokens": [
  tok("وَالرَّابِعُ", "rabi-fourth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالرَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fourth»", "«dördüncüsü»", segments=wa("الرَّابِعُ", "rabi-fourth", "noun")),
  tok("الْبَدَلُ", "badal", "noun", [K, MK, BD, TW], "خَبَرٌ مَرْفُوعٌ.", "«the badal» — the khabar.", "«bedel» — haber.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمَقْصُودُ", "maqsud", "noun", [K, MK, IMF, BD], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«the one intended» — the khabar, a passive participle.", "«kastedilen» — haber, ism-i mef'ûl."),
  tok("بِالنِّسْبَةِ", "nisba", "noun", [K, HJ, BD], "الْبَاءُ حَرْفُ جَرٍّ، وَالنِّسْبَةِ مَجْرُورٌ — مُتَعَلِّقٌ بِالْمَقْصُودِ.", "«by the attribution»", "«nisbet bakımından»", segments=[seg("بِ", "bi", "prep"), seg("النِّسْبَةِ", "nisba", "noun")]),
  tok("دُونَهُ", "duna", "noun", [K, MF, ID, BD], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ دُونَ الْمَتْبُوعِ.", "«rather than it» — i.e. not the matbūʿ.", "«onun değil» — yani metbû değil.", punct="،", segments=[seg("دُونَ", "duna", "noun"), pr3ms()]),
  tok("وَأَقْسَامُهُ", "qism", "noun", [K, AT, MK, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَأَقْسَامُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its kinds»", "«kısımları»", segments=[seg("وَ", "wa", "conj"), seg("أَقْسَامُ", "qism", "noun"), pr3ms()]),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«four»", "«dörttür»", punct=":"),
 ]})
# ----------- s2 — badal of the whole
S.append({"id": "s2", "translation": {"en": "the badal of the whole from the whole, if the two are true of one — as in «there came to me Zayd, your brother»;", "tr": "külden küle bedel, ikisi tek bir şey hakkında doğru olursa — «bana Zeyd, kardeşin geldi» gibi;"},
 "tokens": [
  badalu("بَدَلُ", None, "«the badal of»", "«bedeli»"),
  tok("الْكُلِّ", "kull", "noun", [K, ID, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the whole»", "«külün»"),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْكُلِّ", "kull", "noun", [K, HJ, BD], "مَجْرُورٌ بِمِنْ.", "«the whole»", "«kül»"),
  *inkana(),
  tok("صَدَقَا", "sadaqa-verb", "verb", [K, FL, MTH, BD], "فِعْلٌ مَاضٍ، وَالْأَلِفُ فَاعِلٌ — أَيِ الْبَدَلُ وَالْمُبْدَلُ مِنْهُ.", "«the two are true» — the badal and the mubdal minhu.", "«ikisi doğru olursa» — bedel ile mübdelün minh.", segments=[seg("صَدَقَ", "sadaqa-verb", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«üzerine»"),
  tok("وَاحِدٍ", "wahid", "noun", [K, HJ, BD], "مَجْرُورٌ بِعَلَى — عَلَى ذَاتٍ وَاحِدَةٍ.", "«one» — one and the same person.", "«bir» — aynı zat.", punct="،"),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL, BD], "فَاعِلٌ مَرْفُوعٌ — الْمُبْدَلُ مِنْهُ.", "«Zayd» — the mubdal minhu.", "«Zeyd» — mübdelün minh."),
  tok("أَخُوكَ", "akh", "noun", [K, BD, TW, FN, ID], "بَدَلُ الْكُلِّ مِنْ زَيْدٍ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your brother» — badal of the whole, rafʿ by the wāw.", "«kardeşin» — kül bedeli, vâv ile merfû.", punct="،", segments=[seg("أَخُو", "akh", "noun"), seg("كَ", "pron-2ms", "pron")]),
 ]})
# ----------- s3 — badal of the part
S.append({"id": "s3", "translation": {"en": "and the badal of the part from the whole, if it is a part of the mubdal minhu — as in «I struck Zayd, his head»;", "tr": "ba'zdan küle bedel, mübdelün minhin bir cüzü olursa — «Zeyd'i, başını dövdüm» gibi;"},
 "tokens": [
  badalu("وَبَدَلُ", None, "«and the badal of»", "«ve bedeli»", first=False),
  tok("الْبَعْضِ", "bad", "noun", [K, ID, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the part»", "«ba'zın»"),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْكُلِّ", "kull", "noun", [K, HJ, BD], "مَجْرُورٌ بِمِنْ.", "«the whole»", "«kül»"),
  *inkana(),
  tok("جُزْءًا", "juz", "noun", [K, KN, BD], "خَبَرُ كَانَ مَنْصُوبٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — الْبَدَلُ.", "«a part» — kāna's khabar; its ism the hidden «it», the badal.", "«bir cüz» — kâne'nin haberi; ismi gizli «o», bedel."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("الْمُبْدَلِ", "mubdal", "noun", [K, HJ, IMF, F4, BD], "مَجْرُورٌ بِمِنْ — اسْمُ مَفْعُولٍ مِنْ أَبْدَلَ.", "«the one substituted» — the passive participle of abdala.", "«mübdel» — ebdele'nin ism-i mef'ûlü."),
  tok("مِنْهُ", "min", "prep", [K, HJ, BD], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ فَاعِلِ الْمُبْدَلِ: الْمُبْدَلُ مِنْهُ.", "«from» — the mubdal minhu.", "«-den» — mübdelün minh.", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  nahw(),
  tok("ضَرَبْتُ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("زَيْدًا", "zayd", "propn", [K, MB, BD], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُبْدَلُ مِنْهُ.", "«Zayd» — the mubdal minhu.", "«Zeyd'i» — mübdelün minh."),
  tok("رَأْسَهُ", "ras", "noun", [K, BD, TW, ID], "بَدَلُ الْبَعْضِ مِنْ زَيْدٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الرَّابِطُ.", "«his head» — badal of the part; the pronoun is the link.", "«başını» — ba'z bedeli; zamir râbıt.", punct="،", segments=[seg("رَأْسَ", "ras", "noun"), pr3ms()]),
 ]})
# ----------- s4 — badal of inclusion
S.append({"id": "s4", "translation": {"en": "and the badal of inclusion, if between the two there is a bond with something other than them, such that the soul waits after the mention of the first and longs for the second — as in «Zayd was robbed, his garment»;", "tr": "iştimâl bedeli, ikisi arasında kendilerinden başka bir şeyle bir bağ olursa, öyle ki nefis ilkinin zikrinden sonra bekler ve ikincisini özler — «Zeyd soyuldu, elbisesi» gibi;"},
 "tokens": [
  badalu("وَبَدَلُ", None, "«and the badal of»", "«ve bedeli»", first=False),
  tok("الِاشْتِمَالِ", "ishtimal", "noun", [K, ID, MSD, F8, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اشْتَمَلَ.", "«inclusion» — the maṣdar of ishtamala.", "«iştimâl» — iştemele'nin mastarı."),
  *inkana(),
  tok("بَيْنَهُمَا", "bayna", "noun", [K, MF, ID, KN], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — خَبَرُ كَانَ مُقَدَّمٌ.", "«between the two» — kāna's khabar, put first.", "«ikisi arasında» — kâne'nin öne alınmış haberi.", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("تَعَلُّقٌ", "taalluq", "noun", [K, KN, MSD, F5], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a bond» — kāna's ism, put after.", "«bir bağ» — kâne'nin sona bırakılmış ismi."),
  tok("بِغَيْرِهِمَا", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«with something other than them»", "«kendilerinden başkasıyla»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("بِحَيْثُ", "haythu", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَحَيْثُ ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ.", "«such that»", "«öyle ki»", segments=[seg("بِ", "bi", "prep"), seg("حَيْثُ", "haythu", "noun")]),
  tok("تَنْتَظِرُ", "intazara", "verb", [K, MR, F8], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«waits»", "«bekler»"),
  tok("النَّفْسُ", "nafs", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«the soul»", "«nefis»"),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("ذِكْرِ", "dhikr", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the mention of»", "«zikrinden»"),
  tok("الْأَوَّلِ", "awwal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the first»", "«ilkinin»"),
  tok("وَتَتَشَوَّقُ", "tashawwaqa", "verb", [K, AT, MR, F5], "الْوَاوُ عَاطِفَةٌ، وَتَتَشَوَّقُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and longs»", "«ve özler»", segments=wa("تَتَشَوَّقُ", "tashawwaqa", "verb")),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-e»"),
  tok("الثَّانِي", "thani", "noun", [K, HJ, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — اسْمٌ مَنْقُوصٌ.", "«the second»", "«ikincisini»", punct="،"),
  nahw(),
  tok("سُلِبَ", "salaba", "verb", [K, NF], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was robbed»", "«soyuldu»"),
  tok("زَيْدٌ", "zayd", "propn", [K, NF, BD], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الْمُبْدَلُ مِنْهُ.", "«Zayd» — the mubdal minhu.", "«Zeyd» — mübdelün minh."),
  tok("ثَوْبُهُ", "thawb", "noun", [K, BD, TW, ID], "بَدَلُ الِاشْتِمَالِ مِنْ زَيْدٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his garment» — badal of inclusion.", "«elbisesi» — iştimâl bedeli.", punct="،", segments=[seg("ثَوْبُ", "thawb", "noun"), pr3ms()]),
 ]})
# ----------- s5 — badal of error
S.append({"id": "s5", "translation": {"en": "and the badal of error, if the mention of the mubdal minhu was an error — as in «I saw a man — a donkey»; and it does not occur in the speech of the eloquent; rather «bal» is brought instead of it.", "tr": "galat bedeli, mübdelün minhin zikri yanlış olmuşsa — «bir adam gördüm — eşek» gibi; fasihlerin sözünde bulunmaz, onun yerine «bel» getirilir."},
 "tokens": [
  badalu("وَبَدَلُ", None, "«and the badal of»", "«ve bedeli»", first=False),
  tok("الْغَلَطِ", "ghalat", "noun", [K, ID, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«error»", "«galatın»"),
  *inkana(),
  tok("ذِكْرُ", "dhikr", "noun", [K, KN, ID, MSD], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ.", "«the mention of»", "«zikri»"),
  tok("الْمُبْدَلِ", "mubdal", "noun", [K, ID, IMF, F4, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the one substituted»", "«mübdelün»"),
  tok("مِنْهُ", "min", "prep", [K, HJ, BD], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ فَاعِلِ الْمُبْدَلِ.", "«from»", "«minh»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("غَلَطًا", "ghalat", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«an error» — kāna's khabar.", "«yanlış» — kâne'nin haberi.", punct="،"),
  nahw(),
  tok("رَأَيْتُ", "raa", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw»", "«gördüm»", segments=[seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("رَجُلًا", "rajul", "noun", [K, MB, BD], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُبْدَلُ مِنْهُ، ذُكِرَ غَلَطًا.", "«a man» — the mubdal minhu, said by mistake.", "«bir adam» — yanlışlıkla söylenen mübdelün minh."),
  tok("حِمَارًا", "himar", "noun", [K, BD, TW], "بَدَلُ الْغَلَطِ مِنْ رَجُلٍ مَنْصُوبٌ.", "«a donkey» — badal of error.", "«eşek» — galat bedeli.", punct="،"),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and it does not»", "«ve … -maz»", segments=wa("لَا", "la", "part")),
  tok("يَقَعُ", "waqaa", "verb", [K, MR, LN, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — بَدَلُ الْغَلَطِ.", "«occur» — the hidden doer: the badal of error.", "«bulunmaz» — gizli fâil: galat bedeli."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("كَلَامِ", "kalam", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the speech of»", "«sözünde»"),
  tok("الْفُصَحَاءِ", "fasih", "noun", [K, ID, JT, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ — جَمْعُ فَصِيحٍ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«the eloquent» — plural of faṣīḥ, a diptote in jarr by kasra through the iḍāfa.", "«fasihlerin» — fasîh'in çoğulu, izafetle kesreli."),
  tok("بَلْ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ.", "«rather»", "«bilakis»"),
  tok("يُورَدُ", "awrada", "verb", [K, MR, NF, F4], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — مِنْ أَوْرَدَ.", "«is brought» — passive of awrada.", "«getirilir» — evrede'nin meçhûlü."),
  tok("دُونَهُ", "duna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ بَدَلَهُ.", "«instead of it»", "«onun yerine»", segments=[seg("دُونَ", "duna", "noun"), pr3ms()]),
  tok("بَلْ", "bal", "part", [K, NF], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلِ يُورَدُ.", "«bal» — the cited word, deputy doer of «is brought».", "«bel» — alıntı lafız, yûradü'nün nâib-i fâili.", punct="."),
 ]})
# ----------- s6 — the nakira described; the apparent noun from the pronoun
S.append({"id": "s6", "translation": {"en": "And it is obligatory to describe the nakira [standing] from the maʿrifa as badal of the whole — as in His saying, exalted be He: «by the forelock — a lying forelock»; and the apparent noun is not made badal of the whole from the pronoun except from the third person — as in «I struck him, Zayd».", "tr": "Ma'rifeden kül bedeli olan nekreyi vasıflamak vâciptir — Allah Teâlâ'nın «perçeminden — yalancı bir perçem» sözü gibi; zâhir isim zamirden ancak gâibden kül bedeli yapılır — «onu dövdüm, Zeyd'i» gibi."},
 "tokens": [
  tok("وَيَجِبُ", "wajaba", "verb", [K, AT, MR, "mithal-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is obligatory»", "«ve vâciptir»", segments=wa("يَجِبُ", "wajaba", "verb")),
  tok("وَصْفُ", "wasf", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«to describe» — the doer, a maṣdar.", "«vasıflamak» — fâil, mastar."),
  tok("النَّكِرَةِ", "nakira", "noun", [K, ID, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَصْدَرُ مُضَافٌ إِلَى مَفْعُولِهِ.", "«the nakira» — the maṣdar annexed to its object.", "«nekreyi» — mastar mef'ûlüne muzâf."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْمَعْرِفَةِ", "marifa", "noun", [K, HJ, BD], "مَجْرُورٌ بِمِنْ — الْمُبْدَلُ مِنْهُ.", "«the maʿrifa» — the mubdal minhu.", "«ma'rifeden» — mübdelün minh."),
  tok("بَدَلَ", "badal", "noun", [K, "hal", ID, BD, TW], "حَالٌ مَنْصُوبٌ مِنَ النَّكِرَةِ، مُضَافٌ — أَيْ حَالَ كَوْنِهَا بَدَلَ الْكُلِّ.", "«as badal of» — a ḥāl of the nakira.", "«bedeli olarak» — nekrenin hâli."),
  tok("الْكُلِّ", "kull", "noun", [K, ID, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the whole»", "«kül»", punct="،"),
  *nahwqawlihi(),
  tok("بِالنَّاصِيَةِ", "nasiya-forelock", "noun", [K, HJ, IQ, BD], "الْبَاءُ حَرْفُ جَرٍّ، وَالنَّاصِيَةِ مَجْرُورٌ — الْمُبْدَلُ مِنْهُ، مَعْرِفَةٌ؛ ﴿الْعَلَق ٩٦: ١٥-١٦﴾.", "«by the forelock» — the mubdal minhu, a maʿrifa (al-ʿAlaq 96:15-16).", "«perçeminden» — mübdelün minh, ma'rife (Alak 96:15-16).", segments=[seg("بِ", "bi", "prep"), seg("النَّاصِيَةِ", "nasiya-forelock", "noun")]),
  tok("نَاصِيَةٍ", "nasiya-forelock", "noun", [K, BD, TW, IQ], "بَدَلُ الْكُلِّ مِنَ النَّاصِيَةِ مَجْرُورٌ — نَكِرَةٌ مِنْ مَعْرِفَةٍ، فَوَجَبَ وَصْفُهَا.", "«a forelock» — the nakira as whole-badal of a maʿrifa; so it must be described.", "«bir perçem» — ma'rifeden kül bedeli olan nekre; vasfı vâcip."),
  tok("كَاذِبَةٍ", "kadhib-liar", "noun", [K, NA, IFA, IQ], "نَعْتٌ لِنَاصِيَةٍ مَجْرُورٌ — الْوَصْفُ الْوَاجِبُ.", "«lying» — the required description.", "«yalancı» — vâcip olan vasıf.", punct="،"),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -maz»", segments=wa("لَا", "la", "part")),
  tok("يُبْدَلُ", "abdala", "verb", [K, MR, NF, F4, LN, BD], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — مِنْ أَبْدَلَ.", "«is made badal» — passive of abdala.", "«bedel yapılır» — ebdele'nin meçhûlü."),
  tok("الظَّاهِرُ", "zahir", "noun", [K, NF, IFA, BD], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الِاسْمُ الظَّاهِرُ.", "«the apparent [noun]» — the deputy doer.", "«zâhir isim» — nâib-i fâil."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْمُضْمَرِ", "mudmar", "noun", [K, HJ, IMF, F4, BD], "مَجْرُورٌ بِمِنْ — الضَّمِيرُ.", "«the pronoun»", "«zamirden»"),
  tok("بَدَلَ", "badal", "noun", [K, "hal", ID, BD], "حَالٌ مَنْصُوبٌ، مُضَافٌ.", "«as badal of»", "«bedeli olarak»"),
  tok("الْكُلِّ", "kull", "noun", [K, ID, BD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the whole»", "«kül»"),
  tok("إِلَّا", "illa", "part", [K, "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except»", "«ancak»"),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْغَائِبِ", "ghaib", "noun", [K, HJ, IFA, BD], "مَجْرُورٌ بِمِنْ — ضَمِيرُ الْغَائِبِ.", "«the third person» — the absent one's pronoun.", "«gâibden» — gâib zamiri.", punct="،"),
  nahw(),
  tok("ضَرَبْتُهُ", "daraba", "verb", [K, FL, MB, BD], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْمُبْدَلُ مِنْهُ.", "«I struck him» — the pronoun is the mubdal minhu.", "«onu dövdüm» — zamir mübdelün minh.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron"), pr3ms()]),
  tok("زَيْدًا", "zayd", "propn", [K, BD, TW], "بَدَلُ الْكُلِّ مِنَ الْهَاءِ مَنْصُوبٌ — الظَّاهِرُ مِنَ الْمُضْمَرِ الْغَائِبِ.", "«Zayd» — the apparent noun as badal of the third-person pronoun.", "«Zeyd'i» — gâib zamirinden bedel olan zâhir isim.", punct="."),
 ]})
# ----------- s7 — the fifth: ʿaṭf al-bayān
S.append({"id": "s7", "translation": {"en": "And the fifth is ʿaṭf al-bayān, and it is a follower brought to clarify its matbūʿ, and it does not signify a meaning in it — as in «Abū Ḥafṣ, ʿUmar, swore by God».", "tr": "Beşincisi atf-ı beyândır; o, metbûunu açıklamak için getirilen ve onda bir manaya delâlet etmeyen tâbidir — «Ebû Hafs Ömer Allah'a yemin etti» gibi."},
 "tokens": [
  tok("وَالْخَامِسُ", "khamis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَامِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fifth»", "«beşincisi»", segments=wa("الْخَامِسُ", "khamis", "noun")),
  tok("عَطْفُ", "atf", "noun", [K, MK, ID, AB, TW], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«ʿaṭf of» — the khabar.", "«atf-ı» — haber."),
  tok("الْبَيَانِ", "bayan", "noun", [K, ID, AB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«clarification»", "«beyân»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("تَابِعٌ", "tabi", "noun", [K, MK, IFA, TW, AB], "خَبَرٌ مَرْفُوعٌ.", "«a follower»", "«bir tâbidir»"),
  tok("جِيءَ", "jaa", "verb", [K, NA, NF, HV], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ لِتَابِعٍ.", "«brought» — passive; the clause describes «follower».", "«getirilmiş» — meçhûl; cümle tâbi'in sıfatı."),
  tok("بِهِ", "bi", "prep", [K, HJ, NF], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ الْفَاعِلِ.", "«with it» — the deputy doer.", "«onunla» — nâib-i fâil.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("لِإِيضَاحِ", "idah", "noun", [K, HJ, ID, MSD, F4], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَإِيضَاحِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ أَوْضَحَ.", "«to clarify» — the maṣdar of awḍaḥa.", "«açıklamak için» — evdaha'nın mastarı.", segments=[seg("لِ", "li", "prep"), seg("إِيضَاحِ", "idah", "noun")]),
  tok("مَتْبُوعِهِ", "matbu", "noun", [K, ID, IMF, TW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its matbūʿ»", "«metbûunu»", segments=[seg("مَتْبُوعِ", "matbu", "noun"), pr3msi()]),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -mez»", segments=wa("لَا", "la", "part")),
  tok("يَدُلُّ", "dalla", "verb", [K, MR, LN, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — مَعْطُوفٌ عَلَى جِيءَ بِهِ.", "«signify» — joined to the describing clause.", "«delâlet etmez» — sıfat cümlesine atfedilmiş."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«a»", "«-e»"),
  tok("مَعْنًى", "mana", "noun", [K, HJ, MQ], "مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ — اسْمٌ مَقْصُورٌ مُنَوَّنٌ.", "«meaning» — a maqṣūr noun with tanwīn.", "«mana» — tenvinli maksûr isim."),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — فِي الْمَتْبُوعِ.", "«in it» — in the matbūʿ.", "«onda» — metbûda.", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  nahw(),
  tok("أَقْسَمَ", "aqsama", "verb", [K, FL, F4], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ.", "«swore»", "«yemin etti»"),
  tok("بِاللهِ", "allah", "propn", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — الْمُقْسَمُ بِهِ.", "«by God»", "«Allah'a»", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  tok("أَبُو", "ab", "noun", [K, FL, FN, ID], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ — الْكُنْيَةُ.", "«Abū» — the doer, rafʿ by the wāw.", "«Ebû» — fâil, vâv ile merfû."),
  tok("حَفْصٍ", "hafs", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Ḥafṣ»", "«Hafs»"),
  tok("عُمَرُ", "umar", "propn", [K, AB, TW, MMS], "عَطْفُ بَيَانٍ لِأَبِي حَفْصٍ مَرْفُوعٌ — يُوَضِّحُ الْكُنْيَةَ بِالِاسْمِ؛ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«ʿUmar» — ʿaṭf al-bayān, clarifying the kunya by the name; a diptote.", "«Ömer» — atf-ı beyân, künyeyi adla açıklar; gayr-ı munsarıf.", punct="."),
 ]})
# ----------- s8 — the sum
S.append({"id": "s8", "translation": {"en": "So the sum of what we have mentioned of the maʿmūls is thirty.", "tr": "Böylece ma'mûllerden zikrettiklerimizin toplamı otuzdur."},
 "tokens": [
  tok("فَمَجْمُوعُ", "majmu", "noun", [K, AT, MK, ID, IMF], "الْفَاءُ لِلتَّفْرِيعِ، وَمَجْمُوعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«so the sum of»", "«böylece toplamı»", segments=fa("مَجْمُوعُ", "majmu", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MAW, ID], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what»", "«-ler»"),
  tok("ذَكَرْنَا", "dhakara", "verb", [K, FL, MAW], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ — صِلَةُ مَا، وَالْعَائِدُ مَحْذُوفٌ.", "«we have mentioned» — the ṣila; the returning pronoun dropped.", "«zikrettiğimiz» — sıla; âid zamir hazfedilmiş.", segments=[seg("ذَكَرْ", "dhakara", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of»", "«-den»"),
  tok("الْمَعْمُولَاتِ", "mamul", "noun", [K, HJ, IMF, JMS], "مَجْرُورٌ بِمِنْ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the maʿmūls»", "«ma'mûllerden»"),
  tok("ثَلَاثُونَ", "thalathun", "noun", [K, MK, JDS], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ؛ الطَّبْعُ: ثلثون.", "«thirty» — rafʿ by the wāw; the print spells it ثلثون.", "«otuz» — vâv ile merfû; baskıda ثلثون.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "mubdal": G("mubdal", "مُبْدَل", "ب د ل", "noun", "substituted — the mubdal minhu is the word the badal stands for", "mübdel — mübdelün minh, bedelin yerine geçtiği kelime", 3),
 "abdala": G("abdala", "أَبْدَلَ", "ب د ل", "verb", "to substitute, to make a badal (form IV)", "bedel yapmak, yerine koymak (IV. bab)", 3, form="IV"),
 "tashawwaqa": G("tashawwaqa", "تَشَوَّقَ", "ش و ق", "verb", "to long for, to yearn (form V)", "özlemek, iştiyak duymak (V. bab)", 3, form="V"),
 "awrada": G("awrada", "أَوْرَدَ", "و ر د", "verb", "to bring forward, to adduce (form IV)", "getirmek, îrâd etmek (IV. bab)", 3, form="IV"),
 "idah": G("idah", "إِيضَاح", "و ض ح", "noun", "clarification — the maṣdar of awḍaḥa", "îzâh, açıklama — evdaha'nın mastarı", 3),
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
put_morph(mo, "abdala", {"bab": "بَابُ الْإِفْعَالِ", "wazn": "أَفْعَلَ يُفْعِلُ", "masdar": "إِبْدَال", "ismFail": "مُبْدِل",
 "mazi": ["أَبْدَلَ", "أَبْدَلَا", "أَبْدَلُوا", "أَبْدَلَتْ", "أَبْدَلَتَا", "أَبْدَلْنَ", "أَبْدَلْتَ", "أَبْدَلْتُمَا", "أَبْدَلْتُمْ", "أَبْدَلْتِ", "أَبْدَلْتُمَا", "أَبْدَلْتُنَّ", "أَبْدَلْتُ", "أَبْدَلْنَا"],
 "mudari": ["يُبْدِلُ", "يُبْدِلَانِ", "يُبْدِلُونَ", "تُبْدِلُ", "تُبْدِلَانِ", "يُبْدِلْنَ", "تُبْدِلُ", "تُبْدِلَانِ", "تُبْدِلُونَ", "تُبْدِلِينَ", "تُبْدِلَانِ", "تُبْدِلْنَ", "أُبْدِلُ", "نُبْدِلُ"],
 "amr": ["أَبْدِلْ", "أَبْدِلَا", "أَبْدِلُوا", "أَبْدِلِي", "أَبْدِلَا", "أَبْدِلْنَ"], "mansub": "يُبْدِلَ", "majzum": "يُبْدِلْ", "majzum2": "تُبْدِلْ",
 "note": "أَبْدَلَ الشَّيْءَ مِنَ الشَّيْءِ يُبْدِلُهُ إِبْدَالًا: جَعَلَهُ بَدَلًا مِنْهُ — مِنْ بَابِ الْإِفْعَالِ، صَحِيحٌ، مُتَعَدٍّ؛ مَجْهُولُهُ يُبْدَلُ."})
put_morph(mo, "tashawwaqa", {"bab": "بَابُ التَّفَعُّلِ — أَجْوَفُ", "wazn": "تَفَعَّلَ يَتَفَعَّلُ", "masdar": "تَشَوُّق", "ismFail": "مُتَشَوِّق",
 "mazi": ["تَشَوَّقَ", "تَشَوَّقَا", "تَشَوَّقُوا", "تَشَوَّقَتْ", "تَشَوَّقَتَا", "تَشَوَّقْنَ", "تَشَوَّقْتَ", "تَشَوَّقْتُمَا", "تَشَوَّقْتُمْ", "تَشَوَّقْتِ", "تَشَوَّقْتُمَا", "تَشَوَّقْتُنَّ", "تَشَوَّقْتُ", "تَشَوَّقْنَا"],
 "mudari": ["يَتَشَوَّقُ", "يَتَشَوَّقَانِ", "يَتَشَوَّقُونَ", "تَتَشَوَّقُ", "تَتَشَوَّقَانِ", "يَتَشَوَّقْنَ", "تَتَشَوَّقُ", "تَتَشَوَّقَانِ", "تَتَشَوَّقُونَ", "تَتَشَوَّقِينَ", "تَتَشَوَّقَانِ", "تَتَشَوَّقْنَ", "أَتَشَوَّقُ", "نَتَشَوَّقُ"],
 "amr": ["تَشَوَّقْ", "تَشَوَّقَا", "تَشَوَّقُوا", "تَشَوَّقِي", "تَشَوَّقَا", "تَشَوَّقْنَ"], "mansub": "يَتَشَوَّقَ", "majzum": "يَتَشَوَّقْ", "majzum2": "تَتَشَوَّقْ",
 "note": "تَشَوَّقَ إِلَى الشَّيْءِ يَتَشَوَّقُ تَشَوُّقًا: اشْتَاقَ إِلَيْهِ — مِنْ بَابِ التَّفَعُّلِ؛ الْوَاوُ الْمُشَدَّدَةُ تَصِحُّ فِي هٰذَا الْبَابِ، لَازِمٌ يَتَعَدَّى بِإِلَى."})
put_morph(mo, "awrada", {"bab": "بَابُ الْإِفْعَالِ — مِثَالٌ وَاوِيٌّ", "wazn": "أَفْعَلَ يُفْعِلُ", "masdar": "إِيرَاد", "ismFail": "مُورِد",
 "mazi": ["أَوْرَدَ", "أَوْرَدَا", "أَوْرَدُوا", "أَوْرَدَتْ", "أَوْرَدَتَا", "أَوْرَدْنَ", "أَوْرَدْتَ", "أَوْرَدْتُمَا", "أَوْرَدْتُمْ", "أَوْرَدْتِ", "أَوْرَدْتُمَا", "أَوْرَدْتُنَّ", "أَوْرَدْتُ", "أَوْرَدْنَا"],
 "mudari": ["يُورِدُ", "يُورِدَانِ", "يُورِدُونَ", "تُورِدُ", "تُورِدَانِ", "يُورِدْنَ", "تُورِدُ", "تُورِدَانِ", "تُورِدُونَ", "تُورِدِينَ", "تُورِدَانِ", "تُورِدْنَ", "أُورِدُ", "نُورِدُ"],
 "amr": ["أَوْرِدْ", "أَوْرِدَا", "أَوْرِدُوا", "أَوْرِدِي", "أَوْرِدَا", "أَوْرِدْنَ"], "mansub": "يُورِدَ", "majzum": "يُورِدْ", "majzum2": "تُورِدْ",
 "note": "أَوْرَدَ الشَّيْءَ يُورِدُهُ إِيرَادًا: أَحْضَرَهُ وَذَكَرَهُ — مِنْ بَابِ الْإِفْعَالِ، مِثَالٌ وَاوِيٌّ تَصِحُّ وَاوُهُ بَعْدَ الضَّمَّةِ؛ مَجْهُولُهُ يُورَدُ، وَمَصْدَرُهُ إِيرَادٌ بِقَلْبِ الْوَاوِ يَاءً بَعْدَ الْكَسْرَةِ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch51 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("sadaqa-verb", "intazara", "salaba", "aqsama", "jaa", "daraba", "raa", "waqaa", "wajaba", "dalla", "dhakara") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْبَدَلُ: بَدَلُ الْكُلِّ وَالْبَعْضِ وَالِاشْتِمَالِ وَالْغَلَطِ، وَوَصْفُ النَّكِرَةِ، وَبَدَلُ الظَّاهِرِ مِنَ الْمُضْمَرِ، وَعَطْفُ الْبَيَانِ", "en": "The badal: of the whole, the part, inclusion and error; describing the nakira; the apparent noun from the pronoun; ʿaṭf al-bayān", "tr": "Bedel: kül, ba'z, iştimâl ve galat bedeli; nekrenin vasfı; zamirden zâhir ismin bedeli; atf-ı beyân"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — التوابع: البدل وعطف البيان", "الكافية لابن الحاجب — البدل، عطف البيان", "شرح قطر الندى لابن هشام — البدل"],
 "amil": "the fourth follower, the badal, is the one intended by the attribution rather than its matbūʿ; four kinds: of the whole (both true of one — جَاءَنِي زَيْدٌ أَخُوكَ), of the part (رَأْسَهُ), of inclusion (a bond with something else, the soul waiting for the second — سُلِبَ زَيْدٌ ثَوْبُهُ), of error (رَأَيْتُ رَجُلًا حِمَارًا — not in eloquent speech; بَلْ instead). A nakira as whole-badal of a maʿrifa must be described (﴿بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ﴾); the apparent noun is whole-badal only of the third-person pronoun (ضَرَبْتُهُ زَيْدًا). The fifth, ʿaṭf al-bayān, clarifies its matbūʿ without adding a meaning in it (أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ). Total maʿmūls: thirty.",
 "question": {
  "en": ["What is the badal? The fourth follower: the one the attribution really aims at, not its matbūʿ — in جَاءَنِي زَيْدٌ أَخُوكَ the coming is meant of «your brother», and «Zayd» paves the way.",
         "What are its four kinds? Of the whole (both words true of one person: زَيْدٌ أَخُوكَ), of the part (رَأْسَهُ, a part of Zayd), of inclusion (ثَوْبُهُ — a bond other than whole and part, so the soul waits for the second), of error (رَأَيْتُ رَجُلًا حِمَارًا).",
         "Does the badal of error occur in eloquent speech? No — the eloquent bring بَلْ instead: رَأَيْتُ رَجُلًا بَلْ حِمَارًا.",
         "When must the badal be described? When a nakira stands as badal of the whole for a maʿrifa: ﴿بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ﴾ (al-ʿAlaq 96:15-16) — the badal نَاصِيَةٍ carries كَاذِبَةٍ so that it falls no short of the mubdal minhu.",
         "May an apparent noun be badal of a pronoun? As badal of the whole only of the third-person pronoun: ضَرَبْتُهُ زَيْدًا — not of the first or second person.",
         "What is ʿaṭf al-bayān, and how does it differ from the badal? A follower brought to clarify its matbūʿ without signifying a meaning in it: أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ — the name explains the kunya; the badal is itself the intended one, the ʿaṭf al-bayān only a clarifier.",
         "How many maʿmūls in all? Thirty: twenty-five by origin and five by following.",
         "What does the engine READ here? The DabtEngine reads أَخُوكَ as a whole-badal in rafʿ by the wāw after the doer, رَأْسَهُ and ثَوْبُهُ as badals carrying their matbūʿ's case, نَاصِيَةٍ in jarr after the jarr-phrase with its naʿt كَاذِبَةٍ, زَيْدًا in naṣb after the object pronoun, and عُمَرُ as a diptote in rafʿ following أَبُو حَفْصٍ."],
  "tr": ["Bedel nedir? Dördüncü tâbi: nisbetin asıl kastettiği, metbûu değil kendisi — câenî Zeydün ehûke'de geliş «kardeşin» hakkında kastedilir, «Zeyd» zemin hazırlar.",
         "Dört kısmı nedir? Kül bedeli (iki lafız bir zat hakkında doğru: Zeydün ehûke), ba'z bedeli (ra'sühû, Zeyd'in cüzü), iştimâl bedeli (sevbühû — külliyet ve cüziyet dışı bir alâka; nefis ikinciyi bekler), galat bedeli (raeytü racülen himâran).",
         "Galat bedeli fasih sözde bulunur mu? Hayır — fasihler yerine bel getirir: raeytü racülen bel himâran.",
         "Bedel ne zaman vasıflanmalıdır? Nekre bir ma'rifeden kül bedeli olunca: bi'n-nâsiyeti nâsiyetin kâzibetin (Alak 96:15-16) — bedel nâsiyetin, mübdelün minhten eksik kalmasın diye kâzibetin ile vasıflanır.",
         "Zâhir isim zamirden bedel olur mu? Kül bedeli olarak ancak gâib zamirinden: darabtühû Zeyden — mütekellim ve muhâtaptan olmaz.",
         "Atf-ı beyân nedir, bedelden farkı ne? Metbûunu açıklamak için getirilen, onda bir manaya delâlet etmeyen tâbi: aksame billâhi Ebû Hafsin Umeru — ad künyeyi açıklar; bedel kastedilenin kendisidir, atf-ı beyân yalnız açıklayıcıdır.",
         "Toplam kaç ma'mûl? Otuz: yirmi beşi bi'l-asâle, beşi bi't-tebaiyye.",
         "Motor burada neyi OKUR? DabtEngine ehûke'yi fâilden sonra vâv ile merfû kül bedeli, ra'sühû ve sevbühû'yu metbûunun i'râbını taşıyan bedel, nâsiyetin'i cer öbeğinden sonra sıfatı kâzibetin ile mecrûr, Zeyden'i mef'ûl zamirinden sonra mansûb, Umeru'yu Ebû Hafsin'den sonra gayr-ı munsarıf merfû olarak okur."],
 },
 "plain": {"en": "A badal restates the word before it and is the real target: «Zayd came, your brother» (whole), «I struck Zayd, his head» (part), «Zayd was robbed, his garment» (bond), «I saw a man, a donkey» (a slip). An indefinite badal of a definite word needs an adjective. ʿAṭf al-bayān just clarifies: «Abū Ḥafṣ, ʿUmar».",
           "tr": "Bedel, öncekini yeniden söyleyen ve asıl hedef olan sözdür: «Zeyd geldi, kardeşin» (kül), «Zeyd'i dövdüm, başını» (ba'z), «Zeyd soyuldu, elbisesi» (bağ), «bir adam gördüm, eşek» (sürçme; yerine «bilakis» de). Belirli sözün belirsiz bedeli sıfat ister. Atf-ı beyân yalnız açıklar: «Ebû Hafs, Ömer». Toplam otuz ma'mûl."},
 "explanation": {"en": "The fourth follower is the badal: the one intended by the attribution rather than its matbūʿ. It is of four kinds. The badal of the whole from the whole, when both are true of one — جَاءَنِي زَيْدٌ أَخُوكَ. The badal of the part from the whole, when it is a part of the mubdal minhu — ضَرَبْتُ زَيْدًا رَأْسَهُ. The badal of inclusion, when between the two there is a bond with something other than them, such that the soul waits after the first is mentioned and longs for the second — سُلِبَ زَيْدٌ ثَوْبُهُ. The badal of error, when the mention of the mubdal minhu was a slip — رَأَيْتُ رَجُلًا حِمَارًا; it does not occur in the speech of the eloquent, who bring بَلْ instead. A nakira that stands as whole-badal of a maʿrifa must be described: ﴿بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ﴾ (al-ʿAlaq 96:15-16). The apparent noun is made whole-badal of a pronoun only from the third person: ضَرَبْتُهُ زَيْدًا. The fifth follower is ʿaṭf al-bayān: a follower brought to clarify its matbūʿ and signifying no meaning in it — أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ, where the name clarifies the kunya. The sum of the maʿmūls mentioned is thirty: twenty-five by origin and five by following (the Ottoman commentary's count). The lithograph spells the number ثلثون in the old orthography.",
                 "tr": "Dördüncü tâbi bedeldir: nisbet bakımından metbûu değil kendisi kastedilen. Dört kısımdır. Külden küle bedel, ikisi bir zat hakkında doğru olunca — câenî Zeydün ehûke. Ba'zdan küle bedel, mübdelün minhin cüzü olunca — darabtü Zeyden ra'sehû. İştimâl bedeli, ikisi arasında kendilerinden başka bir şeyle bir bağ olup nefis ilkinin zikrinden sonra bekleyip ikincisini özleyince — sülibe Zeydün sevbühû. Galat bedeli, mübdelün minhin zikri yanlış olunca — raeytü racülen himâran; fasihlerin sözünde bulunmaz, onlar yerine bel getirir. Ma'rifeden kül bedeli olan nekreyi vasıflamak vâciptir: bi'n-nâsiyeti nâsiyetin kâzibetin (Alak 96:15-16). Zâhir isim zamirden kül bedeli olarak ancak gâibden yapılır: darabtühû Zeyden. Beşinci tâbi atf-ı beyândır: metbûunu açıklamak için getirilen ve onda bir manaya delâlet etmeyen tâbi — aksame billâhi Ebû Hafsin Umeru; ad künyeyi açıklar. Zikredilen ma'mûllerin toplamı otuzdur: yirmi beşi bi'l-asâle, beşi bi't-tebaiyye (Osmanlı şerhinin sayımı). Litografi sayıyı eski imlâ ile ثلثون yazar."},
 "examples": [
  {"ar": "جَاءَنِي زَيْدٌ أَخُوكَ", "en": "the badal of the whole", "tr": "kül bedeli", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "ضَرَبْتُ زَيْدًا رَأْسَهُ", "en": "the badal of the part", "tr": "ba'z bedeli", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "سُلِبَ زَيْدٌ ثَوْبُهُ", "en": "the badal of inclusion", "tr": "iştimâl bedeli", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ", "en": "the nakira badal described (al-ʿAlaq 96:15-16)", "tr": "vasıflanan nekre bedel (Alak 96:15-16)", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ", "en": "ʿaṭf al-bayān", "tr": "atf-ı beyân", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "بِالنَّاصِيَةِ نَاصِيَةٍ (no description)", "right": "بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ", "why": {"en": "a nakira standing as whole-badal of a maʿrifa must be described", "tr": "ma'rifeden kül bedeli olan nekre vasıflanmalıdır"}},
  {"wrong": "ضَرَبْتُكَ زَيْدًا (whole-badal of «you»)", "right": "ضَرَبْتُهُ زَيْدًا", "why": {"en": "the apparent noun is whole-badal only of the third-person pronoun", "tr": "zâhir isim kül bedeli olarak ancak gâib zamirinden olur"}},
  {"wrong": "رَأَيْتُ رَجُلًا حِمَارًا (in careful speech)", "right": "رَأَيْتُ رَجُلًا بَلْ حِمَارًا", "why": {"en": "the eloquent correct a slip with بَلْ, not with a badal of error", "tr": "fasihler sürçmeyi galat bedeliyle değil bel ile düzeltir"}},
  {"wrong": "جَاءَنِي زَيْدٌ أَخَاكَ", "right": "جَاءَنِي زَيْدٌ أَخُوكَ", "why": {"en": "the badal follows its matbūʿ's case: rafʿ, shown by the wāw of the five nouns", "tr": "bedel metbûunun i'râbına uyar: ref', beş ismin vâvı ile"}},
 ],
}
ADD_EN = (" Chapter 51 (print pp. 146-147): the badal — the one intended by the attribution (s1), of the whole (s2), the part (s3), inclusion (s4), error and بَلْ (s5), the described nakira of al-ʿAlaq 96:15-16 and the apparent noun from the third-person pronoun (s6); ʿaṭf al-bayān (s7); the thirty maʿmūls (s8).")
ADD_TR = (" Elli birinci bab (baskı s. 146-147): bedel — nisbetle kastedilen (s1), kül (s2), ba'z (s3), iştimâl (s4), galat ve bel (s5), Alak 96:15-16'nın vasıflanan nekresi ve gâib zamirinden zâhir isim (s6); atf-ı beyân (s7); otuz ma'mûl (s8).")
write_out(51, S, TITLE, ADD_EN, ADD_TR, "pp. 146-147", GLOSS_ADD, notes=(NOTE,),
          related=((K50, [K]), (BD, [K]), (AB, [K]), (TW, [K]), (FN, [K])))
report(51, S, GLOSS_ADD, (NOTE,))
