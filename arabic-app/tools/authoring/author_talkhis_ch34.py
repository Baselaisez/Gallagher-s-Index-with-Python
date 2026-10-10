# -*- coding: utf-8 -*-
"""Author chapter 34 of talkhis-al-miftah — شِبْهُ كَمَالِ الِاتِّصَالِ: الِاسْتِئْنَافُ.

Sahifa 82-83 (lines ~2378-2400): the isti'naf — the second jumla answers
the QUESTION the first jumla provoked, so it is cut loose exactly as an
answer is cut loose from its question. Three kinds, each with the source's
own witness:

  {1} the question asks the GENERAL cause — the bayt:
      قَالَ لِي كَيْفَ أَنْتَ قُلْتُ عَلِيلٌ • سَهَرٌ دَائِمٌ وَحُزْنٌ طَوِيلٌ
      — the second hemistich answers «مَا سَبَبُ عِلَّتِكَ؟», its mubtada
      (سَبَبُ عِلَّتِي) omitted. The FASL falls at the hemistich.
  {2} the question asks the SPECIFIC cause — Yusuf 12:53:
      وَمَا أُبَرِّئُ نَفْسِي إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ — the
      inna-clause answers «does every nafs so command?» and this kind
      DEMANDS the ta'kid (inna + the sliding lam).
  {3} the question asks OTHER than the cause — Hud 11:69:
      قَالُوا سَلَامًا قَالَ سَلَامٌ — the answer to «what did he say?»,
      with the nasb/raf minimal pair as its ornament.

The bayt already stands whole in chapter 7 (the khabar bab read it for
its own lesson); this chapter SPLITS it at the fasl, because the split is
the lesson — the corpus reuses a witness where a second bab teaches from
the same words (the لَا رَيْبَ فِيهِ precedent).

ATTRIBUTION: s3-s4 are Yusuf 12:53 and s5 Hud 11:69 (part), received
Qur'anic text quoted exactly in standard imla as the source prints them;
s1-s2 are the bayt the source cites, verbatim, in verse dress. Ottoman
orthography normalized to standard — recorded normalizations.

Grammar this chapter teaches:
  • note 137 `shibh-kamal-al-ittisal` — the isti'naf's three kinds,
    Sakkaki's nukta, the omitted-mubtada answers, and the mubalagha of
    the sifa-built answer (in the explanation).
  • new paradigms: بَرَّأَ (Form II hamza-lam, the istahzaa seat
    conventions already stored in this package).
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

TITLE34 = {"ar": "شِبْهُ كَمَالِ الِاتِّصَالِ — الِاسْتِئْنَافُ",
           "en": "The Isti'naf: Answering the Unasked Question",
           "tr": "İsti'nâf: Sorulmamış Soruyu Cevaplamak"}

# ------------------------- s1 — the bayt's first hemistich: the question asked
S.append({"id": "s1", "translation": {
 "en": "He said to me: how are you? I said: ill —",
 "tr": "Bana dedi ki: nasılsın? Dedim ki: hastayım —"},
 "tokens": [
  tok("قَالَ","qala","verb",["shibh-kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ.",
      "«he said» — a mazi on the fatha, its doer concealed.",
      "«dedi» — fetha üzere mebnî mâzî; fâili gizli."),
  tok("لِي","li","part",["shibh-kamal-al-ittisal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِقَالَ.",
      "«to me» — the jarr phrase on the verb.",
      "«bana» — fiile taalluk eden câr-mecrûr.",
      segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("كَيْفَ","kayfa","noun",["shibh-kamal-al-ittisal","adawat-al-tasawwur"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.",
      "«how» — the interrogative noun of STATE, mabni, fronted as the khabar.",
      "«nasıl» — hâl soran soru ismi; mebnî, öne alınmış haber."),
  tok("أَنْتَ","anta","pron",["shibh-kamal-al-ittisal"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
      "«you» — the detached pronoun, the deferred mubtada.",
      "«sen» — munfasıl zamir; ertelenmiş mübtedâ."),
  tok("قُلْتُ","qala","verb",["shibh-kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ.",
      "«I said» — mabni on the sukun for the doer's ta; the ta is the fa'il.",
      "«dedim» — fâil tâsına bitiştiği için sükûn üzere mebnî; tâ fâildir."),
  tok("عَلِيلٌ","alil","noun",["shibh-kamal-al-ittisal"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ أَنَا، مَرْفُوعٌ بِالضَّمَّةِ.",
      "«ill» — the khabar of an omitted mubtada (I am: أَنَا عَلِيلٌ), marfu'. And the word ILL provokes the question the next hemistich will answer.",
      "«hasta» — mahzûf mübtedânın haberi (takdiri: أَنَا عَلِيلٌ); merfû. Ve HASTA kelimesi, bir sonraki mısraın cevaplayacağı soruyu doğurur.",
      punct="•")],
 "jumal": [
  J("كَيْفَ أَنْتَ",
    "مَقُولُ الْقَوْلِ الْأَوَّلِ — فِي مَحَلِّ نَصْبٍ.",
    "The friend's question, quoted — in nasb as what he said.",
    "Arkadaşın sorusu, aktarılmış — dediği olarak mahallen mansub."),
  J("قُلْتُ عَلِيلٌ",
    "الْجَوَابُ الْمُجْمَلُ — وَهُوَ يُوَلِّدُ سُؤَالًا جَدِيدًا: مَا سَبَبُ عِلَّتِكَ؟",
    "The summary answer — and «ill» BREEDS a new question: what is the cause of your illness? The unasked question is the fasl's whole machinery.",
    "Özet cevap — ve «hasta», YENİ bir soru doğurur: hastalığının sebebi ne? Sorulmamış soru, faslın bütün mekanizmasıdır.")]})

# -------------------- s2 — the second hemistich: the isti'naf of kind ONE
S.append({"id": "s2", "translation": {
 "en": "— constant sleeplessness and a long sorrow. (the ISTI'NAF, kind 1: it answers the general-cause question the first jumla provoked, so no letter joins them.)",
 "tr": "— sürekli uykusuzluk ve uzun bir hüzün. (İSTİ'NÂF, 1. kısım: ilk cümlenin doğurduğu genel-sebep sorusunu cevaplar; araya harf girmez.)"},
 "tokens": [
  tok("سَهَرٌ","sahar","noun",["shibh-kamal-al-ittisal"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ سَبَبُ عِلَّتِي، مَرْفُوعٌ بِالضَّمَّةِ.",
      "«sleeplessness» — the khabar of an OMITTED mubtada the source itself names: «the cause of my illness is…». The answer wears the question's frame with the question rubbed out.",
      "«uykusuzluk» — kaynağın bizzat adlandırdığı MAHZUF mübtedânın haberi: «hastalığımın sebebi…dir». Cevap, sorusu silinmiş soru çerçevesini giyer."),
  tok("دَائِمٌ","daim","noun",["shibh-kamal-al-ittisal"],
      "صِفَةٌ لِسَهَرٌ مَرْفُوعَةٌ.",
      "«constant» — sahar's sifa, following it in raf'.",
      "«sürekli» — سَهَرٌ'un sıfatı; ref'te ona tâbi."),
  tok("وَحُزْنٌ","huzn","noun",["shibh-kamal-al-ittisal"],
      "الْوَاوُ عَاطِفَةٌ، وَحُزْنٌ مَعْطُوفٌ عَلَى سَهَرٌ مَرْفُوعٌ.",
      "«and a sorrow» — joined onto «sleeplessness» (a mufrad join inside the answer — the bab's shart binds jumlas, not these).",
      "«ve bir hüzün» — «uykusuzluk» üzerine atfedilmiş (cevabın içinde müfred atfı — bâbın şartı cümleleri bağlar, bunları değil).",
      segments=[seg("وَ","wa","part"), seg("حُزْنٌ","huzn","noun")]),
  tok("طَوِيلٌ","tawil-long","noun",["shibh-kamal-al-ittisal"],
      "صِفَةٌ لِحُزْنٌ مَرْفُوعَةٌ.",
      "«long» — huzn's sifa.",
      "«uzun» — حُزْنٌ'un sıfatı.",
      punct="•")],
 "jumal": [
  J("سَهَرٌ دَائِمٌ وَحُزْنٌ طَوِيلٌ",
    "جُمْلَةٌ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا — فُصِلَتْ لِشِبْهِ كَمَالِ الِاتِّصَالِ.",
    "THE ISTI'NAF: the first jumla was lowered to a question's rank, and an answer is never JOINED to its question — kind 1: the question asks the general cause of the hukm.",
    "İSTİ'NÂF: ilk cümle soru makamına indirildi ve cevap, sorusuna asla ATFEDİLMEZ — 1. kısım: soru, hükmün genel sebebini sorar."),
  J("سَهَرٌ",
    "خَبَرٌ حُذِفَ مُبْتَدَؤُهُ — سَبَبُ عِلَّتِي سَهَرٌ.",
    "Sakkaki's nukta rides the hadhf: the speaker leaves no room for the asking — the answer arrives before the question is spoken.",
    "Hazfin üstünde Sekkâkî'nin nüktesi: konuşan, sormaya yer bırakmaz — cevap, soru söylenmeden gelir.")]})

# -------------------- s3 — Yusuf 12:53a: the hukm that provokes kind TWO
S.append({"id": "s3", "translation": {
 "en": "And I do not absolve my own nafs. (Yusuf 12:53 — the hukm; it provokes: does every nafs so command evil?)",
 "tr": "Ben nefsimi temize çıkarmam. (Yûsuf 12:53 — hüküm; şu soruyu doğurur: her nefis kötülüğü böyle mi emreder?)"},
 "tokens": [
  tok("وَمَا","ma-nafiya","part",["shibh-kamal-al-ittisal"],
      "الْوَاوُ عَاطِفَةٌ عَلَى مَا قَبْلَهَا فِي الْآيَاتِ، وَمَا نَافِيَةٌ.",
      "«and not» — the waw joins the aya's train; ma negates and governs nothing.",
      "«ve …mam» — vâv, âyet zincirine bağlar; mâ nefyeder, amel etmez.",
      segments=[seg("وَ","wa","part"), seg("مَا","ma-nafiya","part")]),
  tok("أُبَرِّئُ","barraa","verb",["shibh-kamal-al-ittisal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنَا.",
      "«I absolve» — a Form II mudari (its lam a hamza), marfu'; the doer is the concealed I.",
      "«temize çıkarırım» — II. bâbdan muzâri (lâmı hemze); merfû; fâili gizli ben."),
  tok("نَفْسِي","nafs","noun",["shibh-kamal-al-ittisal"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.",
      "«my nafs» — the object, its fatha estimated before the speaker's ya; the ya is the mudaf ilayh.",
      "«nefsimi» — mef'ûl; fethası mütekellim yâsından önce takdîrî; yâ muzâfun ileyhtir.",
      punct=".", segments=[seg("نَفْسِ","nafs","noun"), seg("ي","pron-1s","pron")])],
 "jumal": [
  J("وَمَا أُبَرِّئُ نَفْسِي",
    "جُمْلَةٌ مَنْفِيَّةٌ — الْحُكْمُ الَّذِي يُوَلِّدُ السُّؤَالَ الْخَاصَّ.",
    "The refusal to self-absolve — and it provokes the SPECIFIC question: is the nafs really such a commander of evil?",
    "Kendini aklamayı reddediş — ve ÖZEL soruyu doğurur: nefis gerçekten kötülüğün böyle bir âmiri mi?"),
  J("نَفْسِي",
    "مَفْعُولٌ بِهِ مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ.",
    "The speaker's own nafs — the honesty that makes the coming ta'kid necessary.",
    "Konuşanın kendi nefsi — gelecek te'kîdi gerekli kılan dürüstlük.")]})

# -------------------- s4 — Yusuf 12:53b: the isti'naf of kind TWO, with ta'kid
S.append({"id": "s4", "translation": {
 "en": "Indeed the nafs commands evil incessantly. (the ISTI'NAF, kind 2: answering the specific-cause question — and this kind DEMANDS the ta'kid: inna and the sliding lam.)",
 "tr": "Şüphesiz nefis, kötülüğü durmadan emreder. (İSTİ'NÂF, 2. kısım: özel-sebep sorusunun cevabı — ve bu kısım TE'KÎD ister: inne ve kayan lâm.)"},
 "tokens": [
  tok("إِنَّ","inna","part",["shibh-kamal-al-ittisal","inna-wa-akhawatuha"],
      "حَرْفٌ نَاسِخٌ لِلتَّوْكِيدِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "«indeed» — the emphasizing nasikh: nasb on its ism, raf' on its khabar. Kind-2 isti'naf carries emphasis, because the unasked question doubted.",
      "«şüphesiz» — te'kîd eden nâsih: ismini nasb, haberini raf eder. 2. kısım isti'nâf te'kîd taşır; çünkü sorulmamış soru şüphe etmişti."),
  tok("النَّفْسَ","nafs","noun",["shibh-kamal-al-ittisal","inna-wa-akhawatuha"],
      "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«the nafs» — inna's ism, mansub by the plain fatha.",
      "«nefis» — إِنَّ'nin ismi; açık fethayla mansub."),
  tok("لَأَمَّارَةٌ","ammara","noun",["shibh-kamal-al-ittisal","inna-wa-akhawatuha"],
      "اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَأَمَّارَةٌ خَبَرُ إِنَّ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَعَّالَةٍ.",
      "«surely a commander» — the SLIDING LAM of emphasis (pushed off the ism onto the khabar), then inna's khabar, marfu' — a mubalagha on فَعَّالَة: not one that commands, one that COMMANDS AND COMMANDS.",
      "«elbette çok emredici» — te'kîdin KAYAN LÂMI (isimden habere itilmiş), sonra إِنَّ'nin haberi, merfû — فَعَّالَة vezninde mübalağa: emreden değil, EMREDİP DURAN.",
      segments=[seg("لَ","li","part"), seg("أَمَّارَةٌ","ammara","noun")]),
  tok("بِالسُّوءِ","su","noun",["shibh-kamal-al-ittisal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَمَّارَةٌ.",
      "«evil» — the jarr phrase hanging on the mubalagha itself.",
      "«kötülüğü» — mübalağanın kendisine taalluk eden câr-mecrûr.",
      punct=".", segments=[seg("بِ","bi","part"), seg("السُّوءِ","su","noun")])],
 "jumal": [
  J("إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ",
    "جُمْلَةٌ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا — فُصِلَتْ لِشِبْهِ كَمَالِ الِاتِّصَالِ، وَفِيهَا التَّوْكِيدُ الَّذِي يَقْتَضِيهِ هَذَا الْقِسْمُ.",
    "THE ISTI'NAF, kind 2 — and the source's own rule shows on its face: an answer to a doubting question arrives ARMED, inna at its head and the lam slid onto its khabar.",
    "İSTİ'NÂF, 2. kısım — ve kaynağın kuralı yüzünde görünür: şüphe eden sorunun cevabı SİLAHLI gelir; başında inne, haberine kaymış lâm."),
  J("لَأَمَّارَةٌ",
    "اللَّامُ الْمُزَحْلَقَةُ عَلَى الْخَبَرِ.",
    "The lam wanted the ism's head; inna took that seat, so the lam SLID to the khabar — two emphases stacked on one clause.",
    "Lâm, ismin başını istedi; o makamı inne aldı, lâm da habere KAYDI — tek cümlede üst üste iki te'kîd.")]})

# -------------------- s5 — Hud 11:69: the isti'naf of kind THREE
S.append({"id": "s5", "translation": {
 "en": "They said: peace. He said: peace. (Hud 11:69 — the ISTI'NAF, kind 3: «what did he answer?» — and the raf' of his reply outlasts the nasb of their greeting.)",
 "tr": "«Selâm» dediler. O da «selâm» dedi. (Hûd 11:69 — İSTİ'NÂF, 3. kısım: «ne cevap verdi?» — ve cevabının ref'i, selâmlarının nasbından uzun ömürlüdür.)"},
 "tokens": [
  tok("قَالُوا","qala","verb",["shibh-kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.",
      "«they said» — mabni on the damm for the group's waw; the waw is the doer (the angel guests).",
      "«dediler» — cemaat vâvına bitiştiği için damme üzere mebnî; vâv fâildir (melek misafirler)."),
  tok("سَلَامًا","salam","noun",["shibh-kamal-al-ittisal"],
      "مَنْصُوبٌ بِفِعْلٍ مَحْذُوفٍ — التَّقْدِيرُ: سَلَّمْنَا سَلَامًا.",
      "«peace» — MANSUB by an omitted verb (we greet: سَلَّمْنَا سَلَامًا): the passing greeting of travellers, an event that ends.",
      "«selâm» — mahzûf fiille MANSUB (takdiri: سَلَّمْنَا سَلَامًا): yolcuların geçici selâmı; biten bir hadise."),
  tok("قَالَ","qala","verb",["shibh-kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ — وَلَا عَاطِفَ قَبْلَهُ.",
      "«he said» — Ibrahim's reply, and NO atf letter stands before it: the fasl of the answered question.",
      "«dedi» — İbrâhîm'in cevabı; önünde HİÇBİR atıf harfi yok: cevaplanmış sorunun faslı."),
  tok("سَلَامٌ","salam","noun",["shibh-kamal-al-ittisal"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ — التَّقْدِيرُ: أَمْرِي سَلَامٌ — مَرْفُوعٌ بِالضَّمَّةِ.",
      "«peace» — MARFU', the khabar of an omitted mubtada (my state IS peace): the nominal clause abides where their verbal greeting passed. One tanwin apart, a whole ranking of hospitality.",
      "«selâm» — MERFÛ; mahzûf mübtedânın haberi (hâlim selâmdır): isim cümlesi kalıcıdır, onların fiil selâmı geçip gitti. Tek tenvin farkı, koca bir ikram sıralaması.",
      punct=".")],
 "jumal": [
  J("قَالَ سَلَامٌ",
    "جُمْلَةٌ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا — جَوَابُ: فَمَاذَا قَالَ؟",
    "THE ISTI'NAF, kind 3: the question asks neither cause — only «and what did he say?» — and the answer is cut loose from the telling.",
    "İSTİ'NÂF, 3. kısım: soru sebep sormaz — yalnız «peki o ne dedi?» — ve cevap, anlatıştan koparılır."),
  J("سَلَامًا … سَلَامٌ",
    "النَّصْبُ لِلْحُدُوثِ وَالرَّفْعُ لِلثُّبُوتِ.",
    "The pair the mufassirun treasure: their nasb is a deed that happens and ends; his raf' is a state that stands — the reply outranks the greeting by one damma.",
    "Müfessirlerin hazinesi olan çift: onların nasbı olup biten bir fiildir; onun ref'i duran bir hâldir — cevap, selâmı tek dammeyle geçer.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "barraa": g("بَرَّأَ", "ب ر أ", "verb", "to absolve, declare innocent", "temize çıkarmak, aklamak", 5, form="II"),
 "ammara": g("أَمَّارَة", "أ م ر", "noun", "one who commands incessantly (mubalagha of آمِر)", "durmadan emreden (آمِر'in mübalağası)", 5),
 "su": copy_gloss("bad-al-amali", "su"),
 "salam": copy_gloss("kitab-al-sulh", "salam"),
 "ma-nafiya": copy_gloss("wasiyyat-abi-hanifa-samti", "ma-nafiya"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/34.json").write_text(
    json.dumps({"chapter": 34, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 34 for c in man["chapters"]):
    man["chapters"].append({"n": 34, "title": TITLE34})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.34.0"
ADD_EN = (" Chapter 34 carries the isti'naf (lines ~2378-2400, sahifa 82-83): s3-s4 are Yusuf "
          "12:53 and s5 Hud 11:69 (part), received Qur'anic text quoted exactly in standard "
          "imla as the source prints them; s1-s2 are the bayt the source cites, verbatim, split "
          "at its hemistich because the fasl falls there — the bayt also stands whole in "
          "chapter 7, where the khabar bab read it for its own lesson (a recorded reuse). "
          "Ottoman orthography normalized to standard — recorded normalizations.")
ADD_TR = (" Otuz dördüncü bâb isti'nâfı taşır (satır ~2378-2400, sahife 82-83): s3-s4 Yûsuf "
          "12:53, s5 Hûd 11:69 (kısmen) — kaynağın bastığı standart imlâ ile aynen alınmış "
          "mervî Kur'ân metni; s1-s2, kaynağın iktibas ettiği beytin aynen alınmışıdır ve "
          "mısra başında bölünmüştür, çünkü fasl oraya düşer — beyit, haber bâbının kendi dersi "
          "için okuduğu 7. bâbda bütün hâliyle de durur (kayıtlı bir yeniden kullanım). Osmanlı "
          "imlâsı standart imlâya çevrildi — kayıtlı normalizasyonlardır.")
if "2378-2400" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "barraa" not in mo["verbs"]:
    # Form II with a hamza lam — the istahzaa seat conventions this package
    # already stores (the mechanical dual بَرَّأَا, hamza kept on its alif
    # seat in the mazi, on the ya seat where kasra precedes).
    mo["verbs"]["barraa"] = _sg.derived(
        _sg.B2, _sg.W2, "ُ", "بَرَّأ", "بَرِّئ", "بَرِّئ",
        "تَبْرِئَة", "مُبَرِّئ", "مُبَرَّأ", "بُرِّئَ", "يُبَرَّأُ")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 137
GR = ROOT / "content/grammar"
NOTE137 = {
 "id": "shibh-kamal-al-ittisal",
 "title": {"ar": "شِبْهُ كَمَالِ الِاتِّصَالِ — الِاسْتِئْنَافُ",
           "en": "The isti'naf: answering the unasked question",
           "tr": "İsti'nâf: sorulmamış soruyu cevaplamak"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — دواعي الفصل: شبه كمال الاتصال"],
 "question": {
  "en": ["Did the first jumla provoke a question its hearer would ask? Then the second, if it answers it, is an ISTI'NAF — and an answer is never joined to its question.",
         "Does the answer arrive armed with inna and the lam? Kind 2: the unasked question doubted.",
         "Is the answer's mubtada rubbed out — سَهَرٌ دَائِمٌ for «the cause is…»? Sakkaki's nukta: no room is left for the asking."],
  "tr": ["İlk cümle, dinleyenin soracağı bir soru doğurdu mu? İkincisi onu cevaplıyorsa İSTİ'NÂFTIR — ve cevap, sorusuna asla atfedilmez.",
         "Cevap, inne ve lâm ile silahlı mı geliyor? 2. kısım: sorulmamış soru şüphe etmişti.",
         "Cevabın mübtedâsı silinmiş mi — «sebep …dir» yerine سَهَرٌ دَائِمٌ? Sekkâkî'nin nüktesi: sormaya yer bırakılmaz."]},
 "plain": {
  "en": "When the first jumla breeds a question — «ill» breeds «why?» — the second answers it, and an answer is cut loose from its question: the isti'naf. Three kinds: the general cause (the bayt), the specific cause (إِنَّ النَّفْسَ لَأَمَّارَةٌ — armed with ta'kid), or something else (قَالُوا سَلَامًا قَالَ سَلَامٌ).",
  "tr": "İlk cümle bir soru doğurduğunda — «hasta», «neden?»i doğurur — ikincisi onu doğrudan cevaplayabilir ve cevap, sorusundan koparılır: isti'nâf budur. Sorulana göre üç kısım: genel sebep (beyit), özel sebep (إِنَّ النَّفْسَ لَأَمَّارَةٌ — te'kîdle silahlı) veya bambaşka bir şey (قَالُوا سَلَامًا قَالَ سَلَامٌ)."},
 "explanation": {
  "en": "SHIBH KAMAL AL-ITTISAL: the first jumla is lowered to the rank of a QUESTION — because it provokes one — and the second stands as its answer, cut loose as every answer is from every question. Sakkaki's nukta: the speaker answers before the asking, leaving the hearer no need to ask, or sparing him the asking's embarrassment. THREE KINDS by what the provoked question asks. (1) The GENERAL cause: قُلْتُ عَلِيلٌ breeds «what is the cause of your illness?», and سَهَرٌ دَائِمٌ وَحُزْنٌ طَوِيلٌ answers with its mubtada (سَبَبُ عِلَّتِي) omitted. (2) The SPECIFIC cause: وَمَا أُبَرِّئُ نَفْسِي breeds «is the nafs really such?», and إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ (Yusuf 12:53) answers — and THIS kind demands the ta'kid, inna with the sliding lam, because the question carried doubt. (3) OTHER than the cause: قَالُوا سَلَامًا breeds «and what did he reply?», and قَالَ سَلَامٌ (Hud 11:69) answers — with the mufassirun's treasured pair: their greeting mansub (a deed that passes), his reply marfu' (a state that abides). The isti'naf may repeat the asked-about's NAME (زَيْدٌ حَقِيقٌ بِالْإِحْسَانِ), or build on its SIFA for the stronger claim (صَدِيقُكَ الْقَدِيمُ أَهْلٌ لِذَلِكَ), and its head — or its whole — may be omitted where a qarina stands (يُسَبِّحُهُ dropped before رِجَالٌ, an-Nur 24:36).",
  "tr": "ŞİBH-İ KEMÂL-İ İTTİSÂL: ilk cümle — bir soru doğurduğu için — SORU makamına indirilir; ikincisi cevabı olarak durur ve her cevabın her sorudan koparıldığı gibi koparılır. Sekkâkî'nin nüktesi: konuşan, sorulmadan cevaplar — dinleyene sorma ihtiyacı bırakmaz veya sorma mahcubiyetinden esirger. Doğan sorunun sorduğuna göre ÜÇ KISIM. (1) GENEL sebep: قُلْتُ عَلِيلٌ, «hastalığının sebebi ne?»yi doğurur; سَهَرٌ دَائِمٌ وَحُزْنٌ طَوِيلٌ, mübtedâsı (سَبَبُ عِلَّتِي) hazfedilmiş olarak cevaplar. (2) ÖZEL sebep: وَمَا أُبَرِّئُ نَفْسِي, «nefis gerçekten böyle mi?»yi doğurur; إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ (Yûsuf 12:53) cevaplar — ve BU kısım te'kîd ister: inne ve kayan lâm, çünkü soru şüphe taşıyordu. (3) Sebebin GAYRİSİ: قَالُوا سَلَامًا, «peki ne cevap verdi?»yi doğurur; قَالَ سَلَامٌ (Hûd 11:69) cevaplar — müfessirlerin hazinesi çiftle: selâmları mansub (geçen bir fiil), cevabı merfû (duran bir hâl). İsti'nâf, sorulanın ADINI iade edebilir (زَيْدٌ حَقِيقٌ بِالْإِحْسَانِ) veya daha kuvvetli iddia için SIFATI üzerine kurulabilir (صَدِيقُكَ الْقَدِيمُ أَهْلٌ لِذَلِكَ); karîne varsa başı — veya tamamı — hazfedilir (يُسَبِّحُهُ'nun رِجَالٌ'dan önce düşmesi, Nûr 24:36)."},
 "examples": [
  {"ar": "سَهَرٌ دَائِمٌ وَحُزْنٌ طَوِيلٌ",
   "en": "kind 1 — the general cause, its mubtada omitted.",
   "tr": "1. kısım — genel sebep; mübtedâsı mahzuf.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ",
   "en": "kind 2 — the doubting question answered with double ta'kid (12:53).",
   "tr": "2. kısım — şüphe eden soruya çift te'kîdle cevap (12:53).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "قَالُوا سَلَامًا قَالَ سَلَامٌ",
   "en": "kind 3 — «what did he say?»; nasb passes, raf' abides (11:69).",
   "tr": "3. kısım — «ne dedi?»; nasb geçer, ref kalır (11:69).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«İsti'nâf, konuyla ilgisiz yeni bir başlangıçtır»",
   "right": "«İsti'nâf, ilk cümlenin DOĞURDUĞU sorunun cevabıdır»",
   "why": {"en": "A random fresh start would be kamal inqita' — difference of kind. The isti'naf is TIED to the first jumla, more tightly than a waw could tie it: it answers the very question the first jumla planted in the hearer, which is why the books call this a RESEMBLANCE of perfect union.",
           "tr": "Alâkasız taze bir başlangıç kemâl-i inkıtâ olurdu — tür farkı. İsti'nâf ilk cümleye, vâvın bağlayabileceğinden daha sıkı BAĞLIDIR: ilk cümlenin dinleyene ektiği sorunun tam kendisini cevaplar; kitapların buna kemâl-i ittisâlin BENZERİ demesi bundandır."}}],
 "relatedNotes": ["al-fasl-wa-al-wasl", "kamal-al-ittisal", "inna-wa-akhawatuha", "khabar-fi-mana-al-insha"]}

(GR / "shibh-kamal-al-ittisal.json").write_text(
    json.dumps(NOTE137, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch34:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + barraa; note 137")
