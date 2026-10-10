# -*- coding: utf-8 -*-
"""Author chapter 51 of talkhis-al-miftah — الْحَقِيقَةُ وَالْمَجَازُ (sahifa 119-123,
lines ~3440-3570): the definitions of haqiqa and majaz, the ʿalaqa and the
qarina, the four kinds by convention, the majaz mursal with its relations
and the aya-examples the matn recites, the istiʿara with its four arkan, and
the qarina of the istiʿara.

  s1-s7, s10-s12, s20-s21 (frames)  — RESTORED from the source's Turkish.
  s8      Zuhayr's لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ … — as printed (the second
          hemistich لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ is the received text of the
          bayt, restored where the source prints the first hemistich only).
  s9      the aya 1:6 اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ — as printed.
  s13-s19 the received examples of the mursal — رَعَيْنَا الْغَيْثَ, أَمْطَرَتِ
          السَّمَاءُ نَبَاتًا, and the ayat 4:2, 12:36, 96:17, 3:107, 26:84 — as
          printed (the source writes وَاَتُوا for وَآتُوا; the app writes the
          standard وَآتُوا); each inside a restored frame كَقَوْلِهِ / كَقَوْلِهِ تَعَالَى.
  s21     رَأَيْتُ أَسَدًا يَرْمِي — as printed.
  s22     the bayt وَإِنْ تَعَافُوا الْعَدْلَ وَالْإِيمَانَا … — as printed, the alif of
          itlaq on الْإِيمَانَا / نِيرَانَا kept.

Every majaz carries an authored `majaz` frame the MajazEngine must read
back — the word by token index, its kind (mursal / istiara / nuqsan /
ziyada / aqli) and the ʿalaqa — and the likenings inside the istiʿara
examples are described, not framed (the mushabbah is dropped by
definition).

Grammar this chapter teaches: note `haqiqa-wa-majaz` extended by
`majaz-mursal` and `arkan-al-istiara` (group bayan); the alif of itlaq;
the manqus in idafa (شَاكِي السِّلَاحِ); the fa'il as a sifa-clause
(أَظْفَارُهُ لَمْ تُقَلَّمِ); paradigms اسْتَعْمَلَ، قَيَّدَ، تَحَقَّقَ، قَلَّمَ، رَعَى،
أَمْطَرَ، عَصَرَ، فَارَقَ، رَمَى، عَافَ; وَضَعَ، صَحَّ، أَخْرَجَ، هَدَى، آتَى، دَعَا،
جَعَلَ، رَأَى copied or already owned.
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
def mj(word, kind, alaqa=None, haqiqa=None, murad=None, qarina=None):
    f = {"word": word, "kind": kind}
    if alaqa: f["alaqa"] = alaqa
    if haqiqa: f["haqiqa"] = haqiqa
    if murad: f["murad"] = murad
    if qarina is not None: f["qarina"] = qarina
    return f
S = []
H = "haqiqa-majaz"; M = "majaz-mursal"; I = "arkan-al-istiara"; A = "arkan-al-tashbih"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
TITLE51 = {"ar": "الْحَقِيقَةُ وَالْمَجَازُ: الْعَلَاقَةُ وَالْقَرِينَةُ، الْمَجَازُ الْمُرْسَلُ، وَالِاسْتِعَارَةُ وَأَرْكَانُهَا",
           "en": "Haqiqa and Majaz: the ʿAlaqa and the Qarina, the Majaz Mursal, and the Istiʿara with its Arkan",
           "tr": "Hakikat ve Mecaz: Alâka ve Karîne, Mecâz-ı Mürsel, ve İstiâre ile Rükünleri"}

# ----------- s1 — haqiqa defined (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The haqiqa is the word used in what it was coined for, in the convention of the speakers." + R_EN,
 "tr": "Hakikat, konuşanların ıstılahında, kendisi için konulduğu mânâda kullanılan kelimedir." + R_TR},
 "tokens": [
  tok("الْحَقِيقَةُ","haqiqa","noun",[H,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the haqiqa» — the mubtada: the term defined.", "«hakikat» — mübtedâ: tarif edilen terim."),
  tok("الْكَلِمَةُ","kalima","noun",[H,"mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«the word» — the khabar: the genus.", "«kelime» — haber: cins."),
  tok("الْمُسْتَعْمَلَةُ","mustamal","noun",[H,"naat-sifa","ism-maful","form-x-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنِ اسْتَعْمَلَ.", "«used» — na't; the ism maf'ul of Form X.", "«kullanılan» — sıfat; X. bâbın ism-i mef'ûlü."),
  tok("فِيمَا","fi","part",[H,"huruf-jarr","ism-mawsul"], "فِي جَارَّةٌ وَمَا مَوْصُولَةٌ فِي مَحَلِّ جَرٍّ.", "«in what» — فِي + the relative مَا.", "«… şeyde» — فِي + mevsûl مَا.",
      segments=[seg("فِي","fi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("وُضِعَتْ","wadaa","verb",[H,"naib-al-fail","mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةٌ.", "«it was coined» — the sila: the word's first assignment (وَضْع).", "«konuldu» — sıla: kelimenin ilk tayini (vaz')."),
  tok("لَهُ","li","part",[H,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْعَائِدُ.", "«for it» — the returning pronoun.", "«onun için» — âid.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","part",[H,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("اصْطِلَاحِ","istilah","noun",[H,"huruf-jarr","idafa-definiteness","masdar","form-viii-verbs"], "اسْمٌ مَجْرُورٌ مُضَافٌ — مَصْدَرُ اصْطَلَحَ: تَوَاضُعُ قَوْمٍ عَلَى لَفْظٍ.", "«the convention of» — a group's agreed usage.", "«ıstılahında» — bir topluluğun uzlaştığı kullanım."),
  tok("التَّخَاطُبِ","takhatub","noun",[H,"idafa-definiteness","masdar","form-vi-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَخَاطَبَ. بِهٰذَا الْقَيْدِ يَخْرُجُ الْمَجَازُ: لِأَنَّهُ مُسْتَعْمَلٌ فِي غَيْرِ مَا وُضِعَ لَهُ.",
      "«the speakers» — the addressing that goes on among them. The clause keeps majaz OUT: it is used in what it was NOT coined for.",
      "«konuşanların» — aralarındaki hitaplaşma. Kayıt mecazı DIŞARIDA bırakır: o, konulmadığı mânâda kullanılır.",
      punct=".")]})

# ----------- s2 — majaz defined (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And the majaz is the word used in other than what it was coined for, in a way that is sound, together with a clue that the literal is not meant." + R_EN,
 "tr": "Mecaz ise, kendisi için konulduğundan başka mânâda, sahih bir vecih üzere, hakikatin kastedilmediğine dair bir karîneyle kullanılan kelimedir." + R_TR},
 "tokens": [
  tok("وَالْمَجَازُ","majaz","noun",[H,"mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْمَجَازُ مُبْتَدَأٌ.", "«and the majaz» — the mubtada.", "«mecaz ise» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمَجَازُ","majaz","noun")]),
  tok("الْكَلِمَةُ","kalima","noun",[H,"mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«the word».", "«kelime»."),
  tok("الْمُسْتَعْمَلَةُ","mustamal","noun",[H,"naat-sifa","ism-maful"], "نَعْتٌ مَرْفُوعٌ.", "«used».", "«kullanılan»."),
  tok("فِي","fi","part",[H,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("غَيْرِ","ghayr","noun",[H,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ مُضَافٌ.", "«other than».", "«başka»."),
  tok("مَا","ma-mawsula","pron",[H,"ism-mawsul","idafa-definiteness"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«what».", "«… şey»."),
  tok("وُضِعَتْ","wadaa","verb",[H,"naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«it was coined».", "«konuldu»."),
  tok("لَهُ","li","part",[H,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْعَائِدُ.", "«for».", "«için».", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("عَلَى","ala","part",[H,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in (a way)».", "«üzere»."),
  tok("وَجْهٍ","wajh","noun",[H,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«a way».", "«bir vecih»."),
  tok("يَصِحُّ","sahha","verb",[H,"jumla-sifa","doubled-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ صِفَةٌ لِوَجْهٍ. وَهٰذَا قَيْدُ الْعَلَاقَةِ: يُخْرِجُ الْغَلَطَ.",
      "«that is sound» — the describing clause: the ʿALAQA clause, which keeps out a mere mistake.", "«sahih olan» — vasıf cümlesi: ALÂKA kaydı, hatayı dışarıda bırakır."),
  tok("مَعَ","maa","noun",[H,"maful-fih","idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«together with».", "«ile birlikte»."),
  tok("قَرِينَةِ","qarina","noun",[H,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ — قَيْدُ الْقَرِينَةِ: يُخْرِجُ الْكِنَايَةَ.",
      "«a clue of» — the QARINA clause, which keeps out kinaya (where the literal may still be meant).", "«karînesiyle» — KARÎNE kaydı, kinâyeyi dışarıda bırakır (orada hakikat yine kastedilebilir)."),
  tok("عَدَمِ","adam","noun",[H,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مُضَافٌ.", "«the absence of».", "«-memesinin»."),
  tok("إِرَادَتِهِ","irada","noun",[H,"idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَائِدٌ إِلَى مَا وُضِعَتْ لَهُ.",
      "«its being meant» — the ha returns to the coined meaning: the clue says the literal is NOT intended.", "«kastedilmesi» — hâ konulan mânâya döner: karîne hakikatin kastedilMEDİĞİNİ söyler.",
      segments=[seg("إِرَادَتِ","irada","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s3 — the two clauses (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "So the ʿalaqa keeps out the mistake, and the qarina keeps out the kinaya." + R_EN,
 "tr": "Öyleyse alâka hatayı, karîne kinâyeyi dışarıda bırakır." + R_TR},
 "tokens": [
  tok("فَالْعَلَاقَةُ","alaqa","noun",[H,"mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْعَلَاقَةُ مُبْتَدَأٌ.", "«so the ʿalaqa» — the relation between the two meanings.", "«alâka» — iki mânâ arasındaki bağ.",
      segments=[seg("فَ","fa","conj"), seg("الْعَلَاقَةُ","alaqa","noun")]),
  tok("تُخْرِجُ","akhraja","verb",[H,"form-iv-verbs","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — خَبَرٌ.", "«keeps out».", "«dışarıda bırakır»."),
  tok("الْغَلَطَ","ghalat","noun",[H,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — كَمَنْ قَالَ: خُذْ هٰذَا الْفَرَسَ، وَأَشَارَ إِلَى كِتَابٍ.", "«the mistake» — a slip of the tongue with no relation at all.", "«hatayı» — hiç bağı olmayan dil sürçmesi.", punct="،"),
  tok("وَالْقَرِينَةُ","qarina","noun",[H,"mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْقَرِينَةُ مُبْتَدَأٌ.", "«and the qarina».", "«karîne ise».",
      segments=[seg("وَ","wa","conj"), seg("الْقَرِينَةُ","qarina","noun")]),
  tok("تُخْرِجُ","akhraja","verb",[H,"form-iv-verbs"], "خَبَرٌ.", "«keeps out».", "«dışarıda bırakır»."),
  tok("الْكِنَايَةَ","kinaya","noun",[H,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — فِي الْكِنَايَةِ يَجُوزُ إِرَادَةُ الْمَعْنَى الْأَصْلِيِّ.", "«the kinaya» — where the literal may be meant too.", "«kinâyeyi» — orada asıl mânâ da kastedilebilir.", punct=".")]})

# ----------- s4 — the four conventions (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "And each of the two is linguistic, or legal, or customary — particular or general." + R_EN,
 "tr": "İkisinden her biri ya lügavî, ya şer'î, ya örfî — hâs veya âm — olur." + R_TR},
 "tokens": [
  tok("وَكُلٌّ","kull","noun",[H,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكُلٌّ مُبْتَدَأٌ — التَّنْوِينُ عِوَضٌ.", "«and each» — the mubtada.", "«her biri» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("كُلٌّ","kull","noun")]),
  tok("مِنْهُمَا","min","part",[H,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْحَقِيقَةُ وَالْمَجَازُ.", "«of the two».", "«ikisinden».", segments=[seg("مِنْ","min","part"), seg("هُمَا","pron-3d","pron")]),
  tok("لُغَوِيٌّ","lughawi","noun",[H,"mubtada-khabar","ism-mansub"], "خَبَرٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى اللُّغَةِ.", "«linguistic» — the khabar; a nisba to لُغَة.", "«lügavî» — haber; لُغَة'ye nisbet."),
  tok("أَوْ","aw","conj",[H,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("شَرْعِيٌّ","shari","noun",[H,"atf-nasaq","ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ.", "«legal» — of the sharia.", "«şer'î»."),
  tok("أَوْ","aw","conj",[H,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("عُرْفِيٌّ","urfi","noun",[H,"atf-nasaq","ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى الْعُرْفِ.", "«customary».", "«örfî»."),
  tok("خَاصٌّ","khass","noun",[H,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ — عُرْفُ طَائِفَةٍ، كَالْفِعْلِ عِنْدَ النُّحَاةِ.", "«particular» — a group's custom (فِعْل among the grammarians).", "«hâs» — bir zümrenin örfü (nahivcilerde فِعْل)."),
  tok("أَوْ","aw","conj",[H,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("عَامٌّ","amm","noun",[H,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ — عُرْفُ النَّاسِ، كَالدَّابَّةِ لِذَوَاتِ الْأَرْبَعِ.", "«general» — everyone's custom (دَابَّة for a four-footed beast).", "«âm» — herkesin örfü (dört ayaklı için دَابَّة).", punct=".")]})

# ----------- s5 — the examples (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "As the lion for the beast and for the brave man; and the salat for supplication and for the worship." + R_EN,
 "tr": "Arslanın yırtıcı için ve cesur adam için; salâtın dua için ve ibadet için kullanılması gibi." + R_TR},
 "tokens": [
  tok("كَالْأَسَدِ","asad","noun",[H,"huruf-jarr"],
      "الْكَافُ لِلتَّمْثِيلِ، وَالْأَسَدِ مَجْرُورٌ — خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: وَذَٰلِكَ كَالْأَسَدِ. لَا تَشْبِيهَ هُنَا.",
      "«as the lion» — the kaf of example, not of likening: the word cited, with its two uses.", "«arslan gibi» — benzetme değil örnek kâfı: kelime, iki kullanımıyla anılıyor.",
      segments=[seg("كَ","ka","part"), seg("الْأَسَدِ","asad","noun")]),
  tok("لِلسَّبُعِ","sabu","noun",[H,"huruf-jarr"], "اللَّامُ جَارَّةٌ وَالسَّبُعِ مَجْرُورٌ — حَقِيقَةٌ لُغَوِيَّةٌ.", "«for the beast» — the linguistic haqiqa.", "«yırtıcı için» — lügavî hakikat.",
      segments=[seg("لِ","li","part"), seg("السَّبُعِ","sabu","noun")]),
  tok("وَلِلرَّجُلِ","rajul","noun",[H,"atf-nasaq","huruf-jarr"], "مَعْطُوفٌ — مَجَازٌ لُغَوِيٌّ.", "«and for the man» — the linguistic majaz.", "«ve adam için» — lügavî mecaz.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","part"), seg("الرَّجُلِ","rajul","noun")]),
  tok("الشُّجَاعِ","shujaa","noun",[H,"naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«brave».", "«cesur».", punct="،"),
  tok("وَالصَّلَاةِ","salat","noun",[H,"atf-nasaq"], "مَعْطُوفٌ عَلَى الْأَسَدِ مَجْرُورٌ.", "«and the salat».", "«ve salât».",
      segments=[seg("وَ","wa","conj"), seg("الصَّلَاةِ","salat","noun")]),
  tok("لِلدُّعَاءِ","dua","noun",[H,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — حَقِيقَةٌ لُغَوِيَّةٌ، مَجَازٌ شَرْعِيٌّ.", "«for supplication» — linguistic haqiqa, legal majaz.", "«dua için» — lügavî hakikat, şer'î mecaz.",
      segments=[seg("لِ","li","part"), seg("الدُّعَاءِ","dua","noun")]),
  tok("وَلِلْعِبَادَةِ","ibada","noun",[H,"atf-nasaq","huruf-jarr"], "مَعْطُوفٌ — حَقِيقَةٌ شَرْعِيَّةٌ.", "«and for the worship» — the legal haqiqa (the prayer).", "«ve ibadet için» — şer'î hakikat (namaz).",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","part"), seg("الْعِبَادَةِ","ibada","noun")], punct=".")]})

# ----------- s6 — mursal or istiʿara (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "The single-word majaz: if the relation is other than likeness, it is mursal; otherwise it is an istiʿara." + R_EN,
 "tr": "Müfred mecaz: alâka müşâbehetten başka ise mürseldir; yoksa istiâredir." + R_TR},
 "tokens": [
  tok("وَالْمَجَازُ","majaz","noun",[H,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْمَجَازُ مُبْتَدَأٌ.", "«the majaz» — the mubtada.", "«mecaz» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمَجَازُ","majaz","noun")]),
  tok("الْمُفْرَدُ","mufrad","noun",[H,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ — مَجَازُ الْكَلِمَةِ لَا التَّرْكِيبِ.", "«single-word» — the majaz of a word, not of a whole sentence.", "«müfred» — cümlenin değil kelimenin mecazı."),
  tok("إِنْ","in-shartiyya","part",[H,"in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("كَانَتِ","kana","verb",[H,"kana-wa-akhawatuha","in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ.", "«is» — the shart-verb; its ta takes a kasra before the article.", "«ise» — şart fiili; tâsı harf-i tarif önünde kesra alır."),
  tok("الْعَلَاقَةُ","alaqa","noun",[H,"kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the relation» — the ism of كَانَ.", "«alâka» — كَانَ'nin ismi."),
  tok("غَيْرَ","ghayr","noun",[H,"kana-wa-akhawatuha","idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ مُضَافٌ.", "«other than» — the khabar of كَانَ.", "«-den başka» — كَانَ'nin haberi."),
  tok("الْمُشَابَهَةِ","mushabaha","noun",[H,"idafa-definiteness","masdar","form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ شَابَهَ.", "«likeness» — the masdar of Form III.", "«müşâbehet» — III. bâbın masdarı."),
  tok("فَمُرْسَلٌ","mursal","noun",[H,"in-shartiyya","mubtada-khabar"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَمُرْسَلٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: فَهُوَ مُرْسَلٌ.", "«it is mursal» — the fa binds the jawab: sent loose from likeness.", "«mürseldir» — fâ cevabı bağlar: müşâbehetten salınmış.",
      segments=[seg("فَ","fa","conj"), seg("مُرْسَلٌ","mursal","noun")], punct="،"),
  tok("وَإِلَّا","illa-shartiyya","part",[H,"in-shartiyya"], "وَإِلَّا: إِنْ لَا — أَيْ: وَإِنْ لَمْ تَكُنْ غَيْرَ الْمُشَابَهَةِ.", "«otherwise» — إِنْ + لَا: if the relation IS likeness.", "«yoksa» — إِنْ + لَا: alâka müşâbehet İSE.",
      segments=[seg("وَ","wa","conj"), seg("إِلَّا","illa-shartiyya","part")]),
  tok("فَاسْتِعَارَةٌ","istiara","noun",[H,I,"in-shartiyya","mubtada-khabar","masdar","form-x-verbs"],
      "الْفَاءُ رَابِطَةٌ، وَاسْتِعَارَةٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ — مَصْدَرُ اسْتَعَارَ: طَلَبَ الْعَارِيَّةَ.",
      "«it is an istiʿara» — a BORROWING: the masdar of اسْتَعَارَ; the bihi's name lent to the mushabbah.", "«istiâredir» — ÖDÜNÇ ALMA: اسْتَعَارَ'nin masdarı; bihin adı müşebbehe ödünç verilmiş.",
      segments=[seg("فَ","fa","conj"), seg("اسْتِعَارَةٌ","istiara","noun")], punct=".")]})

# ----------- s7 — the tahqiqiyya (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "And the istiʿara may be qualified as tahqiqiyya, because its meaning is realised — by sense or by reason." + R_EN,
 "tr": "İstiâre bazen tahkîkiyye ile kayıtlanır — mânâsı hissen yahut aklen gerçekleştiği için." + R_TR},
 "tokens": [
  tok("وَالِاسْتِعَارَةُ","istiara","noun",[H,I,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالِاسْتِعَارَةُ مُبْتَدَأٌ.", "«the istiʿara» — the mubtada.", "«istiâre» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الِاسْتِعَارَةُ","istiara","noun")]),
  tok("قَدْ","qad","part",[H,"qad-harf"], "حَرْفُ تَقْلِيلٍ.", "«may».", "«bazen»."),
  tok("تُقَيَّدُ","qayyada","verb",[H,"naib-al-fail","form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — خَبَرٌ.", "«is qualified» — Form II majhul.", "«kayıtlanır» — II. bâb meçhul."),
  tok("بِالتَّحْقِيقِيَّةِ","tahqiqiyya","noun",[H,I,"huruf-jarr","ism-mansub"], "الْبَاءُ جَارَّةٌ وَالتَّحْقِيقِيَّةِ مَجْرُورٌ — نِسْبَةٌ إِلَى التَّحْقِيقِ.", "«as tahqiqiyya» — a nisba to تَحْقِيق: realised.", "«tahkîkiyye ile» — تَحْقِيق'e nisbet: gerçekleşmiş.",
      segments=[seg("بِ","bi","part"), seg("التَّحْقِيقِيَّةِ","tahqiqiyya","noun")]),
  tok("لِتَحَقُّقِ","tahaqquq","noun",[H,"huruf-jarr","lam-taleel","idafa-definiteness","masdar","form-v-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَتَحَقُّقِ مَجْرُورٌ مُضَافٌ.", "«because of the realising of».", "«gerçekleştiği için».",
      segments=[seg("لِ","li","part"), seg("تَحَقُّقِ","tahaqquq","noun")]),
  tok("مَعْنَاهَا","mana","noun",[H,"idafa-definiteness","ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهَا مُضَافٌ إِلَيْهِ — الْمَعْنَى الْمُسْتَعَارُ لَهُ.", "«its meaning» — the meaning the word is lent to.", "«mânâsının» — kelimenin ödünç verildiği mânâ.",
      segments=[seg("مَعْنَا","mana","noun"), seg("هَا","pron-3fs","pron")]),
  tok("حِسًّا","hiss","noun",[H,"tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — أَوْ حَالٌ: مَحْسُوسًا.", "«by sense» — a tamyiz (or a hal): a thing the senses reach.", "«hissen» — temyiz (yahut hâl): duyunun ulaştığı şey."),
  tok("أَوْ","aw","conj",[H,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("عَقْلًا","aql","noun",[H,"atf-nasaq","tamyiz"], "مَعْطُوفٌ مَنْصُوبٌ.", "«by reason» — a thing the mind reaches.", "«aklen» — aklın ulaştığı şey.", punct=".")]})

# ----------- s8 — Zuhayr's bayt (as printed; the second hemistich restored)
S.append({"id": "s8", "translation": {
 "en": "«— beside a lion fully armed, hurled (into battle); he has a mane, and his claws have not been clipped.»",
 "tr": "«— tepeden tırnağa silâhlı, (savaşa) atılmış bir arslanın yanında; yelesi var, pençeleri de kesilmemiş.»"},
 "majaz": mj(1, "istiara", "mushabaha", {"en": "the lion (the beast)", "tr": "arslan (yırtıcı)"}, {"en": "the brave warrior", "tr": "cesur savaşçı"}),
 "tokens": [
  tok("لَدَى","lada","noun",[H,"maful-fih","idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«beside».", "«yanında»."),
  tok("أَسَدٍ","asad","noun",[H,I,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْتِعَارَةٌ تَحْقِيقِيَّةٌ: اسْتُعِيرَ الْأَسَدُ لِلرَّجُلِ الشُّجَاعِ، وَالْقَرِينَةُ: شَاكِي السِّلَاحِ. الْمُسْتَعَارُ مِنْهُ الْأَسَدُ، الْمُسْتَعَارُ لَهُ الرَّجُلُ، الْمُسْتَعَارُ اللَّفْظُ.",
      "«a lion» — an ISTIʿARA realised by sense: the lion's name lent to a brave man, and the CLUE is that he carries weapons. The bihi is spoken, the mushabbah dropped — so no tashbih frame, a majaz frame.",
      "«bir arslan» — hissen gerçekleşen İSTİÂRE: arslanın adı cesur adama ödünç verilmiş, KARÎNE silâh taşımasıdır. Bih söylenmiş, müşebbeh düşmüş — teşbih çerçevesi değil, mecaz çerçevesi."),
  tok("شَاكِي","shaki","noun",[H,"naat-sifa","ism-maqsur-manqus","idafa-definiteness","idafa-lafziyya"],
      "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَهُوَ مُضَافٌ — مَنْقُوصٌ: شَاكٍ، أُعِيدَتْ يَاؤُهُ بِالْإِضَافَةِ. أَصْلُهُ شَائِك، قُلِبَ.",
      "«fully armed» — a manqus na't whose ya returns in the idafa (شَاكٍ → شَاكِي السِّلَاحِ); the QARINA of the istiʿara: a beast carries no arms.",
      "«silâhlı» — izâfette yâsı geri gelen mankûs sıfat (شَاكٍ → شَاكِي السِّلَاحِ); istiârenin KARÎNESİ: yırtıcı silâh taşımaz."),
  tok("السِّلَاحِ","silah","noun",[H,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — إِضَافَةٌ لَفْظِيَّةٌ.", "«weapons» — a lafzi idafa (the participle to its object).", "«silâh» — lafzî izâfet (sıfat mef'ûlüne)."),
  tok("مُقَذَّفٍ","muqadhdhaf","noun",[H,"naat-sifa","ism-maful","form-ii-verbs"], "نَعْتٌ ثَانٍ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ قَذَّفَ: مَرْمِيٌّ بِهِ فِي الْحُرُوبِ.", "«hurled» — a second na't: thrown into wars.", "«atılmış» — ikinci sıfat: savaşlara atılmış."),
  tok("لَهُ","li","part",[H,"huruf-jarr","mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — وَالْجُمْلَةُ صِفَةٌ ثَالِثَةٌ.", "«he has» — a fronted khabar; the clause a third description (restored hemistich).", "«onun var» — mukaddem haber; cümle üçüncü vasıf (geri yazılan mısra).",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("لِبَدٌ","libad","noun",[H,"mubtada-khabar","jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — جَمْعُ لِبْدَةٍ: شَعْرُ الْعُنُقِ الْمُتَلَبِّدُ.", "«a mane» — the delayed mubtada (the matted hair of the neck).", "«yele» — muahhar mübtedâ (boynun keçeleşmiş kılı)."),
  tok("أَظْفَارُهُ","zufr","noun",[H,"mubtada-khabar","idafa-definiteness","jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ ظُفْرٍ.", "«his claws» — the mubtada of a fourth clause.", "«pençeleri» — dördüncü cümlenin mübtedâsı.",
      segments=[seg("أَظْفَارُ","zufr","noun"), seg("هُ","pron-3ms","pron")]),
  tok("لَمْ","lam-jazima","part",[H,"lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-memiş»."),
  tok("تُقَلَّمِ","qallama","verb",[H,"lam-jazim","naib-al-fail","form-ii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ، حُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ. التَّرْشِيحُ: ذِكْرُ مَا يُلَائِمُ الْمُسْتَعَارَ مِنْهُ.",
      "«have not been clipped» — the khabar-clause; the rhyme gives the jazm a kasra. Mane and claws suit the LION: the istiʿara is furnished (murashshaha) with the bihi's own traits.",
      "«kesilmemiş» — haber cümlesi; kafiye cezme kesra verir. Yele ve pençe ARSLANA yakışır: istiâre bihin kendi vasıflarıyla donatılmış (müreşşaha).",
      punct=".")]})

# ----------- s9 — the aya 1:6: the istiʿara realised by reason
S.append({"id": "s9", "translation": {
 "en": "«Guide us to the straight path.» (1:6)",
 "tr": "«Bizi dosdoğru yola ilet.» (1:6)"},
 "majaz": mj(1, "istiara", "mushabaha", {"en": "the road", "tr": "yol"}, {"en": "the true religion", "tr": "hak din"}),
 "tokens": [
  tok("اهْدِنَا","hada","verb",[H,"imperative-amr","naqis-verbs","maful-bihi"],
      "فِعْلُ دُعَاءٍ عَلَى صِيغَةِ الْأَمْرِ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَنَا مَفْعُولٌ بِهِ أَوَّلُ.",
      "«guide us» — the amr of the naqis هَدَى, its ya dropped; نَا the first object.", "«bizi ilet» — nâkıs هَدَى'nın emri, yâsı düşmüş; نَا ilk mef'ûl.",
      segments=[seg("اهْدِ","hada","verb"), seg("نَا","pron-1p","pron")]),
  tok("الصِّرَاطَ","sirat","noun",[H,I,"maful-bihi","mafulayn"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — اسْتِعَارَةٌ تَحْقِيقِيَّةٌ: ذُكِرَ الصِّرَاطُ وَأُرِيدَ الدِّينُ الْحَقُّ، وَمَعْنَاهُ مُتَحَقِّقٌ عَقْلًا. الْقَرِينَةُ: طَلَبُ الْهِدَايَةِ إِلَيْهِ.",
      "«the path» — the second object; an ISTIʿARA realised by reason: the road is spoken and the true religion meant — a thing the mind grasps. The clue: guidance is asked to it.",
      "«yola» — ikinci mef'ûl; aklen gerçekleşen İSTİÂRE: yol söylenmiş, hak din kastedilmiş — aklın kavradığı bir şey. Karîne: ona hidâyet istenmesi."),
  tok("الْمُسْتَقِيمَ","mustaqim","noun",[H,"naat-sifa","ism-fail","form-x-verbs"], "نَعْتٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنِ اسْتَقَامَ.", "«straight» — na't; the ism fa'il of Form X.", "«dosdoğru» — sıfat; X. bâbın ism-i fâili.", punct=".")]})

# ----------- s10 — the four arkan of the istiʿara (RESTORED)
S.append({"id": "s10", "translation": {
 "en": "The arkan of the istiʿara are four: that from which it is borrowed, that for which it is borrowed, the borrowed word, and the borrower." + R_EN,
 "tr": "İstiârenin rükünleri dörttür: müsteârun minh, müsteârun leh, müsteâr ve müstaîr." + R_TR},
 "tokens": [
  tok("وَأَرْكَانُ","rukn","noun",[I,"mubtada-khabar","idafa-definiteness","jam-taksir"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَأَرْكَانُ مُبْتَدَأٌ مُضَافٌ — جَمْعُ رُكْنٍ.", "«the arkan of» — the mubtada.", "«rükünleri» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("أَرْكَانُ","rukn","noun")]),
  tok("الِاسْتِعَارَةِ","istiara","noun",[I,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the istiʿara».", "«istiârenin»."),
  tok("أَرْبَعَةٌ","arbaa","noun",[I,"mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«four» — the khabar.", "«dörttür» — haber.", punct=":"),
  tok("مُسْتَعَارٌ","mustaar","noun",[I,"badal","ism-maful","form-x-verbs"],
      "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ، أَوْ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ — اسْمُ مَفْعُولٍ مِنِ اسْتَعَارَ.",
      "«borrowed» — the detailing badal; the ism maf'ul of Form X (اسْتَعَارَ: hollow, the alif of اسْتَعَارَ becomes مُسْتَعَار).", "«müsteâr» — tafsil bedeli; X. bâbın ism-i mef'ûlü."),
  tok("مِنْهُ","min","part",[I,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُسْتَعَارُ مِنْهُ: الْمُشَبَّهُ بِهِ.", "«from it» — the source of the loan: the MUSHABBAH BIHI (the lion).", "«kendisinden» — ödüncün kaynağı: MÜŞEBBEHÜN BİH (arslan).",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("وَمُسْتَعَارٌ","mustaar","noun",[I,"atf-nasaq","ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and borrowed».", "«ve müsteâr».", segments=[seg("وَ","wa","conj"), seg("مُسْتَعَارٌ","mustaar","noun")]),
  tok("لَهُ","li","part",[I,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُسْتَعَارُ لَهُ: الْمُشَبَّهُ.", "«for it» — the MUSHABBAH (the brave man).", "«kendisi için» — MÜŞEBBEH (cesur adam).",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("وَمُسْتَعَارٌ","mustaar","noun",[I,"atf-nasaq","ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ — اللَّفْظُ نَفْسُهُ.", "«and the borrowed (word)» — the word itself (أَسَد).", "«ve müsteâr» — kelimenin kendisi (أَسَد).",
      segments=[seg("وَ","wa","conj"), seg("مُسْتَعَارٌ","mustaar","noun")], punct="،"),
  tok("وَمُسْتَعِيرٌ","mustair","noun",[I,"atf-nasaq","ism-fail","form-x-verbs"], "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ: الْمُتَكَلِّمُ.", "«and the borrower» — the ism fa'il: the speaker who makes the loan.", "«ve müstaîr» — ism-i fâil: ödüncü yapan konuşan.",
      segments=[seg("وَ","wa","conj"), seg("مُسْتَعِيرٌ","mustair","noun")], punct=".")]})

# ----------- s11 — the mursal: hand and water-camel (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "The mursal is like «hand» for a favour and for power, and «rawiya» for the water-skin." + R_EN,
 "tr": "Mürsel, nimet ve kudret için «el», su tulumu için «râviye» demek gibidir." + R_TR},
 "majaz": [mj(1, "mursal", "sababiyya", {"en": "the hand", "tr": "el"}, {"en": "a favour, power — what the hand does", "tr": "nimet, kudret — elin yaptığı"})],
 "tokens": [
  tok("فَالْمُرْسَلُ","mursal","noun",[M,"mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمُرْسَلُ مُبْتَدَأٌ.", "«the mursal» — the mubtada.", "«mürsel» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْمُرْسَلُ","mursal","noun")]),
  tok("كَالْيَدِ","yad","noun",[M,"huruf-jarr"],
      "الْكَافُ لِلتَّمْثِيلِ، وَالْيَدِ مَجْرُورٌ — خَبَرٌ. مَجَازٌ مُرْسَلٌ: الْيَدُ لِلنِّعْمَةِ لِأَنَّهَا سَبَبُهَا، وَلِلْقُدْرَةِ.",
      "«like the hand» — the example-kaf (no likening); the hand is a MURSAL majaz for a favour, because the hand is its CAUSE — the ʿalaqa of sababiyya.",
      "«el gibi» — örnek kâfı (benzetme yok); el, nimet için MÜRSEL mecazdır, çünkü el onun SEBEBİDİR — sebebiyet alâkası.",
      segments=[seg("كَ","ka","part"), seg("الْيَدِ","yad","noun")]),
  tok("فِي","fi","part",[M,"huruf-jarr"], "حَرْفُ جَرٍّ — فِي: لِلْمَعْنَى الْمُسْتَعْمَلِ فِيهِ.", "«for (in the sense of)».", "«… için (mânâsında)»."),
  tok("النِّعْمَةِ","nima","noun",[M,"huruf-jarr"], "اسْمٌ مَجْرُورٌ — الْمَعْنَى الْمَجَازِيُّ الْأَوَّلُ.", "«a favour» — the first intended meaning.", "«nimet» — ilk kastedilen mânâ."),
  tok("وَالْقُدْرَةِ","qudra","noun",[M,"atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ — الثَّانِي.", "«and power» — the second.", "«ve kudret» — ikincisi.",
      segments=[seg("وَ","wa","conj"), seg("الْقُدْرَةِ","qudra","noun")], punct="،"),
  tok("وَالرَّاوِيَةِ","rawiya","noun",[M,"atf-nasaq"],
      "مَعْطُوفٌ عَلَى الْيَدِ مَجْرُورٌ — الرَّاوِيَةُ: الْبَعِيرُ الَّذِي يَحْمِلُ الْمَاءَ، سُمِّيَتْ بِهِ الْمَزَادَةُ لِلْمُجَاوَرَةِ.",
      "«and the rawiya» — the water-carrying camel, whose name passed to the water-skin it carries: the ʿalaqa of adjacency.", "«ve râviye» — su taşıyan deve; adı taşıdığı tuluma geçti: mücâveret alâkası.",
      segments=[seg("وَ","wa","conj"), seg("الرَّاوِيَةِ","rawiya","noun")]),
  tok("فِي","fi","part",[M,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«için»."),
  tok("الْمَزَادَةِ","mazada","noun",[M,"huruf-jarr"], "اسْمٌ مَجْرُورٌ — الْمَزَادَةُ: قِرْبَةٌ كَبِيرَةٌ.", "«the water-skin».", "«su tulumu».", punct=".")]})

# ----------- s12 — part for whole, whole for part (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "And of it: naming a thing by the name of its part, like «eye» for the scout; and by the name of its whole, like «fingers» for the fingertips." + R_EN,
 "tr": "Bir şeyi parçasının adıyla adlandırmak da bundandır: gözcü için «göz» gibi; bütününün adıyla: parmak uçları için «parmaklar» gibi." + R_TR},
 "majaz": [mj(5, "mursal", "juziyya", {"en": "the eye", "tr": "göz"}, {"en": "the scout — a whole named by its part", "tr": "gözcü — parçasıyla adlanan bütün"}),
           mj(10, "mursal", "kulliyya", {"en": "the fingers", "tr": "parmaklar"}, {"en": "the fingertips — a part named by its whole", "tr": "parmak uçları — bütünüyle adlanan parça"})],
 "tokens": [
  tok("وَمِنْهُ","min","part",[M,"huruf-jarr","mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — الْهَاءُ لِلْمُرْسَلِ.", "«and of it» — a fronted khabar: among the mursal.", "«ve ondandır» — mukaddem haber: mürselden.",
      segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("تَسْمِيَةُ","tasmiya","noun",[M,"mubtada-khabar","idafa-definiteness","masdar","form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مُضَافٌ — مَصْدَرُ سَمَّى.", "«naming».", "«adlandırmak»."),
  tok("الشَّيْءِ","shay","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyi»."),
  tok("بِاسْمِ","ism","noun",[M,"huruf-jarr","idafa-definiteness"], "الْبَاءُ جَارَّةٌ وَاسْمِ مَجْرُورٌ مُضَافٌ.", "«by the name of».", "«adıyla».", segments=[seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("جُزْئِهِ","juz","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَلَاقَةُ الْجُزْئِيَّةِ.", "«its part» — the ʿalaqa of juz'iyya.", "«parçasının» — cüz'iyyet alâkası.",
      segments=[seg("جُزْئِ","juz","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَالْعَيْنِ","ayn-eye","noun",[M,"huruf-jarr"],
      "الْكَافُ لِلتَّمْثِيلِ، وَالْعَيْنِ مَجْرُورٌ — الْعَيْنُ لِلرَّبِيئَةِ: الْجُزْءُ لِلْكُلِّ، لِأَنَّ الْعَيْنَ آلَتُهُ فِي عَمَلِهِ.",
      "«like the eye» — the eye for the SCOUT: the part for the whole, because the eye is what he scouts with.", "«göz gibi» — GÖZCÜ için göz: bütün yerine parça, çünkü gözcü işini gözüyle görür.",
      segments=[seg("كَ","ka","part"), seg("الْعَيْنِ","ayn-eye","noun")]),
  tok("فِي","fi","part",[M,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«için»."),
  tok("الرَّبِيئَةِ","rabia","noun",[M,"huruf-jarr"], "اسْمٌ مَجْرُورٌ — الرَّبِيئَةُ: الطَّلِيعَةُ.", "«the scout» — the look-out.", "«gözcü».", punct="،"),
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ عَلَى بِاسْمِ جُزْئِهِ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("كُلِّهِ","kull","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَلَاقَةُ الْكُلِّيَّةِ.", "«its whole» — the ʿalaqa of kulliyya.", "«bütününün» — külliyyet alâkası.",
      segments=[seg("كُلِّ","kull","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَالْأَصَابِعِ","isba","noun",[M,"huruf-jarr","jam-taksir","mamnu-min-sarf"],
      "الْكَافُ لِلتَّمْثِيلِ، وَالْأَصَابِعِ مَجْرُورٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، وَالْأَلِفُ وَاللَّامُ تُعِيدَانِ الْكَسْرَةَ. الْأَصَابِعُ لِلْأَنَامِلِ: الْكُلُّ لِلْجُزْءِ — جَعَلُوا أَصَابِعَهُمْ فِي آذَانِهِمْ.",
      "«like the fingers» — for the FINGERTIPS: the whole for the part (they put their FINGERS in their ears, 71:7 — only the tips fit).",
      "«parmaklar gibi» — PARMAK UÇLARI için: parça yerine bütün (PARMAKLARINI kulaklarına tıkadılar, 71:7 — ancak uçları sığar).",
      segments=[seg("كَ","ka","part"), seg("الْأَصَابِعِ","isba","noun")]),
  tok("فِي","fi","part",[M,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«için»."),
  tok("الْأَنَامِلِ","anmula","noun",[M,"huruf-jarr","jam-taksir","mamnu-min-sarf"], "اسْمٌ مَجْرُورٌ — جَمْعُ أُنْمُلَةٍ.", "«the fingertips».", "«parmak uçları».", punct=".")]})

# ----------- s13 — the cause: رَعَيْنَا الْغَيْثَ (RESTORED frame, printed example)
S.append({"id": "s13", "translation": {
 "en": "And by the name of its cause, as in their saying: «We grazed the rain.»" + R_EN,
 "tr": "Sebebinin adıyla: «Yağmuru otlattık» sözleri gibi." + R_TR},
 "majaz": mj(4, "mursal", "sababiyya", {"en": "the rain", "tr": "yağmur"}, {"en": "the pasture the rain grew", "tr": "yağmurun bitirdiği ot"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("سَبَبِهِ","sabab","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَلَاقَةُ السَّبَبِيَّةِ.", "«its cause» — the ʿalaqa of sababiyya.", "«sebebinin» — sebebiyet alâkası.",
      segments=[seg("سَبَبِ","sabab","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِمْ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جِدَارٌ لِلْمُحَرِّكِ: مَا بَعْدَهُ مِثَالٌ.", "«as in their saying» — the wall: a quotation follows.", "«sözleri gibi» — duvar: alıntı geliyor.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِمْ","pron-3mp","pron")], punct=":"),
  tok("رَعَيْنَا","raa-graze","verb",[M,"naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ — نَاقِصٌ يَائِيٌّ: رَعَى.", "«we grazed» — رَعَى with نَا its fa'il; the verb of PASTURE is the clue.", "«otlattık» — رَعَى, نَا fâili; OTLATMA fiili karînedir.",
      segments=[seg("رَعَيْ","raa-graze","verb"), seg("نَا","pron-1p","pron")]),
  tok("الْغَيْثَ","ghayth","noun",[M,"maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَجَازٌ مُرْسَلٌ: الْغَيْثُ لِلنَّبَاتِ، لِأَنَّهُ سَبَبُهُ؛ وَالْقَرِينَةُ: الرَّعْيُ لَا يَقَعُ عَلَى الْمَطَرِ.",
      "«the rain» — the object: a MURSAL majaz, the rain named for the pasture it CAUSED; the clue: one cannot graze rain.", "«yağmuru» — mef'ûl: MÜRSEL mecaz, yağmur SEBEP olduğu ot yerine; karîne: yağmur otlatılmaz.",
      punct=".")]})

# ----------- s14 — the effect: أَمْطَرَتِ السَّمَاءُ نَبَاتًا
S.append({"id": "s14", "translation": {
 "en": "And by the name of its effect, as in their saying: «The sky rained plants.»" + R_EN,
 "tr": "Müsebbebinin adıyla: «Gök bitki yağdırdı» sözleri gibi." + R_TR},
 "majaz": mj(5, "mursal", "musabbabiyya", {"en": "plants", "tr": "bitki"}, {"en": "the rain that grows them", "tr": "onları bitiren yağmur"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("مُسَبَّبِهِ","musabbab","noun",[M,"idafa-definiteness","ism-maful","form-ii-verbs"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ مَفْعُولٍ مِنْ سَبَّبَ: الْمُسَبَّبُ عَنْهُ.", "«its effect» — the ʿalaqa of musabbabiyya.", "«müsebbebinin» — müsebbebiyet alâkası.",
      segments=[seg("مُسَبَّبِ","musabbab","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِمْ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ.", "«as in their saying».", "«sözleri gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِمْ","pron-3mp","pron")], punct=":"),
  tok("أَمْطَرَتِ","amtara","verb",[M,"form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«rained» — Form IV; the ta takes a kasra before the article.", "«yağdırdı» — IV. bâb; tâ harf-i tarif önünde kesra alır."),
  tok("السَّمَاءُ","sama","noun",[M,"fail","ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ.", "«the sky» — the fa'il.", "«gök» — fâil."),
  tok("نَبَاتًا","nabat","noun",[M,"maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَجَازٌ مُرْسَلٌ: النَّبَاتُ لِلْمَطَرِ، لِأَنَّهُ مُسَبَّبٌ عَنْهُ؛ وَالْقَرِينَةُ: السَّمَاءُ لَا تُمْطِرُ نَبَاتًا.",
      "«plants» — the object: the EFFECT named for its cause (the rain); the clue: the sky does not rain plants.", "«bitki» — mef'ûl: sebebi (yağmur) yerine MÜSEBBEB; karîne: gök bitki yağdırmaz.",
      punct=".")]})

# ----------- s15 — what it was: وَآتُوا الْيَتَامَى أَمْوَالَهُمْ (4:2)
S.append({"id": "s15", "translation": {
 "en": "And by the name of what it was, as in His saying: «And give the orphans their property.» (4:2)" + R_EN,
 "tr": "Önceki hâlinin adıyla: «Yetimlere mallarını verin» (4:2) kavl-i şerifi gibi." + R_TR},
 "majaz": mj(7, "mursal", "ma-kana", {"en": "the orphans", "tr": "yetimler"}, {"en": "those who WERE orphans, now grown", "tr": "yetim OLMUŞ, artık yetişkin olanlar"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("مَا","ma-mawsula","pron",[M,"ism-mawsul","idafa-definiteness"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«what».", "«… şeyin»."),
  tok("كَانَ","kana","verb",[M,"kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — صِلَةٌ.", "«it was» — the sila: the thing's PAST state.", "«idi» — sıla: şeyin GEÇMİŞ hâli."),
  tok("عَلَيْهِ","ala","part",[M,"huruf-jarr","kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ خَبَرُ كَانَ — عَلَاقَةُ مَا كَانَ.", "«upon» — the ʿalaqa of ma-kana.", "«üzere» — mâ-kâne alâkası.",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ.", "«as in His saying».", "«kavli gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")]),
  tok("تَعَالَى","taala","verb",[M,"naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Exalted is He» — a parenthesis.", "«Teâlâ» — ara cümle.", punct=":"),
  tok("وَآتُوا","aataa","verb",[M,"imperative-amr","form-iv-verbs","mafulayn"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — آتَى يَنْصِبُ مَفْعُولَيْنِ. (يَكْتُبُهُ الْمَصْدَرُ وَاَتُوا.)",
      "«and give» — the amr of Form IV آتَى, two objects (the source writes وَاَتُوا).", "«verin» — IV. bâb آتَى'nın emri, iki mef'ûl (kaynak وَاَتُوا yazar).",
      segments=[seg("وَ","wa","conj"), seg("آتُوا","aataa","verb")]),
  tok("الْيَتَامَى","yatim","noun",[M,"maful-bihi","mafulayn","jam-taksir","ism-maqsur-manqus"],
      "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — جَمْعُ يَتِيمٍ. مَجَازٌ مُرْسَلٌ: سُمُّوا يَتَامَى بِاعْتِبَارِ مَا كَانُوا، وَقَدْ بَلَغُوا؛ الْقَرِينَةُ: لَا يُعْطَى الْمَالُ يَتِيمًا.",
      "«the orphans» — the first object: a MURSAL majaz by what they WERE — now of age; the clue: property is not handed to a minor.", "«yetimlere» — ilk mef'ûl: NE İDİLERSE onunla MÜRSEL mecaz — artık bâliğ; karîne: mal küçüğe teslim edilmez."),
  tok("أَمْوَالَهُمْ","mal","noun",[M,"maful-bihi","idafa-definiteness","jam-taksir"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their property» — the second object.", "«mallarını» — ikinci mef'ûl.",
      segments=[seg("أَمْوَالَ","mal","noun"), seg("هُمْ","pron-3mp","pron")], punct=".")]})

# ----------- s16 — what it will become: إِنِّي أَرَانِي أَعْصِرُ خَمْرًا (12:36)
S.append({"id": "s16", "translation": {
 "en": "And by the name of what it will become, as in His saying: «I see myself pressing wine.» (12:36)" + R_EN,
 "tr": "Dönüşeceği şeyin adıyla: «Ben kendimi şarap sıkarken görüyorum» (12:36) kavl-i şerifi gibi." + R_TR},
 "majaz": mj(9, "mursal", "ma-yaul", {"en": "wine", "tr": "şarap"}, {"en": "grapes that will become wine", "tr": "şarap OLACAK üzüm"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("مَا","ma-mawsula","pron",[M,"ism-mawsul","idafa-definiteness"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«what».", "«… şeyin»."),
  tok("يَؤُولُ","ala-return","verb",[M,"hollow-verbs","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ مَهْمُوزُ الْفَاءِ: آلَ يَؤُولُ: رَجَعَ وَصَارَ.", "«it will come» — آلَ يَؤُولُ: to end up as.", "«dönüşecek» — آلَ يَؤُولُ: sonunda olmak."),
  tok("إِلَيْهِ","ila","part",[M,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — عَلَاقَةُ مَا يَؤُولُ إِلَيْهِ.", "«to» — the ʿalaqa of ma-ya'ul.", "«-e» — mâ-yeûl alâkası.",
      segments=[seg("إِلَيْ","ila","part"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ.", "«as in His saying».", "«kavli gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")]),
  tok("تَعَالَى","taala","verb",[M,"naqis-verbs"], "جُمْلَةٌ مُعْتَرِضَةٌ.", "«Exalted is He».", "«Teâlâ».", punct=":"),
  tok("إِنِّي","inna","part",[M,"inna-wa-akhawatuha","ya-al-mutakallim"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا — إِنَّ + نِي، حُذِفَتْ إِحْدَى النُّونَيْنِ.", "«indeed I» — إِنَّ with the speaker's ya as its ism.", "«şüphesiz ben» — mütekellim yâsı ismi olan إِنَّ.",
      segments=[seg("إِنِّ","inna","part"), seg("ي","pron-1s","pron")]),
  tok("أَرَانِي","raa","verb",[M,"naqis-verbs","mafulayn","ya-al-mutakallim"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ أَنَا، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ — الرُّؤْيَا الْحُلْمِيَّةُ. وَالْجُمْلَةُ خَبَرُ إِنَّ.",
      "«I see myself» — أَرَى (a dream-vision) with the wiqaya nun and the speaker's ya as its first object; the clause is the khabar of إِنَّ.", "«kendimi görüyorum» — vikaye nûnu ve mef'ûl olan mütekellim yâsıyla أَرَى (rüya); cümle إِنَّ'nin haberi.",
      segments=[seg("أَرَا","raa","verb"), seg("نِي","pron-1s","pron")]),
  tok("أَعْصِرُ","asara","verb",[M,"hal","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ أَوْ حَالٌ.", "«pressing» — the second object (or hal) of the vision-verb; the verb of PRESSING is the clue.", "«sıkarken» — rüya fiilinin ikinci mef'ûlü (yahut hâl); SIKMA fiili karînedir."),
  tok("خَمْرًا","khamr","noun",[M,"maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَجَازٌ مُرْسَلٌ: الْخَمْرُ لِلْعِنَبِ بِاعْتِبَارِ مَا يَؤُولُ إِلَيْهِ؛ الْقَرِينَةُ: لَا يُعْصَرُ الْخَمْرُ.",
      "«wine» — the object: the grapes named by what they WILL BECOME; the clue: wine is not pressed, grapes are.", "«şarap» — mef'ûl: üzüm, OLACAĞI şeyle adlanmış; karîne: şarap sıkılmaz, üzüm sıkılır.",
      punct=".")]})

# ----------- s17 — the place: فَلْيَدْعُ نَادِيَهُ (96:17)
S.append({"id": "s17", "translation": {
 "en": "And by the name of its place, as in His saying: «Then let him call his assembly.» (96:17)" + R_EN,
 "tr": "Mahallinin adıyla: «Haydi meclisini çağırsın» (96:17) kavl-i şerifi gibi." + R_TR},
 "majaz": mj(5, "mursal", "mahalliyya", {"en": "the assembly-place", "tr": "meclis yeri"}, {"en": "the people of the assembly", "tr": "meclis ehli"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("مَحَلِّهِ","mahall","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَلَاقَةُ الْمَحَلِّيَّةِ.", "«its place» — the ʿalaqa of mahalliyya.", "«mahallinin» — mahalliyet alâkası.",
      segments=[seg("مَحَلِّ","mahall","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ.", "«as in His saying».", "«kavli gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")]),
  tok("تَعَالَى","taala","verb",[M,"naqis-verbs"], "جُمْلَةٌ مُعْتَرِضَةٌ.", "«Exalted is He».", "«Teâlâ».", punct=":"),
  tok("فَلْيَدْعُ","daa","verb",[M,"lam-amr","naqis-verbs"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لَامُ الْأَمْرِ سُكِّنَتْ بَعْدَ الْفَاءِ، وَيَدْعُ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ الْوَاوِ (يَدْعُو → يَدْعُ)، وَالْفَاعِلُ مُسْتَتِرٌ.",
      "«then let him call» — the lam of command (quiet after the fa) on the naqis يَدْعُو: jazm drops the waw.", "«haydi çağırsın» — nâkıs يَدْعُو üstünde emir lâmı (fâdan sonra sâkin): cezm vâvı düşürür.",
      segments=[seg("فَ","fa","conj"), seg("لْ","lam-amr","part"), seg("يَدْعُ","daa","verb")]),
  tok("نَادِيَهُ","nadi","noun",[M,"maful-bihi","idafa-definiteness","ism-maqsur-manqus"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ (الْمَنْقُوصُ يُظْهِرُ الْفَتْحَةَ)، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَجَازٌ مُرْسَلٌ: النَّادِي لِأَهْلِهِ، عَلَاقَتُهُ الْمَحَلِّيَّةُ؛ الْقَرِينَةُ: لَا يُدْعَى الْمَكَانُ.",
      "«his assembly» — a manqus object showing its fatha on the ya; a MURSAL majaz: the PLACE named for its people; the clue: a place is not called.", "«meclisini» — fethasını yâda gösteren mankûs mef'ûl; MÜRSEL mecaz: MAHAL ehli yerine; karîne: mekân çağrılmaz.",
      segments=[seg("نَادِيَ","nadi","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s18 — what dwells in it: فَفِي رَحْمَةِ اللهِ هُمْ فِيهَا خَالِدُونَ (3:107)
S.append({"id": "s18", "translation": {
 "en": "And by the name of what dwells in it, as in His saying: «then in the mercy of God — in it they abide.» (3:107)" + R_EN,
 "tr": "Kendisinde bulunanın adıyla: «Allah'ın rahmeti içindedirler; orada ebedî kalırlar» (3:107) kavl-i şerifi gibi." + R_TR},
 "majaz": mj(5, "mursal", "halliyya", {"en": "mercy", "tr": "rahmet"}, {"en": "Paradise — the place mercy dwells in", "tr": "cennet — rahmetin bulunduğu yer"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("حَالِّهِ","hall","noun",[M,"idafa-definiteness","ism-fail","doubled-verbs"],
      "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — حَالٌّ: اسْمُ فَاعِلٍ مِنْ حَلَّ (نَزَلَ)، مُضَاعَفٌ: مَا يَحُلُّ فِي الشَّيْءِ. عَلَاقَةُ الْحَالِّيَّةِ.",
      "«what dwells in it» — حَالّ (with a shadda: the geminate ism fa'il of حَلَّ, to dwell), not حَال (state): the ʿalaqa of halliyya.", "«kendisinde bulunanın» — حَالّ (şeddeli: حَلَّ'nin muzâaf ism-i fâili, bulunmak), حَال (hâl) değil: hâlliyet alâkası.",
      segments=[seg("حَالِّ","hall","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ.", "«as in His saying».", "«kavli gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")]),
  tok("تَعَالَى","taala","verb",[M,"naqis-verbs"], "جُمْلَةٌ مُعْتَرِضَةٌ.", "«Exalted is He».", "«Teâlâ».", punct=":"),
  tok("فَفِي","fi","part",[M,"huruf-jarr","mubtada-khabar"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا (فِي الْآيَةِ)، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«then in» — the fa of أَمَّا's answer; a fronted khabar.", "«… içindedirler» — أَمَّا cevabının fâsı; mukaddem haber.",
      segments=[seg("فَ","fa","conj"), seg("فِي","fi","part")]),
  tok("رَحْمَةِ","rahma","noun",[M,"huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — مَجَازٌ مُرْسَلٌ: الرَّحْمَةُ لِلْجَنَّةِ، لِأَنَّ الرَّحْمَةَ حَالَّةٌ فِيهَا؛ الْقَرِينَةُ: فِيهَا خَالِدُونَ — الْخُلُودُ فِي مَكَانٍ.",
      "«the mercy of» — a MURSAL majaz: mercy for PARADISE, the place mercy dwells in; the clue: one abides IN a place.", "«rahmeti» — MÜRSEL mecaz: rahmet, içinde bulunduğu CENNET yerine; karîne: bir mekânDA ebedî kalınır."),
  tok("اللهِ","allah","propn",[M,"idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God».", "«Allah'ın»."),
  tok("هُمْ","hum","pron",[M,"mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«they» — the delayed mubtada.", "«onlar» — muahhar mübtedâ."),
  tok("فِيهَا","fi","part",[M,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِخَالِدُونَ — وَالْهَاءُ لِلرَّحْمَةِ، أَيِ: الْجَنَّةِ.", "«in it» — the pronoun points to the «mercy» that is a place.", "«orada» — zamir, mekân olan «rahmet»e döner.",
      segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("خَالِدُونَ","khalid","noun",[M,"mubtada-khabar","ism-fail","jam-mudhakkar-salim"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«abiding» — the khabar, a sound plural.", "«ebedî kalıcılar» — haber, sâlim çoğul.", punct=".")]})

# ----------- s19 — the instrument: وَاجْعَلْ لِي لِسَانَ صِدْقٍ (26:84)
S.append({"id": "s19", "translation": {
 "en": "And by the name of its instrument, as in His saying: «And grant me a tongue of truth among the later ones.» (26:84)" + R_EN,
 "tr": "Âletinin adıyla: «Sonrakiler içinde bana bir doğruluk dili ver» (26:84) kavl-i şerifi gibi." + R_TR},
 "majaz": mj(6, "mursal", "aliyya", {"en": "a tongue", "tr": "dil"}, {"en": "a good mention — the tongue is its instrument", "tr": "güzel bir anılış — dil onun aletidir"}),
 "tokens": [
  tok("وَبِاسْمِ","ism","noun",[M,"atf-nasaq","huruf-jarr","idafa-definiteness"], "مَعْطُوفٌ.", "«and by the name of».", "«ve … adıyla».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("اسْمِ","ism","noun")]),
  tok("آلَتِهِ","ala-tool","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَلَاقَةُ الْآلِيَّةِ.", "«its instrument» — the ʿalaqa of aliyya.", "«âletinin» — âliyet alâkası.",
      segments=[seg("آلَتِ","ala-tool","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَقَوْلِهِ","qawl","noun",[M,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ.", "«as in His saying».", "«kavli gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")]),
  tok("تَعَالَى","taala","verb",[M,"naqis-verbs"], "جُمْلَةٌ مُعْتَرِضَةٌ.", "«Exalted is He».", "«Teâlâ».", punct=":"),
  tok("وَاجْعَلْ","jaala","verb",[M,"imperative-amr","mafulayn"], "الْوَاوُ عَاطِفَةٌ، وَاجْعَلْ فِعْلُ دُعَاءٍ عَلَى صِيغَةِ الْأَمْرِ، وَالْفَاعِلُ أَنْتَ.", "«and grant» — the amr of جَعَلَ (a prayer).", "«ve ver» — جَعَلَ'nin emri (dua).",
      segments=[seg("وَ","wa","conj"), seg("اجْعَلْ","jaala","verb")]),
  tok("لِي","li","part",[M,"huruf-jarr","ya-al-mutakallim"], "جَارٌّ وَمَجْرُورٌ — مَفْعُولٌ ثَانٍ فِي الْمَعْنَى.", "«for me».", "«bana».",
      segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("لِسَانَ","lisan","noun",[M,"maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ — مَجَازٌ مُرْسَلٌ: اللِّسَانُ لِلذِّكْرِ الْحَسَنِ، لِأَنَّهُ آلَتُهُ؛ الْقَرِينَةُ: جَعْلُ اللِّسَانِ فِي الْآخِرِينَ.",
      "«a tongue of» — a MURSAL majaz: the INSTRUMENT (the tongue) for what it makes (a good mention); the clue: a tongue is not «put among» later people.", "«dili» — MÜRSEL mecaz: yaptığı şey (güzel anılış) yerine ÂLET (dil); karîne: dil sonrakilerin «içine konmaz»."),
  tok("صِدْقٍ","sidq","noun",[M,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«truth».", "«doğruluk»."),
  tok("فِي","fi","part",[M,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«among».", "«içinde»."),
  tok("الْآخِرِينَ","akhir","noun",[M,"huruf-jarr","jam-mudhakkar-salim"], "اسْمٌ مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ: الْأُمَمُ الْآتِيَةُ.", "«the later ones» — the nations to come.", "«sonrakiler» — gelecek ümmetler.", punct=".")]})

# ----------- s20 — the istiʿara and the lie (RESTORED)
S.append({"id": "s20", "translation": {
 "en": "And the istiʿara differs from the lie by being built on interpretation, and by the setting-up of a clue that the opposite of the surface is meant." + R_EN,
 "tr": "İstiâre yalandan, te'vil üzere kurulmasıyla ve zâhirin hilâfının kastedildiğine karîne dikilmesiyle ayrılır." + R_TR},
 "tokens": [
  tok("وَالِاسْتِعَارَةُ","istiara","noun",[I,"mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالِاسْتِعَارَةُ مُبْتَدَأٌ.", "«the istiʿara» — the mubtada.", "«istiâre» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الِاسْتِعَارَةُ","istiara","noun")]),
  tok("تُفَارِقُ","faraqa","verb",[I,"form-iii-verbs","mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — خَبَرٌ.", "«differs from» — Form III.", "«ayrılır» — III. bâb."),
  tok("الْكَذِبَ","kadhib","noun",[I,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the lie» — for the liar too says what is not.", "«yalandan» — yalancı da olmayanı söyler."),
  tok("بِالْبِنَاءِ","bina","noun",[I,"huruf-jarr","masdar"], "الْبَاءُ جَارَّةٌ وَالْبِنَاءِ مَجْرُورٌ — مَصْدَرُ بَنَى.", "«by being built».", "«kurulmasıyla».",
      segments=[seg("بِ","bi","part"), seg("الْبِنَاءِ","bina","noun")]),
  tok("عَلَى","ala","part",[I,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  tok("التَّأْوِيلِ","tawil","noun",[I,"huruf-jarr","masdar","form-ii-verbs"],
      "اسْمٌ مَجْرُورٌ — التَّأْوِيلُ: ادِّعَاءُ دُخُولِ الْمُشَبَّهِ فِي جِنْسِ الْمُشَبَّهِ بِهِ.",
      "«interpretation» — the CLAIM that the mushabbah belongs to the bihi's kind (the brave man IS a lion): the liar claims nothing.", "«te'vil» — müşebbehin bihin cinsine girdiği İDDİASI (cesur adam arslanDIR): yalancı hiçbir şey iddia etmez."),
  tok("وَنَصْبِ","nasb-setting","noun",[I,"atf-nasaq","idafa-definiteness","masdar"], "مَعْطُوفٌ عَلَى الْبِنَاءِ مَجْرُورٌ مُضَافٌ — نَصْبُ الْقَرِينَةِ: إِقَامَتُهَا.", "«and by the setting-up of» — نَصْب here is «to set up», not the case.", "«ve dikilmesiyle» — نَصْب burada «dikmek», i'râb değil.",
      segments=[seg("وَ","wa","conj"), seg("نَصْبِ","nasb-setting","noun")]),
  tok("الْقَرِينَةِ","qarina","noun",[I,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the clue».", "«karînenin»."),
  tok("عَلَى","ala","part",[I,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«that».", "«-e»."),
  tok("إِرَادَةِ","irada","noun",[I,"huruf-jarr","idafa-definiteness"], "اسْمٌ مَجْرُورٌ مُضَافٌ.", "«the intending of».", "«kastedildiğine»."),
  tok("خِلَافِ","khilaf","noun",[I,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مُضَافٌ.", "«the opposite of».", "«hilâfının»."),
  tok("الظَّاهِرِ","zahir","noun",[I,"idafa-definiteness","ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الظَّاهِرُ: الْمَعْنَى الْحَقِيقِيُّ. وَالْكَاذِبُ يُرِيدُ ظَاهِرَ كَلَامِهِ.", "«the surface» — the literal sense; the liar wants his words taken literally.", "«zâhirin» — hakikî mânâ; yalancı sözünün zâhirini ister.", punct=".")]})

# ----------- s21 — the clue: one thing (RESTORED frame, printed example)
S.append({"id": "s21", "translation": {
 "en": "Its clue is either one thing, as in your saying: «I saw a lion shooting.»" + R_EN,
 "tr": "Karînesi ya tek bir şeydir — «Ok atan bir arslan gördüm» sözün gibi." + R_TR},
 "majaz": mj(6, "istiara", "mushabaha", {"en": "a lion", "tr": "arslan"}, {"en": "a brave man", "tr": "cesur bir adam"}),
 "tokens": [
  tok("وَقَرِينَتُهَا","qarina","noun",[I,"mubtada-khabar","idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَرِينَتُ مُبْتَدَأٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its clue» — the mubtada.", "«karînesi» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("قَرِينَتُ","qarina","noun"), seg("هَا","pron-3fs","pron")]),
  tok("إِمَّا","imma","part",[I,"atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("أَمْرٌ","amr","noun",[I,"mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a thing» — the khabar.", "«bir şey» — haber."),
  tok("وَاحِدٌ","wahid","noun",[I,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«one».", "«tek»."),
  tok("كَقَوْلِكَ","qawl","noun",[I,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — جِدَارٌ.", "«as in your saying» — the wall.", "«sözün gibi» — duvar.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("كَ","pron-2ms","pron")], punct=":"),
  tok("رَأَيْتُ","raa","verb",[I,"naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — رُؤْيَةُ الْعَيْنِ.", "«I saw» — with the eye.", "«gördüm» — gözle."),
  tok("أَسَدًا","asad","noun",[I,"maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: الْأَسَدُ لِلرَّجُلِ الشُّجَاعِ، وَالْقَرِينَةُ يَرْمِي.",
      "«a lion» — the object: the ISTIʿARA, the lion's name lent to a brave man; the clue is the ONE word after it.", "«bir arslan» — mef'ûl: İSTİÂRE, arslanın adı cesur adama ödünç; karîne ardındaki TEK kelimedir."),
  tok("يَرْمِي","rama","verb",[I,"jumla-sifa","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ صِفَةٌ لِأَسَدًا. هِيَ الْقَرِينَةُ: الْأَسَدُ لَا يَرْمِي.",
      "«shooting» — the describing clause: THE clue — a lion does not shoot arrows; the engine names it as the qarina.", "«ok atan» — vasıf cümlesi: KARÎNE — arslan ok atmaz; motor onu karîne diye adlandırır.",
      punct=".")]})

# ----------- s22 — the clue: more than one thing (the bayt as printed)
S.append({"id": "s22", "translation": {
 "en": "Or more than one, as in his saying: «If you shun justice and faith, then indeed in our right hands are fires.»" + R_EN,
 "tr": "Ya da birden çoktur — «Adaletten ve imandan kaçınırsanız, bilin ki sağ ellerimizde ateşler vardır» sözü gibi." + R_TR},
 "majaz": mj(12, "istiara", "mushabaha", {"en": "fires", "tr": "ateşler"}, {"en": "gleaming swords", "tr": "parlak kılıçlar"}),
 "tokens": [
  tok("وَإِمَّا","imma","part",[I,"atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا لِلتَّفْصِيلِ.", "«or».", "«ya da».", segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("أَكْثَرُ","akthar","noun",[I,"mubtada-khabar","ism-tafdil","mamnu-min-sarf"], "مَعْطُوفٌ عَلَى أَمْرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more» — an ism tafdil, diptote.", "«daha çok» — ism-i tafdil, gayr-i munsarif."),
  tok("مِنْ","min","part",[I,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  tok("وَاحِدٍ","wahid","noun",[I,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«one».", "«bir»."),
  tok("كَقَوْلِهِ","qawl","noun",[I,"huruf-jarr","idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ.", "«as in his saying».", "«sözü gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")], punct=":"),
  tok("وَإِنْ","in-shartiyya","part",[I,"in-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer».", segments=[seg("وَ","wa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("تَعَافُوا","afa-shun","verb",[I,"in-shartiyya","afal-khamsa","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — عَافَ يَعَافُ: كَرِهَ.",
      "«you shun» — one of the five verbs in jazm (the nun dropped); عَافَ = to loathe. The verb's REACH to justice and faith is the first clue.", "«kaçınırsanız» — ef'âl-i hamseden, cezmi nûn düşmesiyle; عَافَ = tiksinmek. Fiilin adalet ve imana TAALLUKU ilk karînedir."),
  tok("الْعَدْلَ","adl","noun",[I,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«justice».", "«adaleti»."),
  tok("وَالْإِيمَانَا","iman","noun",[I,"atf-nasaq"],
      "مَعْطُوفٌ مَنْصُوبٌ، وَالْأَلِفُ لِلْإِطْلَاقِ (الْإِيمَانَ).", "«and faith» — joined; the final alif is the rhyme's alif of itlaq.", "«ve imanı» — atıf; son elif kafiyenin ıtlak elifi.",
      segments=[seg("وَ","wa","conj"), seg("الْإِيمَانَا","iman","noun")]),
  tok("فَإِنَّ","inna","part",[I,"inna-wa-akhawatuha","in-shartiyya"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«then indeed» — the jawab.", "«bilin ki» — cevap.",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part")]),
  tok("فِي","fi","part",[I,"huruf-jarr","inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ مُقَدَّمٌ.", "«in» — the fronted khabar of إِنَّ.", "«-de» — إِنَّ'nin mukaddem haberi."),
  tok("أَيْمَانِنَا","yamin","noun",[I,"huruf-jarr","idafa-definiteness","jam-taksir"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ يَمِينٍ: الْأَيْدِي الْيُمْنَى، لَا الْحَلِفُ. الْقَرِينَةُ الثَّانِيَةُ: مَا فِي الْيَدِ لَا يَكُونُ نَارًا.",
      "«our right hands» — the plural of يَمِين (the hand, not the oath): the SECOND clue — what a hand holds is no fire.", "«sağ ellerimizde» — يَمِين'in çoğulu (el, yemin değil): İKİNCİ karîne — elde tutulan ateş olmaz.",
      segments=[seg("أَيْمَانِ","yamin","noun"), seg("نَا","pron-1p","pron")]),
  tok("نِيرَانَا","nar","noun",[I,"inna-wa-akhawatuha","jam-taksir"],
      "اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ، وَالْأَلِفُ لِلْإِطْلَاقِ (نِيرَانًا) — جَمْعُ نَارٍ. اسْتِعَارَةٌ: النِّيرَانُ لِلسُّيُوفِ اللَّامِعَةِ، بِقَرِينَتَيْنِ.",
      "«fires» — the delayed ism of إِنَّ (the alif of itlaq for نِيرَانًا): an ISTIʿARA, fires for gleaming SWORDS — with two clues, the verb's reach and the hands.", "«ateşler» — إِنَّ'nin muahhar ismi (نِيرَانًا için ıtlak elifi): İSTİÂRE, parlak KILIÇLAR yerine ateşler — iki karîneyle: fiilin taalluku ve eller.",
      punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "mustamal": g("مُسْتَعْمَل", "ع م ل", "noun", "used, employed (ism maf'ul of اسْتَعْمَلَ)", "kullanılan (اسْتَعْمَلَ'nin ism-i mef'ûlü)", 4),
 "istilah": g("اصْطِلَاح", "ص ل ح", "noun", "convention, agreed usage; technical term (masdar of اصْطَلَحَ)", "ıstılah, uzlaşılmış kullanım (اصْطَلَحَ'nin masdarı)", 4),
 "takhatub": g("تَخَاطُب", "خ ط ب", "noun", "addressing one another, discourse (masdar of تَخَاطَبَ)", "hitaplaşma, tehâtub (تَخَاطَبَ'nin masdarı)", 5),
 "qarina": find_gloss("qarina"),
 "irada": find_gloss("irada"),
 "alaqa": find_gloss("alaqa"),
 "ghalat": g("غَلَط", "غ ل ط", "noun", "mistake, error", "galat, hata", 3, plural="أَغْلَاط"),
 "lughawi": g("لُغَوِيّ", "ل غ و", "noun", "linguistic (nisba to لُغَة)", "lügavî (لُغَة'ye nisbet)", 4),
 "shari": find_gloss("shari"),
 "urfi": g("عُرْفِيّ", "ع ر ف", "noun", "customary (nisba to عُرْف)", "örfî (عُرْف'e nisbet)", 4),
 "khass": find_gloss("khass"),
 "amm": find_gloss("amm"),
 "dua": find_gloss("dua"),
 "ibada": g("عِبَادَة", "ع ب د", "noun", "worship", "ibadet", 2, plural="عِبَادَات"),
 "mushabaha": g("مُشَابَهَة", "ش ب ه", "noun", "likeness, resemblance (masdar of شَابَهَ)", "müşâbehet (شَابَهَ'nin masdarı)", 4),
 "illa-shartiyya": find_gloss("illa-shartiyya"),
 "istiara": g("اسْتِعَارَة", "ع و ر", "noun", "isti'ara — borrowing: the majaz whose relation is likeness (masdar of اسْتَعَارَ)", "istiâre — ödünç alma: alâkası müşâbehet olan mecaz (اسْتَعَارَ'nin masdarı)", 5),
 "tahqiqiyya": g("تَحْقِيقِيَّة", "ح ق ق", "noun", "tahqiqiyya — the isti'ara whose meaning is realised (nisba)", "tahkîkiyye — mânâsı gerçekleşen istiâre (nisbet)", 6),
 "tahaqquq": g("تَحَقُّق", "ح ق ق", "noun", "being realised, actual (masdar of تَحَقَّقَ)", "tahakkuk, gerçekleşme (تَحَقَّقَ'nin masdarı)", 4),
 "hiss": g("حِسّ", "ح س س", "noun", "sense, sensation", "his, duyu", 3),
 "aql": find_gloss("aql"),
 "shaki": g("شَاكٍ (الشَّاكِي)", "ش و ك", "noun", "fully armed (شَاكِي السِّلَاحِ); a manqus from شَائِك", "tepeden tırnağa silâhlı (شَاكِي السِّلَاحِ); شَائِك'ten mankûs", 6),
 "silah": g("سِلَاح", "س ل ح", "noun", "weapon, arms", "silâh", 2, plural="أَسْلِحَة"),
 "muqadhdhaf": g("مُقَذَّف", "ق ذ ف", "noun", "hurled (into battle) (ism maf'ul of قَذَّفَ)", "(savaşa) atılmış (قَذَّفَ'nin ism-i mef'ûlü)", 6),
 "libad": g("لِبَد", "ل ب د", "noun", "a mane (plural of لِبْدَة)", "yele (لِبْدَة'nin çoğulu)", 6),
 "zufr": g("ظُفْر", "ظ ف ر", "noun", "claw, nail", "pençe, tırnak", 3, plural="أَظْفَار"),
 "sirat": find_gloss("sirat"),
 "mustaqim": g("مُسْتَقِيم", "ق و م", "noun", "straight (ism fa'il of اسْتَقَامَ)", "dosdoğru (اسْتَقَامَ'nin ism-i fâili)", 2),
 "rukn": find_gloss("rukn"),
 "mustaar": g("مُسْتَعَار", "ع و ر", "noun", "borrowed (ism maf'ul of اسْتَعَارَ); the borrowed word", "müsteâr, ödünç alınan (اسْتَعَارَ'nin ism-i mef'ûlü)", 5),
 "mustair": g("مُسْتَعِير", "ع و ر", "noun", "borrower (ism fa'il of اسْتَعَارَ)", "müstaîr, ödünç alan (اسْتَعَارَ'nin ism-i fâili)", 5),
 "yad": find_gloss("yad"),
 "nima": g("نِعْمَة", "ن ع م", "noun", "favour, blessing", "nimet", 2, plural="نِعَم"),
 "qudra": find_gloss("qudra"),
 "rawiya": g("رَاوِيَة", "ر و ي", "noun", "the water-carrying camel; then the water-skin", "su taşıyan deve; sonra su tulumu", 6),
 "mazada": g("مَزَادَة", "ز ي د", "noun", "a large water-skin", "büyük su tulumu", 6),
 "tasmiya": find_gloss("tasmiya"),
 "ism": find_gloss("ism"),
 "rabia": g("رَبِيئَة", "ر ب أ", "noun", "a scout, look-out", "gözcü", 6),
 "isba": g("إِصْبَع", "ص ب ع", "noun", "finger", "parmak", 2, plural="أَصَابِع"),
 "anmula": g("أُنْمُلَة", "ن م ل", "noun", "fingertip", "parmak ucu", 5, plural="أَنَامِل"),
 "ghayth": g("غَيْث", "غ ي ث", "noun", "rain", "yağmur", 3),
 "musabbab": g("مُسَبَّب", "س ب ب", "noun", "effect, what is caused (ism maf'ul of سَبَّبَ)", "müsebbeb, sebep olunan (سَبَّبَ'nin ism-i mef'ûlü)", 4),
 "taala": g("تَعَالَى", "ع ل و", "verb", "Exalted is He (the formula after the divine name)", "Teâlâ (ilâhî isimden sonraki formül)", 2, form="VI"),
 "yatim": g("يَتِيم", "ي ت م", "noun", "orphan", "yetim", 2, plural="يَتَامَى"),
 "nadi": g("نَادٍ (النَّادِي)", "ن د و", "noun", "assembly, club (manqus)", "meclis, toplantı yeri (mankûs)", 4),
 "hall": g("حَالّ", "ح ل ل", "noun", "what dwells in a place (ism fa'il of حَلَّ)", "bir yerde bulunan (حَلَّ'nin ism-i fâili)", 5),
 "rahma": g("رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "ala-tool": find_gloss("ala-tool"),
 "lisan": find_gloss("lisan"),
 "bina": g("بِنَاء", "ب ن ي", "noun", "building, being built (masdar of بَنَى)", "binâ, kurulma (بَنَى'nın masdarı)", 3),
 "tawil": find_gloss("tawil"),
 "nasb-setting": g("نَصْب", "ن ص ب", "noun", "setting up, erecting (masdar of نَصَبَ)", "dikme, kurma (نَصَبَ'nin masdarı)", 3),
 "adl": g("عَدْل", "ع د ل", "noun", "justice", "adalet", 2),
 "iman": find_gloss("iman"),
 "yamin": find_gloss("yamin"),
 "ala-return": g("آلَ", "أ و ل", "verb", "to come to, end up as (آلَ يَؤُولُ; hollow)", "dönüşmek, sonunda olmak (آلَ يَؤُولُ; ecvef)", 5, form="I"),
 "qayyada": g("قَيَّدَ", "ق ي د", "verb", "to restrict, qualify (Form II)", "kayıtlamak (II. bâb)", 4, form="II"),
 "qallama": g("قَلَّمَ", "ق ل م", "verb", "to clip (nails, claws) (Form II)", "(tırnak) kesmek (II. bâb)", 5, form="II"),
 "raa-graze": g("رَعَى", "ر ع ي", "verb", "to graze, pasture (naqis-ya)", "otlatmak, otlamak (nâkıs-yâî)", 3, form="I"),
 "amtara": g("أَمْطَرَ", "م ط ر", "verb", "to rain (Form IV)", "yağdırmak (IV. bâb)", 3, form="IV"),
 "asara": g("عَصَرَ", "ع ص ر", "verb", "to press, squeeze", "sıkmak", 3, form="I"),
 "faraqa": g("فَارَقَ", "ف ر ق", "verb", "to part from, differ from (Form III)", "ayrılmak, farklı olmak (III. bâb)", 3, form="III"),
 "rama": find_gloss("rama"),
 "afa-shun": g("عَافَ", "ع ي ف", "verb", "to loathe, shun (hollow)", "tiksinmek, kaçınmak (ecvef)", 5, form="I"),
 "istamala": g("اسْتَعْمَلَ", "ع م ل", "verb", "to use (Form X)", "kullanmak (X. bâb)", 3, form="X"),
 "sahha": find_gloss("sahha"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/51.json").write_text(
    json.dumps({"chapter": 51, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 51 for c in man["chapters"]):
    man["chapters"].append({"n": 51, "title": TITLE51})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.51.0"
ADD_EN = (" Chapter 51 (lines ~3440-3570, sahifa 119-123) carries haqiqa and majaz: the aya s9 (1:6), the "
          "examples of the mursal in s13-s19 (رَعَيْنَا الْغَيْثَ, أَمْطَرَتِ السَّمَاءُ نَبَاتًا and the ayat 4:2, "
          "12:36, 96:17, 3:107, 26:84), the saying in s21 and the bayt s22 are Arabic as the source prints "
          "it, inside restored frames; the source writes وَاَتُوا (s15) where the app writes the standard "
          "وَآتُوا — the one divergence; the alif of itlaq on الْإِيمَانَا / نِيرَانَا (s22) is kept as printed. "
          "s8 prints Zuhayr's first hemistich only (لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ); the second (لَهُ لِبَدٌ "
          "أَظْفَارُهُ لَمْ تُقَلَّمِ) is the received text of the bayt, added and marked restored. s1-s7, "
          "s10-s12, s20 and the frames of s13-s19, s21-s22 are RESTORATIONS, not quotations: the source "
          "carries those steps only in Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording "
          "in the musannif's register; each is marked «restored» in its translation. Every majaz carries an "
          "authored `majaz` frame the engine is tested against — the word, its kind (mursal, isti'ara) and its "
          "'alaqa; the example-kaf and the كَقَوْلِهِ walls are authored as no likening.")
ADD_TR = (" Elli birinci bâb (satır ~3440-3570, sahife 119-123) hakikat ve mecazı taşır: s9 âyeti (1:6), "
          "s13-s19'daki mürsel örnekleri (رَعَيْنَا الْغَيْثَ, أَمْطَرَتِ السَّمَاءُ نَبَاتًا ve 4:2, 12:36, 96:17, "
          "3:107, 26:84 âyetleri), s21'deki söz ve s22 beyti, geri yazılmış çerçeveler içinde kaynağın bastığı "
          "Arapçadır; kaynak وَاَتُوا yazar (s15), uygulama standart وَآتُوا — tek fark; الْإِيمَانَا / نِيرَانَا "
          "(s22) üzerindeki ıtlak elifi basıldığı gibi korunmuştur. s8'de kaynak Züheyr'in yalnız ilk mısraını "
          "basar (لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ); ikincisi (لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ) beytin yerleşik "
          "metnidir, eklenmiş ve geri yazım diye işaretlenmiştir. s1-s7, s10-s12, s20 ile s13-s19, s21-s22'nin "
          "çerçeveleri ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla "
          "taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri "
          "yazılmıştır» diye işaretlidir. Her mecaz, motorun sınandığı müellif eliyle yazılmış bir `majaz` "
          "çerçevesi taşır — kelime, nev'i (mürsel, istiâre) ve alâkası; örnek kâfı ve كَقَوْلِهِ duvarları "
          "benzetme değil diye yazılmıştır.")
if "3440-3570" not in man["attribution"]["en"]:
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
put("istamala", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَعْمَل", "سْتَعْمِل", "اِسْتَعْمِل", "اِسْتِعْمَال", "مُسْتَعْمِل", "مُسْتَعْمَل", "اُسْتُعْمِلَ", "يُسْتَعْمَلُ"))
put("qayyada", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَيَّد", "قَيِّد", "قَيِّد", "تَقْيِيد", "مُقَيِّد", "مُقَيَّد", "قُيِّدَ", "يُقَيَّدُ"))
put("qallama", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَلَّم", "قَلِّم", "قَلِّم", "تَقْلِيم", "مُقَلِّم", "مُقَلَّم", "قُلِّمَ", "يُقَلَّمُ",
                           "فِي الشِّعْرِ يُحَرَّكُ الْمَجْزُومُ بِالْكَسْرِ لِلْقَافِيَةِ: لَمْ تُقَلَّمِ."))
put("raa-graze", _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ", "y", "رَعَ", "رْع", "a", "اِرْع", "رَعْي", "رَاعٍ (الرَّاعِي)", "مَرْعِيّ", "رُعِيَ", "يُرْعَى",
                            "نَاقِصٌ يَائِيٌّ مِنْ بَابِ فَتَحَ: رَعَى يَرْعَى، رَعَيْنَا."))
put("amtara", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَمْطَر", "مْطِر", "أَمْطِر", "إِمْطَار", "مُمْطِر", "مُمْطَر", "أُمْطِرَ", "يُمْطَرُ"))
put("asara", _sg.sound1("daraba", "عَصَر", "عْصِر", "اِعْصِر", "عَصْر", "عَاصِر", "مَعْصُور", "عُصِرَ", "يُعْصَرُ"))
put("faraqa", _sg.derived(_sg.B3, _sg.W3, "ُ", "فَارَق", "فَارِق", "فَارِق", "مُفَارَقَة", "مُفَارِق", "مُفَارَق", "فُورِقَ", "يُفَارَقُ"))
put("afa-shun", _sg.hollow1("fataha", "أَجْوَفُ يَائِيٌّ", "عَاف", "عِف", "عَاف", "عَف", "عَاف", "عَف", "عِيَافَة", "عَائِف", None, None, None,
                            "أَجْوَفُ مِنْ بَابِ فَتَحَ (عَافَ يَعَافُ): تَعَافُوا بِحَذْفِ النُّونِ فِي الْجَزْمِ."))
put("ala-return", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ مَهْمُوزُ الْفَاءِ", "آل", "أُل", "ؤُول", "ؤُل", "أُول", "أُل", "أَوْل", "آئِل", None, None, None,
                              "آلَ يَؤُولُ: الْهَمْزَةُ فَاؤُهُ، تُكْتَبُ عَلَى وَاوٍ بَعْدَ الضَّمَّةِ (يَؤُولُ)."))
put("rama", find_morph("rama"))
put("sahha", find_morph("sahha"))
put("taala", _sg.derived_naqis(_sg.B6, _sg.W6, "َ", "تَعَالَ", "تَعَال", "a", "تَعَال", "تَعَالٍ (التَّعَالِي)", "مُتَعَالٍ (الْمُتَعَالِي)", None, None, None,
                               "لَا يُسْتَعْمَلُ مَعَ اسْمِ اللهِ إِلَّا الْمَاضِي: اللهُ تَعَالَى."))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the notes
GR = ROOT / "content/grammar"
NOTE_M = {
 "id": "majaz-mursal",
 "title": {"ar": "الْمَجَازُ الْمُرْسَلُ — عَلَاقَاتُهُ وَقَرَائِنُهُ", "en": "The majaz mursal — its relations and its clues", "tr": "Mecâz-ı mürsel — alâkaları ve karîneleri"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الحقيقة والمجاز، المجاز المرسل"],
 "question": {
  "en": ["Is the word used for what it was coined for (HAQIQA) or for something else (MAJAZ)? A majaz needs a RELATION that makes the move sound and a CLUE that bars the literal reading.",
         "Is the relation LIKENESS? Then the majaz is an istiʿara. Any other relation — cause, effect, part, whole, past state, future state, place, dweller, instrument — makes it MURSAL.",
         "What is the clue? A verb that cannot take the literal object (رَعَيْنَا الْغَيْثَ: one cannot graze rain), a place that cannot be called (نَادِيَهُ), a thing that is not pressed (خَمْرًا)."],
  "tr": ["Kelime konulduğu mânâda mı (HAKİKAT) başka mânâda mı (MECAZ) kullanılmış? Mecaz, geçişi sahih kılan bir ALÂKA ve hakikati engelleyen bir KARÎNE ister.",
         "Alâka MÜŞÂBEHET mi? O zaman mecaz istiâredir. Başka her alâka — sebep, müsebbeb, cüz, kül, geçmiş hâl, gelecek hâl, mahal, hâll, âlet — onu MÜRSEL yapar.",
         "Karîne nedir? Hakikî mef'ûlü alamayan bir fiil (رَعَيْنَا الْغَيْثَ: yağmur otlatılmaz), çağrılamayan bir yer (نَادِيَهُ), sıkılmayan bir şey (خَمْرًا)."]},
 "plain": {
  "en": "A word moved off its literal meaning is a majaz. When the move rides on likeness it is an istiʿara; when it rides on any other tie — cause and effect, part and whole, what a thing was or will be, its place, its dweller, its instrument — it is MURSAL. The engine reads the received pairs and the clue on the surface.",
  "tr": "Hakikî mânâsından kaydırılmış kelime mecazdır. Geçiş müşâbehete dayanıyorsa istiâre; başka bir bağa — sebep-müsebbeb, cüz-kül, bir şeyin ne idiği ve ne olacağı, yeri, sakini, âleti — dayanıyorsa MÜRSELdir. Motor yerleşik çiftleri ve yüzeydeki karîneyi okur."},
 "explanation": {
  "en": "HAQIQA is the word used in what it was coined for, in the convention of those speaking (اصْطِلَاحُ التَّخَاطُبِ); MAJAZ the word used in other than that, in a way that is sound (a RELATION, which keeps out the mere mistake) together with a CLUE that the literal is not meant (which keeps out the KINAYA, where the literal may still be meant). Each may be linguistic (الْأَسَد for the beast, then for the brave man), legal (الصَّلَاة for supplication, then for the worship), or customary — particular (فِعْل among grammarians) or general (دَابَّة for a four-footed beast). A single-word majaz whose relation is LIKENESS is an ISTIʿARA; any other relation makes it MURSAL — «sent loose» from likeness. The Talkhis lists the relations with the matn's own examples, and the engine stores them as received pairs: the CAUSE for the effect — رَعَيْنَا الْغَيْثَ, the rain for the pasture it grew; the EFFECT for the cause — أَمْطَرَتِ السَّمَاءُ نَبَاتًا, plants for the rain; the PART for the whole — الْعَيْن for the scout (رَبِيئَة); the WHOLE for the part — الْأَصَابِع for the fingertips (أَنَامِل); what a thing WAS — وَآتُوا الْيَتَامَى أَمْوَالَهُمْ, the orphans now of age (4:2); what it WILL BE — إِنِّي أَرَانِي أَعْصِرُ خَمْرًا, the grapes called wine (12:36); the PLACE for its people — فَلْيَدْعُ نَادِيَهُ (96:17); the DWELLER for the place — فَفِي رَحْمَةِ اللهِ هُمْ فِيهَا خَالِدُونَ, mercy for Paradise (3:107); the INSTRUMENT for its product — وَاجْعَلْ لِي لِسَانَ صِدْقٍ فِي الْآخِرِينَ, a tongue for a good mention (26:84); and adjacency — الرَّاوِيَة, the water-camel, for the water-skin it carries; the hand (الْيَد) for a favour and for power. WHAT THE ENGINE CLAIMS: the received pairs by verb and object (رَعَى + غَيْث، أَمْطَرَ + نَبَات، آتَى + يَتَامَى، عَصَرَ + خَمْر، دَعَا + نَادِي، جَعَلَ + لِسَان، فِي + رَحْمَة) with their ʿalaqa, haqiqa and murad, and it names the qarina — the verb or particle that cannot take the word literally. It refuses a frame where the relation would be knowledge alone (الْعَيْن for the scout is read only when authored). The majaz by ADDITION (لَيْسَ كَمِثْلِهِ شَيْءٌ: the kaf is extra) and by OMISSION (وَاسْأَلِ الْقَرْيَةَ: أَهْلَ is dropped) and the MENTAL majaz (the attribution moved: أَنْبَتَ الرَّبِيعُ الْبَقْلَ) it reads from the surface too.",
  "tr": "HAKİKAT, konuşanların ıstılahında (اصْطِلَاحُ التَّخَاطُبِ) konulduğu mânâda kullanılan kelime; MECAZ ondan başkasında, sahih bir vecih üzere (bir ALÂKA, sırf hatayı dışarıda bırakır), hakikatin kastedilmediğine dair bir KARÎNEyle (KİNÂYEyi dışarıda bırakır; orada hakikat de kastedilebilir) kullanılan kelimedir. Her biri lügavî (yırtıcı için, sonra cesur adam için الْأَسَد), şer'î (dua için, sonra namaz için الصَّلَاة) yahut örfî — hâs (nahivcilerde فِعْل) yahut âm (dört ayaklı için دَابَّة) — olur. Alâkası MÜŞÂBEHET olan müfred mecaz İSTİÂREdir; başka her alâka onu MÜRSEL yapar — müşâbehetten «salınmış». Telhîs alâkaları matnın kendi örnekleriyle sayar, motor onları yerleşik çiftler olarak saklar: müsebbeb yerine SEBEP — رَعَيْنَا الْغَيْثَ, bitirdiği ot yerine yağmur; sebep yerine MÜSEBBEB — أَمْطَرَتِ السَّمَاءُ نَبَاتًا, yağmur yerine bitki; kül yerine CÜZ — gözcü (رَبِيئَة) için الْعَيْن; cüz yerine KÜL — parmak uçları (أَنَامِل) için الْأَصَابِع; NE İDİYSE — وَآتُوا الْيَتَامَى أَمْوَالَهُمْ, artık bâliğ yetimler (4:2); NE OLACAKSA — إِنِّي أَرَانِي أَعْصِرُ خَمْرًا, şarap denen üzüm (12:36); ehli yerine MAHAL — فَلْيَدْعُ نَادِيَهُ (96:17); mahal yerine HÂLL — فَفِي رَحْمَةِ اللهِ هُمْ فِيهَا خَالِدُونَ, cennet yerine rahmet (3:107); ürünü yerine ÂLET — وَاجْعَلْ لِي لِسَانَ صِدْقٍ فِي الْآخِرِينَ, güzel anılış yerine dil (26:84); ve mücâveret — taşıdığı tulum yerine su devesi الرَّاوِيَة; nimet ve kudret yerine el (الْيَد). MOTORUN İDDİASI: fiil ve mef'ûl ile yerleşik çiftler (رَعَى + غَيْث، أَمْطَرَ + نَبَات، آتَى + يَتَامَى، عَصَرَ + خَمْر، دَعَا + نَادِي، جَعَلَ + لِسَان، فِي + رَحْمَة) alâkası, hakikati ve murâdıyla; ve karîneyi adlandırır — kelimeyi hakikatiyle alamayan fiil yahut harf. Alâkanın yalnız bilgi olduğu yerde çerçeve okumaz (gözcü için الْعَيْن ancak müellif yazınca okunur). ZİYÂDE ile mecazı (لَيْسَ كَمِثْلِهِ شَيْءٌ: kâf fazla), NOKSAN ile mecazı (وَاسْأَلِ الْقَرْيَةَ: أَهْلَ düşmüş) ve AKLÎ mecazı (isnâd kaymış: أَنْبَتَ الرَّبِيعُ الْبَقْلَ) da yüzeyden okur."},
 "examples": [
  {"ar": "رَعَيْنَا الْغَيْثَ", "en": "the cause for the effect; the clue is the verb of grazing.", "tr": "müsebbeb yerine sebep; karîne otlatma fiili.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "أَمْطَرَتِ السَّمَاءُ نَبَاتًا", "en": "the effect for the cause.", "tr": "sebep yerine müsebbeb.", "sourceStory": "talkhis-al-miftah", "sentence": "s14"},
  {"ar": "وَآتُوا الْيَتَامَى أَمْوَالَهُمْ", "en": "what they were.", "tr": "ne idiyseler.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"},
  {"ar": "فَفِي رَحْمَةِ اللهِ هُمْ فِيهَا خَالِدُونَ", "en": "the dweller for the place; the clue is فِيهَا خَالِدُونَ.", "tr": "mahal yerine hâll; karîne فِيهَا خَالِدُونَ.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"}],
 "commonMistakes": [
  {"wrong": "«رَعَيْنَا الْغَيْثَ bir istiâredir: ot yağmura benzetilmiş»",
   "right": "«Mürseldir: yağmur, bitirdiği otun SEBEBİdir — benzerlik yok, sebep-müsebbeb bağı var»",
   "why": {"en": "Only likeness makes an istiʿara. Cause, effect, part, whole, place and instrument are ties, not resemblances — the majaz they carry is mursal.", "tr": "İstiâreyi ancak müşâbehet yapar. Sebep, müsebbeb, cüz, kül, mahal ve âlet benzerlik değil bağdır — taşıdıkları mecaz mürseldir."}},
  {"wrong": "«فَفِي رَحْمَةِ اللهِ: rahmet hakikattir, mecaz yoktur»",
   "right": "«فِيهَا خَالِدُونَ karînedir: içinde ebedî kalınan bir YER kastedilmiştir — cennet»",
   "why": {"en": "Without a clue the literal stands; with فِيهَا خَالِدُونَ the mercy must be a place, and the word has moved.", "tr": "Karînesiz hakikat kalır; فِيهَا خَالِدُونَ ile rahmet bir yer olmak zorundadır ve kelime kaymıştır."}}],
 "relatedNotes": ["haqiqa-majaz", "anwa-al-majaz", "istiara", "arkan-al-istiara", "majaz-aqli", "qarinat-al-majaz", "kinaya", "tashbih", "ilm-al-bayan"]}
NOTE_I = {
 "id": "arkan-al-istiara",
 "title": {"ar": "أَرْكَانُ الِاسْتِعَارَةِ — وَالتَّحْقِيقِيَّةُ وَقَرِينَتُهَا", "en": "The arkan of the istiʿara — the tahqiqiyya and its clue", "tr": "İstiârenin rükünleri — tahkîkiyye ve karînesi"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الاستعارة"],
 "question": {
  "en": ["Four arkan: the MUSTAʿAR MINHU (the bihi the name is taken from), the MUSTAʿAR LAHU (the mushabbah it is given to), the MUSTAʿAR (the word itself), the MUSTAʿIR (the speaker).",
         "Is the intended meaning realised by SENSE (the armed «lion» is a man) or by REASON (the «path» is the true religion)? Then the istiʿara is TAHQIQIYYA.",
         "How does the istiʿara differ from a lie? By the CLAIM that the mushabbah is of the bihi's kind, and by a CLUE — one word (يَرْمِي), several (تَعَافُوا الْعَدْلَ … فِي أَيْمَانِنَا), or the sense of the whole."],
  "tr": ["Dört rükün: MÜSTEÂRUN MİNH (adın alındığı bih), MÜSTEÂRUN LEH (adın verildiği müşebbeh), MÜSTEÂR (kelimenin kendisi), MÜSTAÎR (konuşan).",
         "Kastedilen mânâ HİSSEN mi (silâhlı «arslan» bir adamdır) AKLEN mi (yol, hak dindir) gerçekleşir? O zaman istiâre TAHKÎKİYYEdir.",
         "İstiâre yalandan nasıl ayrılır? Müşebbehin bihin cinsinden olduğu İDDİASIyla ve bir KARÎNEyle — tek kelime (يَرْمِي), birkaç (تَعَافُوا الْعَدْلَ … فِي أَيْمَانِنَا), yahut bütünün mânâsı."]},
 "plain": {
  "en": "An istiʿara is a likening with one end dropped: the bihi's name is lent to the mushabbah. Its four arkan: the word's source, its new owner, the word, the speaker. A clue must bar the literal reading, else the sentence is a lie. The engine finds the lent word among stock likenesses and names the clue.",
  "tr": "İstiâre, bir tarafı düşmüş benzetmedir: bihin adı müşebbehe ödünç verilir. Dört rüknü, ödünç kelimenin kaynağı, yeni sahibi, kelimenin kendisi ve konuşandır. Bir karîne hakikati engellemelidir — yoksa cümle yalan yahut hatadır. Motor ödünç kelimeyi yerleşik benzetmeler arasında bulur ve karîneyi yanında adlandırır."},
 "explanation": {
  "en": "When the relation is likeness the majaz is an ISTIʿARA; most often the word is the BIHI's name used for the mushabbah. Its ARKAN are four: مُسْتَعَارٌ مِنْهُ, the bihi from which the name is borrowed (the lion); مُسْتَعَارٌ لَهُ, the mushabbah it is lent to (the brave man); مُسْتَعَار, the word (أَسَد); مُسْتَعِير, the borrower who speaks it. It may be qualified as TAHQIQIYYA because its meaning is REALISED — by sense, as in Zuhayr's لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ, where «lion» is a warrior the eye can see (and mane and claws FURNISH the loan with the lion's own traits); or by reason, as in اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ, where «path» is the true religion the mind grasps (1:6). The istiʿara is a LINGUISTIC majaz: the word was coined for the bihi alone, not for both. It DIFFERS FROM THE LIE by being built on interpretation — the CLAIM that the mushabbah belongs to the bihi's kind — and by the setting-up of a CLUE that the opposite of the surface is meant; the liar claims nothing and wants his words taken literally. The clue is one thing — رَأَيْتُ أَسَدًا يَرْمِي, where يَرْمِي alone bars the beast — or more than one — وَإِنْ تَعَافُوا الْعَدْلَ وَالْإِيمَانَا فَإِنَّ فِي أَيْمَانِنَا نِيرَانَا, where the verb's reach to justice and faith and the fires being IN HANDS together make «fires» swords — or the sense of the whole line. WHAT THE ENGINE CLAIMS: a stock-likeness noun (أَسَد، بَحْر، بَدْر، نَار…) standing where its literal sense cannot (a describing clause it could not do, a perception verb, a place it cannot be) is an istiʿara CANDIDATE with the clue named — sure only where the surface bars the literal, a shortlist where knowledge does. It does not build a tashbih frame for it: the mushabbah is dropped by definition, and the frame is the majaz frame.",
  "tr": "Alâka müşâbehet olunca mecaz İSTİÂREdir; çoğu kere kelime, müşebbeh için kullanılan BİHİN adıdır. RÜKÜNLERİ dörttür: مُسْتَعَارٌ مِنْهُ, adın ödünç alındığı bih (arslan); مُسْتَعَارٌ لَهُ, adın ödünç verildiği müşebbeh (cesur adam); مُسْتَعَار, kelime (أَسَد); مُسْتَعِير, onu söyleyen ödünç alan. Mânâsı GERÇEKLEŞTİĞİ için TAHKÎKİYYE ile kayıtlanabilir — hissen, Züheyr'in لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ beytinde «arslan» gözün gördüğü bir savaşçıdır (yele ve pençe, ödüncü arslanın kendi vasıflarıyla DONATIR); yahut aklen, اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ'de «yol» aklın kavradığı hak dindir (1:6). İstiâre LÜGAVÎ mecazdır: kelime yalnız bih için konulmuştur, ikisi için değil. YALANDAN, te'vil üzere kurulmasıyla — müşebbehin bihin cinsinden olduğu İDDİASI — ve zâhirin hilâfının kastedildiğine KARÎNE dikilmesiyle AYRILIR; yalancı hiçbir şey iddia etmez ve sözünün zâhirini ister. Karîne tek bir şeydir — رَأَيْتُ أَسَدًا يَرْمِي, يَرْمِي tek başına yırtıcıyı engeller — yahut birden çok — وَإِنْ تَعَافُوا الْعَدْلَ وَالْإِيمَانَا فَإِنَّ فِي أَيْمَانِنَا نِيرَانَا, fiilin adalet ve imana taalluku ile ateşlerin ELLERDE olması birlikte «ateşler»i kılıç yapar — yahut bütünün mânâsı. MOTORUN İDDİASI: hakikî mânâsının duramayacağı yerde duran yerleşik benzetme ismi (أَسَد، بَحْر، بَدْر، نَار…) — yapamayacağı bir vasıf cümlesi, bir idrak fiili, olamayacağı bir yer — karînesi adlandırılmış bir istiâre ADAYIdır; yüzey hakikati engelliyorsa kesin, bilgi engelliyorsa kısa liste. Ona teşbih çerçevesi kurmaz: müşebbeh tarifi gereği düşmüştür, çerçeve mecaz çerçevesidir."},
 "examples": [
  {"ar": "لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ", "en": "tahqiqiyya by sense; the clue: arms.", "tr": "hissen tahkîkiyye; karîne: silâh.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ", "en": "tahqiqiyya by reason.", "tr": "aklen tahkîkiyye.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "رَأَيْتُ أَسَدًا يَرْمِي", "en": "one clue.", "tr": "tek karîne.", "sourceStory": "talkhis-al-miftah", "sentence": "s21"},
  {"ar": "فَإِنَّ فِي أَيْمَانِنَا نِيرَانَا", "en": "two clues: the verb's reach and the hands.", "tr": "iki karîne: fiilin taalluku ve eller.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«رَأَيْتُ أَسَدًا يَرْمِي bir teşbihtir: adam arslana benzetilmiş»",
   "right": "«İstiâredir: müşebbeh (adam) hiç söylenmemiş, arslanın adı ona verilmiştir»",
   "why": {"en": "A tashbih keeps both ends; an istiʿara drops the mushabbah and lends the bihi's name. The engine builds a majaz frame, not a tashbih frame.", "tr": "Teşbih iki tarafı tutar; istiâre müşebbehi düşürür, bihin adını ödünç verir. Motor teşbih değil mecaz çerçevesi kurar."}},
  {"wrong": "«رَأَيْتُ أَسَدًا (tek başına) istiâredir»",
   "right": "«Karînesiz hakikat kalır: gerçek bir arslan görülmüştür»",
   "why": {"en": "Without يَرْمِي or another bar on the literal, the word means what it was coined for. The clue is a rukn of the reading, not an ornament.", "tr": "يَرْمِي yahut hakikati engelleyen başka bir şey olmadan kelime konulduğu mânâdadır. Karîne okumanın rüknüdür, süsü değil."}}],
 "relatedNotes": ["istiara", "majaz-mursal", "haqiqa-majaz", "qarinat-al-majaz", "arkan-al-tashbih", "tashbih", "jumla-sifa", "ism-maqsur-manqus"]}
for n in (NOTE_M, NOTE_I):
    (GR / f"{n['id']}.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")
for nid, add in (("haqiqa-majaz", ["majaz-mursal", "arkan-al-istiara"]), ("istiara", ["arkan-al-istiara", "majaz-mursal"]), ("anwa-al-majaz", ["majaz-mursal"])):
    fp = GR / f"{nid}.json"
    if not fp.exists(): continue
    w = json.loads(fp.read_text(encoding="utf-8"))
    ch = False
    for a in add:
        if a not in w.get("relatedNotes", []): w.setdefault("relatedNotes", []).append(a); ch = True
    if ch: fp.write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch51:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + 10 built, 1 copied; notes majaz-mursal, arkan-al-istiara;",
      "majaz frames:", sum(1 for x in S if x.get("majaz")))
