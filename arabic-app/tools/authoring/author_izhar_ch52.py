# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 52: the THIRD bāb, the iʿrāb — a thing that comes from the governor, by which the end of the muʿrab differs; four
# interlocking divisions. The FIRST, by essence: a vowel, a letter, or a dropping — the vowels three (ḍamma, fatḥa, kasra: جَاءَنِي زَيْدٌ، رَأَيْتُ زَيْدًا، مَرَرْتُ بِزَيْدٍ),
# the letters four (wāw, alif, yāʾ: أَبُوهُ، أَبَاهُ، بِأَبِيهِ; and nūn: يَضْرِبَانِ), the droppings three (of the vowel لَمْ يَضْرِبْ, of the last letter لَمْ يَغْزُ, of the nūn
# لَمْ يَضْرِبَا) — ten in all. The SECOND, by locus: pure vowels, pure letters, vowels with dropping, or letters with dropping; the first either complete
# by the three vowels (the singular noun and the broken plural when declinable: رَجُلٌ وَرِجَالٌ …). Print pp. 147–148.
# Orthography: the lithograph prints ثلثة / الثلث (old spelling without alif); the text gives ثَلَاثَةٌ / الثَّلَاثِ. The Ottoman commentary
# (izhar-full-corrected l. 1649 ff.) is followed for the readings.
#   python3 author_izhar_ch52.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; FN = "five-nouns"; JDS = "jam-mudhakkar-salim"; LJ = "lam-jazim"; NQV = "naqis-verbs"; TQ = "taqsim"; F6 = "form-vi-verbs"
K = "al-irab-wa-taqsimuhu-bil-dhat-wal-mahall"
K51 = "al-badal-wa-aqsamuh-wa-atf-al-bayan"
TITLE = {"ar": "الْبَابُ الثَّالِثُ فِي الْإِعْرَابِ: تَعْرِيفُهُ، وَتَقْسِيمُهُ بِحَسَبِ الذَّاتِ إِلَى عَشَرَةٍ، وَبِحَسَبِ الْمَحَلِّ", "en": "The third bāb, the iʿrāb: its definition, its division by essence into ten, and by locus", "tr": "Üçüncü bab, i'râb: tarifi, zâta göre ona ve mahalle göre taksimi"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wnahw(): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=":", segments=wa("نَحْوُ", "nahw", "noun"))
def jaani(): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")])
def waraaytu(): return tok("وَرَأَيْتُ", "raa", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَرَأَيْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I saw»", "«ve gördüm»", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron")])
def wamarartu(): return tok("وَمَرَرْتُ", "marra", "verb", [K, AT, FL, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمَرَرْتُ فِعْلٌ مَاضٍ مُضَاعَفٌ، وَالتَّاءُ فَاعِلٌ.", "«and I passed»", "«ve uğradım»", segments=[seg("وَ", "wa", "conj"), seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")])
def lam(): return tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«did not»", "«-medi»")
def wlam(): return tok("وَلَمْ", "lam", "part", [K, AT, LJ, JZ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … did not»", "«ve … -medi»", segments=wa("لَمْ", "lam", "part"))
def hadhfu(form, en, tr, first=False):
    ar = "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ: أَحَدُهَا حَذْفُ." if first else "الْوَاوُ عَاطِفَةٌ، وَحَذْفُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ."
    return tok(form, "hadhf", "noun", [K, MK, ID, MSD, IRB] + ([] if first else [AT]), ar, en, tr, segments=None if first else wa("حَذْفُ", "hadhf", "noun"))

# ----------- s1 — the third bāb: the definition of iʿrāb; four interlocking divisions
S.append({"id": "s1", "translation": {"en": "The third bāb, on the iʿrāb. And it is a thing that comes from the governor, by which the end of the muʿrab differs; and it has four interlocking divisions.", "tr": "Üçüncü bab, i'râb hakkındadır. O, âmilden gelen ve kendisiyle mu'rebin sonu değişen bir şeydir; birbirine giren dört taksimi vardır."},
 "tokens": [
  tok("الْبَابُ", "bab", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the bāb»", "«bab»"),
  tok("الثَّالِثُ", "thalith", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«third»", "«üçüncü»"),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«on» — the phrase is the khabar.", "«hakkında» — öbek haber."),
  tok("الْإِعْرَابِ", "irab", "noun", [K, HJ, MSD, F4, IRB], "مَجْرُورٌ بِفِي.", "«the iʿrāb»", "«i'râb»", punct="."),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("شَيْءٌ", "shay", "noun", [K, MK, IRB], "خَبَرٌ مَرْفُوعٌ — الْجِنْسُ فِي التَّعْرِيفِ.", "«a thing» — the genus of the definition.", "«bir şey» — tarifin cinsi."),
  tok("جَاءَ", "jaa", "verb", [K, NA, HV, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ نَعْتٌ لِشَيْءٍ.", "«that comes» — the clause describes «thing».", "«gelen» — cümle şey'in sıfatı."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْعَامِلِ", "amil", "noun", [K, HJ, IFA, AQ], "مَجْرُورٌ بِمِنْ.", "«the governor»", "«âmilden»"),
  tok("يَخْتَلِفُ", "ikhtalafa", "verb", [K, NA, MR, F8], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِشَيْءٍ.", "«differs» — a second describing clause.", "«değişir» — ikinci sıfat cümlesi."),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — رَاجِعٌ إِلَى شَيْءٍ.", "«by it» — back to «thing».", "«onunla» — şey'e döner.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("آخِرُ", "akhir", "noun", [K, FL, ID], "فَاعِلُ يَخْتَلِفُ مَرْفُوعٌ، مُضَافٌ.", "«the end of» — the doer of «differs».", "«sonu» — yahtelifü'nün fâili."),
  tok("الْمُعْرَبِ", "murab", "noun", [K, ID, IMF, F4, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muʿrab»", "«mu'rebin»", punct="،"),
  tok("وَلَهُ", "lahu", "prep", [K, AT, MK, HJ], "الْوَاوُ عَاطِفَةٌ، وَلَهُ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and it has» — the khabar, put first.", "«ve onun … vardır» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "li", "prep"), pr3ms()]),
  tok("تَقْسِيمَاتٌ", "taqsim", "noun", [K, MK, MSD, F2, "jam-muannath-salim", TQ], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«divisions» — the mubtadaʾ, put after.", "«taksimler» — sona bırakılmış mübteda."),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«four»", "«dört»"),
  tok("مُتَدَاخِلَةٌ", "mutadakhil", "noun", [K, NA, IFA, F6], "نَعْتٌ ثَانٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ تَدَاخَلَ: يَدْخُلُ بَعْضُهَا فِي بَعْضٍ.", "«interlocking» — one entering the other.", "«birbirine giren» — biri ötekine girer.", punct="."),
 ]})
# ----------- s2 — the first division, by essence
S.append({"id": "s2", "translation": {"en": "The first division is according to the essence and the reality; so we say: it is either a vowel, or a letter, or a dropping.", "tr": "Birinci taksim zâta ve hakikate göredir; deriz ki: o ya bir hareke, ya bir harf, ya da bir hazftir."},
 "tokens": [
  tok("التَّقْسِيمُ", "taqsim", "noun", [K, MK, MSD, F2, TQ], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the division»", "«taksim»"),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«first»", "«birinci»"),
  tok("بِحَسَبِ", "hasab", "noun", [K, HJ, ID, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَحَسَبِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«according to» — the khabar.", "«-e göre» — haber.", segments=[seg("بِ", "bi", "prep"), seg("حَسَبِ", "hasab", "noun")]),
  tok("الذَّاتِ", "dhat", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the essence»", "«zât»"),
  tok("وَالْحَقِيقَةِ", "haqiqa", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَالْحَقِيقَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the reality»", "«ve hakikat»", punct="،", segments=wa("الْحَقِيقَةِ", "haqiqa", "noun")),
  tok("فَنَقُولُ", "qala", "verb", [K, AT, MR, HV], "الْفَاءُ لِلتَّفْرِيعِ، وَنَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«so we say»", "«deriz ki»", punct=":", segments=fa("نَقُولُ", "qala", "verb")),
  tok("هُوَ", "huwa", "pron", [K, MK], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَقُولُ الْقَوْلِ.", "«it is» — what is said.", "«o» — makûl-i kavl."),
  tok("إِمَّا", "imma", "part", [K, AT, TQ], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("حَرَكَةٌ", "haraka", "noun", [K, MK, IRB], "خَبَرٌ مَرْفُوعٌ.", "«a vowel»", "«hareke»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya»"),
  tok("حَرْفٌ", "harf", "noun", [K, AT, IRB], "مَعْطُوفٌ مَرْفُوعٌ.", "«a letter»", "«harf»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("حَذْفٌ", "hadhf", "noun", [K, AT, MSD, IRB], "مَعْطُوفٌ مَرْفُوعٌ.", "«a dropping»", "«hazf»", punct="،"),
 ]})
# ----------- s3 — the vowels three
S.append({"id": "s3", "translation": {"en": "And the vowels are three: ḍamma, fatḥa and kasra — as in «there came to me Zayd», «and I saw Zayd», «and I passed by Zayd»;", "tr": "Hareke üçtür: damme, fetha ve kesre — «bana Zeyd geldi», «Zeyd'i gördüm», «Zeyd'e uğradım» gibi;"},
 "tokens": [
  tok("وَالْحَرَكَةُ", "haraka", "noun", [K, AT, MK, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْحَرَكَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the vowel»", "«hareke»", segments=wa("الْحَرَكَةُ", "haraka", "noun")),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ — الطَّبْعُ: ثلثة.", "«three» — the print spells it ثلثة.", "«üçtür» — baskıda ثلثة.", punct=":"),
  tok("ضَمَّةٌ", "damma", "noun", [K, MK, HT, IRB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا ضَمَّةٌ — أَوْ بَدَلٌ مِنْ ثَلَاثَةٍ.", "«ḍamma»", "«damme»"),
  tok("وَفَتْحَةٌ", "fatha", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَفَتْحَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and fatḥa»", "«ve fetha»", segments=wa("فَتْحَةٌ", "fatha", "noun")),
  tok("وَكَسْرَةٌ", "kasra", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَكَسْرَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and kasra»", "«ve kesre»", punct="،", segments=wa("كَسْرَةٌ", "kasra", "noun")),
  nahw(),
  jaani(),
  tok("زَيْدٌ", "zayd", "propn", [K, FL, IRB], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — rafʿ by ḍamma.", "«Zeyd» — damme ile merfû.", punct="،"),
  waraaytu(),
  tok("زَيْدًا", "zayd", "propn", [K, MB, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — naṣb by fatḥa.", "«Zeyd'i» — fetha ile mansûb.", punct="،"),
  wamarartu(),
  tok("بِزَيْدٍ", "zayd", "propn", [K, HJ, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«by Zayd» — jarr by kasra.", "«Zeyd'e» — kesre ile mecrûr.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
 ]})
# ----------- s4 — the letters four
S.append({"id": "s4", "translation": {"en": "and the letters are four: wāw, alif and yāʾ — as in «there came to me his father», «and I saw his father», «and I passed by his father»; and nūn — as in «the two strike»;", "tr": "harf dörttür: vâv, elif ve yâ — «bana babası geldi», «babasını gördüm», «babasına uğradım» gibi; ve nûn — «ikisi döver» gibi;"},
 "tokens": [
  tok("وَالْحَرْفُ", "harf", "noun", [K, AT, MK, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْحَرْفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the letter»", "«harf»", segments=wa("الْحَرْفُ", "harf", "noun")),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«four»", "«dörttür»", punct=":"),
  tok("وَاوٌ", "waw-letter", "noun", [K, MK, HT, IRB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا وَاوٌ.", "«wāw»", "«vâv»"),
  tok("وَأَلِفٌ", "alif-letter", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَأَلِفٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and alif»", "«ve elif»", segments=wa("أَلِفٌ", "alif-letter", "noun")),
  tok("وَيَاءٌ", "ya-letter", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَيَاءٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and yāʾ»", "«ve yâ»", punct="،", segments=wa("يَاءٌ", "ya-letter", "noun")),
  nahw(),
  jaani(),
  tok("أَبُوهُ", "ab", "noun", [K, FL, FN, ID, IRB], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ السِّتَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — rafʿ by the wāw.", "«babası» — vâv ile merfû.", punct="،", segments=[seg("أَبُو", "ab", "noun"), pr3ms()]),
  waraaytu(),
  tok("أَبَاهُ", "ab", "noun", [K, MB, FN, ID, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — naṣb by the alif.", "«babasını» — elif ile mansûb.", punct="،", segments=[seg("أَبَا", "ab", "noun"), pr3ms()]),
  wamarartu(),
  tok("بِأَبِيهِ", "ab", "noun", [K, HJ, FN, ID, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَأَبِي مَجْرُورٌ بِالْيَاءِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«by his father» — jarr by the yāʾ.", "«babasına» — yâ ile mecrûr.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("أَبِي", "ab", "noun"), pr3msi()]),
  tok("وَنُونٌ", "nun-letter", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَنُونٌ مَعْطُوفٌ عَلَى وَاوٍ مَرْفُوعٌ.", "«and nūn»", "«ve nûn»", punct="،", segments=wa("نُونٌ", "nun-letter", "noun")),
  nahw(),
  tok("يَضْرِبَانِ", "daraba", "verb", [K, MR, MTH, FL, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«the two strike» — rafʿ by the nūn's presence.", "«ikisi döver» — nûnun sübûtu ile merfû.", punct="،", segments=[seg("يَضْرِبَ", "daraba", "verb"), seg("ا", "pron-3d", "pron"), seg("نِ", "nun-letter", "part")]),
 ]})
# ----------- s5 — the droppings three; ten in all
S.append({"id": "s5", "translation": {"en": "and the droppings are three: the dropping of the vowel — as in «he did not strike»; and the dropping of the last letter — as in «he did not raid»; and the dropping of the nūn — as in «the two did not strike»; so the total is ten.", "tr": "hazf üçtür: harekenin hazfi — «dövmedi» gibi; sonun hazfi — «gazâ etmedi» gibi; nûnun hazfi — «ikisi dövmedi» gibi; böylece toplam ondur."},
 "tokens": [
  tok("وَالْحَذْفُ", "hadhf", "noun", [K, AT, MK, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْحَذْفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the dropping»", "«hazf»", segments=wa("الْحَذْفُ", "hadhf", "noun")),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«three»", "«üçtür»", punct=":"),
  hadhfu("حَذْفُ", "«the dropping of»", "«hazfi»", first=True),
  tok("الْحَرَكَةِ", "haraka", "noun", [K, ID, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the vowel»", "«harekenin»"),
  nahw(),
  lam(),
  tok("يَضْرِبْ", "daraba", "verb", [K, LJ, JZ, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ الْحَرَكَةِ (السُّكُونِ).", "«strike» — jazm by dropping the vowel.", "«dövmedi» — hareke hazfi ile meczûm.", punct="،"),
  hadhfu("وَحَذْفُ", "«and the dropping of»", "«ve hazfi»"),
  tok("الْآخِرِ", "akhir", "noun", [K, ID, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حَرْفِ الْعِلَّةِ.", "«the last letter» — the weak letter.", "«sonun» — illet harfinin."),
  nahw(),
  lam(),
  tok("يَغْزُ", "ghaza", "verb", [K, LJ, JZ, NQV, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِحَذْفِ الْوَاوِ — أَصْلُهُ يَغْزُو.", "«raid» — jazm by dropping the wāw of yaghzū.", "«gazâ etmedi» — yağzû'nun vâvı hazfedilerek meczûm.", punct="،"),
  hadhfu("وَحَذْفُ", "«and the dropping of»", "«ve hazfi»"),
  tok("النُّونِ", "nun-letter", "noun", [K, ID, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the nūn»", "«nûnun»"),
  nahw(),
  lam(),
  tok("يَضْرِبَا", "daraba", "verb", [K, LJ, JZ, MTH, FL, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«the two strike» — jazm by dropping the nūn.", "«ikisi dövmedi» — nûn hazfi ile meczûm.", punct="،", segments=[seg("يَضْرِبَ", "daraba", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("فَالْمَجْمُوعُ", "majmu", "noun", [K, AT, MK, IMF], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمَجْمُوعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the total»", "«böylece toplam»", segments=fa("الْمَجْمُوعُ", "majmu", "noun")),
  tok("عَشَرَةٌ", "ashara", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ — ثَلَاثُ حَرَكَاتٍ وَأَرْبَعَةُ أَحْرُفٍ وَثَلَاثَةُ أَنْوَاعٍ مِنَ الْحَذْفِ.", "«ten» — three vowels, four letters, three droppings.", "«ondur» — üç hareke, dört harf, üç hazf.", punct="."),
 ]})
# ----------- s6 — the second division, by locus
S.append({"id": "s6", "translation": {"en": "And the second division is according to the locus: it is either by pure vowels, or by pure letters, or by vowels together with dropping, or by letters together with dropping.", "tr": "İkinci taksim mahalle göredir: o ya sırf harekelerle, ya sırf harflerle, ya hazf ile birlikte harekelerle, ya da hazf ile birlikte harflerledir."},
 "tokens": [
  tok("وَالتَّقْسِيمُ", "taqsim", "noun", [K, AT, MK, TQ], "الْوَاوُ عَاطِفَةٌ، وَالتَّقْسِيمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division»", "«taksim»", segments=wa("التَّقْسِيمُ", "taqsim", "noun")),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«second»", "«ikinci»"),
  tok("بِحَسَبِ", "hasab", "noun", [K, HJ, ID, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَحَسَبِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«according to»", "«-e göre»", segments=[seg("بِ", "bi", "prep"), seg("حَسَبِ", "hasab", "noun")]),
  tok("الْمَحَلِّ", "mahall", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَحَلِّ الْإِعْرَابِ مِنَ الْكَلِمَةِ.", "«the locus» — where in the word the iʿrāb sits.", "«mahal» — i'râbın kelimedeki yeri.", punct="،"),
  tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«so it is»", "«o»", segments=fa("هُوَ", "huwa", "pron")),
  tok("إِمَّا", "imma", "part", [K, AT, TQ], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("بِالْحَرَكَاتِ", "haraka", "noun", [K, HJ, MK, "jam-muannath-salim", IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرَكَاتِ مَجْرُورٌ — خَبَرٌ.", "«by the vowels» — the khabar.", "«harekelerle» — haber.", segments=[seg("بِ", "bi", "prep"), seg("الْحَرَكَاتِ", "haraka", "noun")]),
  tok("الْمَحْضَةِ", "mahd", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«pure»", "«sırf»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya»"),
  tok("بِالْحُرُوفِ", "harf", "noun", [K, HJ, AT, JT, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحُرُوفِ مَجْرُورٌ — مَعْطُوفٌ.", "«by the letters»", "«harflerle»", segments=[seg("بِ", "bi", "prep"), seg("الْحُرُوفِ", "harf", "noun")]),
  tok("الْمَحْضَةِ", "mahd", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«pure»", "«sırf»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya»"),
  tok("بِالْحَرَكَاتِ", "haraka", "noun", [K, HJ, AT, "jam-muannath-salim", IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرَكَاتِ مَجْرُورٌ — مَعْطُوفٌ.", "«by the vowels»", "«harekelerle»", segments=[seg("بِ", "bi", "prep"), seg("الْحَرَكَاتِ", "haraka", "noun")]),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«together with»", "«ile birlikte»"),
  tok("الْحَذْفِ", "hadhf", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«dropping»", "«hazf»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("بِالْحُرُوفِ", "harf", "noun", [K, HJ, AT, JT, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحُرُوفِ مَجْرُورٌ — مَعْطُوفٌ.", "«by the letters»", "«harflerle»", segments=[seg("بِ", "bi", "prep"), seg("الْحُرُوفِ", "harf", "noun")]),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«together with»", "«ile birlikte»"),
  tok("الْحَذْفِ", "hadhf", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«dropping»", "«hazf»", punct="،"),
 ]})
# ----------- s7 — the first locus, complete by the three vowels
S.append({"id": "s7", "translation": {"en": "And the first is either complete in iʿrāb by the three vowels — by ḍamma in rafʿ, fatḥa in naṣb and kasra in jarr — and that is the singular noun and the broken plural, both declinable, as in «there came to me a man and men», «and I saw a man and men», «and I passed by a man and men»;", "tr": "Birincisi ya üç hareke ile i'râbı tam olandır — ref'te damme, nasbda fetha, cerde kesre ile — o da munsarif olan müfred isim ve cem'-i mükesserdir: «bana bir adam ve adamlar geldi», «bir adam ve adamlar gördüm», «bir adama ve adamlara uğradım» gibi;"},
 "tokens": [
  tok("وَالْأَوَّلُ", "awwal", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ — الْمُعْرَبُ بِالْحَرَكَاتِ الْمَحْضَةِ.", "«and the first» — the one declined by pure vowels.", "«birincisi» — sırf harekelerle mu'reb olan.", segments=wa("الْأَوَّلُ", "awwal", "noun")),
  tok("إِمَّا", "imma", "part", [K, AT, TQ], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("تَامُّ", "tamm", "noun", [K, MK, ID, "doubled-verbs"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«complete in»", "«tam»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbı»"),
  tok("بِالْحَرَكَاتِ", "haraka", "noun", [K, HJ, "jam-muannath-salim", IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرَكَاتِ مَجْرُورٌ.", "«by the vowels»", "«harekelerle»", segments=[seg("بِ", "bi", "prep"), seg("الْحَرَكَاتِ", "haraka", "noun")]),
  tok("الثَّلَاثِ", "thalatha", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ — الطَّبْعُ: الثلث.", "«three» — the print spells it الثلث.", "«üç» — baskıda الثلث.", punct=":"),
  tok("بِالضَّمَّةِ", "damma", "noun", [K, HJ, HT, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالضَّمَّةِ مَجْرُورٌ — بَدَلٌ مِنْ بِالْحَرَكَاتِ.", "«by ḍamma» — spelling out «by the vowels».", "«damme ile» — harekelerin açılımı.", segments=[seg("بِ", "bi", "prep"), seg("الضَّمَّةِ", "damma", "noun")]),
  tok("رَفْعًا", "raf", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ — أَيْ حَالَ الرَّفْعِ، أَوْ مَفْعُولٌ لَهُ.", "«in rafʿ» — a ḥāl: in the state of rafʿ.", "«ref'te» — hâl: ref' hâlinde."),
  tok("وَالْفَتْحَةِ", "fatha", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْفَتْحَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and fatḥa»", "«ve fetha»", segments=wa("الْفَتْحَةِ", "fatha", "noun")),
  tok("نَصْبًا", "nasb", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ.", "«in naṣb»", "«nasbda»"),
  tok("وَالْكَسْرَةِ", "kasra", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْكَسْرَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and kasra»", "«ve kesre»", segments=wa("الْكَسْرَةِ", "kasra", "noun")),
  tok("جَرًّا", "jarr", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ.", "«in jarr»", "«cerde»", punct="،"),
  tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=fa("هُوَ", "huwa", "pron")),
  tok("الِاسْمُ", "ism", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the noun»", "«isim»"),
  tok("الْمُفْرَدُ", "mufrad", "noun", [K, NA, IMF, F4], "نَعْتٌ مَرْفُوعٌ.", "«singular»", "«müfred»"),
  tok("وَالْجَمْعُ", "jam", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْجَمْعُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the plural»", "«ve cem'»", segments=wa("الْجَمْعُ", "jam", "noun")),
  tok("الْمُكَسَّرُ", "mukassar", "noun", [K, NA, IMF, F2, JT], "نَعْتٌ مَرْفُوعٌ.", "«broken»", "«mükesser»"),
  tok("الْمُنْصَرِفَانِ", "munsarif", "noun", [K, NA, IFA, MTH, MMS], "نَعْتٌ لِلِاسْمِ وَالْجَمْعِ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى لِأَنَّ الْمَنْعُوتَ اثْنَانِ.", "«both declinable» — dual, describing the two.", "«munsarif olan ikisi» — iki mevsûfa tesniye.", punct="،"),
  nahw(),
  jaani(),
  tok("رَجُلٌ", "rajul", "noun", [K, FL, IRB], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — الْمُفْرَدُ.", "«a man» — the singular.", "«bir adam» — müfred."),
  tok("وَرِجَالٌ", "rajul", "noun", [K, AT, JT, IRB], "الْوَاوُ عَاطِفَةٌ، وَرِجَالٌ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ — الْجَمْعُ الْمُكَسَّرُ.", "«and men» — the broken plural.", "«ve adamlar» — cem'-i mükesser.", punct="،", segments=wa("رِجَالٌ", "rajul", "noun")),
  waraaytu(),
  tok("رَجُلًا", "rajul", "noun", [K, MB, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a man»", "«bir adam»"),
  tok("وَرِجَالًا", "rajul", "noun", [K, AT, JT, IRB], "الْوَاوُ عَاطِفَةٌ، وَرِجَالًا مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and men»", "«ve adamlar»", punct="،", segments=wa("رِجَالًا", "rajul", "noun")),
  wamarartu(),
  tok("بِرَجُلٍ", "rajul", "noun", [K, HJ, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَرَجُلٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«by a man»", "«bir adama»", segments=[seg("بِ", "bi", "prep"), seg("رَجُلٍ", "rajul", "noun")]),
  tok("وَرِجَالٍ", "rajul", "noun", [K, AT, JT, IRB], "الْوَاوُ عَاطِفَةٌ، وَرِجَالٍ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and men»", "«ve adamlara»", punct="،", segments=wa("رِجَالٍ", "rajul", "noun")),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "mutadakhil": G("mutadakhil", "مُتَدَاخِل", "د خ ل", "noun", "interlocking, one entering into another (active participle of form VI)", "birbirine giren, mütedâhil (VI. babın ism-i fâili)", 4),
 "ghaza": G("ghaza", "غَزَا", "غ ز و", "verb", "to raid, to go on a campaign — a defective wāw-verb (yaghzū)", "gazâ etmek, sefere çıkmak — nâkıs vâvî fiil (yağzû)", 3),
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
put_morph(mo, "ghaza", {"bab": "الْبَابُ الْأَوَّلُ فَعَلَ يَفْعُلُ — نَاقِصٌ وَاوِيٌّ", "wazn": "فَعَلَ يَفْعُلُ", "masdar": "غَزْو", "ismFail": "غَازٍ",
 "mazi": ["غَزَا", "غَزَوَا", "غَزَوْا", "غَزَتْ", "غَزَتَا", "غَزَوْنَ", "غَزَوْتَ", "غَزَوْتُمَا", "غَزَوْتُمْ", "غَزَوْتِ", "غَزَوْتُمَا", "غَزَوْتُنَّ", "غَزَوْتُ", "غَزَوْنَا"],
 "mudari": ["يَغْزُو", "يَغْزُوَانِ", "يَغْزُونَ", "تَغْزُو", "تَغْزُوَانِ", "يَغْزُونَ", "تَغْزُو", "تَغْزُوَانِ", "تَغْزُونَ", "تَغْزِينَ", "تَغْزُوَانِ", "تَغْزُونَ", "أَغْزُو", "نَغْزُو"],
 "amr": ["اُغْزُ", "اُغْزُوَا", "اُغْزُوا", "اُغْزِي", "اُغْزُوَا", "اُغْزُونَ"], "mansub": "يَغْزُوَ", "majzum": "يَغْزُ", "majzum2": "تَغْزُ",
 "note": "غَزَا يَغْزُو غَزْوًا: نَاقِصٌ وَاوِيٌّ مِنَ الْبَابِ الْأَوَّلِ — رَفْعُهُ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَنَصْبُهُ بِالْفَتْحَةِ الظَّاهِرَةِ، وَجَزْمُهُ بِحَذْفِ الْآخِرِ: لَمْ يَغْزُ — مِثَالُ الْمَتْنِ لِحَذْفِ الْآخِرِ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch52 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("ikhtalafa", "marra", "qala", "jaa", "raa", "daraba", "ghaza") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْإِعْرَابُ: تَعْرِيفُهُ، وَأَقْسَامُهُ بِحَسَبِ الذَّاتِ: حَرَكَةٌ وَحَرْفٌ وَحَذْفٌ — عَشَرَةٌ، وَبِحَسَبِ الْمَحَلِّ", "en": "The iʿrāb: its definition; its kinds by essence — vowel, letter, dropping: ten; and by locus", "tr": "İ'râb: tarifi; zâta göre kısımları — hareke, harf, hazf: on; ve mahalle göre"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الباب الثالث: الإعراب", "الكافية لابن الحاجب — الإعراب", "شرح قطر الندى لابن هشام — علامات الإعراب"],
 "amil": "the iʿrāb is a thing that comes from the governor by which the end of the muʿrab differs; four interlocking divisions. By essence: a vowel (ḍamma, fatḥa, kasra — زَيْدٌ، زَيْدًا، بِزَيْدٍ), a letter (wāw, alif, yāʾ — أَبُوهُ، أَبَاهُ، بِأَبِيهِ; nūn — يَضْرِبَانِ), or a dropping (of the vowel لَمْ يَضْرِبْ, of the last letter لَمْ يَغْزُ, of the nūn لَمْ يَضْرِبَا): ten. By locus: pure vowels, pure letters, vowels with dropping, letters with dropping; the first is complete by the three vowels in the declinable singular and broken plural (رَجُلٌ وَرِجَالٌ).",
 "question": {
  "en": ["What is the iʿrāb? A thing that comes from the governor and by which the end of the muʿrab differs — the ḍamma of زَيْدٌ after جَاءَ, the fatḥa of زَيْدًا after رَأَيْتُ, the kasra of بِزَيْدٍ after the bāʾ.",
         "Why are the four divisions called interlocking? Because one and the same sign falls under several of them — the ḍamma is a vowel by essence, a pure vowel by locus, a rafʿ by kind.",
         "What is the iʿrāb by essence? A vowel, a letter, or a dropping: three vowels, four letters (wāw, alif, yāʾ, nūn), three droppings — ten in all.",
         "Which letters carry the iʿrāb, and where? Wāw, alif and yāʾ in the six nouns (أَبُوهُ، أَبَاهُ، بِأَبِيهِ) and nūn in the dual and plural muḍāriʿ (يَضْرِبَانِ).",
         "What are the three droppings? Of the vowel in the sound muḍāriʿ (لَمْ يَضْرِبْ), of the last weak letter (لَمْ يَغْزُ from يَغْزُو), of the nūn after the dual and plural pronouns (لَمْ يَضْرِبَا).",
         "What is the division by locus? Pure vowels, pure letters, vowels together with dropping, letters together with dropping — four loci.",
         "Which words are complete in iʿrāb by the three vowels? The declinable singular noun and broken plural: رَجُلٌ، رَجُلًا، بِرَجُلٍ and رِجَالٌ، رِجَالًا، بِرِجَالٍ.",
         "What does the engine READ here? The DabtEngine reads the three Zayds by the three vowels, أَبُوهُ/أَبَاهُ/بِأَبِيهِ by the three letters, يَضْرِبَانِ with its nūn, the jazm of لَمْ يَضْرِبْ by sukūn, of لَمْ يَغْزُ by the dropped wāw, of لَمْ يَضْرِبَا by the dropped nūn, and رِجَالٌ as a broken plural carrying full iʿrāb."],
  "tr": ["İ'râb nedir? Âmilden gelen ve kendisiyle mu'rebin sonu değişen şey — câe'den sonra Zeydün'ün dammesi, raeytü'den sonra Zeyden'in fethası, bâ'dan sonra bi-Zeydin'in kesresi.",
         "Dört taksime neden «mütedâhil» denir? Çünkü aynı alâmet birkaçına girer — damme zâtça hareke, mahalce sırf hareke, nev'ce ref'tir.",
         "Zâta göre i'râb nedir? Hareke, harf ya da hazf: üç hareke, dört harf (vâv, elif, yâ, nûn), üç hazf — toplam on.",
         "Hangi harfler i'râbı taşır, nerede? Altı isimde vâv, elif ve yâ (ebûhü, ebâhü, bi-ebîhi); tesniye ve cemi muzâride nûn (yadribâni).",
         "Üç hazf nedir? Sahih muzâride harekenin (lem yadrib), son illet harfinin (yağzû'dan lem yağzü), tesniye ve cemi zamirlerinden sonra nûnun (lem yadribâ) hazfi.",
         "Mahalle göre taksim nedir? Sırf hareke, sırf harf, hazf ile hareke, hazf ile harf — dört mahal.",
         "Üç hareke ile i'râbı tam olan kelimeler hangileridir? Munsarif müfred isim ve cem'-i mükesser: racülün, racülen, bi-racülin ve ricâlün, ricâlen, bi-ricâlin.",
         "Motor burada neyi OKUR? DabtEngine üç Zeyd'i üç hareke ile, ebûhü/ebâhü/bi-ebîhi'yi üç harf ile, yadribâni'yi nûnuyla, lem yadrib'in cezmini sükûnla, lem yağzü'nünkini düşen vâvla, lem yadribâ'nınkini düşen nûnla ve ricâlün'ü tam i'râblı cem'-i mükesser olarak okur."],
 },
 "plain": {"en": "Iʿrāb is the change at a word's end caused by the word governing it. It shows up as a vowel (u, a, i: «Zayd-un, Zayd-an, bi-Zayd-in»), a letter (wāw, alif, yāʾ in «his father»; nūn in «the two strike»), or a dropping (no vowel, a lost weak letter, a lost nūn). Ten signs. Plain nouns and broken plurals use the vowels.",
           "tr": "İ'râb, kelimeyi yöneten sözün o kelimenin sonunda yaptığı değişikliktir. Hareke (u, a, i: «Zeyd-ün, Zeyd-en, bi-Zeyd-in»), harf (ebûhü'de vâv, elif, yâ; yadribâni'de nûn) ya da düşme (hareke yok, illet harfi düşer, nûn düşer) olarak görünür. Toplam on alâmet. Sıradan isimler ve kırık çoğullar üç harekeyi kullanır."},
 "explanation": {"en": "The third bāb treats the iʿrāb: a thing that comes from the governor, by which the end of the muʿrab differs — the genus «thing» embracing vowel, letter and dropping alike. It has four interlocking divisions. The first, by essence and reality: the iʿrāb is a vowel, a letter, or a dropping. The vowels are three — ḍamma, fatḥa, kasra: جَاءَنِي زَيْدٌ، رَأَيْتُ زَيْدًا، مَرَرْتُ بِزَيْدٍ. The letters are four — wāw, alif and yāʾ: جَاءَنِي أَبُوهُ، رَأَيْتُ أَبَاهُ، مَرَرْتُ بِأَبِيهِ; and nūn: يَضْرِبَانِ. The droppings are three — of the vowel: لَمْ يَضْرِبْ; of the last letter: لَمْ يَغْزُ; of the nūn: لَمْ يَضْرِبَا. The total is ten. The second division, by locus: the iʿrāb is by pure vowels, by pure letters, by vowels together with dropping, or by letters together with dropping. The first of these is either complete, by the three vowels — ḍamma in rafʿ, fatḥa in naṣb, kasra in jarr — and that is the singular noun and the broken plural when both are declinable: جَاءَنِي رَجُلٌ وَرِجَالٌ، رَأَيْتُ رَجُلًا وَرِجَالًا، مَرَرْتُ بِرَجُلٍ وَرِجَالٍ. The deficient kinds follow in the next chapter. The lithograph spells the numerals ثلثة and الثلث in the old orthography.",
                 "tr": "Üçüncü bab i'râbı ele alır: âmilden gelen ve kendisiyle mu'rebin sonu değişen şey — «şey» cinsi hareke, harf ve hazfi birlikte kuşatır. Birbirine giren dört taksimi vardır. Birincisi zâta ve hakikate göre: i'râb hareke, harf ya da hazftir. Hareke üçtür — damme, fetha, kesre: câenî Zeydün, raeytü Zeyden, merartü bi-Zeydin. Harf dörttür — vâv, elif ve yâ: câenî ebûhü, raeytü ebâhü, merartü bi-ebîhi; ve nûn: yadribâni. Hazf üçtür — harekenin: lem yadrib; sonun: lem yağzü; nûnun: lem yadribâ. Toplam on. İkinci taksim mahalle göre: i'râb sırf harekelerle, sırf harflerle, hazf ile harekelerle ya da hazf ile harflerledir. Bunların birincisi ya üç hareke ile tamdır — ref'te damme, nasbda fetha, cerde kesre — o da munsarif olan müfred isim ve cem'-i mükesserdir: câenî racülün ve ricâlün, raeytü racülen ve ricâlen, merartü bi-racülin ve ricâlin. Nâkıs kısımlar sonraki babda gelir. Litografi sayıları ثلثة ve الثلث şeklinde eski imlâ ile yazar."},
 "examples": [
  {"ar": "وَهُوَ شَيْءٌ جَاءَ مِنَ الْعَامِلِ يَخْتَلِفُ بِهِ آخِرُ الْمُعْرَبِ", "en": "the definition of iʿrāb", "tr": "i'râbın tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "جَاءَنِي زَيْدٌ، وَرَأَيْتُ زَيْدًا، وَمَرَرْتُ بِزَيْدٍ", "en": "the three vowels", "tr": "üç hareke", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "جَاءَنِي أَبُوهُ، وَرَأَيْتُ أَبَاهُ، وَمَرَرْتُ بِأَبِيهِ؛ يَضْرِبَانِ", "en": "the four letters", "tr": "dört harf", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "لَمْ يَضْرِبْ، لَمْ يَغْزُ، لَمْ يَضْرِبَا", "en": "the three droppings", "tr": "üç hazf", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "جَاءَنِي رَجُلٌ وَرِجَالٌ، وَرَأَيْتُ رَجُلًا وَرِجَالًا", "en": "complete iʿrāb by the three vowels", "tr": "üç hareke ile tam i'râb", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "لَمْ يَغْزُو", "right": "لَمْ يَغْزُ", "why": {"en": "the jazm of a defective muḍāriʿ is by dropping the last weak letter", "tr": "nâkıs muzârinin cezmi son illet harfinin hazfi iledir"}},
  {"wrong": "لَمْ يَضْرِبَانِ", "right": "لَمْ يَضْرِبَا", "why": {"en": "after the dual pronoun the jazm is by dropping the nūn", "tr": "tesniye zamirinden sonra cezm nûnun hazfi iledir"}},
  {"wrong": "رَأَيْتُ أَبُوهُ", "right": "رَأَيْتُ أَبَاهُ", "why": {"en": "the six nouns take naṣb by the alif, not the wāw", "tr": "altı isim nasbı vâvla değil elifle alır"}},
  {"wrong": "مَرَرْتُ بِرِجَالَ", "right": "مَرَرْتُ بِرِجَالٍ", "why": {"en": "رِجَال is a declinable broken plural: jarr by kasra with tanwīn", "tr": "ricâl munsarif cem'-i mükesserdir: tenvinli kesre ile mecrûr"}},
 ],
}
ADD_EN = (" Chapter 52 (print pp. 147-148): the third bāb — the definition of iʿrāb and its four interlocking divisions (s1); by essence: vowel, letter, dropping (s2), the three vowels (s3), the four letters (s4), the three droppings and the ten (s5); by locus: the four loci (s6), complete iʿrāb by the three vowels in the declinable singular and broken plural (s7).")
ADD_TR = (" Elli ikinci bab (baskı s. 147-148): üçüncü bab — i'râbın tarifi ve birbirine giren dört taksim (s1); zâta göre: hareke, harf, hazf (s2), üç hareke (s3), dört harf (s4), üç hazf ve on (s5); mahalle göre: dört mahal (s6), munsarif müfred ve cem'-i mükesserde üç hareke ile tam i'râb (s7).")
write_out(52, S, TITLE, ADD_EN, ADD_TR, "pp. 147-148", GLOSS_ADD, notes=(NOTE,),
          related=((K51, [K]), (IRB, [K]), (FN, [K]), (LJ, [K]), (NQV, [K]), (JT, [K])))
report(52, S, GLOSS_ADD, (NOTE,))
