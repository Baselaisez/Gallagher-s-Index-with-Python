# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 60: the taqdīrī's SEVENTH position — the word paused upon with sukūn, of those declined by vowel: with no tanwīn of
# tamakkun, or with the feminine tāʾ at its end, all three states estimated (أَحْمَدْ، ضَارِبَهْ، ضَارِبَاتْ); with that tanwīn and no tāʾ, rafʿ and jarr estimated
# but not naṣb (زَيْدْ — رَأَيْتُ زَيْدَا shows). The MAḤALLĪ in two places: the declined noun whose end is busy with a non-cited iʿrāb (مَرَرْتُ بِزَيْدٍ — Zayd's
# position is naṣb as object; أَعْجَبَنِي ضَرْبُ زَيْدٍ and مُرَّ بِزَيْدٍ — rafʿ as doer and as deputy); and the mabnī: what has its vowel and sukūn by no governor,
# unlike the muʿrab, which has them by a governor. The mabnī is of two kinds — by origin and by accident; the first four: the particle, the māḍī, the
# lām-less command (the Baṣrans) and the sentence; the second lāzim and non-lāzim. Print pp. 155–156.
# Readings: the lithograph's «ومررت بزيد» in the deputy-doer example is read مُرَّ بِزَيْدٍ with the Ottoman commentary (izhar-full-corrected l. 1866:
# «Zayd, busy with the kasra, is rafʿ by position as the deputy doer»), since a deputy doer wants a passive; the lithograph's «والجامد» as the fourth
# mabnī al-aṣl is read الْجُمْلَةُ with the commentary (l. 1870) and the Turkish question-book (izhar-sual-cevap-tafsilatli l. 1298: «4- Cümle») — both
# departures are flagged in the explanation.
#   python3 author_izhar_ch60.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; JMS = "jam-muannath-salim"; MN = "al-muannath-wa-alamatuh"; TQ = "taqsim"; MJ = "mawadi-irab-al-jumla"; HK = "hikayat-al-hal"; AMR = "imperative-amr"; WQF = "hadhf-wa-taqdir"
K = "al-taqdiri-al-sabi-wal-mahalli-wal-mabni-wa-aqsamuh"
K59 = "al-taqdiri-al-rabi-ila-al-sadis-al-ya-wal-waw-wal-murab-bil-huruf-qabl-al-sakin"
TITLE = {"ar": "الْمَوْضِعُ السَّابِعُ لِلتَّقْدِيرِيِّ: الْمَوْقُوفُ عَلَيْهِ، وَالْإِعْرَابُ الْمَحَلِّيُّ فِي مَوْضِعَيْهِ، وَتَعْرِيفُ الْمَبْنِيِّ وَأَقْسَامُهُ", "en": "The seventh position of the taqdīrī: the paused word; the maḥallī in its two places; the mabnī defined and divided", "tr": "Takdîrînin yedinci mevzii: üzerinde durulan kelime; iki mevziinde mahallî i'râb; mebnînin tarifi ve kısımları"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def taqdiri(punct=None, en="«is taqdīrī»"): return tok("تَقْدِيرِيٌّ", "taqdiri", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", en, "«takdîrîdir»", punct=punct)
def kana_in(w=False): return [tok("وَإِنْ" if w else "فَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], ("الْوَاوُ عَاطِفَةٌ" if w else "الْفَاءُ لِلتَّفْرِيعِ") + "، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»" if w else "«so if»", "«ve eğer»" if w else "«eğer»", segments=(wa if w else fa)("إِنْ", "in-shartiyya", "part")), tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»")]
def zayd_jarr(form="بِزَيْدٍ", punct=None, ar=None, en="«by Zayd»", tr="«Zeyd'e»"): return tok(form, "zayd", "propn", [K, HJ, IRB], ar or "الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ لَفْظًا.", en, tr, punct=punct, segments=[seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")])

# ----------- s1 — the seventh: the paused word
S.append({"id": "s1", "translation": {"en": "And the seventh: the word paused upon with sukūn, of those whose iʿrāb is by vowel. If it has no tanwīn of tamakkun, or has the feminine tāʾ at its end, its three states are taqdīrī — as in Aḥmad, ḍāribah and ḍāribāt; and if it has tanwīn without the tāʾ, its rafʿ and its jarr are taqdīrī, not its naṣb — as in Zayd.", "tr": "Yedincisi: i'râbı hareke ile olanlardan, üzerinde sükûn ile durulan kelime. Temekkün tenvini almıyorsa ya da sonunda te'nis tâsı varsa üç hâli takdîrîdir — Ahmed, dâribeh ve dâribât gibi; tâ'sız olarak tenvinli ise ref'i ve ceri takdîrî, nasbı değil — Zeyd gibi."},
 "tokens": [
  tok("وَالسَّابِعُ", "sabi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the seventh»", "«yedincisi»", segments=wa("السَّابِعُ", "sabi", "noun")),
  tok("الْمَوْقُوفُ", "mawquf", "noun", [K, MK, IMF, WQF], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«the word paused»", "«durulan»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ, NF], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ فَاعِلِ الْمَوْقُوفِ.", "«upon» — the participle's deputy doer.", "«üzerinde» — ism-i mef'ûlün nâib-i fâili.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("بِالْإِسْكَانِ", "iskan", "noun", [K, HJ, MSD, F4, WQF], "الْبَاءُ حَرْفُ جَرٍّ، وَالْإِسْكَانِ مَجْرُورٌ — مَصْدَرُ أَسْكَنَ.", "«with sukūn»", "«sükûn ile»", segments=[seg("بِ", "bi", "prep"), seg("الْإِسْكَانِ", "iskan", "noun")]),
  tok("مِمَّا", "ma-mawsula", "pron", [K, HJ, MAW], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — بَيَانٌ لِلْمَوْقُوفِ.", "«of those which»", "«-lerden»", segments=[seg("مِنْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("كَانَ", "kana", "verb", [K, MAW, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةُ مَا.", "«is»", "«olan»"),
  tok("إِعْرَابُهُ", "irab", "noun", [K, KN, ID, MSD, IRB], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its iʿrāb»", "«i'râbı»", segments=[seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  tok("بِالْحَرَكَةِ", "haraka", "noun", [K, HJ, KN, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرَكَةِ مَجْرُورٌ — خَبَرُ كَانَ.", "«by vowel» — kāna's khabar.", "«hareke ile» — kâne'nin haberi.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْحَرَكَةِ", "haraka", "noun")]),
  *kana_in(),
  tok("غَيْرَ", "ghayr", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«without»", "«almayan»"),
  tok("مُنَوَّنٍ", "munawwan", "noun", [K, ID, IMF, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«tanwīn»", "«tenvinli»"),
  tok("بِتَنْوِينِ", "tanwin", "noun", [K, HJ, ID, MSD, F2], "الْبَاءُ حَرْفُ جَرٍّ، وَتَنْوِينِ مَجْرُورٌ، مُضَافٌ.", "«the tanwīn of»", "«tenvini»", segments=[seg("بِ", "bi", "prep"), seg("تَنْوِينِ", "tanwin", "noun")]),
  tok("التَّمَكُّنِ", "tamakkun", "noun", [K, ID, MSD, F5], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَنْوِينُ الْمُنْصَرِفِ؛ فَأَحْمَدُ لَا يُنَوَّنُ بِهِ، وَضَارِبَاتٌ تَنْوِينُهَا لِلْمُقَابَلَةِ.", "«firmness» — the declinable's tanwīn; Aḥmad has none, ḍāribāt's is the tanwīn of correspondence.", "«temekkün» — munsarifin tenvini; Ahmed'de yok, dâribât'ınki mukabele tenvini.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("كَانَ", "kana", "verb", [K, AT, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ — مَعْطُوفٌ عَلَى فِعْلِ الشَّرْطِ.", "«has»", "«varsa»"),
  tok("فِي", "fi", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — خَبَرُ كَانَ مُقَدَّمٌ.", "«at»", "«-de»"),
  tok("آخِرِهِ", "akhir", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonunda»", segments=[seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("تَاءُ", "ta-letter", "noun", [K, KN, ID, MN], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the tāʾ of»", "«tâsı»"),
  tok("التَّأْنِيثِ", "tanith", "noun", [K, ID, MSD, MN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تُقْلَبُ هَاءً فِي الْوَقْفِ.", "«femininity» — turned to hāʾ in pause.", "«te'nis» — vakıfta hâ'ya döner.", punct="،"),
  tok("فَأَحْوَالُهُ", "hal", "noun", [K, INS, MK, ID, JT], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَأَحْوَالُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its states»", "«hâlleri»", segments=[seg("فَ", "fa", "conj"), seg("أَحْوَالُ", "hal", "noun"), pr3ms()]),
  tok("الثَّلَاثُ", "thalatha", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ — الطَّبْعُ: الثلث.", "«three» — the print spells it الثلث.", "«üç» — baskıda الثلث."),
  taqdiri(punct="،"),
  nahw(),
  tok("أَحْمَدْ", "ahmad", "propn", [K, ID, MMS, WQF, IRB], "لَفْظٌ مَحْكِيٌّ مَوْقُوفٌ عَلَيْهِ بِالسُّكُونِ — غَيْرُ مُنْصَرِفٍ، فَلَا تَنْوِينَ يَدُلُّ عَلَى الْحَرَكَةِ.", "«Aḥmad» — paused with sukūn; a diptote, no tanwīn to betray the vowel.", "«Ahmed» — sükûnla durulmuş; gayr-ı munsarif, harekeyi gösterecek tenvin yok."),
  tok("وَضَارِبَهْ", "darib", "noun", [K, AT, IFA, MN, WQF, IRB], "الْوَاوُ عَاطِفَةٌ، وَضَارِبَهْ مَعْطُوفٌ — التَّاءُ هَاءٌ فِي الْوَقْفِ، فَلَا تَظْهَرُ الْحَرَكَةُ.", "«and ḍāribah» — the tāʾ is hāʾ in pause; no vowel shows.", "«ve dâribeh» — tâ vakıfta hâ; hareke görünmez.", segments=wa("ضَارِبَهْ", "darib", "noun")),
  tok("وَضَارِبَاتْ", "darib", "noun", [K, AT, IFA, JMS, WQF, IRB], "الْوَاوُ عَاطِفَةٌ، وَضَارِبَاتْ مَعْطُوفٌ — تَنْوِينُهَا تَنْوِينُ مُقَابَلَةٍ لَا تَمَكُّنٍ، وَنَصْبُهَا بِالْكَسْرَةِ، فَالثَّلَاثُ مُقَدَّرَةٌ.", "«and ḍāribāt» — its tanwīn is of correspondence, its naṣb by kasra: all three estimated.", "«ve dâribât» — tenvini mukabele tenvini, nasbı kesre ile: üçü de takdîrî.", punct="،", segments=wa("ضَارِبَاتْ", "darib", "noun")),
  *kana_in(w=True),
  tok("مُنَوَّنًا", "munawwan", "noun", [K, KN, IMF, F2], "خَبَرُ كَانَ مَنْصُوبٌ.", "«with tanwīn»", "«tenvinli»"),
  tok("بِغَيْرِهَا", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — بِغَيْرِ التَّاءِ: خَالِيًا مِنْهَا.", "«without the tāʾ» — lacking it.", "«tâ'sız» — ondan yoksun.", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  tok("فَرَفْعُهُ", "raf", "noun", [K, INS, MK, ID, MSD, IRB], "الْفَاءُ رَابِطَةٌ، وَرَفْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its rafʿ»", "«ref'i»", segments=[seg("فَ", "fa", "conj"), seg("رَفْعُ", "raf", "noun"), pr3ms()]),
  tok("وَجَرُّهُ", "jarr", "noun", [K, AT, MK, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَرُّ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jarr»", "«ve ceri»", segments=[seg("وَ", "wa", "conj"), seg("جَرُّ", "jarr", "noun"), pr3ms()]),
  taqdiri(),
  tok("دُونَ", "duna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — بِمَعْنَى غَيْرِ.", "«not»", "«değil»"),
  tok("نَصْبِهِ", "nasb", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — لِأَنَّ تَنْوِينَهُ يُقْلَبُ أَلِفًا فَتَظْهَرُ الْفَتْحَةُ: زَيْدَا.", "«its naṣb» — the tanwīn becomes an alif and the fatḥa shows: zaydā.", "«nasbı» — tenvin elife döner ve fetha görünür: zeydâ.", punct="،", segments=[seg("نَصْبِ", "nasb", "noun"), pr3msi()]),
  nahw(),
  tok("زَيْدْ", "zayd", "propn", [K, ID, WQF, IRB], "لَفْظٌ مَحْكِيٌّ مَوْقُوفٌ عَلَيْهِ بِالسُّكُونِ — سَقَطَ التَّنْوِينُ وَالْحَرَكَةُ فِي الرَّفْعِ وَالْجَرِّ.", "«Zayd» — paused; tanwīn and vowel gone in rafʿ and jarr.", "«Zeyd» — durulmuş; ref' ve cerde tenvin ve hareke düşmüş.", punct="."),
 ]})
# ----------- s2 — the maḥallī: the first place
S.append({"id": "s2", "translation": {"en": "As for the maḥallī, it is in two places. One of them is the declined noun whose end is busy with a non-cited iʿrāb — as in «I passed by Zayd», for Zayd's position is ruled to be naṣb as the object; and likewise «Zayd's striking pleased me» and «Zayd was passed by», for Zayd is rafʿ in position as the doer in the first and as the deputy in the second.", "tr": "Mahallîye gelince, iki mevzidedir. Biri, sonu hikâye edilmeyen bir i'râbla meşgul olan mu'reb isimdir — «Zeyd'e uğradım» gibi; çünkü Zeyd'in mahalline mef'ûl olarak nasb hükmü verilir; «Zeyd'in dövmesi hoşuma gitti» ve «Zeyd'e uğranıldı» da böyledir; çünkü Zeyd ilkinde fâil, ikincisinde nâib olarak mahallen merfûdur."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, "amma-tafsiliyya"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«-e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْمَحَلِّيُّ", "mahalli", "noun", [K, MK, NSB, IRB], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the maḥallī»", "«mahallî»"),
  tok("فَفِي", "fi", "prep", [K, HJ, MK], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is in»", "«-dedir»", segments=fa("فِي", "fi", "prep")),
  tok("مَوْضِعَيْنِ", "mawdi", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two places»", "«iki mevzi»", punct=":"),
  tok("أَحَدُهُمَا", "ahad", "noun", [K, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them»", "«biri»", segments=[seg("أَحَدُ", "ahad", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("الِاسْمُ", "ism", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the noun»", "«isim»"),
  tok("الْمُعْرَبُ", "murab", "noun", [K, NA, IMF, F4, IRB], "نَعْتٌ مَرْفُوعٌ.", "«declined»", "«mu'reb»"),
  tok("الْمُشْتَغِلُ", "mushtaghil", "noun", [K, NA, IFA, F8], "نَعْتٌ ثَانٍ مَرْفُوعٌ — سَبَبِيٌّ.", "«busy» — a causal description.", "«meşgul» — sebebî sıfat."),
  tok("آخِرُهُ", "akhir", "noun", [K, FL, ID], "فَاعِلُ الْمُشْتَغِلِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whose end»", "«sonu»", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("بِإِعْرَابٍ", "irab", "noun", [K, HJ, MSD, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَإِعْرَابٍ مَجْرُورٌ.", "«with an iʿrāb»", "«bir i'râbla»", segments=[seg("بِ", "bi", "prep"), seg("إِعْرَابٍ", "irab", "noun")]),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ لِإِعْرَابٍ مَجْرُورٌ، مُضَافٌ.", "«non-»", "«olmayan»"),
  tok("مَحْكِيٍّ", "mahki", "noun", [K, ID, NSB, HK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَخَرَجَ الْمَوْضِعُ الثَّالِثُ مِنَ التَّقْدِيرِيِّ.", "«cited» — excluding the third taqdīrī position.", "«hikâye edilmeyen» — takdîrînin üçüncü mevzii dışarıda.", punct="،"),
  nahw(punct=":"),
  tok("مَرَرْتُ", "marra", "verb", [K, FL, "doubled-verbs"], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I passed»", "«uğradım»", segments=[seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  zayd_jarr(punct="،", ar="الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ لَفْظًا بِالْكَسْرَةِ، فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِمَرَرْتُ.", en="«by Zayd» — jarr in wording, naṣb in position.", tr="«Zeyd'e» — lafzen mecrûr, mahallen mansûb."),
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — ضَمِيرُ الشَّأْنِ.", "«for it» — the pronoun of the matter.", "«çünkü» — şe'n zamiri.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("يُحْكَمُ", "hakama", "verb", [K, IN, MR, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«it is ruled»", "«hüküm verilir»"),
  tok("عَلَى", "ala", "prep", [K, HJ, NF], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَائِبُ فَاعِلٍ.", "«upon» — the phrase is the deputy doer.", "«-e» — öbek nâib-i fâil."),
  tok("مَحَلِّ", "mahall", "noun", [K, HJ, ID, IRB], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the position of»", "«mahalline»"),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»"),
  tok("بِالنَّصْبِ", "nasb", "noun", [K, HJ, MSD, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالنَّصْبِ مَجْرُورٌ.", "«to be naṣb»", "«nasb»", segments=[seg("بِ", "bi", "prep"), seg("النَّصْبِ", "nasb", "noun")]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«olarak»"),
  tok("الْمَفْعُولِيَّةِ", "mafuliyya", "noun", [K, HJ, NSB, MB], "مَجْرُورٌ بِعَلَى — عَلَى جِهَةِ كَوْنِهِ مَفْعُولًا بِهِ.", "«object-hood»", "«mef'ûliyet»", punct="،"),
  tok("وَكَذَا", "kadha", "part", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَكَذَا خَبَرٌ مُقَدَّمٌ، وَالْمُبْتَدَأُ الْمِثَالُ.", "«and likewise»", "«ve böyledir»", segments=wa("كَذَا", "kadha", "part")),
  tok("أَعْجَبَنِي", "ajaba-please", "verb", [K, FL, MB, F4], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«pleased me»", "«hoşuma gitti»", segments=[seg("أَعْجَبَ", "ajaba-please", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("ضَرْبُ", "darb", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى فَاعِلِهِ.", "«the striking of» — a maṣdar annexed to its doer.", "«dövmesi» — fâiline muzâf mastar."),
  tok("زَيْدٍ", "zayd", "propn", [K, ID, FL, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ لَفْظًا، فِي مَحَلِّ رَفْعٍ فَاعِلُ الْمَصْدَرِ.", "«Zayd» — jarr in wording, rafʿ in position as the maṣdar's doer.", "«Zeyd'in» — lafzen mecrûr, mastarın fâili olarak mahallen merfû.", punct="،"),
  tok("وَمُرَّ", "marra", "verb", [K, AT, NF, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمُرَّ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — قِرَاءَةُ الشَّرْحِ؛ الطَّبْعُ: ومررت.", "«and … was passed» — the commentary's passive; the print has مررت.", "«ve uğranıldı» — şerhin meçhûlü; baskıda مررت.", segments=wa("مُرَّ", "marra", "verb")),
  zayd_jarr(punct="،", ar="الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ لَفْظًا، فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", en="«by Zayd» — rafʿ in position as the deputy doer.", tr="«Zeyd'e» — nâib-i fâil olarak mahallen merfû."),
  tok("فَزَيْدٌ", "zayd", "propn", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«so Zayd»", "«Zeyd»", segments=fa("زَيْدٌ", "zayd", "propn")),
  tok("مَرْفُوعُ", "marfu", "noun", [K, MK, ID, IMF, IRB], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«is rafʿ in»", "«merfûdur»"),
  tok("الْمَحَلِّ", "mahall", "noun", [K, ID, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«position»", "«mahallen»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«olarak»"),
  tok("الْفَاعِلِيَّةِ", "failiyya", "noun", [K, HJ, NSB, FL], "مَجْرُورٌ بِعَلَى.", "«doer-hood»", "«fâiliyet»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَوَّلِ", "awwal", "noun", [K, HJ], "مَجْرُورٌ بِفِي — أَعْجَبَنِي ضَرْبُ زَيْدٍ.", "«the first»", "«ilkinde»"),
  tok("وَالنَّائِبِيَّةِ", "naibiyya", "noun", [K, AT, NSB, NF], "الْوَاوُ عَاطِفَةٌ، وَالنَّائِبِيَّةِ مَعْطُوفٌ عَلَى الْفَاعِلِيَّةِ مَجْرُورٌ.", "«and deputy-hood»", "«ve nâibiyet»", segments=wa("النَّائِبِيَّةِ", "naibiyya", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الثَّانِي", "thani", "noun", [K, HJ, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مُرَّ بِزَيْدٍ.", "«the second»", "«ikincisinde»", punct="."),
 ]})
# ----------- s3 — the second place: the mabnī, defined against the muʿrab
S.append({"id": "s3", "translation": {"en": "And the second is the mabnī: it is what has its vowel and its sukūn by no governor — unlike the muʿrab, which is what has its vowel and its sukūn by a governor.", "tr": "İkincisi mebnîdir: o, harekesi ve sükûnu bir âmille olmayandır — mu'rebin aksine; mu'reb, harekesi ve sükûnu bir âmille olandır."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — ثَانِي مَوْضِعَيِ الْمَحَلِّيِّ.", "«and the second» — of the maḥallī's two places.", "«ikincisi» — mahallînin iki mevziinden.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْمَبْنِيُّ", "mabni", "noun", [K, MK, IMF, IRB], "خَبَرٌ مَرْفُوعٌ — إِعْرَابُهُ مَحَلِّيٌّ أَبَدًا.", "«the mabnī» — its iʿrāb is always by position.", "«mebnî» — i'râbı daima mahallîdir.", punct=":"),
  tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«it is»", "«o»", segments=fa("هُوَ", "huwa", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dır»"),
  tok("كَانَ", "kana", "verb", [K, MAW, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةُ مَا.", "«has»", "«olan»"),
  tok("حَرَكَتُهُ", "haraka", "noun", [K, KN, ID, IRB], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its vowel»", "«harekesi»", segments=[seg("حَرَكَتُ", "haraka", "noun"), pr3ms()]),
  tok("وَسُكُونُهُ", "sukun", "noun", [K, AT, KN, ID, MSD], "الْوَاوُ عَاطِفَةٌ، وَسُكُونُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its sukūn»", "«ve sükûnu»", segments=[seg("وَ", "wa", "conj"), seg("سُكُونُ", "sukun", "noun"), pr3ms()]),
  tok("لَا", "la", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«değil»"),
  tok("بِعَامِلٍ", "amil", "noun", [K, HJ, KN, IFA, AQ], "الْبَاءُ حَرْفُ جَرٍّ، وَعَامِلٍ مَجْرُورٌ — خَبَرُ كَانَ.", "«by a governor» — kāna's khabar.", "«bir âmille» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("عَامِلٍ", "amil", "noun")]),
  tok("بِخِلَافِ", "khilaf", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِ مَجْرُورٌ، مُضَافٌ.", "«unlike»", "«aksine»", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun")]),
  tok("الْمُعْرَبِ", "murab", "noun", [K, ID, IMF, F4, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muʿrab»", "«mu'rebin»"),
  tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«which is»", "«o»", segments=fa("هُوَ", "huwa", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dır»"),
  tok("كَانَ", "kana", "verb", [K, MAW, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةُ مَا.", "«has»", "«olan»"),
  tok("حَرَكَتُهُ", "haraka", "noun", [K, KN, ID, IRB], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its vowel»", "«harekesi»", segments=[seg("حَرَكَتُ", "haraka", "noun"), pr3ms()]),
  tok("وَسُكُونُهُ", "sukun", "noun", [K, AT, KN, ID, MSD], "الْوَاوُ عَاطِفَةٌ، وَسُكُونُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its sukūn»", "«ve sükûnu»", segments=[seg("وَ", "wa", "conj"), seg("سُكُونُ", "sukun", "noun"), pr3ms()]),
  tok("بِعَامِلٍ", "amil", "noun", [K, HJ, KN, IFA, AQ], "الْبَاءُ حَرْفُ جَرٍّ، وَعَامِلٍ مَجْرُورٌ — خَبَرُ كَانَ.", "«by a governor»", "«bir âmille»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("عَامِلٍ", "amil", "noun")]),
 ]})
# ----------- s4 — the mabnī's two kinds; the four by origin; the accidental two
S.append({"id": "s4", "translation": {"en": "And the mabnī is of two sorts: mabnī by origin and mabnī by accident. The first is four: the particle, the māḍī, the command without the lām according to the Baṣrans, and the sentence; and the second is of two sorts, lāzim and non-lāzim.", "tr": "Mebnî iki türlüdür: mebnî-i asl ve mebnî-i ârız. Birincisi dörttür: harf, mâzî, Basralılara göre lâmsız emir ve cümle; ikincisi iki türlüdür: lâzım ve gayr-ı lâzım."},
 "tokens": [
  tok("وَالْمَبْنِيُّ", "mabni", "noun", [K, AT, MK, IMF, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْمَبْنِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the mabnī»", "«mebnî»", segments=wa("الْمَبْنِيُّ", "mabni", "noun")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of»", "«üzere»"),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ.", "«two sorts»", "«iki tür»", punct=":"),
  tok("مَبْنِيُّ", "mabni", "noun", [K, MK, HT, ID, IRB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ: أَحَدُهُمَا مَبْنِيُّ الْأَصْلِ.", "«mabnī of»", "«mebnî-i»"),
  tok("الْأَصْلِ", "asl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَا بُنِيَ بِحَسَبِ أَصْلِ وَضْعِهِ.", "«origin» — built by its original coinage.", "«asl» — aslî vaz'ı gereği mebnî."),
  tok("وَمَبْنِيُّ", "mabni", "noun", [K, AT, ID, IRB], "الْوَاوُ عَاطِفَةٌ، وَمَبْنِيُّ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and mabnī of»", "«ve mebnî-i»", segments=wa("مَبْنِيُّ", "mabni", "noun")),
  tok("الْعَارِضِ", "arid", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَا عَرَضَ لَهُ الْبِنَاءُ لِشَبَهِهِ بِالْحَرْفِ.", "«accident» — built by a likeness to the particle.", "«ârız» — harfe benzerlikle sonradan mebnî.", punct="،"),
  tok("وَالْأَوَّلُ", "awwal", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the first»", "«birincisi»", segments=wa("الْأَوَّلُ", "awwal", "noun")),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«is four»", "«dörttür»", punct=":"),
  tok("الْحَرْفُ", "harf", "noun", [K, MK, HT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا الْحَرْفُ — أَوْ بَدَلٌ.", "«the particle»", "«harf»"),
  tok("وَالْمَاضِي", "madi", "noun", [K, AT, MQ], "الْوَاوُ عَاطِفَةٌ، وَالْمَاضِي مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the māḍī»", "«ve mâzî»", segments=wa("الْمَاضِي", "madi", "noun")),
  tok("وَالْأَمْرُ", "amr", "noun", [K, AT, AMR], "الْوَاوُ عَاطِفَةٌ، وَالْأَمْرُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the command»", "«ve emir»", segments=wa("الْأَمْرُ", "amr", "noun")),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID, NA], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ — نَعْتٌ لِلْأَمْرِ.", "«without»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("اللَّامِ", "lam-letter", "noun", [K, ID, "lam-amr"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَامِ الْأَمْرِ: اضْرِبْ لَا لِيَضْرِبْ.", "«the lām» — iḍrib, not li-yaḍrib.", "«lâm» — idrib, li-yadrib değil."),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«according to»", "«göre»"),
  tok("الْبَصْرِيِّينَ", "basri", "noun", [K, ID, NSB, "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — وَعِنْدَ الْكُوفِيِّينَ هُوَ مُعْرَبٌ مَجْزُومٌ بِلَامٍ مُقَدَّرَةٍ.", "«the Baṣrans» — the Kūfans hold it jazm by an estimated lām.", "«Basralılara» — Kûfeliler takdîrî lâmla meczûm sayar."),
  tok("وَالْجُمْلَةُ", "jumla", "noun", [K, AT, MJ], "الْوَاوُ عَاطِفَةٌ، وَالْجُمْلَةُ مَعْطُوفٌ مَرْفُوعٌ — قِرَاءَةُ الشَّرْحِ؛ الطَّبْعُ: والجامد.", "«and the sentence» — the commentary's reading; the print has والجامد.", "«ve cümle» — şerhin okuyuşu; baskıda والجامد.", punct="،", segments=wa("الْجُمْلَةُ", "jumla", "noun")),
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — خَبَرٌ.", "«of»", "«üzere»"),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ.", "«two sorts»", "«iki tür»", punct=":"),
  tok("لَازِمٌ", "lazim", "noun", [K, MK, HT, IFA], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا لَازِمٌ.", "«lāzim» — inseparable", "«lâzım»"),
  tok("وَغَيْرُ", "ghayr", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and non-»", "«ve gayr-ı»", segments=wa("غَيْرُ", "ghayr", "noun")),
  tok("لَازِمٍ", "lazim", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«lāzim»", "«lâzım»", punct="،"),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "iskan": G("iskan", "إِسْكَان", "س ك ن", "noun", "giving a sukūn, making the last letter vowelless (the maṣdar of askana)", "sükûn verme, iskân (eskene'nin mastarı)", 3),
 "munawwan": G("munawwan", "مُنَوَّن", "ن و ن", "noun", "bearing tanwīn (passive participle of nawwana)", "tenvinli, münevven (nevvene'nin ism-i mef'ûlü)", 3),
 "mushtaghil": G("mushtaghil", "مُشْتَغِل", "ش غ ل", "noun", "busy, occupied with (active participle of ishtaghala, form VIII)", "meşgul olan, müştegil (işteğale'nin ism-i fâili, VIII. bab)", 3),
 "failiyya": G("failiyya", "فَاعِلِيَّة", "ف ع ل", "noun", "doer-hood, the status of being the fāʿil", "fâiliyet, fâil olma", 4),
 "naibiyya": G("naibiyya", "نَائِبِيَّة", "ن و ب", "noun", "deputy-hood, the status of being the deputy doer", "nâibiyet, nâib-i fâil olma", 4),
 "arid": G("arid", "عَارِض", "ع ر ض", "noun", "accidental, supervening (active participle of ʿaraḍa); mabnī al-ʿāriḍ", "ârız, sonradan gelen (arada'nın ism-i fâili); mebnî-i ârız", 3),
 "basri": G("basri", "بَصْرِيّ", "ب ص ر", "noun", "Baṣran — of the grammarians of Baṣra", "Basralı — Basra nahivcilerinden", 3, plural="بَصْرِيُّونَ"),
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
print("izhar ch60 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "marra", "hakama", "ajaba-please") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَوْقُوفُ عَلَيْهِ وَإِعْرَابُهُ الْمُقَدَّرُ، وَالْإِعْرَابُ الْمَحَلِّيُّ فِي الْمُعْرَبِ الْمَشْغُولِ آخِرُهُ وَفِي الْمَبْنِيِّ، وَالْمَبْنِيُّ: تَعْرِيفُهُ وَنَوْعَاهُ وَأَرْبَعَةُ الْأَصْلِ", "en": "The paused word and its estimated iʿrāb; the maḥallī in the declined noun whose end is busy and in the mabnī; the mabnī defined, its two sorts, the four by origin", "tr": "Üzerinde durulan kelime ve takdîrî i'râbı; sonu meşgul mu'rebde ve mebnîde mahallî; mebnînin tarifi, iki türü, aslî dördü"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الإعراب التقديري: الموضع السابع؛ الإعراب المحلي؛ المبني", "الكافية لابن الحاجب — المبني", "شرح قطر الندى لابن هشام — الوقف، المبني والمعرب"],
 "amil": "the seventh taqdīrī position: the word paused upon with sukūn, of those declined by vowel — without the tanwīn of tamakkun or with the feminine tāʾ, all three estimated (أَحْمَدْ، ضَارِبَهْ، ضَارِبَاتْ); with that tanwīn and no tāʾ, rafʿ and jarr estimated, naṣb shown (زَيْدْ / زَيْدَا). The maḥallī is in two places: the declined noun whose end is busy with a non-cited iʿrāb (مَرَرْتُ بِزَيْدٍ — naṣb in position; أَعْجَبَنِي ضَرْبُ زَيْدٍ، مُرَّ بِزَيْدٍ — rafʿ in position), and the mabnī: what has its vowel and sukūn by no governor, unlike the muʿrab. The mabnī is by origin — the particle, the māḍī, the lām-less command for the Baṣrans, the sentence — or by accident, lāzim or not.",
 "question": {
  "en": ["What is the seventh taqdīrī position? The word paused upon with sukūn, among those whose iʿrāb is a vowel: in pause the vowel is silenced, so the case is estimated.",
         "Which paused words are estimated in all three states? The diptote with no tanwīn of tamakkun (أَحْمَدْ), the word ending in the feminine tāʾ which becomes hāʾ (ضَارِبَهْ), and the sound feminine plural whose tanwīn is of correspondence and whose naṣb is by kasra (ضَارِبَاتْ).",
         "Why is زَيْدْ estimated in rafʿ and jarr only? Its tanwīn of tamakkun is lost in pause with the ḍamma and kasra, but in naṣb the tanwīn becomes an alif and the fatḥa stays audible: رَأَيْتُ زَيْدَا.",
         "What is the maḥallī iʿrāb? The case the word's position carries when its end is already taken — by a non-cited iʿrāb, or by indeclinability.",
         "How is مَرَرْتُ بِزَيْدٍ maḥallī? Zayd's end is busy with the bāʾ's kasra, so the naṣb that مَرَرْتُ gives it as its object sits on the position; likewise ضَرْبُ زَيْدٍ, Zayd the maṣdar's doer in rafʿ by position, and مُرَّ بِزَيْدٍ, Zayd the deputy doer by position — the commentary's passive for the print's مررت.",
         "What is the mabnī, and the muʿrab? The mabnī has its vowel and sukūn by no governor; the muʿrab has them by a governor — the second place of the maḥallī, since a mabnī's case can only be positional.",
         "What is mabnī by origin? Four: the particle, the māḍī, the command without the lām (so the Baṣrans; the Kūfans decline it by an estimated lām), and the sentence — the commentary's and the Turkish question-book's reading where the print has والجامد.",
         "What does the engine READ here? The DabtEngine reads the paused forms at their sukūn as cited words, بِزَيْدٍ in jarr with its positional naṣb and rafʿ, ضَرْبُ زَيْدٍ as a maṣdar annexed to its doer, مُرَّ as a passive owing its deputy, and the lists of the mabnī as the khabar-lists they are."],
  "tr": ["Takdîrînin yedinci mevzii nedir? İ'râbı hareke olanlardan, üzerinde sükûnla durulan kelime: vakıfta hareke susar, i'râb takdir edilir.",
         "Hangi durulan kelimeler üç hâlde takdîrîdir? Temekkün tenvini olmayan gayr-ı munsarif (Ahmed), hâ'ya dönen te'nis tâsıyla biten kelime (dâribeh) ve tenvini mukabele tenvini, nasbı kesreli cem'-i müennes-i sâlim (dâribât).",
         "Zeyd neden yalnız ref' ve cerde takdîrîdir? Temekkün tenvini vakıfta damme ve kesreyle birlikte düşer; nasbda ise tenvin elife döner ve fetha duyulur: raeytü Zeydâ.",
         "Mahallî i'râb nedir? Sonu zaten dolu olan kelimenin — hikâye edilmeyen bir i'râbla ya da binâ ile — mahallinin taşıdığı i'râb.",
         "Merartü bi-Zeydin nasıl mahallîdir? Zeyd'in sonu bâ'nın kesresiyle meşguldür; merartü'nün mef'ûl olarak verdiği nasb mahalde oturur; darbu Zeydin'de Zeyd mastarın fâili olarak mahallen merfû, murre bi-Zeydin'de nâib-i fâil olarak mahallen merfû — baskının مررت'ı için şerhin meçhûlü.",
         "Mebnî ve mu'reb nedir? Mebnînin harekesi ve sükûnu âmille değildir; mu'rebinki âmilledir — mahallînin ikinci mevzii, çünkü mebnînin i'râbı ancak mahallî olur.",
         "Mebnî-i asl nedir? Dört: harf, mâzî, lâmsız emir (Basralılara göre; Kûfeliler takdîrî lâmla i'râblar) ve cümle — baskıda والجامد varken şerhin ve Türkçe soru kitabının okuyuşu.",
         "Motor burada neyi OKUR? DabtEngine durulan şekilleri sükûnlarıyla alıntı kelime, bi-Zeydin'i mahallî nasb ve ref'iyle mecrûr, darbu Zeydin'i fâiline muzâf mastar, murre'yi nâibini bekleyen meçhûl, mebnî listelerini haber listeleri olarak okur."],
 },
 "plain": {"en": "Stopping on a word silences its last vowel, so its case is only assumed — fully for Aḥmad, ḍāribah, ḍāribāt; for Zayd only in rafʿ and jarr, as «Zaydā» still sounds its naṣb. A word's position can carry a case its ending cannot show: in «I passed by Zayd», Zayd is naṣb by position, and so are indeclinable words.",
           "tr": "Bir sözcükte durunca son harekesi susar, i'râbı yalnız varsayılır — Ahmed, dâribeh, dâribât için tamamen; Zeyd için yalnız ref' ve cerde, çünkü «Zeydâ» nasbını hâlâ duyurur. Sözcüğün yeri, sonunun gösteremediği i'râbı taşıyabilir: «Zeyd'e uğradım»da Zeyd mahallen mansûbdur. Mebnî sözcükler de böyle değerlendirilir."},
 "explanation": {"en": "The seventh taqdīrī position is the word paused upon with sukūn, among those whose iʿrāb is by vowel. If it has no tanwīn of tamakkun or has the feminine tāʾ at its end, its three states are taqdīrī — أَحْمَدْ، ضَارِبَهْ، ضَارِبَاتْ; if it has that tanwīn without the tāʾ, its rafʿ and jarr are taqdīrī and not its naṣb — زَيْدْ, since رَأَيْتُ زَيْدَا keeps the fatḥa. The maḥallī is in two places. One is the declined noun whose end is busy with a non-cited iʿrāb — مَرَرْتُ بِزَيْدٍ, where Zayd's position is ruled naṣb as the object; likewise أَعْجَبَنِي ضَرْبُ زَيْدٍ and مُرَّ بِزَيْدٍ, Zayd rafʿ in position as the doer in the first and the deputy in the second — the second example is read with the Ottoman commentary as the passive مُرَّ, since the print's مررت would leave no deputy doer. The second is the mabnī: what has its vowel and sukūn by no governor, unlike the muʿrab, which has them by a governor. The mabnī is of two sorts, by origin and by accident. The first is four: the particle, the māḍī, the command without the lām according to the Baṣrans, and the sentence — read with the commentary and the Turkish question-book where the lithograph prints والجامد. The second is lāzim or non-lāzim; the lāzim kinds follow. The lithograph spells الثلث in the old orthography.",
                 "tr": "Takdîrînin yedinci mevzii, i'râbı hareke ile olanlardan üzerinde sükûnla durulan kelimedir. Temekkün tenvini almıyorsa ya da sonunda te'nis tâsı varsa üç hâli takdîrîdir — Ahmed, dâribeh, dâribât; tâ'sız olarak o tenvini alıyorsa ref' ve ceri takdîrî, nasbı değil — Zeyd; çünkü raeytü Zeydâ fethayı korur. Mahallî iki mevzidedir. Biri, sonu hikâye edilmeyen bir i'râbla meşgul mu'reb isimdir — merartü bi-Zeydin; Zeyd'in mahalline mef'ûl olarak nasb hükmü verilir; a'cebenî darbu Zeydin ve murre bi-Zeydin de böyledir, Zeyd ilkinde fâil, ikincisinde nâib olarak mahallen merfûdur — ikinci örnek Osmanlı şerhiyle meçhûl murre okunur, çünkü baskının مررت'ı nâib-i fâil bırakmaz. İkincisi mebnîdir: harekesi ve sükûnu âmille olmayan; mu'rebin aksine, onunki âmilledir. Mebnî iki türlüdür: asl ve ârız. Birincisi dörttür: harf, mâzî, Basralılara göre lâmsız emir ve cümle — litografide والجامد yazılıyken şerh ve Türkçe soru kitabıyla okunur. İkincisi lâzım ya da gayr-ı lâzımdır; lâzım olanlar gelir. Litografi الثلث'i eski imlâ ile yazar."},
 "examples": [
  {"ar": "نَحْوُ أَحْمَدْ وَضَارِبَهْ وَضَارِبَاتْ", "en": "paused: all three states estimated", "tr": "durulmuş: üç hâl takdîrî", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "فَرَفْعُهُ وَجَرُّهُ تَقْدِيرِيٌّ دُونَ نَصْبِهِ، نَحْوُ زَيْدْ", "en": "paused Zayd: naṣb still shows", "tr": "durulmuş Zeyd: nasb yine görünür", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "مَرَرْتُ بِزَيْدٍ — يُحْكَمُ عَلَى مَحَلِّ زَيْدٍ بِالنَّصْبِ", "en": "the maḥallī: the busy end", "tr": "mahallî: meşgul son", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "أَعْجَبَنِي ضَرْبُ زَيْدٍ، وَمُرَّ بِزَيْدٍ", "en": "rafʿ by position: doer and deputy", "tr": "mahallen ref': fâil ve nâib", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "الْمَبْنِيُّ مَا كَانَ حَرَكَتُهُ وَسُكُونُهُ لَا بِعَامِلٍ", "en": "the mabnī defined", "tr": "mebnînin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "الْحَرْفُ وَالْمَاضِي وَالْأَمْرُ بِغَيْرِ اللَّامِ عِنْدَ الْبَصْرِيِّينَ وَالْجُمْلَةُ", "en": "the four mabnī by origin", "tr": "aslî dört mebnî", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "رَأَيْتُ زَيْدْ (paused with sukūn)", "right": "رَأَيْتُ زَيْدَا", "why": {"en": "in pause the naṣb tanwīn becomes an alif and the fatḥa is heard", "tr": "vakıfta nasb tenvini elife döner ve fetha duyulur"}},
  {"wrong": "مَرَرْتُ بِزَيْدًا", "right": "مَرَرْتُ بِزَيْدٍ (naṣb by position)", "why": {"en": "the end is busy with the bāʾ's kasra; the object's naṣb is positional", "tr": "son bâ'nın kesresiyle meşguldür; mef'ûlün nasbı mahallîdir"}},
  {"wrong": "مُرِرْتُ بِزَيْدٍ (as the deputy-doer example)", "right": "مُرَّ بِزَيْدٍ", "why": {"en": "a deputy doer needs the passive with no other subject; the commentary reads murra", "tr": "nâib-i fâil başka öznesi olmayan meçhûl ister; şerh murre okur"}},
  {"wrong": "the mabnī has no iʿrāb at all", "right": "the mabnī has positional iʿrāb", "why": {"en": "it is the second place of the maḥallī", "tr": "mahallînin ikinci mevziidir"}},
 ],
}
ADD_EN = (" Chapter 60 (print pp. 155-156): the seventh taqdīrī position — the paused word, all three states or rafʿ and jarr only (s1); the maḥallī — the declined noun whose end is busy, murra bi-Zayd read with the commentary (s2); the mabnī defined against the muʿrab (s3); its two sorts, the four by origin with al-jumla read for the print's al-jāmid, the accidental lāzim and non-lāzim (s4).")
ADD_TR = (" Altmışıncı bab (baskı s. 155-156): takdîrînin yedinci mevzii — durulan kelime, üç hâl ya da yalnız ref' ve cer (s1); mahallî — sonu meşgul mu'reb isim, şerhle okunan murre bi-Zeyd (s2); mu'rebe karşı mebnînin tarifi (s3); iki türü, baskının el-câmid'i yerine el-cümle okunan aslî dördü, ârız lâzım ve gayr-ı lâzım (s4).")
write_out(60, S, TITLE, ADD_EN, ADD_TR, "pp. 155-156", GLOSS_ADD, notes=(NOTE,),
          related=((K59, [K]), (IRB, [K]), (MJ, [K]), (HK, [K]), (AMR, [K])))
report(60, S, GLOSS_ADD, (NOTE,))
