# -*- coding: utf-8 -*-
"""Author chapter 50 of talkhis-al-miftah — أَقْسَامُ التَّشْبِيهِ (sahifa 113-119,
lines ~3290-3440): the tashbih divided by its two ends (mufrad / murakkab;
malfuf, mafruq, taswiya, jam), by its wajh (tamthil, mujmal / mufassal,
qarib mubtadhal / baʿid gharib), by its adat (muakkad / mursal), and the
RANKS of the tashbih by what is dropped.

  s1, s3, s6-s7, s9, s11, s13, s15-s17, s19-s22, s25  — RESTORED from the
          source's Turkish (each marked in its translation).
  s2      هُوَ كَالرَّاقِمِ عَلَى الْمَاءِ — as printed.
  s4-s5   Abu Tammam's يَا صَاحِبَيَّ تَقَصَّيَا … / تَرَيَا نَهَارًا … — as printed
          (the source writes فَكَاََََنَّمَا with a run of fathas; the app writes
          فَكَأَنَّمَا; the rhyme's bare damma on مُقْمِرُ is kept).
  s8      Imruʾ al-Qays's كَأَنَّ قُلُوبَ الطَّيْرِ … — as printed.
  s10     al-Muraqqish's النَّشْرُ مِسْكٌ … عَنَمْ — as printed, the rhyme sukun kept.
  s12     Rashid al-Din's صُدْغُ الْحَبِيبِ … / وَثَغْرُهُ فِي صَفَاءٍ … — as printed
          (the source writes كَاللاٰلِي with the dagger alif; the app كَاللَّآلِي).
  s14     al-Buhturi's كَأَنَّمَا يَبْسِمُ … — as printed.
  s17-s19 زَيْدٌ كَالْأَسَدِ, هُمْ كَالْحَلْقَةِ الْمُفْرَغَةِ … and هُوَ كَالْعَسَلِ فِي
          الْحَلَاوَةِ — the examples as printed inside restored frames.
  s23     the aya 27:88 وَهِيَ تَمُرُّ مَرَّ السَّحَابِ — as printed.
  s24     Ibn Khafaja's وَالرِّيحُ تَعْبَثُ … — as printed.

Every likening carries an authored `tashbih` frame — and, new in this
chapter, the frame's TAʿADDUD (malfuf / mafruq / taswiya / jam) and its
RANK (aʿla / mutawassit / adna) which the engine must read back.

Grammar this chapter teaches: note `aqsam-al-tashbih` (group bayan); the
annexed dual with a pronoun as munada and as object (صَاحِبَيَّ، نَظَرَيْكُمَا،
طَرَفَاهَا); the hal pair; the tawkid كِلَاهُمَا; the maf'ul mutlaq of likeness;
paradigms تَقَصَّى، تَعَدَّدَ، بَسَمَ، دَرَى، انْتَقَلَ، حَذَفَ، عَبِثَ; تَصَوَّرَ copied.
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
Q = "aqsam-al-tashbih"; A = "arkan-al-tashbih"; W = "wajh-al-shabah"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
TITLE50 = {"ar": "أَقْسَامُ التَّشْبِيهِ بِاعْتِبَارِ الطَّرَفَيْنِ وَالْوَجْهِ وَالْأَدَاةِ، وَمَرَاتِبُهُ",
           "en": "The Kinds of Tashbih by its Two Ends, its Wajh and its Adat — and its Ranks",
           "tr": "Teşbihin İki Taraf, Vech ve Edat Bakımından Kısımları — ve Mertebeleri"}

# ----------- s1 — by the two ends (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The tashbih, with regard to its two ends, is either the likening of a single to a single, or a composite to a composite, or a single to a composite, or a composite to a single." + R_EN,
 "tr": "Teşbih, iki tarafı bakımından ya müfredin müfrede, ya mürekkebin mürekkebe, ya müfredin mürekkebe, ya mürekkebin müfrede benzetilmesidir." + R_TR},
 "tokens": [
  tok("وَالتَّشْبِيهُ","tashbih","noun",[Q,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالتَّشْبِيهُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the tashbih» — the mubtada.", "«teşbih» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("التَّشْبِيهُ","tashbih","noun")]),
  tok("بِاعْتِبَارِ","itibar","noun",[Q,"huruf-jarr","idafa-definiteness"], "الْبَاءُ جَارَّةٌ وَاعْتِبَارِ مَجْرُورٌ مُضَافٌ — بِاعْتِبَارِ: مِنْ جِهَةِ.", "«with regard to» — from the side of.", "«bakımından» — cihetinden.",
      segments=[seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("الطَّرَفَيْنِ","taraf","noun",[Q,A,"al-muthanna","idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — الْمُشَبَّهُ وَالْمُشَبَّهُ بِهِ.", "«the two ends» — a dual in jarr: the mushabbah and the bihi.", "«iki tarafı» — mecrur tesniye: müşebbeh ve bih."),
  tok("إِمَّا","imma","part",[Q,"atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("تَشْبِيهُ","tashbih","noun",[Q,"mubtada-khabar","idafa-definiteness","imal-al-masdar"],
      "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ. وَطَرَفَاهُ هُنَا أَسْمَاءُ أَقْسَامٍ، فَلَا يُقْرَأُ تَشْبِيهًا بِعَيْنِهِ.",
      "«the likening of» — the khabar; a masdar whose ends are CATEGORY names (a single, a composite): the engine reads no particular likening here.",
      "«benzetilmesi» — haber; tarafları KISIM adları (müfred, mürekkeb) olan masdar: motor burada belirli bir benzetme okumaz."),
  tok("مُفْرَدٍ","mufrad","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a single».", "«müfredin»."),
  tok("بِمُفْرَدٍ","mufrad","noun",[Q,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَمُفْرَدٍ مَجْرُورٌ.", "«to a single».", "«müfrede».",
      segments=[seg("بِ","bi","part"), seg("مُفْرَدٍ","mufrad","noun")], punct="،"),
  tok("أَوْ","aw","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("مُرَكَّبٍ","murakkab","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ عَلَى مُفْرَدٍ مَجْرُورٌ — أَيْ: تَشْبِيهُ مُرَكَّبٍ.", "«a composite» — joined (the likening of a composite…).", "«mürekkebin» — atıf."),
  tok("بِمُرَكَّبٍ","murakkab","noun",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to a composite».", "«mürekkebe».",
      segments=[seg("بِ","bi","part"), seg("مُرَكَّبٍ","murakkab","noun")], punct="،"),
  tok("أَوْ","aw","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("مُفْرَدٍ","mufrad","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«a single».", "«müfredin»."),
  tok("بِمُرَكَّبٍ","murakkab","noun",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to a composite».", "«mürekkebe».",
      segments=[seg("بِ","bi","part"), seg("مُرَكَّبٍ","murakkab","noun")], punct="،"),
  tok("أَوْ","aw","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("مُرَكَّبٍ","murakkab","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«a composite».", "«mürekkebin»."),
  tok("بِمُفْرَدٍ","mufrad","noun",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — أَرْبَعَةُ أَقْسَامٍ.", "«to a single» — four kinds.", "«müfrede» — dört kısım.",
      segments=[seg("بِ","bi","part"), seg("مُفْرَدٍ","mufrad","noun")], punct=".")]})

# ----------- s2 — the Arabs' saying (as printed): both ends single, the bihi restricted
S.append({"id": "s2", "translation": {
 "en": "«He is like one who writes on water.»",
 "tr": "«O, su üzerine yazı yazan gibidir.»"},
 "tashbih": frame([0], 1, [1, 2, 3], [], "mursal-mujmal", "mufrad", "muqayyad", None, rank="mid"),
 "tokens": [
  tok("هُوَ","huwa","pron",[Q,A,"mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — الْمُشَبَّهُ، مُفْرَدٌ غَيْرُ مُقَيَّدٍ.", "«he» — the mushabbah, a bare single.", "«o» — müşebbeh, kayıtsız tek."),
  tok("كَالرَّاقِمِ","raqim","noun",[Q,A,"huruf-jarr","ism-fail","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ، وَالرَّاقِمِ مَجْرُورٌ — خَبَرٌ. الْمُشَبَّهُ بِهِ، مُقَيَّدٌ بِمَا بَعْدَهُ.",
      "«like one who writes» — the kaf-adat; the bihi, RESTRICTED by the phrase after it: not any writer, but one writing on water.",
      "«yazan gibi» — kâf-edat; bih, ardındaki tamlamayla KAYITLI: herhangi bir yazan değil, su üstüne yazan.",
      segments=[seg("كَ","ka","part"), seg("الرَّاقِمِ","raqim","noun")]),
  tok("عَلَى","ala","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ — الْقَيْدُ.", "«on» — the restriction begins.", "«üzerine» — kayıt başlar."),
  tok("الْمَاءِ","ma-water","noun",[Q,"huruf-jarr"], "اسْمٌ مَجْرُورٌ مُتَعَلِّقٌ بِالرَّاقِمِ.", "«water» — the mushabbah too is understood as restricted: one whose striving yields nothing.", "«su» — müşebbeh de kayıtlı anlaşılır: çabasından bir şey çıkmayan.", punct=".")]})

# ----------- s3 — the composite kinds, by their bayts (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "The likening of a composite to a composite is as in Bashshar's bayt, and of a single to a composite as in the bayt of the anemone." + R_EN,
 "tr": "Mürekkebin mürekkebe benzetilmesi Beşşâr'ın beytindeki gibidir; müfredin mürekkebe benzetilmesi de şakāyık beytindeki gibi." + R_TR},
 "tokens": [
  tok("وَتَشْبِيهُ","tashbih","noun",[Q,"mubtada-khabar","idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَتَشْبِيهُ مُبْتَدَأٌ مُضَافٌ.", "«the likening of» — the mubtada.", "«benzetilmesi» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("تَشْبِيهُ","tashbih","noun")]),
  tok("الْمُرَكَّبِ","murakkab","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ قِسْمٍ.", "«the composite» — a category name.", "«mürekkebin» — kısım adı."),
  tok("بِالْمُرَكَّبِ","murakkab","noun",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to the composite».", "«mürekkebe».",
      segments=[seg("بِ","bi","part"), seg("الْمُرَكَّبِ","murakkab","noun")]),
  tok("كَبَيْتِ","bayt","noun",[Q,"huruf-jarr","idafa-definiteness"],
      "الْكَافُ لِلتَّمْثِيلِ، وَبَيْتِ مَجْرُورٌ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. كَافُ التَّمْثِيلِ لَا التَّشْبِيهِ.",
      "«as in the bayt of» — the kaf that cites an example (a wall for the engine), the khabar.", "«beytindeki gibi» — örnek gösteren kâf (motor için duvar), haber.",
      segments=[seg("كَ","ka","part"), seg("بَيْتِ","bayt","noun")]),
  tok("بَشَّارٍ","bashshar","propn",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — بَشَّارُ بْنُ بُرْدٍ.", "«Bashshar» — b. Burd: كَأَنَّ مُثَارَ النَّقْعِ.", "«Beşşâr» — b. Bürd: كَأَنَّ مُثَارَ النَّقْعِ.", punct="،"),
  tok("وَالْمُفْرَدِ","mufrad","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ عَلَى الْمُرَكَّبِ مَجْرُورٌ — أَيْ: وَتَشْبِيهُ الْمُفْرَدِ.", "«and (the likening of) the single» — joined to the first mudaf ilayh.", "«ve müfredin» — ilk muzâfun ileyhe atıf.",
      segments=[seg("وَ","wa","conj"), seg("الْمُفْرَدِ","mufrad","noun")]),
  tok("بِالْمُرَكَّبِ","murakkab","noun",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to the composite».", "«mürekkebe».",
      segments=[seg("بِ","bi","part"), seg("الْمُرَكَّبِ","murakkab","noun")]),
  tok("كَبَيْتِ","bayt","noun",[Q,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — خَبَرٌ.", "«as in the bayt of» — the example-kaf.", "«beytindeki gibi» — örnek kâfı.",
      segments=[seg("كَ","ka","part"), seg("بَيْتِ","bayt","noun")]),
  tok("الشَّقِيقِ","shaqiq","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — بَيْتُ مُحْمَرِّ الشَّقِيقِ.", "«the anemone» — the bayt وَكَأَنَّ مُحْمَرَّ الشَّقِيقِ.", "«şakāyık» — وَكَأَنَّ مُحْمَرَّ الشَّقِيقِ beyti.", punct=".")]})

# ----------- s4 — Abu Tammam, first bayt (as printed): the annexed duals with their pronouns
S.append({"id": "s4", "translation": {
 "en": "«O my two companions, send your two gazes far: you will see the faces of the earth, how they are shaped —»",
 "tr": "«Ey iki dostum, bakışlarınızı uzağa gönderin: yeryüzünün yüzlerinin nasıl şekillendiğini görürsünüz —»"},
 "tokens": [
  tok("يَا","ya","part",[Q,"vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("صَاحِبَيَّ","sahib","noun",[Q,"vocative-munada","al-muthanna","ya-al-mutakallim","idafa-definiteness"],
      "مُنَادًى مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى مُضَافٌ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَيَاءُ الْمُتَكَلِّمِ مُضَافٌ إِلَيْهِ — صَاحِبَيْ + ي: أُدْغِمَتِ الْيَاءُ فِي الْيَاءِ.",
      "«my two companions» — a munada in nasb by the DUAL YA (annexed, so no nun), then the speaker's ya: صَاحِبَيْ + ي fuse into يَّ. One word, two offices — and the engine reads the dual under the shadda.",
      "«iki dostum» — TESNİYE YÂSIYLA mansub münâdâ (muzâf, nûnsuz), sonra mütekellim yâsı: صَاحِبَيْ + ي, يَّ olarak idgam. Bir kelime, iki vazife — motor şeddenin altındaki tesniyeyi okur.",
      segments=[seg("صَاحِبَيْ","sahib","noun"), seg("يَ","pron-1s","pron")]),
  tok("تَقَصَّيَا","taqassa","verb",[Q,"imperative-amr","form-v-verbs","naqis-verbs","al-muthanna"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — تَقَصَّى: بَلَغَ الْأَقْصَى.",
      "«send far (you two)» — the dual amr of تَقَصَّى (to reach the farthest); the alif is the fa'il.", "«uzağa gönderin (ikiniz)» — تَقَصَّى'nın tesniye emri (en uzağa ulaşmak); elif fâil."),
  tok("نَظَرَيْكُمَا","nazar","noun",[Q,"maful-bihi","al-muthanna","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى مُضَافٌ، وَكُمَا مُضَافٌ إِلَيْهِ.",
      "«your two gazes» — the object: a dual by its ya, annexed to the dual pronoun كُمَا.", "«iki bakışınızı» — mef'ûl: yâ ile tesniye, tesniye zamiri كُمَا'ya muzâf.",
      segments=[seg("نَظَرَيْ","nazar","noun"), seg("كُمَا","pron-2d","pron")]),
  tok("تَرَيَا","raa","verb",[Q,"jawab-al-talab","naqis-verbs","al-muthanna"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — تَرَيَانِ → تَرَيَا.",
      "«you will see» — jazm as the answer of the command: the dual nun drops (تَرَيَانِ → تَرَيَا).", "«görürsünüz» — emrin cevabında cezm: tesniye nûnu düşer (تَرَيَانِ → تَرَيَا)."),
  tok("وُجُوهَ","wajh","noun",[Q,"maful-bihi","idafa-definiteness","jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ — جَمْعُ وَجْهٍ.", "«the faces of».", "«yüzlerini»."),
  tok("الْأَرْضِ","ard","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the earth».", "«yerin»."),
  tok("كَيْفَ","kayfa","noun",[Q,"al-istifham","hal"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ حَالٌ — وَالْجُمْلَةُ بَدَلٌ مِنْ وُجُوهَ.", "«how» — the question-noun as hal; the clause stands in for the object.", "«nasıl» — hâl olan istifham ismi; cümle mef'ûlden bedel."),
  tok("تَصَوَّرُ","tasawwara","verb",[Q,"form-v-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، أَصْلُهُ تَتَصَوَّرُ حُذِفَتْ إِحْدَى تَاءَيْهِ، وَالْفَاعِلُ مُسْتَتِرٌ (هِيَ).",
      "«they are shaped» — تَتَصَوَّرُ with one of its two ta's dropped, as poets may.", "«şekillenir» — iki tâsından biri düşmüş تَتَصَوَّرُ, şairlerin yaptığı gibi.",
      punct=".")]})

# ----------- s5 — the second bayt (as printed): a composite likened to a single
S.append({"id": "s5", "translation": {
 "en": "«— you will see a sunlit day that the flowers of the hills have mingled with, so that it is as if it were moonlit.»",
 "tr": "«— tepelerin çiçeklerinin karıştığı güneşli bir gündüz görürsünüz; sanki o, mehtaplı bir gecedir.»"},
 "tashbih": frame([8], 7, [9], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("تَرَيَا","raa","verb",[Q,"naqis-verbs","al-muthanna"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ (تَكْرِيرُ الْجَوَابِ)، وَالْأَلِفُ فَاعِلٌ.", "«you will see» — the answer repeated.", "«görürsünüz» — cevap tekrarlanmış."),
  tok("نَهَارًا","nahar","noun",[Q,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a day» — the object; the composite mushabbah begins here.", "«bir gündüz» — mef'ûl; mürekkeb müşebbeh burada başlar."),
  tok("مُشْمِسًا","mushmis","noun",[Q,"naat-sifa","ism-fail","form-iv-verbs"], "نَعْتٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ أَشْمَسَ.", "«sunlit» — na't.", "«güneşli» — sıfat."),
  tok("قَدْ","qad","part",[Q,"qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«gerçekten»."),
  tok("شَابَهُ","shaba","verb",[Q,"jumla-sifa","hollow-verbs","maful-bihi"],
      "فِعْلٌ مَاضٍ أَجْوَفُ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِنَهَارًا. شَابَ: خَلَطَ — لَا شَابَهَ: أَشْبَهَ.",
      "«that … have mingled with it» — the hollow شَابَ (to mix) with its object-ha, NOT شَابَهَ (to resemble): the engine reads the lemma, not the letters, and refuses a likening-verb here.",
      "«ona karışan» — mef'ûl hâsıyla ecvef شَابَ (karıştırmak), شَابَهَ (benzemek) DEĞİL: motor harfleri değil lemmayı okur ve burada benzetme fiili reddeder.",
      segments=[seg("شَابَ","shaba","verb"), seg("هُ","pron-3ms","pron")]),
  tok("زَهَرُ","zahar","noun",[Q,"fail","idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ مُضَافٌ.", "«the flowers of» — the fa'il.", "«çiçekleri» — fâil."),
  tok("الرُّبَا","ruba-hills","noun",[Q,"idafa-definiteness","jam-taksir","ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — جَمْعُ رَبْوَةٍ.", "«the hills» — plural of رَبْوَة, a maqsur.", "«tepelerin» — رَبْوَة'nin çoğulu, maksûr."),
  tok("فَكَأَنَّمَا","ka-anna","part",[Q,A,"inna-wa-akhawatuha","innama-kaffa","tashbih"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَكَأَنَّمَا: كَأَنَّ كُفَّتْ بِمَا عَنِ الْعَمَلِ — الْأَدَاةُ. (يَكْتُبُهُ الْمَصْدَرُ بِفَتَحَاتٍ مُكَرَّرَةٍ.)",
      "«so that it is as if» — كَأَنَّ stopped by مَا: the adat, followed by a full clause.", "«öyle ki sanki» — مَا ile amelden alıkonmuş كَأَنَّ: edat, ardından tam cümle.",
      segments=[seg("فَ","fa","conj"), seg("كَأَنَّمَا","ka-anna","part")]),
  tok("هُوَ","huwa","pron",[Q,A,"mubtada-khabar"],
      "مُبْتَدَأٌ — يَعُودُ إِلَى النَّهَارِ الْمُشْمِسِ الَّذِي شَابَهُ الزَّهَرُ: الْمُشَبَّهُ، وَهُوَ مُرَكَّبٌ فِي الْمَعْنَى.",
      "«it» — the mubtada: the MUSHABBAH is this pronoun, which stands for the whole picture (a sunlit day mixed with flowers) — composite in meaning, a pronoun on the surface.",
      "«o» — mübtedâ: MÜŞEBBEH bu zamirdir, bütün tabloyu (çiçek karışmış güneşli gündüzü) temsil eder — mânâca mürekkeb, yüzeyde zamir."),
  tok("مُقْمِرُ","muqmir","noun",[Q,A,"mubtada-khabar","ism-fail","form-iv-verbs","tashbih"],
      "خَبَرٌ مَرْفُوعٌ، حُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ — اسْمُ فَاعِلٍ مِنْ أَقْمَرَ: لَيْلٌ مُقْمِرٌ. الْمُشَبَّهُ بِهِ، مُفْرَدٌ مُقَيَّدٌ.",
      "«moonlit» — the khabar, its tanwin dropped for the rhyme; the ism fa'il of أَقْمَرَ (a moonlit night): the BIHI, a single — the composite likened to a single.",
      "«mehtaplı» — haber, tenvini kafiye için düşmüş; أَقْمَرَ'nin ism-i fâili (mehtaplı gece): BİH, tek — mürekkeb tek'e benzetilmiş.",
      punct=".")]})

# ----------- s6 — by the number of the ends (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And with regard to the plurality of the two ends: malfuf (wrapped), mafruq (separated), taswiya (equalising) and jam (gathering)." + R_EN,
 "tr": "İki tarafın çokluğu bakımından: melfûf, mefrûk, tesviye ve cem'." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[Q,"huruf-jarr","idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ جَارَّةٌ، وَاعْتِبَارِ مَجْرُورٌ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«and with regard to» — a fronted khabar.", "«ve … bakımından» — mukaddem haber.",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("تَعَدُّدِ","taaddud","noun",[Q,"idafa-definiteness","masdar","form-v-verbs"], "مُضَافٌ إِلَيْهِ مُضَافٌ — مَصْدَرُ تَعَدَّدَ.", "«the plurality of».", "«çokluğu»."),
  tok("الطَّرَفَيْنِ","taraf","noun",[Q,"al-muthanna","idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two ends».", "«iki tarafın»."),
  tok("مَلْفُوفٌ","malfuf","noun",[Q,"mubtada-khabar","ism-maful"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — أَيْ: هُوَ مَلْفُوفٌ.", "«wrapped» — the delayed mubtada (the tashbih is…).", "«melfûf» — muahhar mübtedâ."),
  tok("وَمَفْرُوقٌ","mafruq","noun",[Q,"atf-nasaq","ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ.", "«separated».", "«mefrûk».", segments=[seg("وَ","wa","conj"), seg("مَفْرُوقٌ","mafruq","noun")]),
  tok("وَتَسْوِيَةٌ","taswiya","noun",[Q,"atf-nasaq","masdar","form-ii-verbs"], "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ سَوَّى.", "«equalising».", "«tesviye».", segments=[seg("وَ","wa","conj"), seg("تَسْوِيَةٌ","taswiya","noun")]),
  tok("وَجَمْعٌ","jam-gathering","noun",[Q,"atf-nasaq","masdar"], "مَعْطُوفٌ مَرْفُوعٌ.", "«gathering».", "«cem'».", segments=[seg("وَ","wa","conj"), seg("جَمْعٌ","jam-gathering","noun")], punct=".")]})

# ----------- s7 — malfuf defined (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "The malfuf is that whose two ends are plural, the mushabbahs being mentioned first and then the things they are likened to." + R_EN,
 "tr": "Melfûf, iki tarafı müteaddid olup önce müşebbehlerin, sonra müşebbehün bihlerin zikredildiği teşbihtir." + R_TR},
 "tokens": [
  tok("فَالْمَلْفُوفُ","malfuf","noun",[Q,"mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمَلْفُوفُ مُبْتَدَأٌ.", "«the malfuf» — the mubtada.", "«melfûf» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْمَلْفُوفُ","malfuf","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«… olan» — haber."),
  tok("تَعَدَّدَ","taaddada","verb",[Q,"form-v-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«are plural» — the sila.", "«çoğaldı» — sıla."),
  tok("طَرَفَاهُ","taraf","noun",[Q,"fail","al-muthanna","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its two ends» — the dual fa'il, annexed to its pronoun.", "«iki tarafı» — tesniye fâil, zamirine muzâf.",
      segments=[seg("طَرَفَا","taraf","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَذُكِرَتِ","dhakara","verb",[Q,"naib-al-fail","atf-nasaq"], "مَعْطُوفٌ — فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and were mentioned» — majhul; the ta takes a kasra before the article.", "«ve zikredildi» — meçhul; tâ harf-i tarif önünde kesra alır.",
      segments=[seg("وَ","wa","conj"), seg("ذُكِرَتِ","dhakara","verb")]),
  tok("الْمُشَبَّهَاتُ","mushabbah","noun",[Q,A,"naib-al-fail","jam-muannath-salim"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the mushabbahs» — the deputy, a sound feminine plural.", "«müşebbehler» — nâib, cem-i müennes-i sâlim."),
  tok("أَوَّلًا","awwalan","noun",[Q,"maful-fih"], "ظَرْفٌ مَنْصُوبٌ.", "«first».", "«önce»."),
  tok("ثُمَّ","thumma","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("الْمُشَبَّهُ","mushabbah","noun",[Q,A,"atf-nasaq"], "مَعْطُوفٌ عَلَى الْمُشَبَّهَاتُ مَرْفُوعٌ.", "«the things likened» — joined.", "«benzetilenler» — atıf."),
  tok("بِهَا","bi","part",[Q,A,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُشَبَّهُ بِهَا: جَمْعُ الْمُشَبَّهِ بِهِ.", "«to them» — the plural of الْمُشَبَّهُ بِهِ.", "«kendilerine» — الْمُشَبَّهُ بِهِ'nin çoğulu.",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")], punct=".")]})

# ----------- s8 — Imruʾ al-Qays: malfuf (as printed)
S.append({"id": "s8", "translation": {
 "en": "«As if the hearts of the birds, moist and dry, beside its nest, were jujubes and rotten dates.»",
 "tr": "«Sanki kuşların yaş ve kuru yürekleri, yuvasının yanında, hünnap ve çürük hurmadır.»"},
 "tashbih": frame([1, 2, 3, 4], 0, [7, 8, 9], [], "mursal-mujmal", "mufrad", "mufrad", None, taaddud="malfuf", rank="mid"),
 "tokens": [
  tok("كَأَنَّ","ka-anna","part",[Q,A,"inna-wa-akhawatuha","tashbih"], "حَرْفُ تَشْبِيهٍ وَنَصْبٍ — الْأَدَاةُ.", "«as if» — the adat.", "«sanki» — edat."),
  tok("قُلُوبَ","qalb","noun",[Q,A,"inna-wa-akhawatuha","idafa-definiteness","jam-taksir"], "اسْمُ كَأَنَّ مَنْصُوبٌ مُضَافٌ — جَمْعُ قَلْبٍ.", "«the hearts of» — the ism: the first end begins.", "«yüreklerini» — ism: ilk taraf başlar."),
  tok("الطَّيْرِ","tayr","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ جِنْسٍ.", "«the birds» — a collective.", "«kuşların» — cins ismi."),
  tok("رَطْبًا","ratb","noun",[Q,A,"hal"], "حَالٌ مَنْصُوبٌ مِنْ قُلُوبَ — الْمُشَبَّهُ الْأَوَّلُ: الْقُلُوبُ رَطْبَةً.", "«moist» — a HAL: the FIRST mushabbah is the hearts-while-moist.", "«yaş» — HÂL: İLK müşebbeh yaş hâldeki yürekler."),
  tok("وَيَابِسًا","yabis","noun",[Q,A,"hal","atf-nasaq"],
      "مَعْطُوفٌ عَلَى الْحَالِ مَنْصُوبٌ — الْمُشَبَّهُ الثَّانِي: الْقُلُوبُ يَابِسَةً. مُشَبَّهَانِ ذُكِرَا أَوَّلًا.",
      "«and dry» — the second hal: the SECOND mushabbah. Two mushabbahs first — the mark of the MALFUF.", "«ve kuru» — ikinci hâl: İKİNCİ müşebbeh. Önce iki müşebbeh — MELFÛFun alâmeti.",
      segments=[seg("وَ","wa","conj"), seg("يَابِسًا","yabis","noun")]),
  tok("لَدَى","lada","noun",[Q,"maful-fih","idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«beside».", "«yanında»."),
  tok("وَكْرِهَا","wakr","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَهَا مُضَافٌ إِلَيْهِ — عَائِدٌ إِلَى الْعُقَابِ.", "«its nest» — the eagle's.", "«yuvasının» — kartalın.",
      segments=[seg("وَكْرِ","wakr","noun"), seg("هَا","pron-3fs","pron")]),
  tok("الْعُنَّابُ","unnab","noun",[Q,A,"inna-wa-akhawatuha","tashbih"], "خَبَرُ كَأَنَّ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ الْأَوَّلُ، لِلرَّطْبِ.", "«jujubes» — the khabar: the FIRST bihi, for the moist.", "«hünnap» — haber: İLK bih, yaşlar için."),
  tok("وَالْحَشَفُ","hashaf","noun",[Q,A,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ الثَّانِي، لِلْيَابِسِ: لَفٌّ وَنَشْرٌ مُرَتَّبٌ.", "«and rotten dates» — the SECOND bihi, for the dry: an ordered fold-and-unfold.", "«ve çürük hurma» — İKİNCİ bih, kurular için: mürettep leff ü neşr.",
      segments=[seg("وَ","wa","conj"), seg("الْحَشَفُ","hashaf","noun")]),
  tok("الْبَالِي","bali","noun",[Q,"naat-sifa","ism-maqsur-manqus","ism-fail"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — مَنْقُوصٌ.", "«decayed» — na't, a manqus with the article.", "«çürümüş» — sıfat, harf-i tarifli mankûs.", punct=".")]})

# ----------- s9 — mafruq defined (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "The mafruq is that in which each mushabbah is mentioned together with its own mushabbah bihi." + R_EN,
 "tr": "Mefrûk, her müşebbehin kendi müşebbehün bihiyle birlikte zikredildiği teşbihtir." + R_TR},
 "tokens": [
  tok("وَالْمَفْرُوقُ","mafruq","noun",[Q,"mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْمَفْرُوقُ مُبْتَدَأٌ.", "«the mafruq» — the mubtada.", "«mefrûk» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمَفْرُوقُ","mafruq","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that in which».", "«… olan»."),
  tok("ذُكِرَ","dhakara","verb",[Q,"naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is mentioned» — the sila.", "«zikredilir» — sıla."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْعَائِدُ.", "«in it» — the returning pronoun.", "«onda» — âid.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("كُلُّ","kull","noun",[Q,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", "«each» — the deputy fa'il.", "«her» — nâib-i fâil."),
  tok("مُشَبَّهٍ","mushabbah","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«mushabbah».", "«müşebbeh»."),
  tok("مَعَ","maa","noun",[Q,"maful-fih","idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«together with».", "«ile birlikte»."),
  tok("مُشَبَّهِهِ","mushabbah","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its … likened-to» — the term with its pronoun inside: مُشَبَّهِهِ بِهِ.", "«kendi … benzetileni» — zamiri içinde terim: مُشَبَّهِهِ بِهِ.",
      segments=[seg("مُشَبَّهِ","mushabbah","noun"), seg("هِ","pron-3ms","pron")]),
  tok("بِهِ","bi","part",[Q,A,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — تَمَامُ الْمُصْطَلَحِ.", "«bihi».", "«bih».",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s10 — al-Muraqqish: mafruq (as printed)
S.append({"id": "s10", "translation": {
 "en": "«The scent is musk, the faces are dinars, and the tips of the palms are anam-wood.»",
 "tr": "«Koku misk, yüzler dinar, avuçların uçları anem ağacıdır.»"},
 "tashbih": frame([0], None, [1], [], "baligh", "mufrad", "mufrad", None, taaddud="mafruq", rank="ala"),
 "tokens": [
  tok("النَّشْرُ","nashr-scent","noun",[Q,A,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — الْمُشَبَّهُ الْأَوَّلُ.", "«the scent» — the first mushabbah.", "«koku» — ilk müşebbeh."),
  tok("مِسْكٌ","misk","noun",[Q,A,"mubtada-khabar","tashbih"],
      "خَبَرٌ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ الْأَوَّلُ بِلَا أَدَاةٍ وَلَا وَجْهٍ: تَشْبِيهٌ بَلِيغٌ.",
      "«is musk» — the first bihi with no adat and no wajh: BALIGH, the highest rank.", "«misktir» — edatsız ve vechsiz ilk bih: BELÎĞ, en yüksek mertebe."),
  tok("وَالْوُجُوهُ","wajh","noun",[Q,A,"atf-nasaq","mubtada-khabar","jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَالْوُجُوهُ مُبْتَدَأٌ ثَانٍ — الْمُشَبَّهُ الثَّانِي.", "«and the faces» — the second mushabbah, with its own bihi beside it.", "«ve yüzler» — ikinci müşebbeh, bihi yanında.",
      segments=[seg("وَ","wa","conj"), seg("الْوُجُوهُ","wajh","noun")]),
  tok("دَنَانِيرُ","dinar","noun",[Q,A,"mubtada-khabar","jam-taksir","mamnu-min-sarf","tashbih"],
      "خَبَرٌ مَرْفُوعٌ بِلَا تَنْوِينٍ — صِيغَةُ مُنْتَهَى الْجُمُوعِ (فَعَالِيل).", "«dinars» — the second bihi; a heaviest-shape plural, no tanwin.", "«dinarlar» — ikinci bih; en ağır kalıp çoğul, tenvinsiz."),
  tok("وَأَطْرَافُ","taraf","noun",[Q,A,"atf-nasaq","mubtada-khabar","idafa-definiteness"], "مُبْتَدَأٌ ثَالِثٌ مُضَافٌ — الْمُشَبَّهُ الثَّالِثُ.", "«and the tips of» — the third mushabbah.", "«ve uçları» — üçüncü müşebbeh.",
      segments=[seg("وَ","wa","conj"), seg("أَطْرَافُ","taraf","noun")]),
  tok("الْأَكُفِّ","kaff","noun",[Q,"idafa-definiteness","jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ كَفٍّ.", "«the palms» — plural of كَفّ.", "«avuçların» — كَفّ'in çoğulu."),
  tok("عَنَمْ","anam-plant","noun",[Q,A,"mubtada-khabar","tashbih"],
      "خَبَرٌ مَرْفُوعٌ، سُكِّنَ لِلْقَافِيَةِ — الْعَنَمُ: شَجَرٌ لَيِّنٌ أَحْمَرُ. ثَلَاثُ تَشْبِيهَاتٍ كُلٌّ مَعَ صَاحِبِهِ: مَفْرُوقٌ.",
      "«anam-wood» — the third bihi (a soft red plant; the rhyme sukun kept). Three likenings, each end beside its own: MAFRUQ.",
      "«anem ağacı» — üçüncü bih (yumuşak kızıl bir bitki; kafiye sükûnu korunmuş). Her taraf kendi eşiyle üç benzetme: MEFRÛK.",
      punct=".")]})

# ----------- s11 — taswiya defined (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "The taswiya is that in which the mushabbah is plural but not the mushabbah bihi." + R_EN,
 "tr": "Tesviye, müşebbehin müteaddid olup müşebbehün bihin olmadığı teşbihtir." + R_TR},
 "tokens": [
  tok("وَالتَّسْوِيَةُ","taswiya","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the taswiya» — the mubtada.", "«tesviye» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("التَّسْوِيَةُ","taswiya","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that in which».", "«… olan»."),
  tok("تَعَدَّدَ","taaddada","verb",[Q,"form-v-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«is plural».", "«çoğalır»."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْمُشَبَّهُ","mushabbah","noun",[Q,A,"fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the mushabbah» — the fa'il.", "«müşebbeh» — fâil."),
  tok("دُونَ","duna","noun",[Q,"maful-fih","idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — بِمَعْنَى: لَا.", "«but not» — دُونَ as «without».", "«değil» — «-sız» mânâsında دُونَ."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the … likened-to».", "«benzetilen»."),
  tok("بِهِ","bi","part",[Q,A,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«bihi».", "«bih».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s12 — Rashid al-Din: taswiya, then the mufassal hemistich (as printed)
S.append({"id": "s12", "translation": {
 "en": "«The beloved's temple-lock and my state, both of them, are like the nights; • and his teeth, in clearness, and my tears are like the pearls.»",
 "tr": "«Sevgilinin zülfü ve benim hâlim, ikisi de, geceler gibidir; • dişleri, berraklıkta, ve gözyaşlarım inciler gibidir.»"},
 "tashbih": frame([0, 1, 2, 3], 4, [4], [], "mursal-mujmal", "mufrad", "mufrad", None, taaddud="taswiya", rank="mid"),
 "tokens": [
  tok("صُدْغُ","sudgh","noun",[Q,A,"mubtada-khabar","idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ — الْمُشَبَّهُ الْأَوَّلُ.", "«the temple-lock of» — the first mushabbah.", "«zülfü» — ilk müşebbeh."),
  tok("الْحَبِيبِ","habib","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the beloved».", "«sevgilinin»."),
  tok("وَحَالِي","hal","noun",[Q,A,"atf-nasaq","ya-al-mutakallim"], "مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — الْمُشَبَّهُ الثَّانِي.", "«and my state» — the second mushabbah, joined.", "«ve hâlim» — ikinci müşebbeh, atıf.",
      segments=[seg("وَ","wa","conj"), seg("حَالِ","hal","noun"), seg("ي","pron-1s","pron")]),
  tok("كِلَاهُمَا","kila","noun",[Q,"tawkid","al-muthanna","idafa-definiteness"],
      "تَوْكِيدٌ مَعْنَوِيٌّ لِلْمُبْتَدَأِ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، وَهُمَا مُضَافٌ إِلَيْهِ.",
      "«both of them» — the tawkid of the two mushabbahs, declined like a dual (كِلَا + هُمَا); it closes the mushabbah group.", "«ikisi de» — iki müşebbehin te'kidi, tesniye gibi çekilir (كِلَا + هُمَا); müşebbeh grubunu kapatır.",
      segments=[seg("كِلَا","kila","noun"), seg("هُمَا","pron-3d","pron")]),
  tok("كَاللَّيَالِي","layl","noun",[Q,A,"huruf-jarr","jam-taksir","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ، وَاللَّيَالِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — خَبَرٌ. مُشَبَّهٌ بِهِ وَاحِدٌ لِمُشَبَّهَيْنِ: تَسْوِيَةٌ.",
      "«like the nights» — the kaf-adat, the khabar: ONE bihi for TWO mushabbahs — TASWIYA (both black).", "«geceler gibi» — kâf-edat, haber: İKİ müşebbehe TEK bih — TESVİYE (ikisi de siyah).",
      segments=[seg("كَ","ka","part"), seg("اللَّيَالِي","layl","noun")], punct="•"),
  tok("وَثَغْرُهُ","thaghr","noun",[Q,A,W,"mubtada-khabar","idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَثَغْرُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُشَبَّهٌ ثَالِثٌ فِي تَشْبِيهٍ ثَانٍ.", "«and his teeth» — a new mushabbah in a second likening.", "«ve dişleri» — ikinci benzetmede yeni müşebbeh.",
      segments=[seg("وَ","wa","conj"), seg("ثَغْرُ","thaghr","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","part",[Q,W,"huruf-jarr"], "حَرْفُ جَرٍّ — يَبْدَأُ وَجْهَ الشَّبَهِ مُقَدَّمًا.", "«in» — the WAJH, spoken early.", "«-de» — VECH, önce söylenmiş."),
  tok("صَفَاءٍ","safa","noun",[Q,W,"huruf-jarr","masdar"], "اسْمٌ مَجْرُورٌ — وَجْهُ الشَّبَهِ مَذْكُورٌ: تَشْبِيهٌ مُفَصَّلٌ.", "«clearness» — the wajh SPOKEN: this second likening is MUFASSAL.", "«berraklık» — vech SÖYLENMİŞ: bu ikinci benzetme MUFASSALdır."),
  tok("وَأَدْمُعِي","dam-tear","noun",[Q,A,"atf-nasaq","jam-taksir","ya-al-mutakallim"], "مَعْطُوفٌ عَلَى ثَغْرُهُ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ دَمْعٍ.", "«and my tears» — joined: again two mushabbahs.", "«ve gözyaşlarım» — atıf: yine iki müşebbeh.",
      segments=[seg("وَ","wa","conj"), seg("أَدْمُعِ","dam-tear","noun"), seg("ي","pron-1s","pron")]),
  tok("كَاللَّآلِي","lulu","noun",[Q,A,"huruf-jarr","jam-taksir","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ، وَاللَّآلِي مَجْرُورٌ — خَبَرٌ. (يَكْتُبُهُ الْمَصْدَرُ كَاللاٰلِي.)",
      "«like the pearls» — the bihi of the second likening (the source writes كَاللاٰلِي).", "«inciler gibi» — ikinci benzetmenin bihi (kaynak كَاللاٰلِي yazar).",
      segments=[seg("كَ","ka","part"), seg("اللَّآلِي","lulu","noun")], punct=".")]})

# ----------- s13 — jam defined (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "The jam is that in which the mushabbah bihi is plural but not the mushabbah." + R_EN,
 "tr": "Cem', müşebbehün bihin müteaddid olup müşebbehin olmadığı teşbihtir." + R_TR},
 "tokens": [
  tok("وَالْجَمْعُ","jam-gathering","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the jam» — the mubtada.", "«cem'» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْجَمْعُ","jam-gathering","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that in which».", "«… olan»."),
  tok("تَعَدَّدَ","taaddada","verb",[Q,"form-v-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«is plural».", "«çoğalır»."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْمُشَبَّهُ","mushabbah","noun",[Q,A,"fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the … likened-to».", "«benzetilen»."),
  tok("بِهِ","bi","part",[Q,A,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«bihi».", "«bih».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("دُونَ","duna","noun",[Q,"maful-fih","idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«but not».", "«değil»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mushabbah».", "«müşebbeh».", punct=".")]})

# ----------- s14 — al-Buhturi: jam (as printed)
S.append({"id": "s14", "translation": {
 "en": "«As if he smiles from strung pearls, or hail, or camomile.»",
 "tr": "«Sanki dizili incilerden, yahut doludan, yahut papatyadan gülümsüyor.»"},
 "tashbih": {"mushabbah": [], "adat": 0, "bihi": [2, 3, 4, 5, 6, 7, 8], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": None, "bihi": "mufrad", "wajh": None}, "taaddud": "jam", "rank": "mid"},
 "tokens": [
  tok("كَأَنَّمَا","ka-anna","part",[Q,A,"inna-wa-akhawatuha","innama-kaffa","tashbih"],
      "كَأَنَّ كُفَّتْ بِمَا فَدَخَلَتْ عَلَى الْجُمْلَةِ الْفِعْلِيَّةِ — الْأَدَاةُ.", "«as if» — كَأَنَّ stopped by مَا, before a verbal clause: the adat.", "«sanki» — مَا ile alıkonmuş كَأَنَّ, fiil cümlesi önünde: edat."),
  tok("يَبْسِمُ","basama","verb",[Q,"mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ (الْمَمْدُوحُ) — وَالْمُشَبَّهُ ثَغْرُهُ الْمَفْهُومُ.", "«he smiles» — the hidden fa'il; the mushabbah (his teeth) is understood, not written.", "«gülümser» — gizli fâil; müşebbeh (dişleri) anlaşılır, yazılmaz."),
  tok("عَنْ","an","part",[Q,A,"huruf-jarr"], "حَرْفُ جَرٍّ — يَبْسِمُ عَنْ: يَكْشِفُ عَنْ.", "«from (revealing)» — the بِهِ-group opens on عَنْ.", "«-den (açarak)» — bih grubu عَنْ ile açılır."),
  tok("لُؤْلُؤٍ","lulu","noun",[Q,A,"huruf-jarr","tashbih"], "اسْمٌ مَجْرُورٌ — الْمُشَبَّهُ بِهِ الْأَوَّلُ.", "«pearls» — the first bihi.", "«inci» — ilk bih."),
  tok("مُنَضَّدٍ","munaddad","noun",[Q,"naat-sifa","ism-maful","form-ii-verbs"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ نَضَّدَ.", "«strung» — na't.", "«dizili» — sıfat."),
  tok("أَوْ","aw","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ.", "«or» — the alternatives count as several bihis.", "«yahut» — seçenekler birden çok bih sayılır."),
  tok("بَرَدٍ","barad","noun",[Q,A,"atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ — الثَّانِي.", "«hail» — the second bihi.", "«dolu» — ikinci bih."),
  tok("أَوْ","aw","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("أَقَاحٍ","uqah","noun",[Q,A,"atf-nasaq","jam-taksir","ism-maqsur-manqus"],
      "مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — أَقَاحٍ: جَمْعُ أُقْحُوَانٍ، مَنْقُوصٌ. ثَلَاثَةُ مُشَبَّهَاتٍ بِهَا لِمُشَبَّهٍ وَاحِدٍ: جَمْعٌ.",
      "«camomile» — the third bihi, a manqus plural. Three bihis for ONE mushabbah — JAM.", "«papatya» — üçüncü bih, mankûs çoğul. TEK müşebbehe üç bih — CEM'.",
      punct=".")]})

# ----------- s15 — by the wajh (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "And with regard to the wajh al-shabah: either tamthil or not tamthil; either mujmal or mufassal; either near and hackneyed, or far and rare." + R_EN,
 "tr": "Vech-i şebeh bakımından: ya temsil ya gayr-i temsil; ya mücmel ya mufassal; ya karîb-i mübtezel ya baîd-i garîb." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[Q,"huruf-jarr","idafa-definiteness"], "خَبَرٌ مُقَدَّمٌ.", "«and with regard to».", "«ve … bakımından».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("وَجْهِ","wajh","noun",[Q,W,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مُضَافٌ.", "«the face of».", "«yüzü»."),
  tok("الشَّبَهِ","shabah","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness».", "«benzerliğin»."),
  tok("إِمَّا","imma","part",[Q,"atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("تَمْثِيلٌ","tamthil","noun",[Q,"mubtada-khabar","masdar","form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ — التَّمْثِيلُ: مَا وَجْهُهُ هَيْئَةٌ.", "«tamthil» — the likening whose wajh is a hay'a.", "«temsil» — vechi hey'et olan benzetme."),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«or».", "«ya da».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("غَيْرُ","ghayr","noun",[Q,"atf-nasaq","idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ مُضَافٌ.", "«not».", "«gayr-i»."),
  tok("تَمْثِيلٍ","tamthil","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«tamthil».", "«temsil».", punct="،"),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"], "لِلتَّفْصِيلِ.", "«either».", "«ya».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("مُجْمَلٌ","mujmal","noun",[Q,"atf-nasaq","ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ — مَا لَمْ يُذْكَرْ وَجْهُهُ.", "«mujmal» — the wajh unspoken.", "«mücmel» — vechi söylenmemiş."),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"], "لِلتَّفْصِيلِ.", "«or».", "«ya».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("مُفَصَّلٌ","mufassal","noun",[Q,"atf-nasaq","ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ — مَا ذُكِرَ وَجْهُهُ.", "«mufassal» — the wajh spoken.", "«mufassal» — vechi söylenmiş.", punct="،"),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"], "لِلتَّفْصِيلِ.", "«either».", "«ya».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("قَرِيبٌ","qarib","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«near».", "«karîb»."),
  tok("مُبْتَذَلٌ","mubtadhal","noun",[Q,"naat-sifa","ism-maful","form-viii-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنِ ابْتَذَلَ: مَطْرُوقٌ.", "«hackneyed» — na't; worn by use.", "«mübtezel» — sıfat; kullanılmaktan aşınmış."),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"], "لِلتَّفْصِيلِ.", "«or».", "«ya».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("بَعِيدٌ","baid","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«far».", "«baîd»."),
  tok("غَرِيبٌ","gharib","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ — نَادِرٌ.", "«rare» — na't.", "«garîb» — sıfat.", punct=".")]})

# ----------- s16 — tamthil (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "The tamthil is that whose wajh is drawn from several things — as in likening the Pleiades to a cluster of white grapes." + R_EN,
 "tr": "Temsil, vechi birkaç şeyden çıkarılan teşbihtir — Süreyya'yı beyaz üzüm salkımına benzetmek gibi." + R_TR},
 "tashbih": frame([7], 6, [8, 9], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("فَالتَّمْثِيلُ","tamthil","noun",[Q,"mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالتَّمْثِيلُ مُبْتَدَأٌ.", "«the tamthil» — the mubtada.", "«temsil» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("التَّمْثِيلُ","tamthil","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that whose».", "«… olan»."),
  tok("وَجْهُهُ","wajh","noun",[Q,W,"mubtada-khabar","idafa-definiteness"], "مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةٌ اسْمِيَّةٌ.", "«its wajh» — a nominal sila.", "«vechi» — isim cümlesi sıla.",
      segments=[seg("وَجْهُ","wajh","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مُنْتَزَعٌ","muntaza","noun",[Q,"mubtada-khabar","ism-maful","form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنِ انْتَزَعَ.", "«drawn» — the khabar.", "«çıkarılmış» — haber."),
  tok("مِنْ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("مُتَعَدِّدٍ","mutaaddid","noun",[Q,"huruf-jarr"], "اسْمٌ مَجْرُورٌ — أُمُورٍ مُتَعَدِّدَةٍ.", "«several things» — the hay'a.", "«birkaç şey» — hey'et.", punct="،"),
  tok("كَتَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"], "الْكَافُ لِلتَّمْثِيلِ، وَتَشْبِيهِ مَجْرُورٌ مُضَافٌ — الْأَدَاةُ.", "«as in the likening of» — the masdar-adat.", "«benzetmek gibi» — masdar-edat.",
      segments=[seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("الثُّرَيَّا","thurayya","propn",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — الْمُشَبَّهُ.", "«the Pleiades» — the mushabbah.", "«Süreyya» — müşebbeh."),
  tok("بِعُنْقُودِ","unqud","noun",[Q,A,"huruf-jarr","idafa-definiteness"], "الْبَاءُ جَارَّةٌ وَعُنْقُودِ مَجْرُورٌ مُضَافٌ — الْمُشَبَّهُ بِهِ.", "«to a cluster of» — the bihi.", "«salkımına» — bih.",
      segments=[seg("بِ","bi","part"), seg("عُنْقُودِ","unqud","noun")]),
  tok("الْمُلَّاحِيَّةِ","mullahiyya","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«white grapes» — the wajh (unspoken here) is the hay'a of ch48.", "«beyaz üzümün» — vech (burada söylenmemiş) 48. bâbın hey'etidir.", punct=".")]})

# ----------- s17 — mujmal (RESTORED frame, printed example)
S.append({"id": "s17", "translation": {
 "en": "The mujmal is that whose wajh is not mentioned — for instance: «Zayd is like the lion.»" + R_EN,
 "tr": "Mücmel, vechi zikredilmeyen teşbihtir — meselâ: «Zeyd arslan gibidir.»" + R_TR},
 "tashbih": frame([6], 7, [7], [], "mursal-mujmal", "mufrad", "mufrad", None, rank="mid"),
 "tokens": [
  tok("وَالْمُجْمَلُ","mujmal","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the mujmal» — the mubtada.", "«mücmel» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُجْمَلُ","mujmal","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that whose».", "«… olan»."),
  tok("لَمْ","lam-jazima","part",[Q,"lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-medi»."),
  tok("يُذْكَرْ","dhakara","verb",[Q,"lam-jazim","naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ — صِلَةٌ.", "«is mentioned» — jazm.", "«zikredilmez» — meczum."),
  tok("وَجْهُهُ","wajh","noun",[Q,W,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its wajh».", "«vechi».",
      segments=[seg("وَجْهُ","wajh","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("نَحْوُ","nahw","noun",[Q,"mubtada-khabar"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: وَذَٰلِكَ نَحْوُ — يُدْخِلُ مِثَالًا، لَا أَدَاةَ تَشْبِيهٍ.", "«for instance» — a wall: it introduces the example and is no adat.", "«meselâ» — duvar: örneği getirir, edat değildir.", punct=":"),
  tok("زَيْدٌ","zayd","propn",[Q,A,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — الْمُشَبَّهُ.", "«Zayd» — the mushabbah.", "«Zeyd» — müşebbeh."),
  tok("كَالْأَسَدِ","asad","noun",[Q,A,"huruf-jarr","tashbih"], "الْكَافُ لِلتَّشْبِيهِ، وَالْأَسَدِ مَجْرُورٌ — خَبَرٌ. الْمُشَبَّهُ بِهِ، وَلَا وَجْهَ مَذْكُورٌ: مُجْمَلٌ.", "«like the lion» — the bihi; no wajh spoken: MUJMAL.", "«arslan gibi» — bih; vech söylenmemiş: MÜCMEL.",
      segments=[seg("كَ","ka","part"), seg("الْأَسَدِ","asad","noun")], punct=".")]})

# ----------- s18 — the Arabs' hidden mujmal (as printed)
S.append({"id": "s18", "translation": {
 "en": "«They are like the cast ring: none knows where its two ends are.»",
 "tr": "«Onlar, iki ucunun nerede olduğu bilinmeyen dökme halka gibidir.»"},
 "tashbih": frame([0], 1, [1, 2], [], "mursal-mujmal", "mufrad", "mufrad", None, rank="mid"),
 "tokens": [
  tok("هُمْ","hum","pron",[Q,A,"mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — الْمُشَبَّهُ.", "«they» — the mushabbah.", "«onlar» — müşebbeh."),
  tok("كَالْحَلْقَةِ","halqa","noun",[Q,A,"huruf-jarr","tashbih"], "الْكَافُ لِلتَّشْبِيهِ، وَالْحَلْقَةِ مَجْرُورٌ — خَبَرٌ. الْمُشَبَّهُ بِهِ، مَوْصُوفٌ.", "«like the ring» — the bihi, described by what follows.", "«halka gibi» — bih, ardındakiyle vasıflanmış.",
      segments=[seg("كَ","ka","part"), seg("الْحَلْقَةِ","halqa","noun")]),
  tok("الْمُفْرَغَةِ","mufragh","noun",[Q,"naat-sifa","ism-maful","form-iv-verbs"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ أَفْرَغَ: صُبَّتْ فِي قَالَبٍ.", "«cast» — na't: poured in one mould, seamless.", "«dökme» — sıfat: bir kalıba dökülmüş, eksiz."),
  tok("لَا","la-nafiya","part",[Q], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يُدْرَى","dara","verb",[Q,"naib-al-fail","naqis-verbs","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ بَعْدَهُ — وَالْجُمْلَةُ حَالٌ مِنَ الْحَلْقَةِ.",
      "«it is not known» — the majhul of دَرَى; the question-clause is its deputy; the whole is a hal of the ring. The wajh is HIDDEN in the description: that its parts match — only the knowing see it.",
      "«bilinmez» — دَرَى'nın meçhulü; soru cümlesi nâibi; bütünü halkadan hâl. Vech tasvirin içinde GİZLİ: parçalarının denkliği — yalnız bilenler görür."),
  tok("أَيْنَ","ayna","noun",[Q,"al-istifham","mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ خَبَرٌ مُقَدَّمٌ.", "«where» — a fronted khabar.", "«nerede» — mukaddem haber."),
  tok("طَرَفَاهَا","taraf","noun",[Q,A,"mubtada-khabar","al-muthanna","idafa-definiteness"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهَا مُضَافٌ إِلَيْهِ.",
      "«its two ends» — the dual mubtada by its alif, the nun gone for the idafa, هَا annexed: the letter-noun with its pronoun.", "«iki ucu» — elifle tesniye mübtedâ, nûnu izâfet için düşmüş, هَا muzâf: zamirli harf-isim.",
      segments=[seg("طَرَفَا","taraf","noun"), seg("هَا","pron-3fs","pron")], punct=".")]})

# ----------- s19 — mufassal (RESTORED frame, printed example)
S.append({"id": "s19", "translation": {
 "en": "The mufassal is that whose wajh is mentioned — for instance: «He is like honey in sweetness.»" + R_EN,
 "tr": "Mufassal, vechi zikredilen teşbihtir — meselâ: «O, tatlılıkta bal gibidir.»" + R_TR},
 "tashbih": frame([5], 6, [6], [7, 8], "mursal-mufassal", "mufrad", "mufrad", "mufrad", rank="adna"),
 "tokens": [
  tok("وَالْمُفَصَّلُ","mufassal","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the mufassal» — the mubtada.", "«mufassal» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُفَصَّلُ","mufassal","noun")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that whose».", "«… olan»."),
  tok("ذُكِرَ","dhakara","verb",[Q,"naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is mentioned».", "«zikredilir»."),
  tok("وَجْهُهُ","wajh","noun",[Q,W,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its wajh».", "«vechi».",
      segments=[seg("وَجْهُ","wajh","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("نَحْوُ","nahw","noun",[Q,"mubtada-khabar"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ — يُدْخِلُ الْمِثَالَ.", "«for instance» — the wall.", "«meselâ» — duvar.", punct=":"),
  tok("هُوَ","huwa","pron",[Q,A,"mubtada-khabar"], "مُبْتَدَأٌ — الْمُشَبَّهُ.", "«he» — the mushabbah.", "«o» — müşebbeh."),
  tok("كَالْعَسَلِ","asal","noun",[Q,A,"huruf-jarr","tashbih"], "الْكَافُ لِلتَّشْبِيهِ، وَالْعَسَلِ مَجْرُورٌ — خَبَرٌ. الْمُشَبَّهُ بِهِ.", "«like honey» — the bihi.", "«bal gibi» — bih.",
      segments=[seg("كَ","ka","part"), seg("الْعَسَلِ","asal","noun")]),
  tok("فِي","fi","part",[Q,W,"huruf-jarr"], "حَرْفُ جَرٍّ — يَبْدَأُ وَجْهَ الشَّبَهِ.", "«in» — the wajh begins.", "«-de» — vech başlar."),
  tok("الْحَلَاوَةِ","halawa","noun",[Q,W,"huruf-jarr"],
      "اسْمٌ مَجْرُورٌ — وَجْهُ الشَّبَهِ مَذْكُورٌ: مُفَصَّلٌ. وَفِيهِ تَسَامُحٌ: الْوَجْهُ فِي الْحَقِيقَةِ مَيْلُ الطَّبْعِ، وَالْحَلَاوَةُ لَازِمُهُ.",
      "«sweetness» — the wajh SPOKEN: mufassal (with the books' licence: the true wajh is what sweetness entails, the inclination of the taste).",
      "«tatlılık» — vech SÖYLENMİŞ: mufassal (kitapların müsamahasıyla: gerçek vech tatlılığın lâzımı olan tabiat meylidir).",
      punct=".")]})

# ----------- s20 — the near and hackneyed (RESTORED)
S.append({"id": "s20", "translation": {
 "en": "The near-and-hackneyed is that in which one passes from the mushabbah to the mushabbah bihi without scrutiny, because its wajh shows at first sight." + R_EN,
 "tr": "Karîb-i mübtezel, vechi ilk bakışta göründüğü için müşebbehten müşebbehün bihe araştırmaksızın geçilen teşbihtir." + R_TR},
 "tokens": [
  tok("وَالْقَرِيبُ","qarib","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the near» — the mubtada.", "«karîb» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْقَرِيبُ","qarib","noun")]),
  tok("الْمُبْتَذَلُ","mubtadhal","noun",[Q,"naat-sifa","ism-maful"], "نَعْتٌ مَرْفُوعٌ.", "«hackneyed» — na't.", "«mübtezel» — sıfat."),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that in which».", "«… olan»."),
  tok("يُنْتَقَلُ","intaqala","verb",[Q,"naib-al-fail","form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«one passes» — an impersonal majhul; the jarr-phrase is its deputy.", "«geçilir» — gayr-i şahsî meçhul; câr-mecrûr nâibidir."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr","naib-al-fail"], "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — الْعَائِدُ.", "«in it» — the deputy and the returning pronoun.", "«onda» — nâib ve âid.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("مِنَ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[Q,A,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the mushabbah».", "«müşebbeh»."),
  tok("إِلَى","ila","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[Q,A,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the … likened-to».", "«benzetilen»."),
  tok("بِهِ","bi","part",[Q,A,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«bihi».", "«bih».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("مِنْ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«without».", "«-sızın»."),
  tok("غَيْرِ","ghayr","noun",[Q,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ مُضَافٌ.", "«(with)out».", "«-sızın»."),
  tok("تَدَقُّقٍ","tadaqquq","noun",[Q,"idafa-definiteness","masdar","form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَدَقَّقَ.", "«scrutiny».", "«araştırma».", punct="،"),
  tok("لِظُهُورِ","zuhur","noun",[Q,"huruf-jarr","lam-taleel","idafa-definiteness","masdar"], "اللَّامُ لِلتَّعْلِيلِ، وَظُهُورِ مَجْرُورٌ مُضَافٌ.", "«because of the showing of».", "«göründüğü için».",
      segments=[seg("لِ","li","part"), seg("ظُهُورِ","zuhur","noun")]),
  tok("وَجْهِهِ","wajh","noun",[Q,W,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its wajh».", "«vechinin».",
      segments=[seg("وَجْهِ","wajh","noun"), seg("هِ","pron-3ms","pron")]),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  tok("بَادِئِ","badi-first","noun",[Q,"huruf-jarr","idafa-definiteness","ism-fail"], "اسْمٌ مَجْرُورٌ مُضَافٌ — اسْمُ فَاعِلٍ مِنْ بَدَأَ.", "«the first of» — the ism fa'il of بَدَأَ.", "«ilki» — بَدَأَ'nin ism-i fâili."),
  tok("الرَّأْيِ","ray","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فِي بَادِئِ الرَّأْيِ: عِنْدَ أَوَّلِ النَّظَرِ.", "«sight» — at first glance.", "«bakış» — ilk bakışta.", punct=".")]})

# ----------- s21 — the far and rare (RESTORED)
S.append({"id": "s21", "translation": {
 "en": "The far-and-rare is the opposite — as in likening the sun to a mirror in the hand of the palsied." + R_EN,
 "tr": "Baîd-i garîb bunun aksidir — güneşi titrek ellinin elindeki aynaya benzetmek gibi." + R_TR},
 "tashbih": frame([4], 3, [5, 6, 7, 8], [], "mursal-mujmal", "mufrad", "muqayyad", None),
 "tokens": [
  tok("وَالْبَعِيدُ","baid","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the far» — the mubtada.", "«baîd» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْبَعِيدُ","baid","noun")]),
  tok("الْغَرِيبُ","gharib","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«rare» — na't.", "«garîb» — sıfat."),
  tok("بِخِلَافِهِ","khilaf","noun",[Q,"huruf-jarr","idafa-definiteness"], "الْبَاءُ جَارَّةٌ وَخِلَافِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«is its opposite» — the khabar-phrase.", "«aksidir» — haber tamlaması.",
      segments=[seg("بِ","bi","part"), seg("خِلَافِ","khilaf","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("كَتَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"], "الْكَافُ لِلتَّمْثِيلِ، وَتَشْبِيهِ مَجْرُورٌ مُضَافٌ — الْأَدَاةُ.", "«as in the likening of» — the masdar-adat.", "«benzetmek gibi» — masdar-edat.",
      segments=[seg("كَ","ka","part"), seg("تَشْبِيهِ","tashbih","noun")]),
  tok("الشَّمْسِ","shams","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«the sun» — the mushabbah.", "«güneşi» — müşebbeh."),
  tok("بِالْمِرْآةِ","mirat","noun",[Q,A,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَالْمِرْآةِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to the mirror» — the bihi.", "«aynaya» — bih.",
      segments=[seg("بِ","bi","part"), seg("الْمِرْآةِ","mirat","noun")]),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ — قَيْدٌ عَلَى الْمُشَبَّهِ بِهِ.", "«in» — a restriction on the bihi, not the wajh.", "«-de» — bih üzerinde kayıt, vech değil."),
  tok("كَفِّ","kaff","noun",[Q,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ مُضَافٌ.", "«the hand of».", "«elinde»."),
  tok("الْأَشَلِّ","ashall","noun",[Q,"idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّ الْأَلِفَ وَاللَّامَ تُعِيدَانِهَا. غَرَابَتُهُ مِنْ كَثْرَةِ التَّفْصِيلِ فِي الْوَجْهِ وَقِلَّةِ تَكَرُّرِ الْمُشَبَّهِ بِهِ عَلَى الْحِسِّ.",
      "«the palsied» — the article gives the diptote its kasra back. Rare on two counts: much detail in the wajh, and a bihi the senses seldom meet.",
      "«titrek ellinin» — harf-i tarif gayr-i munsarife kesrasını geri verir. İki yönden garîb: vechte çok tafsil, ve duyunun nadir karşılaştığı bir bih.",
      punct=".")]})

# ----------- s22 — by the adat (RESTORED)
S.append({"id": "s22", "translation": {
 "en": "And with regard to the adat: either muakkad — that whose adat is dropped — or mursal, which is the opposite." + R_EN,
 "tr": "Edat bakımından: ya müekked — edatı hazfedilen — ya mürsel, ki onun aksidir." + R_TR},
 "tokens": [
  tok("وَبِاعْتِبَارِ","itibar","noun",[Q,"huruf-jarr","idafa-definiteness"], "خَبَرٌ مُقَدَّمٌ.", "«and with regard to».", "«ve … bakımından».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("الْأَدَاةِ","adat","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the adat».", "«edat»."),
  tok("إِمَّا","imma","part",[Q,"atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("مُؤَكَّدٌ","muakkad","noun",[Q,"mubtada-khabar","ism-maful","form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ — اسْمُ مَفْعُولٍ مِنْ أَكَّدَ.", "«muakkad» — the strengthened likening.", "«müekked» — kuvvetlendirilmiş benzetme."),
  tok("وَهُوَ","huwa","pron",[Q,"mubtada-khabar"], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it is».", "«o da»."
      , segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "خَبَرٌ.", "«that whose».", "«… olan»."),
  tok("حُذِفَتْ","hadhafa","verb",[Q,"naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ — صِلَةٌ.", "«is dropped» — the sila.", "«hazfedilir» — sıla."),
  tok("أَدَاتُهُ","adat","noun",[Q,A,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its adat».", "«edatı».",
      segments=[seg("أَدَاتُ","adat","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"], "لِلتَّفْصِيلِ.", "«or».", "«ya da».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("مُرْسَلٌ","mursal","noun",[Q,"atf-nasaq","ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ أَرْسَلَ: أُطْلِقَ بِأَدَاتِهِ.", "«mursal» — sent forth with its adat.", "«mürsel» — edatıyla salınmış."),
  tok("وَهُوَ","huwa","pron",[Q,"mubtada-khabar"], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it is».", "«o da».", segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("بِخِلَافِهِ","khilaf","noun",[Q,"huruf-jarr","idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its opposite» — the adat kept.", "«aksidir» — edat korunmuş.",
      segments=[seg("بِ","bi","part"), seg("خِلَافِ","khilaf","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s23 — the aya 27:88: muakkad by the maf'ul mutlaq
S.append({"id": "s23", "translation": {
 "en": "«— while they pass as the clouds pass.» (27:88)",
 "tr": "«— hâlbuki onlar bulutun geçişi gibi geçer.» (27:88)"},
 "tashbih": {"mushabbah": [0], "adat": None, "bihi": [3], "wajh": [], "kind": "muakkad-mujmal",
             "shape": {"mushabbah": "mufrad", "bihi": "mufrad", "wajh": None}, "rank": "ala"},
 "tokens": [
  tok("وَهِيَ","hiya","pron",[Q,A,"mubtada-khabar","hal","anwa-al-waw"], "الْوَاوُ لِلْحَالِ، وَهِيَ مُبْتَدَأٌ — الْمُشَبَّهُ: الْجِبَالُ.", "«while they» — the mubtada: the MUSHABBAH (the mountains).", "«hâlbuki onlar» — mübtedâ: MÜŞEBBEH (dağlar).",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("تَمُرُّ","marra","verb",[Q,"doubled-verbs","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«pass» — the geminate mudari; the clause is the khabar.", "«geçer» — muzâaf muzâri; cümle haber."),
  tok("مَرَّ","marr-passing","noun",[Q,A,"maful-mutlaq","masdar","idafa-definiteness","tashbih"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ مُضَافٌ — أَصْلُهُ: مَرًّا مِثْلَ مَرِّ السَّحَابِ: حُذِفَتِ الْأَدَاةُ وَأُقِيمَ الْمَصْدَرُ مَقَامَهَا.",
      "«(as) the passing of» — the maf'ul mutlaq standing where the adat was (مَرًّا مِثْلَ مَرِّ): MUAKKAD, the adat dropped.",
      "«geçişi (gibi)» — edatın yerinde duran mef'ûl-i mutlak (مَرًّا مِثْلَ مَرِّ): MÜEKKED, edat düşmüş."),
  tok("السَّحَابِ","sahab","noun",[Q,A,"idafa-definiteness","tashbih"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ. لَا أَدَاةَ وَلَا وَجْهَ: الْمَرْتَبَةُ الْعُلْيَا.",
      "«the clouds» — the bihi. No adat, no wajh: the HIGHEST rank.", "«bulutun» — bih. Ne edat ne vech: EN YÜKSEK mertebe.",
      punct=".")]})

# ----------- s24 — Ibn Khafaja: the bihi annexed to the mushabbah (as printed)
S.append({"id": "s24", "translation": {
 "en": "«And the wind toys with the branches, while the gold of the evening light has run over the silver of the water.»",
 "tr": "«Rüzgâr dallarla oynaşıyor; ikindi güneşinin altını, suyun gümüşü üzerinde akmış.»"},
 "tashbih": {"mushabbah": [6], "adat": None, "bihi": [5], "wajh": [], "kind": "muakkad-mujmal",
             "shape": {"mushabbah": "mufrad", "bihi": "mufrad", "wajh": None}, "rank": "ala"},
 "tokens": [
  tok("وَالرِّيحُ","rih","noun",[Q,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالرِّيحُ مُبْتَدَأٌ.", "«and the wind» — the mubtada.", "«rüzgâr» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الرِّيحُ","rih","noun")]),
  tok("تَعْبَثُ","abatha","verb",[Q,"mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«toys» — the verbal khabar.", "«oynaşır» — fiil cümlesi haber."),
  tok("بِالْغُصُونِ","ghusn","noun",[Q,"huruf-jarr","jam-taksir"], "الْبَاءُ جَارَّةٌ وَالْغُصُونِ مَجْرُورٌ — جَمْعُ غُصْنٍ.", "«with the branches».", "«dallarla».",
      segments=[seg("بِ","bi","part"), seg("الْغُصُونِ","ghusn","noun")]),
  tok("وَقَدْ","qad","part",[Q,"hal","anwa-al-waw"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«while indeed» — the waw of hal.", "«hâlbuki» — hâl vâvı.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("جَرَى","jara","verb",[Q,"naqis-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«has run».", "«akmış»."),
  tok("ذَهَبُ","dhahab-gold","noun",[Q,A,"fail","idafa-definiteness","tashbih"],
      "فَاعِلٌ مَرْفُوعٌ مُضَافٌ — الْمُشَبَّهُ بِهِ مُضَافٌ إِلَى الْمُشَبَّهِ: أَصْلُهُ أَصِيلٌ كَالذَّهَبِ، حُذِفَتِ الْأَدَاةُ وَقُدِّمَ الْمُشَبَّهُ بِهِ.",
      "«the gold of» — the fa'il: the BIHI annexed to its mushabbah (an evening like gold → the gold of the evening): MUAKKAD by idafa.",
      "«altını» — fâil: müşebbehine muzâf BİH (altın gibi ikindi → ikindinin altını): izâfetle MÜEKKED."),
  tok("الْأَصِيلِ","asil","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ: وَقْتُ الْعَصْرِ.", "«the evening light» — the MUSHABBAH.", "«ikindinin» — MÜŞEBBEH."),
  tok("عَلَى","ala","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«üzerinde»."),
  tok("لُجَيْنِ","lujayn","noun",[Q,A,"huruf-jarr","idafa-definiteness","tashbih"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — مُشَبَّهٌ بِهِ ثَانٍ مُضَافٌ إِلَى مُشَبَّهِهِ: مَاءٌ كَاللُّجَيْنِ.",
      "«the silver of» — a second bihi annexed to its mushabbah (water like silver).", "«gümüşü» — müşebbehine muzâf ikinci bih (gümüş gibi su)."),
  tok("الْمَاءِ","ma-water","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«the water» — the mushabbah.", "«suyun» — müşebbeh.", punct=".")]})

# ----------- s25 — the ranks (RESTORED)
S.append({"id": "s25", "translation": {
 "en": "The highest rank of the tashbih in strength of exaggeration is that in which the adat and the wajh are dropped; then that in which one of them is dropped; then that in which both are mentioned." + R_EN,
 "tr": "Mübalağa kuvvetinde teşbihin en yüksek mertebesi, edatı ve vechi hazfedilendir; sonra ikisinden biri hazfedilen; sonra ikisi de zikredilen." + R_TR},
 "tokens": [
  tok("وَأَعْلَى","ala-highest","noun",[Q,"mubtada-khabar","ism-tafdil","idafa-definiteness","ism-maqsur-manqus"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَأَعْلَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَهُوَ مُضَافٌ — اسْمُ تَفْضِيلٍ مَقْصُورٌ.",
      "«the highest of» — the mubtada, an ism tafdil that is also a maqsur, annexed.", "«en yükseği» — mübtedâ, aynı zamanda maksûr ism-i tafdil, muzâf.",
      segments=[seg("وَ","wa","conj"), seg("أَعْلَى","ala-highest","noun")]),
  tok("مَرَاتِبِ","martaba","noun",[Q,"idafa-definiteness","jam-taksir","mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ — جَمْعُ مَرْتَبَةٍ عَلَى مَفَاعِلَ؛ الْإِضَافَةُ تُعِيدُ الْكَسْرَةَ.", "«the ranks of» — a heaviest-shape plural given its kasra by the idafa.", "«mertebelerinin» — izâfetle kesrasını alan en ağır kalıp çoğul."),
  tok("التَّشْبِيهِ","tashbih","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tashbih».", "«teşbihin»."),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("قُوَّةِ","quwwa","noun",[Q,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ مُضَافٌ.", "«strength of».", "«kuvvetinde»."),
  tok("الْمُبَالَغَةِ","mubalagha","noun",[Q,"idafa-definiteness","masdar","form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ بَالَغَ.", "«exaggeration».", "«mübalağanın»."),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that in which» — the khabar.", "«… olan» — haber."),
  tok("حُذِفَ","hadhafa","verb",[Q,"naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is dropped».", "«hazfedilir»."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْعَائِدُ.", "«in it».", "«onda».", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْأَدَاةُ","adat","noun",[Q,A,"naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the adat» — the deputy.", "«edat» — nâib."),
  tok("وَالْوَجْهُ","wajh","noun",[Q,W,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ — كِلَاهُمَا مَحْذُوفٌ: زَيْدٌ أَسَدٌ.", "«and the wajh» — both dropped: زَيْدٌ أَسَدٌ, the BALIGH.", "«ve vech» — ikisi de düşmüş: زَيْدٌ أَسَدٌ, BELÎĞ.",
      segments=[seg("وَ","wa","conj"), seg("الْوَجْهُ","wajh","noun")], punct="،"),
  tok("ثُمَّ","thumma","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then».", "«sonra»."),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","atf-nasaq"], "مَعْطُوفٌ عَلَى مَا الْأُولَى.", "«that in which».", "«… olan»."),
  tok("حُذِفَ","hadhafa","verb",[Q,"naib-al-fail"], "صِلَةٌ.", "«is dropped».", "«hazfedilir»."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("أَحَدُهُمَا","ahad","noun",[Q,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ — الْمَرْتَبَةُ الْوُسْطَى: زَيْدٌ كَالْأَسَدِ، زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ.", "«one of the two» — the MIDDLE rank: زَيْدٌ كَالْأَسَدِ or زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ.", "«ikisinden biri» — ORTA mertebe: زَيْدٌ كَالْأَسَدِ yahut زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ.",
      segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")], punct="،"),
  tok("ثُمَّ","thumma","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("مَا","ma-mawsula","pron",[Q,"ism-mawsul","atf-nasaq"], "مَعْطُوفٌ.", "«that in which».", "«… olan»."),
  tok("ذُكِرَا","dhakara","verb",[Q,"naib-al-fail","al-muthanna"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَأَلِفُ الِاثْنَيْنِ نَائِبُ فَاعِلٍ — الْأَدَاةُ وَالْوَجْهُ.", "«both are mentioned» — the dual alif is the deputy: adat and wajh.", "«ikisi zikredilir» — tesniye elifi nâib: edat ve vech."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمَرْتَبَةُ الدُّنْيَا: زَيْدٌ كَالْأَسَدِ فِي الشَّجَاعَةِ.", "«in it» — the LOWEST rank: زَيْدٌ كَالْأَسَدِ فِي الشَّجَاعَةِ, mursal and mufassal.", "«onda» — EN AŞAĞI mertebe: زَيْدٌ كَالْأَسَدِ فِي الشَّجَاعَةِ, mürsel ve mufassal.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "pron-2d": g("كُمَا", None, "pron", "you two (the attached dual pronoun)", "siz ikiniz (bitişik tesniye zamiri)", 3),
 "raqim": g("رَاقِم", "ر ق م", "noun", "one who writes (ism fa'il of رَقَمَ)", "yazan (رَقَمَ'nin ism-i fâili)", 4),
 "bashshar": g("بَشَّار", "ب ش ر", "propn", "Bashshar b. Burd, the poet", "şair Beşşâr b. Bürd", 5),
 "mushmis": g("مُشْمِس", "ش م س", "noun", "sunny, sunlit (ism fa'il of أَشْمَسَ)", "güneşli (أَشْمَسَ'nin ism-i fâili)", 4),
 "zahar": g("زَهَر", "ز ه ر", "noun", "flowers, blossoms (collective)", "çiçekler (cins ismi)", 3, plural="أَزْهَار"),
 "ruba-hills": g("رُبًا", "ر ب و", "noun", "hills (plural of رَبْوَة; maqsur)", "tepeler (رَبْوَة'nin çoğulu; maksûr)", 5),
 "muqmir": g("مُقْمِر", "ق م ر", "noun", "moonlit (ism fa'il of أَقْمَرَ)", "mehtaplı (أَقْمَرَ'nin ism-i fâili)", 4),
 "taaddud": g("تَعَدُّد", "ع د د", "noun", "plurality, being several (masdar of تَعَدَّدَ)", "taaddüd, çokluk (تَعَدَّدَ'nin masdarı)", 4),
 "malfuf": g("مَلْفُوف", "ل ف ف", "noun", "wrapped, folded (ism maf'ul of لَفَّ); the malfuf tashbih", "melfûf, sarılmış (لَفَّ'nin ism-i mef'ûlü); melfûf teşbih", 5),
 "mafruq": g("مَفْرُوق", "ف ر ق", "noun", "separated (ism maf'ul of فَرَقَ); the mafruq tashbih", "mefrûk, ayrılmış (فَرَقَ'nin ism-i mef'ûlü); mefrûk teşbih", 5),
 "taswiya": g("تَسْوِيَة", "س و ي", "noun", "equalising (masdar of سَوَّى); the taswiya tashbih", "tesviye, eşitleme (سَوَّى'nın masdarı); tesviye teşbihi", 5),
 "awwalan": find_gloss("awwalan"),
 "qalb": find_gloss("qalb"),
 "tayr": find_gloss("tayr"),
 "ratb": g("رَطْب", "ر ط ب", "noun", "moist, fresh", "yaş, taze", 3),
 "yabis": g("يَابِس", "ي ب س", "noun", "dry (ism fa'il of يَبِسَ)", "kuru (يَبِسَ'nin ism-i fâili)", 3),
 "lada": find_gloss("lada"),
 "wakr": g("وَكْر", "و ك ر", "noun", "nest (of a bird of prey)", "yuva (yırtıcı kuş)", 5, plural="أَوْكَار"),
 "unnab": g("عُنَّاب", "ع ن ب", "noun", "jujube (the red fruit)", "hünnap", 5),
 "hashaf": g("حَشَف", "ح ش ف", "noun", "worthless dried dates", "çürük, kalitesiz hurma", 6),
 "bali": g("بَالٍ (الْبَالِي)", "ب ل ي", "noun", "worn out, decayed (ism fa'il of بَلِيَ; manqus)", "eskimiş, çürümüş (بَلِيَ'nin ism-i fâili; mankûs)", 4),
 "nashr-scent": g("نَشْر", "ن ش ر", "noun", "a sweet scent spreading", "yayılan güzel koku", 5),
 "dinar": find_gloss("dinar"),
 "anam-plant": g("عَنَم", "ع ن م", "noun", "anam, a soft red plant whose twigs dyed fingertips are likened to", "anem, kınalı parmak uçlarının benzetildiği yumuşak kızıl bitki", 6),
 "duna": find_gloss("duna"),
 "sudgh": g("صُدْغ", "ص د غ", "noun", "temple; the lock of hair at the temple", "şakak; zülüf", 5, plural="أَصْدَاغ"),
 "kila": g("كِلَا", "ك ل و", "noun", "both (annexed to a dual pronoun: كِلَاهُمَا)", "her ikisi (tesniye zamirine muzâf: كِلَاهُمَا)", 3),
 "thaghr": find_gloss("thaghr"),
 "safa": g("صَفَاء", "ص ف و", "noun", "clearness, purity (masdar of صَفَا)", "safâ, berraklık (صَفَا'nın masdarı)", 3),
 "lulu": g("لُؤْلُؤ", "ل أ ل أ", "noun", "pearls (collective; pl. لَآلِئ / لَآلِي)", "inci (cins ismi; ç. لَآلِئ / لَآلِي)", 3, plural="لَآلِئ"),
 "munaddad": g("مُنَضَّد", "ن ض د", "noun", "strung, arranged in rows (ism maf'ul of نَضَّدَ)", "dizili, sıralanmış (نَضَّدَ'nin ism-i mef'ûlü)", 5),
 "barad": g("بَرَد", "ب ر د", "noun", "hail", "dolu", 3),
 "uqah": g("أَقَاحٍ (الْأَقَاحِي)", "ق ح و", "noun", "camomile flowers (plural of أُقْحُوَان; manqus)", "papatyalar (أُقْحُوَان'ın çoğulu; mankûs)", 6),
 "tamthil": g("تَمْثِيل", "م ث ل", "noun", "tamthil — the likening whose wajh is a composite picture (masdar of مَثَّلَ)", "temsil — vechi mürekkeb tablo olan benzetme (مَثَّلَ'nin masdarı)", 5),
 "mujmal": find_gloss("mujmal"),
 "mufassal": g("مُفَصَّل", "ف ص ل", "noun", "detailed; the tashbih whose wajh is spoken (ism maf'ul of فَصَّلَ)", "mufassal; vechi söylenen teşbih (فَصَّلَ'nin ism-i mef'ûlü)", 4),
 "qarib": find_gloss("qarib"),
 "mubtadhal": g("مُبْتَذَل", "ب ذ ل", "noun", "hackneyed, worn by use (ism maf'ul of ابْتَذَلَ)", "mübtezel, kullanıla kullanıla aşınmış (ابْتَذَلَ'nin ism-i mef'ûlü)", 5),
 "baid": find_gloss("baid"),
 "gharib": g("غَرِيب", "غ ر ب", "noun", "strange, rare", "garîb, nadir", 3, plural="غُرَبَاء"),
 "muntaza": g("مُنْتَزَع", "ن ز ع", "noun", "drawn out, extracted (ism maf'ul of انْتَزَعَ)", "çıkarılmış (انْتَزَعَ'nin ism-i mef'ûlü)", 5),
 "halqa": g("حَلْقَة", "ح ل ق", "noun", "ring, circle", "halka", 3, plural="حَلَقَات"),
 "mufragh": g("مُفْرَغ", "ف ر غ", "noun", "cast in a mould, seamless (ism maf'ul of أَفْرَغَ)", "kalıba dökülmüş, eksiz (أَفْرَغَ'nin ism-i mef'ûlü)", 5),
 "halawa": g("حَلَاوَة", "ح ل و", "noun", "sweetness", "tatlılık", 2),
 "tadaqquq": g("تَدَقُّق", "د ق ق", "noun", "scrutiny, close examination (masdar of تَدَقَّقَ)", "inceden inceye araştırma (تَدَقَّقَ'nin masdarı)", 5),
 "zuhur": find_gloss("zuhur"),
 "badi-first": g("بَادِئ", "ب د أ", "noun", "beginning, first (ism fa'il of بَدَأَ); فِي بَادِئِ الرَّأْيِ: at first sight", "ilk, başlangıç (بَدَأَ'nin ism-i fâili); فِي بَادِئِ الرَّأْيِ: ilk bakışta", 4),
 "muakkad": g("مُؤَكَّد", "أ ك د", "noun", "strengthened (ism maf'ul of أَكَّدَ); the tashbih with its adat dropped", "müekked (أَكَّدَ'nin ism-i mef'ûlü); edatı düşmüş teşbih", 4),
 "marr-passing": g("مَرّ", "م ر ر", "noun", "passing (masdar of مَرَّ)", "geçiş (مَرَّ'nin masdarı)", 3),
 "ghusn": g("غُصْن", "غ ص ن", "noun", "branch, bough", "dal", 2, plural="غُصُون"),
 "asil": g("أَصِيل", "أ ص ل", "noun", "the late afternoon, the evening light", "ikindi vakti, akşam üstü ışığı", 4),
 "lujayn": g("لُجَيْن", "ل ج ن", "noun", "silver (poetic)", "gümüş (şiirde)", 5),
 "ala-highest": g("أَعْلَى", "ع ل و", "noun", "highest, higher (ism tafdil; maqsur)", "en yüksek, daha yüksek (ism-i tafdil; maksûr)", 3),
 "martaba": find_gloss("martaba"),
 "quwwa": find_gloss("quwwa"),
 "ahad": find_gloss("ahad"),
 "taqassa": g("تَقَصَّى", "ق ص و", "verb", "to go to the farthest end, to pursue thoroughly (Form V)", "en uzağa gitmek, sonuna kadar araştırmak (V. bâb)", 5, form="V"),
 "tasawwara": find_gloss("tasawwara"),
 "taaddada": g("تَعَدَّدَ", "ع د د", "verb", "to be several, to multiply (Form V)", "birden çok olmak, çoğalmak (V. bâb)", 4, form="V"),
 "basama": g("بَسَمَ", "ب س م", "verb", "to smile", "gülümsemek", 3, form="I"),
 "dara": g("دَرَى", "د ر ي", "verb", "to know (naqis-ya); لَا يُدْرَى: it is not known", "bilmek (nâkıs-yâî); لَا يُدْرَى: bilinmez", 3, form="I"),
 "intaqala": g("انْتَقَلَ", "ن ق ل", "verb", "to move, pass from one thing to another (Form VIII)", "intikal etmek, geçmek (VIII. bâb)", 3, form="VIII"),
 "hadhafa": g("حَذَفَ", "ح ذ ف", "verb", "to drop, elide", "hazfetmek, düşürmek", 3, form="I"),
 "abatha": g("عَبِثَ", "ع ب ث", "verb", "to toy, play (with: بِ)", "oynaşmak, oyalanmak (بِ ile)", 4, form="I"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/50.json").write_text(
    json.dumps({"chapter": 50, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 50 for c in man["chapters"]):
    man["chapters"].append({"n": 50, "title": TITLE50})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.50.0"
ADD_EN = (" Chapter 50 (lines ~3290-3440, sahifa 113-119) carries the kinds of the tashbih: the sayings s2, s17 "
          "(inside a restored frame), s18 and s19 (inside a restored frame), the bayts s4-s5, s8, s10, s12, s14 "
          "and s24, and the aya s23 (27:88) are Arabic as the source prints it, with the rhyme sukun on عَنَمْ "
          "and the rhyme's bare damma on مُقْمِرُ kept; the source writes فَكَاََََنَّمَا with a run of fathas (s5) "
          "and كَاللاٰلِي with the dagger alif (s12) — the app writes فَكَأَنَّمَا and كَاللَّآلِي, the two divergences "
          "recorded here. s1, s3, s6-s7, s9, s11, s13, s15-s16, s20-s22 and s25 are RESTORATIONS, not "
          "quotations: the source carries those steps only in Ottoman-Turkish paraphrase, and the Arabic "
          "restores the matn's wording in the musannif's register; each is marked «restored» in its "
          "translation. Every likening carries an authored `tashbih` frame the engine is tested against — "
          "with, new in this chapter, the frame's TAʿADDUD (malfuf, mafruq, taswiya, jam) and its RANK by what "
          "is dropped (aʿla, mutawassit, adna); the category statements (تَشْبِيهُ مُفْرَدٍ بِمُفْرَدٍ) and the "
          "example-kaf (كَبَيْتِ بَشَّارٍ) are authored as no likening.")
ADD_TR = (" Ellinci bâb (satır ~3290-3440, sahife 113-119) teşbihin kısımlarını taşır: s2, s17 (geri yazılmış "
          "çerçeve içinde), s18 ve s19 (geri yazılmış çerçeve içinde) sözleri, s4-s5, s8, s10, s12, s14 ve s24 "
          "beyitleri ile s23 âyeti (27:88) kaynağın bastığı Arapçadır; عَنَمْ'deki kafiye sükûnu ve مُقْمِرُ'daki "
          "kafiyenin çıplak dammesi korunmuştur; kaynak فَكَاََََنَّمَا'yı üst üste fethalarla (s5) ve كَاللاٰلِي'yi "
          "hançer elifle (s12) yazar — uygulama فَكَأَنَّمَا ve كَاللَّآلِي yazar; iki fark burada kayıtlıdır. s1, "
          "s3, s6-s7, s9, s11, s13, s15-s16, s20-s22 ve s25 ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız "
          "Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her "
          "biri tercümesinde «geri yazılmıştır» diye işaretlidir. Her benzetme, motorun sınandığı müellif "
          "eliyle yazılmış bir `tashbih` çerçevesi taşır — bu bâbda yeni olarak çerçevenin TAADDÜDÜ (melfûf, "
          "mefrûk, tesviye, cem') ve düşene göre MERTEBESİ (a'lâ, mutavassıt, ednâ) ile; kısım cümleleri "
          "(تَشْبِيهُ مُفْرَدٍ بِمُفْرَدٍ) ve örnek kâfı (كَبَيْتِ بَشَّارٍ) benzetme değil diye yazılmıştır.")
if "3290-3440" not in man["attribution"]["en"]:
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
if "plural" not in gl["entries"]["kaff"]: gl["entries"]["kaff"]["plural"] = "أَكُفّ"
if "plural" not in gl["entries"]["layl"]: gl["entries"]["layl"]["plural"] = "لَيَالٍ"
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
V = mo["verbs"]
def put(key, e):
    if key not in V: V[key] = e
put("taqassa", _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَقَصَّ", "تَقَصّ", "a", "تَقَصّ", "تَقَصٍّ (التَّقَصِّي)", "مُتَقَصٍّ (الْمُتَقَصِّي)", None, None, None,
                                 "نَاقِصٌ: أَمْرُ الْمُثَنَّى تَقَصَّيَا — يَا صَاحِبَيَّ تَقَصَّيَا نَظَرَيْكُمَا."))
put("taaddada", _sg.derived(_sg.B5, _sg.W5, "َ", "تَعَدَّد", "تَعَدَّد", "تَعَدَّد", "تَعَدُّد", "مُتَعَدِّد"))
put("basama", _sg.sound1("daraba", "بَسَم", "بْسِم", "اِبْسِم", "بَسْم", "بَاسِم", None, None, None, "لَازِمٌ: يَبْسِمُ عَنْ ثَغْرٍ."))
put("dara", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "دَرَ", "دْر", "i", "اِدْر", "دِرَايَة", "دَارٍ (الدَّارِي)", "مَدْرِيّ", "دُرِيَ", "يُدْرَى",
                       "نَاقِصٌ يَائِيٌّ: دَرَى يَدْرِي؛ الْمَجْهُولُ يُدْرَى بِأَلِفٍ — لَا يُدْرَى أَيْنَ طَرَفَاهَا."))
put("intaqala", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَقَل", "نْتَقِل", "اِنْتَقِل", "اِنْتِقَال", "مُنْتَقِل", "مُنْتَقَل", "اُنْتُقِلَ", "يُنْتَقَلُ",
                            "لَازِمٌ: يُبْنَى لِلْمَجْهُولِ مَعَ الْجَارِّ وَالْمَجْرُورِ — يُنْتَقَلُ فِيهِ."))
put("hadhafa", _sg.sound1("daraba", "حَذَف", "حْذِف", "اِحْذِف", "حَذْف", "حَاذِف", "مَحْذُوف", "حُذِفَ", "يُحْذَفُ"))
put("abatha", _sg.sound1("samia", "عَبِث", "عْبَث", "اِعْبَث", "عَبَث", "عَابِث", None, None, None, "لَازِمٌ يَتَعَدَّى بِالْبَاءِ: تَعْبَثُ بِالْغُصُونِ."))
put("tasawwara", find_morph("tasawwara"))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the note
GR = ROOT / "content/grammar"
NOTE = {
 "id": "aqsam-al-tashbih",
 "title": {"ar": "أَقْسَامُ التَّشْبِيهِ — الطَّرَفَانِ وَالْوَجْهُ وَالْأَدَاةُ، وَمَرَاتِبُهُ",
           "en": "The kinds of tashbih — by the ends, the wajh, the adat — and its ranks",
           "tr": "Teşbihin kısımları — taraflar, vech, edat — ve mertebeleri"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — أقسام التشبيه، مراتب التشبيه"],
 "question": {
  "en": ["How many things stand at each end? Two mushabbahs first and then their two bihis is MALFUF (wrapped); each with its own beside it is MAFRUQ; several mushabbahs for one bihi is TASWIYA; one mushabbah for several bihis is JAM.",
         "Is the wajh a picture drawn from several things (TAMTHIL), spoken (MUFASSAL) or unspoken (MUJMAL), near and worn (QARIB MUBTADHAL) or far and rare (BAʿID GHARIB)?",
         "Is the adat there (MURSAL) or dropped (MUAKKAD) — and how much is dropped? Both adat and wajh: the highest rank; one: the middle; neither: the lowest."],
  "tr": ["Her tarafta kaç şey var? Önce iki müşebbeh, sonra iki bihleri MELFÛF; her biri kendi eşinin yanında MEFRÛK; bir bihe birkaç müşebbeh TESVİYE; bir müşebbehe birkaç bih CEM'.",
         "Vech birkaç şeyden çıkan bir tablo mu (TEMSİL), söylenmiş mi (MUFASSAL) söylenmemiş mi (MÜCMEL), yakın ve aşınmış mı (KARÎB-İ MÜBTEZEL) uzak ve nadir mi (BAÎD-İ GARÎB)?",
         "Edat var mı (MÜRSEL) düşmüş mü (MÜEKKED) — ve ne kadarı düşmüş? Edat da vech de: en yüksek mertebe; biri: orta; hiçbiri: en aşağı."]},
 "plain": {
  "en": "A likening is sorted three ways: by its ENDS (single or composite; how many stand at each end), by its WAJH (a picture or not; spoken or not; near or far), by its ADAT (kept or dropped). The engine counts the ends, reads the wajh's shape, checks the adat, and ranks by what is dropped.",
  "tr": "Bir benzetme üç yoldan tasnif edilir: TARAFLARINA göre (tek mi mürekkeb mi; her tarafta kaç şey var), VECHİNE göre (tablo mu değil mi; söylenmiş mi; yakın mı uzak mı), EDATINA göre (var mı düşmüş mü). Motor tarafları sayar, vechin şeklini okur, edatın varlığına bakar ve benzetmeyi düşene göre sıralar."},
 "explanation": {
  "en": "BY THE TWO ENDS: single to single (هُوَ كَالرَّاقِمِ عَلَى الْمَاءِ — both restricted), composite to composite (Bashshar's dust and swords), single to composite (the anemone), composite to single (Abu Tammam's sunlit day mixed with flowers فَكَأَنَّمَا هُوَ مُقْمِرُ). BY THE NUMBER OF THE ENDS: MALFUF — the mushabbahs first, then their bihis in order, كَأَنَّ قُلُوبَ الطَّيْرِ رَطْبًا وَيَابِسًا لَدَى وَكْرِهَا الْعُنَّابُ وَالْحَشَفُ الْبَالِي; MAFRUQ — each with its own beside it, النَّشْرُ مِسْكٌ وَالْوُجُوهُ دَنَانِيرُ وَأَطْرَافُ الْأَكُفِّ عَنَمْ; TASWIYA — several mushabbahs, one bihi, صُدْغُ الْحَبِيبِ وَحَالِي كِلَاهُمَا كَاللَّيَالِي; JAM — one mushabbah, several bihis, كَأَنَّمَا يَبْسِمُ عَنْ لُؤْلُؤٍ مُنَضَّدٍ أَوْ بَرَدٍ أَوْ أَقَاحٍ. BY THE WAJH: TAMTHIL when the wajh is drawn from several things (the Pleiades and the grape-cluster), else not; MUJMAL when the wajh is unspoken — plain (زَيْدٌ كَالْأَسَدِ) or hidden in the description (هُمْ كَالْحَلْقَةِ الْمُفْرَغَةِ لَا يُدْرَى أَيْنَ طَرَفَاهَا: that their parts match) — and MUFASSAL when spoken (وَثَغْرُهُ فِي صَفَاءٍ وَأَدْمُعِي كَاللَّآلِي; هُوَ كَالْعَسَلِ فِي الْحَلَاوَةِ, with the licence that the true wajh is what sweetness entails); QARIB MUBTADHAL when one passes from the mushabbah to the bihi without scrutiny because the wajh shows at first sight (the wajh is summary, or the bihi comes readily to mind), BAʿID GHARIB when it does not (much detail in the wajh, or a bihi the mind seldom reaches: the sun as a mirror in a palsied hand). BY THE ADAT: MUAKKAD when the adat is dropped — وَهِيَ تَمُرُّ مَرَّ السَّحَابِ (the masdar in the adat's place), and the bihi annexed to its mushabbah, وَالرِّيحُ تَعْبَثُ بِالْغُصُونِ وَقَدْ جَرَى ذَهَبُ الْأَصِيلِ عَلَى لُجَيْنِ الْمَاءِ — MURSAL when kept. THE RANKS by strength of claim: highest when both adat and wajh are dropped (زَيْدٌ أَسَدٌ — the baligh), middle when one is (زَيْدٌ كَالْأَسَدِ; زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ), lowest when both stand (زَيْدٌ كَالْأَسَدِ فِي الشَّجَاعَةِ). WHAT THE ENGINE CLAIMS: the COUNT of each end from the joined members and hal-pairs inside it (وَ counts; أَوْ counts the bihi's alternatives; a picture counts as one) and so the ta'addud — malfuf, mafruq (several likenings in one line, each closed), taswiya, jam; the RANK from what it finds dropped; mufassal/mujmal from a spoken wajh; and tamthil from the wajh's shape. Near/far and the hidden wajh are knowledge of the two things: the lab lists them, the frame does not claim them.",
  "tr": "İKİ TARAFA GÖRE: tekin tek'e (هُوَ كَالرَّاقِمِ عَلَى الْمَاءِ — ikisi de kayıtlı), mürekkebin mürekkebe (Beşşâr'ın tozu ve kılıçları), tekin mürekkebe (şakāyık), mürekkebin tek'e (Ebû Temmâm'ın çiçek karışmış güneşli gündüzü فَكَأَنَّمَا هُوَ مُقْمِرُ). TARAFLARIN SAYISINA GÖRE: MELFÛF — önce müşebbehler, sonra sırayla bihleri, كَأَنَّ قُلُوبَ الطَّيْرِ رَطْبًا وَيَابِسًا لَدَى وَكْرِهَا الْعُنَّابُ وَالْحَشَفُ الْبَالِي; MEFRÛK — her biri kendi eşinin yanında, النَّشْرُ مِسْكٌ وَالْوُجُوهُ دَنَانِيرُ وَأَطْرَافُ الْأَكُفِّ عَنَمْ; TESVİYE — birkaç müşebbeh, tek bih, صُدْغُ الْحَبِيبِ وَحَالِي كِلَاهُمَا كَاللَّيَالِي; CEM' — tek müşebbeh, birkaç bih, كَأَنَّمَا يَبْسِمُ عَنْ لُؤْلُؤٍ مُنَضَّدٍ أَوْ بَرَدٍ أَوْ أَقَاحٍ. VECHE GÖRE: vech birkaç şeyden çıkarılınca TEMSİL (Süreyya ve üzüm salkımı), yoksa değil; vech söylenmemişse MÜCMEL — açık (زَيْدٌ كَالْأَسَدِ) yahut tasvirde gizli (هُمْ كَالْحَلْقَةِ الْمُفْرَغَةِ لَا يُدْرَى أَيْنَ طَرَفَاهَا: parçalarının denkliği) — söylenmişse MUFASSAL (وَثَغْرُهُ فِي صَفَاءٍ وَأَدْمُعِي كَاللَّآلِي; هُوَ كَالْعَسَلِ فِي الْحَلَاوَةِ, gerçek vechin tatlılığın lâzımı olduğu müsamahasıyla); vech ilk bakışta göründüğünden müşebbehten bihe araştırmasız geçilince KARÎB-İ MÜBTEZEL (vech icmâlî, yahut bih akla hemen gelir), geçilmeyince BAÎD-İ GARÎB (vechte çok tafsil, yahut zihnin nadir ulaştığı bir bih: titrek eldeki ayna olarak güneş). EDATA GÖRE: edat düşünce MÜEKKED — وَهِيَ تَمُرُّ مَرَّ السَّحَابِ (edatın yerinde masdar) ve müşebbehine muzâf bih, وَالرِّيحُ تَعْبَثُ بِالْغُصُونِ وَقَدْ جَرَى ذَهَبُ الْأَصِيلِ عَلَى لُجَيْنِ الْمَاءِ — korununca MÜRSEL. MERTEBELER iddianın kuvvetine göre: edat da vech de düşünce en yüksek (زَيْدٌ أَسَدٌ — belîğ), biri düşünce orta (زَيْدٌ كَالْأَسَدِ; زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ), ikisi de durunca en aşağı (زَيْدٌ كَالْأَسَدِ فِي الشَّجَاعَةِ). MOTORUN İDDİASI: her tarafın SAYISI, içindeki atıf üyelerinden ve hâl çiftlerinden (وَ sayar; أَوْ bihin seçeneklerini sayar; tablo bir sayılır) ve böylece taaddüd — melfûf, mefrûk (bir satırda kapanmış birkaç benzetme), tesviye, cem'; düşeni bularak MERTEBE; söylenen vechten mufassal/mücmel; vechin şeklinden temsil. Yakın/uzak ve gizli vech iki şeyin bilgisidir: lâboratuvar sıralar, çerçeve iddia etmez."},
 "examples": [
  {"ar": "كَأَنَّ قُلُوبَ الطَّيْرِ رَطْبًا وَيَابِسًا لَدَى وَكْرِهَا الْعُنَّابُ وَالْحَشَفُ الْبَالِي", "en": "malfuf: two mushabbahs (a hal pair), two bihis.", "tr": "melfûf: iki müşebbeh (hâl çifti), iki bih.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "النَّشْرُ مِسْكٌ وَالْوُجُوهُ دَنَانِيرُ وَأَطْرَافُ الْأَكُفِّ عَنَمْ", "en": "mafruq, three baligh likenings — the highest rank.", "tr": "mefrûk, üç belîğ benzetme — en yüksek mertebe.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "صُدْغُ الْحَبِيبِ وَحَالِي كِلَاهُمَا كَاللَّيَالِي", "en": "taswiya: كِلَاهُمَا closes the two mushabbahs.", "tr": "tesviye: كِلَاهُمَا iki müşebbehi kapatır.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "كَأَنَّمَا يَبْسِمُ عَنْ لُؤْلُؤٍ مُنَضَّدٍ أَوْ بَرَدٍ أَوْ أَقَاحٍ", "en": "jam: أَوْ counts the bihis.", "tr": "cem': أَوْ bihleri sayar.", "sourceStory": "talkhis-al-miftah", "sentence": "s14"},
  {"ar": "وَهِيَ تَمُرُّ مَرَّ السَّحَابِ", "en": "muakkad: the masdar where the adat was; both dropped — the highest rank.", "tr": "müekked: edatın yerinde masdar; ikisi de düşmüş — en yüksek mertebe.", "sourceStory": "talkhis-al-miftah", "sentence": "s23"}],
 "commonMistakes": [
  {"wrong": "«النَّشْرُ مِسْكٌ وَالْوُجُوهُ دَنَانِيرُ: melfûf teşbih»",
   "right": "«Mefrûk: her müşebbeh kendi bihiyle yan yana; melfûf, müşebbehlerin önce, bihlerin sonra sıralanmasıdır»",
   "why": {"en": "Malfuf folds the ends (A B … A' B'); mafruq pairs them (A A', B B'). The engine reads the order of the members.", "tr": "Melfûf tarafları katlar (A B … A' B'); mefrûk eşler (A A', B B'). Motor üyelerin sırasını okur."}},
  {"wrong": "«زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ en yüksek mertebedir, çünkü edat yok»",
   "right": "«Orta mertebe: edat düşmüş ama vech söylenmiş; en yüksek, ikisinin de düştüğüdür (زَيْدٌ أَسَدٌ)»",
   "why": {"en": "Rank is counted by what is DROPPED: two, one, none. A spoken wajh weakens the claim as much as a kept adat.", "tr": "Mertebe DÜŞENE göre sayılır: iki, bir, hiç. Söylenen vech iddiayı, korunan edat kadar zayıflatır."}},
  {"wrong": "«فَكَأَنَّمَا هُوَ مُقْمِرُ: مُقْمِرُ merfû, tenvinsiz olduğu için gayr-i munsariftir»",
   "right": "«Tenvin kafiye için düşmüştür; مُقْمِر munsarif bir ism-i fâildir»",
   "why": {"en": "Poetry drops a tanwin at the rhyme. The engine keeps the printed form and records the licence; it does not infer a diptote from a rhyme.", "tr": "Şiir kafiyede tenvini düşürür. Motor basılı şekli korur ve ruhsatı kaydeder; kafiyeden gayr-i munsarif çıkarmaz."}}],
 "relatedNotes": ["arkan-al-tashbih", "wajh-al-shabah", "aqsam-wajh-al-shabah", "aghrad-al-tashbih", "tashbih", "ilm-al-bayan", "maful-mutlaq", "hal", "tawkid", "al-muthanna", "ya-al-mutakallim", "innama-kaffa", "mamnu-min-sarf"]}
(GR / "aqsam-al-tashbih.json").write_text(json.dumps(NOTE, ensure_ascii=False, indent=1), encoding="utf-8")
for nid in ("arkan-al-tashbih", "aqsam-wajh-al-shabah", "aghrad-al-tashbih"):
    w = json.loads((GR / f"{nid}.json").read_text(encoding="utf-8"))
    if "aqsam-al-tashbih" not in w["relatedNotes"]:
        w["relatedNotes"].append("aqsam-al-tashbih")
        (GR / f"{nid}.json").write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch50:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + 7 built, 1 copied; note aqsam-al-tashbih;",
      "frames:", sum(1 for x in S if x.get("tashbih")))
