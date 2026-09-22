# -*- coding: utf-8 -*-
"""Author chapter 33 of talkhis-al-miftah — the ayat on the martaba ladder.

Sahifa 80-82 (lines ~2320-2345): the three kamal-al-ittisal grades ch32's
ladder measured, now in their own worked texts:

  • BADAL BA'D — al-Shu'ara 26:132-133: أَمَدَّكُمْ بِمَا تَعْلَمُونَ then
    أَمَدَّكُمْ بِأَنْعَامٍ وَبَنِينَ وَجَنَّاتٍ وَعُيُونٍ — the detailed
    ni'am re-deliver PART of the summary (the rank of وَجْهُهُ), fasl.
  • BADAL ISHTIMAL — the bayt: أَقُولُ لَهُ اِرْحَلْ لَا تُقِيمَنَّ عِنْدَنَا
    وَإِلَّا فَكُنْ فِي السِّرِّ وَالْجَهْرِ مُسْلِمًا — لَا تُقِيمَنَّ unfolds
    what اِرْحَلْ contained (the rank of حُسْنُهَا), fasl.
  • ATF BAYAN — Ta-Ha 20:120: فَوَسْوَسَ إِلَيْهِ الشَّيْطَانُ then
    قَالَ يَا آدَمُ هَلْ أَدُلُّكَ عَلَى شَجَرَةِ الْخُلْدِ وَمُلْكٍ لَا يَبْلَى
    — the qawl unveils the whisper (the rank of عُمَرُ), fasl.

ATTRIBUTION: s1-s2 are al-Shu'ara 26:132-133 and s5-s6 Ta-Ha 20:120,
received Qur'anic text quoted exactly in standard imla as the source
prints them; s3-s4 are the bayt the source cites (its own wording,
verbatim, verse dress). Ottoman orthography normalized to standard —
recorded normalizations.

Grammar this chapter teaches:
  • sourced anchors appended to note 136 (the three grades now stand in
    real text) and to rubai-babs — فَوَسْوَسَ is the corpus's first
    quadriliteral token, retiring that note's standing warning.
  • new paradigms: أَمَدَّ (IV geminate, the ahalla road), دَلَّ (I
    geminate, the sarra road), أَقَامَ (IV hollow, the ajaba road),
    بَلِيَ (naqis kasra, the baqiya road), رَحَلَ (sound), وَسْوَسَ
    (the first stored quadriliteral).
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
S = []

TITLE33 = {"ar": "شَوَاهِدُ كَمَالِ الِاتِّصَالِ",
           "en": "The Ladder's Witnesses",
           "tr": "Merdivenin Şahitleri"}

# ----------------------------------------- s1 — al-Shu'ara 26:132: the summary
S.append({"id": "s1", "translation": {
 "en": "He has aided you with what you know. (al-Shu'ara 26:132 — the summary, referred to the hearers' own knowledge.)",
 "tr": "Size bildiğiniz şeylerle yardım etti. (Şuarâ 26:132 — özet; dinleyenlerin kendi bilgisine havale edilmiş.)"},
 "tokens": [
  tok("أَمَدَّكُمْ","amadda","verb",["kamal-al-ittisal","doubled-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ، وَالْكُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "«He aided you» — a Form IV geminate mazi; the doer is the concealed He, and the fused كُمْ is the object.",
      "«size yardım etti» — IV. bâbdan muzâaf mâzî; fâili gizli O, bitişik كُمْ mef'ûldür.",
      segments=[seg("أَمَدَّ","amadda","verb"), seg("كُمْ","pron-2mp","pron")]),
  tok("بِمَا","ma-mawsula","part",["kamal-al-ittisal"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ، مُتَعَلِّقٌ بِأَمَدَّ.",
      "«with what» — the ba of jarr over the relative ma, in the position of jarr; the phrase hangs on the verb.",
      "«şeyle ki» — cer bâsı, ism-i mevsûl mâ üzerinde; mahallen mecrûr; öbek fiile taalluk eder.",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("تَعْلَمُونَ","alima","verb",["kamal-al-ittisal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "«you know» — one of the five verbs, marfu' by the RETAINED nun, the group's waw its doer; the clause is the sila, no mahall.",
      "«bilirsiniz» — beş fiilden; SABİT nûn ile merfû, cemaat vâvı fâil; cümle sıladır, mahalsiz.",
      punct=".")],
 "jumal": [
  J("أَمَدَّكُمْ بِمَا تَعْلَمُونَ",
    "جُمْلَةٌ فِعْلِيَّةٌ — الْإِجْمَالُ الَّذِي سَيُفَصَّلُ.",
    "The SUMMARY: the aid named only as «what you know» — a whole handed to the hearers' memory, awaiting its detail.",
    "ÖZET: yardım yalnız «bildiğiniz» diye anılır — dinleyenin hafızasına bırakılmış bir bütün, ayrıntısını bekler."),
  J("بِمَا تَعْلَمُونَ",
    "صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
    "The sila clause, no mahall — and its vagueness is the very ibham the next aya will repair.",
    "Sıla cümlesi, mahalsiz — ve kapalılığı, bir sonraki âyetin onaracağı ibhâmın tâ kendisidir.")]})

# ------------------------------- s2 — al-Shu'ara 26:133: the badal-ba'd detail
S.append({"id": "s2", "translation": {
 "en": "He has aided you with livestock and sons, and gardens and springs. (26:133 — the detail: badal ba'd, at the rank of وَجْهُهُ, and no atf letter joins the two ayat.)",
 "tr": "Size davarlar ve oğullarla, bahçeler ve pınarlarla yardım etti. (26:133 — ayrıntı: bedel-i ba'z, وَجْهُهُ mertebesinde; iki âyeti hiçbir atıf harfi bağlamaz.)"},
 "tokens": [
  tok("أَمَدَّكُمْ","amadda","verb",["kamal-al-ittisal","doubled-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْكُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ بَدَلٌ مِنَ الْأُولَى.",
      "«He aided you» — the SAME verb said again, opening the jumla that stands from the first as its BADAL.",
      "«size yardım etti» — AYNI fiil yeniden; ilkinden BEDEL duran cümleyi açar.",
      segments=[seg("أَمَدَّ","amadda","verb"), seg("كُمْ","pron-2mp","pron")]),
  tok("بِأَنْعَامٍ","anam","noun",["kamal-al-ittisal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَمَدَّ.",
      "«with livestock» — jarr, hanging on the verb: the first of the named ni'am.",
      "«davarlarla» — cer; fiile taalluk eder: adlandırılan nimetlerin ilki.",
      segments=[seg("بِ","bi","part"), seg("أَنْعَامٍ","anam","noun")]),
  tok("وَبَنِينَ","ibn","noun",["kamal-al-ittisal"],
      "الْوَاوُ عَاطِفَةٌ، وَبَنِينَ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.",
      "«and sons» — joined by the waw, majrur by the YA: بَنُونَ is attached to the sound plural and declines by letters.",
      "«ve oğullarla» — vâv ile atfedilmiş; YÂ ile mecrûr: بَنُونَ, cem'-i sâlime mülhaktır, harflerle i'rablanır.",
      segments=[seg("وَ","wa","part"), seg("بَنِينَ","ibn","noun")]),
  tok("وَجَنَّاتٍ","janna","noun",["kamal-al-ittisal"],
      "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "«and gardens» — joined, majrur by the kasra of the sound feminine plural.",
      "«ve bahçelerle» — atfedilmiş; cem'-i müennes sâlimin kesrasıyla mecrûr.",
      segments=[seg("وَ","wa","part"), seg("جَنَّاتٍ","janna","noun")]),
  tok("وَعُيُونٍ","ayn","noun",["kamal-al-ittisal"],
      "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ الظَّاهِرَةِ.",
      "«and springs» — the last of the joined ni'am, majrur.",
      "«ve pınarlarla» — atfedilen nimetlerin sonuncusu; mecrûr.",
      punct=".", segments=[seg("وَ","wa","part"), seg("عُيُونٍ","ayn","noun")])],
 "jumal": [
  J("أَمَدَّكُمْ بِأَنْعَامٍ وَبَنِينَ وَجَنَّاتٍ وَعُيُونٍ",
    "بَدَلُ بَعْضٍ مِنْ جُمْلَةِ الْإِجْمَالِ — فُصِلَتْ لِكَمَالِ الِاتِّصَالِ، مَرْتَبَةُ وَجْهِهِ.",
    "THE BADAL BA'D: the detailed ni'am re-deliver part of «what you know» more tellingly than the summary did — the rank of وَجْهُهُ in أَعْجَبَنِي زَيْدٌ وَجْهُهُ — so the aya is CUT LOOSE from its sister: what re-delivers needs no letter.",
    "BEDEL-İ BA'Z: ayrıntılı nimetler, «bildiğiniz»in bir kısmını özetten daha dokunaklı yeniden verir — أَعْجَبَنِي زَيْدٌ وَجْهُهُ'deki وَجْهُهُ mertebesi — âyet, kardeşinden KOPARILMIŞTIR: yeniden veren, harf istemez."),
  J("وَبَنِينَ وَجَنَّاتٍ وَعُيُونٍ",
    "مَعْطُوفَاتٌ بِالْوَاوِ عَلَى أَنْعَامٍ — عَطْفُ الْمُفْرَدَاتِ لَا الْجُمَلِ.",
    "INSIDE the jumla the waws join freely — these are mufrad joins on one ba, not jumla joins, and the bab's shart does not touch them.",
    "Cümlenin İÇİNDE vâvlar serbestçe bağlar — bunlar tek bâ üzerinde müfred atıflarıdır, cümle atfı değil; bâbın şartı onlara dokunmaz.")]})

# ------------------------------------- s3 — the bayt: irhal, the ishtimal badal
S.append({"id": "s3", "translation": {
 "en": "I say to him: depart! — do not ever stay among us —",
 "tr": "Ona derim ki: göç, git! — sakın yanımızda kalma —"},
 "tokens": [
  tok("أَقُولُ","qala","verb",["kamal-al-ittisal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنَا.",
      "«I say» — a marfu' mudari, its doer the concealed I.",
      "«derim» — merfû muzâri; fâili gizli ben."),
  tok("لَهُ","li","part",["kamal-al-ittisal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَقُولُ.",
      "«to him» — the jarr phrase on the verb.",
      "«ona» — fiile taalluk eden câr-mecrûr.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("اِرْحَلْ","rahala","verb",["kamal-al-ittisal","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ — مَقُولُ الْقَوْلِ.",
      "«depart!» — the amr, mabni on the sukun, opening the quoted speech.",
      "«göç git!» — sükûn üzere mebnî emir; mekûlü'l-kavli açar."),
  tok("لَا","la-nahiya","part",["kamal-al-ittisal","al-nahy-wa-wujuhuh"],
      "لَا النَّاهِيَةُ الْجَازِمَةُ.",
      "«do not» — the prohibiting, jazming la.",
      "«sakın -ma» — nehyeden, cezmeden lâ."),
  tok("تُقِيمَنَّ","aqama","verb",["kamal-al-ittisal","nun-tawkid"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ، مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ أَنْتَ.",
      "«ever stay» — jazmed by the la yet MABNI on the fatha: the HEAVY NUN of emphasis fuses to it and takes the ending for itself.",
      "«aslâ kalma» — lâ ile meczum, fakat fetha üzere MEBNÎ: ağır TE'KÎD NÛNU ona kaynaşır ve sonu kendine alır."),
  tok("عِنْدَنَا","inda","noun",["kamal-al-ittisal"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِتُقِيمَنَّ، وَنَا مُضَافٌ إِلَيْهِ.",
      "«among us» — the zarf of place on the verb; نَا its mudaf ilayh.",
      "«yanımızda» — fiile taalluk eden mekân zarfı; نَا muzâfun ileyh.",
      punct="•", segments=[seg("عِنْدَ","inda","noun"), seg("نَا","pron-1p","pron")])],
 "jumal": [
  J("اِرْحَلْ",
    "مَقُولُ الْقَوْلِ — فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "The quoted amr: the departure demanded whole, in nasb as what «I say» says.",
    "Aktarılan emir: bütün hâliyle istenen gidiş; «derim»in dediği olarak mahallen mansub."),
  J("لَا تُقِيمَنَّ عِنْدَنَا",
    "بَدَلُ اشْتِمَالٍ مِنْ جُمْلَةِ اِرْحَلْ — فُصِلَتْ لِكَمَالِ الِاتِّصَالِ، مَرْتَبَةُ حُسْنِهَا.",
    "THE BADAL ISHTIMAL: not-staying is not a piece of departing — it is what departing CONTAINS, said with the emphasis the amr could not carry: the rank of حُسْنُهَا in أَعْجَبَنِي الدَّارُ حُسْنُهَا — so no letter joins them.",
    "BEDEL-İ İŞTİMÂL: kalmamak, gitmenin bir parçası değil — gitmenin KAPSADIĞIDIR; emrin taşıyamadığı te'kîdle söylenmiştir: أَعْجَبَنِي الدَّارُ حُسْنُهَا'daki حُسْنُهَا mertebesi — bu yüzden aralarına harf girmez.")]})

# --------------------------- s4 — the bayt's second hemistich: wa-illa fa-kun
S.append({"id": "s4", "translation": {
 "en": "— and if not, then be, in secret and in the open, one who submits.",
 "tr": "— yok eğer gitmeyeceksen, gizlide ve açıkta tam bir müslüman ol."},
 "tokens": [
  tok("وَإِلَّا","illa-shartiyya","part",["kamal-al-ittisal"],
      "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنِ الشَّرْطِيَّةُ أُدْغِمَتْ فِي لَا النَّافِيَةِ — إِنْ لَا تَرْحَلْ، وَفِعْلُ الشَّرْطِ مَحْذُوفٌ.",
      "«and if not» — the waw joins; إِلَّا here is the conditional إِنْ fused into لَا, its shart verb OMITTED: «if you will not depart…».",
      "«yok eğer» — vâv bağlar; buradaki إِلَّا, لَا'ya idgam edilmiş şart إِنْ'idir; şart fiili MAHZUFTUR: «gitmeyeceksen…».",
      segments=[seg("وَ","wa","part"), seg("إِلَّا","illa-shartiyya","part")]),
  tok("فَكُنْ","kana","verb",["kamal-al-ittisal","kana-wa-akhawatuha"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَكُنْ فِعْلُ أَمْرٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ وَاسْمُهَا أَنْتَ.",
      "«then be» — the fa binds the jawab; the defective kun carries its concealed you as its ism.",
      "«o hâlde ol» — fâ, cevabı bağlar; nâkıs كُنْ, gizli sen'i ismi olarak taşır.",
      segments=[seg("فَ","fa","part"), seg("كُنْ","kana","verb")]),
  tok("فِي","fi","part",["kamal-al-ittisal"],
      "حَرْفُ جَرٍّ.",
      "«in» — a jarr letter.",
      "«-de» — cer harfi."),
  tok("السِّرِّ","sirr","noun",["kamal-al-ittisal","tibaq"],
      "اسْمٌ مَجْرُورٌ، مُتَعَلِّقٌ بِمُسْلِمًا.",
      "«the secret» — majrur; the phrase hangs on «one who submits».",
      "«gizlide» — mecrûr; öbek «müslüman»a taalluk eder."),
  tok("وَالْجَهْرِ","jahr","noun",["kamal-al-ittisal","tibaq"],
      "مَعْطُوفٌ مَجْرُورٌ — وَبَيْنَهُ وَبَيْنَ السِّرِّ طِبَاقٌ.",
      "«and the open» — joined, majrur — and against «the secret» it stands in TIBAQ: the pair closes every door.",
      "«ve açıkta» — atfedilmiş, mecrûr — «gizli» ile TIBAK kurar: çift, bütün kapıları kapatır.",
      segments=[seg("وَ","wa","part"), seg("الْجَهْرِ","jahr","noun")]),
  tok("مُسْلِمًا","muslim","noun",["kamal-al-ittisal"],
      "خَبَرُ كُنْ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«one who submits» — kun's khabar, mansub by the plain fatha.",
      "«müslüman» — كُنْ'un haberi; açık fethayla mansub.",
      punct="•")],
 "jumal": [
  J("وَإِلَّا فَكُنْ فِي السِّرِّ وَالْجَهْرِ مُسْلِمًا",
    "جُمْلَةٌ شَرْطِيَّةٌ مَعْطُوفَةٌ بِالْوَاوِ — هُنَا الْعَطْفُ مَقْصُودٌ.",
    "Here the waw IS wanted: a new demand, not a restatement — the alternative joins the speech lawfully, and the contrast with the fasl before it is the lesson.",
    "Burada vâv İSTENİR: yeniden söyleyiş değil, yeni bir talep — seçenek, söze meşru bağlanır; önceki faslla zıtlığı dersin kendisidir."),
  J("فِي السِّرِّ وَالْجَهْرِ",
    "طِبَاقٌ بَيْنَ الضِّدَّيْنِ.",
    "The badi' rides along: secret against open, the pair that leaves no third place.",
    "Bedî' beraber gider: gizliye karşı açık — üçüncü yer bırakmayan çift.")]})

# ------------------------------------ s5 — Ta-Ha 20:120a: the obscure whisper
S.append({"id": "s5", "translation": {
 "en": "Then Satan whispered to him… (Ta-Ha 20:120 — the first jumla, and its whisper is left unnamed: the ibham.)",
 "tr": "Derken şeytan ona vesvese verdi… (Tâhâ 20:120 — ilk cümle; fısıltının ne olduğu söylenmez: ibhâm.)"},
 "tokens": [
  tok("فَوَسْوَسَ","waswasa","verb",["kamal-al-ittisal","rubai-babs"],
      "الْفَاءُ عَاطِفَةٌ، وَوَسْوَسَ فِعْلٌ مَاضٍ رُبَاعِيٌّ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«then whispered» — the fa joins the aya's train; وَسْوَسَ is a QUADRILITERAL mazi on فَعْلَلَ — the doubled syllable is the whisper's own sound.",
      "«derken vesvese verdi» — fâ, âyet zincirine bağlar; وَسْوَسَ, فَعْلَلَ vezninde RUBÂÎ mâzîdir — ikizlenen hece, fısıltının kendi sesidir.",
      segments=[seg("فَ","fa","part"), seg("وَسْوَسَ","waswasa","verb")]),
  tok("إِلَيْهِ","ila","part",["kamal-al-ittisal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِوَسْوَسَ.",
      "«to him» — the jarr phrase on the verb.",
      "«ona» — fiile taalluk eden câr-mecrûr.",
      segments=[seg("إِلَى","ila","part"), seg("هِ","pron-3ms","pron")]),
  tok("الشَّيْطَانُ","shaytan","noun",["kamal-al-ittisal"],
      "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Satan» — the fa'il, deferred past the jarr phrase, marfu'.",
      "«şeytan» — fâil; câr-mecrûrun ardına ertelenmiş, merfû.",
      punct=".")],
 "jumal": [
  J("فَوَسْوَسَ إِلَيْهِ الشَّيْطَانُ",
    "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ بِالْفَاءِ عَلَى مَا قَبْلَهَا فِي الْآيَاتِ.",
    "The whisper reported — but WHAT was whispered stays dark: the jumla carries an ibham only its neighbour can lift.",
    "Fısıltı haber verilir — fakat NE fısıldandığı karanlıkta kalır: cümle, ancak komşusunun kaldıracağı bir ibhâm taşır."),
  J("فَوَسْوَسَ",
    "الْفِعْلُ الرُّبَاعِيُّ — فَعْلَلَ يُفَعْلِلُ.",
    "The corpus's first quadriliteral in real text: فَعْلَلَ, whose mudari alone among bare verbs opens on a DAMMA prefix (يُوَسْوِسُ).",
    "Külliyatın gerçek metindeki ilk rubâîsi: فَعْلَلَ — mücerred fiiller içinde muzârisi tek başına DAMME önekiyle açılır (يُوَسْوِسُ).")]})

# --------------------------- s6 — Ta-Ha 20:120b: the atf-bayan qawl, cut loose
S.append({"id": "s6", "translation": {
 "en": "He said: O Adam, shall I show you the tree of eternity and a dominion that never decays? (the unveiling — atf bayan at the rank of عُمَرُ, and no letter joins it to the whisper.)",
 "tr": "Dedi ki: Ey Âdem, sana sonsuzluk ağacını ve hiç eskimeyen bir saltanatı göstereyim mi? (perdenin açılışı — عُمَرُ mertebesinde atf-ı beyân; fısıltıya hiçbir harf bağlamaz.)"},
 "tokens": [
  tok("قَالَ","qala","verb",["kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ — وَلَا عَاطِفَ قَبْلَهُ.",
      "«he said» — a mazi with NO atf letter before it: the absence is the fasl the bab teaches.",
      "«dedi» — önünde HİÇBİR atıf harfi olmayan mâzî: bu yokluk, bâbın öğrettiği faslın kendisidir."),
  tok("يَا","ya","part",["kamal-al-ittisal","vocative-munada"],
      "حَرْفُ نِدَاءٍ.",
      "«O» — the calling particle.",
      "«ey» — nidâ harfi."),
  tok("آدَمُ","aadam","propn",["kamal-al-ittisal","vocative-munada","mamnu-min-sarf"],
      "مُنَادَى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
      "«Adam» — the munada, a single alam, mabni on the damm in nasb's position; the name itself is diptote, barred by name-hood and foreign origin.",
      "«Âdem» — münâdâ; müfred alem, zamme üzere mebnî, mahallen mansub; adın kendisi alemlik ve ucme sebebiyle gayr-i munsariftir."),
  tok("هَلْ","hal-istifham","part",["kamal-al-ittisal","al-istifham"],
      "حَرْفُ اسْتِفْهَامٍ لِطَلَبِ التَّصْدِيقِ — وَالْمُرَادُ الْعَرْضُ وَالْإِغْرَاءُ.",
      "«shall…?» — hal, asking assent in letter; in aim the tempter OFFERS — the question dress on the lure.",
      "«…mi?» — lafzen tasdik isteyen هَلْ; maksatta iğvâcı SUNAR — yem üzerine soru kılığı."),
  tok("أَدُلُّكَ","dalla","verb",["kamal-al-ittisal","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ — مُضَاعَفٌ.",
      "«I show you» — a geminate mudari, its doer I, the kaf its object.",
      "«sana göstereyim» — muzâaf muzâri; fâili ben, kâf mef'ûlü.",
      segments=[seg("أَدُلُّ","dalla","verb"), seg("كَ","pron-2ms","pron")]),
  tok("عَلَى","ala","part",["kamal-al-ittisal"],
      "حَرْفُ جَرٍّ.",
      "«upon» — a jarr letter.",
      "«üzerine» — cer harfi."),
  tok("شَجَرَةِ","shajara","noun",["kamal-al-ittisal"],
      "اسْمٌ مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِأَدُلُّ.",
      "«the tree of» — majrur, and a mudaf; the phrase hangs on the verb.",
      "«ağacına» — mecrûr ve muzâf; öbek fiile taalluk eder."),
  tok("الْخُلْدِ","khuld","noun",["kamal-al-ittisal"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ الظَّاهِرَةِ.",
      "«eternity» — the mudaf ilayh, majrur.",
      "«sonsuzluğun» — muzâfun ileyh; mecrûr."),
  tok("وَمُلْكٍ","mulk","noun",["kamal-al-ittisal"],
      "الْوَاوُ عَاطِفَةٌ، وَمُلْكٍ مَعْطُوفٌ عَلَى شَجَرَةِ مَجْرُورٌ.",
      "«and a dominion» — joined onto «the tree», majrur.",
      "«ve bir saltanata» — «ağaç» üzerine atfedilmiş; mecrûr.",
      segments=[seg("وَ","wa","part"), seg("مُلْكٍ","mulk","noun")]),
  tok("لَا","la-nafiya","part",["kamal-al-ittisal"],
      "لَا النَّافِيَةُ.",
      "«never» — the negating la, governing nothing.",
      "«hiç» — nefyeden lâ; amel etmez."),
  tok("يَبْلَى","balia","verb",["kamal-al-ittisal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْجُمْلَةُ صِفَةٌ لِمُلْكٍ فِي مَحَلِّ جَرٍّ.",
      "«decays» — a naqis mudari, its damma estimated on the alif; the clause is مُلْكٍ's SIFA, in the position of jarr.",
      "«eskir» — nâkıs muzâri; dammesi elif üzerinde takdîrî; cümle, مُلْكٍ'in SIFATIDIR, mahallen mecrûr.",
      punct="؟")],
 "jumal": [
  J("قَالَ يَا آدَمُ هَلْ أَدُلُّكَ عَلَى شَجَرَةِ الْخُلْدِ وَمُلْكٍ لَا يَبْلَى",
    "عَطْفُ بَيَانٍ مِنْ جُمْلَةِ فَوَسْوَسَ — فُصِلَتْ لِكَمَالِ الِاتِّصَالِ، مَرْتَبَةُ عُمَرَ.",
    "THE UNVEILING: the qawl says WHAT the whisper was, as عُمَرُ says who أَبُو حَفْصٍ is — atf bayan between jumlas, so the aya cuts it loose: no letter stands between a veil and its lifting.",
    "PERDENİN AÇILIŞI: kavl, fısıltının NE olduğunu söyler — عُمَرُ'in أَبُو حَفْصٍ'ın kim olduğunu söylediği gibi — cümleler arası atf-ı beyân; âyet onu koparır: örtü ile açılışı arasına harf girmez."),
  J("لَا يَبْلَى",
    "جُمْلَةُ الصِّفَةِ — فِي مَحَلِّ جَرٍّ.",
    "The sifa clause on the indefinite مُلْكٍ, in jarr's position — the lure polished to its last word.",
    "Nekre مُلْكٍ üzerindeki sıfat cümlesi; mahallen mecrûr — yem, son kelimesine dek cilalanmış.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "amadda": g("أَمَدَّ", "م د د", "verb", "to aid, supply, reinforce", "yardım etmek, desteklemek", 5, form="IV"),
 "anam": g("أَنْعَام", "ن ع م", "noun", "livestock, cattle (pl. of نَعَم)", "davarlar, en'âm (نَعَم'in çoğulu)", 4),
 "rahala": g("رَحَلَ", "ر ح ل", "verb", "to depart, set out", "göçmek, yola çıkmak", 3, form="I"),
 "aqama": g("أَقَامَ", "ق و م", "verb", "to stay, reside; to establish", "kalmak, ikamet etmek; ikame etmek", 3, form="IV"),
 "jahr": g("جَهْر", "ج ه ر", "noun", "the open, public utterance", "açık, âşikâre", 4),
 "waswasa": g("وَسْوَسَ", "و س و س", "verb", "to whisper (temptation)", "vesvese vermek, fısıldamak", 4, form="Q1"),
 "aadam": g("آدَم", None, "propn", "Adam (the prophet; a diptote name)", "Âdem (peygamber; gayr-i munsarif isim)", 2),
 "dalla": g("دَلَّ", "د ل ل", "verb", "to show, point (to)", "göstermek, delâlet etmek", 3, form="I"),
 "shajara": g("شَجَرَة", "ش ج ر", "noun", "tree", "ağaç", 2, plural="أَشْجَار"),
 "khuld": g("خُلْد", "خ ل د", "noun", "eternity, everlastingness", "sonsuzluk, hulûd", 4),
 "balia": g("بَلِيَ", "ب ل ي", "verb", "to decay, wear out", "eskimek, çürümek", 4, form="I"),
 "illa-shartiyya": g("إِلَّا (= إِنْ لَا)", None, "part", "otherwise; if not (the conditional in fused into la)", "yoksa; değilse (şart إِنْ'i لَا'ya idgamlı)", 5),
 "la-nafiya": copy_gloss("aqaid-ahl-al-sunna", "la-nafiya") if False else None,  # resolved below
 "ma-mawsula": copy_gloss("kitab-al-sulh", "ma-mawsula"),
 "ibn": copy_gloss("wasiyyat-abi-hanifa-samti", "ibn"),
 "janna": copy_gloss("aqaid-ahl-al-sunna", "janna"),
 "ayn": copy_gloss("kitab-al-buyu", "ayn"),
 "inda": copy_gloss("kitab-al-sulh", "inda"),
 "sirr": copy_gloss("wasiyyat-abi-hanifa-samti", "sirr"),
 "muslim": copy_gloss("kitab-al-sulh", "muslim"),
 "mulk": copy_gloss("aqaid-ahl-al-sunna", "mulk"),
}
del GLOSS_ADD["la-nafiya"]

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/33.json").write_text(
    json.dumps({"chapter": 33, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 33 for c in man["chapters"]):
    man["chapters"].append({"n": 33, "title": TITLE33})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.33.0"
ADD_EN = (" Chapter 33 carries the ladder's witnesses (lines ~2320-2345, sahifa 80-82): s1-s2 "
          "are al-Shu'ara 26:132-133 and s5-s6 Ta-Ha 20:120, received Qur'anic text quoted "
          "exactly in standard imla as the source prints them; s3-s4 are the bayt the source "
          "cites, its own wording verbatim in verse dress. Ottoman orthography normalized to "
          "standard — recorded normalizations.")
ADD_TR = (" Otuz üçüncü bâb, merdivenin şahitlerini taşır (satır ~2320-2345, sahife 80-82): "
          "s1-s2 Şuarâ 26:132-133, s5-s6 Tâhâ 20:120 — kaynağın kendi bastığı standart imlâ "
          "ile aynen alınmış mervî Kur'ân metni; s3-s4, kaynağın iktibas ettiği beytin kendi "
          "ifadesiyle, nazım kisvesinde aynen alınmışıdır. Osmanlı imlâsı standart imlâya "
          "çevrildi — kayıtlı normalizasyonlardır.")
if "2320-2345" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "amadda" not in mo["verbs"]:
    # Form IV geminate, assembled like the corpus's أَحَلَّ: contracted stem
    # before vowels, broken stem before consonants.
    mo["verbs"]["amadda"] = _sg.entry(
        "بَابُ الْإِفْعَالِ: أَفْعَلَ يُفْعِلُ — مُضَاعَفٌ", _sg.W4,
        "إِمْدَاد", "مُمِدّ",
        _sg.mazi14("أَمَدّ", "أَمْدَد"),
        _sg.mudari14("ُ", "مِدّ", "مْدِد"),
        ["أَمِدَّ", "أَمِدَّا", "أَمِدُّوا", "أَمِدِّي", "أَمِدَّا", "أَمْدِدْنَ"],
        "يُمِدَّ", "يُمِدَّ", "تُمِدَّ",
        "مُمَدّ", "أُمِدَّ", "يُمَدُّ",
        "مُضَاعَفٌ مِنَ الْإِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُمِدَّ، وَيَجُوزُ لَمْ يُمْدِدْ.")
if "dalla" not in mo["verbs"]:
    # Form I geminate of bab nasara, spelled out like the corpus's سَرَّ.
    mo["verbs"]["dalla"] = _sg.entry(
        "مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
        "دَلَالَة", "دَالّ",
        _sg.mazi14("دَلّ", "دَلَل"),
        _sg.mudari14("َ", "دُلّ", "دْلُل"),
        ["دُلَّ", "دُلَّا", "دُلُّوا", "دُلِّي", "دُلَّا", "اُدْلُلْنَ"],
        "يَدُلَّ", "يَدُلَّ", "تَدُلَّ",
        "مَدْلُول", "دُلَّ", "يُدَلُّ",
        "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَدُلَّ، وَيَجُوزُ لَمْ يَدْلُلْ.")
if "aqama" not in mo["verbs"]:
    # Form IV hollow on the أَجَابَ road.
    mo["verbs"]["aqama"] = _sg.derived_hollow(
        _sg.B4, _sg.W4, "ُ", "أَقَام", "أَقَم", "قِيم", "قِم", "أَقِيم", "أَقِم",
        "إِقَامَة", "مُقِيم", "مُقَام", "أُقِيمَ", "يُقَامُ")
if "rahala" not in mo["verbs"]:
    mo["verbs"]["rahala"] = _sg.sound1(
        "fataha", "رَحَل", "رْحَل", "اِرْحَل", "رَحِيل", "رَاحِل")
if "balia" not in mo["verbs"]:
    # naqis of bab sami'a on the بَقِيَ road: the ya keeps its kasra in the
    # mazi and falls only against the group's waw; lazim, so no majhul.
    mo["verbs"]["balia"] = _sg.entry(
        "مِنْ بَابِ سَمِعَ يَسْمَعُ — نَاقِصٌ يَائِيٌّ", "فَعِلَ يَفْعَلُ",
        "بِلًى", "بَالٍ",
        ["بَلِيَ", "بَلِيَا", "بَلُوا", "بَلِيَتْ", "بَلِيَتَا", "بَلِينَ",
         "بَلِيتَ", "بَلِيتُمَا", "بَلِيتُمْ", "بَلِيتِ", "بَلِيتُمَا", "بَلِيتُنَّ",
         "بَلِيتُ", "بَلِينَا"],
        ["يَبْلَى", "يَبْلَيَانِ", "يَبْلَوْنَ", "تَبْلَى", "تَبْلَيَانِ", "يَبْلَيْنَ",
         "تَبْلَى", "تَبْلَيَانِ", "تَبْلَوْنَ", "تَبْلَيْنَ", "تَبْلَيَانِ", "تَبْلَيْنَ",
         "أَبْلَى", "نَبْلَى"],
        ["اِبْلَ", "اِبْلَيَا", "اِبْلَوْا", "اِبْلَيْ", "اِبْلَيَا", "اِبْلَيْنَ"],
        "يَبْلَى", "يَبْلَ", "تَبْلَ",
        None, None, None,
        "نَاقِصٌ يَائِيٌّ لَازِمٌ فَلَا مَجْهُولَ لَهُ؛ تَسْقُطُ الْيَاءُ مَعَ وَاوِ الْجَمَاعَةِ — بَلُوا.")
if "waswasa" not in mo["verbs"]:
    # the corpus's FIRST quadriliteral: فَعْلَلَ يُفَعْلِلُ — the one bare
    # verb whose mudari prefix takes the DAMMA. The derived() maker builds
    # it exactly (yv damma + the four-letter stems).
    mo["verbs"]["waswasa"] = _sg.derived(
        "الرُّبَاعِيُّ الْمُجَرَّدُ: فَعْلَلَ يُفَعْلِلُ فَعْلَلَةً", "فَعْلَلَ يُفَعْلِلُ",
        "ُ", "وَسْوَس", "وَسْوِس", "وَسْوِس",
        "وَسْوَسَة", "مُوَسْوِس", "مُوَسْوَس", "وُسْوِسَ", "يُوَسْوَسُ")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ------------------------------------- sourced anchors into notes 136 + rubai
GR = ROOT / "content/grammar"
n136p = GR / "kamal-al-ittisal.json"
n136 = json.loads(n136p.read_text(encoding="utf-8"))
# sentence ids REPEAT across chapters (every chapter restarts s1…), so a
# dedupe keyed on (story, sentence) collides with ch32's own s2/s6 rows
# and silently drops the witnesses — key on the AR text as well.
have = {(e.get("sourceStory"), e.get("sentence"), e.get("ar")) for e in n136.get("examples", [])}
for ex in [
  {"ar": "أَمَدَّكُمْ بِأَنْعَامٍ وَبَنِينَ وَجَنَّاتٍ وَعُيُونٍ",
   "en": "26:133 — the badal-ba'd witness: the detail cut loose from the summary.",
   "tr": "26:133 — bedel-i ba'z şahidi: ayrıntı, özetten koparılmış.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "لَا تُقِيمَنَّ عِنْدَنَا",
   "en": "the bayt — the badal-ishtimal witness, at the rank of حُسْنُهَا.",
   "tr": "beyit — bedel-i iştimâl şahidi, حُسْنُهَا mertebesinde.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "قَالَ يَا آدَمُ",
   "en": "20:120 — the atf-bayan witness: the qawl unveils the whisper.",
   "tr": "20:120 — atf-ı beyân şahidi: kavl, fısıltıyı açar.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}]:
    if (ex["sourceStory"], ex["sentence"], ex["ar"]) not in have:
        n136["examples"].append(ex)
n136p.write_text(json.dumps(n136, ensure_ascii=False, indent=1), encoding="utf-8")

nrp = GR / "rubai-babs.json"
nr = json.loads(nrp.read_text(encoding="utf-8"))
have = {(e.get("sourceStory"), e.get("sentence")) for e in nr.get("examples", [])}
if ("talkhis-al-miftah", "s5") not in have:
    nr.setdefault("examples", []).append({
        "ar": "فَوَسْوَسَ إِلَيْهِ الشَّيْطَانُ",
        "en": "Ta-Ha 20:120 — وَسْوَسَ on فَعْلَلَ: the corpus's first quadriliteral in real text.",
        "tr": "Tâhâ 20:120 — فَعْلَلَ vezninde وَسْوَسَ: külliyatın gerçek metindeki ilk rubâîsi.",
        "sourceStory": "talkhis-al-miftah", "sentence": "s5"})
nrp.write_text(json.dumps(nr, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch33:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD),
      "; morph + amadda, dalla, aqama, rahala, balia, waswasa; notes 136+rubai anchored")
