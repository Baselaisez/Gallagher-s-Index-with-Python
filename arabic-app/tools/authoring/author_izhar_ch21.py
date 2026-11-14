# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 21: the governed word is of two sorts — governed in its own right and governed by following;
# the first has four divisions: marfūʿ, manṣūb, majrūr, majzūm. The MARFŪʿ are nine: the first the DOER — what a complete active verb,
# or its like, is predicated of (ضَرَبَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ، هَيْهَاتَ زَيْدٌ); the second the DEPUTY DOER — what a complete passive
# verb, or what has its sense, is predicated of (ضُرِبَ زَيْدٌ، أَمَضْرُوبٌ الزَّيْدَانِ). Both are nouns or read as nouns — save that the
# deputy may be a jarr phrase (مُرَّ بِزَيْدٍ); their governor must stay singular and masculine; they never precede it, and are never
# both dropped save with the maṣdar. Print pp. 121–122.
#   python3 author_izhar_ch21.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-marfuat-al-fail-wa-naibuh"
K20 = "mawadi-irab-al-jumla"
TITLE = {"ar": "الْمَرْفُوعَاتُ: الْفَاعِلُ وَنَائِبُ الْفَاعِلِ", "en": "The marfūʿāt: the doer and the deputy doer", "tr": "Merfûlar: fâil ve nâib-i fâil"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; MSD = "masdar"; LN = "la-nafiya"; IN = "inna-wa-akhawatuha"; BD = "badal"; JT = "jam-taksir"; ISH = "asma-al-ishara"; MQ = "ism-maqsur-manqus"; MR = "mudari-marfu"; MAW = "ism-mawsul"; JS = "jumla-sifa"; MM = "maful-mutlaq"
KK = "al-kalima-wal-kalam"; MH = "mahall-al-majrur"; TM = "tamyiz"; IST = "al-istifham"; MST = "istithna"; IFL = "ism-fil"; MNF = "mana-al-fil"; NSB = "ism-mansub"; TB = "al-tawabi" if False else "atf-nasaq"; AQ = "al-amil-wa-aqsamuh"; TRT = "tartib-al-jumla" if False else "fail"; IMM = "imal-al-masdar"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)

# ----------- s1 — the governed in its own right and by following
S.append({"id": "s1", "translation": {"en": "Then the governed word is of two sorts: governed in its own right, and governed by following.", "tr": "Sonra ma'mûl iki türlüdür: asâleten ma'mûl ve tebaiyyeten ma'mûl."},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي — هُنَا لِلِانْتِقَالِ.", "«then» — moving on.", "«sonra» — geçiş."),
  tok("الْمَعْمُولُ", "mamul", "noun", [K, MK, IMF], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the governed word» — the mubtada.", "«ma'mûl» — mübtedâ."),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the khabar.", "«üzere» — haber."),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MTH], "مَجْرُورٌ بِعَلَى بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two sorts»", "«iki tür»", punct=":"),
  tok("مَعْمُولٌ", "mamul", "noun", [K, MK, HT, IMF], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ: أَحَدُهُمَا مَعْمُولٌ.", "«governed» — the khabar of a dropped «one of them».", "«ma'mûl» — hazfedilmiş «biri»nin haberi."),
  tok("بِالْأَصَالَةِ", "asala-origin", "noun", [K, HJ, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَالْأَصَالَةِ مَجْرُورٌ — مَعْمُولٌ لِذَاتِهِ.", "«in its own right»", "«asâleten»", segments=[seg("بِ", "bi", "prep"), seg("الْأَصَالَةِ", "asala-origin", "noun")]),
  tok("وَمَعْمُولٌ", "mamul", "noun", [K, AT, MK, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَعْمُولٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and governed»", "«ve ma'mûl»", segments=wa("مَعْمُولٌ", "mamul", "noun")),
  tok("بِالتَّبَعِيَّةِ", "tabaiyya", "noun", [K, HJ, NSB], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّبَعِيَّةِ مَجْرُورٌ — التَّوَابِعُ.", "«by following» — the followers.", "«tebaiyyeten» — tevâbi.", punct="."),
 ]})
# ----------- s2 — the first: four divisions
S.append({"id": "s2", "translation": {"en": "The first is of four divisions: marfūʿ, manṣūb, majrūr and majzūm.", "tr": "İlki dört kısımdır: merfû, mansûb, mecrûr ve meczûm."},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«ilki» — mübtedâ."),
  tok("أَرْبَعَةُ", "arbaa", "noun", [K, MK, ID, TM], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«four» — the khabar.", "«dört» — haber."),
  tok("أَقْسَامٍ", "aqsam", "noun", [K, ID, JT, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَمْيِيزُ الْعَدَدِ.", "«divisions»", "«kısım»", punct=":"),
  tok("مَرْفُوعٌ", "marfu", "noun", [K, MK, HT, IMF], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ: أَحَدُهَا مَرْفُوعٌ.", "«marfūʿ»", "«merfû»"),
  tok("وَمَنْصُوبٌ", "mansub", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَنْصُوبٌ مَعْطُوفٌ مَرْفُوعٌ.", "«manṣūb»", "«mansûb»", segments=wa("مَنْصُوبٌ", "mansub", "noun")),
  tok("وَمَجْرُورٌ", "majrur", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَجْرُورٌ مَعْطُوفٌ مَرْفُوعٌ.", "«majrūr»", "«mecrûr»", segments=wa("مَجْرُورٌ", "majrur", "noun")),
  tok("وَمَجْزُومٌ", "majzum", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَجْزُومٌ مَعْطُوفٌ مَرْفُوعٌ.", "«majzūm»", "«meczûm»", punct=".", segments=wa("مَجْزُومٌ", "majzum", "noun")),
 ]})
# ----------- s3 — the marfūʿ are nine; the first, the doer
S.append({"id": "s3", "translation": {"en": "As for the marfūʿ, they are nine. The first is the doer, and it is what the complete active verb, or what resembles it, is predicated of — as in «Zayd struck», «are the two Zayds standing?» and «far is Zayd!».", "tr": "Merfûa gelince dokuzdur. İlki fâildir; o, tam ma'lûm fiilin veya ona benzeyenin isnâd edildiği şeydir — «Zeyd vurdu», «iki Zeyd ayakta mı?» ve «Zeyd uzaktır!» gibi."},
 "tokens": [
  tok("أَمَّا", "amma", "part", [K, AT], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»"),
  tok("الْمَرْفُوعُ", "marfu", "noun", [K, MK, IMF], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the marfūʿ» — the mubtada.", "«merfû» — mübtedâ."),
  tok("فَتِسْعَةٌ", "tisa", "noun", [K, MK], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَتِسْعَةٌ خَبَرٌ مَرْفُوعٌ.", "«nine» — the khabar after ammā's fāʾ.", "«dokuzdur» — emmâ'nın fâsından sonra haber.", punct=".", segments=fa("تِسْعَةٌ", "tisa", "noun")),
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«ilki» — mübtedâ."),
  tok("الْفَاعِلُ", "fail-doer", "noun", [K, MK, FL], "خَبَرٌ مَرْفُوعٌ.", "«the doer» — the khabar.", "«fâil» — haber.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… şey» — haber."),
  tok("أُسْنِدَ", "asnada", "verb", [K, NF, F4, MAW], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةُ مَا.", "«is predicated» — the relative clause.", "«isnâd edildi» — sıla."),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, MAW], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«of it» — the returning pronoun.", "«ona» — âid.", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("الْفِعْلُ", "fil", "noun", [K, NF, KK], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the verb» — the deputy doer.", "«fiil» — nâib-i fâil."),
  tok("التَّامُّ", "tamm", "noun", [K, NA, KN], "نَعْتٌ مَرْفُوعٌ — لَا النَّاقِصُ كَكَانَ.", "«complete» — not deficient like kāna.", "«tam» — kâne gibi nâkıs değil."),
  tok("الْمَعْلُومُ", "malum", "noun", [K, NA, IMF], "نَعْتٌ ثَانٍ مَرْفُوعٌ — الْمَبْنِيُّ لِلْفَاعِلِ.", "«active» — a second naʿt: built for the doer.", "«ma'lûm» — ikinci na't."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَا", "ma-mawsula", "pron", [K, AT, MAW], "اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى الْفِعْلُ فِي مَحَلِّ رَفْعٍ.", "«what»", "«… şey»"),
  tok("شَابَهَهُ", "shabaha", "verb", [K, FL, MB, MAW, "form-iii-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ: اسْمُ الْفَاعِلِ وَاسْمُ الْفِعْلِ.", "«resembles it» — the participle and the noun-verb.", "«ona benzeyen» — ism-i fâil ve isim fiil.", punct="،", segments=[seg("شَابَهَ", "shabaha", "verb"), pr3ms()]),
  nahw(),
  tok("ضَرَبَ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ.", "«struck»", "«vurdu»"),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="،"),
  tok("وَأَقَائِمٌ", "qaim", "noun", [K, AT, IST, IFA, MK, MNF], "الْوَاوُ عَاطِفَةٌ، وَالْهَمْزَةُ لِلِاسْتِفْهَامِ، وَقَائِمٌ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ اعْتَمَدَ عَلَى الِاسْتِفْهَامِ.", "«and are … standing» — the participle leaning on the question.", "«ve ayakta mı» — istifhâma dayanan ism-i fâil.", segments=[seg("وَ", "wa", "conj"), seg("أَ", "a-istifham", "part"), seg("قَائِمٌ", "qaim", "noun")]),
  tok("الزَّيْدَانِ", "zayd", "propn", [K, FL, MTH, MK], "فَاعِلٌ سَدَّ مَسَدَّ الْخَبَرِ مَرْفُوعٌ بِالْأَلِفِ.", "«the two Zayds» — the doer filling the khabar's place.", "«iki Zeyd» — haberin yerini tutan fâil.", punct="،"),
  tok("وَهَيْهَاتَ", "hayhat", "noun", [K, AT, IFL, MNF], "الْوَاوُ عَاطِفَةٌ، وَهَيْهَاتَ اسْمُ فِعْلٍ مَاضٍ.", "«and far is» — the noun-verb.", "«ve uzaktır» — isim fiil.", segments=wa("هَيْهَاتَ", "hayhat", "noun")),
  tok("زَيْدٌ", "zayd", "propn", [K, IFL, FL], "فَاعِلُ اسْمِ الْفِعْلِ مَرْفُوعٌ.", "«Zayd» — the noun-verb's doer.", "«Zeyd» — isim fiilin fâili.", punct="."),
 ]})
# ----------- s4 — the second: the deputy doer
S.append({"id": "s4", "translation": {"en": "And the second is the deputy doer, and it is what the complete passive verb, or what has its sense, is predicated of — as in «Zayd was struck» and «are the two Zayds struck?».", "tr": "İkincisi nâib-i fâildir; o, tam meçhul fiilin veya onun mânâsında olanın isnâd edildiği şeydir — «Zeyd vuruldu» ve «iki Zeyd vurulmuş mu?» gibi."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second» — the mubtada.", "«ikincisi» — mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("نَائِبُ", "naib", "noun", [K, MK, ID, NF, IFA], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the deputy of» — the khabar.", "«nâibi» — haber."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, NF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâilin»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«… şey»"),
  tok("أُسْنِدَ", "asnada", "verb", [K, NF, F4, MAW], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is predicated»", "«isnâd edildi»"),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, MAW], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«of it»", "«ona»", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("الْفِعْلُ", "fil", "noun", [K, NF, KK], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the verb»", "«fiil»"),
  tok("التَّامُّ", "tamm", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«complete»", "«tam»"),
  tok("الْمَجْهُولُ", "majhul", "noun", [K, NA, IMF, NF], "نَعْتٌ ثَانٍ مَرْفُوعٌ — الْمَبْنِيُّ لِلْمَفْعُولِ.", "«passive» — built for the object.", "«meçhul» — mef'ûl için binâ edilen."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَا", "ma-mawsula", "pron", [K, AT, MAW], "اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«… şey»"),
  tok("بِمَعْنَاهُ", "mana", "noun", [K, HJ, ID, MQ, MAW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَاهُ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةٌ: اسْمُ الْمَفْعُولِ.", "«has its sense» — the ism mafʿūl.", "«mânâsında olan» — ism-i mef'ûl.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  nahw(),
  tok("ضُرِبَ", "daraba", "verb", [K, NF], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was struck»", "«vuruldu»"),
  tok("زَيْدٌ", "zayd", "propn", [K, NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«Zayd» — the deputy doer.", "«Zeyd» — nâib-i fâil.", punct="،"),
  tok("وَأَمَضْرُوبٌ", "madrub", "noun", [K, AT, IST, IMF, MK, MNF], "الْوَاوُ عَاطِفَةٌ، وَالْهَمْزَةُ لِلِاسْتِفْهَامِ، وَمَضْرُوبٌ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ اعْتَمَدَ عَلَى الِاسْتِفْهَامِ.", "«and are … struck» — the ism mafʿūl leaning on the question.", "«ve vurulmuş mu» — istifhâma dayanan ism-i mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("أَ", "a-istifham", "part"), seg("مَضْرُوبٌ", "madrub", "noun")]),
  tok("الزَّيْدَانِ", "zayd", "propn", [K, NF, MTH, MK], "نَائِبُ فَاعِلٍ سَدَّ مَسَدَّ الْخَبَرِ مَرْفُوعٌ بِالْأَلِفِ.", "«the two Zayds» — the deputy doer filling the khabar's place.", "«iki Zeyd» — haberin yerini tutan nâib-i fâil.", punct="."),
 ]})
# ----------- s5 — both nouns; the deputy may be a jarr phrase
S.append({"id": "s5", "translation": {"en": "And the two are never anything but nouns, or read as a noun — save that the deputy may be a jarr particle with its noun, as in «Zayd was passed by».", "tr": "İkisi ancak isim ya da isim te'vilinde olur — şu kadar ki nâib, câr ve mecrûr olabilir: «Zeyd'e uğranıldı» gibi."},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -maz»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَكُونَانِ", "kana", "verb", [K, KN, HV, MTH, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ اسْمُهُ.", "«the two are» — the dual alif is its ism.", "«ikisi olur» — tesniye elifi ismi."),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ — مُفَرَّغٌ.", "«but»", "«ancak»"),
  tok("اسْمَيْنِ", "ism", "noun", [K, KN, MTH, MST], "خَبَرُ يَكُونَانِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«nouns» — the khabar in the dual.", "«iki isim» — tesniye haber."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("فِي", "fi", "prep", [K, HJ, AT], "حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى اسْمَيْنِ.", "«in»", "«-de»"),
  tok("تَأْوِيلِهِ", "tawil", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — تَأْوِيلِ الِاسْمِ.", "«the reading of it» — read as a noun.", "«onun te'vilinde» — isim te'vilinde.", punct="،", segments=[seg("تَأْوِيلِ", "tawil", "noun"), pr3msi()]),
  tok("غَيْرَ", "ghayr", "noun", [K, MST, ID], "مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ، مُضَافٌ — غَيْرَ أَنَّ: إِلَّا أَنَّ.", "«save» — ghayra anna: except that.", "«şu kadar ki» — gayra enne."),
  tok("أَنَّ", "anna", "part", [K, ID, IN], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُضَافٌ إِلَيْهِ.", "«that»", "«ki»"),
  tok("النَّائِبَ", "naib", "noun", [K, IN, NF], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the deputy» — the ism of anna.", "«nâib» — enne'nin ismi."),
  tok("قَدْ", "qad", "part", [K], "حَرْفُ تَقْلِيلٍ.", "«may»", "«bazen»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR, IN], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«be» — the khabar of anna.", "«olur» — enne'nin haberi."),
  tok("جَارًّا", "jarr-active", "noun", [K, KN, IFA, HJ], "خَبَرُ يَكُونُ مَنْصُوبٌ — حَرْفَ جَرٍّ.", "«a jarr particle» — the khabar of kāna.", "«câr» — kâne'nin haberi."),
  tok("وَمَجْرُورًا", "majrur", "noun", [K, AT, IMF, HJ], "الْوَاوُ عَاطِفَةٌ، وَمَجْرُورًا مَعْطُوفٌ مَنْصُوبٌ.", "«with its noun»", "«ve mecrûr»", punct="،", segments=wa("مَجْرُورًا", "majrur", "noun")),
  nahw(),
  tok("مُرَّ", "marra", "verb", [K, NF], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مُضَاعَفٌ.", "«was passed»", "«uğranıldı»"),
  tok("بِزَيْدٍ", "zayd", "propn", [K, HJ, NF], "الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ نَائِبُ الْفَاعِلِ فِي مَحَلِّ رَفْعٍ.", "«by Zayd» — the jarr phrase as the deputy doer.", "«Zeyd'e» — nâib-i fâil olan câr-mecrûr.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
 ]})
# ----------- s6 — the governor singular and masculine; no fronting; no dropping both save with the maṣdar
S.append({"id": "s6", "translation": {"en": "So their governor must be kept singular and masculine; and it is not allowed to put them before their governor, nor to drop them both — except with the maṣdar, which has passed.", "tr": "Bu yüzden âmillerinin müfred ve müzekker kalması vâcibdir; onları âmillerinin önüne almak câiz değildir; her ikisini birden hazfetmek de — mastar hariç, ki geçti — câiz değildir."},
 "tokens": [
  tok("فَيَجِبُ", "wajaba", "verb", [K, AT, FL, MR, "mithal-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَجِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ وَاوِيٌّ.", "«so it is necessary»", "«bu yüzden vâcibdir»", segments=fa("يَجِبُ", "wajaba", "verb")),
  tok("إِفْرَادُ", "ifrad", "noun", [K, FL, ID, MSD, F4], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ أَفْرَدَ: جَعْلُهُ مُفْرَدًا.", "«the keeping singular of» — the doer.", "«müfred bırakılması» — fâil."),
  tok("عَامِلِهِمَا", "amil-governor", "noun", [K, ID, AQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«their governor»", "«âmillerinin»", segments=[seg("عَامِلِ", "amil-governor", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("وَتَذْكِيرُهُ", "tadhkir", "noun", [K, AT, ID, MSD, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَذْكِيرُهُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ ذَكَّرَ.", "«and its being masculine»", "«ve müzekker bırakılması»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("تَذْكِيرُ", "tadhkir", "noun"), pr3ms()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve değil»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("تَقْدِيمُهُمَا", "taqdim", "noun", [K, FL, ID, MSD, "form-ii-verbs"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«putting them first» — the doer.", "«onları öne almak» — fâil.", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("عَامِلِهِمَا", "amil-governor", "noun", [K, HJ, ID, AQ], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«their governor»", "«âmillerinin»", punct="،", segments=[seg("عَامِلِ", "amil-governor", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ مُؤَكِّدَةٌ.", "«nor»", "«ne de»", segments=wa("لَا", "la-nafiya", "part")),
  tok("حَذْفُهُمَا", "hadhf", "noun", [K, AT, ID, MSD, HT], "مَعْطُوفٌ عَلَى تَقْدِيمُهُمَا مَرْفُوعٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«dropping them»", "«onları hazfetmek»", segments=[seg("حَذْفُ", "hadhf", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("مَعًا", "maan", "adv", [K, HL], "حَالٌ مَنْصُوبٌ — جَمِيعًا.", "«both» — a ḥāl: together.", "«birlikte» — hâl."),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  tok("مِنَ", "min", "prep", [K, HJ, MST], "حَرْفُ جَرٍّ.", "«with»", "«-den»"),
  tok("الْمَصْدَرِ", "masdar-noun", "noun", [K, HJ, MSD, IMM], "مَجْرُورٌ بِمِنْ — الْمَصْدَرُ يُحْذَفُ فَاعِلُهُ وَمَفْعُولُهُ مَعًا.", "«the maṣdar» — whose doer and object drop together.", "«mastar» — fâili ve mef'ûlü birlikte hazfedilir.", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=wa("قَدْ", "qad", "part")),
  tok("مَرَّ", "marra", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — ذٰلِكَ.", "«it has passed»", "«geçti»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

NEW = {
 "asala-origin": G("asala-origin", "أَصَالَة", "أ ص ل", "noun", "originality, being in one's own right — مَعْمُولٌ بِالْأَصَالَةِ", "asâlet — asâleten ma'mûl", 4),
 "shabaha": G("shabaha", "شَابَهَ", "ش ب ه", "verb", "to resemble", "benzemek", 3, form="III"),
 "madrub": G("madrub", "مَضْرُوب", "ض ر ب", "noun", "struck (ism mafʿūl of ضَرَبَ)", "vurulmuş (darabe'nin ism-i mef'ûlü)", 2),
 "jarr-active": G("jarr-active", "جَارّ", "ج ر ر", "noun", "the jarr particle as a governor (ism fāʿil of جَرَّ) — الْجَارُّ وَالْمَجْرُورُ", "câr — cer eden (cerre'nin ism-i fâili) — el-câr ve'l-mecrûr", 3),
 "ifrad": G("ifrad", "إِفْرَاد", "ف ر د", "noun", "keeping singular (maṣdar of أَفْرَدَ)", "müfred bırakma (efrede'nin mastarı)", 4, form="IV"),
 "tadhkir": G("tadhkir", "تَذْكِير", "ذ ك ر", "noun", "making masculine (maṣdar of ذَكَّرَ)", "müzekker kılma (zekkere'nin mastarı)", 4, form="II"),
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
put_morph(mo, "shabaha", _sg.derived(_sg.B3, _sg.W3, "ُ", "شَابَه", "شَابِه", "شَابِه", "مُشَابَهَة", "مُشَابِه", "مُشَابَه", "شُوبِهَ", "يُشَابَهُ", "مُتَعَدٍّ: شَابَهَ الشَّيْءُ الشَّيْءَ — أَشْبَهَهُ."))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch21 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("asnada", "shabaha", "daraba", "kana", "marra", "wajaba", "jaaza") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَرْفُوعَاتُ التِّسْعَةُ: الْفَاعِلُ وَنَائِبُ الْفَاعِلِ وَأَحْكَامُهُمَا", "en": "The nine marfūʿāt: the doer and the deputy doer, and their rules", "tr": "Dokuz merfû: fâil ve nâib-i fâil ve hükümleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الباب الثاني: المرفوعات", "الكافية لابن الحاجب — الفاعل، مفعول ما لم يسم فاعله", "شرح قطر الندى لابن هشام — الفاعل ونائبه"],
 "amil": "the governed word in its own right is marfūʿ, manṣūb, majrūr or majzūm; the marfūʿ are nine, the first the doer — what a complete active verb or its like is predicated of — and the second the deputy doer — what a complete passive verb or its like is predicated of; both nouns (or read as nouns), the deputy also a jarr phrase; their governor singular and masculine; no fronting them, no dropping both save with the maṣdar",
 "question": {
  "en": ["How is the governed word divided? Governed in its own right or by following; the first is marfūʿ, manṣūb, majrūr or majzūm.",
         "How many marfūʿ are there, and what is the first? Nine. The first is the doer: what the complete active verb, or what resembles it (the participle, the noun-verb), is predicated of — ضَرَبَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ، هَيْهَاتَ زَيْدٌ.",
         "What is the second? The deputy doer: what the complete passive verb, or what has its sense (the ism mafʿūl), is predicated of — ضُرِبَ زَيْدٌ، أَمَضْرُوبٌ الزَّيْدَانِ.",
         "Must they be nouns? Yes — nouns, or sentences read as nouns; except that the deputy may be a jarr phrase: مُرَّ بِزَيْدٍ.",
         "What follows for their governor? It stays singular and masculine (ضَرَبَ الزَّيْدَانِ، قَامَتْ … no: the verb takes no dual or plural sign before its doer); they are never put before it, and are never both dropped save with the maṣdar, as was said in the maṣdar's chapter.",
         "What does the engine READ here? The DabtEngine raises the noun after a verb as its doer, the noun after a passive as its deputy, the dual after the questioned participle as the doer filling the khabar's place, and reads بِزَيْدٍ after مُرَّ as the jarr phrase that deputises."],
  "tr": ["Ma'mûl nasıl bölünür? Asâleten veya tebaiyyeten ma'mûl; ilki merfû, mansûb, mecrûr veya meczûmdur.",
         "Merfû kaç tanedir, ilki nedir? Dokuz. İlki fâildir: tam ma'lûm fiilin veya ona benzeyenin (ism-i fâil, isim fiil) isnâd edildiği şey — darabe Zeydün, e-kâimün ez-Zeydâni, heyhâte Zeydün.",
         "İkincisi nedir? Nâib-i fâil: tam meçhul fiilin veya onun mânâsında olanın (ism-i mef'ûl) isnâd edildiği şey — duribe Zeydün, e-madrûbün ez-Zeydâni.",
         "İsim olmaları şart mı? Evet — isim ya da isim te'vilinde cümle; şu kadar ki nâib, câr-mecrûr olabilir: murra bi-Zeydin.",
         "Âmilleri için ne gerekir? Müfred ve müzekker kalır (fiil fâilinden önce tesniye veya cem' alâmeti almaz); onların önüne alınmazlar ve ikisi birden hazfedilmez — mastar hariç, mastar babında söylendiği gibi.",
         "Motor burada neyi OKUR? DabtEngine fiilden sonraki ismi fâil, meçhulden sonrakini nâib-i fâil, istifhâmlı ism-i fâilden sonraki tesniyeyi haberin yerini tutan fâil olarak ref' eder ve murra'dan sonraki bi-Zeydin'i nâib olan câr-mecrûr olarak okur."],
 },
 "plain": {"en": "The words a sentence raises come in nine kinds; the first two are the subject of an active verb («Zayd struck») and of a passive one («Zayd was struck»). Either must be a noun, though the passive's subject can be a prepositional phrase. The verb stays singular before its subject, and the subject never precedes it.",
           "tr": "Bir cümlenin ref' ettiği kelimeler dokuz çeşittir; ilk ikisi ma'lûm fiilin öznesi («Zeyd vurdu») ve meçhul fiilin öznesi («Zeyd vuruldu»). İkisi de isim olmalıdır; ancak meçhulün öznesi bir câr-mecrûr olabilir («Zeyd'e uğranıldı»). Fiil öznesinden önce tekil kalır ve özne onun önüne geçmez."},
 "explanation": {"en": "The governed word is of two sorts, in its own right and by following; the first is of four divisions — marfūʿ, manṣūb, majrūr and majzūm. The marfūʿ are nine. The first is the doer: what the complete active verb, or what resembles it, is predicated of (ضَرَبَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ، هَيْهَاتَ زَيْدٌ). The second is the deputy doer: what the complete passive verb, or what has its sense, is predicated of (ضُرِبَ زَيْدٌ، أَمَضْرُوبٌ الزَّيْدَانِ). Both are nouns or read as nouns, except that the deputy may be a jarr phrase (مُرَّ بِزَيْدٍ). Hence their governor must be kept singular and masculine, they may not be put before it, and they may not both be dropped save with the maṣdar, as has passed.",
                 "tr": "Ma'mûl iki türlüdür: asâleten ve tebaiyyeten; ilki dört kısımdır — merfû, mansûb, mecrûr ve meczûm. Merfû dokuzdur. İlki fâildir: tam ma'lûm fiilin veya ona benzeyenin isnâd edildiği şey (darabe Zeydün, e-kâimün ez-Zeydâni, heyhâte Zeydün). İkincisi nâib-i fâildir: tam meçhul fiilin veya onun mânâsında olanın isnâd edildiği şey (duribe Zeydün, e-madrûbün ez-Zeydâni). İkisi de isim ya da isim te'vilindedir; şu kadar ki nâib câr-mecrûr olabilir (murra bi-Zeydin). Bu yüzden âmilleri müfred ve müzekker kalmalı, önüne alınmamalı ve ikisi birden hazfedilmemelidir — mastar hariç, geçtiği gibi."},
 "examples": [
  {"ar": "مَعْمُولٌ بِالْأَصَالَةِ وَمَعْمُولٌ بِالتَّبَعِيَّةِ", "en": "the two sorts of governed word", "tr": "ma'mûlün iki türü", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "ضَرَبَ زَيْدٌ، وَأَقَائِمٌ الزَّيْدَانِ، وَهَيْهَاتَ زَيْدٌ", "en": "the doer of the verb and of its like", "tr": "fiilin ve benzerinin fâili", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "ضُرِبَ زَيْدٌ، وَأَمَضْرُوبٌ الزَّيْدَانِ", "en": "the deputy doer of the passive and of the ism mafʿūl", "tr": "meçhulün ve ism-i mef'ûlün nâib-i fâili", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "مُرَّ بِزَيْدٍ", "en": "the jarr phrase as the deputy doer", "tr": "nâib-i fâil olan câr-mecrûr", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "فَيَجِبُ إِفْرَادُ عَامِلِهِمَا وَتَذْكِيرُهُ", "en": "the governor singular and masculine", "tr": "âmil müfred ve müzekker", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "ضَرَبَا الزَّيْدَانِ", "right": "ضَرَبَ الزَّيْدَانِ", "why": {"en": "the verb stays singular before its doer", "tr": "fiil fâilinden önce müfred kalır"}},
  {"wrong": "زَيْدٌ ضَرَبَ (as the doer fronted)", "right": "ضَرَبَ زَيْدٌ", "why": {"en": "the doer never precedes its governor; fronted, Zayd is a mubtadaʾ", "tr": "fâil âmilinin önüne geçmez; öne alınınca Zeyd mübtedâdır"}},
  {"wrong": "ضُرِبَ زَيْدًا", "right": "ضُرِبَ زَيْدٌ", "why": {"en": "the passive raises its deputy doer", "tr": "meçhul fiil nâib-i fâilini ref' eder"}},
 ],
}
ADD_EN = (" Chapter 21 (print pp. 121-122): the governed in its own right and by following (s1), the four divisions (s2); the nine marfūʿāt — the doer (s3) and the deputy doer (s4), both nouns or read as nouns with the deputy also a jarr phrase (s5), their governor singular and masculine, no fronting, no dropping both save with the maṣdar (s6).")
ADD_TR = (" Yirmi birinci bab (baskı s. 121-122): asâleten ve tebaiyyeten ma'mûl (s1), dört kısım (s2); dokuz merfû — fâil (s3) ve nâib-i fâil (s4), ikisi de isim ya da isim te'vilinde, nâib câr-mecrûr da olabilir (s5), âmilleri müfred ve müzekker, öne alınmaz, mastar hariç ikisi birden hazfedilmez (s6).")
write_out(21, S, TITLE, ADD_EN, ADD_TR, "pp. 121-122", GLOSS_ADD, notes=(NOTE,),
          related=((K20, [K]), (FL, [K]), (NF, [K]), (IST, [K]), (IMM, [K]), (AQ, [K])))
report(21, S, GLOSS_ADD, (NOTE,))
