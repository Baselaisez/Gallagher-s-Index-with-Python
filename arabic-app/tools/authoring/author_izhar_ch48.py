# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 48: the FOURTH kind, the relative — it must have a ṣila, a declarative sentence known to the hearer holding a pronoun
# returning to it, droppable on a clue; الَّذِي for the one, اللَّذَانِ in rafʿ and اللَّذَيْنِ in naṣb and jarr for its dual, الَّذِينَ in all three cases for its
# plural; الَّتِي for the one (f.), اللَّتَانِ / اللَّتَيْنِ for its dual, اللَّوَاتِي اللَّائِي اللَّاءِ اللَّآتِي اللَّاتِي اللَّوَائِي for its plural; ذَا after مَا of question;
# مَنْ، مَا، أَيٌّ، أَيَّةٌ; the alif-lām on the participles in the sense of الَّذِي / الَّتِي. The FIFTH kind, the lām-defined — of acquaintance (جَاءَنِي
# رَجُلٌ فَأَكْرَمْتُ الرَّجُلَ) or of genus (الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ); the vocative defines when a particular one is meant (يَا رَجُلُ). The SIXTH, what is
# annexed to one of these five by a semantic annexation (غُلَامُ زَيْدٍ). Print pp. 143–144. The lithograph's line reads «وَاللَّذَيْنِ فِي الْأَحْوَالِ الثَّلَاثِ»,
# dropping the plural; the Ottoman commentary (izhar-full-corrected l. 1560-1561) gives اللَّذَيْنِ for naṣb and jarr and الَّذِينَ for all three cases, which the text follows.
#   python3 author_izhar_ch48.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TRF = "tarif-al-musnad-ilayh"; MMB = "al-murab-wal-mabni-wal-irab"; ALT = "anwa-al-lam-al-tarif"; TBI = "tarif-bil-idafa"; VN = "vocative-munada"; JS = "jumla-sifa"; IDM = "idafa-definiteness"
K = "al-mawsul-wal-muarraf-bil-lam-wal-mudaf"
K47 = "asma-al-ishara-wa-sighuha"
TITLE = {"ar": "الْمَوْصُولُ وَصِلَتُهُ وَصِيَغُهُ، وَالْمُعَرَّفُ بِاللَّامِ، وَالْمُضَافُ إِلَى الْمَعْرِفَةِ", "en": "The relative, its ṣila and its forms; the lām-defined; and the noun annexed to a maʿrifa", "tr": "Mevsûl, sılası ve şekilleri; lâmla ma'rife; ma'rifeye muzâf"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def R(form, lex, en, tr, ar="لَفْظٌ مَحْكِيٌّ: اسْمٌ مَوْصُولٌ مَبْنِيٌّ.", punct=None, gr=None): return tok(form, lex, "pron", [K, MAW, MMB] + (gr or []), ar, en, tr, punct=punct)
def wR(form, lex, en, tr, punct=None, ar=None): return tok(form, lex, "pron", [K, AT, MAW, MMB], "الْوَاوُ عَاطِفَةٌ، وَ" + (ar or (form[2:] + " لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: اسْمٌ مَوْصُولٌ مَبْنِيٌّ.")), en, tr, punct=punct, segments=wa(form[2:], lex, "pron"))
def li_(form, lex, en, tr, punct=None, gr=None, segs=None): return tok(form, lex, "noun", [K, HJ] + (gr or []), "اللَّامُ حَرْفُ جَرٍّ، وَ" + form[2:] + " مَجْرُورٌ.", en, tr, punct=punct, segments=segs or [seg("لِ", "li", "prep"), seg(form[2:], lex, "noun")])
def wanaw(ord_ar, ord_lex, en_ord, tr_ord): return [tok("وَالنَّوْعُ", "naw", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالنَّوْعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the kind»", "«ve nev'»", segments=wa("النَّوْعُ", "naw", "noun")), tok(ord_ar, ord_lex, "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", en_ord, tr_ord)]

# ----------- s1 — the fourth kind: the relative and its ṣila
S.append({"id": "s1", "translation": {"en": "And the fourth kind is the relative, and it must have a ṣila: a declarative sentence known to the hearer, in which is a pronoun returning to the relative; and its dropping on a clue is allowed;", "tr": "Dördüncü nev' mevsûldür; sılası olmak zorundadır: dinleyenin bildiği, içinde mevsûle dönen bir zamir bulunan haber cümlesi; karîne ile hazfi de câizdir;"},
 "tokens": [
  *wanaw("الرَّابِعُ", "rabi-fourth", "«fourth»", "«dördüncü»"),
  tok("الْمَوْصُولُ", "mawsul", "noun", [K, MK, IMF, MAW, TRF], "خَبَرٌ مَرْفُوعٌ.", "«the relative» — the khabar.", "«mevsûl» — haber.", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no»", "«ve … yok»", segments=wa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, LN, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«escape» — it must.", "«çâre» — zorunlu."),
  tok("لَهُ", "li", "prep", [K, HJ, LN], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«for it» — the khabar of lā.", "«onun için» — lâ'nın haberi.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-dan»"),
  tok("صِلَةٍ", "sila", "noun", [K, HJ, MAW], "مَجْرُورٌ بِمِنْ.", "«a ṣila»", "«bir sıla»", punct=":"),
  tok("جُمْلَةٍ", "jumla", "noun", [K, "badal", MAW], "بَدَلٌ مِنْ صِلَةٍ مَجْرُورٌ — أَوْ عَطْفُ بَيَانٍ.", "«a sentence» — the badal of ṣila.", "«bir cümle» — sılanın bedeli."),
  tok("خَبَرِيَّةٍ", "khabariyya", "noun", [K, NA, NSB], "نَعْتٌ مَجْرُورٌ.", "«declarative»", "«haber cümlesi»"),
  tok("مَعْلُومَةٍ", "malum", "noun", [K, NA, IMF], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«known»", "«bilinen»"),
  li_("لِلسَّامِعِ", "sami-hearer", "«to the hearer»", "«dinleyence»", gr=[IFA], punct="،"),
  tok("فِيهَا", "fi", "prep", [K, HJ, MK], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ نَعْتٌ ثَالِثٌ.", "«in which» — a fronted khabar; the clause a third naʿt.", "«içinde» — öne alınmış haber; cümle üçüncü sıfat.", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  tok("ضَمِيرٌ", "damir", "noun", [K, MK, MAW], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a pronoun»", "«bir zamir»"),
  tok("عَائِدٌ", "aid", "noun", [K, NA, IFA, MAW], "نَعْتٌ مَرْفُوعٌ.", "«returning»", "«dönen»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْمَوْصُولِ", "mawsul", "noun", [K, HJ, IMF, MAW], "مَجْرُورٌ بِإِلَى.", "«the relative»", "«mevsûle»", punct="،"),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("حَذْفُهُ", "hadhf", "noun", [K, FL, ID, MSD, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدِ.", "«its dropping» — the returner's.", "«hazfi» — âidin.", segments=[seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«where stands»", "«bulununca»"),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»", punct="،"),
 ]})
# ----------- s2 — the masculine forms
S.append({"id": "s2", "translation": {"en": "and it is: «alladhī» for the one, and for its dual «alladhāni» in the state of rafʿ and «alladhayni» in naṣb and jarr, and «alladhīna» for its plural in the three states;", "tr": "o: tek için ellezî; tesniyesi için ref' hâlinde ellezâni, nasb ve cerde ellezeyni; cemi için üç hâlde de ellezîne;"},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o»", punct=":", segments=wa("هُوَ", "huwa", "pron")),
  R("الَّذِي", "alladhi", "«alladhī» — who, which", "«ellezî» — ki o", ar="لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ، خَبَرٌ — اسْمٌ مَوْصُولٌ مَبْنِيٌّ."),
  li_("لِلْوَاحِدِ", "wahid", "«for the one»", "«tek için»", punct="،"),
  tok("وَلِمُثَنَّاهُ", "muthanna", "noun", [K, AT, HJ, ID, MTH, MQ], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمُثَنَّاهُ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«and for its dual»", "«ve tesniyesi için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مُثَنَّا", "muthanna", "noun"), pr3ms()]),
  R("اللَّذَانِ", "alladhi", "«alladhāni»", "«ellezâni»", ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — مُثَنَّى الَّذِي.", gr=[MTH]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("حَالَةِ", "hala-state", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the state of»", "«hâlinde»"),
  tok("الرَّفْعِ", "raf", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rafʿ»", "«ref'»"),
  wR("وَاللَّذَيْنِ", "alladhi", "«and alladhayni»", "«ve ellezeyni»", ar="اللَّذَيْنِ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مُثَنَّى الَّذِي بِالْيَاءِ."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("النَّصْبِ", "nasb", "noun", [K, HJ, MSD], "مَجْرُورٌ بِفِي.", "«naṣb»", "«nasb»"),
  tok("وَالْجَرِّ", "jarr", "noun", [K, AT, MSD], "الْوَاوُ عَاطِفَةٌ، وَالْجَرِّ مَعْطُوفٌ مَجْرُورٌ.", "«and jarr»", "«ve cer»", punct="،", segments=wa("الْجَرِّ", "jarr", "noun")),
  tok("وَلِجَمْعِهِ", "jam", "noun", [K, AT, HJ, ID, "jam"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَجَمْعِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«and for its plural»", "«ve cemi için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("جَمْعِ", "jam", "noun"), pr3msi()]),
  R("الَّذِينَ", "alladhina", "«alladhīna»", "«ellezîne»", ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — جَمْعُ الَّذِي، بِالْيَاءِ فِي كُلِّ حَالٍ."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَحْوَالِ", "hal", "noun", [K, HJ, JT], "مَجْرُورٌ بِفِي.", "«the states»", "«hâllerde»"),
  tok("الثَّلَاثِ", "thalatha", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«three»", "«üç»", punct="،"),
 ]})
# ----------- s3 — the feminine forms; dhā, man, mā, ayy; the alif-lām
S.append({"id": "s3", "translation": {"en": "and «allatī» for the one woman, and for its dual «allatāni» and «allatayni», and for its plural «allawātī», «allāʾī», «allāʾi», «allāti», «allātī», «allawāʾī»; and «dhā» after the «mā» of question; and «man», «mā», «ayyun», «ayyatun»; and the alif and lām on the active and passive participles, in the sense of «alladhī» or «allatī».", "tr": "tek kadın için elletî; tesniyesi için elletâni ve elleteyni; cemi için ellevâtî, ellâî, ellâi, ellâti, ellâtî, ellevâî; soru mâ'sından sonra zâ; men, mâ, eyyün, eyyetün; ism-i fâil ve ism-i mef'ûldeki ellezî veya elletî mânâsındaki elif-lâm."},
 "tokens": [
  wR("وَالَّتِي", "allati", "«and allatī»", "«ve elletî»", ar="الَّتِي لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: اسْمٌ مَوْصُولٌ مَبْنِيٌّ لِلْمُؤَنَّثِ."),
  li_("لِلْوَاحِدَةِ", "wahid", "«for the one woman»", "«tek kadın için»", punct="،"),
  tok("وَلِمُثَنَّاهَا", "muthanna", "noun", [K, AT, HJ, ID, MTH, MQ], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمُثَنَّاهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and for its dual»", "«ve tesniyesi için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مُثَنَّا", "muthanna", "noun"), pr3fs()]),
  R("اللَّتَانِ", "allati", "«allatāni»", "«elletâni»", ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — مُثَنَّى الَّتِي فِي الرَّفْعِ.", gr=[MTH]),
  wR("وَاللَّتَيْنِ", "allati", "«and allatayni»", "«ve elleteyni»", punct="،", ar="اللَّتَيْنِ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مُثَنَّى الَّتِي فِي النَّصْبِ وَالْجَرِّ."),
  tok("وَلِجَمْعِهَا", "jam", "noun", [K, AT, HJ, ID, "jam"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَجَمْعِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and for its plural»", "«ve cemi için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("جَمْعِ", "jam", "noun"), pr3fs()]),
  R("اللَّوَاتِي", "allati", "«allawātī»", "«ellevâtî»", ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — جَمْعُ الَّتِي."),
  wR("وَاللَّائِي", "allati", "«and allāʾī»", "«ve ellâî»"), wR("وَاللَّاءِ", "allati", "«and allāʾi»", "«ve ellâi»"), wR("وَاللَّآتِي", "allati", "«and allāti»", "«ve ellâti»"), wR("وَاللَّاتِي", "allati", "«and allātī»", "«ve ellâtî»"), wR("وَاللَّوَائِي", "allati", "«and allawāʾī»", "«ve ellevâî»", punct="،"),
  wR("وَذَا", "dha", "«and dhā»", "«ve zâ»", ar="ذَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — اسْمٌ مَوْصُولٌ لَا إِشَارَةٌ."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("مَا", "ma-istifhamiyya", "pron", [K, ID, IST], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«the mā»", "«mâ'dan»"),
  tok("الِاسْتِفْهَامِيَّةِ", "istifhamiyya", "noun", [K, NA, NSB, IST], "نَعْتٌ مَجْرُورٌ — مَاذَا صَنَعْتَ.", "«of question» — مَاذَا صَنَعْتَ.", "«istifhâm» — mâzâ sana'te.", punct="،"),
  wR("وَمَنْ", "man", "«and man» — who", "«ve men» — kim", ar="مَنْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: اسْمٌ مَوْصُولٌ لِلْعَاقِلِ."),
  wR("وَمَا", "ma-mawsula", "«and mā» — what", "«ve mâ» — ne", ar="مَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: اسْمٌ مَوْصُولٌ لِغَيْرِ الْعَاقِلِ."),
  wR("وَأَيٌّ", "ayy", "«and ayyun» — whichever", "«ve eyyün» — hangisi", ar="أَيٌّ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — الْمَوْصُولُ الْمُعْرَبُ."),
  wR("وَأَيَّةٌ", "ayy", "«and ayyatun»", "«ve eyyetün»", punct="،", ar="أَيَّةٌ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مُؤَنَّثُ أَيٍّ."),
  tok("وَالْأَلِفُ", "alif-letter", "noun", [K, AT, MK, ALT], "الْوَاوُ عَاطِفَةٌ، وَالْأَلِفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the alif»", "«ve elif»", segments=wa("الْأَلِفُ", "alif-letter", "noun")),
  tok("وَاللَّامُ", "lam-letter", "noun", [K, AT, ALT], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the lām»", "«ve lâm»", segments=wa("اللَّامُ", "lam-letter", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-deki»"),
  tok("اسْمِ", "ism", "noun", [K, HJ, ID, IFA], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the noun of»", "«ism-i»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer» — the active participle.", "«fâil»"),
  tok("وَالْمَفْعُولِ", "maful-noun", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَالْمَفْعُولِ مَعْطُوفٌ مَجْرُورٌ — اسْمِ الْمَفْعُولِ.", "«and the passive participle»", "«ve ism-i mef'ûl»", segments=wa("الْمَفْعُولِ", "maful-noun", "noun")),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — خَبَرُ الْأَلِفُ وَاللَّامُ.", "«in the sense of» — the khabar.", "«mânâsında» — haber.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  R("الَّذِي", "alladhi", "«alladhī»", "«ellezî»", ar="لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  R("الَّتِي", "allati", "«allatī»", "«elletî»", ar="لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — الضَّارِبُ: الَّذِي ضَرَبَ.", punct="."),
 ]})
# ----------- s4 — the fifth kind: the lām-defined; the vocative
S.append({"id": "s4", "translation": {"en": "And the fifth kind is the lām-defined, whether it be for acquaintance — as in «a man came to me, and I honoured the man» — or for genus — as in «man is better than woman»; and the vocative defines, when a particular one is meant by it — as in «O man».", "tr": "Beşinci nev' lâmla ma'rife olandır; ister ahd için olsun — «bana bir adam geldi, adama ikram ettim» gibi — ister cins için — «erkek kadından hayırlıdır» gibi; muayyen biri kastedilince nidâ da ma'rife kılar — «ey adam» gibi."},
 "tokens": [
  *wanaw("الْخَامِسُ", "khamis", "«fifth»", "«beşinci»"),
  tok("الْمُعَرَّفُ", "muarraf", "noun", [K, MK, IMF, F2, ALT, TRF], "خَبَرٌ مَرْفُوعٌ.", "«the defined» — the khabar.", "«ma'rife kılınan» — haber."),
  tok("بِاللَّامِ", "lam-letter", "noun", [K, HJ, ALT], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّامِ مَجْرُورٌ — لَامُ التَّعْرِيفِ.", "«by the lām» — of definition.", "«lâmla» — ta'rif lâmı.", segments=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  tok("سَوَاءٌ", "sawa", "noun", [K, MK, "ism-mamdud"], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ — سَوَاءٌ كَوْنُهُ لِلْعَهْدِ أَوْ لِلْجِنْسِ.", "«whether» — alike.", "«ister» — müsâvî."),
  tok("كَانَ", "kana", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — الْمُعَرَّفُ.", "«it be»", "«olsun»"),
  li_("لِلْعَهْدِ", "ahd", "«for acquaintance»", "«ahd için»", gr=[KN, ALT]),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("رَجُلٌ", "rajul", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ — نَكِرَةٌ أَوَّلًا.", "«a man» — a nakira first.", "«bir adam» — önce nekre."),
  tok("فَأَكْرَمْتُ", "akrama", "verb", [K, AT, FL, F4], "الْفَاءُ عَاطِفَةٌ، وَأَكْرَمْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I honoured»", "«ve ikram ettim»", segments=[seg("فَ", "fa", "conj"), seg("أَكْرَمْ", "akrama", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("الرَّجُلَ", "rajul", "noun", [K, MB, ALT], "مَفْعُولٌ بِهِ مَنْصُوبٌ — مُعَرَّفٌ بِلَامِ الْعَهْدِ: الرَّجُلُ الْمَذْكُورُ.", "«the man» — the lām of acquaintance: the man just mentioned.", "«adama» — ahd lâmı: anılan adam."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  li_("لِلْجِنْسِ", "jins", "«for genus»", "«cins için»", gr=[AT, ALT], punct="،"),
  nahw(),
  tok("الرَّجُلُ", "rajul", "noun", [K, MK, ALT], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ — مُعَرَّفٌ بِلَامِ الْجِنْسِ.", "«man» — the lām of genus.", "«erkek» — cins lâmı."),
  tok("خَيْرٌ", "khayr", "noun", [K, MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«better»", "«hayırlıdır»"),
  tok("مِنَ", "min", "prep", [K, HJ, "ism-tafdil"], "حَرْفُ جَرٍّ.", "«than»", "«-dan»"),
  tok("الْمَرْأَةِ", "imraa", "noun", [K, HJ, ALT], "مَجْرُورٌ بِمِنْ.", "«woman»", "«kadın»", punct="،"),
  tok("وَتُعَرِّفُ", "arrafa", "verb", [K, AT, MR, FL, F2], "الْوَاوُ عَاطِفَةٌ، وَتُعَرِّفُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and defines»", "«ve ma'rife kılar»", segments=wa("تُعَرِّفُ", "arrafa", "verb")),
  tok("النِّدَاءُ", "nida", "noun", [K, FL, VN, MSD], "فَاعِلٌ مَرْفُوعٌ.", "«the vocative»", "«nidâ»"),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ince»"),
  tok("قُصِدَ", "qasada", "verb", [K, NF, "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is meant»", "«kastedilince»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — بِالنِّدَاءِ.", "«by it» — by the vocative.", "«onunla» — nidâ ile."),
  tok("مُعَيَّنٌ", "muayyan", "noun", [K, NF, IMF, F2], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a particular one»", "«muayyen biri»", punct="،"),
  nahw(),
  tok("يَا", "ya-nida", "part", [K, VN], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("رَجُلُ", "rajul", "noun", [K, VN, MMB], "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — نَكِرَةٌ مَقْصُودَةٌ تَعَرَّفَتْ بِالنِّدَاءِ.", "«man» — an intended nakira, defined by the call.", "«adam» — nidâ ile ma'rife olmuş nekre-i maksûde.", punct="."),
 ]})
# ----------- s5 — the sixth kind: the annexed
S.append({"id": "s5", "translation": {"en": "And the sixth kind is what is annexed to one of these five by a semantic annexation — as in «the servant of Zayd».", "tr": "Altıncı nev' bu beşten birine ma'nevî izâfetle muzâf olandır — «Zeyd'in kölesi» gibi."},
 "tokens": [
  *wanaw("السَّادِسُ", "sadis", "«sixth»", "«altıncı»"),
  tok("الْمُضَافُ", "mudaf", "noun", [K, MK, IMF, TBI, IDM], "خَبَرٌ مَرْفُوعٌ.", "«the annexed» — the khabar.", "«muzâf» — haber."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("أَحَدِ", "ahad", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«one of»", "«birine»"),
  tok("هٰذِهِ", "hadhihi", "pron", [K, ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«these»", "«bu»"),
  tok("الْخَمْسَةِ", "khamsa", "noun", [K, "badal"], "بَدَلٌ مِنْ هٰذِهِ مَجْرُورٌ — أَوْ عَطْفُ بَيَانٍ.", "«five»", "«beşten»"),
  tok("إِضَافَةً", "idafa", "noun", [K, "maful-mutlaq", MSD, F4, IDM], "مَفْعُولٌ مُطْلَقٌ لِلْمُضَافِ مَنْصُوبٌ.", "«by an annexation»", "«izâfetle»"),
  tok("مَعْنَوِيَّةً", "manawi", "noun", [K, NA, NSB, TBI], "نَعْتٌ مَنْصُوبٌ — لَا لَفْظِيَّةً كَضَارِبِ زَيْدٍ.", "«semantic» — not the verbal one of ضَارِبِ زَيْدٍ.", "«ma'nevî» — dâribi Zeydin'deki lafzî değil.", punct="،"),
  nahw(),
  tok("غُلَامُ", "ghulam", "noun", [K, MK, ID, TBI], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — تَعَرَّفَ بِالْإِضَافَةِ إِلَى الْعَلَمِ.", "«the servant of» — defined by annexation to the name.", "«kölesi» — aleme izâfetle ma'rife."),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "hala-state": G("hala-state", "حَالَة", "ح و ل", "noun", "a state, a case (of iʿrāb)", "hâl, durum (i'râb hâli)", 3, plural="حَالَات"),
 "muayyan": G("muayyan", "مُعَيَّن", "ع ي ن", "noun", "specified, particular (passive participle of form II)", "muayyen, belirli (II. babın ism-i mef'ûlü)", 3),
 "arrafa": G("arrafa", "عَرَّفَ", "ع ر ف", "verb", "to make definite, to define (form II)", "ma'rife kılmak, tarif etmek (II. bab)", 3, form="II"),
 "hadhihi": G("hadhihi", "هٰذِهِ", "ه ذ", "pron", "this (feminine demonstrative)", "bu (dişil işaret ismi)", 1),
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
put_morph(mo, "arrafa", {"bab": "الْبَابُ الثَّانِي فَعَّلَ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَعْرِيف", "ismFail": "مُعَرِّف",
 "mazi": ["عَرَّفَ", "عَرَّفَا", "عَرَّفُوا", "عَرَّفَتْ", "عَرَّفَتَا", "عَرَّفْنَ", "عَرَّفْتَ", "عَرَّفْتُمَا", "عَرَّفْتُمْ", "عَرَّفْتِ", "عَرَّفْتُمَا", "عَرَّفْتُنَّ", "عَرَّفْتُ", "عَرَّفْنَا"],
 "mudari": ["يُعَرِّفُ", "يُعَرِّفَانِ", "يُعَرِّفُونَ", "تُعَرِّفُ", "تُعَرِّفَانِ", "يُعَرِّفْنَ", "تُعَرِّفُ", "تُعَرِّفَانِ", "تُعَرِّفُونَ", "تُعَرِّفِينَ", "تُعَرِّفَانِ", "تُعَرِّفْنَ", "أُعَرِّفُ", "نُعَرِّفُ"],
 "amr": ["عَرِّفْ", "عَرِّفَا", "عَرِّفُوا", "عَرِّفِي", "عَرِّفَا", "عَرِّفْنَ"], "mansub": "يُعَرِّفَ", "majzum": "يُعَرِّفْ", "majzum2": "تُعَرِّفْ",
 "note": "عَرَّفَ الِاسْمَ يُعَرِّفُهُ تَعْرِيفًا: جَعَلَهُ مَعْرِفَةً — مِنَ الْبَابِ الثَّانِي، مُتَعَدٍّ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch48 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "jaa", "akrama", "qasada") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَوْصُولُ وَصِلَتُهُ وَعَائِدُهُ وَصِيَغُهُ؛ الْمُعَرَّفُ بِلَامِ الْعَهْدِ وَالْجِنْسِ وَبِالنِّدَاءِ؛ الْمُضَافُ إِلَى الْمَعْرِفَةِ", "en": "The relative, its ṣila, returner and forms; the lām of acquaintance and of genus and the vocative; the noun annexed to a maʿrifa", "tr": "Mevsûl, sılası, âidi ve şekilleri; ahd ve cins lâmı ve nidâ ile ma'rife; ma'rifeye muzâf"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المعرفة: الموصول والمعرف باللام والمضاف", "الكافية لابن الحاجب — الموصولات، المعرف باللام", "شرح قطر الندى لابن هشام — الموصول وأل"],
 "amil": "the fourth maʿrifa, the relative, needs a ṣila — a declarative sentence known to the hearer with a pronoun returning to the relative, droppable on a clue; its forms: الَّذِي, dual اللَّذَانِ (rafʿ) / اللَّذَيْنِ (naṣb, jarr), plural الَّذِينَ (all cases); الَّتِي, dual اللَّتَانِ / اللَّتَيْنِ, plural اللَّوَاتِي اللَّائِي اللَّاءِ اللَّآتِي اللَّاتِي اللَّوَائِي; ذَا after the مَا of question (مَاذَا); مَنْ، مَا، أَيٌّ، أَيَّةٌ; and the alif-lām on the participles in the sense of الَّذِي / الَّتِي; the fifth, the lām-defined — of acquaintance (فَأَكْرَمْتُ الرَّجُلَ) or genus (الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ) — and the vocative defining an intended nakira (يَا رَجُلُ); the sixth, what is annexed to one of these five by a semantic annexation (غُلَامُ زَيْدٍ)",
 "question": {
  "en": ["What must a relative have? A ṣila: a declarative sentence the hearer already knows, holding a pronoun that returns to the relative — droppable on a clue (الَّذِي ضَرَبْتُ for الَّذِي ضَرَبْتُهُ).",
         "What are the masculine forms? الَّذِي; اللَّذَانِ in rafʿ and اللَّذَيْنِ in naṣb and jarr; الَّذِينَ in all three cases — the plural keeps one shape.",
         "And the feminine? الَّتِي; اللَّتَانِ and اللَّتَيْنِ; the plurals اللَّوَاتِي، اللَّائِي، اللَّاءِ، اللَّآتِي، اللَّاتِي، اللَّوَائِي.",
         "Which other words are relatives? ذَا after the question's مَا (مَاذَا صَنَعْتَ = مَا الَّذِي صَنَعْتَ), مَنْ for the rational, مَا for the rest, أَيٌّ and أَيَّةٌ (the only declinable relative), and the alif-lām on the participles (الضَّارِبُ = الَّذِي ضَرَبَ).",
         "What is the lām of acquaintance, and of genus? Acquaintance: جَاءَنِي رَجُلٌ فَأَكْرَمْتُ الرَّجُلَ — the man just mentioned; genus: الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ — the kind as a whole.",
         "How does the vocative define? When a particular one is meant: يَا رَجُلُ — the nakira becomes definite by the call and is built on ḍamm.",
         "What is the sixth maʿrifa? The noun annexed to one of the five by a semantic annexation: غُلَامُ زَيْدٍ — the verbal annexation (ضَارِبُ زَيْدٍ) does not define.",
         "What does the engine READ here? The DabtEngine keeps every cited relative at the author's form as a built word, reads the لِ-phrases as fronted khabars with the cited form as the delayed mubtadaʾ, فَأَكْرَمْتُ الرَّجُلَ as verb and object, الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ as mubtadaʾ, comparative khabar and مِنْ-phrase, يَا رَجُلُ as the munādā on ḍamm, and غُلَامُ زَيْدٍ as muḍāf and muḍāf ilayh."],
  "tr": ["Mevsûlde ne olmalıdır? Sıla: dinleyenin zaten bildiği, mevsûle dönen bir zamir taşıyan haber cümlesi — karîne ile hazfedilebilir (ellezî darabtühû yerine ellezî darabtü).",
         "Müzekker şekiller nelerdir? Ellezî; ref'te ellezâni, nasb ve cerde ellezeyni; üç hâlde de ellezîne — cemi tek şekil korur.",
         "Müennes? Elletî; elletâni ve elleteyni; cemiler ellevâtî, ellâî, ellâi, ellâti, ellâtî, ellevâî.",
         "Başka hangi kelimeler mevsûldür? Soru mâ'sından sonra zâ (mâzâ sana'te = me'llezî sana'te), akıllı için men, diğeri için mâ, eyyün ve eyyetün (tek mu'rab mevsûl) ve ism-i fâil/mef'ûl üzerindeki elif-lâm (ed-dâribü = ellezî darabe).",
         "Ahd lâmı ve cins lâmı nedir? Ahd: câenî racülün fe-ekramtü'r-racüle — az önce anılan adam; cins: er-racülü hayrun mine'l-mer'eti — tür bütünüyle.",
         "Nidâ nasıl ma'rife kılar? Muayyen biri kastedilince: yâ racülü — nekre nidâ ile ma'rife olur ve damme üzere mebnî olur.",
         "Altıncı ma'rife nedir? Beşten birine ma'nevî izâfetle muzâf isim: gulâmu Zeydin — lafzî izâfet (dâribu Zeydin) ma'rife kılmaz.",
         "Motor burada neyi OKUR? DabtEngine alıntılanan her mevsûlü mebnî kelime olarak yazarın şeklinde tutar; li-öbeklerini sona alınmış mübtedâlı öne alınmış haber; fe-ekramtü'r-racüle'yi fiil ve mef'ûl; er-racülü hayrun mine'l-mer'eti'yi mübtedâ, tafdîl haberi ve min öbeği; yâ racülü'yü damme üzere münâdâ; gulâmu Zeydin'i muzâf ve muzâfun ileyh okur."],
 },
 "plain": {"en": "A relative («who, which») needs a clause the listener knows, with a pronoun pointing back: alladhī, allatī and their duals and plurals, plus man, mā, ayy and «al-» on participles. «The» points to someone just mentioned or to a whole kind; calling someone («O man») makes the word definite, as does «Zayd's servant».",
           "tr": "İlgi adılı («ki o») dinleyenin bildiği, geriye işaret eden zamirli bir cümle ister: ellezî, elletî, tesniye ve cemileri; men, mâ, eyy ve ism-i fâillerdeki «el-». «El-» az önce anılana ya da bütün türe işaret eder; seslenmek («ey adam») sözü belirli kılar; belirli bir söze eklemek («Zeyd'in kölesi») de."},
 "explanation": {"en": "The fourth kind of maʿrifa is the relative. It must have a ṣila: a declarative sentence known to the hearer, holding a pronoun that returns to the relative; the pronoun may be dropped on a clue. The relatives are الَّذِي for the one, اللَّذَانِ in the state of rafʿ and اللَّذَيْنِ in naṣb and jarr for its dual, الَّذِينَ in the three states for its plural; الَّتِي for the one woman, اللَّتَانِ and اللَّتَيْنِ for its dual, اللَّوَاتِي، اللَّائِي، اللَّاءِ، اللَّآتِي، اللَّاتِي، اللَّوَائِي for its plural; ذَا after the مَا of question; مَنْ، مَا، أَيٌّ، أَيَّةٌ; and the alif and lām on the active and passive participles, in the sense of الَّذِي or الَّتِي. The fifth kind is the lām-defined, whether for acquaintance (جَاءَنِي رَجُلٌ فَأَكْرَمْتُ الرَّجُلَ) or for genus (الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ); and the vocative defines when a particular one is meant (يَا رَجُلُ). The sixth kind is what is annexed to one of these five by a semantic annexation (غُلَامُ زَيْدٍ). The lithograph's line gives «اللَّذَيْنِ in the three states», dropping the plural; the Ottoman commentary's reading is followed.",
                 "tr": "Ma'rifenin dördüncü nev'i mevsûldür. Sılası olmak zorundadır: dinleyenin bildiği, mevsûle dönen bir zamir taşıyan haber cümlesi; zamir karîne ile hazfedilebilir. Mevsûller: tek için ellezî, tesniyesi için ref' hâlinde ellezâni, nasb ve cerde ellezeyni, cemi için üç hâlde ellezîne; tek kadın için elletî, tesniyesi için elletâni ve elleteyni, cemi için ellevâtî, ellâî, ellâi, ellâti, ellâtî, ellevâî; soru mâ'sından sonra zâ; men, mâ, eyyün, eyyetün; ism-i fâil ve ism-i mef'ûl üzerindeki ellezî veya elletî mânâsındaki elif-lâm. Beşinci nev' lâmla ma'rife olandır; ahd için (câenî racülün fe-ekramtü'r-racüle) veya cins için (er-racülü hayrun mine'l-mer'eti); muayyen biri kastedilince nidâ da ma'rife kılar (yâ racülü). Altıncı nev' bu beşten birine ma'nevî izâfetle muzâf olandır (gulâmu Zeydin). Taşbaskının satırı «üç hâlde ellezeyni» diyerek cemiyi atlar; Osmanlıca şerhin okuyuşu izlenir."},
 "examples": [
  {"ar": "وَلَا بُدَّ لَهُ مِنْ صِلَةٍ: جُمْلَةٍ خَبَرِيَّةٍ مَعْلُومَةٍ لِلسَّامِعِ فِيهَا ضَمِيرٌ عَائِدٌ", "en": "the ṣila and its returner", "tr": "sıla ve âidi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "الَّذِي، اللَّذَانِ، اللَّذَيْنِ، الَّذِينَ", "en": "the masculine relatives", "tr": "müzekker mevsûller", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "الَّتِي، اللَّتَانِ، اللَّتَيْنِ، اللَّوَاتِي … وَذَا بَعْدَ مَا، وَمَنْ وَمَا وَأَيٌّ", "en": "the feminine relatives and the rest", "tr": "müennes mevsûller ve diğerleri", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "جَاءَنِي رَجُلٌ فَأَكْرَمْتُ الرَّجُلَ؛ الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ؛ يَا رَجُلُ", "en": "the lām of acquaintance, of genus, and the vocative", "tr": "ahd lâmı, cins lâmı ve nidâ", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "غُلَامُ زَيْدٍ", "en": "the noun annexed to a maʿrifa", "tr": "ma'rifeye muzâf", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "رَأَيْتُ اللَّذَانِ", "right": "رَأَيْتُ اللَّذَيْنِ", "why": {"en": "the dual relative shows naṣb and jarr by the yāʾ", "tr": "tesniye mevsûl nasb ve cerri yâ ile gösterir"}},
  {"wrong": "جَاءَنِي الَّذِي قَامَ زَيْدٌ", "right": "جَاءَنِي الَّذِي قَامَ أَبُوهُ", "why": {"en": "the ṣila must hold a pronoun returning to the relative", "tr": "sıla mevsûle dönen bir zamir taşımalıdır"}},
  {"wrong": "ضَارِبُ زَيْدٍ counted as a maʿrifa", "right": "غُلَامُ زَيْدٍ is the maʿrifa by annexation", "why": {"en": "only the semantic annexation defines; the verbal one (participle + object) does not", "tr": "yalnız ma'nevî izâfet ma'rife kılar; lafzî (ism-i fâil + mef'ûl) kılmaz"}},
 ],
}
ADD_EN = (" Chapter 48 (print pp. 143-144): the relative and its ṣila (s1), the masculine forms (s2), the feminine forms, dhā after mā, man, mā, ayy and the alif-lām (s3); the lām of acquaintance and of genus and the vocative (s4); the noun annexed to a maʿrifa (s5).")
ADD_TR = (" Kırk sekizinci bab (baskı s. 143-144): mevsûl ve sılası (s1), müzekker şekiller (s2), müennes şekiller, mâ'dan sonra zâ, men, mâ, eyy ve elif-lâm (s3); ahd ve cins lâmı ve nidâ (s4); ma'rifeye muzâf (s5).")
write_out(48, S, TITLE, ADD_EN, ADD_TR, "pp. 143-144", GLOSS_ADD, notes=(NOTE,),
          related=((K47, [K]), (MAW, [K]), (ALT, [K]), (TBI, [K]), (VN, [K]), (TRF, [K]), (IDM, [K])))
report(48, S, GLOSS_ADD, (NOTE,))
