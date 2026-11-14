# -*- coding: utf-8 -*-
"""Author chapter 49 of talkhis-al-miftah — أَدَاةُ التَّشْبِيهِ وَأَغْرَاضُهُ (sahifa
111-113, lines ~3200-3290): the adat and what follows it, the verb that
tells of a likening (nearness / distance), the AIMS of the tashbih — the
seven that return to the mushabbah and the two that return to the bihi
(the reversed tashbih) — and the judgement of TASHABUH instead.

  s1-s2   the adat and its rule — RESTORED from the source's Turkish.
  s3      the aya 18:45 وَاضْرِبْ لَهُمْ مَثَلَ الْحَيَاةِ الدُّنْيَا كَمَاءٍ … — as printed
          (the source writes الْحَيٰوةِ with the dagger alif; the app writes الْحَيَاةِ).
  s4-s5   the intended likening and the verb that tells of it — RESTORED.
  s6-s7   عَلِمْتُ زَيْدًا أَسَدًا / حَسِبْتُ زَيْدًا أَسَدًا — the examples as printed,
          in a restored frame.
  s8-s9   the aims — RESTORED.
  s10     al-Mutanabbi's فَإِنْ تَفُقِ الْأَنَامَ … — as printed.
  s11-s15 the aims with their examples — RESTORED from the source's Turkish
          (the matn's own examples: the garment, the raven, writing on water,
          the black face, the coal).
  s16-s17 Abu l-ʿAtahiya's وَلَازَوَرْدِيَّةٍ … / كَأَنَّهَا فَوْقَ قَامَاتٍ … — as printed
          (the source writes وَلاَ زِوَرْدِيَّةٍ with a kasra; the app writes
          لَازَوَرْدِيَّةٍ, the received reading of the word).
  s18     the aims of the bihi — RESTORED.
  s19     Muhammad b. Wuhayb's وَبَدَا الصَّبَاحُ كَأَنَّ غُرَّتَهُ … — as printed.
  s20-s21 the second aim and the rule of tashabuh — RESTORED.
  s22     Abu Ishaq's تَشَابَهَ دَمْعِي … — as printed, except that the source
          prints عَيْنَىَّ where its own Turkish reads the eyes as the subject
          (gözlerim … döküyor): the app writes عَيْنِي, the fa'il, and records it.

Every likening carries an authored `tashbih` frame — arkan, kind, shapes —
the engine is tested against, including the two verb-of-the-heart frames
(qulub), the masdar frames whose ends are relatives and nominal clauses,
and the TASHABUH frame with no direction.

Grammar this chapter teaches: note `aghrad-al-tashbih` (group bayan); the
verbs of the heart with two objects; the waw of رُبَّ; the reversed tashbih;
the manqus fa'il (يَلِيهِ); paradigms أَنْبَأَ، حَسِبَ، فَاقَ، رَقَمَ، زَهَا، ضَعُفَ،
بَدَا، اِمْتَدَحَ، تَشَابَهَ، سَكَبَ; أَنْزَلَ، قَصَدَ، حَصَلَ copied.
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
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
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
def frame(mush, adat, bihi, wajh, kind, sm, sb, sw, **extra):
    f = {"mushabbah": mush, "adat": adat, "bihi": bihi, "wajh": wajh, "kind": kind,
         "shape": {"mushabbah": sm, "bihi": sb, "wajh": sw}}
    f.update(extra); return f
S = []
G = "aghrad-al-tashbih"; A = "arkan-al-tashbih"; W = "wajh-al-shabah"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
TITLE49 = {"ar": "أَدَاةُ التَّشْبِيهِ وَأَغْرَاضُهُ: مَا يَعُودُ إِلَى الْمُشَبَّهِ وَمَا يَعُودُ إِلَى الْمُشَبَّهِ بِهِ، وَالتَّشَابُهُ",
           "en": "The Adat of Tashbih and its Aims: what Returns to the Mushabbah, what Returns to the Bihi, and Tashabuh",
           "tr": "Teşbih Edatı ve Gayeleri: Müşebbehe Dönen, Müşebbehün Bihe Dönen, ve Teşâbüh"}

# ----------- s1 — the adat (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The adat of tashbih is the kaf, كَأَنَّ, مِثْل and the like." + R_EN,
 "tr": "Teşbih edatı kâf, كَأَنَّ, مِثْل ve benzerleridir." + R_TR},
 "tokens": [
  tok("أَدَاةُ","adat","noun",[G,A,"mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.", "«the tool of» — the mubtada, annexed.", "«edatı» — mübtedâ, muzâf."),
  tok("التَّشْبِيهِ","tashbih","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«likening».", "«teşbihin»."),
  tok("الْكَافُ","kaf-letter","noun",[G,A,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ الْحَرْفِ.", "«the kaf» — the khabar: the letter named as a noun.", "«kâf» — haber: harfin adı isim olarak."),
  tok("وَكَأَنَّ","ka-anna","part",[G,A,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَكَأَنَّ مَعْطُوفٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ — لَفْظٌ مَذْكُورٌ لَا حَرْفٌ عَامِلٌ.",
      "«and كَأَنَّ» — the word QUOTED and joined: it names the particle, it does not govern — the engine reads no likening here.",
      "«ve كَأَنَّ» — NAKLEDİLMİŞ ve atfedilmiş kelime: edatı adlandırır, amel etmez — motor burada teşbih okumaz.",
      segments=[seg("وَ","wa","conj"), seg("كَأَنَّ","ka-anna","part")]),
  tok("وَمِثْلُ","mithl","noun",[G,A,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and مِثْل» — joined.", "«ve مِثْل» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("مِثْلُ","mithl","noun")]),
  tok("وَنَحْوُهُ","nahw","noun",[G,A,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: مَا فِي مَعْنَى مِثْلٍ.",
      "«and the like of it» — joined; whatever means مِثْل (شِبْه، نَظِير…).", "«ve benzeri» — atıf; مِثْل mânâsındaki her kelime (شِبْه، نَظِير…).",
      segments=[seg("وَ","wa","conj"), seg("نَحْوُ","nahw","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s2 — what follows the kaf (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "The rule with the kaf and its kin is that the mushabbah bihi follows it — yet sometimes something else does." + R_EN,
 "tr": "Kâf ve benzerlerinde asıl olan, müşebbehün bihin onu takip etmesidir — fakat bazen başkası takip eder." + R_TR},
 "tokens": [
  tok("وَالْأَصْلُ","asl","noun",[G,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْأَصْلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the rule» — the mubtada.", "«asıl olan» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْأَصْلُ","asl","noun")]),
  tok("فِي","fi","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«with».", "«-de»."),
  tok("نَحْوِ","nahw","noun",[G,"huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — نَحْوِ الْكَافِ: الْكَافُ وَمَا فِي مَعْنَاهَا. لَا أَدَاةَ تَشْبِيهٍ هُنَا: نَحْوِ بَعْدَ حَرْفِ جَرٍّ يُسَمِّي صِنْفًا.",
      "«the like of» — annexed to the kaf: the kaf and its kin. NOT an adat: نَحْو after a jarr-particle names a class, and the engine refuses a likening.",
      "«benzeri» — kâfa muzâf: kâf ve benzerleri. Edat DEĞİL: cer harfinden sonraki نَحْو bir sınıf adlandırır, motor teşbihi reddeder."),
  tok("الْكَافِ","kaf-letter","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the kaf».", "«kâfın»."),
  tok("أَنْ","an-masdariyya","part",[G,"an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — its clause is the khabar.", "«-ması» — cümlesi haberdir."),
  tok("يَلِيَهُ","waliya","verb",[G,"an-masdariyya","mithal-verbs","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْهَاءُ مَفْعُولٌ بِهِ — لَفِيفٌ مَفْرُوقٌ: وَلِيَ يَلِي.",
      "«follows it» — nasb by أَنْ, the fatha shown on the ya (the naqis takes nasb openly); the ha is its object. وَلِيَ يَلِي is doubly weak (waw first, ya last).",
      "«onu takip etsin» — أَنْ ile mansub, fetha yâ üzerinde açık (nâkıs nasbı açık gösterir); hâ mef'ûl. وَلِيَ يَلِي lefîf-i mefrûktur (başta vâv, sonda yâ).",
      segments=[seg("يَلِيَ","waliya","verb"), seg("هُ","pron-3ms","pron")]),
  tok("الْمُشَبَّهُ","mushabbah","noun",[G,A,"fail","ism-maful"], "فَاعِلٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ شَبَّهَ.", "«the mushabbah» — the fa'il.", "«müşebbeh» — fâil."),
  tok("بِهِ","bi","part",[G,A,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْمُشَبَّهُ — الْمُشَبَّهُ بِهِ: الِاسْمُ الْمُرَكَّبُ.",
      "«bihi» — completes the term الْمُشَبَّهُ بِهِ: the thing likened TO.", "«bih» — الْمُشَبَّهُ بِهِ terimini tamamlar: kendisine benzetilen.",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("وَقَدْ","qad","part",[G,"qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«yet sometimes».", "«fakat bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يَلِيهِ","waliya","verb",[G,"mudari-marfu","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْهَاءُ مَفْعُولٌ بِهِ.",
      "«follows it» — raf' by a damma only supposed on the ya.", "«onu takip eder» — ref'i yâ üzerinde takdîrî damme.",
      segments=[seg("يَلِي","waliya","verb"), seg("هِ","pron-3ms","pron")]),
  tok("غَيْرُهُ","ghayr","noun",[G,"fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — غَيْرُ الْمُشَبَّهِ بِهِ.",
      "«something else» — the fa'il: other than the bihi, as the aya shows next.", "«başkası» — fâil: bihten başkası; âyet bunu gösterir.",
      segments=[seg("غَيْرُ","ghayr","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s3 — the aya 18:45 (as printed; الْحَيٰوةِ → الْحَيَاةِ)
S.append({"id": "s3", "translation": {
 "en": "«And strike for them the likeness of the life of this world: as water We sent down from the sky.» (18:45)",
 "tr": "«Onlara dünya hayatının misalini ver: gökten indirdiğimiz bir su gibi.» (18:45)"},
 "tashbih": frame([2, 3, 4], 5, [5, 6, 7, 8], [], "mursal-mujmal", "mufrad", "murakkab", None),
 "tokens": [
  tok("وَاضْرِبْ","daraba","verb",[G,"imperative-amr"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاضْرِبْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ أَنْتَ — ضَرَبَ الْمَثَلَ: ذَكَرَهُ.",
      "«and strike» — the amr on sukun; ضَرَبَ مَثَلًا = to set forth a parable.", "«ver» — sükûn üzere emir; ضَرَبَ مَثَلًا = misal getirmek.",
      segments=[seg("وَ","wa","conj"), seg("اضْرِبْ","daraba","verb")]),
  tok("لَهُمْ","li","part",[G,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِاضْرِبْ.", "«for them».", "«onlara».",
      segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَثَلَ","mathal","noun",[G,A,"maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ — الْمُشَبَّهُ: مَثَلُ الْحَيَاةِ.",
      "«the likeness of» — the object, annexed: the MUSHABBAH is the state of this life (مَثَل, not مِثْل).",
      "«misalini» — mef'ûl, muzâf: MÜŞEBBEH dünya hayatının hâlidir (مَثَل, مِثْل değil)."),
  tok("الْحَيَاةِ","hayat","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — يَكْتُبُهُ الْمَصْدَرُ الْحَيٰوةِ.", "«the life» (the source writes الْحَيٰوةِ).", "«hayatının» (kaynak الْحَيٰوةِ yazar)."),
  tok("الدُّنْيَا","dunya","noun",[G,"naat-sifa","ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«this world's» — na't, a maqsur.", "«dünya» — sıfat, maksûr."),
  tok("كَمَاءٍ","ma-water","noun",[G,A,"huruf-jarr","hal","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ، وَمَاءٍ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ حَالٌ أَوْ صِفَةٌ. الْأَدَاةُ، وَمَا بَعْدَهَا لَيْسَ الْمُشَبَّهَ بِهِ عَلَى الْحَقِيقَةِ.",
      "«as water» — the kaf-adat; what follows it is NOT the real bihi (the life is not likened to water) but the start of its description.",
      "«bir su gibi» — kâf-edat; ardındaki, gerçek bih DEĞİLDİR (hayat suya benzetilmemiştir), tasvirinin başıdır.",
      segments=[seg("كَ","ka","part"), seg("مَاءٍ","ma-water","noun")]),
  tok("أَنْزَلْنَاهُ","anzala","verb",[G,"jumla-sifa","form-iv-verbs"],
      "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِمَاءٍ.",
      "«We sent down» — the describing clause on the indefinite مَاءٍ; the ha returns to it. The bihi is a whole picture.",
      "«indirdiğimiz» — nekre مَاءٍ'in vasıf cümlesi; hâ ona döner. Bih bütün bir tablodur.",
      segments=[seg("أَنْزَلْنَا","anzala","verb"), seg("هُ","pron-3ms","pron")]),
  tok("مِنَ","min","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("السَّمَاءِ","sama","noun",[G,"huruf-jarr","ism-mamdud"],
      "اسْمٌ مَجْرُورٌ مُتَعَلِّقٌ بِأَنْزَلْنَا.",
      "«the sky» — the aya continues: the plants mingle with it, then become dry chaff the winds scatter — THAT is the bihi.",
      "«gökten» — âyet devam eder: bitkiler ona karışır, sonra rüzgârın savurduğu kuru çöpe döner — bih İŞTE odur.",
      punct=".")]})

# ----------- s4 — what is meant (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "What is meant is the likening of the state of this world, in the speed of its passing, to the state of the plants that arise from the water." + R_EN,
 "tr": "Murad, dünyanın hâlini — geçip gitmesinin hızında — sudan hâsıl olan bitkinin hâline benzetmektir." + R_TR},
 "tashbih": frame([2, 3], 1, [7, 8, 9], [4, 5, 6], "mursal-mufassal", "mufrad", "mufrad", "murakkab"),
 "tokens": [
  tok("فَالْمُرَادُ","murad","noun",[G,"mubtada-khabar","ism-maful"], "الْفَاءُ لِلتَّعْلِيلِ، وَالْمُرَادُ مُبْتَدَأٌ مَرْفُوعٌ.", "«what is meant» — the mubtada.", "«murad» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْمُرَادُ","murad","noun")]),
  tok("تَشْبِيهُ","tashbih","noun",[G,A,"mubtada-khabar","idafa-definiteness","imal-al-masdar"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ: الْأَدَاةُ.", "«the likening of» — the khabar; the masdar-adat.", "«benzetmektir» — haber; masdar-edat."),
  tok("حَالِ","hal","noun",[G,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ — الْمُشَبَّهُ.", "«the state of» — the mushabbah begins.", "«hâlini» — müşebbeh başlar."),
  tok("الدُّنْيَا","dunya","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«this world».", "«dünyanın»."),
  tok("فِي","fi","part",[G,W,"huruf-jarr"], "حَرْفُ جَرٍّ — يَبْدَأُ وَجْهَ الشَّبَهِ.", "«in» — the WAJH begins, spoken between the two ends.", "«-de» — VECH başlar, iki taraf arasında söylenmiş."),
  tok("سُرْعَةِ","sura-speed","noun",[G,W,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ مُضَافٌ.", "«the speed of».", "«hızında»."),
  tok("زَوَالِهَا","zawal","noun",[G,W,"idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — مَصْدَرُ زَالَ.",
      "«its passing» — an idafa chain of masdars: the wajh is a picture (how fast a thing goes), not one quality.",
      "«geçip gitmesinin» — masdarlardan izâfet zinciri: vech bir tablodur (bir şeyin ne hızla gittiği), tek vasıf değil.",
      segments=[seg("زَوَالِ","zawal","noun"), seg("هَا","pron-3fs","pron")]),
  tok("بِحَالِ","hal","noun",[G,A,"huruf-jarr","idafa-definiteness"],
      "الْبَاءُ جَارَّةٌ وَحَالِ مَجْرُورٌ مُضَافٌ — الْمُشَبَّهُ بِهِ.", "«to the state of» — the bihi.", "«hâline» — bih.",
      segments=[seg("بِ","bi","part"), seg("حَالِ","hal","noun")]),
  tok("النَّبَاتِ","nabat","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the plants».", "«bitkinin»."),
  tok("الْحَاصِلِ","hasil","noun",[G,"naat-sifa","ism-fail"], "نَعْتٌ مَجْرُورٌ.", "«arising» — na't.", "«hâsıl olan» — sıfat."),
  tok("مِنَ","min","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْمَاءِ","ma-water","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ مُتَعَلِّقٌ بِالْحَاصِلِ.", "«the water» — hangs on الْحَاصِلِ.", "«sudan» — الْحَاصِلِ'e bağlı.", punct=".")]})

# ----------- s5 — the verb that tells of a likening (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "And sometimes a verb is mentioned that tells of the likening." + R_EN,
 "tr": "Bazen de teşbihten haber veren bir fiil zikredilir." + R_TR},
 "tokens": [
  tok("وَقَدْ","qad","part",[G,"qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يُذْكَرُ","dhakara","verb",[G,"naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is mentioned» — majhul.", "«zikredilir» — meçhul."),
  tok("فِعْلٌ","fil","noun",[G,"naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a verb» — the deputy fa'il.", "«bir fiil» — nâib-i fâil."),
  tok("يُنْبِئُ","anbaa","verb",[G,"jumla-sifa","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِفِعْلٌ. مَهْمُوزُ اللَّامِ.",
      "«that tells» — the describing clause on the indefinite فِعْلٌ; Form IV with a hamza as last radical.",
      "«haber veren» — nekre فِعْلٌ'ün vasıf cümlesi; lâmı hemzeli IV. bâb."),
  tok("عَنِ","an","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of» — its nun takes a kasra before the article.", "«-den» — nûnu harf-i tarif önünde kesra alır."),
  tok("التَّشْبِيهِ","tashbih","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the likening».", "«teşbihten».", punct=".")]})

# ----------- s6 — nearness: عَلِمْتُ (the example as printed, the frame restored)
S.append({"id": "s6", "translation": {
 "en": "If nearness is intended, one says: «I knew Zayd to be a lion.»" + R_EN,
 "tr": "Yakınlık kastedilirse denir: «Zeyd'i arslan bildim.»" + R_TR},
 "tashbih": frame([5], 4, [6], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("فَإِنْ","in-shartiyya","part",[G,"in-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the shart.", "«eğer» — şart.",
      segments=[seg("فَ","fa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("قُصِدَ","qasada","verb",[G,"in-shartiyya","naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.", "«is intended» — the shart-verb, majhul.", "«kastedilirse» — şart fiili, meçhul."),
  tok("الْقُرْبُ","qurb","noun",[G,"naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — قُرْبُ الْمُشَبَّهِ مِنَ الْمُشَبَّهِ بِهِ.", "«nearness» — the deputy: the mushabbah is CLOSE to the bihi.", "«yakınlık» — nâib: müşebbeh bihe YAKINDIR."),
  tok("قِيلَ","qala","verb",[G,"in-shartiyya","naib-al-fail","hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ — أَجْوَفُ: قُوِلَ → قِيلَ.",
      "«one says» — the jawab; the hollow majhul (قُوِلَ → قِيلَ).", "«denir» — cevap; ecvef meçhul (قُوِلَ → قِيلَ).", punct=":"),
  tok("عَلِمْتُ","alima","verb",[G,A,"zanna-wa-akhawatuha","mafulayn","tashbih"],
      "فِعْلٌ مَاضٍ مِنْ أَفْعَالِ الْقُلُوبِ، وَالتَّاءُ فَاعِلٌ — يَنْصِبُ مَفْعُولَيْنِ أَصْلُهُمَا مُبْتَدَأٌ وَخَبَرٌ. وَهُوَ الْفِعْلُ الْمُنْبِئُ عَنِ التَّشْبِيهِ: أَدَاتُهُ.",
      "«I knew» — a verb of the HEART taking two objects (once mubtada and khabar); it is the verb that tells of the likening — the ADAT — and عَلِمَ says the two are close.",
      "«bildim» — iki mef'ûl alan KALP fiili (aslı mübtedâ ve haber); benzetmeden haber veren fiil — EDAT — ve عَلِمَ ikisinin yakın olduğunu söyler."),
  tok("زَيْدًا","zayd","propn",[G,A,"mafulayn","maful-bihi"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ — الْمُشَبَّهُ.", "«Zayd» — the first object: the MUSHABBAH.", "«Zeyd'i» — ilk mef'ûl: MÜŞEBBEH."),
  tok("أَسَدًا","asad","noun",[G,A,"mafulayn","maful-bihi","tashbih"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — الْمُشَبَّهُ بِهِ.", "«a lion» — the second object: the MUSHABBAH BIHI.", "«arslan» — ikinci mef'ûl: MÜŞEBBEHÜN BİH.", punct=".")]})

# ----------- s7 — distance: حَسِبْتُ
S.append({"id": "s7", "translation": {
 "en": "And if distance is intended, one says: «I reckoned Zayd a lion.»" + R_EN,
 "tr": "Uzaklık kastedilirse denir: «Zeyd'i arslan sandım.»" + R_TR},
 "tashbih": frame([5], 4, [6], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("وَإِنْ","in-shartiyya","part",[G,"in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».",
      segments=[seg("وَ","wa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("قُصِدَ","qasada","verb",[G,"in-shartiyya","naib-al-fail"], "فِعْلُ الشَّرْطِ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is intended».", "«kastedilirse»."),
  tok("الْبُعْدُ","bud-distance","noun",[G,"naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — بُعْدُ الْمُشَبَّهِ عَنِ الْمُشَبَّهِ بِهِ.", "«distance» — the mushabbah is FAR from the bihi.", "«uzaklık» — müşebbeh bihten UZAKTIR."),
  tok("قِيلَ","qala","verb",[G,"in-shartiyya","naib-al-fail"], "جَوَابُ الشَّرْطِ.", "«one says».", "«denir».", punct=":"),
  tok("حَسِبْتُ","hasiba","verb",[G,A,"zanna-wa-akhawatuha","mafulayn","tashbih"],
      "فِعْلٌ مَاضٍ مِنْ أَفْعَالِ الْقُلُوبِ لِلظَّنِّ، وَالتَّاءُ فَاعِلٌ — الْأَدَاةُ، وَتُنْبِئُ عَنِ الْبُعْدِ.",
      "«I reckoned» — a verb of the heart for SUPPOSING: the adat, and it says the likeness is far (حَسِبَ يَحْسَبُ).",
      "«sandım» — ZAN bildiren kalp fiili: edat, ve benzerliğin uzak olduğunu söyler (حَسِبَ يَحْسَبُ)."),
  tok("زَيْدًا","zayd","propn",[G,A,"mafulayn"], "مَفْعُولٌ بِهِ أَوَّلُ — الْمُشَبَّهُ.", "«Zayd» — the mushabbah.", "«Zeyd'i» — müşebbeh."),
  tok("أَسَدًا","asad","noun",[G,A,"mafulayn","tashbih"], "مَفْعُولٌ بِهِ ثَانٍ — الْمُشَبَّهُ بِهِ.", "«a lion» — the bihi.", "«arslan» — bih.", punct=".")]})

# ----------- s8 — the aim mostly returns to the mushabbah (RESTORED)
S.append({"id": "s8", "translation": {
 "en": "The aim of the tashbih, in most cases, returns to the mushabbah." + R_EN,
 "tr": "Teşbihin gayesi çoğunlukla müşebbehe döner." + R_TR},
 "tokens": [
  tok("وَالْغَرَضُ","gharad","noun",[G,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْغَرَضُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the aim» — the mubtada.", "«gaye» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْغَرَضُ","gharad","noun")]),
  tok("مِنَ","min","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("التَّشْبِيهِ","tashbih","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ مُتَعَلِّقٌ بِالْغَرَضِ.", "«the likening».", "«teşbihin»."),
  tok("فِي","fi","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْأَغْلَبِ","aghlab","noun",[G,"huruf-jarr","ism-tafdil"], "اسْمٌ مَجْرُورٌ — اسْمُ تَفْضِيلٍ: فِي أَكْثَرِ الْأَحْوَالِ.", "«the most (cases)» — an ism tafdil.", "«çoğunlukla» — ism-i tafdil."),
  tok("يَعُودُ","ada-return","verb",[G,"hollow-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«returns» — the verbal khabar.", "«döner» — fiil cümlesi haber."),
  tok("إِلَى","ila","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[G,A,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the mushabbah» — the aims serve the thing likened.", "«müşebbehe» — gayeler benzetilene hizmet eder.", punct=".")]})

# ----------- s9 — the seven aims (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "It is: showing its possibility, or its state, or the measure of that state, or settling it, or adorning the mushabbah, or disfiguring it, or making it seem novel." + R_EN,
 "tr": "O da: müşebbehin imkânını, yahut hâlini, yahut hâlinin miktarını göstermek, yahut hâlini karara bağlamak, yahut müşebbehi süslemek, yahut çirkin göstermek, yahut yeni ve hoş göstermektir." + R_TR},
 "tokens": [
  tok("وَهُوَ","huwa","pron",[G,"mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ — الْغَرَضُ.", "«and it» — the aim.", "«o da» — gaye.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("بَيَانُ","bayan","noun",[G,"mubtada-khabar","idafa-definiteness","masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ بَيَّنَ.", "«showing» — the khabar; the first aim.", "«göstermek» — haber; ilk gaye."),
  tok("إِمْكَانِهِ","imkan","noun",[G,"idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْهَاءُ لِلْمُشَبَّهِ.", "«its possibility» — (1) that the mushabbah CAN be.", "«imkânını» — (1) müşebbehin OLABİLECEĞİ.",
      segments=[seg("إِمْكَانِ","imkan","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("أَوْ","aw","conj",[G,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("حَالِهِ","hal","noun",[G,"atf-nasaq","idafa-definiteness"], "مَعْطُوفٌ عَلَى إِمْكَانِهِ مَجْرُورٌ.", "«its state» — (2).", "«hâlini» — (2).",
      segments=[seg("حَالِ","hal","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("أَوْ","aw","conj",[G,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("مِقْدَارِهَا","miqdar","noun",[G,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ، وَهَا لِلْحَالِ.", "«the measure of it» — (3) how much of that state; the ha returns to حَال.", "«miktarını» — (3) o hâlin ne kadarı; hâ حَال'e döner.",
      segments=[seg("مِقْدَارِ","miqdar","noun"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("أَوْ","aw","conj",[G,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("تَقْرِيرُهَا","taqrir","noun",[G,"atf-nasaq","masdar","form-ii-verbs"],
      "مَعْطُوفٌ عَلَى بَيَانُ مَرْفُوعٌ — فَالضَّمَّةُ: هُوَ عَطْفٌ عَلَى الْخَبَرِ لَا عَلَى الْمُضَافِ إِلَيْهِ.",
      "«settling it» — (4) joined to بَيَانُ in RAF' (the damma shows it): the join climbs back to the khabar.",
      "«karara bağlamak» — (4) بَيَانُ'ya REF' ile atıf (damme gösterir): atıf habere geri tırmanır.",
      segments=[seg("تَقْرِيرُ","taqrir","noun"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("أَوْ","aw","conj",[G,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("تَزْيِينُهُ","tazyin","noun",[G,"atf-nasaq","masdar","form-ii-verbs"], "مَعْطُوفٌ مَرْفُوعٌ.", "«adorning it» — (5).", "«süslemek» — (5).",
      segments=[seg("تَزْيِينُ","tazyin","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("أَوْ","aw","conj",[G,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("تَشْوِيهُهُ","tashwih","noun",[G,"atf-nasaq","masdar","form-ii-verbs"], "مَعْطُوفٌ مَرْفُوعٌ.", "«disfiguring it» — (6).", "«çirkin göstermek» — (6).",
      segments=[seg("تَشْوِيهُ","tashwih","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("أَوِ","aw","conj",[G,"atf-nasaq"], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — its waw takes a kasra before the wasl-alif.", "«yahut» — vâvı vasl elifi önünde kesra alır."),
  tok("اسْتِطْرَافُهُ","istitraf","noun",[G,"atf-nasaq","masdar","form-x-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ اسْتَطْرَفَ: عَدُّهُ طَرِيفًا.", "«making it seem novel» — (7) the masdar of Form X: to count a thing fresh and strange.", "«yeni göstermek» — (7) X. bâbın masdarı: bir şeyi yeni ve hoş saymak.",
      segments=[seg("اسْتِطْرَافُ","istitraf","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s10 — al-Mutanabbi: the hidden likening (as printed)
S.append({"id": "s10", "translation": {
 "en": "«If you surpass mankind while you are of them — why, musk is but part of the gazelle's blood.»",
 "tr": "«İnsanlardan olduğun hâlde insanları aşarsan (bu mümkündür): misk de ceylanın kanının bir parçasıdır.»"},
 "tokens": [
  tok("فَإِنْ","in-shartiyya","part",[G,"in-shartiyya"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the shart.", "«eğer» — şart.",
      segments=[seg("فَ","fa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("تَفُقِ","faqa","verb",[G,"in-shartiyya","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِإِنْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَحُذِفَتْ عَيْنُهُ لِلْجَزْمِ (تَفُوقُ → تَفُقْ)، وَالْفَاعِلُ أَنْتَ.",
      "«you surpass» — the hollow verb in jazm: the waw drops (تَفُوقُ → تَفُقْ) and the sukun takes a kasra before the article.",
      "«aşarsan» — meczum ecvef: vâv düşer (تَفُوقُ → تَفُقْ), sükûn harf-i tarif önünde kesra alır."),
  tok("الْأَنَامَ","anam-mankind","noun",[G,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْأَنَامُ: الْخَلْقُ.", "«mankind» — the object.", "«insanları» — mef'ûl."),
  tok("وَأَنْتَ","anta","pron",[G,"hal","anwa-al-waw","mubtada-khabar"],
      "الْوَاوُ لِلْحَالِ، وَأَنْتَ مُبْتَدَأٌ — وَالْجُمْلَةُ حَالٌ.", "«while you» — the waw of hal opens a nominal clause.", "«sen … iken» — hâl vâvı isim cümlesi açar.",
      segments=[seg("وَ","wa","conj"), seg("أَنْتَ","anta","pron")]),
  tok("مِنْهُمْ","min","part",[G,"huruf-jarr","mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«of them» — the khabar: you are one of mankind.", "«onlardansın» — haber.",
      segments=[seg("مِنْ","min","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("فَإِنَّ","inna","part",[G,"inna-wa-akhawatuha","in-shartiyya"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ: فَذَٰلِكَ مُمْكِنٌ، لِأَنَّ…",
      "«why, indeed» — the fa binds the jawab; the answer is understood (THAT IS POSSIBLE) and إِنَّ gives its proof.",
      "«çünkü» — fâ cevabı bağlar; cevap mukadder (BU MÜMKÜNDÜR) ve إِنَّ delilini verir.",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part")]),
  tok("الْمِسْكَ","misk","noun",[G,A,"inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«musk» — the ism of إِنَّ.", "«misk» — إِنَّ'nin ismi."),
  tok("بَعْضُ","bad","noun",[G,"inna-wa-akhawatuha","idafa-definiteness"], "خَبَرُ إِنَّ مَرْفُوعٌ وَهُوَ مُضَافٌ.", "«part of» — the khabar, annexed.", "«bir parçası» — haber, muzâf."),
  tok("دَمِ","dam-blood","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«the blood of».", "«kanının»."),
  tok("الْغَزَالِ","ghazal","noun",[G,A,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ. وَالتَّشْبِيهُ هُنَا ضِمْنِيٌّ: الْمَمْدُوحُ بَيْنَ النَّاسِ كَالْمِسْكِ فِي دَمِ الْغَزَالِ — لَا أَدَاةَ وَلَا مُشَبَّهَ مَذْكُورٌ.",
      "«the gazelle» — the likening is IMPLICIT: the praised man among mankind is as musk within the gazelle's blood — no adat, no mushabbah on the surface, so the engine reads no frame; the aim is to show the mushabbah POSSIBLE.",
      "«ceylanın» — benzetme ZIMNÎdir: memdûh insanlar arasında ceylanın kanındaki misk gibidir — yüzeyde ne edat ne müşebbeh var, motor çerçeve okumaz; gaye müşebbehin MÜMKÜN olduğunu göstermektir.",
      punct=".")],
 "jumal": [J("وَأَنْتَ مِنْهُمْ", "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ حَالٌ.", "The hal-clause: the claim that needs proving.", "Hâl cümlesi: ispat isteyen iddia."),
           J("فَإِنَّ الْمِسْكَ بَعْضُ دَمِ الْغَزَالِ", "جُمْلَةٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، أَوْ تَعْلِيلٌ لِجَوَابٍ مَحْذُوفٍ.", "The jawab, or the proof of a dropped jawab: the hidden tashbih.", "Cevap, yahut düşmüş cevabın delili: gizli teşbih.")]})

# ----------- s11 — the aim: possibility (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "So the aim is to show the mushabbah possible — that the praised one surpasses mankind while being of them." + R_EN,
 "tr": "Gaye, müşebbehin mümkün olduğunu göstermektir: memdûhun insanlardan olduğu hâlde onları aşması." + R_TR},
 "tokens": [
  tok("فَالْغَرَضُ","gharad","noun",[G,"mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْغَرَضُ مُبْتَدَأٌ.", "«so the aim» — the mubtada.", "«gaye» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْغَرَضُ","gharad","noun")]),
  tok("بَيَانُ","bayan","noun",[G,"mubtada-khabar","idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«showing».", "«göstermektir»."),
  tok("إِمْكَانِ","imkan","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مُضَافٌ.", "«the possibility of».", "«imkânını»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[G,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mushabbah».", "«müşebbehin».", punct="،"),
  tok("وَهُوَ","huwa","pron",[G,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ — الْمُشَبَّهُ.", "«and it» — the mushabbah, explained.", "«o da» — müşebbeh, açıklanıyor.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("أَنْ","an-masdariyya","part",[G,"an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that».", "«-ması»."),
  tok("يَفُوقَ","faqa","verb",[G,"an-masdariyya","hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — أَجْوَفُ وَاوِيٌّ، تَعُودُ وَاوُهُ فِي النَّصْبِ.", "«surpasses» — nasb by أَنْ; in nasb the hollow keeps its waw.", "«aşması» — أَنْ ile mansub; nasbda ecvef vâvını korur."),
  tok("الْمَمْدُوحُ","mamduh","noun",[G,"fail","ism-maful"], "فَاعِلٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«the praised one» — the fa'il.", "«memdûh» — fâil."),
  tok("النَّاسَ","nas","noun",[G,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«mankind» — the object.", "«insanları» — mef'ûl."),
  tok("وَهُوَ","huwa","pron",[G,"hal","anwa-al-waw"], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ.", "«while he» — the hal-clause.", "«o … iken» — hâl cümlesi.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("مِنْهُمْ","min","part",[G,"huruf-jarr","mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«of them».", "«onlardan».",
      segments=[seg("مِنْ","min","part"), seg("هُمْ","pron-3mp","pron")], punct=".")]})

# ----------- s12 — the state and its measure (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "As in likening a garment to another in blackness, to show its state — and likening it to the raven, to show the measure of its blackness." + R_EN,
 "tr": "Bir elbiseyi siyahlıkta başka bir elbiseye benzetmek gibi — hâlini göstermek için; ve onu kargaya benzetmek — siyahlığının miktarını göstermek için." + R_TR},
 "tashbih": frame([1], 0, [2], [3, 4], "mursal-mufassal", "mufrad", "mufrad", "mufrad"),
 "tokens": [
  tok("كَتَشْبِيهِ","tashbih","noun",[G,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "الْكَافُ لِلتَّمْثِيلِ جَارَّةٌ، وَتَشْبِيهِ مَجْرُورٌ مُضَافٌ — مَصْدَرٌ عَامِلٌ: الْأَدَاةُ.",
      "«as in the likening of» — the kaf of example on the masdar-adat.", "«benzetmesi gibi» — masdar-edat üstünde örnek kâfı.",
      segments=[seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("ثَوْبٍ","thawb","noun",[G,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«a garment» — the mushabbah.", "«bir elbiseyi» — müşebbeh."),
  tok("بِآخَرَ","akhar","noun",[G,A,"huruf-jarr","mamnu-min-sarf"],
      "الْبَاءُ جَارَّةٌ وَآخَرَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — الْمُشَبَّهُ بِهِ.",
      "«to another» — the bihi; آخَر is a diptote, jarr by fatha.", "«başkasına» — bih; آخَر gayr-i munsarif, cerri fethayla.",
      segments=[seg("بِ","bi","part"), seg("آخَرَ","akhar","noun")]),
  tok("فِي","fi","part",[G,W,"huruf-jarr"], "حَرْفُ جَرٍّ — يَبْدَأُ وَجْهَ الشَّبَهِ.", "«in» — the wajh.", "«-de» — vech."),
  tok("السَّوَادِ","sawad","noun",[G,W,"huruf-jarr"], "اسْمٌ مَجْرُورٌ — وَجْهُ الشَّبَهِ.", "«blackness» — the wajh, one quality.", "«siyahlıkta» — vech, tek vasıf."),
  tok("لِبَيَانِ","bayan","noun",[G,"huruf-jarr","idafa-definiteness","lam-taleel"],
      "اللَّامُ لِلتَّعْلِيلِ، وَبَيَانِ مَجْرُورٌ مُضَافٌ — الْغَرَضُ.", "«to show» — the lam of purpose: the AIM (2).", "«göstermek için» — ta'lil lâmı: GAYE (2).",
      segments=[seg("لِ","li","part"), seg("بَيَانِ","bayan","noun")]),
  tok("حَالِهِ","hal","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its state».", "«hâlini».",
      segments=[seg("حَالِ","hal","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("وَتَشْبِيهِهِ","tashbih","noun",[G,A,"atf-nasaq","idafa-definiteness","imal-al-masdar"],
      "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْمُشَبَّهُ ضَمِيرٌ.",
      "«and likening it» — a second masdar-frame whose mushabbah is the pronoun.", "«ve onu benzetmek» — müşebbehi zamir olan ikinci masdar çerçevesi.",
      segments=[seg("وَ","wa","conj"), seg("تَشْبِيهِ","tashbih","noun"), seg("هِ","pron-3ms","pron")]),
  tok("بِالْغُرَابِ","ghurab","noun",[G,A,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَالْغُرَابِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to the raven» — the bihi.", "«kargaya» — bih.",
      segments=[seg("بِ","bi","part"), seg("الْغُرَابِ","ghurab","noun")]),
  tok("لِبَيَانِ","bayan","noun",[G,"huruf-jarr","lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَبَيَانِ مَجْرُورٌ مُضَافٌ.", "«to show» — the aim (3).", "«göstermek için» — gaye (3).",
      segments=[seg("لِ","li","part"), seg("بَيَانِ","bayan","noun")]),
  tok("مِقْدَارِ","miqdar","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مُضَافٌ.", "«the measure of».", "«miktarını»."),
  tok("سَوَادِهِ","sawad","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its blackness» — how black: the raven is the measure.", "«siyahlığının» — ne kadar siyah: ölçü kargadır.",
      segments=[seg("سَوَادِ","sawad","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s13 — settling the state (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And as in likening one who gets nothing from his striving to one who writes on water." + R_EN,
 "tr": "Ve çabasından bir fayda elde edemeyeni su üzerine yazı yazana benzetmek gibi." + R_TR},
 "tashbih": frame([1, 2, 3, 4, 5, 6, 7], 0, [8, 9, 10, 11], [], "mursal-mujmal", "murakkab", "murakkab", None),
 "tokens": [
  tok("وَكَتَشْبِيهِ","tashbih","noun",[G,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ لِلتَّمْثِيلِ، وَتَشْبِيهِ مَجْرُورٌ مُضَافٌ إِلَى الْمَوْصُولِ — الْأَدَاةُ.",
      "«and as in the likening of» — the masdar-adat, annexed to a RELATIVE: the mushabbah is a whole clause.",
      "«ve … benzetmek gibi» — masdar-edat, bir MEVSÛLE muzâf: müşebbeh bütün bir cümledir.",
      segments=[seg("وَ","wa","conj"), seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("مَنْ","man-mawsul","pron",[G,A,"ism-mawsul","idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْمُشَبَّهُ.", "«one who» — the mushabbah begins.", "«… kimseyi» — müşebbeh başlar."),
  tok("لَا","la-nafiya","part",[G], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يَحْصُلُ","hasala","verb",[G,"jumla-sifa","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةٌ.", "«gets» — the sila.", "«elde eder» — sıla."),
  tok("مِنْ","min","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("سَعْيِهِ","say","noun",[G,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«his striving» — the returning pronoun.", "«çabasından» — âid.",
      segments=[seg("سَعْيِ","say","noun"), seg("هِ","pron-3ms","pron")]),
  tok("عَلَى","ala","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ — حَصَلَ عَلَى: نَالَ.", "«on» — حَصَلَ عَلَى = to obtain.", "«-e» — حَصَلَ عَلَى = elde etmek."),
  tok("طَائِلٍ","tail","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ — طَائِلٌ: فَائِدَةٌ.", "«anything of use» — the mushabbah ends: a composite state.", "«bir fayda» — müşebbeh biter: mürekkeb bir hâl."),
  tok("بِمَنْ","man-mawsul","pron",[G,A,"huruf-jarr","ism-mawsul"],
      "الْبَاءُ جَارَّةٌ، وَمَنْ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — الْمُشَبَّهُ بِهِ يَبْدَأُ.", "«to one who» — the bihi begins: the بِ on a relative.", "«… kimseye» — bih başlar: mevsûl üstünde بِ.",
      segments=[seg("بِ","bi","part"), seg("مَنْ","man-mawsul","pron")]),
  tok("يَرْقُمُ","raqama","verb",[G,"jumla-sifa","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«writes» — the sila.", "«yazar» — sıla."),
  tok("عَلَى","ala","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  tok("الْمَاءِ","ma-water","noun",[G,"huruf-jarr"],
      "اسْمٌ مَجْرُورٌ. الْغَرَضُ: تَقْرِيرُ حَالِ الْمُشَبَّهِ — الْمُشَبَّهُ بِهِ أَتَمُّ وَأَشْهَرُ فِي الْوَجْهِ.",
      "«water» — the aim (4): to SETTLE the mushabbah's state by a bihi where the wajh is plainer and more famous.",
      "«su» — gaye (4): müşebbehin hâlini, vechin daha açık ve meşhur olduğu bir bihle KARARA BAĞLAMAK.",
      punct=".")]})

# ----------- s14 — adorning (RESTORED)
S.append({"id": "s14", "translation": {
 "en": "And as in likening a black face to the eye of the gazelle, to adorn it." + R_EN,
 "tr": "Ve siyah bir yüzü ceylanın gözüne benzetmek gibi — onu süslemek için." + R_TR},
 "tashbih": frame([1, 2], 0, [3, 4], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("وَكَتَشْبِيهِ","tashbih","noun",[G,A,"huruf-jarr","imal-al-masdar"], "مَعْطُوفٌ — الْكَافُ لِلتَّمْثِيلِ، وَتَشْبِيهِ مُضَافٌ: الْأَدَاةُ.", "«and as in likening» — the masdar-adat.", "«ve … benzetmek gibi» — masdar-edat.",
      segments=[seg("وَ","wa","conj"), seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("وَجْهٍ","wajh","noun",[G,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«a face» — the mushabbah.", "«bir yüzü» — müşebbeh."),
  tok("أَسْوَدَ","aswad","noun",[G,"naat-sifa","mamnu-min-sarf"],
      "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — أَفْعَلُ اللَّوْنِ.",
      "«black» — its na't, a colour-أَفْعَل: diptote, jarr by fatha.", "«siyah» — sıfatı, renk أَفْعَل'i: gayr-i munsarif, cerri fethayla."),
  tok("بِمُقْلَةِ","muqla","noun",[G,A,"huruf-jarr","idafa-definiteness"], "الْبَاءُ جَارَّةٌ وَمُقْلَةِ مَجْرُورٌ مُضَافٌ — الْمُشَبَّهُ بِهِ.", "«to the eye of» — the bihi.", "«gözüne» — bih.",
      segments=[seg("بِ","bi","part"), seg("مُقْلَةِ","muqla","noun")]),
  tok("الظَّبْيِ","zaby","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the gazelle» — whose black eye is beauty itself.", "«ceylanın» — kara gözü güzelliğin kendisi."),
  tok("لِتَزْيِينِهِ","tazyin","noun",[G,"huruf-jarr","lam-taleel","masdar"],
      "اللَّامُ لِلتَّعْلِيلِ، وَتَزْيِينِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْغَرَضُ الْخَامِسُ.", "«to adorn it» — the aim (5).", "«süslemek için» — gaye (5).",
      segments=[seg("لِ","li","part"), seg("تَزْيِينِ","tazyin","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s15 — novelty: the coal (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "And as in likening coal with lit embers in it to a sea of musk whose waves are gold." + R_EN,
 "tr": "Ve içinde yanan korlar bulunan kömürü, dalgası altın olan bir misk denizine benzetmek gibi." + R_TR},
 "tashbih": frame([1, 2, 3, 4], 0, [5, 6, 7, 8, 9], [], "mursal-mujmal", "murakkab", "murakkab", None),
 "tokens": [
  tok("وَكَتَشْبِيهِ","tashbih","noun",[G,A,"huruf-jarr","imal-al-masdar"], "مَعْطُوفٌ — الْأَدَاةُ.", "«and as in likening» — the masdar-adat.", "«ve … benzetmek gibi» — masdar-edat.",
      segments=[seg("وَ","wa","conj"), seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("فَحْمٍ","fahm-coal","noun",[G,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ، وَتَصِفُهُ الْجُمْلَةُ بَعْدَهُ.", "«coal» — the mushabbah, described by the clause after it.", "«kömürü» — müşebbeh, ardındaki cümle onu vasfeder."),
  tok("فِيهِ","fi","part",[G,"jumla-sifa","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ، وَالْهَاءُ الْعَائِدُ — وَالْجُمْلَةُ الِاسْمِيَّةُ صِفَةٌ لِفَحْمٍ.",
      "«in it» — a fronted khabar; the ha returns to the coal: a NOMINAL describing clause, and the mushabbah is a picture.",
      "«içinde» — mukaddem haber; hâ kömüre döner: İSİM cümlesi sıfat, müşebbeh bir tablo.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("جَمْرٌ","jamr","noun",[G,"mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«embers» — the delayed mubtada.", "«korlar» — muahhar mübtedâ."),
  tok("مُوقَدٌ","muqad","noun",[G,"naat-sifa","ism-maful","form-iv-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ أَوْقَدَ.", "«lit» — its na't; the ism maf'ul of أَوْقَدَ.", "«yanan» — sıfatı; أَوْقَدَ'nin ism-i mef'ûlü."),
  tok("بِبَحْرٍ","bahr","noun",[G,A,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَبَحْرٍ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to a sea» — the bihi begins.", "«bir denize» — bih başlar.",
      segments=[seg("بِ","bi","part"), seg("بَحْرٍ","bahr","noun")]),
  tok("مِنَ","min","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of» — the min of explanation.", "«-den» — beyan mini."),
  tok("الْمِسْكِ","misk","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ صِفَةٌ لِبَحْرٍ.", "«musk» — a sea made of musk (black).", "«miskten» — miskten (siyah) bir deniz."),
  tok("مَوْجُهُ","mawj","noun",[G,"mubtada-khabar","jumla-sifa","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ عَائِدٌ إِلَى بَحْرٍ — وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ.",
      "«whose waves» — a nominal clause describing the sea; the ha returns to it: the bihi too is a picture.",
      "«dalgası» — denizi vasfeden isim cümlesi; hâ ona döner: bih de bir tablo.",
      segments=[seg("مَوْجُ","mawj","noun"), seg("هُ","pron-3ms","pron")]),
  tok("الذَّهَبُ","dhahab-gold","noun",[G,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ. الْغَرَضُ: الِاسْتِطْرَافُ — إِبْرَازُ الْمُشَبَّهِ فِي صُورَةِ الْمُمْتَنِعِ عَادَةً.",
      "«gold» — the khabar. The aim (7): NOVELTY, showing the mushabbah in a shape that custom holds impossible (a sea of musk with golden waves).",
      "«altındır» — haber. Gaye (7): İSTİTRÂF, müşebbehi âdeten imkânsız bir surette göstermek (altın dalgalı misk denizi).",
      punct=".")]})

# ----------- s16 — Abu l-ʿAtahiya, first bayt (as printed; وَلاَ زِوَرْدِيَّةٍ → وَلَازَوَرْدِيَّةٍ)
S.append({"id": "s16", "translation": {
 "en": "«Many a lazuline (violet) that flaunts its blue among the gardens over the red of the rubies —»",
 "tr": "«Nice lâcivert (menekşe) ki bahçeler arasında, yakutların kızılı üstünde maviliğiyle böbürlenir —»"},
 "tokens": [
  tok("وَلَازَوَرْدِيَّةٍ","lazawardiyya","noun",[G,"anwa-al-waw","huruf-jarr-nawadir","ism-mansub"],
      "الْوَاوُ وَاوُ رُبَّ، وَلَازَوَرْدِيَّةٍ مَجْرُورٌ لَفْظًا بِرُبَّ الْمَحْذُوفَةِ، مَرْفُوعٌ مَحَلًّا مُبْتَدَأٌ — وَالتَّقْدِيرُ: رُبَّ أَزْهَارٍ لَازَوَرْدِيَّةٍ. (يَكْتُبُهُ الْمَصْدَرُ وَلاَ زِوَرْدِيَّةٍ.)",
      "«many a lazuline (flower)» — the WAW OF رُبَّ: the noun is majrur by the dropped رُبَّ and a mubtada in place; a nisba to lazuward, the blue stone (the source writes وَلاَ زِوَرْدِيَّةٍ).",
      "«nice lâcivert (çiçek)» — RUBBE VÂVI: isim düşmüş رُبَّ ile lafzen mecrur, mahallen merfû mübtedâ; mavi taş lâciverde nisbet (kaynak وَلاَ زِوَرْدِيَّةٍ yazar).",
      segments=[seg("وَ","wa","conj"), seg("لَازَوَرْدِيَّةٍ","lazawardiyya","noun")]),
  tok("تَزْهُو","zaha","verb",[G,"jumla-sifa","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ صِفَةٌ لِلْمَجْرُورِ بِرُبَّ.",
      "«flaunts» — a naqis-waw mudari (زَهَا يَزْهُو); the clause describes the noun after رُبَّ, as رُبَّ always wants.",
      "«böbürlenir» — nâkıs-vâvî muzâri (زَهَا يَزْهُو); cümle رُبَّ'den sonraki ismi vasfeder, رُبَّ hep bunu ister."),
  tok("بِزُرْقَتِهَا","zurqa","noun",[G,"huruf-jarr","idafa-definiteness"], "الْبَاءُ جَارَّةٌ وَزُرْقَةِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«with its blue».", "«maviliğiyle».",
      segments=[seg("بِ","bi","part"), seg("زُرْقَةِ","zurqa","noun"), seg("هَا","pron-3fs","pron")]),
  tok("بَيْنَ","bayna","noun",[G,"maful-fih","idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُضَافٌ.", "«among».", "«arasında»."),
  tok("الرِّيَاضِ","rawda","noun",[G,"idafa-definiteness","jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ رَوْضَةٍ.", "«the gardens» — plural of رَوْضَة.", "«bahçelerin» — رَوْضَة'nin çoğulu."),
  tok("عَلَى","ala","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«üstünde»."),
  tok("حُمْرِ","ahmar","noun",[G,"huruf-jarr","idafa-definiteness","jam-taksir"], "اسْمٌ مَجْرُورٌ مُضَافٌ — جَمْعُ أَحْمَرَ عَلَى فُعْلٍ.", "«the red (ones) of» — the colour plural فُعْل of أَحْمَر.", "«kızılları» — أَحْمَر'in فُعْل renk çoğulu."),
  tok("الْيَوَاقِيتِ","yaqut","noun",[G,"idafa-definiteness","jam-taksir","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ يَاقُوتٍ عَلَى فَعَالِيلَ، صِيغَةُ مُنْتَهَى الْجُمُوعِ؛ الْأَلِفُ وَاللَّامُ تُعِيدَانِ الْكَسْرَةَ.",
      "«the rubies» — a heaviest-shape plural (فَعَالِيل); the article gives back its kasra. The likening waits for the next bayt.",
      "«yakutların» — en ağır kalıp çoğul (فَعَالِيل); harf-i tarif kesrayı geri verir. Benzetme sonraki beyti bekler.",
      punct=".")]})

# ----------- s17 — the second bayt: كَأَنَّهَا (as printed; كِبْرِيتِ with the rhyme's bare kasra)
S.append({"id": "s17", "translation": {
 "en": "«— as if they were, upon stalks that they have weighed down, the first flames of fire at the tips of matches.»",
 "tr": "«— sanki onlar, kendileriyle bükülen sapların üstünde, kibrit uçlarındaki ilk ateşlerdir.»"},
 "tashbih": {"mushabbah": [], "adat": 0, "bihi": [5, 6, 7, 8, 9], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": None, "bihi": "muqayyad", "wajh": None}},
 "tokens": [
  tok("كَأَنَّهَا","ka-anna","part",[G,A,"inna-wa-akhawatuha","tashbih"],
      "حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَهَا اسْمُهَا فِي مَحَلِّ نَصْبٍ — الْمُشَبَّهُ ضَمِيرُ اللَّازَوَرْدِيَّةِ.",
      "«as if they» — the adat with its ism attached: the MUSHABBAH is the pronoun of the violets.",
      "«sanki onlar» — ismi bitişik edat: MÜŞEBBEH menekşelerin zamiri.",
      segments=[seg("كَأَنَّ","ka-anna","part"), seg("هَا","pron-3fs","pron")]),
  tok("فَوْقَ","fawqa","noun",[G,"maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُضَافٌ، مُتَعَلِّقٌ بِالْخَبَرِ — لَيْسَ الْخَبَرَ: الْخَبَرُ أَوَائِلُ.",
      "«upon» — a zarf hanging on the khabar, not the khabar itself: the engine prefers the plain noun أَوَائِلُ.",
      "«üstünde» — habere bağlı zarf, haberin kendisi değil: motor açık isim أَوَائِلُ'i tercih eder."),
  tok("قَامَاتٍ","qama-stalk","noun",[G,"idafa-definiteness","jam-muannath-salim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ: قَامَاتٌ، الْقَامَةُ: السَّاقُ.",
      "«stalks» — a sound feminine plural in jarr (قَامَة: the stalk's stature).", "«sapların» — mecrur cem-i müennes-i sâlim (قَامَة: boy, sap)."),
  tok("ضَعُفْنَ","daufa","verb",[G,"jumla-sifa","thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ مِنْ بَابِ كَرُمَ، وَنُونُ النِّسْوَةِ فَاعِلٌ — وَالْجُمْلَةُ صِفَةٌ لِقَامَاتٍ.",
      "«that have grown weak» — فَعُلَ of the fifth bab with the nun of women (the stalks are feminine plural); a describing clause on قَامَاتٍ.",
      "«zayıflamış» — beşinci bâbdan فَعُلَ, nisve nûnuyla (saplar müennes çoğul); قَامَاتٍ'in vasıf cümlesi."),
  tok("بِهَا","bi","part",[G,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — وَهَا لِلَّازَوَرْدِيَّةِ: ضَعُفَتِ الْقَامَاتُ بِثِقَلِ الْأَزْهَارِ.", "«by them» — weighed down by the flowers.", "«onlarla» — çiçeklerin ağırlığıyla.",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("أَوَائِلُ","awail","noun",[G,A,"inna-wa-akhawatuha","idafa-definiteness","jam-taksir","mamnu-min-sarf"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ أُولَى/أَوَّل عَلَى فَوَاعِلَ، صِيغَةُ مُنْتَهَى الْجُمُوعِ. الْمُشَبَّهُ بِهِ.",
      "«the first (flames) of» — the khabar: the MUSHABBAH BIHI, a heaviest-shape plural annexed.",
      "«ilkleri» — haber: MÜŞEBBEHÜN BİH, en ağır kalıpta çoğul, muzâf."),
  tok("النَّارِ","nar","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«fire».", "«ateşin»."),
  tok("فِي","fi","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ — قَيْدٌ عَلَى الْمُشَبَّهِ بِهِ لَا وَجْهُ شَبَهٍ.", "«at» — a RESTRICTION on the bihi (its place), not a wajh.", "«-de» — bih üzerinde KAYIT (yeri), vech değil."),
  tok("أَطْرَافِ","taraf","noun",[G,"huruf-jarr","idafa-definiteness","jam-taksir"], "اسْمٌ مَجْرُورٌ مُضَافٌ — جَمْعُ طَرَفٍ.", "«the tips of».", "«uçlarında»."),
  tok("كِبْرِيتِ","kibrit","noun",[G,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ (كِبْرِيتٍ). الْغَرَضُ: الِاسْتِطْرَافُ — نُدْرَةُ حُضُورِ الْمُشَبَّهِ بِهِ عِنْدَ حُضُورِ الْمُشَبَّهِ.",
      "«matches» — its tanwin dropped for the rhyme. The aim (7) again: the bihi is one that seldom comes to mind when the violets are before us — novelty by rarity.",
      "«kibritin» — tenvini kafiye için düşmüş. Gaye (7) yine: menekşeler önümüzdeyken bih nadiren akla gelir — nadirlikle istitrâf.",
      punct=".")]})

# ----------- s18 — the aims that return to the bihi: the reversed tashbih (RESTORED)
S.append({"id": "s18", "translation": {
 "en": "The aim that returns to the mushabbah bihi is to suggest that it is the more complete — and that is in the reversed tashbih." + R_EN,
 "tr": "Müşebbehün bihe dönen gaye, onun daha tam olduğunu ihsas ettirmektir — bu, maklûb teşbihte olur." + R_TR},
 "tokens": [
  tok("وَالْغَرَضُ","gharad","noun",[G,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْغَرَضُ مُبْتَدَأٌ.", "«the aim» — the mubtada.", "«gaye» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْغَرَضُ","gharad","noun")]),
  tok("الْعَائِدُ","aid","noun",[G,"naat-sifa","ism-fail","hollow-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ عَادَ، هَمْزَتُهُ مُنْقَلِبَةٌ عَنِ الْوَاوِ.", "«that returns» — the ism fa'il of the hollow عَادَ: its waw became a hamza.", "«dönen» — ecvef عَادَ'nin ism-i fâili: vâvı hemzeye dönmüş."),
  tok("إِلَى","ila","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[G,A,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the mushabbah».", "«müşebbeh»."),
  tok("بِهِ","bi","part",[G,A,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — تَمَامُ الْمُصْطَلَحِ.", "«bihi».", "«bih».",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("إِيهَامُ","iham","noun",[G,"mubtada-khabar","idafa-definiteness","masdar","form-iv-verbs"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ — مَصْدَرُ أَوْهَمَ.", "«suggesting» — the khabar; the masdar of أَوْهَمَ.", "«ihsas ettirmek» — haber; أَوْهَمَ'nin masdarı."),
  tok("أَنَّهُ","anna","part",[G,"inna-wa-akhawatuha","an-masdariyya"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مُضَافٌ إِلَيْهِ.", "«that it» — أَنَّ with its ism; the clause is the mudaf ilayh.", "«onun» — ismi bitişik أَنَّ; cümle muzâfun ileyh.",
      segments=[seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("أَتَمُّ","atamm","noun",[G,"inna-wa-akhawatuha","ism-tafdil","mamnu-min-sarf"],
      "خَبَرُ أَنَّ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ مِنَ الْمُضَاعَفِ (أَتْمَمُ → أَتَمُّ)، مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "«more complete» — the khabar of أَنَّ; an ism tafdil of a geminate root (أَتْمَمُ → أَتَمُّ), diptote.",
      "«daha tam» — أَنَّ'nin haberi; muzâaf kökten ism-i tafdil (أَتْمَمُ → أَتَمُّ), gayr-i munsarif.", punct="،"),
  tok("وَذَٰلِكَ","dhalika","pron",[G,"asma-al-ishara","mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَٰلِكَ مُبْتَدَأٌ.", "«and that» — the mubtada.", "«ve bu» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("ذَٰلِكَ","dhalika","pron")]),
  tok("فِي","fi","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the khabar-phrase.", "«-de» — haber tamlaması."),
  tok("التَّشْبِيهِ","tashbih","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the tashbih».", "«teşbih»."),
  tok("الْمَقْلُوبِ","maqlub","noun",[G,"naat-sifa","ism-maful"],
      "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ قَلَبَ: جُعِلَ الْمُشَبَّهُ مُشَبَّهًا بِهِ.",
      "«reversed» — the ism maf'ul of قَلَبَ: the natural mushabbah is made the bihi, claiming the other outdoes it.",
      "«maklûb» — قَلَبَ'nin ism-i mef'ûlü: tabiî müşebbeh bih yapılmış, öteki onu geçer iddiasıyla.",
      punct=".")]})

# ----------- s19 — Muhammad b. Wuhayb: the reversed tashbih (as printed)
S.append({"id": "s19", "translation": {
 "en": "«And the morning appeared, as if its brightness were the Caliph's face when he is praised.»",
 "tr": "«Ve sabah belirdi; sanki onun ağarması, övüldüğü andaki halifenin yüzüdür.»"},
 "tashbih": frame([3], 2, [4, 5, 6, 7], [], "mursal-mujmal", "mufrad", "muqayyad", None),
 "tokens": [
  tok("وَبَدَا","bada-appear","verb",[G,"naqis-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَبَدَا فِعْلٌ مَاضٍ نَاقِصٌ وَاوِيٌّ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ.", "«and appeared» — بَدَا يَبْدُو, a naqis-waw mazi.", "«ve belirdi» — بَدَا يَبْدُو, nâkıs-vâvî mâzî.",
      segments=[seg("وَ","wa","conj"), seg("بَدَا","bada-appear","verb")]),
  tok("الصَّبَاحُ","sabah","noun",[G,"fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the morning» — the fa'il.", "«sabah» — fâil."),
  tok("كَأَنَّ","ka-anna","part",[G,A,"inna-wa-akhawatuha","tashbih"], "حَرْفُ تَشْبِيهٍ وَنَصْبٍ — وَالْجُمْلَةُ حَالٌ مِنَ الصَّبَاحِ.", "«as if» — the adat; the clause is a hal of the morning.", "«sanki» — edat; cümle sabahtan hâl."),
  tok("غُرَّتَهُ","ghurra","noun",[G,A,"inna-wa-akhawatuha","idafa-definiteness"],
      "اسْمُ كَأَنَّ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْمُشَبَّهُ: بَيَاضُ الصَّبَاحِ. وَهُوَ فِي الْحَقِيقَةِ الْأَتَمُّ فِي الْبَيَاضِ.",
      "«its brightness» — the ism: the MUSHABBAH (the morning's white blaze) — which is in truth the more complete in whiteness: the tashbih is REVERSED to claim the Caliph's face outshines it.",
      "«ağarması» — ism: MÜŞEBBEH (sabahın beyazlığı) — aslında beyazlıkta daha tam olan odur: teşbih TERS ÇEVRİLMİŞ, halifenin yüzünün onu geçtiği iddiasıyla.",
      segments=[seg("غُرَّتَ","ghurra","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَجْهُ","wajh","noun",[G,A,"inna-wa-akhawatuha","idafa-definiteness"], "خَبَرُ كَأَنَّ مَرْفُوعٌ مُضَافٌ — الْمُشَبَّهُ بِهِ.", "«the face of» — the khabar: the MUSHABBAH BIHI.", "«yüzü» — haber: MÜŞEBBEHÜN BİH."),
  tok("الْخَلِيفَةِ","khalifa","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Caliph» — al-Ma'mun.", "«halifenin» — Me'mûn."),
  tok("حِينَ","hin","noun",[G,"maful-fih","idafa-definiteness"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ إِلَى الْجُمْلَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنَ الْوَجْهِ — قَيْدٌ عَلَى الْمُشَبَّهِ بِهِ.",
      "«when» — a zarf annexed to the clause, restricting the face: the bihi is MUQAYYAD (his face as he is praised, glowing with pleasure).",
      "«-diği anda» — cümleye muzâf zarf, yüzü kayıtlar: bih MUKAYYEDdir (övülürken sevinçle parlayan yüzü)."),
  tok("يُمْتَدَحُ","imtadaha","verb",[G,"naib-al-fail","form-viii-verbs","idafa-definiteness"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«he is praised» — Form VIII majhul; the clause is the mudaf ilayh of حِينَ. A verb inside the rukn, yet held by the zarf: a restriction, not a picture.",
      "«övülür» — VIII. bâb meçhul; cümle حِينَ'nin muzâfun ileyhi. Rükün içinde fiil var, fakat zarf onu tutar: kayıt, tablo değil.",
      punct=".")]})

# ----------- s20 — the second aim of the bihi: caring for it (RESTORED)
S.append({"id": "s20", "translation": {
 "en": "The second is to show one's concern for it — as in the hungry man likening a face like the full moon to a loaf." + R_EN,
 "tr": "İkincisi ona verilen ehemmiyeti göstermektir — açın, dolunay gibi bir yüzü ekmeğe benzetmesi gibi." + R_TR},
 "tashbih": frame([6], 4, [8], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("وَالثَّانِي","thani","noun",[G,"mubtada-khabar","ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«the second» — the mubtada, a manqus with the article.", "«ikincisi» — mübtedâ, harf-i tarifli mankûs.",
      segments=[seg("وَ","wa","conj"), seg("الثَّانِي","thani","noun")]),
  tok("بَيَانُ","bayan","noun",[G,"mubtada-khabar","idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«showing».", "«göstermek»."),
  tok("الِاهْتِمَامِ","ihtimam","noun",[G,"idafa-definiteness","masdar","form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اهْتَمَّ، مُضَاعَفٌ.", "«concern» — the masdar of اِهْتَمَّ (Form VIII, geminate).", "«ehemmiyet vermek» — اِهْتَمَّ'nin masdarı (VIII. bâb, muzâaf)."),
  tok("بِهِ","bi","part",[G,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالِاهْتِمَامِ — وَالْهَاءُ لِلْمُشَبَّهِ بِهِ.", "«for it» — for the bihi (the loaf).", "«ona» — bihe (ekmeğe).",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("كَتَشْبِيهِ","tashbih","noun",[G,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "الْكَافُ لِلتَّمْثِيلِ، وَتَشْبِيهِ مَجْرُورٌ مُضَافٌ إِلَى فَاعِلِهِ — الْأَدَاةُ.",
      "«as in the likening (by)» — the masdar-adat, annexed to its FA'IL this time: the hungry man does the likening.",
      "«benzetmesi gibi» — masdar-edat, bu kez FÂİLİNE muzâf: benzetmeyi aç yapar.",
      segments=[seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("الْجَائِعِ","jai","noun",[G,"idafa-definiteness","ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلُ الْمَصْدَرِ.", "«the hungry man» — the masdar's fa'il.", "«açın» — masdarın fâili."),
  tok("وَجْهًا","wajh","noun",[G,A,"maful-bihi","imal-al-masdar"],
      "مَفْعُولُ الْمَصْدَرِ مَنْصُوبٌ — الْمُشَبَّهُ: الْمَصْدَرُ الْمُضَافُ إِلَى فَاعِلِهِ يَنْصِبُ مَفْعُولَهُ.",
      "«a face» — the masdar's OBJECT in nasb: the MUSHABBAH. Annexed to its fa'il, the masdar still governs its object.",
      "«bir yüzü» — masdarın nasbdaki MEF'ÛLÜ: MÜŞEBBEH. Fâiline muzâf masdar, mef'ûlünü yine nasb eder."),
  tok("كَالْبَدْرِ","badr","noun",[G,A,"naat-sifa","huruf-jarr","tashbih"],
      "الْكَافُ جَارَّةٌ وَالْبَدْرِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِوَجْهًا: تَشْبِيهٌ دَاخِلَ التَّشْبِيهِ.",
      "«like the full moon» — a kaf-phrase describing the face: a likening INSIDE the likening — and the face is still likened to a loaf.",
      "«dolunay gibi» — yüzü vasfeden kâf tamlaması: teşbih İÇİNDE teşbih — ve yüz yine ekmeğe benzetilir.",
      segments=[seg("كَ","ka","part"), seg("الْبَدْرِ","badr","noun")]),
  tok("بِالرَّغِيفِ","raghif","noun",[G,A,"huruf-jarr","tashbih"],
      "الْبَاءُ جَارَّةٌ وَالرَّغِيفِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ: الرَّغِيفُ أَهَمُّ عِنْدَ الْجَائِعِ مِنَ الْبَدْرِ.",
      "«to a loaf» — the bihi: to the hungry, the loaf matters more than the moon — the tashbih says what he cares about.",
      "«ekmeğe» — bih: aç için ekmek aydan mühimdir — teşbih neye önem verdiğini söyler.",
      segments=[seg("بِ","bi","part"), seg("الرَّغِيفِ","raghif","noun")], punct=".")]})

# ----------- s21 — tashabuh instead of tashbih (RESTORED)
S.append({"id": "s21", "translation": {
 "en": "And when the joining of two things in one matter is intended, it is better to leave tashbih for the judgement of tashabuh (mutual likeness)." + R_EN,
 "tr": "İki şeyi bir hususta birleştirmek murad edilince, en güzeli teşbihi bırakıp teşâbühle (karşılıklı benzeşmeyle) hükmetmektir." + R_TR},
 "tokens": [
  tok("وَإِذَا","idha","part",[G,"idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the conditional إِذَا.", "«ve … -ınca» — şart إِذَا'sı.",
      segments=[seg("وَ","wa","conj"), seg("إِذَا","idha","part")]),
  tok("أُرِيدَ","arada","verb",[G,"naib-al-fail","hollow-verbs","form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ: أُرِيدَ.", "«is intended» — the hollow Form IV in the majhul.", "«murad edilirse» — ecvef IV. bâb meçhul."),
  tok("الْجَمْعُ","jam-gathering","noun",[G,"naib-al-fail","masdar"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — مَصْدَرُ جَمَعَ.", "«the joining» — the deputy fa'il.", "«birleştirmek» — nâib-i fâil."),
  tok("بَيْنَ","bayna","noun",[G,"maful-fih","idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«between».", "«arasını»."),
  tok("شَيْئَيْنِ","shay","noun",[G,"al-muthanna","idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two things» — a dual in jarr.", "«iki şey» — mecrur tesniye."),
  tok("فِي","fi","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("أَمْرٍ","amr","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«a matter» — one shared quality.", "«bir husus» — bir ortak vasıf."),
  tok("فَالْأَحْسَنُ","ahsan","noun",[G,"mubtada-khabar","ism-tafdil","idha-shartiyya"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ إِذَا، وَالْأَحْسَنُ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«the better (course)» — the fa binds the answer; an ism tafdil as mubtada.", "«en güzeli» — fâ cevabı bağlar; ism-i tafdil mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْأَحْسَنُ","ahsan","noun")]),
  tok("تَرْكُ","tark","noun",[G,"mubtada-khabar","idafa-definiteness","masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ.", "«leaving» — the khabar.", "«bırakmak» — haber."),
  tok("التَّشْبِيهِ","tashbih","noun",[G,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«tashbih» — which ranks one end over the other.", "«teşbihi» — bir tarafı ötekine üstün kılan."),
  tok("إِلَى","ila","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ — تَرَكَ كَذَا إِلَى كَذَا: عَدَلَ عَنْهُ إِلَيْهِ.", "«for» — تَرَكَ … إِلَى: to turn from one to the other.", "«-e» — تَرَكَ … إِلَى: birinden ötekine dönmek."),
  tok("الْحُكْمِ","hukm","noun",[G,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ.", "«the judgement».", "«hükmetmeye»."),
  tok("بِالتَّشَابُهِ","tashabuh","noun",[G,A,"huruf-jarr","masdar","form-vi-verbs"],
      "الْبَاءُ جَارَّةٌ وَالتَّشَابُهِ مَجْرُورٌ — مَصْدَرُ تَشَابَهَ: التَّمَاثُلُ مِنَ الْجَانِبَيْنِ، لَا مُشَبَّهَ وَلَا مُشَبَّهَ بِهِ.",
      "«of tashabuh» — the masdar of Form VI: likeness from BOTH sides, with no mushabbah and no bihi ranked.",
      "«teşâbühle» — VI. bâbın masdarı: İKİ taraftan benzeşme, sıralanmış müşebbeh ve bih yok.",
      segments=[seg("بِ","bi","part"), seg("التَّشَابُهِ","tashabuh","noun")], punct=".")]})

# ----------- s22 — Abu Ishaq's bayt (as printed; عَيْنَىَّ → عَيْنِي, see the module note)
S.append({"id": "s22", "translation": {
 "en": "«My tears, as they ran, and my wine came to resemble each other: so from the like of what is in the cup my eye pours.»",
 "tr": "«Gözyaşım akarken, o ve şarabım birbirine benzedi: kadehtekinin bir mislini gözüm döküyor.»"},
 "tashbih": {"mushabbah": [1], "adat": 0, "bihi": [4], "wajh": [], "kind": "tashabuh",
             "shape": {"mushabbah": "mufrad", "bihi": "mufrad", "wajh": None}},
 "tokens": [
  tok("تَشَابَهَ","tashabaha","verb",[G,A,"form-vi-verbs","tashbih"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — فِعْلُ الْمُشَارَكَةِ: يَطْلُبُ فَاعِلَيْنِ مُتَعَاطِفَيْنِ. وَهُوَ أَدَاةُ الْحُكْمِ بِالتَّشَابُهِ.",
      "«came to resemble each other» — Form VI, the verb of MUTUAL action: it wants two joined fa'ils. The engine reads it as the tashabuh frame: two ends, no direction.",
      "«birbirine benzedi» — VI. bâb, MÜŞÂREKET fiili: iki atıflı fâil ister. Motor bunu teşâbüh çerçevesi okur: iki taraf, yön yok."),
  tok("دَمْعِي","dam-tear","noun",[G,A,"fail","ya-al-mutakallim"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِكَسْرَةِ الْمُنَاسَبَةِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — الطَّرَفُ الْأَوَّلُ.",
      "«my tears» — the first fa'il, its damma hidden by the speaker's ya: the FIRST end.", "«gözyaşım» — ilk fâil, dammesi mütekellim yâsıyla gizli: İLK taraf.",
      segments=[seg("دَمْعِ","dam-tear","noun"), seg("ي","pron-1s","pron")]),
  tok("إِذْ","idh","noun",[G,"maful-fih"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مُضَافٌ إِلَى الْجُمْلَةِ.", "«as, when» — the zarf of past time.", "«-diğinde» — geçmiş zaman zarfı."),
  tok("جَرَى","jara","verb",[G,"naqis-verbs","idafa-definiteness"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهِ.", "«it ran» — the clause annexed to إِذْ.", "«aktı» — إِذْ'e muzâf cümle."),
  tok("وَمُدَامَتِي","mudama","noun",[G,A,"atf-nasaq","ya-al-mutakallim"],
      "مَعْطُوفٌ عَلَى دَمْعِي مَرْفُوعٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — الطَّرَفُ الثَّانِي.",
      "«and my wine» — joined to the first fa'il: the SECOND end. Neither is «likened to» the other.", "«ve şarabım» — ilk fâile atıf: İKİNCİ taraf. Hiçbiri ötekine «benzetilmiş» değil.",
      segments=[seg("وَ","wa","conj"), seg("مُدَامَتِ","mudama","noun"), seg("ي","pron-1s","pron")]),
  tok("فَمِنْ","min","part",[G,"huruf-jarr"], "الْفَاءُ لِلتَّفْرِيعِ، وَمِنْ حَرْفُ جَرٍّ.", "«so from».", "«artık … -den».",
      segments=[seg("فَ","fa","conj"), seg("مِنْ","min","part")]),
  tok("مِثْلِ","mithl","noun",[G,"huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — لَا أَدَاةَ تَشْبِيهٍ هُنَا: مِثْلُ بَعْدَ حَرْفِ جَرٍّ اسْمٌ لِلْمِقْدَارِ.",
      "«the like of» — not an adat here: after a jarr-particle مِثْل is a plain noun (a like amount); the engine refuses a frame.",
      "«mislini» — burada edat değil: cer harfinden sonra مِثْل düz isimdir (bir misli); motor çerçeveyi reddeder."),
  tok("مَا","ma-mawsula","pron",[G,"ism-mawsul","idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what».", "«-in»."),
  tok("فِي","fi","part",[G,"huruf-jarr"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«in» — the sila.", "«-deki» — sıla."),
  tok("الْكَأْسِ","kas","noun",[G,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the cup».", "«kadeh»."),
  tok("عَيْنِي","ayn-eye","noun",[G,"fail","ya-al-mutakallim"],
      "فَاعِلٌ مُقَدَّمٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — (يَكْتُبُهُ الْمَصْدَرُ عَيْنَىَّ.)",
      "«my eye» — the fa'il of the verb after it (the source prints عَيْنَىَّ; its own Turkish makes the eyes the subject, and the app writes عَيْنِي).",
      "«gözüm» — ardındaki fiilin fâili (kaynak عَيْنَىَّ yazar; kendi Türkçesi gözleri özne yapar, uygulama عَيْنِي yazar).",
      segments=[seg("عَيْنِ","ayn-eye","noun"), seg("ي","pron-1s","pron")]),
  tok("تَسْكُبُ","sakaba","verb",[G,"mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ عَيْنِي الْمُتَقَدِّمُ — فِي الشِّعْرِ يَتَقَدَّمُ الْفَاعِلُ عَلَى فِعْلِهِ لَفْظًا وَهُوَ مُبْتَدَأٌ عِنْدَ الْبَصْرِيِّينَ.",
      "«pours» — the verb whose doer stands before it (for the Basrans, عَيْنِي is then a mubtada and the clause its khabar).",
      "«döker» — fâili önünde duran fiil (Basralılara göre عَيْنِي o zaman mübtedâ, cümle haberidir).",
      punct=".")],
 "jumal": [J("تَشَابَهَ دَمْعِي … وَمُدَامَتِي", "جُمْلَةٌ فِعْلِيَّةٌ فَاعِلُهَا مُتَعَدِّدٌ — الْحُكْمُ بِالتَّشَابُهِ.",
             "The tashabuh: red tears and red wine judged alike, neither ranked above the other.",
             "Teşâbüh: kızıl gözyaşı ile kızıl şarap benzeşir sayılır, hiçbiri ötekinin üstünde değil.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "kaf-letter": g("الْكَاف", None, "noun", "the letter kaf (named as a noun); the kaf of likening", "kâf harfi (isim olarak); benzetme kâfı", 4),
 "sura-speed": g("سُرْعَة", "س ر ع", "noun", "speed, quickness", "hız, sürat", 3),
 "zawal": g("زَوَال", "ز و ل", "noun", "passing away, ceasing (masdar of زَالَ)", "zevâl, geçip gitme (زَالَ'nin masdarı)", 3),
 "nabat": g("نَبَات", "ن ب ت", "noun", "plants, vegetation", "bitki, nebat", 2),
 "qurb": g("قُرْب", "ق ر ب", "noun", "nearness", "yakınlık", 2),
 "bud-distance": g("بُعْد", "ب ع د", "noun", "distance, farness", "uzaklık", 2),
 "gharad": g("غَرَض", "غ ر ض", "noun", "aim, purpose", "gaye, maksat", 3, plural="أَغْرَاض"),
 "aghlab": g("أَغْلَب", "غ ل ب", "noun", "the most, the greater part (ism tafdil); فِي الْأَغْلَبِ: mostly", "çoğu, ekseri (ism-i tafdil); فِي الْأَغْلَبِ: çoğunlukla", 4),
 "imkan": g("إِمْكَان", "م ك ن", "noun", "possibility (masdar of أَمْكَنَ)", "imkân (أَمْكَنَ'nin masdarı)", 3),
 "tazyin": g("تَزْيِين", "ز ي ن", "noun", "adorning (masdar of زَيَّنَ)", "süsleme (زَيَّنَ'nin masdarı)", 3),
 "tashwih": g("تَشْوِيه", "ش و ه", "noun", "disfiguring, making ugly (masdar of شَوَّهَ)", "çirkinleştirme (شَوَّهَ'nin masdarı)", 4),
 "istitraf": g("اسْتِطْرَاف", "ط ر ف", "noun", "finding novel, counting a thing fresh (masdar of اسْتَطْرَفَ)", "istitrâf, yeni ve hoş sayma (اسْتَطْرَفَ'nin masdarı)", 6),
 "anam-mankind": g("أَنَام", "أ ن م", "noun", "mankind, creatures", "insanlar, halk", 4),
 "dam-blood": g("دَم", "د م ي", "noun", "blood", "kan", 1, plural="دِمَاء"),
 "ghazal": g("غَزَال", "غ ز ل", "noun", "gazelle", "ceylan", 2, plural="غِزْلَان"),
 "mamduh": g("مَمْدُوح", "م د ح", "noun", "the praised one (ism maf'ul of مَدَحَ)", "memdûh, övülen (مَدَحَ'nin ism-i mef'ûlü)", 3),
 "say": g("سَعْي", "س ع ي", "noun", "striving, effort (masdar of سَعَى)", "çaba, sa'y (سَعَى'nın masdarı)", 3),
 "tail": g("طَائِل", "ط و ل", "noun", "benefit, use; لَا طَائِلَ: to no avail", "fayda; لَا طَائِلَ: faydasız", 5),
 "muqla": g("مُقْلَة", "م ق ل", "noun", "the eyeball, the eye", "göz bebeği, göz", 4, plural="مُقَل"),
 "zaby": g("ظَبْي", "ظ ب ي", "noun", "gazelle, antelope", "ceylan, âhû", 3, plural="ظِبَاء"),
 "fahm-coal": g("فَحْم", "ف ح م", "noun", "coal, charcoal", "kömür", 2),
 "jamr": g("جَمْر", "ج م ر", "noun", "embers, live coals", "kor", 3),
 "muqad": g("مُوقَد", "و ق د", "noun", "kindled, lit (ism maf'ul of أَوْقَدَ)", "yakılmış, yanan (أَوْقَدَ'nin ism-i mef'ûlü)", 4),
 "mawj": g("مَوْج", "م و ج", "noun", "waves", "dalga", 2, plural="أَمْوَاج"),
 "dhahab-gold": g("ذَهَب", "ذ ه ب", "noun", "gold", "altın", 1),
 "lazawardiyya": g("لَازَوَرْدِيَّة", None, "noun", "lazuline, lapis-blue (a nisba to لَازَوَرْد, the blue stone; here a violet)", "lâcivert (mavi taş لَازَوَرْد'e nisbet; burada menekşe)", 6),
 "zurqa": g("زُرْقَة", "ز ر ق", "noun", "blueness", "mavilik", 3),
 "rawda": g("رَوْضَة", "ر و ض", "noun", "garden, meadow", "bahçe, ravza", 2, plural="رِيَاض"),
 "ahmar": g("أَحْمَر", "ح م ر", "noun", "red (the colour-أَفْعَل; diptote)", "kızıl, kırmızı (renk أَفْعَل'i; gayr-i munsarif)", 2, plural="حُمْر"),
 "qama-stalk": g("قَامَة", "ق و م", "noun", "stature; a stalk", "boy; sap", 4, plural="قَامَات"),
 "awail": g("أَوَائِل", "أ و ل", "noun", "the first ones, beginnings (plural of أُولَى / أَوَّل; diptote)", "ilkler, başlangıçlar (أُولَى / أَوَّل'in çoğulu; gayr-i munsarif)", 4),
 "kibrit": g("كِبْرِيت", "ك ب ر ت", "noun", "sulphur; a match", "kükürt; kibrit", 3),
 "aid": g("عَائِد", "ع و د", "noun", "returning (ism fa'il of عَادَ)", "dönen (عَادَ'nin ism-i fâili)", 3),
 "atamm": g("أَتَمّ", "ت م م", "noun", "more complete (ism tafdil of تَامّ; diptote)", "daha tam (تَامّ'ın ism-i tafdili; gayr-i munsarif)", 4),
 "maqlub": g("مَقْلُوب", "ق ل ب", "noun", "reversed, inverted (ism maf'ul of قَلَبَ)", "maklûb, ters çevrilmiş (قَلَبَ'nin ism-i mef'ûlü)", 4),
 "ihtimam": g("اهْتِمَام", "ه م م", "noun", "concern, care (masdar of اهْتَمَّ)", "ehemmiyet verme, ihtimam (اهْتَمَّ'nin masdarı)", 4),
 "jai": g("جَائِع", "ج و ع", "noun", "hungry (ism fa'il of جَاعَ)", "aç (جَاعَ'nın ism-i fâili)", 2),
 "badr": g("بَدْر", "ب د ر", "noun", "the full moon", "dolunay", 2, plural="بُدُور"),
 "raghif": g("رَغِيف", "ر غ ف", "noun", "a loaf of bread", "ekmek, somun", 3, plural="أَرْغِفَة"),
 "jam-gathering": g("جَمْع", "ج م ع", "noun", "gathering, joining (masdar of جَمَعَ)", "toplama, birleştirme (جَمَعَ'nin masdarı)", 2),
 "ahsan": g("أَحْسَن", "ح س ن", "noun", "better, best (ism tafdil of حَسَن)", "daha güzel, en güzel (حَسَن'in ism-i tafdili)", 2),
 "tashabuh": g("تَشَابُه", "ش ب ه", "noun", "mutual likeness, resemblance (masdar of تَشَابَهَ)", "teşâbüh, karşılıklı benzeşme (تَشَابَهَ'nin masdarı)", 4),
 "dam-tear": g("دَمْع", "د م ع", "noun", "tears", "gözyaşı", 2, plural="أَدْمُع"),
 "mudama": g("مُدَامَة", "د و م", "noun", "wine (aged)", "eski şarap, müdâme", 5),
 "kas": g("كَأْس", "ك أ س", "noun", "cup, goblet", "kadeh", 2, plural="كُؤُوس"),
 "anbaa": g("أَنْبَأَ", "ن ب أ", "verb", "to tell, inform (Form IV; hamza as last radical)", "haber vermek (IV. bâb; lâmı hemzeli)", 4, form="IV"),
 "hasiba": g("حَسِبَ", "ح س ب", "verb", "to reckon, suppose (a verb of the heart; two objects)", "sanmak, zannetmek (kalp fiili; iki mef'ûl)", 3, form="I"),
 "faqa": g("فَاقَ", "ف و ق", "verb", "to surpass, excel (hollow)", "aşmak, üstün gelmek (ecvef)", 3, form="I"),
 "raqama": g("رَقَمَ", "ر ق م", "verb", "to write, inscribe", "yazmak, nakşetmek", 4, form="I"),
 "zaha": g("زَهَا", "ز ه و", "verb", "to flaunt, be proud; to bloom (naqis-waw)", "böbürlenmek; parlamak (nâkıs-vâvî)", 5, form="I"),
 "daufa": g("ضَعُفَ", "ض ع ف", "verb", "to be weak (the fifth bab)", "zayıf olmak (beşinci bâb)", 2, form="I"),
 "bada-appear": g("بَدَا", "ب د و", "verb", "to appear (naqis-waw)", "belirmek, görünmek (nâkıs-vâvî)", 2, form="I"),
 "imtadaha": g("امْتَدَحَ", "م د ح", "verb", "to praise (Form VIII)", "övmek (VIII. bâb)", 4, form="VIII"),
 "tashabaha": g("تَشَابَهَ", "ش ب ه", "verb", "to resemble one another (Form VI)", "birbirine benzemek (VI. bâb)", 3, form="VI"),
 "sakaba": g("سَكَبَ", "س ك ب", "verb", "to pour", "dökmek", 3, form="I"),
 "dunya": find_gloss("dunya"),
 "anzala": find_gloss("anzala"),
 "qasada": find_gloss("qasada"),
 "hasala": find_gloss("hasala"),
 "bayan": find_gloss("bayan"),
 "taqrir": find_gloss("taqrir"),
 "misk": find_gloss("misk"),
 "bahr": find_gloss("bahr"),
 "sabah": find_gloss("sabah"),
 "hukm": find_gloss("hukm"),
 "ghurab": find_gloss("ghurab"),
}
for k in ("dunya", "hukm"):
    pass

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/49.json").write_text(
    json.dumps({"chapter": 49, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 49 for c in man["chapters"]):
    man["chapters"].append({"n": 49, "title": TITLE49})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.49.0"
ADD_EN = (" Chapter 49 (lines ~3200-3290, sahifa 111-113) carries the adat and the aims of the tashbih: the aya "
          "s3 (18:45; the source writes الْحَيٰوةِ with the dagger alif, the app الْحَيَاةِ), the two examples inside "
          "s6-s7, and the bayts s10, s16-s17, s19 and s22 are Arabic as the source prints it — with three "
          "divergences recorded here: the source writes وَلاَ زِوَرْدِيَّةٍ (s16) where the app writes "
          "وَلَازَوَرْدِيَّةٍ, the received spelling of the word; the source prints كَأَنّ (s19) without the "
          "fatha, the app كَأَنَّ; and the source prints عَيْنَىَّ (s22) where its own Turkish makes the eyes "
          "the subject (gözlerim … döküyor) — the app writes عَيْنِي, the fa'il the printed editions read. "
          "s1-s2, s4-s5, the frames of s6-s7, s8-s9, s11-s15, s18 and s20-s21 are RESTORATIONS, not "
          "quotations: the source carries those steps only in Ottoman-Turkish paraphrase, and the Arabic "
          "restores the matn's wording in the musannif's register; each is marked «restored» in its "
          "translation. Every likening carries an authored `tashbih` frame the engine is tested against — "
          "the verb-of-the-heart frames, the masdar frames whose ends are relatives and nominal clauses, the "
          "reversed tashbih, the tashabuh frame with no direction; the implicit likening of s10 and the كَأَنَّ "
          "named as a word in s1 are authored as no frame.")
ADD_TR = (" Kırk dokuzuncu bâb (satır ~3200-3290, sahife 111-113) teşbih edatını ve gayelerini taşır: s3 "
          "âyeti (18:45; kaynak hançer elifle الْحَيٰوةِ yazar, uygulama الْحَيَاةِ), s6-s7'nin içindeki iki "
          "örnek ve s10, s16-s17, s19, s22 beyitleri kaynağın bastığı Arapçadır — burada kayıtlı üç farkla: "
          "kaynak وَلاَ زِوَرْدِيَّةٍ yazar (s16), uygulama kelimenin yerleşik imlâsı وَلَازَوَرْدِيَّةٍ'i; kaynak "
          "كَأَنّ'i fethasız basar (s19), uygulama كَأَنَّ; kaynak عَيْنَىَّ basar (s22), oysa kendi Türkçesi gözleri "
          "özne yapar (gözlerim … döküyor) — uygulama basılı neşirlerin okuduğu fâili, عَيْنِي, yazar. s1-s2, "
          "s4-s5, s6-s7'nin çerçeveleri, s8-s9, s11-s15, s18 ve s20-s21 ALINTI DEĞİL GERİ YAZIMDIR: kaynak o "
          "adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda "
          "geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Her benzetme, motorun "
          "sınandığı müellif eliyle yazılmış bir `tashbih` çerçevesi taşır — kalp fiili çerçeveleri, tarafları "
          "mevsûl ve isim cümlesi olan masdar çerçeveleri, maklûb teşbih, yönsüz teşâbüh çerçevesi; s10'un "
          "zımnî benzetmesi ile s1'de kelime olarak anılan كَأَنَّ çerçevesiz yazılmıştır.")
if "3200-3290" not in man["attribution"]["en"]:
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
put("anbaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْبَأ", "نْبِئ", "أَنْبِئ", "إِنْبَاء", "مُنْبِئ", "مُنْبَأ", "أُنْبِئَ", "يُنْبَأُ",
                         "مَهْمُوزُ اللَّامِ: تُكْتَبُ الْهَمْزَةُ عَلَى مَا يُنَاسِبُ حَرَكَتَهَا وَحَرَكَةَ مَا قَبْلَهَا — يُنْبِئُ، أَنْبَأَ، أَنْبَؤُوا."))
put("hasiba", _sg.sound1("samia", "حَسِب", "حْسَب", "اِحْسَب", "حُسْبَان", "حَاسِب", "مَحْسُوب", "حُسِبَ", "يُحْسَبُ",
                         "مِنْ أَفْعَالِ الْقُلُوبِ: يَنْصِبُ مَفْعُولَيْنِ — حَسِبْتُ زَيْدًا أَسَدًا؛ وَفِيهِ لُغَةٌ: يَحْسِبُ بِالْكَسْرِ."))
put("faqa", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "فَاق", "فُق", "فُوق", "فُق", "فُوق", "فُق", "فَوْق", "فَائِق", None, None, None,
                        "أَجْوَفُ: تَسْقُطُ الْوَاوُ عِنْدَ السُّكُونِ — فُقْتُ، يَفُقْنَ، لَمْ يَفُقْ؛ وَفِي الشِّعْرِ تَفُقِ الْأَنَامَ بِكَسْرَةِ الْتِقَاءِ السَّاكِنَيْنِ."))
put("raqama", _sg.sound1("nasara", "رَقَم", "رْقُم", "اُرْقُم", "رَقْم", "رَاقِم", "مَرْقُوم", "رُقِمَ", "يُرْقَمُ"))
put("zaha", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "زَهَ", "زْه", "u", "اُزْه", "زَهْو", "زَاهٍ (الزَّاهِي)", None, None, None,
                       "نَاقِصٌ وَاوِيٌّ: زَهَا يَزْهُو، زَهَتْ، زَهَوْا؛ تَزْهُو بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ."))
put("daufa", _sg.sound1("karuma", "ضَعُف", "ضْعُف", "اُضْعُف", "ضَعْف", "ضَعِيف", None, None, None,
                        "مِنَ الْبَابِ الْخَامِسِ فَعُلَ يَفْعُلُ: لَازِمٌ، وَوَصْفُهُ صِفَةٌ مُشَبَّهَةٌ ضَعِيف؛ مَعَ نُونِ النِّسْوَةِ: ضَعُفْنَ."))
put("bada-appear", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "بَدَ", "بْد", "u", "اُبْد", "بُدُوّ", "بَادٍ (الْبَادِي)", None, None, None,
                       "نَاقِصٌ وَاوِيٌّ: بَدَا يَبْدُو، بَدَتْ، بَدَوْا."))
put("imtadaha", _sg.derived(_sg.B8, _sg.W8, "َ", "اِمْتَدَح", "مْتَدِح", "اِمْتَدِح", "اِمْتِدَاح", "مُمْتَدِح", "مُمْتَدَح", "اُمْتُدِحَ", "يُمْتَدَحُ"))
put("tashabaha", _sg.derived(_sg.B6, _sg.W6, "َ", "تَشَابَه", "تَشَابَه", "تَشَابَه", "تَشَابُه", "مُتَشَابِه", None, None, None,
                             "فِعْلُ الْمُشَارَكَةِ: يَطْلُبُ فَاعِلَيْنِ — تَشَابَهَ دَمْعِي وَمُدَامَتِي."))
put("sakaba", _sg.sound1("nasara", "سَكَب", "سْكُب", "اُسْكُب", "سَكْب", "سَاكِب", "مَسْكُوب", "سُكِبَ", "يُسْكَبُ"))
put("anzala", find_morph("anzala"))
put("qasada", find_morph("qasada"))
put("hasala", find_morph("hasala"))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the note
GR = ROOT / "content/grammar"
NOTE = {
 "id": "aghrad-al-tashbih",
 "title": {"ar": "أَدَاةُ التَّشْبِيهِ وَأَغْرَاضُهُ — وَالتَّشْبِيهُ الْمَقْلُوبُ وَالتَّشَابُهُ",
           "en": "The adat and the aims of tashbih — the reversed tashbih and tashabuh",
           "tr": "Teşbih edatı ve gayeleri — maklûb teşbih ve teşâbüh"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — أداة التشبيه، الغرض من التشبيه"],
 "question": {
  "en": ["What marks the likening — the kaf, كَأَنَّ, مِثْل and its kin, a masdar (تَشْبِيهُ), or a verb of the heart (عَلِمْتُ زَيْدًا أَسَدًا: near; حَسِبْتُ: far)?",
         "WHY liken? Seven aims return to the mushabbah (possibility, state, measure, settling, adorning, disfiguring, novelty); two return to the bihi (claiming it the more complete — the REVERSED tashbih — or showing one's concern for it).",
         "Are the two ends equal in the shared quality? Then leave tashbih for TASHABUH: تَشَابَهَ دَمْعِي وَمُدَامَتِي — no mushabbah, no bihi."],
  "tr": ["Benzetmeyi ne gösterir — kâf, كَأَنَّ, مِثْل ve benzerleri, bir masdar (تَشْبِيهُ), yahut bir kalp fiili (عَلِمْتُ زَيْدًا أَسَدًا: yakın; حَسِبْتُ: uzak)?",
         "NİÇİN benzetilir? Yedi gaye müşebbehe döner (imkân, hâl, miktar, karar, süsleme, çirkin gösterme, istitrâf); ikisi bihe döner (onu daha tam gösterme — MAKLÛB teşbih — yahut ona ehemmiyet verme).",
         "İki taraf ortak vasıfta eşit mi? Öyleyse teşbihi bırakıp TEŞÂBÜHE geç: تَشَابَهَ دَمْعِي وَمُدَامَتِي — ne müşebbeh ne bih."]},
 "plain": {
  "en": "The tools of likening are the kaf, كَأَنَّ, مِثْل and its kin; the engine also reads the masdar تَشْبِيه and the verbs of the heart as tools. A likening serves a purpose: mostly about the mushabbah, sometimes about the bihi. When two things are simply alike, the books say they RESEMBLE each other.",
  "tr": "Benzetme âletleri kâf, كَأَنَّ, مِثْل ve onun gibi kelimelerdir — motor تَشْبِيه masdarını ve kalp fiillerini de âlet olarak okur. Benzetme bir gaye için yapılır: çoğunlukla müşebbeh hakkında, bazen bih hakkında bir şey göstermek; iki şey sadece birbirine benziyorsa kitaplar BENZEŞTİLER demeyi yeğler."},
 "explanation": {
  "en": "THE ADAT: the kaf, كَأَنَّ, مِثْل and whatever means it (شِبْه، نَحْو، نَظِير). With the kaf and its kin the rule is that the MUSHABBAH BIHI follows the adat — yet sometimes something else does: وَاضْرِبْ لَهُمْ مَثَلَ الْحَيَاةِ الدُّنْيَا كَمَاءٍ أَنْزَلْنَاهُ مِنَ السَّمَاءِ (18:45) likens not the life to water but the STATE of this world, in the speed of its passing, to the state of the plants the water brings up and then dries. A VERB may tell of the likening: عَلِمْتُ زَيْدًا أَسَدًا when the mushabbah is near the bihi, حَسِبْتُ زَيْدًا أَسَدًا when it is far — the verbs of the heart with their two objects. THE AIMS mostly return to the mushabbah: (1) to show it POSSIBLE — فَإِنْ تَفُقِ الْأَنَامَ وَأَنْتَ مِنْهُمْ فَإِنَّ الْمِسْكَ بَعْضُ دَمِ الْغَزَالِ, a hidden likening with no adat; (2) its STATE — a garment likened to another in blackness; (3) the MEASURE of that state — likened to the raven; (4) to SETTLE it — one who gets nothing from his striving likened to one who writes on water, for the wajh is plainer and more famous in the bihi; (5) to ADORN — a black face likened to the gazelle's eye; (6) to DISFIGURE; (7) NOVELTY (اسْتِطْرَاف) — coal with lit embers likened to a sea of musk whose waves are gold, and Abu l-ʿAtahiya's violets وَلَازَوَرْدِيَّةٍ تَزْهُو بِزُرْقَتِهَا … كَأَنَّهَا فَوْقَ قَامَاتٍ ضَعُفْنَ بِهَا أَوَائِلُ النَّارِ فِي أَطْرَافِ كِبْرِيتِ, where the bihi seldom comes to mind when the mushabbah is before us. Two aims return to the BIHI: to suggest it is the MORE COMPLETE — the REVERSED tashbih (التَّشْبِيهُ الْمَقْلُوبُ): وَبَدَا الصَّبَاحُ كَأَنَّ غُرَّتَهُ وَجْهُ الْخَلِيفَةِ حِينَ يُمْتَدَحُ, where the morning, in truth the whiter, is made the mushabbah so that the Caliph's face outshines it; and to show one's CONCERN for it — the hungry man likening a face like the full moon to a loaf. And when the JOINING of two things in one quality is intended, it is better to leave tashbih for the judgement of TASHABUH: تَشَابَهَ دَمْعِي إِذْ جَرَى وَمُدَامَتِي — red tears and red wine judged alike, neither ranked. WHAT THE ENGINE CLAIMS: the adat and the arkan from the syntax — the verbs of the heart (0b), the masdar annexed to a relative or to a noun with its describing clause (تَشْبِيهِ مَنْ لَا يَحْصُلُ … بِمَنْ يَرْقُمُ عَلَى الْمَاءِ; فَحْمٍ فِيهِ جَمْرٌ مُوقَدٌ), the masdar annexed to its FA'IL with its object in nasb (تَشْبِيهِ الْجَائِعِ وَجْهًا … بِالرَّغِيفِ), the tashabuh frame (0c) with no direction, and the zarf-clause that restricts a bihi (وَجْهُ الْخَلِيفَةِ حِينَ يُمْتَدَحُ). It refuses مِثْل / نَحْو after a jarr-particle (فِي نَحْوِ الْكَافِ، مِنْ مِثْلِ مَا) and مَثَل with a fatha (a state, a parable), and كَأَنَّ named as a word. The AIMS and the reversal are knowledge of what the poet meant: the lab lists them as a shortlist and the frame does not claim them.",
  "tr": "EDAT: kâf, كَأَنَّ, مِثْل ve onun mânâsındaki her kelime (شِبْه، نَحْو، نَظِير). Kâf ve benzerlerinde asıl, edatı MÜŞEBBEHÜN BİHİN takip etmesidir — fakat bazen başkası takip eder: وَاضْرِبْ لَهُمْ مَثَلَ الْحَيَاةِ الدُّنْيَا كَمَاءٍ أَنْزَلْنَاهُ مِنَ السَّمَاءِ (18:45) hayatı suya değil, dünyanın HÂLİNİ, geçip gitmesinin hızında, suyun bitirip sonra kuruttuğu bitkinin hâline benzetir. Benzetmeden bir FİİL haber verebilir: müşebbeh bihe yakınsa عَلِمْتُ زَيْدًا أَسَدًا, uzaksa حَسِبْتُ زَيْدًا أَسَدًا — iki mef'ûllü kalp fiilleri. GAYELER çoğunlukla müşebbehe döner: (1) MÜMKÜN olduğunu göstermek — فَإِنْ تَفُقِ الْأَنَامَ وَأَنْتَ مِنْهُمْ فَإِنَّ الْمِسْكَ بَعْضُ دَمِ الْغَزَالِ, edatsız gizli benzetme; (2) HÂLİNİ — siyahlıkta bir elbisenin başka elbiseye benzetilmesi; (3) hâlin MİKTARINI — kargaya benzetilmesi; (4) KARARA BAĞLAMAK — çabasından bir şey elde edemeyenin su üstüne yazana benzetilmesi, çünkü vech bihte daha açık ve meşhurdur; (5) SÜSLEMEK — siyah yüzün ceylan gözüne benzetilmesi; (6) ÇİRKİN GÖSTERMEK; (7) İSTİTRÂF — korlu kömürün altın dalgalı misk denizine benzetilmesi ve Ebü'l-Atâhiye'nin menekşeleri وَلَازَوَرْدِيَّةٍ تَزْهُو بِزُرْقَتِهَا … كَأَنَّهَا فَوْقَ قَامَاتٍ ضَعُفْنَ بِهَا أَوَائِلُ النَّارِ فِي أَطْرَافِ كِبْرِيتِ, müşebbeh önümüzdeyken bihin nadiren akla geldiği yer. İki gaye BİHE döner: onun DAHA TAM olduğunu ihsas — MAKLÛB teşbih (التَّشْبِيهُ الْمَقْلُوبُ): وَبَدَا الصَّبَاحُ كَأَنَّ غُرَّتَهُ وَجْهُ الْخَلِيفَةِ حِينَ يُمْتَدَحُ, aslında daha beyaz olan sabah müşebbeh yapılır ki halifenin yüzü onu geçsin; ve ona EHEMMİYET verildiğini göstermek — açın dolunay gibi yüzü ekmeğe benzetmesi. İki şeyi bir vasıfta BİRLEŞTİRMEK murad edilince teşbihi bırakıp TEŞÂBÜHLE hükmetmek daha güzeldir: تَشَابَهَ دَمْعِي إِذْ جَرَى وَمُدَامَتِي — kızıl gözyaşı ile kızıl şarap benzeşir sayılır, sıralanmaz. MOTORUN İDDİASI: edat ve rükünler söz diziminden — kalp fiilleri (0b), mevsûle yahut vasıf cümleli isme muzâf masdar (تَشْبِيهِ مَنْ لَا يَحْصُلُ … بِمَنْ يَرْقُمُ عَلَى الْمَاءِ; فَحْمٍ فِيهِ جَمْرٌ مُوقَدٌ), FÂİLİNE muzâf olup mef'ûlünü nasb eden masdar (تَشْبِيهِ الْجَائِعِ وَجْهًا … بِالرَّغِيفِ), yönsüz teşâbüh çerçevesi (0c) ve bihi kayıtlayan zarf cümlesi (وَجْهُ الْخَلِيفَةِ حِينَ يُمْتَدَحُ). Cer harfinden sonraki مِثْل / نَحْو'u (فِي نَحْوِ الْكَافِ، مِنْ مِثْلِ مَا), fethalı مَثَل'i (hâl, mesel) ve kelime olarak anılan كَأَنَّ'yi reddeder. GAYELER ve kalb, şairin muradının bilgisidir: lâboratuvar onları kısa liste olarak sunar, çerçeve iddia etmez."},
 "examples": [
  {"ar": "عَلِمْتُ زَيْدًا أَسَدًا", "en": "the verb of the heart as adat: near.", "tr": "edat olarak kalp fiili: yakın.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "وَاضْرِبْ لَهُمْ مَثَلَ الْحَيَاةِ الدُّنْيَا كَمَاءٍ أَنْزَلْنَاهُ مِنَ السَّمَاءِ", "en": "the kaf followed by a description, not the bihi.", "tr": "kâfı bih değil tasvir takip eder.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "وَكَتَشْبِيهِ مَنْ لَا يَحْصُلُ مِنْ سَعْيِهِ عَلَى طَائِلٍ بِمَنْ يَرْقُمُ عَلَى الْمَاءِ", "en": "two relatives as the two ends; the aim: settling.", "tr": "iki mevsûl iki taraf; gaye: karar.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "وَبَدَا الصَّبَاحُ كَأَنَّ غُرَّتَهُ وَجْهُ الْخَلِيفَةِ حِينَ يُمْتَدَحُ", "en": "the reversed tashbih; the bihi restricted by a zarf-clause.", "tr": "maklûb teşbih; zarf cümlesiyle kayıtlı bih.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"},
  {"ar": "تَشَابَهَ دَمْعِي إِذْ جَرَى وَمُدَامَتِي", "en": "tashabuh: two joined fa'ils, no direction.", "tr": "teşâbüh: iki atıflı fâil, yön yok.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«فِي نَحْوِ الْكَافِ: nahv teşbih edatıdır, kâf müşebbehün bihtir»",
   "right": "«Cer harfinden sonraki نَحْو bir sınıfı adlandırır: kâf ve benzerleri»",
   "why": {"en": "مِثْل and نَحْو liken only when they head the predicate; after a jarr-particle they are plain nouns of kind or amount.", "tr": "مِثْل ve نَحْو ancak yüklemin başındayken benzetir; cer harfinden sonra cins yahut miktar bildiren düz isimdir."}},
  {"wrong": "«مَثَلُ الْحَيَاةِ: مَثَل benzetme edatıdır»",
   "right": "«مَثَل (fetha ile) hâl ve mesel demektir; edat olan مِثْل (kesra ile)dır»",
   "why": {"en": "One letter-skeleton, two words: مِثْل «like» and مَثَل «a state, a parable». The engine reads the vowel on the mim.", "tr": "Bir iskelet, iki kelime: مِثْل «gibi» ve مَثَل «hâl, mesel». Motor mimin harekesini okur."}},
  {"wrong": "«وَبَدَا الصَّبَاحُ كَأَنَّ غُرَّتَهُ وَجْهُ الْخَلِيفَةِ: sabah halifenin yüzüne benzetilmiş, çünkü yüz daha parlaktır»",
   "right": "«Sabah aslında daha beyazdır; müşebbeh yapılması kalbdir — bih daha tam gösterilmek istenmiştir»",
   "why": {"en": "The reversed tashbih puts the truly stronger end in the mushabbah's seat on purpose. The syntax cannot see the reversal; knowledge of the two things can.", "tr": "Maklûb teşbih, aslında daha güçlü olan tarafı bile bile müşebbeh mevkiine koyar. Söz dizimi kalbı göremez; iki şeyin bilgisi görür."}}],
 "relatedNotes": ["arkan-al-tashbih", "wajh-al-shabah", "aqsam-wajh-al-shabah", "tashbih", "ilm-al-bayan", "zanna-wa-akhawatuha", "mafulayn", "imal-al-masdar", "ism-mawsul", "jumla-sifa", "anwa-al-waw", "hollow-verbs", "naqis-verbs"]}
(GR / "aghrad-al-tashbih.json").write_text(json.dumps(NOTE, ensure_ascii=False, indent=1), encoding="utf-8")
for nid in ("arkan-al-tashbih", "aqsam-wajh-al-shabah"):
    w = json.loads((GR / f"{nid}.json").read_text(encoding="utf-8"))
    if "aghrad-al-tashbih" not in w["relatedNotes"]:
        w["relatedNotes"].append("aghrad-al-tashbih")
        (GR / f"{nid}.json").write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch49:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + 10 built, 3 copied; note aghrad-al-tashbih;",
      "frames:", sum(1 for x in S if x.get("tashbih")))
