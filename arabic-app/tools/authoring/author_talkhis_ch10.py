# -*- coding: utf-8 -*-
"""Author chapter 10 of talkhis-al-miftah — التَّوَابِعُ بَعْدَ الْمُسْنَدِ إِلَيْهِ.

Chapters 7-9 asked whether to say the subject, and then how to make it
definite. This one asks what may be hung on it AFTERWARDS, and the answer is
the five tawabiʿ the nahw books already name — النَّعْت، التَّوْكِيد، عَطْفُ
الْبَيَان، الْبَدَل، عَطْفُ النَّسَق — each with its own balagha reasons.

The pattern is the one this fann keeps repeating: the SYNTAX is settled and
the CHOICE is not. A ṣifa may explain (الْجِسْمُ الطَّوِيلُ الْعَرِيضُ الْعَمِيقُ),
narrow (زَيْدٌ التَّاجِرُ), praise (زَيْدٌ الْعَالِمُ), blame (زَيْدٌ الْجَاهِلُ) or
merely confirm (أَمْسِ الدَّابِرُ) — and the last three are told apart by nothing
in the grammar at all, only by what the hearer already knew.

Taʾkīd has four reasons and three of them are the removal of a specific
suspicion: that the speech was figurative (قَطَعَ اللِّصَّ الْأَمِيرُ نَفْسُهُ — the
commander in person, not by his men), that the speaker misspoke, or that the
statement did not reach everybody (جَاءَنِي الْقَوْمُ كُلُّهُمْ). ʿAṭf bayān
clarifies with a name of its own; badal is ziyādat taqrīr and comes in the
three kinds the books count; and ʿaṭf nasaq details the subject while the
predicate is said once (جَاءَنِي زَيْدٌ وَعَمْرٌو), corrects a hearer who had it
wrong (زَيْدٌ لَا عَمْرٌو), or leaves him in doubt — and the SAME sentence is
shakk when the speaker does not know and tashkīk when he does.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~885-925, which carries
all of it in vowelled Arabic. Paired examples are juxtaposed with a full stop
between them, as in chapters 5 to 9; nothing is composed.

Grammar this chapter is chosen to teach:
  • جَاءَنِي four times over — نُونُ الْوِقَايَةِ, which note 103 states and the
    analyzer's peel had never been told: the nun belongs to neither side, and
    the ya after it is a MAF'UL, never a mudaf ilayh, because a verb is never
    a mudaf.
  • أَخُوكَ — one of the five nouns, in raf' by the WAW, and annexed. Its root
    cannot be read off its surface at all, since what stands at the end is a
    case-LETTER.
  • اللِّصَّ and كُلُّهُمْ — geminate nouns, whose third radical is a shadda and
    disappears the moment the harakat are stripped.
  • عَمْرٌو — the silent WAW OF DISTINCTION, written in raf' and jarr only, to
    tell the name from عُمَر; the tanwin therefore sits on the ra with a letter
    still to come, and both harakat auditors have to know it.
  • سُلِبَ عَمْرٌو ثَوْبُهُ — a passive with its naʾib al-faʿil, and a badal
    ishtimal on top of it.
  • لَا as an ʿATIF, which is a face the analyzer's table did not offer at all.
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
# جَاءَنِي, four times in this chapter — one helper so the four never drift
JAA_SEG = [seg("جَاءَ", "jaa", "verb"), seg("نِي", "ni-wiqaya", "pron")]
JAA_AR = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ نُونُ الْوِقَايَةِ حَرْفٌ لَا مَحَلَّ لَهُ، "
          "وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.")
JAA_EN = ("A mazi verb, mabni on the fatha — and «ني» is TWO things: نُونُ الْوِقَايَةِ, a letter "
          "belonging to neither side and having no position in i'rab, and the speaker's ya, an "
          "attached pronoun mabni in the position of nasb as the MAF'UL BIHI. The nun is a shield: "
          "without it the verb's own final fatha would be broken by the kasra the ya demands. And "
          "the ya is an object, never a mudaf ilayh — a verb is never a mudaf.")
JAA_TR = ("Fetha üzere mebnî mâzî fiil — ve «ني» İKİ şeydir: iki taraftan da olmayan, i'râbdan "
          "mahalli bulunmayan NÛNU'L-VİKĀYE, ve mahallen mansub MEF'ÛLÜN BİH olan mütekellim yâsı. "
          "Nûn bir kalkandır: o olmasa fiilin kendi son fethası, yânın istediği kesra ile bozulurdu. "
          "Yâ ise mef'ûldür, muzâfun ileyh değildir — fiil muzâf olmaz.")
def jaa(): return tok("جَاءَنِي", "jaa", "verb", ["ya-al-mutakallim", "fail"],
                      JAA_AR, JAA_EN, JAA_TR, segments=JAA_SEG)

TITLE10 = {"ar": "التَّوَابِعُ بَعْدَ الْمُسْنَدِ إِلَيْهِ",
           "en": "What Follows the Subject: Adjective, Emphasis, Apposition and Conjunction",
           "tr": "Müsnedün İleyhten Sonra Gelenler: Sıfat, Te'kîd, Atf-ı Beyân, Bedel ve Atf"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "The body having length, breadth and depth needs a void for it to occupy.",
 "tr": "Uzunluğu, genişliği ve derinliği olan cisim, dolduracağı bir boşluğa muhtaçtır."},
 "tokens": [
  tok("الْجِسْمُ","jism","noun",["mubtada-khabar","tawabi-al-musnad-ilayh","anwa-al-lam-al-tarif"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَ«ال» فِيهِ لَامُ الْجِنْسِ — وَجَاءَتْ بَعْدَهُ الْأَوْصَافُ لِبَيَانِهِ وَكَشْفِ مَعْنَاهُ.",
      "The mubtada, in raf', its «al» the lam of the genus — and the three adjectives after it come to EXPLAIN it, not to pick one body out of many. That is the first of the five reasons for a sifa, and it is the one a definition needs: a body IS what has length, breadth and depth, so the adjectives unfold the word rather than narrow it.",
      "Merfû mübtedâ; «ال»ı cins lâmıdır — ve ardından gelen üç vasıf, birçok cisim arasından birini ayırmak için değil, onu AÇIKLAMAK için gelmiştir. Bu, sıfatın beş sebebinin birincisidir ve bir tarifin muhtaç olduğu sebeptir: cisim, zâten uzunluğu genişliği ve derinliği olan şeydir; öyleyse vasıflar kelimeyi daraltmaz, açar."),
  tok("الطَّوِيلُ","tawil-long","noun",["naat-sifa","tawabi-al-musnad-ilayh"],
      "نَعْتٌ لِـ«الْجِسْمُ» مَرْفُوعٌ — وَالنَّعْتُ يُتْبَعُ مَنْعُوتَهُ فِي أَرْبَعَةٍ مِنْ عَشَرَةٍ: الْإِعْرَابِ وَالتَّعْرِيفِ وَالْإِفْرَادِ وَالتَّذْكِيرِ.",
      "A na't of «the body», in raf' — and a na't follows its noun in four of the ten things a tabi' can agree in: case, definiteness, number and gender. All three adjectives here are definite because the noun is, and that agreement is what tells a na't from a khabar: «الْجِسْمُ طَوِيلٌ» would be a sentence, «الْجِسْمُ الطَّوِيلُ» is not.",
      "«الْجِسْمُ»un merfû na'tı — ve na't, tâbi'in uyabileceği on şeyden DÖRDÜNDE metbûuna uyar: i'râb, ta'rîf, ifrâd ve tezkîr. Buradaki üç sıfat da mevsûf marife olduğu için marifedir; ve na'tı haberden ayıran şey tam bu uyumdur: «الْجِسْمُ طَوِيلٌ» bir cümle olurdu, «الْجِسْمُ الطَّوِيلُ» değildir."),
  tok("الْعَرِيضُ","arid-wide","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ ثَانٍ مَرْفُوعٌ — عَلَى وَزْنِ فَعِيلٍ، وَهُوَ مِنْ أَبْنِيَةِ الصِّفَةِ الْمُشَبَّهَةِ الدَّالَّةِ عَلَى الثُّبُوتِ.",
      "A second na't, in raf' — on فَعِيل, one of the shapes of the sifa mushabbaha, which names a settled quality rather than an act. That matters here: a body's breadth is not something it DOES, and the pattern says so before the meaning does.",
      "İkinci merfû na't — FA'ÎL vezninde; bu, bir fiili değil sâbit bir vasfı bildiren sıfat-ı müşebbehe binâlarındandır. Bu, burada mühimdir: cismin genişliği onun YAPTIĞI bir şey değildir ve vezin bunu mânâdan önce söyler."),
  tok("الْعَمِيقُ","amiq","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ ثَالِثٌ مَرْفُوعٌ — وَتَعَدُّدُ النَّعْتِ لِمَنْعُوتٍ وَاحِدٍ جَائِزٌ بِلَا عَاطِفٍ.",
      "A third na't, in raf' — and several na'ts may stand on one noun with no conjunction between them, which is exactly what happens here. Put a waw between them and the sentence starts claiming they are separate qualities being added up; without it they are one description in three words.",
      "Üçüncü merfû na't — ve bir mevsûfa, aralarında âtıf olmaksızın birden çok na't gelebilir; burada olan da budur. Aralarına vâv konsa cümle, bunların toplanan ayrı vasıflar olduğunu iddia etmeye başlar; vâvsız hâlde ise üç kelimelik tek bir tavsiftir."),
  tok("يَحْتَاجُ","ihtaja","verb",["fa-khabar-mubtada","form-viii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَالْجُمْلَةُ الْفِعْلِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "A mudari' in raf' with a concealed fa'il — and the verbal clause is the khabar of the mubtada, in the position of raf'. Four words of subject and one verb: the weight is at the front because the definition, not the news, is what the sentence is for.",
      "Merfû muzâri fiil; fâili müstetirdir — ve fiil cümlesi, mübtedânın haberi olarak mahallen merfûdur. Dört kelimelik özne, tek fiil: ağırlık öndedir, zira cümlenin maksadı haber değil tariftir."),
  tok("إِلَى","ila","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ.",
      "A jarr letter of the goal's end — and here it is the letter «yahtaju» itself demands: this verb reaches its complement only through إِلَى.",
      "İntihâ-i gāye için cer harfi — ve burada «يَحْتَاجُ»un kendisinin istediği harftir: bu fiil tümlecine ancak «إِلَى» ile ulaşır."),
  tok("فَرَاغٍ","faragh","noun",["huruf-jarr","tankir-al-musnad-ilayh"],
      "مَجْرُورٌ بِـ«إِلَى» — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَحْتَاجُ»، فَهُوَ لَغْوٌ. وَتَنْكِيرُهُ لِلنَّوْعِيَّةِ.",
      "Majrur by «ila» — the phrase attaching to «needs», so it is LAGHW: its governor is written down and it adds no second predication. Its indefiniteness is for KIND, the second reason of chapter 9's list: a void of the sort a body occupies, not any particular one.",
      "«إِلَى» ile mecrûr — câr-mecrûr «يَحْتَاجُ»a taalluk eder, dolayısıyla LAĞVdır: âmili yazılıdır ve ikinci bir isnâd katmaz. Nekreliği NEV'İYYET içindir; dokuzuncu bâbın listesindeki ikinci sebep: muayyen bir boşluk değil, cismin dolduracağı cinsten bir boşluk."),
  tok("يَشْغَلُهُ","shaghala","verb",["jumla-sifa","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، فَاعِلُهُ مُسْتَتِرٌ يَعُودُ عَلَى الْجِسْمِ، وَالْهَاءُ مَفْعُولٌ بِهِ يَعُودُ عَلَى الْفَرَاغِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«فَرَاغٍ».",
      "A mudari' in raf'; its fa'il is concealed and points back at the body, and the ha is its object, pointing back at the void — the clause standing in the position of JARR as an adjective of «a void». A clause describing an INDEFINITE is a sifa; the same clause after a definite would be a hal. That is the whole rule, and this sentence has both a word-adjective and a clause-adjective in it so the two can be compared.",
      "Merfû muzâri fiil; fâili müstetirdir ve cisme râcidir, hâ ise boşluğa râci mef'ûlün bihtir — cümle, «فَرَاغٍ»in sıfatı olarak mahallen MECRÛRdur. NEKREyi niteleyen cümle sıfat, aynı cümle marifeden sonra gelse hâl olurdu. Kāide bundan ibârettir; ve bu cümlede hem kelime-sıfat hem cümle-sıfat bulunduğu için ikisi karşılaştırılabilir.",
      punct=".")],
 "jumal": [
  J("يَحْتَاجُ إِلَى فَرَاغٍ يَشْغَلُهُ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
    "A verbal clause in the position of raf' as the khabar — one of the seven that carry a mahall.",
    "Mübtedânın haberi olarak mahallen merfû fiil cümlesi — mahalli olan yedi cümleden biri."),
  J("يَشْغَلُهُ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«فَرَاغٍ».",
    "A verbal clause in the position of jarr, an adjective of the indefinite before it.",
    "Kendisinden önceki nekrenin sıfatı olarak mahallen mecrûr fiil cümlesi.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "Zayd the merchant is with us. — Zayd the learned came to me. — Zayd the ignorant came to me.",
 "tr": "Tâcir olan Zeyd bizim yanımızdadır. — Bana âlim Zeyd geldi. — Bana câhil Zeyd geldi."},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar","tawabi-al-musnad-ilayh"],
      "مُبْتَدَأٌ مَرْفُوعٌ — عَلَمٌ، وَجَاءَ نَعْتُهُ لِلتَّخْصِيصِ.",
      "The mubtada, in raf' — a proper name, and the na't after it is for NARROWING. A name is already definite, so an adjective on it cannot make it more so; what it does is cut the Zayds down to the one who trades. The books say plainly that this reason works only where the name is shared.",
      "Merfû mübtedâ — alemdir ve ardından gelen na't TAHSÎS içindir. Bir alem zâten marifedir; üzerine gelen sıfat onu daha marife yapamaz. Yaptığı şey, Zeydleri ticaret yapanına indirmektir. Kitaplar, bu sebebin ancak ismin ortak olduğu yerde işlediğini açıkça söyler."),
  tok("التَّاجِرُ","tajir","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«زَيْدٌ» مَرْفُوعٌ — اسْمُ فَاعِلٍ عَلَى فَاعِلٍ مِنْ «تَجَرَ».",
      "A na't of «Zayd», in raf' — an ism fa'il on فَاعِل. The app's peel table used to answer «ا ج ر» for this word on the scale تَفَعَّلَ, reading the article's own alif as a radical and the ta of تَاجِر as an augment; a bare alif is never a first radical, and the row now says so.",
      "«زَيْدٌ»un merfû na'tı — FÂİL vezninde ism-i fâil. Uygulamanın soyma tablosu bu kelimeye «تَفَعَّلَ» vezniyle «ا ج ر» cevabını veriyordu: harf-i ta'rîfin elifini aslî harf, «تَاجِر»in tâsını zâid sayıyordu. Çıplak elif hiçbir zaman fâü'l-fiil olmaz ve satır artık bunu söylüyor."),
  tok("عِنْدَنَا","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ — وَهُوَ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ، ظَرْفٌ مُسْتَقَرٌّ.",
      "A zarf of place in nasb and a mudaf, «na» annexed to it — standing in the position of raf' as the khabar, and MUSTAQARR, since its amil is estimated. عِنْدَ is an ism and not a letter, so the pronoun on it is a mudaf ilayh rather than a majrur by a letter.",
      "Mansub mekân zarfı ve muzâf; «نَا» muzâfun ileyhtir — haber olarak mahallen merfûdur ve âmili takdîr edildiği için MÜSTAKARdır. «عِنْدَ» harf değil isimdir; öyleyse üzerindeki zamir, bir harfle mecrûr değil, muzâfun ileyhtir.",
      segments=[seg("عِنْدَ","inda","noun"), seg("نَا","pron-1p","pron")],
      punct="."),
  jaa(),
  tok("زَيْدٌ","zayd","propn",["fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ — وَجَاءَ نَعْتُهُ لِلْمَدْحِ.",
      "The fa'il, in raf' — and the na't after it is for PRAISE. Note that the syntax has not changed a hair from the sentence before: same case, same agreement, same position. Only the situation is different.",
      "Merfû fâil — ve ardından gelen na't MEDH içindir. Dikkat: nahiv, bir önceki cümleden kıl kadar farklı değildir — aynı hâl, aynı uyum, aynı mevki. Değişen yalnız makāmdır."),
  tok("الْعَالِمُ","alim","noun",["naat-sifa","tawabi-al-musnad-ilayh"],
      "نَعْتٌ مَرْفُوعٌ — لِلْمَدْحِ، وَذَلِكَ حَيْثُ يَكُونُ الْوَصْفُ مَعْلُومًا لِلسَّامِعِ مِنْ قَبْلُ.",
      "A na't in raf', for PRAISE — and the books add the condition that makes it praise rather than narrowing: the hearer must already know Zayd is learned. An adjective that tells him something new is identifying him; one that tells him nothing new is praising him.",
      "Merfû na't; MEDH içindir — ve kitaplar, onu tahsîs değil medh yapan şartı da ekler: muhâtab, Zeyd'in âlim olduğunu önceden biliyor olmalıdır. Ona yeni bir şey söyleyen sıfat tanıtır; hiçbir yeni şey söylemeyen sıfat över.",
      punct="."),
  jaa(),
  tok("زَيْدٌ","zayd","propn",["fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ — وَجَاءَ نَعْتُهُ لِلذَّمِّ.",
      "The fa'il, in raf' — and the na't after it is for BLAME. Three sentences, one grammatical shape, three different acts: narrowing, praise, blame.",
      "Merfû fâil — ve ardından gelen na't ZEMM içindir. Üç cümle, tek bir nahiv şekli, üç ayrı fiil: tahsîs, medh, zemm."),
  tok("الْجَاهِلُ","jahil","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ مَرْفُوعٌ — لِلذَّمِّ، بِالشَّرْطِ نَفْسِهِ.",
      "A na't in raf', for BLAME, on the same condition — the hearer must already know it. If he does not, the word is not blaming Zayd; it is telling the hearer which Zayd came, and the sentence has become a narrowing again.",
      "Merfû na't; aynı şartla ZEMM içindir — muhâtab bunu önceden biliyor olmalıdır. Bilmiyorsa kelime Zeyd'i yermiyordur; muhâtaba hangi Zeyd'in geldiğini söylüyordur ve cümle yine tahsîse dönmüştür.",
      punct=".")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "Yesterday, the one just gone, was a mighty day. — The commander himself cut the thief. — The people came to me, all of them.",
 "tr": "Geçip giden dün, büyük bir gündü. — Hırsızı emîrin bizzat kendisi kesti. — Bana kavim geldi, hepsi."},
 "tokens": [
  tok("أَمْسِ","ams","noun",["mubtada-khabar","tawabi-al-musnad-ilayh"],
      "مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَجَاءَ نَعْتُهُ لِلتَّأْكِيدِ.",
      "Mabni ON THE KASRA, standing in the position of raf' as the mubtada — and the na't after it is the fifth reason: pure CONFIRMATION. «Yesterday» cannot mean any day but the one just gone, so الدَّابِرُ adds no information whatever; it presses the word down, which is what a taʾkīd-adjective is for.",
      "KESRA üzere mebnî; mübtedâ olarak mahallen merfû — ve ardından gelen na't beşinci sebeptir: sırf TE'KÎD. «Dün», geçip gitmiş olandan başka bir gün olamaz; öyleyse «الدَّابِرُ» hiçbir haber katmaz, kelimeyi pekiştirir — te'kîd sıfatının işi de budur."),
  tok("الدَّابِرُ","dabir","noun",["naat-sifa","tawabi-al-musnad-ilayh"],
      "نَعْتٌ فِي مَحَلِّ رَفْعٍ — وَلَمَّا كَانَ الْمَنْعُوتُ مَبْنِيًّا تَبِعَهُ فِي مَحَلِّهِ لَا فِي لَفْظِهِ.",
      "A na't in the position of raf' — and here is the detail worth the whole sentence: أَمْسِ is MABNI, so its na't cannot copy a case-vowel that is not there. It follows the noun's PLACE instead of its letters. A tabi' agrees with what its metbu' actually has.",
      "Mahallen merfû na't — ve bütün cümleye değen incelik şudur: «أَمْسِ» MEBNÎdir; öyleyse na'tı, orada bulunmayan bir i'râb harekesini kopyalayamaz. Kelimenin lafzına değil MAHALLİNE uyar. Tâbi', metbûunun gerçekte sâhib olduğu şeye uyar."),
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","fa-khabar-mubtada"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "An incomplete mazi; its ism is a concealed «he» pointing back at yesterday — and the whole kana-clause is the khabar of the mubtada, in the position of raf'.",
      "Nâkıs mâzî; ismi, düne râci müstetir «هُوَ» zamiridir — ve bütün kâne cümlesi, mübtedânın haberi olarak mahallen merfûdur."),
  tok("يَوْمًا","yawm","noun",["kana-wa-akhawatuha","tankir-al-musnad-ilayh"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ — نَكِرَةٌ.",
      "The khabar of «kana», in nasb — and indefinite, which a khabar may be even where the ism is a definite mabni word.",
      "Mansub «كَانَ» haberi — ve nekredir; ismi marife ve mebnî bir kelime olsa da haberin nekre olması câizdir."),
  tok("عَظِيمًا","azim","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«يَوْمًا» مَنْصُوبٌ — وَهُوَ نَعْتُ نَكِرَةٍ، فَجَاءَ نَكِرَةً مِثْلَهَا.",
      "A na't of «a day», in nasb — the na't of an INDEFINITE, so it is indefinite too. Set this beside الدَّابِرُ four words back: one na't is definite because its noun is, one indefinite because its noun is, and one follows a place rather than a vowel. Three agreements in a single sentence.",
      "«يَوْمًا»ın mansub na'tı — NEKRE na'tıdır, öyleyse kendisi de nekredir. Bunu dört kelime geride duran «الدَّابِرُ» ile yan yana koy: bir na't mevsûfu marife olduğu için marife, biri mevsûfu nekre olduğu için nekre, biri de harekeye değil mahalle uyuyor. Tek cümlede üç uyum.",
      punct="."),
  tok("قَطَعَ","qataa","verb",["fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "A mazi verb, mabni on the fatha. Its object comes BEFORE its doer here, which Arabic allows freely and which is what puts الْأَمِيرُ next to its own taʾkīd at the end of the line.",
      "Fetha üzere mebnî mâzî fiil. Mef'ûlü, fâilinden ÖNCE gelmiştir; Arapça buna serbestçe izin verir ve «الْأَمِيرُ»u mısraın sonunda kendi te'kîdinin yanına getiren de budur."),
  tok("اللِّصَّ","liss","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَهُوَ مُضَاعَفٌ، عَيْنُهُ وَلَامُهُ مِنْ جِنْسٍ وَاحِدٍ (ل ص ص).",
      "The object, in nasb — and a GEMINATE noun: its second and third radicals are the same letter (ل ص ص), written once with a shadda. Strip the harakat and the third radical goes with them, which is why the app's peel table used to answer «ل ل ص» here, reading the article's own lam as a radical. The shadda is now read off the vowelled word before the letters are counted.",
      "Mansub mef'ûlün bih — ve MUZÂAF bir isimdir: ayn'ı ile lâm'ı aynı cinstendir (ل ص ص) ve şedde ile bir kere yazılır. Harekeler soyulunca üçüncü aslî harf de onlarla gider; uygulamanın soyma tablosunun burada «ل ل ص» cevabını vermesinin, yani harf-i ta'rîfin lâmını aslî harf saymasının sebebi buydu. Şedde artık, harfler sayılmadan önce harekeli kelimeden okunuyor."),
  tok("الْأَمِيرُ","amir","noun",["fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ — وَجَاءَ تَوْكِيدُهُ لِدَفْعِ تَوَهُّمِ الْمَجَازِ.",
      "The fa'il, in raf' — and the taʾkīd after it is there to KILL A FIGURE. «The commander cut the thief» is ordinarily read as maja'z aqli: he had it done, by his men. The emphasis forbids that reading and puts the act back in his own hand. Chapter 5 taught the figure; this is the word that refuses it.",
      "Merfû fâil — ve ardından gelen te'kîd, MECÂZ VEHMİNİ DEFETMEK içindir. «Emîr hırsızı kesti» sözü âdeten mecâz-ı aklî okunur: adamlarına yaptırmıştır. Te'kîd bu okuyuşu yasaklar ve fiili onun kendi eline geri koyar. Beşinci bâb mecâzı öğretmişti; bu, onu reddeden kelimedir."),
  tok("نَفْسُهُ","nafs","noun",["tawkid","tawabi-al-musnad-ilayh"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ تَابِعٌ لِـ«الْأَمِيرُ»، وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A MA'NAWI taʾkīd, in raf' following «the commander», a mudaf with the ha annexed to it. The ma'nawi emphasis is a small closed list — نَفْس، عَيْن، كِلَا، كُلّ، جَمِيع، أَجْمَع — and every one of them must carry a pronoun agreeing with what it emphasises. Repeat the word itself instead (الْأَمِيرُ الْأَمِيرُ) and the emphasis is لَفْظِيّ; both are offered in this chapter's own source.",
      "«الْأَمِيرُ»a tâbi, merfû MA'NEVÎ te'kîd; muzâftır ve hâ muzâfun ileyhtir. Ma'nevî te'kîd küçük ve kapalı bir listedir — نَفْس، عَيْن، كِلَا، كُلّ، جَمِيع، أَجْمَع — ve her biri, te'kîd ettiği kelimeye uyan bir zamir taşımak zorundadır. Kelimenin kendisi tekrarlansa (الْأَمِيرُ الْأَمِيرُ) te'kîd LAFZÎ olurdu; bu bâbın kendi kaynağı ikisini de verir.",
      segments=[seg("نَفْسُ","nafs","noun"), seg("هُ","pron-3ms","pron")],
      punct="."),
  jaa(),
  tok("الْقَوْمُ","qawm","noun",["fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ — وَجَاءَ تَوْكِيدُهُ لِدَفْعِ تَوَهُّمِ عَدَمِ الشُّمُولِ.",
      "The fa'il, in raf' — and its taʾkīd is there against a third suspicion: that the statement did not cover everybody. «The people came» leaves room for «most of them», and كُلُّهُمْ shuts it. Four reasons for taʾkīd and three of them are the removal of a particular doubt; the emphasis is aimed, not decorative.",
      "Merfû fâil — ve te'kîdi üçüncü bir vehme karşıdır: hükmün herkesi kapsamadığı vehmi. «Kavim geldi» sözü «çoğu geldi»ye yer bırakır; «كُلُّهُمْ» o yeri kapatır. Te'kîdin dört sebebi vardır ve üçü muayyen bir şüphenin defidir; te'kîd nişan alır, süslemez."),
  tok("كُلُّهُمْ","kull","noun",["tawkid","tawabi-al-musnad-ilayh"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ، مُضَافٌ وَ«هُمْ» مُضَافٌ إِلَيْهِ — وَآخِرُهُ ضَمِيرٌ مَبْنِيٌّ عَلَى السُّكُونِ، فَإِعْرَابُ الْكَلِمَةِ لَا يَظْهَرُ عَلَيْهِ.",
      "A ma'nawi taʾkīd, in raf', a mudaf with «hum» annexed to it — and its last letters are an attached pronoun built on a sukun. That quiescent ending is a BINA and no sign of i'rab: the app read it as jazm until this chapter, which is a case that belongs to verbs and needs a governor, and neither is present. كُلّ is also a geminate (ك ل ل) whose third radical is the shadda.",
      "Merfû ma'nevî te'kîd; muzâftır ve «هُمْ» muzâfun ileyhtir — ve sonu, sükûn üzere mebnî bitişik zamirdir. O sâkin son bir BİNÂdır, i'râb alâmeti değildir: uygulama bu bâba kadar onu cezm okuyordu; oysa cezm fiillere âittir ve bir câzim ister — ikisi de yoktur. «كُلّ» ayrıca muzâaftır (ك ل ل) ve üçüncü aslî harfi şeddededir.",
      segments=[seg("كُلُّ","kull","noun"), seg("هُمْ","pron-3mp","pron")],
      punct=".")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "Your friend Khalid arrived. — Your brother Zayd came to me. — The people came, most of them. — ʿAmr was robbed of his garment.",
 "tr": "Arkadaşın Hâlid geldi. — Bana kardeşin Zeyd geldi. — Kavim geldi, çoğu. — Amr'ın elbisesi soyuldu."},
 "tokens": [
  tok("قَدِمَ","qadima","verb",["fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "A mazi verb, mabni on the fatha.",
      "Fetha üzere mebnî mâzî fiil."),
  tok("صَدِيقُكَ","sadiq","noun",["fail","idafa-definiteness","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَجَاءَ بَعْدَهُ عَطْفُ بَيَانٍ.",
      "The fa'il, in raf' and a mudaf, the kaf annexed to it — and what follows is an ʿATF BAYAN. «Your friend» is definite and still does not say WHICH friend; the name supplies exactly that and nothing else. That is the whole office of the atf bayan: to clarify with a word of its own, where the first word was definite but not clear.",
      "Merfû fâil ve muzâf; kâf muzâfun ileyhtir — ve ardından gelen ATF-I BEYÂNdır. «Arkadaşın» marifedir ve yine de HANGİ arkadaş olduğunu söylemez; isim, tam da bunu ve başka bir şeyi söylemez. Atf-ı beyânın bütün vazifesi budur: birinci kelimenin marife olduğu fakat açık olmadığı yerde, kendine mahsus bir kelimeyle îzâh etmek.",
      segments=[seg("صَدِيقُ","sadiq","noun"), seg("كَ","pron-2ms","pron")]),
  tok("خَالِدٌ","khalid","propn",["atf-bayan","tawabi-al-musnad-ilayh"],
      "عَطْفُ بَيَانٍ مَرْفُوعٌ تَابِعٌ لِـ«صَدِيقُكَ» — وَهُوَ الْجَامِدُ الْمُوَضِّحُ لِمَتْبُوعِهِ.",
      "An ʿatf bayan in raf', following «your friend» — a JAMID noun (a name, not a derived word) that clarifies what it follows. That is the standing test against a na't: a na't is derived and says what its noun is LIKE; an atf bayan is a rigid noun and says which one it IS.",
      "«صَدِيقُكَ»a tâbi merfû atf-ı beyân — metbûunu îzâh eden CÂMİD bir isim (müştak değil, alem). Na'ttan ayıran ölçü de budur: na't müştaktır ve mevsûfunun NASIL olduğunu söyler; atf-ı beyân câmiddir ve HANGİSİ olduğunu söyler.",
      punct="."),
  jaa(),
  tok("أَخُوكَ","akh","noun",["five-nouns","fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ وَالْكَافُ مُضَافٌ إِلَيْهِ — وَجَاءَ بَعْدَهُ بَدَلُ كُلٍّ مِنْ كُلٍّ.",
      "The fa'il, in raf' BY THE WAW because it is one of the five nouns, a mudaf with the kaf annexed to it. Being annexed to something other than the speaker's ya is the very condition the five nouns decline by letters under. What follows is a BADAL KULL: the second word could stand in the first one's place and the sentence would still be complete.",
      "VÂV ile merfû fâil — zira esmâ-i hamseden biridir; muzâftır ve kâf muzâfun ileyhtir. Mütekellim yâsından başka bir şeye muzâf olmak, esmâ-i hamsenin harflerle i'râb aldığı şartın ta kendisidir. Ardından gelen BEDEL-İ KÜLdür: ikinci kelime birincisinin yerine konsa cümle yine tam olurdu.",
      segments=[seg("أَخُو","akh","noun"), seg("كَ","pron-2ms","pron")]),
  tok("زَيْدٌ","zayd","propn",["badal","tawabi-al-musnad-ilayh"],
      "بَدَلُ كُلٍّ مِنْ كُلٍّ مَرْفُوعٌ تَابِعٌ لِـ«أَخُوكَ» — وَالْبَدَلُ لِزِيَادَةِ التَّقْرِيرِ.",
      "A badal kull min kull, in raf', following «your brother» — and the balagha reason the Talkhis gives for every badal is one and the same: ZIYADAT TAQRIR, extra settling. The listener is told the thing twice by two different routes, and the second telling is the one that is meant. Note the case: it copies the WAW's raf' in meaning, not in letter, since زَيْدٌ is not one of the five nouns.",
      "«أَخُوكَ»a tâbi merfû bedel-i kül — ve Telhîs'in her bedel için verdiği belâgat sebebi tektir: ZİYÂDE-İ TAKRÎR, fazladan pekiştirme. Muhâtaba aynı şey iki ayrı yoldan iki kere söylenir ve kastedilen ikincisidir. Hâline dikkat: «زَيْدٌ» esmâ-i hamseden olmadığı için vâvın ref'ine lafzan değil mânen uyar.",
      punct="."),
  tok("جَاءَ","jaa","verb",["fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — بِلَا نُونِ وِقَايَةٍ هُنَا، إِذْ لَا يَاءَ بَعْدَهُ.",
      "A mazi verb, mabni on the fatha — and with NO nun of protection this time, because no speaker's ya follows it. Set it against جَاءَنِي three words back: the nun appears exactly when the ya does, which is the proof that it belongs to neither of them and is put there for the meeting.",
      "Fetha üzere mebnî mâzî fiil — ve bu sefer VİKĀYE NÛNU YOKtur, zira ardından mütekellim yâsı gelmiyor. Üç kelime geride duran «جَاءَنِي» ile karşılaştır: nûn tam da yâ göründüğünde görünür; bu da onun iki taraftan da olmayıp buluşma için konduğunun delilidir."),
  tok("الْقَوْمُ","qawm","noun",["fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ — وَجَاءَ بَعْدَهُ بَدَلُ بَعْضٍ مِنْ كُلٍّ.",
      "The fa'il, in raf' — and what follows is a BADAL BA'D MIN KULL, a part standing for its whole. This is where badal and taʾkīd part company: كُلُّهُمْ in the last sentence covered everybody, أَكْثَرُهُمْ here covers most of them, and the two words sit in the same syntactic seat.",
      "Merfû fâil — ve ardından gelen BEDEL-İ BA'DdIR: bütünün yerine duran bir parça. Bedel ile te'kîdin ayrıldığı yer burasıdır: bir önceki cümlede «كُلُّهُمْ» herkesi kapsıyordu, burada «أَكْثَرُهُمْ» çoğunu kapsar — ve iki kelime aynı nahiv mevkiinde durur."),
  tok("أَكْثَرُهُمْ","akthar","noun",["badal","ism-tafdil"],
      "بَدَلُ بَعْضٍ مِنْ كُلٍّ مَرْفُوعٌ، وَهُوَ مُضَافٌ وَ«هُمْ» مُضَافٌ إِلَيْهِ — وَلَا بُدَّ فِيهِ مِنْ ضَمِيرٍ يَرْجِعُ إِلَى الْمُبْدَلِ مِنْهُ.",
      "A badal ba'd, in raf', a mudaf with «hum» annexed — and this kind of badal MUST carry a pronoun going back to what it replaces. That is the rule that keeps it from being a new subject: the «hum» is the thread. أَكْثَر is also an ism tafdil in idafa, and so wears no tanwin and no article.",
      "Merfû bedel-i ba'd; muzâftır ve «هُمْ» muzâfun ileyhtir — ve bu nevi bedel, mübdelün minhe dönen bir zamir taşımak ZORUNDADIR. Onu yeni bir özne olmaktan alıkoyan kāide budur: «هُمْ» iptir. «أَكْثَر» aynı zamanda izâfetteki bir ism-i tafdîldir; bu yüzden ne tenvîn ne harf-i ta'rîf taşır.",
      segments=[seg("أَكْثَرُ","akthar","noun"), seg("هُمْ","pron-3mp","pron")],
      punct="."),
  tok("سُلِبَ","salaba","verb",["naib-al-fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ.",
      "A mazi built for the PASSIVE — damma on the first letter, kasra on the one before the last, which is the whole rule and is why the app can build this form rather than store it. No noun in Arabic wears فُعِلَ with a bare final fatha, so the shape settles the class by itself.",
      "MECHÛL için binâ edilmiş mâzî — evveli zammelenmiş, âhirinden önceki harf kesralanmıştır; kāide bundan ibârettir ve uygulamanın bu sîgayı saklamak yerine türetebilmesinin sebebi de budur. Arapçada hiçbir isim, sonunda çıplak fetha ile «فُعِلَ» giymez; öyleyse şekil, cinsi kendi başına belirler."),
  tok("عَمْرٌو","amr-alam","propn",["naib-al-fail","tawabi-al-musnad-ilayh"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ — وَالْوَاوُ فِيهِ زَائِدَةٌ لِلْفَرْقِ بَيْنَهُ وَبَيْنَ «عُمَر»، لَا تُنْطَقُ وَلَا تُكْتَبُ فِي النَّصْبِ.",
      "The NA'IB AL-FA'IL, in raf' — the deputy standing where the doer would have stood. Its waw is the WAW OF DISTINCTION: silent, added to tell عَمْرو from عُمَر in an unpointed text, and written in raf' and jarr only — in nasb the alif of the fatha does the distinguishing and the waw is dropped (عَمْرًا). So the tanwin here sits on the ra with a letter still to come, and both of this app's harakat auditors had to be taught the exception.",
      "Merfû NÂİBÜ'L-FÂİL — fâilin duracağı yerde duran vekil. Vâvı FARK VÂVIdır: okunmaz, harekesiz metinde «عَمْرو»yu «عُمَر»den ayırmak için eklenir ve yalnız ref' ile cerde yazılır; nasbda fethanın elifi bu işi görür ve vâv düşer (عَمْرًا). Bu yüzden tenvîn burada, arkasında bir harf dururken râ'nın üzerindedir; ve uygulamanın iki hareke müfettişine de bu istisnâyı öğretmek gerekti."),
  tok("ثَوْبُهُ","thawb","noun",["badal","idafa-definiteness"],
      "بَدَلُ اشْتِمَالٍ مَرْفُوعٌ، مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالضَّمِيرُ رَابِطٌ يَعُودُ عَلَى الْمُبْدَلِ مِنْهُ.",
      "A BADAL ISHTIMAL, in raf', a mudaf with the ha annexed — the pronoun again the thread back to what it replaces. Ishtimal is the third kind: the badal is not the whole of the first word and not a part of it either, but something the first word ENCOMPASSES. A man is not his garment and does not have it as a limb; he has it about him, and it is what was actually taken.",
      "Merfû BEDEL-İ İŞTİMÂL; muzâftır ve hâ muzâfun ileyhtir — zamir yine mübdelün minhe dönen iptir. İştimâl üçüncü nevidir: bedel, birinci kelimenin ne tamamıdır ne de bir parçası; birinci kelimenin KUŞATTIĞI bir şeydir. Bir adam elbisesi değildir ve elbise onun bir uzvu da değildir; onu üzerinde taşır — ve alınan da odur.",
      segments=[seg("ثَوْبُ","thawb","noun"), seg("هُ","pron-3ms","pron")],
      punct=".")],
 "jumal": [
  J("سُلِبَ عَمْرٌو ثَوْبُهُ",
    "جُمْلَةٌ فِعْلِيَّةٌ مَبْنِيَّةٌ لِلْمَجْهُولِ، لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A verbal sentence built for the passive — no position in i'rab. Its deputy-doer carries a badal ishtimal, so the sentence names both the man and the thing that was actually taken.",
    "Mechûl için binâ edilmiş fiil cümlesi — i'râbdan mahalli yoktur. Nâibü'l-fâili bir bedel-i iştimâl taşır; böylece cümle hem adamı hem gerçekten alınan şeyi adlandırır.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "Zayd and ʿAmr came to me. — Zayd came to me, not ʿAmr. — Zayd or ʿAmr came to me.",
 "tr": "Bana Zeyd ile Amr geldi. — Bana Zeyd geldi, Amr değil. — Bana Zeyd yahut Amr geldi."},
 "tokens": [
  jaa(),
  tok("زَيْدٌ","zayd","propn",["fail","tawabi-al-musnad-ilayh"],
      "فَاعِلٌ مَرْفُوعٌ — وَعُطِفَ عَلَيْهِ لِتَفْصِيلِ الْمُسْنَدِ إِلَيْهِ مَعَ اخْتِصَارِ الْمُسْنَدِ.",
      "The fa'il, in raf' — and something is joined to it in order to DETAIL the subject while the predicate is said once. «Came» is uttered a single time and does duty for two men: the economy is in the musnad and the elaboration is in the musnad ilayh, which is exactly how the Talkhis states this reason.",
      "Merfû fâil — ve üzerine atıf yapılmıştır ki müsned bir kere söylenirken müsnedün ileyh TAFSÎL edilsin. «Geldi» tek sefer söylenir ve iki adama yeter: îcâz müsnedde, tafsîl müsnedün ileyhtedir — Telhîs'in bu sebebi ifade edişi tam da budur."),
  tok("وَعَمْرٌو","amr-alam","propn",["atf-nasaq","tawabi-al-musnad-ilayh"],
      "الْوَاوُ عَاطِفَةٌ لِمُطْلَقِ الْجَمْعِ، وَ«عَمْرٌو» مَعْطُوفٌ عَلَى «زَيْدٌ» مَرْفُوعٌ.",
      "The waw joins, for MERE COMBINING and nothing more: it says the two came, not which came first. Replace it with فَ and the second follows immediately on the first; with ثُمَّ and there is a gap; with حَتَّى and the last-named is the extreme of the group. All four are ʿatf, and each adds a different detail to the same joined pair — which is the second reason the book lists.",
      "Vâv âtıfadır ve MUTLAK CEM' içindir, fazlası değil: ikisinin geldiğini söyler, hangisinin önce geldiğini değil. Yerine «فَ» konsa ikincisi birincinin hemen ardından; «ثُمَّ» konsa arada bir aralıkla; «حَتَّى» konsa en sonda anılan, topluluğun uç ferdi olur. Dördü de atıftır ve her biri aynı çifte ayrı bir tafsîl katar — kitabın saydığı ikinci sebep budur.",
      segments=[seg("وَ","wa","conj"), seg("عَمْرٌو","amr-alam","propn")],
      punct="."),
  jaa(),
  tok("زَيْدٌ","zayd","propn",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "The fa'il, in raf' — and this time the joining is a correction, so the first word is the one that is true.",
      "Merfû fâil — ve bu sefer atıf bir tashîhtir; öyleyse doğru olan, birinci kelimedir."),
  tok("لَا","la-atifa","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلنَّفْيِ — تَنْفِي عَنِ الثَّانِي مَا أُثْبِتَ لِلْأَوَّلِ، وَلَا تُسْتَعْمَلُ إِلَّا بَعْدَ إِيجَابٍ.",
      "A LETTER OF CONJUNCTION, and the app's table did not offer this face at all — it read every لَا as a negation or a prohibition. The ʿatif la denies of the second what was affirmed of the first, and it can only be used after an affirmative: «مَا جَاءَنِي زَيْدٌ لَا عَمْرٌو» is not a sentence, because there is nothing affirmed for it to take away.",
      "ATIF HARFİdir ve uygulamanın tablosu bu yüzü hiç sunmuyordu — her «لَا»yı nefiy yahut nehiy okuyordu. Âtıfa lâ, birinciye isbât edileni ikinciden nefyeder ve ancak îcâbdan sonra kullanılır: «مَا جَاءَنِي زَيْدٌ لَا عَمْرٌو» bir cümle değildir, zira kaldıracağı isbât edilmiş bir şey yoktur."),
  tok("عَمْرٌو","amr-alam","propn",["atf-nasaq"],
      "مَعْطُوفٌ عَلَى «زَيْدٌ» مَرْفُوعٌ — وَالْغَرَضُ رَدُّ الْمُخَاطَبِ عَنِ الْخَطَإِ فِي الْحُكْمِ.",
      "Joined to «Zayd» and in raf' — and the purpose is to TURN THE HEARER BACK from a mistake. He believed ʿAmr came, or that both did; the sentence hands him the right name and removes the wrong one in one breath. Nothing here is new information about Zayd; the whole work is done on what the hearer already thought.",
      "«زَيْدٌ»a ma'tûf ve merfû — ve maksad, muhâtabı hükümdeki HATADAN DÖNDÜRMEKtir. O, Amr'ın geldiğine yahut ikisinin birden geldiğine inanıyordu; cümle ona tek nefeste doğru ismi verir ve yanlışını kaldırır. Burada Zeyd hakkında yeni hiçbir haber yoktur; bütün iş, muhâtabın zâten düşündüğü şey üzerinde görülür.",
      punct="."),
  jaa(),
  tok("زَيْدٌ","zayd","propn",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "The fa'il, in raf'.",
      "Merfû fâil."),
  tok("أَوْ","aw","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِأَحَدِ الشَّيْئَيْنِ.",
      "A conjunction naming ONE OF TWO — and it carries the chapter's finest distinction, which is not in the sentence at all. If the speaker does not know which of them came, this is شَكّ, his own doubt. If he knows and says it this way to leave the hearer unsure, it is تَشْكِيك, doubt-making. Two utterly different acts, the same six letters, and only the speaker's state tells them apart.",
      "İki şeyden BİRİNİ bildiren atıf harfi — ve bâbın en ince farkını taşır; o fark ise cümlenin içinde hiç yoktur. Mütekellim hangisinin geldiğini bilmiyorsa bu ŞEKtir, kendi şüphesidir. Biliyor da muhâtabı şüphede bırakmak için böyle söylüyorsa TEŞKÎKtir, şüphelendirmedir. Bütünüyle ayrı iki fiil, aynı üç harf; ve onları yalnız mütekellimin hâli ayırır."),
  tok("عَمْرٌو","amr-alam","propn",["atf-nasaq","tawabi-al-musnad-ilayh"],
      "مَعْطُوفٌ عَلَى «زَيْدٌ» مَرْفُوعٌ.",
      "Joined to «Zayd» and in raf'. The five reasons for ʿatf are now all on the page, and the last of them ends where this whole science does: with a difference that lives in the speaker and the situation rather than in the words. The syntax of all three sentences here is identical.",
      "«زَيْدٌ»a ma'tûf ve merfû. Atfın beş sebebi artık sayfadadır ve sonuncusu, bütün bu ilmin bittiği yerde biter: kelimelerde değil, mütekellim ile makāmda yaşayan bir farkta. Buradaki üç cümlenin nahvi birbirinin aynıdır.",
      punct=".")],
 "jumal": [
  J("جَاءَنِي زَيْدٌ لَا عَمْرٌو",
    "جُمْلَةٌ فِعْلِيَّةٌ مُوجَبَةٌ، وَ«لَا» فِيهَا عَاطِفَةٌ لَا نَافِيَةٌ لِلْجُمْلَةِ.",
    "An AFFIRMATIVE verbal sentence — the la inside it joins, it does not negate the sentence. That is why the sentence would collapse if the verb were negated first.",
    "MÛCEB bir fiil cümlesi — içindeki lâ atfeder, cümleyi nefyetmez. Fiil önce nefyedilse cümlenin yıkılmasının sebebi de budur.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "jism":       g("جِسْم", "ج س م", "noun", "body", "cisim", 2, plural="أَجْسَام"),
 "arid-wide":  g("عَرِيض", "ع ر ض", "noun", "broad, wide", "geniş", 3),
 "amiq":       g("عَمِيق", "ع م ق", "noun", "deep", "derin", 3),
 "faragh":     g("فَرَاغ", "ف ر غ", "noun", "empty space, a void", "boşluk", 3),
 "tajir":      g("تَاجِر", "ت ج ر", "noun", "merchant, trader (ism fa'il)", "tâcir (ism-i fâil)", 2, plural="تُجَّار"),
 "jahil":      g("جَاهِل", "ج ه ل", "noun", "ignorant (ism fa'il)", "câhil (ism-i fâil)", 2),
 "dabir":      g("دَابِر", "د ب ر", "noun", "the one gone by, the last of a thing (ism fa'il)", "geçip giden, sonuncu (ism-i fâil)", 4),
 "liss":       g("لِصّ", "ل ص ص", "noun", "thief", "hırsız", 3, plural="لُصُوص"),
 "amr-alam":   g("عَمْرو", None, "propn", "ʿAmr (a man's name; its waw is silent, written to tell it from عُمَر)", "Amr (bir erkek adı; vâvı okunmaz, «عُمَر»den ayırmak için yazılır)", 1),
 "shaghala":   g("شَغَلَ", "ش غ ل", "verb", "to occupy, to fill", "işgal etmek, doldurmak", 3, form="I"),
 "qataa":      g("قَطَعَ", "ق ط ع", "verb", "to cut, to cut off", "kesmek", 2, form="I"),
 "salaba":     g("سَلَبَ", "س ل ب", "verb", "to strip, to rob of", "soymak, gasbetmek", 3, form="I"),
 "ni-wiqaya":  g("نِي (نُونُ الْوِقَايَةِ + يَاءُ الْمُتَكَلِّمِ)", None, "pron", "…me (the shielding nun + the speaker's ya)", "…beni/bana (vikāye nûnu + mütekellim yâsı)", 3),
 "la-atifa":   g("لَا (الْعَاطِفَة)", None, "conj", "not (joining — denies of the second what was affirmed of the first)", "…değil (âtıfa lâ — birinciye isbât edileni ikinciden nefyeder)", 4),
 "pron-3mp":   g("ـهُمْ", None, "pron", "them, their (attached, masc. pl.)", "onları, onların (muttasıl, cemi müzekker)", 1),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "ihtaja":     g("اِحْتَاجَ", "ح و ج", "verb", "to need, to be in need of", "muhtaç olmak", 3, form="VIII"),
 "qadima":     g("قَدِمَ", "ق د م", "verb", "to arrive, to come", "gelmek, varmak", 2, form="I"),
 "azim":       g("عَظِيم", "ع ظ م", "noun", "mighty, great", "büyük, azîm", 2),
 "qawm":       g("قَوْم", "ق و م", "noun", "a people, a folk", "kavim, topluluk", 2, plural="أَقْوَام"),
 "sadiq":      g("صَدِيق", "ص د ق", "noun", "friend", "arkadaş, dost", 2, plural="أَصْدِقَاء"),
 "khalid":     g("خَالِد", None, "propn", "Khalid (a man's name)", "Hâlid (bir erkek adı)", 1),
 "akh":        g("أَخ", "أ خ و", "noun", "brother (one of the five nouns)", "kardeş (esmâ-i hamseden)", 1, plural="إِخْوَة"),
 "akthar":     g("أَكْثَر", "ك ث ر", "noun", "most of, the greater part (ism tafdil)", "çoğu, ekseri (ism-i tafdîl)", 3),
 "thawb":      g("ثَوْب", "ث و ب", "noun", "garment, robe", "elbise, sevb", 2, plural="ثِيَاب"),
}

def build_morph():
    """Every verb this chapter uses, with its paradigm.

    Four are copied lemma-identical out of packages that already carry them;
    three are new and are built by the generator. قَطَعَ and سَلَبَ are here for a
    second reason as well: without them the analyzer had never met either verb,
    and a bare mazi wears no prefix — so «not a verb» and «I have never heard
    of this word» were the same answer, and both sentences were being read as
    idafas. Growing the corpus IS the fix for that class.
    """
    out = {}
    for pkg, lex in [("aqaid-ahl-al-sunna", "ihtaja"),
                     ("wasiyyat-abi-hanifa-samti", "qadima")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    # شَغَلَ يَشْغَلُ — bab فَتَحَ (its ayn is a throat letter).
    out["shaghala"] = _sg.sound1("fataha", "شَغَل", "شْغَل", "اِشْغَل", "شُغْل", "شَاغِل",
                                 "مَشْغُول", "شُغِلَ", "يُشْغَلُ")
    # قَطَعَ يَقْطَعُ — bab فَتَحَ.
    out["qataa"] = _sg.sound1("fataha", "قَطَع", "قْطَع", "اِقْطَع", "قَطْع", "قَاطِع",
                              "مَقْطُوع", "قُطِعَ", "يُقْطَعُ")
    # سَلَبَ يَسْلُبُ — bab نَصَرَ.
    out["salaba"] = _sg.sound1("nasara", "سَلَب", "سْلُب", "اُسْلُب", "سَلْب", "سَالِب",
                               "مَسْلُوب", "سُلِبَ", "يُسْلَبُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/10.json").write_text(
    json.dumps({"chapter": 10, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 10 for c in man["chapters"]):
    man["chapters"].append({"n": 10, "title": TITLE10})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.10.0"
ADD_EN = (" Chapter 10 continues from the same file (lines ~885-925), which carries every one of its "
          "examples vowelled: الْجِسْمُ الطَّوِيلُ الْعَرِيضُ الْعَمِيقُ, زَيْدٌ التَّاجِرُ عِنْدَنَا, the madh/dhamm pair, "
          "أَمْسِ الدَّابِرُ, قَطَعَ اللِّصَّ الْأَمِيرُ نَفْسُهُ, جَاءَنِي الْقَوْمُ كُلُّهُمْ, قَدِمَ صَدِيقُكَ خَالِدٌ, the three "
          "badal examples and the wa/la/aw triple of the atf section.")
ADD_TR = (" Onuncu bâb aynı dosyadan (satır ~885-925) devam eder; o satırlar bâbın bütün misallerini "
          "harekeli olarak taşır: الْجِسْمُ الطَّوِيلُ الْعَرِيضُ الْعَمِيقُ, زَيْدٌ التَّاجِرُ عِنْدَنَا, medh/zemm çifti, "
          "أَمْسِ الدَّابِرُ, قَطَعَ اللِّصَّ الْأَمِيرُ نَفْسُهُ, جَاءَنِي الْقَوْمُ كُلُّهُمْ, قَدِمَ صَدِيقُكَ خَالِدٌ, üç bedel misali "
          "ve atıf bahsinin vâv/lâ/ev üçlüsü.")
if "885-925" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch10:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
