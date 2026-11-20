# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 17: the MAʿNAWĪ governor — what the tongue has no share in, a sense known by the heart —
# which is two: the raiser of the mubtada and the khabar (their being stripped of the lafẓī governors for the sake of the predication:
# زَيْدٌ قَائِمٌ) and the raiser of the muḍāriʿ (its standing by itself in the place of a noun: زَيْدٌ يَضْرِبُ — يَضْرِبُ stands where
# ضَارِبٌ would — and that standing is only when it is stripped of the nāṣibs and the jāzims). "So the sum of the governors we have
# mentioned is SIXTY" — the close of the first bāb, the governors. Print p. 115.
#   python3 author_izhar_ch17.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-amil-al-manawi"
K16 = "mana-al-fil-wa-asma-al-afal"
TITLE = {"ar": "الْعَامِلُ الْمَعْنَوِيُّ وَمَجْمُوعُ الْعَوَامِلِ", "en": "The maʿnawī governor, and the sum of the governors", "tr": "Mânevî âmil ve âmillerin toplamı"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; F5 = "form-v-verbs"; MSD = "masdar"; LN = "la-nafiya"; JT = "jam-taksir"; JMS = "jam-mudhakkar-salim"; ISH = "asma-al-ishara"; MQ = "ism-maqsur-manqus"; AQ = "al-amil-wa-aqsamuh"; MR = "mudari-marfu"; MJZ = "nawasib-wa-jawazim-al-mudari"; MAW = "ism-mawsul"; JS = "jumla-sifa"; QSR = "qasr"; MM = "maful-mutlaq"

# ----------- s1 — the maʿnawī governor: no share for the tongue; two of them
S.append({"id": "s1", "translation": {"en": "And the MAʿNAWĪ governor is what the tongue has no share in; it is only a sense known by the heart — and it is two.", "tr": "MÂNEVÎ ÂMİL, dilin kendisinde bir payı olmayandır; o ancak kalple bilinen bir mânâdır — ve ikidir."},
 "tokens": [
  tok("وَالْعَامِلُ", "amil-governor", "noun", [K, AT, MK, AQ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the governor» — the mubtada.", "«ve âmil» — mübtedâ.", segments=wa("الْعَامِلُ", "amil-governor", "noun")),
  tok("الْمَعْنَوِيُّ", "manawi", "noun", [K, NA, AQ], "نَعْتٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى الْمَعْنَى.", "«of the sense» — a naʿt: the nisba of maʿnā.", "«mânevî» — na't: mânâya nisbet."),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber."),
  tok("لَا", "la-nafiya", "part", [K, LN, MAW], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MAW], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِلَةٌ.", "«there is» — kāna, the relative clause.", "«olmaz» — kâne, sıla."),
  tok("لِلِّسَانِ", "lisan", "noun", [K, HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَاللِّسَانِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُ مُقَدَّمٌ.", "«for the tongue» — the fronted khabar of kāna.", "«dil için» — kâne'nin öne alınmış haberi.", segments=[seg("لِ", "li", "prep"), seg("اللِّسَانِ", "lisan", "noun")]),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«in it» — the returning pronoun.", "«onda» — âid.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("حَظٌّ", "hazz", "noun", [K, KN], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ — نَصِيبٌ مِنَ النُّطْقِ.", "«a share» — the delayed ism of kāna: a share of the utterance.", "«bir pay» — kâne'nin sonraya bırakılmış ismi: telaffuzdan bir pay.", punct="،"),
  tok("وَإِنَّمَا", "innama", "part", [K, AT, QSR], "الْوَاوُ عَاطِفَةٌ، وَإِنَّمَا أَدَاةُ حَصْرٍ: إِنَّ الْمَكْفُوفَةُ بِمَا.", "«and only» — the restricting innamā.", "«ve ancak» — hasr edatı innemâ.", segments=wa("إِنَّمَا", "innama", "part")),
  tok("هُوَ", "huwa", "pron", [K, MK], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«it» — the mubtada.", "«o» — mübtedâ."),
  tok("مَعْنًى", "mana", "noun", [K, MK, MQ], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمٌ مَقْصُورٌ مُنَوَّنٌ.", "«a sense» — the khabar: the maqṣūr noun with tanwīn.", "«bir mânâ» — haber: tenvinli maksûr isim."),
  tok("يُعْرَفُ", "arafa", "verb", [K, NA, NF, JS], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ نَعْتٌ لِمَعْنًى.", "«known» — the ṣifa clause of «a sense».", "«bilinen» — mânâ'nın sıfat cümlesi."),
  tok("بِالْقَلْبِ", "qalb", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْقَلْبِ مَجْرُورٌ.", "«by the heart»", "«kalple»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْقَلْبِ", "qalb", "noun")]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("اثْنَانِ", "ithnan", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى.", "«two» — the khabar, declined like the dual.", "«iki» — haber, tesniyeye mülhak.", punct="."),
 ]})
# ----------- s2 — the first: the raiser of the mubtada and the khabar
S.append({"id": "s2", "translation": {"en": "The first is the raiser of the mubtada and the khabar, and that is being stripped of the lafẓī governors for the sake of the predication, as in «Zayd is standing».", "tr": "İlki mübtedâ ile haberin râfi'idir; o da isnâd için lafzî âmillerden soyunmuş olmaktır, «Zeyd ayaktadır» gibi."},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«ilki» — mübtedâ."),
  tok("رَافِعُ", "rafi-raiser", "noun", [K, MK, ID, IFA], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ فَاعِلِ رَفَعَ.", "«the raiser of» — the khabar.", "«râfi'i» — haber."),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID, MK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — هَمْزَتُهُ عَلَى نَبْرَةٍ لِكَسْرِهَا.", "«the mubtada» — its hamza on the tooth for the kasra.", "«mübtedâ» — kesresi için hemzesi dişte."),
  tok("وَالْخَبَرِ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar»", "«ve haber»", punct="،", segments=wa("الْخَبَرِ", "khabar-predicate", "noun")),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("التَّجَرُّدُ", "tajarrud", "noun", [K, MK, MSD, F5, AQ], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ تَجَرَّدَ: الْخُلُوُّ.", "«being stripped» — the khabar: the maṣdar of «to be stripped».", "«soyunmuşluk» — haber: tecerrüd mastarı."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("الْعَوَامِلِ", "amil-governor", "noun", [K, HJ, JT, AQ], "مَجْرُورٌ بِعَنْ — جَمْعُ عَامِلٍ.", "«the governors» — the broken plural.", "«âmiller» — cem'-i mükesser."),
  tok("اللَّفْظِيَّةِ", "lafzi", "noun", [K, NA, AQ], "نَعْتٌ مَجْرُورٌ — مُؤَنَّثُ اللَّفْظِيِّ لِأَنَّ الْجَمْعَ غَيْرُ الْعَاقِلِ يُعَامَلُ مُعَامَلَةَ الْمُفْرَدَةِ.", "«lafẓī» — feminine singular: the plural of non-rational nouns takes it.", "«lafzî» — müfred müennes: gayr-i âkil cem' öyle alır."),
  tok("لِأَجْلِ", "ajl", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَأَجْلِ مَجْرُورٌ، مُضَافٌ — لِلتَّعْلِيلِ.", "«for the sake of»", "«… için»", segments=[seg("لِ", "li", "prep"), seg("أَجْلِ", "ajl", "noun")]),
  tok("الْإِسْنَادِ", "isnad", "noun", [K, ID, MSD, MK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — إِسْنَادُ الْخَبَرِ إِلَى الْمُبْتَدَإِ.", "«the predication» — of the khabar to the mubtada.", "«isnâd» — haberin mübtedâya isnâdı.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=":"),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, AQ], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ بِالتَّجَرُّدِ.", "«Zayd» — the mubtada, raised by the stripping.", "«Zeyd» — tecerrüdle merfû mübtedâ."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA, AQ], "خَبَرٌ مَرْفُوعٌ بِالتَّجَرُّدِ — اسْمُ فَاعِلِ قَامَ.", "«standing» — the khabar, raised by the stripping.", "«ayakta» — tecerrüdle merfû haber.", punct="."),
 ]})
# ----------- s3 — the second: the raiser of the muḍāriʿ
S.append({"id": "s3", "translation": {"en": "And the second is the raiser of the muḍāriʿ verb, and that is its standing, by itself, in the place of a noun — as in «Zayd strikes»: «strikes» stands in the place of «striking».", "tr": "İkincisi muzâri fiilin râfi'idir; o da fiilin kendiliğinden ismin yerinde bulunmasıdır — «Zeyd vurur» gibi: «vurur», «vuran»ın yerinde bulunur."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«and the second» — the mubtada.", "«ikincisi» — mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("رَافِعُ", "rafi-raiser", "noun", [K, MK, ID, IFA], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the raiser of» — the khabar.", "«râfi'i» — haber."),
  tok("الْفِعْلِ", "fil", "noun", [K, ID, MR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiilin»"),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, NA, MR], "نَعْتٌ مَجْرُورٌ.", "«muḍāriʿ» — a naʿt.", "«muzâri» — na't.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("وُقُوعُهُ", "wuqu", "noun", [K, MK, ID, MSD, MR], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ وَقَعَ.", "«its standing» — the khabar: the maṣdar of «to fall, to occur».", "«bulunması» — haber: vakaa mastarı.", segments=[seg("وُقُوعُ", "wuqu", "noun"), pr3ms()]),
  tok("بِنَفْسِهِ", "nafs", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَنَفْسِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بِلَا وَاسِطَةِ حَرْفٍ.", "«by itself» — without a particle between.", "«kendiliğinden» — arada bir harf olmadan.", segments=[seg("بِ", "bi", "prep"), seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  tok("مَوْقِعَ", "mawqi", "noun", [K, MF, ID, MR], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ — اسْمُ مَكَانٍ مِنْ وَقَعَ.", "«in the place of» — the ẓarf of place: the noun of place from «to fall».", "«… yerinde» — mekân zarfı: vakaa'dan ism-i mekân."),
  tok("الِاسْمِ", "ism", "noun", [K, ID, MR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a noun»", "«ismin»", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=":"),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, MR], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("يَضْرِبُ", "daraba", "verb", [K, MK, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِوُقُوعِهِ مَوْقِعَ الِاسْمِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«strikes» — raised for standing where a noun would; the khabar clause.", "«vurur» — ismin yerinde bulunduğu için merfû; haber cümlesi.", punct="،"),
  tok("فَيَضْرِبُ", "daraba", "verb", [K, AT, MK, MR, HT], "الْفَاءُ لِلتَّفْرِيعِ، وَيَضْرِبُ لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْمَقْصُودُ لَفْظُهُ.", "«so «strikes»» — the cited word as the mubtada.", "«o hâlde «vurur»» — lafzı kastedilen, mübtedâ.", segments=fa("يَضْرِبُ", "daraba", "verb")),
  tok("وَاقِعٌ", "waqia", "noun", [K, MK, IFA, MR], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ وَقَعَ.", "«standing» — the khabar: the ism fāʿil of «to fall».", "«bulunan» — haber: vakaa'nın ism-i fâili."),
  tok("مَوْقِعَ", "mawqi", "noun", [K, MF, ID, MR], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«in the place of»", "«… yerinde»"),
  tok("ضَارِبٍ", "darib", "noun", [K, ID, IFA, MR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْفَاعِلِ الَّذِي يُشْبِهُهُ الْمُضَارِعُ.", "«striking» — the ism fāʿil the muḍāriʿ resembles.", "«vuran» — muzârinin benzediği ism-i fâil.", punct="."),
 ]})
# ----------- s4 — that standing only when stripped of the nāṣibs and the jāzims
S.append({"id": "s4", "translation": {"en": "And that standing is only when it is stripped of the nāṣibs and the jāzims.", "tr": "Bu yerinde bulunma, ancak nasb ve cezm edenlerden soyunduğunda olur."},
 "tokens": [
  tok("وَذٰلِكَ", "dhalika", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve bu» — mübtedâ.", segments=wa("ذٰلِكَ", "dhalika", "pron")),
  tok("الْوُقُوعُ", "wuqu", "noun", [K, "badal", MSD, MR], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ.", "«standing» — a badal of the demonstrative.", "«bulunma» — ism-i işâretin bedeli."),
  tok("إِنَّمَا", "innama", "part", [K, QSR], "أَدَاةُ حَصْرٍ.", "«only»", "«ancak»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MK], "فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — بِمَعْنَى يَحْصُلُ؛ وَالْجُمْلَةُ خَبَرٌ.", "«happens» — the complete kāna: «comes about»; the khabar clause.", "«olur» — tam kâne: «gerçekleşir»; haber cümlesi."),
  tok("إِذَا", "idha", "part", [K, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the conditional time-adverb.", "«-diğinde» — şart mânâlı zaman zarfı."),
  tok("تَجَرَّدَ", "tajarrada", "verb", [K, FL, F5, MR], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْمُضَارِعُ.", "«it is stripped» — the muḍāriʿ.", "«soyunursa» — muzâri."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("النَّوَاصِبِ", "nasib", "noun", [K, HJ, JT, MJZ], "مَجْرُورٌ بِعَنْ — جَمْعُ نَاصِبٍ: أَنْ وَأَخَوَاتُهَا.", "«the nāṣibs» — an and its sisters.", "«nâsıblar» — en ve kardeşleri."),
  tok("وَالْجَوَازِمِ", "jazim", "noun", [K, AT, JT, MJZ], "الْوَاوُ عَاطِفَةٌ، وَالْجَوَازِمِ مَعْطُوفٌ مَجْرُورٌ — جَمْعُ جَازِمٍ: لَمْ وَأَخَوَاتُهَا.", "«and the jāzims» — lam and its sisters.", "«ve câzimler» — lem ve kardeşleri.", punct=".", segments=wa("الْجَوَازِمِ", "jazim", "noun")),
 ]})
# ----------- s5 — the sum: sixty
S.append({"id": "s5", "translation": {"en": "So the sum of the governors we have mentioned is sixty.", "tr": "Böylece zikrettiğimiz âmillerin toplamı altmıştır."},
 "tokens": [
  tok("فَمَجْمُوعُ", "majmu", "noun", [K, AT, MK, ID, IMF], "الْفَاءُ لِلتَّفْرِيعِ، وَمَجْمُوعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ مَفْعُولِ جَمَعَ.", "«so the sum of» — the mubtada.", "«böylece toplamı» — mübtedâ.", segments=fa("مَجْمُوعُ", "majmu", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«what»", "«… şeylerin»"),
  tok("ذَكَرْنَا", "dhakara", "verb", [K, FL, MAW], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ — صِلَةُ مَا، وَالْعَائِدُ مَحْذُوفٌ: ذَكَرْنَاهُ.", "«we have mentioned» — the relative clause; the returning pronoun dropped.", "«zikrettiğimiz» — sıla; âid hazfedilmiş.", segments=[seg("ذَكَرْ", "dhakara", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("الْعَوَامِلِ", "amil-governor", "noun", [K, HJ, JT, AQ], "مَجْرُورٌ بِمِنْ — جَمْعُ عَامِلٍ.", "«the governors»", "«âmiller»"),
  tok("سِتُّونَ", "sittun", "noun", [K, MK, JMS], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — ٤٩ لَفْظِيًّا سَمَاعِيًّا، ٩ لَفْظِيَّةً قِيَاسِيَّةً، ٢ مَعْنَوِيَّانِ.", "«sixty» — the khabar: 49 samāʿī, 9 qiyāsī, 2 maʿnawī.", "«altmış» — haber: 49 semâî, 9 kıyâsî, 2 mânevî.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

NEW = {
 "tajarrud": G("tajarrud", "تَجَرُّد", "ج ر د", "noun", "being stripped, bareness (maṣdar of تَجَرَّدَ) — in nahw: a word's freedom from lafẓī governors", "tecerrüd, soyunmuşluk (tecerrede'nin mastarı) — nahivde: lafzî âmillerden hâlî oluş", 4, form="V"),
 "mawqi": G("mawqi", "مَوْقِع", "و ق ع", "noun", "place, position (the noun of place of وَقَعَ)", "mevki, yer (vakaa'nın ism-i mekânı)", 3),
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
print("izhar ch17 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "arafa", "daraba", "tajarrada", "dhakara") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْعَامِلُ الْمَعْنَوِيُّ: رَافِعُ الْمُبْتَدَإِ وَالْخَبَرِ وَرَافِعُ الْمُضَارِعِ", "en": "The maʿnawī governor: what raises the mubtada and the khabar, and what raises the muḍāriʿ", "tr": "Mânevî âmil: mübtedâ ile haberi ve muzâriyi ref' eden"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العامل المعنوي", "الكافية لابن الحاجب — رافع المبتدأ والخبر", "العوامل المائة للجرجاني — العوامل المعنوية"],
 "amil": "الْعَامِلُ الْمَعْنَوِيُّ — a governor the tongue has no share in: the stripping of the mubtada and the khabar from lafẓī governors for the sake of the predication raises them both (زَيْدٌ قَائِمٌ); the muḍāriʿ's standing by itself in a noun's place raises it (زَيْدٌ يَضْرِبُ), and only while it is free of the nāṣibs and the jāzims; with these two the governors are sixty",
 "question": {
  "en": ["What is the maʿnawī governor? A governor the tongue has no share in — not a word but a sense known by the heart. There are two.",
         "What raises the mubtada and the khabar? Their being stripped of the lafẓī governors for the sake of the predication: in زَيْدٌ قَائِمٌ nothing spoken governs either word; the bare predication raises both.",
         "What raises the muḍāriʿ? Its standing, by itself, in the place of a noun: in زَيْدٌ يَضْرِبُ the verb stands where ضَارِبٌ would, so it takes the noun's rafʿ.",
         "When does that standing hold? Only while the verb is stripped of the nāṣibs (أَنْ and its sisters) and the jāzims (لَمْ and its sisters): once لَنْ or لَمْ enters, the lafẓī governor takes over.",
         "How many governors has the Iẓhār counted? Sixty — forty-nine samāʿī (the letters and the frozen verbs of chapters 1–7), nine qiyāsī (the verb, the ism fāʿil, the ism mafʿūl, the ṣifa mushabbaha, the ism tafḍīl, the maṣdar, the muḍāf, the complete vague noun, the sense of the verb) and these two maʿnawī. The first bāb, the governors, ends here.",
         "What does the engine READ here? The DabtEngine raises a bare mubtada and its khabar by the predication alone, raises a muḍāriʿ that no nāṣib or jāzim precedes, and lets لَنْ and لَمْ take it back."],
  "tr": ["Mânevî âmil nedir? Dilin kendisinde payı olmayan bir âmil — bir kelime değil, kalple bilinen bir mânâ. İki tanedir.",
         "Mübtedâ ile haberi ne ref' eder? İsnâd için lafzî âmillerden soyunmuş olmaları: Zeydün kâimün'de söylenen hiçbir şey iki kelimede amel etmez; yalın isnâd ikisini de ref' eder.",
         "Muzâriyi ne ref' eder? Kendiliğinden ismin yerinde bulunması: Zeydün yadribu'da fiil, dâribün'ün yerinde durur; bu yüzden ismin ref'ini alır.",
         "Bu yerinde bulunma ne zaman geçerlidir? Ancak fiil nâsıblardan (en ve kardeşleri) ve câzimlerden (lem ve kardeşleri) soyunmuşken: len veya lem girdiğinde lafzî âmil devralır.",
         "İzhâr kaç âmil saydı? Altmış — kırk dokuz semâî (1–7. babların harfleri ve câmid fiilleri), dokuz kıyâsî (fiil, ism-i fâil, ism-i mef'ûl, sıfat-ı müşebbehe, ism-i tafdîl, mastar, muzâf, mübhem tâm isim, mana-yı fiil) ve bu iki mânevî. Birinci bab, âmiller, burada biter.",
         "Motor burada neyi OKUR? DabtEngine yalın mübtedâ ile haberini yalnız isnâdla ref' eder, önünde nâsıb veya câzim olmayan muzâriyi ref' eder ve len ile lem'in onu geri almasına izin verir."],
 },
 "plain": {"en": "Not every governor is a word. «Zayd is standing» has no particle or verb to raise its two nouns: saying one thing about another raises them. A present verb standing where a noun could — «Zayd strikes» — is raised the same silent way, until «will not» or «did not» steps in front. With these two the count reaches sixty.",
           "tr": "Her âmil bir kelime değildir. «Zeyd ayaktadır»da iki ismi ref' edecek edat ya da fiil yoktur: bir şeyi bir şey hakkında söylemek onları ref' eder. İsmin yerinde duran muzâri — «Zeyd vurur» — aynı sessiz yolla ref' edilir; önüne «-meyecek» veya «-medi» girene dek. Bu ikisiyle sayı altmışa ulaşır."},
 "explanation": {"en": "The maʿnawī governor is what the tongue has no share in; it is only a sense known by the heart, and it is two. The first is the raiser of the mubtada and the khabar: their being stripped of the lafẓī governors for the sake of the predication, as in زَيْدٌ قَائِمٌ. The second is the raiser of the muḍāriʿ verb: its standing, by itself, in the place of a noun, as in زَيْدٌ يَضْرِبُ, where يَضْرِبُ stands where ضَارِبٌ would; and that standing holds only when the verb is stripped of the nāṣibs and the jāzims. So the sum of the governors the Iẓhār has mentioned is sixty: forty-nine samāʿī, nine qiyāsī and two maʿnawī.",
                 "tr": "Mânevî âmil, dilin kendisinde payı olmayandır; o ancak kalple bilinen bir mânâdır ve ikidir. İlki mübtedâ ile haberin râfi'idir: isnâd için lafzî âmillerden soyunmuş olmaları, Zeydün kâimün gibi. İkincisi muzâri fiilin râfi'idir: kendiliğinden ismin yerinde bulunması, Zeydün yadribu gibi; yadribu, dâribün'ün yerinde durur; bu yerinde bulunma ancak fiil nâsıb ve câzimlerden soyunmuşken geçerlidir. Böylece İzhâr'ın zikrettiği âmillerin toplamı altmıştır: kırk dokuz semâî, dokuz kıyâsî ve iki mânevî."},
 "examples": [
  {"ar": "زَيْدٌ قَائِمٌ", "en": "the mubtada and the khabar raised by the stripping", "tr": "tecerrüdle merfû mübtedâ ve haber", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "زَيْدٌ يَضْرِبُ — فَيَضْرِبُ وَاقِعٌ مَوْقِعَ ضَارِبٍ", "en": "the muḍāriʿ raised for standing in a noun's place", "tr": "ismin yerinde bulunduğu için merfû muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "إِنَّمَا يَكُونُ إِذَا تَجَرَّدَ عَنِ النَّوَاصِبِ وَالْجَوَازِمِ", "en": "the condition of that standing", "tr": "bu bulunmanın şartı", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "فَمَجْمُوعُ مَا ذَكَرْنَا مِنَ الْعَوَامِلِ سِتُّونَ", "en": "the count that closes the first bāb", "tr": "birinci babı kapatan sayı", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدًا قَائِمٌ", "right": "زَيْدٌ قَائِمٌ", "why": {"en": "nothing spoken governs the mubtada; the predication raises it", "tr": "mübtedâda söylenen hiçbir şey amel etmez; isnâd onu ref' eder"}},
  {"wrong": "زَيْدٌ يَضْرِبَ", "right": "زَيْدٌ يَضْرِبُ", "why": {"en": "a muḍāriʿ free of nāṣib and jāzim is raised by standing in a noun's place", "tr": "nâsıb ve câzimden hâlî muzâri, ismin yerinde durmakla merfûdur"}},
  {"wrong": "لَنْ يَضْرِبُ", "right": "لَنْ يَضْرِبَ", "why": {"en": "once a nāṣib enters, the maʿnawī raiser withdraws", "tr": "nâsıb girince mânevî râfi' çekilir"}},
 ],
}
ADD_EN = (" Chapter 17 (print p. 115): the maʿnawī governor — no share for the tongue, a sense known by the heart, two of them (s1); the raiser of the mubtada and the khabar: the stripping for the predication (s2); the raiser of the muḍāriʿ: its standing in a noun's place (s3), only while free of the nāṣibs and the jāzims (s4); the sum of the governors, sixty — the close of the first bāb (s5).")
ADD_TR = (" On yedinci bab (baskı s. 115): mânevî âmil — dilin payı yok, kalple bilinen mânâ, iki tane (s1); mübtedâ ile haberin râfi'i: isnâd için tecerrüd (s2); muzârinin râfi'i: ismin yerinde bulunması (s3), ancak nâsıb ve câzimlerden hâlîyken (s4); âmillerin toplamı altmış — birinci babın sonu (s5).")
write_out(17, S, TITLE, ADD_EN, ADD_TR, "p. 115", GLOSS_ADD, notes=(NOTE,),
          related=((AQ, [K]), (MR, [K]), (MJZ, [K]), (MK, [K]), (K16, [K])))
report(17, S, GLOSS_ADD, (NOTE,))
