# -*- coding: utf-8 -*-
"""Author chapter 3 of talkhis-al-miftah — أَضْرُبُ الْخَبَر, the three kinds of
report, and مُقْتَضَى الظَّاهِر.

Chapter 2 ended by splitting all speech into khabar and inshaʾ. This chapter is
the first real chapter of ʿilm al-maʿani, and it is the passage the whole
discipline is famous for: the SAME ruling, said three different ways, and what
decides between them is not the speaker and not the fact — it is **what the
hearer already believes**. Empty-minded, he is told plainly. Hesitating, the
sentence is strengthened once. Denying, it is strengthened as hard as he denies.

That is why balagha is not ornament. The three sentences differ in Arabic and
do not differ in meaning, and the matn's own grammar carries the doctrine: a
verb of RECOMMENDATION with an indefinite instrument (حَسُنَ … بِمُؤَكِّدٍ) against
a verb of OBLIGATION with a proportion (وَجَبَ … بِحَسَبِ الْإِنْكَارِ).

ATTRIBUTION: the received matn of the Talkhis. The supplied Ottoman commentary
(research/sources/talkhis-al-miftah-balagha.txt, lines ~452-470) carries this
passage as Turkish prose with the Arabic EXAMPLES vowelled — زَيْدٌ قَائِمٌ,
إِنَّ زَيْدًا قَائِمٌ, and the two Ya-Sin verses — and names the three kinds in
Arabic. The matn sentences themselves are restored in the wording the tradition
quotes. Nothing here is composed.

Grammar this chapter is chosen to teach:
  • يُلْقَى — a NAQIS majhul in nasb whose fatha is ESTIMATED on an alif. Set
    beside Manar ch15's يَجْرِي (damma estimated on a ya) and ch16's يُفْتِيَ
    (fatha WRITTEN on a ya), the three verbs complete the question: which
    vowel, on which letter, written or estimated.
  • يُسَمَّى … ابْتِدَائِيًّا — a verb of TWO objects built for the unnamed doer:
    one object becomes the naib al-fail and the other STAYS MANSUB. Four times
    in five sentences. A new note.
  • خَالِي الذِّهْنِ — a manqus made mudaf (the ya stands, the kasra is
    estimated) AND an idafa lafziyya, so the phrase is still indefinite enough
    to be what it is. Both notes from chapter 1, in one word.
  • إِخْرَاجُ … إِخْرَاجًا — one masdar twice in one clause, in two cases, as the
    two objects of the same verb.
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

TITLE3 = {"ar": "أَضْرُبُ الْخَبَرِ وَمُقْتَضَى الظَّاهِر",
          "en": "The Three Kinds of Report, and What the Surface Calls For",
          "tr": "Haberin Üç Kısmı ve Muktezâ-yı Zâhir"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "The rule for a report is that it be delivered to a mind empty of it, with no emphasis; and this is called ibtidaʾi.",
 "tr": "Haberde asıl olan, zihni ondan hâlî olana te'kîdsiz olarak söylenmesidir; buna «ibtidâî» denir."},
 "tokens": [
  tok("وَالْأَصْلُ","asl","noun",["mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْأَصْلُ» مُبْتَدَأٌ مَرْفُوعٌ — وَالْأَصْلُ فِي بَابٍ مَا هُوَ الْحَالُ الَّتِي لَا تَحْتَاجُ إِلَى سَبَبٍ، وَمَا سِوَاهَا يُطْلَبُ لَهُ مُقْتَضٍ.",
      "A joining waw, and «the rule» is the mubtada in raf' — and «the aṣl» of a chapter is the state that needs no reason given for it; everything else has to be accounted for. Naming the default first is how a discipline says which of its cases are the ones that need explaining. The word stood in Mukhtasar al-Manar as «the case measured against»; here it is «the unmarked case», and the two senses are one root doing one job.",
      "Atıf vâvı; «الْأَصْل» merfû mübtedâdır — ve bir bâbdaki ASIL, sebep gösterilmesi gerekmeyen hâldir; onun dışındaki her şey için bir muktezî aranır. Önce varsayılanı adlandırmak, bir ilmin hangi hâllerinin izah istediğini söyleyiş biçimidir. Kelime Muhtasaru'l-Menâr'da «kendisine kıyas edilen» idi; burada «işaretlenmemiş hâl»dir ve iki mânâ tek kökün tek işidir.",
      segments=[seg("وَ","wa","conj"), seg("الْأَصْلُ","asl","noun")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْأَصْلُ» — أَيِ الْأَصْلُ ثَابِتًا فِي بَابِ الْخَبَرِ.",
      "A jarr letter attaching to an unsaid word — «the rule, taken IN the chapter of the report». The phrase fences the claim: what follows is the default here and not everywhere.",
      "SÖYLENMEMİŞ bir kelimeye taalluk eden cer harfi — «haber bâbında SÂBİT olmak üzere asıl». İbare iddiayı sınırlar: gelen şey burada asıldır, her yerde değil."),
  tok("الْخَبَرِ","khabar","noun",["huruf-jarr","khabar-insha"],
      "مَجْرُورٌ بِـ«فِي» — وَهُوَ الْمَحْدُودُ فِي آخِرِ الْبَابِ الثَّانِي، فَالْبَابُ يَبْتَدِئُ مِنْ حَيْثُ انْتَهَى الَّذِي قَبْلَهُ.",
      "Majrur by «fi» — the term defined at the end of chapter 2, so this chapter begins exactly where the last one stopped. A matn that defines a word and then spends a chapter on it is not repeating itself; the definition was the entry fee.",
      "«فِي» ile mecrûr — ikinci bâbın sonunda tarif edilen terim; öyleyse bu bâb, bir öncekinin bittiği yerden başlar. Bir kelimeyi tarif edip sonra ona bir bâb ayıran metin kendini tekrarlamıyordur; tarif, giriş bedeliydi."),
  tok("أَنْ","an-nasiba","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِمَّا بَعْدَهُ فِي مَحَلِّ رَفْعٍ خَبَرُ «الْأَصْلُ».",
      "A masdar-making letter putting the verb into nasb, and the masdar it forms stands in the position of raf' as the khabar of «the rule». The default is stated as an ACT — «that it be delivered» — not as a property, which is what lets the next two sentences vary it.",
      "Masdariyye ve nâsıbe harfi; kendisiyle sonrasından çıkan masdar-ı müevvel, «الْأَصْل»un haberi olarak mahallen merfûdur. Asıl, bir vasıf olarak değil bir FİİL olarak konur — «söylenmesi» — ve sonraki iki cümlenin onu değiştirebilmesini sağlayan şey budur."),
  tok("يُلْقَى","alqa","verb",["naib-al-fail","an-masdariyya","naqis-verbs","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى الْخَبَرِ — نَاقِصٌ مِنْ «أَلْقَى».",
      "A mudari built for the unnamed doer, in NASB after «an», and its fatha is ESTIMATED on the alif, which cannot carry one. Set it beside two verbs from the Manar: يَجْرِي had a damma estimated on a ya (too heavy), يُفْتِيَ had a fatha WRITTEN on a ya (light enough). Here the letter is an ALIF, which carries nothing at all, so even the light fatha is estimated. Three verbs, and between them the whole question: which vowel, on which letter, written or supposed.",
      "«أَنْ» ile MANSUB, meçhûl sîgasında muzâri; nasb alâmeti, taşıyamadığı için elif üzerinde MUKADDER fethadır; nâib-i fâili habere râci müstetir zamirdir — «أَلْقَى»dan nâkıs. Menâr'daki iki fiille yan yana koyun: «يَجْرِي»nin dammesi yâ üzerinde mukadderdi (ağır); «يُفْتِيَ»nin fethası yâ üzerinde ZÂHİRdi (yeterince hafif). Burada harf ELİFtir ve hiçbir şey taşımaz; öyleyse hafif fetha bile mukadderdir. Üç fiil ve aralarında meselenin tamamı: hangi hareke, hangi harf üzerinde, zâhir mi mukadder mi."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يُلْقَى» — وَالْإِلْقَاءُ يَتَعَدَّى بِإِلَى إِلَى الْمُلْقَى إِلَيْهِ.",
      "A jarr letter attaching to «be delivered» — إِلْقَاء reaches the one delivered TO through an ila. The person is named by a preposition and never by the verb directly, which is a small sign that this chapter is about the hearer.",
      "«يُلْقَى»a taalluk eden cer harfi — «ilkā», kendisine ilkā edilene «إِلَى» ile ulaşır. Kişi, fiille değil bir harf-i cerle anılır; bu, bu bâbın muhâtab üzerine olduğunun küçük bir işaretidir."),
  tok("خَالِي","khali","noun",["huruf-jarr","ism-maqsur-manqus","idafa-lafziyya","ism-fail","idafa-definiteness"],
      "مَجْرُورٌ بِـ«إِلَى» وَعَلَامَةُ جَرِّهِ كَسْرَةٌ مُقَدَّرَةٌ عَلَى الْيَاءِ لِلثِّقَلِ، وَهُوَ مُضَافٌ — مَنْقُوصٌ ثَبَتَتْ يَاؤُهُ لِلْإِضَافَةِ، وَالْإِضَافَةُ لَفْظِيَّةٌ لِأَنَّهُ اسْمُ فَاعِلٍ أُضِيفَ إِلَى فَاعِلِهِ فَلَا تُفِيدُ تَعْرِيفًا.",
      "Majrur by «ila» with a kasra ESTIMATED on the ya for heaviness, and a mudaf — a manqus whose ya STANDS because it is annexed (indefinite it would have been خَالٍ, ya gone, tanwin in its place). And the annexation is LAFZIYYA: an ism fa'il joined to its own fa'il, so nothing is made definite. Chapter 1 taught both rules; this one word runs them at the same time.",
      "«إِلَى» ile mecrûr; cer alâmeti sıklet sebebiyle yâ üzerinde MUKADDER kesradır ve muzâftır — izâfet sebebiyle yâsı DURAN bir menkūs (nekre olsaydı «خَالٍ» olur, yâ düşer, yerine tenvin gelirdi). Ve izâfet LAFZİYYEdir: kendi fâiline izâfe edilmiş ism-i fâil; hiçbir şeyi marife yapmaz. Birinci bâb her iki kâideyi de öğretti; bu tek kelime ikisini birden çalıştırır."),
  tok("الذِّهْنِ","dhihn","noun",["idafa-definiteness","idafa-lafziyya"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فَاعِلُ «خَالِي» مَعْنًى: الذِّهْنُ هُوَ الَّذِي يَخْلُو.",
      "The mudaf ilayh in jarr — and the fa'il of «empty» in meaning: it is the MIND that is empty. What the whole discipline turns on is named here for the first time, and it is not the sentence and not the speaker.",
      "Mecrûr muzâfun ileyh — ve mânen «خَالِي»nin fâilidir: hâlî olan ZİHİNdir. Bütün ilmin üzerinde döndüğü şey burada ilk defa anılır ve o, ne cümledir ne de mütekellim."),
  tok("بِلَا","bila","prep",["huruf-jarr","huruf-jarr-nawadir"],
      "الْبَاءُ حَرْفُ جَرٍّ وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يُلْقَى» — وَالْمَعْنَى: خَالِيًا مِنَ التَّأْكِيدِ.",
      "The ba is a jarr letter and «la» rides on it to negate; together they mean «without», and the phrase hangs on «be delivered». Two letters written apart and read as one word — the sort of thing a parser must be told rather than left to work out.",
      "Bâ cer harfidir, «لَا» ise nefyi te'kîd için ona binmiştir; ikisi birlikte «-sız» mânâsı verir ve ibare «يُلْقَى»a taalluk eder. Ayrı yazılıp tek kelime gibi okunan iki harf — bir tahlîl motoruna söylenmesi gereken, kendi başına çıkarması beklenmeyecek türden bir şey.",
      segments=[seg("بِ","bi","prep"), seg("لَا","la-nafiya","part")]),
  tok("تَأْكِيدٍ","takid","noun",["huruf-jarr","masdar","form-ii-verbs"],
      "مَجْرُورٌ بِـ«بِلَا» — مَصْدَرُ «أَكَّدَ» عَلَى تَفْعِيلٍ، وَتَنْكِيرُهُ فِي سِيَاقِ النَّفْيِ يُفِيدُ الْعُمُومَ: لَا تَأْكِيدَ أَصْلًا.",
      "Majrur by «bila» — the Form II masdar of أَكَّدَ, and an indefinite inside a negation is GENERAL: no emphasis of any kind. The next sentence will make it definite in number — one emphasiser — and the one after that will make it proportional. Watch the same noun get counted three different ways in three lines.",
      "«بِلَا» ile mecrûr — «أَكَّدَ»nin TEF'ÎL vezninde masdarı; ve nefiy siyâkında nekre UMÛM ifade eder: hiçbir te'kîd yok. Bir sonraki cümle onu sayıca belirleyecek — bir te'kîd — ondan sonraki ise nisbetlendirecek. Aynı ismin üç satırda üç ayrı şekilde sayıldığına dikkat edin."),
  tok("وَيُسَمَّى","samma","verb",["naib-al-fail","mafulayn","naqis-verbs","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«يُسَمَّى» فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ.",
      "A joining waw, and «is called» a mudari for the unnamed doer, in raf' by a damma estimated on the alif, its naib al-fa'il a hidden pronoun. سَمَّى takes TWO objects; built for the unnamed doer, the first becomes the deputy subject and the second — the name itself — has to stay where it was.",
      "Atıf vâvı; «يُسَمَّى» meçhûl sîgasında muzâri, elif üzerinde mukadder damme ile merfûdur; nâib-i fâili müstetir zamirdir. «سَمَّى» İKİ mef'ûl alır; meçhûle bina edildiğinde birincisi nâib-i fâil olur, ikincisi — yani ismin kendisi — bulunduğu yerde kalmak zorundadır.",
      segments=[seg("وَ","wa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("ابْتِدَائِيًّا","ibtidai","noun",["mafulayn","maful-bihi"],
      "الْمَفْعُولُ الثَّانِي لِـ«يُسَمَّى» مَنْصُوبٌ بِالْفَتْحَةِ — بَقِيَ عَلَى نَصْبِهِ لِأَنَّ نَائِبَ الْفَاعِلِ قَدْ أَخَذَهُ الْأَوَّلُ. اسْمٌ مَنْسُوبٌ إِلَى الِابْتِدَاءِ.",
      "The SECOND object of «is called», in nasb by the fatha — it kept its nasb because the first object had already taken the deputy's place. A verb of two objects surrenders only one of them to the passive; the other is untouched, and the fatha here is the visible proof. A nisba noun built on «beginning»: the plain opening, before anyone has objected to anything.",
      "«يُسَمَّى»nin İKİNCİ mef'ûlü, fetha ile mansub — nasbını korumuştur, zira nâib-i fâil mevkiini birinci mef'ûl almıştır. İki mef'ûllü bir fiil, meçhûle bina edildiğinde bunlardan yalnız birini teslim eder; öteki el değmemiş kalır ve buradaki fetha bunun gözle görülür ispatıdır. «İbtidâ»ya nisbet edilmiş isim: kimse bir şeye itiraz etmeden önceki sade açılış.",
      punct="."),
 ],
 "jumal": [J("أَنْ يُلْقَى إِلَى خَالِي الذِّهْنِ بِلَا تَأْكِيدٍ",
   "الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ «الْأَصْلُ».",
   "The masdar muawwal, in the position of raf' as the khabar of «the rule».",
   "Masdar-ı müevvel, «الْأَصْل»un haberi olarak mahallen merfûdur."),
  J("وَيُسَمَّى ابْتِدَائِيًّا",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined verbal clause, with no position in i'rab.",
   "Ma'tûf fiil cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "But if he is hesitating about it and seeking it, it is GOOD to strengthen it with one emphasiser; and this is called talabi.",
 "tr": "Fakat muhâtab onda tereddüd eder ve onu taleb ederse, bir te'kîdle kuvvetlendirilmesi GÜZEL olur; buna «talebî» denir."},
 "tokens": [
  tok("فَإِنْ","in-shartiyya","part",["in-shartiyya"],
      "الْفَاءُ لِلتَّفْصِيلِ، وَ«إِنْ» حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ.",
      "The fa opens the detailing, and «in» is a conditional LETTER that puts two verbs into jazm. Note that the matn does not say «and if»; it says «but if» — the fa marks that what follows is a departure from the rule just stated, not a second rule beside it.",
      "Fâ tafsîl içindir; «إِنْ» ise iki fiili cezmeden şart HARFİdir. Metnin «ve eğer» demediğine, «fakat eğer» dediğine dikkat: fâ, gelenin yeni bir kâide değil, az önce konan asıldan bir ayrılış olduğunu gösterir.",
      segments=[seg("فَ","fa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","in-shartiyya","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» عَائِدٌ عَلَى الْمُخَاطَبِ — وَالْمَاضِي مَبْنِيٌّ، فَجَزْمُهُ مَحَلِّيٌّ لَا لَفْظِيٌّ.",
      "An incomplete mazi standing in the POSITION of jazm as the condition's verb, its ism a hidden «he» going back to the hearer — and a mazi is mabni, so its jazm is by POSITION only and nothing on the letters shows it. A governor may rule a word that cannot display the ruling; that is what mahalli i'rab is for.",
      "Şartın fiili olarak MAHALLEN MECZÛM nâkıs mâzî; ismi, muhâtaba râci müstetir «هُوَ»dur — ve mâzî mebnîdir; öyleyse cezmi lafzî değil MAHALLÎdir, harflerde hiçbir iz bırakmaz. Bir âmil, hükmünü gösteremeyen bir kelimeye de hükmedebilir; mahallî i'râb tam da bunun içindir."),
  tok("مُتَرَدِّدًا","mutaraddid","noun",["kana-wa-akhawatuha","ism-fail","form-v-verbs"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «تَرَدَّدَ» عَلَى مُتَفَعِّلٍ، وَبِنَاءُ التَّفَعُّلِ لِلتَّكَلُّفِ وَالتَّكْرَارِ: الذِّهْنُ يَذْهَبُ وَيَعُودُ.",
      "The khabar of «kana», in nasb — the ism fa'il of تَرَدَّدَ on مُتَفَعِّل, and Form V carries repetition: the mind goes and comes back and goes again. The pattern is doing the psychology, and the word could not have been replaced by a simple شَاكّ without losing it.",
      "«كَانَ»nin mansub haberi — «تَرَدَّدَ»nin MÜTEFA'İL vezninde ism-i fâili; ve tefe''ul kalıbı tekrar ifade eder: zihin gider, döner, yine gider. Psikolojiyi yapan şey vezindir; kelimenin yerine sade bir «شَاكّ» konsaydı bu kaybolurdu."),
  tok("فِيهِ","fi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«مُتَرَدِّدًا» — وَتَعَلُّقُ الْجَارِّ بِاسْمِ الْفَاعِلِ دَلِيلٌ عَلَى عَمَلِهِ عَمَلَ فِعْلِهِ.",
      "A jarr-majrur attaching to «hesitating» — and a jarr phrase hanging on an ism fa'il is one more sign that a participle works exactly as its verb does. The same doctrine the Manar's بَذْلُ الْفَقِيهِ showed for a masdar.",
      "«مُتَرَدِّدًا»a taalluk eden câr-mecrûr — ve bir câr-mecrûrun ism-i fâile taalluk etmesi, sıfatın fiilinin amelini yaptığının bir başka delilidir. Menâr'ın «بَذْلُ الْفَقِيهِ»inin masdar için gösterdiği doktrinin aynısı.",
      segments=[seg("فِي","fi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("طَالِبًا","talib","noun",["kana-wa-akhawatuha","ism-fail","atf-nasaq"],
      "خَبَرٌ ثَانٍ لِـ«كَانَ» مَنْصُوبٌ، أَوْ حَالٌ — وَالْقَيْدُ لَازِمٌ: الْمُتَرَدِّدُ الَّذِي لَا يَطْلُبُ لَا يُقَوَّى لَهُ الْكَلَامُ، لِأَنَّهُ غَيْرُ مُنْتَظِرٍ لِلْجَوَابِ.",
      "A SECOND khabar of «kana», in nasb, or a hal — and the restriction is doing real work: a man who is unsure but not ASKING is not given a strengthened sentence, because he is not waiting for one. Two conditions, both required, and the second is the one people forget.",
      "«كَانَ»nin İKİNCİ mansub haberi yahut hâl — ve kayıt gerçek bir iş görür: tereddüd edip de TALEB ETMEYEN kimseye kelâm kuvvetlendirilmez, zira cevap beklemiyordur. İki şart, ikisi de lâzım; unutulanı ikincisidir."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«طَالِبًا».",
      "A jarr-majrur attaching to «seeking».",
      "«طَالِبًا»a taalluk eden câr-mecrûr.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("حَسُنَ","hasuna","verb",["in-shartiyya","fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، مِنْ بَابِ حَسُنَ يَحْسُنُ — وَهُوَ بَابُ الْأَوْصَافِ الثَّابِتَةِ.",
      "A mazi on the fatha, standing in the position of jazm as the ANSWER to the condition, from the bab of حَسُنَ — the bab of settled qualities. And the choice of verb is the ruling: it is GOOD to strengthen here, not required. Hold that word until the next sentence.",
      "Fetha üzere mebnî mâzî; şartın CEVÂBI olarak mahallen meczûm; «حَسُنَ يَحْسُنُ» bâbından — sâbit vasıflar bâbı. Ve fiilin seçimi hükmün kendisidir: burada kuvvetlendirmek GÜZELdir, vâcib değil. Bu kelimeyi bir sonraki cümleye kadar aklınızda tutun."),
  tok("تَقْوِيَتُهُ","taqwiya","noun",["fail","masdar","form-ii-verbs","idafa-definiteness"],
      "فَاعِلُ «حَسُنَ» مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ مَفْعُولُ الْمَصْدَرِ مَعْنًى — مَصْدَرُ «قَوَّى» عَلَى تَفْعِلَةٍ، وَهِيَ صِيغَةُ التَّفْعِيلِ مِنَ النَّاقِصِ.",
      "The fa'il of «is good», in raf' and a mudaf, the ha its mudaf ilayh and the masdar's OBJECT in meaning — the Form II masdar of قَوَّى on تَفْعِلَة, which is what تَفْعِيل becomes when the last radical is weak (تَقْوِيَة, not *تَقْوِيّ). Another masdar annexed to what it works on, and the third the reader has met in this book.",
      "«حَسُنَ»nin merfû fâili ve muzâf; hâ muzâfun ileyhtir ve mânen masdarın MEF'ÛLÜdür — «قَوَّى»nin TEF'İLE vezninde masdarı; son harfi illetli olduğunda «tef'îl»in aldığı şekildir (تَقْوِيَة, «تَقْوِيّ» değil). Mef'ûlüne izâfe edilmiş bir masdar daha; okuyucunun bu kitapta gördüğü üçüncüsü.",
      segments=[seg("تَقْوِيَتُ","taqwiya","noun"), seg("هُ","pron-3ms","pron")]),
  tok("بِمُؤَكِّدٍ","muakkid","noun",["huruf-jarr","ism-fail","form-ii-verbs"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«تَقْوِيَتُهُ» — اسْمُ فَاعِلٍ مِنْ «أَكَّدَ»، وَتَنْكِيرُهُ مَقْصُودٌ: بِمُؤَكِّدٍ وَاحِدٍ، لَا أَكْثَرَ.",
      "A jarr-majrur attaching to «strengthening it» — the ism fa'il of أَكَّدَ, and the indefinite is exact: with ONE emphasiser, no more. Chapter 1's تَأْكِيدٍ was indefinite for GENERALITY inside a negation; this one is indefinite for SINGULARITY inside an affirmation. Same tanwin, opposite work, two sentences apart.",
      "«تَقْوِيَتُهُ»a taalluk eden câr-mecrûr — «أَكَّدَ»nin ism-i fâili; ve nekreliği tamdır: BİR te'kîdle, fazlası değil. Birinci cümledeki «تَأْكِيدٍ» nefiy içinde UMÛM için nekreydi; bu ise îcâb içinde TEKLİK için nekredir. Aynı tenvin, zıt vazife, iki cümle arayla.",
      segments=[seg("بِ","bi","prep"), seg("مُؤَكِّدٍ","muakkid","noun")]),
  tok("وَيُسَمَّى","samma","verb",["naib-al-fail","mafulayn","naqis-verbs","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«يُسَمَّى» مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.",
      "A joining waw, and «is called» again — the same verb, the same estimated damma, the same hidden deputy, and one more noun about to keep its fatha. Three sentences, one formula: state the hearer's condition, state the ruling, then name the kind.",
      "Atıf vâvı; «يُسَمَّى» yine meçhûl sîgasında, mukadder damme ile merfû muzâri; nâib-i fâili müstetirdir. Üç cümle, tek kalıp: muhâtabın hâlini söyle, hükmü söyle, sonra kısmı adlandır.",
      segments=[seg("وَ","wa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("طَلَبِيًّا","talabi","noun",["mafulayn","maful-bihi"],
      "الْمَفْعُولُ الثَّانِي مَنْصُوبٌ — اسْمٌ مَنْسُوبٌ إِلَى الطَّلَبِ، وَالتَّسْمِيَةُ مِنْ حَالِ السَّامِعِ لَا مِنْ صِيغَةِ الْكَلَامِ.",
      "The second object, in nasb — a nisba noun built on «seeking», and note where the NAME comes from: the hearer's state, not the sentence's form. إِنَّ زَيْدًا قَائِمٌ is talabi when a hesitating man hears it and inkari when a denier does. The same Arabic gets two different names, which is precisely what makes this a science of situations.",
      "İkinci mef'ûl, mansub — «taleb»e nisbet edilmiş isim; ve ADIN nereden geldiğine dikkat: kelâmın sîgasından değil, dinleyenin hâlinden. «إِنَّ زَيْدًا قَائِمٌ», tereddüd eden işitince talebî, inkâr eden işitince inkârîdir. Aynı Arapça iki ayrı ad alır — bunu bir hâller ilmi yapan şey tam da budur.",
      punct="."),
 ],
 "jumal": [J("إِنْ كَانَ مُتَرَدِّدًا فِيهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.",
   "A verbal clause in the position of jazm, the verb of the condition.",
   "Şartın fiili olarak mahallen meczûm fiil cümlesi."),
  J("حَسُنَ تَقْوِيَتُهُ بِمُؤَكِّدٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
   "A verbal clause in the position of jazm, the answer to the condition.",
   "Şartın cevâbı olarak mahallen meczûm fiil cümlesi.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "And if he is denying it, emphasising it is OBLIGATORY, in proportion to the denial; and this is called inkari.",
 "tr": "Eğer muhâtab inkâr ediyorsa, inkârın derecesine göre te'kîd VÂCİBtir; buna «inkârî» denir."},
 "tokens": [
  tok("وَإِنْ","in-shartiyya","part",["in-shartiyya"],
      "الْوَاوُ عَاطِفَةٌ، وَ«إِنْ» شَرْطِيَّةٌ جَازِمَةٌ — وَالتَّرْكِيبُ نَفْسُهُ لِلْمَرَّةِ الثَّانِيَةِ، لِيَقَعَ الْفَرْقُ فِي الْجَوَابِ وَحْدَهُ.",
      "A joining waw and the same conditional letter — the SAME construction a second time, so that the difference falls entirely in the answer. When a matn repeats a frame word for word, it is telling you to read only what changed.",
      "Atıf vâvı ve aynı şart harfi — İKİNCİ defa aynı terkîb; böylece fark yalnız cevapta kalır. Bir metin bir kalıbı kelimesi kelimesine tekrar ediyorsa, size yalnız değişeni okumanızı söylüyordur.",
      segments=[seg("وَ","wa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","in-shartiyya","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ.",
      "An incomplete mazi in the position of jazm as the condition's verb, its ism hidden.",
      "Şartın fiili olarak mahallen meczûm nâkıs mâzî; ismi müstetirdir."),
  tok("مُنْكِرًا","munkir","noun",["kana-wa-akhawatuha","ism-fail","form-iv-verbs"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «أَنْكَرَ» عَلَى مُفْعِلٍ، وَلَمْ يُقَيَّدْ بِشَيْءٍ: الْمُنْكِرُ لَا يُشْتَرَطُ فِيهِ طَلَبٌ، لِأَنَّهُ لَا يَطْلُبُ.",
      "The khabar of «kana», in nasb — the ism fa'il of أَنْكَرَ on مُفْعِل, and it carries NO second condition. The hesitating man had to be seeking as well; the denier is not asked to seek anything, because a denier by definition is not asking. The missing restriction is the argument.",
      "«كَانَ»nin mansub haberi — «أَنْكَرَ»nin MUF'İL vezninde ism-i fâili; ve HİÇBİR ikinci kayıt taşımaz. Tereddüd edenin ayrıca taleb etmesi gerekiyordu; inkâr edenden bir şey talebi istenmez, zira inkâr eden tarifi gereği taleb etmiyordur. Delîl, eksik olan kayıttır."),
  tok("وَجَبَ","wajaba","verb",["in-shartiyya","fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ — وَبَيْنَهُ وَبَيْنَ «حَسُنَ» فِي الْجُمْلَةِ السَّابِقَةِ فَرْقُ الْحُكْمِ كُلُّهُ.",
      "A mazi on the fatha, in the position of jazm as the answer — and between this verb and «is good» in the sentence before lies the entire difference of ruling. The matn did not write «and it is likewise good»; it changed the verb, and the change is the doctrine. A reader who skims past a verb here has missed the chapter.",
      "Fetha üzere mebnî mâzî; şartın cevâbı olarak mahallen meczûm — ve bu fiil ile bir önceki cümledeki «حَسُنَ» arasında hükmün bütün farkı yatar. Metin «o da güzeldir» demedi; fiili değiştirdi ve değişikliğin kendisi doktrindir. Buradaki fiilin üzerinden atlayan okuyucu bâbı kaçırmıştır."),
  tok("تَوْكِيدُهُ","tawkid","noun",["fail","masdar","form-ii-verbs","idafa-definiteness"],
      "فَاعِلُ «وَجَبَ» مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مَفْعُولُهُ مَعْنًى — مَصْدَرُ «وَكَّدَ» عَلَى تَفْعِيلٍ مِنْ مِثَالٍ وَاوِيٍّ، وَالْوَاوُ ثَابِتَةٌ لِأَنَّ الْفَتْحَةَ قَبْلَهَا.",
      "The fa'il of «is obligatory», in raf' and a mudaf, the ha its object in meaning — the Form II masdar of وَكَّدَ from a waw-initial root, and the waw STANDS because a fatha precedes it. Compare the Manar's إِيجَاب, where the same waw turned into a ya under a kasra. One weak letter, and the vowel in front of it decides everything.",
      "«وَجَبَ»nin merfû fâili ve muzâf; hâ mânen mef'ûlüdür — misâl-i vâvîden TEF'ÎL vezninde «وَكَّدَ»nin masdarı; ve vâv DURUR, çünkü öncesinde fetha vardır. Menâr'ın «إِيجَاب»ıyla karşılaştırın: orada aynı vâv kesra altında yâya dönmüştü. Tek illetli harf ve her şeyi önündeki hareke tayin eder.",
      segments=[seg("تَوْكِيدُ","tawkid","noun"), seg("هُ","pron-3ms","pron")]),
  tok("بِحَسَبِ","hasab","noun",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«تَوْكِيدُهُ»، وَ«حَسَبِ» مُضَافٌ — أَيْ عَلَى قَدْرِهِ.",
      "A jarr-majrur attaching to «emphasising it», and «the measure of» is a mudaf — «in proportion to». Where the previous sentence named a QUANTITY (one emphasiser), this one names a RATIO, and a ratio has no ceiling: the Yasin verses answer a first denial with إِنَّا and a second with رَبُّنَا يَعْلَمُ إِنَّا … لَمُرْسَلُونَ.",
      "«تَوْكِيدُهُ»a taalluk eden câr-mecrûr; «حَسَبِ» muzâftır — «-in derecesine göre». Bir önceki cümle bir MİKTAR anmıştı (bir te'kîd), bu ise bir NİSBET anar ve nisbetin tavanı yoktur: Yâsîn âyetleri ilk yalanlamaya «إِنَّا» ile, ikincisine «رَبُّنَا يَعْلَمُ إِنَّا ... لَمُرْسَلُونَ» ile cevap verir.",
      segments=[seg("بِ","bi","prep"), seg("حَسَبِ","hasab","noun")]),
  tok("الْإِنْكَارِ","inkar","noun",["idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «أَنْكَرَ» عَلَى إِفْعَالٍ، وَهُوَ الِاسْمُ الَّذِي اشْتُقَّ مِنْهُ «مُنْكِرًا» أَوَّلَ الْجُمْلَةِ وَ«إِنْكَارِيًّا» آخِرَهَا.",
      "The mudaf ilayh in jarr — the Form IV masdar of أَنْكَرَ, and the same root stands three times in one sentence: as the participle that names the hearer, as the masdar that measures the emphasis, and as the nisba that names the kind. A sentence built on one root is a sentence that has decided what it is about.",
      "Mecrûr muzâfun ileyh — «أَنْكَرَ»nin İF'ÂL vezninde masdarı; ve aynı kök tek cümlede üç defa durur: muhâtabı adlandıran ism-i fâil, te'kîdi ölçen masdar ve kısmı adlandıran nisbet. Tek kök üzerine kurulmuş bir cümle, neden bahsettiğine karar vermiş bir cümledir."),
  tok("وَيُسَمَّى","samma","verb",["naib-al-fail","mafulayn","naqis-verbs","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«يُسَمَّى» مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.",
      "A joining waw, and «is called» for the third time — the formula closes each of the three cases, and the reader who has met it twice now reads it as punctuation.",
      "Atıf vâvı; «يُسَمَّى» üçüncü defa — kalıp, üç hâlin her birini kapatır; iki defa gören okuyucu onu artık noktalama gibi okur.",
      segments=[seg("وَ","wa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("إِنْكَارِيًّا","inkari","noun",["mafulayn","maful-bihi"],
      "الْمَفْعُولُ الثَّانِي مَنْصُوبٌ — وَبِهِ تَمَّتِ الْأَضْرُبُ الثَّلَاثَةُ.",
      "The second object, in nasb — and with it the three kinds are complete. Three sentences, one shape, three verbs of ruling: none, good, obligatory. The grammar and the doctrine are the same three steps.",
      "İkinci mef'ûl, mansub — ve onunla üç kısım tamamlanır. Üç cümle, tek kalıp, üç hüküm fiili: yok, güzel, vâcib. Gramer ile doktrin aynı üç basamaktır.",
      punct="."),
 ],
 "jumal": [J("وَجَبَ تَوْكِيدُهُ بِحَسَبِ الْإِنْكَارِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
   "A verbal clause in the position of jazm, the answer to the condition.",
   "Şartın cevâbı olarak mahallen meczûm fiil cümlesi.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "And putting speech out along these lines is called putting it out according to what the surface calls for.",
 "tr": "Kelâmı bu vecihler üzere söylemeye, «muktezâ-yı zâhir üzere söylemek» denir."},
 "tokens": [
  tok("وَيُسَمَّى","samma","verb",["naib-al-fail","mafulayn","naqis-verbs","form-ii-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«يُسَمَّى» مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — وَنَائِبُ الْفَاعِلِ هُنَا مَذْكُورٌ لَا مُسْتَتِرٌ، وَهُوَ الْآتِي بَعْدَهُ.",
      "A resuming waw, and «is called» a fourth time — but here the deputy subject is WRITTEN rather than hidden, and it is the noun that follows. Same verb, same voice, and the reader can now see both ways its first object can be filled.",
      "İsti'nâf vâvı; «يُسَمَّى» dördüncü defa — fakat burada nâib-i fâil müstetir değil ZÂHİRdir ve ardından gelen isimdir. Aynı fiil, aynı sîga; okuyucu artık birinci mef'ûlün doldurulmasının her iki yolunu da görmüştür.",
      segments=[seg("وَ","wa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("إِخْرَاجُ","ikhraj","noun",["naib-al-fail","masdar","form-iv-verbs","idafa-definiteness"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «أَخْرَجَ» عَلَى إِفْعَالٍ.",
      "The naib al-fa'il in raf' and a mudaf — the Form IV masdar of أَخْرَجَ. «Putting speech out» is the tradition's own image for the act of composing: the meaning is inside, and the shape it is sent out in is what this discipline studies.",
      "Merfû nâib-i fâil ve muzâf — «أَخْرَجَ»nin İF'ÂL vezninde masdarı. «Kelâmı çıkarmak», geleneğin telif fiili için kendi tasviridir: mânâ içeridedir ve dışarı hangi şekilde gönderildiği, bu ilmin incelediği şeydir."),
  tok("الْكَلَامِ","kalam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ مَفْعُولُ الْمَصْدَرِ مَعْنًى.",
      "The mudaf ilayh in jarr — and the masdar's object in meaning: what is put out is the speech.",
      "Mecrûr muzâfun ileyh — ve mânen masdarın mef'ûlüdür: çıkarılan şey kelâmdır."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«إِخْرَاجُ».",
      "A jarr letter attaching to «putting out».",
      "«إِخْرَاجُ»a taalluk eden cer harfi."),
  tok("هَذِهِ","hadhihi","pron",["idafa-definiteness"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَهُوَ مُضَافٌ فِي الْمَعْنَى إِلَى مَا بَعْدَهُ عَلَى الْبَدَلِ — وَالْمُشَارُ إِلَيْهِ الْأَضْرُبُ الثَّلَاثَةُ الْمَذْكُورَةُ.",
      "A demonstrative, fixed in form, in the position of jarr — and what it points at is the three kinds just named. A demonstrative reaching back over three sentences is the matn's way of saying «all of that, together»; nothing else in Arabic gathers a list that cheaply.",
      "Mebnî ism-i işaret, mahallen mecrûr — ve işaret ettiği şey, az önce anılan üç kısımdır. Üç cümle geriye uzanan bir ism-i işaret, metnin «bütün bunlar, hepsi birden» deyiş biçimidir; Arapçada bir listeyi bu kadar ucuza toplayan başka bir şey yoktur."),
  tok("الْوُجُوهِ","wajh","noun",["badal"],
      "بَدَلٌ مِنَ اسْمِ الْإِشَارَةِ مَجْرُورٌ — جَمْعُ «وَجْهٍ»، وَالْوَجْهُ هُنَا الْأُسْلُوبُ.",
      "A badal of the demonstrative, in jarr — the plural of وَجْه, and a «wajh» here is a manner of putting something. The reader has met this word as the face of a many-faced particle; the sense is the same one, at the level of a whole sentence.",
      "İsm-i işaretten bedel, mecrûr — «وَجْه»in cemi; ve buradaki «vech», bir şeyi ortaya koyuş tarzıdır. Okuyucu bu kelimeyi çok vecihli bir edatın vechi olarak görmüştü; mânâ aynı mânâdır, fakat bütün bir cümle seviyesinde."),
  tok("إِخْرَاجًا","ikhraj","noun",["mafulayn","maful-bihi"],
      "الْمَفْعُولُ الثَّانِي لِـ«يُسَمَّى» مَنْصُوبٌ — وَهُوَ نَفْسُ الْمَصْدَرِ الَّذِي نَابَ عَنِ الْفَاعِلِ فِي أَوَّلِ الْجُمْلَةِ، مَرْفُوعًا هُنَاكَ وَمَنْصُوبًا هُنَا.",
      "The SECOND object of «is called», in nasb — and it is the very same masdar that stood as the deputy subject four words earlier, in raf' there and in nasb here. One word, one clause, two cases, and the two offices of a doubly-transitive verb's passive laid out side by side. There is no clearer demonstration in the book.",
      "«يُسَمَّى»nin İKİNCİ mef'ûlü, mansub — ve dört kelime önce nâib-i fâil olarak duran masdarın ta kendisidir: orada merfû, burada mansub. Tek kelime, tek cümle, iki hâl; ve iki mef'ûllü bir fiilin meçhûlündeki iki vazife yan yana serilmiş. Kitapta bundan daha açık bir gösterim yoktur."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«إِخْرَاجًا».",
      "A jarr letter attaching to the second «putting out».",
      "İkinci «إِخْرَاجًا»a taalluk eden cer harfi."),
  tok("مُقْتَضَى","muqtada","noun",["huruf-jarr","ism-maqsur-manqus","ism-maful","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَلَى» بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ وَهُوَ مُضَافٌ — وَقَدْ مَرَّ فِي الْبَابِ الثَّانِي مَجْرُورًا ثُمَّ مَنْصُوبًا.",
      "Majrur by «ala» with a kasra estimated on the alif, and a mudaf — the word chapter 2 showed first in jarr and then in nasb without changing a letter. Here it is in jarr again, and the reader who noticed it there has a fact about maqsur nouns that no amount of explanation supplies as well.",
      "«عَلَى» ile, taazzür sebebiyle elif üzerinde mukadder kesra ile mecrûr ve muzâf — ikinci bâbın önce cerde sonra nasbda, tek harf değiştirmeden gösterdiği kelime. Burada yine cerdedir; orada fark eden okuyucunun elinde, maksûr isimler hakkında hiçbir izahın veremeyeceği bir hakikat vardır."),
  tok("الظَّاهِرِ","zahir","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «ظَهَرَ». وَ«مُقْتَضَى الظَّاهِرِ» أَخَصُّ مِنْ «مُقْتَضَى الْحَالِ»: كُلُّ مُقْتَضَى ظَاهِرٍ مُقْتَضَى حَالٍ وَلَا عَكْسَ.",
      "The mudaf ilayh in jarr — the ism fa'il of ظَهَرَ. And «what the SURFACE calls for» is narrower than «what the situation calls for»: every muqtada zahir is a muqtada hal and not the reverse. The wider term was the definition of the whole discipline in chapter 2; this narrower one is the default case inside it, and the next sentence is about leaving it.",
      "Mecrûr muzâfun ileyh — «ظَهَرَ»nin ism-i fâili. Ve «muktezâ-yı ZÂHİR», «muktezâ-yı hâl»den daha husûsîdir: her muktezâ-yı zâhir bir muktezâ-yı hâldir, aksi değil. Geniş olanı ikinci bâbda bütün ilmin tarifiydi; bu dar olan ise onun içindeki varsayılan hâldir ve bir sonraki cümle onu terk etmeye dairdir.",
      punct="."),
 ],
 "jumal": [J("وَيُسَمَّى إِخْرَاجُ الْكَلَامِ … إِخْرَاجًا عَلَى مُقْتَضَى الظَّاهِرِ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed verbal sentence, with no position in i'rab.",
   "İsti'nâfî fiil cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "And speech is sometimes put out against what the surface calls for.",
 "tr": "Kelâm bazen muktezâ-yı zâhirin hilâfına da söylenir."},
 "tokens": [
  tok("وَقَدْ","qad","part",["qad-harf"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«قَدْ» حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ — وَهِيَ مَعَ الْمَاضِي لِلتَّحْقِيقِ، فَالْحَرْفُ وَاحِدٌ وَالْمَعْنَى يَتَبَدَّلُ بِالْفِعْلِ الَّذِي يَدْخُلُ عَلَيْهِ.",
      "A resuming waw, and «qad» — which with a MUDARI means «sometimes» and with a MAZI means «indeed». One letter, two opposite jobs, and what decides is nothing but the tense of the verb after it. Here it is doing the first: the departure is real but not the rule.",
      "İsti'nâf vâvı; ve «قَدْ» — MUZÂRİ ile «bazen», MÂZÎ ile «muhakkak» mânâsı verir. Tek harf, iki zıt vazife; ve tayin eden şey, yalnızca ardındaki fiilin zamanıdır. Burada birincisini yapar: ayrılış gerçektir, fakat kâide değildir.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يُخْرَجُ","akhraja","verb",["naib-al-fail","mudari-marfu","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ — وَقَاعِدَتُهُ: ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ، يُخْرِجُ ← يُخْرَجُ.",
      "A mudari for the unnamed doer, in raf' with the damma WRITTEN — and the rule that made it is the one every Emsile student recites: raise the first letter and open the one before the last. يُخْرِجُ becomes يُخْرَجُ, and the whole difference between the active and the passive is one vowel on one letter. Set it beside يُسَمَّى, where the same damma had to be estimated because the last letter was an alif.",
      "Meçhûl sîgasında muzâri, ZÂHİR damme ile merfû — ve onu yapan kâide, her Emsile talebesinin ezberlediği kâidedir: evvelini zammeli, âhirinden öncekini fethalı yap. «يُخْرِجُ» «يُخْرَجُ» olur ve ma'lûm ile meçhûl arasındaki bütün fark, tek harf üzerindeki tek harekedir. Son harfi elif olduğu için aynı dammenin mukadder kaldığı «يُسَمَّى» ile yan yana koyun."),
  tok("الْكَلَامُ","kalam","noun",["naib-al-fail"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — وَهُوَ الَّذِي كَانَ مَجْرُورًا مُضَافًا إِلَيْهِ فِي الْجُمْلَةِ السَّابِقَةِ.",
      "The naib al-fa'il in raf' — and it is the word that stood majrur as a mudaf ilayh one sentence ago. The matn is putting the same noun through its cases as it goes, which is what makes a matn readable by a student rather than only by a scholar.",
      "Merfû nâib-i fâil — ve bir önceki cümlede muzâfun ileyh olarak mecrûr duran kelimenin ta kendisidir. Metin, ilerledikçe aynı ismi hâllerinden geçirir; bir metni yalnız âlimin değil talebenin de okuyabilmesini sağlayan şey budur."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يُخْرَجُ».",
      "A jarr letter attaching to «is put out».",
      "«يُخْرَجُ»a taalluk eden cer harfi."),
  tok("خِلَافِ","khilaf","noun",["idafa-definiteness","masdar","form-iii-verbs"],
      "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ — مَصْدَرُ «خَالَفَ» عَلَى فِعَالٍ، وَهُوَ الْمُصْطَلَحُ نَفْسُهُ الَّذِي خُتِمَ بِهِ «مُخْتَصَرُ الْمَنَارِ»: «عَلَى خِلَافِ الْقِيَاسِ».",
      "Majrur by «ala» and a mudaf — the Form III masdar of خَالَفَ, and the very phrase Mukhtasar al-Manar closed on: «contrary to analogy». Two disciplines, and each keeps a named place for the case that breaks its own rule. That is not a coincidence of vocabulary; it is what a mature discipline does.",
      "«عَلَى» ile mecrûr ve muzâf — «خَالَفَ»nin FİÂL vezninde masdarı; ve «Muhtasaru'l-Menâr»ın kendisiyle kapandığı ibarenin aynısı: «kıyâsa muhâlif». İki ilim ve her biri, kendi kâidesini bozan hâle adlı bir yer ayırır. Bu bir kelime tesadüfü değil, olgunlaşmış bir ilmin yaptığı şeydir."),
  tok("مُقْتَضَى","muqtada","noun",["idafa-definiteness","ism-maqsur-manqus","ism-maful"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ وَهُوَ مُضَافٌ — ثَلَاثُ إِضَافَاتٍ مُتَتَابِعَةٍ: خِلَافِ ← مُقْتَضَى ← الظَّاهِرِ.",
      "The mudaf ilayh, majrur by an estimated kasra, and itself a mudaf — three annexations in a row: the contrary OF what is called for BY the surface. Each link narrows the one before it, and the phrase cannot be read at all until the last word arrives.",
      "Mukadder kesra ile mecrûr muzâfun ileyh ve kendisi de muzâf — arka arkaya üç izâfet: ZÂHİRin GEREKTİRDİĞİnin HİLÂFI. Her halka öncekini daraltır ve ibare, son kelime gelmeden hiç okunamaz."),
  tok("الظَّاهِرِ","zahir","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ يُفْتَحُ أَطْوَلُ فُصُولِ هَذَا الْفَنِّ: مَتَى يُنَزَّلُ غَيْرُ السَّائِلِ مَنْزِلَةَ السَّائِلِ، وَالْمُنْكِرُ مَنْزِلَةَ غَيْرِهِ.",
      "The mudaf ilayh in jarr — and with it the longest section of this discipline opens: when a man who is not asking is treated as though he were, when a denier is treated as though he were not, and why. The rule was stated in three sentences; the exceptions take the rest of the book. That ratio is itself worth noticing.",
      "Mecrûr muzâfun ileyh — ve onunla bu fennin en uzun faslı açılır: taleb etmeyen ne zaman taleb eden menzilesine indirilir, inkâr eden ne zaman inkâr etmeyen menzilesine konur ve niçin. Kâide üç cümlede söylendi; istisnâlar kitabın geri kalanını alır. Bu nisbetin kendisi de dikkate değer.",
      punct="."),
 ],
 "jumal": [J("وَقَدْ يُخْرَجُ الْكَلَامُ عَلَى خِلَافِ مُقْتَضَى الظَّاهِرِ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed verbal sentence, with no position in i'rab.",
   "İsti'nâfî fiil cümlesi; i'râbdan mahalli yoktur.")]})

GLOSS_ADD = {
 "ila":      g("إِلَى", None, "prep", "to, towards", "-e, -a doğru", 0),
 "qad":      g("قَدْ", None, "part", "qad — «indeed» with a past verb, «sometimes» with a present one", "kad — mâzî ile «muhakkak», muzâri ile «bazen»", 2),
 "in-shartiyya": g("إِنْ", None, "part", "if (conditional; it puts two verbs into jazm)", "eğer (şart; iki fiili cezmeder)", 2),
 "hadhihi":  g("هَذِهِ", None, "pron", "this (fem.)", "bu (müennes)", 1),
 "bila":     g("بِلَا", None, "prep", "without", "-sız, -siz", 2),
 "asl":      g("أَصْل", "أ ص ل", "noun", "the root case; the default that needs no reason", "asıl; sebep gerektirmeyen varsayılan hâl", 3, plural="أُصُول"),
 "dhihn":    g("ذِهْن", "ذ ه ن", "noun", "the mind", "zihin", 3, plural="أَذْهَان"),
 "khali":    g("خَالٍ (الْخَالِي)", "خ ل و", "noun", "empty of, free of (ism fa'il, manqus)", "hâlî; boş (ism-i fâil, menkūs)", 4),
 "takid":    g("تَأْكِيد", "أ ك د", "noun", "emphasis (masdar, Form II)", "te'kîd; pekiştirme (masdar, tef'îl)", 3),
 "tawkid":   g("تَوْكِيد", "و ك د", "noun", "emphasis (masdar, Form II — the waw-initial spelling)", "te'kîd (masdar, tef'îl — vâvlı yazılışı)", 3),
 "muakkid":  g("مُؤَكِّد", "أ ك د", "noun", "an emphasiser (ism fa'il, Form II)", "müekkid; te'kîd edici (ism-i fâil, tef'îl)", 4),
 "taqwiya":  g("تَقْوِيَة", "ق و ي", "noun", "strengthening (masdar, Form II of a naqis)", "takviye; kuvvetlendirme (nâkıstan tef'îl masdarı)", 4),
 "mutaraddid": g("مُتَرَدِّد", "ر د د", "noun", "hesitating, going back and forth (ism fa'il, Form V)", "mütereddid; gidip gelen (ism-i fâil, tefe''ul)", 4),
 "talib":    g("طَالِب", "ط ل ب", "noun", "seeking, asking for (ism fa'il)", "tâlib; isteyen (ism-i fâil)", 2),
 "munkir":   g("مُنْكِر", "ن ك ر", "noun", "denying (ism fa'il, Form IV)", "münkir; inkâr eden (ism-i fâil, if'âl)", 4),
 "inkar":    g("إِنْكَار", "ن ك ر", "noun", "denial (masdar, Form IV)", "inkâr (masdar, if'âl)", 3),
 "hasab":    g("حَسَب", "ح س ب", "noun", "measure, proportion (used as بِحَسَبِ = in proportion to)", "hasep; ölçü (بِحَسَبِ = -e göre)", 4),
 "ikhraj":   g("إِخْرَاج", "خ ر ج", "noun", "putting out, sending forth (masdar, Form IV)", "ihrâc; çıkarma (masdar, if'âl)", 4),
 "wajh":     g("وَجْه", "و ج ه", "noun", "a face; a manner of putting something", "vecih; bir şeyi ortaya koyuş tarzı", 2, plural="وُجُوه"),
 "ibtidai":  g("ابْتِدَائِيّ", "ب د أ", "noun", "ibtidaʾi — said to a mind empty of the ruling, with no emphasis", "ibtidâî — hükümden hâlî bir zihne te'kîdsiz söylenen", 5),
 "talabi":   g("طَلَبِيّ", "ط ل ب", "noun", "talabi — said to a hesitating hearer, with one emphasiser", "talebî — tereddüd eden muhâtaba bir te'kîdle söylenen", 5),
 "inkari":   g("إِنْكَارِيّ", "ن ك ر", "noun", "inkari — said to a denier, emphasised in proportion to the denial", "inkârî — münkire, inkârı nisbetinde te'kîdle söylenen", 5),
 "khilaf":   g("خِلَاف", "خ ل ف", "noun", "disagreement; the contrary of", "muhalefet, hilâf", 3),
 "samma":    g("سَمَّى", "س م و", "verb", "to name, to call (two objects)", "adlandırmak, isim vermek (iki mef'ûllü)", 2, form="II"),
 "alqa":     g("أَلْقَى", "ل ق ي", "verb", "to deliver, to cast (a word) to someone", "ilkā etmek; (sözü) birine söylemek", 4, form="IV"),
 "hasuna":   g("حَسُنَ", "ح س ن", "verb", "to be good, to be fitting", "güzel olmak, yakışık almak", 3, form="I"),
 "wajaba":   g("وَجَبَ", "و ج ب", "verb", "to be obligatory", "vâcib olmak, gerekmek", 2, form="I"),
 "akhraja":  g("أَخْرَجَ", "خ ر ج", "verb", "to put out, to bring forth", "çıkarmak, ihrâc etmek", 3, form="IV"),
}

def build_morph():
    out = {}
    # COPIED after a lemma-identity assert — a lex key is global.
    for pkg, lex in [("bad-al-amali", "samma"),
                     ("aqaid-ahl-al-sunna", "wajaba"),
                     ("aqaid-ahl-al-sunna", "akhraja")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))
        assert g_["entries"][lex]["lemma"] == GLOSS_ADD[lex]["lemma"], lex
        out[lex] = m["verbs"][lex]
    # أَلْقَى — Form IV of a NAQIS. Its majhul is the chapter's own first lesson
    # and is stored: يُلْقَى, where the fatha of nasb has nowhere to sit.
    out["alqa"] = _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ",
                                    "أَلْقَ", "لْق", "i", "أَلْق",
                                    "إِلْقَاء", "مُلْقٍ", "مُلْقًى", "أُلْقِيَ", "يُلْقَى",
                                    "نَاقِصٌ مِنَ الْإِفْعَالِ: يُلْقِي ← لَمْ يُلْقِ، وَمَجْهُولُهُ يُلْقَى.")
    # حَسُنَ — the FIFTH bab of the mujarrad, فَعُلَ يَفْعُلُ, which sarf_gen could
    # not build until this chapter needed it. Its ism fa'il is regularly the
    # sifa mushabbaha حَسَن; حَاسِن is the mechanical فَاعِل and is what the
    # conjugator derives, so it is what the paradigm stores and the note says
    # which is which.
    # …and it goes through idgham, because its last radical is a NUN and the
    # feminine plural's own nun meets it: حَسُنْ + نَ = حَسُنَّ. The audit caught
    # this on the first run — the generator wrote the fakk and the reader's
    # Form I branch assimilates — which is precisely what that gate is for.
    out["hasuna"] = _sg.idgham(
        _sg.sound1("karuma", "حَسُن", "حْسُن", "اُحْسُن", "حُسْن", "حَاسِن",
                   note="بَابُ الْأَوْصَافِ الثَّابِتَةِ — وَالْوَصْفُ مِنْهُ صِفَةٌ مُشَبَّهَةٌ: حَسَنٌ، لَا فَاعِلٌ. "
                        "وَلَامُهُ نُونٌ، فَتُدْغَمُ فِي نُونِ النِّسْوَةِ: حَسُنَّ."))
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/3.json").write_text(
    json.dumps({"chapter": 3, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 3 for c in man["chapters"]):
    man["chapters"].append({"n": 3, "title": TITLE3})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.3.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch3:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
