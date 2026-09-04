# -*- coding: utf-8 -*-
"""Author chapter 41 of talkhis-al-miftah — الْإِيغَالُ.

Sahifa 98 (lines ~2843-2855): the fourth occasion of itnab — IGHAL
(«going very far»): sealing the bayt with something that yields a
point the meaning would be complete without.

  • al-Khansa on her brother Sakhr: وَإِنَّ صَخْرًا لَتَأْتَمُّ
    الْهُدَاةُ بِهِ • كَأَنَّهُ عَلَمٌ فِي رَأْسِهِ نَارٌ — the
    likening is complete at كَأَنَّهُ عَلَمٌ; the fire at the summit
    is ighal, heaping the mubalagha higher.
  • Imru' al-Qays: كَأَنَّ عُيُونَ الْوَحْشِ حَوْلَ خِبَائِنَا
    وَأَرْحُلِنَا • الْجَزْعُ الَّذِي لَمْ يُثَقَّبْ — the likening is
    complete at الْجَزْعُ; the UNPIERCED bead is ighal, verifying it
    (a pierced bead loses its lustre — living eyes shine whole).
  • And for those who say ighal is not poetry's alone: قَالَ يَا
    قَوْمِ اتَّبِعُوا الْمُرْسَلِينَ * اتَّبِعُوا مَنْ لَا
    يَسْأَلُكُمْ أَجْرًا وَهُمْ مُهْتَدُونَ (Ya-Sin 36:20-21), where
    وَهُمْ مُهْتَدُونَ seals the aya as added urging.

ATTRIBUTION: s5-s6 are Ya-Sin 36:20-21 (part), received Qur'anic text
quoted exactly in standard imla as the source prints them; s1-s2 are
al-Khansa's bayt and s3-s4 Imru' al-Qays's, as the source recites
them, each split at the hemistich per the package's precedent.

Grammar this chapter teaches:
  • note 145 `ighal` — the definition, the two bayts' nuktas
    (mubalagha vs tahqiq), and the khilaf on poetry-onliness.
  • new paradigms: اِئْتَمَّ (Form VIII geminate — the twin-cell
    doctrine's newest predator, bank-checked), ثَقَّبَ (II), اِتَّبَعَ
    (VIII on the اِتَّصَلَ road).
  • the munada's endings at the case layer: يَا زَيْدُ mabni, يَا
    عَبْدَ اللهِ nasb, يَا قَوْمِ silence (the dropped speaker's ya).
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

TITLE41 = {"ar": "الْإِيغَالُ",
           "en": "Ighal — the Far-Reaching Seal",
           "tr": "Îgāl — Uzağa Varan Mühür"}

# ----------- s1 — Khansa, first hemistich
S.append({"id": "s1", "translation": {
 "en": "Truly Sakhr — the guides take him for their leader,",
 "tr": "Gerçekten Sahr — hidayet rehberleri ona uyarlar,"},
 "tokens": [
  tok("وَإِنَّ","inna","part",["ighal","inna-wa-akhawatuha"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.",
      "«truly» — the lament opens on certainty.",
      "«gerçekten» — mersiye kesinlikle açılır.",
      segments=[seg("وَ","wa","part"), seg("إِنَّ","inna","part")]),
  tok("صَخْرًا","sakhr","propn",["ighal"],
      "اسْمُ إِنَّ مَنْصُوبٌ — صَخْرٌ أَخُو الْخَنْسَاءِ، تَرْثِيهِ.",
      "«Sakhr» — inna's ism: al-Khansa's brother, whom she mourns.",
      "«Sahr» — inne'nin ismi: Hansâ'nın ağıt yaktığı kardeşi."),
  tok("لَتَأْتَمُّ","itamma","verb",["ighal","form-viii-verbs","doubled-verbs"],
      "اللَّامُ الْمُزَحْلَقَةُ، وَتَأْتَمُّ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.",
      "«surely take for leader» — the slid-down lam over the Form VIII geminate of أَمَّ: to follow as one follows an imam.",
      "«elbette uyarlar» — kaydırılmış lâm, أَمَّ kökünün VIII. bâb muzâafı üzerinde: imama uyar gibi uymak.",
      segments=[seg("لَ","li","part"), seg("تَأْتَمُّ","itamma","verb")]),
  tok("الْهُدَاةُ","hadin","noun",["ighal"],
      "فَاعِلٌ مَرْفُوعٌ — جَمْعُ هَادٍ.",
      "«the guides» — even those who guide need his lead: plural of the manqus هَادٍ.",
      "«rehberler» — yol gösterenler bile onun öncülüğüne muhtaç: mankus هَادٍ'nin cem'i."),
  tok("بِهِ","bi","part",["ighal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِتَأْتَمُّ.",
      "«by him» —",
      "«ona» —",
      punct="•", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")])],
 "jumal": [
  J("وَإِنَّ صَخْرًا لَتَأْتَمُّ الْهُدَاةُ بِهِ",
    "جُمْلَةُ إِنَّ وَاسْمُهَا وَخَبَرُهَا الْفِعْلِيُّ — صَدْرُ بَيْتِ الْخَنْسَاءِ.",
    "The claim the bayt will now magnify: the guides themselves are guided by him.",
    "Beytin şimdi büyüteceği dava: rehberlerin rehberi odur."),
  J("لَتَأْتَمُّ",
    "اللَّامُ الْمُزَحْلَقَةُ عَلَى خَبَرِ إِنَّ.",
    "The emphasis lam slid from inna's ism onto its khabar — the old muzahlaqa rule in verse.",
    "İnne'nin isminden haberine kaydırılan te'kid lâmı — eski muzahlaka kuralı şiirde.")]})

# ----------- s2 — Khansa, second hemistich: the ighal
S.append({"id": "s2", "translation": {
 "en": "as if he were a mountain — with a FIRE at its summit. (the likening was complete at «mountain»; the fire is IGHAL: mubalagha heaped higher, and the rhyme earned.)",
 "tr": "sanki bir dağ — ZİRVESİNDE ATEŞ yanan. (teşbih «dağ»da tamamdı; ateş ÎGĀLDİR: mübâlağa bir kat daha, kafiye de kazanılmış.)"},
 "tokens": [
  tok("كَأَنَّهُ","ka-anna","part",["ighal","inna-wa-akhawatuha","tashbih"],
      "كَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.",
      "«as if he» — the likening harf with its pronoun ism.",
      "«sanki o» — teşbih harfi ve zamir ismi.",
      segments=[seg("كَأَنَّ","ka-anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("عَلَمٌ","alam","noun",["ighal","tashbih"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ — وَبِهِ يَتِمُّ التَّشْبِيهُ.",
      "«a mountain» — and here the likening is COMPLETE: what follows is surplus, and earns.",
      "«bir dağ» — ve teşbih burada TAMAMDIR: sonrası fazlalıktır, ve kazanır."),
  tok("فِي","fi","part",["ighal"],
      "حَرْفُ جَرٍّ.",
      "«at» —",
      "«-de» —"),
  tok("رَأْسِهِ","ras","noun",["ighal"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ صِفَةٌ لِعَلَمٌ.",
      "«its summit» —",
      "«zirvesinde» —",
      segments=[seg("رَأْسِ","ras","noun"), seg("هِ","pron-3ms","pron")]),
  tok("نَارٌ","nar","noun",["ighal","taqdim-al-musnad"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَالْجَارُّ قَبْلَهُ خَبَرٌ مُقَدَّمٌ — وَهٰذَا الْقَوْلُ هُوَ الْإِيغَالُ: زِيَادَةُ الْمُبَالَغَةِ.",
      "«a fire» — the beacon-fire that makes the mountain a LANDMARK by night: the ighal, added after completeness for more mubalagha.",
      "«bir ateş» — dağı gecede NİŞAN kılan işaret ateşi: tamamdan sonra, mübâlağayı artırmak için gelen îgāl.",
      punct="•")],
 "jumal": [
  J("كَأَنَّهُ عَلَمٌ فِي رَأْسِهِ نَارٌ",
    "جُمْلَةُ التَّشْبِيهِ — وَفِي عَجُزِهَا الْإِيغَالُ.",
    "The ighal witness: strike the fire and the meaning stands; keep it and the praise blazes.",
    "Îgāl şahidi: ateşi sil, mânâ ayakta; bırak, övgü alev alır."),
  J("فِي رَأْسِهِ نَارٌ",
    "خَتْمُ الْبَيْتِ بِمَا يُفِيدُ نُكْتَةً يَتِمُّ الْمَعْنَى بِدُونِهَا.",
    "The definition of ighal, enacted: a seal the meaning did not need — and the point it adds.",
    "Îgāl tarifi sahnede: mânânın muhtaç olmadığı bir mühür — ve kattığı nükte.")]})

# ----------- s3 — Imru' al-Qays, first hemistich
S.append({"id": "s3", "translation": {
 "en": "As if the eyes of the wild deer, around our tents and our saddles,",
 "tr": "Sanki yaban geyiklerinin gözleri, çadırlarımızın ve semerlerimizin etrafında,"},
 "tokens": [
  tok("كَأَنَّ","ka-anna","part",["ighal","inna-wa-akhawatuha","tashbih"],
      "حَرْفُ تَشْبِيهٍ وَنَصْبٍ.",
      "«as if» — Imru' al-Qays surveys the morning after the hunt.",
      "«sanki» — İmruülkays av sabahını süzer."),
  tok("عُيُونَ","ayn-eye","noun",["ighal"],
      "اسْمُ كَأَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ — جَمْعُ عَيْنٍ.",
      "«the eyes of» — kaanna's ism, a mudaf.",
      "«gözleri» — keenne'nin ismi; muzâf."),
  tok("الْوَحْشِ","wahsh","noun",["ighal"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the wild deer» — the oryx and gazelle taken in the night's hunt.",
      "«yaban» — gecenin avında düşen yaban sığırı ve ceylan."),
  tok("حَوْلَ","hawl","noun",["ighal","maful-fih"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«around» — the place-zarf.",
      "«etrafında» — mekân zarfı."),
  tok("خِبَائِنَا","khiba","noun",["ighal"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.",
      "«our tents» —",
      "«çadırlarımızın» —",
      segments=[seg("خِبَائِ","khiba","noun"), seg("نَا","pron-1p","pron")]),
  tok("وَأَرْحُلِنَا","rahl","noun",["ighal","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَأَرْحُلِ مَعْطُوفٌ مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ رَحْلٍ.",
      "«and our saddles» — plural of رَحْل.",
      "«ve semerlerimizin» — رَحْل'in cem'i.",
      punct="•", segments=[seg("وَ","wa","part"), seg("أَرْحُلِ","rahl","noun"), seg("نَا","pron-1p","pron")])],
 "jumal": [
  J("كَأَنَّ عُيُونَ الْوَحْشِ حَوْلَ خِبَائِنَا وَأَرْحُلِنَا",
    "صَدْرُ بَيْتِ امْرِئِ الْقَيْسِ — اسْمُ كَأَنَّ وَظَرْفُهُ، وَالْخَبَرُ فِي الْعَجُزِ.",
    "The scene set: dark eyes scattered on the ground, the khabar held back for the second hemistich.",
    "Sahne kurulur: yere saçılmış kara gözler; haber ikinci mısraya saklanır."),
  J("حَوْلَ خِبَائِنَا وَأَرْحُلِنَا",
    "الظَّرْفُ وَمَا عُطِفَ عَلَيْهِ.",
    "The camp's geography in one zarf phrase.",
    "Obanın coğrafyası tek zarf öbeğinde.")]})

# ----------- s4 — Imru' al-Qays, second hemistich: the ighal
S.append({"id": "s4", "translation": {
 "en": "were onyx beads — that have NOT BEEN PIERCED. (the likening was complete at «onyx»; the unpierced is IGHAL: tahqiq — a pierced bead loses its water, and living eyes shine whole.)",
 "tr": "delinmemiş göz boncukları olsun. (teşbih «boncuk»ta tamamdı; delinmemişlik ÎGĀLDİR: tahkîk — delinen boncuğun suyu kaçar, canlı göz bütün parlar.)"},
 "tokens": [
  tok("الْجَزْعُ","jaz","noun",["ighal","tashbih"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ — خَرَزٌ يَمَانِيٌّ فِيهِ سَوَادٌ وَبَيَاضٌ، وَبِهِ يَتِمُّ التَّشْبِيهُ.",
      "«onyx beads» — the black-and-white Yemeni bead: the likening is complete here.",
      "«göz boncuğu» — siyahlı beyazlı Yemen boncuğu: teşbih burada tamamdır."),
  tok("الَّذِي","alladhi","pron",["ighal","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ، صِفَةٌ لِلْجَزْعُ.",
      "«that» — the relative opening the ighal clause.",
      "«ki o» — îgāl cümlesini açan mevsûl."),
  tok("لَمْ","lam-jazima","part",["ighal","lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "«not» — jazm incoming.",
      "«-memiş» — cezm gelir."),
  tok("يُثَقَّبْ","thaqqaba","verb",["ighal","form-ii-verbs","naib-al-fail"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَتُهُ السُّكُونُ، وَنَائِبُ الْفَاعِلِ هُوَ — وَهٰذَا الْقَيْدُ هُوَ الْإِيغَالُ: تَحْقِيقُ التَّشْبِيهِ.",
      "«been pierced» — the passive jussive: piercing drains a bead's lustre, and these eyes are alive and whole. The seal verifies the likeness — ighal for tahqiq.",
      "«delinmiş» — meçhûl meczum: delmek boncuğun suyunu alır; bu gözlerse canlı ve bütün. Mühür, benzetmeyi doğrular — tahkîk için îgāl.",
      punct="•")],
 "jumal": [
  J("الْجَزْعُ الَّذِي لَمْ يُثَقَّبْ",
    "خَبَرُ كَأَنَّ وَصِفَتُهُ — وَفِي الصِّفَةِ الْإِيغَالُ.",
    "The ighal witness again — this time the surplus VERIFIES rather than magnifies.",
    "Yine îgāl şahidi — bu kez fazlalık büyütmez, DOĞRULAR."),
  J("لَمْ يُثَقَّبْ",
    "قَيْدُ التَّحْقِيقِ — نُكْتَةُ الْإِيغَالِ هُنَا.",
    "Two words the meaning could spare, and the whole image sharpens by them.",
    "Mânânın vazgeçebileceği iki kelime — ve bütün tablo onlarla keskinleşir.")]})

# ----------- s5 — Ya-Sin 36:20: the call
S.append({"id": "s5", "translation": {
 "en": "He said: O my people, follow the messengers! (36:20)",
 "tr": "Dedi: Ey kavmim, gönderilenlere uyun! (36:20)"},
 "tokens": [
  tok("قَالَ","qala","verb",["ighal"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ هُوَ — صَاحِبُ يس، الرَّجُلُ السَّاعِي مِنْ أَقْصَى الْمَدِينَةِ.",
      "«he said» — the man who came running from the city's far side.",
      "«dedi» — şehrin öbür ucundan koşup gelen adam."),
  tok("يَا","ya","part",["ighal","vocative-munada"],
      "حَرْفُ نِدَاءٍ.",
      "«O» —",
      "«ey» —"),
  tok("قَوْمِ","qawm","noun",["ighal","vocative-munada","ya-al-mutakallim"],
      "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ.",
      "«my people» — the trimmed construct: the speaker's ya is gone and its kasra stands witness — the رَبِّ shape, one noun over.",
      "«kavmim» — kısaltılmış izâfet: mütekellim yâsı düşmüş, kesresi şahit — رَبِّ kalıbı, bir isim ötede."),
  tok("اتَّبِعُوا","ittabaa","verb",["ighal","form-viii-verbs","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«follow» — Form VIII's amr to the group.",
      "«uyun» — VIII. bâbın cemaate emri."),
  tok("الْمُرْسَلِينَ","mursal","noun",["ighal","jam-mudhakkar-salim","ism-maful"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "«the messengers» — nasb worn as a ya: the sound masculine plural.",
      "«gönderilenlere» — yâ ile nasb: cem'-i müzekker-i sâlim.",
      punct=".")],
 "jumal": [
  J("يَا قَوْمِ اتَّبِعُوا الْمُرْسَلِينَ",
    "نِدَاءٌ وَأَمْرٌ — الدَّعْوَةُ بِأَوْجَزِ لَفْظٍ.",
    "The call at its shortest: my people, follow.",
    "Davetin en kısası: kavmim, uyun."),
  J("قَوْمِ",
    "مُنَادًى حُذِفَتْ يَاؤُهُ وَبَقِيَتِ الْكَسْرَةُ.",
    "One kasra doing a dropped letter's work.",
    "Düşmüş bir harfin işini gören tek kesre.")]})

# ----------- s6 — Ya-Sin 36:21: the aya's ighal
S.append({"id": "s6", "translation": {
 "en": "Follow those who ask you no wage — and THEY ARE RIGHTLY GUIDED (36:21). The argument was complete at «no wage»; the seal adds the second urging: ighal, say those who deny it is poetry's alone.",
 "tr": "Sizden ücret istemeyenlere uyun — VE ONLAR HİDÂYET ÜZEREDİRLER (36:21). Delil «ücret istemez»de tamamdı; mühür ikinci teşviki ekler: îgāl şiire mahsus değildir diyenlerin şahidi."},
 "tokens": [
  tok("اتَّبِعُوا","ittabaa","verb",["ighal","form-viii-verbs","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — كُرِّرَ لِلْحَثِّ.",
      "«follow» — repeated from the last aya: the urging climbs.",
      "«uyun» — önceki âyetten tekrar: teşvik tırmanır."),
  tok("مَنْ","man-mawsula","pron",["ighal","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "«those who» — the relative as object.",
      "«o kimselere ki» — mef'ûl makamında mevsûl."),
  tok("لَا","la-nafiya","part",["ighal"],
      "نَافِيَةٌ.",
      "«not» —",
      "«-mez» —"),
  tok("يَسْأَلُكُمْ","saala","verb",["ighal","mafulayn"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ هُوَ، وَكُمْ مَفْعُولٌ أَوَّلُ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "«asks you» — the sila clause; سَأَلَ takes two objects and «you» is the first.",
      "«sizden ister» — sıla cümlesi; سَأَلَ iki mef'ûl alır, «siz» birincisidir.",
      segments=[seg("يَسْأَلُ","saala","verb"), seg("كُمْ","pron-2mp","pron")]),
  tok("أَجْرًا","ajr","noun",["ighal","mafulayn"],
      "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.",
      "«a wage» — the second object: sincerity's proof.",
      "«bir ücret» — ikinci mef'ûl: samimiyetin delili."),
  tok("وَهُمْ","hum","pron",["ighal","anwa-al-waw","hal"],
      "الْوَاوُ حَالِيَّةٌ، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«while they» — the hal waw opens the sealing clause.",
      "«hem onlar» — hâl vâvı mühür cümlesini açar.",
      segments=[seg("وَ","wa","part"), seg("هُمْ","hum","pron")]),
  tok("مُهْتَدُونَ","muhtadin","noun",["ighal","jam-mudhakkar-salim","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ، وَالْجُمْلَةُ حَالٌ — وَهِيَ الْإِيغَالُ عِنْدَ مَنْ لَمْ يَقْصُرْهُ عَلَى الشِّعْرِ.",
      "«rightly guided» — the aya's seal: follow them for their honesty — and besides, they are guided. The scholars who let ighal into prose point here.",
      "«hidâyet üzeredirler» — âyetin mührü: dürüstlükleri için uyun — üstelik hidâyettedirler. Îgāli nesre de sokan âlimlerin işaret ettiği yer.",
      punct=".")],
 "jumal": [
  J("اتَّبِعُوا مَنْ لَا يَسْأَلُكُمْ أَجْرًا وَهُمْ مُهْتَدُونَ",
    "أَمْرٌ وَصِلَتُهُ وَحَالٌ — وَفِي الْحَالِ الْإِيغَالُ.",
    "The aya's argument, complete without its seal — and stronger with it.",
    "Âyetin delili mühürsüz de tamam — mühürle daha güçlü."),
  J("وَهُمْ مُهْتَدُونَ",
    "خَتْمُ الْكَلَامِ بِزِيَادَةِ التَّرْغِيبِ — شَاهِدُ مَنْ عَمَّمَ الْإِيغَالَ.",
    "For urging on top of proof: the witness that ighal is not poetry's alone.",
    "Delil üstüne teşvik: îgālin şiire mahsus olmadığının şahidi.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "itamma": g("اِئْتَمَّ", "أ م م", "verb", "to take as leader, follow (with بِ)", "uymak, imam edinmek (بِ ile)", 5, form="VIII"),
 "sakhr": g("صَخْر", "ص خ ر", "propn", "Sakhr (al-Khansa's brother)", "Sahr (Hansâ'nın kardeşi)", 4),
 "hadin": g("هَادٍ", "ه د ي", "noun", "guide (ism fa'il, manqus)", "yol gösteren, rehber (mankus)", 4, plural="هُدَاة"),
 "alam": g("عَلَم", "ع ل م", "noun", "mountain, landmark; banner", "dağ, nişan; sancak", 4, plural="أَعْلَام"),
 "ayn-eye": g("عَيْن", "ع ي ن", "noun", "eye", "göz", 1, plural="عُيُون"),
 "wahsh": g("وَحْش", "و ح ش", "noun", "wild animals (oryx, gazelle)", "yaban hayvanları (yaban sığırı, ceylan)", 4, plural="وُحُوش"),
 "hawl": g("حَوْل", "ح و ل", "noun", "around (zarf)", "etraf, çevre (zarf)", 2),
 "khiba": g("خِبَاء", "خ ب ي", "noun", "tent", "çadır", 4, plural="أَخْبِيَة"),
 "rahl": g("رَحْل", "ر ح ل", "noun", "saddle; travel gear", "semer; yol takımı", 4, plural="أَرْحُل"),
 "jaz": g("جَزْع", "ج ز ع", "noun", "onyx beads (black and white)", "göz boncuğu (siyah-beyaz Yemen boncuğu)", 5),
 "thaqqaba": g("ثَقَّبَ", "ث ق ب", "verb", "to pierce, bore through", "delmek", 4, form="II"),
 "ittabaa": g("اِتَّبَعَ", "ت ب ع", "verb", "to follow", "uymak, tâbi olmak", 2, form="VIII"),
 "mursal": g("مُرْسَل", "ر س ل", "noun", "one sent, messenger (ism maf'ul)", "gönderilen, resûl (ism-i mef'ûl)", 3, plural="مُرْسَلُونَ"),
 "ajr": g("أَجْر", "أ ج ر", "noun", "wage, reward", "ücret, ecir", 2, plural="أُجُور"),
 "muhtadin": g("مُهْتَدٍ", "ه د ي", "noun", "rightly guided (ism fa'il of اِهْتَدَى)", "hidâyette olan (اِهْتَدَى'nın ism-i fâili)", 4, plural="مُهْتَدُونَ"),
 "ras": copy_gloss("kitab-al-kaffarat", "ras"),
 "ka-anna": copy_gloss("wasiyyat-abi-hanifa-samti", "ka-anna"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/41.json").write_text(
    json.dumps({"chapter": 41, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 41 for c in man["chapters"]):
    man["chapters"].append({"n": 41, "title": TITLE41})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.41.0"
ADD_EN = (" Chapter 41 carries ighal (lines ~2843-2855, sahifa 98): s5-s6 are Ya-Sin 36:20-21 "
          "(part), received Qur'anic text quoted exactly in standard imla as the source prints "
          "them; s1-s2 are al-Khansa's bayt on Sakhr and s3-s4 Imru' al-Qays's onyx-eyes bayt, "
          "as the source recites them, each split at the hemistich per the package's "
          "precedent.")
ADD_TR = (" Kırk birinci bâb îgāli taşır (satır ~2843-2855, sahife 98): s5-s6 Yâsîn 36:20-21 "
          "(kısmen) — kaynağın bastığı standart imlâ ile aynen alınmış mervî Kur'ân metni; "
          "s1-s2 Hansâ'nın Sahr beyti, s3-s4 İmruülkays'ın boncuk-gözler beyti — kaynağın "
          "okuduğu şekliyle, paketin teâmülünce mısra başından bölünmüştür.")
if "2843-2855" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "itamma" not in mo["verbs"]:
    # Form VIII geminate: اِئْتَمَّ يَأْتَمُّ — the contracted stems written
    # out (the ظَنَّ road inside bab iftial), the whole entry through idgham.
    mo["verbs"]["itamma"] = _sg.idgham(_sg.entry(
        _sg.B8 + " — مُضَاعَفٌ", _sg.W8,
        "اِئْتِمَام", "مُؤْتَمّ",
        _sg.mazi14("اِئْتَمّ", "اِئْتَمَم"),
        _sg.mudari14("َ", "أْتَمّ", "أْتَمِم"),
        ["اِئْتَمَّ", "اِئْتَمَّا", "اِئْتَمُّوا", "اِئْتَمِّي", "اِئْتَمَّا", "اِئْتَمِمْنَ"],
        "يَأْتَمَّ", "يَأْتَمَّ", "تَأْتَمَّ",
        None, None, None,
        "مُضَاعَفٌ مِنْ بَابِ الِافْتِعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَأْتَمَّ، وَيَجُوزُ لَمْ يَأْتَمِمْ."))
if "thaqqaba" not in mo["verbs"]:
    mo["verbs"]["thaqqaba"] = _sg.derived(
        _sg.B2, _sg.W2, "ُ", "ثَقَّب", "ثَقِّب", "ثَقِّب",
        "تَثْقِيب", "مُثَقِّب", "مُثَقَّب", "ثُقِّبَ", "يُثَقَّبُ")
if "ittabaa" not in mo["verbs"]:
    # Form VIII of a mithal root on the اِتَّصَلَ road: the waw of تَبِعَ...
    # no — تَبِعَ is sound; the ta doubles by iftial's own ta.
    mo["verbs"]["ittabaa"] = _sg.derived(
        _sg.B8, _sg.W8, "َ", "اِتَّبَع", "تَّبِع", "اِتَّبِع",
        "اِتِّبَاع", "مُتَّبِع", "مُتَّبَع", "اُتُّبِعَ", "يُتَّبَعُ")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 145
GR = ROOT / "content/grammar"
NOTE145 = {
 "id": "ighal",
 "title": {"ar": "الْإِيغَالُ",
           "en": "Ighal — the far-reaching seal",
           "tr": "Îgāl — uzağa varan mühür"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإطناب: الإيغال"],
 "question": {
  "en": ["Is the meaning COMPLETE before the speech's last words — and do those words still add a point? That is ighal: خَتْمُ الْبَيْتِ بِمَا يُفِيدُ نُكْتَةً يَتِمُّ الْمَعْنَى بِدُونِهَا.",
         "What does the seal add? More mubalagha (Khansa's fire on the mountain), or tahqiq of the likeness (the unpierced bead), or more urging (36:21's وَهُمْ مُهْتَدُونَ)?",
         "Is ighal poetry's alone? Some said yes — it is the BAYT that is sealed; others brought Ya-Sin 36:21 and let it into prose."],
  "tr": ["Sözün son kelimelerinden ÖNCE mânâ tamam mı — ve o kelimeler yine de bir nükte katıyor mu? Îgāl budur: خَتْمُ الْبَيْتِ بِمَا يُفِيدُ نُكْتَةً يَتِمُّ الْمَعْنَى بِدُونِهَا.",
         "Mühür ne katar? Mübâlağa fazlası (Hansâ'nın dağ başındaki ateşi), teşbihin tahkîki (delinmemiş boncuk), yahut teşvik fazlası (36:21'in وَهُمْ مُهْتَدُونَ'u)?",
         "Îgāl şiire mi mahsus? Kimi evet dedi — mühürlenen BEYİTTİR; kimi Yâsîn 36:21'i getirip nesre de soktu."]},
 "plain": {
  "en": "The fourth occasion of itnab: seal the speech with what the meaning could stand without — and let the seal earn its place. Khansa's mountain needed no fire, but the fire magnifies; the onyx needed no «unpierced», but the bound verifies; «and they are guided» was not needed, but it urges twice.",
  "tr": "Itnâbın dördüncü sebebi: sözü, mânânın onsuz da ayakta duracağı bir şeyle mühürle — ve mühür yerini hak etsin. Hansâ'nın dağı ateşsiz de dağdı, ama ateş büyütür; boncuğa «delinmemiş» gerekmezdi, ama kayıt doğrular; elçilerin dürüstlüğü «hem hidâyettedirler»siz de yeterdi, ama mühür iki kez teşvik eder.",},
 "explanation": {
  "en": "IGHAL — from «going very far» — is defined by some scholars as خَتْمُ الْبَيْتِ بِمَا يُفِيدُ نُكْتَةً يَتِمُّ الْمَعْنَى بِدُونِهَا: sealing the bayt with what yields a point the meaning is already complete without. Al-Khansa mourns Sakhr: وَإِنَّ صَخْرًا لَتَأْتَمُّ الْهُدَاةُ بِهِ • كَأَنَّهُ عَلَمٌ — the likening to a mountain is complete — فِي رَأْسِهِ نَارٌ: the beacon at the summit is the ighal, heaping mubalagha on mubalagha (a mountain is found by day; a mountain with fire is found by night too). Imru' al-Qays: كَأَنَّ عُيُونَ الْوَحْشِ حَوْلَ خِبَائِنَا وَأَرْحُلِنَا الْجَزْعُ — complete — الَّذِي لَمْ يُثَقَّبْ: the unpierced bead is the ighal, this time for TAHQIQ: a pierced bead loses its water and its likeness to a living eye; the bound makes the likening true, not merely bigger. And against those who keep ighal for the bayt's rhyme-seat, others brought قَالَ يَا قَوْمِ اتَّبِعُوا الْمُرْسَلِينَ. اتَّبِعُوا مَنْ لَا يَسْأَلُكُمْ أَجْرًا وَهُمْ مُهْتَدُونَ (36:20-21): the case for following is complete at «no wage», and وَهُمْ مُهْتَدُونَ seals it with a second urging — ighal in prose, on their reading. The seat matters: ighal lives at the END of the speech, which is what separates it from the takmil and tatmim of the coming chapter, whose surpluses sit mid-speech.",
  "tr": "ÎGĀL — «pek uzağa gitmek»ten — bazı âlimlerce şöyle tarif edilir: خَتْمُ الْبَيْتِ بِمَا يُفِيدُ نُكْتَةً يَتِمُّ الْمَعْنَى بِدُونِهَا — beyti, mânânın onsuz da tamam olduğu, fakat bir nükte ifade eden şeyle mühürlemek. Hansâ, Sahr'a ağıt yakar: وَإِنَّ صَخْرًا لَتَأْتَمُّ الْهُدَاةُ بِهِ • كَأَنَّهُ عَلَمٌ — dağa benzetme tamamdır — فِي رَأْسِهِ نَارٌ: zirvedeki işaret ateşi îgāldir; mübâlağa üstüne mübâlağa (dağ gündüz bulunur; ateşli dağ gece de bulunur). İmruülkays: كَأَنَّ عُيُونَ الْوَحْشِ حَوْلَ خِبَائِنَا وَأَرْحُلِنَا الْجَزْعُ — tamam — الَّذِي لَمْ يُثَقَّبْ: delinmemiş boncuk îgāldir, bu kez TAHKÎK için: delinen boncuğun suyu kaçar, canlı göze benzerliği bozulur; kayıt benzetmeyi büyütmez, doğrular. Îgāli beytin kafiye oturağına hasredenlere karşı başkaları şu âyeti getirdi: قَالَ يَا قَوْمِ اتَّبِعُوا الْمُرْسَلِينَ. اتَّبِعُوا مَنْ لَا يَسْأَلُكُمْ أَجْرًا وَهُمْ مُهْتَدُونَ (36:20-21): uyma delili «ücret istemez»de tamamdır; وَهُمْ مُهْتَدُونَ ikinci bir teşvikle mühürler — onların okuyuşunca nesirde îgāl. Oturak mühimdir: îgāl sözün SONUNDA yaşar; gelecek bâbın tekmîl ve tetmîmi ise fazlalarını söz ortasına koyar.",},
 "examples": [
  {"ar": "كَأَنَّهُ عَلَمٌ فِي رَأْسِهِ نَارٌ",
   "en": "Khansa's seal: mubalagha heaped higher.",
   "tr": "Hansâ'nın mührü: mübâlağa bir kat daha.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "الْجَزْعُ الَّذِي لَمْ يُثَقَّبْ",
   "en": "Imru' al-Qays's seal: the likeness verified.",
   "tr": "İmruülkays'ın mührü: benzetme doğrulanır.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "وَهُمْ مُهْتَدُونَ",
   "en": "the aya's seal (36:21): urging on top of proof — ighal in prose.",
   "tr": "âyetin mührü (36:21): delil üstüne teşvik — nesirde îgāl.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«Mânâ tamamlandıysa gerisi fazlalıktır, atılmalıdır»",
   "right": "«Sona gelen fazlalık bir nükte taşıyorsa ÎGĀLDİR ve sözü süsler»",
   "why": {"en": "The ijaz bab taught that surplus without benefit is tatwil; ighal is the licensed surplus — its seat is the very end, and its licence is the nukta: more mubalagha, a verified likeness, a doubled urging. Cut Khansa's fire and the bayt survives; keep it and the bayt burns.",
           "tr": "Îcâz bâbı faydasız fazlalığın tatvîl olduğunu öğretti; îgāl ruhsatlı fazlalıktır — oturağı sözün tâ sonu, ruhsatı nüktedir: mübâlağa fazlası, doğrulanmış benzetme, katlanmış teşvik. Hansâ'nın ateşini kes, beyit yaşar; bırak, beyit yanar."}}],
 "relatedNotes": ["asbab-al-itnab", "ijaz-itnab-musawat", "tashbih", "inna-wa-akhawatuha",
                  "vocative-munada", "jam-mudhakkar-salim", "hal"]}

(GR / "ighal.json").write_text(
    json.dumps(NOTE145, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch41:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + itamma/thaqqaba/ittabaa; note 145")
