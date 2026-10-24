# -*- coding: utf-8 -*-
"""Author chapter 12 of talkhis-al-miftah — تَقْوِيَةُ الْحُكْمِ وَالتَّخْصِيصُ.

The second half of taqdim, and the fine one: the SAME word order sometimes
confines (takhsis) and sometimes merely strengthens (taqwiyat al-hukm), and
the books give the tests that tell them apart.

هُوَ يُعْطِي الْجَزِيلَ strengthens and does NOT confine — no claim that others
give little. With a negated verb the two readings split on ʿAbd al-Qāhir's
axis: أَنْتَ مَا سَعَيْتَ فِي حَاجَتِي (pronoun BEFORE the negation) is takhsis —
qasr qalb or ifrad — while أَنْتَ لَا تَكْذِبُ is taqwiya, and the book grades
the three ways of saying it: أَنْتَ لَا تَكْذِبُ is the STRONGEST because it
carries TWO isnads (khabar to mubtada, verb to fa'il); لَا تَكْذِبُ has one;
لَا تَكْذِبُ أَنْتَ has one plus a mere tawkid of the concealed pronoun.
Counting the isnads is the whole doctrine.

Then the indefinite subject: رَجُلٌ جَاءَنِي confines the genus or the unit
(qasr qalb against «a woman», qasr ifrad against «two men») — and Sakkākī's
khilāf: he demands that the fronted subject be estimable as a delayed fāʿil,
reads رَجُلٌ جَاءَنِي as بَدَل from the concealed pronoun on the model of
وَأَسَرُّوا النَّجْوَى الَّذِينَ ظَلَمُوا, and the ʿArabs' proverb شَرٌّ أَهَرَّ
ذَا نَابٍ stands as the test case — the nahw scholars read it as a qasr
(مَا أَهَرَّ ذَا نَابٍ إِلَّا شَرٌّ) and Sakkākī saves his rule by reading the
tanwin as taʿẓīm. Last, مِثْلُكَ لَا يَبْخَلُ — the taʿrīḍ construction: «one
like you is not stingy» said to the hearer about someone else.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~977-1060: the four
prose examples with their gradation, رَجُلٌ جَاءَنِي with its two taqdirs,
al-Anbiya 21:3, the proverb with its taʾwīl, and مِثْلُكَ لَا يَبْخَلُ.
Nothing is composed.

Grammar this chapter is chosen to teach (and FEED):
  • note 114 `taqwiyat-al-hukm` — the takhsis/taqwiya tests, the two-isnad
    gradation, and Sakkaki's khilaf, with the madrasah question test.
  • `qasr` gains the proverb with the nahw scholars' own taʾwīl; `badal`
    gains a kind chapter 10 could not show — badal from a PRONOUN.
  • أَسَرُّوا and أَهَرَّ — Form IV geminates, generated from أَحَلَّ's stored
    pattern by root substitution; كَذَبَ and بَخِلَ — new sound paradigms.
  • the engine work the probe forced: the group-waw's silent alif in
    IrabSign, the naqis radical ya un-peeled (يُعْطِي), the فَعْلَى row
    (نَجْوَى), the mim-kasra refusal (مِثْل), and Abd al-Qahir's second frame
    in MaEngine (أَنْتَ مَا سَعَيْتَ — person agreement kills the sila).
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
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
S = []

TITLE12 = {"ar": "تَقْوِيَةُ الْحُكْمِ وَالتَّخْصِيصُ",
           "en": "Strengthening the Ruling, or Confining It — the Same Word Order, Two Works",
           "tr": "Takviyetü'l-Hüküm ve Tahsîs — Aynı Söz Dizimi, İki İş"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "HE gives abundantly. (Strengthened — and no claim at all that others do not.)",
 "tr": "O, bol bol verir. (Hüküm kuvvetlenmiştir — başkaları vermez, denmemiştir.)"},
 "tokens": [
  tok("هُوَ","huwa","pron",["taqwiyat-al-hukm","mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَتَقْدِيمُهُ هُنَا لِتَقْوِيَةِ الْحُكْمِ لَا لِلتَّخْصِيصِ.",
      "A detached pronoun, mabni, in the position of raf' as the mubtada — and its fronting here STRENGTHENS the ruling without confining it. «He gives abundantly» does not whisper that others give little; the sentence simply lands twice. This is the reading takhsis-hunters miss, and the book opens the chapter with it for exactly that reason.",
      "Munfasıl zamir; mebnîdir, mübtedâ olarak mahallen merfûdur — ve buradaki takdîmi TAHSÎS için değil, HÜKMÜ KUVVETLENDİRMEK içindir. «O bol bol verir», başkaları az verir diye fısıldamaz; cümle sadece iki kere yerleşir. Tahsîs avcılarının kaçırdığı okuyuş budur ve kitap bâbı tam bu sebeple onunla açar."),
  tok("يُعْطِي","aata","verb",["fa-khabar-mubtada","form-iv-verbs","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَفَاعِلُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ. وَبِهَذَا الْإِسْنَادِ الثَّانِي تَحْصُلُ التَّقْوِيَةُ.",
      "A Form IV naqis mudari', its raf' a damma ESTIMATED on the ya as too heavy; the fa'il concealed — and the clause is the khabar. Here is the machinery of taqwiya laid bare: the sentence now carries TWO isnads — the clause to the pronoun, the verb to its own fa'il — and a ruling ascribed twice sits harder than one ascribed once. (And that final ya is a RADICAL, the third letter of ع ط و; the app's peel once took it for an object pronoun.)",
      "Form IV nâkıs muzâri; ref'i, ağırlık sebebiyle yâ üzerinde TAKDÎR edilen dammedir; fâili müstetirdir — cümle haberdir. Takviyenin mekanizması burada apaçıktır: cümle artık İKİ isnâd taşır — cümlenin zamire, fiilin kendi fâiline isnâdı — ve iki kere isnâd edilen hüküm, bir kere edilenden sağlam oturur. (O son yâ da ASLÎ harftir, ع ط و'nun üçüncüsü; uygulamanın soyucusu onu bir zamanlar mef'ûl zamiri sanmıştı.)"),
  tok("الْجَزِيلَ","jazil","noun",["maful-bihi","sifa-mushabbaha"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — صِفَةٌ عَلَى فَعِيلٍ نَابَتْ عَنِ الْمَوْصُوفِ، أَيِ الْعَطَاءَ الْجَزِيلَ.",
      "The object, in nasb — an adjective on فَعِيل standing in for its dropped noun: «the abundant [gift]». The ellipsis is itself a small taqwiya — the quality is so known it needs no bearer named.",
      "Mansub mef'ûlün bih — mevsûfunun yerine geçmiş فَعِيل vezninde bir sıfat: «bol [ihsan]». Bu hazif de küçük bir takviyedir — vasıf o kadar bilinir ki taşıyıcısının adı gerekmez.",
      punct=".")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "It was not YOU who laboured in my need. (The pronoun stands before the negation: a takhsis — of reversal or of singling-out.)",
 "tr": "Benim işimde çalışan SEN değildin. (Zamir nefiyden öncedir: kalb yahut ifrâd kasrıyla tahsîs.)"},
 "tokens": [
  tok("أَنْتَ","anta","pron",["taqwiyat-al-hukm","taqdim-al-musnad-ilayh","mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — قُدِّمَ وَالنَّفْيُ بَعْدَهُ، فَأَفَادَ التَّخْصِيصَ: قَصْرَ قَلْبٍ أَوْ قَصْرَ إِفْرَادٍ.",
      "The mubtada, fronted with the negation AFTER it — ʿAbd al-Qāhir's second frame, the mirror of مَا أَنَا قُلْتُ. Because the pronoun does not follow the ma, the takhsis reads the other way: «it was not YOU who laboured» — qasr QALB if the hearer credited you instead of the true worker, qasr IFRAD if he believed you both laboured. Which of the two is meant, only the hearer's prior belief decides.",
      "Mübtedâ; öne alınmış ve nefiy ARDINDAdır — Abdülkāhir'in ikinci kalıbı, «مَا أَنَا قُلْتُ»nun aynası. Zamir mâyı takip etmediği için tahsîs öbür yöne okunur: «çalışan SEN değildin» — muhâtab işi gerçek çalışanın yerine sana mâl ettiyse kasr-ı KALB, ikinizin birlikte çalıştığına inanıyorduysa kasr-ı İFRÂD. İkisinden hangisi, yalnız muhâtabın önceki zannıyla belli olur."),
  tok("مَا","ma-nafiya","part",["ma-la-mushabbaha","taqwiyat-al-hukm"],
      "حَرْفُ نَفْيٍ — وَالْفِعْلُ بَعْدَهُ يُوَافِقُ الضَّمِيرَ فِي الشَّخْصِ، فَالْجُمْلَةُ خَبَرٌ لَا صِلَةٌ.",
      "The negation — and note what the analyzer now reads off the surface: the verb after it AGREES IN PERSON with the pronoun (the ta of سَعَيْتَ is the same «you»), so the clause is the khabar, not a sila. A relative's clause carries a third-person ʿaid; a second-person verb has no seat for one.",
      "Nefiy harfi — ve analizörün artık yüzeyden okuduğuna dikkat: ardındaki fiil zamirle ŞAHISTA uyuşur («سَعَيْتَ»nin tâsı aynı «sen»dir), öyleyse cümle sıla değil haberdir. Mevsûlün cümlesi üçüncü şahıs bir âid taşır; ikinci şahıs fiilde ona yer yoktur."),
  tok("سَعَيْتَ","saa-verb","verb",["fail","fa-khabar-mubtada"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "The mazi, mabni on the sukun, its ta the fa'il — the clause standing in raf' as the khabar.",
      "Mâzî; sükûn üzere mebnîdir, tâ fâildir — cümle, haber olarak mahallen merfûdur.",
      segments=[seg("سَعَيْ","saa-verb","verb"), seg("تَ","pron-2ms","pron")]),
  tok("فِي","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "حَرْفُ جَرٍّ، مُتَعَلِّقٌ بِـ«سَعَيْتَ»، لَغْوٌ.",
      "A jarr letter; the phrase attaches to «laboured» — laghw.",
      "Cer harfi; terkîb «سَعَيْتَ»ye taalluk eder — lağvdır."),
  tok("حَاجَتِي","haja","noun",["huruf-jarr","ya-al-mutakallim","idafa-definiteness"],
      "مَجْرُورٌ بِكَسْرَةٍ ظَاهِرَةٍ عَلَى التَّاءِ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ — وَتَاؤُهُ تَاءُ التَّأْنِيثِ الْمَرْبُوطَةُ انْبَسَطَتْ قَبْلَ الضَّمِيرِ.",
      "Majrur by a kasra written on the ta, annexed to the speaker's ya — and that ta is the MARBUTA unrolled before the pronoun (حَاجَة ← حَاجَتِي). A verb's feminine-ta can never stand here: a verb reaching the speaker's ya takes the nun of protection first, so a ta before a bare possessive ya is always the noun's.",
      "Tâ üzerinde yazılı kesra ile mecrûr; mütekellim yâsına muzâftır — ve o tâ, zamirden önce AÇILMIŞ tâ-i merbûtadır (حَاجَة ← حَاجَتِي). Fiilin te'nîs tâsı burada asla duramaz: mütekellim yâsına ulaşan fiil önce vikāye nûnunu alır; öyleyse çıplak mülkiyet yâsından önceki tâ dâima ismindir.",
      segments=[seg("حَاجَتِ","haja","noun"), seg("ي","pron-1s","pron")],
      punct=".")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "YOU do not lie. — Do not lie, you. (The first is the strongest of the three ways to say it: it carries two ascriptions.)",
 "tr": "SEN yalan söylemezsin. — Yalan söylemezsin, sen. (Birincisi üç söyleyişin en kuvvetlisidir: iki isnâd taşır.)"},
 "tokens": [
  tok("أَنْتَ","anta","pron",["taqwiyat-al-hukm","mubtada-khabar"],
      "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — قُدِّمَ لِتَقْوِيَةِ الْحُكْمِ: إِسْنَادُ الْجُمْلَةِ إِلَيْهِ وَإِسْنَادُ الْفِعْلِ إِلَى فَاعِلِهِ إِسْنَادَانِ.",
      "The mubtada — and here the fronting STRENGTHENS: «YOU do not lie» denies the lying harder than لَا تَكْذِبُ alone, because it carries TWO isnads where the bare verb carries one. The negation is ascribed to you twice: once as the clause to its mubtada, once as the verb to its fa'il. Count the isnads and the gradation of the three sentences falls out by arithmetic.",
      "Mübtedâ — ve buradaki takdîm KUVVETLENDİRİR: «SEN yalan söylemezsin», yalanı yalın «لَا تَكْذِبُ»dan daha şiddetle nefyeder; çünkü yalın fiil bir isnâd taşırken bu İKİ isnâd taşır. Nefiy sana iki kere isnâd edilir: bir kere cümle mübtedâsına, bir kere fiil fâiline. İsnâdları say — üç cümlenin derecelenmesi aritmetikle çıkar."),
  tok("لَا","la-nafiya","part",["la-nahiya","taqwiyat-al-hukm"],
      "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ فِي الْمُضَارِعِ.",
      "The negating la, governing nothing in the mudari'.",
      "Nefiy lâsı; muzâride amel etmez."),
  tok("تَكْذِبُ","kadhaba","verb",["mudari-marfu","fa-khabar-mubtada"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «أَنْتَ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A mudari' in raf', its fa'il the concealed «you» — the clause standing as the khabar, and the second of the two isnads.",
      "Merfû muzâri; fâili müstetir «أَنْتَ»dir — cümle haber olarak mahallen merfûdur ve iki isnâdın ikincisidir.",
      punct="."),
  tok("لَا","la-nafiya","part",["la-nahiya"],
      "حَرْفُ نَفْيٍ.",
      "The negating la again — and now watch the same three words in the other order.",
      "Yine nefiy lâsı — şimdi aynı üç kelimeyi öbür sırayla izle."),
  tok("تَكْذِبُ","kadhaba","verb",["mudari-marfu","taqwiyat-al-hukm"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَفَاعِلُهُ مُسْتَتِرٌ — إِسْنَادٌ وَاحِدٌ لَا غَيْرُ.",
      "The same verb — but standing first, it is the WHOLE predication: one isnad, no more. This is the middle strength.",
      "Aynı fiil — fakat başta dururken isnâdın TAMAMI odur: tek isnâd, fazlası yok. Orta kuvvet budur."),
  tok("أَنْتَ","anta","pron",["tawkid","taqwiyat-al-hukm"],
      "تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ فِي «تَكْذِبُ» — لَا إِسْنَادَ ثَانِيَ هُنَا، فَلَا تَقْوِيَةَ.",
      "NOT a mubtada this time: the sentence was already complete at تَكْذِبُ, so this anta only CONFIRMS the pronoun concealed in the verb — a tawkid of the mahkum-alayh, not a second ascription of the ruling. One isnad plus an emphasis is weaker than two isnads: the book's gradation, read off the syntax alone.",
      "Bu sefer mübtedâ DEĞİL: cümle «تَكْذِبُ»da zâten tamamlanmıştı; öyleyse bu «أَنْتَ», fiilde gizli zamiri yalnız PEKİŞTİRİR — hükmün ikinci isnâdı değil, mahkûmun aleyhin te'kîdidir. Bir isnâd artı bir te'kîd, iki isnâddan zayıftır: kitabın derecelenmesi, yalnız nahivden okunur.",
      punct=".")],
 "jumal": [
  J("أَنْتَ لَا تَكْذِبُ",
    "جُمْلَةٌ اسْمِيَّةٌ، خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ — فَفِيهَا إِسْنَادَانِ.",
    "A nominal sentence whose khabar is itself a verbal clause — so it carries TWO ascriptions, and that arithmetic is the whole doctrine of taqwiya.",
    "Haberi fiil cümlesi olan isim cümlesi — öyleyse İKİ isnâd taşır; takviyenin bütün doktrini bu aritmetiktir."),
  J("لَا تَكْذِبُ أَنْتَ",
    "جُمْلَةٌ فِعْلِيَّةٌ، وَ«أَنْتَ» تَوْكِيدٌ لِلْفَاعِلِ الْمُسْتَتِرِ — إِسْنَادٌ وَاحِدٌ.",
    "A verbal sentence; the trailing pronoun is a tawkid of the concealed fa'il — one ascription only, so no taqwiya however emphatic it sounds.",
    "Fiil cümlesi; sondaki zamir, müstetir fâilin te'kîdidir — tek isnâd; ne kadar vurgulu dursa da takviye yoktur.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "A man came to me. — And they whispered — those who do wrong — their secret talk.",
 "tr": "Bana bir adam geldi. — Gizlediler — o zulmedenler — fısıltılarını."},
 "tokens": [
  tok("رَجُلٌ","rajul","noun",["taqwiyat-al-hukm","tankir-al-musnad-ilayh","mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ سَوَّغَ الِابْتِدَاءَ بِهَا قَصْدُ التَّخْصِيصِ: جِنْسًا أَوْ وَاحِدًا.",
      "The mubtada, in raf' — INDEFINITE, and licensed to open the sentence by the very takhsis it performs. Fronted before its verb it confines the GENUS or the UNIT: against a hearer who believed a woman came, the taqdir is رَجُلٌ جَاءَنِي لَا امْرَأَةٌ (qasr qalb); against one who believed two men came, لَا رَجُلَانِ (qasr ifrad). One sentence, two corrections, and the hearer's error picks between them.",
      "Merfû mübtedâ — NEKREdir ve cümleye başlamasını, bizzat yaptığı tahsîs meşrû kılar. Fiilinden önce alınınca CİNSİ yahut TEKİ kasreder: gelenin kadın olduğuna inanan muhâtaba karşı takdîr «رَجُلٌ جَاءَنِي لَا امْرَأَةٌ»dur (kasr-ı kalb); iki adam geldi sanana karşı «لَا رَجُلَانِ» (kasr-ı ifrâd). Tek cümle, iki tashîh; aralarında muhâtabın hatası seçer."),
  tok("جَاءَنِي","jaa","verb",["ya-al-mutakallim","fa-khabar-mubtada"],
      "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ. وَعِنْدَ السَّكَّاكِيِّ: «رَجُلٌ» بَدَلٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِيهِ.",
      "The mazi with the nun of protection and the speaker's ya as object — the clause the khabar. And here Sakkākī enters: for him the fronting only confines if the subject can be ESTIMATED as a delayed fa'il, so he reads رَجُلٌ as a BADAL from the pronoun concealed in جَاءَنِي — on the model of the aya that follows. ʿAbd al-Qāhir needs no such machinery; the khilaf is real and the chapter shows both.",
      "Vikāye nûnu ve mef'ûl olan mütekellim yâsıyla mâzî — cümle haberdir. Ve burada Sekkâkî girer: ona göre takdîm ancak özne, sonraya bırakılmış fâil TAKDÎR edilebilirse kasreder; bu yüzden «رَجُلٌ»u, «جَاءَنِي»de gizli zamirden BEDEL okur — ardından gelen âyetin modeliyle. Abdülkāhir'in böyle bir çarka ihtiyacı yoktur; hilâf gerçektir ve bâb ikisini de gösterir.",
      segments=[seg("جَاءَ","jaa","verb"), seg("نِي","ni-wiqaya","pron")],
      punct="."),
  tok("وَأَسَرُّوا","asarra","verb",["fail","form-iv-verbs","doubled-verbs"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَ«أَسَرُّوا» فِعْلٌ مَاضٍ مُضَاعَفٌ مِنَ الْإِفْعَالِ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ عَلَى الْمَشْهُورِ.",
      "«And they hid» — a Form IV geminate mazi, built on the damm for the group's waw, and that waw is the fa'il on the common reading. The alif after it is the silent alif of separation, which the app's sign engine once read as a maqsur's ending.",
      "«Ve gizlediler» — if'âl bâbından muzâaf mâzî; cemâat vâvına bitiştiği için zamme üzere mebnîdir ve meşhur okuyuşta o vâv fâildir. Ardındaki elif, okunmayan fârika elifidir — uygulamanın alâmet motoru onu bir zamanlar maksûr sonu sanmıştı.",
      segments=[seg("وَ","wa","conj"), seg("أَسَرُّوا","asarra","verb")]),
  tok("النَّجْوَى","najwa","noun",["maful-bihi","ism-maqsur-manqus"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَأَلِفُهُ أَلِفُ التَّأْنِيثِ الْمَقْصُورَةُ (فَعْلَى مِنْ ن ج و).",
      "The object, its fatha ESTIMATED on the alif — and that alif is the feminine alif of فَعْلَى (root ن ج و), which is why the word finally has its own row in the peel table instead of answering «Form VII».",
      "Mef'ûlün bih; fethası elif üzerinde TAKDÎRÎdir — ve o elif, فَعْلَى'nın (kök ن ج و) te'nîs elifidir; kelimenin soyma tablosunda artık «Form VII» yerine kendi satırının olmasının sebebi budur."),
  tok("الَّذِينَ","alladhina","pron",["badal","ism-mawsul","taqwiyat-al-hukm"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ بَدَلٌ مِنْ وَاوِ الْجَمَاعَةِ — بَدَلُ اسْمٍ ظَاهِرٍ مِنْ ضَمِيرٍ.",
      "The relative, mabni, in the position of raf' as a BADAL FROM THE WAW — a plain noun standing in apposition to a PRONOUN, the kind chapter 10's three examples could not show. This aya is Sakkākī's model: the fa'il appears first as a pronoun, then again as the noun that unpacks it, and he reads رَجُلٌ جَاءَنِي the same way.",
      "Mebnî ism-i mevsûl; cemâat VÂVINDAN BEDEL olarak mahallen merfûdur — bir ZAMİRDEN açık isim bedeli; onuncu bâbın üç misalinin gösteremediği nevi. Bu âyet Sekkâkî'nin modelidir: fâil önce zamir olarak, sonra onu açan isim olarak görünür; o, «رَجُلٌ جَاءَنِي»yi de böyle okur."),
  tok("ظَلَمُوا","zalama","verb",["jumla-sifa","fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "«Did wrong» — mabni on the damm, its waw the fa'il, the clause the sila with no position.",
      "«Zulmettiler» — zamme üzere mebnî; vâvı fâildir, cümle sıladır ve mahalli yoktur.",
      punct=".")],
 "jumal": [
  J("وَأَسَرُّوا النَّجْوَى الَّذِينَ ظَلَمُوا",
    "جُمْلَةٌ فِعْلِيَّةٌ، وَفِيهَا بَدَلُ الظَّاهِرِ مِنَ الضَّمِيرِ.",
    "A verbal sentence carrying the badal of a plain noun from a pronoun — Sakkaki's model for every fronted indefinite subject.",
    "Zamirden açık isim bedeli taşıyan fiil cümlesi — Sekkâkî'nin öne alınmış her nekre özne için modeli.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "Evil — and only evil — makes the fanged one snarl. — One like you is not stingy.",
 "tr": "Dişli olanı ancak bir ŞER hırlatır. — Senin gibi biri cimrilik etmez."},
 "tokens": [
  tok("شَرٌّ","sharr","noun",["taqwiyat-al-hukm","qasr","tankir-al-musnad-ilayh"],
      "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ، وَالنُّحَاةُ أَوَّلُوهُ بِالْقَصْرِ: مَا أَهَرَّ ذَا نَابٍ إِلَّا شَرٌّ. وَعِنْدَ السَّكَّاكِيِّ تَنْوِينُهُ لِلتَّعْظِيمِ.",
      "The mubtada, indefinite and fronted — and the ʿArabs' own proverb is the chapter's test case. The nahw scholars read it as a QASR outright, with the taʾwil مَا أَهَرَّ ذَا نَابٍ إِلَّا شَرٌّ: nothing makes the fanged one snarl but an evil. Sakkākī, whose two conditions the sentence strains, saves his rule by reading the TANWIN as taʿẓīm — «a mighty evil» — confining the KIND where the genus and the unit resist. One proverb, two schools, and the divergence is stated rather than smoothed.",
      "Merfû mübtedâ — nekre ve öne alınmış; Arabların kendi meselî, bâbın imtihan cümlesidir. Nahivciler onu doğrudan KASR okur, te'vîli de «مَا أَهَرَّ ذَا نَابٍ إِلَّا شَرٌّ»dur: dişliyi ancak bir şer hırlatır. İki şartı bu cümlede zorlanan Sekkâkî ise kāidesini, TENVÎNİ ta'zîm okuyarak kurtarır — «büyük bir şer» — cins ile ferdin direndiği yerde NEV'İ kasreder. Tek mesel, iki mektep; ve ayrılık düzlenmek yerine söylenmiştir."),
  tok("أَهَرَّ","aharra","verb",["fa-khabar-mubtada","form-iv-verbs","doubled-verbs"],
      "فِعْلٌ مَاضٍ مُضَاعَفٌ مِنَ الْإِفْعَالِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَفَاعِلُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.",
      "«Made snarl» — a Form IV geminate (أَهَرَّ يُهِرُّ, the أَحَلَّ pattern), its fa'il concealed, the clause the khabar.",
      "«Hırlattı» — if'âl bâbından muzâaf (أَهَرَّ يُهِرُّ, «أَحَلَّ» kalıbı); fâili müstetirdir, cümle haberdir."),
  tok("ذَا","dhu","noun",["five-nouns","maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ.",
      "The object, in nasb BY THE ALIF — one of the five nouns (ذُو، ذَا، ذِي: «possessor of»), and a mudaf by its very nature: it never stands without an annexation. Not the demonstrative, though the letters match — a demonstrative is never mudaf, and the bare majrur after this word is the annexation's own signature.",
      "Mef'ûlün bih; esmâ-i hamseden olduğu için ELİFLE mansubdur (ذُو، ذَا، ذِي: «sâhibi») ve tabiatı gereği muzâftır: izâfetsiz hiç durmaz. Harfleri tutsa da işaret ismi değildir — işaret ismi asla muzâf olmaz ve bu kelimeden sonraki çıplak mecrûr, izâfetin kendi imzasıdır."),
  tok("نَابٍ","nab","noun",["idafa-definiteness","five-nouns"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — «صَاحِبُ نَابٍ»: الْكَلْبُ وَنَحْوُهُ.",
      "The mudaf ilayh, in jarr — «possessor of a fang»: the dog and its kin, named by the tooth rather than the species, which is half the proverb's bite.",
      "Mecrûr muzâfun ileyh — «diş sâhibi»: köpek ve benzeri; türüyle değil dişiyle adlandırılmıştır, meselin ısırığının yarısı budur.",
      punct="."),
  tok("مِثْلُكَ","mithl","noun",["taqwiyat-al-hukm","mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ وَالْكَافُ مُضَافٌ إِلَيْهِ — وَالْمُرَادُ الْمُخَاطَبُ نَفْسُهُ: تَعْرِيضٌ.",
      "The mubtada, a mudaf with the kaf annexed — and the person meant is the HEARER himself: «one like you is not stingy» is التَّعْرِيض, saying it slant. The construction lets the speaker praise (or warn) without the bluntness of أَنْتَ, and the books file it here because the fronting is what carries the slant. (Root م ث ل — the mim is RADICAL; the app's peel table once answered «ث ل ك».)",
      "Merfû mübtedâ; muzâftır ve kâf muzâfun ileyhtir — kastedilen ise MUHÂTABIN kendisidir: «senin gibi biri cimrilik etmez», TA'RÎZdir, yandan söylemek. Terkîb, mütekellime «أَنْتَ»nin kabalığı olmadan övme (yahut uyarma) imkânı verir; kitapların onu buraya koyması, imâyı taşıyanın takdîm olmasındandır. (Kök م ث ل — mîm ASLÎdir; uygulamanın soyma tablosu bir zamanlar «ث ل ك» demişti.)",
      segments=[seg("مِثْلُ","mithl","noun"), seg("كَ","pron-2ms","pron")]),
  tok("لَا","la-nafiya","part",["la-nahiya"],
      "حَرْفُ نَفْيٍ.",
      "The negating la.",
      "Nefiy lâsı."),
  tok("يَبْخَلُ","bakhila","verb",["mudari-marfu","fa-khabar-mubtada"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.",
      "«Is not stingy» — a mudari' in raf', its fa'il concealed, the clause the khabar. Said of «one like you», meant of you: the sentence teaches that word order can carry even a courtesy.",
      "«Cimrilik etmez» — merfû muzâri; fâili müstetirdir, cümle haberdir. «Senin gibin» için söylenir, sen kastedilirsin: cümle, söz diziminin bir nezâketi bile taşıyabildiğini öğretir.",
      punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "jazil":    g("جَزِيل", "ج ز ل", "noun", "abundant, ample", "bol, cezîl", 4),
 "najwa":    g("نَجْوَى", "ن ج و", "noun", "secret talk, whispering", "fısıltı, gizli konuşma, necvâ", 4),
 "nab":      g("نَاب", "ن ي ب", "noun", "fang, canine tooth", "azı dişi, köpek dişi", 4, plural="أَنْيَاب"),
 "kadhaba":  g("كَذَبَ", "ك ذ ب", "verb", "to lie", "yalan söylemek", 2, form="I"),
 "bakhila":  g("بَخِلَ", "ب خ ل", "verb", "to be stingy", "cimrilik etmek", 3, form="I"),
 "asarra":   g("أَسَرَّ", "س ر ر", "verb", "to hide, to keep secret", "gizlemek, sır tutmak", 3, form="IV"),
 "aharra":   g("أَهَرَّ", "ه ر ر", "verb", "to make snarl", "hırlatmak", 5, form="IV"),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "aata":     g("أَعْطَى", "ع ط و", "verb", "to give", "vermek", 2, form="IV"),
 "zalama":   g("ظَلَمَ", "ظ ل م", "verb", "to wrong, to oppress", "zulmetmek", 2, form="I"),
 "sharr":    g("شَرّ", "ش ر ر", "noun", "evil (its hamza dropped like خَيْر's)", "şer, kötülük (hemzesi خَيْر gibi düşmüş)", 2, plural="شُرُور"),
 "mithl":    g("مِثْل", "م ث ل", "noun", "the like of (always a mudaf)", "gibi, benzeri (dâima muzâf)", 2),
 "dhu":      g("ذُو", None, "noun", "possessor of (one of the five nouns; always a mudaf)", "sâhibi (esmâ-i hamseden; dâima muzâf)", 3),
 "la-nafiya": g("لَا (النَّافِيَة)", None, "part", "not (negating the mudari')", "…mez (muzâriyi nefyeden lâ)", 1),
}

def build_morph():
    """Two Form IV geminates generated from أَحَلَّ's stored pattern by root
    substitution — the pattern is identical (sound letters, the أَحَلَّ jazm
    bil-fath) so the substitution is mechanical, and it is done in ONE pass
    with a callback because chained .replace() cascades. Plus two new sound
    paradigms and two lemma-identical copies."""
    out = {}
    for pkg, lex in [("wasiyyat-abi-hanifa-samti", "aata"),
                     ("kitab-al-waqf", "zalama")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    ahalla = json.loads((ROOT / "content/samples/kitab-al-sulh/morphology.json").read_text(encoding="utf-8"))["verbs"]["ahalla"]
    def subst(obj, table):
        s = json.dumps(obj, ensure_ascii=False)
        s = re.sub("|".join(map(re.escape, table)), lambda m: table[m.group(0)], s)
        return json.loads(s)
    out["asarra"] = subst(ahalla, {"ح": "س", "ل": "ر"})
    out["asarra"]["masdar"] = "إِسْرَار"
    out["aharra"] = subst(ahalla, {"ح": "ه", "ل": "ر"})
    out["aharra"]["masdar"] = "إِهْرَار"
    # the substitution touches every string, including the bab/wazn labels
    # (their فعل scale carries a ل) and the note's own prose — restore the
    # labels wholesale and write each verb's note fresh with its own forms.
    for k, jz in (("asarra", "يُسِرَّ/يُسْرِرْ"), ("aharra", "يُهِرَّ/يُهْرِرْ")):
        out[k]["bab"] = ahalla["bab"]; out[k]["wazn"] = ahalla["wazn"]
        a, b = jz.split("/")
        out[k]["note"] = f"مُضَاعَفٌ مِنَ الْإِفْعَالِ عَلَى مِثَالِ أَحَلَّ: الْجَزْمُ بِالْفَتْحِ — لَمْ {a}، وَيَجُوزُ لَمْ {b}."
    # كَذَبَ يَكْذِبُ — bab ضَرَبَ.
    out["kadhaba"] = _sg.sound1("daraba", "كَذَب", "كْذِب", "اِكْذِب", "كَذِب", "كَاذِب",
                                "مَكْذُوب", "كُذِبَ", "يُكْذَبُ")
    # بَخِلَ يَبْخَلُ — bab سَمِعَ.
    out["bakhila"] = _sg.sound1("samia", "بَخِل", "بْخَل", "اِبْخَل", "بُخْل", "بَاخِل",
                                None, None, None)
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/12.json").write_text(
    json.dumps({"chapter": 12, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 12 for c in man["chapters"]):
    man["chapters"].append({"n": 12, "title": TITLE12})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.12.0"
ADD_EN = (" Chapter 12 continues from the same file (lines ~977-1060), which carries every one of its "
          "examples vowelled: هُوَ يُعْطِي الْجَزِيلَ, أَنْتَ مَا سَعَيْتَ فِي حَاجَتِي, the graded triple "
          "أَنْتَ لَا تَكْذِبُ / لَا تَكْذِبُ / لَا تَكْذِبُ أَنْتَ, رَجُلٌ جَاءَنِي with its two taqdirs, al-Anbiya 21:3, "
          "the Arabs' proverb شَرٌّ أَهَرَّ ذَا نَابٍ with the nahw scholars' ta'wil and Sakkaki's answer, and "
          "مِثْلُكَ لَا يَبْخَلُ.")
ADD_TR = (" On ikinci bâb aynı dosyadan (satır ~977-1060) devam eder; o satırlar bâbın bütün misallerini "
          "harekeli olarak taşır: هُوَ يُعْطِي الْجَزِيلَ, أَنْتَ مَا سَعَيْتَ فِي حَاجَتِي, dereceli üçlü "
          "أَنْتَ لَا تَكْذِبُ / لَا تَكْذِبُ / لَا تَكْذِبُ أَنْتَ, iki takdîriyle رَجُلٌ جَاءَنِي, Enbiyâ 21:3, "
          "nahivcilerin te'vîli ve Sekkâkî'nin cevâbıyla Arabların meselî شَرٌّ أَهَرَّ ذَا نَابٍ, ve "
          "مِثْلُكَ لَا يَبْخَلُ.")
if "977-1060" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch12:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
