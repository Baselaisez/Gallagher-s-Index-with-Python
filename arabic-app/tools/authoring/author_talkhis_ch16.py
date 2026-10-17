# -*- coding: utf-8 -*-
"""Author chapter 16 of talkhis-al-miftah — ذِكْرُ الْمُسْنَدِ وَكَوْنُهُ فِعْلًا أَوِ اسْمًا وَتَقْيِيدُهُ.

Chapter 15 opened the musnad's bab with its omission; this chapter walks the
musnad SAID, and the three questions the musannif asks of a said musnad:

  • FI'L or ISM? — الْفِعْلُ لِلتَّجَدُّدِ وَالِاسْمُ لِلثُّبُوتِ. Tarif b. Tamim's
    يَتَوَسَّمُ (the scout examines him anew with every arriving tribe —
    renewal, and time-binding by the shortest route) against Juwayya
    b. al-Nadr's وَهْوَ مُنْطَلِقٌ (the minted dirham never STAYS — an ism,
    because the leaving is a settled quality of the coin).
  • BOUND by the maf'ul family? — every qayd multiplies the news: ضَرَبَ
    زَيْدٌ says only that Zayd struck; the matn's own ladder adds whom, when,
    where, and how. And in كَانَ زَيْدٌ مُنْطَلِقًا it is كَانَ that binds
    (muqayyid) and the khabar that is bound (muqayyad).
  • BOUND by shart? — إِنْ for what is doubtful or rare, إِذَا for what is
    certain — and al-A'raf 131 carries BOTH in one aya: إِذَا + the definite
    الْحَسَنَة + a mazi (good comes, certainly and generally), إِنْ + the
    indefinite سَيِّئَة + a mudari (evil strikes rarely).

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1358-1408 (sahifa
47-49): Tarif b. Tamim's bayt, Juwayya b. al-Nadr's bayt, the matn's frames
ضَرَبَ زَيْدٌ عَمْرًا… and كَانَ زَيْدٌ مُنْطَلِقًا, and al-A'raf 7:131. The ayat
and the abyat are received text quoted exactly; the Ottoman print's
plain-alif spellings are restored to standard orthography.

Grammar this chapter is chosen to teach:
  • note 118 `tajaddud-wa-thubut` — fi'l vs ism in the musnad, the taqyid
    ladder, and the in/idha doctrine with its five nukta-driven exceptions.
  • the engine work the probe forced: the sukun-nun split for إِنْ and
    لَكِنْ, the fuja'iyya generalized, أَوَكُلَّمَا's hamza riding over the
    joining waw (with the fatha guard the bank demanded), إِلَيَّ's merged
    ya, the wasl-vowelled enclitics (جَاءَتْهُمُ), the Form V assimilation
    unfold (يَطَّيَّرُوا), the geminate under the opened ta marbuta
    (صُرَّتَنَا), the radical-sin and nounish guards on the future-sin peel,
    and the glossary outranking every hedged rules-root.
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

TITLE16 = {"ar": "ذِكْرُ الْمُسْنَدِ: فِعْلًا لِلتَّجَدُّدِ وَاسْمًا لِلثُّبُوتِ، وَتَقْيِيدُهُ",
           "en": "The Musnad Said: a Verb for Renewal, a Noun for Permanence — and Its Binding",
           "tr": "Müsnedin Zikri: Teceddüt İçin Fiil, Sübût İçin İsim — ve Kayıtlanması"}

# ---------------------------------------------------------------- s1 — Tarif b. Tamim
S.append({"id": "s1", "translation": {
 "en": "And is it that every time a tribe arrived at ʿUkaz, they sent me their discerner — examining me anew? (Tarif b. Tamim; the musnad يَتَوَسَّمُ is a VERB, for renewal.)",
 "tr": "Her ne zaman Ukâz'a bir kabile gelse, en bilgilisini — beni yeniden inceleyip dururken — bana mı gönderirler? (Tarîf b. Temîm; müsned olan يَتَوَسَّمُ FİİLdir, teceddüt için.)"},
 "tokens": [
  tok("أَوَكُلَّمَا","kullama","part",["tajaddud-wa-thubut","maful-fih"],
      "الْهَمْزَةُ لِلاسْتِفْهَامِ، وَالْوَاوُ عَاطِفَةٌ، وَ«كُلَّمَا» ظَرْفُ تَكْرَارٍ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "Three pieces fused: the interrogative hamza riding OVER the joining waw, and كُلَّمَا — the zarf of REPETITION carrying a shart's sense: «every single time…». Repetition is this bayt's whole engine: the poet is famous enough that the examining happens again with every arriving tribe — and that repeated happening is exactly what will demand a VERB for its musnad.",
      "Kaynaşmış üç parça: atıf vâvının ÜZERİNE binmiş istifhâm hemzesi ve كُلَّمَا — şart mânâsı yüklü TEKRAR zarfı: «her ne zaman…». Tekrar, bu beytin bütün motorudur: şair o kadar meşhurdur ki inceleme her gelen kabileyle yeniden olur — ve bu tekrarlanan oluş, müsnedi için tam da bir FİİL isteyecektir.",
      segments=[seg("أَ","hamza-istifham","part"), seg("وَ","wa","part"), seg("كُلَّمَا","kullama","part")]),
  tok("وَرَدَتْ","warada","verb",["fail","in-shartiyya"],
      "فِعْلُ الشَّرْطِ، مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَفَاعِلُهُ «قَبِيلَةٌ» الْآتِي.",
      "«arrived» — the shart verb of كُلَّمَا (which takes only a MAZI), the ta marking its feminine doer, who is still to come: the sentence runs verb–object–subject.",
      "«geldi» — كُلَّمَا'nın şart fiili (yalnız MÂZÎ alır); tâ, henüz gelmemiş müennes fâilini işaretler: cümle fiil–mef'ûl–fâil dizilir."),
  tok("عُكَاظَ","ukaz","propn",["maful-bihi","mamnu-min-sarf"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "ʿUkaz — the great fair of the Jahiliyya, where the tribes met and the poets were judged. The object of the arriving, and a proper name BARRED from tanwin: no tanwin ever, and a fatha where others take kasra.",
      "Ukâz — câhiliyyenin büyük panayırı; kabilelerin buluştuğu, şairlerin tartıldığı yer. Gelmenin mef'ûlü; ve tenvinden MEN EDİLMİŞ bir özel ad: asla tenvin almaz, başkalarının kesra aldığı yerde fetha alır."),
  tok("قَبِيلَةٌ","qabila-n","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ.",
      "«a tribe» — the delayed doer, indefinite: ANY tribe, which is what lets كُلَّمَا mean every one of them.",
      "«bir kabile» — geciktirilmiş fâil, nekre: HERHANGİ bir kabile — كُلَّمَا'nın «her biri» diyebilmesi bundandır."),
  tok("بَعَثُوا","baatha","verb",["fail"],
      "جَوَابُ الشَّرْطِ، مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.",
      "«they sent» — the jawab, a mazi on the damma of the group's waw; the alif after it is silent spelling.",
      "«gönderdiler» — cevap; cemâat vâvı için zamme üzere mebnî mâzî. Ardındaki elif okunmayan imlâdır.",
      segments=[seg("بَعَثُوا","baatha","verb")]),
  tok("إِلَيَّ","ila","part",["huruf-jarr","ya-al-mutakallim"],
      "جَارٌّ وَمَجْرُورٌ — «إِلَى» وَيَاءُ الْمُتَكَلِّمِ مُدْغَمَتَانِ فِي يَاءٍ وَاحِدَةٍ مُشَدَّدَةٍ.",
      "«to ME» — one written ya where two words meet: the maqsura of إِلَى turns ya before its pronoun, and the speaker's own ya then merges with it under the shadda. The bare skeleton cannot see the seam; the shadda is its receipt.",
      "«BANA» — iki kelimenin buluştuğu yerde tek yazılı yâ: إِلَى'nın maksûresi zamirinden önce yâya döner, konuşanın kendi yâsı da şedde altında onunla kaynaşır. Çıplak iskelet dikişi göremez; şedde onun makbuzudur.",
      segments=[seg("إِلَى","ila","prep"), seg("يَ","pron-1s","pron")]),
  tok("عَرِيفَهُمْ","arif","noun",["maful-bihi","sighat-mubalagha","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«هُمْ» مُضَافٌ إِلَيْهِ — وَ«عَرِيف» مُبَالَغَةُ عَارِفٍ.",
      "«their DISCERNER» — the object of the sending, mudaf to their pronoun. عَرِيف is فَعِيل in the intensive office: not one who merely knows but the tribe's professional knower — the one they trust to identify a famous face.",
      "«en BİLGİLİLERİNİ» — göndermenin mef'ûlü; zamirlerine muzâf. عَرِيف, mübâlağa makāmında فَعِيل'dir: sıradan bilen değil, kabilenin işi bilmek olan adamı — meşhur bir yüzü teşhis etmesine güvendikleri kişi.",
      segments=[seg("عَرِيفَ","arif","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("يَتَوَسَّمُ","tawassama","verb",["tajaddud-wa-thubut","form-v-verbs","hal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ حَالٌ — وَهُوَ الْمُسْنَدُ الَّذِي جَاءَ فِعْلًا لِلتَّجَدُّدِ مَعَ التَّقْيِيدِ بِأَخَصَرِ طَرِيقٍ.",
      "«examining anew» — the bayt's teaching word. Form V of و س م: to search a face for its marks, again and again. The musannif's rule: a musnad comes as a VERB to say TAJADDUD — the act renews, happens afresh with every tribe — while binding itself to a time by the SHORTEST route, for a verb carries its tense in its own letters, no extra word spent. Say مُتَوَسِّمٌ instead and the examining freezes into a standing quality; the bayt's whole complaint — that it keeps happening — dies.",
      "«inceleyip duruyor» — beytin ders kelimesi. و س م'nin V. bâbı: bir yüzde alâmet aramak, tekrar tekrar. Musannifin kuralı: müsned, TECEDDÜT söylemek için FİİL gelir — iş yenilenir, her kabileyle yeniden olur — ve kendini EN KISA yoldan bir zamana bağlar; çünkü fiil, zamanını kendi harflerinde taşır, fazladan kelime harcanmaz. Yerine مُتَوَسِّمٌ de: inceleme donup yerleşik bir vasfa döner; beytin bütün şikâyeti — bunun hep olduğu — ölür.",
      punct="؟")],
 "jumal": [
  J("أَوَكُلَّمَا وَرَدَتْ عُكَاظَ قَبِيلَةٌ بَعَثُوا إِلَيَّ عَرِيفَهُمْ يَتَوَسَّمُ",
    "الْمُسْنَدُ فِعْلٌ — لِإِفَادَةِ التَّجَدُّدِ وَالتَّقْيِيدِ بِأَحَدِ الْأَزْمِنَةِ الثَّلَاثَةِ عَلَى أَخْصَرِ وَجْهٍ.",
    "The musnad as a VERB: renewal — the examining happens afresh each time — and time-binding by the shortest route, the tense riding in the verb's own letters.",
    "Müsned FİİL: teceddüt — inceleme her seferinde yeniden olur — ve en kısa yoldan zamana bağlanış; zaman, fiilin kendi harflerinde taşınır.")]})

# ---------------------------------------------------------------- s2 — Juwayya b. al-Nadr
S.append({"id": "s2", "translation": {
 "en": "The minted dirham never befriends our purse — it only passes over it, and it is GONE. (Juwayya b. al-Nadr; the musnad مُنْطَلِقٌ is an ISM, for permanence.)",
 "tr": "Basılı para bizim keseye alışmaz — ona yalnız uğrar, ve o hep GİDİCİDİR. (Cüveyye b. en-Nadr; müsned olan مُنْطَلِقٌ İSİMdir, sübût için.)"},
 "tokens": [
  tok("لَا","la-nafiya","part",[],
      "حَرْفُ نَفْيٍ.",
      "The negation over the mudari.",
      "Muzâri üzerindeki nefiy."),
  tok("يَأْلَفُ","alifa","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِنْ أَلِفَ يَأْلَفُ: مَهْمُوزُ الْفَاءِ مِنْ بَابِ سَمِعَ.",
      "«never befriends» — أَلِفَ, to grow familiar with, bab سَمِعَ, its first radical a hamza. Generosity in a poet's boast: money never stays long enough to make friends.",
      "«alışmaz» — أَلِفَ: ünsiyet etmek; سَمِعَ bâbından, ilk kök harfi hemze. Şair övüncünde cömertlik: para, dostluk kuracak kadar kalmaz."),
  tok("الدِّرْهَمُ","dirham","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«the dirham» — the doer, generic by its article: coin as such.",
      "«dirhem» — fâil; harf-i tarifi cins içindir: para olarak para."),
  tok("الْمَضْرُوبُ","madrub","noun",["naat-sifa","ism-maful"],
      "صِفَةٌ مَرْفُوعَةٌ — اسْمُ مَفْعُولٍ: الْمَسْكُوكُ.",
      "«the MINTED» — sifa of the dirham, ism maf'ul of ضَرَبَ in its coining sense: struck at the mint. The same root this chapter conjugates in its next sentence — one verb, two trades.",
      "«BASILI» — dirhemin sıfatı; ضَرَبَ'nin sikke mânâsında ism-i mef'ûlü: darphânede basılmış. Bu bâbın bir sonraki cümlede çekeceği kökün ta kendisi — tek fiil, iki zanaat.",
      segments=[seg("الْمَضْرُوبُ","madrub","noun")]),
  tok("صُرَّتَنَا","surra","noun",["maful-bihi","doubled-verbs","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ — وَتَاءُ صُرَّةٍ الْمَرْبُوطَةُ انْفَتَحَتْ لِلْإِضَافَةِ.",
      "«our PURSE» — the object of the befriending; صُرَّة, the tied money-pouch, its ta marbuta opening into a plain ta before the pronoun. A geminate root — ص ر ر, the tying — with the shadda holding the doubled letter the skeleton alone would lose.",
      "«KESEmizi» — alışmanın mef'ûlü; صُرَّة: ağzı bağlı para kesesi; tâ-i merbûtası zamirden önce düz tâya açılır. Muzâaf kök — ص ر ر, bağlamak — iskeletin tek başına yitireceği çift harfi şedde tutar.",
      segments=[seg("صُرَّتَ","surra","noun"), seg("نَا","pron-1p","pron")]),
  tok("لَكِنْ","lakin","part",["tajaddud-wa-thubut"],
      "حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ — لَا عَمَلَ لَهُ، وَالنُّونُ سَاكِنَةٌ.",
      "«but» — the LIGHT lakin, its nun on sukun: pure istidrak, governing nothing. Only the doubled لَكِنَّ joins the inna family; what follows here keeps its own i'rab.",
      "«fakat» — HAFİF lâkin; nûnu sükûnlu: sırf istidrâk, hiçbir şeyi amel etmez. İnne ailesine yalnız şeddeli لَكِنَّ girer; buradan sonrası kendi i'râbını korur."),
  tok("يَمُرُّ","marra","verb",["mudari-marfu","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِنَ الْمُضَاعَفِ: مَرَّ يَمُرُّ.",
      "«it passes» — the geminate مَرَّ, its twin letters fused under the shadda. Still a verb, still renewal: each coin passes once.",
      "«uğrar» — muzâaf مَرَّ; ikiz harfleri şedde altında kaynaşmış. Hâlâ fiil, hâlâ teceddüt: her sikke bir kez uğrar.",
      segments=[seg("يَمُرُّ","marra","verb")]),
  tok("عَلَيْهَا","ala","part",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَمُرُّ» — وَالضَّمِيرُ لِلصُّرَّةِ.",
      "«over it» — hanging on the passing; the pronoun is the purse.",
      "«onun üzerinden» — geçmeye bağlanır; zamir kesedir.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هَا","pron-3fs","pron")]),
  tok("وَهْوَ","huwa","pron",["mubtada-khabar","anwa-al-waw","tajaddud-wa-thubut"],
      "الْوَاوُ لِلْحَالِ، وَ«هُوَ» مُبْتَدَأٌ — أُسْكِنَتْ هَاؤُهُ بَعْدَ الْوَاوِ تَخْفِيفًا.",
      "«while IT—» — the waw of circumstance opening a nominal sentence; هُوَ its mubtada, the ha resting on a sukun after the waw (a licensed lightening: وَهْوَ for وَهُوَ). The nominal frame is the point: the bayt shifts from what the coin DOES to what the coin IS.",
      "«hâlbuki O—» — hâl vâvı bir isim cümlesi açar; هُوَ mübtedâsıdır, hâsı vâvdan sonra hafiflik için sükûnlanmıştır (ruhsatlı tahfif: وَهُوَ yerine وَهْوَ). İsim çatısı işin özüdür: beyit, sikkenin YAPTIĞINDAN sikkenin OLDUĞUNA geçer.",
      segments=[seg("وَ","wa","part"), seg("هْوَ","huwa","pron")]),
  tok("مُنْطَلِقٌ","muntaliq","noun",["tajaddud-wa-thubut","mubtada-khabar","ism-fail","form-vii-verbs"],
      "خَبَرٌ مَرْفُوعٌ — وَهُوَ الْمُسْنَدُ الَّذِي جَاءَ اسْمًا لِإِفَادَةِ الثُّبُوتِ وَالدَّوَامِ.",
      "«GONE» — the teaching word of the second bayt, and chapter 15's مُنْطَلِقٌ returned with its office changed. The musnad comes as an ISM to say THUBUT: leaving is not something this coin happens to do, it is what the coin IS — a settled, durable quality, unbound to any tense. Say يَنْطَلِقُ instead and it becomes one more event; the ism is what makes the poet's poverty a permanent boast.",
      "«GİDİCİ» — ikinci beytin ders kelimesi; 15. bâbın مُنْطَلِقٌ'u vazifesi değişmiş olarak döndü. Müsned, SÜBÛT söylemek için İSİM gelir: gitmek bu sikkenin ara sıra yaptığı bir şey değil, OLDUĞU şeydir — yerleşik, kalıcı, hiçbir zamana bağlı olmayan bir vasıf. Yerine يَنْطَلِقُ de: bir olaya daha döner; şairin fakrini kalıcı bir övünç yapan, isimdir.",
      punct=".")],
 "jumal": [
  J("لَا يَأْلَفُ الدِّرْهَمُ الْمَضْرُوبُ صُرَّتَنَا — وَهْوَ مُنْطَلِقٌ",
    "الْمُسْنَدُ اسْمٌ — لِإِفَادَةِ الثُّبُوتِ وَالدَّوَامِ مِنْ غَيْرِ تَقْيِيدٍ بِزَمَانٍ.",
    "The musnad as an ISM: permanence — the coin's leaving is what it IS, bound to no tense — set against the verbs around it.",
    "Müsned İSİM: sübût — sikkenin gidiciliği, hiçbir zamana bağlı olmadan, OLDUĞU şeydir — çevresindeki fiillerin karşısına dikilmiş.")]})

# ---------------------------------------------------------------- s3 — the taqyid ladder
S.append({"id": "s3", "translation": {
 "en": "Zayd struck ʿAmr — on Friday, before the commander, a severe striking. (The matn's own ladder: every added qayd multiplies the news.)",
 "tr": "Zeyd Amr'ı dövdü — cuma günü, emîrin önünde, şiddetli bir dövüşle. (Metnin kendi merdiveni: eklenen her kayıt haberi çoğaltır.)"},
 "tokens": [
  tok("ضَرَبَ","daraba","verb",["fail","tajaddud-wa-thubut"],
      "فِعْلٌ مَاضٍ — الْمُسْنَدُ، وَكُلُّ مَا بَعْدَ فَاعِلِهِ قُيُودٌ تُرَبِّي الْفَائِدَةَ.",
      "«struck» — the Emsile's own first verb, standing as the musnad. Alone with its doer it reports one bare fact; the musannif's word for what the coming words do to it is تَرْبِيَةُ الْفَائِدَةِ — they RAISE the yield, qayd by qayd.",
      "«dövdü» — Emsile'nin kendi ilk fiili, müsned makāmında. Fâiliyle yalnızken tek çıplak vak'a bildirir; musannifin, gelecek kelimelerin ona yaptığına verdiği ad تَرْبِيَةُ الْفَائِدَةِ'dir — kayıt kayıt, verimi BÜYÜTÜRLER."),
  tok("زَيْدٌ","zayd","propn",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "The doer, in raf'. So far: someone struck.",
      "Fâil, merfû. Şimdilik: biri dövdü."),
  tok("عَمْرًا","amr-alam","propn",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَفِي النَّصْبِ تَسْقُطُ وَاوُ عَمْرٍو لِأَنَّ أَلِفَ التَّنْوِينِ تَكْفِي فَرْقًا.",
      "«ʿAmr» — the first qayd: WHOM. And note the spelling lesson: the silent waw that guards عَمْرو from عُمَر in raf' and jarr DROPS in nasb, because the tanwin's alif already tells the two names apart.",
      "«Amr'ı» — ilk kayıt: KİMİ. Ve imlâ dersi: ref' ve cerde عَمْرو'yu عُمَر'den koruyan sessiz vâv, nasbda DÜŞER; çünkü tenvinin elifi iki adı zaten ayırır."),
  tok("يَوْمَ","yawm","noun",["maful-fih","idafa-definiteness"],
      "مَفْعُولٌ فِيهِ — ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«on the day of…» — the second qayd: WHEN. A zarf of time, mudaf to what names the day.",
      "«…gününde» — ikinci kayıt: NE ZAMAN. Zaman zarfı; günü adlandırana muzâf."),
  tok("الْجُمُعَةِ","juma","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«Friday» — the mudaf ilayh closing the time.",
      "«cuma» — zamanı kapatan muzâfun ileyh."),
  tok("أَمَامَ","amama","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«before…» — the third qayd: WHERE. A zarf of place — a NOUN, root أ م م, for all that it works like a preposition.",
      "«…önünde» — üçüncü kayıt: NEREDE. Mekân zarfı — edat gibi işlese de bir İSİMdir; kökü أ م م."),
  tok("الْأَمِيرِ","amir","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the commander» — closing the place, and raising the stakes: a public striking, before authority.",
      "«emîrin» — mekânı kapatır ve bahsi büyütür: alenî bir dövme, otoritenin önünde."),
  tok("ضَرْبًا","darb","noun",["maful-mutlaq"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرُ الْفِعْلِ نَفْسِهِ.",
      "«a striking» — the fourth qayd: the verb's OWN masdar returned to it, the maf'ul mutlaq, here as the peg for the coming HOW.",
      "«bir dövüşle» — dördüncü kayıt: fiilin KENDİ masdarı kendisine dönmüş — mef'ûl-i mutlak; buradaki işi, gelecek NASIL'a askı olmaktır."),
  tok("شَدِيدًا","shadid","noun",["naat-sifa","sifa-mushabbaha"],
      "صِفَةٌ لِلْمَصْدَرِ مَنْصُوبَةٌ — وَبِهَا تَمَّ الْجَوَابُ عَنْ: كَيْفَ.",
      "«severe» — the sifa on the masdar answers HOW, and the ladder is complete: one verb, and the hearer now knows whom, when, where and how. That growth — and nothing mystical — is why a speaker binds the musnad; and the TARK of these qayds has its reasons too: no time, no knowledge, or no wish to tell.",
      "«şiddetli» — masdarın sıfatı NASIL'ı cevaplar ve merdiven tamamlanır: tek fiil; dinleyen artık kimi, ne zaman, nerede ve nasıl olduğunu bilir. Konuşanın müsnedi kayıtlaması bu çoğalış içindir — mistik bir şey değil; ve bu kayıtların TERKİ de sebepsiz değildir: vakit yoktur, bilgi yoktur, yahut söyleme isteği.",
      punct=".")],
 "jumal": [
  J("ضَرَبَ زَيْدٌ عَمْرًا يَوْمَ الْجُمُعَةِ أَمَامَ الْأَمِيرِ ضَرْبًا شَدِيدًا",
    "تَقْيِيدُ الْمُسْنَدِ بِالْمَفْعُولِ وَنَحْوِهِ — لِتَرْبِيَةِ الْفَائِدَةِ.",
    "The musnad bound by the maf'ul family: each qayd multiplies the news — whom, when, where, how — from one bare verb.",
    "Müsned, mef'ûl ailesiyle kayıtlanmış: her kayıt haberi çoğaltır — kimi, ne zaman, nerede, nasıl — tek çıplak fiilden.")]})

# ---------------------------------------------------------------- s4 — kana binds
S.append({"id": "s4", "translation": {
 "en": "Zayd WAS setting out. (It is كَانَ that binds — muqayyid — and the khabar that is bound: the going is tied to past time.)",
 "tr": "Zeyd yola çıkıyorDU. (Kayıtlayan — mukayyid — كَانَ'dir; kayıtlanan haberdir: gidiş, geçmiş zamana bağlanmıştır.)"},
 "tokens": [
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","tajaddud-wa-thubut"],
      "فِعْلٌ مَاضٍ نَاقِصٌ — وَهُوَ الْمُقَيِّدُ: قَيَّدَ الِانْطِلَاقَ بِالزَّمَانِ الْمَاضِي.",
      "«was» — and the matn stops to fix a direction: in كَانَ زَيْدٌ مُنْطَلِقًا it is NOT the khabar that binds kana; كَانَ is the MUQAYYID and the setting-out is the MUQAYYAD — the sister ties Zayd's going to past time. The binder is the incomplete verb; the bound is the news itself.",
      "«idi» — ve metin, bir yönü sabitlemek için durur: كَانَ زَيْدٌ مُنْطَلِقًا'da kana'yı kayıtlayan haber DEĞİLDİR; MUKAYYİD olan كَانَ, MUKAYYED olan ise gidiştir — nâkıs kardeş, Zeyd'in gidişini geçmiş zamana bağlar. Bağlayan nâkıs fiildir; bağlanan haberin kendisidir."),
  tok("زَيْدٌ","zayd","propn",["kana-wa-akhawatuha"],
      "اسْمُ كَانَ مَرْفُوعٌ.",
      "Kana's ism, in raf'.",
      "Kâne'nin ismi, merfû."),
  tok("مُنْطَلِقًا","muntaliq","noun",["kana-wa-akhawatuha","tajaddud-wa-thubut","ism-fail"],
      "خَبَرُ كَانَ مَنْصُوبٌ — وَهُوَ الْمُقَيَّدُ.",
      "«setting out» — kana's khabar in nasb, and the MUQAYYAD: the same ism that carried permanence in the dirham bayt, here handed to a sister that stamps a TENSE on it. The pair of sentences is the chapter in miniature: the ism says what a thing is; kana says when it was so.",
      "«yola çıkan» — kâne'nin mansûb haberi ve MUKAYYED: dirhem beytinde sübût taşıyan aynı isim, burada üzerine ZAMAN damgası vuran bir kardeşe teslim edilmiş. Cümle çifti, bâbın minyatürüdür: isim bir şeyin ne olduğunu söyler; kâne ne zaman öyle olduğunu.",
      punct=".")],
 "jumal": [
  J("كَانَ زَيْدٌ مُنْطَلِقًا",
    "كَانَ مُقَيِّدٌ وَالْخَبَرُ مُقَيَّدٌ — قُيِّدَ الِانْطِلَاقُ بِالزَّمَانِ الْمَاضِي.",
    "Kana is the binder and the khabar the bound: the going is tied to past time.",
    "Kâne kayıtlayan, haber kayıtlanandır: gidiş geçmiş zamana bağlanmıştır.")]})

# ---------------------------------------------------------------- s5 — al-A'raf 131
S.append({"id": "s5", "translation": {
 "en": "So when the good came to them, they said: «this is ours» — and if an evil struck them, they took ill omen from Musa and those with him. (al-A'raf 7:131 — إِذَا with the definite and the mazi for the certain; إِنْ with the indefinite and the mudari for the rare.)",
 "tr": "Onlara iyilik geldiğinde «bu bizimdir» dediler — ve eğer bir kötülük dokunursa, Mûsâ ile beraberindekileri uğursuz sayarlardı. (A'râf 7:131 — kesin olana marife ve mâzî ile إِذَا; nâdir olana nekre ve muzâri ile إِنْ.)"},
 "tokens": [
  tok("فَإِذَا","idha","part",["idha-shartiyya","tajaddud-wa-thubut"],
      "الْفَاءُ عَاطِفَةٌ، وَ«إِذَا» ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ — لِمَا كَانَ وُقُوعُهُ قَطْعِيًّا.",
      "«so WHEN…» — this side of the aya uses إِذَا, the conditional of the CERTAIN: good arriving is treated as a thing that assuredly comes. Watch the two halves of this one aya run the whole doctrine against each other.",
      "«artık …-DIĞINDA» — âyetin bu yakası إِذَا kullanır: KESİN olanın şartı; iyiliğin gelişi, mutlaka gelen bir şey muâmelesi görür. Tek âyetin iki yakasının bütün kāideyi birbirine karşı işlettiğine bak.",
      segments=[seg("فَ","fa","part"), seg("إِذَا","idha","part")]),
  tok("جَاءَتْهُمُ","jaa","verb",["fail","tajaddud-wa-thubut"],
      "فِعْلُ الشَّرْطِ، مَاضٍ، وَ«هُمْ» مَفْعُولٌ بِهِ — حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْمَاضِي مَعَ إِذَا يَدُلُّ عَلَى الْقَطْعِ.",
      "«came to them» — a MAZI with إِذَا, and that pairing is deliberate: the past tense speaks of a thing as done, so it suits what certainly happens. The pronoun's mim takes a helping damma before the article's resting alif — the wasl vowel that let this very word hide from the paradigms until the engine learned to hear it.",
      "«onlara geldi» — إِذَا ile MÂZÎ; ve bu eşleşme kasıtlıdır: geçmiş kipi, işi olup bitmiş gibi söyler; kesin olana bu yakışır. Zamirin mîmi, harf-i tarifin sâkin elifinden önce yardımcı bir damme alır — bu kelimeyi, motor duymayı öğrenene dek paradigmalardan saklayan vasıl harekesi.",
      segments=[seg("جَاءَتْ","jaa","verb"), seg("هُمُ","pron-3mp","pron")]),
  tok("الْحَسَنَةُ","hasana","noun",["fail","tajaddud-wa-thubut"],
      "فَاعِلٌ مَرْفُوعٌ — عُرِّفَ بِلَامِ الْجِنْسِ لِأَنَّ الْمُرَادَ مُطْلَقُ الْحَسَنَةِ.",
      "«THE good» — definite, by the lam of GENUS: good as such, any of it — rain, harvest, ease. Definiteness sits on the certain side of the aya: what surely comes is spoken of as a known thing.",
      "«iyilik» — marife; CİNS lâmıyla: iyilik olarak iyilik, hangisi olursa — yağmur, hasat, bolluk. Marifelik, âyetin kesin yakasında oturur: mutlaka gelen, bilinen bir şey gibi anılır."),
  tok("قَالُوا","qala","verb",["fail"],
      "جَوَابُ إِذَا، مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.",
      "«they said» — the jawab of idha.",
      "«dediler» — izânın cevabı."),
  tok("لَنَا","li","part",["huruf-jarr","mubtada-khabar"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.",
      "«ours» — the fronted khabar of the coming demonstrative: this is FOR US — merit claimed, gratitude refused.",
      "«bizimdir» — gelecek işaretin öne alınmış haberi: bu BİZİM — hak sahiplenildi, şükür reddedildi.",
      segments=[seg("لَ","li","prep"), seg("نَا","pron-1p","pron")]),
  tok("هَذِهِ","hadhihi","pron",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ فِي مَحَلِّ رَفْعٍ.",
      "«this» — the delayed mubtada.",
      "«bu» — geciktirilmiş mübtedâ.",
      punct="،"),
  tok("وَإِنْ","in-shartiyya","part",["in-shartiyya","tajaddud-wa-thubut"],
      "الْوَاوُ عَاطِفَةٌ، وَ«إِنْ» شَرْطِيَّةٌ سَاكِنَةُ النُّونِ — لِمَا كَانَ وُقُوعُهُ نَادِرًا أَوْ مَشْكُوكًا.",
      "«and IF…» — the aya turns to إِنْ, the conditional of the DOUBTFUL and the rare: evil, next to the flood of good, is the exception. The nun's sukun is the whole diagnosis — only the doubled nun would make the inna family.",
      "«ve EĞER…» — âyet إِنْ'e döner: ŞÜPHELİ ve nâdir olanın şartı; kötülük, iyilik selinin yanında istisnâdır. Nûnun sükûnu teşhisin tamamıdır — inne ailesini ancak şeddeli nûn yapardı.",
      segments=[seg("وَ","wa","part"), seg("إِنْ","in-shartiyya","part")]),
  tok("تُصِبْهُمْ","asaba","verb",["in-shartiyya","form-iv-verbs","tajaddud-wa-thubut"],
      "فِعْلُ الشَّرْطِ، مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، وَ«هُمْ» مَفْعُولٌ بِهِ — وَالْمُضَارِعُ مَعَ إِنْ لِعَدَمِ الْقَطْعِ.",
      "«should strike them» — a MUDARI in jazm with إِنْ, and again the pairing teaches: the unfinished tense suits the uncertain event. Form IV of the hollow ص و ب, its middle letter gone in the jussive: أَصَابَ → تُصِبْ.",
      "«dokunursa» — إِنْ ile MECZUM MUZÂRİ; eşleşme yine öğretir: bitmemiş kip, kesin olmayan olaya yakışır. Ecvef ص و ب'un IV. bâbı; cezimde orta harfi düşmüş: أَصَابَ → تُصِبْ.",
      segments=[seg("تُصِبْ","asaba","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("سَيِّئَةٌ","sayyia","noun",["fail","tajaddud-wa-thubut"],
      "فَاعِلٌ مَرْفُوعٌ — نُكِّرَ لِأَنَّ السَّيِّئَةَ بِالنِّسْبَةِ إِلَى الْحَسَنَةِ نَادِرَةٌ.",
      "«an evil» — INDEFINITE, where its sister wore the article: some evil, now and then. The tanwin is the rarity made visible — one aya, and every knob of the doctrine turned to its opposite setting: إِذَا/إِنْ, definite/indefinite, mazi/mudari.",
      "«bir kötülük» — kız kardeşi harf-i tarif giyerken bu NEKRE: ara sıra bir kötülük. Tenvin, nâdirliğin görünür hâlidir — tek âyet; ve kāidenin her düğmesi zıt konuma çevrilmiş: إِذَا/إِنْ, marife/nekre, mâzî/muzâri."),
  tok("يَطَّيَّرُوا","tatayyara","verb",["form-v-verbs","in-shartiyya"],
      "جَوَابُ الشَّرْطِ، مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ — أَصْلُهُ يَتَطَيَّرُوا، أُدْغِمَتِ التَّاءُ فِي الطَّاءِ.",
      "«they took ill omen» — the jawab, jussive by its dropped nun; and underneath, Form V of ط ي ر with its ta SWALLOWED into the ṭa: يَتَطَيَّرُوا spoken as يَطَّيَّرُوا. From the birds (طَيْر) the pagans read for luck — they blamed their rare misfortunes on the Prophet in their midst.",
      "«uğursuz saydılar» — cevap; düşen nûnuyla meczum. Altında, tâsı ṭâya YUTULMUŞ ط ي ر'in V. bâbı: يَتَطَيَّرُوا, söylenişte يَطَّيَّرُوا. Uğur okudukları kuşlardan (طَيْر) — nâdir belâlarını içlerindeki Peygambere yüklediler.",
      segments=[seg("يَطَّيَّرُوا","tatayyara","verb")]),
  tok("بِمُوسَى","musa","propn",["huruf-jarr","ism-maqsur-manqus"],
      "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«from Musa» — the omen's target in jarr, its kasra estimated on the maqsur alif of the name.",
      "«Mûsâ'dan» — uğursuzluğun hedefi; kesrası, adın maksûr elifi üzerinde takdîr edilir.",
      segments=[seg("بِ","bi","prep"), seg("مُوسَى","musa","propn")]),
  tok("وَمَنْ","man-mawsula","pron",["ism-mawsul"],
      "الْوَاوُ عَاطِفَةٌ، وَ«مَنْ» مَوْصُولَةٌ فِي مَحَلِّ جَرٍّ.",
      "«and those who…» — man the relative, joined to Musa under the ba.",
      "«ve …-kilere» — ism-i mevsûl men; bâ altında Mûsâ'ya atfedilmiş.",
      segments=[seg("وَ","wa","part"), seg("مَنْ","man-mawsula","pron")]),
  tok("مَعَهُ","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ صِلَةُ «مَنْ».",
      "«with him» — the zarf مَعَ (a noun, mudaf to the pronoun), standing whole as the sila of man.",
      "«beraberindekileri» — zarf مَعَ (isimdir; zamire muzâf); bütünüyle, مَنْ'in sılası olarak durur.",
      punct=".")],
 "jumal": [
  J("فَإِذَا جَاءَتْهُمُ الْحَسَنَةُ … وَإِنْ تُصِبْهُمْ سَيِّئَةٌ",
    "إِذَا مَعَ الْمُعَرَّفِ وَالْمَاضِي لِلْقَطْعِيِّ، وَإِنْ مَعَ الْمُنَكَّرِ وَالْمُضَارِعِ لِلنَّادِرِ — فِي آيَةٍ وَاحِدَةٍ.",
    "One aya, both settings: إِذَا with the definite and the mazi for what certainly comes; إِنْ with the indefinite and the mudari for what rarely strikes.",
    "Tek âyet, iki ayar: kesin gelene marife ve mâzî ile إِذَا; nâdir dokunana nekre ve muzâri ile إِنْ.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # NEW this chapter
 "kullama":   g("كُلَّمَا", None, "part", "every time that… (zarf of repetition with a shart's sense)", "her ne zaman… (şart mânâlı tekrar zarfı)", 4),
 "hamza-istifham": g("أَ (هَمْزَةُ الاِسْتِفْهَامِ)", None, "part", "the interrogative hamza — is it that…?", "istifhâm hemzesi — …mı?", 3),
 "ukaz":      g("عُكَاظ", None, "propn", "ʿUkaz — the great pre-Islamic fair near Ta'if", "Ukâz — Tâif yakınındaki büyük câhiliye panayırı", 5),
 "qabila-n":  g("قَبِيلَة", "ق ب ل", "noun", "tribe", "kabile", 2, plural="قَبَائِل"),
 "arif":      g("عَرِيف", "ع ر ف", "noun", "the tribe's knower / identifier (intensive of عَارِف)", "arîf — kabilenin tanıma işini bilen adamı (عَارِف'in mübâlağası)", 5),
 "tawassama": g("تَوَسَّمَ", "و س م", "verb", "to scan for marks, examine closely", "alâmet aramak, dikkatle incelemek", 5, form="V"),
 "tatayyara": g("تَطَيَّرَ", "ط ي ر", "verb", "to take ill omen (from the birds)", "uğursuz saymak (kuşlardan fal tutmak)", 5, form="V"),
 "daraba":    g("ضَرَبَ", "ض ر ب", "verb", "to strike; to mint (a coin)", "vurmak, dövmek; (sikke) basmak", 1, form="I"),
 "madrub":    g("مَضْرُوب", "ض ر ب", "noun", "struck; minted (ism maf'ul)", "vurulmuş; basılı (ism-i mef'ûl)", 3),
 "surra":     g("صُرَّة", "ص ر ر", "noun", "money-pouch, purse", "para kesesi", 4, plural="صُرَر"),
 "juma":      g("جُمُعَة", "ج م ع", "noun", "Friday", "cuma", 1),
 "hasana":    g("حَسَنَة", "ح س ن", "noun", "a good thing, good fortune", "iyilik, güzellik", 2, plural="حَسَنَات"),
 "sayyia":    g("سَيِّئَة", "س و أ", "noun", "an evil, a misfortune", "kötülük, fenalık", 2, plural="سَيِّئَات"),
 "musa":      g("مُوسَى", None, "propn", "Musa (the prophet Moses)", "Mûsâ (aleyhisselâm)", 1),
 "man-mawsula": g("مَنْ (الْمَوْصُولَة)", None, "pron", "the one(s) who (relative man)", "o kimse(ler) ki (ism-i mevsûl men)", 3),
 "hadhihi":   g("هَذِهِ", None, "pron", "this (feminine demonstrative)", "bu (müennes ism-i işâret)", 1),
 "ala":       g("عَلَى", None, "part", "on, over", "üzerinde, üzerine", 1),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "warada":    g("وَرَدَ", "و ر د", "verb", "to arrive at, come to (water, a place)", "varmak, gelmek (suya, bir yere)", 3, form="I"),
 "baatha":    g("بَعَثَ", "ب ع ث", "verb", "to send; to raise up", "göndermek; diriltmek", 2, form="I"),
 "alifa":     g("أَلِفَ", "أ ل ف", "verb", "to grow familiar with, befriend", "alışmak, ünsiyet etmek", 4, form="I"),
 "marra":     g("مَرَّ", "م ر ر", "verb", "to pass, pass by", "geçmek, uğramak", 2, form="I"),
 "asaba":     g("أَصَابَ", "ص و ب", "verb", "to strike, befall; to hit the mark", "isâbet etmek, dokunmak", 3, form="IV"),
 "lakin":     g("لَكِنْ", None, "part", "but (light — governs nothing)", "fakat, lâkin (hafif — amel etmez)", 2),
 "amama":     g("أَمَامَ", "أ م م", "noun", "before, in front of (a zarf)", "önünde (zarf)", 2),
 "shadid":    g("شَدِيد", "ش د د", "noun", "severe, intense", "şiddetli", 2),
}

def build_morph():
    """Copies for warada/baatha/alifa/marra/asaba; three new paradigms.

    ضَرَبَ يَضْرِبُ — the Emsile's own model verb, bab ضَرَبَ.
    تَوَسَّمَ / تَطَيَّرَ — Form V sound (the weak letters ي/و stand as
    ordinary consonants throughout Form V), mudari prefix on fatha.
    """
    out = {}
    for pkg, lex in [("mukhtasar-al-manar", "warada"),
                     ("aqaid-ahl-al-sunna", "baatha"),
                     ("wasiyyat-abi-hanifa-samti", "alifa"),
                     ("wasiyyat-abi-hanifa-samti", "marra"),
                     ("wasiyyat-abi-hanifa-samti", "asaba")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    out["daraba"] = _sg.sound1("daraba", "ضَرَب", "ضْرِب", "اِضْرِب", "ضَرْب", "ضَارِب",
                               "مَضْرُوب", "ضُرِبَ", "يُضْرَبُ")
    out["tawassama"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَوَسَّم", "تَوَسَّم", "تَوَسَّم",
                                   "تَوَسُّم", "مُتَوَسِّم",
                                   pmz="تُوُسِّمَ", pmd="يُتَوَسَّمُ")
    out["tatayyara"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَطَيَّر", "تَطَيَّر", "تَطَيَّر",
                                   "تَطَيُّر", "مُتَطَيِّر",
                                   pmz="تُطُيِّرَ", pmd="يُتَطَيَّرُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/16.json").write_text(
    json.dumps({"chapter": 16, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 16 for c in man["chapters"]):
    man["chapters"].append({"n": 16, "title": TITLE16})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.16.0"
ADD_EN = (" Chapter 16 continues from the same file (lines ~1358-1408, sahifa 47-49): Tarif b. Tamim's bayt "
          "أَوَكُلَّمَا وَرَدَتْ عُكَاظَ…, Juwayya b. al-Nadr's bayt لَا يَأْلَفُ الدِّرْهَمُ…, the matn's frames "
          "ضَرَبَ زَيْدٌ عَمْرًا يَوْمَ الْجُمُعَةِ… and كَانَ زَيْدٌ مُنْطَلِقًا, and al-A'raf 7:131. The aya and the "
          "abyat are received text quoted exactly; the Ottoman print's plain-alif spellings are restored to "
          "standard orthography, a spelling normalization only.")
ADD_TR = (" On altıncı bâb aynı dosyadan (satır ~1358-1408, sahife 47-49) devam eder: Tarîf b. Temîm'in beyti "
          "أَوَكُلَّمَا وَرَدَتْ عُكَاظَ…, Cüveyye b. en-Nadr'ın beyti لَا يَأْلَفُ الدِّرْهَمُ…, metnin kalıpları "
          "ضَرَبَ زَيْدٌ عَمْرًا يَوْمَ الْجُمُعَةِ… ile كَانَ زَيْدٌ مُنْطَلِقًا ve A'râf 7:131. Âyet ve beyitler aynen "
          "alınmış mervî metindir; Osmanlı baskısının düz elifli imlâsı standart imlâya çevrilmiştir — yalnız "
          "bir imlâ normalizasyonudur.")
if "1358-1408" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch16:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
