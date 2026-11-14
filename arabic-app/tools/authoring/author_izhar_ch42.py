# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 42: the muḍāf DROPPED and its iʿrāb given to the muḍāf ilayh — the rule (وَاسْأَلِ الْقَرْيَةَ, Yūsuf 12:82, i.e.
# أَهْلَ الْقَرْيَةِ); rarely the jarr kept (يُرِيدُ الْآخِرَةِ on a reading, al-Anfāl 8:67, i.e. ثَوَابَ الْآخِرَةِ); the muḍāf ilayh dropped with the muḍāf kept
# as it was when a like-annexed word is joined to it (بَيْنَ ذِرَاعَيْ وَجَبْهَةِ الْأَسَدِ) or it is repeated annexed to the like (يَا تَيْمُ تَيْمَ عَدِيٍّ); else the
# muḍāf takes tanwīn in compensation unless it is a limit-word (وَكُلًّا آتَيْنَا, al-Anbiyāʾ 21:79; يَوْمَئِذٍ = يَوْمَ إِذْ كَانَ كَذَا); the limit-words — the six
# directions, حَسْبُ، لَا غَيْرُ، لَيْسَ غَيْرُ — with the muḍāf ilayh intended are built on ḍamm. Print pp. 138–139. The lithograph abridges the āya as
# «وكلا آتيناه»; the Ottoman commentary (izhar-full-corrected l. 1442) prints وَكُلًّا آتَيْنَا حُكْمًا وَعِلْمًا, which the text follows.
#   python3 author_izhar_ch42.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
MDF = "al-mudaf-wa-nawa-al-idafa"; VN = "vocative-munada"; MMB = "al-murab-wal-mabni-wal-irab"; IMP = "imperative-amr"; MMA = "majaz-mursal"
K = "hadhf-al-mudaf-wal-mudaf-ilayh"
K41 = "al-majrur-bil-harf-wa-bil-idafa"
TITLE = {"ar": "حَذْفُ الْمُضَافِ وَحَذْفُ الْمُضَافِ إِلَيْهِ، وَتَنْوِينُ الْعِوَضِ، وَالْغَايَاتُ", "en": "The dropping of the muḍāf and of the muḍāf ilayh, the tanwīn of compensation, and the limit-words", "tr": "Muzâfın ve muzâfun ileyhin hazfi, ivaz tenvîni ve gâyeler"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def nahwqawlihi(): return [tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as in»", "«… gibi»"), tok("قَوْلِهِ", "qawl", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]), tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ.", "«exalted be He»", "«Teâlâ»", punct=":")]
def waqad(): return tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part"))
def ay(): return tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":")
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")

# ----------- s1 — the muḍāf dropped, its iʿrāb to the muḍāf ilayh
S.append({"id": "s1", "translation": {"en": "And sometimes the muḍāf is dropped and its iʿrāb is given to the muḍāf ilayh, and that is the rule — as in His saying, exalted be He: «and ask the town», that is, «the people of the town»;", "tr": "Bazen muzâf hazfedilir ve i'râbı muzâfun ileyhe verilir; kıyas budur — Allah Teâlâ'nın «kasabaya sor» sözündeki gibi, yani «kasabanın halkına»;"},
 "tokens": [
  waqad(),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF, MR, HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is dropped»", "«hazfedilir»"),
  tok("الْمُضَافُ", "mudaf", "noun", [K, NF, MDF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the muḍāf» — the deputy doer.", "«muzâf» — nâib-i fâil."),
  tok("فَيُعْطَى", "ata-give", "verb", [K, AT, NF, MR, MQ], "الْفَاءُ عَاطِفَةٌ، وَيُعْطَى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and is given»", "«ve verilir»", segments=fa("يُعْطَى", "ata-give", "verb")),
  tok("إِعْرَابُهُ", "irab", "noun", [K, NF, ID, MSD, F4], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its iʿrāb»", "«i'râbı»", segments=[seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  tok("لِلْمُضَافِ", "mudaf", "noun", [K, HJ, MDF], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُضَافِ مَجْرُورٌ.", "«to the muḍāf»", "«muzâfa»", segments=[seg("لِ", "li", "prep"), seg("الْمُضَافِ", "mudaf", "noun")]),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, MDF], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«ilayh»", "«ileyh»", punct="،", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْقِيَاسُ", "qiyas", "noun", [K, MK, MSD], "خَبَرٌ مَرْفُوعٌ — الْقَاعِدَةُ الْمُطَّرِدَةُ.", "«the rule» — the regular way.", "«kıyas» — muttarid kural.", punct="،"),
  *nahwqawlihi(),
  tok("وَاسْأَلِ", "saala", "verb", [K, IMP, FL, HT], "الْوَاوُ عَاطِفَةٌ، وَاسْأَلِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ حُرِّكَ بِالْكَسْرِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and ask»", "«ve sor»", segments=wa("اسْأَلِ", "saala", "verb")),
  tok("الْقَرْيَةَ", "qarya", "noun", [K, MB, HT, MMA], "مَفْعُولٌ بِهِ مَنْصُوبٌ — أُعْطِيَ إِعْرَابَ الْمُضَافِ الْمَحْذُوفِ.", "«the town» — given the dropped muḍāf's naṣb.", "«kasabaya» — hazfedilmiş muzâfın nasbı verilmiş.", punct="،"),
  ay(),
  tok("أَهْلَ", "ahl", "noun", [K, MB, ID, HT], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — الْمُضَافُ الْمَحْذُوفُ.", "«the people of» — the dropped muḍāf.", "«halkına» — hazfedilmiş muzâf."),
  tok("الْقَرْيَةِ", "qarya", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَى الْأَصْلِ.", "«the town» — in its original jarr.", "«kasabanın» — asıldaki cer.", punct="،"),
 ]})
# ----------- s2 — rarely the jarr kept
S.append({"id": "s2", "translation": {"en": "and sometimes it stays in jarr, on rare usage — as in His saying, exalted be He: «He desires the Hereafter», with jarr of «the Hereafter» on one reading, that is, «the reward of the Hereafter»;", "tr": "bazen de nâdir olarak mecrûr kalır — Allah Teâlâ'nın «âhireti ister» sözündeki gibi: bir kıraatte âhiret'in ceriyle, yani «âhiretin sevâbını»;"},
 "tokens": [
  waqad(),
  tok("يَبْقَى", "baqiya", "verb", [K, MR, FL, MQ], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْمُضَافُ إِلَيْهِ.", "«it stays» — the muḍāf ilayh.", "«kalır» — muzâfun ileyh."),
  tok("مَجْرُورًا", "majrur", "noun", [K, "hal", IMF], "حَالٌ مَنْصُوبٌ.", "«in jarr»", "«mecrûr olarak»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"),
  tok("النُّدُورِ", "nudur", "noun", [K, HJ, MSD], "مَجْرُورٌ بِعَلَى — خِلَافَ الْقِيَاسِ.", "«rare usage» — against the rule.", "«nâdir olarak» — kıyasa aykırı.", punct="،"),
  *nahwqawlihi(),
  tok("يُرِيدُ", "arada", "verb", [K, MR, FL, HV, F4], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«He desires»", "«ister»"),
  tok("الْآخِرَةِ", "akhira", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بَقِيَ عَلَى جَرِّهِ بَعْدَ حَذْفِ الْمُضَافِ — عَلَى هٰذِهِ الْقِرَاءَةِ.", "«the Hereafter» — kept in jarr after the muḍāf was dropped, on this reading.", "«âhiretin» — muzâf hazfedildikten sonra cerde kalmış; bu kıraatte.", punct="،"),
  tok("بِجَرِّ", "jarr", "noun", [K, HJ, ID, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَجَرِّ مَجْرُورٌ، مُضَافٌ.", "«with jarr of»", "«ceriyle»", segments=[seg("بِ", "bi", "prep"), seg("جَرِّ", "jarr", "noun")]),
  tok("الْآخِرَةِ", "akhira", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Hereafter»", "«âhiret'in»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"),
  tok("قِرَاءَةٍ", "qiraa", "noun", [K, HJ, MSD], "مَجْرُورٌ بِعَلَى — قِرَاءَةٍ مِنَ الْقِرَاءَاتِ.", "«a reading» — one of the readings.", "«bir kıraat» — kıraatlerden biri.", punct="،"),
  ay(),
  tok("ثَوَابَ", "thawab", "noun", [K, MB, ID, HT], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — الْمُضَافُ الْمَحْذُوفُ.", "«the reward of» — the dropped muḍāf.", "«sevâbını» — hazfedilmiş muzâf."),
  tok("الْآخِرَةِ", "akhira", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Hereafter»", "«âhiretin»", punct="،"),
 ]})
# ----------- s3 — the muḍāf ilayh dropped, the muḍāf kept: joined
S.append({"id": "s3", "translation": {"en": "and sometimes the muḍāf ilayh is dropped and the muḍāf stays as it was, if there is joined to it something annexed to the like of the dropped word — as in «between the forelegs and the brow of the lion», that is, «what is between the forelegs of the lion» —", "tr": "bazen de muzâfun ileyh hazfedilir ve muzâf hâlinde kalır; hazfedilenin benzerine muzâf bir şey ona atfedilmişse — «aslanın ön ayakları ile alnı arasında» gibi, yani «aslanın ön ayaklarının arası» —"},
 "tokens": [
  waqad(),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF, MR, HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is dropped»", "«hazfedilir»"),
  tok("الْمُضَافُ", "mudaf", "noun", [K, NF, MDF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the muḍāf»", "«muzâf»"),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, MDF], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«ilayh»", "«ileyh»", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("وَيَبْقَى", "baqiya", "verb", [K, AT, MR, FL, MQ], "الْوَاوُ عَاطِفَةٌ، وَيَبْقَى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and stays»", "«ve kalır»", segments=wa("يَبْقَى", "baqiya", "verb")),
  tok("الْمُضَافُ", "mudaf", "noun", [K, FL, MDF], "فَاعِلٌ مَرْفُوعٌ.", "«the muḍāf»", "«muzâf»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«üzere»"),
  tok("حَالِهِ", "hal", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بِلَا تَنْوِينٍ.", "«it was» — without tanwīn.", "«hâli» — tenvînsiz."),
  tok("إِنْ", "in-shartiyya", "part", [K, INS], "حَرْفُ شَرْطٍ.", "«if»", "«-se»"),
  tok("عُطِفَ", "atafa", "verb", [K, INS, NF, AT], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، فِعْلُ الشَّرْطِ.", "«is joined»", "«atfedilmişse»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَلَى الْمُضَافِ.", "«to it» — to the muḍāf.", "«ona» — muzâfa.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("مَا", "ma-mawsula", "pron", [K, NF, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، نَائِبُ فَاعِلٍ.", "«something» — the deputy doer.", "«bir şey» — nâib-i fâil."),
  tok("أُضِيفَ", "adafa", "verb", [K, MAW, NF, F4], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةُ مَا.", "«annexed»", "«muzâf olan»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مِثْلِ", "mithl", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«the like of»", "«benzerine»"),
  tok("الْمَحْذُوفِ", "mahdhuf", "noun", [K, ID, IMF, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dropped word»", "«hazfedilenin»", punct="،"),
  nahw(),
  tok("بَيْنَ", "bayna", "noun", [K, MF, ID, MDF], "لَفْظٌ مَحْكِيٌّ: ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasında»"),
  tok("ذِرَاعَيْ", "dhira", "noun", [K, ID, MTH, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ وَمُضَافُهُ إِلَيْهِ مَحْذُوفٌ: الْأَسَدِ.", "«the forelegs of» — a dual muḍāf whose muḍāf ilayh «the lion» is dropped.", "«ön ayakları» — muzâfun ileyhi «aslan» hazfedilmiş tesniye muzâf."),
  tok("وَجَبْهَةِ", "jabha", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَجَبْهَةِ مَعْطُوفٌ عَلَى ذِرَاعَيْ مَجْرُورٌ، مُضَافٌ.", "«and the brow of»", "«ve alnı»", segments=wa("جَبْهَةِ", "jabha", "noun")),
  tok("الْأَسَدِ", "asad", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الدَّلِيلُ عَلَى الْمَحْذُوفِ.", "«the lion» — the pointer to the dropped word.", "«aslanın» — hazfedilene delil.", punct="،"),
  ay(),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«… şey»"),
  tok("بَيْنَ", "bayna", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — صِلَةُ مَا.", "«between»", "«arası»"),
  tok("ذِرَاعَيِ", "dhira", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ — حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«the forelegs of»", "«ön ayaklarının»"),
  tok("الْأَسَدِ", "asad", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَحْذُوفُ الْمُقَدَّرُ.", "«the lion» — the dropped word restored.", "«aslanın» — hazfedilenin takdîri.", punct="،"),
 ]})
# ----------- s4 — or repeated annexed to the like
S.append({"id": "s4", "translation": {"en": "or it is repeated annexed to the like of the dropped word — as in «O Taym, Taym of ʿAdī» —", "tr": "ya da hazfedilenin benzerine muzâf olarak tekrarlanmışsa — «ey Teym, Adî'nin Teym'i» gibi —"},
 "tokens": [
  aw(),
  tok("كُرِّرَ", "karrara", "verb", [K, AT, NF, F2, INS], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ عَلَى عُطِفَ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْمُضَافُ.", "«it is repeated» — the muḍāf.", "«tekrarlanmışsa» — muzâf."),
  tok("مُضَافًا", "mudaf", "noun", [K, "hal", IMF, MDF], "حَالٌ مَنْصُوبٌ.", "«annexed»", "«muzâf olarak»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مِثْلِ", "mithl", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«the like of»", "«benzerine»"),
  tok("الْمَحْذُوفِ", "mahdhuf", "noun", [K, ID, IMF, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dropped word»", "«hazfedilenin»", punct="،"),
  nahw(),
  tok("يَا", "ya-nida", "part", [K, VN], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("تَيْمُ", "taym", "propn", [K, VN, HT, MDF], "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — مُضَافٌ حُذِفَ مُضَافُهُ إِلَيْهِ: تَيْمَ عَدِيٍّ.", "«Taym» — the muḍāf whose muḍāf ilayh is dropped, built on ḍamm as a munādā.", "«Teym» — muzâfun ileyhi hazfedilmiş muzâf; münâdâ olarak damme üzere mebnî."),
  tok("تَيْمَ", "taym", "propn", [K, ID, VN, HT], "مُنَادًى ثَانٍ مَنْصُوبٌ لِأَنَّهُ مُضَافٌ — أَوْ تَوْكِيدٌ، التَّكْرَارُ الْمُضَافُ.", "«Taym» — the repetition, annexed.", "«Teym'i» — muzâf olan tekrar."),
  tok("عَدِيٍّ", "adi-name", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مِثْلُ الْمَحْذُوفِ.", "«of ʿAdī» — the like of the dropped word.", "«Adî'nin» — hazfedilenin benzeri.", punct="،"),
 ]})
# ----------- s5 — else tanwīn in compensation, unless a limit-word
S.append({"id": "s5", "translation": {"en": "and otherwise the muḍāf takes tanwīn in compensation for it, if the muḍāf is not a limit-word — as in His saying, exalted be He: «and to each We gave judgement and knowledge», and as in «on that day», that is, «each one», and «at the time when it was so», and «on the day when it was so»;", "tr": "yoksa muzâf onun yerine tenvîn alır — muzâf gâye değilse — Allah Teâlâ'nın «her birine hüküm ve ilim verdik» sözündeki gibi ve «o gün» gibi; yani «her biri», «öyle olduğu zaman», «öyle olduğu gün»;"},
 "tokens": [
  tok("وَإِلَّا", "illa", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ الشَّرْطِيَّةُ وَلَا النَّافِيَةُ — وَإِنْ لَمْ يَكُنْ كَذٰلِكَ.", "«and otherwise» — in + lā.", "«yoksa» — in ve lâ.", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part"), seg("لَا", "la-nafiya", "part")]),
  tok("فَيُنَوَّنُ", "nawwana", "verb", [K, AT, NF, MR, F2, INS], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَيُنَوَّنُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«then takes tanwīn»", "«tenvîn alır»", segments=fa("يُنَوَّنُ", "nawwana", "verb")),
  tok("الْمُضَافُ", "mudaf", "noun", [K, NF, MDF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the muḍāf»", "«muzâf»"),
  tok("عِوَضًا", "iwad", "noun", [K, "maful-lah"], "مَفْعُولٌ لَهُ مَنْصُوبٌ — أَوْ حَالٌ.", "«in compensation»", "«ivaz olarak»"),
  tok("عَنْهُ", "an", "prep", [K, HJ], "عَنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَنِ الْمُضَافِ إِلَيْهِ.", "«for it» — for the muḍāf ilayh.", "«onun yerine» — muzâfun ileyhin.", segments=[seg("عَنْ", "an", "prep"), pr3ms()]),
  tok("إِنْ", "in-shartiyya", "part", [K, INS], "حَرْفُ شَرْطٍ.", "«if»", "«-se»"),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not»", "«değil»"),
  tok("يَكُنِ", "kana", "verb", [K, KN, "lam-jazim", HV, INS], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«it be»", "«olmazsa»"),
  tok("الْمُضَافُ", "mudaf", "noun", [K, KN, MDF], "اسْمُ يَكُنْ مَرْفُوعٌ.", "«the muḍāf»", "«muzâf»"),
  tok("غَايَةً", "ghaya", "noun", [K, KN, MMB], "خَبَرُ يَكُنْ مَنْصُوبٌ — مَا يُبْنَى عَلَى الضَّمِّ عِنْدَ حَذْفِ الْمُضَافِ إِلَيْهِ.", "«a limit-word» — what is built on ḍamm when its muḍāf ilayh is dropped.", "«gâye» — muzâfun ileyhi hazfedilince damme üzere mebnî olan.", punct="،"),
  *nahwqawlihi(),
  tok("وَكُلًّا", "kull", "noun", [K, AT, MB, MDF, HT], "الْوَاوُ عَاطِفَةٌ، وَكُلًّا مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ — نُوِّنَ عِوَضًا عَنِ الْمُضَافِ إِلَيْهِ.", "«and to each» — tanwīn in place of the muḍāf ilayh.", "«ve her birine» — muzâfun ileyh yerine tenvîn.", segments=wa("كُلًّا", "kull", "noun")),
  tok("آتَيْنَا", "aata-bring", "verb", [K, FL, MB, F4], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ.", "«We gave»", "«verdik»", segments=[seg("آتَيْ", "aata-bring", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("حُكْمًا", "hukm", "noun", [K, MB], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«judgement»", "«hüküm»"),
  tok("وَعِلْمًا", "ilm", "noun", [K, AT, MB], "الْوَاوُ عَاطِفَةٌ، وَعِلْمًا مَعْطُوفٌ مَنْصُوبٌ.", "«and knowledge»", "«ve ilim»", punct="،", segments=wa("عِلْمًا", "ilm", "noun")),
  tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=":", segments=wa("نَحْوُ", "nahw", "noun")),
  tok("يَوْمَئِذٍ", "yawmaidhin", "noun", [K, MF, ID, MDF, HT], "لَفْظٌ مَحْكِيٌّ: ظَرْفٌ، مُضَافٌ إِلَى إِذْ، وَتَنْوِينُ إِذْ عِوَضٌ عَنِ الْجُمْلَةِ الْمَحْذُوفَةِ.", "«on that day» — the tanwīn of إِذْ replaces the dropped clause.", "«o gün» — iz'in tenvîni hazfedilmiş cümlenin ivazı.", punct="،", segments=[seg("يَوْمَ", "yawm", "noun"), seg("إِذٍ", "idh", "noun")]),
  ay(),
  tok("كُلَّ", "kull", "noun", [K, MB, ID, HT], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — تَقْدِيرُ كُلًّا.", "«each» — the estimation of كُلًّا.", "«her» — küllen'in takdîri."),
  tok("وَاحِدٍ", "wahid", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَحْذُوفُ.", "«one» — the dropped word.", "«biri» — hazfedilen.", punct="،"),
  tok("وَحِينَ", "hin", "noun", [K, AT, MF, ID, HT], "الْوَاوُ عَاطِفَةٌ، وَحِينَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — تَقْدِيرُ حِينَئِذٍ.", "«and at the time» — the estimation of حِينَئِذٍ.", "«ve … zaman» — hîneizin'in takdîri.", segments=wa("حِينَ", "hin", "noun")),
  tok("إِذْ", "idh", "noun", [K, ID, MF], "ظَرْفٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ، مُضَافٌ إِلَى الْجُمْلَةِ.", "«when»", "«… olduğu»"),
  tok("كَانَ", "kana", "verb", [K, KN, HV, ID], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — الْجُمْلَةُ الْمُضَافُ إِلَيْهَا.", "«it was» — the annexed clause.", "«oldu» — muzâfun ileyh cümle."),
  tok("كَذَا", "kadha", "part", [K, KN], "اسْمٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ، خَبَرُ كَانَ.", "«so»", "«öyle»", punct="،"),
  tok("وَيَوْمَ", "yawm", "noun", [K, AT, MF, ID, HT], "الْوَاوُ عَاطِفَةٌ، وَيَوْمَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — تَقْدِيرُ يَوْمَئِذٍ.", "«and on the day» — the estimation of يَوْمَئِذٍ.", "«ve … gün» — yevmeizin'in takdîri.", segments=wa("يَوْمَ", "yawm", "noun")),
  tok("إِذْ", "idh", "noun", [K, ID, MF], "ظَرْفٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَى الْجُمْلَةِ.", "«when»", "«… olduğu»"),
  tok("كَانَ", "kana", "verb", [K, KN, HV, ID], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«it was»", "«oldu»"),
  tok("كَذَا", "kadha", "part", [K, KN], "خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ.", "«so»", "«öyle»", punct="،"),
 ]})
# ----------- s6 — the limit-words built on ḍamm
S.append({"id": "s6", "translation": {"en": "and if it is a limit-word — and these are the six directions, «ḥasbu», «lā ghayru» and «laysa ghayru» — with the muḍāf ilayh intended in them, it is built on ḍamm.", "tr": "gâye ise — bunlar altı yön, hasbü, lâ gayru ve leyse gayru'dur — muzâfun ileyh onlarda niyet edilmiş olarak damme üzere mebnî olur."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمُضَافُ.", "«it is» — the muḍāf.", "«olursa» — muzâf."),
  tok("غَايَةً", "ghaya", "noun", [K, KN, MMB], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a limit-word»", "«gâye»"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاعْتِرَاضِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and these are»", "«bunlar»", segments=wa("هِيَ", "hiya", "pron")),
  tok("الْجِهَاتُ", "jiha", "noun", [K, MK, "jam-muannath-salim", MMB], "خَبَرٌ مَرْفُوعٌ.", "«the directions» — the khabar.", "«yönler» — haber."),
  tok("السِّتُّ", "sitt", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ — فَوْقُ وَتَحْتُ وَقُدَّامُ وَخَلْفُ وَيَمِينُ وَشِمَالُ.", "«six» — above, below, before, behind, right, left.", "«altı» — üst, alt, ön, arka, sağ, sol."),
  tok("وَحَسْبُ", "hasb", "noun", [K, AT, MMB], "الْوَاوُ عَاطِفَةٌ، وَحَسْبُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — بِمَعْنَى كَافٍ.", "«and ḥasbu» — enough.", "«ve hasbü» — yeter.", segments=wa("حَسْبُ", "hasb", "noun")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and lā»", "«ve lâ»", segments=wa("لَا", "la-nafiya", "part")),
  tok("غَيْرُ", "ghayr", "noun", [K, MMB, ID], "لَفْظٌ مَحْكِيٌّ مَبْنِيٌّ عَلَى الضَّمِّ — مُضَافُهُ إِلَيْهِ مَنْوِيٌّ.", "«ghayru» — built on ḍamm, its muḍāf ilayh intended.", "«gayru» — damme üzere mebnî, muzâfun ileyhi niyette."),
  tok("وَلَيْسَ", "laysa", "verb", [K, AT, "al-fil-al-tamm-wal-naqis"], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and laysa»", "«ve leyse»", segments=wa("لَيْسَ", "laysa", "verb")),
  tok("غَيْرُ", "ghayr", "noun", [K, MMB, ID], "لَفْظٌ مَحْكِيٌّ مَبْنِيٌّ عَلَى الضَّمِّ.", "«ghayru»", "«gayru»"),
  tok("مَنْوِيًّا", "manwi", "noun", [K, "hal", IMF], "حَالٌ مَنْصُوبٌ.", "«intended»", "«niyet edilmiş olarak»"),
  tok("فِيهَا", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — فِي الْغَايَاتِ.", "«in them» — in the limit-words.", "«onlarda» — gâyelerde.", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  tok("الْمُضَافُ", "mudaf", "noun", [K, FL, MDF], "فَاعِلُ مَنْوِيًّا مَرْفُوعٌ.", "«the muḍāf» — the doer of «intended».", "«muzâf» — menviyyen'in fâili."),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, MDF], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«ilayh»", "«ileyh»", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("يُبْنَى", "bana", "verb", [K, NF, MR, MQ, INS, MMB], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْمُضَافُ.", "«it is built» — the answer: the muḍāf.", "«mebnî olur» — cevap: muzâf."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"),
  tok("الضَّمِّ", "damm", "noun", [K, HJ, MMB], "مَجْرُورٌ بِعَلَى — مِنْ فَوْقُ، حَسْبُ، لَا غَيْرُ.", "«ḍamm» — مِنْ فَوْقُ، حَسْبُ، لَا غَيْرُ.", "«damme» — min fevku, hasbü, lâ gayru.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "nudur": G("nudur", "نُدُور", "ن د ر", "noun", "rarity — usage against the rule, heard but not reasoned from", "nâdirlik — kurala aykırı, işitilen ama kıyas edilmeyen kullanım", 4),
 "thawab": G("thawab", "ثَوَاب", "ث و ب", "noun", "reward, recompense", "sevap, karşılık", 2),
 "qiraa": G("qiraa", "قِرَاءَة", "ق ر أ", "noun", "a reading — one of the Qurʾānic readings", "kıraat — Kur'ân okuyuşlarından biri", 3, plural="قِرَاءَات"),
 "jabha": G("jabha", "جَبْهَة", "ج ب ه", "noun", "the brow, forehead", "alın", 2),
 "karrara": G("karrara", "كَرَّرَ", "ك ر ر", "verb", "to repeat (form II)", "tekrarlamak (II. bab)", 3, form="II"),
 "taym": G("taym", "تَيْم", "ت ي م", "propn", "Taym — a tribal name (Taym of ʿAdī)", "Teym — bir kabile adı (Adî'nin Teym'i)", 4),
 "adi-name": G("adi-name", "عَدِيّ", "ع د و", "propn", "ʿAdī — a tribal ancestor's name", "Adî — bir kabile atasının adı", 4),
 "nawwana": G("nawwana", "نَوَّنَ", "ن و ن", "verb", "to give a word tanwīn (form II)", "bir kelimeye tenvîn vermek (II. bab)", 4, form="II"),
 "manwi": G("manwi", "مَنْوِيّ", "ن و ي", "noun", "intended, kept in mind (passive participle)", "niyet edilmiş, akılda tutulmuş (ism-i mef'ûl)", 4),
 "mahdhuf": G("mahdhuf", "مَحْذُوف", "ح ذ ف", "noun", "dropped, elided (passive participle)", "hazfedilmiş (ism-i mef'ûl)", 3),
 "damm": G("damm", "ضَمّ", "ض م م", "noun", "the ḍamm — the vowel u, the mark the limit-words are built on", "damme — u sesi; gâyelerin üzerine mebnî olduğu hareke", 2),
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
put_morph(mo, "karrara", {"bab": "الْبَابُ الثَّانِي فَعَّلَ — مُضَاعَفٌ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَكْرِير", "ismFail": "مُكَرِّر",
 "mazi": ["كَرَّرَ", "كَرَّرَا", "كَرَّرُوا", "كَرَّرَتْ", "كَرَّرَتَا", "كَرَّرْنَ", "كَرَّرْتَ", "كَرَّرْتُمَا", "كَرَّرْتُمْ", "كَرَّرْتِ", "كَرَّرْتُمَا", "كَرَّرْتُنَّ", "كَرَّرْتُ", "كَرَّرْنَا"],
 "mudari": ["يُكَرِّرُ", "يُكَرِّرَانِ", "يُكَرِّرُونَ", "تُكَرِّرُ", "تُكَرِّرَانِ", "يُكَرِّرْنَ", "تُكَرِّرُ", "تُكَرِّرَانِ", "تُكَرِّرُونَ", "تُكَرِّرِينَ", "تُكَرِّرَانِ", "تُكَرِّرْنَ", "أُكَرِّرُ", "نُكَرِّرُ"],
 "amr": ["كَرِّرْ", "كَرِّرَا", "كَرِّرُوا", "كَرِّرِي", "كَرِّرَا", "كَرِّرْنَ"], "mansub": "يُكَرِّرَ", "majzum": "يُكَرِّرْ", "majzum2": "تُكَرِّرْ",
 "note": "كَرَّرَ الشَّيْءَ يُكَرِّرُهُ تَكْرِيرًا: أَعَادَهُ — مِنَ الْبَابِ الثَّانِي، مُتَعَدٍّ."})
put_morph(mo, "nawwana", {"bab": "الْبَابُ الثَّانِي فَعَّلَ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَنْوِين", "ismFail": "مُنَوِّن",
 "mazi": ["نَوَّنَ", "نَوَّنَا", "نَوَّنُوا", "نَوَّنَتْ", "نَوَّنَتَا", "نَوَّنَّ", "نَوَّنْتَ", "نَوَّنْتُمَا", "نَوَّنْتُمْ", "نَوَّنْتِ", "نَوَّنْتُمَا", "نَوَّنْتُنَّ", "نَوَّنْتُ", "نَوَّنَّا"],
 "mudari": ["يُنَوِّنُ", "يُنَوِّنَانِ", "يُنَوِّنُونَ", "تُنَوِّنُ", "تُنَوِّنَانِ", "يُنَوِّنَّ", "تُنَوِّنُ", "تُنَوِّنَانِ", "تُنَوِّنُونَ", "تُنَوِّنِينَ", "تُنَوِّنَانِ", "تُنَوِّنَّ", "أُنَوِّنُ", "نُنَوِّنُ"],
 "amr": ["نَوِّنْ", "نَوِّنَا", "نَوِّنُوا", "نَوِّنِي", "نَوِّنَا", "نَوِّنَّ"], "mansub": "يُنَوِّنَ", "majzum": "يُنَوِّنْ", "majzum2": "تُنَوِّنْ",
 "note": "نَوَّنَ الْكَلِمَةَ يُنَوِّنُهَا تَنْوِينًا: أَلْحَقَ بِهَا التَّنْوِينَ — مِنَ الْبَابِ الثَّانِي، مُتَعَدٍّ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch42 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("hadhafa", "ata-give", "saala", "baqiya", "arada", "atafa", "adafa", "aata-bring", "kana", "bana") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "حَذْفُ الْمُضَافِ وَإِعْطَاءُ إِعْرَابِهِ لِلْمُضَافِ إِلَيْهِ، وَحَذْفُ الْمُضَافِ إِلَيْهِ وَتَنْوِينُ الْعِوَضِ، وَالْغَايَاتُ الْمَبْنِيَّةُ عَلَى الضَّمِّ", "en": "The muḍāf dropped and its iʿrāb given to the muḍāf ilayh; the muḍāf ilayh dropped and the tanwīn of compensation; the limit-words built on ḍamm", "tr": "Muzâfın hazfi ve i'râbının muzâfun ileyhe verilmesi; muzâfun ileyhin hazfi ve ivaz tenvîni; damme üzere mebnî gâyeler"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المجرور بالإضافة: الحذف", "الكافية لابن الحاجب — المضاف إليه", "مغني اللبيب لابن هشام — الغايات"],
 "amil": "the muḍāf may be dropped and its iʿrāb given to the muḍāf ilayh — the rule (وَاسْأَلِ الْقَرْيَةَ = أَهْلَ الْقَرْيَةِ, Yūsuf 12:82); rarely the muḍāf ilayh keeps its jarr (يُرِيدُ الْآخِرَةِ on a reading, al-Anfāl 8:67, = ثَوَابَ الْآخِرَةِ); the muḍāf ilayh may be dropped with the muḍāf kept as it was if a like-annexed word is joined to it (بَيْنَ ذِرَاعَيْ وَجَبْهَةِ الْأَسَدِ) or it is repeated annexed to the like (يَا تَيْمُ تَيْمَ عَدِيٍّ); otherwise the muḍāf takes tanwīn in compensation (وَكُلًّا آتَيْنَا حُكْمًا وَعِلْمًا, al-Anbiyāʾ 21:79; يَوْمَئِذٍ = يَوْمَ إِذْ كَانَ كَذَا) unless it is a limit-word — the six directions, حَسْبُ، لَا غَيْرُ، لَيْسَ غَيْرُ — which, its muḍāf ilayh intended, is built on ḍamm",
 "question": {
  "en": ["What happens when the muḍāf is dropped? Its iʿrāb passes to the muḍāf ilayh — the rule: وَاسْأَلِ الْقَرْيَةَ for وَاسْأَلْ أَهْلَ الْقَرْيَةِ, the town taking the naṣb of «the people».",
         "Is the jarr ever kept? Rarely: يُرِيدُ الْآخِرَةِ, with jarr on one reading, for ثَوَابَ الْآخِرَةِ — heard, not reasoned from.",
         "When may the muḍāf ilayh be dropped with the muḍāf left as it was? When a word annexed to the like of the dropped one is joined to the muḍāf (بَيْنَ ذِرَاعَيْ وَجَبْهَةِ الْأَسَدِ: the lion serves both), or the muḍāf is repeated annexed to the like (يَا تَيْمُ تَيْمَ عَدِيٍّ).",
         "And otherwise? The muḍāf takes tanwīn in compensation for the dropped muḍāf ilayh: كُلًّا for كُلَّ وَاحِدٍ; يَوْمَئِذٍ for يَوْمَ إِذْ كَانَ كَذَا — the tanwīn of إِذْ standing for the dropped clause.",
         "What are the limit-words? The six directions (فَوْقُ، تَحْتُ، قُدَّامُ، خَلْفُ، يَمِينُ، شِمَالُ), حَسْبُ, لَا غَيْرُ and لَيْسَ غَيْرُ: with the muḍāf ilayh intended, they are built on ḍamm — مِنْ فَوْقُ، قَبَضْتُ عَشَرَةً لَا غَيْرُ.",
         "Why ḍamm and not tanwīn? Because the muḍāf ilayh is still meant; the word is cut from annexation in wording only, so it is built, as a sign of that cutting.",
         "What does the engine READ here? The DabtEngine reads the dropped muḍāf's object by the author's fatḥa (الْقَرْيَةَ), the cited rare jarr as the author wrote it, the dual muḍāf ذِرَاعَيْ before the joined word, the munādā تَيْمُ on its ḍamm, the compensating tanwīn of كُلًّا and يَوْمَئِذٍ, and the limit-words on their ḍamm."],
  "tr": ["Muzâf hazfedilince ne olur? İ'râbı muzâfun ileyhe geçer — kıyas: ve's'eli'l-karyete, ve's'el ehle'l-karyeti yerine; kasaba «halk»ın nasbını alır.",
         "Cer hiç korunur mu? Nâdiren: bir kıraatte cer ile yürîdü'l-âhireti, sevâbe'l-âhireti yerine — işitilir, kıyas edilmez.",
         "Muzâfun ileyh ne zaman muzâf hâlinde bırakılarak hazfedilir? Hazfedilenin benzerine muzâf bir kelime muzâfa atfedilince (beyne zirâay ve cebheti'l-esed: aslan ikisine de hizmet eder) ya da muzâf benzerine muzâf olarak tekrarlanınca (yâ Teymü Teyme Adiyyin).",
         "Yoksa? Muzâf, hazfedilen muzâfun ileyhin yerine tenvîn alır: külle vâhidin yerine küllen; yevme iz kâne kezâ yerine yevmeizin — iz'in tenvîni hazfedilmiş cümlenin yerini tutar.",
         "Gâyeler nedir? Altı yön (fevku, tahtü, kuddâmü, halfü, yemînü, şimâlü), hasbü, lâ gayru ve leyse gayru: muzâfun ileyh niyette iken damme üzere mebnîdirler — min fevku, kabadtü aşereten lâ gayru.",
         "Neden tenvîn değil damme? Çünkü muzâfun ileyh hâlâ kastedilir; kelime izâfetten yalnız lafzan kesilmiştir, bu kesilmenin alâmeti olarak mebnî olur.",
         "Motor burada neyi OKUR? DabtEngine hazfedilmiş muzâfın mef'ûlünü yazarın fethasıyla (el-karyete), nâdir ceri yazıldığı gibi, atfedilen kelimeden önceki tesniye muzâf zirâay'ı, dammesi üzere münâdâ Teymü'yü, küllen ve yevmeizin'in ivaz tenvînini ve gâyeleri dammeleri üzere okur."],
 },
 "plain": {"en": "The first noun of a possessive pair may be dropped and its case passes to the second: «ask the town» for «ask the people of the town». The second may be dropped too: the first stays when a twin phrase follows or the word is repeated, else it takes a tanwīn, except the «limit-words» (above, enough), which end in -u.",
           "tr": "İzâfet çiftinin ilk ismi atılabilir, hâli ikinciye geçer: «kasabanın halkına sor» yerine «kasabaya sor». İkinci isim de atılabilir; ikiz bir ifade gelirse ya da kelime tekrarlanırsa ilki olduğu gibi kalır, yoksa onun yerine tenvîn alır; «gâye» sözcükleri (üst, alt, yeter) ise -u ile biter."},
 "explanation": {"en": "The muḍāf may be dropped and its iʿrāb given to the muḍāf ilayh — that is the rule: وَاسْأَلِ الْقَرْيَةَ (Yūsuf 12:82), i.e. أَهْلَ الْقَرْيَةِ. Rarely the muḍāf ilayh stays in jarr: يُرِيدُ الْآخِرَةِ with jarr on one reading (al-Anfāl 8:67), i.e. ثَوَابَ الْآخِرَةِ. The muḍāf ilayh may be dropped and the muḍāf kept as it was — no tanwīn — if a word annexed to the like of the dropped one is joined to it (بَيْنَ ذِرَاعَيْ وَجَبْهَةِ الْأَسَدِ, i.e. مَا بَيْنَ ذِرَاعَيِ الْأَسَدِ) or the muḍāf is repeated annexed to the like (يَا تَيْمُ تَيْمَ عَدِيٍّ). Otherwise the muḍāf takes tanwīn in compensation, provided it is not a limit-word: وَكُلًّا آتَيْنَا حُكْمًا وَعِلْمًا (al-Anbiyāʾ 21:79) for كُلَّ وَاحِدٍ; يَوْمَئِذٍ for يَوْمَ إِذْ كَانَ كَذَا, and so حِينَئِذٍ. If it is a limit-word — the six directions, حَسْبُ, لَا غَيْرُ, لَيْسَ غَيْرُ — with the muḍāf ilayh intended in it, it is built on ḍamm. The lithograph abridges the āya as وكلا آتيناه; the Ottoman commentary prints the āya's wording, which the chapter follows.",
                 "tr": "Muzâf hazfedilip i'râbı muzâfun ileyhe verilebilir — kıyas budur: ve's'eli'l-karyete (Yûsuf 12:82), yani ehle'l-karyeti. Nâdiren muzâfun ileyh cerde kalır: bir kıraatte cer ile yürîdü'l-âhireti (Enfâl 8:67), yani sevâbe'l-âhireti. Muzâfun ileyh hazfedilip muzâf hâlinde — tenvînsiz — bırakılabilir: hazfedilenin benzerine muzâf bir kelime ona atfedilmişse (beyne zirâay ve cebheti'l-esedi, yani mâ beyne zirâayi'l-esedi) ya da muzâf benzerine muzâf olarak tekrarlanmışsa (yâ Teymü Teyme Adiyyin). Yoksa muzâf, gâye olmamak şartıyla, ivaz olarak tenvîn alır: külle vâhidin yerine ve küllen âteynâ hukmen ve ilmen (Enbiyâ 21:79); yevme iz kâne kezâ yerine yevmeizin; hîneizin de öyle. Gâye ise — altı yön, hasbü, lâ gayru, leyse gayru — muzâfun ileyh niyette iken damme üzere mebnî olur. Taşbaskı âyeti vekullen âteynâhu diye kısaltır; Osmanlıca şerh âyetin lafzını basar, bab onu izler."},
 "examples": [
  {"ar": "وَاسْأَلِ الْقَرْيَةَ، أَيْ أَهْلَ الْقَرْيَةِ", "en": "the muḍāf dropped, its naṣb to the muḍāf ilayh", "tr": "muzâf hazfedilmiş, nasbı muzâfun ileyhe", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "يُرِيدُ الْآخِرَةِ، بِجَرِّ الْآخِرَةِ عَلَى قِرَاءَةٍ", "en": "the rare kept jarr", "tr": "nâdir korunmuş cer", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "بَيْنَ ذِرَاعَيْ وَجَبْهَةِ الْأَسَدِ", "en": "the muḍāf ilayh dropped before a joined twin", "tr": "atfedilen ikizden önce hazfedilen muzâfun ileyh", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "يَا تَيْمُ تَيْمَ عَدِيٍّ", "en": "the muḍāf repeated", "tr": "tekrarlanan muzâf", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَكُلًّا آتَيْنَا حُكْمًا وَعِلْمًا؛ يَوْمَئِذٍ", "en": "the tanwīn of compensation", "tr": "ivaz tenvîni", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "الْجِهَاتُ السِّتُّ وَحَسْبُ وَلَا غَيْرُ وَلَيْسَ غَيْرُ", "en": "the limit-words built on ḍamm", "tr": "damme üzere mebnî gâyeler", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "وَاسْأَلِ الْقَرْيَةِ (jarr kept as the rule)", "right": "وَاسْأَلِ الْقَرْيَةَ", "why": {"en": "the rule gives the dropped muḍāf's iʿrāb to the muḍāf ilayh; the kept jarr is a rarity of one reading", "tr": "kıyas, hazfedilmiş muzâfın i'râbını muzâfun ileyhe verir; korunmuş cer bir kıraatin nâdirliğidir"}},
  {"wrong": "كُلُّ آتَيْنَا (no tanwīn)", "right": "كُلًّا آتَيْنَا", "why": {"en": "with its muḍāf ilayh dropped and nothing joined or repeated, كُلّ takes tanwīn in compensation", "tr": "muzâfun ileyhi hazfedilmiş, atıf veya tekrar yokken küll ivaz tenvîni alır"}},
  {"wrong": "مِنْ فَوْقٍ (tanwīn on a limit-word)", "right": "مِنْ فَوْقُ", "why": {"en": "the limit-words with their muḍāf ilayh intended are built on ḍamm, not given tanwīn", "tr": "muzâfun ileyhi niyette olan gâyeler tenvîn almaz, damme üzere mebnî olur"}},
 ],
}
ADD_EN = (" Chapter 42 (print pp. 138-139): the muḍāf dropped and its iʿrāb given to the muḍāf ilayh, Yūsuf 12:82 (s1), the rare kept jarr, al-Anfāl 8:67 (s2), the muḍāf ilayh dropped before a joined twin (s3) or a repetition (s4), the tanwīn of compensation, al-Anbiyāʾ 21:79 and yawmaʾidhin (s5), the limit-words built on ḍamm (s6).")
ADD_TR = (" Kırk ikinci bab (baskı s. 138-139): muzâfın hazfi ve i'râbının muzâfun ileyhe verilmesi, Yûsuf 12:82 (s1), nâdir korunmuş cer, Enfâl 8:67 (s2), atfedilen ikizden (s3) veya tekrardan (s4) önce muzâfun ileyhin hazfi, ivaz tenvîni, Enbiyâ 21:79 ve yevmeizin (s5), damme üzere mebnî gâyeler (s6).")
write_out(42, S, TITLE, ADD_EN, ADD_TR, "pp. 138-139", GLOSS_ADD, notes=(NOTE,),
          related=((K41, [K]), (MDF, [K]), (HT, [K]), (VN, [K]), (MMB, [K]), (MMA, [K])))
report(42, S, GLOSS_ADD, (NOTE,))
