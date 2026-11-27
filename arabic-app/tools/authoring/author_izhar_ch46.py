# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 46: the six maʿrifas — the FIRST kind, the pronouns, four divisions: the attached rafʿ (passed), the detached rafʿ
# (هُوَ … نَحْنُ), the one shared between attached naṣb and attached jarr (ضَرَبَهُ … ضَرَبَنَا، لَهُ etc.), the detached naṣb (إِيَّاهُ … إِيَّانَا); the SECOND kind,
# the proper name, two divisions: of a person (زَيْدٌ) and of a genus (أُسَامَةُ، سُبْحَانَ). Print p. 142.
#   python3 author_izhar_ch46.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TRF = "tarif-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; DF = "damir-fasl"; MMB = "al-murab-wal-mabni-wal-irab"; MNS = "mamnu-min-sarf"
K = "al-marifa-al-mudmarat-wal-alam"
K45 = "al-tawabi-wal-sifa"
TITLE = {"ar": "أَنْوَاعُ الْمَعْرِفَةِ: الْمُضْمَرَاتُ وَأَقْسَامُهَا الْأَرْبَعَةُ، وَالْعَلَمُ وَقِسْمَاهُ", "en": "The kinds of maʿrifa: the pronouns and their four divisions, and the proper name with its two divisions", "tr": "Ma'rifenin nev'leri: zamirler ve dört kısmı, alem ve iki kısmı"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wahuwa(): return tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o da»", punct=":", segments=wa("هُوَ", "huwa", "pron"))
def P(form, lex, en, tr, punct=None): return tok(form, lex, "pron", [K, BM, MMB], "لَفْظٌ مَحْكِيٌّ: ضَمِيرٌ مَبْنِيٌّ.", en, tr, punct=punct)
def D(obj, lex, en, tr, punct=None): return tok("ضَرَبَ" + obj, "daraba", "verb", [K, BM, MB], "فِعْلٌ مَاضٍ، وَالضَّمِيرُ الْمُتَّصِلُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.", en, tr, punct=punct, segments=[seg("ضَرَبَ", "daraba", "verb"), seg(obj, lex, "pron")])
def I(suf, lex, en, tr, punct=None): return tok("إِيَّا" + suf, "iyya", "pron", [K, BM, MMB, MB], "لَفْظٌ مَحْكِيٌّ: ضَمِيرٌ مُنْفَصِلٌ مَنْصُوبٌ مَبْنِيٌّ.", en, tr, punct=punct, segments=[seg("إِيَّا", "iyya", "pron"), seg(suf, lex, "pron")])
def qism(ar_ord, lex_ord, en, tr): return [tok("وَالْقِسْمُ" if ar_ord != "الْأَوَّلُ" else "الْقِسْمُ", "qism", "noun", [K, AT, MK] if ar_ord != "الْأَوَّلُ" else [K, MK], ("الْوَاوُ عَاطِفَةٌ، وَ" if ar_ord != "الْأَوَّلُ" else "") + "الْقِسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division»" if ar_ord != "الْأَوَّلُ" else "«the division»", "«kısım»", segments=wa("الْقِسْمُ", "qism", "noun") if ar_ord != "الْأَوَّلُ" else None),
                                          tok(ar_ord, lex_ord, "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", en, tr)]

# ----------- s1 — the first kind: the pronouns, four divisions; the first division
S.append({"id": "s1", "translation": {"en": "The first kind is the pronouns, and they are four divisions: the first division is the attached rafʿ pronoun, and it has passed;", "tr": "Birinci nev' zamirlerdir; dört kısımdır: birinci kısım muttasıl merfû zamirdir; o geçmişti;"},
 "tokens": [
  tok("النَّوْعُ", "naw", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the kind»", "«nev'»"),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«first»", "«birinci»"),
  tok("الْمُضْمَرَاتُ", "mudmar", "noun", [K, MK, IMF, "jam-muannath-salim", TRF], "خَبَرٌ مَرْفُوعٌ.", "«the pronouns» — the khabar.", "«zamirler» — haber.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are»", "«ve onlar»", segments=wa("هِيَ", "hiya", "pron")),
  tok("أَرْبَعَةُ", "arbaa", "noun", [K, MK, ID, TMZ], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«four»", "«dört»"),
  tok("أَقْسَامٍ", "aqsam", "noun", [K, ID, JT, TMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«divisions»", "«kısım»", punct=":"),
  *qism("الْأَوَّلُ", "awwal", "«first»", "«birinci»"),
  tok("مَرْفُوعٌ", "marfu", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ — ضَمِيرٌ مَرْفُوعٌ.", "«a rafʿ one» — the khabar.", "«merfû» — haber."),
  tok("مُتَّصِلٌ", "muttasil", "noun", [K, NA, IFA, BM, "form-viii-verbs"], "نَعْتٌ مَرْفُوعٌ.", "«attached»", "«muttasıl»", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and already»", "«ve … idi»", segments=wa("قَدْ", "qad", "part")),
  tok("سَبَقَ", "sabaqa", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — فِي بَابِ الْمَرْفُوعَاتِ.", "«it has passed» — in the marfūʿāt.", "«geçmişti» — merfûlarda.", punct="،"),
 ]})
# ----------- s2 — the second division: the detached rafʿ pronouns
S.append({"id": "s2", "translation": {"en": "and the second division is the detached rafʿ pronoun, and it is: he, they two, they, she, they two, they (f.), you, you two, you (pl.), you (f.), you two, you (f. pl.), I, we;", "tr": "ikinci kısım munfasıl merfû zamirdir; o: hüve, hümâ, hüm, hiye, hümâ, hünne, ente, entümâ, entüm, enti, entümâ, entünne, ene, nahnü;"},
 "tokens": [
  *qism("الثَّانِي", "thani", "«second»", "«ikinci»"),
  tok("مَرْفُوعٌ", "marfu", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«a rafʿ one»", "«merfû»"),
  tok("مُنْفَصِلٌ", "munfasil", "noun", [K, NA, IFA, "form-vii-verbs"], "نَعْتٌ مَرْفُوعٌ.", "«detached»", "«munfasıl»", punct="،"),
  wahuwa(),
  P("هُوَ", "huwa", "«he»", "«o»"), P("هُمَا", "pron-3d", "«they two»", "«o ikisi»"), P("هُمْ", "hum", "«they»", "«onlar»"), P("هِيَ", "hiya", "«she»", "«o (dişil)»"), P("هُمَا", "pron-3d", "«they two (f.)»", "«o ikisi (dişil)»"), P("هُنَّ", "hunna", "«they (f.)»", "«onlar (dişil)»"),
  P("أَنْتَ", "anta", "«you»", "«sen»"), P("أَنْتُمَا", "antuma", "«you two»", "«siz ikiniz»"), P("أَنْتُمْ", "antum", "«you (pl.)»", "«siz»"), P("أَنْتِ", "anti", "«you (f.)»", "«sen (dişil)»"), P("أَنْتُمَا", "antuma", "«you two (f.)»", "«siz ikiniz (dişil)»"), P("أَنْتُنَّ", "antunna", "«you (f. pl.)»", "«siz (dişil)»"),
  P("أَنَا", "ana", "«I»", "«ben»"), P("نَحْنُ", "nahnu", "«we»", "«biz»", punct="،"),
 ]})
# ----------- s3 — the third division: shared between attached naṣb and attached jarr
S.append({"id": "s3", "translation": {"en": "and the third division is the one shared between the attached naṣb and the attached jarr — as in «he struck him, them two, them, her, them two, them (f.), you, you two, you (pl.), you (f.), you two, you (f. pl.), me, us», and as in «to him» and so on;", "tr": "üçüncü kısım muttasıl mansûb ile muttasıl mecrûr arasında ortak olandır — «onu, o ikisini, onları, onu (dişil), o ikisini, onları (dişil), seni, siz ikinizi, sizi, seni (dişil), siz ikinizi, sizi (dişil), beni, bizi dövdü» gibi; ve «ona» vb. gibi;"},
 "tokens": [
  *qism("الثَّالِثُ", "thalith", "«third»", "«üçüncü»"),
  tok("مُشْتَرَكٌ", "mushtarak", "noun", [K, MK, IMF, "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«shared» — the khabar.", "«müşterek» — haber."),
  tok("بَيْنَ", "bayna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasında»"),
  tok("مَنْصُوبٍ", "mansub", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a naṣb one»", "«mansûb»"),
  tok("مُتَّصِلٍ", "muttasil", "noun", [K, NA, IFA, BM], "نَعْتٌ مَجْرُورٌ.", "«attached»", "«muttasıl»"),
  tok("وَمَجْرُورٍ", "majrur", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَجْرُورٍ مَعْطُوفٌ مَجْرُورٌ.", "«and a jarr one»", "«ve mecrûr»", segments=wa("مَجْرُورٍ", "majrur", "noun")),
  tok("مُتَّصِلٍ", "muttasil", "noun", [K, NA, IFA, BM], "نَعْتٌ مَجْرُورٌ.", "«attached»", "«muttasıl»", punct="،"),
  nahw(),
  D("هُ", "pron-3ms", "«he struck him»", "«onu dövdü»"), D("هُمَا", "pron-3d", "«struck them two»", "«o ikisini»"), D("هُمْ", "pron-3mp", "«struck them»", "«onları»"), D("هَا", "pron-3fs", "«struck her»", "«onu (dişil)»"), D("هُمَا", "pron-3d", "«struck them two (f.)»", "«o ikisini (dişil)»"), D("هُنَّ", "pron-3fp", "«struck them (f.)»", "«onları (dişil)»"),
  D("كَ", "pron-2ms", "«struck you»", "«seni»"), D("كُمَا", "pron-2d", "«struck you two»", "«siz ikinizi»"), D("كُمْ", "pron-2mp", "«struck you (pl.)»", "«sizi»"), D("كِ", "pron-2fs", "«struck you (f.)»", "«seni (dişil)»"), D("كُمَا", "pron-2d", "«struck you two (f.)»", "«siz ikinizi (dişil)»"), D("كُنَّ", "pron-2fp", "«struck you (f. pl.)»", "«sizi (dişil)»"),
  D("نِي", "pron-1s-obj", "«struck me»", "«beni»"), D("نَا", "pron-1p", "«struck us»", "«bizi»", punct="،"),
  tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=":", segments=wa("نَحْوُ", "nahw", "noun")),
  tok("لَهُ", "li", "prep", [K, HJ, BM], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — نَفْسُ الصِّيَغِ مَجْرُورَةً.", "«to him» — the same forms in jarr.", "«ona» — aynı şekiller mecrûr.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("إِلَخْ", "ilakh", "part", [K], "اخْتِصَارُ: إِلَى آخِرِهِ.", "«and so on» — short for «to its end».", "«vb.» — «sonuna kadar»ın kısaltması.", punct="،"),
 ]})
# ----------- s4 — the fourth division: the detached naṣb pronouns
S.append({"id": "s4", "translation": {"en": "and the fourth division is the detached naṣb pronoun, and it is: him, them two, them, her, them two, them (f.), you, you two, you (pl.), you (f.), you two, you (f. pl.), me, us.", "tr": "dördüncü kısım munfasıl mansûb zamirdir; o: iyyâhu, iyyâhümâ, iyyâhüm, iyyâhâ, iyyâhümâ, iyyâhünne, iyyâke, iyyâkümâ, iyyâküm, iyyâki, iyyâkümâ, iyyâkünne, iyyâye, iyyânâ."},
 "tokens": [
  *qism("الرَّابِعُ", "rabi-fourth", "«fourth»", "«dördüncü»"),
  tok("مَنْصُوبٌ", "mansub", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«a naṣb one»", "«mansûb»"),
  tok("مُنْفَصِلٌ", "munfasil", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ.", "«detached»", "«munfasıl»", punct="،"),
  wahuwa(),
  I("هُ", "pron-3ms", "«him»", "«onu»"), I("هُمَا", "pron-3d", "«them two»", "«o ikisini»"), I("هُمْ", "pron-3mp", "«them»", "«onları»"), I("هَا", "pron-3fs", "«her»", "«onu (dişil)»"), I("هُمَا", "pron-3d", "«them two (f.)»", "«o ikisini (dişil)»"), I("هُنَّ", "pron-3fp", "«them (f.)»", "«onları (dişil)»"),
  I("كَ", "pron-2ms", "«you»", "«seni»"), I("كُمَا", "pron-2d", "«you two»", "«siz ikinizi»"), I("كُمْ", "pron-2mp", "«you (pl.)»", "«sizi»"), I("كِ", "pron-2fs", "«you (f.)»", "«seni (dişil)»"), I("كُمَا", "pron-2d", "«you two (f.)»", "«siz ikinizi (dişil)»"), I("كُنَّ", "pron-2fp", "«you (f. pl.)»", "«sizi (dişil)»"),
  I("يَ", "pron-1s", "«me»", "«beni»"), I("نَا", "pron-1p", "«us»", "«bizi»", punct="."),
 ]})
# ----------- s5 — the second kind: the proper name
S.append({"id": "s5", "translation": {"en": "And the second kind is the proper name, and it is two divisions: the name of a person, as «Zayd», and the name of a genus, as «Usāma» and «Subḥān».", "tr": "İkinci nev' alemdir; iki kısımdır: şahıs alemi, «Zeyd» gibi; cins alemi, «Üsâme» ve «Sübhân» gibi."},
 "tokens": [
  tok("وَالنَّوْعُ", "naw", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالنَّوْعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the kind»", "«ve nev'»", segments=wa("النَّوْعُ", "naw", "noun")),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«second»", "«ikinci»"),
  tok("الْعَلَمُ", "alam-name", "noun", [K, MK, TRF], "خَبَرٌ مَرْفُوعٌ.", "«the proper name» — the khabar.", "«alem» — haber.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("قِسْمَانِ", "qism", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two divisions»", "«iki kısım»", punct=":"),
  tok("عَلَمُ", "alam-name", "noun", [K, MK, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ: أَحَدُهُمَا عَلَمُ شَخْصٍ.", "«the name of»", "«alemi»"),
  tok("شَخْصٍ", "shakhs", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a person»", "«şahıs»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: عَلَمُ شَخْصٍ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»", punct="،"),
  tok("وَعَلَمُ", "alam-name", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَعَلَمُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the name of»", "«ve … alemi»", segments=wa("عَلَمُ", "alam-name", "noun")),
  tok("جِنْسٍ", "jins", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a genus»", "«cins»", punct="،"),
  nahw(),
  tok("أُسَامَةَ", "usama", "propn", [K, MNS], "لَفْظٌ مَحْكِيٌّ: عَلَمُ جِنْسٍ لِلْأَسَدِ، مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«Usāma» — the lion's genus-name, a diptote.", "«Üsâme» — aslanın cins alemi, gayr-ı munsarıf."),
  tok("وَسُبْحَانَ", "subhana", "noun", [K, AT, MNS, "maful-mutlaq"], "الْوَاوُ عَاطِفَةٌ، وَسُبْحَانَ لَفْظٌ مَحْكِيٌّ: عَلَمُ جِنْسٍ لِلتَّسْبِيحِ.", "«and Subḥān» — the genus-name of glorifying.", "«ve Sübhân» — tesbîhin cins alemi.", punct=".", segments=wa("سُبْحَانَ", "subhana", "noun")),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "antuma": G("antuma", "أَنْتُمَا", "أ ن ت", "pron", "you two (dual, masculine and feminine)", "siz ikiniz (tesniye)", 2),
 "antunna": G("antunna", "أَنْتُنَّ", "أ ن ت", "pron", "you (feminine plural)", "siz (dişil çoğul)", 2),
 "ilakh": G("ilakh", "إِلَخْ", "أ خ ر", "part", "etc. — the abbreviation of إِلَى آخِرِهِ «to its end»", "vb. — ilâ âhirihî «sonuna kadar»ın kısaltması", 3),
 "alam-name": G("alam-name", "عَلَم", "ع ل م", "noun", "a proper name — of a person (زَيْد) or of a genus (أُسَامَة)", "alem, özel ad — şahıs (Zeyd) veya cins (Üsâme) alemi", 3, plural="أَعْلَام"),
 "usama": G("usama", "أُسَامَة", "أ س م", "propn", "Usāma — the lion's genus-name, also a man's name", "Üsâme — aslanın cins adı; erkek adı da olur", 3),
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
print("izhar ch46 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("daraba", "sabaqa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُضْمَرَاتُ الْأَرْبَعَةُ: الْمَرْفُوعُ الْمُتَّصِلُ وَالْمُنْفَصِلُ، الْمُشْتَرَكُ، الْمَنْصُوبُ الْمُنْفَصِلُ؛ وَالْعَلَمُ: عَلَمُ الشَّخْصِ وَعَلَمُ الْجِنْسِ", "en": "The four pronoun divisions: attached and detached rafʿ, the shared naṣb/jarr, the detached naṣb; and the proper name of person and of genus", "tr": "Dört zamir kısmı: muttasıl ve munfasıl merfû, müşterek mansûb/mecrûr, munfasıl mansûb; şahıs ve cins alemi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المعرفة: المضمرات والعلم", "الكافية لابن الحاجب — المضمر، العلم", "شرح قطر الندى لابن هشام — الضمير والعلم"],
 "amil": "the maʿrifa's first kind is the pronoun, in four divisions: the attached rafʿ (the doer-pronouns of the conjugation), the detached rafʿ (هُوَ هُمَا هُمْ هِيَ هُمَا هُنَّ أَنْتَ أَنْتُمَا أَنْتُمْ أَنْتِ أَنْتُمَا أَنْتُنَّ أَنَا نَحْنُ), the one shared between attached naṣb and attached jarr (ضَرَبَهُ … ضَرَبَنَا and لَهُ … — one set of fourteen forms, naṣb after a verb, jarr after a particle or a muḍāf), and the detached naṣb (إِيَّاهُ … إِيَّانَا); the second kind is the proper name — of a person (زَيْدٌ) or of a genus (أُسَامَةُ for the lion, سُبْحَانَ for glorifying)",
 "question": {
  "en": ["How many divisions have the pronouns? Four — attached rafʿ, detached rafʿ, the shared attached naṣb/jarr, and detached naṣb.",
         "Which are the detached rafʿ pronouns? هُوَ هُمَا هُمْ هِيَ هُمَا هُنَّ (absent), أَنْتَ أَنْتُمَا أَنْتُمْ أَنْتِ أَنْتُمَا أَنْتُنَّ (addressed), أَنَا نَحْنُ (speaking) — mubtadaʾs, khabars, doers after a separation.",
         "Why is the third division «shared»? Because the same fourteen forms serve for the attached naṣb (ضَرَبَهُ … ضَرَبَنَا) and the attached jarr (لَهُ، غُلَامُهُ …): the governor before them, verb or particle, decides the place.",
         "Which are the detached naṣb pronouns? إِيَّاهُ … إِيَّانَا — used where attachment is impossible, as before the verb (إِيَّاكَ نَعْبُدُ) or after إِلَّا.",
         "What is the proper name? The maʿrifa coined for a particular named thing: of a person (زَيْدٌ) or of a genus (أُسَامَةُ the lion, سُبْحَانَ glorifying) — the genus-name is a maʿrifa though its bearer is a kind.",
         "Why are أُسَامَةُ and سُبْحَانَ diptotes? أُسَامَةُ by name-ness and the feminine tāʾ; سُبْحَانَ by name-ness and the added alif-nūn.",
         "What does the engine READ here? The DabtEngine keeps the fourteen detached rafʿ pronouns, the fourteen object forms on ضَرَبَ and the fourteen إِيَّا-forms at the author's form as built words, reads the ordinal before each division as its naʿt and the division's khabar after it, and the cited proper names on their written case."],
  "tr": ["Zamirlerin kaç kısmı vardır? Dört — muttasıl merfû, munfasıl merfû, müşterek muttasıl mansûb/mecrûr ve munfasıl mansûb.",
         "Munfasıl merfû zamirler hangileridir? Hüve hümâ hüm hiye hümâ hünne (gâib), ente entümâ entüm enti entümâ entünne (muhâtab), ene nahnü (mütekellim) — mübtedâ, haber, ayrılmadan sonra fâil olurlar.",
         "Üçüncü kısım neden «müşterek»tir? Çünkü aynı on dört şekil hem muttasıl mansûb (darabehû … darabenâ) hem muttasıl mecrûr (lehû, gulâmuhû …) için kullanılır: öndeki âmil, fiil veya harf, mahalli belirler.",
         "Munfasıl mansûb zamirler hangileridir? İyyâhu … iyyânâ — bitişmenin mümkün olmadığı yerde, fiilden önce (iyyâke na'büdü) veya illâ'dan sonra.",
         "Alem nedir? Belirli adlandırılmış bir şey için konulan ma'rife: şahıs (Zeyd) veya cins (aslan için Üsâme, tesbîh için Sübhân) alemi — cins alemi, sahibi bir tür olsa da ma'rifedir.",
         "Üsâme ve Sübhân neden gayr-ı munsarıftır? Üsâme alemlik ve te'nîs tâ'sı ile; Sübhân alemlik ve zâid elif-nûn ile.",
         "Motor burada neyi OKUR? DabtEngine on dört munfasıl merfû zamiri, darabe üzerindeki on dört nesne şeklini ve on dört iyyâ şeklini mebnî kelimeler olarak yazarın şeklinde tutar; her kısımdan önceki sıra sayısını na't, ardındaki haberi haber okur; alıntılanan alemleri yazılı hâlleriyle okur."],
 },
 "plain": {"en": "Pronouns come in four sets: the subject endings on verbs, the stand-alone subject words («he … we»), the object/possessive endings («him, you, me» after a verb or preposition) and the stand-alone object words («iyyāhu … iyyānā»). The second definite word is the proper name, of a person (Zayd) or a kind (Usāma, «lion»).",
           "tr": "Zamirler dört takımdır: fiillerdeki özne ekleri, bağımsız özne sözcükleri («o … biz»), fiil veya edattan sonraki nesne/iyelik ekleri («onu, onları, seni, beni, bizi») ve bağımsız nesne sözcükleri («iyyâhu … iyyânâ»). Belirli sözcüğün ikinci türü özel addır: ya bir kişinin (Zeyd) ya da bir türün (aslan için Üsâme)."},
 "explanation": {"en": "The first kind of maʿrifa is the pronoun, in four divisions. The first is the attached rafʿ pronoun, treated under the doer. The second is the detached rafʿ pronoun: هُوَ هُمَا هُمْ هِيَ هُمَا هُنَّ أَنْتَ أَنْتُمَا أَنْتُمْ أَنْتِ أَنْتُمَا أَنْتُنَّ أَنَا نَحْنُ. The third is shared between the attached naṣb and the attached jarr — one set of fourteen forms, ضَرَبَهُ ضَرَبَهُمَا ضَرَبَهُمْ ضَرَبَهَا ضَرَبَهُمَا ضَرَبَهُنَّ ضَرَبَكَ ضَرَبَكُمَا ضَرَبَكُمْ ضَرَبَكِ ضَرَبَكُمَا ضَرَبَكُنَّ ضَرَبَنِي ضَرَبَنَا, and the same after a particle or a muḍāf: لَهُ and so on. The fourth is the detached naṣb pronoun: إِيَّاهُ إِيَّاهُمَا إِيَّاهُمْ إِيَّاهَا إِيَّاهُمَا إِيَّاهُنَّ إِيَّاكَ إِيَّاكُمَا إِيَّاكُمْ إِيَّاكِ إِيَّاكُمَا إِيَّاكُنَّ إِيَّايَ إِيَّانَا. The second kind of maʿrifa is the proper name, in two divisions: the name of a person, as زَيْدٌ, and the name of a genus, as أُسَامَةُ for the lion and سُبْحَانَ for glorifying.",
                 "tr": "Ma'rifenin birinci nev'i zamirdir, dört kısımdır. Birincisi fâilde işlenen muttasıl merfû zamir. İkincisi munfasıl merfû zamir: hüve hümâ hüm hiye hümâ hünne ente entümâ entüm enti entümâ entünne ene nahnü. Üçüncüsü muttasıl mansûb ile muttasıl mecrûr arasında müşterek olan — tek bir on dörtlük takım: darabehû darabehümâ darabehüm darabehâ darabehümâ darabehünne darabeke darabekümâ darabeküm darabeki darabekümâ darabekünne darabenî darabenâ; harf veya muzâftan sonra da aynı: lehû vb. Dördüncüsü munfasıl mansûb zamir: iyyâhu iyyâhümâ iyyâhüm iyyâhâ iyyâhümâ iyyâhünne iyyâke iyyâkümâ iyyâküm iyyâki iyyâkümâ iyyâkünne iyyâye iyyânâ. Ma'rifenin ikinci nev'i alemdir, iki kısımdır: şahıs alemi, Zeyd gibi; cins alemi, aslan için Üsâme ve tesbîh için Sübhân gibi."},
 "examples": [
  {"ar": "الْقِسْمُ الْأَوَّلُ مَرْفُوعٌ مُتَّصِلٌ وَقَدْ سَبَقَ", "en": "the attached rafʿ pronoun", "tr": "muttasıl merfû zamir", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "هُوَ هُمَا هُمْ هِيَ هُمَا هُنَّ أَنْتَ أَنْتُمَا أَنْتُمْ أَنْتِ أَنْتُمَا أَنْتُنَّ أَنَا نَحْنُ", "en": "the detached rafʿ pronouns", "tr": "munfasıl merfû zamirler", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "ضَرَبَهُ … ضَرَبَنَا، وَنَحْوُ لَهُ إِلَخْ", "en": "the shared attached naṣb and jarr", "tr": "müşterek muttasıl mansûb ve mecrûr", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "إِيَّاهُ … إِيَّانَا", "en": "the detached naṣb pronouns", "tr": "munfasıl mansûb zamirler", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "عَلَمُ شَخْصٍ نَحْوُ زَيْدٌ، وَعَلَمُ جِنْسٍ نَحْوُ أُسَامَةَ وَسُبْحَانَ", "en": "the proper name of person and of genus", "tr": "şahıs ve cins alemi", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "ضَرَبَ إِيَّاهُ (where attachment is possible)", "right": "ضَرَبَهُ", "why": {"en": "the detached naṣb pronoun is used only where the attached one cannot be", "tr": "munfasıl mansûb zamir ancak muttasılın mümkün olmadığı yerde kullanılır"}},
  {"wrong": "هُوَ read as the object in ضَرَبَ هُوَ", "right": "هُوَ is a rafʿ pronoun — the doer or a mubtadaʾ", "why": {"en": "the detached rafʿ set never stands as an object; naṣb has its own detached set (إِيَّاهُ)", "tr": "munfasıl merfû takım mef'ûl olmaz; nasbın kendi munfasıl takımı vardır (iyyâhu)"}},
  {"wrong": "أُسَامَةٌ (with tanwīn)", "right": "أُسَامَةُ", "why": {"en": "the genus-name is a diptote by name-ness and the feminine tāʾ", "tr": "cins alemi alemlik ve te'nîs tâ'sıyla gayr-ı munsarıftır"}},
 ],
}
TMZ = "tamyiz"
ADD_EN = (" Chapter 46 (print p. 142): the pronouns' four divisions — the attached rafʿ (s1), the detached rafʿ (s2), the shared attached naṣb/jarr (s3), the detached naṣb (s4) — and the proper name of person and of genus (s5).")
ADD_TR = (" Kırk altıncı bab (baskı s. 142): zamirlerin dört kısmı — muttasıl merfû (s1), munfasıl merfû (s2), müşterek muttasıl mansûb/mecrûr (s3), munfasıl mansûb (s4) — ve şahıs ve cins alemi (s5).")
write_out(46, S, TITLE, ADD_EN, ADD_TR, "p. 142", GLOSS_ADD, notes=(NOTE,),
          related=((K45, [K]), (TRF, [K]), (BM, [K]), (DF, [K]), (MMB, [K]), (MNS, [K])))
report(46, S, GLOSS_ADD, (NOTE,))
