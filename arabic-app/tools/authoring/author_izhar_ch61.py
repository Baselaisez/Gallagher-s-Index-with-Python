# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 61: the mabnī by accident, LĀZIM — what never parts from indeclinability: the pronouns, the demonstratives, the
# relatives other than أَيّ and أَيَّة (which are declined), the noun-verbs (already treated); whatever is on فَعَالِ as a maṣdar (فَجَارِ), a description
# (يَا فَسَاقِ) or a woman's name (حَذَامِ, for the Ḥijāz); the sounds — every word that cites a sound (غَاقِ) or is sounded to beasts (نَخْ); and some
# compounds — two words neither governing the other, made one name: if the second is a sound the first is built on fatḥa (سِيبَوَيْهِ); if not, the
# first is built on fatḥa when its end is a sound letter (بَعْلَبَكَّ، حَضْرَمَوْتَ) and on sukūn when a weak letter (مَعْدِيكَرِبَ), the second declined
# as a diptote in the eloquent dialect. Print pp. 156–157.
# Readings: the lithograph prints «وهو كلمتين»; the text reads كَلِمَتَانِ as the khabar (the commentary, izhar-full-corrected l. 1880 ff., paraphrases
# «two words»). The orthography الثلث is given as الثَّلَاثِ where it occurs.
#   python3 author_izhar_ch61.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F7 = "form-vii-verbs"; MMS = "mamnu-min-sarf"; JMS = "jam-muannath-salim"; ISH = "asma-al-ishara-wa-sighuha"; ALM = "al-marifa-al-mudmarat-wal-alam"; MST = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"; LJ = "lam-jazim"; ND = "vocative-munada"
K = "al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab"
K60 = "al-taqdiri-al-sabi-wal-mahalli-wal-mabni-wa-aqsamuh"
TITLE = {"ar": "الْمَبْنِيُّ الْعَارِضُ اللَّازِمُ: الْمُضْمَرَاتُ وَالْإِشَارَاتُ وَالْمَوْصُولَاتُ وَأَسْمَاءُ الْأَفْعَالِ، وَفَعَالِ، وَالْأَصْوَاتُ، وَالْمُرَكَّبُ الْمَجْعُولُ اسْمًا وَاحِدًا", "en": "The accidental lāzim mabnī: pronouns, demonstratives, relatives and noun-verbs; faʿāli; the sounds; the compound made one name", "tr": "Ârız lâzım mebnî: zamirler, işaret isimleri, mevsûller ve isim-fiiller; feâli; sesler; tek ad kılınan mürekkep"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def cit(form, lex, pos, en, tr, extra=(), punct=None, ar=None): return tok(form, lex, pos, [K, ID, IRB] + list(extra), ar or "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مَبْنِيٌّ.", en, tr, punct=punct)
def kaf_cit(form, lex, pos, en, tr, extra=(), punct=None, ar=None): return tok(form, lex, pos, [K, HJ, IRB] + list(extra), ar or ("الْكَافُ حَرْفُ جَرٍّ، وَ" + form[2:] + " لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — مَبْنِيٌّ."), en, tr, punct=punct, segments=[seg("كَ", "ka", "prep"), seg(form[2:], lex, pos)])
def in_kana(w=False, lam=False):
    out = [tok("وَإِنْ" if w else "فَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], ("الْوَاوُ عَاطِفَةٌ" if w else "الْفَاءُ لِلتَّفْرِيعِ") + "، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»" if w else "«so if»", "«ve eğer»" if w else "«eğer»", segments=(wa if w else fa)("إِنْ", "in-shartiyya", "part"))]
    if lam: out += [tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«değilse»"), tok("يَكُنْ", "kana", "verb", [K, INS, LJ, JZ, KN, HV], "فِعْلُ الشَّرْطِ، مُضَارِعٌ نَاقِصٌ مَجْزُومٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»")]
    else: out += [tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»")]
    return out
def buniya_awwal(): return [tok("بُنِيَ", "bana", "verb", [K, INS, NF, IRB], "جَوَابُ الشَّرْطِ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is built»", "«mebnî kılınır»"), tok("الْأَوَّلُ", "awwal", "noun", [K, NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the first»", "«birincisi»")]
def ala_fath(): return [tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"), tok("الْفَتْحِ", "fath", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَلَى.", "«fatḥa»", "«fetha»")]

# ----------- s1 — the lāzim: pronouns, demonstratives, relatives, noun-verbs
S.append({"id": "s1", "translation": {"en": "And the lāzim is what does not part from indeclinability; and it is the pronouns, the demonstrative nouns, the relatives other than ayy and ayya — for those two are declined — and the noun-verbs, which have already come;", "tr": "Lâzım, binâdan ayrılmayandır; o, zamirler, işaret isimleri, eyy ve eyye dışındaki mevsûller — çünkü o ikisi mu'rebdir — ve daha önce geçen isim-fiillerdir;"},
 "tokens": [
  tok("وَاللَّازِمُ", "lazim", "noun", [K, AT, MK, IFA, IRB], "الْوَاوُ عَاطِفَةٌ، وَاللَّازِمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the lāzim»", "«lâzım»", segments=wa("اللَّازِمُ", "lazim", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dır»"),
  tok("لَا", "la", "part", [K, LN, MAW], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ صِلَةٌ.", "«not»", "«-mayan»"),
  tok("يَنْفَكُّ", "infakka", "verb", [K, MR, LN, F7, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — مُضَاعَفٌ مِنَ الِانْفِعَالِ.", "«parts» — a doubled form-VII verb.", "«ayrılır» — infiâl babından muzâaf."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  tok("الْبِنَاءِ", "bina", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَنْ.", "«indeclinability»", "«binâdan»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمُضْمَرَاتُ", "mudmar", "noun", [K, MK, IMF, F4, JMS, BM, ALM], "خَبَرٌ مَرْفُوعٌ — جَمْعُ مُضْمَرٍ: الضَّمَائِرُ كُلُّهَا.", "«the pronouns» — all of them.", "«zamirler» — hepsi."),
  tok("وَأَسْمَاءُ", "ism", "noun", [K, AT, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَأَسْمَاءُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the nouns of»", "«ve isimleri»", segments=wa("أَسْمَاءُ", "ism", "noun")),
  tok("الْإِشَارَاتِ", "ishara", "noun", [K, ID, MSD, F4, JMS, ISH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ إِشَارَةٍ.", "«demonstration» — the demonstratives.", "«işaret» — işaret isimleri."),
  tok("وَالْمَوْصُولَاتُ", "mawsul", "noun", [K, AT, IMF, JMS, MAW], "الْوَاوُ عَاطِفَةٌ، وَالْمَوْصُولَاتُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the relatives»", "«ve mevsûller»", segments=wa("الْمَوْصُولَاتُ", "mawsul", "noun")),
  tok("غَيْرَ", "ghayr", "noun", [K, MST, ID], "مُسْتَثْنًى بِغَيْرَ مَنْصُوبٌ، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("أَيٍّ", "ayy", "pron", [K, ID, MAW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَيٌّ الْمَوْصُولَةُ.", "«ayy» — the relative ayy.", "«eyy» — mevsûl eyy."),
  tok("وَأَيَّةٍ", "ayya", "pron", [K, AT, MAW], "الْوَاوُ عَاطِفَةٌ، وَأَيَّةٍ مَعْطُوفٌ مَجْرُورٌ.", "«and ayya»", "«ve eyye»", segments=wa("أَيَّةٍ", "ayya", "pron")),
  tok("فَإِنَّهُمَا", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهُمَا اسْمُهَا.", "«for those two»", "«çünkü o ikisi»", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُمَا", "pron-3d", "pron")]),
  tok("مُعْرَبَانِ", "murab", "noun", [K, IN, IMF, F4, MTH, IRB], "خَبَرُ إِنَّ مَرْفُوعٌ بِالْأَلِفِ — لِلُزُومِهِمَا الْإِضَافَةَ.", "«are declined» — since they are always annexed.", "«mu'rebdir» — daima muzâf olduklarından.", punct="،"),
  tok("وَأَسْمَاءُ", "ism", "noun", [K, AT, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَأَسْمَاءُ مَعْطُوفٌ عَلَى الْمُضْمَرَاتُ مَرْفُوعٌ، مُضَافٌ.", "«and the nouns of»", "«ve isimleri»", segments=wa("أَسْمَاءُ", "ism", "noun")),
  tok("الْأَفْعَالِ", "afal", "noun", [K, ID, JT, MNF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَزَالِ وَصَهْ وَرُوَيْدَ.", "«the verbs» — the noun-verbs: nazāli, ṣah, ruwayda.", "«fiiller» — isim-fiiller: nezâli, sah, ruveyde."),
  tok("وَقَدْ", "qad", "part", [K, AT, "hal"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and already»", "«ve … -miş»", segments=wa("قَدْ", "qad", "part")),
  tok("سَبَقَتْ", "sabaqa", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — فِي بَابِ الْعَامِلِ.", "«they have come» — in the governor's bāb.", "«geçmiştir» — âmil babında.", punct="،", segments=[seg("سَبَقَ", "sabaqa", "verb"), seg("تْ", "ta-tanith", "part")]),
 ]})
# ----------- s2 — faʿāli
S.append({"id": "s2", "translation": {"en": "and what is on faʿāli as a maṣdar, like fajāri; or as a description, as in «yā fasāqi»; or as a woman's name, as in Ḥadhāmi, according to the people of the Ḥijāz;", "tr": "ve feâli vezninde olan — mastar olarak fecâri gibi; sıfat olarak «yâ fesâki» gibi; kadın adı olarak, Hicaz ehline göre, Hazâmi gibi;"},
 "tokens": [
  tok("وَمَا", "ma-mawsula", "pron", [K, AT, MAW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى الْمُضْمَرَاتُ فِي مَحَلِّ رَفْعٍ.", "«and what»", "«ve … olan»", segments=wa("مَا", "ma-mawsula", "pron")),
  tok("كَانَ", "kana", "verb", [K, MAW, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — صِلَةُ مَا.", "«is»", "«olan»"),
  tok("عَلَى", "ala", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — خَبَرُ كَانَ.", "«on»", "«üzere»"),
  tok("فَعَالِ", "faali-wazn", "noun", [K, HJ, IRB], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — الْوَزْنُ، مَبْنِيٌّ عَلَى الْكَسْرِ.", "«faʿāli» — the pattern, built on kasra.", "«feâli» — vezin, kesre üzere mebnî."),
  tok("مَصْدَرًا", "masdar-noun", "noun", [K, "hal", MSD], "حَالٌ مَنْصُوبٌ — حَالَ كَوْنِهِ مَصْدَرًا.", "«as a maṣdar»", "«mastar olarak»"),
  kaf_cit("كَفَجَارِ", "fajar", "noun", "«like fajāri» — «debauchery», for fajra", "«fecâri gibi» — «fısk», fecre yerine", extra=(MSD,), punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("صِفَةً", "sifa", "noun", [K, AT, "hal"], "مَعْطُوفٌ عَلَى مَصْدَرًا مَنْصُوبٌ.", "«as a description»", "«sıfat olarak»"),
  nahw(),
  tok("يَا", "ya-nida", "part", [K, ND], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("فَسَاقِ", "fasaq", "noun", [K, ND, IRB], "مُنَادًى مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ — بِمَعْنَى يَا فَاسِقَةُ.", "«fasāqi» — «you wicked woman», built on kasra.", "«fesâki» — «ey fâsık kadın», kesre üzere mebnî.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("عَلَمَ", "alam-name", "noun", [K, AT, "hal", ID, ALM], "مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«as the name of»", "«alemi olarak»"),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the female»", "«dişinin»"),
  nahw(),
  cit("حَذَامِ", "hadham", "propn", "«Ḥadhāmi» — a woman's name", "«Hazâmi» — kadın adı", extra=(ALM,)),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«according to»", "«göre»"),
  tok("أَهْلِ", "ahl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the people of»", "«ehline»"),
  tok("الْحِجَازِ", "hijaz", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبَنُو تَمِيمٍ يَمْنَعُونَهُ مِنَ الصَّرْفِ.", "«the Ḥijāz» — Tamīm treats it as a diptote instead.", "«Hicaz» — Temîm ise gayr-ı munsarif sayar.", punct="،"),
 ]})
# ----------- s3 — the sounds
S.append({"id": "s3", "translation": {"en": "and the sounds — that is every word by which a sound is cited, like ghāqi, or by which beasts are called, like nakh;", "tr": "ve sesler — yani kendisiyle bir ses hikâye edilen her lafız, gâki gibi; ya da hayvanlara seslenilen, nah gibi;"},
 "tokens": [
  tok("وَالْأَصْوَاتُ", "sawt", "noun", [K, AT, JT], "الْوَاوُ عَاطِفَةٌ، وَالْأَصْوَاتُ مَعْطُوفٌ عَلَى الْمُضْمَرَاتُ مَرْفُوعٌ.", "«and the sounds»", "«ve sesler»", segments=wa("الْأَصْوَاتُ", "sawt", "noun")),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — أَيْ وَالصَّوْتُ.", "«and it is»", "«o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("كُلُّ", "kull", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«every»", "«her»"),
  tok("لَفْظٍ", "lafz", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«word»", "«lafız»"),
  tok("حُكِيَ", "haka", "verb", [K, NA, NF, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ لِلَفْظٍ.", "«is cited» — the describing clause.", "«hikâye edilen» — sıfat cümlesi."),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«by it»", "«kendisiyle»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("صَوْتٌ", "sawt", "noun", [K, NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a sound»", "«bir ses»"),
  kaf_cit("كَغَاقِ", "ghaq", "part", "«like ghāqi» — the crow's cry", "«gâki gibi» — karga sesi", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("صُوِّتَ", "sawwata", "verb", [K, AT, NF, F2], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — مَعْطُوفٌ عَلَى حُكِيَ.", "«is sounded»", "«seslenilen»"),
  tok("بِهِ", "bi", "prep", [K, HJ, NF], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ الْفَاعِلِ.", "«with it» — the deputy doer.", "«kendisiyle» — nâib-i fâil.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("لِلْبَهَائِمِ", "bahima", "noun", [K, HJ, JT, MMS], "اللَّامُ حَرْفُ جَرٍّ، وَالْبَهَائِمِ مَجْرُورٌ بِالْكَسْرَةِ لِلَّامِ — جَمْعُ بَهِيمَةٍ.", "«to beasts» — the plural of bahīma.", "«hayvanlara» — behîme'nin çoğulu.", segments=[seg("لِ", "li", "prep"), seg("الْبَهَائِمِ", "bahima", "noun")]),
  kaf_cit("كَنَخْ", "nakh", "part", "«like nakh» — to make a camel kneel", "«nah gibi» — deveyi çöktürmek için", punct="،"),
 ]})
# ----------- s4 — some compounds made one name
S.append({"id": "s4", "translation": {"en": "and some of the compounds — that is, two words neither of which governs the other, made one name: if the second is a sound, the first is built on fatḥa, as in Sībawayhi; and if it is not a sound, the first is built on fatḥa if its end is a sound letter, as in Baʿlabakk and Ḥaḍramawt, and on sukūn if its end is a weak letter, as in Maʿdīkarib — and the second is declined as a diptote in the eloquent dialect;", "tr": "ve mürekkeplerin bazısı — yani biri ötekinde âmil olmayan, tek ad kılınmış iki kelime: ikincisi ses ise birincisi fetha üzere mebnîdir, Sîbeveyhi gibi; ses değilse, sonu sahih harf ise birincisi fetha üzere — Ba'lebek ve Hadramevt gibi — sonu illet harfi ise sükûn üzere mebnîdir — Ma'dîkerib gibi — ikincisi ise fasih lehçede gayr-ı munsarif olarak mu'rebdir;"},
 "tokens": [
  tok("وَبَعْضُ", "bad", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مَعْطُوفٌ عَلَى الْمُضْمَرَاتُ مَرْفُوعٌ، مُضَافٌ.", "«and some of»", "«ve bazısı»", segments=wa("بَعْضُ", "bad", "noun")),
  tok("الْمُرَكَّبَاتِ", "murakkab", "noun", [K, ID, IMF, F2, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the compounds»", "«mürekkeplerin»"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("كَلِمَتَانِ", "kalima", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — الطَّبْعُ: كلمتين.", "«two words» — the print has كلمتين.", "«iki kelimedir» — baskıda كلمتين."),
  tok("لَيْسَتْ", "laysa", "verb", [K, NA, KN], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ نَعْتٌ لِكَلِمَتَانِ.", "«neither … is» — the describing clause.", "«… değildir» — sıfat cümlesi.", segments=[seg("لَيْسَ", "laysa", "verb"), seg("تْ", "ta-tanith", "part")]),
  tok("إِحْدَاهُمَا", "ihda", "noun", [K, KN, ID, MQ], "اسْمُ لَيْسَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them»", "«biri»", segments=[seg("إِحْدَا", "ihda", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("عَامِلَةً", "amil", "noun", [K, KN, IFA, AQ], "خَبَرُ لَيْسَ مَنْصُوبٌ.", "«governing»", "«âmil»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأُخْرَى", "ukhra", "noun", [K, HJ, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the other»", "«ötekinde»"),
  tok("جُعِلَتَا", "jaala", "verb", [K, NA, NF, MTH], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.", "«made» — a second describing clause.", "«kılınmış» — ikinci sıfat cümlesi.", segments=[seg("جُعِلَتَ", "jaala", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("اسْمًا", "ism", "noun", [K, MB], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a name»", "«ad»"),
  tok("وَاحِدًا", "wahid", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«one»", "«tek»", punct="،"),
  *in_kana(),
  tok("الثَّانِي", "thani", "noun", [K, KN, MQ], "اسْمُ كَانَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second»", "«ikincisi»"),
  tok("صَوْتًا", "sawt", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a sound»", "«ses»"),
  *buniya_awwal(),
  *ala_fath(),
  nahw(),
  cit("سِيبَوَيْهِ", "sibawayh", "propn", "«Sībawayhi» — sību + wayhi, the second a sound", "«Sîbeveyhi» — sîbu + veyhi, ikincisi ses", extra=(ALM,), punct="،", ar="لَفْظٌ مَحْكِيٌّ: الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالثَّانِي صَوْتٌ مَبْنِيٌّ عَلَى الْكَسْرِ — فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ."),
  *in_kana(w=True, lam=True),
  tok("صَوْتًا", "sawt", "noun", [K, KN], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«a sound»", "«ses»"),
  *buniya_awwal(),
  *ala_fath(),
  tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ، وَالْجَوَابُ مَحْذُوفٌ لِدَلَالَةِ مَا قَبْلَهُ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ.", "«is»", "«ise»"),
  tok("آخِرُهُ", "akhir", "noun", [K, KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonu»", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("حَرْفًا", "harf", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a letter»", "«harf»"),
  tok("صَحِيحًا", "sahih", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«sound»", "«sahih»"),
  nahw(),
  cit("بَعْلَبَكَّ", "balabakk", "propn", "«Baʿlabakk» — baʿla built on fatḥa", "«Ba'lebek» — ba'le fetha üzere mebnî", extra=(ALM, MMS)),
  tok("وَحَضْرَمَوْتَ", "hadramawt", "propn", [K, AT, ALM, MMS], "الْوَاوُ عَاطِفَةٌ، وَحَضْرَمَوْتَ مَعْطُوفٌ — الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالثَّانِي غَيْرُ مُنْصَرِفٍ.", "«and Ḥaḍramawt»", "«ve Hadramevt»", punct="،", segments=wa("حَضْرَمَوْتَ", "hadramawt", "propn")),
  tok("وَعَلَى", "ala", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَعَلَى حَرْفُ جَرٍّ.", "«and on»", "«ve … üzere»", segments=wa("عَلَى", "ala", "prep")),
  tok("السُّكُونِ", "sukun", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَلَى.", "«sukūn»", "«sükûn»"),
  tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ.", "«is»", "«ise»"),
  tok("آخِرُهُ", "akhir", "noun", [K, KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonu»", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("حَرْفَ", "harf", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«a letter of»", "«harfi»"),
  tok("عِلَّةٍ", "illa-cause", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«weakness»", "«illet»"),
  nahw(),
  cit("مَعْدِيكَرِبَ", "madikarib", "propn", "«Maʿdīkarib» — maʿdī ends in yāʾ, so built on sukūn", "«Ma'dîkerib» — ma'dî yâ ile bittiğinden sükûn üzere", extra=(ALM, MMS), punct="،", ar="لَفْظٌ مَحْكِيٌّ: الْأَوَّلُ مَبْنِيٌّ عَلَى السُّكُونِ لِأَنَّ آخِرَهُ يَاءٌ، وَالثَّانِي مُعْرَبٌ غَيْرُ مُنْصَرِفٍ — فِي مَحَلِّ جَرٍّ."),
  tok("وَأُعْرِبَ", "araba", "verb", [K, AT, NF, F4, IRB], "الْوَاوُ عَاطِفَةٌ، وَأُعْرِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … is declined»", "«ve … mu'reb kılınır»", segments=wa("أُعْرِبَ", "araba", "verb")),
  tok("الثَّانِي", "thani", "noun", [K, NF, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second»", "«ikincisi»"),
  tok("غَيْرَ", "ghayr", "noun", [K, "hal", ID, MMS], "حَالٌ مَنْصُوبٌ، مُضَافٌ.", "«as a non-»", "«gayr-ı … olarak»"),
  tok("مُنْصَرِفٍ", "munsarif", "noun", [K, ID, IFA, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لِلْعَلَمِيَّةِ وَالتَّرْكِيبِ.", "«declinable» — for name-hood and composition.", "«munsarif» — alemiyet ve terkip için."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-e göre»"),
  tok("اللُّغَةِ", "lugha", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«the dialect»", "«lehçe»"),
  tok("الْفَصِيحَةِ", "fasih", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ — وَفِيهِ لُغَاتٌ أُخْرَى: الْإِضَافَةُ، وَبِنَاءُ الْجُزْأَيْنِ.", "«eloquent» — other dialects annex the two or build both.", "«fasih» — başka lehçeler izafet yapar ya da ikisini de mebnî kılar.", punct="،"),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "ayya": G("ayya", "أَيَّة", "أ ي ي", "pron", "ayya — the feminine of ayy; declined, like ayy, among the relatives", "eyye — eyy'in müennesi; mevsûller içinde eyy gibi mu'reb", 3),
 "faali-wazn": G("faali-wazn", "فَعَالِ", "ف ع ل", "noun", "the pattern faʿāli — built on kasra: maṣdars (fajāri), descriptions (fasāqi), women's names (Ḥadhāmi)", "feâli vezni — kesre üzere mebnî: mastarlar (fecâri), sıfatlar (fesâki), kadın adları (Hazâmi)", 5),
 "fajar": G("fajar", "فَجَارِ", "ف ج ر", "noun", "fajāri — «debauchery», the indeclinable maṣdar on faʿāli", "fecâri — «fısk», feâli vezninde mebnî mastar", 5),
 "fasaq": G("fasaq", "فَسَاقِ", "ف س ق", "noun", "fasāqi — «you wicked woman», the faʿāli description used in address", "fesâki — «ey fâsık kadın», nidâda kullanılan feâli sıfatı", 5),
 "hadham": G("hadham", "حَذَامِ", "ح ذ م", "propn", "Ḥadhāmi — a woman's name on faʿāli, built on kasra by the Ḥijāz", "Hazâmi — feâli vezninde kadın adı, Hicaz'da kesre üzere mebnî", 5),
 "hijaz": G("hijaz", "الْحِجَاز", "ح ج ز", "propn", "the Ḥijāz — western Arabia; its people's usage against Tamīm's", "Hicaz — Arabistan'ın batısı; ehlinin kullanımı Temîm'inkine karşı", 3),
 "ghaq": G("ghaq", "غَاقِ", "غ ا ق", "part", "ghāqi — the cited cry of the crow; a sound-word, indeclinable", "gâki — hikâye edilen karga sesi; ses kelimesi, mebnî", 5),
 "bahima": G("bahima", "بَهِيمَة", "ب ه م", "noun", "a beast, a dumb animal; plural bahāʾim", "hayvan, behîme; çoğulu behâim", 3, plural="بَهَائِم"),
 "nakh": G("nakh", "نَخْ", "ن خ خ", "part", "nakh — the sound made to a camel to make it kneel; indeclinable", "nah — deveyi çöktürmek için çıkarılan ses; mebnî", 5),
 "sawwata": G("sawwata", "صَوَّتَ", "ص و ت", "verb", "to make a sound, to call out (form II); passive ṣuwwita bihi", "ses çıkarmak, seslenmek (II. bab); meçhûlü suvvite bihî", 3, form="II"),
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
put_morph(mo, "sawwata", {"bab": "الْبَابُ الثَّانِي فَعَّلَ — أَجْوَفُ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَصْوِيت", "ismFail": "مُصَوِّت",
 "mazi": ["صَوَّتَ", "صَوَّتَا", "صَوَّتُوا", "صَوَّتَتْ", "صَوَّتَتَا", "صَوَّتْنَ", "صَوَّتَّ", "صَوَّتُّمَا", "صَوَّتُّمْ", "صَوَّتِّ", "صَوَّتُّمَا", "صَوَّتُّنَّ", "صَوَّتُّ", "صَوَّتْنَا"],
 "mudari": ["يُصَوِّتُ", "يُصَوِّتَانِ", "يُصَوِّتُونَ", "تُصَوِّتُ", "تُصَوِّتَانِ", "يُصَوِّتْنَ", "تُصَوِّتُ", "تُصَوِّتَانِ", "تُصَوِّتُونَ", "تُصَوِّتِينَ", "تُصَوِّتَانِ", "تُصَوِّتْنَ", "أُصَوِّتُ", "نُصَوِّتُ"],
 "amr": ["صَوِّتْ", "صَوِّتَا", "صَوِّتُوا", "صَوِّتِي", "صَوِّتَا", "صَوِّتْنَ"], "mansub": "يُصَوِّتَ", "majzum": "يُصَوِّتْ", "majzum2": "تُصَوِّتْ",
 "note": "صَوَّتَ بِهِ يُصَوِّتُ تَصْوِيتًا: نَادَى وَصَاحَ — مِنَ الْبَابِ الثَّانِي، أَجْوَفُ وَاوِيٌّ تَصِحُّ وَاوُهُ لِتَشْدِيدِهَا؛ مَجْهُولُهُ صُوِّتَ بِهِ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch61 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("infakka", "sabaqa", "kana", "haka", "sawwata", "jaala", "bana", "araba", "laysa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَبْنِيُّ اللَّازِمُ: الْمُضْمَرَاتُ وَالْإِشَارَاتُ وَالْمَوْصُولَاتُ غَيْرَ أَيٍّ وَأَيَّةٍ، وَأَسْمَاءُ الْأَفْعَالِ، وَفَعَالِ، وَالْأَصْوَاتُ، وَالْمُرَكَّبُ الْمَجْعُولُ اسْمًا وَاحِدًا وَبِنَاءُ جُزْأَيْهِ", "en": "The lāzim mabnī: pronouns, demonstratives, relatives except ayy and ayya, noun-verbs; faʿāli; the sounds; the compound made one name and how its two parts are built", "tr": "Lâzım mebnî: zamirler, işaretler, eyy ve eyye dışında mevsûller, isim-fiiller; feâli; sesler; tek ad kılınan mürekkep ve iki cüzünün binâsı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المبني اللازم", "الكافية لابن الحاجب — المبني: المضمرات والإشارات والموصولات وأسماء الأفعال والأصوات والمركبات", "شرح قطر الندى لابن هشام — المبنيات"],
 "amil": "the lāzim mabnī never parts from indeclinability: the pronouns, the demonstratives, the relatives (ayy and ayya excepted — they decline), the noun-verbs; whatever is on faʿāli — maṣdar (فَجَارِ), description (يَا فَسَاقِ), woman's name (حَذَامِ, for the Ḥijāz); the sounds — a cited sound (غَاقِ) or a call to beasts (نَخْ); some compounds — two words neither governing the other, made one name: first part on fatḥa when the second is a sound (سِيبَوَيْهِ) or when the first ends in a sound letter (بَعْلَبَكَّ، حَضْرَمَوْتَ), on sukūn when it ends in a weak letter (مَعْدِيكَرِبَ); the second part a declined diptote in the eloquent dialect.",
 "question": {
  "en": ["What is the lāzim mabnī? The accidentally indeclinable word that never parts from its indeclinability — as against the non-lāzim, which is built only in some settings.",
         "Which nouns are lāzim? The pronouns, the demonstratives, the relatives and the noun-verbs — all resembling the particle in needing something else or in having its sense.",
         "Why are ayy and ayya declined among the relatives? Because they are always annexed, and annexation is a property of declined nouns — أَيُّهُمْ فِي الدَّارِ.",
         "What is faʿāli? A pattern built on kasra: as a maṣdar (فَجَارِ for الْفَجْرَة), as a description in address (يَا فَسَاقِ for يَا فَاسِقَةُ), as a woman's name (حَذَامِ) — the last for the Ḥijāz; Tamīm treats such names as diptotes instead.",
         "What are the sounds? Every word by which a sound is cited (غَاقِ, the crow) or by which beasts are called (نَخْ, to kneel a camel) — words that signify nothing by composition, so they are built.",
         "Which compounds are lāzim mabnī, and how are their parts built? Two words neither governing the other, made one name: if the second is a sound, the first is built on fatḥa (سِيبَوَيْهِ); otherwise the first is built on fatḥa when it ends in a sound letter (بَعْلَبَكَّ، حَضْرَمَوْتَ) and on sukūn when in a weak letter (مَعْدِيكَرِبَ), while the second is declined as a diptote in the eloquent dialect.",
         "What does the print write for «two words»? كلمتين where the syntax wants كَلِمَتَانِ as the khabar of وَهُوَ; the text gives the khabar form and flags the print.",
         "What does the engine READ here? The DabtEngine reads the cited forms — فَعَالِ، فَجَارِ، فَسَاقِ، حَذَامِ، غَاقِ، نَخْ، سِيبَوَيْهِ، بَعْلَبَكَّ، مَعْدِيكَرِبَ — as indeclinable quoted words after نَحْوُ and the kāf, the conditional chains with بُنِيَ الْأَوَّلُ as their answers, and the defining clauses as the khabar-lists they are."],
  "tr": ["Lâzım mebnî nedir? Binâsından hiç ayrılmayan ârız mebnî — yalnız bazı durumlarda mebnî olan gayr-ı lâzımın karşıtı.",
         "Hangi isimler lâzımdır? Zamirler, işaret isimleri, mevsûller ve isim-fiiller — hepsi başkasına muhtaç olmakla ya da onun manasını taşımakla harfe benzer.",
         "Eyy ve eyye mevsûller içinde neden mu'rebdir? Çünkü daima muzâftır; izafet mu'reb isimlerin özelliğidir — eyyühüm fi'd-dâr.",
         "Feâli nedir? Kesre üzere mebnî bir vezin: mastar olarak (el-fecre için fecâri), nidâda sıfat olarak (yâ fâsıkatü için yâ fesâki), kadın adı olarak (Hazâmi) — sonuncusu Hicaz'a göre; Temîm bu adları gayr-ı munsarif sayar.",
         "Sesler nedir? Kendisiyle bir sesin hikâye edildiği (gâki, karga) ya da hayvanlara seslenilen (nah, deveyi çöktürmek) her lafız — terkiple hiçbir mana taşımadıklarından mebnîdir.",
         "Hangi mürekkepler lâzım mebnîdir, cüzleri nasıl mebnî olur? Biri ötekinde âmil olmayan, tek ad kılınmış iki kelime: ikincisi ses ise birincisi fetha üzere (Sîbeveyhi); değilse birincisi sonu sahih harf olunca fetha üzere (Ba'lebek, Hadramevt), illet harfi olunca sükûn üzere (Ma'dîkerib) mebnîdir; ikincisi fasih lehçede gayr-ı munsarif olarak mu'rebdir.",
         "Baskı «iki kelime» için ne yazar? Nahvin ve hüve'nin haberi olarak kelimetâni istediği yerde كلمتين; metin haber şeklini verir ve baskıyı işaretler.",
         "Motor burada neyi OKUR? DabtEngine alıntı şekilleri — feâli, fecâri, fesâki, Hazâmi, gâki, nah, Sîbeveyhi, Ba'lebek, Ma'dîkerib — nahvü ve kâf'tan sonra mebnî alıntı kelime, bünie'l-evvelü cevaplı şart zincirlerini ve tarif cümlelerini haber listeleri olarak okur."],
 },
 "plain": {"en": "Some words never take case endings: pronouns, «this/that», «who/which» (except ayy), command-nouns like «ṣah!», words on faʿāli (fajāri, Ḥadhāmi), sound-words (ghāqi, nakh), and two-word names fused into one. There the first word freezes on -a (Baʿlabakk, Sībawayhi), or on no vowel after a weak letter (Maʿdīkarib).",
           "tr": "Bazı sözcükler hiç i'râb almaz: zamirler, «bu/şu», «ki» (eyy hariç), «sus!» gibi emir-isimler, feâli kalıbındaki sözler (fecâri, Hazâmi), ses sözleri (gâki, nah) ve tek ad olmuş iki sözcüklü adlar. Orada ilk sözcük -a üzerinde (Ba'lebek, Sîbeveyhi) ya da illet harfinden sonra harekesiz (Ma'dîkerib) donar."},
 "explanation": {"en": "The lāzim mabnī is what does not part from indeclinability: the pronouns, the demonstrative nouns, the relatives other than أَيّ and أَيَّة — those two are declined — and the noun-verbs, treated already under the governor. Also whatever is on فَعَالِ: as a maṣdar, like فَجَارِ; as a description, as in يَا فَسَاقِ; as a woman's name, as in حَذَامِ, according to the people of the Ḥijāz. Also the sounds: every word by which a sound is cited, like غَاقِ, or by which beasts are called, like نَخْ. And some of the compounds, that is two words neither of which governs the other, made one name (the print writes كلمتين; the khabar form كَلِمَتَانِ is read): if the second is a sound, the first is built on fatḥa — سِيبَوَيْهِ; if it is not a sound, the first is built on fatḥa when its end is a sound letter — بَعْلَبَكَّ، حَضْرَمَوْتَ — and on sukūn when its end is a weak letter — مَعْدِيكَرِبَ — and the second is declined as a diptote in the eloquent dialect. The compounds not made one name, the numeral compounds, and the non-lāzim follow.",
                 "tr": "Lâzım mebnî, binâdan ayrılmayandır: zamirler, işaret isimleri, eyy ve eyye dışındaki mevsûller — o ikisi mu'rebdir — ve âmil bahsinde geçen isim-fiiller. Ayrıca feâli vezninde olan: mastar olarak fecâri gibi; sıfat olarak yâ fesâki gibi; kadın adı olarak Hicaz ehline göre Hazâmi gibi. Ayrıca sesler: kendisiyle bir sesin hikâye edildiği her lafız, gâki gibi, ya da hayvanlara seslenilen, nah gibi. Ve mürekkeplerin bazısı, yani biri ötekinde âmil olmayan, tek ad kılınmış iki kelime (baskı كلمتين yazar; haber şekli kelimetâni okunur): ikincisi ses ise birincisi fetha üzere mebnîdir — Sîbeveyhi; ses değilse, sonu sahih harf olunca birincisi fetha üzere — Ba'lebek, Hadramevt — illet harfi olunca sükûn üzere mebnîdir — Ma'dîkerib — ikincisi ise fasih lehçede gayr-ı munsarif olarak mu'rebdir. Tek ad kılınmayan mürekkepler, sayı terkipleri ve gayr-ı lâzım gelir."},
 "examples": [
  {"ar": "الْمُضْمَرَاتُ وَأَسْمَاءُ الْإِشَارَاتِ وَالْمَوْصُولَاتُ غَيْرَ أَيٍّ وَأَيَّةٍ", "en": "the lāzim nouns", "tr": "lâzım isimler", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "كَفَجَارِ، نَحْوُ يَا فَسَاقِ، نَحْوُ حَذَامِ", "en": "faʿāli as maṣdar, description and name", "tr": "mastar, sıfat ve ad olarak feâli", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "كَغَاقِ … كَنَخْ", "en": "the sound-words", "tr": "ses kelimeleri", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "نَحْوُ سِيبَوَيْهِ … نَحْوُ بَعْلَبَكَّ وَحَضْرَمَوْتَ … نَحْوُ مَعْدِيكَرِبَ", "en": "the compound made one name: fatḥa, fatḥa, sukūn", "tr": "tek ad kılınan mürekkep: fetha, fetha, sükûn", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "مَرَرْتُ بِأَيٍّ (as an indeclinable relative)", "right": "أَيّ is declined: مَرَرْتُ بِأَيِّهِمْ", "why": {"en": "ayy and ayya are always annexed and so declined", "tr": "eyy ve eyye daima muzâftır, dolayısıyla mu'rebdir"}},
  {"wrong": "يَا فَسَاقَ", "right": "يَا فَسَاقِ", "why": {"en": "faʿāli is built on kasra", "tr": "feâli kesre üzere mebnîdir"}},
  {"wrong": "مَعْدِيَكَرِبَ", "right": "مَعْدِيكَرِبَ", "why": {"en": "a first part ending in a weak letter is built on sukūn", "tr": "sonu illet harfi olan birinci cüz sükûn üzere mebnîdir"}},
  {"wrong": "جَاءَنِي سِيبَوَيْهٌ", "right": "جَاءَنِي سِيبَوَيْهِ", "why": {"en": "the second part is a sound, so the whole stays indeclinable", "tr": "ikinci cüz sestir, bütün mebnî kalır"}},
 ],
}
ADD_EN = (" Chapter 61 (print pp. 156-157): the lāzim mabnī — pronouns, demonstratives, relatives except ayy and ayya, noun-verbs (s1); faʿāli as maṣdar, description and woman's name (s2); the sounds (s3); the compound made one name — Sībawayhi, Baʿlabakk, Ḥaḍramawt, Maʿdīkarib, with the print's kalimatayn flagged (s4).")
ADD_TR = (" Altmış birinci bab (baskı s. 156-157): lâzım mebnî — zamirler, işaretler, eyy ve eyye dışında mevsûller, isim-fiiller (s1); mastar, sıfat ve kadın adı olarak feâli (s2); sesler (s3); tek ad kılınan mürekkep — Sîbeveyhi, Ba'lebek, Hadramevt, Ma'dîkerib, baskının kelimeteyn'i işaretli (s4).")
write_out(61, S, TITLE, ADD_EN, ADD_TR, "pp. 156-157", GLOSS_ADD, notes=(NOTE,),
          related=((K60, [K]), (IRB, [K]), (ISH, [K]), (MAW, [K]), (MNF, [K]), (ALM, [K]), (MMS, [K])))
report(61, S, GLOSS_ADD, (NOTE,))
