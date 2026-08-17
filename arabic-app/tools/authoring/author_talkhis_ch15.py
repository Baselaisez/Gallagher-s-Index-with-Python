# -*- coding: utf-8 -*-
"""Author chapter 15 of talkhis-al-miftah — أَحْوَالُ الْمُسْنَدِ: تَرْكُ الْمُسْنَدِ.

Chapter 13 closed the musnad-ilayh bab on لَا فِيهَا غَوْلٌ — «the door to the
musnad's own bab» — and chapter 14 walked the khilaf muqtada al-zahir bridge.
Here the musnad's bab OPENS, and it opens the same way the subject's did:
with omission. The musannif's rule: the musnad is dropped for the same
reasons the musnad ilayh was — but every dropping needs a QARINA, and the
chapter is really a course in reading qara'in:

  • زَيْدٌ مُنْطَلِقٌ وَعَمْرٌو — the mentioned musnad is the qarina for the
    omitted one: ikhtisar, and the avoidance of ʿabath.
  • خَرَجْتُ فَإِذَا زَيْدٌ — the fuja'iyya frame itself is the qarina: the
    maqam is too NARROW for the general verb (مَوْجُودٌ is felt, not said).
  • Qays b. al-Khatim's bayt — the siyaq supplies رَاضُونَ for the first
    half from the رَاضٍ said in the second: the musnad omitted from the
    FIRST clause and voiced in the second, the reverse of Zayd's frame.
  • فَصَبْرٌ جَمِيلٌ — the omission the mufassirun leave OPEN: read the
    mahdhuf as musnad (فَصَبْرٌ جَمِيلٌ أَجْمَلُ) or as musnad ilayh
    (فَأَمْرِي صَبْرٌ جَمِيلٌ) — the two-taqdir case, taught as two.
  • وَلَئِنْ سَأَلْتَهُمْ مَنْ خَلَقَ… لَيَقُولُنَّ اللَّهُ — the REALIZED QUESTION
    is the qarina: the answer says اللَّهُ alone and the omitted خَلَقَهُنَّ
    is heard inside it.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1337-1400 (sahifa
46-47): the two textbook frames زَيْدٌ مُنْطَلِقٌ وَعَمْرٌو and خَرَجْتُ فَإِذَا
زَيْدٌ, Qays b. al-Khatim's bayt نَحْنُ بِمَا عِنْدَنَا…, Yusuf 12:83 and
Luqman 31:25. The ayat and the bayt are received text quoted exactly.

Grammar this chapter is chosen to teach:
  • note 117 `tark-al-musnad` — omission of the predicate, its reasons and
    its qara'in, with the two-taqdir doctrine of فَصَبْرٌ جَمِيلٌ.
  • the engine work the probe forced: إِذَا الْفُجَائِيَّة (the next word's
    class decides), لَئِنْ split into the oath-paving lam + إِنْ, the heavy
    nun restored to its cell (لَيَقُولُنَّ), نَحْنُ joining PARTICLES (rule 6d
    was blind to it), the zarf-sila list completed (عِنْدَكَ), the radical
    sin of سَأَلَ (the corpus decides against the future-sin peel), the
    manqus vs hollow kasratan (the glossary decides رَاضٍ from بَابٍ), and
    the primitive masdar shapes فَعْل/فِعْل/فُعْل joining the IsmTagger.
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

TITLE15 = {"ar": "أَحْوَالُ الْمُسْنَدِ: تَرْكُ الْمُسْنَدِ",
           "en": "The States of the Musnad: Omitting the Predicate",
           "tr": "Müsnedin Hâlleri: Müsnedin Terki"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "Zayd is setting out — and ʿAmr [is too]. (The musnad of ʿAmr is omitted: the one already said is its qarina.)",
 "tr": "Zeyd yola çıkıyor — Amr da [öyle]. (Amr'ın müsnedi hazfedilmiştir: söylenmiş olan, onun karînesidir.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar","tark-al-musnad"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.",
      "The first mubtada, in raf' by the plain damma. His khabar is about to be SAID — hold it, because the sentence's second half will lean on it.",
      "İlk mübtedâ; zâhir damme ile merfû. Haberi birazdan SÖYLENECEK — aklında tut; çünkü cümlenin ikinci yarısı ona yaslanacak."),
  tok("مُنْطَلِقٌ","muntaliq","noun",["mubtada-khabar","ism-fail","form-vii-verbs","tark-al-musnad"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ انْطَلَقَ — وَهُوَ الْقَرِينَةُ عَلَى الْمَحْذُوفِ بَعْدُ.",
      "The khabar, in raf' — ism fail of the Form VII اِنْطَلَقَ. And it does double duty: said once for Zayd, it becomes the QARINA for the same musnad omitted after ʿAmr. Every hadhf must leave such a witness behind, or the hearer is left guessing at what was never recoverable.",
      "Haber, merfû — VII. bâb اِنْطَلَقَ'nın ism-i fâili. Ve çifte iş görür: Zeyd için bir kez söylenince, Amr'dan sonra hazfedilen aynı müsnedin KARÎNESİ olur. Her hazif ardında böyle bir şahit bırakmalıdır; yoksa dinleyen, geri getirilemeyecek bir şeyi tahmine bırakılmış olur."),
  tok("وَعَمْرٌو","amr-alam","propn",["mubtada-khabar","tark-al-musnad","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«عَمْرٌو» مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ — أَيْ: وَعَمْرٌو مُنْطَلِقٌ — لِلِاخْتِصَارِ وَالِاحْتِرَازِ عَنِ الْعَبَثِ.",
      "«And ʿAmr» — a second mubtada whose khabar is OMITTED: the full sentence is وَعَمْرٌو مُنْطَلِقٌ, and saying مُنْطَلِقٌ twice in one breath would be ʿabath — pointless repetition — when the first one still hangs in the air. This is the musnad's bab opening exactly as the musnad ilayh's did: with ikhtisar. (And the silent waw at the end is spelling, not sound: it tells عَمْرو from عُمَر on the page.)",
      "«Ve Amr» — haberi HAZFEDİLMİŞ ikinci mübtedâ: cümlenin tamamı وَعَمْرٌو مُنْطَلِقٌ'tur ve ilki daha havada asılıyken مُنْطَلِقٌ'u bir nefeste iki kez söylemek ABES olurdu — boş tekrar. Müsnedin bâbı, müsnedün ileyhinki gibi açılıyor: ihtisârla. (Sondaki sessiz vâv ise yazımdır, ses değil: sayfada عَمْرو'yu عُمَر'den ayırır.)",
      segments=[seg("وَ","wa","part"), seg("عَمْرٌو","amr-alam","propn")],
      punct=".")],
 "jumal": [
  J("زَيْدٌ مُنْطَلِقٌ وَعَمْرٌو",
    "حُذِفَ خَبَرُ الثَّانِي لِدَلَالَةِ الْأَوَّلِ عَلَيْهِ — اخْتِصَارًا وَاحْتِرَازًا عَنِ الْعَبَثِ.",
    "The second khabar dropped because the first one points to it — brevity, and the avoidance of saying what is already heard.",
    "İkinci haber, birincisi ona delâlet ettiği için düşürülmüştür — îcâz için ve zaten duyulanı söylemekten kaçınmak için.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "I went out — and there was Zayd! (The general musnad — «present, standing there» — is omitted: the maqam of surprise is too narrow for it.)",
 "tr": "Çıktım — bir de ne göreyim, Zeyd! (Umûmî müsned — «mevcut, duruyor» — hazfedilmiştir: sürpriz makāmı ona dardır.)"},
 "tokens": [
  tok("خَرَجْتُ","kharaja","verb",["fail","tark-al-musnad"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ.",
      "«I went out» — mazi built on the sukun for the subject-ta; the ta is the doer. An ordinary report — until the fa turns the corner.",
      "«Çıktım» — fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâildir. Sıradan bir haber — tâ ki fâ köşeyi dönene dek.",
      segments=[seg("خَرَجْ","kharaja","verb"), seg("تُ","pron-1s","pron")]),
  tok("فَإِذَا","idha-fujaiyya","part",["idha-shartiyya","tark-al-musnad"],
      "الْفَاءُ عَاطِفَةٌ، وَ«إِذَا» لِلْمُفَاجَأَةِ — تَدْخُلُ عَلَى الْجُمْلَةِ الِاسْمِيَّةِ وَلَا عَمَلَ لَهَا.",
      "«and THERE was—» — this is NOT the conditional idha: a NOUN follows it, not a verb, and that class-change is the whole diagnosis. إِذَا الْفُجَائِيَّةُ, the idha of surprise, opens a nominal sentence and governs nothing; the books dispute its essence (a harf for al-Akhfash, a zarf for al-Mubarrad) and agree on its work. The fa rides it, as it loves to.",
      "«bir de ne göreyim—» — bu, şart idhâsı DEĞİLDİR: ardından fiil değil İSİM geliyor ve bu sınıf değişimi teşhisin tamamıdır. إِذَا الْفُجَائِيَّة — ansızlık idhâsı — isim cümlesi açar ve amel etmez; mâhiyeti ihtilaflıdır (Ahfeş'e göre harf, Müberred'e göre zarf), işi ittifaklıdır. Fâ ona biner; sever bunu.",
      segments=[seg("فَ","fa","part"), seg("إِذَا","idha-fujaiyya","part")]),
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar","tark-al-musnad","hadhf-wa-taqdir"],
      "مُبْتَدَأٌ مَرْفُوعٌ خَبَرُهُ مَحْذُوفٌ وُجُوبًا — أَيْ: فَإِذَا زَيْدٌ مَوْجُودٌ — لِأَنَّ الْمَقَامَ ضَيِّقٌ.",
      "«Zayd!» — a mubtada whose khabar never comes, and the musannif names the reason with a picture: the maqam is NARROW (ضَيِّق). Surprise has no room in it for the general verb — «present», «standing there» — the fact of him is the whole news. The omitted musnad here is the colourless مَوْجُودٌ, and saying it would flatten the very jolt the fuja'iyya exists to carry.",
      "«Zeyd!» — haberi hiç gelmeyen bir mübtedâ; ve musannif sebebini bir resimle adlandırır: makām DARdır (ضَيِّق). Sürprizin içinde umûmî fiile yer yoktur — «mevcut», «orada duruyor» — onun varlığı haberin tamamıdır. Burada hazfedilen müsned renksiz مَوْجُودٌ'tur; söylemek, fücâiyyenin taşımak için var olduğu sarsıntıyı düzleştirirdi.",
      punct=".")],
 "jumal": [
  J("خَرَجْتُ فَإِذَا زَيْدٌ",
    "حُذِفَ الْمُسْنَدُ الْعَامُّ — مَوْجُودٌ — لِضِيقِ الْمَقَامِ عَنْ إِطَالَةِ الْكَلَامِ.",
    "The general musnad — «there, present» — omitted because the maqam of surprise is too narrow to stretch the speech.",
    "Umûmî müsned — «mevcut» — hazfedildi; çünkü sürpriz makāmı sözü uzatmaya dardır.")]})

# ---------------------------------------------------------------- s3 — Qays b. al-Khatim
S.append({"id": "s3", "translation": {
 "en": "We with what we hold, and you with what you hold, are content — and the two minds differ. (Qays b. al-Khatim; the first clause's musnad رَاضُونَ is omitted, heard from the رَاضٍ said in the second.)",
 "tr": "Biz elimizdekinden, sen de elindekinden hoşnutsun — ve görüşler farklıdır. (Kays b. el-Hatîm; ilk cümlenin müsnedi رَاضُونَ hazfedilmiş, ikincide söylenen رَاضٍ'den işitilir.)"},
 "tokens": [
  tok("نَحْنُ","nahnu","pron",["mubtada-khabar","tark-al-musnad"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — خَبَرُهُ مَحْذُوفٌ: رَاضُونَ.",
      "«WE» — detached pronoun as mubtada, and its khabar is the one word this bayt never says for it: رَاضُونَ. The omission runs FORWARD — the qarina comes later, in the second clause's رَاضٍ — the mirror image of Zayd's sentence, where the said one preceded. Siyaq points both ways.",
      "«BİZ» — mübtedâ olan munfasıl zamir; haberi, beytin onun için hiç söylemediği kelimedir: رَاضُونَ. Hazif İLERİYE doğru işler — karîne sonra, ikinci cümlenin رَاضٍ'sinde gelir — Zeyd cümlesinin ayna görüntüsü: orada söylenen önce gelmişti. Siyâk iki yöne de işaret eder."),
  tok("بِمَا","ma-mawsula","pron",["anwa-ma","huruf-jarr","tark-al-musnad"],
      "الْبَاءُ جَارَّةٌ وَ«مَا» مَوْصُولَةٌ فِي مَحَلِّ جَرٍّ — وَالظَّرْفُ بَعْدَهَا صِلَتُهَا.",
      "«with WHAT…» — the ba governs, and this ma is MAWSULA: the zarf عِنْدَنَا after it is its sila (a sila may be a shibh jumla — it needs only something to hang on, while a negation would need a whole clause to work on). «With that which is with us».",
      "«…-DEKİnden» — bâ cer eder ve bu mâ MEVSÛLEdir: ardındaki عِنْدَنَا zarfı onun sılasıdır (sıla şibh-i cümle olabilir — yalnız asılacak bir şey ister; nefiy ise üzerinde amel edeceği koca bir cümle isterdi). «Yanımızda olan ile».",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("عِنْدَنَا","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ — وَالظَّرْفُ صِلَةُ «مَا».",
      "«with us» — the zarf عِنْدَ, a noun and a mudaf, with the attached «na» as its mudaf ilayh; the whole zarf is the sila of the ma before it.",
      "«yanımızda» — zarf عِنْدَ: isimdir ve muzâftır; bitişik «نَا» muzâfun ileyhidir. Zarfın bütünü, önceki mânın sılasıdır."),
  tok("وَأَنْتَ","anta","pron",["mubtada-khabar","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَنْتَ» مُبْتَدَأٌ ثَانٍ — وَخَبَرُهُ «رَاضٍ» الْآتِي.",
      "«and YOU» — the second mubtada, and THIS one gets the spoken khabar: the رَاضٍ still to come serves the second clause aloud and the first by echo.",
      "«ve SEN» — ikinci mübtedâ; ve söylenen haber BUNUNDUR: birazdan gelecek رَاضٍ, ikinci cümleye sesli, birinciye yankıyla hizmet eder.",
      segments=[seg("وَ","wa","part"), seg("أَنْتَ","anta","pron")]),
  tok("بِمَا","ma-mawsula","pron",["anwa-ma","huruf-jarr"],
      "الْبَاءُ جَارَّةٌ وَ«مَا» مَوْصُولَةٌ — مَعْطُوفَةُ الْقِصَّةِ عَلَى الْأُولَى.",
      "The second «with what» — read exactly as the first: the ma'tuf follows the ma'tuf alayh.",
      "İkinci «…-dekinden» — tıpkı ilki gibi okunur: ma'tûf, ma'tûfun aleyhe tâbidir.",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("عِنْدَكَ","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — صِلَةُ «مَا».",
      "«with you» — the same zarf-sila anatomy, the kaf now the mudaf ilayh.",
      "«yanında» — aynı zarf-sıla anatomisi; muzâfun ileyh şimdi kâftır."),
  tok("رَاضٍ","radin","noun",["mubtada-khabar","ism-fail","ism-maqsur-manqus","tark-al-musnad"],
      "خَبَرُ «أَنْتَ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ، وَهُوَ الْقَرِينَةُ عَلَى «رَاضُونَ» الْمَحْذُوفِ.",
      "«content» — the bayt's one spoken musnad, khabar of أَنْتَ. A MANQUS: ism fail of رَضِيَ whose ya has dropped against the tanwin, the damma estimated on the absent letter — the kasratan you see is all that remains of رَاضِي. And it is the QARINA: from this single رَاضٍ the hearer supplies رَاضُونَ for «we». One word, two clauses, and the omission is the eloquence.",
      "«hoşnut» — beytin söylenen tek müsnedi; أَنْتَ'nin haberi. MENKŪS: رَضِيَ'nin ism-i fâili; yâsı tenvine karşı düşmüş, damme yok harfin üzerinde takdîr edilir — gördüğün kesreteyn, رَاضِي'den geriye kalanın tamamıdır. Ve KARÎNE odur: bu tek رَاضٍ'den dinleyen, «biz» için رَاضُونَ'yi tamamlar. Tek kelime, iki cümle; ve hazif, belâgatin kendisidir."),
  tok("وَالرَّأْيُ","ray","noun",["mubtada-khabar","anwa-al-waw"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ أَوْ حَالِيَّةٌ، وَ«الرَّأْيُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and the opinion» — a closing nominal sentence: the waw opens it (isti'naf, or hal), and الرَّأْيُ is its mubtada.",
      "«ve görüş» — kapanış isim cümlesi: vâv onu açar (isti'nâf yahut hâl), الرَّأْيُ mübtedâsıdır.",
      segments=[seg("وَ","wa","part"), seg("الرَّأْيُ","ray","noun")]),
  tok("مُخْتَلِفٌ","mukhtalif","noun",["mubtada-khabar","ism-fail","form-viii-verbs"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ اخْتَلَفَ.",
      "«differing» — the khabar, ism fail of the Form VIII اِخْتَلَفَ: each side content, and the two contentments face opposite ways.",
      "«muhtelif» — haber; VIII. bâb اِخْتَلَفَ'nin ism-i fâili: iki taraf da hoşnut, ve iki hoşnutluk zıt yönlere bakar.",
      punct=".")],
 "jumal": [
  J("نَحْنُ بِمَا عِنْدَنَا وَأَنْتَ بِمَا عِنْدَكَ رَاضٍ",
    "حُذِفَ مُسْنَدُ الْأَوَّلِ — رَاضُونَ — بِدَلَالَةِ سِيَاقِ الْكَلَامِ، احْتِرَازًا عَنِ الْعَبَثِ.",
    "The first clause's musnad — «we are content» — omitted on the strength of the siyaq: the one رَاضٍ spoken later answers for both.",
    "İlk cümlenin müsnedi — «biz hoşnuduz» — siyâkın delâletiyle hazfedildi: sonra söylenen tek رَاضٍ ikisine birden cevap verir.")]})

# ---------------------------------------------------------------- s4 — Yusuf 83
S.append({"id": "s4", "translation": {
 "en": "So — a beautiful patience. (Yusuf 12:83. The omitted word may be the musnad — «is more beautiful» — or the musnad ilayh — «my course is…»: the books keep BOTH taqdirs.)",
 "tr": "Artık — güzel bir sabır. (Yûsuf 12:83. Hazfedilen, müsned olabilir — «daha güzeldir» — yahut müsnedün ileyh — «benim işim…»: kitaplar İKİ takdiri de saklar.)"},
 "tokens": [
  tok("فَصَبْرٌ","sabr","noun",["mubtada-khabar","tark-al-musnad","hadhf-wa-taqdir"],
      "الْفَاءُ فَصِيحَةٌ، وَ«صَبْرٌ» مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ — أَوْ خَبَرٌ مُبْتَدَؤُهُ مَحْذُوفٌ.",
      "Yaʿqub's word over his torn son — and grammar's most honest fork. Read صَبْرٌ as MUBTADA and the omitted word is the MUSNAD: فَصَبْرٌ جَمِيلٌ أَجْمَلُ, «a beautiful patience is more beautiful». Read it as KHABAR and the omitted word is the MUSNAD ILAYH: فَأَمْرِي صَبْرٌ جَمِيلٌ, «my course is a beautiful patience». Nothing on the surface closes the fork, so the books carry both taqdirs side by side — and the musannif quotes the aya here precisely because it teaches that a mahdhuf is NAMED by reconstruction, not guessed at. The fa is the fasiha: it discloses an unspoken condition — «since this is so…».",
      "Yakub'un, paramparça oğlu üzerine sözü — ve gramerin en dürüst çatalı. صَبْرٌ'u MÜBTEDÂ oku: hazfedilen MÜSNEDdir — فَصَبْرٌ جَمِيلٌ أَجْمَلُ, «güzel bir sabır daha güzeldir». HABER oku: hazfedilen MÜSNEDÜN İLEYHtir — فَأَمْرِي صَبْرٌ جَمِيلٌ, «benim işim güzel bir sabırdır». Yüzeyde çatalı kapatan hiçbir şey yok; kitaplar iki takdiri yan yana taşır — ve musannif âyeti tam da şunu öğrettiği için burada anar: mahzuf, tahminle değil, KURARAK adlandırılır. Fâ, fasîhadır: söylenmemiş bir şartı açığa vurur — «mademki böyle…».",
      segments=[seg("فَ","fa","part"), seg("صَبْرٌ","sabr","noun")]),
  tok("جَمِيلٌ","jamil","noun",["naat-sifa","sifa-mushabbaha"],
      "صِفَةٌ لِـ«صَبْرٌ» مَرْفُوعَةٌ — عَلَى التَّقْدِيرَيْنِ جَمِيعًا.",
      "«beautiful» — sifa of the patience, in raf' — and note the economy: whichever taqdir you choose, this word's i'rab never moves. The fork is entirely in the unsaid.",
      "«güzel» — sabrın sıfatı, merfû — ve şu iktisada dikkat: hangi takdiri seçersen seç, bu kelimenin i'râbı yerinden oynamaz. Çatal, tümüyle söylenmemiş olandadır.",
      punct=".")],
 "jumal": [
  J("فَصَبْرٌ جَمِيلٌ",
    "الْمَحْذُوفُ مُسْنَدٌ عَلَى تَقْدِيرٍ وَمُسْنَدٌ إِلَيْهِ عَلَى تَقْدِيرٍ — وَالْوَجْهَانِ مَحْفُوظَانِ فِي الْكُتُبِ.",
    "One aya, two reconstructions — the omitted word is the musnad on one taqdir and the musnad ilayh on the other, and the books keep both.",
    "Tek âyet, iki kuruluş — hazfedilen bir takdirde müsned, ötekinde müsnedün ileyhtir; kitaplar ikisini de saklar.")]})

# ---------------------------------------------------------------- s5 — Luqman 25
S.append({"id": "s5", "translation": {
 "en": "And if you asked them who created the heavens and the earth, they would surely say: «Allah». (Luqman 31:25 — the answer omits the musnad خَلَقَهُنَّ: the realized question is its qarina.)",
 "tr": "Onlara gökleri ve yeri kim yarattı diye sorsan, elbette «Allah» derler. (Lokmân 31:25 — cevap, müsned olan خَلَقَهُنَّ'yi hazfeder: gerçekleşmiş soru onun karînesidir.)"},
 "tokens": [
  tok("وَلَئِنْ","lain","part",["in-shartiyya","tark-al-musnad"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَ«إِنْ» شَرْطِيَّةٌ.",
      "Two particles fused in the writing: the lam that PAVES for an omitted oath (اللَّامُ الْمُوَطِّئَةُ لِلْقَسَمِ), and إِنْ the conditional. Their meeting sets a rule in motion: when oath and shart share one sentence, the coming jawab belongs to the EARLIER of the two — watch لَيَقُولُنَّ arrive dressed for the oath, not for the shart.",
      "Yazıda kaynaşmış iki edat: hazfedilmiş bir yemine zemin döşeyen lâm (اللَّامُ الْمُوَطِّئَةُ لِلْقَسَمِ) ve şart edatı إِنْ. Buluşmaları bir kuralı işletir: yemin ile şart tek cümlede buluşunca gelecek cevap İKİSİNDEN ÖNCEKİNİNDİR — لَيَقُولُنَّ'nin şart için değil, yemin için giyinmiş geldiğine bak.",
      segments=[seg("وَ","wa","part"), seg("لَ","lam-qasam","part"), seg("إِنْ","in-shartiyya","part")]),
  tok("سَأَلْتَهُمْ","saala","verb",["in-shartiyya","mafulayn"],
      "فِعْلُ الشَّرْطِ، مَاضٍ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ فَاعِلٌ وَ«هُمْ» مَفْعُولٌ أَوَّلُ.",
      "«you asked them» — the shart verb, a mazi standing in the position of jazm; the ta is the doer, the fused «hum» the first object. And its sin is a RADICAL — سَأَلَ, not the future prefix: the root is س أ ل and the paradigm owns the word whole.",
      "«onlara sorsan» — şart fiili; mahallen meczum mâzî. Tâ fâil, bitişik «هُمْ» birinci mef'ûldür. Ve sîni KÖK HARFİDİR — سَأَلَ; istikbal sîni değil: kök س أ ل'dir ve paradigma kelimeyi bütün hâliyle tanır.",
      segments=[seg("سَأَلْ","saala","verb"), seg("تَ","pron-2ms","pron"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَنْ","man-istifham","pron",["mubtada-khabar","tark-al-musnad"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ مَقُولُ السُّؤَالِ.",
      "«WHO…?» — the interrogative man, mabni, as mubtada; the question-clause is the second object of the asking. The fatha on its mim is the diagnostic: this is the ISM, never the jarr letter مِنْ. Keep this question in hand — the aya's last word will lean its whole omission on it.",
      "«KİM…?» — istifhâm ismi men; mebnî, mübtedâ. Soru cümlesi, sormanın ikinci mef'ûlüdür. Mîmindeki fetha teşhistir: bu İSİMdir, asla cer harfi مِنْ değil. Bu soruyu elde tut — âyetin son kelimesi bütün hazfini ona yaslayacak.",
      punct=""),
  tok("خَلَقَ","khalaqa","verb",["fail","tark-al-musnad"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى «مَنْ» — وَالْجُمْلَةُ خَبَرُ «مَنْ».",
      "«created» — mazi, its doer concealed, returning upon man; the clause is man's khabar. This is the very verb the ANSWER will omit — said here in the question, it will not need saying again.",
      "«yarattı» — mâzî; fâili gizli, مَنْ'e râcidir; cümle, مَنْ'in haberidir. Cevabın hazfedeceği fiil tam da budur — soruda bir kez söylenince, yeniden söylenmeye muhtaç kalmaz.",
      segments=[seg("خَلَقَ","khalaqa","verb")]),
  tok("السَّمَاوَاتِ","samawat","noun",["maful-bihi","jam-muannath-salim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْكَسْرَةُ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "«the heavens» — the object, and its nasb sign is the KASRA: a sound feminine plural takes kasra for fatha, one of the classical substitutions.",
      "«gökleri» — mef'ûl; nasb alâmeti KESRAdır: cem'-i müennes-i sâlim, fetha yerine kesra alır — klasik bedellerdendir.",
      segments=[seg("السَّمَاوَاتِ","samawat","noun")]),
  tok("وَالْأَرْضَ","ard","noun",["maful-bihi","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْأَرْضَ» مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.",
      "«and the earth» — joined to the heavens, in nasb by the plain fatha.",
      "«ve yeri» — göklere atfedilmiş; zâhir fetha ile mansûb.",
      segments=[seg("وَ","wa","part"), seg("الْأَرْضَ","ard","noun")]),
  tok("لَيَقُولُنَّ","qala","verb",["nun-tawkid","afal-khamsa","tark-al-musnad"],
      "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَالْفِعْلُ مُضَارِعٌ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِتَوَالِي الْأَمْثَالِ، وَوَاوُ الْجَمَاعَةِ الْمَحْذُوفَةُ فَاعِلٌ، وَالنُّونُ لِلتَّوْكِيدِ.",
      "«they will SURELY say» — the aya's densest word, four pieces in one: the lam answers the paved-for OATH (this is the jawab al-qasam, which is why no jazm appears); the verb is يَقُولُونَ with its raf'-nun dropped and then the group's waw squeezed out against the heavy nun (تَوَالِي الْأَمْثَالِ); that omitted waw is still the FA'IL; and the doubled nun is the NUN OF EMPHASIS. Assemble it backwards and يَقُولُونَ stands whole again.",
      "«ELBETTE derler» — âyetin en yoğun kelimesi; birde dört parça: lâm, zemini döşenmiş YEMİNİN cevabına düşer (cevâb-ı kasemdir; cezm görünmeyişi bundandır); fiil, ref' nûnu düşmüş, sonra cemâat vâvı şeddeli nûna karşı sıkışıp çıkmış يَقُولُونَ'dir (تَوَالِي الْأَمْثَالِ); o düşen vâv hâlâ FÂİLdir; çift nûn ise TE'KÎD NÛNUdur. Tersinden kur, يَقُولُونَ yeniden bütün olur.",
      segments=[seg("لَ","lam-qasam","part"), seg("يَقُولُ","qala","verb"), seg("نَّ","nun-tawkid","part")]),
  tok("اللَّهُ","allah","propn",["mubtada-khabar","tark-al-musnad","hadhf-wa-taqdir"],
      "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ، خَبَرُهُ مَحْذُوفٌ — أَيْ: اللَّهُ خَلَقَهُنَّ — وَالْقَرِينَةُ السُّؤَالُ الْمُحَقَّقُ.",
      "«Allah.» — one word where a sentence stands. The mubtada, and its musnad is OMITTED: the full answer is اللَّهُ خَلَقَهُنَّ, «Allah created them». The qarina is a سُؤَالٌ مُحَقَّقٌ — a question actually asked and standing in the text — and against it the repetition would be ʿabath: the verb is already ringing in the air from مَنْ خَلَقَ. This is the chapter's rule in its purest state: every hadhf leans on a qarina, and the strongest qarina of all is the question the answer answers.",
      "«Allah.» — cümle yerinde duran tek kelime. Mübtedâdır ve müsnedi HAZFEDİLMİŞTİR: cevabın tamamı اللَّهُ خَلَقَهُنَّ'dir, «onları Allah yarattı». Karîne, سُؤَالٌ مُحَقَّقٌ'tır — fiilen sorulmuş, metinde duran bir soru — ve ona karşı tekrar ABES olurdu: fiil, مَنْ خَلَقَ'dan hâlâ havada çınlamaktadır. Bâbın kuralı en saf hâlinde budur: her hazif bir karîneye yaslanır; karînelerin en güçlüsü de cevabın cevapladığı sorudur.",
      punct=".")],
 "jumal": [
  J("مَنْ خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ — لَيَقُولُنَّ اللَّهُ",
    "حُذِفَ الْمُسْنَدُ — خَلَقَهُنَّ — لِقِيَامِ السُّؤَالِ الْمُحَقَّقِ قَرِينَةً عَلَيْهِ.",
    "The answer's musnad — «created them» — omitted, because the realized question stands as its qarina: the verb still rings from the asking.",
    "Cevabın müsnedi — «onları yarattı» — hazfedildi; çünkü gerçekleşmiş soru ona karîne olarak dikilidir: fiil, sorudan hâlâ çınlar.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # NEW this chapter
 "muntaliq":  g("مُنْطَلِق", "ط ل ق", "noun", "setting out, departing (ism fail of اِنْطَلَقَ)", "yola çıkan (اِنْطَلَقَ'nın ism-i fâili)", 3, form="VII"),
 "idha-fujaiyya": g("إِذَا (الْفُجَائِيَّة)", None, "part", "and there was…! (idha of surprise — a noun follows it)", "bir de ne göreyim…! (ansızlık idhâsı — ardından isim gelir)", 4),
 "nahnu":     g("نَحْنُ", None, "pron", "we (detached)", "biz (munfasıl)", 1),
 "radin":     g("رَاضٍ", "ر ض ي", "noun", "content, pleased (ism fail of رَضِيَ, manqus)", "hoşnut, râzı (رَضِيَ'nin ism-i fâili, menkūs)", 4),
 "mukhtalif": g("مُخْتَلِف", "خ ل ف", "noun", "differing, various (ism fail of اِخْتَلَفَ)", "muhtelif, farklı (اِخْتَلَفَ'nin ism-i fâili)", 3, form="VIII"),
 "lain":      g("لَئِنْ", None, "part", "and surely if — the oath-paving lam + conditional in", "yemine zemin döşeyen lâm + şart in'i: «andolsun ki eğer»", 5),
 "lam-qasam": g("لَ (لَامُ الْقَسَمِ)", None, "part", "the lam of the oath / its answer", "kasem lâmı / cevabında düşen lâm", 4),
 "nun-tawkid": g("نَّ (نُونُ التَّوْكِيدِ)", None, "part", "the heavy nun of emphasis on a verb", "fiildeki şeddeli te'kîd nûnu", 4),
 "man-istifham": g("مَنْ (الاِسْتِفْهَامِيَّة)", None, "pron", "who? (interrogative)", "kim? (istifhâm meni)", 3),
 "khalaqa":   g("خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1, form="I"),
 "samawat":   g("سَمَاء", "س م و", "noun", "sky, heaven", "gök, semâ", 1, plural="سَمَاوَات"),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "ray":       g("رَأْي", "ر أ ي", "noun", "opinion, view", "görüş, rey", 2, plural="آرَاء"),
 "sabr":      g("صَبْر", "ص ب ر", "noun", "patience", "sabır", 1),
 "jamil":     g("جَمِيل", "ج م ل", "noun", "beautiful", "güzel", 1),
 "saala":     g("سَأَلَ", "س أ ل", "verb", "to ask", "sormak", 1, form="I"),
 "hatta2-unused": None,
}
GLOSS_ADD = {k: v for k, v in GLOSS_ADD.items() if v}

def build_morph():
    """Copy saala; one new sound paradigm خَلَقَ (bab نَصَرَ)."""
    out = {}
    m = json.loads((ROOT / "content/samples/wasiyyat-abi-yusuf-l5/morphology.json").read_text(encoding="utf-8"))
    out["saala"] = m["verbs"]["saala"]
    out["khalaqa"] = _sg.sound1("nasara", "خَلَق", "خْلُق", "اُخْلُق", "خَلْق", "خَالِق",
                                "مَخْلُوق", "خُلِقَ", "يُخْلَقُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/15.json").write_text(
    json.dumps({"chapter": 15, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 15 for c in man["chapters"]):
    man["chapters"].append({"n": 15, "title": TITLE15})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.15.0"
ADD_EN = (" Chapter 15 continues from the same file (lines ~1337-1400, sahifa 46-47), where ahwal al-musnad "
          "opens with its omission: زَيْدٌ مُنْطَلِقٌ وَعَمْرٌو and خَرَجْتُ فَإِذَا زَيْدٌ (the matns' frames), Qays "
          "b. al-Khatim's bayt نَحْنُ بِمَا عِنْدَنَا وَأَنْتَ بِمَا عِنْدَكَ رَاضٍ وَالرَّأْيُ مُخْتَلِفٌ, Yusuf 12:83 and "
          "Luqman 31:25. The ayat and the bayt are received text quoted exactly; the Ottoman print's "
          "plain-alif spellings are restored to standard orthography, a spelling normalization only.")
ADD_TR = (" On beşinci bâb aynı dosyadan (satır ~1337-1400, sahife 46-47) devam eder; ahvâl-i müsned, terkle "
          "açılır: metinlerin kalıpları زَيْدٌ مُنْطَلِقٌ وَعَمْرٌو ile خَرَجْتُ فَإِذَا زَيْدٌ, Kays b. el-Hatîm'in beyti "
          "نَحْنُ بِمَا عِنْدَنَا وَأَنْتَ بِمَا عِنْدَكَ رَاضٍ وَالرَّأْيُ مُخْتَلِفٌ, Yûsuf 12:83 ve Lokmân 31:25. Âyetler ve "
          "beyit aynen alınmış mervî metindir; Osmanlı baskısının düz elifli imlâsı standart imlâya "
          "çevrilmiştir — yalnız bir imlâ normalizasyonudur.")
if "1337-1400" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch15:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
