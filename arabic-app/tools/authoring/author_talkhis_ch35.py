# -*- coding: utf-8 -*-
"""Author chapter 35 of talkhis-al-miftah — كَمَالُ الِانْقِطَاعِ وَشِبْهُهُ.

Sahifa 83-84 (lines ~2283-2295 and ~2361-2371): the fasl's remaining two
dawa'i, closing the four (kamal ittisal ch33, shibh kamal ittisal ch34):

  {1} KAMAL INQITA' BILA IHAM — the jumlas differ in khabar/insha (in
      word and sense, or in sense alone), or share no jihat jamia:
      • al-Akhtal's bayt: وَقَالَ رَائِدُهُمْ أَرْسُوا نُزَاوِلُهَا —
        أَرْسُوا insha in word and sense, نُزَاوِلُهَا khabar in both,
        so the atf is dropped between them;
      • مَاتَ فُلَانٌ رَحِمَهُ اللهُ — the second KHABAR in word, DUA in
        sense: fasl again;
      • زَيْدٌ طَوِيلٌ عَمْرٌو نَائِمٌ — both khabari, but no jihat
        jamia joins tallness to sleep: fasl.
  {2} SHIBH KAMAL INQITA' — the atf would suggest the WRONG hookup:
      وَتَظُنُّ سَلْمَى أَنَّنِي أَبْغِي بِهَا بَدَلًا • أُرَاهَا فِي
      الضَّلَالِ تَهِيمُ — a waw before أُرَاهَا would be read as atf on
      أَبْغِي, planting the poet's counter-thought INSIDE Salma's
      supposition; to kill that misreading the atf is dropped.

ATTRIBUTION: s1-s2 are al-Akhtal's bayt and s5-s6 the Salma bayt exactly
as the source cites them, in verse dress; s3-s4 are the source's own
worked examples, verbatim. Ottoman orthography normalized to standard
(يَجْرِى → يَجْرِي — the dotless ya) — recorded normalizations.

Grammar this chapter teaches:
  • note 138 `kamal-al-inqita` — both halves of the doctrine (bila iham:
    fasl wajib; ma'a iham: WASL wajib, the لَا وَأَيَّدَكَ اللهُ bad-dua
    guard) and the catalogue of the four fasl dawa'i + two wasl dawa'i.
  • note 139 `shibh-kamal-al-inqita` — the iham of the wrong hookup,
    with the source's own khilaf (أُرَاهَا also reads as isti'naf, and
    on that reading the fasl is shibh kamal ITTISAL).
  • new paradigms: ظَنَّ (I geminate whose lam is a nun — the idgham
    with the pronoun nun: ظَنَنَّا), أَرْسَى (IV naqis), زَاوَلَ (III of
    a hollow root — sound road), بَغَى (I naqis ya, bab daraba), هَامَ
    (I hollow ya, lazim); مَاتَ and رَحِمَ copied from samti after the
    lemma identity check.
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

TITLE35 = {"ar": "كَمَالُ الِانْقِطَاعِ وَشِبْهُهُ",
           "en": "Perfect Severance, and Its Semblance",
           "tr": "Kemâl-i İnkıtâ ve Benzeri"}

# --------------------- s1 — al-Akhtal: the command and the report, unjoined
S.append({"id": "s1", "translation": {
 "en": "And their scout said: halt — we engage it! (insha beside khabar: the FASL of kamal inqita' falls between the command and the report.)",
 "tr": "Öncüleri dedi ki: durun — savaşa girişiyoruz! (haber yanında inşâ: emirle haber arasına kemâl-i inkıtâ FASLI düşer.)"},
 "tokens": [
  tok("وَقَالَ","qala","verb",["kamal-al-inqita"],
      "الْوَاوُ عَاطِفَةٌ عَلَى مَا قَبْلَ الْبَيْتِ، وَقَالَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«and said» — the waw joins to what precedes the bayt; a mazi on the fatha.",
      "«ve dedi» — vâv, beyitten öncesine atfeder; fetha üzere mebnî mâzî.",
      segments=[seg("وَ","wa","part"), seg("قَالَ","qala","verb")]),
  tok("رَائِدُهُمْ","raid","noun",["kamal-al-inqita","ism-fail"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
      "«their scout» — the doer, marfu'; a mudaf with the pronoun annexed to it. The ra'id rides ahead to find water and ground — his word carries the camp.",
      "«öncüleri» — fâil, merfû; muzâf, zamir muzâfun ileyh. Râid, su ve konak bulmak için önden gider — sözü orduyu taşır.",
      segments=[seg("رَائِدُ","raid","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("أَرْسُوا","arsa","verb",["kamal-al-inqita","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَقُولُ الْقَوْلِ.",
      "«halt!» — the amr of أَرْسَى (anchor!), mabni on the DROPPED NUN, the waw its doer; what the scout said, insha in word and sense.",
      "«durun!» — أَرْسَى'nın emri (demirleyin!); NÛNUN HAZFİ üzere mebnî, vâv fâildir — makûlü'l-kavl; lafzan ve mânen inşâ."),
  tok("نُزَاوِلُهَا","zawala","verb",["kamal-al-inqita"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ نَحْنُ، وَالضَّمِيرُ مَفْعُولٌ بِهِ — جُمْلَةٌ خَبَرِيَّةٌ فُصِلَتْ عَنِ الْأَمْرِ لِكَمَالِ الِانْقِطَاعِ.",
      "«we engage it» — Form III mudari, marfu', doer «we», the pronoun (the battle) its object: khabar in word and sense, so NO waw may join it to the amr — kamal inqita' bila iham.",
      "«ona girişiyoruz» — III. bâbdan muzâri, merfû; fâil «biz», zamir (savaş) mef'ûlü: lafzan ve mânen haber; emre hiçbir vâv bağlayamaz — îhâmsız kemâl-i inkıtâ.",
      punct="•", segments=[seg("نُزَاوِلُ","zawala","verb"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("أَرْسُوا",
    "جُمْلَةٌ إِنْشَائِيَّةٌ لَفْظًا وَمَعْنًى — مَقُولُ الْقَوْلِ فِي مَحَلِّ نَصْبٍ.",
    "The command — insha in word and sense, standing as what was said (nasb position).",
    "Emir — lafzan ve mânen inşâ; makûlü'l-kavl olarak nasb mahallinde."),
  J("نُزَاوِلُهَا",
    "جُمْلَةٌ خَبَرِيَّةٌ لَفْظًا وَمَعْنًى — فُصِلَتْ لِكَمَالِ الِانْقِطَاعِ بِلَا إِيهَامٍ.",
    "The report — khabar in word and sense. Insha and khabar cannot share a waw: the fasl is KAMAL INQITA', with no misreading to fear.",
    "Haber — lafzan ve mânen haber. İnşâ ile haber vâv paylaşamaz: fasl, ÎHÂMSIZ KEMÂL-İ İNKITÂDIR.")]})

# ------------------------------- s2 — the bayt's reason: every death is fated
S.append({"id": "s2", "translation": {
 "en": "— for every man's doom runs by a measure. (the fa joins the REASON to the command it justifies.)",
 "tr": "— çünkü her kişinin eceli bir ölçüyle akar. (fâ, SEBEBİ gerekçelendirdiği emre bağlar.)"},
 "tokens": [
  tok("فَكُلُّ","kull","noun",["kamal-al-inqita"],
      "الْفَاءُ لِلتَّعْلِيلِ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«for every» — the fa of REASON (this clause justifies the daring), then kull as mubtada, a mudaf.",
      "«çünkü her» — TA'LÎL fâsı (bu cümle cüreti gerekçeler), sonra كُلُّ mübtedâ; muzâftır.",
      segments=[seg("فَ","fa","part"), seg("كُلُّ","kull","noun")]),
  tok("حَتْفِ","hatf","noun",["kamal-al-inqita","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ إِلَى مَا بَعْدَهُ.",
      "«doom» — mudaf ilayh in jarr, itself annexed to the next word: the chain runs two links.",
      "«ecel» — mecrur muzâfun ileyh; kendisi de sonrakine muzâf: zincir iki halka yürür.",
      segments=None),
  tok("امْرِئٍ","imru","noun",["kamal-al-inqita","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَعَيْنُهُ تَتْبَعُ حَرَكَةَ آخِرِهِ: امْرُؤٌ، امْرَأً، امْرِئٍ.",
      "«of a man» — the second mudaf ilayh, and the famous chameleon: its MIDDLE vowel follows its ENDING — امْرُؤٌ in raf', امْرَأً in nasb, امْرِئٍ in jarr.",
      "«bir kişinin» — ikinci muzâfun ileyh ve meşhur bukalemun: ORTA harekesi SONUNA uyar — ref'te امْرُؤٌ, nasbda امْرَأً, cerde امْرِئٍ."),
  tok("يَجْرِي","jara","verb",["kamal-al-inqita"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.",
      "«runs» — mudari, marfu' by a damma ESTIMATED on the ya (too heavy to say); the clause is the khabar of kull.",
      "«akar» — muzâri; dammesi yâ üzerinde TAKDÎRÎ (söylenmesi ağır); cümle, كُلُّ'nün haberidir."),
  tok("بِمِقْدَارٍ","miqdar","noun",["kamal-al-inqita"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيَجْرِي.",
      "«by a measure» — the jarr phrase hanging on the running: no death arrives unmeasured.",
      "«bir ölçüyle» — يَجْرِي'ye taalluk eden câr-mecrûr: hiçbir ölüm ölçüsüz gelmez.",
      punct="•", segments=[seg("بِ","bi","part"), seg("مِقْدَارٍ","miqdar","noun")])],
 "jumal": [
  J("فَكُلُّ حَتْفِ امْرِئٍ يَجْرِي بِمِقْدَارٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ بِفَاءِ التَّعْلِيلِ.",
    "The scout's reason, joined by the fa — the joining is fine HERE, because reason and command share their jiha.",
    "Öncünün gerekçesi, fâ ile bağlı — BURADA bağlamak yerindedir; çünkü sebep ile emir cihetini paylaşır."),
  J("يَجْرِي بِمِقْدَارٍ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ كُلُّ.",
    "The khabar clause of kull — raf' position.",
    "كُلُّ'nün haber cümlesi — ref mahallinde.")]})

# --------------------------- s3 — the report that is really a prayer: fasl
S.append({"id": "s3", "translation": {
 "en": "So-and-so died — Allah have mercy on him. (khabar in word, DUA in sense: the difference severs.)",
 "tr": "Falanca öldü — Allah ona rahmet etsin. (lafzan haber, mânen DUÂ: fark, keser.)"},
 "tokens": [
  tok("مَاتَ","mata-die","verb",["kamal-al-inqita"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«died» — a mazi on the fatha; khabar in word and in sense.",
      "«öldü» — fetha üzere mebnî mâzî; lafzan ve mânen haber."),
  tok("فُلَانٌ","fulan","noun",["kamal-al-inqita"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — كِنَايَةٌ عَنِ الْعَلَمِ.",
      "«so-and-so» — the doer, marfu'; the word that stands in for ANY proper name.",
      "«falanca» — fâil, merfû; HERHANGİ bir özel ismin yerini tutan kelime."),
  tok("رَحِمَهُ","rahima","verb",["kamal-al-inqita","khabar-fi-mana-al-insha"],
      "فِعْلٌ مَاضٍ، وَالضَّمِيرُ مَفْعُولٌ بِهِ مُقَدَّمٌ — لَفْظُهُ الْخَبَرُ وَمَعْنَاهُ الدُّعَاءُ.",
      "«have mercy on him» — a mazi with the object pronoun aboard; its WORD is a report, its SENSE a prayer.",
      "«ona rahmet etsin» — mef'ûl zamiri üzerinde mâzî; LAFZI haber, MÂNÂSI duâdır.",
      segments=[seg("رَحِمَ","rahima","verb"), seg("هُ","pron-3ms","pron")]),
  tok("اللهُ","allah","propn",["kamal-al-inqita"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ — وَالْجُمْلَةُ دُعَائِيَّةٌ فُصِلَتْ لِكَمَالِ الِانْقِطَاعِ.",
      "«Allah» — the jalala as doer, marfu'. The prayer-clause is cut from the report: khabar and insha take no waw between them.",
      "«Allah» — fâil olarak lafz-ı celâl, merfû. Duâ cümlesi haberden kesilir: haber ile inşâ arasına vâv girmez.",
      punct=".")],
 "jumal": [
  J("مَاتَ فُلَانٌ",
    "جُمْلَةٌ خَبَرِيَّةٌ لَفْظًا وَمَعْنًى.",
    "The report — khabar through and through.",
    "Haber — lafzıyla da mânâsıyla da."),
  J("رَحِمَهُ اللهُ",
    "خَبَرِيَّةٌ لَفْظًا إِنْشَائِيَّةٌ مَعْنًى — فَالْفَصْلُ لِكَمَالِ الِانْقِطَاعِ.",
    "Khabar in word, prayer in sense — the sense decides, and the fasl is kamal inqita'.",
    "Lafzan haber, mânen duâ — hükmü mânâ verir ve fasl kemâl-i inkıtâdır.")]})

# ------------------------- s4 — two true reports with nothing between them
S.append({"id": "s4", "translation": {
 "en": "Zayd is tall. 'Amr is asleep. (both khabari — but no jihat jamia joins tallness to sleep: fasl.)",
 "tr": "Zeyd uzundur. Amr uyuyor. (ikisi de haber — fakat uzunlukla uykuyu birleştiren cihet-i câmia yok: fasl.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["kamal-al-inqita"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«Zayd» — the first mubtada, marfu'.",
      "«Zeyd» — ilk mübtedâ, merfû."),
  tok("طَوِيلٌ","tawil-long","noun",["kamal-al-inqita"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«tall» — its khabar. A complete, true sentence.",
      "«uzun» — haberi. Tam ve doğru bir cümle."),
  tok("عَمْرٌو","amr-alam",'propn',["kamal-al-inqita"],
      "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ — وَوَاوُهُ صَامِتَةٌ تَفْرِقُ بَيْنَهُ وَبَيْنَ عُمَرَ.",
      "«'Amr» — a second mubtada, marfu'; its silent waw only tells it from 'Umar on the page.",
      "«Amr» — ikinci mübtedâ, merfû; sessiz vâvı onu yazıda yalnız Ömer'den ayırır."),
  tok("نَائِمٌ","naaim","noun",["kamal-al-inqita","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — وَلَمَّا انْعَدَمَتِ الْجِهَةُ الْجَامِعَةُ وَجَبَ الْفَصْلُ.",
      "«asleep» — the second khabar. Both sentences are khabari, both true — but no jihat jamia relates tallness to sleeping, so the waw is FORBIDDEN: kamal inqita'.",
      "«uyuyan» — ikinci haber. İki cümle de haberdir, ikisi de doğru — fakat uzunlukla uyumayı bağlayan cihet-i câmia yok; vâv YASAKTIR: kemâl-i inkıtâ.",
      punct=".")],
 "jumal": [
  J("زَيْدٌ طَوِيلٌ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ.",
    "The first nominal sentence — about Zayd's build.",
    "İlk isim cümlesi — Zeyd'in boyu hakkında."),
  J("عَمْرٌو نَائِمٌ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ — لَا جِهَةَ جَامِعَةَ بَيْنَهُمَا فَامْتَنَعَ الْعَطْفُ.",
    "The second — about 'Amr's nap. Agreement in FORM is not a jiha: the topics never meet, so the atf is refused.",
    "İkincisi — Amr'ın uykusu hakkında. ŞEKİLCE uyuşmak cihet değildir: konular buluşmaz, atıf reddedilir.")]})

# -------------------- s5 — the Salma bayt: what Salma supposes (hemistich 1)
S.append({"id": "s5", "translation": {
 "en": "And Salma supposes that I seek a substitute for her —",
 "tr": "Selmâ, ona bir bedel aradığımı sanıyor —"},
 "tokens": [
  tok("وَتَظُنُّ","zanna","verb",["shibh-kamal-al-inqita","doubled-verbs"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَتَظُنُّ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِنْ أَفْعَالِ الْقُلُوبِ يَنْصِبُ مَفْعُولَيْنِ.",
      "«and supposes» — a geminate mudari, marfu'; a HEART-verb that governs two objects.",
      "«ve sanıyor» — muzâaf muzâri, merfû; iki mef'ûl alan KALP fiillerinden.",
      segments=[seg("وَ","wa","part"), seg("تَظُنُّ","zanna","verb")]),
  tok("سَلْمَى","salma","propn",["shibh-kamal-al-inqita","ism-maqsur-manqus"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَقْصُورَةِ.",
      "«Salma» — the doer, her damma estimated on the maqsur alif that can carry nothing.",
      "«Selmâ» — fâil; dammesi, hiçbir şey taşıyamayan maksûr elif üzerinde takdîrîdir."),
  tok("أَنَّنِي","anna","part",["shibh-kamal-al-inqita","inna-wa-akhawatuha","ya-al-mutakallim"],
      "أَنَّ حَرْفٌ نَاسِخٌ، وَنُونُ الْوِقَايَةِ، وَالْيَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ — وَالْمَصْدَرُ سَدَّ مَسَدَّ مَفْعُولَيْ ظَنَّ.",
      "«that I» — anna with the WIQAYA NUN and the speaker's ya as its ism (nasb position); the masdar-clause fills BOTH of zanna's object seats.",
      "«benim …-dığımı» — VİKAYE NÛNU ve mütekellim yâsı ismi olan أَنَّ (nasb mahalli); masdar, ظَنَّ'nin İKİ mef'ûl yerini birden doldurur.",
      segments=[seg("أَنَّ","anna","part"), seg("نِي","ni-wiqaya","pron")]),
  tok("أَبْغِي","bagha","verb",["shibh-kamal-al-inqita"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ أَنَا — وَالْجُمْلَةُ خَبَرُ أَنَّ.",
      "«I seek» — mudari, marfu' by the estimated damma on its ya, doer the concealed I; the clause is anna's khabar.",
      "«ararım» — muzâri; dammesi yâsı üzerinde takdîrî, fâili gizli ben; cümle أَنَّ'nin haberidir."),
  tok("بِهَا","bi",'part',["shibh-kamal-al-inqita"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَبْغِي — وَالْبَاءُ لِلْبَدَلِ: أَطْلُبُ بَدَلًا عَنْهَا.",
      "«for her» — the jarr phrase on the seeking; the BA OF EXCHANGE: a substitute in her place.",
      "«ona karşılık» — arayışa taalluk eden câr-mecrûr; BEDEL BÂSI: onun yerine bir bedel.",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("بَدَلًا","badal","noun",["shibh-kamal-al-inqita"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«a substitute» — the object of the seeking, plain fatha.",
      "«bir bedel» — arayışın mef'ûlü; açık fetha.",
      punct="•")],
 "jumal": [
  J("وَتَظُنُّ سَلْمَى أَنَّنِي أَبْغِي بِهَا بَدَلًا",
    "جُمْلَةٌ فِعْلِيَّةٌ — ظَنُّ سَلْمَى، وَفِيهِ مَا تَظُنُّهُ هِيَ.",
    "Salma's supposition, with its content folded inside the anna-clause: this whole hemistich is HER thought.",
    "Selmâ'nın zannı; içeriği أَنَّ cümlesinde dürülü: bu mısraın tamamı ONUN düşüncesidir."),
  J("أَنَّنِي أَبْغِي بِهَا بَدَلًا",
    "مَصْدَرٌ مُؤَوَّلٌ سَدَّ مَسَدَّ الْمَفْعُولَيْنِ.",
    "The rolled-up masdar standing where zanna's two objects would stand.",
    "ظَنَّ'nin iki mef'ûlünün yerinde duran müevvel masdar.")]})

# ------------- s6 — the poet's counter-thought, unjoined: the iham guarded
S.append({"id": "s6", "translation": {
 "en": "I deem HER the one wandering in error. (a waw here would hang this on «I seek» — INSIDE her thought; the fasl kills that misreading.)",
 "tr": "Ben ise ONUN dalâlet içinde şaşkın dolaştığını sanıyorum. (buradaki bir vâv bunu «ararım»a — onun düşüncesinin İÇİNE — asardı; fasl o yanlış okumayı öldürür.)"},
 "tokens": [
  tok("أُرَاهَا","raa","verb",["shibh-kamal-al-inqita","naib-al-fail"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ بِمَعْنَى أَظُنُّ، وَنَائِبُ الْفَاعِلِ أَنَا، وَالضَّمِيرُ مَفْعُولٌ بِهِ.",
      "«I deem her» — the PASSIVE mudari of رَأَى in the heart-sense («it is shown me» = I hold the view), the concealed I its deputy-doer, «her» the object.",
      "«onu sanırım» — رَأَى'nın kalp mânâsında MEÇHUL muzârisi («bana öyle gösterilir» = kanaatim odur); gizli ben nâib-i fâil, «onu» mef'ûl.",
      segments=[seg("أُرَا","raa","verb"), seg("هَا","pron-3fs","pron")]),
  tok("فِي","fi","part",["shibh-kamal-al-inqita"],
      "حَرْفُ جَرٍّ.",
      "«in» — the jarr letter.",
      "«içinde» — cer harfi."),
  tok("الضَّلَالِ","dalal","noun",["shibh-kamal-al-inqita"],
      "مَجْرُورٌ بِفِي، مُتَعَلِّقٌ بِتَهِيمُ.",
      "«error» — majrur by fi, hanging forward on the wandering.",
      "«dalâletin» — فِي ile mecrur; ileriye, şaşkın dolaşmaya taalluk eder."),
  tok("تَهِيمُ","hama","verb",["shibh-kamal-al-inqita"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ هِيَ — وَالْجُمْلَةُ مَفْعُولٌ ثَانٍ، وَقِيلَ حَالٌ.",
      "«wandering» — a hollow mudari, marfu', doer «she»; the clause is the second object of the deeming — some read it a hal. Both readings are in the books.",
      "«şaşkın dolaşır» — ecvef muzâri, merfû; fâili «o». Cümle, sanmanın ikinci mef'ûlüdür — hâl diyen de var. İki okuyuş da kitaplardadır.",
      punct="•")],
 "jumal": [
  J("أُرَاهَا فِي الضَّلَالِ تَهِيمُ",
    "جُمْلَةٌ مَفْصُولَةٌ لِشِبْهِ كَمَالِ الِانْقِطَاعِ — الْعَطْفُ يُوهِمُ عَطْفَهَا عَلَى أَبْغِي.",
    "The poet's answer, CUT LOOSE: a waw would be read as joining to «I seek» — making Salma think both thoughts. Meant on «she supposes», mis-read into it: shibh kamal inqita'.",
    "Şairin cevabı, KOPARILMIŞ: bir vâv «ararım»a atıf okunurdu — iki düşünceyi de Selmâ'ya verirdi. «Sanıyor»a kastedilen, içine yanlış okunan: şibh-i kemâl-i inkıtâ."),
  J("تَهِيمُ",
    "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ لِأُرَى، وَقِيلَ حَالٌ مِنَ الضَّمِيرِ.",
    "Nasb position — the deeming's second object; or, on the other reading, a hal of «her».",
    "Nasb mahallinde — sanmanın ikinci mef'ûlü; öbür okuyuşta «onu»dan hâl.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "raid": g("رَائِد", "ر و د", "noun", "scout, vanguard rider (ism fa'il)", "öncü, kılavuz süvari (ism-i fâil)", 5, plural="رُوَّاد"),
 "arsa": g("أَرْسَى", "ر س و", "verb", "to anchor, bring to a halt", "demirlemek, durdurmak", 5, form="IV"),
 "zawala": g("زَاوَلَ", "ز و ل", "verb", "to engage in, ply, grapple with", "girişmek, uğraşmak", 5, form="III"),
 "hatf": g("حَتْف", "ح ت ف", "noun", "death, doom", "ölüm, ecel", 5, plural="حُتُوف"),
 "imru": g("امْرُؤ", "م ر أ", "noun", "man, person (its middle vowel follows its ending: امْرُؤٌ، امْرَأً، امْرِئٍ)", "adam, kişi (orta harekesi son harekesine uyar: امْرُؤٌ، امْرَأً، امْرِئٍ)", 5),
 "fulan": g("فُلَان", None, "noun", "so-and-so (stands in for any proper name)", "falanca (herhangi bir özel ismin yerini tutar)", 3),
 "naaim": g("نَائِم", "ن و م", "noun", "sleeping, asleep (ism fa'il)", "uyuyan (ism-i fâil)", 3),
 "salma": g("سَلْمَى", None, "propn", "Salma (a woman's name)", "Selmâ (kadın adı)", 4),
 "zanna": g("ظَنَّ", "ظ ن ن", "verb", "to suppose, think", "zannetmek, sanmak", 3, form="I"),
 "bagha": g("بَغَى", "ب غ ي", "verb", "to seek, desire", "aramak, istemek", 4, form="I"),
 "badal": g("بَدَل", "ب د ل", "noun", "substitute, replacement", "bedel, karşılık", 3, plural="أَبْدَال"),
 "hama": g("هَامَ", "ه ي م", "verb", "to wander distracted, roam lovelorn", "şaşkın dolaşmak, âvâre gezmek", 5, form="I"),
 "mata-die": copy_gloss("wasiyyat-abi-hanifa-samti", "mata-die"),
 "rahima": copy_gloss("wasiyyat-abi-hanifa-samti", "rahima"),
 "miqdar": copy_gloss("wasiyyat-abi-hanifa-samti", "miqdar"),
 "dalal": copy_gloss("bad-al-amali", "dalal"),
 "anna": copy_gloss("mukhtasar-al-manar", "anna"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/35.json").write_text(
    json.dumps({"chapter": 35, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 35 for c in man["chapters"]):
    man["chapters"].append({"n": 35, "title": TITLE35})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.35.0"
ADD_EN = (" Chapter 35 carries kamal al-inqita' and its semblance (lines ~2283-2295 and "
          "~2361-2371, sahifa 83-84): s1-s2 are al-Akhtal's bayt and s5-s6 the Salma bayt "
          "exactly as the source cites them; s3-s4 are the source's own worked examples, "
          "verbatim. Ottoman orthography normalized to standard (the dotless ya of يَجْرِى "
          "written يَجْرِي) — recorded normalizations.")
ADD_TR = (" Otuz beşinci bâb kemâl-i inkıtâ ve benzerini taşır (satır ~2283-2295 ve "
          "~2361-2371, sahife 83-84): s1-s2 Ahtal'ın beyti, s5-s6 Selmâ beyti — kaynağın "
          "iktibas ettiği şekliyle aynen; s3-s4 kaynağın kendi işlenmiş misalleridir, aynen. "
          "Osmanlı imlâsı standart imlâya çevrildi (يَجْرِى'nın noktasız yâsı يَجْرِي "
          "yazıldı) — kayıtlı normalizasyonlardır.")
if "2283-2295" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "zanna" not in mo["verbs"]:
    # Form I geminate of bab nasara on the دَلَّ road — but its LAM IS A NUN,
    # so the broken stem's nun meets the pronoun suffixes' nun and contracts
    # (ظَنَنَّا، ظَنَنَّ، يَظْنُنَّ): the whole entry goes through idgham().
    mo["verbs"]["zanna"] = _sg.idgham(_sg.entry(
        "مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
        "ظَنّ", "ظَانّ",
        _sg.mazi14("ظَنّ", "ظَنَن"),
        _sg.mudari14("َ", "ظُنّ", "ظْنُن"),
        ["ظُنَّ", "ظُنَّا", "ظُنُّوا", "ظُنِّي", "ظُنَّا", "اُظْنُنْنَ"],
        "يَظُنَّ", "يَظُنَّ", "تَظُنَّ",
        "مَظْنُون", "ظُنَّ", "يُظَنُّ",
        "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَظُنَّ، وَيَجُوزُ لَمْ يَظْنُنْ؛ وَلَامُهُ نُونٌ تُدْغَمُ فِي نُونِ الضَّمِيرِ — ظَنَنَّا."))
if "arsa" not in mo["verbs"]:
    # Form IV naqis on the أَوْصَى road.
    mo["verbs"]["arsa"] = _sg.derived_naqis(
        _sg.B4, _sg.W4, "ُ", "أَرْسَ", "رْس", "i", "أَرْس",
        "إِرْسَاء", "مُرْسٍ", "مُرْسًى", "أُرْسِيَ", "يُرْسَى")
if "zawala" not in mo["verbs"]:
    # Form III of a hollow root: the weak letter stands as a full consonant
    # in this bab (زَاوَلَ يُزَاوِلُ like حَاوَلَ), so the SOUND derived maker
    # builds it; the passive rides فُوعِلَ (زُووِلَ like قُووِلَ).
    mo["verbs"]["zawala"] = _sg.derived(
        _sg.B3, _sg.W3, "ُ", "زَاوَل", "زَاوِل", "زَاوِل",
        "مُزَاوَلَة", "مُزَاوِل", "مُزَاوَل", "زُووِلَ", "يُزَاوَلُ")
if "bagha" not in mo["verbs"]:
    mo["verbs"]["bagha"] = _sg.naqis1(
        "daraba", "نَاقِصٌ يَائِيٌّ", "y", "بَغَ", "بْغ", "i", "اِبْغ",
        "بُغَاء", "بَاغٍ", "مَبْغِيّ", "بُغِيَ", "يُبْغَى")
if "hama" not in mo["verbs"]:
    # hollow ya of bab daraba, lazim — no majhul, no maful.
    mo["verbs"]["hama"] = _sg.hollow1(
        "daraba", "أَجْوَفُ يَائِيٌّ", "هَام", "هِم", "هِيم", "هِم", "هِيم", "هِم",
        "هَيَمَان", "هَائِم", None, None, None,
        "أَجْوَفُ يَائِيٌّ لَازِمٌ فَلَا مَجْهُولَ لَهُ.")
_smo = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json")
                  .read_text(encoding="utf-8"))["verbs"]
for _k in ("mata-die", "rahima"):
    if _k not in mo["verbs"]:
        mo["verbs"][_k] = _smo[_k]
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# --------------------------------------------------------- notes 138 + 139
GR = ROOT / "content/grammar"
NOTE138 = {
 "id": "kamal-al-inqita",
 "title": {"ar": "كَمَالُ الِانْقِطَاعِ — وَدَوَاعِي الْفَصْلِ وَالْوَصْلِ",
           "en": "Perfect severance — and the six reasons of fasl and wasl",
           "tr": "Kemâl-i inkıtâ — ve fasl ile vaslın altı sebebi"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — دواعي الفصل والوصل"],
 "question": {
  "en": ["Is one jumla a report and the other a request or prayer — in word, or in sense alone? Then no waw may join them: kamal inqita'.",
         "Do the two reports share any jihat jamia at all? زَيْدٌ طَوِيلٌ and عَمْرٌو نَائِمٌ do not — fasl again.",
         "Would DROPPING the waw be misread — لَا وَأَيَّدَكَ اللهُ heard as a curse? Then the wasl is obligatory: kamal inqita' MA'A iham."],
  "tr": ["Cümlenin biri haber, öteki talep veya duâ mı — lafzan yahut yalnız mânen? Vâv onları bağlayamaz: kemâl-i inkıtâ.",
         "İki haber herhangi bir cihet-i câmia paylaşıyor mu? زَيْدٌ طَوِيلٌ ile عَمْرٌو نَائِمٌ paylaşmaz — yine fasl.",
         "Vâvı DÜŞÜRMEK yanlış mı okunurdu — لَا وَأَيَّدَكَ اللهُ beddua mı işitilirdi? O zaman vasl vâcibdir: ÎHÂMLI kemâl-i inkıtâ."]},
 "plain": {
  "en": "When two jumlas differ in kind — one reports, the other commands or prays — or share no joining aspect at all, the waw is forbidden: kamal inqita'. Its mirror: where DROPPING the waw would be misread (لَا وَأَيَّدَكَ اللهُ heard as a curse), the wasl becomes obligatory.",
  "tr": "İki cümle türce ayrılırsa — biri haber verir, öteki emreder veya duâ eder — yahut hiçbir birleştirici cihet paylaşmazsa vâv yasaktır: kemâl-i inkıtâ. Aynası: vâvı DÜŞÜRMEK yanlış okunacaksa (لَا وَأَيَّدَكَ اللهُ beddua işitilir) vasl vâcib olur."},
 "explanation": {
  "en": "The bab's ledger closes here: FASL has four reasons — kamal inqita' (this note), kamal ittisal, shibh kamal inqita', shibh kamal ittisal — and WASL has two: kamal inqita' MA'A iham, and tawassut bayna l-kamalayn. KAMAL INQITA' BILA IHAM holds in two shapes. (1) The jumlas differ in khabar and insha — in word and sense both, as in al-Akhtal's وَقَالَ رَائِدُهُمْ أَرْسُوا نُزَاوِلُهَا (the command, then the report); or in sense alone, as in مَاتَ فُلَانٌ رَحِمَهُ اللهُ, where the prayer wears a report's dress. (2) The jumlas agree in kind but share NO jihat jamia: زَيْدٌ طَوِيلٌ عَمْرٌو نَائِمٌ — nothing relates tallness to sleep, so nothing licenses a waw. MA'A IHAM is the mirror image, and it COMPELS the wasl: in the refined speaker's لَا، وَأَيَّدَكَ اللهُ («no — and may Allah strengthen you»), the لَا stands for لَيْسَ الْأَمْرُ كَذَلِكَ (khabari) and the prayer is insha in sense — kamal inqita' by the rule; but drop the waw and the ear hears لَا أَيَّدَكَ اللهُ, «may Allah NOT strengthen you» — a curse. To bar the misreading, the atf is made: the one place the bab ORDERS a waw where its own arithmetic forbids one.",
  "tr": "Bâbın defteri burada kapanır: FASLIN dört sebebi vardır — kemâl-i inkıtâ (bu not), kemâl-i ittisâl, şibh-i kemâl-i inkıtâ, şibh-i kemâl-i ittisâl — VASLIN iki: ÎHÂMLI kemâl-i inkıtâ ve tevassut beyne'l-kemâleyn. ÎHÂMSIZ KEMÂL-İ İNKITÂ iki şekilde olur. (1) Cümleler haberlik-inşâlıkta ayrılır — hem lafzan hem mânen: Ahtal'ın وَقَالَ رَائِدُهُمْ أَرْسُوا نُزَاوِلُهَا beyti (emir, sonra haber); yahut yalnız mânen: مَاتَ فُلَانٌ رَحِمَهُ اللهُ — duâ, haber elbisesi giymiştir. (2) Türce uyuşur, fakat HİÇBİR cihet-i câmia paylaşmazlar: زَيْدٌ طَوِيلٌ عَمْرٌو نَائِمٌ — uzunlukla uykuyu hiçbir şey bağlamaz, vâva ruhsat yok. ÎHÂMLISI aynadaki aksidir ve vaslı VÂCİB kılar: zarif konuşanın لَا، وَأَيَّدَكَ اللهُ sözünde («hayır — Allah seni kuvvetlendirsin») لَا, lafzan haberî لَيْسَ الْأَمْرُ كَذَلِكَ yerindedir, duâ ise mânen inşâdır — kural gereği kemâl-i inkıtâ; fakat vâvı düşür, kulak لَا أَيَّدَكَ اللهُ işitir: «Allah seni kuvvetlendirMEsin» — beddua. Yanlış okumayı kesmek için atıf YAPILIR: bâbın kendi hesabının yasakladığı yerde vâvı EMRETTİĞİ tek yer.",},
 "examples": [
  {"ar": "أَرْسُوا نُزَاوِلُهَا",
   "en": "insha then khabar, in word and sense — the atf refused (al-Akhtal).",
   "tr": "lafzan ve mânen inşâ, sonra haber — atıf reddedildi (Ahtal).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "مَاتَ فُلَانٌ رَحِمَهُ اللهُ",
   "en": "the difference in SENSE alone: a prayer in a report's dress.",
   "tr": "yalnız MÂNÂDA ayrılık: haber elbisesinde bir duâ.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "زَيْدٌ طَوِيلٌ عَمْرٌو نَائِمٌ",
   "en": "two true reports with no jihat jamia — the fasl of unrelated things.",
   "tr": "cihet-i câmiası olmayan iki doğru haber — alâkasızların faslı.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"}],
 "commonMistakes": [
  {"wrong": "«Vâvsız yan yana duran her iki cümle bozuk metindir»",
   "right": "«Vâvsızlık çoğu kez HÜKÜMDÜR: fasl, dört sebebin biriyle vâcib olmuştur»",
   "why": {"en": "The bab's whole point: the missing waw is grammar, not damage. A prayer after a report (رَحِمَهُ اللهُ), an answer after its provoking question, a tawkid after its matbu' — each REFUSES the waw by rule. Only where the four reasons are absent and a jiha exists does the missing waw become a fault.",
           "tr": "Bâbın bütün derdi: eksik vâv hasar değil, gramerdir. Haberden sonra duâ (رَحِمَهُ اللهُ), doğurduğu sorudan sonra cevap, metbûundan sonra te'kîd — her biri vâvı KURALLA reddeder. Eksik vâv ancak dört sebep yokken ve cihet varken kusur olur."}}],
 "relatedNotes": ["al-fasl-wa-al-wasl", "kamal-al-ittisal", "shibh-kamal-al-ittisal",
                  "shibh-kamal-al-inqita", "khabar-fi-mana-al-insha"]}

NOTE139 = {
 "id": "shibh-kamal-al-inqita",
 "title": {"ar": "شِبْهُ كَمَالِ الِانْقِطَاعِ",
           "en": "The semblance of severance: guarding against the wrong hookup",
           "tr": "Şibh-i kemâl-i inkıtâ: yanlış bağlanmaya karşı koruma"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — دواعي الفصل: شبه كمال الانقطاع"],
 "question": {
  "en": ["If the waw were written, could the ear hang the clause on the WRONG antecedent? Then drop it: shibh kamal inqita'.",
         "In the Salma bayt: joined, أُرَاهَا reads as atf on أَبْغِي — the poet's answer swallowed into Salma's supposition."],
  "tr": ["Vâv yazılsaydı kulak cümleyi YANLIŞ öncüle asabilir miydi? O hâlde düşür: şibh-i kemâl-i inkıtâ.",
         "Selmâ beytinde: bağlansa أُرَاهَا, أَبْغِي üzerine atıf okunur — şairin cevabı Selmâ'nın zannının içine yutulurdu."]},
 "plain": {
  "en": "Sometimes joining is half-right: the atf is meant onto one clause but would be READ onto another. In the Salma bayt a waw before «I deem her astray» would hang it on «I seek» — inside Salma's thought. To kill the misreading, the waw is dropped: the semblance of severance.",
  "tr": "Bazen bağlamak yarı doğrudur: atıf bir cümleye kastedilir, fakat başkasına OKUNUR. Selmâ beytinde «onu şaşkın sanırım»dan önceki vâv, onu «ararım»a — Selmâ'nın düşüncesinin içine — asardı. Yanlış okumayı öldürmek için vâv düşürülür: kemâl-i inkıtânın benzeri."},
 "explanation": {
  "en": "SHIBH KAMAL INQITA': the second jumla could rightly be joined to the FIRST, but the written waw would be read as joining it to a NEARER (or otherwise likelier) clause — and on that reading the meaning breaks. The type sentence is the Salma bayt: وَتَظُنُّ سَلْمَى أَنَّنِي أَبْغِي بِهَا بَدَلًا • أُرَاهَا فِي الضَّلَالِ تَهِيمُ. Joined to تَظُنُّ, the second hemistich is the poet's own counter-thought — true to his intent. But a waw would be READ as atf on أَبْغِي inside the anna-clause, making «I deem her astray» one more thing SALMA supposes. The joining that serves the intent on one antecedent slanders it on the other, so the atf is dropped — a fasl that RESEMBLES kamal inqita' without being it (the clauses are intimately related; the severance only guards the reading). The source records the khilaf honestly: أُرَاهَا can also be read as an ISTI'NAF — the answer to «and how do YOU see her?» — and on that reading the fasl belongs to shibh kamal ITTISAL. One dropped waw, two lawful accounts of why it is dropped.",
  "tr": "ŞİBH-İ KEMÂL-İ İNKITÂ: ikinci cümle İLK cümleye pekâlâ bağlanabilirdi; fakat yazılan vâv, daha YAKIN (yahut daha akla gelir) bir cümleye atıf okunurdu — o okuyuşta da mânâ bozulur. Tip cümle Selmâ beytidir: وَتَظُنُّ سَلْمَى أَنَّنِي أَبْغِي بِهَا بَدَلًا • أُرَاهَا فِي الضَّلَالِ تَهِيمُ. تَظُنُّ'ye bağlanınca ikinci mısra şairin kendi karşı-düşüncesidir — kasta uygun. Fakat vâv, أَنَّ cümlesinin içindeki أَبْغِي üzerine atıf OKUNUR, «onu şaşkın sanırım»ı SELMÂ'nın zannettiği bir şey daha yapardı. Bir öncülde kasta hizmet eden bağlayış, ötekinde ona iftira eder; atıf düşürülür — kemâl-i inkıtâya BENZEYEN ama o olmayan bir fasl (cümleler sıkı akrabadır; kesme yalnız okuyuşu korur). Kaynak hilâfı dürüstçe kaydeder: أُرَاهَا bir İSTİ'NÂF da okunabilir — «peki SEN onu nasıl görüyorsun?» sorusunun cevabı — o okuyuşta fasl, şibh-i kemâl-i İTTİSÂLE âittir. Tek düşmüş vâv, düşüşünün iki meşru hesabı.",},
 "examples": [
  {"ar": "وَتَظُنُّ سَلْمَى أَنَّنِي أَبْغِي بِهَا بَدَلًا",
   "en": "Salma's supposition — the clause a wrong atf would land inside.",
   "tr": "Selmâ'nın zannı — yanlış atfın içine düşeceği cümle.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "أُرَاهَا فِي الضَّلَالِ تَهِيمُ",
   "en": "the poet's answer, cut loose to keep it OUT of her thought.",
   "tr": "şairin cevabı — onun düşüncesinin DIŞINDA kalsın diye koparılmış.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«Vâv düştüğüne göre iki mısra alâkasızdır»",
   "right": "«Mısralar sıkı alâkalıdır; vâv, yanlış öncüle OKUNMASIN diye düşmüştür»",
   "why": {"en": "Unrelatedness is kamal inqita' — a different reason with a different name. Here the severance is protective, not real: the poet ANSWERS Salma's thought; the fasl only stops the answer being filed inside it.",
           "tr": "Alâkasızlık kemâl-i inkıtâdır — başka adlı başka sebep. Buradaki kesme gerçek değil koruyucudur: şair Selmâ'nın düşüncesine CEVAP verir; fasl yalnız cevabın onun içine dosyalanmasını önler."}}],
 "relatedNotes": ["al-fasl-wa-al-wasl", "kamal-al-inqita", "shibh-kamal-al-ittisal", "atf-nasaq"]}

(GR / "kamal-al-inqita.json").write_text(
    json.dumps(NOTE138, ensure_ascii=False, indent=1), encoding="utf-8")
(GR / "shibh-kamal-al-inqita.json").write_text(
    json.dumps(NOTE139, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch35:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + zanna/arsa/zawala/bagha/hama (+2 copied); notes 138-139")
