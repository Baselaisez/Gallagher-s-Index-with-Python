# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 50: the THIRD follower, the tawkīd — two kinds: the verbal, the repetition of the first word or its synonym in the
# attached pronoun, running through all words (جَاءَنِي زَيْدٌ زَيْدٌ، ضَرَبْتُ أَنْتَ، ضَرَبَ زَيْدٌ، زَيْدٌ قَائِمٌ قَائِمٌ); and the semantic, particular to the
# maʿrifas: نَفْسُهُ وَعَيْنُهُ وَكِلَاهُمَا وَكِلْتَاهُمَا وَكُلُّهُ وَأَجْمَعُ وَأَكْتَعُ وَأَبْتَعُ وَأَبْصَعُ — the last three followers of أَجْمَع, never before it nor without it in
# eloquent speech; the attached rafʿ pronoun confirmed by نَفْس or عَيْن is first confirmed by a detached one (زَيْدٌ ضَرَبَ هُوَ نَفْسُهُ أَوْ عَيْنُهُ). Print pp. 145–146.
#   python3 author_izhar_ch50.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; TRF = "tarif-al-musnad-ilayh"; IDH = "idha-shartiyya"
K = "al-tawkid-al-lafzi-wal-manawi"
K49 = "al-atf-bil-huruf-wa-ahkamuh"
TITLE = {"ar": "التَّابِعُ الثَّالِثُ: التَّأْكِيدُ اللَّفْظِيُّ وَالْمَعْنَوِيُّ وَأَلْفَاظُهُ", "en": "The third follower: the verbal and the semantic tawkīd and its words", "tr": "Üçüncü tâbi: lafzî ve ma'nevî te'kîd ve lafızları"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wW(form, lex, en, tr, punct=None, ar=None, segs=None): return tok(form, lex, "noun", [K, AT, TK], "الْوَاوُ عَاطِفَةٌ، وَ" + (ar or (form[2:] + " لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مِنْ أَلْفَاظِ التَّأْكِيدِ.")), en, tr, punct=punct, segments=segs or wa(form[2:], lex, "noun"))

# ----------- s1 — the third: two kinds; the verbal
S.append({"id": "s1", "translation": {"en": "And the third is the tawkīd, and it is two kinds: verbal — and it is the repetition of the first word, or of its synonym in the attached pronoun, and it runs through all the words — as in «there came to me Zayd, Zayd», «I struck, you», «he struck, Zayd», and «Zayd is standing, standing»;", "tr": "Üçüncüsü te'kîddir; iki kısımdır: lafzî — ilk lafzın ya da muttasıl zamirde onun eş anlamlısının tekrarıdır; bütün lafızlarda yürür — «bana Zeyd geldi, Zeyd», «dövdüm, sen», «dövdü, Zeyd», «Zeyd ayaktadır, ayakta» gibi;"},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third»", "«üçüncüsü»", segments=wa("الثَّالِثُ", "thalith", "noun")),
  tok("التَّأْكِيدُ", "takid", "noun", [K, MK, MSD, TK, TW], "خَبَرٌ مَرْفُوعٌ.", "«the tawkīd» — the khabar.", "«te'kîd» — haber.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("قِسْمَانِ", "qism", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds»", "«iki kısım»", punct=":"),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, MK, NSB, TK], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا لَفْظِيٌّ.", "«verbal»", "«lafzî»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("تَكْرِيرُ", "takrir", "noun", [K, MK, ID, MSD, F2], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the repetition of» — the khabar.", "«tekrarı» — haber."),
  tok("اللَّفْظِ", "lafz", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the word»", "«lafzın»"),
  tok("الْأَوَّلِ", "awwal", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«first»", "«ilk»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مُرَادِفِهِ", "muradif", "noun", [K, AT, ID, IFA, "form-iii-verbs"], "مَعْطُوفٌ عَلَى اللَّفْظِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its synonym»", "«eş anlamlısının»", segments=[seg("مُرَادِفِ", "muradif", "noun"), pr3msi()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الضَّمِيرِ", "damir", "noun", [K, HJ, BM], "مَجْرُورٌ بِفِي.", "«the pronoun»", "«zamir»"),
  tok("الْمُتَّصِلِ", "muttasil", "noun", [K, NA, IFA, BM], "نَعْتٌ مَجْرُورٌ — يُؤَكَّدُ بِالْمُنْفَصِلِ الْمُرَادِفِ لَهُ.", "«attached» — confirmed by its detached synonym.", "«muttasıl» — eş anlamlı munfasılla te'kîd edilir."),
  tok("وَيَجْرِي", "jara", "verb", [K, AT, MR, FL, MQ], "الْوَاوُ عَاطِفَةٌ، وَيَجْرِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and it runs»", "«ve yürür»", segments=wa("يَجْرِي", "jara", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«through»", "«-de»"),
  tok("الْأَلْفَاظِ", "lafz", "noun", [K, HJ, JT], "مَجْرُورٌ بِفِي.", "«the words»", "«lafızlarda»"),
  tok("كُلِّهَا", "kull", "noun", [K, TK, ID], "تَوْكِيدٌ مَعْنَوِيٌّ لِلْأَلْفَاظِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«all» — a semantic tawkīd of «the words».", "«bütün» — lafızların ma'nevî te'kîdi.", punct="،", segments=[seg("كُلِّ", "kull", "noun"), pr3fs()]),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("زَيْدٌ", "zayd", "propn", [K, TK], "تَوْكِيدٌ لَفْظِيٌّ مَرْفُوعٌ — الِاسْمُ مُكَرَّرًا.", "«Zayd» — the noun repeated.", "«Zeyd» — tekrarlanan isim."),
  tok("وَضَرَبْتُ", "daraba", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَضَرَبْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I struck»", "«ve dövdüm»", segments=[seg("وَ", "wa", "conj"), seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنْتَ", "anta", "pron", [K, TK], "تَوْكِيدٌ لَفْظِيٌّ لِلتَّاءِ فِي مَحَلِّ رَفْعٍ — الضَّمِيرُ بِمُرَادِفِهِ الْمُنْفَصِلِ؛ هٰكَذَا فِي الطَّبْعِ.", "«you» — the attached pronoun by its detached synonym, as printed.", "«sen» — muttasıl zamirin munfasıl eş anlamlısı; baskıdaki gibi."),
  tok("وَضَرَبَ", "daraba", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَضَرَبَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and he struck»", "«ve dövdü»", segments=wa("ضَرَبَ", "daraba", "verb")),
  tok("زَيْدٌ", "zayd", "propn", [K, TK], "تَوْكِيدٌ لَفْظِيٌّ لِلْمُسْتَتِرِ مَرْفُوعٌ — عَلَى مَا فِي الطَّبْعِ.", "«Zayd» — confirming the hidden doer, as printed.", "«Zeyd» — gizli fâilin te'kîdi; baskıdaki gibi."),
  tok("وَزَيْدٌ", "zayd", "propn", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and Zayd»", "«ve Zeyd»", segments=wa("زَيْدٌ", "zayd", "propn")),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«is standing»", "«ayaktadır»"),
  tok("قَائِمٌ", "qaim", "noun", [K, TK, IFA], "تَوْكِيدٌ لَفْظِيٌّ لِلْخَبَرِ مَرْفُوعٌ.", "«standing» — the khabar repeated.", "«ayakta» — tekrarlanan haber.", punct="،"),
 ]})
# ----------- s2 — the semantic tawkīd and its words
S.append({"id": "s2", "translation": {"en": "and semantic, particular to the maʿrifas — and it is «nafsuhu», «ʿaynuhu», «kilāhumā», «kiltāhumā», «kulluhu», «ajmaʿu», «aktaʿu», «abtaʿu», «abṣaʿu»; and these three are followers of «ajmaʿu»: none precedes it, nor is any mentioned without it in eloquent speech;", "tr": "ve ma'nevî — ma'rifelere mahsustur; o: nefsühû, aynühû, kilâhümâ, kiltâhümâ, küllühû, ecmau, ektau, ebtau, ebsau; bu üçü ecmau'nun tâbileridir: fasih sözde onun önüne geçmez, onsuz da anılmazlar;"},
 "tokens": [
  tok("وَمَعْنَوِيٌّ", "manawi", "noun", [K, AT, MK, NSB, TK], "الْوَاوُ عَاطِفَةٌ، وَمَعْنَوِيٌّ مَعْطُوفٌ عَلَى لَفْظِيٌّ مَرْفُوعٌ.", "«and semantic»", "«ve ma'nevî»", segments=wa("مَعْنَوِيٌّ", "manawi", "noun")),
  tok("مَخْصُوصٌ", "makhsus", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«particular»", "«mahsus»"),
  tok("بِالْمَعَارِفِ", "marifa", "noun", [K, HJ, JT, TRF], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمَعَارِفِ مَجْرُورٌ — لَا تُؤَكَّدُ النَّكِرَةُ تَأْكِيدًا مَعْنَوِيًّا.", "«to the maʿrifas» — no nakira takes it.", "«ma'rifelere» — nekre ma'nevî te'kîd almaz.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْمَعَارِفِ", "marifa", "noun")]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("نَفْسُهُ", "nafs", "noun", [K, MK, TK, ID], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — يُضَافُ إِلَى ضَمِيرِ الْمُؤَكَّدِ.", "«nafsuhu» — himself; annexed to the confirmed word's pronoun.", "«nefsühû» — kendisi; te'kîd edilenin zamirine muzâf.", segments=[seg("نَفْسُ", "nafs", "noun"), pr3ms()]),
  wW("وَعَيْنُهُ", "ayn-thing", "«and ʿaynuhu» — his very self", "«ve aynühû» — bizzat kendisi", segs=[seg("وَ", "wa", "conj"), seg("عَيْنُ", "ayn-thing", "noun"), pr3ms()]),
  wW("وَكِلَاهُمَا", "kila", "«and kilāhumā» — both of them", "«ve kilâhümâ» — her ikisi", segs=[seg("وَ", "wa", "conj"), seg("كِلَا", "kila", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  wW("وَكِلْتَاهُمَا", "kilta", "«and kiltāhumā» — both (f.)", "«ve kiltâhümâ» — her ikisi (dişil)", segs=[seg("وَ", "wa", "conj"), seg("كِلْتَا", "kilta", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  wW("وَكُلُّهُ", "kull", "«and kulluhu» — all of it", "«ve küllühû» — tamamı", segs=[seg("وَ", "wa", "conj"), seg("كُلُّ", "kull", "noun"), pr3ms()]),
  wW("وَأَجْمَعُ", "ajma-all", "«and ajmaʿu» — entire", "«ve ecmau» — bütün"),
  wW("وَأَكْتَعُ", "akta", "«and aktaʿu»", "«ve ektau»"),
  wW("وَأَبْتَعُ", "abta", "«and abtaʿu»", "«ve ebtau»"),
  wW("وَأَبْصَعُ", "absa", "«and abṣaʿu»", "«ve ebsau»", punct="،"),
  tok("وَهٰذِهِ", "hadhihi", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذِهِ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and these»", "«ve bu»", segments=wa("هٰذِهِ", "hadhihi", "pron")),
  tok("الثَّلَاثَةُ", "thalatha", "noun", [K, "badal"], "بَدَلٌ مِنْ هٰذِهِ مَرْفُوعٌ — أَكْتَعُ وَأَبْتَعُ وَأَبْصَعُ.", "«three» — aktaʿu, abtaʿu, abṣaʿu.", "«üçü» — ektau, ebtau, ebsau."),
  tok("أَتْبَاعٌ", "atba", "noun", [K, MK, JT, TK], "خَبَرٌ مَرْفُوعٌ.", "«followers» — the khabar.", "«tâbilerdir» — haber."),
  tok("لِأَجْمَعَ", "ajma-all", "noun", [K, HJ, "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَأَجْمَعَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of ajmaʿu» — a diptote, jarr by the fatḥa.", "«ecmau'nun» — gayr-ı munsarıf, fetha ile mecrûr.", punct="،", segments=[seg("لِ", "li", "prep"), seg("أَجْمَعَ", "ajma-all", "noun")]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, LN, MR, FL, F5], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَاحِدٌ مِنْهَا.", "«precedes» — any of them.", "«geçer» — biri."),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَلَى أَجْمَعَ.", "«it» — ajmaʿu.", "«onun önüne» — ecmau'nun.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«nor»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("تُذْكَرُ", "dhakara", "verb", [K, LN, NF, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«are they mentioned»", "«anılır»"),
  tok("بِدُونِهِ", "duna", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَدُونِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«without it»", "«onsuz»", segments=[seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun"), pr3msi()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْفَصِيحِ", "fasih", "noun", [K, HJ], "مَجْرُورٌ بِفِي — الْكَلَامِ الْفَصِيحِ.", "«eloquent speech»", "«fasih sözde»", punct="،"),
 ]})
# ----------- s3 — confirming the attached rafʿ pronoun by nafs/ʿayn
S.append({"id": "s3", "translation": {"en": "and when the attached rafʿ pronoun is confirmed by «nafs» and «ʿayn», it is first confirmed by a detached one — as in «Zayd struck, he himself» or «he his very self».", "tr": "muttasıl merfû zamir nefs ve ayn ile te'kîd edilince önce munfasılla te'kîd edilir — «Zeyd dövdü, o kendisi» veya «o bizzat kendisi» gibi."},
 "tokens": [
  tok("وَإِذَا", "idha", "part", [K, AT, IDH, MF], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -ince»", segments=wa("إِذَا", "idha", "part")),
  tok("أُكِّدَ", "akkada", "verb", [K, IDH, NF, F2, TK], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، فِعْلُ الشَّرْطِ.", "«is confirmed»", "«te'kîd edilince»"),
  tok("الْمُضْمَرُ", "mudmar", "noun", [K, NF, IMF, BM], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the pronoun»", "«zamir»"),
  tok("الْمَرْفُوعُ", "marfu", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«the rafʿ»", "«merfû»"),
  tok("الْمُتَّصِلُ", "muttasil", "noun", [K, NA, IFA, BM], "نَعْتٌ ثَانٍ مَرْفُوعٌ.", "«attached»", "«muttasıl»"),
  tok("بِالنَّفْسِ", "nafs", "noun", [K, HJ, TK], "الْبَاءُ حَرْفُ جَرٍّ، وَالنَّفْسِ مَجْرُورٌ.", "«by nafs»", "«nefs ile»", segments=[seg("بِ", "bi", "prep"), seg("النَّفْسِ", "nafs", "noun")]),
  tok("وَالْعَيْنِ", "ayn-thing", "noun", [K, AT, TK], "الْوَاوُ عَاطِفَةٌ، وَالْعَيْنِ مَعْطُوفٌ مَجْرُورٌ.", "«and ʿayn»", "«ve ayn»", segments=wa("الْعَيْنِ", "ayn-thing", "noun")),
  tok("أُكِّدَ", "akkada", "verb", [K, IDH, NF, F2], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«it is confirmed»", "«te'kîd edilir»"),
  tok("أَوَّلًا", "awwal", "noun", [K, MF], "ظَرْفٌ مَنْصُوبٌ — أَوَّلَ الْأَمْرِ.", "«first»", "«önce»"),
  tok("بِمُنْفَصِلٍ", "munfasil", "noun", [K, HJ, IFA, BM], "الْبَاءُ حَرْفُ جَرٍّ، وَمُنْفَصِلٍ مَجْرُورٌ — بِضَمِيرٍ مُنْفَصِلٍ.", "«by a detached one»", "«munfasıl ile»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("مُنْفَصِلٍ", "munfasil", "noun")]),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("ضَرَبَ", "daraba", "verb", [K, MK, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«struck» — the hidden doer; the clause the khabar.", "«dövdü» — gizli fâil; cümle haber."),
  tok("هُوَ", "huwa", "pron", [K, TK], "تَوْكِيدٌ لَفْظِيٌّ لِلضَّمِيرِ الْمُسْتَتِرِ فِي مَحَلِّ رَفْعٍ — التَّمْهِيدُ لِلنَّفْسِ.", "«he» — the detached confirmation, paving the way for nafs.", "«o» — munfasıl te'kîd; nefs'e zemin."),
  tok("نَفْسُهُ", "nafs", "noun", [K, TK, ID], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«himself» — the semantic tawkīd.", "«kendisi» — ma'nevî te'kîd.", segments=[seg("نَفْسُ", "nafs", "noun"), pr3ms()]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("عَيْنُهُ", "ayn-thing", "noun", [K, AT, TK, ID], "مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his very self»", "«bizzat kendisi»", punct=".", segments=[seg("عَيْنُ", "ayn-thing", "noun"), pr3ms()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "takrir": G("takrir", "تَكْرِير", "ك ر ر", "noun", "repetition — the maṣdar of karrara", "tekrar, tekrir — kerrara'nın mastarı", 3),
 "muradif": G("muradif", "مُرَادِف", "ر د ف", "noun", "a synonym (active participle of form III)", "eş anlamlı, müradif (III. babın ism-i fâili)", 3),
 "kilta": G("kilta", "كِلْتَا", "ك ل ت", "noun", "both (feminine) — the dual tawkīd", "her ikisi (dişil) — tesniye te'kîdi", 3),
 "ajma-all": G("ajma-all", "أَجْمَع", "ج م ع", "noun", "entire, all together — a word of semantic tawkīd (diptote)", "bütün, hepsi — ma'nevî te'kîd lafzı (gayr-ı munsarıf)", 3),
 "akta": G("akta", "أَكْتَع", "ك ت ع", "noun", "aktaʿu — a follower of ajmaʿu in tawkīd", "ektau — te'kîdde ecmau'nun tâbii", 4),
 "abta": G("abta", "أَبْتَع", "ب ت ع", "noun", "abtaʿu — a follower of ajmaʿu in tawkīd", "ebtau — te'kîdde ecmau'nun tâbii", 4),
 "absa": G("absa", "أَبْصَع", "ب ص ع", "noun", "abṣaʿu — a follower of ajmaʿu in tawkīd", "ebsau — te'kîdde ecmau'nun tâbii", 4),
 "fasih": G("fasih", "فَصِيح", "ف ص ح", "noun", "eloquent, pure (of speech)", "fasih, düzgün (söz)", 3, plural="فُصَحَاء"),
 "akkada": G("akkada", "أَكَّدَ", "أ ك د", "verb", "to confirm, to emphasize (form II)", "te'kîd etmek, pekiştirmek (II. bab)", 3, form="II"),
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
put_morph(mo, "akkada", {"bab": "الْبَابُ الثَّانِي فَعَّلَ — مَهْمُوزُ الْفَاءِ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَأْكِيد", "ismFail": "مُؤَكِّد",
 "mazi": ["أَكَّدَ", "أَكَّدَا", "أَكَّدُوا", "أَكَّدَتْ", "أَكَّدَتَا", "أَكَّدْنَ", "أَكَّدْتَ", "أَكَّدْتُمَا", "أَكَّدْتُمْ", "أَكَّدْتِ", "أَكَّدْتُمَا", "أَكَّدْتُنَّ", "أَكَّدْتُ", "أَكَّدْنَا"],
 "mudari": ["يُؤَكِّدُ", "يُؤَكِّدَانِ", "يُؤَكِّدُونَ", "تُؤَكِّدُ", "تُؤَكِّدَانِ", "يُؤَكِّدْنَ", "تُؤَكِّدُ", "تُؤَكِّدَانِ", "تُؤَكِّدُونَ", "تُؤَكِّدِينَ", "تُؤَكِّدَانِ", "تُؤَكِّدْنَ", "أُؤَكِّدُ", "نُؤَكِّدُ"],
 "amr": ["أَكِّدْ", "أَكِّدَا", "أَكِّدُوا", "أَكِّدِي", "أَكِّدَا", "أَكِّدْنَ"], "mansub": "يُؤَكِّدَ", "majzum": "يُؤَكِّدْ", "majzum2": "تُؤَكِّدْ",
 "note": "أَكَّدَ الْكَلَامَ يُؤَكِّدُهُ تَأْكِيدًا: قَوَّاهُ وَثَبَّتَهُ — مِنَ الْبَابِ الثَّانِي، مَهْمُوزُ الْفَاءِ، مُتَعَدٍّ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch50 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jara", "jaa", "daraba", "taqaddama", "dhakara") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "التَّأْكِيدُ اللَّفْظِيُّ بِالتَّكْرِيرِ، وَالْمَعْنَوِيُّ بِالنَّفْسِ وَالْعَيْنِ وَكِلَا وَكُلٍّ وَأَجْمَعَ وَأَتْبَاعِهِ", "en": "The verbal tawkīd by repetition, and the semantic by nafs, ʿayn, kilā, kull, ajmaʿ and its followers", "tr": "Tekrarla lafzî te'kîd; nefs, ayn, kilâ, küll, ecma' ve tâbileriyle ma'nevî te'kîd"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — التوابع: التأكيد", "الكافية لابن الحاجب — التأكيد", "شرح قطر الندى لابن هشام — التوكيد"],
 "amil": "the third follower, the tawkīd, is two kinds: the verbal, repeating the first word or its synonym (the attached pronoun confirmed by the detached), running through all words — جَاءَنِي زَيْدٌ زَيْدٌ، ضَرَبْتُ أَنْتَ، ضَرَبَ زَيْدٌ، زَيْدٌ قَائِمٌ قَائِمٌ (so printed); the semantic, for the maʿrifas only — نَفْسُهُ، عَيْنُهُ، كِلَاهُمَا، كِلْتَاهُمَا، كُلُّهُ، أَجْمَعُ، and its three followers أَكْتَعُ، أَبْتَعُ، أَبْصَعُ, never before it nor without it in eloquent speech; the attached rafʿ pronoun confirmed by نَفْس or عَيْن is first confirmed by a detached pronoun (زَيْدٌ ضَرَبَ هُوَ نَفْسُهُ)",
 "question": {
  "en": ["What is the verbal tawkīd? The repetition of the first word (جَاءَنِي زَيْدٌ زَيْدٌ، زَيْدٌ قَائِمٌ قَائِمٌ) or of its synonym — the attached pronoun repeated by the detached one; it runs through every kind of word: nouns, verbs, particles, sentences.",
         "How does the print give the pronoun examples? ضَرَبْتُ أَنْتَ and ضَرَبَ زَيْدٌ — the attached tāʾ confirmed by the detached pronoun and the hidden doer by the name; the chapter keeps the print's wording.",
         "What is the semantic tawkīd, and for what? The words that remove the doubt of figurative sense or of incompleteness — particular to the maʿrifas: نَفْسُهُ، عَيْنُهُ (the self), كِلَاهُمَا، كِلْتَاهُمَا (both), كُلُّهُ، أَجْمَعُ (all).",
         "What are أَكْتَعُ، أَبْتَعُ، أَبْصَعُ? Followers of أَجْمَعُ: they come after it in that order and never stand before it or without it in eloquent speech — جَاءَ الْقَوْمُ كُلُّهُمْ أَجْمَعُونَ أَكْتَعُونَ.",
         "How is the attached rafʿ pronoun confirmed by نَفْس? First by a detached pronoun: زَيْدٌ ضَرَبَ هُوَ نَفْسُهُ — not ضَرَبَ نَفْسُهُ, which would read as the doer.",
         "Why is the semantic tawkīd refused to the nakira? Because its words are annexed to a pronoun that must return to a known thing; an unknown cannot be confirmed as itself.",
         "What does the engine READ here? The DabtEngine reads the repeated name after the doer as its tawkīd in rafʿ, the repeated khabar as the khabar's tawkīd, the cited tawkīd words at the author's form, أَجْمَعَ after لِ in jarr by the fatḥa as a diptote, and هُوَ نَفْسُهُ after the hidden doer as detached and semantic tawkīd in rafʿ."],
  "tr": ["Lafzî te'kîd nedir? İlk lafzın tekrarı (câenî Zeydün Zeydün, Zeydün kâimün kâimün) ya da eş anlamlısının — muttasıl zamirin munfasılla tekrarı; her kelime türünde yürür: isim, fiil, harf, cümle.",
         "Baskı zamir örneklerini nasıl verir? Darabtü ente ve darabe Zeydün — muttasıl tâ munfasıl zamirle, gizli fâil isimle te'kîd edilmiş; bab baskının lafzını korur.",
         "Ma'nevî te'kîd nedir, ne içindir? Mecâz veya eksiklik vehmini kaldıran lafızlar — ma'rifelere mahsus: nefsühû, aynühû (kendisi), kilâhümâ, kiltâhümâ (her ikisi), küllühû, ecmau (hepsi).",
         "Ektau, ebtau, ebsau nedir? Ecmau'nun tâbileri: ondan sonra bu sırayla gelir, fasih sözde onun önünde ya da onsuz bulunmazlar — câe'l-kavmü küllühüm ecmaûne ekteûne.",
         "Muttasıl merfû zamir nefs ile nasıl te'kîd edilir? Önce munfasıl zamirle: Zeydün darabe hüve nefsühû — darabe nefsühû değil; o fâil okunurdu.",
         "Ma'nevî te'kîd nekreye neden verilmez? Çünkü lafızları bilinen bir şeye dönmesi gereken zamire muzâftır; bilinmeyen kendisi olarak te'kîd edilemez.",
         "Motor burada neyi OKUR? DabtEngine fâilden sonra tekrarlanan ismi ref'li te'kîd, tekrarlanan haberi haberin te'kîdi; alıntılanan te'kîd lafızlarını yazarın şeklinde; li'den sonraki ecmaa'yı gayr-ı munsarıf olarak fetha ile mecrûr; gizli fâilden sonraki hüve nefsühû'yu munfasıl ve ma'nevî te'kîd olarak ref'li okur."],
 },
 "plain": {"en": "Emphasis comes in two ways. Repeat the word itself («Zayd came, Zayd»), or add a fixed emphasis word to a definite noun: «himself», «his very self», «both», «all of it», «entire», with «aktaʿ, abtaʿ, abṣaʿ» trailing «entire». For «he himself struck», put the free pronoun first: «Zayd struck, he himself».",
           "tr": "Pekiştirme iki yolla olur. Sözü tekrar edersin («Zeyd geldi, Zeyd») ya da belirli isme sabit bir pekiştirme sözü eklersin: «kendisi», «bizzat kendisi», «her ikisi», «tamamı», «bütün»; «ektau, ebtau, ebsau» «bütün»ün ardından gelir. «Kendisi dövdü» için önce bağımsız zamiri koy: «Zeyd dövdü, o kendisi»."},
 "explanation": {"en": "The third follower is the tawkīd, of two kinds. The verbal is the repetition of the first word, or of its synonym in the case of the attached pronoun, and it runs through all words: جَاءَنِي زَيْدٌ زَيْدٌ، ضَرَبْتُ أَنْتَ، ضَرَبَ زَيْدٌ، زَيْدٌ قَائِمٌ قَائِمٌ — the print's examples, kept as printed. The semantic is particular to the maʿrifas: نَفْسُهُ، عَيْنُهُ، كِلَاهُمَا، كِلْتَاهُمَا، كُلُّهُ، أَجْمَعُ، أَكْتَعُ، أَبْتَعُ، أَبْصَعُ; the last three are followers of أَجْمَعُ — none precedes it, nor is any mentioned without it in eloquent speech. When the attached rafʿ pronoun is confirmed by نَفْس or عَيْن it is first confirmed by a detached pronoun: زَيْدٌ ضَرَبَ هُوَ نَفْسُهُ أَوْ عَيْنُهُ.",
                 "tr": "Üçüncü tâbi te'kîddir, iki kısımdır. Lafzî, ilk lafzın ya da muttasıl zamirde eş anlamlısının tekrarıdır ve bütün lafızlarda yürür: câenî Zeydün Zeydün, darabtü ente, darabe Zeydün, Zeydün kâimün kâimün — baskının örnekleri, basıldığı gibi. Ma'nevî, ma'rifelere mahsustur: nefsühû, aynühû, kilâhümâ, kiltâhümâ, küllühû, ecmau, ektau, ebtau, ebsau; son üçü ecmau'nun tâbileridir — fasih sözde onun önüne geçmez, onsuz da anılmazlar. Muttasıl merfû zamir nefs veya ayn ile te'kîd edilince önce munfasıl zamirle te'kîd edilir: Zeydün darabe hüve nefsühû ev aynühû."},
 "examples": [
  {"ar": "جَاءَنِي زَيْدٌ زَيْدٌ، وَزَيْدٌ قَائِمٌ قَائِمٌ", "en": "the verbal tawkīd by repetition", "tr": "tekrarla lafzî te'kîd", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "نَفْسُهُ وَعَيْنُهُ وَكِلَاهُمَا وَكِلْتَاهُمَا وَكُلُّهُ وَأَجْمَعُ وَأَكْتَعُ وَأَبْتَعُ وَأَبْصَعُ", "en": "the words of semantic tawkīd", "tr": "ma'nevî te'kîd lafızları", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "وَهٰذِهِ الثَّلَاثَةُ أَتْبَاعٌ لِأَجْمَعَ", "en": "the followers of ajmaʿu", "tr": "ecmau'nun tâbileri", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "زَيْدٌ ضَرَبَ هُوَ نَفْسُهُ أَوْ عَيْنُهُ", "en": "the detached pronoun before nafs", "tr": "nefs'ten önce munfasıl zamir", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٌ ضَرَبَ نَفْسُهُ (meaning «Zayd himself struck»)", "right": "زَيْدٌ ضَرَبَ هُوَ نَفْسُهُ", "why": {"en": "the attached rafʿ pronoun must first be confirmed by a detached one before نَفْس", "tr": "muttasıl merfû zamir nefs'ten önce munfasılla te'kîd edilmelidir"}},
  {"wrong": "جَاءَ الْقَوْمُ أَكْتَعُونَ أَجْمَعُونَ", "right": "جَاءَ الْقَوْمُ أَجْمَعُونَ أَكْتَعُونَ", "why": {"en": "aktaʿu follows ajmaʿu and never precedes it", "tr": "ektau ecmau'yu izler, önüne geçmez"}},
  {"wrong": "جَاءَنِي رَجُلٌ نَفْسُهُ", "right": "جَاءَنِي الرَّجُلُ نَفْسُهُ", "why": {"en": "the semantic tawkīd is particular to the maʿrifas", "tr": "ma'nevî te'kîd ma'rifelere mahsustur"}},
 ],
}
ADD_EN = (" Chapter 50 (print pp. 145-146): the tawkīd — verbal by repetition through all words (s1), semantic for the maʿrifas with its nine words and the followers of ajmaʿu (s2), the detached pronoun before nafs and ʿayn (s3).")
ADD_TR = (" Ellinci bab (baskı s. 145-146): te'kîd — bütün lafızlarda tekrarla lafzî (s1), dokuz lafzı ve ecmau'nun tâbileriyle ma'rifeler için ma'nevî (s2), nefs ve ayn'dan önce munfasıl zamir (s3).")
write_out(50, S, TITLE, ADD_EN, ADD_TR, "pp. 145-146", GLOSS_ADD, notes=(NOTE,),
          related=((K49, [K]), (TK, [K]), (TW, [K]), (BM, [K]), (TRF, [K])))
report(50, S, GLOSS_ADD, (NOTE,))
