# -*- coding: utf-8 -*-
"""Author chapter 25 of talkhis-al-miftah — هَلْ: بَسِيطَةٌ وَمُرَكَّبَةٌ، وَمَا وَمَنْ.

The istifham bab continues (sahifa 71-72):

  • هَلْ leans to the FI'L more than the hamza does — the source argues it
    on the aya: فَهَلْ أَنْتُمْ شَاكِرُونَ (Anbiya 21:80) presses the demand
    for thanks harder than فَهَلْ تَشْكُرُونَ (showing the coming deed as
    done) AND harder than أَفَأَنْتُمْ شَاكِرُونَ (dropping the verb beside
    the verb-hungry هَلْ presses further). Hence هَلْ زَيْدٌ مُنْطَلِقٌ sits
    well only in an eloquent mouth.
  • هَلْ splits into BASITA — the existence of the thing itself is asked
    (هَلِ الْحَرَكَةُ مَوْجُودَةٌ) — and MURAKKABA — the existence of a thing
    FOR a thing (هَلِ الْحَرَكَةُ دَائِمَةٌ: motion conceded, its duration
    weighed).
  • مَا asks the NAME's explanation or the THING's essence (مَا الْعَنْقَاءُ),
    and the books order the four questions with hal basita standing between
    the two ma's; Sakkaki adds the JINS-ask (مَا عِنْدَكَ — answered «a
    book»).
  • مَنْ asks the PERSON of the one endowed with knowledge (مَنْ فِي
    الدَّارِ) — a name answers, never a yes.

ATTRIBUTION: فَهَلْ أَنْتُمْ شَاكِرُونَ is received Qur'anic text quoted
exactly (al-Anbiya 21:80, cited by the source for this doctrine); every
other sentence is the source's own worked example verbatim
(research/sources/talkhis-al-miftah-balagha.txt lines ~2044-2085, sahifa
71-72), Ottoman plain-alif normalized to standard orthography — a
recorded normalization.

Grammar this chapter teaches:
  • note 127 `hal-ma-man` — hal's fi'l-affinity, basita/murakkaba, the
    four-question ladder, ma's three asks, man's person-ask.
  • engine work: the nominal-hal frames (basita/murakkaba split on the
    mawjud-khabar, the fi'l-affinity frame on a pronoun subject), the
    ma/man ask-frames read off the analyzer's own ism-face decision,
    MaEngine's sentence-final zarf-phrase question, and مَنْ the ism
    carrying its OWN pk (the jarr key no longer rides the fatha-mim row).
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/talkhis-al-miftah"
sys.path.insert(0, str(ROOT / "tools/authoring"))
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

TITLE25 = {"ar": "هَلِ الْبَسِيطَةُ وَالْمُرَكَّبَةُ — وَمَا وَمَنْ",
           "en": "Hal Basita and Murakkaba — and Ma and Man",
           "tr": "Basîta ve Mürekkebe Hel — Mâ ve Men"}

# ------------------------------------------------- s1 — Anbiya 21:80
S.append({"id": "s1", "translation": {
 "en": "So are you thankful? (al-Anbiya 21:80 — hal leans to the verb, so the NOMINAL after it works hardest: the aya outdoes both its rewrites.)",
 "tr": "Şükreder misiniz? (Enbiyâ 21:80 — هَلْ fiile meyleder; bu yüzden ardındaki İSİM CÜMLESİ en çok iş görür: âyet iki yeniden-yazımından da üstündür.)"},
 "tokens": [
  tok("فَهَلْ","hal","part",["hal-ma-man","al-istifham"],
      "الْفَاءُ عَاطِفَةٌ وَ«هَلْ» حَرْفُ اسْتِفْهَامٍ — وَهِيَ أَشَدُّ اقْتِضَاءً لِلْفِعْلِ مِنَ الْهَمْزَةِ.",
      "«so are…?» — the fa joins, and هَلْ asks. The doctrine this aya carries: هَلْ demands the VERB more than the hamza does — its bond to time is plainer — so what follows here is a deliberate choice.",
      "«peki …misiniz?» — fâ atfeder, هَلْ sorar. Âyetin taşıdığı doktrin: هَلْ, FİİLİ hemzeden daha çok ister — zamana bağı daha açıktır — öyleyse burada ardından gelen, bilinçli bir seçimdir.",
      segments=[seg("فَ","fa","part"), seg("هَلْ","hal","part")]),
  tok("أَنْتُمْ","antum","pron",["hal-ma-man"],
      "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.",
      "«you» — the detached pronoun as mubtada: a NOMINAL sentence handed to the verb-hungry هَلْ. Dropping the verb beside the particle that demands it presses the demand — the aya outdoes أَفَأَنْتُمْ شَاكِرُونَ for exactly this reason.",
      "«siz» — munfasıl zamir, mübtedâ: fiile aç هَلْ'e İSİM CÜMLESİ verilmiştir. Fiili, onu isteyen edatın yanında düşürmek talebi bastırır — âyetin أَفَأَنْتُمْ شَاكِرُونَ'dan üstünlüğü tam da bundandır."),
  tok("شَاكِرُونَ","shakir","noun",["hal-ma-man","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — اسْمُ فَاعِلٍ مِنْ شَكَرَ.",
      "«thankful» — the khabar, raf' by the WAW of the sound plural; the ism fa'il of شَكَرَ. Beside فَهَلْ تَشْكُرُونَ this shows the coming thanks as a STANDING QUALITY — the done shown for the doing — which is the second edge the source counts for the aya's wording.",
      "«şükredenler» — haber, sâlim cem'in VÂVIyla merfû; شَكَرَ'nın ism-i fâili. فَهَلْ تَشْكُرُونَ'un yanında bu, gelecek şükrü YERLEŞİK BİR VASIF olarak gösterir — olacağın olmuş gösterilmesi — kaynağın âyetin lafzına saydığı ikinci üstünlük budur.",
      punct="؟")],
 "jumal": [
  J("فَهَلْ أَنْتُمْ شَاكِرُونَ",
    "هَلْ أَشَدُّ طَلَبًا لِلْفِعْلِ مِنَ الْهَمْزَةِ — فَالْجُمْلَةُ الِاسْمِيَّةُ بَعْدَهَا أَبْلَغُ.",
    "The COMPARISON LADDER the source builds: the aya > فَهَلْ تَشْكُرُونَ (the future shown as done presses the demand) > أَفَأَنْتُمْ شَاكِرُونَ (only hal's verb-hunger makes the dropped verb tell). Three wordings, one meaning, ranked — balagha as engineering.",
    "Kaynağın kurduğu KARŞILAŞTIRMA MERDİVENİ: âyet > فَهَلْ تَشْكُرُونَ (gelecek olmuş gösterilince talep bastırılır) > أَفَأَنْتُمْ شَاكِرُونَ (düşürülen fiili ancak hel'in fiil açlığı konuşturur). Üç lafız, tek mânâ, sıralanmış — mühendislik olarak belâgat."),
  J("فَهَلْ أَنْتُمْ شَاكِرُونَ",
    "وَلِهَذَا: هَلْ زَيْدٌ مُنْطَلِقٌ لَا يَحْسُنُ إِلَّا مِنَ الْبَلِيغِ.",
    "The corollary: a plain nominal after هَلْ (هَلْ زَيْدٌ مُنْطَلِقٌ) sits well only in an ELOQUENT mouth — the ordinary speaker should give هَلْ its verb. A refusal graded by the speaker, not by the grammar: the sentence is sound, and marked.",
    "Netice: هَلْ'den sonra yalın isim cümlesi (هَلْ زَيْدٌ مُنْطَلِقٌ) ancak BELÎĞ ağzında güzel durur — sıradan konuşan هَلْ'e fiilini vermelidir. Gramerin değil konuşanın derecelendirdiği bir çekince: cümle sahihtir ve işaretlidir.")]})

# ------------------------------------------------- s2 — hal basita
S.append({"id": "s2", "translation": {
 "en": "Is motion existent? (HAL BASITA — the existence of the thing itself is asked.)",
 "tr": "Hareket mevcut mu? (BASÎTA هَلْ — şeyin bizzat varlığı sorulur.)"},
 "tokens": [
  tok("هَلِ","hal","part",["hal-ma-man"],
      "حَرْفُ اسْتِفْهَامٍ — كُسِرَتْ لَامُهَا لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«is…?» — هَلْ with a KASRA on its lam: its sukun meets the silent alif of the article, and two sukuns will not stand — the iltiqa as-sakinayn repair, the same kasra as دَفَّتَيِ الْمُصْحَفِ.",
      "«… mu?» — lâmı KESRALI هَلْ: sükûnu, harf-i tarifin sessiz elifiyle karşılaşır ve iki sükûn bir arada durmaz — iltikā-i sâkineyn tamiri; دَفَّتَيِ الْمُصْحَفِ'teki kesranın aynısı."),
  tok("الْحَرَكَةُ","haraka","noun",["hal-ma-man"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "«motion» — the mubtada, marfu'; the thing whose very BEING is on trial.",
      "«hareket» — mübtedâ, merfû; bizzat VARLIĞI yargılanan şey."),
  tok("مَوْجُودَةٌ","mawjud","noun",["hal-ma-man"],
      "خَبَرٌ مَرْفُوعٌ — وَكَوْنُ الْخَبَرِ «مَوْجُود» هُوَ عَلَامَةُ الْبَسِيطَةِ.",
      "«existent» — the khabar; and THIS khabar is the basita's own tell: when what is predicated is bare EXISTENCE, the question is basita — يُطْلَبُ بِهَا وُجُودُ الشَّيْءِ.",
      "«mevcut» — haber; ve BU haber, basîtanın kendi işaretidir: yüklenen şey çıplak VARLIK olduğunda soru basîtadır — يُطْلَبُ بِهَا وُجُودُ الشَّيْءِ.",
      punct="؟")],
 "jumal": [
  J("هَلِ الْحَرَكَةُ مَوْجُودَةٌ",
    "هَلِ الْبَسِيطَةُ: يُطْلَبُ بِهَا وُجُودُ الشَّيْءِ نَفْسِهِ.",
    "BASITA: nothing is yet conceded — the subject itself may not be. The answer settles whether there is a thing at all, before any quality of it can be weighed.",
    "BASÎTA: henüz hiçbir şey teslim edilmemiştir — öznenin kendisi olmayabilir. Cevap, herhangi bir vasfı tartılmadan önce ortada bir şey olup olmadığını karara bağlar."),
  J("هَلِ الْحَرَكَةُ مَوْجُودَةٌ",
    "كَسْرَةُ «هَلِ» لِالْتِقَاءِ السَّاكِنَيْنِ — لَا إِعْرَابَ لِحَرْفٍ.",
    "The kasra on هَلِ is REPAIR, not i'rab — a harf takes none; two silences met and one bent. The reader who parses that kasra as a case has read a particle as a noun.",
    "هَلِ'deki kesra TAMİRdir, i'râb değil — harf i'râb almaz; iki sükûn karşılaştı ve biri eğildi. O kesrayı hâl okuyan, harfi isim okumuş demektir.")]})

# ------------------------------------------------- s3 — hal murakkaba
S.append({"id": "s3", "translation": {
 "en": "Is motion perpetual? (HAL MURAKKABA — motion's being is conceded; a further predicate is weighed.)",
 "tr": "Hareket dâimî mi? (MÜREKKEBE هَلْ — hareketin varlığı teslim edilmiş; ilâve bir yüklem tartılıyor.)"},
 "tokens": [
  tok("هَلِ","hal","part",["hal-ma-man"],
      "حَرْفُ اسْتِفْهَامٍ مَكْسُورٌ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«is…?» — the same repaired هَلِ; and the same particle now asks a DIFFERENT kind of question, told apart only by the khabar.",
      "«… mi?» — aynı tamirli هَلِ; ve aynı edat şimdi BAŞKA tür bir soru sorar — yalnız haberden ayırt edilir."),
  tok("الْحَرَكَةُ","haraka","noun",["hal-ma-man"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَوُجُودُهَا مُسَلَّمٌ هُنَا.",
      "«motion» — the mubtada again, but its EXISTENCE is now conceded: s2 asked whether it is; this sentence starts from the yes.",
      "«hareket» — yine mübtedâ, fakat VARLIĞI artık teslim: s2 var mı diye sordu; bu cümle evet'ten başlar."),
  tok("دَائِمَةٌ","daim","noun",["hal-ma-man"],
      "خَبَرٌ مَرْفُوعٌ — وَكَوْنُهُ غَيْرَ «مَوْجُود» هُوَ عَلَامَةُ الْمُرَكَّبَةِ.",
      "«perpetual» — the khabar, and NOT the bare «existent»: a further thing is predicated OF an existing subject — يُطْلَبُ بِهَا وُجُودُ شَيْءٍ لِشَيْءٍ. One word swapped, and the question changes kind.",
      "«dâimî» — haber ve çıplak «mevcut» DEĞİL: var olan bir özne İÇİN ilâve bir şey yüklenir — يُطْلَبُ بِهَا وُجُودُ شَيْءٍ لِشَيْءٍ. Tek kelime değişti ve soru tür değiştirdi.",
      punct="؟")],
 "jumal": [
  J("هَلِ الْحَرَكَةُ دَائِمَةٌ",
    "هَلِ الْمُرَكَّبَةُ: يُطْلَبُ بِهَا وُجُودُ شَيْءٍ لِشَيْءٍ.",
    "MURAKKABA: the being of the subject is off the table; what its predicate holds is on it. s2 and s3 are a MINIMAL PAIR — the same particle, the same subject, and the khabar alone flips the kind.",
    "MÜREKKEBE: öznenin varlığı masadan kalkmıştır; yüklemin tuttuğu masadadır. s2 ile s3 ASGARÎ ÇİFTtir — aynı edat, aynı özne; türü yalnız haber çevirir."),
  J("هَلِ الْحَرَكَةُ دَائِمَةٌ",
    "وَتَقَعُ الْبَسِيطَةُ بَيْنَ «مَا» الشَّارِحَةِ وَ«مَا» الْحَقِيقِيَّةِ فِي التَّرْتِيبِ.",
    "The FOUR-QUESTION LADDER the books recite: ma of the name → hal basita → ma of the essence → hal murakkaba. One asks the word, one the being, one the essence, one the qualities — inquiry itself given a grammar.",
    "Kitapların okuduğu DÖRT SORU MERDİVENİ: ismin mâsı → basîta هل → mâhiyet mâsı → mürekkebe هل. Biri kelimeyi, biri varlığı, biri mâhiyeti, biri vasıfları sorar — sorgulamanın kendisine gramer verilmiş.")]})

# ------------------------------------------------- s4 — ma of the name
S.append({"id": "s4", "translation": {
 "en": "What is the anqa? (MA before a definite noun: the NAME's explanation is asked — or the essence; the surface cannot split the two.)",
 "tr": "Ankā nedir? (Marife isimden önce MÂ: İSMİN şerhi sorulur — yahut mâhiyet; yüzey ikisini ayıramaz.)"},
 "tokens": [
  tok("مَا","ma-istifham","pron",["hal-ma-man","anwa-ma"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.",
      "«what» — the interrogative MA, a mabni ISM standing as fronted khabar. Before a definite noun it asks the NAME's explanation (what does «anqa» mean?) or the THING's essence — and only the asker's state, never the page, tells which.",
      "«ne» — istifham MÂ'sı; mukaddem haber olarak duran mebnî bir İSİM. Marife isimden önce İSMİN şerhini (« ankā» ne demektir?) yahut ŞEYİN mâhiyetini sorar — hangisini sorduğunu sayfa değil, yalnız soranın hâli söyler."),
  tok("الْعَنْقَاءُ","anqa","noun",["hal-ma-man"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.",
      "«the anqa» — the deferred mubtada, marfu'. The books choose a FABLED bird on purpose: for a thing with no existence, only its NAME can be explained — which is why the name-ask comes first on the ladder.",
      "«ankā» — muahhar mübtedâ, merfû. Kitaplar MASAL kuşunu bilerek seçer: varlığı olmayan şeyin ancak ADI şerh edilebilir — isim sorusunun merdivende önce gelmesi bundandır.",
      punct="؟")],
 "jumal": [
  J("مَا الْعَنْقَاءُ",
    "مَا: يُطْلَبُ بِهَا شَرْحُ الِاسْمِ أَوْ مَاهِيَّةُ الْمُسَمَّى.",
    "MA'S TWO ASKS, taught on one bird: of the anqa — which does not exist — only the name can be explained; ask مَا الْحَرَكَةُ after hal basita's yes and the SAME word demands the essence. The ladder's order carries the difference the surface cannot.",
    "MÂ'NIN İKİ SORUSU, tek kuşta öğretilir: var olmayan ankānın ancak adı şerh edilir; basîta هل'in evet'inden sonra مَا الْحَرَكَةُ deyin, AYNI kelime mâhiyeti ister. Yüzeyin taşıyamadığı farkı merdivenin sırası taşır."),
  J("مَا الْعَنْقَاءُ",
    "وَعِنْدَ السَّكَّاكِيِّ: يُسْأَلُ بِمَا عَنِ الْجِنْسِ أَوِ الْوَصْفِ — مَا عِنْدَكَ، مَا زَيْدٌ.",
    "Sakkaki widens ma's field: it may ask the JINS (مَا عِنْدَكَ — answered «a book» or its kind) or the DESCRIPTION (مَا زَيْدٌ — what is Zayd like?). Three asks on one particle, all answered by names, never by yes.",
    "Sekkâkî mânın sahasını genişletir: CİNSİ sorabilir (مَا عِنْدَكَ — «kitap» yahut türü cevaplar) yahut VASFI (مَا زَيْدٌ — Zeyd nasıl biridir?). Tek edatta üç soru; hepsi isimle cevaplanır, asla evet'le değil.")]})

# ------------------------------------------------- s5 — man
S.append({"id": "s5", "translation": {
 "en": "Who is in the house? (MAN asks the PERSON — a name or a distinguishing mark answers, never a yes.)",
 "tr": "Evde kim var? (MEN, KİŞİYİ sorar — bir isim yahut ayırt edici bir vasıf cevaplar, asla evet değil.)"},
 "tokens": [
  tok("مَنْ","man-istifham","pron",["hal-ma-man","anwa-ma"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْمِيمُ مَفْتُوحَةٌ.",
      "«who» — the interrogative MAN, a mabni ism as mubtada; the FATHA on the mim is what tells it from the jarr letter مِنْ. It asks for the PERSON: a name (زَيْدٌ) or a mark that singles him out.",
      "«kim» — istifham MEN'i; mübtedâ olarak mebnî bir isim; onu cer harfi مِنْ'den ayıran, mîmdeki FETHAdır. KİŞİYİ ister: bir ad (زَيْدٌ) yahut onu tek başına gösteren bir vasıf."),
  tok("فِي","fi","part",["hal-ma-man","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in» — the jarr letter opening the khabar's phrase.",
      "«-de» — haberin öbeğini açan cer harfi."),
  tok("الدَّارِ","dar","noun",["hal-ma-man"],
      "مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "«the house» — majrur; the jarr-phrase stands as the khabar, and the whole sentence waits for a person's name.",
      "«ev» — mecrur; câr-mecrûr haber olarak durur ve bütün cümle bir kişinin adını bekler.",
      punct="؟")],
 "jumal": [
  J("مَنْ فِي الدَّارِ",
    "مَنْ: يُطْلَبُ بِهَا تَعْيِينُ ذِي الْعِلْمِ — عَلَمُهُ أَوْ وَصْفٌ يَخُصُّهُ.",
    "MAN = the person-ask: what is sought is the KNOWER's name or a mark that is his alone. Beside ma's thing-asks and hal's yes/no, the tasawwur particles now divide the world between them — each with its own answer-shape.",
    "MEN = kişi sorusu: aranan, İLİM SAHİBİnin adı yahut yalnız ona ait bir vasıftır. Mânın şey-soruları ile hel'in evet/hayır'ının yanında tasavvur edatları artık dünyayı aralarında bölüşür — her birinin kendi cevap-kalıbı vardır."),
  J("مَنْ فِي الدَّارِ",
    "فَتْحَةُ الْمِيمِ هِيَ الْفَيْصَلُ — وَمَنِ اسْمٌ فِي كُلِّ وُجُوهِهَا.",
    "One vowel splits two words: kasra on the mim is the jarr LETTER, fatha the ISM — and مَنْ is a noun in every one of its faces (question, condition, relative), never a harf. The analyzer's oldest split, here in its home bab.",
    "Tek hareke iki kelimeyi ayırır: mîmde kesra cer HARFİdir, fetha İSİM — ve مَنْ bütün vecihlerinde (soru, şart, mevsûl) isimdir, asla harf değil. Çözümleyicinin en eski ayrımı, burada kendi bâbında.")]})

# ------------------------------------------------- s6 — ma of the jins
S.append({"id": "s6", "translation": {
 "en": "What is with you? (Sakkaki's jins-ask: the answer is «a book» or its kind — and no negation can stand where the sentence holds nothing to deny.)",
 "tr": "Yanında ne var? (Sekkâkî'nin cins sorusu: cevap «kitap» yahut türüdür — cümlede inkâr edilecek bir şey yokken nefiy duramaz.)"},
 "tokens": [
  tok("مَا","ma-istifham","pron",["hal-ma-man","anwa-ma"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«what» — the interrogative ma as mubtada; and the shape itself rules the negation out: a sentence that is nothing but a zarf-phrase holds no verb and no khabar for a مَا نَافِيَة to deny. The question is not merely likelier — the alternative has nothing to stand on.",
      "«ne» — mübtedâ olarak istifham mâsı; ve kalıbın kendisi nefyi dışlar: yalın zarf öbeğinden ibaret bir cümlede, nefiy mâsının inkâr edeceği ne fiil ne haber vardır. Soru yalnız daha muhtemel değildir — alternatifin basacağı yer yoktur."),
  tok("عِنْدَكَ","inda","noun",["hal-ma-man"],
      "«عِنْدَ» ظَرْفٌ مَنْصُوبٌ مُضَافٌ وَالْكَافُ مُضَافٌ إِلَيْهِ — وَشِبْهُ الْجُمْلَةِ خَبَرٌ.",
      "«with you» — the zarf عِنْدَ, mansub and mudaf, the kaf its mudaf ilayh; the phrase stands as khabar. Sakkaki reads the ask as the JINS: the answer names a KIND — «a book» — not a yes and not an individual.",
      "«yanında» — zarf عِنْدَ, mansub ve muzâf; kâf muzâfun ileyhtir; öbek haber olarak durur. Sekkâkî soruyu CİNS okur: cevap bir TÜR adlandırır — «kitap» — ne evet ne de bir fert.",
      punct="؟")],
 "jumal": [
  J("مَا عِنْدَكَ",
    "سُؤَالُ الْجِنْسِ عِنْدَ السَّكَّاكِيِّ — وَجَوَابُهُ «كِتَابٌ» وَنَحْوُهُ.",
    "THE JINS-ASK: of all that is with you, WHICH KIND is there? The answer-shape is the diagnosis — a kind-name, where man demands a person and hal takes a yes. Ask the answer's shape and the particle names itself.",
    "CİNS SORUSU: yanındakilerden HANGİ TÜR var? Cevap-kalıbı teşhisin kendisidir — tür adı; men kişi ister, hel evet alır. Cevabın kalıbını sorun, edat kendini adlandırır."),
  J("مَا عِنْدَكَ",
    "لَا مَجَالَ لِلنَّفْيِ: لَا فِعْلَ وَلَا خَبَرَ مَنْصُوبَ تَنْفِيهِ مَا.",
    "Why the negation cannot compete: مَا النَّافِيَة needs a clause to deny — a verb, or a mubtada with its khabar. A bare zarf-phrase ending the sentence offers neither, so the reading is excluded by STRUCTURE, not by taste.",
    "Nefyin yarışamamasının sebebi: مَا النَّافِيَة inkâr edecek bir cümle ister — bir fiil yahut haberli bir mübtedâ. Cümleyi bitiren yalın zarf öbeği ikisini de sunmaz; okuma zevkle değil YAPIyla dışlanır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "shakir": copy_gloss("wasiyyat-abi-hanifa-l4", "shakir"),
 "mawjud": copy_gloss("aqaid-ahl-al-sunna", "mawjud"),
 "haraka": g("حَرَكَة", "ح ر ك", "noun", "motion, movement", "hareket", 3, plural="حَرَكَات"),
 "anqa": g("عَنْقَاء", "ع ن ق", "noun", "the anqa — the fabled bird (a name with no named)",
           "ankā — masal kuşu (adlandırılanı olmayan bir ad)", 5),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/25.json").write_text(
    json.dumps({"chapter": 25, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 25 for c in man["chapters"]):
    man["chapters"].append({"n": 25, "title": TITLE25})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.25.0"
ADD_EN = (" Chapter 25 continues the istifham bab from the same file (lines ~2044-2085, sahifa 71-72): "
          "فَهَلْ أَنْتُمْ شَاكِرُونَ is received Qur'anic text quoted exactly (al-Anbiya 21:80, cited by "
          "the source for hal's fi'l-affinity); هَلِ الْحَرَكَةُ مَوْجُودَةٌ / دَائِمَةٌ, مَا الْعَنْقَاءُ, "
          "مَنْ فِي الدَّارِ and مَا عِنْدَكَ are the source's own worked examples verbatim, Ottoman "
          "plain-alif normalized to standard orthography — a recorded normalization.")
ADD_TR = (" Yirmi beşinci bâb, istifham bâbını aynı dosyadan sürdürür (satır ~2044-2085, sahife 71-72): "
          "فَهَلْ أَنْتُمْ شَاكِرُونَ aynen alınmış mervî Kur'ân metnidir (Enbiyâ 21:80; kaynak, hel'in "
          "fiile meyli için zikreder); هَلِ الْحَرَكَةُ مَوْجُودَةٌ / دَائِمَةٌ, مَا الْعَنْقَاءُ, مَنْ فِي "
          "الدَّارِ ve مَا عِنْدَكَ kaynağın kendi işlenmiş örneklerinin aynen alınmışıdır; Osmanlı "
          "düz-elif imlâsı standart imlâya çevrilmiştir — kayıtlı bir normalizasyondur.")
if "2044-2085" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch25:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
