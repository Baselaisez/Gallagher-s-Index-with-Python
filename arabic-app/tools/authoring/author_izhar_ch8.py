# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 8: the QIYĀSĪ governor — its definition (a universal rule can be stated for its governing, its
# subject unbounded; a samāʿī form does not hurt it: every ṣifa mushabbaha raises the doer), its nine kinds; the FIRST, the verb —
# every verb raises and puts in naṣb, its manṣūb may be fronted; lāzim and mutaʿaddī; the lāzim understood without an object, taking
# none but through a jarr letter; the verbs of praise and blame نِعْمَ and بِئْسَ with the three shapes of their doer (ال, annexed to ال,
# a concealed pronoun explained by a tamyīz), the makhṣūṣ after them as a mubtadaʾ whose khabar is the clause before it, its omission
# and its fronting; سَاءَ like بِئْسَ, حَبَّذَا with its frozen doer ذَا. Print pp. 101–102.
#   python3 author_izhar_ch8.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-lazim-wal-mutaaddi"
K1 = "al-amil-wa-aqsamuh"
TITLE = {"ar": "الْعَامِلُ الْقِيَاسِيُّ: الْفِعْلُ اللَّازِمُ وَالْمُتَعَدِّي، وَأَفْعَالُ الْمَدْحِ وَالذَّمِّ", "en": "The qiyāsī governor: the verb, lāzim and mutaʿaddī, and the verbs of praise and blame", "tr": "Kıyâsî âmil: lâzım ve müteaddî fiil, medih ve zem fiilleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; TM = "tamyiz"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"; MDH = "takid-al-madh-wal-dhamm"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def quoted(form, lex, pos, tags, role_ar, role_en, role_tr, punct=None, segments=None):
    return tok(form, lex, pos, [K] + tags + [HT], f"لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، {role_ar}", role_en, role_tr, punct=punct, segments=segments)
def lil(form_rest, lex, tags, ar, en, tr, punct=None):
    return tok("لِ" + form_rest, lex, "noun", [K, HJ] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=[seg("لِ", "li", "prep"), seg(form_rest, lex, "noun")])
def nima_tok(form="نِعْمَ", joined=False, punct=None):
    f = ("وَ" if joined else "") + form
    return tok(f, "nima-verb", "verb", [K, MDH, FL] + ([AT] if joined else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "نِعْمَ فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "«how fine is» — the frozen verb of praise.", "«ne güzel» — câmid medih fiili.", punct=punct, segments=(wa(form, "nima-verb", "verb") if joined else None))

# ----------- s1 — the qiyasi governor defined
S.append({"id": "s1", "translation": {"en": "And the qiyāsī governor is that for whose governing a universal rule can be stated, whose subject is not bounded; and it does not hurt it that its form is samāʿī — as in «every ṣifa mushabbaha raises the doer».", "tr": "Kıyâsî âmil, ameli için konusu sınırlı olmayan küllî bir kaide söylenebilendir; sîgasının semâî olması ona zarar vermez — «her sıfat-ı müşebbehe fâili ref eder» gibi."},
 "tokens": [
  tok("وَالْعَامِلُ", "amil", "noun", [K, MK, K1, IFA], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the governor» — the mubtada.", "«âmil» — mübtedâ.", segments=wa("الْعَامِلُ", "amil", "noun")),
  tok("الْقِيَاسِيُّ", "qiyasi", "noun", [K, NA, K1, "ism-mansub"], "نَعْتٌ مَرْفُوعٌ — مَنْسُوبٌ إِلَى الْقِيَاسِ.", "«qiyāsī» — the naʿt: of qiyās, of rule.", "«kıyâsî» — sıfat: kıyasa nispet."),
  tok("مَا", "ma-mawsula", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«that which» — the relative, the khabar.", "«… olandır» — ism-i mevsûl, haber."),
  tok("يُمْكِنُ", "amkana", "verb", [K, MW, FL, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنْ يُذْكَرَ — وَالْجُمْلَةُ صِلَةٌ.", "«it is possible» — its doer is the أَنْ-clause; the ṣila.", "«mümkündür» — fâili en'li cümle; sıla."),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, FL], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ يُمْكِنُ.", "«that» — the clause is the doer of «is possible».", "«-ması» — cümle yümkinü'nün fâili."),
  tok("يُذْكَرَ", "dhakara", "verb", [K, AM, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be stated» — the passive, in naṣb.", "«söylenmesi» — meçhul, mansûb."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-de»"),
  tok("عَمَلِهِ", "amal-governing", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — فِي عَمَلِ الْعَامِلِ.", "«its governing» — the governor's.", "«ameli için» — âmilin.", segments=[seg("عَمَلِ", "amal-governing", "noun"), pr3msi()]),
  tok("قَاعِدَةٌ", "qaida", "noun", [K, NF, IFA], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«a rule» — the deputy doer.", "«bir kaide» — nâib-i fâil."),
  tok("كُلِّيَّةٌ", "kulli", "noun", [K, NA, "ism-mansub"], "نَعْتٌ مَرْفُوعٌ — مَنْسُوبٌ إِلَى الْكُلِّ.", "«universal» — the naʿt.", "«küllî» — sıfat."),
  tok("مَوْضُوعُهَا", "mawdu", "noun", [K, MK, ID, IMF, "jumla-sifa"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِقَاعِدَةٍ.", "«its subject» — the mubtada of a second, clausal naʿt.", "«konusu» — ikinci, cümle hâlinde sıfatın mübtedâsı.", segments=[seg("مَوْضُوعُ", "mawdu", "noun"), pr3fs()]),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«not» — the khabar, annexed.", "«olmayan» — haber, muzâf."),
  tok("مَحْصُورٍ", "mahsur", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ حَصَرَ.", "«bounded» — ism mafʿūl of حَصَرَ.", "«sınırlı» — hasara'nın ism-i mef'ûlü.", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, "la-nafiya", AT], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَضُرُّهُ", "darra", "verb", [K, MB, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — يَضُرُّ الْعَامِلَ.", "«hurts it» — the governor is the object.", "«ona zarar verir» — âmil mef'ûl.", segments=[seg("يَضُرُّ", "darra", "verb"), pr3ms()]),
  tok("كَوْنُ", "kawn", "noun", [K, FL, ID, "masdar", KN], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ كَانَ النَّاقِصَةِ.", "«the being of» — the doer; the masdar of kāna.", "«olması» — fâil; kâne'nin masdarı."),
  tok("صِيغَتِهِ", "sigha", "noun", [K, ID, KN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ كَوْنِ.", "«its form» — the ism of the masdar.", "«sîgasının» — masdarın ismi.", segments=[seg("صِيغَتِ", "sigha", "noun"), pr3msi()]),
  tok("سَمَاعِيَّةً", "samai", "noun", [K, KN, "ism-mansub"], "خَبَرُ كَوْنِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«samāʿī» — the khabar of the masdar.", "«semâî» — masdarın haberi.", punct="،"),
  nahw(),
  tok("كُلُّ", "kull", "noun", [K, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«every» — the mubtada, annexed.", "«her» — mübtedâ, muzâf."),
  tok("صِفَةٍ", "sifa", "noun", [K, ID, "sifa-mushabbaha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ṣifa»", "«sıfat»"),
  tok("مُشَبَّهَةٍ", "mushabbah", "noun", [K, NA, IMF, "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ — الصِّفَةُ الْمُشَبَّهَةُ بِاسْمِ الْفَاعِلِ.", "«mushabbaha» — the naʿt: the adjective likened to the ism fāʿil.", "«müşebbehe» — sıfat: ism-i fâile benzeyen sıfat."),
  tok("تَرْفَعُ", "rafaa", "verb", [K, MK, FL, "sifa-mushabbaha"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«raises» — the clause is the khabar.", "«ref eder» — cümle haber."),
  tok("الْفَاعِلَ", "fail-doer", "noun", [K, MB, FL], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the doer» — the object.", "«fâili» — mef'ûl.", punct="."),
 ]})
# ----------- s2 — the nine; the verb
S.append({"id": "s2", "translation": {"en": "And it is nine: the first is the verb — every verb raises and puts in naṣb many governed words, and its manṣūb may be fronted before it; and it is of two kinds, lāzim and mutaʿaddī.", "tr": "O dokuzdur: birincisi fiildir — her fiil pek çok ma'mûlü ref ve nasb eder, mansûbunun ondan önce gelmesi câizdir; ve iki türlüdür: lâzım ve müteaddî."},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the mubtada.", "«o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("تِسْعَةٌ", "tisa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«nine» — the khabar.", "«dokuzdur» — haber.", punct=":"),
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«birincisi» — mübtedâ."),
  tok("الْفِعْلُ", "fil", "noun", [K, MK, K1], "خَبَرٌ مَرْفُوعٌ.", "«the verb» — the khabar.", "«fiildir» — haber.", punct="،"),
  tok("فَكُلُّ", "kull", "noun", [K, MK, ID, "fa-khabar-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«so every» — the mubtada.", "«her» — mübtedâ.", segments=fa("كُلُّ", "kull", "noun")),
  tok("فِعْلٍ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verb»", "«fiil»"),
  tok("يَرْفَعُ", "rafaa", "verb", [K, MK, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«raises» — the khabar clause.", "«ref eder» — haber cümlesi."),
  tok("وَيَنْصِبُ", "nasaba-nahw", "verb", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَيَنْصِبُ مُضَارِعٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and puts in naṣb»", "«ve nasb eder»", segments=wa("يَنْصِبُ", "nasaba-nahw", "verb")),
  tok("مَعْمُولَاتٍ", "mamul", "noun", [K, MB, "jam-muannath-salim", IMF], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«governed words» — the object; the sound feminine plural takes the kasra for naṣb.", "«ma'mûller» — mef'ûl; cem-i müennes sâlim nasbını kesre ile alır."),
  tok("كَثِيرَةً", "kathir", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«many» — the naʿt.", "«pek çok» — sıfat.", punct="،"),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, FL, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, FL, ID, "masdar", "taqdim-al-musnad"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the fronting of» — the doer.", "«öne alınması» — fâil."),
  tok("مَنْصُوبِهِ", "mansub", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its manṣūb» — what the verb puts in naṣb.", "«mansûbunun» — fiilin nasb ettiği.", segments=[seg("مَنْصُوبِ", "mansub", "noun"), pr3msi()]),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَلَى الْفِعْلِ.", "«before it» — before the verb.", "«ondan önce» — fiilden.", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«üzere»"),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MK, MTH], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«two kinds» — the dual; the phrase is the khabar.", "«iki tür» — tesniye; câr-mecrûr haber.", punct=":"),
  tok("لَازِمٌ", "lazim", "noun", [K, MK, HT, IFA], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا لَازِمٌ.", "«lāzim» — the khabar of a dropped mubtada: one of them is intransitive.", "«lâzım» — mahzûf mübtedânın haberi: biri lâzımdır."),
  tok("وَمُتَعَدٍّ", "mutaaddi", "noun", [K, AT, IFA, "ism-maqsur-manqus", "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمُتَعَدٍّ مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمُ فَاعِلٍ مِنْ تَعَدَّى.", "«and mutaʿaddī» — joined; a manqūṣ, its ḍamma estimated on the dropped yāʾ.", "«ve müteaddî» — ma'tûf; mankûs, zammesi hazfedilen yâ üzerinde takdîrî.", punct=".", segments=wa("مُتَعَدٍّ", "mutaaddi", "noun")),
 ]})
# ----------- s3 — the lazim
S.append({"id": "s3", "translation": {"en": "So the lāzim is what is fully understood without what the action fell upon — as in «Zayd sat» — and it puts no object in naṣb except through a jarr letter;", "tr": "Lâzım, fiilin üzerine vâki olduğu şey olmadan da anlaşılması tamam olandır — «Zeyd oturdu» gibi — ve mef'ûlün bihi cer harfi olmadan nasb etmez;"},
 "tokens": [
  tok("فَاللَّازِمُ", "lazim", "noun", [K, MK, "fa-khabar-mubtada", IFA], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّازِمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the lāzim» — the mubtada.", "«lâzım» — mübtedâ.", segments=fa("اللَّازِمُ", "lazim", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the relative, the khabar.", "«… olandır» — ism-i mevsûl, haber."),
  tok("يَتِمُّ", "tamma", "verb", [K, MW, FL, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ.", "«is complete» — the ṣila.", "«tamam olur» — sıla."),
  tok("فَهْمُهُ", "fahm", "noun", [K, FL, ID, "masdar"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its understanding» — the doer.", "«anlaşılması» — fâil.", segments=[seg("فَهْمُ", "fahm", "noun"), pr3ms()]),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«without»", "«olmadan»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [K, MW, ID], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«what» — the muḍāf ilayh.", "«şey» — muzâfun ileyh."),
  tok("وَقَعَ", "waqaa", "verb", [K, MW, FL, "mithal-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«fell» — the ṣila.", "«vâki oldu» — sıla."),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ, MW], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«upon it» — the returning pronoun.", "«üzerine» — âid.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("الْفِعْلُ", "fil", "noun", [K, FL], "فَاعِلُ وَقَعَ مَرْفُوعٌ.", "«the action» — the doer of «fell».", "«fiil» — vakaa'nın fâili.", punct="،"),
  nahw(),
  tok("قَعَدَ", "qaada", "verb", [K, FL, "mana-al-fil"], "فِعْلٌ مَاضٍ لَازِمٌ.", "«sat» — an intransitive verb.", "«oturdu» — lâzım fiil."),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, "la-nafiya", AT], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَنْصِبُ", "nasaba-nahw", "verb", [K, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — اللَّازِمُ.", "«puts in naṣb» — the doer concealed: the lāzim.", "«nasb eder» — fâil müstetir: lâzım."),
  tok("الْمَفْعُولَ", "maful-object", "noun", [K, MB, IMF], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the object» — the object.", "«mef'ûlü» — mef'ûl."),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاصْطِلَاحِ: الْمَفْعُولُ بِهِ.", "«bihi» — part of the term.", "«bih» — ıstılahın parçası.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«except through»", "«olmadan»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("حَرْفِ", "harf", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«a letter of»", "«harfi»"),
  tok("الْجَرِّ", "jarr", "noun", [K, ID, HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr»", "«cer»", punct="،"),
 ]})
# ----------- s4 — the verbs of praise and blame
S.append({"id": "s4", "translation": {"en": "and of it are the verbs of praise and blame, namely نِعْمَ for praise and بِئْسَ for blame;", "tr": "medih ve zem fiilleri de ondandır: medih için ni'me, zem için bi'se;"},
 "tokens": [
  tok("وَمِنْهُ", "min", "prep", [K, HJ, MK, AT], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ: مِنَ اللَّازِمِ.", "«and of it» — the fronted khabar: of the lāzim.", "«ondandır» — mukaddem haber: lâzımdan.", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("أَفْعَالُ", "afal", "noun", [K, MK, ID, MDH, "jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the verbs of» — the delayed mubtada.", "«fiilleri» — muahhar mübtedâ."),
  tok("الْمَدْحِ", "madh", "noun", [K, ID, MDH, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«praise»", "«medih»"),
  tok("وَالذَّمِّ", "dhamm", "noun", [K, AT, MDH, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالذَّمِّ مَعْطُوفٌ مَجْرُورٌ.", "«and blame»", "«ve zem»", punct="،", segments=wa("الذَّمِّ", "dhamm", "noun")),
  tok("وَهِيَ", "hiya", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are» — the mubtada.", "«ve onlar» — mübtedâ.", punct=":"),
  quoted("نِعْمَ", "nima-verb", "verb", [MDH, MK], "خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«niʿma» — quoted; the khabar.", "«ni'me» — hikâye edilmiş; haber."),
  lil("لْمَدْحِ", "madh", [MK, MDH], "الْمَدْحِ مَجْرُورٌ — مُتَعَلِّقٌ بِحَالٍ: كَائِنًا لِلْمَدْحِ.", "«for praise»", "«medih için»", punct="،"),
  tok("وَبِئْسَ", "bisa", "verb", [K, MDH, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَبِئْسَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and biʾsa» — quoted, joined.", "«ve bi'se» — hikâye edilmiş, ma'tûf.", segments=wa("بِئْسَ", "bisa", "verb")),
  lil("لذَّمِّ", "dhamm", [MK, MDH], "الذَّمِّ مَجْرُورٌ.", "«for blame»", "«zem için»", punct="،"),
 ]})
# ----------- s5 — their condition; the makhsus
S.append({"id": "s5", "translation": {"en": "and their condition is that the doer be made definite by the lām, or annexed to one so made, or a concealed pronoun explained by an indefinite noun; and that after that the specified one be mentioned, agreeing with the doer — it is a mubtada and what precedes it is its khabar — as in «how fine a man is Zayd», «how fine is the man's servant, Zayd», «how fine, as a man, is Zayd».", "tr": "şartları, fâilin lâm ile ma'rife olması yahut ona muzâf olması yahut bir nekre ile temyiz edilmiş gizli bir zamir olması, ve ondan sonra fâile uygun olarak mahsûsun zikredilmesidir — o mübtedâdır, öncesi de onun haberi — «ne güzel adamdır Zeyd», «ne güzeldir adamın kölesi Zeyd», «adam olarak ne güzeldir Zeyd» gibi."},
 "tokens": [
  tok("وَشَرْطُهُمَا", "shart", "noun", [K, MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and their condition» — the mubtada.", "«ve şartları» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("شَرْطُ", "shart", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("يَكُونَ", "kana", "verb", [K, AM, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be»", "«olması»"),
  tok("الْفَاعِلُ", "fail-doer", "noun", [K, KN, MDH], "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the doer» — the ism of kāna.", "«fâil» — kâne'nin ismi."),
  tok("مُعَرَّفًا", "muarraf", "noun", [K, KN, IMF, "form-ii-verbs"], "خَبَرُ يَكُونَ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ عَرَّفَ.", "«made definite» — the khabar of kāna.", "«ma'rife kılınmış» — kâne'nin haberi."),
  tok("بِاللَّامِ", "lam-letter", "noun", [K, HJ, "anwa-al-lam-al-tarif"], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّامِ مَجْرُورٌ — لَامُ التَّعْرِيفِ.", "«by the lām» — the lām of the article.", "«lâm ile» — ta'rif lâmı.", segments=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  tok("مُضَافًا", "mudaf", "noun", [K, AT, IMF, ID], "مَعْطُوفٌ عَلَى مُعَرَّفًا مَنْصُوبٌ.", "«annexed» — joined to «made definite».", "«muzâf» — ma'tûf."),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — إِلَى الْمُعَرَّفِ بِاللَّامِ.", "«to it» — to what the lām made definite.", "«ona» — lâmla ma'rife olana.", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  tok("مُضْمَرًا", "mudmar", "noun", [K, AT, IMF, "form-iv-verbs"], "مَعْطُوفٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ أَضْمَرَ: ضَمِيرًا مُسْتَتِرًا.", "«concealed» — a hidden pronoun.", "«gizli» — müstetir zamir."),
  tok("مُمَيَّزًا", "mumayyaz", "noun", [K, NA, IMF, TM, "form-ii-verbs"], "نَعْتٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ مَيَّزَ.", "«explained» — the naʿt: made clear by a tamyīz.", "«temyiz edilmiş» — sıfat."),
  tok("بِنَكِرَةٍ", "nakira", "noun", [K, HJ, TM], "الْبَاءُ حَرْفُ جَرٍّ، وَنَكِرَةٍ مَجْرُورٌ — التَّمْيِيزُ.", "«by an indefinite noun» — the tamyīz.", "«bir nekre ile» — temyiz.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("نَكِرَةٍ", "nakira", "noun")]),
  tok("وَيُذْكَرَ", "dhakara", "verb", [K, AT, AM, NF], "الْوَاوُ عَاطِفَةٌ، وَيُذْكَرَ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ عَلَى يَكُونَ مَنْصُوبٌ.", "«and be mentioned» — joined to «be», in naṣb.", "«ve zikredilmesi» — yekûne'ye ma'tûf, mansûb.", segments=wa("يُذْكَرَ", "dhakara", "verb")),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("ذٰلِكَ", "dhalika", "pron", [K, ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that»", "«ondan»"),
  tok("الْمَخْصُوصُ", "makhsus", "noun", [K, NF, MDH, IMF], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — الْمَخْصُوصُ بِالْمَدْحِ أَوِ الذَّمِّ.", "«the specified one» — the deputy doer: the one singled out for praise or blame.", "«mahsûs» — nâib-i fâil: medih yahut zemle özgülenen."),
  tok("مُطَابِقًا", "mutabiq", "noun", [K, "hal", IFA, "form-iii-verbs"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ طَابَقَ.", "«agreeing» — the ḥāl.", "«uygun olarak» — hâl."),
  lil("لْفَاعِلِ", "fail-doer", [MDH], "الْفَاعِلِ مَجْرُورٌ.", "«with the doer»", "«fâile»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْمَخْصُوصُ.", "«and it is» — the specified one.", "«ve o» — mahsûs.", segments=wa("هُوَ", "huwa", "pron")),
  tok("مُبْتَدَأٌ", "mubtada", "noun", [K, MK, MDH], "خَبَرٌ مَرْفُوعٌ.", "«a mubtada» — the khabar.", "«mübtedâdır» — haber."),
  tok("وَمَا", "ma-mawsula", "pron", [K, MW, MK, AT], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and what» — a mubtada.", "«ve … olan» — mübtedâ.", segments=wa("مَا", "ma-mawsula", "pron")),
  tok("قَبْلَهُ", "qabla", "noun", [K, MF, ID, MW, HT], "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةٍ مَحْذُوفَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«precedes it» — the ṣila.", "«öncesi» — sıla.", segments=[seg("قَبْلَ", "qabla", "noun"), pr3ms()]),
  tok("خَبَرُهُ", "khabar-predicate", "noun", [K, MK, ID, MDH], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْجُمْلَةُ قَبْلَهُ خَبَرُهُ.", "«its khabar» — the clause before it.", "«onun haberidir» — öncesindeki cümle.", punct="،", segments=[seg("خَبَرُ", "khabar-predicate", "noun"), pr3ms()]),
  nahw(),
  nima_tok(),
  tok("الرَّجُلُ", "rajul", "noun", [K, FL, MDH], "فَاعِلٌ مَرْفُوعٌ — مُعَرَّفٌ بِاللَّامِ.", "«the man» — the doer, definite by the article.", "«adam» — fâil, lâmla ma'rife."),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, MDH], "الْمَخْصُوصُ بِالْمَدْحِ: مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَجُمْلَةُ نِعْمَ الرَّجُلُ خَبَرُهُ الْمُقَدَّمُ.", "«Zayd» — the one praised: the delayed mubtada; «how fine is the man» its khabar.", "«Zeyd» — mahsûs: muahhar mübtedâ; ni'me'r-racül haberi.", punct="،"),
  nima_tok(joined=True),
  tok("غُلَامُ", "ghulam", "noun", [K, FL, ID, MDH], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ إِلَى الْمُعَرَّفِ بِاللَّامِ.", "«the servant of» — the doer, annexed to an article-noun.", "«kölesi» — fâil, lâmlıya muzâf."),
  tok("الرَّجُلِ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the man»", "«adamın»"),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, MDH], "الْمَخْصُوصُ: مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«Zayd» — the delayed mubtada.", "«Zeyd» — muahhar mübtedâ.", punct="،"),
  nima_tok(joined=True),
  tok("رَجُلًا", "rajul", "noun", [K, TM, MDH], "تَمْيِيزٌ مَنْصُوبٌ يُفَسِّرُ الْفَاعِلَ الْمُسْتَتِرَ.", "«as a man» — the tamyīz explaining the concealed doer.", "«adam olarak» — gizli fâili açıklayan temyiz."),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, MDH], "الْمَخْصُوصُ: مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«Zayd» — the delayed mubtada.", "«Zeyd» — muahhar mübtedâ.", punct="."),
 ]})
# ----------- s6 — the makhsus omitted or fronted
S.append({"id": "s6", "translation": {"en": "And the specified one may be omitted when it is known, and it may come before the verb — as in «the Zayds: how fine are the men».", "tr": "Mahsûs bilindiğinde hazfedilebilir ve fiilden önce de gelebilir — «Zeydler, ne güzel adamlardır» gibi."},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes» — qad of paucity.", "«ve bazen» — taklîl kad'ı.", segments=wa("قَدْ", "qad", "part")),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF, HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is omitted»", "«hazfedilir»"),
  tok("الْمَخْصُوصُ", "makhsus", "noun", [K, NF, MDH], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«the specified one» — the deputy doer.", "«mahsûs» — nâib-i fâil."),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-dığında»"),
  tok("عُلِمَ", "alima", "verb", [K, NF, "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — فِعْلُ الشَّرْطِ، وَالْجَوَابُ مَا تَقَدَّمَ.", "«it is known» — the condition's verb.", "«bilindiğinde» — şart fiili.", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, "qad-harf", AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, FL, "form-v-verbs", "taqdim-al-musnad-ilayh"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْمَخْصُوصُ.", "«comes before» — the doer concealed: the specified one.", "«önce gelir» — fâil müstetir: mahsûs."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«-den önce»"),
  tok("الْفِعْلِ", "fil", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«the verb»", "«fiilden»", punct="،"),
  nahw(),
  tok("الزَّيْدُونَ", "zayd", "propn", [K, MK, MDH, "jam-mudhakkar-salim"], "مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — الْمَخْصُوصُ مُقَدَّمًا.", "«the Zayds» — the mubtada, in rafʿ by the wāw; the specified one fronted.", "«Zeydler» — mübtedâ, vâv ile merfû; mahsûs öne alınmış."),
  nima_tok(),
  tok("الرِّجَالُ", "rajul", "noun", [K, FL, MDH, "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ الزَّيْدُونَ.", "«the men» — the doer; the clause is the khabar.", "«adamlar» — fâil; cümle haber.", punct="."),
 ]})
# ----------- s7 — sa'a and habbadha
S.append({"id": "s7", "translation": {"en": "And سَاءَ is like بِئْسَ; and حَبَّذَا is for praise, its doer is ذَا and it does not change, and after it comes the specified one, whose iʿrāb is like that of the specified one of نِعْمَ — as in «how lovely is Zayd».", "tr": "Sâe de bi'se gibidir; habbezâ medih içindir, fâili zâ'dır ve değişmez, ondan sonra mahsûs gelir ve i'râbı ni'me'nin mahsûsunun i'râbı gibidir — «ne hoştur Zeyd» gibi."},
 "tokens": [
  tok("وَسَاءَ", "saa-bad", "verb", [K, MDH, MK, HT, "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَسَاءَ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and sāʾa» — quoted; the mubtada.", "«sâe» — hikâye edilmiş; mübtedâ.", segments=wa("سَاءَ", "saa-bad", "verb")),
  tok("مِثْلُ", "mithl", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«like» — the khabar, annexed.", "«gibidir» — haber, muzâf."),
  quoted("بِئْسَ", "bisa", "verb", [MDH, ID], "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«biʾsa» — quoted; the muḍāf ilayh.", "«bi'se» — hikâye edilmiş; muzâfun ileyh.", punct="،"),
  tok("وَحَبَّذَا", "habbadha", "part", [K, MDH, MK, HT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَحَبَّذَا لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and ḥabbadhā» — quoted; the mubtada.", "«habbezâ» — hikâye edilmiş; mübtedâ.", segments=wa("حَبَّذَا", "habbadha", "part")),
  lil("لْمَدْحِ", "madh", [MK, MDH], "الْمَدْحِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for praise» — the khabar.", "«medih için» — haber.", punct="،"),
  tok("وَفَاعِلُهُ", "fail-doer", "noun", [K, MK, ID, AT], "الْوَاوُ عَاطِفَةٌ، وَفَاعِلُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its doer» — the mubtada.", "«ve fâili» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("فَاعِلُ", "fail-doer", "noun"), pr3ms()]),
  quoted("ذَا", "dha", "pron", [MK, "asma-al-ishara", MDH], "خَبَرٌ فِي مَحَلِّ رَفْعٍ — اسْمُ الْإِشَارَةِ، فَاعِلُ حَبَّ.", "«dhā» — quoted; the khabar: the demonstrative, the doer of ḥabba.", "«zâ» — hikâye edilmiş; haber: işaret ismi, habbe'nin fâili."),
  tok("وَلَا", "la-nafiya", "part", [K, "la-nafiya", AT], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَتَغَيَّرُ", "taghayyara", "verb", [K, FL, "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — ذَا: لَا يُثَنَّى وَلَا يُجْمَعُ وَلَا يُؤَنَّثُ.", "«changes» — ذَا takes no dual, plural or feminine.", "«değişir» — zâ tesniye, cemi ve müennes olmaz.", punct="،"),
  tok("وَبَعْدَهُ", "bada", "noun", [K, MF, ID, MK, AT], "الْوَاوُ عَاطِفَةٌ، وَبَعْدَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«and after it» — the fronted khabar.", "«ondan sonra» — mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("بَعْدَ", "bada", "noun"), pr3ms()]),
  tok("الْمَخْصُوصُ", "makhsus", "noun", [K, MK, MDH], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the specified one» — the delayed mubtada.", "«mahsûs» — muahhar mübtedâ.", punct="،"),
  tok("وَإِعْرَابُهُ", "irab", "noun", [K, MK, ID, AT], "الْوَاوُ عَاطِفَةٌ، وَإِعْرَابُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its iʿrāb» — the mubtada.", "«ve i'râbı» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  tok("كَإِعْرَابِ", "irab", "noun", [K, HJ, ID, MK], "الْكَافُ حَرْفُ جَرٍّ، وَإِعْرَابِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«like the iʿrāb of» — the khabar.", "«i'râbı gibidir» — haber.", segments=[seg("كَ", "ka", "prep"), seg("إِعْرَابِ", "irab", "noun")]),
  tok("مَخْصُوصِ", "makhsus", "noun", [K, ID, MDH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the specified one of»", "«mahsûsunun»"),
  quoted("نِعْمَ", "nima-verb", "verb", [MDH, ID], "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«niʿma» — quoted; the muḍāf ilayh.", "«ni'me» — hikâye edilmiş; muzâfun ileyh.", punct="،"),
  nahw(),
  tok("حَبَّذَا", "habbadha", "part", [K, MDH, FL], "حَبَّ فِعْلٌ مَاضٍ لِإِنْشَاءِ الْمَدْحِ، وَذَا اسْمُ إِشَارَةٍ فَاعِلُهُ فِي مَحَلِّ رَفْعٍ.", "«how lovely is» — ḥabba the verb, dhā its doer.", "«ne hoştur» — habbe fiil, zâ fâili."),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, MDH], "الْمَخْصُوصُ بِالْمَدْحِ: مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَجُمْلَةُ حَبَّذَا خَبَرُهُ.", "«Zayd» — the one praised: the delayed mubtada.", "«Zeyd» — mahsûs: muahhar mübtedâ.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i]]

CAND = {
 "amkana": G("amkana", "أَمْكَنَ", "م ك ن", "verb", "to be possible (Form IV, impersonal: يُمْكِنُ أَنْ)", "mümkün olmak (if'âl; yümkinü en)", 3, form="IV"),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to mention, to state", "zikretmek, söylemek", 2),
 "qaida": G("qaida", "قَاعِدَة", "ق ع د", "noun", "a rule, a principle", "kaide", 3, plural="قَوَاعِد"),
 "kulli": G("kulli", "كُلِّيّ", "ك ل ل", "noun", "universal, general (nisba of كُلّ)", "küllî — umûmî", 4),
 "mahsur": G("mahsur", "مَحْصُور", "ح ص ر", "noun", "bounded, confined to a number (ism mafʿūl of حَصَرَ)", "mahsûr — sayıyla sınırlı", 4),
 "darra": G("darra", "ضَرَّ", "ض ر ر", "verb", "to harm, to hurt", "zarar vermek", 2),
 "sigha": G("sigha", "صِيغَة", "ص و غ", "noun", "a form, a pattern of a word", "sîga — kelimenin kalıbı", 3, plural="صِيَغ"),
 "sifa": G("sifa", "صِفَة", "و ص ف", "noun", "an adjective, a quality; الصِّفَةُ الْمُشَبَّهَةُ", "sıfat; sıfat-ı müşebbehe", 2, plural="صِفَات"),
 "tisa": G("tisa", "تِسْعَة", "ت س ع", "noun", "nine (with a masculine counted noun)", "dokuz (müzekker ma'dûdla)", 1),
 "nasaba-nahw": G("nasaba-nahw", "نَصَبَ", "ن ص ب", "verb", "to put in naṣb — the grammarians' نَصَبَ يَنْصِبُ (bāb ضَرَبَ)", "nasb etmek — nahivcilerin nasabe yensıbü'sü (darabe bâbı)", 3),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "mansub": G("mansub", "مَنْصُوب", "ن ص ب", "noun", "the manṣūb — a word put in naṣb (ism mafʿūl of نَصَبَ)", "mansûb — nasb edilmiş kelime", 3, plural="مَنْصُوبَات"),
 "lazim": G("lazim", "لَازِم", "ل ز م", "noun", "intransitive (of a verb: its sense complete without an object); necessary", "lâzım — geçişsiz; gerekli", 3),
 "mutaaddi": G("mutaaddi", "مُتَعَدٍّ", "ع د و", "noun", "transitive — a verb whose sense needs an object (ism fāʿil of تَعَدَّى, a manqūṣ)", "müteaddî — geçişli (teaddâ'nın ism-i fâili, mankûs)", 4),
 "tamma": G("tamma", "تَمَّ", "ت م م", "verb", "to be complete", "tamam olmak", 2),
 "madh": G("madh", "مَدْح", "م د ح", "noun", "praise (masdar of مَدَحَ)", "medih, övme", 3),
 "dhamm": G("dhamm", "ذَمّ", "ذ م م", "noun", "blame (masdar of ذَمَّ)", "zem, yerme", 3),
 "nima-verb": G("nima-verb", "نِعْمَ", "ن ع م", "verb", "how fine is… — the frozen verb of praise", "ni'me — ne güzel; câmid medih fiili", 3),
 "bisa": G("bisa", "بِئْسَ", "ب أ س", "verb", "how bad is… — the frozen verb of blame", "bi'se — ne kötü; câmid zem fiili", 3),
 "muarraf": G("muarraf", "مُعَرَّف", "ع ر ف", "noun", "made definite (ism mafʿūl of عَرَّفَ); مُعَرَّفٌ بِاللَّامِ", "ma'rife kılınmış; lâm ile ma'rife", 4),
 "mudmar": G("mudmar", "مُضْمَر", "ض م ر", "noun", "concealed — a pronoun unspoken (ism mafʿūl of أَضْمَرَ)", "muzmar — gizli zamir", 4),
 "mumayyaz": G("mumayyaz", "مُمَيَّز", "م ي ز", "noun", "explained by a tamyīz (ism mafʿūl of مَيَّزَ)", "mümeyyez — temyizle açıklanmış", 4),
 "mutabiq": G("mutabiq", "مُطَابِق", "ط ب ق", "noun", "agreeing with, matching (ism fāʿil of طَابَقَ)", "mutâbık — uygun", 4),
 "saa-bad": G("saa-bad", "سَاءَ", "س و أ", "verb", "to be bad; سَاءَ as a verb of blame like بِئْسَ", "kötü olmak; bi'se gibi zem fiili", 3),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "like, the like of", "gibi, benzeri", 1),
 "habbadha": G("habbadha", "حَبَّذَا", "ح ب ب", "part", "how lovely is… — حَبَّ with its frozen doer ذَا, a verb of praise", "habbezâ — ne hoş; fâili zâ olan medih fiili", 4),
 "dha": G("dha", "ذَا", None, "pron", "this (the demonstrative without هَا); the frozen doer of حَبَّذَا", "zâ — bu (hâ'sız işaret ismi); habbezâ'nın fâili", 3),
 "taghayyara": G("taghayyara", "تَغَيَّرَ", "غ ي ر", "verb", "to change (Form V)", "değişmek (tefa''ul)", 3, form="V"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "nasaba-nahw", _sg.sound1("daraba", "نَصَب", "نْصِب", "اِنْصِب", "نَصْب", "نَاصِب", "مَنْصُوب", "نُصِبَ", "يُنْصَبُ", "نَصَبَ يَنْصِبُ: جَعَلَهُ مَنْصُوبًا — بَابُ ضَرَبَ (وَنَصَبَ يَنْصُبُ: أَقَامَ — بَابُ نَصَرَ)"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
if "bisa" not in mo["verbs"]:
    _n = find_morph("nima-verb")
    mo["verbs"]["bisa"] = {"jamid": True, "bab": "فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الذَّمِّ", "wazn": "فَعِلَ (أَصْلُهُ بَئِسَ)",
                          "mazi": [c.replace("نِعْم", "بِئْس") if c != "—" else c for c in _n["mazi"]],
                          "note": "جَامِدٌ: لَا مُضَارِعَ لَهُ وَلَا أَمْرَ وَلَا مَصْدَرَ — فَاعِلُهُ كَفَاعِلِ نِعْمَ، وَبَعْدَهُ الْمَخْصُوصُ بِالذَّمِّ."}
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch8 gloss+morph ok", len(GLOSS_ADD), "verbs:", [k for k in ("amkana", "dhakara", "darra", "nasaba-nahw", "tamma", "nima-verb", "bisa", "saa-bad", "taghayyara") if k in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْفِعْلُ اللَّازِمُ وَالْمُتَعَدِّي، وَنِعْمَ وَبِئْسَ وَحَبَّذَا", "en": "The verb lāzim and mutaʿaddī, and نِعْمَ، بِئْسَ، حَبَّذَا", "tr": "Lâzım ve müteaddî fiil, ni'me, bi'se ve habbezâ"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العامل القياسي، الفعل", "الكافية لابن الحاجب — أفعال المدح والذم", "العوامل المائة للبركوي"],
 "amil": "الْفِعْلُ — every verb raises its doer and puts its objects in naṣb; the lāzim takes no object but through a jarr letter; نِعْمَ، بِئْسَ، سَاءَ، حَبَّذَا raise a doer of three shapes and the praised one is a mubtadaʾ",
 "question": {
  "en": ["What is a QIYĀSĪ governor? One for whose governing a universal rule can be stated, with no bounded subject — «every verb raises the doer» — even where its FORM is heard (the ṣifa mushabbaha's patterns are samāʿī; the rule over them is not).",
         "How many are the qiyāsī governors, and which is first? Nine; the first is the verb — it raises and puts in naṣb, and its manṣūb may stand before it.",
         "What is a lāzim verb? One understood without the thing the act fell upon (قَعَدَ زَيْدٌ); it puts no object in naṣb except through a jarr letter (ذَهَبَ بِهِ).",
         "Why do the verbs of praise and blame belong to the lāzim? نِعْمَ and بِئْسَ raise their doer and take no object — the praised one is not their object but a MUBTADAʾ.",
         "What may their doer be? Three shapes: made definite by the lām (نِعْمَ الرَّجُلُ), annexed to such a noun (نِعْمَ غُلَامُ الرَّجُلِ), or a concealed pronoun explained by an indefinite tamyīz (نِعْمَ رَجُلًا).",
         "What is the makhṣūṣ and how is it parsed? The one singled out for praise or blame, mentioned after the doer and agreeing with it: a delayed mubtadaʾ whose khabar is the clause before it — زَيْدٌ in نِعْمَ الرَّجُلُ زَيْدٌ. It may be omitted when known, or fronted: الزَّيْدُونَ نِعْمَ الرِّجَالُ.",
         "What of سَاءَ and حَبَّذَا? سَاءَ works like بِئْسَ; حَبَّذَا is ḥabba with the frozen doer ذَا — never dual, plural or feminine — and the makhṣūṣ after it is parsed as after نِعْمَ: حَبَّذَا زَيْدٌ.",
         "What does the engine READ here? The DabtEngine raises the article-noun or the annexed noun after نِعْمَ / بِئْسَ as the doer, writes the tamyīz's fatḥatān after a concealed doer, reads the name that follows as the delayed mubtadaʾ in rafʿ, keeps ذَا whole after حَبَّ, and reads a verb's transitivity off its own paradigm — a verb with no passive and no ism mafʿūl takes no object."],
  "tr": ["KIYÂSÎ âmil nedir? Ameli için konusu sınırsız küllî bir kaide söylenebilen âmil — «her fiil fâili ref eder» — SÎGASI işitme yoluyla olsa bile (sıfat-ı müşebbehenin vezinleri semâîdir; onlara hükmeden kaide değil).",
         "Kıyâsî âmiller kaç tanedir, birincisi hangisidir? Dokuz; birincisi fiildir — ref ve nasb eder, mansûbu ondan önce gelebilir.",
         "Lâzım fiil nedir? Fiilin üzerine vâki olduğu şey olmadan anlaşılan fiil (kaade Zeydün); mef'ûlün bihi ancak cer harfiyle alır (zehebe bihî).",
         "Medih ve zem fiilleri niçin lâzımdandır? Ni'me ve bi'se fâillerini ref eder, mef'ûl almaz — övülen onların mef'ûlü değil MÜBTEDÂdır.",
         "Fâilleri ne olabilir? Üç şekil: lâmla ma'rife (ni'me'r-racül), böyle bir isme muzâf (ni'me gulâmü'r-racül), yahut nekre bir temyizle açıklanan gizli zamir (ni'me racülen).",
         "Mahsûs nedir, nasıl i'râb edilir? Medih yahut zemle özgülenen; fâilden sonra, ona uygun olarak zikredilir: haberi öncesindeki cümle olan muahhar mübtedâ — ni'me'r-racülü Zeydün'deki Zeyd. Bilindiğinde hazfedilir, öne de alınır: ez-Zeydûne ni'me'r-ricâl.",
         "Sâe ve habbezâ? Sâe bi'se gibi amel eder; habbezâ, fâili donmuş zâ olan habbe'dir — tesniye, cemi, müennes olmaz — ardındaki mahsûs ni'me'ninki gibi i'râb edilir: habbezâ Zeydün.",
         "Motor burada neyi OKUR? DabtEngine ni'me / bi'se'den sonraki lâmlı yahut muzâf ismi fâil olarak ref eder, gizli fâilden sonra temyizin fethateynini yazar, ardından gelen ismi muahhar mübtedâ olarak ref'te okur, habbe'den sonra zâ'yı bütün tutar ve fiilin geçişliliğini kendi tasrif tablosundan okur — meçhulü ve ism-i mef'ûlü olmayan fiil mef'ûl almaz."]
 },
 "plain": {"en": "A verb is a rule-bound governor: it raises its doer and pushes its objects into naṣb. Some verbs stop at the doer (Zayd sat) and reach an object only through a letter; the praise and blame verbs are of that kind — «how fine is the man, Zayd» has a doer, and Zayd is a sentence of his own.",
           "tr": "Fiil kaideye bağlı bir âmildir: fâilini ref eder, mef'ûllerini nasb eder. Bazı fiiller fâilde durur (Zeyd oturdu) ve mef'ûle ancak bir harfle ulaşır; medih ve zem fiilleri bu türdendir — «ne güzel adamdır Zeyd»de bir fâil vardır, Zeyd ise kendi başına bir cümledir."},
 "explanation": {"en": "The qiyāsī governor is that for whose governing a universal rule with an unbounded subject can be stated, and a heard form does not hurt it (every ṣifa mushabbaha raises the doer). It is nine. The first is the verb: every verb raises and puts in naṣb many governed words, its manṣūb may be fronted, and it is lāzim or mutaʿaddī. The lāzim is understood without the thing the act fell upon (قَعَدَ زَيْدٌ) and puts no object in naṣb except through a jarr letter; of it are the verbs of praise and blame, نِعْمَ and بِئْسَ, whose doer is made definite by the lām, annexed to such a noun, or a concealed pronoun explained by an indefinite tamyīz, after which the makhṣūṣ is mentioned agreeing with the doer — a mubtadaʾ whose khabar is the clause before it (نِعْمَ الرَّجُلُ زَيْدٌ، نِعْمَ غُلَامُ الرَّجُلِ زَيْدٌ، نِعْمَ رَجُلًا زَيْدٌ); the makhṣūṣ may be omitted when known or fronted before the verb (الزَّيْدُونَ نِعْمَ الرِّجَالُ). سَاءَ is like بِئْسَ; حَبَّذَا is for praise, its doer ذَا unchanging, the makhṣūṣ after it parsed as after نِعْمَ (حَبَّذَا زَيْدٌ).",
                 "tr": "Kıyâsî âmil, ameli için konusu sınırsız küllî bir kaide söylenebilen âmildir; sîgasının semâî olması ona zarar vermez (her sıfat-ı müşebbehe fâili ref eder). Dokuzdur. Birincisi fiildir: her fiil pek çok ma'mûlü ref ve nasb eder, mansûbu öne alınabilir, lâzım yahut müteaddîdir. Lâzım, fiilin üzerine vâki olduğu şey olmadan anlaşılır (kaade Zeydün) ve mef'ûlün bihi ancak cer harfiyle nasb eder; medih ve zem fiilleri ni'me ve bi'se ondandır — fâilleri lâmla ma'rife, böyle bir isme muzâf yahut nekre bir temyizle açıklanan gizli zamirdir; ondan sonra fâile uygun mahsûs zikredilir: haberi öncesindeki cümle olan mübtedâ (ni'me'r-racülü Zeydün, ni'me gulâmü'r-racüli Zeydün, ni'me racülen Zeydün); mahsûs bilindiğinde hazfedilir yahut fiilden önce gelir (ez-Zeydûne ni'me'r-ricâl). Sâe bi'se gibidir; habbezâ medih içindir, fâili değişmeyen zâ'dır, ardındaki mahsûs ni'me'ninki gibi i'râb edilir (habbezâ Zeydün)."},
 "examples": [
  {"ar": "كُلُّ صِفَةٍ مُشَبَّهَةٍ تَرْفَعُ الْفَاعِلَ", "en": "a qiyāsī governor with a samāʿī form: the rule is universal, the pattern heard", "tr": "sîgası semâî kıyâsî âmil: kaide küllî, kalıp işitilmiş", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "قَعَدَ زَيْدٌ", "en": "the lāzim: complete without an object", "tr": "lâzım: mef'ûlsüz tamam", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "نِعْمَ الرَّجُلُ زَيْدٌ، وَنِعْمَ غُلَامُ الرَّجُلِ زَيْدٌ، وَنِعْمَ رَجُلًا زَيْدٌ", "en": "the three shapes of the doer; the makhṣūṣ a delayed mubtadaʾ", "tr": "fâilin üç şekli; mahsûs muahhar mübtedâ", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "الزَّيْدُونَ نِعْمَ الرِّجَالُ", "en": "the makhṣūṣ fronted before the verb", "tr": "mahsûs fiilden önce", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "حَبَّذَا زَيْدٌ", "en": "ḥabba with its frozen doer ذَا", "tr": "donmuş fâili zâ olan habbe", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "نِعْمَ الرَّجُلُ زَيْدًا", "right": "نِعْمَ الرَّجُلُ زَيْدٌ", "why": {"en": "the praised one is not an object — نِعْمَ is lāzim; it is a mubtadaʾ in rafʿ", "tr": "övülen mef'ûl değildir — ni'me lâzımdır; mübtedâ olup merfûdur"}},
  {"wrong": "نِعْمَ رَجُلٌ زَيْدٌ", "right": "نِعْمَ رَجُلًا زَيْدٌ", "why": {"en": "a bare indefinite after نِعْمَ is the tamyīz of the concealed doer, in naṣb — the doer itself must be definite", "tr": "ni'me'den sonraki nekre gizli fâilin temyizidir, mansûb — fâilin kendisi ma'rife olmalıdır"}},
  {"wrong": "حَبَّذَانِ الزَّيْدَانِ", "right": "حَبَّذَا الزَّيْدَانِ", "why": {"en": "ذَا of حَبَّذَا never changes — no dual, plural or feminine", "tr": "habbezâ'nın zâ'sı değişmez — tesniye, cemi, müennes olmaz"}},
  {"wrong": "قَعَدَ زَيْدٌ الْكُرْسِيَّ", "right": "قَعَدَ زَيْدٌ عَلَى الْكُرْسِيِّ", "why": {"en": "a lāzim verb reaches its complement only through a jarr letter", "tr": "lâzım fiil tümlecine ancak cer harfiyle ulaşır"}},
 ],
}
ADD_EN = (" Chapter 8 (print pp. 101-102): the qiyāsī governor defined (s1) and its nine kinds opened with the verb — raising and naṣb, the fronted "
          "manṣūb, lāzim and mutaʿaddī (s2); the lāzim (s3) and the verbs of praise and blame of it: نِعْمَ and بِئْسَ (s4), the three shapes of their "
          "doer and the makhṣūṣ as a mubtadaʾ (s5), its omission and fronting (s6), سَاءَ and حَبَّذَا with its frozen doer (s7).")
ADD_TR = (" Sekizinci bab (baskı s. 101-102): kıyâsî âmilin tarifi (s1) ve fiille açılan dokuz türü — ref ve nasb, öne alınan mansûb, lâzım ve "
          "müteaddî (s2); lâzım (s3) ve ondan olan medih ve zem fiilleri: ni'me ve bi'se (s4), fâillerinin üç şekli ve mübtedâ olarak mahsûs (s5), "
          "mahsûsun hazfi ve öne alınması (s6), sâe ve donmuş fâilli habbezâ (s7).")
write_out(8, S, TITLE, ADD_EN, ADD_TR, "pp. 101-102", GLOSS_ADD, notes=(NOTE,),
          related=((MDH, [K]), ("fail", [K]), ("maful-bihi", [K]), ("tamyiz", [K]), ("mana-al-fil", [K]), (K1, [K]), ("sifa-mushabbaha", [K])))
report(8, S, GLOSS_ADD, (NOTE,))
