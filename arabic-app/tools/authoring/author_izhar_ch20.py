# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 20: the sentence that is NOT read as a single noun has iʿrāb only in its positions — the khabar of
# the mubtadaʾ (زَيْدٌ أَبُوهُ قَائِمٌ) and of إِنَّ's bāb (place of rafʿ); of كَانَ's and كَادَ's bāb, the second object of عَلِمَ's bāb, the
# third of أَعْلَمَ's, the clause suspended from them (عَلِمْتُ أَقَائِمٌ زَيْدٌ), the ḥāl (جَاءَنِي زَيْدٌ وَهُوَ رَاكِبٌ) — place of naṣb; the
# answer of a jāzim condition after the fāʾ or إِذَا (إِنْ تُكْرِمْنِي فَأَنْتَ مُكْرَمٌ) — place of jazm; the ṣifa of a nakira, the clause joined
# to a single noun or to a sentence with a maḥall, the badal, the tawkīd and the bayān — the follower takes the followed word's iʿrāb.
# So the sentence is of two kinds: read as a single noun (its wording or a maṣdar sense intended) — governed everywhere; not so read —
# governed only in five positions: khabar, object, answer of a jāzim condition with the fāʾ or إِذَا, ḥāl, follower. Print pp. 119–121.
#   python3 author_izhar_ch20.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "mawadi-irab-al-jumla"
K19 = "al-madi-wal-jumla-mamulayn"
TITLE = {"ar": "مَوَاضِعُ إِعْرَابِ الْجُمْلَةِ: الْخَبَرُ وَالْمَفْعُولُ وَالْجَوَابُ وَالْحَالُ وَالتَّابِعُ", "en": "The positions in which a sentence has iʿrāb: khabar, object, answer, ḥāl and follower", "tr": "Cümlenin i'râb aldığı yerler: haber, mef'ûl, cevap, hâl ve tâbi"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; MSD = "masdar"; LN = "la-nafiya"; IN = "inna-wa-akhawatuha"; BD = "badal"; JT = "jam-taksir"; ISH = "asma-al-ishara"; MQ = "ism-maqsur-manqus"; MR = "mudari-marfu"; MJZ = "nawasib-wa-jawazim-al-mudari"; MAW = "ism-mawsul"; JS = "jumla-sifa"; MM = "maful-mutlaq"
KK = "al-kalima-wal-kalam"; SH = "in-shartiyya"; MH = "mahall-al-majrur"; TM = "tamyiz"; IST = "al-istifham"; AMQ = "afal-al-muqaraba"; QLB = "al-mutaaddi-wa-afal-al-qulub"; TWK = "tawkid"; ABY = "atf-bayan"; ALK = "five-nouns"; AMS = "an-masdariyya"; MST = "istithna"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def li_bab(form, lex, en, tr, bab_ar, pos="part", punct=None):
    return tok(form, lex, pos, [K, AT, HJ, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — بَابُ " + bab_ar + ".", en, tr, punct=punct)
def abuhu(role_ar, en, tr, punct=None): return tok("أَبُوهُ", "ab", "noun", [K, ALK, ID, MK], role_ar, en, tr, punct=punct, segments=[seg("أَبُو", "ab", "noun"), pr3ms()])
def qaimun(role_ar, en, tr, punct=None, tags=()): return tok("قَائِمٌ", "qaim", "noun", [K, IFA, MK] + list(tags), role_ar, en, tr, punct=punct)
def fatakun(form_case, case_en, case_tr, punct="؛"):
    return [tok("فَتَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَتَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — الْجُمْلَةُ.", "«so it is» — the sentence.", "«böylece olur» — cümle.", segments=fa("تَكُونُ", "kana", "verb")),
            tok(form_case, {"مَرْفُوعَةَ": "marfua", "مَنْصُوبَةَ": "mansuba", "مَجْزُومَةَ": "majzuma"}[form_case], "noun", [K, KN, ID, IMF, MH], "خَبَرُ تَكُونُ مَنْصُوبٌ، مُضَافٌ.", case_en, case_tr),
            tok("الْمَحَلِّ", "mahall", "noun", [K, ID, MH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of place»", "«mahallen»", punct=punct)]

# ----------- s1 — elsewhere no iʿrāb, save as the khabar of the mubtadaʾ or of إِنَّ's bāb: place of rafʿ
S.append({"id": "s1", "translation": {"en": "And in other than these two positions it has no iʿrāb — unless it stands as the khabar of the mubtada, as in «Zayd — his father is standing», or of inna's bāb, as in «indeed Zayd — his father stood», and so it is in the place of rafʿ;", "tr": "Bu iki yerin dışında cümlenin i'râbı yoktur — ancak mübtedânın haberi olarak gelirse, «Zeyd'in babası ayaktadır» gibi, ya da inne babının haberi olarak, «şüphesiz Zeyd'in babası kalktı» gibi; o zaman mahallen merfûdur;"},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, AT, HJ, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in» — the fronted khabar.", "«ve … -de» — öne alınmış haber.", segments=wa("فِي", "fi", "prep")),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«… dışında»"),
  tok("هٰذَيْنِ", "hadhayn", "pron", [K, ID, ISH, MTH], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«these two»", "«bu iki»"),
  tok("الْمَوْضِعَيْنِ", "mawdi", "noun", [K, BD, MTH], "بَدَلٌ مَجْرُورٌ بِالْيَاءِ — إِرَادَةُ اللَّفْظِ وَإِرَادَةُ الْمَعْنَى الْمَصْدَرِيِّ.", "«positions» — the wording intended, the maṣdar sense intended.", "«yerin» — lafzın ve mastar mânâsının kastı."),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«yok»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«is»", "«olur»"),
  tok("لَهَا", "li", "prep", [K, HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرُ يَكُونُ مُقَدَّمٌ.", "«for it» — the fronted khabar of kāna.", "«onun için» — kâne'nin öne alınmış haberi.", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  tok("إِعْرَابٌ", "irab", "noun", [K, KN, MH], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ.", "«iʿrāb» — the delayed ism of kāna.", "«i'râb» — kâne'nin sonraya bırakılmış ismi."),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ.", "«unless»", "«ancak»"),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("تَقَعْ", "waqaa", "verb", [K, SH, MJZ, FL, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجَوَابُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«it stands» — the protasis; the answer understood.", "«bulunursa» — şart fiili; cevap mahzuf."),
  tok("خَبَرَ", "khabar-predicate", "noun", [K, HL, ID, MK], "حَالٌ مَنْصُوبٌ، مُضَافٌ — أَيْ: خَبَرًا لِلْمُبْتَدَإِ.", "«as the khabar of» — a ḥāl.", "«haberi olarak» — hâl."),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID, MK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtada»", "«mübtedânın»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  abuhu("مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.", "«his father» — the second mubtada; the clause is the first's khabar.", "«babası» — ikinci mübtedâ; cümle ilkinin haberi."),
  qaimun("خَبَرُ الْمُبْتَدَإِ الثَّانِي مَرْفُوعٌ.", "«standing» — the khabar of the second.", "«ayakta» — ikincinin haberi.", punct="،"),
  aw(),
  tok("لِبَابِ", "bab", "noun", [K, AT, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَبَابِ مَجْرُورٌ، مُضَافٌ — مَعْطُوفٌ عَلَى خَبَرَ الْمُبْتَدَإِ بِتَقْدِيرِ: خَبَرًا لِبَابِ.", "«or [the khabar] of the bāb of»", "«veya … babının»", segments=[seg("لِ", "li", "prep"), seg("بَابِ", "bab", "noun")]),
  li_bab("إِنَّ", "inna", "«inna»", "«inne»", "إِنَّ وَأَخَوَاتِهَا", punct="،"),
  nahw(),
  tok("إِنَّ", "inna", "part", [K, IN], "لَفْظٌ مَحْكِيٌّ: حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed»", "«şüphesiz»"),
  tok("زَيْدًا", "zayd", "propn", [K, IN], "اسْمُ إِنَّ مَنْصُوبٌ.", "«Zayd» — the ism of inna.", "«Zeyd» — inne'nin ismi."),
  tok("قَامَ", "qama", "verb", [K, FL, HV, IN], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ خَبَرُ إِنَّ فِي مَحَلِّ رَفْعٍ.", "«stood» — the clause is inna's khabar, in the place of rafʿ.", "«kalktı» — cümle inne'nin haberi, ref' mahallinde."),
  abuhu("فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the doer.", "«babası» — fâil.", punct="،"),
  *fatakun("مَرْفُوعَةَ", "«in rafʿ» — the khabar of «it is».", "«merfû» — tekûnu'nun haberi."),
 ]})
# ----------- s2 — the bāb of كَانَ and كَادَ, the second object of عَلِمَ, the third of أَعْلَمَ
S.append({"id": "s2", "translation": {"en": "or [the khabar] of kāna's bāb, as in «Zayd was — his father is learned», or of kāda, as in «Zayd was about to go out»; or a second object of ʿalima's bāb, as in «Zayd knew ʿAmr — his father is standing», or a third of aʿlama's, as in «Zayd informed ʿAmr of Bakr — his father is standing»;", "tr": "ya da kâne babının haberi, «Zeyd — babası âlimdi» gibi, ya da kâde'nin, «Zeyd nerdeyse çıkıyordu» gibi; ya da alime babının ikinci mef'ûlü, «Zeyd Amr'ı — babası ayaktadır — bildi» gibi, ya da a'leme'nin üçüncüsü, «Zeyd Amr'a Bekir'i — babası ayaktadır — bildirdi» gibi;"},
 "tokens": [
  aw(),
  tok("لِبَابِ", "bab", "noun", [K, AT, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَبَابِ مَجْرُورٌ، مُضَافٌ.", "«[the khabar] of the bāb of»", "«… babının»", segments=[seg("لِ", "li", "prep"), seg("بَابِ", "bab", "noun")]),
  li_bab("كَانَ", "kana", "«kāna»", "«kâne»", "كَانَ وَأَخَوَاتِهَا", pos="verb", punct="،"),
  nahw(),
  tok("كَانَ", "kana", "verb", [K, KN, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ نَاقِصٌ.", "«was»", "«idi»"),
  tok("زَيْدٌ", "zayd", "propn", [K, KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«Zayd» — the ism of kāna.", "«Zeyd» — kâne'nin ismi."),
  abuhu("مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ.", "«his father» — the mubtada of the clause that is kāna's khabar, in the place of naṣb.", "«babası» — kâne'nin haberi olan cümlenin mübtedâsı, nasb mahallinde."),
  tok("عَالِمٌ", "alim-knowing", "noun", [K, MK, IFA], "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ.", "«learned» — the khabar.", "«âlim» — haber.", punct="،"),
  aw(),
  tok("كَادَ", "kada", "verb", [K, AT, AMQ, HV], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى كَانَ: بَابُ كَادَ — أَفْعَالُ الْمُقَارَبَةِ.", "«kāda» — the verbs of approach.", "«kâde» — mukârebe fiilleri.", punct="،"),
  nahw(),
  tok("كَادَ", "kada", "verb", [K, AMQ, HV, KN], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ.", "«was about to»", "«nerdeyse»"),
  tok("زَيْدٌ", "zayd", "propn", [K, AMQ, KN], "اسْمُ كَادَ مَرْفُوعٌ.", "«Zayd» — the ism of kāda.", "«Zeyd» — kâde'nin ismi."),
  tok("يَخْرُجُ", "kharaja", "verb", [K, AMQ, KN, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ كَادَ فِي مَحَلِّ نَصْبٍ.", "«go out» — the clause is kāda's khabar, in the place of naṣb.", "«çıkıyordu» — cümle kâde'nin haberi, nasb mahallinde.", punct="،"),
  aw(),
  tok("مَفْعُولًا", "maful-object", "noun", [K, AT, HL, MB, QLB], "مَعْطُوفٌ عَلَى خَبَرَ مَنْصُوبٌ — حَالٌ.", "«an object» — joined to «as the khabar».", "«mef'ûl» — habere ma'tûf."),
  tok("ثَانِيًا", "thani", "noun", [K, NA, QLB], "نَعْتٌ مَنْصُوبٌ.", "«second»", "«ikinci»"),
  tok("لِبَابِ", "bab", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَبَابِ مَجْرُورٌ، مُضَافٌ.", "«of the bāb of»", "«… babının»", segments=[seg("لِ", "li", "prep"), seg("بَابِ", "bab", "noun")]),
  li_bab("عَلِمَ", "alima", "«ʿalima»", "«alime»", "عَلِمَ — أَفْعَالُ الْقُلُوبِ", pos="verb", punct="،"),
  nahw(),
  tok("عَلِمَ", "alima", "verb", [K, QLB, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مِنْ أَفْعَالِ الْقُلُوبِ.", "«knew»", "«bildi»"),
  tok("زَيْدٌ", "zayd", "propn", [K, QLB, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil."),
  tok("عَمْرٌو", "amr-name", "propn", [K, QLB, MB], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ (كَذَا فِي الطَّبْعَةِ بِالْوَاوِ: عَمْرٌو — وَالْوَجْهُ: عَمْرًا).", "«ʿAmr» — the first object; the print writes عَمْرٌو, the expected form being عَمْرًا.", "«Amr» — birinci mef'ûl; baskı عَمْرٌو yazar, beklenen عَمْرًا."),
  abuhu("مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ الْمَفْعُولُ الثَّانِي فِي مَحَلِّ نَصْبٍ.", "«his father» — the mubtada of the clause that is the second object.", "«babası» — ikinci mef'ûl olan cümlenin mübtedâsı."),
  qaimun("خَبَرٌ مَرْفُوعٌ.", "«standing» — the khabar.", "«ayakta» — haber.", punct="،", tags=[QLB]),
  aw(),
  tok("ثَالِثًا", "thalith", "noun", [K, AT, HL, QLB], "مَعْطُوفٌ عَلَى ثَانِيًا مَنْصُوبٌ — مَفْعُولًا ثَالِثًا.", "«a third» — joined to «second».", "«üçüncü» — sâniyen'e ma'tûf."),
  tok("لِبَابِ", "bab", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَبَابِ مَجْرُورٌ، مُضَافٌ.", "«of the bāb of»", "«… babının»", segments=[seg("لِ", "li", "prep"), seg("بَابِ", "bab", "noun")]),
  li_bab("أَعْلَمَ", "aalama", "«aʿlama»", "«a'leme»", "أَعْلَمَ وَأَرَى — الْمُتَعَدِّي إِلَى ثَلَاثَةٍ", pos="verb", punct="،"),
  nahw(),
  tok("أَعْلَمَ", "aalama", "verb", [K, QLB, FL, F4], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُتَعَدٍّ إِلَى ثَلَاثَةِ مَفَاعِيلَ.", "«informed»", "«bildirdi»"),
  tok("زَيْدٌ", "zayd", "propn", [K, QLB, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil."),
  tok("عَمْرًا", "amr-name", "propn", [K, QLB, MB], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ.", "«ʿAmr» — the first object.", "«Amr» — birinci mef'ûl."),
  tok("بَكْرًا", "bakr", "propn", [K, QLB, MB], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«Bakr» — the second object.", "«Bekir» — ikinci mef'ûl."),
  abuhu("مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ الْمَفْعُولُ الثَّالِثُ فِي مَحَلِّ نَصْبٍ.", "«his father» — the mubtada of the clause that is the third object.", "«babası» — üçüncü mef'ûl olan cümlenin mübtedâsı."),
  qaimun("خَبَرٌ مَرْفُوعٌ.", "«standing» — the khabar.", "«ayakta» — haber.", punct="؛", tags=[QLB]),
 ]})
# ----------- s3 — the suspended clause and the ḥāl: place of naṣb
S.append({"id": "s3", "translation": {"en": "or suspended from them, as in «I knew — is Zayd standing?», or a ḥāl, as in «Zayd came to me while he was riding», and so it is in the place of naṣb;", "tr": "ya da onlardan muallak, «bildim — Zeyd ayakta mı?» gibi, ya da hâl, «Zeyd binmiş hâlde bana geldi» gibi; o zaman mahallen mansûbdur;"},
 "tokens": [
  aw(),
  tok("مُعَلَّقًا", "muallaq", "noun", [K, AT, HL, IMF, QLB], "مَعْطُوفٌ مَنْصُوبٌ — اسْمُ مَفْعُولِ عَلَّقَ: الْجُمْلَةُ الَّتِي عُلِّقَ عَنْهَا فِعْلُ الْقَلْبِ.", "«suspended» — the clause the verb of the heart is suspended from.", "«muallak» — kalp fiilinin ta'lîk edildiği cümle."),
  tok("عَنْهَا", "an", "prep", [K, HJ, QLB], "عَنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — عَنْ أَفْعَالِ الْقُلُوبِ.", "«from them» — from the verbs of the heart.", "«onlardan» — kalp fiillerinden.", punct="،", segments=[seg("عَنْ", "an", "prep"), pr3fs()]),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, QLB, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — عُلِّقَ عَنِ الْعَمَلِ بِالِاسْتِفْهَامِ.", "«I knew» — suspended by the question.", "«bildim» — istifhâmla ta'lîk edildi.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَقَائِمٌ", "qaim", "noun", [K, IST, IFA, MK, QLB], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَقَائِمٌ مُبْتَدَأٌ مَرْفُوعٌ (أَوْ خَبَرٌ مُقَدَّمٌ) — وَالْجُمْلَةُ سَدَّتْ مَسَدَّ الْمَفْعُولَيْنِ فِي مَحَلِّ نَصْبٍ.", "«is … standing» — the clause fills the place of both objects.", "«ayakta mı» — cümle iki mef'ûlün yerini tutar.", segments=[seg("أَ", "a-istifham", "part"), seg("قَائِمٌ", "qaim", "noun")]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL, MK, QLB], "فَاعِلٌ سَدَّ مَسَدَّ الْخَبَرِ مَرْفُوعٌ.", "«Zayd» — the doer that fills the khabar's place.", "«Zeyd» — haberin yerini tutan fâil.", punct="،"),
  aw(),
  tok("حَالًا", "hal", "noun", [K, AT, HL], "مَعْطُوفٌ مَنْصُوبٌ.", "«a ḥāl»", "«hâl»", punct="،"),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL, HL], "فَاعِلٌ مَرْفُوعٌ — صَاحِبُ الْحَالِ.", "«Zayd» — the doer; the owner of the ḥāl.", "«Zeyd» — fâil; hâl sahibi."),
  tok("وَهُوَ", "huwa", "pron", [K, HL, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — وَالْجُمْلَةُ حَالٌ فِي مَحَلِّ نَصْبٍ.", "«while he» — the wāw of the ḥāl; the clause in the place of naṣb.", "«o … iken» — hâl vâvı; cümle nasb mahallinde.", segments=wa("هُوَ", "huwa", "pron")),
  tok("رَاكِبٌ", "rakib", "noun", [K, MK, IFA, HL], "خَبَرٌ مَرْفُوعٌ.", "«riding» — the khabar.", "«binmiş» — haber.", punct="،"),
  *fatakun("مَنْصُوبَةَ", "«in naṣb»", "«mansûb»"),
 ]})
# ----------- s4 — the answer of a jāzim condition after the fāʾ or إِذَا: place of jazm
S.append({"id": "s4", "translation": {"en": "or the answer of a jāzim condition, after the fāʾ or idhā, as in «if you honour me, then you are honoured», and so it is in the place of jazm;", "tr": "ya da fâ veya izâ'dan sonra câzim şartın cevabı, «bana ikram edersen sen ikram görmüşsün» gibi; o zaman mahallen meczûmdur;"},
 "tokens": [
  aw(),
  tok("جَوَابًا", "jawab", "noun", [K, AT, HL, SH], "مَعْطُوفٌ مَنْصُوبٌ.", "«an answer»", "«cevap»"),
  tok("لِشَرْطٍ", "shart", "noun", [K, HJ, SH], "اللَّامُ حَرْفُ جَرٍّ، وَشَرْطٍ مَجْرُورٌ.", "«of a condition»", "«şartın»", segments=[seg("لِ", "li", "prep"), seg("شَرْطٍ", "shart", "noun")]),
  tok("جَازِمٍ", "jazim", "noun", [K, NA, MJZ, IFA], "نَعْتٌ مَجْرُورٌ.", "«jāzim» — a naʿt.", "«câzim» — na't."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«-den sonra»"),
  tok("الْفَاءِ", "fa-letter", "noun", [K, ID, SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاءُ الْجَزَاءِ.", "«the fāʾ» — of the apodosis.", "«fâ» — cezâ fâsı."),
  aw(),
  tok("إِذَا", "idha-fujaiyya", "part", [K, AT, SH], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى الْفَاءِ — إِذَا الْفُجَائِيَّةُ.", "«idhā» — the idhā of surprise.", "«izâ» — fücâiyye izâ.", punct="،"),
  nahw(),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "لَفْظٌ مَحْكِيٌّ: حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("تُكْرِمْنِي", "akrama", "verb", [K, SH, MJZ, FL, MB, F4], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you honour me»", "«bana ikram edersen»", segments=[seg("تُكْرِمْ", "akrama", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("فَأَنْتَ", "anta", "pron", [K, SH, MK], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَأَنْتَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«then you» — the apodosis clause in the place of jazm.", "«o hâlde sen» — cezm mahallinde cevap cümlesi.", segments=fa("أَنْتَ", "anta", "pron")),
  tok("مُكْرَمٌ", "mukram", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ أَكْرَمَ.", "«honoured» — the khabar.", "«ikram görmüş» — haber.", punct="،"),
  *fatakun("مَجْزُومَةَ", "«in jazm»", "«meczûm»"),
 ]})
# ----------- s5 — the ṣifa of a nakira, the clause joined to a single noun or to a sentence with a maḥall
S.append({"id": "s5", "translation": {"en": "or a ṣifa of an indefinite noun, as in «there came to me a man — his father is standing»; or joined to a single noun, as in «Zayd is striking and kills», or to a sentence that has a place in the iʿrāb, as in «Zayd — his father is standing and his son is sitting»;", "tr": "ya da nekrenin sıfatı, «bana babası ayakta olan bir adam geldi» gibi; ya da müfrede ma'tûf, «Zeyd vurucudur ve öldürür» gibi, ya da i'râbdan mahalli olan bir cümleye ma'tûf, «Zeyd — babası ayaktadır ve oğlu oturmaktadır» gibi;"},
 "tokens": [
  aw(),
  tok("صِفَةً", "sifa", "noun", [K, AT, HL, NA, JS], "مَعْطُوفٌ مَنْصُوبٌ.", "«a ṣifa»", "«sıfat»"),
  tok("لِنَكِرَةٍ", "nakira", "noun", [K, HJ, JS], "اللَّامُ حَرْفُ جَرٍّ، وَنَكِرَةٍ مَجْرُورٌ.", "«of an indefinite noun»", "«nekrenin»", punct="،", segments=[seg("لِ", "li", "prep"), seg("نَكِرَةٍ", "nakira", "noun")]),
  nahw(),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("رَجُلٌ", "rajul", "noun", [K, FL, JS], "فَاعِلٌ مَرْفُوعٌ — الْمَوْصُوفُ.", "«a man» — the doer, described.", "«bir adam» — fâil, mevsûf."),
  abuhu("مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ صِفَةُ رَجُلٍ فِي مَحَلِّ رَفْعٍ.", "«his father» — the clause is the ṣifa of «a man», in the place of rafʿ.", "«babası» — cümle racül'ün sıfatı, ref' mahallinde."),
  qaimun("خَبَرٌ مَرْفُوعٌ.", "«standing» — the khabar.", "«ayakta» — haber.", punct="،", tags=[JS]),
  aw(),
  tok("مَعْطُوفَةً", "matuf", "noun", [K, AT, HL, IMF], "مَعْطُوفٌ عَلَى صِفَةً مَنْصُوبٌ.", "«joined»", "«ma'tûf»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مُفْرَدٍ", "mufrad", "noun", [K, HJ, IMF], "مَجْرُورٌ بِعَلَى.", "«a single noun»", "«müfrede»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("ضَارِبٌ", "darib", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ — الْمُفْرَدُ الْمَعْطُوفُ عَلَيْهِ.", "«striking» — the khabar: the single noun joined to.", "«vurucu» — haber: kendisine atfedilen müfred."),
  tok("وَيَقْتُلُ", "qatala", "verb", [K, AT, FL, MR], "الْوَاوُ عَاطِفَةٌ، وَيَقْتُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى ضَارِبٌ فِي مَحَلِّ رَفْعٍ.", "«and kills» — the clause joined to «striking», in the place of rafʿ.", "«ve öldürür» — dârib'e ma'tûf cümle, ref' mahallinde.", punct="،", segments=wa("يَقْتُلُ", "qatala", "verb")),
  aw(),
  tok("جُمْلَةٍ", "jumla", "noun", [K, AT, HJ, KK], "مَعْطُوفٌ عَلَى مُفْرَدٍ مَجْرُورٌ.", "«a sentence» — joined to «a single noun».", "«cümle» — müfred'e ma'tûf."),
  tok("لَهَا", "li", "prep", [K, HJ, MK, JS], "اللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ؛ وَالْجُمْلَةُ نَعْتٌ لِجُمْلَةٍ.", "«that has» — the fronted khabar of the ṣifa clause.", "«… olan» — sıfat cümlesinin öne alınmış haberi.", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  tok("مَحَلٌّ", "mahall", "noun", [K, MK, MH], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a place» — the delayed mubtada.", "«mahal» — sonraya bırakılmış mübtedâ."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-dan»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, HJ, MH], "مَجْرُورٌ بِمِنْ.", "«the iʿrāb»", "«i'râb»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  abuhu("مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«his father» — the second mubtada; the clause is the khabar.", "«babası» — ikinci mübtedâ; cümle haber."),
  qaimun("خَبَرُ الثَّانِي مَرْفُوعٌ.", "«standing»", "«ayakta»"),
  tok("وَابْنُهُ", "ibn", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَابْنُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الْخَبَرِ فِي مَحَلِّ رَفْعٍ.", "«and his son» — the joined clause, in the place of rafʿ.", "«ve oğlu» — ma'tûf cümle, ref' mahallinde.", segments=[seg("وَ", "wa", "conj"), seg("ابْنُ", "ibn", "noun"), pr3ms()]),
  tok("قَاعِدٌ", "qaid", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«sitting» — the khabar.", "«oturmakta» — haber.", punct="؛"),
 ]})
# ----------- s6 — the badal, the tawkīd and the bayān: the follower's iʿrāb
S.append({"id": "s6", "translation": {"en": "or a badal of one of the two, or a tawkīd of the second, or a bayān of it on one view — and so its iʿrāb is according to the iʿrāb of the word it follows.", "tr": "ya da ikisinden birinin bedeli, ya da ikincinin te'kîdi, ya da bir görüşe göre onun beyânı — o zaman i'râbı, tâbi olduğu kelimenin i'râbına göredir."},
 "tokens": [
  aw(),
  tok("بَدَلًا", "badal", "noun", [K, AT, HL, BD], "مَعْطُوفٌ مَنْصُوبٌ.", "«a badal»", "«bedel»"),
  tok("مِنْ", "min", "prep", [K, HJ, BD], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("أَحَدِهِمَا", "ahad", "noun", [K, HJ, ID, MTH], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — الْمُفْرَدِ أَوِ الْجُمْلَةِ.", "«one of the two» — the single noun or the sentence.", "«ikisinden biri» — müfred veya cümle.", segments=[seg("أَحَدِ", "ahad", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  aw(),
  tok("تَأْكِيدًا", "tawkid", "noun", [K, AT, HL, TWK, MSD], "مَعْطُوفٌ مَنْصُوبٌ.", "«a tawkīd»", "«te'kîd»"),
  tok("لِلثَّانِيَةِ", "thani", "noun", [K, HJ, TWK], "اللَّامُ حَرْفُ جَرٍّ، وَالثَّانِيَةِ مَجْرُورٌ — الْجُمْلَةِ.", "«of the second» — the sentence.", "«ikincinin» — cümlenin.", segments=[seg("لِ", "li", "prep"), seg("الثَّانِيَةِ", "thani", "noun")]),
  aw(),
  tok("بَيَانًا", "bayan", "noun", [K, AT, HL, ABY, MSD], "مَعْطُوفٌ مَنْصُوبٌ — عَطْفَ بَيَانٍ.", "«a bayān» — the explicative apposition.", "«beyân» — atf-ı beyân."),
  tok("لَهَا", "li", "prep", [K, HJ, ABY], "اللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«of it»", "«onun»", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«… göre»"),
  tok("رَأْيٍ", "ray", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى — عَلَى قَوْلٍ لِبَعْضِهِمْ.", "«one view» — the view of some.", "«bir görüş» — bazılarının görüşü.", punct="،"),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«and so is»", "«böylece olur»", segments=fa("يَكُونُ", "kana", "verb")),
  tok("إِعْرَابُهَا", "irab", "noun", [K, KN, ID], "اسْمُ يَكُونُ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its iʿrāb» — the ism of kāna.", "«i'râbı» — kâne'nin ismi.", segments=[seg("إِعْرَابُ", "irab", "noun"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — خَبَرُ يَكُونُ.", "«according to» — the khabar of kāna.", "«… göre» — kâne'nin haberi."),
  tok("حَسَبِ", "hasab", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the measure of»", "«… göre»"),
  tok("إِعْرَابِ", "irab", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the iʿrāb of»", "«i'râbına»"),
  tok("الْمَتْبُوعِ", "matbu", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ تَبِعَ: الْمَوْصُوفُ وَالْمَعْطُوفُ عَلَيْهِ وَالْمُبْدَلُ مِنْهُ وَالْمُؤَكَّدُ.", "«the word followed» — the described, the joined-to, the replaced, the confirmed.", "«metbû» — mevsûf, ma'tûfun aleyh, mübdelün minh, müekked.", punct="."),
 ]})
# ----------- s7 — so the sentence is of two kinds: read as a single noun …
S.append({"id": "s7", "translation": {"en": "So it has appeared from this whole that the sentence is of two kinds: a kind read as a single noun, which therefore has iʿrāb in every position — and that too is of two kinds: what its wording is intended by, and what a maṣdar's sense is intended by;", "tr": "Böylece bu bütünden cümlenin iki kısım olduğu ortaya çıktı: müfred te'vilinde olan kısım — bu yüzden her yerde i'râbı vardır — ki o da iki kısımdır: lafzı kastedilen ve mastar mânâsı kastedilen;"},
 "tokens": [
  tok("فَظَهَرَ", "zahara", "verb", [K, AT, FL], "الْفَاءُ لِلتَّفْرِيعِ، وَظَهَرَ فِعْلٌ مَاضٍ.", "«so it has appeared»", "«böylece ortaya çıktı»", segments=fa("ظَهَرَ", "zahara", "verb")),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("هٰذِهِ", "hadhihi", "pron", [K, HJ, ISH], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("الْجُمْلَةِ", "jumla", "noun", [K, BD], "بَدَلٌ مَجْرُورٌ — بِمَعْنَى: الْمَجْمُوعِ.", "«whole» — the sum of what was said.", "«bütün» — söylenenlerin toplamı."),
  tok("أَنَّ", "anna", "part", [K, IN, FL], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ ظَهَرَ.", "«that» — the clause is the doer of «appeared».", "«ki» — cümle zahera'nın fâili."),
  tok("الْجُمْلَةَ", "jumla", "noun", [K, IN, KK], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the sentence» — the ism of anna.", "«cümle» — enne'nin ismi."),
  tok("قِسْمَانِ", "qism", "noun", [K, IN, MTH], "خَبَرُ أَنَّ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two kinds» — the khabar of anna.", "«iki kısım» — enne'nin haberi.", punct=":"),
  tok("قِسْمٌ", "qism", "noun", [K, MK, HT], "مُبْتَدَأٌ مَرْفُوعٌ (نَكِرَةٌ مَوْصُوفَةٌ).", "«a kind» — the mubtada.", "«bir kısım» — mübtedâ."),
  tok("فِي", "fi", "prep", [K, HJ, NA], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ (أَوْ خَبَرٌ).", "«in»", "«-de»"),
  tok("تَأْوِيلِ", "tawil", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the reading of»", "«te'vilinde»"),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a single noun»", "«müfred»"),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«which therefore has»", "«bu yüzden olur»", segments=fa("يَكُونُ", "kana", "verb")),
  tok("لَهُ", "li", "prep", [K, HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرُ يَكُونُ مُقَدَّمٌ.", "«for it»", "«onun için»", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("إِعْرَابٌ", "irab", "noun", [K, KN, MH], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ.", "«iʿrāb»", "«i'râb»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("كُلِّ", "kull", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«every»", "«her»"),
  tok("مَوْضِعٍ", "mawdi", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«position»", "«yerde»", punct="،"),
  tok("وَذٰلِكَ", "dhalika", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("ذٰلِكَ", "dhalika", "pron")),
  tok("أَيْضًا", "aydan", "noun", [K, MM], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ.", "«too»", "«da»"),
  tok("قِسْمَانِ", "qism", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds» — the khabar.", "«iki kısım» — haber.", punct=":"),
  tok("مَا", "ma-mawsula", "pron", [K, MK, HT, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا مَا.", "«what» — the khabar of a dropped «one of them».", "«… olan» — hazfedilmiş «biri»nin haberi."),
  tok("أُرِيدَ", "arada", "verb", [K, NF, F4, HV, MAW], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is intended» — the relative clause.", "«kastedilen» — sıla."),
  tok("بِهِ", "bi", "prep", [K, HJ, MAW], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«by it»", "«onunla»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("لَفْظُهُ", "lafz", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its wording» — the deputy doer.", "«lafzı» — nâib-i fâil.", segments=[seg("لَفْظُ", "lafz", "noun"), pr3ms()]),
  tok("وَمَا", "ma-mawsula", "pron", [K, AT, MAW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and what»", "«ve … olan»", segments=wa("مَا", "ma-mawsula", "pron")),
  tok("أُرِيدَ", "arada", "verb", [K, NF, F4, HV, MAW], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is intended»", "«kastedilen»"),
  tok("بِهِ", "bi", "prep", [K, HJ, MAW], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«by it»", "«onunla»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("مَعْنًى", "mana", "noun", [K, NF, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«a sense»", "«bir mânâ»"),
  tok("مَصْدَرِيٌّ", "masdari", "noun", [K, NA, MSD], "نَعْتٌ مَرْفُوعٌ.", "«of a maṣdar»", "«mastarî»", punct="؛"),
 ]})
# ----------- s8 — … and a kind not so read: governed only in five positions
S.append({"id": "s8", "translation": {"en": "and a kind of sentence not read as a single noun, which is therefore governed only in five positions: a khabar, an object, the answer of a jāzim condition with the fāʾ or idhā, a ḥāl, and a follower.", "tr": "ve müfred te'vilinde olmayan bir kısım cümle, ki ancak beş yerde ma'mûl olur: haber, mef'ûl, fâ veya izâ ile câzim şartın cevabı, hâl ve tâbi."},
 "tokens": [
  tok("وَقِسْمٌ", "qism", "noun", [K, AT, MK, HT], "الْوَاوُ عَاطِفَةٌ، وَقِسْمٌ مَعْطُوفٌ عَلَى قِسْمٌ مَرْفُوعٌ.", "«and a kind»", "«ve bir kısım»", segments=wa("قِسْمٌ", "qism", "noun")),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of»", "«-den»"),
  tok("الْجُمْلَةِ", "jumla", "noun", [K, HJ, KK], "مَجْرُورٌ بِمِنْ.", "«the sentence»", "«cümle»"),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR, NA], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ لِقِسْمٌ.", "«is» — the ṣifa clause.", "«olan» — sıfat cümlesi."),
  tok("فِي", "fi", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — خَبَرُ يَكُونُ.", "«in»", "«-de»"),
  tok("تَأْوِيلِ", "tawil", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the reading of»", "«te'vilinde»"),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a single noun»", "«müfred»", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, AT, LN], "الْفَاءُ لِلسَّبَبِيَّةِ، وَلَا نَافِيَةٌ.", "«and so not»", "«bu yüzden -maz»", segments=fa("لَا", "la-nafiya", "part")),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«is»", "«olur»"),
  tok("مَعْمُولَةً", "mamul", "noun", [K, KN, IMF], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«governed»", "«ma'mûl»"),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ — الِاسْتِثْنَاءُ مُفَرَّغٌ.", "«except»", "«ancak»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("خَمْسَةِ", "khamsa", "noun", [K, HJ, ID, TM], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«five»", "«beş»"),
  tok("مَوَاضِعَ", "mawdi", "noun", [K, ID, JT, TM, "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«positions» — the diptote plural.", "«yerde» — gayr-i munsarif çoğul.", punct=":"),
  tok("خَبَرٌ", "khabar-predicate", "noun", [K, MK, HT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ: أَحَدُهَا خَبَرٌ.", "«a khabar» — the khabar of a dropped «one of them».", "«haber» — hazfedilmiş «biri»nin haberi."),
  tok("وَمَفْعُولٌ", "maful-object", "noun", [K, AT, MB], "الْوَاوُ عَاطِفَةٌ، وَمَفْعُولٌ مَعْطُوفٌ مَرْفُوعٌ.", "«an object»", "«mef'ûl»", segments=wa("مَفْعُولٌ", "maful-object", "noun")),
  tok("وَجَوَابُ", "jawab", "noun", [K, AT, ID, SH], "الْوَاوُ عَاطِفَةٌ، وَجَوَابُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«the answer of»", "«cevabı»", segments=wa("جَوَابُ", "jawab", "noun")),
  tok("شَرْطٍ", "shart", "noun", [K, ID, SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a condition»", "«şartın»"),
  tok("جَازِمٍ", "jazim", "noun", [K, NA, MJZ], "نَعْتٌ مَجْرُورٌ.", "«jāzim»", "«câzim»"),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("الْفَاءِ", "fa-letter", "noun", [K, ID, SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the fāʾ»", "«fâ»"),
  aw(),
  tok("إِذَا", "idha-fujaiyya", "part", [K, AT, SH], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى الْفَاءِ.", "«idhā»", "«izâ»"),
  tok("وَحَالٌ", "hal", "noun", [K, AT, HL], "الْوَاوُ عَاطِفَةٌ، وَحَالٌ مَعْطُوفٌ مَرْفُوعٌ.", "«a ḥāl»", "«hâl»", segments=wa("حَالٌ", "hal", "noun")),
  tok("وَتَابِعٌ", "tabi", "noun", [K, AT, IFA], "الْوَاوُ عَاطِفَةٌ، وَتَابِعٌ مَعْطُوفٌ مَرْفُوعٌ — النَّعْتُ وَالْعَطْفُ وَالْبَدَلُ وَالتَّأْكِيدُ وَالْبَيَانُ.", "«a follower» — naʿt, ʿaṭf, badal, tawkīd, bayān.", "«tâbi» — na't, atıf, bedel, te'kîd, beyân.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

NEW = {
 "marfua": G("marfua", "مَرْفُوعَة", "ر ف ع", "noun", "in the nominative (feminine of marfūʿ)", "merfû (müennes)", 2),
 "majzuma": G("majzuma", "مَجْزُومَة", "ج ز م", "noun", "in the jussive (feminine of majzūm) — مَجْزُومَةُ الْمَحَلِّ", "meczûm (müennes) — meczûmetü'l-mahall", 3),
 "muallaq": G("muallaq", "مُعَلَّق", "ع ل ق", "noun", "suspended (ism mafʿūl of عَلَّقَ) — the clause a verb of the heart is suspended from", "muallak (alleka'nın ism-i mef'ûlü) — kalp fiilinin ta'lîk edildiği cümle", 4, form="II"),
 "mukram": G("mukram", "مُكْرَم", "ك ر م", "noun", "honoured (ism mafʿūl of أَكْرَمَ)", "ikram görmüş (ekreme'nin ism-i mef'ûlü)", 3, form="IV"),
 "matbu": G("matbu", "مَتْبُوع", "ت ب ع", "noun", "the word followed (matbūʿ) — what a follower takes its iʿrāb from", "metbû — tâbinin i'râbını aldığı kelime", 3),
 "aalama": G("aalama", "أَعْلَمَ", "ع ل م", "verb", "to inform, to let know (three objects)", "bildirmek (üç mef'ûl)", 3, form="IV"),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (masculine singular)", "sen", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
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
put_morph(mo, "aalama", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْلَم", "عْلِم", "أَعْلِم", "إِعْلَام", "مُعْلِم", "مُعْلَم", "أُعْلِمَ", "يُعْلَمُ", "مُتَعَدٍّ إِلَى ثَلَاثَةِ مَفَاعِيلَ: أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا قَائِمًا."))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch20 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("waqaa", "kana", "qama", "kada", "kharaja", "alima", "aalama", "jaa", "akrama", "qatala", "zahara", "arada") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "مَوَاضِعُ إِعْرَابِ الْجُمْلَةِ الَّتِي لَيْسَتْ فِي تَأْوِيلِ الْمُفْرَدِ", "en": "The positions in which a sentence not read as a single noun has a place in the iʿrāb", "tr": "Müfred te'vilinde olmayan cümlenin i'râbdan mahalli olduğu yerler"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الباب الثاني في المعمول: الجملة", "مغني اللبيب لابن هشام — الباب الثاني: الجمل التي لها محل من الإعراب", "شرح ابن عقيل — الجمل"],
 "amil": "a sentence not read as a single noun is governed only in five positions — the khabar (of the mubtadaʾ and of إِنَّ's bāb: rafʿ; of كَانَ's and كَادَ's bāb: naṣb), the object (the second of عَلِمَ, the third of أَعْلَمَ, the suspended clause: naṣb), the ḥāl (naṣb), the answer of a jāzim condition after the fāʾ or إِذَا (jazm), and the follower (ṣifa of a nakira, ʿaṭf on a single noun or on a sentence with a maḥall, badal, tawkīd, bayān: the followed word's iʿrāb)",
 "question": {
  "en": ["Where has a sentence that is NOT read as a single noun a place in the iʿrāb? In five positions only: khabar, object, answer of a jāzim condition with the fāʾ or idhā, ḥāl, and follower. Elsewhere it has no iʿrāb at all.",
         "Which khabar-sentences are in the place of rafʿ? The khabar of the mubtadaʾ (زَيْدٌ أَبُوهُ قَائِمٌ) and of inna's bāb (إِنَّ زَيْدًا قَامَ أَبُوهُ).",
         "Which are in the place of naṣb? The khabar of kāna's bāb (كَانَ زَيْدٌ أَبُوهُ عَالِمٌ) and of kāda's (كَادَ زَيْدٌ يَخْرُجُ); the second object of ʿalima's bāb (عَلِمَ زَيْدٌ عَمْرًا أَبُوهُ قَائِمٌ) and the third of aʿlama's (أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا أَبُوهُ قَائِمٌ); the clause the verb of the heart is suspended from (عَلِمْتُ أَقَائِمٌ زَيْدٌ); and the ḥāl (جَاءَنِي زَيْدٌ وَهُوَ رَاكِبٌ).",
         "Which is in the place of jazm? The answer of a jāzim condition after the fāʾ or idhā: إِنْ تُكْرِمْنِي فَأَنْتَ مُكْرَمٌ.",
         "And the follower? The ṣifa of an indefinite noun (جَاءَنِي رَجُلٌ أَبُوهُ قَائِمٌ), the clause joined to a single noun (زَيْدٌ ضَارِبٌ وَيَقْتُلُ) or to a sentence with a maḥall (زَيْدٌ أَبُوهُ قَائِمٌ وَابْنُهُ قَاعِدٌ), the badal of either, the tawkīd of the second, the bayān of it on one view — each takes the iʿrāb of the word it follows.",
         "What is the sum? The sentence is of two kinds: read as a single noun (its wording or a maṣdar sense intended) and so governed in every position; or not so read, and governed only in the five positions.",
         "Why does the print have عَمْرٌو in the example of ʿalima? The lithograph writes عمرو with its silent wāw where the first object wants عَمْرًا; the reader keeps the print's form and says so in the iʿrāb.",
         "What does the engine READ here? The DabtEngine raises the inner mubtadaʾ and khabar of every clause, reads أَبُوهُ by its wāw, keeps the quoted particles and verbs, declines the five diptote مَوَاضِعَ on the fatḥa, and gives the apodosis after the fāʾ its own mubtadaʾ and khabar."],
  "tr": ["Müfred te'vilinde OLMAYAN cümlenin i'râbdan mahalli nerede olur? Yalnız beş yerde: haber, mef'ûl, fâ veya izâ ile câzim şartın cevabı, hâl ve tâbi. Başka yerde i'râbı hiç yoktur.",
         "Hangi haber cümleleri ref' mahallindedir? Mübtedânın haberi (Zeydün ebûhu kâimün) ve inne babının haberi (inne Zeyden kâme ebûhu).",
         "Hangileri nasb mahallindedir? Kâne babının haberi (kâne Zeydün ebûhu âlimün) ve kâde'nin (kâde Zeydün yahrucu); alime babının ikinci mef'ûlü (alime Zeydün Amran ebûhu kâimün) ve a'leme'nin üçüncüsü (a'leme Zeydün Amran Bekran ebûhu kâimün); kalp fiilinin ta'lîk edildiği cümle (alimtü e-kâimün Zeydün); ve hâl (câenî Zeydün ve hüve râkibün).",
         "Hangisi cezm mahallindedir? Fâ veya izâ'dan sonra câzim şartın cevabı: in tükrimnî fe-ente mükramün.",
         "Tâbi? Nekrenin sıfatı (câenî racülün ebûhu kâimün), müfrede (Zeydün dâribün ve yaktülü) ya da mahalli olan cümleye ma'tûf cümle (Zeydün ebûhu kâimün vebnühu kâidün), ikisinden birinin bedeli, ikincinin te'kîdi, bir görüşe göre beyânı — her biri tâbi olduğu kelimenin i'râbını alır.",
         "Netice? Cümle iki kısımdır: müfred te'vilinde olan (lafzı veya mastar mânâsı kastedilen) — her yerde ma'mûl; öyle olmayan — yalnız beş yerde ma'mûl.",
         "Baskıda alime örneğinde niçin عَمْرٌو var? Taşbaskı birinci mef'ûlün عَمْرًا istediği yerde sessiz vâvlı عمرو yazar; okuyucu baskının şeklini korur ve i'râbda söyler.",
         "Motor burada neyi OKUR? DabtEngine her cümlenin iç mübtedâ ve haberini ref' eder, ebûhu'yu vâvıyla okur, hikâye edilen harf ve fiilleri tutar, gayr-i munsarif mevâdıa'yı fetha ile çeker ve fâ'dan sonraki cevaba kendi mübtedâ ve haberini verir."],
 },
 "plain": {"en": "A sentence can sit inside another sentence and take its slot: as the predicate («Zayd — his father is standing»), as an object («I knew — is Zayd standing?»), as the answer to «if», as a «while» clause, or as a follower. There the whole clause counts as raised, accusative or jussive; elsewhere a clause has no case.",
           "tr": "Bir cümle başka bir cümlenin içinde durup onun yerini alabilir: haber olarak («Zeyd — babası ayaktadır»), mef'ûl olarak («bildim — Zeyd ayakta mı?»), «eğer»in cevabı, «iken» cümlesi ya da bir ismin tâbii olarak. Bu yerlerde bütün cümle merfû, mansûb veya meczûm sayılır; başka yerde cümlenin i'râbı yoktur."},
 "explanation": {"en": "Outside the two positions of the single-noun reading, a sentence has no iʿrāb unless it stands as the khabar of the mubtadaʾ (زَيْدٌ أَبُوهُ قَائِمٌ) or of inna's bāb (إِنَّ زَيْدًا قَامَ أَبُوهُ) — the place of rafʿ; as the khabar of kāna's bāb (كَانَ زَيْدٌ أَبُوهُ عَالِمٌ) or of kāda (كَادَ زَيْدٌ يَخْرُجُ), as the second object of ʿalima's bāb (عَلِمَ زَيْدٌ عَمْرًا أَبُوهُ قَائِمٌ) or the third of aʿlama's (أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا أَبُوهُ قَائِمٌ), as the clause suspended from them (عَلِمْتُ أَقَائِمٌ زَيْدٌ) or as a ḥāl (جَاءَنِي زَيْدٌ وَهُوَ رَاكِبٌ) — the place of naṣb; as the answer of a jāzim condition after the fāʾ or idhā (إِنْ تُكْرِمْنِي فَأَنْتَ مُكْرَمٌ) — the place of jazm; or as a ṣifa of an indefinite noun (جَاءَنِي رَجُلٌ أَبُوهُ قَائِمٌ), joined to a single noun (زَيْدٌ ضَارِبٌ وَيَقْتُلُ) or to a sentence with a maḥall (زَيْدٌ أَبُوهُ قَائِمٌ وَابْنُهُ قَاعِدٌ), a badal of either, a tawkīd of the second or a bayān of it on one view — its iʿrāb then follows the followed word's. So the sentence is of two kinds: read as a single noun, with iʿrāb everywhere (its wording or a maṣdar sense intended), and not so read, governed only in five positions — khabar, object, the answer of a jāzim condition with the fāʾ or idhā, ḥāl and follower.",
                 "tr": "Müfred te'vilinin iki yeri dışında cümlenin i'râbı yoktur; ancak mübtedânın (Zeydün ebûhu kâimün) veya inne babının haberi (inne Zeyden kâme ebûhu) olursa — ref' mahalli; kâne babının (kâne Zeydün ebûhu âlimün) veya kâde'nin haberi (kâde Zeydün yahrucu), alime babının ikinci (alime Zeydün Amran ebûhu kâimün) veya a'leme'nin üçüncü mef'ûlü (a'leme Zeydün Amran Bekran ebûhu kâimün), onlardan muallak cümle (alimtü e-kâimün Zeydün) ya da hâl (câenî Zeydün ve hüve râkibün) olursa — nasb mahalli; fâ veya izâ'dan sonra câzim şartın cevabı olursa (in tükrimnî fe-ente mükramün) — cezm mahalli; ya da nekrenin sıfatı (câenî racülün ebûhu kâimün), müfrede (Zeydün dâribün ve yaktülü) veya mahalli olan cümleye ma'tûf (Zeydün ebûhu kâimün vebnühu kâidün), ikisinden birinin bedeli, ikincinin te'kîdi veya bir görüşe göre beyânı olursa — i'râbı metbûunkine göredir. Böylece cümle iki kısımdır: müfred te'vilinde olan, her yerde i'râblı (lafzı veya mastar mânâsı kastedilen); ve öyle olmayan, yalnız beş yerde ma'mûl — haber, mef'ûl, fâ veya izâ ile câzim şartın cevabı, hâl ve tâbi."},
 "examples": [
  {"ar": "زَيْدٌ أَبُوهُ قَائِمٌ", "en": "the khabar-sentence of the mubtadaʾ: place of rafʿ", "tr": "mübtedânın haber cümlesi: ref' mahalli", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "كَادَ زَيْدٌ يَخْرُجُ", "en": "the khabar of kāda: place of naṣb", "tr": "kâde'nin haberi: nasb mahalli", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "عَلِمْتُ أَقَائِمٌ زَيْدٌ", "en": "the suspended clause filling the two objects' place", "tr": "iki mef'ûlün yerini tutan muallak cümle", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "جَاءَنِي زَيْدٌ وَهُوَ رَاكِبٌ", "en": "the ḥāl-sentence with its wāw", "tr": "vâvlı hâl cümlesi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "إِنْ تُكْرِمْنِي فَأَنْتَ مُكْرَمٌ", "en": "the apodosis after the fāʾ: place of jazm", "tr": "fâ'dan sonra cevap: cezm mahalli", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "زَيْدٌ ضَارِبٌ وَيَقْتُلُ", "en": "the clause joined to a single noun", "tr": "müfrede ma'tûf cümle", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "خَبَرٌ وَمَفْعُولٌ وَجَوَابُ شَرْطٍ جَازِمٍ مَعَ الْفَاءِ أَوْ إِذَا وَحَالٌ وَتَابِعٌ", "en": "the five positions", "tr": "beş yer", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٌ أَبَاهُ قَائِمٌ", "right": "زَيْدٌ أَبُوهُ قَائِمٌ", "why": {"en": "the inner mubtadaʾ keeps its rafʿ; the place of rafʿ belongs to the clause as a whole", "tr": "iç mübtedâ ref'ini korur; ref' mahalli cümlenin bütününündür"}},
  {"wrong": "إِنْ تُكْرِمْنِي أَنْتَ مُكْرَمٌ", "right": "إِنْ تُكْرِمْنِي فَأَنْتَ مُكْرَمٌ", "why": {"en": "a nominal apodosis needs the fāʾ (or idhā) to take the place of jazm", "tr": "isim cümlesi olan cevap cezm mahalli için fâ (veya izâ) ister"}},
  {"wrong": "جَاءَنِي زَيْدٌ هُوَ رَاكِبٌ", "right": "جَاءَنِي زَيْدٌ وَهُوَ رَاكِبٌ", "why": {"en": "the nominal ḥāl-clause is bound by the wāw (or a pronoun)", "tr": "isim cümlesi olan hâl, vâv (veya zamir) ile bağlanır"}},
 ],
}
ADD_EN = (" Chapter 20 (print pp. 119-121): the positions in which a sentence not read as a single noun has a place in the iʿrāb — the khabar of the mubtadaʾ and of inna's bāb, rafʿ (s1); of kāna's and kāda's bāb, the second object of ʿalima's and the third of aʿlama's (s2), the suspended clause and the ḥāl, naṣb (s3); the answer of a jāzim condition after the fāʾ or idhā, jazm (s4); the ṣifa of a nakira, the clause joined to a single noun or to a sentence with a maḥall (s5), the badal, the tawkīd and the bayān with the followed word's iʿrāb (s6); the sum: two kinds of sentence (s7), the five positions (s8). The print's عَمْرٌو in عَلِمَ زَيْدٌ عَمْرٌو أَبُوهُ قَائِمٌ is kept and flagged.")
ADD_TR = (" Yirminci bab (baskı s. 119-121): müfred te'vilinde olmayan cümlenin i'râbdan mahalli olduğu yerler — mübtedânın ve inne babının haberi, ref' (s1); kâne ve kâde babının haberi, alime'nin ikinci ve a'leme'nin üçüncü mef'ûlü (s2), muallak cümle ve hâl, nasb (s3); fâ veya izâ'dan sonra câzim şartın cevabı, cezm (s4); nekrenin sıfatı, müfrede veya mahalli olan cümleye ma'tûf cümle (s5), metbûun i'râbıyla bedel, te'kîd ve beyân (s6); netice: iki kısım cümle (s7), beş yer (s8). Baskının عَلِمَ زَيْدٌ عَمْرٌو أَبُوهُ قَائِمٌ'deki عَمْرٌو'su korundu ve işaretlendi.")
write_out(20, S, TITLE, ADD_EN, ADD_TR, "pp. 119-121", GLOSS_ADD, notes=(NOTE,),
          related=((K19, [K]), (MH, [K]), (MK, [K]), (QLB, [K]), (AMQ, [K]), (HL, [K]), (SH, [K]), (JS, [K])))
report(20, S, GLOSS_ADD, (NOTE,))
