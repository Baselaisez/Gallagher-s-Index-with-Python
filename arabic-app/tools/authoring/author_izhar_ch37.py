# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 37: the SEVENTH manṣūb, the tamyīz — what lifts the vagueness off a mentioned essence completed by one of
# the five things (passed in the bāb of the complete vague noun), or an essence estimated in a sentence (طَابَ زَيْدٌ نَفْسًا = طَابَ نَفْسُ زَيْدٍ),
# or what is between the two (الْحَوْضُ مُمْتَلِئٌ مَاءً، الْأَرْضُ مُفَجَّرَةٌ عُيُونًا، زَيْدٌ طَيِّبٌ أَبًا وَأُبُوَّةً وَدَارًا، حَسَنٌ وَجْهًا، أَفْضَلُ مِنْ عَمْرٍو عِلْمًا وَأَبًا —
# in the sense of أَعْجَبَنِي طِيبُهُ أَبًا وَأُبُوَّةً); this tamyīz is a doer in sense, so it is never fronted before its governor; the tamyīz is
# only ever a nakira. Print pp. 134–135.
#   python3 author_izhar_ch37.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; IMT = "al-ism-al-mubham-al-tamm"; TF = "ism-tafdil"; SM = "sifa-mushabbaha"
K = "al-tamyiz-wa-ahkamuh"
K36 = "al-hal-jumla-wa-rabituha"
TITLE = {"ar": "الْمَنْصُوبُ السَّابِعُ: التَّمْيِيزُ وَأَحْكَامُهُ", "en": "The seventh manṣūb: the tamyīz and its rules", "tr": "Yedinci mansûb: temyiz ve hükümleri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def aban(gr, punct=None): return tok("أَبًا", "ab", "noun", [K, TMZ] + gr, "تَمْيِيزٌ مَنْصُوبٌ — عَنِ النِّسْبَةِ.", "«in father» — the tamyīz of the relation.", "«baba bakımından» — nisbet temyizi.", punct=punct)
def waubuwwatan(gr, punct=None): return tok("وَأُبُوَّةً", "ubuwwa", "noun", [K, AT, TMZ, MSD] + gr, "الْوَاوُ عَاطِفَةٌ، وَأُبُوَّةً مَعْطُوفٌ مَنْصُوبٌ.", "«and in fatherhood»", "«ve babalık bakımından»", punct=punct, segments=wa("أُبُوَّةً", "ubuwwa", "noun"))

# ----------- s1 — the seventh: the tamyīz defined, the first kind
S.append({"id": "s1", "translation": {"en": "And the seventh is the tamyīz, and it is what lifts the vagueness off a mentioned essence completed by one of the five things — and it has passed —", "tr": "Yedincisi temyizdir: beş şeyden biriyle tamamlanmış, zikredilmiş bir zâttan kapalılığı kaldıran şeydir — o geçmişti —"},
 "tokens": [
  tok("وَالسَّابِعُ", "sabi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the seventh»", "«yedincisi»", segments=wa("السَّابِعُ", "sabi", "noun")),
  tok("التَّمْيِيزُ", "tamyiz-noun", "noun", [K, MK, TMZ, MSD, F2], "خَبَرٌ مَرْفُوعٌ.", "«the tamyīz» — the khabar.", "«temyiz» — haber.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، خَبَرٌ.", "«what» — the khabar.", "«şey» — haber."),
  tok("يَرْفَعُ", "rafaa", "verb", [K, MAW, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ مَا.", "«lifts»", "«kaldıran»"),
  tok("الْإِبْهَامَ", "ibham", "noun", [K, MB, MSD, F4], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the vagueness»", "«kapalılığı»"),
  tok("عَنْ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«off»", "«-dan»"),
  tok("ذَاتٍ", "dhat", "noun", [K, HJ, TMZ], "مَجْرُورٌ بِعَنْ — الْمُمَيَّزُ.", "«an essence» — the thing distinguished.", "«bir zât» — mümeyyez."),
  tok("مَذْكُورَةٍ", "madhkur", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«mentioned»", "«zikredilmiş»"),
  tok("تَامَّةٍ", "tamm", "noun", [K, NA, IMT], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«completed»", "«tamamlanmış»"),
  tok("بِأَحَدِ", "ahad", "noun", [K, HJ, ID, IMT], "الْبَاءُ حَرْفُ جَرٍّ، وَأَحَدِ مَجْرُورٌ، مُضَافٌ.", "«by one of»", "«biriyle»", segments=[seg("بِ", "bi", "prep"), seg("أَحَدِ", "ahad", "noun")]),
  tok("الْأَشْيَاءِ", "shay", "noun", [K, ID, JT, IMT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the things»", "«şeylerden»"),
  tok("الْخَمْسَةِ", "khamsa", "noun", [K, NA, IMT], "نَعْتٌ مَجْرُورٌ — الْعَدَدُ وَالْمِقْدَارُ وَالْمَكِيلُ وَالْمَوْزُونُ وَالْمَذْرُوعُ.", "«five» — number, measure, the measured, the weighed, the spanned.", "«beş» — sayı, miktar, ölçek, tartı, arşın.", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and already»", "«ve … idi»", segments=wa("قَدْ", "qad", "part")),
  tok("سَبَقَ", "sabaqa", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — بَيَانُهُ فِي بَابِ الِاسْمِ الْمُبْهَمِ التَّامِّ.", "«it has passed» — in the bāb of the complete vague noun.", "«geçmişti» — ism-i mübhem-i tâm bâbında.", punct="،"),
 ]})
# ----------- s2 — the second kind: an essence estimated in a sentence
S.append({"id": "s2", "translation": {"en": "or off an essence estimated in a sentence — as in «Zayd was good in soul», that is, «Zayd's soul was good» —", "tr": "ya da bir cümlede takdîr edilmiş bir zâttan — «Zeyd nefisçe hoş oldu», yani «Zeyd'in nefsi hoş oldu» gibi —"},
 "tokens": [
  aw(),
  tok("مُقَدَّرَةٍ", "muqaddar", "noun", [K, AT, IMF, F2, TMZ], "مَعْطُوفٌ عَلَى مَذْكُورَةٍ مَجْرُورٌ.", "«estimated»", "«takdîr edilmiş»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("جُمْلَةٍ", "jumla", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«a sentence»", "«bir cümle»", punct="،"),
  nahw(),
  tok("طَابَ", "taba", "verb", [K, FL, HV, TMZ], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ.", "«was good»", "«hoş oldu»"),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("نَفْسًا", "nafs", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — مُحَوَّلٌ عَنِ الْفَاعِلِ.", "«in soul» — the tamyīz transferred from the doer.", "«nefisçe» — fâilden çevrilmiş temyiz.", punct="،"),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":"),
  tok("طَابَ", "taba", "verb", [K, FL, HV], "فِعْلٌ مَاضٍ.", "«was good»", "«hoş oldu»"),
  tok("نَفْسُ", "nafs", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — الْأَصْلُ.", "«the soul of» — the doer in origin.", "«nefsi» — asıldaki fâil."),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»", punct="،"),
 ]})
# ----------- s3 — what is between the two: the first examples
S.append({"id": "s3", "translation": {"en": "or off what is between the two — as in «the basin is full of water», «the earth is burst with springs»,", "tr": "ya da ikisinin arasındakinden — «havuz su ile doludur», «yer pınarlarla fışkırmıştır» gibi,"},
 "tokens": [
  aw(),
  tok("مَا", "ma-mawsula", "pron", [K, AT, MAW], "اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى ذَاتٍ فِي مَحَلِّ جَرٍّ.", "«what»", "«şey»"),
  tok("بَيْنَهُمَا", "bayna", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا: بَيْنَ الْمَذْكُورَةِ وَالْمُقَدَّرَةِ.", "«between the two» — between the mentioned and the estimated essence.", "«ikisinin arasında» — zikredilen ile takdîr edilen arasında.", punct="،", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  nahw(),
  tok("الْحَوْضُ", "hawd", "noun", [K, MK, TMZ], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«the basin»", "«havuz»"),
  tok("مُمْتَلِئٌ", "mumtali", "noun", [K, MK, IFA, "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«full» — the khabar.", "«dolu» — haber."),
  tok("مَاءً", "ma-water", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — عَنِ النِّسْبَةِ.", "«of water» — the tamyīz of the relation.", "«su ile» — nisbet temyizi.", punct="،"),
  tok("وَالْأَرْضُ", "ard", "noun", [K, AT, MK, TMZ], "الْوَاوُ عَاطِفَةٌ، وَالْأَرْضُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the earth»", "«ve yer»", segments=wa("الْأَرْضُ", "ard", "noun")),
  tok("مُفَجَّرَةٌ", "mufajjar", "noun", [K, MK, IMF, F2], "خَبَرٌ مَرْفُوعٌ.", "«burst» — the khabar.", "«fışkırmış» — haber."),
  tok("عُيُونًا", "ayn-spring", "noun", [K, TMZ, JT], "تَمْيِيزٌ مَنْصُوبٌ.", "«with springs»", "«pınarlarla»", punct="،"),
 ]})
# ----------- s4 — the ṣifa and the comparative with their tamyīz
S.append({"id": "s4", "translation": {"en": "«Zayd is good in father and in fatherhood and in house», «fine in face», and «better than ʿAmr in knowledge and in father» —", "tr": "«Zeyd baba, babalık ve ev bakımından hoştur», «yüzce güzeldir», «ilimce ve babaca Amr'dan üstündür» —"},
 "tokens": [
  tok("وَزَيْدٌ", "zayd", "propn", [K, AT, MK, TMZ], "الْوَاوُ عَاطِفَةٌ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and Zayd»", "«ve Zeyd»", segments=wa("زَيْدٌ", "zayd", "propn")),
  tok("طَيِّبٌ", "tayyib-good", "noun", [K, MK, SM], "خَبَرٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ.", "«good» — the ṣifa mushabbaha as khabar.", "«hoş» — sıfat-ı müşebbehe haber."),
  aban([SM]), waubuwwatan([]),
  tok("وَدَارًا", "dar", "noun", [K, AT, TMZ], "الْوَاوُ عَاطِفَةٌ، وَدَارًا مَعْطُوفٌ مَنْصُوبٌ.", "«and in house»", "«ve ev bakımından»", punct="،", segments=wa("دَارًا", "dar", "noun")),
  tok("وَحَسَنٌ", "hasan-adj", "noun", [K, AT, MK, SM], "الْوَاوُ عَاطِفَةٌ، وَحَسَنٌ مَعْطُوفٌ عَلَى طَيِّبٌ مَرْفُوعٌ.", "«and fine»", "«ve güzel»", segments=wa("حَسَنٌ", "hasan-adj", "noun")),
  tok("وَجْهًا", "wajh", "noun", [K, TMZ, SM], "تَمْيِيزٌ مَنْصُوبٌ — فَاعِلٌ فِي الْمَعْنَى: حَسُنَ وَجْهُهُ.", "«in face» — a doer in sense: his face is fine.", "«yüzce» — mânen fâil: yüzü güzeldir.", punct="،"),
  tok("وَأَفْضَلُ", "afdal", "noun", [K, AT, MK, TF], "الْوَاوُ عَاطِفَةٌ، وَأَفْضَلُ مَعْطُوفٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«and better» — the comparative.", "«ve üstün» — ism-i tafdîl.", segments=wa("أَفْضَلُ", "afdal", "noun")),
  tok("مِنْ", "min", "prep", [K, HJ, TF], "حَرْفُ جَرٍّ.", "«than»", "«-dan»"),
  tok("عَمْرٍو", "amr-name", "propn", [K, HJ, TF], "مَجْرُورٌ بِمِنْ — وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ.", "«ʿAmr»", "«Amr»"),
  tok("عِلْمًا", "ilm", "noun", [K, TMZ, TF, MSD], "تَمْيِيزٌ مَنْصُوبٌ.", "«in knowledge»", "«ilimce»"),
  tok("وَأَبًا", "ab", "noun", [K, AT, TMZ, TF], "الْوَاوُ عَاطِفَةٌ، وَأَبًا مَعْطُوفٌ مَنْصُوبٌ.", "«and in father»", "«ve babaca»", punct="،", segments=wa("أَبًا", "ab", "noun")),
 ]})
# ----------- s5 — the sense: a doer in meaning
S.append({"id": "s5", "translation": {"en": "for it is in the sense of «his goodness in father and in fatherhood pleased me»;", "tr": "çünkü bu, «onun baba ve babalık bakımından hoşluğu beni hayran bıraktı» mânâsındadır;"},
 "tokens": [
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ، وَالْهَاءُ اسْمُهَا — الْمِثَالُ.", "«for it» — the example.", "«çünkü o» — misâl.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ, IN], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى الْمَحْكِيِّ — خَبَرُ إِنَّ.", "«in the sense of» — the khabar of inna.", "«mânâsında» — inne'nin haberi.", punct=":", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("أَعْجَبَنِي", "ajaba-please", "verb", [K, FL, MB, F4, YM], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«pleased me»", "«beni hayran bıraktı»", segments=[seg("أَعْجَبَ", "ajaba-please", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("طِيبُهُ", "tib", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْمُمَيَّزُ الْمُقَدَّرُ.", "«his goodness» — the doer, the estimated thing distinguished.", "«onun hoşluğu» — fâil, takdîr edilen mümeyyez.", segments=[seg("طِيبُ", "tib", "noun"), pr3ms()]),
  aban([]), waubuwwatan([], punct="،"),
 ]})
# ----------- s6 — a doer in sense, so never fronted
S.append({"id": "s6", "translation": {"en": "and this tamyīz is a doer in sense, and for this it is not fronted before its governor;", "tr": "bu temyiz mânâca fâildir; bu yüzden âmilinin önüne alınmaz;"},
 "tokens": [
  tok("وَهٰذَا", "hadha", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذَا مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and this»", "«ve bu»", segments=wa("هٰذَا", "hadha", "pron")),
  tok("التَّمْيِيزُ", "tamyiz-noun", "noun", [K, "badal", TMZ], "بَدَلٌ مِنْ هٰذَا مَرْفُوعٌ — أَوْ عَطْفُ بَيَانٍ.", "«tamyīz» — the badal of «this».", "«temyiz» — hâzâ'dan bedel."),
  tok("فَاعِلٌ", "fail-doer", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«a doer» — the khabar.", "«fâil» — haber."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-ca»"),
  tok("الْمَعْنَى", "mana", "noun", [K, HJ, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«sense»", "«mânâ»", punct="،"),
  tok("فَلِهٰذَا", "hadha", "pron", [K, AT, HJ], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ حَرْفُ جَرٍّ، وَهٰذَا فِي مَحَلِّ جَرٍّ.", "«and for this»", "«bu yüzden»", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, LN, MR, FL, F5], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — التَّمْيِيزُ.", "«it is fronted»", "«öne alınır»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("عَامِلِهِ", "amil", "noun", [K, HJ, ID, IFA], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", punct="،", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
 ]})
# ----------- s7 — only ever a nakira
S.append({"id": "s7", "translation": {"en": "and the tamyīz is never other than indefinite.", "tr": "ve temyiz ancak nekre olur."},
 "tokens": [
  tok("وَالتَّمْيِيزُ", "tamyiz-noun", "noun", [K, AT, MK, TMZ], "الْوَاوُ عَاطِفَةٌ، وَالتَّمْيِيزُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the tamyīz»", "«ve temyiz»", segments=wa("التَّمْيِيزُ", "tamyiz-noun", "noun")),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَكُونُ", "kana", "verb", [K, LN, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is»", "«olur»"),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ حَصْرٍ.", "«but»", "«ancak»"),
  tok("نَكِرَةً", "nakira", "noun", [K, KN, "istithna-mufarragh"], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«indefinite»", "«nekre»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "ibham": G("ibham", "إِبْهَام", "ب ه م", "noun", "vagueness, obscurity — what the tamyīz lifts", "kapalılık, mübhemlik — temyizin kaldırdığı", 4),
 "mumtali": G("mumtali", "مُمْتَلِئ", "م ل أ", "noun", "full, filled (active participle of form VIII)", "dolu, dolmuş (VIII. babın ism-i fâili)", 3),
 "mufajjar": G("mufajjar", "مُفَجَّر", "ف ج ر", "noun", "burst open, made to gush (passive participle of form II)", "fışkırtılmış, yarılmış (II. babın ism-i mef'ûlü)", 4),
 "ubuwwa": G("ubuwwa", "أُبُوَّة", "أ ب و", "noun", "fatherhood", "babalık", 3),
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
print("izhar ch37 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "rafaa", "sabaqa", "taba", "ajaba-please", "taqaddama") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "التَّمْيِيزُ: رَافِعُ الْإِبْهَامِ عَنِ الذَّاتِ وَعَنِ النِّسْبَةِ، فَاعِلٌ فِي الْمَعْنَى، نَكِرَةٌ أَبَدًا", "en": "The tamyīz: lifting the vagueness off an essence or a relation, a doer in sense, always indefinite", "tr": "Temyiz: zâttan ve nisbetten kapalılığı kaldıran, mânâca fâil, dâimâ nekre"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: التمييز", "الكافية لابن الحاجب — التمييز", "شرح قطر الندى لابن هشام — التمييز"],
 "amil": "the seventh manṣūb is the tamyīz — what lifts the vagueness off a mentioned essence completed by one of the five things (number, measure, the measured, the weighed, the spanned — عِشْرُونَ دِرْهَمًا، رِطْلٌ زَيْتًا), or off an essence estimated in a sentence (طَابَ زَيْدٌ نَفْسًا = طَابَ نَفْسُ زَيْدٍ), or off what lies between the two (الْحَوْضُ مُمْتَلِئٌ مَاءً، الْأَرْضُ مُفَجَّرَةٌ عُيُونًا، زَيْدٌ طَيِّبٌ أَبًا وَأُبُوَّةً وَدَارًا، حَسَنٌ وَجْهًا، أَفْضَلُ مِنْ عَمْرٍو عِلْمًا وَأَبًا — in the sense of أَعْجَبَنِي طِيبُهُ أَبًا); this tamyīz is a doer in sense, so it is never fronted before its governor; the tamyīz is only ever a nakira",
 "question": {
  "en": ["What is the tamyīz? What lifts the vagueness off an essence — a mentioned one completed by one of the five things (عِشْرُونَ دِرْهَمًا), or one estimated in a sentence (طَابَ زَيْدٌ نَفْسًا), or what is between the two.",
         "What are the five things? Number, measure, the measured, the weighed and the spanned — treated in the bāb of the complete vague noun (chapter 15).",
         "What is the tamyīz of the sentence? The vagueness lies in the relation of the verb to its doer: طَابَ زَيْدٌ نَفْسًا is in origin طَابَ نَفْسُ زَيْدٍ — the doer became the tamyīz.",
         "What is «between the two»? The ṣifa and the comparative with a relation to distinguish: الْحَوْضُ مُمْتَلِئٌ مَاءً، زَيْدٌ حَسَنٌ وَجْهًا، أَفْضَلُ مِنْ عَمْرٍو عِلْمًا — in the sense of أَعْجَبَنِي حُسْنُهُ وَجْهًا.",
         "Why may it not be fronted? Because this tamyīz is a doer in sense, and the doer never precedes its governor: not نَفْسًا طَابَ زَيْدٌ.",
         "May the tamyīz be definite? Never — it is only ever a nakira: وَجْهًا, not الْوَجْهَ.",
         "What does the engine READ here? The DabtEngine reads the tanwīn-fatḥ noun after a verb with its doer bound (طَابَ زَيْدٌ نَفْسًا), after a ṣifa khabar (حَسَنٌ وَجْهًا) or after a comparative phrase (أَفْضَلُ مِنْ عَمْرٍو عِلْمًا) as the tamyīz, and the وَ-list of tamyīz nouns by their written case."],
  "tr": ["Temyiz nedir? Zâttan kapalılığı kaldıran şey — beş şeyden biriyle tamamlanmış zikredilmiş bir zâttan (işrûne dirhemen), bir cümlede takdîr edilmiş bir zâttan (tâbe Zeydün nefsen) ya da ikisi arasındakinden.",
         "Beş şey nedir? Sayı, miktar, ölçülen, tartılan ve arşınlanan — ism-i mübhem-i tâm bâbında (15. bab) işlenmişti.",
         "Cümle temyizi nedir? Kapalılık fiilin fâiline nisbetindedir: tâbe Zeydün nefsen aslında tâbe nefsü Zeydin — fâil temyiz oldu.",
         "«İkisi arasındaki» nedir? Ayırt edilecek nisbeti olan sıfat ve ism-i tafdîl: el-havdu mümteliün mâen, Zeydün hasenün vechen, efdalü min Amrin ilmen — a'cebenî husnuhû vechen mânâsında.",
         "Neden öne alınamaz? Çünkü bu temyiz mânâca fâildir, fâil ise âmilinin önüne geçmez: nefsen tâbe Zeydün denmez.",
         "Temyiz ma'rife olabilir mi? Asla — ancak nekre olur: vechen, el-veche değil.",
         "Motor burada neyi OKUR? DabtEngine fâili bağlı fiilden sonra (tâbe Zeydün nefsen), sıfat haberden sonra (hasenün vechen) veya ism-i tafdîl öbeğinden sonra (efdalü min Amrin ilmen) gelen tenvîn-fethalı ismi temyiz; ve ile sıralanan temyiz isimlerini yazılı hâlleriyle okur."],
 },
 "plain": {"en": "The seventh accusative is the «specifier» (tamyīz): an indefinite noun that says in what respect something holds. «Twenty» of what? dirhams. «Zayd was good» in what? soul. «Full» of what? water. «Fine» in what? face. Being the doer in disguise, it never comes before its verb, and it is always indefinite.",
           "tr": "Yedinci mansûb temyizdir: bir şeyin hangi bakımdan olduğunu söyleyen nekre isim. «Yirmi» ne? dirhem. «Zeyd hoş oldu» ne bakımdan? nefisçe. «Havuz dolu» ne ile? su ile. «Güzel» ne bakımdan? yüzce. Aslında kılık değiştirmiş fâil olduğundan fiilinin önüne geçmez ve dâimâ nekredir."},
 "explanation": {"en": "The seventh manṣūb, the tamyīz, lifts the vagueness off an essence. The essence may be mentioned and completed by one of the five things — number, measure, the measured, the weighed, the spanned (عِشْرُونَ دِرْهَمًا) — as the bāb of the complete vague noun said; or it may be estimated in a sentence, the vagueness lying in the verb's relation to its doer: طَابَ زَيْدٌ نَفْسًا is in origin طَابَ نَفْسُ زَيْدٍ; or it may lie between the two — the ṣifa or the comparative with a relation to clear: الْحَوْضُ مُمْتَلِئٌ مَاءً، الْأَرْضُ مُفَجَّرَةٌ عُيُونًا، زَيْدٌ طَيِّبٌ أَبًا وَأُبُوَّةً وَدَارًا، حَسَنٌ وَجْهًا، أَفْضَلُ مِنْ عَمْرٍو عِلْمًا وَأَبًا, which is in the sense of أَعْجَبَنِي طِيبُهُ أَبًا وَأُبُوَّةً. This tamyīz is a doer in sense, and for that it is never fronted before its governor. And the tamyīz is only ever a nakira.",
                 "tr": "Yedinci mansûb temyiz, zâttan kapalılığı kaldırır. Zât ya zikredilmiş ve beş şeyden biriyle — sayı, miktar, ölçülen, tartılan, arşınlanan (işrûne dirhemen) — tamamlanmıştır, ism-i mübhem-i tâm bâbında denildiği gibi; ya bir cümlede takdîr edilmiştir, kapalılık fiilin fâiline nisbetindedir: tâbe Zeydün nefsen aslında tâbe nefsü Zeydin; ya da ikisi arasındadır — nisbeti açılacak sıfat veya ism-i tafdîl: el-havdu mümteliün mâen, el-ardu müfecceratün uyûnen, Zeydün tayyibün eben ve ubüvveten ve dâren, hasenün vechen, efdalü min Amrin ilmen ve eben; bu, a'cebenî tîbühû eben ve ubüvveten mânâsındadır. Bu temyiz mânâca fâildir; bu yüzden âmilinin önüne alınmaz. Temyiz ancak nekre olur."},
 "examples": [
  {"ar": "مَا يَرْفَعُ الْإِبْهَامَ عَنْ ذَاتٍ مَذْكُورَةٍ تَامَّةٍ بِأَحَدِ الْأَشْيَاءِ الْخَمْسَةِ", "en": "the tamyīz defined", "tr": "temyizin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "طَابَ زَيْدٌ نَفْسًا، أَيْ طَابَ نَفْسُ زَيْدٍ", "en": "the tamyīz of the sentence", "tr": "cümle temyizi", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "الْحَوْضُ مُمْتَلِئٌ مَاءً، وَالْأَرْضُ مُفَجَّرَةٌ عُيُونًا", "en": "the tamyīz of the ṣifa's relation", "tr": "sıfatın nisbet temyizi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "زَيْدٌ طَيِّبٌ أَبًا وَأُبُوَّةً وَدَارًا، وَحَسَنٌ وَجْهًا، وَأَفْضَلُ مِنْ عَمْرٍو عِلْمًا وَأَبًا", "en": "the ṣifa and the comparative distinguished", "tr": "sıfat ve ism-i tafdîlin temyizi", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَهٰذَا التَّمْيِيزُ فَاعِلٌ فِي الْمَعْنَى", "en": "a doer in sense, never fronted", "tr": "mânâca fâil, öne alınmaz", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "وَالتَّمْيِيزُ لَا يَكُونُ إِلَّا نَكِرَةً", "en": "only ever a nakira", "tr": "ancak nekre", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "نَفْسًا طَابَ زَيْدٌ", "right": "طَابَ زَيْدٌ نَفْسًا", "why": {"en": "the tamyīz of the sentence is a doer in sense and never precedes its governor", "tr": "cümle temyizi mânâca fâildir; âmilinin önüne geçmez"}},
  {"wrong": "زَيْدٌ حَسَنٌ الْوَجْهَ", "right": "زَيْدٌ حَسَنٌ وَجْهًا", "why": {"en": "the tamyīz is only ever a nakira; the definite form would be the ṣifa's annexed or governed noun", "tr": "temyiz ancak nekredir; ma'rife şekil sıfatın muzâfı veya ma'mûlü olurdu"}},
  {"wrong": "الْحَوْضُ مُمْتَلِئٌ مَاءٌ", "right": "الْحَوْضُ مُمْتَلِئٌ مَاءً", "why": {"en": "the tamyīz of the relation takes naṣb from the ṣifa before it", "tr": "nisbet temyizi önündeki sıfattan nasb alır"}},
 ],
}
ADD_EN = (" Chapter 37 (print pp. 134-135): the tamyīz defined off the completed essence (s1), off the essence estimated in a sentence (s2), off what lies between — the ṣifa's relation (s3-s4) and its sense (s5); a doer in sense, never fronted (s6); only ever a nakira (s7).")
ADD_TR = (" Otuz yedinci bab (baskı s. 134-135): tamamlanmış zâttan (s1), cümlede takdîr edilmiş zâttan (s2), ikisi arasındakinden — sıfatın nisbeti (s3-s4) ve mânâsı (s5) — temyizin tarifi; mânâca fâil, öne alınmaz (s6); ancak nekre (s7).")
write_out(37, S, TITLE, ADD_EN, ADD_TR, "pp. 134-135", GLOSS_ADD, notes=(NOTE,),
          related=((K36, [K]), (TMZ, [K]), (IMT, [K]), (TF, [K]), (SM, [K]), (FL, [K])))
report(37, S, GLOSS_ADD, (NOTE,))
