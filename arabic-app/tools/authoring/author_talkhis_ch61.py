# -*- coding: utf-8 -*-
"""Author chapter 61 of talkhis-al-miftah — the JAMʿ (many things gathered under one
ruling), the TAFRIQ (a difference struck between two things of one kind) and the
TAQSIM (many things named, then to each its own) — sahifa 141-142, lines ~4100-4130.

  RESTORED (the source carries the step only in Turkish): s1, s4, s7 (the three
          definitions) and s9 (the closing summary); the frames of every example.
  As printed: the ayat (18:46) and the verses of Abu l-ʿAtahiya, Rashid al-Din
          al-Watwat and Jarir b. ʿAbd al-Masih.

Frames: jam {set: the gathered items, word: the one ruling}; tafriq {first: the
first thing, second: the second, of one kind — the likeness denied}; taqsim
{first: the items named, second: the head of each item's own ruling, in order}.
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
def kaqawl(tag, punct=None):
    return tok("كَقَوْلِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")], punct=punct)
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

J = "jam"; T = "tafriq"; Q = "taqsim"
TITLE = {"ar": "الْجَمْعُ، وَالتَّفْرِيقُ، وَالتَّقْسِيمُ",
         "en": "The Jamʿ; the Tafriq; the Taqsim", "tr": "Cem'; Tefrîk; Taksîm"}
S = []
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them» — a fronted khabar.", "«onlardan biri de» — takdim edilmiş haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def wahuwa(tag, full="وَهُوَ"):
    lex = "hiya" if full.endswith("هِيَ") else "huwa"
    return tok(full, lex, "pron", [tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالضَّمِيرُ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
               segments=[seg("وَ","wa","conj"), seg(full[1:], lex, "pron")])
def an_masd(tag):
    return tok("أَنْ","an","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the interpreted masdar is the khabar.", "«… -mesi» — müevvel masdar haberdir.")
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

# ----------- s1 — the jamʿ (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the JAMʿ: to GATHER many things under ONE ruling." + R_EN,
 "tr": "Onlardan biri CEM'DİR: birden çok şeyi TEK bir hükümde TOPLAMAK." + R_TR},
 "tokens": [
  minha(J),
  tok("الْجَمْعُ","jam","noun",[J, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ جَمَعَ.", "«the jamʿ» — the masdar of جَمَعَ.", "«cem'» — جَمَعَ'nin masdarı."),
  wahuwa(J),
  an_masd(J),
  tok("يُجْمَعَ","jamaa-gather","verb",[J, "an-masdariyya", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«be gathered» — the passive, mansub by أَنْ; the jarr phrase after it stands as its deputy.", "«toplanması» — meçhul, أَنْ ile mansûb; ardındaki câr-mecrûr nâib-i fâildir."),
  tok("بَيْنَ","bayna","noun",[J, "maful-fih"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُضَافٌ.", "«between» — a zarf, mudaf.", "«arasında» — zarf, muzâf."),
  tok("مُتَعَدِّدٍ","mutaaddid","noun",[J, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ تَعَدَّدَ.", "«many things» — mudaf ilayh.", "«birden çok şey» — muzâfun ileyh."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("حُكْمٍ","hukm","noun",[J, "huruf-jarr"], "مَجْرُورٌ — حُكْمٌ وَاحِدٌ يَعُمُّ الْمُتَعَدِّدَ.", "«one ruling» — a single ruling that covers them all.", "«bir hükümde» — hepsini kuşatan tek hüküm.", punct=".")]})

# ----------- s2 — 18:46
S.append({"id": "s2", "translation": {
 "en": "As He says, exalted is He: «WEALTH and SONS are the adornment of the life of this world» — two things gathered under one ruling." + R_EN,
 "tr": "Nitekim Allah Teâlâ buyurur: «MAL ve OĞULLAR dünya hayatının süsüdür» — iki şey tek hükümde toplanmıştır." + R_TR},
 "tokens": [
  kaq(J), taala(J),
  tok("الْمَالُ","mal","noun",[J, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«wealth» — the mubtada.", "«mal» — mübtedâ."),
  wa_conj("وَالْبَنُونَ","banun","noun",[J, "atf-nasaq", "jam-mudhakkar-salim"], "الْبَنُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«and sons» — joined, raf' by the waw: attached to the sound plural.", "«ve oğullar» — ma'tûf, vâv ile merfû: cem-i müzekker-i sâlime mülhak."),
  tok("زِينَةُ","zina","noun",[J, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — الْحُكْمُ الْوَاحِدُ الَّذِي جُمِعَ فِيهِ الْمَالُ وَالْبَنُونَ.", "«the adornment» — the khabar, mudaf: the one ruling wealth and sons are gathered in.", "«süsü» — haber, muzâf: malın ve oğulların toplandığı tek hüküm."),
  tok("الْحَيَاةِ","hayat","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«of the life».", "«hayatının»."),
  tok("الدُّنْيَا","dunya","noun",[J, "naat-sifa", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«of this world» — a na't, its kasra estimated on the alif.", "«dünya» — na't, kesresi elif üzerinde takdîrî.", punct=".")]})
S[-1]["badi"] = [{"kind": "jam", "set": [ix(S[-1], "الْمَالُ"), ix(S[-1], "وَالْبَنُونَ")], "word": ix(S[-1], "زِينَةُ")}]

# ----------- s3 — Abu l-ʿAtahiya
S.append({"id": "s3", "translation": {
 "en": "And Abu l-ʿAtahiya's verse: «YOUTH, IDLENESS and WEALTH • are a ruin for a man — and what a ruin!» — three things gathered under one ruling." + R_EN,
 "tr": "Ve Ebü'l-Atâhiye'nin beyti: «GENÇLİK, BOŞLUK ve ZENGİNLİK • kişi için bir fesat kaynağıdır — hem ne fesat!» — üç şey tek hükümde toplanmıştır." + R_TR},
 "tokens": [
  tok("وَقَوْلِ","qawl","noun",[J, "atf-nasaq", "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ عَلَى قَوْلِهِ مَجْرُورٌ مُضَافٌ.", "«and the saying» — joined onto the citation before it.", "«ve … sözü» — önceki iktibasa atfedilmiş.",
      segments=[seg("وَ","wa","conj"), seg("قَوْلِ","qawl","noun")]),
  tok("أَبِي","ab","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — of the five nouns, jarr by the ya, itself annexed.", "«Ebû» — beş isimden, yâ ile mecrûr, muzâf."),
  tok("الْعَتَاهِيَةِ","abu-l-atahiya","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الْعَتَاهِيَةِ، شَاعِرُ الزُّهْدِ.", "«al-ʿAtahiya» — Abu l-ʿAtahiya, the poet of renunciation.", "«el-Atâhiye» — Ebü'l-Atâhiye, zühd şairi.", punct=":"),
  tok("إِنَّ","inna","part",[J, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«verily».", "«muhakkak»."),
  tok("الشَّبَابَ","shabab","noun",[J, "inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«youth» — the ism of inna.", "«gençlik» — inne'nin ismi."),
  wa_conj("وَالْفَرَاغَ","faragh","noun",[J, "atf-nasaq"], "الْفَرَاغَ مَعْطُوفٌ مَنْصُوبٌ.", "«and idleness» — joined.", "«ve boşluk» — ma'tûf."),
  wa_conj("وَالْجِدَةَ","jida","noun",[J, "atf-nasaq"], "الْجِدَةَ مَعْطُوفٌ مَنْصُوبٌ — الْجِدَةُ: الْغِنَى.", "«and wealth» — joined; jida is affluence.", "«ve zenginlik» — ma'tûf; cide: varlık.", punct="*"),
  tok("مَفْسَدَةٌ","mafsada","noun",[J, "inna-wa-akhawatuha", "masdar"], "خَبَرُ إِنَّ مَرْفُوعٌ — مَصْدَرٌ مِيمِيٌّ: الْحُكْمُ الْوَاحِدُ.", "«a ruin» — the khabar of inna, a mimi masdar: the one ruling.", "«fesat kaynağı» — inne'nin haberi, mîmî masdar: tek hüküm."),
  tok("لِلْمَرْءِ","mar","noun",[J, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَفْسَدَةٍ.", "«for a man».", "«kişi için».", segments=[seg("لِ","li","part"), seg("الْمَرْءِ","mar","noun")]),
  tok("أَيُّ","ayy","pron",[J, "naat-sifa", "idafa-definiteness"], "نَعْتٌ لِمَفْسَدَةٍ مَرْفُوعٌ مُضَافٌ — أَيُّ لِلتَّعْظِيمِ.", "«what a» — a na't of the ruin, annexed; ayy of magnifying.", "«hem ne» — fesadın na'ti, muzâf; ta'zîm için eyy."),
  tok("مَفْسَدَةٍ","mafsada","noun",[J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ruin».", "«fesat».", punct=".")]})
S[-1]["badi"] = [{"kind": "jam", "set": [ix(S[-1], "الشَّبَابَ"), ix(S[-1], "وَالْفَرَاغَ"), ix(S[-1], "وَالْجِدَةَ")], "word": ix(S[-1], "مَفْسَدَةٌ")}]

# ----------- s4 — the tafriq (RESTORED matn)
S.append({"id": "s4", "translation": {
 "en": "Among them is the TAFRIQ: to strike a DIFFERENCE between two things of ONE KIND, in praise or otherwise." + R_EN,
 "tr": "Onlardan biri TEFRÎKTİR: methde yahut başkasında, AYNI CİNSTEN iki şey arasına bir FARK koymak." + R_TR},
 "tokens": [
  minha(T),
  tok("التَّفْرِيقُ","tafriq","noun",[T, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ فَرَّقَ.", "«the tafriq» — the masdar of فَرَّقَ.", "«tefrîk» — فَرَّقَ'nin masdarı."),
  wahuwa(T),
  tok("إِيقَاعُ","iqa","noun",[T, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ أَوْقَعَ.", "«the striking» — the khabar, mudaf; masdar of أَوْقَعَ.", "«koymak» — haber, muzâf; أَوْقَعَ'nin masdarı."),
  tok("تَبَايُنٍ","tabayun","noun",[T, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَبَايَنَ.", "«of a difference» — mudaf ilayh; masdar of تَبَايَنَ.", "«bir farkın» — muzâfun ileyh; تَبَايَنَ'nin masdarı."),
  tok("بَيْنَ","bayna","noun",[T, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«between».", "«arasına»."),
  tok("أَمْرَيْنِ","amr","noun",[T, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two things» — a dual, jarr by the ya.", "«iki şey» — tesniye, yâ ile mecrûr."),
  tok("مِنْ","min","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("نَوْعٍ","naw","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«a kind».", "«cinsten»."),
  tok("وَاحِدٍ","wahid","noun",[T, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«one» — a na't.", "«bir» — na't."),
  tok("فِي","fi","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْمَدْحِ","madh","noun",[T, "huruf-jarr", "masdar"], "مَجْرُورٌ — مَصْدَرُ مَدَحَ.", "«praise».", "«medihte»."),
  tok("أَوْ","aw","part",[T, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("غَيْرِهِ","ghayr","noun",[T, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«otherwise» — joined, annexed to its pronoun.", "«başkasında» — ma'tûf, zamirine muzâf.",
      segments=[seg("غَيْرِ","ghayr","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s5 — al-Watwat, first bayt
S.append({"id": "s5", "translation": {
 "en": "As Rashid al-Din al-Watwat says: «The bounty of the CLOUD in spring-time • is NOT like the bounty of the PRINCE on a day of giving»." + R_EN,
 "tr": "Reşîdüddîn el-Vatvât'ın dediği gibi: «Bahar vaktinde BULUTUN bağışı • cömertlik gününde EMÎRİN bağışı GİBİ DEĞİLDİR»." + R_TR},
 "tokens": [
  kaqawl(T),
  tok("الْوَطْوَاطِ","watwat","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — رَشِيدُ الدِّينِ الْوَطْوَاطُ، شَاعِرُ خُوَارِزْمَ.", "«al-Watwat» — Rashid al-Din, the poet of Khwarazm.", "«el-Vatvât» — Reşîdüddîn, Hârizm şairi.", punct=":"),
  tok("مَا","ma-nafiya","part",[T, "anwa-ma"], "مَا نَافِيَةٌ عَامِلَةٌ عَمَلَ لَيْسَ — الْحِجَازِيَّةُ.", "«not» — the Hijazi ma, working like لَيْسَ.", "«değil» — لَيْسَ gibi amel eden Hicâzî mâ."),
  tok("نَوَالُ","nawal","noun",[T, "anwa-ma", "idafa-definiteness"], "اسْمُ مَا مَرْفُوعٌ مُضَافٌ — النَّوَالُ: الْعَطَاءُ.", "«the bounty» — the ism of ma, annexed; nawal is a gift.", "«bağışı» — mâ'nın ismi, muzâf; nevâl: atâ."),
  tok("الْغَمَامِ","ghamam","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْأَمْرُ الْأَوَّلُ.", "«of the cloud» — the first of the two things.", "«bulutun» — iki şeyin ilki."),
  tok("وَقْتَ","waqt","noun",[T, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ.", "«in the time» — a zarf of time.", "«vaktinde» — zaman zarfı."),
  tok("رَبِيعٍ","rabi","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of spring».", "«baharın».", punct="*"),
  tok("كَنَوَالِ","nawal","noun",[T, "anwa-ma", "huruf-jarr", "idafa-definiteness"], "الْكَافُ حَرْفُ جَرٍّ، وَنَوَالِ مَجْرُورٌ مُضَافٌ — فِي مَحَلِّ نَصْبٍ خَبَرُ مَا.", "«like the bounty» — the kaf a jarr letter; the phrase stands in nasb as the khabar of ma.", "«bağışı gibi» — kâf cer harfi; câr-mecrûr mâ'nın haberi yerinde.",
      segments=[seg("كَ","ka","part"), seg("نَوَالِ","nawal","noun")]),
  tok("الْأَمِيرِ","amir","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْأَمْرُ الثَّانِي مِنَ النَّوْعِ نَفْسِهِ.", "«of the prince» — the second thing, of the same kind.", "«emîrin» — aynı cinsten ikinci şey."),
  tok("يَوْمَ","yawm","noun",[T, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ.", "«on a day» — a zarf.", "«gününde» — zarf."),
  tok("سَخَاءِ","sakha","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — سُكِّنَ لِلْقَافِيَةِ.", "«of giving» — mudaf ilayh; the rhyme quiets its ending.", "«cömertliğin» — muzâfun ileyh; kafiye sonunu sükûna çevirir.", punct=".")]})
S[-1]["badi"] = [{"kind": "tafriq", "first": [ix(S[-1], "نَوَالُ"), ix(S[-1], "الْغَمَامِ")], "second": [ix(S[-1], "كَنَوَالِ"), ix(S[-1], "الْأَمِيرِ")]}]

# ----------- s6 — al-Watwat, second bayt
S.append({"id": "s6", "translation": {
 "en": "«For the bounty of the PRINCE is a purse of gold • and the bounty of the CLOUD a drop of water» — the difference struck between two bounties." + R_EN,
 "tr": "«Zira EMÎRİN bağışı bir kese altın • BULUTUN bağışı ise bir damla sudur» — iki bağış arasına konan fark." + R_TR},
 "tokens": [
  tok("فَنَوَالُ","nawal","noun",[T, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ لِلتَّعْلِيلِ، وَنَوَالُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ.", "«for the bounty» — the fa of reason; the mubtada, annexed.", "«zira … bağışı» — ta'lîl fâsı; mübtedâ, muzâf.",
      segments=[seg("فَ","fa","conj"), seg("نَوَالُ","nawal","noun")]),
  tok("الْأَمِيرِ","amir","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of the prince».", "«emîrin»."),
  tok("بَدْرَةُ","badra","noun",[T, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — الْبَدْرَةُ: كِيسُ الْمَالِ.", "«a purse» — the khabar; a badra is a purse of coin.", "«bir kese» — haber; bedre: para kesesi."),
  tok("عَيْنٍ","ayn","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْعَيْنُ هُنَا: الذَّهَبُ.", "«of gold» — ʿayn here is minted gold.", "«altın» — ayn burada: altın.", punct="*"),
  wa_conj("وَنَوَالُ","nawal","noun",[T, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "نَوَالُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ — جُمْلَةٌ مَعْطُوفَةٌ عَلَى جُمْلَةٍ.", "«and the bounty» — a second mubtada; a sentence joined on a sentence.", "«… bağışı ise» — ikinci mübtedâ; cümleye atfedilmiş cümle."),
  tok("الْغَمَامِ","ghamam","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of the cloud».", "«bulutun»."),
  tok("قَطْرَةُ","qatra","noun",[T, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«a drop» — the khabar.", "«bir damla» — haber."),
  tok("مَاءِ","ma-water","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — سُكِّنَ لِلْقَافِيَةِ.", "«of water» — the rhyme quiets its ending.", "«su» — kafiye sonunu sükûna çevirir.", punct=".")]})
S[-1]["badi"] = [{"kind": "tafriq", "first": [ix(S[-1], "فَنَوَالُ"), ix(S[-1], "الْأَمِيرِ")], "second": [ix(S[-1], "وَنَوَالُ"), ix(S[-1], "الْغَمَامِ")]}]

# ----------- s7 — the taqsim (RESTORED matn)
S.append({"id": "s7", "translation": {
 "en": "Among them is the TAQSIM: to NAME many things, then to ADD to each what belongs to it, one by one." + R_EN,
 "tr": "Onlardan biri TAKSÎMDİR: birden çok şeyi ANMAK, sonra her birine kendisine ait olanı tek tek EKLEMEK." + R_TR},
 "tokens": [
  minha(Q),
  tok("التَّقْسِيمُ","taqsim","noun",[Q, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ قَسَّمَ.", "«the taqsim» — the masdar of قَسَّمَ.", "«taksîm» — قَسَّمَ'nin masdarı."),
  wahuwa(Q),
  tok("ذِكْرُ","dhikr","noun",[Q, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«the naming» — the khabar, annexed.", "«anmak» — haber, muzâf."),
  tok("مُتَعَدِّدٍ","mutaaddid","noun",[Q, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of many things».", "«birden çok şeyi»."),
  tok("ثُمَّ","thumma","part",[Q, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then».", "«sonra»."),
  tok("إِضَافَةُ","idafa","noun",[Q, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ عَلَى ذِكْرُ مَرْفُوعٌ مُضَافٌ.", "«the adding» — joined onto the naming.", "«eklemek» — anmaya atfedilmiş."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the relative, annexed.", "«… olanı» — ism-i mevsûl, muzâfun ileyh."),
  tok("لِكُلٍّ","kull","noun",[Q, "huruf-jarr", "ism-mawsul"], "جَارٌّ وَمَجْرُورٌ — صِلَةُ الْمَوْصُولِ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ.", "«to each» — the sila; the tanwin stands for a dropped mudaf ilayh.", "«her birine» — sıla; tenvin hazfedilen muzâfun ileyhin ıvazı.",
      segments=[seg("لِ","li","part"), seg("كُلٍّ","kull","noun")]),
  tok("إِلَيْهِ","ila","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِإِضَافَةُ.", "«to it».", "«ona».", segments=[seg("إِلَيْ","ila","part"), seg("هِ","pron-3ms","pron")]),
  tok("عَلَى","ala","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  tok("التَّعْيِينِ","tayin","noun",[Q, "huruf-jarr", "masdar"], "مَجْرُورٌ — أَيْ مُعَيَّنًا لَا مُجْمَلًا.", "«specification» — each named, not lumped.", "«tayin» — belirleyerek, toptan değil.", punct=".")]})

# ----------- s8 — Jarir b. ʿAbd al-Masih (two bayts, one taqsim)
S.append({"id": "s8", "translation": {
 "en": "As Jarir b. ʿAbd al-Masih says: «None abides the wrong that is meant for him • but the two most abject: the tribe's DONKEY and the TENT-PEG; • THIS one is tied by its rope to humiliation • and THAT one is struck on the head and no one pities it» — the two named, then to each its own." + R_EN,
 "tr": "Cerîr b. Abdülmesîh'in dediği gibi: «Kendisine kastedilen zulme kimse katlanmaz • ancak iki zelil katlanır: kabilenin EŞEĞİ ile KAZIK; • ŞU, ipiyle zillete bağlanmıştır • ŞU ise başı yarılır da kimse ona acımaz» — ikisi anılmış, sonra her birine kendininki verilmiş." + R_TR},
 "tokens": [
  kaqawl(Q),
  tok("جَرِيرِ","jarir-ibn-abd-al-masih","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَرِيرُ بْنُ عَبْدِ الْمَسِيحِ، الْمُتَلَمِّسُ، شَاعِرٌ جَاهِلِيٌّ.", "«Jarir» — b. ʿAbd al-Masih, al-Mutalammis, a pre-Islamic poet.", "«Cerîr» — b. Abdülmesîh, el-Mütelemmis, Câhiliye şairi."),
  tok("بْنِ","ibn","noun",[Q, "naat-sifa", "idafa-definiteness"], "نَعْتٌ لِجَرِيرٍ مَجْرُورٌ مُضَافٌ.", "«son» — a na't of Jarir, annexed.", "«oğlu» — Cerîr'in na'ti, muzâf."),
  tok("عَبْدِ","abd","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«ʿAbd».", "«Abd»."),
  tok("الْمَسِيحِ","masih","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Masih».", "«el-Mesîh».", punct=":"),
  tok("وَلَا","la-nafiya","part",[Q, "la-nafiya-lil-jins"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَا نَافِيَةٌ.", "«and not» — the negation.", "«ve … -maz» — nefiy.", segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُقِيمُ","aqama","verb",[Q, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَقَامَ عَلَى الشَّيْءِ: ثَبَتَ عَلَيْهِ.", "«abides» — to stay upon a thing.", "«katlanır» — bir şey üzere durmak."),
  tok("عَلَى","ala","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  tok("ضَيْمٍ","daym","noun",[Q, "huruf-jarr"], "مَجْرُورٌ — الضَّيْمُ: الظُّلْمُ.", "«a wrong» — daym is oppression.", "«zulme» — daym: zulüm."),
  tok("يُرَادُ","arada","verb",[Q, "naat-sifa", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ لِضَيْمٍ؛ نَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«that is meant» — the passive; the clause is a na't of the wrong; the deputy is concealed.", "«kastedilen» — meçhul; cümle zulmün na'ti; nâib-i fâil gizli."),
  tok("بِهِ","bi","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for him».", "«ona».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct="*"),
  tok("إِلَّا","illa","part",[Q, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except» — the emptied exception.", "«ancak» — müferrağ istisnâ."),
  tok("الْأَذَلَّانِ","adhall","noun",[Q, "fail", "al-muthanna", "ism-tafdil"], "فَاعِلُ يُقِيمُ مَرْفُوعٌ بِالْأَلِفِ — مُثَنَّى أَذَلَّ.", "«the two most abject» — the doer, raf' by the alif; the dual of the elative.", "«iki zelil» — fâil, elif ile merfû; ism-i tafdîlin tesniyesi."),
  tok("عَيْرُ","ayr","noun",[Q, "badal", "idafa-definiteness"], "بَدَلٌ مِنَ الْأَذَلَّانِ مَرْفُوعٌ مُضَافٌ — الْأَمْرُ الْأَوَّلُ الْمَذْكُورُ.", "«the donkey» — a badal of the two; the first thing named.", "«eşeği» — ikisinden bedel; anılan ilk şey."),
  tok("الْحَيِّ","hayy","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْحَيُّ: الْقَبِيلَةُ.", "«of the tribe» — hayy is the clan.", "«kabilenin» — hayy: kabile."),
  wa_conj("وَالْوَتَدُ","watad","noun",[Q, "atf-nasaq"], "الْوَتَدُ مَعْطُوفٌ مَرْفُوعٌ — الْأَمْرُ الثَّانِي.", "«and the tent-peg» — joined; the second thing.", "«ve kazık» — ma'tûf; ikinci şey.", punct="*"),
  tok("هَذَا","hadha","pron",[Q, "asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ — إِشَارَةٌ إِلَى الْأَوَّلِ.", "«this» — the mubtada; points to the first.", "«şu» — mübtedâ; ilkine işaret."),
  tok("عَلَى","ala","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْخَسْفِ","khasf","noun",[Q, "huruf-jarr"], "مَجْرُورٌ — الْخَسْفُ: الذُّلُّ.", "«humiliation».", "«zillete»."),
  tok("مَرْبُوطٌ","marbut","noun",[Q, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ رَبَطَ: حُكْمُ الْأَوَّلِ.", "«tied» — the khabar; the first thing's own ruling.", "«bağlanmış» — haber; ilkinin hükmü."),
  tok("بِرُمَّتِهِ","rumma","noun",[Q, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ إِلَى الْهَاءِ — الرُّمَّةُ: قِطْعَةُ حَبْلٍ بَالِيَةٍ.", "«by its rope» — rumma is a frayed length of rope.", "«ipiyle» — rümme: eski ip parçası.",
      segments=[seg("بِ","bi","part"), seg("رُمَّتِ","rumma","noun"), seg("هِ","pron-3ms","pron")], punct="*"),
  tok("وَذَا","dha","pron",[Q, "atf-nasaq", "asma-al-ishara", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَذَا اسْمُ إِشَارَةٍ مُبْتَدَأٌ — إِشَارَةٌ إِلَى الثَّانِي.", "«and that» — a second mubtada; points to the second.", "«şu ise» — ikinci mübtedâ; ikincisine işaret.",
      segments=[seg("وَ","wa","conj"), seg("ذَا","dha","pron")]),
  tok("يُشَجُّ","shajja","verb",[Q, "mubtada-khabar", "naib-al-fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ خَبَرٌ — شَجَّ رَأْسَهُ: شَقَّهُ.", "«is struck on the head» — the passive; the clause is the khabar: the second thing's own ruling.", "«başı yarılır» — meçhul; cümle haber: ikincisinin hükmü."),
  tok("فَلَا","la-nafiya","part",[Q, "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not».", "«ve … -maz».", segments=[seg("فَ","fa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَرْثِي","ratha","verb",[Q, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«pities» — raf' estimated on the ya.", "«acır» — yâ üzerinde takdîrî damme."),
  tok("لَهُ","lahu","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«it».", "«ona».", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("أَحَدُ","ahad","noun",[Q, "fail"], "فَاعِلٌ مَرْفُوعٌ — سُكِّنَ لِلْقَافِيَةِ.", "«anyone» — the doer; the rhyme quiets its ending.", "«kimse» — fâil; kafiye sonunu sükûna çevirir.", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "first": [ix(S[-1], "عَيْرُ"), ix(S[-1], "وَالْوَتَدُ")], "second": [ix(S[-1], "هَذَا"), ix(S[-1], "وَذَا")]}]

# ----------- s9 — the three side by side (RESTORED summary)
S.append({"id": "s9", "translation": {
 "en": "So in the jamʿ there is a gathering under one ruling; in the tafriq a difference between two of a kind; and in the taqsim the return of each thing to what is its own." + R_EN,
 "tr": "Demek cem'de tek hükümde toplanma, tefrîkte aynı cinsten ikisi arasında fark, taksîmde ise her şeyin kendine ait olana döndürülmesi vardır." + R_TR},
 "tokens": [
  tok("فَفِي","fi","part",[J, "huruf-jarr", "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«so in» — the jarr phrase is a fronted khabar.", "«demek … -de» — câr-mecrûr takdim edilmiş haber.", segments=[seg("فَ","fa","conj"), seg("فِي","fi","part")]),
  tok("الْجَمْعِ","jam","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«the jamʿ».", "«cem'de»."),
  tok("اجْتِمَاعٌ","ijtima","noun",[J, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a gathering» — the delayed mubtada.", "«toplanma» — muahhar mübtedâ."),
  tok("فِي","fi","part",[J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«under».", "«-de»."),
  tok("حُكْمٍ","hukm","noun",[J, "huruf-jarr"], "مَجْرُورٌ.", "«one ruling».", "«tek hükümde».", punct="،"),
  tok("وَفِي","fi","part",[T, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in».", "«… -de ise».", segments=[seg("وَ","wa","conj"), seg("فِي","fi","part")]),
  tok("التَّفْرِيقِ","tafriq","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«the tafriq».", "«tefrîkte»."),
  tok("تَبَايُنٌ","tabayun","noun",[T, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a difference».", "«bir fark»."),
  tok("بَيْنَ","bayna","noun",[T, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«between».", "«arasında»."),
  tok("الْمُتَّفِقَيْنِ","muttafiq","noun",[T, "idafa-definiteness", "al-muthanna", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — اسْمُ فَاعِلِ اتَّفَقَ، مُثَنًّى: الْأَمْرَانِ الْمُتَّفِقَانِ فِي النَّوْعِ.", "«two of a kind» — the dual participle: the two things agreeing in kind.", "«aynı cinsten ikisi» — ism-i fâilin tesniyesi.", punct="،"),
  tok("وَفِي","fi","part",[Q, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in».", "«… -de ise».", segments=[seg("وَ","wa","conj"), seg("فِي","fi","part")]),
  tok("التَّقْسِيمِ","taqsim","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«the taqsim».", "«taksîmde»."),
  tok("رَدُّ","radd","noun",[Q, "mubtada-khabar", "idafa-definiteness", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ.", "«the return» — the delayed mubtada, annexed.", "«döndürülmesi» — muahhar mübtedâ, muzâf."),
  tok("كُلِّ","kull","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«of each».", "«her»."),
  tok("أَمْرٍ","amr","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«thing».", "«şeyin»."),
  tok("إِلَى","ila","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what».", "«… olana»."),
  tok("لَهُ","lahu","part",[Q, "huruf-jarr", "ism-mawsul"], "جَارٌّ وَمَجْرُورٌ — صِلَةُ الْمَوْصُولِ.", "«is its own» — the sila.", "«kendine ait» — sıla.", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ---------------------------------------------------------------- glossary
def FG(*ks): return {k: find_gloss(k) for k in ks}
GLOSS_ADD = FG("ab", "abd", "ahad", "ala", "amir", "amr", "an", "arada", "aqama", "aw", "ayn", "ayy", "bayna", "bi", "dhikr", "dunya", "fa", "fi", "ghayr", "hadha", "hayat",
               "hayy", "hiya", "hukm", "huwa", "ibn", "idafa", "illa", "inna", "jam", "kull", "ka", "la-nafiya", "lahu", "li", "ma-mawsula", "ma-nafiya", "mal",
               "mar", "min", "mutaaddid", "naw", "qawl", "rabi", "shabab", "faragh", "tayin", "thumma", "wa", "wahid", "yawm", "taala",
               "pron-3fs", "pron-3ms")
GLOSS_ADD.update({
 "ijtima": G("ijtima", "اجْتِمَاع", "ج م ع", "noun", "a gathering, a coming together (masdar of اجْتَمَعَ)", "toplanma, bir araya gelme (اجْتَمَعَ'nin masdarı)", 4),
 "nawal": G("nawal", "نَوَال", "ن و ل", "noun", "bounty, a gift given (masdar of نَالَ «to give»)", "bağış, ihsan (نَالَ «vermek» fiilinin masdarı)", 5),
 "radd": G("radd", "رَدّ", "ر د د", "noun", "returning, giving back (masdar of رَدَّ)", "geri verme, döndürme (رَدَّ'nin masdarı)", 3),
 "waqt": G("waqt", "وَقْت", "و ق ت", "noun", "time, a point of time", "vakit, zaman", 2, plural="أَوْقَات"),
 "zina": G("zina", "زِينَة", "ز ي ن", "noun", "adornment, ornament", "süs, ziynet", 3),
 "jamaa-gather": G("jamaa-gather", "جَمَعَ", "ج م ع", "verb", "to gather, to bring together (جَمَعَ يَجْمَعُ)", "toplamak, bir araya getirmek (جَمَعَ يَجْمَعُ)", 2, form="I"),
 "banun": G("banun", "بَنُونَ", "ب ن و", "noun", "sons (the plural of ابْن attached to the sound masculine plural)", "oğullar (ابْن'in cem-i müzekker-i sâlime mülhak çoğulu)", 3),
 "jida": G("jida", "جِدَة", "و ج د", "noun", "affluence, wealth (masdar of وَجَدَ in the sense «to be rich»)", "zenginlik, varlık (وَجَدَ'nin «zengin olmak» mânâsındaki masdarı)", 5),
 "mafsada": G("mafsada", "مَفْسَدَة", "ف س د", "noun", "a cause of ruin, a source of corruption (masdar mimi of فَسَدَ)", "fesat kaynağı (فَسَدَ'nin mîmî masdarı)", 4),
 "abu-l-atahiya": G("abu-l-atahiya", "الْعَتَاهِيَة", None, "propn", "Abu l-ʿAtahiya — Ismaʿil b. al-Qasim, the ʿAbbasid poet of renunciation (d. 210/826)", "Ebü'l-Atâhiye — İsmâil b. Kâsım, Abbâsî zühd şairi (ö. 210/826)", 6),
 "tafriq": G("tafriq", "تَفْرِيق", "ف ر ق", "noun", "tafriq — striking a difference between two things of one kind (masdar of فَرَّقَ)", "tefrîk — aynı cinsten iki şey arasına fark koymak (فَرَّقَ'nin masdarı)", 6),
 "iqa": G("iqa", "إِيقَاع", "و ق ع", "noun", "striking, bringing about (masdar of أَوْقَعَ)", "koymak, vâki kılmak (أَوْقَعَ'nin masdarı)", 5),
 "tabayun": G("tabayun", "تَبَايُن", "ب ي ن", "noun", "a difference, a divergence (masdar of تَبَايَنَ)", "fark, ayrılık (تَبَايَنَ'nin masdarı)", 5),
 "madh": G("madh", "مَدْح", "م د ح", "noun", "praise (masdar of مَدَحَ)", "medih, övgü (مَدَحَ'nin masdarı)", 3),
 "watwat": G("watwat", "الْوَطْوَاط", None, "propn", "al-Watwat — Rashid al-Din Muhammad, the Khwarazmian poet and secretary (d. 573/1177)", "el-Vatvât — Reşîdüddîn Muhammed, Hârizmli şair ve kâtip (ö. 573/1177)", 6),
 "ghamam": G("ghamam", "غَمَام", "غ م م", "noun", "cloud", "bulut", 3),
 "sakha": G("sakha", "سَخَاء", "س خ و", "noun", "generosity, open-handed giving", "cömertlik, sehâ", 4),
 "badra": G("badra", "بَدْرَة", "ب د ر", "noun", "a purse of coin (ten thousand dirhams)", "para kesesi, bedre (on bin dirhem)", 5),
 "qatra": G("qatra", "قَطْرَة", "ق ط ر", "noun", "a drop", "damla", 2),
 "taqsim": G("taqsim", "تَقْسِيم", "ق س م", "noun", "taqsim — naming many things and then giving each its own (masdar of قَسَّمَ)", "taksîm — birden çok şeyi anıp sonra her birine kendininkini vermek (قَسَّمَ'nin masdarı)", 6),
 "jarir-ibn-abd-al-masih": G("jarir-ibn-abd-al-masih", "جَرِير", None, "propn", "Jarir b. ʿAbd al-Masih — al-Mutalammis, the pre-Islamic poet of Bakr, maternal uncle of Tarafa", "Cerîr b. Abdülmesîh — el-Mütelemmis, Bekr'in Câhiliye şairi, Tarafe'nin dayısı", 6),
 "masih": G("masih", "الْمَسِيح", None, "propn", "al-Masih (in the name ʿAbd al-Masih)", "el-Mesîh (Abdülmesîh adında)", 6),
 "daym": G("daym", "ضَيْم", "ض ي م", "noun", "wrong, oppression", "zulüm, haksızlık", 5),
 "adhall": G("adhall", "أَذَلّ", "ذ ل ل", "noun", "more abject, lowlier (the elative of ذَلِيل)", "daha zelil (ذَلِيل'in ism-i tafdîli)", 4),
 "ayr": G("ayr", "عَيْر", "ع ي ر", "noun", "a donkey, an ass", "eşek, yaban eşeği", 4),
 "watad": G("watad", "وَتَد", "و ت د", "noun", "a tent-peg, a stake", "kazık, çadır kazığı", 4),
 "khasf": G("khasf", "خَسْف", "خ س ف", "noun", "humiliation, abasement", "zillet, aşağılanma", 5),
 "marbut": G("marbut", "مَرْبُوط", "ر ب ط", "noun", "tied, bound (ism mafʿul of رَبَطَ)", "bağlanmış (رَبَطَ'nin ism-i mef'ûlü)", 3),
 "rumma": G("rumma", "رُمَّة", "ر م م", "noun", "a frayed length of rope", "eski ip parçası", 5),
 "shajja": G("shajja", "شَجَّ", "ش ج ج", "verb", "to split the head, to wound the scalp (doubled: شَجَّ يَشُجُّ)", "başını yarmak (muzâaf: شَجَّ يَشُجُّ)", 5, form="I"),
 "ratha": G("ratha", "رَثَى", "ر ث ي", "verb", "to pity, to mourn (رَثَى يَرْثِي)", "acımak, ağıt yakmak (رَثَى يَرْثِي)", 4, form="I"),
 "dha": G("dha", "ذَا", None, "pron", "that (the demonstrative without the ha of alerting)", "şu (tenbih hâsı olmayan işaret ismi)", 3),
 "muttafiq": G("muttafiq", "مُتَّفِق", "و ف ق", "noun", "agreeing, alike (ism fa'il of اتَّفَقَ)", "uyuşan, benzeşen (اتَّفَقَ'nin ism-i fâili)", 4),
})
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
# جَمَعَ يَجْمَعُ (bab fataha) — the passive stored for the chapter's own يُجْمَعَ; stems WITHOUT their sukun, the amr with its wasl vowel
put_morph(mo, "jamaa-gather", _sg.sound1("fataha", "جَمَع", "جْمَع", "اِجْمَع", "جَمْع", "جَامِع", maful="مَجْمُوع", pmz="جُمِعَ", pmd="يُجْمَعُ"))
# شَجَّ يَشُجُّ — a geminate of bab nasara: the contracted stems, the fakk before a sakin ending, the amr contracted (شُجَّ) and its fem-plural with the wasl alif
put_morph(mo, "shajja", _sg.entry(_sg.BABS["nasara"][0] + " — مُضَاعَفٌ", _sg.BABS["nasara"][1], "شَجّ", "شَاجّ", _sg.mazi14("شَجّ", "شَجَج"), _sg.mudari14("َ", "شُجّ", "شْجُج"),
                                 ["شُجَّ", "شُجَّا", "شُجُّوا", "شُجِّي", "شُجَّا", "اُشْجُجْنَ"], "يَشُجَّ", "يَشُجَّ", "تَشُجَّ", "مَشْجُوج", "شُجَّ", "يُشَجُّ",
                                 note="مُضَاعَفٌ مِنْ بَابِ نَصَرَ: شَجَّ يَشُجُّ — شَجَجْتُ، يَشْجُجْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ."))
# رَثَى يَرْثِي — naqis yaʾi of bab daraba (رَمَى's model): the alif-type mazi, the amr اِرْثِ
put_morph(mo, "ratha", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "رَثَ", "رْث", "i", "اِرْث", "رِثَاء", "رَاثٍ (الرَّاثِي)", "مَرْثِيّ", "رُثِيَ", "يُرْثَى"))
# a verb copied in from another package brings its paradigm with it (the release gate wants every glossary verb conjugated)
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_J = {
 "id": "jam",
 "title": {"ar": "الْجَمْعُ — أَنْ يُجْمَعَ بَيْنَ مُتَعَدِّدٍ فِي حُكْمٍ", "en": "The jamʿ — many things gathered under one ruling", "tr": "Cem' — birden çok şeyin tek hükümde toplanması"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الجمع: أن يجمع بين متعدد في حكم"],
 "question": {
  "en": ["How many things, and how many rulings? «Wealth and sons are the adornment of this life» — two things, ONE ruling. «Youth, idleness and wealth are a ruin for a man» — three things, one ruling. That is the JAMʿ.",
         "What does the engine look for? A list joined by the waw that stands as ONE mubtada (or one ism of inna) and takes ONE khabar — DabtEngine's own seats, read back.",
         "What is it not? Not a taqsim — there each thing gets its own; here the ruling is shared."],
  "tr": ["Kaç şey, kaç hüküm? «Mal ve oğullar dünya hayatının süsüdür» — iki şey, TEK hüküm. «Gençlik, boşluk ve zenginlik kişi için fesattır» — üç şey, tek hüküm. CEM' budur.",
         "Motor neye bakar? Vâv ile bağlanmış, TEK mübtedâ (yahut inne'nin tek ismi) olarak duran ve TEK haber alan bir liste — DabtEngine'in kendi koltukları, geri okunmuş.",
         "Ne değildir? Taksîm değildir — orada her şey kendininkini alır; burada hüküm ortaktır."]},
 "plain": {
  "en": "The jamʿ: several things are named and one ruling covers them all — «wealth and sons are the adornment of this life». The engine reads a wāw-joined list standing as one subject with one predicate.",
  "tr": "Cem': birkaç şey anılır ve tek bir hüküm hepsini kuşatır — «mal ve oğullar dünya hayatının süsüdür». Motor, tek özne olarak duran vâvlı bir listeyi tek yüklemiyle okur."},
 "explanation": {
  "en": "The JAMʿ is أَنْ يُجْمَعَ بَيْنَ مُتَعَدِّدٍ فِي حُكْمٍ — to gather many things under ONE ruling. الْمَالُ وَالْبَنُونَ زِينَةُ الْحَيَاةِ الدُّنْيَا (18:46): wealth and sons, two mubtadas joined by the waw, and one khabar — adornment — over both. Abu l-ʿAtahiya gathers three: إِنَّ الشَّبَابَ وَالْفَرَاغَ وَالْجِدَةَ مَفْسَدَةٌ لِلْمَرْءِ — youth, idleness and wealth are one ruin. The figure is in the ARITHMETIC: n things, one ruling.\n\nWHAT THE ENGINE CLAIMS: the BadiEngine reads the jamʿ off DabtEngine's seats — an atf list whose head is the mubtada (or the ism of إِنَّ) and whose members all hang on one khabar; two members or more, one predicate. It names the set and the ruling word. It cannot judge whether the gathering is apt — that is the poet's choice, not the syntax's.",
  "tr": "CEM' أَنْ يُجْمَعَ بَيْنَ مُتَعَدِّدٍ فِي حُكْمٍ'dir — birden çok şeyi TEK hükümde toplamak. الْمَالُ وَالْبَنُونَ زِينَةُ الْحَيَاةِ الدُّنْيَا (Kehf 18:46): mal ve oğullar, vâv ile bağlanmış iki mübtedâ, ve ikisini de kuşatan tek haber — süs. Ebü'l-Atâhiye üçünü toplar: إِنَّ الشَّبَابَ وَالْفَرَاغَ وَالْجِدَةَ مَفْسَدَةٌ لِلْمَرْءِ — gençlik, boşluk ve zenginlik tek fesattır. Sanat ARİTMETİKtedir: n şey, tek hüküm.\n\nMOTORUN İDDİASI: BadiEngine cem'i DabtEngine'in koltuklarından okur — başı mübtedâ (yahut إِنَّ'nin ismi) olan ve üyeleri tek habere asılan bir atıf listesi; iki yahut daha çok üye, tek yüklem. Kümeyi ve hüküm kelimesini adlandırır. Toplamanın yerinde olup olmadığına hükmedemez — o şairin seçimidir, sentaksın değil."},
 "examples": [
  {"ar": "الْمَالُ وَالْبَنُونَ زِينَةُ الْحَيَاةِ الدُّنْيَا", "en": "18:46 — two things, one ruling.", "tr": "Kehf 18:46 — iki şey, tek hüküm.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "إِنَّ الشَّبَابَ وَالْفَرَاغَ وَالْجِدَةَ * مَفْسَدَةٌ لِلْمَرْءِ أَيُّ مَفْسَدَةٍ", "en": "Abu l-ʿAtahiya — three things, one ruling.", "tr": "Ebü'l-Atâhiye — üç şey, tek hüküm.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "أَنْ يُجْمَعَ بَيْنَ مُتَعَدِّدٍ فِي حُكْمٍ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s1"}],
 "commonMistakes": [
  {"wrong": "«Her vâvlı liste cem' sanatıdır»",
   "right": "«Cem', listenin TEK hükümde toplanmasıdır; hüküm dağılıyorsa taksîmdir»",
   "why": {"en": "A list is syntax; the jamʿ is the one ruling that binds it — a list whose members each get their own ruling is a taqsim.", "tr": "Liste sentakstır; cem', onu bağlayan tek hükümdür — her üyesi kendi hükmünü alan liste taksîmdir."}}],
 "relatedNotes": ["tafriq", "taqsim", "atf-nasaq", "ilm-al-badi", "laff-wa-nashr"]}

NOTE_T = {
 "id": "tafriq",
 "title": {"ar": "التَّفْرِيقُ — إِيقَاعُ تَبَايُنٍ بَيْنَ أَمْرَيْنِ مِنْ نَوْعٍ وَاحِدٍ", "en": "The tafriq — a difference struck between two things of one kind", "tr": "Tefrîk — aynı cinsten iki şey arasına konan fark"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التفريق: إيقاع تباين بين أمرين من نوع واحد في المدح أو غيره"],
 "question": {
  "en": ["Are the two things of ONE KIND, and is their LIKENESS DENIED? The cloud's bounty and the prince's bounty are both «bounty» — and «the bounty of the cloud in spring is NOT like the bounty of the prince». That is the TAFRIQ.",
         "Where is the difference stated? In the next line: the prince's bounty is a purse of gold, the cloud's a drop of water — the two nawals set apart.",
         "What does the engine look for? A negated likening (مَا … كَ …) whose two ends share a head word, or two parallel nominal sentences that give the same head two different predicates."],
  "tr": ["İki şey AYNI CİNSTEN mi, ve BENZERLİKLERİ İNKÂR mı ediliyor? Bulutun bağışı da emîrin bağışı da «bağış» — ve «baharda bulutun bağışı emîrin bağışı GİBİ DEĞİL». TEFRÎK budur.",
         "Fark nerede söylenir? Sonraki mısrada: emîrin bağışı bir kese altın, bulutunki bir damla su — iki nevâl ayrılmış.",
         "Motor neye bakar? İki ucu aynı baş kelimeyi paylaşan nefyedilmiş bir teşbih (مَا … كَ …), yahut aynı başa iki farklı yüklem veren iki paralel isim cümlesi."]},
 "plain": {
  "en": "The tafriq: two things of the same kind are set apart — «the cloud's bounty in spring is not like the prince's bounty on a day of giving; the prince gives a purse of gold, the cloud a drop of water». The engine reads the denied likeness and the parallel sentences.",
  "tr": "Tefrîk: aynı cinsten iki şey birbirinden ayrılır — «baharda bulutun bağışı, cömertlik gününde emîrin bağışı gibi değildir; emîr bir kese altın verir, bulut bir damla su». Motor inkâr edilen benzerliği ve paralel cümleleri okur."},
 "explanation": {
  "en": "The TAFRIQ is إِيقَاعُ تَبَايُنٍ بَيْنَ أَمْرَيْنِ مِنْ نَوْعٍ وَاحِدٍ فِي الْمَدْحِ أَوْ غَيْرِهِ — striking a DIFFERENCE between two things of ONE KIND, in praise or elsewhere. Al-Watwat: مَا نَوَالُ الْغَمَامِ وَقْتَ رَبِيعٍ كَنَوَالِ الْأَمِيرِ يَوْمَ سَخَاءٍ — the cloud's giving and the prince's giving are one kind of thing, «bounty», and the likeness between them is denied; then فَنَوَالُ الْأَمِيرِ بَدْرَةُ عَيْنٍ وَنَوَالُ الْغَمَامِ قَطْرَةُ مَاءٍ states the difference: a purse of gold against a drop of water. The figure needs the sameness of KIND — separating a cloud from a prince is no tafriq; separating two bounties is.\n\nWHAT THE ENGINE CLAIMS: the BadiEngine reads the tafriq off two receipts — the Hijazi مَا denying a كَ-likening whose two ends carry the same head word (نَوَال … كَنَوَالِ), and the pair of nominal sentences that give that head two different predicates. It names the two things; whether the difference flatters (madh) or not is the note's business.",
  "tr": "TEFRÎK إِيقَاعُ تَبَايُنٍ بَيْنَ أَمْرَيْنِ مِنْ نَوْعٍ وَاحِدٍ فِي الْمَدْحِ أَوْ غَيْرِهِ'dir — methde yahut başkasında AYNI CİNSTEN iki şey arasına FARK koymak. Vatvât: مَا نَوَالُ الْغَمَامِ وَقْتَ رَبِيعٍ كَنَوَالِ الْأَمِيرِ يَوْمَ سَخَاءٍ — bulutun vermesi ile emîrin vermesi aynı cins şeydir, «bağış», ve aralarındaki benzerlik inkâr edilir; sonra فَنَوَالُ الْأَمِيرِ بَدْرَةُ عَيْنٍ وَنَوَالُ الْغَمَامِ قَطْرَةُ مَاءٍ farkı söyler: bir kese altına karşı bir damla su. Sanat CİNS aynılığını ister — bulutu emîrden ayırmak tefrîk değildir; iki bağışı ayırmak tefrîktir.\n\nMOTORUN İDDİASI: BadiEngine tefrîki iki delilden okur — iki ucu aynı baş kelimeyi taşıyan (نَوَال … كَنَوَالِ) bir كَ-teşbihini nefyeden Hicâzî مَا, ve o başa iki farklı yüklem veren isim cümlesi çifti. İki şeyi adlandırır; farkın övgü (medih) olup olmadığı notun işidir."},
 "examples": [
  {"ar": "مَا نَوَالُ الْغَمَامِ وَقْتَ رَبِيعٍ * كَنَوَالِ الْأَمِيرِ يَوْمَ سَخَاءِ", "en": "al-Watwat — the likeness denied.", "tr": "Vatvât — benzerlik inkâr edildi.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "فَنَوَالُ الْأَمِيرِ بَدْرَةُ عَيْنٍ * وَنَوَالُ الْغَمَامِ قَطْرَةُ مَاءِ", "en": "al-Watwat — the difference stated.", "tr": "Vatvât — fark söylendi.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "إِيقَاعُ تَبَايُنٍ بَيْنَ أَمْرَيْنِ مِنْ نَوْعٍ وَاحِدٍ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"}],
 "commonMistakes": [
  {"wrong": "«İki şeyi ayırmak her zaman tefrîktir»",
   "right": "«Tefrîk, aynı CİNSTEN iki şeyi ayırmaktır; cinsleri farklı olanı ayırmak sanat değildir»",
   "why": {"en": "The definition says of one kind: the surprise is in parting two things that ought to be alike.", "tr": "Tarif «aynı cinsten» der: hayret, benzeşmesi gereken iki şeyin ayrılmasındadır."}}],
 "relatedNotes": ["jam", "taqsim", "tashbih", "anwa-ma", "ilm-al-badi"]}

NOTE_Q = {
 "id": "taqsim",
 "title": {"ar": "التَّقْسِيمُ — ذِكْرُ مُتَعَدِّدٍ ثُمَّ إِضَافَةُ مَا لِكُلٍّ إِلَيْهِ عَلَى التَّعْيِينِ", "en": "The taqsim — many things named, then to each its own", "tr": "Taksîm — birden çok şey anılır, sonra her birine kendininki verilir"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التقسيم: ذكر متعدد ثم إضافة ما لكل إليه على التعيين"],
 "question": {
  "en": ["Are the things NAMED first, and then does EACH get its own? «…but the two most abject: the donkey and the tent-peg — THIS one is tied by its rope to humiliation, THAT one is struck and no one pities it.» Two named, two rulings, each to its own. That is the TAQSIM.",
         "How is it unlike the laff wa-nashr? There the second list leaves the reader to match; here each ruling is pinned to its thing by name or pointer (هَذَا … وَذَا) — عَلَى التَّعْيِينِ.",
         "What does the engine look for? A list of n items, then n demonstratives or repeated heads, each opening its own clause, in order."],
  "tr": ["Şeyler önce ANILIYOR, sonra HER BİRİ kendininkini mi alıyor? «…ancak iki zelil: eşek ile kazık — ŞU ipiyle zillete bağlıdır, ŞU ise başı yarılır da kimse acımaz.» İkisi anıldı, iki hüküm, her biri kendininkine. TAKSÎM budur.",
         "Leff ü neşirden farkı? Orada ikinci liste eşleştirmeyi okuyucuya bırakır; burada her hüküm adıyla yahut işaretiyle (هَذَا … وَذَا) kendi şeyine iğnelenir — عَلَى التَّعْيِينِ.",
         "Motor neye bakar? n üyeli bir liste, sonra her biri kendi cümlesini açan n işaret ismi yahut tekrarlanan baş, sırayla."]},
 "plain": {
  "en": "The taqsim: several things are named and then each is given its own ruling, one by one — the donkey «is tied by its rope», the tent-peg «is struck and no one pities it». The engine reads the list and the pointers that hand each thing its clause.",
  "tr": "Taksîm: birkaç şey anılır, sonra her birine kendi hükmü tek tek verilir — eşek «ipiyle bağlıdır», kazık «başı yarılır da kimse acımaz». Motor listeyi ve her şeye cümlesini veren işaretleri okur."},
 "explanation": {
  "en": "The TAQSIM is ذِكْرُ مُتَعَدِّدٍ ثُمَّ إِضَافَةُ مَا لِكُلٍّ إِلَيْهِ عَلَى التَّعْيِينِ — naming many things, then adding to each what belongs to it, by SPECIFICATION. Al-Mutalammis: وَلَا يُقِيمُ عَلَى ضَيْمٍ يُرَادُ بِهِ إِلَّا الْأَذَلَّانِ عَيْرُ الْحَيِّ وَالْوَتَدُ — the two abject things named; then هَذَا عَلَى الْخَسْفِ مَرْبُوطٌ بِرُمَّتِهِ وَذَا يُشَجُّ فَلَا يَرْثِي لَهُ أَحَدُ — THIS (the donkey) tied by its frayed rope, THAT (the peg) beaten on the head. The demonstratives are the specification: each ruling is handed to its thing.\n\nWHAT THE ENGINE CLAIMS: the BadiEngine reads the taqsim off an atf list (the items) followed by as many clause-openers — demonstratives (هَذَا، ذَا) or the items' own heads repeated — each with its own predicate. It names the items and the pointer of each. The two wider uses of the name (naming a thing's states with what suits each; the complete division of a thing) come in the next chapter.",
  "tr": "TAKSÎM ذِكْرُ مُتَعَدِّدٍ ثُمَّ إِضَافَةُ مَا لِكُلٍّ إِلَيْهِ عَلَى التَّعْيِينِ'dir — birden çok şeyi anmak, sonra her birine kendisine ait olanı BELİRLEYEREK eklemek. Mütelemmis: وَلَا يُقِيمُ عَلَى ضَيْمٍ يُرَادُ بِهِ إِلَّا الْأَذَلَّانِ عَيْرُ الْحَيِّ وَالْوَتَدُ — iki zelil anıldı; sonra هَذَا عَلَى الْخَسْفِ مَرْبُوطٌ بِرُمَّتِهِ وَذَا يُشَجُّ فَلَا يَرْثِي لَهُ أَحَدُ — ŞU (eşek) eski ipiyle bağlı, ŞU (kazık) başından dövülür. İşaret isimleri belirlemenin kendisidir: her hüküm kendi şeyine verilir.\n\nMOTORUN İDDİASI: BadiEngine taksîmi bir atıf listesinden (üyeler) ve ardından o sayıda cümle açıcıdan okur — işaret isimleri (هَذَا، ذَا) yahut üyelerin tekrar edilen başları — her biri kendi yüklemiyle. Üyeleri ve her birinin işaretini adlandırır. Adın iki geniş kullanımı (bir şeyin hâllerini her birine uygun düşenle anmak; bir şeyin bütün kısımlarını tamamlamak) sonraki bâbda gelir."},
 "examples": [
  {"ar": "وَلَا يُقِيمُ عَلَى ضَيْمٍ يُرَادُ بِهِ * إِلَّا الْأَذَلَّانِ عَيْرُ الْحَيِّ وَالْوَتَدُ * هَذَا عَلَى الْخَسْفِ مَرْبُوطٌ بِرُمَّتِهِ * وَذَا يُشَجُّ فَلَا يَرْثِي لَهُ أَحَدُ", "en": "al-Mutalammis — two named, two rulings, each to its own.", "tr": "Mütelemmis — ikisi anıldı, iki hüküm, her biri kendininkine.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "ذِكْرُ مُتَعَدِّدٍ ثُمَّ إِضَافَةُ مَا لِكُلٍّ إِلَيْهِ عَلَى التَّعْيِينِ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«Taksîm ile leff ü neşr aynı şeydir»",
   "right": "«Leff ü neşirde eşleştirme okuyucuya bırakılır; taksîmde her hüküm adıyla yahut işaretiyle kendi şeyine verilir — عَلَى التَّعْيِينِ»",
   "why": {"en": "The definition's last words are the difference: by specification.", "tr": "Tarifin son sözü farkın kendisidir: belirleyerek."}}],
 "relatedNotes": ["jam", "tafriq", "laff-wa-nashr", "asma-al-ishara", "ilm-al-badi"]}

ADD_EN = (" Chapter 61 (lines ~4100-4130, sahifa 141-142) carries the jamʿ, the tafriq and the taqsim: the aya (s2, 18:46) and the verses of "
          "Abu l-ʿAtahiya (s3), Rashid al-Din al-Watwat (s5-s6) and Jarir b. ʿAbd al-Masih (s8) are the source's printed Arabic. s1, s4, s7 "
          "(the three definitions) and s9 (the closing summary) are RESTORED, NOT QUOTED: the source carries those steps only in its "
          "Ottoman-Turkish gloss, and the Arabic restores the matn's wording in the author's own idiom; each is marked «restored» in its "
          "translation. The examples carry `badi` frames (jam: the set and the one ruling; tafriq: the two things of one kind; taqsim: the "
          "items and the pointer of each).")
ADD_TR = (" Altmış birinci bâb (satır ~4100-4130, sahife 141-142) cem'i, tefrîki ve taksîmi taşır: âyet (s2 Kehf 18:46) ile Ebü'l-Atâhiye (s3), "
          "Reşîdüddîn el-Vatvât (s5-s6) ve Cerîr b. Abdülmesîh (s8) beyitleri kaynağın bastığı Arapçadır. s1, s4, s7 (üç tarif) ve s9 "
          "(kapanış özeti) ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini "
          "musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Örnekler `badi` çerçeveleri taşır "
          "(cem': küme ve tek hüküm; tefrîk: aynı cinsten iki şey; taksîm: üyeler ve her birinin işareti).")
write_out(61, S, TITLE, ADD_EN, ADD_TR, "4100-4130", GLOSS_ADD, notes=(NOTE_J, NOTE_T, NOTE_Q),
          related=(("laff-wa-nashr", ["taqsim", "jam"]), ("ilm-al-badi", ["jam", "tafriq", "taqsim"]), ("muqabala", ["tafriq"])))
report(61, S, GLOSS_ADD, (NOTE_J, NOTE_T, NOTE_Q))
