# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 35: the FIFTH manṣūb, the mafʿūl maʿah — what is mentioned after the wāw for the accompaniment of a governor's
# governed (جِئْتُ وَزَيْدًا); never fronted before the governor or the accompanied governed, never multiplied — and the SIXTH, the ḥāl: what
# shows the state of the doer or the object, in wording or in sense (ضَرَبْتُ زَيْدًا قَائِمًا، هٰذَا زَيْدٌ قَائِمًا); its governor the verb, its
# likeness or its sense; its conditions — a nakira, not before the maʿnawī governor nor before the jarr'd owner (مُرَّ بِزَيْدٍ جَالِسًا is not
# said); the ḥāl fronted when its owner is a pure nakira (جَاءَنِي رَاكِبًا رَجُلٌ). Print pp. 133–134.
#   python3 author_izhar_ch35.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; MM2 = "maful-maah"; HL = "hal"; AM = "al-amil-al-manawi"; SH = "shurut-amal-ism-al-fail"; AW = "anwa-al-waw"
K = "al-maful-maah-wal-hal"
K34 = "al-maful-fih-wal-maful-lah"
TITLE = {"ar": "الْمَنْصُوبُ الْخَامِسُ وَالسَّادِسُ: الْمَفْعُولُ مَعَهُ وَالْحَالُ وَشُرُوطُهَا", "en": "The fifth and sixth manṣūb: the mafʿūl maʿah, and the ḥāl with its conditions", "tr": "Beşinci ve altıncı mansûb: mef'ûl-i meah ve şartlarıyla hâl"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wala(): return tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part"))
def ala(): return tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»")

# ----------- s1 — the fifth: the mafʿūl maʿah
S.append({"id": "s1", "translation": {"en": "And the fifth is the mafʿūl maʿah, and it is what is mentioned after the wāw for the accompaniment of a governor's governed word — as in «I came, and Zayd with me»;", "tr": "Beşincisi mef'ûl-i meahtır: bir âmilin ma'mûlüne eşlik etmek üzere vâv'dan sonra zikredilen şeydir — «Zeyd'le birlikte geldim» gibi;"},
 "tokens": [
  tok("وَالْخَامِسُ", "khamis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَامِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fifth»", "«beşincisi»", segments=wa("الْخَامِسُ", "khamis", "noun")),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, IMF, MM2], "خَبَرٌ مَرْفُوعٌ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("مَعَهُ", "maa", "noun", [K, MF, ID, MM2], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جُزْءُ الِاسْمِ.", "«maʿah» — part of the term.", "«meah» — terimin parçası.", punct="،", segments=[seg("مَعَ", "maa", "noun"), pr3ms()]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمَذْكُورُ", "madhkur", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«what is mentioned» — the khabar.", "«zikredilen» — haber."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("الْوَاوِ", "waw-letter", "noun", [K, ID, AW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَاوُ الْمَعِيَّةِ.", "«the wāw» — of accompaniment.", "«vâv» — maiyyet vâvı."),
  tok("لِمُصَاحَبَةِ", "musahaba", "noun", [K, HJ, ID, MSD, "form-iii-verbs"], "اللَّامُ حَرْفُ جَرٍّ، وَمُصَاحَبَةِ مَجْرُورٌ، مُضَافٌ.", "«for the accompaniment of»", "«eşlik etmek için»", segments=[seg("لِ", "li", "prep"), seg("مُصَاحَبَةِ", "musahaba", "noun")]),
  tok("مَعْمُولِ", "mamul", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the governed of»", "«ma'mûlüne»"),
  tok("عَامِلٍ", "amil", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a governor»", "«bir âmilin»", punct="،"),
  nahw(),
  tok("جِئْتُ", "jaa", "verb", [K, FL, HV, MM2], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْمَعْمُولُ الْمُصَاحَبُ.", "«I came» — the tāʾ is the accompanied governed.", "«geldim» — tâ eşlik edilen ma'mûl.", segments=[seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("وَزَيْدًا", "zayd", "propn", [K, MM2, AW], "الْوَاوُ لِلْمَعِيَّةِ، وَزَيْدًا مَفْعُولٌ مَعَهُ مَنْصُوبٌ.", "«and Zayd with me» — the mafʿūl maʿah.", "«ve Zeyd'le» — mef'ûl-i meah.", punct="،", segments=wa("زَيْدًا", "zayd", "propn")),
 ]})
# ----------- s2 — never fronted, never multiplied
S.append({"id": "s2", "translation": {"en": "and its fronting before a governor is not allowed, nor before the accompanied governed, nor its multiplication.", "tr": "âmilin önüne alınması câiz değildir; eşlik edilen ma'mûlün önüne de; taaddüdü de."},
 "tokens": [
  wala(),
  tok("يَجُوزُ", "jaaza", "verb", [K, LN, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("تَقْدِيمُهُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its fronting»", "«öne alınması»", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
  ala(),
  tok("عَامِلٍ", "amil", "noun", [K, HJ, IFA], "مَجْرُورٌ بِعَلَى.", "«a governor»", "«âmilin»", punct="،"),
  wala(), ala(),
  tok("الْمَعْمُولِ", "mamul", "noun", [K, HJ, IMF], "مَجْرُورٌ بِعَلَى.", "«the governed»", "«ma'mûlün»"),
  tok("الْمُصَاحِبِ", "musahib", "noun", [K, NA, IFA, "form-iii-verbs"], "نَعْتٌ مَجْرُورٌ.", "«accompanied»", "«eşlik edilen»", punct="،"),
  wala(),
  tok("تَعَدُّدُهُ", "taaddud", "noun", [K, AT, FL, ID, MSD, F5], "مَعْطُوفٌ عَلَى تَقْدِيمُهُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its multiplication»", "«taaddüdü»", punct=".", segments=[seg("تَعَدُّدُ", "taaddud", "noun"), pr3ms()]),
 ]})
# ----------- s3 — the sixth: the ḥāl defined
S.append({"id": "s3", "translation": {"en": "And the sixth is the ḥāl, and it is what shows the state of the doer or of the object, in wording or in sense — like «I struck Zayd standing» and «this is Zayd, standing»;", "tr": "Altıncısı hâldir: fâilin veya mef'ûl-i bihin — lafzan ya da mânen — durumunu açıklayan şeydir; «Zeyd'i ayakta dövdüm» ve «işte Zeyd, ayakta» gibi;"},
 "tokens": [
  tok("وَالسَّادِسُ", "sadis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّادِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sixth»", "«altıncısı»", segments=wa("السَّادِسُ", "sadis", "noun")),
  tok("الْحَالُ", "hal", "noun", [K, MK, HL], "خَبَرٌ مَرْفُوعٌ.", "«the ḥāl» — the khabar.", "«hâl» — haber.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هِيَ", "hiya", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، خَبَرٌ.", "«what» — the khabar.", "«şey» — haber."),
  tok("يُبَيِّنُ", "bayyana", "verb", [K, MAW, MR, FL, F2], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ مَا.", "«shows»", "«açıklayan»"),
  tok("هَيْئَةَ", "haya-shape", "noun", [K, MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the state of»", "«durumunu»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâilin»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("الْمَفْعُولِ", "maful-noun", "noun", [K, AT, IMF], "مَعْطُوفٌ مَجْرُورٌ.", "«the object»", "«mef'ûlün»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«bih»", "«bih»"),
  tok("لَفْظًا", "lafz", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — أَوْ حَالٌ.", "«in wording»", "«lafzan»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَعْنًى", "mana", "noun", [K, AT, TMZ, MQ], "مَعْطُوفٌ مَنْصُوبٌ.", "«in sense»", "«mânen»", punct="،"),
  tok("مِثْلُ", "mithl", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«like»", "«… gibi»", punct=":"),
  tok("ضَرَبْتُ", "daraba", "verb", [K, FL, HL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("زَيْدًا", "zayd", "propn", [K, MB, HL], "مَفْعُولٌ بِهِ مَنْصُوبٌ — ذُو الْحَالِ.", "«Zayd» — the object, the owner of the ḥāl.", "«Zeyd'i» — mef'ûl, hâl sahibi."),
  tok("قَائِمًا", "qaim", "noun", [K, HL, IFA], "حَالٌ مَنْصُوبٌ — مِنَ الْمَفْعُولِ لَفْظًا.", "«standing» — the ḥāl of the object in wording.", "«ayakta» — lafzan mef'ûlün hâli.", punct="،"),
  tok("وَهٰذَا", "hadha", "pron", [K, AT, MK, HL], "الْوَاوُ عَاطِفَةٌ، وَهٰذَا مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and this»", "«ve işte bu»", segments=wa("هٰذَا", "hadha", "pron")),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, HL], "خَبَرٌ مَرْفُوعٌ — ذُو الْحَالِ مَعْنًى.", "«is Zayd» — the owner of the ḥāl in sense.", "«Zeyd» — mânen hâl sahibi."),
  tok("قَائِمًا", "qaim", "noun", [K, HL, IFA, MNF], "حَالٌ مَنْصُوبٌ، وَعَامِلُهُ مَعْنَى الْفِعْلِ فِي هٰذَا: أُشِيرُ.", "«standing» — the ḥāl, governed by the sense of the verb in «this».", "«ayakta» — hâl; âmili hâzâ'daki fiil mânâsı.", punct="،"),
 ]})
# ----------- s4 — its governor
S.append({"id": "s4", "translation": {"en": "and its governor is the verb, or its likeness, or its sense;", "tr": "âmili fiil, fiilin benzeri veya fiilin mânâsıdır;"},
 "tokens": [
  tok("وَعَامِلُهَا", "amil", "noun", [K, AT, MK, ID, IFA], "الْوَاوُ عَاطِفَةٌ، وَعَامِلُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its governor»", "«ve âmili»", segments=[seg("وَ", "wa", "conj"), seg("عَامِلُ", "amil", "noun"), pr3fs()]),
  tok("الْفِعْلُ", "fil", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the verb» — the khabar.", "«fiil» — haber."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("شِبْهُهُ", "shibh", "noun", [K, AT, ID, SH], "مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — كَاسْمِ الْفَاعِلِ.", "«its likeness» — as the participle.", "«benzeri» — ism-i fâil gibi.", segments=[seg("شِبْهُ", "shibh", "noun"), pr3ms()]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَعْنَاهُ", "mana", "noun", [K, AT, ID, MQ, MNF], "مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — كَاسْمِ الْإِشَارَةِ وَالظَّرْفِ.", "«its sense» — as the demonstrative and the ẓarf.", "«mânâsı» — işaret ismi ve zarf gibi.", punct="،", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
 ]})
# ----------- s5 — its conditions
S.append({"id": "s5", "translation": {"en": "and its condition is that it be indefinite, and that it not be fronted before the maʿnawī governor nor before the owner of the ḥāl in jarr — so one does not say «Zayd was passed by, sitting»;", "tr": "şartı nekre olması, ma'nevî âmilin ve mecrûr hâl sahibinin önüne alınmamasıdır — bu yüzden «mürre bi-Zeydin câlisen» denmez;"},
 "tokens": [
  tok("وَشَرْطُهَا", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its condition»", "«ve şartı»", segments=[seg("وَ", "wa", "conj"), seg("شَرْطُ", "shart", "noun"), pr3fs()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, MK], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that»", "«-ması»"),
  tok("تَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«it be»", "«olması»"),
  tok("نَكِرَةً", "nakira", "noun", [K, KN], "خَبَرُ تَكُونَ مَنْصُوبٌ.", "«indefinite»", "«nekre»", punct="،"),
  wala(),
  tok("تَتَقَدَّمَ", "taqaddama", "verb", [K, AT, AMS, F5], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى تَكُونَ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«it be fronted»", "«öne alınmaması»"),
  ala(),
  tok("الْعَامِلِ", "amil", "noun", [K, HJ, IFA, AM], "مَجْرُورٌ بِعَلَى.", "«the governor»", "«âmilin»"),
  tok("الْمَعْنَوِيِّ", "manawi", "noun", [K, NA, NSB, AM], "نَعْتٌ مَجْرُورٌ — مَعْنَى الْفِعْلِ.", "«maʿnawī» — the sense of the verb.", "«ma'nevî» — fiil mânâsı.", punct="،"),
  wala(), ala(),
  tok("ذِي", "dhu", "noun", [K, HJ, ID, "five-nouns"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«the owner of»", "«sahibinin»"),
  tok("الْحَالِ", "hal", "noun", [K, ID, HL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ḥāl»", "«hâl»"),
  tok("الْمَجْرُورِ", "majrur", "noun", [K, NA, IMF], "نَعْتٌ لِذِي مَجْرُورٌ.", "«in jarr»", "«mecrûr»", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, AT, LN], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not»", "«bu yüzden … -mez»", segments=fa("لَا", "la-nafiya", "part")),
  tok("يُقَالُ", "qala", "verb", [K, LN, NF, HV, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«is it said»", "«denmez»", punct=":"),
  tok("مُرَّ", "marra", "verb", [K, NF, HL, "doubled-verbs"], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was passed»", "«uğranıldı»"),
  tok("بِزَيْدٍ", "zayd", "propn", [K, HJ, NF, HL], "الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ — نَائِبُ الْفَاعِلِ مَحَلًّا، ذُو الْحَالِ.", "«by Zayd» — the jarr'd deputy doer, owner of the ḥāl.", "«Zeyd'e» — mecrûr nâib-i fâil, hâl sahibi.", segments=[seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
  tok("جَالِسًا", "jalis-sitting", "noun", [K, HL, IFA], "حَالٌ مَنْصُوبٌ مِنَ الْمَجْرُورِ — وَالْمَمْنُوعُ تَقْدِيمُهُ: جَالِسًا مُرَّ بِزَيْدٍ.", "«sitting» — the ḥāl of the jarr'd owner; its fronting is what is refused.", "«oturur hâlde» — mecrûrun hâli; reddedilen, öne alınmasıdır.", punct="،"),
 ]})
# ----------- s6 — the owner a pure nakira: the ḥāl fronted
S.append({"id": "s6", "translation": {"en": "and if its owner is a pure indefinite, the fronting of the ḥāl before it is obligatory — as in «there came to me, riding, a man».", "tr": "sahibi hâlis nekre olursa hâlin onun önüne alınması vâcibdir — «bana binmiş olarak bir adam geldi» gibi."},
 "tokens": [
  tok("وَلَوْ", "law", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَلَوْ حَرْفُ شَرْطٍ.", "«and if»", "«ve eğer»", segments=wa("لَوْ", "law", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، فِعْلُ الشَّرْطِ.", "«is»", "«olursa»"),
  tok("صَاحِبُهَا", "sahib", "noun", [K, KN, ID, IFA, HL], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — ذُو الْحَالِ.", "«its owner» — the ism of kāna.", "«sahibi» — kâne'nin ismi.", segments=[seg("صَاحِبُ", "sahib", "noun"), pr3fs()]),
  tok("نَكِرَةً", "nakira", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«an indefinite»", "«nekre»"),
  tok("مَحْضَةً", "mahd", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ — غَيْرَ مَوْصُوفَةٍ وَلَا مُضَافَةٍ.", "«pure» — unqualified, unannexed.", "«hâlis» — vasıfsız, muzâf değil."),
  tok("وَجَبَ", "wajaba", "verb", [K, FL, INS], "فِعْلٌ مَاضٍ، جَوَابُ الشَّرْطِ.", "«it is obligatory»", "«vâcib olur»"),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the fronting of»", "«öne alınması»"),
  tok("الْحَالِ", "hal", "noun", [K, ID, HL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ḥāl»", "«hâlin»"),
  tok("عَلَيْهَا", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — عَلَى النَّكِرَةِ.", "«before it» — before the indefinite.", "«onun önüne» — nekrenin.", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3fs()]),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV, HL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("رَاكِبًا", "rakib", "noun", [K, HL, IFA], "حَالٌ مُقَدَّمٌ مَنْصُوبٌ — مِنَ النَّكِرَةِ بَعْدَهُ.", "«riding» — the ḥāl fronted before its indefinite owner.", "«binmiş olarak» — nekre sahibinin önüne alınmış hâl."),
  tok("رَجُلٌ", "rajul", "noun", [K, FL, HL], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ — ذُو الْحَالِ، نَكِرَةٌ مَحْضَةٌ.", "«a man» — the delayed doer, the pure indefinite owner.", "«bir adam» — sona alınmış fâil, hâlis nekre sahip.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "musahaba": G("musahaba", "مُصَاحَبَة", "ص ح ب", "noun", "accompaniment — the maṣdar of form III «to accompany»", "eşlik etme, maiyyet — III. bab mastarı", 4),
 "musahib": G("musahib", "مُصَاحِب", "ص ح ب", "noun", "accompanying, accompanied (active participle of form III)", "eşlik eden, eşlik edilen (III. babın ism-i fâili)", 4),
 "manawi": G("manawi", "مَعْنَوِيّ", "ع ن ي", "noun", "of sense, semantic — the maʿnawī governor, as opposed to the lafẓī", "ma'nevî, mânâya ait — lafzînin karşıtı olan ma'nevî âmil", 4),
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
print("izhar ch35 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "jaa", "bayyana", "taqaddama", "marra", "wajaba", "daraba") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَفْعُولُ مَعَهُ وَالْحَالُ: تَعْرِيفُهُمَا وَعَامِلُ الْحَالِ وَشُرُوطُهَا", "en": "The mafʿūl maʿah and the ḥāl: their definitions, the ḥāl's governor and its conditions", "tr": "Mef'ûl-i meah ve hâl: tarifleri, hâlin âmili ve şartları"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: المفعول معه والحال", "الكافية لابن الحاجب — المفعول معه، الحال", "شرح قطر الندى لابن هشام — المفعول معه والحال"],
 "amil": "the fifth manṣūb is the mafʿūl maʿah — what is mentioned after the wāw of accompaniment to accompany a governor's governed word (جِئْتُ وَزَيْدًا): never fronted before the governor or before the accompanied word, never multiplied; the sixth is the ḥāl — what shows the state of the doer or the object in wording or in sense (ضَرَبْتُ زَيْدًا قَائِمًا، هٰذَا زَيْدٌ قَائِمًا), governed by the verb, its likeness (the participle) or its sense (the demonstrative, the ẓarf); its conditions: a nakira, not fronted before a maʿnawī governor nor before an owner in jarr (مُرَّ بِزَيْدٍ جَالِسًا is not said with the ḥāl first), and fronted of necessity when its owner is a pure nakira (جَاءَنِي رَاكِبًا رَجُلٌ)",
 "question": {
  "en": ["What is the mafʿūl maʿah? What is mentioned after the wāw of accompaniment to go along with a governor's governed word: زَيْدًا in جِئْتُ وَزَيْدًا — «I came together with Zayd».",
         "What may it not do? Be fronted before the governor (وَزَيْدًا جِئْتُ), be fronted before the accompanied word, or be multiplied (جِئْتُ وَزَيْدًا وَعَمْرًا is two ʿaṭfs, not two mafʿūl maʿah).",
         "What is the ḥāl? What shows the state of the doer or the object — in wording (ضَرَبْتُ زَيْدًا قَائِمًا: Zayd is the object by wording) or in sense (هٰذَا زَيْدٌ قَائِمًا: Zayd is pointed at, an object in sense).",
         "What governs the ḥāl? The verb, its likeness (ism al-fāʿil, the ṣifa), or its sense — the demonstrative, the ẓarf, كَأَنَّ.",
         "What are its conditions? A nakira; not fronted before a maʿnawī governor (هٰذَا قَائِمًا زَيْدٌ is refused); not fronted before an owner in jarr: جَالِسًا مُرَّ بِزَيْدٍ is not said.",
         "When MUST the ḥāl be fronted? When its owner is a pure nakira — unqualified, unannexed: جَاءَنِي رَاكِبًا رَجُلٌ, lest رَاكِبًا be taken for a naʿt of رَجُلٌ.",
         "What does the engine READ here? The DabtEngine reads the name after وَ on the tanwīn fatḥ after a bound-doer verb as the mafʿūl maʿah, the ṣifa-shaped nakira on the tanwīn fatḥ after an object or a demonstrative's khabar as its ḥāl, the fronted ḥāl before a delayed nakira doer, and the passive مُرَّ بِزَيْدٍ with its jarr'd deputy."],
  "tr": ["Mef'ûl-i meah nedir? Maiyyet vâvından sonra bir âmilin ma'mûlüne eşlik etmek üzere zikredilen şey: ci'tü ve-Zeyden'deki Zeyden — «Zeyd'le birlikte geldim».",
         "Neyi yapamaz? Âmilin önüne alınamaz (ve-Zeyden ci'tü), eşlik edilen kelimenin önüne alınamaz, taaddüd edemez (ci'tü ve-Zeyden ve-Amren iki atıftır, iki mef'ûl-i meah değil).",
         "Hâl nedir? Fâilin veya mef'ûlün durumunu gösteren şey — lafzan (darabtü Zeyden kâimen: Zeyd lafzan mef'ûl) veya mânen (hâzâ Zeydün kâimen: Zeyd işaret edilen, mânen mef'ûl).",
         "Hâli ne yönetir? Fiil, benzeri (ism-i fâil, sıfat) veya mânâsı — işaret ismi, zarf, keenne.",
         "Şartları nedir? Nekre olması; ma'nevî âmilin önüne alınmaması (hâzâ kâimen Zeydün reddedilir); mecrûr sahibinin önüne alınmaması: câlisen mürre bi-Zeydin denmez.",
         "Hâl ne zaman öne alınmak ZORUNDADIR? Sahibi hâlis nekre olunca — vasıfsız, muzâf olmayan: câenî râkiben racülün; yoksa râkiben, racülün'ün sıfatı sanılır.",
         "Motor burada neyi OKUR? DabtEngine fâili bağlı fiilden sonra vâv'ın ardındaki tenvîn-fethalı ismi mef'ûl-i meah okur; mef'ûlden veya işaret isminin haberinden sonraki tenvîn-fethalı sıfat şekilli nekreyi hâl okur; sona alınmış nekre fâilin önündeki hâli, ve mecrûr nâibiyle meçhul mürre bi-Zeydin'i okur."],
 },
 "plain": {"en": "The fifth accusative is the «companion object»: «I came, and Zayd», i.e. together with Zayd. It never moves before its verb. The sixth is the ḥāl, a state word: «I struck Zayd standing». It must be indefinite, may not precede a verbless governor or an owner after a preposition, and must precede a bare indefinite one.",
           "tr": "Beşinci mansûb «beraberlik nesnesi»dir: «geldim ve Zeyd» yani «Zeyd'le birlikte». Fiilinin önüne geçmez, ikilenmez. Altıncısı hâldir, durum sözü: «Zeyd'i ayakta dövdüm», «işte Zeyd, ayakta». Nekre olmalı, fiilsiz âmilin ya da edatlı sahibinin önüne geçmemeli, çıplak nekre sahibinin ise önüne geçmelidir."},
 "explanation": {"en": "The fifth manṣūb, the mafʿūl maʿah, is what is mentioned after the wāw of accompaniment to go along with a governor's governed word: جِئْتُ وَزَيْدًا, where the tāʾ of جِئْتُ is the accompanied word and زَيْدًا takes naṣb by the verb through the wāw. It may not be fronted before the governor, nor before the accompanied word, nor multiplied. The sixth, the ḥāl, is what shows the state of the doer or the object, in wording (ضَرَبْتُ زَيْدًا قَائِمًا) or in sense (هٰذَا زَيْدٌ قَائِمًا, Zayd being pointed at). Its governor is the verb, its likeness (the participle) or its sense (the demonstrative, the ẓarf). Its conditions: that it be a nakira; that it not be fronted before a maʿnawī governor; and that it not be fronted before an owner in jarr — جَالِسًا مُرَّ بِزَيْدٍ is not said. When the owner is a pure nakira the ḥāl must be fronted before it (جَاءَنِي رَاكِبًا رَجُلٌ), lest it be read as a naʿt.",
                 "tr": "Beşinci mansûb mef'ûl-i meah, maiyyet vâvından sonra bir âmilin ma'mûlüne eşlik etmek üzere zikredilendir: ci'tü ve-Zeyden; ci'tü'nün tâ'sı eşlik edilen kelime, Zeyden vâv aracılığıyla fiille mansûb. Âmilin önüne, eşlik edilen kelimenin önüne alınamaz; taaddüd edemez. Altıncısı hâl, fâilin veya mef'ûlün durumunu lafzan (darabtü Zeyden kâimen) veya mânen (hâzâ Zeydün kâimen, Zeyd işaret edilen) gösterendir. Âmili fiil, benzeri (ism-i fâil) veya mânâsıdır (işaret ismi, zarf). Şartları: nekre olması; ma'nevî âmilin önüne alınmaması; mecrûr sahibinin önüne alınmaması — câlisen mürre bi-Zeydin denmez. Sahibi hâlis nekre olunca hâl onun önüne alınmak zorundadır (câenî râkiben racülün); yoksa sıfat okunur."},
 "examples": [
  {"ar": "جِئْتُ وَزَيْدًا", "en": "the mafʿūl maʿah", "tr": "mef'ûl-i meah", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَلَا يَجُوزُ تَقْدِيمُهُ … وَلَا تَعَدُّدُهُ", "en": "never fronted, never multiplied", "tr": "öne alınmaz, taaddüd etmez", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "ضَرَبْتُ زَيْدًا قَائِمًا، وَهٰذَا زَيْدٌ قَائِمًا", "en": "the ḥāl of the object in wording and in sense", "tr": "lafzan ve mânen mef'ûlün hâli", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَعَامِلُهَا الْفِعْلُ أَوْ شِبْهُهُ أَوْ مَعْنَاهُ", "en": "the ḥāl's governor", "tr": "hâlin âmili", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "فَلَا يُقَالُ: مُرَّ بِزَيْدٍ جَالِسًا", "en": "no ḥāl fronted before a jarr'd owner", "tr": "mecrûr sahibin önüne hâl alınmaz", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "جَاءَنِي رَاكِبًا رَجُلٌ", "en": "the ḥāl fronted before a pure nakira", "tr": "hâlis nekrenin önüne alınmış hâl", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "وَزَيْدًا جِئْتُ", "right": "جِئْتُ وَزَيْدًا", "why": {"en": "the mafʿūl maʿah may not be fronted before its governor", "tr": "mef'ûl-i meah âmilinin önüne alınamaz"}},
  {"wrong": "ضَرَبْتُ زَيْدًا الْقَائِمَ (as a ḥāl)", "right": "ضَرَبْتُ زَيْدًا قَائِمًا", "why": {"en": "the ḥāl must be a nakira; the definite word would be a naʿt", "tr": "hâl nekre olmalı; ma'rife kelime sıfat olur"}},
  {"wrong": "جَاءَنِي رَجُلٌ رَاكِبًا", "right": "جَاءَنِي رَاكِبًا رَجُلٌ", "why": {"en": "with a pure nakira owner the ḥāl must be fronted, else رَاكِبًا is read as a naʿt and would take rafʿ", "tr": "hâlis nekre sahipte hâl öne alınmalı; yoksa râkiben sıfat okunur ve ref' alırdı"}},
 ],
}
TMZ = "tamyiz"
ADD_EN = (" Chapter 35 (print pp. 133-134): the mafʿūl maʿah defined (s1), never fronted nor multiplied (s2); the ḥāl defined in wording and in sense (s3), its governor (s4), its conditions with the refused مُرَّ بِزَيْدٍ جَالِسًا (s5), fronted before a pure nakira owner (s6).")
ADD_TR = (" Otuz beşinci bab (baskı s. 133-134): mef'ûl-i meahın tarifi (s1), öne alınmaması ve taaddüd etmemesi (s2); hâlin lafzan ve mânen tarifi (s3), âmili (s4), reddedilen mürre bi-Zeydin câlisen ile şartları (s5), hâlis nekre sahibinin önüne alınması (s6).")
write_out(35, S, TITLE, ADD_EN, ADD_TR, "pp. 133-134", GLOSS_ADD, notes=(NOTE,),
          related=((K34, [K]), (MM2, [K]), (HL, [K]), (AM, [K]), (AW, [K]), (MNF, [K])))
report(35, S, GLOSS_ADD, (NOTE,))
