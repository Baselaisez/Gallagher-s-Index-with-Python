# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 63: the TAJRID — one thing of a quality, and out of it another like it, for the sake of
hyperbole: by مِنْ, by بِ, by the بِ of accompaniment, by فِي, with no letter, by way of kinaya, and by a man addressing
himself. Source lines ~4170-4200 (sahifa 144-145).

  RESTORED (the source carries the step only in Turkish): s1 (the definition), s2, s4, s6, s8, s10, s12, s14 (the seven
  kinds' headings). The examples (s3, s5, s7, s9, s11, s13, s15) are the source's printed Arabic.

  python3 tools/authoring/author_talkhis_ch63.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

D = "tajrid"
TITLE = {"ar": "التَّجْرِيدُ وَأَقْسَامُهُ", "en": "The Tajrid and its kinds", "tr": "Tecrîd ve kısımları"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them is» — the fronted khabar.", "«ve onlardan biri» — öne alınmış haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def minhu(tag):
    return tok("وَمِنْهُ","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — أَيْ مِنَ التَّجْرِيدِ.", "«and of it is» — the fronted khabar: of the tajrid.", "«ve ondan biri» — öne alınmış haber: tecrîdden.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")])
def wahuwa(tag, full="وَهُوَ"):
    lex = "hiya" if full.endswith("هِيَ") else "huwa"
    return tok(full, lex, "pron", [tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالضَّمِيرُ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
               segments=[seg("وَ","wa","conj"), seg(full[1:], lex, "pron")])
def an_masd(tag):
    return tok("أَنْ","an-masdariyya","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the clause is the khabar.", "«-mak» — masdar yapan en; cümle haberdir.")
def ma_yakun(tag):
    return [tok("مَا","ma-mawsula","pron",[tag, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what» — the delayed mubtada.", "«…-anı» — sona bırakılmış mübtedâ."),
            tok("يَكُونُ","kana","verb",[tag, "ism-mawsul", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — صِلَةٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«is» — the sila; kana's ism concealed.", "«olur» — sıla; kâne'nin ismi gizli.")]
def kaqawl(tag, punct=None):
    return tok("كَقَوْلِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")], punct=punct)
def kaqh(tag, who="pron-3ms"):
    pr = {"pron-3ms": "هِ", "pron-3mp": "هِمْ"}[who]
    return tok("كَقَوْلِ" + pr, "qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«as in the saying».", "«sözü gibi».",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg(pr, who, "pron")], punct=":")
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)

# ----------- s1 — the definition (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the TAJRID: out of a thing that has a quality, ANOTHER thing like it in that quality is drawn — for hyperbole, because the quality is complete in it." + R_EN,
 "tr": "Onlardan biri TECRÎDDİR: bir sıfatı olan şeyden, o sıfatta onun gibi BAŞKA bir şey çıkarılır — mübalağa için, sıfat onda kemâle erdiğinden." + R_TR},
 "tokens": [
  minha(D),
  tok("التَّجْرِيدُ","tajrid","noun",[D, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ جَرَّدَ.", "«the tajrid» — the delayed mubtada; the masdar of jarrada.", "«tecrîd» — sona bırakılmış mübtedâ; cerrede'nin masdarı.", punct="،"),
  wahuwa(D),
  an_masd(D),
  tok("يُنْتَزَعَ","intazaa","verb",[D, "an-masdariyya", "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«is drawn out» — a passive, mansub by an.", "«çıkarılır» — meçhul, en ile mansûb."),
  tok("مِنْ","min","part",[D, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«out of».", "«-den»."),
  tok("أَمْرٍ","amr","noun",[D, "huruf-jarr"], "مَجْرُورٌ — الْأَمْرُ الْأَوَّلُ: صَاحِبُ الصِّفَةِ.", "«a thing» — the first thing, the owner of the quality.", "«bir şey» — ilk şey, sıfatın sahibi."),
  tok("ذِي","dhu","noun",[D, "naat-sifa", "five-nouns", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«having» — a na't; one of the five nouns, its jarr the ya.", "«sahibi» — na't; esmâ-i hamseden, cerri yâ ile."),
  tok("صِفَةٍ","sifa","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a quality».", "«bir sıfat»."),
  tok("أَمْرٌ","amr","noun",[D, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الْأَمْرُ الثَّانِي: الْمُنْتَزَعُ.", "«another thing» — the naib al-fail; the second thing, the one drawn out.", "«bir şey» — nâib-i fâil; ikinci şey, çıkarılan."),
  tok("آخَرُ","akhar","noun",[D, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — a na't; a diptote.", "«başka» — na't; gayr-i munsarif."),
  tok("مِثْلُهُ","mithl","noun",[D, "naat-sifa", "idafa-definiteness"], "نَعْتٌ ثَانٍ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«like it» — a second na't, annexed.", "«onun gibi» — ikinci na't, muzâf.",
      segments=[seg("مِثْلُ","mithl","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فِيهَا","fi","part",[D, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمِثْلِ — أَيْ فِي تِلْكَ الصِّفَةِ.", "«in it» — in that quality.", "«onda» — o sıfatta.", segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("مُبَالَغَةً","mubalagha","noun",[D, "maful-lah", "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ — الْغَرَضُ.", "«for hyperbole» — the maf'ul lahu: the aim.", "«mübalağa için» — mef'ûlün leh: gaye."),
  tok("لِكَمَالِهَا","kamal","noun",[D, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عِلَّةُ الْمُبَالَغَةِ.", "«because of its completeness» — the ground of the hyperbole.", "«kemâlinden dolayı» — mübalağanın illeti.",
      segments=[seg("لِ","li","part"), seg("كَمَالِ","kamal","noun"), seg("هَا","pron-3fs","pron")]),
  tok("فِيهِ","fi","part",[D, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي الْأَمْرِ الْأَوَّلِ.", "«in it» — in the first thing.", "«onda» — ilk şeyde.", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s2 — by مِنْ (RESTORED heading)
S.append({"id": "s2", "translation": {
 "en": "It has kinds. Of it is what comes by MIN." + R_EN, "tr": "Kısımları vardır. Ondan biri MİN ile olandır." + R_TR},
 "tokens": [
  wahuwa(D),
  tok("أَقْسَامٌ","aqsam","noun",[D, "mubtada-khabar", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ — أَيْ ذُو أَقْسَامٍ.", "«kinds» — the khabar: «of kinds».", "«kısımlar» — haber: «kısımları olan».", punct="."),
  minhu(D), *ma_yakun(D),
  tok("بِمِنْ","min","part",[D, "huruf-jarr", "kana-wa-akhawatuha"], "الْبَاءُ حَرْفُ جَرٍّ، وَمِنْ مَقْصُودٌ لَفْظُهُ فِي مَحَلِّ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُ.", "«by min» — the letter named as a word; the khabar of kana.", "«min ile» — lafzı kastedilen harf; kâne'nin haberi.",
      segments=[seg("بِ","bi","part"), seg("مِنْ","min","part")], punct=".")]})

# ----------- s3 — لِي مِنْ فُلَانٍ صَدِيقٌ حَمِيمٌ
S.append({"id": "s3", "translation": {
 "en": "As they say: «I have, OUT OF so-and-so, a warm friend» — his friendship is so complete that another friend, like him, is drawn out of him." + R_EN,
 "tr": "Nitekim derler: «Falandan bana sıcak bir dost var» — dostluğu öyle kemâldedir ki ondan, onun gibi başka bir dost çıkarılır." + R_TR},
 "tokens": [
  kaqh(D, "pron-3mp"),
  tok("لِي","li","part",[D, "huruf-jarr", "mubtada-khabar", "ya-al-mutakallim"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«I have» — the fronted khabar.", "«bana var» — öne alınmış haber.", segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("مِنْ","min","part",[D, "huruf-jarr"], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ — حَرْفُ التَّجْرِيدِ.", "«out of» — the min of the tajrid.", "«-den» — tecrîd harfi."),
  tok("فُلَانٍ","fulan","noun",[D, "huruf-jarr"], "مَجْرُورٌ — الْأَمْرُ ذُو الصِّفَةِ: مِنْهُ يُنْتَزَعُ.", "«so-and-so» — the thing that has the quality; the other is drawn out of him.", "«falan» — sıfatın sahibi; öbürü ondan çıkarılır."),
  tok("صَدِيقٌ","sadiq","noun",[D, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — الْمُنْتَزَعُ: صَدِيقٌ آخَرُ مِثْلُهُ.", "«a friend» — the delayed mubtada; the drawn-out: another friend like him.", "«bir dost» — sona bırakılmış mübtedâ; çıkarılan: onun gibi başka bir dost."),
  tok("حَمِيمٌ","hamim","noun",[D, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَرْفُوعٌ — الْحَمِيمُ: الْقَرِيبُ الْوَدُودُ.", "«warm» — a na't; hamim is the close and loving.", "«sıcak» — na't; hamîm: yakın ve sevecen.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "min", "word": ix(S[-1], "صَدِيقٌ"), "companion": ix(S[-1], "فُلَانٍ")}]

# ----------- s4 — by the بِ (RESTORED heading)
S.append({"id": "s4", "translation": {"en": "Of it is what comes by the BAʾ." + R_EN, "tr": "Ondan biri BÂ ile olandır." + R_TR},
 "tokens": [
  minhu(D), *ma_yakun(D),
  tok("بِالْبَاءِ","ba-harf","noun",[D, "huruf-jarr", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ خَبَرُ يَكُونُ — الْبَاءُ: الْحَرْفُ.", "«by the baʾ» — the khabar of kana; the letter named.", "«bâ ile» — kâne'nin haberi; harfin adı.",
      segments=[seg("بِ","bi","part"), seg("الْبَاءِ","ba-harf","noun")], punct=".")]})

# ----------- s5 — لَئِنْ سَأَلْتَ فُلَانًا لَتَسْأَلَنَّ بِهِ الْبَحْرَ
S.append({"id": "s5", "translation": {
 "en": "As they say: «If you ask so-and-so, you will surely be asking, BY HIM, the sea» — the sea is drawn out of the giver; the ba carries it." + R_EN,
 "tr": "Nitekim derler: «Falandan istersen, ONUNLA denizden istemiş olursun» — deniz, verenden çıkarılmıştır; bâ onu taşır." + R_TR},
 "tokens": [
  kaqh(D, "pron-3mp"),
  tok("لَئِنْ","lain","part",[D, "in-shartiyya", "lam-jazim"], "اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if indeed» — the oath-paving lam on the conditional in.", "«eğer» — yemine zemin döşeyen lâm, şart edatı in."),
  tok("سَأَلْتَ","saala","verb",[D, "in-shartiyya"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«you ask» — the shart's verb; the ta its doer.", "«istersen» — şart fiili; tâ fâil."),
  tok("فُلَانًا","fulan","noun",[D, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — صَاحِبُ الصِّفَةِ.", "«so-and-so» — the object; the owner of the quality.", "«falanı» — mef'ûl; sıfatın sahibi."),
  tok("لَتَسْأَلَنَّ","saala","verb",[D, "nun-tawkid", "tawkid", "jawab-al-talab"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ الْمُقَدَّرِ، وَتَسْأَلَنَّ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — الْجُمْلَةُ جَوَابُ الْقَسَمِ، وَجَوَابُ الشَّرْطِ مَحْذُوفٌ.", "«you will surely ask» — the oath's answer: the lam and the heavy nun; the shart's own answer is unspoken.", "«elbette istersin» — yeminin cevabı: lâm ve şeddeli nûn; şartın cevabı hazfedilmiş.",
      segments=[seg("لَ","lam-qasam","part"), seg("تَسْأَلَ","saala","verb"), seg("نَّ","nun-tawkid","part")]),
  tok("بِهِ","bi","part",[D, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — بَاءُ التَّجْرِيدِ: مِنْهُ انْتُزِعَ الْبَحْرُ.", "«by him» — the ba of the tajrid: the sea is drawn out of him.", "«onunla» — tecrîd bâsı: deniz ondan çıkarılmıştır.", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْبَحْرَ","bahr","noun",[D, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُنْتَزَعُ: بَحْرٌ فِي الْعَطَاءِ.", "«the sea» — the object; the drawn-out: a sea of giving.", "«denizi» — mef'ûl; çıkarılan: cömertlikte bir deniz.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "bi", "word": ix(S[-1], "الْبَحْرَ"), "companion": ix(S[-1], "بِهِ")}]

# ----------- s6 — by the بِ of accompaniment (RESTORED heading)
S.append({"id": "s6", "translation": {"en": "Of it is what comes by the BAʾ OF ACCOMPANIMENT." + R_EN, "tr": "Ondan biri MAİYYET BÂSI ile olandır." + R_TR},
 "tokens": [
  minhu(D), *ma_yakun(D),
  tok("بِبَاءِ","ba-harf","noun",[D, "huruf-jarr", "idafa-definiteness", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — خَبَرُ يَكُونُ.", "«by the ba» — annexed; the khabar of kana.", "«bâsı ile» — muzâf; kâne'nin haberi.",
      segments=[seg("بِ","bi","part"), seg("بَاءِ","ba-harf","noun")]),
  tok("الْمَعِيَّةِ","maiyya","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَعِيَّةُ: الْمُصَاحَبَةُ.", "«of accompaniment» — maʿiyya: being-with.", "«maiyyetin» — birliktelik.", punct=".")]})

# ----------- s7 — Dhu l-Rumma: the mare carries me … with an armoured rider (himself)
S.append({"id": "s7", "translation": {
 "en": "As Dhu l-Rumma says: «Many a wide-mouthed mare runs with me toward the crier of battle • WITH A MAILED RIDER like the tar-smeared stallion camel» — the rider drawn out of the speaker is the speaker himself." + R_EN,
 "tr": "Zürrumme'nin dediği gibi: «Nice geniş ağızlı kısrak beni harp çağırıcısına doğru koşturur • katranlı azgın deve gibi ZIRHLI BİR SÜVÂRİ İLE» — konuşandan çıkarılan süvâri konuşanın kendisidir." + R_TR},
 "tokens": [
  kaqawl(D),
  tok("ذِي","dhu-al-rumma","noun",[D, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ — ذُو الرُّمَّةِ غَيْلَانُ بْنُ عُقْبَةَ.", "«Dhu» — of the five nouns; Dhu l-Rumma, Ghaylan b. ʿUqba.", "«Zü» — esmâ-i hamseden; Zürrumme, Gaylân b. Ukbe."),
  tok("الرُّمَّةِ","rumma","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«l-Rumma».", "«'r-Rumme».", punct=":"),
  tok("وَشَوْهَاءَ","shawha","noun",[D, "huruf-jarr-nawadir", "mamnu-min-sarf", "mubtada-khabar"], "الْوَاوُ وَاوُ رُبَّ، وَشَوْهَاءَ مَجْرُورٌ بِرُبَّ الْمَحْذُوفَةِ، عَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ؛ الشَّوْهَاءُ: الْفَرَسُ الْوَاسِعَةُ الْفَمِ.", "«many a wide-mouthed mare» — the waw of rubba; a diptote, its jarr a fatha; the mubtada in place.", "«nice geniş ağızlı kısrak» — rubbe vâvı; gayr-i munsarif, cerri fetha; mahallen mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("شَوْهَاءَ","shawha","noun")]),
  tok("تَعْدُو","ada-run","verb",[D, "mudari-marfu", "naqis-verbs", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ — الْجُمْلَةُ خَبَرٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«runs» — the khabar clause; the doer concealed.", "«koşar» — haber cümlesi; fâil gizli."),
  tok("بِي","bi","part",[D, "huruf-jarr", "ya-al-mutakallim"], "جَارٌّ وَمَجْرُورٌ — الْمُتَكَلِّمُ: صَاحِبُ الصِّفَةِ.", "«with me» — the speaker: the owner of the quality.", "«beni» — konuşan: sıfatın sahibi.", segments=[seg("بِ","bi","part"), seg("ي","pron-1s","pron")]),
  tok("إِلَى","ila","part",[D, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«toward».", "«-e doğru»."),
  tok("صَارِخِ","sarikh","noun",[D, "huruf-jarr", "idafa-definiteness", "ism-fail"], "مَجْرُورٌ مُضَافٌ — اسْمُ فَاعِلِ صَرَخَ: الْمُسْتَغِيثُ.", "«the crier» — annexed; the one calling for help.", "«çağırıcısına» — muzâf; yardım isteyen."),
  tok("الْوَغَى","wagha","noun",[D, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ: الْحَرْبُ.", "«of battle» — a maqsur: the din of war.", "«harbin» — maksûr: savaş.", punct="*"),
  tok("بِمُسْتَلْئِمٍ","mustalim","noun",[D, "huruf-jarr", "hal", "ism-fail"], "الْبَاءُ لِلْمُصَاحَبَةِ، وَمُسْتَلْئِمٍ مَجْرُورٌ — حَالٌ مِنْ يَاءِ بِي: مَعَ فَارِسٍ مُدَرَّعٍ، وَهُوَ الشَّاعِرُ نَفْسُهُ: التَّجْرِيدُ.", "«with a mailed rider» — the ba of accompaniment; a hal of «me»: the rider is the speaker himself — the tajrid.", "«zırhlı bir süvâri ile» — maiyyet bâsı; «beni»nin hâli: süvâri konuşanın kendisidir — tecrîd.",
      segments=[seg("بِ","bi","part"), seg("مُسْتَلْئِمٍ","mustalim","noun")]),
  tok("مِثْلِ","mithl","noun",[D, "naat-sifa", "idafa-definiteness"], "نَعْتٌ لِمُسْتَلْئِمٍ مَجْرُورٌ مُضَافٌ.", "«like» — a na't, annexed.", "«gibi» — na't, muzâf."),
  tok("الْفَنِيقِ","faniq","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْفَنِيقُ: الْفَحْلُ الْمُكْرَمُ مِنَ الْإِبِلِ.", "«the stallion camel» — the prized stud.", "«azgın deve» — değerli erkek deve."),
  tok("الْمُدَجَّلِ","mudajjal","noun",[D, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولِ دَجَّلَ: الْمَطْلِيُّ بِالْقَطِرَانِ.", "«tar-smeared» — the ism maf'ul of dajjala.", "«katranlı» — deccele'nin ism-i mef'ûlü.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "bi-musahaba", "word": ix(S[-1], "بِمُسْتَلْئِمٍ"), "companion": ix(S[-1], "بِي")}]

# ----------- s8 — by فِي (RESTORED heading)
S.append({"id": "s8", "translation": {"en": "Of it is what comes by FI." + R_EN, "tr": "Ondan biri FÎ ile olandır." + R_TR},
 "tokens": [
  minhu(D), *ma_yakun(D),
  tok("بِفِي","fi","part",[D, "huruf-jarr", "kana-wa-akhawatuha"], "الْبَاءُ حَرْفُ جَرٍّ، وَفِي مَقْصُودٌ لَفْظُهُ — خَبَرُ يَكُونُ.", "«by fi» — the letter named; the khabar of kana.", "«fî ile» — lafzı kastedilen harf; kâne'nin haberi.",
      segments=[seg("بِ","bi","part"), seg("فِي","fi","part")], punct=".")]})

# ----------- s9 — 41:28 لَهُمْ فِيهَا دَارُ الْخُلْدِ
S.append({"id": "s9", "translation": {
 "en": "As He says, exalted is He: «Theirs, IN IT, is the abode of eternity» — the Fire is the abode of eternity, and yet an abode is drawn out of it, in it." + R_EN,
 "tr": "Nitekim Allah Teâlâ buyurur: «Onlar için ONDA ebedîlik yurdu vardır» — ateşin kendisi ebedîlik yurdudur; yine de ondan, onun içinde bir yurt çıkarılmıştır." + R_TR},
 "tokens": [
  kaqh(D), taala(D),
  tok("لَهُمْ","li","part",[D, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«theirs» — the fronted khabar.", "«onlar için» — öne alınmış haber.", segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("فِيهَا","fi","part",[D, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْخَبَرِ — الضَّمِيرُ لِلنَّارِ: صَاحِبَةُ الصِّفَةِ.", "«in it» — the pronoun is the Fire: the owner of the quality.", "«onda» — zamir ateşe: sıfatın sahibi.", segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("دَارُ","dar","noun",[D, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ — الْمُنْتَزَعُ: دَارٌ مِنَ النَّارِ وَهِيَ النَّارُ.", "«the abode» — the delayed mubtada; the drawn-out: an abode out of the Fire, which IS the Fire.", "«yurdu» — sona bırakılmış mübtedâ; çıkarılan: ateşten bir yurt ki ateşin kendisidir."),
  tok("الْخُلْدِ","khuld","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of eternity».", "«ebedîliğin».", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "fi", "word": ix(S[-1], "دَارُ"), "companion": ix(S[-1], "فِيهَا")}]

# ----------- s10 — with no letter (RESTORED heading)
S.append({"id": "s10", "translation": {"en": "Of it is what comes with NO letter between." + R_EN, "tr": "Ondan biri araya HİÇBİR HARF girmeden olandır." + R_TR},
 "tokens": [
  minhu(D), *ma_yakun(D),
  tok("بِلَا","la-nafiya","part",[D, "huruf-jarr", "kana-wa-akhawatuha"], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا زَائِدَةٌ بِمَعْنَى غَيْرِ — خَبَرُ يَكُونُ.", "«with no» — the ba, and la in the sense of «without».", "«…-sız» — bâ ve «gayr» mânâsında lâ.",
      segments=[seg("بِ","bi","part"), seg("لَا","la-nafiya","part")]),
  tok("وَاسِطَةِ","wasita","noun",[D, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the mediation» — annexed.", "«vâsıtası» — muzâf."),
  tok("حَرْفٍ","harf","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of a letter».", "«bir harfin».", punct=".")]})

# ----------- s11 — Qatada: … or a noble man dies (himself)
S.append({"id": "s11", "translation": {
 "en": "As Qatada says: «If I live, I will surely set out on a raid • that gathers the spoils — or a NOBLE MAN dies» — the noble man drawn out of «I» with no letter: it is the speaker." + R_EN,
 "tr": "Katâde'nin dediği gibi: «Sağ kalırsam elbette bir gazâya çıkarım • ganimetleri toplayan — yahut bir KERÎM ölür» — «ben»den harfsiz çıkarılan kerîm: konuşanın kendisi." + R_TR},
 "tokens": [
  kaqawl(D),
  tok("قَتَادَةَ","qatada","noun",[D, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — عَلَمٌ مُؤَنَّثٌ بِالتَّاءِ: مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Qatada» — a name with the ta: a diptote, jarr by a fatha.", "«Katâde» — tâlı alem: gayr-i munsarif, cerri fetha.", punct=":"),
  wa_conj("وَلَئِنْ","lain","part",[D, "in-shartiyya", "lam-jazim"], "لَئِنْ: اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَإِنْ شَرْطِيَّةٌ.", "«and if indeed».", "«ve eğer»."),
  tok("بَقِيتُ","baqiya","verb",[D, "in-shartiyya", "naqis-verbs"], "فِعْلٌ مَاضٍ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ فَاعِلٌ: الْمُتَكَلِّمُ — صَاحِبُ الصِّفَةِ.", "«I live» — the shart's verb; the speaker, owner of the quality.", "«sağ kalırsam» — şart fiili; konuşan, sıfatın sahibi."),
  tok("لَأَرْحَلَنَّ","rahala","verb",[D, "nun-tawkid", "tawkid", "jawab-al-talab"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَأَرْحَلَنَّ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِنُونِ التَّوْكِيدِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I will surely set out» — the oath's answer with the heavy nun.", "«elbette çıkarım» — şeddeli nûnla yeminin cevabı.",
      segments=[seg("لَ","lam-qasam","part"), seg("أَرْحَلَ","rahala","verb"), seg("نَّ","nun-tawkid","part")]),
  tok("بِغَزْوَةٍ","ghazwa","noun",[D, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«on a raid».", "«bir gazâya».", segments=[seg("بِ","bi","part"), seg("غَزْوَةٍ","ghazwa","noun")], punct="*"),
  tok("تَحْوِي","hawa-contain","verb",[D, "mudari-marfu", "naqis-verbs", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — الْجُمْلَةُ نَعْتٌ لِغَزْوَةٍ.", "«that gathers» — a clause as the raid's na't.", "«toplayan» — gazânın na'ti olan cümle."),
  tok("الْغَنَائِمَ","ghanima","noun",[D, "maful-bihi", "jam-taksir", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ غَنِيمَةٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.", "«the spoils» — the object; a plural of plurals.", "«ganimetleri» — mef'ûl; müntehe'l-cümû'."),
  tok("أَوْ","aw","part",[D, "atf-nasaq", "an-masdariyya"], "أَوْ بِمَعْنَى إِلَّا أَنْ — يَنْتَصِبُ الْمُضَارِعُ بَعْدَهَا بِأَنْ مُضْمَرَةٍ.", "«or» — in the sense of «unless»; the mudari after it is mansub by a hidden an.", "«yahut» — «meğer ki» mânâsında; ardındaki muzâri gizli en ile mansûb."),
  tok("يَمُوتَ","mata-die","verb",[D, "an-masdariyya", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ أَوْ.", "«dies» — mansub by the hidden an after aw.", "«ölür» — ev'den sonra gizli en ile mansûb."),
  tok("كَرِيمُ","karim","noun",[D, "fail", "sifa-mushabbaha"], "فَاعِلٌ مَرْفُوعٌ، سُكِّنَ لِلْقَافِيَةِ — الْمُنْتَزَعُ مِنَ الْمُتَكَلِّمِ بِلَا حَرْفٍ: هُوَ الشَّاعِرُ.", "«a noble man» — the doer, its tanwin quieted by the rhyme; drawn out of «I» with no letter: the poet himself.", "«bir kerîm» — fâil, tenvini kâfiyece susturulmuş; «ben»den harfsiz çıkarılan: şairin kendisi.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "bila-harf", "word": ix(S[-1], "كَرِيمُ"), "companion": ix(S[-1], "بَقِيتُ")}]

# ----------- s12 — by way of kinaya (RESTORED heading)
S.append({"id": "s12", "translation": {"en": "Of it is what comes BY WAY OF KINAYA." + R_EN, "tr": "Ondan biri KİNÂYE YOLUYLA olandır." + R_TR},
 "tokens": [
  minhu(D), *ma_yakun(D),
  tok("بِطَرِيقِ","tariq","noun",[D, "huruf-jarr", "idafa-definiteness", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — خَبَرُ يَكُونُ.", "«by way of» — annexed; the khabar.", "«yoluyla» — muzâf; haber.",
      segments=[seg("بِ","bi","part"), seg("طَرِيقِ","tariq","noun")]),
  tok("الْكِنَايَةِ","kinaya","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«kinaya».", "«kinâyenin».", punct=".")]})

# ----------- s13 — al-Aʿsha: O best of those who ride … and drinks no cup from a miser's hand
S.append({"id": "s13", "translation": {
 "en": "As al-Aʿsha says: «O BEST of those who ride the mounts, and who • drinks no cup from the hand of one who is STINGY» — by kinaya he makes of one man two: the drinker and the hand that pours." + R_EN,
 "tr": "A'şâ'nın dediği gibi: «Ey binekleri sürenlerin en HAYIRLISI, ve • CİMRİNİN eliyle kâse içmeyen» — kinâye ile bir insanı iki eder: içen ve sunan el." + R_TR},
 "tokens": [
  kaqawl(D),
  tok("الْأَعْشَى","asha","noun",[D, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ: الْأَعْشَى مَيْمُونُ بْنُ قَيْسٍ.", "«al-Aʿsha» — a maqsur: Maymun b. Qays.", "«A'şâ» — maksûr: Meymûn b. Kays.", punct=":"),
  tok("يَا","ya","part",[D, "vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("خَيْرَ","khayr","noun",[D, "vocative-munada", "idafa-definiteness"], "مُنَادًى مَنْصُوبٌ مُضَافٌ — الْمَمْدُوحُ: صَاحِبُ الصِّفَةِ.", "«best» — the annexed munada; the praised one, owner of the quality.", "«en hayırlısı» — muzâf münâdâ; övülen, sıfatın sahibi."),
  tok("مَنْ","man-mawsula","pron",[D, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«those who».", "«…-enlerin»."),
  tok("يَرْكَبُ","rakiba","verb",[D, "ism-mawsul", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ.", "«ride».", "«sürer»."),
  tok("الْمَطِيَّ","matiyy","noun",[D, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمَطِيُّ: الرَّوَاحِلُ.", "«the mounts» — the riding beasts.", "«binekleri» — binek hayvanları."),
  wa_conj("وَلَا","la-nafiya","part",[D, "atf-nasaq"], "لَا نَافِيَةٌ.", "«and not».", "«ve …-meyen».", punct="*"),
  tok("يَشْرَبُ","shariba","verb",[D, "atf-nasaq", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَعْطُوفٌ عَلَى يَرْكَبُ مَرْفُوعٌ — دَاخِلٌ فِي الصِّلَةِ.", "«drinks» — joined to «ride», inside the sila.", "«içer» — «sürer»e ma'tûf, sıla içinde."),
  tok("كَأْسًا","kas","noun",[D, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a cup».", "«bir kâse»."),
  tok("بِكَفِّ","kaff-hand","noun",[D, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — الْكِنَايَةُ: كَفُّ الْبَخِيلِ هِيَ كَفُّهُ لَوْ بَخِلَ، فَجَعَلَ مِنْ نَفْسِهِ آخَرَ.", "«from the hand of» — the kinaya: the miser's hand would be his own if he were stingy; so he makes of himself another.", "«eliyle» — kinâye: cimrinin eli, cimri olsa kendi elidir; böylece kendinden bir başkası çıkarır.",
      segments=[seg("بِ","bi","part"), seg("كَفِّ","kaff-hand","noun")]),
  tok("مَنْ","man-mawsula","pron",[D, "ism-mawsul", "idafa-definiteness"], "مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْمُنْتَزَعُ.", "«one who» — the drawn-out.", "«…-in» — çıkarılan."),
  tok("بَخِلَا","bakhila","verb",[D, "ism-mawsul"], "فِعْلٌ مَاضٍ — صِلَةٌ، وَالْأَلِفُ لِلْإِطْلَاقِ.", "«is stingy» — the sila; the alif is the rhyme's.", "«cimridir» — sıla; elif ıtlâk elifi.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "kinaya", "word": ix(S[-1], "بِكَفِّ"), "companion": ix(S[-1], "خَيْرَ")}]

# ----------- s14 — by addressing oneself (RESTORED heading)
S.append({"id": "s14", "translation": {"en": "Of it is what comes by a man ADDRESSING HIMSELF." + R_EN, "tr": "Ondan biri insanın KENDİNE HİTAP ETMESİYLE olandır." + R_TR},
 "tokens": [
  minhu(D), *ma_yakun(D),
  tok("بِمُخَاطَبَةِ","mukhataba","noun",[D, "huruf-jarr", "idafa-definiteness", "masdar", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — مَصْدَرُ خَاطَبَ؛ خَبَرُ يَكُونُ.", "«by the addressing» — the masdar of khataba; the khabar.", "«hitap etmesiyle» — hâtabe'nin masdarı; haber.",
      segments=[seg("بِ","bi","part"), seg("مُخَاطَبَةِ","mukhataba","noun")]),
  tok("الْإِنْسَانِ","insan","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلُ الْمَصْدَرِ فِي الْمَعْنَى.", "«a man» — the masdar's doer in sense.", "«insanın» — mânâca masdarın fâili."),
  tok("نَفْسَهُ","nafs","noun",[D, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«himself» — the masdar's object.", "«kendine» — masdarın mef'ûlü.",
      segments=[seg("نَفْسَ","nafs","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s15 — al-Mutanabbi to himself: no horses with you, no wealth
S.append({"id": "s15", "translation": {
 "en": "As al-Mutanabbi says: «No horses have YOU to give, and no wealth; • so let speech help, if fortune does not» — the poet addresses himself as another." + R_EN,
 "tr": "Mütenebbî'nin dediği gibi: «SENDE hediye edecek at yok, mal da yok; • hâl yardım etmezse söz yardım etsin» — şair kendine bir başkası gibi hitap eder." + R_TR},
 "tokens": [
  kaqawl(D),
  tok("الْمُتَنَبِّي","mutanabbi","noun",[D, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«al-Mutanabbi».", "«Mütenebbî».", punct=":"),
  tok("لَا","la-nafiya","part",[D, "la-nafiya-lil-jins"], "لَا النَّافِيَةُ لِلْجِنْسِ — تَعْمَلُ عَمَلَ إِنَّ.", "«no» — the la that denies the whole kind.", "«hiç … yok» — cinsi nefyeden lâ."),
  tok("خَيْلَ","khayl","noun",[D, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«horses» — the ism of la, built on the fatha.", "«at» — lâ'nın ismi, fetha üzere mebnî."),
  tok("عِنْدَكَ","inda","noun",[D, "la-nafiya-lil-jins", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ خَبَرُ لَا، وَالْكَافُ مُضَافٌ إِلَيْهِ — الْمُخَاطَبُ هُوَ الشَّاعِرُ نَفْسُهُ: التَّجْرِيدُ.", "«with you» — the zarf, la's khabar; the «you» is the poet himself — the tajrid.", "«sende» — zarf, lâ'nın haberi; «sen» şairin kendisidir — tecrîd.",
      segments=[seg("عِنْدَ","inda","noun"), seg("كَ","pron-2ms","pron")]),
  tok("تُهْدِيهَا","ahda","verb",[D, "mudari-marfu", "form-iv-verbs", "naqis-verbs", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ نَعْتٌ لِخَيْلَ، وَالْفَاعِلُ: أَنْتَ.", "«you would give» — a clause as the horses' na't; the doer «you».", "«hediye edeceğin» — atın na'ti olan cümle; fâil «sen».",
      segments=[seg("تُهْدِي","ahda","verb"), seg("هَا","pron-3fs","pron")]),
  wa_conj("وَلَا","la-nafiya","part",[D, "atf-nasaq", "la-nafiya-lil-jins"], "لَا نَافِيَةٌ لِلْجِنْسِ مُكَرَّرَةٌ.", "«and no».", "«ve … yok»."),
  tok("مَالَ","mal","noun",[D, "la-nafiya-lil-jins"], "اسْمُ لَا الثَّانِيَةِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«wealth» — the second la's ism; its khabar unspoken.", "«mal» — ikinci lâ'nın ismi; haberi hazfedilmiş.", punct="*"),
  tok("فَلْيُسْعِدِ","asada","verb",[D, "lam-amr", "form-iv-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لَامُ الْأَمْرِ، وَيُسْعِدِ مُضَارِعٌ مَجْزُومٌ بِهَا، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«so let … help» — the lam of command; the jussive takes a kasra before the wasl.", "«öyleyse … yardım etsin» — emir lâmı; meczûm, vasıldan önce kesre alır.",
      segments=[seg("فَ","fa","conj"), seg("لْ","lam-amr","part"), seg("يُسْعِدِ","asada","verb")]),
  tok("النُّطْقُ","nutq","noun",[D, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«speech» — the doer.", "«söz» — fâil."),
  tok("إِنْ","in-shartiyya","part",[D, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("لَمْ","lam","part",[D, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«…-mezse»."),
  tok("تُسْعِدِ","asada","verb",[D, "lam-jazim", "in-shartiyya", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ فِعْلُ الشَّرْطِ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَجَوَابُ الشَّرْطِ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«does help» — jussive by lam, the shart's verb; the answer is what came before.", "«yardım etmezse» — lem ile meczûm şart fiili; cevabı öncesidir."),
  tok("الْحَالُ","hal","noun",[D, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«fortune» — the doer.", "«hâl» — fâil.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajrid", "sub": "nafs", "word": ix(S[-1], "عِنْدَكَ"), "companion": ix(S[-1], "تُهْدِيهَا")}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "tajrid": need("tajrid", "تَجْرِيد", "ج ر د", "noun", "tajrid — drawing out of a thing another like it, for hyperbole (masdar of جَرَّدَ)", "tecrîd — bir şeyden onun gibi bir başkasını çıkarmak, mübalağa için (جَرَّدَ'nin masdarı)", 5),
 "intazaa": need("intazaa", "اِنْتَزَعَ", "ن ز ع", "verb", "to draw out, to extract (Form VIII)", "çıkarmak, çekip almak (VIII. bâb)", 5, form="VIII"),
 "sifa": need("sifa", "صِفَة", "و ص ف", "noun", "a quality, an attribute; an adjective", "sıfat, nitelik", 2),
 "mithl": need("mithl", "مِثْل", "م ث ل", "noun", "the like of, similar to", "benzeri, gibi", 2),
 "kamal": need("kamal", "كَمَال", "ك م ل", "noun", "completeness, perfection", "kemâl, tamlık", 3),
 "mubalagha": need("mubalagha", "مُبَالَغَة", "ب ل غ", "noun", "hyperbole, overstatement (masdar of بَالَغَ)", "mübalağa, aşırılık (بَالَغَ'nin masdarı)", 4),
 "ba-harf": need("ba-harf", "الْبَاء", None, "noun", "the letter ba — named as a word", "bâ harfi — adıyla anılan", 3),
 "hamim": need("hamim", "حَمِيم", "ح م م", "noun", "warm, intimate (of a friend)", "sıcak, yakın (dost için)", 5),
 "maiyya": need("maiyya", "مَعِيَّة", None, "noun", "accompaniment, being-with (the ba of maʿiyya)", "maiyyet, birliktelik (maiyyet bâsı)", 5),
 "dhu-al-rumma": need("dhu-al-rumma", "ذُو الرُّمَّة", None, "propn", "Dhu l-Rumma — Ghaylan b. ʿUqba, the Umayyad desert poet (d. 117/735)", "Zürrumme — Gaylân b. Ukbe, Emevî çöl şairi (ö. 117/735)", 6),
 "rumma": need("rumma", "رُمَّة", "ر م م", "noun", "a frayed length of rope", "eski ip parçası", 5),
 "shawha": need("shawha", "شَوْهَاء", "ش و ه", "noun", "a wide-mouthed mare (a diptote, فَعْلَاء)", "geniş ağızlı kısrak (gayr-i munsarif, فَعْلَاء)", 6),
 "ada-run": need("ada-run", "عَدَا", "ع د و", "verb", "to run (عَدَا يَعْدُو)", "koşmak (عَدَا يَعْدُو)", 4, form="I"),
 "sarikh": need("sarikh", "صَارِخ", "ص ر خ", "noun", "one crying out, calling for help (ism fa'il of صَرَخَ)", "bağıran, yardım isteyen (صَرَخَ'nin ism-i fâili)", 5),
 "wagha": need("wagha", "وَغًى", "و غ ي", "noun", "the din of battle; war (a maqsur noun)", "savaş gürültüsü; harp (maksûr isim)", 6),
 "mustalim": need("mustalim", "مُسْتَلْئِم", "ل أ م", "noun", "one wearing a coat of mail (ism fa'il of اسْتَلْأَمَ)", "zırh giymiş (اسْتَلْأَمَ'nin ism-i fâili)", 6),
 "faniq": need("faniq", "فَنِيق", "ف ن ق", "noun", "a prized stallion camel", "değerli erkek deve", 6),
 "mudajjal": need("mudajjal", "مُدَجَّل", "د ج ل", "noun", "smeared with tar (ism maf'ul of دَجَّلَ)", "katrana bulanmış (دَجَّلَ'nin ism-i mef'ûlü)", 6),
 "wasita": need("wasita", "وَاسِطَة", "و س ط", "noun", "a mediation, a go-between", "vâsıta, aracı", 4),
 "harf": need("harf", "حَرْف", "ح ر ف", "noun", "a letter; a particle", "harf", 1),
 "qatada": need("qatada", "قَتَادَة", None, "propn", "Qatada — Qatada b. Maslama al-Hanafi, the poet of Bakr (a diptote name)", "Katâde — Katâde b. Mesleme el-Hanefî, Bekr şairi (gayr-i munsarif alem)", 6),
 "ghazwa": need("ghazwa", "غَزْوَة", "غ ز و", "noun", "a raid, an expedition", "gazâ, sefer", 4),
 "hawa-contain": need("hawa-contain", "حَوَى", "ح و ي", "verb", "to contain, to gather in (حَوَى يَحْوِي)", "içine almak, toplamak (حَوَى يَحْوِي)", 4, form="I"),
 "ghanima": need("ghanima", "غَنِيمَة", "غ ن م", "noun", "spoil, booty", "ganimet", 4, plural="غَنَائِم"),
 "tariq": need("tariq", "طَرِيق", "ط ر ق", "noun", "a way, a road", "yol, tarik", 2),
 "kinaya": need("kinaya", "كِنَايَة", "ك ن ي", "noun", "kinaya — saying a thing by what follows from it", "kinâye — bir şeyi lâzımıyla söylemek", 4),
 "asha": need("asha", "الْأَعْشَى", None, "propn", "al-Aʿsha — Maymun b. Qays, the pre-Islamic poet (d. c. 7/629)", "A'şâ — Meymûn b. Kays, Câhiliye şairi (ö. yak. 7/629)", 6),
 "matiyy": need("matiyy", "مَطِيّ", "م ط و", "noun", "riding beasts, mounts (a collective)", "binek hayvanları, binekler (cins ismi)", 6),
 "kaff-hand": need("kaff-hand", "كَفّ", "ك ف ف", "noun", "the palm, the hand", "el, avuç", 3),
 "mukhataba": need("mukhataba", "مُخَاطَبَة", "خ ط ب", "noun", "addressing, speaking to (masdar of خَاطَبَ)", "hitap etme (خَاطَبَ'nin masdarı)", 4),
 "insan": need("insan", "إِنْسَان", "أ ن س", "noun", "a human being, a man", "insan", 2),
 "khayl": need("khayl", "خَيْل", "خ ي ل", "noun", "horses (a collective)", "atlar (cins ismi)", 3),
 "inda": need("inda", "عِنْدَ", None, "noun", "with, at, in the possession of (a zarf)", "yanında, katında (zarf)", 2),
 "ahda": need("ahda", "أَهْدَى", "ه د ي", "verb", "to give as a gift (Form IV, naqis)", "hediye etmek (IV. bâb, nâkıs)", 4, form="IV"),
 "asada": need("asada", "أَسْعَدَ", "س ع د", "verb", "to help, to make happy (Form IV)", "yardım etmek, mutlu kılmak (IV. bâb)", 4, form="IV"),
 "nutq": need("nutq", "نُطْق", "ن ط ق", "noun", "speech, utterance (masdar of نَطَقَ)", "söz, konuşma (نَطَقَ'nin masdarı)", 4),
 "mutanabbi": need("mutanabbi", "الْمُتَنَبِّي", None, "propn", "al-Mutanabbi — Abu l-Tayyib Ahmad b. al-Husayn, the poet of Sayf al-Dawla (d. 354/965)", "el-Mütenebbî — Ebü't-Tayyib Ahmed b. Hüseyin, Seyfüddevle'nin şairi (ö. 354/965)", 6),
}
for k in ("qawl", "min", "huwa", "an-masdariyya", "kana", "amr", "dhu", "akhar", "fi", "li", "bi", "ila", "ka", "wa", "fa", "pron-3fs", "pron-3ms", "pron-3mp", "pron-1s", "pron-2ms",
          "aqsam", "ma-mawsula", "man-mawsula", "fulan", "sadiq", "lain", "saala", "bahr", "dar", "khuld", "la-nafiya", "baqiya", "rahala", "aw", "mata-die", "karim", "ya", "khayr",
          "rakiba", "shariba", "kas", "bakhila", "nafs", "mal", "lam-amr", "in-shartiyya", "lam", "hal", "taala", "tawkid", "nun-tawkid"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

if not os.environ.get("DRY_PKG"):
    pass
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "intazaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَزَع", "نْتَزِع", "اِنْتَزِع", "اِنْتِزَاع", "مُنْتَزِع", "مُنْتَزَع", "اُنْتُزِعَ", "يُنْتَزَعُ"))
put_morph(mo, "ada-run", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "عَدَ", "عْد", "u", "اُعْد", "عَدْو", "عَادٍ (الْعَادِي)", "مَعْدُوّ", "عُدِيَ", "يُعْدَى"))
put_morph(mo, "hawa-contain", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "حَوَ", "حْو", "i", "اِحْو", "حَوْي", "حَاوٍ (الْحَاوِي)", "مَحْوِيّ", "حُوِيَ", "يُحْوَى"))
put_morph(mo, "ahda", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَهْدَ", "هْد", "i", "أَهْد", "إِهْدَاء", "مُهْدٍ (الْمُهْدِي)", "مُهْدًى", "أُهْدِيَ", "يُهْدَى"))
put_morph(mo, "asada", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْعَد", "سْعِد", "أَسْعِد", "إِسْعَاد", "مُسْعِد", "مُسْعَد", "أُسْعِدَ", "يُسْعَدُ"))
# a verb copied in from another package brings its paradigm with it (the release gate wants every glossary verb conjugated)
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note
NOTE_D = {
 "id": "tajrid",
 "title": {"ar": "التَّجْرِيدُ — أَنْ يُنْتَزَعَ مِنْ أَمْرٍ ذِي صِفَةٍ أَمْرٌ آخَرُ مِثْلُهُ فِيهَا مُبَالَغَةً", "en": "The tajrid — out of a thing with a quality, another like it is drawn, for hyperbole", "tr": "Tecrîd — sıfatı olan bir şeyden, o sıfatta onun gibi bir başkası çıkarılır, mübalağa için"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التجريد: أن ينتزع من أمر ذي صفة أمر آخر مثله فيها مبالغة لكمالها فيه؛ وهو أقسام: بمن، بالباء، بباء المعية، بفي، بلا واسطة حرف، بطريق الكناية، بمخاطبة الإنسان نفسه"],
 "question": {
  "en": ["Is a SECOND figure drawn out of a first that has the quality — so complete in it that another like it can be taken from it? «I have out of so-and-so a warm friend» — the friend is drawn OUT OF the friend. That is the TAJRID.",
         "By what? By مِنْ (لِي مِنْ فُلَانٍ صَدِيقٌ), by بِ (لَتَسْأَلَنَّ بِهِ الْبَحْرَ), by the بِ of accompaniment (تَعْدُو بِي … بِمُسْتَلْئِمٍ — the rider is the speaker), by فِي (لَهُمْ فِيهَا دَارُ الْخُلْدِ — the abode drawn out of the Fire that IS the abode), with no letter (أَوْ يَمُوتَ كَرِيمُ — the noble man is the «I» who spoke), by kinaya (بِكَفِّ مَنْ بَخِلَا — the miser's hand is his own if he were stingy), and by a man addressing himself (لَا خَيْلَ عِنْدَكَ — Mutanabbi to Mutanabbi).",
         "What does the engine read? The letter and the seats: a fronted لِ-khabar with مِنْ + a name + an indefinite mubtada; a verb of asking with بِ + pronoun + a definite object; a motion verb with بِي and a بِ-participle as its hal; لَهُمْ فِيهَا + a construct mubtada; a first-person clause then أَوْ + verb + an indefinite doer; a vocative with a relative and a negation; the second-person marks in a poet's own voice."],
  "tr": ["Sıfatı olan bir ilkten İKİNCİ bir figür mü çıkarılıyor — sıfat onda öyle tam ki ondan onun gibisi alınabiliyor? «Falandan bana sıcak bir dost var» — dost, dostun İÇİNDEN çıkarılır. TECRÎD budur.",
         "Ne ile? مِنْ ile (لِي مِنْ فُلَانٍ صَدِيقٌ), بِ ile (لَتَسْأَلَنَّ بِهِ الْبَحْرَ), maiyyet بِ'si ile (تَعْدُو بِي … بِمُسْتَلْئِمٍ — süvâri konuşandır), فِي ile (لَهُمْ فِيهَا دَارُ الْخُلْدِ — yurt, yurdun KENDİSİ olan ateşten çıkarılır), harfsiz (أَوْ يَمُوتَ كَرِيمُ — kerîm, konuşan «ben»dir), kinâye ile (بِكَفِّ مَنْ بَخِلَا — cimrinin eli cimri olsa kendi elidir), kendine hitapla (لَا خَيْلَ عِنْدَكَ — Mütenebbî Mütenebbî'ye).",
         "Motor neyi okur? Harfi ve koltukları: öne alınmış لِ haberi ile مِنْ + isim + nekre mübtedâ; istemek fiili ile بِ + zamir + belirli mef'ûl; بِي'li hareket fiili ve hâl olan بِ'li ism-i fâil; لَهُمْ فِيهَا + muzâf mübtedâ; birinci şahıs cümlesi, sonra أَوْ + fiil + nekre fâil; sıla ve nefiyli nidâ; şairin kendi sesindeki ikinci şahıs alâmetleri."]},
 "plain": {
  "en": "The tajrid: out of a thing that has a quality, another thing like it is drawn — for hyperbole, because the quality is complete in it. Seven ways: by min, by bi, by the bi of accompaniment, by fi, with no letter, by kinaya, by self-address. The engine reads the letter and the seats that carry each.",
  "tr": "Tecrîd: sıfatı olan bir şeyden onun gibi bir başkası çıkarılır — mübalağa için, sıfat onda tam olduğundan. Yedi yol: min ile, bâ ile, maiyyet bâsı ile, fî ile, harfsiz, kinâye ile, kendine hitapla. Motor her birini taşıyan harfi ve koltukları okur."},
 "explanation": {
  "en": "The TAJRID is أَنْ يُنْتَزَعَ مِنْ أَمْرٍ ذِي صِفَةٍ أَمْرٌ آخَرُ مِثْلُهُ فِيهَا مُبَالَغَةً لِكَمَالِهَا فِيهِ — out of a thing that HAS a quality, ANOTHER thing like it in that quality is drawn, for hyperbole: the quality is so complete in the first that a second can be taken from it. Its kinds are told by the letter that carries the drawing-out. By مِنْ: لِي مِنْ فُلَانٍ صَدِيقٌ حَمِيمٌ — a friend out of the friend. By بِ: لَئِنْ سَأَلْتَ فُلَانًا لَتَسْأَلَنَّ بِهِ الْبَحْرَ — the sea, asked BY him. By the بِ of accompaniment: Dhu l-Rumma's وَشَوْهَاءَ تَعْدُو بِي إِلَى صَارِخِ الْوَغَى بِمُسْتَلْئِمٍ — the mare carries «me» WITH a mailed rider, who is the poet himself. By فِي: لَهُمْ فِيهَا دَارُ الْخُلْدِ (41:28) — the Fire is the abode of eternity, yet an abode is drawn out of it, IN it. With no letter: Qatada's وَلَئِنْ بَقِيتُ لَأَرْحَلَنَّ بِغَزْوَةٍ تَحْوِي الْغَنَائِمَ أَوْ يَمُوتَ كَرِيمُ — «or a noble man dies»: the noble man is the «I» who spoke; some read it with مِنِّي understood, and the author doubts that. By kinaya: al-Aʿsha's يَا خَيْرَ مَنْ يَرْكَبُ الْمَطِيَّ وَلَا يَشْرَبُ كَأْسًا بِكَفِّ مَنْ بَخِلَا — «who drinks no cup from a miser's hand»: the hand would be his own were he stingy, so one man is shown as two. By a man addressing himself: al-Mutanabbi's لَا خَيْلَ عِنْدَكَ تُهْدِيهَا وَلَا مَالَ فَلْيُسْعِدِ النُّطْقُ إِنْ لَمْ تُسْعِدِ الْحَالُ — the «you» is the poet. WHAT THE ENGINE CLAIMS: it names the kind from the letter and the seats DabtEngine hands it — the لِ-fronted khabar with مِنْ, a name and an indefinite mubtada (min); a verb of asking carrying بِ + pronoun and a definite object (bi); a verb of motion with the speaker's بِي and a بِ-participle standing as its hal (bi of accompaniment); لَهُمْ فِيهَا with a construct mubtada that names a place (fi); a first-person shart-and-oath clause and then أَوْ with a verb and an indefinite doer (no letter); a vocative annexed to a relative that carries a negated second clause (kinaya); and the second-person pronouns in a poem spoken in the poet's own voice (self-address) — the last two are read as candidates and confirmed by the authored frame.",
  "tr": "TECRÎD أَنْ يُنْتَزَعَ مِنْ أَمْرٍ ذِي صِفَةٍ أَمْرٌ آخَرُ مِثْلُهُ فِيهَا مُبَالَغَةً لِكَمَالِهَا فِيهِ'dir — sıfatı OLAN bir şeyden, o sıfatta onun gibi BAŞKA bir şey çıkarılır, mübalağa için: sıfat ilkinde öyle tamdır ki ondan ikincisi alınabilir. Kısımları, çıkarışı taşıyan harfle söylenir. مِنْ ile: لِي مِنْ فُلَانٍ صَدِيقٌ حَمِيمٌ — dosttan bir dost. بِ ile: لَئِنْ سَأَلْتَ فُلَانًا لَتَسْأَلَنَّ بِهِ الْبَحْرَ — deniz, ONUNLA istenir. Maiyyet بِ'si ile: Zürrumme'nin وَشَوْهَاءَ تَعْدُو بِي إِلَى صَارِخِ الْوَغَى بِمُسْتَلْئِمٍ'i — kısrak «beni» zırhlı bir süvâri İLE taşır, o süvâri şairin kendisidir. فِي ile: لَهُمْ فِيهَا دَارُ الْخُلْدِ (Fussilet 28) — ateş ebedîlik yurdudur, yine de ondan, onun İÇİNDE bir yurt çıkarılır. Harfsiz: Katâde'nin وَلَئِنْ بَقِيتُ لَأَرْحَلَنَّ بِغَزْوَةٍ تَحْوِي الْغَنَائِمَ أَوْ يَمُوتَ كَرِيمُ'u — «yahut bir kerîm ölür»: kerîm, konuşan «ben»dir; kimi مِنِّي takdir eder, musannif buna itiraz eder. Kinâye ile: A'şâ'nın يَا خَيْرَ مَنْ يَرْكَبُ الْمَطِيَّ وَلَا يَشْرَبُ كَأْسًا بِكَفِّ مَنْ بَخِلَا'sı — «cimrinin eliyle kâse içmeyen»: el, cimri olsa kendi eli olurdu; böylece bir insan iki gösterilir. Kendine hitapla: Mütenebbî'nin لَا خَيْلَ عِنْدَكَ تُهْدِيهَا وَلَا مَالَ فَلْيُسْعِدِ النُّطْقُ إِنْ لَمْ تُسْعِدِ الْحَالُ'i — «sen» şairdir. MOTORUN İDDİASI: kısmı, harften ve DabtEngine'in verdiği koltuklardan adlandırır — مِنْ, isim ve nekre mübtedâ ile öne alınmış لِ haberi (min); بِ + zamir ve belirli mef'ûl taşıyan istemek fiili (bâ); konuşanın بِي'si ve hâl olan بِ'li ism-i fâil ile hareket fiili (maiyyet bâsı); yer adlandıran muzâf mübtedâ ile لَهُمْ فِيهَا (fî); birinci şahıs şart-yemin cümlesi, sonra أَوْ, fiil ve nekre fâil (harfsiz); nefiyli ikinci cümle taşıyan sılaya muzâf nidâ (kinâye); şairin kendi sesiyle söylenmiş şiirde ikinci şahıs zamirleri (kendine hitap) — son ikisi aday olarak okunur, yazılı çerçeveyle doğrulanır."},
 "examples": [
  {"ar": "لِي مِنْ فُلَانٍ صَدِيقٌ حَمِيمٌ", "en": "by min.", "tr": "min ile.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "لَئِنْ سَأَلْتَ فُلَانًا لَتَسْأَلَنَّ بِهِ الْبَحْرَ", "en": "by the ba.", "tr": "bâ ile.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "وَشَوْهَاءَ تَعْدُو بِي إِلَى صَارِخِ الْوَغَى * بِمُسْتَلْئِمٍ مِثْلِ الْفَنِيقِ الْمُدَجَّلِ", "en": "Dhu l-Rumma — by the ba of accompaniment.", "tr": "Zürrumme — maiyyet bâsı ile.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "لَهُمْ فِيهَا دَارُ الْخُلْدِ", "en": "41:28 — by fi.", "tr": "Fussilet 28 — fî ile.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "وَلَئِنْ بَقِيتُ لَأَرْحَلَنَّ بِغَزْوَةٍ * تَحْوِي الْغَنَائِمَ أَوْ يَمُوتَ كَرِيمُ", "en": "Qatada — with no letter.", "tr": "Katâde — harfsiz.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "يَا خَيْرَ مَنْ يَرْكَبُ الْمَطِيَّ وَلَا * يَشْرَبُ كَأْسًا بِكَفِّ مَنْ بَخِلَا", "en": "al-Aʿsha — by kinaya.", "tr": "A'şâ — kinâye ile.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "لَا خَيْلَ عِنْدَكَ تُهْدِيهَا وَلَا مَالَ * فَلْيُسْعِدِ النُّطْقُ إِنْ لَمْ تُسْعِدِ الْحَالُ", "en": "al-Mutanabbi — addressing himself.", "tr": "Mütenebbî — kendine hitapla.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"}],
 "commonMistakes": [
  {"wrong": "«لِي مِنْ فُلَانٍ صَدِيقٌ: min, «-den» demektir, dost falanın dostudur»",
   "right": "«Dost falanın KENDİSİDİR; min, ondan onun gibisini çıkaran tecrîd min'idir»",
   "why": {"en": "If the friend were someone else, no hyperbole would remain; the definition asks for the second to be LIKE the first, drawn out of it.", "tr": "Dost başkası olsa mübalağa kalmazdı; tarif, ikincinin ilkinden çıkarılan ONUN GİBİSİ olmasını ister."}}],
 "relatedNotes": ["kinaya", "mubalagha", "huruf-jarr", "la-nafiya-lil-jins", "vocative-munada", "ilm-al-badi"]}

ADD_EN = (" Chapter 63 (lines ~4170-4200, sahifa 144-145) carries the tajrid and its seven ways: the sayings of the Arabs (s3, s5), Dhu l-Rumma (s7), "
          "41:28 (s9), Qatada (s11), al-Aʿsha (s13) and al-Mutanabbi (s15) are the source's printed Arabic. s1 (the definition) and s2, s4, s6, s8, "
          "s10, s12, s14 (the kinds' headings) are RESTORED, NOT QUOTED: the source carries those steps only in its Ottoman-Turkish gloss, and the "
          "Arabic restores the matn's wording in the author's own idiom; each is marked «restored» in its translation. The examples carry `badi` frames "
          "of kind tajrid (the sub is the way; `word` the drawn-out figure, `companion` the mark it is drawn from).")
ADD_TR = (" Altmış üçüncü bâb (satır ~4170-4200, sahife 144-145) tecrîdi ve yedi yolunu taşır: Arapların sözleri (s3, s5), Zürrumme (s7), Fussilet 28 "
          "(s9), Katâde (s11), A'şâ (s13) ve Mütenebbî (s15) kaynağın bastığı Arapçadır. s1 (tarif) ile s2, s4, s6, s8, s10, s12, s14 (kısım başlıkları) "
          "ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda geri "
          "yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Örnekler tecrîd türünden `badi` çerçeveleri taşır (alt tür yoldur; `word` "
          "çıkarılan figür, `companion` çıkarıldığı alâmet).")
write_out(63, S, TITLE, ADD_EN, ADD_TR, "4170-4200", GLOSS_ADD, notes=(NOTE_D,),
          related=(("kinaya", ["tajrid"]), ("ilm-al-badi", ["tajrid"]), ("tarshih-wa-tajrid", ["tajrid"])))
report(63, S, GLOSS_ADD, (NOTE_D,))
