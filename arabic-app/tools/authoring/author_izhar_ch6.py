# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 6: the seventh and eighth of the first division — إِلَّا in the DISJOINED exception
# (the excepted thing not drawn from a plural whole; إِلَّا in the sense of لٰكِنَّ, a khabar estimated for it) and لَا of the
# absolute negation of the genus (its ism an indefinite muḍāf or like one, nothing parting them); then the SECOND division —
# مَا and لَا that resemble لَيْسَ (negation, entering upon mubtada and khabar), their three conditions (no إِنْ, no khabar, nothing
# else between them and their ism; the negation not broken by إِلَّا; لَا's ism indefinite), the failures, and the bar on a
# fronted maʿmūl. Print pp. 98–99.
#   python3 author_izhar_ch6.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "ma-la-laysa-wa-la-al-jins"
K1 = "al-amil-wa-aqsamuh"
LJ = "la-nafiya-lil-jins"; ML = "ma-la-mushabbaha"; IS = "istithna"; IW = "inna-wa-akhawatuha"
TITLE = {"ar": "إِلَّا فِي الْمُنْقَطِعِ، وَلَا لِنَفْيِ الْجِنْسِ، وَمَا وَلَا الْمُشَبَّهَتَانِ بِلَيْسَ", "en": "إِلَّا in the disjoined exception, لَا of the genus, and مَا / لَا that resemble لَيْسَ", "tr": "Munkatı' istisnâda illâ, cins nefyi lâ'sı, ve leyse'ye benzeyen mâ / lâ"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; AM = "an-masdariyya"; SH = "in-shartiyya"; LJz = "lam-jazim"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def ay(punct=":"): return tok("أَيْ", "ay", "part", [K, HT, "amma-tafsiliyya"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».", punct=punct)
def wala_q(punct=None):
    return tok("وَلَا", "la-nafiya", "part", [K, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَلَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and lā» — quoted, joined.", "«ve lâ» — hikâye edilmiş, ma'tûf.", punct=punct, segments=wa("لَا", "la-nafiya", "part"))

# ----------- s1 — the seventh: illa in the disjoined exception
S.append({"id": "s1", "translation": {"en": "And the seventh is إِلَّا in the disjoined exception — which is the one that is not drawn out of a plurality — because it has the sense of لٰكِنَّ; so a khabar is estimated for it, as in «the people came to me, except the donkey», that is: but a donkey did not come.", "tr": "Yedincisi munkatı' istisnâdaki illâ'dır — ki o, bir çokluktan çıkarılmamış olandır — lâkinne mânâsında olduğu için; o yüzden ona bir haber takdir edilir: «kavim bana geldi, eşek hâriç» gibi; yani: fakat bir eşek gelmedi."},
 "tokens": [
  tok("وَالسَّابِعُ", "sabi", "noun", [K, MK, K1], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالسَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the seventh» — the mubtada: the seventh of the eight letters.", "«yedincisi» — mübtedâ: sekiz harfin yedincisi.", segments=wa("السَّابِعُ", "sabi", "noun")),
  tok("إِلَّا", "illa", "part", [K, IS, MK, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«illā» — quoted; the khabar.", "«illâ» — hikâye edilmiş; haber."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمُسْتَثْنَى", "mustathna", "noun", [K, HJ, IS, "ism-maqsur-manqus", "ism-maful"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the excepted» — estimated jarr.", "«müstesnâ» — takdîren mecrûr."),
  tok("الْمُنْقَطِعِ", "munqati", "noun", [K, NA, IS, "ism-fail", "form-vii-verbs"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ انْقَطَعَ.", "«disjoined» — the naʿt.", "«munkatı'» — sıfat.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the mubtada.", "«o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("الَّذِي", "alladhi", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«the one that» — the relative, the khabar.", "«… olandır» — ism-i mevsûl, haber."),
  tok("لَمْ", "lam", "part", [K, LJz], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-madı»"),
  tok("يَخْرُجْ", "kharaja", "verb", [K, LJz, MW], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةٌ.", "«is drawn out» — majzūm; the ṣila.", "«çıkarılmadı» — meczûm; sıla."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("مُتَعَدِّدٍ", "mutaaddid", "noun", [K, HJ, "ism-fail", "form-v-verbs"], "مَجْرُورٌ بِمِنْ — أَيْ: مِنْ جُمْلَةٍ ذَاتِ أَفْرَادٍ.", "«a plurality» — a whole of many.", "«bir çokluktan» — fertleri olan bir bütün.", punct="،"),
  tok("لِكَوْنِهَا", "kawn", "noun", [K, HJ, ID, "masdar", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَكَوْنِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — اسْمُ كَانَ: إِلَّا.", "«because it is» — the lām of cause; the ism of the masdar is illā.", "«olduğu için» — ta'lîl lâmı; masdarın ismi illâ.", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3fs()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, KN, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَوْنِ.", "«in the sense of» — the khabar of the masdar.", "«mânâsında» — masdarın haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("لٰكِنَّ", "lakinna", "part", [K, ID, HT, IW], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«lākinna» — quoted; the muḍāf ilayh.", "«lâkinne» — hikâye edilmiş; muzâfun ileyh.", punct="،"),
  tok("فَيُقَدَّرُ", "qaddara", "verb", [K, "naib-al-fail", "form-ii-verbs", HT], "الْفَاءُ لِلتَّفْرِيعِ، وَيُقَدَّرُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«so is estimated»", "«o yüzden takdir edilir»", segments=fa("يُقَدَّرُ", "qaddara", "verb")),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — لِلْمُسْتَثْنَى.", "«for it» — for the excepted.", "«ona» — müstesnâya.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("الْخَبَرُ", "khabar-predicate", "noun", [K, "naib-al-fail", IW], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«a khabar» — the deputy doer.", "«haber» — nâib-i fâil.", punct="،"),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("الْقَوْمُ", "qawm", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — the doer.", "«kavim» — fâil."),
  tok("إِلَّا", "illa", "part", [K, IS], "أَدَاةُ اسْتِثْنَاءٍ مُنْقَطِعٍ — بِمَعْنَى لٰكِنَّ.", "«except» — the disjoined exception: «but».", "«hâriç» — munkatı' istisnâ: «fakat»."),
  tok("الْحِمَارَ", "himar", "noun", [K, IS, "mustathna-note"], "مُسْتَثْنًى مُنْقَطِعٌ مَنْصُوبٌ بِالْفَتْحَةِ — الْحِمَارُ لَيْسَ مِنَ الْقَوْمِ.", "«the donkey» — the disjoined excepted, in naṣb: no donkey is of the people.", "«eşek» — munkatı' müstesnâ, mansûb: eşek kavimden değildir.", punct="،"),
  ay(),
  tok("لٰكِنَّ", "lakinna", "part", [K, IW, HT], "حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ — التَّقْدِيرُ.", "«but» — the estimated lākinna.", "«fakat» — takdir edilen lâkinne."),
  tok("حِمَارًا", "himar", "noun", [K, IW], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a donkey» — the ism of lākinna.", "«bir eşek» — lâkinne'nin ismi."),
  tok("لَمْ", "lam", "part", [K, LJz], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-medi»"),
  tok("يَجِئْ", "jaa", "verb", [K, LJz, IW, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ لٰكِنَّ.", "«did come» — majzūm, the hollow verb's middle dropped; the khabar of lākinna.", "«geldi» — meczûm, ecvefin ortası düşmüş; lâkinne'nin haberi.", punct="."),
 ]})
# ----------- s2 — the eighth: la of the genus
S.append({"id": "s2", "translation": {"en": "And the eighth is لَا for the negation of the genus; and the condition of its governing is that its ism be an indefinite noun, annexed or resembling one annexed, not parted from it — as in «no servant of a man is sitting with us».", "tr": "Sekizincisi cinsi nefyeden lâ'dır; amelinin şartı, isminin nekre olup muzâf veya muzâfa benzer olması ve kendisinden ayrılmamasıdır — «bir adamın hiçbir kölesi yanımızda oturmuyor» gibi."},
 "tokens": [
  tok("وَالثَّامِنُ", "thamin-eighth", "noun", [K, MK, K1], "الْوَاوُ عَاطِفَةٌ، وَالثَّامِنُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the eighth» — the mubtada.", "«sekizincisi» — mübtedâ.", segments=wa("الثَّامِنُ", "thamin-eighth", "noun")),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LJ, MK, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«lā» — quoted; the khabar.", "«lâ» — hikâye edilmiş; haber."),
  tok("لِنَفْيِ", "nafy", "noun", [K, HJ, ID, "masdar", LJ], "اللَّامُ حَرْفُ جَرٍّ، وَنَفْيِ مَجْرُورٌ، مُضَافٌ — نَعْتٌ لِلَا.", "«for the negation of»", "«nefyi için»", segments=[seg("لِ", "li", "prep"), seg("نَفْيِ", "nafy", "noun")]),
  tok("الْجِنْسِ", "jins", "noun", [K, ID, LJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the genus»", "«cinsin»", punct="،"),
  tok("وَشَرْطُ", "shart", "noun", [K, MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the condition of» — the mubtada, annexed.", "«ve şartı» — mübtedâ, muzâf.", segments=wa("شَرْطُ", "shart", "noun")),
  tok("عَمَلِهَا", "amal-governing", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its governing»", "«amelinin»", segments=[seg("عَمَلِ", "amal-governing", "noun"), pr3fs()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("يَكُونَ", "kana", "verb", [K, AM, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be»", "«olması»"),
  tok("اسْمُهَا", "ism", "noun", [K, KN, ID], "اسْمُ يَكُونَ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ism» — the ism of kāna.", "«ismi» — kâne'nin ismi.", segments=[seg("اسْمُ", "ism", "noun"), pr3fs()]),
  tok("نَكِرَةً", "nakira", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«indefinite» — the khabar of kāna.", "«nekre» — kâne'nin haberi."),
  tok("مُضَافَةً", "mudaf", "noun", [K, NA, ID, "ism-maful"], "نَعْتٌ لِنَكِرَةً مَنْصُوبٌ.", "«annexed» — the naʿt.", "«muzâf» — sıfat."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  tok("مُشْتَبِهَةً", "mushtabih", "noun", [K, AT, NA, "ism-fail", "form-viii-verbs"], "مَعْطُوفٌ عَلَى مُضَافَةً مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنَ اشْتَبَهَ.", "«resembling» — joined to «annexed».", "«benzeyen» — muzâfa ma'tûf."),
  tok("بِهَا", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — بِالْمُضَافَةِ: نَحْوُ لَا خَيْرًا مِنْ زَيْدٍ عِنْدَنَا.", "«it» — the annexed one: لَا خَيْرًا مِنْ زَيْدٍ.", "«ona» — muzâfa: lâ hayran min Zeydin.", segments=[seg("بِ", "bi", "prep"), pr3fs()], punct="،"),
  tok("غَيْرَ", "ghayr", "noun", [K, "hal", ID], "حَالٌ مِنِ اسْمِهَا مَنْصُوبٌ، مُضَافٌ.", "«not» — the ḥāl, annexed.", "«olmayan» — hâl, muzâf."),
  tok("مَفْصُولٍ", "mafsul", "noun", [K, ID, "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ.", "«parted»", "«ayrılmış»"),
  tok("عَنْهَا", "an", "prep", [K, HJ], "عَنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — عَنْ لَا.", "«from it» — from lā.", "«ondan» — lâ'dan.", punct="،", segments=[seg("عَنْ", "an", "prep"), pr3fs()]),
  nahw(),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LJ], "لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ إِنَّ.", "«no» — lā of the genus, governing like inna.", "«hiçbir» — cins nefyi lâ'sı, inne gibi amel eder."),
  tok("غُلَامَ", "ghulam", "noun", [K, LJ, ID], "اسْمُ لَا مَنْصُوبٌ بِالْفَتْحَةِ لِأَنَّهُ مُضَافٌ.", "«servant of» — the ism of lā, in naṣb because annexed.", "«kölesi» — lâ'nın ismi, muzâf olduğu için mansûb."),
  tok("رَجُلٍ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a man»", "«bir adamın»"),
  tok("جَالِسٌ", "jalis-sitting", "noun", [K, LJ, "ism-fail"], "خَبَرُ لَا مَرْفُوعٌ بِالضَّمَّةِ.", "«is sitting» — the khabar of lā.", "«oturuyor» — lâ'nın haberi."),
  tok("عِنْدَنَا", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«with us»", "«yanımızda»", punct=".", segments=[seg("عِنْدَ", "inda", "noun"), seg("نَا", "pron-1p", "pron")]),
 ]})
# ----------- s3 — the second division: ma and la like laysa
S.append({"id": "s3", "translation": {"en": "And the second division is two letters: مَا and لَا, which resemble لَيْسَ in being for negation and in entering upon the mubtada and the khabar;", "tr": "İkinci kısım iki harftir: mâ ve lâ — nefy için olmakta ve mübtedâ ile habere girmekte leyse'ye benzerler;"},
 "tokens": [
  tok("وَالْقِسْمُ", "qism", "noun", [K, MK, K1], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْقِسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division» — the mubtada.", "«ve kısım» — mübtedâ.", segments=wa("الْقِسْمُ", "qism", "noun")),
  tok("الثَّانِي", "thani", "noun", [K, NA, "ism-maqsur-manqus"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«second» — the naʿt, estimated.", "«ikinci» — sıfat, takdîren."),
  tok("حَرْفَانِ", "harf", "noun", [K, MK, "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two letters» — the khabar, a dual.", "«iki harftir» — haber, tesniye.", punct=":"),
  tok("مَا", "ma-hijaziyya", "part", [K, ML, "badal", HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، بَدَلٌ مِنْ حَرْفَانِ فِي مَحَلِّ رَفْعٍ.", "«mā» — quoted; the badal.", "«mâ» — hikâye edilmiş; bedel."),
  wala_q(),
  tok("الْمُشَبَّهَتَانِ", "mushabbah", "noun", [K, NA, ML, "al-muthanna", "ism-maful"], "نَعْتٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«which resemble» — the naʿt, a dual.", "«benzeyen» — sıfat, tesniye."),
  tok("بِلَيْسَ", "laysa", "verb", [K, HJ, ML, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَلَيْسَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«to laysa» — quoted after the bāʾ.", "«leyse'ye» — bâ'dan sonra hikâye edilmiş.", segments=[seg("بِ", "bi", "prep"), seg("لَيْسَ", "laysa", "verb")]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("كَوْنِهِمَا", "kawn", "noun", [K, HJ, ID, "masdar"], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — اسْمُ كَانَ.", "«their being»", "«olmalarında»", segments=[seg("كَوْنِ", "kawn", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("لِلنَّفْيِ", "nafy", "noun", [K, HJ, KN, "masdar"], "اللَّامُ حَرْفُ جَرٍّ، وَالنَّفْيِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَوْنِ.", "«for negation» — the khabar of the masdar.", "«nefy için» — masdarın haberi.", segments=[seg("لِ", "li", "prep"), seg("النَّفْيِ", "nafy", "noun")]),
  tok("وَالدُّخُولِ", "dukhul", "noun", [K, AT, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالدُّخُولِ مَعْطُوفٌ مَجْرُورٌ.", "«and entering»", "«ve girmekte»", segments=wa("الدُّخُولِ", "dukhul", "noun")),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«upon»", "«üzerine»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "مَجْرُورٌ بِعَلَى.", "«the mubtada»", "«mübtedâ»"),
  tok("وَالْخَبَرِ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar»", "«ve haber»", punct="،", segments=wa("الْخَبَرِ", "khabar-predicate", "noun")),
 ]})
# ----------- s4 — the conditions of their governing
S.append({"id": "s4", "translation": {"en": "and the condition of their governing is that nothing part them from their ism — neither إِنْ, nor their khabar, nor anything else — and that the negation not be broken by إِلَّا; and for لَا, besides these two, it is required that its ism be indefinite — as in «Zayd is not standing» and «no man is present».", "tr": "amellerinin şartı, kendileriyle isimleri arasına ne in'in, ne haberlerinin, ne de başka bir şeyin girmemesi ve nefyin illâ ile bozulmamasıdır; lâ'da bu ikisiyle birlikte isminin nekre olması da şart koşulmuştur — «Zeyd ayakta değildir» ve «hiçbir adam hazır değildir» gibi."},
 "tokens": [
  tok("وَشَرْطُ", "shart", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the condition of» — the mubtada.", "«ve şartı» — mübtedâ.", segments=wa("شَرْطُ", "shart", "noun")),
  tok("عَمَلِهِمَا", "amal-governing", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their governing»", "«amellerinin»", segments=[seg("عَمَلِ", "amal-governing", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«not»", "«-me»"),
  tok("يُفْصَلَ", "fasala", "verb", [K, AM, "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«be parted» — the passive, its deputy the phrase after it.", "«ayrılmaması» — meçhul, nâibi ardındaki câr-mecrûr."),
  tok("بَيْنَهُمَا", "bayna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«between them»", "«onlarla»", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("وَبَيْنَ", "bayna", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«and»", "«ve»", segments=wa("بَيْنَ", "bayna", "noun")),
  tok("اسْمِهِمَا", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their ism»", "«isimleri»", segments=[seg("اسْمِ", "ism", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("بِإِنْ", "in-zaida", "part", [K, HJ, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَإِنْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — إِنْ الزَّائِدَةُ.", "«by in» — the added إِنْ, quoted.", "«in ile» — zâid in, hikâye edilmiş.", segments=[seg("بِ", "bi", "prep"), seg("إِنْ", "in-zaida", "part")]),
  wala_q(),
  tok("بِخَبَرِهِمَا", "khabar-predicate", "noun", [K, HJ, ID, AT], "الْبَاءُ حَرْفُ جَرٍّ، وَخَبَرِ مَجْرُورٌ مَعْطُوفٌ عَلَى إِنْ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«by their khabar»", "«haberleriyle»", segments=[seg("بِ", "bi", "prep"), seg("خَبَرِ", "khabar-predicate", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  wala_q(),
  tok("بِغَيْرِهِمَا", "ghayr", "noun", [K, HJ, ID, AT], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ مَعْطُوفٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«by anything else»", "«başka bir şeyle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("وَأَنْ", "an-masdariyya", "part", [K, AM, AT], "الْوَاوُ عَاطِفَةٌ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ.", "«and that»", "«ve -ması»", segments=wa("أَنْ", "an-masdariyya", "part")),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«not»", "«-me»"),
  tok("يُنْتَقَضَ", "intaqada", "verb", [K, AM, "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be broken»", "«bozulmaması»"),
  tok("النَّفْيُ", "nafy", "noun", [K, "naib-al-fail", "masdar"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«the negation» — the deputy doer.", "«nefy» — nâib-i fâil."),
  tok("بِإِلَّا", "illa", "part", [K, HJ, IS, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَإِلَّا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«by illā» — quoted.", "«illâ ile» — hikâye edilmiş.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("إِلَّا", "illa", "part")]),
  tok("وَشُرِطَ", "sharata", "verb", [K, "naib-al-fail"], "الْوَاوُ عَاطِفَةٌ، وَشُرِطَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and it is required»", "«ve şart koşulmuştur»", segments=wa("شُرِطَ", "sharata", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-de»"),
  tok("لَا", "la-nafiya", "part", [K, ML, HJ, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ فِي مَحَلِّ جَرٍّ.", "«lā» — quoted after فِي.", "«lâ» — fî'den sonra hikâye edilmiş."),
  tok("مَعَهُمَا", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — مَعَ الشَّرْطَيْنِ.", "«besides these two» — with the two conditions.", "«bu ikisiyle birlikte» — iki şartla.", segments=[seg("مَعَ", "maa", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("كَوْنُ", "kawn", "noun", [K, "naib-al-fail", ID, "masdar"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ.", "«the being of» — the deputy doer.", "«olması» — nâib-i fâil."),
  tok("اسْمِهَا", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — اسْمُ كَانَ.", "«its ism»", "«isminin»", segments=[seg("اسْمِ", "ism", "noun"), pr3fs()]),
  tok("نَكِرَةً", "nakira", "noun", [K, KN], "خَبَرُ كَوْنُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«indefinite» — the khabar of the masdar.", "«nekre» — masdarın haberi.", punct="،"),
  nahw(),
  tok("مَا", "ma-hijaziyya", "part", [K, ML], "مَا الْحِجَازِيَّةُ، تَعْمَلُ عَمَلَ لَيْسَ.", "«not» — the Ḥijāzī mā, governing like laysa.", "«değil» — Hicâzî mâ, leyse gibi amel eder."),
  tok("زَيْدٌ", "zayd", "propn", [K, ML], "اسْمُ مَا مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the ism of mā.", "«Zeyd» — mâ'nın ismi."),
  tok("قَائِمًا", "qaim", "noun", [K, ML, "ism-fail"], "خَبَرُ مَا مَنْصُوبٌ بِالْفَتْحَةِ.", "«standing» — the khabar of mā, in naṣb.", "«ayakta» — mâ'nın haberi, mansûb.", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, ML, AT], "الْوَاوُ عَاطِفَةٌ، وَلَا الْمُشَبَّهَةُ بِلَيْسَ.", "«and no» — lā like laysa.", "«ve hiçbir» — leyse'ye benzeyen lâ.", segments=wa("لَا", "la-nafiya", "part")),
  tok("رَجُلٌ", "rajul", "noun", [K, ML], "اسْمُ لَا مَرْفُوعٌ بِالضَّمَّةِ — نَكِرَةٌ كَمَا شُرِطَ.", "«a man» — the ism of lā, indefinite as required.", "«adam» — lâ'nın ismi, şart koşulduğu gibi nekre."),
  tok("حَاضِرًا", "hadir", "noun", [K, ML, "ism-fail"], "خَبَرُ لَا مَنْصُوبٌ بِالْفَتْحَةِ.", "«present» — the khabar of lā, in naṣb.", "«hazır» — lâ'nın haberi, mansûb.", punct="."),
 ]})
# ----------- s5 — a condition missing: no governing; no fronting
S.append({"id": "s5", "translation": {"en": "And if one of the conditions is not found they do not govern — as in «Zayd is not at all standing», «standing Zayd is not», «Zayd is nothing but standing»; and their governed word does not come before them.", "tr": "Şartlardan biri bulunmazsa amel etmezler — «Zeyd hiç ayakta değildir», «ayakta değildir Zeyd», «Zeyd ancak ayaktadır» gibi; ma'mûlleri onların önüne geçmez."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, SH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("لَمْ", "lam", "part", [K, LJz, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mazsa»"),
  tok("يُوجَدْ", "wajada", "verb", [K, LJz, SH, "naib-al-fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ — فِعْلُ الشَّرْطِ.", "«is found» — the condition's verb, passive and majzūm.", "«bulunmazsa» — şart fiili, meçhul ve meczûm."),
  tok("أَحَدُ", "ahad", "noun", [K, "naib-al-fail", ID], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ.", "«one of» — the deputy doer.", "«biri» — nâib-i fâil."),
  tok("الشُّرُوطِ", "shart", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ شَرْطٍ.", "«the conditions»", "«şartlardan»"),
  tok("لَمْ", "lam", "part", [K, LJz, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("تَعْمَلْ", "amila", "verb", [K, LJz, SH], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ — جَوَابُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they govern» — the answer, majzūm.", "«amel eder» — cevap, meczûm.", punct="،"),
  nahw(),
  tok("مَا", "ma-nafiya", "part", [K, ML, "anwa-ma"], "حَرْفُ نَفْيٍ مُهْمَلٌ — فُصِلَ بِإِنْ.", "«not» — mā left ungoverning: إِنْ parts it.", "«değil» — amelsiz mâ: in ayırıyor."),
  tok("إِنْ", "in-zaida", "part", [K, ML, "tawkid"], "إِنْ الزَّائِدَةُ لِتَأْكِيدِ النَّفْيِ — الْفَاصِلَةُ.", "«at all» — the added إِنْ strengthening the negation; the parting word.", "«hiç» — nefyi pekiştiren zâid in; ayırıcı."),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — a mubtada.", "«Zeyd» — mübtedâ."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ — لَا مَنْصُوبٌ.", "«standing» — the khabar, in rafʿ, not naṣb.", "«ayaktadır» — haber, merfû, mansûb değil.", punct="،"),
  tok("وَمَا", "ma-nafiya", "part", [K, ML, "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا حَرْفُ نَفْيٍ مُهْمَلٌ — تَقَدَّمَ الْخَبَرُ.", "«and not» — ungoverning: the khabar came first.", "«ve değil» — amelsiz: haber öne geçti.", segments=wa("مَا", "ma-nafiya", "part")),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, "ism-fail", "taqdim-al-musnad"], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«standing» — the fronted khabar.", "«ayakta» — mukaddem haber."),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«Zayd» — the delayed mubtada.", "«Zeyd» — muahhar mübtedâ.", punct="،"),
  tok("وَمَا", "ma-nafiya", "part", [K, ML, "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا حَرْفُ نَفْيٍ مُهْمَلٌ — انْتُقِضَ النَّفْيُ بِإِلَّا.", "«and not» — ungoverning: illā broke the negation.", "«ve değil» — amelsiz: illâ nefyi bozdu.", segments=wa("مَا", "ma-nafiya", "part")),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — a mubtada.", "«Zeyd» — mübtedâ."),
  tok("إِلَّا", "illa", "part", [K, IS, "istithna-mufarragh", "qasr"], "أَدَاةُ حَصْرٍ — اسْتِثْنَاءٌ مُفَرَّغٌ.", "«nothing but» — the restriction.", "«ancak» — hasr."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«standing» — the khabar.", "«ayaktadır» — haber.", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, "la-nafiya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, FL, "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«comes before»", "«öne geçer»"),
  tok("مَعْمُولُهُمَا", "mamul", "noun", [K, FL, ID, "ism-maful"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their governed word» — the doer.", "«ma'mûlleri» — fâil.", segments=[seg("مَعْمُولُ", "mamul", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("عَلَيْهِمَا", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَهِمَا فِي مَحَلِّ جَرٍّ.", "«them»", "«onların önüne»", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِمَا", "pron-3d", "pron")]),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i] and g != "mustathna-note"]

CAND = {
 "sabi": G("sabi", "سَابِع", "س ب ع", "noun", "seventh", "yedinci", 2),
 "thamin-eighth": G("thamin-eighth", "ثَامِن", "ث م ن", "noun", "eighth", "sekizinci", 2),
 "illa": G("illa", "إِلَّا", None, "part", "except; (after a negation) only", "hâriç; ancak", 1),
 "mustathna": G("mustathna", "الْمُسْتَثْنَى", "ث ن ي", "noun", "the excepted thing (ism mafʿūl of اسْتَثْنَى)", "müstesnâ — istisnâ edilen", 4),
 "munqati": G("munqati", "مُنْقَطِع", "ق ط ع", "noun", "disjoined — an exception not drawn from the whole (ism fāʿil of انْقَطَعَ)", "munkatı' — bütünden çıkarılmamış istisnâ", 5),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which, that (masculine relative)", "ellezî — müzekker ism-i mevsûl", 2),
 "lam": G("lam", "لَمْ", None, "part", "did not — negates the muḍāriʿ, puts it in jazm and turns it to the past", "lem — muzâriyi cezm eder ve mâzîye çevirir", 2),
 "kharaja": G("kharaja", "خَرَجَ", "خ ر ج", "verb", "to go out, to be drawn out of", "çıkmak", 1),
 "mutaaddid": G("mutaaddid", "مُتَعَدِّد", "ع د د", "noun", "plural, manifold (ism fāʿil of تَعَدَّدَ)", "müteaddit — birden çok", 4),
 "qaddara": G("qaddara", "قَدَّرَ", "ق د ر", "verb", "to estimate, to assume an unspoken wording", "takdir etmek", 3),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people, a folk", "kavim", 1),
 "himar": G("himar", "حِمَار", "ح م ر", "noun", "a donkey", "eşek", 1, plural="حَمِير"),
 "jins": G("jins", "جِنْس", "ج ن س", "noun", "the genus, the kind; لَا لِنَفْيِ الْجِنْسِ", "cins; cins nefyi lâ'sı", 3),
 "nakira": G("nakira", "نَكِرَة", "ن ك ر", "noun", "an indefinite noun", "nekre — belirsiz isim", 3),
 "mushtabih": G("mushtabih", "مُشْتَبِه", "ش ب ه", "noun", "resembling (ism fāʿil of اشْتَبَهَ); الْمُشْتَبِهُ بِالْمُضَافِ: لَا خَيْرًا مِنْ زَيْدٍ", "müştebih — benzeyen; muzâfa benzeyen: lâ hayran min Zeyd", 5),
 "mafsul": G("mafsul", "مَفْصُول", "ف ص ل", "noun", "parted, separated (ism mafʿūl of فَصَلَ)", "mefsûl — ayrılmış", 4),
 "ghulam": G("ghulam", "غُلَام", "غ ل م", "noun", "a boy, a servant", "köle, oğlan", 1, plural="غِلْمَان"),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1, plural="رِجَال"),
 "thani": G("thani", "ثَانِي", "ث ن ي", "noun", "second", "ikinci", 1),
 "ma-hijaziyya": G("ma-hijaziyya", "مَا (الْحِجَازِيَّة)", None, "part", "the Ḥijāzī mā — the negating mā that governs like لَيْسَ", "Hicâzî mâ — leyse gibi amel eden nefy mâ'sı", 5),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not — the frozen verb of negation", "leyse — değildir; câmid nefy fiili", 2),
 "fasala": G("fasala", "فَصَلَ", "ف ص ل", "verb", "to part, to separate", "ayırmak", 3),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between (a ẓarf)", "arasında (zarf)", 1),
 "in-zaida": G("in-zaida", "إِنْ (الزَّائِدَة)", None, "part", "the added إِنْ — after مَا it strengthens the negation and stops مَا's governing", "zâid in — mâ'dan sonra nefyi pekiştirir ve mâ'nın amelini durdurur", 5),
 "intaqada": G("intaqada", "اِنْتَقَضَ", "ن ق ض", "verb", "to be broken, undone (Form VIII)", "bozulmak (iftiâl)", 4),
 "sharata": G("sharata", "شَرَطَ", "ش ر ط", "verb", "to stipulate, to require as a condition", "şart koşmak", 3),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find; (passive) to be found, to exist", "bulmak; (meçhul) bulunmak", 1),
 "taqaddama": G("taqaddama", "تَقَدَّمَ", "ق د م", "verb", "to come before, to precede (Form V)", "öne geçmek (tefa''ul)", 3),
 "mamul": G("mamul", "الْمَعْمُول", "ع م ل", "noun", "the governed word (ism mafʿūl of عَمِلَ)", "ma'mûl — âmilin etki ettiği", 4),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "the negating lā", "nefy lâ'sı", 1),
 "la-nafiya-lil-jins": G("la-nafiya-lil-jins", "لَا (النَّافِيَةُ لِلْجِنْس)", None, "part", "lā of the absolute negation of the genus — governs like إِنَّ", "cins nefyi lâ'sı — inne gibi amel eder", 4),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but, yet — the sister of إِنَّ that rectifies", "lâkinne — fakat; istidrak bildiren inne kardeşi", 3),
 "maa": G("maa", "مَعَ", None, "noun", "with, together with (a ẓarf)", "ile, beraber (zarf)", 2),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "with, at (a ẓarf of place)", "yanında, nezdinde (mekân zarfı)", 2),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection before the speaker's yāʾ", "vikâye nûnu — mütekellim yâsından önce", 4),
 "pron-3d": G("pron-3d", "هُمَا", None, "pron", "they two / their (attached)", "o ikisi / onların (bitişik)", 1),
 "jalis-sitting": G("jalis-sitting", "جَالِس", "ج ل س", "noun", "sitting (ism fāʿil of جَلَسَ)", "oturan", 2),
 "hadir": G("hadir", "حَاضِر", "ح ض ر", "noun", "present (ism fāʿil of حَضَرَ)", "hazır", 2),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "shart": G("shart", "شَرْط", "ش ر ط", "noun", "a condition", "şart", 2, plural="شُرُوط"),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "one, any one", "biri, herhangi biri", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to work; to govern (of a governor)", "çalışmak; amel etmek (âmil)", 2),
 "dukhul": G("dukhul", "دُخُول", "د خ ل", "noun", "entering (masdar of دَخَلَ)", "giriş, dâhil olma", 2),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "the negating mā (with the māḍī: did not)", "nefy mâ'sı (mâzîyle: -medi)", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "kharaja", _sg.sound1("nasara", "خَرَج", "خْرُج", "اُخْرُج", "خُرُوج", "خَارِج", "مَخْرُوج", "خُرِجَ", "يُخْرَجُ", "خَرَجَ يَخْرُجُ: بَرَزَ — بَابُ نَصَرَ"))
put_morph(mo, "qaddara", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَدَّر", "قَدِّر", "قَدِّر", "تَقْدِير", "مُقَدِّر", "مُقَدَّر", "قُدِّرَ", "يُقَدَّرُ", "قَدَّرَ يُقَدِّرُ: افْتَرَضَ وَأَضْمَرَ — بَابُ التَّفْعِيلِ"))
put_morph(mo, "fasala", _sg.sound1("daraba", "فَصَل", "فْصِل", "اِفْصِل", "فَصْل", "فَاصِل", "مَفْصُول", "فُصِلَ", "يُفْصَلُ", "فَصَلَ يَفْصِلُ: فَرَّقَ — بَابُ ضَرَبَ"))
put_morph(mo, "intaqada", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَقَض", "نْتَقِض", "اِنْتَقِض", "اِنْتِقَاض", "مُنْتَقِض", "مُنْتَقَض", "اُنْتُقِضَ", "يُنْتَقَضُ", "اِنْتَقَضَ يَنْتَقِضُ: انْحَلَّ وَبَطَلَ — بَابُ الِافْتِعَالِ"))
put_morph(mo, "sharata", _sg.sound1("daraba", "شَرَط", "شْرِط", "اِشْرِط", "شَرْط", "شَارِط", "مَشْرُوط", "شُرِطَ", "يُشْرَطُ", "شَرَطَ يَشْرِطُ: جَعَلَهُ شَرْطًا — بَابُ ضَرَبَ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch6 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "إِلَّا الْمُنْقَطِعَةُ، وَلَا لِنَفْيِ الْجِنْسِ، وَمَا وَلَا الْمُشَبَّهَتَانِ بِلَيْسَ", "en": "The disjoined إِلَّا, لَا of the genus, and مَا / لَا that resemble لَيْسَ", "tr": "Munkatı' illâ, cins nefyi lâ'sı, ve leyse'ye benzeyen mâ / lâ"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العامل في اسمين", "الكافية لابن الحاجب — الاستثناء، لا لنفي الجنس، ما ولا المشبهتان بليس", "العوامل المائة للبركوي"],
 "amil": "إِلَّا بِمَعْنَى لٰكِنَّ، وَلَا بِمَعْنَى إِنَّ، وَمَا وَلَا بِمَعْنَى لَيْسَ — three letters that borrow a verb's work: إِلَّا takes لٰكِنَّ's naṣb, لَا takes إِنَّ's, مَا and لَا take لَيْسَ's naṣb of the khabar",
 "question": {
  "en": ["WHEN is إِلَّا a governor of two nouns? In the DISJOINED exception — the excepted thing was never part of the whole (جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ): إِلَّا then means لٰكِنَّ, the noun after it is in naṣb and a khabar is estimated (لٰكِنَّ حِمَارًا لَمْ يَجِئْ).",
         "WHEN does لَا govern like إِنَّ? When it denies the whole genus and its ism is an indefinite noun that is ANNEXED (لَا غُلَامَ رَجُلٍ) or resembles one annexed (لَا خَيْرًا مِنْ زَيْدٍ), with nothing between لَا and the ism.",
         "What are مَا and لَا that resemble لَيْسَ? Negations that enter upon a mubtada and khabar and, like لَيْسَ, leave the ism in rafʿ and put the KHABAR in naṣb: مَا زَيْدٌ قَائِمًا، لَا رَجُلٌ حَاضِرًا.",
         "Their three conditions? Nothing parts them from the ism — not the added إِنْ, not the khabar, not anything else; the negation is not broken by إِلَّا; and لَا's ism must be indefinite.",
         "What happens when a condition fails? They stop governing and a plain mubtada and khabar remain: مَا إِنْ زَيْدٌ قَائِمٌ (إِنْ parted them), مَا قَائِمٌ زَيْدٌ (the khabar came first), مَا زَيْدٌ إِلَّا قَائِمٌ (إِلَّا broke the negation) — the khabar in RAFʿ every time.",
         "May their governed word come before them? Never — مَا and لَا are weak governors, and nothing they govern may stand ahead of them.",
         "What does the engine READ here? The DabtEngine reads مَا before a definite ism and an indefinite predicate as the Ḥijāzī مَا and writes the khabar's naṣb, keeps the khabar in rafʿ once إِنْ, a fronted khabar or إِلَّا appears, writes the single fatḥa on لَا's annexed ism (لَا غُلَامَ رَجُلٍ) and its khabar in rafʿ, and reads the disjoined إِلَّا as لٰكِنَّ with the excepted in naṣb."],
  "tr": ["İllâ NE ZAMAN iki isimde âmildir? MUNKATI' istisnâda — müstesnâ bütünün parçası değildir (câenî'l-kavmu ille'l-himâr): illâ o zaman lâkinne mânâsındadır, ardındaki isim mansûb olur ve bir haber takdir edilir (lâkinne himâran lem yeci').",
         "Lâ NE ZAMAN inne gibi amel eder? Cinsin tamamını nefyettiğinde ve ismi MUZÂF (lâ gulâme racülin) veya muzâfa benzer (lâ hayran min Zeyd) nekre olduğunda, lâ ile isim arasında hiçbir şey yokken.",
         "Leyse'ye benzeyen mâ ve lâ nedir? Mübtedâ ve habere giren ve leyse gibi ismi ref'te bırakıp HABERİ nasb eden nefy harfleri: mâ Zeydün kâimen, lâ racülün hâdıran.",
         "Üç şartı? Onlarla isim arasına hiçbir şey girmez — ne zâid in, ne haber, ne başka bir şey; nefy illâ ile bozulmaz; lâ'nın ismi nekre olmalıdır.",
         "Şart bozulunca ne olur? Amelden düşerler ve düz mübtedâ-haber kalır: mâ in Zeydün kâimün (in araya girdi), mâ kâimün Zeydün (haber öne geçti), mâ Zeydün illâ kâimün (illâ nefyi bozdu) — haber her seferinde REF'te.",
         "Ma'mûlleri onlardan önce gelebilir mi? Asla — mâ ve lâ zayıf âmillerdir, ma'mûlleri önlerine geçemez.",
         "Motor burada neyi OKUR? DabtEngine marife isim ve nekre yüklem önündeki mâ'yı Hicâzî mâ okuyup haberin nasbını yazar, in, mukaddem haber veya illâ görününce haberi ref'te tutar, lâ'nın muzâf ismine tek fetha (lâ gulâme racülin) ve haberine ref' yazar, munkatı' illâ'yı lâkinne okuyup müstesnâyı nasb eder."]
 },
 "plain": {"en": "Three little negations borrow a verb's power: إِلَّا in «except the donkey» works like «but», لَا in «no servant of a man» like إِنَّ, and مَا / لَا in «Zayd is not standing» like لَيْسَ, putting the second noun into naṣb. Put anything between them and their noun, or an إِلَّا after them, and the power is gone.",
           "tr": "Üç küçük olumsuzluk bir fiilin gücünü ödünç alır: «eşek hâriç»teki illâ «fakat» gibi, «bir adamın hiçbir kölesi»ndeki lâ inne gibi, «Zeyd ayakta değil»deki mâ / lâ leyse gibi çalışır ve ikinci ismi nasb eder. Aralarına bir şey girsin ya da ardından illâ gelsin, güç gider."},
 "explanation": {"en": "The first division of the governor in two nouns closes with إِلَّا and لَا: إِلَّا governs only in the disjoined exception, where it carries the sense of لٰكِنَّ, the excepted noun stands in naṣb and a khabar is estimated; لَا of the genus governs like إِنَّ when its ism is an indefinite noun annexed or resembling one annexed, with nothing between them. The second division — مَا and لَا that resemble لَيْسَ — negates and enters upon the mubtada and khabar, putting the khabar in naṣb; they govern only while nothing parts them from the ism (the added إِنْ, the khabar, anything else), the negation is not broken by إِلَّا, and (for لَا) the ism is indefinite; when a condition fails they are ungoverning, and their governed word never precedes them.",
                 "tr": "İki isimdeki âmilin birinci kısmı illâ ve lâ ile kapanır: illâ yalnız munkatı' istisnâda amel eder — lâkinne mânâsındadır, müstesnâ mansûb olur ve bir haber takdir edilir; cins nefyi lâ'sı, ismi muzâf veya muzâfa benzer nekre olup arada bir şey yokken inne gibi amel eder. İkinci kısım — leyse'ye benzeyen mâ ve lâ — nefyeder, mübtedâ ve habere girer ve haberi nasb eder; yalnız isimle aralarına bir şey girmediği (zâid in, haber, başka bir şey), nefy illâ ile bozulmadığı ve (lâ'da) isim nekre olduğu sürece amel ederler; bir şart bozulunca amelsizdirler ve ma'mûlleri asla önlerine geçmez."},
 "examples": [
  {"ar": "جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ، أَيْ: لٰكِنَّ حِمَارًا لَمْ يَجِئْ", "en": "the disjoined exception: إِلَّا as لٰكِنَّ, a khabar estimated", "tr": "munkatı' istisnâ: illâ lâkinne gibi, haber takdir edilir", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "لَا غُلَامَ رَجُلٍ جَالِسٌ عِنْدَنَا", "en": "لَا of the genus with an annexed indefinite ism in naṣb", "tr": "muzâf nekre ismi mansûb cins nefyi lâ'sı", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "مَا زَيْدٌ قَائِمًا، وَلَا رَجُلٌ حَاضِرًا", "en": "مَا and لَا like لَيْسَ: the khabar in naṣb", "tr": "leyse gibi mâ ve lâ: haber mansûb", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "مَا إِنْ زَيْدٌ قَائِمٌ، وَمَا قَائِمٌ زَيْدٌ، وَمَا زَيْدٌ إِلَّا قَائِمٌ", "en": "a condition missing: the khabar stays in rafʿ", "tr": "bir şart eksik: haber ref'te kalır", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "مَا زَيْدٌ إِلَّا قَائِمًا", "right": "مَا زَيْدٌ إِلَّا قَائِمٌ", "why": {"en": "إِلَّا breaks the negation, so مَا no longer governs — the khabar is in rafʿ", "tr": "illâ nefyi bozar, mâ artık amel etmez — haber merfû"}},
  {"wrong": "لَا غُلَامُ رَجُلٍ جَالِسٌ", "right": "لَا غُلَامَ رَجُلٍ جَالِسٌ", "why": {"en": "لَا of the genus puts its annexed ism in naṣb", "tr": "cins nefyi lâ'sı muzâf ismini nasb eder"}},
  {"wrong": "مَا قَائِمًا زَيْدٌ", "right": "مَا قَائِمٌ زَيْدٌ", "why": {"en": "a fronted khabar parts مَا from its ism — no governing, so rafʿ", "tr": "öne geçen haber mâ'yı isminden ayırır — amel yok, ref'"}},
 ],
}
ADD_EN = (" Chapter 6 (print pp. 98-99): the seventh and eighth of the first division — إِلَّا in the disjoined exception, read as لٰكِنَّ with a khabar "
          "estimated (s1), and لَا of the genus with its condition (s2); the second division, مَا and لَا that resemble لَيْسَ, their three conditions, the "
          "three failures and the bar on a fronted maʿmūl (s3-s5). Two readings of the lithograph's transcription: «لكونهما» is read as لِكَوْنِهَا "
          "(إِلَّا alone has the sense of لٰكِنَّ), and «إلا الأحمار» as إِلَّا الْحِمَارَ, the received example.")
ADD_TR = (" Altıncı bab (baskı s. 98-99): birinci kısmın yedinci ve sekizincisi — lâkinne okunup haberi takdir edilen munkatı' istisnâdaki illâ (s1) "
          "ve şartıyla cins nefyi lâ'sı (s2); ikinci kısım, leyse'ye benzeyen mâ ve lâ, üç şartı, üç bozulma ve ma'mûlün öne geçme yasağı (s3-s5). "
          "Taşbaskı transkripsiyonunda iki okuma: «لكونهما» li-kevnihâ okunmuştur (lâkinne mânâsında olan yalnız illâ'dır), «إلا الأحمار» ise alınan "
          "örnek olan ille'l-himâr.")
write_out(6, S, TITLE, ADD_EN, ADD_TR, "pp. 98-99", GLOSS_ADD, notes=(NOTE,),
          related=((LJ, [K]), (ML, [K]), (IS, [K]), ("istithna-mufarragh", [K]), (K1, [K]), ("mawadi-kasr-inna", [K])))
report(6, S, GLOSS_ADD, (NOTE,))
