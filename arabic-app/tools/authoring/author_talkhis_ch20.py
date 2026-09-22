# -*- coding: utf-8 -*-
"""Author chapter 20 of talkhis-al-miftah — أَحْوَالُ مُتَعَلِّقَاتِ الْفِعْلِ:
حَذْفُ الْمَفْعُولِ وَتَقْدِيمُهُ.

A new bab opens: the verb's complements. Chapter 20 carries its first two
doctrines, each shipped as NAMED jumal rows (the ch18/ch19 pattern):

  • تَنْزِيلُ الْمُتَعَدِّي مَنْزِلَةَ اللَّازِمِ — قُلْ هَلْ يَسْتَوِي الَّذِينَ
    يَعْلَمُونَ وَالَّذِينَ لَا يَعْلَمُونَ (Zumar 39:9): the object is not
    omitted, it was never intended — knowing itself is the predicate.
  • الْإِبْهَامُ ثُمَّ الْبَيَانُ — وَلَوْ شَاءَ لَهَدَاكُمْ أَجْمَعِينَ (An'am
    6:149): mashi'a's object drops because it is not strange, and the
    jawab names it.
  • التَّعْمِيمُ مَعَ الِاخْتِصَارِ — وَاللَّهُ يَدْعُو إِلَى دَارِ السَّلَامِ
    (Yunus 10:25): drop جَمِيعَ عِبَادِهِ and the call reaches everyone.
  • رِعَايَةُ الْفَاصِلَةِ — مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَى (Duha 93:3): the
    kaf of قَلَاكَ drops for the rhyme of the suras.
  • تَقْدِيمُ الْمَفْعُولِ لِلتَّخْصِيصِ — إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
    (Fatiha 1:4): You ALONE — with the aksariyya rule (most fronting
    restricts; some is mere ihtimam/tabarruk).

ATTRIBUTION: every Arabic word is VERBATIM received Qur'anic text quoted
exactly (Zumar 39:9, An'am 6:149, Yunus 10:25, Duha 93:3, Fatiha 1:4),
following research/sources/talkhis-al-miftah-balagha.txt lines ~1620-1700
(sahifa 55-59), which cites each aya for the doctrine taught here.

Grammar this chapter is chosen to teach:
  • note 122 `hadhf-al-maful` — the wujuh of dropping the object and of
    fronting it, with the refusal doctrine (مَا زَيْدًا ضَرَبْتُ وَلَا غَيْرَهُ
    is not said) carried in the note.
  • TaqdimEngine grew the maful-muqaddam frame (iyya family or fathatan
    noun + verb directly after), and the WawEngine stopped offering hal
    before إِيَّاكَ — the iyya family opens a VERBAL clause.
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
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
S = []

TITLE20 = {"ar": "أَحْوَالُ مُتَعَلِّقَاتِ الْفِعْلِ — حَذْفُ الْمَفْعُولِ وَتَقْدِيمُهُ",
           "en": "The Verb's Complements — the Object Dropped and Fronted",
           "tr": "Fiilin Müteallakātının Halleri — Mef'ûlün Hazfi ve Takdimi"}

# ---------------------------------------------------------------- s1 — Zumar 9
S.append({"id": "s1", "translation": {
 "en": "Say: are those who know and those who do not know equal? (al-Zumar 39:9 — the transitive verb DEMOTED to intransitive rank: no object is meant; knowing itself is the whole predicate.)",
 "tr": "De ki: hiç bilenlerle bilmeyenler bir olur mu? (Zümer 39:9 — müteaddî fiil lâzım menzilesine indirilmiş: mef'ûl kastedilmemiştir; bilmenin kendisi yüklemin tamamıdır.)"},
 "tokens": [
  tok("قُلْ","qala","verb",[],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ.",
      "«Say» — the amr of قَالَ, its hollow middle dropped against the sukun.",
      "«De» — قَالَ'nin emri; ecvef ortası sükûn karşısında düşmüş."),
  tok("هَلْ","hal-istifham","part",[],
      "حَرْفُ اسْتِفْهَامٍ — وَالِاسْتِفْهَامُ هُنَا لِلْإِنْكَارِ.",
      "«are…?» — the question letter, and the question here DENIES: of course they are not equal.",
      "«hiç … mi?» — istifham harfi; buradaki soru İNKÂR içindir: elbette bir olmazlar."),
  tok("يَسْتَوِي","istawa","verb",[],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.",
      "«are equal» — Form VIII of س و ي, a naqis: its damma is estimated on the ya, too heavy to sound. The ya is the RADICAL, not a pronoun — the corpus paradigm is what settles that.",
      "«bir olur» — س و ي'nin VIII. bâbı; nâkıs: dammesi yâ üzerinde takdîr edilir — söylenmesi ağırdır. Yâ, ZAMİR değil ASIL harftir; bunu külliyat paradigması karara bağlar."),
  tok("الَّذِينَ","alladhina","pron",[],
      "اسْمٌ مَوْصُولٌ فَاعِلٌ.",
      "«those who» — the relative, standing as fa'il of the equality-verb.",
      "«o kimseler ki» — ism-i mevsûl; eşitlik fiilinin fâili."),
  tok("يَعْلَمُونَ","alima","verb",["hadhf-al-maful"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ — نُزِّلَ مَنْزِلَةَ اللَّازِمِ فَلَا مَفْعُولَ لَهُ.",
      "«who KNOW» — and the teaching is what is NOT there: عَلِمَ takes an object, and none is meant. The verb is set at the rank of an intransitive: the claim is not «they know something particular» but that knowing is their state. Nothing is reconstructed, because nothing was dropped — the object was never intended.",
      "«BİLENLER» — ve ders, orada OLMAYANdadır: عَلِمَ mef'ûl alır ve hiçbiri kastedilmemiştir. Fiil lâzım menzilesine konmuştur: iddia «belli bir şeyi bilirler» değil; bilmenin onların hâli olduğudur. Hiçbir şey takdîr edilmez, çünkü hiçbir şey düşmemiştir — mef'ûl hiç kastedilmemiştir."),
  tok("وَالَّذِينَ","alladhina","pron",["anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَالْمَوْصُولُ مَعْطُوفٌ.",
      "«and those who» — joined to the first relative.",
      "«ve o kimseler ki» — ilk mevsûle atfedilmiş.",
      segments=[seg("وَ","wa","part"), seg("الَّذِينَ","alladhina","pron")]),
  tok("لَا","la-nafiya","part",[],
      "نَافِيَةٌ لَا عَمَلَ لَهَا فِي الْمُضَارِعِ.",
      "«not» — plain negation over the mudari.",
      "«-mez» — muzâri üzerinde amelsiz nefiy."),
  tok("يَعْلَمُونَ","alima","verb",["hadhf-al-maful"],
      "مِثْلُ أُخْتِهِ — مُنَزَّلٌ مَنْزِلَةَ اللَّازِمِ.",
      "«do not know» — the twin, demoted the same way: not-knowing as a state, no object in view. Sakkaki adds: in a KHATABI maqam the generalized verb affirms knowing of the one and denies it of the other, blocking any arbitrary escape.",
      "«bilmezler» — ikizi; aynı şekilde indirilmiş: hâl olarak bilmemek, görüşte mef'ûl yok. Sekkâkî ekler: HİTÂBÎ makamda umumîleşen fiil, bilmeyi birine isbat, ötekinden nefyeder — keyfî kaçışı kapatır.",
      punct=".")],
 "jumal": [
  J("هَلْ يَسْتَوِي الَّذِينَ يَعْلَمُونَ وَالَّذِينَ لَا يَعْلَمُونَ",
    "الْوَجْهُ الْأَوَّلُ: تَنْزِيلُ الْمُتَعَدِّي مَنْزِلَةَ اللَّازِمِ — لَا حَذْفَ وَلَا تَقْدِيرَ.",
    "WAJH 1 — the demotion: when the speaker's purpose is to affirm the act of its doer absolutely (or deny it), the transitive is SET AT the intransitive's rank. No object is reconstructed — a taqdir here would ruin the point, which is knowing as such.",
    "1. VECİH — tenzîl: konuşanın maksadı fiili fâiline mutlak olarak isbat (yahut nefiy) ise, müteaddî LÂZIM menzilesine konur. Mef'ûl takdîr edilmez — burada takdir, maksadı bozar; maksat bilmenin kendisidir."),
  J("هَلْ يَسْتَوِي الَّذِينَ يَعْلَمُونَ وَالَّذِينَ لَا يَعْلَمُونَ",
    "وَفَرْقُ الْبَابِ: هَذَا غَيْرُ الْحَذْفِ — الْمَحْذُوفُ مُقَدَّرٌ، وَالْمُنَزَّلُ لَا مَفْعُولَ لَهُ أَصْلًا.",
    "And the bab's dividing line: DEMOTION is not OMISSION. An omitted object can be named back (the coming ayat name theirs); a demoted verb never had one in view. Confusing the two is the chapter's own commonMistake.",
    "Ve bâbın ayırım çizgisi: TENZÎL, HAZİF değildir. Hazfedilen mef'ûl geri adlandırılabilir (gelecek âyetler kendilerininkini adlandırır); tenzîl edilmiş fiilin görüşte mef'ûlü hiç olmamıştır. İkisini karıştırmak, bâbın kendi yaygın hatasıdır.")]})

# ---------------------------------------------------------------- s2 — An'am 149
S.append({"id": "s2", "translation": {
 "en": "And had He willed, He would have guided you all. (al-An'am 6:149 — mashi'a's object dropped for IBHAM then BAYAN: the jawab names what the shart left dark.)",
 "tr": "Dileseydi hepinizi hidayete erdirirdi. (En'âm 6:149 — meşîet fiilinin mef'ûlü İBHÂM sonra BEYÂN için hazfedilmiş: şartın karanlık bıraktığını cevap adlandırır.)"},
 "tokens": [
  tok("وَلَوْ","law","part",["in-shartiyya"],
      "الْوَاوُ عَاطِفَةٌ وَ«لَوْ» حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.",
      "«and had» — law: the shart certainly did not happen, so neither did the jawab.",
      "«ve eğer … -seydi» — lev: şart kesinlikle olmadı, cevap da olmadı.",
      segments=[seg("وَ","wa","part"), seg("لَوْ","law","part")]),
  tok("شَاءَ","shaa","verb",["hadhf-al-maful"],
      "فِعْلُ الشَّرْطِ — وَمَفْعُولُهُ «هِدَايَتَكُمْ» مَحْذُوفٌ لِلْإِبْهَامِ ثُمَّ الْبَيَانِ.",
      "«He willed» — and willed WHAT? The object (هِدَايَتَكُمْ, your guidance) is dropped, and the drop is a technique: the mashi'a is left DARK for one beat, and the jawab lights it. The rule beneath: a mashi'a-object drops when it is nothing strange; Abu Yaqub's «had I wished to weep BLOOD» keeps its object precisely because weeping blood is gharib.",
      "«diledi» — NEYİ diledi? Mef'ûl (هِدَايَتَكُمْ, hidayetinizi) hazfedilmiştir ve hazif bir tekniktir: meşîet bir vuruş KARANLIK bırakılır, cevap onu aydınlatır. Alttaki kural: meşîet mef'ûlü, garip bir şey değilse düşer; Ebû Ya'kūb'un «KAN ağlamak isteseydim» sözü mef'ûlünü tam da kan ağlamak garip olduğu için söyler."),
  tok("لَهَدَاكُمْ","hada","verb",["hadhf-al-maful"],
      "اللَّامُ وَاقِعَةٌ فِي جَوَابِ «لَوْ»، وَ«هَدَى» مَاضٍ وَ«كُمْ» مَفْعُولُهُ — وَهُوَ الْبَيَانُ.",
      "«He would have guided you» — the jawab wearing law's beloved lam, and it IS the bayan: the guiding named here tells the hearer what the willing was about. One clause holds the dark word and the lamp.",
      "«sizi hidayete erdirirdi» — lev'in sevdiği lâmı giymiş cevap; ve BEYÂNIN kendisidir: burada adlanan hidayet, dilemenin neye dair olduğunu söyler. Tek cümle, karanlık kelimeyle kandili birlikte taşır.",
      segments=[seg("لَ","lam-jawab","part"), seg("هَدَا","hada","verb"), seg("كُمْ","pron-2mp","pron")]),
  tok("أَجْمَعِينَ","ajmain","noun",["tawkid"],
      "تَوْكِيدٌ مَعْنَوِيٌّ لِلضَّمِيرِ «كُمْ» مَنْصُوبٌ بِالْيَاءِ.",
      "«all of you» — the ma'nawi tawkid riding the object pronoun, its nasb shown by the ya: had He willed, not one would be left unguided.",
      "«hepinizi» — mef'ûl zamirine binen mânevî te'kid; nasbı yâ iledir: dileseydi, hidayetsiz bir kişi kalmazdı.",
      punct=".")],
 "jumal": [
  J("وَلَوْ شَاءَ لَهَدَاكُمْ أَجْمَعِينَ",
    "الْوَجْهُ الثَّانِي: حَذْفُ مَفْعُولِ الْمَشِيئَةِ لِلْإِبْهَامِ ثُمَّ الْبَيَانِ.",
    "WAJH 2 — IBHAM then BAYAN: leave the willing unspecified, then let the jawab specify it. The suspense is one clause long, and the drop is licensed because a mashi'a-object is expected — only a GHARIB object (weeping blood) must be spoken.",
    "2. VECİH — İBHÂM sonra BEYÂN: dilemeyi belirsiz bırak, cevabın belirlemesine izin ver. Gerilim tek cümle sürer; hazfe cevaz, meşîet mef'ûlünün beklenen bir şey olmasındandır — yalnız GARİP mef'ûl (kan ağlamak) söylenmek zorundadır."),
  J("وَلَوْ شَاءَ لَهَدَاكُمْ أَجْمَعِينَ",
    "وَشَاهِدُ الْعَكْسِ: «وَلَوْ شِئْتُ أَنْ أَبْكِيَ دَمًا لَبَكَيْتُهُ» — ذُكِرَ لِغَرَابَتِهِ.",
    "And the counter-witness, kept in the note: Abu Yaqub SPEAKS his object because weeping blood is strange; al-Jawhari's second bakaytu tafakkuran is excluded from this bab — there the mention is for want of a qarina, not for gharaba. The books split hairs here on purpose; so do we.",
    "Ve aksin şahidi (notta saklı): Ebû Ya'kūb mef'ûlünü SÖYLER, çünkü kan ağlamak gariptir; Cevherî'nin ikinci bekeytü tefekkuran'ı bu bâbdan değildir — orada zikir, garâbetten değil karîne yokluğundandır. Kitaplar burada kılı kırk yarar; biz de yararız.")]})

# ---------------------------------------------------------------- s3 — Yunus 25
S.append({"id": "s3", "translation": {
 "en": "And Allah calls to the Abode of Peace. (Yunus 10:25 — the object جَمِيعَ عِبَادِهِ dropped for TA'MIM with brevity: the call is to everyone.)",
 "tr": "Allah selâmet yurduna çağırır. (Yûnus 10:25 — mef'ûl جَمِيعَ عِبَادِهِ, kısaltmayla birlikte TAMİM için hazfedilmiş: çağrı herkesedir.)"},
 "tokens": [
  tok("وَاللَّهُ","allah","propn",["anwa-al-waw","mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ.",
      "«And Allah» — a fresh sentence; the Name as mubtada.",
      "«Ve Allah» — yeni cümle; lafza-i celâl mübtedâ.",
      segments=[seg("وَ","wa","part"), seg("اللَّهُ","allah","propn")]),
  tok("يَدْعُو","daa","verb",["hadhf-al-maful","tajaddud-wa-thubut"],
      "فِعْلٌ مُضَارِعٌ — مَفْعُولُهُ «جَمِيعَ عِبَادِهِ» مَحْذُوفٌ لِلتَّعْمِيمِ مَعَ الِاخْتِصَارِ.",
      "«calls» — and calls WHOM? Everyone: drop the object and no listener can read himself out of the call. The named-object sentence (He calls His servants) is LONGER and says LESS — the drop generalizes and abbreviates in one stroke. The mudari adds renewal: the calling stands open now.",
      "«çağırır» — ve KİMİ çağırır? Herkesi: mef'ûlü düşür; hiçbir dinleyen kendini çağrının dışına okuyamaz. Mef'ûllü cümle (kullarını çağırır) hem daha UZUNdur hem daha az söyler — hazif tek hamlede hem umumîleştirir hem kısaltır. Muzâri teceddüt katar: çağrı şimdi de açıktır."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ.",
      "«to» — the endpoint letter: the call has a destination.",
      "«-e» — gayenin sonu harfi: çağrının bir varış yeri var."),
  tok("دَارِ","dar","noun",["tarif-bil-idafa"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the Abode» — majrur under ila, and a mudaf: definite through what follows. (The same letters spell the amr of دَارَى — «humour him!» — and only the jarr letter before this word settles which it is.)",
      "«yurduna» — ilâ altında mecrûr ve muzâf: sonrakiyle marife. (Aynı harfler دَارَى'nın emrini de yazar — «idare et!» — hangisi olduğunu yalnız önündeki cer harfi çözer.)"),
  tok("السَّلَامِ","salam","noun",["tarif-bil-idafa"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«of Peace» — the mudaf ilayh: Paradise named by what is found there.",
      "«selâmın» — muzâfun ileyh: cennet, içinde bulunanla adlandırılmış.",
      punct=".")],
 "jumal": [
  J("وَاللَّهُ يَدْعُو إِلَى دَارِ السَّلَامِ",
    "الْوَجْهُ الثَّالِثُ: حَذْفُ الْمَفْعُولِ لِلتَّعْمِيمِ مَعَ الِاخْتِصَارِ.",
    "WAJH 3 — TA'MIM: the unnamed object is every servant. Naming any set would fence the call; silence fences nothing. And it comes with brevity for free — the rare case where saying less asserts more.",
    "3. VECİH — TAMİM: adlanmayan mef'ûl her kuldur. Herhangi bir küme adlamak çağrıyı çitlerdi; susku hiçbir şeyi çitlemez. Ve kısaltma bedavaya gelir — az söylemenin çok iddia ettiği nadir hâl."),
  J("وَاللَّهُ يَدْعُو إِلَى دَارِ السَّلَامِ",
    "وَأُخْتَاهُ فِي النَّوْعِ: الِاخْتِصَارُ الْمُجَرَّدُ مَعَ الْقَرِينَةِ، وَرِعَايَةُ الْفَاصِلَةِ.",
    "Its two sisters in kind, kept in the note: mere brevity where a qarina stands (أَصْغَيْتُ إِلَيْهِ — the ear goes unsaid; أَرِنِي — the second object ذَاتَكَ unsaid), and the fasila — which the next aya shows.",
    "Türdeşi iki kardeşi (notta saklı): karîne varken salt kısaltma (أَصْغَيْتُ إِلَيْهِ — kulak söylenmez; أَرِنِي — ikinci mef'ûl ذَاتَكَ söylenmez), ve fâsıla — onu da sonraki âyet gösterir.")]})

# ---------------------------------------------------------------- s4 — Duha 3
S.append({"id": "s4", "translation": {
 "en": "Your Lord has not forsaken you, nor does He hate. (al-Duha 93:3 — the kaf of قَلَاكَ dropped for the FASILA: the sura's verses end on the same letter.)",
 "tr": "Rabbin seni terk etmedi ve darılmadı. (Duhâ 93:3 — قَلَاكَ'nın kâfı FÂSILA için hazfedilmiş: sûrenin âyet sonları aynı harfte biter.)"},
 "tokens": [
  tok("مَا","ma-nafiya","part",["anwa-ma"],
      "نَافِيَةٌ.",
      "«not» — plain negation over the madi.",
      "«-medi» — mâzî üzerinde nefiy."),
  tok("وَدَّعَكَ","waddaa","verb",[],
      "فِعْلٌ مَاضٍ وَ«كَ» مَفْعُولُهُ — مَذْكُورٌ.",
      "«forsaken YOU» — Form II of و د ع, and its object kaf is SPOKEN: hold this against its twin at the verse's end.",
      "«SENİ terk etmedi» — و د ع'nin II. bâbı; mef'ûl kâfı SÖYLENMİŞTİR: bunu âyet sonundaki ikiziyle karşılaştır.",
      segments=[seg("وَدَّعَ","waddaa","verb"), seg("كَ","pron-2ms","pron")]),
  tok("رَبُّكَ","rabb","noun",["tarif-bil-idafa"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ إِلَى الْكَافِ.",
      "«your Lord» — the fa'il, made definite by the kaf of the addressed.",
      "«Rabbin» — fâil; muhatabın kâfıyla marife.",
      segments=[seg("رَبُّ","rabb","noun"), seg("كَ","pron-2ms","pron")]),
  tok("وَمَا","ma-nafiya","part",["anwa-ma","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ وَ«مَا» نَافِيَةٌ.",
      "«nor» — the joined second negation.",
      "«ve … -madı» — atfedilmiş ikinci nefiy.",
      segments=[seg("وَ","wa","part"), seg("مَا","ma-nafiya","part")]),
  tok("قَلَى","qalaa","verb",["hadhf-al-maful"],
      "فِعْلٌ مَاضٍ — وَمَفْعُولُهُ «كَ» مَحْذُوفٌ رِعَايَةً لِلْفَاصِلَةِ.",
      "«nor does He hate [you]» — and the kaf is GONE. Not for generality this time: for the FASILA, the rhyme the sura's verses close on (سَجَى، قَلَى، فَتَرْضَى…). قَلَاكَ would break the cadence; the ear supplies the object from وَدَّعَكَ beside it. Orthography note: قَلَى's alif is the ya-naqis third radical — the same shape as هَدَى.",
      "«ve darılmadı [sana]» — kâf GİTMİŞ. Bu kez umum için değil: FÂSILA için — sûrenin âyet sonlarının kapandığı seci (سَجَى، قَلَى، فَتَرْضَى…). قَلَاكَ âhengi bozardı; kulak, mef'ûlü yanındaki وَدَّعَكَ'den tamamlar. İmlâ notu: قَلَى'nın elifi, yâ-nâkıs üçüncü asıl harftir — هَدَى ile aynı kalıp.",
      punct=".")],
 "jumal": [
  J("مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَى",
    "الْوَجْهُ الرَّابِعُ: حَذْفُ الْمَفْعُولِ رِعَايَةً لِلْفَاصِلَةِ.",
    "WAJH 4 — the FASILA: one verse, the object spoken in its first verb and dropped from its second, and the only difference is the rhyme. The pair is the cleanest minimal contrast the bab owns — nothing else changed.",
    "4. VECİH — FÂSILA: tek âyet; mef'ûl ilk fiilde söylenmiş, ikincisinden düşürülmüş ve tek fark kafiyedir. Çift, bâbın sahip olduğu en temiz asgarî karşıtlıktır — başka hiçbir şey değişmemiştir."),
  J("مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَى",
    "وَمِنْ إِخْوَتِهِ: الْحَذْفُ لِلِاسْتِهْجَانِ — «مَا رَأَيْتُ مِنْهُ وَلَا رَأَى مِنِّي».",
    "And its remaining brothers, carried in the note: the mustahjan drop (Aisha's «I saw not from him, nor he from me» — the object unfit to speak), and concealment — dropping so the object CAN be denied at need. Eight wujuh in all; the chapter walks five in real text.",
    "Ve kalan kardeşleri (notta): müstehcen hazfi (Âişe vâlidemizin «ben ondan görmedim, o da benden» sözü — söylenmesi çirkin mef'ûl), ve gizleme — gerektiğinde İNKÂR edilebilsin diye düşürmek. Toplam sekiz vecih; bâb beşini gerçek metinde yürütür.")]})

# ---------------------------------------------------------------- s5 — Fatiha 4
S.append({"id": "s5", "translation": {
 "en": "You alone we worship, and You alone we ask for help. (al-Fatiha 1:4 — the object FRONTED before its verb: takhsis, worship confined to Him.)",
 "tr": "Yalnız Sana ibadet eder ve yalnız Senden yardım isteriz. (Fâtiha 1:4 — mef'ûl fiilinin ÖNÜNE alınmış: tahsis, ibadet O'na hasredilmiş.)"},
 "tokens": [
  tok("إِيَّاكَ","iyyaka","pron",["hadhf-al-maful","taqdim-al-musnad"],
      "ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَفْعُولٌ بِهِ مُقَدَّمٌ لِلتَّخْصِيصِ.",
      "«You alone» — the detached NASB pronoun (its case is its very spelling: iyya exists for nothing else), standing as the object FRONTED. The order is the meaning: نَعْبُدُكَ says «we worship You»; إِيَّاكَ نَعْبُدُ says «You and none other do we worship». Most fronting restricts — the aksariyya rule — and this is its throne verse.",
      "«yalnız Sana» — munfasıl NASB zamiri (hâli imlâsının kendisidir: iyyâ başka hiçbir şey için yoktur); ÖNE alınmış mef'ûl. Sıra mânâdır: نَعْبُدُكَ «Sana ibadet ederiz» der; إِيَّاكَ نَعْبُدُ «Senden başkasına değil, yalnız Sana ibadet ederiz» der. Takdimin çoğu hasreder — ekseriyet kuralı — ve bu, onun taht âyetidir."),
  tok("نَعْبُدُ","abada","verb",[],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ «نَحْنُ» مُسْتَتِرٌ.",
      "«we worship» — the verb arriving AFTER its object, its «we» concealed within.",
      "«ibadet ederiz» — mef'ûlünden SONRA gelen fiil; «biz»i içinde gizli."),
  tok("وَإِيَّاكَ","iyyaka","pron",["hadhf-al-maful","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَالضَّمِيرُ مَفْعُولٌ مُقَدَّمٌ ثَانٍ.",
      "«and You alone» — the frame repeated whole: the waw joins two VERBAL clauses, each with its object fronted. (Not a hal waw — the iyya family opens a verbal clause, never the nominal clause a hal needs.)",
      "«ve yalnız Senden» — çatı bütünüyle tekrarlanır: vâv, her biri mef'ûlü öne alınmış iki FİİL cümlesini bağlar. (Hâl vâvı değil — iyyâ ailesi fiil cümlesi açar; hâlin istediği isim cümlesini asla.)",
      segments=[seg("وَ","wa","part"), seg("إِيَّاكَ","iyyaka","pron")]),
  tok("نَسْتَعِينُ","istaana","verb",[],
      "فِعْلٌ مُضَارِعٌ — أَجْوَفُ مِنَ الِاسْتِفْعَالِ، أَصْلُهُ نَسْتَعْوِنُ.",
      "«we ask for help» — Form X of ع و ن, hollow: the waw melted to a ya-sound alif in the mazi (اِسْتَعَانَ) and stands as a ya here — the i'lal of أَقَالَ/اِسْتَقَالَ. Repeating إِيَّاكَ rather than saying وَنَسْتَعِينُ keeps the takhsis on BOTH acts.",
      "«yardım isteriz» — ع و ن'un X. bâbı; ecvef: vâv, mâzîde elife eridi (اِسْتَعَانَ), burada yâ olarak durur — أَقَالَ/اِسْتَقَالَ i'lâli. وَنَسْتَعِينُ demek yerine إِيَّاكَ'yi tekrarlamak, tahsisi İKİ fiil üzerinde de tutar.",
      punct=".")],
 "jumal": [
  J("إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
    "الْوَجْهُ الْخَامِسُ: تَقْدِيمُ الْمَفْعُولِ لِلتَّخْصِيصِ — وَالْأَكْثَرِيَّةُ: أَكْثَرُ التَّقْدِيمِ لِلتَّخْصِيصِ لَا كُلُّهُ.",
    "WAJH 5 — TAQDIM of the object: worship and help-seeking confined to Him alone. And the honest rule rides with it: MOST fronting restricts, not all — some is mere care, blessing or savour (بِسْمِ اللهِ… أَقْرَأُ, the basmala's deferred verb), which is why the books argue the case verse by verse.",
    "5. VECİH — mef'ûlün TAKDİMİ: ibadet ve istiâne yalnız O'na hasredilmiş. Dürüst kural da yanında: takdimin ÇOĞU hasreder, hepsi değil — kimi salt ihtimam, teberrük yahut istilzâzdır (بِسْمِ اللهِ… أَقْرَأُ, besmelenin sona bırakılmış fiili); kitapların dâvâyı âyet âyet tartışması bundandır."),
  J("إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
    "وَحَدُّ الدَّعْوَى: «مَا زَيْدًا ضَرَبْتُ وَلَا غَيْرَهُ» لَا يُقَالُ — لِأَنَّ التَّقْدِيمَ يُثْبِتُ الْوُقُوعَ.",
    "And the claim's edge, kept exact: مَا زَيْدًا ضَرَبْتُ means «it was not ZAYD I struck» — the striking itself stands. So «wa-la ghayrahu» after it is a contradiction, and the books REFUSE the sentence. A fronting that denies must deny the choice of object, never the act — the doctrine's own boundary, taught as a boundary.",
    "Ve iddianın sınırı, tam hâliyle: مَا زَيْدًا ضَرَبْتُ «dövdüğüm ZEYD değildi» demektir — dövmenin kendisi ayaktadır. O hâlde ardından «وَلَا غَيْرَهُ» çelişkidir ve kitaplar cümleyi REDDEDER. Nefyeden bir takdim, fiili değil mef'ûl seçimini nefyeder — doktrinin kendi sınırı, sınır olarak öğretilmiş.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # copies — a lex key is GLOBAL: entries copied verbatim from their home package
 "hal-istifham": copy_gloss("jumal-al-tadrib", "hal-istifham"),
 "alima":        copy_gloss("wasiyyat-abi-hanifa-samti", "alima"),
 "shaa":         copy_gloss("wasiyyat-abi-hanifa-samti", "shaa"),
 "salam":        copy_gloss("kitab-al-sulh", "salam"),
 "waddaa":       copy_gloss("wasiyyat-abi-hanifa", "waddaa"),
 # NEW this chapter
 "istawa":  g("اِسْتَوَى", "س و ي", "verb", "to be equal, level (Form VIII)", "eşit olmak, bir olmak (VIII. bâb)", 4, form="VIII"),
 "hada":    g("هَدَى", "ه د ي", "verb", "to guide", "hidayet etmek, yol göstermek", 2),
 "qalaa":   g("قَلَى", "ق ل ي", "verb", "to hate, to forsake", "darılmak, buğzetmek", 4),
 "istaana": g("اِسْتَعَانَ", "ع و ن", "verb", "to seek help (Form X)", "yardım istemek (X. bâb)", 3, form="X"),
 "ajmain":  g("أَجْمَعُونَ", "ج م ع", "noun", "all together (ma'nawi tawkid; nasb/jarr أَجْمَعِينَ)", "hepsi, topluca (mânevî te'kid; nasb/cer: أَجْمَعِينَ)", 4),
}

def build_morph():
    """اِسْتَوَى (VIII, naqis), هَدَى and قَلَى (I daraba, ya-naqis on the جَزَى
    model), اِسْتَعَانَ (X, hollow waw on the أَثَارَ/اِسْتَقَالَ model); عَلِمَ,
    شَاءَ and وَدَّعَ copied from their home packages after the lemma check."""
    out = {}
    for pkg, lex in [("wasiyyat-abi-hanifa-samti", "alima"),
                     ("wasiyyat-abi-hanifa-samti", "shaa"),
                     ("wasiyyat-abi-hanifa", "waddaa")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    out["hada"] = _sg.naqis1(
        "daraba", "نَاقِصٌ يَائِيٌّ", "y", "هَدَ", "هْد", "i", "اِهْد",
        "هُدًى", "هَادٍ", "مَهْدِيّ", "هُدِيَ", "يُهْدَى")
    out["qalaa"] = _sg.naqis1(
        "daraba", "نَاقِصٌ يَائِيٌّ", "y", "قَلَ", "قْل", "i", "اِقْل",
        "قِلًى", "قَالٍ")
    out["istawa"] = _sg.derived_naqis(
        _sg.B8 + " — نَاقِصٌ", _sg.W8, "َ", "اِسْتَوَ", "سْتَو", "i", "اِسْتَو",
        "اِسْتِوَاء", "مُسْتَوٍ")
    out["istaana"] = _sg.idgham(_sg.derived_hollow(
        _sg.B10 + " — أَجْوَفُ وَاوِيٌّ", _sg.W10, "َ",
        "اِسْتَعَان", "اِسْتَعَن", "سْتَعِين", "سْتَعِن", "اِسْتَعِين", "اِسْتَعِن",
        "اِسْتِعَانَة", "مُسْتَعِين", maful="مُسْتَعَان",
        pmz="اُسْتُعِينَ", pmd="يُسْتَعَانُ",
        note="أَجْوَفُ وَاوِيٌّ مِنَ الِاسْتِفْعَالِ عَلَى مِثَالِ اِسْتَقَالَ."))
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/20.json").write_text(
    json.dumps({"chapter": 20, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 20 for c in man["chapters"]):
    man["chapters"].append({"n": 20, "title": TITLE20})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.20.0"
ADD_EN = (" Chapter 20 opens the mutaallaqat bab from the same file (lines ~1620-1700, sahifa 55-59): "
          "al-Zumar 39:9, al-An'am 6:149, Yunus 10:25, al-Duha 93:3 and al-Fatiha 1:4 — all received "
          "Qur'anic text quoted exactly, each cited by the source for the doctrine taught on it; the "
          "Buhturi, Abu Yaqub and Aisha witnesses are carried in the note and jumal rows, not as tokens.")
ADD_TR = (" Yirminci bâb, müteallakāt bâbını aynı dosyadan açar (satır ~1620-1700, sahife 55-59): "
          "Zümer 39:9, En'âm 6:149, Yûnus 10:25, Duhâ 93:3 ve Fâtiha 1:4 — hepsi aynen alınmış mervî "
          "Kur'ân metnidir; her biri, üzerinde öğretilen doktrin için kaynağın kendisince zikredilir. "
          "Buhtürî, Ebû Ya'kūb ve Âişe şahitleri token olarak değil, not ve cümle satırlarında taşınır.")
if "1620-1700" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch20:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
