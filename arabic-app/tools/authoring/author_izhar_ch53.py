# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 53: the division by locus continued — deficient iʿrāb by two vowels: ḍamma in rafʿ and fatḥa in naṣb and jarr, the
# non-declinable (أَحْمَدُ، أَحْمَدَ، بِأَحْمَدَ); ḍamma in rafʿ and kasra in naṣb and jarr, the sound feminine plural (مُسْلِمَاتٌ، مُسْلِمَاتٍ، بِمُسْلِمَاتٍ). The second
# locus, the letters: complete by the three (wāw, alif, yāʾ) — the six nouns annexed to other than the speaker's yāʾ, singular and un-diminished;
# deficient by two: wāw in rafʿ and yāʾ in naṣb and jarr — the sound masculine plural, أُولُو, عِشْرُونَ and its sisters (مُسْلِمُونَ وَأُولُو مَالٍ وَعِشْرُونَ …);
# alif in rafʿ and yāʾ in naṣb and jarr — the dual, اثْنَانِ and كِلَا annexed to a pronoun (مُسْلِمَانِ وَاثْنَانِ وَكِلَاهُمَا …). Print pp. 148–149.
# Orthography: the lithograph prints الثلثة (old spelling); the text gives الثَّلَاثَةِ. The Ottoman commentary (izhar-full-corrected l. 1649 ff.) is followed.
#   python3 author_izhar_ch53.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; FN = "five-nouns"; JDS = "jam-mudhakkar-salim"; JMS = "jam-muannath-salim"; TQ = "taqsim"
K = "naqis-al-irab-bil-harakat-wal-murab-bil-huruf"
K52 = "al-irab-wa-taqsimuhu-bil-dhat-wal-mahall"
TITLE = {"ar": "نَاقِصُ الْإِعْرَابِ بِالْحَرَكَتَيْنِ، وَالْمُعْرَبُ بِالْحُرُوفِ: تَامُّهُ وَنَاقِصُهُ", "en": "Deficient iʿrāb by two vowels, and the iʿrāb by letters: complete and deficient", "tr": "İki hareke ile nâkıs i'râb ve harflerle i'râb: tamı ve nâkısı"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def jaani(): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")])
def waraaytu(): return tok("وَرَأَيْتُ", "raa", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَرَأَيْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I saw»", "«ve gördüm»", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron")])
def wamarartu(): return tok("وَمَرَرْتُ", "marra", "verb", [K, AT, FL, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمَرَرْتُ فِعْلٌ مَاضٍ مُضَاعَفٌ، وَالتَّاءُ فَاعِلٌ.", "«and I passed»", "«ve uğradım»", segments=[seg("وَ", "wa", "conj"), seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")])
def imma(w=False): return tok("وَإِمَّا" if w else "إِمَّا", "imma", "part", [K, AT, TQ], ("الْوَاوُ عَاطِفَةٌ، وَإِمَّا" if w else "إِمَّا") + " حَرْفُ تَفْصِيلٍ.", "«or either»" if w else "«either»", "«ya da»" if w else "«ya»", segments=wa("إِمَّا", "imma", "part") if w else None)
def bi_sign(form, lex, en, tr, w=False, extra=()):
    base = form[2:] if w else form
    if w: return tok(form, lex, "noun", [K, AT, HJ, IRB] + list(extra), "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَ" + base[2:] + " مَجْرُورٌ — مَعْطُوفٌ.", en, tr, segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg(base[2:], lex, "noun")])
    return tok(form, lex, "noun", [K, HJ, IRB] + list(extra), "الْبَاءُ حَرْفُ جَرٍّ، وَ" + form[2:] + " مَجْرُورٌ.", en, tr, segments=[seg("بِ", "bi", "prep"), seg(form[2:], lex, "noun")])
def wsign(form, lex, en, tr, extra=()): return tok(form, lex, "noun", [K, AT, IRB] + list(extra), "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ مَجْرُورٌ.", en, tr, segments=wa(form[2:], lex, "noun"))
def rafan(): return tok("رَفْعًا", "raf", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ — حَالَ الرَّفْعِ.", "«in rafʿ»", "«ref'te»")
def nasban(): return tok("نَصْبًا", "nasb", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ.", "«in naṣb»", "«nasbda»")
def wajarran(): return tok("وَجَرًّا", "jarr", "noun", [K, AT, "hal", MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَرًّا مَعْطُوفٌ مَنْصُوبٌ.", "«and in jarr»", "«ve cerde»", punct="،", segments=wa("جَرًّا", "jarr", "noun"))
def fahuwa(): return tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=fa("هُوَ", "huwa", "pron"))

# ----------- s1 — deficient by two vowels: the non-declinable
S.append({"id": "s1", "translation": {"en": "or deficient in iʿrāb by two vowels: either by ḍamma in rafʿ and fatḥa in naṣb and jarr — and that is the non-declinable, as in «there came to me Aḥmad», «and I saw Aḥmad», «and I passed by Aḥmad»;", "tr": "ya da iki hareke ile i'râbı nâkıs olandır: ya ref'te damme, nasb ve cerde fetha ile — o da gayr-ı munsariftir: «bana Ahmed geldi», «Ahmed'i gördüm», «Ahmed'e uğradım» gibi;"},
 "tokens": [
  tok("أَوْ", "aw", "part", [K, AT, TQ], "حَرْفُ عَطْفٍ — عَلَى تَامُّ الْإِعْرَابِ.", "«or»", "«ya da»"),
  tok("نَاقِصُ", "naqis", "noun", [K, AT, ID, IFA, MQ], "مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ ظَاهِرَةٍ لِلْإِضَافَةِ، مُضَافٌ.", "«deficient in»", "«nâkıs»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbı»"),
  tok("بِالْحَرَكَتَيْنِ", "haraka", "noun", [K, HJ, MTH, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرَكَتَيْنِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«by two vowels» — a dual in jarr by the yāʾ.", "«iki hareke ile» — yâ ile mecrûr tesniye.", punct=":", segments=[seg("بِ", "bi", "prep"), seg("الْحَرَكَتَيْنِ", "haraka", "noun")]),
  imma(),
  bi_sign("بِالضَّمَّةِ", "damma", "«by ḍamma»", "«damme ile»"),
  rafan(),
  wsign("وَالْفَتْحَةِ", "fatha", "«and fatḥa»", "«ve fetha»"),
  nasban(),
  wajarran(),
  fahuwa(),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID, MMS], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the non-»", "«gayr-ı»"),
  tok("الْمُنْصَرِفِ", "munsarif", "noun", [K, ID, IFA, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَمْنُوعُ مِنَ الصَّرْفِ.", "«declinable» — the diptote.", "«munsarif» — gayr-ı munsarif.", punct="،"),
  nahw(),
  jaani(),
  tok("أَحْمَدُ", "ahmad", "propn", [K, FL, MMS, IRB], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ عَلَى وَزْنِ الْفِعْلِ، غَيْرُ مُنْصَرِفٍ.", "«Aḥmad» — rafʿ by ḍamma; a diptote.", "«Ahmed» — damme ile merfû; gayr-ı munsarif.", punct="،"),
  waraaytu(),
  tok("أَحْمَدَ", "ahmad", "propn", [K, MB, MMS, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Aḥmad» — naṣb by fatḥa.", "«Ahmed'i» — fetha ile mansûb.", punct="،"),
  wamarartu(),
  tok("بِأَحْمَدَ", "ahmad", "propn", [K, HJ, MMS, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَأَحْمَدَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ غَيْرُ مُنْصَرِفٍ.", "«by Aḥmad» — jarr by fatḥa in place of kasra.", "«Ahmed'e» — kesre yerine fetha ile mecrûr.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("أَحْمَدَ", "ahmad", "propn")]),
 ]})
# ----------- s2 — deficient by two vowels: the sound feminine plural
S.append({"id": "s2", "translation": {"en": "or by ḍamma in rafʿ and kasra in naṣb and jarr — and that is the sound feminine plural, as in «there came to me Muslim women», «and I saw Muslim women», «and I passed by Muslim women».", "tr": "ya da ref'te damme, nasb ve cerde kesre ile — o da cem'-i müennes-i sâlimdir: «bana müslüman kadınlar geldi», «müslüman kadınları gördüm», «müslüman kadınlara uğradım» gibi."},
 "tokens": [
  imma(w=True),
  bi_sign("بِالضَّمَّةِ", "damma", "«by ḍamma»", "«damme ile»"),
  rafan(),
  wsign("وَالْكَسْرَةِ", "kasra", "«and kasra»", "«ve kesre»"),
  nasban(),
  wajarran(),
  fahuwa(),
  tok("جَمْعُ", "jam", "noun", [K, MK, ID, JMS], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the plural of»", "«cem'-i»"),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, ID, IMF, F2, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine»", "«müennes»"),
  tok("السَّالِمُ", "salim", "noun", [K, NA, IFA, JMS], "نَعْتٌ لِجَمْعُ مَرْفُوعٌ.", "«sound»", "«sâlim»", punct="،"),
  nahw(),
  jaani(),
  tok("مُسْلِمَاتٌ", "muslima", "noun", [K, FL, JMS, IRB], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Muslim women» — rafʿ by ḍamma.", "«müslüman kadınlar» — damme ile merfû.", punct="،"),
  waraaytu(),
  tok("مُسْلِمَاتٍ", "muslima", "noun", [K, MB, JMS, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ.", "«Muslim women» — naṣb by kasra in place of fatḥa.", "«müslüman kadınları» — fetha yerine kesre ile mansûb.", punct="،"),
  wamarartu(),
  tok("بِمُسْلِمَاتٍ", "muslima", "noun", [K, HJ, JMS, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَمُسْلِمَاتٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«by Muslim women» — jarr by kasra.", "«müslüman kadınlara» — kesre ile mecrûr.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("مُسْلِمَاتٍ", "muslima", "noun")]),
 ]})
# ----------- s3 — the second locus: complete by the three letters — the six nouns
S.append({"id": "s3", "translation": {"en": "And the second, likewise, is either complete in iʿrāb by the three letters — by wāw in rafʿ, alif in naṣb and yāʾ in jarr — and that is the six nouns, annexed to other than the speaker's yāʾ, singular and un-diminished;", "tr": "İkincisi de ya üç harf ile i'râbı tam olandır — ref'te vâv, nasbda elif, cerde yâ ile — o da mütekellim yâsından başkasına muzâf, müfred ve mükebber olan altı isimdir;"},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — الْمُعْرَبُ بِالْحُرُوفِ الْمَحْضَةِ.", "«and the second» — the one declined by pure letters.", "«ikincisi» — sırf harflerle mu'reb olan.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("أَيْضًا", "aydan", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ أَيْضًا.", "«likewise»", "«de»"),
  imma(),
  tok("تَامُّ", "tamm", "noun", [K, MK, ID, "doubled-verbs"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«complete in»", "«tam»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbı»"),
  tok("بِالْحُرُوفِ", "harf", "noun", [K, HJ, JT, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحُرُوفِ مَجْرُورٌ.", "«by the letters»", "«harflerle»", segments=[seg("بِ", "bi", "prep"), seg("الْحُرُوفِ", "harf", "noun")]),
  tok("الثَّلَاثَةِ", "thalatha", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ — الطَّبْعُ: الثلثة.", "«three» — the print spells it الثلثة.", "«üç» — baskıda الثلثة.", punct=":"),
  bi_sign("بِالْوَاوِ", "waw-letter", "«by wāw»", "«vâv ile»"),
  rafan(),
  wsign("وَالْأَلِفِ", "alif-letter", "«and alif»", "«ve elif»"),
  nasban(),
  wsign("وَالْيَاءِ", "ya-letter", "«and yāʾ»", "«ve yâ»"),
  tok("جَرًّا", "jarr", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ.", "«in jarr»", "«cerde»", punct="،"),
  fahuwa(),
  tok("الْأَسْمَاءُ", "ism", "noun", [K, MK, JT, FN], "خَبَرٌ مَرْفُوعٌ.", "«the nouns»", "«isimler»"),
  tok("السِّتَّةُ", "sitta", "noun", [K, NA, FN], "نَعْتٌ مَرْفُوعٌ — أَبٌ، أَخٌ، حَمٌ، هَنٌ، فُو، ذُو.", "«six» — ab, akh, ḥam, han, fū, dhū.", "«altı» — eb, ah, ham, hen, fû, zû."),
  tok("الْمُضَافَةُ", "mudaf", "noun", [K, NA, IMF, F4, ID, FN], "نَعْتٌ ثَانٍ مَرْفُوعٌ — شَرْطُ إِعْرَابِهَا بِالْحُرُوفِ.", "«annexed» — the condition of their letter-iʿrāb.", "«muzâf olan» — harfle i'râbın şartı."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«other than»", "«başkasına»"),
  tok("يَاءِ", "ya-letter", "noun", [K, ID, YM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the yāʾ of»", "«yâsından»"),
  tok("الْمُتَكَلِّمِ", "mutakallim", "noun", [K, ID, IFA, F5, YM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَأَبِي لَا يُعْرَبُ بِالْحُرُوفِ.", "«the speaker» — so أَبِي takes no letter-iʿrāb.", "«mütekellim» — ebî harfle i'râblanmaz.", punct="،"),
  tok("الْمُفْرَدَةُ", "mufrad", "noun", [K, NA, IMF, F4, FN], "نَعْتٌ ثَالِثٌ مَرْفُوعٌ — لَا الْمُثَنَّاةُ وَلَا الْمَجْمُوعَةُ.", "«singular» — not dual or plural.", "«müfred» — tesniye ve cemi değil."),
  tok("الْمُكَبَّرَةُ", "mukabbar", "noun", [K, NA, IMF, F2, FN], "نَعْتٌ رَابِعٌ مَرْفُوعٌ — لَا الْمُصَغَّرَةُ كَأُبَيٍّ.", "«un-diminished» — not a diminutive like ubayy.", "«mükebber» — übeyy gibi tasgîr edilmiş değil.", punct="،"),
 ]})
# ----------- s4 — deficient by two letters: wāw / yāʾ
S.append({"id": "s4", "translation": {"en": "or deficient in iʿrāb by two letters: either by wāw in rafʿ and yāʾ in naṣb and jarr — and that is the sound masculine plural, and ulū, and ʿishrūn and its sisters — as in «there came to me Muslims and men of wealth and twenty», «and I saw Muslims and men of wealth and twenty», «and I passed by Muslims and men of wealth and twenty»;", "tr": "ya da iki harf ile i'râbı nâkıs olandır: ya ref'te vâv, nasb ve cerde yâ ile — o da cem'-i müzekker-i sâlim, ulû, işrûn ve kardeşleridir — «bana müslümanlar, mal sahipleri ve yirmi geldi», «müslümanları, mal sahiplerini ve yirmiyi gördüm», «müslümanlara, mal sahiplerine ve yirmiye uğradım» gibi;"},
 "tokens": [
  imma(w=True),
  tok("نَاقِصُ", "naqis", "noun", [K, MK, ID, IFA, MQ], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«deficient in»", "«nâkıs»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbı»"),
  tok("بِالْحَرْفَيْنِ", "harf", "noun", [K, HJ, MTH, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرْفَيْنِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«by two letters»", "«iki harf ile»", punct=":", segments=[seg("بِ", "bi", "prep"), seg("الْحَرْفَيْنِ", "harf", "noun")]),
  imma(),
  bi_sign("بِالْوَاوِ", "waw-letter", "«by wāw»", "«vâv ile»"),
  rafan(),
  wsign("وَالْيَاءِ", "ya-letter", "«and yāʾ»", "«ve yâ»"),
  nasban(),
  wajarran(),
  fahuwa(),
  tok("جَمْعُ", "jam", "noun", [K, MK, ID, JDS], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the plural of»", "«cem'-i»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, IMF, F2, JDS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekker»"),
  tok("السَّالِمُ", "salim", "noun", [K, NA, IFA, JDS], "نَعْتٌ لِجَمْعُ مَرْفُوعٌ.", "«sound»", "«sâlim»"),
  tok("وَأُولُو", "ulu", "noun", [K, AT, JDS, FN], "الْوَاوُ عَاطِفَةٌ، وَأُولُو مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِالْجَمْعِ، لَا وَاحِدَ لَهُ مِنْ لَفْظِهِ.", "«and ulū» — attached to the plural, with no singular of its own form.", "«ve ulû» — cemiye mülhak, kendi lafzından tekili yok.", segments=wa("أُولُو", "ulu", "noun")),
  tok("وَعِشْرُونَ", "ishrun", "noun", [K, AT, JDS], "الْوَاوُ عَاطِفَةٌ، وَعِشْرُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ.", "«and twenty»", "«ve yirmi»", segments=wa("عِشْرُونَ", "ishrun", "noun")),
  tok("وَأَخَوَاتُهَا", "ukht", "noun", [K, AT, ID, JMS, JDS], "الْوَاوُ عَاطِفَةٌ، وَأَخَوَاتُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — ثَلَاثُونَ إِلَى تِسْعِينَ.", "«and its sisters» — thirty to ninety.", "«ve kardeşleri» — otuzdan doksana.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("أَخَوَاتُ", "ukht", "noun"), pr3fs()]),
  nahw(),
  jaani(),
  tok("مُسْلِمُونَ", "muslim", "noun", [K, FL, JDS, IRB], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ.", "«Muslims» — rafʿ by the wāw.", "«müslümanlar» — vâv ile merfû."),
  tok("وَأُولُو", "ulu", "noun", [K, AT, JDS, ID, IRB], "الْوَاوُ عَاطِفَةٌ، وَأُولُو مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ.", "«and men of»", "«ve sahipleri»", segments=wa("أُولُو", "ulu", "noun")),
  tok("مَالٍ", "mal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wealth»", "«mal»"),
  tok("وَعِشْرُونَ", "ishrun", "noun", [K, AT, JDS, IRB], "الْوَاوُ عَاطِفَةٌ، وَعِشْرُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ.", "«and twenty»", "«ve yirmi»", punct="،", segments=wa("عِشْرُونَ", "ishrun", "noun")),
  waraaytu(),
  tok("مُسْلِمِينَ", "muslim", "noun", [K, MB, JDS, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«Muslims» — naṣb by the yāʾ.", "«müslümanları» — yâ ile mansûb."),
  tok("وَأُولِي", "ulu", "noun", [K, AT, JDS, ID, IRB], "الْوَاوُ عَاطِفَةٌ، وَأُولِي مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ، مُضَافٌ.", "«and men of»", "«ve sahiplerini»", segments=wa("أُولِي", "ulu", "noun")),
  tok("مَالٍ", "mal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wealth»", "«mal»"),
  tok("وَعِشْرِينَ", "ishrun", "noun", [K, AT, JDS, IRB], "الْوَاوُ عَاطِفَةٌ، وَعِشْرِينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ.", "«and twenty»", "«ve yirmiyi»", punct="،", segments=wa("عِشْرِينَ", "ishrun", "noun")),
  wamarartu(),
  tok("بِمُسْلِمِينَ", "muslim", "noun", [K, HJ, JDS, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَمُسْلِمِينَ مَجْرُورٌ بِالْيَاءِ.", "«by Muslims» — jarr by the yāʾ.", "«müslümanlara» — yâ ile mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("مُسْلِمِينَ", "muslim", "noun")]),
  tok("وَأُولِي", "ulu", "noun", [K, AT, JDS, ID, IRB], "الْوَاوُ عَاطِفَةٌ، وَأُولِي مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«and men of»", "«ve sahiplerine»", segments=wa("أُولِي", "ulu", "noun")),
  tok("مَالٍ", "mal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wealth»", "«mal»"),
  tok("وَعِشْرِينَ", "ishrun", "noun", [K, AT, JDS, IRB], "الْوَاوُ عَاطِفَةٌ، وَعِشْرِينَ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ.", "«and twenty»", "«ve yirmiye»", punct="،", segments=wa("عِشْرِينَ", "ishrun", "noun")),
 ]})
# ----------- s5 — deficient by two letters: alif / yāʾ
S.append({"id": "s5", "translation": {"en": "or by alif in rafʿ and yāʾ in naṣb and jarr — and that is the dual, and ithnān, and kilā annexed to a pronoun — as in «there came to me two Muslims and two and both of them», «and I saw two Muslims and two and both of them», «and I passed by two Muslims and two and both of them».", "tr": "ya da ref'te elif, nasb ve cerde yâ ile — o da tesniye, isnân ve zamire muzâf kilâ'dır — «bana iki müslüman, iki ve her ikisi geldi», «iki müslümanı, ikiyi ve her ikisini gördüm», «iki müslümana, ikiye ve her ikisine uğradım» gibi."},
 "tokens": [
  tok("أَوْ", "aw", "part", [K, AT, TQ], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  bi_sign("بِالْأَلِفِ", "alif-letter", "«by alif»", "«elif ile»"),
  rafan(),
  wsign("وَالْيَاءِ", "ya-letter", "«and yāʾ»", "«ve yâ»"),
  nasban(),
  wajarran(),
  fahuwa(),
  tok("الْمُثَنَّى", "muthanna", "noun", [K, MK, IMF, F2, MTH, MQ], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمٌ مَقْصُورٌ.", "«the dual»", "«tesniye»"),
  tok("وَاثْنَانِ", "ithnan", "noun", [K, AT, MTH], "الْوَاوُ عَاطِفَةٌ، وَاثْنَانِ مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ — مُلْحَقٌ بِالْمُثَنَّى.", "«and ithnān» — attached to the dual.", "«ve isnân» — tesniyeye mülhak.", segments=wa("اثْنَانِ", "ithnan", "noun")),
  tok("وَكِلَا", "kila", "noun", [K, AT, MTH, TK], "الْوَاوُ عَاطِفَةٌ، وَكِلَا مَعْطُوفٌ مَرْفُوعٌ بِأَلِفٍ مُقَدَّرَةٍ.", "«and kilā»", "«ve kilâ»", segments=wa("كِلَا", "kila", "noun")),
  tok("مُضَافًا", "mudaf", "noun", [K, "hal", IMF, F4, ID], "حَالٌ مِنْ كِلَا مَنْصُوبٌ — شَرْطُ إِعْرَابِهِ بِالْحُرُوفِ.", "«annexed» — a ḥāl: the condition for its letter-iʿrāb.", "«muzâf olarak» — hâl: harfle i'râbın şartı."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مُضْمَرٍ", "mudmar", "noun", [K, HJ, IMF, F4, BM], "مَجْرُورٌ بِإِلَى — فَإِنْ أُضِيفَ إِلَى الظَّاهِرِ فَبِالْأَلِفِ فِي الْأَحْوَالِ كُلِّهَا.", "«a pronoun» — annexed to an apparent noun it keeps the alif throughout.", "«zamire» — zâhire muzâf olunca her halde elifle kalır.", punct="،"),
  nahw(),
  jaani(),
  tok("مُسْلِمَانِ", "muslim", "noun", [K, FL, MTH, IRB], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two Muslims» — rafʿ by the alif.", "«iki müslüman» — elif ile merfû."),
  tok("وَاثْنَانِ", "ithnan", "noun", [K, AT, MTH, IRB], "الْوَاوُ عَاطِفَةٌ، وَاثْنَانِ مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ.", "«and two»", "«ve iki»", segments=wa("اثْنَانِ", "ithnan", "noun")),
  tok("وَكِلَاهُمَا", "kila", "noun", [K, AT, MTH, ID, TK, IRB], "الْوَاوُ عَاطِفَةٌ، وَكِلَا مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and both of them»", "«ve her ikisi»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("كِلَا", "kila", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  waraaytu(),
  tok("مُسْلِمَيْنِ", "muslim", "noun", [K, MB, MTH, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«two Muslims» — naṣb by the yāʾ.", "«iki müslümanı» — yâ ile mansûb."),
  tok("وَاثْنَيْنِ", "ithnan", "noun", [K, AT, MTH, IRB], "الْوَاوُ عَاطِفَةٌ، وَاثْنَيْنِ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ.", "«and two»", "«ve ikiyi»", segments=wa("اثْنَيْنِ", "ithnan", "noun")),
  tok("وَكِلَيْهِمَا", "kila", "noun", [K, AT, MTH, ID, TK, IRB], "الْوَاوُ عَاطِفَةٌ، وَكِلَيْ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«and both of them»", "«ve her ikisini»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("كِلَيْ", "kila", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  wamarartu(),
  tok("بِمُسْلِمَيْنِ", "muslim", "noun", [K, HJ, MTH, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَمُسْلِمَيْنِ مَجْرُورٌ بِالْيَاءِ.", "«by two Muslims» — jarr by the yāʾ.", "«iki müslümana» — yâ ile mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("مُسْلِمَيْنِ", "muslim", "noun")]),
  tok("وَاثْنَيْنِ", "ithnan", "noun", [K, AT, MTH, IRB], "الْوَاوُ عَاطِفَةٌ، وَاثْنَيْنِ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ.", "«and two»", "«ve ikiye»", segments=wa("اثْنَيْنِ", "ithnan", "noun")),
  tok("وَكِلَيْهِمَا", "kila", "noun", [K, AT, MTH, ID, TK, IRB], "الْوَاوُ عَاطِفَةٌ، وَكِلَيْ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«and both of them»", "«ve her ikisine»", punct=".", segments=[seg("وَ", "wa", "conj"), seg("كِلَيْ", "kila", "noun"), seg("هِمَا", "pron-3d", "pron")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "mukabbar": G("mukabbar", "مُكَبَّر", "ك ب ر", "noun", "un-diminished, in its full (non-diminutive) form", "mükebber, tasgîr edilmemiş (büyük şekliyle)", 4),
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
print("izhar ch53 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaa", "raa", "marra") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "نَاقِصُ الْإِعْرَابِ بِالْحَرَكَتَيْنِ: غَيْرُ الْمُنْصَرِفِ وَجَمْعُ الْمُؤَنَّثِ السَّالِمُ، وَالْمُعْرَبُ بِالْحُرُوفِ: الْأَسْمَاءُ السِّتَّةُ، وَجَمْعُ الْمُذَكَّرِ وَمُلْحَقَاتُهُ، وَالْمُثَنَّى وَمُلْحَقَاتُهُ", "en": "Deficient iʿrāb by two vowels: the diptote and the sound feminine plural; iʿrāb by letters: the six nouns, the sound masculine plural with ulū and ʿishrūn, the dual with ithnān and kilā", "tr": "İki hareke ile nâkıs i'râb: gayr-ı munsarif ve cem'-i müennes-i sâlim; harflerle i'râb: altı isim, ulû ve işrûn ile cem'-i müzekker, isnân ve kilâ ile tesniye"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الإعراب: التقسيم بحسب المحل", "الكافية لابن الحاجب — المعرب بالحروف", "شرح قطر الندى لابن هشام — الأسماء الستة والمثنى والجمع"],
 "amil": "deficient iʿrāb by two vowels: ḍamma in rafʿ and fatḥa in naṣb and jarr — the diptote (أَحْمَدُ، أَحْمَدَ، بِأَحْمَدَ); ḍamma in rafʿ and kasra in naṣb and jarr — the sound feminine plural (مُسْلِمَاتٌ، مُسْلِمَاتٍ، بِمُسْلِمَاتٍ). By letters, complete: wāw/alif/yāʾ in the six nouns when annexed to other than the speaker's yāʾ, singular and un-diminished. Deficient by two letters: wāw/yāʾ in the sound masculine plural, أُولُو, عِشْرُونَ and its sisters; alif/yāʾ in the dual, اثْنَانِ and كِلَا annexed to a pronoun.",
 "question": {
  "en": ["Which nouns are deficient in iʿrāb by two vowels? The diptote (ḍamma in rafʿ, fatḥa for both naṣb and jarr: بِأَحْمَدَ) and the sound feminine plural (ḍamma in rafʿ, kasra for both naṣb and jarr: رَأَيْتُ مُسْلِمَاتٍ).",
         "Why is بِأَحْمَدَ in fatḥa? Because the diptote takes no kasra; the fatḥa stands in for it — unless annexed or given the article, as the next chapters say.",
         "What are the six nouns, and when do they take letters? أَب، أَخ، حَم، هَن، فُو، ذُو — when annexed to other than the speaker's yāʾ, singular and un-diminished: أَبُوهُ، أَبَاهُ، بِأَبِيهِ; but أَبِي, أَبَوَانِ, أُبَيّ fall outside.",
         "What takes wāw in rafʿ and yāʾ in naṣb and jarr? The sound masculine plural and what is attached to it: أُولُو and the tens عِشْرُونَ to تِسْعُونَ — مُسْلِمُونَ وَأُولُو مَالٍ وَعِشْرُونَ, then مُسْلِمِينَ وَأُولِي مَالٍ وَعِشْرِينَ.",
         "What takes alif in rafʿ and yāʾ in naṣb and jarr? The dual and what is attached to it: اثْنَانِ and كِلَا when annexed to a pronoun — كِلَاهُمَا, كِلَيْهِمَا; annexed to an apparent noun, كِلَا keeps its alif in every case.",
         "Why is ulū attached rather than a true plural? It has no singular of its own form; it is declined like the plural but is not formed from one.",
         "Where does the print's ثلثة spelling appear? The lithograph writes الثلثة for الثَّلَاثَةِ, the old orthography without alif; the text reads it in the standard way.",
         "What does the engine READ here? The DabtEngine reads أَحْمَدَ after the bāʾ as a diptote in jarr by fatḥa, مُسْلِمَاتٍ after رَأَيْتُ as naṣb by kasra, مُسْلِمُونَ/مُسْلِمِينَ by wāw and yāʾ, أُولُو/أُولِي and عِشْرُونَ/عِشْرِينَ as attached plurals, and مُسْلِمَانِ/مُسْلِمَيْنِ, اثْنَانِ/اثْنَيْنِ, كِلَاهُمَا/كِلَيْهِمَا as duals by alif and yāʾ."],
  "tr": ["Hangi isimlerin i'râbı iki hareke ile nâkıstır? Gayr-ı munsarif (ref'te damme, nasb ve cerde fetha: bi-Ahmede) ve cem'-i müennes-i sâlim (ref'te damme, nasb ve cerde kesre: raeytü müslimâtin).",
         "Bi-Ahmede neden fethalı? Gayr-ı munsarif kesre almaz; fetha onun yerine geçer — izafet ya da harf-i tarif olmadıkça, sonraki bablarda geleceği gibi.",
         "Altı isim nedir, ne zaman harf alır? Eb, ah, ham, hen, fû, zû — mütekellim yâsından başkasına muzâf, müfred ve mükebber olunca: ebûhü, ebâhü, bi-ebîhi; ebî, ebevâni, übeyy dışarıda kalır.",
         "Ref'te vâv, nasb ve cerde yâ alan nedir? Cem'-i müzekker-i sâlim ve ona mülhak olanlar: ulû ve işrûn'dan tis'ûn'a onlar — müslimûne ve ulû mâlin ve işrûne, sonra müslimîne ve ulî mâlin ve işrîne.",
         "Ref'te elif, nasb ve cerde yâ alan nedir? Tesniye ve ona mülhak olanlar: isnân ve zamire muzâf kilâ — kilâhümâ, kileyhimâ; zâhire muzâf olunca kilâ her halde elifini korur.",
         "Ulû neden gerçek cemi değil de mülhak? Kendi lafzından tekili yok; cemi gibi i'râblanır ama ondan türememiştir.",
         "Baskının ثلثة imlâsı nerede görünür? Litografi es-selâseti için الثلثة yazar, elifsiz eski imlâ; metin standart okunuşla verir.",
         "Motor burada neyi OKUR? DabtEngine bâ'dan sonra Ahmede'yi fetha ile mecrûr gayr-ı munsarif, raeytü'den sonra müslimâtin'i kesre ile mansûb, müslimûne/müslimîne'yi vâv ve yâ ile, ulû/ulî ve işrûne/işrîne'yi mülhak cemi, müslimâni/müslimeyni, isnâni/isneyni, kilâhümâ/kileyhimâ'yı elif ve yâ ile tesniye olarak okur."],
 },
 "plain": {"en": "Some nouns use only two vowels: diptotes like Aḥmad (u for subject, a for everything else) and feminine plurals in -āt (u, then i). Others change letters instead: «his father» (abū-hu, abā-hu, abī-hi), masculine plurals (-ūna / -īna), «twenty» and «men of», and duals (-āni / -ayni), including «two» and «both».",
           "tr": "Bazı isimler yalnız iki hareke kullanır: Ahmed gibi gayr-ı munsarifler (özne için u, gerisi için a) ve -ât ile biten dişil çoğullar (u, sonra i). Bazıları harf değiştirir: «babası» (ebû-hü, ebâ-hü, ebî-hi), eril çoğullar (-ûne / -îne), «yirmi» ve «sahipleri», tesniyeler (-âni / -eyni), «iki» ve «her ikisi» dahil."},
 "explanation": {"en": "The locus-division continues. Deficient iʿrāb by two vowels is of two kinds: by ḍamma in rafʿ and fatḥa in naṣb and jarr — the non-declinable: جَاءَنِي أَحْمَدُ، رَأَيْتُ أَحْمَدَ، مَرَرْتُ بِأَحْمَدَ; and by ḍamma in rafʿ and kasra in naṣb and jarr — the sound feminine plural: جَاءَنِي مُسْلِمَاتٌ، رَأَيْتُ مُسْلِمَاتٍ، مَرَرْتُ بِمُسْلِمَاتٍ. The second locus, the pure letters, is likewise either complete by the three letters — wāw in rafʿ, alif in naṣb, yāʾ in jarr — which is the six nouns annexed to other than the speaker's yāʾ, singular and un-diminished; or deficient by two letters: wāw in rafʿ and yāʾ in naṣb and jarr — the sound masculine plural, أُولُو, and عِشْرُونَ with its sisters: جَاءَنِي مُسْلِمُونَ وَأُولُو مَالٍ وَعِشْرُونَ، رَأَيْتُ مُسْلِمِينَ وَأُولِي مَالٍ وَعِشْرِينَ، مَرَرْتُ بِمُسْلِمِينَ وَأُولِي مَالٍ وَعِشْرِينَ; or alif in rafʿ and yāʾ in naṣb and jarr — the dual, اثْنَانِ, and كِلَا annexed to a pronoun: جَاءَنِي مُسْلِمَانِ وَاثْنَانِ وَكِلَاهُمَا، رَأَيْتُ مُسْلِمَيْنِ وَاثْنَيْنِ وَكِلَيْهِمَا، مَرَرْتُ بِمُسْلِمَيْنِ وَاثْنَيْنِ وَكِلَيْهِمَا. The lithograph writes الثلثة in the old orthography.",
                 "tr": "Mahal taksimi sürer. İki hareke ile nâkıs i'râb iki türlüdür: ref'te damme, nasb ve cerde fetha ile — gayr-ı munsarif: câenî Ahmedü, raeytü Ahmede, merartü bi-Ahmede; ref'te damme, nasb ve cerde kesre ile — cem'-i müennes-i sâlim: câenî müslimâtün, raeytü müslimâtin, merartü bi-müslimâtin. İkinci mahal, sırf harfler, aynı şekilde ya üç harf ile tamdır — ref'te vâv, nasbda elif, cerde yâ — o da mütekellim yâsından başkasına muzâf, müfred ve mükebber altı isimdir; ya da iki harf ile nâkıstır: ref'te vâv, nasb ve cerde yâ — cem'-i müzekker-i sâlim, ulû ve kardeşleriyle işrûn: câenî müslimûne ve ulû mâlin ve işrûne, raeytü müslimîne ve ulî mâlin ve işrîne, merartü bi-müslimîne ve ulî mâlin ve işrîne; ya ref'te elif, nasb ve cerde yâ — tesniye, isnân ve zamire muzâf kilâ: câenî müslimâni ve'snâni ve kilâhümâ, raeytü müslimeyni ve'sneyni ve kileyhimâ, merartü bi-müslimeyni ve'sneyni ve kileyhimâ. Litografi الثلثة'yi eski imlâ ile yazar."},
 "examples": [
  {"ar": "جَاءَنِي أَحْمَدُ، وَرَأَيْتُ أَحْمَدَ، وَمَرَرْتُ بِأَحْمَدَ", "en": "the diptote by two vowels", "tr": "iki hareke ile gayr-ı munsarif", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "جَاءَنِي مُسْلِمَاتٌ، وَرَأَيْتُ مُسْلِمَاتٍ، وَمَرَرْتُ بِمُسْلِمَاتٍ", "en": "the sound feminine plural", "tr": "cem'-i müennes-i sâlim", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "الْأَسْمَاءُ السِّتَّةُ الْمُضَافَةُ إِلَى غَيْرِ يَاءِ الْمُتَكَلِّمِ الْمُفْرَدَةُ الْمُكَبَّرَةُ", "en": "the six nouns and their conditions", "tr": "altı isim ve şartları", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "جَاءَنِي مُسْلِمُونَ وَأُولُو مَالٍ وَعِشْرُونَ", "en": "the sound masculine plural and its attachments", "tr": "cem'-i müzekker-i sâlim ve mülhakları", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "رَأَيْتُ مُسْلِمَيْنِ وَاثْنَيْنِ وَكِلَيْهِمَا", "en": "the dual and its attachments", "tr": "tesniye ve mülhakları", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "مَرَرْتُ بِأَحْمَدٍ", "right": "مَرَرْتُ بِأَحْمَدَ", "why": {"en": "the diptote takes neither kasra nor tanwīn; its jarr is by fatḥa", "tr": "gayr-ı munsarif ne kesre ne tenvin alır; ceri fetha iledir"}},
  {"wrong": "رَأَيْتُ مُسْلِمَاتًا", "right": "رَأَيْتُ مُسْلِمَاتٍ", "why": {"en": "the sound feminine plural takes naṣb by kasra", "tr": "cem'-i müennes-i sâlim nasbı kesre ile alır"}},
  {"wrong": "رَأَيْتُ أُولُو مَالٍ", "right": "رَأَيْتُ أُولِي مَالٍ", "why": {"en": "ulū is declined like the sound masculine plural: yāʾ in naṣb", "tr": "ulû cem'-i müzekker-i sâlim gibi i'râblanır: nasbda yâ"}},
  {"wrong": "رَأَيْتُ كِلَاهُمَا", "right": "رَأَيْتُ كِلَيْهِمَا", "why": {"en": "kilā annexed to a pronoun takes yāʾ in naṣb and jarr like the dual", "tr": "zamire muzâf kilâ nasb ve cerde tesniye gibi yâ alır"}},
 ],
}
ADD_EN = (" Chapter 53 (print pp. 148-149): deficient iʿrāb by two vowels — the diptote (s1) and the sound feminine plural (s2); iʿrāb by letters — complete in the six nouns under their conditions (s3), deficient by wāw/yāʾ in the sound masculine plural, ulū and the tens (s4), by alif/yāʾ in the dual, ithnān and kilā (s5).")
ADD_TR = (" Elli üçüncü bab (baskı s. 148-149): iki hareke ile nâkıs i'râb — gayr-ı munsarif (s1) ve cem'-i müennes-i sâlim (s2); harflerle i'râb — şartlarıyla altı isimde tam (s3), cem'-i müzekker-i sâlim, ulû ve onlarda vâv/yâ ile nâkıs (s4), tesniye, isnân ve kilâ'da elif/yâ ile (s5).")
write_out(53, S, TITLE, ADD_EN, ADD_TR, "pp. 148-149", GLOSS_ADD, notes=(NOTE,),
          related=((K52, [K]), (MMS, [K]), (JMS, [K]), (JDS, [K]), (FN, [K]), (MTH, [K])))
report(53, S, GLOSS_ADD, (NOTE,))
