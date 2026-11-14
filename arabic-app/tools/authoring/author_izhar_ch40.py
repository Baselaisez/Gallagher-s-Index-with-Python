# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 40: the NINTH to THIRTEENTH manṣūb — the khabar of the bāb of كَانَ (as the khabar of the mubtadaʾ; كَانَ alone may be
# dropped on a clue: النَّاسُ مَجْزِيُّونَ بِأَعْمَالِهِمْ إِنْ خَيْرًا فَخَيْرٌ وَإِنْ شَرًّا فَشَرٌّ, four ways allowed); the ism of the bāb of إِنَّ (as the mubtadaʾ, never
# dropped); the ism of لَا of genus-negation (لَا غُلَامَ رَجُلٍ عِنْدَنَا; dropped when the khabar is present: لَا عَلَيْكَ = لَا بَأْسَ عَلَيْكَ); the khabar of مَا and لَا
# likened to لَيْسَ (as the khabar of the mubtadaʾ); the muḍāriʿ entered by a nāṣib (لَنْ يَضْرِبَ). Print p. 137.
#   python3 author_izhar_ch40.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; LNJ = "la-nafiya-lil-jins"; MLM = "ma-la-mushabbaha"; TN = "al-fil-al-tamm-wal-naqis"; FK = "fa-khabar-mubtada"; JMS = "jam-mudhakkar-salim"
K = "al-mansubat-al-tasi-ila-al-thalith-ashar"
K39 = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"; K31 = "al-marfuat-al-khamis-ila-al-tasi"
TITLE = {"ar": "الْمَنْصُوبَاتُ مِنَ التَّاسِعِ إِلَى الثَّالِثَ عَشَرَ: خَبَرُ كَانَ، اسْمُ إِنَّ، اسْمُ لَا، خَبَرُ مَا وَلَا، وَالْمُضَارِعُ الْمَنْصُوبُ", "en": "The ninth to thirteenth manṣūbāt: the khabar of kāna, the ism of inna, the ism of lā, the khabar of mā and lā, and the muḍāriʿ in naṣb", "tr": "Dokuzuncudan on üçüncüye mansûblar: kâne'nin haberi, inne'nin ismi, lâ'nın ismi, mâ ve lâ'nın haberi ve mansûb muzâri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def babi(): return tok("بَابِ", "bab", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the bāb of»", "«bâbının»")
def wayajuz(): return tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb"))
def mubtadai(punct=None): return tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtadaʾ»", "«mübtedânın»", punct=punct)

# ----------- s1 — the ninth: the khabar of kāna
S.append({"id": "s1", "translation": {"en": "And the ninth is the khabar of the bāb of «kāna», and its matter is as the matter of the khabar of the mubtadaʾ;", "tr": "Dokuzuncusu kâne bâbının haberidir; durumu mübtedânın haberinin durumu gibidir;"},
 "tokens": [
  tok("وَالتَّاسِعُ", "tasi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالتَّاسِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the ninth»", "«dokuzuncusu»", segments=wa("التَّاسِعُ", "tasi", "noun")),
  tok("خَبَرُ", "khabar", "noun", [K, MK, ID, KN], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the khabar of» — the khabar.", "«haberi» — haber."),
  babi(),
  tok("كَانَ", "kana", "verb", [K, ID, KN, TN], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«kāna»", "«kâne»", punct="،"),
  tok("وَأَمْرُهُ", "amr", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَأَمْرُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its matter»", "«ve durumu»", segments=[seg("وَ", "wa", "conj"), seg("أَمْرُ", "amr", "noun"), pr3ms()]),
  tok("كَأَمْرِ", "amr", "noun", [K, HJ, ID, MK], "الْكَافُ حَرْفُ جَرٍّ، وَأَمْرِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«as the matter of» — the khabar.", "«… durumu gibi» — haber.", segments=[seg("كَ", "ka", "prep"), seg("أَمْرِ", "amr", "noun")]),
  tok("خَبَرِ", "khabar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the khabar of»", "«haberinin»"),
  mubtadai("،"),
 ]})
# ----------- s2 — kāna alone dropped on a clue
S.append({"id": "s2", "translation": {"en": "and the dropping of «kāna», not of its sisters, is allowed where a clue stands — as in «people are requited by their deeds: if good, then good, and if evil, then evil» — and four ways are allowed in the like of it.", "tr": "karîne bulununca kâne'nin — diğerlerinin değil — hazfi câizdir; «insanlar amelleriyle karşılık görür: hayırsa hayır, şerse şer» gibi; bunun benzerinde dört vecih câizdir."},
 "tokens": [
  wayajuz(),
  tok("حَذْفُ", "hadhf", "noun", [K, FL, ID, MSD, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the dropping of»", "«hazfi»"),
  tok("كَانَ", "kana", "verb", [K, ID, KN, HT], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«kāna»", "«kâne'nin»"),
  tok("دُونَ", "duna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — بِمَعْنَى: لَا.", "«not» — to the exclusion of.", "«dışında» — değil."),
  tok("غَيْرِهِ", "ghayr", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَخَوَاتِهَا.", "«its sisters» — the others of its bāb.", "«diğerleri» — bâbının öbürleri.", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«where stands»", "«bulununca»"),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»", punct="،"),
  nahw(),
  tok("النَّاسُ", "nas", "noun", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«people»", "«insanlar»"),
  tok("مَجْزِيُّونَ", "majzi", "noun", [K, MK, IMF, JMS], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«requited» — the khabar, sound plural.", "«karşılık görürler» — haber, cem-i müzekker-i sâlim."),
  tok("بِأَعْمَالِهِمْ", "amal-deed", "noun", [K, HJ, ID, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَأَعْمَالِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«by their deeds»", "«amelleriyle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("أَعْمَالِ", "amal-deed", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("إِنْ", "in-shartiyya", "part", [K, INS, KN, HT], "حَرْفُ شَرْطٍ — وَكَانَ مَحْذُوفَةٌ بَعْدَهُ: إِنْ كَانَ عَمَلُهُمْ خَيْرًا.", "«if» — kāna dropped after it: إِنْ كَانَ عَمَلُهُمْ خَيْرًا.", "«-sa» — ardında kâne hazfedilmiş: in kâne amelühüm hayran."),
  tok("خَيْرًا", "khayr", "noun", [K, KN, HT], "خَبَرُ كَانَ الْمَحْذُوفَةِ مَنْصُوبٌ.", "«good» — the khabar of the dropped kāna.", "«hayır» — hazfedilmiş kâne'nin haberi."),
  tok("فَخَيْرٌ", "khayr", "noun", [K, FK, MK, INS, HT], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَخَيْرٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فَجَزَاؤُهُمْ خَيْرٌ.", "«then good» — the answer: their requital is good.", "«hayırdır» — cevap: karşılıkları hayırdır.", segments=fa("خَيْرٌ", "khayr", "noun")),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, KN, HT], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if»", "«ve … -sa»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("شَرًّا", "sharr", "noun", [K, KN, HT], "خَبَرُ كَانَ الْمَحْذُوفَةِ مَنْصُوبٌ.", "«evil»", "«şer»"),
  tok("فَشَرٌّ", "sharr", "noun", [K, FK, MK, INS, HT], "الْفَاءُ فِي الْجَوَابِ، وَشَرٌّ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«then evil»", "«şerdir»", punct="،", segments=fa("شَرٌّ", "sharr", "noun")),
  wayajuz(),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("مِثْلِهِ", "mithl", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the like of it»", "«bunun benzerinde»", segments=[seg("مِثْلِ", "mithl", "noun"), pr3msi()]),
  tok("أَرْبَعَةُ", "arbaa", "noun", [K, FL, ID, TMZ], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«four»", "«dört»"),
  tok("أَوْجُهٍ", "wajh", "noun", [K, ID, JT, TMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَصْبُهُمَا، وَرَفْعُهُمَا، وَنَصْبُ الْأَوَّلِ وَرَفْعُ الثَّانِي، وَعَكْسُهُ.", "«ways» — both naṣb, both rafʿ, naṣb then rafʿ, and the reverse.", "«vecih» — ikisi nasb, ikisi ref', ilki nasb ikincisi ref', tersi.", punct="."),
 ]})
# ----------- s3 — the tenth: the ism of inna
S.append({"id": "s3", "translation": {"en": "And the tenth is the ism of the bāb of «inna», and it is like the mubtadaʾ, but its dropping is not allowed.", "tr": "Onuncusu inne bâbının ismidir; mübtedâ gibidir, fakat hazfi câiz değildir."},
 "tokens": [
  tok("وَالْعَاشِرُ", "ashir-tenth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْعَاشِرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the tenth»", "«onuncusu»", segments=wa("الْعَاشِرُ", "ashir-tenth", "noun")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, IN], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the ism of» — the khabar.", "«ismi» — haber."),
  babi(),
  tok("إِنَّ", "inna", "part", [K, ID, IN], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«inna»", "«inne»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("كَالْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "الْكَافُ حَرْفُ جَرٍّ، وَالْمُبْتَدَإِ مَجْرُورٌ — خَبَرٌ.", "«like the mubtadaʾ» — the khabar.", "«mübtedâ gibi» — haber.", punct="،", segments=[seg("كَ", "ka", "prep"), seg("الْمُبْتَدَإِ", "mubtada", "noun")]),
  tok("لٰكِنْ", "lakin", "part", [K, AT], "حَرْفُ اسْتِدْرَاكٍ.", "«but»", "«fakat»"),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«değildir»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, LN, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("حَذْفُهُ", "hadhf", "noun", [K, FL, ID, MSD, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its dropping»", "«hazfi»", punct=".", segments=[seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
 ]})
# ----------- s4 — the eleventh: the ism of lā of genus-negation
S.append({"id": "s4", "translation": {"en": "And the eleventh is the ism of the «lā» that is for the negation of the genus — as in «no servant of a man is with us» — and it may be dropped when the khabar is present, as in «no (harm) upon you», that is, «no harm upon you».", "tr": "On birincisi cins nefyi için olan lâ'nın ismidir — «bizde hiçbir adamın kölesi yoktur» gibi — haber bulununca hazfedilebilir: «lâ aleyke», yani «sana bir beis yok» gibi."},
 "tokens": [
  tok("وَالْحَادِيَ", "hadi-ashar", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْحَادِيَ عَشَرَ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«and the eleventh» — the compound ordinal.", "«on birincisi» — mürekkeb sıra sayısı.", segments=wa("الْحَادِيَ", "hadi-ashar", "noun")),
  tok("عَشَرَ", "ashar", "noun", [K, MK], "جُزْءُ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«-teenth»", "«on bir»"),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, LNJ], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the ism of» — the khabar.", "«ismi» — haber."),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, ID, LNJ], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«lā»", "«lâ»"),
  tok("الَّتِي", "allati", "pron", [K, NA, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ، نَعْتٌ لِلَا.", "«that is»", "«… olan»"),
  tok("لِنَفْيِ", "nafy", "noun", [K, HJ, ID, MSD, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَنَفْيِ مَجْرُورٌ، مُضَافٌ — صِلَةُ الَّتِي.", "«for the negation of»", "«nefyi için»", segments=[seg("لِ", "li", "prep"), seg("نَفْيِ", "nafy", "noun")]),
  tok("الْجِنْسِ", "jins", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the genus»", "«cins»", punct="،"),
  nahw(),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LNJ], "لَفْظٌ مَحْكِيٌّ: نَافِيَةٌ لِلْجِنْسِ.", "«no»", "«hiçbir … yok»"),
  tok("غُلَامَ", "ghulam", "noun", [K, LNJ, ID], "اسْمُ لَا مَنْصُوبٌ لِأَنَّهُ مُضَافٌ.", "«servant of» — the ism of lā in naṣb, being annexed.", "«kölesi» — lâ'nın ismi; muzâf olduğundan mansûb."),
  tok("رَجُلٍ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a man»", "«bir adamın»"),
  tok("عِنْدَنَا", "inda", "noun", [K, MF, ID, LNJ], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — خَبَرُ لَا.", "«with us» — the khabar of lā.", "«bizde» — lâ'nın haberi.", punct="،", segments=[seg("عِنْدَ", "inda", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF, MR, HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الِاسْمُ.", "«it is dropped» — the ism.", "«hazfedilir» — isim."),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«when»", "«… bulununca»"),
  tok("وُجُودِ", "wujud", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the presence of»", "«bulunması»"),
  tok("الْخَبَرِ", "khabar", "noun", [K, ID, LNJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar»", "«haberin»", punct="،"),
  nahw(),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LNJ, HT], "لَفْظٌ مَحْكِيٌّ: نَافِيَةٌ لِلْجِنْسِ، وَاسْمُهَا مَحْذُوفٌ.", "«no» — its ism dropped.", "«yok» — ismi hazfedilmiş."),
  tok("عَلَيْكَ", "ala", "prep", [K, HJ, LNJ], "عَلَى حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«upon you» — the khabar of lā.", "«sana» — lâ'nın haberi.", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":"),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LNJ], "نَافِيَةٌ لِلْجِنْسِ.", "«no»", "«yok»"),
  tok("بَأْسَ", "bas", "noun", [K, LNJ, HT], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ — الْمَحْذُوفُ الْمُقَدَّرُ.", "«harm» — the ism restored.", "«beis» — takdîr edilen isim."),
  tok("عَلَيْكَ", "ala", "prep", [K, HJ, LNJ], "عَلَى حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«upon you»", "«sana»", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), seg("كَ", "pron-2ms", "pron")]),
 ]})
# ----------- s5 — the twelfth: the khabar of mā and lā likened to laysa
S.append({"id": "s5", "translation": {"en": "And the twelfth is the khabar of «mā» and «lā» likened to «laysa», and it is like the khabar of the mubtadaʾ.", "tr": "On ikincisi leyse'ye benzetilen mâ ve lâ'nın haberidir; mübtedânın haberi gibidir."},
 "tokens": [
  tok("وَالثَّانِيَ", "thani", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِيَ عَشَرَ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«and the twelfth»", "«on ikincisi»", segments=wa("الثَّانِيَ", "thani", "noun")),
  tok("عَشَرَ", "ashar", "noun", [K, MK], "جُزْءُ الْعَدَدِ الْمُرَكَّبِ.", "«-teenth»", "«on iki»"),
  tok("خَبَرُ", "khabar", "noun", [K, MK, ID, MLM], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the khabar of» — the khabar.", "«haberi» — haber."),
  tok("مَا", "ma-hijaziyya", "part", [K, ID, MLM], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«mā»", "«mâ»"),
  tok("وَلَا", "la-nafiya", "part", [K, AT, MLM], "الْوَاوُ عَاطِفَةٌ، وَلَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and lā»", "«ve lâ»", segments=wa("لَا", "la-nafiya", "part")),
  tok("الْمُشَبَّهَتَيْنِ", "mushabbah", "noun", [K, NA, MTH, IMF, F2], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«the two likened»", "«benzetilen ikisi»"),
  tok("بِلَيْسَ", "laysa", "verb", [K, HJ, TN], "الْبَاءُ حَرْفُ جَرٍّ، وَلَيْسَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«to laysa»", "«leyse'ye»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("لَيْسَ", "laysa", "verb")]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("مِثْلُ", "mithl", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«like» — the khabar.", "«gibi» — haber."),
  tok("خَبَرِ", "khabar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the khabar of»", "«haberi»"),
  mubtadai("."),
 ]})
# ----------- s6 — the thirteenth: the muḍāriʿ entered by a nāṣib
S.append({"id": "s6", "translation": {"en": "And the thirteenth is the muḍāriʿ entered by one of the nāṣibs — as in «he will not strike».", "tr": "On üçüncüsü nâsıblardan biri başına gelmiş muzâridir — «asla vurmayacak» gibi."},
 "tokens": [
  tok("وَالثَّالِثَ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثَ عَشَرَ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«and the thirteenth»", "«on üçüncüsü»", segments=wa("الثَّالِثَ", "thalith", "noun")),
  tok("عَشَرَ", "ashar", "noun", [K, MK], "جُزْءُ الْعَدَدِ الْمُرَكَّبِ.", "«-teenth»", "«on üç»"),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, MK, JZ], "خَبَرٌ مَرْفُوعٌ.", "«the muḍāriʿ» — the khabar.", "«muzâri» — haber."),
  tok("الدَّاخِلُ", "dakhil", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ.", "«entered»", "«başına gelmiş»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«upon it»", "«onun üzerine»", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("أَحَدُ", "ahad", "noun", [K, FL, ID], "فَاعِلُ الدَّاخِلِ مَرْفُوعٌ، مُضَافٌ.", "«one of» — the doer of the participle.", "«biri» — ism-i fâilin fâili."),
  tok("النَّوَاصِبِ", "nasib", "noun", [K, ID, JT, JZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the nāṣibs»", "«nâsıbların»", punct="،"),
  nahw(),
  tok("لَنْ", "lan", "part", [K, JZ], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "«will not»", "«asla … -meyecek»"),
  tok("يَضْرِبَ", "daraba", "verb", [K, JZ, FL], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«strike» — naṣb by lan.", "«vuracak» — len ile mansûb.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "majzi": G("majzi", "مَجْزِيّ", "ج ز ي", "noun", "requited, recompensed (passive participle)", "karşılığı verilmiş, cezâ görmüş (ism-i mef'ûl)", 4, plural="مَجْزِيُّونَ"),
 "ashir-tenth": G("ashir-tenth", "عَاشِر", "ع ش ر", "noun", "tenth (ordinal)", "onuncu (sıra sayısı)", 2),
 "hadi-ashar": G("hadi-ashar", "حَادِيَ عَشَرَ", "و ح د", "noun", "eleventh (compound ordinal, built on fatḥ)", "on birinci (fetha üzere mebnî mürekkeb sıra sayısı)", 3),
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
print("izhar ch40 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "hadhafa", "daraba", "laysa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَنْصُوبَاتُ التَّاسِعُ إِلَى الثَّالِثَ عَشَرَ: خَبَرُ كَانَ وَحَذْفُهَا، اسْمُ إِنَّ، اسْمُ لَا وَحَذْفُهُ، خَبَرُ مَا وَلَا، الْمُضَارِعُ بَعْدَ النَّاصِبِ", "en": "The ninth to thirteenth manṣūbāt: the khabar of kāna and kāna's dropping, the ism of inna, the ism of lā and its dropping, the khabar of mā and lā, the muḍāriʿ after a nāṣib", "tr": "Dokuzuncudan on üçüncüye mansûblar: kâne'nin haberi ve kâne'nin hazfi, inne'nin ismi, lâ'nın ismi ve hazfi, mâ ve lâ'nın haberi, nâsıbdan sonraki muzâri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات التسعة الأخيرة", "الكافية لابن الحاجب — خبر كان، اسم إنّ، اسم لا", "شرح قطر الندى لابن هشام — النواسخ"],
 "amil": "the thirteen manṣūbāt close: the ninth is the khabar of the bāb of كَانَ, ruled as the khabar of the mubtadaʾ, and كَانَ alone of its bāb may be dropped on a clue (النَّاسُ مَجْزِيُّونَ بِأَعْمَالِهِمْ إِنْ خَيْرًا فَخَيْرٌ وَإِنْ شَرًّا فَشَرٌّ — four ways: both naṣb, both rafʿ, or mixed); the tenth is the ism of the bāb of إِنَّ, like the mubtadaʾ but never dropped; the eleventh the ism of لَا of genus-negation (لَا غُلَامَ رَجُلٍ عِنْدَنَا), dropped when the khabar is present (لَا عَلَيْكَ = لَا بَأْسَ عَلَيْكَ); the twelfth the khabar of مَا and لَا likened to لَيْسَ, like the khabar of the mubtadaʾ; the thirteenth the muḍāriʿ entered by a nāṣib (لَنْ يَضْرِبَ)",
 "question": {
  "en": ["What is the ninth manṣūb? The khabar of the bāb of كَانَ, ruled as the khabar of the mubtadaʾ — single or multiplied, word or clause, definite or indefinite.",
         "May كَانَ be dropped? Yes — كَانَ alone, not its sisters, on a clue: النَّاسُ مَجْزِيُّونَ بِأَعْمَالِهِمْ إِنْ خَيْرًا فَخَيْرٌ وَإِنْ شَرًّا فَشَرٌّ, i.e. إِنْ كَانَ عَمَلُهُمْ خَيْرًا فَجَزَاؤُهُمْ خَيْرٌ.",
         "What are the four ways? خَيْرًا فَخَيْرٌ (naṣb then rafʿ, as printed), خَيْرٌ فَخَيْرٌ, خَيْرًا فَخَيْرًا, خَيْرٌ فَخَيْرًا — the first a dropped kāna's khabar, the second a mubtadaʾ's, each reading restoring a different dropped word.",
         "What is the tenth? The ism of the bāb of إِنَّ — like the mubtadaʾ in all save that it is never dropped.",
         "What is the eleventh, and when is it dropped? The ism of لَا of genus-negation (لَا غُلَامَ رَجُلٍ عِنْدَنَا); it may be dropped when the khabar stands: لَا عَلَيْكَ for لَا بَأْسَ عَلَيْكَ.",
         "What are the twelfth and the thirteenth? The khabar of مَا and لَا likened to لَيْسَ, like the khabar of the mubtadaʾ; and the muḍāriʿ entered by a nāṣib — لَنْ يَضْرِبَ.",
         "What does the engine READ here? The DabtEngine reads the sound-plural khabar after النَّاسُ, the conditional pair إِنْ خَيْرًا فَخَيْرٌ by the author's written cases, the annexed ism of لَا in naṣb with its ẓarf khabar, the cited لَا عَلَيْكَ as the author wrote it, and the muḍāriʿ after لَنْ in naṣb."],
  "tr": ["Dokuzuncu mansûb nedir? Kâne bâbının haberi; mübtedânın haberi gibi — tek veya taaddüd, kelime veya cümle, ma'rife veya nekre.",
         "Kâne hazfedilebilir mi? Evet — yalnız kâne, kardeşleri değil, karîne ile: en-nâsü meczıyyûne bi-a'mâlihim in hayran fe-hayrun ve in şerran fe-şerrun, yani in kâne amelühüm hayran fe-cezâühüm hayrun.",
         "Dört vecih nedir? Hayran fe-hayrun (basıldığı gibi nasb sonra ref'), hayrun fe-hayrun, hayran fe-hayran, hayrun fe-hayran — ilki hazfedilmiş kâne'nin haberi, ikincisi mübtedânın; her okuyuş başka bir hazfedilmiş kelimeyi geri getirir.",
         "Onuncusu? İnne bâbının ismi — hazfedilmemesi dışında her şeyde mübtedâ gibi.",
         "On birincisi ve ne zaman hazfedilir? Cins nefyi lâ'sının ismi (lâ gulâme racülin indenâ); haber dururken hazfedilebilir: lâ be'se aleyke yerine lâ aleyke.",
         "On ikincisi ve on üçüncüsü? Leyse'ye benzetilen mâ ve lâ'nın haberi, mübtedânın haberi gibi; ve başına nâsıb gelmiş muzâri — len yadribe.",
         "Motor burada neyi OKUR? DabtEngine en-nâsü'den sonraki cem-i sâlim haberi; in hayran fe-hayrun şart çiftini yazarın harekeleriyle; lâ'nın muzâf ismini nasbla ve zarf haberiyle; lâ aleyke alıntısını yazarın yazdığı gibi; len'den sonraki muzâriyi nasbla okur."],
 },
 "plain": {"en": "Five more accusatives close the list: the predicate of «kāna» («kāna» itself may be left out: «if good, then good»), the subject of «inna» (never dropped), the subject of «no» denying a whole kind (dropped in «no harm upon you»), the predicate of «mā» and «lā» used like «laysa», and the present-tense verb after «lan».",
           "tr": "Beş mansûb daha listeyi kapatır: kâne'nin yüklemi (kâne'nin kendisi atılabilir: «hayırsa hayır»), inne'nin öznesi (hiç atılmaz), bütün bir cinsi yok sayan lâ'nın öznesi («sana (beis) yok»ta atılır), leyse gibi kullanılan mâ ve lâ'nın yüklemi ve len gibi bir edattan sonraki muzâri fiil."},
 "explanation": {"en": "The ninth manṣūb is the khabar of the bāb of كَانَ, whose matter is that of the khabar of the mubtadaʾ; كَانَ — not its sisters — may be dropped on a clue: النَّاسُ مَجْزِيُّونَ بِأَعْمَالِهِمْ إِنْ خَيْرًا فَخَيْرٌ وَإِنْ شَرًّا فَشَرٌّ, i.e. إِنْ كَانَ عَمَلُهُمْ خَيْرًا فَجَزَاؤُهُمْ خَيْرٌ; four ways are allowed in the like of it — both words in naṣb, both in rafʿ, or either mixed — each reading restoring a different dropped word. The tenth is the ism of the bāb of إِنَّ, like the mubtadaʾ but never dropped. The eleventh is the ism of لَا of genus-negation (لَا غُلَامَ رَجُلٍ عِنْدَنَا), which may be dropped when the khabar is present: لَا عَلَيْكَ for لَا بَأْسَ عَلَيْكَ. The twelfth is the khabar of مَا and لَا likened to لَيْسَ, like the khabar of the mubtadaʾ. The thirteenth is the muḍāriʿ entered by one of the nāṣibs: لَنْ يَضْرِبَ. With these the manṣūbāt are complete and the majrūr follows.",
                 "tr": "Dokuzuncu mansûb kâne bâbının haberidir; durumu mübtedânın haberinin durumudur; kâne — kardeşleri değil — karîne ile hazfedilebilir: en-nâsü meczıyyûne bi-a'mâlihim in hayran fe-hayrun ve in şerran fe-şerrun, yani in kâne amelühüm hayran fe-cezâühüm hayrun; bunun benzerinde dört vecih câizdir — iki kelime de nasb, ikisi de ref' veya karışık — her okuyuş başka bir hazfedilmiş kelimeyi geri getirir. Onuncusu inne bâbının ismidir; mübtedâ gibi, fakat hazfedilmez. On birincisi cins nefyi lâ'sının ismidir (lâ gulâme racülin indenâ); haber bulununca hazfedilebilir: lâ be'se aleyke yerine lâ aleyke. On ikincisi leyse'ye benzetilen mâ ve lâ'nın haberidir; mübtedânın haberi gibidir. On üçüncüsü nâsıblardan biri başına gelmiş muzâridir: len yadribe. Böylece mansûblar tamamlanır, mecrûr gelir."},
 "examples": [
  {"ar": "خَبَرُ بَابِ كَانَ، وَأَمْرُهُ كَأَمْرِ خَبَرِ الْمُبْتَدَإِ", "en": "the ninth: the khabar of kāna", "tr": "dokuzuncu: kâne'nin haberi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "النَّاسُ مَجْزِيُّونَ بِأَعْمَالِهِمْ إِنْ خَيْرًا فَخَيْرٌ وَإِنْ شَرًّا فَشَرٌّ", "en": "kāna dropped on a clue, four ways", "tr": "karîne ile hazfedilen kâne, dört vecih", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "اسْمُ بَابِ إِنَّ، وَهُوَ كَالْمُبْتَدَإِ لٰكِنْ لَا يَجُوزُ حَذْفُهُ", "en": "the tenth: the ism of inna", "tr": "onuncu: inne'nin ismi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "لَا عَلَيْكَ، أَيْ لَا بَأْسَ عَلَيْكَ", "en": "the ism of lā dropped before its khabar", "tr": "haberinden önce hazfedilen lâ'nın ismi", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "خَبَرُ مَا وَلَا الْمُشَبَّهَتَيْنِ بِلَيْسَ", "en": "the twelfth", "tr": "on ikinci", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "لَنْ يَضْرِبَ", "en": "the thirteenth: the muḍāriʿ after a nāṣib", "tr": "on üçüncü: nâsıbdan sonraki muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "إِنَّ قَائِمٌ (the ism of inna dropped)", "right": "إِنَّ زَيْدًا قَائِمٌ", "why": {"en": "the ism of inna, unlike the mubtadaʾ, is never dropped", "tr": "inne'nin ismi mübtedânın aksine hiç hazfedilmez"}},
  {"wrong": "لَا غُلَامُ رَجُلٍ عِنْدَنَا", "right": "لَا غُلَامَ رَجُلٍ عِنْدَنَا", "why": {"en": "the annexed ism of lā of genus-negation takes naṣb", "tr": "cins nefyi lâ'sının muzâf ismi nasb alır"}},
  {"wrong": "لَنْ يَضْرِبُ", "right": "لَنْ يَضْرِبَ", "why": {"en": "the muḍāriʿ entered by a nāṣib takes naṣb — the thirteenth manṣūb", "tr": "nâsıb başına gelen muzâri nasb alır — on üçüncü mansûb"}},
 ],
}
TMZ = "tamyiz"
ADD_EN = (" Chapter 40 (print p. 137): the ninth to thirteenth manṣūbāt — the khabar of kāna (s1) and kāna dropped on a clue with its four ways (s2), the ism of inna never dropped (s3), the ism of lā of genus-negation and its dropping before the khabar (s4), the khabar of mā and lā likened to laysa (s5), the muḍāriʿ after a nāṣib (s6).")
ADD_TR = (" Kırkıncı bab (baskı s. 137): dokuzuncudan on üçüncüye mansûblar — kâne'nin haberi (s1) ve dört vecihle karîne ile hazfedilen kâne (s2), hiç hazfedilmeyen inne'nin ismi (s3), cins nefyi lâ'sının ismi ve haberden önce hazfi (s4), leyse'ye benzetilen mâ ve lâ'nın haberi (s5), nâsıbdan sonraki muzâri (s6).")
write_out(40, S, TITLE, ADD_EN, ADD_TR, "p. 137", GLOSS_ADD, notes=(NOTE,),
          related=((K39, [K]), (K31, [K]), (KN, [K]), (IN, [K]), (LNJ, [K]), (MLM, [K]), (JZ, [K]), (HT, [K])))
report(40, S, GLOSS_ADD, (NOTE,))
