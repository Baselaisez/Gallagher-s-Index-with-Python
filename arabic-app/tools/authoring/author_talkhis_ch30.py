# -*- coding: utf-8 -*-
"""Author chapter 30 of talkhis-al-miftah — بَابُ الْخَبَرِ الْمُسْتَعْمَلِ فِي مَعْنَى الْإِنْشَاءِ.

Sahifa 77 (lines ~2216-2222): the mirror of the five insha babs — the KHABAR
form standing in for insha, for exactly four reasons the source lists:

  {1} تَفَاؤُل — the good omen: وَفَّقَكَ اللهُ لِلتَّقْوَى (speak it as done);
  {2} إِظْهَارُ الْحِرْصِ — showing eagerness for the occurrence:
      رَزَقَنِيَ اللهُ لِقَاءَكَ — and the source's own tanbih: a mazi du'a
      from an eloquent speaker is OPEN TO BOTH of these kinds;
  {3} fleeing the AMR's shape — the slave to his master:
      يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً (no isti'la is possible upward);
  {4} pressing the addressee toward the request — تَأْتِينِي غَدًا: a hearer
      who will not let the speaker stand a liar is carried to the deed.

ATTRIBUTION: every sentence is the source's own worked example verbatim
(lines ~2216-2222, sahifa 77), Ottoman orthography normalized to standard:
plain-alif hamza seats, اِلَىَّ → إِلَيَّ, رَزَقَنِىَ → رَزَقَنِيَ,
لِقَائَكَ → لِقَاءَكَ (the hamza written on the line after the alif),
تَأْتِينِى → تَأْتِينِي — all recorded normalizations.

Grammar this chapter teaches:
  • note 134 `khabar-fi-mana-al-insha` — the four reasons, the mazi-du'a
    two-ways ruling, and the tanbih (most of the five babs' insha parallels
    the ikhbari the same way).
  • engine work: the khabarDua frame (mazi + 1st/2nd enclitic + the jalala
    as fa'il — read off row.enc, never off letter tails); the idafa pass's
    two refusals (a pronoun-closed head, a raf'-marked ilayh); the twin-cell
    shortlist (تَأْتِي is «she — or you» in every paradigm of the language).
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PKG = ROOT / "content/samples/talkhis-al-miftah"
sys.path.insert(0, str(ROOT / "tools/authoring"))
import sarf_gen as _sg
import re
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
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
def copy_verb(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))["verbs"]
    return d[key]
S = []

TITLE30 = {"ar": "بَابُ الْخَبَرِ الْمُسْتَعْمَلِ فِي مَعْنَى الْإِنْشَاءِ",
           "en": "Khabar Worn for Insha",
           "tr": "İnşâ Mânâsında Kullanılan Haber"}

# ------------------------------------------------- s1 — tafa'ul: the good omen
S.append({"id": "s1", "translation": {
 "en": "May Allah grant you success toward taqwa! (the FIRST reason — TAFA'UL: the du'a spoken as already done, for the good omen in it.)",
 "tr": "Allah seni takvâya muvaffak kılsın! (BİRİNCİ sebep — TEFE'ÜL: hayra yormak için, olmuş gibi söylenen duâ.)"},
 "tokens": [
  tok("وَفَّقَكَ","waffaqa","verb",["khabar-fi-mana-al-insha"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "«He granted you success» — a mazi, mabni on the fatha; the kaf is the attached pronoun, in the position of nasb: the maf'ul bihi. The PAST tense is the whole point: the asker speaks the wish as a thing already done.",
      "«seni muvaffak kıldı» — fetha üzere mebnî mâzî; kâf, bitişik zamir, mahallen mansub: mef'ûlün bih. Bütün mesele MÂZÎ oluşundadır: isteyen, dileğini olmuş bir şey gibi söylüyor.",
      segments=[seg("وَفَّقَ","waffaqa","verb"), seg("كَ","pron-2ms","pron")]),
  tok("اللهُ","allah","propn",["khabar-fi-mana-al-insha"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Allah» — the Name, the fa'il, marfu' by the plain damma: the One asked, seated as the doer of a deed already ascribed.",
      "«Allah» — lafza-i celâl, fâil; açık dammeyle merfû: kendisinden istenen, olmuş sayılan fiilin fâili makamında."),
  tok("لِلتَّقْوَى","taqwa","noun",["khabar-fi-mana-al-insha"],
      "اللَّامُ حَرْفُ جَرٍّ، وَالتَّقْوَى اسْمٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُتَعَلِّقٌ بِوَفَّقَ.",
      "«toward taqwa» — the lam is a jarr letter (its alif of ال swallowed); taqwa is majrur by a kasra ESTIMATED on the alif, and the phrase hangs on the verb.",
      "«takvâya» — lâm cer harfidir (ال'ın elifi yutulmuş); takvâ, elif üzerinde TAKDÎRÎ kesrayla mecrûr; öbek fiile taalluk eder.",
      punct="!", segments=[seg("لِ","li","part"), seg("التَّقْوَى","taqwa","noun")])],
 "jumal": [
  J("وَفَّقَكَ اللهُ لِلتَّقْوَى",
    "جُمْلَةٌ خَبَرِيَّةٌ لَفْظًا إِنْشَائِيَّةٌ مَعْنًى — دُعَاءٌ — لَا مَحَلَّ لَهَا.",
    "KHABAR in letter, INSHA in meaning: a du'a wearing a report's dress, no mahall.",
    "Lafzan HABER, mânen İNŞÂ: haber kılığında bir duâ; mahalli yok."),
  J("وَفَّقَكَ اللهُ",
    "وَجْهُ التَّفَاؤُلِ — الدُّعَاءُ بِصِيغَةِ الْمَاضِي تَيَمُّنًا بِوُقُوعِهِ.",
    "THE TAFA'UL WAJH: the first of the four reasons — the mazi makes an omen of the wish, speaking it as if fallen due.",
    "TEFE'ÜL VECHİ: dört sebebin ilki — mâzî, dileği uğura çevirir; onu vâki olmuş gibi söyler.")]})

# --------------------------------------- s2 — izhar al-hirs: shown eagerness
S.append({"id": "s2", "translation": {
 "en": "May Allah bless me with meeting you! (the SECOND reason — showing EAGERNESS for the thing's occurrence; and the source rules a mazi du'a open to both readings.)",
 "tr": "Allah beni sana kavuşmakla rızıklandırsın! (İKİNCİ sebep — vukuuna DÜŞKÜNLÜĞÜ göstermek; kaynak, mâzî duâyı iki okumaya da açık sayar.)"},
 "tokens": [
  tok("رَزَقَنِيَ","razaqa","verb",["khabar-fi-mana-al-insha"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ.",
      "«He provided me» — a mazi on the fatha; the nun is the GUARDING nun and the speaker's ya the FIRST object (رَزَقَ gives two). The ya wears a fatha only because the Name's wasl-alif follows.",
      "«beni rızıklandırdı» — fetha üzere mebnî mâzî; nûn VİKAYE nûnu, mütekellim yâsı BİRİNCİ mef'ûl (رَزَقَ iki mef'ûl alır). Yâ'nın fethası yalnız ardından gelen vasıl elifi içindir.",
      segments=[seg("رَزَقَ","razaqa","verb"), seg("نِي","pron-1s","pron")]),
  tok("اللهُ","allah","propn",["khabar-fi-mana-al-insha"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Allah» — the Name, the fa'il, marfu' by the plain damma.",
      "«Allah» — lafza-i celâl, fâil; açık dammeyle merfû."),
  tok("لِقَاءَكَ","liqa","noun",["khabar-fi-mana-al-insha"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«meeting you» — the SECOND object, mansub by the plain fatha; the kaf is the mudaf ilayh. A mamdud noun: its hamza is a turned radical (ل ق ي), so the tanwin it would carry elsewhere is lawful — here the idafa takes it instead.",
      "«sana kavuşmayı» — İKİNCİ mef'ûl; açık fethayla mansub; kâf muzâfun ileyhtir. Memdud isim: hemzesi dönüşmüş aslî harftir (ل ق ي); başka yerde alacağı tenvin câizdir — burada onu izâfet almıştır.",
      punct="!", segments=[seg("لِقَاءَ","liqa","noun"), seg("كَ","pron-2ms","pron")])],
 "jumal": [
  J("رَزَقَنِيَ اللهُ لِقَاءَكَ",
    "جُمْلَةٌ خَبَرِيَّةٌ لَفْظًا إِنْشَائِيَّةٌ مَعْنًى — دُعَاءٌ — لَا مَحَلَّ لَهَا.",
    "Again khabar in letter, du'a in force — no mahall.",
    "Yine lafzan haber, kuvvetçe duâ — mahalsiz."),
  J("رَزَقَنِيَ اللهُ",
    "وَجْهُ إِظْهَارِ الْحِرْصِ — وَالْمَاضِي فِي الدُّعَاءِ يَحْتَمِلُ الْوَجْهَيْنِ.",
    "THE HIRS WAJH: eagerness for the meeting shown by reporting it granted — and the source's tanbih: a mazi du'a from the eloquent is OPEN TO BOTH this and the tafa'ul.",
    "HIRS VECHİ: kavuşma, verilmiş diye haber verilerek düşkünlük gösterilir — ve kaynağın tenbihi: beliğin mâzî duâsı buna da tefe'üle de AÇIKTIR.")]})

# ------------------------------- s3 — fleeing the amr's shape (slave → master)
S.append({"id": "s3", "translation": {
 "en": "My master looks at me for a moment. (the THIRD reason — the slave cannot COMMAND his master, so the request flees the amr's shape into a report.)",
 "tr": "Efendim bana bir an bakar. (ÜÇÜNCÜ sebep — köle efendisine EMREDEMEZ; istek, emir kalıbından kaçıp haber kılığına girer.)"},
 "tokens": [
  tok("يَنْظُرُ","nazara","verb",["khabar-fi-mana-al-insha"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«he looks» — a mudari, marfu' by the plain damma. No amr stands anywhere: isti'la toward one's master is impossible, so the asking hides in the report.",
      "«bakar» — açık dammeyle merfû muzâri. Ortada hiçbir emir yok: efendiye karşı isti'lâ imkânsızdır; istek, haberin içine gizlenir."),
  tok("الْمَوْلَى","mawla","noun",["khabar-fi-mana-al-insha"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«the master» — the fa'il, marfu' by a damma ESTIMATED on the maqsur alif.",
      "«efendi» — fâil; maksûr elif üzerinde TAKDÎRÎ dammeyle merfû."),
  tok("إِلَيَّ","ila","part",["khabar-fi-mana-al-insha"],
      "إِلَى حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ، مُتَعَلِّقٌ بِيَنْظُرُ.",
      "«at me» — ila with the speaker's ya (the maqsura turned to ya before the pronoun), hanging on the verb.",
      "«bana» — إِلَى ile mütekellim yâsı (zamirden önce elif-i maksûre yâya döner); fiile taalluk eder.",
      segments=[seg("إِلَى","ila","part"), seg("يَ","pron-1s","pron")]),
  tok("سَاعَةً","saa","noun",["khabar-fi-mana-al-insha"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — مَفْعُولٌ فِيهِ.",
      "«for a moment» — a zarf of time, mansub by the plain fatha: the maf'ul fih.",
      "«bir an» — zaman zarfı; açık fethayla mansub: mef'ûlün fîh.",
      punct=".")],
 "jumal": [
  J("يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً",
    "جُمْلَةٌ خَبَرِيَّةٌ لَفْظًا طَلَبِيَّةٌ مَعْنًى — لَا مَحَلَّ لَهَا.",
    "A report in letter, a plea in force — no mahall.",
    "Lafzan haber, kuvvetçe niyaz — mahalsiz."),
  J("يَنْظُرُ الْمَوْلَى",
    "وَجْهُ التَّحَرُّزِ عَنْ صُورَةِ الْأَمْرِ.",
    "THE THIRD REASON: shunning the amr's very shape — the low may not command the high, so the wish is worded as what the master simply does.",
    "ÜÇÜNCÜ SEBEP: emrin sûretinden sakınmak — aşağıdaki yukarıdakine buyuramaz; dilek, efendinin zaten yaptığı bir şey gibi söylenir.")]})

# ---------------------- s4 — carrying the addressee: the liar no one permits
S.append({"id": "s4", "translation": {
 "en": "You come to me tomorrow. (the FOURTH reason — the addressee who will not let the speaker stand a liar is CARRIED to the deed by the report itself.)",
 "tr": "Yarın bana gelirsin. (DÖRDÜNCÜ sebep — konuşanı yalancı durumuna düşürmek istemeyen muhatap, haberin kendisiyle işe SEVK edilir.)"},
 "tokens": [
  tok("تَأْتِينِي","ata","verb",["khabar-fi-mana-al-insha"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«you come to me» — a mudari, its damma estimated on the naqis ya; the doer is the concealed «YOU» (the same letters spell «she comes» — the frame settles the person); the nun guards, and the speaker's ya is the maf'ul.",
      "«bana gelirsin» — muzâri; dammesi nâkıs yâ üzerinde takdîrî; fâili gizli «SEN» (aynı harfler «o gelir» diye de okunur — şahsı bağlam belirler); nûn vikaye, mütekellim yâsı mef'ûl.",
      segments=[seg("تَأْتِي","ata","verb"), seg("نِي","pron-1s","pron")]),
  tok("غَدًا","ghad","noun",["khabar-fi-mana-al-insha"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — مَفْعُولٌ فِيهِ.",
      "«tomorrow» — a zarf of time, mansub by the plain fatha (the fathatan written before its seat-alif).",
      "«yarın» — zaman zarfı; açık fethayla mansub (fethateyn, dayanak elifinden önce yazılır).",
      punct=".")],
 "jumal": [
  J("تَأْتِينِي غَدًا",
    "جُمْلَةٌ خَبَرِيَّةٌ لَفْظًا إِنْشَائِيَّةٌ مَعْنًى — لَا مَحَلَّ لَهَا.",
    "The fourth dress: a flat report of tomorrow's visit — that IS the request.",
    "Dördüncü kılık: yarınki gelişin düz haberi — istek TAM DA budur."),
  J("تَأْتِينِي غَدًا",
    "وَجْهُ حَمْلِ الْمُخَاطَبِ عَلَى الْمَطْلُوبِ.",
    "THE FOURTH REASON: the hearer is pressed to the deed — refusing now would make the speaker a liar, and a hearer who will not allow that must come.",
    "DÖRDÜNCÜ SEBEP: muhatap işe zorlanır — şimdi kaçınmak konuşanı yalancı çıkarır; buna râzı olmayan muhatap gelmek zorundadır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "waffaqa": g("وَفَّقَ", "و ف ق", "verb", "to grant success (to)", "muvaffak kılmak", 4, form="II"),
 "razaqa": g("رَزَقَ", "ر ز ق", "verb", "to provide for, bestow upon", "rızıklandırmak", 3, form="I"),
 "liqa": g("لِقَاء", "ل ق ي", "noun", "meeting, encounter", "kavuşma, buluşma", 4),
 "ghad": g("غَد", "غ د و", "noun", "tomorrow, the morrow", "yarın", 2),
 "nazara": copy_gloss("wasiyyat-abi-hanifa", "nazara"),
 "mawla": copy_gloss("bad-al-amali", "mawla"),
 "saa": copy_gloss("wasiyyat-abi-hanifa-samti", "saa"),
 "taqwa": copy_gloss("wasiyyat-abi-hanifa-samti", "taqwa"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/30.json").write_text(
    json.dumps({"chapter": 30, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 30 for c in man["chapters"]):
    man["chapters"].append({"n": 30, "title": TITLE30})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.30.0"
ADD_EN = (" Chapter 30 carries the khabar worn for insha (lines ~2216-2222, sahifa 77): "
          "all four sentences are the source's own worked examples verbatim, Ottoman "
          "orthography normalized to standard — اِلَىَّ to إِلَيَّ, رَزَقَنِىَ to رَزَقَنِيَ, "
          "لِقَائَكَ to لِقَاءَكَ, تَأْتِينِى to تَأْتِينِي — recorded normalizations, no "
          "wording changed.")
ADD_TR = (" Otuzuncu bâb, inşâ mânâsında kullanılan haberi taşır (satır ~2216-2222, sahife 77): "
          "dört cümlenin dördü de kaynağın kendi işlenmiş örneklerinin aynen alınmışıdır; Osmanlı "
          "imlâsı standart imlâya çevrildi — اِلَىَّ → إِلَيَّ, رَزَقَنِىَ → رَزَقَنِيَ, "
          "لِقَائَكَ → لِقَاءَكَ, تَأْتِينِى → تَأْتِينِي — kayıtlı normalizasyonlardır, hiçbir "
          "ifade değiştirilmedi.")
if "2216-2222" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "waffaqa" not in mo["verbs"]:
    mo["verbs"]["waffaqa"] = _sg.derived(
        _sg.B2, _sg.W2, "ُ", "وَفَّق", "وَفِّق", "وَفِّق",
        "تَوْفِيق", "مُوَفِّق", "مُوَفَّق", "وُفِّقَ", "يُوَفَّقُ")
if "razaqa" not in mo["verbs"]:
    mo["verbs"]["razaqa"] = _sg.sound1(
        "nasara", "رَزَق", "رْزُق", "اُرْزُق", "رِزْق", "رَازِق",
        "مَرْزُوق", "رُزِقَ", "يُرْزَقُ")
if "nazara" not in mo["verbs"]:
    mo["verbs"]["nazara"] = copy_verb("wasiyyat-abi-hanifa", "nazara")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 134
GR = ROOT / "content/grammar"
NOTE134 = {
 "id": "khabar-fi-mana-al-insha",
 "title": {"ar": "الْخَبَرُ الْمُسْتَعْمَلُ فِي مَعْنَى الْإِنْشَاءِ",
           "en": "Khabar worn for insha: the four reasons",
           "tr": "İnşâ mânâsında kullanılan haber: dört sebep"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح (الخطيب القزويني) — الخبر المستعمل في معنى الإنشاء"],
 "question": {
  "en": ["Is the sentence a report whose truth could even be asked about? Then it is khabar on its post.",
         "Is it a du'a in a mazi's dress — وَفَّقَكَ اللهُ? TAFA'UL or IZHAR AL-HIRS — the books leave a mazi du'a open to both.",
         "Is a request worded as what the addressee simply does — تَأْتِينِي غَدًا? The amr's shape is being fled, or the hearer pressed."],
  "tr": ["Cümle, doğruluğu sorulabilecek bir haber mi? O hâlde haber, yerindedir.",
         "Mâzî kılığında bir duâ mı — وَفَّقَكَ اللهُ? TEFE'ÜL veya İZHÂR-I HIRS — kitaplar mâzî duâyı ikisine de açık bırakır.",
         "İstek, muhatabın zaten yaptığı bir şey gibi mi söylenmiş — تَأْتِينِي غَدًا? Ya emrin kalıbından kaçılıyor, ya muhatap zorlanıyordur."]},
 "plain": {
  "en": "A report's shape can carry a request, for four reasons: the good omen (وَفَّقَكَ اللهُ — the wish spoken as done), showing eagerness (رَزَقَنِيَ اللهُ), fleeing the command's shape before one's master (يَنْظُرُ الْمَوْلَى), and pressing a hearer who will not let the speaker stand a liar (تَأْتِينِي غَدًا).",
  "tr": "Haber kalıbı dört sebeple istek taşır: hayra yormak (وَفَّقَكَ اللهُ — olmuş gibi söylenen dilek), düşkünlüğü göstermek (رَزَقَنِيَ اللهُ), efendi karşısında emir kalıbından kaçmak (يَنْظُرُ الْمَوْلَى) ve konuşanı yalancı çıkarmak istemeyen muhatabı işe sevk etmek (تَأْتِينِي غَدًا)."},
 "explanation": {
  "en": "The five insha babs each showed insha leaving its post; this bab is the mirror — the KHABAR standing where insha belongs, for four reasons the source lists: (1) التَّفَاؤُل, the good omen — the mazi speaks the wish as already granted; (2) إِظْهَارُ الْحِرْصِ, showing eagerness for the thing's occurrence — and the tanbih rules that a mazi du'a from an eloquent speaker is OPEN TO BOTH of these; (3) التَّحَرُّزُ عَنْ صُورَةِ الْأَمْرِ — the slave may not command, so يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً words the plea as the master's own doing; (4) حَمْلُ الْمُخَاطَبِ عَلَى الْمَطْلُوبِ — تَأْتِينِي غَدًا presses a hearer who will not let the speaker prove false. The bab closes on the reverse tanbih: in most of the five preceding babs the insha runs parallel to the ikhbari the same way — let the reader of insight carry the doctrine across.",
  "tr": "Beş inşâ bâbı, inşânın yerinden çıkışını gösterdi; bu bâb aynadır — İNŞÂNIN yerinde duran HABER, kaynağın saydığı dört sebeple: (1) التَّفَاؤُل, hayra yormak — mâzî, dileği verilmiş gibi söyler; (2) إِظْهَارُ الْحِرْصِ, vukuuna düşkünlüğü göstermek — ve tenbih: beliğin mâzî duâsı bu İKİSİNE DE açıktır; (3) التَّحَرُّزُ عَنْ صُورَةِ الْأَمْرِ — köle emredemez; يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً niyazı, efendinin kendi işi gibi söyler; (4) حَمْلُ الْمُخَاطَبِ عَلَى الْمَطْلُوبِ — تَأْتِينِي غَدًا, konuşanı yalancı çıkarmaya râzı olmayan muhatabı zorlar. Bâb, ters tenbihle kapanır: geçen beş bâbın çoğunda inşâ da ihbârîye aynı şekilde paraleldir — basîret ehli okuyucu hükmü öteye taşısın."},
 "examples": [
  {"ar": "وَفَّقَكَ اللهُ لِلتَّقْوَى",
   "en": "«May Allah grant you success toward taqwa» — tafa'ul: the wish as a done deed.",
   "tr": "«Allah seni takvâya muvaffak kılsın» — tefe'ül: dilek, olmuş bir iş gibi.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً",
   "en": "«My master looks at me for a moment» — the amr's shape fled.",
   "tr": "«Efendim bana bir an bakar» — emrin kalıbından kaçış.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "تَأْتِينِي غَدًا",
   "en": "«You come to me tomorrow» — the hearer carried to the deed.",
   "tr": "«Yarın bana gelirsin» — muhatap işe sevk edilir.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"}],
 "commonMistakes": [
  {"wrong": "«وَفَّقَكَ اللهُ geçmiş bir olayın haberidir»",
   "right": "«Mâzî kalıbında bir duâdır — tefe'ül veya hırs izhârı için»",
   "why": {"en": "Read as a report it would claim the tawfiq already happened — which no speaker of the formula means. The mazi is chosen FOR the omen in it: a wish spoken as done. The frame (Allah as fa'il, the speaker or addressee as object) is the receipt.",
           "tr": "Haber okunsa, tevfîkin çoktan vâki olduğu iddia edilmiş olurdu — formülü söyleyen hiç kimse bunu kastetmez. Mâzî, içindeki uğur İÇİN seçilir: olmuş gibi söylenen dilek. Çerçeve (fâil Allah, mef'ûl konuşan veya muhatap) makbuzdur."}}],
 "relatedNotes": ["al-amr-wa-wujuhuh", "khuruj-al-istifham", "insha-wa-tamanni"]}

(GR / "khabar-fi-mana-al-insha.json").write_text(
    json.dumps(NOTE134, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch30:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + waffaqa, razaqa, nazara(copy); note 134")
