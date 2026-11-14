# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 59: the taqdīrī's FOURTH position — what ends in a yāʾ with kasra before it, even if dropped for two sukūns: a
# noun estimated in rafʿ and jarr (الْقَاضِي، قَاضٍ), a verb in rafʿ only when no pronoun is attached (يَرْمِي، تَرْمِي، أَرْمِي، نَرْمِي); the FIFTH — a verb ending in a
# wāw with ḍamma before it, rafʿ only estimated without a pronoun (يَغْزُو، تَغْزُو، أَغْزُو، نَغْزُو); the SIXTH — a noun declined by letters meeting a sukūn after
# it (a word beginning with hamzat al-waṣl): the six nouns estimated in all three states (أَبُو الْقَاسِمِ، أَبَا الْقَاسِمِ، بِأَبِي الْقَاسِمِ); the sound masculine
# plural with a fatḥa before the letter of iʿrāb (مُصْطَفَوْنَ، مُصْطَفَيْنَ) has its wāw vowelled with ḍamma and its yāʾ with kasra, so lafẓī throughout
# (مُصْطَفُو الْقَوْمِ، مُصْطَفِي الْقَوْمِ، بِمُصْطَفِي الْقَوْمِ); without the fatḥa the two are dropped, so taqdīrī throughout (ضَارِبُو الْقَوْمِ، ضَارِبِي الْقَوْمِ، بِضَارِبِي
# الْقَوْمِ); the dual estimated in rafʿ, while in naṣb and jarr its yāʾ takes kasra, so lafẓī (غُلَامَا ابْنِكَ، غُلَامَيِ ابْنِكَ، بِغُلَامَيِ ابْنِكَ). Print pp. 153–155.
# Orthography: the lithograph prints الثلث (old spelling); the text gives الثَّلَاثِ. The Ottoman commentary (izhar-full-corrected l. 1816 ff.) is followed.
#   python3 author_izhar_ch59.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; JDS = "jam-mudhakkar-salim"; FN = "five-nouns"; NQV = "naqis-verbs"; LJ = "lam-jazim"; HMZ = "hadhf-wa-taqdir"
K = "al-taqdiri-al-rabi-ila-al-sadis-al-ya-wal-waw-wal-murab-bil-huruf-qabl-al-sakin"
K58 = "al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"
TITLE = {"ar": "الْمَوَاضِعُ الرَّابِعُ وَالْخَامِسُ وَالسَّادِسُ لِلتَّقْدِيرِيِّ: الْمَنْقُوصُ، وَالْفِعْلُ الْوَاوِيُّ، وَالْمُعْرَبُ بِالْحُرُوفِ قَبْلَ السَّاكِنِ", "en": "The fourth, fifth and sixth positions of the taqdīrī: the yāʾ-ending word, the wāw-ending verb, and the letter-declined noun before a sukūn", "tr": "Takdîrînin dördüncü, beşinci ve altıncı mevzileri: sonu yâlı kelime, sonu vâvlı fiil ve sâkinden önce harfle mu'reb isim"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def fain_kana(f=True): return [tok("فَإِنْ" if f else "وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], ("الْفَاءُ لِلتَّفْرِيعِ" if f else "الْوَاوُ عَاطِفَةٌ") + "، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if»" if f else "«and if»", "«eğer»" if f else "«ve eğer»", segments=(fa if f else wa)("إِنْ", "in-shartiyya", "part")), tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»")]
def rafuhu(f=True): return tok("فَرَفْعُهُ", "raf", "noun", [K, INS, MK, ID, MSD, IRB], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَرَفْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its rafʿ»", "«ref'i»", segments=[seg("فَ", "fa", "conj"), seg("رَفْعُ", "raf", "noun"), pr3ms()])
def taqdiri(punct=None, en="«is taqdīrī»"): return tok("تَقْدِيرِيٌّ", "taqdiri", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", en, "«takdîrîdir»", punct=punct)
def lafzi(punct=None, en="«is lafẓī»"): return tok("لَفْظِيٌّ", "lafzi", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", en, "«lafzîdir»", punct=punct)
def in_lam_yalhaq(): return [tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ، وَالْجَوَابُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«if»", "«eğer»"), tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-memişse»"), tok("يَلْحَقْ", "lahiqa", "verb", [K, INS, LJ, JZ], "فِعْلُ الشَّرْطِ، مُضَارِعٌ مَجْزُومٌ بِلَمْ.", "«is attached»", "«bitişmemişse»"), tok("بِآخِرِهِ", "akhir", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَآخِرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its end»", "«sonuna»", segments=[seg("بِ", "bi", "prep"), seg("آخِرِ", "akhir", "noun"), pr3msi()]), tok("ضَمِيرٌ", "damir", "noun", [K, FL, BM], "فَاعِلٌ مَرْفُوعٌ.", "«a pronoun»", "«bir zamir»", punct="،")]
def fi_ahwal(): return [tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"), tok("الْأَحْوَالِ", "hal", "noun", [K, HJ, JT], "مَجْرُورٌ بِفِي — جَمْعُ حَالٍ.", "«the states»", "«hâllerde»"), tok("الثَّلَاثِ", "thalatha", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ — الطَّبْعُ: الثلث.", "«three» — the print spells it الثلث.", "«üç» — baskıda الثلث.")]
def jaani(): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")])
def waraaytu(): return tok("وَرَأَيْتُ", "raa", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَرَأَيْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I saw»", "«ve gördüm»", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron")])
def wamarartu(): return tok("وَمَرَرْتُ", "marra", "verb", [K, AT, FL, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمَرَرْتُ فِعْلٌ مَاضٍ مُضَاعَفٌ، وَالتَّاءُ فَاعِلٌ.", "«and I passed»", "«ve uğradım»", segments=[seg("وَ", "wa", "conj"), seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")])
def qawm(punct=None): return tok("الْقَوْمِ", "qawm", "noun", [K, ID, HMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَوَّلُهُ هَمْزَةُ وَصْلٍ سَاكِنٌ مَا بَعْدَهَا.", "«the people» — begins with hamzat al-waṣl.", "«kavmin» — başı vasıl hemzesi.", punct=punct)
def qasim(punct=None): return tok("الْقَاسِمِ", "qasim", "propn", [K, ID, HMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَوَّلُهُ هَمْزَةُ وَصْلٍ.", "«al-Qāsim»", "«Kâsım'ın»", punct=punct)
def ibnika(punct=None): return tok("ابْنِكَ", "ibn", "noun", [K, ID, HMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — أَوَّلُهُ هَمْزَةُ وَصْلٍ.", "«your son» — begins with hamzat al-waṣl.", "«oğlunun» — başı vasıl hemzesi.", punct=punct, segments=[seg("ابْنِ", "ibn", "noun"), seg("كَ", "pron-2ms", "pron")])

# ----------- s1 — the fourth: the yāʾ with kasra before it
S.append({"id": "s1", "translation": {"en": "And the fourth: what has at its end a yāʾ with a kasra before it — even if it is dropped for the meeting of two sukūns. If it is a noun, its rafʿ and its jarr are taqdīrī — as in al-qāḍī and qāḍin; and if it is a verb, its rafʿ alone is taqdīrī, if no pronoun is attached to its end — as in yarmī, tarmī, armī and narmī.", "tr": "Dördüncüsü: sonunda öncesi kesreli bir yâ bulunan — iki sâkinin karşılaşması için hazfedilse de. İsim ise ref'i ve ceri takdîrîdir — el-kâdî ve kâdin gibi; fiil ise sonuna zamir bitişmemişse yalnız ref'i takdîrîdir — yermî, termî, ermî ve nermî gibi."},
 "tokens": [
  tok("وَالرَّابِعُ", "rabi-fourth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالرَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fourth»", "«dördüncüsü»", segments=wa("الرَّابِعُ", "rabi-fourth", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dir»"),
  tok("فِي", "fi", "prep", [K, HJ, MAW, MK], "حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِلَةٌ.", "«at»", "«-de»"),
  tok("آخِرِهِ", "akhir", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonunda»", segments=[seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("يَاءٌ", "ya-letter", "noun", [K, MK, MQ], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a yāʾ»", "«bir yâ»"),
  tok("مَكْسُورٌ", "maksur", "noun", [K, NA, IMF, MK], "نَعْتٌ لِيَاءٌ مَرْفُوعٌ — سَبَبِيٌّ، رَافِعٌ لِمَا بَعْدَهُ.", "«with a kasra on» — a causal description governing what follows.", "«kesreli» — sebebî sıfat, sonrakini ref' eder."),
  tok("مَا", "ma-mawsula", "pron", [K, FL, MAW], "اسْمٌ مَوْصُولٌ فَاعِلُ مَكْسُورٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-i»"),
  tok("قَبْلَهَا", "qabl", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is before it»", "«öncesi»", punct="،", segments=[seg("قَبْلَ", "qabl", "noun"), pr3fs()]),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ لِلْحَالِ، وَإِنْ وَصْلِيَّةٌ.", "«even if»", "«… -se de»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("حُذِفَ", "hadhafa", "verb", [K, INS, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — الْيَاءُ.", "«it is dropped» — the yāʾ.", "«hazfedilse» — yâ."),
  tok("لِالْتِقَاءِ", "iltiqa", "noun", [K, HJ, ID, MSD, F8], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَالْتِقَاءِ مَجْرُورٌ، مُضَافٌ.", "«for the meeting of»", "«karşılaşması için»", segments=[seg("لِ", "li", "prep"), seg("الْتِقَاءِ", "iltiqa", "noun")]),
  tok("السَّاكِنَيْنِ", "sakin", "noun", [K, ID, MTH, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — نَحْوُ قَاضٍ، وَالْقَاضِي الْعَادِلُ.", "«the two sukūns» — as in qāḍin.", "«iki sâkinin» — kâdin gibi.", punct="،"),
  *fain_kana(),
  tok("اسْمًا", "ism", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a noun»", "«isim»"),
  rafuhu(),
  tok("وَجَرُّهُ", "jarr", "noun", [K, AT, MK, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَرُّ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jarr»", "«ve ceri»", segments=[seg("وَ", "wa", "conj"), seg("جَرُّ", "jarr", "noun"), pr3ms()]),
  taqdiri(punct="،", en="«are taqdīrī» — the naṣb shows: قَاضِيًا"),
  nahw(),
  tok("الْقَاضِي", "qadi", "noun", [K, ID, MQ, IRB], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.", "«the judge» — a manqūṣ noun; kasra estimated for heaviness.", "«kâdî» — manqûs isim; ağırlık sebebiyle takdîrî kesre."),
  tok("وَقَاضٍ", "qadi", "noun", [K, AT, MQ, IRB], "الْوَاوُ عَاطِفَةٌ، وَقَاضٍ مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and a judge» — the yāʾ dropped before the tanwīn's sukūn.", "«ve bir kâdî» — yâ tenvinin sükûnu önünde düşmüş.", punct="،", segments=wa("قَاضٍ", "qadi", "noun")),
  *fain_kana(f=False),
  tok("فِعْلًا", "fil", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a verb»", "«fiil»"),
  rafuhu(),
  tok("فَقَطْ", "faqat", "part", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ.", "«alone»", "«yalnız»"),
  taqdiri(),
  *in_lam_yalhaq(),
  nahw(),
  tok("يَرْمِي", "rama", "verb", [K, ID, MR, NQV, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«he throws» — rafʿ estimated on the yāʾ.", "«atar» — yâ'da takdîrî damme."),
  tok("وَتَرْمِي", "rama", "verb", [K, AT, MR, NQV, IRB], "الْوَاوُ عَاطِفَةٌ، وَتَرْمِي مَعْطُوفٌ — مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and you throw»", "«ve atarsın»", segments=wa("تَرْمِي", "rama", "verb")),
  tok("وَأَرْمِي", "rama", "verb", [K, AT, MR, NQV, IRB], "الْوَاوُ عَاطِفَةٌ، وَأَرْمِي مَعْطُوفٌ — مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and I throw»", "«ve atarım»", segments=wa("أَرْمِي", "rama", "verb")),
  tok("وَنَرْمِي", "rama", "verb", [K, AT, MR, NQV, IRB], "الْوَاوُ عَاطِفَةٌ، وَنَرْمِي مَعْطُوفٌ — مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ؛ الْأَرْبَعَةُ الْخَالِيَةُ مِنَ الضَّمِيرِ الْبَارِزِ.", "«and we throw» — the four forms without an apparent pronoun.", "«ve atarız» — bâriz zamirsiz dört şekil.", punct=".", segments=wa("نَرْمِي", "rama", "verb")),
 ]})
# ----------- s2 — the fifth: the verb ending in wāw
S.append({"id": "s2", "translation": {"en": "And the fifth: a verb whose end is a wāw with a ḍamma before it; its rafʿ likewise is alone taqdīrī, if no pronoun is attached to its end — as in yaghzū, taghzū, aghzū and naghzū.", "tr": "Beşincisi: sonu öncesi dammeli bir vâv olan fiil; sonuna zamir bitişmemişse onun da yalnız ref'i takdîrîdir — yağzû, tağzû, ağzû ve nağzû gibi."},
 "tokens": [
  tok("وَالْخَامِسُ", "khamis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَامِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fifth»", "«beşincisi»", segments=wa("الْخَامِسُ", "khamis", "noun")),
  tok("فِعْلٌ", "fil", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«a verb»", "«bir fiil»"),
  tok("آخِرُهُ", "akhir", "noun", [K, NA, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِفِعْلٌ.", "«whose end is»", "«sonu»", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("وَاوٌ", "waw-letter", "noun", [K, MK, NQV], "خَبَرٌ مَرْفُوعٌ.", "«a wāw»", "«bir vâv»"),
  tok("مَضْمُومٌ", "madmum", "noun", [K, NA, IMF, MK], "نَعْتٌ لِوَاوٌ مَرْفُوعٌ — سَبَبِيٌّ.", "«with a ḍamma on» — causal.", "«dammeli» — sebebî."),
  tok("مَا", "ma-mawsula", "pron", [K, FL, MAW], "اسْمٌ مَوْصُولٌ فَاعِلُ مَضْمُومٌ.", "«what»", "«-i»"),
  tok("قَبْلَهَا", "qabl", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is before it»", "«öncesi»", punct="،", segments=[seg("قَبْلَ", "qabl", "noun"), pr3fs()]),
  rafuhu(),
  tok("أَيْضًا", "aydan", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ.", "«likewise»", "«da»"),
  tok("فَقَطْ", "faqat", "part", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ.", "«alone»", "«yalnız»"),
  taqdiri(),
  *in_lam_yalhaq(),
  nahw(),
  tok("يَغْزُو", "ghaza", "verb", [K, ID, MR, NQV, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ.", "«he raids» — rafʿ estimated on the wāw.", "«gazâ eder» — vâv'da takdîrî damme."),
  tok("وَتَغْزُو", "ghaza", "verb", [K, AT, MR, NQV, IRB], "الْوَاوُ عَاطِفَةٌ، وَتَغْزُو مَعْطُوفٌ — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and you raid»", "«ve gazâ edersin»", segments=wa("تَغْزُو", "ghaza", "verb")),
  tok("وَأَغْزُو", "ghaza", "verb", [K, AT, MR, NQV, IRB], "الْوَاوُ عَاطِفَةٌ، وَأَغْزُو مَعْطُوفٌ — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and I raid»", "«ve gazâ ederim»", segments=wa("أَغْزُو", "ghaza", "verb")),
  tok("وَنَغْزُو", "ghaza", "verb", [K, AT, MR, NQV, IRB], "الْوَاوُ عَاطِفَةٌ، وَنَغْزُو مَعْطُوفٌ — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and we raid»", "«ve gazâ ederiz»", punct=".", segments=wa("نَغْزُو", "ghaza", "verb")),
 ]})
# ----------- s3 — the sixth: letter-declined noun before a sukūn — the six nouns
S.append({"id": "s3", "translation": {"en": "And the sixth: a noun declined by letters and meeting a sukūn after it — that is, a word whose beginning is hamzat al-waṣl. If it is one of the six nouns mentioned, its iʿrāb in the three states is taqdīrī — as in «there came to me Abū l-Qāsim», «and I saw Abā l-Qāsim», «and I passed by Abī l-Qāsim»;", "tr": "Altıncısı: harflerle mu'reb olup ardından bir sâkinle karşılaşan isim — yani başı vasıl hemzesi olan bir kelimeyle. Sözü geçen altı isimden ise üç hâlde i'râbı takdîrîdir — «bana Ebu'l-Kâsım geldi», «Ebe'l-Kâsım'ı gördüm», «Ebi'l-Kâsım'a uğradım» gibi;"},
 "tokens": [
  tok("وَالسَّادِسُ", "sadis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّادِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sixth»", "«altıncısı»", segments=wa("السَّادِسُ", "sadis", "noun")),
  tok("اسْمٌ", "ism", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«a noun»", "«bir isim»"),
  tok("أُعْرِبَ", "araba", "verb", [K, NA, NF, F4, IRB], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ.", "«declined» — the describing clause.", "«mu'reb olan» — sıfat cümlesi."),
  tok("بِالْحُرُوفِ", "harf", "noun", [K, HJ, JT, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحُرُوفِ مَجْرُورٌ.", "«by letters»", "«harflerle»", segments=[seg("بِ", "bi", "prep"), seg("الْحُرُوفِ", "harf", "noun")]),
  tok("وَمُلَاقٍ", "mulaqi", "noun", [K, AT, NA, IFA, MQ], "الْوَاوُ عَاطِفَةٌ، وَمُلَاقٍ نَعْتٌ ثَانٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمٌ مَنْقُوصٌ.", "«and meeting» — a manqūṣ participle.", "«ve karşılaşan» — manqûs ism-i fâil.", segments=wa("مُلَاقٍ", "mulaqi", "noun")),
  tok("لِسَاكِنٍ", "sakin", "noun", [K, HJ, IFA], "اللَّامُ حَرْفُ جَرٍّ، وَسَاكِنٍ مَجْرُورٌ — مَفْعُولُ مُلَاقٍ بِوَاسِطَةِ اللَّامِ.", "«a sukūn» — the participle's object through the lām.", "«bir sâkinle» — lâm vasıtasıyla ism-i fâilin mef'ûlü.", segments=[seg("لِ", "li", "prep"), seg("سَاكِنٍ", "sakin", "noun")]),
  tok("بَعْدَهُ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«after it»", "«ardından»"),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»"),
  tok("كَلِمَةٍ", "kalima", "noun", [K, HT, HJ], "بَدَلٌ مِنْ سَاكِنٍ مَجْرُورٌ — أَيْ لِكَلِمَةٍ.", "«a word» — in apposition to «a sukūn».", "«bir kelime» — sâkin'den bedel."),
  tok("أَوَّلُهَا", "awwal", "noun", [K, NA, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِكَلِمَةٍ.", "«whose beginning is»", "«başı»", segments=[seg("أَوَّلُ", "awwal", "noun"), pr3fs()]),
  tok("هَمْزَةُ", "hamza-letter", "noun", [K, MK, ID, HMZ], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the hamza of»", "«hemzesi»"),
  tok("وَصْلٍ", "wasl", "noun", [K, ID, MSD, HMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَسْقُطُ فِي الدَّرْجِ فَيَلْتَقِي السَّاكِنَانِ.", "«joining» — it drops in connected speech, so two sukūns meet.", "«vasıl» — vasılda düşer, iki sâkin karşılaşır.", punct="،"),
  *fain_kana(),
  tok("مِنَ", "min", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«one of»", "«-den»"),
  tok("الْأَسْمَاءِ", "ism", "noun", [K, HJ, JT, FN], "مَجْرُورٌ بِمِنْ.", "«the nouns»", "«isimlerden»"),
  tok("السِّتَّةِ", "sitta", "noun", [K, NA, FN], "نَعْتٌ مَجْرُورٌ.", "«six»", "«altı»"),
  tok("الْمَذْكُورَةِ", "madhkur", "noun", [K, NA, IMF], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«mentioned»", "«sözü geçen»"),
  tok("فَإِعْرَابُهُ", "irab", "noun", [K, INS, MK, ID, MSD, IRB], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَإِعْرَابُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its iʿrāb»", "«i'râbı»", segments=[seg("فَ", "fa", "conj"), seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  *fi_ahwal(),
  taqdiri(punct="،"),
  nahw(punct=":"),
  jaani(),
  tok("أَبُو", "ab", "noun", [K, FL, FN, ID, IRB], "فَاعِلٌ مَرْفُوعٌ بِوَاوٍ مُقَدَّرَةٍ — الْوَاوُ تَسْقُطُ لَفْظًا لِالْتِقَاءِ السَّاكِنَيْنِ، مُضَافٌ.", "«Abū» — the wāw estimated; it drops in speech before the sukūn.", "«Ebû» — vâv takdîrî; sâkin önünde lafzen düşer."),
  qasim(punct="،"),
  waraaytu(),
  tok("أَبَا", "ab", "noun", [K, MB, FN, ID, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِأَلِفٍ مُقَدَّرَةٍ، مُضَافٌ.", "«Abā» — the alif estimated.", "«Ebâ» — elif takdîrî."),
  qasim(punct="،"),
  wamarartu(),
  tok("بِأَبِي", "ab", "noun", [K, HJ, FN, ID, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَأَبِي مَجْرُورٌ بِيَاءٍ مُقَدَّرَةٍ، مُضَافٌ.", "«by Abī» — the yāʾ estimated.", "«Ebî'ye» — yâ takdîrî.", segments=[seg("بِ", "bi", "prep"), seg("أَبِي", "ab", "noun")]),
  qasim(punct="،"),
 ]})
# ----------- s4 — the sound masculine plural before the sukūn
S.append({"id": "s4", "translation": {"en": "and if it is the sound masculine plural, then if what precedes the letter of iʿrāb is vowelled with fatḥa — as in muṣṭafawna and muṣṭafayna — the wāw is vowelled with ḍamma and the yāʾ with kasra, so it is lafẓī in the three states — as in «there came to me the chosen of the people», «and I saw the chosen of the people», «and I passed by the chosen of the people»; and if it is not vowelled with fatḥa, the two are dropped, so it is taqdīrī in the three states — as in «there came to me the strikers of the people», «and I saw the strikers of the people», «and I passed by the strikers of the people»;", "tr": "cem'-i müzekker-i sâlim ise: i'râb harfinden önceki fethalı ise — mustafevne ve mustafeyne gibi — vâv damme ile, yâ kesre ile harekelenir, böylece üç hâlde lafzîdir — «bana kavmin seçkinleri geldi», «kavmin seçkinlerini gördüm», «kavmin seçkinlerine uğradım» gibi; fethalı değilse ikisi hazfedilir, böylece üç hâlde takdîrîdir — «bana kavmi dövenler geldi», «kavmi dövenleri gördüm», «kavmi dövenlere uğradım» gibi;"},
 "tokens": [
  *fain_kana(f=False),
  tok("جَمْعَ", "jam", "noun", [K, KN, ID, JDS], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«the plural of»", "«cem'-i»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, IMF, F2, JDS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekker»"),
  tok("السَّالِمَ", "salim", "noun", [K, NA, IFA, JDS], "نَعْتٌ لِجَمْعَ مَنْصُوبٌ.", "«sound»", "«sâlim»"),
  *fain_kana(),
  tok("مَا", "ma-mawsula", "pron", [K, KN, MAW], "اسْمٌ مَوْصُولٌ اسْمُ كَانَ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-i»"),
  tok("قَبْلَ", "qabl", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — صِلَةُ مَا.", "«precedes»", "«önceki»"),
  tok("حَرْفِ", "harf", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the letter of»", "«harfinden»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râb»"),
  tok("مَفْتُوحًا", "maftuh", "noun", [K, KN, IMF], "خَبَرُ كَانَ مَنْصُوبٌ.", "«vowelled with fatḥa»", "«fethalı»"),
  nahw(),
  tok("مُصْطَفَوْنَ", "mustafa", "noun", [K, ID, JDS, IMF, F8, MQ], "لَفْظٌ مَحْكِيٌّ: جَمْعُ مُصْطَفًى — أَلِفُ الْمَقْصُورِ حُذِفَتْ وَبَقِيَتِ الْفَتْحَةُ قَبْلَ الْوَاوِ.", "«muṣṭafawna» — the maqṣūr's alif dropped, its fatḥa kept before the wāw.", "«mustafevne» — maksûrun elifi düşmüş, fethası vâv önünde kalmış."),
  tok("وَمُصْطَفَيْنَ", "mustafa", "noun", [K, AT, JDS, IMF, F8, MQ], "الْوَاوُ عَاطِفَةٌ، وَمُصْطَفَيْنَ مَعْطُوفٌ — الْفَتْحَةُ قَبْلَ الْيَاءِ.", "«and muṣṭafayna» — the fatḥa before the yāʾ.", "«ve mustafeyne» — yâ önünde fetha.", punct="،", segments=wa("مُصْطَفَيْنَ", "mustafa", "noun")),
  tok("فَتَحَرَّكَ", "taharraka", "verb", [K, INS, F5], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَتَحَرَّكَ فِعْلٌ مَاضٍ.", "«then … is vowelled»", "«harekelenir»", segments=fa("تَحَرَّكَ", "taharraka", "verb")),
  tok("الْوَاوُ", "waw-letter", "noun", [K, FL, JDS], "فَاعِلٌ مَرْفُوعٌ.", "«the wāw»", "«vâv»"),
  tok("بِالضَّمَّةِ", "damma", "noun", [K, HJ, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالضَّمَّةِ مَجْرُورٌ.", "«with ḍamma»", "«damme ile»", segments=[seg("بِ", "bi", "prep"), seg("الضَّمَّةِ", "damma", "noun")]),
  tok("وَالْيَاءُ", "ya-letter", "noun", [K, AT, FL, JDS], "الْوَاوُ عَاطِفَةٌ، وَالْيَاءُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the yāʾ»", "«ve yâ»", segments=wa("الْيَاءُ", "ya-letter", "noun")),
  tok("بِالْكَسْرَةِ", "kasra", "noun", [K, HJ, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْكَسْرَةِ مَجْرُورٌ — لِالْتِقَاءِ السَّاكِنَيْنِ.", "«with kasra» — for the two sukūns.", "«kesre ile» — iki sâkin için.", segments=[seg("بِ", "bi", "prep"), seg("الْكَسْرَةِ", "kasra", "noun")]),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَكُونُ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: الْإِعْرَابُ.", "«so it is»", "«böylece … olur»", segments=fa("يَكُونُ", "kana", "verb")),
  tok("لَفْظِيًّا", "lafzi", "noun", [K, KN, NSB, IRB], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«lafẓī»", "«lafzî»"),
  *fi_ahwal(),
  nahw(punct=":"),
  jaani(),
  tok("مُصْطَفُو", "mustafa", "noun", [K, FL, JDS, ID, IMF, IRB], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ الْمُحَرَّكَةِ بِالضَّمَّةِ، مُضَافٌ — النُّونُ حُذِفَتْ لِلْإِضَافَةِ.", "«the chosen of» — rafʿ by the wāw, now vowelled with ḍamma.", "«seçkinleri» — damme ile harekelenmiş vâv ile merfû."),
  qawm(punct="،"),
  waraaytu(),
  tok("مُصْطَفَيِ", "mustafa", "noun", [K, MB, JDS, ID, IMF, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ الْمُحَرَّكَةِ بِالْكَسْرَةِ، مُضَافٌ.", "«the chosen of» — naṣb by the yāʾ, vowelled with kasra.", "«seçkinlerini» — kesre ile harekelenmiş yâ ile mansûb."),
  qawm(punct="،"),
  wamarartu(),
  tok("بِمُصْطَفَيِ", "mustafa", "noun", [K, HJ, JDS, ID, IMF, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَمُصْطَفَيِ مَجْرُورٌ بِالْيَاءِ الْمُحَرَّكَةِ بِالْكَسْرَةِ، مُضَافٌ.", "«by the chosen of»", "«seçkinlerine»", segments=[seg("بِ", "bi", "prep"), seg("مُصْطَفَيِ", "mustafa", "noun")]),
  qawm(punct="،"),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-değilse»"),
  tok("يَكُنْ", "kana", "verb", [K, INS, LJ, JZ, KN, HV], "فِعْلُ الشَّرْطِ، مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»"),
  tok("مَفْتُوحًا", "maftuh", "noun", [K, KN, IMF], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«vowelled with fatḥa»", "«fethalı»"),
  tok("يُحْذَفَانِ", "hadhafa", "verb", [K, INS, NF, MR, MTH], "جَوَابُ الشَّرْطِ: مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ — الْوَاوُ وَالْيَاءُ.", "«the two are dropped» — the wāw and the yāʾ.", "«ikisi hazfedilir» — vâv ve yâ.", segments=[seg("يُحْذَفَ", "hadhafa", "verb"), seg("ا", "pron-3d", "pron"), seg("نِ", "nun-letter", "part")]),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَكُونُ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«so it is»", "«böylece … olur»", segments=fa("يَكُونُ", "kana", "verb")),
  tok("تَقْدِيرِيًّا", "taqdiri", "noun", [K, KN, NSB, IRB], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«taqdīrī»", "«takdîrî»"),
  *fi_ahwal(),
  nahw(punct=":"),
  jaani(),
  tok("ضَارِبُو", "darib", "noun", [K, FL, JDS, ID, IFA, IRB], "فَاعِلٌ مَرْفُوعٌ بِوَاوٍ مُقَدَّرَةٍ حُذِفَتْ لَفْظًا لِالْتِقَاءِ السَّاكِنَيْنِ، مُضَافٌ.", "«the strikers of» — the wāw estimated, dropped in speech.", "«dövenleri» — vâv takdîrî, lafzen düşmüş."),
  qawm(punct="،"),
  waraaytu(),
  tok("ضَارِبِي", "darib", "noun", [K, MB, JDS, ID, IFA, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِيَاءٍ مُقَدَّرَةٍ حُذِفَتْ لَفْظًا، مُضَافٌ.", "«the strikers of» — the yāʾ estimated.", "«dövenleri» — yâ takdîrî."),
  qawm(punct="،"),
  wamarartu(),
  tok("بِضَارِبِي", "darib", "noun", [K, HJ, JDS, ID, IFA, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَضَارِبِي مَجْرُورٌ بِيَاءٍ مُقَدَّرَةٍ، مُضَافٌ.", "«by the strikers of»", "«dövenlere»", segments=[seg("بِ", "bi", "prep"), seg("ضَارِبِي", "darib", "noun")]),
  qawm(punct="،"),
 ]})
# ----------- s5 — the dual before the sukūn
S.append({"id": "s5", "translation": {"en": "and if it is a dual, its rafʿ is taqdīrī, while in its naṣb and jarr the yāʾ is vowelled with kasra, so it is lafẓī — as in «there came to me the two servants of your son», «and I saw the two servants of your son», «and I passed by the two servants of your son».", "tr": "tesniye ise ref'i takdîrîdir, nasb ve cerinde ise yâ kesre ile harekelenir, böylece lafzîdir — «bana oğlunun iki kölesi geldi», «oğlunun iki kölesini gördüm», «oğlunun iki kölesine uğradım» gibi."},
 "tokens": [
  *fain_kana(f=False),
  tok("تَثْنِيَةً", "tathniya", "noun", [K, KN, MSD, F2, MTH], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a dual»", "«tesniye»"),
  rafuhu(),
  taqdiri(),
  tok("وَفِي", "fi", "prep", [K, AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«while in»", "«… -inde ise»", segments=wa("فِي", "fi", "prep")),
  tok("نَصْبِهِ", "nasb", "noun", [K, HJ, ID, MSD, IRB], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its naṣb»", "«nasbında»", segments=[seg("نَصْبِ", "nasb", "noun"), pr3msi()]),
  tok("وَجَرِّهِ", "jarr", "noun", [K, AT, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَرِّ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jarr»", "«ve cerinde»", segments=[seg("وَ", "wa", "conj"), seg("جَرِّ", "jarr", "noun"), pr3msi()]),
  tok("تَحَرُّكُ", "taharruk", "noun", [K, MK, ID, MSD, F5], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the vowelling of»", "«harekelenmesi»"),
  tok("الْيَاءِ", "ya-letter", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the yāʾ»", "«yânın»"),
  tok("بِالْكَسْرَةِ", "kasra", "noun", [K, HJ, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْكَسْرَةِ مَجْرُورٌ.", "«with kasra»", "«kesre ile»", segments=[seg("بِ", "bi", "prep"), seg("الْكَسْرَةِ", "kasra", "noun")]),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَكُونُ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«so it is»", "«böylece … olur»", segments=fa("يَكُونُ", "kana", "verb")),
  tok("لَفْظِيًّا", "lafzi", "noun", [K, KN, NSB, IRB], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«lafẓī»", "«lafzî»", punct="،"),
  nahw(punct=":"),
  jaani(),
  tok("غُلَامَا", "ghulam", "noun", [K, FL, MTH, ID, IRB], "فَاعِلٌ مَرْفُوعٌ بِأَلِفٍ مُقَدَّرَةٍ حُذِفَتْ لَفْظًا لِالْتِقَاءِ السَّاكِنَيْنِ، مُضَافٌ.", "«the two servants of» — the alif estimated, dropped in speech.", "«iki kölesi» — elif takdîrî, lafzen düşmüş."),
  ibnika(punct="،"),
  waraaytu(),
  tok("غُلَامَيِ", "ghulam", "noun", [K, MB, MTH, ID, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ الْمُحَرَّكَةِ بِالْكَسْرَةِ، مُضَافٌ.", "«the two servants of» — the yāʾ vowelled with kasra.", "«iki kölesini» — kesreli yâ ile mansûb."),
  ibnika(punct="،"),
  wamarartu(),
  tok("بِغُلَامَيِ", "ghulam", "noun", [K, HJ, MTH, ID, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَغُلَامَيِ مَجْرُورٌ بِالْيَاءِ الْمُحَرَّكَةِ بِالْكَسْرَةِ، مُضَافٌ.", "«by the two servants of»", "«iki kölesine»", segments=[seg("بِ", "bi", "prep"), seg("غُلَامَيِ", "ghulam", "noun")]),
  ibnika(punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "hamza-letter": G("hamza-letter", "هَمْزَة", "ه م ز", "noun", "the hamza (glottal stop); hamzat al-waṣl, the joining hamza that drops in connected speech", "hemze; hemze-i vasıl, vasılda düşen hemze", 3),
 "mustafa": G("mustafa", "مُصْطَفًى", "ص ف و", "noun", "chosen, elect (passive participle of iṣṭafā, form VIII); plural muṣṭafawna", "seçkin, mustafâ (ıstafâ'nın ism-i mef'ûlü, VIII. bab); çoğulu mustafevne", 4),
 "taharruk": G("taharruk", "تَحَرُّك", "ح ر ك", "noun", "being vowelled, taking a vowel — the maṣdar of taḥarraka", "harekelenme — teharrake'nin mastarı", 3),
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
print("izhar ch59 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("hadhafa", "kana", "lahiqa", "rama", "ghaza", "araba", "taharraka", "jaa", "raa", "marra") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "التَّقْدِيرِيُّ فِي الْمَنْقُوصِ وَالْفِعْلِ الْيَائِيِّ وَالْوَاوِيِّ، وَفِي الْمُعْرَبِ بِالْحُرُوفِ قَبْلَ هَمْزَةِ الْوَصْلِ: الْأَسْمَاءُ السِّتَّةُ، وَجَمْعُ الْمُذَكَّرِ، وَالتَّثْنِيَةُ", "en": "The taqdīrī in the manqūṣ noun, the yāʾ- and wāw-ending verbs, and in the letter-declined noun before hamzat al-waṣl: the six nouns, the sound masculine plural, the dual", "tr": "Manqûs isimde, yâlı ve vâvlı fiillerde ve vasıl hemzesi önünde harfle mu'reb isimde takdîrî: altı isim, cem'-i müzekker, tesniye"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الإعراب التقديري: المواضع الرابع إلى السادس", "الكافية لابن الحاجب — المنقوص والمعتل", "شرح قطر الندى لابن هشام — التقاء الساكنين"],
 "amil": "the fourth taqdīrī position: the word ending in yāʾ with kasra before it — the noun estimated in rafʿ and jarr (الْقَاضِي، قَاضٍ), the verb in rafʿ only without a pronoun (يَرْمِي …); the fifth: the verb ending in wāw with ḍamma before it, rafʿ only (يَغْزُو …); the sixth: the letter-declined noun before a hamzat al-waṣl word — the six nouns estimated throughout (أَبُو الْقَاسِمِ …), the sound masculine plural lafẓī when a fatḥa precedes the letter (مُصْطَفُو الْقَوْمِ …) and taqdīrī otherwise (ضَارِبُو الْقَوْمِ …), the dual estimated in rafʿ and lafẓī in naṣb and jarr (غُلَامَا ابْنِكَ، غُلَامَيِ ابْنِكَ).",
 "question": {
  "en": ["Why are the manqūṣ noun's rafʿ and jarr estimated but not its naṣb? The ḍamma and kasra are heavy on the yāʾ and are left off (الْقَاضِي), while the fatḥa is light and shows: الْقَاضِيَ.",
         "What happens in قَاضٍ? The yāʾ drops for the meeting of two sukūns — its own and the tanwīn's — and the estimated case rides on the dropped yāʾ.",
         "Why is the yāʾ-ending verb estimated in rafʿ only? Its naṣb shows the fatḥa (لَنْ يَرْمِيَ) and its jazm drops the yāʾ (لَمْ يَرْمِ); only the ḍamma of rafʿ is unspoken — and only in the four forms with no apparent pronoun (يَرْمِي، تَرْمِي، أَرْمِي، نَرْمِي).",
         "And the wāw-ending verb? The same: rafʿ alone estimated in يَغْزُو، تَغْزُو، أَغْزُو، نَغْزُو; naṣb shows (لَنْ يَغْزُوَ), jazm drops the wāw (لَمْ يَغْزُ).",
         "What is the sixth position? A noun declined by letters that meets a sukūn after it — a following word beginning with hamzat al-waṣl, which drops in connected speech so that two sukūns meet.",
         "How do the six nouns behave there? Their wāw, alif and yāʾ drop in speech, so all three states are estimated: أَبُو الْقَاسِمِ، أَبَا الْقَاسِمِ، بِأَبِي الْقَاسِمِ.",
         "Why does مُصْطَفُو الْقَوْمِ differ from ضَارِبُو الْقَوْمِ? Where a fatḥa precedes the letter of iʿrāb (مُصْطَفَوْنَ), the wāw takes ḍamma and the yāʾ kasra instead of dropping, so the iʿrāb stays lafẓī; where there is no fatḥa (ضَارِبُونَ), the letters drop and all three states are estimated.",
         "And the dual? Its rafʿ alif drops before the sukūn (غُلَامَا ابْنِكَ: rafʿ estimated); its naṣb and jarr yāʾ takes kasra instead (غُلَامَيِ ابْنِكَ: lafẓī).",
         "What does the engine READ here? The DabtEngine reads الْقَاضِي and قَاضٍ with estimated case, the four يَرْمِي and يَغْزُو forms as rafʿ by an implied ḍamma, أَبُو/أَبَا/أَبِي before الْقَاسِمِ by estimated letters, مُصْطَفُو/مُصْطَفَيِ by vowelled letters, ضَارِبُو/ضَارِبِي by estimated ones, and غُلَامَا/غُلَامَيِ before ابْنِكَ as the dual's rafʿ and naṣb/jarr."],
  "tr": ["Manqûs ismin ref' ve ceri neden takdîrî, nasbı değil? Damme ve kesre yâ üzerinde ağırdır ve bırakılır (el-kâdî); fetha hafiftir ve görünür: el-kâdiye.",
         "Kâdin'de ne olur? Yâ iki sâkinin — kendisinin ve tenvinin — karşılaşması için düşer; takdîrî i'râb düşen yâ üzerindedir.",
         "Sonu yâlı fiil neden yalnız ref'te takdîrîdir? Nasbı fethayı gösterir (len yermiye), cezmi yâ'yı düşürür (lem yermi); yalnız ref' dammesi söylenmez — ve yalnız bâriz zamirsiz dört şekilde (yermî, termî, ermî, nermî).",
         "Sonu vâvlı fiil? Aynı: yağzû, tağzû, ağzû, nağzû'da yalnız ref' takdîrî; nasb görünür (len yağzüve), cezm vâvı düşürür (lem yağzü).",
         "Altıncı mevzi nedir? Harflerle mu'reb olup ardından sâkinle karşılaşan isim — vasıl hemzesiyle başlayan ve hemzesi vasılda düşüp iki sâkinin karşılaştığı bir kelime.",
         "Altı isim orada nasıl davranır? Vâv, elif ve yâları lafzen düşer, üç hâl de takdîrîdir: Ebu'l-Kâsım, Ebe'l-Kâsım, bi-Ebi'l-Kâsım.",
         "Mustafu'l-kavm, dâribu'l-kavm'den neden farklıdır? İ'râb harfinden önce fetha varsa (mustafevne) vâv damme, yâ kesre alır, düşmez; i'râb lafzî kalır; fetha yoksa (dâribûne) harfler düşer ve üç hâl takdîrîdir.",
         "Tesniye? Ref' elifi sâkin önünde düşer (gulâme'bnike: ref' takdîrî); nasb ve cer yâsı kesre alır (gulâmeyi'bnike: lafzî).",
         "Motor burada neyi OKUR? DabtEngine el-kâdî ve kâdin'i takdîrî i'râbla, dört yermî ve yağzû şeklini takdîrî damme ile merfû, Ebû/Ebâ/Ebî'yi el-Kâsım önünde takdîrî harflerle, mustafû/mustafeyi'yi harekeli harflerle, dâribû/dâribî'yi takdîrî harflerle, gulâmâ/gulâmeyi'yi ibnike önünde tesniyenin ref' ve nasb/ceri olarak okur."],
 },
 "plain": {"en": "More endings that hide their case: a noun in -ī like al-qāḍī (only its naṣb shows), verbs in -ī or -ū like yarmī and yaghzū (only their rafʿ hides), and letter-declined nouns before a word opening with a silent hamza: abū l-Qāsim loses its wāw in speech, ḍāribū l-qawm loses its letters, muṣṭafū l-qawm keeps them.",
           "tr": "İ'râbını gizleyen başka sonlar: el-kâdî gibi -î'li isim (yalnız nasbı görünür), yermî ve yağzû gibi -î ya da -û'lu fiiller (yalnız ref'i gizlenir) ve sessiz hemzeyle başlayan sözcük önündeki harfle mu'reb isimler: ebu'l-Kâsım konuşmada vâvını yitirir, dâribu'l-kavm harflerini yitirir, mustafu'l-kavm korur."},
 "explanation": {"en": "The fourth taqdīrī position is what has at its end a yāʾ with kasra before it, even if dropped for the meeting of two sukūns: a noun is estimated in rafʿ and jarr — الْقَاضِي، قَاضٍ; a verb in rafʿ only, when no pronoun is attached to its end — يَرْمِي، تَرْمِي، أَرْمِي، نَرْمِي. The fifth is a verb whose end is a wāw with ḍamma before it: its rafʿ likewise is alone estimated without a pronoun — يَغْزُو، تَغْزُو، أَغْزُو، نَغْزُو. The sixth is a noun declined by letters that meets a sukūn after it, that is, a word beginning with hamzat al-waṣl. If it is one of the six nouns, its iʿrāb in the three states is taqdīrī — جَاءَنِي أَبُو الْقَاسِمِ، رَأَيْتُ أَبَا الْقَاسِمِ، مَرَرْتُ بِأَبِي الْقَاسِمِ. If it is the sound masculine plural, then where what precedes the letter of iʿrāb is vowelled with fatḥa — مُصْطَفَوْنَ، مُصْطَفَيْنَ — the wāw takes ḍamma and the yāʾ kasra, and the iʿrāb is lafẓī in the three states — جَاءَنِي مُصْطَفُو الْقَوْمِ، رَأَيْتُ مُصْطَفَيِ الْقَوْمِ، مَرَرْتُ بِمُصْطَفَيِ الْقَوْمِ; where it is not, the two letters drop and the iʿrāb is taqdīrī throughout — ضَارِبُو الْقَوْمِ، ضَارِبِي الْقَوْمِ، بِضَارِبِي الْقَوْمِ. If it is a dual, its rafʿ is taqdīrī, while in naṣb and jarr the yāʾ takes kasra and the iʿrāb is lafẓī — غُلَامَا ابْنِكَ، غُلَامَيِ ابْنِكَ، بِغُلَامَيِ ابْنِكَ. The seventh position and the maḥallī follow. The lithograph spells الثلث in the old orthography.",
                 "tr": "Takdîrînin dördüncü mevzii sonunda öncesi kesreli yâ bulunan, iki sâkinin karşılaşması için düşse de: isim ref' ve cerde takdîrîdir — el-kâdî, kâdin; fiil, sonuna zamir bitişmemişse yalnız ref'te — yermî, termî, ermî, nermî. Beşincisi sonu öncesi dammeli vâv olan fiildir: zamirsiz onun da yalnız ref'i takdîrîdir — yağzû, tağzû, ağzû, nağzû. Altıncısı harflerle mu'reb olup ardından sâkinle karşılaşan isimdir, yani vasıl hemzesiyle başlayan bir kelimeyle. Altı isimden ise üç hâlde i'râbı takdîrîdir — câenî Ebu'l-Kâsım, raeytü Ebe'l-Kâsım, merartü bi-Ebi'l-Kâsım. Cem'-i müzekker-i sâlim ise: i'râb harfinden önceki fethalıysa — mustafevne, mustafeyne — vâv damme, yâ kesre alır ve i'râb üç hâlde lafzîdir — câenî mustafu'l-kavm, raeytü mustafeyi'l-kavm, merartü bi-mustafeyi'l-kavm; değilse iki harf düşer ve i'râb üç hâlde takdîrîdir — dâribu'l-kavm, dâribi'l-kavm, bi-dâribi'l-kavm. Tesniye ise ref'i takdîrî, nasb ve cerde yâ kesre alır ve i'râb lafzîdir — gulâme'bnike, gulâmeyi'bnike, bi-gulâmeyi'bnike. Yedinci mevzi ve mahallî gelir. Litografi الثلث'i eski imlâ ile yazar."},
 "examples": [
  {"ar": "نَحْوُ الْقَاضِي وَقَاضٍ", "en": "the manqūṣ noun: rafʿ and jarr estimated", "tr": "manqûs isim: ref' ve cer takdîrî", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "نَحْوُ يَرْمِي وَتَرْمِي وَأَرْمِي وَنَرْمِي", "en": "the yāʾ-ending verb: rafʿ only", "tr": "sonu yâlı fiil: yalnız ref'", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "نَحْوُ يَغْزُو وَتَغْزُو وَأَغْزُو وَنَغْزُو", "en": "the wāw-ending verb: rafʿ only", "tr": "sonu vâvlı fiil: yalnız ref'", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "جَاءَنِي أَبُو الْقَاسِمِ، وَرَأَيْتُ أَبَا الْقَاسِمِ، وَمَرَرْتُ بِأَبِي الْقَاسِمِ", "en": "the six nouns before hamzat al-waṣl", "tr": "vasıl hemzesi önünde altı isim", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "مُصْطَفُو الْقَوْمِ … ضَارِبُو الْقَوْمِ", "en": "the sound plural: vowelled letters against dropped ones", "tr": "sâlim cemi: harekeli harflere karşı düşen harfler", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "غُلَامَا ابْنِكَ، وَرَأَيْتُ غُلَامَيِ ابْنِكَ", "en": "the dual before hamzat al-waṣl", "tr": "vasıl hemzesi önünde tesniye", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي الْقَاضِيُ", "right": "جَاءَنِي الْقَاضِي", "why": {"en": "the manqūṣ noun's ḍamma is estimated, never written", "tr": "manqûs ismin dammesi takdîrîdir, yazılmaz"}},
  {"wrong": "رَأَيْتُ الْقَاضِي (with the fatḥa hidden)", "right": "رَأَيْتُ الْقَاضِيَ", "why": {"en": "the naṣb of the manqūṣ shows its fatḥa", "tr": "manqûsun nasbı fethasını gösterir"}},
  {"wrong": "رَأَيْتُ مُصْطَفَيْ الْقَوْمِ", "right": "رَأَيْتُ مُصْطَفَيِ الْقَوْمِ", "why": {"en": "before hamzat al-waṣl the yāʾ after a fatḥa takes kasra rather than dropping", "tr": "vasıl hemzesi önünde fethadan sonraki yâ düşmek yerine kesre alır"}},
  {"wrong": "جَاءَنِي غُلَامَيِ ابْنِكَ", "right": "جَاءَنِي غُلَامَا ابْنِكَ", "why": {"en": "the dual's rafʿ is by the alif, estimated before the sukūn; the yāʾ is for naṣb and jarr", "tr": "tesniyenin ref'i elifledir, sâkin önünde takdîrî; yâ nasb ve cer içindir"}},
 ],
}
ADD_EN = (" Chapter 59 (print pp. 153-155): the fourth taqdīrī position — the yāʾ-ending noun and verb (s1); the fifth — the wāw-ending verb (s2); the sixth — the letter-declined noun before hamzat al-waṣl: the six nouns (s3), the sound masculine plural with and without the fatḥa (s4), the dual (s5).")
ADD_TR = (" Elli dokuzuncu bab (baskı s. 153-155): takdîrînin dördüncü mevzii — sonu yâlı isim ve fiil (s1); beşincisi — sonu vâvlı fiil (s2); altıncısı — vasıl hemzesi önünde harfle mu'reb isim: altı isim (s3), fethalı ve fethasız cem'-i müzekker-i sâlim (s4), tesniye (s5).")
write_out(59, S, TITLE, ADD_EN, ADD_TR, "pp. 153-155", GLOSS_ADD, notes=(NOTE,),
          related=((K58, [K]), (MQ, [K]), (NQV, [K]), (FN, [K]), (JDS, [K]), (MTH, [K])))
report(59, S, GLOSS_ADD, (NOTE,))
