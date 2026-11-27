# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 39: the mustathnā continued — naṣb by exception allowed and the BADAL preferred in non-affirmative speech with
# the mustathnā minhu mentioned (مَا جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا أَوْ إِلَّا زَيْدٌ); declined by the governors when the minhu is unmentioned (مَا جَاءَنِي
# إِلَّا زَيْدٌ); in JARR after غَيْر، سِوَى، سَوَاء and mostly حَاشَا, rarely عَدَا، خَلَا; the origin of غَيْر a ṣifa, carried onto إِلَّا in exception and
# declined like its mustathnā in detail; the origin of إِلَّا exception, carried onto غَيْر as a ṣifa when exception is impossible — what follows it
# then a ṣifa, not a mustathnā (al-Anbiyāʾ 21:22 لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ لَفَسَدَتَا). Print pp. 136–137. At the page break the lithograph
# prints «فتكون تابعا | بعدها صفة لا مستثنى»; the text follows the Ottoman commentary (izhar-full-corrected l. 1385): مَا بَعْدَهَا صِفَةٌ لَا مُسْتَثْنًى.
#   python3 author_izhar_ch39.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
IS = "istithna"; ISM = "istithna-mufarragh"; BD = "badal"; TF2 = "ism-tafdil"; IDH = "idha-shartiyya"
K = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"
K38 = "al-mustathna-wa-nawah-wa-nasbuh"
TITLE = {"ar": "الْمُسْتَثْنَى: الْبَدَلُ وَالْإِعْرَابُ عَلَى حَسَبِ الْعَوَامِلِ وَالْجَرُّ بَعْدَ غَيْرٍ، وَأَصْلُ غَيْرٍ وَإِلَّا", "en": "The mustathnā: the badal, the declension by the governors, the jarr after ghayr, and the origins of ghayr and illā", "tr": "Müstesnâ: bedel, âmillere göre i'râb, gayr'dan sonra cer; gayr ve illâ'nın aslı"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def jaani(): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV, IS], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")])
def illa(gr=None): return tok("إِلَّا", "illa", "part", [K] + (gr or [IS]), "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«hariç»")
def ma_nafiya(): return tok("مَا", "ma-nafiya", "part", [K, LN, IS], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نَفْيٍ.", "«not»", "«-medi»")
def wayuarabu(): return tok("وَيُعْرَبُ", "araba", "verb", [K, AT, NF, MR, F4], "الْوَاوُ عَاطِفَةٌ، وَيُعْرَبُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْمُسْتَثْنَى.", "«and it is declined» — the mustathnā.", "«ve i'râb edilir» — müstesnâ.", segments=wa("يُعْرَبُ", "araba", "verb"))
def waaslu(what, lex, gr): return [tok("وَأَصْلُ", "asl", "noun", [K, AT, MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَصْلُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the origin of»", "«ve … aslı»", segments=wa("أَصْلُ", "asl", "noun")),
                                  tok(what, lex, "part" if lex == "illa" else "noun", [K, ID] + gr, "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«" + ("ghayr" if lex == "ghayr" else "illā") + "»", "«" + ("gayr" if lex == "ghayr" else "illâ") + "»")]
def yuhmalu(wa_=True): return tok("وَيُحْمَلُ" if wa_ else "يُحْمَلُ", "hamala", "verb", [K, AT, NF, MR], "الْوَاوُ عَاطِفَةٌ، وَيُحْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is carried»", "«ve haml olunur»", segments=wa("يُحْمَلُ", "hamala", "verb") if wa_ else None)

# ----------- s1 — naṣb allowed, badal preferred in non-affirmative speech
S.append({"id": "s1", "translation": {"en": "And naṣb by exception is allowed in it, while the badal is preferred, in non-affirmative speech with the mustathnā minhu mentioned — as in «the people did not come to me except Zayd», with naṣb or with rafʿ;", "tr": "Müsbet olmayan sözde, müstesnâ minh zikredilmişken, istisnâ üzere nasb câiz, bedel ise muhtardır — «kavim bana gelmedi, Zeyd hariç» gibi: nasb ile veya ref' ile;"},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي الْمُسْتَثْنَى.", "«in it» — in the mustathnā.", "«onda» — müstesnâda.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("النَّصْبُ", "nasb", "noun", [K, FL, MSD], "فَاعِلٌ مَرْفُوعٌ.", "«naṣb» — the doer.", "«nasb» — fâil."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«by»", "«üzere»"),
  tok("الِاسْتِثْنَاءِ", "istithna", "noun", [K, HJ, IS, MSD], "مَجْرُورٌ بِعَلَى.", "«exception»", "«istisnâ»", punct="،"),
  tok("وَيُخْتَارُ", "ikhtara", "verb", [K, AT, NF, MR, "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُخْتَارُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and is preferred»", "«ve tercih edilir»", segments=wa("يُخْتَارُ", "ikhtara", "verb")),
  tok("الْبَدَلُ", "badal", "noun", [K, NF, BD], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الْبَدَلُ مِنَ الْمُسْتَثْنَى مِنْهُ.", "«the badal» — of the mustathnā minhu.", "«bedel» — müstesnâ minhten bedel.", punct="،"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("كَلَامٍ", "kalam", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«speech»", "«sözde»"),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ مَجْرُورٌ، مُضَافٌ.", "«non-»", "«olmayan»"),
  tok("مُوجَبٍ", "mujib", "noun", [K, ID, IMF, F4], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَنْفِيِّ وَالْمَنْهِيِّ وَالْمُسْتَفْهَمِ.", "«affirmative» — the negated, the forbidden, the questioned.", "«müsbet» — menfî, nehiy ve istifhâm.", punct="،"),
  tok("وَالْمُسْتَثْنَى", "mustathna", "noun", [K, AT, MK, IS, MQ], "الْوَاوُ لِلْحَالِ، وَالْمُسْتَثْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the mustathnā»", "«ve müstesnâ»", segments=wa("الْمُسْتَثْنَى", "mustathna", "noun")),
  tok("مِنْهُ", "min", "prep", [K, HJ, IS], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«minhu»", "«minh»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مَذْكُورٌ", "madhkur", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ حَالٌ.", "«mentioned» — the khabar; the clause a ḥāl.", "«zikredilmiş» — haber; cümle hâl.", punct="،"),
  nahw(), ma_nafiya(), jaani(),
  tok("الْقَوْمُ", "qawm", "noun", [K, FL, IS], "فَاعِلٌ مَرْفُوعٌ — الْمُسْتَثْنَى مِنْهُ.", "«the people»", "«kavim»"),
  illa(),
  tok("زَيْدًا", "zayd", "propn", [K, IS], "مُسْتَثْنًى مَنْصُوبٌ — الْوَجْهُ الْجَائِزُ.", "«Zayd» — naṣb, the allowed way.", "«Zeyd» — nasb, câiz vecih."),
  aw(), illa(),
  tok("زَيْدٌ", "zayd", "propn", [K, BD, IS], "بَدَلٌ مِنَ الْقَوْمُ مَرْفُوعٌ — الْوَجْهُ الْمُخْتَارُ.", "«Zayd» — the badal, the preferred way.", "«Zeyd» — bedel, muhtar vecih.", punct="،"),
 ]})
# ----------- s2 — declined by the governors when the minhu is unmentioned
S.append({"id": "s2", "translation": {"en": "and it is declined according to the governors when the mustathnā minhu is not mentioned — as in «there came to me none but Zayd»;", "tr": "müstesnâ minh zikredilmemişse âmillere göre i'râb edilir — «bana ancak Zeyd geldi» gibi;"},
 "tokens": [
  wayuarabu(),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«according to»", "«göre»"),
  tok("حَسَبِ", "hasab", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the measure of»", "«… hesabına»"),
  tok("الْعَوَامِلِ", "amil", "noun", [K, ID, JT, ISM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governors»", "«âmillerin»"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ince»"),
  tok("كَانَ", "kana", "verb", [K, KN, HV, IDH], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is»", "«olursa»"),
  tok("الْمُسْتَثْنَى", "mustathna", "noun", [K, KN, IS, MQ], "اسْمُ كَانَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the mustathnā»", "«müstesnâ»"),
  tok("مِنْهُ", "min", "prep", [K, HJ, IS], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«minhu»", "«minh»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("غَيْرَ", "ghayr", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«not»", "«olmayan»"),
  tok("مَذْكُورٍ", "madhkur", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«mentioned»", "«zikredilmiş»", punct="،"),
  nahw(), ma_nafiya(), jaani(), illa([ISM]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL, ISM], "فَاعِلٌ مَرْفُوعٌ — الْمُسْتَثْنَى الْمُفَرَّغُ، عَلَى حَسَبِ عَامِلِهِ.", "«Zayd» — the doer: the exempt mustathnā, as its governor asks.", "«Zeyd» — fâil: müferrağ müstesnâ, âmilinin istediği gibi.", punct="،"),
 ]})
# ----------- s3 — jarr after ghayr, siwā, sawāʾ, ḥāshā; rarely ʿadā, khalā
S.append({"id": "s3", "translation": {"en": "and it is in jarr after «ghayr», «siwā», «sawāʾ» and — in most cases — «ḥāshā», and after «ʿadā» and «khalā» in the fewer;", "tr": "gayr, sivâ, sevâ ve çoğunlukla hâşâ'dan sonra, azı da adâ ve halâ'dan sonra mecrûrdur;"},
 "tokens": [
  tok("وَمَخْفُوضٌ", "makhfud", "noun", [K, AT, MK, IMF, IS], "الْوَاوُ عَاطِفَةٌ، وَمَخْفُوضٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَهُوَ مَخْفُوضٌ.", "«and in jarr» — the khabar of a dropped «it».", "«ve mecrûrdur» — hazfedilmiş mübtedânın haberi.", segments=wa("مَخْفُوضٌ", "makhfud", "noun")),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("غَيْرٍ", "ghayr", "noun", [K, ID, IS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْمُسْتَثْنَى بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«ghayr» — its mustathnā is annexed to it.", "«gayr» — müstesnâsı ona muzâf."),
  tok("وَسِوَى", "siwa", "adv", [K, AT, IS, MQ], "الْوَاوُ عَاطِفَةٌ، وَسِوَى مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«and siwā»", "«ve sivâ»", segments=wa("سِوَى", "siwa", "adv")),
  tok("وَسَوَاءٍ", "sawa", "noun", [K, AT, IS, "ism-mamdud"], "الْوَاوُ عَاطِفَةٌ، وَسَوَاءٍ مَعْطُوفٌ مَجْرُورٌ.", "«and sawāʾ»", "«ve sevâ»", segments=wa("سَوَاءٍ", "sawa", "noun")),
  tok("وَحَاشَا", "hasha", "part", [K, AT, IS], "الْوَاوُ عَاطِفَةٌ، وَحَاشَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and ḥāshā»", "«ve hâşâ»", segments=wa("حَاشَا", "hasha", "part")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَكْثَرِ", "akthar", "noun", [K, HJ, TF2], "مَجْرُورٌ بِفِي.", "«most cases»", "«çoğunlukla»", punct="،"),
  tok("وَعَدَا", "ada-except", "part", [K, AT, IS], "الْوَاوُ عَاطِفَةٌ، وَعَدَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and ʿadā»", "«ve adâ»", segments=wa("عَدَا", "ada-except", "part")),
  tok("وَخَلَا", "khala-except", "part", [K, AT, IS], "الْوَاوُ عَاطِفَةٌ، وَخَلَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and khalā»", "«ve halâ»", segments=wa("خَلَا", "khala-except", "part")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَقَلِّ", "aqall", "noun", [K, HJ, TF2, "doubled-verbs"], "مَجْرُورٌ بِفِي.", "«the fewer»", "«azı»", punct="،"),
 ]})
# ----------- s4 — the origin of ghayr
S.append({"id": "s4", "translation": {"en": "and the origin of «ghayr» is to be a ṣifa, and it is carried onto «illā» in exception, and declined like the declension of the mustathnā by «illā», in detail;", "tr": "gayr'ın aslı sıfat olmaktır; istisnâda illâ'ya haml olunur ve tafsîl üzere illâ ile müstesnânın i'râbı gibi i'râb edilir;"},
 "tokens": [
  *waaslu("غَيْرٍ", "ghayr", [IS]),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, MK], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that»", "«-mak»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ.", "«it be»", "«olması»"),
  tok("صِفَةً", "sifa", "noun", [K, KN, NA], "خَبَرُ يَكُونَ مَنْصُوبٌ — جَاءَنِي رَجُلٌ غَيْرُكَ.", "«a ṣifa» — جَاءَنِي رَجُلٌ غَيْرُكَ.", "«sıfat» — câenî racülün gayruke.", punct="،"),
  yuhmalu(),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«onto»", "«üzerine»"),
  tok("إِلَّا", "illa", "part", [K, HJ, IS], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«illā»", "«illâ»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-da»"),
  tok("الِاسْتِثْنَاءِ", "istithna", "noun", [K, HJ, IS, MSD], "مَجْرُورٌ بِفِي.", "«exception»", "«istisnâ»", punct="،"),
  wayuarabu(),
  tok("كَإِعْرَابِ", "irab", "noun", [K, HJ, ID, MSD, F4], "الْكَافُ حَرْفُ جَرٍّ، وَإِعْرَابِ مَجْرُورٌ، مُضَافٌ.", "«like the declension of»", "«… i'râbı gibi»", segments=[seg("كَ", "ka", "prep"), seg("إِعْرَابِ", "irab", "noun")]),
  tok("الْمُسْتَثْنَى", "mustathna", "noun", [K, ID, IS, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the mustathnā»", "«müstesnânın»"),
  tok("بِإِلَّا", "illa", "part", [K, HJ, IS], "الْبَاءُ حَرْفُ جَرٍّ، وَإِلَّا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«by illā»", "«illâ ile»", segments=[seg("بِ", "bi", "prep"), seg("إِلَّا", "illa", "part")]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«üzere»"),
  tok("التَّفْصِيلِ", "tafsil", "noun", [K, HJ, MSD, F2], "مَجْرُورٌ بِعَلَى — النَّصْبُ وَالْبَدَلُ وَحَسَبُ الْعَوَامِلِ تَجْرِي عَلَى غَيْرٍ نَفْسِهَا.", "«the detail» — naṣb, badal and the governors' rule fall on ghayr itself.", "«tafsîl» — nasb, bedel ve âmillere göre hüküm gayr'ın kendisine düşer.", punct="،"),
 ]})
# ----------- s5 — the origin of illā; the ṣifa reading
S.append({"id": "s5", "translation": {"en": "and the origin of «illā» is exception, and it may be carried onto «ghayr» as a ṣifa when exception is impossible, so that what follows it is a ṣifa, not a mustathnā — as in His saying, exalted be He: «had there been in them gods other than God, both would have gone to ruin».", "tr": "illâ'nın aslı istisnâdır; istisnâ mümkün olmayınca sıfat olarak gayr'a haml olunabilir, o zaman ondan sonrası müstesnâ değil sıfattır — Allah Teâlâ'nın «ikisinde Allah'tan başka ilâhlar olsaydı ikisi de bozulurdu» sözündeki gibi."},
 "tokens": [
  *waaslu("إِلَّا", "illa", [IS]),
  tok("الِاسْتِثْنَاءُ", "istithna", "noun", [K, MK, IS, MSD], "خَبَرٌ مَرْفُوعٌ.", "«exception» — the khabar.", "«istisnâ» — haber.", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  yuhmalu(False),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«onto»", "«üzerine»"),
  tok("غَيْرٍ", "ghayr", "noun", [K, HJ, IS], "لَفْظٌ مَحْكِيٌّ مَجْرُورٌ بِعَلَى.", "«ghayr»", "«gayr»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-ta»"),
  tok("الصِّفَةِ", "sifa", "noun", [K, HJ, NA], "مَجْرُورٌ بِفِي.", "«the ṣifa»", "«sıfat»"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ince»"),
  tok("تَعَذَّرَ", "taadhdhara", "verb", [K, FL, IDH, F5], "فِعْلٌ مَاضٍ، فِعْلُ الشَّرْطِ.", "«is impossible»", "«mümkün olmayınca»"),
  tok("الِاسْتِثْنَاءُ", "istithna", "noun", [K, FL, IS, MSD], "فَاعِلٌ مَرْفُوعٌ.", "«exception»", "«istisnâ»", punct="،"),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR, IDH], "الْفَاءُ لِلتَّفْرِيعِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — الطَّبْعُ: فَتَكُونُ تَابِعًا.", "«so that it is» — the lithograph: فَتَكُونُ تَابِعًا.", "«o zaman … olur» — taşbaskı: fe-tekûnu tâbian.", segments=fa("يَكُونُ", "kana", "verb")),
  tok("مَا", "ma-mawsula", "pron", [K, KN, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، اسْمُ يَكُونُ.", "«what» — the ism of yakūnu.", "«… olan» — yekûnu'nun ismi."),
  tok("بَعْدَهَا", "bada", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا: بَعْدَ إِلَّا.", "«follows it» — after illā.", "«ondan sonra» — illâ'dan sonra.", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  tok("صِفَةً", "sifa", "noun", [K, KN, NA], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«a ṣifa»", "«sıfat»"),
  tok("لَا", "la-nafiya", "part", [K, AT, LN], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not»", "«değil»"),
  tok("مُسْتَثْنًى", "mustathna", "noun", [K, AT, IS, MQ], "مَعْطُوفٌ عَلَى صِفَةً مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«a mustathnā»", "«müstesnâ»", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as in»", "«… gibi»"),
  tok("قَوْلِهِ", "qawl", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ.", "«exalted be He»", "«Teâlâ»", punct=":"),
  tok("لَوْ", "law", "part", [K, INS], "حَرْفُ شَرْطٍ لِلِامْتِنَاعِ.", "«had»", "«-saydı»"),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«been»", "«olsaydı»"),
  tok("فِيهِمَا", "fi", "prep", [K, HJ, KN], "فِي حَرْفُ جَرٍّ، وَهِمَا فِي مَحَلِّ جَرٍّ — خَبَرُ كَانَ مُقَدَّمٌ: فِي السَّمَاءِ وَالْأَرْضِ.", "«in them» — the fronted khabar: in the heaven and the earth.", "«ikisinde» — öne alınmış haber: gökte ve yerde.", segments=[seg("فِي", "fi", "prep"), seg("هِمَا", "pron-3d", "pron")]),
  tok("آلِهَةٌ", "ilah", "noun", [K, KN, JT], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ — الْمَوْصُوفُ.", "«gods» — the delayed ism, the qualified noun.", "«ilâhlar» — sona alınmış isim, mevsûf."),
  tok("إِلَّا", "illa", "part", [K, NA, IS], "بِمَعْنَى غَيْرٍ — صِفَةٌ لِآلِهَةٌ، وَإِعْرَابُهَا ظَاهِرٌ عَلَى مَا بَعْدَهَا.", "«other than» — in the sense of ghayr, a ṣifa of «gods».", "«-dan başka» — gayr mânâsında, ilâhlar'ın sıfatı."),
  tok("اللهُ", "allah", "propn", [K, NA, IS], "مَرْفُوعٌ — تَبَعًا لِآلِهَةٌ بِالصِّفَةِ لَا بِالِاسْتِثْنَاءِ.", "«God» — rafʿ, following «gods» as a ṣifa, not by exception.", "«Allah» — merfû; ilâhlar'a istisnâ ile değil sıfatla tâbi."),
  tok("لَفَسَدَتَا", "fasada", "verb", [K, INS, FL, MTH], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَفَسَدَتَا فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْأَلِفُ فَاعِلٌ.", "«both would have gone to ruin» — the answer of law.", "«ikisi de bozulurdu» — lev'in cevâbı.", punct=".", segments=[seg("لَ", "li", "prep"), seg("فَسَدَ", "fasada", "verb"), seg("تَا", "pron-3d", "pron")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "makhfud": G("makhfud", "مَخْفُوض", "خ ف ض", "noun", "in the genitive (khafḍ = jarr, the Kūfan term)", "mecrûr (hafd = cer, Kûfe terimi)", 4),
 "taadhdhara": G("taadhdhara", "تَعَذَّرَ", "ع ذ ر", "verb", "to be impossible, unfeasible (form V)", "mümkün olmamak, imkânsız olmak (V. bab)", 4, form="V"),
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
put_morph(mo, "taadhdhara", {"bab": "الْبَابُ الْخَامِسُ تَفَعَّلَ", "wazn": "تَفَعَّلَ يَتَفَعَّلُ", "masdar": "تَعَذُّر", "ismFail": "مُتَعَذِّر",
 "mazi": ["تَعَذَّرَ", "تَعَذَّرَا", "تَعَذَّرُوا", "تَعَذَّرَتْ", "تَعَذَّرَتَا", "تَعَذَّرْنَ", "تَعَذَّرْتَ", "تَعَذَّرْتُمَا", "تَعَذَّرْتُمْ", "تَعَذَّرْتِ", "تَعَذَّرْتُمَا", "تَعَذَّرْتُنَّ", "تَعَذَّرْتُ", "تَعَذَّرْنَا"],
 "mudari": ["يَتَعَذَّرُ", "يَتَعَذَّرَانِ", "يَتَعَذَّرُونَ", "تَتَعَذَّرُ", "تَتَعَذَّرَانِ", "يَتَعَذَّرْنَ", "تَتَعَذَّرُ", "تَتَعَذَّرَانِ", "تَتَعَذَّرُونَ", "تَتَعَذَّرِينَ", "تَتَعَذَّرَانِ", "تَتَعَذَّرْنَ", "أَتَعَذَّرُ", "نَتَعَذَّرُ"],
 "amr": ["تَعَذَّرْ", "تَعَذَّرَا", "تَعَذَّرُوا", "تَعَذَّرِي", "تَعَذَّرَا", "تَعَذَّرْنَ"], "mansub": "يَتَعَذَّرَ", "majzum": "يَتَعَذَّرْ", "majzum2": "تَتَعَذَّرْ",
 "note": "تَعَذَّرَ الْأَمْرُ يَتَعَذَّرُ تَعَذُّرًا: صَعُبَ وَامْتَنَعَ — مِنَ الْبَابِ الْخَامِسِ، لَازِمٌ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch39 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "jaa", "ikhtara", "araba", "hamala", "fasada") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُسْتَثْنَى: الْبَدَلُ الْمُخْتَارُ، وَالْمُفَرَّغُ، وَالْمَجْرُورُ بَعْدَ غَيْرٍ وَأَخَوَاتِهَا، وَأَصْلُ غَيْرٍ وَإِلَّا", "en": "The mustathnā: the preferred badal, the exempt one, the jarr after ghayr and its sisters, and the origins of ghayr and illā", "tr": "Müstesnâ: muhtar bedel, müferrağ, gayr ve kardeşlerinden sonra cer, gayr ve illâ'nın aslı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: المستثنى (تتمة)", "الكافية لابن الحاجب — المستثنى", "مغني اللبيب لابن هشام — إلّا وغير"],
 "amil": "in non-affirmative speech with the mustathnā minhu mentioned, naṣb by exception is allowed and the badal preferred (مَا جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا / إِلَّا زَيْدٌ); with the minhu unmentioned the mustathnā is declined by the governors — the exempt mustathnā (مَا جَاءَنِي إِلَّا زَيْدٌ); it is in jarr after غَيْر، سِوَى، سَوَاء and mostly حَاشَا, rarely after عَدَا، خَلَا; غَيْر is a ṣifa in origin, carried onto إِلَّا in exception and declined like the mustathnā by إِلَّا in detail; إِلَّا is exception in origin, carried onto غَيْر as a ṣifa when exception is impossible, what follows it then a ṣifa (لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ لَفَسَدَتَا, al-Anbiyāʾ 21:22)",
 "question": {
  "en": ["When is the badal preferred? In non-affirmative speech (negation, prohibition, question) with the mustathnā minhu mentioned: مَا جَاءَنِي الْقَوْمُ إِلَّا زَيْدٌ — naṣb by exception stays allowed: إِلَّا زَيْدًا.",
         "What is the exempt (mufarragh) mustathnā? The one whose minhu is unmentioned: مَا جَاءَنِي إِلَّا زَيْدٌ — declined as the governor asks, here the doer of جَاءَ.",
         "After which tools is the mustathnā in jarr? Always after غَيْر، سِوَى، سَوَاء (annexed to them), mostly after حَاشَا, and in the fewer cases after عَدَا and خَلَا.",
         "What is غَيْر in origin? A ṣifa (رَجُلٌ غَيْرُكَ); in exception it is carried onto إِلَّا and takes the mustathnā's own declension — naṣb, badal or the governors' rule — while its mustathnā is annexed in jarr.",
         "What is إِلَّا in origin? Exception; when exception is impossible it is carried onto غَيْر and becomes a ṣifa: لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ لَفَسَدَتَا — اللهُ follows آلِهَةٌ in rafʿ as a qualifier, not an exception.",
         "Why is exception impossible there? Because لَوْ supposes the plurality of gods; an exception would imply their existence apart from God — so إِلَّا means «other than».",
         "What does the engine READ here? The DabtEngine reads the name after إِلَّا in a negated clause whose minhu is present by the author's vowel — naṣb or the badal's rafʿ — the exempt mustathnā by its governor, the noun after غَيْر as its muḍāf ilayh, and the Qurʾānic citation as the source prints it."],
  "tr": ["Bedel ne zaman muhtardır? Müsbet olmayan sözde (nefiy, nehiy, istifhâm) müstesnâ minh zikredilmişken: mâ câenî'l-kavmü illâ Zeydün — istisnâ üzere nasb da câiz kalır: illâ Zeyden.",
         "Müferrağ müstesnâ nedir? Minhi zikredilmeyen: mâ câenî illâ Zeydün — âmilin istediği gibi i'râb edilir; burada câe'nin fâili.",
         "Hangi edatlardan sonra müstesnâ mecrûrdur? Dâimâ gayr, sivâ, sevâ'dan sonra (onlara muzâf), çoğunlukla hâşâ'dan sonra, azı adâ ve halâ'dan sonra.",
         "Gayr aslında nedir? Sıfat (racülün gayruke); istisnâda illâ'ya haml olunur ve müstesnânın i'râbını — nasb, bedel veya âmillere göre — kendisi alır; müstesnâsı ise muzâfun ileyh olarak mecrûrdur.",
         "İllâ aslında nedir? İstisnâ; istisnâ mümkün olmayınca gayr'a haml olunur ve sıfat olur: lev kâne fîhimâ âlihetün illallâhu le-fesedetâ — Allâhu, âlihetün'e istisnâ değil sıfat olarak ref' ile tâbi.",
         "Orada istisnâ neden mümkün değildir? Çünkü lev ilâhların çokluğunu farz eder; istisnâ onların Allah dışında var olduğunu îmâ ederdi — bu yüzden illâ «-dan başka» demektir.",
         "Motor burada neyi OKUR? DabtEngine minhi mevcut menfî cümlede illâ'dan sonraki ismi yazarın harekesiyle — nasb veya bedelin ref'i — okur; müferrağ müstesnâyı âmiline göre; gayr'dan sonraki ismi muzâfun ileyh; Kur'ân alıntısını kaynağın bastığı gibi okur."],
 },
 "plain": {"en": "In a negative sentence the exception may agree with the group word («the people did not come except Zayd»); that is preferred. With no group word it takes the case the verb demands. After «ghayr» it is genitive. «Ghayr» is an adjective lent to exceptions, «illā» an exception word lent as an adjective.",
           "tr": "Olumsuz cümlede istisnâ, nasb yerine topluluk sözcüğüne uyabilir («kavim gelmedi, Zeyd hariç»); tercih edilen budur. Topluluk sözcüğü yoksa fiilin istediği hâli alır. Gayr ve kardeşlerinden sonra mecrûrdur. Gayr istisnâ için ödünç alınmış bir sıfat, illâ ise sıfat olarak ödünç alınmış bir istisnâ edatıdır."},
 "explanation": {"en": "In non-affirmative speech with the mustathnā minhu mentioned, naṣb by exception is allowed in the mustathnā and the badal is preferred: مَا جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا or إِلَّا زَيْدٌ. When the minhu is not mentioned the mustathnā is declined according to the governors — the exempt mustathnā: مَا جَاءَنِي إِلَّا زَيْدٌ, Zayd being the doer. It is in jarr after غَيْر، سِوَى، سَوَاء and, in most usage, حَاشَا, and in the fewer cases after عَدَا and خَلَا. The origin of غَيْر is to be a ṣifa; in exception it is carried onto إِلَّا and is declined like the mustathnā by إِلَّا, in detail. The origin of إِلَّا is exception; when exception is impossible it may be carried onto غَيْر as a ṣifa, so that what follows it is a ṣifa, not a mustathnā: لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ لَفَسَدَتَا (al-Anbiyāʾ 21:22), where اللهُ follows آلِهَةٌ in rafʿ. The lithograph prints the clause as «فتكون تابعا | بعدها صفة لا مستثنى» across the page break; the Ottoman commentary's «what follows it is a ṣifa, not a mustathnā» is followed here.",
                 "tr": "Müsbet olmayan sözde müstesnâ minh zikredilmişken müstesnâda istisnâ üzere nasb câiz, bedel ise muhtardır: mâ câenî'l-kavmü illâ Zeyden veya illâ Zeydün. Minh zikredilmemişse müstesnâ âmillere göre i'râb edilir — müferrağ müstesnâ: mâ câenî illâ Zeydün; Zeyd fâildir. Gayr, sivâ, sevâ ve çoğunlukla hâşâ'dan sonra, azı da adâ ve halâ'dan sonra mecrûrdur. Gayr'ın aslı sıfat olmaktır; istisnâda illâ'ya haml olunur ve tafsîl üzere illâ ile müstesnâ gibi i'râb edilir. İllâ'nın aslı istisnâdır; istisnâ mümkün olmayınca sıfat olarak gayr'a haml olunabilir, o zaman ondan sonrası müstesnâ değil sıfattır: lev kâne fîhimâ âlihetün illallâhu le-fesedetâ (Enbiyâ 21:22); Allâhu, âlihetün'e ref' ile tâbidir. Taşbaskı cümleyi sayfa sonunda «fetekûnu tâbian | ba'dehâ sıfatün lâ müstesnen» diye basar; burada Osmanlıca şerhin «ondan sonrası müstesnâ değil sıfattır» okuyuşu izlenir."},
 "examples": [
  {"ar": "مَا جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا أَوْ إِلَّا زَيْدٌ", "en": "naṣb allowed, the badal preferred", "tr": "nasb câiz, bedel muhtar", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "مَا جَاءَنِي إِلَّا زَيْدٌ", "en": "the exempt mustathnā declined by its governor", "tr": "âmiline göre i'râb edilen müferrağ müstesnâ", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "وَمَخْفُوضٌ بَعْدَ غَيْرٍ وَسِوَى وَسَوَاءٍ وَحَاشَا", "en": "the jarr after ghayr and its sisters", "tr": "gayr ve kardeşlerinden sonra cer", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَأَصْلُ غَيْرٍ أَنْ يَكُونَ صِفَةً", "en": "ghayr a ṣifa in origin", "tr": "gayr aslında sıfat", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ لَفَسَدَتَا", "en": "illā as a ṣifa where exception is impossible", "tr": "istisnâ mümkün olmayınca sıfat olan illâ", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "مَا جَاءَنِي إِلَّا زَيْدًا (with no minhu)", "right": "مَا جَاءَنِي إِلَّا زَيْدٌ", "why": {"en": "the exempt mustathnā takes the case its governor demands — here the doer's rafʿ", "tr": "müferrağ müstesnâ âmilinin istediği hâli alır — burada fâilin ref'i"}},
  {"wrong": "جَاءَنِي الْقَوْمُ غَيْرَ زَيْدًا", "right": "جَاءَنِي الْقَوْمُ غَيْرَ زَيْدٍ", "why": {"en": "after ghayr the mustathnā is annexed in jarr; ghayr itself carries the exception's case", "tr": "gayr'dan sonra müstesnâ muzâfun ileyh olarak mecrûrdur; istisnânın hâlini gayr taşır"}},
  {"wrong": "لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهَ", "right": "لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ", "why": {"en": "illā here means «other than» and what follows it is a ṣifa in rafʿ, not an exception in naṣb", "tr": "illâ burada «-dan başka» demektir; ondan sonrası nasblı istisnâ değil ref'li sıfattır"}},
 ],
}
ADD_EN = (" Chapter 39 (print pp. 136-137): naṣb allowed and the badal preferred in non-affirmative speech (s1), the exempt mustathnā declined by its governor (s2), the jarr after ghayr, siwā, sawāʾ, ḥāshā and rarely ʿadā, khalā (s3), ghayr a ṣifa in origin (s4), illā exception in origin and a ṣifa where exception is impossible, al-Anbiyāʾ 21:22 (s5).")
ADD_TR = (" Otuz dokuzuncu bab (baskı s. 136-137): müsbet olmayan sözde nasb câiz, bedel muhtar (s1), âmiline göre i'râb edilen müferrağ müstesnâ (s2), gayr, sivâ, sevâ, hâşâ ve nâdiren adâ, halâ'dan sonra cer (s3), aslı sıfat olan gayr (s4), aslı istisnâ olan ve istisnâ mümkün olmayınca sıfat olan illâ, Enbiyâ 21:22 (s5).")
write_out(39, S, TITLE, ADD_EN, ADD_TR, "pp. 136-137", GLOSS_ADD, notes=(NOTE,),
          related=((K38, [K]), (IS, [K]), (ISM, [K]), (BD, [K]), (NA, [K]), ("in-shartiyya", [K])))
report(39, S, GLOSS_ADD, (NOTE,))
