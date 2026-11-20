# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 57: the THIRD division of iʿrāb, by kind — four: rafʿ and naṣb shared by noun and verb, jarr particular to the
# noun, jazm to the verb; the signs — rafʿ four (ḍamma, wāw, alif, nūn), naṣb five (fatḥa, kasra, alif, yāʾ, dropping the nūn), jarr three (kasra, yāʾ,
# fatḥa), jazm three (dropping the vowel, the last letter, the nūn). The FOURTH, by attribute — lafẓī (appearing in the wording), taqdīrī and maḥallī;
# the last two are set out so that whatever is not they is lafẓī. The taqdīrī: what does not appear in the wording but is estimated at the end, the
# preventer being other than a real iʿrāb; only in the muʿrab, like the lafẓī; in seven positions — the FIRST: a muʿrab ending in the alif, even if dropped
# for two sukūns: a noun estimated in all three states (الْعَصَا، عَصًا), a verb estimated in rafʿ and naṣb, lafẓī in jazm (يَخْشَى، لَنْ يَخْشَى، لَمْ يَخْشَ). Print pp. 151–152.
# Orthography: the lithograph prints ثلثة / الثلث (old spelling); the text gives ثَلَاثَةٌ / الثَّلَاثِ. The Ottoman commentary (izhar-full-corrected
# l. 1781) reads الْمَانِعُ فِيهِ غَيْرُ الْإِعْرَابِ الْحَقِيقِيِّ as «because of a preventer other than a real iʿrāb», which the text follows.
#   python3 author_izhar_ch57.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; TQ = "taqsim"; LJ = "lam-jazim"; NQV = "naqis-verbs"; LA = "lam-amr"; MST = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"; ISH = "asma-al-ishara-wa-sighuha"
K = "taqsim-al-irab-bil-naw-wal-sifa-wal-taqdiri-al-awwal"
K56 = "ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh"
TITLE = {"ar": "تَقْسِيمُ الْإِعْرَابِ بِحَسَبِ النَّوْعِ وَعَلَامَاتُهُ، وَبِحَسَبِ الصِّفَةِ: اللَّفْظِيُّ وَالتَّقْدِيرِيُّ وَالْمَحَلِّيُّ، وَالْمَوْضِعُ الْأَوَّلُ لِلتَّقْدِيرِيِّ", "en": "The division of iʿrāb by kind and its signs, and by attribute: lafẓī, taqdīrī and maḥallī; the first position of the taqdīrī", "tr": "İ'râbın nev'e göre taksimi ve alâmetleri, sıfata göre: lafzî, takdîrî ve mahallî; takdîrînin birinci mevzii"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def alamatu(lex, en, tr):
    return [tok("وَعَلَامَةُ", "alama", "noun", [K, AT, MK, ID, IRB], "الْوَاوُ عَاطِفَةٌ، وَعَلَامَةُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the sign of»", "«alâmeti»", segments=wa("عَلَامَةُ", "alama", "noun")),
            tok(lex[0], lex[1], "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", en, tr)]
def sign(form, lex, en, tr, first=False, punct=None):
    if first: return tok(form, lex, "noun", [K, MK, HT, IRB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا " + form + " — أَوْ بَدَلٌ.", en, tr, punct=punct)
    return tok(form, lex, "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ مَرْفُوعٌ.", en, tr, punct=punct, segments=wa(form[2:], lex, "noun"))
def hadhfu(form, lex2, first=False, punct=None):
    return [tok(form, "hadhf", "noun", [K, MK, ID, MSD, IRB] + ([] if first else [AT]), ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ." if first else "الْوَاوُ عَاطِفَةٌ، وَحَذْفُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ."), "«the dropping of»" if first else "«and the dropping of»", "«hazfi»", segments=None if first else wa("حَذْفُ", "hadhf", "noun")),
            tok(lex2[0], lex2[1], "noun", [K, ID, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", lex2[2], lex2[3], punct=punct)]

# ----------- s1 — the third division, by kind
S.append({"id": "s1", "translation": {"en": "And the third division is according to the kind, and it is four: rafʿ and naṣb, shared between the noun and the verb; jarr, particular to the noun; and jazm, particular to the verb.", "tr": "Üçüncü taksim nev'e göredir; o dörttür: isim ile fiil arasında ortak olan ref' ve nasb, isme mahsus cer ve fiile mahsus cezm."},
 "tokens": [
  tok("وَالتَّقْسِيمُ", "taqsim", "noun", [K, AT, MK, TQ], "الْوَاوُ عَاطِفَةٌ، وَالتَّقْسِيمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division»", "«taksim»", segments=wa("التَّقْسِيمُ", "taqsim", "noun")),
  tok("الثَّالِثُ", "thalith", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«third»", "«üçüncü»"),
  tok("بِحَسَبِ", "hasab", "noun", [K, HJ, ID, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَحَسَبِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«according to»", "«-e göre»", segments=[seg("بِ", "bi", "prep"), seg("حَسَبِ", "hasab", "noun")]),
  tok("النَّوْعِ", "naw", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the kind»", "«nev'»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«four»", "«dörttür»", punct=":"),
  tok("رَفْعٌ", "raf", "noun", [K, MK, HT, MSD, IRB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا رَفْعٌ.", "«rafʿ»", "«ref'»"),
  tok("وَنَصْبٌ", "nasb", "noun", [K, AT, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَنَصْبٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and naṣb»", "«ve nasb»", segments=wa("نَصْبٌ", "nasb", "noun")),
  tok("مُشْتَرَكَانِ", "mushtarak", "noun", [K, NA, IMF, F8, MTH], "نَعْتٌ لِرَفْعٌ وَنَصْبٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«shared» — a dual description.", "«ortak» — tesniye sıfat."),
  tok("بَيْنَ", "bayna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasında»"),
  tok("الِاسْمِ", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the noun»", "«isim»"),
  tok("وَالْفِعْلِ", "fil", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَالْفِعْلِ مَعْطُوفٌ مَجْرُورٌ.", "«and the verb»", "«ve fiil»", punct="،", segments=wa("الْفِعْلِ", "fil", "noun")),
  tok("وَجَرٌّ", "jarr", "noun", [K, AT, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَرٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and jarr»", "«ve cer»", segments=wa("جَرٌّ", "jarr", "noun")),
  tok("مُخْتَصٌّ", "mukhtass", "noun", [K, NA, IMF, F8], "نَعْتٌ مَرْفُوعٌ.", "«particular»", "«mahsus»"),
  tok("بِالِاسْمِ", "ism", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالِاسْمِ مَجْرُورٌ.", "«to the noun»", "«isme»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الِاسْمِ", "ism", "noun")]),
  tok("وَجَزْمٌ", "jazm", "noun", [K, AT, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَزْمٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and jazm»", "«ve cezm»", segments=wa("جَزْمٌ", "jazm", "noun")),
  tok("مُخْتَصٌّ", "mukhtass", "noun", [K, NA, IMF, F8], "نَعْتٌ مَرْفُوعٌ.", "«particular»", "«mahsus»"),
  tok("بِالْفِعْلِ", "fil", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفِعْلِ مَجْرُورٌ.", "«to the verb»", "«fiile»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْفِعْلِ", "fil", "noun")]),
 ]})
# ----------- s2 — the signs of each
S.append({"id": "s2", "translation": {"en": "And the signs of rafʿ are four: ḍamma, wāw, alif and nūn; the signs of naṣb five: fatḥa, kasra, alif, yāʾ and the dropping of the nūn; the signs of jarr three: kasra, yāʾ and fatḥa; and the signs of jazm three: the dropping of the vowel, the dropping of the last letter and the dropping of the nūn.", "tr": "Ref'in alâmeti dörttür: damme, vâv, elif ve nûn; nasbın alâmeti beştir: fetha, kesre, elif, yâ ve nûnun hazfi; cerin alâmeti üçtür: kesre, yâ ve fetha; cezmin alâmeti üçtür: harekenin hazfi, sonun hazfi ve nûnun hazfi."},
 "tokens": [
  *alamatu(("الرَّفْعِ", "raf"), "«rafʿ»", "«ref'in»"),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«four»", "«dörttür»", punct=":"),
  sign("ضَمَّةٌ", "damma", "«ḍamma»", "«damme»", first=True),
  sign("وَوَاوٌ", "waw-letter", "«wāw»", "«vâv»"),
  sign("وَأَلِفٌ", "alif-letter", "«alif»", "«elif»"),
  sign("وَنُونٌ", "nun-letter", "«nūn»", "«nûn»", punct="،"),
  *alamatu(("النَّصْبِ", "nasb"), "«naṣb»", "«nasbın»"),
  tok("خَمْسَةٌ", "khamsa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«five»", "«beştir»", punct=":"),
  sign("فَتْحَةٌ", "fatha", "«fatḥa»", "«fetha»", first=True),
  sign("وَكَسْرَةٌ", "kasra", "«kasra» — in the sound feminine plural", "«kesre» — cem'-i müennes-i sâlimde"),
  sign("وَأَلِفٌ", "alif-letter", "«alif» — in the six nouns", "«elif» — altı isimde"),
  sign("وَيَاءٌ", "ya-letter", "«yāʾ» — in the dual and the sound plural", "«yâ» — tesniye ve sâlim cemide"),
  *hadhfu("وَحَذْفُ", ("النُّونِ", "nun-letter", "«the nūn» — after the rafʿ pronouns", "«nûnun» — merfû zamirlerden sonra"), punct="،"),
  *alamatu(("الْجَرِّ", "jarr"), "«jarr»", "«cerin»"),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ — الطَّبْعُ: ثلثة.", "«three» — the print spells it ثلثة.", "«üçtür» — baskıda ثلثة.", punct=":"),
  sign("كَسْرَةٌ", "kasra", "«kasra»", "«kesre»", first=True),
  sign("وَيَاءٌ", "ya-letter", "«yāʾ»", "«yâ»"),
  sign("وَفَتْحَةٌ", "fatha", "«fatḥa» — in the diptote", "«fetha» — gayr-ı munsarifte", punct="،"),
  *alamatu(("الْجَزْمِ", "jazm"), "«jazm»", "«cezmin»"),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«three»", "«üçtür»", punct=":"),
  *hadhfu("حَذْفُ", ("الْحَرَكَةِ", "haraka", "«the vowel»", "«harekenin»"), first=True),
  *hadhfu("وَحَذْفُ", ("الْآخِرِ", "akhir", "«the last letter»", "«sonun»")),
  *hadhfu("وَحَذْفُ", ("النُّونِ", "nun-letter", "«the nūn»", "«nûnun»"), punct="."),
 ]})
# ----------- s3 — the fourth division, by attribute
S.append({"id": "s3", "translation": {"en": "And the fourth division is according to the attribute: it is three — lafẓī, which appears in the wording; taqdīrī; and maḥallī. So let us mention the last two, so that it be known that whatever is other than them is lafẓī.", "tr": "Dördüncü taksim sıfata göredir: üçtür — lafızda görünen lafzî, takdîrî ve mahallî. Son ikisini zikredelim ki onların dışındakinin lafzî olduğu bilinsin."},
 "tokens": [
  tok("وَالتَّقْسِيمُ", "taqsim", "noun", [K, AT, MK, TQ], "الْوَاوُ عَاطِفَةٌ، وَالتَّقْسِيمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division»", "«taksim»", segments=wa("التَّقْسِيمُ", "taqsim", "noun")),
  tok("الرَّابِعُ", "rabi-fourth", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«fourth»", "«dördüncü»"),
  tok("بِحَسَبِ", "hasab", "noun", [K, HJ, ID, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَحَسَبِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«according to»", "«-e göre»", segments=[seg("بِ", "bi", "prep"), seg("حَسَبِ", "hasab", "noun")]),
  tok("الصِّفَةِ", "sifa", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — صِفَةِ الْإِعْرَابِ: ظُهُورُهُ أَوْ تَقْدِيرُهُ أَوْ مَحَلُّهُ.", "«the attribute» — of the iʿrāb: shown, estimated, or by position.", "«sıfat» — i'râbın: görünmesi, takdiri ya da mahalli.", punct="،"),
  tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«it is»", "«o»", segments=fa("هُوَ", "huwa", "pron")),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«three»", "«üçtür»", punct=":"),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, MK, HT, NSB, IRB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا لَفْظِيٌّ.", "«lafẓī»", "«lafzî»"),
  tok("يَظْهَرُ", "zahara", "verb", [K, NA, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ.", "«which appears» — the describing clause.", "«görünen» — sıfat cümlesi."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("اللَّفْظِ", "lafz", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the wording»", "«lafız»", punct="،"),
  tok("وَتَقْدِيرِيٌّ", "taqdiri", "noun", [K, AT, NSB, IRB], "الْوَاوُ عَاطِفَةٌ، وَتَقْدِيرِيٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and taqdīrī» — estimated", "«ve takdîrî»", punct="،", segments=wa("تَقْدِيرِيٌّ", "taqdiri", "noun")),
  tok("وَمَحَلِّيٌّ", "mahalli", "noun", [K, AT, NSB, IRB], "الْوَاوُ عَاطِفَةٌ، وَمَحَلِّيٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and maḥallī» — by position", "«ve mahallî»", punct="،", segments=wa("مَحَلِّيٌّ", "mahalli", "noun")),
  tok("فَلْنَذْكُرِ", "dhakara", "verb", [K, AT, LA, JZ], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لَامُ الْأَمْرِ، وَنَذْكُرِ مُضَارِعٌ مَجْزُومٌ بِهَا، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«so let us mention» — the lām of command on the first person.", "«zikredelim» — birinci şahısta emir lâmı.", segments=[seg("فَ", "fa", "conj"), seg("لْ", "lam-amr", "part"), seg("نَذْكُرِ", "dhakara", "verb")]),
  tok("الْأَخِيرَيْنِ", "akhir-last", "noun", [K, MB, MTH], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ — مُثَنًّى: التَّقْدِيرِيَّ وَالْمَحَلِّيَّ.", "«the last two» — the taqdīrī and the maḥallī.", "«son ikisini» — takdîrî ve mahallî."),
  tok("حَتَّى", "hatta", "part", [K, JZ, AMS], "حَرْفُ غَايَةٍ وَتَعْلِيلٍ، يُنْصَبُ الْمُضَارِعُ بَعْدَهَا بِأَنْ مُضْمَرَةٍ.", "«so that»", "«ki … -sin»"),
  tok("يُعْلَمَ", "alima", "verb", [K, JZ, NF, AMS], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«it be known»", "«bilinsin»"),
  tok("أَنَّ", "anna", "part", [K, IN, NF], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ نَائِبُ فَاعِلٍ.", "«that» — the clause is the deputy doer.", "«… olduğu» — mastar-ı müevvel nâib-i fâil."),
  tok("مَا", "ma-mawsula", "pron", [K, IN, MAW], "اسْمٌ مَوْصُولٌ اسْمُ أَنَّ فِي مَحَلِّ نَصْبٍ.", "«whatever»", "«ne»"),
  tok("عَدَاهُمَا", "ada-except", "verb", [K, MAW, MST, MB], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ، وَهُمَا مَفْعُولٌ بِهِ — صِلَةُ مَا.", "«is other than them» — the exceptive verb; the ṣila.", "«onların dışında» — istisnâ fiili; sıla.", segments=[seg("عَدَا", "ada-except", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, IN, NSB, IRB], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is lafẓī»", "«lafzîdir»", punct="،"),
 ]})
# ----------- s4 — the taqdīrī defined; seven positions
S.append({"id": "s4", "translation": {"en": "So the taqdīrī is what does not appear in the wording but is estimated at its end, the preventer in it being other than a real iʿrāb; and it is only in the muʿrab, like the lafẓī; and that is in seven positions:", "tr": "Takdîrî, lafızda görünmeyip sonunda takdir edilendir; ondaki engel hakikî i'râbdan başkadır; lafzî gibi ancak mu'rebde olur; o da yedi mevzidedir:"},
 "tokens": [
  tok("فَالتَّقْدِيرِيُّ", "taqdiri", "noun", [K, AT, MK, NSB, IRB], "الْفَاءُ لِلتَّفْرِيعِ، وَالتَّقْدِيرِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the taqdīrī»", "«takdîrî»", segments=fa("التَّقْدِيرِيُّ", "taqdiri", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dir»"),
  tok("لَا", "la", "part", [K, LN, MAW], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ صِلَةٌ.", "«not»", "«-meyen»"),
  tok("يَظْهَرُ", "zahara", "verb", [K, MR, LN, MAW], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«does appear»", "«görünmeyen»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("اللَّفْظِ", "lafz", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the wording»", "«lafız»"),
  tok("بَلْ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ.", "«but rather»", "«bilakis»"),
  tok("يُقَدَّرُ", "qaddara", "verb", [K, AT, MR, NF, F2], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«is estimated»", "«takdir edilir»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«at»", "«-de»"),
  tok("آخِرِهِ", "akhir", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonunda»", punct="،", segments=[seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("الْمَانِعُ", "mani-preventer", "noun", [K, MK, IFA, "hal"], "مُبْتَدَأٌ مَرْفُوعٌ — وَالْجُمْلَةُ حَالٌ: وَالْمَانِعُ فِيهِ.", "«the preventer» — a ḥāl-clause: the preventer in it being …", "«engel» — hâl cümlesi: ondaki engel …"),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — مُتَعَلِّقٌ بِالْمَانِعِ.", "«in it»", "«ondaki»", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«other than»", "«başkadır»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbdan»"),
  tok("الْحَقِيقِيِّ", "haqiqi", "noun", [K, NA, NSB], "نَعْتٌ مَجْرُورٌ — فَخَرَجَ الْمَحَلِّيُّ، فَإِنَّ الْمَانِعَ فِيهِ إِعْرَابٌ حَقِيقِيٌّ كَالْحِكَايَةِ.", "«real» — excluding the maḥallī, where a real iʿrāb blocks the end.", "«hakikî» — mahallî dışarıda; onda engel hikâye gibi hakikî bir i'râbdır.", punct="،"),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -maz»", segments=wa("لَا", "la", "part")),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR, LN], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«is»", "«olur»"),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except»", "«ancak»"),
  tok("فِي", "fi", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُ.", "«in»", "«-de»"),
  tok("الْمُعْرَبِ", "murab", "noun", [K, HJ, IMF, F4, IRB], "مَجْرُورٌ بِفِي.", "«the muʿrab»", "«mu'rebde»"),
  tok("كَاللَّفْظِيِّ", "lafzi", "noun", [K, HJ, NSB], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَاللَّفْظِيِّ مَجْرُورٌ.", "«like the lafẓī»", "«lafzî gibi»", punct="،", segments=[seg("كَ", "ka", "prep"), seg("اللَّفْظِيِّ", "lafzi", "noun")]),
  tok("وَذٰلِكَ", "dhalika", "pron", [K, AT, MK, ISH], "الْوَاوُ عَاطِفَةٌ، وَذٰلِكَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=wa("ذٰلِكَ", "dhalika", "pron")),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — خَبَرٌ.", "«in»", "«-de»"),
  tok("سَبْعَةِ", "saba-seven", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«seven»", "«yedi»"),
  tok("مَوَاضِعَ", "mawdi", "noun", [K, ID, JT, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — جَمْعُ مَوْضِعٍ عَلَى مَفَاعِلَ، غَيْرُ مُنْصَرِفٍ.", "«positions» — the faʿālil-type plural, a diptote.", "«mevzide» — feâlil türü cemi, gayr-ı munsarif.", punct=":"),
 ]})
# ----------- s5 — the first position: the alif-ending
S.append({"id": "s5", "translation": {"en": "The first: a muʿrab whose end is an alif — even if it is dropped for the meeting of two sukūns; if it is a noun, its iʿrāb in the three states is taqdīrī — as in al-ʿaṣā and ʿaṣan; and if it is a verb, its rafʿ and its naṣb are taqdīrī and its jazm lafẓī — as in yakhshā, lan yakhshā and lam yakhsha.", "tr": "Birincisi: sonu elif olan mu'reb — iki sâkinin karşılaşması için hazfedilse de; isim ise üç hâlde i'râbı takdîrîdir — el-asâ ve asan gibi; fiil ise ref'i ve nasbı takdîrî, cezmi lafzîdir — yahşâ, len yahşâ ve lem yahşe gibi."},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first»", "«birincisi»"),
  tok("مُعْرَبٌ", "murab", "noun", [K, MK, IMF, F4, IRB], "خَبَرٌ مَرْفُوعٌ.", "«a muʿrab»", "«bir mu'reb»"),
  tok("آخِرُهُ", "akhir", "noun", [K, NA, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِمُعْرَبٌ.", "«whose end is» — the describing clause.", "«sonu» — sıfat cümlesi.", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("أَلِفٌ", "alif-letter", "noun", [K, MK, MQ], "خَبَرٌ مَرْفُوعٌ.", "«an alif»", "«elif»"),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ لِلْحَالِ، وَإِنْ وَصْلِيَّةٌ.", "«even if»", "«… -se de»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("حُذِفَ", "hadhafa", "verb", [K, INS, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْأَلِفُ.", "«it is dropped» — the alif.", "«hazfedilse» — elif."),
  tok("لِالْتِقَاءِ", "iltiqa", "noun", [K, HJ, ID, MSD, F8], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَالْتِقَاءِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ الْتَقَى.", "«for the meeting of»", "«karşılaşması için»", segments=[seg("لِ", "li", "prep"), seg("الْتِقَاءِ", "iltiqa", "noun")]),
  tok("السَّاكِنَيْنِ", "sakin", "noun", [K, ID, MTH, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى: نَحْوُ الْعَصَا الَّتِي رَأَيْتُهَا.", "«the two sukūns» — as in al-ʿaṣā before a hamzat al-waṣl.", "«iki sâkinin» — vasıl hemzesi önünde el-asâ gibi.", punct="،"),
  tok("فَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if»", "«eğer»", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»"),
  tok("اسْمًا", "ism", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a noun»", "«isim»"),
  tok("فَإِعْرَابُهُ", "irab", "noun", [K, INS, MK, ID, MSD, IRB], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَإِعْرَابُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its iʿrāb»", "«i'râbı»", segments=[seg("فَ", "fa", "conj"), seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَحْوَالِ", "hal", "noun", [K, HJ, JT], "مَجْرُورٌ بِفِي — جَمْعُ حَالٍ.", "«the states»", "«hâllerde»"),
  tok("الثَّلَاثِ", "thalatha", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ — الطَّبْعُ: الثلث.", "«three» — the print spells it الثلث.", "«üç» — baskıda الثلث."),
  tok("تَقْدِيرِيٌّ", "taqdiri", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", "«taqdīrī»", "«takdîrîdir»", punct="،"),
  nahw(),
  tok("الْعَصَا", "asa-staff", "noun", [K, ID, MQ, IRB], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمٌ مَقْصُورٌ.", "«the staff» — a maqṣūr noun; all three cases estimated.", "«asâ» — maksûr isim; üç hâl takdîrî."),
  tok("وَعَصًا", "asa-staff", "noun", [K, AT, MQ, IRB], "الْوَاوُ عَاطِفَةٌ، وَعَصًا مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — بِالتَّنْوِينِ، وَالْأَلِفُ مَحْذُوفَةٌ لَفْظًا.", "«and a staff» — with tanwīn; the alif dropped in speech.", "«ve bir asâ» — tenvinli; elif lafzen düşmüş.", punct="،", segments=wa("عَصًا", "asa-staff", "noun")),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ.", "«it is»", "«ise»"),
  tok("فِعْلًا", "fil", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a verb»", "«fiil»"),
  tok("فَرَفْعُهُ", "raf", "noun", [K, INS, MK, ID, MSD, IRB], "الْفَاءُ رَابِطَةٌ، وَرَفْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its rafʿ»", "«ref'i»", segments=[seg("فَ", "fa", "conj"), seg("رَفْعُ", "raf", "noun"), pr3ms()]),
  tok("وَنَصْبُهُ", "nasb", "noun", [K, AT, MK, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَنَصْبُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its naṣb»", "«ve nasbı»", segments=[seg("وَ", "wa", "conj"), seg("نَصْبُ", "nasb", "noun"), pr3ms()]),
  tok("تَقْدِيرِيٌّ", "taqdiri", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", "«are taqdīrī»", "«takdîrîdir»"),
  tok("وَجَزْمُهُ", "jazm", "noun", [K, AT, MK, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَزْمُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jazm»", "«cezmi»", segments=[seg("وَ", "wa", "conj"), seg("جَزْمُ", "jazm", "noun"), pr3ms()]),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ — بِحَذْفِ الْأَلِفِ.", "«lafẓī» — by dropping the alif.", "«lafzîdir» — elifin hazfiyle.", punct="،"),
  nahw(),
  tok("يَخْشَى", "khashiya", "verb", [K, MR, NQV, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«he fears» — rafʿ estimated on the alif.", "«korkar» — elifte takdîrî damme."),
  tok("وَلَنْ", "lan", "part", [K, AT, JZ], "الْوَاوُ عَاطِفَةٌ، وَلَنْ حَرْفُ نَفْيٍ وَنَصْبٍ.", "«and … will not»", "«ve … -meyecek»", segments=wa("لَنْ", "lan", "part")),
  tok("يَخْشَى", "khashiya", "verb", [K, JZ, NQV, IRB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«fear» — naṣb estimated on the alif.", "«korkmayacak» — elifte takdîrî fetha."),
  tok("وَلَمْ", "lam", "part", [K, AT, LJ, JZ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … did not»", "«ve … -medi»", segments=wa("لَمْ", "lam", "part")),
  tok("يَخْشَ", "khashiya", "verb", [K, LJ, JZ, NQV, IRB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ بِحَذْفِ الْأَلِفِ — لَفْظِيٌّ.", "«fear» — jazm by dropping the alif, shown.", "«korkmadı» — elifin hazfiyle meczûm, lafzî.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "taqdiri": G("taqdiri", "تَقْدِيرِيّ", "ق د ر", "noun", "estimated, taqdīrī — of an iʿrāb assumed at an end that cannot show it", "takdîrî — sonunda gösterilemeyip takdir edilen i'râb", 3),
 "mani-preventer": G("mani-preventer", "مَانِع", "م ن ع", "noun", "a preventer, what bars (active participle of manaʿa)", "mâni, engel (menea'nın ism-i fâili)", 3),
 "iltiqa": G("iltiqa", "الْتِقَاء", "ل ق ي", "noun", "meeting, encounter — iltiqāʾ al-sākinayn, the meeting of two sukūns", "karşılaşma, iltikâ — iltikâü's-sâkineyn, iki sâkinin karşılaşması", 3),
 "asa-staff": G("asa-staff", "عَصًا", "ع ص و", "noun", "a staff, a stick — the maqṣūr noun (al-ʿaṣā)", "asâ, değnek — maksûr isim (el-asâ)", 2, plural="عِصِيّ"),
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
print("izhar ch57 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("zahara", "dhakara", "alima", "ada-except", "qaddara", "kana", "hadhafa", "khashiya") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "أَنْوَاعُ الْإِعْرَابِ الْأَرْبَعَةُ وَعَلَامَاتُهَا، وَصِفَاتُهُ: اللَّفْظِيُّ وَالتَّقْدِيرِيُّ وَالْمَحَلِّيُّ، وَالْمَوْضِعُ الْأَوَّلُ لِلتَّقْدِيرِيِّ: الْمُعْرَبُ آخِرُهُ أَلِفٌ", "en": "The four kinds of iʿrāb and their signs; its attributes — lafẓī, taqdīrī, maḥallī; the first taqdīrī position: the muʿrab ending in alif", "tr": "İ'râbın dört nev'i ve alâmetleri; sıfatları — lafzî, takdîrî, mahallî; takdîrînin birinci mevzii: sonu elif olan mu'reb"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الإعراب: التقسيم بحسب النوع والصفة", "الكافية لابن الحاجب — الإعراب التقديري", "شرح قطر الندى لابن هشام — المقصور والمنقوص"],
 "amil": "by kind the iʿrāb is four: rafʿ and naṣb shared by noun and verb, jarr the noun's, jazm the verb's; the signs — rafʿ: ḍamma, wāw, alif, nūn; naṣb: fatḥa, kasra, alif, yāʾ, dropping the nūn; jarr: kasra, yāʾ, fatḥa; jazm: dropping the vowel, the last letter, the nūn. By attribute: lafẓī (shown), taqdīrī, maḥallī. The taqdīrī is estimated at the end, barred by something other than a real iʿrāb, only in the muʿrab; seven positions — the first, the alif-ending: a noun estimated in all three states (الْعَصَا، عَصًا), a verb estimated in rafʿ and naṣb and shown in jazm (يَخْشَى، لَنْ يَخْشَى، لَمْ يَخْشَ).",
 "question": {
  "en": ["What are the four kinds of iʿrāb, and who takes which? Rafʿ and naṣb, shared by noun and verb; jarr, the noun's alone; jazm, the verb's alone.",
         "How many signs has each kind? Rafʿ four (ḍamma, wāw, alif, nūn), naṣb five (fatḥa, kasra, alif, yāʾ, the nūn dropped), jarr three (kasra, yāʾ, fatḥa), jazm three (the vowel, the last letter, the nūn dropped) — fifteen, the ten signs counted by the kinds they serve.",
         "Why is the kasra a sign of naṣb and the fatḥa a sign of jarr? The sound feminine plural takes naṣb by kasra (مُسْلِمَاتٍ); the diptote takes jarr by fatḥa (بِأَحْمَدَ).",
         "What are the three attributes? Lafẓī — the sign appears in the wording; taqdīrī — it is assumed at an end that cannot show it; maḥallī — the word's position carries the case while its end is busy with something else.",
         "Why does the author set out only the last two? So that whatever is neither taqdīrī nor maḥallī is known to be lafẓī — the default needs no list.",
         "What bars the taqdīrī iʿrāb from showing? Something other than a real iʿrāb — the alif, the yāʾ, the speaker's yāʾ, the pause; where a real iʿrāb occupies the end (the cited word), the case is maḥallī instead.",
         "What is the first taqdīrī position? The muʿrab ending in alif — even where the alif is dropped for two sukūns: the noun الْعَصَا / عَصًا estimated in all three states; the verb يَخْشَى estimated in rafʿ and naṣb, its jazm shown by dropping the alif: لَمْ يَخْشَ.",
         "What does the engine READ here? The DabtEngine reads the four kinds and their signs as the khabar-lists they are, الْمَانِعُ فِيهِ غَيْرُ … as the ḥāl-clause of the commentary's reading, مَوَاضِعَ in jarr by fatḥa as a diptote, الْعَصَا and عَصًا with an estimated kasra, يَخْشَى with the estimated ḍamma and fatḥa, and لَمْ يَخْشَ by the dropped alif."],
  "tr": ["İ'râbın dört nev'i nedir, hangisini kim alır? İsim ile fiilde ortak ref' ve nasb; yalnız ismin ceri; yalnız fiilin cezmi.",
         "Her nev'in kaç alâmeti var? Ref' dört (damme, vâv, elif, nûn), nasb beş (fetha, kesre, elif, yâ, nûnun hazfi), cer üç (kesre, yâ, fetha), cezm üç (hareke, son harf, nûn hazfi) — on beş; on alâmet hizmet ettikleri nev'e göre sayılır.",
         "Kesre neden nasb, fetha neden cer alâmetidir? Cem'-i müennes-i sâlim nasbı kesre ile alır (müslimâtin); gayr-ı munsarif ceri fetha ile alır (bi-Ahmede).",
         "Üç sıfat nedir? Lafzî — alâmet lafızda görünür; takdîrî — gösteremeyen sonda varsayılır; mahallî — sonu başka şeyle meşgulken kelimenin mahalli i'râbı taşır.",
         "Müellif neden yalnız son ikisini açıklar? Takdîrî ve mahallî olmayanın lafzî olduğu bilinsin diye — asıl olan liste istemez.",
         "Takdîrî i'râbın görünmesini ne engeller? Hakikî i'râbdan başka bir şey — elif, yâ, mütekellim yâsı, vakf; sonu hakikî bir i'râb tutuyorsa (hikâye edilen söz) i'râb mahallîdir.",
         "Takdîrînin birinci mevzii nedir? Sonu elif olan mu'reb — elif iki sâkin için düşse de: el-asâ / asan ismi üç hâlde takdîrî; yahşâ fiili ref' ve nasbda takdîrî, cezmi elifin hazfiyle lafzî: lem yahşe.",
         "Motor burada neyi OKUR? DabtEngine dört nev'i ve alâmetlerini haber listeleri, el-mâniu fîhi gayru …'yu şerhin okuyuşuyla hâl cümlesi, mevâdıa'yı fetha ile mecrûr gayr-ı munsarif, el-asâ ve asan'ı takdîrî kesreyle, yahşâ'yı takdîrî damme ve fethayla, lem yahşe'yi düşen elifle okur."],
 },
 "plain": {"en": "Case has four kinds: rafʿ and naṣb for nouns and verbs alike, jarr only for nouns, jazm only for verbs, each with its own signs. A sign may be visible (lafẓī), assumed where the word's end cannot show it (taqdīrī), or carried by the word's position (maḥallī). Words ending in alif, like al-ʿaṣā, take assumed vowels.",
           "tr": "İ'râb dört nev'dir: ref' ve nasb isim ve fiilde ortak, cer yalnız isimde, cezm yalnız fiilde; her birinin kendi alâmetleri var. Alâmet görünür (lafzî), sözcüğün sonu gösteremediği için varsayılır (takdîrî) ya da sözcüğün yerinde taşınır (mahallî). El-asâ ya da yahşâ gibi elifle bitenler varsayılan hareke alır."},
 "explanation": {"en": "The third division is by kind: four — rafʿ and naṣb, shared between noun and verb; jarr, particular to the noun; jazm, particular to the verb. The sign of rafʿ is four: ḍamma, wāw, alif, nūn; of naṣb five: fatḥa, kasra, alif, yāʾ and the dropping of the nūn; of jarr three: kasra, yāʾ, fatḥa; of jazm three: the dropping of the vowel, of the last letter, of the nūn. The fourth division is by attribute: three — lafẓī, which appears in the wording; taqdīrī; maḥallī. The author sets out the last two so that whatever is other than them is known to be lafẓī. The taqdīrī is what does not appear in the wording but is estimated at the end, the preventer being other than a real iʿrāb (the commentary's reading: «because of a preventer other than the real iʿrāb»); it is only in the muʿrab, like the lafẓī, and it is in seven positions. The first: a muʿrab whose end is an alif, even if that alif is dropped for the meeting of two sukūns — if a noun, its iʿrāb in the three states is taqdīrī: الْعَصَا، عَصًا; if a verb, its rafʿ and naṣb are taqdīrī and its jazm lafẓī: يَخْشَى، لَنْ يَخْشَى، لَمْ يَخْشَ. The remaining six positions follow. The lithograph spells the numerals ثلثة and الثلث in the old orthography.",
                 "tr": "Üçüncü taksim nev'e göredir: dört — isim ile fiil arasında ortak ref' ve nasb; isme mahsus cer; fiile mahsus cezm. Ref'in alâmeti dört: damme, vâv, elif, nûn; nasbınki beş: fetha, kesre, elif, yâ ve nûnun hazfi; cerinki üç: kesre, yâ, fetha; cezminki üç: harekenin, sonun, nûnun hazfi. Dördüncü taksim sıfata göredir: üç — lafızda görünen lafzî; takdîrî; mahallî. Müellif son ikisini açıklar ki onların dışındakinin lafzî olduğu bilinsin. Takdîrî, lafızda görünmeyip sonda takdir edilendir; engel hakikî i'râbdan başkadır (şerhin okuyuşu: «hakikî i'râbın gayrı bir mâni'den dolayı»); lafzî gibi ancak mu'rebdedir ve yedi mevzidedir. Birincisi: sonu elif olan mu'reb, o elif iki sâkinin karşılaşması için düşse de — isimse üç hâlde i'râbı takdîrî: el-asâ, asan; fiilse ref'i ve nasbı takdîrî, cezmi lafzî: yahşâ, len yahşâ, lem yahşe. Kalan altı mevzi gelir. Litografi sayıları ثلثة ve الثلث şeklinde eski imlâ ile yazar."},
 "examples": [
  {"ar": "رَفْعٌ وَنَصْبٌ مُشْتَرَكَانِ بَيْنَ الِاسْمِ وَالْفِعْلِ، وَجَرٌّ مُخْتَصٌّ بِالِاسْمِ، وَجَزْمٌ مُخْتَصٌّ بِالْفِعْلِ", "en": "the four kinds", "tr": "dört nev'", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَعَلَامَةُ النَّصْبِ خَمْسَةٌ: فَتْحَةٌ وَكَسْرَةٌ وَأَلِفٌ وَيَاءٌ وَحَذْفُ النُّونِ", "en": "the five signs of naṣb", "tr": "nasbın beş alâmeti", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "لَفْظِيٌّ يَظْهَرُ فِي اللَّفْظِ، وَتَقْدِيرِيٌّ، وَمَحَلِّيٌّ", "en": "the three attributes", "tr": "üç sıfat", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "الْمَانِعُ فِيهِ غَيْرُ الْإِعْرَابِ الْحَقِيقِيِّ", "en": "the taqdīrī defined against the maḥallī", "tr": "takdîrînin mahallîye karşı tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "نَحْوُ الْعَصَا وَعَصًا … نَحْوُ يَخْشَى وَلَنْ يَخْشَى وَلَمْ يَخْشَ", "en": "the alif-ending noun and verb", "tr": "sonu elif olan isim ve fiil", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "لَمْ يَخْشَى", "right": "لَمْ يَخْشَ", "why": {"en": "the jazm of the alif-ending verb is shown by dropping the alif", "tr": "sonu elifli fiilin cezmi elifin hazfiyle gösterilir"}},
  {"wrong": "رَأَيْتُ الْعَصَى (with a visible fatḥa)", "right": "رَأَيْتُ الْعَصَا", "why": {"en": "the maqṣūr noun's naṣb is estimated on the alif; nothing appears", "tr": "maksûr ismin nasbı elifte takdîrîdir; hiçbir şey görünmez"}},
  {"wrong": "the fatḥa is only a sign of naṣb", "right": "the fatḥa is also a sign of jarr (بِأَحْمَدَ)", "why": {"en": "the diptote takes jarr by fatḥa", "tr": "gayr-ı munsarif ceri fetha ile alır"}},
  {"wrong": "jarr on a verb or jazm on a noun", "right": "jarr is the noun's alone, jazm the verb's alone", "why": {"en": "the two particular kinds never cross", "tr": "iki mahsus nev' asla yer değiştirmez"}},
 ],
}
ADD_EN = (" Chapter 57 (print pp. 151-152): the division by kind — the four kinds (s1) and their fifteen signs (s2); the division by attribute — lafẓī, taqdīrī, maḥallī (s3); the taqdīrī defined, seven positions (s4); the first, the alif-ending noun and verb (s5).")
ADD_TR = (" Elli yedinci bab (baskı s. 151-152): nev'e göre taksim — dört nev' (s1) ve on beş alâmet (s2); sıfata göre taksim — lafzî, takdîrî, mahallî (s3); takdîrînin tarifi, yedi mevzi (s4); birincisi, sonu elif olan isim ve fiil (s5).")
write_out(57, S, TITLE, ADD_EN, ADD_TR, "pp. 151-152", GLOSS_ADD, notes=(NOTE,),
          related=((K56, [K]), (IRB, [K]), (MQ, [K]), (NQV, [K]), (LJ, [K]), (TQ, [K])))
report(57, S, GLOSS_ADD, (NOTE,))
