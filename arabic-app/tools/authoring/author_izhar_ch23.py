# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 23: the pronoun hidden BY CHOICE — in the single absent masculine and feminine of the verb
# (زَيْدٌ ضَرَبَ أَوْ يَضْرِبُ أَوْ لِيَضْرِبْ أَوْ لَا يَضْرِبْ، هِنْدٌ ضَرَبَتْ …), for one also says ضَرَبَ زَيْدٌ and so the rest, and then
# no pronoun hides in it; and in the verb's likeness, as was said, when a condition of governing other than the dual and plural named
# is found (زَيْدٌ ضَارِبٌ وَمَضْرُوبٌ وَأَسَدٌ نَاطِقٌ أَوْ هَاشِمِيٌّ أَوْ حَسَنٌ أَوْ فِي الدَّارِ) — for one says زَيْدٌ ضَارِبٌ غُلَامُهُ and so the
# rest, and then nothing hides. Print pp. 123–124.
# The transcription reads «زيد ضاربا ومضروبا» at s3; the khabar of زَيْدٌ is in rafʿ, so ضَارِبٌ وَمَضْرُوبٌ is printed — FLAGGED for review.
#   python3 author_izhar_ch23.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-mustatir-jawazan"
K22 = "al-fail-al-mudmar-al-mustatir-wujuban"
TITLE = {"ar": "الضَّمِيرُ الْمُسْتَتِرُ جَوَازًا", "en": "The pronoun hidden by choice", "tr": "Cevâzen müstetir zamir"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; F8 = "form-viii-verbs"; LN = "la-nafiya"; MR = "mudari-marfu"; MST = "istithna"; MNF = "mana-al-fil"; NSB = "ism-mansub"; SM = "sifa-mushabbaha"; JMS = "jam-mudhakkar-salim"; IDH = "idha-shartiyya"; AQ = "al-amil-wa-aqsamuh"
LA = "lam-amr"; LNH = "la-nahiya"; JZ = "nawasib-wa-jawazim-al-mudari"; AMR = "imperative-amr"; MDI = "al-madi"; JS = "jumla-sifa"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def yuqal(): return tok("وَيُقَالُ", "qala", "verb", [K, AT, NF, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ فَاعِلِهِ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«and one says» — the quoted clause its deputy.", "«ve denir» — nâibi nakledilen cümle.", punct=":", segments=wa("يُقَالُ", "qala", "verb"))
def kadha(): return tok("وَكَذَا", "kadha", "part", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ — خَبَرٌ مُقَدَّمٌ.", "«and so» — the fronted khabar.", "«ve böyledir» — öne alınmış haber.", segments=wa("كَذَا", "kadha", "part"))
def bawaqi(punct="،"): return tok("الْبَوَاقِي", "bawaqi", "noun", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — بَاقِي الصِّيَغِ.", "«the rest» — the remaining forms.", "«geri kalanlar» — diğer sîgalar.", punct=punct)
def fala(): return tok("فَلَا", "la-nafiya", "part", [K, AT, LN], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so … not»", "«o halde … -mez»", segments=fa("لَا", "la-nafiya", "part"))
def yastatir(punct=None): return tok("يَسْتَتِرُ", "istatara", "verb", [K, FL, F8, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«hides»", "«gizlenir»", punct=punct)

# ----------- s1 — the second: the single absent masculine and feminine
S.append({"id": "s1", "translation": {"en": "And the second is in the single absent masculine and the single absent feminine — as in «Zayd struck, or strikes, or let him strike, or let him not strike», and «Hind struck, or strikes, or let her strike, or let her not strike»;", "tr": "İkincisi müfred gâib ve müfred gâibededir: «Zeyd vurdu, ya vurur, ya vursun, ya vurmasın» ve «Hind vurdu, ya vurur, ya vursun, ya vurmasın» gibi;"},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — جَائِزُ الِاسْتِتَارِ.", "«and the second» — the one hidden by choice.", "«ikincisi» — cevâzen müstetir.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the khabar.", "«-de» — haber."),
  tok("الْغَائِبِ", "ghaib", "noun", [K, HJ, IFA], "مَجْرُورٌ بِفِي — الْمُفْرَدُ الْمُذَكَّرُ الْغَائِبُ.", "«the absent» — the third person.", "«gâib» — üçüncü şahıs."),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«single»", "«müfred»"),
  tok("وَالْغَائِبَةِ", "ghaiba", "noun", [K, AT, IFA], "الْوَاوُ عَاطِفَةٌ، وَالْغَائِبَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the absent feminine»", "«ve gâibe»", segments=wa("الْغَائِبَةِ", "ghaiba", "noun")),
  tok("الْمُفْرَدَةِ", "mufrad", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«single»", "«müfrede»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("ضَرَبَ", "daraba", "verb", [K, MK, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«struck» — the doer hidden by choice: he.", "«vurdu» — cevâzen gizli fâil: o."),
  aw(),
  tok("يَضْرِبُ", "daraba", "verb", [K, AT, FL, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هُوَ.", "«strikes»", "«vurur»"),
  aw(),
  tok("لِيَضْرِبْ", "daraba", "verb", [K, AT, FL, LA, JZ], "اللَّامُ لَامُ الْأَمْرِ، وَيَضْرِبْ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِهَا، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هُوَ.", "«let him strike» — the lām of command.", "«vursun» — emir lâmı.", segments=[seg("لِ", "lam-amr", "part"), seg("يَضْرِبْ", "daraba", "verb")]),
  aw(),
  tok("لَا", "la-nahiya", "part", [K, LNH, JZ], "لَا النَّاهِيَةُ — حَرْفُ نَهْيٍ وَجَزْمٍ.", "«let … not» — the prohibitive lā.", "«-masın» — nehiy lâsı."),
  tok("يَضْرِبْ", "daraba", "verb", [K, FL, LNH, JZ], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هُوَ.", "«strike»", "«vursun»", punct="،"),
  tok("وَهِنْدٌ", "hind", "propn", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهِنْدٌ مُبْتَدَأٌ مَرْفُوعٌ — مُنْصَرِفٌ عَلَى الْأَشْهَرِ.", "«and Hind» — the mubtada.", "«ve Hind» — mübtedâ.", segments=wa("هِنْدٌ", "hind", "propn")),
  tok("ضَرَبَتْ", "daraba", "verb", [K, MK, FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هِيَ.", "«struck» — the doer hidden by choice: she.", "«vurdu» — cevâzen gizli fâil: o (dişi)."),
  aw(),
  tok("تَضْرِبُ", "daraba", "verb", [K, AT, FL, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هِيَ.", "«strikes»", "«vurur»"),
  aw(),
  tok("لِتَضْرِبْ", "daraba", "verb", [K, AT, FL, LA, JZ], "اللَّامُ لَامُ الْأَمْرِ، وَتَضْرِبْ مَجْزُومٌ بِهَا، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هِيَ.", "«let her strike»", "«vursun»", segments=[seg("لِ", "lam-amr", "part"), seg("تَضْرِبْ", "daraba", "verb")]),
  aw(),
  tok("لَا", "la-nahiya", "part", [K, LNH, JZ], "لَا النَّاهِيَةُ.", "«let … not»", "«-masın»"),
  tok("تَضْرِبْ", "daraba", "verb", [K, FL, LNH, JZ], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا، وَالْفَاعِلُ مُسْتَتِرٌ جَوَازًا: هِيَ.", "«strike»", "«vursun»", punct="؛"),
 ]})
# ----------- s2 — for one says ضَرَبَ زَيْدٌ, and so the rest
S.append({"id": "s2", "translation": {"en": "and one says «Zayd struck» (with the noun after the verb), and so the rest — and then no pronoun hides in it.", "tr": "«darabe Zeydün» denir (isim fiilden sonra), diğerleri de böyle — o zaman onda zamir gizlenmez."},
 "tokens": [
  yuqal(),
  tok("ضَرَبَ", "daraba", "verb", [K, FL, NF], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ.", "«struck»", "«vurdu»"),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ — اسْمٌ ظَاهِرٌ أُسْنِدَ إِلَيْهِ الْعَامِلُ.", "«Zayd» — the apparent noun the governor is predicated of.", "«Zeyd» — âmilin isnâd edildiği açık isim.", punct="،"),
  kadha(),
  bawaqi(),
  fala(),
  yastatir(),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي الْعَامِلِ.", "«in it» — in the governor.", "«onda» — âmilde.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("ضَمِيرٌ", "damir", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«a pronoun» — the doer.", "«bir zamir» — fâil.", punct="."),
 ]})
# ----------- s3 — the verb's likeness when a condition of governing is found
S.append({"id": "s3", "translation": {"en": "And in the verb's likeness, as was said, when a condition of governing other than the dual and plural named is found — as in «Zayd is striking and struck», and «a lion is speaking», or «a Hāshimī», or «handsome», or «in the house»;", "tr": "Ve fiile benzeyende — söylendiği gibi — zikredilen tesniye ve cem' dışında bir amel şartı bulunduğunda: «Zeyd vurandır ve vurulandır», «bir aslan konuşandır», ya «Hâşimîdir», ya «güzeldir», ya «evdedir» gibi;"},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى فِي الْغَائِبِ.", "«and in»", "«ve -de»", segments=wa("فِي", "fi", "prep")),
  tok("شِبْهِ", "shibh", "noun", [K, HJ, ID, MNF], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the likeness of»", "«benzeri»"),
  tok("الْفِعْلِ", "fil", "noun", [K, ID, MNF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْفَاعِلِ وَأَخَوَاتُهُ.", "«the verb» — the participle and its sisters.", "«fiil» — ism-i fâil ve kardeşleri."),
  tok("كَمَا", "kama", "part", [K, HJ], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as»", "«gibi»"),
  tok("ذُكِرَ", "dhakara", "verb", [K, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«was said»", "«zikredildi»", punct="،"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-dığında»"),
  tok("وُجِدَ", "wajada", "verb", [K, NF, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is found»", "«bulunur»"),
  tok("شَرْطُ", "shart", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«a condition of» — the deputy doer.", "«şartı» — nâib-i fâil."),
  tok("عَمَلٍ", "amal-governing", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الِاعْتِمَادُ عَلَى نَفْيٍ أَوِ اسْتِفْهَامٍ أَوْ مَوْصُوفٍ أَوْ ذِي حَالٍ.", "«governing» — leaning on a negation, a question, a described noun or a ḥāl's owner.", "«amel» — nefiy, istifhâm, mevsûf veya zü'l-hâle dayanma."),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ لِعَمَلٍ مَجْرُورٌ، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("التَّثْنِيَةِ", "tathniya", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dual»", "«tesniye»"),
  tok("وَالْجَمْعِ", "jam", "noun", [K, AT, JMS], "الْوَاوُ عَاطِفَةٌ، وَالْجَمْعِ مَعْطُوفٌ مَجْرُورٌ.", "«and the plural»", "«ve cem'»", segments=wa("الْجَمْعِ", "jam", "noun")),
  tok("الْمَذْكُورَيْنِ", "madhkur", "noun", [K, NA, MTH, IMF], "نَعْتٌ لِلتَّثْنِيَةِ وَالْجَمْعِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«named» — a naʿt in the dual.", "«zikredilen» — tesniye na't.", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("ضَارِبٌ", "darib", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ اعْتَمَدَ عَلَى الْمُبْتَدَإِ، وَفَاعِلُهُ مُسْتَتِرٌ جَوَازًا: هُوَ.", "«striking» — the khabar, its doer hidden by choice.", "«vuran» — haber, fâili cevâzen gizli."),
  tok("وَمَضْرُوبٌ", "madrub", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَضْرُوبٌ مَعْطُوفٌ مَرْفُوعٌ — وَنَائِبُ فَاعِلِهِ مُسْتَتِرٌ جَوَازًا.", "«and struck»", "«ve vurulan»", segments=wa("مَضْرُوبٌ", "madrub", "noun")),
  tok("وَأَسَدٌ", "asad", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَأَسَدٌ مُبْتَدَأٌ مَرْفُوعٌ — جُمْلَةٌ مَعْطُوفَةٌ.", "«and a lion» — a second clause.", "«ve bir aslan» — ikinci cümle.", segments=wa("أَسَدٌ", "asad", "noun")),
  tok("نَاطِقٌ", "natiq", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ — وَفَاعِلُهُ مُسْتَتِرٌ جَوَازًا: هُوَ.", "«speaking» — the khabar.", "«konuşan» — haber."),
  aw(),
  tok("هَاشِمِيٌّ", "hashimi", "noun", [K, AT, NSB], "مَعْطُوفٌ عَلَى نَاطِقٌ مَرْفُوعٌ.", "«a Hāshimī»", "«Hâşimî»"),
  aw(),
  tok("حَسَنٌ", "hasan-adj", "noun", [K, AT, SM], "مَعْطُوفٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ.", "«handsome»", "«güzel»"),
  aw(),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الدَّارِ", "dar", "noun", [K, HJ, MK, MF], "مَجْرُورٌ بِفِي — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مَعْطُوفٌ، وَفِيهِ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا.", "«the house» — the ẓarf as khabar, its pronoun hidden by choice.", "«ev» — haber olan zarf, zamiri cevâzen gizli.", punct="؛"),
 ]})
# ----------- s4 — for one says زَيْدٌ ضَارِبٌ غُلَامُهُ, and so the rest
S.append({"id": "s4", "translation": {"en": "and one says «Zayd — his servant is striking», and so the rest; and then nothing hides.", "tr": "«Zeyd — kölesi vurandır» denir, diğerleri de böyle; o zaman hiçbir şey gizlenmez."},
 "tokens": [
  yuqal(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, NF], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("ضَارِبٌ", "darib", "noun", [K, MK, IFA, FL], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ رَفَعَ الظَّاهِرَ بَعْدَهُ.", "«striking» — the khabar raising the apparent noun after it.", "«vuran» — ardındaki açık ismi ref' eden haber."),
  tok("غُلَامُهُ", "ghulam", "noun", [K, FL, ID], "فَاعِلُ اسْمِ الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَهُوَ الرَّابِطُ.", "«his servant» — the participle's doer, and the tie to the mubtada.", "«kölesi» — ism-i fâilin fâili ve mübtedâya bağ.", punct="،", segments=[seg("غُلَامُ", "ghulam", "noun"), pr3ms()]),
  kadha(),
  bawaqi(),
  fala(),
  yastatir(punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "ghaiba": G("ghaiba", "غَائِبَة", "غ ي ب", "noun", "the absent feminine — the third person singular feminine (ism fāʿil of غَابَ)", "gâibe — üçüncü tekil şahıs dişi (gâbe'nin ism-i fâili)", 4),
 "hind": G("hind", "هِنْد", "ه ن د", "propn", "Hind — the grammarians' stock woman's name", "Hind — nahivcilerin örnek kadın adı", 2),
 "bawaqi": G("bawaqi", "بَوَاقٍ", "ب ق ي", "noun", "the remaining ones (plural of بَاقٍ) — الْبَوَاقِي: the rest of the forms", "bevâkî — geri kalanlar (bâkin'in çoğulu): diğer sîgalar", 4),
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
print("izhar ch23 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("daraba", "qala", "istatara", "dhakara", "wajada") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الضَّمِيرُ الْمُسْتَتِرُ جَوَازًا وَمَوَاضِعُهُ", "en": "The pronoun hidden by choice and its places", "tr": "Cevâzen müstetir zamir ve yerleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الفاعل: المستتر جوازا", "الكافية لابن الحاجب — المضمر", "شرح قطر الندى لابن هشام — الضمير المستتر جوازا"],
 "amil": "the pronoun hidden by choice lives in the single absent masculine and feminine of the verb (زَيْدٌ ضَرَبَ، هِنْدٌ ضَرَبَتْ) — since one also says ضَرَبَ زَيْدٌ, where nothing hides — and in the verb's likeness when a condition of governing other than the dual and plural is found (زَيْدٌ ضَارِبٌ، أَسَدٌ نَاطِقٌ، فِي الدَّارِ) — since one also says زَيْدٌ ضَارِبٌ غُلَامُهُ, where nothing hides",
 "question": {
  "en": ["Where is the pronoun hidden by choice in the verb? In the single absent masculine and feminine: زَيْدٌ ضَرَبَ أَوْ يَضْرِبُ أَوْ لِيَضْرِبْ أَوْ لَا يَضْرِبْ، هِنْدٌ ضَرَبَتْ أَوْ تَضْرِبُ أَوْ لِتَضْرِبْ أَوْ لَا تَضْرِبْ.",
         "Why «by choice»? Because one also says ضَرَبَ زَيْدٌ, the verb predicated of the apparent noun — and then no pronoun hides in it; the same for the rest of the forms.",
         "And in the verb's likeness? When a condition of governing other than the dual and the sound plural is found — leaning on a negation, a question, a described noun or a ḥāl's owner: زَيْدٌ ضَارِبٌ وَمَضْرُوبٌ، أَسَدٌ نَاطِقٌ أَوْ هَاشِمِيٌّ أَوْ حَسَنٌ أَوْ فِي الدَّارِ.",
         "Why «by choice» there? Because one also says زَيْدٌ ضَارِبٌ غُلَامُهُ, the participle raising the apparent noun — and then nothing hides.",
         "What of the dual and the sound plural of the participles? Their pronoun is hidden by necessity whatever the condition (the previous chapter): رَجُلَانِ ضَارِبَانِ.",
         "What does the engine READ here? The DabtEngine reads the verb after a mubtadaʾ as its khabar with the doer concealed, raises the noun after the verb as its doer, and raises غُلَامُهُ after the participle as the participle's own doer."],
  "tr": ["Fiilde cevâzen müstetir zamir nerede? Müfred gâib ve gâibede: Zeydün darabe ev yadribu ev li-yadrib ev lâ yadrib; Hindün darabet ev tadribu ev li-tadrib ev lâ tadrib.",
         "Niçin «cevâzen»? Çünkü darabe Zeydün de denir — fiil açık isme isnâd edilir ve o zaman onda zamir gizlenmez; diğer sîgalar da böyle.",
         "Fiile benzeyende? Tesniye ve sâlim cem' dışında bir amel şartı bulununca — nefiy, istifhâm, mevsûf veya zü'l-hâle dayanınca: Zeydün dâribün ve madrûbün, esedün nâtıkun ev Hâşimiyyün ev hasenün ev fi'd-dâr.",
         "Orada niçin «cevâzen»? Çünkü Zeydün dâribün gulâmuhû da denir — ism-i fâil açık ismi ref' eder ve o zaman hiçbir şey gizlenmez.",
         "İsm-i fâillerin tesniye ve sâlim cem'i? Zamirleri şart ne olursa olsun vücûben gizlidir (önceki bab): racülâni dâribâni.",
         "Motor burada neyi OKUR? DabtEngine mübtedâdan sonraki fiili fâili gizli haber olarak okur, fiilden sonraki ismi fâil olarak ref' eder ve ism-i fâilden sonraki gulâmuhû'yu ism-i fâilin kendi fâili olarak ref' eder."],
 },
 "plain": {"en": "Sometimes the hidden subject is a choice: «Zayd struck» can be said with the name first and the pronoun hidden in the verb, or with the verb first and the name as its open subject. Adjectives like «striking» work the same way: they hide a pronoun unless a noun follows as their subject («Zayd, his servant is striking»).",
           "tr": "Bazen gizli özne bir tercihtir: «Zeyd vurdu» önce ad, sonra içinde zamir gizli fiil ile; ya da önce fiil, sonra açık özne olan ad ile söylenebilir. «Vuran» gibi sıfatlar için de böyledir: ardından özne olacak bir isim gelmedikçe zamir gizlerler — «Zeyd, kölesi vurandır» gibi."},
 "explanation": {"en": "The pronoun hidden by choice is in the single absent masculine and the single absent feminine of the verb — زَيْدٌ ضَرَبَ أَوْ يَضْرِبُ أَوْ لِيَضْرِبْ أَوْ لَا يَضْرِبْ، هِنْدٌ ضَرَبَتْ أَوْ تَضْرِبُ أَوْ لِتَضْرِبْ أَوْ لَا تَضْرِبْ — for one also says ضَرَبَ زَيْدٌ and so with the rest, and then no pronoun hides in the verb. And it is in the verb's likeness, as was said, when a condition of governing other than the dual and the plural named is found — زَيْدٌ ضَارِبٌ وَمَضْرُوبٌ، وَأَسَدٌ نَاطِقٌ أَوْ هَاشِمِيٌّ أَوْ حَسَنٌ أَوْ فِي الدَّارِ — for one also says زَيْدٌ ضَارِبٌ غُلَامُهُ and so with the rest, and then nothing hides.",
                 "tr": "Cevâzen müstetir zamir fiilin müfred gâib ve müfred gâibesindedir — Zeydün darabe ev yadribu ev li-yadrib ev lâ yadrib; Hindün darabet ev tadribu ev li-tadrib ev lâ tadrib — çünkü darabe Zeydün de denir, diğerleri de böyle; o zaman fiilde zamir gizlenmez. Ve söylendiği gibi fiile benzeyende, zikredilen tesniye ve cem' dışında bir amel şartı bulununca — Zeydün dâribün ve madrûbün, esedün nâtıkun ev Hâşimiyyün ev hasenün ev fi'd-dâr — çünkü Zeydün dâribün gulâmuhû da denir, diğerleri de böyle; o zaman hiçbir şey gizlenmez."},
 "examples": [
  {"ar": "زَيْدٌ ضَرَبَ أَوْ يَضْرِبُ أَوْ لِيَضْرِبْ أَوْ لَا يَضْرِبْ", "en": "the absent masculine: the pronoun hidden by choice", "tr": "gâib: cevâzen gizli zamir", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "هِنْدٌ ضَرَبَتْ أَوْ تَضْرِبُ أَوْ لِتَضْرِبْ أَوْ لَا تَضْرِبْ", "en": "the absent feminine", "tr": "gâibe", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَيُقَالُ: ضَرَبَ زَيْدٌ، فَلَا يَسْتَتِرُ فِيهِ ضَمِيرٌ", "en": "the apparent doer leaves nothing hidden", "tr": "açık fâil ile hiçbir şey gizlenmez", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "زَيْدٌ ضَارِبٌ وَمَضْرُوبٌ، وَأَسَدٌ نَاطِقٌ", "en": "the verb's likeness with a condition of governing", "tr": "amel şartlı fiil benzeri", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "زَيْدٌ ضَارِبٌ غُلَامُهُ", "en": "the participle raising an apparent doer", "tr": "açık fâil ref' eden ism-i fâil", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٌ ضَرَبَ هُوَ (هُوَ as the hidden doer shown)", "right": "زَيْدٌ ضَرَبَ — the doer hidden by choice, or ضَرَبَ زَيْدٌ", "why": {"en": "a detached هُوَ after the verb is a tawkīd of the hidden doer, not the doer", "tr": "fiilden sonraki munfasıl hüve gizli fâilin te'kîdidir, fâil değil"}},
  {"wrong": "هِنْدٌ ضَرَبَ", "right": "هِنْدٌ ضَرَبَتْ", "why": {"en": "the verb predicated of a feminine pronoun takes the tāʾ", "tr": "dişi zamire isnâd edilen fiil tâ alır"}},
  {"wrong": "زَيْدٌ ضَارِبٌ غُلَامَهُ (as the doer)", "right": "زَيْدٌ ضَارِبٌ غُلَامُهُ", "why": {"en": "the participle leaning on the mubtadaʾ raises the apparent noun as its doer", "tr": "mübtedâya dayanan ism-i fâil açık ismi fâil olarak ref' eder"}},
 ],
}
ADD_EN = (" Chapter 23 (print pp. 123-124): the pronoun hidden by choice in the single absent masculine and feminine (s1), since ضَرَبَ زَيْدٌ is also said and then nothing hides (s2); in the verb's likeness when a condition of governing other than the dual and plural is found (s3), since زَيْدٌ ضَارِبٌ غُلَامُهُ is also said (s4).")
ADD_TR = (" Yirmi üçüncü bab (baskı s. 123-124): müfred gâib ve gâibede cevâzen müstetir zamir (s1), darabe Zeydün de denir ve o zaman hiçbir şey gizlenmez (s2); tesniye ve cem' dışında amel şartı bulunan fiil benzerinde (s3), Zeydün dâribün gulâmuhû da denir (s4).")
write_out(23, S, TITLE, ADD_EN, ADD_TR, "pp. 123-124", GLOSS_ADD, notes=(NOTE,),
          related=((K22, [K]), (FL, [K]), (IFA, [K]), (LA, [K]), (LNH, [K]), (MK, [K])))
report(23, S, GLOSS_ADD, (NOTE,))
