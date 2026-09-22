# -*- coding: utf-8 -*-
"""Author chapter 46 of talkhis-al-miftah — the BAYAN DOOR: فَنُّ الْبَيَانِ opens.

Sahifa 102-104 (lines ~2955-3025): the definition of ʿilm al-bayan, its
subject, the three dalalat, the definition of tashbih, its four arkan, and
the two ends (tarafan) — hissi, ʿaqli, khayali, wahmi — with the
textbook examples.

  s1-s2  the matn's definition: وَهُوَ عِلْمٌ يُعْرَفُ بِهِ إِيرَادُ الْمَعْنَى
         الْوَاحِدِ بِطُرُقٍ مُخْتَلِفَةٍ فِي وُضُوحِ الدَّلَالَةِ عَلَيْهِ (Arabic as
         the source prints it).
  s3     its subject — RESTORED from the source's Q/A paraphrase.
  s4-s6  the dalala triad — RESTORED from the paraphrase (wadʿiyya /
         ʿaqliyya; mutabaqa, tadammun, iltizam).
  s7     the definition of tashbih (Arabic as printed): الدَّلَالَةُ عَلَى
         مُشَارَكَةِ أَمْرٍ لِأَمْرٍ فِي مَعْنًى.
  s8-s9  زَيْدٌ أَسَدٌ and صُمٌّ بُكْمٌ عُمْيٌ (2:18) — the shapes the
         definition still covers.
  s10    the four arkan — RESTORED from the source's Q/A.
  s11-s18 the tarafan: the five senses (خَدُّهُ كَالْوَرْدِ …), the ʿaqli
         pair (الْعِلْمُ كَالْحَيَاةِ), the mixed pairs (الْمَنِيَّةُ كَالسَّبُعِ،
         الْعِطْرُ كَخُلُقٍ كَرِيمٍ) — Arabic as printed.
  s19-s20 the khayali bayt (Ibn al-Muʿtazz per the commentaries; the source
         gives no name) and s21-s22 Imruʾ al-Qays's wahmi bayt — as the
         source recites them, split at the hemistich, the rhyme sukun on
         تَصَعَّدْ / زَبَرْجَدْ kept as printed.

Every likening carries an AUTHORED `tashbih` frame (token indices of the
mushabbah, the adat, the mushabbah bihi, the wajh, and the kind) — the
TashbihEngine must agree with it, and the smoke suite says so.

Grammar this chapter teaches: note 150 `ilm-al-bayan` and note 151
`arkan-al-tashbih` (group bayan); the fused kaf of likening; كَأَنَّ's ism
and khabar as the two ends; the sound plurals of colour and defect
(صُمٌّ بُكْمٌ عُمْيٌ، زُرْقٌ); the majhul on the group's nun (نُشِرْنَ);
the question hamza on a mudari with the speaker's ya (أَيَقْتُلُنِي);
paradigms قَتَلَ، تَصَوَّبَ، تَصَعَّدَ; نَشَرَ copied.
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
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
def copy_morph(pkg, key):
    return json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))["verbs"][key]
S = []
B = "ilm-al-bayan"; A = "arkan-al-tashbih"

TITLE46 = {"ar": "فَنُّ الْبَيَانِ: تَعْرِيفُهُ وَالتَّشْبِيهُ وَأَرْكَانُهُ وَطَرَفَاهُ",
           "en": "The Science of Bayan: its Definition, Tashbih, its Four Arkan and its Two Ends",
           "tr": "Beyân İlmi: Tarifi, Teşbih, Dört Rüknü ve İki Tarafı"}

# ----------- s1 — the definition, first clause
S.append({"id": "s1", "translation": {
 "en": "And it is a science by which is known the bringing of ONE meaning",
 "tr": "O, BİR mânâyı getirmenin kendisiyle bilindiği bir ilimdir"},
 "tokens": [
  tok("وَهُوَ","huwa","pron",[B,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — عَائِدٌ عَلَى عِلْمِ الْبَيَانِ.",
      "«and it» — the mubtada, pointing back to the science just named.",
      "«o» — mübtedâ; az önce adı geçen ilme râci'.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("عِلْمٌ","ilm","noun",[B,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«a science» — the khabar; the definition's genus.",
      "«bir ilim» — haber; tarifin cinsi."),
  tok("يُعْرَفُ","arafa","verb",[B,"naib-al-fail","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ صِفَةٌ لِعِلْمٍ.",
      "«is known» — the passive; its clause is the sifa of عِلْمٌ (a science BY WHICH…).",
      "«bilinir» — meçhûl; cümlesi عِلْمٌ'in sıfatı (KENDİSİYLE … bilinen bir ilim)."),
  tok("بِهِ","bi","part",[B,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيُعْرَفُ.",
      "«by it» —",
      "«kendisiyle» —",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("إِيرَادُ","irad","noun",[B,"naib-al-fail","masdar"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ أَوْرَدَ.",
      "«the bringing of» — the deputy doer, a Form IV masdar, a mudaf.",
      "«getirilmesi» — nâib-i fâil; IV. bâb masdarı, muzâf."),
  tok("الْمَعْنَى","mana","noun",[B,"ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«the meaning» — a maqsur.",
      "«mânânın» — maksûr."),
  tok("الْوَاحِدِ","wahid","noun",[B,"naat-sifa"],
      "صِفَةٌ مَجْرُورَةٌ.",
      "«one» — ONE meaning: the science is about many roads to one place.",
      "«bir» — BİR mânâ: ilim, bir yere giden birçok yol hakkındadır.")],
 "jumal": [
  J("يُعْرَفُ بِهِ إِيرَادُ الْمَعْنَى الْوَاحِدِ",
    "جُمْلَةٌ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِعِلْمٍ.",
    "The clause-sifa that makes «a science» THIS science.",
    "«Bir ilm»i BU ilim yapan cümle-sıfat.")]})

# ----------- s2 — second clause
S.append({"id": "s2", "translation": {
 "en": "by DIFFERENT roads, in the clarity of the indication of it.",
 "tr": "— ona delâletin açıklığında FARKLI yollarla."},
 "tokens": [
  tok("بِطُرُقٍ","tariq","noun",[B,"huruf-jarr"],
      "الْبَاءُ جَارَّةٌ، وَطُرُقٍ مَجْرُورٌ — جَمْعُ طَرِيقٍ، مُتَعَلِّقٌ بِإِيرَادُ.",
      "«by roads» — the masdar's own complement: the bringing is done BY roads.",
      "«yollarla» — masdarın kendi mütealliki: getirme YOLLARLA olur.",
      segments=[seg("بِ","bi","part"), seg("طُرُقٍ","tariq","noun")]),
  tok("مُخْتَلِفَةٍ","mukhtalif","noun",[B,"naat-sifa","ism-fail","form-viii-verbs"],
      "صِفَةٌ مَجْرُورَةٌ — اسْمُ فَاعِلٍ مِنِ اخْتَلَفَ.",
      "«different» — Form VIII's ism fa'il.",
      "«farklı» — VIII. bâbın ism-i fâili."),
  tok("فِي","fi","part",[B,"huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«-de» —"),
  tok("وُضُوحِ","wuduh","noun",[B,"masdar"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ — وَشِبْهُ الْجُمْلَةِ صِفَةٌ لِطُرُقٍ.",
      "«the clarity of» — the roads differ IN CLARITY: that is the whole science.",
      "«açıklığında» — yollar AÇIKLIKTA farklıdır: ilmin bütün derdi budur."),
  tok("الدَّلَالَةِ","dalala","noun",[B],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the indication» —",
      "«delâletin» —"),
  tok("عَلَيْهِ","ala","part",[B,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالدَّلَالَةِ.",
      "«of it» — the indication OF that one meaning.",
      "«ona» — o bir mânâya delâlet.",
      punct=".",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")])],
 "jumal": [
  J("بِطُرُقٍ مُخْتَلِفَةٍ فِي وُضُوحِ الدَّلَالَةِ عَلَيْهِ",
    "مُتَعَلِّقُ الْمَصْدَرِ وَصِفَتُهُ — قَيْدُ التَّعْرِيفِ.",
    "The definition's restriction: not any roads — roads that differ in how clearly they point.",
    "Tarifin kaydı: herhangi yollar değil — ne kadar açık gösterdikleri bakımından farklı yollar.")]})

# ----------- s3 — the subject (restored)
S.append({"id": "s3", "translation": {
 "en": "And its subject is tashbih, majaz and kinaya. (Restored from the source's question-and-answer.)",
 "tr": "Mevzuu teşbih, mecaz ve kinayedir. (Kaynağın soru-cevabından geri yazılmıştır.)"},
 "tokens": [
  tok("وَمَوْضُوعُهُ","mawdu","noun",[B,"mubtada-khabar","ism-maful"],
      "الْوَاوُ عَاطِفَةٌ، وَمَوْضُوعُ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«and its subject» — the mubtada, an ism maf'ul.",
      "«ve mevzuu» — mübtedâ, ism-i mef'ûl.",
      segments=[seg("وَ","wa","conj"), seg("مَوْضُوعُ","mawdu","noun"), seg("هُ","pron-3ms","pron")]),
  tok("التَّشْبِيهُ","tashbih","noun",[B,A,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«tashbih» — the first of the three doors, and this chapter's.",
      "«teşbih» — üç kapının ilki; bu bâbın konusu."),
  tok("وَالْمَجَازُ","majaz","noun",[B,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالْمَجَازُ مَعْطُوفٌ مَرْفُوعٌ.",
      "«and majaz» —",
      "«ve mecaz» —",
      segments=[seg("وَ","wa","conj"), seg("الْمَجَازُ","majaz","noun")]),
  tok("وَالْكِنَايَةُ","kinaya","noun",[B,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالْكِنَايَةُ مَعْطُوفٌ مَرْفُوعٌ.",
      "«and kinaya» — majaz before kinaya, the source says, because majaz's meaning is like a PART of kinaya's.",
      "«ve kinaye» — kaynağa göre mecaz kinayeden önce gelir; zira mecazın mânâsı kinayeninkinin bir PARÇASI gibidir.",
      punct=".",
      segments=[seg("وَ","wa","conj"), seg("الْكِنَايَةُ","kinaya","noun")])],
 "jumal": [
  J("وَمَوْضُوعُهُ التَّشْبِيهُ وَالْمَجَازُ وَالْكِنَايَةُ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — أَبْوَابُ الْفَنِّ الثَّلَاثَةُ.",
    "The three doors of the second fann, in the order the book will walk them.",
    "İkinci fennin üç kapısı, kitabın yürüyeceği sırayla.")]})

# ----------- s4 — the dalala triad (restored)
S.append({"id": "s4", "translation": {
 "en": "And a word's indication is either of the whole of what it was coined for, or of a part of it, or of something outside it. (Restored.)",
 "tr": "Lafzın delâleti ya vaz' olunduğu şeyin tamamına, ya bir cüz'üne, ya da onun dışındaki bir şeyedir. (Geri yazılmıştır.)"},
 "tokens": [
  tok("وَدَلَالَةُ","dalala","noun",[B,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَدَلَالَةُ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«and the indication of» — the mubtada.",
      "«ve delâleti» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("دَلَالَةُ","dalala","noun")]),
  tok("اللَّفْظِ","lafz","noun",[B],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«a word» —",
      "«lafzın» —"),
  tok("إِمَّا","imma","part",[B],
      "حَرْفُ تَفْصِيلٍ.",
      "«either» — the particle that opens a division.",
      "«ya» — bir taksimi açan harf."),
  tok("عَلَى","ala","part",[B,"huruf-jarr"],
      "حَرْفُ جَرٍّ، وَشِبْهُ الْجُمْلَةِ خَبَرٌ.",
      "«of» — the jarr phrase is the khabar.",
      "«-e» — câr-mecrûr haberdir."),
  tok("تَمَامِ","tamam","noun",[B],
      "مَجْرُورٌ بِعَلَى وَهُوَ مُضَافٌ.",
      "«the whole of» —",
      "«tamamına» —"),
  tok("مَا","ma-mawsula","pron",[B,"ism-mawsul"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«what» —",
      "«şey» —"),
  tok("وُضِعَ","wadaa","verb",[B,"naib-al-fail","mithal-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةٌ.",
      "«it was coined» — the passive of وَضَعَ: the wadʿ, the assignment of a word to a meaning.",
      "«vaz' olundu» — وَضَعَ'nin meçhûlü: vaz', lafzın bir mânâya tahsisi."),
  tok("لَهُ","li","part",[B,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِوُضِعَ.",
      "«for» —",
      "«-e» —",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("أَوْ","aw","conj",[B,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.",
      "«or» —",
      "«ya» —"),
  tok("عَلَى","ala","part",[B,"huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«of» —",
      "«-e» —"),
  tok("جُزْئِهِ","juz","noun",[B],
      "مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«a part of it» —",
      "«cüz'üne» —",
      segments=[seg("جُزْئِ","juz","noun"), seg("هِ","pron-3ms","pron")]),
  tok("أَوْ","aw","conj",[B,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.",
      "«or» —",
      "«ya da» —"),
  tok("عَلَى","ala","part",[B,"huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«of» —",
      "«-e» —"),
  tok("خَارِجٍ","kharij","noun",[B,"ism-fail"],
      "مَجْرُورٌ — اسْمُ فَاعِلٍ.",
      "«something outside» —",
      "«dışındaki bir şeye» —"),
  tok("عَنْهُ","an","part",[B,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِخَارِجٍ.",
      "«it» —",
      "«ondan» —",
      punct=".",
      segments=[seg("عَنْ","an","part"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("وَدَلَالَةُ اللَّفْظِ إِمَّا عَلَى تَمَامِ مَا وُضِعَ لَهُ أَوْ عَلَى جُزْئِهِ أَوْ عَلَى خَارِجٍ عَنْهُ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا شِبْهُ جُمْلَةٍ — التَّقْسِيمُ الثُّلَاثِيُّ.",
    "The three-way division on which the whole science rests.",
    "Bütün ilmin üstüne oturduğu üçlü taksim.")]})

# ----------- s5 (restored)
S.append({"id": "s5", "translation": {
 "en": "The first is called wadʿiyya, the other two ʿaqliyya. (Restored.)",
 "tr": "İlkine vaz'iyye, öteki ikisine akliyye denir. (Geri yazılmıştır.)"},
 "tokens": [
  tok("وَالْأُولَى","ula-first","noun",[B,"mubtada-khabar","ism-maqsur-manqus"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْأُولَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«and the first» — the mubtada, a maqsur.",
      "«ve ilki» — mübtedâ, maksûr.",
      segments=[seg("وَ","wa","conj"), seg("الْأُولَى","ula-first","noun")]),
  tok("وَضْعِيَّةٌ","wadiyya","noun",[B,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى الْوَضْعِ.",
      "«coinage-borne» — a nisba to the wadʿ.",
      "«vaz'iyye» — vaz'a nispet.",
      punct="،"),
  tok("وَالْأُخْرَيَانِ","ukhra","noun",[B,"mubtada-khabar","al-muthanna"],
      "الْوَاوُ عَاطِفَةٌ، وَالْأُخْرَيَانِ مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.",
      "«and the other two» — the dual of أُخْرَى, raf' in the alif.",
      "«öteki ikisi» — أُخْرَى'nın tesniyesi; elif ile merfû.",
      segments=[seg("وَ","wa","conj"), seg("الْأُخْرَيَانِ","ukhra","noun")]),
  tok("عَقْلِيَّتَانِ","aqli","noun",[B,"mubtada-khabar","al-muthanna"],
      "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.",
      "«reason-borne» — the mind supplies the part and the concomitant.",
      "«akliyye» — cüz'ü ve lâzımı akıl verir.",
      punct=".")],
 "jumal": [
  J("وَالْأُولَى وَضْعِيَّةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ — الْمُطَابَقَةُ وَحْدَهَا مِنَ الْوَضْعِ.",
    "Only the first indication is the coinage's own.",
    "Yalnız ilk delâlet vaz'ın öz malıdır."),
  J("وَالْأُخْرَيَانِ عَقْلِيَّتَانِ",
    "مَعْطُوفَةٌ — وَبِهِمَا يَقَعُ الْإِيرَادُ بِطُرُقٍ مُخْتَلِفَةٍ.",
    "And through these two the «different roads» become possible at all.",
    "Ve «farklı yollar» ancak bu ikisiyle mümkün olur.")]})

# ----------- s6 (restored)
S.append({"id": "s6", "translation": {
 "en": "And the first is named mutabaqa, the second tadammun, the third iltizam. (Restored.)",
 "tr": "İlkine mutâbakat, ikincisine tazammun, üçüncüsüne iltizam adı verilir. (Geri yazılmıştır.)"},
 "tokens": [
  tok("وَتُسَمَّى","samma","verb",[B,"naib-al-fail","form-ii-verbs","naqis-verbs","mafulayn"],
      "الْوَاوُ عَاطِفَةٌ، وَتُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — نَاقِصٌ.",
      "«is named» — Form II's passive on a naqis root; its first object becomes the deputy doer.",
      "«adlandırılır» — nâkıs kökte II. bâbın meçhûlü; ilk mef'ûlü nâib-i fâil olur.",
      segments=[seg("وَ","wa","conj"), seg("تُسَمَّى","samma","verb")]),
  tok("الْأُولَى","ula-first","noun",[B,"naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.",
      "«the first» — the deputy doer.",
      "«ilki» — nâib-i fâil."),
  tok("مُطَابَقَةً","mutabaqa","noun",[B,"mafulayn"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.",
      "«mutabaqa» — the second object of سَمَّى: the name given.",
      "«mutâbakat» — سَمَّى'nın ikinci mef'ûlü: verilen ad."),
  tok("وَالثَّانِيَةُ","thaniya","noun",[B,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالثَّانِيَةُ مَعْطُوفٌ عَلَى نَائِبِ الْفَاعِلِ مَرْفُوعٌ.",
      "«and the second» —",
      "«ve ikincisi» —",
      segments=[seg("وَ","wa","conj"), seg("الثَّانِيَةُ","thaniya","noun")]),
  tok("تَضَمُّنًا","tadammun","noun",[B,"mafulayn"],
      "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ تَضَمَّنَ.",
      "«tadammun» — inclusion: the part inside the whole.",
      "«tazammun» — kapsama: bütünün içindeki parça."),
  tok("وَالثَّالِثَةُ","thalitha","noun",[B,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثَةُ مَعْطُوفٌ مَرْفُوعٌ.",
      "«and the third» —",
      "«ve üçüncüsü» —",
      segments=[seg("وَ","wa","conj"), seg("الثَّالِثَةُ","thalitha","noun")]),
  tok("الْتِزَامًا","iltizam","noun",[B,"mafulayn","form-viii-verbs"],
      "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ الْتَزَمَ.",
      "«iltizam» — concomitance: what the mind cannot help attaching.",
      "«iltizam» — lüzum: aklın bağlamadan edemediği şey.",
      punct=".")],
 "jumal": [
  J("وَتُسَمَّى الْأُولَى مُطَابَقَةً",
    "جُمْلَةٌ فِعْلِيَّةٌ مَجْهُولَةٌ — الْمَفْعُولُ الثَّانِي بَاقٍ عَلَى نَصْبِهِ.",
    "A passive of a two-object verb: the first object turns deputy doer, the second keeps its nasb.",
    "İki mef'ûllü fiilin meçhûlü: ilk mef'ûl nâib-i fâil olur, ikincisi nasbını korur.")]})

# ----------- s7 — the definition of tashbih
S.append({"id": "s7", "translation": {
 "en": "TASHBIH is the indication that one thing shares another thing in a meaning.",
 "tr": "TEŞBİH, bir şeyin başka bir şeye bir mânâda ortak olduğuna delâlettir."},
 "tokens": [
  tok("التَّشْبِيهُ","tashbih","noun",[A,B,"mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "«tashbih» — the mubtada: the thing defined.",
      "«teşbih» — mübtedâ: tarif edilen."),
  tok("الدَّلَالَةُ","dalala","noun",[A,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«the indication» — the genus of the definition: tashbih is a POINTING, not a saying.",
      "«delâlet» — tarifin cinsi: teşbih bir SÖYLEME değil, bir GÖSTERMEDİR."),
  tok("عَلَى","ala","part",[A,"huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِالدَّلَالَةِ.",
      "«that» —",
      "«-e» —"),
  tok("مُشَارَكَةِ","musharaka","noun",[A,"masdar","form-iii-verbs"],
      "مَجْرُورٌ بِعَلَى وَهُوَ مُضَافٌ — مَصْدَرُ شَارَكَ.",
      "«the sharing of» — Form III's masdar: two parties in one act.",
      "«ortaklığına» — III. bâbın masdarı: bir işte iki taraf."),
  tok("أَمْرٍ","amr","noun",[A],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — هُوَ الْمُشَبَّهُ.",
      "«a thing» — the MUSHABBAH, the definition's first rukn.",
      "«bir şeyin» — MÜŞEBBEH, tarifin ilk rüknü."),
  tok("لِأَمْرٍ","amr","noun",[A,"huruf-jarr"],
      "اللَّامُ جَارَّةٌ، وَأَمْرٍ مَجْرُورٌ — هُوَ الْمُشَبَّهُ بِهِ.",
      "«another thing» — the MUSHABBAH BIHI, the second rukn, behind its lam.",
      "«başka bir şeye» — MÜŞEBBEHÜN BİH, ikinci rükün; lâmın ardında.",
      segments=[seg("لِ","li","part"), seg("أَمْرٍ","amr","noun")]),
  tok("فِي","fi","part",[A,"huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«-de» —"),
  tok("مَعْنًى","mana","noun",[A,"ism-maqsur-manqus"],
      "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ — هُوَ وَجْهُ الشَّبَهِ.",
      "«a meaning» — the WAJH AL-SHABAH, the third rukn: the meaning the two share.",
      "«bir mânâda» — VECH-İ ŞEBEH, üçüncü rükün: ikisinin paylaştığı mânâ.",
      punct=".")],
 "jumal": [
  J("التَّشْبِيهُ الدَّلَالَةُ عَلَى مُشَارَكَةِ أَمْرٍ لِأَمْرٍ فِي مَعْنًى",
    "جُمْلَةٌ اسْمِيَّةٌ — وَفِي التَّعْرِيفِ ثَلَاثَةُ أَرْكَانٍ، وَالرَّابِعُ الْأَدَاةُ.",
    "Three arkan hide in the definition itself; the fourth, the adat, is the DALALA's own instrument.",
    "Üç rükün tarifin içinde saklıdır; dördüncüsü, edat, DELÂLETİN kendi aracıdır.")]})

# ----------- s8 — زَيْدٌ أَسَدٌ
S.append({"id": "s8", "translation": {
 "en": "Zayd is a lion — the adat and the wajh both dropped, and still a tashbih by the definition.",
 "tr": "Zeyd bir aslandır — edat da vech de düşmüş; tarife göre yine teşbih."},
 "tashbih": {"mushabbah": [0], "adat": None, "bihi": [1], "wajh": [], "kind": "baligh"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",[A,"mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — هُوَ الْمُشَبَّهُ.",
      "«Zayd» — the mubtada and the mushabbah.",
      "«Zeyd» — mübtedâ ve müşebbeh."),
  tok("أَسَدٌ","asad","noun",[A,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ — هُوَ الْمُشَبَّهُ بِهِ، وَالْأَدَاةُ وَوَجْهُ الشَّبَهِ مَحْذُوفَانِ.",
      "«a lion» — the khabar and the mushabbah bihi; no كَ, no «in courage»: the BALIGH shape.",
      "«bir aslan» — haber ve müşebbehün bih; ne كَ ne «cesarette»: BELÎĞ şekil.",
      punct=".")],
 "jumal": [
  J("زَيْدٌ أَسَدٌ",
    "جُمْلَةٌ اسْمِيَّةٌ — تَشْبِيهٌ بَلِيغٌ: حُذِفَتِ الْأَدَاةُ وَالْوَجْهُ.",
    "A tashbih baligh: the two ends stand as if one thing.",
    "Teşbih-i belîğ: iki taraf tek şeymiş gibi durur.")]})

# ----------- s9 — 2:18
S.append({"id": "s9", "translation": {
 "en": "Deaf, dumb, blind (2:18) — the adat, the wajh AND the mushabbah dropped; still inside the definition.",
 "tr": "Sağırdırlar, dilsizdirler, kördürler (2:18) — edat, vech VE müşebbeh düşmüş; yine tarifin içinde."},
 "tokens": [
  tok("صُمٌّ","summ","noun",[A,"mubtada-khabar","sifa-mushabbaha"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ مَرْفُوعٌ: هُمْ صُمٌّ — جَمْعُ أَصَمَّ.",
      "«deaf» — the khabar of an unspoken «they»: the mushabbah itself is dropped.",
      "«sağırdırlar» — söylenmeyen «onlar»ın haberi: müşebbehin kendisi düşmüş."),
  tok("بُكْمٌ","bukm","noun",[A,"sifa-mushabbaha"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ — جَمْعُ أَبْكَمَ.",
      "«dumb» — a second khabar.",
      "«dilsizdirler» — ikinci haber."),
  tok("عُمْيٌ","umy","noun",[A,"sifa-mushabbaha"],
      "خَبَرٌ ثَالِثٌ مَرْفُوعٌ — جَمْعُ أَعْمَى.",
      "«blind» — a third; the three plurals of the أَفْعَل defect-adjectives on فُعْل.",
      "«kördürler» — üçüncüsü; أَفْعَل kusur sıfatlarının فُعْل vezninde üç cem'i.",
      punct=".")],
 "jumal": [
  J("صُمٌّ بُكْمٌ عُمْيٌ",
    "أَخْبَارٌ ثَلَاثَةٌ لِمُبْتَدَأٍ مَحْذُوفٍ — تَشْبِيهٌ حُذِفَ مِنْهُ الْمُشَبَّهُ وَالْأَدَاةُ وَالْوَجْهُ.",
    "Three khabars of a dropped mubtada: they are LIKE the deaf, the dumb, the blind — with three of the four arkan unspoken.",
    "Düşmüş bir mübtedânın üç haberi: sağırlar, dilsizler, körler GİBİDİRLER — dört rüknün üçü söylenmemiş.")]})

# ----------- s10 — the four arkan (restored)
S.append({"id": "s10", "translation": {
 "en": "And its arkan are four: the mushabbah, the mushabbah bihi, the wajh al-shabah and the adat of tashbih. (Restored from the source's question-and-answer.)",
 "tr": "Rükünleri dörttür: müşebbeh, müşebbehün bih, vech-i şebeh ve teşbih edatı. (Kaynağın soru-cevabından geri yazılmıştır.)"},
 "tokens": [
  tok("وَأَرْكَانُهُ","arkan","noun",[A,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَأَرْكَانُ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«and its pillars» —",
      "«ve rükünleri» —",
      segments=[seg("وَ","wa","conj"), seg("أَرْكَانُ","arkan","noun"), seg("هُ","pron-3ms","pron")]),
  tok("أَرْبَعَةٌ","arbaa","noun",[A,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«four» —",
      "«dörttür» —",
      punct=":"),
  tok("الْمُشَبَّهُ","mushabbah","noun",[A,"badal","ism-maful","form-ii-verbs"],
      "بَدَلٌ مِنْ أَرْبَعَةٍ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ شَبَّهَ.",
      "«the mushabbah» — a badal spelling out «four»; Form II's ism maf'ul: the thing LIKENED.",
      "«müşebbeh» — «dört»ü açan bedel; II. bâbın ism-i mef'ûlü: BENZETİLEN."),
  tok("وَالْمُشَبَّهُ","mushabbah","noun",[A,"atf-nasaq","ism-maful"],
      "الْوَاوُ عَاطِفَةٌ، وَالْمُشَبَّهُ مَعْطُوفٌ مَرْفُوعٌ.",
      "«and the mushabbah» —",
      "«ve müşebbeh» —",
      segments=[seg("وَ","wa","conj"), seg("الْمُشَبَّهُ","mushabbah","noun")]),
  tok("بِهِ","bi","part",[A,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْمُشَبَّهِ — وَبِهِ يَتِمُّ الِاسْمُ: الْمُشَبَّهُ بِهِ.",
      "«bihi» — the phrase completes the term: the thing likened TO.",
      "«bih» — öbek terimi tamamlar: KENDİSİNE benzetilen.",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("وَوَجْهُ","wajh","noun",[A,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَوَجْهُ مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«and the face of» —",
      "«ve vechi» —",
      segments=[seg("وَ","wa","conj"), seg("وَجْهُ","wajh","noun")]),
  tok("الشَّبَهِ","shabah","noun",[A],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the likeness» — the wajh al-shabah: the shared meaning.",
      "«benzerliğin» — vech-i şebeh: ortak mânâ."),
  tok("وَأَدَاةُ","adat","noun",[A,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَأَدَاةُ مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«and the tool of» —",
      "«ve edatı» —",
      segments=[seg("وَ","wa","conj"), seg("أَدَاةُ","adat","noun")]),
  tok("التَّشْبِيهِ","tashbih","noun",[A],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«likening» — كَ، كَأَنَّ، مِثْل، and the verbs of likening.",
      "«teşbihin» — كَ، كَأَنَّ، مِثْل ve benzetme fiilleri.",
      punct=".")],
 "jumal": [
  J("وَأَرْكَانُهُ أَرْبَعَةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ — وَمَا بَعْدَهَا بَدَلُ تَفْصِيلٍ.",
    "The count, then the four named as its badal.",
    "Sayı, sonra dördü bedel olarak adlandırılır.")]})

# ----------- s11-s18 — the tarafan
def liken(sid, en, tr, mush_tokens, bihi_tok, frame, jumal_ar, jumal_en, jumal_tr, tag_bihi=None):
    S.append({"id": sid, "translation": {"en": en, "tr": tr}, "tashbih": frame,
              "tokens": mush_tokens + [bihi_tok],
              "jumal": [J(" ".join(t["surface"]["full"] for t in mush_tokens + [bihi_tok]), jumal_ar, jumal_en, jumal_tr)]})
def ka(full, lex, en, tr, note_en, note_tr, punct="."):
    inner = full[2:] if full.startswith("كَ") else full[1:]
    return tok(full, lex, "noun", [A,"huruf-jarr"],
      "الْكَافُ لِلتَّشْبِيهِ جَارَّةٌ، وَمَا بَعْدَهَا مَجْرُورٌ — هُوَ الْمُشَبَّهُ بِهِ، وَشِبْهُ الْجُمْلَةِ خَبَرٌ.",
      f"«{en}» — the kaf of likening (the ADAT) with the mushabbah bihi; the phrase is the khabar. {note_en}",
      f"«{tr}» — teşbih kâfı (EDAT) ve müşebbehün bih; öbek haberdir. {note_tr}",
      punct=punct, segments=[seg("كَ","ka","part"), seg(inner, lex, "noun")])
def head(full, lex, en, tr, extra=None):
    segs = None
    if full.endswith("هُ"): segs = [seg(full[:-2], lex, "noun"), seg("هُ","pron-3ms","pron")]
    return tok(full, lex, "noun", [A,"mubtada-khabar"] + (extra or []),
      "مُبْتَدَأٌ مَرْفُوعٌ" + (" وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ" if segs else "") + " — هُوَ الْمُشَبَّهُ.",
      f"«{en}» — the mubtada and the MUSHABBAH.",
      f"«{tr}» — mübtedâ ve MÜŞEBBEH.", segments=segs)
def sifa(full, lex, en, tr):
    return tok(full, lex, "noun", [A,"naat-sifa","sifa-mushabbaha"],
      "صِفَةٌ لِلْمُبْتَدَأِ مَرْفُوعَةٌ — دَاخِلَةٌ فِي الْمُشَبَّهِ.",
      f"«{en}» — a sifa of the mubtada, part of the mushabbah.",
      f"«{tr}» — mübtedânın sıfatı; müşebbehin içinde.")
F = lambda m, a, b: {"mushabbah": m, "adat": a, "bihi": b, "wajh": [], "kind": "mursal-mujmal"}
liken("s11", "His cheek is like the rose — seen: both ends sensory (sight).", "Yanağı gül gibi — görülen: iki taraf da hissî (görme).",
      [head("خَدُّهُ","khadd","his cheek","yanağı")], ka("كَالْوَرْدِ","ward","like the rose","gül gibi","Redness is the unspoken wajh: MUJMAL.","Kızıllık söylenmeyen vechtir: MÜCMEL."),
      F([0],1,[1]), "تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ — طَرَفَاهُ حِسِّيَّانِ بِالْبَصَرِ.", "Mursal (the kaf spoken), mujmal (the wajh unspoken); both ends things seen.", "Mürsel (kâf söylenmiş), mücmel (vech söylenmemiş); iki taraf da görülen şey.")
liken("s12", "His weak voice is like a whisper — heard.", "Zayıf sesi fısıltı gibi — işitilen.",
      [head("صَوْتُهُ","sawt","his voice","sesi"), sifa("الضَّعِيفُ","daif","weak","zayıf")], ka("كَالْهَمْسِ","hams","like a whisper","fısıltı gibi","Faintness is the wajh.","Hafiflik vechtir."),
      F([0,1],2,[2]), "تَشْبِيهٌ حِسِّيٌّ بِالسَّمْعِ — وَالصِّفَةُ مِنَ الْمُشَبَّهِ.", "Both ends heard; the sifa belongs to the mushabbah, not to the likeness.", "İki taraf da işitilen; sıfat benzerliğe değil müşebbehe aittir.")
liken("s13", "The scent of his mouth is like ambergris — smelled.", "Ağzının kokusu amber gibi — koklanan.",
      [head("نَكْهَتُهُ","nakha","the scent of his mouth","ağzının kokusu")], ka("كَالْعَنْبَرِ","anbar","like ambergris","amber gibi","Fragrance is the wajh.","Güzel koku vechtir."),
      F([0],1,[1]), "تَشْبِيهٌ حِسِّيٌّ بِالشَّمِّ.", "Both ends smelled.", "İki taraf da koklanan.")
liken("s14", "His saliva is like wine — tasted.", "Tükürüğü şarap gibi — tadılan.",
      [head("رِيقُهُ","riq","his saliva","tükürüğü")], ka("كَالْخَمْرِ","khamr","like wine","şarap gibi","Sweetness is the wajh.","Lezzet vechtir."),
      F([0],1,[1]), "تَشْبِيهٌ حِسِّيٌّ بِالذَّوْقِ.", "Both ends tasted.", "İki taraf da tadılan.")
liken("s15", "His soft skin is like silk — touched.", "Yumuşak teni ipek gibi — dokunulan.",
      [head("جِلْدُهُ","jild","his skin","teni"), sifa("النَّاعِمُ","naim-soft","soft","yumuşak")], ka("كَالْحَرِيرِ","harir","like silk","ipek gibi","Softness is the wajh — and it is spoken on the mushabbah's sifa, yet the tashbih stays MUJMAL: the wajh is not stated AS the shared meaning.","Yumuşaklık vechtir — müşebbehin sıfatında söylenmiştir, ama teşbih MÜCMEL kalır: vech, ORTAK mânâ olarak zikredilmemiştir."),
      F([0,1],2,[2]), "تَشْبِيهٌ حِسِّيٌّ بِاللَّمْسِ — الْحَوَاسُّ الْخَمْسُ تَمَّتْ.", "Both ends touched: the five senses complete.", "İki taraf da dokunulan: beş duyu tamamlandı.")
liken("s16", "Knowledge is like life — both ends rational (ʿaqli).", "İlim hayat gibi — iki taraf da aklî.",
      [head("الْعِلْمُ","ilm","knowledge","ilim")], ka("كَالْحَيَاةِ","hayat","like life","hayat gibi","Neither end is grasped by a sense.","İki taraf da bir duyu ile idrak edilmez."),
      F([0],1,[1]), "تَشْبِيهٌ عَقْلِيٌّ — لَا يُدْرَكُ طَرَفَاهُ بِحَاسَّةٍ.", "Both ends rational.", "İki taraf da aklî.")
liken("s17", "Death is like a beast of prey — a rational mushabbah, a sensory mushabbah bihi.", "Ölüm yırtıcı hayvan gibi — aklî müşebbeh, hissî müşebbehün bih.",
      [head("الْمَنِيَّةُ","maniyya","death","ölüm")], ka("كَالسَّبُعِ","sabu","like a beast of prey","yırtıcı hayvan gibi","The two ends DIFFER in kind.","İki taraf tür bakımından FARKLIDIR."),
      F([0],1,[1]), "تَشْبِيهٌ مُخْتَلِفُ الطَّرَفَيْنِ — الْمُشَبَّهُ عَقْلِيٌّ وَالْمُشَبَّهُ بِهِ حِسِّيٌّ.", "Mixed ends: death is grasped by the mind, the beast by the eye.", "Karışık taraflar: ölüm akılla, yırtıcı gözle idrak edilir.")
liken("s18", "Perfume is like a generous character — a sensory mushabbah, a rational mushabbah bihi.", "Güzel koku kerem sahibi bir huy gibi — hissî müşebbeh, aklî müşebbehün bih.",
      [head("الْعِطْرُ","itr","perfume","güzel koku")], ka("كَخُلُقٍ","khuluq","like a character","bir huy gibi","", "", punct=None),
      {"mushabbah": [0], "adat": 1, "bihi": [1, 2], "wajh": [], "kind": "mursal-mujmal"},
      "تَشْبِيهٌ مُخْتَلِفُ الطَّرَفَيْنِ عَكْسُ الَّذِي قَبْلَهُ — وَالصِّفَةُ مِنَ الْمُشَبَّهِ بِهِ.", "The mirror of the last: the perfume is smelled, the character is thought; the sifa belongs to the bihi.", "Öncekinin aynası: koku koklanır, huy düşünülür; sıfat müşebbehün bihe aittir.")
S[-1]["tokens"].append(tok("كَرِيمٍ","karim","noun",[A,"naat-sifa","sifa-mushabbaha"],
      "صِفَةٌ لِخُلُقٍ مَجْرُورَةٌ — دَاخِلَةٌ فِي الْمُشَبَّهِ بِهِ.",
      "«generous» — the sifa of خُلُق, inside the mushabbah bihi.",
      "«kerem sahibi» — خُلُق'un sıfatı; müşebbehün bihin içinde.", punct="."))
S[-1]["jumal"][0]["text"] = "الْعِطْرُ كَخُلُقٍ كَرِيمٍ"

# ----------- s19-s20 — the khayali bayt
S.append({"id": "s19", "translation": {
 "en": "And as if the red of the anemones, when they dip or rise, —",
 "tr": "Kırmızı lâleler, aşağı yukarı salındığında sanki —"},
 "tashbih": {"mushabbah": [1, 2], "adat": 0, "bihi": [], "wajh": [], "kind": "mursal-mujmal"},
 "tokens": [
  tok("وَكَأَنَّ","ka-anna","part",[A,"inna-wa-akhawatuha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ — هُوَ الْأَدَاةُ.",
      "«and as if» — كَأَنَّ, an inna-sister and the ADAT: its ism is the mushabbah, its khabar the bihi.",
      "«ve sanki» — كَأَنَّ, inne kardeşi ve EDAT: ismi müşebbeh, haberi müşebbehün bih.",
      segments=[seg("وَ","wa","conj"), seg("كَأَنَّ","ka-anna","part")]),
  tok("مُحْمَرَّ","muhmarr","noun",[A,"inna-wa-akhawatuha","ism-fail","doubled-verbs"],
      "اسْمُ كَأَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ مِنِ احْمَرَّ.",
      "«the red of» — كَأَنَّ's ism, the mushabbah; the ism fa'il of اِحْمَرَّ (Form IX).",
      "«kızılı» — كَأَنَّ'nin ismi, müşebbeh; اِحْمَرَّ'nin (IX. bâb) ism-i fâili."),
  tok("الشَّقِيقِ","shaqiq","noun",[A],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — شَقَائِقُ النُّعْمَانِ.",
      "«the anemones» — the mushabbah is seen: sensory.",
      "«lâlelerin» — müşebbeh görülür: hissî."),
  tok("إِذَا","idha","part",[A,"idha-shartiyya","maful-fih"],
      "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مُتَعَلِّقٌ بِخَبَرِ كَأَنَّ الْآتِي.",
      "«when» — hanging on كَأَنَّ's khabar, which the next line brings.",
      "«-dığında» — sonraki mısraın getireceği كَأَنَّ haberine bağlı."),
  tok("تَصَوَّبَ","tasawwaba","verb",[A,"form-v-verbs"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا.",
      "«they dip» — Form V.",
      "«aşağı salınır» — V. bâb."),
  tok("أَوْ","aw","conj",[A,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.",
      "«or» —",
      "«yahut» —"),
  tok("تَصَعَّدْ","tasaada","verb",[A,"form-v-verbs"],
      "فِعْلٌ مَاضٍ مَعْطُوفٌ — سُكِّنَ آخِرُهُ لِلْقَافِيَةِ.",
      "«rise» — Form V; its final letter quiesced for the rhyme, as the source prints it.",
      "«yukarı salınır» — V. bâb; sonu kafiye için sükûnlu, kaynağın bastığı gibi.")],
 "jumal": [
  J("وَكَأَنَّ مُحْمَرَّ الشَّقِيقِ",
    "كَأَنَّ وَاسْمُهَا — الْمُشَبَّهُ، وَالْخَبَرُ فِي الْمِصْرَاعِ الثَّانِي.",
    "The adat and the mushabbah; the mushabbah bihi waits in the second hemistich.",
    "Edat ve müşebbeh; müşebbehün bih ikinci mısrada bekler.")]})
S.append({"id": "s20", "translation": {
 "en": "— are banners of ruby unfurled upon lances of chrysolite. The mushabbah bihi is KHAYALI: never seen assembled, but assembled from things seen.",
 "tr": "— zeberced mızraklar üstüne açılmış yakut sancaklardır. Müşebbehün bih HAYÂLÎDİR: toplu hâlde hiç görülmemiş, ama görülen şeylerden toplanmış."},
 "tokens": [
  tok("أَعْلَامُ","alam","noun",[A,"inna-wa-akhawatuha"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ وَهُوَ مُضَافٌ — هُوَ الْمُشَبَّهُ بِهِ.",
      "«banners of» — كَأَنَّ's khabar and the mushabbah bihi.",
      "«sancakları» — كَأَنَّ'nin haberi ve müşebbehün bih."),
  tok("يَاقُوتٍ","yaqut","noun",[A],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«ruby» —",
      "«yakut» —"),
  tok("نُشِرْنَ","nashara","verb",[A,"naib-al-fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنُونُ النِّسْوَةِ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ صِفَةٌ لِأَعْلَامٍ.",
      "«unfurled» — the passive on the nun of the feminine plural; the clause is the sifa of the banners.",
      "«açılmış» — nûn-i nisve üzerine meçhûl; cümle sancakların sıfatı."),
  tok("عَلَى","ala","part",[A,"huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«upon» —",
      "«üstüne» —"),
  tok("رِمَاحٍ","rimah","noun",[A],
      "مَجْرُورٌ بِعَلَى — جَمْعُ رُمْحٍ.",
      "«lances» —",
      "«mızraklar» —"),
  tok("مِنْ","min","part",[A,"huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«of» —",
      "«-den» —"),
  tok("زَبَرْجَدْ","zabarjad","noun",[A],
      "مَجْرُورٌ — سُكِّنَ آخِرُهُ لِلْقَافِيَةِ.",
      "«chrysolite» — its ending quiesced for the rhyme, as printed.",
      "«zeberced» — sonu kafiye için sükûnlu, basıldığı gibi.",
      punct=".")],
 "jumal": [
  J("أَعْلَامُ يَاقُوتٍ نُشِرْنَ عَلَى رِمَاحٍ مِنْ زَبَرْجَدْ",
    "خَبَرُ كَأَنَّ وَصِفَتُهُ — الْمُشَبَّهُ بِهِ الْخَيَالِيُّ.",
    "The khabar with its clause-sifa: the imagined picture, built from rubies, banners and green lances each seen apart.",
    "Cümle-sıfatlı haber: her biri ayrı ayrı görülen yakut, sancak ve yeşil mızraklardan kurulmuş hayâlî tablo.")]})

# ----------- s21-s22 — Imru' al-Qays: the wahmi bayt
S.append({"id": "s21", "translation": {
 "en": "Will he kill me, while the Mashrafi sword shares my bed —",
 "tr": "Meşrefî kılıç yatak arkadaşım iken o beni öldürecek mi —"},
 "tokens": [
  tok("أَيَقْتُلُنِي","qatala","verb",[A,"al-istifham","ya-al-mutakallim"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَيَقْتُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«will he kill me?» — the hamza of denial; the wiqaya nun guards the verb before the speaker's ya.",
      "«beni öldürecek mi?» — inkâr hemzesi; mütekellim yâsından önce vikâye nûnu fiili korur.",
      segments=[seg("أَ","hamza-istifham","part"), seg("يَقْتُلُ","qatala","verb"), seg("نِي","pron-1s","pron")]),
  tok("وَالْمَشْرَفِيُّ","mashrafi","noun",[A,"hal","mubtada-khabar"],
      "الْوَاوُ حَالِيَّةٌ، وَالْمَشْرَفِيُّ مُبْتَدَأٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى مَشَارِفِ الشَّامِ.",
      "«while the Mashrafi» — the waw of hal opens a nominal clause: the sword named for the Syrian borderlands.",
      "«Meşrefî iken» — hâl vâvı isim cümlesi açar: Şam sınır boylarına nispetle anılan kılıç.",
      segments=[seg("وَ","wa","conj"), seg("الْمَشْرَفِيُّ","mashrafi","noun")]),
  tok("مُضَاجِعِي","mudaji","noun",[A,"mubtada-khabar","ism-fail","form-iii-verbs","ya-al-mutakallim"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.",
      "«my bedfellow» — Form III's ism fa'il with the speaker's ya: the sword lies beside him.",
      "«yatak arkadaşım» — mütekellim yâlı III. bâb ism-i fâili: kılıç yanında yatar.")],
 "jumal": [
  J("وَالْمَشْرَفِيُّ مُضَاجِعِي",
    "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The hal clause: HOW could he — with a sword at my side?",
    "Hâl cümlesi: NASIL öldürsün — yanımda kılıç varken?")]})
S.append({"id": "s22", "translation": {
 "en": "— and sharpened blue-grey [arrowheads], like the fangs of ghouls. The mushabbah bihi is WAHMI: no sense has met a ghoul's fang, yet had it been met, the eye would have met it.",
 "tr": "— ve bilenmiş mavimsi [temrenler], gulyabani dişleri gibi. Müşebbehün bih VEHMÎDİR: gulyabani dişini hiçbir duyu görmemiştir; görülseydi göz görürdü."},
 "tashbih": {"mushabbah": [0, 1], "adat": 2, "bihi": [2, 3], "wajh": [], "kind": "mursal-mujmal"},
 "tokens": [
  tok("وَمَسْنُونَةٌ","masnun","noun",[A,"atf-nasaq","ism-maful","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَمَسْنُونَةٌ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ: مَسْنُونَةٌ أَيْ نِصَالٌ مَسْنُونَةٌ.",
      "«and sharpened [blades]» — a second mubtada joined to the first; the noun (arrowheads) is left to the adjective.",
      "«ve bilenmiş [temrenler]» — ilkine atfedilen ikinci mübtedâ; isim (temrenler) sıfata bırakılmış.",
      segments=[seg("وَ","wa","conj"), seg("مَسْنُونَةٌ","masnun","noun")]),
  tok("زُرْقٌ","zurq","noun",[A,"naat-sifa","sifa-mushabbaha"],
      "صِفَةٌ مَرْفُوعَةٌ — جَمْعُ أَزْرَقَ عَلَى فُعْلٍ.",
      "«blue-grey» — the plural of أَزْرَق on فُعْل, a sifa; with the first it is the mushabbah.",
      "«mavimsi» — أَزْرَق'ın فُعْل veznindeki cem'i, sıfat; ilkiyle birlikte müşebbeh."),
  tok("كَأَنْيَابِ","nab","noun",[A,"huruf-jarr"],
      "الْكَافُ لِلتَّشْبِيهِ جَارَّةٌ، وَأَنْيَابِ مَجْرُورٌ وَهُوَ مُضَافٌ — جَمْعُ نَابٍ؛ وَشِبْهُ الْجُمْلَةِ خَبَرٌ.",
      "«like the fangs of» — the kaf of likening (the ADAT) and the mushabbah bihi's head.",
      "«dişleri gibi» — teşbih kâfı (EDAT) ve müşebbehün bihin başı.",
      segments=[seg("كَ","ka","part"), seg("أَنْيَابِ","nab","noun")]),
  tok("أَغْوَالٍ","ghul","noun",[A],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ غُولٍ.",
      "«ghouls» — the mushabbah bihi completed: a thing no sense has met — WAHMI.",
      "«gulyabanilerin» — müşebbehün bih tamamlandı: hiçbir duyunun görmediği şey — VEHMÎ.",
      punct=".")],
 "jumal": [
  J("وَمَسْنُونَةٌ زُرْقٌ كَأَنْيَابِ أَغْوَالٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْحَالِ — تَشْبِيهٌ مُشَبَّهُهُ حِسِّيٌّ وَمُشَبَّهُهُ بِهِ وَهْمِيٌّ.",
    "Joined to the hal clause: a sensory mushabbah (the blades) likened to a wahmi bihi (the fangs) — and the wahmi counts as rational.",
    "Hâl cümlesine atıf: hissî müşebbeh (temrenler), vehmî müşebbehün bihe (dişler) benzetilmiş — vehmî, aklî sayılır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "irad": g("إِيرَاد", "و ر د", "noun", "bringing, adducing (masdar of أَوْرَدَ)", "îrâd, getirme (أَوْرَدَ'nin masdarı)", 5),
 "mawdu": g("مَوْضُوع", "و ض ع", "noun", "subject (of a science); ism maf'ul of وَضَعَ", "mevzu; وَضَعَ'nin ism-i mef'ûlü", 3),
 "tashbih": g("تَشْبِيه", "ش ب ه", "noun", "tashbih: likening — the first door of bayan", "teşbih: benzetme — beyânın ilk kapısı", 4),
 "tamam": g("تَمَام", "ت م م", "noun", "the whole, entirety", "tamam, bütün", 3),
 "kharij": g("خَارِج", "خ ر ج", "noun", "outside, external (ism fa'il)", "hâriç, dış (ism-i fâil)", 3),
 "ula-first": g("الْأُولَى", "أ و ل", "noun", "the first (feminine of أَوَّل)", "ilki (أَوَّل'in müennesi)", 2),
 "wadiyya": g("وَضْعِيَّة", "و ض ع", "noun", "coinage-borne (nisba to the wadʿ)", "vaz'iyye (vaz'a nispet)", 5),
 "thaniya": g("الثَّانِيَة", "ث ن ي", "noun", "the second (feminine)", "ikincisi (müennes)", 2),
 "thalitha": g("الثَّالِثَة", "ث ل ث", "noun", "the third (feminine)", "üçüncüsü (müennes)", 2),
 "tadammun": g("تَضَمُّن", "ض م ن", "noun", "inclusion, implication of a part (masdar of تَضَمَّنَ)", "tazammun (تَضَمَّنَ'nin masdarı)", 5),
 "iltizam": g("الْتِزَام", "ل ز م", "noun", "concomitance (masdar of الْتَزَمَ)", "iltizam, lüzum (الْتَزَمَ'nin masdarı)", 5),
 "musharaka": g("مُشَارَكَة", "ش ر ك", "noun", "sharing, partnership (masdar of شَارَكَ)", "müşâreket, ortaklık (شَارَكَ'nin masdarı)", 4),
 "asad": g("أَسَد", "أ س د", "noun", "lion", "aslan", 1, plural="أُسُود"),
 "summ": g("صُمّ", "ص م م", "noun", "deaf (pl. of أَصَمّ, adjective)", "sağırlar (أَصَمّ'in cem'i, sıfat)", 3),
 "bukm": g("بُكْم", "ب ك م", "noun", "dumb (pl. of أَبْكَم, adjective)", "dilsizler (أَبْكَم'in cem'i, sıfat)", 3),
 "umy": g("عُمْي", "ع م ي", "noun", "blind (pl. of أَعْمَى, adjective)", "körler (أَعْمَى'nın cem'i, sıfat)", 3),
 "mushabbah": g("مُشَبَّه", "ش ب ه", "noun", "the mushabbah — what is likened (ism maf'ul of شَبَّهَ)", "müşebbeh — benzetilen (شَبَّهَ'nin ism-i mef'ûlü)", 4),
 "shabah": g("شَبَه", "ش ب ه", "noun", "likeness, resemblance", "benzerlik", 3),
 "adat": g("أَدَاة", "أ د و", "noun", "tool, instrument; particle", "edat, âlet", 3, plural="أَدَوَات"),
 "khadd": g("خَدّ", "خ د د", "noun", "cheek", "yanak", 2, plural="خُدُود"),
 "ward": g("وَرْد", "و ر د", "noun", "rose(s)", "gül", 1),
 "sawt": g("صَوْت", "ص و ت", "noun", "voice, sound", "ses", 1, plural="أَصْوَات"),
 "daif": g("ضَعِيف", "ض ع ف", "noun", "weak (adjective)", "zayıf (sıfat)", 1),
 "hams": g("هَمْس", "ه م س", "noun", "whisper", "fısıltı", 3),
 "nakha": g("نَكْهَة", "ن ك ه", "noun", "the scent of the mouth, breath", "ağız kokusu, nefes", 5),
 "anbar": g("عَنْبَر", "ع ن ب ر", "noun", "ambergris", "amber", 4),
 "riq": g("رِيق", "ر ي ق", "noun", "saliva", "tükürük", 4),
 "jild": g("جِلْد", "ج ل د", "noun", "skin", "deri, ten", 2, plural="جُلُود"),
 "naim-soft": g("نَاعِم", "ن ع م", "noun", "soft, smooth (ism fa'il)", "yumuşak (ism-i fâil)", 3),
 "harir": g("حَرِير", "ح ر ر", "noun", "silk", "ipek", 2),
 "maniyya": g("مَنِيَّة", "م ن ي", "noun", "death, fate", "ölüm, ecel", 4, plural="مَنَايَا"),
 "sabu": g("سَبُع", "س ب ع", "noun", "beast of prey", "yırtıcı hayvan", 3, plural="سِبَاع"),
 "itr": g("عِطْر", "ع ط ر", "noun", "perfume", "güzel koku, ıtır", 3),
 "muhmarr": g("مُحْمَرّ", "ح م ر", "noun", "reddened, red (ism fa'il of اِحْمَرَّ, Form IX)", "kızarmış, kızıl (اِحْمَرَّ'nin ism-i fâili, IX. bâb)", 5),
 "shaqiq": g("شَقِيق", "ش ق ق", "noun", "the anemone (شَقَائِقُ النُّعْمَانِ)", "lâle, şakâyık", 5, plural="شَقَائِق"),
 "tasawwaba": g("تَصَوَّبَ", "ص و ب", "verb", "to descend, dip down", "aşağı inmek, sarkmak", 5, form="V"),
 "tasaada": g("تَصَعَّدَ", "ص ع د", "verb", "to rise, go up", "yukarı çıkmak", 5, form="V"),
 "yaqut": g("يَاقُوت", "ي ق ت", "noun", "ruby, sapphire", "yakut", 4),
 "rimah": g("رُمْح", "ر م ح", "noun", "lance, spear", "mızrak", 3, plural="رِمَاح"),
 "zabarjad": g("زَبَرْجَد", "ز ب ر ج د", "noun", "chrysolite, peridot", "zeberced", 5),
 "qatala": g("قَتَلَ", "ق ت ل", "verb", "to kill", "öldürmek", 1, form="I"),
 "mashrafi": g("مَشْرَفِيّ", "ش ر ف", "noun", "a Mashrafi sword (nisba to the Syrian borderlands)", "Meşrefî kılıç (Şam sınır boylarına nispet)", 6),
 "mudaji": g("مُضَاجِع", "ض ج ع", "noun", "bedfellow (ism fa'il of ضَاجَعَ)", "yatak arkadaşı (ضَاجَعَ'nin ism-i fâili)", 5),
 "masnun": g("مَسْنُون", "س ن ن", "noun", "sharpened, whetted (ism maf'ul)", "bilenmiş (ism-i mef'ûl)", 5),
 "zurq": g("زُرْق", "ز ر ق", "noun", "blue-grey (pl. of أَزْرَق, adjective)", "mavimsi, gök (أَزْرَق'ın cem'i, sıfat)", 4),
 "ghul": g("غُول", "غ و ل", "noun", "ghoul", "gulyabani", 4, plural="أَغْوَال"),
 "wahid": copy_gloss("aqaid-ahl-al-sunna", "wahid"),
 "tariq": dict(copy_gloss("aqaid-ahl-al-sunna", "tariq"), plural="طُرُق"),
 "wuduh": copy_gloss("mukhtasar-al-manar", "wuduh"),
 "dalala": copy_gloss("mukhtasar-al-manar", "dalala"),
 "kinaya": copy_gloss("mukhtasar-al-manar", "kinaya"),
 "juz": copy_gloss("aqaid-ahl-al-sunna", "juz"),
 "arkan": copy_gloss("min-muqaddimat-al-maqsud", "arkan"),
 "arbaa": copy_gloss("mukhtasar-al-manar", "arbaa"),
 "khamr": copy_gloss("kitab-al-sulh", "khamr"),
 "khuluq": copy_gloss("wasiyyat-abi-hanifa-samti", "khuluq"),
 "karim": copy_gloss("bad-al-amali", "karim"),
 "nashara": copy_gloss("wasiyyat-abi-hanifa-l4", "nashara"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/46.json").write_text(
    json.dumps({"chapter": 46, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 46 for c in man["chapters"]):
    man["chapters"].append({"n": 46, "title": TITLE46})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.46.0"
ADD_EN = (" Chapter 46 opens Fann 2, ʿilm al-bayan (lines ~2955-3025, sahifa 102-104): s1-s2 the "
          "definition and s7 the definition of tashbih are the matn as the source prints it; s8 "
          "زَيْدٌ أَسَدٌ and s11-s18 the tarafan examples are the source's own; s9 is al-Baqara 2:18 "
          "(part), received Qur'anic text; s19-s20 the khayali bayt and s21-s22 Imru' al-Qays's bayt "
          "are as the source recites them, split at the hemistich, the rhyme sukun on تَصَعَّدْ and "
          "زَبَرْجَدْ kept as printed (the source writes اَغْوَالٍ with tanwin, written here أَغْوَالٍ). "
          "s3, s4-s6 and s10 are RESTORATIONS, not quotations: the source gives the subject, the "
          "three dalalat and the four arkan only in Ottoman-Turkish question-and-answer, and the "
          "Arabic restores them in the musannif's register; each is marked «restored» in its "
          "translation. Every likening carries an authored `tashbih` frame the engine is tested "
          "against.")
ADD_TR = (" Kırk altıncı bâb ikinci fenni, beyân ilmini açar (satır ~2955-3025, sahife 102-104): s1-s2 "
          "tarif ile s7 teşbih tarifi kaynağın bastığı matndır; s8 زَيْدٌ أَسَدٌ ve s11-s18 taraf örnekleri "
          "kaynağın kendi örnekleridir; s9 Bakara 2:18 (kısmen), mervî Kur'ân metni; s19-s20 hayâlî "
          "beyit ile s21-s22 İmruülkays'ın beyti kaynağın okuduğu şekliyle, mısra başından bölünmüş, "
          "تَصَعَّدْ ve زَبَرْجَدْ'deki kafiye sükûnu basıldığı gibi (kaynak اَغْوَالٍ yazar, burada "
          "أَغْوَالٍ). s3, s4-s6 ve s10 ALINTI DEĞİL GERİ YAZIMDIR: kaynak mevzuu, üç delâleti ve dört "
          "rüknü yalnız Osmanlıca soru-cevapla verir; Arapça onları musannifin üslûbunda geri yazar; "
          "her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Her benzetme, motorun sınandığı "
          "müellif eliyle yazılmış bir `tashbih` çerçevesi taşır.")
if "2955-3025" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
for k, v in GLOSS_ADD.items():
    gl["entries"].setdefault(k, v)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
V = mo["verbs"]
if "qatala" not in V:
    V["qatala"] = _sg.sound1("nasara", "قَتَل", "قْتُل", "اُقْتُل", "قَتْل", "قَاتِل",
                             "مَقْتُول", "قُتِلَ", "يُقْتَلُ")
if "tasawwaba" not in V:
    V["tasawwaba"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَصَوَّب", "تَصَوَّب", "تَصَوَّب",
                                 "تَصَوُّب", "مُتَصَوِّب", None)
if "tasaada" not in V:
    V["tasaada"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَصَعَّد", "تَصَعَّد", "تَصَعَّد",
                               "تَصَعُّد", "مُتَصَعِّد", None)
if "samma" not in V:
    V["samma"] = _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "سَمَّ", "سَمِّ", "i", "سَمِّ",
                                   "تَسْمِيَة", "مُسَمٍّ (الْمُسَمِّي)", "مُسَمًّى", "سُمِّيَ", "يُسَمَّى")
if "nashara" not in V:
    V["nashara"] = copy_morph("wasiyyat-abi-hanifa-l4", "nashara")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes 150-151
GR = ROOT / "content/grammar"
NOTE150 = {
 "id": "ilm-al-bayan",
 "title": {"ar": "عِلْمُ الْبَيَانِ — تَعْرِيفُهُ وَمَوْضُوعُهُ وَالدَّلَالَاتُ الثَّلَاثُ",
           "en": "ʿIlm al-bayan — its definition, its subject, and the three indications",
           "tr": "Beyân ilmi — tarifi, mevzuu ve üç delâlet"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الفنّ الثاني: علم البيان"],
 "question": {
  "en": ["Can ONE meaning be brought by several roads that differ in how clearly they point to it? The science of those roads is bayan.",
         "Does the word point to ALL it was coined for (mutabaqa), to a PART of it (tadammun), or to something OUTSIDE it that the mind attaches (iltizam)? Only the last two open different roads.",
         "Which door is being walked — tashbih, majaz or kinaya? Bayan has three, and the book walks them in that order."],
  "tr": ["BİR mânâ, ona delâletin açıklığında farklı olan birkaç yolla getirilebilir mi? O yolların ilmi beyândır.",
         "Lafız, vaz' olunduğu şeyin TAMAMINA mı (mutâbakat), bir CÜZ'ÜNE mi (tazammun), yoksa aklın bağladığı DIŞINDAKİ bir şeye mi (iltizam) delâlet ediyor? Yalnız son ikisi farklı yollar açar.",
         "Hangi kapıda yürünüyor — teşbih, mecaz, kinaye? Beyânın üç kapısı vardır; kitap onları bu sırayla yürür."]},
 "plain": {
  "en": "Maʿani asked whether a sentence fits its occasion. Bayan asks a narrower thing: given ONE meaning, how many ways can Arabic point at it, and which points more clearly? Only the mind-borne indications (part, concomitant) allow more than one road; hence three doors — tashbih, majaz, kinaya.",
  "tr": "Meânî, cümlenin makamına uyup uymadığını sordu. Beyân daha dar bir şey sorar: BİR mânâ verildiğinde Arapça ona kaç yoldan işaret edebilir ve hangisi daha açık gösterir? Yalnız akıl-taşımalı delâletler (cüz, lâzım) birden çok yola izin verir; bu yüzden üç kapı — teşbih, mecaz, kinaye."},
 "explanation": {
  "en": "The matn: وَهُوَ عِلْمٌ يُعْرَفُ بِهِ إِيرَادُ الْمَعْنَى الْوَاحِدِ بِطُرُقٍ مُخْتَلِفَةٍ فِي وُضُوحِ الدَّلَالَةِ عَلَيْهِ — «a science by which is known the bringing of ONE meaning by roads that DIFFER in the clarity of their indication of it». Three restrictions carry the definition: one meaning (not several), several roads (not one), roads that differ in CLARITY (not in wording alone). The commentary then asks why such roads exist at all, and answers through the DALALA: a word indicates either the whole of what it was coined for, or a part of it, or something outside it — the first is wadʿiyya (coinage-borne) and is called mutabaqa; the other two are ʿaqliyya (reason-borne) and are called tadammun and iltizam. Coinage-borne indication cannot yield different roads: a hearer who knows the coinage finds no word clearer than another, and one who does not finds none pointing at all. The mind-borne indications can, because concomitance comes in DEGREES — near or far, one step or several — and so the same meaning can be reached by a clear road or a dim one. The subject of the science is therefore tashbih, majaz and kinaya; majaz is set before kinaya because majaz's meaning is like a part of kinaya's (in majaz only the concomitant is meant; in kinaya the coined meaning may be meant too), and tashbih stands first because majaz is built upon it. The wave-14 engine reads the FIRST door: TashbihEngine names the four arkan from the nahw seats the analyzers already fill.",
  "tr": "Matn: وَهُوَ عِلْمٌ يُعْرَفُ بِهِ إِيرَادُ الْمَعْنَى الْوَاحِدِ بِطُرُقٍ مُخْتَلِفَةٍ فِي وُضُوحِ الدَّلَالَةِ عَلَيْهِ — «BİR mânâyı, ona delâletin AÇIKLIĞINDA farklı yollarla getirmenin kendisiyle bilindiği ilim». Tarifi üç kayıt taşır: bir mânâ (birkaç değil), birkaç yol (bir değil), AÇIKLIKTA farklı yollar (yalnız lafızda değil). Şerh sonra bu yolların neden var olduğunu sorar ve DELÂLET üzerinden cevaplar: lafız ya vaz' olunduğu şeyin tamamına, ya bir cüz'üne, ya dışındaki bir şeye delâlet eder — ilki vaz'iyyedir, mutâbakat denir; öteki ikisi akliyyedir, tazammun ve iltizam denir. Vaz'iyye delâlet farklı yollar veremez: vaz'ı bilen dinleyici için hiçbir lafız ötekinden açık değildir; bilmeyen için hiçbiri göstermez. Akliyye delâletler verebilir; çünkü lüzum DERECELİDİR — yakın ya da uzak, bir adım ya da birkaç — ve aynı mânâya açık bir yoldan da loş bir yoldan da varılabilir. İlmin mevzuu bu yüzden teşbih, mecaz ve kinayedir; mecaz kinayeden önce konur, çünkü mecazın mânâsı kinayeninkinin bir cüz'ü gibidir (mecazda yalnız lâzım kastedilir; kinayede vaz' olunan mânâ da kastedilebilir); teşbih başta durur, çünkü mecaz onun üstüne kurulur. On dördüncü dalga motoru İLK kapıyı okur: TashbihEngine, tahlilcilerin zaten doldurduğu nahiv oturaklarından dört rüknü adlandırır."},
 "examples": [
  {"ar": "وَهُوَ عِلْمٌ يُعْرَفُ بِهِ إِيرَادُ الْمَعْنَى الْوَاحِدِ",
   "en": "the definition's first clause: ONE meaning.",
   "tr": "tarifin ilk cümlesi: BİR mânâ.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "بِطُرُقٍ مُخْتَلِفَةٍ فِي وُضُوحِ الدَّلَالَةِ عَلَيْهِ",
   "en": "the second: roads that differ in clarity.",
   "tr": "ikincisi: açıklıkta farklı yollar.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "وَتُسَمَّى الْأُولَى مُطَابَقَةً",
   "en": "the three indications named (restored).",
   "tr": "üç delâlet adlandırılır (geri yazım).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«Beyân, güzel söz söyleme sanatıdır»",
   "right": "«Beyân, BİR mânâya giden farklı açıklıktaki yolların ilmidir»",
   "why": {"en": "The definition is narrower than «eloquence»: it counts roads to a fixed meaning and ranks them by clarity. Beauty is fasaha's and badiʿ's business; bayan's is the map.",
           "tr": "Tarif «belâgat»ten dardır: sabit bir mânâya giden yolları sayar ve açıklığa göre sıralar. Güzellik fesâhatin ve bedîin işidir; beyânınki haritadır."}}],
 "relatedNotes": ["arkan-al-tashbih", "ijaz-itnab-musawat", "haqiqa-majaz", "anwa-al-majaz", "kinaya", "tashbih", "istiara"]}
NOTE151 = {
 "id": "arkan-al-tashbih",
 "title": {"ar": "أَرْكَانُ التَّشْبِيهِ وَطَرَفَاهُ",
           "en": "The four arkan of tashbih, and its two ends",
           "tr": "Teşbihin dört rüknü ve iki tarafı"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — التشبيه: أركانه وطرفاه"],
 "question": {
  "en": ["What is likened (the mushabbah), to what (the mushabbah bihi), in what shared meaning (the wajh al-shabah), and by what tool (the adat: كَ، كَأَنَّ، مِثْل، a verb of likening)?",
         "Is the adat spoken? Then mursal; dropped, mu'akkad. Is the wajh spoken? Then mufassal; dropped, mujmal. Both dropped: baligh — زَيْدٌ أَسَدٌ.",
         "Are the two ends grasped by a sense (hissi), by the mind (ʿaqli), assembled from sensed things never seen together (khayali), or never sensed at all though they would be (wahmi)?"],
  "tr": ["Ne benzetiliyor (müşebbeh), neye (müşebbehün bih), hangi ortak mânâda (vech-i şebeh), hangi araçla (edat: كَ، كَأَنَّ، مِثْل، bir benzetme fiili)?",
         "Edat söylenmiş mi? Mürsel; düşmüş mü, müekked. Vech söylenmiş mi? Mufassal; düşmüş mü, mücmel. İkisi de düşmüşse belîğ — زَيْدٌ أَسَدٌ.",
         "İki taraf duyuyla mı (hissî), akılla mı (aklî), birlikte hiç görülmemiş duyulur şeylerden mi kurulmuş (hayâlî), yoksa görülseydi görülecek ama hiç duyulmamış mı (vehmî)?"]},
 "plain": {
  "en": "A tashbih is a pointing: THIS shares THAT in SOME meaning. Three arkan sit in the definition; the tool is the fourth. Drop the tool: mu'akkad. Drop the shared meaning: mujmal. Drop both: baligh (Zayd is a lion). The two ends are then sorted by how they are grasped — sense, mind, imagination, fancy.",
  "tr": "Teşbih bir göstermedir: BU, ŞUNA bir MÂNÂDA ortaktır. Tarif üç rükün sayar, araç dördüncüsüdür. Aracı düşür, müekked; ortak mânâyı düşür, mücmel; ikisini düşür, belîğ (Zeyd bir aslandır). İki taraf sonra nasıl idrak edildiklerine göre ayrılır — duyu, akıl, hayal, vehim."},
 "explanation": {
  "en": "The definition — التَّشْبِيهُ الدَّلَالَةُ عَلَى مُشَارَكَةِ أَمْرٍ لِأَمْرٍ فِي مَعْنًى — already holds three arkan: أَمْرٍ the mushabbah, لِأَمْرٍ the mushabbah bihi, فِي مَعْنًى the wajh al-shabah; the adat (كَ، كَأَنَّ، مِثْل، شِبْه، and the verbs يُشْبِهُ، يُحَاكِي، يُمَاثِلُ) is the instrument of the DALALA itself. The definition is deliberately wide: زَيْدٌ أَسَدٌ, with adat and wajh dropped, is still a tashbih (baligh), and صُمٌّ بُكْمٌ عُمْيٌ (2:18), with the mushabbah dropped too, is still inside it — what the definition EXCLUDES is only the tashbih carried by an istiʿara (that is majaz, the second door) and the tajrid kind (that is badiʿ). The TWO ENDS are sorted by how they are grasped. HISSI: by one of the five outer senses, itself or its matter — sight (خَدُّهُ كَالْوَرْدِ), hearing (صَوْتُهُ الضَّعِيفُ كَالْهَمْسِ), smell (نَكْهَتُهُ كَالْعَنْبَرِ), taste (رِيقُهُ كَالْخَمْرِ), touch (جِلْدُهُ النَّاعِمُ كَالْحَرِيرِ); the KHAYALI counts as hissi — a non-existent thing assembled from things each sensed apart, like the anemones' red as rubied banners on chrysolite lances. ʿAQLI: grasped by no outer sense in itself or its matter — الْعِلْمُ كَالْحَيَاةِ; the WAHMI counts as ʿaqli — never sensed, though had it existed a sense would have met it, like the ghouls' fangs of Imru' al-Qays; and so do the things grasped by inner feeling (pain, pleasure). The ends may differ: الْمَنِيَّةُ كَالسَّبُعِ (ʿaqli to hissi), الْعِطْرُ كَخُلُقٍ كَرِيمٍ (hissi to ʿaqli). The engine (TashbihEngine) reads the arkan from the nahw seats — the fused kaf, كَأَنَّ's ism and khabar, مِثْل's mudaf ilayh, a verb's fa'il and maf'ul — and the kind from what is spoken; the sensory sorting is the reader's, taught here, not the engine's.",
  "tr": "Tarif — التَّشْبِيهُ الدَّلَالَةُ عَلَى مُشَارَكَةِ أَمْرٍ لِأَمْرٍ فِي مَعْنًى — üç rüknü zaten tutar: أَمْرٍ müşebbeh, لِأَمْرٍ müşebbehün bih, فِي مَعْنًى vech-i şebeh; edat (كَ، كَأَنَّ، مِثْل، شِبْه ve يُشْبِهُ، يُحَاكِي، يُمَاثِلُ fiilleri) DELÂLETİN kendi aracıdır. Tarif bilerek geniştir: edatı ve vechi düşmüş زَيْدٌ أَسَدٌ yine teşbihtir (belîğ); müşebbehi de düşmüş صُمٌّ بُكْمٌ عُمْيٌ (2:18) yine içindedir — tarifin DIŞARIDA tuttuğu yalnız istiâre yoluyla gelen teşbih (o mecazdır, ikinci kapı) ile tecrid türüdür (o bedîdir). İKİ TARAF, nasıl idrak edildiklerine göre ayrılır. HİSSÎ: beş dış duyudan biriyle, kendisi ya da maddesi — görme (خَدُّهُ كَالْوَرْدِ), işitme (صَوْتُهُ الضَّعِيفُ كَالْهَمْسِ), koklama (نَكْهَتُهُ كَالْعَنْبَرِ), tatma (رِيقُهُ كَالْخَمْرِ), dokunma (جِلْدُهُ النَّاعِمُ كَالْحَرِيرِ); HAYÂLÎ hissî sayılır — her biri ayrı ayrı duyulmuş şeylerden kurulmuş var olmayan bir şey; lâlelerin kızılının zeberced mızraklar üstünde yakut sancaklar olması gibi. AKLÎ: kendisi ya da maddesi hiçbir dış duyuyla idrak edilmeyen — الْعِلْمُ كَالْحَيَاةِ; VEHMÎ aklî sayılır — hiç duyulmamış, ama var olsaydı bir duyu onu görürdü; İmruülkays'ın gulyabani dişleri gibi; iç duyguyla idrak edilenler (elem, lezzet) de öyle. Taraflar farklı olabilir: الْمَنِيَّةُ كَالسَّبُعِ (aklîden hissîye), الْعِطْرُ كَخُلُقٍ كَرِيمٍ (hissîden aklîye). Motor (TashbihEngine) rükünleri nahiv oturaklarından okur — bitişik kâf, كَأَنَّ'nin ismi ve haberi, مِثْل'in muzâfun ileyhi, fiilin fâili ve mef'ûlü — nev'i de söylenenden; duyu tasnifi ise burada öğretilen, okuyucunun işidir, motorun değil."},
 "examples": [
  {"ar": "خَدُّهُ كَالْوَرْدِ",
   "en": "mursal mujmal, both ends seen.",
   "tr": "mürsel mücmel, iki taraf da görülen.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "زَيْدٌ أَسَدٌ",
   "en": "baligh: adat and wajh both dropped.",
   "tr": "belîğ: edat da vech de düşmüş.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "وَمَسْنُونَةٌ زُرْقٌ كَأَنْيَابِ أَغْوَالٍ",
   "en": "a wahmi mushabbah bihi.",
   "tr": "vehmî bir müşebbehün bih.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«Zeyd aslandır» cümlesinde edat olmadığı için teşbih yoktur»",
   "right": "«Edatı ve vechi düşmüş teşbih, teşbihin en kuvvetlisidir: belîğ»",
   "why": {"en": "Dropping the tool does not cancel the pointing; it tightens it. The definition asks only for an indication of sharing, and «Zayd is a lion» indicates it more forcefully than «Zayd is like a lion».",
           "tr": "Aracı düşürmek göstermeyi iptal etmez, sıkılaştırır. Tarif yalnız ortaklığa delâlet ister; «Zeyd aslandır», «Zeyd aslan gibidir»den daha güçlü delâlet eder."}}],
 "relatedNotes": ["ilm-al-bayan", "tashbih", "istiara", "inna-wa-akhawatuha", "huruf-jarr", "mubtada-khabar", "sifa-mushabbaha", "ism-fail", "ism-maful"]}
for n in (NOTE150, NOTE151):
    (GR / f"{n['id']}.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch46:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + qatala/tasawwaba/tasaada/samma (+nashara copied); notes 150-151;",
      "frames:", sum(1 for x in S if x.get("tashbih")))
