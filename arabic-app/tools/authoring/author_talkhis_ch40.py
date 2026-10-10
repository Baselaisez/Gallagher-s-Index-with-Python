# -*- coding: utf-8 -*-
"""Author chapter 40 of talkhis-al-miftah — أَسْبَابُ الْإِطْنَابِ.

Sahifa 96-98 (lines ~2800-2845): itnab comes by occasions, and the
source counts them —

  • ÎDAH AFTER IBHAM: the meaning shown twice, veiled then clear, so
    it settles — رَبِّ اشْرَحْ لِي صَدْرِي (Ta-Ha 20:25): اشْرَحْ لِي
    asks an opening of SOMETHING; صَدْرِي is its tafsir. The ni'ma bab
    joins this kind on one reading (نِعْمَ زَيْدٌ would have sufficed).
    TAWSHI' belongs here: ending the speech with a dual explained by
    two nouns, the second joined to the first — the hadith يَشِيبُ
    ابْنُ آدَمَ وَيَشِبُّ فِيهِ خَصْلَتَانِ: الْحِرْصُ وَطُولُ الْأَمَلِ.
  • THE KHASS AFTER THE 'AMM, alerting to its excellence:
    حَافِظُوا عَلَى الصَّلَوَاتِ وَالصَّلَاةِ الْوُسْطَى (2:238).
  • TAKRIR for a point, like doubling a warning: كَلَّا سَوْفَ
    تَعْلَمُونَ ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ (102:3-4) — and the
    ثُمَّ says the second warning is the stronger.
  (Ighal — sealing the bayt with a surplus point — is the next slice.)

ATTRIBUTION: s1 is Ta-Ha 20:25 (part), s3 al-Baqara 2:238 (part),
s4-s5 al-Takathur 102:3-4 — received Qur'anic text quoted exactly in
standard imla as the source prints them; s2 is the hadith as the
source recites it.

Grammar this chapter teaches:
  • note 144 `asbab-al-itnab` — the occasions, with tawshi's verbatim
    definition and the ni'ma-bab remark.
  • new paradigms: شَابَ يَشِيبُ (hollow ya) and شَبَّ يَشِبُّ
    (geminate — bank checked before trusting, per doctrine); شَرَحَ.
  • the engine's كَلَّا: its own rad'-wa-zajr face (the kaf's kasra
    names كِلَا the dual; unvowelled stays unsure).
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

TITLE40 = {"ar": "أَسْبَابُ الْإِطْنَابِ",
           "en": "The Occasions of Amplification",
           "tr": "Itnâbın Sebepleri"}

# ------------------- s1 — Ta-Ha 20:25: idah after ibham
S.append({"id": "s1", "translation": {
 "en": "My Lord, lay open for me — my breast (20:25). The request comes veiled, then صَدْرِي unveils it: the meaning seen twice settles deeper — idah after ibham.",
 "tr": "Rabbim, benim için aç — göğsümü (20:25). İstek önce örtülü gelir, sonra صَدْرِي örtüyü kaldırır: iki kez görülen mânâ daha derin yerleşir — ibhâmdan sonra îzâh."},
 "tokens": [
  tok("رَبِّ","rabb","noun",["asbab-al-itnab","vocative-munada","ya-al-mutakallim"],
      "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ وَالْكَسْرَةُ دَلِيلُهَا — مَنْصُوبٌ مَحَلًّا.",
      "«my Lord» — the trimmed vocative: the ya is gone and its kasra stands witness.",
      "«Rabbim» — kısaltılmış nidâ: yâ düşmüş, kesresi şahit kalmıştır."),
  tok("اشْرَحْ","sharaha","verb",["asbab-al-itnab","imperative-amr"],
      "فِعْلُ أَمْرٍ — دُعَاءً — مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ أَنْتَ.",
      "«lay open» — the amr of supplication: a request for the opening of… something, as yet unnamed.",
      "«aç» — duâ emri: bir şeyin açılması istenir — henüz adı konmamış bir şeyin."),
  tok("لِي","li","part",["asbab-al-itnab"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِاشْرَحْ — وَإِلَى هُنَا الْكَلَامُ مُبْهَمٌ.",
      "«for me» — and up to here the speech is veiled: WHAT is to be opened?",
      "«benim için» — buraya kadar söz örtülüdür: NE açılacak?",
      segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("صَدْرِي","sadr","noun",["asbab-al-itnab","ya-al-mutakallim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَهُوَ الْإِيضَاحُ بَعْدَ الْإِبْهَامِ.",
      "«my breast» — the tafsir of the veiled request: itnab, because the meaning heard twice — sought, then given — sits firm in the soul.",
      "«göğsümü» — örtülü isteğin tefsiri: ıtnâb; çünkü iki kez işitilen mânâ — önce aranır, sonra verilir — nefiste sağlam oturur.",
      punct=".")],
 "jumal": [
  J("رَبِّ اشْرَحْ لِي صَدْرِي",
    "جُمْلَةٌ دُعَائِيَّةٌ — شَاهِدُ الْإِيضَاحِ بَعْدَ الْإِبْهَامِ.",
    "Musa's prayer before Pharaoh: the model witness of idah after ibham.",
    "Mûsâ'nın Firavun öncesi duâsı: ibhâmdan sonra îzâhın baş şahidi."),
  J("صَدْرِي",
    "تَفْسِيرُ الْمُبْهَمِ — وَبِهِ تَمَّ الْإِطْنَابُ.",
    "One word carrying the unveiling — and the whole reason the sentence is longer than its core.",
    "Örtüyü kaldıran tek kelime — ve cümlenin özünden uzun oluşunun bütün sebebi.")]})

# ------------------- s2 — the tawshi' hadith
S.append({"id": "s2", "translation": {
 "en": "The son of Adam grows old, and two traits grow young in him: greed, and long hope. (TAWSHI': the speech seals with a dual, then two nouns unfold it, the second joined to the first.)",
 "tr": "Âdemoğlu yaşlanır ve onda iki haslet gençleşir: hırs ve tûl-i emel. (TEVŞÎ': söz bir tesniye ile mühürlenir, sonra iki isim onu açar — ikincisi birincisine atfedilmiş.)"},
 "tokens": [
  tok("يَشِيبُ","shaba","verb",["asbab-al-itnab","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«grows grey» — the hollow ya verb of aging.",
      "«ağarır, kocar» — yaşlanmanın ecvef-i yâîsi."),
  tok("ابْنُ","ibn","noun",["asbab-al-itnab","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the son of» —",
      "«oğlu» —"),
  tok("آدَمَ","aadam","propn",["asbab-al-itnab","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "«Adam» — jarr worn as a fatha: the diptote name.",
      "«Âdem» — fetha ile cer: gayr-i munsarif isim."),
  tok("وَيَشِبُّ","shabba","verb",["asbab-al-itnab","doubled-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَيَشِبُّ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — ضِدُّ يَشِيبُ مِنْ جِذْرٍ مُضَاعَفٍ.",
      "«and grows young» — the geminate verb, set against يَشِيبُ letter for letter: the hadith's own tibaq.",
      "«ve gençleşir» — muzâaf fiil; يَشِيبُ'un harfi harfine karşısında: hadisin kendi tıbâkı.",
      segments=[seg("وَ","wa","part"), seg("يَشِبُّ","shabba","verb")]),
  tok("فِيهِ","fi","part",["asbab-al-itnab"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيَشِبُّ.",
      "«in him» —",
      "«onda» —",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("خَصْلَتَانِ","khasla","noun",["asbab-al-itnab","al-muthanna"],
      "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى — وَهُوَ الْمُبْهَمُ الَّذِي سَيُفَسَّرُ.",
      "«two traits» — the dual at the speech's seat: tawshi's veiled word, waiting to be unfolded.",
      "«iki haslet» — sözün oturağındaki tesniye: tevşî'in örtülü kelimesi, açılmayı bekler.",
      punct=":"),
  tok("الْحِرْصُ","hirs","noun",["asbab-al-itnab","badal"],
      "بَدَلٌ مِنْ خَصْلَتَانِ مَرْفُوعٌ، وَقِيلَ خَبَرُ مُبْتَدَأٍ مَحْذُوفٍ أَيْ هُمَا — أَوَّلُ الِاسْمَيْنِ الْمُفَسِّرَيْنِ.",
      "«greed» — the first of the two unfolding nouns.",
      "«hırs» — açan iki ismin birincisi."),
  tok("وَطُولُ","tul","noun",["asbab-al-itnab","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَطُولُ مَعْطُوفٌ عَلَى الْحِرْصُ مَرْفُوعٌ وَهُوَ مُضَافٌ — كَمَا نَصَّ حَدُّ التَّوْشِيعِ: ثَانِيهِمَا مَعْطُوفٌ عَلَى الْأَوَّلِ.",
      "«and the length of» — the second noun, JOINED to the first exactly as tawshi's definition demands.",
      "«ve uzunluğu» — ikinci isim, tevşî' tarifinin istediği gibi birincisine ATFEDİLMİŞ.",
      segments=[seg("وَ","wa","part"), seg("طُولُ","tul","noun")]),
  tok("الْأَمَلِ","amal","noun",["asbab-al-itnab"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«hope» — hope that outlives the strength to chase it.",
      "«emelin» — peşinden koşacak güçten uzun yaşayan emel.",
      punct=".")],
 "jumal": [
  J("يَشِيبُ ابْنُ آدَمَ وَيَشِبُّ فِيهِ خَصْلَتَانِ",
    "جُمْلَتَانِ مُتَعَاطِفَتَانِ — وَفِي عَجُزِ الْكَلَامِ الْمُثَنَّى الْمُبْهَمُ.",
    "Aging and growing-young set side by side, and the dual left veiled at the seat: the tawshi' frame.",
    "Yaşlanma ile gençleşme yan yana; oturakta örtülü tesniye: tevşî' çerçevesi."),
  J("الْحِرْصُ وَطُولُ الْأَمَلِ",
    "الِاسْمَانِ الْمُفَسِّرَانِ — ثَانِيهِمَا مَعْطُوفٌ عَلَى الْأَوَّلِ.",
    "The two nouns that open the dual — the definition of tawshi' enacted word by word.",
    "Tesniyeyi açan iki isim — tevşî' tarifi kelime kelime sahnede.")]})

# ------------------- s3 — Baqara 2:238: the khass after the 'amm
S.append({"id": "s3", "translation": {
 "en": "Guard the prayers — and the MIDDLE prayer (2:238): the special named after the general, to alert to its excellence, as if it were of another kind altogether.",
 "tr": "Namazları koruyun — ve ORTA namazı (2:238): husûsî olan, umûmîden sonra anılır ki faziletine dikkat çekilsin — sanki başka bir cinstenmiş gibi."},
 "tokens": [
  tok("حَافِظُوا","hafaza","verb",["asbab-al-itnab","form-iii-verbs","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«guard» — Form III's amr to the community: keep up, persistently.",
      "«koruyun» — III. bâbın cemaate emri: devamlı gözetin."),
  tok("عَلَى","ala","part",["asbab-al-itnab"],
      "حَرْفُ جَرٍّ.",
      "«over» —",
      "«üzerine» —"),
  tok("الصَّلَوَاتِ","salat","noun",["asbab-al-itnab","jam-muannath-salim"],
      "مَجْرُورٌ بِعَلَى بِالْكَسْرَةِ — وَهُوَ الْعَامُّ.",
      "«the prayers» — ALL of them: the general word.",
      "«namazları» — HEPSİNİ: umûmî kelime."),
  tok("وَالصَّلَاةِ","salat","noun",["asbab-al-itnab","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالصَّلَاةِ مَعْطُوفٌ مَجْرُورٌ — عَطْفُ الْخَاصِّ عَلَى الْعَامِّ تَنْبِيهًا عَلَى فَضْلِهِ.",
      "«and the prayer» — already inside «the prayers», yet named again: the khass joined to the 'amm is itnab with a purpose.",
      "«ve namazı» — «namazlar»ın zaten içindeydi, yine de anılır: hâssın âmma atfı, maksatlı ıtnâbdır.",
      segments=[seg("وَ","wa","part"), seg("الصَّلَاةِ","salat","noun")]),
  tok("الْوُسْطَى","wusta","noun",["asbab-al-itnab","naat-sifa","ism-maqsur-manqus"],
      "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَقَالَ قَوْمٌ هِيَ الصُّبْحُ وَقَالَ قَوْمٌ هِيَ الْعَصْرُ.",
      "«the middle» — the maqsura hides its kasra; and the scholars differ on which prayer is meant: fajr, said some; 'asr, said others.",
      "«orta» — maksûre kesresini gizler; hangi namaz olduğunda ihtilâf vardır: kimi sabah dedi, kimi ikindi.",
      punct=".")],
 "jumal": [
  J("حَافِظُوا عَلَى الصَّلَوَاتِ وَالصَّلَاةِ الْوُسْطَى",
    "جُمْلَةٌ طَلَبِيَّةٌ — شَاهِدُ ذِكْرِ الْخَاصِّ بَعْدَ الْعَامِّ.",
    "The khass-after-'amm witness: the change in description is lowered to the rank of a change in essence.",
    "Âmdan sonra hâs şahidi: vasıftaki fark, zâttaki fark makamına indirilir."),
  J("وَالصَّلَاةِ الْوُسْطَى",
    "الْخَاصُّ الْمَعْطُوفُ — كَأَنَّهُ لَيْسَ مِنْ جِنْسِ الْعَامِّ.",
    "As if the middle prayer were not of the prayers' own kind — that is the alerting.",
    "Sanki orta namaz, namazlar cinsinden değilmiş gibi — dikkat çekiş budur.")]})

# ------------------- s4 — Takathur 102:3: the first warning
S.append({"id": "s4", "translation": {
 "en": "No indeed — you shall come to know (102:3).",
 "tr": "Hayır — ileride bileceksiniz (102:3)."},
 "tokens": [
  tok("كَلَّا","kalla","part",["asbab-al-itnab"],
      "حَرْفُ رَدْعٍ وَزَجْرٍ.",
      "«no indeed» — the letter that throws the boast back.",
      "«hayır, asla» — övünmeyi geri fırlatan harf."),
  tok("سَوْفَ","sawfa","part",["asbab-al-itnab"],
      "حَرْفُ اسْتِقْبَالٍ — تَنْفِيسٍ.",
      "«shall» — the far future's letter.",
      "«ileride» — uzak istikbâl harfi."),
  tok("تَعْلَمُونَ","alima","verb",["asbab-al-itnab","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«you will know» — the five-verbs raf', its nun standing firm.",
      "«bileceksiniz» — ef'âl-i hamse ref'i; nûnu yerinde durur.",
      punct=".")],
 "jumal": [
  J("كَلَّا سَوْفَ تَعْلَمُونَ",
    "زَجْرٌ وَوَعِيدٌ — الْإِنْذَارُ الْأَوَّلُ.",
    "The first warning, complete in three words.",
    "İlk inzâr, üç kelimede tamam."),
  J("كَلَّا",
    "حَرْفُ الرَّدْعِ — وَبِهِ يَنْقَطِعُ التَّفَاخُرُ.",
    "One letter against the whole contest of piling up.",
    "Çokluk yarışının tamamına karşı tek harf.")]})

# ------------------- s5 — Takathur 102:4: the takrir
S.append({"id": "s5", "translation": {
 "en": "Then no indeed — you shall come to know (102:4). The repetition is itnab for a point: the warning doubled — and ثُمَّ says the second is the weightier.",
 "tr": "Sonra hayır — ileride bileceksiniz (102:4). Tekrar, bir nükte için ıtnâbdır: inzâr katlanmış — ve ثُمَّ, ikincisinin daha ağır olduğunu söyler."},
 "tokens": [
  tok("ثُمَّ","thumma","part",["asbab-al-itnab","atf-nasaq"],
      "حَرْفُ عَطْفٍ — وَفِيهِ دَلَالَةٌ عَلَى أَنَّ الْإِنْذَارَ الثَّانِيَ أَبْلَغُ مِنَ الْأَوَّلِ.",
      "«then» — the joining letter that grades the two warnings: the second outweighs.",
      "«sonra» — iki inzârı dereceleyen atıf harfi: ikincisi ağır basar."),
  tok("كَلَّا","kalla","part",["asbab-al-itnab"],
      "حَرْفُ رَدْعٍ وَزَجْرٍ — مُكَرَّرٌ لِتَأْكِيدِ الْإِنْذَارِ.",
      "«no indeed» — repeated: takrir with its nukta, not padding.",
      "«hayır, asla» — tekrarlanmış: nüktesiyle tekrîr, dolgu değil."),
  tok("سَوْفَ","sawfa","part",["asbab-al-itnab"],
      "حَرْفُ اسْتِقْبَالٍ.",
      "«shall» —",
      "«ileride» —"),
  tok("تَعْلَمُونَ","alima","verb",["asbab-al-itnab","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«you will know» — word for word the first warning: the takrir is exact.",
      "«bileceksiniz» — kelimesi kelimesine ilk inzâr: tekrîr birebirdir.",
      punct=".")],
 "jumal": [
  J("ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ",
    "تَكْرِيرُ الْإِنْذَارِ — إِطْنَابٌ لِنُكْتَةٍ.",
    "The takrir witness: the same words again, and the again IS the meaning.",
    "Tekrîr şahidi: aynı kelimeler yeniden — ve yenidenlik, mânânın tâ kendisidir."),
  J("ثُمَّ",
    "لِلدَّلَالَةِ عَلَى أَنَّ الثَّانِيَ أَبْلَغُ.",
    "Not mere sequence: a step up in severity.",
    "Sırf sıra değil: şiddette bir basamak yukarı.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "sharaha": g("شَرَحَ", "ش ر ح", "verb", "to lay open, expand; to expound", "açmak, genişletmek; şerh etmek", 3, form="I"),
 "shaba": g("شَابَ", "ش ي ب", "verb", "to grow grey with age", "saçı ağarmak, kocamak", 4, form="I"),
 "shabba": g("شَبَّ", "ش ب ب", "verb", "to be young, grow young", "genç olmak, gençleşmek", 4, form="I"),
 "hirs": g("حِرْص", "ح ر ص", "noun", "greed, avid craving", "hırs", 3),
 "tul": g("طُول", "ط و ل", "noun", "length (of hope: its stretching on)", "uzunluk (emelin uzayıp gitmesi)", 3),
 "wusta": g("وُسْطَى", "و س ط", "noun", "middlemost (fem. of أَوْسَط)", "orta, vustâ (أَوْسَط'ın müennesi)", 4),
 "kalla": g("كَلَّا", None, "part", "no indeed! (rebuke and deterrence)", "hayır, asla! (red' ve zecir)", 4),
 "sadr": copy_gloss("wasiyyat-abi-hanifa-samti", "sadr"),
 "khasla": copy_gloss("bad-al-amali", "khasla"),
 "amal": copy_gloss("bad-al-amali", "amal"),
 "sawfa": copy_gloss("bad-al-amali", "sawfa"),
 "hafaza": copy_gloss("wasiyyat-abi-hanifa-samti", "hafaza"),
 "salat": copy_gloss("wasiyyat-abi-hanifa-samti", "salat"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/40.json").write_text(
    json.dumps({"chapter": 40, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 40 for c in man["chapters"]):
    man["chapters"].append({"n": 40, "title": TITLE40})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.40.0"
ADD_EN = (" Chapter 40 opens the occasions of itnab (lines ~2800-2845, sahifa 96-98): s1 is "
          "Ta-Ha 20:25 (part), s3 al-Baqara 2:238 (part) and s4-s5 al-Takathur 102:3-4, "
          "received Qur'anic text quoted exactly in standard imla as the source prints them; "
          "s2 is the hadith of the son of Adam's two ever-young traits as the source recites "
          "it, the tawshi' witness.")
ADD_TR = (" Kırkıncı bâb ıtnâbın sebeplerini açar (satır ~2800-2845, sahife 96-98): s1 Tâhâ "
          "20:25 (kısmen), s3 Bakara 2:238 (kısmen), s4-s5 Tekâsür 102:3-4 — kaynağın "
          "bastığı standart imlâ ile aynen alınmış mervî Kur'ân metni; s2, Âdemoğlunun iki "
          "genç kalan hasleti hadisidir — kaynağın okuduğu şekliyle, tevşî' şahidi.")
if "2800-2845" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "sharaha" not in mo["verbs"]:
    mo["verbs"]["sharaha"] = _sg.sound1(
        "fataha", "شَرَح", "شْرَح", "اِشْرَح", "شَرْح", "شَارِح",
        "مَشْرُوح", "شُرِحَ", "يُشْرَحُ")
if "shaba" not in mo["verbs"]:
    # hollow ya of bab daraba, lazim — the حَاقَ road.
    mo["verbs"]["shaba"] = _sg.hollow1(
        "daraba", "أَجْوَفُ يَائِيٌّ", "شَاب", "شِب", "شِيب", "شِب", "شِيب", "شِب",
        "شَيْب", "شَائِب", None, None, None,
        "أَجْوَفُ يَائِيٌّ لَازِمٌ: شَابَ يَشِيبُ شَيْبًا.")
if "shabba" not in mo["verbs"]:
    # Form I geminate of bab daraba on the ظَنَّ road — its lam is a ba, so
    # only the تْتَ seams contract; idgham() is the standing convention.
    mo["verbs"]["shabba"] = _sg.idgham(_sg.entry(
        "مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ",
        "شَبَاب", "شَابّ",
        _sg.mazi14("شَبّ", "شَبَب"),
        _sg.mudari14("َ", "شِبّ", "شْبِب"),
        ["شِبَّ", "شِبَّا", "شِبُّوا", "شِبِّي", "شِبَّا", "اِشْبِبْنَ"],
        "يَشِبَّ", "يَشِبَّ", "تَشِبَّ",
        None, None, None,
        "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَشِبَّ، وَيَجُوزُ لَمْ يَشْبِبْ."))
if "hafaza" not in mo["verbs"]:
    src = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json").read_text(encoding="utf-8"))
    mo["verbs"]["hafaza"] = src["verbs"]["hafaza"]
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 144
GR = ROOT / "content/grammar"
NOTE144 = {
 "id": "asbab-al-itnab",
 "title": {"ar": "أَسْبَابُ الْإِطْنَابِ",
           "en": "The occasions of amplification",
           "tr": "Itnâbın sebepleri"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإطناب"],
 "question": {
  "en": ["Why is the speech longer than its core? Idah after ibham (the meaning lands twice), the khass after the 'amm (its excellence flagged), or takrir for a point?",
         "Does the speech seal with a dual that two joined nouns then unfold? That is TAWSHI' — a named kind of idah after ibham.",
         "Does the repetition carry a nukta (a doubled warning, a graded ثُمَّ)? Then it is itnab; strip the nukta and only tatwil remains."],
  "tr": ["Söz özünden niçin uzun? İbhâmdan sonra îzâh (mânâ iki kez konar), âmdan sonra hâs (fazileti işaretlenir), yahut bir nükte için tekrîr mi?",
         "Söz, sonra iki atıflı ismin açtığı bir tesniye ile mi mühürleniyor? O, TEVŞÎ'dir — îzâhın adlı bir türü.",
         "Tekrar bir nükte mi taşıyor (katlanan inzâr, dereceleyen ثُمَّ)? O hâlde ıtnâbdır; nükteyi çıkar, geriye yalnız tatvîl kalır."]},
 "plain": {
  "en": "Itnab needs a reason: IDAH AFTER IBHAM — veil the meaning, then unveil it (رَبِّ اشْرَحْ لِي… صَدْرِي); the KHASS after the 'AMM — the middle prayer named after all prayers (2:238); TAKRIR for a point — the doubled warning of 102:3-4. Tawshi' seals speech with a dual that two joined nouns unfold.",
  "tr": "Itnâb sebep ister; kaynak sayar: İBHÂMDAN SONRA ÎZÂH — mânâyı örter, sonra açarsın; yerleşir (رَبِّ اشْرَحْ لِي… صَدْرِي); ÂMDAN SONRA HÂS — bütün namazlardan sonra orta namazı an; rütbesi belirir (2:238); nükte için TEKRÎR — 102:3-4'ün katlanan inzârı. Tevşî', sözü iki atıflı ismin açtığı bir tesniye ile mühürler."},
 "explanation": {
  "en": "The surplus word must EARN its place; the source names the earnings. (1) IDAH AFTER IBHAM: the meaning is shown in two forms, veiled then clear — so it lands twice and settles; or the hearer's craving to know, once roused, makes the knowing sweeter. رَبِّ اشْرَحْ لِي صَدْرِي (20:25): the request is veiled up to لِي, and صَدْرِي is its tafsir. On the reading that makes the makhsus the khabar of an omitted mubtada, the نِعْمَ bab joins this kind — نِعْمَ زَيْدٌ would have sufficed, and the fuller form shows the speech in its middle way and gathers the two opposites in mind. TAWSHI' is a named kind: أَنْ يُؤْتَى فِي عَجُزِ الْكَلَامِ بِمُثَنًّى مُفَسَّرٍ بِاسْمَيْنِ ثَانِيهِمَا مَعْطُوفٌ عَلَى الْأَوَّلِ — a dual at the speech's seat, unfolded by two nouns, the second joined to the first: يَشِيبُ ابْنُ آدَمَ وَيَشِبُّ فِيهِ خَصْلَتَانِ: الْحِرْصُ وَطُولُ الْأَمَلِ. (2) THE KHASS AFTER THE 'AMM, alerting to its excellence — as if the difference in attribute were a difference in essence, so the khass seems of another kind: حَافِظُوا عَلَى الصَّلَوَاتِ وَالصَّلَاةِ الْوُسْطَى (2:238; fajr said some, 'asr said others). (3) TAKRIR for a point, like doubling the warning: كَلَّا سَوْفَ تَعْلَمُونَ ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ (102:3-4) — and ثُمَّ grades the second warning above the first. The next slice adds IGHAL: sealing the bayt with a point the meaning could stand without.",
  "tr": "Fazla söz yerini HAK etmelidir; kaynak hak edişleri adlandırır. (1) İBHÂMDAN SONRA ÎZÂH: mânâ biri örtülü biri açık iki sûrette gösterilir — iki kez konar, yerleşir; yahut bilme iştiyakı uyandırılınca bilmenin lezzeti tamamlanır. رَبِّ اشْرَحْ لِي صَدْرِي (20:25): istek لِي'ye kadar örtülüdür, صَدْرِي tefsiridir. Mahsûsu mahzuf mübtedânın haberi sayan okuyuşta نِعْمَ bâbı da bu türe girer — نِعْمَ زَيْدٌ yeterdi; dolu sûret sözü orta yolda gösterir ve iki zıddı bir arada hatıra getirir. TEVŞÎ' adlı bir türdür: أَنْ يُؤْتَى فِي عَجُزِ الْكَلَامِ بِمُثَنًّى مُفَسَّرٍ بِاسْمَيْنِ ثَانِيهِمَا مَعْطُوفٌ عَلَى الْأَوَّلِ — sözün oturağında bir tesniye, ikincisi birincisine atfedilmiş iki isimle açılır: يَشِيبُ ابْنُ آدَمَ وَيَشِبُّ فِيهِ خَصْلَتَانِ: الْحِرْصُ وَطُولُ الْأَمَلِ. (2) ÂMDAN SONRA HÂSSIN ZİKRİ, faziletine tenbih için — vasıftaki fark zâttaki fark menziline indirilir; hâs sanki başka cinstendir: حَافِظُوا عَلَى الصَّلَوَاتِ وَالصَّلَاةِ الْوُسْطَى (2:238; kimi sabah dedi, kimi ikindi). (3) Nükte için TEKRÎR, inzârı katlamak gibi: كَلَّا سَوْفَ تَعْلَمُونَ ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ (102:3-4) — ve ثُمَّ ikinci inzârı birincinin üstüne derecelendirir. Gelecek dilim ÎGĀLİ ekler: beyti, mânânın onsuz da tamam olacağı bir nükteyle mühürlemek."},
 "examples": [
  {"ar": "رَبِّ اشْرَحْ لِي صَدْرِي",
   "en": "idah after ibham: the veiled request, then its tafsir (20:25).",
   "tr": "ibhâmdan sonra îzâh: örtülü istek, sonra tefsiri (20:25).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "يَشِيبُ ابْنُ آدَمَ وَيَشِبُّ فِيهِ خَصْلَتَانِ: الْحِرْصُ وَطُولُ الْأَمَلِ",
   "en": "tawshi': the sealing dual unfolded by two joined nouns.",
   "tr": "tevşî': mühür tesniyesi, atıflı iki isimle açılır.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "حَافِظُوا عَلَى الصَّلَوَاتِ وَالصَّلَاةِ الْوُسْطَى",
   "en": "the khass after the 'amm (2:238).",
   "tr": "âmdan sonra hâs (2:238).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ",
   "en": "takrir for the doubled warning — and ثُمَّ grades it (102:3-4).",
   "tr": "katlanan inzâr için tekrîr — ثُمَّ onu dereceler (102:3-4).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«Tekrar her zaman dolgudur»",
   "right": "«Nükte taşıyan tekrar ITNÂBDIR; nüktesiz fazlalık tatvîl yahut haşivdir»",
   "why": {"en": "The previous chapter drew the boundary: surplus WITHOUT benefit is rejected. This chapter fills the other side: the same three words repeated in 102:3-4 are eloquence, because the repetition itself — graded by ثُمَّ — is the meaning.",
           "tr": "Önceki bâb sınırı çizdi: faydasız fazlalık merduttur. Bu bâb öbür tarafı doldurur: 102:3-4'te aynı üç kelimenin tekrarı belâgattir; çünkü tekrarın kendisi — ثُمَّ ile derecelenmiş — mânânın tâ kendisidir."}}],
 "relatedNotes": ["ijaz-itnab-musawat", "ijaz-al-hadhf", "badal", "atf-nasaq",
                  "al-muthanna", "vocative-munada", "tibaq"]}

(GR / "asbab-al-itnab.json").write_text(
    json.dumps(NOTE144, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch40:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + sharaha/shaba/shabba (+hafaza copied); note 144")
