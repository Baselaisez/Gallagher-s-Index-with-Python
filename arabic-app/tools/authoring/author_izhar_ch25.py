# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 25: the APPARENT doer is plain; when the governor is predicated of it, the governor stays
# singular and third person even for a dual or plural (ضَرَبَ الزَّيْدَانِ وَالزَّيْدُونَ); a real feminine of the humans, singular or
# dual, attached to its governor, makes the governor feminine if it declines (ضَرَبَتْ هِنْدٌ أَوِ الْهِنْدَانِ، زَيْدٌ ضَارِبَةٌ جَارِيَتُهُ);
# so too when predicated of a feminine pronoun other than the rational broken masculine plural's (هِنْدٌ ضَرَبَتْ أَوْ ضَارِبَةٌ،
# الشَّمْسُ طَلَعَتْ أَوْ طَالِعَةٌ); elsewhere the governor may be feminine or masculine (طَلَعَتْ أَوْ طَلَعَ الشَّمْسُ، سَارَتْ أَوْ سَارَ
# النَّاقَةُ، جَاءَتْ أَوْ جَاءَ الْمُؤْمِنَاتُ، جَاءَتْ أَوْ جَاءَ الْقَاضِيَ الْيَوْمَ امْرَأَةٌ، الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا). Print pp. 125–126.
#   python3 author_izhar_ch25.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-fail-al-muzhar-wa-tanith-amilih"
K22 = "al-fail-al-mudmar-al-mustatir-wujuban"; K21 = "al-marfuat-al-fail-wa-naibuh"
TITLE = {"ar": "الْفَاعِلُ الْمُظْهَرُ وَتَأْنِيثُ عَامِلِهِ", "en": "The apparent doer and the feminine of its governor", "tr": "Muzhar fâil ve âmilinin te'nîsi"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; MSD = "masdar"; MR = "mudari-marfu"; JMS = "jam-mudhakkar-salim"; JMA = "jam-muannath-salim"; JT = "jam-taksir"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"
IDH = "idha-shartiyya"; INS = "in-shartiyya"; NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; MH = "mahall-al-majrur"; TAN = "tanith-al-fil" if False else "fail"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)
def wanahw(): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«and as in»", "«ve … gibi»", punct=":", segments=wa("نَحْوُ", "nahw", "noun"))
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")

# ----------- s1 — the apparent is plain
S.append({"id": "s1", "translation": {"en": "As for the apparent noun, it is plain.", "tr": "Muzhara (açık isme) gelince, o açıktır."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْمُظْهَرُ", "muzhar", "noun", [K, MK, IMF], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the apparent noun» — the mubtada.", "«muzhar» — mübtedâ."),
  tok("فَظَاهِرٌ", "zahir", "noun", [K, MK, IFA], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَظَاهِرٌ خَبَرٌ مَرْفُوعٌ — بَيِّنٌ لَا يَحْتَاجُ إِلَى بَيَانٍ.", "«is plain» — needs no explaining.", "«açıktır» — açıklama gerekmez.", punct=".", segments=fa("ظَاهِرٌ", "zahir", "noun")),
 ]})
# ----------- s2 — the governor singular and third person
S.append({"id": "s2", "translation": {"en": "And when the governor is predicated of it, it must be kept singular and in the third person, even if the doer is a dual or a plural — as in «the two Zayds struck» and «the Zayds struck».", "tr": "Âmil ona isnâd edildiğinde, fâil tesniye veya cemi' olsa bile, âmilin müfred ve gâib olması vâcibdir: «iki Zeyd vurdu», «Zeydler vurdu» gibi."},
 "tokens": [
  tok("وَإِذَا", "idha", "part", [K, AT, IDH, MF], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -dığında»", segments=wa("إِذَا", "idha", "part")),
  tok("أُسْنِدَ", "asnada", "verb", [K, NF, F4], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is predicated»", "«isnâd edilir»"),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — إِلَى الْمُظْهَرِ.", "«of it» — of the apparent noun.", "«ona» — muzhara.", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("الْعَامِلُ", "amil-governor", "noun", [K, NF, AQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the governor» — the deputy doer.", "«âmil» — nâib-i fâil."),
  tok("يَجِبُ", "wajaba", "verb", [K, FL, MR, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — جَوَابُ إِذَا.", "«it is necessary» — the answer of idhā.", "«vâcib olur» — izâ'nın cevâbı."),
  tok("إِفْرَادُهُ", "ifrad", "noun", [K, FL, ID, MSD, F4], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — إِفْرَادُ الْعَامِلِ.", "«keeping it singular» — the doer: the governor's singular.", "«onu müfred bırakmak» — fâil: âmilin müfredliği.", segments=[seg("إِفْرَادُ", "ifrad", "noun"), pr3ms()]),
  tok("وَغَيْبَتُهُ", "ghayba", "noun", [K, AT, ID, MSD], "الْوَاوُ عَاطِفَةٌ، وَغَيْبَتُهُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِيغَةُ الْغَائِبِ.", "«and its third person» — the absent's form.", "«ve gâib olması» — gâib sîgası.", segments=[seg("وَ", "wa", "conj"), seg("غَيْبَتُ", "ghayba", "noun"), pr3ms()]),
  tok("وَلَوْ", "law", "part", [K, AT, INS], "الْوَاوُ لِلْحَالِ، وَلَوْ وَصْلِيَّةٌ — لِلْمُبَالَغَةِ.", "«even if»", "«… olsa bile»", segments=wa("لَوْ", "law", "part")),
  tok("كَانَ", "kana", "verb", [K, KN], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمُظْهَرُ.", "«it be» — kāna, its ism the apparent noun.", "«olsa» — kâne, ismi muzhar."),
  tok("مُثَنًّى", "muthanna", "noun", [K, KN, MTH, MQ], "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — اسْمٌ مَقْصُورٌ.", "«a dual» — kāna's khabar.", "«tesniye» — kâne'nin haberi."),
  aw(),
  tok("مَجْمُوعًا", "majmu", "noun", [K, AT, KN, IMF], "مَعْطُوفٌ عَلَى مُثَنًّى مَنْصُوبٌ.", "«a plural»", "«cemi'»", punct="،"),
  nahw(),
  tok("ضَرَبَ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُفْرَدٌ غَائِبٌ.", "«struck» — singular, third person.", "«vurdu» — müfred gâib."),
  tok("الزَّيْدَانِ", "zayd", "propn", [K, FL, MTH], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«the two Zayds» — the doer in the dual.", "«iki Zeyd» — tesniye fâil."),
  tok("وَالزَّيْدُونَ", "zayd", "propn", [K, AT, FL, JMS], "الْوَاوُ عَاطِفَةٌ، وَالزَّيْدُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the Zayds» — the sound plural.", "«ve Zeydler» — cem-i müzekker sâlim.", punct=".", segments=wa("الزَّيْدُونَ", "zayd", "propn")),
 ]})
# ----------- s3 — the real feminine of the humans attached to its governor
S.append({"id": "s3", "translation": {"en": "And if it is a real feminine of the humans, singular or dual, attached to its governor, the governor must be made feminine, if it declines — as in «Hind struck», or «the two Hinds», and «Zayd — his maidservant is striking».", "tr": "Eğer insanlardan hakîkî müennes olup müfred veya tesniye ise ve âmiline bitişikse, âmil mutasarrıf olduğu takdirde te'nîsi vâcibdir: «Hind vurdu», ya «iki Hind», ve «Zeyd — câriyesi vurandır» gibi."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, INS], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is» — the condition's verb.", "«ise» — şart fiili."),
  tok("مُؤَنَّثًا", "muannath", "noun", [K, KN, IMF], "خَبَرُ كَانَ مَنْصُوبٌ.", "«feminine» — kāna's khabar.", "«müennes» — kâne'nin haberi."),
  tok("حَقِيقِيًّا", "haqiqi", "noun", [K, NA, NSB], "نَعْتٌ مَنْصُوبٌ — مَا بِإِزَائِهِ ذَكَرٌ.", "«real» — with a male counterpart.", "«hakîkî» — karşısında erkeği olan."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("الْآدَمِيِّينَ", "adami", "noun", [K, HJ, NSB, JMS], "مَجْرُورٌ بِمِنْ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — بَنِي آدَمَ.", "«the humans» — the children of Adam.", "«Âdemoğulları»", punct="،"),
  tok("مُفْرَدًا", "mufrad", "noun", [K, HL], "حَالٌ مَنْصُوبٌ.", "«singular»", "«müfred»"),
  aw(),
  tok("مُثَنًّى", "muthanna", "noun", [K, AT, HL, MTH, MQ], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«dual»", "«tesniye»", punct="،"),
  tok("مُتَّصِلًا", "muttasil", "noun", [K, HL, IFA], "حَالٌ ثَانٍ مَنْصُوبٌ — لَا فَاصِلَ بَيْنَهُ وَبَيْنَ عَامِلِهِ.", "«attached» — nothing between it and its governor.", "«bitişik» — âmiliyle arasında fâsıla yok."),
  tok("بِعَامِلِهِ", "amil-governor", "noun", [K, HJ, ID, AQ], "الْبَاءُ حَرْفُ جَرٍّ، وَعَامِلِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its governor»", "«âmiline»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("عَامِلِ", "amil-governor", "noun"), pr3msi()]),
  tok("يَجِبُ", "wajaba", "verb", [K, FL, MR, INS, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ — جَوَابُ الشَّرْطِ، مَرْفُوعٌ لِأَنَّهُ لَمْ يُقْصَدْ بِهِ الْجَزَاءُ لَفْظًا.", "«it is necessary» — the answer, in rafʿ.", "«vâcib olur» — cevap, merfû."),
  tok("تَأْنِيثُهُ", "tanith", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — تَأْنِيثُ الْعَامِلِ.", "«making it feminine» — the governor's tāʾ.", "«onun te'nîsi» — âmilin tâsı.", segments=[seg("تَأْنِيثُ", "tanith", "noun"), pr3ms()]),
  tok("إِنْ", "in-shartiyya", "part", [K, INS], "حَرْفُ شَرْطٍ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, KN, INS], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْعَامِلُ.", "«it is» — the governor.", "«ise» — âmil."),
  tok("مُتَصَرِّفًا", "mutasarrif", "noun", [K, KN, IFA], "خَبَرُ كَانَ مَنْصُوبٌ — يَقْبَلُ عَلَامَةَ التَّأْنِيثِ، لَا كَنِعْمَ عِنْدَ بَعْضٍ.", "«declining» — able to take the feminine sign.", "«mutasarrıf» — te'nîs alâmetini kabul eden.", punct="،"),
  nahw(),
  tok("ضَرَبَتْ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«struck (f.)»", "«vurdu (dişi)»"),
  tok("هِنْدٌ", "hind", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ حَقِيقِيٌّ.", "«Hind» — the doer, a real feminine.", "«Hind» — fâil, hakîkî müennes."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، كُسِرَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("الْهِنْدَانِ", "hind", "propn", [K, AT, FL, MTH], "مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«the two Hinds»", "«iki Hind»", punct="،"),
  tok("وَزَيْدٌ", "zayd", "propn", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and Zayd» — the mubtada.", "«ve Zeyd» — mübtedâ.", segments=wa("زَيْدٌ", "zayd", "propn")),
  tok("ضَارِبَةٌ", "darib", "noun", [K, MK, IFA, FL], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ أُنِّثَ لِفَاعِلِهِ الْمُؤَنَّثِ.", "«striking (f.)» — the participle made feminine for its doer.", "«vuran (dişi)» — fâili için te'nîs edilmiş ism-i fâil."),
  tok("جَارِيَتُهُ", "jariya", "noun", [K, FL, ID], "فَاعِلُ اسْمِ الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his maidservant» — the participle's doer.", "«câriyesi» — ism-i fâilin fâili.", punct=".", segments=[seg("جَارِيَتُ", "jariya", "noun"), pr3ms()]),
 ]})
# ----------- s4 — so too the feminine pronoun
S.append({"id": "s4", "translation": {"en": "And so too when it is predicated of the pronoun of a feminine other than the rational masculine broken plural — as in «Hind struck» or «is striking», and «the sun rose» or «is rising».", "tr": "Âkıl müzekker mükesser cemi' dışındaki müennesin zamirine isnâd edildiğinde de böyledir: «Hind vurdu» ya «vurandır», «güneş doğdu» ya «doğandır» gibi."},
 "tokens": [
  tok("وَكَذَا", "kadha", "part", [K, AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: الْحُكْمُ كَذَا.", "«and so too» — the khabar of a dropped «the ruling».", "«ve böyledir» — hazfedilmiş «hüküm»ün haberi.", segments=wa("كَذَا", "kadha", "part")),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-dığında»"),
  tok("أُسْنِدَ", "asnada", "verb", [K, NF, F4], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْعَامِلُ.", "«it is predicated» — the governor.", "«isnâd edilir» — âmil."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-e»"),
  tok("ضَمِيرِ", "damir", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«the pronoun of»", "«zamirine»"),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine»", "«müennesin»"),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ لِلْمُؤَنَّثِ مَجْرُورٌ، مُضَافٌ.", "«other than»", "«dışındaki»"),
  tok("جَمْعِ", "jam", "noun", [K, ID, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the plural of»", "«cem'i»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekkerin»"),
  tok("الْمُكَسَّرِ", "mukassar", "noun", [K, NA, JT, IMF], "نَعْتٌ لِلْجَمْعِ مَجْرُورٌ.", "«broken»", "«mükesser»"),
  tok("الْعَاقِلِ", "aqil", "noun", [K, NA, IFA], "نَعْتٌ ثَانٍ مَجْرُورٌ — نَحْوُ الرِّجَالِ.", "«rational» — like الرِّجَال.", "«âkıl» — er-ricâl gibi.", punct="،"),
  nahw(),
  tok("هِنْدٌ", "hind", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Hind» — the mubtada.", "«Hind» — mübtedâ."),
  tok("ضَرَبَتْ", "daraba", "verb", [K, MK, FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«struck» — the doer the hidden «she».", "«vurdu» — fâil gizli «o»."),
  aw(),
  tok("ضَارِبَةٌ", "darib", "noun", [K, AT, MK, IFA], "مَعْطُوفٌ عَلَى الْجُمْلَةِ مَرْفُوعٌ — خَبَرٌ، وَفَاعِلُهُ مُسْتَتِرٌ: هِيَ.", "«is striking» — a khabar with the hidden «she».", "«vurandır» — gizli «o» ile haber.", punct="،"),
  tok("وَالشَّمْسُ", "shams", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالشَّمْسُ مُبْتَدَأٌ مَرْفُوعٌ — مُؤَنَّثٌ لَفْظِيٌّ.", "«and the sun» — a formal feminine.", "«ve güneş» — lafzî müennes.", segments=wa("الشَّمْسُ", "shams", "noun")),
  tok("طَلَعَتْ", "talaa", "verb", [K, MK, FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«rose»", "«doğdu»"),
  aw(),
  tok("طَالِعَةٌ", "tali", "noun", [K, AT, MK, IFA], "مَعْطُوفٌ مَرْفُوعٌ — خَبَرٌ، وَفَاعِلُهُ مُسْتَتِرٌ: هِيَ.", "«is rising»", "«doğandır»", punct="."),
 ]})
# ----------- s5 — elsewhere, feminine or masculine
S.append({"id": "s5", "translation": {"en": "And in other than these two, it is allowed to make its governor feminine or masculine, if the doer is feminine — as in «the sun rose» (with or without the tāʾ), and as in «the she-camel went», and as in «the believing women came»;", "tr": "Bu ikisinin dışında, fâil müennes ise âmilini te'nîs de tezkîr de câizdir: «güneş doğdu» (tâlı veya tâsız), «dişi deve yürüdü», «mümin kadınlar geldi» gibi;"},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, AT, HJ, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and in» — the fronted khabar.", "«ve -de» — öne alınmış haber.", segments=wa("فِي", "fi", "prep")),
  tok("غَيْرِهِمَا", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — غَيْرِ الصُّورَتَيْنِ.", "«other than the two» — the two cases above.", "«o ikisinin dışında» — yukarıdaki iki sûret.", segments=[seg("غَيْرِ", "ghayr", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câizdir»"),
  tok("تَأْنِيثُ", "tanith", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«making feminine» — the doer.", "«te'nîsi» — fâil."),
  tok("عَامِلِهِ", "amil-governor", "noun", [K, ID, AQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", segments=[seg("عَامِلِ", "amil-governor", "noun"), pr3msi()]),
  tok("وَتَذْكِيرُهُ", "tadhkir", "noun", [K, AT, ID, MSD, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَذْكِيرُهُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and making it masculine»", "«ve tezkîri»", segments=[seg("وَ", "wa", "conj"), seg("تَذْكِيرُ", "tadhkir", "noun"), pr3ms()]),
  tok("إِنْ", "in-shartiyya", "part", [K, INS], "حَرْفُ شَرْطٍ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, KN, INS], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْفَاعِلُ.", "«it is» — the doer.", "«ise» — fâil."),
  tok("مُؤَنَّثًا", "muannath", "noun", [K, KN, IMF], "خَبَرُ كَانَ مَنْصُوبٌ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«feminine» — the answer understood from what precedes.", "«müennes» — cevap öncesinden anlaşılır.", punct="،"),
  nahw(),
  tok("طَلَعَتْ", "talaa", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«rose (f.)»", "«doğdu (dişi)»"),
  aw(),
  tok("طَلَعَ", "talaa", "verb", [K, AT, FL], "فِعْلٌ مَاضٍ مَعْطُوفٌ — بِلَا تَاءٍ.", "«rose» — without the tāʾ.", "«doğdu» — tâsız."),
  tok("الشَّمْسُ", "shams", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ لِلْفِعْلَيْنِ — تَنَازُعٌ، أَوْ فَاعِلُ الثَّانِي.", "«the sun» — the doer the two verbs share.", "«güneş» — iki fiilin paylaştığı fâil.", punct="،"),
  wanahw(),
  tok("سَارَتْ", "sara-go", "verb", [K, FL, HV], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«went (f.)»", "«yürüdü (dişi)»"),
  aw(),
  tok("سَارَ", "sara-go", "verb", [K, AT, FL, HV], "فِعْلٌ مَاضٍ مَعْطُوفٌ.", "«went»", "«yürüdü»"),
  tok("النَّاقَةُ", "naqa", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ حَقِيقِيٌّ مِنْ غَيْرِ الْآدَمِيِّينَ.", "«the she-camel» — a real feminine, not human.", "«dişi deve» — insan olmayan hakîkî müennes.", punct="،"),
  wanahw(),
  tok("جَاءَتْ", "jaa", "verb", [K, FL, HV], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«came (f.)»", "«geldi (dişi)»"),
  aw(),
  tok("جَاءَ", "jaa", "verb", [K, AT, FL, HV], "فِعْلٌ مَاضٍ مَعْطُوفٌ.", "«came»", "«geldi»"),
  tok("الْمُؤْمِنَاتُ", "mumin", "noun", [K, FL, JMA, IFA], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the believing women» — the sound feminine plural.", "«mümin kadınlar» — cem-i müennes sâlim.", punct="؛"),
 ]})
# ----------- s6 — the separated feminine and the broken plural
S.append({"id": "s6", "translation": {"en": "and as in «there came to the judge today a woman» (with or without the tāʾ), and «the men came» (with the tāʾ or the wāw), or «the men came» (with or without the tāʾ).", "tr": "ve «bugün kadıya bir kadın geldi» (tâlı veya tâsız), «adamlar geldi» (tâ ile veya vâv ile), ya da «adamlar geldi» (tâlı veya tâsız) gibi."},
 "tokens": [
  wanahw(),
  tok("جَاءَتْ", "jaa", "verb", [K, FL, HV], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«came (f.)»", "«geldi (dişi)»"),
  aw(),
  tok("جَاءَ", "jaa", "verb", [K, AT, FL, HV], "فِعْلٌ مَاضٍ مَعْطُوفٌ.", "«came»", "«geldi»"),
  tok("الْقَاضِيَ", "qadi", "noun", [K, MB, MQ], "مَفْعُولٌ بِهِ مَنْصُوبٌ — فَاصِلٌ بَيْنَ الْفِعْلِ وَفَاعِلِهِ.", "«the judge» — the object parting the verb from its doer.", "«kadı» — fiil ile fâili arasındaki fâsıla."),
  tok("الْيَوْمَ", "yawm", "noun", [K, MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«today»", "«bugün»"),
  tok("امْرَأَةٌ", "imraa", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ حَقِيقِيٌّ مُنْفَصِلٌ عَنْ عَامِلِهِ.", "«a woman» — the real feminine, parted from its governor.", "«bir kadın» — âmilinden ayrı hakîkî müennes.", punct="،"),
  tok("وَالرِّجَالُ", "rijal", "noun", [K, AT, MK, JT], "الْوَاوُ عَاطِفَةٌ، وَالرِّجَالُ مُبْتَدَأٌ مَرْفُوعٌ — جَمْعُ مُذَكَّرٍ مُكَسَّرٌ عَاقِلٌ.", "«and the men» — the rational broken plural.", "«ve adamlar» — âkıl mükesser cemi'.", segments=wa("الرِّجَالُ", "rijal", "noun")),
  tok("جَاءَتْ", "jaa", "verb", [K, MK, FL, HV], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — الْجَمَاعَةُ؛ وَالْجُمْلَةُ خَبَرٌ.", "«came (f.)» — the hidden «she»: the group.", "«geldi (dişi)» — gizli «o»: cemâat."),
  aw(),
  tok("جَاؤُوا", "jaa", "verb", [K, AT, FL, HV, MH], "فِعْلٌ مَاضٍ مَعْطُوفٌ، وَالْوَاوُ فَاعِلٌ.", "«came (pl.)» — the wāw the doer.", "«geldiler» — vâv fâil.", punct="،"),
  aw(),
  tok("جَاءَتْ", "jaa", "verb", [K, FL, HV], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — جُمْلَةٌ مَعْطُوفَةٌ.", "«came (f.)»", "«geldi (dişi)»"),
  aw(),
  tok("جَاءَ", "jaa", "verb", [K, AT, FL, HV], "فِعْلٌ مَاضٍ مَعْطُوفٌ.", "«came»", "«geldi»"),
  tok("الرِّجَالُ", "rijal", "noun", [K, FL, JT], "فَاعِلٌ مَرْفُوعٌ.", "«the men» — the doer.", "«adamlar» — fâil.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "ghayba": G("ghayba", "غَيْبَة", "غ ي ب", "noun", "absence — the third person's form (maṣdar of غَابَ)", "gaybet — gâib sîgası (gâbe'nin mastarı)", 4),
 "adami": G("adami", "آدَمِيّ", "أ د م", "noun", "human, a child of Adam (nisba)", "âdemî — Âdemoğlu (nisbet)", 3, plural="آدَمِيُّونَ"),
 "tanith": G("tanith", "تَأْنِيث", "أ ن ث", "noun", "making feminine — the feminine sign on the governor (maṣdar of أَنَّثَ)", "te'nîs — âmil üzerindeki müenneslik alâmeti (ennese'nin mastarı)", 4, form="II"),
 "tali": G("tali", "طَالِع", "ط ل ع", "noun", "rising (ism fāʿil of طَلَعَ)", "doğan (talaa'nın ism-i fâili)", 2),
 "sara-go": G("sara-go", "سَارَ", "س ي ر", "verb", "to go, travel, move along", "yürümek, gitmek", 2),
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
put_morph(mo, "sara-go", {"bab": "الْبَابُ الثَّانِي فَعَلَ يَفْعِلُ — أَجْوَفُ يَائِيٌّ", "wazn": "فَعَلَ يَفْعِلُ", "masdar": "سَيْر", "ismFail": "سَائِر",
 "mazi": ["سَارَ", "سَارَا", "سَارُوا", "سَارَتْ", "سَارَتَا", "سِرْنَ", "سِرْتَ", "سِرْتُمَا", "سِرْتُمْ", "سِرْتِ", "سِرْتُمَا", "سِرْتُنَّ", "سِرْتُ", "سِرْنَا"],
 "mudari": ["يَسِيرُ", "يَسِيرَانِ", "يَسِيرُونَ", "تَسِيرُ", "تَسِيرَانِ", "يَسِرْنَ", "تَسِيرُ", "تَسِيرَانِ", "تَسِيرُونَ", "تَسِيرِينَ", "تَسِيرَانِ", "تَسِرْنَ", "أَسِيرُ", "نَسِيرُ"],
 "amr": ["سِرْ", "سِيرَا", "سِيرُوا", "سِيرِي", "سِيرَا", "سِرْنَ"], "mansub": "يَسِيرَ", "majzum": "يَسِرْ", "majzum2": "تَسِرْ",
 "note": "سَارَ يَسِيرُ سَيْرًا: مَضَى وَذَهَبَ — أَجْوَفُ يَائِيٌّ مِنَ الْبَابِ الثَّانِي (أَصْلُهُ سَيَرَ)؛ تُحْذَفُ عَيْنُهُ عِنْدَ السُّكُونِ (سِرْتُ، يَسِرْنَ، لَمْ يَسِرْ)."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch25 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("daraba", "jaa", "kana", "asnada", "wajaba", "jaaza", "talaa", "sara-go") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْفَاعِلُ الْمُظْهَرُ: إِفْرَادُ عَامِلِهِ وَغَيْبَتُهُ وَتَأْنِيثُهُ", "en": "The apparent doer: its governor singular, third person, and feminine", "tr": "Muzhar fâil: âmilinin müfredliği, gaybeti ve te'nîsi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الفاعل المظهر وتأنيث عامله", "الكافية لابن الحاجب — الفاعل: تأنيث الفعل", "شرح قطر الندى لابن هشام — تأنيث الفعل للفاعل"],
 "amil": "the apparent doer keeps its governor singular and in the third person even when it is a dual or plural (ضَرَبَ الزَّيْدَانِ وَالزَّيْدُونَ); a real feminine of the humans, singular or dual, attached to a declining governor, makes it feminine (ضَرَبَتْ هِنْدٌ أَوِ الْهِنْدَانِ، زَيْدٌ ضَارِبَةٌ جَارِيَتُهُ), and so does a feminine pronoun other than the rational broken plural's (هِنْدٌ ضَرَبَتْ، الشَّمْسُ طَلَعَتْ); elsewhere the governor may be feminine or masculine (طَلَعَتْ أَوْ طَلَعَ الشَّمْسُ، سَارَتْ أَوْ سَارَ النَّاقَةُ، جَاءَتْ أَوْ جَاءَ الْمُؤْمِنَاتُ، جَاءَتْ أَوْ جَاءَ الْقَاضِيَ الْيَوْمَ امْرَأَةٌ، الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا)",
 "question": {
  "en": ["What happens to the governor predicated of an apparent doer? It stays singular and third person, even if the doer is a dual or a plural: ضَرَبَ الزَّيْدَانِ، ضَرَبَ الزَّيْدُونَ — never ضَرَبَا الزَّيْدَانِ.",
         "When must the governor be feminine? When the doer is a real feminine of the humans, singular or dual, attached to its governor — and the governor declines: ضَرَبَتْ هِنْدٌ، ضَرَبَتِ الْهِنْدَانِ، زَيْدٌ ضَارِبَةٌ جَارِيَتُهُ.",
         "And with a pronoun? When the governor is predicated of a feminine pronoun other than the rational broken masculine plural's: هِنْدٌ ضَرَبَتْ أَوْ ضَارِبَةٌ، الشَّمْسُ طَلَعَتْ أَوْ طَالِعَةٌ.",
         "Where is it a choice? In every other case with a feminine doer: طَلَعَتْ أَوْ طَلَعَ الشَّمْسُ (a formal feminine), سَارَتْ أَوْ سَارَ النَّاقَةُ (a real feminine not human), جَاءَتْ أَوْ جَاءَ الْمُؤْمِنَاتُ (a sound feminine plural), جَاءَتْ أَوْ جَاءَ الْقَاضِيَ الْيَوْمَ امْرَأَةٌ (a real feminine parted from its governor), الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا (the rational broken plural's pronoun).",
         "Why is «attached» a condition? Because an object or ẓarf between the verb and a real feminine doer loosens the tie: جَاءَ الْقَاضِيَ الْيَوْمَ امْرَأَةٌ is allowed.",
         "What does the engine READ here? The DabtEngine raises the noun after a singular verb as its doer whatever its number, raises جَارِيَتُهُ after the feminine participle as the participle's doer, reads الْقَاضِيَ between the verb and امْرَأَةٌ as the object, and joins the paired verbs with أَوْ as alternatives sharing one doer."],
  "tr": ["Muzhar fâile isnâd edilen âmile ne olur? Fâil tesniye veya cemi' olsa bile müfred ve gâib kalır: darabe'z-Zeydâni, darabe'z-Zeydûne — asla darabâ'z-Zeydâni değil.",
         "Âmilin te'nîsi ne zaman vâcibdir? Fâil insanlardan hakîkî müennes olup müfred veya tesniye ise, âmiline bitişikse ve âmil mutasarrıfsa: darabet Hindün, darabeti'l-Hindâni, Zeydün dâribetün câriyetühû.",
         "Zamirle? Âmil, âkıl mükesser müzekker cemi' dışındaki müennesin zamirine isnâd edilince: Hindün darabet ev dâribetün, eş-şemsü tala'at ev tâli'atün.",
         "Nerede tercihe kalır? Müennes fâilli diğer her durumda: tala'at ev tala'a'ş-şemsü (lafzî müennes), sârat ev sâra'n-nâkatü (insan olmayan hakîkî müennes), câet ev câe'l-mü'minâtü (cem-i müennes sâlim), câet ev câe'l-kâdıye'l-yevme imraetün (âmilinden ayrı hakîkî müennes), er-ricâlü câet ev câû (âkıl mükesser cemi'in zamiri).",
         "«Bitişik» niçin şarttır? Çünkü fiil ile hakîkî müennes fâil arasına giren mef'ûl veya zarf bağı gevşetir: câe'l-kâdıye'l-yevme imraetün câizdir.",
         "Motor burada neyi OKUR? DabtEngine müfred fiilden sonraki ismi sayısı ne olursa olsun fâil olarak ref' eder, müennes ism-i fâilden sonraki câriyetühû'yu ism-i fâilin fâili okur, fiil ile imraetün arasındaki el-kâdıye'yi mef'ûl okur ve ev ile eşlenen fiilleri tek fâili paylaşan seçenekler olarak bağlar."],
 },
 "plain": {"en": "A verb keeps its singular form before its subject even when the subject is two or many: «struck the two Zayds». If the subject is a woman's name right after the verb, the verb takes the feminine tāʾ: «struck (f.) Hind». For the sun, a she-camel, or a woman separated from the verb, the tāʾ is optional.",
           "tr": "Fiil, öznesi iki veya çok olsa da öznesinden önce tekil kalır: «vurdu iki Zeyd». Özne fiilin hemen ardındaki bir kadın adıysa fiil dişil tâ alır: «vurdu (dişi) Hind». Güneş, dişi deve ya da fiilden ayrı düşmüş bir kadın için tâ isteğe bağlıdır."},
 "explanation": {"en": "The apparent doer is plain. When the governor is predicated of it, the governor must be kept singular and in the third person even if the doer is a dual or a plural (ضَرَبَ الزَّيْدَانِ وَالزَّيْدُونَ). If the doer is a real feminine of the humans, singular or dual, attached to its governor, the governor must be made feminine — if it declines (ضَرَبَتْ هِنْدٌ أَوِ الْهِنْدَانِ، زَيْدٌ ضَارِبَةٌ جَارِيَتُهُ); and so when the governor is predicated of the pronoun of a feminine other than the rational masculine broken plural (هِنْدٌ ضَرَبَتْ أَوْ ضَارِبَةٌ، الشَّمْسُ طَلَعَتْ أَوْ طَالِعَةٌ). In other than these two, the governor may be made feminine or masculine if the doer is feminine (طَلَعَتْ أَوْ طَلَعَ الشَّمْسُ، سَارَتْ أَوْ سَارَ النَّاقَةُ، جَاءَتْ أَوْ جَاءَ الْمُؤْمِنَاتُ، جَاءَتْ أَوْ جَاءَ الْقَاضِيَ الْيَوْمَ امْرَأَةٌ، الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا، جَاءَتْ أَوْ جَاءَ الرِّجَالُ).",
                 "tr": "Muzhar fâil açıktır. Âmil ona isnâd edilince, fâil tesniye veya cemi' olsa bile âmilin müfred ve gâib olması vâcibdir (darabe'z-Zeydâni ve'z-Zeydûne). Fâil insanlardan hakîkî müennes olup müfred veya tesniye ise ve âmiline bitişikse, âmil mutasarrıf olduğu takdirde te'nîsi vâcibdir (darabet Hindün evi'l-Hindâni, Zeydün dâribetün câriyetühû); âmil, âkıl müzekker mükesser cemi' dışındaki müennesin zamirine isnâd edilince de böyledir (Hindün darabet ev dâribetün, eş-şemsü tala'at ev tâli'atün). Bu ikisinin dışında fâil müennes ise âmilin te'nîsi de tezkîri de câizdir (tala'at ev tala'a'ş-şemsü, sârat ev sâra'n-nâkatü, câet ev câe'l-mü'minâtü, câet ev câe'l-kâdıye'l-yevme imraetün, er-ricâlü câet ev câû, câet ev câe'r-ricâlü)."},
 "examples": [
  {"ar": "ضَرَبَ الزَّيْدَانِ وَالزَّيْدُونَ", "en": "the governor singular before the dual and plural doer", "tr": "tesniye ve cemi' fâilden önce müfred âmil", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "ضَرَبَتْ هِنْدٌ أَوِ الْهِنْدَانِ، وَزَيْدٌ ضَارِبَةٌ جَارِيَتُهُ", "en": "the real human feminine attached: the feminine governor", "tr": "bitişik hakîkî müennes: müennes âmil", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "هِنْدٌ ضَرَبَتْ أَوْ ضَارِبَةٌ، وَالشَّمْسُ طَلَعَتْ أَوْ طَالِعَةٌ", "en": "the feminine pronoun", "tr": "müennes zamir", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "طَلَعَتْ أَوْ طَلَعَ الشَّمْسُ، سَارَتْ أَوْ سَارَ النَّاقَةُ", "en": "the choice elsewhere", "tr": "diğer yerlerde tercih", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "جَاءَتْ أَوْ جَاءَ الْقَاضِيَ الْيَوْمَ امْرَأَةٌ", "en": "the feminine parted from its governor", "tr": "âmilinden ayrı müennes", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "ضَرَبُوا الزَّيْدُونَ", "right": "ضَرَبَ الزَّيْدُونَ", "why": {"en": "the governor before an apparent doer stays singular: the wāw would be a second doer", "tr": "muzhar fâilden önceki âmil müfred kalır: vâv ikinci bir fâil olurdu"}},
  {"wrong": "ضَرَبَ هِنْدٌ", "right": "ضَرَبَتْ هِنْدٌ", "why": {"en": "a real human feminine attached to a declining governor makes it feminine by necessity", "tr": "bitişik hakîkî müennes, mutasarrıf âmili vücûben te'nîs eder"}},
  {"wrong": "الرِّجَالُ جَاءَ", "right": "الرِّجَالُ جَاءَتْ أَوْ جَاؤُوا", "why": {"en": "predicated of the rational broken plural's pronoun, the governor is feminine singular or masculine plural", "tr": "âkıl mükesser cemi'in zamirine isnâd edilince âmil müfred müennes veya cemi' müzekker olur"}},
 ],
}
ADD_EN = (" Chapter 25 (print pp. 125-126): the apparent doer plain (s1), its governor singular and third person before a dual or plural (s2), feminine by necessity for the attached real human feminine (s3) and the feminine pronoun other than the rational broken plural's (s4), feminine or masculine elsewhere (s5-s6).")
ADD_TR = (" Yirmi beşinci bab (baskı s. 125-126): muzhar fâil açıktır (s1), tesniye ve cemi' önünde âmili müfred ve gâib (s2), bitişik hakîkî insan müennesi (s3) ve âkıl mükesser cemi' dışındaki müennes zamiri için vücûben müennes (s4), diğer yerlerde müennes veya müzekker (s5-s6).")
write_out(25, S, TITLE, ADD_EN, ADD_TR, "pp. 125-126", GLOSS_ADD, notes=(NOTE,),
          related=((K22, [K]), (K21, [K]), (FL, [K]), (MTH, [K]), (JMS, [K]), (JMA, [K]), (JT, [K]), (IFA, [K])))
report(25, S, GLOSS_ADD, (NOTE,))
