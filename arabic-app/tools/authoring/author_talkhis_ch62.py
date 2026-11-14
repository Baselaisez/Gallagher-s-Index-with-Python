# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 62: the JAMʿ WITH TAFRIQ, the JAMʿ WITH TAQSIM, the JAMʿ WITH BOTH, and the two other
taqsims (the states of a thing, each with what befits it; the exhaustive division). Source lines ~4130-4170 (sahifa 142-144).

  RESTORED (the source carries the step only in Turkish): s1, s3, s8, s12, s14 — the definitions, in the matn's own words.
  The verse and the ayas (s2, s4-s7, s9-s11, s13, s15) are the source's printed Arabic; the source prints خرشنة as حرشنة
  (a slip of the press: the fort is Kharshana) and وَالْأَرْضُ once as ولارض — both printed here in their known form.

  python3 tools/authoring/author_talkhis_ch62.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

C1 = C2 = C3 = "jam-maa-tafriq-taqsim"; Q = "taqsim"
TITLE = {"ar": "الْجَمْعُ مَعَ التَّفْرِيقِ وَالتَّقْسِيمِ، وَتَقْسِيمَانِ آخَرَانِ",
         "en": "The Jamʿ with Tafriq and with Taqsim; two other Taqsims", "tr": "Cem' ma'a't-Tefrîk ve ma'a't-Taksîm; iki taksîm daha"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them is» — the fronted khabar.", "«ve onlardan biri» — öne alınmış haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def wahuwa(tag, full="وَهُوَ"):
    lex = "hiya" if full.endswith("هِيَ") else "huwa"
    return tok(full, lex, "pron", [tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالضَّمِيرُ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
               segments=[seg("وَ","wa","conj"), seg(full[1:], lex, "pron")])
def an_masd(tag):
    return tok("أَنْ","an-masdariyya","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the clause is the khabar.", "«-mak» — masdar yapan en; cümle haberdir.")
def kaqawl(tag, punct=None):
    return tok("كَقَوْلِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")], punct=punct)
def kaqh(tag):
    return tok("كَقَوْلِهِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«as in His saying».", "«O'nun sözü gibi».",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")])
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

# ----------- s1 — the jamʿ with tafriq (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the JAMʿ WITH TAFRIQ: two things are brought into ONE meaning, and then the two SIDES of that entry are set apart." + R_EN,
 "tr": "Onlardan biri CEM' MA'A'T-TEFRÎKTİR: iki şey TEK bir mânâya sokulur, sonra o sokuluşun iki CİHETİ birbirinden ayrılır." + R_TR},
 "tokens": [
  minha(C1),
  tok("الْجَمْعُ","jam","noun",[C1, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the jamʿ» — the delayed mubtada.", "«cem'» — sona bırakılmış mübtedâ."),
  tok("مَعَ","maa","noun",[C1, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — قَيْدٌ لِلْجَمْعِ.", "«with» — a zarf, restricting the jamʿ.", "«ile» — cem'i kayıtlayan zarf."),
  tok("التَّفْرِيقِ","tafriq","noun",[C1, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tafriq».", "«tefrîk».", punct="،"),
  wahuwa(C1),
  an_masd(C1),
  tok("يُدْخَلَ","adkhala","verb",[C1, "an-masdariyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«are brought in» — a passive, mansub by an.", "«sokulur» — meçhul, en ile mansûb."),
  tok("شَيْئَانِ","shay","noun",[C1, "naib-al-fail", "al-muthanna"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«two things» — the naib al-fail, a dual.", "«iki şey» — nâib-i fâil, tesniye."),
  tok("فِي","fi","part",[C1, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«into».", "«-e»."),
  tok("مَعْنًى","mana","noun",[C1, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَقْصُورٌ.", "«one meaning» — a maqsur noun.", "«tek bir mânâya» — maksûr isim."),
  wa_conj("وَيُفَرَّقَ","farraqa","verb",[C1, "atf-nasaq", "naib-al-fail", "form-ii-verbs"], "يُفَرَّقَ مَعْطُوفٌ عَلَى يُدْخَلَ مَنْصُوبٌ — مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الظَّرْفُ.", "«and are set apart» — joined to the first verb; the zarf stands as its naib.", "«ve ayrılır» — ilk fiile ma'tûf; zarf nâib-i fâildir."),
  tok("بَيْنَ","bayna","noun",[C1, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مُضَافٌ — نَائِبُ الْفَاعِلِ.", "«between» — a zarf, annexed.", "«arasında» — muzâf zarf."),
  tok("جِهَتَيِ","jiha","noun",[C1, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَكُسِرَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«the two sides» — a dual annexed, its nun dropped; the ya takes a kasra before the wasl.", "«iki ciheti» — muzâf tesniye, nûnu düşmüş; yâ vasıldan önce kesre alır."),
  tok("الْإِدْخَالِ","idkhal","noun",[C1, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ أَدْخَلَ.", "«of the entry» — the masdar of adkhala.", "«sokuluşun» — edhale'nin masdarı.", punct=".")]})

# ----------- s2 — al-Watwat: the face and the heart, one fire, two sides
S.append({"id": "s2", "translation": {
 "en": "As al-Watwat says: «Your FACE is like the fire in its LIGHT • and my HEART is like the fire in its HEAT» — two things gathered under one fire, then parted by the two sides of it." + R_EN,
 "tr": "Vatvât'ın dediği gibi: «YÜZÜN ışığıyla ateş gibidir • KALBİM ise sıcaklığıyla ateş gibidir» — iki şey tek bir ateşte toplanmış, sonra onun iki cihetiyle ayrılmıştır." + R_TR},
 "tokens": [
  kaqawl(C1),
  tok("الْوَطْوَاطِ","watwat","noun",[C1, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Watwat».", "«Vatvât».", punct=":"),
  tok("فَوَجْهُكَ","wajh","noun",[C1, "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَوَجْهُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — الشَّيْءُ الْأَوَّلُ.", "«your face» — the mubtada; the first of the two things.", "«yüzün» — mübtedâ; iki şeyin ilki.",
      segments=[seg("فَ","fa","conj"), seg("وَجْهُ","wajh","noun"), seg("كَ","pron-2ms","pron")]),
  tok("كَالنَّارِ","nar","noun",[C1, "huruf-jarr", "mubtada-khabar", "tashbih"], "الْكَافُ لِلتَّشْبِيهِ، وَالنَّارِ مَجْرُورٌ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ: الْمَعْنَى الْوَاحِدُ الَّذِي أُدْخِلَ فِيهِ الشَّيْئَانِ.", "«like the fire» — the khabar; the ONE meaning both things enter.", "«ateş gibi» — haber; iki şeyin sokulduğu TEK mânâ.",
      segments=[seg("كَ","ka","part"), seg("النَّارِ","nar","noun")]),
  tok("فِي","fi","part",[C1, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("ضَوْئِهَا","daw","noun",[C1, "huruf-jarr", "idafa-definiteness", "wajh-al-shabah"], "مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جِهَةُ الْإِدْخَالِ الْأُولَى: وَجْهُ الشَّبَهِ.", "«its light» — the first side: the wajh of the first likening.", "«ışığında» — birinci cihet: ilk benzetmenin vechi.",
      segments=[seg("ضَوْئِ","daw","noun"), seg("هَا","pron-3fs","pron")], punct="*"),
  wa_conj("وَقَلْبِيَ","qalb","noun",[C1, "atf-nasaq", "mubtada-khabar", "ya-al-mutakallim"], "قَلْبِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — الشَّيْءُ الثَّانِي.", "«and my heart» — the second mubtada; the second thing.", "«ve kalbim» — ikinci mübtedâ; ikinci şey.", pron=("ي","pron-1s")),
  tok("كَالنَّارِ","nar","noun",[C1, "huruf-jarr", "mubtada-khabar", "tashbih"], "الْكَافُ لِلتَّشْبِيهِ، وَالنَّارِ مَجْرُورٌ — خَبَرٌ: الْمُشَبَّهُ بِهِ نَفْسُهُ.", "«like the fire» — the khabar; the same mushabbah bihi.", "«ateş gibi» — haber; aynı müşebbehün bih.",
      segments=[seg("كَ","ka","part"), seg("النَّارِ","nar","noun")]),
  tok("فِي","fi","part",[C1, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("حَرِّهَا","harr","noun",[C1, "huruf-jarr", "idafa-definiteness", "wajh-al-shabah"], "مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جِهَةُ الْإِدْخَالِ الثَّانِيَةُ: هُنَا التَّفْرِيقُ.", "«its heat» — the second side: here the two sides part.", "«sıcaklığında» — ikinci cihet: burada iki cihet ayrılır.",
      segments=[seg("حَرِّ","harr","noun"), seg("هَا","pron-3fs","pron")], punct=".")]})
S[-1]["badi"] = [{"kind": "jam-tafriq", "set": [ix(S[-1], "فَوَجْهُكَ"), ix(S[-1], "وَقَلْبِيَ")], "word": ix(S[-1], "كَالنَّارِ"),
                  "pairs": [[ix(S[-1], "فَوَجْهُكَ"), ix(S[-1], "ضَوْئِهَا")], [ix(S[-1], "وَقَلْبِيَ"), ix(S[-1], "حَرِّهَا")]]}]

# ----------- s3 — the jamʿ with taqsim (RESTORED matn)
S.append({"id": "s3", "translation": {
 "en": "Among them is the JAMʿ WITH TAQSIM: many things are gathered under one ruling and then divided — or divided first and then gathered." + R_EN,
 "tr": "Onlardan biri CEM' MA'A'T-TAKSÎMDİR: birden çok şey tek hükümde toplanır, sonra taksim edilir — yahut önce taksim edilir, sonra toplanır." + R_TR},
 "tokens": [
  minha(C2),
  tok("الْجَمْعُ","jam","noun",[C2, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the jamʿ».", "«cem'»."),
  tok("مَعَ","maa","noun",[C2, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«with».", "«ile»."),
  tok("التَّقْسِيمِ","taqsim","noun",[C2, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the taqsim».", "«taksîm».", punct="،"),
  wahuwa(C2),
  tok("جَمْعُ","jam","noun",[C2, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«the gathering» — the khabar.", "«toplamak» — haber."),
  tok("مُتَعَدِّدٍ","mutaaddid","noun",[C2, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of many things».", "«birden çok şeyi»."),
  tok("تَحْتَ","tahta","noun",[C2, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُضَافٌ.", "«under» — a zarf.", "«altında» — zarf."),
  tok("حُكْمٍ","hukm","noun",[C2, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«one ruling».", "«tek hükümde»."),
  tok("ثُمَّ","thumma","part",[C2, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.", "«then».", "«sonra»."),
  tok("تَقْسِيمُهُ","taqsim","noun",[C2, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ عَلَى جَمْعُ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its dividing» — joined to the gathering.", "«sonra taksîmi» — cem'e ma'tûf.",
      segments=[seg("تَقْسِيمُ","taqsim","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("أَوْ","aw","part",[C2, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّقْسِيمِ.", "«or».", "«yahut»."),
  tok("تَقْسِيمُهُ","taqsim","noun",[C2, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ مَرْفُوعٌ مُضَافٌ — الصُّورَةُ الثَّانِيَةُ: التَّقْسِيمُ أَوَّلًا.", "«its dividing» — the second shape: the division first.", "«taksîmi» — ikinci şekil: önce taksîm.",
      segments=[seg("تَقْسِيمُ","taqsim","noun"), seg("هُ","pron-3ms","pron")]),
  tok("ثُمَّ","thumma","part",[C2, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("جَمْعُهُ","jam","noun",[C2, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its gathering».", "«cem'i».",
      segments=[seg("جَمْعُ","jam","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s4 — al-Mutanabbi, bayt 1: the jamʿ (three doers under one verb)
S.append({"id": "s4", "translation": {
 "en": "The first, as al-Mutanabbi says: «…until he camped on the outskirts of KHARSHANA • where the ROMANS, the CROSSES and the CHURCHES are wretched through him» — three things gathered under one ruling." + R_EN,
 "tr": "İlki, Mütenebbî'nin dediği gibi: «…nihayet HARŞENE'nin varoşlarına kondu • ki RUMLAR, HAÇLAR ve KİLİSELER onunla perişandır» — üç şey tek hükümde toplanmıştır." + R_TR},
 "tokens": [
  tok("فَالْأَوَّلُ","awwal","noun",[C2, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«ilki» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْأَوَّلُ","awwal","noun")]),
  kaqawl(C2),
  tok("الْمُتَنَبِّي","mutanabbi","noun",[C2, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ: أَبُو الطَّيِّبِ الْمُتَنَبِّي.", "«al-Mutanabbi» — a manqus name: Abu l-Tayyib.", "«Mütenebbî» — manqûs isim: Ebü't-Tayyib.", punct=":"),
  tok("حَتَّى","hatta","part",[C2, "huruf-jarr"], "حَرْفُ غَايَةٍ وَابْتِدَاءٍ.", "«until» — hatta opening the clause.", "«nihayet» — cümle açan hattâ."),
  tok("أَقَامَ","aqama","verb",[C2, "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: سَيْفُ الدَّوْلَةِ.", "«he camped» — the doer concealed: Sayf al-Dawla.", "«kondu» — fâil gizli: Seyfüddevle."),
  tok("عَلَى","ala","part",[C2, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-na»."),
  tok("أَرْبَاضِ","rabad","noun",[C2, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ مُضَافٌ — جَمْعُ رَبَضٍ: مَا حَوْلَ الْمَدِينَةِ.", "«the outskirts» — the plural of rabad.", "«varoşlarına» — rabad'ın çoğulu."),
  tok("خَرْشَنَةٍ","kharshana","noun",[C2, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حِصْنٌ لِلرُّومِ؛ صُرِفَ لِلضَّرُورَةِ.", "«Kharshana» — a Byzantine fort; declined fully for the metre.", "«Harşene» — Rum kalesi; vezin için munsarif.", punct="*"),
  tok("تَشْقَى","shaqiya","verb",[C2, "mudari-marfu", "naqis-verbs", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — الْحُكْمُ الْوَاحِدُ.", "«are wretched» — the ONE ruling over the three.", "«perişandır» — üçü kuşatan TEK hüküm."),
  tok("بِهِ","bi","part",[C2, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«through him».", "«onunla».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الرُّومُ","rum","noun",[C2, "fail"], "فَاعِلٌ مَرْفُوعٌ — الْأَوَّلُ مِنَ الْمُتَعَدِّدِ.", "«the Romans» — the doer; the first of the many.", "«Rumlar» — fâil; çoğun ilki."),
  wa_conj("وَالصُّلْبَانُ","salib","noun",[C2, "atf-nasaq", "jam-taksir"], "الصُّلْبَانُ مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ صَلِيبٍ.", "«and the crosses» — joined; the plural of salib.", "«ve haçlar» — ma'tûf; salîb'in çoğulu."),
  wa_conj("وَالْبِيَعُ","bia","noun",[C2, "atf-nasaq", "jam-taksir"], "الْبِيَعُ مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ بِيعَةٍ: كَنِيسَةُ النَّصَارَى.", "«and the churches» — joined; the plural of biʿa.", "«ve kiliseler» — ma'tûf; bîa'nın çoğulu.", punct=".")]})
S[-1]["badi"] = [{"kind": "jam", "sub": "fail", "set": [ix(S[-1], "الرُّومُ"), ix(S[-1], "وَالصُّلْبَانُ"), ix(S[-1], "وَالْبِيَعُ")], "word": ix(S[-1], "تَشْقَى")},
                 {"kind": "jam-taqsim", "sub": "jam-first", "with": "s5"}]

# ----------- s5 — al-Mutanabbi, bayt 2: the taqsim (each ruin to its own)
S.append({"id": "s5", "translation": {
 "en": "«To CAPTIVITY what they wedded, to SLAUGHTER what they begot, • to PLUNDER what they gathered, to FIRE what they sowed» — the division: each thing handed its own ruin." + R_EN,
 "tr": "«ESÂRETE nikâhladıkları, KATLE doğurdukları, • YAĞMAYA topladıkları, ATEŞE ektikleri» — taksîm: her şeye kendi felâketi." + R_TR},
 "tokens": [
  tok("لِلسَّبْيِ","saby","noun",[Q, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — السَّبْيُ: الْأَسْرُ.", "«to captivity» — the fronted khabar; the first ruling.", "«esârete» — öne alınmış haber; ilk hüküm.",
      segments=[seg("لِ","li","part"), seg("السَّبْيِ","saby","noun")]),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ — الشَّيْءُ الْأَوَّلُ.", "«what» — the delayed mubtada; the first thing.", "«…-dıkları» — sona bırakılmış mübtedâ; ilk şey."),
  tok("نَكَحُوا","nakaha","verb",[Q, "ism-mawsul"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — صِلَةُ الْمَوْصُولِ.", "«they wedded» — the sila.", "«nikâhladıkları» — sıla."),
  wa_conj("وَالْقَتْلِ","qatl","noun",[Q, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْقَتْلِ مَعْطُوفٌ عَلَى السَّبْيِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ ثَانٍ.", "«and to slaughter» — joined to the first; the second ruling.", "«ve katle» — ilkine ma'tûf; ikinci hüküm."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "mubtada-khabar"], "مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«…-dıkları»."),
  tok("وَلَدُوا","walada","verb",[Q, "ism-mawsul", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — صِلَةٌ.", "«they begot» — the sila.", "«doğurdukları» — sıla.", punct="*"),
  wa_conj("وَالنَّهْبِ","nahb","noun",[Q, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "النَّهْبِ مَعْطُوفٌ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ ثَالِثٌ.", "«and to plunder» — the third ruling.", "«ve yağmaya» — üçüncü hüküm."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "mubtada-khabar"], "مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«…-dıkları»."),
  tok("جَمَعُوا","jamaa-gather","verb",[Q, "ism-mawsul"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — صِلَةٌ.", "«they gathered».", "«topladıkları»."),
  wa_conj("وَالنَّارِ","nar","noun",[Q, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "النَّارِ مَعْطُوفٌ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ رَابِعٌ.", "«and to fire» — the fourth ruling.", "«ve ateşe» — dördüncü hüküm."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "mubtada-khabar"], "مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«…-dıkları»."),
  tok("زَرَعُوا","zaraa","verb",[Q, "ism-mawsul"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — صِلَةٌ.", "«they sowed».", "«ektikleri».", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "tayin", "first": [ix(S[-1], "لِلسَّبْيِ"), ix(S[-1], "وَالْقَتْلِ"), ix(S[-1], "وَالنَّهْبِ"), ix(S[-1], "وَالنَّارِ")],
                  "second": [ix(S[-1], "نَكَحُوا"), ix(S[-1], "وَلَدُوا"), ix(S[-1], "جَمَعُوا"), ix(S[-1], "زَرَعُوا")]}]

# ----------- s6 — Hassan b. Thabit, bayt 1: the taqsim first
S.append({"id": "s6", "translation": {
 "en": "The second, as Hassan b. Thabit says: «A people who, WHEN they make war, harm their enemy, • OR when they seek the good of their followers, do them good» — divided first: each case with its ruling." + R_EN,
 "tr": "İkincisi, Hassân b. Sâbit'in dediği gibi: «Bir kavim ki HARP ETTİKLERİ zaman düşmanlarına zarar verir, • YAHUT tâbileri için menfaat istediklerinde fayda verirler» — önce taksîm: her hâle kendi hükmü." + R_TR},
 "tokens": [
  wa_conj("وَالثَّانِي","thani","noun",[C2, "atf-nasaq", "mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«and the second» — the mubtada, a manqus.", "«ikincisi» — mübtedâ, manqûs."),
  kaqawl(C2),
  tok("حَسَّانَ","hassan-ibn-thabit","noun",[C2, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ.", "«Hassan» — a diptote name: jarr by a fatha.", "«Hassân» — gayr-i munsarif: kesre yerine fetha."),
  tok("بْنِ","ibn","noun",[C2, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("ثَابِتٍ","thabit-name","noun",[C2, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Thabit».", "«Sâbit».", punct=":"),
  tok("قَوْمٌ","qawm","noun",[C2, "mubtada-khabar"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هُمْ قَوْمٌ.", "«a people» — the khabar of an unspoken «they are».", "«bir kavim» — hazfedilmiş «onlar»ın haberi."),
  tok("إِذَا","idha","part",[C2, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ — الْحَالُ الْأُولَى.", "«when» — the zarf of the condition; the first case.", "«…-dıkları zaman» — şart mânâlı zarf; ilk hâl."),
  tok("حَارَبُوا","haraba","verb",[C2, "idha-shartiyya", "form-iii-verbs"], "فِعْلٌ مَاضٍ فِعْلُ الشَّرْطِ، وَالْوَاوُ فَاعِلٌ.", "«they make war» — the shart's verb.", "«harp ettikleri» — şart fiili."),
  tok("ضَرُّوا","darra","verb",[C2, "idha-shartiyya", "doubled-verbs"], "فِعْلٌ مَاضٍ جَوَابُ الشَّرْطِ، وَالْوَاوُ فَاعِلٌ — حُكْمُ الْحَالِ الْأُولَى.", "«they harm» — the jawab; the first case's ruling.", "«zarar verirler» — cevap; ilk hâlin hükmü."),
  tok("عَدُوَّهُمْ","aduw","noun",[C2, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«their enemy» — the object.", "«düşmanlarına» — mef'ûl.",
      segments=[seg("عَدُوَّ","aduw","noun"), seg("هُمْ","pron-3mp","pron")], punct="*"),
  tok("أَوْ","aw","part",[C2, "atf-nasaq"], "حَرْفُ عَطْفٍ — يَعْطِفُ الْحَالَ الثَّانِيَةَ.", "«or» — joining the second case.", "«yahut» — ikinci hâli bağlar."),
  tok("حَاوَلُوا","hawala","verb",[C2, "atf-nasaq", "form-iii-verbs"], "فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى حَارَبُوا، وَالْوَاوُ فَاعِلٌ — الْحَالُ الثَّانِيَةُ.", "«they seek» — joined to the first shart; the second case.", "«istedikleri» — ilk şarta ma'tûf; ikinci hâl."),
  tok("النَّفْعَ","naf","noun",[C2, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the good» — the object.", "«menfaati» — mef'ûl."),
  tok("فِي","fi","part",[C2, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«…-de»."),
  tok("أَشْيَاعِهِمْ","shia","noun",[C2, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ شِيعَةٍ: الْأَتْبَاعُ.", "«their followers» — the plural of shiʿa.", "«tâbileri» — şîa'nın çoğulu.",
      segments=[seg("أَشْيَاعِ","shia","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("نَفَعُوا","nafaa","verb",[C2, "idha-shartiyya"], "فِعْلٌ مَاضٍ جَوَابٌ لِلشَّرْطِ الْمَعْطُوفِ، وَالْوَاوُ فَاعِلٌ — حُكْمُ الْحَالِ الثَّانِيَةِ.", "«they do good» — the second jawab; the second case's ruling.", "«fayda verirler» — ikinci cevap; ikinci hâlin hükmü.", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "tayin", "first": [ix(S[-1], "حَارَبُوا"), ix(S[-1], "حَاوَلُوا")], "second": [ix(S[-1], "ضَرُّوا"), ix(S[-1], "نَفَعُوا")]},
                 {"kind": "jam-taqsim", "sub": "taqsim-first", "with": "s7"}]

# ----------- s7 — Hassan, bayt 2: the jamʿ after (that is a nature in them)
S.append({"id": "s7", "translation": {
 "en": "«A NATURE, that, in them, not newly made; • know that of all natures the worst are the new-fangled» — then gathered: the two rulings are ONE nature." + R_EN,
 "tr": "«O, onlarda sonradan olmayan bir HUYDUR; • bil ki huyların en kötüsü sonradan uydurulanlardır» — sonra cem': iki hüküm TEK huydur." + R_TR},
 "tokens": [
  tok("سَجِيَّةٌ","sajiya","noun",[C2, "mubtada-khabar"], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ — الْحُكْمُ الْوَاحِدُ الَّذِي جُمِعَ فِيهِ الْقِسْمَانِ.", "«a nature» — the fronted khabar: the ONE ruling both cases are gathered under.", "«bir huy» — öne alınmış haber: iki hâlin toplandığı TEK hüküm."),
  tok("تِلْكَ","tilka","pron",[C2, "asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ مُؤَخَّرٌ — إِشَارَةٌ إِلَى الْحَالَيْنِ مَعًا: هُنَا الْجَمْعُ.", "«that» — the delayed mubtada, pointing at BOTH cases at once: here the jamʿ.", "«o» — sona bırakılmış mübtedâ, iki hâle BİRDEN işaret: cem' burada."),
  tok("مِنْهُمْ","min","part",[C2, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ.", "«in them».", "«onlarda».", segments=[seg("مِنْ","min","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("غَيْرُ","ghayr","noun",[C2, "naat-sifa", "idafa-definiteness"], "نَعْتٌ لِسَجِيَّةٍ مَرْفُوعٌ مُضَافٌ.", "«not» — a na't of the nature, annexed.", "«olmayan» — huyun na'ti, muzâf."),
  tok("مُحْدَثَةٍ","muhdath","noun",[C2, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ أَحْدَثَ.", "«newly made» — the ism maf'ul.", "«sonradan olma» — ism-i mef'ûl.", punct="*"),
  tok("إِنَّ","inna","part",[C2, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«verily».", "«muhakkak»."),
  tok("الْخَلَائِقَ","khalaiq","noun",[C2, "inna-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf"], "اسْمُ إِنَّ مَنْصُوبٌ — جَمْعُ خَلِيقَةٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.", "«the natures» — the ism of inna; a plural of plurals shape.", "«huylar» — inne'nin ismi; müntehe'l-cümû' vezni."),
  tok("فَاعْلَمْ","alima","verb",[C2, "imperative-amr", "jumla-mutarida"], "الْفَاءُ زَائِدَةٌ، وَاعْلَمْ فِعْلُ أَمْرٍ، وَالْفَاعِلُ أَنْتَ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«know!» — a parenthetical command.", "«bil!» — mu'teriza cümle.",
      segments=[seg("فَ","fa","conj"), seg("اعْلَمْ","alima","verb")]),
  tok("شَرُّهَا","sharr","noun",[C2, "mubtada-khabar", "idafa-definiteness", "ism-tafdil"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَفْعَلُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.", "«the worst of them» — the mubtada of the khabar-clause; an elative with its hamza dropped.", "«en kötüsü» — haber cümlesinin mübtedâsı; hemzesi düşmüş ism-i tafdîl.",
      segments=[seg("شَرُّ","sharr","noun"), seg("هَا","pron-3fs","pron")]),
  tok("الْبِدَعُ","bida","noun",[C2, "mubtada-khabar", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ — جَمْعُ بِدْعَةٍ.", "«the new-fangled» — the khabar; the clause is inna's khabar.", "«uydurmalar» — haber; cümle inne'nin haberidir.", punct=".")]})
S[-1]["badi"] = [{"kind": "jam", "sub": "ishara", "set": [ix(S[-1], "تِلْكَ")], "word": ix(S[-1], "سَجِيَّةٌ")}]

# ----------- s8 — the jamʿ with both (RESTORED matn)
S.append({"id": "s8", "translation": {
 "en": "And among them is the JAMʿ WITH TAFRIQ AND TAQSIM together." + R_EN,
 "tr": "Ve onlardan biri, TEFRÎK VE TAKSÎM İLE BİRLİKTE CEM'DİR." + R_TR},
 "tokens": [
  minha(C3),
  tok("الْجَمْعُ","jam","noun",[C3, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the jamʿ».", "«cem'»."),
  tok("مَعَ","maa","noun",[C3, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«with».", "«ile»."),
  tok("التَّفْرِيقِ","tafriq","noun",[C3, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tafriq».", "«tefrîk»."),
  wa_conj("وَالتَّقْسِيمِ","taqsim","noun",[C3, "atf-nasaq", "masdar"], "التَّقْسِيمِ مَعْطُوفٌ مَجْرُورٌ.", "«and the taqsim».", "«ve taksîm».", punct=".")]})

# ----------- s9 — Hud 11:105: the jamʿ (no soul speaks) and the tafriq (wretched / blessed)
S.append({"id": "s9", "translation": {
 "en": "As He says, exalted is He: «The day it comes, NO SOUL shall speak save by His leave; then of them is the WRETCHED and the BLESSED» — all gathered under one ruling, then parted in two." + R_EN,
 "tr": "Nitekim Allah Teâlâ buyurur: «O gün gelince HİÇBİR NEFİS O'nun izni olmadan konuşamaz; artık onlardan kimi ŞAKÎ, kimi SAÎDDİR» — hepsi tek hükümde toplanmış, sonra ikiye ayrılmıştır." + R_TR},
 "tokens": [
  kaqh(C3), taala(C3),
  tok("يَوْمَ","yawm","noun",[C3, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ إِلَى الْجُمْلَةِ.", "«the day» — a zarf annexed to the clause.", "«gün» — cümleye muzâf zarf."),
  tok("يَأْتِ","ata","verb",[C3, "mudari-marfu", "naqis-verbs", "idafa-definiteness"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، حُذِفَتْ يَاؤُهُ فِي الرَّسْمِ اتِّبَاعًا لِلْمُصْحَفِ، وَالْفَاعِلُ مُسْتَتِرٌ: الْيَوْمُ.", "«it comes» — marfuʿ; the ya is dropped in the mushaf's spelling; the doer concealed: the day.", "«gelir» — merfû; yâ mushaf imlâsında düşmüş; fâil gizli: gün."),
  tok("لَا","la-nafiya","part",[C3, "anwa-ma"], "نَافِيَةٌ.", "«not».", "«…-maz»."),
  tok("تَكَلَّمُ","takallama","verb",[C3, "mudari-marfu", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَصْلُهُ تَتَكَلَّمُ حُذِفَتْ إِحْدَى التَّاءَيْنِ: الْحُكْمُ الْوَاحِدُ.", "«shall speak» — one of the two tas dropped; the ONE ruling over all.", "«konuşur» — iki tâdan biri düşmüş; hepsini kuşatan TEK hüküm."),
  tok("نَفْسٌ","nafs","noun",[C3, "fail", "umum-al-salb"], "فَاعِلٌ مَرْفُوعٌ — نَكِرَةٌ فِي سِيَاقِ النَّفْيِ فَتَعُمُّ: كُلُّ نَفْسٍ.", "«a soul» — the doer; an indefinite under negation covers EVERY soul: the jamʿ.", "«bir nefis» — fâil; nefiy içindeki nekre HER nefsi kuşatır: cem'."),
  tok("إِلَّا","illa","part",[C3, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«save».", "«ancak»."),
  tok("بِإِذْنِهِ","idhn","noun",[C3, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِحَالٍ مَحْذُوفَةٍ.", "«by His leave».", "«O'nun izniyle».",
      segments=[seg("بِ","bi","part"), seg("إِذْنِ","idhn","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("فَمِنْهُمْ","min","part",[C3, "huruf-jarr", "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَمِنْهُمْ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — هُنَا التَّفْرِيقُ.", "«then of them» — the fronted khabar: here the tafriq.", "«artık onlardan» — öne alınmış haber: tefrîk burada.",
      segments=[seg("فَ","fa","conj"), seg("مِنْ","min","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("شَقِيٌّ","shaqi","noun",[C3, "mubtada-khabar", "sifa-mushabbaha"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — الْقِسْمُ الْأَوَّلُ.", "«the wretched» — the delayed mubtada; the first part.", "«şakî» — sona bırakılmış mübtedâ; ilk kısım."),
  wa_conj("وَسَعِيدٌ","said","noun",[C3, "atf-nasaq", "sifa-mushabbaha"], "سَعِيدٌ مَعْطُوفٌ مَرْفُوعٌ — الْقِسْمُ الثَّانِي.", "«and the blessed» — the second part.", "«ve saîd» — ikinci kısım.", punct=".")]})
S[-1]["badi"] = [{"kind": "jam", "sub": "amm", "set": [ix(S[-1], "نَفْسٌ")], "word": ix(S[-1], "تَكَلَّمُ")},
                 {"kind": "tafriq", "sub": "partition", "first": [ix(S[-1], "شَقِيٌّ")], "second": [ix(S[-1], "وَسَعِيدٌ")]},
                 {"kind": "jam-tafriq-taqsim", "with": "s10"}]

# ----------- s10 — Hud 11:106-107: the taqsim, first half (the wretched → the Fire)
S.append({"id": "s10", "translation": {
 "en": "«As for those who are WRETCHED, in the FIRE: theirs therein is sighing and sobbing, abiding there as long as the heavens and the earth endure, save what your Lord wills — your Lord does whatever He wills» — the first share of the division." + R_EN,
 "tr": "«ŞAKÎ olanlara gelince, ATEŞTEDİRLER: orada onlar için inleme ve hıçkırık vardır; gökler ve yer durdukça, Rabbinin dilediği müstesnâ, orada kalıcıdırlar — Rabbin dilediğini yapandır» — taksîmin ilk payı." + R_TR},
 "tokens": [
  tok("فَأَمَّا","amma","part",[C3, "amma-tafsiliyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ — يَفْتَحُ الْقِسْمَ الْأَوَّلَ.", "«as for» — the particle of detailing; it opens the first share.", "«gelince» — tafsîl harfi; ilk payı açar.",
      segments=[seg("فَ","fa","conj"), seg("أَمَّا","amma","part")]),
  tok("الَّذِينَ","alladhina","pron",[C3, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«those who» — the mubtada.", "«olanlar» — mübtedâ."),
  tok("شَقُوا","shaqiya","verb",[C3, "ism-mawsul", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — صِلَةٌ؛ حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«are wretched» — the sila; the weak last radical dropped before the waw.", "«şakî oldular» — sıla; illetli son harf vâvdan önce düşmüş."),
  tok("فَفِي","fi","part",[C3, "huruf-jarr", "amma-tafsiliyya", "mubtada-khabar"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَفِي حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«then in» — the fa of amma's answer; the jarr phrase is the khabar.", "«işte …-dedir» — emmâ'nın cevap fâsı; câr-mecrûr haberdir.",
      segments=[seg("فَ","fa","conj"), seg("فِي","fi","part")]),
  tok("النَّارِ","nar","noun",[C3, "huruf-jarr"], "مَجْرُورٌ — حُكْمُ الْقِسْمِ الْأَوَّلِ.", "«the Fire» — the first share's ruling.", "«ateş» — ilk payın hükmü."),
  tok("لَهُمْ","li","part",[C3, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«theirs» — a fronted khabar.", "«onlar için» — öne alınmış haber.", segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("فِيهَا","fi","part",[C3, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْخَبَرِ.", "«therein».", "«orada».", segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("زَفِيرٌ","zafir","noun",[C3, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«sighing» — the delayed mubtada.", "«inleme» — sona bırakılmış mübtedâ."),
  wa_conj("وَشَهِيقٌ","shahiq","noun",[C3, "atf-nasaq"], "شَهِيقٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and sobbing».", "«ve hıçkırık»."),
  tok("خَالِدِينَ","khalid-abiding","noun",[C3, "hal", "jam-mudhakkar-salim", "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«abiding» — a hal; a sound masculine plural in nasb.", "«kalıcı olarak» — hâl; cem-i müzekker-i sâlim, mansûb."),
  tok("فِيهَا","fi","part",[C3, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«there».", "«orada».", segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","part",[C3, "anwa-ma", "maful-fih"], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ: مُدَّةَ دَوَامِ السَّمَاوَاتِ.", "«as long as» — the masdar-making ma of duration.", "«…-dıkça» — zarf mânâlı masdariye mâ."),
  tok("دَامَتِ","dama","verb",[C3, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«endure» — a sister of kana; its ta takes a kasra before the wasl.", "«durdukça» — kâne'nin kardeşi; tâ vasıldan önce kesre alır."),
  tok("السَّمَاوَاتُ","samawat","noun",[C3, "kana-wa-akhawatuha", "jam-muannath-salim"], "اسْمُ دَامَ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the heavens» — the ism of dama.", "«gökler» — dâme'nin ismi."),
  wa_conj("وَالْأَرْضُ","ard","noun",[C3, "atf-nasaq"], "الْأَرْضُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the earth».", "«ve yer»."),
  tok("إِلَّا","illa","part",[C3, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«save».", "«müstesnâ»."),
  tok("مَا","ma-mawsula","pron",[C3, "ism-mawsul", "istithna"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مُسْتَثْنًى.", "«what» — the excepted.", "«…-diği» — müstesnâ."),
  tok("شَاءَ","shaa","verb",[C3, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«wills» — the sila.", "«diledi» — sıla."),
  tok("رَبُّكَ","rabb","noun",[C3, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord» — the doer.", "«Rabbin» — fâil.", segments=[seg("رَبُّ","rabb","noun"), seg("كَ","pron-2ms","pron")], punct="،"),
  tok("إِنَّ","inna","part",[C3, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«verily».", "«muhakkak»."),
  tok("رَبَّكَ","rabb","noun",[C3, "inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ إِنَّ مَنْصُوبٌ مُضَافٌ.", "«your Lord» — the ism of inna.", "«Rabbin» — inne'nin ismi.", segments=[seg("رَبَّ","rabb","noun"), seg("كَ","pron-2ms","pron")]),
  tok("فَعَّالٌ","faal","noun",[C3, "inna-wa-akhawatuha", "sighat-mubalagha"], "خَبَرُ إِنَّ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَعَّالٍ.", "«ever-doing» — inna's khabar; the intensive faʿʿal.", "«hep yapan» — inne'nin haberi; fa''âl mübalağa sîgası."),
  tok("لِمَا","ma-mawsula","pron",[C3, "huruf-jarr", "ism-mawsul"], "اللَّامُ حَرْفُ جَرٍّ، وَمَا مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«whatever».", "«…-diğini».", segments=[seg("لِ","li","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُرِيدُ","arada","verb",[C3, "ism-mawsul", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«He wills» — the sila.", "«diler» — sıla.", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "amma", "first": [ix(S[-1], "شَقُوا")], "second": [ix(S[-1], "النَّارِ")]}]

# ----------- s11 — Hud 11:108: the taqsim, second half (the blessed → the Garden)
S.append({"id": "s11", "translation": {
 "en": "«And as for those who are BLESSED, in the GARDEN, abiding there as long as the heavens and the earth endure, save what your Lord wills — a gift never cut off» — the second share; the division complete." + R_EN,
 "tr": "«SAÎD olanlara gelince, CENNETTEDİRLER; gökler ve yer durdukça, Rabbinin dilediği müstesnâ, orada kalıcıdırlar — kesilmeyen bir bağış olarak» — ikinci pay; taksîm tamamlanır." + R_TR},
 "tokens": [
  wa_conj("وَأَمَّا","amma","part",[C3, "amma-tafsiliyya"], "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ — يَفْتَحُ الْقِسْمَ الثَّانِيَ.", "«and as for» — opening the second share.", "«…-e gelince» — ikinci payı açar."),
  tok("الَّذِينَ","alladhina","pron",[C3, "ism-mawsul", "mubtada-khabar"], "مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«those who».", "«olanlar»."),
  tok("سُعِدُوا","saida","verb",[C3, "ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — صِلَةٌ.", "«are made blessed» — a passive; the waw its naib.", "«saîd kılındılar» — meçhul; vâv nâib-i fâil."),
  tok("فَفِي","fi","part",[C3, "huruf-jarr", "amma-tafsiliyya", "mubtada-khabar"], "الْفَاءُ فِي جَوَابِ أَمَّا، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«then in» — the answer's fa; the khabar.", "«işte …-dedir» — cevap fâsı; haber.",
      segments=[seg("فَ","fa","conj"), seg("فِي","fi","part")]),
  tok("الْجَنَّةِ","janna","noun",[C3, "huruf-jarr"], "مَجْرُورٌ — حُكْمُ الْقِسْمِ الثَّانِي.", "«the Garden» — the second share's ruling.", "«cennet» — ikinci payın hükmü."),
  tok("خَالِدِينَ","khalid-abiding","noun",[C3, "hal", "jam-mudhakkar-salim", "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ.", "«abiding» — a hal.", "«kalıcı olarak» — hâl."),
  tok("فِيهَا","fi","part",[C3, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«there».", "«orada».", segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","part",[C3, "anwa-ma", "maful-fih"], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ.", "«as long as».", "«…-dıkça»."),
  tok("دَامَتِ","dama","verb",[C3, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ مَكْسُورَةٌ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«endure» — dama; the ta's kasra before the wasl.", "«durdukça» — dâme; vasıl kesresi."),
  tok("السَّمَاوَاتُ","samawat","noun",[C3, "kana-wa-akhawatuha", "jam-muannath-salim"], "اسْمُ دَامَ مَرْفُوعٌ.", "«the heavens».", "«gökler»."),
  wa_conj("وَالْأَرْضُ","ard","noun",[C3, "atf-nasaq"], "الْأَرْضُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the earth».", "«ve yer»."),
  tok("إِلَّا","illa","part",[C3, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«save».", "«müstesnâ»."),
  tok("مَا","ma-mawsula","pron",[C3, "ism-mawsul", "istithna"], "مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مُسْتَثْنًى.", "«what».", "«…-diği»."),
  tok("شَاءَ","shaa","verb",[C3, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«wills».", "«diledi»."),
  tok("رَبُّكَ","rabb","noun",[C3, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ مُضَافٌ.", "«your Lord».", "«Rabbin».", segments=[seg("رَبُّ","rabb","noun"), seg("كَ","pron-2ms","pron")]),
  tok("عَطَاءً","ata-gift","noun",[C3, "maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ: يُعْطَوْنَ عَطَاءً — مَصْدَرٌ مَصْرُوفٌ، هَمْزَتُهُ مُنْقَلِبَةٌ عَنْ وَاوٍ.", "«a gift» — the maf'ul mutlaq of an unspoken «they are given»; its hamza is from a waw, so it takes tanwin.", "«bir bağış olarak» — hazfedilmiş «verilirler»in mef'ûl-i mutlakı; hemzesi vâvdan dönme, tenvin alır."),
  tok("غَيْرَ","ghayr","noun",[C3, "naat-sifa", "idafa-definiteness"], "نَعْتٌ لِعَطَاءً مَنْصُوبٌ مُضَافٌ.", "«never» — a na't of the gift, annexed.", "«…-meyen» — bağışın na'ti, muzâf."),
  tok("مَجْذُوذٍ","majdhudh","noun",[C3, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ جَذَّ: قَطَعَ.", "«cut off» — the ism maf'ul of jadhdha.", "«kesilmiş» — cezze'nin ism-i mef'ûlü.", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "amma", "first": [ix(S[-1], "سُعِدُوا")], "second": [ix(S[-1], "الْجَنَّةِ")]}]

Q = "taqsim-al-ahwal-wal-istifa"
# ----------- s12 — the two other taqsims: the first (RESTORED matn)
S.append({"id": "s12", "translation": {
 "en": "The taqsim is at times applied to two other things: one of them is naming the STATES of a thing, adding to each what befits it." + R_EN,
 "tr": "Taksîm bazen başka iki şeye de denir: biri, bir şeyin HÂLLERİNİ anıp her birine ona yakışanı eklemektir." + R_TR},
 "tokens": [
  wa_conj("وَقَدْ","qad","part",[Q, "qad-harf"], "قَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and at times» — qad of rarity before a mudari.", "«ve bazen» — muzâriden önce azlık kad'ı."),
  tok("يُطْلَقُ","atlaqa","verb",[Q, "mudari-marfu", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is applied» — a passive.", "«denir» — meçhul."),
  tok("التَّقْسِيمُ","taqsim","noun",[Q, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the taqsim» — the naib al-fail.", "«taksîm» — nâib-i fâil."),
  tok("عَلَى","ala","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("أَمْرَيْنِ","amr","noun",[Q, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two things» — a dual.", "«iki şeye» — tesniye."),
  tok("آخَرَيْنِ","akhar","noun",[Q, "naat-sifa", "al-muthanna"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ.", "«other» — a na't.", "«başka» — na't.", punct=":"),
  tok("أَحَدُهُمَا","ahad","noun",[Q, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«one of them» — the mubtada.", "«biri» — mübtedâ.", segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")]),
  tok("ذِكْرُ","dhikr","noun",[Q, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«the naming» — the khabar.", "«anmak» — haber."),
  tok("أَحْوَالِ","ahwal","noun",[Q, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ — جَمْعُ حَالٍ.", "«of the states» — the plural of hal.", "«hâllerini» — hâl'in çoğulu."),
  tok("الشَّيْءِ","shay","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of a thing».", "«bir şeyin»."),
  tok("مُضَافًا","mudaf","noun",[Q, "hal", "ism-maful"], "حَالٌ مَنْصُوبٌ — اسْمُ مَفْعُولِ أَضَافَ.", "«adding» — a hal: «with … added».", "«eklenmiş olarak» — hâl."),
  tok("إِلَى","ila","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("كُلٍّ","kull","noun",[Q, "huruf-jarr"], "مَجْرُورٌ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ.", "«each» — its tanwin stands for the dropped annex.", "«her birine» — tenvin, düşen muzâfun ileyhin ıvazı."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلِ مُضَافًا.", "«what» — the naib of the participle.", "«…-anı» — ism-i mef'ûlün nâibi."),
  tok("يَلِيقُ","laqa-befit","verb",[Q, "ism-mawsul", "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ؛ أَجْوَفُ يَائِيٌّ.", "«befits» — the sila; a hollow verb.", "«yakışır» — sıla; ecvef."),
  tok("بِهِ","bi","part",[Q, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«it».", "«ona».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s13 — al-Mutanabbi: the states of the shaykhs, each with its own
S.append({"id": "s13", "translation": {
 "en": "As al-Mutanabbi says of them: «HEAVY when they meet the foe, LIGHT when called, • MANY when they charge, FEW when counted» — four states, and to each what befits it." + R_EN,
 "tr": "Mütenebbî'nin onlar için dediği gibi: «Düşmanla karşılaşınca AĞIR, çağrılınca HAFİF, • hücum edince ÇOK, sayılınca AZ» — dört hâl, her birine yakışanı." + R_TR},
 "tokens": [
  kaqawl(Q),
  tok("الْمُتَنَبِّي","mutanabbi","noun",[Q, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«al-Mutanabbi».", "«Mütenebbî».", punct=":"),
  tok("ثِقَالٍ","thaqil","noun",[Q, "naat-sifa", "jam-taksir", "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ تَبَعًا لِمَوْصُوفِهِ فِي الْبَيْتِ قَبْلَهُ (مِنْ مَشَايِخَ) — جَمْعُ ثَقِيلٍ: الْحَالُ الْأُولَى.", "«heavy» — a na't in jarr, following its noun in the previous bayt; the first state.", "«ağır» — bir önceki beyitteki mevsûfuna tâbi na't; ilk hâl."),
  tok("إِذَا","idha","part",[Q, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«…-ınca»."),
  tok("لَاقَوْا","laqa-meet","verb",[Q, "idha-shartiyya", "form-iii-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — حُذِفَتْ لَامُهُ لِلْوَاوِ: مَا يَلِيقُ بِالْحَالِ الْأُولَى.", "«they meet» — the weak last radical dropped; what befits the first state.", "«karşılaşırlar» — illetli lâm düşmüş; ilk hâle yakışan."),
  tok("خِفَافٍ","khafif","noun",[Q, "naat-sifa", "jam-taksir", "sifa-mushabbaha"], "نَعْتٌ ثَانٍ مَجْرُورٌ — جَمْعُ خَفِيفٍ: الْحَالُ الثَّانِيَةُ.", "«light» — a second na't; the second state.", "«hafif» — ikinci na't; ikinci hâl."),
  tok("إِذَا","idha","part",[Q, "idha-shartiyya", "maful-fih"], "ظَرْفُ شَرْطٍ.", "«when».", "«…-ınca»."),
  tok("دُعُوا","daa","verb",[Q, "idha-shartiyya", "naib-al-fail", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ.", "«they are called» — a passive.", "«çağrılırlar» — meçhul.", punct="*"),
  tok("كَثِيرٍ","kathir","noun",[Q, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ ثَالِثٌ مَجْرُورٌ — الْحَالُ الثَّالِثَةُ.", "«many» — the third state.", "«çok» — üçüncü hâl."),
  tok("إِذَا","idha","part",[Q, "idha-shartiyya", "maful-fih"], "ظَرْفُ شَرْطٍ.", "«when».", "«…-ınca»."),
  tok("شَدُّوا","shadda","verb",[Q, "idha-shartiyya", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — شَدَّ عَلَى الْعَدُوِّ: حَمَلَ.", "«they charge» — shadda ʿala: to attack.", "«hücum ederler» — şedde alâ: saldırmak."),
  tok("قَلِيلٍ","qalil","noun",[Q, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ رَابِعٌ مَجْرُورٌ — الْحَالُ الرَّابِعَةُ.", "«few» — the fourth state.", "«az» — dördüncü hâl."),
  tok("إِذَا","idha","part",[Q, "idha-shartiyya", "maful-fih"], "ظَرْفُ شَرْطٍ.", "«when».", "«…-ınca»."),
  tok("عُدُّوا","adda-count","verb",[Q, "idha-shartiyya", "naib-al-fail", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — مُضَاعَفٌ.", "«they are counted» — a passive of the doubled ʿadda.", "«sayılırlar» — muzâaf adde'nin meçhulü.", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "ahwal", "first": [ix(S[-1], "ثِقَالٍ"), ix(S[-1], "خِفَافٍ"), ix(S[-1], "كَثِيرٍ"), ix(S[-1], "قَلِيلٍ")],
                  "second": [ix(S[-1], "لَاقَوْا"), ix(S[-1], "دُعُوا"), ix(S[-1], "شَدُّوا"), ix(S[-1], "عُدُّوا")]}]

# ----------- s14 — the second other taqsim (RESTORED matn)
S.append({"id": "s14", "translation": {
 "en": "And the other is the EXHAUSTING of a thing's divisions — every part named, none left out." + R_EN,
 "tr": "Öbürü ise bir şeyin bütün kısımlarını EKSİKSİZ saymaktır — her kısım anılır, hiçbiri dışarıda kalmaz." + R_TR},
 "tokens": [
  wa_conj("وَالثَّانِي","thani","noun",[Q, "atf-nasaq", "mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the other» — the mubtada.", "«öbürü» — mübtedâ."),
  tok("اسْتِيفَاءُ","istifa","noun",[Q, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ اسْتَوْفَى.", "«the exhausting» — the khabar; the masdar of istawfa.", "«eksiksiz sayma» — haber; istevfâ'nın masdarı."),
  tok("أَقْسَامِ","aqsam","noun",[Q, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«of the divisions».", "«kısımlarını»."),
  tok("الشَّيْءِ","shay","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of a thing».", "«bir şeyin».", punct=".")]})

# ----------- s15 — al-Shura 42:49-50: every kind of offspring, none left out
S.append({"id": "s15", "translation": {
 "en": "As He says, exalted is He: «He creates what He wills: He grants to whom He wills DAUGHTERS, and grants to whom He wills SONS, or pairs them, MALES AND FEMALES, and makes whom He wills BARREN» — the divisions of humankind, exhausted." + R_EN,
 "tr": "Nitekim Allah Teâlâ buyurur: «Dilediğini yaratır: dilediğine KIZLAR bağışlar, dilediğine OĞULLAR bağışlar; yahut onları ERKEKLİ DİŞİLİ çift verir, dilediğini de KISIR bırakır» — insanın kısımları eksiksiz sayılmıştır." + R_TR},
 "tokens": [
  kaqh(Q), taala(Q),
  tok("يَخْلُقُ","khalaqa","verb",[Q, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«He creates».", "«yaratır»."),
  tok("مَا","ma-mawsula","pron",[Q, "ism-mawsul", "maful-bihi"], "مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the object.", "«…-diğini» — mef'ûl."),
  tok("يَشَاءُ","shaa","verb",[Q, "ism-mawsul", "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ.", "«He wills».", "«diler».", punct="،"),
  tok("يَهَبُ","wahaba","verb",[Q, "mudari-marfu", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ وَاوِيٌّ سَقَطَتْ وَاوُهُ: الْقِسْمُ الْأَوَّلُ.", "«He grants» — a mithal verb, its waw dropped; the first division.", "«bağışlar» — misâl fiil, vâvı düşmüş; ilk kısım."),
  tok("لِمَنْ","man-mawsula","pron",[Q, "huruf-jarr", "ism-mawsul"], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to whom».", "«…-e».", segments=[seg("لِ","li","part"), seg("مَنْ","man-mawsula","pron")]),
  tok("يَشَاءُ","shaa","verb",[Q, "ism-mawsul", "mudari-marfu", "hollow-verbs"], "صِلَةٌ.", "«He wills».", "«diler»."),
  tok("إِنَاثًا","inath","noun",[Q, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ أُنْثَى.", "«daughters» — the object; the plural of untha.", "«kızlar» — mef'ûl; ünsâ'nın çoğulu."),
  wa_conj("وَيَهَبُ","wahaba","verb",[Q, "atf-nasaq", "mudari-marfu", "mithal-verbs"], "يَهَبُ مَعْطُوفٌ مَرْفُوعٌ — الْقِسْمُ الثَّانِي.", "«and grants» — the second division.", "«ve bağışlar» — ikinci kısım."),
  tok("لِمَنْ","man-mawsula","pron",[Q, "huruf-jarr", "ism-mawsul"], "جَارٌّ وَمَوْصُولٌ.", "«to whom».", "«…-e».", segments=[seg("لِ","li","part"), seg("مَنْ","man-mawsula","pron")]),
  tok("يَشَاءُ","shaa","verb",[Q, "ism-mawsul", "mudari-marfu", "hollow-verbs"], "صِلَةٌ.", "«He wills».", "«diler»."),
  tok("الذُّكُورَ","dhakar","noun",[Q, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ ذَكَرٍ.", "«sons» — the object.", "«oğullar» — mef'ûl."),
  tok("أَوْ","aw","part",[Q, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّقْسِيمِ.", "«or».", "«yahut»."),
  tok("يُزَوِّجُهُمْ","zawwaja","verb",[Q, "atf-nasaq", "mudari-marfu", "form-ii-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَعْطُوفٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْقِسْمُ الثَّالِثُ.", "«pairs them» — the third division; the pronoun its object.", "«onları çift verir» — üçüncü kısım.",
      segments=[seg("يُزَوِّجُ","zawwaja","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("ذُكْرَانًا","dhakar","noun",[Q, "hal", "jam-taksir"], "حَالٌ مَنْصُوبٌ — جَمْعُ ذَكَرٍ عَلَى فُعْلَانٍ، مَصْرُوفٌ.", "«males» — a hal; the plural fuʿlan, fully declined.", "«erkekler» — hâl; fu'lân çoğulu, munsarif."),
  wa_conj("وَإِنَاثًا","inath","noun",[Q, "atf-nasaq", "jam-taksir"], "إِنَاثًا مَعْطُوفٌ مَنْصُوبٌ.", "«and females».", "«ve dişiler»."),
  wa_conj("وَيَجْعَلُ","jaala","verb",[Q, "atf-nasaq", "mudari-marfu", "mafulayn"], "يَجْعَلُ مَعْطُوفٌ مَرْفُوعٌ — يَنْصِبُ مَفْعُولَيْنِ: الْقِسْمُ الرَّابِعُ.", "«and makes» — a two-object verb; the fourth division.", "«ve kılar» — iki mef'ûl alan fiil; dördüncü kısım."),
  tok("مَنْ","man-mawsula","pron",[Q, "ism-mawsul", "maful-bihi"], "مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ أَوَّلُ.", "«whom» — the first object.", "«…-ini» — ilk mef'ûl."),
  tok("يَشَاءُ","shaa","verb",[Q, "ism-mawsul", "mudari-marfu", "hollow-verbs"], "صِلَةٌ.", "«He wills».", "«diler»."),
  tok("عَقِيمًا","aqim","noun",[Q, "maful-bihi", "sifa-mushabbaha"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — فَعِيلٌ بِمَعْنَى فَاعِلٍ يَسْتَوِي فِيهِ الْمُذَكَّرُ وَالْمُؤَنَّثُ.", "«barren» — the second object; faʿil serving both genders.", "«kısır» — ikinci mef'ûl; her iki cinse ortak fa'îl.", punct=".")]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "istifa", "first": [ix(S[-1], "يَهَبُ"), ix(S[-1], "وَيَهَبُ"), ix(S[-1], "يُزَوِّجُهُمْ"), ix(S[-1], "وَيَجْعَلُ")],
                  "second": [ix(S[-1], "إِنَاثًا"), ix(S[-1], "الذُّكُورَ"), ix(S[-1], "ذُكْرَانًا"), ix(S[-1], "عَقِيمًا")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "idkhal": need("idkhal", "إِدْخَال", "د خ ل", "noun", "bringing in, insertion (masdar of أَدْخَلَ)", "sokma, dâhil etme (أَدْخَلَ'nin masdarı)", 4),
 "daw": need("daw", "ضَوْء", "ض و ء", "noun", "light, brightness", "ışık, aydınlık", 3),
 "harr": need("harr", "حَرّ", "ح ر ر", "noun", "heat", "sıcaklık, hararet", 3),
 "tahta": need("tahta", "تَحْتَ", "ت ح ت", "noun", "under, beneath (a zarf of place)", "altında (mekân zarfı)", 2),
 "mutanabbi": need("mutanabbi", "الْمُتَنَبِّي", None, "propn", "al-Mutanabbi — Abu l-Tayyib Ahmad b. al-Husayn, the poet of Sayf al-Dawla (d. 354/965)", "el-Mütenebbî — Ebü't-Tayyib Ahmed b. Hüseyin, Seyfüddevle'nin şairi (ö. 354/965)", 6),
 "rabad": need("rabad", "رَبَض", "ر ب ض", "noun", "the outskirts of a town, its suburb", "varoş, şehrin dış mahallesi", 6, plural="أَرْبَاض"),
 "kharshana": need("kharshana", "خَرْشَنَة", None, "propn", "Kharshana — a Byzantine fort north of Malatya, stormed by Sayf al-Dawla", "Harşene — Malatya'nın kuzeyinde, Seyfüddevle'nin aldığı Rum kalesi", 6),
 "rum": need("rum", "الرُّوم", None, "propn", "the Romans — the Byzantines", "Rumlar — Bizanslılar", 4),
 "salib": need("salib", "صَلِيب", "ص ل ب", "noun", "a cross", "haç, salîb", 4, plural="صُلْبَان"),
 "bia": need("bia", "بِيعَة", None, "noun", "a church (of the Christians)", "kilise", 5, plural="بِيَع"),
 "saby": need("saby", "سَبْي", "س ب ي", "noun", "captivity, taking captive (masdar of سَبَى)", "esir alma, esâret (سَبَى'nın masdarı)", 5),
 "nakaha": need("nakaha", "نَكَحَ", "ن ك ح", "verb", "to marry, to wed (نَكَحَ يَنْكِحُ)", "nikâhlamak, evlenmek (نَكَحَ يَنْكِحُ)", 4, form="I"),
 "walada": need("walada", "وَلَدَ", "و ل د", "verb", "to beget, to bear (وَلَدَ يَلِدُ — a mithal verb)", "doğurmak (وَلَدَ يَلِدُ — misâl fiil)", 3, form="I"),
 "nahb": need("nahb", "نَهْب", "ن ه ب", "noun", "plunder, pillage (masdar of نَهَبَ)", "yağma (نَهَبَ'nin masdarı)", 5),
 "zaraa": need("zaraa", "زَرَعَ", "ز ر ع", "verb", "to sow, to plant (زَرَعَ يَزْرَعُ)", "ekmek, dikmek (زَرَعَ يَزْرَعُ)", 3, form="I"),
 "hassan-ibn-thabit": need("hassan-ibn-thabit", "حَسَّان", None, "propn", "Hassan b. Thabit — the Prophet's poet, of the Ansar (d. c. 54/674)", "Hassân b. Sâbit — Ensâr'dan, Peygamber'in şairi (ö. yak. 54/674)", 5),
 "thabit-name": need("thabit-name", "ثَابِت", None, "propn", "Thabit (in the name Hassan b. Thabit)", "Sâbit (Hassân b. Sâbit adında)", 5),
 "haraba": need("haraba", "حَارَبَ", "ح ر ب", "verb", "to make war on, to fight (Form III)", "harp etmek, savaşmak (III. bâb)", 4, form="III"),
 "darra": need("darra", "ضَرَّ", "ض ر ر", "verb", "to harm (a doubled verb: ضَرَّ يَضُرُّ)", "zarar vermek (muzâaf: ضَرَّ يَضُرُّ)", 3, form="I"),
 "hawala": need("hawala", "حَاوَلَ", "ح و ل", "verb", "to try for, to seek (Form III, hollow)", "istemek, teşebbüs etmek (III. bâb, ecvef)", 4, form="III"),
 "shia": need("shia", "شِيعَة", "ش ي ع", "noun", "a following, the followers of a man", "tâbiler, bir kimsenin taraftarları", 5, plural="أَشْيَاع"),
 "sajiya": need("sajiya", "سَجِيَّة", "س ج و", "noun", "a nature, an inborn disposition", "huy, tabiat, seciye", 5),
 "tilka": need("tilka", "تِلْكَ", None, "pron", "that (feminine demonstrative)", "o, şu (müennes işaret ismi)", 2),
 "khalaiq": need("khalaiq", "خَلِيقَة", "خ ل ق", "noun", "a nature, a disposition", "huy, hilkat", 5, plural="خَلَائِق"),
 "zafir": need("zafir", "زَفِير", "ز ف ر", "noun", "a sighing, the outbreath of grief", "inleme, iç çekiş", 5),
 "shahiq": need("shahiq", "شَهِيق", "ش ه ق", "noun", "a sobbing, the drawn breath of grief", "hıçkırık, nefes alış", 5),
 "khalid-abiding": need("khalid-abiding", "خَالِد", "خ ل د", "noun", "abiding, everlasting (ism fa'il of خَلَدَ)", "kalıcı, ebedî (خَلَدَ'nin ism-i fâili)", 3),
 "dama": need("dama", "دَامَ", "د و م", "verb", "to endure, to last (دَامَ يَدُومُ; مَا دَامَ: as long as — a sister of كَانَ)", "sürmek, devam etmek (دَامَ يَدُومُ; مَا دَامَ: …-dıkça — كَانَ'nin kardeşi)", 3, form="I"),
 "faal": need("faal", "فَعَّال", "ف ع ل", "noun", "ever-doing, one who does much (the intensive فَعَّال)", "çok yapan, hep yapan (فَعَّال mübalağa sîgası)", 4),
 "ata-gift": need("ata-gift", "عَطَاء", "ع ط و", "noun", "a gift, a bestowal (masdar of أَعْطَى; its hamza is a waw turned)", "bağış, atâ (أَعْطَى'nın masdarı; hemzesi vâvdan dönmedir)", 3),
 "majdhudh": need("majdhudh", "مَجْذُوذ", "ج ذ ذ", "noun", "cut off (ism maf'ul of جَذَّ)", "kesilmiş (جَذَّ'nin ism-i mef'ûlü)", 6),
 "laqa-befit": need("laqa-befit", "لَاقَ", "ل ي ق", "verb", "to befit, to suit (لَاقَ يَلِيقُ — hollow)", "yakışmak, uygun düşmek (لَاقَ يَلِيقُ — ecvef)", 4, form="I"),
 "thaqil": need("thaqil", "ثَقِيل", "ث ق ل", "noun", "heavy, weighty", "ağır", 3, plural="ثِقَال"),
 "laqa-meet": need("laqa-meet", "لَاقَى", "ل ق ي", "verb", "to meet, to encounter (Form III, naqis)", "karşılaşmak (III. bâb, nâkıs)", 4, form="III"),
 "khafif": need("khafif", "خَفِيف", "خ ف ف", "noun", "light, quick", "hafif, çevik", 3, plural="خِفَاف"),
 "shadda": need("shadda", "شَدَّ", "ش د د", "verb", "to tighten; شَدَّ عَلَى: to charge upon (doubled: شَدَّ يَشُدُّ)", "sıkmak; شَدَّ عَلَى: hücum etmek (muzâaf: شَدَّ يَشُدُّ)", 4, form="I"),
 "adda-count": need("adda-count", "عَدَّ", "ع د د", "verb", "to count (doubled: عَدَّ يَعُدُّ)", "saymak (muzâaf: عَدَّ يَعُدُّ)", 3, form="I"),
 "istifa": need("istifa", "اسْتِيفَاء", "و ف ي", "noun", "exhausting, taking in full (masdar of اسْتَوْفَى)", "eksiksiz alma, tamamını sayma (اسْتَوْفَى'nın masdarı)", 5),
 "wahaba": need("wahaba", "وَهَبَ", "و ه ب", "verb", "to grant, to give freely (وَهَبَ يَهَبُ — a mithal verb)", "bağışlamak, hibe etmek (وَهَبَ يَهَبُ — misâl fiil)", 3, form="I"),
 "dhakar": need("dhakar", "ذَكَر", "ذ ك ر", "noun", "a male", "erkek", 3, plural="ذُكُور / ذُكْرَان"),
 "zawwaja": need("zawwaja", "زَوَّجَ", "ز و ج", "verb", "to pair, to give in marriage (Form II)", "çift kılmak, evlendirmek (II. bâb)", 4, form="II"),
 "aqim": need("aqim", "عَقِيم", "ع ق م", "noun", "barren (فَعِيل, for both genders)", "kısır (her iki cinse فَعِيل)", 5),
 "shaqi": need("shaqi", "شَقِيّ", "ش ق و", "noun", "wretched, unblessed", "şakî, bedbaht", 4),
 "idhn": need("idhn", "إِذْن", "أ ذ ن", "noun", "leave, permission", "izin", 3),
 "takallama": need("takallama", "تَكَلَّمَ", "ك ل م", "verb", "to speak (Form V)", "konuşmak (V. bâb)", 3, form="V"),
 "aduw": need("aduw", "عَدُوّ", "ع د و", "noun", "an enemy", "düşman", 3, plural="أَعْدَاء"),
 "naf": need("naf", "نَفْع", "ن ف ع", "noun", "benefit, good (masdar of نَفَعَ)", "fayda, menfaat (نَفَعَ'nin masdarı)", 3),
 "muhdath": need("muhdath", "مُحْدَث", "ح د ث", "noun", "newly made, originated (ism maf'ul of أَحْدَثَ)", "sonradan olma, muhdes (أَحْدَثَ'nin ism-i mef'ûlü)", 5),
 "shaqiya": need("shaqiya", "شَقِيَ", "ش ق و", "verb", "to be wretched (شَقِيَ يَشْقَى)", "şakî olmak, bedbaht olmak (شَقِيَ يَشْقَى)", 4, form="I"),
 "mutaaddid": need("mutaaddid", "مُتَعَدِّد", "ع د د", "noun", "many, several things (ism fa'il of تَعَدَّدَ)", "birden çok şey (تَعَدَّدَ'nin ism-i fâili)", 4),
 "watwat": need("watwat", "الْوَطْوَاط", None, "propn", "al-Watwat — Rashid al-Din Muhammad, the Khwarazmian poet and secretary (d. 573/1177)", "el-Vatvât — Reşîdüddîn Muhammed, Hârizmli şair ve kâtip (ö. 573/1177)", 6),
 "jamaa-gather": need("jamaa-gather", "جَمَعَ", "ج م ع", "verb", "to gather, to bring together (جَمَعَ يَجْمَعُ)", "toplamak, bir araya getirmek (جَمَعَ يَجْمَعُ)", 2, form="I"),
 "tafriq": need("tafriq", "تَفْرِيق", "ف ر ق", "noun", "tafriq — striking a difference between two things of one kind (masdar of فَرَّقَ)", "tefrîk — aynı cinsten iki şey arasına fark koymak (فَرَّقَ'nin masdarı)", 5),
 "taqsim": need("taqsim", "تَقْسِيم", "ق س م", "noun", "taqsim — naming many things and then giving each its own (masdar of قَسَّمَ)", "taksîm — birden çok şeyi anıp sonra her birine kendininkini vermek (قَسَّمَ'nin masdarı)", 5),
 "jam": need("jam", "جَمْع", "ج م ع", "noun", "jamʿ — gathering many things under one ruling (masdar of جَمَعَ)", "cem' — birden çok şeyi tek hükümde toplamak (جَمَعَ'nin masdarı)", 3),
}
for k in ("qawl", "min", "huwa", "hiya", "an-masdariyya", "adkhala", "farraqa", "bayna", "wa", "fa", "pron-3fs", "pron-3ms", "pron-2ms", "pron-1s", "pron-3mp", "pron-3d",
          "nafaa", "saida", "alima", "ata", "khalaqa", "shaa", "jaala", "arada", "atlaqa", "aqama", "daa", "maa", "thumma", "aw", "hatta", "ala", "bi", "fi", "ila", "li", "ka",
          "la-nafiya", "illa", "inna", "amma", "alladhina", "ma-mawsula", "man-mawsula", "idha", "qad", "kull", "shay", "dhikr", "amr", "ahad", "akhar", "mudaf", "hukm", "mana",
          "jiha", "thani", "awwal", "aqsam", "wajh", "qalb", "nar", "qatl", "walad", "qawm", "sharr", "bida", "ghayr", "yawm", "nafs", "said", "rabb", "janna", "samawat", "ard",
          "kathir", "qalil", "taala", "ibn", "mal", "ahwal", "inath"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
# stems WITHOUT their sukun, the amr with its wasl vowel (wave-19 lesson); the doubled verbs through entry() with the fakk stems
put_morph(mo, "nakaha", _sg.sound1("daraba", "نَكَح", "نْكِح", "اِنْكِح", "نِكَاح", "نَاكِح", maful="مَنْكُوح", pmz="نُكِحَ", pmd="يُنْكَحُ"))
put_morph(mo, "walada", _sg.sound1("daraba", "وَلَد", "لِد", "لِد", "وِلَادَة", "وَالِد", maful="مَوْلُود", pmz="وُلِدَ", pmd="يُولَدُ", cls="مِثَالٌ وَاوِيٌّ",
                                   note="مِثَالٌ وَاوِيٌّ مِنْ بَابِ ضَرَبَ: وَلَدَ يَلِدُ — تَسْقُطُ الْوَاوُ فِي الْمُضَارِعِ وَالْأَمْرِ."))
put_morph(mo, "zaraa", _sg.sound1("fataha", "زَرَع", "زْرَع", "اِزْرَع", "زَرْع", "زَارِع", maful="مَزْرُوع", pmz="زُرِعَ", pmd="يُزْرَعُ"))
put_morph(mo, "wahaba", _sg.sound1("fataha", "وَهَب", "هَب", "هَب", "هِبَة", "وَاهِب", maful="مَوْهُوب", pmz="وُهِبَ", pmd="يُوهَبُ", cls="مِثَالٌ وَاوِيٌّ",
                                   note="مِثَالٌ وَاوِيٌّ: وَهَبَ يَهَبُ — سَقَطَتِ الْوَاوُ فِي الْمُضَارِعِ لِوُقُوعِهَا بَيْنَ يَاءٍ وَفَتْحَةٍ (بَابُ فَتَحَ لِحَلْقِيَّةِ الْعَيْنِ)."))
put_morph(mo, "haraba", _sg.derived(_sg.B3, _sg.W3, "ُ", "حَارَب", "حَارِب", "حَارِب", "مُحَارَبَة", "مُحَارِب", "مُحَارَب", "حُورِبَ", "يُحَارَبُ"))
put_morph(mo, "hawala", _sg.derived(_sg.B3, _sg.W3, "ُ", "حَاوَل", "حَاوِل", "حَاوِل", "مُحَاوَلَة", "مُحَاوِل", "مُحَاوَل", "حُووِلَ", "يُحَاوَلُ"))
put_morph(mo, "zawwaja", _sg.derived(_sg.B2, _sg.W2, "ُ", "زَوَّج", "زَوِّج", "زَوِّج", "تَزْوِيج", "مُزَوِّج", "مُزَوَّج", "زُوِّجَ", "يُزَوَّجُ"))
put_morph(mo, "laqa-meet", _sg.derived_naqis(_sg.B3, _sg.W3, "ُ", "لَاقَ", "لَاق", "i", "لَاق", "مُلَاقَاة", "مُلَاقٍ (الْمُلَاقِي)", "مُلَاقًى", "لُوقِيَ", "يُلَاقَى",
                                             "نَاقِصٌ عَلَى فَاعَلَ: لَاقَى يُلَاقِي — لَاقَوْا: حُذِفَتِ الْأَلِفُ قَبْلَ وَاوِ الْجَمَاعَةِ."))
put_morph(mo, "laqa-befit", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "لَاق", "لِق", "لِيق", "لِق", "لِيق", "لِق", "لِيَاقَة", "لَائِق",
                                        note="أَجْوَفُ يَائِيٌّ مِنْ بَابِ ضَرَبَ: لَاقَ يَلِيقُ — يَلِيقُ بِهِ: يُنَاسِبُهُ؛ لَازِمٌ."))
put_morph(mo, "dama", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "دَام", "دُم", "دُوم", "دُم", "دُوم", "دُم", "دَوَام", "دَائِم",
                                  note="أَجْوَفُ وَاوِيٌّ: دَامَ يَدُومُ — وَمَا دَامَ مِنْ أَخَوَاتِ كَانَ: تَرْفَعُ الِاسْمَ وَتَنْصِبُ الْخَبَرَ."))
def gem(bab_key, L, F, yv, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    # a DOUBLED verb of Form I: the contracted stems (L) and the fakk stems (F) before a sakin ending
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
put_morph(mo, "darra", gem("nasara", "ضَرّ", "ضَرَر", "َ", "ضُرّ", "ضْرُر", ["ضُرَّ", "ضُرَّا", "ضُرُّوا", "ضُرِّي", "ضُرَّا", "اُضْرُرْنَ"], "ضَرّ", "ضَارّ", "مَضْرُور", "ضُرَّ", "يُضَرُّ",
                        "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: ضَرَّ يَضُرُّ — ضَرَرْتُ، يَضْرُرْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ."))
put_morph(mo, "shadda", gem("nasara", "شَدّ", "شَدَد", "َ", "شُدّ", "شْدُد", ["شُدَّ", "شُدَّا", "شُدُّوا", "شُدِّي", "شُدَّا", "اُشْدُدْنَ"], "شَدّ", "شَادّ", "مَشْدُود", "شُدَّ", "يُشَدُّ",
                         "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: شَدَّ يَشُدُّ — شَدُّوا عَلَى الْعَدُوِّ: حَمَلُوا."))
put_morph(mo, "adda-count", gem("nasara", "عَدّ", "عَدَد", "َ", "عُدّ", "عْدُد", ["عُدَّ", "عُدَّا", "عُدُّوا", "عُدِّي", "عُدَّا", "اُعْدُدْنَ"], "عَدّ", "عَادّ", "مَعْدُود", "عُدَّ", "يُعَدُّ",
                             "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: عَدَّ يَعُدُّ — عُدُّوا: مَبْنِيٌّ لِلْمَجْهُولِ."))
# the passives the chapter's own forms need on paradigms stored without them
if "saida" in mo["verbs"] and not mo["verbs"]["saida"].get("majhulMazi"):
    mo["verbs"]["saida"]["majhulMazi"], mo["verbs"]["saida"]["majhulMudari"] = "سُعِدَ", "يُسْعَدُ"
# a verb copied in from another package brings its paradigm with it (the release gate wants every glossary verb conjugated)
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_C = {
 "id": "jam-maa-tafriq-taqsim",
 "title": {"ar": "الْجَمْعُ مَعَ التَّفْرِيقِ، وَمَعَ التَّقْسِيمِ، وَمَعَ كِلَيْهِمَا", "en": "The compound figures — jamʿ with tafriq, with taqsim, with both", "tr": "Mürekkeb sanatlar — cem' ma'a't-tefrîk, ma'a't-taksîm, ma'a kileyhimâ"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الجمع مع التفريق: أن يدخل شيئان في معنى ويفرق بين جهتي الإدخال؛ الجمع مع التقسيم: جمع متعدد تحت حكم ثم تقسيمه أو تقسيمه ثم جمعه؛ الجمع مع التفريق والتقسيم"],
 "question": {
  "en": ["Are two things put into ONE likeness and then told apart by the SIDE each enters from? «Your face is like the fire in its light, my heart like the fire in its heat» — one fire, two sides. JAMʿ WITH TAFRIQ.",
         "Are many things gathered under one ruling and then DEALT OUT one by one — or dealt out first and gathered after? Mutanabbi: the Romans, the crosses and the churches are wretched (jamʿ) — to captivity, to slaughter, to plunder, to fire (taqsim). Hassan: when they war they harm, when they seek good they do good (taqsim) — THAT is a nature in them (jamʿ). JAMʿ WITH TAQSIM.",
         "All three at once? Hud 105-108: no soul speaks without His leave (jamʿ) — of them the wretched and the blessed (tafriq) — as for the wretched, the Fire; as for the blessed, the Garden (taqsim).",
         "What does the engine read? The single figures on each sentence — a list under one seat, a shared mushabbah bihi with two wajhs, أَمَّا-shares, مِنْهُمْ-partitions — and then the COMPOUND off their order, within a sentence or across the next one."],
  "tr": ["İki şey TEK bir benzetmeye sokulup sonra her birinin girdiği CİHETLE mi ayrılıyor? «Yüzün ışığıyla ateş gibi, kalbim sıcaklığıyla ateş gibi» — tek ateş, iki cihet. CEM' MA'A'T-TEFRÎK.",
         "Birden çok şey tek hükümde toplanıp sonra tek tek DAĞITILIYOR mu — yahut önce dağıtılıp sonra mı toplanıyor? Mütenebbî: Rumlar, haçlar, kiliseler perişandır (cem') — esârete, katle, yağmaya, ateşe (taksîm). Hassân: harp edince zarar, iyilik isteyince fayda (taksîm) — O onlarda bir huydur (cem'). CEM' MA'A'T-TAKSÎM.",
         "Üçü birden? Hûd 105-108: hiçbir nefis izinsiz konuşamaz (cem') — kimi şakî kimi saîd (tefrîk) — şakî olanlar ateşte, saîd olanlar cennette (taksîm).",
         "Motor neyi okur? Her cümledeki tek sanatları — tek koltuk altında liste, iki vechli ortak müşebbehün bih, أَمَّا payları, مِنْهُمْ bölmeleri — sonra sıralarından MÜREKKEBİ, cümle içinde yahut bir sonrakine geçerek."]},
 "plain": {
  "en": "Three compound figures: jamʿ with tafriq (one likeness, two sides), jamʿ with taqsim (a gathering and a dealing-out, in either order) and jamʿ with both. The engine reads the single figures on each sentence and names the compound from the way they follow one another.",
  "tr": "Üç mürekkeb sanat: cem' ma'a't-tefrîk (tek benzetme, iki cihet), cem' ma'a't-taksîm (toplama ve dağıtma, iki sırayla da) ve ikisiyle birlikte cem'. Motor her cümledeki tek sanatları okur ve birbirini izleyişlerinden mürekkebi adlandırır."},
 "explanation": {
  "en": "The JAMʿ WITH TAFRIQ is أَنْ يُدْخَلَ شَيْئَانِ فِي مَعْنًى وَيُفَرَّقَ بَيْنَ جِهَتَيِ الْإِدْخَالِ — two things ENTER one meaning, and the two SIDES of that entry are set apart. Al-Watwat: فَوَجْهُكَ كَالنَّارِ فِي ضَوْئِهَا وَقَلْبِيَ كَالنَّارِ فِي حَرِّهَا — face and heart both enter «the fire» (the jamʿ), the face by its light and the heart by its heat (the tafriq). The JAMʿ WITH TAQSIM is جَمْعُ مُتَعَدِّدٍ تَحْتَ حُكْمٍ ثُمَّ تَقْسِيمُهُ، أَوْ تَقْسِيمُهُ ثُمَّ جَمْعُهُ: al-Mutanabbi gathers the Romans, the crosses and the churches under «are wretched through him», then deals out — to captivity what they wedded, to slaughter what they begot, to plunder what they gathered, to fire what they sowed; Hassan deals out first — when they war they harm, when they seek good they do good — and gathers after: سَجِيَّةٌ تِلْكَ مِنْهُمْ, THAT is one nature in them. The JAMʿ WITH BOTH is Hud 105-108: لَا تَكَلَّمُ نَفْسٌ إِلَّا بِإِذْنِهِ gathers every soul under one ruling; فَمِنْهُمْ شَقِيٌّ وَسَعِيدٌ parts them in two; فَأَمَّا الَّذِينَ شَقُوا فَفِي النَّارِ … وَأَمَّا الَّذِينَ سُعِدُوا فَفِي الْجَنَّةِ hands each part its own. WHAT THE ENGINE CLAIMS: it reads the single figures by their seats — a wāw-list standing as one doer or one mubtada, a demonstrative that gathers the previous shares, the negated indefinite that covers all, the مِنْهُمْ partition, the أَمَّا shares, the repeated head with its objects — and then composes the compound: two likenings sharing one bihi with two wajhs in ONE sentence are the jamʿ with tafriq; a jamʿ followed by a taqsim (or the reverse) in the NEXT sentence is the jamʿ with taqsim, its order named; a jamʿ and a tafriq followed by أَمَّا-shares is the jamʿ with both.",
  "tr": "CEM' MA'A'T-TEFRÎK أَنْ يُدْخَلَ شَيْئَانِ فِي مَعْنًى وَيُفَرَّقَ بَيْنَ جِهَتَيِ الْإِدْخَالِ'dir — iki şey tek mânâya GİRER ve girişin iki CİHETİ ayrılır. Vatvât: فَوَجْهُكَ كَالنَّارِ فِي ضَوْئِهَا وَقَلْبِيَ كَالنَّارِ فِي حَرِّهَا — yüz de kalp de «ateşe» girer (cem'), yüz ışığıyla, kalp sıcaklığıyla (tefrîk). CEM' MA'A'T-TAKSÎM جَمْعُ مُتَعَدِّدٍ تَحْتَ حُكْمٍ ثُمَّ تَقْسِيمُهُ، أَوْ تَقْسِيمُهُ ثُمَّ جَمْعُهُ'dur: Mütenebbî Rumları, haçları, kiliseleri «onunla perişandır» altında toplar, sonra dağıtır — esârete nikâhladıkları, katle doğurdukları, yağmaya topladıkları, ateşe ektikleri; Hassân önce dağıtır — harp edince zarar, iyilik isteyince fayda — sonra toplar: سَجِيَّةٌ تِلْكَ مِنْهُمْ, O onlarda tek bir huydur. İKİSİYLE BİRLİKTE CEM' Hûd 105-108'dir: لَا تَكَلَّمُ نَفْسٌ إِلَّا بِإِذْنِهِ her nefsi tek hükümde toplar; فَمِنْهُمْ شَقِيٌّ وَسَعِيدٌ ikiye ayırır; فَأَمَّا الَّذِينَ شَقُوا فَفِي النَّارِ … وَأَمَّا الَّذِينَ سُعِدُوا فَفِي الْجَنَّةِ her paya kendininkini verir. MOTORUN İDDİASI: tek sanatları koltuklarından okur — tek fâil yahut tek mübtedâ olarak duran vâvlı liste, önceki payları toplayan işaret ismi, hepsini kuşatan nefiy içindeki nekre, مِنْهُمْ bölmesi, أَمَّا payları, mef'ûlleriyle tekrarlanan baş — sonra mürekkebi kurar: TEK cümlede tek bir müşebbehün bihi iki vechle paylaşan iki benzetme cem' ma'a't-tefrîktir; bir cem'in SONRAKİ cümlede taksîmle izlenmesi (yahut tersi) sırası adlandırılmış cem' ma'a't-taksîmdir; cem' ve tefrîkin أَمَّا paylarıyla izlenmesi ikisiyle birlikte cem'dir."},
 "examples": [
  {"ar": "فَوَجْهُكَ كَالنَّارِ فِي ضَوْئِهَا * وَقَلْبِيَ كَالنَّارِ فِي حَرِّهَا", "en": "al-Watwat — jamʿ with tafriq.", "tr": "Vatvât — cem' ma'a't-tefrîk.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "تَشْقَى بِهِ الرُّومُ وَالصُّلْبَانُ وَالْبِيَعُ * لِلسَّبْيِ مَا نَكَحُوا وَالْقَتْلِ مَا وَلَدُوا", "en": "al-Mutanabbi — jamʿ, then taqsim.", "tr": "Mütenebbî — cem', sonra taksîm.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "قَوْمٌ إِذَا حَارَبُوا ضَرُّوا عَدُوَّهُمْ * سَجِيَّةٌ تِلْكَ مِنْهُمْ غَيْرُ مُحْدَثَةٍ", "en": "Hassan — taqsim, then jamʿ.", "tr": "Hassân — taksîm, sonra cem'.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "لَا تَكَلَّمُ نَفْسٌ إِلَّا بِإِذْنِهِ فَمِنْهُمْ شَقِيٌّ وَسَعِيدٌ", "en": "11:105 — jamʿ and tafriq; the taqsim follows.", "tr": "Hûd 105 — cem' ve tefrîk; taksîm ardından gelir.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«İki teşbih yan yana gelince cem' ma'a't-tefrîk olur»",
   "right": "«Cem' ma'a't-tefrîk, iki müşebbehin TEK müşebbehün bihe girip vechlerinin AYRILMASIDIR; iki ayrı benzetme sadece iki benzetmedir»",
   "why": {"en": "The definition asks for one meaning entered and two sides parted — the shared bihi is the jamʿ, the two wajhs the tafriq.", "tr": "Tarif tek mânâya girişi ve iki cihetin ayrılmasını ister — ortak bih cem', iki vech tefrîktir."}}],
 "relatedNotes": ["jam", "tafriq", "taqsim", "tashbih", "amma-tafsiliyya", "ilm-al-badi"]}

NOTE_Q2 = {
 "id": "taqsim-al-ahwal-wal-istifa",
 "title": {"ar": "التَّقْسِيمُ بِمَعْنَيَيْنِ آخَرَيْنِ — ذِكْرُ أَحْوَالِ الشَّيْءِ مُضَافًا إِلَى كُلٍّ مَا يَلِيقُ بِهِ، وَاسْتِيفَاءُ أَقْسَامِهِ", "en": "The taqsim in two more senses — the states of a thing, each with what befits it; the exhaustive division", "tr": "İki mânâda daha taksîm — bir şeyin hâlleri, her birine yakışanıyla; kısımların eksiksiz sayılması"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — وقد يطلق التقسيم على أمرين آخرين: أحدهما ذكر أحوال الشيء مضافا إلى كل ما يليق به؛ والثاني استيفاء أقسام الشيء"],
 "question": {
  "en": ["Are the STATES of one thing named, each with what befits it? «Heavy when they meet, light when called, many when they charge, few when counted» — four states, four fitting things. That is the taqsim of states.",
         "Are ALL the divisions of a thing counted out, none left? «He grants daughters, grants sons, pairs them male and female, makes barren» — the four lots of offspring, exhausted. That is the taqsim of istifaʾ.",
         "What does the engine look for? Adjective + إِذَا-clause pairs, two or more; or one verb-head repeated over a list of objects, three or more."],
  "tr": ["Tek şeyin HÂLLERİ, her birine yakışanıyla mı anılıyor? «Karşılaşınca ağır, çağrılınca hafif, hücum edince çok, sayılınca az» — dört hâl, dört yakışan. Ahvâl taksîmi budur.",
         "Bir şeyin BÜTÜN kısımları eksiksiz mi sayılıyor? «Kızlar bağışlar, oğullar bağışlar, erkekli dişili çift verir, kısır bırakır» — evlâdın dört payı, eksiksiz. İstîfâ taksîmi budur.",
         "Motor neye bakar? Sıfat + إِذَا cümlesi çiftleri, iki yahut daha çok; yahut bir mef'ûl listesi üzerinde tekrarlanan tek fiil başı, üç yahut daha çok."]},
 "plain": {
  "en": "Two more things are called taqsim: naming a thing's states with what befits each (Mutanabbi's heavy / light / many / few), and exhausting a thing's divisions (42:49-50: daughters, sons, both, barren). The engine reads the adjective-and-إِذَا pairs and the repeated verb over its objects.",
  "tr": "İki şeye daha taksîm denir: bir şeyin hâllerini her birine yakışanıyla anmak (Mütenebbî'nin ağır / hafif / çok / az'ı) ve bir şeyin kısımlarını eksiksiz saymak (Şûrâ 49-50: kızlar, oğullar, ikisi, kısır). Motor sıfat-إِذَا çiftlerini ve mef'ûlleri üzerinde tekrarlanan fiili okur."},
 "explanation": {
  "en": "The Talkhis adds: وَقَدْ يُطْلَقُ التَّقْسِيمُ عَلَى أَمْرَيْنِ آخَرَيْنِ. The first is ذِكْرُ أَحْوَالِ الشَّيْءِ مُضَافًا إِلَى كُلٍّ مَا يَلِيقُ بِهِ — al-Mutanabbi on the shaykhs: ثِقَالٍ إِذَا لَاقَوْا خِفَافٍ إِذَا دُعُوا كَثِيرٍ إِذَا شَدُّوا قَلِيلٍ إِذَا عُدُّوا: heavy in the meeting, light at the call, many in the charge, few in the count — every state joined to the thing that befits it. The second is اسْتِيفَاءُ أَقْسَامِ الشَّيْءِ — al-Shura 49-50: يَهَبُ لِمَنْ يَشَاءُ إِنَاثًا وَيَهَبُ لِمَنْ يَشَاءُ الذُّكُورَ أَوْ يُزَوِّجُهُمْ ذُكْرَانًا وَإِنَاثًا وَيَجْعَلُ مَنْ يَشَاءُ عَقِيمًا: daughters only, sons only, both, none — the whole of what a household can be, and nothing outside it. WHAT THE ENGINE CLAIMS: the states-taqsim is two or more pairs of a sifa-shaped word and an إِذَا-clause (read off the adjective shape and the shart zarf); the exhaustive taqsim is one verb-head repeated (with its wāw or أَوْ) over three or more objects — the repetition is the sign, the exhaustiveness the reader's judgement.",
  "tr": "Telhîs ekler: وَقَدْ يُطْلَقُ التَّقْسِيمُ عَلَى أَمْرَيْنِ آخَرَيْنِ. İlki ذِكْرُ أَحْوَالِ الشَّيْءِ مُضَافًا إِلَى كُلٍّ مَا يَلِيقُ بِهِ — Mütenebbî şeyhler için: ثِقَالٍ إِذَا لَاقَوْا خِفَافٍ إِذَا دُعُوا كَثِيرٍ إِذَا شَدُّوا قَلِيلٍ إِذَا عُدُّوا: karşılaşmada ağır, çağrıda hafif, hücumda çok, sayımda az — her hâl kendine yakışanla. İkincisi اسْتِيفَاءُ أَقْسَامِ الشَّيْءِ — Şûrâ 49-50: يَهَبُ لِمَنْ يَشَاءُ إِنَاثًا وَيَهَبُ لِمَنْ يَشَاءُ الذُّكُورَ أَوْ يُزَوِّجُهُمْ ذُكْرَانًا وَإِنَاثًا وَيَجْعَلُ مَنْ يَشَاءُ عَقِيمًا: yalnız kız, yalnız oğul, ikisi, hiçbiri — bir hânenin olabileceği her şey, dışında hiçbir şey yok. MOTORUN İDDİASI: ahvâl taksîmi sıfat şeklinde bir kelime ile bir إِذَا cümlesinin iki yahut daha çok çifti (sıfat şekli ve şart zarfından okunur); istîfâ taksîmi üç yahut daha çok mef'ûl üzerinde (vâv yahut أَوْ ile) tekrarlanan tek fiil başı — tekrar alâmettir, eksiksizlik okuyucunun hükmü."},
 "examples": [
  {"ar": "ثِقَالٍ إِذَا لَاقَوْا خِفَافٍ إِذَا دُعُوا * كَثِيرٍ إِذَا شَدُّوا قَلِيلٍ إِذَا عُدُّوا", "en": "al-Mutanabbi — the states.", "tr": "Mütenebbî — hâller.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "يَهَبُ لِمَنْ يَشَاءُ إِنَاثًا وَيَهَبُ لِمَنْ يَشَاءُ الذُّكُورَ أَوْ يُزَوِّجُهُمْ ذُكْرَانًا وَإِنَاثًا وَيَجْعَلُ مَنْ يَشَاءُ عَقِيمًا", "en": "42:49-50 — the divisions exhausted.", "tr": "Şûrâ 49-50 — kısımlar eksiksiz.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"}],
 "commonMistakes": [
  {"wrong": "«İstîfâ, uzun bir listedir»",
   "right": "«İstîfâ, kısımların TAMAMININ sayılmasıdır — dışarıda kalan kısım varsa taksîm, istîfâ değildir»",
   "why": {"en": "The name is taken from exhausting (istifaʾ) — the count must close.", "tr": "Ad, eksiksiz almadan (istîfâ) gelir — sayım kapanmalıdır."}}],
 "relatedNotes": ["taqsim", "jam-maa-tafriq-taqsim", "idha-shartiyya", "sifa-mushabbaha", "ilm-al-badi"]}

ADD_EN = (" Chapter 62 (lines ~4130-4170, sahifa 142-144) carries the jamʿ with tafriq (al-Watwat, s2), the jamʿ with taqsim in both orders "
          "(al-Mutanabbi s4-s5, Hassan b. Thabit s6-s7), the jamʿ with both (Hud 11:105-108, s9-s11) and the two other taqsims (al-Mutanabbi s13; "
          "al-Shura 42:49-50, s15) — the verse and the ayas are the source's printed Arabic; the source prints خرشنة as حرشنة and وَالْأَرْضُ once as "
          "ولارض (slips of the press), printed here in their known form. s1, s3, s8, s12, s14 (the definitions) are RESTORED, NOT QUOTED: the source "
          "carries those steps only in its Ottoman-Turkish gloss, and the Arabic restores the matn's wording in the author's own idiom; each is marked "
          "«restored» in its translation. The examples carry `badi` frames (jam / tafriq / taqsim with their subs; the compounds as `with`-links to the "
          "partner sentence).")
ADD_TR = (" Altmış ikinci bâb (satır ~4130-4170, sahife 142-144) cem' ma'a't-tefrîki (Vatvât, s2), iki sırasıyla cem' ma'a't-taksîmi (Mütenebbî s4-s5, "
          "Hassân b. Sâbit s6-s7), ikisiyle birlikte cem'i (Hûd 105-108, s9-s11) ve iki taksîmi daha (Mütenebbî s13; Şûrâ 49-50, s15) taşır — beyitler "
          "ve âyetler kaynağın bastığı Arapçadır; kaynak خرشنة'yi حرشنة ve وَالْأَرْضُ'yu bir kez ولارض basar (baskı sürçmesi), burada bilinen "
          "şekliyle basılmıştır. s1, s3, s8, s12, s14 (tarifler) ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla "
          "taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Örnekler `badi` "
          "çerçeveleri taşır (cem' / tefrîk / taksîm, alt türleriyle; mürekkebler eş cümleye `with` bağıyla).")
write_out(62, S, TITLE, ADD_EN, ADD_TR, "4130-4170", GLOSS_ADD, notes=(NOTE_C, NOTE_Q2),
          related=(("jam", ["jam-maa-tafriq-taqsim"]), ("tafriq", ["jam-maa-tafriq-taqsim"]), ("taqsim", ["jam-maa-tafriq-taqsim", "taqsim-al-ahwal-wal-istifa"]),
                   ("ilm-al-badi", ["jam-maa-tafriq-taqsim", "taqsim-al-ahwal-wal-istifa"])))
report(62, S, GLOSS_ADD, (NOTE_C, NOTE_Q2))
