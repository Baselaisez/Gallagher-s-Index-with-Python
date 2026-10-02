# -*- coding: utf-8 -*-
"""Author chapter 21 of talkhis-al-miftah — الْقَصْرُ: حَدُّهُ وَأَقْسَامُهُ.

The qasr bab opens. Chapter 21 carries the definition and the whole
taxonomy, on the frame the QasrEngine reads exactly — نَفْيٌ + إِلَّا:

  • the hadd: تَخْصِيصُ شَيْءٍ بِشَيْءٍ بِطَرِيقٍ مَخْصُوصٍ.
  • by essence: حَقِيقِيّ / غَيْرُ حَقِيقِيٍّ (إِضَافِيّ).
  • by ends: قَصْرُ الصِّفَةِ عَلَى الْمَوْصُوفِ (plentiful — لَا إِلَهَ إِلَّا
    اللهُ its throne text, مَا فِي الدَّارِ إِلَّا زَيْدٌ its everyday one) and
    قَصْرُ الْمَوْصُوفِ عَلَى الصِّفَةِ (haqiqatan almost nonexistent — no one
    encircles all attributes — so idafi or by exaggeration).
  • the idafi kinds BY ADDRESSEE: إِفْرَاد (against the partnership
    believer), قَلْب (against the opposite believer), تَعْيِين (against the
    undecided) — one sentence, three readings, and only the hearer's
    state picks; the sifa here is the balagha's (a meaning standing in
    another), not the nahw's adjective.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1790-1840 (sahifa
61-63): the matn's frames مَا زَيْدٌ إِلَّا كَاتِبٌ, مَا كَاتِبٌ إِلَّا زَيْدٌ,
مَا شَاعِرٌ إِلَّا زَيْدٌ, مَا فِي الدَّارِ إِلَّا زَيْدٌ, and the kalima of
tawhid لَا إِلَهَ إِلَّا اللهُ which the source itself cites for the haqiqi
qasr of the ilah-attribute to Allah.

Grammar this chapter is chosen to teach:
  • note 123 `aqsam-al-qasr` — the taxonomy with the addressee kinds.
  • QasrEngine (new): the nafy+istithna frame read exactly — maqsur ←
    maqsur alayh — with the ends settled by the lexicon where a propn
    stands, and the addressee kinds kept a shortlist.
  • MaEngine rule 6h: an إِلَّا later in the line promotes the negation —
    the interrogative was selling «what is in the house?» over the frame.
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
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
S = []

TITLE21 = {"ar": "الْقَصْرُ — حَدُّهُ وَأَقْسَامُهُ",
           "en": "Qasr — its Definition and Kinds",
           "tr": "Kasr — Tarifi ve Kısımları"}

# ---------------------------------------------------------------- s1 — the kalima
S.append({"id": "s1", "translation": {
 "en": "There is no god but Allah. (The frame's throne text: the attribute of ilah-hood confined, haqiqatan, to Allah — negation + exception, the first tariq of qasr.)",
 "tr": "Allah'tan başka ilah yoktur. (Çatının taht metni: ilahlık vasfı, hakikaten, Allah'a hasredilmiş — nefiy + istisnâ, kasrın ilk yolu.)"},
 "tokens": [
  tok("لَا","la-nafiya-lil-jins","part",["aqsam-al-qasr"],
      "نَافِيَةٌ لِلْجِنْسِ.",
      "«no … at all» — the genus-la, denying every instance of what follows: the negation half of the qasr frame.",
      "«hiçbir … yok» — cins lâ'sı; ardından gelenin her ferdini nefyeder: kasr çatısının nefiy yarısı."),
  tok("إِلَهَ","ilah","noun",["aqsam-al-qasr"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ — وَهُوَ الْمَقْصُورُ: وَصْفُ الْأُلُوهِيَّةِ.",
      "«god» — the la's ism on the fath, and the MAQSUR: what is being confined is the ATTRIBUTE of ilah-hood itself. The khabar (مَوْجُودٌ, «exists») is omitted, as this frame always omits it.",
      "«ilah» — lâ'nın fetha üzre ismi ve MAKSÛR: hasredilen, İLAHLIK vasfının kendisidir. Haber (مَوْجُودٌ, «vardır») hazfedilmiştir; bu çatı onu hep hazfeder."),
  tok("إِلَّا","illa","part",["aqsam-al-qasr","qasr"],
      "أَدَاةُ اسْتِثْنَاءٍ — وَهِيَ مَعَ النَّفْيِ طَرِيقُ الْقَصْرِ الْأَوَّلُ.",
      "«but, except» — the exception particle; with the negation before it, the FIRST TARIQ of qasr. Everything between the la and the illa is confined to what follows the illa.",
      "«başka, ancak» — istisnâ edatı; önündeki nefiyle birlikte kasrın İLK YOLU. Lâ ile illâ arasındaki her şey, illâdan sonrakine hasredilir."),
  tok("اللهُ","allah","propn",["aqsam-al-qasr"],
      "لَفْظُ الْجَلَالَةِ بَدَلٌ مِنْ مَحَلِّ اسْمِ «لَا» مَرْفُوعٌ — وَهُوَ الْمَقْصُورُ عَلَيْهِ.",
      "«Allah» — in raf', a badal from the la's ism read in its POSITION (the position of a mubtada), and the MAQSUR ALAYH: the one bearer the attribute is confined to. This qasr is ḤAQĪQĪ — true in all reality, not merely against some hearer's belief — the strongest sentence the frame ever carries.",
      "«Allah» — merfû; lâ'nın isminin MAHALLİNDEN (mübtedâlık mahallinden) bedel ve MAKSÛRUN ALEYH: vasfın kendisine hasredildiği tek sahip. Bu kasr ḤAKÎKÎdir — bir muhatabın zannına karşı değil, bütün vâkıada doğru — çatının taşıdığı en güçlü cümle.",
      punct=".")],
 "jumal": [
  J("لَا إِلَهَ إِلَّا اللهُ",
    "قَصْرُ الصِّفَةِ عَلَى الْمَوْصُوفِ — حَقِيقَةً: وَصْفُ الْأُلُوهِيَّةِ مَقْصُورٌ عَلَى اللهِ تَعَالَى.",
    "SIFA confined to MAWSUF, haqiqatan: ilah-hood belongs to Allah and to no other, in reality — not merely against a hearer's belief. The source cites this very kalima as the haqiqi qasr's example.",
    "SIFANIN MEVSÛFA kasrı, hakikaten: ilahlık Allah'ındır, başkasının değil — vâkıada; yalnız bir muhatabın zannına karşı değil. Kaynak, hakîkî kasrın örneği olarak bizzat bu kelimeyi zikreder."),
  J("لَا إِلَهَ إِلَّا اللهُ",
    "وَالطَّرِيقُ: النَّفْيُ وَالِاسْتِثْنَاءُ — أَقْوَى طُرُقِ الْقَصْرِ.",
    "And the route: negation + exception — the strongest of the qasr's turuq, because it states the denial and the exception in separate words the ear cannot miss. (إِنَّمَا, the fronting, and عطف بلا are its gentler siblings — the qasr note walks all four.)",
    "Ve yol: nefiy + istisnâ — kasr yollarının en güçlüsü; çünkü inkârı ve istisnâyı kulağın kaçıramayacağı ayrı kelimelerle söyler. (إِنَّمَا, takdim ve بلا atfı daha yumuşak kardeşleridir — kasr notu dördünü de yürütür.)")]})

# ---------------------------------------------------------------- s2 — the house
S.append({"id": "s2", "translation": {
 "en": "No one is in the house but Zayd. (The attribute of being-in-the-house confined to Zayd — the everyday haqiqi qasr of a sifa to its mawsuf.)",
 "tr": "Evde Zeyd'den başkası yok. (Evde-bulunma vasfı Zeyd'e hasredilmiş — bir sıfatın mevsûfuna gündelik hakikî kasrı.)"},
 "tokens": [
  tok("مَا","ma-nafiya","part",["aqsam-al-qasr","anwa-ma"],
      "نَافِيَةٌ — وَ«إِلَّا» بَعْدَهَا عَلَامَةُ قَصْرٍ.",
      "«not» — and the illa standing later is this ma's own signature: negation-plus-exception, so the ma of the frame is always the NEGATION, whatever stands between them.",
      "«yok» — ve ilerideki illâ, bu mânın kendi imzasıdır: nefiy + istisnâ; çatının mâsı, arada ne durursa dursun her zaman NEFİYdir."),
  tok("فِي","fi","prep",["huruf-jarr","aqsam-al-qasr"],
      "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ هُوَ الْمَقْصُورُ: وَصْفُ الْكَوْنِ فِي الدَّارِ.",
      "«in» — the jarr phrase it opens is the MAQSUR: the attribute of being-in-the-house. A jarr phrase can only ever be the sifa side of a qasr — an attribute, never a bearer.",
      "«-de» — açtığı câr-mecrûr MAKSÛRdur: evde-bulunma vasfı. Bir câr-mecrûr, kasrın ancak sıfat tarafı olabilir — vasıftır, sahip olamaz."),
  tok("الدَّارِ","dar","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "«the house» — majrur under fi. (The same letters spell the amr of دَارَى — only the jarr letter before this word settles which it is.)",
      "«ev» — fî ile mecrûr. (Aynı harfler دَارَى'nın emrini de yazar — hangisi olduğunu yalnız önündeki cer harfi çözer.)"),
  tok("إِلَّا","illa","part",["aqsam-al-qasr"],
      "أَدَاةُ الِاسْتِثْنَاءِ الْمُفَرَّغِ.",
      "«but» — the exception, mufarragh: the negation left the sentence empty-handed, so what follows takes the case the sentence itself demands.",
      "«başka» — istisnâ; müferrağ: nefiy cümleyi eli boş bıraktı, ardından gelen cümlenin kendi istediği i'râbı alır."),
  tok("زَيْدٌ","zayd","propn",["aqsam-al-qasr"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَهُوَ الْمَقْصُورُ عَلَيْهِ.",
      "«Zayd» — the mubtada mu'akhkhar in raf' (the fronted jarr-khabar's old rule), and the MAQSUR ALAYH: the one bearer being-in-the-house is confined to. Haqiqatan possible here — a house CAN really hold only Zayd — which is why the sifa-to-mawsuf direction is the plentiful one.",
      "«Zeyd» — muahhar mübtedâ, merfû (öne alınmış câr haberin eski kuralı) ve MAKSÛRUN ALEYH: evde-bulunmanın kendisine hasredildiği tek sahip. Burada hakikaten mümkündür — bir evde gerçekten yalnız Zeyd olabilir — sıfat-mevsûf yönünün bol olması bundandır.",
      punct=".")],
 "jumal": [
  J("مَا فِي الدَّارِ إِلَّا زَيْدٌ",
    "قَصْرُ الصِّفَةِ عَلَى الْمَوْصُوفِ — وَهُوَ الْكَثِيرُ، وَقَدْ يَقَعُ حَقِيقَةً.",
    "Sifa on mawsuf again — the PLENTIFUL direction, and it can be literally true: survey the house and the claim checks out. Its mirror (one bearer confined to one attribute) almost never can — no census covers all a man's attributes.",
    "Yine sıfatın mevsûfa kasrı — BOL olan yön; ve harfiyen doğru olabilir: evi dolaş, iddia sağlanır. Aynadaki karşılığı (bir sahibin tek vasfa hasrı) neredeyse hiç olamaz — hiçbir sayım bir adamın bütün vasıflarını kuşatamaz."),
  J("مَا فِي الدَّارِ إِلَّا زَيْدٌ",
    "وَبَعْضُ الْأَحْيَانِ يُقْصَدُ بِهِ الْمُبَالَغَةُ: يُعَدُّ غَيْرُ الْمَذْكُورِ كَلَا شَيْءٍ.",
    "And sometimes even this direction is exaggeration: others ARE in the house, and the speaker counts them as nothing — the iddi'a the ch18 jins-lam already taught, wearing the illa frame now.",
    "Ve bazen bu yön bile mübâlağadır: evde başkaları DA vardır; konuşan onları hiç sayar — 18. bâbın cins lâmında öğrettiği iddiâ, şimdi illâ çatısını giymiş.")]})

# ---------------------------------------------------------------- s3 — mawsuf on sifa
S.append({"id": "s3", "translation": {
 "en": "Zayd is nothing but a writer. (The bearer confined to one attribute — and which KIND of qasr this is, only the addressee's state decides.)",
 "tr": "Zeyd kâtipten başka bir şey değildir. (Sahip tek vasfa hasredilmiş — ve bunun HANGİ kasr olduğuna yalnız muhatabın hâli karar verir.)"},
 "tokens": [
  tok("مَا","ma-nafiya","part",["aqsam-al-qasr","anwa-ma"],
      "نَافِيَةٌ عَامِلَةٌ عَمَلَ «لَيْسَ» أَوْ مُهْمَلَةٌ — وَالْقَصْرُ قَائِمٌ عَلَى كِلَا الْوَجْهَيْنِ.",
      "«not» — Hijazi (working like laysa) or bare: the schools differ on its government here, and the QASR stands on either reading — the frame's meaning does not hang on the i'rab khilaf.",
      "«değil» — Hicâzî (leyse gibi âmil) yahut mühmel: buradaki amelinde ekoller ayrılır; KASR her iki okumada da ayaktadır — çatının mânâsı i'râb hilâfına asılı değildir."),
  tok("زَيْدٌ","zayd","propn",["aqsam-al-qasr"],
      "مُبْتَدَأٌ (أَوِ اسْمُ «مَا») مَرْفُوعٌ — وَهُوَ الْمَقْصُورُ.",
      "«Zayd» — the MAQSUR this time: the bearer himself, about to be confined to a single attribute. Note the direction flipped from s2 — the propn stands BEFORE the illa now.",
      "«Zeyd» — bu kez MAKSÛR: sahibin kendisi; tek bir vasfa hasredilmek üzere. Yönün s2'den döndüğüne dikkat — özel isim şimdi illâdan ÖNCE duruyor."),
  tok("إِلَّا","illa","part",["aqsam-al-qasr"],
      "أَدَاةُ الِاسْتِثْنَاءِ الْمُفَرَّغِ.",
      "«but» — the same mufarragh exception.",
      "«başka» — aynı müferrağ istisnâ."),
  tok("كَاتِبٌ","katib","noun",["aqsam-al-qasr","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — وَهُوَ الْمَقْصُورُ عَلَيْهِ: صِفَةُ الْكِتَابَةِ.",
      "«a writer» — the khabar, and the MAQSUR ALAYH: the one attribute Zayd is confined to. Haqiqatan this is nearly impossible (a man has countless attributes), so the qasr is IDAFI — relative to an addressee — or exaggeration. And the sifa here is the balagha's: a meaning standing in another, not the nahw's adjective.",
      "«bir kâtip» — haber ve MAKSÛRUN ALEYH: Zeyd'in hasredildiği tek vasıf. Hakikaten bu neredeyse imkânsızdır (bir adamın sayısız vasfı vardır); o hâlde kasr İZÂFÎdir — muhataba göredir — yahut mübâlağadır. Buradaki sıfat belâgatindir: başkasında duran bir mânâ; nahvin sıfatı değil.",
      punct=".")],
 "jumal": [
  J("مَا زَيْدٌ إِلَّا كَاتِبٌ",
    "قَصْرُ الْمَوْصُوفِ عَلَى الصِّفَةِ — حَقِيقَةً يَكَادُ لَا يُوجَدُ، فَهُوَ إِضَافِيٌّ أَوِ ادِّعَاءٌ.",
    "MAWSUF on SIFA: the direction that haqiqatan almost does not exist — encircling ALL a bearer's attributes is beyond speech — so it lives as idafi qasr, or as deliberate exaggeration. The taxonomy's asymmetry is the chapter's first surprise.",
    "MEVSÛFUN SIFAYA kasrı: hakikaten neredeyse bulunmayan yön — bir sahibin BÜTÜN vasıflarını kuşatmak sözün gücünü aşar — o hâlde izâfî kasr yahut bilinçli mübâlağa olarak yaşar. Taksimin bakışımsızlığı bâbın ilk sürprizidir."),
  J("مَا زَيْدٌ إِلَّا كَاتِبٌ",
    "وَبِحَسَبِ الْمُخَاطَبِ: إِفْرَادٌ لِمَنِ اعْتَقَدَ الشَّرِكَةَ، قَلْبٌ لِمَنِ اعْتَقَدَ الْعَكْسَ، تَعْيِينٌ لِلْمُتَرَدِّدِ.",
    "One sentence, three kinds, and only the ADDRESSEE picks: said to one who thought Zayd both writes and makes verse, it is IFRAD (cutting the partnership); to one who thought him no writer at all, QALB (flipping the ruling); to one who could not decide, TAYIN (appointing). The words never change — the hearer does.",
    "Tek cümle, üç tür; ve seçimi yalnız MUHATAP yapar: Zeyd'i hem kâtip hem şair sanana söylenirse İFRAD (ortaklığı keser); onu hiç kâtip bilmeyene KALB (hükmü çevirir); karar veremeyene TAYİN (tayin eder). Kelimeler hiç değişmez — dinleyen değişir.")]})

# ---------------------------------------------------------------- s4 — sifa on mawsuf, ifrad
S.append({"id": "s4", "translation": {
 "en": "No one is a writer but Zayd. (Said to one who believed both Zayd and Amr write: qasr IFRAD — the partnership cut.)",
 "tr": "Zeyd'den başka kâtip yok. (Hem Zeyd'in hem Amr'ın kâtip olduğuna inanana söylenmiş: İFRAD kasrı — ortaklık kesilmiş.)"},
 "tokens": [
  tok("مَا","ma-nafiya","part",["aqsam-al-qasr"],
      "نَافِيَةٌ.",
      "«no one is» — the frame's negation again.",
      "«yok» — çatının nefyi yine."),
  tok("كَاتِبٌ","katib","noun",["aqsam-al-qasr"],
      "مُبْتَدَأٌ مَرْفُوعٌ (نَكِرَةٌ فِي سِيَاقِ النَّفْيِ تُفِيدُ الْعُمُومَ) — وَهُوَ الْمَقْصُورُ.",
      "«a writer» — the MAQSUR: the attribute side, and a nakira under negation reads as ALL: no writer whatsoever. The direction is s2's again (sifa on mawsuf), but this time the claim is plainly false in reality — other writers exist —",
      "«kâtip» — MAKSÛR: vasıf tarafı; ve nefiy siyâkındaki nekre UMUM okunur: hiçbir kâtip. Yön yine s2'ninki (sıfatın mevsûfa kasrı); fakat bu kez iddia vâkıada apaçık yanlıştır — başka kâtipler vardır —"),
  tok("إِلَّا","illa","part",["aqsam-al-qasr"],
      "أَدَاةُ الِاسْتِثْنَاءِ.",
      "«but» — the exception.",
      "«başka» — istisnâ."),
  tok("زَيْدٌ","zayd","propn",["aqsam-al-qasr"],
      "بَدَلٌ مَرْفُوعٌ — وَهُوَ الْمَقْصُورُ عَلَيْهِ: قَصْرُ إِفْرَادٍ لِمَنِ اعْتَقَدَ الشَّرِكَةَ.",
      "«Zayd» — the maqsur alayh; and because the claim is not literally true, the qasr is IDAFI, aimed at THIS addressee: he believed Zayd AND Amr both write, and the sentence cuts Amr away — qasr IFRAD, the partnership-cutter. Its condition: the two beliefs must not be contradictories, merely companions.",
      "«Zeyd» — maksûrun aleyh; ve iddia harfiyen doğru olmadığından kasr İZÂFÎdir, BU muhataba nişanlanmıştır: o, Zeyd'in DE Amr'ın DA kâtip olduğuna inanıyordu; cümle Amr'ı keser — İFRAD kasrı, ortaklık kesici. Şartı: iki inanç çelişik değil, yalnız yoldaş olmalı.",
      punct=".")],
 "jumal": [
  J("مَا كَاتِبٌ إِلَّا زَيْدٌ",
    "قَصْرُ إِفْرَادٍ: الْمُخَاطَبُ اعْتَقَدَ الشَّرِكَةَ، وَالْقَصْرُ يَقْطَعُهَا — وَشَرْطُهُ أَلَّا يَتَضَادَّ الْوَصْفَانِ.",
    "IFRAD: the hearer held BOTH claims at once (Zayd writes; Amr writes), which is only possible when the two do not contradict — the ifrad's own condition. The qasr does not flip his belief; it prunes it.",
    "İFRAD: dinleyen İKİ iddiayı birden tutuyordu (Zeyd kâtip; Amr kâtip) — bu ancak ikisi çelişmezse mümkündür; ifradın kendi şartı budur. Kasr inancını çevirmez; budar."),
  J("مَا كَاتِبٌ إِلَّا زَيْدٌ",
    "وَعَكْسُ اعْتِقَادِهِ: «مَا شَاعِرٌ إِلَّا زَيْدٌ» لِمَنِ اعْتَقَدَ أَنَّ الشَّاعِرَ عَمْرٌو — قَصْرُ قَلْبٍ.",
    "And the next sentence turns the addressee around: said to one who held the OPPOSITE (the poet is Amr, not Zayd), the same frame becomes qasr QALB — it flips his ruling whole. Contradiction between the beliefs is qalb's condition, exactly where ifrad forbade it.",
    "Ve sonraki cümle muhatabı döndürür: TERSİNİ tutana (şair Amr'dır, Zeyd değil) söylenince aynı çatı KALB kasrı olur — hükmünü bütünüyle çevirir. İnançlar arası çelişki kalbin şartıdır; ifradın yasakladığı tam o yerde.")]})

# ---------------------------------------------------------------- s5 — qalb
S.append({"id": "s5", "translation": {
 "en": "No one is a poet but Zayd. (Said to one who believed the poet is Amr: qasr QALB — the ruling flipped; said to one undecided between the two: TAYIN.)",
 "tr": "Zeyd'den başka şair yok. (Şairin Amr olduğuna inanana söylenmiş: KALB kasrı — hüküm çevrilmiş; ikisi arasında kararsıza söylenirse: TAYİN.)"},
 "tokens": [
  tok("مَا","ma-nafiya","part",["aqsam-al-qasr"],
      "نَافِيَةٌ.",
      "«no one is» — the same negation, third time: the frame is a MOLD, and the chapter fills it three ways.",
      "«yok» — aynı nefiy, üçüncü kez: çatı bir KALIPtır ve bâb onu üç türlü doldurur."),
  tok("شَاعِرٌ","shair","noun",["aqsam-al-qasr","ism-fail"],
      "مُبْتَدَأٌ مَرْفُوعٌ — الْمَقْصُورُ: صِفَةُ الشِّعْرِ.",
      "«a poet» — the maqsur: the attribute of poetry, denied of everyone —",
      "«şair» — maksûr: şiir vasfı; herkesten nefyedilmiş —"),
  tok("إِلَّا","illa","part",["aqsam-al-qasr"],
      "أَدَاةُ الِاسْتِثْنَاءِ.",
      "«but» — the exception.",
      "«başka» — istisnâ."),
  tok("زَيْدٌ","zayd","propn",["aqsam-al-qasr","qasr"],
      "بَدَلٌ مَرْفُوعٌ — الْمَقْصُورُ عَلَيْهِ: قَلْبًا لِمَنِ اعْتَقَدَ الْعَكْسَ، وَتَعْيِينًا لِلْمُتَرَدِّدِ.",
      "«Zayd» — the maqsur alayh, and the addressee names the kind: to one convinced the poet is AMR, this is QALB — his ruling reversed outright; to one who stood undecided between the two men, TAYIN — the wavering resolved. Three sentences, one frame, and the whole taxonomy taught by whom you say them to.",
      "«Zeyd» — maksûrun aleyh; ve türü muhatap adlandırır: şairin AMR olduğuna kāil olana bu KALBdir — hükmü baştan başa çevrilir; iki adam arasında kararsız durana TAYİN — tereddüt çözülür. Üç cümle, tek çatı; ve bütün taksim, kime söylediğinle öğretilir.",
      punct=".")],
 "jumal": [
  J("مَا شَاعِرٌ إِلَّا زَيْدٌ",
    "قَصْرُ قَلْبٍ: الْمُخَاطَبُ اعْتَقَدَ الْعَكْسَ، وَالْقَصْرُ يَقْلِبُ حُكْمَهُ — وَشَرْطُهُ التَّضَادُّ.",
    "QALB: the addressee's belief and the sentence cannot both stand — that contradiction is qalb's condition, the exact mirror of ifrad's. One taxonomy, two complementary conditions: the books' symmetry, worth showing whole.",
    "KALB: muhatabın inancı ile cümle birlikte ayakta duramaz — o çelişki kalbin şartıdır; ifradınkinin tam aynası. Tek taksim, iki tamamlayıcı şart: kitapların bakışımı; bütün hâliyle göstermeye değer."),
  J("مَا شَاعِرٌ إِلَّا زَيْدٌ",
    "وَقَصْرُ التَّعْيِينِ: لِمَنِ اسْتَوَى عِنْدَهُ الْأَمْرَانِ — يُعَيِّنُ الْقَصْرُ أَحَدَهُمَا.",
    "And TAYIN: to the hearer for whom the two stood level, the qasr appoints one. The three kinds exhaust the addressee's possible states — partnership, opposition, indecision — which is why the books' list stops at three.",
    "Ve TAYİN: iki şıkkın kendisinde eşit durduğu dinleyene kasr birini tayin eder. Üç tür, muhatabın mümkün hâllerini tüketir — ortaklık, karşıtlık, kararsızlık — kitapların listesinin üçte durması bundandır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "illa": copy_gloss("aqaid-ahl-al-sunna", "illa"),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/21.json").write_text(
    json.dumps({"chapter": 21, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 21 for c in man["chapters"]):
    man["chapters"].append({"n": 21, "title": TITLE21})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.21.0"
ADD_EN = (" Chapter 21 opens the qasr bab from the same file (lines ~1790-1840, sahifa 61-63): the matn's "
          "frames مَا زَيْدٌ إِلَّا كَاتِبٌ, مَا كَاتِبٌ إِلَّا زَيْدٌ, مَا شَاعِرٌ إِلَّا زَيْدٌ and مَا فِي الدَّارِ إِلَّا زَيْدٌ, "
          "and the kalima لَا إِلَهَ إِلَّا اللهُ which the source itself cites for the haqiqi qasr.")
ADD_TR = (" Yirmi birinci bâb, kasr bâbını aynı dosyadan açar (satır ~1790-1840, sahife 61-63): metnin "
          "kalıpları مَا زَيْدٌ إِلَّا كَاتِبٌ, مَا كَاتِبٌ إِلَّا زَيْدٌ, مَا شَاعِرٌ إِلَّا زَيْدٌ ve مَا فِي الدَّارِ إِلَّا زَيْدٌ, "
          "ve kaynağın hakîkî kasr için bizzat zikrettiği لَا إِلَهَ إِلَّا اللهُ kelimesi.")
if "1790-1840" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch21:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
