# -*- coding: utf-8 -*-
"""Author chapter 18 of talkhis-al-miftah — تَنْكِيرُ الْمُسْنَدِ وَتَعْرِيفُهُ: وُجُوهُ الْبَلَاغَةِ.

The musnad's last states — indefinite, made specific, definite — and this
chapter is authored with the BELAGAT VECİHLERİ made explicit: every
sentence carries multiple jumal rows, each naming ONE rhetorical vech with
the madrasah's own formula and a full explanation. The frames of this
section exist for nothing else: nobody says زَيْدٌ كَاتِبٌ to inform; the
matn says it to show what the TANWIN is doing.

The vecih roll this chapter teaches:
  • عَدَمُ الْحَصْرِ وَالْعَهْدِ — the musnad nakira because neither confinement
    nor a known referent is meant (زَيْدٌ كَاتِبٌ وَعَمْرٌو شَاعِرٌ).
  • التَّفْخِيم — tankir to MAGNIFY (هُدًى لِلْمُتَّقِينَ: guidance past
    describing).
  • التَّحْقِير — tankir to BELITTLE (مَا زَيْدٌ شَيْئًا: not even a «thing»).
  • التَّخْصِيصُ بِالْوَصْفِ — the sifa multiplies the yield (زَيْدٌ رَجُلٌ
    عَالِمٌ), twin of the idafa takhsis (زَيْدٌ غُلَامُ رَجُلٍ).
  • قَصْرُ الْجِنْسِ — the jins-lam musnad confines: حَقِيقَةً (زَيْدٌ
    الْأَمِيرُ when none but Zayd commands) or مُبَالَغَةً (عَمْرٌو الشُّجَاعُ:
    others' courage counts for nothing beside his) — with al-Razi's khilaf
    on الْمُنْطَلِقُ زَيْدٌ taught as a khilaf.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1510-1545 (sahifa
53-54): the matn's frames زَيْدٌ كَاتِبٌ وَعَمْرٌو شَاعِرٌ, مَا زَيْدٌ شَيْئًا,
زَيْدٌ رَجُلٌ عَالِمٌ (with its idafa twin زَيْدٌ غُلَامُ رَجُلٍ), عَمْرٌو الشُّجَاعُ
and الْمُنْطَلِقُ زَيْدٌ, and al-Baqara 2:2 (هُدًى لِلْمُتَّقِينَ). The aya is
received text quoted exactly.

Grammar this chapter is chosen to teach:
  • note 120 `wujuh-al-musnad` — the vecih catalogue of the musnad's
    tankir/tarif with every formula named.
  • the engine work the probe forced: the propn guard on the learned scale
    (زَيْدٌ was offered «فَعْل — a heard masdar»), the فُعَال/فَعَال shapes
    joining the IsmTagger (شُجَاع wore an invented shadda), and the noun
    lexicon as the root finder's LAST resort (لِلْمُتَّقِينَ walked out
    rootless).
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

TITLE18 = {"ar": "تَنْكِيرُ الْمُسْنَدِ وَتَعْرِيفُهُ — وُجُوهُ الْبَلَاغَةِ",
           "en": "The Musnad Indefinite and Definite — the Faces of Balagha",
           "tr": "Müsnedin Nekre ve Marife Oluşu — Belâgat Vecihleri"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "Zayd is a writer, and ʿAmr is a poet. (Both musnads indefinite: neither confinement nor a known referent is meant — the plainest setting of the dial.)",
 "tr": "Zeyd bir kâtiptir, Amr bir şairdir. (İki müsned de nekre: ne hasr ne ahd kastedilmiştir — ayarın en yalın konumu.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar","tankir-al-musnad-ilayh"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "The mubtada — definite by being a name; the interest of this frame is entirely in what follows.",
      "Mübtedâ — ad olmakla marife; bu kalıbın bütün ilgisi ardından gelendedir."),
  tok("كَاتِبٌ","katib","noun",["mubtada-khabar","ism-fail","wujuh-al-musnad"],
      "خَبَرٌ مَرْفُوعٌ — نُكِّرَ لِعَدَمِ إِرَادَةِ الْحَصْرِ وَالْعَهْدِ.",
      "«a writer» — the khabar, and its TANWIN is the teaching: indefinite because neither of the two things a definite musnad would claim is meant. No ḤAṢR — writing is not confined to Zayd, others write too; and no ʿAHD — no particular known writer («THE writer you know of») is intended. The nakira is the honest default: it ascribes the craft and claims nothing more.",
      "«bir kâtip» — haber; ve TENVİNİ dersin kendisidir: nekredir, çünkü marife bir müsnedin iddia edeceği iki şeyden hiçbiri kastedilmemiştir. HASR yok — kâtiplik Zeyd'e hasredilmiş değildir, başkaları da yazar; AHD de yok — bilinen belli bir kâtip («hani o kâtip») kastedilmemiştir. Nekre dürüst varsayılandır: zanaatı isnâd eder, fazlasını iddia etmez."),
  tok("وَعَمْرٌو","amr-alam","propn",["mubtada-khabar","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«عَمْرٌو» مُبْتَدَأٌ ثَانٍ.",
      "«and ʿAmr» — the second mubtada, silent waw and all.",
      "«ve Amr» — ikinci mübtedâ; sessiz vâvıyla birlikte.",
      segments=[seg("وَ","wa","part"), seg("عَمْرٌو","amr-alam","propn")]),
  tok("شَاعِرٌ","shair","noun",["mubtada-khabar","ism-fail","wujuh-al-musnad"],
      "خَبَرٌ مَرْفُوعٌ — نُكِّرَ كَذَلِكَ.",
      "«a poet» — the twin khabar, indefinite for the same two absences. The matn pairs the frames so the eye sees the SETTING, not the sentence: this is what a musnad looks like when the speaker wants nothing but the ascription.",
      "«bir şair» — ikiz haber; aynı iki yokluk için nekre. Metin kalıpları çiftler ki göz cümleyi değil AYARI görsün: konuşan isnâddan başka bir şey istemediğinde müsned böyle görünür.",
      punct=".")],
 "jumal": [
  J("زَيْدٌ كَاتِبٌ وَعَمْرٌو شَاعِرٌ",
    "الْوَجْهُ الْأَوَّلُ: تَنْكِيرُ الْمُسْنَدِ لِعَدَمِ إِرَادَةِ الْحَصْرِ.",
    "VECH 1 — no ḥaṣr: being-a-writer is NOT confined to Zayd. Had the speaker meant «Zayd and none other writes», the musnad would have worn the article (زَيْدٌ الْكَاتِبُ). The tanwin explicitly declines that claim.",
    "1. VECİH — hasr yok: kâtiplik Zeyd'e HASREDİLMİŞ değildir. Konuşan «Zeyd'den başkası yazmaz» demek isteseydi müsned harf-i tarif giyerdi (زَيْدٌ الْكَاتِبُ). Tenvin bu iddiayı açıkça reddeder."),
  J("زَيْدٌ كَاتِبٌ وَعَمْرٌو شَاعِرٌ",
    "الْوَجْهُ الثَّانِي: تَنْكِيرُهُ لِعَدَمِ الْعَهْدِ.",
    "VECH 2 — no ʿahd: nor is a KNOWN writer meant — «that writer we spoke of is Zayd» would again demand the article, this time the lam of ʿahd. Two absences, one tanwin: the indefinite musnad is defined by what it refuses to claim.",
    "2. VECİH — ahd yok: BİLİNEN bir kâtip de kastedilmemiştir — «sözünü ettiğimiz o kâtip Zeyd'dir» yine harf-i tarif isterdi; bu kez ahd lâmını. İki yokluk, tek tenvin: nekre müsned, iddia etmeyi reddettikleriyle tanımlanır.")]})

# ---------------------------------------------------------------- s2 — Baqara 2
S.append({"id": "s2", "translation": {
 "en": "…a guidance for the God-fearing. (al-Baqara 2:2 — the musnad indefinite for TAFKHIM: a guidance so great that no description would reach its limit.)",
 "tr": "…müttakîler için bir hidayettir. (Bakara 2:2 — müsned TAFHÎM için nekre: hiçbir tavsifin sınırına eremeyeceği kadar büyük bir hidayet.)"},
 "tokens": [
  tok("هُدًى","huda","noun",["mubtada-khabar","ism-maqsur-manqus","wujuh-al-musnad","hadhf-wa-taqdir"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — نُكِّرَ لِلتَّفْخِيمِ — وَفِي مُبْتَدَئِهِ تَقْدِيرَانِ: «هُوَ هُدًى» أَوْ «ذَلِكَ الْكِتَابُ» مُبْتَدَأٌ وَ«هُدًى» خَبَرُهُ.",
      "«a GUIDANCE» — a maqsur, its damma estimated on the alif; and the tanwin here is not the plain default of s1 but TAFKHIM, magnification: guidance whose ultimate reach cannot be grasped nor its description completed — as if to say «a guidance beyond telling what guidance». And the mubtada is a two-taqdir case, as chapter 15 taught to expect: read هُوَ هُدًى with the mubtada omitted, or read ذَلِكَ الْكِتَابُ as the mubtada and هُدًى its khabar — the books keep both.",
      "«bir HİDAYET» — maksûr; dammesi elif üzerinde takdîr edilir. Ve buradaki tenvin, s1'in yalın varsayılanı değil, TAFHÎMdir — büyütme: nihayetine vâkıf olunamayacak, hakkıyla tavsif edilemeyecek bir hidayet — sanki «ne hidayet olduğu anlatılamaz bir hidayet» der. Mübtedâsı da, 15. bâbın beklemeyi öğrettiği gibi iki takdirlidir: هُوَ هُدًى diye mübtedâ hazfiyle oku, yahut ذَلِكَ الْكِتَابُ mübtedâ ve هُدًى haberi olsun — kitaplar ikisini de saklar."),
  tok("لِلْمُتَّقِينَ","muttaqi","noun",["huruf-jarr","jam-mudhakkar-salim","form-viii-verbs"],
      "جَارٌّ وَمَجْرُورٌ — اللَّامُ لِلِاخْتِصَاصِ وَ«الْمُتَّقِينَ» جَمْعُ مُذَكَّرٍ سَالِمٌ مَجْرُورٌ بِالْيَاءِ.",
      "«for the God-fearing» — لِ + الْمُتَّقِينَ with the article's alif swallowed in writing; a sound masculine plural in jarr by its YA. The ism fail of اِتَّقَى (Form VIII of و ق ي, its waw assimilated into the ta): those who shield themselves. The guidance is magnified, and then aimed.",
      "«müttakîler için» — لِ + الْمُتَّقِينَ; harf-i tarifin elifi yazıda yutulmuş. Cem'-i müzekker-i sâlim; YÂ ile mecrûr. اِتَّقَى'nın ism-i fâili (و ق ي'nin VIII. bâbı; vâvı tâya idgam edilmiş): kendilerini koruyanlar. Hidayet önce büyütülür, sonra nişanlanır.",
      segments=[seg("لِ","li","prep"), seg("الْمُتَّقِينَ","muttaqi","noun")],
      punct=".")],
 "jumal": [
  J("هُدًى لِلْمُتَّقِينَ",
    "الْوَجْهُ الثَّالِثُ: تَنْكِيرُ الْمُسْنَدِ لِلتَّفْخِيمِ — هُدًى لَا يُكْتَنَهُ كُنْهُهُ.",
    "VECH 3 — TAFKHIM: the same tanwin that declined every claim in s1 here makes the largest claim of all. Indefiniteness can say «one among many» or «one beyond counting» — context decides, and here the Book's own majesty decides it upward: a guidance whose essence cannot be fathomed.",
    "3. VECİH — TAFHÎM: s1'de her iddiayı reddeden aynı tenvin, burada iddiaların en büyüğünü yapar. Nekrelik «birçoklarından biri» de diyebilir, «sayıya sığmaz bir» de — bağlam belirler; burada Kitâb'ın kendi azameti yukarı doğru belirler: künhüne varılamaz bir hidayet."),
  J("هُدًى لِلْمُتَّقِينَ",
    "وَفِي الْمُبْتَدَإِ تَقْدِيرَانِ مَحْفُوظَانِ — هُوَ هُدًى، أَوْ ذَلِكَ الْكِتَابُ هُدًى.",
    "And the omitted-mubtada fork is kept open, exactly as فَصَبْرٌ جَمِيلٌ taught: «it is a guidance», or «THAT Book — is a guidance». Two reconstructions, both classical, neither flattened.",
    "Ve hazfedilmiş mübtedâ çatalı açık tutulur; tıpkı فَصَبْرٌ جَمِيلٌ'in öğrettiği gibi: «o bir hidayettir», yahut «İŞTE O KİTAP — bir hidayettir». İki kuruluş, ikisi de klasik; hiçbiri teke indirilmemiş.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "Zayd is not a thing. (The matn's frame for TAHQIR: the musnad indefinite to belittle — not even worth calling a «thing».)",
 "tr": "Zeyd bir şey değildir. (Metnin TAHKÎR kalıbı: müsned küçültmek için nekre — «şey» demeye bile değmez.)"},
 "tokens": [
  tok("مَا","ma-hijaziyya","part",["anwa-ma","wujuh-al-musnad"],
      "«مَا» الْحِجَازِيَّةُ — تَعْمَلُ عَمَلَ لَيْسَ: تَرْفَعُ الِاسْمَ وَتَنْصِبُ الْخَبَرَ.",
      "The HIJAZI ma — the negation that governs like لَيْسَ: raf' on its ism, nasb on its khabar. The mansub شَيْئًا three words on is its signature; the Tamimi reading would leave the khabar marfu'.",
      "HİCÂZÎ mâ — لَيْسَ gibi amel eden nefiy: ismini ref, haberini nasb eder. Üç kelime ötedeki mansûb شَيْئًا onun imzasıdır; Temîmî okuyuş haberi merfû bırakırdı."),
  tok("زَيْدٌ","zayd","propn",["anwa-ma"],
      "اسْمُ «مَا» مَرْفُوعٌ.",
      "Ma's ism, in raf'.",
      "Mânın ismi; merfû."),
  tok("شَيْئًا","shay","noun",["anwa-ma","wujuh-al-musnad"],
      "خَبَرُ «مَا» مَنْصُوبٌ — نُكِّرَ لِلتَّحْقِيرِ.",
      "«a THING» — ma's khabar in nasb, and the tanwin's third face: TAHQIR. شَيْء is the widest word in the language — everything that is, is a thing — so to deny even THAT, indefinite and minimal, is to deny Zayd the least rank there is. The same three letters that magnified هُدًى here grind to dust.",
      "«bir ŞEY» — mânın mansûb haberi; ve tenvinin üçüncü yüzü: TAHKÎR. شَيْء dilin en geniş kelimesidir — var olan her şey bir şeydir — öyleyse EN AZI bile, nekre ve asgarî hâliyle nefyetmek, Zeyd'e mertebelerin en küçüğünü bile tanımamaktır. هُدًى'yı büyüten aynı üç harf, burada toz eder.",
      punct=".")],
 "jumal": [
  J("مَا زَيْدٌ شَيْئًا",
    "الْوَجْهُ الرَّابِعُ: تَنْكِيرُ الْمُسْنَدِ لِلتَّحْقِيرِ.",
    "VECH 4 — TAHQIR: the indefinite at its floor. One tanwin, three offices now — the plain default (s1), magnification (s2), and here contempt. The vech is never in the letters; it is in what the maqam does with them.",
    "4. VECİH — TAHKÎR: nekrenin tabanı. Tek tenvin, artık üç vazife — yalın varsayılan (s1), büyütme (s2) ve burada hor görme. Vecih hiçbir zaman harflerde değildir; makāmın onlarla yaptığındadır."),
  J("مَا زَيْدٌ شَيْئًا",
    "وَالنَّصْبُ عَلَامَةُ الْحِجَازِيَّةِ — وَبِهَا نَزَلَ التَّنْزِيلُ: مَا هَذَا بَشَرًا.",
    "And the nasb on the khabar is the Hijazi ma's own signature — the dialect the Revelation came down in (مَا هَذَا بَشَرًا). One accusative fatha carries a whole dialectology.",
    "Haberdeki nasb, Hicâzî mânın kendi imzasıdır — Tenzîl'in indiği lehçe (مَا هَذَا بَشَرًا). Tek bir nasb fethası, koca bir lehçe bilgisini taşır.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "Zayd is a learned man. (TAKHSIS by the sifa: «man» alone says little; «learned» multiplies the yield — the twin of the idafa's takhsis, زَيْدٌ غُلَامُ رَجُلٍ.)",
 "tr": "Zeyd âlim bir adamdır. (Sıfatla TAHSÎS: yalnız «adam» az söyler; «âlim» faydayı çoğaltır — izâfet tahsîsinin ikizi: زَيْدٌ غُلَامُ رَجُلٍ.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "The mubtada again — the constant of every frame in this chapter, so that only the musnad's dress changes.",
      "Yine mübtedâ — bu bâbın her kalıbının sabiti; değişen yalnız müsnedin kıyafeti olsun diye."),
  tok("رَجُلٌ","rajul","noun",["mubtada-khabar","wujuh-al-musnad"],
      "خَبَرٌ مَرْفُوعٌ — وَحْدَهُ قَلِيلُ الْفَائِدَةِ.",
      "«a man» — the khabar, and by itself nearly empty: that Zayd is a man is hardly news. The frame sets it up to be completed.",
      "«bir adam» — haber; ve tek başına nerdeyse boş: Zeyd'in adam olduğu pek haber değildir. Kalıp onu tamamlanmak üzere kurar."),
  tok("عَالِمٌ","alim","noun",["naat-sifa","ism-fail","wujuh-al-musnad"],
      "صِفَةٌ لِ«رَجُلٌ» مَرْفُوعَةٌ — وَبِهَا تَخَصَّصَ الْمُسْنَدُ وَتَمَّتِ الْفَائِدَةُ.",
      "«LEARNED» — the sifa on the khabar, and the yield arrives with it: not merely a man but a man of knowledge. This is تَخْصِيصُ الْمُسْنَدِ بِالْوَصْفِ, and the matn pairs it with its idafa twin — زَيْدٌ غُلَامُ رَجُلٍ, «Zayd is a man's servant» — where the mudaf-ilayh does the same narrowing work the sifa does here. And the TARK of both has its reasons: no opportunity, no knowledge, or no wish to tell — the same three that excused the maf'ul qayds in chapter 16.",
      "«ÂLİM» — haberin sıfatı; fayda onunla gelir: yalnız bir adam değil, ilim sahibi bir adam. Bu, تَخْصِيصُ الْمُسْنَدِ بِالْوَصْفِ'tir; ve metin onu izâfet ikiziyle çiftler — زَيْدٌ غُلَامُ رَجُلٍ, «Zeyd bir adamın hizmetkârıdır» — orada muzâfun ileyh, burada sıfatın yaptığı daraltmayı yapar. Ve ikisinin de TERKİ sebepsiz değildir: fırsat yok, bilgi yok, yahut söyleme isteği yok — 16. bâbda mef'ûl kayıtlarını mâzur gösteren aynı üçlü.",
      punct=".")],
 "jumal": [
  J("زَيْدٌ رَجُلٌ عَالِمٌ",
    "الْوَجْهُ الْخَامِسُ: تَخْصِيصُ الْمُسْنَدِ بِالْوَصْفِ — لِكَوْنِ الْفَائِدَةِ أَتَمَّ.",
    "VECH 5 — TAKHSIS by the sifa: the description narrows the musnad and the news multiplies, exactly as the maf'ul family multiplied the verb's news in chapter 16 — one doctrine, nominal edition.",
    "5. VECİH — sıfatla TAHSÎS: vasıf müsnedi daraltır ve haber çoğalır; tıpkı 16. bâbda mef'ûl ailesinin fiilin haberini çoğalttığı gibi — tek kāide, isim tarafı."),
  J("زَيْدٌ رَجُلٌ عَالِمٌ",
    "وَتَوْأَمُهُ التَّخْصِيصُ بِالْإِضَافَةِ: زَيْدٌ غُلَامُ رَجُلٍ.",
    "And its twin, takhsis by IDAFA — زَيْدٌ غُلَامُ رَجُلٍ: the annexation narrows «servant» to «a man's servant» just as the sifa narrowed «man» to «learned man». Two grammatical routes, one rhetorical office.",
    "Ve ikizi, İZÂFETLE tahsîs — زَيْدٌ غُلَامُ رَجُلٍ: izâfet «hizmetkâr»ı «bir adamın hizmetkârı»na daraltır; sıfatın «adam»ı «âlim adam»a daralttığı gibi. İki gramer yolu, tek belâgat vazifesi.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "ʿAmr is THE brave one. (The jins-lam musnad confines the genus: courage, beside ʿAmr's, counts for nothing — qasr by EXAGGERATION; and when the fact matches, the qasr is literal: زَيْدٌ الْأَمِيرُ.)",
 "tr": "Amr, cesûrun ta kendisidir. (Cins lâmlı müsned cinsi hasreder: Amr'ınkinin yanında cesaret sayılmaz — MÜBÂLAĞA yoluyla kasr; vâkıa uyarsa kasr hakikî olur: زَيْدٌ الْأَمِيرُ.)"},
 "tokens": [
  tok("عَمْرٌو","amr-alam","propn",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "ʿAmr as mubtada, his silent waw guarding the spelling.",
      "Mübtedâ olarak Amr; sessiz vâvı imlâyı korur."),
  tok("الشُّجَاعُ","shujaa","noun",["mubtada-khabar","anwa-al-lam-al-tarif","wujuh-al-musnad","qasr"],
      "خَبَرٌ مَرْفُوعٌ مُعَرَّفٌ بِلَامِ الْجِنْسِ — لِقَصْرِ الْجِنْسِ عَلَى الْمُبْتَدَإِ مُبَالَغَةً.",
      "«THE brave one» — the khabar wearing the lam of GENUS, and the definite musnad's great office: QASR. Literally it says «the genus of courage IS ʿAmr» — and since other brave men exist, the confinement is مُبَالَغَةً, by exaggeration: beside his courage, theirs is as if it were not. Where the fact matches the claim — زَيْدٌ الْأَمِيرُ said when none but Zayd commands — the same lam makes a qasr حَقِيقَةً, literal. One article, two strengths, and the world decides which. (On فُعَال, no shadda: the intensive lives in the LAM here, not the pattern.)",
      "«cesûrun ta kendisi» — CİNS lâmını giymiş haber; ve marife müsnedin büyük vazifesi: KASR. Harfiyen «cesaret cinsi Amr'DIR» der — başka cesurlar da var olduğuna göre hasr مُبَالَغَةً'dir, abartıyladır: onun cesareti yanında ötekilerinki yok hükmündedir. İddia vâkıayla örtüşünce — Zeyd'den başka emîr yokken söylenen زَيْدٌ الْأَمِيرُ — aynı lâm kasrı حَقِيقَةً, hakikî yapar. Tek harf-i tarif, iki kuvvet; hangisi olduğuna dünya karar verir. (Vezin فُعَال'dir, şeddesiz: buradaki mübâlağa kalıpta değil, LÂMdadır.)",
      punct=".")],
 "jumal": [
  J("عَمْرٌو الشُّجَاعُ",
    "الْوَجْهُ السَّادِسُ: تَعْرِيفُ الْمُسْنَدِ بِلَامِ الْجِنْسِ لِقَصْرِ الْجِنْسِ مُبَالَغَةً — وَحَقِيقَةً فِي زَيْدٌ الْأَمِيرُ.",
    "VECH 6 — the jins-lam qasr, in both strengths: mubalaghatan here (others' courage discounted, not denied), haqiqatan in زَيْدٌ الْأَمِيرُ when no other amir exists. The claim's letter is identical; its warrant differs — teach the pair together or the learner will read every such lam as literal.",
    "6. VECİH — cins lâmı kasrı, iki kuvvetiyle: burada mübâlağaten (başkalarının cesareti inkâr değil, iskonto edilir), زَيْدٌ الْأَمِيرُ'de hakikaten — başka emîr yokken. İddianın harfi aynıdır; senedi farklıdır — çifti birlikte öğret, yoksa öğrenci her böyle lâmı hakikî okur."),
  J("عَمْرٌو الشُّجَاعُ",
    "وَخِلَافُ الرَّازِيِّ فِي «الْمُنْطَلِقُ زَيْدٌ»: قِيلَ الِاسْمُ مُبْتَدَأٌ أَبَدًا لِدَلَالَتِهِ عَلَى الذَّاتِ — وَرُدَّ بِأَنَّ الْمُتَقَدِّمَ هُوَ الْمُبْتَدَأُ.",
    "And al-Razi's khilaf rides this frame: he argued the NAME is always the mubtada (it points at the essence) and the sifa always the khabar, even in الْمُنْطَلِقُ زَيْدٌ. The refutation: that sentence means «the one leaving is THE BEARER OF THIS NAME» — so what comes first is the mubtada, and order wins. A khilaf taught as a khilaf, with the winning argument stated.",
    "Ve Râzî'nin hilâfı bu kalıba biner: İSİM (zâta delâlet ettiği için) her zaman mübtedâ, sıfat her zaman haberdir dedi — الْمُنْطَلِقُ زَيْدٌ'de bile. Reddi: o cümle «giden, BU ADIN SAHİBİdir» demektir — öyleyse önce gelen mübtedâdır ve sıra kazanır. Hilâf, hilâf olarak; kazanan delil söylenerek öğretilmiş.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # NEW this chapter
 "katib":    g("كَاتِب", "ك ت ب", "noun", "writer, scribe (ism fail)", "kâtip, yazıcı (ism-i fâil)", 2),
 "shair":    g("شَاعِر", "ش ع ر", "noun", "poet (ism fail)", "şair (ism-i fâil)", 2),
 "huda":     g("هُدًى", "ه د ي", "noun", "guidance", "hidayet", 2),
 "muttaqi":  g("مُتَّقٍ", "و ق ي", "noun", "God-fearing (ism fail of اِتَّقَى)", "müttakî (اِتَّقَى'nın ism-i fâili)", 3, plural="مُتَّقِينَ", form="VIII"),
 "shay":     g("شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "rajul":    g("رَجُل", "ر ج ل", "noun", "man", "adam, er kişi", 1, plural="رِجَال"),
 "alim":     g("عَالِم", "ع ل م", "noun", "learned, a scholar (ism fail)", "âlim (ism-i fâil)", 2, plural="عُلَمَاء"),
 "shujaa":   g("شُجَاع", "ش ج ع", "noun", "brave, courageous (on فُعَال)", "cesur, şecaatli (فُعَال vezninde)", 3),
 "ghulam":   g("غُلَام", "غ ل م", "noun", "boy, servant", "oğlan, hizmetkâr", 3, plural="غِلْمَان"),
 "ma-hijaziyya": g("مَا (الْحِجَازِيَّة)", None, "part", "the Hijazi negation — governs like laysa", "Hicâzî mâ — leyse gibi amel eder", 4),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/18.json").write_text(
    json.dumps({"chapter": 18, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 18 for c in man["chapters"]):
    man["chapters"].append({"n": 18, "title": TITLE18})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.18.0"
ADD_EN = (" Chapter 18 continues from the same file (lines ~1510-1545, sahifa 53-54): the matn's frames "
          "زَيْدٌ كَاتِبٌ وَعَمْرٌو شَاعِرٌ, مَا زَيْدٌ شَيْئًا, زَيْدٌ رَجُلٌ عَالِمٌ with its idafa twin زَيْدٌ غُلَامُ رَجُلٍ, "
          "عَمْرٌو الشُّجَاعُ (with زَيْدٌ الْأَمِيرُ and al-Razi's khilaf on الْمُنْطَلِقُ زَيْدٌ carried in the jumal "
          "rows and the note), and al-Baqara 2:2. The aya is received text quoted exactly.")
ADD_TR = (" On sekizinci bâb aynı dosyadan (satır ~1510-1545, sahife 53-54) devam eder: metnin kalıpları "
          "زَيْدٌ كَاتِبٌ وَعَمْرٌو شَاعِرٌ, مَا زَيْدٌ شَيْئًا, زَيْدٌ رَجُلٌ عَالِمٌ ile izâfet ikizi زَيْدٌ غُلَامُ رَجُلٍ, "
          "عَمْرٌو الشُّجَاعُ (زَيْدٌ الْأَمِيرُ ve Râzî'nin الْمُنْطَلِقُ زَيْدٌ hilâfı cümle satırlarında ve notta "
          "taşınır) ve Bakara 2:2. Âyet aynen alınmış mervî metindir.")
if "1510-1545" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch18:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
