# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 27: the REAL feminine has a male counterpart among the animate (امْرَأَة، نَاقَة), the FORMAL
# has none (غُرْفَة، شَمْس); the broken plural changes its singular's form (رِجَال); the sound masculine plural adds a wāw after a
# ḍamma or a yāʾ after a kasra, and a nūn with fatḥa outside annexation (مُسْلِمُونَ، مُسْلِمِينَ); the sound feminine plural adds alif
# and tāʾ (مُسْلِمَات); the dual adds an alif or a yāʾ after a fatḥa, and a nūn with kasra outside annexation (مُسْلِمَانِ، مُسْلِمَيْنِ);
# every plural but the sound masculine is feminine, for the sense of «the group». The sound masculine plural keeps its governor
# masculine (جَاءَ الْمُسْلِمُونَ، رَجُلٌ قَاعِدٌ نَاصِرُوهُ) and, predicated of its pronoun, makes it a masculine plural (الْمُسْلِمُونَ
# جَاؤُوا أَوْ يَجِيئُونَ أَوْ جَاؤُونَ); the rational broken masculine plural, predicated of its pronoun, wants a feminine singular or
# masculine plural governor (الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا أَوْ جَائِيَةٌ أَوْ جَاؤُونَ); every other plural a feminine singular or feminine
# plural (الْمُسْلِمَاتُ جَاءَتْ أَوْ جِئْنَ أَوْ جَائِيَةٌ أَوْ جَائِيَاتٌ، الْأَشْجَارُ قُطِعَتْ أَوْ قُطِعْنَ أَوْ مَقْطُوعَةٌ أَوْ مَقْطُوعَاتٌ). Print pp. 127–128.
#   python3 author_izhar_ch27.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-jumu-wa-tanith-amiliha"
K25 = "al-fail-al-muzhar-wa-tanith-amilih"; K26 = "al-muannath-wa-alamatuh"
TITLE = {"ar": "الْحَقِيقِيُّ وَاللَّفْظِيُّ، وَالْجُمُوعُ وَتَأْنِيثُ عَامِلِهَا", "en": "The real and the formal feminine; the plurals and the feminine of their governor", "tr": "Hakîkî ve lafzî müennes; cemi'ler ve âmillerinin te'nîsi"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; JMS = "jam-mudhakkar-salim"; JMA = "jam-muannath-salim"; JT = "jam-taksir"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"
IDH = "idha-shartiyya"; NSB = "ism-mansub"; MH = "mahall-al-majrur"; AMS = "an-masdariyya"; F4 = "form-iv-verbs"; F2 = "form-ii-verbs"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def ma_(): return tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber.")
def lahiqa(): return tok("لَحِقَ", "lahiqa", "verb", [K, FL, MAW], "فِعْلٌ مَاضٍ — صِلَةُ مَا.", "«is joined by» — the relative clause.", "«… bitişen» — sıla.")
def akhira(): return tok("آخِرَ", "akhir", "noun", [K, MB, ID], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ، مُضَافٌ.", "«the end of» — the object put first.", "«sonuna» — öne alınmış mef'ûl.")
def mufradihi(): return tok("مُفْرَدِهِ", "mufrad", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its singular»", "«müfredinin»", segments=[seg("مُفْرَدِ", "mufrad", "noun"), pr3msi()])
def maqablaha(): return [tok("مَا", "ma-mawsula", "pron", [K, NF, MAW], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ فِي مَحَلِّ رَفْعٍ.", "«what» — the participle's deputy doer.", "«… olan» — nâib-i fâil."), tok("قَبْلَهَا", "qabla", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةٌ.", "«before it»", "«ondan önce»", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()])]
def fighayr(): return [tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"), tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«dışında»"), tok("الْإِضَافَةِ", "idafa", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«annexation»", "«izâfet»")]
def waamma(): return tok("وَأَمَّا", "amma", "part", [K, AT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»", segments=wa("أَمَّا", "amma", "part"))
def idhausnida(enc): return [tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ınca»"), tok("أُسْنِدَ", "asnada", "verb", [K, NF, F4], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْعَامِلُ.", "«it is predicated» — the governor.", "«isnâd edilince» — âmil."), tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-e»"), tok("ضَمِيرِ" + enc, "damir", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«its pronoun»", "«zamirine»", segments=[seg("ضَمِيرِ", "damir", "noun"), (pr3msi() if enc == "هِ" else pr3fs())])]

# ----------- s1 — real and formal feminine
S.append({"id": "s1", "translation": {"en": "And the real feminine is what has a male counterpart among the animate — as in «a woman» and «a she-camel» — and the formal is the opposite — as in «a room» and «the sun».", "tr": "Hakîkî te'nîs, canlılardan karşısında bir erkeği bulunandır — «kadın», «dişi deve» gibi —; lafzî olan bunun aksidir — «oda», «güneş» gibi."},
 "tokens": [
  tok("وَالتَّأْنِيثُ", "tanith", "noun", [K, AT, MK, MSD], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالتَّأْنِيثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the feminine» — the mubtada.", "«te'nîs» — mübtedâ.", segments=wa("التَّأْنِيثُ", "tanith", "noun")),
  tok("الْحَقِيقِيُّ", "haqiqi", "noun", [K, NA, NSB], "نَعْتٌ مَرْفُوعٌ.", "«real»", "«hakîkî»"),
  ma_(),
  tok("بِإِزَائِهِ", "iza", "noun", [K, HJ, ID, MK, MAW], "الْبَاءُ حَرْفُ جَرٍّ، وَإِزَائِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«opposite it» — the fronted khabar of the relative clause.", "«karşısında» — sılanın öne alınmış haberi.", segments=[seg("بِ", "bi", "prep"), seg("إِزَائِ", "iza", "noun"), pr3msi()]),
  tok("ذَكَرٌ", "dhakar", "noun", [K, MK, MAW], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a male» — the mubtada put after.", "«bir erkek» — sonraya bırakılmış mübtedâ."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("الْحَيَوَانِ", "hayawan", "noun", [K, HJ, NA], "مَجْرُورٌ بِمِنْ — صِفَةٌ لِذَكَرٍ.", "«the animate» — a naʿt of «male».", "«canlı» — «erkek»in sıfatı.", punct="،"),
  nahw(),
  tok("امْرَأَةٍ", "imraa", "noun", [K, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a woman»", "«kadın»"),
  tok("وَنَاقَةٍ", "naqa", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَنَاقَةٍ مَعْطُوفٌ مَجْرُورٌ.", "«and a she-camel»", "«ve dişi deve»", punct="،", segments=wa("نَاقَةٍ", "naqa", "noun")),
  tok("وَاللَّفْظِيُّ", "lafzi", "noun", [K, AT, MK, NSB], "الْوَاوُ عَاطِفَةٌ، وَاللَّفْظِيُّ مُبْتَدَأٌ مَرْفُوعٌ — التَّأْنِيثُ اللَّفْظِيُّ.", "«and the formal» — the formal feminine.", "«lafzî» — lafzî te'nîs.", segments=wa("اللَّفْظِيُّ", "lafzi", "noun")),
  tok("بِخِلَافِهِ", "khilaf", "noun", [K, HJ, ID, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ: مَا لَيْسَ بِإِزَائِهِ ذَكَرٌ.", "«is the opposite» — the khabar: no male counterpart.", "«bunun aksidir» — haber: karşısında erkeği yok.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun"), pr3msi()]),
  nahw(),
  tok("غُرْفَةٍ", "ghurfa", "noun", [K, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a room»", "«oda»"),
  tok("وَشَمْسٍ", "shams", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَشَمْسٍ مَعْطُوفٌ مَجْرُورٌ.", "«and the sun»", "«ve güneş»", punct=".", segments=wa("شَمْسٍ", "shams", "noun")),
 ]})
# ----------- s2 — the broken plural
S.append({"id": "s2", "translation": {"en": "And the broken plural is what has changed the form of its singular — as in «men»;", "tr": "Mükesser cemi', müfredinin sîgası değişmiş olandır — «adamlar» gibi;"},
 "tokens": [
  tok("وَالْجَمْعُ", "jam", "noun", [K, AT, MK, JT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْجَمْعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the plural» — the mubtada.", "«cemi'» — mübtedâ.", segments=wa("الْجَمْعُ", "jam", "noun")),
  tok("الْمُكَسَّرُ", "mukassar", "noun", [K, NA, JT, IMF], "نَعْتٌ مَرْفُوعٌ.", "«broken»", "«mükesser»"),
  ma_(),
  tok("تَغَيَّرَ", "taghayyara", "verb", [K, FL, MAW, "form-v-verbs"], "فِعْلٌ مَاضٍ — صِلَةُ مَا.", "«has changed» — the relative clause.", "«değişen» — sıla."),
  tok("صِيغَةُ", "sigha", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the form of» — the doer.", "«sîgası» — fâil."),
  mufradihi(),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«as in»", "«… gibi»", punct=":"),
  tok("رِجَالٍ", "rijal", "noun", [K, ID, JT], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَغَيَّرَ عَنْ رَجُلٍ.", "«men» — changed from رَجُل.", "«adamlar» — racül'den değişmiş.", punct="؛"),
 ]})
# ----------- s3 — the sound masculine plural
S.append({"id": "s3", "translation": {"en": "and the sound masculine plural is what has had joined to the end of its singular a wāw with a ḍamma before it, or a yāʾ with a kasra before it, and a nūn with a fatḥa outside annexation — for in annexation the nūn is dropped — as in «Muslims» (muslimūna, muslimīna);", "tr": "cem-i müzekker sâlim, müfredinin sonuna öncesi mazmûm bir vâv ya da öncesi meksûr bir yâ ve izâfet dışında meftûh bir nûn bitişmiş olandır — izâfette nûn düşer —: «müslümanlar» (müslimûne, müslimîne) gibi;"},
 "tokens": [
  tok("وَجَمْعُ", "jam", "noun", [K, AT, MK, ID, JMS], "الْوَاوُ عَاطِفَةٌ، وَجَمْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the plural of»", "«ve cem'i»", segments=wa("جَمْعُ", "jam", "noun")),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekkerin»"),
  tok("السَّالِمُ", "salim", "noun", [K, NA, JMS, IFA], "نَعْتٌ لِجَمْعُ مَرْفُوعٌ.", "«sound»", "«sâlim»"),
  ma_(),
  lahiqa(),
  akhira(),
  mufradihi(),
  tok("وَاوٌ", "waw-letter", "noun", [K, FL], "فَاعِلُ لَحِقَ مَرْفُوعٌ.", "«a wāw» — the doer of «joined».", "«bir vâv» — lahika'nın fâili."),
  tok("مَضْمُومٌ", "madmum", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ رَافِعٌ لِنَائِبِ فَاعِلٍ.", "«with a ḍamma on» — a participle raising its deputy.", "«zammeli» — nâib ref' eden ism-i mef'ûl."),
  *maqablaha(),
  aw(),
  tok("يَاءٌ", "ya-letter", "noun", [K, AT, FL], "مَعْطُوفٌ عَلَى وَاوٌ مَرْفُوعٌ.", "«a yāʾ»", "«bir yâ»"),
  tok("مَكْسُورٌ", "maksur", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«with a kasra on»", "«kesreli»"),
  *maqablaha(),
  tok("وَنُونٌ", "nun-letter", "noun", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَنُونٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a nūn»", "«ve bir nûn»", segments=wa("نُونٌ", "nun-letter", "noun")),
  tok("مَفْتُوحَةٌ", "maftuh", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«with a fatḥa»", "«fethalı»"),
  *fighayr(),
  tok("فَإِنَّ", "inna", "part", [K, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for»", "«çünkü»", segments=fa("إِنَّ", "inna", "part")),
  tok("النُّونَ", "nun-letter", "noun", [K, IN], "اسْمُ إِنَّ مَنْصُوبٌ.", "«the nūn» — inna's ism.", "«nûn» — inne'nin ismi."),
  tok("تُحْذَفُ", "hadhafa", "verb", [K, IN, NF, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«is dropped» — inna's khabar.", "«düşer» — inne'nin haberi."),
  tok("فِيهَا", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — فِي الْإِضَافَةِ.", "«in it» — in annexation.", "«onda» — izâfette.", punct="،", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  nahw(),
  tok("مُسْلِمُونَ", "muslim", "noun", [K, JMS, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ — بِالْوَاوِ وَالنُّونِ.", "«Muslims» — with the wāw.", "«müslimûne» — vâv ile."),
  tok("وَمُسْلِمِينَ", "muslim", "noun", [K, AT, JMS], "الْوَاوُ عَاطِفَةٌ، وَمُسْلِمِينَ مَعْطُوفٌ — بِالْيَاءِ وَالنُّونِ.", "«and Muslims» — with the yāʾ.", "«ve müslimîne» — yâ ile.", punct="؛", segments=wa("مُسْلِمِينَ", "muslim", "noun")),
 ]})
# ----------- s4 — the sound feminine plural
S.append({"id": "s4", "translation": {"en": "and the sound feminine plural is what has had joined to the end of its singular an alif and a tāʾ — as in «Muslim women»;", "tr": "cem-i müennes sâlim, müfredinin sonuna elif ve tâ bitişmiş olandır — «müslüman kadınlar» gibi;"},
 "tokens": [
  tok("وَجَمْعُ", "jam", "noun", [K, AT, MK, ID, JMA], "الْوَاوُ عَاطِفَةٌ، وَجَمْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the plural of»", "«ve cem'i»", segments=wa("جَمْعُ", "jam", "noun")),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, ID, JMA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine»", "«müennesin»"),
  tok("السَّالِمُ", "salim", "noun", [K, NA, JMA, IFA], "نَعْتٌ لِجَمْعُ مَرْفُوعٌ.", "«sound»", "«sâlim»"),
  ma_(),
  lahiqa(),
  akhira(),
  mufradihi(),
  tok("أَلِفٌ", "alif-letter", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«an alif»", "«bir elif»"),
  tok("وَتَاءٌ", "ta-letter", "noun", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَتَاءٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a tāʾ»", "«ve bir tâ»", punct="،", segments=wa("تَاءٌ", "ta-letter", "noun")),
  nahw(),
  tok("مُسْلِمَاتٍ", "muslima", "noun", [K, JMA, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Muslim women»", "«müslüman kadınlar»", punct="؛"),
 ]})
# ----------- s5 — the dual
S.append({"id": "s5", "translation": {"en": "and the dual is what has had joined to the end of its singular an alif, or a yāʾ with a fatḥa before it, and a nūn with a kasra outside annexation — and in it the nūn is dropped — as in «two Muslims» (muslimāni, muslimayni).", "tr": "tesniye, müfredinin sonuna bir elif ya da öncesi meftûh bir yâ ve izâfet dışında meksûr bir nûn bitişmiş olandır — izâfette nûn düşer —: «iki müslüman» (müslimâni, müslimeyni) gibi."},
 "tokens": [
  tok("وَالتَّثْنِيَةُ", "tathniya", "noun", [K, AT, MK, MTH], "الْوَاوُ عَاطِفَةٌ، وَالتَّثْنِيَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the dual»", "«ve tesniye»", segments=wa("التَّثْنِيَةُ", "tathniya", "noun")),
  ma_(),
  lahiqa(),
  akhira(),
  mufradihi(),
  tok("أَلِفٌ", "alif-letter", "noun", [K, FL, MTH], "فَاعِلٌ مَرْفُوعٌ.", "«an alif»", "«bir elif»"),
  aw(),
  tok("يَاءٌ", "ya-letter", "noun", [K, AT, FL, MTH], "مَعْطُوفٌ مَرْفُوعٌ.", "«a yāʾ»", "«bir yâ»"),
  tok("مَفْتُوحٌ", "maftuh", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«with a fatḥa on»", "«fethalı»"),
  *maqablaha(),
  tok("وَنُونٌ", "nun-letter", "noun", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَنُونٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a nūn»", "«ve bir nûn»", segments=wa("نُونٌ", "nun-letter", "noun")),
  tok("مَكْسُورَةٌ", "maksur", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«with a kasra»", "«kesreli»"),
  *fighayr(),
  tok("وَفِيهَا", "fi", "prep", [K, AT, HJ], "الْوَاوُ لِلْحَالِ، وَفِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«and in it»", "«ve onda»", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), pr3fs()]),
  tok("تُحْذَفُ", "hadhafa", "verb", [K, NF, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — النُّونُ.", "«it is dropped» — the nūn.", "«düşer» — nûn.", punct="،"),
  nahw(),
  tok("مُسْلِمَانِ", "muslim", "noun", [K, MTH, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ — بِالْأَلِفِ وَالنُّونِ.", "«two Muslims» — with the alif.", "«müslimâni» — elif ile."),
  tok("وَمُسْلِمَيْنِ", "muslim", "noun", [K, AT, MTH], "الْوَاوُ عَاطِفَةٌ، وَمُسْلِمَيْنِ مَعْطُوفٌ — بِالْيَاءِ وَالنُّونِ.", "«and two Muslims» — with the yāʾ.", "«ve müslimeyni» — yâ ile.", punct=".", segments=wa("مُسْلِمَيْنِ", "muslim", "noun")),
 ]})
# ----------- s6 — every other plural feminine
S.append({"id": "s6", "translation": {"en": "And every plural other than the sound masculine plural is feminine, for its being in the sense of «the group».", "tr": "Cem-i müzekker sâlim dışındaki her cemi' müennestir; çünkü «cemâat» mânâsındadır."},
 "tokens": [
  tok("وَكُلُّ", "kull", "noun", [K, AT, MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and every» — the mubtada.", "«ve her» — mübtedâ.", segments=wa("كُلُّ", "kull", "noun")),
  tok("جَمْعٍ", "jam", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«plural»", "«cemi'»"),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ لِجَمْعٍ مَجْرُورٌ، مُضَافٌ.", "«other than»", "«dışındaki»"),
  tok("جَمْعِ", "jam", "noun", [K, ID, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the plural of»", "«cem'i»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekkerin»"),
  tok("السَّالِمِ", "salim", "noun", [K, NA, JMS], "نَعْتٌ مَجْرُورٌ.", "«sound»", "«sâlim»"),
  tok("مُؤَنَّثٌ", "muannath", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«is feminine» — the khabar.", "«müennestir» — haber."),
  tok("لِكَوْنِهِ", "kawn", "noun", [K, HJ, ID, MSD], "اللَّامُ لِلتَّعْلِيلِ، وَكَوْنِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ كَانَ.", "«for its being»", "«… olduğu için»", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3msi()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — خَبَرُ كَوْنِ.", "«in the sense of» — the khabar of «being».", "«mânâsında» — kevn'in haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الْجَمَاعَةِ", "jamaa", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the group»", "«cemâat»", punct="."),
 ]})
# ----------- s7 — the sound masculine plural's governor
S.append({"id": "s7", "translation": {"en": "As for the sound masculine plural, its governor must be masculine — so you say «the Muslims came» or «a man whose helpers are seated» — and when the governor is predicated of its pronoun it must be a masculine plural — as in «the Muslims came, or come, or are coming».", "tr": "Cem-i müzekker sâlime gelince, âmilinin müzekker olması vâcibdir — «müslümanlar geldi», «yardımcıları oturan bir adam» dersin —; âmil onun zamirine isnâd edilince cemi' müzekker olması vâcibdir — «müslümanlar geldiler, ya gelirler, ya gelmektedirler» gibi."},
 "tokens": [
  waamma(),
  tok("جَمْعُ", "jam", "noun", [K, MK, ID, JMS], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the plural of» — the mubtada.", "«cem'i» — mübtedâ."),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekkerin»"),
  tok("السَّالِمُ", "salim", "noun", [K, NA, JMS], "نَعْتٌ مَرْفُوعٌ.", "«sound»", "«sâlim»"),
  tok("فَيَجِبُ", "wajaba", "verb", [K, MK, FL, MR, "mithal-verbs"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَيَجِبُ فِعْلٌ مُضَارِعٌ — وَالْجُمْلَةُ خَبَرٌ.", "«it is necessary» — the khabar after ammā's fāʾ.", "«vâcibdir» — emmâ'nın fâsından sonra haber.", segments=fa("يَجِبُ", "wajaba", "verb")),
  tok("تَذْكِيرُ", "tadhkir", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«making masculine» — the doer.", "«tezkîri» — fâil."),
  tok("عَامِلِهِ", "amil-governor", "noun", [K, ID, AQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", punct="،", segments=[seg("عَامِلِ", "amil-governor", "noun"), pr3msi()]),
  tok("فَتَقُولُ", "qala", "verb", [K, AT, FL, HV, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَتَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«so you say»", "«dersin»", punct=":", segments=fa("تَقُولُ", "qala", "verb")),
  tok("جَاءَ", "jaa", "verb", [K, FL, HV, MB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُذَكَّرٌ.", "«came» — masculine.", "«geldi» — müzekker."),
  tok("الْمُسْلِمُونَ", "muslim", "noun", [K, FL, JMS], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ.", "«the Muslims» — the doer.", "«müslümanlar» — fâil.", punct="،"),
  aw(),
  tok("رَجُلٌ", "rajul", "noun", [K, AT, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ — أَوْ مَوْصُوفٌ.", "«a man»", "«bir adam»"),
  tok("قَاعِدٌ", "qaid", "noun", [K, NA, IFA, FL], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مُذَكَّرٌ رَافِعٌ لِلظَّاهِرِ.", "«seated» — a masculine participle raising the apparent noun.", "«oturan» — açık ismi ref' eden müzekker ism-i fâil."),
  tok("نَاصِرُوهُ", "nasir-helper", "noun", [K, FL, JMS, ID], "فَاعِلُ قَاعِدٍ مَرْفُوعٌ بِالْوَاوِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his helpers» — the participle's doer, the nūn dropped for the annexation.", "«yardımcıları» — ism-i fâilin fâili, izâfetle nûnu düşmüş.", punct="،", segments=[seg("نَاصِرُو", "nasir-helper", "noun"), pr3ms()]),
  tok("وَإِذَا", "idha", "part", [K, AT, IDH, MF], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -ınca»", segments=wa("إِذَا", "idha", "part")),
  *idhausnida("هِ")[1:],
  tok("يَجِبُ", "wajaba", "verb", [K, FL, MR, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — جَوَابُ إِذَا.", "«it is necessary»", "«vâcib olur»"),
  tok("كَوْنُهُ", "kawn", "noun", [K, FL, ID, MSD, KN], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ كَانَ: الْعَامِلُ.", "«its being» — the doer; the governor is kāna's ism.", "«olması» — fâil; âmil kevn'in ismi.", segments=[seg("كَوْنُ", "kawn", "noun"), pr3ms()]),
  tok("جَمْعًا", "jam", "noun", [K, KN], "خَبَرُ كَوْنِ مَنْصُوبٌ.", "«a plural» — the khabar of «being».", "«cemi'» — kevn'in haberi."),
  tok("مُذَكَّرًا", "mudhakkar", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«masculine»", "«müzekker»", punct="،"),
  nahw(),
  tok("الْمُسْلِمُونَ", "muslim", "noun", [K, MK, JMS], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ.", "«the Muslims» — the mubtada.", "«müslümanlar» — mübtedâ."),
  tok("جَاؤُوا", "jaa", "verb", [K, MK, FL, HV, MH], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرٌ.", "«came» — the wāw the doer.", "«geldiler» — vâv fâil."),
  aw(),
  tok("يَجِيئُونَ", "jaa", "verb", [K, AT, FL, HV, MR, MH], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«come»", "«gelirler»"),
  aw(),
  tok("جَاؤُونَ", "jai-coming", "noun", [K, AT, MK, JMS, IFA], "مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — اسْمُ فَاعِلٍ جَمْعٌ مُذَكَّرٌ سَالِمٌ خَبَرٌ.", "«are coming» — the participle's sound plural as khabar.", "«gelmektedirler» — ism-i fâilin sâlim cem'i haber.", punct="."),
 ]})
# ----------- s8 — the rational broken masculine plural
S.append({"id": "s8", "translation": {"en": "As for the rational broken masculine plural, when the governor is predicated of its pronoun it must be a feminine singular or a masculine plural — as in «the men came» (jāʾat, jāʾū, jāʾiyatun, jāʾūna);", "tr": "Âkıl mükesser müzekker cemi'e gelince, âmil onun zamirine isnâd edilince müfred müennes ya da cemi' müzekker olması vâcibdir — «adamlar geldi» (câet, câû, câiyetün, câûne) gibi;"},
 "tokens": [
  waamma(),
  tok("جَمْعُ", "jam", "noun", [K, MK, ID, JT], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the plural of»", "«cem'i»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekkerin»"),
  tok("الْمُكَسَّرُ", "mukassar", "noun", [K, NA, JT, IMF], "نَعْتٌ مَرْفُوعٌ.", "«broken»", "«mükesser»"),
  tok("الْعَاقِلُ", "aqil", "noun", [K, NA, IFA], "نَعْتٌ ثَانٍ مَرْفُوعٌ.", "«rational»", "«âkıl»"),
  *idhausnida("هِ"),
  tok("فَيَجِبُ", "wajaba", "verb", [K, MK, FL, MR, "mithal-verbs"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَيَجِبُ فِعْلٌ مُضَارِعٌ — خَبَرٌ.", "«it is necessary»", "«vâcibdir»", segments=fa("يَجِبُ", "wajaba", "verb")),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ فَاعِلُ يَجِبُ.", "«be» — the clause the doer of «is necessary».", "«olması» — masdar yecibu'nun fâili."),
  tok("عَامِلُهُ", "amil-governor", "noun", [K, KN, ID, AQ], "اسْمُ يَكُونَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor» — kāna's ism.", "«âmili» — yekûne'nin ismi.", segments=[seg("عَامِلُ", "amil-governor", "noun"), pr3ms()]),
  tok("مُفْرَدًا", "mufrad", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«singular»", "«müfred»"),
  tok("مُؤَنَّثًا", "muannath", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«feminine»", "«müennes»"),
  aw(),
  tok("جَمْعًا", "jam", "noun", [K, AT, KN], "مَعْطُوفٌ عَلَى مُفْرَدًا مَنْصُوبٌ.", "«a plural»", "«cemi'»"),
  tok("مُذَكَّرًا", "mudhakkar", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«masculine»", "«müzekker»", punct="،"),
  nahw(),
  tok("الرِّجَالُ", "rijal", "noun", [K, MK, JT], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«the men» — the mubtada.", "«adamlar» — mübtedâ."),
  tok("جَاءَتْ", "jaa", "verb", [K, MK, FL, HV], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — خَبَرٌ.", "«came (f. sg.)»", "«geldi (müfred müennes)»"),
  aw(),
  tok("جَاؤُوا", "jaa", "verb", [K, AT, FL, HV, MH], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«came (m. pl.)»", "«geldiler»"),
  aw(),
  tok("جَائِيَةٌ", "jai-coming", "noun", [K, AT, MK, IFA], "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مُفْرَدٌ مُؤَنَّثٌ.", "«is coming (f. sg.)»", "«gelmektedir (müfred müennes)»"),
  aw(),
  tok("جَاؤُونَ", "jai-coming", "noun", [K, AT, MK, JMS, IFA], "مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — اسْمُ فَاعِلٍ جَمْعٌ مُذَكَّرٌ.", "«are coming (m. pl.)»", "«gelmektedirler»", punct="؛"),
 ]})
# ----------- s9 — the other plurals
S.append({"id": "s9", "translation": {"en": "and the other plurals, when the governor is predicated of their pronoun, its governor must be a feminine singular or a feminine plural — as in «the Muslim women came» (jāʾat, jiʾna, jāʾiyatun, jāʾiyātun) and «the trees were cut» (quṭiʿat, quṭiʿna, maqṭūʿatun, maqṭūʿātun).", "tr": "diğer cemi'lere gelince, âmil onların zamirine isnâd edilince müfred müennes ya da cemi' müennes olması vâcibdir — «müslüman kadınlar geldi» (câet, ci'ne, câiyetün, câiyâtün) ve «ağaçlar kesildi» (kutıat, kutı'ne, maktûatün, maktûâtün) gibi."},
 "tokens": [
  tok("وَغَيْرُهَا", "ghayr", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and the others» — the mubtada.", "«ve diğerleri» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("غَيْرُ", "ghayr", "noun"), pr3fs()]),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of»", "«-den»"),
  tok("الْجُمُوعِ", "jumu", "noun", [K, HJ, JT], "مَجْرُورٌ بِمِنْ — جَمْعُ جَمْعٍ.", "«the plurals» — a plural of «plural».", "«cemi'ler» — cemi'in cem'i."),
  *idhausnida("هَا"),
  tok("يَجِبُ", "wajaba", "verb", [K, MK, FL, MR, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — خَبَرُ غَيْرُهَا.", "«it is necessary» — the khabar.", "«vâcib olur» — haber."),
  tok("كَوْنُ", "kawn", "noun", [K, FL, ID, MSD, KN], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the being of»", "«olması»"),
  tok("عَامِلِهَا", "amil-governor", "noun", [K, ID, AQ, KN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — اسْمُ كَوْنِ.", "«their governor»", "«âmillerinin»", segments=[seg("عَامِلِ", "amil-governor", "noun"), pr3fs()]),
  tok("مُفْرَدًا", "mufrad", "noun", [K, KN], "خَبَرُ كَوْنِ مَنْصُوبٌ.", "«singular»", "«müfred»"),
  tok("مُؤَنَّثًا", "muannath", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«feminine»", "«müennes»"),
  aw(),
  tok("جَمْعًا", "jam", "noun", [K, AT, KN], "مَعْطُوفٌ مَنْصُوبٌ.", "«a plural»", "«cemi'»"),
  tok("مُؤَنَّثًا", "muannath", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«feminine»", "«müennes»", punct="،"),
  nahw(),
  tok("الْمُسْلِمَاتُ", "muslima", "noun", [K, MK, JMA], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«the Muslim women» — the mubtada.", "«müslüman kadınlar» — mübtedâ."),
  tok("جَاءَتْ", "jaa", "verb", [K, MK, FL, HV], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — خَبَرٌ.", "«came (f. sg.)»", "«geldi»"),
  aw(),
  tok("جِئْنَ", "jaa", "verb", [K, AT, FL, HV, MH], "فِعْلٌ مَاضٍ، وَالنُّونُ ضَمِيرُ النِّسْوَةِ فَاعِلٌ.", "«came (f. pl.)» — the women's nūn.", "«geldiler (dişi)» — nisve nûnu."),
  aw(),
  tok("جَائِيَةٌ", "jai-coming", "noun", [K, AT, MK, IFA], "مَعْطُوفٌ مَرْفُوعٌ — مُفْرَدٌ مُؤَنَّثٌ.", "«is coming (f. sg.)»", "«gelmektedir»"),
  aw(),
  tok("جَائِيَاتٌ", "jai-coming", "noun", [K, AT, MK, JMA, IFA], "مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«are coming (f. pl.)»", "«gelmektedirler (dişi)»", punct="،"),
  tok("وَالْأَشْجَارُ", "shajara", "noun", [K, AT, MK, JT], "الْوَاوُ عَاطِفَةٌ، وَالْأَشْجَارُ مُبْتَدَأٌ مَرْفُوعٌ — جَمْعُ تَكْسِيرٍ لِغَيْرِ الْعَاقِلِ.", "«and the trees» — a broken plural of the non-rational.", "«ve ağaçlar» — gayr-ı âkılın mükesser cem'i.", segments=wa("الْأَشْجَارُ", "shajara", "noun")),
  tok("قُطِعَتْ", "qataa", "verb", [K, MK, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ — خَبَرٌ.", "«were cut (f. sg.)»", "«kesildi»"),
  aw(),
  tok("قُطِعْنَ", "qataa", "verb", [K, AT, NF, MH], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالنُّونُ نَائِبُ فَاعِلٍ.", "«were cut (f. pl.)»", "«kesildiler»"),
  aw(),
  tok("مَقْطُوعَةٌ", "maqtu", "noun", [K, AT, MK, IMF], "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مُفْرَدٌ مُؤَنَّثٌ.", "«are cut (f. sg.)»", "«kesilmiştir»"),
  aw(),
  tok("مَقْطُوعَاتٌ", "maqtu", "noun", [K, AT, MK, JMA, IMF], "مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«are cut (f. pl.)»", "«kesilmişlerdir»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "iza": G("iza", "إِزَاء", "أ ز ي", "noun", "opposite, facing — بِإِزَائِهِ: as its counterpart", "karşı — bi-izâihî: karşısında", 3),
 "ghurfa": G("ghurfa", "غُرْفَة", "غ ر ف", "noun", "a room, an upper chamber", "oda", 2, plural="غُرَف"),
 "madmum": G("madmum", "مَضْمُوم", "ض م م", "noun", "carrying a ḍamma (ism mafʿūl of ضَمَّ)", "zammeli (damme'nin ism-i mef'ûlü)", 3),
 "hadhafa": G("hadhafa", "حَذَفَ", "ح ذ ف", "verb", "to drop, to elide", "hazfetmek, düşürmek", 3),
 "jai-coming": G("jai-coming", "جَائِي", "ج ي ء", "noun", "coming (ism fāʿil of جَاءَ) — جَائِيَة، جَاؤُونَ، جَائِيَات", "gelen (câe'nin ism-i fâili)", 3),
 "jumu": G("jumu", "جُمُوع", "ج م ع", "noun", "plurals — the plural of جَمْع", "cemi'ler — cem'in cem'i", 3),
 "maqtu": G("maqtu", "مَقْطُوع", "ق ط ع", "noun", "cut (ism mafʿūl of قَطَعَ)", "kesilmiş (kataa'nın ism-i mef'ûlü)", 2),
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
print("izhar ch27 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("lahiqa", "taghayyara", "hadhafa", "qataa", "jaa", "wajaba", "qala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُؤَنَّثُ الْحَقِيقِيُّ وَاللَّفْظِيُّ، وَالْجُمُوعُ وَالتَّثْنِيَةُ وَعَامِلُ الْجَمْعِ", "en": "The real and formal feminine; the plurals, the dual, and the plural's governor", "tr": "Hakîkî ve lafzî müennes; cemi'ler, tesniye ve cem'in âmili"},
 "level": 4, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الجموع وتأنيث عاملها", "الكافية لابن الحاجب — المثنى والمجموع", "شرح قطر الندى لابن هشام — الفاعل جمعا"],
 "amil": "the real feminine has a male counterpart among the animate (امْرَأَة، نَاقَة), the formal none (غُرْفَة، شَمْس); the broken plural changes its singular's form (رِجَال), the sound masculine plural adds wāw/yāʾ and a nūn with fatḥa that annexation drops (مُسْلِمُونَ، مُسْلِمِينَ), the sound feminine plural alif and tāʾ (مُسْلِمَات), the dual alif/yāʾ and a nūn with kasra that annexation drops (مُسْلِمَانِ، مُسْلِمَيْنِ); every plural but the sound masculine is feminine; the sound masculine plural keeps its governor masculine and, as a pronoun, a masculine plural (جَاءَ الْمُسْلِمُونَ، الْمُسْلِمُونَ جَاؤُوا); the rational broken plural's pronoun wants a feminine singular or masculine plural (الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا); the other plurals' pronoun a feminine singular or feminine plural (الْمُسْلِمَاتُ جَاءَتْ أَوْ جِئْنَ، الْأَشْجَارُ قُطِعَتْ أَوْ قُطِعْنَ)",
 "question": {
  "en": ["What is the real feminine, and the formal? The real has a male counterpart among the animate (امْرَأَة، نَاقَة); the formal has none (غُرْفَة، شَمْس).",
         "What is the broken plural? One whose singular's form has changed: رِجَال from رَجُل.",
         "What is the sound masculine plural? The singular's end joined by a wāw after a ḍamma or a yāʾ after a kasra, plus a nūn with a fatḥa — dropped in annexation: مُسْلِمُونَ، مُسْلِمِينَ، نَاصِرُوهُ.",
         "The sound feminine plural and the dual? Alif and tāʾ (مُسْلِمَات); an alif or a yāʾ after a fatḥa plus a nūn with a kasra, dropped in annexation (مُسْلِمَانِ، مُسْلِمَيْنِ).",
         "Why is every other plural feminine? For the sense of «the group» (جَمَاعَة), which is feminine.",
         "What governor does each plural take? The sound masculine plural a masculine one — جَاءَ الْمُسْلِمُونَ، رَجُلٌ قَاعِدٌ نَاصِرُوهُ — and, predicated of its pronoun, a masculine plural (الْمُسْلِمُونَ جَاؤُوا أَوْ يَجِيئُونَ أَوْ جَاؤُونَ); the rational broken plural's pronoun a feminine singular or masculine plural (الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا أَوْ جَائِيَةٌ أَوْ جَاؤُونَ); every other plural's pronoun a feminine singular or feminine plural (الْمُسْلِمَاتُ جَاءَتْ أَوْ جِئْنَ، الْأَشْجَارُ قُطِعَتْ أَوْ قُطِعْنَ).",
         "What does the engine READ here? The DabtEngine writes the sound plurals and duals by their wāw, yāʾ and alif, drops the nūn before an annexed pronoun (نَاصِرُوهُ), reads the paused participles after أَوْ as alternative khabars of the plural mubtadaʾ, and the women's nūn as the doer of جِئْنَ and قُطِعْنَ."],
  "tr": ["Hakîkî ve lafzî müennes nedir? Hakîkî olanın canlılardan karşısında erkeği vardır (imrae, nâka); lafzî olanın yoktur (gurfe, şems).",
         "Mükesser cemi' nedir? Müfredinin sîgası değişmiş olan: racül'den ricâl.",
         "Cem-i müzekker sâlim nedir? Müfredinin sonuna öncesi mazmûm vâv ya da öncesi meksûr yâ ile meftûh nûn bitişen — izâfette nûn düşer: müslimûne, müslimîne, nâsırûhu.",
         "Cem-i müennes sâlim ve tesniye? Elif ve tâ (müslimât); öncesi meftûh elif ya da yâ ile meksûr nûn, izâfette düşer (müslimâni, müslimeyni).",
         "Diğer her cemi' niçin müennestir? «Cemâat» mânâsında olduğu için; cemâat müennestir.",
         "Her cemi' hangi âmili alır? Cem-i müzekker sâlim müzekker âmil — câe'l-müslimûne, racülün kâidün nâsırûhu — ve zamirine isnâdda cemi' müzekker (el-müslimûne câû ev yecîûne ev câûne); âkıl mükesser cemi'in zamiri müfred müennes ya da cemi' müzekker (er-ricâlü câet ev câû ev câiyetün ev câûne); diğer cemi'lerin zamiri müfred müennes ya da cemi' müennes (el-müslimâtü câet ev ci'ne, el-eşcâru kutıat ev kutı'ne).",
         "Motor burada neyi OKUR? DabtEngine sâlim cemi'leri ve tesniyeleri vâv, yâ ve elifleriyle yazar, muzâf zamirden önce nûnu düşürür (nâsırûhu), ev'den sonraki ism-i fâilleri cemi' mübtedânın alternatif haberleri okur ve nisve nûnunu ci'ne ve kutı'ne'nin fâili sayar."],
 },
 "plain": {"en": "A feminine noun is «real» when a male exists for it (woman, she-camel) and «formal» when none does (room, sun). Plurals are broken, sound masculine or sound feminine. Only the sound masculine plural counts as masculine; every other plural is a feminine group: «the trees were cut» may take a singular verb.",
           "tr": "Müennes isim, karşısında erkeği varsa «hakîkî» (kadın, dişi deve), yoksa «lafzî»dir (oda, güneş). Cemi'ler mükesser, müzekker sâlim ve müennes sâlimdir; bir de tesniye vardır. Yalnız müzekker sâlim cemi' müzekker sayılır; diğer her cemi' müennes bir topluluktur; bu yüzden «ağaçlar kesildi» müfred müennes fiil alabilir."},
 "explanation": {"en": "The real feminine is what has a male counterpart among the animate (امْرَأَة، نَاقَة), the formal is its opposite (غُرْفَة، شَمْس). The broken plural changes the form of its singular (رِجَال); the sound masculine plural joins to its singular's end a wāw after a ḍamma or a yāʾ after a kasra and a nūn with fatḥa outside annexation, in which the nūn drops (مُسْلِمُونَ، مُسْلِمِينَ); the sound feminine plural an alif and a tāʾ (مُسْلِمَات); the dual an alif or a yāʾ after a fatḥa and a nūn with kasra outside annexation (مُسْلِمَانِ، مُسْلِمَيْنِ). Every plural but the sound masculine is feminine, for the sense of the group. The sound masculine plural's governor must be masculine (جَاءَ الْمُسْلِمُونَ، رَجُلٌ قَاعِدٌ نَاصِرُوهُ) and, predicated of its pronoun, a masculine plural (الْمُسْلِمُونَ جَاؤُوا أَوْ يَجِيئُونَ أَوْ جَاؤُونَ); the rational broken masculine plural's pronoun wants a feminine singular or masculine plural governor (الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا أَوْ جَائِيَةٌ أَوْ جَاؤُونَ); the other plurals' pronoun a feminine singular or feminine plural (الْمُسْلِمَاتُ جَاءَتْ أَوْ جِئْنَ أَوْ جَائِيَةٌ أَوْ جَائِيَاتٌ، الْأَشْجَارُ قُطِعَتْ أَوْ قُطِعْنَ أَوْ مَقْطُوعَةٌ أَوْ مَقْطُوعَاتٌ).",
                 "tr": "Hakîkî müennes canlılardan karşısında erkeği olan (imrae, nâka), lafzî bunun aksidir (gurfe, şems). Mükesser cemi' müfredinin sîgasını değiştirir (ricâl); cem-i müzekker sâlim müfredinin sonuna öncesi mazmûm vâv ya da öncesi meksûr yâ ve izâfet dışında meftûh nûn ekler, izâfette nûn düşer (müslimûne, müslimîne); cem-i müennes sâlim elif ve tâ (müslimât); tesniye öncesi meftûh elif ya da yâ ve izâfet dışında meksûr nûn (müslimâni, müslimeyni). Müzekker sâlim dışındaki her cemi' cemâat mânâsıyla müennestir. Cem-i müzekker sâlimin âmili müzekker olmalı (câe'l-müslimûne, racülün kâidün nâsırûhu), zamirine isnâdda cemi' müzekker (el-müslimûne câû ev yecîûne ev câûne); âkıl mükesser müzekker cemi'in zamiri müfred müennes ya da cemi' müzekker âmil ister (er-ricâlü câet ev câû ev câiyetün ev câûne); diğer cemi'lerin zamiri müfred müennes ya da cemi' müennes (el-müslimâtü câet ev ci'ne ev câiyetün ev câiyâtün, el-eşcâru kutıat ev kutı'ne ev maktûatün ev maktûâtün)."},
 "examples": [
  {"ar": "امْرَأَةٍ وَنَاقَةٍ … غُرْفَةٍ وَشَمْسٍ", "en": "the real and the formal feminine", "tr": "hakîkî ve lafzî müennes", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "مُسْلِمُونَ وَمُسْلِمِينَ", "en": "the sound masculine plural", "tr": "cem-i müzekker sâlim", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "مُسْلِمَانِ وَمُسْلِمَيْنِ", "en": "the dual", "tr": "tesniye", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "رَجُلٌ قَاعِدٌ نَاصِرُوهُ", "en": "the sound plural annexed: the nūn dropped", "tr": "muzâf sâlim cemi': nûn düşmüş", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا أَوْ جَائِيَةٌ أَوْ جَاؤُونَ", "en": "the rational broken plural's governor", "tr": "âkıl mükesser cemi'in âmili", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "الْأَشْجَارُ قُطِعَتْ أَوْ قُطِعْنَ أَوْ مَقْطُوعَةٌ أَوْ مَقْطُوعَاتٌ", "en": "the non-rational plural's governor", "tr": "gayr-ı âkıl cemi'in âmili", "sourceStory": "izhar-al-asrar", "sentence": "s9"},
 ],
 "commonMistakes": [
  {"wrong": "نَاصِرُونَهُ", "right": "نَاصِرُوهُ", "why": {"en": "the sound plural's nūn drops in annexation", "tr": "sâlim cemi'in nûnu izâfette düşer"}},
  {"wrong": "الْمُسْلِمُونَ جَاءَتْ", "right": "الْمُسْلِمُونَ جَاؤُوا", "why": {"en": "the sound masculine plural's pronoun takes a masculine plural governor", "tr": "cem-i müzekker sâlimin zamiri cemi' müzekker âmil alır"}},
  {"wrong": "الْأَشْجَارُ جَاؤُوا", "right": "الْأَشْجَارُ قُطِعَتْ أَوْ قُطِعْنَ", "why": {"en": "a non-rational plural's pronoun takes a feminine singular or feminine plural governor", "tr": "gayr-ı âkıl cemi'in zamiri müfred müennes ya da cemi' müennes âmil alır"}},
 ],
}
ADD_EN = (" Chapter 27 (print pp. 127-128): the real and formal feminine (s1), the broken plural (s2), the sound masculine plural (s3), the sound feminine plural (s4), the dual (s5), every other plural feminine (s6), the sound masculine plural's governor (s7), the rational broken plural's (s8), the other plurals' (s9).")
ADD_TR = (" Yirmi yedinci bab (baskı s. 127-128): hakîkî ve lafzî müennes (s1), mükesser cemi' (s2), cem-i müzekker sâlim (s3), cem-i müennes sâlim (s4), tesniye (s5), diğer her cemi' müennes (s6), cem-i müzekker sâlimin âmili (s7), âkıl mükesser cemi'in (s8), diğer cemi'lerin (s9).")
write_out(27, S, TITLE, ADD_EN, ADD_TR, "pp. 127-128", GLOSS_ADD, notes=(NOTE,),
          related=((K25, [K]), (K26, [K]), (FL, [K]), (JMS, [K]), (JMA, [K]), (JT, [K]), (MTH, [K])))
report(27, S, GLOSS_ADD, (NOTE,))
