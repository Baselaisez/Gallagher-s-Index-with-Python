# -*- coding: utf-8 -*-
"""Author chapter 14 of talkhis-al-miftah — خِلَافُ مُقْتَضَى الظَّاهِرِ وَالِالْتِفَاتُ.

The bab that answers chapter 6's khilaf al-muqtada note in full. Two doors:
the ISM ZAHIR set in the pronoun's place (Ibrahim b. Adham's عَبْدُكَ الْعَاصِي
where the plain sense wanted أَنَا — mercy is easier to ask for a slave than
for a self), and ILTIFAT — the turning of the discourse between the three
persons (takallum, khitab, ghayba), six kinds in all, which the mutakallimun
of maani count among the deepest beauties of the Qur'an. Al-Sakkaki widens
the term to ANY shift between the three modes; the jumhur restrict it to
re-expressing the SAME referent by a different mode — between the two
definitions stands ʿumūm khuṣūṣ muṭlaq, and the chapter teaches the khilaf
as a khilaf.

Four of the six kinds are walked in the chapter itself: takallum→ghayba
(al-Kawthar), takallum→khitab (Ya-Sin 22), khitab→ghayba (Yunus 22), and
ghayba→khitab (the Fatiha — with the nukta the musannif keeps for it: the
servant who has named Allah's perfections one by one finds, by مَالِكِ يَوْمِ
الدِّينِ, the strength gathered to address Him face to face). The remaining
two witnesses (Fatir 9 and ʿAlqama's bayt) are carried by note 116.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1155-1245: al-Kawthar
108:1-2, Ya-Sin 36:22, Yunus 10:22, al-Fatiha 1:4-5, and the du'a bayt of
Ibrahim b. Adham (إِلَهِي عَبْدُكَ الْعَاصِي أَتَاكَا…). The ayat and the du'a
are received text quoted exactly; the Ottoman print's plain-alif spellings
are restored to standard orthography (اَعْطَيْنَاكَ → أَعْطَيْنَاكَ), which is a
spelling normalization and not a change of text.

Grammar this chapter is chosen to teach:
  • note 116 `iltifat` — the six kinds with their witnesses, the
    Sakkaki-vs-jumhur khilaf, and the Fatiha nukta.
  • the engine work the probe forced: the iyya-family in PARTICLES (إِيَّاكَ
    was a فَعَّال intensive), the pronoun-remainder guard on the ب/ل/ك peel
    (بِهِمْ lost its jarr), the إِنَّا shadda branch with its NFC mark-order
    lesson, the itlaq-alif peel (أَتَاكَا reached no paradigm), the
    closed-class refusal in RootFinder, the mim-prefix geminate row
    (مُقِرًّا answered ق ر و/ي), the suffix-aware derived majhul
    (تُرْجَعُونَ was «Form IV, he»), and the tanwin-seat branch in IrabSign.
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

TITLE14 = {"ar": "خِلَافُ مُقْتَضَى الظَّاهِرِ وَالِالْتِفَاتُ",
           "en": "Against the Surface's Demand — and Iltifat, the Turning of the Discourse",
           "tr": "Zâhirin Muktezâsının Hilâfı ve İltifât — Sözün Yön Değiştirmesi"}

# ---------------------------------------------------------------- s1 — al-Kawthar
S.append({"id": "s1", "translation": {
 "en": "Truly WE have given you al-Kawthar — so pray to YOUR LORD and sacrifice. (al-Kawthar 108:1-2 — the discourse turns from the speaker to the third person.)",
 "tr": "Muhakkak Bİz sana Kevser'i verdik — öyleyse RABBİN için namaz kıl ve kurban kes. (Kevser 108:1-2 — söz, birinci şahıstan üçüncü şahsa döner.)"},
 "tokens": [
  tok("إِنَّا","inna","part",["inna-wa-akhawatuha","iltifat"],
      "«إِنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَ«نَا» اسْمُهَا فِي مَحَلِّ نَصْبٍ — وَالْكَلَامُ بِضَمِيرِ الْمُتَكَلِّمِ: مِنْ هُنَا يَبْدَأُ الِالْتِفَاتُ.",
      "إِنَّ with its ism already aboard: the shadda is the sign that this is the emphasis particle plus the fused «na» (mahallan mansub), not the speaker's أَنَا. The discourse opens in the FIRST person — «truly WE» — and holding that register in mind is the whole point: the turning, when it comes two words later, needs a fixed point to turn FROM.",
      "İsmi üzerinde kaynaşmış إِنَّ: şedde, bunun te'kîd harfi + bitişik «نَا» (mahallen mansûb) olduğunun alâmetidir; konuşanın أَنَا'sı değildir. Söz BİRİNCİ şahısta açılır — «muhakkak BİZ» — ve bu kipi akılda tutmak işin özüdür: iki kelime sonra gelecek dönüş, kendisinden DÖNÜLECEK sâbit bir nokta ister.",
      segments=[seg("إِنَّ","inna","part"), seg("نَا","pron-1p","pron")]),
  tok("أَعْطَيْنَاكَ","aata","verb",["inna-wa-akhawatuha","form-iv-verbs","mafulayn"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَ«نَا» فَاعِلٌ، وَالْكَافُ مَفْعُولُهُ الْأَوَّلُ — وَالْجُمْلَةُ خَبَرُ إِنَّ.",
      "«We have given you» — mazi built on the sukun for the attached «na» of the doers; the kaf is the FIRST object (أَعْطَى governs two). The clause is inna's khabar, in the position of raf'. Note the persons standing shoulder to shoulder: WE give, YOU receive — takallum and khitab both on stage, the ghayba not yet entered.",
      "«Biz sana verdik» — fâil «نَا»sına bitiştiği için sükûn üzere mebnî mâzî; kâf, BİRİNCİ mef'ûldür (أَعْطَى iki mef'ûl alır). Cümle, إِنَّ'nin haberidir, mahallen merfû. Şahısların omuz omuza durduğuna dikkat: BİZ veriyoruz, SEN alıyorsun — tekellüm ile hitâb sahnede, gaybet henüz girmemiştir.",
      segments=[seg("أَعْطَيْنَا","aata","verb"), seg("كَ","pron-2ms","pron")]),
  tok("الْكَوْثَرَ","kawthar","noun",["maful-bihi","mafulayn"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ.",
      "The SECOND object of the giving, in nasb by the plain fatha: al-Kawthar — the abundance, and the river of Paradise by that name.",
      "Vermenin İKİNCİ mef'ûlü, zâhir fetha ile mansûb: Kevser — bolluk; ve o adla cennetteki nehir.",
      punct="،"),
  tok("فَصَلِّ","salla","verb",["imperative-amr","naqis-verbs"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَ«صَلِّ» أَمْرٌ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ أَنْتَ.",
      "The fa of consequence — «so», the command growing out of the gift — and the amr of a naqis verb, built on the DROPPING of its weak letter: صَلِّ from صَلَّى, the kasra standing where the ya fell. The doer is «you», concealed.",
      "Tefrî' fâsı — «öyleyse»: emir, ihsandan filizlenir — ve nâkıs fiilin emri, illet harfinin DÜŞMESİ üzere mebnîdir: صَلَّى'dan صَلِّ; yânın düştüğü yerde kesra durur. Fâil, gizli «sen»dir.",
      segments=[seg("فَ","fa","part"), seg("صَلِّ","salla","verb")]),
  tok("لِرَبِّكَ","rabb","noun",["huruf-jarr","idafa-definiteness","iltifat","khilaf-muqtada-al-zahir"],
      "جَارٌّ وَمَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَهُنَا مَوْضِعُ الِالْتِفَاتِ مِنَ التَّكَلُّمِ إِلَى الْغَيْبَةِ: مُقْتَضَى الظَّاهِرِ «فَصَلِّ لَنَا».",
      "«To your LORD» — and here the discourse TURNS. The Giver spoke as «We»; the surface therefore demanded «so pray to US» (فَصَلِّ لَنَا). Instead the third person enters: your LORD — the name that carries lordship, nurture, ownership. This is ILTIFAT from takallum to ghayba, and the turn is the rhetoric: the gift came intimately, from «Us»; the worship is owed to the Lord in His station.",
      "«RABBİN için» — ve söz burada DÖNER. Veren «Biz» diye konuşmuştu; zâhir bu yüzden «bize namaz kıl» (فَصَلِّ لَنَا) isterdi. Yerine üçüncü şahıs girer: RABBİN — rubûbiyeti, terbiyeyi, sahipliği taşıyan isim. Bu, tekellümden gaybete İLTİFÂTtır ve dönüşün kendisi belâgattir: ihsan «Biz»den, yakınlıkla geldi; ibâdet ise makāmındaki Rabbe borçludur.",
      segments=[seg("لِ","li","prep"), seg("رَبِّ","rabb","noun"), seg("كَ","pron-2ms","pron")]),
  tok("وَانْحَرْ","nahara","verb",["imperative-amr","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«انْحَرْ» أَمْرٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ أَنْتَ.",
      "«And sacrifice» — the joining waw hangs a second command on the first: amr built on the sukun, its hamza a hamzat al-wasl that melts after the waw. Prayer and sacrifice, the two great acts of devotion, both turned toward the Lord the iltifat just named.",
      "«Ve kurban kes» — atıf vâvı ikinci emri birinciye asar: sükûn üzere mebnî emir; hemzesi, vâvdan sonra eriyen vasıl hemzesidir. Namaz ve kurban — iki büyük ibâdet — ikisi de iltifâtın az önce andığı Rabbe yöneltilmiştir.",
      segments=[seg("وَ","wa","part"), seg("انْحَرْ","nahara","verb")],
      punct=".")],
 "jumal": [
  J("إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ فَصَلِّ لِرَبِّكَ",
    "اِلْتِفَاتٌ مِنَ التَّكَلُّمِ إِلَى الْغَيْبَةِ — مُقْتَضَى الظَّاهِرِ «فَصَلِّ لَنَا».",
    "Iltifat from first to third person: «We gave» … «so pray to your Lord» — where the surface demanded «pray to Us».",
    "Tekellümden gaybete iltifât: «Biz verdik» … «Rabbin için namaz kıl» — zâhir «bize namaz kıl» isterdi.")]})

# ---------------------------------------------------------------- s2 — Ya-Sin 22
S.append({"id": "s2", "translation": {
 "en": "And why should I not worship the One who created me — and to Him YOU will be returned? (Ya-Sin 36:22 — the discourse turns from the speaker to those addressed.)",
 "tr": "Ben, beni yaratana neden ibadet etmeyeyim — ve SİZ O'na döndürüleceksiniz? (Yâsîn 36:22 — söz, birinci şahıstan muhataplara döner.)"},
 "tokens": [
  tok("وَمَا","ma-istifham","pron",["anwa-ma","mubtada-khabar"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَ«مَا» اسْتِفْهَامِيَّةٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.",
      "The interrogative «ma» as mubtada — «what is it to me…?», a question worn by wonder, not a request for information. The speaker is the believer of Ya-Sin, arguing for his own worship.",
      "İstifhâm «mâ»sı mübtedâ — «bana ne oluyor ki…?»; bilgi isteyen değil, hayret yüklü bir sorudur. Konuşan, Yâsîn'in mü'minidir; kendi ibâdetinin savunmasını yapar.",
      segments=[seg("وَ","wa","part"), seg("مَا","ma-istifham","pron")]),
  tok("لِيَ","li","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ — مُسْتَقَرٌّ.",
      "«To me» — the jarr pair standing as the khabar, mustaqarr on an omitted amil: what is [there] to me. The lam wears its fatha before the pronoun, as it always does.",
      "«Bana» — haber olarak duran câr-mecrûr; mahzûf âmil üzere müstakar: bana ne [var]. Lâm, zamirden önce her zamanki fethasını giyer.",
      segments=[seg("لِ","li","prep"), seg("يَ","pron-1s","pron")]),
  tok("لَا","la-nafiya","part",[],
      "حَرْفُ نَفْيٍ.",
      "The negation over the coming verb.",
      "Gelecek fiilin üzerindeki nefiy."),
  tok("أَعْبُدُ","abada","verb",["mudari-marfu","hal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "«[that] I do not worship» — mudari' in raf', its doer the concealed «I»; the clause sits as HAL: what is it to me, in the state of not worshipping? Still the first person — the register the aya will turn away from at its close.",
      "«ibadet etmeyeyim» — merfû muzâri; fâili gizli «ben». Cümle HÂL olarak mahallen mansûbtur: bana ne oluyor, ibadet etmez hâlde? Hâlâ birinci şahıs — âyetin sonunda dönüleceği kip.",
      punct=""),
  tok("الَّذِي","alladhi","pron",["ism-mawsul","maful-bihi"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ، فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "The relative, mabni, standing as the object of the worship: «the One who…» — and its sila comes to name Him by His act.",
      "İsm-i mevsûl, mebnî; ibâdetin mef'ûlü olarak mahallen mansûb: «O ki…» — ve sılası, O'nu fiiliyle adlandırmaya gelir."),
  tok("فَطَرَنِي","fatara","verb",["ya-al-mutakallim"],
      "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "«who CREATED me» — fatara, the primal origination, the verb of Ibrahim's فَطَرَنِي before it. The nun is the protective nun that spares the verb's ending from the ya's kasra; the ya of the speaker is the object. The clause is the sila, with no place in i'rab.",
      "«beni YARATAN» — fatara: ilk yaratış, yoktan var ediş. Nûn, fiilin sonunu yânın kesrasından koruyan vikāye nûnudur; mütekellim yâsı mef'ûldür. Cümle sıladır; i'râbdan mahalli yoktur.",
      segments=[seg("فَطَرَ","fatara","verb"), seg("نِ","ni-wiqaya","part"), seg("ي","pron-1s","pron")]),
  tok("وَإِلَيْهِ","ila","prep",["huruf-jarr","qasr","taqdim-al-musnad-ilayh"],
      "الْوَاوُ عَاطِفَةٌ، وَجَارٌّ وَمَجْرُورٌ مُقَدَّمٌ عَلَى عَامِلِهِ لِإِفَادَةِ الِاخْتِصَاصِ.",
      "«And to HIM» — the jarr pair FRONTED over its verb, and the fronting is a qasr: to Him and to none other is the return. The pronoun still ghayba, the Creator just named by His act.",
      "«Ve yalnız O'NA» — câr-mecrûr, fiilinin ÖNÜNE alınmıştır ve takdîm bir kasırdır: dönüş O'nadır, başkasına değil. Zamir hâlâ gaybettedir; Yaratan az önce fiiliyle anılmıştı.",
      segments=[seg("وَ","wa","part"), seg("إِلَيْ","ila","prep"), seg("هِ","pron-3ms","pron")]),
  tok("تُرْجَعُونَ","rajaa","verb",["naib-al-fail","afal-khamsa","iltifat","khilaf-muqtada-al-zahir"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — وَالِالْتِفَاتُ مِنَ التَّكَلُّمِ إِلَى الْخِطَابِ: مُقْتَضَى الظَّاهِرِ «وَإِلَيْهِ أُرْجَعُ».",
      "«YOU will be returned» — and the discourse has TURNED. The whole aya ran in the first person (what is it to ME… who created ME); the surface demanded «and to Him I shall be returned» (أُرْجَعُ). Instead the plural YOU: the speaker, having argued worship for himself, wheels on his people — the return he proved for himself is theirs too, whether they worship or not. Passive, one of the five verbs, its raf' the fixed nun; the waw is the deputy doer.",
      "«SİZ döndürüleceksiniz» — ve söz DÖNMÜŞTÜR. Âyetin tamamı birinci şahısta aktı (BANA ne oluyor… BENİ yaratan); zâhir «ben O'na döndürüleceğim» (أُرْجَعُ) isterdi. Yerine çoğul SİZ: ibâdeti kendi adına ispat eden konuşan, kavmine döner — kendisi için kanıtladığı dönüş, ibadet etseler de etmeseler de onlarındır. Meçhûl; ef'âl-i hamseden, ref'i sâbit nûnladır; vâv, nâib-i fâildir.",
      punct="؟")],
 "jumal": [
  J("وَمَا لِيَ لَا أَعْبُدُ الَّذِي فَطَرَنِي وَإِلَيْهِ تُرْجَعُونَ",
    "اِلْتِفَاتٌ مِنَ التَّكَلُّمِ إِلَى الْخِطَابِ — مُقْتَضَى الظَّاهِرِ «وَإِلَيْهِ أُرْجَعُ».",
    "Iltifat from first to second person: the speaker proves the return for himself, then hands it to his hearers — «YOU will be returned» where the surface demanded «I».",
    "Tekellümden hitâba iltifât: konuşan dönüşü kendi adına ispatlar, sonra dinleyenlere devreder — zâhir «ben» isterken «SİZ döndürüleceksiniz».")]})

# ---------------------------------------------------------------- s3 — Yunus 22
S.append({"id": "s3", "translation": {
 "en": "…until, when YOU are aboard the ships, and they run with THEM… (Yunus 10:22 — the discourse turns from those addressed to the third person.)",
 "tr": "…nihayet SİZ gemilerde olduğunuzda ve gemiler ONLARI götürdüğünde… (Yûnus 10:22 — söz, muhataplardan üçüncü şahsa döner.)"},
 "tokens": [
  tok("حَتَّى","hatta","part",[],
      "حَرْفُ ابْتِدَاءٍ — يُبْتَدَأُ بَعْدَهُ الْكَلَامُ وَلَا عَمَلَ لَهُ هُنَا.",
      "Here NOT the jarr letter: before إِذَا it is the hatta of COMMENCEMENT — it opens a new stretch of discourse and governs nothing.",
      "Burada cer harfi DEĞİL: إِذَا'dan önce İBTİDÂ hattâsıdır — yeni bir söz açar ve hiçbir şeyi amel etmez."),
  tok("إِذَا","idha","part",["idha-shartiyya"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "The zarf of future time carrying the sense of condition: «when…» — its clause is the mudaf-ilayh of the moment it names.",
      "Şart mânâsı yüklü istikbal zarfı: «…dığı zaman» — cümlesi, adlandırdığı ânın muzâfun ileyhidir."),
  tok("كُنْتُمْ","kana","verb",["kana-wa-akhawatuha","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهَا — وَالْخِطَابُ لِلنَّاسِ جَمِيعًا.",
      "«when YOU were» — kana the incomplete sister, built on the sukun for the subject-ta; the ta-plus-mim is its ism. Mark the register: the aya is speaking TO them — second person, the mode it is about to leave.",
      "«SİZ olduğunuzda» — nâkıs kardeş kâne, fâil tâsına bitiştiği için sükûn üzere mebnî; tâ+mîm onun ismidir. Kipe dikkat: âyet onlara HİTAP etmektedir — ikinci şahıs; birazdan terk edeceği kip."),
  tok("فِي","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ، مُسْتَقَرٌّ.",
      "The jarr letter; the pair is kana's khabar, mustaqarr.",
      "Cer harfi; câr-mecrûr, kânenin haberidir — müstakar."),
  tok("الْفُلْكِ","fulk","noun",["huruf-jarr"],
      "اسْمٌ مَجْرُورٌ — وَ«الْفُلْكُ» يَسْتَوِي فِيهِ الْوَاحِدُ وَالْجَمْعُ.",
      "«The ships» — in jarr; and فُلْك is one of the words whose singular and plural share a single form. Here it is plural: the ships of the sea-farers.",
      "«Gemiler» — mecrûr; فُلْك, tekili ile çoğulu tek kalıpta birleşen kelimelerdendir. Burada çoğuldur: deniz yolcularının gemileri.",
      punct="،"),
  tok("وَجَرَيْنَ","jara","verb",["naqis-verbs","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنُونُ النِّسْوَةِ فَاعِلٌ — وَالضَّمِيرُ لِلْفُلْكِ.",
      "«and they RAN» — the feminine plural nun as doer, its pronoun the ships (a broken-plural sense takes the feminine). Mazi of the naqis جَرَى, its weak ya surfacing before the nun: جَرَيْنَ.",
      "«ve AKTILAR» — nisve nûnu fâildir; zamiri gemilerdir (cem' mânâsı müennes muâmelesi görür). Nâkıs جَرَى'nın mâzîsi; illetli yâsı nûndan önce yüzeye çıkar: جَرَيْنَ.",
      segments=[seg("وَ","wa","part"), seg("جَرَيْنَ","jara","verb")]),
  tok("بِهِمْ","bi","prep",["huruf-jarr","iltifat","khilaf-muqtada-al-zahir"],
      "جَارٌّ وَمَجْرُورٌ — وَالِالْتِفَاتُ مِنَ الْخِطَابِ إِلَى الْغَيْبَةِ: مُقْتَضَى الظَّاهِرِ «وَجَرَيْنَ بِكُمْ».",
      "«with THEM» — and the discourse has TURNED again. The aya was addressing them — «when YOU were aboard» — so the surface demanded «and they ran with YOU» (بِكُمْ). Instead the third person: with THEM. The classical reading of the turn: as the storm nears, the ungrateful are turned OUT of the divine address — spoken about, no longer spoken to — a distancing that is itself the rebuke.",
      "«ONLARLA» — ve söz yine DÖNMÜŞTÜR. Âyet onlara hitap ediyordu — «SİZ gemilerdeyken» — zâhir bu yüzden «sizinle aktılar» (بِكُمْ) isterdi. Yerine üçüncü şahıs: ONLARLA. Dönüşün klasik okunuşu: fırtına yaklaşırken nankörler ilâhî hitâbın DIŞINA çıkarılır — artık kendilerine değil, haklarında konuşulur — ve bu uzaklaştırma azarın ta kendisidir.",
      segments=[seg("بِ","bi","prep"), seg("هِمْ","pron-3mp","pron")],
      punct="…")],
 "jumal": [
  J("حَتَّى إِذَا كُنْتُمْ فِي الْفُلْكِ وَجَرَيْنَ بِهِمْ",
    "اِلْتِفَاتٌ مِنَ الْخِطَابِ إِلَى الْغَيْبَةِ — مُقْتَضَى الظَّاهِرِ «بِكُمْ»: أُخْرِجُوا مِنَ الْخِطَابِ إِخْرَاجًا.",
    "Iltifat from second to third person: «when YOU were aboard… and they ran with THEM» — the ungrateful are turned out of the address, and the distancing is the rebuke.",
    "Hitâbdan gaybete iltifât: «SİZ gemideyken… onlarla aktılar» — nankörler hitâbdan çıkarılır ve uzaklaştırma, azarın kendisidir.")]})

# ---------------------------------------------------------------- s4 — al-Fatiha
S.append({"id": "s4", "translation": {
 "en": "Master of the Day of Judgment. YOU alone we worship. (al-Fatiha 1:4-5 — the discourse turns from the third person to direct address.)",
 "tr": "Din gününün sahibi. Yalnız SANA ibadet ederiz. (Fâtiha 1:4-5 — söz, üçüncü şahıstan doğrudan hitâba döner.)"},
 "tokens": [
  tok("مَالِكِ","malik","noun",["ism-fail","idafa-definiteness","tarif-bil-idafa"],
      "صِفَةٌ لِلَّهِ تَعَالَى مَجْرُورَةٌ، وَهُوَ مُضَافٌ — وَالْكَلَامُ إِلَى هُنَا غَيْبَةٌ: الْحَمْدُ لِلَّهِ… مَالِكِ….",
      "«Master» — ism fail, a sifa of Allah in jarr, itself a mudaf. Count the register: from الْحَمْدُ لِلَّهِ the sura has spoken ABOUT Him — Lord of the worlds, the Merciful, Master of the Day — every attribute in the third person, each one building what the musannif calls the gathering strength.",
      "«Sahibi» — ism-i fâil; Allah'ın mecrûr sıfatı, kendisi muzâf. Kipi sayın: الْحَمْدُ لِلَّهِ'den beri sûre O'nun HAKKINDA konuşmuştur — âlemlerin Rabbi, Rahmân, din gününün sahibi — her vasıf üçüncü şahısta; her biri, musannifin «birikip güçlenen kuvvet» dediği şeyi kurar."),
  tok("يَوْمِ","yawm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.",
      "The mudaf ilayh, itself a mudaf: the chain runs on.",
      "Mecrûr muzâfun ileyh; kendisi de muzâftır: zincir sürer."),
  tok("الدِّينِ","din","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالدِّينُ هُنَا الْجَزَاءُ.",
      "The chain closes: «of the Judgment» — din here is requital, the settling of accounts.",
      "Zincir kapanır: «dînin» — din burada cezâ, hesabın görülmesidir.",
      punct="."),
  tok("إِيَّاكَ","iyyaka","pron",["maful-bihi","qasr","iltifat","khilaf-muqtada-al-zahir"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَتَقْدِيمُهُ قَصْرٌ — وَالِالْتِفَاتُ مِنَ الْغَيْبَةِ إِلَى الْخِطَابِ: مُقْتَضَى الظَّاهِرِ «إِيَّاهُ نَعْبُدُ».",
      "«YOU alone» — and the sura TURNS to face Him. Every attribute so far was ghayba; the surface demanded «HIM we worship» (إِيَّاهُ نَعْبُدُ). But the servant who has named the perfections one by one — the musannif's nukta — finds by the end of مَالِكِ يَوْمِ الدِّينِ that the gathered force can no longer speak ABOUT; it must speak TO. The detached pronoun, fronted, is also a QASR: You and none other. Iltifat and ikhtisas in one word — the most famous turning in the language.",
      "«Yalnız SANA» — ve sûre O'na DÖNER. Şimdiye dek her vasıf gaybetteydi; zâhir «O'NA ibadet ederiz» (إِيَّاهُ نَعْبُدُ) isterdi. Fakat kemâlleri bir bir sayan kul — musannifin nüktesi — مَالِكِ يَوْمِ الدِّينِ'in sonunda, biriken gücün artık HAKKINDA konuşamayacağını, yüz yüze KONUŞMASI gerektiğini bulur. Öne alınmış munfasıl zamir aynı zamanda KASIRdır: Sana, başkasına değil. Bir kelimede iltifât ve ihtisâs — dilin en meşhur dönüşü.",
      punct=""),
  tok("نَعْبُدُ","abada","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ نَحْنُ.",
      "«we worship» — mudari' in raf', its doer the concealed «we»: the single servant praying in the plural of the praying community.",
      "«ibadet ederiz» — merfû muzâri; fâili gizli «biz»: tek kul, ibadet eden cemaatin çoğuluyla söyler.",
      punct=".")],
 "jumal": [
  J("مَالِكِ يَوْمِ الدِّينِ إِيَّاكَ نَعْبُدُ",
    "اِلْتِفَاتٌ مِنَ الْغَيْبَةِ إِلَى الْخِطَابِ مَعَ قَصْرٍ بِتَقْدِيمِ الْمَفْعُولِ — مُقْتَضَى الظَّاهِرِ «إِيَّاهُ نَعْبُدُ».",
    "Iltifat from third person to direct address, carrying a qasr in the fronted object: the named perfections gather until speech about Him must become speech to Him.",
    "Gaybetten hitâba iltifât; öne alınmış mef'ûlde bir kasır taşır: sayılan kemâller birikir, tâ ki O'nun hakkındaki söz O'na söylenen söz olmak zorunda kalır.")]})

# ---------------------------------------------------------------- s5 — Ibrahim b. Adham
S.append({"id": "s5", "translation": {
 "en": "My God — Your disobedient SLAVE has come to You, confessing his sins, and he has called on You. (Ibrahim b. Adham's du'a — the plain sense demanded «I»; the servant names himself a slave to ask for mercy.)",
 "tr": "İlâhî — âsi KULUN Sana geldi; günahlarını ikrar ederek, ve Sana dua etti. (İbrahim b. Edhem'in duası — zâhir «ben» isterdi; kul, merhamet dilemek için kendini «kulun» diye adlandırır.)"},
 "tokens": [
  tok("إِلَهِي","ilah","noun",["vocative-munada","ya-al-mutakallim"],
      "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ.",
      "«My God» — a munada whose calling particle (يَا) is omitted, as du'a loves to do; the mudaf ilayh is the speaker's own ya. The most intimate address in the language opens the plea.",
      "«İlâhî / Allah'ım» — nidâ harfi (يَا) hazfedilmiş münâdâ; duânın sevdiği üslûp. Muzâfun ileyh, konuşanın kendi yâsıdır. Dilin en içli hitâbı, yakarışı açar.",
      segments=[seg("إِلَهِ","ilah","noun"), seg("ي","pron-1s","pron")],
      punct="،"),
  tok("عَبْدُكَ","abd","noun",["mubtada-khabar","khilaf-muqtada-al-zahir","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وُضِعَ الظَّاهِرُ مَوْضِعَ الضَّمِيرِ: مُقْتَضَى الظَّاهِرِ «أَنَا».",
      "«Your SLAVE» — the mubtada, and here is the chapter's FIRST door: an ism zahir set where the pronoun belonged. The speaker means himself; the surface demanded «I, the disobedient one» (أَنَا الْعَاصِي). But «I» claims standing, and this prayer wants none: he comes as a slave — Yours, owned, with no plea but the owning. The musannif files the motive precisely: لِطَلَبِ الشَّفَقَةِ وَالْمَرْحَمَةِ — to call forth tenderness and mercy.",
      "«KULUN» — mübtedâ; ve işte bâbın BİRİNCİ kapısı: zamirin yerine konmuş ism-i zâhir. Konuşan kendini kasteder; zâhir «ben, âsi olan» (أَنَا الْعَاصِي) isterdi. Fakat «ben» bir makam iddia eder; bu duânın istediği makam yoktur: kul olarak gelir — Senin kulun, sahiplinin sahibinden başka delili olmadan. Musannif gerekçeyi tam kaydeder: لِطَلَبِ الشَّفَقَةِ وَالْمَرْحَمَةِ — şefkat ve merhameti celbetmek için.",
      segments=[seg("عَبْدُ","abd","noun"), seg("كَ","pron-2ms","pron")]),
  tok("الْعَاصِي","aasi","noun",["ism-fail","naat-sifa","ism-maqsur-manqus"],
      "صِفَةٌ لِعَبْدُكَ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — مَنْقُوصٌ.",
      "«the disobedient» — sifa of the slave, a manqus whose damma is estimated on the ya (thiqal). The confession is built into the very NAME he gives himself: not a slave who happens to have sinned, but THE disobedient slave, article and all.",
      "«âsi» — kulun sıfatı; menkūstur, dammesi yâ üzerinde takdîr edilir (sıklet). İtiraf, kendine verdiği İSMİN içine örülmüştür: günah işlemiş herhangi bir kul değil, harf-i tarifiyle, O âsi kul."),
  tok("أَتَاكَا","ata","verb",["naqis-verbs","mubtada-khabar"],
      "فِعْلٌ مَاضٍ، وَالْكَافُ مَفْعُولٌ بِهِ، وَالْأَلِفُ لِلْإِطْلَاقِ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.",
      "«has COME to You» — mazi of the naqis أَتَى, its kaf the object, and the final alif is the ALIF AL-ITLAQ: verse pads its rhyme-word with a prolonging alif the grammar does not count. The clause is the khabar of «Your slave». He does not send the plea; he brings it.",
      "«Sana GELDİ» — nâkıs أَتَى'nın mâzîsi; kâf mef'ûl, sondaki elif ise ITLAK ELİFİdir: şiir, kafiye kelimesini gramerin saymadığı bir uzatma elifiyle doldurur. Cümle, «kulun»un haberidir. Yakarışı göndermez; kendisi getirir.",
      segments=[seg("أَتَا","ata","verb"), seg("كَ","pron-2ms","pron"), seg("ا","alif-itlaq","part")]),
  tok("مُقِرًّا","muqirr","noun",["hal","ism-fail","doubled-verbs"],
      "حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ — اسْمُ فَاعِلٍ مِنْ أَقَرَّ، مِنَ الْمُضَاعَفِ.",
      "«confessing» — hal in nasb by the plain fathatan (the final alif is only the tanwin's seat): in WHAT STATE did he come? Confessing. Ism fail of the geminate Form IV أَقَرَّ — the shadda holds the doubled ra that is the root's third letter.",
      "«ikrar ederek» — zâhir fethateynle mansûb hâl (sondaki elif yalnız tenvinin kürsüsüdür): NE HÂLDE geldi? İkrar ederek. Muzâaf IV. bâb أَقَرَّ'nin ism-i fâili — şedde, kökün üçüncü harfi olan çift râyı tutar."),
  tok("بِالذُّنُوبِ","dhanb","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«مُقِرًّا».",
      "«of the sins» — the jarr pair hanging on the confessing: iqrar takes its object through bi. Plural: not one lapse but the whole ledger.",
      "«günahları» — câr-mecrûr, «مُقِرًّا»ya bağlanır: ikrar, mef'ûlünü bâ ile alır. Çoğul: tek bir sürçme değil, defterin tamamı.",
      segments=[seg("بِ","bi","prep"), seg("الذُّنُوبِ","dhanb","noun")]),
  tok("وَقَدْ","qad","part",["qad-harf","anwa-al-waw","hal"],
      "الْوَاوُ لِلْحَالِ، وَ«قَدْ» لِلتَّحْقِيقِ.",
      "The waw of circumstance with qad of realization: «while he has already…» — a past verb after وَقَدْ reads as an accomplished state.",
      "Hâl vâvı ile tahkîk kādı: «hâlbuki çoktan…» — وَقَدْ'den sonraki mâzî, tamamlanmış bir hâl olarak okunur.",
      segments=[seg("وَ","wa","part"), seg("قَدْ","qad","part")]),
  tok("دَعَاكَا","daa","verb",["naqis-verbs","hal"],
      "فِعْلٌ مَاضٍ، وَالْكَافُ مَفْعُولٌ بِهِ، وَالْأَلِفُ لِلْإِطْلَاقِ — وَالْجُمْلَةُ حَالٌ.",
      "«and he has CALLED on You» — the second rhyme-word, the same anatomy as أَتَاكَا: naqis mazi, object kaf, itlaq alif. The bayt's two halves close on the same sound because the plea's two acts — coming and calling — end in the same You.",
      "«ve Sana DUA ETTİ» — ikinci kafiye kelimesi; أَتَاكَا ile aynı anatomi: nâkıs mâzî, mef'ûl kâfı, ıtlak elifi. Beytin iki yarısı aynı seste kapanır; çünkü yakarışın iki fiili — gelmek ve çağırmak — aynı SEN'de biter.",
      segments=[seg("دَعَا","daa","verb"), seg("كَ","pron-2ms","pron"), seg("ا","alif-itlaq","part")],
      punct=".")],
 "jumal": [
  J("إِلَهِي عَبْدُكَ الْعَاصِي أَتَاكَا مُقِرًّا بِالذُّنُوبِ وَقَدْ دَعَاكَا",
    "وَضْعُ الظَّاهِرِ مَوْضِعَ الضَّمِيرِ لِطَلَبِ الشَّفَقَةِ — مُقْتَضَى الظَّاهِرِ «أَنَا الْعَاصِي».",
    "An ism zahir in the pronoun's place, to call forth mercy: «Your disobedient slave has come» where the plain sense demanded «I». The plea renounces standing before it asks anything.",
    "Merhameti celb için zamirin yerine ism-i zâhir: zâhir «ben» isterken «âsi kulun geldi». Yakarış, bir şey istemeden önce makam iddiasından vazgeçer.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # NEW this chapter
 "kawthar":   g("الْكَوْثَر", "ك ث ر", "propn", "al-Kawthar — the abundance; the river of Paradise", "Kevser — bolluk; cennetteki nehir", 4),
 "fulk":      g("فُلْك", "ف ل ك", "noun", "ship(s) — one form for singular and plural", "gemi(ler) — tekili ve çoğulu aynı kalıp", 4),
 "aasi":      g("عَاصٍ", "ع ص ي", "noun", "disobedient, sinning (ism fail, manqus)", "âsi, günahkâr (ism-i fâil, menkūs)", 4),
 "muqirr":    g("مُقِرّ", "ق ر ر", "noun", "confessing, admitting (ism fail of أَقَرَّ)", "ikrar eden, itiraf eden (أَقَرَّ'nin ism-i fâili)", 5, form="IV"),
 "nahara":    g("نَحَرَ", "ن ح ر", "verb", "to sacrifice (a camel), to slaughter", "kurban kesmek, boğazlamak", 4, form="I"),
 "abada":     g("عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek, kulluk etmek", 2, form="I"),
 "fatara":    g("فَطَرَ", "ف ط ر", "verb", "to create, to originate", "yaratmak, yoktan var etmek", 3, form="I"),
 "iyyaka":    g("إِيَّاكَ", None, "pron", "You (detached object pronoun — fronting it gives qasr)", "Seni / yalnız Sana (munfasıl nasb zamiri — takdîmi kasır verir)", 3),
 "ma-istifham": g("مَا (الاِسْتِفْهَامِيَّة)", None, "pron", "what? (interrogative ma)", "ne? (istifhâm mâsı)", 3),
 "alif-itlaq": g("ـا (أَلِفُ الْإِطْلَاقِ)", None, "part", "the prolonging alif at a verse's rhyme — metre, not grammar", "kafiye sonundaki uzatma (ıtlak) elifi — gramer değil vezin", 5),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "salla":     g("صَلَّى", "ص ل و", "verb", "to pray; to bless", "namaz kılmak; salât etmek", 1, form="II"),
 "ata":       g("أَتَى", "أ ت ي", "verb", "to come", "gelmek", 1, form="I"),
 "daa":       g("دَعَا", "د ع و", "verb", "to call upon, to pray", "dua etmek, çağırmak", 1, form="I"),
 "rajaa":     g("رَجَعَ", "ر ج ع", "verb", "to return", "dönmek", 1, form="I"),
 "malik":     g("مَالِك", "م ل ك", "noun", "owner, master (ism fail)", "mâlik, sahip (ism-i fâil)", 2),
 "din":       g("دِين", "د ي ن", "noun", "religion; judgment, requital", "din; cezâ, hesap günü karşılığı", 2),
 "dhanb":     g("ذَنْب", "ذ ن ب", "noun", "sin", "günah", 2, plural="ذُنُوب"),
 "hatta":     g("حَتَّى", None, "part", "until; even; (before idha) opening a clause", "tâ ki; hattâ (إِذَا'dan önce ibtidâ harfi)", 3),
}

def build_morph():
    """Copies for salla/ata/daa/rajaa; three new sound paradigms.

    عَبَدَ يَعْبُدُ — bab نَصَرَ, masdar عِبَادَة.
    فَطَرَ يَفْطُرُ — bab نَصَرَ, masdar فَطْر.
    نَحَرَ يَنْحَرُ — bab فَتَحَ (the guttural ha), masdar نَحْر.
    """
    out = {}
    for pkg, lex in [("aqaid-ahl-al-sunna", "salla"),
                     ("wasiyyat-abi-hanifa", "ata"),
                     ("yunus-wa-al-hut", "daa"),
                     ("wasiyyat-abi-hanifa", "rajaa")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    out["abada"] = _sg.sound1("nasara", "عَبَد", "عْبُد", "اُعْبُد", "عِبَادَة", "عَابِد",
                              "مَعْبُود", "عُبِدَ", "يُعْبَدُ")
    out["fatara"] = _sg.sound1("nasara", "فَطَر", "فْطُر", "اُفْطُر", "فَطْر", "فَاطِر",
                               "مَفْطُور", "فُطِرَ", "يُفْطَرُ")
    out["nahara"] = _sg.sound1("fataha", "نَحَر", "نْحَر", "اِنْحَر", "نَحْر", "نَاحِر",
                               "مَنْحُور", "نُحِرَ", "يُنْحَرُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/14.json").write_text(
    json.dumps({"chapter": 14, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 14 for c in man["chapters"]):
    man["chapters"].append({"n": 14, "title": TITLE14})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.14.0"
ADD_EN = (" Chapter 14 continues from the same file (lines ~1155-1245): the ism-zahir-for-pronoun section "
          "with Ibrahim b. Adham's du'a bayt (إِلَهِي عَبْدُكَ الْعَاصِي أَتَاكَا…), and the iltifat section with "
          "al-Kawthar 108:1-2, Ya-Sin 36:22, Yunus 10:22, and al-Fatiha 1:4-5. The ayat and the du'a are "
          "received text quoted exactly; the Ottoman print's plain-alif spellings are restored to standard "
          "orthography, a spelling normalization only.")
ADD_TR = (" On dördüncü bâb aynı dosyadan (satır ~1155-1245) devam eder: zamir yerine ism-i zâhir faslı, "
          "İbrahim b. Edhem'in duâ beytiyle (إِلَهِي عَبْدُكَ الْعَاصِي أَتَاكَا…), ve iltifât faslı — Kevser 108:1-2, "
          "Yâsîn 36:22, Yûnus 10:22 ve Fâtiha 1:4-5 ile. Âyetler ve duâ, aynen alınmış mervî metindir; Osmanlı "
          "baskısının düz elifli imlâsı standart imlâya çevrilmiştir — yalnız bir imlâ normalizasyonudur.")
if "1155-1245" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch14:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
