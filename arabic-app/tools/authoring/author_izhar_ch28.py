# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 28: the THIRD marfūʿ, the MUBTADAʾ, of two kinds — the noun (or what is read as one)
# predicated of and stripped of the wording's governors (زَيْدٌ قَائِمٌ، حَقٌّ أَنَّكَ قَائِمٌ), which must have a khabar; and the ṣifa after
# a word of question or negation raising an apparent noun (أَقَائِمٌ الزَّيْدَانِ، مَا قَائِمٌ الزَّيْدُونَ), which has no khabar, its doer
# filling the khabar's place. No multiplying the mubtadaʾ; its origin is to come first; its condition is definiteness or a
# particularised nakira (﴿وَلَعَبْدٌ مُؤْمِنٌ خَيْرٌ مِنْ مُشْرِكٍ﴾); it may be dropped on a clue (زَيْدٌ answering مَنِ الْقَائِمُ). Print pp. 128–129.
#   python3 author_izhar_ch28.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-mubtada-wa-nawah"
K21 = "al-marfuat-al-fail-wa-naibuh"
TITLE = {"ar": "الْمَرْفُوعُ الثَّالِثُ: الْمُبْتَدَأُ وَنَوْعَاهُ", "en": "The third marfūʿ: the mubtadaʾ and its two kinds", "tr": "Üçüncü merfû: mübtedâ ve iki türü"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; JMS = "jam-mudhakkar-salim"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"
AMS = "an-masdariyya"; NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; ISH = "asma-al-ishara"; TM = "tamyiz"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; ANN = "al-mubtada-wa-nawah"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wahuwa(): return tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron"))

# ----------- s1 — the third: the mubtadaʾ, two kinds
S.append({"id": "s1", "translation": {"en": "And the third is the mubtadaʾ, and it is of two kinds.", "tr": "Üçüncüsü mübtedâdır ve iki türlüdür."},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ — الْمَرْفُوعُ الثَّالِثُ.", "«and the third» — the third marfūʿ.", "«üçüncüsü» — üçüncü merfû.", segments=wa("الثَّالِثُ", "thalith", "noun")),
  tok("الْمُبْتَدَأُ", "mubtada", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«the mubtadaʾ» — the khabar.", "«mübtedâ» — haber.", punct="،"),
  wahuwa(),
  tok("نَوْعَانِ", "naw", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two kinds»", "«iki tür»", punct="."),
 ]})
# ----------- s2 — the first kind
S.append({"id": "s2", "translation": {"en": "The first is the noun, or what is read as a noun, predicated of and stripped of the governors of wording — as in «Zayd is standing» and «it is true that you are standing» — and it must have a khabar.", "tr": "İlki, isnâd edilen ve lafzî âmillerden soyutlanmış isim ya da isim te'vilindeki şeydir — «Zeyd ayaktadır», «ayakta olman haktır» gibi —; onun için bir haber zorunludur."},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«ilki» — mübtedâ."),
  tok("الِاسْمُ", "ism", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the noun» — the khabar.", "«isim» — haber."),
  tok("وَالْمُؤَوَّلُ", "muawwal", "noun", [K, AT, IMF, F2], "الْوَاوُ عَاطِفَةٌ، وَالْمُؤَوَّلُ مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ أَوَّلَ.", "«and what is read as» — the ism mafʿūl of أَوَّلَ.", "«ve te'vîl edilen» — evvele'nin ism-i mef'ûlü.", segments=wa("الْمُؤَوَّلُ", "muawwal", "noun")),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — بِالِاسْمِ.", "«as it» — as a noun.", "«onunla» — isimle.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الْمُسْنَدُ", "musnad", "noun", [K, NA, IMF, F4 if False else "form-iv-verbs"], "نَعْتٌ لِلِاسْمِ مَرْفُوعٌ.", "«predicated»", "«isnâd edilen»"),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — نَائِبُ فَاعِلِ الْمُسْنَدِ.", "«of» — the participle's deputy.", "«kendisine» — ism-i mef'ûlün nâibi.", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("الْمُجَرَّدُ", "mujarrad", "noun", [K, NA, IMF, F2], "نَعْتٌ ثَانٍ مَرْفُوعٌ.", "«stripped»", "«soyutlanmış»"),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، كُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("الْعَوَامِلِ", "awamil", "noun", [K, HJ, JT, AQ], "مَجْرُورٌ بِعَنْ — جَمْعُ عَامِلٍ.", "«the governors» — the plural of عَامِل.", "«âmiller» — âmilin cem'i."),
  tok("اللَّفْظِيَّةِ", "lafzi", "noun", [K, NA, NSB], "نَعْتٌ مَجْرُورٌ — كَانَ وَإِنَّ وَأَخَوَاتِهِمَا.", "«of wording» — kāna, inna and their sisters.", "«lafzî» — kâne, inne ve kardeşleri.", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«standing» — the khabar.", "«ayakta» — haber.", punct="،"),
  tok("وَحَقٌّ", "haqq", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَحَقٌّ خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«and true» — the fronted khabar.", "«ve haktır» — öne alınmış haber.", segments=wa("حَقٌّ", "haqq", "noun")),
  tok("أَنَّكَ", "anna", "part", [K, IN, MK], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهُ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that you» — the clause read as a noun is the mubtada.", "«senin» — isim te'vilindeki cümle mübtedâ.", segments=[seg("أَنَّ", "anna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("قَائِمٌ", "qaim", "noun", [K, IN, IFA], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«are standing» — anna's khabar.", "«ayaktasın» — enne'nin haberi.", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no»", "«ve … yok»", segments=wa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, LN, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ — لَا بُدَّ: لَا مَفَرَّ.", "«escape» — lā's ism: no escape, i.e. it must.", "«çâre» — lâ'nın ismi: lâ büdde, kaçınılmaz."),
  tok("لَهُ", "li", "prep", [K, HJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — لِلْمُبْتَدَإِ.", "«for it» — for the mubtada.", "«onun için» — mübtedâ için.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("خَبَرٍ", "khabar", "noun", [K, HJ, MK], "مَجْرُورٌ بِمِنْ — وَخَبَرُ لَا مَحْذُوفٌ.", "«a khabar» — lā's own khabar dropped.", "«bir haber» — lâ'nın haberi hazfedilmiş.", punct="."),
 ]})
# ----------- s3 — the second kind
S.append({"id": "s3", "translation": {"en": "And the second is the adjective falling after a word of question or negation, raising an apparent noun — as in «are the two Zayds standing?» and «the Zayds are not standing» — and this mubtadaʾ has no khabar, since it has the sense of a verb; rather its doer fills the khabar's place.", "tr": "İkincisi, istifhâm veya nefiy kelimesinden sonra gelip açık ismi ref' eden sıfattır — «iki Zeyd ayakta mı?», «Zeydler ayakta değil» gibi —; bu mübtedânın haberi yoktur, çünkü fiil mânâsındadır; fâili haberin yerini tutar."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الصِّفَةُ", "sifa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the adjective» — the khabar.", "«sıfat» — haber."),
  tok("الْوَاقِعَةُ", "waqia", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ.", "«falling»", "«gelen»"),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("كَلِمَةِ", "kalima", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«a word of»", "«kelimesi»"),
  tok("الِاسْتِفْهَامِ", "istifham", "noun", [K, ID, IST], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«question»", "«istifhâm»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، كُسِرَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("النَّفْيِ", "nafy", "noun", [K, AT, LN], "مَعْطُوفٌ عَلَى الِاسْتِفْهَامِ مَجْرُورٌ.", "«negation»", "«nefiy»"),
  tok("رَافِعَةً", "rafi-raising", "noun", [K, HL if False else "hal", IFA], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ عَامِلٌ.", "«raising» — a ḥāl, the governing participle.", "«ref' eden» — hâl, amel eden ism-i fâil."),
  tok("لِظَاهِرٍ", "zahir", "noun", [K, HJ, IFA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّقْوِيَةِ، وَظَاهِرٍ مَجْرُورٌ — مَفْعُولُ رَافِعَةً فِي الْمَعْنَى.", "«an apparent noun» — the lām of strengthening on the participle's object.", "«açık ismi» — takviye lâmı, ism-i fâilin mef'ûlü.", punct="،", segments=[seg("لِ", "li", "prep"), seg("ظَاهِرٍ", "zahir", "noun")]),
  nahw(),
  tok("أَقَائِمٌ", "qaim", "noun", [K, IST, MK, IFA, MNF], "لَفْظٌ مَحْكِيٌّ: الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَقَائِمٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«are … standing» — the mubtada after the question's hamza.", "«ayakta mı» — istifhâm hemzesinden sonra mübtedâ.", segments=[seg("أَ", "a-istifham", "part"), seg("قَائِمٌ", "qaim", "noun")]),
  tok("الزَّيْدَانِ", "zayd", "propn", [K, FL, MTH, MK], "فَاعِلٌ سَدَّ مَسَدَّ الْخَبَرِ مَرْفُوعٌ بِالْأَلِفِ.", "«the two Zayds» — the doer filling the khabar's place.", "«iki Zeyd» — haberin yerini tutan fâil.", punct="،"),
  tok("وَمَا", "ma-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and not»", "«ve değil»", segments=wa("مَا", "ma-nafiya", "part")),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA, MNF], "مُبْتَدَأٌ مَرْفُوعٌ — اعْتَمَدَ عَلَى النَّفْيِ.", "«standing» — the mubtada leaning on the negation.", "«ayakta» — nefye dayanan mübtedâ."),
  tok("الزَّيْدُونَ", "zayd", "propn", [K, FL, JMS, MK], "فَاعِلٌ سَدَّ مَسَدَّ الْخَبَرِ مَرْفُوعٌ بِالْوَاوِ.", "«the Zayds»", "«Zeydler»", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no»", "«ve … yok»", segments=wa("لَا", "la-nafiya", "part")),
  tok("خَبَرَ", "khabar", "noun", [K, LN, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«khabar» — lā's ism.", "«haber» — lâ'nın ismi."),
  tok("لِهٰذَا", "hadha", "pron", [K, HJ, ISH, MK], "اللَّامُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«for this» — lā's khabar.", "«bu … için» — lâ'nın haberi.", segments=[seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, NA, ISH], "بَدَلٌ مِنْ هٰذَا مَجْرُورٌ.", "«mubtadaʾ» — the badal of «this».", "«mübtedâ» — «bu»nun bedeli."),
  tok("لِكَوْنِهِ", "kawn", "noun", [K, HJ, ID, MSD, KN], "اللَّامُ لِلتَّعْلِيلِ، وَكَوْنِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«since it is»", "«… olduğu için»", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3msi()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — خَبَرُ كَوْنِ.", "«in the sense of»", "«mânâsında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الْفِعْلِ", "fil", "noun", [K, ID, MNF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»", punct="،"),
  tok("بَلْ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ.", "«rather»", "«bilakis»"),
  tok("فَاعِلُهُ", "fail-doer", "noun", [K, MK, ID, FL], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its doer» — the mubtada.", "«fâili» — mübtedâ.", segments=[seg("فَاعِلُ", "fail-doer", "noun"), pr3ms()]),
  tok("سَادٌّ", "sadd-filling", "noun", [K, MK, IFA, "doubled-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ سَدَّ.", "«filling» — the khabar.", "«tutan» — haber."),
  tok("مَسَدَّ", "masadd", "noun", [K, MB, ID], "مَفْعُولٌ بِهِ لِسَادٍّ مَنْصُوبٌ، مُضَافٌ — أَوْ ظَرْفٌ.", "«the place of»", "«yerini»"),
  tok("الْخَبَرِ", "khabar", "noun", [K, ID, MK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar»", "«haberin»", punct="."),
 ]})
# ----------- s4 — no multiplying; the origin is to come first
S.append({"id": "s4", "translation": {"en": "And the mubtadaʾ may not be multiplied, and its origin is to come first;", "tr": "Mübtedânın taaddüdü câiz değildir; aslı öne gelmesidir;"},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … değil»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("تَعَدُّدُ", "taaddud", "noun", [K, FL, ID, MSD, F5], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ تَعَدَّدَ.", "«the multiplying of» — the doer.", "«taaddüdü» — fâil."),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtadaʾ»", "«mübtedânın»", punct="،"),
  tok("وَالْأَصْلُ", "asl", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْأَصْلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the origin» — the mubtada.", "«ve asıl» — mübtedâ.", segments=wa("الْأَصْلُ", "asl", "noun")),
  tok("تَقْدِيمُهُ", "taqdim", "noun", [K, MK, ID, MSD, F2], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its coming first» — the khabar.", "«onun öne gelmesi» — haber.", punct="؛", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
 ]})
# ----------- s5 — its condition: definite or a particularised nakira
S.append({"id": "s5", "translation": {"en": "and its condition is that it be definite, or a particularised indefinite — as in His word, exalted: «and a believing slave is better than an idolater»;", "tr": "şartı ma'rife ya da tahsîs edilmiş nekre olmasıdır — Allah Teâlâ'nın «mümin bir köle müşrikten hayırlıdır» sözü gibi;"},
 "tokens": [
  tok("وَشَرْطُهُ", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its condition» — the mubtada.", "«ve şartı» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause read as a noun is the khabar.", "«-ması» — masdar haber."),
  tok("يَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it be»", "«olması»"),
  tok("مَعْرِفَةً", "marifa", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«definite»", "«ma'rife»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("نَكِرَةً", "nakira", "noun", [K, AT, KN], "مَعْطُوفٌ مَنْصُوبٌ.", "«an indefinite»", "«nekre»"),
  tok("مُخَصَّصَةً", "mukhassas", "noun", [K, NA, IMF, F2], "نَعْتٌ مَنْصُوبٌ — بِوَصْفٍ أَوْ إِضَافَةٍ.", "«particularised» — by a description or an annexation.", "«tahsîs edilmiş» — vasıf veya izâfetle.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«as in»", "«… gibi»"),
  tok("قَوْلِهِ", "qawl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«exalted»", "«yücedir»", punct=":"),
  tok("وَلَعَبْدٌ", "abd", "noun", [K, MK, "inna-wa-akhawatuha"], "لَفْظٌ مَحْكِيٌّ: الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لِلِابْتِدَاءِ، وَعَبْدٌ مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ مُخَصَّصَةٌ بِالْوَصْفِ.", "«and a slave» — the mubtada: a nakira particularised by its adjective.", "«ve bir köle» — vasıfla tahsîs edilmiş nekre mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-ibtida", "part"), seg("عَبْدٌ", "abd", "noun")]),
  tok("مُؤْمِنٌ", "mumin", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ.", "«believing»", "«mümin»"),
  tok("خَيْرٌ", "khayr", "noun", [K, MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — أَفْعَلُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.", "«better» — the khabar.", "«daha hayırlı» — haber."),
  tok("مِنْ", "min", "prep", [K, HJ, "ism-tafdil"], "حَرْفُ جَرٍّ.", "«than»", "«-den»"),
  tok("مُشْرِكٍ", "mushrik", "noun", [K, HJ, IFA], "مَجْرُورٌ بِمِنْ.", "«an idolater»", "«müşrik»", punct="؛"),
 ]})
# ----------- s6 — it may be dropped on a clue
S.append({"id": "s6", "translation": {"en": "and it may be dropped where a clue stands — as in «Zayd» in answer to «who is standing?», that is: «the standing one is Zayd».", "tr": "karîne bulununca hazfi câizdir — «ayakta olan kim?» sorusuna cevâben «Zeyd» gibi; yani: «ayakta olan Zeyd'dir»."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("حَذْفُهُ", "hadhf", "noun", [K, FL, ID, MSD, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«dropping it» — the doer.", "«onun hazfi» — fâil.", segments=[seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«where»", "«-ında»"),
  tok("قِيَامِ", "qiyam", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the standing of»", "«bulunması»"),
  tok("الْقَرِينَةِ", "qarina", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, HT], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ.", "«Zayd» — the khabar of a dropped mubtada.", "«Zeyd» — hazfedilmiş mübtedânın haberi.", punct="،"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("جَوَابِ", "jawab", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ إِلَى الْجُمْلَةِ.", "«answer to»", "«cevâbında»", punct=":"),
  tok("مَنِ", "man", "pron", [K, IST, MK], "لَفْظٌ مَحْكِيٌّ: اسْمُ اسْتِفْهَامٍ خَبَرٌ مُقَدَّمٌ فِي مَحَلِّ رَفْعٍ — أَوْ مُبْتَدَأٌ.", "«who» — the question word.", "«kim» — istifhâm ismi."),
  tok("الْقَائِمُ", "qaim", "noun", [K, MK, IFA], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«is standing» — the mubtada put after.", "«ayakta olan» — sonraya bırakılmış mübtedâ.", punct="؟"),
  tok("أَيِ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ، كُسِرَتْ يَاؤُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«that is»", "«yani»", punct=":"),
  tok("الْقَائِمُ", "qaim", "noun", [K, MK, IFA, HT], "مُبْتَدَأٌ مَرْفُوعٌ — الْمَحْذُوفُ مُقَدَّرًا.", "«the standing one» — the dropped mubtada restored.", "«ayakta olan» — hazfedilen mübtedâ takdîr edilmiş."),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«is Zayd» — the khabar.", "«Zeyd'dir» — haber.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "awamil": G("awamil", "عَوَامِل", "ع م ل", "noun", "governors — the plural of عَامِل; الْعَوَامِلُ اللَّفْظِيَّةُ", "âmiller — âmilin cem'i; lafzî âmiller", 4),
 "rafi-raising": G("rafi-raising", "رَافِع", "ر ف ع", "noun", "raising — the governor that puts a word in rafʿ (ism fāʿil of رَفَعَ)", "ref' eden — kelimeyi merfû kılan âmil (refea'nın ism-i fâili)", 4),
 "mukhassas": G("mukhassas", "مُخَصَّص", "خ ص ص", "noun", "particularised — a nakira narrowed by a description or an annexation (ism mafʿūl of خَصَّصَ)", "tahsîs edilmiş — vasıf veya izâfetle daraltılmış nekre (hassasa'nın ism-i mef'ûlü)", 4, form="II"),
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
print("izhar ch28 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "taala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُبْتَدَأُ: نَوْعَاهُ وَشَرْطُهُ وَحَذْفُهُ", "en": "The mubtadaʾ: its two kinds, its condition and its dropping", "tr": "Mübtedâ: iki türü, şartı ve hazfi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المرفوعات: المبتدأ", "الكافية لابن الحاجب — المبتدأ", "شرح قطر الندى لابن هشام — المبتدأ والخبر"],
 "amil": "the third marfūʿ, the mubtadaʾ, is of two kinds — the noun (or what is read as one) predicated of and stripped of the governors of wording, which must have a khabar (زَيْدٌ قَائِمٌ، حَقٌّ أَنَّكَ قَائِمٌ); and the adjective after a word of question or negation raising an apparent noun, which has no khabar, its doer filling the khabar's place (أَقَائِمٌ الزَّيْدَانِ، مَا قَائِمٌ الزَّيْدُونَ); it is never multiplied, its origin is to come first, its condition is definiteness or a particularised nakira (﴿وَلَعَبْدٌ مُؤْمِنٌ خَيْرٌ مِنْ مُشْرِكٍ﴾), and it may be dropped on a clue (زَيْدٌ answering مَنِ الْقَائِمُ)",
 "question": {
  "en": ["What is the first kind of mubtadaʾ? The noun, or what is read as a noun, predicated of and stripped of the governors of wording: زَيْدٌ قَائِمٌ، حَقٌّ أَنَّكَ قَائِمٌ — and it must have a khabar.",
         "What is the second kind? The adjective after a word of question or negation that raises an apparent noun: أَقَائِمٌ الزَّيْدَانِ، مَا قَائِمٌ الزَّيْدُونَ — it has no khabar, for it has the sense of a verb; its doer fills the khabar's place.",
         "May the mubtadaʾ be multiplied? No; and its origin is to come first — before its khabar.",
         "What is its condition? To be definite, or a nakira particularised by a description or an annexation: ﴿وَلَعَبْدٌ مُؤْمِنٌ خَيْرٌ مِنْ مُشْرِكٍ﴾ (al-Baqara 2:221).",
         "When may it be dropped? Where a clue stands: زَيْدٌ in answer to مَنِ الْقَائِمُ — that is, الْقَائِمُ زَيْدٌ.",
         "Why is the adjective after the hamza a mubtadaʾ and not a khabar? Because it leans on the question (or the negation) and governs like a verb: it raises the apparent noun after it as its doer, and a verb-like word needs no khabar.",
         "What does the engine READ here? The DabtEngine raises the noun opening a clause as the mubtadaʾ and the nakira after it as its khabar, raises the dual or sound plural after the questioned participle as the doer filling the khabar's place, reads the clause after حَقٌّ أَنَّكَ as the delayed mubtadaʾ, and keeps the Qurʾānic words as the source prints them."],
  "tr": ["Mübtedânın ilk türü nedir? İsnâd edilen ve lafzî âmillerden soyutlanmış isim ya da isim te'vilindeki şey: Zeydün kâimün, hakkun enneke kâimün — ve onun için haber zorunludur.",
         "İkinci türü nedir? İstifhâm veya nefiy kelimesinden sonra gelip açık ismi ref' eden sıfat: e-kâimün ez-Zeydâni, mâ kâimün ez-Zeydûne — haberi yoktur, çünkü fiil mânâsındadır; fâili haberin yerini tutar.",
         "Mübtedâ taaddüd edebilir mi? Hayır; aslı haberinden önce gelmesidir.",
         "Şartı nedir? Ma'rife ya da vasıf veya izâfetle tahsîs edilmiş nekre olması: ve-le-abdün mü'minün hayrun min müşrikin (Bakara 2:221).",
         "Ne zaman hazfedilebilir? Karîne bulununca: meni'l-kâimü sorusuna cevâben Zeydün — yani el-kâimü Zeydün.",
         "Hemzeden sonraki sıfat niçin haber değil mübtedâdır? Çünkü istifhâma (veya nefye) dayanır ve fiil gibi amel eder: ardındaki açık ismi fâil olarak ref' eder; fiil gibi olan şeye haber gerekmez.",
         "Motor burada neyi OKUR? DabtEngine cümleyi açan ismi mübtedâ, ardındaki nekreyi haber olarak ref' eder; istifhâmlı ism-i fâilden sonraki tesniye ve sâlim cem'i haberin yerini tutan fâil olarak okur; hakkun enneke'den sonraki cümleyi geciktirilmiş mübtedâ sayar; Kur'ân kelimelerini kaynağın yazdığı gibi tutar."],
 },
 "plain": {"en": "A subject that stands with no verb before it is the mubtadaʾ, and it needs a predicate: «Zayd is standing». A second kind has no predicate: after a question or a negation, an adjective like «standing» acts as a verb and takes the next noun as its subject. It must be definite, or an indefinite narrowed by a description.",
           "tr": "Önünde fiil olmadan duran cümle öznesi mübtedâdır ve bir yüklem ister: «Zeyd ayaktadır». İkinci türün yüklemi yoktur: soru ya da olumsuzluktan sonra «ayakta» gibi bir sıfat fiil gibi davranır ve ardındaki ismi öznesi yapar. Özne ma'rife olmalı ya da bir vasıfla daraltılmış nekre olmalıdır."},
 "explanation": {"en": "The third marfūʿ is the mubtadaʾ, of two kinds. The first is the noun, or what is read as a noun, predicated of and stripped of the governors of wording (زَيْدٌ قَائِمٌ، حَقٌّ أَنَّكَ قَائِمٌ), and it must have a khabar. The second is the adjective falling after a word of question or negation, raising an apparent noun (أَقَائِمٌ الزَّيْدَانِ، مَا قَائِمٌ الزَّيْدُونَ); this mubtadaʾ has no khabar, since it has the sense of a verb — rather its doer fills the khabar's place. The mubtadaʾ may not be multiplied; its origin is to come first; its condition is to be definite or a particularised nakira (﴿وَلَعَبْدٌ مُؤْمِنٌ خَيْرٌ مِنْ مُشْرِكٍ﴾); and it may be dropped where a clue stands (زَيْدٌ in answer to مَنِ الْقَائِمُ, i.e. الْقَائِمُ زَيْدٌ).",
                 "tr": "Üçüncü merfû mübtedâdır, iki türlüdür. İlki isnâd edilen ve lafzî âmillerden soyutlanmış isim ya da isim te'vilindeki şeydir (Zeydün kâimün, hakkun enneke kâimün) ve onun için haber zorunludur. İkincisi istifhâm veya nefiy kelimesinden sonra gelip açık ismi ref' eden sıfattır (e-kâimün ez-Zeydâni, mâ kâimün ez-Zeydûne); bu mübtedânın haberi yoktur, çünkü fiil mânâsındadır — fâili haberin yerini tutar. Mübtedâ taaddüd edemez; aslı öne gelmesidir; şartı ma'rife ya da tahsîs edilmiş nekre olmasıdır (ve-le-abdün mü'minün hayrun min müşrikin); karîne bulununca hazfi câizdir (meni'l-kâimü'ye cevâben Zeydün, yani el-kâimü Zeydün)."},
 "examples": [
  {"ar": "زَيْدٌ قَائِمٌ، وَحَقٌّ أَنَّكَ قَائِمٌ", "en": "the first kind: the noun and what is read as one", "tr": "ilk tür: isim ve isim te'vilindeki", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "أَقَائِمٌ الزَّيْدَانِ، وَمَا قَائِمٌ الزَّيْدُونَ", "en": "the second kind: the adjective raising its doer", "tr": "ikinci tür: fâilini ref' eden sıfat", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "فَاعِلُهُ سَادٌّ مَسَدَّ الْخَبَرِ", "en": "the doer filling the khabar's place", "tr": "haberin yerini tutan fâil", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَلَعَبْدٌ مُؤْمِنٌ خَيْرٌ مِنْ مُشْرِكٍ", "en": "the particularised nakira as mubtadaʾ (2:221)", "tr": "mübtedâ olan tahsîs edilmiş nekre (2:221)", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "زَيْدٌ فِي جَوَابِ مَنِ الْقَائِمُ", "en": "the mubtadaʾ dropped on a clue", "tr": "karîne ile hazfedilen mübtedâ", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "أَقَائِمٌ الزَّيْدَانِ — الزَّيْدَانِ as the khabar", "right": "الزَّيْدَانِ is the doer filling the khabar's place", "why": {"en": "the adjective after the question's hamza governs like a verb and has no khabar", "tr": "istifhâm hemzesinden sonraki sıfat fiil gibi amel eder, haberi yoktur"}},
  {"wrong": "عَبْدٌ خَيْرٌ مِنْ مُشْرِكٍ (a bare nakira as mubtadaʾ)", "right": "عَبْدٌ مُؤْمِنٌ خَيْرٌ مِنْ مُشْرِكٍ", "why": {"en": "a nakira is a mubtadaʾ only when particularised by a description or an annexation", "tr": "nekre ancak vasıf veya izâfetle tahsîs edilince mübtedâ olur"}},
  {"wrong": "زَيْدٌ عَمْرٌو قَائِمَانِ (two mubtadaʾs)", "right": "زَيْدٌ وَعَمْرٌو قَائِمَانِ", "why": {"en": "the mubtadaʾ is never multiplied; a second noun joins it by ʿaṭf", "tr": "mübtedâ taaddüd etmez; ikinci isim ona atıfla bağlanır"}},
 ],
}
ADD_EN = (" Chapter 28 (print pp. 128-129): the third marfūʿ, the mubtadaʾ, of two kinds (s1) — the noun or what is read as one, stripped of the governors of wording, with its khabar (s2); the adjective after a question or negation raising an apparent noun, its doer filling the khabar's place (s3); no multiplying, the origin to come first (s4); its condition — definite or a particularised nakira, al-Baqara 2:221 (s5); dropped on a clue (s6).")
ADD_TR = (" Yirmi sekizinci bab (baskı s. 128-129): üçüncü merfû mübtedâ, iki tür (s1) — lafzî âmillerden soyutlanmış isim veya isim te'vilindeki, haberiyle (s2); istifhâm veya nefiyden sonra açık ismi ref' eden sıfat, fâili haberin yerinde (s3); taaddüd yok, asıl öne gelmesi (s4); şartı — ma'rife veya tahsîs edilmiş nekre, Bakara 2:221 (s5); karîne ile hazfi (s6).")
write_out(28, S, TITLE, ADD_EN, ADD_TR, "pp. 128-129", GLOSS_ADD, notes=(NOTE,),
          related=((K21, [K]), (MK, [K]), (IST, [K]), (HT, [K]), (IFA, [K]), (MNF, [K])))
report(28, S, GLOSS_ADD, (NOTE,))
