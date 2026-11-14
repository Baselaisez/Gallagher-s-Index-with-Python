# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 62: the compounds NOT made one name whose second part contains a particle — when the first is not the word
# «two», both parts are built on fatḥa if their ends are sound letters and on sukūn if weak letters (أَحَدَ عَشَرَ، ثَلَاثَةَ عَشَرَ، ثَلَاثَ عَشَرَةَ، حَادِيْ عَشَرَ،
# حَادِيَةَ عَشَرَةَ up to تِسْعَ عَشَرَةَ; هُوَ جَارِي بَيْتَ بَيْتَ، بَيْنَ بَيْنَ); when the first is the word «two», the second is built, the first declined and its nūn
# dropped (جَاءَنِي اثْنَا عَشَرَ رَجُلًا، رَأَيْتُ اثْنَيْ عَشَرَ رَجُلًا، مَرَرْتُ بِاثْنَيْ عَشَرَ رَجُلًا). Print pp. 157–158.
# Readings: the lithograph's «وحد نونه» is read وَحُذِفَ نُونُهُ with the Ottoman commentary (izhar-full-corrected l. 1909: «the nūn of ithnayn is
# dropped»); the commentary vowels the compounds and notes حَادِيْ on sukūn (l. 1905), which the text follows; the lithograph's ثلثة is given as ثَلَاثَةَ.
#   python3 author_izhar_ch62.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; MMS = "mamnu-min-sarf"; LJ = "lam-jazim"; ADD = "al-muthanna"
K = "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"
K61 = "al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab"
TITLE = {"ar": "الْمُرَكَّبُ الَّذِي لَمْ يُجْعَلِ اسْمًا وَاحِدًا: أَحَدَ عَشَرَ إِلَى تِسْعَ عَشَرَةَ، وَبَيْتَ بَيْتَ، وَاثْنَا عَشَرَ", "en": "The compound not made one name: eleven to nineteen, bayta bayta, and ithnā ʿashara", "tr": "Tek ad kılınmayan mürekkep: on birden on dokuza, beyte beyte ve isnâ aşere"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wnahw(punct=None): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=punct, segments=wa("نَحْوُ", "nahw", "noun"))
def num(first, lex1, en1, tr1, second, lex2, en2, tr2, w=False, punct=None, ar1=None, ar2=None):
    a1 = ar1 or (("الْوَاوُ عَاطِفَةٌ، وَ" if w else "لَفْظٌ مَحْكِيٌّ: ") + (first[2:] if w else first) + " الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ.")
    a2 = ar2 or "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — الْمُرَكَّبُ فِي مَحَلِّ جَرٍّ."
    t1 = tok(first, lex1, "noun", [K, ADD, IRB] + ([AT] if w else [ID]), a1, en1, tr1, segments=wa(first[2:], lex1, "noun") if w else None)
    t2 = tok(second, lex2, "noun", [K, ADD, IRB], a2, en2, tr2, punct=punct)
    return [t1, t2]
def akhiruhuma(): return tok("آخِرُهُمَا", "akhir", "noun", [K, KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their ends»", "«sonları»", segments=[seg("آخِرُ", "akhir", "noun"), seg("هُمَا", "pron-3d", "pron")])
def in_kana(): return [tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ، وَالْجَوَابُ مَحْذُوفٌ لِدَلَالَةِ مَا قَبْلَهُ.", "«if»", "«eğer»"), tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ.", "«are»", "«ise»")]
def rajulan(punct=None): return tok("رَجُلًا", "rajul", "noun", [K, TMZ], "تَمْيِيزُ الْعَدَدِ مَنْصُوبٌ.", "«men» — the numeral's tamyīz.", "«adam» — sayının temyizi.", punct=punct)

# ----------- s1 — not made one name, the second containing a particle; the first not «two»
S.append({"id": "s1", "translation": {"en": "And if the two are not made one name, but the second contains a particle: if the first is not the word «two», the two are built on fatḥa if their ends are sound letters, and on sukūn if their ends are weak letters — as in aḥada ʿashara, thalāthata ʿashara, thalātha ʿashrata, ḥādī ʿashara and ḥādiyata ʿashrata up to tisʿa ʿashrata; and as in «he is my neighbour house to house» and «between and between»;", "tr": "İkisi tek ad kılınmayıp ikincisi bir harf içerirse: birincisi «iki» lafzı değilse, sonları sahih harf ise ikisi fetha üzere, illet harfi ise sükûn üzere mebnîdir — ehade aşere, selâsete aşere, selâse aşrate, hâdî aşere ve hâdiyete aşrate'den tis'a aşrate'ye kadar gibi; ve «o, ev eve komşumdur» ve «ara ara» gibi;"},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mazsa»"),
  tok("تُجْعَلَا", "jaala", "verb", [K, INS, LJ, JZ, NF, MTH], "فِعْلُ الشَّرْطِ، مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ.", "«the two are made»", "«ikisi kılın-»", segments=[seg("تُجْعَلَ", "jaala", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("اسْمًا", "ism", "noun", [K, MB], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a name»", "«ad»"),
  tok("وَاحِدًا", "wahid", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«one»", "«tek»"),
  tok("وَلٰكِنْ", "lakin", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ.", "«but»", "«fakat»", segments=wa("لٰكِنْ", "lakin", "part")),
  tok("تَضَمَّنَ", "tadammana", "verb", [K, FL, F5], "فِعْلٌ مَاضٍ.", "«contains»", "«içerirse»"),
  tok("الثَّانِي", "thani", "noun", [K, FL, MQ], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second»", "«ikincisi»"),
  tok("حَرْفًا", "harf", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ — حَرْفَ الْعَطْفِ أَوِ الْجَرِّ: أَحَدٌ وَعَشَرَةٌ، بَيْتًا إِلَى بَيْتٍ.", "«a particle» — the conjunction or preposition folded in.", "«bir harf» — içerilen atıf ya da cer harfi.", punct="،"),
  tok("فَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if»", "«eğer»", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«değilse»"),
  tok("يَكُنِ", "kana", "verb", [K, INS, LJ, JZ, KN, HV], "فِعْلُ الشَّرْطِ، مُضَارِعٌ نَاقِصٌ مَجْزُومٌ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«is»", "«ise»"),
  tok("الْأَوَّلُ", "awwal", "noun", [K, KN], "اسْمُ يَكُنْ مَرْفُوعٌ.", "«the first»", "«birincisi»"),
  tok("لَفْظَ", "lafz", "noun", [K, KN, ID], "خَبَرُ يَكُنْ مَنْصُوبٌ، مُضَافٌ.", "«the word»", "«lafzı»"),
  tok("اثْنَيْنِ", "ithnan", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two»", "«iki»"),
  tok("بُنِيَا", "bana", "verb", [K, INS, NF, MTH, IRB], "جَوَابُ الشَّرْطِ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ.", "«the two are built»", "«ikisi mebnîdir»", segments=[seg("بُنِيَ", "bana", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"),
  tok("الْفَتْحِ", "fath", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَلَى.", "«fatḥa»", "«fetha»"),
  *in_kana(),
  akhiruhuma(),
  tok("حَرْفًا", "harf", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a letter»", "«harf»"),
  tok("صَحِيحًا", "sahih", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«sound»", "«sahih»", punct="،"),
  tok("وَعَلَى", "ala", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَعَلَى حَرْفُ جَرٍّ.", "«and on»", "«ve … üzere»", segments=wa("عَلَى", "ala", "prep")),
  tok("السُّكُونِ", "sukun", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَلَى.", "«sukūn»", "«sükûn»"),
  *in_kana(),
  akhiruhuma(),
  tok("حَرْفَ", "harf", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«a letter of»", "«harfi»"),
  tok("عِلَّةٍ", "illa-cause", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«weakness»", "«illet»", punct="،"),
  nahw(),
  *num("أَحَدَ", "ahad", "«aḥada»", "«ehade»", "عَشَرَ", "ashar", "«ʿashara» — eleven", "«aşere» — on bir"),
  *num("وَثَلَاثَةَ", "thalatha", "«and thalāthata» — the print: ثلثة", "«ve selâsete» — baskıda ثلثة", "عَشَرَ", "ashar", "«ʿashara» — thirteen", "«aşere» — on üç", w=True),
  *num("وَثَلَاثَ", "thalath", "«and thalātha»", "«ve selâse»", "عَشَرَةَ", "ashara", "«ʿashrata» — thirteen (feminine)", "«aşrate» — on üç (müennes)", w=True),
  *num("وَحَادِيْ", "hadi-ordinal", "«and ḥādī» — on sukūn, its end a weak letter", "«ve hâdî» — sükûn üzere, sonu illet harfi", "عَشَرَ", "ashar", "«ʿashara» — eleventh", "«aşere» — on birinci", w=True, ar1="الْوَاوُ عَاطِفَةٌ، وَحَادِيْ الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى السُّكُونِ لِأَنَّ آخِرَهُ يَاءٌ — الشَّرْحُ."),
  *num("وَحَادِيَةَ", "hadiya-ordinal", "«and ḥādiyata»", "«ve hâdiyete»", "عَشَرَةَ", "ashara", "«ʿashrata» — eleventh (feminine)", "«aşrate» — on birinci (müennes)", w=True),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْغَايَةِ.", "«up to»", "«-e kadar»"),
  *num("تِسْعَ", "tis", "«tisʿa»", "«tis'a»", "عَشَرَةَ", "ashara", "«ʿashrata» — nineteen", "«aşrate» — on dokuz", punct="،", ar1="مَجْرُورٌ بِإِلَى تَقْدِيرًا — الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ."),
  wnahw(punct=":"),
  tok("هُوَ", "huwa", "pron", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«he is»", "«o»"),
  tok("جَارِي", "jar", "noun", [K, MK, ID, YM, MQ], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my neighbour»", "«komşumdur»", segments=[seg("جَارِ", "jar", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("بَيْتَ", "bayt", "noun", [K, "hal", IRB], "حَالٌ: الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — أَيْ مُلَاصِقًا.", "«house» — a ḥāl: «adjoining».", "«ev» — hâl: «bitişik».", ),
  tok("بَيْتَ", "bayt", "noun", [K, IRB], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — مُتَضَمِّنٌ مَعْنَى الْوَاوِ: بَيْتِي وَبَيْتُهُ.", "«to house» — holding the sense of «and».", "«eve» — vâv manasını içerir.", punct="،"),
  tok("وَبَيْنَ", "bayna", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ — هُوَ بَيْنَ بَيْنَ.", "«and between» — «he is between and between», middling.", "«ve ara» — «o ara aradır», orta hâlli.", segments=wa("بَيْنَ", "bayna", "noun")),
  tok("بَيْنَ", "bayna", "noun", [K, IRB], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — بَيْنَ الْجَيِّدِ وَبَيْنَ الرَّدِيءِ.", "«between» — between the good and the bad.", "«ara» — iyi ile kötü arası.", punct="،"),
 ]})
# ----------- s2 — the first is «two»
S.append({"id": "s2", "translation": {"en": "and if the first is the word «two», the second is built, the first declined and its nūn dropped — as in «there came to me twelve men», «and I saw twelve men», «and I passed by twelve men».", "tr": "birincisi «iki» lafzı ise ikincisi mebnî kılınır, birincisi i'râblanır ve nûnu hazfedilir — «bana on iki adam geldi», «on iki adam gördüm», «on iki adama uğradım» gibi."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَتِ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«is»", "«ise»", segments=[seg("كَانَ", "kana", "verb"), seg("تِ", "ta-tanith", "part")]),
  tok("الْأُولَى", "ula-first", "noun", [K, KN, MQ], "اسْمُ كَانَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — الْكَلِمَةُ الْأُولَى.", "«the first» — the first word.", "«birincisi» — ilk kelime."),
  tok("لَفْظَ", "lafz", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«the word»", "«lafzı»"),
  tok("اثْنَيْنِ", "ithnan", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two»", "«iki»"),
  tok("بُنِيَ", "bana", "verb", [K, INS, NF, IRB], "جَوَابُ الشَّرْطِ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is built»", "«mebnî kılınır»"),
  tok("الثَّانِي", "thani", "noun", [K, NF, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — عَشَرَ.", "«the second» — ʿashara.", "«ikincisi» — aşere."),
  tok("وَأُعْرِبَ", "araba", "verb", [K, AT, NF, F4, IRB], "الْوَاوُ عَاطِفَةٌ، وَأُعْرِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … is declined»", "«ve … i'râblanır»", segments=wa("أُعْرِبَ", "araba", "verb")),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — اثْنَا، بِالْأَلِفِ وَالْيَاءِ كَالْمُثَنَّى.", "«the first» — ithnā, by alif and yāʾ like the dual.", "«birincisi» — isnâ, tesniye gibi elif ve yâ ile."),
  tok("وَحُذِفَ", "hadhafa", "verb", [K, AT, NF], "الْوَاوُ عَاطِفَةٌ، وَحُذِفَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — قِرَاءَةُ الشَّرْحِ؛ الطَّبْعُ: وحد.", "«and … is dropped» — the commentary's reading; the print has وحد.", "«ve … hazfedilir» — şerhin okuyuşu; baskıda وحد.", segments=wa("حُذِفَ", "hadhafa", "verb")),
  tok("نُونُهُ", "nun-letter", "noun", [K, NF, ID, MTH], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — نُونُ التَّثْنِيَةِ، كَمَا فِي الْإِضَافَةِ.", "«its nūn» — the dual's nūn, as under annexation.", "«nûnu» — tesniye nûnu, izafette olduğu gibi.", punct="،", segments=[seg("نُونُ", "nun-letter", "noun"), pr3ms()]),
  nahw(punct=":"),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("اثْنَا", "ithnan", "noun", [K, FL, MTH, ADD, IRB], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ — مُعْرَبٌ، نُونُهُ مَحْذُوفَةٌ.", "«twelve» (ithnā) — rafʿ by the alif.", "«on iki» (isnâ) — elif ile merfû."),
  tok("عَشَرَ", "ashar", "noun", [K, ADD, IRB], "مَبْنِيٌّ عَلَى الْفَتْحِ — كَالنُّونِ الْمَحْذُوفَةِ.", "«ʿashara» — built on fatḥa, in the dropped nūn's place.", "«aşere» — fetha üzere mebnî, düşen nûnun yerinde."),
  rajulan(punct="،"),
  tok("وَرَأَيْتُ", "raa", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَرَأَيْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I saw»", "«ve gördüm»", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("اثْنَيْ", "ithnan", "noun", [K, MB, MTH, ADD, IRB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ — مُعْرَبٌ.", "«twelve» (ithnay) — naṣb by the yāʾ.", "«on iki» (isney) — yâ ile mansûb."),
  tok("عَشَرَ", "ashar", "noun", [K, ADD, IRB], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«ʿashara»", "«aşere»"),
  rajulan(punct="،"),
  tok("وَمَرَرْتُ", "marra", "verb", [K, AT, FL, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمَرَرْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I passed»", "«ve uğradım»", segments=[seg("وَ", "wa", "conj"), seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِاثْنَيْ", "ithnan", "noun", [K, HJ, MTH, ADD, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَاثْنَيْ مَجْرُورٌ بِالْيَاءِ — مُعْرَبٌ.", "«by twelve» — jarr by the yāʾ.", "«on ikiye» — yâ ile mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("اثْنَيْ", "ithnan", "noun")]),
  tok("عَشَرَ", "ashar", "noun", [K, ADD, IRB], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«ʿashara»", "«aşere»"),
  rajulan(punct="،"),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "hadi-ordinal": G("hadi-ordinal", "حَادِي", "ح د و", "noun", "ḥādī — «first» as the first part of the ordinal eleventh (ḥādī ʿashara)", "hâdî — on birinci'nin birinci cüzü olarak «birinci» (hâdî aşere)", 4),
 "hadiya-ordinal": G("hadiya-ordinal", "حَادِيَة", "ح د و", "noun", "ḥādiya — the feminine of ḥādī in ḥādiyata ʿashrata", "hâdiye — hâdiyete aşrate'de hâdî'nin müennesi", 4),
 "tis": G("tis", "تِسْع", "ت س ع", "noun", "nine (the form used before a feminine counted noun); tisʿa ʿashrata, nineteen", "dokuz (müennes ma'dûd önündeki şekil); tis'a aşrate, on dokuz", 3),
 "ula-first": G("ula-first", "أُولَى", "أ و ل", "noun", "first (feminine of awwal)", "birinci, ilk (evvel'in müennesi)", 2),
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
print("izhar ch62 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaala", "tadammana", "kana", "bana", "araba", "hadhafa", "jaa", "raa", "marra") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُرَكَّبُ غَيْرُ الْمَجْعُولِ اسْمًا وَاحِدًا وَثَانِيهِ مُتَضَمِّنٌ حَرْفًا: بِنَاءُ الْجُزْأَيْنِ فِي أَحَدَ عَشَرَ وَأَخَوَاتِهِ وَبَيْتَ بَيْتَ، وَإِعْرَابُ اثْنَا عَشَرَ", "en": "The compound not made one name whose second part holds a particle: both parts built in aḥada ʿashara and its sisters and in bayta bayta; the declension of ithnā ʿashara", "tr": "Tek ad kılınmayıp ikincisi harf içeren mürekkep: ehade aşere ve kardeşlerinde ve beyte beyte'de iki cüzün binâsı; isnâ aşere'nin i'râbı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المبني اللازم: المركبات", "الكافية لابن الحاجب — المركب والعدد", "شرح قطر الندى لابن هشام — العدد المركب"],
 "amil": "the compound not made one name whose second part contains a particle: when the first is not the word «two», both parts are built on fatḥa if their ends are sound letters and on sukūn if weak — أَحَدَ عَشَرَ، ثَلَاثَةَ عَشَرَ، ثَلَاثَ عَشَرَةَ، حَادِيْ عَشَرَ، حَادِيَةَ عَشَرَةَ … تِسْعَ عَشَرَةَ; هُوَ جَارِي بَيْتَ بَيْتَ، بَيْنَ بَيْنَ; when the first is «two», the second is built, the first declined by alif and yāʾ with its nūn dropped — اثْنَا عَشَرَ، اثْنَيْ عَشَرَ.",
 "question": {
  "en": ["What compound is this chapter about? Two words neither governing the other, not fused into one name, whose second part holds the sense of a particle — the folded «and» of the teens (أَحَدٌ وَعَشَرَةٌ) or the folded preposition of بَيْتَ بَيْتَ (بَيْتًا إِلَى بَيْتٍ).",
         "How are the two parts built? Both on fatḥa when their ends are sound letters (أَحَدَ عَشَرَ، ثَلَاثَةَ عَشَرَ، ثَلَاثَ عَشَرَةَ), on sukūn when weak — حَادِيْ عَشَرَ, whose first part ends in yāʾ, as the Ottoman commentary notes.",
         "Which forms does the print list? From أَحَدَ عَشَرَ and the thirteens, masculine and feminine, through the ordinals حَادِيْ عَشَرَ and حَادِيَةَ عَشَرَةَ, up to تِسْعَ عَشَرَةَ — the whole run of eleven to nineteen.",
         "What do بَيْتَ بَيْتَ and بَيْنَ بَيْنَ mean? «He is my neighbour house to house» — adjoining, as the commentary paraphrases مُلَاصِقًا بَيْتِي وَبَيْتُهُ; «he is between and between» — middling, between the good and the bad.",
         "What changes when the first part is «two»? Only the second is built; the first, اثْنَا, is declined like the dual — alif in rafʿ, yāʾ in naṣb and jarr — and its nūn is dropped, since عَشَرَ stands where an annexed noun would.",
         "What does the print write for the dropped nūn? وحد نونه; the text reads وَحُذِفَ نُونُهُ with the commentary («the nūn of ithnayn is dropped»).",
         "What does the engine READ here? The DabtEngine reads the cited numeral compounds as two indeclinable parts on the fatḥa, حَادِيْ on its sukūn, بَيْتَ بَيْتَ as a built ḥāl, and اثْنَا / اثْنَيْ / بِاثْنَيْ as the dual-like first part declined by alif and yāʾ before the built عَشَرَ with its tamyīz رَجُلًا."],
  "tr": ["Bu bab hangi mürekkebi ele alır? Biri ötekinde âmil olmayan, tek ad hâline gelmemiş, ikinci cüzü bir harfin manasını taşıyan iki kelime — onlu sayıların içerilmiş «ve»si (ehadün ve aşeratün) ya da beyte beyte'nin içerilmiş cer harfi (beyten ilâ beytin).",
         "İki cüz nasıl mebnî olur? Sonları sahih harf ise ikisi de fetha üzere (ehade aşere, selâsete aşere, selâse aşrate), illet harfi ise sükûn üzere — hâdî aşere, birinci cüzü yâ ile biter; Osmanlı şerhi not eder.",
         "Baskı hangi şekilleri sayar? Ehade aşere ve müzekker-müennes on üçlerden hâdî aşere ve hâdiyete aşrate sıra sayılarına, tis'a aşrate'ye kadar — on birden on dokuza bütün dizi.",
         "Beyte beyte ve beyne beyne ne demektir? «O ev eve komşumdur» — bitişik; şerhin açılımı mülâsıkan beytî ve beytühû; «o ara aradır» — orta hâlli, iyi ile kötü arası.",
         "Birinci cüz «iki» olunca ne değişir? Yalnız ikincisi mebnî olur; birincisi isnâ tesniye gibi i'râblanır — ref'te elif, nasb ve cerde yâ — ve nûnu düşer, çünkü aşere muzâfun ileyhin yerinde durur.",
         "Baskı düşen nûn için ne yazar? وحد نونه; metin şerhle ve huzife nûnuhû okur («isneyn'in nûnu hazfolunur»).",
         "Motor burada neyi OKUR? DabtEngine alıntı sayı terkiplerini fetha üzere iki mebnî cüz, hâdî'yi sükûnuyla, beyte beyte'yi mebnî hâl, isnâ / isney / bi'sney'i mebnî aşere önünde elif ve yâ ile i'râblanan tesniye benzeri birinci cüz olarak, temyizi racülen ile okur."],
 },
 "plain": {"en": "Compound numbers from eleven to nineteen are frozen: both halves end in -a (aḥada ʿashara), except that ḥādī keeps its silent yāʾ. Set phrases like «bayta bayta» (next door) and «bayna bayna» (so-so) freeze the same way. «Twelve» is the exception: its first half ithnā / ithnay changes like a dual and drops its nūn.",
           "tr": "On birden on dokuza bileşik sayılar donuktur: iki yarım da -a ile biter (ehade aşere); yalnız hâdî sessiz yâsını korur. «Beyte beyte» (bitişik) ve «beyne beyne» (şöyle böyle) gibi kalıplar da donar. «On iki» istisnadır: ilk yarısı isnâ / isney tesniye gibi değişir ve nûnunu yitirir."},
 "explanation": {"en": "If the two words are not made one name, but the second contains a particle: when the first is not the word «two», both are built on fatḥa if their ends are sound letters and on sukūn if their ends are weak letters — أَحَدَ عَشَرَ، ثَلَاثَةَ عَشَرَ، ثَلَاثَ عَشَرَةَ، حَادِيْ عَشَرَ، حَادِيَةَ عَشَرَةَ up to تِسْعَ عَشَرَةَ (the commentary vowels the run and marks حَادِيْ on sukūn, which the text follows; the print's ثلثة is given as ثَلَاثَةَ), and هُوَ جَارِي بَيْتَ بَيْتَ, وَبَيْنَ بَيْنَ. When the first is the word «two», the second is built, the first declined and its nūn dropped — the print's وحد نونه read وَحُذِفَ نُونُهُ with the commentary: جَاءَنِي اثْنَا عَشَرَ رَجُلًا، رَأَيْتُ اثْنَيْ عَشَرَ رَجُلًا، مَرَرْتُ بِاثْنَيْ عَشَرَ رَجُلًا. The kināyāt and the indeclinable adverbs follow.",
                 "tr": "İki kelime tek ad kılınmayıp ikincisi bir harf içerirse: birincisi «iki» lafzı değilse, sonları sahih harf ise ikisi fetha üzere, illet harfi ise sükûn üzere mebnîdir — ehade aşere, selâsete aşere, selâse aşrate, hâdî aşere, hâdiyete aşrate'den tis'a aşrate'ye kadar (şerh diziyi harekeler ve hâdî'yi sükûn üzere işaretler; metin ona uyar; baskının ثلثة'si selâsete olarak verilir) ve hüve cârî beyte beyte, ve beyne beyne. Birincisi «iki» lafzı ise ikincisi mebnî kılınır, birincisi i'râblanır ve nûnu hazfedilir — baskının وحد نونه'si şerhle ve huzife nûnuhû okunur: câenî isnâ aşere racülen, raeytü isney aşere racülen, merartü bi'sney aşere racülen. Kinâyeler ve mebnî zarflar gelir."},
 "examples": [
  {"ar": "أَحَدَ عَشَرَ وَثَلَاثَةَ عَشَرَ وَثَلَاثَ عَشَرَةَ", "en": "both parts on fatḥa", "tr": "iki cüz fetha üzere", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "حَادِيْ عَشَرَ وَحَادِيَةَ عَشَرَةَ إِلَى تِسْعَ عَشَرَةَ", "en": "the ordinals; the weak-ending first part on sukūn", "tr": "sıra sayıları; sonu illetli birinci cüz sükûn üzere", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "هُوَ جَارِي بَيْتَ بَيْتَ، وَبَيْنَ بَيْنَ", "en": "the set phrases", "tr": "kalıp sözler", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "جَاءَنِي اثْنَا عَشَرَ رَجُلًا، وَرَأَيْتُ اثْنَيْ عَشَرَ رَجُلًا", "en": "ithnā declined, ʿashara built", "tr": "isnâ mu'reb, aşere mebnî", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي أَحَدُ عَشَرَ رَجُلًا", "right": "جَاءَنِي أَحَدَ عَشَرَ رَجُلًا", "why": {"en": "both parts of eleven to nineteen are built on fatḥa", "tr": "on birden on dokuza iki cüz de fetha üzere mebnîdir"}},
  {"wrong": "حَادِيَ عَشَرَ (with fatḥa on the yāʾ)", "right": "حَادِيْ عَشَرَ", "why": {"en": "a first part ending in a weak letter is built on sukūn — the commentary's note", "tr": "sonu illet harfi olan birinci cüz sükûn üzere mebnîdir — şerhin notu"}},
  {"wrong": "رَأَيْتُ اثْنَا عَشَرَ رَجُلًا", "right": "رَأَيْتُ اثْنَيْ عَشَرَ رَجُلًا", "why": {"en": "ithnā is declined like the dual: yāʾ in naṣb and jarr", "tr": "isnâ tesniye gibi i'râblanır: nasb ve cerde yâ"}},
  {"wrong": "اثْنَانِ عَشَرَ", "right": "اثْنَا عَشَرَ", "why": {"en": "the nūn of ithnān drops before the built ʿashara", "tr": "isnân'ın nûnu mebnî aşere önünde düşer"}},
 ],
}
ADD_EN = (" Chapter 62 (print pp. 157-158): the compound not made one name with a particle folded into its second part — eleven to nineteen and the set phrases bayta bayta and bayna bayna, both parts built (s1); ithnā ʿashara, the first part declined with its nūn dropped, the print's wa-ḥadda read wa-ḥudhifa with the commentary (s2).")
ADD_TR = (" Altmış ikinci bab (baskı s. 157-158): ikinci cüzüne harf katılmış, tek ad kılınmayan mürekkep — on birden on dokuza ve beyte beyte, beyne beyne kalıpları, iki cüz mebnî (s1); isnâ aşere, birinci cüz nûnu düşerek mu'reb, baskının vehadde'si şerhle ve huzife okunur (s2).")
write_out(62, S, TITLE, ADD_EN, ADD_TR, "pp. 157-158", GLOSS_ADD, notes=(NOTE,),
          related=((K61, [K]), (IRB, [K]), (MTH, [K]), (TMZ, [K])))
report(62, S, GLOSS_ADD, (NOTE,))
