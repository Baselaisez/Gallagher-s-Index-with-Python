# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 22: each of the doer and the deputy is of two sorts, PRONOUN and NOUN; the pronoun hidden or
# apparent; the hidden one hidden BY NECESSITY (it may never be shown and its governor is predicated of nothing else) or BY CHOICE
# (its governor is predicated now of it, now of an apparent noun). The first lives in the two speakers and the single masculine
# addressee of the non-past (أَضْرِبُ، نَضْرِبُ، تَضْرِبُ), the command noun-verb (نَزَالِ، صَهْ، مَهْ), the afʿal of preference outside the
# kuḥl case (زَيْدٌ أَفْضَلُ مِنْ عَمْرٍو), the participles and their like, the ṣifa mushabbaha and the settled ẓarf when the condition
# of their governing an apparent doer is absent (جَاءَنِي ضَارِبٌ … فِي الدَّارِ زَيْدٌ), the dual and sound plural of the participles
# absolutely (رَجُلَانِ ضَارِبَانِ، رِجَالٌ ضَارِبُونَ), and عَدَا، خَلَا، مَا عَدَا، مَا خَلَا، لَيْسَ، لَا يَكُونُ of the exception. Print pp. 122–123.
#   python3 author_izhar_ch22.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-fail-al-mudmar-al-mustatir-wujuban"
K21 = "al-marfuat-al-fail-wa-naibuh"
TITLE = {"ar": "الْفَاعِلُ مُضْمَرٌ وَمُظْهَرٌ: الْمُسْتَتِرُ وُجُوبًا", "en": "The doer as pronoun or as noun: the pronoun hidden by necessity", "tr": "Fâil zamir ve isim: vücûben müstetir zamir"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; F8 = "form-viii-verbs"; MSD = "masdar"; LN = "la-nafiya"; JT = "jam-taksir"; MQ = "ism-maqsur-manqus"; MR = "mudari-marfu"; MAW = "ism-mawsul"; MM = "maful-mutlaq"
MST = "istithna"; IFL = "ism-fil"; MNF = "mana-al-fil"; NSB = "ism-mansub"; TF = "ism-tafdil"; SM = "sifa-mushabbaha"; JMS = "jam-mudhakkar-salim"; LJ = "lam-jazim"; IDH = "idha-shartiyya"; DM = K; AQ = "al-amil-wa-aqsamuh"; YM = "ya-al-mutakallim"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def jaani(): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV, YM], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")])
def istitar(punct="،"): return tok("الِاسْتِتَارِ", "istitar", "noun", [K, ID, MSD, F8, DM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اسْتَتَرَ: الْخَفَاءُ.", "«hiding»", "«gizlenme»", punct=punct)
def bihaythu(): return tok("بِحَيْثُ", "haythu", "noun", [K, HJ, MF], "الْبَاءُ حَرْفُ جَرٍّ، وَحَيْثُ ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَالْجُمْلَةُ بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«such that»", "«öyle ki»", segments=[seg("بِ", "bi", "prep"), seg("حَيْثُ", "haythu", "noun")])
def yusnad(): return tok("يُسْنَدُ", "asnada", "verb", [K, NF, F4, MR], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is predicated»", "«isnâd edilir»")
def amiluhu(): return tok("عَامِلُهُ", "amil-governor", "noun", [K, NF, ID, AQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor» — the deputy doer.", "«âmili» — nâib-i fâil.", segments=[seg("عَامِلُ", "amil-governor", "noun"), pr3ms()])
def ilayhi(punct=None): return tok("إِلَيْهِ", "ila", "prep", [K, HJ], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«to it»", "«ona»", punct=punct, segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()])
def aydan(): return tok("أَيْضًا", "aydan", "noun", [K, MM], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ.", "«too»", "«da»")
def qisman(punct=":"): return tok("قِسْمَانِ", "qism", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two sorts» — the khabar in the dual.", "«iki kısım» — tesniye haber.", punct=punct)

# ----------- s1 — each of the two: pronoun and noun
S.append({"id": "s1", "translation": {"en": "Each of the two is of two sorts: a pronoun and an apparent noun.", "tr": "Her biri iki kısımdır: muzmar (zamir) ve muzhar (açık isim)."},
 "tokens": [
  tok("كُلٌّ", "kull", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ — كُلُّ وَاحِدٍ.", "«each» — the mubtada.", "«her biri» — mübtedâ."),
  tok("مِنْهُمَا", "min", "prep", [K, HJ, NA], "مِنْ حَرْفُ جَرٍّ، وَهُمَا فِي مَحَلِّ جَرٍّ — صِفَةٌ لِكُلٍّ: الْفَاعِلِ وَنَائِبِهِ.", "«of the two» — the doer and the deputy.", "«ikisinden» — fâil ve nâibi.", segments=[seg("مِنْ", "min", "prep"), seg("هُمَا", "pron-3d", "pron")]),
  qisman(),
  tok("مُضْمَرٌ", "mudmar", "noun", [K, MK, HT, IMF, DM], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ: أَحَدُهُمَا مُضْمَرٌ — الضَّمِيرُ.", "«a pronoun» — the khabar of a dropped «one of them».", "«muzmar» — hazfedilmiş «biri»nin haberi: zamir."),
  tok("وَمُظْهَرٌ", "muzhar", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمُظْهَرٌ مَعْطُوفٌ مَرْفُوعٌ — الِاسْمُ الظَّاهِرُ.", "«and an apparent noun»", "«ve muzhar» — açık isim.", punct=".", segments=wa("مُظْهَرٌ", "muzhar", "noun")),
 ]})
# ----------- s2 — the pronoun: hidden and apparent
S.append({"id": "s2", "translation": {"en": "The pronoun too is of two sorts: hidden and apparent.", "tr": "Zamir de iki kısımdır: müstetir (gizli) ve bâriz (açık)."},
 "tokens": [
  tok("فَالْمُضْمَرُ", "mudmar", "noun", [K, AT, MK, DM], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمُضْمَرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the pronoun» — the mubtada.", "«zamir» — mübtedâ.", segments=fa("الْمُضْمَرُ", "mudmar", "noun")),
  aydan(),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the khabar.", "«üzere» — haber."),
  tok("قِسْمَيْنِ", "qism", "noun", [K, HJ, MTH], "مَجْرُورٌ بِعَلَى بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two sorts»", "«iki kısım»", punct=":"),
  tok("مُسْتَتِرٌ", "mustatir", "noun", [K, MK, HT, IFA, DM], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ: أَحَدُهُمَا مُسْتَتِرٌ.", "«hidden»", "«müstetir»"),
  tok("وَبَارِزٌ", "bariz", "noun", [K, AT, IFA, DM], "الْوَاوُ عَاطِفَةٌ، وَبَارِزٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and apparent»", "«ve bâriz»", punct=".", segments=wa("بَارِزٌ", "bariz", "noun")),
 ]})
# ----------- s3 — the hidden: by necessity
S.append({"id": "s3", "translation": {"en": "The hidden too is of two sorts: hidden by necessity, such that it may not be shown and its governor is predicated of nothing but it;", "tr": "Müstetir de iki kısımdır: vücûben müstetir — öyle ki açığa çıkarılması câiz değildir ve âmili ondan başkasına isnâd edilmez;"},
 "tokens": [
  tok("فَالْمُسْتَتِرُ", "mustatir", "noun", [K, AT, MK, DM], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمُسْتَتِرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the hidden» — the mubtada.", "«müstetir» — mübtedâ.", segments=fa("الْمُسْتَتِرُ", "mustatir", "noun")),
  aydan(),
  qisman(),
  tok("وَاجِبُ", "wajib", "noun", [K, MK, HT, ID, IFA], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ: أَحَدُهُمَا وَاجِبُ الِاسْتِتَارِ.", "«necessarily» — the khabar of a dropped «one of them».", "«vâcib» — hazfedilmiş «biri»nin haberi."),
  istitar(),
  bihaythu(),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«değil»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ.", "«it is allowed»", "«câizdir»"),
  tok("إِبْرَازُهُ", "ibraz", "noun", [K, FL, ID, MSD, F4], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ أَبْرَزَ: إِظْهَارُهُ.", "«showing it» — the doer.", "«onu açığa çıkarmak» — fâil.", segments=[seg("إِبْرَازُ", "ibraz", "noun"), pr3ms()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«nor»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  yusnad(),
  amiluhu(),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ — مُفَرَّغٌ.", "«but»", "«ancak»"),
  ilayhi(punct="؛"),
 ]})
# ----------- s4 — the hidden: by choice
S.append({"id": "s4", "translation": {"en": "and hidden by choice, such that its governor is predicated now of it and now of an apparent noun.", "tr": "ve cevâzen müstetir — öyle ki âmili bazen ona, bazen de açık bir isme isnâd edilir."},
 "tokens": [
  tok("وَجَائِزُ", "jaiz", "noun", [K, AT, ID, IFA], "الْوَاوُ عَاطِفَةٌ، وَجَائِزُ مَعْطُوفٌ عَلَى وَاجِبُ مَرْفُوعٌ، مُضَافٌ.", "«and optionally»", "«ve câiz»", segments=wa("جَائِزُ", "jaiz", "noun")),
  istitar(),
  bihaythu(),
  yusnad(),
  amiluhu(),
  tok("تَارَةً", "tara", "noun", [K, MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ — مَرَّةً.", "«now» — once.", "«bazen» — bir kez."),
  ilayhi(),
  tok("وَتَارَةً", "tara", "noun", [K, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَتَارَةً ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ.", "«and now»", "«ve bazen»", segments=wa("تَارَةً", "tara", "noun")),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("اسْمٍ", "ism", "noun", [K, HJ, NA], "مَجْرُورٌ بِإِلَى.", "«a noun»", "«bir isme»"),
  tok("ظَاهِرٍ", "zahir", "noun", [K, NA, IFA], "نَعْتٌ مَجْرُورٌ.", "«apparent»", "«açık»", punct="."),
 ]})
# ----------- s5 — the first: the speakers and the single masculine addressee of the non-past
S.append({"id": "s5", "translation": {"en": "The first is in the two speakers and the single masculine addressee of the non-past, as in «I strike», «we strike», «you strike»;", "tr": "İlki, mâzî dışındaki iki mütekellimde ve müfred müzekker muhâtabdadır: «vururum», «vururuz», «vurursun» gibi;"},
 "tokens": [
  tok("وَالْأَوَّلُ", "awwal", "noun", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ — وَاجِبُ الِاسْتِتَارِ.", "«the first» — the mubtada: the one hidden by necessity.", "«ilki» — mübtedâ: vücûben müstetir.", segments=wa("الْأَوَّلُ", "awwal", "noun")),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the khabar.", "«-de» — haber."),
  tok("الْمُتَكَلِّمَيْنِ", "mutakallim", "noun", [K, HJ, MTH, IFA, DM], "مَجْرُورٌ بِفِي بِالْيَاءِ لِأَنَّهُ مُثَنًّى — الْمُتَكَلِّمُ وَحْدَهُ وَالْمُتَكَلِّمُ مَعَ غَيْرِهِ.", "«the two speakers» — the speaker alone and with others.", "«iki mütekellim» — tek başına ve başkalarıyla.", punct="،"),
  tok("وَالْمُخَاطَبِ", "mukhatab", "noun", [K, AT, IMF, DM], "الْوَاوُ عَاطِفَةٌ، وَالْمُخَاطَبِ مَعْطُوفٌ مَجْرُورٌ.", "«and the addressee»", "«ve muhâtab»", segments=wa("الْمُخَاطَبِ", "mukhatab", "noun")),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«single»", "«müfred»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, NA, IMF], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«masculine»", "«müzekker»"),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("الْمَاضِي", "madi", "noun", [K, ID, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — الْمُضَارِعُ وَالْأَمْرُ.", "«the past» — so the muḍāriʿ and the imperative.", "«mâzî» — yani muzâri ve emir.", punct="،"),
  nahw(),
  tok("أَضْرِبُ", "daraba", "verb", [K, FL, MR, DM], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا.", "«I strike» — the doer hidden: I.", "«vururum» — gizli fâil: ben."),
  tok("وَنَضْرِبُ", "daraba", "verb", [K, AT, FL, MR, DM], "الْوَاوُ عَاطِفَةٌ، وَنَضْرِبُ فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ.", "«and we strike» — the doer hidden: we.", "«ve vururuz» — gizli fâil: biz.", segments=wa("نَضْرِبُ", "daraba", "verb")),
  tok("وَتَضْرِبُ", "daraba", "verb", [K, AT, FL, MR, DM], "الْوَاوُ عَاطِفَةٌ، وَتَضْرِبُ فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«and you strike» — the doer hidden: you.", "«ve vurursun» — gizli fâil: sen.", punct="؛", segments=wa("تَضْرِبُ", "daraba", "verb")),
 ]})
# ----------- s6 — the command noun-verb
S.append({"id": "s6", "translation": {"en": "and in the command noun-verb, as in «come down!», «hush!», «stop!»;", "tr": "ve emir isim fiilinde: «in!», «sus!», «dur!» gibi;"},
 "tokens": [
  tok("وَاسْمِ", "ism", "noun", [K, AT, ID, IFL], "الْوَاوُ عَاطِفَةٌ، وَاسْمِ مَعْطُوفٌ عَلَى الْمُتَكَلِّمَيْنِ مَجْرُورٌ، مُضَافٌ.", "«and the noun of» — joined to the speakers.", "«ve ismi» — mütekellimlere atıf.", segments=wa("اسْمِ", "ism", "noun")),
  tok("فِعْلِ", "fil", "noun", [K, ID, IFL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the verb of»", "«fiil»"),
  tok("الْأَمْرِ", "amr", "noun", [K, ID, IFL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فِعْلِ الْأَمْرِ.", "«command» — the command noun-verb.", "«emir» — emir isim fiili.", punct="،"),
  nahw(),
  tok("نَزَالِ", "nazal", "noun", [K, IFL, MNF, DM], "لَفْظٌ مَحْكِيٌّ: اسْمُ فِعْلِ أَمْرٍ مَبْنِيٌّ عَلَى الْكَسْرِ بِمَعْنَى انْزِلْ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«come down!» — a noun-verb on the kasra, its doer hidden: you.", "«in!» — kesre üzere mebnî isim fiil, gizli fâil: sen."),
  tok("وَصَهْ", "sah", "noun", [K, AT, IFL, MNF, DM], "الْوَاوُ عَاطِفَةٌ، وَصَهْ اسْمُ فِعْلِ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ بِمَعْنَى اسْكُتْ.", "«and hush!» — be silent.", "«ve sus!» — sükût et.", segments=wa("صَهْ", "sah", "noun")),
  tok("وَمَهْ", "mah", "noun", [K, AT, IFL, MNF, DM], "الْوَاوُ عَاطِفَةٌ، وَمَهْ اسْمُ فِعْلِ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ بِمَعْنَى اكْفُفْ.", "«and stop!» — desist.", "«ve dur!» — vazgeç.", punct="؛", segments=wa("مَهْ", "mah", "noun")),
 ]})
# ----------- s7 — the afʿal of preference outside the kuḥl case
S.append({"id": "s7", "translation": {"en": "and in the afʿal of preference outside the kuḥl case, as in «Zayd is better than ʿAmr»;", "tr": "ve kuhl meselesi dışındaki ism-i tafdîlde: «Zeyd Amr'dan daha üstündür» gibi;"},
 "tokens": [
  tok("وَأَفْعَلِ", "afal-wazn", "noun", [K, AT, ID, TF], "الْوَاوُ عَاطِفَةٌ، وَأَفْعَلِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ لِإِضَافَتِهِ، مُضَافٌ — وَزْنُ أَفْعَلَ.", "«and the afʿal of» — the pattern, declined by its annexation.", "«ve ef'ali» — izâfetle kesre alan vezin.", segments=wa("أَفْعَلِ", "afal-wazn", "noun")),
  tok("التَّفْضِيلِ", "tafdil", "noun", [K, ID, TF, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ التَّفْضِيلِ.", "«preference» — the comparative.", "«tafdîl» — ism-i tafdîl."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("مَسْأَلَةِ", "masala", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the case of»", "«meselesi»"),
  tok("الْكُحْلِ", "kuhl", "noun", [K, ID, TF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ: هُنَاكَ يَرْفَعُ ظَاهِرًا.", "«the kohl» — the one case where afʿal raises an apparent doer.", "«kuhl» — ism-i tafdîlin açık fâil ref' ettiği tek mesele.", punct="،"),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, TF], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("أَفْضَلُ", "afdal", "noun", [K, MK, TF, DM], "خَبَرٌ مَرْفُوعٌ — أَفْعَلُ تَفْضِيلٍ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: هُوَ.", "«better» — the khabar, its doer hidden: he.", "«daha üstün» — haber, gizli fâil: o."),
  tok("مِنْ", "min", "prep", [K, HJ, TF], "حَرْفُ جَرٍّ — مِنْ التَّفْضِيلِ.", "«than»", "«-den»"),
  tok("عَمْرٍو", "amr-name", "propn", [K, HJ], "مَجْرُورٌ بِمِنْ — وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ لِلْفَرْقِ بَيْنَهُ وَبَيْنَ عُمَرَ.", "«ʿAmr» — the silent wāw tells it from ʿUmar.", "«Amr» — yazıdaki vâv Ömer'den ayırmak için.", punct="؛"),
 ]})
# ----------- s8 — the participles, the ṣifa mushabbaha and the settled ẓarf without the condition of governing an apparent doer
S.append({"id": "s8", "translation": {"en": "and in the active and passive participle, what has their sense, the resembling adjective and the settled ẓarf, when the condition of their governing an apparent doer is not found — as in «there came to me one who strikes, or one struck, or a speaking lion, or a Hāshimī, or a handsome one», or as in «in the house is Zayd»;", "tr": "ve ism-i fâil, ism-i mef'ûl, onların mânâsında olan, sıfat-ı müşebbehe ve müstakar zarfta — açık fâilde amel etme şartı bulunmadığında: «bana vuran biri, ya vurulan biri, ya konuşan bir aslan, ya bir Hâşimî, ya güzel biri geldi» gibi; veya «evde Zeyd vardır» gibi;"},
 "tokens": [
  tok("وَاسْمِ", "ism", "noun", [K, AT, ID, IFA], "الْوَاوُ عَاطِفَةٌ، وَاسْمِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the noun of»", "«ve ismi»", segments=wa("اسْمِ", "ism", "noun")),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْفَاعِلِ.", "«the doer» — the active participle.", "«fâil» — ism-i fâil."),
  tok("وَاسْمِ", "ism", "noun", [K, AT, ID, IMF], "الْوَاوُ عَاطِفَةٌ، وَاسْمِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the noun of»", "«ve ismi»", segments=wa("اسْمِ", "ism", "noun")),
  tok("الْمَفْعُولِ", "maful-object", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَفْعُولِ.", "«the acted-upon» — the passive participle.", "«mef'ûl» — ism-i mef'ûl."),
  tok("وَمَا", "ma-mawsula", "pron", [K, AT, MAW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and what»", "«ve … olan»", segments=wa("مَا", "ma-mawsula", "pron")),
  tok("كَانَ", "kana", "verb", [K, KN, MAW], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — صِلَةُ مَا.", "«is» — the relative clause.", "«olan» — sıla."),
  tok("بِمَعْنَاهُمَا", "mana", "noun", [K, HJ, ID, MQ, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَاهُمَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ: الصِّيَغُ الْمُبَالَغَةُ وَنَحْوُهَا.", "«in their sense» — the khabar of kāna: the intensive forms and their like.", "«onların mânâsında» — kâne'nin haberi: mübâlağa sîgaları vb.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("وَالصِّفَةِ", "sifa", "noun", [K, AT, SM], "الْوَاوُ عَاطِفَةٌ، وَالصِّفَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the adjective»", "«ve sıfat»", segments=wa("الصِّفَةِ", "sifa", "noun")),
  tok("الْمُشَبَّهَةِ", "mushabbaha", "noun", [K, NA, SM, IMF], "نَعْتٌ مَجْرُورٌ — الصِّفَةُ الْمُشَبَّهَةُ بِاسْمِ الْفَاعِلِ.", "«resembling» — the adjective likened to the participle.", "«müşebbehe» — ism-i fâile benzeyen sıfat."),
  tok("وَالظَّرْفِ", "zarf", "noun", [K, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَالظَّرْفِ مَعْطُوفٌ مَجْرُورٌ.", "«and the ẓarf»", "«ve zarf»", segments=wa("الظَّرْفِ", "zarf", "noun")),
  tok("الْمُسْتَقِرِّ", "mustaqirr", "noun", [K, NA, IFA, MF], "نَعْتٌ مَجْرُورٌ — الظَّرْفُ الَّذِي تَعَلَّقَ بِمَحْذُوفٍ عَامٍّ: مُسْتَقِرٌّ أَوْ كَائِنٌ، فَفِيهِ ضَمِيرٌ.", "«settled» — the ẓarf hanging on a dropped «settled», so it holds a pronoun.", "«müstakar» — hazfedilmiş «müstakırr»e bağlı zarf; içinde zamir vardır.", punct="،"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-dığında»"),
  tok("لَمْ", "lam", "part", [K, LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("يُوجَدْ", "wajada", "verb", [K, NF, LJ, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ — مِثَالٌ وَاوِيٌّ.", "«is found»", "«bulunmaz»"),
  tok("شَرْطُ", "shart", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«the condition of» — the deputy doer.", "«şartı» — nâib-i fâil."),
  tok("عَمَلِهِنَّ", "amal-governing", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهِنَّ مُضَافٌ إِلَيْهِ — الصِّفَاتُ الْمَذْكُورَةُ.", "«their governing» — the adjectives named.", "«onların amel etmesi» — zikredilen sıfatlar.", segments=[seg("عَمَلِ", "amal-governing", "noun"), seg("هِنَّ", "pron-3fp", "pron")]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-de»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, HJ, FL], "مَجْرُورٌ بِفِي.", "«the doer»", "«fâil»"),
  tok("الظَّاهِرِ", "zahir", "noun", [K, NA, IFA], "نَعْتٌ مَجْرُورٌ.", "«apparent»", "«açık»", punct="،"),
  nahw(),
  jaani(),
  tok("ضَارِبٌ", "darib", "noun", [K, FL, IFA, DM], "فَاعِلٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ لَمْ يَعْتَمِدْ، فَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا.", "«one who strikes» — a participle leaning on nothing: its doer hidden.", "«vuran» — dayanağı olmayan ism-i fâil: fâili gizli."),
  aw(),
  tok("مَضْرُوبٌ", "madrub", "noun", [K, AT, IMF, DM], "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ، وَنَائِبُ فَاعِلِهِ مُسْتَتِرٌ وُجُوبًا.", "«one struck»", "«vurulan»"),
  aw(),
  tok("أَسَدٌ", "asad", "noun", [K, AT], "مَعْطُوفٌ مَرْفُوعٌ.", "«a lion»", "«bir aslan»"),
  tok("نَاطِقٌ", "natiq", "noun", [K, NA, IFA, DM], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ، وَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا: هُوَ.", "«speaking» — a naʿt with its doer hidden.", "«konuşan» — fâili gizli na't."),
  aw(),
  tok("هَاشِمِيٌّ", "hashimi", "noun", [K, AT, NSB, DM], "مَعْطُوفٌ مَرْفُوعٌ — مَنْسُوبٌ بِمَعْنَى اسْمِ الْفَاعِلِ: مُنْتَسِبٌ.", "«a Hāshimī» — the nisba with the participle's sense.", "«bir Hâşimî» — ism-i fâil mânâsındaki nisbet."),
  aw(),
  tok("حَسَنٌ", "hasan-adj", "noun", [K, AT, SM, DM], "مَعْطُوفٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ، وَفَاعِلُهَا مُسْتَتِرٌ وُجُوبًا.", "«a handsome one» — the ṣifa mushabbaha.", "«güzel biri» — sıfat-ı müşebbehe.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  nahw(),
  tok("فِي", "fi", "prep", [K, HJ, MK], "لَفْظٌ مَحْكِيٌّ: حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الدَّارِ", "dar", "noun", [K, HJ, MK, MF, DM], "مَجْرُورٌ بِفِي — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ مُتَعَلِّقٌ بِمُسْتَقِرٍّ، فِيهِ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا.", "«the house» — the fronted khabar, the settled ẓarf holding its hidden pronoun.", "«ev» — öne alınmış haber, içinde gizli zamir.", ),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«Zayd» — the mubtada put after.", "«Zeyd» — sonraya bırakılmış mübtedâ.", punct="؛"),
 ]})
# ----------- s9 — the dual and sound plural of the participles, absolutely
S.append({"id": "s9", "translation": {"en": "and in the duals of the active and passive participle and their sound plural, absolutely — as in «there came to me two men striking, or struck», or «men striking, or struck»;", "tr": "ve ism-i fâil ile ism-i mef'ûlün tesniyesinde ve sâlim cem'inde — mutlak olarak: «bana vuran ya da vurulan iki adam geldi» veya «vuran ya da vurulan adamlar» gibi;"},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى فِي الْمُتَكَلِّمَيْنِ.", "«and in»", "«ve -de»", segments=wa("فِي", "fi", "prep")),
  tok("تَثْنِيَتَيِ", "tathniya", "noun", [K, HJ, MTH, ID], "مَجْرُورٌ بِفِي بِالْيَاءِ لِأَنَّهُ مُثَنًّى، مُضَافٌ — حُذِفَتْ نُونُهُ لِلْإِضَافَةِ وَكُسِرَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«the two duals of» — the dual's nūn dropped for the annexation.", "«iki tesniyesi» — izâfet için nûn düşmüş.", segments=[seg("تَثْنِيَتَيِ", "tathniya", "noun")]),
  tok("اسْمِ", "ism", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the noun of»", "«ismi»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâil»"),
  tok("وَالْمَفْعُولِ", "maful-object", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَالْمَفْعُولِ مَعْطُوفٌ عَلَى الْفَاعِلِ مَجْرُورٌ — اسْمِ الْمَفْعُولِ.", "«and the acted-upon»", "«ve mef'ûl»", segments=wa("الْمَفْعُولِ", "maful-object", "noun")),
  tok("وَجَمْعِهِمَا", "jam", "noun", [K, AT, ID, JMS], "الْوَاوُ عَاطِفَةٌ، وَجَمْعِهِمَا مَعْطُوفٌ عَلَى تَثْنِيَتَيِ مَجْرُورٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ.", "«and their plural»", "«ve cem'i»", segments=[seg("وَ", "wa", "conj"), seg("جَمْعِ", "jam", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("السَّالِمِ", "salim", "noun", [K, NA, JMS, IFA], "نَعْتٌ مَجْرُورٌ — جَمْعُ الْمُذَكَّرِ السَّالِمُ.", "«sound» — the sound masculine plural.", "«sâlim» — cem-i müzekker sâlim."),
  tok("مُطْلَقًا", "mutlaqan", "noun", [K, HL, IMF], "حَالٌ مَنْصُوبٌ — سَوَاءٌ وُجِدَ شَرْطُ الْعَمَلِ أَوْ لَا.", "«absolutely» — whether the condition is found or not.", "«mutlak olarak» — şart bulunsun bulunmasın.", punct="،"),
  nahw(),
  jaani(),
  tok("رَجُلَانِ", "rajul", "noun", [K, FL, MTH], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two men» — the doer.", "«iki adam» — fâil."),
  tok("ضَارِبَانِ", "darib", "noun", [K, NA, MTH, IFA, DM], "نَعْتٌ مَرْفُوعٌ بِالْأَلِفِ — وَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا: هُمَا.", "«striking» — its doer hidden: the two.", "«vuran» — gizli fâil: o ikisi."),
  aw(),
  tok("مَضْرُوبَانِ", "madrub", "noun", [K, AT, MTH, IMF, DM], "مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ.", "«struck»", "«vurulan»", punct="،"),
  aw(),
  tok("رِجَالٌ", "rijal", "noun", [K, AT, JT], "مَعْطُوفٌ عَلَى رَجُلَانِ مَرْفُوعٌ — جَمْعُ تَكْسِيرٍ.", "«men»", "«adamlar»"),
  tok("ضَارِبُونَ", "darib", "noun", [K, NA, JMS, IFA, DM], "نَعْتٌ مَرْفُوعٌ بِالْوَاوِ — وَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا: هُمْ.", "«striking» — its doer hidden: they.", "«vuran» — gizli fâil: onlar."),
  aw(),
  tok("مَضْرُوبُونَ", "madrub", "noun", [K, AT, JMS, IMF, DM], "مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ.", "«struck»", "«vurulan»", punct="؛"),
 ]})
# ----------- s10 — the verbs of exception
S.append({"id": "s10", "translation": {"en": "and in ʿadā, khalā, mā ʿadā, mā khalā, laysa and lā yakūnu in the chapter of exception — as in «the people came to me except Zayd», with ʿadā, laysa or lā yakūnu.", "tr": "ve istisnâ babındaki adâ, halâ, mâ adâ, mâ halâ, leyse ve lâ yekûnu'da: «topluluk bana geldi, Zeyd hariç» gibi — adâ, leyse veya lâ yekûnu ile."},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in»", "«ve -de»", segments=wa("فِي", "fi", "prep")),
  tok("عَدَا", "ada-except", "verb", [K, HJ, MST, DM], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ: فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ، وَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا.", "«ʿadā» — the exception verb.", "«adâ» — istisnâ fiili."),
  tok("وَخَلَا", "khala", "verb", [K, AT, MST, DM], "الْوَاوُ عَاطِفَةٌ، وَخَلَا فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ.", "«and khalā»", "«ve halâ»", segments=wa("خَلَا", "khala", "verb")),
  tok("وَمَا", "ma-masdariyya", "part", [K, AT, MST], "الْوَاوُ عَاطِفَةٌ، وَمَا مَصْدَرِيَّةٌ.", "«and mā»", "«ve mâ»", segments=wa("مَا", "ma-masdariyya", "part")),
  tok("عَدَا", "ada-except", "verb", [K, MST, DM], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ — مَا عَدَا.", "«ʿadā»", "«adâ»"),
  tok("وَمَا", "ma-masdariyya", "part", [K, AT, MST], "الْوَاوُ عَاطِفَةٌ، وَمَا مَصْدَرِيَّةٌ.", "«and mā»", "«ve mâ»", segments=wa("مَا", "ma-masdariyya", "part")),
  tok("خَلَا", "khala", "verb", [K, MST, DM], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ — مَا خَلَا.", "«khalā»", "«halâ»"),
  tok("وَلَيْسَ", "laysa", "verb", [K, AT, MST, KN, DM], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ لِلِاسْتِثْنَاءِ.", "«and laysa»", "«ve leyse»", segments=wa("لَيْسَ", "laysa", "verb")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and lā»", "«ve lâ»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَكُونُ", "kana", "verb", [K, MST, KN, HV, MR, DM], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — لَا يَكُونُ لِلِاسْتِثْنَاءِ.", "«yakūnu»", "«yekûnu»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("بَابِ", "bab", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the chapter of»", "«bâbı»"),
  tok("الِاسْتِثْنَاءِ", "istithna", "noun", [K, ID, MST, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«exception»", "«istisnâ»", punct="،"),
  nahw(),
  jaani(),
  tok("الْقَوْمُ", "qawm", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«the people» — the doer.", "«topluluk» — fâil."),
  tok("عَدَا", "ada-except", "verb", [K, MST, DM], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: هُوَ — يَعُودُ عَلَى الْبَعْضِ.", "«except» — its doer hidden: «some of them».", "«hariç» — gizli fâil: bazıları."),
  aw(),
  tok("لَيْسَ", "laysa", "verb", [K, AT, MST, KN, DM], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ وُجُوبًا: هُوَ.", "«laysa» — its ism hidden.", "«leyse» — ismi gizli."),
  aw(),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«değil»"),
  tok("يَكُونُ", "kana", "verb", [K, MST, KN, HV, MR, DM], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ وُجُوبًا: هُوَ.", "«is» — its ism hidden.", "«olur» — ismi gizli."),
  tok("زَيْدًا", "zayd", "propn", [K, MST, KN, MB], "مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ: مَفْعُولُ عَدَا وَخَبَرُ لَيْسَ وَلَا يَكُونُ.", "«Zayd» — the object of ʿadā, the khabar of laysa and lā yakūnu.", "«Zeyd» — adâ'nın mef'ûlü, leyse ve lâ yekûnu'nun haberi.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "muzhar": G("muzhar", "مُظْهَر", "ظ ه ر", "noun", "shown, an apparent noun as against the pronoun (ism mafʿūl of أَظْهَرَ)", "muzhar — zamirin karşıtı olan açık isim (azhere'nin ism-i mef'ûlü)", 4, form="IV"),
 "bariz": G("bariz", "بَارِز", "ب ر ز", "noun", "apparent, visible — the pronoun that shows (ism fāʿil of بَرَزَ)", "bâriz — görünen zamir (bereze'nin ism-i fâili)", 4),
 "istitar": G("istitar", "اسْتِتَار", "س ت ر", "noun", "hiding, concealment (maṣdar of اسْتَتَرَ) — وَاجِبُ الِاسْتِتَارِ، جَائِزُ الِاسْتِتَارِ", "istitâr — gizlenme (istetere'nin mastarı)", 4, form="VIII"),
 "ibraz": G("ibraz", "إِبْرَاز", "ب ر ز", "noun", "bringing out, showing (maṣdar of أَبْرَزَ)", "ibrâz — açığa çıkarma (ebreze'nin mastarı)", 4, form="IV"),
 "nazal": G("nazal", "نَزَالِ", "ن ز ل", "noun", "«come down!» — a command noun-verb on the pattern فَعَالِ, built on the kasra", "nezâli — «in!» (fe'âli vezninde, kesre üzere mebnî emir isim fiili)", 5),
 "sah": G("sah", "صَهْ", "ص ه", "noun", "«hush!» — a command noun-verb: be silent", "sah — «sus!» (emir isim fiili)", 5),
 "mah": G("mah", "مَهْ", "م ه", "noun", "«stop!» — a command noun-verb: desist", "meh — «dur!» (emir isim fiili)", 5),
 "mustaqirr": G("mustaqirr", "مُسْتَقِرّ", "ق ر ر", "noun", "settled — the ẓarf hanging on a dropped general verb (ism fāʿil of اسْتَقَرَّ)", "müstakırr — hazfedilmiş umûmî fiile bağlı zarf (istekarra'nın ism-i fâili)", 4, form="X"),
 "hasan-adj": G("hasan-adj", "حَسَن", "ح س ن", "noun", "handsome, good — a ṣifa mushabbaha", "güzel, iyi — sıfat-ı müşebbehe", 2),
 "afal-wazn": G("afal-wazn", "أَفْعَل", "ف ع ل", "noun", "the pattern afʿal — of preference (أَفْضَلُ) and of colour and defect (أَحْمَرُ): a diptote", "ef'al vezni — tafdîl (efdalü) ve renk-kusur (ahmeru): gayr-ı munsarif", 4),
 "mutlaqan": G("mutlaqan", "مُطْلَقًا", "ط ل ق", "noun", "absolutely, without restriction (ism mafʿūl of أَطْلَقَ as a ḥāl)", "mutlak olarak — kayıtsız (atlaka'nın ism-i mef'ûlü, hâl)", 3, form="IV"),
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
print("izhar ch22 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("daraba", "jaa", "kana", "asnada", "wajada", "jaaza", "ada-except", "khala", "laysa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْفَاعِلُ وَنَائِبُهُ مُضْمَرٌ وَمُظْهَرٌ: الضَّمِيرُ الْمُسْتَتِرُ وُجُوبًا وَمَوَاضِعُهُ", "en": "The doer and its deputy as pronoun or noun: the pronoun hidden by necessity and its places", "tr": "Fâil ve nâibi zamir ve isim: vücûben müstetir zamir ve yerleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الفاعل: المضمر والمظهر", "الكافية لابن الحاجب — المضمر", "شرح قطر الندى لابن هشام — الضمير المستتر وجوبا وجوازا"],
 "amil": "the doer and the deputy are each a pronoun or an apparent noun; the pronoun is hidden or apparent; the hidden one is hidden by necessity (never shown, its governor predicated of nothing else) or by choice (its governor predicated now of it, now of an apparent noun); by necessity in the two speakers and the single masculine addressee of the non-past, the command noun-verb, the afʿal of preference outside the kuḥl case, the participles and their like, the ṣifa mushabbaha and the settled ẓarf without the condition of governing an apparent doer, the dual and sound plural of the participles absolutely, and عَدَا، خَلَا، مَا عَدَا، مَا خَلَا، لَيْسَ، لَا يَكُونُ of the exception",
 "question": {
  "en": ["How are the doer and the deputy each divided? Into a pronoun (مُضْمَر) and an apparent noun (مُظْهَر); the pronoun into hidden (مُسْتَتِر) and apparent (بَارِز).",
         "What is the pronoun hidden by necessity? One that may never be shown, and whose governor is predicated of nothing but it — وَاجِبُ الِاسْتِتَارِ.",
         "And by choice? One whose governor is predicated now of it and now of an apparent noun — جَائِزُ الِاسْتِتَارِ.",
         "Where is the necessary hiding found in the verb? In the two speakers and the single masculine addressee of the non-past: أَضْرِبُ، نَضْرِبُ، تَضْرِبُ — and in the command noun-verb: نَزَالِ، صَهْ، مَهْ.",
         "Where in the nouns? In the afʿal of preference outside the kuḥl case (زَيْدٌ أَفْضَلُ مِنْ عَمْرٍو); in the participles, what has their sense, the ṣifa mushabbaha and the settled ẓarf when the condition of their governing an apparent doer is absent (جَاءَنِي ضَارِبٌ … فِي الدَّارِ زَيْدٌ); and in the dual and sound plural of the participles absolutely (رَجُلَانِ ضَارِبَانِ، رِجَالٌ ضَارِبُونَ).",
         "And in the exception? In عَدَا، خَلَا، مَا عَدَا، مَا خَلَا، لَيْسَ and لَا يَكُونُ: جَاءَنِي الْقَوْمُ عَدَا زَيْدًا — their doer or ism is a hidden «some of them».",
         "What does the engine READ here? The DabtEngine raises the noun after جَاءَنِي as the doer and the nakira adjectives after it as its naʿts, keeps the cited verbs, noun-verbs and exception verbs as quoted wording, and reads زَيْدًا after the exception verbs as the exceptee in naṣb."],
  "tr": ["Fâil ve nâib nasıl bölünür? Muzmar (zamir) ve muzhar (açık isim); zamir de müstetir (gizli) ve bâriz (açık).",
         "Vücûben müstetir zamir nedir? Hiç açığa çıkarılamayan ve âmili ondan başkasına isnâd edilmeyen zamir — vâcibü'l-istitâr.",
         "Cevâzen olan? Âmili bazen ona, bazen açık bir isme isnâd edilen — câizü'l-istitâr.",
         "Fiilde vücûben istitâr nerede? Mâzî dışındaki iki mütekellim ve müfred müzekker muhâtabda: adribu, nadribu, tadribu — ve emir isim fiilinde: nezâli, sah, meh.",
         "İsimlerde nerede? Kuhl meselesi dışındaki ism-i tafdîlde (Zeydün efdalü min Amrin); ism-i fâil, ism-i mef'ûl, onların mânâsındakiler, sıfat-ı müşebbehe ve müstakar zarfta — açık fâilde amel şartı yoksa (câenî dâribün … fi'd-dâri Zeydün); ism-i fâil ve mef'ûlün tesniye ve sâlim cem'inde mutlak olarak (racülâni dâribâni, ricâlün dâribûne).",
         "İstisnâda? Adâ, halâ, mâ adâ, mâ halâ, leyse ve lâ yekûnu'da: câeni'l-kavmü adâ Zeyden — fâilleri veya isimleri gizli «bazıları»dır.",
         "Motor burada neyi OKUR? DabtEngine câenî'den sonraki ismi fâil, ardındaki nekre sıfatları na't olarak ref' eder; zikredilen fiilleri, isim fiilleri ve istisnâ fiillerini nakledilmiş lafız olarak tutar; istisnâ fiillerinden sonraki Zeyden'i mansûb müstesnâ okur."],
 },
 "plain": {"en": "A verb's subject can be a pronoun or a noun, and a pronoun may hide inside the verb. Sometimes it must stay hidden: with «I strike» no noun can take its place. Sometimes it may show: with «he strikes» a noun can. This chapter lists where the hiding is forced, down to adjectives like «striking» and words like «except».",
           "tr": "Fiilin öznesi zamir ya da isim olabilir; zamir fiilin içinde gizli kalabilir. Bazen gizli kalmak zorundadır: «vururum» derken yerine isim gelemez. Bazen görünebilir: «vurur» derken bir isim gelebilir. Bu bölüm gizlenmenin zorunlu olduğu yerleri sayar; «vuran» gibi sıfatlar ve «hariç» gibi sözcükler de bunlardandır."},
 "explanation": {"en": "Each of the doer and the deputy is a pronoun or an apparent noun; the pronoun is hidden or apparent; the hidden one is hidden by necessity — it may never be shown, and its governor is predicated of nothing but it — or by choice — its governor is predicated now of it, now of an apparent noun. The necessary hiding lives in the two speakers and the single masculine addressee of the non-past (أَضْرِبُ، نَضْرِبُ، تَضْرِبُ), the command noun-verb (نَزَالِ، صَهْ، مَهْ), the afʿal of preference outside the kuḥl case (زَيْدٌ أَفْضَلُ مِنْ عَمْرٍو), the participles, what has their sense, the ṣifa mushabbaha and the settled ẓarf when the condition of their governing an apparent doer is absent (جَاءَنِي ضَارِبٌ أَوْ مَضْرُوبٌ أَوْ أَسَدٌ نَاطِقٌ أَوْ هَاشِمِيٌّ أَوْ حَسَنٌ، فِي الدَّارِ زَيْدٌ), the dual and sound plural of the participles absolutely (رَجُلَانِ ضَارِبَانِ، رِجَالٌ ضَارِبُونَ), and عَدَا، خَلَا، مَا عَدَا، مَا خَلَا، لَيْسَ، لَا يَكُونُ in the chapter of exception (جَاءَنِي الْقَوْمُ عَدَا زَيْدًا).",
                 "tr": "Fâil ve nâibin her biri zamir ya da açık isimdir; zamir müstetir ya da bârizdir; müstetir olan vücûben — hiç açığa çıkarılamaz, âmili ondan başkasına isnâd edilmez — ya da cevâzen — âmili bazen ona, bazen açık bir isme isnâd edilir — gizlidir. Vücûben istitâr: mâzî dışındaki iki mütekellim ve müfred müzekker muhâtab (adribu, nadribu, tadribu), emir isim fiili (nezâli, sah, meh), kuhl meselesi dışındaki ism-i tafdîl (Zeydün efdalü min Amrin), ism-i fâil, ism-i mef'ûl, onların mânâsındakiler, sıfat-ı müşebbehe ve müstakar zarf — açık fâilde amel şartı yoksa (câenî dâribün ev madrûbün ev esedün nâtıkun ev Hâşimiyyün ev hasenün, fi'd-dâri Zeydün), ism-i fâil ve mef'ûlün tesniye ve sâlim cem'i mutlak olarak (racülâni dâribâni, ricâlün dâribûne) ve istisnâ babında adâ, halâ, mâ adâ, mâ halâ, leyse, lâ yekûnu (câeni'l-kavmü adâ Zeyden)."},
 "examples": [
  {"ar": "كُلٌّ مِنْهُمَا قِسْمَانِ: مُضْمَرٌ وَمُظْهَرٌ", "en": "pronoun and apparent noun", "tr": "zamir ve açık isim", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَاجِبُ الِاسْتِتَارِ بِحَيْثُ لَا يَجُوزُ إِبْرَازُهُ", "en": "hidden by necessity", "tr": "vücûben müstetir", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "أَضْرِبُ وَنَضْرِبُ وَتَضْرِبُ", "en": "the speakers and the single masculine addressee", "tr": "mütekellimler ve müfred müzekker muhâtab", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "نَزَالِ وَصَهْ وَمَهْ", "en": "the command noun-verbs", "tr": "emir isim fiilleri", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "جَاءَنِي ضَارِبٌ أَوْ مَضْرُوبٌ أَوْ أَسَدٌ نَاطِقٌ", "en": "the participles without the condition of governing", "tr": "amel şartı olmayan ism-i fâil ve mef'ûl", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "جَاءَنِي الْقَوْمُ عَدَا أَوْ لَيْسَ أَوْ لَا يَكُونُ زَيْدًا", "en": "the exception verbs with their hidden doer", "tr": "gizli fâilli istisnâ fiilleri", "sourceStory": "izhar-al-asrar", "sentence": "s10"},
 ],
 "commonMistakes": [
  {"wrong": "أَضْرِبُ أَنَا زَيْدًا (أَنَا as the doer)", "right": "أَضْرِبُ زَيْدًا — the doer hidden by necessity", "why": {"en": "the speaker's doer may never be shown as the doer; an added أَنَا is a tawkīd", "tr": "mütekellimin fâili açığa çıkarılamaz; eklenen ene te'kîddir"}},
  {"wrong": "زَيْدٌ أَفْضَلُ أَبُوهُ مِنْ عَمْرٍو (an apparent doer of afʿal)", "right": "زَيْدٌ أَفْضَلُ مِنْ عَمْرٍو", "why": {"en": "the afʿal of preference raises an apparent doer only in the kuḥl case", "tr": "ism-i tafdîl açık fâili yalnız kuhl meselesinde ref' eder"}},
  {"wrong": "جَاءَنِي الْقَوْمُ عَدَا زَيْدٌ", "right": "جَاءَنِي الْقَوْمُ عَدَا زَيْدًا", "why": {"en": "ʿadā's doer is the hidden «some of them»; Zayd is its object in naṣb", "tr": "adâ'nın fâili gizli «bazıları»dır; Zeyd mansûb mef'ûldür"}},
 ],
}
ADD_EN = (" Chapter 22 (print pp. 122-123): the doer and the deputy each a pronoun or an apparent noun (s1), the pronoun hidden or apparent (s2), hidden by necessity (s3) or by choice (s4); the necessary hiding in the speakers and the single masculine addressee of the non-past (s5), the command noun-verb (s6), the afʿal of preference outside the kuḥl case (s7), the participles, the ṣifa mushabbaha and the settled ẓarf without the condition of governing (s8), their dual and sound plural absolutely (s9), and the exception verbs (s10).")
ADD_TR = (" Yirmi ikinci bab (baskı s. 122-123): fâil ve nâib zamir veya açık isim (s1), zamir müstetir veya bâriz (s2), vücûben (s3) veya cevâzen (s4) müstetir; vücûben istitâr: mâzî dışındaki mütekellimler ve müfred müzekker muhâtab (s5), emir isim fiili (s6), kuhl meselesi dışındaki ism-i tafdîl (s7), amel şartı olmayan ism-i fâil, mef'ûl, sıfat-ı müşebbehe ve müstakar zarf (s8), bunların tesniye ve sâlim cem'i mutlak olarak (s9) ve istisnâ fiilleri (s10).")
write_out(22, S, TITLE, ADD_EN, ADD_TR, "pp. 122-123", GLOSS_ADD, notes=(NOTE,),
          related=((K21, [K]), (FL, [K]), (NF, [K]), (IFL, [K]), (TF, [K]), (SM, [K]), (MST, [K]), (IFA, [K])))
report(22, S, GLOSS_ADD, (NOTE,))
