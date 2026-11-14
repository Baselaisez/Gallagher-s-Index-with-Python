# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 56: the QIYĀSĪ ghayr munṣarif, second half — every proper name with the feminine tāʾ in wording (فَاطِمَةَ، حَمْزَةَ)
# or in estimation when over three letters (زَيْنَبَ) or vowelled in the middle as a woman's name (قَدَمَ) — declined if a male is so named; the three-lettered
# feminine name with a still middle may be declined or barred (هِنْدَ); every name compounded of two nouns neither governing the other, the second no sound
# and no particle-sense (بَعْلَبَكَّ، حَضْرَمَوْتَ); everything with an added alif and nūn as a name or a description that takes no tāʾ (عِمْرَانَ، سَكْرَانَ، رَحْمٰنَ);
# every plural on faʿālil or faʿālīl (مَسَاجِدَ، مَصَابِيحَ) — declinable for the necessity of verse or for assonance (سَلَاسِلًا، قَوَارِيرًا, al-Insān 76:4, 15);
# and every diptote declines when annexed or given the lām of definition (مَرَرْتُ بِالْأَحْمَرِ وَأَحْمَرِنَا). Print p. 151.
# Readings: the lithograph writes رحمن without the alif, given as رَحْمٰنَ; the Qurʾānic readings with tanwīn are as the print cites them. The Ottoman commentary
# (izhar-full-corrected l. 1744 ff.) is followed.
#   python3 author_izhar_ch56.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F7 = "form-vii-verbs"; MMS = "mamnu-min-sarf"; ALM = "al-marifa-al-mudmarat-wal-alam"; MN = "al-muannath-wa-alamatuh"; IDH = "idha-shartiyya"; IQ = "al-iqtibas-wal-tadmin"; SM = "sifa-mushabbaha"; TRF = "anwa-al-lam-al-tarif"
K = "ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh"
K55 = "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"
TITLE = {"ar": "غَيْرُ الْمُنْصَرِفِ الْقِيَاسِيُّ: الْعَلَمُ بِتَاءِ التَّأْنِيثِ، وَالْمُرَكَّبُ، وَذُو الْأَلِفِ وَالنُّونِ، وَجَمْعُ فَعَالِلَ، وَانْصِرَافُهُ بِالْإِضَافَةِ وَاللَّامِ", "en": "The qiyāsī ghayr munṣarif: the name with the feminine tāʾ, the compound, the alif-nūn word, the faʿālil plural, and its declining by iḍāfa and the lām", "tr": "Kıyâsî gayr-ı munsarif: te'nis tâlı alem, mürekkep, elif-nûnlu, feâlil cemi ve izafet ile lâm ile munsarif oluşu"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def cit(form, lex, pos, en, tr, first=True, punct=None, extra=(), ar=None):
    a = ar or ("لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — غَيْرُ مُنْصَرِفٍ." if first else "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ — لَفْظٌ مَحْكِيٌّ، غَيْرُ مُنْصَرِفٍ.")
    return tok(form, lex, pos, [K, MMS] + ([ID] if first else [AT]) + list(extra), a, en, tr, punct=punct, segments=None if first else wa(form[2:], lex, pos))
def wakullu(): return tok("وَكُلُّ", "kull", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلُّ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and every»", "«ve her»", segments=wa("كُلُّ", "kull", "noun"))
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»")

# ----------- s1 — the name with the feminine tāʾ, in wording or estimation
S.append({"id": "s1", "translation": {"en": "And every proper name in which is the feminine tāʾ in wording — as in Fāṭima and Ḥamza — or in estimation, when it exceeds three letters — as in Zaynab — or is vowelled in the middle as the name of a female — as in Qadam, the name of a woman; and if a male were named with it, it would decline;", "tr": "Ve lafzen te'nis tâsı bulunan her alem — Fâtıma ve Hamza gibi — ya da takdiren bulunup üçten fazla harfli olan — Zeyneb gibi — ya da ortası harekeli olup bir dişiye alem olan — kadın adı olarak Kadem gibi; onunla bir erkek adlansa munsarif olurdu;"},
 "tokens": [
  wakullu(),
  tok("عَلَمٍ", "alam-name", "noun", [K, ID, ALM, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«proper name»", "«alem»"),
  tok("فِيهِ", "fi", "prep", [K, HJ, NA, MK], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ نَعْتٌ لِعَلَمٍ.", "«in which is» — the fronted khabar; the clause describes «name».", "«kendisinde … bulunan» — öne alınmış haber; cümle alem'in sıfatı.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("تَاءُ", "ta-letter", "noun", [K, MK, ID, MN], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the tāʾ of»", "«tâsı»"),
  tok("التَّأْنِيثِ", "tanith", "noun", [K, ID, MSD, F2, MN, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — التَّأْنِيثُ أَحَدُ السَّبَبَيْنِ مَعَ الْعَلَمِيَّةِ.", "«femininity» — one cause, with name-hood the other.", "«te'nis» — alemiyetle birlikte iki sebepten biri."),
  tok("لَفْظًا", "lafz", "noun", [K, "hal", MN], "حَالٌ مَنْصُوبٌ — أَيْ مَلْفُوظَةً.", "«in wording» — a ḥāl: pronounced.", "«lafzen» — hâl: söylenen.", punct="،"),
  nahw(),
  cit("فَاطِمَةَ", "fatima", "propn", "«Fāṭima»", "«Fâtıma»", extra=(MN,)),
  cit("وَحَمْزَةَ", "hamza-name", "propn", "«and Ḥamza» — a man's name, yet with the tāʾ", "«ve Hamza» — erkek adı, yine de tâlı", first=False, punct="،", extra=(MN,)),
  aw(),
  tok("تَقْدِيرًا", "taqdir", "noun", [K, AT, "hal", MSD, F2, MN], "مَعْطُوفٌ عَلَى لَفْظًا مَنْصُوبٌ — أَيْ مُقَدَّرَةً.", "«in estimation» — the tāʾ understood, not written.", "«takdiren» — tâ yazılmadan anlaşılan."),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK, "hal"], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«when it is»", "«o … iken»", segments=wa("هُوَ", "huwa", "pron")),
  tok("زَائِدٌ", "zaid", "noun", [K, MK, IFA, HV], "خَبَرٌ مَرْفُوعٌ.", "«exceeding»", "«fazla»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«over»", "«üzerine»"),
  tok("الثَّلَاثَةِ", "thalatha", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«three»", "«üç»", punct="،"),
  nahw(),
  cit("زَيْنَبَ", "zaynab", "propn", "«Zaynab» — four letters, the tāʾ estimated", "«Zeyneb» — dört harf, tâ takdîrî", punct="،", extra=(MN,)),
  aw(),
  tok("مُتَحَرِّكُ", "mutaharrik", "noun", [K, AT, MK, ID, IFA, F5], "مَعْطُوفٌ عَلَى زَائِدٌ مَرْفُوعٌ، مُضَافٌ.", "«vowelled in»", "«harekeli»"),
  tok("الْأَوْسَطِ", "awsat", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the middle»", "«ortası»"),
  tok("عَلَمًا", "alam-name", "noun", [K, "hal", ALM], "حَالٌ مَنْصُوبٌ.", "«as a name»", "«alem olarak»"),
  tok("لِمُؤَنَّثٍ", "muannath", "noun", [K, HJ, IMF, F2, MN], "اللَّامُ حَرْفُ جَرٍّ، وَمُؤَنَّثٍ مَجْرُورٌ.", "«for a female»", "«bir dişiye»", punct="،", segments=[seg("لِ", "li", "prep"), seg("مُؤَنَّثٍ", "muannath", "noun")]),
  nahw(),
  cit("قَدَمَ", "qadam", "propn", "«Qadam» — three letters, the middle vowelled", "«Kadem» — üç harf, ortası harekeli", extra=(MN,)),
  tok("اسْمَ", "ism", "noun", [K, "hal", ID], "حَالٌ مِنْ قَدَمَ مَنْصُوبٌ، مُضَافٌ — حَالَ كَوْنِهِ اسْمَ امْرَأَةٍ.", "«as the name of» — a ḥāl.", "«adı olarak» — hâl."),
  tok("امْرَأَةٍ", "imraa", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a woman»", "«bir kadının»", punct="،"),
  tok("وَلَوْ", "law", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ.", "«and if»", "«ve … -sa»", segments=wa("لَوْ", "law", "part")),
  tok("سُمِّيَ", "samma", "verb", [K, INS, NF, F2], "فِعْلُ الشَّرْطِ، مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«were named»", "«adlansa»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — بِقَدَمَ.", "«with it» — with Qadam.", "«onunla» — Kadem ile.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("مُذَكَّرٌ", "mudhakkar", "noun", [K, NF, IMF, F2], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a male»", "«bir erkek»"),
  tok("صُرِفَ", "sarafa", "verb", [K, INS, NF, MMS], "جَوَابُ الشَّرْطِ، مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — لِفَوَاتِ التَّأْنِيثِ الْمَعْنَوِيِّ.", "«it would decline» — the feminine sense gone.", "«munsarif olurdu» — ma'nevî te'nis kalktığından.", punct="،"),
 ]})
# ----------- s2 — the three-lettered feminine name with a still middle
S.append({"id": "s2", "translation": {"en": "and if the female's name is three-lettered with a still middle, its declining and its barring are both allowed — as in Hind;", "tr": "dişinin alemi üç harfli ve ortası sâkin olursa, munsarif olması da men edilmesi de câizdir — Hind gibi;"},
 "tokens": [
  tok("وَلَوْ", "law", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ.", "«and if»", "«ve … -sa»", segments=wa("لَوْ", "law", "part")),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ.", "«is»", "«olursa»"),
  tok("عَلَمُ", "alam-name", "noun", [K, KN, ID, ALM], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ.", "«the name of»", "«alemi»"),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, ID, IMF, MN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the female»", "«dişinin»"),
  tok("ثُلَاثِيًّا", "thulathi", "noun", [K, KN, NSB], "خَبَرُ كَانَ مَنْصُوبٌ.", "«three-lettered»", "«üç harfli»"),
  tok("سَاكِنَ", "sakin", "noun", [K, KN, AT, ID, IFA], "خَبَرٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«still in»", "«sâkin»"),
  tok("الْأَوْسَطِ", "awsat", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the middle»", "«ortası»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, INS, MR, HV], "جَوَابُ لَوْ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«are allowed»", "«câizdir»"),
  tok("صَرْفُهُ", "sarf-declension", "noun", [K, FL, ID, MSD, MMS], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its declining»", "«munsarif olması»", segments=[seg("صَرْفُ", "sarf-declension", "noun"), pr3ms()]),
  tok("وَمَنْعُهُ", "man-prevention", "noun", [K, AT, FL, ID, MSD, MMS], "الْوَاوُ عَاطِفَةٌ، وَمَنْعُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its barring»", "«ve men edilmesi»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("مَنْعُ", "man-prevention", "noun"), pr3ms()]),
  nahw(),
  cit("هِنْدَ", "hind", "propn", "«Hind» — three letters, the middle still; both readings allowed", "«Hind» — üç harf, ortası sâkin; iki okunuş da câiz", punct="؛", extra=(MN,)),
 ]})
# ----------- s3 — the compound name
S.append({"id": "s3", "translation": {"en": "and every proper name compounded of two nouns, neither of which governs the other, the second being neither a sound nor containing the sense of a particle — as in Baʿlabakk and Ḥaḍramawt;", "tr": "ve biri ötekinde âmil olmayan, ikincisi ne ses ne de harf manası içeren iki isimden mürekkep her alem — Ba'lebek ve Hadramevt gibi;"},
 "tokens": [
  wakullu(),
  tok("عَلَمٍ", "alam-name", "noun", [K, ID, ALM, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«proper name»", "«alem»"),
  tok("مُرَكَّبٍ", "murakkab", "noun", [K, NA, IMF, F2, MMS], "نَعْتٌ مَجْرُورٌ — التَّرْكِيبُ أَحَدُ السَّبَبَيْنِ.", "«compounded» — composition is one cause.", "«mürekkep» — terkip iki sebepten biri."),
  tok("مِنِ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("اسْمَيْنِ", "ism", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two nouns»", "«iki isim»"),
  tok("لَيْسَ", "laysa", "verb", [K, NA, KN], "فِعْلٌ مَاضٍ نَاقِصٌ — وَالْجُمْلَةُ نَعْتٌ لِاسْمَيْنِ.", "«neither … is» — the clause describes the two nouns.", "«… değildir» — cümle iki ismin sıfatı."),
  tok("أَحَدُهُمَا", "ahad", "noun", [K, KN, ID], "اسْمُ لَيْسَ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them»", "«biri»", segments=[seg("أَحَدُ", "ahad", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("عَامِلًا", "amil", "noun", [K, KN, IFA, AQ], "خَبَرُ لَيْسَ مَنْصُوبٌ.", "«governing»", "«âmil»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْآخَرِ", "akhar", "noun", [K, HJ, MMS], "مَجْرُورٌ بِفِي — فَخَرَجَ نَحْوُ عَبْدِ اللهِ.", "«the other» — so ʿAbd Allāh is out: its first governs the second.", "«ötekinde» — Abdullah dışarıda: ilki ikincide âmil."),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor»", "«ne de»", segments=wa("لَا", "la", "part")),
  tok("الثَّانِي", "thani", "noun", [K, AT, KN, MQ], "مَعْطُوفٌ عَلَى أَحَدُهُمَا مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمُ لَيْسَ.", "«the second» — joined to laysa's ism.", "«ikincisi» — leyse'nin ismine atıf."),
  tok("صَوْتًا", "sawt", "noun", [K, KN], "خَبَرُ لَيْسَ مَنْصُوبٌ — فَخَرَجَ سِيبَوَيْهِ، فَإِنَّهُ مَبْنِيٌّ.", "«a sound» — so Sībawayh is out, being indeclinable.", "«ses» — Sîbeveyh dışarıda, mebnîdir."),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ.", "«nor»", "«ne de»", segments=wa("لَا", "la", "part")),
  tok("مُتَضَمِّنًا", "mutadammin", "noun", [K, AT, KN, IFA, F5], "مَعْطُوفٌ عَلَى صَوْتًا مَنْصُوبٌ.", "«containing»", "«içeren»"),
  tok("لِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "اللَّامُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the sense of»", "«manasını»", segments=[seg("لِ", "li", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("حَرْفٍ", "harf", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَخَرَجَ خَمْسَةَ عَشَرَ، فَإِنَّهُ مَبْنِيٌّ.", "«a particle» — so khamsata ʿashara is out, being indeclinable.", "«harf» — hamsete aşere dışarıda, mebnîdir.", punct="،"),
  nahw(),
  cit("بَعْلَبَكَّ", "balabakk", "propn", "«Baʿlabakk» — the town", "«Ba'lebek» — şehir"),
  cit("وَحَضْرَمَوْتَ", "hadramawt", "propn", "«and Ḥaḍramawt» — the region", "«ve Hadramevt» — bölge", first=False, punct="؛"),
 ]})
# ----------- s4 — the alif and nūn
S.append({"id": "s4", "translation": {"en": "and everything in which are an added alif and nūn, as a proper name, or as a description that the tāʾ does not enter — as in ʿImrān, sakrān and raḥmān;", "tr": "ve kendisinde zâid elif ve nûn bulunan her şey, alem olarak ya da tâ'nın girmediği bir sıfat olarak — İmrân, sekrân ve rahmân gibi;"},
 "tokens": [
  wakullu(),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that which»", "«şey»"),
  tok("فِيهِ", "fi", "prep", [K, HJ, MAW, MK], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِلَةٌ.", "«in which are» — the ṣila.", "«kendisinde … bulunan» — sıla.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("أَلِفٌ", "alif-letter", "noun", [K, MK, MMS], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«an alif»", "«elif»"),
  tok("وَنُونٌ", "nun-letter", "noun", [K, AT, MMS], "الْوَاوُ عَاطِفَةٌ، وَنُونٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a nūn»", "«ve nûn»", segments=wa("نُونٌ", "nun-letter", "noun")),
  tok("زَائِدَتَانِ", "zaid", "noun", [K, NA, IFA, MTH], "نَعْتٌ لِلْأَلِفِ وَالنُّونِ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى مُؤَنَّثٌ.", "«added» — a dual feminine description.", "«zâid» — tesniye müennes sıfat."),
  tok("عَلَمًا", "alam-name", "noun", [K, "hal", ALM, MMS], "حَالٌ مِنَ الضَّمِيرِ فِي فِيهِ مَنْصُوبٌ.", "«as a proper name»", "«alem olarak»"),
  aw(),
  tok("وَصْفًا", "wasf", "noun", [K, AT, "hal", MSD, SM], "مَعْطُوفٌ عَلَى عَلَمًا مَنْصُوبٌ.", "«as a description»", "«vasıf olarak»"),
  tok("لَا", "la", "part", [K, LN, NA], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ نَعْتٌ لِوَصْفًا.", "«not» — the clause describes the description.", "«-meyen» — cümle vasfın sıfatı."),
  tok("تَدْخُلُهُ", "dakhala", "verb", [K, MR, LN, MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«enter it»", "«ona girmez»", segments=[seg("تَدْخُلُ", "dakhala", "verb"), pr3ms()]),
  tok("التَّاءُ", "ta-letter", "noun", [K, FL, MN], "فَاعِلٌ مَرْفُوعٌ — تَاءُ التَّأْنِيثِ: سَكْرَانُ مُؤَنَّثُهُ سَكْرَى لَا سَكْرَانَةُ.", "«the tāʾ» — sakrān's feminine is sakrā, not sakrāna.", "«tâ» — sekrân'ın müennesi sekrâ, sekrâne değil.", punct="،"),
  nahw(),
  cit("عِمْرَانَ", "imran", "propn", "«ʿImrān» — a name", "«İmrân» — alem"),
  cit("وَسَكْرَانَ", "sakran", "noun", "«and sakrān» — «drunk», a description", "«ve sekrân» — «sarhoş», vasıf", first=False, extra=(SM,)),
  cit("وَرَحْمٰنَ", "rahman", "noun", "«and raḥmān» — «most merciful»; the print writes رحمن", "«ve rahmân» — «çok merhametli»; baskıda رحمن", first=False, punct="؛", extra=(SM,)),
 ]})
# ----------- s5 — the plural on faʿālil / faʿālīl, and the licence
S.append({"id": "s5", "translation": {"en": "and every plural on faʿālil or faʿālīl — as in masājid and maṣābīḥ; and its declining is allowed for the necessity of verse or for assonance — as in «salāsilan» and «qawārīran»;", "tr": "ve feâlil ya da feâlîl vezninde her cemi — mesâcid ve mesâbîh gibi; şiir zarureti ya da tenâsüb için munsarif kılınması câizdir — «selâsilen» ve «kavârîren» gibi;"},
 "tokens": [
  wakullu(),
  tok("جَمْعٍ", "jam", "noun", [K, ID, JT, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«plural» — the plural of plurals.", "«cemi» — müntehe'l-cumû' sîgası."),
  tok("عَلَى", "ala", "prep", [K, HJ, NA], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِجَمْعٍ.", "«on»", "«üzere»"),
  tok("فَعَالِلَ", "faalil-wazn", "noun", [K, HJ, MMS, JT], "مَجْرُورٌ بِالْفَتْحَةِ — الْوَزْنُ نَفْسُهُ غَيْرُ مُنْصَرِفٍ.", "«faʿālil» — the pattern, itself a diptote.", "«feâlil» — vezin, kendisi gayr-ı munsarif."),
  aw(),
  tok("فَعَالِيلَ", "faalil-wazn-long", "noun", [K, AT, MMS, JT], "مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ.", "«faʿālīl»", "«feâlîl»", punct="،"),
  nahw(),
  cit("مَسَاجِدَ", "masjid", "noun", "«masājid» — «mosques», on faʿālil", "«mesâcid» — «mescidler», feâlil", extra=(JT,)),
  cit("وَمَصَابِيحَ", "misbah", "noun", "«and maṣābīḥ» — «lamps», on faʿālīl", "«ve mesâbîh» — «kandiller», feâlîl", first=False, punct="،", extra=(JT,)),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, MR, HV], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and … is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("صَرْفُهُ", "sarf-declension", "noun", [K, FL, ID, MSD, MMS], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its declining»", "«munsarif kılınması»", segments=[seg("صَرْفُ", "sarf-declension", "noun"), pr3ms()]),
  tok("لِضَرُورَةِ", "darura", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَضَرُورَةِ مَجْرُورٌ، مُضَافٌ.", "«for the necessity of»", "«zarureti için»", segments=[seg("لِ", "li", "prep"), seg("ضَرُورَةِ", "darura", "noun")]),
  tok("الشِّعْرِ", "shir", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verse»", "«şiir»"),
  aw(),
  tok("لِلتَّنَاسُبِ", "tanasub", "noun", [K, AT, HJ, MSD, "form-vi-verbs"], "اللَّامُ حَرْفُ جَرٍّ، وَالتَّنَاسُبِ مَجْرُورٌ — مَعْطُوفٌ؛ تَنَاسُبِ رُؤُوسِ الْآيِ.", "«for assonance» — the verse-ends matching.", "«tenâsüb için» — âyet sonlarının uyumu.", punct="،", segments=[seg("لِ", "li", "prep"), seg("التَّنَاسُبِ", "tanasub", "noun")]),
  nahw(),
  tok("سَلَاسِلًا", "salasil", "noun", [K, ID, JT, IQ, MMS], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ — مَصْرُوفٌ بِالتَّنْوِينِ فِي قِرَاءَةِ ﴿سَلَاسِلًا وَأَغْلَالًا﴾ (الْإِنْسَان ٧٦: ٤).", "«salāsilan» — declined by tanwīn in the reading of al-Insān 76:4.", "«selâsilen» — İnsân 76:4 kıraatinde tenvinle munsarif."),
  tok("وَقَوَارِيرًا", "qarura", "noun", [K, AT, JT, IQ, MMS], "الْوَاوُ عَاطِفَةٌ، وَقَوَارِيرًا مَعْطُوفٌ — مَصْرُوفٌ بِالتَّنْوِينِ فِي قِرَاءَةِ ﴿قَوَارِيرًا﴾ (الْإِنْسَان ٧٦: ١٥) لِلتَّنَاسُبِ.", "«and qawārīran» — declined for assonance in al-Insān 76:15.", "«ve kavârîren» — İnsân 76:15'te tenâsüb için munsarif.", punct="؛", segments=wa("قَوَارِيرًا", "qarura", "noun")),
 ]})
# ----------- s6 — the diptote declines when annexed or with the lām
S.append({"id": "s6", "translation": {"en": "And everything that does not decline, when it is annexed or the lām of definition enters it, declines — as in «I passed by the red one» and «by our red one».", "tr": "Munsarif olmayan her şey, muzâf olunca ya da kendisine harf-i tarif lâmı girince munsarif olur — «kırmızıya uğradım» ve «bizim kırmızımıza» gibi."},
 "tokens": [
  wakullu(),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that which»", "«şey»"),
  tok("لَا", "la", "part", [K, LN, MAW], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ صِلَةٌ.", "«not» — the ṣila.", "«-mayan» — sıla."),
  tok("يَنْصَرِفُ", "insarafa", "verb", [K, MR, LN, F7, MMS], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«declines»", "«munsarif olur»"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ince»"),
  tok("أُضِيفَ", "adafa", "verb", [K, IDH, NF, F4], "فِعْلُ الشَّرْطِ، مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«it is annexed»", "«muzâf olunca»"),
  aw(),
  tok("دَخَلَهُ", "dakhala", "verb", [K, AT, IDH, MB], "الْفِعْلُ مَعْطُوفٌ عَلَى أُضِيفَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«enters it»", "«ona girince»", segments=[seg("دَخَلَ", "dakhala", "verb"), pr3ms()]),
  tok("لَامُ", "lam-letter", "noun", [K, FL, ID, TRF], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the lām of»", "«lâmı»"),
  tok("التَّعْرِيفِ", "tarif", "noun", [K, ID, MSD, F2, TRF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«definition»", "«tarifin»"),
  tok("انْصَرَفَ", "insarafa", "verb", [K, IDH, F7, MMS, MK], "جَوَابُ الشَّرْطِ، مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كُلُّ.", "«declines» — the khabar of «every».", "«munsarif olur» — küll'ün haberi.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=":"),
  tok("مَرَرْتُ", "marra", "verb", [K, FL, "doubled-verbs"], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I passed»", "«uğradım»", segments=[seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِالْأَحْمَرِ", "ahmar", "noun", [K, HJ, TRF, MMS, SM], "الْبَاءُ حَرْفُ جَرٍّ، وَالْأَحْمَرِ مَجْرُورٌ بِالْكَسْرَةِ — انْصَرَفَ بِاللَّامِ.", "«by the red one» — kasra returns with the lām.", "«kırmızıya» — lâm ile kesre döner.", segments=[seg("بِ", "bi", "prep"), seg("الْأَحْمَرِ", "ahmar", "noun")]),
  tok("وَأَحْمَرِنَا", "ahmar", "noun", [K, AT, ID, MMS, SM], "الْوَاوُ عَاطِفَةٌ، وَأَحْمَرِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — انْصَرَفَ بِالْإِضَافَةِ.", "«and by our red one» — kasra returns with the iḍāfa.", "«ve bizim kırmızımıza» — izafetle kesre döner.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("أَحْمَرِ", "ahmar", "noun"), seg("نَا", "pron-1p", "pron")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "tanith": G("tanith", "تَأْنِيث", "أ ن ث", "noun", "femininity, the feminine marking — the maṣdar of annatha", "te'nis, dişillik — ennese'nin mastarı", 3),
 "fatima": G("fatima", "فَاطِمَةُ", "ف ط م", "propn", "Fāṭima — a woman's name with the feminine tāʾ (diptote)", "Fâtıma — te'nis tâlı kadın adı (gayr-ı munsarif)", 4),
 "hamza-name": G("hamza-name", "حَمْزَةُ", "ح م ز", "propn", "Ḥamza — a man's name with the feminine tāʾ (diptote)", "Hamza — te'nis tâlı erkek adı (gayr-ı munsarif)", 4),
 "zaynab": G("zaynab", "زَيْنَبُ", "ز ن ب", "propn", "Zaynab — a woman's name, the tāʾ estimated (diptote)", "Zeyneb — kadın adı, tâ takdîrî (gayr-ı munsarif)", 4),
 "qadam": G("qadam", "قَدَم", "ق د م", "noun", "foot; as a woman's name a diptote (three letters, vowelled middle)", "ayak; kadın adı olarak gayr-ı munsarif (üç harf, ortası harekeli)", 3, plural="أَقْدَام"),
 "sarafa": G("sarafa", "صَرَفَ", "ص ر ف", "verb", "to decline (a noun), to give it tanwīn and kasra; passive ṣurifa", "sarf etmek, (ismi) tenvin ve kesreyle çekmek; meçhûlü surife", 4),
 "thulathi": G("thulathi", "ثُلَاثِيّ", "ث ل ث", "noun", "three-lettered, triliteral", "üç harfli, sülâsî", 3),
 "sarf-declension": G("sarf-declension", "صَرْف", "ص ر ف", "noun", "declension — taking tanwīn and kasra; the opposite of manʿ", "sarf — tenvin ve kesre alma; men'in karşıtı", 3),
 "man-prevention": G("man-prevention", "مَنْع", "م ن ع", "noun", "barring, prevention — the maṣdar of manaʿa; manʿ al-ṣarf", "men, engelleme — menea'nın mastarı; men-i sarf", 3),
 "balabakk": G("balabakk", "بَعْلَبَكُّ", "ب ع ل", "propn", "Baʿlabakk — a town; a compound name (diptote)", "Ba'lebek — şehir; mürekkep alem (gayr-ı munsarif)", 4),
 "hadramawt": G("hadramawt", "حَضْرَمَوْتُ", "ح ض ر", "propn", "Ḥaḍramawt — a region; a compound name (diptote)", "Hadramevt — bölge; mürekkep alem (gayr-ı munsarif)", 4),
 "sakran": G("sakran", "سَكْرَان", "س ك ر", "noun", "drunk — with the added alif and nūn; feminine sakrā (diptote)", "sarhoş, sekrân — zâid elif ve nûnla; müennesi sekrâ (gayr-ı munsarif)", 3),
 "faalil-wazn": G("faalil-wazn", "فَعَالِل", "ف ع ل", "noun", "the pattern faʿālil — the plural of plurals, a diptote (masājid)", "feâlil vezni — müntehe'l-cumû', gayr-ı munsarif (mesâcid)", 4),
 "faalil-wazn-long": G("faalil-wazn-long", "فَعَالِيل", "ف ع ل", "noun", "the pattern faʿālīl — the plural of plurals with a long third, a diptote (maṣābīḥ)", "feâlîl vezni — üçüncüsü uzun müntehe'l-cumû', gayr-ı munsarif (mesâbîh)", 4),
 "salasil": G("salasil", "سَلَاسِل", "س ل س ل", "noun", "chains — the plural of silsila, on faʿālil", "zincirler — silsile'nin çoğulu, feâlil vezninde", 3),
 "insarafa": G("insarafa", "انْصَرَفَ", "ص ر ف", "verb", "to decline, to take tanwīn and kasra (form VII); munṣarif", "munsarif olmak, tenvin ve kesre almak (VII. bab)", 3, form="VII"),
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
put_morph(mo, "sarafa", {"bab": "الْبَابُ الثَّانِي فَعَلَ يَفْعِلُ", "wazn": "فَعَلَ يَفْعِلُ", "masdar": "صَرْف", "ismFail": "صَارِف",
 "mazi": ["صَرَفَ", "صَرَفَا", "صَرَفُوا", "صَرَفَتْ", "صَرَفَتَا", "صَرَفْنَ", "صَرَفْتَ", "صَرَفْتُمَا", "صَرَفْتُمْ", "صَرَفْتِ", "صَرَفْتُمَا", "صَرَفْتُنَّ", "صَرَفْتُ", "صَرَفْنَا"],
 "mudari": ["يَصْرِفُ", "يَصْرِفَانِ", "يَصْرِفُونَ", "تَصْرِفُ", "تَصْرِفَانِ", "يَصْرِفْنَ", "تَصْرِفُ", "تَصْرِفَانِ", "تَصْرِفُونَ", "تَصْرِفِينَ", "تَصْرِفَانِ", "تَصْرِفْنَ", "أَصْرِفُ", "نَصْرِفُ"],
 "amr": ["اِصْرِفْ", "اِصْرِفَا", "اِصْرِفُوا", "اِصْرِفِي", "اِصْرِفَا", "اِصْرِفْنَ"], "mansub": "يَصْرِفَ", "majzum": "يَصْرِفْ", "majzum2": "تَصْرِفْ",
 "note": "صَرَفَ الِاسْمَ يَصْرِفُهُ صَرْفًا: نَوَّنَهُ وَجَرَّهُ بِالْكَسْرَةِ — مِنَ الْبَابِ الثَّانِي، صَحِيحٌ، مُتَعَدٍّ؛ مَجْهُولُهُ صُرِفَ، وَالْمَصْرُوفُ هُوَ الْمُنْصَرِفُ."})
put_morph(mo, "insarafa", {"bab": "بَابُ الِانْفِعَالِ", "wazn": "انْفَعَلَ يَنْفَعِلُ", "masdar": "انْصِرَاف", "ismFail": "مُنْصَرِف",
 "mazi": ["انْصَرَفَ", "انْصَرَفَا", "انْصَرَفُوا", "انْصَرَفَتْ", "انْصَرَفَتَا", "انْصَرَفْنَ", "انْصَرَفْتَ", "انْصَرَفْتُمَا", "انْصَرَفْتُمْ", "انْصَرَفْتِ", "انْصَرَفْتُمَا", "انْصَرَفْتُنَّ", "انْصَرَفْتُ", "انْصَرَفْنَا"],
 "mudari": ["يَنْصَرِفُ", "يَنْصَرِفَانِ", "يَنْصَرِفُونَ", "تَنْصَرِفُ", "تَنْصَرِفَانِ", "يَنْصَرِفْنَ", "تَنْصَرِفُ", "تَنْصَرِفَانِ", "تَنْصَرِفُونَ", "تَنْصَرِفِينَ", "تَنْصَرِفَانِ", "تَنْصَرِفْنَ", "أَنْصَرِفُ", "نَنْصَرِفُ"],
 "amr": ["اِنْصَرِفْ", "اِنْصَرِفَا", "اِنْصَرِفُوا", "اِنْصَرِفِي", "اِنْصَرِفَا", "اِنْصَرِفْنَ"], "mansub": "يَنْصَرِفَ", "majzum": "يَنْصَرِفْ", "majzum2": "تَنْصَرِفْ",
 "note": "انْصَرَفَ الِاسْمُ يَنْصَرِفُ انْصِرَافًا: قَبِلَ التَّنْوِينَ وَالْجَرَّ — مُطَاوِعُ صَرَفَ، مِنْ بَابِ الِانْفِعَالِ، لَازِمٌ، هَمْزَتُهُ هَمْزَةُ وَصْلٍ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch56 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("samma", "sarafa", "kana", "jaaza", "laysa", "dakhala", "insarafa", "adafa", "marra") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "غَيْرُ الْمُنْصَرِفِ الْقِيَاسِيُّ: الْعَلَمُ بِتَاءِ التَّأْنِيثِ لَفْظًا أَوْ تَقْدِيرًا، وَهِنْدُ، وَالْمُرَكَّبُ، وَالْأَلِفُ وَالنُّونُ، وَجَمْعُ فَعَالِلَ وَصَرْفُهُ لِلضَّرُورَةِ، وَالِانْصِرَافُ بِالْإِضَافَةِ وَاللَّامِ", "en": "The qiyāsī diptote: the name with the feminine tāʾ in wording or estimation, Hind, the compound, the alif and nūn, the faʿālil plural and its licence, declining by iḍāfa and the lām", "tr": "Kıyâsî gayr-ı munsarif: lafzen ya da takdiren te'nis tâlı alem, Hind, mürekkep, elif ve nûn, feâlil cemi ve ruhsatı, izafet ve lâm ile munsarif oluş"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — غير المنصرف القياسي", "الكافية لابن الحاجب — أسباب منع الصرف", "شرح قطر الندى لابن هشام — الممنوع من الصرف"],
 "amil": "the qiyāsī diptote continued: every name with the feminine tāʾ in wording (فَاطِمَةَ، حَمْزَةَ) or in estimation when over three letters (زَيْنَبَ) or vowelled in the middle as a female's name (قَدَمَ) — declined if a male is so named; the three-lettered still-middled female name may decline or be barred (هِنْدَ); every name compounded of two nouns neither governing the other, the second no sound and no particle-sense (بَعْلَبَكَّ، حَضْرَمَوْتَ); every name or tāʾ-less description with an added alif and nūn (عِمْرَانَ، سَكْرَانَ، رَحْمٰنَ); every faʿālil/faʿālīl plural (مَسَاجِدَ، مَصَابِيحَ) — declinable for verse-necessity or assonance (سَلَاسِلًا، قَوَارِيرًا); and every diptote declines when annexed or given the lām (بِالْأَحْمَرِ وَأَحْمَرِنَا).",
 "question": {
  "en": ["When does the feminine tāʾ bar a name? In wording — فَاطِمَةَ, and even the man's name حَمْزَةَ; or in estimation when the name exceeds three letters (زَيْنَبَ) or is three-lettered with a vowelled middle as a female's name (قَدَمَ).",
         "What if a male is named قَدَم? It declines — the estimated tāʾ went with the female sense; the print: وَلَوْ سُمِّيَ بِهِ مُذَكَّرٌ صُرِفَ.",
         "What of هِنْد? A three-lettered female name with a still middle: both declining and barring are allowed — بِهِنْدٍ and بِهِنْدَ.",
         "Which compound names are diptotes? Those of two nouns neither governing the other (so not عَبْدُ اللهِ), the second neither a sound (so not سِيبَوَيْهِ, indeclinable) nor particle-sensed (so not خَمْسَةَ عَشَرَ, indeclinable): بَعْلَبَكَّ، حَضْرَمَوْتَ.",
         "When do the alif and nūn bar? As a name (عِمْرَانَ) or as a description that takes no feminine tāʾ (سَكْرَانَ, fem. سَكْرَى; رَحْمٰنَ) — نَدْمَان with fem. نَدْمَانَة declines.",
         "Which plural is a diptote by itself? The plural of plurals on فَعَالِل or فَعَالِيل — مَسَاجِدَ، مَصَابِيحَ; verse-necessity or assonance may decline it: ﴿سَلَاسِلًا﴾ (al-Insān 76:4) and ﴿قَوَارِيرًا﴾ (76:15) in the readings with tanwīn.",
         "When does a diptote decline again? When annexed or given the lām of definition — مَرَرْتُ بِالْأَحْمَرِ وَأَحْمَرِنَا: the kasra returns.",
         "What does the engine READ here? The DabtEngine reads the cited names after نَحْوُ at their fatḥa as diptotes, صُرِفَ and انْصَرَفَ as the answers of لَوْ and إِذَا, سَلَاسِلًا and قَوَارِيرًا with their tanwīn as the licensed forms, and بِالْأَحْمَرِ / أَحْمَرِنَا in kasra by the lām and the iḍāfa."],
  "tr": ["Te'nis tâsı alemi ne zaman men eder? Lafzen — Fâtımete, hatta erkek adı Hamzete; takdiren, alem üçten fazla harfli (Zeynebe) ya da üç harfli olup ortası harekeli dişi adı olunca (Kademe).",
         "Bir erkek Kadem diye adlanırsa? Munsarif olur — takdîrî tâ dişi manasıyla gitti; baskı: ve lev sümmiye bihî müzekkerun surife.",
         "Hind'in durumu? Üç harfli, ortası sâkin dişi adı: munsarif olması da men edilmesi de câiz — bi-Hindin ve bi-Hinde.",
         "Hangi mürekkep alemler gayr-ı munsariftir? Biri ötekinde âmil olmayan iki isimden (Abdullah değil), ikincisi ne ses (Sîbeveyh değil, mebnî) ne harf manalı (hamsete aşere değil, mebnî): Ba'lebekke, Hadramevte.",
         "Elif ve nûn ne zaman men eder? Alem olarak (İmrâne) ya da te'nis tâsı almayan vasıf olarak (sekrâne, müennesi sekrâ; rahmâne) — müennesi nedmâne olan nedmân munsariftir.",
         "Hangi cemi kendi başına gayr-ı munsariftir? Feâlil ya da feâlîl vezninde müntehe'l-cumû' — mesâcide, mesâbîha; şiir zarureti ya da tenâsüb onu munsarif kılabilir: selâsilen (İnsân 76:4) ve kavârîren (76:15) tenvinli kıraatlerde.",
         "Gayr-ı munsarif ne zaman yeniden munsarif olur? Muzâf olunca ya da harf-i tarif lâmı girince — merartü bi'l-ahmeri ve ahmerinâ: kesre döner.",
         "Motor burada neyi OKUR? DabtEngine nahvü'den sonra alıntılanan adları fethalarıyla gayr-ı munsarif, surife ve insarafe'yi lev ve izâ'nın cevabı, selâsilen ve kavârîren'i tenvinleriyle ruhsatlı şekiller, bi'l-ahmeri / ahmerinâ'yı lâm ve izafetle kesreli okur."],
 },
 "plain": {"en": "More words that refuse kasra and tanwīn: names ending in -a (Fāṭima, even Ḥamza), longer feminine names (Zaynab), two-word place names (Baʿlabakk), words in -ān with no -āna feminine (ʿImrān, sakrān), and «plurals of plurals» like masājid. Hind may go either way. Add «al-» or annex the word and the kasra returns.",
           "tr": "Kesre ve tenvini reddeden başka sözler: -a ile biten adlar (Fâtıma, hatta Hamza), uzun dişil adlar (Zeyneb), iki sözcüklü yer adları (Ba'lebek), -âne dişili olmayan -ân'lı sözcükler (İmrân, sekrân) ve mesâcid gibi «çoğulun çoğulu». Hind iki türlü olabilir. «el-» ekle ya da sözcüğü muzâf yap, kesre geri gelir."},
 "explanation": {"en": "The qiyāsī kinds continue. Every proper name in which is the feminine tāʾ in wording — فَاطِمَة، حَمْزَة — or in estimation, when the name exceeds three letters (زَيْنَب) or is vowelled in the middle as a female's name (قَدَم as a woman's name); if a male were named with it, it would decline. If the female's name is three-lettered with a still middle, declining and barring are both allowed — هِنْد. Every proper name compounded of two nouns neither of which governs the other, the second being neither a sound nor containing the sense of a particle — بَعْلَبَكّ، حَضْرَمَوْت. Everything in which are an added alif and nūn as a proper name, or as a description the tāʾ does not enter — عِمْرَان، سَكْرَان، رَحْمٰن (the print writes رحمن). Every plural on فَعَالِل or فَعَالِيل — مَسَاجِد، مَصَابِيح — and its declining is allowed for the necessity of verse or for assonance — ﴿سَلَاسِلًا﴾ (al-Insān 76:4) and ﴿قَوَارِيرًا﴾ (76:15) in the readings with tanwīn. And everything that does not decline, when it is annexed or the lām of definition enters it, declines — مَرَرْتُ بِالْأَحْمَرِ وَأَحْمَرِنَا. The third division, by kind, follows.",
                 "tr": "Kıyâsî türler sürer. Lafzen te'nis tâsı bulunan her alem — Fâtıma, Hamza — ya da takdiren bulunup üçten fazla harfli (Zeyneb) ya da dişi adı olarak ortası harekeli olan (kadın adı olarak Kadem); bir erkek onunla adlansa munsarif olurdu. Dişinin alemi üç harfli ve ortası sâkin olursa munsarif olması da men edilmesi de câizdir — Hind. Biri ötekinde âmil olmayan, ikincisi ne ses ne harf manası içeren iki isimden mürekkep her alem — Ba'lebek, Hadramevt. Alem olarak ya da tâ'nın girmediği vasıf olarak zâid elif ve nûn bulunan her şey — İmrân, sekrân, rahmân (baskıda رحمن). Feâlil ya da feâlîl vezninde her cemi — mesâcid, mesâbîh — şiir zarureti ya da tenâsüb için munsarif kılınması câizdir — selâsilen (İnsân 76:4) ve kavârîren (76:15) tenvinli kıraatlerde. Munsarif olmayan her şey, muzâf olunca ya da harf-i tarif lâmı girince munsarif olur — merartü bi'l-ahmeri ve ahmerinâ. Nev'e göre üçüncü taksim gelir."},
 "examples": [
  {"ar": "نَحْوُ فَاطِمَةَ وَحَمْزَةَ … نَحْوُ زَيْنَبَ … نَحْوُ قَدَمَ اسْمَ امْرَأَةٍ", "en": "the feminine tāʾ in wording and in estimation", "tr": "lafzen ve takdiren te'nis tâsı", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "يَجُوزُ صَرْفُهُ وَمَنْعُهُ، نَحْوُ هِنْدَ", "en": "Hind: both allowed", "tr": "Hind: ikisi de câiz", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "نَحْوُ بَعْلَبَكَّ وَحَضْرَمَوْتَ", "en": "the compound names", "tr": "mürekkep alemler", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "نَحْوُ عِمْرَانَ وَسَكْرَانَ وَرَحْمٰنَ", "en": "the added alif and nūn", "tr": "zâid elif ve nûn", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "نَحْوُ سَلَاسِلًا وَقَوَارِيرًا", "en": "the faʿālil plural declined by licence", "tr": "ruhsatla munsarif kılınan feâlil cemi", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "مَرَرْتُ بِالْأَحْمَرِ وَأَحْمَرِنَا", "en": "the diptote declining by the lām and the iḍāfa", "tr": "lâm ve izafetle munsarif olan gayr-ı munsarif", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "مَرَرْتُ بِحَمْزَةٍ", "right": "مَرَرْتُ بِحَمْزَةَ", "why": {"en": "the feminine tāʾ in wording bars the name even of a man", "tr": "lafzî te'nis tâsı erkek adını bile men eder"}},
  {"wrong": "مَرَرْتُ بِأَحْمَرَنَا", "right": "مَرَرْتُ بِأَحْمَرِنَا", "why": {"en": "annexed, the diptote declines: jarr by kasra", "tr": "muzâf olunca gayr-ı munsarif munsarif olur: cer kesre ile"}},
  {"wrong": "مَرَرْتُ بِمَسَاجِدٍ", "right": "مَرَرْتُ بِمَسَاجِدَ", "why": {"en": "the faʿālil plural is a diptote outside verse-licence", "tr": "feâlil cemi şiir ruhsatı dışında gayr-ı munsariftir"}},
  {"wrong": "مَرَرْتُ بِنَدْمَانَ (fem. نَدْمَانَة)", "right": "مَرَرْتُ بِنَدْمَانٍ", "why": {"en": "the alif and nūn bar a description only when its feminine takes no tāʾ", "tr": "elif ve nûn vasfı ancak müennesi tâ almayınca men eder"}},
 ],
}
ADD_EN = (" Chapter 56 (print p. 151): the qiyāsī diptote continued — the name with the feminine tāʾ in wording or estimation, Qadam and the male so named (s1), Hind both ways (s2), the compound name (s3), the added alif and nūn (s4), the faʿālil plural and its licence, al-Insān 76:4 and 76:15 (s5), the diptote declining by the iḍāfa and the lām (s6).")
ADD_TR = (" Elli altıncı bab (baskı s. 151): kıyâsî gayr-ı munsarif devam — lafzen ya da takdiren te'nis tâlı alem, Kadem ve onunla adlanan erkek (s1), iki türlü Hind (s2), mürekkep alem (s3), zâid elif ve nûn (s4), feâlil cemi ve ruhsatı, İnsân 76:4 ve 76:15 (s5), izafet ve lâm ile munsarif olan gayr-ı munsarif (s6).")
write_out(56, S, TITLE, ADD_EN, ADD_TR, "p. 151", GLOSS_ADD, notes=(NOTE,),
          related=((K55, [K]), (MMS, [K]), (MN, [K]), (ALM, [K]), (JT, [K]), (TRF, [K])))
report(56, S, GLOSS_ADD, (NOTE,))
