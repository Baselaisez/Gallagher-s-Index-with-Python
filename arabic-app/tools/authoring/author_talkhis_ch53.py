# -*- coding: utf-8 -*-
"""Author chapter 53 of talkhis-al-miftah — الِاسْتِعَارَةُ بِاعْتِبَارِ اللَّفْظِ
وَالْمُلَائِمِ (sahifa 126-128, lines ~3640-3720): the asliyya and the tabaʿiyya
(the verb, its derivatives and the particle; the seat of the tabaʿiyya's clue:
faʿil, mafʿul, second mafʿul, majrur), the mutlaqa / mujarrada / murashshaha by
the mulaʾim, the tanasi of the tashbih, and the majaz murakkab (the tamthil and
the mathal).

  RESTORED (the source carries the step only in Turkish): s1-s5, s7-s8, s12-s14,
          s16, s19-s20, s23-s25, and the frames of the examples.
  As printed: the ayat 28:8 (s6), 9:34 (s11), 2:16 (s17); the hemistich of s9,
          the bayts of s10, s15, s21, s22 and Zuhayr's (s18).

Every istiʿara carries an authored `majaz` frame with an `istiara` object; the
mulaʾim words are named by index (mulaimMinhu / mulaimLahu) so the engine's
tarshih / tajrid reading is graded against them.
"""
import json, pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PKG = ROOT / "content/samples/talkhis-al-miftah"
sys.path.insert(0, str(ROOT / "tools/authoring"))
import sarf_gen as _sg
DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)
def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
def find_gloss(key):
    for p in sorted((ROOT / "content/samples").iterdir()):
        gp = p / "glossary.json"
        if gp.exists():
            d = json.loads(gp.read_text(encoding="utf-8"))["entries"]
            if key in d: return d[key]
    raise KeyError(key)
def find_morph(key):
    for p in sorted((ROOT / "content/samples").iterdir()):
        gp = p / "morphology.json"
        if gp.exists():
            d = json.loads(gp.read_text(encoding="utf-8"))["verbs"]
            if key in d: return d[key]
    raise KeyError(key)
def mj(word, kind, alaqa=None, haqiqa=None, murad=None, qarina=None, istiara=None):
    f = {"word": word, "kind": kind}
    if alaqa: f["alaqa"] = alaqa
    if haqiqa: f["haqiqa"] = haqiqa
    if murad: f["murad"] = murad
    if qarina is not None: f["qarina"] = qarina
    if istiara: f["istiara"] = istiara
    return f
def ist(lafz, ends=None, jami=None, hissi=None, seat=None, mulaim=None, minhu=None, lahu=None):
    d = {"lafz": lafz}
    if ends: d["ends"] = ends
    if jami: d["jami"] = jami
    if hissi: d["hissi"] = hissi
    if seat: d["qarinaSeat"] = seat
    if mulaim: d["mulaim"] = mulaim
    if minhu: d["mulaimMinhu"] = minhu
    if lahu: d["mulaimLahu"] = lahu
    return d
S = []
T = "istiara-tabaiyya"; R = "tarshih-wa-tajrid"; K = "majaz-murakkab"; A = "aqsam-al-istiara"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
TITLE53 = {"ar": "الِاسْتِعَارَةُ بِاعْتِبَارِ اللَّفْظِ وَالْمُلَائِمِ، وَالْمَجَازُ الْمُرَكَّبُ",
           "en": "The Istiʿara by the Word and by the Mulaʾim, and the Compound Majaz",
           "tr": "Lafız ve Mülâim İtibariyle İstiâre, ve Mürekkeb Mecaz"}
def kaq(full="كَقَوْلِهِ", who="pron-3ms", punct=":", tag=T):
    pr = {"pron-3ms": "هِ", "pron-3mp": "هِمْ", "pron-2ms": "كَ"}[who]
    return tok(full, "qawl", "noun", [tag, "huruf-jarr", "idafa-definiteness"],
               "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
               "«as in his/your saying» — the kaf of «for instance», a wall: no likening.", "«sözü gibi» — «meselâ» kâfı, duvar: benzetme değil.",
               segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), seg(pr, who, "pron")], punct=punct)
TAALA = tok("تَعَالَى", "taala", "verb", [T], "فِعْلٌ مَاضٍ جَامِدٌ فِي مَعْنَى الدُّعَاءِ — لَا يَجْرِي عَلَى اللهِ إِلَّا مَاضِيًا.", "«exalted is He» — the frozen mazi of praise.", "«teâlâ» — ta'zim mâzîsi.", punct=":")
def kawa(full="وَكَقَوْلِهِ", who="pron-3ms", tag=T):
    t = kaq(full, who, ":", tag); t["segments"].insert(0, seg("وَ", "wa", "conj")); return t

# ----------- s1 — by the word: two kinds (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "And regarded by the borrowed WORD it is of two kinds: the asliyya and the tabaʿiyya." + R_EN,
 "tr": "Ödünç alınan LAFIZ itibariyle iki kısımdır: asliyye ve tebeiyye." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[T, "huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَاعْتِبَارِ مُضَافٌ.", "«and by the regard of» — jarr, the khabar brought forward; a mudaf.", "«ve itibariyle» — câr-mecrûr, öne alınmış haber; muzâf.",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("اللَّفْظِ","lafz","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the word» — mudaf ilayh.", "«lafız» — muzâfun ileyh."),
  tok("الْمُسْتَعَارِ","mustaar","noun",[T, "naat-sifa", "ism-maful"], "نَعْتٌ لِلَّفْظِ مَجْرُورٌ — اسْمُ مَفْعُولٍ.", "«the borrowed» — a na't of the word; ism maf'ul.", "«ödünç alınan» — lafzın na'ti; ism-i mef'ûl."),
  tok("قِسْمَانِ","qism","noun",[T, "mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds» — the mubtada, held back; raf' by the alif.", "«iki kısım» — geriye bırakılmış mübtedâ; elifle merfû.", punct=":"),
  tok("أَصْلِيَّةٌ","asliyya","noun",[T, "badal", "ism-mansub"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ.", "«an asliyya» — badal of detail.", "«asliyye» — tafsîl bedeli."),
  tok("وَتَبَعِيَّةٌ","tabaiyya","noun",[T, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and a tabaʿiyya» — joined.", "«ve tebeiyye» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("تَبَعِيَّةٌ","tabaiyya","noun")], punct=".")]})

# ----------- s2 — the asliyya (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "The asliyya is that in which the borrowed word is a NOUN OF A KIND — as «lion» for the brave man and «killing» for the hard beating." + R_EN,
 "tr": "Asliyye, ödünç alınan lafzın CİNS İSMİ olduğu istiâredir — cesur adam için «arslan», şiddetli dövme için «öldürme» gibi." + R_TR},
 "tokens": [
  tok("فَالْأَصْلِيَّةُ","asliyya","noun",[T, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْأَصْلِيَّةُ مُبْتَدَأٌ.", "«so the asliyya» — the mubtada.", "«asliyye» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْأَصْلِيَّةُ","asliyya","noun")]),
  tok("مَا","ma-mawsula","pron",[T, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the relative, the khabar.", "«… olan» — mevsûl, haber."),
  tok("كَانَ","kana","verb",[T, "kana-wa-akhawatuha", "ism-mawsul"], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةُ الْمَوْصُولِ.", "«is» — kana; the sila.", "«olan» — kâne; sıla."),
  tok("الْمُسْتَعَارُ","mustaar","noun",[T, "kana-wa-akhawatuha", "ism-maful"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the borrowed word» — the ism of kana.", "«ödünç alınan» — kânenin ismi."),
  tok("فِيهَا","fi","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — أَيْ فِي الِاسْتِعَارَةِ.", "«in it» — in the istiʿara.", "«onda» — istiârede.",
      segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("اسْمَ","ism","noun",[T, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«a noun» — the khabar of kana, a mudaf.", "«ismi» — kânenin haberi, muzâf."),
  tok("جِنْسٍ","jins","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of a kind» — mudaf ilayh.", "«cins» — muzâfun ileyh.", punct="،"),
  tok("كَأَسَدٍ","asad","noun",[T, "huruf-jarr"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ، لَا تَشْبِيهَ؛ أَسَدٍ مَجْرُورٌ.", "«as ‹lion›» — the kaf of «for instance», a wall: no likening here.", "«‹arslan› gibi» — «meselâ» kâfı, duvar: benzetme değil.",
      segments=[seg("كَ","ka","part"), seg("أَسَدٍ","asad","noun")]),
  tok("لِلرَّجُلِ","rajul","noun",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — لِلْمُسْتَعَارِ لَهُ.", "«for the man» — the one it is lent to.", "«adam için» — müsteârun leh.",
      segments=[seg("لِ","li","part"), seg("الرَّجُلِ","rajul","noun")]),
  tok("الشُّجَاعِ","shujaa","noun",[T, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«the brave» — a na't.", "«cesur» — na't."),
  tok("وَقَتْلٍ","qatl","noun",[T, "atf-nasaq", "masdar"], "مَعْطُوفٌ عَلَى أَسَدٍ مَجْرُورٌ — مَصْدَرٌ.", "«and ‹killing›» — joined to «lion»; a masdar.", "«ve ‹öldürme›» — «arslan»a matuf; masdar.",
      segments=[seg("وَ","wa","conj"), seg("قَتْلٍ","qatl","noun")]),
  tok("لِلضَّرْبِ","darb","noun",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for the beating».", "«dövme için».",
      segments=[seg("لِ","li","part"), seg("الضَّرْبِ","darb","noun")]),
  tok("الشَّدِيدِ","shadid","noun",[T, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«the hard» — a na't.", "«şiddetli» — na't.", punct=".")]})

# ----------- s3 — the tabaʿiyya (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And the tabaʿiyya is that in which it is something else — as the verb, what is derived from it, and the particle." + R_EN,
 "tr": "Tebeiyye, ödünç alınanın ondan başkası olduğu istiâredir — fiil, ondan türeyen ve harf gibi." + R_TR},
 "tokens": [
  tok("وَالتَّبَعِيَّةُ","tabaiyya","noun",[T, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالتَّبَعِيَّةُ مُبْتَدَأٌ.", "«and the tabaʿiyya» — the mubtada.", "«tebeiyye» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("التَّبَعِيَّةُ","tabaiyya","noun")]),
  tok("مَا","ma-mawsula","pron",[T, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«… olan» — haber."),
  tok("كَانَ","kana","verb",[T, "kana-wa-akhawatuha", "ism-mawsul"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى الْمُسْتَعَارِ — صِلَةٌ.", "«is» — kana, its ism hidden: the borrowed word; the sila.", "«olan» — kâne, ismi gizli: ödünç lafız; sıla."),
  tok("غَيْرَهُ","ghayr","noun",[T, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — غَيْرَ اسْمِ الْجِنْسِ.", "«other than it» — the khabar of kana; other than a noun of a kind.", "«ondan başkası» — kânenin haberi; cins isminden başkası.",
      segments=[seg("غَيْرَ","ghayr","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("كَالْفِعْلِ","fil","noun",[T, "huruf-jarr"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ الْفِعْلِ مَجْرُورٌ.", "«as the verb» — the kaf of «for instance», a wall.", "«fiil gibi» — «meselâ» kâfı, duvar.",
      segments=[seg("كَ","ka","part"), seg("الْفِعْلِ","fil","noun")]),
  tok("وَمَا","ma-mawsula","pron",[T, "atf-nasaq", "ism-mawsul"], "مَعْطُوفٌ عَلَى الْفِعْلِ — اسْمٌ مَوْصُولٌ.", "«and what» — joined; the relative.", "«ve … olan» — matuf; mevsûl.",
      segments=[seg("وَ","wa","conj"), seg("مَا","ma-mawsula","pron")]),
  tok("يُشْتَقُّ","ishtaqqa","verb",[T, "naib-al-fail", "doubled-verbs", "form-viii-verbs", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةٌ.", "«is derived» — the passive mudari' of the doubled Form VIII; the sila.", "«türetilir» — muzâaf VIII. bâbın meçhûlü; sıla."),
  tok("مِنْهُ","min","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«from it».", "«ondan».",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("وَالْحَرْفِ","harf","noun",[T, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«and the particle» — joined.", "«ve harf» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("الْحَرْفِ","harf","noun")], punct=".")]})

# ----------- s4 — where the tashbih runs (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "So the likening, in the verb and what is derived from it, is made for the meaning of the MASDAR; and in the particle, for what its meaning HANGS ON." + R_EN,
 "tr": "Fiilde ve ondan türeyende benzetme MASDARIN mânâsı için; harfte ise mânâsının MÜTEALLAKI için yapılır." + R_TR},
 "tokens": [
  tok("فَالتَّشْبِيهُ","tashbih","noun",[T, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالتَّشْبِيهُ مُبْتَدَأٌ.", "«so the likening» — the mubtada.", "«benzetme» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("التَّشْبِيهُ","tashbih","noun")]),
  tok("فِي","fi","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْفِعْلِ","fil","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«the verb».", "«fiil»."),
  tok("وَمَا","ma-mawsula","pron",[T, "atf-nasaq", "ism-mawsul"], "مَعْطُوفٌ — اسْمٌ مَوْصُولٌ.", "«and what» — the relative.", "«ve … olan» — mevsûl.",
      segments=[seg("وَ","wa","conj"), seg("مَا","ma-mawsula","pron")]),
  tok("يُشْتَقُّ","ishtaqqa","verb",[T, "naib-al-fail", "ism-mawsul"], "مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is derived» — the sila.", "«türetilir» — sıla."),
  tok("مِنْهُ","min","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«from it».", "«ondan».",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("لِمَعْنَى","mana","noun",[T, "huruf-jarr", "mubtada-khabar", "ism-maqsur-manqus", "idafa-definiteness"], "الْجَارُّ وَالْمَجْرُورُ خَبَرٌ؛ مَعْنَى مَقْصُورٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«for the meaning of» — the khabar; a maqsur, its kasra assumed; a mudaf.", "«mânâsı için» — haber; maksûr, kesresi takdirî; muzâf.",
      segments=[seg("لِ","li","part"), seg("مَعْنَى","mana","noun")]),
  tok("الْمَصْدَرِ","masdar-noun","noun",[T, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masdar» — mudaf ilayh.", "«masdarın» — muzâfun ileyh.", punct="،"),
  tok("وَفِي","fi","part",[T, "huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in».", "«ve -de».",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","part")]),
  tok("الْحَرْفِ","harf","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«the particle».", "«harf»."),
  tok("لِمُتَعَلَّقِ","mutaallaq","noun",[T, "huruf-jarr", "idafa-definiteness", "ism-maful"], "جَارٌّ وَمَجْرُورٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ (فَالتَّشْبِيهُ)؛ مُضَافٌ.", "«for what hangs on» — the khabar of a dropped «the likening»; a mudaf.", "«müteallakı için» — hazfedilmiş «benzetme»nin haberi; muzâf.",
      segments=[seg("لِ","li","part"), seg("مُتَعَلَّقِ","mutaallaq","noun")]),
  tok("مَعْنَاهُ","mana","noun",[T, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its meaning» — mudaf ilayh; the ه annexed.", "«mânâsının» — muzâfun ileyh; هُ muzâfun ileyh.",
      segments=[seg("مَعْنَا","mana","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s5 — نَطَقَتِ الْحَالُ (RESTORED frame + the stock example)
S.append({"id": "s5", "translation": {
 "en": "As in your saying: «The state SPOKE of such-and-such», and «the state is SPEAKING» — for «it indicated»." + R_EN,
 "tr": "Senin şu sözün gibi: «Hâl şöyle KONUŞTU», «hâl KONUŞUYOR» — «delâlet etti» yerine." + R_TR},
 "majaz": [mj(1, "istiara", "mushabaha", {"en": "spoke", "tr": "konuştu"}, {"en": "indicated — the state made the matter plain as a speaker does", "tr": "delâlet etti — hâl, konuşanın yaptığı gibi işi açık etti"},
              istiara=ist("tabaiyya", seat="fail")),
           mj(5, "istiara", "mushabaha", {"en": "speaking", "tr": "konuşan"}, {"en": "indicating — the derived noun follows its masdar's likening", "tr": "delâlet eden — müştak isim masdarının benzetmesine tâbidir"},
              istiara=ist("tabaiyya", seat="fail"))],
 "tokens": [
  kaq("كَقَوْلِكَ", "pron-2ms"),
  tok("نَطَقَتِ","nataqa","verb",[T, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — اسْتِعَارَةٌ تَبَعِيَّةٌ: النُّطْقُ لِلدَّلَالَةِ، وَالْقَرِينَةُ الْفَاعِلُ (الْحَالُ لَا تَنْطِقُ).",
      "«spoke» — the mazi with the feminine ta, given a kasra before the hamzat al-wasl. A TABAʿIYYA: speaking for indicating; the clue is the FAʿIL — a state does not speak.",
      "«konuştu» — te'nis tâ'lı mâzî; vasl hemzesi önünde kesre almış. TEBEİYYE: konuşmak delâlet yerine; karîne FÂİL — hâl konuşmaz.",
      segments=[seg("نَطَقَ","nataqa","verb"), seg("تِ","ta-tanith","part")]),
  tok("الْحَالُ","hal","noun",[T, "fail"], "فَاعِلٌ مَرْفُوعٌ — قَرِينَةُ الِاسْتِعَارَةِ.", "«the state» — the fa'il; the clue.", "«hâl» — fâil; karîne."),
  tok("بِكَذَا","kadha","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — كِنَايَةٌ عَنِ الْمَذْكُورِ.", "«of such-and-such».", "«şöyle».",
      segments=[seg("بِ","bi","part"), seg("كَذَا","kadha","part")], punct="،"),
  tok("وَالْحَالُ","hal","noun",[T, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْحَالُ مُبْتَدَأٌ.", "«and the state» — the mubtada.", "«ve hâl» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْحَالُ","hal","noun")]),
  tok("نَاطِقَةٌ","natiq","noun",[T, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ؛ اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْمُشْتَقِّ، وَالْقَرِينَةُ الْمُبْتَدَأُ الَّذِي هُوَ فَاعِلُهُ فِي الْمَعْنَى.",
      "«speaking» — the khabar; an ism fa'il. The tabaʿiyya in the DERIVED noun: its clue is the mubtada, which is its doer in meaning.",
      "«konuşan» — haber; ism-i fâil. MÜŞTAKTA tebeiyye: karînesi, mânâca fâili olan mübtedâdır.", punct=".")]})

# ----------- s6 — the aya 28:8 (as printed)
S.append({"id": "s6", "translation": {
 "en": "And as in His saying: «Then the family of Pharaoh picked him up, that he might become for them an enemy and a grief» (28:8).",
 "tr": "Ve kavl-i şerifi gibi: «Firavun ailesi onu, kendilerine düşman ve tasa olsun diye aldı» (28:8)."},
 "majaz": mj(5, "istiara", "mushabaha", {"en": "in order that (the lam of purpose)", "tr": "…için (ta'lil lâmı)"}, {"en": "so that it ended in — the lam of OUTCOME: they did not pick him up to gain an enemy, but that is what followed", "tr": "sonunda … oldu — ÂKIBET lâmı: onu düşman edinmek için almadılar, fakat sonuç bu oldu"},
             istiara=ist("tabaiyya", seat="majrur")),
 "tokens": [
  kawa("وَكَقَوْلِهِ"), TAALA,
  tok("فَالْتَقَطَهُ","iltaqata","verb",[T, "form-viii-verbs", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَالْتَقَطَ فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«then picked him up» — Form VIII; the ه the object.", "«onu aldı» — VIII. bâb; هُ mef'ûl.",
      segments=[seg("فَ","fa","conj"), seg("الْتَقَطَ","iltaqata","verb"), seg("هُ","pron-3ms","pron")]),
  tok("آلُ","al-family","noun",[T, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the family of» — the fa'il, a mudaf.", "«ailesi» — fâil, muzâf."),
  tok("فِرْعَوْنَ","firawn","noun",[T, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.", "«Pharaoh» — mudaf ilayh; jarr by a fatha: a diptote (proper name, foreign).", "«Firavun» — muzâfun ileyh; fetha ile mecrûr: gayr-i munsarif (alem, acem)."),
  tok("لِيَكُونَ","kana","verb",[T, "lam-taleel", "an-masdariyya", "kana-wa-akhawatuha"], "اللَّامُ لِلْعَاقِبَةِ مُسْتَعَارَةٌ مِنْ لَامِ التَّعْلِيلِ، وَيَكُونَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَاسْمُهُ مُسْتَتِرٌ — اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْحَرْفِ.",
      "«that he might be» — the lam of OUTCOME borrowed from the lam of purpose; the verb nasb by a hidden أَنْ; its ism hidden. The tabaʿiyya in the PARTICLE.",
      "«olsun diye» — ta'lil lâmından ödünç alınmış ÂKIBET lâmı; fiil gizli أَنْ ile mansûb; ismi gizli. HARFTE tebeiyye.",
      segments=[seg("لِ","li","part"), seg("يَكُونَ","kana","verb")]),
  tok("لَهُمْ","li","part",[T, "huruf-jarr", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْخَبَرِ.", "«for them».", "«kendilerine».",
      segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("عَدُوًّا","aduww","noun",[T, "kana-wa-akhawatuha"], "خَبَرُ يَكُونَ مَنْصُوبٌ — الْمَجْرُورُ الَّذِي هُوَ قَرِينَةُ اللَّامِ: لَمْ يَلْتَقِطُوهُ لِلْعَدَاوَةِ.", "«an enemy» — the khabar of يَكُونَ; the CLUE of the lam: they did not pick him up in order to gain an enemy.", "«düşman» — يَكُونَ'nin haberi; lâmın KARÎNESİ: onu düşman olsun diye almadılar."),
  tok("وَحَزَنًا","hazan","noun",[T, "atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«and a grief» — joined.", "«ve tasa» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("حَزَنًا","hazan","noun")], punct=".")]})

# ----------- s7 — the lam of outcome (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "So the lam is for the OUTCOME, borrowed from the lam of purpose; and the jamiʿ is the FOLLOWING of one thing upon another." + R_EN,
 "tr": "Lâm ÂKIBET içindir, ta'lil lâmından ödünç alınmıştır; câmi ise bir şeyin diğerini TAKİP ETMESİdir." + R_TR},
 "tokens": [
  tok("فَاللَّامُ","lam-letter","noun",[T, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ مُبْتَدَأٌ.", "«so the lam» — the mubtada.", "«lâm» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("اللَّامُ","lam-letter","noun")]),
  tok("لِلْعَاقِبَةِ","aqiba","noun",[T, "huruf-jarr", "mubtada-khabar"], "الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the outcome» — the khabar.", "«âkıbet için» — haber.",
      segments=[seg("لِ","li","part"), seg("الْعَاقِبَةِ","aqiba","noun")]),
  tok("مُسْتَعَارَةٌ","mustaar","noun",[T, "mubtada-khabar", "ism-maful"], "خَبَرٌ ثَانٍ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«borrowed» — a second khabar; ism maf'ul.", "«ödünç alınmış» — ikinci haber; ism-i mef'ûl."),
  tok("مِنْ","min","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("لَامِ","lam-letter","noun",[T, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the lam of» — a mudaf.", "«lâmından» — muzâf."),
  tok("التَّعْلِيلِ","talil","noun",[T, "idafa-definiteness", "lam-taleel"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«purpose» — mudaf ilayh.", "«ta'lil» — muzâfun ileyh.", punct="،"),
  tok("وَالْجَامِعُ","jami-link","noun",[T, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْجَامِعُ مُبْتَدَأٌ.", "«and the jamiʿ» — the mubtada.", "«câmi» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْجَامِعُ","jami-link","noun")]),
  tok("التَّرَتُّبُ","tarattub","noun",[T, "mubtada-khabar", "form-v-verbs", "masdar"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ تَرَتَّبَ.", "«the following-upon» — the khabar; the masdar of Form V.", "«terettüb» — haber; V. bâbın masdarı.", punct=".")]})

# ----------- s8 — the clue of the tabaʿiyya: the faʿil (RESTORED)
S.append({"id": "s8", "translation": {
 "en": "And the clue of the tabaʿiyya in the verb is either the FAʿIL — as in «the state spoke» —" + R_EN,
 "tr": "Fiildeki tebeiyyenin karînesi ya FÂİLdir — «hâl konuştu»da olduğu gibi —" + R_TR},
 "tokens": [
  tok("وَقَرِينَةُ","qarina","noun",[T, "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَرِينَةُ مُبْتَدَأٌ مُضَافٌ.", "«and the clue of» — the mubtada, a mudaf.", "«karînesi» — mübtedâ, muzâf.",
      segments=[seg("وَ","wa","conj"), seg("قَرِينَةُ","qarina","noun")]),
  tok("التَّبَعِيَّةِ","tabaiyya","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tabaʿiyya» — mudaf ilayh.", "«tebeiyyenin» — muzâfun ileyh."),
  tok("فِي","fi","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْفِعْلِ","fil","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«the verb».", "«fiil»."),
  tok("إِمَّا","imma","part",[T, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either» — the particle of detail.", "«ya» — tafsîl harfi."),
  tok("الْفَاعِلُ","fail-doer","noun",[T, "mubtada-khabar", "fail"], "خَبَرٌ مَرْفُوعٌ.", "«the fa'il» — the khabar.", "«fâil» — haber."),
  tok("كَمَا","ka","part",[T, "huruf-jarr"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ مَا مَصْدَرِيَّةٌ.", "«as» — the kaf of «for instance», a wall; ما masdariyya.", "«olduğu gibi» — «meselâ» kâfı, duvar; ما masdariyye.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("فِي","fi","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("نَطَقَتِ","nataqa","verb",[T, "fail"], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«‹spoke›» — the quoted clause, in the place of jarr.", "«‹konuştu›» — hikâye edilen cümle, cer mahallinde.",
      segments=[seg("نَطَقَ","nataqa","verb"), seg("تِ","ta-tanith","part")]),
  tok("الْحَالُ","hal","noun",[T, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the state» — the fa'il.", "«hâl» — fâil.", punct="،")]})

# ----------- s9 — the mafʿul: قَتَلَ الْبُخْلَ وَأَحْيَا السَّمَاحَا (hemistich as printed)
S.append({"id": "s9", "translation": {
 "en": "— or the MAFʿUL, as in his saying: «He KILLED miserliness and GAVE LIFE to generosity».",
 "tr": "— ya MEF'ÛL, şairin şu sözü gibi: «Cimriliği ÖLDÜRDÜ, cömertliği DİRİLTTİ»."},
 "majaz": [mj(3, "istiara", "mushabaha", {"en": "killed", "tr": "öldürdü"}, {"en": "removed, put an end to — miserliness cannot be killed", "tr": "giderdi, sona erdirdi — cimrilik öldürülmez"},
              istiara=ist("tabaiyya", seat="maful")),
           mj(5, "istiara", "mushabaha", {"en": "gave life to", "tr": "diriltti"}, {"en": "brought forth, made manifest — generosity is not revived", "tr": "ortaya çıkardı, izhar etti — cömertlik diriltilmez"},
              istiara=ist("tabaiyya", seat="maful"))],
 "tokens": [
  tok("وَإِمَّا","imma","part",[T, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«or» — the second «either».", "«ya» — ikinci tafsîl.",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("الْمَفْعُولُ","maful-object","noun",[T, "atf-nasaq", "maful-bihi"], "مَعْطُوفٌ عَلَى الْفَاعِلِ مَرْفُوعٌ.", "«the maf'ul» — joined to «the fa'il».", "«mef'ûl» — fâile matuf.", punct="،"),
  kaq("كَقَوْلِهِ"),
  tok("قَتَلَ","qatala","verb",[T, "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الْقَتْلُ لِلْإِزَالَةِ، وَالْقَرِينَةُ الْمَفْعُولُ.", "«he killed» — a tabaʿiyya: killing for removing; the clue is the OBJECT.", "«öldürdü» — tebeiyye: öldürmek gidermek yerine; karîne MEF'ÛL."),
  tok("الْبُخْلَ","bukhl","noun",[T, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — قَرِينَةٌ: الْبُخْلُ لَا يُقْتَلُ.", "«miserliness» — the object; the clue: it cannot be killed.", "«cimriliği» — mef'ûl; karîne: cimrilik öldürülmez."),
  tok("وَأَحْيَا","ahya","verb",[T, "atf-nasaq", "form-iv-verbs", "naqis-verbs", "maful-bihi"], "مَعْطُوفٌ، فِعْلٌ مَاضٍ نَاقِصٌ مِنَ الرَّابِعِ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الْإِحْيَاءُ لِلْإِظْهَارِ، وَالْقَرِينَةُ الْمَفْعُولُ.", "«and gave life» — Form IV naqis; a tabaʿiyya: reviving for bringing forth; the clue is the object.", "«ve diriltti» — IV. bâb nâkıs; tebeiyye: diriltmek izhar yerine; karîne mef'ûl.",
      segments=[seg("وَ","wa","conj"), seg("أَحْيَا","ahya","verb")]),
  tok("السَّمَاحَا","samah","noun",[T, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْأَلِفُ لِلْإِطْلَاقِ.", "«generosity» — the object; the alif of itlaq for the rhyme.", "«cömertliği» — mef'ûl; kafiye için ıtlak elifi.", punct=".")]})

# ----------- s10 — the second mafʿul: the bayt (as printed)
S.append({"id": "s10", "translation": {
 "en": "— or the SECOND MAFʿUL, as in his saying: «We ENTERTAIN them with sharp spears, with which we cut • whatever every mail-maker had sewn upon them».",
 "tr": "— ya İKİNCİ MEF'ÛL, şairin şu sözü gibi: «Onları keskin mızraklarla AĞIRLARIZ; onlarla keseriz • her zırhçının üzerlerine diktiğini»."},
 "majaz": mj(4, "istiara", "mushabaha", {"en": "we entertain (a guest)", "tr": "(misafiri) ağırlarız"}, {"en": "we stab, we thrust at them — the meal offered is spearheads", "tr": "saplarız, mızraklarız — sunulan ziyafet mızrak uçlarıdır"},
             istiara=ist("tabaiyya", seat="maful2")),
 "tokens": [
  tok("وَإِمَّا","imma","part",[T, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«or».", "«ya».",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("الْمَفْعُولُ","maful-object","noun",[T, "atf-nasaq", "mafulayn"], "مَعْطُوفٌ مَرْفُوعٌ.", "«the maf'ul» — joined.", "«mef'ûl» — matuf."),
  tok("الثَّانِي","thani","noun",[T, "naat-sifa", "ism-maqsur-manqus"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second» — a na't; a manqus, its damma assumed.", "«ikinci» — na't; mankûs, zammesi takdirî.", punct="،"),
  kaq("كَقَوْلِهِ"),
  tok("نَقْرِيهِمْ","qara-host","verb",[T, "mafulayn", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ (نَحْنُ)، وَهُمْ مَفْعُولٌ أَوَّلُ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الْقِرَى لِلطَّعْنِ، وَالْقَرِينَةُ الْمَفْعُولُ الثَّانِي.",
      "«we entertain them» — the mudari' of the naqis قَرَى, its damma assumed on the ya; «them» the first object. A TABAʿIYYA: hosting for stabbing; the clue is the SECOND OBJECT.",
      "«onları ağırlarız» — nâkıs قَرَى'nın muzârii, zammesi yâ üzerinde takdirî; «onları» birinci mef'ûl. TEBEİYYE: ağırlamak saplamak yerine; karîne İKİNCİ MEF'ÛL.",
      segments=[seg("نَقْرِي","qara-host","verb"), seg("هِمْ","pron-3mp","pron")]),
  tok("لَهْذَمِيَّاتٍ","lahdhamiyyat","noun",[T, "mafulayn", "jam-muannath-salim"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ؛ وَهُوَ الْقَرِينَةُ: لَا يُقْرَى الضَّيْفُ بِالرِّمَاحِ.",
      "«sharp spears» — the second object; nasb by a kasra (sound feminine plural). The CLUE: a guest is not fed spears.",
      "«keskin mızraklar» — ikinci mef'ûl; kesre ile mansûb (cem-i müennes sâlim). KARÎNE: misafir mızrakla ağırlanmaz."),
  tok("نَقُدُّ","qadda","verb",[T, "jumla-sifa", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مُضَاعَفٌ، وَالْجُمْلَةُ صِفَةٌ لِلَهْذَمِيَّاتٍ.", "«we cut» — the doubled mudari'; the clause a sifa of the spears.", "«keseriz» — muzâaf muzâri; cümle mızrakların sıfatı."),
  tok("بِهَا","bi","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«with them».", "«onlarla».",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")], punct="•"),
  tok("مَا","ma-mawsula","pron",[T, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولُ نَقُدُّ.", "«whatever» — the relative, the object of «we cut».", "«… -ini» — mevsûl, «keseriz»in mef'ûlü."),
  tok("كَانَ","kana","verb",[T, "kana-wa-akhawatuha", "ism-mawsul"], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةٌ.", "«had» — kana; the sila.", "«idi» — kâne; sıla."),
  tok("خَاطَ","khata-sew","verb",[T, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالْجُمْلَةُ خَبَرُ كَانَ.", "«sewn» — the hollow mazi; the clause is kana's khabar.", "«dikmiş» — ecvef mâzî; cümle kânenin haberi."),
  tok("عَلَيْهِمْ","ala","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«upon them».", "«üzerlerine».",
      segments=[seg("عَلَيْ","ala","part"), seg("هِمْ","pron-3mp","pron")]),
  tok("كُلُّ","kull","noun",[T, "fail", "idafa-definiteness"], "فَاعِلُ خَاطَ مَرْفُوعٌ، مُضَافٌ.", "«every» — the fa'il of «sewn», a mudaf.", "«her» — «dikmiş»in fâili, muzâf."),
  tok("زَرَّادِ","zarrad","noun",[T, "idafa-definiteness", "sighat-mubalagha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَعَّالٌ لِلْمُبَالَغَةِ؛ الْكَسْرَةُ لِلرَّوِيِّ.", "«mail-maker» — mudaf ilayh; the intensive فَعَّال; the kasra of the rhyme.", "«zırhçı» — muzâfun ileyh; mübalağa فَعَّال; revî kesresi.", punct=".")]})

# ----------- s11 — the majrur: 9:34 (as printed)
S.append({"id": "s11", "translation": {
 "en": "— or the MAJRUR, as in His saying: «So give them glad tidings of a painful torment» (9:34).",
 "tr": "— ya MECRÛR, kavl-i şerifi gibi: «Onları elîm bir azapla müjdele» (9:34)."},
 "majaz": mj(4, "istiara", "mushabaha", {"en": "give glad tidings", "tr": "müjdele"}, {"en": "warn — the contrary, used in mockery", "tr": "uyar — alay için zıddı"},
             istiara=ist("tabaiyya", ends="inadiyya", seat="majrur")),
 "tokens": [
  tok("وَإِمَّا","imma","part",[T, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«or».", "«ya».",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("الْمَجْرُورُ","majrur-noun","noun",[T, "atf-nasaq", "huruf-jarr"], "مَعْطُوفٌ مَرْفُوعٌ.", "«the majrur» — joined.", "«mecrûr» — matuf.", punct="،"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("فَبَشِّرْهُمْ","bashshara","verb",[T, "imperative-amr", "form-ii-verbs", "maful-bihi"], "الْفَاءُ لِلْجَزَاءِ، وَبَشِّرْ أَمْرٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَهُمْ مَفْعُولٌ — اسْتِعَارَةٌ تَبَعِيَّةٌ تَهَكُّمِيَّةٌ، وَالْقَرِينَةُ الْمَجْرُورُ.",
      "«so give them glad tidings» — the amr on sukun; «them» the object. A tabaʿiyya by TAHAKKUM; the clue is the MAJRUR.",
      "«onları müjdele» — sükûn üzere emir; «onları» mef'ûl. TEHEKKÜM ile tebeiyye; karîne MECRÛR.",
      segments=[seg("فَ","fa","conj"), seg("بَشِّرْ","bashshara","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("بِعَذَابٍ","adhab","noun",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْقَرِينَةُ: لَا بِشَارَةَ بِالْعَذَابِ.", "«of a torment» — the clue: no glad tiding is a torment.", "«azapla» — karîne: azap müjde olmaz.",
      segments=[seg("بِ","bi","part"), seg("عَذَابٍ","adhab","noun")]),
  tok("أَلِيمٍ","alim-painful","noun",[T, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«painful» — a na't.", "«elîm» — na't.", punct=".")]})

# ----------- s12 — by the mulaʾim: three kinds (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "And regarded by the MENTION OF THE MULAʾIM it is of three kinds: the mutlaqa, the mujarrada and the murashshaha." + R_EN,
 "tr": "MÜLÂİMİN ZİKRİ itibariyle üç kısımdır: mutlaka, mücerrede ve müreşşaha." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[R, "huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، مُضَافٌ.", "«and by the regard of» — the khabar brought forward; a mudaf.", "«ve itibariyle» — öne alınmış haber; muzâf.",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("ذِكْرِ","dhikr","noun",[R, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the mention of» — mudaf ilayh, itself a mudaf.", "«zikri» — muzâfun ileyh, kendisi muzâf."),
  tok("الْمُلَائِمِ","mulaim","noun",[R, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ لَاءَمَ: مَا يُنَاسِبُ أَحَدَ الطَّرَفَيْنِ.", "«the mulaʾim» — mudaf ilayh; the ism fa'il of لَاءَمَ: what suits one of the two ends.", "«mülâim» — muzâfun ileyh; لَاءَمَ'nin ism-i fâili: iki taraftan birine uyan."),
  tok("ثَلَاثَةُ","thalatha","noun",[R, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«three» — the mubtada, held back; a mudaf.", "«üç» — geriye bırakılmış mübtedâ; muzâf."),
  tok("أَقْسَامٍ","aqsam","noun",[R, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«kinds» — mudaf ilayh.", "«kısım» — muzâfun ileyh.", punct=":"),
  tok("مُطْلَقَةٌ","mutlaqa","noun",[R, "badal", "ism-maful"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ.", "«a mutlaqa» — badal of detail.", "«mutlaka» — tafsîl bedeli."),
  tok("وَمُجَرَّدَةٌ","mujarrada","noun",[R, "atf-nasaq", "ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and a mujarrada» — joined.", "«ve mücerrede» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("مُجَرَّدَةٌ","mujarrada","noun")]),
  tok("وَمُرَشَّحَةٌ","murashshaha","noun",[R, "atf-nasaq", "ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and a murashshaha» — joined.", "«ve müreşşaha» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("مُرَشَّحَةٌ","murashshaha","noun")], punct=".")]})

# ----------- s13 — the mutlaqa (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "The mutlaqa is that which is NOT joined to any quality or any branching — as in your saying: «I have a lion»." + R_EN,
 "tr": "Mutlaka, hiçbir vasfa ve tefrîe BAĞLANMAMIŞ olandır — «Yanımda bir arslan var» sözün gibi." + R_TR},
 "majaz": mj(9, "istiara", "mushabaha", {"en": "a lion", "tr": "bir arslan"}, {"en": "a brave man — the clue lies in the situation, not in a word", "tr": "cesur bir adam — karîne sözde değil durumdadır"},
             istiara=ist("asliyya", mulaim="mutlaqa")),
 "tokens": [
  tok("فَالْمُطْلَقَةُ","mutlaqa","noun",[R, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمُطْلَقَةُ مُبْتَدَأٌ.", "«so the mutlaqa» — the mubtada.", "«mutlaka» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْمُطْلَقَةُ","mutlaqa","noun")]),
  tok("مَا","ma-mawsula","pron",[R, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«… olan» — haber."),
  tok("لَمْ","lam-jazima","part",[R, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not» — the jazm particle.", "«-memiş» — cezm harfi."),
  tok("تُقْرَنْ","qarana","verb",[R, "lam-jazim", "naib-al-fail", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ (هِيَ) — صِلَةٌ.", "«is joined» — jazm by لَمْ, passive; the sila.", "«bağlanmış» — لَمْ ile meczûm, meçhûl; sıla."),
  tok("بِصِفَةٍ","sifa","noun",[R, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to a quality».", "«bir vasfa».",
      segments=[seg("بِ","bi","part"), seg("صِفَةٍ","sifa","noun")]),
  tok("وَلَا","la-nafiya","part",[R, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor» — the waw with a reinforcing لَا.", "«ne de» — vâv ile te'kid lâsı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("تَفْرِيعٍ","tafri","noun",[R, "atf-nasaq", "masdar", "form-ii-verbs"], "مَعْطُوفٌ عَلَى صِفَةٍ مَجْرُورٌ — مَصْدَرُ فَرَّعَ: بِنَاءُ كَلَامٍ عَلَيْهَا.", "«branching» — joined to «quality»; the masdar of فَرَّعَ: building speech upon it.", "«tefrî» — «vasıf»a matuf; فَرَّعَ'nin masdarı: üzerine söz kurma.", punct="،"),
  kaq("كَقَوْلِكَ", "pron-2ms", ":", R),
  tok("عِنْدِي","inda","noun",[R, "maful-fih", "mubtada-khabar"], "ظَرْفٌ خَبَرٌ مُقَدَّمٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«with me» — the zarf as khabar, brought forward.", "«yanımda» — öne alınmış haber zarfı.",
      segments=[seg("عِنْدَ","inda","noun"), seg("ي","pron-1s","pron")]),
  tok("أَسَدٌ","asad","noun",[R, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — اسْتِعَارَةٌ أَصْلِيَّةٌ مُطْلَقَةٌ: لَا صِفَةَ وَلَا تَفْرِيعَ مَعَهَا.", "«a lion» — the mubtada, held back. An asliyya, MUTLAQA: nothing joined to it.", "«bir arslan» — geriye bırakılmış mübtedâ. Asliyye, MUTLAKA: yanında hiçbir şey yok.", punct=".")]})

# ----------- s14 — the mujarrada (RESTORED)
S.append({"id": "s14", "translation": {
 "en": "And the mujarrada is that which is joined to what suits the MUSTAʿAR LAHU." + R_EN,
 "tr": "Mücerrede, MÜSTEÂRUN LEHe uyan bir şeye bağlanmış olandır." + R_TR},
 "tokens": [
  tok("وَالْمُجَرَّدَةُ","mujarrada","noun",[R, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْمُجَرَّدَةُ مُبْتَدَأٌ.", "«and the mujarrada» — the mubtada.", "«mücerrede» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُجَرَّدَةُ","mujarrada","noun")]),
  tok("مَا","ma-mawsula","pron",[R, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«… olan» — haber."),
  tok("قُرِنَ","qarana","verb",[R, "naib-al-fail", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةٌ.", "«is joined» — the passive mazi; the sila.", "«bağlanmış» — meçhûl mâzî; sıla."),
  tok("بِمَا","ma-mawsula","pron",[R, "huruf-jarr", "ism-mawsul"], "الْبَاءُ جَارَّةٌ، وَمَا مَوْصُولٌ مَجْرُورٌ.", "«to what» — the relative after the ba.", "«… şeye» — bâ'dan sonra mevsûl.",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُلَائِمُ","laama","verb",[R, "form-iii-verbs", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مِنَ الثَّالِثِ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«suits» — Form III; the sila.", "«uyan» — III. bâb; sıla."),
  tok("الْمُسْتَعَارَ","mustaar","noun",[R, "maful-bihi", "ism-maful"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the borrowed-for» — the object.", "«müsteâr» — mef'ûl."),
  tok("لَهُ","li","part",[R, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُسْتَعَارُ لَهُ: الْمُشَبَّهُ.", "«-to» — the mustaʿar LAHU: the mushabbah.", "«leh» — müsteârun LEH: müşebbeh.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s15 — the bayt غَمْرُ الرِّدَاءِ (as printed)
S.append({"id": "s15", "translation": {
 "en": "As in his saying: «Abundant of CLOAK — when he smiles, laughing, • the necks of wealth fall forfeit to his laugh».",
 "tr": "Şairin şu sözü gibi: «RİDÂSI bol — gülerek tebessüm ettiğinde, • malın boyunları gülüşüne rehin düşer»."},
 "majaz": mj(2, "istiara", "mushabaha", {"en": "the cloak", "tr": "ridâ, örtü"}, {"en": "his giving — the bounty that covers people as a cloak covers", "tr": "ihsanı — ridânın örttüğü gibi insanları saran cömertlik"},
             istiara=ist("asliyya", mulaim="mujarrada", lahu=[1])),
 "tokens": [
  kaq("كَقَوْلِهِ", "pron-3ms", ":", R),
  tok("غَمْرُ","ghamr","noun",[R, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ (هُوَ) مَرْفُوعٌ، مُضَافٌ — مُلَائِمٌ لِلْمُسْتَعَارِ لَهُ: الْغَمْرُ يُوصَفُ بِهِ الْعَطَاءُ لَا الثَّوْبُ.",
      "«abundant of» — the khabar of a dropped «he», a mudaf. The MULAʾIM of the mustaʿar lahu: «abundant» describes giving, not a garment — that is what makes the istiʿara MUJARRADA.",
      "«bol» — hazfedilmiş «o»nun haberi, muzâf. Müsteârun lehin MÜLÂİMİ: «bol» elbiseyi değil ihsanı vasfeder — istiâreyi MÜCERREDE kılan budur."),
  tok("الرِّدَاءِ","rida","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْتِعَارَةٌ أَصْلِيَّةٌ: الرِّدَاءُ لِلْعَطَاءِ، لِأَنَّهُ يَصُونُ كَمَا يَصُونُ الثَّوْبُ.", "«cloak» — mudaf ilayh. An ASLIYYA: the cloak for giving, since it shelters as a garment does.", "«ridâ» — muzâfun ileyh. ASLİYYE: ridâ ihsan yerine; elbise gibi korur."),
  tok("إِذَا","idha","part",[R, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the zarf of the future with a shart's sense.", "«-diğinde» — şart mânâlı istikbal zarfı."),
  tok("تَبَسَّمَ","tabassama","verb",[R, "idha-shartiyya", "form-v-verbs"], "فِعْلٌ مَاضٍ مِنَ الْخَامِسِ — فِعْلُ الشَّرْطِ.", "«he smiles» — Form V; the verb of the shart.", "«tebessüm etti» — V. bâb; şart fiili."),
  tok("ضَاحِكًا","dahik","noun",[R, "hal", "ism-fail"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ.", "«laughing» — a hal.", "«gülerek» — hâl.", punct="•"),
  tok("غَلِقَتْ","ghaliqa","verb",[R, "idha-shartiyya"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — جَوَابُ إِذَا: صَارَتْ رَهْنًا لَا يُفَكُّ.", "«fall forfeit» — the jawab of إِذَا: become a pledge past redeeming.", "«rehin düşer» — إِذَا'nın cevabı: kurtarılmaz rehin olur.",
      segments=[seg("غَلِقَ","ghaliqa","verb"), seg("تْ","ta-tanith","part")]),
  tok("لِضَحْكَتِهِ","dahka","noun",[R, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his laugh».", "«gülüşüne».",
      segments=[seg("لِ","li","part"), seg("ضَحْكَةِ","dahka","noun"), seg("هِ","pron-3ms","pron")]),
  tok("رِقَابُ","raqaba","noun",[R, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ رَقَبَةٍ.", "«the necks of» — the fa'il, a mudaf; plural of رَقَبَة.", "«boyunları» — fâil, muzâf; رَقَبَة'nin çoğulu."),
  tok("الْمَالِ","mal","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wealth» — mudaf ilayh.", "«malın» — muzâfun ileyh.", punct=".")]})

# ----------- s16 — the murashshaha (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "And the murashshaha is that which is joined to what suits the MUSTAʿAR MINHU." + R_EN,
 "tr": "Müreşşaha, MÜSTEÂRUN MİNHe uyan bir şeye bağlanmış olandır." + R_TR},
 "tokens": [
  tok("وَالْمُرَشَّحَةُ","murashshaha","noun",[R, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْمُرَشَّحَةُ مُبْتَدَأٌ.", "«and the murashshaha» — the mubtada.", "«müreşşaha» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُرَشَّحَةُ","murashshaha","noun")]),
  tok("مَا","ma-mawsula","pron",[R, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«… olan» — haber."),
  tok("قُرِنَ","qarana","verb",[R, "naib-al-fail", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is joined» — passive; the sila.", "«bağlanmış» — meçhûl; sıla."),
  tok("بِمَا","ma-mawsula","pron",[R, "huruf-jarr", "ism-mawsul"], "الْبَاءُ جَارَّةٌ، وَمَا مَوْصُولٌ.", "«to what».", "«… şeye».",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُلَائِمُ","laama","verb",[R, "form-iii-verbs", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ — صِلَةٌ.", "«suits» — the sila.", "«uyan» — sıla."),
  tok("الْمُسْتَعَارَ","mustaar","noun",[R, "maful-bihi", "ism-maful"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the borrowed-from» — the object.", "«müsteâr» — mef'ûl."),
  tok("مِنْهُ","min","part",[R, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُسْتَعَارُ مِنْهُ: الْمُشَبَّهُ بِهِ.", "«-from» — the mustaʿar MINHU: the bihi.", "«minh» — müsteârun MİNH: müşebbehün bih.",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s17 — the aya 2:16 (as printed)
S.append({"id": "s17", "translation": {
 "en": "As in His saying: «Those are they who BOUGHT error with guidance, so their TRADE did not PROFIT» (2:16).",
 "tr": "Kavl-i şerifi gibi: «Onlar hidayete karşılık dalâleti SATIN ALANLARDIR; TİCARETLERİ KÂR ETMEDİ» (2:16)."},
 "majaz": mj(4, "istiara", "mushabaha", {"en": "they bought", "tr": "satın aldılar"}, {"en": "they exchanged, took error in place of guidance", "tr": "değiştiler, hidayet yerine dalâleti aldılar"},
             istiara=ist("tabaiyya", seat="maful", mulaim="murashshaha", minhu=[8, 9])),
 "tokens": [
  kaq("كَقَوْلِهِ", "pron-3ms", ":", R), TAALA,
  tok("أُولَئِكَ","ulaika","pron",[R, "asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ.", "«those» — the demonstrative, the mubtada.", "«onlar» — işaret ismi, mübtedâ."),
  tok("الَّذِينَ","alladhina","pron",[R, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«they who» — the relative, the khabar.", "«… olanlar» — mevsûl, haber."),
  tok("اشْتَرَوُا","ishtara","verb",[R, "form-viii-verbs", "naqis-verbs", "ism-mawsul", "maful-bihi"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنَ الثَّامِنِ، حُذِفَتْ لَامُهُ لِوَاوِ الْجَمَاعَةِ، وَضُمَّتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الشِّرَاءُ لِلِاسْتِبْدَالِ، وَالْقَرِينَةُ الْمَفْعُولُ.",
      "«they bought» — Form VIII naqis; its last radical dropped before the plural waw, and the waw given a damma before the hamzat al-wasl. A TABAʿIYYA: buying for exchanging; the clue is the OBJECT.",
      "«satın aldılar» — VIII. bâb nâkıs; cemaat vâvı önünde lâmı düşmüş, vasl hemzesi önünde vâv zamme almış. TEBEİYYE: satın almak değişmek yerine; karîne MEF'ÛL."),
  tok("الضَّلَالَةَ","dalalah-error","noun",[R, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْقَرِينَةُ: الضَّلَالَةُ لَا تُشْتَرَى.", "«error» — the object; the clue: error is not bought.", "«dalâleti» — mef'ûl; karîne: dalâlet satın alınmaz."),
  tok("بِالْهُدَى","huda","noun",[R, "huruf-jarr", "ism-maqsur-manqus"], "الْبَاءُ لِلْمُقَابَلَةِ، وَالْهُدَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«with guidance» — the ba of exchange; a maqsur.", "«hidayete karşılık» — mukabele bâsı; maksûr.",
      segments=[seg("بِ","bi","part"), seg("الْهُدَى","huda","noun")]),
  tok("فَمَا","ma-nafiya","part",[R, "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«so … not».", "«… -medi».",
      segments=[seg("فَ","fa","conj"), seg("مَا","ma-nafiya","part")]),
  tok("رَبِحَتْ","rabiha","verb",[R, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — مُلَائِمٌ لِلْمُسْتَعَارِ مِنْهُ: الرِّبْحُ مِنْ لَوَازِمِ الشِّرَاءِ؛ بِهِ تَصِيرُ الِاسْتِعَارَةُ مُرَشَّحَةً.",
      "«profited» — the MULAʾIM of the mustaʿar minhu: profit belongs to buying; it makes the istiʿara MURASHSHAHA.",
      "«kâr etti» — müsteârun minhin MÜLÂİMİ: kâr satın almanın levâzımındandır; istiâreyi MÜREŞŞAHA kılar.",
      segments=[seg("رَبِحَ","rabiha","verb"), seg("تْ","ta-tanith","part")]),
  tok("تِجَارَتُهُمْ","tijara","noun",[R, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُمْ مُضَافٌ إِلَيْهِ — مُلَائِمٌ ثَانٍ لِلْمُسْتَعَارِ مِنْهُ.", "«their trade» — the fa'il; a second mulaʾim of the minhu.", "«ticaretleri» — fâil; minhin ikinci mülâimi.",
      segments=[seg("تِجَارَةُ","tijara","noun"), seg("هُمْ","pron-3mp","pron")], punct=".")]})

# ----------- s18 — both together: Zuhayr's bayt (RESTORED frame + the bayt as printed)
S.append({"id": "s18", "translation": {
 "en": "And the two may come together, as in Zuhayr's saying: «With a lion, bristling with arms, hurled into battle, • who has a mane, whose claws are never clipped»." + R_EN,
 "tr": "İkisi bir arada da bulunabilir; Züheyr'in şu sözü gibi: «Silâhı çok, savaşa atılmış bir arslanın yanında, • yelesi var, pençeleri hiç kesilmemiş»." + R_TR},
 "majaz": mj(5, "istiara", "mushabaha", {"en": "a lion", "tr": "arslan"}, {"en": "a brave warrior", "tr": "cesur bir savaşçı"},
             istiara=ist("asliyya", mulaim="both", lahu=[6, 7, 8], minhu=[10, 11, 12, 13])),
 "tokens": [
  tok("وَقَدْ","qad","part",[R, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and sometimes» — qad with a mudari'.", "«bazen» — muzâri ile kad.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يَجْتَمِعَانِ","ijtamaa","verb",[R, "form-viii-verbs", "afal-khamsa", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — التَّجْرِيدُ وَالتَّرْشِيحُ.", "«the two come together» — raf' by the kept nun; the dual alif the doer: tajrid and tarshih.", "«ikisi bir araya gelir» — nûnun sübutuyla merfû; tesniye elifi fâil: tecrîd ve terşîh.",
      segments=[seg("يَجْتَمِعَ","ijtamaa","verb"), seg("انِ","pron-3md","pron")], punct="،"),
  tok("كَقَوْلِ","qawl","noun",[R, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance», a wall.", "«sözü gibi» — «meselâ» kâfı, duvar.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")]),
  tok("زُهَيْرٍ","zuhayr","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ مُنْصَرِفٌ.", "«Zuhayr» — mudaf ilayh; a declinable proper name.", "«Züheyr» — muzâfun ileyh; munsarif alem.", punct=":"),
  tok("لَدَى","lada","noun",[R, "maful-fih", "mubtada-khabar"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ، مُضَافٌ — خَبَرٌ مُقَدَّمٌ لِمُبْتَدَإٍ مُتَقَدِّمٍ فِي الْبَيْتِ.", "«with» — the zarf of place, a mudaf; the khabar of a mubtada earlier in the poem.", "«yanında» — mekân zarfı, muzâf; şiirde daha önce geçen mübtedânın haberi."),
  tok("أَسَدٍ","asad","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْتِعَارَةٌ أَصْلِيَّةٌ لِلشُّجَاعِ، قُرِنَتْ بِمَا يُلَائِمُ الطَّرَفَيْنِ مَعًا.", "«a lion» — mudaf ilayh. An ASLIYYA for the brave man, joined to what suits BOTH ends.", "«arslan» — muzâfun ileyh. Cesur adam için ASLİYYE; HER İKİ tarafa uyanla bir arada."),
  tok("شَاكِي","shaki","noun",[R, "naat-sifa", "ism-fail", "idafa-lafziyya", "ism-maqsur-manqus"], "نَعْتٌ لِأَسَدٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ، مُضَافٌ إِضَافَةً لَفْظِيَّةً؛ مُلَائِمٌ لِلْمُسْتَعَارِ لَهُ: السِّلَاحُ لِلرَّجُلِ لَا لِلْأَسَدِ.",
      "«bristling with» — a na't of «lion»; a manqus in a lafzi idafa. A MULAʾIM OF THE LAHU: arms belong to the man, not the beast — the TAJRID.",
      "«… ile dolu» — «arslan»ın na'ti; lafzî izâfette mankûs. LEHİN MÜLÂİMİ: silâh arslanın değil adamındır — TECRÎD."),
  tok("السِّلَاحِ","silah","noun",[R, "idafa-lafziyya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«arms» — mudaf ilayh.", "«silâh» — muzâfun ileyh."),
  tok("مُقَذَّفٍ","muqadhdhaf","noun",[R, "naat-sifa", "ism-maful"], "نَعْتٌ ثَانٍ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنَ الثَّانِي: مَرْمِيٌّ بِهِ فِي الْحُرُوبِ؛ مُلَائِمٌ لِلْمُسْتَعَارِ لَهُ.", "«hurled (into battle)» — a second na't; ism maf'ul of Form II. A mulaʾim of the lahu.", "«savaşa atılmış» — ikinci na't; II. bâbın ism-i mef'ûlü. Lehin mülâimi.", punct="•"),
  tok("لَهُ","li","part",[R, "huruf-jarr", "mubtada-khabar", "jumla-sifa"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — الْجُمْلَةُ نَعْتٌ ثَالِثٌ.", "«who has» — the khabar brought forward; the clause a third na't.", "«… var» — öne alınmış haber; cümle üçüncü na't.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("لِبَدٌ","libad","noun",[R, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مُلَائِمٌ لِلْمُسْتَعَارِ مِنْهُ: اللِّبَدُ لِلْأَسَدِ؛ بِهِ التَّرْشِيحُ.", "«a mane» — the mubtada, held back. A MULAʾIM OF THE MINHU: the mane is the lion's — the TARSHIH.", "«yele» — geriye bırakılmış mübtedâ. MİNHİN MÜLÂİMİ: yele arslanındır — TERŞÎH."),
  tok("أَظْفَارُهُ","zufr","noun",[R, "mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ ظُفْرٍ؛ مُلَائِمٌ لِلْمُسْتَعَارِ مِنْهُ.", "«his claws» — a mubtada; plural of ظُفْر. A mulaʾim of the minhu.", "«pençeleri» — mübtedâ; ظُفْر'ün çoğulu. Minhin mülâimi.",
      segments=[seg("أَظْفَارُ","zufr","noun"), seg("هُ","pron-3ms","pron")]),
  tok("لَمْ","lam-jazima","part",[R, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«never» — the jazm particle.", "«-memiş» — cezm harfi."),
  tok("تُقَلَّمِ","qallama","verb",[R, "lam-jazim", "naib-al-fail", "form-ii-verbs", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، مَبْنِيٌّ لِلْمَجْهُولِ، حُرِّكَ بِالْكَسْرِ لِلرَّوِيِّ — الْجُمْلَةُ خَبَرُ أَظْفَارُهُ.", "«are clipped» — jazm by لَمْ, passive; the kasra for the rhyme; the clause the khabar of «his claws».", "«kesilmiş» — لَمْ ile meczûm, meçhûl; revî için kesre; cümle «pençeleri»nin haberi.", punct=".")]})

# ----------- s19 — the tarshih is more eloquent (RESTORED)
S.append({"id": "s19", "translation": {
 "en": "And the tarshih is MORE ELOQUENT, because it contains the realising of the exaggeration." + R_EN,
 "tr": "Terşîh DAHA BELİĞdir; çünkü mübalağanın tahkikini içerir." + R_TR},
 "tokens": [
  tok("وَالتَّرْشِيحُ","tarshih","noun",[R, "mubtada-khabar", "masdar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالتَّرْشِيحُ مُبْتَدَأٌ — مَصْدَرُ رَشَّحَ.", "«and the tarshih» — the mubtada; the masdar of Form II.", "«terşîh» — mübtedâ; II. bâbın masdarı.",
      segments=[seg("وَ","wa","conj"), seg("التَّرْشِيحُ","tarshih","noun")]),
  tok("أَبْلَغُ","ablagh","noun",[R, "mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more eloquent» — the khabar; an ism tafdil, a diptote.", "«daha beliğ» — haber; ism-i tafdîl, gayr-i munsarif."),
  tok("لِاشْتِمَالِهِ","ishtimal","noun",[R, "huruf-jarr", "lam-taleel", "masdar", "form-viii-verbs", "idafa-definiteness"], "اللَّامُ لِلتَّعْلِيلِ، وَاشْتِمَالِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ اشْتَمَلَ.", "«because it contains» — the lam of cause; the masdar of Form VIII with its pronoun.", "«içermesi sebebiyle» — ta'lil lâmı; VIII. bâbın masdarı ve zamiri.",
      segments=[seg("لِ","li","part"), seg("اشْتِمَالِ","ishtimal","noun"), seg("هِ","pron-3ms","pron")]),
  tok("عَلَى","ala","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«(contains) … on».", "«-i»."),
  tok("تَحْقِيقِ","tahqiq","noun",[R, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، مُضَافٌ.", "«the realising of» — a mudaf.", "«tahkikini» — muzâf."),
  tok("الْمُبَالَغَةِ","mubalagha","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the exaggeration» — mudaf ilayh.", "«mübalağanın» — muzâfun ileyh.", punct=".")]})

# ----------- s20 — built on forgetting the tashbih (RESTORED)
S.append({"id": "s20", "translation": {
 "en": "And its foundation is the FORGETTING of the likening — so that upon highness of rank is built what is built upon highness of place." + R_EN,
 "tr": "Onun binası benzetmenin UNUTULMASI üzerinedir — öyle ki mekân yüksekliği üzerine kurulan, kadir yüksekliği üzerine kurulur." + R_TR},
 "tokens": [
  tok("وَمَبْنَاهُ","mabna","noun",[R, "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَمَبْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its foundation» — the mubtada; a maqsur.", "«ve binası» — mübtedâ; maksûr.",
      segments=[seg("وَ","wa","conj"), seg("مَبْنَا","mabna","noun"), seg("هُ","pron-3ms","pron")]),
  tok("عَلَى","ala","part",[R, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«on» — the khabar.", "«üzerine» — haber."),
  tok("تَنَاسِي","tanasi","noun",[R, "huruf-jarr", "idafa-definiteness", "form-vi-verbs", "masdar", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مَصْدَرُ تَنَاسَى: إِظْهَارُ النِّسْيَانِ.", "«the forgetting of» — the masdar of Form VI: feigned forgetting; a mudaf.", "«unutulması» — VI. bâbın masdarı: unutmuş görünme; muzâf."),
  tok("التَّشْبِيهِ","tashbih","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likening» — mudaf ilayh.", "«benzetmenin» — muzâfun ileyh.", punct="،"),
  tok("حَتَّى","hatta","part",[R, "an-masdariyya"], "حَرْفُ غَايَةٍ وَنَصْبٍ بِأَنْ مُضْمَرَةٍ.", "«so that» — hatta with a hidden أَنْ.", "«öyle ki» — gizli أَنْ ile hattâ."),
  tok("يُبْنَى","bana","verb",[R, "an-masdariyya", "naib-al-fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مَبْنِيٌّ لِلْمَجْهُولِ.", "«is built» — nasb assumed on the alif; passive.", "«kurulur» — elif üzerinde takdirî nasb; meçhûl."),
  tok("عَلَى","ala","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  tok("عُلُوِّ","uluww","noun",[R, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، مُضَافٌ.", "«highness of» — a mudaf.", "«yüksekliği» — muzâf."),
  tok("الْقَدْرِ","qadr","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rank» — mudaf ilayh.", "«kadir» — muzâfun ileyh."),
  tok("مَا","ma-mawsula","pron",[R, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلِ يُبْنَى.", "«what» — the relative, the deputy doer of «is built».", "«… şey» — mevsûl, «kurulur»un nâib-i fâili."),
  tok("يُبْنَى","bana","verb",[R, "ism-mawsul", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is built» — the sila.", "«kurulan» — sıla."),
  tok("عَلَى","ala","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  tok("عُلُوِّ","uluww","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«highness of» — a mudaf.", "«yüksekliği» — muzâf."),
  tok("الْمَكَانِ","makan","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«place» — mudaf ilayh.", "«mekân» — muzâfun ileyh.", punct=".")]})

# ----------- s21 — the bayt وَيَصْعَدُ (as printed)
S.append({"id": "s21", "translation": {
 "en": "As in his saying: «And he CLIMBS, until the ignorant one thinks • that he has some business in the sky».",
 "tr": "Şairin şu sözü gibi: «Ve ÇIKAR, öyle ki cahil sanır • onun gökte bir işi var»."},
 "majaz": mj(1, "istiara", "mushabaha", {"en": "he climbs", "tr": "yukarı çıkar"}, {"en": "he rises in rank — highness of place for highness of worth; the whole second half is built on the climbing", "tr": "kadri yükselir — mekân yüksekliği kadir yüksekliği yerine; ikinci yarı tırmanma üzerine kurulur"},
             istiara=ist("tabaiyya", mulaim="murashshaha", minhu=[2, 3, 4, 5, 6, 7, 8, 9])),
 "tokens": [
  kaq("كَقَوْلِهِ", "pron-3ms", ":", R),
  tok("وَيَصْعَدُ","saada-climb","verb",[R, "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَصْعَدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — اسْتِعَارَةٌ تَبَعِيَّةٌ مُرَشَّحَةٌ: الصُّعُودُ لِعُلُوِّ الْقَدْرِ، وَبُنِيَ عَلَيْهِ مَا بَعْدَهُ.",
      "«and he climbs» — the mudari', its doer hidden. A TABAʿIYYA, MURASHSHAHA: climbing for rising in worth, and what follows is built on the climbing.",
      "«ve çıkar» — muzâri, fâili gizli. TEBEİYYE, MÜREŞŞAHA: çıkmak kadir yüksekliği yerine; devamı tırmanma üzerine kurulmuş.",
      segments=[seg("وَ","wa","conj"), seg("يَصْعَدُ","saada-climb","verb")]),
  tok("حَتَّى","hatta","part",[R, "an-masdariyya"], "حَرْفُ غَايَةٍ وَنَصْبٍ بِأَنْ مُضْمَرَةٍ — بِهِ يَبْدَأُ التَّرْشِيحُ.", "«until» — hatta with a hidden أَنْ; the tarshih begins here.", "«öyle ki» — gizli أَنْ ile hattâ; terşîh burada başlar."),
  tok("يَظُنَّ","zanna","verb",[R, "an-masdariyya", "zanna-wa-akhawatuha", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ — مِنْ أَفْعَالِ الْقُلُوبِ، وَمَفْعُولَاهُ فِي جُمْلَةِ أَنَّ.", "«thinks» — nasb; a heart-verb whose two objects are the أَنَّ clause.", "«sanır» — mansûb; iki mef'ûlü أَنَّ cümlesi olan kalp fiili."),
  tok("الْجَهُولُ","jahul","noun",[R, "fail", "sighat-mubalagha"], "فَاعِلٌ مَرْفُوعٌ — فَعُولٌ لِلْمُبَالَغَةِ.", "«the ignorant one» — the fa'il; the intensive فَعُول.", "«cahil» — fâil; mübalağa فَعُول.", punct="•"),
  tok("بِأَنَّ","anna","part",[R, "inna-wa-akhawatuha", "huruf-jarr"], "الْبَاءُ زَائِدَةٌ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَادٌّ مَسَدَّ مَفْعُولَيْ يَظُنَّ.", "«that» — a redundant ba over أَنَّ; the clause fills both objects of «thinks».", "«… olduğunu» — zâid bâ ve أَنَّ; cümle «sanır»ın iki mef'ûlü yerinde.",
      segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part")]),
  tok("لَهُ","li","part",[R, "huruf-jarr", "inna-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ خَبَرُ أَنَّ مُقَدَّمٌ.", "«he has» — the khabar of أَنَّ, brought forward.", "«onun … var» — أَنَّ'nin öne alınmış haberi.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("حَاجَةً","haja","noun",[R, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ.", "«some business» — the ism of أَنَّ, held back.", "«bir iş» — أَنَّ'nin geriye bırakılmış ismi."),
  tok("فِي","fi","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("السَّمَاءِ","sama","noun",[R, "huruf-jarr"], "مَجْرُورٌ — مُلَائِمٌ لِلْمُسْتَعَارِ مِنْهُ: السَّمَاءُ غَايَةُ الصُّعُودِ الْحِسِّيِّ.", "«the sky» — majrur; a mulaʾim of the minhu: the sky is where bodily climbing ends.", "«gökte» — mecrûr; minhin mülâimi: gök, cismânî çıkışın son durağı.", punct=".")]})

# ----------- s22 — built on the branch with the root acknowledged (RESTORED + bayt)
S.append({"id": "s22", "translation": {
 "en": "And speech may be built on the BRANCH while the ROOT is acknowledged, as in his saying: «She is the SUN — her dwelling is in the sky; • so console the heart with a fair consolation»." + R_EN,
 "tr": "Söz, ASIL itiraf edilmekle birlikte FER' üzerine de kurulabilir; şairin şu sözü gibi: «O GÜNEŞtir — konağı göktedir; • gönlü güzel bir tesellîyle teselli et»." + R_TR},
 "tashbih": {"kind": "baligh", "mushabbah": [9], "bihi": [10], "adat": None, "wajh": []},
 "tokens": [
  tok("وَقَدْ","qad","part",[R, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يُبْنَى","bana","verb",[R, "naib-al-fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is built» — passive.", "«kurulur» — meçhûl."),
  tok("الْكَلَامُ","kalam","noun",[R, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the speech» — the deputy doer.", "«söz» — nâib-i fâil."),
  tok("عَلَى","ala","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  tok("الْفَرْعِ","far-branch","noun",[R, "huruf-jarr"], "مَجْرُورٌ — الْفَرْعُ: مَا بُنِيَ عَلَى الْمُشَبَّهِ بِهِ.", "«the branch» — what is built on the bihi.", "«fer'» — bih üzerine kurulan."),
  tok("مَعَ","maa","noun",[R, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«together with» — a zarf, a mudaf.", "«ile birlikte» — zarf, muzâf."),
  tok("الِاعْتِرَافِ","itiraf","noun",[R, "idafa-definiteness", "form-viii-verbs", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اعْتَرَفَ.", "«the acknowledging» — mudaf ilayh; the masdar of Form VIII.", "«itiraf» — muzâfun ileyh; VIII. bâbın masdarı."),
  tok("بِالْأَصْلِ","asl","noun",[R, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْأَصْلُ: التَّشْبِيهُ.", "«of the root» — the root: the likening itself.", "«aslı» — asıl: benzetmenin kendisi.",
      segments=[seg("بِ","bi","part"), seg("الْأَصْلِ","asl","noun")], punct="،"),
  kaq("كَقَوْلِهِ", "pron-3ms", ":", R),
  tok("هِيَ","hiya","pron",[R, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — الْمُشَبَّهُ.", "«she» — the mubtada; the mushabbah.", "«o» — mübtedâ; müşebbeh."),
  tok("الشَّمْسُ","shams","noun",[R, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ: تَشْبِيهٌ بَلِيغٌ، هُوَ الْأَصْلُ الْمُعْتَرَفُ بِهِ.", "«the sun» — the khabar; the bihi. A TASHBIH BALIGH: the root, acknowledged.", "«güneş» — haber; bih. TEŞBÎH-İ BELÎĞ: itiraf edilen asıl."),
  tok("مَسْكَنُهَا","maskan","noun",[R, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — الْفَرْعُ: بُنِيَ عَلَى كَوْنِهَا شَمْسًا.", "«her dwelling» — a mubtada; the BRANCH: built on her being a sun.", "«konağı» — mübtedâ; FER': güneş oluşu üzerine kurulmuş.",
      segments=[seg("مَسْكَنُ","maskan","noun"), seg("هَا","pron-3fs","pron")]),
  tok("فِي","fi","part",[R, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the khabar.", "«-de» — haber."),
  tok("السَّمَاءِ","sama","noun",[R, "huruf-jarr"], "مَجْرُورٌ.", "«the sky».", "«gök».", punct="•"),
  tok("فَعَزِّ","azza","verb",[R, "imperative-amr", "form-ii-verbs", "naqis-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَعَزِّ أَمْرٌ مِنَ النَّاقِصِ عَزَّى مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ.", "«so console» — the amr of the naqis Form II, built on the dropped weak letter.", "«teselli et» — nâkıs II. bâbın emri, illet harfi düşmüş.",
      segments=[seg("فَ","fa","conj"), seg("عَزِّ","azza","verb")]),
  tok("الْفُؤَادَ","fuad","noun",[R, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the heart» — the object.", "«gönlü» — mef'ûl."),
  tok("عَزَاءً","aza","noun",[R, "maful-mutlaq", "ism-mamdud"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَمْدُودٌ.", "«with a consolation» — the maf'ul mutlaq; a mamdud.", "«bir tesellîyle» — mef'ûl-i mutlak; memdûd."),
  tok("جَمِيلًا","jamil","noun",[R, "naat-sifa"], "نَعْتٌ مَنْصُوبٌ.", "«fair» — a na't.", "«güzel» — na't.", punct=".")]})

# ----------- s23 — the majaz murakkab (RESTORED)
S.append({"id": "s23", "translation": {
 "en": "And the COMPOUND majaz is the expression used for what has been likened to its original meaning by a likening of TAMTHIL, for exaggeration." + R_EN,
 "tr": "MÜREKKEB mecaz, mübalağa için, aslî mânâsına TEMSİL benzetmesiyle benzetilmiş olan şeyde kullanılan lafızdır." + R_TR},
 "tokens": [
  tok("وَالْمَجَازُ","majaz","noun",[K, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْمَجَازُ مُبْتَدَأٌ.", "«and the majaz» — the mubtada.", "«mecaz» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمَجَازُ","majaz","noun")]),
  tok("الْمُرَكَّبُ","murakkab","noun",[K, "naat-sifa", "ism-maful"], "نَعْتٌ مَرْفُوعٌ.", "«the compound» — a na't.", "«mürekkeb» — na't."),
  tok("هُوَ","huwa","pron",[K, "damir-fasl", "mubtada-khabar"], "ضَمِيرُ فَصْلٍ.", "«is» — the pronoun of separation.", "«-dir» — fasıl zamiri."),
  tok("اللَّفْظُ","lafz","noun",[K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«the expression» — the khabar.", "«lafız» — haber."),
  tok("الْمُسْتَعْمَلُ","mustamal","noun",[K, "naat-sifa", "ism-maful", "form-x-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنَ الْعَاشِرِ.", "«used» — a na't; ism maf'ul of Form X.", "«kullanılan» — na't; X. bâbın ism-i mef'ûlü."),
  tok("فِيمَا","ma-mawsula","pron",[K, "huruf-jarr", "ism-mawsul"], "فِي جَارَّةٌ، وَمَا مَوْصُولٌ مَجْرُورٌ.", "«for what» — the relative after فِي.", "«… şeyde» — فِي'den sonra mevsûl.",
      segments=[seg("فِي","fi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("شُبِّهَ","shabbaha","verb",[K, "naib-al-fail", "form-ii-verbs", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةٌ.", "«has been likened» — the passive; the sila.", "«benzetilmiş» — meçhûl; sıla."),
  tok("بِمَعْنَاهُ","mana","noun",[K, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its meaning» — a maqsur with its pronoun.", "«mânâsına» — maksûr ve zamiri.",
      segments=[seg("بِ","bi","part"), seg("مَعْنَا","mana","noun"), seg("هُ","pron-3ms","pron")]),
  tok("الْأَصْلِيِّ","asli","noun",[K, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — مَنْسُوبٌ.", "«original» — a na't; a nisba.", "«aslî» — na't; nisbet."),
  tok("تَشْبِيهَ","tashbih","noun",[K, "maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ مَنْصُوبٌ، مُضَافٌ.", "«by a likening of» — the maf'ul mutlaq naming the kind; a mudaf.", "«… benzetmesiyle» — nev'i bildiren mef'ûl-i mutlak; muzâf."),
  tok("التَّمْثِيلِ","tamthil","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَشْبِيهُ التَّمْثِيلِ: وَجْهُهُ مُنْتَزَعٌ مِنْ مُتَعَدِّدٍ.", "«tamthil» — mudaf ilayh: the likening whose wajh is drawn from several things.", "«temsil» — muzâfun ileyh: vechi birçok şeyden çıkarılan benzetme."),
  tok("لِلْمُبَالَغَةِ","mubalagha","noun",[K, "huruf-jarr", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَالْمُبَالَغَةِ مَجْرُورٌ.", "«for exaggeration» — the lam of cause.", "«mübalağa için» — ta'lil lâmı.",
      segments=[seg("لِ","li","part"), seg("الْمُبَالَغَةِ","mubalagha","noun")], punct=".")]})

# ----------- s24 — the stock example (RESTORED frame + the received saying)
S.append({"id": "s24", "translation": {
 "en": "As in your saying to one who hesitates over a matter: «I see you putting one foot forward and drawing the other back»." + R_EN,
 "tr": "Bir işte tereddüt edene şöyle demen gibi: «Seni bir ayağını ileri atıp diğerini geri çekerken görüyorum»." + R_TR},
 "majaz": mj(6, "murakkab", "tamthil", {"en": "putting one foot forward and drawing the other back — the picture of a man at a threshold", "tr": "bir ayağı ileri atıp diğerini geri çekmek — eşikte duran adamın resmi"}, {"en": "hesitating — the whole clause is lent to the state of the waverer", "tr": "tereddüt etmek — cümlenin bütünü kararsızın hâline ödünç verilmiştir"},
             istiara=ist("murakkab")),
 "tokens": [
  kaq("كَقَوْلِكَ", "pron-2ms", "", K),
  tok("لِلْمُتَرَدِّدِ","mutaraddid","noun",[K, "huruf-jarr", "ism-fail", "form-v-verbs"], "جَارٌّ وَمَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ الْخَامِسِ.", "«to the one who hesitates» — ism fa'il of Form V.", "«tereddüt edene» — V. bâbın ism-i fâili.",
      segments=[seg("لِ","li","part"), seg("الْمُتَرَدِّدِ","mutaraddid","noun")]),
  tok("فِي","fi","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«-de»."),
  tok("أَمْرٍ","amr","noun",[K, "huruf-jarr"], "مَجْرُورٌ.", "«a matter».", "«bir iş».", punct=":"),
  tok("إِنِّي","inna","part",[K, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا.", "«indeed I» — inna with its ism.", "«şüphesiz ben» — inne ve ismi.",
      segments=[seg("إِنَّ","inna","part"), seg("ي","pron-1s","pron")]),
  tok("أَرَاكَ","raa","verb",[K, "inna-wa-akhawatuha", "mafulayn", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْكَافُ مَفْعُولٌ أَوَّلُ — الْجُمْلَةُ خَبَرُ إِنَّ.", "«I see you» — the mudari' of رَأَى; «you» the first object; the clause is inna's khabar.", "«seni görüyorum» — رَأَى'nın muzârii; «seni» birinci mef'ûl; cümle innenin haberi.",
      segments=[seg("أَرَا","raa","verb"), seg("كَ","pron-2ms","pron")]),
  tok("تُقَدِّمُ","qaddama","verb",[K, "mafulayn", "form-ii-verbs", "hal"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ مَفْعُولٌ ثَانٍ لِأَرَى (أَوْ حَالٌ) — رَأْسُ الْمَجَازِ الْمُرَكَّبِ: الْهَيْئَةُ كُلُّهَا لِلتَّرَدُّدِ.",
      "«putting forward» — the clause is the second object of «I see» (or a hal). The HEAD of the compound majaz: the whole picture stands for hesitation.",
      "«ileri atıyorsun» — cümle «görüyorum»un ikinci mef'ûlü (yahut hâl). Mürekkeb mecazın BAŞI: resmin bütünü tereddüt yerine."),
  tok("رِجْلًا","rijl","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a foot» — the object.", "«bir ayağı» — mef'ûl."),
  tok("وَتُؤَخِّرُ","akhkhara","verb",[K, "atf-nasaq", "form-ii-verbs"], "مَعْطُوفٌ — فِعْلٌ مُضَارِعٌ مِنَ الثَّانِي، مَهْمُوزُ الْفَاءِ.", "«and drawing back» — joined; Form II with a hamza first radical.", "«ve geri çekiyorsun» — matuf; fâ'sı hemzeli II. bâb.",
      segments=[seg("وَ","wa","conj"), seg("تُؤَخِّرُ","akhkhara","verb")]),
  tok("أُخْرَى","ukhra","noun",[K, "maful-bihi", "mamnu-min-sarf", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ.", "«the other» — the object; a diptote by the feminine alif.", "«diğerini» — mef'ûl; te'nis elifiyle gayr-i munsarif.", punct=".")]})

# ----------- s25 — the mathal (RESTORED)
S.append({"id": "s25", "translation": {
 "en": "And when its use becomes widespread it is called a PROVERB — and for that reason proverbs are not altered." + R_EN,
 "tr": "Kullanımı yayılınca MESEL diye adlandırılır — bu yüzden meseller değiştirilmez." + R_TR},
 "tokens": [
  tok("وَإِذَا","idha","part",[K, "idha-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — idha of the shart.", "«ve … -ınca» — şart mânâlı izâ.",
      segments=[seg("وَ","wa","conj"), seg("إِذَا","idha","part")]),
  tok("فَشَا","fasha","verb",[K, "idha-shartiyya", "naqis-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ وَاوِيٌّ (فَشَا يَفْشُو) — فِعْلُ الشَّرْطِ.", "«becomes widespread» — the naqis-waw mazi; the verb of the shart.", "«yayılır» — nâkıs-vâvî mâzî; şart fiili."),
  tok("اسْتِعْمَالُهُ","istimal","noun",[K, "fail", "idafa-definiteness", "form-x-verbs", "masdar"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ اسْتَعْمَلَ.", "«its use» — the fa'il; the masdar of Form X.", "«kullanımı» — fâil; X. bâbın masdarı.",
      segments=[seg("اسْتِعْمَالُ","istimal","noun"), seg("هُ","pron-3ms","pron")]),
  tok("سُمِّيَ","samma","verb",[K, "idha-shartiyya", "naib-al-fail", "form-ii-verbs", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — جَوَابُ إِذَا.", "«it is called» — the passive; the jawab of إِذَا.", "«adlandırılır» — meçhûl; izânın cevabı."),
  tok("مَثَلًا","mathal","noun",[K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a proverb» — the second object.", "«mesel» — ikinci mef'ûl.", punct="،"),
  tok("وَلِذَلِكَ","dhalika","pron",[K, "huruf-jarr", "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لِلتَّعْلِيلِ، وَذَلِكَ اسْمُ إِشَارَةٍ مَجْرُورٌ.", "«and for that reason» — the lam of cause over the demonstrative.", "«ve bu yüzden» — işaret ismi üzerinde ta'lil lâmı.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","part"), seg("ذَلِكَ","dhalika","pron")]),
  tok("لَا","la-nafiya","part",[K, "mudari-marfu"], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("تُغَيَّرُ","ghayyara","verb",[K, "naib-al-fail", "form-ii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«are altered» — the passive mudari'.", "«değiştirilir» — meçhûl muzâri."),
  tok("الْأَمْثَالُ","mathal","noun",[K, "naib-al-fail", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — جَمْعُ مَثَلٍ.", "«the proverbs» — the deputy doer; plural of مَثَل.", "«meseller» — nâib-i fâil; مَثَل'in çoğulu.", punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
  "saada-climb": {"lemma": "صَعِدَ", "pos": "verb", "root": "ص ع د", "gloss": {"en": "to climb, ascend", "tr": "yükselmek, çıkmak"}, "level": 3},
 "asliyya": g("أَصْلِيَّة", "أ ص ل", "noun", "asliyya — the istiʿara whose borrowed word is a noun of a kind", "asliyye — ödünç lafzı cins ismi olan istiâre", 6),
 "tabaiyya": g("تَبَعِيَّة", "ت ب ع", "noun", "tabaʿiyya — the istiʿara in a verb, a derived noun or a particle, following the likening in the meaning", "tebeiyye — fiilde, müştakta yahut harfte, mânâdaki benzetmeye tâbi istiâre", 6),
 "asli": g("أَصْلِيّ", "أ ص ل", "noun", "original (nisba of أَصْل)", "aslî (أَصْل'e nisbet)", 3),
 "qatl": find_gloss("qatl"),
 "ishtaqqa": g("اِشْتَقَّ", "ش ق ق", "verb", "to derive (a word) (Form VIII, doubled)", "türetmek (VIII. bâb, muzâaf)", 5, form="VIII"),
 "masdar-noun": g("مَصْدَر", "ص د ر", "noun", "the masdar — the verbal noun the verb's forms issue from", "masdar — fiil kalıplarının çıktığı isim", 3, plural="مَصَادِر"),
 "mutaallaq": g("مُتَعَلَّق", "ع ل ق", "noun", "what a thing hangs on, its object of relation (ism mafʿul of تَعَلَّقَ)", "müteallak — bir şeyin bağlandığı, ilgili olduğu şey (تَعَلَّقَ'nin ism-i mef'ûlü)", 6),
 "nataqa": g("نَطَقَ", "ن ط ق", "verb", "to speak, utter (نَطَقَ يَنْطِقُ)", "konuşmak, söylemek (نَطَقَ يَنْطِقُ)", 3, form="I"),
 "natiq": g("نَاطِق", "ن ط ق", "noun", "speaking (ism faʿil of نَطَقَ)", "konuşan, nâtık (نَطَقَ'nin ism-i fâili)", 4),
 "iltaqata": g("اِلْتَقَطَ", "ل ق ط", "verb", "to pick up (Form VIII)", "yerden almak, bulup almak (VIII. bâb)", 4, form="VIII"),
 "al-family": g("آل", "أ و ل", "noun", "family, house, people (of)", "âl, aile, hanedan", 3),
 "firawn": g("فِرْعَوْن", None, "propn", "Pharaoh", "Firavun", 2),
 "aduww": find_gloss("aduww"),
 "hazan": g("حَزَن", "ح ز ن", "noun", "grief", "tasa, hüzün", 3),
 "lam-letter": g("لَام", None, "noun", "the letter lam — here the particle لِ", "lâm harfi — burada لِ edatı", 2),
 "aqiba": g("عَاقِبَة", "ع ق ب", "noun", "outcome, end result", "âkıbet, sonuç", 3, plural="عَوَاقِب"),
 "talil": g("تَعْلِيل", "ع ل ل", "noun", "giving the cause, purpose (the lam of taʿlil)", "ta'lil — sebep bildirme (ta'lil lâmı)", 5),
 "tarattub": g("تَرَتُّب", "ر ت ب", "noun", "following upon, resulting from (masdar of تَرَتَّبَ)", "terettüb — bir şeyin ardından gelme (تَرَتَّبَ'nin masdarı)", 6),
 "fail-doer": g("فَاعِل", "ف ع ل", "noun", "the faʿil — the doer, the verb's subject", "fâil — fiilin öznesi", 2),
 "maful-object": g("مَفْعُول", "ف ع ل", "noun", "the mafʿul — the object", "mef'ûl — nesne", 2),
 "majrur-noun": g("مَجْرُور", "ج ر ر", "noun", "the majrur — the noun after a jarr particle", "mecrûr — cer harfinden sonraki isim", 2),
 "bukhl": g("بُخْل", "ب خ ل", "noun", "miserliness", "cimrilik", 3),
 "ahya": find_gloss("ahya"),
 "samah": g("سَمَاح", "س م ح", "noun", "generosity, liberality", "cömertlik, semâhat", 4),
 "qara-host": g("قَرَى", "ق ر ي", "verb", "to entertain a guest, offer hospitality (naqis-ya: قَرَى يَقْرِي)", "misafiri ağırlamak (nâkıs-yâî: قَرَى يَقْرِي)", 5, form="I"),
 "lahdhamiyyat": g("لَهْذَمِيَّات", "ل ه ذ م", "noun", "sharp, cutting spears (nisba to لَهْذَم)", "keskin mızraklar (لَهْذَم'e nisbet)", 6),
 "qadda": g("قَدَّ", "ق د د", "verb", "to cut, slit lengthwise (doubled: قَدَّ يَقُدُّ)", "yarmak, uzunlamasına kesmek (muzâaf: قَدَّ يَقُدُّ)", 5, form="I"),
 "khata-sew": g("خَاطَ", "خ ي ط", "verb", "to sew (hollow-ya: خَاطَ يَخِيطُ)", "dikmek (ecvef-yâî: خَاطَ يَخِيطُ)", 3, form="I"),
 "zarrad": g("زَرَّاد", "ز ر د", "noun", "maker of coats of mail", "zırh yapan, zırhçı", 6),
 "bashshara": find_gloss("bashshara"), "adhab": find_gloss("adhab"), "alim-painful": find_gloss("alim-painful"),
 "dhikr": find_gloss("dhikr"),
 "mulaim": g("مُلَائِم", "ل أ م", "noun", "the mulaʾim — what suits one of the istiʿara's two ends (ism faʿil of لَاءَمَ)", "mülâim — istiârenin iki tarafından birine uyan şey (لَاءَمَ'nin ism-i fâili)", 6),
 "mutlaqa": g("مُطْلَقَة", "ط ل ق", "noun", "mutlaqa — the istiʿara joined to no mulaʾim", "mutlaka — hiçbir mülâime bağlanmamış istiâre", 6),
 "mujarrada": g("مُجَرَّدَة", "ج ر د", "noun", "mujarrada — the istiʿara joined to what suits the mustaʿar lahu (the tajrid)", "mücerrede — müsteârun lehe uyana bağlanmış istiâre (tecrîd)", 6),
 "murashshaha": g("مُرَشَّحَة", "ر ش ح", "noun", "murashshaha — the istiʿara joined to what suits the mustaʿar minhu (the tarshih)", "müreşşaha — müsteârun minhe uyana bağlanmış istiâre (terşîh)", 6),
 "qarana": g("قَرَنَ", "ق ر ن", "verb", "to join, couple (قَرَنَ يَقْرِنُ)", "bağlamak, birleştirmek (قَرَنَ يَقْرِنُ)", 4, form="I"),
 "tafri": g("تَفْرِيع", "ف ر ع", "noun", "branching — building further speech on the istiʿara (masdar of فَرَّعَ)", "tefrî — istiâre üzerine söz kurma (فَرَّعَ'nin masdarı)", 6),
 "laama": g("لَاءَمَ", "ل أ م", "verb", "to suit, fit (Form III)", "uymak, uygun düşmek (III. bâb)", 5, form="III"),
 "ghamr": g("غَمْر", "غ م ر", "noun", "abundant, overflowing (of giving)", "bol, taşkın (ihsan için)", 6),
 "rida": g("رِدَاء", "ر د ي", "noun", "cloak, upper garment", "ridâ, üste giyilen örtü", 4, plural="أَرْدِيَة"),
 "tabassama": find_gloss("tabassama"),
 "dahik": find_gloss("dahik"),
 "ghaliqa": g("غَلِقَ", "غ ل ق", "verb", "to fall forfeit, become a pledge past redeeming (غَلِقَ يَغْلَقُ)", "rehin düşmek, kurtarılamaz olmak (غَلِقَ يَغْلَقُ)", 6, form="I"),
 "dahka": g("ضَحْكَة", "ض ح ك", "noun", "a laugh", "gülüş", 3),
 "raqaba": find_gloss("raqaba"),
 "ishtara": find_gloss("ishtara"),
 "ijtamaa": find_gloss("ijtamaa"),
 "zuhayr": g("زُهَيْر", None, "noun", "Zuhayr (b. Abi Sulma), the pre-Islamic poet", "Züheyr (b. Ebî Sülmâ), câhiliye şairi", 5),
 "tarshih": g("تَرْشِيح", "ر ش ح", "noun", "the tarshih — joining the istiʿara to what suits the mustaʿar minhu (masdar of رَشَّحَ)", "terşîh — istiâreyi müsteârun minhe uyanla bir araya getirme (رَشَّحَ'nin masdarı)", 6),
 "ablagh": g("أَبْلَغُ", "ب ل غ", "noun", "more eloquent (ism tafdil)", "daha beliğ (ism-i tafdîl)", 4),
 "ishtimal": find_gloss("ishtimal"),
 "mabna": g("مَبْنًى", "ب ن ي", "noun", "foundation, what a thing is built on", "binâ, temel, üzerine kurulduğu şey", 5),
 "tanasi": g("تَنَاسٍ (التَّنَاسِي)", "ن س ي", "noun", "feigned forgetting (masdar of تَنَاسَى)", "tenâsî — unutmuş görünme (تَنَاسَى'nın masdarı)", 6),
 "uluww": g("عُلُوّ", "ع ل و", "noun", "highness, height", "yükseklik, ulüvv", 4),
 "qadr": find_gloss("qadr"),
 "makan": find_gloss("makan"),
 "jahul": g("جَهُول", "ج ه ل", "noun", "very ignorant (intensive فَعُول)", "çok cahil (mübalağa فَعُول)", 5),
 "far-branch": g("فَرْع", "ف ر ع", "noun", "branch — what is built on the root", "fer' — asıl üzerine kurulan", 3, plural="فُرُوع"),
 "itiraf": g("اِعْتِرَاف", "ع ر ف", "noun", "acknowledging (masdar of اِعْتَرَفَ)", "itiraf, kabul etme (اِعْتَرَفَ'nin masdarı)", 4),
 "maskan": g("مَسْكَن", "س ك ن", "noun", "dwelling (ism makan of سَكَنَ)", "mesken, konak (سَكَنَ'nin ism-i mekânı)", 3, plural="مَسَاكِن"),
 "azza": g("عَزَّى", "ع ز ي", "verb", "to console (Form II, naqis)", "teselli etmek (II. bâb, nâkıs)", 4, form="II"),
 "fuad": g("فُؤَاد", "ف أ د", "noun", "heart", "gönül, fuâd", 3, plural="أَفْئِدَة"),
 "aza": g("عَزَاء", "ع ز ي", "noun", "consolation", "tesellî", 4),
 "rijl": g("رِجْل", "ر ج ل", "noun", "foot, leg", "ayak", 2, plural="أَرْجُل"),
 "qaddama": find_gloss("qaddama"),
 "akhkhara": g("أَخَّرَ", "أ خ ر", "verb", "to put back, delay (Form II)", "geri çekmek, geciktirmek (II. bâb)", 3, form="II"),
 "fasha": g("فَشَا", "ف ش و", "verb", "to spread, become widespread (naqis-waw: فَشَا يَفْشُو)", "yayılmak (nâkıs-vâvî: فَشَا يَفْشُو)", 5, form="I"),
 "istimal": find_gloss("istimal"),
 "ghayyara": g("غَيَّرَ", "غ ي ر", "verb", "to alter, change (Form II)", "değiştirmek (II. bâb)", 3, form="II"),
 "jami-link": find_gloss("jami-link"), "qism": find_gloss("qism"),
 "pron-3md": g("ـا (أَلِفُ الِاثْنَيْنِ)", None, "pron", "they two (the dual alif on the verb)", "o ikisi (fiildeki tesniye elifi)", 1),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/53.json").write_text(
    json.dumps({"chapter": 53, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 53 for c in man["chapters"]):
    man["chapters"].append({"n": 53, "title": TITLE53})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.53.0"
ADD_EN = (" Chapter 53 (lines ~3640-3720, sahifa 126-128) carries the istiʿara by the word (asliyya / tabaʿiyya), the "
          "seat of the tabaʿiyya's clue, the mutlaqa / mujarrada / murashshaha, the tanasi and the compound majaz: the "
          "ayat 28:8 (s6), 9:34 (s11), 2:16 (s17), the hemistich قَتَلَ الْبُخْلَ وَأَحْيَا السَّمَاحَا (s9), the bayts of "
          "s10 (نَقْرِيهِمْ لَهْذَمِيَّاتٍ), s15 (غَمْرُ الرِّدَاءِ), s21 (وَيَصْعَدُ حَتَّى يَظُنَّ الْجَهُولُ), s22 (هِيَ الشَّمْسُ) and "
          "Zuhayr's (s18), and the stock نَطَقَتِ الْحَالُ (s5), عِنْدِي أَسَدٌ (s13), تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى "
          "(s24) are Arabic as the source prints it, inside restored frames; the alif of itlaq on السَّمَاحَا and the "
          "rhyme kasras on زَرَّادِ and تُقَلَّمِ are kept as printed. s1-s4, s7-s8, s12-s14, s16, s19-s20, s23, s25 and "
          "the frames of the examples are RESTORATIONS, not quotations: the source carries those steps only in "
          "Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's register; each is "
          "marked «restored» in its translation. Every istiʿara carries an authored `majaz` frame whose `istiara` "
          "object names the lafz, the clue's seat and the mulaʾim words by index; the compound majaz of s24 is a "
          "`murakkab` frame; هِيَ الشَّمْسُ (s22) is a baligh tashbih frame with the branch built on it.")
ADD_TR = (" Elli üçüncü bâb (satır ~3640-3720, sahife 126-128) istiâreyi lafız itibariyle (asliyye / tebeiyye), "
          "tebeiyyenin karînesinin yerini, mutlaka / mücerrede / müreşşahayı, tenâsîyi ve mürekkeb mecazı taşır: 28:8 "
          "(s6), 9:34 (s11), 2:16 (s17) âyetleri, قَتَلَ الْبُخْلَ وَأَحْيَا السَّمَاحَا mısraı (s9), s10 (نَقْرِيهِمْ "
          "لَهْذَمِيَّاتٍ), s15 (غَمْرُ الرِّدَاءِ), s21 (وَيَصْعَدُ حَتَّى يَظُنَّ الْجَهُولُ), s22 (هِيَ الشَّمْسُ) beyitleri ile "
          "Züheyr'inki (s18), ve yerleşik نَطَقَتِ الْحَالُ (s5), عِنْدِي أَسَدٌ (s13), تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى (s24), "
          "geri yazılmış çerçeveler içinde kaynağın bastığı Arapçadır; السَّمَاحَا üzerindeki ıtlak elifi ile زَرَّادِ ve "
          "تُقَلَّمِ üzerindeki revî kesreleri basıldığı gibi korunmuştur. s1-s4, s7-s8, s12-s14, s16, s19-s20, s23, s25 "
          "ile örneklerin çerçeveleri ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla "
          "taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» "
          "diye işaretlidir. Her istiâre, `istiara` nesnesi lafzı, karînenin yerini ve mülâim kelimeleri indeksle "
          "adlandıran müellif eliyle yazılmış bir `majaz` çerçevesi taşır; s24'ün mürekkeb mecazı bir `murakkab` "
          "çerçevesi; هِيَ الشَّمْسُ (s22), üzerine fer' kurulmuş bir belîğ teşbih çerçevesidir.")
if "3640-3720" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
other = {}
for p in (ROOT / "content/samples").iterdir():
    if p.name == PKG.name or not (p / "glossary.json").exists(): continue
    for k, v in json.loads((p / "glossary.json").read_text(encoding="utf-8"))["entries"].items():
        other.setdefault(k, set()).add(bare(v["lemma"]).split(" ")[0])
for k, v in GLOSS_ADD.items():
    if k in gl["entries"]:
        assert bare(gl["entries"][k]["lemma"]).replace("ال", "", 1) == bare(v["lemma"]).replace("ال", "", 1), f"key {k} already means {gl['entries'][k]['lemma']}"
        continue
    if k in other:
        assert bare(v["lemma"]).split(" ")[0] in other[k], f"key {k} means something else elsewhere: {other[k]}"
    gl["entries"][k] = v
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
V = mo["verbs"]
def put(key, e):
    if key not in V: V[key] = e
def doubled(bab, yv, m, mm, d, dd, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    # حَجَّ template: the merge holds while the twin stays vowelled, breaks before a sukun-initial ending
    b = _sg.BABS[bab]
    return _sg.idgham(_sg.entry(b[0] + " — مُضَاعَفٌ", b[1], masdar, fail, _sg.mazi14(m, mm), _sg.mudari14(yv, d, dd), amr,
                                "يَ" + d + "َ", "يَ" + d + "َ", "تَ" + d + "َ", maful, pmz, pmd, note))
put("nataqa", _sg.sound1("daraba", "نَطَق", "نْطِق", "اِنْطِق", "نُطْق", "نَاطِق", "مَنْطُوق", "نُطِقَ", "يُنْطَقُ",
                         "فِي الْمَتْنِ: نَطَقَتِ الْحَالُ — كُسِرَتْ تَاءُ التَّأْنِيثِ لِالْتِقَاءِ السَّاكِنَيْنِ."))
put("iltaqata", _sg.derived(_sg.B8, _sg.W8, "َ", "اِلْتَقَط", "لْتَقِط", "اِلْتَقِط", "اِلْتِقَاط", "مُلْتَقِط", "مُلْتَقَط", "اُلْتُقِطَ", "يُلْتَقَطُ"))
put("ishtaqqa", doubled("nasara", "َ", "اِشْتَقّ", "اِشْتَقَق", "شْتَقّ", "شْتَقِق",
                        ["اِشْتَقَّ", "اِشْتَقَّا", "اِشْتَقُّوا", "اِشْتَقِّي", "اِشْتَقَّا", "اِشْتَقِقْنَ"], "اِشْتِقَاق", "مُشْتَقّ", "مُشْتَقّ", "اُشْتُقَّ", "يُشْتَقُّ",
                        "مُضَاعَفٌ عَلَى افْتَعَلَ: اِشْتَقَّ يَشْتَقُّ؛ الْمَجْهُولُ يُشْتَقُّ — وَاسْمُ الْفَاعِلِ وَالْمَفْعُولِ سَوَاءٌ فِي اللَّفْظِ (مُشْتَقّ)."))
V["ishtaqqa"]["bab"] = _sg.B8 + " — مُضَاعَفٌ"; V["ishtaqqa"]["wazn"] = _sg.W8
put("qara-host", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "قَرَ", "قْر", "i", "اِقْر", "قِرًى", "قَارٍ (الْقَارِي)", "مَقْرِيّ", "قُرِيَ", "يُقْرَى",
                            "نَاقِصٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ: قَرَى الضَّيْفَ يَقْرِيهِ — نَقْرِيهِمْ."))
put("qadda", doubled("nasara", "َ", "قَدّ", "قَدَد", "قُدّ", "قْدُد", ["قُدَّ", "قُدَّا", "قُدُّوا", "قُدِّي", "قُدَّا", "اُقْدُدْنَ"], "قَدّ", "قَادّ", "مَقْدُود", "قُدَّ", "يُقَدُّ",
                     "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: قَدَّ يَقُدُّ — نَقُدُّ بِهَا."))
put("khata-sew", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "خَاط", "خِط", "خِيط", "خِط", "خِيط", "خِط", "خِيَاطَة", "خَائِط", "مَخِيط", "خِيطَ", "يُخَاطُ",
                         "أَجْوَفُ يَائِيٌّ مِنْ بَابِ ضَرَبَ: خَاطَ يَخِيطُ."))
put("saada-climb", _sg.sound1("samia", "صَعِد", "صْعَد", "اِصْعَد", "صُعُود", "صَاعِد", "مَصْعُود", "صُعِدَ", "يُصْعَدُ",
                         "مِنْ بَابِ سَمِعَ: صَعِدَ يَصْعَدُ — وَيَصْعَدُ فِي الْبَيْتِ اسْتِعَارَةٌ تَبَعِيَّةٌ."))
put("qarana", _sg.idgham(_sg.sound1("daraba", "قَرَن", "قْرِن", "اِقْرِن", "قَرْن", "قَارِن", "مَقْرُون", "قُرِنَ", "يُقْرَنُ",
                         "فِي الْمَتْنِ مَبْنِيٌّ لِلْمَجْهُولِ: قُرِنَ، لَمْ تُقْرَنْ.")))
put("laama", _sg.derived(_sg.B3, _sg.W3, "ُ", "لَاءَم", "لَائِم", "لَائِم", "مُلَاءَمَة", "مُلَائِم", "مُلَاءَم", "لُوئِمَ", "يُلَاءَمُ",
                         "مَهْمُوزُ الْعَيْنِ عَلَى فَاعَلَ: لَاءَمَ يُلَائِمُ؛ الْهَمْزَةُ عَلَى نَبْرَةٍ بَعْدَ الْكَسْرَةِ (يُلَائِمُ)."))
put("tabassama", find_morph("tabassama"))
put("ghaliqa", _sg.sound1("samia", "غَلِق", "غْلَق", "اِغْلَق", "غَلَق", "غَلِق", None, None, None,
                          "مِنْ بَابِ سَمِعَ: غَلِقَ الرَّهْنُ يَغْلَقُ — لَمْ يُفَكَّ."))
put("ishtara", find_morph("ishtara"))
put("azza", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "عَزَّ", "عَزّ", "i", "عَزّ", "تَعْزِيَة", "مُعَزٍّ (الْمُعَزِّي)", "مُعَزًّى", "عُزِّيَ", "يُعَزَّى",
                              "نَاقِصٌ عَلَى فَعَّلَ: عَزَّى يُعَزِّي؛ الْأَمْرُ عَزِّ بِحَذْفِ الْيَاءِ."))
put("qaddama", find_morph("qaddama"))
put("akhkhara", _sg.derived(_sg.B2, _sg.W2, "ُ", "أَخَّر", "ؤَخِّر", "أَخِّر", "تَأْخِير", "مُؤَخِّر", "مُؤَخَّر", "أُخِّرَ", "يُؤَخَّرُ",
                            "مَهْمُوزُ الْفَاءِ عَلَى فَعَّلَ: الْهَمْزَةُ عَلَى وَاوٍ بَعْدَ الضَّمَّةِ (يُؤَخِّرُ)."))
put("fasha", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "فَشَ", "فْش", "u", "اُفْش", "فُشُوّ", "فَاشٍ (الْفَاشِي)", None, None, None,
                        "نَاقِصٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ: فَشَا يَفْشُو — فَشَا اسْتِعْمَالُهُ."))
put("ghayyara", _sg.derived(_sg.B2, _sg.W2, "ُ", "غَيَّر", "غَيِّر", "غَيِّر", "تَغْيِير", "مُغَيِّر", "مُغَيَّر", "غُيِّرَ", "يُغَيَّرُ",
                            "فِي الْمَتْنِ مَبْنِيٌّ لِلْمَجْهُولِ: لَا تُغَيَّرُ الْأَمْثَالُ."))
for k in ("ahya", "bashshara", "ijtamaa"):
    put(k, find_morph(k))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the notes
GR = ROOT / "content/grammar"
NOTE_R = {
 "id": "tarshih-wa-tajrid",
 "title": {"ar": "الْمُطْلَقَةُ وَالْمُجَرَّدَةُ وَالْمُرَشَّحَةُ — الْمُلَائِمُ وَتَنَاسِي التَّشْبِيهِ", "en": "The mutlaqa, the mujarrada and the murashshaha — the mulaʾim and the forgetting of the likening", "tr": "Mutlaka, mücerrede ve müreşşaha — mülâim ve benzetmenin unutulması"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الاستعارة باعتبار ذكر الملائم: المطلقة والمجردة والمرشحة"],
 "question": {
  "en": ["Is anything JOINED to the istiʿara? Nothing — عِنْدِي أَسَدٌ: MUTLAQA. A word that suits the MUSTAʿAR LAHU (the thing meant): MUJARRADA — غَمْرُ الرِّدَاءِ, «abundant» suits giving, not a cloak. A word that suits the MUSTAʿAR MINHU (the lent word's own meaning): MURASHSHAHA — فَمَا رَبِحَتْ تِجَارَتُهُمْ, profit and trade suit buying.",
         "Can both stand together? Yes — Zuhayr's lion: arms and being hurled into battle suit the warrior (tajrid), a mane and unclipped claws suit the lion (tarshih).",
         "Why is the tarshih MORE ELOQUENT? Because it feigns to FORGET the likening and treats the mushabbah as the bihi itself — so that on a man's high rank is built what belongs to high place: وَيَصْعَدُ حَتَّى يَظُنَّ الْجَهُولُ بِأَنَّ لَهُ حَاجَةً فِي السَّمَاءِ."],
  "tr": ["İstiâreye bir şey BAĞLANMIŞ mı? Hiçbir şey — عِنْدِي أَسَدٌ: MUTLAKA. MÜSTEÂRUN LEHe (kastedilene) uyan bir kelime: MÜCERREDE — غَمْرُ الرِّدَاءِ, «bol» ridâya değil ihsana uyar. MÜSTEÂRUN MİNHe (ödünç kelimenin kendi mânâsına) uyan bir kelime: MÜREŞŞAHA — فَمَا رَبِحَتْ تِجَارَتُهُمْ, kâr ve ticaret satın almaya uyar.",
         "İkisi bir arada durabilir mi? Evet — Züheyr'in arslanı: silâh ve savaşa atılmışlık savaşçıya (tecrîd), yele ve kesilmemiş pençe arslana (terşîh) uyar.",
         "Terşîh niçin DAHA BELİĞ? Çünkü benzetmeyi UNUTMUŞ görünür ve müşebbehi bihin kendisi sayar — öyle ki adamın kadrinin yüksekliği üzerine mekân yüksekliğine ait olan kurulur: وَيَصْعَدُ حَتَّى يَظُنَّ الْجَهُولُ بِأَنَّ لَهُ حَاجَةً فِي السَّمَاءِ."]},
 "plain": {
  "en": "By what is joined to it the istiʿara is MUTLAQA (nothing), MUJARRADA (a word suiting the thing meant: tajrid) or MURASHSHAHA (a word suiting the lent word's own sense: tarshih). The tarshih is strongest: it feigns to forget a likening was made. The engine names the mulaʾim words and their side.",
  "tr": "Bağlananına göre istiâre MUTLAKA (hiçbir şey), MÜCERREDE (kastedilene uyan kelime: tecrîd) yahut MÜREŞŞAHA (ödünç kelimenin kendi mânâsına uyan kelime: terşîh) olur. Terşîh en kuvvetlisidir; çünkü benzetme yapıldığını unutmuş görünür. Motor mülâim kelimeleri ve hangi tarafa uyduklarını adlandırır."},
 "explanation": {
  "en": "By the MENTION OF THE MULAʾIM — a word that suits one of the two ends — the istiʿara is of three kinds. MUTLAQA: joined to no quality and no branching of speech, عِنْدِي أَسَدٌ, the lion alone. MUJARRADA: joined to what suits the MUSTAʿAR LAHU, the thing meant — in غَمْرُ الرِّدَاءِ إِذَا تَبَسَّمَ ضَاحِكًا • غَلِقَتْ لِضَحْكَتِهِ رِقَابُ الْمَالِ the cloak is lent for giving, and «abundant» (غَمْر) suits giving, not cloth: the istiʿara is STRIPPED (the TAJRID) back toward its meaning. MURASHSHAHA: joined to what suits the MUSTAʿAR MINHU, the lent word's own sense — in أُولَئِكَ الَّذِينَ اشْتَرَوُا الضَّلَالَةَ بِالْهُدَى فَمَا رَبِحَتْ تِجَارَتُهُمْ (2:16) buying is lent for exchanging, and «profited» and «their trade» belong to buying: the istiʿara is FED (the TARSHIH) with its literal sense. The two may meet, as in Zuhayr's لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ • لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ: arms and being hurled into battle suit the man (tajrid), the mane and the unclipped claws suit the lion (tarshih). The tarshih is MORE ELOQUENT, since it contains the realising of the exaggeration; and it is BUILT ON FORGETTING THE LIKENING (تَنَاسِي التَّشْبِيهِ) — the speaker acts as if the mushabbah were the bihi itself, so that upon highness of RANK is built what is built upon highness of PLACE: وَيَصْعَدُ حَتَّى يَظُنَّ الْجَهُولُ • بِأَنَّ لَهُ حَاجَةً فِي السَّمَاءِ, the whole second half branching from the climbing. Speech may also be built on the BRANCH while the ROOT is acknowledged, as in هِيَ الشَّمْسُ مَسْكَنُهَا فِي السَّمَاءِ • فَعَزِّ الْفُؤَادَ عَزَاءً جَمِيلًا: the likening stands as a baligh tashbih (she is the sun), and «her dwelling is in the sky» — hence the consolation — is built on it. WHAT THE ENGINE CLAIMS: for every istiʿara it reads the words that hang on the lent word — its na'ts, its dependents, the clauses that branch from it — and sorts each as suiting the minhu (the lent word's own field: mane, claws, profit, sky) or the lahu (the meant thing's field: arms, abundance), from the corpus glosses and a stored field table; a frame with no such word is MUTLAQA. It grades that reading against the authored mulaʾim indices, and it never decides the poet's intent — the murad on the frame carries it.",
  "tr": "MÜLÂİMİN ZİKRİne — iki taraftan birine uyan bir kelime — göre istiâre üç kısımdır. MUTLAKA: hiçbir vasfa ve söz tefrîine bağlanmamış, عِنْدِي أَسَدٌ, yalnız arslan. MÜCERREDE: MÜSTEÂRUN LEHe, kastedilene uyana bağlanmış — غَمْرُ الرِّدَاءِ إِذَا تَبَسَّمَ ضَاحِكًا • غَلِقَتْ لِضَحْكَتِهِ رِقَابُ الْمَالِ beytinde ridâ ihsan yerine ödünç, «bol» (غَمْر) kumaşa değil ihsana uyar: istiâre mânâsına doğru SOYULMUŞTUR (TECRÎD). MÜREŞŞAHA: MÜSTEÂRUN MİNHe, ödünç kelimenin kendi mânâsına uyana bağlanmış — أُولَئِكَ الَّذِينَ اشْتَرَوُا الضَّلَالَةَ بِالْهُدَى فَمَا رَبِحَتْ تِجَارَتُهُمْ'de (2:16) satın almak değişmek yerine ödünç, «kâr etti» ve «ticaretleri» satın almaya aittir: istiâre hakikî mânâsıyla BESLENMİŞTİR (TERŞÎH). İkisi birleşebilir; Züheyr'in لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ • لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ beytinde silâh ve savaşa atılmışlık adama (tecrîd), yele ve kesilmemiş pençe arslana (terşîh) uyar. Terşîh DAHA BELİĞdir; mübalağanın tahkikini içerir ve BENZETMEYİ UNUTMA (تَنَاسِي التَّشْبِيهِ) üzerine kurulur — konuşan müşebbehi bihin kendisi sayar; öyle ki KADİR yüksekliği üzerine MEKÂN yüksekliğine ait olan kurulur: وَيَصْعَدُ حَتَّى يَظُنَّ الْجَهُولُ • بِأَنَّ لَهُ حَاجَةً فِي السَّمَاءِ; ikinci yarının tamamı tırmanmadan dallanır. Söz, ASIL itiraf edilmekle birlikte FER' üzerine de kurulabilir: هِيَ الشَّمْسُ مَسْكَنُهَا فِي السَّمَاءِ • فَعَزِّ الْفُؤَادَ عَزَاءً جَمِيلًا — benzetme belîğ teşbih olarak durur (o güneştir), «konağı göktedir» — dolayısıyla tesellî — onun üzerine kurulur. MOTORUN İDDİASI: her istiâre için ödünç kelimeye bağlı kelimeleri — na'tlarını, bağımlılarını, ondan dallanan cümleleri — okur ve her birini derlem karşılıklarından ve saklı bir alan tablosundan minhe (ödünç kelimenin kendi alanı: yele, pençe, kâr, gök) yahut lehe (kastedilenin alanı: silâh, bolluk) uyan diye ayırır; böyle bir kelimesi olmayan çerçeve MUTLAKAdır. Bu okumayı müellifin mülâim indekslerine karşı sınar; şairin niyetine asla karar vermez — çerçevedeki murâd onu taşır."},
 "examples": [
  {"ar": "عِنْدِي أَسَدٌ", "en": "mutlaqa: nothing joined.", "tr": "mutlaka: hiçbir şey bağlı değil.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "غَمْرُ الرِّدَاءِ", "en": "mujarrada: «abundant» suits the giving meant.", "tr": "mücerrede: «bol», kastedilen ihsana uyar.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"},
  {"ar": "فَمَا رَبِحَتْ تِجَارَتُهُمْ", "en": "murashshaha: profit and trade suit the lent «buying».", "tr": "müreşşaha: kâr ve ticaret ödünç «satın alma»ya uyar.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"},
  {"ar": "لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ", "en": "tarshih after tajrid: both in one lion.", "tr": "tecrîdden sonra terşîh: ikisi bir arslanda.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"}],
 "commonMistakes": [
  {"wrong": "«رَبِحَتْ تِجَارَتُهُمْ: ticaret kastedilen mânâya uyar, tecrîddir»",
   "right": "«Terşîhtir: kâr ve ticaret, ödünç alınan SATIN ALMAnın levâzımındandır; kastedilen değişmenin değil»",
   "why": {"en": "The test is which END the joined word suits: the lent word's own sense (minhu) or the thing meant (lahu). Profit belongs to buying, not to choosing error.", "tr": "Ölçü, bağlanan kelimenin hangi TARAFa uyduğudur: ödünç kelimenin kendi mânâsı (minh) mı, kastedilen (leh) mi. Kâr satın almaya aittir, dalâleti seçmeye değil."}},
  {"wrong": "«Terşîh istiâreyi zayıflatır: arslanın yelesini anmak benzetmeyi açığa çıkarır»",
   "right": "«Terşîh daha beliğdir: benzetmeyi unutmuş görünür ve müşebbehi bihin kendisi sayar»",
   "why": {"en": "Naming the lion's mane does not confess a likening; it insists there is none — the man IS the lion. That is the tanasi the exaggeration rides on.", "tr": "Arslanın yelesini anmak benzetmeyi itiraf etmez; benzetme yok der — adam arslanın KENDİSİdir. Mübalağanın bindiği tenâsî budur."}}],
 "relatedNotes": ["istiara-tabaiyya", "aqsam-al-istiara", "istiara", "arkan-al-istiara", "majaz-murakkab", "tashbih", "aqsam-al-tashbih", "naat-sifa", "jumla-sifa"]}
NOTE_K = {
 "id": "majaz-murakkab",
 "title": {"ar": "الْمَجَازُ الْمُرَكَّبُ — الِاسْتِعَارَةُ التَّمْثِيلِيَّةُ وَالْمَثَلُ", "en": "The compound majaz — the istiʿara of tamthil and the proverb", "tr": "Mürekkeb mecaz — temsilî istiâre ve mesel"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — المجاز المركب"],
 "question": {
  "en": ["Is it a single WORD that has moved, or a whole PICTURE? إِنِّي أَرَاكَ تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى said to a waverer: no single word is lent; the whole clause — a man with one foot forward and one back — stands for the state of hesitation. That is the COMPOUND majaz.",
         "What likening carries it? A likening of TAMTHIL: the wajh is drawn from several things together, and the compound is used for exaggeration.",
         "When does it become a PROVERB? When its use spreads. And a proverb is never altered — it is quoted as first said, whatever the gender or number of the case at hand."],
  "tr": ["Kaymış olan tek bir KELİME mi, bütün bir RESİM mi? Kararsıza söylenen إِنِّي أَرَاكَ تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى: tek kelime ödünç değildir; cümlenin bütünü — bir ayağı ileride bir ayağı geride adam — tereddüt hâli yerine durur. MÜREKKEB mecaz budur.",
         "Onu hangi benzetme taşır? TEMSİL benzetmesi: vech birçok şeyden birlikte çıkarılır ve mürekkeb, mübalağa için kullanılır.",
         "Ne zaman MESEL olur? Kullanımı yayılınca. Mesel asla değiştirilmez — eldeki durumun cinsi ve sayısı ne olursa olsun ilk söylendiği gibi aktarılır."]},
 "plain": {
  "en": "When a whole expression, not a word, is used for what it has been likened to by a tamthil — a picture drawn from several things — the majaz is COMPOUND (the istiʿara tamthiliyya). Spread by use it becomes a PROVERB, and proverbs are never altered. The engine reads the picture as one frame over the whole clause.",
  "tr": "Bir kelime değil bütün bir ifade, temsil — birçok şeyden çıkarılmış bir resim — ile benzetildiği şey için kullanılınca mecaz MÜREKKEBdir (temsilî istiâre). Kullanımla yayılınca MESEL olur ve meseller değiştirilmez. Motor resmi bütün cümle üzerinde tek çerçeve olarak okur."},
 "explanation": {
  "en": "The COMPOUND MAJAZ is the expression used for what has been likened to its original meaning by a likening of TAMTHIL — that is, the picture the words paint is likened, as a whole, to another state, and the words are then used for that state, for exaggeration. To one who hesitates over a matter you say إِنِّي أَرَاكَ تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى, «I see you put one foot forward and draw the other back»: no foot moves; the picture of a man stalled at a threshold is lent to the waverer's state, and the wajh — a going that is no going, a will that cancels itself — is drawn from the two movements together, which is what makes the likening a tamthil. Later writers call this the ISTIʿARA TAMTHILIYYA. When its use SPREADS it is called a MATHAL, a proverb; and because a proverb is quoted as it was first said, PROVERBS ARE NOT ALTERED: الصَّيْفَ ضَيَّعْتِ اللَّبَنَ keeps its feminine even when said to a man. WHAT THE ENGINE CLAIMS: a frame of kind `murakkab` spans the clause, headed by its first verb; the engine checks that the span is one clause (a verb with its dependents and what is joined to it), that no single word inside it is itself a stock istiʿara, and that the murad on the frame names a state, not a thing. It does not find compound majaz unaided: a picture is knowledge, and the authored frame carries it.",
  "tr": "MÜREKKEB MECAZ, aslî mânâsına TEMSİL benzetmesiyle benzetilmiş olan şeyde kullanılan lafızdır — yani kelimelerin çizdiği resim bütün olarak başka bir hâle benzetilir, sonra kelimeler mübalağa için o hâlde kullanılır. Bir işte tereddüt edene إِنِّي أَرَاكَ تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى dersin, «seni bir ayağını ileri atıp diğerini geri çekerken görüyorum»: hiçbir ayak kımıldamaz; eşikte takılmış adamın resmi kararsızın hâline ödünç verilir; vech — gitmeyen bir gidiş, kendini bozan bir irade — iki hareketten birlikte çıkarılır; benzetmeyi temsil yapan budur. Sonraki müellifler buna TEMSİLÎ İSTİÂRE der. Kullanımı YAYILINCA MESEL denir; mesel ilk söylendiği gibi aktarıldığından MESELLER DEĞİŞTİRİLMEZ: الصَّيْفَ ضَيَّعْتِ اللَّبَنَ erkeğe söylense de müennesliğini korur. MOTORUN İDDİASI: `murakkab` türünden çerçeve cümleyi kaplar, ilk fiili başıdır; motor kapsamın tek cümle olduğunu (fiil, bağımlıları ve ona atfedilen), içindeki hiçbir kelimenin kendi başına yerleşik istiâre olmadığını ve çerçevedeki murâdın bir şeyi değil bir hâli adlandırdığını sınar. Mürekkeb mecazı kendi başına bulmaz: resim bilgidir, müellif çerçevesi taşır."},
 "examples": [
  {"ar": "إِنِّي أَرَاكَ تُقَدِّمُ رِجْلًا وَتُؤَخِّرُ أُخْرَى", "en": "the whole picture for hesitation.", "tr": "bütün resim tereddüt yerine.", "sourceStory": "talkhis-al-miftah", "sentence": "s24"},
  {"ar": "وَإِذَا فَشَا اسْتِعْمَالُهُ سُمِّيَ مَثَلًا", "en": "spread by use, it is a proverb.", "tr": "kullanımla yayılınca meseldir.", "sourceStory": "talkhis-al-miftah", "sentence": "s25"}],
 "commonMistakes": [
  {"wrong": "«تُقَدِّمُ رِجْلًا: ayak, ‹adım› için müfred bir istiâredir»",
   "right": "«Mürekkebdir: tek kelime değil, iki hareketin resmi bütünüyle ödünç verilmiştir»",
   "why": {"en": "Take the foot alone and the picture collapses: what stands for hesitation is one foot forward WITH one foot back. The wajh is drawn from several things — a tamthil.", "tr": "Ayağı tek başına al, resim dağılır: tereddüt yerine duran, ileri bir ayakla BİRLİKTE geri bir ayaktır. Vech birçok şeyden çıkarılır — temsil."}},
  {"wrong": "«Erkeğe söylerken meseli الصَّيْفَ ضَيَّعْتَ اللَّبَنَ diye düzeltmeli»",
   "right": "«Mesel değiştirilmez: ilk söylendiği gibi, müennes tâ ile aktarılır»",
   "why": {"en": "A proverb is a quotation of its first occasion; its wording is the thing lent, not a template to conjugate.", "tr": "Mesel ilk vesilesinin aktarımıdır; ödünç verilen onun lafzıdır, çekilecek bir kalıp değil."}}],
 "relatedNotes": ["tarshih-wa-tajrid", "istiara", "aqsam-al-tashbih", "wajh-al-shabah", "majaz-mursal", "haqiqa-majaz", "mafulayn"]}
for n in (NOTE_R, NOTE_K):
    (GR / f"{n['id']}.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")
for nid, add in (("istiara-tabaiyya", ["tarshih-wa-tajrid", "majaz-murakkab"]), ("aqsam-al-istiara", ["tarshih-wa-tajrid"]),
                 ("istiara", ["tarshih-wa-tajrid", "majaz-murakkab"]), ("aqsam-al-tashbih", ["majaz-murakkab"])):
    fp = GR / f"{nid}.json"
    if not fp.exists(): continue
    w = json.loads(fp.read_text(encoding="utf-8"))
    ch = False
    for a in add:
        if a not in w.get("relatedNotes", []): w.setdefault("relatedNotes", []).append(a); ch = True
    if ch: fp.write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch53:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; notes tarshih-wa-tajrid, majaz-murakkab;",
      "majaz frames:", sum(len(x["majaz"]) if isinstance(x.get("majaz"), list) else (1 if x.get("majaz") else 0) for x in S))
