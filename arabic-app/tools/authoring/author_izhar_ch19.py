# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 19: the THIRD division of the governed — what is not governed by origin but may stand where the
# second division stands: the MĀḌĪ (after أَنْ its place is naṣb, after the jāzim as protasis or apodosis its place is jazm — the iʿrāb
# shows in what is joined to it: أَعْجَبَنِي أَنْ ضَرَبْتَ وَتَقْتُلَ، وَإِنْ ضَرَبْتَ وَتَقْتُلْ ضَرَبْتُكَ وَأَقْتُلْ; elsewhere not governed) and the
# SENTENCE — verbal (verb, in word or in sense, with its doer: ضَرَبَ زَيْدٌ، إِنْ تُكْرِمْنِي أُكْرِمْكَ، هَيْهَاتَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ)
# or nominal (mubtadaʾ and khabar, or the governing particle's ism and its khabar: زَيْدٌ قَائِمٌ، إِنَّ زَيْدًا قَائِمٌ). When its wording
# is meant it takes iʿrāb like a single noun (زَيْدٌ قَائِمٌ جُمْلَةٌ اسْمِيَّةٌ); so the saying's content (﴿وَإِذَا قِيلَ لَهُمْ آمِنُوا﴾);
# so a maṣdar sense through أَنْ / أَنَّ / مَا (بَلَغَنِي أَنَّكَ قَائِمٌ، ﴿وَأَنْ تَصُومُوا خَيْرٌ لَكُمْ﴾) or without them — the clause annexed
# to (﴿يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ﴾), ﴿سَوَاءٌ عَلَيْهِمْ أَأَنْذَرْتَهُمْ أَمْ لَمْ تُنْذِرْهُمْ﴾, تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرٌ مِنْ أَنْ تَرَاهُ
# (the last confined to what was heard). Print pp. 117–119.
#   python3 author_izhar_ch19.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-madi-wal-jumla-mamulayn"
K18 = "al-mamul-wa-aqsamuh"
TITLE = {"ar": "الْقِسْمُ الثَّالِثُ: الْمَاضِي وَالْجُمْلَةُ حِينَ يُعْمَلُ فِيهِمَا", "en": "The third division: the māḍī and the sentence when they are governed", "tr": "Üçüncü kısım: mâzî ve cümle, amel edildikleri zaman"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; MSD = "masdar"; LN = "la-nafiya"; IN = "inna-wa-akhawatuha"; BD = "badal"; JT = "jam-taksir"; JMS = "jam-mudhakkar-salim"; ISH = "asma-al-ishara"; MQ = "ism-maqsur-manqus"; AQ = "al-amil-wa-aqsamuh"; MR = "mudari-marfu"; MJZ = "nawasib-wa-jawazim-al-mudari"; MAW = "ism-mawsul"; JS = "jumla-sifa"; MM = "maful-mutlaq"
AMR = "imperative-amr"; IFL = "ism-fil"; KK = "al-kalima-wal-kalam"; SH = "in-shartiyya"; MFL = "maful-lah"; MH = "mahall-al-majrur"; LAJ = "la-nafiya-lil-jins"; NSB = "ism-mansub"; AMS = "an-masdariyya"; TM = "tamyiz"; QA = "al-iqtibas-wal-tadmin"; IST = "al-istifham"; NQ = "naqis-verbs"; JI = "jumla-ismiyya" if False else "mubtada-khabar"; ITF = "ism-tafdil"; MNF = "mana-al-fil"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)
def qawlihi(pre="", lexpre=None):
    segs = ([seg(pre, lexpre, "conj" if pre == "وَ" else "prep")] if pre else []) + [seg("قَوْلِ", "qawl", "noun"), pr3msi()]
    ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "وَ" else ("الْكَافُ حَرْفُ جَرٍّ، وَ" if pre == "كَ" else "")) + "قَوْلِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ."
    return tok(pre + "قَوْلِهِ", "qawl", "noun", [K, HJ, ID, QA], ar, "«His word»", "«O'nun sözü»", segments=segs)
def taala(): return tok("تَعَالَى", "taala", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«Most High»", "«Teâlâ»", punct=":")
def ay(kasra=False, punct=None): return tok("أَيِ" if kasra else "أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=punct)

# ----------- s1 — the third division defined
S.append({"id": "s1", "translation": {"en": "And the third division is what by origin is not governed, yet may stand in the place of the second division and so be governed; and it too is two.", "tr": "Üçüncü kısım, aslında ma'mûl olmayan fakat bazen ikinci kısmın yerinde bulunup ma'mûl olandır; o da ikidir."},
 "tokens": [
  tok("وَالْقِسْمُ", "qism", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْقِسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division» — the mubtada.", "«ve kısım» — mübtedâ.", segments=wa("الْقِسْمُ", "qism", "noun")),
  tok("الثَّالِثُ", "thalith", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«third» — a naʿt.", "«üçüncü» — na't."),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber."),
  tok("كَانَ", "kana", "verb", [K, KN, HV, MAW], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةٌ.", "«is» — kāna, the relative clause.", "«olan» — kâne, sıla."),
  tok("الْأَصْلُ", "asl", "noun", [K, KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«the origin» — the ism of kāna.", "«asıl» — kâne'nin ismi."),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«in it»", "«onda»", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, KN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ كَانَ: عَدَمُ كَوْنِهِ مَعْمُولًا.", "«that» — the clause is the khabar of kāna.", "«… olmaması» — cümle kâne'nin haberi."),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-ma»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, HV, MJZ], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«be» — kāna in naṣb after an.", "«olması» — en ile mansûb kâne."),
  tok("مَعْمُولًا", "mamul", "noun", [K, KN, IMF], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«governed» — the khabar of kāna.", "«ma'mûl» — kâne'nin haberi.", punct="،"),
  tok("لٰكِنْ", "lakin", "part", [K, AT], "حَرْفُ اسْتِدْرَاكٍ.", "«yet»", "«fakat»"),
  tok("قَدْ", "qad", "part", [K], "حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«may» — qad of rarity.", "«bazen» — taklîl kad'ı."),
  tok("يَقَعُ", "waqaa", "verb", [K, FL, MR, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«stands»", "«bulunur»"),
  tok("مَوْقِعَ", "mawqi", "noun", [K, MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«in the place of»", "«… yerinde»"),
  tok("الْقِسْمِ", "qism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the division»", "«kısmın»"),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«second»", "«ikinci»"),
  tok("فَيَكُونُ", "kana", "verb", [K, AT, KN, HV, MR], "الْفَاءُ عَاطِفَةٌ لِلسَّبَبِيَّةِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and so is»", "«ve böylece olur»", segments=fa("يَكُونُ", "kana", "verb")),
  tok("مَعْمُولًا", "mamul", "noun", [K, KN, IMF], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«governed»", "«ma'mûl»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("اثْنَانِ", "ithnan", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two» — the khabar.", "«iki» — haber."),
  tok("أَيْضًا", "aydan", "noun", [K, MM], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ.", "«too»", "«da»", punct="."),
 ]})
# ----------- s2 — the māḍī: its place after أَنْ and after the jāzim
S.append({"id": "s2", "translation": {"en": "The first is the māḍī: when it stands after the maṣdar-making an, its place is ruled to be naṣb; and when it stands after the jāzim, as a protasis or an apodosis, its place is ruled to be jazm — because that iʿrāb appears in what is joined to it.", "tr": "İlki mâzîdir: mastariyye en'den sonra bulunduğunda mahallinin nasb olduğuna, câzimden sonra şart veya cezâ olarak bulunduğunda mahallinin cezm olduğuna hükmedilir — çünkü o i'râb ma'tûfta görünür."},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«ilki» — mübtedâ."),
  tok("الْمَاضِي", "madi", "noun", [K, MK, MQ], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«the māḍī» — the khabar.", "«mâzî» — haber.", punct="،"),
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«for it»", "«çünkü o»", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("إِذَا", "idha", "part", [K, MF, SH], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-diğinde»"),
  tok("وَقَعَ", "waqaa", "verb", [K, SH, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«it stands»", "«bulunur»"),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«-den sonra»"),
  tok("أَنِ", "an-masdariyya", "part", [K, ID, AMS], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«an» — the cited particle, annexed to.", "«en» — hikâye edilen, muzâfun ileyh."),
  tok("الْمَصْدَرِيَّةِ", "masdariyya", "noun", [K, NA, AMS], "نَعْتٌ مَجْرُورٌ.", "«maṣdar-making» — a naʿt.", "«mastariyye» — na't."),
  tok("يُحْكَمُ", "hakama", "verb", [K, NF, SH, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — جَوَابُ إِذَا.", "«it is ruled» — the apodosis.", "«hükmedilir» — cevap."),
  tok("عَلَى", "ala", "prep", [K, HJ, NF], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَائِبُ الْفَاعِلِ.", "«of»", "«hakkında»"),
  tok("مَحَلِّهِ", "mahall", "noun", [K, HJ, ID, MH], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its place»", "«mahalline»", segments=[seg("مَحَلِّ", "mahall", "noun"), pr3msi()]),
  tok("بِالنَّصْبِ", "nasb", "noun", [K, HJ, MH], "الْبَاءُ حَرْفُ جَرٍّ، وَالنَّصْبِ مَجْرُورٌ.", "«to be naṣb»", "«nasb olduğuna»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("النَّصْبِ", "nasb", "noun")]),
  tok("وَإِذَا", "idha", "part", [K, AT, MF, SH], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve -diğinde»", segments=wa("إِذَا", "idha", "part")),
  tok("وَقَعَ", "waqaa", "verb", [K, SH, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«it stands»", "«bulunur»"),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«-den sonra»"),
  tok("الْجَازِمِ", "jazim", "noun", [K, ID, MJZ, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — إِنْ وَأَخَوَاتُهَا.", "«the jāzim» — in and its sisters.", "«câzim» — in ve kardeşleri."),
  tok("شَرْطًا", "shart", "noun", [K, HL, SH], "حَالٌ مَنْصُوبٌ — كَوْنُهُ شَرْطًا.", "«as a protasis» — a ḥāl.", "«şart olarak» — hâl."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("جَزَاءً", "jaza-answer", "noun", [K, AT, HL, SH], "مَعْطُوفٌ عَلَى شَرْطًا مَنْصُوبٌ — جَوَابُ الشَّرْطِ.", "«an apodosis» — the condition's answer.", "«cezâ» — şartın cevabı."),
  tok("يُحْكَمُ", "hakama", "verb", [K, NF, SH, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — جَوَابُ إِذَا.", "«it is ruled»", "«hükmedilir»"),
  tok("عَلَى", "ala", "prep", [K, HJ, NF], "حَرْفُ جَرٍّ.", "«of»", "«hakkında»"),
  tok("مَحَلِّهِ", "mahall", "noun", [K, HJ, ID, MH], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its place»", "«mahalline»", segments=[seg("مَحَلِّ", "mahall", "noun"), pr3msi()]),
  tok("بِالْجَزْمِ", "jazm", "noun", [K, HJ, MH], "الْبَاءُ حَرْفُ جَرٍّ، وَالْجَزْمِ مَجْرُورٌ.", "«to be jazm»", "«cezm olduğuna»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْجَزْمِ", "jazm", "noun")]),
  tok("لِظُهُورِ", "zuhur", "noun", [K, HJ, ID, MSD, MFL], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَظُهُورِ مَجْرُورٌ، مُضَافٌ.", "«because of the appearing of»", "«görünmesi sebebiyle»", segments=[seg("لِ", "li", "prep"), seg("ظُهُورِ", "zuhur", "noun")]),
  tok("ذٰلِكَ", "dhalika", "pron", [K, ID, ISH], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that»", "«o»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, BD, MH], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«iʿrāb» — a badal.", "«i'râb» — bedel."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمَعْطُوفِ", "matuf", "noun", [K, HJ, IMF, AT], "مَجْرُورٌ بِفِي — الْمُضَارِعُ الْمَعْطُوفُ عَلَى الْمَاضِي.", "«what is joined» — the muḍāriʿ joined to the māḍī.", "«ma'tûf» — mâzîye atfedilen muzâri.", punct="."),
 ]})
# ----------- s3 — the examples; elsewhere not governed
S.append({"id": "s3", "translation": {"en": "As in «it pleased me that you struck and [that you] kill» and «if you struck and [if you] kill, I would strike you and kill»; and in other than these two positions it is not governed.", "tr": "«Vurman ve öldürmen hoşuma gitti» ve «vurursan ve öldürürsen seni vururum ve öldürürüm» gibi; bu iki yerin dışında ma'mûl olmaz."},
 "tokens": [
  nahw(),
  tok("أَعْجَبَنِي", "ajaba-please", "verb", [K, FL, MB, F4], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«it pleased me»", "«hoşuma gitti»", segments=[seg("أَعْجَبَ", "ajaba-please", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, FL], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ أَعْجَبَ.", "«that» — the clause is the doer of «pleased».", "«-men» — cümle a'cebe'nin fâili."),
  tok("ضَرَبْتَ", "daraba", "verb", [K, AMS, FL, MH], "فِعْلٌ مَاضٍ فِي مَحَلِّ نَصْبٍ بِأَنْ، وَالتَّاءُ فَاعِلٌ.", "«you struck» — the māḍī in the place of naṣb.", "«vurdun» — nasb mahallinde mâzî.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("وَتَقْتُلَ", "qatala", "verb", [K, AT, MJZ, FL], "الْوَاوُ عَاطِفَةٌ، وَتَقْتُلَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ — مَعْطُوفٌ عَلَى مَحَلِّ ضَرَبْتَ، وَفِيهِ ظَهَرَ النَّصْبُ.", "«and [that you] kill» — joined to the māḍī's place: the naṣb shows here.", "«ve öldürmen» — mâzînin mahalline ma'tûf: nasb burada görünür.", punct="،", segments=wa("تَقْتُلَ", "qatala", "verb")),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("ضَرَبْتَ", "daraba", "verb", [K, SH, FL, MH], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«you struck» — the protasis in the place of jazm.", "«vurursan» — cezm mahallinde şart fiili.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("وَتَقْتُلْ", "qatala", "verb", [K, AT, MJZ, FL], "الْوَاوُ عَاطِفَةٌ، وَتَقْتُلْ فِعْلٌ مُضَارِعٌ مَجْزُومٌ — مَعْطُوفٌ عَلَى مَحَلِّ ضَرَبْتَ.", "«and [if you] kill» — joined to the protasis's place: jazm.", "«ve öldürürsen» — şartın mahalline ma'tûf: cezm.", segments=wa("تَقْتُلْ", "qatala", "verb")),
  tok("ضَرَبْتُكَ", "daraba", "verb", [K, SH, FL, MB, MH], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I would strike you» — the apodosis in the place of jazm.", "«seni vururum» — cezm mahallinde cevap.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَأَقْتُلْ", "qatala", "verb", [K, AT, MJZ, FL], "الْوَاوُ عَاطِفَةٌ، وَأَقْتُلْ فِعْلٌ مُضَارِعٌ مَجْزُومٌ — مَعْطُوفٌ عَلَى مَحَلِّ الْجَوَابِ.", "«and kill» — joined to the apodosis's place.", "«ve öldürürüm» — cevabın mahalline ma'tûf.", punct="،", segments=wa("أَقْتُلْ", "qatala", "verb")),
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ لِمَا بَعْدَهُ (أَوْ مُتَعَلِّقٌ بِيَكُونُ).", "«and in»", "«ve … -de»", segments=wa("فِي", "fi", "prep")),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«… dışında»"),
  tok("هٰذَيْنِ", "hadhayn", "pron", [K, ID, ISH, MTH], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — مُثَنًّى.", "«these two»", "«bu iki»"),
  tok("الْمَوْضِعَيْنِ", "mawdi", "noun", [K, BD, MTH], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«positions» — a badal in the dual.", "«yerin» — tesniye bedel."),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمَاضِي.", "«it is» — the māḍī.", "«olmaz» — mâzî."),
  tok("مَعْمُولًا", "mamul", "noun", [K, KN, IMF], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«governed»", "«ma'mûl»", punct="."),
 ]})
# ----------- s4 — the second: the sentence; the verbal sentence
S.append({"id": "s4", "translation": {"en": "And the second is the sentence, and it is of two kinds: verbal — that composed of a verb, in word or in sense, and its doer, as in «Zayd struck», «if you honour me I honour you», «far is Zayd!», «are the two Zayds standing?».", "tr": "İkincisi cümledir; o da iki kısımdır: fiiliyye — lafzen veya mânen fiil ile fâilinden mürekkeb olan: «Zeyd vurdu», «bana ikram edersen sana ikram ederim», «Zeyd uzaktır!», «iki Zeyd ayakta mı?» gibi."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second» — the mubtada.", "«ikincisi» — mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْجُمْلَةُ", "jumla", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ.", "«the sentence» — the khabar.", "«cümle» — haber.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هِيَ", "hiya", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the khabar.", "«üzere» — haber."),
  tok("قِسْمَيْنِ", "qism", "noun", [K, HJ, MTH], "مَجْرُورٌ بِعَلَى بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two kinds» — the dual.", "«iki kısım» — tesniye.", punct=":"),
  tok("فِعْلِيَّةٌ", "filiyya", "noun", [K, MK, HT, NSB], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ: أَحَدُهُمَا فِعْلِيَّةٌ.", "«verbal» — the khabar of a dropped «one of them».", "«fiiliyye» — hazfedilmiş «biri»nin haberi.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it»", "«ve o»", segments=wa("هِيَ", "hiya", "pron")),
  tok("الْمُرَكَّبَةُ", "murakkab", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ رَكَّبَ.", "«the one composed» — the khabar.", "«mürekkeb olan» — haber."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("الْفِعْلِ", "fil", "noun", [K, HJ, KK], "مَجْرُورٌ بِمِنْ.", "«a verb»", "«fiil»"),
  tok("لَفْظًا", "lafz", "noun", [K, TM, HL], "تَمْيِيزٌ (أَوْ حَالٌ) مَنْصُوبٌ — مِنْ جِهَةِ اللَّفْظِ.", "«in word» — a tamyīz: in respect of the wording.", "«lafzen» — temyiz: lafız bakımından."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَعْنًى", "mana", "noun", [K, AT, TM, MQ], "مَعْطُوفٌ عَلَى لَفْظًا مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — كَاسْمِ الْفِعْلِ.", "«in sense» — such as the noun-verb.", "«mânen» — isim fiil gibi."),
  tok("وَفَاعِلِهِ", "fail-doer", "noun", [K, AT, ID, FL], "الْوَاوُ عَاطِفَةٌ، وَفَاعِلِهِ مَعْطُوفٌ عَلَى الْفِعْلِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its doer»", "«ve fâilinden»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("فَاعِلِ", "fail-doer", "noun"), pr3msi()]),
  nahw(),
  tok("ضَرَبَ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ.", "«struck»", "«vurdu»"),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="،"),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ — لَفْظٌ مَحْكِيٌّ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("تُكْرِمْنِي", "akrama", "verb", [K, SH, MJZ, FL, MB, F4], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you honour me» — the protasis.", "«bana ikram edersen» — şart fiili.", segments=[seg("تُكْرِمْ", "akrama", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("أُكْرِمْكَ", "akrama", "verb", [K, SH, MJZ, FL, MB, F4], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ جَوَابُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I honour you» — the apodosis.", "«sana ikram ederim» — cevap.", punct="،", segments=[seg("أُكْرِمْ", "akrama", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَهَيْهَاتَ", "hayhat", "noun", [K, AT, IFL, MNF, FL], "الْوَاوُ عَاطِفَةٌ، وَهَيْهَاتَ اسْمُ فِعْلٍ مَاضٍ بِمَعْنَى بَعُدَ — الْفِعْلُ مَعْنًى.", "«and far is» — the noun-verb: the verb in sense.", "«ve uzaktır» — isim fiil: mânen fiil.", segments=wa("هَيْهَاتَ", "hayhat", "noun")),
  tok("زَيْدٌ", "zayd", "propn", [K, IFL, FL], "فَاعِلُ اسْمِ الْفِعْلِ مَرْفُوعٌ.", "«Zayd» — the noun-verb's doer.", "«Zeyd» — isim fiilin fâili.", punct="،"),
  tok("وَأَقَائِمٌ", "qaim", "noun", [K, AT, IST, IFA, MK, MNF], "الْوَاوُ عَاطِفَةٌ، وَالْهَمْزَةُ لِلِاسْتِفْهَامِ، وَقَائِمٌ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ بِمَعْنَى الْفِعْلِ اعْتَمَدَ عَلَى الِاسْتِفْهَامِ.", "«and are … standing» — the participle leaning on the question: the verb in sense.", "«ve ayakta mı» — istifhâma dayanan ism-i fâil: mânen fiil.", segments=[seg("وَ", "wa", "conj"), seg("أَ", "a-istifham", "part"), seg("قَائِمٌ", "qaim", "noun")]),
  tok("الزَّيْدَانِ", "zayd", "propn", [K, FL, MTH, MK], "فَاعِلٌ سَدَّ مَسَدَّ الْخَبَرِ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«the two Zayds» — the doer that fills the khabar's place.", "«iki Zeyd» — haberin yerini tutan fâil.", punct="."),
 ]})
# ----------- s5 — the nominal sentence
S.append({"id": "s5", "translation": {"en": "And nominal — that composed of the mubtada and the khabar, or of the governing particle's ism and its khabar, as in «Zayd is standing» and «indeed Zayd is standing».", "tr": "Ve ismiyye — mübtedâ ile haberden ya da âmil olan harfin ismi ile haberinden mürekkeb olan: «Zeyd ayaktadır» ve «şüphesiz Zeyd ayaktadır» gibi."},
 "tokens": [
  tok("وَاسْمِيَّةٌ", "ismiyya", "noun", [K, AT, MK, NSB], "الْوَاوُ عَاطِفَةٌ، وَاسْمِيَّةٌ مَعْطُوفٌ عَلَى فِعْلِيَّةٌ مَرْفُوعٌ.", "«and nominal» — joined to «verbal».", "«ve ismiyye» — fiiliyye'ye ma'tûf.", punct="،", segments=wa("اسْمِيَّةٌ", "ismiyya", "noun")),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it»", "«ve o»", segments=wa("هِيَ", "hiya", "pron")),
  tok("الْمُرَكَّبَةُ", "murakkab", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«the one composed»", "«mürekkeb olan»"),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "مَجْرُورٌ بِمِنْ.", "«the mubtada»", "«mübtedâ»"),
  tok("وَالْخَبَرِ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar»", "«ve haber»", segments=wa("الْخَبَرِ", "khabar-predicate", "noun")),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مِنِ", "min", "prep", [K, HJ, AT], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("اسْمِ", "ism", "noun", [K, HJ, ID, IN], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«the ism of»", "«ismi»"),
  tok("الْحَرْفِ", "harf", "noun", [K, ID, IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ (قُرِئَ فِي الطَّبْعَةِ: الْجَرِّ).", "«the particle» — the lithograph transcription reads «al-jarr» here.", "«harf» — taşbaskı transkripsiyonunda «el-cerr» okunmuş."),
  tok("الْعَامِلِ", "amil-governor", "noun", [K, NA, IN], "نَعْتٌ مَجْرُورٌ — إِنَّ وَأَخَوَاتُهَا.", "«governing» — inna and its sisters.", "«âmil olan» — inne ve kardeşleri."),
  tok("وَخَبَرِهِ", "khabar-predicate", "noun", [K, AT, ID, IN], "الْوَاوُ عَاطِفَةٌ، وَخَبَرِهِ مَعْطُوفٌ عَلَى اسْمِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its khabar»", "«ve haberinden»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("خَبَرِ", "khabar-predicate", "noun"), pr3msi()]),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«standing» — the khabar.", "«ayakta» — haber.", punct="،"),
  tok("وَإِنَّ", "inna", "part", [K, AT, IN], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — لَفْظٌ مَحْكِيٌّ.", "«and indeed»", "«ve şüphesiz»", segments=wa("إِنَّ", "inna", "part")),
  tok("زَيْدًا", "zayd", "propn", [K, IN], "اسْمُ إِنَّ مَنْصُوبٌ.", "«Zayd» — the ism of inna.", "«Zeyd» — inne'nin ismi."),
  tok("قَائِمٌ", "qaim", "noun", [K, IN, IFA], "خَبَرُ إِنَّ مَرْفُوعٌ.", "«standing» — the khabar of inna.", "«ayakta» — inne'nin haberi.", punct="."),
 ]})
# ----------- s6 — when the wording of the sentence is intended, it has iʿrāb
S.append({"id": "s6", "translation": {"en": "Now if the sentence's wording is intended, it must have iʿrāb, since it stands in the ruling of a single noun — so that it may stand wherever one stands: it occurs as a mubtada, a doer and other than that, as in «‹Zayd is standing› is a nominal sentence», that is, this wording.", "tr": "Cümleyle lafzı kastedilirse, müfred isim hükmünde olduğundan i'râbı olması gerekir; öyle ki müfred ismin bulunduğu her yerde bulunabilir: mübtedâ, fâil ve başka şeyler olarak gelir, «‹Zeyd ayaktadır› isim cümlesidir» yani bu lafız, gibi."},
 "tokens": [
  tok("فَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«now if»", "«eğer»", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("أُرِيدَ", "arada", "verb", [K, SH, NF, F4, HV], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.", "«is intended» — the passive protasis.", "«kastedilirse» — meçhul şart fiili."),
  tok("بِالْجُمْلَةِ", "jumla", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْجُمْلَةِ مَجْرُورٌ.", "«by the sentence»", "«cümleyle»", segments=[seg("بِ", "bi", "prep"), seg("الْجُمْلَةِ", "jumla", "noun")]),
  tok("لَفْظُهَا", "lafz", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its wording» — the deputy doer.", "«lafzı» — nâib-i fâil.", segments=[seg("لَفْظُ", "lafz", "noun"), pr3fs()]),
  tok("فَلَا", "la-nafiya", "part", [K, SH, LAJ], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«then no» — the apodosis.", "«o hâlde yok» — cevap.", segments=fa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, LAJ, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ — لَا بُدَّ: لَا مَفَرَّ.", "«escape» — the ism of lā: «there is no avoiding».", "«çare» — lâ'nın ismi: lâ büdde."),
  tok("لَهَا", "li", "prep", [K, HJ, LAJ], "اللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«for it» — the khabar of lā.", "«onun için» — lâ'nın haberi.", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("إِعْرَابٍ", "irab", "noun", [K, HJ, MH], "مَجْرُورٌ بِمِنْ.", "«iʿrāb»", "«i'râb»"),
  tok("لِكَوْنِهَا", "kawn", "noun", [K, HJ, ID, MSD, MFL], "اللَّامُ لِلتَّعْلِيلِ، وَكَوْنِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«because of its being»", "«olması sebebiyle»", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3fs()]),
  tok("فِي", "fi", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — خَبَرُ كَوْنِهَا.", "«in» — the khabar of «being».", "«-de» — kevn'in haberi."),
  tok("حُكْمِ", "hukm", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the ruling of»", "«hükmünde»"),
  tok("الِاسْمِ", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the noun»", "«ismin»"),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ — الْمُفْرَدُ: مَا لَيْسَ بِجُمْلَةٍ.", "«single» — not a sentence.", "«müfred» — cümle olmayan.", punct="،"),
  tok("حَتَّى", "hatta", "part", [K, AMS], "حَرْفُ جَرٍّ وَغَايَةٍ — وَالْمُضَارِعُ بَعْدَهَا مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«so that» — the muḍāriʿ after it in naṣb by a hidden an.", "«öyle ki» — sonrasındaki muzâri gizli en ile mansûb."),
  tok("يَجُوزَ", "jaaza", "verb", [K, MJZ, HV, FL], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى.", "«it is allowed»", "«câiz olur»"),
  tok("وُقُوعُهَا", "wuqu", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its standing» — the doer.", "«bulunması» — fâil.", segments=[seg("وُقُوعُ", "wuqu", "noun"), pr3fs()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("كُلِّ", "kull", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«every»", "«her»"),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«[place] that»", "«yerde»"),
  tok("وَقَعَ", "waqaa", "verb", [K, FL, MAW], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الِاسْمُ الْمُفْرَدُ؛ صِلَةُ مَا.", "«stands» — the single noun; the relative clause.", "«bulunur» — müfred isim; sıla."),
  tok("فِيهِ", "fi", "prep", [K, HJ, MAW], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«in it»", "«onda»", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("فَتَقَعُ", "waqaa", "verb", [K, AT, FL, MR, "mithal-verbs"], "الْفَاءُ عَاطِفَةٌ لِلتَّفْرِيعِ، وَتَقَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«so it occurs»", "«böylece gelir»", segments=fa("تَقَعُ", "waqaa", "verb")),
  tok("مُبْتَدَأً", "mubtada", "noun", [K, HL, MK], "حَالٌ مَنْصُوبٌ.", "«as a mubtada» — a ḥāl.", "«mübtedâ olarak» — hâl."),
  tok("وَفَاعِلًا", "fail-doer", "noun", [K, AT, HL, FL], "الْوَاوُ عَاطِفَةٌ، وَفَاعِلًا مَعْطُوفٌ مَنْصُوبٌ.", "«and a doer»", "«ve fâil»", segments=wa("فَاعِلًا", "fail-doer", "noun")),
  tok("وَغَيْرَ", "ghayr", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and other than»", "«ve … başkası»", segments=wa("غَيْرَ", "ghayr", "noun")),
  tok("ذٰلِكَ", "dhalika", "pron", [K, ID, ISH], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that»", "«bu»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, HT], "لَفْظٌ مَحْكِيٌّ: الْجُمْلَةُ «زَيْدٌ قَائِمٌ» مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — قُصِدَ لَفْظُهَا.", "«Zayd» — the quoted sentence as a mubtada.", "«Zeyd» — mübtedâ olan hikâye edilen cümle."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA, HT], "لَفْظٌ مَحْكِيٌّ: تَمَامُ الْجُمْلَةِ الْمُبْتَدَإِ.", "«is standing» — the rest of the quoted sentence.", "«ayaktadır» — hikâye edilen cümlenin devamı."),
  tok("جُمْلَةٌ", "jumla", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ.", "«a sentence» — the khabar.", "«bir cümle» — haber."),
  tok("اسْمِيَّةٌ", "ismiyya", "noun", [K, NA, NSB], "نَعْتٌ مَرْفُوعٌ.", "«nominal» — a naʿt.", "«isim …» — na't.", punct="،"),
  ay(),
  tok("هٰذَا", "hadha", "pron", [K, MK, ISH, HT], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْمُرَادُ بِالْجُمْلَةِ هٰذَا.", "«this» — the mubtada: what is meant is this.", "«bu» — mübtedâ."),
  tok("اللَّفْظُ", "lafz", "noun", [K, BD, MK], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ (وَالْخَبَرُ مَحْذُوفٌ: هُوَ الْمُرَادُ).", "«wording» — a badal; the khabar dropped.", "«lafız» — bedel; haber hazfedilmiş.", punct="."),
 ]})
# ----------- s7 — the saying's content
S.append({"id": "s7", "translation": {"en": "And likewise the content of a saying, as in His word, Most High: «and when it is said to them: believe».", "tr": "Makûlü'l-kavl de böyledir, Allah Teâlâ'nın «onlara ‹iman edin› denildiğinde» sözündeki gibi."},
 "tokens": [
  tok("وَمِثْلُ", "mithl", "noun", [K, AT, MK, ID, HT], "الْوَاوُ عَاطِفَةٌ، وَمِثْلُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَالْخَبَرُ مَحْذُوفٌ: مِثْلُ مَقُولِ الْقَوْلِ لَهُ إِعْرَابٌ.", "«and likewise» — the mubtada; its khabar dropped.", "«ve … gibi» — mübtedâ; haberi hazfedilmiş.", segments=wa("مِثْلُ", "mithl", "noun")),
  tok("مَقُولِ", "maqul", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — اسْمُ مَفْعُولِ قَالَ.", "«the content of» — the ism mafʿūl of «to say».", "«makûl» — kâle'nin ism-i mef'ûlü."),
  tok("الْقَوْلِ", "qawl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَقُولُ الْقَوْلِ: الْجُمْلَةُ مَفْعُولُ قَالَ.", "«the saying» — the sentence as the object of «said».", "«kavl» — kâle'nin mef'ûlü olan cümle.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as in»", "«… gibi»"),
  qawlihi(),
  taala(),
  tok("وَإِذَا", "idha", "part", [K, QA, MF, SH], "لَفْظٌ مَحْكِيٌّ (مِنَ الْقُرْآنِ، الْبَقَرَة ١٣): الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — al-Baqara 13.", "«ve -diğinde» — Bakara 13.", segments=wa("إِذَا", "idha", "part")),
  tok("قِيلَ", "qala", "verb", [K, QA, NF, HV, SH], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَقُولَةُ: آمِنُوا.", "«it is said» — the deputy doer is the sentence said.", "«denildi» — nâib-i fâil söylenen cümle."),
  tok("لَهُمْ", "li", "prep", [K, QA, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَهُمْ فِي مَحَلِّ جَرٍّ.", "«to them»", "«onlara»", segments=[seg("لَ", "li", "prep"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("آمِنُوا", "aamana", "verb", [K, QA, AMR, F4, NF], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — الْجُمْلَةُ مَقُولُ الْقَوْلِ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«believe» — the sentence said, in the place of rafʿ as the deputy doer.", "«iman edin» — makûlü'l-kavl, nâib-i fâil olarak ref' mahallinde.", punct=".", segments=[seg("آمِنُ", "aamana", "verb"), seg("وا", "pron-2mp", "pron")]),
 ]})
# ----------- s8 — a maṣdar sense through أَنْ / أَنَّ / مَا
S.append({"id": "s8", "translation": {"en": "And likewise if a maṣdar's sense is intended by it — either by means of an, anna or mā, the maṣdar-makers, as in your saying «it reached me that you are standing» and His word, Most High: «and that you fast is better for you».", "tr": "Cümleyle mastar mânâsı kastedilirse de böyledir — ya mastariyye olan en, enne veya mâ vasıtasıyla, «ayakta olduğun bana ulaştı» sözün ve Allah Teâlâ'nın «oruç tutmanız sizin için daha hayırlıdır» sözü gibi."},
 "tokens": [
  tok("وَكَذَا", "kadha", "part", [K, AT, MK, HT], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ — خَبَرٌ مُقَدَّمٌ لِمُبْتَدَإٍ مَحْذُوفٍ: الْأَمْرُ كَذَا.", "«and likewise»", "«ve böyledir»", segments=wa("كَذَا", "kadha", "part")),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("أُرِيدَ", "arada", "verb", [K, SH, NF, F4, HV], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ.", "«is intended»", "«kastedilirse»"),
  tok("بِهَا", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — بِالْجُمْلَةِ.", "«by it» — by the sentence.", "«onunla» — cümleyle.", segments=[seg("بِ", "bi", "prep"), pr3fs()]),
  tok("مَعْنًى", "mana", "noun", [K, NF, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«a sense» — the deputy doer.", "«bir mânâ» — nâib-i fâil."),
  tok("مَصْدَرِيٌّ", "masdari", "noun", [K, NA, NSB, MSD], "نَعْتٌ مَرْفُوعٌ.", "«of a maṣdar» — a naʿt.", "«mastarî» — na't.", punct="،"),
  tok("إِمَّا", "imma", "part", [K, AT], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("بِوَاسِطَةِ", "wasita", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَوَاسِطَةِ مَجْرُورٌ، مُضَافٌ.", "«by means of»", "«vasıtasıyla»", segments=[seg("بِ", "bi", "prep"), seg("وَاسِطَةِ", "wasita", "noun")]),
  tok("أَنْ", "an-masdariyya", "part", [K, ID, AMS], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«an»", "«en»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("أَنَّ", "anna", "part", [K, AT, IN], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«anna»", "«enne»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَا", "ma-masdariyya", "part", [K, AT, AMS], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«mā»", "«mâ»"),
  tok("الْمَصْدَرِيَّتَيْنِ", "masdariyya", "noun", [K, NA, MTH, AMS], "نَعْتٌ لِلْمَعْطُوفَيْنِ (أَنْ وَمَا) مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — كَذَا فِي الطَّبْعَةِ.", "«the two maṣdar-makers» — the dual as the print has it.", "«iki mastariyye» — baskıdaki gibi tesniye."),
  tok("كَقَوْلِكَ", "qawl", "noun", [K, HJ, ID, MK], "الْكَافُ حَرْفُ جَرٍّ، وَقَوْلِكَ مَجْرُورٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«as your saying»", "«… sözün gibi»", punct=":", segments=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("بَلَغَنِي", "balagha", "verb", [K, FL, MB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«it reached me»", "«bana ulaştı»", segments=[seg("بَلَغَ", "balagha", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("أَنَّكَ", "anna", "part", [K, IN, FL], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ بَلَغَ: قِيَامُكَ.", "«that you» — the clause is the doer: «your standing».", "«senin» — cümle fâil: kıyâmın.", segments=[seg("أَنَّ", "anna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("قَائِمٌ", "qaim", "noun", [K, IN, IFA], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«standing» — the khabar of anna.", "«ayakta» — enne'nin haberi.", punct="،"),
  qawlihi("وَكَ", None) if False else tok("وَكَقَوْلِهِ", "qawl", "noun", [K, AT, HJ, ID, QA], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ حَرْفُ جَرٍّ، وَقَوْلِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and as His word»", "«ve O'nun sözü gibi»", segments=[seg("وَ", "wa", "conj"), seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  taala(),
  tok("وَأَنْ", "an-masdariyya", "part", [K, QA, AMS, MK], "لَفْظٌ مَحْكِيٌّ (مِنَ الْقُرْآنِ، الْبَقَرَة ١٨٤): الْوَاوُ عَاطِفَةٌ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ: صَوْمُكُمْ.", "«and that» — al-Baqara 184: the clause is the mubtada, «your fasting».", "«ve … -nız» — Bakara 184: cümle mübtedâ: savmüküm.", segments=wa("أَنْ", "an-masdariyya", "part")),
  tok("تَصُومُوا", "saama", "verb", [K, QA, MJZ, HV, FL, AMS], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«you fast» — naṣb by the dropped nūn.", "«oruç tutmanız» — nûnun hazfiyle mansûb.", segments=[seg("تَصُومُ", "saama", "verb"), seg("وا", "pron-2mp", "pron")]),
  tok("خَيْرٌ", "khayr", "noun", [K, QA, MK, ITF], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.", "«better» — the khabar: the tafḍīl without its hamza.", "«daha hayırlı» — haber: hemzesi düşmüş ism-i tafdîl."),
  tok("لَكُمْ", "li", "prep", [K, QA, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ فِي مَحَلِّ جَرٍّ.", "«for you»", "«sizin için»", punct=".", segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")]),
 ]})
# ----------- s9 — or without them: the clause annexed to
S.append({"id": "s9", "translation": {"en": "Or without them, as the sentence to which something is annexed, as in His word, Most High: «the day their truthfulness profits the truthful» — that is, the day of the profiting of the truthfulness of the truthful.", "tr": "Ya da onlarsız — kendisine izâfet yapılan cümle gibi: Allah Teâlâ'nın «doğruların doğruluklarının kendilerine fayda vereceği gün» sözündeki gibi, yani doğruların doğruluğunun fayda verme günü."},
 "tokens": [
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("بِغَيْرِهَا", "ghayr", "noun", [K, AT, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — مَعْطُوفٌ عَلَى بِوَاسِطَةِ.", "«without them» — joined to «by means of».", "«onlarsız» — bi-vâsıta'ya ma'tûf.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as»", "«… gibi»"),
  tok("الْجُمْلَةِ", "jumla", "noun", [K, ID, KK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence»", "«cümle»"),
  tok("الَّتِي", "allati", "pron", [K, NA, MAW], "اسْمٌ مَوْصُولٌ نَعْتٌ فِي مَحَلِّ جَرٍّ.", "«which»", "«ki»"),
  tok("أُضِيفَ", "adafa", "verb", [K, NF, F4, HV, MAW, ID], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ؛ وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«is annexed» — the relative clause.", "«izâfe edilen» — sıla."),
  tok("إِلَيْهَا", "ila", "prep", [K, HJ, NF, MAW], "إِلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«to it»", "«ona»", punct="،", segments=[seg("إِلَيْ", "ila", "prep"), pr3fs()]),
  tok("كَقَوْلِهِ", "qawl", "noun", [K, HJ, ID, QA], "الْكَافُ حَرْفُ جَرٍّ، وَقَوْلِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«as His word»", "«O'nun sözü gibi»", segments=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  taala(),
  tok("يَوْمَ", "yawm", "noun", [K, QA, MF, ID], "لَفْظٌ مَحْكِيٌّ (مِنَ الْقُرْآنِ، الْمَائِدَة ١١٩): ظَرْفٌ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ.", "«the day» — al-Māʾida 119: the ẓarf annexed to the sentence.", "«gün» — Mâide 119: cümleye muzâf zarf."),
  tok("يَنْفَعُ", "nafaa", "verb", [K, QA, FL, ID, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا فِي مَحَلِّ جَرٍّ.", "«profits» — the sentence in the place of jarr.", "«fayda verir» — cümle cer mahallinde."),
  tok("الصَّادِقِينَ", "sadiq", "noun", [K, QA, MB, JMS, IFA], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the truthful» — the fronted object.", "«doğrulara» — öne alınmış mef'ûl."),
  tok("صِدْقُهُمْ", "sidq", "noun", [K, QA, FL, ID], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their truthfulness» — the delayed doer.", "«doğrulukları» — sonraya bırakılmış fâil.", segments=[seg("صِدْقُ", "sidq", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  ay(),
  tok("يَوْمَ", "yawm", "noun", [K, MF, ID, HT], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — التَّقْدِيرُ بِالْمَصْدَرِ.", "«the day of» — the supplied reading with the maṣdar.", "«günü» — mastarlı takdir."),
  tok("نَفْعِ", "naf", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ نَفَعَ.", "«the profiting of»", "«fayda vermesinin»"),
  tok("صِدْقِ", "sidq", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the truthfulness of»", "«doğruluğunun»"),
  tok("الصَّادِقِينَ", "sadiq", "noun", [K, ID, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the truthful»", "«doğruların»", punct="."),
 ]})
# ----------- s10 — ﴿سَوَاءٌ عَلَيْهِمْ أَأَنْذَرْتَهُمْ أَمْ لَمْ تُنْذِرْهُمْ﴾
S.append({"id": "s10", "translation": {"en": "And as His word, Most High: «it is the same to them whether you warned them or did not warn them» — that is, your warning and your not warning.", "tr": "Ve Allah Teâlâ'nın «onları uyarsan da uyarmasan da onlar için birdir» sözü gibi — yani uyarman ve uyarmaman."},
 "tokens": [
  tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«and as»", "«ve … gibi»", segments=wa("نَحْوُ", "nahw", "noun")),
  qawlihi(),
  taala(),
  tok("سَوَاءٌ", "sawa", "noun", [K, QA, MK], "لَفْظٌ مَحْكِيٌّ (مِنَ الْقُرْآنِ، الْبَقَرَة ٦): خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«the same» — al-Baqara 6: the fronted khabar.", "«birdir» — Bakara 6: öne alınmış haber."),
  tok("عَلَيْهِمْ", "ala", "prep", [K, QA, HJ], "عَلَى حَرْفُ جَرٍّ، وَهِمْ فِي مَحَلِّ جَرٍّ.", "«to them»", "«onlar için»", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("أَأَنْذَرْتَهُمْ", "andhara", "verb", [K, QA, IST, FL, MB, F4, MK], "الْهَمْزَةُ لِلتَّسْوِيَةِ، وَأَنْذَرْتَ فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلٌ وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي تَأْوِيلِ مَصْدَرٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«whether you warned them» — the hamza of equivalence; the clause as a maṣdar is the delayed mubtada.", "«uyarsan da» — tesviye hemzesi; mastar hükmündeki cümle sonraya bırakılmış mübtedâ.", segments=[seg("أَ", "a-istifham", "part"), seg("أَنْذَرْ", "andhara", "verb"), seg("تَ", "pron-2ms", "pron"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("أَمْ", "am", "part", [K, QA, AT], "حَرْفُ عَطْفٍ — الْمُعَادِلَةُ لِهَمْزَةِ التَّسْوِيَةِ.", "«or» — the am that answers the hamza.", "«da» — tesviye hemzesinin dengi."),
  tok("لَمْ", "lam-jazima", "part", [K, QA, MJZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-ma»"),
  tok("تُنْذِرْهُمْ", "andhara", "verb", [K, QA, MJZ, FL, MB, F4], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَهُمْ مَفْعُولٌ بِهِ.", "«you warn them»", "«uyarmasan da»", segments=[seg("تُنْذِرْ", "andhara", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  ay(),
  tok("إِنْذَارُكَ", "indhar", "noun", [K, MK, ID, MSD, HT], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — التَّقْدِيرُ بِالْمَصْدَرِ.", "«your warning» — the supplied maṣdar.", "«uyarman» — mastarlı takdir.", segments=[seg("إِنْذَارُ", "indhar", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَعَدَمُ", "adam", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَعَدَمُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the absence of»", "«ve … -maman»", segments=wa("عَدَمُ", "adam", "noun")),
  tok("إِنْذَارِكَ", "indhar", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your warning»", "«uyarman»", punct=".", segments=[seg("إِنْذَارِ", "indhar", "noun"), seg("كَ", "pron-2ms", "pron")]),
 ]})
# ----------- s11 — تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرٌ مِنْ أَنْ تَرَاهُ; confined to what was heard
S.append({"id": "s11", "translation": {"en": "And as «that you hear of the Muʿaydī is better than that you see him» — that is, your hearing; and this last is confined to what was heard.", "tr": "Ve «Muaydî'yi işitmen onu görmenden hayırlıdır» gibi — yani işitmen; bu sonuncusu semâa mahsustur."},
 "tokens": [
  tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«and as»", "«ve … gibi»", punct=":", segments=wa("نَحْوُ", "nahw", "noun")),
  tok("تَسْمَعُ", "samia", "verb", [K, MK, FL, MR, HT], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — الْجُمْلَةُ مُبْتَدَأٌ بِتَأْوِيلِ الْمَصْدَرِ بِلَا حَرْفٍ.", "«you hear» — the sentence as a maṣdar, the mubtada, with no particle.", "«işitirsin» — harfsiz mastar hükmünde mübtedâ cümle."),
  tok("بِالْمُعَيْدِيِّ", "muaydi", "noun", [K, HJ, NSB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمُعَيْدِيِّ مَجْرُورٌ — تَصْغِيرُ الْمَعَدِّيِّ.", "«of the Muʿaydī» — the diminutive of Maʿaddī.", "«Muaydî'yi» — Maaddî'nin tasgîri."),
  tok("خَيْرٌ", "khayr", "noun", [K, MK, ITF], "خَبَرٌ مَرْفُوعٌ.", "«better» — the khabar.", "«hayırlıdır» — haber."),
  tok("مِنْ", "min", "prep", [K, HJ, ITF], "حَرْفُ جَرٍّ.", "«than»", "«-den»"),
  tok("أَنْ", "an-masdariyya", "part", [K, HJ, AMS], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِمِنْ.", "«that»", "«-men»"),
  tok("تَرَاهُ", "raa", "verb", [K, MJZ, FL, MB, MQ], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«you see him»", "«onu görmen»", punct="،", segments=[seg("تَرَا", "raa", "verb"), pr3ms()]),
  ay(),
  tok("سَمَاعُكَ", "samaa", "noun", [K, MK, ID, MSD, HT], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — التَّقْدِيرُ بِالْمَصْدَرِ.", "«your hearing» — the supplied maṣdar.", "«işitmen» — mastarlı takdir.", punct="،", segments=[seg("سَمَاعُ", "samaa", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَهٰذَا", "hadha", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذَا اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and this» — the mubtada.", "«ve bu» — mübtedâ.", segments=wa("هٰذَا", "hadha", "pron")),
  tok("الْأَخِيرُ", "akhir-last", "noun", [K, BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ — التَّأْوِيلُ بِلَا حَرْفٍ.", "«last» — a badal: the maṣdar reading without a particle.", "«sonuncusu» — bedel: harfsiz te'vil."),
  tok("مَقْصُورٌ", "maqsur", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ قَصَرَ.", "«confined» — the khabar.", "«mahsus» — haber."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-a»"),
  tok("السَّمَاعِ", "samaa", "noun", [K, HJ, MSD], "مَجْرُورٌ بِعَلَى — مَا سُمِعَ عَنِ الْعَرَبِ، لَا يُقَاسُ عَلَيْهِ.", "«what was heard» — from the Arabs; no analogy on it.", "«semâ» — Araplardan işitilen; kıyas yapılmaz.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

NEW = {
 "matuf": G("matuf", "مَعْطُوف", "ع ط ف", "noun", "the word joined (maʿṭūf) — what follows the conjunction", "ma'tûf — atıf harfinden sonra gelen", 3),
 "maqul": G("maqul", "مَقُول", "ق و ل", "noun", "what is said — مَقُولُ الْقَوْلِ: the sentence that is the object of «said»", "makûl — makûlü'l-kavl: kâle'nin mef'ûlü olan cümle", 3),
 "naf": G("naf", "نَفْع", "ن ف ع", "noun", "benefit, profiting (maṣdar of نَفَعَ)", "fayda, yarar (nefea'nın mastarı)", 2),
 "indhar": G("indhar", "إِنْذَار", "ن ذ ر", "noun", "warning (maṣdar of أَنْذَرَ)", "uyarı, inzâr (enzera'nın mastarı)", 3, form="IV"),
 "muaydi": G("muaydi", "مُعَيْدِيّ", "ع د د", "noun", "the Muʿaydī — the little man of Maʿadd in the proverb «to hear of the Muʿaydī is better than to see him»", "Muaydî — «Muaydî'yi işitmek onu görmekten hayırlıdır» atasözündeki Maaddli adam", 5),
 "maqsur": G("maqsur", "مَقْصُور", "ق ص ر", "noun", "confined, restricted to (ism mafʿūl of قَصَرَ)", "mahsus, kısıtlı (kasara'nın ism-i mef'ûlü)", 3),
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
print("izhar ch19 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("waqaa", "kana", "hakama", "ajaba-please", "daraba", "qatala", "akrama", "arada", "jaaza", "qala", "aamana", "balagha", "saama", "adafa", "nafaa", "andhara", "samia", "raa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَاضِي وَالْجُمْلَةُ مَعْمُولَيْنِ: مَحَلُّ الْمَاضِي بَعْدَ أَنْ وَالْجَازِمِ، وَإِعْرَابُ الْجُمْلَةِ", "en": "The māḍī and the sentence as governed words: the māḍī's place after an and the jāzim, and the sentence's iʿrāb", "tr": "Ma'mûl olarak mâzî ve cümle: en ve câzimden sonra mâzînin mahalli, cümlenin i'râbı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الباب الثاني في المعمول: القسم الثالث", "مغني اللبيب لابن هشام — الجمل التي لها محل من الإعراب", "الكافية لابن الحاجب — الجملة"],
 "amil": "the third division of the governed: the māḍī, not governed by origin, takes a place of naṣb after أَنْ and a place of jazm after the jāzim (the iʿrāb shows on the muḍāriʿ joined to it); the sentence, verbal or nominal, takes iʿrāb when its wording is meant, as the saying's content, and as a maṣdar — through أَنْ / أَنَّ / مَا or without them (the clause annexed to, the سَوَاء clause, تَسْمَعُ بِالْمُعَيْدِيِّ)",
 "question": {
  "en": ["What is the third division of the governed? What by origin is not governed but may stand where the second division stands and so be governed: the māḍī and the sentence.",
         "When has the māḍī a maḥall? After the maṣdar-making an its place is naṣb; after the jāzim, as protasis or apodosis, its place is jazm — and that iʿrāb shows on the muḍāriʿ joined to it: أَعْجَبَنِي أَنْ ضَرَبْتَ وَتَقْتُلَ؛ إِنْ ضَرَبْتَ وَتَقْتُلْ ضَرَبْتُكَ وَأَقْتُلْ. Elsewhere it is not governed.",
         "What are the two kinds of sentence? Verbal — a verb, in word or in sense, with its doer (ضَرَبَ زَيْدٌ، إِنْ تُكْرِمْنِي أُكْرِمْكَ، هَيْهَاتَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ); nominal — mubtadaʾ and khabar, or the governing particle's ism and its khabar (زَيْدٌ قَائِمٌ، إِنَّ زَيْدًا قَائِمٌ).",
         "When does a sentence take iʿrāb? When its wording is meant — it then counts as a single noun and stands wherever one stands (زَيْدٌ قَائِمٌ جُمْلَةٌ اسْمِيَّةٌ); as the content of a saying (﴿وَإِذَا قِيلَ لَهُمْ آمِنُوا﴾); and when a maṣdar's sense is meant by it.",
         "How is the maṣdar sense reached? Through an, anna or mā the maṣdar-makers (بَلَغَنِي أَنَّكَ قَائِمٌ؛ ﴿وَأَنْ تَصُومُوا خَيْرٌ لَكُمْ﴾), or without them: the clause annexed to (﴿يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ﴾ = يَوْمَ نَفْعِ صِدْقِ الصَّادِقِينَ), the clause after the hamza of equivalence (﴿سَوَاءٌ عَلَيْهِمْ أَأَنْذَرْتَهُمْ أَمْ لَمْ تُنْذِرْهُمْ﴾ = إِنْذَارُكَ وَعَدَمُ إِنْذَارِكَ), and تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرٌ مِنْ أَنْ تَرَاهُ = سَمَاعُكَ — this last confined to what was heard.",
         "Why does the lithograph read «اسم الجر فالعامل»? The transcription garbles «اسْمِ الْحَرْفِ الْعَامِلِ» — the ism of the governing particle, إِنَّ — which the example إِنَّ زَيْدًا قَائِمٌ requires; the reader prints it so and flags it.",
         "What does the engine READ here? The DabtEngine jazms the muḍāriʿ joined to a protasis or apodosis in the māḍī, puts in naṣb the one joined to a māḍī after an, raises the doer of the verbal sentence and the khabar of the nominal one, reads the quoted sentence after نَحْوُ as its own clause, and gives the Qurʾānic clauses their iʿrāb word by word."],
  "tr": ["Ma'mûlün üçüncü kısmı nedir? Aslında ma'mûl olmayan fakat ikinci kısmın yerinde bulunup ma'mûl olabilen: mâzî ve cümle.",
         "Mâzînin ne zaman mahalli vardır? Mastariyye en'den sonra mahalli nasb; câzimden sonra şart veya cezâ olarak mahalli cezmdir — bu i'râb ona atfedilen muzâride görünür: a'cebenî en darabte ve taktüle; in darabte ve taktül darabtüke ve aktül. Başka yerde ma'mûl olmaz.",
         "Cümlenin iki kısmı nedir? Fiiliyye — lafzen veya mânen fiil ile fâili (darabe Zeydün, in tükrimnî ükrimke, heyhâte Zeydün, e-kâimün ez-Zeydâni); ismiyye — mübtedâ ile haber ya da âmil harfin ismi ile haberi (Zeydün kâimün, inne Zeyden kâimün).",
         "Cümle ne zaman i'râb alır? Lafzı kastedilince — o zaman müfred isim hükmündedir ve ismin bulunduğu her yerde bulunur (Zeydün kâimün cümletün ismiyyetün); makûlü'l-kavl olarak (﴿ve izâ kîle lehüm âminû﴾); ve onunla mastar mânâsı kastedilince.",
         "Mastar mânâsına nasıl ulaşılır? Mastariyye en, enne veya mâ vasıtasıyla (beleğanî enneke kâimün; ﴿ve en tesûmû hayrun leküm﴾) ya da onlarsız: muzâfun ileyh cümle (﴿yevme yenfeu's-sâdikîne sıdkuhum﴾ = yevme nef'i sıdkı's-sâdikîn), tesviye hemzesinden sonraki cümle (﴿sevâün aleyhim e-enzertehüm em lem tünzirhüm﴾ = inzâruke ve ademü inzârike) ve tesmau bi'l-Muaydiyyi hayrun min en terâhu = semâuke — bu sonuncusu semâa mahsus.",
         "Taşbaskı niçin «اسم الجر فالعامل» okumuş? Transkripsiyon «ismi'l-harfi'l-âmil»i — âmil harfin, inne'nin ismini — bozmuştur; inne Zeyden kâimün örneği bunu gerektirir; okuyucu öyle basar ve işaretler.",
         "Motor burada neyi OKUR? DabtEngine mâzî şart veya cevaba atfedilen muzâriyi cezm eder, en'den sonraki mâzîye atfedileni nasb eder, fiil cümlesinin fâilini ve isim cümlesinin haberini ref' eder, nahvü'den sonraki hikâye cümlesini kendi cümlesi olarak okur ve Kur'ânî cümlelere kelime kelime i'râbını verir."],
 },
 "plain": {"en": "A past-tense verb never shows a case ending, yet it can sit in a slot that has one: after «that» an accusative slot, after «if» a jussive one — and the present verb joined to it shows the ending it cannot. A whole sentence does the same when it counts as one noun: quoted, reported after «said», or read as «your doing».",
           "tr": "Mâzî fiil asla i'râb göstermez, yine de i'râblı bir yerde durabilir: «en»den sonra nasb, «in»den sonra cezm mahallinde — ve ona bağlanan muzâri onun gösteremediği eki gösterir. Bütün bir cümle de tek bir isim sayıldığında aynısını yapar: aktarılınca, «dedi»den sonra gelince ya da «senin yapman» diye okununca."},
 "explanation": {"en": "The third division of the governed is what by origin is not governed yet may stand where the second division stands. The māḍī: after the maṣdar-making an its place is ruled naṣb, after the jāzim as protasis or apodosis its place is ruled jazm, because that iʿrāb appears in what is joined to it — أَعْجَبَنِي أَنْ ضَرَبْتَ وَتَقْتُلَ، وَإِنْ ضَرَبْتَ وَتَقْتُلْ ضَرَبْتُكَ وَأَقْتُلْ; elsewhere it is not governed. The sentence is verbal (a verb in word or in sense with its doer: ضَرَبَ زَيْدٌ، إِنْ تُكْرِمْنِي أُكْرِمْكَ، هَيْهَاتَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ) or nominal (mubtadaʾ and khabar, or the governing particle's ism and its khabar: زَيْدٌ قَائِمٌ، إِنَّ زَيْدًا قَائِمٌ). If its wording is intended it must have iʿrāb, being in the ruling of a single noun, and it occurs as mubtadaʾ, doer and the rest (زَيْدٌ قَائِمٌ جُمْلَةٌ اسْمِيَّةٌ, that is, this wording); so the content of a saying (﴿وَإِذَا قِيلَ لَهُمْ آمِنُوا﴾); so when a maṣdar's sense is intended by it — through an, anna or mā (بَلَغَنِي أَنَّكَ قَائِمٌ؛ ﴿وَأَنْ تَصُومُوا خَيْرٌ لَكُمْ﴾) or without them: the clause annexed to (﴿يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ﴾ = يَوْمَ نَفْعِ صِدْقِ الصَّادِقِينَ), ﴿سَوَاءٌ عَلَيْهِمْ أَأَنْذَرْتَهُمْ أَمْ لَمْ تُنْذِرْهُمْ﴾ (= إِنْذَارُكَ وَعَدَمُ إِنْذَارِكَ), and تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرٌ مِنْ أَنْ تَرَاهُ (= سَمَاعُكَ), this last confined to what was heard.",
                 "tr": "Ma'mûlün üçüncü kısmı, aslında ma'mûl olmayan fakat ikinci kısmın yerinde bulunabilendir. Mâzî: mastariyye en'den sonra mahalli nasb, câzimden sonra şart veya cezâ olarak mahalli cezm sayılır; çünkü bu i'râb ona atfedilende görünür — a'cebenî en darabte ve taktüle, ve in darabte ve taktül darabtüke ve aktül; başka yerde ma'mûl olmaz. Cümle fiiliyyedir (lafzen veya mânen fiil ile fâili: darabe Zeydün, in tükrimnî ükrimke, heyhâte Zeydün, e-kâimün ez-Zeydâni) ya da ismiyyedir (mübtedâ ile haber ya da âmil harfin ismi ile haberi: Zeydün kâimün, inne Zeyden kâimün). Lafzı kastedilirse müfred isim hükmünde olduğundan i'râbı olması gerekir; mübtedâ, fâil ve diğerleri olarak gelir (Zeydün kâimün cümletün ismiyyetün, yani bu lafız); makûlü'l-kavl de böyledir (﴿ve izâ kîle lehüm âminû﴾); mastar mânâsı kastedilince de — en, enne veya mâ ile (beleğanî enneke kâimün; ﴿ve en tesûmû hayrun leküm﴾) ya da onlarsız: muzâfun ileyh cümle (﴿yevme yenfeu's-sâdikîne sıdkuhum﴾ = yevme nef'i sıdkı's-sâdikîn), ﴿sevâün aleyhim e-enzertehüm em lem tünzirhüm﴾ (= inzâruke ve ademü inzârike) ve tesmau bi'l-Muaydiyyi hayrun min en terâhu (= semâuke); bu sonuncusu semâa mahsustur."},
 "examples": [
  {"ar": "أَعْجَبَنِي أَنْ ضَرَبْتَ وَتَقْتُلَ", "en": "the māḍī's place of naṣb shown on the joined muḍāriʿ", "tr": "mâzînin nasb mahalli ma'tûf muzâride görünür", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "إِنْ ضَرَبْتَ وَتَقْتُلْ ضَرَبْتُكَ وَأَقْتُلْ", "en": "the places of jazm of protasis and apodosis", "tr": "şart ve cevabın cezm mahalleri", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "هَيْهَاتَ زَيْدٌ، أَقَائِمٌ الزَّيْدَانِ", "en": "verbal sentences with the verb in sense", "tr": "mânen fiilli fiil cümleleri", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "زَيْدٌ قَائِمٌ جُمْلَةٌ اسْمِيَّةٌ", "en": "the sentence whose wording is meant, as a mubtada", "tr": "lafzı kastedilen cümle, mübtedâ olarak", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "وَإِذَا قِيلَ لَهُمْ آمِنُوا", "en": "the content of a saying (al-Baqara 13)", "tr": "makûlü'l-kavl (Bakara 13)", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "وَأَنْ تَصُومُوا خَيْرٌ لَكُمْ", "en": "the maṣdar sense through an (al-Baqara 184)", "tr": "en ile mastar mânâsı (Bakara 184)", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ", "en": "the clause annexed to (al-Māʾida 119)", "tr": "muzâfun ileyh cümle (Mâide 119)", "sourceStory": "izhar-al-asrar", "sentence": "s9"},
  {"ar": "تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرٌ مِنْ أَنْ تَرَاهُ", "en": "the maṣdar reading without a particle, confined to what was heard", "tr": "harfsiz mastar te'vili, semâa mahsus", "sourceStory": "izhar-al-asrar", "sentence": "s11"},
 ],
 "commonMistakes": [
  {"wrong": "أَعْجَبَنِي أَنْ ضَرَبْتَ وَتَقْتُلُ", "right": "أَعْجَبَنِي أَنْ ضَرَبْتَ وَتَقْتُلَ", "why": {"en": "the muḍāriʿ joined to a māḍī after an takes the naṣb of the māḍī's place", "tr": "en'den sonraki mâzîye atfedilen muzâri, mâzînin mahallinin nasbını alır"}},
  {"wrong": "إِنْ ضَرَبْتَ وَتَقْتُلُ", "right": "إِنْ ضَرَبْتَ وَتَقْتُلْ", "why": {"en": "joined to the protasis, it takes the jazm of its place", "tr": "şarta atfedilen, mahallinin cezmini alır"}},
  {"wrong": "تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرًا", "right": "تَسْمَعُ بِالْمُعَيْدِيِّ خَيْرٌ", "why": {"en": "the sentence read as a maṣdar is the mubtada; خَيْرٌ is its khabar in rafʿ", "tr": "mastar hükmündeki cümle mübtedâdır; hayrun merfû haberidir"}},
 ],
}
ADD_EN = (" Chapter 19 (print pp. 117-119): the third division of the governed (s1); the māḍī's place after an and after the jāzim, shown on what is joined to it (s2-s3); the sentence, verbal (s4) and nominal (s5) — the transcription's «اسم الجر فالعامل» printed as «اسْمِ الْحَرْفِ الْعَامِلِ» and flagged; the sentence's iʿrāb when its wording is meant (s6), as the content of a saying with al-Baqara 2:13 (s7), as a maṣdar through an / anna / mā with al-Baqara 2:184 (s8) or without them — al-Māʾida 5:119 (s9), al-Baqara 2:6 (s10), the Muʿaydī proverb confined to what was heard (s11). The Qurʾānic lines as the print sets them.")
ADD_TR = (" On dokuzuncu bab (baskı s. 117-119): ma'mûlün üçüncü kısmı (s1); en'den ve câzimden sonra mâzînin mahalli, ma'tûfta görünür (s2-s3); cümle, fiiliyye (s4) ve ismiyye (s5) — transkripsiyonun «اسم الجر فالعامل»ı «اسْمِ الْحَرْفِ الْعَامِلِ» olarak basıldı ve işaretlendi; lafzı kastedilen cümlenin i'râbı (s6), Bakara 2:13 ile makûlü'l-kavl (s7), Bakara 2:184 ile en / enne / mâ vasıtasıyla mastar (s8) ya da onlarsız — Mâide 5:119 (s9), Bakara 2:6 (s10), semâa mahsus Muaydî atasözü (s11). Kur'ânî satırlar baskının verdiği şekliyle.")
write_out(19, S, TITLE, ADD_EN, ADD_TR, "pp. 117-119", GLOSS_ADD, notes=(NOTE,),
          related=((K18, [K]), (AMS, [K]), (MJZ, [K]), (SH, [K]), (QA, [K]), (MH, [K]), (MK, [K])))
report(19, S, GLOSS_ADD, (NOTE,))
