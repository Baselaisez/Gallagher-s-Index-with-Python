# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 13: the fifth and sixth QIYĀSĪ governors — the ISM TAFḌĪL, which puts no object in naṣb by
# agreement and raises an overt doer only when it comes to mean the verb (a description of what the quality hangs on, preferred in
# respect of that attachment over itself in respect of another, negated: مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ
# زَيْدٍ) and governs elsewhere; and the MAṢDAR — its condition: no diminutive, no description, no ḥāl attached, no article (for most),
# not a number, a kind or an emphasis, with the verb or without it, the verb intended and not necessarily omitted; where the verb must
# be omitted, by hearing and by rule, the maṣdar works in the verb's place (سَقْيًا); its doer may be dropped with no deputy — not so
# elsewhere; nothing is concealed in it; its governed word never precedes it. Print pp. 109–110.
#   python3 author_izhar_ch13.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "amal-ism-al-tafdil-wal-masdar"
K12 = "shurut-amal-ism-al-fail"
TITLE = {"ar": "اسْمُ التَّفْضِيلِ وَالْمَصْدَرُ وَشُرُوطُ عَمَلِهِمَا", "en": "The ism tafḍīl and the maṣdar, and the conditions of their governing", "tr": "İsm-i tafdîl ve mastar, amellerinin şartları"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; IMF = "ism-maful"; IFA = "ism-fail"
MM = "maful-mutlaq"; HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; NQ = "naqis-verbs"; MSD = "masdar"; LN = "la-nafiya"; SH = "in-shartiyya"; TF = "ism-tafdil"; IM = "imal-al-masdar"; MQ = "ism-maqsur-manqus"; TM = "tamyiz"; MNS = "mamnu-min-sarf"; IDH = "idha-shartiyya"; MST = "istithna"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«… gibi» — hazfedilmiş mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def wala(role="الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", en="«and … not»", tr="«ve … -maz»"): return tok("وَلَا", "la-nafiya", "part", [K, AT, LN], role, en, tr, segments=wa("لَا", "la-nafiya", "part"))
def wala_z(): return tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor»", "«ne de»", segments=wa("لَا", "la-nafiya", "part"))
def amal(form, role_ar, en, tr, punct=None, segments=None, tags=()): return tok(form, "amal-governing", "noun", [K] + list(tags), role_ar, en, tr, punct=punct, segments=segments)

# ----------- s1 — the fifth: the ism tafḍīl takes no object
S.append({"id": "s1", "translation": {"en": "And the fifth is the ISM TAFḌĪL; it does not put the object in naṣb, by agreement.", "tr": "Beşincisi İSM-İ TAFDÎL'dir; ittifakla mef'ûlün bihi nasb etmez."},
 "tokens": [
  tok("وَالْخَامِسُ", "khamis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَامِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fifth» — the mubtada.", "«beşincisi» — mübtedâ.", segments=wa("الْخَامِسُ", "khamis", "noun")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, TF], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the khabar, annexed.", "«ismi» — haber, muzâf."),
  tok("التَّفْضِيلِ", "tafdil", "noun", [K, ID, TF, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ التَّفْضِيلِ: الْعَامِلُ الْخَامِسُ.", "«preference» — the ism tafḍīl, the fifth governor.", "«tafdîl» — ism-i tafdîl, beşinci âmil.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«-mez»"),
  tok("يَنْصِبُ", "nasaba-nahw", "verb", [K, MK, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«puts in naṣb» — the khabar clause.", "«nasb eder» — haber cümlesi."),
  tok("الْمَفْعُولَ", "maful-object", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the object»", "«mef'ûlü»"),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«(by) it»", "«bih»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("بِالِاتِّفَاقِ", "ittifaq", "noun", [K, HJ, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَالِاتِّفَاقِ مَجْرُورٌ — بِاتِّفَاقِ النُّحَاةِ.", "«by agreement» — of the grammarians.", "«ittifakla» — nahivcilerin ittifakıyla.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الِاتِّفَاقِ", "ittifaq", "noun")]),
 ]})
# ----------- s2 — it raises an overt doer only when it means the verb
S.append({"id": "s2", "translation": {"en": "And it does not raise an overt doer — except when it comes to mean the verb: by being a description of what the quality hangs on, preferred in respect of that attachment over itself in respect of another, and negated.", "tr": "Zâhir fâili de ref etmez — fiil mânâsına geldiği zaman hariç: nitelediği şeyin müteallakının vasfı olup, bu taalluk itibariyle, başka bir şey itibariyle kendisine tafdîl edilmiş ve menfî olarak."},
 "tokens": [
  wala(),
  tok("يَرْفَعُ", "rafaa", "verb", [K, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«raises»", "«ref eder»"),
  tok("الْفَاعِلَ", "fail-doer", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the doer»", "«fâili»"),
  tok("الظَّاهِرَ", "zahir", "noun", [K, NA, IFA], "نَعْتٌ مَنْصُوبٌ — الِاسْمُ الظَّاهِرُ لَا الضَّمِيرُ.", "«overt» — the overt noun, not the pronoun.", "«zâhir» — zâhir isim, zamir değil."),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-diği zaman»"),
  tok("صَارَ", "sara", "verb", [K, KN, HV, IDH], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it comes to be» — its ism concealed.", "«olduğu» — ismi gizli."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, KN, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ صَارَ.", "«in the sense of» — the khabar of ṣāra.", "«mânâsında» — sâra'nın haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»", punct="،"),
  tok("بِأَنْ", "an-masdariyya", "part", [K, HJ, AM], "الْبَاءُ حَرْفُ جَرٍّ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْبَاءِ: بَيَانٌ لِمَعْنَى الْفِعْلِ.", "«by (its) being» — the an-clause under the bā: how it means the verb.", "«… olmasıyla» — bâ'lı en cümlesi: fiil mânâsının açıklaması.", segments=[seg("بِ", "bi", "prep"), seg("أَنْ", "an-masdariyya", "part")]),
  tok("يَكُونَ", "kana", "verb", [K, KN, AM], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it be» — naṣb by an.", "«olmak» — en ile mansûb."),
  tok("وَصْفًا", "wasf", "noun", [K, KN, MSD], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«a description» — the khabar.", "«vasıf» — haber."),
  tok("لِمُتَعَلِّقِ", "mutaalliq", "noun", [K, HJ, ID, IFA], "اللَّامُ حَرْفُ جَرٍّ، وَمُتَعَلِّقِ مَجْرُورٌ، مُضَافٌ — مَا تَعَلَّقَ بِالْمَوْصُوفِ.", "«of what is connected to» — annexed.", "«müteallikinin» — muzâf.", segments=[seg("لِ", "li", "prep"), seg("مُتَعَلِّقِ", "mutaalliq", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [K, MW, ID], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«what»", "«… olan»"),
  tok("يَجْرِي", "jara", "verb", [K, MW, NQ], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«it runs» — the ṣila: the quality runs on it.", "«cereyan eder» — sıla."),
  tok("عَلَيْهِ", "alayhi", "part", [K, HJ, MW], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«on it» — the returning pronoun.", "«onun üzerine» — âid.", punct="،", segments=[seg("عَلَى", "ala", "prep"), pr3msi()]),
  tok("مُفَضَّلًا", "mufaddal", "noun", [K, HL, IMF, TF], "حَالٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ فَضَّلَ.", "«preferred» — a ḥāl: the ism mafʿūl of faḍḍala.", "«tafdîl edilmiş» — hâl: faddale'nin ism-i mef'ûlü."),
  tok("بِاعْتِبَارِ", "itibar", "noun", [K, HJ, ID, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَاعْتِبَارِ مَجْرُورٌ، مُضَافٌ.", "«in respect of»", "«itibariyle»", segments=[seg("بِ", "bi", "prep"), seg("اعْتِبَارِ", "itibar", "noun")]),
  tok("التَّعَلُّقِ", "taalluq", "noun", [K, ID, MSD, F5], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the attachment»", "«taalluk»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«over»", "«üzerine»"),
  tok("نَفْسِهِ", "nafs", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«itself»", "«kendisine»", segments=[seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  tok("بِاعْتِبَارِ", "itibar", "noun", [K, HJ, ID, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَاعْتِبَارِ مَجْرُورٌ، مُضَافٌ.", "«in respect of»", "«itibariyle»", segments=[seg("بِ", "bi", "prep"), seg("اعْتِبَارِ", "itibar", "noun")]),
  tok("غَيْرِهِ", "ghayr", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another»", "«başkası»", punct="،", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("مَنْفِيًّا", "manfi", "noun", [K, HL, IMF], "حَالٌ ثَانٍ مَنْصُوبٌ — مَعَ النَّفْيِ.", "«negated» — a second ḥāl.", "«menfî olarak» — ikinci hâl.", punct="،"),
 ]})
# ----------- s3 — the example, and its governing elsewhere
S.append({"id": "s3", "translation": {"en": "As in «I have not seen a man in whose eye the kohl is more beautiful than it is in Zayd's eye»; and it governs in what is other than the overt doer.", "tr": "«Gözünde sürme, Zeyd'in gözündekinden daha güzel olan bir adam görmedim» gibi; zâhir fâil dışındakilerde amel eder."},
 "tokens": [
  nahw(),
  tok("مَا", "ma-nafiya", "part", [K, LN, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not»", "«-medim»"),
  tok("رَأَيْتُ", "raa", "verb", [K, FL, NQ], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw» — the tāʾ its doer.", "«gördüm» — tâ fâil."),
  tok("رَجُلًا", "rajul", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a man» — the object.", "«bir adam» — mef'ûl."),
  tok("أَحْسَنَ", "ahsan", "noun", [K, NA, TF, MNS], "نَعْتٌ لِرَجُلًا مَنْصُوبٌ بِالْفَتْحَةِ (مَمْنُوعٌ مِنَ الصَّرْفِ) — اسْمُ تَفْضِيلٍ بِمَعْنَى الْفِعْلِ، يَرْفَعُ الْفَاعِلَ الظَّاهِرَ.", "«more beautiful» — a naʿt: the ism tafḍīl meaning the verb, raising an overt doer.", "«daha güzel» — na't: fiil mânâsında ism-i tafdîl, zâhir fâili ref eder."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("عَيْنِهِ", "ayn-eye", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his eye»", "«gözünde»", segments=[seg("عَيْنِ", "ayn-eye", "noun"), pr3msi()]),
  tok("الْكُحْلُ", "kuhl", "noun", [K, FL, TF], "فَاعِلٌ لِأَحْسَنَ مَرْفُوعٌ — الْفَاعِلُ الظَّاهِرُ الَّذِي يَرْفَعُهُ اسْمُ التَّفْضِيلِ.", "«the kohl» — the overt doer the ism tafḍīl raises.", "«sürme» — ism-i tafdîlin ref ettiği zâhir fâil."),
  tok("مِنْهُ", "min", "prep", [K, HJ, TF], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مِنَ الْكُحْلِ.", "«than it» — than the kohl.", "«ondan» — sürmeden.", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("عَيْنِ", "ayn-eye", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the eye of»", "«gözünde»"),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»", punct="،"),
  tok("وَيَعْمَلُ", "amila", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَيَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it governs»", "«ve amel eder»", segments=wa("يَعْمَلُ", "amila", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِهَا", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — غَيْرِ هٰذِهِ الْحَالِ: فِي التَّمْيِيزِ وَالْحَالِ وَالظَّرْفِ.", "«in other than it» — the tamyīz, the ḥāl, the ẓarf.", "«bunun dışındakilerde» — temyiz, hâl, zarf.", punct=".", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
 ]})
# ----------- s4 — the sixth: the maṣdar and its conditions
S.append({"id": "s4", "translation": {"en": "And the sixth is the MAṢDAR; the condition of its governing the doer and the object is that it not be a diminutive, nor described, nor joined to a ḥāl, nor made definite by the article (according to most), nor a number, nor a kind, nor an emphasis — with the verb or without it — and the verb intended, not necessarily omitted.", "tr": "Altıncısı MASTAR'dır; fâilde ve mef'ûlde amel etmesinin şartı: tasgîr edilmiş olmaması, vasıflanmamış olması, hâle bitişik olmaması, (çoğunluğa göre) lâm ile ma'rife olmaması, aded, nev' veya te'kîd olmaması — fiille birlikte veya onsuz — ve fiilin murâd olup hazfi lâzım olmaması."},
 "tokens": [
  tok("وَالسَّادِسُ", "sadis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّادِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sixth» — the mubtada.", "«altıncısı» — mübtedâ.", segments=wa("السَّادِسُ", "sadis", "noun")),
  tok("الْمَصْدَرُ", "masdar-noun", "noun", [K, MK, MSD, IM], "خَبَرٌ مَرْفُوعٌ — الْمَصْدَرُ: الْعَامِلُ السَّادِسُ.", "«the maṣdar» — the khabar: the sixth governor.", "«mastar» — haber: altıncı âmil.", punct="،"),
  tok("وَشَرْطُ", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the condition of» — a mubtada.", "«ve şartı» — mübtedâ.", segments=wa("شَرْطُ", "shart", "noun")),
  amal("عَمَلِهِ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governing»", "«amelinin»", segments=[seg("عَمَلِ", "amal-governing", "noun"), pr3msi()], tags=[ID]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the doer»", "«fâilde»"),
  tok("وَالْمَفْعُولِ", "maful-object", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالْمَفْعُولِ مَعْطُوفٌ مَجْرُورٌ.", "«and the object»", "«ve mef'ûlde»", segments=wa("الْمَفْعُولِ", "maful-object", "noun")),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«(by) it»", "«bih»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ شَرْطُ.", "«that» — the an-clause the khabar.", "«-ması» — en cümlesi haber."),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«değil»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, AM], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it be» — naṣb by an.", "«olmak» — en ile mansûb."),
  tok("مُصَغَّرًا", "musaghghar", "noun", [K, KN, IMF], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«a diminutive» — the khabar.", "«tasgîr edilmiş» — haber."),
  wala_z(),
  tok("مَوْصُوفًا", "mawsuf", "noun", [K, AT, IMF], "مَعْطُوفٌ مَنْصُوبٌ.", "«described»", "«mevsûf»"),
  wala_z(),
  tok("مُقْتَرِنًا", "muqtarin", "noun", [K, AT, IFA], "مَعْطُوفٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنِ اقْتَرَنَ.", "«joined»", "«bitişik»"),
  tok("بِالْحَالِ", "hal", "noun", [K, HJ, HL], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَالِ مَجْرُورٌ.", "«to a ḥāl»", "«hâle»", segments=[seg("بِ", "bi", "prep"), seg("الْحَالِ", "hal", "noun")]),
  wala_z(),
  tok("مُعَرَّفًا", "muarraf", "noun", [K, AT, IMF], "مَعْطُوفٌ مَنْصُوبٌ.", "«made definite»", "«ma'rife»"),
  tok("بِاللَّامِ", "lam-letter", "noun", [K, HJ, "anwa-al-lam-al-tarif"], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّامِ مَجْرُورٌ — لَامِ التَّعْرِيفِ.", "«by the lām» — the article.", "«lâm ile» — ta'rîf lâmı.", segments=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«according to»", "«-e göre»"),
  tok("الْأَكْثَرِ", "akthar", "noun", [K, ID, TF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَكْثَرِ النُّحَاةِ.", "«most» — most grammarians.", "«çoğunluğa» — nahivcilerin çoğuna."),
  wala_z(),
  tok("عَدَدًا", "adad", "noun", [K, AT], "مَعْطُوفٌ مَنْصُوبٌ — مَصْدَرُ الْعَدَدِ: ضَرْبَتَيْنِ.", "«a number» — the maṣdar of number: two blows.", "«aded» — aded mastarı: darbeteyn."),
  wala_z(),
  tok("نَوْعًا", "naw", "noun", [K, AT], "مَعْطُوفٌ مَنْصُوبٌ — مَصْدَرُ النَّوْعِ: جِلْسَةً.", "«a kind» — the maṣdar of kind.", "«nev'» — nev' mastarı."),
  wala_z(),
  tok("تَأْكِيدًا", "takid", "noun", [K, AT, MM], "مَعْطُوفٌ مَنْصُوبٌ — الْمَفْعُولُ الْمُطْلَقُ الْمُؤَكِّدُ.", "«an emphasis» — the emphasising absolute object.", "«te'kîd» — te'kîd eden mef'ûl-i mutlak."),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("بِدُونِهِ", "duna", "noun", [K, HJ, ID, AT], "الْبَاءُ حَرْفُ جَرٍّ، وَدُونِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى مَعَ.", "«without it» — joined to «with».", "«onsuz» — mea'ya ma'tûf.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun"), pr3msi()]),
  tok("وَالْفِعْلُ", "fil", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ (أَوْ لِلْحَالِ)، وَالْفِعْلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the verb» — a mubtada.", "«ve fiil» — mübtedâ.", segments=wa("الْفِعْلُ", "fil", "noun")),
  tok("مُرَادٌ", "murad", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«intended» — the khabar.", "«murâd» — haber."),
  tok("غَيْرُ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ (أَوْ خَبَرٌ ثَانٍ) مَرْفُوعٌ، مُضَافٌ.", "«not» — a second khabar, annexed.", "«olmayan» — ikinci haber, muzâf."),
  tok("لَازِمِ", "lazim", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«necessary of»", "«lâzım»"),
  tok("الْحَذْفِ", "hadhf", "noun", [K, ID, MSD, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«omission»", "«hazfi»", punct="."),
 ]})
# ----------- s5 — where the verb must be omitted, the maṣdar stands in its place
S.append({"id": "s5", "translation": {"en": "And if it is necessarily omitted — by hearing and by rule — the maṣdar governs because it stands in the verb's place, as in «(may you be given) water!».", "tr": "Hazfi lâzım ise — semâî ve kıyâsî olarak — mastar, fiilin yerini tuttuğu için amel eder, «sakyen» (su verilsin sana!) gibi."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ شَرْطِيَّةٌ جَازِمَةٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, SH], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الْفِعْلُ).", "«it is» — the shart verb, its ism concealed.", "«ise» — şart fiili, ismi gizli."),
  tok("لَازِمَ", "lazim", "noun", [K, KN, ID, IFA], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«necessary of» — the khabar, annexed.", "«lâzım» — haber, muzâf."),
  tok("الْحَذْفِ", "hadhf", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«omission»", "«hazfi»"),
  tok("سَمَاعِيًّا", "samai", "noun", [K, HL], "حَالٌ مَنْصُوبٌ.", "«by hearing» — a ḥāl.", "«semâî olarak» — hâl."),
  tok("وَقِيَاسِيًّا", "qiyasi", "noun", [K, AT, HL], "الْوَاوُ عَاطِفَةٌ، وَقِيَاسِيًّا مَعْطُوفٌ مَنْصُوبٌ.", "«and by rule»", "«ve kıyâsî olarak»", segments=wa("قِيَاسِيًّا", "qiyasi", "noun")),
  tok("فَيَعْمَلُ", "amila", "verb", [K, SH, FL], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَيَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ.", "«then … governs» — the jawāb with its fāʾ.", "«o zaman … amel eder» — fâ'lı cevap.", segments=fa("يَعْمَلُ", "amila", "verb")),
  tok("الْمَصْدَرُ", "masdar-noun", "noun", [K, FL, MSD], "فَاعِلٌ مَرْفُوعٌ.", "«the maṣdar» — the doer.", "«mastar» — fâil."),
  tok("لِقِيَامِهِ", "qiyam", "noun", [K, HJ, ID, MSD, "maful-lah"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَقِيَامِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرٌ مُضَافٌ إِلَى فَاعِلِهِ.", "«because of its standing» — the lām of cause.", "«… yerini tuttuğu için» — ta'lîl lâmı.", segments=[seg("لِ", "li", "prep"), seg("قِيَامِ", "qiyam", "noun"), pr3msi()]),
  tok("مَقَامَ", "maqam", "noun", [K, MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ — مَفْعُولٌ فِيهِ لِقِيَامِهِ.", "«in the place of» — the ẓarf of «standing».", "«makâmında» — kıyâm'ın zarfı."),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiilin»", punct="،"),
  nahw(),
  tok("سَقْيًا", "saqy", "noun", [K, MM, HT, IM], "لَفْظٌ مَحْكِيٌّ: مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ وُجُوبًا، تَقْدِيرُهُ سَقَاكَ اللهُ — الْمَصْدَرُ الْقَائِمُ مَقَامَ فِعْلِهِ.", "«water (to you)!» — the absolute object of a verb necessarily omitted: the maṣdar in the verb's place.", "«sakyen» — vücûben hazfedilmiş fiilin mef'ûl-i mutlakı: fiilinin yerini tutan mastar.", punct="."),
 ]})
# ----------- s6 — the maṣdar's own licences and bars
S.append({"id": "s6", "translation": {"en": "And it is permitted to drop its doer with no deputy — that is not permitted in anything but the maṣdar; nothing is concealed in it; and its governed word does not precede it.", "tr": "Fâilini nâibsiz hazfetmek câizdir — bu, mastardan başkasında câiz değildir; onda zamir gizlenmez; ma'mûlü onun önüne geçmez."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("حَذْفُ", "hadhf", "noun", [K, FL, ID, MSD, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the dropping of» — the doer, annexed.", "«hazfi» — fâil, muzâf."),
  tok("فَاعِلِهِ", "fail-doer", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its doer»", "«fâilinin»", segments=[seg("فَاعِلِ", "fail-doer", "noun"), pr3msi()]),
  tok("بِلَا", "la-nafiya", "part", [K, HJ, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا اسْمٌ بِمَعْنَى غَيْرٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«without»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part")]),
  tok("نَائِبٍ", "naib", "noun", [K, ID, NF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَائِبِ فَاعِلٍ.", "«a deputy» — a deputy doer.", "«nâib» — nâib-i fâil.", punct="،"),
  wala(role="الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", en="«and … not»", tr="«ve … değildir»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is permitted»", "«câiz»"),
  tok("هٰذَا", "hadha", "pron", [K, FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«this» — the doer.", "«bu» — fâil."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«başkasında»"),
  tok("الْمَصْدَرِ", "masdar-noun", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the maṣdar»", "«mastar»", punct="،"),
  wala(),
  tok("يُضْمَرُ", "admara", "verb", [K, NF, F4], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (الْفَاعِلُ).", "«is concealed» — the maṣdar takes no hidden pronoun.", "«gizlenir» — mastarda gizli zamir olmaz."),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«in it»", "«onda»", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  wala(),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, FL, F5], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«precedes»", "«öne geçer»"),
  tok("مَعْمُولُهُ", "mamul", "noun", [K, FL, ID, IMF], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governed word» — the doer.", "«ma'mûlü» — fâil.", segments=[seg("مَعْمُولُ", "mamul", "noun"), pr3ms()]),
  tok("عَلَيْهِ", "alayhi", "part", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«(before) it»", "«onun önüne»", punct=".", segments=[seg("عَلَى", "ala", "prep"), pr3msi()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

CAND = {
 "khamis": G("khamis", "خَامِس", "خ م س", "noun", "fifth", "beşinci", 2),
 "ism": G("ism", "اِسْم", "س م و", "noun", "noun; name", "isim", 1, plural="أَسْمَاء"),
 "tafdil": G("tafdil", "تَفْضِيل", "ف ض ل", "noun", "preference; the elative (ism tafḍīl)", "tafdîl; ism-i tafdîl", 3),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (negation)", "değil, -mez (nefiy)", 1),
 "nasaba-nahw": G("nasaba-nahw", "نَصَبَ", "ن ص ب", "verb", "to put in naṣb (the grammarians' verb)", "nasb etmek (nahivcilerin fiili)", 3),
 "maful-object": G("maful-object", "مَفْعُول", "ف ع ل", "noun", "object (mafʿūl); the passive participle", "mef'ûl; ism-i mef'ûl", 2, plural="مَفَاعِيل"),
 "bi": G("bi", "بِ", None, "prep", "with, by, in", "ile, -de", 1),
 "ittifaq": G("ittifaq", "اِتِّفَاق", "و ف ق", "noun", "agreement, consensus", "ittifak", 3),
 "rafaa": G("rafaa", "رَفَعَ", "ر ف ع", "verb", "to raise; to put in rafʿ", "kaldırmak; ref etmek", 2),
 "fail-doer": G("fail-doer", "فَاعِل", "ف ع ل", "noun", "the doer (fāʿil); the active participle", "fâil; ism-i fâil", 2),
 "zahir": G("zahir", "ظَاهِر", "ظ ه ر", "noun", "overt, apparent", "zâhir, açık", 2),
 "illa": G("illa", "إِلَّا", None, "part", "except", "-den başka, hariç", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if (a ẓarf with the sense of a condition)", "-diği zaman, eğer (şart mânâlı zarf)", 1),
 "sara": G("sara", "صَارَ", "ص ي ر", "verb", "to become", "olmak, dönüşmek", 1),
 "mana": G("mana", "مَعْنًى", "ع ن ي", "noun", "meaning, sense", "mânâ", 2, plural="مَعَانٍ"),
 "fil": G("fil", "فِعْل", "ف ع ل", "noun", "verb; act", "fiil", 1, plural="أَفْعَال"),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "to, that (the masdar particle that puts the muḍāriʿ in naṣb)", "-mesi, -mek (muzâriyi nasb eden mastar harfi)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak, idi", 1),
 "wasf": G("wasf", "وَصْف", "و ص ف", "noun", "description, attribute", "vasıf, nitelik", 2),
 "mutaalliq": G("mutaalliq", "مُتَعَلِّق", "ع ل ق", "noun", "connected to, attached; what hangs on something", "müteallik; bağlı olan", 4),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "that which, what (relative)", "… olan şey (ism-i mevsûl)", 2),
 "jara": G("jara", "جَرَى", "ج ر ي", "verb", "to run, to flow; (of a quality) to run on", "akmak, cereyan etmek", 2),
 "alayhi": G("alayhi", "عَلَيْهِ", None, "part", "on him, on it", "onun üzerine", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, -e", 1),
 "mufaddal": G("mufaddal", "مُفَضَّل", "ف ض ل", "noun", "preferred (ism mafʿūl of faḍḍala)", "tafdîl edilmiş, üstün tutulan", 4),
 "itibar": G("itibar", "اعْتِبَار", "ع ب ر", "noun", "consideration, respect (in respect of)", "itibar", 3),
 "taalluq": G("taalluq", "تَعَلُّق", "ع ل ق", "noun", "attachment, connection", "taalluk, bağlılık", 3),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "self, soul", "nefis, kendi", 1, plural="أَنْفُس"),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka, gayr; değil", 1),
 "manfi": G("manfi", "مَنْفِيّ", "ن ف ي", "noun", "negated", "menfî, olumsuz", 3),
 "nahw": G("nahw", "نَحْو", "ن ح و", "noun", "like, such as; grammar", "gibi; nahiv", 2),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā)", "değil (nefiy mâ'sı)", 2),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam", 1, plural="رِجَال"),
 "ahsan": G("ahsan", "أَحْسَن", "ح س ن", "noun", "more beautiful, better (elative)", "daha güzel, daha iyi (ism-i tafdîl)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "ayn-eye": G("ayn-eye", "عَيْن", "ع ي ن", "noun", "eye", "göz", 1, plural="عُيُون"),
 "kuhl": G("kuhl", "كُحْل", "ك ح ل", "noun", "kohl (antimony eye-paint)", "sürme", 3),
 "min": G("min", "مِنْ", None, "prep", "from, of; than", "-den", 1),
 "zayd": G("zayd", "زَيْد", None, "propn", "Zayd (the grammarians' stock name)", "Zeyd (nahivcilerin örnek adı)", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to work, to act; (of a governor) to govern", "çalışmak, yapmak; (âmil) amel etmek", 1),
 "sadis": G("sadis", "سَادِس", "س د س", "noun", "sixth", "altıncı", 2),
 "masdar-noun": G("masdar-noun", "مَصْدَر", "ص د ر", "noun", "the maṣdar (verbal noun)", "mastar", 2, plural="مَصَادِر"),
 "shart": G("shart", "شَرْط", "ش ر ط", "noun", "condition", "şart", 2, plural="شُرُوط"),
 "amal-governing": G("amal-governing", "الْعَمَل", "ع م ل", "noun", "the governing (of a word in another's iʿrāb)", "amel (bir kelimenin başkasının i'râbına etkisi)", 3),
 "musaghghar": G("musaghghar", "مُصَغَّر", "ص غ ر", "noun", "diminutive (made small)", "tasgîr edilmiş, küçültülmüş", 4),
 "mawsuf": G("mawsuf", "مَوْصُوف", "و ص ف", "noun", "described; the noun an adjective qualifies", "mevsûf; sıfatın nitelediği isim", 3),
 "muqtarin": G("muqtarin", "مُقْتَرِن", "ق ر ن", "noun", "joined to, accompanied by", "bitişik, birlikte olan", 4),
 "hal": G("hal", "حَال", "ح و ل", "noun", "state, condition; the ḥāl (circumstantial accusative)", "hâl, durum; hâl (durum zarfı)", 2),
 "muarraf": G("muarraf", "مُعَرَّف", "ع ر ف", "noun", "made definite", "ma'rife kılınmış, muarref", 3),
 "lam-letter": G("lam-letter", "لَام", None, "noun", "the letter lām; the lām (the article, the lām of jarr…)", "lâm harfi; lâm (ta'rîf lâmı, cer lâmı…)", 3),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "at, with (a ẓarf)", "yanında, -de (zarf)", 1),
 "akthar": G("akthar", "أَكْثَر", "ك ث ر", "noun", "more, most", "daha çok, çoğu", 2),
 "adad": G("adad", "عَدَد", "ع د د", "noun", "number", "aded, sayı", 2),
 "naw": G("naw", "نَوْع", "ن و ع", "noun", "kind, sort", "nev', tür", 2),
 "takid": G("takid", "تَأْكِيد", "أ ك د", "noun", "emphasis, confirmation", "te'kîd", 3),
 "maa": G("maa", "مَعَ", None, "noun", "with (a ẓarf)", "ile, birlikte (zarf)", 1),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "below, without; other than (a ẓarf)", "aşağısı, -sız; dışında (zarf)", 2),
 "murad": G("murad", "مُرَاد", "ر و د", "noun", "intended, meant", "murâd, kastedilen", 3),
 "lazim": G("lazim", "لَازِم", "ل ز م", "noun", "necessary; intransitive (lāzim)", "lâzım; geçişsiz", 2),
 "hadhf": G("hadhf", "حَذْف", "ح ذ ف", "noun", "omission, dropping", "hazif", 3),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (the conditional particle)", "eğer (şart edatı)", 2),
 "samai": G("samai", "سَمَاعِيّ", "س م ع", "noun", "heard, by hearing (samāʿī)", "semâî, işitmeye dayalı", 3),
 "qiyasi": G("qiyasi", "قِيَاسِيّ", "ق ي س", "noun", "by rule, analogical (qiyāsī)", "kıyâsî, kurala dayalı", 3),
 "qiyam": G("qiyam", "قِيَام", "ق و م", "noun", "standing (masdar of qāma)", "kıyâm, ayakta durma", 2),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "maqam": G("maqam", "مَقَام", "ق و م", "noun", "place, station", "makâm, yer", 2),
 "saqy": G("saqy", "سَقْي", "س ق ي", "noun", "watering, giving to drink — سَقْيًا «water to you!» (the maṣdar in its verb's place)", "sulama, su verme — sakyen «sana su verilsin!» (fiilinin yerini tutan mastar)", 4),
 "jaaza": G("jaaza", "جَازَ", "ج و ز", "verb", "to be permitted", "câiz olmak", 2),
 "naib": G("naib", "نَائِب", "ن و ب", "noun", "deputy, substitute", "nâib, vekil", 3),
 "hadha": G("hadha", "هَذَا", None, "pron", "this", "bu", 1),
 "admara": G("admara", "أَضْمَرَ", "ض م ر", "verb", "to conceal (a pronoun); to keep in mind", "gizlemek (zamir); içinde tutmak", 3, form="IV"),
 "taqaddama": G("taqaddama", "تَقَدَّمَ", "ق د م", "verb", "to precede, to come first", "öne geçmek, önce gelmek", 2, form="V"),
 "mamul": G("mamul", "الْمَعْمُول", "ع م ل", "noun", "the governed word (maʿmūl)", "ma'mûl — amel edilen kelime", 3),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch13 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("nasaba-nahw", "rafaa", "sara", "jara", "raa", "amila", "kana", "jaaza", "admara", "taqaddama") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "عَمَلُ اسْمِ التَّفْضِيلِ وَالْمَصْدَرِ", "en": "The governing of the ism tafḍīl and of the maṣdar", "tr": "İsm-i tafdîl ve mastarın ameli"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العوامل القياسية: اسم التفضيل والمصدر", "الكافية لابن الحاجب — اسم التفضيل، المصدر", "قطر الندى لابن هشام — مسألة الكحل، إعمال المصدر"],
 "amil": "اسْمُ التَّفْضِيلِ — no object in naṣb, an overt doer only in the kohl-construction; الْمَصْدَرُ — a doer and an object like its verb, under its conditions; a maṣdar standing in its omitted verb's place governs as the verb would",
 "question": {
  "en": ["What does the ism tafḍīl NOT govern? The object — it never puts a mafʿūl bihi in naṣb, by the agreement of all.",
         "Does it raise an overt doer? Only when it comes to mean the verb — the kohl-construction (مَسْأَلَةُ الْكُحْلِ): مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ.",
         "What are the marks of that construction? The elative describes what the quality hangs on (the man, through his eye), the thing preferred is compared to ITSELF in another respect (the kohl in his eye against the kohl in Zayd's eye), and the sentence is negated.",
         "What else does the ism tafḍīl govern? Everything other than the overt doer — a tamyīz (أَحْسَنُ وَجْهًا), a ḥāl, a ẓarf, a jarr phrase.",
         "What is the sixth governor? The MAṢDAR — it works the work of its verb in the doer and the object: أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا.",
         "Under what conditions? Not a diminutive, not described, not joined to a ḥāl, not made definite by the article (for most grammarians), not a maṣdar of number (ضَرْبَتَيْنِ), of kind (جِلْسَةً) or of emphasis (ضَرْبًا) — whether the verb is present or not — and the verb intended, not necessarily omitted.",
         "What if the verb MUST be omitted? Then the maṣdar governs because it stands in the verb's place: سَقْيًا (= سَقَاكَ اللهُ), رَعْيًا, by hearing and by rule.",
         "Where is the maṣdar freer than its verb? Its doer may be dropped with no deputy (ضَرْبُ عَمْرٍو — the striker unsaid), which no other governor allows.",
         "Where is it narrower? Nothing is concealed in it (a maṣdar takes no hidden pronoun), and its governed word never stands before it.",
         "What does the engine READ here? The DabtEngine annexes the maṣdar to its doer and puts the noun after it in naṣb as its object, reads the fatḥatān maṣdar at a clause head as the absolute object of an omitted verb, and treats أَحْسَنُ … مِنْ as the elative with its tamyīz rather than a verb."],
  "tr": ["İsm-i tafdîl neye amel ETMEZ? Mef'ûle — ittifakla hiçbir zaman mef'ûlün bihi nasb etmez.",
         "Zâhir fâil ref eder mi? Yalnız fiil mânâsına geldiğinde — sürme meselesi (مَسْأَلَةُ الْكُحْلِ): mâ raeytü racülen ahsene fî aynihi'l-kuhlü minhu fî ayni Zeydin.",
         "Bu yapının alâmetleri nedir? Tafdîl, niteliğin bağlı olduğu şeyin (adamın, gözü yoluyla) vasfıdır; üstün tutulan şey başka bir itibarla KENDİSİYLE karşılaştırılır (onun gözündeki sürme, Zeyd'in gözündekiyle) ve cümle menfîdir.",
         "İsm-i tafdîl başka neye amel eder? Zâhir fâil dışındaki her şeye — temyiz (ahsenü vechen), hâl, zarf, câr-mecrûr.",
         "Altıncı âmil nedir? MASTAR — fâilde ve mef'ûlde fiilinin amelini yapar: a'cebenî darbü Zeydin Amren.",
         "Hangi şartlarla? Tasgîr edilmemiş, vasıflanmamış, hâle bitişik olmamış, (çoğunluğa göre) lâm ile ma'rife olmamış, aded (darbeteyn), nev' (cilseten) veya te'kîd (darben) mastarı olmamış olmalı — fiil zikredilsin edilmesin — ve fiil murâd olup hazfi lâzım olmamalı.",
         "Fiilin hazfi LÂZIMSA? O zaman mastar, fiilin yerini tuttuğu için amel eder: sakyen (= sakâke'llâhu), ra'yen; semâî ve kıyâsî olarak.",
         "Mastar fiilinden nerede daha serbesttir? Fâili nâibsiz hazfedilebilir (darbu Amrin — vuran söylenmeden); bunu başka hiçbir âmil kabul etmez.",
         "Nerede daha dardır? Onda zamir gizlenmez (mastar gizli zamir almaz) ve ma'mûlü asla onun önüne geçmez.",
         "Motor burada neyi OKUR? DabtEngine mastarı fâiline muzâf yapar ve ardındaki ismi mef'ûl olarak nasb eder, cümle başındaki fethateynli mastarı hazfedilmiş fiilin mef'ûl-i mutlakı okur ve ahsenü … min'i fiil değil temyizli ism-i tafdîl sayar."],
 },
 "plain": {"en": "«More beautiful» never takes an object and names its own doer only in the odd kohl sentence. A verb's noun («the striking») acts like its verb — Zayd's striking ʿAmr — unless it is a pet-form, qualified, carries «the», counts or names a kind; where its verb cannot be said, it works alone: «water to you!».",
           "tr": "«Daha güzel» asla mef'ûl almaz; kendi fâilini yalnız tuhaf sürme cümlesinde söyler. Fiilin ismi («vurma») fiili gibi iş görebilir — Zeyd'in Amr'a vurması — küçültülmemiş, nitelenmemiş, «el-» almamış, sayı ya da tür bildirmiyorsa; fiili hiç söylenemediğinde fiilin işini tek başına yapar: «sana su!»."},
 "explanation": {"en": "The fifth qiyāsī governor is the ism tafḍīl: by agreement it puts no object in naṣb, and it raises an overt doer only when it comes to mean the verb — by being a description of what the quality hangs on, preferred in respect of that attachment over itself in respect of another, and negated: مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ — and it governs in everything else. The sixth is the maṣdar; the condition of its governing the doer and the object is that it not be a diminutive, nor described, nor joined to a ḥāl, nor made definite by the article according to most, nor a number, a kind or an emphasis — with the verb or without it — and the verb intended, not necessarily omitted. Where the verb must be omitted, by hearing and by rule, the maṣdar governs because it stands in the verb's place (سَقْيًا). Its doer may be dropped with no deputy, which is permitted in nothing but the maṣdar; nothing is concealed in it; and its governed word does not precede it.",
                 "tr": "Beşinci kıyâsî âmil ism-i tafdîldir: ittifakla mef'ûlü nasb etmez; zâhir fâili yalnız fiil mânâsına geldiğinde — niteliğin bağlı olduğu şeyin vasfı olup, bu taalluk itibariyle başka bir itibarla kendisine tafdîl edilmiş ve menfî iken — ref eder: mâ raeytü racülen ahsene fî aynihi'l-kuhlü minhu fî ayni Zeydin; bunun dışındakilerde amel eder. Altıncısı mastardır; fâilde ve mef'ûlde amel etmesinin şartı tasgîr edilmemiş, vasıflanmamış, hâle bitişik olmamış, çoğunluğa göre lâm ile ma'rife olmamış, aded, nev' ve te'kîd olmamış olması — fiille veya onsuz — ve fiilin murâd olup hazfi lâzım olmamasıdır. Fiilin hazfi semâî ve kıyâsî olarak lâzımsa mastar, fiilin yerini tuttuğu için amel eder (sakyen). Fâili nâibsiz hazfedilebilir; bu mastardan başkasında câiz değildir; onda zamir gizlenmez; ma'mûlü onun önüne geçmez."},
 "examples": [
  {"ar": "وَهُوَ لَا يَنْصِبُ الْمَفْعُولَ بِهِ بِالِاتِّفَاقِ", "en": "the elative takes no object", "tr": "ism-i tafdîl mef'ûl almaz", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ", "en": "the kohl-construction: the elative raising an overt doer", "tr": "sürme meselesi: zâhir fâil ref eden ism-i tafdîl", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَشَرْطُ عَمَلِهِ فِي الْفَاعِلِ وَالْمَفْعُولِ بِهِ أَنْ لَا يَكُونَ مُصَغَّرًا وَلَا مَوْصُوفًا", "en": "the maṣdar's conditions", "tr": "mastarın şartları", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "فَيَعْمَلُ الْمَصْدَرُ لِقِيَامِهِ مَقَامَ الْفِعْلِ، نَحْوُ: سَقْيًا", "en": "the maṣdar in its omitted verb's place", "tr": "hazfedilmiş fiilinin yerini tutan mastar", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "وَيَجُوزُ حَذْفُ فَاعِلِهِ بِلَا نَائِبٍ", "en": "the maṣdar's doer dropped with no deputy", "tr": "mastarın fâili nâibsiz hazfedilir", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "وَلَا يَتَقَدَّمُ مَعْمُولُهُ عَلَيْهِ", "en": "its governed word never precedes it", "tr": "ma'mûlü önüne geçmez", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٌ أَحْسَنُ الْعِلْمَ", "right": "زَيْدٌ أَحْسَنُ عِلْمًا", "why": {"en": "the ism tafḍīl takes no object — the noun after it is a tamyīz in naṣb, not a mafʿūl", "tr": "ism-i tafdîl mef'ûl almaz — ardındaki isim mef'ûl değil mansûb temyizdir"}},
  {"wrong": "أَعْجَبَنِي الضَّرْبُ زَيْدٌ عَمْرًا", "right": "أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا", "why": {"en": "a maṣdar with the article does not govern (for most); the bare maṣdar annexes its doer and takes its object", "tr": "lâmlı mastar (çoğunluğa göre) amel etmez; yalın mastar fâiline muzâf olur ve mef'ûlünü alır"}},
  {"wrong": "عَمْرًا ضَرْبُ زَيْدٍ", "right": "ضَرْبُ زَيْدٍ عَمْرًا", "why": {"en": "the governed word of a maṣdar never stands before it", "tr": "mastarın ma'mûlü onun önüne geçmez"}},
  {"wrong": "سَقْيٌ لَكَ", "right": "سَقْيًا لَكَ", "why": {"en": "the maṣdar standing in its omitted verb's place is its absolute object in naṣb", "tr": "hazfedilmiş fiilinin yerini tutan mastar mansûb mef'ûl-i mutlaktır"}},
 ],
}
ADD_EN = (" Chapter 13 (print pp. 109-110): the ism tafḍīl — no object by agreement (s1), an overt doer only in the kohl-construction (s2, s3); the maṣdar's "
          "conditions (s4), the maṣdar in its omitted verb's place (s5), its doer dropped with no deputy, no concealment, no fronting of its governed word (s6).")
ADD_TR = (" On üçüncü bab (baskı s. 109-110): ism-i tafdîl — ittifakla mef'ûl yok (s1), zâhir fâil yalnız sürme meselesinde (s2, s3); mastarın şartları (s4), hazfedilmiş "
          "fiilinin yerini tutan mastar (s5), fâilinin nâibsiz hazfi, gizli zamir yok, ma'mûlünün öne geçmemesi (s6).")
write_out(13, S, TITLE, ADD_EN, ADD_TR, "pp. 109-110", GLOSS_ADD, notes=(NOTE,),
          related=((TF, [K]), (IM, [K]), (MSD, [K]), (K12, [K]), (MM, [K]), (HT, [K])))
report(13, S, GLOSS_ADD, (NOTE,))
