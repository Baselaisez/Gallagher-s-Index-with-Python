# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 29: the FOURTH marfūʿ, the KHABAR of the mubtadaʾ — what is stripped of the governors of wording
# and predicated, other than the verb and its sense (قَائِمٌ in زَيْدٌ قَائِمٌ); it may be multiplied (زَيْدٌ قَائِمٌ قَاعِدٌ); it may be a
# nominal or verbal sentence, then a pronoun returning to the mubtadaʾ is a must unless the khabar is of the pronoun of the matter
# (زَيْدٌ أَبُوهُ قَائِمٌ أَوْ قَامَ أَبُوهُ); it may be dropped on a clue (الْبُرُّ الْكُرُّ بِسِتِّينَ، أَيْ مِنْهُ); its origin is to be a nakira,
# and it may be definite (اللهُ إِلٰهُنَا); it may be dropped on a clue (زَيْدٌ answering أَزَيْدٌ قَائِمٌ أَمْ عَمْرٌو). Print pp. 129–130.
#   python3 author_izhar_ch29.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "khabar-al-mubtada-wa-ahkamuh"
K28 = "al-mubtada-wa-nawah"
TITLE = {"ar": "الْمَرْفُوعُ الرَّابِعُ: خَبَرُ الْمُبْتَدَإِ وَأَحْكَامُهُ", "en": "The fourth marfūʿ: the khabar of the mubtadaʾ and its rules", "tr": "Dördüncü merfû: mübtedânın haberi ve hükümleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"; AMS = "an-masdariyya"
NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; INS = "in-shartiyya"; JZ = "nawasib-wa-jawazim-al-mudari"; YM = "ya-al-mutakallim"; DF = "damir-fasl"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wayajuz(): return tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb"))
def hadhfuhu(): return tok("حَذْفُهُ", "hadhf", "noun", [K, FL, ID, MSD, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«dropping it» — the doer.", "«onun hazfi» — fâil.", segments=[seg("حَذْفُ", "hadhf", "noun"), pr3ms()])

# ----------- s1 — the fourth: the khabar defined
S.append({"id": "s1", "translation": {"en": "And the fourth is the khabar of the mubtadaʾ, and it is what is stripped of the governors of wording and predicated, other than the verb and what has its sense — as in «standing» in «Zayd is standing»;", "tr": "Dördüncüsü mübtedânın haberidir; o, lafzî âmillerden soyutlanmış, kendisiyle isnâd yapılan, fiil ve fiil mânâsındaki dışındaki şeydir — «Zeyd ayaktadır»daki «ayakta» gibi;"},
 "tokens": [
  tok("وَالرَّابِعُ", "rabi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالرَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fourth»", "«dördüncüsü»", segments=wa("الرَّابِعُ", "rabi", "noun")),
  tok("خَبَرُ", "khabar", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the khabar of» — the khabar.", "«haberi» — haber."),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtadaʾ»", "«mübtedânın»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمُجَرَّدُ", "mujarrad", "noun", [K, MK, IMF, F2], "خَبَرٌ مَرْفُوعٌ.", "«what is stripped» — the khabar.", "«soyutlanmış» — haber."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("الْعَوَامِلِ", "awamil", "noun", [K, HJ, JT, AQ], "مَجْرُورٌ بِعَنْ.", "«the governors»", "«âmiller»"),
  tok("اللَّفْظِيَّةِ", "lafzi", "noun", [K, NA, NSB], "نَعْتٌ مَجْرُورٌ.", "«of wording»", "«lafzî»"),
  tok("الْمُسْنَدُ", "musnad", "noun", [K, NA, IMF, F4], "نَعْتٌ لِلْمُجَرَّدِ مَرْفُوعٌ.", "«predicated»", "«isnâd edilen»"),
  tok("بِهِ", "bi", "prep", [K, HJ, NF], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — نَائِبُ فَاعِلِ الْمُسْنَدِ.", "«by it» — the participle's deputy.", "«onunla» — ism-i mef'ûlün nâibi.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("غَيْرُ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ ثَانٍ مَرْفُوعٌ، مُضَافٌ — أَوْ بَدَلٌ.", "«other than»", "«dışındaki»"),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»"),
  tok("وَمَعْنَاهُ", "mana", "noun", [K, AT, ID, MQ, MNF], "الْوَاوُ عَاطِفَةٌ، وَمَعْنَاهُ مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَا بِمَعْنَى الْفِعْلِ: الصِّفَةُ الْوَاقِعَةُ بَعْدَ الِاسْتِفْهَامِ.", "«and what has its sense» — the adjective after the question.", "«ve onun mânâsındaki» — istifhâmdan sonraki sıfat.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  nahw(),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — أَيْ: كَقَائِمٍ.", "«standing»", "«ayakta»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-deki»", punct=":"),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, HJ], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«is standing»", "«ayaktadır»", punct="؛"),
 ]})
# ----------- s2 — it may be multiplied
S.append({"id": "s2", "translation": {"en": "and it may be multiplied — as in «Zayd is standing, seated»;", "tr": "taaddüdü câizdir — «Zeyd ayaktadır, oturmaktadır» gibi;"},
 "tokens": [
  wayajuz(),
  tok("تَعَدُّدُهُ", "taaddud", "noun", [K, FL, ID, MSD, F5], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its being multiplied» — the doer.", "«taaddüdü» — fâil.", punct="،", segments=[seg("تَعَدُّدُ", "taaddud", "noun"), pr3ms()]),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرٌ أَوَّلُ مَرْفُوعٌ.", "«standing» — the first khabar.", "«ayakta» — ilk haber."),
  tok("قَاعِدٌ", "qaid", "noun", [K, MK, IFA], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«seated» — the second khabar.", "«oturmakta» — ikinci haber.", punct="؛"),
 ]})
# ----------- s3 — the khabar as a sentence; the returning pronoun
S.append({"id": "s3", "translation": {"en": "and it may be a nominal or a verbal sentence, and then a pronoun returning to the mubtadaʾ is a must, unless the sentence is the khabar of the pronoun of the matter — as in «Zayd, his father is standing» or «his father stood»;", "tr": "isim ya da fiil cümlesi olabilir; o zaman — şe'n zamirinin haberi değilse — mübtedâya dönen bir zamir zorunludur: «Zeyd, babası ayaktadır» ya da «babası kalktı» gibi;"},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْخَبَرُ.", "«it is» — the khabar.", "«olur» — haber."),
  tok("جُمْلَةً", "jumla", "noun", [K, KN], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«a sentence»", "«bir cümle»"),
  tok("اسْمِيَّةً", "ismiyya", "noun", [K, NA, NSB], "نَعْتٌ مَنْصُوبٌ.", "«nominal»", "«isim cümlesi»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("فِعْلِيَّةً", "filiyya", "noun", [K, AT, NSB], "مَعْطُوفٌ مَنْصُوبٌ.", "«verbal»", "«fiil cümlesi»", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, AT, LN], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«so no»", "«o halde … yok»", segments=fa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, LN, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«escape» — it must.", "«çâre» — zorunlu."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("عَائِدٍ", "aid", "noun", [K, HJ, IFA, MK], "مَجْرُورٌ بِمِنْ — ضَمِيرٌ يَعُودُ.", "«a returning pronoun»", "«bir âid»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ], "مَجْرُورٌ بِإِلَى.", "«the mubtadaʾ»", "«mübtedâya»"),
  tok("إِنْ", "in-shartiyya", "part", [K, INS], "حَرْفُ شَرْطٍ.", "«if»", "«eğer»"),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not»", "«-mez»"),
  tok("تَكُنْ", "kana", "verb", [K, KN, "lam-jazim", HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — الْجُمْلَةُ.", "«it be» — the sentence.", "«olmazsa» — cümle."),
  tok("خَبَرًا", "khabar", "noun", [K, KN], "خَبَرُ تَكُنْ مَنْصُوبٌ.", "«a khabar»", "«haber»"),
  tok("عَنْ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("ضَمِيرِ", "damir", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَنْ، مُضَافٌ.", "«the pronoun of»", "«zamiri»"),
  tok("الشَّأْنِ", "shan", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — هُوَ زَيْدٌ قَائِمٌ.", "«the matter» — as in هُوَ زَيْدٌ قَائِمٌ.", "«şe'n» — hüve Zeydün kâimün.", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("أَبُوهُ", "ab", "noun", [K, MK, ID, "five-nouns"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«his father» — the second mubtada; the pronoun is the returner.", "«babası» — ikinci mübtedâ; zamiri âid.", segments=[seg("أَبُو", "ab", "noun"), pr3ms()]),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرُ الثَّانِي، وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.", "«is standing» — the second's khabar; the clause the first's.", "«ayaktadır» — ikincinin haberi; cümle ilkinin haberi."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("قَامَ", "qama", "verb", [K, FL, HV, MK], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ الْفِعْلِيَّةُ خَبَرٌ.", "«stood» — the verbal clause as khabar.", "«kalktı» — fiil cümlesi haber."),
  tok("أَبُوهُ", "ab", "noun", [K, FL, ID, "five-nouns"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«his father» — the doer; the pronoun the returner.", "«babası» — fâil; zamiri âid.", punct="؛", segments=[seg("أَبُو", "ab", "noun"), pr3ms()]),
 ]})
# ----------- s4 — the returner dropped on a clue
S.append({"id": "s4", "translation": {"en": "and the returner may be dropped on a clue — as in «wheat: the kurr is at sixty», that is, «of it»;", "tr": "âidin karîne ile hazfi câizdir — «buğday: bir kür altmışadır» gibi; yani: «ondan»;"},
 "tokens": [
  wayajuz(),
  hadhfuhu(),
  tok("لِقَرِينَةٍ", "qarina", "noun", [K, HJ, HT], "اللَّامُ حَرْفُ جَرٍّ، وَقَرِينَةٍ مَجْرُورٌ.", "«on a clue»", "«karîne ile»", punct="،", segments=[seg("لِ", "li", "prep"), seg("قَرِينَةٍ", "qarina", "noun")]),
  nahw(),
  tok("الْبُرُّ", "birr", "noun", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ أَوَّلُ مَرْفُوعٌ.", "«wheat» — the first mubtada.", "«buğday» — ilk mübtedâ."),
  tok("الْكُرُّ", "kurr", "noun", [K, MK], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.", "«the kurr» — the second mubtada: the measure.", "«kür» — ikinci mübtedâ: ölçek."),
  tok("بِسِتِّينَ", "sittun", "noun", [K, HJ, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَسِتِّينَ مَجْرُورٌ بِالْيَاءِ — خَبَرُ الثَّانِي، وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ بِلَا عَائِدٍ ظَاهِرٍ.", "«at sixty» — the second's khabar; the clause the first's, its returner unsaid.", "«altmışa» — ikincinin haberi; cümle ilkinin haberi, âidi hazfedilmiş.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("سِتِّينَ", "sittun", "noun")]),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":"),
  tok("مِنْهُ", "min", "prep", [K, HJ, HT], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ الْمُقَدَّرُ: الْكُرُّ مِنْهُ.", "«of it» — the returner restored.", "«ondan» — takdîr edilen âid.", punct="؛", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
 ]})
# ----------- s5 — its origin a nakira; it may be definite
S.append({"id": "s5", "translation": {"en": "and its origin is to be indefinite, though it may be definite — as in «God is our deity»;", "tr": "aslı nekre olmasıdır; ma'rife de olabilir — «Allah ilâhımızdır» gibi;"},
 "tokens": [
  tok("وَأَصْلُهُ", "asl", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَأَصْلُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its origin»", "«ve aslı»", segments=[seg("وَ", "wa", "conj"), seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, MK], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ.", "«it be»", "«olması»"),
  tok("نَكِرَةً", "nakira", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«indefinite»", "«nekre»", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«olur»"),
  tok("مَعْرِفَةً", "marifa", "noun", [K, KN], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«definite»", "«ma'rife»", punct="،"),
  nahw(),
  tok("اللهُ", "allah", "propn", [K, MK], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«God» — the mubtada.", "«Allah» — mübtedâ."),
  tok("إِلٰهُنَا", "ilah", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — مَعْرِفَةٌ بِالْإِضَافَةِ.", "«our deity» — a definite khabar by annexation.", "«ilâhımız» — izâfetle ma'rife haber.", punct="؛", segments=[seg("إِلٰهُ", "ilah", "noun"), seg("نَا", "pron-1p", "pron")]),
 ]})
# ----------- s6 — the khabar dropped on a clue
S.append({"id": "s6", "translation": {"en": "and it may be dropped where a clue stands — as in «Zayd» to one who asked «is Zayd standing, or ʿAmr?».", "tr": "karîne bulununca hazfi câizdir — «Zeyd mi ayakta, yoksa Amr mı?» diyene cevâben «Zeyd» gibi."},
 "tokens": [
  wayajuz(),
  hadhfuhu(),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«where»", "«-ında»"),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, HT], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ، وَخَبَرُهُ مَحْذُوفٌ: قَائِمٌ.", "«Zayd» — the mubtada, its khabar «standing» dropped.", "«Zeyd» — mübtedâ, haberi «ayakta» hazfedilmiş.", punct="،"),
  tok("لِمَنْ", "man", "pron", [K, HJ, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who»", "«… diyene»", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man", "pron")]),
  tok("قَالَ", "qala", "verb", [K, FL, HV, MAW], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ مَنْ.", "«asked»", "«diyen»", punct=":"),
  tok("أَزَيْدٌ", "zayd", "propn", [K, IST, MK], "لَفْظٌ مَحْكِيٌّ: الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«is Zayd» — the question's hamza, the mubtada.", "«Zeyd mi» — istifhâm hemzesi, mübtedâ.", segments=[seg("أَ", "a-istifham", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«standing»", "«ayakta»"),
  tok("أَمْ", "am", "part", [K, AT, IST], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ.", "«or» — the connected am.", "«yoksa» — muttasıl em."),
  tok("عَمْرٌو", "amr-name", "propn", [K, AT, MK], "مَعْطُوفٌ عَلَى زَيْدٌ مَرْفُوعٌ — وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ.", "«ʿAmr» — joined to Zayd; the silent wāw.", "«Amr» — Zeyd'e atıf; yazıdaki vâv.", punct="؟"),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "kurr": G("kurr", "كُرّ", "ك ر ر", "noun", "a kurr — a large dry measure of grain", "kür — büyük bir tahıl ölçeği", 3),
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
print("izhar ch29 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "qama", "qala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "خَبَرُ الْمُبْتَدَإِ: تَعْرِيفُهُ وَتَعَدُّدُهُ وَجُمْلَتُهُ وَعَائِدُهُ وَحَذْفُهُ", "en": "The khabar of the mubtadaʾ: its definition, multiplicity, sentence form, returning pronoun and dropping", "tr": "Mübtedânın haberi: tarifi, taaddüdü, cümle oluşu, âidi ve hazfi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المرفوعات: خبر المبتدأ", "الكافية لابن الحاجب — الخبر", "شرح قطر الندى لابن هشام — الخبر وأحكامه"],
 "amil": "the fourth marfūʿ, the khabar, is what is stripped of the governors of wording and predicated, other than the verb and its sense (قَائِمٌ in زَيْدٌ قَائِمٌ); it may be multiplied (زَيْدٌ قَائِمٌ قَاعِدٌ); it may be a nominal or verbal sentence with a pronoun returning to the mubtadaʾ unless it is the khabar of the pronoun of the matter (زَيْدٌ أَبُوهُ قَائِمٌ أَوْ قَامَ أَبُوهُ), the returner droppable on a clue (الْبُرُّ الْكُرُّ بِسِتِّينَ); its origin is to be a nakira, though it may be definite (اللهُ إِلٰهُنَا); it may be dropped on a clue (زَيْدٌ answering أَزَيْدٌ قَائِمٌ أَمْ عَمْرٌو)",
 "question": {
  "en": ["What is the khabar? What is stripped of the governors of wording and predicated, other than the verb and what has its sense: قَائِمٌ in زَيْدٌ قَائِمٌ.",
         "May it be multiplied? Yes — زَيْدٌ قَائِمٌ قَاعِدٌ: two khabars of one mubtadaʾ.",
         "May it be a sentence? Yes, nominal or verbal — and then a pronoun returning to the mubtadaʾ is a must (زَيْدٌ أَبُوهُ قَائِمٌ، زَيْدٌ قَامَ أَبُوهُ), unless the sentence is the khabar of the pronoun of the matter (هُوَ زَيْدٌ قَائِمٌ).",
         "May the returner be dropped? On a clue: الْبُرُّ الْكُرُّ بِسِتِّينَ — that is, الْكُرُّ مِنْهُ بِسِتِّينَ.",
         "Is the khabar definite or indefinite? Its origin is to be a nakira, but it may be definite: اللهُ إِلٰهُنَا.",
         "May the khabar be dropped? Where a clue stands: زَيْدٌ in answer to أَزَيْدٌ قَائِمٌ أَمْ عَمْرٌو — the dropped khabar is قَائِمٌ.",
         "What does the engine READ here? The DabtEngine raises the nakira after the mubtadaʾ as its khabar and a second nakira after it as a second khabar, reads أَبُوهُ after زَيْدٌ as a second mubtadaʾ or as the doer of قَامَ by the five nouns' wāw, raises إِلٰهُنَا after اللهُ as a definite khabar, and reads the citation قَائِمٌ فِي زَيْدٌ قَائِمٌ word by word."],
  "tr": ["Haber nedir? Lafzî âmillerden soyutlanmış, kendisiyle isnâd yapılan, fiil ve fiil mânâsındaki dışındaki şey: Zeydün kâimün'deki kâimün.",
         "Taaddüd edebilir mi? Evet — Zeydün kâimün kâidün: bir mübtedânın iki haberi.",
         "Cümle olabilir mi? Evet, isim ya da fiil cümlesi — o zaman mübtedâya dönen bir zamir zorunludur (Zeydün ebûhu kâimün, Zeydün kâme ebûhu); şe'n zamirinin haberi ise hariç (hüve Zeydün kâimün).",
         "Âid hazfedilebilir mi? Karîne ile: el-bürrü'l-kürrü bi-sittîne — yani el-kürrü minhü bi-sittîne.",
         "Haber ma'rife mi nekre mi? Aslı nekredir, ama ma'rife olabilir: Allâhu ilâhunâ.",
         "Haber hazfedilebilir mi? Karîne bulununca: e-Zeydün kâimün em Amrun sorusuna cevâben Zeydün — hazfedilen haber kâimün.",
         "Motor burada neyi OKUR? DabtEngine mübtedâdan sonraki nekreyi haber, ardındaki ikinci nekreyi ikinci haber olarak ref' eder; Zeydün'den sonraki ebûhu'yu ikinci mübtedâ ya da beş isimden biri olarak vâv ile kâme'nin fâili okur; Allâhu'dan sonraki ilâhunâ'yı ma'rife haber olarak ref' eder; kâimün fî Zeydün kâimün alıntısını kelime kelime okur."],
 },
 "plain": {"en": "The khabar is what is predicated of the subject: «standing» in «Zayd is standing». There may be two, or a whole sentence, which then needs a pronoun pointing back to the subject: «Zayd, his father is standing». It is usually indefinite; the pointer or the khabar may be dropped when the context is clear.",
           "tr": "Öznenin yüklemi haberdir: «Zeyd ayaktadır»daki «ayakta». İki tane olabilir; haber bir cümle de olabilir, o zaman özneye dönen bir zamir gerekir: «Zeyd, babası ayaktadır». Haber çoğunlukla nekredir ama ma'rife olabilir; bağlam açıksa dönen zamir de haber de düşürülebilir."},
 "explanation": {"en": "The fourth marfūʿ is the khabar of the mubtadaʾ: what is stripped of the governors of wording and predicated, other than the verb and what has its sense (قَائِمٌ in زَيْدٌ قَائِمٌ). It may be multiplied (زَيْدٌ قَائِمٌ قَاعِدٌ); it may be a nominal or a verbal sentence, and then a pronoun returning to the mubtadaʾ is a must unless the sentence is the khabar of the pronoun of the matter (زَيْدٌ أَبُوهُ قَائِمٌ أَوْ قَامَ أَبُوهُ); the returner may be dropped on a clue (الْبُرُّ الْكُرُّ بِسِتِّينَ، أَيْ مِنْهُ). Its origin is to be indefinite, though it may be definite (اللهُ إِلٰهُنَا); and it may be dropped where a clue stands (زَيْدٌ to one who asked أَزَيْدٌ قَائِمٌ أَمْ عَمْرٌو).",
                 "tr": "Dördüncü merfû mübtedânın haberidir: lafzî âmillerden soyutlanmış, kendisiyle isnâd yapılan, fiil ve fiil mânâsındaki dışındaki şey (Zeydün kâimün'deki kâimün). Taaddüdü câizdir (Zeydün kâimün kâidün); isim ya da fiil cümlesi olabilir, o zaman şe'n zamirinin haberi değilse mübtedâya dönen bir zamir zorunludur (Zeydün ebûhu kâimün ev kâme ebûhu); âid karîne ile hazfedilebilir (el-bürrü'l-kürrü bi-sittîne, ey minhü). Aslı nekre olmasıdır, ma'rife de olabilir (Allâhu ilâhunâ); karîne bulununca hazfi câizdir (e-Zeydün kâimün em Amrun diyene Zeydün)."},
 "examples": [
  {"ar": "قَائِمٌ فِي: زَيْدٌ قَائِمٌ", "en": "the khabar defined", "tr": "haberin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "زَيْدٌ قَائِمٌ قَاعِدٌ", "en": "the khabar multiplied", "tr": "haberin taaddüdü", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "زَيْدٌ أَبُوهُ قَائِمٌ أَوْ قَامَ أَبُوهُ", "en": "the sentence as khabar with its returning pronoun", "tr": "âidiyle cümle haber", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "الْبُرُّ الْكُرُّ بِسِتِّينَ، أَيْ مِنْهُ", "en": "the returner dropped on a clue", "tr": "karîne ile hazfedilen âid", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "اللهُ إِلٰهُنَا", "en": "the definite khabar", "tr": "ma'rife haber", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "زَيْدٌ لِمَنْ قَالَ أَزَيْدٌ قَائِمٌ أَمْ عَمْرٌو", "en": "the khabar dropped on a clue", "tr": "karîne ile hazfedilen haber", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٌ أَبُو عَمْرٍو قَائِمٌ (as the khabar of زَيْدٌ)", "right": "زَيْدٌ أَبُوهُ قَائِمٌ", "why": {"en": "a sentence serving as khabar must carry a pronoun returning to the mubtadaʾ", "tr": "haber olan cümle mübtedâya dönen bir zamir taşımalıdır"}},
  {"wrong": "زَيْدٌ قَائِمًا", "right": "زَيْدٌ قَائِمٌ", "why": {"en": "the khabar of the mubtadaʾ is marfūʿ; naṣb would make it a ḥāl of a verb that is not there", "tr": "mübtedânın haberi merfûdur; nasb onu olmayan bir fiilin hâli yapardı"}},
  {"wrong": "الْبُرُّ الْكُرُّ بِسِتِّينَ read with no returner at all", "right": "الْكُرُّ مِنْهُ بِسِتِّينَ — the returner is estimated", "why": {"en": "the dropping is allowed only because the clue restores it", "tr": "hazif ancak karîne onu geri getirdiği için câizdir"}},
 ],
}
ADD_EN = (" Chapter 29 (print pp. 129-130): the fourth marfūʿ, the khabar — defined (s1), multiplied (s2), as a nominal or verbal sentence with its returning pronoun (s3), the returner dropped on a clue (s4), indefinite in origin and sometimes definite (s5), dropped on a clue (s6).")
ADD_TR = (" Yirmi dokuzuncu bab (baskı s. 129-130): dördüncü merfû haber — tarifi (s1), taaddüdü (s2), âidiyle isim veya fiil cümlesi oluşu (s3), âidin karîne ile hazfi (s4), aslı nekre bazen ma'rife (s5), karîne ile hazfi (s6).")
write_out(29, S, TITLE, ADD_EN, ADD_TR, "pp. 129-130", GLOSS_ADD, notes=(NOTE,),
          related=((K28, [K]), (MK, [K]), (HT, [K]), (KN, [K]), ("five-nouns", [K])))
report(29, S, GLOSS_ADD, (NOTE,))
