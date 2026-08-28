# -*- coding: utf-8 -*-
"""Author chapter 24 of talkhis-al-miftah — الِاسْتِفْهَام.

The second talabi kind (sahifa 70-71): seeking the FORM of a thing in the
mind. Eleven particles, and a three-way split that is pure mechanics:

  • the HAMZA serves talab tasdiq AND talab tasawwur — and what is asked
    about is precisely the word standing AFTER it (أَضَرَبْتَ الفعل،
    ءَأَنْتَ الفاعل، أَزَيْدًا المفعول);
  • هَلْ serves tasdiq ONLY — so هَلْ زَيْدٌ قَامَ أَمْ عَمْرٌو is mumtani,
    هَلْ زَيْدًا ضَرَبْتَ is qabih (the fronting implies the deed conceded,
    against hal's own question), and هَلْ زَيْدًا ضَرَبْتَهُ is rescued by
    the mufassar taqdir; هَلْ also pins the mudari to the FUTURE, which is
    why أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ stands and هَلْ تَضْرِبُ with the
    same hal-clause falls;
  • the rest serve tasawwur only (their bab follows in the source).

ATTRIBUTION: every sentence is the source's own worked example quoted
verbatim (research/sources/talkhis-al-miftah-balagha.txt lines ~2000-2043,
sahifa 70-71), Ottoman plain-alif normalized to standard orthography
(اَزَيْدًا → أَزَيْدًا, فِى → فِي) — a recorded normalization, not an edit.

Grammar this chapter teaches:
  • note 126 `al-istifham` — the definition, the eleven particles, the
    tasdiq/tasawwur split, the hamza-adjacency rule, am muttasila, and
    hal's three consequences.
  • engine work: the interrogative hamza peeled before OPEN-CLASS words
    (lexicon-guarded both ways), أَمْ split from أُمّ on the hamza's vowel,
    and the IstifhamEngine reading the hamza/hal frames off adjacency.
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
S = []

TITLE24 = {"ar": "الِاسْتِفْهَامُ — الْهَمْزَةُ وَهَلْ",
           "en": "Istifham — the Hamza and Hal",
           "tr": "İstifham — Hemze ve Hel"}

# ------------------------------------------------- s1 — hamza, tasdiq
S.append({"id": "s1", "translation": {
 "en": "Is Zayd standing? (The hamza on a nominal sentence with no am: the whole nisba offered for yes or no — talab tasdiq.)",
 "tr": "Zeyd ayakta mı? (أَمْ'siz isim cümlesi üzerinde hemze: nispetin tamamı evet/hayıra sunulur — talep-i tasdik.)"},
 "tokens": [
  tok("أَزَيْدٌ","zayd","propn",["al-istifham"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ وَ«زَيْدٌ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "the question hamza riding «Zayd» — the mubtada, marfu'. ISTIFHAM defined: seeking the FORM of a thing in the mind; here the whole nisba «Zayd is standing» is offered for yes or no, which is TALAB TASDIQ.",
      "«Zeyd»e binmiş istifham hemzesi — mübtedâ, merfû. İSTİFHAM tarifi: bir şeyin sûretinin zihinde hâsıl olmasını istemek; burada «Zeyd ayaktadır» nispetinin tamamı evet/hayıra sunulur — TALEB-İ TASDÎK budur.",
      segments=[seg("أَ","hamza-istifham","part"), seg("زَيْدٌ","zayd","propn")]),
  tok("قَائِمٌ","qaim","noun",["al-istifham"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«standing» — the khabar, marfu'; the nisba's second end, inside the question whole.",
      "«ayakta» — haber, merfû; nispetin ikinci ucu, sorunun bütünü içinde.",
      punct="؟")],
 "jumal": [
  J("أَزَيْدٌ قَائِمٌ",
    "طَلَبُ التَّصْدِيقِ: طَلَبُ وُقُوعِ النِّسْبَةِ أَوْ عَدَمِ وُقُوعِهَا.",
    "TALAB TASDIQ: the asker holds the sentence's two ends and asks only whether the tie between them HOLDS — the answer is yes or no, never a name.",
    "TALEB-İ TASDÎK: soran, cümlenin iki ucunu elinde tutar ve yalnız aralarındaki bağın TUTUP tutmadığını sorar — cevap evet yahut hayırdır, asla bir isim değil."),
  J("أَزَيْدٌ قَائِمٌ",
    "الْجُمْلَةُ إِنْشَائِيَّةٌ: الِاسْتِفْهَامُ ثَانِي أَنْوَاعِ الطَّلَبِ.",
    "The question is INSHA, the second talabi kind after tamanni: it calls for something not in hand at the asking — here, the mind's picture of how things stand — so truth and falsehood cannot touch the asking itself.",
    "Soru İNŞÂdır; temennîden sonra ikinci talebî nevi: isteme ânında elde olmayanı ister — burada, işlerin nasıl durduğunun zihindeki sûretini — bu yüzden sormanın kendisine doğru/yanlış işlemez.")]})

# ------------------------------------------------- s2 — hamza + am, ta'yin
S.append({"id": "s2", "translation": {
 "en": "Is it date-syrup in the vessel, or honey? (The hamza paired with am: two candidates, and WHICH is demanded — talab tasawwur, ta'yin of the musnad ilayh.)",
 "tr": "Kaptaki pekmez mi yoksa bal mı? (Hemze أَمْ ile eşleşmiş: iki aday ve HANGİSİ istenir — taleb-i tasavvur, müsnedün ileyhin tayini.)"},
 "tokens": [
  tok("أَدِبْسٌ","dibs","noun",["al-istifham"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ وَ«دِبْسٌ» مُبْتَدَأٌ مُؤَخَّرٌ تَقْدِيرًا — وَهُوَ الْمَسْؤُولُ عَنْهُ الْأَوَّلُ.",
      "the hamza riding «date-syrup» — the first CANDIDATE. What stands after the hamza is what is asked, and here a thing stands there, not the whole sentence: the asker concedes something is in the vessel and demands its NAME.",
      "«pekmez»e binmiş hemze — birinci ADAY. Hemzeden sonra duran, sorulandır; burada orada bütün cümle değil bir ŞEY durur: soran, kapta bir şey olduğunu teslim eder ve ADINI ister.",
      segments=[seg("أَ","hamza-istifham","part"), seg("دِبْسٌ","dibs","noun")]),
  tok("فِي","fi","part",["al-istifham","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in» — the jarr letter opening the khabar's phrase.",
      "«-de» — haberin öbeğini açan cer harfi."),
  tok("الْإِنَاءِ","inaa","noun",["al-istifham"],
      "مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "«the vessel» — majrur; the jarr-phrase is the khabar, shared by both candidates.",
      "«kap» — mecrur; câr-mecrûr haberdir ve iki adayın ortağıdır."),
  tok("أَمْ","am","part",["al-istifham"],
      "أَمِ الْمُتَّصِلَةُ — عَدِيلَةُ الْهَمْزَةِ.",
      "«or» — AM MUTTASILA, the hamza's counterweight: it holds up the SECOND candidate and turns the question into a demand for ta'yin. It exists only where a question-hamza came before; opening its own question it would be munqati'a (= بَلْ + a new hamza).",
      "«yoksa» — MUTTASILA أَمْ, hemzenin dengesi: İKİNCİ adayı kaldırır ve soruyu tayin talebine çevirir. Ancak önünde soru hemzesi geçmişse vardır; kendi sorusunu açsaydı munkatı'a olurdu (= بَلْ + yeni bir hemze)."),
  tok("عَسَلٌ","asal","noun",["al-istifham"],
      "مَعْطُوفٌ عَلَى «دِبْسٌ» — الْمَسْؤُولُ عَنْهُ الثَّانِي، وَالْمَطْلُوبُ التَّعْيِينُ.",
      "«honey» — joined to the first candidate; the asked-for is TA'YIN of one of the two: pure tasawwur. The answer must be a NAME — «honey» — never «yes».",
      "«bal» — birinci adaya atfedilmiş; istenen, ikisinden birinin TAYİNİdir: saf tasavvur. Cevap bir İSİM olmalıdır — «bal» — asla «evet» değil.",
      punct="؟")],
 "jumal": [
  J("أَدِبْسٌ فِي الْإِنَاءِ أَمْ عَسَلٌ",
    "طَلَبُ التَّصَوُّرِ: طَلَبُ تَعْيِينِ أَحَدِ الشَّيْئَيْنِ — وَهُنَا عُيِّنَ الْمُسْنَدُ إِلَيْهِ.",
    "TALAB TASAWWUR: one of two things is to be NAMED. Which slot is weighed is read off what follows the hamza — a noun here, so the MUSNAD ILAYH is asked; front the jarr-phrase (أَفِي الْخَابِيَةِ دِبْسُكَ أَمْ فِي الزِّقِّ) and the MUSNAD is.",
    "TALEB-İ TASAVVUR: iki şeyden biri ADLANDIRILACAKTIR. Hangi yuvanın tartıldığı, hemzeyi izleyenden okunur — burada isim; öyleyse sorulan MÜSNEDÜN İLEYHtir; câr-mecrûr öne alınırsa (أَفِي الْخَابِيَةِ دِبْسُكَ أَمْ فِي الزِّقِّ) MÜSNED sorulur."),
  J("أَدِبْسٌ فِي الْإِنَاءِ أَمْ عَسَلٌ",
    "أَمِ الْمُتَّصِلَةُ لَا تَقَعُ إِلَّا بَعْدَ هَمْزَةِ التَّسَاوِي أَوْ هَمْزَةِ الِاسْتِفْهَامِ.",
    "AM MUTTASILA never stands alone: it rides a preceding hamza, and the pair is ONE question with two ends. This is why هَلْ can never take it — hal has no «which» to offer (s4's doctrine, seen from am's side).",
    "MUTTASILA أَمْ asla tek durmaz: önceki hemzeye biner ve çift, iki uçlu TEK sorudur. هَلْ'in onu asla alamaması bundandır — hel'in sunacak bir «hangisi»si yoktur (s4'ün doktrini, أَمْ tarafından görünüşü).")]})

# ------------------------------------------------- s3 — hamza on the maf'ul
S.append({"id": "s3", "translation": {
 "en": "Was it Zayd you struck? (The mansub noun stands between the hamza and its verb: the OBJECT is asked — the striking conceded, its target sought.)",
 "tr": "Zeyd'i mi dövdün? (Mansub isim hemze ile fiili arasında durur: sorulan MEF'ÛLdür — dövme teslim edilmiş, hedefi aranmaktadır.)"},
 "tokens": [
  tok("أَزَيْدًا","zayd","propn",["al-istifham","hadhf-al-maful"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ وَ«زَيْدًا» مَفْعُولٌ بِهِ مُقَدَّمٌ.",
      "the hamza riding a MANSUB noun — so the OBJECT is what is asked: «was it ZAYD you struck?» The deed is conceded, its target sought. The chapter's mechanical rule in action: whatever stands directly after the hamza is the asked-about — verb, doer (ءَأَنْتَ ضَرَبْتَ زَيْدًا), or, as here, the fronted object.",
      "MANSUB bir isme binmiş hemze — öyleyse sorulan MEF'ÛLdür: «ZEYD'İ mi dövdün?» Fiil teslim edilmiş, hedefi aranmaktadır. Bâbın mekanik kuralı iş başında: hemzenin hemen ardında duran ne ise sorulan odur — fiil, fâil (ءَأَنْتَ ضَرَبْتَ زَيْدًا), yahut burada olduğu gibi öne alınmış mef'ûl.",
      segments=[seg("أَ","hamza-istifham","part"), seg("زَيْدًا","zayd","propn")]),
  tok("ضَرَبْتَ","daraba","verb",["al-istifham"],
      "فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلُهُ.",
      "«you struck» — the madi with its ta as fa'il; its object stands fronted before it, and the fronting IS the question's aim.",
      "«dövdün» — mâzî; tâ fâilidir; mef'ûlü önüne alınmıştır ve takdim, sorunun maksadının ta kendisidir.",
      punct="؟")],
 "jumal": [
  J("أَزَيْدًا ضَرَبْتَ",
    "مَا وَلِيَ الْهَمْزَةَ فَهُوَ الْمَسْؤُولُ عَنْهُ.",
    "THE ADJACENCY RULE: what follows the hamza is what is asked. Three sentences, one machine — أَضَرَبْتَ زَيْدًا asks the deed, ءَأَنْتَ ضَرَبْتَ زَيْدًا the doer, أَزَيْدًا ضَرَبْتَ the object — and only the word order moves.",
    "BİTİŞİKLİK KURALI: hemzeyi izleyen, sorulandır. Üç cümle, tek makine — أَضَرَبْتَ زَيْدًا fiili, ءَأَنْتَ ضَرَبْتَ زَيْدًا fâili, أَزَيْدًا ضَرَبْتَ mef'ûlü sorar — ve yalnız söz dizimi oynar."),
  J("أَزَيْدًا ضَرَبْتَ",
    "تَقْدِيمُ الْمَفْعُولِ هُنَا لِلِاسْتِفْهَامِ عَنْهُ — وَالتَّصْدِيقُ حَاصِلٌ.",
    "The fronting concedes the deed: only tasawwur remains, and the source notes the first shape (أَضَرَبْتَ) can serve either while the fronted ones serve tasawwur alone — the taqdim bab and the istifham bab meeting on one word order.",
    "Takdim fiili teslim eder: geriye yalnız tasavvur kalır; kaynak, ilk kalıbın (أَضَرَبْتَ) her ikisine, öne alınmışların yalnız tasavvura hizmet ettiğini not eder — takdim bâbı ile istifham bâbı tek söz diziminde buluşur.")]})

# ------------------------------------------------- s4 — hal, tasdiq only
S.append({"id": "s4", "translation": {
 "en": "Did Zayd stand? (hal seeks tasdiq only — yes or no; it never asks WHICH, so am muttasila after it is refused outright.)",
 "tr": "Zeyd kalktı mı? (هَلْ yalnız tasdik ister — evet yahut hayır; asla HANGİSİ demez, bu yüzden ardında muttasıla أَمْ düpedüz reddedilir.)"},
 "tokens": [
  tok("هَلْ","hal","part",["al-istifham"],
      "حَرْفُ اسْتِفْهَامٍ لِطَلَبِ التَّصْدِيقِ فَقَطْ.",
      "«did…?» — HAL, the tasdiq-only particle: the nisba's holding is asked, never a choice between two. Hence هَلْ زَيْدٌ قَامَ أَمْ عَمْرٌو is MUMTANI — hal has no «which» for the am to pair with — and hal leans to the VERB more than the hamza does (فَهَلْ أَنْتُمْ شَاكِرُونَ presses the deed harder than أَفَأَنْتُمْ would).",
      "«…mı?» — HEL, yalnız-tasdik edatı: nispetin tutup tutmadığı sorulur, asla ikisinden biri değil. Bu yüzden هَلْ زَيْدٌ قَامَ أَمْ عَمْرٌو MÜMTENİ'dir — hel'in, أَمْ'in eşleneceği bir «hangisi»si yoktur — ve hel fiile hemzeden çok meyleder (فَهَلْ أَنْتُمْ شَاكِرُونَ, fiili أَفَأَنْتُمْ'dan daha çok ister)."),
  tok("قَامَ","qama","verb",["al-istifham"],
      "فِعْلٌ مَاضٍ.",
      "«stood» — the madi; hal standing directly before a verb is its favourite seat.",
      "«kalktı» — mâzî; hel'in doğrudan fiil önünde durması en sevdiği yerdir."),
  tok("زَيْدٌ","zayd","propn",["al-istifham"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«Zayd» — the fa'il, marfu'.",
      "«Zeyd» — fâil, merfû.",
      punct="؟")],
 "jumal": [
  J("هَلْ قَامَ زَيْدٌ",
    "هَلْ لِطَلَبِ التَّصْدِيقِ فَقَطْ — فَامْتَنَعَ: هَلْ زَيْدٌ قَامَ أَمْ عَمْرٌو.",
    "HAL = tasdiq only. The refusals are the teaching: pair it with am muttasila and the sentence is not ugly but IMPOSSIBLE — the particle promises yes-or-no and the am demands a name.",
    "HEL = yalnız tasdik. Öğreten, redlerdir: onu muttasıla أَمْ ile eşleyin, cümle çirkin değil İMKÂNSIZ olur — edat evet/hayır vaad eder, أَمْ ise bir isim ister."),
  J("هَلْ قَامَ زَيْدٌ",
    "هَلْ أَصْلُهَا أَهَلْ عِنْدَ بَعْضِهِمْ، وَقِيلَ هِيَ بِمَعْنَى قَدْ.",
    "The scholars' two accounts of WHY: hal was originally أَهَلْ (the hamza dropped for frequency), and for the non-Sakkakis it carries قَدْ's sense underneath — which is their explanation for why هَلْ زَيْدٌ عَرَفَ is ugly. Sakkaki ties that ugliness to the fronting instead: a recorded khilaf.",
    "Âlimlerin NİÇİN'e iki cevabı: hel aslında أَهَلْ idi (hemze çoklukta düştü); Sekkâkî dışındakilere göre altında قَدْ mânâsı taşır — هَلْ زَيْدٌ عَرَفَ'nin çirkinliğini böyle açıklarlar. Sekkâkî ise o çirkinliği takdime bağlar: kayıtlı bir hilâf.")]})

# ------------------------------------------------- s5 — the mufassar rescue
S.append({"id": "s5", "translation": {
 "en": "Zayd — did you strike him? (The fronted mansub after hal is ugly — unless the verb carries an object pronoun: then an omitted explaining verb is understood, and hal stands before a verb again.)",
 "tr": "Zeyd'i — onu dövdün mü? (هَلْ'den sonra öne alınmış mansub çirkindir — meğerki fiil bir mef'ûl zamiri taşısın: o zaman hazfedilmiş bir müfessir fiil takdir edilir ve هَلْ yine fiil önünde durur.)"},
 "tokens": [
  tok("هَلْ","hal","part",["al-istifham"],
      "حَرْفُ اسْتِفْهَامٍ لِلتَّصْدِيقِ.",
      "«did…?» — hal again; and a mansub noun directly after it would be UGLY on its own (هَلْ زَيْدًا ضَرَبْتَ): the fronting implies the deed conceded, while hal exists to ask whether it happened at all.",
      "«…mı?» — yine hel; ve hemen ardındaki mansub isim kendi başına ÇİRKİN olurdu (هَلْ زَيْدًا ضَرَبْتَ): takdim fiili teslim edildiğini îmâ eder; oysa hel, fiil hiç oldu mu diye sormak için vardır."),
  tok("زَيْدًا","zayd","propn",["al-istifham"],
      "مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ — تَقْدِيرُهُ: هَلْ ضَرَبْتَ زَيْدًا ضَرَبْتَهُ.",
      "«Zayd» — object of an OMITTED verb which the written one explains: the taqdir is هَلْ ضَرَبْتَ زَيْدًا ضَرَبْتَهُ. With that verb understood, hal once again stands directly before a verbal sentence — and the ugliness lifts.",
      "«Zeyd'i» — yazılı fiilin AÇIKLADIĞI hazfedilmiş bir fiilin mef'ûlü: takdir هَلْ ضَرَبْتَ زَيْدًا ضَرَبْتَهُ'dur. O fiil takdir edilince hel yine doğrudan bir fiil cümlesinin önündedir — ve çirkinlik kalkar."),
  tok("ضَرَبْتَهُ","daraba","verb",["al-istifham"],
      "فِعْلٌ مَاضٍ وَالْهَاءُ مَفْعُولُهُ — وَهِيَ الَّتِي أَجَازَتِ التَّرْكِيبَ.",
      "«you struck him» — the madi with its object pronoun; that ha is the whole LICENCE: it marks the written verb as the explainer of an omitted twin, and the mufassar taqdir rescues the word order.",
      "«onu dövdün» — mâzî ve mef'ûl zamiri; o hâ RUHSATIN kendisidir: yazılı fiili, hazfedilmiş ikizinin açıklayıcısı kılar ve müfesser takdiri söz dizimini kurtarır.",
      segments=[seg("ضَرَبْتَ","daraba","verb"), seg("هُ","pron-3ms","pron")],
      punct="؟")],
 "jumal": [
  J("هَلْ زَيْدًا ضَرَبْتَهُ",
    "الِاشْتِغَالُ: الْمَذْكُورُ مُفَسِّرٌ لِمَحْذُوفٍ — وَبِهِ ارْتَفَعَ الْقُبْحُ.",
    "The ISHTIGHAL shape: the written verb is busy with its pronoun, so the fronted noun takes an omitted twin as its governor. One pronoun separates the ugly (ضَرَبْتَ) from the sound (ضَرَبْتَهُ) — the minimal pair is the lesson.",
    "İŞTİGĀL kalıbı: yazılı fiil zamiriyle meşguldür; öne alınmış isim, âmil olarak hazfedilmiş bir ikiz alır. Çirkini (ضَرَبْتَ) sahihten (ضَرَبْتَهُ) TEK zamir ayırır — asgarî çift, dersin kendisidir."),
  J("هَلْ زَيْدًا ضَرَبْتَهُ",
    "سِرُّ الْقُبْحِ: تَقْدِيمُ الْمَفْعُولِ يَقْتَضِي حُصُولَ التَّصْدِيقِ بِالْفِعْلِ.",
    "WHY the bare fronting is ugly: fronting an object is tasawwur's move — it concedes the deed — while hal's whole office is to ask the deed. Sakkaki reads هَلْ رَجُلٌ عَرَفَ's ugliness the same way; the others blame hal's underlying قَدْ. Both schools, on the page.",
    "Çıplak takdimin çirkinliğinin SIRRI: mef'ûlü öne almak tasavvurun hamlesidir — fiili teslim eder — oysa hel'in bütün görevi fiili sormaktır. Sekkâkî, هَلْ رَجُلٌ عَرَفَ'nin çirkinliğini de böyle okur; diğerleri hel'in altındaki قَدْ'i suçlar. İki mektep de sayfadadır.")]})

# ------------------------------------------------- s6 — hamza tolerates, hal refuses
S.append({"id": "s6", "translation": {
 "en": "Do you strike Zayd, when he is your brother? (Sound with the hamza — but hal pins the mudari to the future, and the hal-clause makes it present: with hal the same sentence falls.)",
 "tr": "Kardeşin olduğu hâlde Zeyd'i döver misin? (Hemze ile sahih — fakat هَلْ muzâriyi istikbâle tahsis eder ve hâl cümlesi onu şimdiye bağlar: aynı cümle هَلْ ile düşer.)"},
 "tokens": [
  tok("أَتَضْرِبُ","daraba","verb",["al-istifham","mudari-marfu"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ وَالْمُضَارِعُ مَرْفُوعٌ — وَهُوَ هُنَا لِلْحَالِ.",
      "the hamza riding a MUDARI kept in the PRESENT — the rebuke is about what he does now. The hamza tolerates that; هَلْ would not: it pins the mudari to the FUTURE, so هَلْ تَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ is refused while this stands.",
      "ŞİMDİDE tutulmuş bir MUZÂRİye binmiş hemze — azar, şu an yaptığınadır. Hemze buna katlanır; هَلْ katlanmazdı: muzâriyi İSTİKBÂLe tahsis eder; bu yüzden هَلْ تَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ reddedilir, bu ise ayakta kalır.",
      segments=[seg("أَ","hamza-istifham","part"), seg("تَضْرِبُ","daraba","verb")]),
  tok("زَيْدًا","zayd","propn",["al-istifham"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«Zayd» — the maf'ul bihi, mansub.",
      "«Zeyd'i» — mef'ûlün bih, mansub."),
  tok("وَهُوَ","huwa","pron",["al-istifham","anwa-al-waw"],
      "الْوَاوُ حَالِيَّةٌ وَ«هُوَ» مُبْتَدَأٌ.",
      "«while he» — the circumstantial waw opening the hal-clause, with the pronoun as its mubtada. This clause is what FORCES the verb's present sense — and thereby what makes hal impossible here.",
      "«o … iken» — hâl cümlesini açan hâl vâvı; zamir mübtedâsıdır. Fiilin şimdiki mânâsını ZORLAYAN bu cümledir — ve hel'i burada imkânsız kılan da odur.",
      segments=[seg("وَ","wa","part"), seg("هُوَ","huwa","pron")]),
  tok("أَخُوكَ","akh","noun",["al-istifham","five-nouns"],
      "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«your brother» — the khabar, marfu' by its WAW: a five-nouns head annexed to the kaf, its mudaf ilayh. The clause «while he is your brother» is the hal that dates the verb — and the whole sentence is the source's own proof-case for hal's futurity.",
      "«kardeşin» — haber, VÂVla merfû: kâf'a muzâf beş isimden biri; kâf muzâfun ileyhtir. «Kardeşin iken» cümlesi fiili tarihleyen hâldir — ve bütün cümle, kaynağın hel'in istikbâline kendi delil vak'asıdır.",
      punct="؟")],
 "jumal": [
  J("أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ",
    "جُمْلَةُ «وَهُوَ أَخُوكَ» حَالِيَّةٌ فِي مَحَلِّ نَصْبٍ.",
    "The waw-clause is a HAL in the position of nasb — and it is load-bearing: as the verb's circumstance it ties the striking to NOW, which the hamza tolerates and hal cannot.",
    "Vâv cümlesi nasb mahallinde HÂLdir — ve yük taşır: fiilin hâli olarak dövmeyi ŞİMDİye bağlar; hemze buna katlanır, hel katlanamaz."),
  J("أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ",
    "هَلْ تُخَصِّصُ الْمُضَارِعَ بِالِاسْتِقْبَالِ — فَصَحَّ مَعَ الْهَمْزَةِ مَا امْتَنَعَ مَعَهَا.",
    "HAL'S FUTURITY, proven by a minimal pair: the identical sentence stands with the hamza and falls with hal, because the circumstantial clause and hal's promised future cannot date one verb two ways.",
    "HEL'İN İSTİKBÂLİ, asgarî çiftle ispatlı: aynı cümle hemze ile ayakta durur, hel ile düşer; çünkü hâl cümlesi ile hel'in vaad ettiği istikbâl, tek fiili iki türlü tarihleyemez.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "dibs": g("دِبْس", "د ب س", "noun", "date-syrup, molasses", "pekmez", 4),
 "inaa": g("إِنَاء", "أ ن ي", "noun", "vessel, container", "kap", 3, plural="آنِيَة"),
 "asal": g("عَسَل", "ع س ل", "noun", "honey", "bal", 2),
 "am":   g("أَمْ", None, "part", "or…? (the ta'yin connective, paired with a question hamza)",
           "yoksa …mı? (tayin atfı; soru hemzesiyle eşleşir)", 4),
 "hamza-istifham": g("أَ (الِاسْتِفْهَام)", None, "part",
                     "the question hamza — what follows it is the thing asked about",
                     "istifham hemzesi — onu izleyen, sorulan şeydir", 3),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/24.json").write_text(
    json.dumps({"chapter": 24, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 24 for c in man["chapters"]):
    man["chapters"].append({"n": 24, "title": TITLE24})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.24.0"
ADD_EN = (" Chapter 24 opens the istifham bab from the same file (lines ~2000-2043, sahifa 70-71): "
          "every sentence is the source's own worked example quoted verbatim — أَزَيْدٌ قَائِمٌ, "
          "أَدِبْسٌ فِي الْإِنَاءِ أَمْ عَسَلٌ, أَزَيْدًا ضَرَبْتَ, هَلْ قَامَ زَيْدٌ, هَلْ زَيْدًا ضَرَبْتَهُ, "
          "أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ — with the Ottoman plain-alif spellings (اَزَيْدًا, فِى) "
          "normalized to standard orthography, a recorded normalization.")
ADD_TR = (" Yirmi dördüncü bâb, aynı dosyadan istifham bâbını açar (satır ~2000-2043, sahife 70-71): "
          "her cümle kaynağın kendi işlenmiş örneğinin aynen alınmışıdır — أَزَيْدٌ قَائِمٌ, أَدِبْسٌ فِي "
          "الْإِنَاءِ أَمْ عَسَلٌ, أَزَيْدًا ضَرَبْتَ, هَلْ قَامَ زَيْدٌ, هَلْ زَيْدًا ضَرَبْتَهُ, أَتَضْرِبُ زَيْدًا وَهُوَ "
          "أَخُوكَ — Osmanlı düz-elif imlâsı (اَزَيْدًا, فِى) standart imlâya çevrilmiştir; kayıtlı bir "
          "normalizasyondur.")
if "2000-2043" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch24:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
