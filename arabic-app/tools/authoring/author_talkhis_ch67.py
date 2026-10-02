# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 67: TAWJIH, the HAZL by which earnest is meant, TAJAHUL AL-'ARIF (four aims), AL-QAWL BIL-MUJIB
(two kinds) and ITTIRAD. Source lines ~4345-4395 (sahifa 150-151).

  RESTORED (the source carries the step only in Turkish): s1 (tawjih's definition), s3 (al-Sakkaki on the mutashabihat), s4 (the
  hazl's heading), s6 (tajahul's definition and its four aims), s11, s12, s14 (the qawl bil-mujib's definition and two kinds), s16
  (ittirad's definition). The examples (s2, s5, s7-s10, s13, s15, s17) are the source's printed Arabic; the rhyme words are written
  by the itlaq (طَرِيفِ، نِسَاءُ، شِهَابِ) as the reader's rhyme rule expects. The Khariji lament is Layla bint Tarif's
  (the source: «the Khariji woman»); the tajahul's fourth bayt is the Majnun's.

  python3 tools/authoring/author_talkhis_ch67.py
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

W = "tawjih-wa-hazl"; J = "tajahul-al-arif"; Q = "qawl-bil-mujib"; T = "ittirad"
TITLE = {"ar": "التَّوْجِيهُ، وَالْهَزْلُ، وَتَجَاهُلُ الْعَارِفِ، وَالْقَوْلُ بِالْمُوجِبِ، وَالِاطِّرَادُ", "en": "Tawjih; Hazl; Tajahul al-ʿarif; al-Qawl bil-mujib; Ittirad", "tr": "Tevcih; Hezl; Tecâhül-i Ârif; Kavl bi'l-Mûcib; İttirâd"}
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
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def abi(tag, name, name_lex, name_ar, name_en, name_tr, punct=":"):
    return [tok("أَبِي","ab","noun",[tag, "five-nouns", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — one of the five nouns, majrur by its ya.", "«Ebû» — beş isimden, yâ ile mecrûr."),
            tok(name, name_lex, "noun", [tag, "idafa-definiteness"], name_ar, name_en, name_tr, punct=punct)]
def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)

# ----------- s1 — tawjih's definition (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is TAWJIH: to bring speech open to TWO different faces." + R_EN, "tr": "Onlardan biri TEVCİHTİR: sözü, farklı İKİ yüze ihtimalli olarak getirmek." + R_TR},
 "tokens": [
  minha(W),
  tok("التَّوْجِيهُ","tawjih","noun",[W, "mubtada-khabar", "masdar", "form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ وَجَّهَ.", "«the tawjih» — the delayed mubtada.", "«tevcih» — sona bırakılmış mübtedâ.", punct="،"),
  wahuwa(W),
  tok("إِيرَادُ","irad","noun",[W, "mubtada-khabar", "idafa-definiteness", "masdar", "form-iv-verbs"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ أَوْرَدَ.", "«bringing» — the khabar, annexed.", "«getirmek» — haber, muzâf."),
  tok("الْكَلَامِ","kalam","noun",[W, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«speech».", "«sözü»."),
  tok("مُحْتَمِلًا","muhtamil","noun",[W, "hal", "ism-fail", "form-viii-verbs"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلِ احْتَمَلَ.", "«open to» — a hal.", "«ihtimalli olarak» — hâl."),
  tok("لِوَجْهَيْنِ","wajh","noun",[W, "huruf-jarr", "al-muthanna"], "جَارٌّ وَمَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«to two faces» — a dual.", "«iki yüze» — tesniye.", segments=[seg("لِ","li","part"), seg("وَجْهَيْنِ","wajh","noun")]),
  tok("مُخْتَلِفَيْنِ","mukhtalif","noun",[W, "naat-sifa", "al-muthanna", "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ.", "«different» — a na't, dual.", "«farklı» — na't, tesniye.", punct=".")]})

# ----------- s2 — the one-eyed man: «would that his two eyes were equal»
S.append({"id": "s2", "translation": {
 "en": "As in the saying of one who said to a ONE-EYED man: «Would that his two eyes were EQUAL»." + R_EN,
 "tr": "Bir TEK GÖZLÜYE «Keşke iki gözü EŞİT olsa» diyenin sözü gibi." + R_TR},
 "tokens": [
  kaqawl(W),
  tok("مَنْ","man-mawsula","pron",[W, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«one who» — the mawsul, annexed to.", "«kimse» — mevsûl, muzâfun ileyh."),
  tok("قَالَ","qala","verb",[W, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«said» — the sila.", "«dedi» — sıla."),
  tok("لِأَعْوَرَ","awar","noun",[W, "huruf-jarr", "mamnu-min-sarf"], "جَارٌّ وَمَجْرُورٌ بِالْفَتْحَةِ — أَفْعَلُ الصِّفَةِ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to a one-eyed man» — the diptote afʿal.", "«bir tek gözlüye» — gayr-i munsarif ef'al.", segments=[seg("لِ","li","part"), seg("أَعْوَرَ","awar","noun")], punct=":"),
  tok("لَيْتَ","layta","part",[W, "inna-wa-akhawatuha", "insha-wa-tamanni"], "حَرْفُ تَمَنٍّ نَاسِخٌ.", "«would that».", "«keşke»."),
  tok("عَيْنَيْهِ","ayn-eye","noun",[W, "inna-wa-akhawatuha", "al-muthanna", "idafa-definiteness"], "اسْمُ لَيْتَ مَنْصُوبٌ بِالْيَاءِ — مُثَنًّى مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his two eyes» — layta's ism, a dual.", "«iki gözü» — leyte'nin ismi, tesniye.", segments=[seg("عَيْنَيْ","ayn-eye","noun"), seg("هِ","pron-3ms","pron")]),
  tok("سَوَاءٌ","sawa","noun",[W, "inna-wa-akhawatuha"], "خَبَرُ لَيْتَ مَرْفُوعٌ — سَوَاءٌ: مُسْتَوِيَتَانِ، يَسْتَوِي فِيهِ الْوَاحِدُ وَالْمُثَنَّى؛ يَحْتَمِلُ: لَيْتَهُمَا صَحِيحَتَانِ، وَلَيْتَهُمَا عَوْرَاوَانِ.", "«equal» — layta's khabar; both sound, or both blind.", "«eşit» — leyte'nin haberi; ikisi de sağlam yahut ikisi de kör.", punct=".")]})
S[-1]["badi"] = [{"kind": "tawjih", "word": ix(S[-1], "سَوَاءٌ")}]

# ----------- s3 — al-Sakkaki: the mutashabihat (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And with al-Sakkaki the MUTASHABIHAT of the Qur'an are of it, since they admit two faces." + R_EN,
 "tr": "Sekkâkî'ye göre, iki yüze ihtimalli olmaları itibariyle Kur'ân'ın MÜTEŞÂBİHÂTI da bundandır." + R_TR},
 "tokens": [
  wa_conj("وَعِنْدَ","inda","noun",[W, "maful-fih", "idafa-definiteness"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ، مُتَعَلِّقٌ بِالْخَبَرِ.", "«and with» — a zarf, annexed.", "«ve …-e göre» — zarf, muzâf."),
  tok("السَّكَّاكِيِّ","sakkaki","noun",[W, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Sakkaki».", "«Sekkâkî»."),
  tok("الْمُتَشَابِهَاتُ","mutashabih","noun",[W, "mubtada-khabar", "jam-muannath-salim", "ism-fail", "form-vi-verbs"], "مُبْتَدَأٌ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the mutashabihat» — the mubtada; a sound feminine plural.", "«müteşâbihât» — mübtedâ; cem-i müennes-i sâlim."),
  tok("مِنْهُ","min","part",[W, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«of it» — the khabar.", "«bundandır» — haber.", segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s4 — the hazl by which earnest is meant (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "Among them is the JEST by which EARNEST is meant." + R_EN, "tr": "Onlardan biri, kendisiyle CİDDİYET kastedilen ŞAKADIR." + R_TR},
 "tokens": [
  minha(W),
  tok("الْهَزْلُ","hazl","noun",[W, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the jest» — the delayed mubtada.", "«şaka» — sona bırakılmış mübtedâ."),
  tok("الَّذِي","alladhi","pron",[W, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ.", "«by which» — a mawsul as a na't.", "«ki onunla» — na't olan mevsûl."),
  tok("يُرَادُ","arada","verb",[W, "ism-mawsul", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is meant» — the sila.", "«kastedilir» — sıla."),
  tok("بِهِ","bi","part",[W, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«by it».", "«onunla».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْجِدُّ","jidd","noun",[W, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«earnest» — the naib al-fail.", "«ciddiyet» — nâib-i fâil.", punct=".")]})

# ----------- s5 — Abu Nuwas: the Tamimi and his lizard
S.append({"id": "s5", "translation": {
 "en": "As Abu Nuwas says: «When a Tamimi comes to you boasting, • say: leave that — HOW do you eat lizard?»." + R_EN,
 "tr": "Ebû Nüvâs'ın dediği gibi: «Bir Temîmli sana övünerek geldiğinde, • de ki: bırak bunu — keleri NASIL yersin?»." + R_TR},
 "tokens": [
  kaqawl(W), *abi(W, "نُوَاسٍ", "nuwas", "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو نُوَاسٍ: الْحَسَنُ بْنُ هَانِئٍ.", "«Nuwas» — Abu Nuwas, al-Hasan b. Hani'.", "«Nüvâs» — Ebû Nüvâs, Hasan b. Hâni'."),
  tok("إِذَا","idha","part",[W, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  tok("مَا","ma-zaida","part",[W, "anwa-ma"], "زَائِدَةٌ لِلتَّوْكِيدِ.", "«(ma)» — the redundant ma.", "«(mâ)» — zâid mâ."),
  tok("تَمِيمِيٌّ","tamimi","noun",[W, "fail", "ism-mansub", "hadhf-wa-taqdir"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ — إِذَا لَا يَلِيهَا إِلَّا الْفِعْلُ؛ نِسْبَةٌ إِلَى تَمِيمٍ.", "«a Tamimi» — the doer of a deleted verb the next one explains; the nisba to Tamim.", "«bir Temîmli» — sonrakinin açıkladığı hazfedilmiş fiilin fâili; Temîm'e nisbet."),
  tok("أَتَاكَ","ata","verb",[W, "maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ مُفَسِّرٌ، وَالْكَافُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«comes to you» — the explaining verb; its object the kaf.", "«sana gelir» — açıklayıcı fiil; mef'ûlü kâf.", segments=[seg("أَتَا","ata","verb"), seg("كَ","pron-2ms","pron")]),
  tok("مُفَاخِرًا","mufakhir","noun",[W, "hal", "ism-fail", "form-iii-verbs"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلِ فَاخَرَ.", "«boasting» — a hal.", "«övünerek» — hâl.", punct="*"),
  tok("فَقُلْ","qala","verb",[W, "imperative-amr", "jawab-al-talab"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَقُلْ فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«say» — the fa of idha's answer on a command.", "«de ki» — izâ'nın cevap fâsı emir üstünde.", segments=[seg("فَ","fa","conj"), seg("قُلْ","qala","verb")], punct=":"),
  tok("عَدِّ","adda-turn","verb",[W, "imperative-amr", "form-ii-verbs", "naqis-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ — عَدَّى عَنْهُ: تَجَاوَزَهُ.", "«leave» — the amr of ʿadda, its weak letter dropped: pass over it.", "«bırak» — addâ'nın emri, illet harfi düşmüş: geç onu."),
  tok("عَنْ","an","part",[W, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("ذَا","dha","pron",[W, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that».", "«bunu»."),
  tok("كَيْفَ","kayfa","noun",[W, "al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ — الْجِدُّ الْمُرَادُ: الْهِجَاءُ بِأَكْلِ الضَّبِّ.", "«how» — the interrogative as the fronted khabar; the earnest meant: the taunt of the lizard-eating.", "«nasıl» — öne alınmış haber olan soru ismi; kastedilen ciddiyet: keler yeme hicvi."),
  tok("أَكْلُكَ","akl","noun",[W, "mubtada-khabar", "idafa-definiteness", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your eating» — the delayed mubtada.", "«yemen» — sona bırakılmış mübtedâ.", segments=[seg("أَكْلُ","akl","noun"), seg("كَ","pron-2ms","pron")]),
  tok("لِلضَّبِّ","dabb","noun",[W, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — اللَّامُ لِلتَّقْوِيَةِ: مَفْعُولُ الْمَصْدَرِ؛ الضَّبُّ: دَابَّةٌ تَأْكُلُهَا الْأَعْرَابُ.", "«lizard» — the lam of strengthening on the masdar's object.", "«keleri» — masdarın mef'ûlü üstünde takviye lâmı.", segments=[seg("لِ","li","part"), seg("الضَّبِّ","dabb","noun")], punct=".")]})
S[-1]["badi"] = [{"kind": "hazl-jidd", "word": ix(S[-1], "كَيْفَ")}]

# ----------- s6 — tajahul's definition and its aims (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "Among them is TAJAHUL AL-ʿARIF, which al-Sakkaki named «driving the known in the course of the unknown» for a point: as REPROACH, HYPERBOLE in praise or in blame, and BEWILDERMENT in love." + R_EN,
 "tr": "Onlardan biri TECÂHÜL-İ ÂRİFTİR; Sekkâkî ona bir nükte için «malûmu meçhulün yolunda sevketmek» adını verdi: TEVBİH, medih yahut zemde MÜBALAĞA ve aşkta HAYRET gibi." + R_TR},
 "tokens": [
  minha(J),
  tok("تَجَاهُلُ","tajahul","noun",[J, "mubtada-khabar", "idafa-definiteness", "masdar", "form-vi-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ تَجَاهَلَ.", "«feigning ignorance of» — the masdar of tajahala.", "«bilmezlenmesi» — tecâhele'nin masdarı."),
  tok("الْعَارِفِ","arif-knower","noun",[J, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ عَرَفَ.", "«the knower».", "«ârifin».", punct="،"),
  wa_conj("وَسَمَّاهُ","samma","verb",[J, "mafulayn", "form-ii-verbs", "naqis-verbs"], "سَمَّى فِعْلٌ مَاضٍ يَنْصِبُ مَفْعُولَيْنِ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«and named it» — the pronoun its first object.", "«ve ona ad verdi» — zamir ilk mef'ûl.", pron=("هُ","pron-3ms")),
  tok("السَّكَّاكِيُّ","sakkaki","noun",[J, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Sakkaki».", "«Sekkâkî»."),
  tok("سَوْقَ","sawq","noun",[J, "maful-bihi", "idafa-definiteness", "masdar"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ مُضَافٌ — مَصْدَرُ سَاقَ.", "«driving» — the second object.", "«sevketmek» — ikinci mef'ûl."),
  tok("الْمَعْلُومِ","malum","noun",[J, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the known».", "«malûmu»."),
  tok("مَسَاقَ","masaq","noun",[J, "maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ مُضَافٌ — مَصْدَرٌ مِيمِيٌّ: سَاقَهُ مَسَاقَ غَيْرِهِ.", "«in the course of» — a maf'ul mutlaq; the mimi masdar.", "«yolunda» — mef'ûl-i mutlak; mîmî masdar."),
  tok("غَيْرِهِ","ghayr","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the unknown» — its other.", "«meçhulün».", segments=[seg("غَيْرِ","ghayr","noun"), seg("هِ","pron-3ms","pron")]),
  tok("لِنُكْتَةٍ","nukta","noun",[J, "huruf-jarr", "lam-taleel"], "جَارٌّ وَمَجْرُورٌ — لَامُ التَّعْلِيلِ.", "«for a point».", "«bir nükte için».", segments=[seg("لِ","li","part"), seg("نُكْتَةٍ","nukta","noun")], punct="،"),
  tok("كَالتَّوْبِيخِ","tawbikh","noun",[J, "huruf-jarr", "masdar", "form-ii-verbs"], "جَارٌّ وَمَجْرُورٌ — كَافُ التَّمْثِيلِ.", "«as reproach».", "«tevbih gibi».", segments=[seg("كَ","ka","part"), seg("التَّوْبِيخِ","tawbikh","noun")], punct="،"),
  wa_conj("وَالْمُبَالَغَةِ","mubalagha","noun",[J, "atf-nasaq"], "الْمُبَالَغَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and hyperbole».", "«ve mübalağa»."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْمَدْحِ","madh","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«praise».", "«medih»."),
  tok("أَوِ","aw","part",[J, "atf-nasaq"], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«yahut»."),
  tok("الذَّمِّ","dhamm","noun",[J, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«blame».", "«zem».", punct="،"),
  wa_conj("وَالتَّحَيُّرِ","tahayyur","noun",[J, "atf-nasaq", "masdar", "form-v-verbs"], "التَّحَيُّرِ مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ تَحَيَّرَ.", "«and bewilderment».", "«ve hayret»."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْحُبِّ","hubb","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«love».", "«aşk».", punct=".")]})

# ----------- s7 — Layla bint Tarif: the tree of the Khabur (reproach)
S.append({"id": "s7", "translation": {
 "en": "For reproach, as the Khariji woman says: «O tree of the Khabur, WHAT is it with you, in leaf — • as if you had not grieved for Ibn Tarif?»." + R_EN,
 "tr": "Tevbih için, Hâricî kadının dediği gibi: «Ey Hâbûr'un ağacı, SANA NE oluyor da yapraklısın — • sanki İbn Tarîf'e yas tutmamış gibisin?»." + R_TR},
 "tokens": [
  tok("فَالتَّوْبِيخُ","tawbikh","noun",[J, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالتَّوْبِيخُ مُبْتَدَأٌ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«the reproach» — the mubtada.", "«tevbih» — mübtedâ.", segments=[seg("فَ","fa","conj"), seg("التَّوْبِيخُ","tawbikh","noun")]),
  kaqawl(J),
  tok("الْخَارِجِيَّةِ","khariji","noun",[J, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَيْلَى بِنْتُ طَرِيفٍ الشَّيْبَانِيَّةُ، تَرْثِي أَخَاهَا الْوَلِيدَ.", "«the Khariji woman» — Layla bint Tarif, lamenting her brother al-Walid.", "«Hâricî kadın» — Leylâ bint Tarîf, kardeşi Velîd'e ağıt.", punct=":"),
  tok("أَيَا","aya-nida","part",[J, "vocative-munada"], "حَرْفُ نِدَاءٍ لِلْبَعِيدِ.", "«O» — the call to the far.", "«ey» — uzağa nidâ."),
  tok("شَجَرَ","shajar","noun",[J, "vocative-munada", "idafa-definiteness"], "مُنَادًى مَنْصُوبٌ مُضَافٌ.", "«tree of» — the munada, annexed.", "«ağacı» — münâdâ, muzâf."),
  tok("الْخَابُورِ","khabur","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَهْرٌ بِالْجَزِيرَةِ.", "«the Khabur» — a river of the Jazira.", "«Hâbûr» — Cezîre'de bir nehir."),
  tok("مَا","ma-istifham","pron",[J, "al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ — بِهِ يَتَجَاهَلُ الْعَارِفُ.", "«what» — the interrogative mubtada; the knower feigns not knowing by it.", "«ne» — soru ismi mübtedâ; ârif onunla bilmezlenir."),
  tok("لَكَ","lahu","part",[J, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«with you» — the khabar.", "«sana» — haber.", segments=[seg("لَ","li","part"), seg("كَ","pron-2ms","pron")]),
  tok("مُورِقًا","muriq","noun",[J, "hal", "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلِ أَوْرَقَ.", "«in leaf» — a hal.", "«yapraklı» — hâl.", punct="*"),
  tok("كَأَنَّكَ","kaanna","part",[J, "inna-wa-akhawatuha"], "حَرْفٌ نَاسِخٌ لِلتَّشْبِيهِ، وَالْكَافُ اسْمُهُ.", "«as if you».", "«sanki sen».", segments=[seg("كَأَنَّ","kaanna","part"), seg("كَ","pron-2ms","pron")]),
  tok("لَمْ","lam","part",[J, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me»."),
  tok("تَجْزَعْ","jazia","verb",[J, "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَالْجُمْلَةُ خَبَرُ كَأَنَّ.", "«grieved» — the clause is kaanna's khabar.", "«yas tutmadın» — cümle keenne'nin haberi."),
  tok("عَلَى","ala","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-e»."),
  tok("ابْنِ","ibn","noun",[J, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«Ibn».", "«İbn»."),
  tok("طَرِيفِ","tarif-alam","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — كَسْرَتُهُ مُطْلَقَةٌ لِلْقَافِيَةِ؛ الْوَلِيدُ بْنُ طَرِيفٍ الشَّيْبَانِيُّ.", "«Tarif» — its kasra prolonged for the rhyme; al-Walid b. Tarif.", "«Tarîf» — kesresi kafiye için uzatılmış; Velîd b. Tarîf.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajahul", "sub": "tawbikh", "receipt": "kaanna", "word": ix(S[-1], "مَا"), "companion": ix(S[-1], "كَأَنَّكَ")}]

# ----------- s8 — al-Buhturi: lightning, a lamp, or her smile (hyperbole in praise)
S.append({"id": "s8", "translation": {
 "en": "For hyperbole in praise, as al-Buhturi says: «IS IT the flash of a lightning that ran by night, OR the light of a lamp, • OR her smile in the sunlit view?»." + R_EN,
 "tr": "Medihte mübalağa için, Buhtürî'nin dediği gibi: «Gece geçen bir şimşeğin parıltısı MI, YOKSA bir kandilin ışığı mı, • YOKSA aydınlık görünüşteki tebessümü mü?»." + R_TR},
 "tokens": [
  wa_conj("وَالْمُبَالَغَةُ","mubalagha","noun",[J, "mubtada-khabar"], "الْمُبَالَغَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the hyperbole» — the mubtada.", "«ve mübalağa» — mübtedâ."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْمَدْحِ","madh","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«praise».", "«medih»."),
  kaqawl(J),
  tok("الْبُحْتُرِيِّ","buhturi","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Buhturi».", "«Buhtürî».", punct=":"),
  tok("أَلَمْعُ","lam-shine","noun",[J, "al-istifham", "mubtada-khabar", "idafa-definiteness", "adawat-al-tasawwur"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ مَعَ أَمْ: طَلَبُ التَّعْيِينِ — وَلَمْعُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَالْخَبَرُ مَحْذُوفٌ: هَذَا.", "«is it the flash of» — the hamza paired with am asks WHICH; the mubtada, its khabar unspoken.", "«parıltısı mı» — em ile eşleşen hemze HANGİSİ diye sorar; mübtedâ, haberi hazfedilmiş.",
      segments=[seg("أَ","hamza-istifham","part"), seg("لَمْعُ","lam-shine","noun")]),
  tok("بَرْقٍ","barq","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a lightning».", "«bir şimşeğin»."),
  tok("سَرَى","sara-night","verb",[J, "jumla-sifa", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ لِبَرْقٍ؛ سَرَى: سَارَ لَيْلًا.", "«that ran by night» — the clause a na't of the lightning.", "«gece geçen» — cümle şimşeğin na'tı."),
  tok("أَمْ","am","part",[J, "atf-nasaq", "al-istifham"], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ، مُعَادِلَةُ الْهَمْزَةِ.", "«or» — the joined am, the hamza's partner.", "«yoksa» — muttasıla em, hemzenin dengi."),
  tok("ضَوْءُ","daw","noun",[J, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ مُضَافٌ.", "«the light of» — joined.", "«ışığı» — ma'tûf."),
  tok("مِصْبَاحٍ","misbah","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَرُوضُ الْمَطْلَعِ مُصَرَّعَةٌ عَلَى الْقَافِيَةِ.", "«a lamp» — the opening bayt's first half rhymes with its close (tasriʿ).", "«bir kandilin» — matlaın arûzu kafiyeye tasrî' edilmiş.", punct="*"),
  tok("أَمِ","am","part",[J, "atf-nasaq", "al-istifham"], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«yoksa»."),
  tok("ابْتِسَامَتُهَا","ibtisama","noun",[J, "atf-nasaq", "idafa-definiteness", "masdar", "form-viii-verbs"], "مَعْطُوفٌ مَرْفُوعٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — مَصْدَرُ ابْتَسَمَ.", "«her smile» — joined.", "«tebessümü» — ma'tûf.", segments=[seg("ابْتِسَامَتُ","ibtisama","noun"), seg("هَا","pron-3fs","pron")]),
  tok("بِالْمَنْظَرِ","manzar","noun",[J, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«in the view».", "«görünüşte».", segments=[seg("بِ","bi","part"), seg("الْمَنْظَرِ","manzar","noun")]),
  tok("الضَّاحِي","dahi","noun",[J, "naat-sifa", "ism-fail", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ؛ الضَّاحِي: الْبَارِزُ لِلشَّمْسِ.", "«sunlit» — a manqus na't; open to the sun.", "«aydınlık» — mankûs na't; güneşe açık.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajahul", "sub": "mubalagha-madh", "receipt": "hamza-am", "word": ix(S[-1], "أَلَمْعُ"), "companion": ix(S[-1], "أَمْ")}]

# ----------- s9 — Zuhayr: are the Al Hisn men or women? (hyperbole in blame)
S.append({"id": "s9", "translation": {
 "en": "For hyperbole in blame, as Zuhayr says: «And I KNOW NOT — and I think I shall know — • are the house of Hisn a people, or women?»." + R_EN,
 "tr": "Zemde mübalağa için, Züheyr'in dediği gibi: «BİLMİYORUM — sanırım ileride bilirim — • Hısn ailesi erkek mi, yoksa kadın mı?»." + R_TR},
 "tokens": [
  wa_conj("وَالْمُبَالَغَةُ","mubalagha","noun",[J, "mubtada-khabar"], "الْمُبَالَغَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the hyperbole».", "«ve mübalağa»."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الذَّمِّ","dhamm","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«blame».", "«zem»."),
  kaqawl(J),
  tok("زُهَيْرٍ","zuhayr","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — زُهَيْرُ بْنُ أَبِي سُلْمَى.", "«Zuhayr» — Zuhayr b. Abi Sulma.", "«Züheyr» — Züheyr b. Ebî Sülmâ.", punct=":"),
  wa_conj("وَمَا","ma-nafiya","part",[J, "anwa-ma"], "مَا نَافِيَةٌ.", "«and not».", "«ve …-miyorum»."),
  tok("أَدْرِي","dara","verb",[J, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — بِهِ يَتَجَاهَلُ الْعَارِفُ.", "«I know» — the knower feigns not knowing by it.", "«biliyorum» — ârif onunla bilmezlenir."),
  wa_conj("وَسَوْفَ","sawfa","part",[J, "jumla-mutarida"], "سَوْفَ حَرْفُ اسْتِقْبَالٍ — وَالْجُمْلَةُ مُعْتَرِضَةٌ.", "«and I shall» — a parenthetical.", "«ve ileride» — mu'terize cümle."),
  tok("إِخَالُ","khala-think","verb",[J, "mudari-marfu", "zanna-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مِنْ أَخَوَاتِ ظَنَّ — كُسِرَتْ هَمْزَتُهُ عَلَى الشُّذُوذِ قِيَاسًا، وَهُوَ الْفَصِيحُ اسْتِعْمَالًا.", "«I think» — a sister of zanna; its hamza kasra'd against the rule and eloquent by usage.", "«sanırım» — zanne'nin kardeşi; hemzesi kıyasa aykırı meksûr, kullanımca fasih."),
  tok("أَدْرِي","dara","verb",[J, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ سَدَّتْ مَسَدَّ مَفْعُولَيْ إِخَالُ.", "«I shall know» — the clause fills the two objects of ikhalu.", "«bileceğim» — cümle ihâlü'nün iki mef'ûlünün yerini tutar.", punct="*"),
  tok("أَقَوْمٌ","qawm","noun",[J, "al-istifham", "mubtada-khabar", "adawat-al-tasawwur"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ مَعَ أَمْ، وَقَوْمٌ خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«a people?» — the hamza with am; the fronted khabar.", "«erkek mi?» — em ile hemze; öne alınmış haber.", segments=[seg("أَ","hamza-istifham","part"), seg("قَوْمٌ","qawm","noun")]),
  tok("آلُ","al-family","noun",[J, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ.", "«the house of» — the delayed mubtada.", "«ailesi» — sona bırakılmış mübtedâ."),
  tok("حِصْنٍ","hisn-alam","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حِصْنُ بْنُ حُذَيْفَةَ الْفَزَارِيُّ.", "«Hisn» — Hisn b. Hudhayfa al-Fazari.", "«Hısn» — Hısn b. Huzeyfe el-Fezârî."),
  tok("أَمْ","am","part",[J, "atf-nasaq", "al-istifham"], "أَمِ الْمُتَّصِلَةُ.", "«or».", "«yoksa»."),
  tok("نِسَاءُ","nisa","noun",[J, "atf-nasaq"], "مَعْطُوفٌ عَلَى قَوْمٌ مَرْفُوعٌ — ضَمَّتُهُ مُطْلَقَةٌ لِلْقَافِيَةِ.", "«women» — joined; its damma prolonged.", "«kadın» — ma'tûf; zammesi uzatılmış.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajahul", "sub": "mubalagha-dhamm", "receipt": "ma-adri", "word": ix(S[-1], "أَدْرِي"), "companion": ix(S[-1], "أَقَوْمٌ")}]

# ----------- s10 — the Majnun: is my Layla one of you, gazelles? (bewilderment in love)
S.append({"id": "s10", "translation": {
 "en": "For bewilderment in love, as the Majnun of ʿAmir says: «By God, O gazelles of the plain, tell us: • is MY LAYLA one of you, or is Layla of humankind?»." + R_EN,
 "tr": "Aşkta hayret için, Âmirî Mecnûn'un dediği gibi: «Allah için, ey düzlüğün ceylanları, söyleyin bize: • LEYLÂM sizden mi, yoksa Leylâ insandan mı?»." + R_TR},
 "tokens": [
  wa_conj("وَالتَّحَيُّرُ","tahayyur","noun",[J, "mubtada-khabar"], "التَّحَيُّرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the bewilderment».", "«ve hayret»."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْحُبِّ","hubb","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«love».", "«aşk»."),
  kaqawl(J),
  tok("الْمَجْنُونِ","majnun-alam","noun",[J, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — قَيْسُ بْنُ الْمُلَوَّحِ، مَجْنُونُ لَيْلَى.", "«the Majnun» — Qays b. al-Mulawwah.", "«Mecnûn» — Kays b. Mülevvah."),
  tok("الْعَامِرِيِّ","amiri","noun",[J, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — نِسْبَةٌ إِلَى بَنِي عَامِرٍ.", "«of ʿAmir» — the nisba to Banu ʿAmir.", "«Âmirî» — Benî Âmir'e nisbet.", punct=":"),
  tok("بِاللهِ","allah","noun",[J, "huruf-jarr"], "الْبَاءُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by God» — the ba of oath.", "«Allah için» — yemin bâsı.", segments=[seg("بِ","bi","part"), seg("اللهِ","allah","noun")]),
  tok("يَا","ya","part",[J, "vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("ظَبَيَاتِ","zabya","noun",[J, "vocative-munada", "idafa-definiteness", "jam-muannath-salim"], "مُنَادًى مَنْصُوبٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ.", "«gazelles of» — the munada, a sound feminine plural.", "«ceylanları» — münâdâ, cem-i müennes-i sâlim."),
  tok("الْقَاعِ","qa","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْقَاعُ: الْأَرْضُ السَّهْلَةُ.", "«the plain».", "«düzlüğün»."),
  tok("قُلْنَ","qala","verb",[J, "imperative-amr", "hollow-verbs", "fail"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنُونُ النِّسْوَةِ فَاعِلٌ.", "«tell» — the command to the women; the nun is the doer.", "«söyleyin» — kadınlara emir; nûn fâil."),
  tok("لَنَا","lahu","part",[J, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«us».", "«bize».", segments=[seg("لَ","li","part"), seg("نَا","pron-1p","pron")], punct="*"),
  tok("لَيْلَايَ","layla-alam","noun",[J, "mubtada-khabar", "idafa-definiteness", "ya-al-mutakallim"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ مَفْتُوحَةٌ بَعْدَ الْأَلِفِ — بِهِ يَتَحَيَّرُ الْعَاشِقُ.", "«my Layla» — the mubtada; my ya opened after the alif; the lover's bewilderment.", "«Leylâm» — mübtedâ; elif ardında yâ meftûh; âşığın hayreti.", segments=[seg("لَيْلَا","layla-alam","noun"), seg("يَ","pron-1s","pron")]),
  tok("مِنْكُنَّ","min","part",[J, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«one of you» — the khabar.", "«sizden» — haber.", segments=[seg("مِنْ","min","part"), seg("كُنَّ","pron-2fp","pron")]),
  tok("أَمْ","am","part",[J, "atf-nasaq", "al-istifham"], "أَمِ الْمُتَّصِلَةُ — وَالْهَمْزَةُ مُقَدَّرَةٌ قَبْلَ لَيْلَايَ.", "«or» — the joined am; the hamza understood before «my Layla».", "«yoksa» — muttasıla em; hemze «Leylâm»dan önce mukadder."),
  tok("لَيْلَى","layla-alam","noun",[J, "mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«Layla» — a mubtada.", "«Leylâ» — mübtedâ."),
  tok("مِنَ","min","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("الْبَشَرِ","bashar","noun",[J, "huruf-jarr", "mubtada-khabar"], "مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«humankind» — the phrase is the khabar.", "«insan» — câr-mecrûr haber.", punct=".")]})
S[-1]["badi"] = [{"kind": "tajahul", "sub": "hayra", "receipt": "am", "word": ix(S[-1], "لَيْلَايَ"), "companion": ix(S[-1], "أَمْ")}]

# ----------- s11 — al-qawl bil-mujib: two kinds (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "Among them is AL-QAWL BIL-MUJIB, and it is of two kinds." + R_EN, "tr": "Onlardan biri KAVL Bİ'L-MÛCİBDİR; iki kısımdır." + R_TR},
 "tokens": [
  minha(Q),
  tok("الْقَوْلُ","qawl","noun",[Q, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«speaking» — the delayed mubtada.", "«söz» — sona bırakılmış mübtedâ."),
  tok("بِالْمُوجِبِ","mujib","noun",[Q, "huruf-jarr", "ism-fail", "form-iv-verbs"], "جَارٌّ وَمَجْرُورٌ — الْمُوجِبُ: مَا يَقْتَضِيهِ كَلَامُ الْغَيْرِ.", "«by its warrant» — the mujib: what the other's words entail.", "«mûcibiyle» — mûcib: muhatabın sözünün gerektirdiği.", segments=[seg("بِ","bi","part"), seg("الْمُوجِبِ","mujib","noun")], punct="،"),
  wahuwa(Q),
  tok("ضَرْبَانِ","darb","noun",[Q, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds».", "«iki kısım».", punct=".")]})

# ----------- s12 — the first kind (RESTORED matn)
S.append({"id": "s12", "translation": {
 "en": "One: that a quality occur in another's speech as a KINAYA for something a ruling has been affirmed of, and you affirm it of something else — without touching whether that ruling holds of it or not." + R_EN,
 "tr": "Biri: muhatabın sözünde, kendisine hüküm ispat edilmiş bir şeyden KİNAYE olan bir sıfatın vâki olması ve senin o sıfatı, o hükmün ona ait olup olmadığına dokunmaksızın, başkasına ispat etmen." + R_TR},
 "tokens": [
  tok("أَحَدُهُمَا","ahad","noun",[Q, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them» — the mubtada.", "«biri» — mübtedâ.", segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")]),
  an_masd(Q),
  tok("تَقَعَ","waqaa","verb",[Q, "an-masdariyya", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — مِثَالٌ، سَقَطَتْ وَاوُهُ.", "«occur» — a mithal verb, its waw dropped.", "«vâki olması» — misâl fiil, vâvı düşmüş."),
  tok("صِفَةٌ","sifa","noun",[Q, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a quality» — the doer.", "«bir sıfat» — fâil."),
  tok("فِي","fi","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("كَلَامِ","kalam","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the speech of».", "«sözünde»."),
  tok("الْغَيْرِ","ghayr","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْغَيْرُ: الْمُخَاطَبُ أَوْ سِوَاهُ.", "«another».", "«muhatabın»."),
  tok("كِنَايَةً","kinaya","noun",[Q, "hal", "masdar"], "حَالٌ مَنْصُوبٌ — أَيْ كَانِيَةً.", "«as a kinaya» — a hal.", "«kinaye olarak» — hâl."),
  tok("عَنْ","an","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  tok("شَيْءٍ","shay","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«something».", "«bir şey»."),
  tok("أُثْبِتَ","athbata","verb",[Q, "jumla-sifa", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ لِشَيْءٍ.", "«has been affirmed» — the clause a na't of «something».", "«ispat edilmiş» — cümle «şey»in na'tı."),
  tok("لَهُ","lahu","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of it».", "«ona».", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("حُكْمٌ","hukm","noun",[Q, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a ruling» — the naib al-fail.", "«bir hüküm» — nâib-i fâil.", punct="،"),
  tok("فَتُثْبِتَهَا","athbata","verb",[Q, "atf-nasaq", "an-masdariyya", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَتُثْبِتَ مُضَارِعٌ مَعْطُوفٌ عَلَى الْمَنْصُوبِ، وَهَا مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and you affirm it» — joined to the nasb; the pronoun its object.", "«ve sen onu ispat edersin» — mansûba ma'tûf; zamir mef'ûl.", segments=[seg("فَ","fa","conj"), seg("تُثْبِتَ","athbata","verb"), seg("هَا","pron-3fs","pron")]),
  tok("لِغَيْرِهِ","ghayr","noun",[Q, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of something else».", "«başkasına».", segments=[seg("لِ","li","part"), seg("غَيْرِ","ghayr","noun"), seg("هِ","pron-3ms","pron")]),
  tok("مِنْ","min","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«without».", "«-sızın»."),
  tok("غَيْرِ","ghayr","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«(other than)».", "«(gayr)»."),
  tok("تَعَرُّضٍ","taarrud","noun",[Q, "idafa-definiteness", "masdar", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَعَرَّضَ.", "«touching».", "«dokunma»."),
  tok("لِثُبُوتِ","thubut","noun",[Q, "huruf-jarr", "idafa-definiteness", "masdar"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«whether … holds».", "«sabit olmasına».", segments=[seg("لِ","li","part"), seg("ثُبُوتِ","thubut","noun")]),
  tok("ذَلِكَ","dhalika","pron",[Q, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that».", "«o»."),
  tok("الْحُكْمِ","hukm","noun",[Q, "badal"], "بَدَلٌ مَجْرُورٌ.", "«ruling» — a badal.", "«hükmün» — bedel."),
  tok("لَهُ","lahu","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of it».", "«ona».", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("أَوْ","aw","part",[Q, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("نَفْيِهِ","nafy","noun",[Q, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ عَلَى ثُبُوتِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its denial».", "«nefyine».", segments=[seg("نَفْيِ","nafy","noun"), seg("هِ","pron-3ms","pron")]),
  tok("عَنْهُ","an","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of it».", "«ondan».", segments=[seg("عَنْ","an","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s13 — 63:8: the mightier will drive out the meaner
S.append({"id": "s13", "translation": {
 "en": "As in His saying, exalted is He: «They say: if we return to Medina, the MIGHTIER will surely drive out the meaner from it — and to God belongs the MIGHT, and to His Messenger and to the believers» (63:8)." + R_EN,
 "tr": "Allah Teâlâ'nın şu sözü gibi: «Diyorlar ki: Medine'ye dönersek, DAHA ÜSTÜN olan daha alçak olanı oradan mutlaka çıkaracak — hâlbuki İZZET Allah'ındır, Resulünün ve müminlerindir» (Münâfikûn 8)." + R_TR},
 "tokens": [
  kaqh(Q, punct=None), taala(Q),
  tok("يَقُولُونَ","qala","verb",[Q, "mudari-marfu", "afal-khamsa", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — الْمُنَافِقُونَ.", "«they say» — the hypocrites; raf by the nun.", "«diyorlar» — münafıklar; nûnun sübûtuyla merfû."),
  tok("لَئِنْ","lain","part",[Q, "in-shartiyya"], "اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَإِنْ شَرْطِيَّةٌ.", "«if» — the oath-paving lam on the conditional.", "«-sek» — yemine zemin lâmı şart edatı üstünde."),
  tok("رَجَعْنَا","rajaa","verb",[Q, "in-shartiyya", "fail"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَنَا فَاعِلٌ.", "«we return» — the shart; na the doer.", "«dönersek» — şart fiili; nâ fâil.", segments=[seg("رَجَعْ","rajaa","verb"), seg("نَا","pron-1p","pron")]),
  tok("إِلَى","ila","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمَدِينَةِ","madina","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«Medina».", "«Medine»."),
  tok("لَيُخْرِجَنَّ","akhraja","verb",[Q, "nun-tawkid", "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَيُخْرِجَنَّ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ — جَوَابُ الْقَسَمِ سَادٌّ مَسَدَّ جَوَابِ الشَّرْطِ.", "«will surely drive out» — the oath's answer, on the heavy nun.", "«mutlaka çıkaracak» — yeminin cevabı, şeddeli nûn üstünde.", segments=[seg("لَ","li","part"), seg("يُخْرِجَنَّ","akhraja","verb")]),
  tok("الْأَعَزُّ","aazz","noun",[Q, "fail", "ism-tafdil"], "فَاعِلٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ؛ الصِّفَةُ الْوَاقِعَةُ فِي كَلَامِ الْمُنَافِقِينَ كِنَايَةً عَنْ أَنْفُسِهِمْ.", "«the mightier» — the doer; the quality in the hypocrites' words, a kinaya for themselves.", "«daha üstün» — fâil; münafıkların sözündeki sıfat, kendilerine kinaye."),
  tok("مِنْهَا","min","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«from it».", "«oradan».", segments=[seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("الْأَذَلَّ","adhall","noun",[Q, "maful-bihi", "ism-tafdil"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the meaner» — the object.", "«daha alçağı» — mef'ûl."),
  wa_conj("وَلِلَّهِ","allah","noun",[Q, "huruf-jarr", "mubtada-khabar"], "لِلَّهِ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — الْوَاوُ لِلْحَالِ أَوِ الِاسْتِئْنَافِ.", "«and to God» — the fronted khabar.", "«hâlbuki Allah'ındır» — öne alınmış haber.", pron=None),
  tok("الْعِزَّةُ","izza","noun",[Q, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — الصِّفَةُ أُثْبِتَتْ لِغَيْرِهِمْ بِلَا تَعَرُّضٍ لِلْحُكْمِ.", "«the might» — the delayed mubtada; the quality affirmed of others, the ruling untouched.", "«izzet» — sona bırakılmış mübtedâ; sıfat başkalarına ispat, hükme dokunulmadı."),
  wa_conj("وَلِرَسُولِهِ","rasul","noun",[Q, "atf-nasaq", "huruf-jarr", "idafa-definiteness"], "لِرَسُولِهِ جَارٌّ وَمَجْرُورٌ مَعْطُوفٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and to His Messenger».", "«ve Resulünün».", pron=("هِ","pron-3ms")),
  wa_conj("وَلِلْمُؤْمِنِينَ","mumin","noun",[Q, "atf-nasaq", "huruf-jarr", "jam-mudhakkar-salim"], "لِلْمُؤْمِنِينَ جَارٌّ وَمَجْرُورٌ بِالْيَاءِ مَعْطُوفٌ.", "«and to the believers».", "«ve müminlerindir».", punct=".")]})
S[-1]["badi"] = [{"kind": "qawl-mujib", "sub": "sifa-kinaya", "word": ix(S[-1], "الْعِزَّةُ"), "companion": ix(S[-1], "الْأَعَزُّ")}]

# ----------- s14 — the second kind (RESTORED matn)
S.append({"id": "s14", "translation": {
 "en": "The second: carrying a word that occurred in another's speech AGAINST his intent, to a sense it admits, by mentioning what it attaches to." + R_EN,
 "tr": "İkincisi: muhatabın sözünde vâki olan bir lafzı, müteallikini zikrederek, ihtimalli olduğu mânâlardan onun muradının HİLÂFINA yormaktır." + R_TR},
 "tokens": [
  wa_conj("وَالثَّانِي","thani","noun",[Q, "mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second» — the mubtada.", "«ve ikincisi» — mübtedâ."),
  tok("حَمْلُ","haml","noun",[Q, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ حَمَلَ.", "«carrying» — the khabar.", "«yormak» — haber."),
  tok("لَفْظٍ","lafz","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a word».", "«bir lafzı»."),
  tok("وَقَعَ","waqaa","verb",[Q, "jumla-sifa", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ لِلَفْظٍ.", "«that occurred» — a na't clause.", "«vâki olan» — na't cümlesi."),
  tok("فِي","fi","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("كَلَامِ","kalam","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the speech of».", "«sözünde»."),
  tok("الْغَيْرِ","ghayr","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«another».", "«muhatabın»."),
  tok("عَلَى","ala","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«against».", "«-e»."),
  tok("خِلَافِ","khilaf","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the contrary of».", "«hilâfına»."),
  tok("مُرَادِهِ","murad","noun",[Q, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his intent».", "«muradının».", segments=[seg("مُرَادِ","murad","noun"), seg("هِ","pron-3ms","pron")]),
  tok("مِمَّا","ma-mawsula","pron",[Q, "huruf-jarr", "ism-mawsul"], "مِنْ جَارَّةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«among what».", "«-lardan».", segments=[seg("مِنْ","min","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يَحْتَمِلُهُ","ihtamala","verb",[Q, "ism-mawsul", "mudari-marfu", "form-viii-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«it admits» — the sila.", "«ihtimalli olduğu» — sıla.", segments=[seg("يَحْتَمِلُ","ihtamala","verb"), seg("هُ","pron-3ms","pron")]),
  tok("بِذِكْرِ","dhikr","noun",[Q, "huruf-jarr", "idafa-definiteness", "masdar"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«by mentioning».", "«zikrederek».", segments=[seg("بِ","bi","part"), seg("ذِكْرِ","dhikr","noun")]),
  tok("مُتَعَلِّقِهِ","mutaalliq","noun",[Q, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what it attaches to».", "«müteallikini».", segments=[seg("مُتَعَلِّقِ","mutaalliq","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s15 — Ibn al-Hajjaj: «I have burdened you» — «you have burdened my shoulders with favours»
S.append({"id": "s15", "translation": {
 "en": "As Ibn al-Hajjaj says: «I said: I have BURDENED you, coming so often. • He said: you have BURDENED my shoulders — with favours»." + R_EN,
 "tr": "İbnü'l-Haccâc'ın dediği gibi: «Dedim: sık sık gelmekle sana AĞIRLIK verdim. • Dedi: omzuma AĞIRLIK verdin — nimetlerle»." + R_TR},
 "tokens": [
  kaqawl(Q),
  tok("ابْنِ","ibn","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«Ibn».", "«İbn»."),
  tok("الْحَجَّاجِ","hajjaj-alam","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ابْنُ الْحَجَّاجِ الْبَغْدَادِيُّ الشَّاعِرُ.", "«al-Hajjaj» — Ibn al-Hajjaj the Baghdadi poet.", "«Haccâc» — Bağdatlı şair İbnü'l-Haccâc.", punct=":"),
  tok("قُلْتُ","qala","verb",[Q, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I said».", "«dedim».", segments=[seg("قُلْ","qala","verb"), seg("تُ","pron-1s","pron")], punct=":"),
  tok("ثَقَّلْتُ","thaqqala","verb",[Q, "fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — ثَقَّلْتُ عَلَيْكَ: أَتْعَبْتُكَ.", "«I have burdened» — the poet's word, meant as «I wearied you».", "«ağırlık verdim» — şairin sözü, «seni yordum» mânâsında.", segments=[seg("ثَقَّلْ","thaqqala","verb"), seg("تُ","pron-1s","pron")]),
  tok("إِذْ","idh","noun",[Q, "maful-fih"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ.", "«when».", "«-diğimde»."),
  tok("أَتَيْتُ","ata","verb",[Q, "fail", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I came».", "«geldim».", segments=[seg("أَتَيْ","ata","verb"), seg("تُ","pron-1s","pron")]),
  tok("مِرَارًا","mirar","noun",[Q, "maful-fih", "jam-taksir"], "ظَرْفٌ مَنْصُوبٌ — جَمْعُ مَرَّةٍ: مَرَّاتٍ كَثِيرَةً.", "«so often» — times over.", "«sık sık» — nice kez.", punct="*"),
  tok("قَالَ","qala","verb",[Q, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْمَمْدُوحُ.", "«he said» — the praised.", "«dedi» — memdûh.", punct=":"),
  tok("ثَقَّلْتَ","thaqqala","verb",[Q, "fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — اللَّفْظُ نَفْسُهُ حُمِلَ عَلَى خِلَافِ مُرَادِ الشَّاعِرِ بِذِكْرِ مُتَعَلِّقِهِ.", "«you have burdened» — the same word, turned against the poet's intent by naming what it attaches to.", "«ağırlık verdin» — aynı lafız, mütealliki anılarak şairin muradının hilâfına çevrilmiş.", segments=[seg("ثَقَّلْ","thaqqala","verb"), seg("تَ","pron-2ms","pron")]),
  tok("كَاهِلِي","kahil","noun",[Q, "maful-bihi", "idafa-definiteness", "ya-al-mutakallim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — الْكَاهِلُ: مَا بَيْنَ الْكَتِفَيْنِ.", "«my shoulders» — the object; the kahil: between the shoulder-blades.", "«omzumu» — mef'ûl; kâhil: iki kürek arası.", segments=[seg("كَاهِلِ","kahil","noun"), seg("ي","pron-1s","pron")]),
  tok("بِالْأَيَادِي","ayadi","noun",[Q, "huruf-jarr", "jam-taksir", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — الْأَيَادِي: النِّعَمُ، جَمْعُ الْجَمْعِ لِيَدٍ؛ وَهُوَ الْمُتَعَلِّقُ الْمَذْكُورُ.", "«with favours» — the ayadi: the mentioned attachment that turns the word.", "«nimetlerle» — eyâdî: lafzı çeviren zikredilmiş müteallik.", segments=[seg("بِ","bi","part"), seg("الْأَيَادِي","ayadi","noun")], punct=".")]})
S[-1]["badi"] = [{"kind": "qawl-mujib", "sub": "lafz-mushtarak", "word": ix(S[-1], "ثَقَّلْتَ"), "companion": ix(S[-1], "ثَقَّلْتُ")}]

# ----------- s16 — ittirad's definition (RESTORED matn)
S.append({"id": "s16", "translation": {
 "en": "Among them is ITTIRAD: to bring the name of the praised and the names of his FATHERS in the order of birth, with no strain." + R_EN,
 "tr": "Onlardan biri İTTİRÂDDIR: memdûhun adını ve BABALARININ adlarını, zorlanmadan doğum sırası üzere getirmek." + R_TR},
 "tokens": [
  minha(T),
  tok("الِاطِّرَادُ","ittirad","noun",[T, "mubtada-khabar", "masdar", "form-viii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ اطَّرَدَ: تَتَابَعَ؛ أَصْلُهُ اطْتَرَدَ، قُلِبَتِ التَّاءُ طَاءً وَأُدْغِمَتْ.", "«the ittirad» — the masdar of ittarada: to run on; its ta turned into a ta' and merged.", "«ittirâd» — ittarade'nin masdarı: ardarda gitmek; tâsı tıya dönüp idgam edilmiş.", punct="،"),
  wahuwa(T),
  an_masd(T),
  tok("يَأْتِيَ","ata","verb",[T, "an-masdariyya", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: الشَّاعِرُ.", "«bring» — nasb by an.", "«getirmesi» — en ile mansûb."),
  tok("بِاسْمِ","ism","noun",[T, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«the name of».", "«adını».", segments=[seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("الْمَمْدُوحِ","mamduh","noun",[T, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the praised».", "«memdûhun»."),
  wa_conj("وَأَسْمَاءِ","ism","noun",[T, "atf-nasaq", "idafa-definiteness", "jam-taksir"], "أَسْمَاءِ مَعْطُوفٌ مَجْرُورٌ مُضَافٌ — جَمْعُ اسْمٍ.", "«and the names of».", "«ve adlarını»."),
  tok("آبَائِهِ","ab","noun",[T, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ أَبٍ.", "«his fathers».", "«babalarının».", segments=[seg("آبَائِ","ab","noun"), seg("هِ","pron-3ms","pron")]),
  tok("عَلَى","ala","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  tok("تَرْتِيبِ","tartib","noun",[T, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the order of».", "«sırası»."),
  tok("الْوِلَادَةِ","wilada","noun",[T, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«birth».", "«doğum»."),
  tok("مِنْ","min","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«with».", "«-dan»."),
  tok("غَيْرِ","ghayr","noun",[T, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«no».", "«(gayr)»."),
  tok("تَكَلُّفٍ","takalluf","noun",[T, "idafa-definiteness", "masdar", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَكَلَّفَ.", "«strain».", "«zorlanma».", punct=".")]})

# ----------- s17 — Rabiʿa: ʿUtayba b. al-Harith b. Shihab
S.append({"id": "s17", "translation": {
 "en": "As Rabiʿa says: «If they kill you, you have already torn down their thrones • with ʿUTAYBA son of AL-HARITH son of SHIHAB»." + R_EN,
 "tr": "Rebîa'nın dediği gibi: «Seni öldürseler de, sen onların tahtlarını • ŞİHÂB oğlu HÂRİS oğlu UTEYBE ile çoktan yıktın»." + R_TR},
 "tokens": [
  kaqawl(T),
  tok("رَبِيعَةَ","rabia-alam","noun",[T, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — رَبِيعَةُ بْنُ مَقْرُومٍ الضَّبِّيُّ.", "«Rabiʿa» — Rabiʿa b. Maqrum al-Dabbi.", "«Rebîa» — Rebîa b. Makrûm ed-Dabbî.", punct=":"),
  tok("إِنْ","in-shartiyya","part",[T, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-se»."),
  tok("يَقْتُلُوكَ","qatala","verb",[T, "in-shartiyya", "afal-khamsa", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ فِعْلُ الشَّرْطِ، وَالْوَاوُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«they kill you» — the shart; jussive by dropping the nun.", "«seni öldürürlerse» — şart fiili; nûnun düşmesiyle meczûm.", segments=[seg("يَقْتُلُو","qatala","verb"), seg("كَ","pron-2ms","pron")]),
  tok("فَقَدْ","qad","part",[T, "in-shartiyya", "qad-harf"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَقَدْ لِلتَّحْقِيقِ.", "«then already» — the fa of the answer on qad.", "«o hâlde çoktan» — cevap fâsı kad üstünde.", segments=[seg("فَ","fa","conj"), seg("قَدْ","qad","part")]),
  tok("ثَلَلْتَ","thalla","verb",[T, "in-shartiyya", "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ مُضَاعَفٌ فُكَّ إِدْغَامُهُ لِاتِّصَالِهِ بِالتَّاءِ، وَالتَّاءُ فَاعِلٌ — ثَلَّ الْعَرْشَ: هَدَمَهُ.", "«you have torn down» — the doubled verb undone before the ta; thalla the throne: to bring it down.", "«yıktın» — tâdan önce idgamı çözülmüş muzâaf; selle'l-arş: tahtı yıkmak.", segments=[seg("ثَلَلْ","thalla","verb"), seg("تَ","pron-2ms","pron")]),
  tok("عُرُوشَهُمْ","arsh","noun",[T, "maful-bihi", "idafa-definiteness", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ عَرْشٍ: الْمُلْكُ.", "«their thrones» — the object; their kingship.", "«tahtlarını» — mef'ûl; saltanatlarını.", segments=[seg("عُرُوشَ","arsh","noun"), seg("هُمْ","pron-3mp","pron")], punct="*"),
  tok("بِعُتَيْبَةَ","utayba-alam","noun",[T, "huruf-jarr", "mamnu-min-sarf"], "جَارٌّ وَمَجْرُورٌ بِالْفَتْحَةِ — عَلَمٌ مُؤَنَّثٌ بِالتَّاءِ، مَمْنُوعٌ مِنَ الصَّرْفِ؛ الْبَاءُ لِلسَّبَبِيَّةِ.", "«with ʿUtayba» — a diptote name; the ba of cause.", "«Uteybe ile» — gayr-i munsarif alem; sebep bâsı.", segments=[seg("بِ","bi","part"), seg("عُتَيْبَةَ","utayba-alam","noun")]),
  tok("بْنِ","ibn","noun",[T, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("الْحَارِثِ","harith-alam","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«al-Harith».", "«Hâris»."),
  tok("بْنِ","ibn","noun",[T, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("شِهَابِ","shihab-alam","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — كَسْرَتُهُ مُطْلَقَةٌ لِلْقَافِيَةِ.", "«Shihab» — its kasra prolonged.", "«Şihâb» — kesresi uzatılmış.", punct=".")]})
S[-1]["badi"] = [{"kind": "ittirad", "set": [ix(S[-1], "بِعُتَيْبَةَ"), ix(S[-1], "الْحَارِثِ"), ix(S[-1], "شِهَابِ")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "tawjih": need("tawjih", "تَوْجِيه", "و ج ه", "noun", "tawjih — speech open to two faces (masdar of وَجَّهَ)", "tevcih — iki yüze açık söz (وَجَّهَ'nin masdarı)", 5),
 "muhtamil": need("muhtamil", "مُحْتَمِل", "ح م ل", "noun", "admitting, open to (ism fa'il of احْتَمَلَ)", "ihtimalli, muhtemel (احْتَمَلَ'nin ism-i fâili)", 4),
 "awar": need("awar", "أَعْوَر", "ع و ر", "noun", "one-eyed (the afʿal of defect)", "tek gözlü (kusur ef'ali)", 4),
 "sawa": need("sawa", "سَوَاء", "س و ي", "noun", "equal, alike (one form for singular and dual)", "eşit, müsavi (tekil ve tesniyede tek şekil)", 3),
 "mutashabih": need("mutashabih", "مُتَشَابِه", "ش ب ه", "noun", "ambiguous, open to more than one reading (ism fa'il of تَشَابَهَ; the mutashabihat of the Qur'an)", "müteşâbih, birden çok okumaya açık (تَشَابَهَ'nin ism-i fâili; Kur'ân'ın müteşâbihâtı)", 5, plural="مُتَشَابِهَات"),
 "jidd": need("jidd", "جِدّ", "ج د د", "noun", "earnest, seriousness", "ciddiyet", 3),
 "tamimi": need("tamimi", "تَمِيمِيّ", None, "noun", "a Tamimi — of the tribe of Tamim", "Temîmli — Temîm kabilesinden", 5),
 "mufakhir": need("mufakhir", "مُفَاخِر", "ف خ ر", "noun", "boasting (ism fa'il of فَاخَرَ)", "övünen (فَاخَرَ'nin ism-i fâili)", 5),
 "adda-turn": need("adda-turn", "عَدَّى", "ع د و", "verb", "to pass over, to turn away from (Form II, naqis; عَدَّى يُعَدِّي؛ عَدِّ عَنْ: leave it)", "geçmek, bırakmak (II. bâb, nâkıs; عَدَّى يُعَدِّي؛ عَدِّ عَنْ: onu bırak)", 5, form="II"),
 "akl": need("akl", "أَكْل", "ء ك ل", "noun", "eating (masdar of أَكَلَ)", "yeme (أَكَلَ'nin masdarı)", 2),
 "dabb": need("dabb", "ضَبّ", "ض ب ب", "noun", "the dabb — the spiny-tailed lizard the Bedouin eat", "keler — bedevîlerin yediği kertenkele", 5),
 "tajahul": need("tajahul", "تَجَاهُل", "ج ه ل", "noun", "feigning ignorance (masdar of تَجَاهَلَ)", "bilmezlenme, tecâhül (تَجَاهَلَ'nin masdarı)", 5),
 "arif-knower": need("arif-knower", "عَارِف", "ع ر ف", "noun", "one who knows (ism fa'il of عَرَفَ)", "bilen, ârif (عَرَفَ'nin ism-i fâili)", 3),
 "sawq": need("sawq", "سَوْق", "س و ق", "noun", "driving, bringing forward (masdar of سَاقَ)", "sevk, sürme (سَاقَ'nın masdarı)", 3),
 "malum": need("malum", "مَعْلُوم", "ع ل م", "noun", "known (ism maf'ul of عَلِمَ)", "malûm, bilinen (عَلِمَ'nin ism-i mef'ûlü)", 2),
 "masaq": need("masaq", "مَسَاق", "س و ق", "noun", "a course, a way of driving (the mimi masdar of سَاقَ)", "sevk yolu, sevkediliş (سَاقَ'nın mîmî masdarı)", 5),
 "tawbikh": need("tawbikh", "تَوْبِيخ", "و ب خ", "noun", "reproach (masdar of وَبَّخَ)", "tevbih, azarlama (وَبَّخَ'nin masdarı)", 4),
 "tahayyur": need("tahayyur", "تَحَيُّر", "ح ي ر", "noun", "bewilderment (masdar of تَحَيَّرَ)", "hayret, şaşkınlık (تَحَيَّرَ'nin masdarı)", 4),
 "khariji": need("khariji", "خَارِجِيّ", "خ ر ج", "noun", "a Khariji (the feminine الْخَارِجِيَّة: Layla bint Tarif)", "Hâricî (müennesi الْخَارِجِيَّة: Leylâ bint Tarîf)", 5),
 "aya-nida": need("aya-nida", "أَيَا", None, "part", "O — the call to the far", "ey — uzağa nidâ", 3),
 "khabur": need("khabur", "الْخَابُور", None, "propn", "the Khabur — a river of the Jazira", "Hâbûr — Cezîre'de bir nehir", 6),
 "ma-istifham": need("ma-istifham", "مَا", None, "pron", "what? — the interrogative ma", "ne? — soru mâsı", 2),
 "muriq": need("muriq", "مُورِق", "و ر ق", "noun", "in leaf (ism fa'il of أَوْرَقَ)", "yapraklı, yaprak vermiş (أَوْرَقَ'nin ism-i fâili)", 5),
 "jazia": need("jazia", "جَزِعَ", "ج ز ع", "verb", "to grieve, to lose composure (جَزِعَ يَجْزَعُ)", "yas tutmak, sabrı tükenmek (جَزِعَ يَجْزَعُ)", 4),
 "tarif-alam": need("tarif-alam", "طَرِيف", None, "propn", "Tarif — al-Walid b. Tarif al-Shaybani, the Khariji leader", "Tarîf — Hâricî önder Velîd b. Tarîf eş-Şeybânî", 6),
 "lam-shine": need("lam-shine", "لَمْع", "ل م ع", "noun", "a flash, a gleam (masdar of لَمَعَ)", "parıltı (لَمَعَ'nin masdarı)", 4),
 "sara-night": need("sara-night", "سَرَى", "س ر ي", "verb", "to travel by night (سَرَى يَسْرِي; naqis)", "gece yol almak (سَرَى يَسْرِي; nâkıs)", 4),
 "misbah": need("misbah", "مِصْبَاح", "ص ب ح", "noun", "a lamp", "kandil, lamba", 3),
 "ibtisama": need("ibtisama", "ابْتِسَامَة", "ب س م", "noun", "a smile (masdar of ابْتَسَمَ)", "tebessüm (ابْتَسَمَ'nin masdarı)", 3),
 "manzar": need("manzar", "مَنْظَر", "ن ظ ر", "noun", "a view, a sight", "manzara, görünüş", 3),
 "dahi": need("dahi", "ضَاحٍ", "ض ح و", "noun", "open to the sun, sunlit (ism fa'il of ضَحَا; الضَّاحِي)", "güneşe açık, aydınlık (ضَحَا'nın ism-i fâili; الضَّاحِي)", 6),
 "khala-think": need("khala-think", "خَالَ", "خ ي ل", "verb", "to think, to suppose (خَالَ يَخَالُ; إِخَالُ «I think» with its kasra'd hamza)", "sanmak (خَالَ يَخَالُ; إِخَالُ «sanırım», hemzesi meksûr)", 5),
 "hisn-alam": need("hisn-alam", "حِصْن", None, "propn", "Hisn — Hisn b. Hudhayfa al-Fazari; Al Hisn, his house", "Hısn — Hısn b. Huzeyfe el-Fezârî; Âl-i Hısn, hanedanı", 6),
 "majnun-alam": need("majnun-alam", "الْمَجْنُون", "ج ن ن", "propn", "the Majnun — Qays b. al-Mulawwah, Majnun Layla", "Mecnûn — Kays b. Mülevvah, Mecnûn-ı Leylâ", 5),
 "amiri": need("amiri", "الْعَامِرِيّ", None, "propn", "al-ʿAmiri — of Banu ʿAmir", "el-Âmirî — Benî Âmir'den", 5),
 "zabya": need("zabya", "ظَبْيَة", "ظ ب ي", "noun", "a gazelle doe (its plural ظَبَيَات)", "dişi ceylan (çoğulu ظَبَيَات)", 4, plural="ظَبَيَات"),
 "qa": need("qa", "قَاع", "ق و ع", "noun", "a plain, level ground", "düzlük, ova", 4),
 "pron-2fp": need("pron-2fp", "كُنَّ", None, "pron", "you (feminine plural), attached", "siz (kadınlar), bitişik", 2),
 "layla-alam": need("layla-alam", "لَيْلَى", None, "propn", "Layla — Layla al-ʿAmiriyya, the Majnun's beloved", "Leylâ — Mecnûn'un sevgilisi Leylâ el-Âmiriyye", 4),
 "mujib": need("mujib", "مُوجِب", "و ج ب", "noun", "what entails; the warrant (ism fa'il of أَوْجَبَ)", "gerektiren; mûcib (أَوْجَبَ'nin ism-i fâili)", 5),
 "taarrud": need("taarrud", "تَعَرُّض", "ع ر ض", "noun", "touching on, addressing (masdar of تَعَرَّضَ)", "dokunma, ele alma (تَعَرَّضَ'nin masdarı)", 4),
 "thubut": need("thubut", "ثُبُوت", "ث ب ت", "noun", "being established, holding (masdar of ثَبَتَ)", "sabit olma, sübût (ثَبَتَ'nin masdarı)", 3),
 "nafy": need("nafy", "نَفْي", "ن ف ي", "noun", "denial, negation (masdar of نَفَى)", "nefiy, olumsuzlama (نَفَى'nın masdarı)", 3),
 "aazz": need("aazz", "أَعَزّ", "ع ز ز", "noun", "mightier (ism tafdil of عَزِيز)", "daha üstün, daha izzetli (عَزِيز'in ism-i tafdîli)", 4),
 "izza": need("izza", "عِزَّة", "ع ز ز", "noun", "might, honour", "izzet, üstünlük", 3),
 "haml": need("haml", "حَمْل", "ح م ل", "noun", "carrying; taking a word in a sense (masdar of حَمَلَ)", "taşıma; bir lafzı bir mânâya yorma (حَمَلَ'nin masdarı)", 3),
 "hajjaj-alam": need("hajjaj-alam", "الْحَجَّاج", None, "propn", "al-Hajjaj — Ibn al-Hajjaj, the Baghdadi poet (d. 391/1001)", "el-Haccâc — Bağdatlı şair İbnü'l-Haccâc (ö. 391/1001)", 6),
 "thaqqala": need("thaqqala", "ثَقَّلَ", "ث ق ل", "verb", "to burden, to weigh down (Form II; ثَقَّلَ يُثَقِّلُ)", "ağırlık vermek, yüklemek (II. bâb; ثَقَّلَ يُثَقِّلُ)", 4, form="II"),
 "mirar": need("mirar", "مِرَار", "م ر ر", "noun", "times, repeatedly (plural of مَرَّة)", "kereler, defalarca (مَرَّة'nin çoğulu)", 4),
 "kahil": need("kahil", "كَاهِل", "ك ه ل", "noun", "the upper back between the shoulders", "kâhil, iki kürek arası", 5),
 "ayadi": need("ayadi", "أَيَادٍ", "ي د ي", "noun", "favours, benefits (a plural of plurals of يَد; الْأَيَادِي)", "nimetler, iyilikler (يَد'in cem'ü'l-cem'i; الْأَيَادِي)", 5),
 "ittirad": need("ittirad", "اطِّرَاد", "ط ر د", "noun", "ittirad — a run of names in order (masdar of اطَّرَدَ)", "ittirâd — adların sırayla akışı (اطَّرَدَ'nin masdarı)", 5),
 "wilada": need("wilada", "وِلَادَة", "و ل د", "noun", "birth (masdar of وَلَدَ)", "doğum (وَلَدَ'nin masdarı)", 3),
 "takalluf": need("takalluf", "تَكَلُّف", "ك ل ف", "noun", "strain, affectation (masdar of تَكَلَّفَ)", "zorlanma, tekellüf (تَكَلَّفَ'nin masdarı)", 4),
 "rabia-alam": need("rabia-alam", "رَبِيعَة", None, "propn", "Rabiʿa — Rabiʿa b. Maqrum al-Dabbi, the mukhadram poet", "Rebîa — muhadram şair Rebîa b. Makrûm ed-Dabbî", 6),
 "in-shartiyya": need("in-shartiyya", "إِنْ", None, "part", "if — the conditional in", "eğer — şart edatı in", 2),
 "thalla": need("thalla", "ثَلَّ", "ث ل ل", "verb", "to tear down, to overthrow (a doubled verb; ثَلَّ يَثُلُّ)", "yıkmak, devirmek (muzâaf; ثَلَّ يَثُلُّ)", 5),
 "utayba-alam": need("utayba-alam", "عُتَيْبَة", None, "propn", "ʿUtayba — ʿUtayba b. al-Harith b. Shihab al-Yarbuʿi, the Tamimi horseman", "Uteybe — Temîmli süvari Uteybe b. Hâris b. Şihâb el-Yerbûî", 6),
 "harith-alam": need("harith-alam", "الْحَارِث", None, "propn", "al-Harith — a man's name", "Hâris — erkek adı", 4),
 "shihab-alam": need("shihab-alam", "شِهَاب", None, "propn", "Shihab — a man's name", "Şihâb — erkek adı", 4),
}
for k in ("qawl", "min", "huwa", "an-masdariyya", "fi", "li", "bi", "ka", "wa", "fa", "an", "ala", "ila", "pron-3fs", "pron-3ms", "pron-3mp", "pron-1s", "pron-1p", "pron-2ms", "pron-3d",
          "kalam", "wajh", "mukhtalif", "man-mawsula", "qala", "layta", "ayn-eye", "jaala", "sakkaki", "hazl", "alladhi", "arada", "ab", "nuwas", "idha", "ma-zaida", "ata", "dha", "kayfa",
          "samma", "ghayr", "nukta", "mubalagha", "madh", "aw", "dhamm", "hubb", "shajar", "lahu", "kaanna", "lam", "ibn", "buhturi", "hamza-istifham", "barq", "am", "daw", "zuhayr",
          "ma-nafiya", "dara", "sawfa", "qawm", "al-family", "nisa", "allah", "ya", "bashar", "darb", "ahad", "waqaa", "sifa", "kinaya", "shay", "athbata", "hukm", "dhalika", "taala",
          "lain", "rajaa", "madina", "akhraja", "adhall", "rasul", "mumin", "thani", "lafz", "khilaf", "murad", "ihtamala", "dhikr", "mutaalliq", "idh", "ism", "mamduh", "tartib", "qad", "qatala", "arsh"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
put_morph(mo, "adda-turn", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "عَدَّ", "عَدّ", "i", "عَدّ", "تَعْدِيَة", "مُعَدٍّ (الْمُعَدِّي)", "مُعَدًّى", "عُدِّيَ", "يُعَدَّى", note="عَدَّى عَنْهُ: تَجَاوَزَهُ — عَدِّ عَنْ ذَا."))
put_morph(mo, "jazia", _sg.sound1("samia", "جَزِع", "جْزَع", "اِجْزَع", "جَزَع", "جَازِع", note="لَازِمٌ مِنْ بَابِ سَمِعَ: جَزِعَ يَجْزَعُ جَزَعًا."))
put_morph(mo, "sara-night", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "سَرَ", "سْر", "i", "اِسْر", "سُرًى", "سَارٍ (السَّارِي)", None, None, None, note="لَازِمٌ: سَرَى يَسْرِي سُرًى — سَارَ لَيْلًا."))
put_morph(mo, "khala-think", _sg.hollow1("fataha", "أَجْوَفُ يَائِيٌّ", "خَال", "خِل", "خَال", "خَل", "خَل", "خَل", "خَيْل", "خَائِل", note="مِنْ أَخَوَاتِ ظَنَّ: خَالَ يَخَالُ — إِخَالُ بِكَسْرِ الْهَمْزَةِ عَلَى الشُّذُوذِ."))
put_morph(mo, "thaqqala", _sg.derived(_sg.B2, _sg.W2, "ُ", "ثَقَّل", "ثَقِّل", "ثَقِّل", "تَثْقِيل", "مُثَقِّل", "مُثَقَّل", "ثُقِّلَ", "يُثَقَّلُ"))
put_morph(mo, "thalla", gem("nasara", "ثَلّ", "ثَلَل", "ثُلّ", "ثْلُل", ["ثُلَّ", "ثُلَّا", "ثُلُّوا", "ثُلِّي", "ثُلَّا", "اُثْلُلْنَ"], "ثَلّ", "ثَالّ", "مَثْلُول", "ثُلَّ", "يُثَلُّ", "مُضَاعَفٌ: ثَلَّ يَثُلُّ — ثَلَلْتَ: فُكَّ الْإِدْغَامُ لِاتِّصَالِ تَاءِ الْفَاعِلِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_W = {
 "id": "tawjih-wa-hazl",
 "title": {"ar": "التَّوْجِيهُ، وَالْهَزْلُ الَّذِي يُرَادُ بِهِ الْجِدُّ", "en": "Tawjih — speech open to two faces; the jest by which earnest is meant", "tr": "Tevcih — iki yüze açık söz; ciddiyet kastedilen şaka"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التوجيه: إيراد الكلام محتملا لوجهين مختلفين، كقول من قال لأعور: ليت عينيه سواء. الهزل الذي يراد به الجد، كقوله: إذا ما تميمي أتاك مفاخرا فقل عد عن ذا كيف أكلك للضب."],
 "question": {
  "en": ["Can the same words be read TWO opposite ways, and the speaker meant them so? TAWJIH — to a one-eyed man: لَيْتَ عَيْنَيْهِ سَوَاءُ, «would that his eyes were equal» — both seeing, or both blind. Al-Sakkaki counted the Qur'an's mutashabihat here, as verses open to two faces.",
         "Is a JEST said so that the EARNEST behind it is meant? Abu Nuwas to the boasting Tamimi: عَدِّ عَنْ ذَا كَيْفَ أَكْلُكَ لِلضَّبِّ — the laughing question carries the taunt: your tribe eats lizards.",
         "What does the engine read? Both are matters of meaning; the frame is the author's, and the card lights the word the two faces turn on."],
  "tr": ["Aynı sözler ZIT iki şekilde okunabiliyor ve söyleyen bunu mu kastetti? TEVCİH — tek gözlüye: لَيْتَ عَيْنَيْهِ سَوَاءُ, «keşke iki gözü eşit olsa» — ikisi de görür yahut ikisi de kör. Sekkâkî Kur'ân'ın müteşâbihâtını da iki yüze açık âyetler diye buraya saydı.",
         "Bir ŞAKA, arkasındaki CİDDİYET kastedilerek mi söyleniyor? Ebû Nüvâs övünen Temîmliye: عَدِّ عَنْ ذَا كَيْفَ أَكْلُكَ لِلضَّبِّ — gülen soru hicvi taşır: kabilen keler yer.",
         "Motor neyi okur? İkisi de mânâ işidir; çerçeve müellifindir; kart iki yüzün döndüğü kelimeyi yakar."]},
 "plain": {
  "en": "Tawjih brings speech open to two different faces (would that the one-eyed man's eyes were equal). The jest by which earnest is meant hides a taunt in a laugh (how do you eat lizard?). Both are matters of meaning: the frames are the author's.",
  "tr": "Tevcih sözü iki farklı yüze açık getirir (keşke tek gözlünün gözleri eşit olsa). Ciddiyet kastedilen şaka, hicvi gülüşe saklar (keleri nasıl yersin?). İkisi de mânâ işidir: çerçeveler müellifindir."},
 "explanation": {
  "en": "TAWJIH is إِيرَادُ الْكَلَامِ مُحْتَمِلًا لِوَجْهَيْنِ مُخْتَلِفَيْنِ: to a one-eyed man, لَيْتَ عَيْنَيْهِ سَوَاءُ — «equal» may mean both sound (a prayer) or both blind (a curse), and the speaker leaves it open. Al-Sakkaki made the mutashabihat of the Qur'an a case of it, since they admit two faces. The HAZL BY WHICH EARNEST IS MEANT: Abu Nuwas lampooning Banu Tamim, إِذَا مَا تَمِيمِيٌّ أَتَاكَ مُفَاخِرًا فَقُلْ عَدِّ عَنْ ذَا كَيْفَ أَكْلُكَ لِلضَّبِّ — the jesting question is the earnest taunt.",
  "tr": "TEVCİH إِيرَادُ الْكَلَامِ مُحْتَمِلًا لِوَجْهَيْنِ مُخْتَلِفَيْنِ'dir: tek gözlüye لَيْتَ عَيْنَيْهِ سَوَاءُ — «eşit» ikisi de sağlam (dua) yahut ikisi de kör (beddua) olabilir; söyleyen bunu açık bırakır. Sekkâkî Kur'ân'ın müteşâbihâtını, iki yüze ihtimalli olmaları itibariyle buna kattı. CİDDİYET KASTEDİLEN HEZL: Ebû Nüvâs Benî Temîm'i hicvederken, إِذَا مَا تَمِيمِيٌّ أَتَاكَ مُفَاخِرًا فَقُلْ عَدِّ عَنْ ذَا كَيْفَ أَكْلُكَ لِلضَّبِّ — şakacı soru ciddî hicivdir."},
 "examples": [
  {"ar": "لَيْتَ عَيْنَيْهِ سَوَاءٌ", "en": "to a one-eyed man — tawjih.", "tr": "tek gözlüye — tevcih.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "إِذَا مَا تَمِيمِيٌّ أَتَاكَ مُفَاخِرًا * فَقُلْ عَدِّ عَنْ ذَا كَيْفَ أَكْلُكَ لِلضَّبِّ", "en": "Abu Nuwas — the jest that means earnest.", "tr": "Ebû Nüvâs — ciddiyet kastedilen şaka.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«لَيْتَ عَيْنَيْهِ سَوَاءٌ bir tevriyedir: yakın mânâ görünür, uzak mânâ kastedilir»",
   "right": "«Tevcihtir: iki yüz de eşit derecede kastedilebilir; tevriyede ise uzak mânâ tek başına muraddır»",
   "why": {"en": "Tawriya hides one meaning behind another; tawjih keeps both faces open.", "tr": "Tevriye bir mânâyı öbürünün ardına saklar; tevcih iki yüzü de açık tutar."}}],
 "relatedNotes": ["tawriya", "tajahul-al-arif", "insha-wa-tamanni", "ilm-al-badi"]}

NOTE_J = {
 "id": "tajahul-al-arif",
 "title": {"ar": "تَجَاهُلُ الْعَارِفِ — سَوْقُ الْمَعْلُومِ مَسَاقَ غَيْرِهِ لِنُكْتَةٍ", "en": "Tajahul al-ʿarif — the knower feigning ignorance, for a point", "tr": "Tecâhül-i ârif — bilenin bir nükte için bilmez görünmesi"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — تجاهل العارف، وسماه السكاكي سوق المعلوم مساق غيره لنكتة: كالتوبيخ، والمبالغة في المدح أو الذم، والتحير في الحب."],
 "question": {
  "en": ["Does the speaker ASK what he plainly knows — and for a reason? TAJAHUL AL-ʿARIF, al-Sakkaki's «driving the known in the course of the unknown for a point».",
         "REPROACH: Layla bint Tarif to the tree of the Khabur, مَا لَكَ مُورِقًا كَأَنَّكَ لَمْ تَجْزَعْ — she knows why a tree is in leaf. HYPERBOLE IN PRAISE: al-Buhturi, أَلَمْعُ بَرْقٍ … أَمْ ضَوْءُ مِصْبَاحٍ أَمِ ابْتِسَامَتُهَا — he knows it is her smile. IN BLAME: Zuhayr, أَقَوْمٌ آلُ حِصْنٍ أَمْ نِسَاءُ. BEWILDERMENT IN LOVE: the Majnun, لَيْلَايَ مِنْكُنَّ أَمْ لَيْلَى مِنَ الْبَشَرِ.",
         "What does the engine read? The question's SHAPE: the hamza paired with أَمْ, a bare أَمْ, لَيْتَ, مَا لَكَ, مَا أَدْرِي, the كَأَنَّ that feigns a doubt; the AIM (reproach, praise, blame, love) is the author's judgement."],
  "tr": ["Söyleyen açıkça BİLDİĞİNİ mi soruyor — bir sebeple? TECÂHÜL-İ ÂRİF, Sekkâkî'nin «bir nükte için malûmu meçhulün yolunda sevketmesi».",
         "TEVBİH: Leylâ bint Tarîf Hâbûr ağacına, مَا لَكَ مُورِقًا كَأَنَّكَ لَمْ تَجْزَعْ — ağacın niçin yapraklandığını bilir. MEDİHTE MÜBALAĞA: Buhtürî, أَلَمْعُ بَرْقٍ … أَمْ ضَوْءُ مِصْبَاحٍ أَمِ ابْتِسَامَتُهَا — tebessümü olduğunu bilir. ZEMDE: Züheyr, أَقَوْمٌ آلُ حِصْنٍ أَمْ نِسَاءُ. AŞKTA HAYRET: Mecnûn, لَيْلَايَ مِنْكُنَّ أَمْ لَيْلَى مِنَ الْبَشَرِ.",
         "Motor neyi okur? Sorunun ŞEKLİNİ: أَمْ ile eşleşen hemze, yalın أَمْ, لَيْتَ, مَا لَكَ, مَا أَدْرِي, şüphe taslayan كَأَنَّ; NÜKTE (tevbih, medih, zem, aşk) müellifin hükmüdür."]},
 "plain": {
  "en": "Tajahul al-ʿarif asks what the speaker knows, for a point: reproach (the leafy tree), hyperbole in praise (lightning or her smile?) or in blame (men or women?), bewilderment in love (is my Layla one of you, gazelles?). The engine reads the question's shape; the aim is the author's.",
  "tr": "Tecâhül-i ârif, söyleyenin bildiğini bir nükte için sorar: tevbih (yapraklı ağaç), medihte mübalağa (şimşek mi tebessümü mü?) yahut zemde (erkek mi kadın mı?), aşkta hayret (Leylâm sizden mi, ceylanlar?). Motor sorunun şeklini okur; nükte müellifindir."},
 "explanation": {
  "en": "TAJAHUL AL-ʿARIF — which al-Sakkaki named سَوْقُ الْمَعْلُومِ مَسَاقَ غَيْرِهِ لِنُكْتَةٍ — has four points in the Talkhis. REPROACH: أَيَا شَجَرَ الْخَابُورِ مَا لَكَ مُورِقًا كَأَنَّكَ لَمْ تَجْزَعْ عَلَى ابْنِ طَرِيفِ. HYPERBOLE IN PRAISE: أَلَمْعُ بَرْقٍ سَرَى أَمْ ضَوْءُ مِصْبَاحٍ أَمِ ابْتِسَامَتُهَا بِالْمَنْظَرِ الضَّاحِي. HYPERBOLE IN BLAME: وَمَا أَدْرِي وَسَوْفَ إِخَالُ أَدْرِي أَقَوْمٌ آلُ حِصْنٍ أَمْ نِسَاءُ — and the kasra of إِخَالُ is irregular by rule, eloquent by usage. BEWILDERMENT IN LOVE: بِاللهِ يَا ظَبَيَاتِ الْقَاعِ قُلْنَ لَنَا لَيْلَايَ مِنْكُنَّ أَمْ لَيْلَى مِنَ الْبَشَرِ. The card fans the question out from its adat and names the aim.",
  "tr": "TECÂHÜL-İ ÂRİF — Sekkâkî'nin سَوْقُ الْمَعْلُومِ مَسَاقَ غَيْرِهِ لِنُكْتَةٍ dediği — Telhîs'te dört nükteye gelir. TEVBİH: أَيَا شَجَرَ الْخَابُورِ مَا لَكَ مُورِقًا كَأَنَّكَ لَمْ تَجْزَعْ عَلَى ابْنِ طَرِيفِ. MEDİHTE MÜBALAĞA: أَلَمْعُ بَرْقٍ سَرَى أَمْ ضَوْءُ مِصْبَاحٍ أَمِ ابْتِسَامَتُهَا بِالْمَنْظَرِ الضَّاحِي. ZEMDE MÜBALAĞA: وَمَا أَدْرِي وَسَوْفَ إِخَالُ أَدْرِي أَقَوْمٌ آلُ حِصْنٍ أَمْ نِسَاءُ — إِخَالُ'nün kesresi kıyasa aykırı, kullanımca fasihtir. AŞKTA HAYRET: بِاللهِ يَا ظَبَيَاتِ الْقَاعِ قُلْنَ لَنَا لَيْلَايَ مِنْكُنَّ أَمْ لَيْلَى مِنَ الْبَشَرِ. Kart soruyu edatından yelpaze gibi açar ve nükteyi adlandırır."},
 "examples": [
  {"ar": "أَيَا شَجَرَ الْخَابُورِ مَا لَكَ مُورِقًا * كَأَنَّكَ لَمْ تَجْزَعْ عَلَى ابْنِ طَرِيفِ", "en": "Layla bint Tarif — reproach.", "tr": "Leylâ bint Tarîf — tevbih.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "أَلَمْعُ بَرْقٍ سَرَى أَمْ ضَوْءُ مِصْبَاحٍ * أَمِ ابْتِسَامَتُهَا بِالْمَنْظَرِ الضَّاحِي", "en": "al-Buhturi — hyperbole in praise.", "tr": "Buhtürî — medihte mübalağa.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "وَمَا أَدْرِي وَسَوْفَ إِخَالُ أَدْرِي * أَقَوْمٌ آلُ حِصْنٍ أَمْ نِسَاءُ", "en": "Zuhayr — hyperbole in blame.", "tr": "Züheyr — zemde mübalağa.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "بِاللهِ يَا ظَبَيَاتِ الْقَاعِ قُلْنَ لَنَا * لَيْلَايَ مِنْكُنَّ أَمْ لَيْلَى مِنَ الْبَشَرِ", "en": "the Majnun — bewilderment in love.", "tr": "Mecnûn — aşkta hayret.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«أَقَوْمٌ آلُ حِصْنٍ أَمْ نِسَاءُ gerçek bir sorudur: şair bilmiyor»",
   "right": "«Tecâhül-i âriftir: şair bilir; zemde mübalağa için bilmez görünür — مَا أَدْرِي bunun alındısıdır»",
   "why": {"en": "The figure is the feigning: the question's shape stands on a thing the speaker knows.", "tr": "Sanat taslamadadır: sorunun şekli söyleyenin bildiği bir şey üstünde durur."}}],
 "relatedNotes": ["al-istifham", "adawat-al-tasawwur", "khuruj-al-istifham", "tawjih-wa-hazl", "mubalagha-maqbula", "ilm-al-badi"]}

NOTE_Q = {
 "id": "qawl-bil-mujib",
 "title": {"ar": "الْقَوْلُ بِالْمُوجِبِ — صِفَةٌ تُرَدُّ إِلَى غَيْرِ صَاحِبِهَا، وَلَفْظٌ يُحْمَلُ عَلَى خِلَافِ مُرَادِهِ", "en": "Al-qawl bil-mujib — the other's word turned by its own warrant", "tr": "Kavl bi'l-mûcib — muhatabın sözünün kendi mûcibiyle çevrilmesi"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — القول بالموجب ضربان: أحدهما أن تقع صفة في كلام الغير كناية عن شيء أثبت له حكم، فتثبتها لغيره من غير تعرض لثبوت ذلك الحكم له أو نفيه عنه؛ والثاني حمل لفظ وقع في كلام الغير على خلاف مراده مما يحتمله بذكر متعلقه."],
 "question": {
  "en": ["Does the reply take the OTHER'S OWN WORD and turn it? AL-QAWL BIL-MUJIB, in two kinds.",
         "A QUALITY used by the other as a kinaya for himself — «the mightier will drive out the meaner» — is affirmed of someone else: وَلِلَّهِ الْعِزَّةُ وَلِرَسُولِهِ وَلِلْمُؤْمِنِينَ, and whether the driving-out holds of the hypocrites is left untouched.",
         "A WORD in the other's mouth is carried to another of its senses by naming what it attaches to: قُلْتُ ثَقَّلْتُ … قَالَ ثَقَّلْتَ كَاهِلِي بِالْأَيَادِي — «I burdened you» becomes «you burdened my shoulders — with favours».",
         "What does the engine read? The same word (or root) standing in both halves — الْأَعَزُّ / الْعِزَّةُ, ثَقَّلْتُ / ثَقَّلْتَ — the second turned on the first; which kind is the author's judgement."],
  "tr": ["Cevap, MUHATABIN KENDİ SÖZÜNÜ alıp çeviriyor mu? KAVL Bİ'L-MÛCİB, iki kısım.",
         "Muhatabın kendine kinaye olarak kullandığı bir SIFAT — «daha üstün olan daha alçağı çıkaracak» — başkasına ispat edilir: وَلِلَّهِ الْعِزَّةُ وَلِرَسُولِهِ وَلِلْمُؤْمِنِينَ; çıkarmanın münafıklara ait olup olmadığına dokunulmaz.",
         "Muhatabın ağzındaki bir LAFIZ, mütealliki anılarak başka bir mânâsına yorulur: قُلْتُ ثَقَّلْتُ … قَالَ ثَقَّلْتَ كَاهِلِي بِالْأَيَادِي — «sana ağırlık verdim», «omzuma ağırlık verdin — nimetlerle» olur.",
         "Motor neyi okur? İki yarıda duran aynı kelimeyi (yahut kökü) — الْأَعَزُّ / الْعِزَّةُ, ثَقَّلْتُ / ثَقَّلْتَ — ikincisi birincinin üstüne çevrilmiş; hangi kısım olduğu müellifin hükmüdür."]},
 "plain": {
  "en": "Al-qawl bil-mujib turns the other's own word: a quality he used as a kinaya for himself is affirmed of someone else (the might is God's), or his word is carried to another sense by naming what it attaches to (you burdened my shoulders with favours). The engine reads the shared word.",
  "tr": "Kavl bi'l-mûcib muhatabın kendi sözünü çevirir: kendine kinaye olarak kullandığı sıfat başkasına ispat edilir (izzet Allah'ındır), yahut lafzı mütealliki anılarak başka mânâya yorulur (omzuma nimetlerle ağırlık verdin). Motor ortak kelimeyi okur."},
 "explanation": {
  "en": "AL-QAWL BIL-MUJIB has two kinds. The FIRST: أَنْ تَقَعَ صِفَةٌ فِي كَلَامِ الْغَيْرِ كِنَايَةً عَنْ شَيْءٍ أُثْبِتَ لَهُ حُكْمٌ، فَتُثْبِتَهَا لِغَيْرِهِ مِنْ غَيْرِ تَعَرُّضٍ لِثُبُوتِ ذَلِكَ الْحُكْمِ لَهُ أَوْ نَفْيِهِ عَنْهُ — in يَقُولُونَ لَئِنْ رَجَعْنَا إِلَى الْمَدِينَةِ لَيُخْرِجَنَّ الْأَعَزُّ مِنْهَا الْأَذَلَّ the hypocrites' «mightier» is a kinaya for themselves, and the ruling of driving out is affirmed of them; the reply وَلِلَّهِ الْعِزَّةُ وَلِرَسُولِهِ وَلِلْمُؤْمِنِينَ affirms the might of others and says nothing of that ruling. The SECOND: حَمْلُ لَفْظٍ وَقَعَ فِي كَلَامِ الْغَيْرِ عَلَى خِلَافِ مُرَادِهِ مِمَّا يَحْتَمِلُهُ بِذِكْرِ مُتَعَلِّقِهِ — Ibn al-Hajjaj: قُلْتُ ثَقَّلْتُ إِذْ أَتَيْتُ مِرَارًا قَالَ ثَقَّلْتَ كَاهِلِي بِالْأَيَادِي; the poet meant «I have wearied you», and the patron carries ثَقَّلْتَ to «loaded my shoulders» by naming the favours.",
  "tr": "KAVL Bİ'L-MÛCİB iki kısımdır. BİRİNCİSİ: أَنْ تَقَعَ صِفَةٌ فِي كَلَامِ الْغَيْرِ كِنَايَةً عَنْ شَيْءٍ أُثْبِتَ لَهُ حُكْمٌ، فَتُثْبِتَهَا لِغَيْرِهِ مِنْ غَيْرِ تَعَرُّضٍ لِثُبُوتِ ذَلِكَ الْحُكْمِ لَهُ أَوْ نَفْيِهِ عَنْهُ — يَقُولُونَ لَئِنْ رَجَعْنَا إِلَى الْمَدِينَةِ لَيُخْرِجَنَّ الْأَعَزُّ مِنْهَا الْأَذَلَّ'de münafıkların «daha üstün»ü kendilerine kinayedir ve çıkarma hükmü onlara ispat edilmiştir; cevap وَلِلَّهِ الْعِزَّةُ وَلِرَسُولِهِ وَلِلْمُؤْمِنِينَ izzeti başkalarına ispat eder, o hükme hiç dokunmaz. İKİNCİSİ: حَمْلُ لَفْظٍ وَقَعَ فِي كَلَامِ الْغَيْرِ عَلَى خِلَافِ مُرَادِهِ مِمَّا يَحْتَمِلُهُ بِذِكْرِ مُتَعَلِّقِهِ — İbnü'l-Haccâc: قُلْتُ ثَقَّلْتُ إِذْ أَتَيْتُ مِرَارًا قَالَ ثَقَّلْتَ كَاهِلِي بِالْأَيَادِي; şair «seni yordum» demek istedi, memdûh ثَقَّلْتَ'yi nimetleri anarak «omzumu yükledin»e çevirdi."},
 "examples": [
  {"ar": "لَيُخْرِجَنَّ الْأَعَزُّ مِنْهَا الْأَذَلَّ وَلِلَّهِ الْعِزَّةُ وَلِرَسُولِهِ وَلِلْمُؤْمِنِينَ", "en": "63:8 — the first kind.", "tr": "Münâfikûn 8 — birinci kısım.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "قُلْتُ ثَقَّلْتُ إِذْ أَتَيْتُ مِرَارًا * قَالَ ثَقَّلْتَ كَاهِلِي بِالْأَيَادِي", "en": "Ibn al-Hajjaj — the second kind.", "tr": "İbnü'l-Haccâc — ikinci kısım.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"}],
 "commonMistakes": [
  {"wrong": "«وَلِلَّهِ الْعِزَّةُ münafıkların hükmünü reddeder: üstün olan çıkarmayacaktır»",
   "right": "«Âyet çıkarma hükmüne hiç dokunmaz; yalnız «izzet» sıfatını gerçek sahiplerine ispat eder — kavl bi'l-mûcib budur»",
   "why": {"en": "The figure answers on the other's own warrant, silent about the ruling he attached to it.", "tr": "Sanat muhatabın kendi mûcibiyle cevap verir; ona bağladığı hüküm hakkında susar."}}],
 "relatedNotes": ["kinaya", "aqsam-al-kinaya", "tawriya", "tajahul-al-arif", "ilm-al-badi"]}

NOTE_T = {
 "id": "ittirad",
 "title": {"ar": "الِاطِّرَادُ — اسْمُ الْمَمْدُوحِ وَأَسْمَاءُ آبَائِهِ عَلَى تَرْتِيبِ الْوِلَادَةِ", "en": "Ittirad — the praised and his fathers named in birth order, unforced", "tr": "İttirâd — memdûh ve babaları doğum sırasıyla, zorlanmadan"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الاطراد: أن يأتي باسم الممدوح وأسماء آبائه على ترتيب الولادة من غير تكلف، كقوله: إن يقتلوك فقد ثللت عروشهم * بعتيبة بن الحارث بن شهاب."],
 "question": {
  "en": ["Does the bayt RUN through the praised man's name and his fathers' names in the order of birth, and does the metre carry them with no strain? ITTIRAD — بِعُتَيْبَةَ بْنِ الْحَارِثِ بْنِ شِهَابِ.",
         "What does the engine read? The chain of names hinged on بْنِ — a name, بْنِ, a name, بْنِ, a name — and shows it as one unbroken run."],
  "tr": ["Beyit, memdûhun adını ve babalarının adlarını doğum sırasıyla mı AKITIYOR, vezin bunları zorlanmadan mı taşıyor? İTTİRÂD — بِعُتَيْبَةَ بْنِ الْحَارِثِ بْنِ شِهَابِ.",
         "Motor neyi okur? بْنِ üstünde menteşelenen ad zincirini — ad, بْنِ, ad, بْنِ, ad — ve onu kesintisiz tek akış olarak gösterir."]},
 "plain": {
  "en": "Ittirad names the praised man and his fathers in birth order with no strain: with ʿUtayba son of al-Harith son of Shihab. The engine reads the run of names hinged on بْنِ.",
  "tr": "İttirâd, memdûhu ve babalarını doğum sırasıyla, zorlanmadan adlandırır: Şihâb oğlu Hâris oğlu Uteybe ile. Motor بْنِ üstünde menteşelenen ad akışını okur."},
 "explanation": {
  "en": "ITTIRAD is أَنْ يَأْتِيَ بِاسْمِ الْمَمْدُوحِ وَأَسْمَاءِ آبَائِهِ عَلَى تَرْتِيبِ الْوِلَادَةِ مِنْ غَيْرِ تَكَلُّفٍ. Rabiʿa b. Maqrum: إِنْ يَقْتُلُوكَ فَقَدْ ثَلَلْتَ عُرُوشَهُمْ بِعُتَيْبَةَ بْنِ الْحَارِثِ بْنِ شِهَابِ — the man addressed had killed ʿUtayba b. al-Harith b. Shihab, the Tamimi horseman, and so brought down their kingship; the three names run in order and the metre takes them whole.",
  "tr": "İTTİRÂD أَنْ يَأْتِيَ بِاسْمِ الْمَمْدُوحِ وَأَسْمَاءِ آبَائِهِ عَلَى تَرْتِيبِ الْوِلَادَةِ مِنْ غَيْرِ تَكَلُّفٍ'dir. Rebîa b. Makrûm: إِنْ يَقْتُلُوكَ فَقَدْ ثَلَلْتَ عُرُوشَهُمْ بِعُتَيْبَةَ بْنِ الْحَارِثِ بْنِ شِهَابِ — hitap edilen kişi Temîmli süvari Uteybe b. Hâris b. Şihâb'ı öldürmüş, böylece saltanatlarını yıkmıştı; üç ad sırayla akar, vezin onları bütün olarak taşır."},
 "examples": [
  {"ar": "إِنْ يَقْتُلُوكَ فَقَدْ ثَلَلْتَ عُرُوشَهُمْ * بِعُتَيْبَةَ بْنِ الْحَارِثِ بْنِ شِهَابِ", "en": "Rabiʿa b. Maqrum — ittirad.", "tr": "Rebîa b. Makrûm — ittirâd.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"}],
 "commonMistakes": [
  {"wrong": "«Her nesep zinciri ittirâddır»",
   "right": "«Şart, doğum sırası ve zorlanmama: adlar vezne sığmak için eğilip bükülürse ittirâd yoktur»",
   "why": {"en": "The figure is the effortless run, not the mere listing.", "tr": "Sanat zorlanmasız akıştır, yalnız sıralama değil."}}],
 "relatedNotes": ["idafa-definiteness", "mamnu-min-sarf", "ilm-al-badi"]}

ADD_EN = (" Chapter 67 (lines ~4345-4395, sahifa 150-151) carries tawjih (the one-eyed man s2; al-Sakkaki on the mutashabihat s3), the jest that means "
          "earnest (Abu Nuwas s5), tajahul al-ʿarif with its four points (Layla bint Tarif s7, al-Buhturi s8, Zuhayr s9, the Majnun s10), al-qawl bil-mujib "
          "(63:8 s13; Ibn al-Hajjaj s15) and ittirad (Rabiʿa b. Maqrum s17). The definitions and headings (s1, s3, s4, s6, s11, s12, s14, s16) are RESTORED: the "
          "source carries them only in Turkish, and the Arabic is the received matn of the Talkhis; every restored sentence is marked «Restored» in its "
          "translation. The rhyme words are written by the itlaq (طَرِيفِ، نِسَاءُ، شِهَابِ) where the print keeps the tanwin. The examples carry "
          "`badi` frames (tawjih and hazl-jidd with the turning `word`; tajahul with the question's `word`, its aim as `sub`, its `receipt` and the partner "
          "`companion`; qawl-mujib with the turned `word`, its kind as `sub` and the other's `companion`; ittirad with the `set` of names).")
ADD_TR = (" Altmış yedinci bâb (satır ~4345-4395, sahife 150-151) tevcihi (tek gözlü s2; Sekkâkî'nin müteşâbihâtı s3), ciddiyet kastedilen şakayı (Ebû "
          "Nüvâs s5), dört nüktesiyle tecâhül-i ârifi (Leylâ bint Tarîf s7, Buhtürî s8, Züheyr s9, Mecnûn s10), kavl bi'l-mûcibi (Münâfikûn 8 s13; İbnü'l-Haccâc "
          "s15) ve ittirâdı (Rebîa b. Makrûm s17) taşır. Tarifler ve başlıklar (s1, s3, s4, s6, s11, s12, s14, s16) GERİ YAZILMIŞTIR: kaynak bunları yalnız "
          "Türkçe taşır; Arapça, Telhîs'in alınan metnidir. Her geri yazılmış cümle tercümesinde «geri yazılmıştır» diye işaretlidir. Kafiye kelimeleri, "
          "baskının tenvini koruduğu yerlerde ıtlâkla yazılmıştır (طَرِيفِ، نِسَاءُ، شِهَابِ). Örnekler `badi` çerçeveleri taşır (tevcih ve hezl: "
          "dönen `word`; tecâhül: sorunun `word`ü, nüktesi `sub`, alındısı `receipt`, eşi `companion`; kavl bi'l-mûcib: çevrilen `word`, kısmı `sub`, "
          "muhatabınki `companion`; ittirâd: adların `set`i).")
write_out(67, S, TITLE, ADD_EN, ADD_TR, "4345-4395", GLOSS_ADD, notes=(NOTE_W, NOTE_J, NOTE_Q, NOTE_T),
          related=(("tawriya", ["tawjih-wa-hazl", "qawl-bil-mujib"]), ("al-istifham", ["tajahul-al-arif"]), ("adawat-al-tasawwur", ["tajahul-al-arif"]), ("kinaya", ["qawl-bil-mujib"]),
                   ("ilm-al-badi", ["tawjih-wa-hazl", "tajahul-al-arif", "qawl-bil-mujib", "ittirad"])))
report(67, S, GLOSS_ADD, (NOTE_W, NOTE_J, NOTE_Q, NOTE_T))
