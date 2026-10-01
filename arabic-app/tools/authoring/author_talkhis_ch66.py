# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 66: TA'KID AL-MADH BIMA YUSHBIHU AL-DHAMM (two kinds, and a third; the istidrak standing for the
exception), TA'KID AL-DHAMM BIMA YUSHBIHU AL-MADH (two kinds), ISTITBA' and IDMAJ. Source lines ~4300-4345 (sahifa 148-150).

  RESTORED (the source carries the step only in Turkish): s1, s2, s4, s6a, s7 (the madh's definition, its two kinds, the third
  kind's heading, the istidrak note), s9, s10a, s11a (the dhamm's definition and kinds), s12 (istitba's definition), s14 (idmaj's
  definition). The examples (s3, s5, s6, s8, s10, s11, s13, s15) are the source's printed Arabic; the Hamadhani's nisba is written
  الْهَمَذَانِيِّ as the received text has it (the print: الهمدانى), recorded in the attribution.

  python3 tools/authoring/author_talkhis_ch66.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

M = "takid-al-madh-wal-dhamm"; I = "istitba-wa-idmaj"
TITLE = {"ar": "تَأْكِيدُ الْمَدْحِ بِمَا يُشْبِهُ الذَّمَّ وَعَكْسُهُ، وَالِاسْتِتْبَاعُ، وَالْإِدْمَاجُ", "en": "Praise confirmed by what looks like blame, and its reverse; Istitbaʿ; Idmaj", "tr": "Zemme benzeyenle medhin tekidi ve aksi; İstitbâ'; İdmâc"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them is» — the fronted khabar.", "«ve onlardan biri» — öne alınmış haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def wahuwa(tag):
    return tok("وَهُوَ","huwa","pron",[tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")])
def an_masd(tag):
    return tok("أَنْ","an-masdariyya","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the clause is the khabar.", "«-mak» — masdar yapan en; cümle haberdir.")
def kaqawl(tag, punct=None):
    return tok("كَقَوْلِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")], punct=punct)
def kaqh(tag, punct=":"):
    return tok("كَقَوْلِهِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«as in his saying».", "«onun sözü gibi».",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")], punct=punct)
def kaqk(tag):
    return tok("كَقَوْلِكَ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«as when you say».", "«senin şu sözün gibi».",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("كَ","pron-2ms","pron")], punct=":")
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def abi(tag, name, name_lex, name_ar, name_en, name_tr, punct=":"):
    return [tok("أَبِي","ab","noun",[tag, "five-nouns", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — one of the five nouns, majrur by its ya.", "«Ebû» — beş isimden, yâ ile mecrûr."),
            tok(name, name_lex, "noun", [tag, "idafa-definiteness"], name_ar, name_en, name_tr, punct=punct)]
def sifat(tag, which, case_ar, case_en, case_tr, punct=None):
    # صِفَةُ مَدْحٍ / صِفَةُ ذَمٍّ — the construct pair
    k = {"madh": ("مَدْحٍ", "madh", "praise", "medih"), "dhamm": ("ذَمٍّ", "dhamm", "blame", "zem")}[which]
    return [tok("صِفَةُ" if case_ar == "raf" else "صِفَةِ","sifa","noun",[tag, "idafa-definiteness"], ("فَاعِلٌ مَرْفُوعٌ مُضَافٌ." if case_ar == "raf" else "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.") if case_en is None else case_en, "«a quality of» — annexed.", "«bir sıfatı» — muzâf."),
            tok(k[0], k[1], "noun", [tag, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«%s»." % k[2], "«%s»." % k[3], punct=punct)]
def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)

# ----------- s1 — the definition: two kinds (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is CONFIRMING PRAISE BY WHAT LOOKS LIKE BLAME, and it is of two kinds." + R_EN,
 "tr": "Onlardan biri ZEMME BENZEYENLE MEDHİN TEKİDİDİR; iki kısımdır." + R_TR},
 "tokens": [
  minha(M),
  tok("تَأْكِيدُ","takid","noun",[M, "mubtada-khabar", "idafa-definiteness", "masdar", "form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ أَكَّدَ.", "«the confirming of» — the delayed mubtada.", "«tekidi» — sona bırakılmış mübtedâ."),
  tok("الْمَدْحِ","madh","noun",[M, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«praise».", "«medhin»."),
  tok("بِمَا","ma-mawsula","pron",[M, "huruf-jarr", "ism-mawsul"], "الْبَاءُ جَارَّةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«by what».", "«şeyle».", segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُشْبِهُ","ashbaha","verb",[M, "ism-mawsul", "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«looks like» — the sila.", "«benzeyen» — sıla."),
  tok("الذَّمَّ","dhamm","noun",[M, "maful-bihi", "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«blame» — the object.", "«zemme» — mef'ûl.", punct="،"),
  wahuwa(M),
  tok("ضَرْبَانِ","darb","noun",[M, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنَّى ضَرْبٍ.", "«two kinds» — the khabar, a dual.", "«iki kısım» — haber, tesniye.", punct=".")]})

# ----------- s2 — the first, the finer kind (RESTORED matn)
S.append({"id": "s2", "translation": {
 "en": "The finer of the two: that a quality of PRAISE be excepted from a quality of BLAME denied of the thing, on the assumption that it enters it." + R_EN,
 "tr": "Daha güzeli: şeyden nefyedilmiş bir ZEM sıfatından, ona dahil olduğu farz edilerek bir MEDİH sıfatının istisna edilmesidir." + R_TR},
 "tokens": [
  tok("أَفْضَلُهُمَا","afdal","noun",[M, "mubtada-khabar", "ism-tafdil", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — اسْمُ تَفْضِيلٍ.", "«the finer of them» — the mubtada; an ism tafdil.", "«ikisinin daha güzeli» — mübtedâ; ism-i tafdîl.", segments=[seg("أَفْضَلُ","afdal","noun"), seg("هُمَا","pron-3d","pron")]),
  an_masd(M),
  tok("يُسْتَثْنَى","istathna","verb",[M, "an-masdariyya", "naib-al-fail", "form-x-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«be excepted» — a passive under an.", "«istisna edilmesi» — en altında meçhul."),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  *sifat(M, "dhamm", "jarr", "مَجْرُورٌ مُضَافٌ.", None),
  tok("مَنْفِيَّةٍ","manfi","noun",[M, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولِ نَفَى.", "«denied» — a na't.", "«nefyedilmiş» — na't."),
  tok("عَنِ","an","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of».", "«-den»."),
  tok("الشَّيْءِ","shay","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the thing».", "«şeyden»."),
  *sifat(M, "madh", "raf", "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", None),
  tok("بِتَقْدِيرِ","taqdir","noun",[M, "huruf-jarr", "idafa-definiteness", "masdar"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«on the assumption of».", "«farz ederek».", segments=[seg("بِ","bi","part"), seg("تَقْدِيرِ","taqdir","noun")]),
  tok("دُخُولِهَا","dukhul","noun",[M, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its entering».", "«dahil olmasını»."
      , segments=[seg("دُخُولِ","dukhul","noun"), seg("هَا","pron-3fs","pron")]),
  tok("فِيهَا","fi","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«into it».", "«ona».", segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")], punct=".")]})

# ----------- s3 — al-Nabigha: no fault but the notched swords
S.append({"id": "s3", "translation": {
 "en": "As al-Nabigha says: «There is no fault in them — EXCEPT that their swords • bear notches from clashing with the squadrons»." + R_EN,
 "tr": "Nâbiga'nın dediği gibi: «Onlarda hiçbir kusur yok — ŞU KADAR Kİ kılıçlarında • bölüklerle çarpışmaktan gedikler var»." + R_TR},
 "tokens": [
  kaqawl(M),
  tok("النَّابِغَةِ","nabigha","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — النَّابِغَةُ الذُّبْيَانِيُّ.", "«al-Nabigha» — al-Dhubyani.", "«Nâbiga» — ez-Zübyânî.", punct=":"),
  tok("وَلَا","la","part",[M, "la-nafiya-lil-jins"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no» — the la that denies the genus.", "«ve hiç … yok» — cins nefyeden lâ.", segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("عَيْبَ","ayb","noun",[M, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«fault» — la's ism, built on the fatha.", "«kusur» — lâ'nın ismi, fetha üzere mebnî."),
  tok("فِيهِمْ","fi","part",[M, "huruf-jarr", "la-nafiya-lil-jins"], "جَارٌّ وَمَجْرُورٌ خَبَرُ لَا.", "«in them» — la's khabar.", "«onlarda» — lâ'nın haberi.", segments=[seg("فِي","fi","part"), seg("هِمْ","pron-3mp","pron")]),
  tok("غَيْرَ","ghayr","noun",[M, "istithna", "idafa-definiteness"], "مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ مُضَافٌ — أَدَاةُ الِاسْتِثْنَاءِ الَّتِي يَقُومُ عَلَيْهَا التَّأْكِيدُ.", "«except» — mansub as the exception; the adat the confirming rides on.", "«şu kadar ki» — istisna üzere mansûb; tekidin bindiği edat."),
  tok("أَنَّ","anna","part",[M, "inna-wa-akhawatuha", "an-masdariyya"], "حَرْفٌ نَاسِخٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُضَافٌ إِلَيْهِ.", "«that» — its clause annexed to ghayr.", "«…-sı» — cümlesi gayr'a muzâfun ileyh."),
  tok("سُيُوفَهُمْ","sayf","noun",[M, "inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], "اسْمُ أَنَّ مَنْصُوبٌ مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ سَيْفٍ.", "«their swords» — anna's ism.", "«kılıçları» — enne'nin ismi.", segments=[seg("سُيُوفَ","sayf","noun"), seg("هُمْ","pron-3mp","pron")], punct="*"),
  tok("بِهِنَّ","bi","part",[M, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — الضَّمِيرُ لِلسُّيُوفِ.", "«in them» — the fronted khabar; the pronoun for the swords.", "«onlarda» — öne alınmış haber; zamir kılıçlara.", segments=[seg("بِ","bi","part"), seg("هِنَّ","pron-3fp","pron")]),
  tok("فُلُولٌ","fulul","noun",[M, "mubtada-khabar", "jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ — جَمْعُ فَلٍّ: الثَّلْمُ.", "«notches» — the delayed mubtada; the clause is anna's khabar.", "«gedikler» — sona bırakılmış mübtedâ; cümle enne'nin haberi."),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ.", "«from».", "«-den»."),
  tok("قِرَاعِ","qira","noun",[M, "huruf-jarr", "idafa-definiteness", "masdar", "form-iii-verbs"], "مَجْرُورٌ مُضَافٌ — مَصْدَرُ قَارَعَ: الْمُضَارَبَةُ.", "«clashing with» — the masdar of qaraʿa.", "«çarpışmak» — kâraa'nın masdarı."),
  tok("الْكَتَائِبِ","katiba","noun",[M, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ كَتِيبَةٍ: الْجَيْشُ.", "«the squadrons» — the plural of katiba.", "«bölükler» — ketîbe'nin çoğulu.", punct=".")]})
S[-1]["badi"] = [{"kind": "takid-madh", "sub": "istithna-min-dhamm", "receipt": "ghayr", "word": ix(S[-1], "غَيْرَ"), "first": [ix(S[-1], "عَيْبَ")], "second": [ix(S[-1], "فُلُولٌ")]}]

# ----------- s4 — the second kind (RESTORED matn)
S.append({"id": "s4", "translation": {
 "en": "The second: that a quality of praise be affirmed of a thing, and followed by an adat of exception after which comes ANOTHER quality of praise of it." + R_EN,
 "tr": "İkincisi: bir şeye bir medih sıfatının ispat edilip, ardından ona ait BAŞKA bir medih sıfatının geldiği bir istisna edatıyla takip edilmesidir." + R_TR},
 "tokens": [
  wa_conj("وَالثَّانِي","thani","noun",[M, "mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second» — the mubtada.", "«ve ikincisi» — mübtedâ."),
  an_masd(M),
  tok("يُثْبَتَ","athbata","verb",[M, "an-masdariyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be affirmed» — a passive under an.", "«ispat edilmesi» — en altında meçhul."),
  tok("لِشَيْءٍ","shay","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of a thing».", "«bir şeye».", segments=[seg("لِ","li","part"), seg("شَيْءٍ","shay","noun")]),
  *sifat(M, "madh", "raf", "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", None),
  wa_conj("وَيُعَقَّبَ","aqqaba","verb",[M, "atf-nasaq", "naib-al-fail", "form-ii-verbs"], "يُعَقَّبَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ عَلَى الْمَنْصُوبِ.", "«and be followed» — joined to the nasb.", "«ve takip edilmesi» — mansûba ma'tûf."),
  tok("بِأَدَاةِ","adat","noun",[M, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«by an adat of».", "«bir edatıyla».", segments=[seg("بِ","bi","part"), seg("أَدَاةِ","adat","noun")]),
  tok("اسْتِثْنَاءٍ","istithna","noun",[M, "idafa-definiteness", "masdar", "form-x-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اسْتَثْنَى.", "«exception».", "«istisna»."),
  tok("تَلِيهَا","waliya","verb",[M, "jumla-sifa", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ لِأَدَاةِ.", "«after which comes» — the clause a na't of the adat.", "«ardından gelen» — cümle edatın na'tı.", segments=[seg("تَلِي","waliya","verb"), seg("هَا","pron-3fs","pron")]),
  *sifat(M, "madh", "raf", "فَاعِلٌ مَرْفُوعٌ مُضَافٌ.", None),
  tok("أُخْرَى","ukhra","noun",[M, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — a na't.", "«başka» — na't."),
  tok("لَهُ","lahu","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of it».", "«ona ait».", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s5 — the hadith: the most eloquent of the Arabs, bayda anni min Quraysh
S.append({"id": "s5", "translation": {
 "en": "As in his saying ﷺ: «I am the most eloquent of the Arabs — BAYDA (except) that I am of Quraysh»." + R_EN,
 "tr": "Onun ﷺ sözünde olduğu gibi: «Ben Arabın en fasihiyim — ŞU KADAR Kİ (beyde) ben Kureyş'tenim»." + R_TR},
 "tokens": [
  kaqh(M, punct=None), saw(M),
  tok("أَنَا","ana","pron",[M, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«I» — the mubtada.", "«ben» — mübtedâ."),
  tok("أَفْصَحُ","afsah","noun",[M, "mubtada-khabar", "ism-tafdil", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«the most eloquent of» — the khabar.", "«en fasihi» — haber."),
  tok("الْعَرَبِ","arab","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Arabs».", "«Arabın»."),
  tok("بَيْدَ","bayd","noun",[M, "istithna", "idafa-definiteness"], "مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ مُضَافٌ، بِمَعْنَى غَيْرَ — لَا يُسْتَعْمَلُ إِلَّا مُضَافًا إِلَى أَنَّ.", "«bayda» — mansub as the exception, «other than»; used only before anna.", "«beyde» — istisna üzere mansûb, «gayra» mânâsında; yalnız enne'ye muzâf gelir."),
  tok("أَنِّي","anna","part",[M, "inna-wa-akhawatuha", "ya-al-mutakallim"], "حَرْفٌ نَاسِخٌ، وَالْيَاءُ اسْمُهُ — وَالْمَصْدَرُ مُضَافٌ إِلَيْهِ.", "«that I» — anna with my ya as its ism.", "«ben …-im» — enne ve ismi olan yâ.", segments=[seg("أَنِّ","anna","part"), seg("ي","pron-1s","pron")]),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("قُرَيْشٍ","quraysh","noun",[M, "huruf-jarr", "inna-wa-akhawatuha"], "مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ — صُرِفَ عَلَى إِرَادَةِ الْحَيِّ.", "«Quraysh» — the phrase is anna's khabar; declined as the clan.", "«Kureyş» — câr-mecrûr enne'nin haberi; kabile mânâsında munsarif.", punct=".")]})
S[-1]["badi"] = [{"kind": "takid-madh", "sub": "madh-thumma-istithna", "receipt": "bayda", "word": ix(S[-1], "بَيْدَ"), "first": [ix(S[-1], "أَفْصَحُ")], "second": [ix(S[-1], "قُرَيْشٍ")]}]

# ----------- s6 — a third kind: 7:126 (heading RESTORED; the aya as printed)
S.append({"id": "s6", "translation": {
 "en": "And of it is another kind, as in His saying, exalted is He: «And you resent us for nothing EXCEPT that we believed in the signs of our Lord when they came to us» (7:126)." + R_EN,
 "tr": "Ondan bir kısım daha vardır; Allah Teâlâ'nın şu sözü gibi: «Bize, Rabbimizin âyetleri bize geldiğinde onlara inandığımızdan BAŞKA bir şey için kızmıyorsun» (A'râf 126)." + R_TR},
 "tokens": [
  tok("وَمِنْهُ","min","part",[M, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمِنْهُ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and of it» — the fronted khabar.", "«ve ondan» — öne alınmış haber.", segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("ضَرْبٌ","darb","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a kind» — the delayed mubtada.", "«bir kısım» — sona bırakılmış mübtedâ."),
  tok("آخَرُ","akhar","noun",[M, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — a na't.", "«başka» — na't.", punct="،"),
  kaqh(M, punct=None), taala(M),
  wa_conj("وَمَا","ma-nafiya","part",[M, "anwa-ma", "istithna-mufarragh"], "مَا نَافِيَةٌ — وَالِاسْتِثْنَاءُ بَعْدَهَا مُفَرَّغٌ.", "«and not» — the negation the emptied exception hangs on.", "«ve …-miyorsun» — müferrağ istisnanın bağlandığı nefiy."),
  tok("تَنْقِمُ","naqama","verb",[M, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — نَقَمَ مِنْهُ: أَنْكَرَ عَلَيْهِ.", "«you resent» — naqama: to hold against.", "«kızıyorsun» — nekame: yadırgamak."),
  tok("مِنَّا","min","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«us».", "«bize».", segments=[seg("مِنْ","min","part"), seg("نَا","pron-1p","pron")]),
  tok("إِلَّا","illa","part",[M, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — عَلَيْهَا يَقُومُ التَّأْكِيدُ.", "«except» — the emptied exception; the confirming rides on it.", "«…-den başka» — müferrağ istisna; tekit onun üstünde."),
  an_masd(M),
  tok("آمَنَّا","amana","verb",[M, "an-masdariyya", "fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِتَنْقِمُ.", "«we believed» — its clause is the object of «you resent».", "«inandık» — cümlesi «kızıyorsun»un mef'ûlü.", segments=[seg("آمَنْ","amana","verb"), seg("نَا","pron-1p","pron")]),
  tok("بِآيَاتِ","aya","noun",[M, "huruf-jarr", "idafa-definiteness", "jam-muannath-salim"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«in the signs of».", "«âyetlerine».", segments=[seg("بِ","bi","part"), seg("آيَاتِ","aya","noun")]),
  tok("رَبِّنَا","rabb","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Lord».", "«Rabbimizin».", segments=[seg("رَبِّ","rabb","noun"), seg("نَا","pron-1p","pron")]),
  tok("لَمَّا","lamma","part",[M, "maful-fih"], "ظَرْفٌ بِمَعْنَى حِينَ، مُتَعَلِّقٌ بِآمَنَّا.", "«when».", "«-diğinde»."),
  tok("جَاءَتْنَا","jaa","verb",[M, "hollow-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَا مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they came to us».", "«bize geldiğinde».", segments=[seg("جَاءَتْ","jaa","verb"), seg("نَا","pron-1p","pron")], punct=".")]})
S[-1]["badi"] = [{"kind": "takid-madh", "sub": "nafy-illa", "receipt": "illa", "word": ix(S[-1], "إِلَّا"), "first": [ix(S[-1], "تَنْقِمُ")], "second": [ix(S[-1], "آمَنَّا")]}]

# ----------- s7 — the istidrak stands for the exception (RESTORED matn)
S.append({"id": "s7", "translation": {
 "en": "And in this chapter the ISTIDRAK is like the exception." + R_EN, "tr": "Bu bâbda İSTİDRÂK istisna gibidir." + R_TR},
 "tokens": [
  wa_conj("وَالِاسْتِدْرَاكُ","istidrak","noun",[M, "mubtada-khabar", "masdar", "form-x-verbs"], "الِاسْتِدْرَاكُ مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ اسْتَدْرَكَ: لَكِنَّ وَأَخَوَاتُهَا.", "«and the istidrak» — the mubtada; lakinna and its sisters.", "«ve istidrâk» — mübtedâ; lâkinne ve kardeşleri."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("هَذَا","hadha","pron",[M, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«this».", "«bu»."),
  tok("الْبَابِ","bab","noun",[M, "badal"], "بَدَلٌ مَجْرُورٌ.", "«chapter» — a badal.", "«bâbda» — bedel."),
  tok("كَالِاسْتِثْنَاءِ","istithna","noun",[M, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«like the exception» — the khabar.", "«istisna gibi» — haber.", segments=[seg("كَ","ka","part"), seg("الِاسْتِثْنَاءِ","istithna","noun")], punct=".")]})

# ----------- s8 — Abu l-Fadl al-Hamadhani: the full moon, but the sea, but the lion, but the downpour
S.append({"id": "s8", "translation": {
 "en": "As Abu l-Fadl al-Hamadhani says: «He is the full moon — except that he is the sea in flood, • save that he is the lion — BUT he is the downpour»." + R_EN,
 "tr": "Ebü'l-Fazl el-Hemedânî'nin dediği gibi: «O dolunaydır — ancak taşkın denizdir, • şu kadar ki arslandır — FAKAT iri damlalı yağmurdur»." + R_TR},
 "tokens": [
  kaqawl(M), *abi(M, "الْفَضْلِ", "fadl-alam", "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الْفَضْلِ: بَدِيعُ الزَّمَانِ.", "«l-Fadl» — Badiʿ al-Zaman.", "«'l-Fazl» — Bedîüzzaman.", punct=None),
  tok("الْهَمَذَانِيِّ","hamadhani","noun",[M, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — نِسْبَةٌ إِلَى هَمَذَانَ.", "«al-Hamadhani» — the nisba to Hamadhan.", "«el-Hemedânî» — Hemedan'a nisbet.", punct=":"),
  tok("هُوَ","huwa","pron",[M, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«he» — the mubtada.", "«o» — mübtedâ."),
  tok("الْبَدْرُ","badr","noun",[M, "mubtada-khabar", "tashbih"], "خَبَرٌ مَرْفُوعٌ — تَشْبِيهٌ بَلِيغٌ.", "«the full moon» — the khabar; a baligh likeness.", "«dolunay» — haber; teşbih-i belîğ."),
  tok("إِلَّا","illa","part",[M, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«ancak»."),
  tok("أَنَّهُ","anna","part",[M, "inna-wa-akhawatuha", "istithna"], "حَرْفٌ نَاسِخٌ، وَالْهَاءُ اسْمُهُ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُسْتَثْنًى مَنْصُوبٌ.", "«that he» — the clause is the excepted, mansub.", "«o …-dır» — cümlesi müstesnâ, mansûb.", segments=[seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("الْبَحْرُ","bahr","noun",[M, "inna-wa-akhawatuha", "tashbih"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«the sea» — anna's khabar.", "«deniz» — enne'nin haberi."),
  tok("زَاخِرًا","zakhir","noun",[M, "hal", "ism-fail"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلِ زَخَرَ: فَاضَ.", "«in flood» — a hal.", "«taşkın» — hâl.", punct="*"),
  tok("سِوَى","siwa","noun",[M, "istithna", "idafa-definiteness"], "مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«save» — mansub as the exception, annexed.", "«şu kadar ki» — istisna üzere mansûb, muzâf."),
  tok("أَنَّهُ","anna","part",[M, "inna-wa-akhawatuha"], "حَرْفٌ نَاسِخٌ، وَالْهَاءُ اسْمُهُ — وَالْمَصْدَرُ مُضَافٌ إِلَيْهِ.", "«that he».", "«o …-dır».", segments=[seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("الضِّرْغَامُ","dirgham","noun",[M, "inna-wa-akhawatuha", "tashbih"], "خَبَرُ أَنَّ مَرْفُوعٌ — الضِّرْغَامُ: الْأَسَدُ.", "«the lion» — dirgham: the lion.", "«arslan» — dırgâm: aslan."),
  tok("لَكِنَّهُ","lakinna","part",[M, "inna-wa-akhawatuha", "istithna"], "حَرْفُ اسْتِدْرَاكٍ نَاسِخٌ، وَالْهَاءُ اسْمُهُ — هُنَا بِمَنْزِلَةِ إِلَّا.", "«but he» — the istidrak, standing here for illa.", "«fakat o» — istidrâk; burada illâ yerinde.", segments=[seg("لَكِنَّ","lakinna","part"), seg("هُ","pron-3ms","pron")]),
  tok("الْوَبْلُ","wabl","noun",[M, "inna-wa-akhawatuha", "tashbih"], "خَبَرُ لَكِنَّ مَرْفُوعٌ — الْوَبْلُ: الْمَطَرُ الشَّدِيدُ.", "«the downpour» — lakinna's khabar.", "«iri damlalı yağmur» — lâkinne'nin haberi.", punct=".")]})
S[-1]["badi"] = [{"kind": "takid-madh", "sub": "madh-thumma-istithna", "receipt": "lakinna", "word": ix(S[-1], "لَكِنَّهُ"), "first": [ix(S[-1], "الْبَدْرُ")], "second": [ix(S[-1], "الْوَبْلُ")]}]

# ----------- s9 — the dhamm's definition: two kinds (RESTORED matn)
S.append({"id": "s9", "translation": {
 "en": "And CONFIRMING BLAME BY WHAT LOOKS LIKE PRAISE is of two kinds." + R_EN, "tr": "MEDHE BENZEYENLE ZEMMİN TEKİDİ de iki kısımdır." + R_TR},
 "tokens": [
  wa_conj("وَتَأْكِيدُ","takid","noun",[M, "mubtada-khabar", "idafa-definiteness", "masdar"], "تَأْكِيدُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ.", "«and the confirming of» — the mubtada.", "«ve tekidi» — mübtedâ."),
  tok("الذَّمِّ","dhamm","noun",[M, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«blame».", "«zemmin»."),
  tok("بِمَا","ma-mawsula","pron",[M, "huruf-jarr", "ism-mawsul"], "الْبَاءُ جَارَّةٌ، وَمَا اسْمٌ مَوْصُولٌ.", "«by what».", "«şeyle».", segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُشْبِهُ","ashbaha","verb",[M, "ism-mawsul", "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ.", "«looks like».", "«benzeyen»."),
  tok("الْمَدْحَ","madh","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«praise».", "«medhe»."),
  tok("ضَرْبَانِ","darb","noun",[M, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds» — the khabar.", "«iki kısım» — haber.", punct=".")]})

# ----------- s10 — the first kind + its example (heading RESTORED)
S.append({"id": "s10", "translation": {
 "en": "That a quality of blame be excepted from a quality of praise denied of the thing — as when you say: «So-and-so has no good in him — except that he wrongs whoever does him good»." + R_EN,
 "tr": "Şeyden nefyedilmiş bir medih sıfatından bir zem sıfatının istisna edilmesi — «Falanda hiç hayır yok — ancak kendisine iyilik edene kötülük eder» demen gibi." + R_TR},
 "tokens": [
  an_masd(M),
  tok("يُسْتَثْنَى","istathna","verb",[M, "an-masdariyya", "naib-al-fail", "form-x-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be excepted».", "«istisna edilmesi»."),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  *sifat(M, "madh", "jarr", "مَجْرُورٌ مُضَافٌ.", None),
  tok("مَنْفِيَّةٍ","manfi","noun",[M, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ.", "«denied».", "«nefyedilmiş»."),
  tok("عَنِ","an","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("الشَّيْءِ","shay","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the thing».", "«şeyden»."),
  *sifat(M, "dhamm", "raf", "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", None, punct="،"),
  kaqk(M),
  tok("فُلَانٌ","fulan","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«so-and-so» — the mubtada.", "«falan» — mübtedâ."),
  tok("لَا","la","part",[M, "la-nafiya-lil-jins"], "نَافِيَةٌ لِلْجِنْسِ.", "«no».", "«hiç … yok»."),
  tok("خَيْرَ","khayr","noun",[M, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«good» — la's ism.", "«hayır» — lâ'nın ismi."),
  tok("فِيهِ","fi","part",[M, "huruf-jarr", "la-nafiya-lil-jins"], "جَارٌّ وَمَجْرُورٌ خَبَرُ لَا، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«in him» — la's khabar; the clause the mubtada's khabar.", "«onda» — lâ'nın haberi; cümle mübtedânın haberi.", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("إِلَّا","illa","part",[M, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ — عَلَيْهَا يَقُومُ التَّأْكِيدُ.", "«except» — the adat the confirming rides on.", "«ancak» — tekidin bindiği edat."),
  tok("أَنَّهُ","anna","part",[M, "inna-wa-akhawatuha", "istithna"], "حَرْفٌ نَاسِخٌ، وَالْهَاءُ اسْمُهُ — وَالْمَصْدَرُ مُسْتَثْنًى مُنْقَطِعٌ مَنْصُوبٌ.", "«that he» — a disjoined exception, mansub.", "«o» — munkatı' müstesnâ, mansûb.", segments=[seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("يُسِيءُ","asaa","verb",[M, "inna-wa-akhawatuha", "mudari-marfu", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«he wrongs» — the clause is anna's khabar.", "«kötülük eder» — cümle enne'nin haberi."),
  tok("إِلَى","ila","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("مَنْ","man-mawsula","pron",[M, "ism-mawsul"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«whoever».", "«kimseye»."),
  tok("أَحْسَنَ","ahsana","verb",[M, "ism-mawsul", "form-iv-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«does good».", "«iyilik eden»."),
  tok("إِلَيْهِ","ila","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to him».", "«kendisine».", segments=[seg("إِلَيْ","ila","part"), seg("هِ","pron-3ms","pron")], punct=".")]})
S[-1]["badi"] = [{"kind": "takid-dhamm", "sub": "istithna-min-madh", "receipt": "illa-anna", "word": ix(S[-1], "إِلَّا"), "first": [ix(S[-1], "خَيْرَ")], "second": [ix(S[-1], "يُسِيءُ")]}]

# ----------- s11 — the second kind + its example (heading RESTORED)
S.append({"id": "s11", "translation": {
 "en": "And that a quality of blame be affirmed of a thing, then followed by an adat of exception after which comes another quality of blame — as when you say: «So-and-so is a sinner — except that he is an ignoramus»." + R_EN,
 "tr": "Ve bir şeye bir zem sıfatının ispat edilip, ardından başka bir zem sıfatının geldiği bir istisna edatıyla takip edilmesi — «Falan fâsıktır — ancak câhildir» demen gibi." + R_TR},
 "tokens": [
  wa_conj("وَأَنْ","an-masdariyya","part",[M, "atf-nasaq", "an-masdariyya"], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«and that».", "«ve …-mesi»."),
  tok("يُثْبَتَ","athbata","verb",[M, "an-masdariyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ.", "«be affirmed».", "«ispat edilmesi»."),
  tok("لِشَيْءٍ","shay","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of a thing».", "«bir şeye».", segments=[seg("لِ","li","part"), seg("شَيْءٍ","shay","noun")]),
  *sifat(M, "dhamm", "raf", "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", None),
  wa_conj("وَيُعَقَّبَ","aqqaba","verb",[M, "atf-nasaq", "naib-al-fail", "form-ii-verbs"], "يُعَقَّبَ مَعْطُوفٌ عَلَى الْمَنْصُوبِ.", "«and be followed».", "«ve takip edilmesi»."),
  tok("بِأَدَاةِ","adat","noun",[M, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«by an adat of».", "«bir edatıyla».", segments=[seg("بِ","bi","part"), seg("أَدَاةِ","adat","noun")]),
  tok("اسْتِثْنَاءٍ","istithna","noun",[M, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«exception».", "«istisna»."),
  tok("تَلِيهَا","waliya","verb",[M, "jumla-sifa", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ، وَهَا مَفْعُولٌ بِهِ — نَعْتٌ.", "«after which comes».", "«ardından gelen».", segments=[seg("تَلِي","waliya","verb"), seg("هَا","pron-3fs","pron")]),
  *sifat(M, "dhamm", "raf", "فَاعِلٌ مَرْفُوعٌ مُضَافٌ.", None),
  tok("أُخْرَى","ukhra","noun",[M, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«another».", "«başka».", punct="،"),
  kaqk(M),
  tok("فُلَانٌ","fulan","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«so-and-so».", "«falan»."),
  tok("فَاسِقٌ","fasiq","noun",[M, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ فَسَقَ.", "«a sinner» — the khabar.", "«fâsık» — haber."),
  tok("إِلَّا","illa","part",[M, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«ancak»."),
  tok("أَنَّهُ","anna","part",[M, "inna-wa-akhawatuha", "istithna"], "حَرْفٌ نَاسِخٌ، وَالْهَاءُ اسْمُهُ — وَالْمَصْدَرُ مُسْتَثْنًى.", "«that he».", "«o».", segments=[seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("جَاهِلٌ","jahil","noun",[M, "inna-wa-akhawatuha", "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«an ignoramus» — anna's khabar.", "«câhil» — enne'nin haberi.", punct=".")]})
S[-1]["badi"] = [{"kind": "takid-dhamm", "sub": "dhamm-thumma-istithna", "receipt": "illa-anna", "word": ix(S[-1], "إِلَّا"), "first": [ix(S[-1], "فَاسِقٌ")], "second": [ix(S[-1], "جَاهِلٌ")]}]

# ----------- s12 — istitba's definition (RESTORED matn)
S.append({"id": "s12", "translation": {
 "en": "Among them is ISTITBAʿ: praise for one thing in a manner that DRAWS AFTER IT praise for another." + R_EN,
 "tr": "Onlardan biri İSTİTBÂ'DIR: bir şeyle, başka bir şeyle medhi ARDINDAN GETİREN bir vecih üzere medhetmek." + R_TR},
 "tokens": [
  minha(I),
  tok("الِاسْتِتْبَاعُ","istitba","noun",[I, "mubtada-khabar", "masdar", "form-x-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ اسْتَتْبَعَ.", "«the istitbaʿ» — the delayed mubtada.", "«istitbâ'» — sona bırakılmış mübtedâ.", punct="،"),
  wahuwa(I),
  tok("الْمَدْحُ","madh","noun",[I, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ.", "«praise» — the khabar.", "«medih» — haber."),
  tok("بِشَيْءٍ","shay","noun",[I, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for a thing».", "«bir şeyle».", segments=[seg("بِ","bi","part"), seg("شَيْءٍ","shay","noun")]),
  tok("عَلَى","ala","part",[I, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  tok("وَجْهٍ","wajh","noun",[I, "huruf-jarr"], "مَجْرُورٌ.", "«a manner».", "«bir vecih»."),
  tok("يَسْتَتْبِعُ","istatbaa","verb",[I, "jumla-sifa", "mudari-marfu", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ لِوَجْهٍ.", "«that draws after it» — the clause a na't of «manner».", "«ardından getiren» — cümle «vecih»in na'tı."),
  tok("الْمَدْحَ","madh","noun",[I, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«praise».", "«medhi»."),
  tok("بِشَيْءٍ","shay","noun",[I, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for a thing».", "«bir şeyle».", segments=[seg("بِ","bi","part"), seg("شَيْءٍ","shay","noun")]),
  tok("آخَرَ","akhar","noun",[I, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ.", "«another».", "«başka».", punct=".")]})

# ----------- s13 — al-Mutanabbi: the lives you plundered
S.append({"id": "s13", "translation": {
 "en": "As Abu l-Tayyib says: «You PLUNDERED so many lives that, had you gathered them, • the world would have been congratulated that you are immortal»." + R_EN,
 "tr": "Ebü't-Tayyib'in dediği gibi: «Ömürlerden öylesini YAĞMALADIN ki, onları toplasaydın, • dünya senin ebedî olmanla tebrik edilirdi»." + R_TR},
 "tokens": [
  kaqawl(I), *abi(I, "الطَّيِّبِ", "tayyib", "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الطَّيِّبِ الْمُتَنَبِّي، فِي سَيْفِ الدَّوْلَةِ.", "«l-Tayyib» — al-Mutanabbi, to Sayf al-Dawla.", "«'t-Tayyib» — Mütenebbî, Seyfüddevle'ye."),
  tok("نَهَبْتَ","nahaba","verb",[I, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — نَهَبَ: سَلَبَ.", "«you plundered» — the ta is the doer.", "«yağmaladın» — tâ fâil."),
  tok("مِنَ","min","part",[I, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("الْأَعْمَارِ","umr","noun",[I, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ عُمْرٍ: أَعْمَارُ الْأَعْدَاءِ.", "«lives» — the enemies' lives.", "«ömürler» — düşmanların ömürleri."),
  tok("مَا","ma-mawsula","pron",[I, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that which» — the object.", "«öylesini» — mef'ûl."),
  tok("لَوْ","law","part",[I, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«had».", "«-saydı»."),
  tok("حَوَيْتَهُ","hawa-contain","verb",[I, "in-shartiyya", "naqis-verbs", "fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ صِلَةٌ.", "«you gathered them» — the shart; the clause is the sila.", "«onları toplasaydın» — şart fiili; cümle sıla.", segments=[seg("حَوَيْتَ","hawa-contain","verb"), seg("هُ","pron-3ms","pron")], punct="*"),
  tok("لَهُنِّئَتِ","hannaa","verb",[I, "in-shartiyya", "naib-al-fail", "form-ii-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَهُنِّئَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«would have been congratulated» — the lam of law's answer on a passive.", "«tebrik edilirdi» — lev'in cevap lâmı meçhul fiil üstünde.", segments=[seg("لَ","li","part"), seg("هُنِّئَتِ","hannaa","verb")]),
  tok("الدُّنْيَا","dunya","noun",[I, "naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the world» — the naib al-fail.", "«dünya» — nâib-i fâil."),
  tok("بِأَنَّكَ","anna","part",[I, "huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ، وَأَنَّ حَرْفٌ نَاسِخٌ، وَالْكَافُ اسْمُهُ.", "«that you».", "«senin».", segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part"), seg("كَ","pron-2ms","pron")]),
  tok("خَالِدُ","khalid-abiding","noun",[I, "inna-wa-akhawatuha", "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ — ضَمَّتُهُ مُطْلَقَةٌ لِلْقَافِيَةِ.", "«immortal» — anna's khabar; its damma prolonged for the rhyme.", "«ebedî» — enne'nin haberi; zammesi kafiye için uzatılmış.", punct=".")]})
S[-1]["badi"] = [{"kind": "istitba", "word": ix(S[-1], "نَهَبْتَ"), "companion": ix(S[-1], "لَهُنِّئَتِ")}]

# ----------- s14 — idmaj's definition (RESTORED matn)
S.append({"id": "s14", "translation": {
 "en": "Among them is IDMAJ: that speech brought for one meaning be made to CARRY another meaning." + R_EN,
 "tr": "Onlardan biri İDMÂCDIR: bir mânâ için getirilen söze başka bir mânânın KATILMASI." + R_TR},
 "tokens": [
  minha(I),
  tok("الْإِدْمَاجُ","idmaj","noun",[I, "mubtada-khabar", "masdar", "form-iv-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ أَدْمَجَ: أَدْخَلَ.", "«the idmaj» — the masdar of admaja: to fold in.", "«idmâc» — edmece'nin masdarı: içine sokmak.", punct="،"),
  wahuwa(I),
  an_masd(I),
  tok("يُضَمَّنَ","dammana","verb",[I, "an-masdariyya", "naib-al-fail", "form-ii-verbs", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ — يَنْصِبُ مَفْعُولَيْنِ.", "«be made to carry» — a two-object passive.", "«katılması» — iki mef'ûllü meçhul."),
  tok("كَلَامٌ","kalam","noun",[I, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«speech» — the naib al-fail.", "«söz» — nâib-i fâil."),
  tok("سِيقَ","saqa","verb",[I, "jumla-sifa", "naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ لِكَلَامٌ.", "«brought» — a hollow passive; the clause a na't of «speech».", "«getirilen» — ecvef meçhul; cümle «söz»ün na'tı."),
  tok("لِمَعْنًى","mana","noun",[I, "huruf-jarr", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«for a meaning».", "«bir mânâ için».", segments=[seg("لِ","li","part"), seg("مَعْنًى","mana","noun")]),
  tok("مَعْنًى","mana","noun",[I, "maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«a meaning» — the second object.", "«bir mânâ» — ikinci mef'ûl."),
  tok("آخَرَ","akhar","noun",[I, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَنْصُوبٌ.", "«another».", "«başka».", punct=".")]})

# ----------- s15 — al-Mutanabbi: counting the age's sins on his eyelids
S.append({"id": "s15", "translation": {
 "en": "As he says: «I turn my eyelids in it, as if • I were COUNTING with them the sins of Time»." + R_EN,
 "tr": "Onun dediği gibi: «Onda gözkapaklarımı çevirip duruyorum, sanki • onlarla zamanın günahlarını SAYIYORUM»." + R_TR},
 "tokens": [
  kaqh(I),
  tok("أُقَلِّبُ","qallaba","verb",[I, "mudari-marfu", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I turn».", "«çeviriyorum»."),
  tok("فِيهِ","fi","part",[I, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي اللَّيْلِ.", "«in it» — in the night.", "«onda» — gecede.", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("أَجْفَانِي","jafn","noun",[I, "maful-bihi", "idafa-definiteness", "jam-taksir", "ya-al-mutakallim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — جَمْعُ جَفْنٍ.", "«my eyelids» — the object; the nasb hidden before my ya.", "«gözkapaklarımı» — mef'ûl.", segments=[seg("أَجْفَانِ","jafn","noun"), seg("ي","pron-1s","pron")]),
  tok("كَأَنِّي","kaanna","part",[I, "inna-wa-akhawatuha", "ya-al-mutakallim"], "حَرْفٌ نَاسِخٌ لِلتَّشْبِيهِ، وَالْيَاءُ اسْمُهُ.", "«as if I».", "«sanki ben».", segments=[seg("كَأَنِّ","kaanna","part"), seg("ي","pron-1s","pron")], punct="*"),
  tok("أَعُدُّ","adda-count","verb",[I, "inna-wa-akhawatuha", "mudari-marfu", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ كَأَنَّ — فِيهِ الْإِدْمَاجُ: الشَّكْوَى مِنَ الدَّهْرِ فِي وَصْفِ اللَّيْلِ.", "«I count» — kaanna's khabar; here the idmaj: the complaint of Time folded into the night's description.", "«sayıyorum» — keenne'nin haberi; idmâc burada: gece tasvirine zamandan şikâyet katılmış."),
  tok("بِهَا","bi","part",[I, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«with them».", "«onlarla».", segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("عَلَى","ala","part",[I, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«against».", "«üzerine»."),
  tok("الدَّهْرِ","dahr","noun",[I, "huruf-jarr"], "مَجْرُورٌ — الدَّهْرُ: الزَّمَانُ.", "«Time».", "«zaman»."),
  tok("الذُّنُوبَا","dhanb","noun",[I, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْأَلِفُ لِلْإِطْلَاقِ — جَمْعُ ذَنْبٍ.", "«the sins» — the object; the alif prolongs the rhyme.", "«günahları» — mef'ûl; elif kafiye içindir.", punct=".")]})
S[-1]["badi"] = [{"kind": "idmaj", "word": ix(S[-1], "أَعُدُّ")}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "takid": need("takid", "تَأْكِيد", "ء ك د", "noun", "confirming, emphasis (masdar of أَكَّدَ)", "tekit, pekiştirme (أَكَّدَ'nin masdarı)", 3),
 "dhamm": need("dhamm", "ذَمّ", "ذ م م", "noun", "blame, censure (masdar of ذَمَّ)", "zem, yerme (ذَمَّ'nin masdarı)", 3),
 "darb": need("darb", "ضَرْب", "ض ر ب", "noun", "a kind, a sort", "kısım, çeşit", 3),
 "afdal": need("afdal", "أَفْضَل", "ف ض ل", "noun", "better, finer (ism tafdil)", "daha üstün, daha güzel (ism-i tafdîl)", 2),
 "istathna": need("istathna", "اسْتَثْنَى", "ث ن ي", "verb", "to except (Form X, naqis; اسْتَثْنَى يَسْتَثْنِي)", "istisna etmek (X. bâb, nâkıs; اسْتَثْنَى يَسْتَثْنِي)", 4, form="X"),
 "dukhul": need("dukhul", "دُخُول", "د خ ل", "noun", "entering (masdar of دَخَلَ)", "girme, dahil olma (دَخَلَ'nin masdarı)", 2),
 "ayb": need("ayb", "عَيْب", "ع ي ب", "noun", "a fault, a defect", "kusur, ayıp", 2),
 "fulul": need("fulul", "فُلُول", "ف ل ل", "noun", "notches in a blade (plural of فَلّ)", "kılıç gedikleri (فَلّ'in çoğulu)", 6),
 "qira": need("qira", "قِرَاع", "ق ر ع", "noun", "clashing, fighting (masdar of قَارَعَ)", "çarpışma, vuruşma (قَارَعَ'nin masdarı)", 5),
 "katiba": need("katiba", "كَتِيبَة", "ك ت ب", "noun", "a squadron, a troop (its plural كَتَائِب)", "bölük, askerî birlik (çoğulu كَتَائِب)", 5, plural="كَتَائِب"),
 "aqqaba": need("aqqaba", "عَقَّبَ", "ع ق ب", "verb", "to follow up, to make follow (Form II; عَقَّبَ يُعَقِّبُ)", "peşine getirmek, takip ettirmek (II. bâb; عَقَّبَ يُعَقِّبُ)", 4, form="II"),
 "istithna": need("istithna", "اسْتِثْنَاء", "ث ن ي", "noun", "exception (masdar of اسْتَثْنَى)", "istisna (اسْتَثْنَى'nın masdarı)", 3),
 "waliya": need("waliya", "وَلِيَ", "و ل ي", "verb", "to follow, to come next after (وَلِيَ يَلِي; mithal)", "ardından gelmek, izlemek (وَلِيَ يَلِي; misâl)", 4),
 "afsah": need("afsah", "أَفْصَح", "ف ص ح", "noun", "the most eloquent (ism tafdil of فَصِيح)", "en fasih (فَصِيح'in ism-i tafdîli)", 4),
 "arab": need("arab", "الْعَرَب", "ع ر ب", "noun", "the Arabs", "Araplar", 1),
 "bayd": need("bayd", "بَيْدَ", None, "noun", "bayda — «except that», used only before أَنَّ", "beyde — «şu kadar ki», yalnız أَنَّ önünde", 5),
 "quraysh": need("quraysh", "قُرَيْش", None, "propn", "Quraysh — the Prophet's tribe", "Kureyş — Peygamber'in kabilesi", 3),
 "naqama": need("naqama", "نَقَمَ", "ن ق م", "verb", "to resent, to hold against (نَقَمَ يَنْقِمُ)", "kızmak, yadırgamak (نَقَمَ يَنْقِمُ)", 4),
 "istidrak": need("istidrak", "اسْتِدْرَاك", "د ر ك", "noun", "istidrak — the retraction of لَكِنَّ and its sisters (masdar of اسْتَدْرَكَ)", "istidrâk — لَكِنَّ ve kardeşlerinin düzeltmesi (اسْتَدْرَكَ'nin masdarı)", 4),
 "bab": need("bab", "بَاب", "ب و ب", "noun", "a door; a chapter", "kapı; bâb, bölüm", 1),
 "fadl-alam": need("fadl-alam", "الْفَضْل", None, "propn", "al-Fadl — Abu l-Fadl, the kunya of Badiʿ al-Zaman al-Hamadhani (d. 398/1008)", "el-Fazl — Ebü'l-Fazl, Bedîüzzaman el-Hemedânî'nin künyesi (ö. 398/1008)", 6),
 "hamadhani": need("hamadhani", "الْهَمَذَانِيّ", None, "propn", "al-Hamadhani — of Hamadhan; Badiʿ al-Zaman, the author of the Maqamat", "el-Hemedânî — Hemedanlı; Makāmât müellifi Bedîüzzaman", 6),
 "zakhir": need("zakhir", "زَاخِر", "ز خ ر", "noun", "in flood, brimming (ism fa'il of زَخَرَ)", "taşkın, dolup taşan (زَخَرَ'nin ism-i fâili)", 5),
 "dirgham": need("dirgham", "ضِرْغَام", "ض ر غ م", "noun", "a lion", "arslan", 6),
 "wabl": need("wabl", "وَبْل", "و ب ل", "noun", "a heavy downpour", "iri damlalı sağanak", 5),
 "asaa": need("asaa", "أَسَاءَ", "س و ء", "verb", "to do ill, to wrong (Form IV, hollow; أَسَاءَ يُسِيءُ)", "kötülük etmek (IV. bâb, ecvef; أَسَاءَ يُسِيءُ)", 3, form="IV"),
 "fasiq": need("fasiq", "فَاسِق", "ف س ق", "noun", "a sinner, one who transgresses (ism fa'il of فَسَقَ)", "fâsık, günahkâr (فَسَقَ'nin ism-i fâili)", 3),
 "istitba": need("istitba", "اسْتِتْبَاع", "ت ب ع", "noun", "istitbaʿ — a praise drawing another after it (masdar of اسْتَتْبَعَ)", "istitbâ' — ardından başka medih getiren medih (اسْتَتْبَعَ'nin masdarı)", 5),
 "istatbaa": need("istatbaa", "اسْتَتْبَعَ", "ت ب ع", "verb", "to draw after, to entail (Form X; اسْتَتْبَعَ يَسْتَتْبِعُ)", "ardından getirmek, gerektirmek (X. bâb; اسْتَتْبَعَ يَسْتَتْبِعُ)", 5, form="X"),
 "nahaba": need("nahaba", "نَهَبَ", "ن ه ب", "verb", "to plunder (نَهَبَ يَنْهَبُ)", "yağmalamak (نَهَبَ يَنْهَبُ)", 4),
 "umr": need("umr", "عُمْر", "ع م ر", "noun", "a life, a lifetime (its plural أَعْمَار)", "ömür (çoğulu أَعْمَار)", 2, plural="أَعْمَار"),
 "hannaa": need("hannaa", "هَنَّأَ", "ه ن ء", "verb", "to congratulate (Form II; هَنَّأَ يُهَنِّئُ)", "tebrik etmek (II. bâb; هَنَّأَ يُهَنِّئُ)", 4, form="II"),
 "idmaj": need("idmaj", "إِدْمَاج", "د م ج", "noun", "idmaj — folding a second meaning into speech (masdar of أَدْمَجَ)", "idmâc — söze ikinci mânâ katma (أَدْمَجَ'nin masdarı)", 5),
 "dammana": need("dammana", "ضَمَّنَ", "ض م ن", "verb", "to make carry, to include (Form II; ضَمَّنَ يُضَمِّنُ)", "içermesini sağlamak, katmak (II. bâb; ضَمَّنَ يُضَمِّنُ)", 4, form="II"),
 "kalam": need("kalam", "كَلَام", "ك ل م", "noun", "speech", "söz, kelâm", 1),
 "saqa": need("saqa", "سَاقَ", "س و ق", "verb", "to drive, to bring forward (سَاقَ يَسُوقُ; hollow)", "sürmek, getirmek (سَاقَ يَسُوقُ; ecvef)", 3),
 "qallaba": need("qallaba", "قَلَّبَ", "ق ل ب", "verb", "to turn over and over (Form II; قَلَّبَ يُقَلِّبُ)", "evirip çevirmek (II. bâb; قَلَّبَ يُقَلِّبُ)", 3, form="II"),
 "dahr": need("dahr", "دَهْر", "د ه ر", "noun", "time, the age, fate", "dehr, zaman, felek", 3),
}
for k in ("qawl", "min", "huwa", "an-masdariyya", "fi", "li", "bi", "ka", "wa", "fa", "an", "pron-3fs", "pron-3ms", "pron-3mp", "pron-3fp", "pron-1s", "pron-1p", "pron-2ms", "pron-3d",
          "madh", "ma-mawsula", "ma-nafiya", "ashbaha", "sifa", "manfi", "shay", "taqdir", "nabigha", "la", "ghayr", "anna", "sayf", "thani", "athbata", "adat", "ukhra", "lahu",
          "salla-allahu", "ana", "illa", "amana", "aya", "rabb", "lamma", "jaa", "taala", "akhar", "hadha", "ab", "tayyib", "badr", "bahr", "siwa", "lakinna", "fulan", "khayr",
          "ila", "man-mawsula", "ahsana", "jahil", "wajh", "ala", "law", "hawa-contain", "dunya", "khalid-abiding", "mana", "jafn", "kaanna", "adda-count", "dhanb", "mutanabbi"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "istathna", _sg.derived_naqis(_sg.B10, _sg.W10, "َ", "اِسْتَثْنَ", "سْتَثْن", "i", "اِسْتَثْن", "اِسْتِثْنَاء", "مُسْتَثْنٍ (الْمُسْتَثْنِي)", "مُسْتَثْنًى", "اُسْتُثْنِيَ", "يُسْتَثْنَى"))
put_morph(mo, "aqqaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "عَقَّب", "عَقِّب", "عَقِّب", "تَعْقِيب", "مُعَقِّب", "مُعَقَّب", "عُقِّبَ", "يُعَقَّبُ"))
put_morph(mo, "naqama", _sg.sound1("daraba", "نَقَم", "نْقِم", "اِنْقِم", "نَقْم", "نَاقِم", maful="مَنْقُوم", pmz="نُقِمَ", pmd="يُنْقَمُ"))
put_morph(mo, "asaa", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَسَاء", "أَسَأ", "سِيء", "سِئ", "أَسِئ", "أَسِئ", "إِسَاءَة", "مُسِيء", "مُسَاء", "أُسِيءَ", "يُسَاءُ"))
put_morph(mo, "istatbaa", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَتْبَع", "سْتَتْبِع", "اِسْتَتْبِع", "اِسْتِتْبَاع", "مُسْتَتْبِع", "مُسْتَتْبَع", "اُسْتُتْبِعَ", "يُسْتَتْبَعُ"))
put_morph(mo, "nahaba", _sg.sound1("fataha", "نَهَب", "نْهَب", "اِنْهَب", "نَهْب", "نَاهِب", maful="مَنْهُوب", pmz="نُهِبَ", pmd="يُنْهَبُ"))
put_morph(mo, "hannaa", _sg.derived(_sg.B2, _sg.W2, "ُ", "هَنَّأ", "هَنِّئ", "هَنِّئ", "تَهْنِئَة", "مُهَنِّئ", "مُهَنَّأ", "هُنِّئَ", "يُهَنَّأُ"))
put_morph(mo, "dammana", _sg.idgham(_sg.derived(_sg.B2, _sg.W2, "ُ", "ضَمَّن", "ضَمِّن", "ضَمِّن", "تَضْمِين", "مُضَمِّن", "مُضَمَّن", "ضُمِّنَ", "يُضَمَّنُ")))
put_morph(mo, "saqa", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "سَاق", "سُق", "سُوق", "سُق", "سُوق", "سُق", "سَوْق", "سَائِق", maful="مَسُوق", pmz="سِيقَ", pmd="يُسَاقُ"))
put_morph(mo, "qallaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَلَّب", "قَلِّب", "قَلِّب", "تَقْلِيب", "مُقَلِّب", "مُقَلَّب", "قُلِّبَ", "يُقَلَّبُ"))
put_morph(mo, "waliya", _sg.entry("بَابُ حَسِبَ يَحْسِبُ — مِثَالٌ وَاوِيٌّ (لَفِيفٌ مَفْرُوقٌ)", "فَعِلَ يَفْعِلُ", "وِلَايَة", "وَالٍ (الْوَالِي)", _sg.mazi_naqis("وَلِ", "y"), _sg.mudari_naqis("َ", "ل", "i"), _sg.amr_naqis("ل", "i"), "يَلِيَ", "يَلِ", "تَلِ", "مَوْلِيّ", "وُلِيَ", "يُولَى", "وَلِيَ يَلِي: تَلِيهَا — يَتْلُوهَا."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_M = {
 "id": "takid-al-madh-wal-dhamm",
 "title": {"ar": "تَأْكِيدُ الْمَدْحِ بِمَا يُشْبِهُ الذَّمَّ، وَتَأْكِيدُ الذَّمِّ بِمَا يُشْبِهُ الْمَدْحَ", "en": "Praise confirmed by what looks like blame — and blame by what looks like praise", "tr": "Zemme benzeyenle medhin, medhe benzeyenle zemmin tekidi"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — تأكيد المدح بما يشبه الذم ضربان: أفضلهما أن يستثنى من صفة ذم منفية عن الشيء صفة مدح بتقدير دخولها فيها؛ والثاني أن يثبت لشيء صفة مدح ويعقب بأداة استثناء تليها صفة مدح أخرى له؛ ومنه ضرب آخر؛ والاستدراك في هذا الباب كالاستثناء. وتأكيد الذم بما يشبه المدح ضربان."],
 "question": {
  "en": ["Does an ADAT OF EXCEPTION (إِلَّا، غَيْرَ، بَيْدَ، سِوَى) — or the لَكِنَّ that stands in for it — follow a praise, and what comes after it is ANOTHER praise? Then the blame it seemed to open never comes: the praise is CONFIRMED.",
         "The finer kind: a blame is DENIED of the thing and a praise is EXCEPTED from it as though it were a blame — لَا عَيْبَ فِيهِمْ غَيْرَ أَنَّ سُيُوفَهُمْ بِهِنَّ فُلُولٌ. The second: a praise is affirmed, then the adat brings a second praise — أَنَا أَفْصَحُ الْعَرَبِ بَيْدَ أَنِّي مِنْ قُرَيْشٍ. A third: nothing to resent but faith — وَمَا تَنْقِمُ مِنَّا إِلَّا أَنْ آمَنَّا.",
         "Turn the polarity and it is BLAME confirmed by what looks like praise: لَا خَيْرَ فِيهِ إِلَّا أَنَّهُ يُسِيءُ; فَاسِقٌ إِلَّا أَنَّهُ جَاهِلٌ.",
         "What does the engine read? The adat's seat (إِلَّا, غَيْرَ, بَيْدَ, سِوَى, لَكِنَّ), the negation before it when the first kind is meant (لَا … / مَا …), and the clause on each side; the polarity — praise or blame — is the author's judgement."],
  "tr": ["Bir medihten sonra bir İSTİSNA EDATI (إِلَّا، غَيْرَ، بَيْدَ، سِوَى) — yahut onun yerine geçen لَكِنَّ — geliyor ve ardından BAŞKA bir medih mi var? O hâlde açar göründüğü zem hiç gelmez: medih TEKİT edilmiştir.",
         "Daha güzeli: şeyden bir zem NEFYEDİLİR ve bir medih, zemmiş gibi ondan İSTİSNA edilir — لَا عَيْبَ فِيهِمْ غَيْرَ أَنَّ سُيُوفَهُمْ بِهِنَّ فُلُولٌ. İkincisi: medih ispat edilir, sonra edat ikinci bir medih getirir — أَنَا أَفْصَحُ الْعَرَبِ بَيْدَ أَنِّي مِنْ قُرَيْشٍ. Üçüncüsü: imandan başka kızılacak şey yok — وَمَا تَنْقِمُ مِنَّا إِلَّا أَنْ آمَنَّا.",
         "Kutbu çevir: medhe benzeyenle ZEMMİN tekidi olur: لَا خَيْرَ فِيهِ إِلَّا أَنَّهُ يُسِيءُ; فَاسِقٌ إِلَّا أَنَّهُ جَاهِلٌ.",
         "Motor neyi okur? Edatın yerini (إِلَّا, غَيْرَ, بَيْدَ, سِوَى, لَكِنَّ), birinci kısımda ondan önceki nefyi (لَا … / مَا …) ve iki yandaki cümleleri; kutup — medih mi zem mi — müellifin hükmüdür."]},
 "plain": {
  "en": "An adat of exception after a praise, followed by another praise, confirms the praise: the blame it seemed to open never comes. Two kinds: a praise excepted from a denied blame (the finer), or a praise, the adat and a second praise; a third with مَا … إِلَّا أَنْ. Reversed, it confirms blame.",
  "tr": "Medihten sonra bir istisna edatı ve ardından başka bir medih, medhi tekit eder (açar göründüğü zem gelmez). İki kısım: nefyedilmiş zemden istisna edilen medih (daha güzeli) yahut medih, edat ve ikinci medih; مَا … إِلَّا أَنْ ile bir üçüncüsü. Zem için kutbu çevir. Motor edatı ve cümleleri okur."},
 "explanation": {
  "en": "TAʾKID AL-MADH BIMA YUSHBIHU AL-DHAMM has two kinds. The FINER: أَنْ يُسْتَثْنَى مِنْ صِفَةِ ذَمٍّ مَنْفِيَّةٍ عَنِ الشَّيْءِ صِفَةُ مَدْحٍ بِتَقْدِيرِ دُخُولِهَا فِيهَا — al-Nabigha: وَلَا عَيْبَ فِيهِمْ غَيْرَ أَنَّ سُيُوفَهُمْ بِهِنَّ فُلُولٌ مِنْ قِرَاعِ الْكَتَائِبِ; the notched swords are excepted from «no fault» as if a notch were a fault — and it is the mark of battle. This kind confirms from two sides: the claim comes with its own proof, and the adat, being in origin a joined exception, makes the mind expect a fault and hands it a praise. The SECOND: a praise is affirmed and an adat of exception follows it with another praise — the hadith أَنَا أَفْصَحُ الْعَرَبِ بَيْدَ أَنِّي مِنْ قُرَيْشٍ; here the exception is in origin disjoined, so it confirms from the second side only, which is why the first kind is finer. A THIRD kind: وَمَا تَنْقِمُ مِنَّا إِلَّا أَنْ آمَنَّا بِآيَاتِ رَبِّنَا — you find nothing in us to resent but our faith. The ISTIDRAK stands in for the exception: هُوَ الْبَدْرُ إِلَّا أَنَّهُ الْبَحْرُ زَاخِرًا سِوَى أَنَّهُ الضِّرْغَامُ لَكِنَّهُ الْوَبْلُ — al-Hamadhani's لَكِنَّهُ works as إِلَّا. TAʾKID AL-DHAMM is the mirror: لَا خَيْرَ فِيهِ إِلَّا أَنَّهُ يُسِيءُ إِلَى مَنْ أَحْسَنَ إِلَيْهِ (a blame excepted from a denied praise) and فُلَانٌ فَاسِقٌ إِلَّا أَنَّهُ جَاهِلٌ (a blame, then the adat and another blame). The card draws the two clauses as a HINGE on the adat.",
  "tr": "TE'KÎDÜ'L-MEDH BİMÂ YÜŞBİHÜ'Z-ZEM iki kısımdır. DAHA GÜZELİ: أَنْ يُسْتَثْنَى مِنْ صِفَةِ ذَمٍّ مَنْفِيَّةٍ عَنِ الشَّيْءِ صِفَةُ مَدْحٍ بِتَقْدِيرِ دُخُولِهَا فِيهَا — Nâbiga: وَلَا عَيْبَ فِيهِمْ غَيْرَ أَنَّ سُيُوفَهُمْ بِهِنَّ فُلُولٌ مِنْ قِرَاعِ الْكَتَائِبِ; gedik kılıçlar, gedik bir kusurmuş gibi «kusur yok»tan istisna edilir — oysa savaşın nişanıdır. Bu kısım iki cihetten tekit eder: dava deliliyle gelir, ve edat aslen muttasıl istisna olduğundan zihne bir kusur bekletip eline medih verir. İKİNCİSİ: medih ispat edilir, istisna edatı ardından başka bir medih getirir — hadis أَنَا أَفْصَحُ الْعَرَبِ بَيْدَ أَنِّي مِنْ قُرَيْشٍ; burada istisna aslen munkatı'dır, yalnız ikinci cihetten tekit eder; bu yüzden birinci kısım daha üstündür. ÜÇÜNCÜ bir kısım: وَمَا تَنْقِمُ مِنَّا إِلَّا أَنْ آمَنَّا بِآيَاتِ رَبِّنَا — bizde imanımızdan başka kızacak şey bulamazsın. İSTİDRÂK istisna yerine geçer: هُوَ الْبَدْرُ إِلَّا أَنَّهُ الْبَحْرُ زَاخِرًا سِوَى أَنَّهُ الضِّرْغَامُ لَكِنَّهُ الْوَبْلُ — Hemedânî'nin لَكِنَّهُ'su إِلَّا işini görür. TE'KÎDÜ'Z-ZEM aynadır: لَا خَيْرَ فِيهِ إِلَّا أَنَّهُ يُسِيءُ إِلَى مَنْ أَحْسَنَ إِلَيْهِ (nefyedilmiş medihten zem istisnası) ve فُلَانٌ فَاسِقٌ إِلَّا أَنَّهُ جَاهِلٌ (zem, sonra edat ve başka zem). Kart iki cümleyi edat üstünde bir MENTEŞE olarak çizer."},
 "examples": [
  {"ar": "وَلَا عَيْبَ فِيهِمْ غَيْرَ أَنَّ سُيُوفَهُمْ * بِهِنَّ فُلُولٌ مِنْ قِرَاعِ الْكَتَائِبِ", "en": "al-Nabigha — a praise excepted from a denied blame.", "tr": "Nâbiga — nefyedilmiş zemden medih istisnası.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "أَنَا أَفْصَحُ الْعَرَبِ بَيْدَ أَنِّي مِنْ قُرَيْشٍ", "en": "the hadith — a praise, then bayda and another.", "tr": "hadis — medih, sonra beyde ve başkası.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "وَمَا تَنْقِمُ مِنَّا إِلَّا أَنْ آمَنَّا بِآيَاتِ رَبِّنَا لَمَّا جَاءَتْنَا", "en": "7:126 — the third kind.", "tr": "A'râf 126 — üçüncü kısım.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "هُوَ الْبَدْرُ إِلَّا أَنَّهُ الْبَحْرُ زَاخِرًا * سِوَى أَنَّهُ الضِّرْغَامُ لَكِنَّهُ الْوَبْلُ", "en": "al-Hamadhani — the istidrak as the adat.", "tr": "Hemedânî — edat yerine istidrâk.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "فُلَانٌ لَا خَيْرَ فِيهِ إِلَّا أَنَّهُ يُسِيءُ إِلَى مَنْ أَحْسَنَ إِلَيْهِ", "en": "blame confirmed — the first kind.", "tr": "zemmin tekidi — birinci kısım.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "فُلَانٌ فَاسِقٌ إِلَّا أَنَّهُ جَاهِلٌ", "en": "blame confirmed — the second kind.", "tr": "zemmin tekidi — ikinci kısım.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"}],
 "commonMistakes": [
  {"wrong": "«غَيْرَ أَنَّ سُيُوفَهُمْ بِهِنَّ فُلُولٌ bir kusur sayar: kılıçlar gedilmiştir»",
   "right": "«Kusurdan istisna edilen şey bir medihtir: gedikler çok savaşmanın nişanıdır — istisna zemmi açar görünüp medhi pekiştirir»",
   "why": {"en": "The figure lives in the reader's expectation: the adat promises a fault and delivers a praise.", "tr": "Sanat okuyucunun beklentisinde yaşar: edat kusur vaat eder, medih verir."}}],
 "relatedNotes": ["istithna", "istithna-mufarragh", "la-nafiya-lil-jins", "inna-wa-akhawatuha", "husn-al-talil", "ilm-al-badi"]}

NOTE_I = {
 "id": "istitba-wa-idmaj",
 "title": {"ar": "الِاسْتِتْبَاعُ وَالْإِدْمَاجُ — مَدْحٌ يَسْتَتْبِعُ مَدْحًا، وَمَعْنًى يُضَمَّنُ مَعْنًى", "en": "Istitbaʿ and idmaj — a praise that draws a second praise, a speech that carries a second meaning", "tr": "İstitbâ' ve idmâc — ikinci medhi getiren medih, ikinci mânâ taşıyan söz"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الاستتباع: المدح بشيء على وجه يستتبع المدح بشيء آخر. الإدماج: أن يضمن كلام سيق لمعنى معنى آخر؛ وهو أعم من الاستتباع، لأنه يكون في المدح وفي غيره."],
 "question": {
  "en": ["Is a man praised for ONE thing in a way that DRAWS a second praise after it? ISTITBAʿ — al-Mutanabbi praises Sayf al-Dawla's courage: نَهَبْتَ مِنَ الْأَعْمَارِ مَا لَوْ حَوَيْتَهُ لَهُنِّئَتِ الدُّنْيَا بِأَنَّكَ خَالِدُ — and the praise of courage carries with it that the world is set right by him, that he plundered lives and not wealth, and was no tyrant in it.",
         "Is speech brought for ONE meaning made to CARRY another — in praise or elsewhere? IDMAJ — أُقَلِّبُ فِيهِ أَجْفَانِي كَأَنِّي أَعُدُّ بِهَا عَلَى الدَّهْرِ الذُّنُوبَا: the night is described as long, and a complaint against Time is folded into the description. Idmaj is the wider: istitbaʿ lives in praise only.",
         "What does the engine read? The two are matters of meaning; the frames are the author's, and the card shows the spoken praise with the entailed one behind it, or the folded meaning lit on its word."],
  "tr": ["Biri BİR şeyle, ardından ikinci bir medhi GETİREN bir vecih üzere mi medhediliyor? İSTİTBÂ' — Mütenebbî Seyfüddevle'nin şecaatini över: نَهَبْتَ مِنَ الْأَعْمَارِ مَا لَوْ حَوَيْتَهُ لَهُنِّئَتِ الدُّنْيَا بِأَنَّكَ خَالِدُ — ve şecaat medhi beraberinde dünyanın onunla düzeldiğini, malları değil ömürleri yağmaladığını ve bunda zalim olmadığını taşır.",
         "BİR mânâ için getirilen söze başka bir mânâ mı KATILIYOR — medihte yahut başka yerde? İDMÂC — أُقَلِّبُ فِيهِ أَجْفَانِي كَأَنِّي أَعُدُّ بِهَا عَلَى الدَّهْرِ الذُّنُوبَا: gece uzun diye tasvir edilir, tasvire zamandan şikâyet katılır. İdmâc daha geniştir: istitbâ' yalnız medihte yaşar.",
         "Motor neyi okur? İkisi de mânâ işidir; çerçeveler müellifindir; kart söylenen medhi arkasındaki gerektirilen medihle, yahut katılan mânâyı kelimesi üstünde yanmış gösterir."]},
 "plain": {
  "en": "Istitbaʿ praises one thing so that a second praise follows (al-Mutanabbi's plundered lives). Idmaj folds a second meaning into speech brought for one (counting Time's sins on the eyelids); it is wider than istitbaʿ, which lives in praise only. Both are matters of meaning: the frames are the author's.",
  "tr": "İstitbâ', ikinci bir medih ardından gelecek şekilde bir şeyi över (Mütenebbî'nin yağmalanan ömürleri). İdmâc, bir mânâ için getirilen söze ikincisini katar (gözkapaklarıyla zamanın günahlarını saymak); yalnız medihte yaşayan istitbâ'dan geniştir. İkisi de mânâ işidir: çerçeveler müellifindir."},
 "explanation": {
  "en": "ISTITBAʿ is الْمَدْحُ بِشَيْءٍ عَلَى وَجْهٍ يَسْتَتْبِعُ الْمَدْحَ بِشَيْءٍ آخَرَ. Al-Mutanabbi: نَهَبْتَ مِنَ الْأَعْمَارِ مَا لَوْ حَوَيْتَهُ لَهُنِّئَتِ الدُّنْيَا بِأَنَّكَ خَالِدُ — he praises him for reaching the summit of courage, in a manner that draws after it the praise that he is the cause of the world's welfare and order, that what he plundered was lives, not wealth, and that in taking them he was no wrongdoer. IDMAJ is أَنْ يُضَمَّنَ كَلَامٌ سِيقَ لِمَعْنًى مَعْنًى آخَرَ, and it is wider than istitbaʿ because it may be in praise or in blame: أُقَلِّبُ فِيهِ أَجْفَانِي كَأَنِّي أَعُدُّ بِهَا عَلَى الدَّهْرِ الذُّنُوبَا — the bayt describes the night as long and folds into it a complaint against Time.",
  "tr": "İSTİTBÂ' الْمَدْحُ بِشَيْءٍ عَلَى وَجْهٍ يَسْتَتْبِعُ الْمَدْحَ بِشَيْءٍ آخَرَ'dir. Mütenebbî: نَهَبْتَ مِنَ الْأَعْمَارِ مَا لَوْ حَوَيْتَهُ لَهُنِّئَتِ الدُّنْيَا بِأَنَّكَ خَالِدُ — onu şecaatin zirvesine ulaşmakla, ardından dünyanın salâh ve nizamına sebep olduğu, yağmaladığının mallar değil ömürler olduğu ve onları almakla zalim olmadığı medhini getiren bir vecih üzere över. İDMÂC أَنْ يُضَمَّنَ كَلَامٌ سِيقَ لِمَعْنًى مَعْنًى آخَرَ'dir ve istitbâ'dan geniştir; çünkü medihte de zemde de olur: أُقَلِّبُ فِيهِ أَجْفَانِي كَأَنِّي أَعُدُّ بِهَا عَلَى الدَّهْرِ الذُّنُوبَا — beyit geceyi uzun diye tasvir eder ve tasvire zamandan şikâyeti katar."},
 "examples": [
  {"ar": "نَهَبْتَ مِنَ الْأَعْمَارِ مَا لَوْ حَوَيْتَهُ * لَهُنِّئَتِ الدُّنْيَا بِأَنَّكَ خَالِدُ", "en": "al-Mutanabbi — istitbaʿ.", "tr": "Mütenebbî — istitbâ'.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "أُقَلِّبُ فِيهِ أَجْفَانِي كَأَنِّي * أَعُدُّ بِهَا عَلَى الدَّهْرِ الذُّنُوبَا", "en": "al-Mutanabbi — idmaj.", "tr": "Mütenebbî — idmâc.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"}],
 "commonMistakes": [
  {"wrong": "«نَهَبْتَ مِنَ الْأَعْمَارِ bir mübalağadır, çünkü ömürler toplanamaz»",
   "right": "«Mübalağa da var; fakat adlandırılan sanat istitbâ'dır: şecaat medhi, dünyanın onunla düzeldiği medhini ardından getirir»",
   "why": {"en": "Istitbaʿ is named for the SECOND praise the first drags in, not for the size of the first.", "tr": "İstitbâ' adını birincinin büyüklüğünden değil, sürüklediği İKİNCİ medihten alır."}}],
 "relatedNotes": ["takid-al-madh-wal-dhamm", "mubalagha-maqbula", "in-shartiyya", "ilm-al-badi"]}

ADD_EN = (" Chapter 66 (lines ~4300-4345, sahifa 148-150) carries praise confirmed by what looks like blame (al-Nabigha s3, the hadith بَيْدَ أَنِّي s5, "
          "7:126 s6, al-Hamadhani's istidrak s8), blame confirmed by what looks like praise (s10, s11), istitbaʿ (al-Mutanabbi s13) and idmaj (al-Mutanabbi s15). "
          "The definitions and headings (s1, s2, s4, s7, s9, s12, s14; the headings of s6, s10, s11) are RESTORED: the source carries them only in Turkish, and the "
          "Arabic is the received matn of the Talkhis; every restored sentence is marked «Restored» in its translation. The Hamadhani's nisba is written "
          "الْهَمَذَانِيِّ as the received text has it (the print: الهمدانى); the idmaj bayt the print attributes to «al-Munbati» is al-Mutanabbi's, as the Talkhis "
          "cites it (كقوله). The examples carry `badi` frames (takid-madh / takid-dhamm with the adat as `word`, its kind as `sub`, its `receipt`, and the two "
          "clauses as `first`/`second`; istitba with the spoken praise as `word` and the entailed one as `companion`; idmaj with the folded meaning's `word`).")
ADD_TR = (" Altmış altıncı bâb (satır ~4300-4345, sahife 148-150) zemme benzeyenle medhin tekidini (Nâbiga s3, بَيْدَ أَنِّي hadisi s5, A'râf 126 s6, "
          "Hemedânî'nin istidrâkı s8), medhe benzeyenle zemmin tekidini (s10, s11), istitbâ'ı (Mütenebbî s13) ve idmâcı (Mütenebbî s15) taşır. Tarifler ve "
          "başlıklar (s1, s2, s4, s7, s9, s12, s14; s6, s10, s11'in başlıkları) GERİ YAZILMIŞTIR: kaynak bunları yalnız Türkçe taşır; Arapça, Telhîs'in alınan "
          "metnidir. Her geri yazılmış cümle tercümesinde «geri yazılmıştır» diye işaretlidir. Hemedânî'nin nisbesi alınan metindeki gibi الْهَمَذَانِيِّ yazılmıştır "
          "(baskıda الهمدانى); baskının «el-Münbetî»ye nispet ettiği idmâc beyti, Telhîs'in iktibas ettiği gibi (كقوله) Mütenebbî'nindir. Örnekler `badi` "
          "çerçeveleri taşır (medih/zem tekidi: edat `word`, kısmı `sub`, alındısı `receipt`, iki cümle `first`/`second`; istitbâ': söylenen medih `word`, "
          "gerektirilen `companion`; idmâc: katılan mânânın `word`ü).")
write_out(66, S, TITLE, ADD_EN, ADD_TR, "4300-4345", GLOSS_ADD, notes=(NOTE_M, NOTE_I),
          related=(("istithna", ["takid-al-madh-wal-dhamm"]), ("istithna-mufarragh", ["takid-al-madh-wal-dhamm"]), ("ilm-al-badi", ["takid-al-madh-wal-dhamm", "istitba-wa-idmaj"]), ("husn-al-talil", ["takid-al-madh-wal-dhamm", "istitba-wa-idmaj"])))
report(66, S, GLOSS_ADD, (NOTE_M, NOTE_I))
