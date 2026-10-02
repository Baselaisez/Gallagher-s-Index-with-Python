# -*- coding: utf-8 -*-
"""Author chapter 52 of talkhis-al-miftah — أَقْسَامُ الِاسْتِعَارَةِ بِاعْتِبَارِ الطَّرَفَيْنِ
وَالْجَامِعِ (sahifa 124-126, lines ~3570-3640): the istiʿara by its two ends
(wifaqiyya / ʿinadiyya, with the tahakkum and the tamlih), by the jamiʿ
(inside or outside the two meanings; ʿammiyya / khassiyya, with the two
bayts), and the six kinds by the sensory or mental nature of the three.

  RESTORED (the source carries the step only in Turkish): s1-s2, s4-s7, s9-s10,
          s12-s14, s16, s18, and the frames of the examples.
  As printed: the ayat 6:122 (s3), 9:34 (s8), 20:88 (s19), 36:37 (s20),
          36:52 (s22), 15:94 (s23), 69:11 (s24); the hadith (s11); the bayts of
          Yazid b. Maslama (s15) and Kuthayyir (s17); رَأَيْتُ شَمْسًا (s21).

Every istiʿara carries an authored `majaz` frame with an `istiara` object —
the fields the SURFACE settles (lafz: asliyya / tabaʿiyya) and the fields
the chapter names (ends, jami, hissi) — which the IstiaraEngine is graded
against.
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
def ist(lafz, ends=None, jami=None, hissi=None, seat=None):
    d = {"lafz": lafz}
    if ends: d["ends"] = ends
    if jami: d["jami"] = jami
    if hissi: d["hissi"] = hissi
    if seat: d["qarinaSeat"] = seat
    return d
S = []
A = "aqsam-al-istiara"; I = "arkan-al-istiara"; T = "istiara-tabaiyya"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
TITLE52 = {"ar": "أَقْسَامُ الِاسْتِعَارَةِ بِاعْتِبَارِ الطَّرَفَيْنِ وَالْجَامِعِ، وَالْحِسِّيُّ وَالْعَقْلِيُّ مِنْهَا",
           "en": "The Kinds of Istiʿara by the Two Ends and the Jamiʿ, and the Sensory and the Mental among Them",
           "tr": "İstiârenin İki Taraf ve Câmi İtibariyle Kısımları, ve Onlardan Hissî ile Aklî Olanlar"}
P3MS = seg("هُ", "pron-3ms", "pron"); P3MP = seg("هُمْ", "pron-3mp", "pron")
def kaq(full="كَقَوْلِهِ", who="pron-3ms", punct=":"):
    pr = {"pron-3ms": "هِ", "pron-3mp": "هِمْ", "pron-2ms": "كَ"}[who]
    return tok(full, "qawl", "noun", [A, "huruf-jarr", "idafa-definiteness"],
               "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
               "«as in his/their saying» — the kaf of «for instance», a wall: no likening.", "«sözü gibi» — «meselâ» kâfı, duvar: benzetme değil.",
               segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), seg(pr, who, "pron")], punct=punct)
TAALA = tok("تَعَالَى", "taala", "verb", [A], "فِعْلٌ مَاضٍ جَامِدٌ فِي مَعْنَى الدُّعَاءِ — لَا يَجْرِي عَلَى اللهِ إِلَّا مَاضِيًا.", "«exalted is He» — the frozen mazi of praise.", "«teâlâ» — ta'zim mâzîsi.", punct=":")

# ----------- s1 — by the two ends: two kinds (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The istiʿara, regarded by its two ends, is of two kinds: the wifaqiyya and the ʿinadiyya." + R_EN,
 "tr": "İstiâre iki tarafı itibariyle iki kısımdır: vifâkiyye ve inâdiyye." + R_TR},
 "tokens": [
  tok("الِاسْتِعَارَةُ","istiara","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the istiʿara» — the mubtada.", "«istiâre» — mübtedâ."),
  tok("بِاعْتِبَارِ","itibar","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«by the regard of» — jarr, a mudaf.", "«itibariyle» — câr-mecrûr, muzâf.",
      segments=[seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("الطَّرَفَيْنِ","taraf","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«the two ends» — mudaf ilayh; the dual's ya.", "«iki taraf» — muzâfun ileyh; tesniyenin yâsı."),
  tok("قِسْمَانِ","qism","noun",[A, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two kinds» — the khabar; raf' by the alif.", "«iki kısım» — haber; elifle merfû.", punct=":"),
  tok("وِفَاقِيَّةٌ","wifaqiyya","noun",[A, "badal", "ism-mansub"], "بَدَلُ تَفْصِيلٍ مِنْ قِسْمَانِ مَرْفُوعٌ.", "«a wifaqiyya» — badal of detail.", "«vifâkiyye» — tafsîl bedeli."),
  tok("وَعِنَادِيَّةٌ","inadiyya","noun",[A, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and an ʿinadiyya» — joined.", "«ve inâdiyye» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("عِنَادِيَّةٌ","inadiyya","noun")], punct=".")]})

# ----------- s2 — the wifaqiyya (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "The wifaqiyya is that whose two ends CAN be gathered in one thing." + R_EN,
 "tr": "Vifâkiyye, iki tarafının bir şeyde toplanması MÜMKÜN olan istiâredir." + R_TR},
 "tokens": [
  tok("فَالْوِفَاقِيَّةُ","wifaqiyya","noun",[A, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْوِفَاقِيَّةُ مُبْتَدَأٌ.", "«so the wifaqiyya» — the mubtada.", "«vifâkiyye» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْوِفَاقِيَّةُ","wifaqiyya","noun")]),
  tok("مَا","ma-mawsula","pron",[A, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the relative, the khabar.", "«… olan» — ism-i mevsûl, haber."),
  tok("أَمْكَنَ","amkana","verb",[A, "form-iv-verbs", "ism-mawsul"], "فِعْلٌ مَاضٍ — صِلَةُ الْمَوْصُولِ.", "«was possible» — the sila.", "«mümkün oldu» — sıla."),
  tok("اجْتِمَاعُ","ijtimaa","noun",[A, "fail", "masdar", "form-viii-verbs"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ اجْتَمَعَ.", "«the gathering» — the fa'il, a mudaf; the masdar of Form VIII.", "«toplanması» — fâil, muzâf; VIII. bâbın masdarı."),
  tok("طَرَفَيْهَا","taraf","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«its two ends» — mudaf ilayh by the ya; the nun dropped; the ها annexed.", "«iki tarafının» — yâ ile muzâfun ileyh; nûn düşmüş; هَا muzâfun ileyh.",
      segments=[seg("طَرَفَيْ","taraf","noun"), seg("هَا","pron-3fs","pron")]),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("شَيْءٍ","shay","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«a thing» — majrur.", "«bir şey» — mecrûr.", punct=".")]})

# ----------- s3 — the aya 6:122 (as printed)
S.append({"id": "s3", "translation": {
 "en": "As in His saying: «Is he who was dead and We gave him life…» (6:122)",
 "tr": "Kavl-i şerifi gibi: «Ölü iken kendisini dirilttiğimiz kimse…» (6:122)"},
 "majaz": mj(5, "istiara", "mushabaha", {"en": "We gave him life", "tr": "onu dirilttik"}, {"en": "We guided him — misguidance is a death, guidance a life", "tr": "ona hidâyet ettik — dalâlet ölüm, hidâyet hayattır"},
             istiara=ist("tabaiyya", ends="wifaqiyya", seat="maful")),
 "tokens": [
  kaq("كَقَوْلِهِ"), TAALA,
  tok("أَوَمَنْ","man-mawsula","pron",[A, "al-istifham", "ism-mawsul", "mubtada-khabar"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْوَاوُ عَاطِفَةٌ، وَمَنْ مَوْصُولٌ مُبْتَدَأٌ.", "«and is he who» — the question hamza over the waw; مَنْ the relative, a mubtada.", "«… kimse mi» — vâv üzerinde soru hemzesi; مَنْ mevsûl, mübtedâ.",
      segments=[seg("أَ","a-istifham","part"), seg("وَ","wa","conj"), seg("مَنْ","man-mawsula","pron")]),
  tok("كَانَ","kana","verb",[A, "kana-wa-akhawatuha", "ism-mawsul"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ — صِلَةٌ.", "«was» — kana, its ism hidden; the sila.", "«idi» — kâne, ismi gizli; sıla."),
  tok("مَيْتًا","mayyit","noun",[A, "kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«dead» — the khabar of kana.", "«ölü» — kânenin haberi."),
  tok("فَأَحْيَيْنَاهُ","ahya","verb",[A,T,"form-iv-verbs","naqis-verbs","maful-bihi"],
      "الْفَاءُ عَاطِفَةٌ، وَأَحْيَا فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — اسْتِعَارَةٌ تَبَعِيَّةٌ وِفَاقِيَّةٌ: الْإِحْيَاءُ لِلْهِدَايَةِ، وَيَجْتَمِعَانِ فِي شَخْصٍ؛ الْقَرِينَةُ: مَفْعُولُهُ الْحَيُّ الضَّالُّ.",
      "«and We gave him life» — Form IV of the naqis حَيِيَ; نَا the doer, the ه the object. A TABAʿIYYA istiʿara (a VERB is borrowed), WIFAQIYYA: giving life stands for guiding, and both can meet in one person. The clue sits in the OBJECT: the one revived was alive and astray.",
      "«onu dirilttik» — nâkıs حَيِيَ'nin IV. bâbı; نَا fâil, هُ mef'ûl. TEBEİYYE istiâre (FİİL ödünç alınmış), VİFÂKİYYE: diriltmek hidâyet yerine; ikisi bir kişide toplanabilir. Karîne MEF'ÛLdedir: diriltilen zaten diriydi, sapkındı.",
      segments=[seg("فَ","fa","conj"), seg("أَحْيَيْ","ahya","verb"), seg("نَا","pron-1p","pron"), seg("هُ","pron-3ms","pron")], punct="…")]})

# ----------- s4 — the gloss (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "That is: «We guided him» — and guidance and giving life can be gathered in one person." + R_EN,
 "tr": "Yani: «Ona hidâyet ettik» — hidâyet ile diriltme bir kişide toplanabilir." + R_TR},
 "tokens": [
  tok("أَيْ","ay","part",[A, "atf-bayan"], "حَرْفُ تَفْسِيرٍ.", "«that is» — the letter of explanation.", "«yani» — tefsir harfi."),
  tok("هَدَيْنَاهُ","hada","verb",[A, "naqis-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«We guided him» — nun the doer, the ه the object.", "«ona hidâyet ettik» — نَا fâil, هُ mef'ûl.",
      segments=[seg("هَدَيْ","hada","verb"), seg("نَا","pron-1p","pron"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("وَالْهِدَايَةُ","hidaya","noun",[A, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْهِدَايَةُ مُبْتَدَأٌ.", "«and guidance» — a new sentence; the mubtada.", "«ve hidâyet» — isti'nâf; mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْهِدَايَةُ","hidaya","noun")]),
  tok("وَالْإِحْيَاءُ","ihya","noun",[A, "atf-nasaq", "masdar", "form-iv-verbs"], "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ أَحْيَا.", "«and giving life» — joined; the masdar of Form IV.", "«ve diriltme» — matuf; IV. bâbın masdarı.",
      segments=[seg("وَ","wa","conj"), seg("الْإِحْيَاءُ","ihya","noun")]),
  tok("يَجْتَمِعَانِ","ijtamaa","verb",[A, "form-viii-verbs", "afal-khamsa", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — الْجُمْلَةُ خَبَرٌ.", "«are gathered» — one of the five verbs, raf' by the retained nun; the alif its doer; the clause the khabar.", "«toplanır» — ef'âl-i hamseden, nûnun sübûtuyla merfû; elif fâil; cümle haber."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("شَخْصٍ","shakhs","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«a person» — majrur.", "«bir kişi» — mecrûr.", punct=".")]})

# ----------- s5 — the ʿinadiyya (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "And the ʿinadiyya is that whose two ends CANNOT be gathered." + R_EN,
 "tr": "İnâdiyye, iki tarafının toplanması İMKÂNSIZ olan istiâredir." + R_TR},
 "tokens": [
  tok("وَالْعِنَادِيَّةُ","inadiyya","noun",[A, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْعِنَادِيَّةُ مُبْتَدَأٌ.", "«and the ʿinadiyya» — the mubtada.", "«inâdiyye ise» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْعِنَادِيَّةُ","inadiyya","noun")]),
  tok("مَا","ma-mawsula","pron",[A, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the relative, the khabar.", "«… olan» — mevsûl, haber."),
  tok("امْتَنَعَ","imtanaa","verb",[A, "form-viii-verbs", "ism-mawsul"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«was impossible» — the sila; Form VIII.", "«mümteni oldu» — sıla; VIII. bâb."),
  tok("اجْتِمَاعُ","ijtimaa","noun",[A, "fail", "masdar"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the gathering» — the fa'il, a mudaf.", "«toplanması» — fâil, muzâf."),
  tok("طَرَفَيْهَا","taraf","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ بِالْيَاءِ، وَهَا مُضَافٌ إِلَيْهِ.", "«its two ends» — mudaf ilayh by the ya.", "«iki tarafının» — yâ ile muzâfun ileyh.",
      segments=[seg("طَرَفَيْ","taraf","noun"), seg("هَا","pron-3fs","pron")], punct=".")]})

# ----------- s6 — رَأَيْتُ الْعَنْقَاءَ (RESTORED frame + the received example)
S.append({"id": "s6", "translation": {
 "en": "Such as borrowing the name of a non-existent for an existent, when there is no gain in it — as in «I saw the ʿanqa» (for a thing that does not exist)." + R_EN,
 "tr": "Faydası olmadığı için, ma'dûmun adının mevcûd için ödünç alınması gibi — «Anka'yı gördüm» (var olmayan bir şey için)." + R_TR},
 "majaz": mj(7, "istiara", "mushabaha", {"en": "the ʿanqa, the fabled bird", "tr": "Anka kuşu"}, {"en": "a thing that does not exist — a non-existent named for an existent's likeness", "tr": "var olmayan şey — ma'dûmun adı mevcûda"},
             istiara=ist("asliyya", ends="inadiyya")),
 "tokens": [
  tok("كَاسْتِعَارَةِ","istiara","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَاسْتِعَارَةِ مَجْرُورٌ مُضَافٌ.", "«such as the borrowing of» — the kaf of example; a mudaf.", "«ödünç alınması gibi» — meselâ kâfı; muzâf.",
      segments=[seg("كَ","ka","part"), seg("اسْتِعَارَةِ","istiara","noun")]),
  tok("اسْمِ","ism","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ، مُضَافٌ.", "«the name of» — mudaf ilayh and mudaf.", "«adının» — muzâfun ileyh, muzâf."),
  tok("الْمَعْدُومِ","madum","noun",[A, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the non-existent» — mudaf ilayh.", "«ma'dûmun» — muzâfun ileyh."),
  tok("لِلْمَوْجُودِ","mawjud","noun",[A, "huruf-jarr", "ism-maful"], "جَارٌّ وَمَجْرُورٌ.", "«for the existent».", "«mevcûd için».",
      segments=[seg("لِ","li","part"), seg("الْمَوْجُودِ","mawjud","noun")]),
  tok("لِعَدَمِ","adam","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ — لَامُ التَّعْلِيلِ.", "«for the absence of» — the lam of cause; a mudaf.", "«… olmadığı için» — ta'lil lâmı; muzâf.",
      segments=[seg("لِ","li","part"), seg("عَدَمِ","adam","noun")]),
  tok("فَائِدَتِهِ","faida","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its gain» — mudaf ilayh with its pronoun.", "«faydasının» — muzâfun ileyh.",
      segments=[seg("فَائِدَتِ","faida","noun"), seg("هِ","pron-3ms","pron")], punct=":"),
  tok("رَأَيْتُ","raa","verb",[A, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw» — the ta the doer.", "«gördüm» — tâ fâil.",
      segments=[seg("رَأَيْ","raa","verb"), seg("تُ","pron-1s","pron")]),
  tok("الْعَنْقَاءَ","anqa","noun",[A,I,"maful-bihi","ism-mamdud"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْتِعَارَةٌ أَصْلِيَّةٌ عِنَادِيَّةٌ: اسْمُ الْمَعْدُومِ لِلْمَوْجُودِ، وَلَا يَجْتَمِعَانِ.",
      "«the ʿanqa» — the object: an ASLIYYA istiʿara (a genus-noun borrowed), ʿINADIYYA: the non-existent's name for an existent, and the two never meet.",
      "«Anka'yı» — mef'ûl: ASLİYYE istiâre (cins ismi ödünç), İNÂDİYYE: ma'dûmun adı mevcûda; ikisi asla buluşmaz.", punct=".")]})

# ----------- s7 — the tahakkum and the tamlih (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "Of it are the tahakkumiyya and the tamlihiyya: what is used in its opposite or its contrary, for mockery or for pleasantry." + R_EN,
 "tr": "Tehekkümiyye ile temlîhiyye de ondandır: alay yahut lâtife için, zıddında yahut nakîzinde kullanılan." + R_TR},
 "tokens": [
  tok("وَمِنْهَا","min","part",[A, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and of it» — a fronted khabar.", "«ondandır» — mukaddem haber.",
      segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("التَّهَكُّمِيَّةُ","tahakkum","noun",[A, "mubtada-khabar", "ism-mansub"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى التَّهَكُّمِ.", "«the tahakkumiyya» — the delayed mubtada; the nisba of mockery.", "«tehekkümiyye» — muahhar mübtedâ; tehekküm nisbesi."),
  tok("وَالتَّمْلِيحِيَّةُ","tamlih","noun",[A, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ.", "«and the tamlihiyya».", "«ve temlîhiyye».",
      segments=[seg("وَ","wa","conj"), seg("التَّمْلِيحِيَّةُ","tamlih","noun")], punct="،"),
  tok("وَهِيَ","pron-3fs","pron",[A, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«o da» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","pron",[A, "ism-mawsul", "mubtada-khabar"], "مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«… olan» — haber."),
  tok("اسْتُعْمِلَ","istamala","verb",[A, "form-x-verbs", "naib-al-fail", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ — صِلَةٌ.", "«is used» — the passive; the deputy hidden; the sila.", "«kullanılan» — mechûl; nâib gizli; sıla."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("ضِدِّهِ","didd","noun",[A, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its opposite».", "«zıddında».",
      segments=[seg("ضِدِّ","didd","noun"), seg("هِ","pron-3ms","pron")]),
  tok("أَوْ","aw","part",[A, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("نَقِيضِهِ","naqid-contrary","noun",[A, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its contrary» — joined.", "«nakîzinde» — matuf.",
      segments=[seg("نَقِيضِ","naqid-contrary","noun"), seg("هِ","pron-3ms","pron")]),
  tok("لِلتَّهَكُّمِ","tahakkum","noun",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — لَامُ التَّعْلِيلِ.", "«for mockery» — the lam of cause.", "«alay için» — ta'lil lâmı.",
      segments=[seg("لِ","li","part"), seg("التَّهَكُّمِ","tahakkum","noun")]),
  tok("أَوِ","aw","part",[A, "atf-nasaq"], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — its waw takes a kasra before the wasl.", "«yahut» — iki sâkinden kesre."),
  tok("التَّمْلِيحِ","tamlih","noun",[A, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«pleasantry» — joined.", "«lâtife» — matuf.", punct=".")]})

# ----------- s8 — the aya 9:34 (as printed): فَبَشِّرْهُمْ بِعَذَابٍ أَلِيمٍ
S.append({"id": "s8", "translation": {
 "en": "The tahakkum: as in His saying: «So give them tidings of a painful punishment.» (9:34)" + R_EN,
 "tr": "Tehekküm: kavl-i şerifi gibi: «Onları acıklı bir azapla müjdele.» (9:34)" + R_TR},
 "majaz": mj(3, "istiara", "mushabaha", {"en": "give glad tidings", "tr": "müjdele"}, {"en": "warn them — the good news's verb lent to bad news, for mockery", "tr": "onları uyar — müjde fiili kötü habere, alay için"},
             istiara=ist("tabaiyya", ends="inadiyya", seat="majrur")),
 "tokens": [
  tok("فَالتَّهَكُّمُ","tahakkum","noun",[A, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالتَّهَكُّمُ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ — أَيْ مِثَالُهُ.", "«the tahakkum» — a mubtada whose khabar is dropped: «its example is».", "«tehekküm» — haberi düşmüş mübtedâ: «örneği».",
      segments=[seg("فَ","fa","conj"), seg("التَّهَكُّمُ","tahakkum","noun")], punct=":"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("فَبَشِّرْهُمْ","bashshara","verb",[A,T,"form-ii-verbs","imperative-amr","maful-bihi"],
      "الْفَاءُ لِلِاسْتِئْنَافِ، وَبَشِّرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ أَنْتَ، وَهُمْ مَفْعُولٌ بِهِ — اسْتِعَارَةٌ تَبَعِيَّةٌ تَهَكُّمِيَّةٌ: بَشِّرْ بِمَعْنَى أَنْذِرْ؛ وَالْقَرِينَةُ الْمَجْرُورُ: بِعَذَابٍ.",
      "«so give them tidings» — the amr of Form II, its doer «you», هُمْ the object. A TABAʿIYYA istiʿara for MOCKERY: «give glad tidings» stands for «warn». The clue sits in the MAJRUR — punishment is no glad tiding.",
      "«onları müjdele» — II. bâbın emri; fâil «sen», هُمْ mef'ûl. ALAY için TEBEİYYE istiâre: «müjdele» «uyar» yerine. Karîne MECRÛRdadır — azap müjde değildir.",
      segments=[seg("فَ","fa","conj"), seg("بَشِّرْ","bashshara","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("بِعَذَابٍ","adhab","noun",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِبَشِّرْ — هُوَ الْقَرِينَةُ.", "«of a punishment» — attached to the verb; the CLUE.", "«bir azapla» — fiile müteallik; KARÎNE.",
      segments=[seg("بِ","bi","part"), seg("عَذَابٍ","adhab","noun")]),
  tok("أَلِيمٍ","alim-painful","noun",[A, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ — فَعِيلٌ بِمَعْنَى مُؤْلِمٍ.", "«painful» — na't; فَعِيل in the sense of the ism fa'il.", "«acıklı» — na't; ism-i fâil mânâsında فَعِيل.", punct=".")]})

# ----------- s9 — the tamlih (RESTORED frame, received example)
S.append({"id": "s9", "translation": {
 "en": "And the tamlih: as in your saying of a coward, «I saw a lion throwing» — as a pleasantry." + R_EN,
 "tr": "Temlîh: korkak için «Ok atan bir arslan gördüm» demen gibi — lâtife olarak." + R_TR},
 "majaz": mj(3, "istiara", "mushabaha", {"en": "a lion", "tr": "arslan"}, {"en": "a coward — the lion's name lent to his contrary, in jest", "tr": "korkak — arslanın adı nakîzine, şaka yollu"},
             istiara=ist("asliyya", ends="inadiyya")),
 "tokens": [
  tok("وَالتَّمْلِيحُ","tamlih","noun",[A, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالتَّمْلِيحُ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ.", "«and the tamlih» — a mubtada, its khabar dropped.", "«temlîh» — haberi düşmüş mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("التَّمْلِيحُ","tamlih","noun")], punct=":"),
  kaq("كَقَوْلِكَ", "pron-2ms"),
  tok("رَأَيْتُ","raa","verb",[A, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw».", "«gördüm».",
      segments=[seg("رَأَيْ","raa","verb"), seg("تُ","pron-1s","pron")]),
  tok("أَسَدًا","asad","noun",[A,I,"maful-bihi"], "مَفْعُولٌ بِهِ — اسْتِعَارَةٌ أَصْلِيَّةٌ تَمْلِيحِيَّةٌ: الْأَسَدُ لِلْجَبَانِ عَلَى سَبِيلِ الْمُلَاطَفَةِ؛ الْقَرِينَةُ يَرْمِي وَالْمَقَامُ.", "«a lion» — the object: an ASLIYYA istiʿara in JEST — the lion for the coward; the clue: يَرْمِي and the occasion.", "«bir arslan» — mef'ûl: ŞAKA yollu ASLİYYE istiâre — arslan korkak için; karîne: يَرْمِي ve makam."),
  tok("يَرْمِي","rama","verb",[A, "jumla-sifa", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ صِفَةٌ لِأَسَدًا — الْقَرِينَةُ.", "«throwing» — a sifa clause; the clue.", "«ok atan» — sıfat cümlesi; karîne."),
  tok("لِلْجَبَانِ","jaban","noun",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِقَوْلِكَ.", "«of a coward» — attached to «your saying».", "«korkak için» — «demen»e müteallik.",
      segments=[seg("لِ","li","part"), seg("الْجَبَانِ","jaban","noun")]),
  tok("تَمْلِيحًا","tamlih","noun",[A, "maful-lah"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ.", "«as a pleasantry» — the maf'ul li-ajlih.", "«lâtife olarak» — mef'ûlün leh.", punct=".")]})

# ----------- s10 — by the jamiʿ: inside or outside (RESTORED)
S.append({"id": "s10", "translation": {
 "en": "And regarded by the jamiʿ, the istiʿara is either one whose jamiʿ enters the concept of the two ends, or one whose jamiʿ does not." + R_EN,
 "tr": "Câmi itibariyle istiâre, ya câmii iki tarafın mefhûmuna dâhil olan, ya da dâhil olmayandır." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَبِاعْتِبَارِ جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«and by the regard of».", "«ve … itibariyle».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("الْجَامِعِ","jami-link","noun",[A, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ — اسْمُ فَاعِلٍ: مَا يَجْمَعُ الطَّرَفَيْنِ.", "«the jamiʿ» — mudaf ilayh; the ism fa'il: what joins the two ends.", "«câmi» — muzâfun ileyh; ism-i fâil: iki tarafı birleştiren."),
  tok("إِمَّا","imma","part",[A, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("دَاخِلٌ","dakhil","noun",[A, "mubtada-khabar", "ism-fail"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ دَاخِلٌ جَامِعُهَا.", "«(one whose jamiʿ is) inside» — the khabar of a dropped «it».", "«dâhil» — düşmüş «o»nun haberi."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-e»."),
  tok("مَفْهُومِ","mafhum","noun",[A, "huruf-jarr", "idafa-definiteness", "ism-maful"], "مَجْرُورٌ مُضَافٌ — اسْمُ مَفْعُولٍ.", "«the concept of» — majrur, a mudaf; the ism maf'ul.", "«mefhûmuna» — mecrûr, muzâf; ism-i mef'ûl."),
  tok("الطَّرَفَيْنِ","taraf","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ بِالْيَاءِ.", "«the two ends».", "«iki tarafın»."),
  tok("أَوْ","aw","part",[A, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  tok("غَيْرُ","ghayr","noun",[A, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى دَاخِلٌ، مُضَافٌ.", "«not» — joined; a mudaf.", "«gayr» — matuf; muzâf."),
  tok("دَاخِلٍ","dakhil","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«inside».", "«dâhil».", punct=".")]})

# ----------- s11 — the hadith: طَارَ إِلَيْهَا (as printed)
S.append({"id": "s11", "translation": {
 "en": "The first, as in his saying ﷺ: «The best of people is a man holding the rein of his horse; whenever he hears a war-cry he flies to it.» — flying and running share the swift crossing of distance, which is inside both.",
 "tr": "Birincisi, hadîs-i şerifi gibi: «İnsanların en hayırlısı, atının dizginini tutan, ne zaman bir savaş çığlığı duysa oraya uçan adamdır.» — uçmakla koşmanın câmii mesafeyi hızla kat etmektir; ikisine de dâhildir."},
 "majaz": mj(12, "istiara", "mushabaha", {"en": "he flew", "tr": "uçtu"}, {"en": "he ran swiftly — the bird's verb lent to the horseman; the jamiʿ (crossing distance fast) is inside both", "tr": "hızla koştu — kuşun fiili süvariye; câmi (mesafeyi hızla kat etmek) ikisine dâhil"},
             istiara=ist("tabaiyya", jami="dakhil", seat="majrur")),
 "tokens": [
  tok("فَالْأَوَّلُ","awwal","noun",[A, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْأَوَّلُ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ.", "«the first» — a mubtada, its khabar dropped.", "«birincisi» — haberi düşmüş mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْأَوَّلُ","awwal","noun")]),
  kaq("كَقَوْلِهِ", punct=None),
  tok("ﷺ","salla-allahu","part",[A], "جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«peace be upon him» — a parenthetical prayer.", "«sallallâhu aleyhi ve sellem» — mu'terize dua.", punct=":"),
  tok("خَيْرُ","khayr","noun",[A, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the best of» — the mubtada, a mudaf.", "«en hayırlısı» — mübtedâ, muzâf."),
  tok("النَّاسِ","nas","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«people».", "«insanların»."),
  tok("رَجُلٌ","rajul","noun",[A, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a man» — the khabar.", "«bir adam» — haber."),
  tok("مُمْسِكٌ","mumsik","noun",[A, "naat-sifa", "ism-fail", "form-iv-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ أَمْسَكَ.", "«holding» — na't; the ism fa'il of Form IV.", "«tutan» — na't; IV. bâbın ism-i fâili."),
  tok("بِعِنَانِ","inan","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمُمْسِكٌ، مُضَافٌ.", "«the rein of» — attached to the participle; a mudaf.", "«dizginini» — ism-i fâile müteallik; muzâf.",
      segments=[seg("بِ","bi","part"), seg("عِنَانِ","inan","noun")]),
  tok("فَرَسِهِ","faras","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his horse».", "«atının».",
      segments=[seg("فَرَسِ","faras","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("كُلَّمَا","kullama","part",[A, "in-shartiyya"], "ظَرْفٌ لِلتَّكْرَارِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«whenever» — the zarf of repetition with the sense of a shart.", "«ne zaman» — tekrar zarfı, şart mânâsında."),
  tok("سَمِعَ","samia","verb",[A, "in-shartiyya"], "فِعْلٌ مَاضٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ هُوَ.", "«he hears» — the shart verb.", "«duysa» — şart fiili."),
  tok("هَيْعَةً","haya","noun",[A, "maful-bihi"], "مَفْعُولٌ بِهِ — صَوْتُ الْفَزَعِ.", "«a war-cry» — the object.", "«bir savaş çığlığı» — mef'ûl."),
  tok("طَارَ","tara","verb",[A,T,"hollow-verbs","in-shartiyya"],
      "فِعْلٌ مَاضٍ أَجْوَفُ جَوَابُ الشَّرْطِ، وَالْفَاعِلُ هُوَ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الطَّيَرَانُ لِلْعَدْوِ السَّرِيعِ، وَالْجَامِعُ قَطْعُ الْمَسَافَةِ بِسُرْعَةٍ دَاخِلٌ فِيهِمَا؛ الْقَرِينَةُ: الْفَارِسُ لَا يَطِيرُ.",
      "«he flies» — a hollow mazi, the jawab; a TABAʿIYYA istiʿara: flying lent to swift running, and the jamiʿ (crossing distance fast) is INSIDE both meanings. The clue: a horseman does not fly.",
      "«uçar» — ecvef mâzî, cevap; TEBEİYYE istiâre: uçmak hızlı koşmaya; câmi (mesafeyi hızla kat etmek) iki mânâya DÂHİL. Karîne: süvari uçmaz."),
  tok("إِلَيْهَا","ila","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِطَارَ.", "«to it» — attached to the verb.", "«oraya» — fiile müteallik.",
      segments=[seg("إِلَيْ","ila","part"), seg("هَا","pron-3fs","pron")], punct=".")]})

# ----------- s12 — the second: courage in the lion (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "And the second, as courage in the borrowing of the lion for the brave man — courage enters neither the concept of the lion nor that of the man." + R_EN,
 "tr": "İkincisi, arslanın cesur adam için ödünç alınmasındaki şecaat gibi — şecaat ne arslanın ne adamın mefhûmuna dâhildir." + R_TR},
 "tokens": [
  tok("وَالثَّانِي","thani","noun",[A, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«and the second» — a mubtada; a manqus, its damma estimated.", "«ikincisi» — mübtedâ; mankûs, dammesi takdîrî.",
      segments=[seg("وَ","wa","conj"), seg("الثَّانِي","thani","noun")]),
  tok("كَالشَّجَاعَةِ","shajaa","noun",[A, "huruf-jarr", "mubtada-khabar"], "الْكَافُ لِلتَّمْثِيلِ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«as courage» — the kaf of example; the phrase is the khabar.", "«şecaat gibi» — meselâ kâfı; haber.",
      segments=[seg("كَ","ka","part"), seg("الشَّجَاعَةِ","shajaa","noun")]),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("اسْتِعَارَةِ","istiara","noun",[A, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the borrowing of».", "«ödünç alınmasında».",),
  tok("الْأَسَدِ","asad","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«the lion».", "«arslanın»."),
  tok("لِلرَّجُلِ","rajul","noun",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for the man».", "«adam için».",
      segments=[seg("لِ","li","part"), seg("الرَّجُلِ","rajul","noun")]),
  tok("الشُّجَاعِ","shujaa","noun",[A, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«brave» — na't.", "«cesur» — na't.", punct=".")]})

# ----------- s13 — the ʿammiyya (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And it is either ʿammiyya — the commonplace, because its jamiʿ is plain, as in «I saw a lion throwing»…" + R_EN,
 "tr": "Ve ya âmmiyyedir — câmii açık olduğu için herkesin bildiği; «Ok atan bir arslan gördüm» gibi…" + R_TR},
 "majaz": mj(8, "istiara", "mushabaha", {"en": "a lion", "tr": "arslan"}, {"en": "a brave man — the jamiʿ (courage) is plain to everyone", "tr": "cesur adam — câmi (şecaat) herkesçe bilinir"},
             istiara=ist("asliyya", jami="ammiyya")),
 "tokens": [
  tok("وَإِمَّا","imma","part",[A, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«and either».", "«ve ya».",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("عَامِّيَّةٌ","ammiyya","noun",[A, "mubtada-khabar", "ism-mansub"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«ʿammiyya» — the khabar of a dropped «it».", "«âmmiyye» — düşmüş «o»nun haberi."),
  tok("وَهِيَ","pron-3fs","pron",[A, "mubtada-khabar"], "الْوَاوُ لِلْحَالِ أَوِ الِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«o da» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","pron-3fs","pron")]),
  tok("الْمُبْتَذَلَةُ","mubtadhala","noun",[A, "mubtada-khabar", "ism-maful", "form-viii-verbs"], "خَبَرٌ — اسْمُ مَفْعُولٍ مِنِ ابْتَذَلَ: الْمُتَدَاوَلَةُ.", "«the commonplace» — the khabar; the ism maf'ul of Form VIII.", "«mübtezele» — haber; VIII. bâbın ism-i mef'ûlü."),
  tok("لِظُهُورِ","zuhur","noun",[A, "huruf-jarr", "idafa-definiteness", "masdar"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — لَامُ التَّعْلِيلِ.", "«because of the plainness of» — the lam of cause.", "«açıklığından» — ta'lil lâmı.",
      segments=[seg("لِ","li","part"), seg("ظُهُورِ","zuhur","noun")]),
  tok("الْجَامِعِ","jami-link","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«the jamiʿ».", "«câmiin».", punct="،"),
  tok("كَقَوْلِكَ","qawl","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ.", "«as in your saying».", "«demen gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("كَ","pron-2ms","pron")], punct=":"),
  tok("رَأَيْتُ","raa","verb",[A, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw».", "«gördüm».",
      segments=[seg("رَأَيْ","raa","verb"), seg("تُ","pron-1s","pron")]),
  tok("أَسَدًا","asad","noun",[A,I,"maful-bihi"], "مَفْعُولٌ بِهِ — اسْتِعَارَةٌ أَصْلِيَّةٌ عَامِّيَّةٌ.", "«a lion» — the object; an asliyya istiʿara everyone reads.", "«bir arslan» — mef'ûl; herkesin okuduğu asliyye istiâre."),
  tok("يَرْمِي","rama","verb",[A, "jumla-sifa", "naqis-verbs"], "جُمْلَةٌ صِفَةٌ — الْقَرِينَةُ.", "«throwing» — the clue.", "«ok atan» — karîne.", punct="…")]})

# ----------- s14 — the khassiyya (RESTORED)
S.append({"id": "s14", "translation": {
 "en": "…or khassiyya — the strange one, which only the few grasp; and the strangeness may lie in the likeness itself." + R_EN,
 "tr": "…ya da hâssiyyedir — garip olan, ancak seçkinlerin kavradığı; garabet bazen benzerliğin kendisinde olur." + R_TR},
 "tokens": [
  tok("وَإِمَّا","imma","part",[A, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«or».", "«ya da».",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("خَاصِّيَّةٌ","khassiyya","noun",[A, "mubtada-khabar", "ism-mansub"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«khassiyya».", "«hâssiyye»."),
  tok("وَهِيَ","pron-3fs","pron",[A, "mubtada-khabar"], "وَهِيَ مُبْتَدَأٌ.", "«and it is».", "«o da».",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","pron-3fs","pron")]),
  tok("الْغَرِيبَةُ","gharib","noun",[A, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ — فَعِيلٌ صِفَةٌ مُشَبَّهَةٌ.", "«the strange one» — the khabar.", "«garip olan» — haber."),
  tok("الَّتِي","allati","pron",[A, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ لِلْغَرِيبَةِ.", "«which» — the relative, a na't.", "«ki» — mevsûl, na't."),
  tok("لَا","la-nafiya","part",[A, "mudari-marfu"], "حَرْفُ نَفْيٍ.", "«not».", "«-maz»."),
  tok("يُدْرِكُهَا","adraka","verb",[A, "form-iv-verbs", "ism-mawsul", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَهَا مَفْعُولٌ بِهِ — صِلَةٌ.", "«grasp it» — the sila; هَا the object.", "«kavrar» — sıla; هَا mef'ûl.",
      segments=[seg("يُدْرِكُ","adraka","verb"), seg("هَا","pron-3fs","pron")]),
  tok("إِلَّا","illa","part",[A, "istithna"], "أَدَاةُ حَصْرٍ.", "«except».", "«ancak»."),
  tok("الْخَاصَّةُ","khassa","noun",[A, "fail"], "فَاعِلٌ مَرْفُوعٌ — أَهْلُ الذَّوْقِ.", "«the few» — the fa'il: the people of taste.", "«hâssa» — fâil: zevk ehli.", punct="؛"),
  tok("وَقَدْ","qad","part",[A, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("تَكُونُ","kana","verb",[A, "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«is» — the mudari of kana.", "«olur» — kânenin muzârii."),
  tok("الْغَرَابَةُ","gharaba","noun",[A, "kana-wa-akhawatuha"], "اسْمُ تَكُونُ مَرْفُوعٌ.", "«the strangeness» — the ism of kana.", "«garabet» — kânenin ismi."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("نَفْسِ","nafs","noun",[A, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ — الْجَارُّ وَالْمَجْرُورُ خَبَرُ تَكُونُ.", "«the very» — a mudaf; the phrase is kana's khabar.", "«kendisinde» — muzâf; câr-mecrûr kânenin haberi."),
  tok("الشَّبَهِ","shabah","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«the likeness».", "«benzerliğin».", punct=".")]})

# ----------- s15 — Yazid b. Maslama's bayt (as printed)
S.append({"id": "s15", "translation": {
 "en": "As in his saying: «And when its pommel sat wrapped in its rein, • it chewed the bit until the visitor's departure.» — the horse is likened to a man who sits with his knees drawn up, and the strangeness is in the picture itself.",
 "tr": "Onun sözü gibi: «Kaşı dizginine sarılıp oturduğunda, • ziyaretçi dönünceye kadar gemi geveledi.» — at, dizlerini kucaklayıp oturan adama benzetilmiştir; garabet hey'etin kendisindedir."},
 "majaz": mj(2, "istiara", "mushabaha", {"en": "it sat with knees drawn up (ihtiba)", "tr": "ihtibâ ile oturdu"}, {"en": "the horse stood still, rein looped on the pommel — a man's posture lent to a horse; a khassiyya, the picture is strange", "tr": "at, dizgini kaşına takılı hareketsiz durdu — adamın oturuşu ata; hâssiyye, hey'et garip"},
             istiara=ist("tabaiyya", jami="khassiyya", seat="fail")),
 "tokens": [
  kaq("كَقَوْلِهِ"),
  tok("وَإِذَا","idha","part",[A, "idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the conditional zarf.", "«ve … -diğinde» — şart mânâlı zarf.",
      segments=[seg("وَ","wa","conj"), seg("إِذَا","idha","part")]),
  tok("احْتَبَى","ihtaba","verb",[A,T,"form-viii-verbs","naqis-verbs","idha-shartiyya"],
      "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ بَابِ الِافْتِعَالِ، فِعْلُ الشَّرْطِ — اسْتِعَارَةٌ تَبَعِيَّةٌ خَاصِّيَّةٌ: الِاحْتِبَاءُ (جِلْسَةُ الرَّجُلِ) لِوُقُوفِ الْفَرَسِ وَعِنَانُهُ فِي قَرْبُوسِهِ؛ الْقَرِينَةُ الْفَاعِلُ: قَرْبُوسُهُ.",
      "«it sat with knees drawn up» — a naqis Form VIII mazi, the shart verb; a TABAʿIYYA istiʿara of the KHASSIYYA kind: a man's sitting-posture lent to a horse standing with its rein looped on the pommel. The clue is the FAʿIL: a pommel does not sit.",
      "«ihtibâ ile oturdu» — VIII. bâbdan nâkıs mâzî, şart fiili; HÂSSİYYE cinsinden TEBEİYYE istiâre: adamın oturuşu, dizgini kaşına takılı duran ata. Karîne FÂİLdir: kaş oturmaz."),
  tok("قَرْبُوسُهُ","qarbus","noun",[A, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُقَدَّمُ السَّرْجِ.", "«its pommel» — the fa'il: the saddle-bow.", "«kaşı» — fâil: eyer kaşı.",
      segments=[seg("قَرْبُوسُ","qarbus","noun"), seg("هُ","pron-3ms","pron")]),
  tok("بِعِنَانِهِ","inan","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِاحْتَبَى، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in its rein» — attached to the verb.", "«dizginine» — fiile müteallik.",
      segments=[seg("بِ","bi","part"), seg("عِنَانِ","inan","noun"), seg("هِ","pron-3ms","pron")], punct="•"),
  tok("عَلَكَ","alaka","verb",[A, "idha-shartiyya"], "فِعْلٌ مَاضٍ جَوَابُ إِذَا، وَالْفَاعِلُ هُوَ.", "«it chewed» — the jawab of إِذَا.", "«geveledi» — إِذَا'nın cevabı."),
  tok("الشَّكِيمَ","shakim","noun",[A, "maful-bihi"], "مَفْعُولٌ بِهِ — حَدِيدَةُ اللِّجَامِ.", "«the bit» — the object.", "«gemi» — mef'ûl."),
  tok("إِلَى","ila","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ لِلْغَايَةِ.", "«until».", "«-e kadar»."),
  tok("انْصِرَافِ","insiraf","noun",[A, "huruf-jarr", "idafa-definiteness", "masdar", "form-vii-verbs"], "مَجْرُورٌ مُضَافٌ — مَصْدَرُ انْصَرَفَ.", "«the departure of» — the masdar of Form VII.", "«dönüşüne» — VII. bâbın masdarı."),
  tok("الزَّائِرِ","zair","noun",[A, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ — اسْمُ فَاعِلٍ مِنْ زَارَ.", "«the visitor» — the ism fa'il of the hollow زَارَ.", "«ziyaretçinin» — ecvef زَارَ'nin ism-i fâili.", punct=".")]})

# ----------- s16 — strangeness by a turn (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "And the strangeness may come from a turn worked upon a commonplace one." + R_EN,
 "tr": "Garabet bazen âmmiyye üzerinde yapılan bir tasarrufla hâsıl olur." + R_TR},
 "tokens": [
  tok("وَقَدْ","qad","part",[A, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("تَحْصُلُ","hasala","verb",[A, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«comes about».", "«hâsıl olur»."),
  tok("الْغَرَابَةُ","gharaba","noun",[A, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the strangeness» — the fa'il.", "«garabet» — fâil."),
  tok("بِتَصَرُّفٍ","tasarruf","noun",[A, "huruf-jarr", "masdar", "form-v-verbs"], "جَارٌّ وَمَجْرُورٌ — بَاءُ السَّبَبِيَّةِ.", "«by a turn» — the ba of cause.", "«bir tasarrufla» — sebep bâsı.",
      segments=[seg("بِ","bi","part"), seg("تَصَرُّفٍ","tasarruf","noun")]),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْعَامِّيَّةِ","ammiyya","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«the commonplace one».", "«âmmiyyede».", punct=".")]})

# ----------- s17 — Kuthayyir's bayt (as printed)
S.append({"id": "s17", "translation": {
 "en": "As in his saying: «We took hold of the fringes of talk between us, • and the valleys FLOWED with the necks of the camels.» — «flowed» is lent to swift going, a commonplace; ascribing it to the valleys and naming the necks makes it strange.",
 "tr": "Onun sözü gibi: «Aramızda sözün uçlarını tuttuk, • ve dereler develerin boyunlarıyla AKTI.» — «aktı» hızlı gidişe ödünç verilmiş, âmmiyye; derelere isnâdı ve boyunların zikri onu hâssiyye yapar."},
 "majaz": [mj(5, "istiara", "mushabaha", {"en": "flowed", "tr": "aktı"}, {"en": "went swiftly — water's verb lent to the camels' gait; commonplace, then made strange by the turn", "tr": "hızla gitti — suyun fiili develerin gidişine; âmmiyye, tasarrufla hâssiyye"},
              istiara=ist("tabaiyya", jami="khassiyya", seat="majrur")),
           mj(8, "aqli", "makaniyya", {"en": "the valleys flowed", "tr": "dereler aktı"}, {"en": "the camels flowed IN the valleys — the deed ascribed to its place", "tr": "develer derelerDE aktı — fiil mekânına isnâd edilmiş"})],
 "tokens": [
  kaq("كَقَوْلِهِ"),
  tok("أَخَذْنَا","akhadha","verb",[A], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ.", "«we took».", "«tuttuk».",
      segments=[seg("أَخَذْ","akhadha","verb"), seg("نَا","pron-1p","pron")]),
  tok("بِأَطْرَافِ","taraf","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ — أَخَذَ بِهِ: تَمَسَّكَ.", "«hold of the fringes of» — a mudaf.", "«uçlarını» — muzâf.",
      segments=[seg("بِ","bi","part"), seg("أَطْرَافِ","taraf","noun")]),
  tok("الْأَحَادِيثِ","hadith","noun",[A, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ — جَمْعُ حَدِيثٍ عَلَى أَفَاعِيلَ.", "«talk» — mudaf ilayh; the plural on أَفَاعِيل.", "«sözün» — muzâfun ileyh; أَفَاعِيل vezninde cemi."),
  tok("بَيْنَنَا","bayna","noun",[A, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«between us» — a zarf.", "«aramızda» — zarf.",
      segments=[seg("بَيْنَ","bayna","noun"), seg("نَا","pron-1p","pron")], punct="•"),
  tok("وَسَالَتْ","sala","verb",[A,T,"hollow-verbs","majaz-aqli"],
      "الْوَاوُ عَاطِفَةٌ، وَسَالَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، أَجْوَفُ، وَالتَّاءُ لِلتَّأْنِيثِ — اسْتِعَارَةٌ تَبَعِيَّةٌ: السَّيَلَانُ لِلسَّيْرِ السَّرِيعِ، وَقَرِينَتُهَا الْمَجْرُورُ: بِأَعْنَاقِ الْمَطِيِّ؛ وَإِسْنَادُهُ إِلَى الْأَبَاطِحِ مَجَازٌ عَقْلِيٌّ.",
      "«and flowed» — a hollow mazi with the feminine ta; a TABAʿIYYA istiʿara: flowing lent to swift going, its clue the MAJRUR (the camels' necks); and its ascription to the valleys is a majaz ʿaqli — the turn that makes a commonplace istiʿara strange.",
      "«ve aktı» — ecvef mâzî, te'nis tâsı; TEBEİYYE istiâre: akmak hızlı gidişe, karînesi MECRÛR (develerin boyunları); derelere isnâdı aklî mecaz — âmmiyye istiâreyi hâssiyye yapan tasarruf.",
      segments=[seg("وَ","wa","conj"), seg("سَالَتْ","sala","verb")]),
  tok("بِأَعْنَاقِ","unuq","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِسَالَتْ، مُضَافٌ — جَمْعُ عُنُقٍ.", "«with the necks of» — attached to the verb; the plural of عُنُق.", "«boyunlarıyla» — fiile müteallik; عُنُق'un cemi.",
      segments=[seg("بِ","bi","part"), seg("أَعْنَاقِ","unuq","noun")]),
  tok("الْمَطِيِّ","matiyya","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الرَّوَاحِلُ.", "«the camels» — mudaf ilayh.", "«develerin» — muzâfun ileyh."),
  tok("الْأَبَاطِحُ","abtah","noun",[A, "fail", "jam-taksir", "majaz-aqli"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ أَبْطَحَ عَلَى أَفَاعِلَ: مَجَازٌ عَقْلِيٌّ، أُسْنِدَ السَّيَلَانُ إِلَى الْمَكَانِ.", "«the valleys» — the fa'il; the plural on أَفَاعِل: a majaz ʿaqli, the flowing ascribed to the PLACE.", "«dereler» — fâil; أَفَاعِل vezninde cemi: aklî mecaz, akış MEKÂNa isnâd edilmiş.", punct=".")]})

# ----------- s18 — six kinds by the three (RESTORED)
S.append({"id": "s18", "translation": {
 "en": "And regarded by the three — the source, the receiver and the jamiʿ — the istiʿara is of six kinds." + R_EN,
 "tr": "Üçü — müsteârun minh, müsteârun leh ve câmi — itibariyle istiâre altı kısımdır." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَبِاعْتِبَارِ جَارٌّ وَمَجْرُورٌ مُضَافٌ.", "«and by the regard of».", "«ve … itibariyle».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("الثَّلَاثَةِ","thalatha","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْمُسْتَعَارُ مِنْهُ وَالْمُسْتَعَارُ لَهُ وَالْجَامِعُ.", "«the three» — the source, the receiver, the jamiʿ.", "«üçünün» — minh, leh, câmi."),
  tok("سِتَّةُ","sitta","noun",[A, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ (هِيَ)، مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى جَمْعٍ.", "«six» — the khabar of a dropped «it»; a number of 3–10 annexed to a plural.", "«altı» — düşmüş «o»nun haberi; 3-10 arası sayı cemiye muzâf."),
  tok("أَقْسَامٍ","aqsam","noun",[A, "idafa-definiteness", "tamyiz"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِسْمٍ.", "«kinds» — the counted noun in jarr.", "«kısım» — ma'dûd, mecrûr.", punct=".")]})

# ----------- s19 — the first: all sensory — 20:88 (as printed)
S.append({"id": "s19", "translation": {
 "en": "The first: that the three be sensory, as in His saying: «So he brought forth for them a calf — a body with a lowing.» (20:88) — the source, the receiver (the figure made from the ornaments) and the jamiʿ (the shape) are all sensed.",
 "tr": "Birincisi: üçünün hissî olması; kavl-i şerifi gibi: «Onlar için böğüren bir buzağı heykeli çıkardı.» (20:88) — minh, leh (ziynetlerden yapılan heykel) ve câmi (şekil) hepsi hissîdir."},
 "majaz": mj(9, "istiara", "mushabaha", {"en": "a calf", "tr": "buzağı"}, {"en": "the figure cast from the ornaments — the animal's name lent to its likeness; all three sensed", "tr": "ziynetlerden dökülen heykel — hayvanın adı benzerine; üçü de hissî"},
             istiara=ist("asliyya", hissi=["hissi", "hissi", "hissi"])),
 "tokens": [
  tok("الْأَوَّلُ","awwal","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«birincisi» — mübtedâ.", punct=":"),
  tok("أَنْ","an-masdariyya","part",[A, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-an; the clause is the khabar.", "«olması» — masdar harfi; te'vil haber."),
  tok("تَكُونَ","kana","verb",[A, "kana-wa-akhawatuha", "an-masdariyya"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be» — mansub by أَنْ.", "«olması» — أَنْ ile mansûb."),
  tok("الثَّلَاثَةُ","thalatha","noun",[A, "kana-wa-akhawatuha"], "اسْمُ تَكُونَ مَرْفُوعٌ.", "«the three» — the ism of kana.", "«üçü» — kânenin ismi."),
  tok("حِسِّيَّةً","hissi","noun",[A, "kana-wa-akhawatuha", "ism-mansub"], "خَبَرُ تَكُونَ مَنْصُوبٌ.", "«sensory» — the khabar of kana.", "«hissî» — kânenin haberi.", punct="،"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("فَأَخْرَجَ","akhraja","verb",[A, "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأَخْرَجَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ هُوَ.", "«so he brought forth».", "«çıkardı».",
      segments=[seg("فَ","fa","conj"), seg("أَخْرَجَ","akhraja","verb")]),
  tok("لَهُمْ","li","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for them».", "«onlar için».",
      segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("عِجْلًا","ijl","noun",[A,I,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْتِعَارَةٌ أَصْلِيَّةٌ: الْعِجْلُ لِلتِّمْثَالِ الْمَصُوغِ مِنَ الْحُلِيِّ؛ الْقَرِينَةُ: جَسَدًا.", "«a calf» — the object: an ASLIYYA istiʿara, the calf's name for the statue cast from the ornaments; the clue: «a body».", "«bir buzağı» — mef'ûl: ASLİYYE istiâre, buzağının adı ziynetten dökülen heykele; karîne: «bir cesed»."),
  tok("جَسَدًا","jasad","noun",[A, "badal"], "بَدَلٌ مِنْ عِجْلًا (أَوْ نَعْتٌ) مَنْصُوبٌ — الْقَرِينَةُ.", "«a body» — badal of the calf; the clue.", "«bir cesed» — buzağıdan bedel; karîne."),
  tok("لَهُ","li","part",[A, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«having» — a fronted khabar.", "«onun» — mukaddem haber.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("خُوَارٌ","khuwar","noun",[A, "mubtada-khabar", "jumla-sifa"], "مُبْتَدَأٌ مُؤَخَّرٌ، وَالْجُمْلَةُ صِفَةٌ لِجَسَدًا.", "«a lowing» — the delayed mubtada; the clause qualifies the body.", "«böğürme» — muahhar mübtedâ; cümle cesede sıfat.", punct=".")]})

# ----------- s20 — the second: ends sensory, jamiʿ mental — 36:37 (as printed)
S.append({"id": "s20", "translation": {
 "en": "The second: the two ends sensory and the jamiʿ mental, as in His saying: «And a sign for them is the night: We strip the day from it.» (36:37) — skinning a beast and removing light are sensed; the jamiʿ, one thing following upon another, is of the mind.",
 "tr": "İkincisi: iki taraf hissî, câmi aklî; kavl-i şerifi gibi: «Onlara bir delil de gecedir: gündüzü ondan sıyırırız.» (36:37) — hayvanın derisini yüzmek ve ışığı kaldırmak hissî; câmi, bir şeyin diğerine terettübü, aklîdir."},
 "majaz": mj(10, "istiara", "mushabaha", {"en": "We strip (skin)", "tr": "sıyırırız (deri yüzmek)"}, {"en": "We remove the daylight from the night's place — skinning lent to the removal of light; the jamiʿ (one thing following upon another) is mental", "tr": "gündüzün ışığını gecenin yerinden kaldırırız — deri yüzmek ışığın kaldırılmasına; câmi (terettüb) aklî"},
             istiara=ist("tabaiyya", hissi=["hissi", "hissi", "aqli"], seat="maful")),
 "tokens": [
  tok("الثَّانِي","thani","noun",[A, "mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second» — the mubtada; a manqus.", "«ikincisi» — mübtedâ; mankûs.", punct=":"),
  tok("الطَّرَفَانِ","taraf","noun",[A, "mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالْأَلِفِ.", "«the two ends» — a second mubtada, raf' by the alif.", "«iki taraf» — ikinci mübtedâ, elifle merfû."),
  tok("حِسِّيَّانِ","hissi","noun",[A, "mubtada-khabar", "al-muthanna", "ism-mansub"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ، وَالْجُمْلَةُ خَبَرُ الثَّانِي.", "«are sensory» — the khabar by the alif; the clause is the khabar of «the second».", "«hissîdir» — elifle haber; cümle «ikincisi»nin haberi."),
  tok("وَالْجَامِعُ","jami-link","noun",[A, "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْجَامِعُ مُبْتَدَأٌ.", "«and the jamiʿ» — a mubtada.", "«câmi ise» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْجَامِعُ","jami-link","noun")]),
  tok("عَقْلِيٌّ","aqli","noun",[A, "mubtada-khabar", "ism-mansub"], "خَبَرٌ مَرْفُوعٌ.", "«mental» — the khabar.", "«aklîdir» — haber.", punct="،"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("وَآيَةٌ","aya","noun",[A, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَآيَةٌ مُبْتَدَأٌ.", "«and a sign» — the mubtada (indefinite, allowed by its khabar's fronting).", "«bir delil» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("آيَةٌ","aya","noun")]),
  tok("لَهُمُ","li","part",[A, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«for them» — the khabar; the mim takes a damma before the wasl.", "«onlara» — haber; mîm vasıl için damme alır.",
      segments=[seg("لَ","li","part"), seg("هُمُ","pron-3mp","pron")]),
  tok("اللَّيْلُ","layl","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ (أَوْ بَدَلٌ مِنْ آيَةٌ) مَرْفُوعٌ، خَبَرُهُ الْجُمْلَةُ بَعْدَهُ.", "«the night» — a mubtada whose khabar is the clause after it.", "«gece» — haberi sonraki cümle olan mübtedâ."),
  tok("نَسْلَخُ","salakha","verb",[A,T,"mudari-marfu","mubtada-khabar"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ نَحْنُ — اسْتِعَارَةٌ تَبَعِيَّةٌ: السَّلْخُ (كَشْطُ الْجِلْدِ) لِإِزَالَةِ الضَّوْءِ، طَرَفَاهَا حِسِّيَّانِ وَالْجَامِعُ (التَّرَتُّبُ) عَقْلِيٌّ؛ الْقَرِينَةُ: الْمَفْعُولُ النَّهَارَ.",
      "«We strip» — the mudari, its doer «We»; a TABAʿIYYA istiʿara: skinning lent to the removal of light — both sensed, the jamiʿ (one thing following upon another) mental. The clue is the OBJECT: a day is not skinned.",
      "«sıyırırız» — muzâri, fâili «biz»; TEBEİYYE istiâre: deri yüzmek ışığın kaldırılmasına — ikisi hissî, câmi (terettüb) aklî. Karîne MEF'ÛLdür: gündüz yüzülmez."),
  tok("مِنْهُ","min","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِنَسْلَخُ.", "«from it».", "«ondan».",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("النَّهَارَ","nahar","noun",[A, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْقَرِينَةُ.", "«the day» — the object; the clue.", "«gündüzü» — mef'ûl; karîne.", punct=".")]})

# ----------- s21 — the third: ends sensory, jamiʿ mixed — رَأَيْتُ شَمْسًا (RESTORED)
S.append({"id": "s21", "translation": {
 "en": "The third: the two ends sensory and the jamiʿ of mixed kind, as in your saying «I saw a sun» of a person of radiant face and lofty rank — the face's beauty is sensed, the rank's loftiness is of the mind." + R_EN,
 "tr": "Üçüncüsü: iki taraf hissî, câmi karışık; yüzü parlak ve şanı yüce bir kimse için «Bir güneş gördüm» demen gibi — yüz güzelliği hissî, şan yüceliği aklîdir." + R_TR},
 "majaz": mj(7, "istiara", "mushabaha", {"en": "a sun", "tr": "güneş"}, {"en": "a person radiant of face and lofty of rank — the sun's name lent; the jamiʿ is half sensed, half mental", "tr": "yüzü parlak, şanı yüce bir kimse — güneşin adı; câmi yarı hissî yarı aklî"},
             istiara=ist("asliyya", hissi=["hissi", "hissi", "mukhtalif"])),
 "tokens": [
  tok("الثَّالِثُ","thalith","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the third» — the mubtada.", "«üçüncüsü» — mübtedâ.", punct=":"),
  tok("الطَّرَفَانِ","taraf","noun",[A, "mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ ثَانٍ.", "«the two ends».", "«iki taraf»."),
  tok("حِسِّيَّانِ","hissi","noun",[A, "mubtada-khabar", "al-muthanna"], "خَبَرٌ بِالْأَلِفِ.", "«are sensory».", "«hissîdir»."),
  tok("وَالْجَامِعُ","jami-link","noun",[A, "atf-nasaq", "mubtada-khabar"], "مُبْتَدَأٌ.", "«and the jamiʿ».", "«câmi ise».",
      segments=[seg("وَ","wa","conj"), seg("الْجَامِعُ","jami-link","noun")]),
  tok("مُخْتَلِفٌ","mukhtalif","noun",[A, "mubtada-khabar", "ism-fail"], "خَبَرٌ — بَعْضُهُ حِسِّيٌّ وَبَعْضُهُ عَقْلِيٌّ.", "«of mixed kind» — the khabar.", "«muhteliftir» — haber.", punct="،"),
  kaq("كَقَوْلِكَ", "pron-2ms"),
  tok("رَأَيْتُ","raa","verb",[A, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw».", "«gördüm».",
      segments=[seg("رَأَيْ","raa","verb"), seg("تُ","pron-1s","pron")]),
  tok("شَمْسًا","shams","noun",[A,I,"maful-bihi"], "مَفْعُولٌ بِهِ — اسْتِعَارَةٌ أَصْلِيَّةٌ لِإِنْسَانٍ مُشْرِقِ الْوَجْهِ عَالِي الشَّأْنِ؛ الْجَامِعُ مُخْتَلِفٌ: الْإِشْرَاقُ حِسِّيٌّ وَالْعُلُوُّ عَقْلِيٌّ.", "«a sun» — the object: an ASLIYYA istiʿara for a person radiant of face and lofty of rank; the jamiʿ is mixed — radiance sensed, loftiness mental.", "«bir güneş» — mef'ûl: yüzü parlak, şanı yüce bir kimse için ASLİYYE istiâre; câmi muhtelif — parlaklık hissî, yücelik aklî.", punct=".")]})

# ----------- s22 — the fourth: all mental — 36:52 (as printed)
S.append({"id": "s22", "translation": {
 "en": "The fourth: the three mental, as in His saying: «Who has raised us from our sleeping-place?» (36:52) — sleep, death and the hiddenness of action are all of the mind.",
 "tr": "Dördüncüsü: üçü aklî; kavl-i şerifi gibi: «Bizi uyuduğumuz yerden kim kaldırdı?» (36:52) — uyku, ölüm ve fiilin gizliliği, hepsi aklîdir."},
 "majaz": mj(8, "istiara", "mushabaha", {"en": "our sleeping-place", "tr": "uyuduğumuz yer"}, {"en": "our graves — sleep's name lent to death; the jamiʿ (no visible action) is mental, as are both ends", "tr": "kabirlerimiz — uykunun adı ölüme; câmi (fiilin görünmemesi) aklî, iki taraf gibi"},
             istiara=ist("asliyya", hissi=["aqli", "aqli", "aqli"])),
 "tokens": [
  tok("الرَّابِعُ","rabi-fourth","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the fourth» — the mubtada.", "«dördüncüsü» — mübtedâ.", punct=":"),
  tok("الثَّلَاثَةُ","thalatha","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ ثَانٍ.", "«the three».", "«üçü»."),
  tok("عَقْلِيَّةٌ","aqli","noun",[A, "mubtada-khabar", "ism-mansub"], "خَبَرٌ — بِالتَّاءِ لِأَنَّ الثَّلَاثَةَ جَمْعٌ.", "«mental» — the khabar, feminine for the plural.", "«aklîdir» — haber; cemi için müennes.", punct="،"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("مَنْ","man-istifham","pron",[A, "al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ.", "«who» — the interrogative, a mubtada.", "«kim» — soru ismi, mübtedâ."),
  tok("بَعَثَنَا","baatha","verb",[A, "maful-bihi", "mubtada-khabar"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ هُوَ، وَنَا مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرٌ.", "«has raised us» — نَا the object; the clause is the khabar.", "«bizi kaldırdı» — نَا mef'ûl; cümle haber.",
      segments=[seg("بَعَثَ","baatha","verb"), seg("نَا","pron-1p","pron")]),
  tok("مِنْ","min","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("مَرْقَدِنَا","marqad","noun",[A,I,"huruf-jarr","idafa-definiteness","masdar"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ — اسْمُ مَكَانٍ عَلَى مَفْعَلٍ: اسْتِعَارَةٌ أَصْلِيَّةٌ، الرُّقَادُ لِلْمَوْتِ، وَالثَّلَاثَةُ عَقْلِيَّةٌ؛ الْقَرِينَةُ: الْبَعْثُ.", "«our sleeping-place» — majrur; a noun of place on مَفْعَل: an ASLIYYA istiʿara, sleep for death, all three mental; the clue: the raising.", "«uyuduğumuz yer» — mecrûr; مَفْعَل vezninde mekân ismi: ASLİYYE istiâre, uyku ölüm yerine, üçü aklî; karîne: ba's.",
      segments=[seg("مَرْقَدِ","marqad","noun"), seg("نَا","pron-1p","pron")], punct="؟")]})

# ----------- s23 — the fifth: source sensory, the rest mental — 15:94 (as printed)
S.append({"id": "s23", "translation": {
 "en": "The fifth: the source sensory and the other two mental, as in His saying: «So proclaim (shatter forth) what you are commanded.» (15:94) — shattering glass is sensed; proclaiming, and the effect they share, are of the mind.",
 "tr": "Beşincisi: müsteârun minh hissî, diğer ikisi aklî; kavl-i şerifi gibi: «Emrolunduğun şeyi (çatlatırcasına) açıkça bildir.» (15:94) — cam kırmak hissî; tebliğ ve ortak câmi olan tesir aklîdir."},
 "majaz": mj(8, "istiara", "mushabaha", {"en": "shatter, split open", "tr": "çatlat, yar"}, {"en": "proclaim openly — the breaking of glass lent to a proclamation that cannot be held back; the jamiʿ is the effect", "tr": "açıkça bildir — cam kırmak, tutulamayan tebliğe; câmi tesirdir"},
             istiara=ist("tabaiyya", hissi=["hissi", "aqli", "aqli"], seat="majrur")),
 "tokens": [
  tok("الْخَامِسُ","khamis","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the fifth» — the mubtada.", "«beşincisi» — mübtedâ.", punct=":"),
  tok("الْمُسْتَعَارُ","mustaar","noun",[A, "mubtada-khabar", "ism-maful"], "مُبْتَدَأٌ ثَانٍ.", "«the borrowed-from».", "«müsteâr»."),
  tok("مِنْهُ","min","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — نَائِبُ فَاعِلِ اسْمِ الْمَفْعُولِ.", "«from it» — the deputy of the participle.", "«minh» — ism-i mef'ûlün nâibi.",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("حِسِّيٌّ","hissi","noun",[A, "mubtada-khabar"], "خَبَرٌ.", "«is sensory».", "«hissîdir»."),
  tok("وَالْبَاقِيَانِ","baqin","noun",[A, "atf-nasaq", "mubtada-khabar", "al-muthanna", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالْبَاقِيَانِ مُبْتَدَأٌ — مُثَنَّى الْمَنْقُوصِ يَرُدُّ يَاءَهُ.", "«and the remaining two» — a mubtada; the manqus's dual takes its ya back.", "«diğer ikisi» — mübtedâ; mankûsun tesniyesi yâsını geri alır.",
      segments=[seg("وَ","wa","conj"), seg("الْبَاقِيَانِ","baqin","noun")]),
  tok("عَقْلِيَّانِ","aqli","noun",[A, "mubtada-khabar", "al-muthanna"], "خَبَرٌ بِالْأَلِفِ.", "«are mental».", "«aklîdir».", punct="،"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("فَاصْدَعْ","sadaa","verb",[A,T,"imperative-amr"],
      "الْفَاءُ لِلِاسْتِئْنَافِ، وَاصْدَعْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ أَنْتَ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الصَّدْعُ (كَسْرُ الزُّجَاجِ) لِلتَّبْلِيغِ، الْمُسْتَعَارُ مِنْهُ حِسِّيٌّ وَالْآخَرَانِ عَقْلِيَّانِ؛ الْقَرِينَةُ: الْمَجْرُورُ بِمَا تُؤْمَرُ.",
      "«so shatter forth» — the amr, its doer «you»; a TABAʿIYYA istiʿara: splitting (breaking glass) lent to proclaiming — the source sensed, the receiver and the jamiʿ (effect) mental. The clue is the MAJRUR: a command is not a thing one breaks.",
      "«çatlat» — emir, fâili «sen»; TEBEİYYE istiâre: yarmak (cam kırmak) tebliğe — minh hissî, leh ve câmi (tesir) aklî. Karîne MECRÛRdur: emir kırılacak şey değildir.",
      segments=[seg("فَ","fa","conj"), seg("اصْدَعْ","sadaa","verb")]),
  tok("بِمَا","ma-mawsula","pron",[A, "huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا مَوْصُولٌ فِي مَحَلِّ جَرٍّ — الْقَرِينَةُ.", "«with what» — the ba and the relative; the clue.", "«… şeyi» — bâ ve mevsûl; karîne.",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("تُؤْمَرُ","amara-v","verb",[A, "naib-al-fail", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ أَنْتَ — صِلَةٌ، وَالْعَائِدُ مَحْذُوفٌ: تُؤْمَرُ بِهِ.", "«you are commanded» — the passive; the sila, its returning pronoun dropped (بِهِ).", "«emrolunduğun» — mechûl; sıla, âidi düşmüş (بِهِ).", punct=".")]})

# ----------- s24 — the sixth: receiver sensory, the rest mental — 69:11 (as printed)
S.append({"id": "s24", "translation": {
 "en": "The sixth: the receiver sensory and the other two mental, as in His saying: «When the water overflowed (grew insolent), We carried you in the ship.» (69:11) — the water's swelling is sensed; arrogance, and the excess they share, are of the mind.",
 "tr": "Altıncısı: müsteârun leh hissî, diğer ikisi aklî; kavl-i şerifi gibi: «Su taşınca (azınca) sizi gemiye yükledik.» (69:11) — suyun çoğalması hissî; tekebbür ve ortak câmi olan aşırılık aklîdir."},
 "majaz": mj(10, "istiara", "mushabaha", {"en": "grew insolent, overstepped", "tr": "azdı, haddi aştı"}, {"en": "the water rose beyond its bounds — arrogance lent to the flood; the receiver sensed, the source and the jamiʿ (excess) mental", "tr": "su hududunu aştı — kibir tufana; leh hissî, minh ve câmi (aşırılık) aklî"},
             istiara=ist("tabaiyya", hissi=["aqli", "hissi", "aqli"], seat="fail")),
 "tokens": [
  tok("السَّادِسُ","sadis","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the sixth» — the mubtada.", "«altıncısı» — mübtedâ.", punct=":"),
  tok("الْمُسْتَعَارُ","mustaar","noun",[A, "mubtada-khabar", "ism-maful"], "مُبْتَدَأٌ ثَانٍ.", "«the borrowed-for».", "«müsteâr»."),
  tok("لَهُ","li","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — نَائِبُ فَاعِلِ اسْمِ الْمَفْعُولِ.", "«for it».", "«leh».",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("حِسِّيٌّ","hissi","noun",[A, "mubtada-khabar"], "خَبَرٌ.", "«is sensory».", "«hissîdir»."),
  tok("وَالْبَاقِيَانِ","baqin","noun",[A, "atf-nasaq", "mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ.", "«and the remaining two».", "«diğer ikisi».",
      segments=[seg("وَ","wa","conj"), seg("الْبَاقِيَانِ","baqin","noun")]),
  tok("عَقْلِيَّانِ","aqli","noun",[A, "mubtada-khabar", "al-muthanna"], "خَبَرٌ بِالْأَلِفِ.", "«are mental».", "«aklîdir».", punct="،"),
  kaq("كَقَوْلِهِ"), TAALA,
  tok("إِنَّا","inna","part",[A, "inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَنَا اسْمُهَا.", "«indeed We» — inna with its ism.", "«şüphesiz biz» — inne ve ismi.",
      segments=[seg("إِنَّ","inna","part"), seg("نَا","pron-1p","pron")]),
  tok("لَمَّا","lamma","part",[A, "maful-fih"], "ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the zarf of the completed past.", "«-ınca» — hîne mânâsında zarf."),
  tok("طَغَى","tagha","verb",[A,T,"naqis-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، فِعْلُ الشَّرْطِ — اسْتِعَارَةٌ تَبَعِيَّةٌ: الطُّغْيَانُ (التَّكَبُّرُ) لِزِيَادَةِ الْمَاءِ، الْمُسْتَعَارُ لَهُ حِسِّيٌّ وَالْآخَرَانِ عَقْلِيَّانِ؛ الْقَرِينَةُ الْفَاعِلُ: الْمَاءُ.",
      "«overflowed» — a naqis mazi, the shart; a TABAʿIYYA istiʿara: insolence lent to the water's rising — the receiver sensed, the source and the jamiʿ (excess) mental. The clue is the FAʿIL: water is not arrogant.",
      "«azdı» — nâkıs mâzî, şart; TEBEİYYE istiâre: kibir suyun yükselmesine — leh hissî, minh ve câmi (aşırılık) aklî. Karîne FÂİLdir: su kibirlenmez."),
  tok("الْمَاءُ","ma-water","noun",[A, "fail"], "فَاعِلٌ مَرْفُوعٌ — الْقَرِينَةُ.", "«the water» — the fa'il; the clue.", "«su» — fâil; karîne."),
  tok("حَمَلْنَاكُمْ","hamala","verb",[A, "maful-bihi"], "فِعْلٌ مَاضٍ جَوَابُ لَمَّا، وَنَا فَاعِلٌ، وَكُمْ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرُ إِنَّ.", "«We carried you» — the jawab of لَمَّا; the clause is inna's khabar.", "«sizi yükledik» — لَمَّا'nın cevabı; cümle innenin haberi.",
      segments=[seg("حَمَلْ","hamala","verb"), seg("نَا","pron-1p","pron"), seg("كُمْ","pron-2mp","pron")]),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْجَارِيَةِ","jariya","noun",[A, "huruf-jarr", "ism-fail"], "مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ جَرَى: السَّفِينَةُ.", "«the ship» — the ism fa'il of «to run»: the running one.", "«gemiye» — جَرَى'nın ism-i fâili: akıp giden.", punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # the chapter's terms
 "wifaqiyya": g("وِفَاقِيَّة", "و ف ق", "noun", "wifaqiyya — the istiʿara whose two ends can meet in one thing", "vifâkıyye — iki tarafı bir şeyde birleşebilen istiâre", 6),
 "inadiyya": g("عِنَادِيَّة", "ع ن د", "noun", "ʿinadiyya — the istiʿara whose two ends cannot meet in one thing", "inâdiyye — iki tarafı bir şeyde birleşemeyen istiâre", 6),
 "ijtimaa": g("اِجْتِمَاع", "ج م ع", "noun", "coming together, combining (masdar of اِجْتَمَعَ)", "birleşme, bir araya gelme (اِجْتَمَعَ'nin masdarı)", 3),
 "ijtamaa": g("اِجْتَمَعَ", "ج م ع", "verb", "to come together, combine (Form VIII)", "birleşmek, bir araya gelmek (VIII. bâb)", 3, form="VIII"),
 "imtanaa": g("اِمْتَنَعَ", "م ن ع", "verb", "to be impossible; to refuse (Form VIII)", "mümteni olmak, imkânsız olmak; kaçınmak (VIII. bâb)", 3, form="VIII"),
 "ihya": g("إِحْيَاء", "ح ي ي", "noun", "giving life (masdar of أَحْيَا)", "diriltme (أَحْيَا'nın masdarı)", 3),
 "ahya": find_gloss("ahya"),
 "amkana": find_gloss("amkana"),
 "mayyit": find_gloss("mayyit"),
 "shakhs": find_gloss("shakhs"),
 "madum": find_gloss("madum"),
 "qism": find_gloss("qism"),
 "didd": g("ضِدّ", "ض د د", "noun", "contrary, opposite", "zıt, karşıt", 3, plural="أَضْدَاد"),
 "naqid-contrary": g("نَقِيض", "ن ق ض", "noun", "contradictory (the negation of a thing)", "nakîz, çelişik (bir şeyin olumsuzu)", 5),
 "bashshara": g("بَشَّرَ", "ب ش ر", "verb", "to give glad tidings (Form II)", "müjdelemek (II. bâb)", 3, form="II"),
 "adhab": find_gloss("adhab"),
 "alim-painful": g("أَلِيم", "أ ل م", "noun", "painful", "elîm, acı veren", 3),
 "jami-link": g("جَامِع", "ج م ع", "noun", "the jamiʿ — the feature the two ends share (ism faʿil of جَمَعَ)", "câmi — iki tarafın ortak vasfı (جَمَعَ'nin ism-i fâili)", 5),
 "dakhil": g("دَاخِل", "د خ ل", "noun", "entering, included in (ism faʿil of دَخَلَ)", "dâhil, içine giren (دَخَلَ'nin ism-i fâili)", 3),
 "mafhum": g("مَفْهُوم", "ف ه م", "noun", "what is understood, the concept (ism mafʿul of فَهِمَ)", "mefhûm, anlaşılan mânâ (فَهِمَ'nin ism-i mef'ûlü)", 5),
 "salla-allahu": g("ﷺ", None, "part", "ṣallā llāhu ʿalayhi wa-sallam — the prayer written after the Prophet's name", "sallallâhu aleyhi ve sellem — Peygamber'in adından sonra yazılan dua", 1),
 "hadith": find_gloss("hadith"),
 "samia": find_gloss("samia"),
 "mumsik": g("مُمْسِك", "م س ك", "noun", "holding, gripping (ism faʿil of أَمْسَكَ)", "tutan (أَمْسَكَ'nin ism-i fâili)", 4),
 "inan": g("عِنَان", "ع ن ن", "noun", "rein (of a horse)", "dizgin", 4, plural="أَعِنَّة"),
 "faras": g("فَرَس", "ف ر س", "noun", "horse", "at", 2, plural="أَفْرَاس"),
 "haya": g("هَيْعَة", "ه ي ع", "noun", "a cry of alarm, a call to arms", "hey'a; savaş çığlığı, imdat nidası", 6),
 "tara": g("طَارَ", "ط ي ر", "verb", "to fly (hollow-ya: طَارَ يَطِيرُ)", "uçmak (ecvef-yâî: طَارَ يَطِيرُ)", 2, form="I"),
 "shajaa": g("شَجَاعَة", "ش ج ع", "noun", "bravery", "şecaat, cesaret", 3),
 "ammiyya": g("عَامِّيَّة", "ع م م", "noun", "ʿammiyya — the common istiʿara, whose jamiʿ is plain", "âmmiyye — câmii açık olan, herkesin anladığı istiâre", 6),
 "mubtadhala": g("مُبْتَذَلَة", "ب ذ ل", "noun", "hackneyed, worn by use (ism mafʿul of اِبْتَذَلَ)", "mübtezel, kullanıla kullanıla eskimiş (اِبْتَذَلَ'nin ism-i mef'ûlü)", 5),
 "khassiyya": g("خَاصِّيَّة", "خ ص ص", "noun", "khassiyya — the rare istiʿara, grasped by the elite alone", "hâssiyye — yalnız havâssın kavradığı garip istiâre", 6),
 "khassa": find_gloss("khassa"),
 "ihtaba": g("اِحْتَبَى", "ح ب و", "verb", "to sit wrapped, knees drawn up and bound (the ihtibaʾ) (Form VIII, naqis)", "ihtibâ etmek — dizlerini karnına çekip sarınarak oturmak (VIII. bâb, nâkıs)", 6, form="VIII"),
 "qarbus": g("قَرْبُوس", "ق ر ب س", "noun", "saddle-bow", "eyer kaşı", 6, plural="قَرَابِيس"),
 "alaka": g("عَلَكَ", "ع ل ك", "verb", "to chew, champ (the bit)", "çiğnemek, (gemi) gevelemek", 5, form="I"),
 "shakim": g("شَكِيم", "ش ك م", "noun", "the bit of a bridle", "gem (dizginin ağızdaki demiri)", 6),
 "insiraf": g("اِنْصِرَاف", "ص ر ف", "noun", "departing, leaving (masdar of اِنْصَرَفَ)", "ayrılıp gitme (اِنْصَرَفَ'nin masdarı)", 4),
 "zair": g("زَائِر", "ز و ر", "noun", "visitor (ism faʿil of زَارَ)", "ziyaretçi (زَارَ'nin ism-i fâili)", 3, plural="زُوَّار"),
 "tasarruf": find_gloss("tasarruf"),
 "sala": g("سَالَ", "س ي ل", "verb", "to flow (hollow-ya: سَالَ يَسِيلُ)", "akmak (ecvef-yâî: سَالَ يَسِيلُ)", 3, form="I"),
 "unuq": g("عُنُق", "ع ن ق", "noun", "neck", "boyun", 2, plural="أَعْنَاق"),
 "matiyya": g("مَطِيَّة", "م ط و", "noun", "riding-beast", "binek hayvanı", 5, plural="مَطِيّ / مَطَايَا"),
 "abtah": g("أَبْطَح", "ب ط ح", "noun", "a wide torrent-bed of sand and pebbles", "ebtah — çakıllı, kumlu geniş sel yatağı", 6, plural="أَبَاطِح"),
 "sitta": find_gloss("sitta"),
 "ijl": g("عِجْل", "ع ج ل", "noun", "calf", "buzağı", 2, plural="عُجُول"),
 "jasad": g("جَسَد", "ج س د", "noun", "body", "ceset, beden", 2, plural="أَجْسَاد"),
 "khuwar": g("خُوَار", "خ و ر", "noun", "lowing (of cattle)", "böğürme (sığır sesi)", 5),
 "salakha": g("سَلَخَ", "س ل خ", "verb", "to strip off, flay; to draw (the day) out of (the night)", "soymak, sıyırmak; (geceden gündüzü) çekip çıkarmak", 4, form="I"),
 "thalith": g("ثَالِث", "ث ل ث", "noun", "third", "üçüncü", 2),
 "rabi-fourth": g("رَابِع", "ر ب ع", "noun", "fourth", "dördüncü", 2),
 "marqad": g("مَرْقَد", "ر ق د", "noun", "resting-place, bed; grave (ism makan of رَقَدَ)", "yatılan yer, yatak; kabir (رَقَدَ'nin ism-i mekânı)", 4, plural="مَرَاقِد"),
 "khamis": g("خَامِس", "خ م س", "noun", "fifth", "beşinci", 2),
 "baqin": find_gloss("baqin"),
 "sadaa": g("صَدَعَ", "ص د ع", "verb", "to split, cleave; صَدَعَ بِالْأَمْرِ: to declare it openly", "yarmak; صَدَعَ بِالْأَمْرِ: açıkça bildirmek", 4, form="I"),
 "sadis": g("سَادِس", "س د س", "noun", "sixth", "altıncı", 2),
 "tagha": g("طَغَى", "ط غ ي", "verb", "to overflow, exceed its bounds (naqis-ya: طَغَى يَطْغَى)", "taşmak, haddini aşmak (nâkıs-yâî: طَغَى يَطْغَى)", 4, form="I"),
 "jariya": g("جَارِيَة", "ج ر ي", "noun", "the ship (that runs on the water); a girl", "gemi (suda akıp giden); câriye, kız", 3, plural="جَوَارٍ"),
 # the particles no package had
 "ay": g("أَيْ", None, "part", "that is, i.e. — the particle of explanation", "yani — tefsir harfi", 2),
 "a-istifham": g("أَ", None, "part", "the hamza of the question (أَ)", "istifham hemzesi (أَ)", 1),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/52.json").write_text(
    json.dumps({"chapter": 52, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 52 for c in man["chapters"]):
    man["chapters"].append({"n": 52, "title": TITLE52})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.52.0"
ADD_EN = (" Chapter 52 (lines ~3570-3640, sahifa 124-126) carries the istiʿara by its two ends, by the jamiʿ and by "
          "the sensory or mental nature of the three: the ayat 6:122 (s3), 9:34 (s8), 20:88 (s19), 36:37 (s20), "
          "36:52 (s22), 15:94 (s23), 69:11 (s24), the hadith of s11, the bayt of Yazid b. Maslama (s15), the bayt "
          "of Kuthayyir (s17) and رَأَيْتُ أَسَدًا يَرْمِي / رَأَيْتُ شَمْسًا (s9, s13, s21) are Arabic as the source prints "
          "it, inside restored frames; 6:122 is printed مَيْتًا (Hafs) and kept so. s1-s2, s4-s7, s9-s10, s12-s14, "
          "s16, s18 and the frames of the examples are RESTORATIONS, not quotations: the source carries those steps "
          "only in Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's "
          "register; each is marked «restored» in its translation. Every istiʿara carries an authored `majaz` frame "
          "with an `istiara` object — the lafz (asliyya / tabaʿiyya) and the qarina's seat, which the surface "
          "settles, and the ends, the jamiʿ and the sensory/mental kind, which the chapter names — that the engine "
          "is graded against.")
ADD_TR = (" Elli ikinci bâb (satır ~3570-3640, sahife 124-126) istiâreyi iki taraf, câmi ve üçünün hissî yahut aklî "
          "oluşu itibariyle taşır: 6:122 (s3), 9:34 (s8), 20:88 (s19), 36:37 (s20), 36:52 (s22), 15:94 (s23), 69:11 "
          "(s24) âyetleri, s11 hadisi, Yezîd b. Mesleme'nin beyti (s15), Küseyyir'in beyti (s17) ve رَأَيْتُ أَسَدًا "
          "يَرْمِي / رَأَيْتُ شَمْسًا (s9, s13, s21), geri yazılmış çerçeveler içinde kaynağın bastığı Arapçadır; 6:122 "
          "مَيْتًا (Hafs) basılmıştır ve öyle korunmuştur. s1-s2, s4-s7, s9-s10, s12-s14, s16, s18 ile örneklerin "
          "çerçeveleri ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; "
          "Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye "
          "işaretlidir. Her istiâre, motorun sınandığı müellif eliyle yazılmış bir `majaz` çerçevesi ve `istiara` "
          "nesnesi taşır — yüzeyin belirlediği lafız (asliyye / tebeiyye) ve karînenin yeri; bâbın adlandırdığı "
          "taraflar, câmi ve hissî/aklî nev'i.")
if "3570-3640" not in man["attribution"]["en"]:
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
put("ijtamaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِجْتَمَع", "جْتَمِع", "اِجْتَمِع", "اِجْتِمَاع", "مُجْتَمِع", "مُجْتَمَع", "اُجْتُمِعَ", "يُجْتَمَعُ",
                           "فِي الْمَتْنِ: يَجْتَمِعَانِ — مُثَنَّى الْغَائِبِ، مَرْفُوعٌ بِثُبُوتِ النُّونِ."))
put("imtanaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِمْتَنَع", "مْتَنِع", "اِمْتَنِع", "اِمْتِنَاع", "مُمْتَنِع", None, None, None,
                           "لَازِمٌ: امْتَنَعَ الشَّيْءُ — صَارَ مُمْتَنِعًا؛ لَا مَفْعُولَ لَهُ."))
put("bashshara", _sg.derived(_sg.B2, _sg.W2, "ُ", "بَشَّر", "بَشِّر", "بَشِّر", "تَبْشِير", "مُبَشِّر", "مُبَشَّر", "بُشِّرَ", "يُبَشَّرُ",
                             "فِي الْآيَةِ: فَبَشِّرْهُمْ — أَمْرٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْهَاءُ مَفْعُولٌ."))
put("tara", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "طَار", "طِر", "طِير", "طِر", "طِير", "طِر", "طَيَرَان", "طَائِر", None, None, None,
                        "أَجْوَفُ يَائِيٌّ مِنْ بَابِ ضَرَبَ: طَارَ يَطِيرُ، طِرْتُ، لَمْ يَطِرْ."))
put("sala", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "سَال", "سِل", "سِيل", "سِل", "سِيل", "سِل", "سَيَلَان", "سَائِل", None, None, None,
                        "أَجْوَفُ يَائِيٌّ مِنْ بَابِ ضَرَبَ: سَالَ يَسِيلُ، سَالَتْ بِتَاءِ التَّأْنِيثِ السَّاكِنَةِ."))
put("salakha", _sg.sound1("fataha", "سَلَخ", "سْلَخ", "اِسْلَخ", "سَلْخ", "سَالِخ", "مَسْلُوخ", "سُلِخَ", "يُسْلَخُ",
                          "مِنْ بَابِ فَتَحَ (وَيُقَالُ يَسْلُخُ): نَسْلَخُ مِنْهُ النَّهَارَ."))
put("sadaa", _sg.sound1("fataha", "صَدَع", "صْدَع", "اِصْدَع", "صَدْع", "صَادِع", "مَصْدُوع", "صُدِعَ", "يُصْدَعُ",
                        "فِي الْآيَةِ: فَاصْدَعْ بِمَا تُؤْمَرُ — أَمْرٌ مَبْنِيٌّ عَلَى السُّكُونِ."))
put("alaka", _sg.sound1("nasara", "عَلَك", "عْلُك", "اُعْلُك", "عَلْك", "عَالِك", "مَعْلُوك", "عُلِكَ", "يُعْلَكُ",
                        "مِنْ بَابِ نَصَرَ (وَيُقَالُ يَعْلِكُ): عَلَكَ الشَّكِيمَ."))
put("tagha", _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ", "y", "طَغَ", "طْغ", "a", "اِطْغ", "طُغْيَان", "طَاغٍ (الطَّاغِي)", None, None, None,
                        "نَاقِصٌ يَائِيٌّ مِنْ بَابِ فَتَحَ: طَغَى يَطْغَى؛ طَغَى الْمَاءُ — تَجَاوَزَ حَدَّهُ."))
put("ihtaba", _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِحْتَبَ", "حْتَب", "i", "اِحْتَب", "اِحْتِبَاء", "مُحْتَبٍ (الْمُحْتَبِي)", None, None, None,
                                "نَاقِصٌ عَلَى افْتَعَلَ: اِحْتَبَى يَحْتَبِي؛ الْأَلِفُ فِي الْمَاضِي مَقْصُورَةٌ (احْتَبَى)."))
put("amkana", find_morph("amkana"))
put("ahya", find_morph("ahya"))
put("samia", find_morph("samia"))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the notes
GR = ROOT / "content/grammar"
NOTE_A = {
 "id": "aqsam-al-istiara",
 "title": {"ar": "أَقْسَامُ الِاسْتِعَارَةِ — الطَّرَفَانِ وَالْجَامِعُ وَالْحِسِّيُّ وَالْعَقْلِيُّ", "en": "The kinds of istiʿara — the two ends, the jamiʿ, the sensory and the mental", "tr": "İstiârenin kısımları — iki taraf, câmi, hissî ve aklî"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الاستعارة باعتبار الطرفين والجامع"],
 "question": {
  "en": ["Can the two ends MEET in one thing? Life and guidance meet in one man (WIFAQIYYA); the non-existent and the existent cannot (ʿINADIYYA). An ʿinadiyya used for the contrary in mockery is TAHAKKUM, in jest TAMLIH.",
         "Is the JAMIʿ inside the meaning of both ends (a man gripping his rein, flying to the alarm — speed is in both) or outside them (bravery is neither the lion nor the man)? Is it plain to all (ʿAMMIYYA) or seen by the elite alone (KHASSIYYA)?",
         "Which of the three — the bihi, the mushabbah, the jamiʿ — is SENSED and which is REASONED? Six kinds: all three sensory, both ends sensory with a mental jamiʿ, both ends sensory with a mixed jamiʿ, all three mental, the bihi alone sensory, the mushabbah alone sensory."],
  "tr": ["İki taraf bir şeyde BİRLEŞEBİLİR mi? Hayat ve hidayet bir adamda birleşir (VİFÂKIYYE); ma'dûm ile mevcut birleşemez (İNÂDİYYE). Zıddı için alayla kullanılan inâdiyye TEHEKKÜM, şakayla TEMLÎHtir.",
         "CÂMİ iki tarafın mefhûmuna dâhil mi (dizginini tutan, nidaya uçan adam — sürat ikisinde de var) hâriç mi (şecaat ne arslandır ne adam)? Herkese açık mı (ÂMMİYYE) yalnız havâssa mı (HÂSSİYYE)?",
         "Üçten — bih, müşebbeh, câmi — hangisi HİSSÎ hangisi AKLÎ? Altı kısım: üçü hissî; iki taraf hissî câmi aklî; iki taraf hissî câmi muhtelif; üçü aklî; yalnız bih hissî; yalnız müşebbeh hissî."]},
 "plain": {
  "en": "The istiʿara is sorted three ways. By its ENDS: wifaqiyya when they can meet in one thing, ʿinadiyya when they cannot (tahakkum and tamlih are ʿinadiyya used for the contrary). By its JAMIʿ: inside or outside the two meanings, common or rare. By what is SENSED: six kinds, from all three sensory to all three mental.",
  "tr": "İstiâre üç yoldan ayrılır. TARAFLARINA göre: bir şeyde birleşebilirlerse vifâkıyye, birleşemezlerse inâdiyye (tehekküm ve temlîh, zıddı için kullanılan inâdiyyedir). CÂMİİNE göre: iki mefhûma dâhil yahut hâriç, âmm yahut hâs. HİSSE göre: üçü hissîden üçü aklîye altı kısım."},
 "explanation": {
  "en": "BY THE TWO ENDS the istiʿara is WIFAQIYYA when its mustaʿar minhu and mustaʿar lahu can be gathered in one thing — أَوَمَنْ كَانَ مَيْتًا فَأَحْيَيْنَاهُ (6:122), that is «we guided him»: life and guidance meet in one person — and ʿINADIYYA when they cannot: the name of the non-existent lent to the existent for its uselessness, رَأَيْتُ الْعَنْقَاءَ. Of the ʿinadiyya are the TAHAKKUMIYYA and the TAMLIHIYYA — a word used for its contrary or its contradictory, for mockery or for jest: فَبَشِّرْهُمْ بِعَذَابٍ أَلِيمٍ (9:34), «give them glad tidings» for «warn them», is tahakkum; رَأَيْتُ أَسَدًا يَرْمِي said of a coward is tamlih. BY THE JAMIʿ it is either INSIDE the meaning of the two ends — the Prophet's ﷺ خَيْرُ النَّاسِ رَجُلٌ مُمْسِكٌ بِعِنَانِ فَرَسِهِ كُلَّمَا سَمِعَ هَيْعَةً طَارَ إِلَيْهَا, where «flew» is lent for «hastened» and the jamiʿ, crossing distance at speed, sits in both flying and hastening — or OUTSIDE them, as bravery in the lion lent to the brave man: bravery is neither the beast nor the man. Again it is ʿAMMIYYA, the hackneyed, because its jamiʿ is plain (رَأَيْتُ أَسَدًا يَرْمِي), or KHASSIYYA, the rare, grasped by the elite alone; the rarity may lie in the likeness itself — Yazid b. Maslama's وَإِذَا احْتَبَى قَرْبُوسُهُ بِعِنَانِهِ • عَلَكَ الشَّكِيمَ إِلَى انْصِرَافِ الزَّائِرِ, the horse standing so still that the saddle-bow «sits wrapped» in the rein — or come from a turn given to a common one, as Kuthayyir's وَسَالَتْ بِأَعْنَاقِ الْمَطِيِّ الْأَبَاطِحُ: «went» becomes «flowed», the beasts' necks become the seat of the flowing, and the torrent-beds are made the doers. BY THE THREE — bihi, mushabbah, jamiʿ — six kinds: all three SENSORY, فَأَخْرَجَ لَهُمْ عِجْلًا جَسَدًا لَهُ خُوَارٌ (20:88), the calf for the golden body; both ends sensory, the jamiʿ MENTAL, وَآيَةٌ لَهُمُ اللَّيْلُ نَسْلَخُ مِنْهُ النَّهَارَ (36:37), flaying for drawing away, the jamiʿ the following of one thing upon another; both ends sensory, the jamiʿ MIXED, رَأَيْتُ شَمْسًا for a bright and beautiful face, the roundness sensed and the beauty reasoned; all three MENTAL, مَنْ بَعَثَنَا مِنْ مَرْقَدِنَا (36:52), death for sleep; the bihi alone sensory, فَاصْدَعْ بِمَا تُؤْمَرُ (15:94), splitting for declaring; the mushabbah alone sensory, إِنَّا لَمَّا طَغَى الْمَاءُ (69:11), overstepping for overflowing. WHAT THE ENGINE CLAIMS: the lafz (asliyya where the lent word is a noun of a kind, tabaʿiyya where it is a verb, a derived noun or a particle) and the qarina's seat it reads from the surface and the ḍabṭ; the ends, the jamiʿ and the six kinds are the chapter's naming, stored on the authored frame and shown, and where a stock likeness settles them (the lion, the sun, death for sleep) the engine offers its shortlist.",
  "tr": "İKİ TARAFA GÖRE istiâre, müsteârun minh ile müsteârun leh bir şeyde toplanabiliyorsa VİFÂKIYYEdir — أَوَمَنْ كَانَ مَيْتًا فَأَحْيَيْنَاهُ (6:122), yani «ona hidayet ettik»: hayat ile hidayet bir şahısta birleşir — toplanamıyorsa İNÂDİYYE: faydasızlığı için ma'dûmun adının mevcuda ödünç verilmesi, رَأَيْتُ الْعَنْقَاءَ. İnâdiyyeden TEHEKKÜMİYYE ve TEMLÎHİYYE — bir kelimenin alay yahut şaka için zıddında yahut nakîzinde kullanılması: فَبَشِّرْهُمْ بِعَذَابٍ أَلِيمٍ (9:34), «uyar» yerine «müjdele», tehekkümdür; korkak için رَأَيْتُ أَسَدًا يَرْمِي temlîhtir. CÂMİE GÖRE ya iki tarafın mefhûmuna DÂHİLdir — Peygamber'in ﷺ خَيْرُ النَّاسِ رَجُلٌ مُمْسِكٌ بِعِنَانِ فَرَسِهِ كُلَّمَا سَمِعَ هَيْعَةً طَارَ إِلَيْهَا sözü: «uçtu», «koştu» için ödünç; câmi, mesafeyi süratle kat etmek, hem uçmada hem koşmada var — ya HÂRİÇ: cesur adama ödünç verilen arslandaki şecaat gibi; şecaat ne hayvandır ne adam. Yine ya ÂMMİYYEdir, mübtezel, câmii açık olduğu için (رَأَيْتُ أَسَدًا يَرْمِي), ya HÂSSİYYE, garip, yalnız havâssın kavradığı; garâbet benzeyişin kendisinde olabilir — Yezîd b. Mesleme'nin وَإِذَا احْتَبَى قَرْبُوسُهُ بِعِنَانِهِ • عَلَكَ الشَّكِيمَ إِلَى انْصِرَافِ الزَّائِرِ beyti: at öyle durur ki eyer kaşı dizginle «ihtibâ eder» — yahut âmm bir istiâreye verilen bir tasarruftan gelebilir, Küseyyir'in وَسَالَتْ بِأَعْنَاقِ الْمَطِيِّ الْأَبَاطِحُ beyti gibi: «gitti» «aktı» olur, hayvanların boyunları akmanın mahalli kılınır, sel yatakları fâil yapılır. ÜÇÜNE GÖRE — bih, müşebbeh, câmi — altı kısım: üçü HİSSÎ, فَأَخْرَجَ لَهُمْ عِجْلًا جَسَدًا لَهُ خُوَارٌ (20:88), altın gövde için buzağı; iki taraf hissî, câmi AKLÎ, وَآيَةٌ لَهُمُ اللَّيْلُ نَسْلَخُ مِنْهُ النَّهَارَ (36:37), çekip almak için soymak, câmi bir şeyin diğerini takibi; iki taraf hissî, câmi MUHTELİF, parlak güzel yüz için رَأَيْتُ شَمْسًا, yuvarlaklık hissî, güzellik aklî; üçü AKLÎ, مَنْ بَعَثَنَا مِنْ مَرْقَدِنَا (36:52), uyku için ölüm; yalnız bih hissî, فَاصْدَعْ بِمَا تُؤْمَرُ (15:94), açıkça bildirmek için yarmak; yalnız müşebbeh hissî, إِنَّا لَمَّا طَغَى الْمَاءُ (69:11), taşmak için haddi aşmak. MOTORUN İDDİASI: lafzı (ödünç kelime cins ismiyse asliyye; fiil, müştak isim yahut harfse tebeiyye) ve karînenin yerini yüzeyden ve zabttan okur; taraflar, câmi ve altı kısım bâbın adlandırmasıdır, müellif çerçevesinde saklanır ve gösterilir; yerleşik bir benzetme onları belirliyorsa (arslan, güneş, uyku için ölüm) motor kısa listesini sunar."},
 "examples": [
  {"ar": "أَوَمَنْ كَانَ مَيْتًا فَأَحْيَيْنَاهُ", "en": "wifaqiyya: life and guidance meet in one man.", "tr": "vifâkıyye: hayat ile hidayet bir adamda birleşir.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "فَبَشِّرْهُمْ بِعَذَابٍ أَلِيمٍ", "en": "ʿinadiyya by tahakkum: «glad tidings» of a painful torment.", "tr": "tehekküm ile inâdiyye: elîm azabın «müjdesi».", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "كُلَّمَا سَمِعَ هَيْعَةً طَارَ إِلَيْهَا", "en": "the jamiʿ inside both ends: speed is in flying and in hastening.", "tr": "câmi iki tarafa dâhil: sürat hem uçmada hem koşmada.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "وَآيَةٌ لَهُمُ اللَّيْلُ نَسْلَخُ مِنْهُ النَّهَارَ", "en": "both ends sensory, the jamiʿ mental.", "tr": "iki taraf hissî, câmi aklî.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"}],
 "commonMistakes": [
  {"wrong": "«فَبَشِّرْهُمْ بِعَذَابٍ: müjde hakikattir, azap da bir haberdir»",
   "right": "«Tehekkümdür: müjde, zıddı olan uyarma için ödünç alınmıştır; karîne بِعَذَابٍ»",
   "why": {"en": "Glad tidings and torment cannot meet in one thing: the istiʿara is ʿinadiyya, and the contrary is used for mockery. The majrur is the clue.", "tr": "Müjde ile azap bir şeyde birleşemez: istiâre inâdiyyedir, zıt alay için kullanılmıştır. Mecrûr karînedir."}},
  {"wrong": "«رَأَيْتُ شَمْسًا: üçü de hissîdir, güneş de yüz de görülür»",
   "right": "«İki taraf hissî, câmi MUHTELİFtir: yuvarlaklık ve parlaklık görülür, güzellik akılla kavranır»",
   "why": {"en": "The count is over the three, not the two ends. When the jamiʿ has a sensed part and a reasoned part, it is mixed — the third kind.", "tr": "Sayım iki taraf üzerinden değil üçü üzerindendir. Câminin hissî ve aklî parçası varsa muhteliftir — üçüncü kısım."}}],
 "relatedNotes": ["istiara", "arkan-al-istiara", "istiara-tabaiyya", "majaz-mursal", "haqiqa-majaz", "aqsam-al-tashbih", "wajh-al-shabah", "tashbih"]}
NOTE_T = {
 "id": "istiara-tabaiyya",
 "title": {"ar": "الِاسْتِعَارَةُ الْأَصْلِيَّةُ وَالتَّبَعِيَّةُ — اللَّفْظُ وَمَقَرُّ الْقَرِينَةِ", "en": "The asliyya and the tabaʿiyya — the word's class and where the clue sits", "tr": "Asliyye ve tebeiyye istiâre — lafzın cinsi ve karînenin yeri"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الاستعارة باعتبار اللفظ: أصلية وتبعية"],
 "question": {
  "en": ["What CLASS is the lent word? A noun of a kind (أَسَد، شَمْس، عِجْل) makes the istiʿara ASLIYYA. A verb (طَارَ، نَسْلَخُ، طَغَى), a derived noun (نَاطِقَة) or a particle (the lam) makes it TABAʿIYYA — the likening runs first in the verb's MEANING (the masdar) and the word follows.",
         "Where does the CLUE sit? In an asliyya, a describing clause or a perception verb (يَرْمِي). In a tabaʿiyya, one of the verb's own seats: its faʿil (طَغَى الْمَاءُ), its mafʿul (نَسْلَخُ … النَّهَارَ), its second mafʿul, or its majrur (بَشِّرْهُمْ بِعَذَابٍ)."],
  "tr": ["Ödünç kelime hangi CİNSTEN? Cins ismi (أَسَد، شَمْس، عِجْل) istiâreyi ASLİYYE yapar. Fiil (طَارَ، نَسْلَخُ، طَغَى), müştak isim (نَاطِقَة) yahut harf (lâm) TEBEİYYE yapar — benzetme önce fiilin MÂNÂSINDA (masdarda) yürür, kelime ona tâbi olur.",
         "KARÎNE nerede oturur? Asliyyede bir vasıf cümlesi yahut idrak fiili (يَرْمِي). Tebeiyyede fiilin kendi yerlerinden biri: fâili (طَغَى الْمَاءُ), mef'ûlü (نَسْلَخُ … النَّهَارَ), ikinci mef'ûlü yahut mecrûru (بَشِّرْهُمْ بِعَذَابٍ)."]},
 "plain": {
  "en": "By the word's class the istiʿara is ASLIYYA when the lent word is a noun of a kind, TABAʿIYYA when it is a verb, a derived noun or a particle: there the likening is first in the meaning and the word follows it. The engine reads the class off the word and names the seat the clue sits in.",
  "tr": "Lafzın cinsine göre istiâre, ödünç kelime cins ismiyse ASLİYYE; fiil, müştak isim yahut harfse TEBEİYYEdir: orada benzetme önce mânâdadır, kelime ona tâbidir. Motor cinsi kelimeden okur ve karînenin oturduğu yeri adlandırır."},
 "explanation": {
  "en": "The Talkhis divides the istiʿara BY THE WORD: ASLIYYA when the lent word is a noun of a kind (اسْمُ جِنْسٍ) — أَسَد for the brave man, شَمْس for the face, عِجْل for the golden body, مَرْقَد for the grave; TABAʿIYYA otherwise — in the verb, the derived noun and the particle. The reason is that a verb or a derived noun is not itself the likened thing: the likening is made first in its MEANING — in the masdar, or in the meaning of the particle — and the word FOLLOWS (يَتْبَعُ) it. So in طَارَ إِلَيْهَا (the hadith) the hastening is likened to flying first, and «flew» is lent on the back of that; in نَسْلَخُ مِنْهُ النَّهَارَ (36:37) the drawing-away is likened to flaying; in فَاصْدَعْ بِمَا تُؤْمَرُ (15:94) declaring is likened to splitting; in طَغَى الْمَاءُ (69:11) overflowing is likened to overstepping; in فَأَحْيَيْنَاهُ (6:122) guiding is likened to giving life; in بَشِّرْهُمْ (9:34) warning is likened, in mockery, to bringing glad tidings. The chapter that follows names the CLUE's seat for the tabaʿiyya: the clue can only be one of the verb's own dependents — the faʿil (طَغَى الْمَاءُ: water cannot overstep), the mafʿul (نَسْلَخُ … النَّهَارَ: day cannot be flayed), the second mafʿul, or the majrur (بَشِّرْهُمْ بِعَذَابٍ: torment is no glad tiding; احْتَبَى قَرْبُوسُهُ: a saddle-bow does not sit). WHAT THE ENGINE CLAIMS: it settles asliyya / tabaʿiyya from the lent word's class in the ḍabṭ (a verb or a derived noun or a particle → tabaʿiyya; a noun of a kind → asliyya), and it names the seat of the clue from DabtEngine's own reading of the verb's faʿil, mafʿul, second mafʿul and jarr-majrur — so a frame that says «seat: majrur» is graded against the parse, not against a stored list. It does not decide which meaning was likened to which: the murad on the authored frame carries that.",
  "tr": "Telhîs istiâreyi LAFZA GÖRE böler: ödünç kelime cins ismi (اسْمُ جِنْسٍ) ise ASLİYYE — cesur adam için أَسَد, yüz için شَمْس, altın gövde için عِجْل, kabir için مَرْقَد; aksi hâlde TEBEİYYE — fiilde, müştak isimde ve harfte. Sebebi şudur: fiil yahut müştak isim benzetilen şeyin kendisi değildir; benzetme önce MÂNÂSINDA — masdarda, yahut harfin mânâsında — yapılır ve kelime ona TÂBİ olur (يَتْبَعُ). Böylece طَارَ إِلَيْهَا (hadis) sözünde önce koşmak uçmaya benzetilir, «uçtu» onun sırtında ödünç verilir; نَسْلَخُ مِنْهُ النَّهَارَ'da (36:37) çekip almak soymaya; فَاصْدَعْ بِمَا تُؤْمَرُ'da (15:94) açıkça bildirmek yarmaya; طَغَى الْمَاءُ'da (69:11) taşmak haddi aşmaya; فَأَحْيَيْنَاهُ'da (6:122) hidayet diriltmeye; بَشِّرْهُمْ'da (9:34) uyarmak, alayla, müjdelemeye. Sonraki bâb tebeiyyede KARÎNEnin yerini adlandırır: karîne ancak fiilin kendi bağımlılarından biri olabilir — fâil (طَغَى الْمَاءُ: su haddi aşmaz), mef'ûl (نَسْلَخُ … النَّهَارَ: gündüz soyulmaz), ikinci mef'ûl yahut mecrûr (بَشِّرْهُمْ بِعَذَابٍ: azap müjde değildir; احْتَبَى قَرْبُوسُهُ: eyer kaşı oturmaz). MOTORUN İDDİASI: asliyye / tebeiyyeyi ödünç kelimenin zabttaki cinsinden belirler (fiil, müştak isim yahut harf → tebeiyye; cins ismi → asliyye) ve karînenin yerini DabtEngine'in fiilin fâilini, mef'ûlünü, ikinci mef'ûlünü ve câr-mecrûrunu okuyuşundan adlandırır — yani «yer: mecrûr» diyen çerçeve saklı listeye değil i'râba karşı sınanır. Hangi mânânın hangisine benzetildiğine karar vermez: müellif çerçevesindeki murâd onu taşır."},
 "examples": [
  {"ar": "كُلَّمَا سَمِعَ هَيْعَةً طَارَ إِلَيْهَا", "en": "tabaʿiyya in the verb: hastening likened to flying; the clue is the majrur إِلَيْهَا.", "tr": "fiilde tebeiyye: koşmak uçmaya benzetilmiş; karîne mecrûr إِلَيْهَا.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "إِنَّا لَمَّا طَغَى الْمَاءُ", "en": "tabaʿiyya; the clue sits in the faʿil.", "tr": "tebeiyye; karîne fâilde.", "sourceStory": "talkhis-al-miftah", "sentence": "s24"},
  {"ar": "فَأَخْرَجَ لَهُمْ عِجْلًا جَسَدًا", "en": "asliyya: the lent word is a noun of a kind.", "tr": "asliyye: ödünç kelime cins ismi.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"},
  {"ar": "فَبَشِّرْهُمْ بِعَذَابٍ أَلِيمٍ", "en": "tabaʿiyya; the clue sits in the majrur.", "tr": "tebeiyye; karîne mecrûrda.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"}],
 "commonMistakes": [
  {"wrong": "«طَغَى الْمَاءُ: su, haddi aşan bir insana benzetilmiş, istiâre suda (asliyye)»",
   "right": "«Fiildedir: taşmak haddi aşmaya benzetilmiş, طَغَى ödünç — tebeiyye; الْمَاءُ karînedir, ödünç değil»",
   "why": {"en": "In a tabaʿiyya the lent word is the verb and its dependent is the clue. Reading the faʿil as the lent word turns the clue into the istiʿara and loses both.", "tr": "Tebeiyyede ödünç kelime fiildir, bağımlısı karînedir. Fâili ödünç kelime saymak karîneyi istiâre yapar ve ikisini de kaybeder."}},
  {"wrong": "«نَسْلَخُ مِنْهُ النَّهَارَ: istiâre النَّهَارَ kelimesindedir»",
   "right": "«نَسْلَخُ'dadır: çekip almak soymaya benzetilmiş; النَّهَارَ mef'ûl-karînedir»",
   "why": {"en": "The day is meant literally; what is not literal is the flaying. The clue is the mafʿul that cannot be flayed.", "tr": "Gündüz hakikatiyle kastedilmiştir; hakikî olmayan soymaktır. Karîne, soyulamayan mef'ûldür."}}],
 "relatedNotes": ["aqsam-al-istiara", "istiara", "arkan-al-istiara", "majaz-mursal", "qarinat-al-majaz", "fail", "maful-bihi", "huruf-jarr", "masdar"]}
for n in (NOTE_A, NOTE_T):
    (GR / f"{n['id']}.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")
for nid, add in (("istiara", ["aqsam-al-istiara", "istiara-tabaiyya"]), ("arkan-al-istiara", ["aqsam-al-istiara", "istiara-tabaiyya"]),
                 ("majaz-mursal", ["aqsam-al-istiara"]), ("qarinat-al-majaz", ["istiara-tabaiyya"])):
    fp = GR / f"{nid}.json"
    if not fp.exists(): continue
    w = json.loads(fp.read_text(encoding="utf-8"))
    ch = False
    for a in add:
        if a not in w.get("relatedNotes", []): w.setdefault("relatedNotes", []).append(a); ch = True
    if ch: fp.write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch52:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + 10 built, 3 copied; notes aqsam-al-istiara, istiara-tabaiyya;",
      "majaz frames:", sum(len(x.get("majaz", [])) for x in S))
