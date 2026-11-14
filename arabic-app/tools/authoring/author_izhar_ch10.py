# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 10: the THIRD kind of the mutaʿaddī — to three objects (أَعْلَمَ, أَرَى): the first object like the
# object of بَابُ أَعْطَيْتُ, the last two like the two objects of بَابُ عَلِمْتُ (أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا); then the TĀMM and the
# NĀQIṢ verb — every verb must have a marfūʿ; the verb that completes a sentence with it is tāmm (its marfūʿ the doer, its manṣūb the
# object), the verb that still needs a manṣūb governed word is nāqiṣ (its marfūʿ its ism, its manṣūb its khabar), entering only on the
# mubtadaʾ and the khabar in origin; its two divisions — the first, with no sense of approach, the common one: كَانَ، صَارَ, and آلَ رَجَعَ
# حَالَ اسْتَحَالَ تَحَوَّلَ ارْتَدَّ جَاءَ قَعَدَ when they mean صَارَ; أَصْبَحَ أَمْسَى أَضْحَى ظَلَّ بَاتَ آضَ غَدَا رَاحَ; مَا فَتِئَ (with the tāʾ's fatḥa and
# its kasra), مَا انْفَكَّ، مَا بَرِحَ، مَا وَنَى — all in the sense of مَا زَالَ — and مَا دَامَ and لَيْسَ; a tāmm verb may carry the sense of صَارَ
# and become nāqiṣ (تَمَّ التِّسْعَةُ بِهٰذَا عَشَرَةً، كَمُلَ زَيْدٌ عَالِمًا); their khabars may be fronted before them, except the ones opened
# by مَا (قَائِمًا مَا زَالَ زَيْدٌ is not allowed). Print pp. 105–106. The lithograph's clause on the substitution of إِنْ and لَمْ for مَا
# (وكذا إن لم يدل ما بأن النافية … نحو قائما لم يزل زيد) is garbled and is HELD BACK pending review; the chapter stops before it, and
# the print's doubled «وما دام» before «كلها بمعنى ما زال» is read once, where the received text has it.
#   python3 author_izhar_ch10.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-fil-al-tamm-wal-naqis"
K9 = "al-mutaaddi-wa-afal-al-qulub"
TITLE = {"ar": "الْمُتَعَدِّي إِلَى ثَلَاثَةٍ، وَالْفِعْلُ التَّامُّ وَالنَّاقِصُ وَأَخَوَاتُ كَانَ", "en": "The verb transitive to three objects; the tāmm and the nāqiṣ verb, and the sisters of kāna", "tr": "Üç mef'ûle müteaddî fiil; tâm ve nâkıs fiil, kâne'nin kardeşleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
MFN = "mafulayn"; ZQ = "zanna-wa-akhawatuha"; TSY = "afal-tasyir"; IN = "inna-wa-akhawatuha"; SH = "in-shartiyya"; HL = "hal"; BD = "badal"; HV = "hollow-verbs"; DV = "doubled-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; F8 = "form-viii-verbs"; F10 = "form-x-verbs"; NQ = "naqis-verbs"; MSD = "masdar"; MQ = "ism-maqsur-manqus"; TM = "tamyiz"; LN = "la-nafiya"; LJ = "la-nafiya-lil-jins"; MNS = "mamnu-min-sarf"; JS = "jumla-sifa"; IDH = "idha-shartiyya"; LMJ = "lam-jazim"; AMM = "amma-tafsiliyya"; TWK = "tawkid"; AMR = "imperative-amr"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def qv(form, lex, en, tr, joined=True, punct=None, tags=(), ar_extra=""):
    """a verb mentioned as a word in a list after نَحْوُ: (the first annexed, the rest joined by the wāw)"""
    f = ("وَ" if joined else "") + form
    return tok(f, lex, "verb", [K, KN, HT] + ([AT] if joined else []) + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ" + ("، مَعْطُوفٌ عَلَى الْأَوَّلِ فِي مَحَلِّ جَرٍّ" if joined else "، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ") + ar_extra + ".", en, tr, punct=punct, segments=(wa(form, lex, "verb") if joined else None))
def ma_qv(form, lex, en, tr, joined=True, punct=None, tags=()):
    """مَا + a verb, the pair mentioned as one word"""
    out = [tok(("وَ" if joined else "") + "مَا", "ma-nafiya", "part", [K, KN, HT] + ([AT] if joined else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "مَا نَافِيَةٌ — لَفْظٌ مَحْكِيٌّ مَعَ فِعْلِهِ، مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«mā …» — the negation quoted with its verb.", "«mâ …» — fiiliyle birlikte hikâye edilen nefiy.", segments=(wa("مَا", "ma-nafiya", "part") if joined else None)),
           tok(form, lex, "verb", [K, KN, HT] + list(tags), "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ — الْفِعْلُ الْمَنْفِيُّ بِمَا، مِنْ أَخَوَاتِ كَانَ.", en, tr, punct=punct)]
    return out
def kana_tok(form="كَانَ", lex="kana", en="«kāna»", tr="«kâne»", punct=None, joined=False):
    return qv(form, lex, en, tr, joined=joined, punct=punct)
def mansub_tok(form="مَنْصُوبُهُ", joined=True, punct=None, role_ar="مَعْطُوفٌ عَلَى مَرْفُوعُهُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", en="«and its manṣūb» — joined", tr="«ve mansûbu» — ma'tûf"):
    f = ("وَ" if joined else "") + form
    return tok(f, "mansub", "noun", [K, AT, ID, IMF] + ([AT] if joined else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + role_ar + ".", en, tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("مَنْصُوبُ", "mansub", "noun"), pr3ms()] if joined else [seg("مَنْصُوبُ", "mansub", "noun"), pr3ms()])
def marfu_tok(form="وَمَرْفُوعُهُ", role_ar="الْوَاوُ عَاطِفَةٌ، وَمَرْفُوعُهُ مَعْطُوفٌ عَلَى فِعْلًا — مَفْعُولٌ أَوَّلُ لِيُسَمَّى فِي مَحَلِّ نَصْبٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", en="«and its marfūʿ» — joined to the named thing: the first object of «is named», annexed", tr="«ve merfûu» — adlandırılan şeye ma'tûf: yüsemmâ'nın birinci mef'ûlü, muzâf"):
    return tok(form, "marfu", "noun", [K, AT, ID, IMF, MFN], role_ar + ".", en, tr, segments=[seg("وَ", "wa", "conj"), seg("مَرْفُوعُ", "marfu", "noun"), pr3ms()])
def zayd(form, role_ar, en, tr, punct=None, tags=()): return tok(form, "zayd", "propn", [K] + list(tags), role_ar, en, tr, punct=punct)

# ----------- s1 — the third kind: three objects
S.append({"id": "s1", "translation": {"en": "And the third is transitive to THREE objects — as in أَعْلَمَ and أَرَى; of these the first object is like the object of the bāb of «I gave», and the last two are like the two objects of the bāb of «I knew» — as in «Zayd informed ʿAmr that Bakr is excellent».", "tr": "Üçüncüsü ÜÇ mef'ûle müteaddîdir — a'leme ve erâ gibi; bunların birinci mef'ûlü «verdim» bâbının mef'ûlü gibi, son ikisi «bildim» bâbının iki mef'ûlü gibidir — «Zeyd, Amr'a Bekr'in fâzıl olduğunu bildirdi» gibi."},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third» — the mubtada.", "«üçüncüsü» — mübtedâ.", segments=wa("الثَّالِثُ", "thalith", "noun")),
  tok("مُتَعَدٍّ", "mutaaddi", "noun", [K, MK, MQ, K9], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ مُنَوَّنٌ.", "«transitive» — the khabar.", "«müteaddîdir» — haber."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«three», annexed.", "«üç», muzâf."),
  tok("مَفَاعِيلَ", "maful-object", "noun", [K, ID, MNS, MFN, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، جَمْعُ مَفْعُولٍ.", "«objects» — the ultimate plural, its jarr a fatḥa.", "«mef'ûle» — müntehe'l-cumû, cerri fetha.", punct="،"),
  nahw(),
  qv("أَعْلَمَ", "alama-inform", "«أَعْلَمَ — to inform (someone of something being so)» — the first verb mentioned.", "«a'leme — bildirmek» — zikredilen ilk fiil.", joined=False, tags=[F4]),
  qv("أَرَى", "ara", "«and أَرَى — to show»", "«ve erâ — göstermek»", punct="،", tags=[F4, NQ]),
  tok("وَهٰذِهِ", "hadhihi", "pron", [K, AT, MK, "asma-al-ishara"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذِهِ اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — إِشَارَةٌ إِلَى هٰذِهِ الْأَفْعَالِ.", "«and these» — the mubtada: these verbs.", "«bunların» — mübtedâ: bu fiiller.", segments=wa("هٰذِهِ", "hadhihi", "pron")),
  tok("مَفْعُولُهَا", "maful-object", "noun", [K, MK, ID, MFN], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their object» — a second mubtada.", "«mef'ûlü» — ikinci mübtedâ.", segments=[seg("مَفْعُولُ", "maful-object", "noun"), pr3fs()]),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«the first» — the naʿt.", "«birinci» — sıfat."),
  tok("كَمَفْعُولِ", "maful-object", "noun", [K, HJ, ID, MK], "الْكَافُ حَرْفُ جَرٍّ، وَمَفْعُولِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ الْمُبْتَدَإِ الثَّانِي.", "«like the object of» — the khabar of the second mubtada.", "«… mef'ûlü gibi» — ikinci mübtedânın haberi.", segments=[seg("كَ", "ka", "prep"), seg("مَفْعُولِ", "maful-object", "noun")]),
  tok("بَابِ", "bab", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the bāb of»", "«bâbının»"),
  tok("أَعْطَيْتُ", "aata", "verb", [K, ID, HT, MFN, NQ, F4], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — بَابُ أَعْطَيْتُ: الْمُتَعَدِّي إِلَى مَفْعُولَيْنِ مُتَبَايِنَيْنِ.", "«I gave» — the bāb's name, annexed to.", "«verdim» — bâbın adı, muzâfun ileyh.", punct="،", segments=[seg("أَعْطَيْ", "aata", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("وَالْأَخِيرَانِ", "akhir-last", "noun", [K, AT, MK, MTH], "الْوَاوُ عَاطِفَةٌ، وَالْأَخِيرَانِ مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى — الْمَفْعُولَانِ الْأَخِيرَانِ.", "«and the last two» — the mubtada, the dual: the last two objects.", "«son ikisi» — mübtedâ, tesniye: son iki mef'ûl.", segments=wa("الْأَخِيرَانِ", "akhir-last", "noun")),
  tok("كَمَفْعُولَيْ", "maful-object", "noun", [K, HJ, ID, MK, MTH], "الْكَافُ حَرْفُ جَرٍّ، وَمَفْعُولَيْ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ — خَبَرٌ.", "«like the two objects of» — the dual annexed, its nūn dropped; the khabar.", "«… iki mef'ûlü gibi» — muzâf tesniye, nûnu düşmüş; haber.", segments=[seg("كَ", "ka", "prep"), seg("مَفْعُولَيْ", "maful-object", "noun")]),
  tok("بَابِ", "bab", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the bāb of»", "«bâbının»"),
  tok("عَلِمْتُ", "alima", "verb", [K, ID, HT, ZQ], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — بَابُ عَلِمْتُ: أَفْعَالُ الْقُلُوبِ.", "«I knew» — the bāb's name: the verbs of the heart.", "«bildim» — bâbın adı: kalp fiilleri.", punct="،", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  nahw(),
  tok("أَعْلَمَ", "alama-inform", "verb", [K, FL, MFN, HT, F4], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا.", "«informed» — the example's verb; its doer follows.", "«bildirdi» — misâlin fiili; fâil sonra."),
  zayd("زَيْدٌ", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", tags=[FL]),
  tok("عَمْرًا", "amr-name", "propn", [K, MB, MFN], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ — كَمَفْعُولِ أَعْطَيْتُ.", "«ʿAmr» — the first object, like the object of «I gave».", "«Amr'a» — birinci mef'ûl.", ),
  tok("بَكْرًا", "bakr", "propn", [K, MB, MFN, ZQ], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — أَصْلُهُ مُبْتَدَأٌ.", "«Bakr» — the second object, a mubtada in origin.", "«Bekr'in» — ikinci mef'ûl, aslı mübtedâ."),
  tok("فَاضِلًا", "fadil", "noun", [K, MB, MFN, ZQ, IFA], "مَفْعُولٌ بِهِ ثَالِثٌ مَنْصُوبٌ — أَصْلُهُ خَبَرٌ.", "«excellent» — the third object, a khabar in origin.", "«fâzıl olduğunu» — üçüncü mef'ûl, aslı haber.", punct="."),
 ]})
# ----------- s2 — every verb has a marfūʿ; the tāmm
S.append({"id": "s2", "translation": {"en": "Then know that every verb must have a marfūʿ; so if it completes a sentence by it and needs nothing else, it is named a tāmm verb, its marfūʿ a doer, and its manṣūb — if it is transitive — an object, like the preceding verbs.", "tr": "Sonra bil ki her fiilin mutlaka bir merfûu vardır; onunla bir cümle tamam olur ve başkasına muhtaç olmazsa tâm fiil, merfûu fâil, mansûbu da — müteaddî ise — mef'ûl diye adlandırılır, önceki fiiller gibi."},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "«then»", "«sonra»"),
  tok("اعْلَمْ", "alima", "verb", [K, AMR, FL, ZQ], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«know!» — the imperative; «you» concealed.", "«bil!» — emir; fâil gizli sen."),
  tok("أَنَّهُ", "anna", "part", [K, IN, "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ اسْمُهَا فِي مَحَلِّ نَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيِ اعْلَمْ.", "«that» — its hāʾ the pronoun of the matter; the clause stands for the two objects of «know».", "«… ki» — hâsı şe'n zamiri; cümle i'lem'in iki mef'ûlünün yerinde.", segments=[seg("أَنَّ", "anna", "part"), pr3ms()]),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LJ], "لَا النَّافِيَةُ لِلْجِنْسِ.", "«no …» — the genus-denying lā.", "«hiç … yok» — cinsi nefyeden lâ."),
  tok("بُدَّ", "budd", "noun", [K, LJ, IN], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«escape» — the ism of lā, its khabar dropped: «there is no escape»; the clause is the khabar of أَنَّ.", "«çare» — lâ'nın ismi, haberi mahzûf: «kaçınılmaz»; cümle enne'nin haberi."),
  tok("لِكُلِّ", "kull", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ، مُضَافٌ — مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ.", "«for every» — hanging on lā's dropped khabar.", "«her … için» — lâ'nın mahzûf haberine müteallik.", segments=[seg("لِ", "li", "prep"), seg("كُلِّ", "kull", "noun")]),
  tok("فِعْلٍ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verb»", "«fiil»"),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("مَرْفُوعٍ", "marfu", "noun", [K, HJ, IMF], "مَجْرُورٌ بِمِنْ — اسْمُ مَفْعُولٍ مِنْ رَفَعَ: الْكَلِمَةُ الْمَرْفُوعَةُ.", "«a marfūʿ» — a word in rafʿ.", "«merfû» — ref'teki kelime.", punct="،"),
  tok("فَإِنْ", "in-shartiyya", "part", [K, SH, AT], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if» — the conditional.", "«öyleyse eğer» — şart edatı.", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("تَمَّ", "tamma", "verb", [K, SH, FL, DV], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الْفِعْلُ).", "«completes» — the sharṭ; the verb its hidden doer.", "«tamam olursa» — şart fiili; fâili gizli hüve."),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — بِالْمَرْفُوعِ.", "«by it» — by the marfūʿ.", "«onunla» — merfû ile.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("كَلَامًا", "kalam", "noun", [K, MB, TM], "مَفْعُولٌ بِهِ مَنْصُوبٌ — تَمَّ هُنَا بِمَعْنَى أَتَمَّ، أَوْ تَمْيِيزٌ.", "«a sentence» — the object (تَمَّ in the sense of «make complete»), or the tamyīz.", "«bir kelâm» — mef'ûl (temme burada «tamamlamak» mânâsında), yahut temyiz."),
  tok("وَلَمْ", "lam-jazima", "part", [K, AT, LMJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and did not»", "«ve -mezse»", segments=wa("لَمْ", "lam-jazima", "part")),
  tok("يَحْتَجْ", "ihtaja", "verb", [K, LMJ, SH, HV, F8], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — مَعْطُوفٌ عَلَى فِعْلِ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«need» — jazm by لَمْ, the hollow's middle dropped; joined to the sharṭ.", "«muhtaç olmazsa» — lem ile meczûm, ecvefin ortası düşmüş; şart fiiline ma'tûf."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("غَيْرِهِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — غَيْرِ الْمَرْفُوعِ.", "«anything else» — other than the marfūʿ.", "«başkasına» — merfûdan başkasına.", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("يُسَمَّى", "samma", "verb", [K, SH, NF, MFN, NQ], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (الْفِعْلُ)، وَهُوَ الْمَفْعُولُ الْأَوَّلُ.", "«is named» — the jawāb; the verb its deputy doer (the first object of naming).", "«… diye adlandırılır» — cevap; nâib-i fâil gizli hüve (adlandırmanın birinci mef'ûlü)."),
  tok("فِعْلًا", "fil", "noun", [K, MB, MFN], "مَفْعُولٌ بِهِ ثَانٍ لِيُسَمَّى مَنْصُوبٌ.", "«a verb» — the second object of «is named».", "«fiil» — yüsemmâ'nın ikinci mef'ûlü."),
  tok("تَامًّا", "tamm", "noun", [K, NA, IFA, KN], "نَعْتٌ مَنْصُوبٌ — الْفِعْلُ التَّامُّ: الَّذِي يَكْتَفِي بِمَرْفُوعِهِ.", "«tāmm» — the naʿt: the verb content with its marfūʿ.", "«tâm» — sıfat: merfûuyla yetinen fiil.", punct="،"),
  marfu_tok(),
  tok("فَاعِلًا", "fail-doer", "noun", [K, MB, MFN, FL], "مَفْعُولٌ ثَانٍ لِيُسَمَّى مَنْصُوبٌ — مَرْفُوعُهُ يُسَمَّى فَاعِلًا.", "«a doer» — the second object: its marfūʿ is named a doer.", "«fâil» — ikinci mef'ûl: merfûu fâil diye adlandırılır.", punct="،"),
  mansub_tok(role_ar="مَعْطُوفٌ عَلَى مَرْفُوعُهُ فِي مَحَلِّ نَصْبٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", en="«and its manṣūb» — joined to «its marfūʿ»", tr="«ve mansûbu» — merfûu'na ma'tûf"),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "حَرْفُ شَرْطٍ جَازِمٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«if» — a parenthetical condition.", "«eğer» — mu'teriza şart."),
  tok("كَانَ", "kana", "verb", [K, SH, KN], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الْفِعْلُ)، وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«it is» — kāna as the sharṭ, its ism hidden; the jawāb understood from before.", "«… ise» — şart fiili kâne, ismi gizli; cevap öncekinden anlaşılır."),
  tok("مُتَعَدِّيًا", "mutaaddi", "noun", [K, KN, MQ, K9], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — الْمَنْقُوصُ تَظْهَرُ فَتْحَتُهُ.", "«transitive» — kāna's khabar; the manqūṣ shows its fatḥa.", "«müteaddî» — kâne'nin haberi; mankûsun fethası görünür."),
  tok("مَفْعُولًا", "maful-object", "noun", [K, MB, MFN], "مَفْعُولٌ ثَانٍ لِيُسَمَّى مَنْصُوبٌ — مَنْصُوبُهُ يُسَمَّى مَفْعُولًا.", "«an object» — the second object: its manṣūb is named an object.", "«mef'ûl» — ikinci mef'ûl.", punct="،"),
  tok("كَالْأَفْعَالِ", "fil", "noun", [K, HJ, "jam-taksir"], "الْكَافُ حَرْفُ جَرٍّ، وَالْأَفْعَالِ مَجْرُورٌ.", "«like the verbs»", "«fiiller gibi»", segments=[seg("كَ", "ka", "prep"), seg("الْأَفْعَالِ", "fil", "noun")]),
  tok("السَّابِقَةِ", "sabiq", "noun", [K, NA, IFA], "نَعْتٌ مَجْرُورٌ.", "«preceding» — the naʿt.", "«önceki» — sıfat.", punct="."),
 ]})
# ----------- s3 — the nāqiṣ
S.append({"id": "s3", "translation": {"en": "And if it needs a manṣūb governed word, it is named a nāqiṣ verb, its marfūʿ an ism of it and its manṣūb a khabar of it; and it enters only on the mubtadaʾ and the khabar, in origin.", "tr": "Mansûb bir ma'mûle muhtaç olursa nâkıs fiil, merfûu onun ismi, mansûbu onun haberi diye adlandırılır; aslında yalnız mübtedâ ve habere dâhil olur."},
 "tokens": [
  tok("وَإِنِ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ، كُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and if» — its nūn kasra'd for the two sukūns.", "«ve eğer» — nûnu iki sâkin için kesreli.", segments=wa("إِنِ", "in-shartiyya", "part")),
  tok("احْتَاجَ", "ihtaja", "verb", [K, SH, FL, HV, F8], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«needs» — the sharṭ.", "«muhtaç olursa» — şart fiili."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْمُولٍ", "mamul", "noun", [K, HJ, IMF], "مَجْرُورٌ بِإِلَى.", "«a governed word»", "«ma'mûle»"),
  tok("مَنْصُوبٍ", "mansub", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«in naṣb» — the naʿt.", "«mansûb» — sıfat."),
  tok("يُسَمَّى", "samma", "verb", [K, SH, NF, MFN, NQ], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«is named» — the jawāb.", "«adlandırılır» — cevap."),
  tok("فِعْلًا", "fil", "noun", [K, MB, MFN], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a verb»", "«fiil»"),
  tok("نَاقِصًا", "naqis", "noun", [K, NA, IFA, KN], "نَعْتٌ مَنْصُوبٌ — الْفِعْلُ النَّاقِصُ: كَانَ وَأَخَوَاتُهَا.", "«nāqiṣ» — the naʿt: kāna and its sisters.", "«nâkıs» — sıfat: kâne ve kardeşleri.", punct="،"),
  marfu_tok(),
  tok("اسْمًا", "ism", "noun", [K, MB, MFN, KN], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ كَانَ.", "«an ism» — kāna's ism.", "«isim» — kâne'nin ismi."),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — لِلْفِعْلِ النَّاقِصِ.", "«of it»", "«onun»", punct="،", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  mansub_tok(role_ar="مَعْطُوفٌ عَلَى مَرْفُوعُهُ فِي مَحَلِّ نَصْبٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", en="«and its manṣūb»", tr="«ve mansûbu»"),
  tok("خَبَرًا", "khabar-predicate", "noun", [K, MB, MFN, KN], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — خَبَرُ كَانَ.", "«a khabar» — kāna's khabar.", "«haber» — kâne'nin haberi."),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«of it»", "«onun»", punct="،", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَدْخُلُ", "dakhala", "verb", [K, FL, "istithna-mufarragh"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الْفِعْلُ النَّاقِصُ).", "«enters» — the nāqiṣ its hidden doer.", "«dâhil olur» — fâili gizli nâkıs fiil."),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except» — the exception with its excluded set unstated.", "«ancak» — müferrağ istisnâ."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "مَجْرُورٌ بِعَلَى.", "«the mubtada»", "«mübtedâya»"),
  tok("وَالْخَبَرِ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar»", "«ve habere»", segments=wa("الْخَبَرِ", "khabar-predicate", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَصْلِ", "asl", "noun", [K, HJ], "مَجْرُورٌ بِفِي — فِي أَصْلِ الْوَضْعِ.", "«origin» — in the original setting.", "«aslında» — aslî vaz'da.", punct="."),
 ]})
# ----------- s4 — the two divisions; the first: kāna and its sisters
S.append({"id": "s4", "translation": {"en": "And it is of two divisions: the first division is that which does not signify the sense of approach — it is the common one, what comes first to mind when «the nāqiṣ verb» is said — as in كَانَ and صَارَ, and likewise آلَ, رَجَعَ, حَالَ, اسْتَحَالَ, تَحَوَّلَ, ارْتَدَّ, جَاءَ and قَعَدَ when they are in the sense of صَارَ.", "tr": "İki kısımdır: birinci kısım yaklaşma mânâsına delâlet etmeyendir — yaygın olan, «nâkıs fiil» denince ilk akla gelen budur — kâne ve sâra gibi; âle, racea, hâle, istehâle, tehavvele, irtedde, câe ve kaade de sâra mânâsında oldukları zaman böyledir."},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ — الْفِعْلُ النَّاقِصُ.", "«and it» — the nāqiṣ verb.", "«o» — nâkıs fiil.", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the khabar.", "«üzere» — haber."),
  tok("قِسْمَيْنِ", "qism", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two divisions» — the dual.", "«iki kısım» — tesniye.", punct=":"),
  tok("الْقِسْمُ", "qism", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the division» — the mubtada.", "«kısım» — mübtedâ."),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«the first» — the naʿt.", "«birinci» — sıfat."),
  tok("مَا", "ma-mawsula", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«that which» — the khabar.", "«… olandır» — haber."),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-mez»"),
  tok("يَدُلُّ", "dalla", "verb", [K, MW, FL, DV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«signifies» — the ṣila.", "«delâlet etmeyen» — sıla."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ.", "«the sense of», annexed.", "«mânâsına», muzâf."),
  tok("الْمُقَارَبَةِ", "muqaraba", "noun", [K, ID, MSD, "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ قَارَبَ: الْقُرْبُ مِنَ الشَّيْءِ.", "«approach» — the masdar of قَارَبَ: nearness.", "«yaklaşma» — kârabe'nin masdarı.", punct="،"),
  tok("فَهُوَ", "huwa", "pron", [K, MK, AT], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ.", "«it is» — the mubtada.", "«o» — mübtedâ.", segments=fa("هُوَ", "huwa", "pron")),
  tok("الشَّائِعُ", "shai", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ شَاعَ.", "«the common one» — the khabar.", "«yaygın olan» — haber."),
  tok("الْمُتَبَادِرُ", "mutabadir", "noun", [K, NA, IFA, "form-vi-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ تَبَادَرَ: السَّابِقُ إِلَى الذِّهْنِ.", "«what first comes to mind» — the naʿt; ism fāʿil of تَبَادَرَ.", "«ilk akla gelen» — sıfat; tebâdere'nin ism-i fâili."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("إِطْلَاقِ", "itlaq", "noun", [K, HJ, ID, MSD, F4], "مَجْرُورٌ بِمِنْ، مُضَافٌ — مَصْدَرُ أَطْلَقَ: ذِكْرُ اللَّفْظِ مُطْلَقًا.", "«the saying of» — the masdar of أَطْلَقَ: the term said unqualified.", "«mutlak olarak söylenmesinden» — etlaka'nın masdarı.", ),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»"),
  tok("النَّاقِصِ", "naqis", "noun", [K, NA, KN], "نَعْتٌ مَجْرُورٌ.", "«nāqiṣ» — the naʿt.", "«nâkıs» — sıfat.", punct="،"),
  nahw(),
  kana_tok(en="«kāna» — the first sister, mentioned as a word, annexed to «as in».", tr="«kâne» — ilk kardeş, lafzı kastedilmiş, meselâ'ya muzâf."),
  qv("صَارَ", "sara", "«and ṣāra — to become»", "«ve sâra — olmak»", punct="،", tags=[HV]),
  tok("وَكَذَا", "kadha", "part", [K, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ: وَكَذٰلِكَ الْأَفْعَالُ الْآتِيَةُ.", "«and likewise» — the fronted khabar of the verbs that follow.", "«ve böylece» — gelecek fiillerin mukaddem haberi.", segments=wa("كَذَا", "kadha", "part")),
  qv("آلَ", "ala-return", "«āla — to turn into» — the delayed mubtada, mentioned as a word.", "«âle — dönüşmek» — muahhar mübtedâ, lafzı kastedilmiş.", joined=False, tags=[HV], ar_extra=" — بَلْ مُبْتَدَأٌ مُؤَخَّرٌ فِي مَحَلِّ رَفْعٍ"),
  qv("رَجَعَ", "rajaa", "«and rajaʿa — to come back (to be)»", "«ve racea — dönmek»"),
  qv("حَالَ", "hala", "«and ḥāla — to change into»", "«ve hâle — dönüşmek»", tags=[HV]),
  qv("اسْتَحَالَ", "istahala", "«and istaḥāla — to be transformed (Form X)»", "«ve istehâle — dönüşmek (istif'âl)»", tags=[HV, F10]),
  qv("تَحَوَّلَ", "tahawwala", "«and taḥawwala — to turn (Form V)»", "«ve tehavvele — dönmek (tefa''ul)»", tags=[F5]),
  qv("ارْتَدَّ", "irtadda", "«and irtadda — to revert (Form VIII)»", "«ve irtedde — geri dönmek (iftiâl)»", tags=[F8, DV]),
  qv("جَاءَ", "jaa", "«and jāʾa — to come (to be)»", "«ve câe — gelmek (olmak)»", tags=[HV]),
  qv("قَعَدَ", "qaada", "«and qaʿada — to sit (to become)»", "«ve kaade — oturmak (olmak)»"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… olduğu zaman»"),
  tok("كُنَّ", "kana", "verb", [K, IDH, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالنُّونُ ضَمِيرُ جَمَاعَةِ النِّسْوَةِ اسْمُهُ فِي مَحَلِّ رَفْعٍ — عَائِدٌ إِلَى هٰذِهِ الْأَفْعَالِ؛ فِعْلُ الشَّرْطِ، وَالْجَوَابُ مَا دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«they (the verbs) are» — the women's nūn is kāna's ism; the sharṭ, its jawāb understood.", "«onlar … olduklarında» — nisve nûnu kâne'nin ismi; şart, cevabı anlaşılır."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, KN, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كُنَّ.", "«in the sense of» — kāna's khabar.", "«mânâsında» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("صَارَ", "sara", "verb", [K, ID, HT, KN, HV], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«ṣāra» — the verb mentioned as a word, annexed to.", "«sâra» — lafzı kastedilen fiil, muzâfun ileyh.", punct="."),
 ]})
# ----------- s5 — the rest of the sisters
S.append({"id": "s5", "translation": {"en": "And أَصْبَحَ, أَمْسَى, أَضْحَى, ظَلَّ, بَاتَ, آضَ, غَدَا and رَاحَ; and مَا فَتِئَ — with the fatḥa of the tāʾ and its kasra — مَا انْفَكَّ, مَا بَرِحَ and مَا وَنَى, all of them in the sense of مَا زَالَ; and مَا دَامَ and لَيْسَ.", "tr": "Asbaha, emsâ, adhâ, zalle, bâte, âda, gadâ ve râha; mâ fetie — tânın fethası ve kesresiyle —, mâ'nfekke, mâ beriha ve mâ venâ, hepsi mâ zâle mânâsında; mâ dâme ve leyse."},
 "tokens": [
  qv("أَصْبَحَ", "asbaha", "«and aṣbaḥa — to become (in the morning)» — joined to the sisters before.", "«ve asbaha — (sabahleyin) olmak» — önceki kardeşlere ma'tûf.", tags=[F4]),
  qv("أَمْسَى", "amsa", "«and amsā — to become (in the evening)»", "«ve emsâ — (akşamleyin) olmak»", tags=[F4, NQ]),
  qv("أَضْحَى", "adha-become", "«and aḍḥā — to become (in the forenoon)»", "«ve adhâ — (kuşlukta) olmak»", tags=[F4, NQ]),
  qv("ظَلَّ", "zalla-remain", "«and ẓalla — to remain (by day)»", "«ve zalle — (gündüz) kalmak»", tags=[DV]),
  qv("بَاتَ", "bata", "«and bāta — to remain (by night)»", "«ve bâte — (gece) kalmak»", tags=[HV]),
  qv("آضَ", "ada-become", "«and āḍa — to become»", "«ve âda — olmak»", tags=[HV]),
  qv("غَدَا", "ghada-become", "«and ghadā — to become (in the morning)»", "«ve gadâ — (sabah) olmak»", tags=[NQ]),
  qv("رَاحَ", "raha-become", "«and rāḥa — to become (in the evening)»", "«ve râha — (akşam) olmak»", punct="،", tags=[HV]),
  *ma_qv("فَتِئَ", "fatia", "«mā fatiʾa — to not cease»", "«mâ fetie — … olmaktan geri durmamak»"),
  tok("بِفَتْحِ", "fath", "noun", [K, HJ, ID, HL, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَفَتْحِ مَجْرُورٌ، مُضَافٌ — حَالٌ: مَفْتُوحَ التَّاءِ.", "«with the fatḥa of» — the ḥāl: its tāʾ open.", "«fethasıyla» — hâl: tâsı fethalı.", segments=[seg("بِ", "bi", "prep"), seg("فَتْحِ", "fath", "noun")]),
  tok("التَّاءِ", "ta-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tāʾ»", "«tânın»"),
  tok("وَكَسْرِهَا", "kasr", "noun", [K, AT, ID, MSD], "الْوَاوُ عَاطِفَةٌ، وَكَسْرِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — فَتِئَ وَفَتَأَ.", "«and its kasra» — فَتِئَ and فَتَأَ.", "«ve kesresiyle» — fetie ve fetee.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("كَسْرِ", "kasr", "noun"), pr3fs()]),
  *ma_qv("انْفَكَّ", "infakka", "«mā infakka — to not cease (Form VII)»", "«mâ'nfekke — ayrılmamak (infiâl)»", tags=[DV, "form-vii-verbs"]),
  *ma_qv("بَرِحَ", "bariha", "«mā bariḥa — to not cease»", "«mâ beriha — ayrılmamak»"),
  *ma_qv("وَنَى", "wana", "«mā wanā — to not flag»", "«mâ venâ — gevşememek»", punct="،", tags=[NQ, "mithal-verbs"]),
  tok("كُلُّهَا", "kull", "noun", [K, MK, ID, TWK], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — عَائِدٌ إِلَى الْمَذْكُورَاتِ.", "«all of them» — the mubtada: the ones just listed.", "«hepsi» — mübtedâ: sayılanlar.", segments=[seg("كُلُّ", "kull", "noun"), pr3fs()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MK, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in the sense of» — the khabar.", "«mânâsında» — haber.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("مَا", "ma-nafiya", "part", [K, ID, HT, KN], "لَفْظٌ مَحْكِيٌّ مَعَ فِعْلِهِ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«mā …» — quoted with its verb, annexed to.", "«mâ …» — fiiliyle hikâye edilmiş, muzâfun ileyh."),
  tok("زَالَ", "zala", "verb", [K, HT, KN, HV], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ — مَا زَالَ: الْمُلَازِمَةُ لِلنَّفْيِ.", "«zāla» — «mā zāla», the sister that never leaves the negation.", "«zâle» — mâ zâle: nefiyden ayrılmayan kardeş.", punct="،"),
  *ma_qv("دَامَ", "dama", "«and mā dāma — as long as»", "«ve mâ dâme — … olduğu sürece»", tags=[HV]),
  qv("لَيْسَ", "laysa", "«and laysa — is not»", "«ve leyse — değildir»", punct=".", tags=[KN]),
 ]})
# ----------- s6 — a tāmm verb carrying the sense of ṣāra
S.append({"id": "s6", "translation": {"en": "And a tāmm verb may contain the sense of صَارَ and so become nāqiṣ — as in «the nine became, by this one, ten», that is, became a complete ten; and «Zayd came to be a learned man», that is, became a complete scholar; and other such.", "tr": "Tâm fiil sâra mânâsını içerip nâkıs olabilir — «dokuz bununla on oldu», yani tam bir on oldu; «Zeyd âlim olup tamamlandı», yani kâmil bir âlim oldu gibi; ve benzerleri."},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, AT, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«and sometimes» — qad with the muḍāriʿ: rarely.", "«ve bazen» — muzârîyle kad: taklîl.", segments=wa("قَدْ", "qad", "part")),
  tok("يَتَضَمَّنُ", "tadammana", "verb", [K, FL, MB, F5], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ بَعْدَهُ.", "«contains» — its doer follows.", "«içerir» — fâil sonra."),
  tok("الْفِعْلُ", "fil", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«the verb» — the doer.", "«fiil» — fâil."),
  tok("التَّامُّ", "tamm", "noun", [K, NA, KN], "نَعْتٌ مَرْفُوعٌ.", "«tāmm» — the naʿt.", "«tâm» — sıfat."),
  tok("مَعْنَى", "mana", "noun", [K, MB, ID, MQ], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ.", "«the sense of» — the object, annexed.", "«mânâsını» — mef'ûl, muzâf."),
  tok("صَارَ", "sara", "verb", [K, ID, HT, KN, HV], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«ṣāra» — the verb mentioned, annexed to.", "«sâra» — muzâfun ileyh."),
  tok("فَيَصِيرُ", "sara", "verb", [K, AT, KN, HV], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَيَصِيرُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الْفِعْلُ التَّامُّ).", "«and so becomes» — ṣāra as a sister of kāna, its ism hidden.", "«ve … olur» — kâne'nin kardeşi sâra, ismi gizli.", segments=fa("يَصِيرُ", "sara", "verb")),
  tok("نَاقِصًا", "naqis", "noun", [K, KN], "خَبَرُ يَصِيرُ مَنْصُوبٌ.", "«nāqiṣ» — the khabar of «becomes».", "«nâkıs» — yesîru'nun haberi.", punct="،"),
  nahw(),
  tok("تَمَّ", "tamma", "verb", [K, KN, DV, HT], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ تَامٌّ ضُمِّنَ مَعْنَى صَارَ فَعَمِلَ عَمَلَهُ — نَاقِصٌ هُنَا.", "«became complete» — the tāmm verb carrying the sense of ṣāra, governing like it.", "«tamamlandı» — sâra mânâsı yüklenen tâm fiil, onun gibi amel eder."),
  tok("التِّسْعَةُ", "tisa", "noun", [K, KN], "اسْمُ تَمَّ مَرْفُوعٌ.", "«the nine» — the ism of تَمَّ.", "«dokuz» — temme'nin ismi."),
  tok("بِهٰذَا", "hadha", "pron", [K, HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — بِهٰذَا الْوَاحِدِ.", "«by this» — by this one.", "«bununla» — bu birle.", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("عَشَرَةً", "ashara", "noun", [K, KN], "خَبَرُ تَمَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«ten» — the khabar of تَمَّ.", "«on» — temme'nin haberi.", punct="،"),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»"),
  tok("صَارَ", "sara", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ (التِّسْعَةُ).", "«became» — ṣāra, its ism hidden.", "«oldu» — sâra, ismi gizli."),
  tok("عَشَرَةً", "ashara", "noun", [K, KN], "خَبَرُ صَارَ مَنْصُوبٌ.", "«ten» — the khabar.", "«on» — haber."),
  tok("تَامَّةً", "tamm", "noun", [K, NA, KN], "نَعْتٌ مَنْصُوبٌ.", "«complete» — the naʿt.", "«tam» — sıfat.", punct="،"),
  tok("وَكَمُلَ", "kamula", "verb", [K, AT, KN, HT], "الْوَاوُ عَاطِفَةٌ، وَكَمُلَ لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ تَامٌّ مِنْ بَابِ حَسُنَ ضُمِّنَ مَعْنَى صَارَ.", "«and came to be complete» — bāb حَسُنَ, carrying the sense of ṣāra.", "«ve tamamlandı» — hasüne bâbı, sâra mânâsı yüklenmiş.", segments=wa("كَمُلَ", "kamula", "verb")),
  zayd("زَيْدٌ", "اسْمُ كَمُلَ مَرْفُوعٌ.", "«Zayd» — its ism.", "«Zeyd» — ismi.", tags=[KN]),
  tok("عَالِمًا", "alim-scholar", "noun", [K, KN, IFA], "خَبَرُ كَمُلَ مَنْصُوبٌ.", "«a learned man» — its khabar.", "«âlim» — haberi.", punct="،"),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»"),
  tok("صَارَ", "sara", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (زَيْدٌ).", "«became»", "«oldu»"),
  tok("عَالِمًا", "alim-scholar", "noun", [K, KN, IFA], "خَبَرُ صَارَ مَنْصُوبٌ.", "«a learned man» — the khabar.", "«âlim» — haber."),
  tok("كَامِلًا", "kamil", "noun", [K, NA, KN, IFA], "نَعْتٌ مَنْصُوبٌ.", "«complete» — the naʿt.", "«kâmil» — sıfat.", punct="،"),
  tok("وَغَيْرُ", "ghayr", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مَعْطُوفٌ عَلَى الْجُمْلَةِ الْمَحْكِيَّةِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَمِنْهُ غَيْرُ ذٰلِكَ، مُضَافٌ.", "«and other» — «and of it is other than that»: the khabar of a dropped mubtada, annexed.", "«ve başkası» — «ondan başkası da vardır»: mahzûf mübtedânın haberi, muzâf.", segments=wa("غَيْرُ", "ghayr", "noun")),
  tok("ذٰلِكَ", "dhalika", "pron", [K, ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that»", "«bundan»", punct="."),
 ]})
# ----------- s7 — fronting their khabars
S.append({"id": "s7", "translation": {"en": "And it is permitted to put their khabars before the verbs themselves — except what has مَا at its head, for that is not permitted, as in «standing, Zayd has not ceased».", "tr": "Haberlerini fiillerin kendilerinden öne almak câizdir — başında mâ bulunan hariç, o câiz değildir, «ayakta, Zeyd olmaktan geri kalmadı» gibi."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ تَقْدِيمُ.", "«and it is permitted» — its doer «the fronting».", "«ve câizdir» — fâili takdim.", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ قَدَّمَ.", "«the fronting of» — the doer, annexed.", "«öne alınması» — fâil, muzâf."),
  tok("أَخْبَارِهَا", "khabar-predicate", "noun", [K, ID, KN, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ خَبَرٍ: أَخْبَارُ كَانَ وَأَخَوَاتِهَا.", "«their khabars» — the khabars of kāna and its sisters.", "«haberlerinin» — kâne ve kardeşlerinin haberleri.", segments=[seg("أَخْبَارِ", "khabar-predicate", "noun"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«-den önce»"),
  tok("أَنْفُسِهَا", "nafs", "noun", [K, HJ, ID, TWK, "jam-taksir"], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — عَلَى الْأَفْعَالِ أَنْفُسِهَا.", "«themselves» — the verbs themselves.", "«kendilerinden» — fiillerin kendilerinden.", segments=[seg("أَنْفُسِ", "nafs", "noun"), pr3fs()]),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  tok("مَا", "ma-mawsula", "pron", [K, MW, "istithna"], "اسْمٌ مَوْصُولٌ مُسْتَثْنًى فِي مَحَلِّ نَصْبٍ — مَا كَانَ فِي أَوَّلِهِ مَا.", "«what» — the excepted relative: what has mā at its head.", "«… olan» — müstesnâ mevsûl: başında mâ bulunan."),
  tok("فِي", "fi", "prep", [K, HJ, MW], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«in» — the fronted khabar inside the ṣila.", "«-de» — sılada mukaddem haber."),
  tok("أَوَّلِهِ", "awwal", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its head»", "«başında»", segments=[seg("أَوَّلِ", "awwal", "noun"), pr3msi()]),
  tok("مَا", "ma-nafiya", "part", [K, HT, MK, KN], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ — مُبْتَدَأٌ مُؤَخَّرٌ فِي مَحَلِّ رَفْعٍ: مَا النَّافِيَةُ.", "«mā» — the negation mentioned as a word: the delayed mubtada.", "«mâ» — lafzı kastedilen nefiy: muahhar mübtedâ."),
  tok("فَلَا", "la-nafiya", "part", [K, LN, AT], "الْفَاءُ لِلتَّعْلِيلِ، وَلَا نَافِيَةٌ.", "«for … not»", "«çünkü … -mez»", segments=fa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (التَّقْدِيمُ).", "«is permitted» — the fronting its hidden doer.", "«câiz olmaz» — fâili gizli takdim.", punct="،"),
  nahw(),
  tok("قَائِمًا", "qaim", "noun", [K, KN, IFA, HT, "taqdim-al-musnad"], "لَفْظٌ مَحْكِيٌّ: خَبَرُ مَا زَالَ مُقَدَّمٌ مَنْصُوبٌ — وَهٰذَا هُوَ الْمَمْنُوعُ.", "«standing» — the khabar of mā zāla, fronted: the forbidden order.", "«ayakta» — mâ zâle'nin haberi öne alınmış: yasak olan sıra budur."),
  tok("مَا", "ma-nafiya", "part", [K, LN, KN], "حَرْفُ نَفْيٍ.", "«not»", "«-madı»"),
  tok("زَالَ", "zala", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ بَعْدَهُ.", "«has ceased» — its ism follows.", "«… olmaktan geri kaldı» — ismi sonra."),
  zayd("زَيْدٌ", "اسْمُ مَا زَالَ مَرْفُوعٌ.", "«Zayd» — the ism of mā zāla.", "«Zeyd» — mâ zâle'nin ismi.", punct=".", tags=[KN]),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i]]

CAND = {
 "alama-inform": G("alama-inform", "أَعْلَمَ", "ع ل م", "verb", "to inform someone of something (Form IV; three objects: أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا)", "bildirmek (if'âl; üç mef'ûl alır)", 4, form="IV"),
 "fadil": G("fadil", "فَاضِل", "ف ض ل", "noun", "excellent, virtuous (ism fāʿil of فَضَلَ)", "fâzıl — erdemli", 3),
 "marfu": G("marfu", "مَرْفُوع", "ر ف ع", "noun", "the marfūʿ — a word in rafʿ (ism mafʿūl of رَفَعَ)", "merfû — ref'teki kelime", 3),
 "muqaraba": G("muqaraba", "مُقَارَبَة", "ق ر ب", "noun", "approach, nearness (masdar of قَارَبَ); أَفْعَالُ الْمُقَارَبَةِ", "mukârebe — yaklaşma (kârabe'nin masdarı); mukârebe fiilleri", 4),
 "mutabadir": G("mutabadir", "مُتَبَادِر", "ب د ر", "noun", "what first comes to mind (ism fāʿil of تَبَادَرَ)", "mütebâdir — ilk akla gelen", 4),
 "istahala": G("istahala", "اِسْتَحَالَ", "ح و ل", "verb", "to be transformed, to turn into (Form X; a sister of kāna in the sense of صَارَ)", "dönüşmek (istif'âl; sâra mânâsında kâne'nin kardeşi)", 4, form="X"),
 "amsa": G("amsa", "أَمْسَى", "م س و", "verb", "to become (in the evening) — a sister of kāna", "(akşamleyin) olmak — kâne'nin kardeşi", 3, form="IV"),
 "adha-become": G("adha-become", "أَضْحَى", "ض ح و", "verb", "to become (in the forenoon) — a sister of kāna", "(kuşlukta) olmak — kâne'nin kardeşi", 3, form="IV"),
 "zalla-remain": G("zalla-remain", "ظَلَّ", "ظ ل ل", "verb", "to remain (by day), to keep on — a sister of kāna (doubled)", "(gündüz) kalmak, sürmek — kâne'nin kardeşi (muzâaf)", 3),
 "bata": G("bata", "بَاتَ", "ب ي ت", "verb", "to remain (by night), to pass the night — a sister of kāna (hollow)", "(gece) kalmak, gecelemek — kâne'nin kardeşi (ecvef)", 3),
 "ada-become": G("ada-become", "آضَ", "أ ي ض", "verb", "to become — a sister of kāna (hollow, hamza-initial: آضَ يَئِيضُ أَيْضًا)", "olmak — kâne'nin kardeşi (ecvef, hemzeli: âda yeîdu eydan)", 5),
 "ghada-become": G("ghada-become", "غَدَا", "غ د و", "verb", "to become (in the morning), to go early — a sister of kāna", "(sabah) olmak, erkenden gitmek — kâne'nin kardeşi", 3),
 "raha-become": G("raha-become", "رَاحَ", "ر و ح", "verb", "to become (in the evening), to go — a sister of kāna (hollow)", "(akşam) olmak, gitmek — kâne'nin kardeşi (ecvef)", 3),
 "fatia": G("fatia", "فَتِئَ", "ف ت أ", "verb", "to cease — مَا فَتِئَ: did not cease (also فَتَأَ), a sister of kāna", "vazgeçmek — mâ fetie: vazgeçmedi (fetee de denir), kâne'nin kardeşi", 4),
 "infakka": G("infakka", "اِنْفَكَّ", "ف ك ك", "verb", "to come apart — مَا انْفَكَّ: did not cease (Form VII, doubled), a sister of kāna", "ayrılmak — mâ'nfekke: ayrılmadı (infiâl, muzâaf), kâne'nin kardeşi", 4, form="VII"),
 "bariha": G("bariha", "بَرِحَ", "ب ر ح", "verb", "to leave a place — مَا بَرِحَ: did not cease, a sister of kāna", "ayrılmak — mâ beriha: ayrılmadı, kâne'nin kardeşi", 4),
 "wana": G("wana", "وَنَى", "و ن ي", "verb", "to flag, to slacken — مَا وَنَى: did not cease (lafīf mafrūq: وَنَى يَنِي), a sister of kāna", "gevşemek — mâ venâ: gevşemedi (lefîf-i mefrûk: venâ yenî), kâne'nin kardeşi", 5),
 "kamula": G("kamula", "كَمُلَ", "ك م ل", "verb", "to be complete, to come to perfection (bāb حَسُنَ)", "tamamlanmak, kâmil olmak (hasüne bâbı)", 3),
 "kadha": G("kadha", "كَذَا", None, "part", "likewise, so (كَ + ذَا)", "böylece, keza (ke + zâ)", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that (masc.)", "o, şu", 1),
 "ism": G("ism", "اسْم", "س م و", "noun", "noun, name", "isim", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, hariç", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed (with a past verb); sometimes (with the present)", "gerçekten (mâzîyle); bazen (muzârîyle)", 2),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "did not (negates, jazm, turns the tense back)", "-medi (nefiy, cezm, mâzîye çevirir)", 2),
 "tamm": G("tamm", "تَامّ", "ت م م", "noun", "complete, full (the ism fa'il of تَمَّ)", "tâm, tamam", 3),
 "naqis": G("naqis", "نَاقِص", "ن ق ص", "noun", "lacking, less (ism fa'il)", "nâkıs, eksik", 3),
 "shai": G("shai", "شَائِع", "ش ي ع", "noun", "widespread, current (an active participle of شَاعَ)", "yaygın", 3),
 "itlaq": G("itlaq", "إِطْلَاق", "ط ل ق", "noun", "coming unqualified, without an indication", "ıtlâk — kayıtsız söyleme", 4),
 "sara": G("sara", "صَارَ", "ص ي ر", "verb", "to become", "olmak", 1),
 "ala-return": G("ala-return", "آلَ", "أ و ل", "verb", "to return, to turn into", "dönmek, dönüşmek", 3),
 "rajaa": G("rajaa", "رَجَعَ", "ر ج ع", "verb", "to return", "dönmek", 1),
 "hala": G("hala", "حَالَ", "ح و ل", "verb", "to change, to turn", "değişmek, dönüşmek", 3),
 "tahawwala": G("tahawwala", "تَحَوَّلَ", "ح و ل", "verb", "to turn, to be transformed (Form V)", "dönmek, dönüşmek (tefa''ul)", 3, form="V"),
 "irtadda": G("irtadda", "اِرْتَدَّ", "ر د د", "verb", "to turn back, to revert (Form VIII)", "geri dönmek (iftiâl)", 3, form="VIII"),
 "asbaha": G("asbaha", "أَصْبَحَ", "ص ب ح", "verb", "to become (in the morning)", "(sabahleyin) olmak", 2, form="IV"),
 "dama": G("dama", "دَامَ", "د و م", "verb", "to last, to endure; مَا دَامَ: as long as", "sürmek; mâ dâme: … olduğu sürece", 2),
 "zala": G("zala", "زَالَ", "ز و ل", "verb", "to cease; مَا زَالَ: still, has not ceased", "ortadan kalkmak; mâ zâle: hâlâ", 2),
 "tadammana": G("tadammana", "تَضَمَّنَ", "ض م ن", "verb", "to contain, to imply (Form V)", "içermek (tefa''ul)", 3, form="V"),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "soul, self", "nefis, kendi", 1, plural="أَنْفُس"),
 "kamil": G("kamil", "كَامِل", "ك م ل", "noun", "complete, full (ism fa'il)", "kâmil, tam", 2),
 "sabiq": G("sabiq", "سَابِق", "س ب ق", "noun", "preceding, earlier (ism fa'il of سَبَقَ)", "önceki, sâbık", 2),
 "alim-scholar": G("alim-scholar", "عَالِم", "ع ل م", "noun", "a learned man, a scholar (ism fa'il of عَلِمَ)", "âlim", 2, plural="عُلَمَاء"),
 "bakr": G("bakr", "بَكْر", None, "propn", "Bakr (a man's name)", "Bekr (erkek adı)", 1),
 "ara": G("ara", "أَرَى", "ر أ ي", "verb", "to show (Form IV; three objects)", "göstermek (if'âl; üç mef'ûl)", 3, form="IV"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
W10 = getattr(_sg, "W10", "اِسْتَفْعَلَ يَسْتَفْعِلُ"); W4 = _sg.W4; W5 = _sg.W5; W7 = getattr(_sg, "W7", "اِنْفَعَلَ يَنْفَعِلُ")
def doubled(bab, yv, m, mm, d, dd, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    b = _sg.BABS[bab]
    return _sg.idgham(_sg.entry(b[0] + " — مُضَاعَفٌ", b[1], masdar, fail, _sg.mazi14(m, mm), _sg.mudari14(yv, d, dd), amr,
                                "يَ" + d + "َ", "يَ" + d + "َ", "تَ" + d + "َ", maful, pmz, pmd, note))
put_morph(mo, "alama-inform", _sg.derived(_sg.B4, W4, "ُ", "أَعْلَم", "عْلِم", "أَعْلِم", "إِعْلَام", "مُعْلِم", "مُعْلَم", "أُعْلِمَ", "يُعْلَمُ", "أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا يُعْلِمُ: جَعَلَهُ يَعْلَمُ — مُتَعَدٍّ إِلَى ثَلَاثَةِ مَفَاعِيلَ."))
put_morph(mo, "istahala", _sg.derived_hollow(_sg.B10 + " — أَجْوَفُ وَاوِيٌّ", W10, "َ", "اِسْتَحَال", "اِسْتَحَل", "سْتَحِيل", "سْتَحِل", "اِسْتَحِيل", "اِسْتَحِل", "اِسْتِحَالَة", "مُسْتَحِيل", None, None, None, "اِسْتَحَالَ الشَّيْءُ يَسْتَحِيلُ اسْتِحَالَةً: تَحَوَّلَ — لَازِمٌ، مِنْ أَخَوَاتِ كَانَ بِمَعْنَى صَارَ."))
put_morph(mo, "amsa", _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", W4, "ُ", "أَمْسَ", "مْس", "i", "أَمْس", "إِمْسَاء", "مُمْسٍ", None, None, None, "أَمْسَى يُمْسِي: دَخَلَ فِي الْمَسَاءِ؛ صَارَ — مِنْ أَخَوَاتِ كَانَ."))
put_morph(mo, "adha-become", _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", W4, "ُ", "أَضْحَ", "ضْح", "i", "أَضْح", "إِضْحَاء", "مُضْحٍ", None, None, None, "أَضْحَى يُضْحِي: دَخَلَ فِي الضُّحَى؛ صَارَ — مِنْ أَخَوَاتِ كَانَ."))
put_morph(mo, "zalla-remain", doubled("samia", "َ", "ظَلّ", "ظَلِل", "ظَلّ", "ظْلَل", ["ظَلَّ", "ظَلَّا", "ظَلُّوا", "ظَلِّي", "ظَلَّا", "اِظْلَلْنَ"], "ظُلُول", "ظَالّ", None, None, None, "ظَلَّ يَظَلُّ ظُلُولًا: دَامَ نَهَارًا — مُضَاعَفٌ مِنْ بَابِ سَمِعَ (ظَلِلْتُ)، مِنْ أَخَوَاتِ كَانَ."))
put_morph(mo, "bata", _sg.idgham(_sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "بَات", "بِت", "بِيت", "بِت", "بِيت", "بِت", "مَبِيت", "بَائِت", None, None, None, _sg.HOLLOW_NOTE.format(ex="بِتَّ"))))
put_morph(mo, "ada-become", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ مَهْمُوزُ الْفَاءِ", "آض", "إِض", "ئِيض", "ئِض", "إِيض", "إِض", "أَيْض", "آئِض", None, None, None, "آضَ يَئِيضُ أَيْضًا: صَارَ، رَجَعَ — مَهْمُوزٌ أَجْوَفُ؛ مِنْهُ أَيْضًا."))
put_morph(mo, "ghada-become", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "غَدَ", "غْد", "u", "اُغْد", "غُدُوّ", "غَادٍ", None, None, None, "غَدَا يَغْدُو غُدُوًّا: ذَهَبَ غُدْوَةً؛ صَارَ — مِنْ أَخَوَاتِ كَانَ."))
put_morph(mo, "raha-become", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "رَاح", "رُح", "رُوح", "رُح", "رُوح", "رُح", "رَوَاح", "رَائِح", None, None, None, _sg.HOLLOW_NOTE.format(ex="رُحْتَ")))
put_morph(mo, "fatia", _sg.sound1("samia", "فَتِئ", "فْتَأ", "اِفْتَأ", "فَتْء", "فَاتِئ", None, None, None, "فَتِئَ يَفْتَأُ: زَالَ؛ وَيُقَالُ فَتَأَ — لَا يُسْتَعْمَلُ إِلَّا مَنْفِيًّا: مَا فَتِئَ."))
put_morph(mo, "infakka", _sg.idgham(_sg.entry(_sg.B7 + " — مُضَاعَفٌ", W7, "اِنْفِكَاك", "مُنْفَكّ", _sg.mazi14("اِنْفَكّ", "اِنْفَكَك"), _sg.mudari14("َ", "نْفَكّ", "نْفَكِك"), ["اِنْفَكَّ", "اِنْفَكَّا", "اِنْفَكُّوا", "اِنْفَكِّي", "اِنْفَكَّا", "اِنْفَكِكْنَ"], "يَنْفَكَّ", "يَنْفَكَّ", "تَنْفَكَّ", None, None, None, "اِنْفَكَّ يَنْفَكُّ: اِنْفَصَلَ؛ مَا انْفَكَّ: مَا زَالَ — مُضَاعَفٌ مِنْ بَابِ الِانْفِعَالِ.")))
put_morph(mo, "bariha", _sg.sound1("samia", "بَرِح", "بْرَح", "اِبْرَح", "بَرَاح", "بَارِح", None, None, None, "بَرِحَ الْمَكَانَ يَبْرَحُ: فَارَقَهُ؛ مَا بَرِحَ: مَا زَالَ."))
put_morph(mo, "wana", _sg.naqis1("daraba", "لَفِيفٌ مَفْرُوقٌ", "y", "وَنَ", "ن", "i", "ن", "وَنًى", "وَانٍ", None, None, None, "وَنَى يَنِي وَنًى: ضَعُفَ وَفَتَرَ — لَفِيفٌ مَفْرُوقٌ، تَسْقُطُ وَاوُهُ فِي الْمُضَارِعِ كَالْمِثَالِ؛ مَا وَنَى: مَا زَالَ."))
put_morph(mo, "kamula", _sg.sound1("karuma", "كَمُل", "كْمُل", "اُكْمُل", "كَمَال", "كَامِل", None, None, None, "كَمُلَ يَكْمُلُ كَمَالًا: تَمَّ — مِنْ بَابِ حَسُنَ، وَاسْمُ فَاعِلِهِ كَامِلٌ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch10 gloss+morph ok", len(GLOSS_ADD), "verbs:", [k for k in ("alama-inform", "istahala", "amsa", "adha-become", "zalla-remain", "bata", "ada-become", "ghada-become", "raha-become", "fatia", "infakka", "bariha", "wana", "kamula", "ara", "sara", "ala-return", "hala", "rajaa", "tahawwala", "irtadda", "asbaha", "dama", "zala", "tadammana") if k in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْفِعْلُ التَّامُّ وَالنَّاقِصُ، وَكَانَ وَأَخَوَاتُهَا عِنْدَ الْبِرْكِوِيِّ", "en": "The tāmm and the nāqiṣ verb, and kāna's sisters as Birgivī counts them", "tr": "Tâm ve nâkıs fiil, Birgivî'nin saydığı kâne ve kardeşleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الفعل التام والناقص", "الكافية لابن الحاجب — كان وأخواتها", "قطر الندى لابن هشام — الأفعال الناقصة"],
 "amil": "الْفِعْلُ النَّاقِصُ — raises its ism and puts its khabar in naṣb; it needs a manṣūb beyond its marfūʿ, and enters only on a mubtadaʾ and a khabar in origin",
 "question": {
  "en": ["How does a verb reach three objects? أَعْلَمَ and أَرَى: the first object is like the object of أَعْطَيْتُ (a plain thing), the last two are like the two objects of عَلِمْتُ — a mubtadaʾ and a khabar in origin (أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا).",
         "What must every verb have? A marfūʿ — no verb stands without one.",
         "What is a TĀMM verb? One that completes a sentence with its marfūʿ and needs nothing else: its marfūʿ is the doer, its manṣūb (if transitive) the object — every verb met so far.",
         "What is a NĀQIṢ verb? One that still needs a manṣūb governed word: its marfūʿ is its ISM, its manṣūb its KHABAR; in origin it enters only on a mubtadaʾ and a khabar.",
         "Which are the nāqiṣ verbs with no sense of approach? كَانَ and صَارَ — and آلَ، رَجَعَ، حَالَ، اسْتَحَالَ، تَحَوَّلَ، ارْتَدَّ، جَاءَ، قَعَدَ when they mean صَارَ; أَصْبَحَ، أَمْسَى، أَضْحَى، ظَلَّ، بَاتَ، آضَ، غَدَا، رَاحَ; مَا فَتِئَ، مَا انْفَكَّ، مَا بَرِحَ، مَا وَنَى (all meaning مَا زَالَ); مَا دَامَ and لَيْسَ.",
         "Can a tāmm verb turn nāqiṣ? Yes, when it takes on the sense of صَارَ: تَمَّ التِّسْعَةُ بِهٰذَا عَشَرَةً (became a complete ten), كَمُلَ زَيْدٌ عَالِمًا (came to be a complete scholar).",
         "May their khabar stand before them? Yes — except the sisters that begin with مَا: قَائِمًا مَا زَالَ زَيْدٌ is not allowed, because nothing may stand before the negation that these verbs never leave.",
         "What does the engine READ here? The DabtEngine raises the noun after كَانَ and its sisters as the ism and writes the khabar's naṣb, keeps a verb mentioned as a word as written, reads مَا with its verb as one quoted word, and takes a tāmm verb's noun after it as its ism only where the chapter says the verb carries the sense of صَارَ."],
  "tr": ["Fiil üç mef'ûle nasıl ulaşır? A'leme ve erâ: birinci mef'ûl a'taytü'nün mef'ûlü gibi (düz bir şey), son ikisi alimtü'nün iki mef'ûlü gibi — aslında mübtedâ ve haber (a'leme Zeydün Amren Bekren fâdılen).",
         "Her fiilde ne bulunmalıdır? Bir merfû — merfûsuz fiil olmaz.",
         "TÂM fiil nedir? Merfûuyla bir cümle tamamlayan ve başkasına muhtaç olmayan fiil: merfûu fâil, mansûbu (müteaddî ise) mef'ûl — şimdiye kadar görülen her fiil.",
         "NÂKIS fiil nedir? Hâlâ mansûb bir ma'mûle muhtaç olan fiil: merfûu İSMİ, mansûbu HABERİ; aslında yalnız mübtedâ ve habere girer.",
         "Yaklaşma mânâsı taşımayan nâkıs fiiller hangileridir? Kâne ve sâra — sâra mânâsında olduklarında âle, racea, hâle, istehâle, tehavvele, irtedde, câe, kaade; asbaha, emsâ, adhâ, zalle, bâte, âda, gadâ, râha; mâ fetie, mâ'nfekke, mâ beriha, mâ venâ (hepsi mâ zâle mânâsında); mâ dâme ve leyse.",
         "Tâm fiil nâkıs olabilir mi? Evet, sâra mânâsını yüklendiğinde: temme't-tis'atü bi-hâzâ aşeraten (tam bir on oldu), kemüle Zeydün âlimen (kâmil bir âlim oldu).",
         "Haberleri onlardan önce gelebilir mi? Evet — başında mâ bulunan kardeşler hariç: kâimen mâ zâle Zeydün câiz değildir, çünkü bu fiillerin hiç ayrılmadığı nefyin önüne bir şey geçemez.",
         "Motor burada neyi OKUR? DabtEngine kâne ve kardeşlerinden sonraki ismi isim olarak ref eder, haberin nasbını yazar, lafzı kastedilen fiili olduğu gibi tutar, mâ'yı fiiliyle tek bir hikâye kelimesi olarak okur ve tâm fiilin ardındaki ismi ancak bölümün «sâra mânâsı yüklendi» dediği yerde onun ismi sayar."]
 },
 "plain": {"en": "Every verb has a word in rafʿ. If that word finishes the thought, the verb is complete and the word is its doer. If it still needs a word in naṣb — «Zayd was … a scholar» — it is deficient: its noun, then its predicate. The ones beginning with «not» cannot have the predicate put in front.",
           "tr": "Her fiilin merfû bir kelimesi vardır. O kelime düşünceyi bitiriyorsa fiil tamdır, kelime de fâilidir. Fiil bitmek için hâlâ mansûb bir kelime istiyorsa — «Zeyd … âlim idi» — nâkıstır: birinci kelime ismi, ikincisi haberidir. Birgivî bunları sayar ve «mâ» ile başlayanların haberinin öne alınamayacağını söyler."},
 "explanation": {"en": "The third kind of the mutaʿaddī is transitive to three objects, as أَعْلَمَ and أَرَى: their first object is like the object of the bāb of أَعْطَيْتُ, and the last two like the two objects of the bāb of عَلِمْتُ — أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا. Then know that every verb must have a marfūʿ. If a sentence is complete with it and the verb needs nothing else, it is named a tāmm verb, its marfūʿ a doer and its manṣūb — if it is transitive — an object, like the verbs before. If it needs a manṣūb governed word it is named a nāqiṣ verb, its marfūʿ its ism and its manṣūb its khabar; in origin it enters only on the mubtadaʾ and the khabar. It is of two divisions. The first signifies no sense of approach — the common one, what first comes to mind when «the nāqiṣ verb» is said: كَانَ and صَارَ, and likewise آلَ، رَجَعَ، حَالَ، اسْتَحَالَ، تَحَوَّلَ، ارْتَدَّ، جَاءَ، قَعَدَ when they are in the sense of صَارَ; أَصْبَحَ، أَمْسَى، أَضْحَى، ظَلَّ، بَاتَ، آضَ، غَدَا، رَاحَ; مَا فَتِئَ (with the tāʾ's fatḥa and its kasra), مَا انْفَكَّ، مَا بَرِحَ، مَا وَنَى — all in the sense of مَا زَالَ — and مَا دَامَ and لَيْسَ. A tāmm verb may carry the sense of صَارَ and become nāqiṣ: تَمَّ التِّسْعَةُ بِهٰذَا عَشَرَةً (became a complete ten), كَمُلَ زَيْدٌ عَالِمًا (became a complete scholar), and other such. Their khabars may be put before them, except the ones opened by مَا: قَائِمًا مَا زَالَ زَيْدٌ is not allowed. The second division — the verbs of approach — follows.",
                 "tr": "Müteaddînin üçüncü türü üç mef'ûle müteaddîdir: a'leme ve erâ gibi; birinci mef'ûlleri a'taytü bâbının mef'ûlü, son ikisi alimtü bâbının iki mef'ûlü gibidir — a'leme Zeydün Amren Bekren fâdılen. Sonra bil ki her fiilin mutlaka bir merfûu vardır. Onunla cümle tamam olur ve fiil başkasına muhtaç olmazsa tâm fiil, merfûu fâil, mansûbu — müteaddî ise — mef'ûl diye adlandırılır, önceki fiiller gibi. Mansûb bir ma'mûle muhtaç olursa nâkıs fiil, merfûu ismi, mansûbu haberi diye adlandırılır; aslında yalnız mübtedâ ve habere girer. İki kısımdır. Birincisi yaklaşma mânâsına delâlet etmeyendir — yaygın olan, «nâkıs fiil» denince ilk akla gelen: kâne ve sâra; sâra mânâsında olduklarında âle, racea, hâle, istehâle, tehavvele, irtedde, câe, kaade; asbaha, emsâ, adhâ, zalle, bâte, âda, gadâ, râha; mâ fetie (tânın fethası ve kesresiyle), mâ'nfekke, mâ beriha, mâ venâ — hepsi mâ zâle mânâsında — ve mâ dâme ile leyse. Tâm fiil sâra mânâsını yüklenip nâkıs olabilir: temme't-tis'atü bi-hâzâ aşeraten (tam bir on oldu), kemüle Zeydün âlimen (kâmil bir âlim oldu) ve benzerleri. Haberleri onlardan önce gelebilir, mâ ile açılanlar hariç: kâimen mâ zâle Zeydün câiz değildir. İkinci kısım — mukârebe fiilleri — bundan sonra gelir."},
 "examples": [
  {"ar": "أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا", "en": "three objects: the first a plain thing, the last two a mubtadaʾ and khabar in origin", "tr": "üç mef'ûl: birincisi düz bir şey, son ikisi aslında mübtedâ ve haber", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "يُسَمَّى فِعْلًا تَامًّا، وَمَرْفُوعُهُ فَاعِلًا", "en": "the tāmm verb: its marfūʿ the doer", "tr": "tâm fiil: merfûu fâil", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "يُسَمَّى فِعْلًا نَاقِصًا، وَمَرْفُوعُهُ اسْمًا لَهُ، وَمَنْصُوبُهُ خَبَرًا لَهُ", "en": "the nāqiṣ verb: ism and khabar", "tr": "nâkıs fiil: isim ve haber", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "كَانَ وَصَارَ، وَكَذَا آلَ وَرَجَعَ وَحَالَ وَاسْتَحَالَ وَتَحَوَّلَ وَارْتَدَّ وَجَاءَ وَقَعَدَ إِذَا كُنَّ بِمَعْنَى صَارَ", "en": "the sisters that mean «to become»", "tr": "«olmak» mânâsındaki kardeşler", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "مَا فَتِئَ وَمَا انْفَكَّ وَمَا بَرِحَ وَمَا وَنَى كُلُّهَا بِمَعْنَى مَا زَالَ", "en": "the sisters that never leave the negation", "tr": "nefiyden hiç ayrılmayan kardeşler", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "تَمَّ التِّسْعَةُ بِهٰذَا عَشَرَةً", "en": "a tāmm verb carrying the sense of ṣāra, governing an ism and a khabar", "tr": "sâra mânâsı yüklenip isim ve habere amel eden tâm fiil", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "قَائِمًا مَا زَالَ زَيْدٌ", "en": "the forbidden fronting before a sister opened by mā", "tr": "mâ ile açılan kardeşin önüne alınan haber — yasak", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "كَانَ زَيْدٌ عَالِمٌ", "right": "كَانَ زَيْدٌ عَالِمًا", "why": {"en": "the nāqiṣ verb puts its khabar in naṣb — it still needed a manṣūb to be complete", "tr": "nâkıs fiil haberini nasb eder — tamam olmak için hâlâ bir mansûba muhtaçtı"}},
  {"wrong": "قَائِمًا مَا زَالَ زَيْدٌ", "right": "مَا زَالَ زَيْدٌ قَائِمًا", "why": {"en": "the khabar of a sister opened by مَا may not stand before it", "tr": "mâ ile açılan kardeşin haberi onun önüne alınamaz"}},
  {"wrong": "زَالَ زَيْدٌ قَائِمًا", "right": "مَا زَالَ زَيْدٌ قَائِمًا", "why": {"en": "زَالَ, فَتِئَ, انْفَكَّ, بَرِحَ, وَنَى work as sisters of kāna only under a negation", "tr": "zâle, fetie, infekke, beriha, venâ ancak nefiy altında kâne'nin kardeşi olur"}},
  {"wrong": "أَعْلَمَ زَيْدٌ عَمْرًا بَكْرٌ فَاضِلٌ", "right": "أَعْلَمَ زَيْدٌ عَمْرًا بَكْرًا فَاضِلًا", "why": {"en": "the mubtadaʾ and khabar that follow the first object become the second and third objects, in naṣb", "tr": "birinci mef'ûlden sonraki mübtedâ ve haber ikinci ve üçüncü mef'ûl olarak nasb edilir"}},
 ],
}
ADD_EN = (" Chapter 10 (print pp. 105-106): the mutaʿaddī's third kind, to three objects (s1); every verb's marfūʿ, the tāmm verb (s2) and the nāqiṣ verb "
          "(s3); its two divisions and the first — kāna, ṣāra and the verbs that mean ṣāra (s4), the sisters of the times of day and the negated ones, "
          "مَا دَامَ and لَيْسَ (s5); a tāmm verb carrying the sense of ṣāra (s6); the fronting of their khabars and the مَا-sisters' bar on it (s7). "
          "The print's doubled «وما دام» before «كلها بمعنى ما زال» is read once, as the received text has it; the garbled clause on the substitution "
          "of إِنْ and لَمْ for مَا (وكذا إن لم يدل ما بأن النافية … نحو قائما لم يزل زيد) is HELD BACK pending review and the chapter stops before it.")
ADD_TR = (" Onuncu bab (baskı s. 105-106): müteaddînin üç mef'ûle olan üçüncü türü (s1); her fiilin merfûu, tâm fiil (s2) ve nâkıs fiil (s3); iki kısmı ve "
          "birincisi — kâne, sâra ve sâra mânâsındaki fiiller (s4), günün vakitlerinin kardeşleri ve menfî olanlar, mâ dâme ve leyse (s5); sâra mânâsını "
          "yüklenen tâm fiil (s6); haberlerinin öne alınması ve mâ'lı kardeşlerde bunun yasağı (s7). Baskının «كلها بمعنى ما زال» öncesindeki mükerrer "
          "«وما دام»ı rivâyet edilen metindeki gibi bir kez okundu; mâ yerine in ve lem konmasına dair bozuk cümle (وكذا إن لم يدل ما بأن النافية … نحو قائما "
          "لم يزل زيد) inceleme beklediğinden ALIKONDU, bab ondan önce biter.")
write_out(10, S, TITLE, ADD_EN, ADD_TR, "pp. 105-106", GLOSS_ADD, notes=(NOTE,),
          related=((KN, [K]), (MFN, [K]), (K9, [K]), ("al-lazim-wal-mutaaddi", [K]), (TSY, [K]), ("taqdim-al-musnad", [K])))
report(10, S, GLOSS_ADD, (NOTE,))
