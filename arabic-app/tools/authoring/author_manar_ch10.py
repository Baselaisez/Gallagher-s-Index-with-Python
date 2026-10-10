# -*- coding: utf-8 -*-
"""Author chapter 10 of mukhtasar-al-manar — the wording taken by its USE.

Chapter 4 divided the lafz by what it was SET DOWN for. This chapter divides
the same lafz by what it is being USED for on this occasion — haqiqa and majaz
— and then by how plainly that use shows: sarih and kinaya. It is the fourth
and last of the book's divisions of the wording, and it is the one that hands
usul over to balagha: the ʿalaqa it names in passing is the same ʿalaqa the
twenty-eight relations of the majaz bank are built on.

ATTRIBUTION: like chapters 2–9, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • اسْتُعْمِلَ — the MAJHUL of Form X, the first in the package. أُ on the first
    letter, a kasra before the last: اِسْتَعْمَلَ → اسْتُعْمِلَ.
  • فِيمَا — a jarr letter fused to مَا, written as one word and TWO words in
    i'rab. The engine's ma-reader has a rule for exactly this position.
  • غَيْرِ مَا وُضِعَ لَهُ — غَيْر taking a whole SILA for its mudaf ilayh.
  • ظُهُورًا بَيِّنًا — a maf'ul mutlaq with its own na't, the second in the
    package after نَقْلًا مُتَوَاتِرًا in chapter 2.
  • فَلَا يُفْهَمُ إِلَّا بِقَرِينَةٍ — the FOURTH istithna mufarragh, and by now the
    shape should be read before the words are.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/mukhtasar-al-manar"
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
def g(lemma, root, pos, en, tr, level, plural=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
S = []

TITLE10 = {"ar": "الْحَقِيقَةُ وَالْمَجَازُ وَالصَّرِيحُ وَالْكِنَايَة",
           "en": "Literal and Figurative, Plain and Veiled",
           "tr": "Hakikat ve Mecâz, Sarîh ve Kinâye"}

S.append({"id": "s1", "translation": {
 "en": "Then the wording, taken by its use, is literal, figurative, plain or veiled.",
 "tr": "Lafız, kullanımı itibarıyla hakikat, mecâz, sarîh ve kinâyedir."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.",
      "A letter of atf giving sequence with an interval.",
      "Terâhî ile tertîb için atıf harfi."),
  tok("اللَّفْظُ","lafz","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ الْمُبْتَدَأُ الَّذِي فُتِحَ بِهِ بَابُ الْأَقْسَامِ وَبَابُ الْوُضُوحِ. ثَلَاثَةُ تَقَاسِيمَ لِمَقْسُومٍ وَاحِدٍ.",
      "The mubtada in raf' — the same mubtada that opened the chapter on the divisions and the chapter on clarity. THREE divisions of one and the same thing, each cut by a different ruler: what it was set down for, how plainly it shows, and what it is being used for now.",
      "Merfû mübtedâ — aksâm bâbını ve vuzûh bâbını açan mübtedânın aynısı. Tek bir maksûmun ÜÇ taksîmi; her biri başka bir ölçüyle: neye vaz' edildiği, ne kadar açık göründüğü ve şimdi ne için kullanıldığı."),
  tok("بِاعْتِبَارِ","itibar","noun",["huruf-jarr","idafa-definiteness","masdar","form-viii-verbs"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ، وَ«اعْتِبَارِ» مُضَافٌ — وَهُوَ اللَّفْظُ الَّذِي يُؤْذِنُ بِتَبْدِيلِ الْمِعْيَارِ.",
      "A jarr-majrur hanging on an omitted hal, and «taken by» a mudaf — the phrase that announces a change of RULER. Every division in this book is introduced by it, and the reader who watches for it never confuses two divisions of the same word.",
      "Mahzûf bir hâle taalluk eden câr-mecrûr; «اعْتِبَارِ» muzâftır — ÖLÇÜNÜN değiştiğini haber veren ibare. Kitaptaki her taksim onunla girer; onu kollayan okuyucu aynı kelimenin iki taksîmini birbirine karıştırmaz.",
      segments=[seg("بِ","bi","prep"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("الِاسْتِعْمَالِ","istimal","noun",["idafa-definiteness","masdar","form-x-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «اِسْتَعْمَلَ» عَلَى اسْتِفْعَالٍ، وَبَيْنَهُ وَبَيْنَ «الْوَضْعِ» تَمَامُ الْفَرْقِ: الْوَضْعُ سَابِقٌ عَلَى الْمُتَكَلِّمِ، وَالِاسْتِعْمَالُ فِعْلُهُ.",
      "The mudaf ilayh in jarr — the masdar of اِسْتَعْمَلَ on اِسْتِفْعَال. Between it and الْوَضْع lies the whole distinction this chapter rests on: the SETTING-DOWN came before any speaker, the USE is what a speaker does with what he found.",
      "Mecrûr muzâfun ileyh — «اِسْتَعْمَلَ»nin İSTİF'ÂL vezninde masdarı. Onunla «الْوَضْع» arasında bu bâbın dayandığı bütün fark vardır: vaz', mütekellimden öncedir; isti'mâl ise onun bulduğu şeyle yaptığıdır."),
  tok("حَقِيقَةٌ","haqiqa","noun",["mubtada-khabar","haqiqa-majaz"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَقَدْ مَرَّتْ «الْحَقِيقَةُ» فِي الْبَابِ السَّابِقِ مُضَافًا إِلَيْهَا، وَهَا هِيَ الْآنَ مَحْدُودَةً لِذَاتِهَا.",
      "The khabar in raf' with its tanwin — and حَقِيقَة stood in the chapter before as a mudaf ilayh, borrowed for another definition. Here it is defined for its own sake. A term is used before it is defined and defined when it must be; that is the order a matn keeps.",
      "Tenvînli merfû haber — «الْحَقِيقَة» bir önceki bâbda başka bir tarifin muzâfun ileyhi olarak geçmişti; burada kendisi için tarif edilir. Bir ıstılah, gerektiğinde tarif edilir; metnin tuttuğu sıra budur."),
  tok("وَمَجَازٌ","majaz","noun",["atf-nasaq","haqiqa-majaz"],
      "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرٌ مِيمِيٌّ مِنْ «جَازَ»، أَيْ تَجَاوَزَ مَوْضِعَهُ.",
      "Joined, in raf' — a mimic masdar from جَازَ: the wording that has stepped past its own place.",
      "Ma'tûf, merfû — «جَازَ»den masdar-ı mîmî: kendi yerini aşmış lafız.",
      segments=[seg("وَ","wa","conj"), seg("مَجَازٌ","majaz","noun")]),
  tok("وَصَرِيحٌ","sarih","noun",["atf-nasaq","sifa-mushabbaha"],
      "مَعْطُوفٌ مَرْفُوعٌ — عَلَى فَعِيلٍ مِنْ «صَرُحَ»: الْخَالِصُ الَّذِي لَا يَحْتَاجُ إِلَى شَيْءٍ مَعَهُ.",
      "Joined, in raf' — on فَعِيل from صَرُحَ: the unmixed, the wording that needs nothing beside it to be understood.",
      "Ma'tûf, merfû — «صَرُحَ»den FAÎL vezninde: hâlis olan, anlaşılmak için yanında başka bir şeye muhtaç olmayan.",
      segments=[seg("وَ","wa","conj"), seg("صَرِيحٌ","sarih","noun")]),
  tok("وَكِنَايَةٌ","kinaya","noun",["atf-nasaq","kinaya","masdar"],
      "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ «كَنَى»، وَبِهِ تَمَّتِ الْأَقْسَامُ. وَالْكِنَايَةُ فِي الْبَلَاغَةِ بَابٌ قَائِمٌ بِنَفْسِهِ، وَهِيَ هُنَا قِسْمٌ مِنْ أَقْسَامِ الِاسْتِعْمَالِ.",
      "Joined, in raf' — the masdar of كَنَى, and with it the kinds are complete. In balagha the kinaya is a chapter of its own; here it is one of the ways a wording may be used, and the two treatments are the same subject approached from two sciences.",
      "Ma'tûf, merfû — «كَنَى»nin masdarı; kısımlar bununla tamamlanır. Belâgatte kinâye müstakil bir bâbdır; burada isti'mâlin kısımlarından biridir — aynı mevzu, iki ilimden bakılmış hâli.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("كِنَايَةٌ","kinaya","noun")]),
 ],
 "jumal": [J("اللَّفْظُ بِاعْتِبَارِ الِاسْتِعْمَالِ حَقِيقَةٌ وَمَجَازٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the literal is what has been used in the very thing it was set down for.",
 "tr": "Hakikat, kendisi için vaz' edildiği mânâda kullanılandır."},
 "tokens": [
  tok("فَالْحَقِيقَةُ","haqiqa","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْحَقِيقَةُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the literal» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الْحَقِيقَةُ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْحَقِيقَةُ","haqiqa","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("اسْتُعْمِلَ","istamala","verb",["naib-al-fail","form-x-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ عَلَى «اِسْتَفْعَلَ»، وَالْجُمْلَةُ صِلَةٌ — وَبِنَاءُ الْمَاضِي لِلْمَجْهُولِ: ضَمُّ أَوَّلِهِ وَكَسْرُ مَا قَبْلَ آخِرِهِ. «اِسْتَعْمَلَ» ← «اسْتُعْمِلَ».",
      "A past verb built for the unnamed doer, on اِسْتَفْعَلَ; the clause is the sila. The rule for the passive of a past verb is two vowels and no more: a DAMMA on its first letter and a KASRA before its last. اِسْتَعْمَلَ becomes اسْتُعْمِلَ, and the same two moves turn نَصَرَ into نُصِرَ and اِسْتَخْرَجَ into اسْتُخْرِجَ, however long the word.",
      "«اِسْتَفْعَلَ» vezninde meçhûl mâzî fiil; cümle sıladır. Mâzînin meçhûl binâsı iki harekedir, fazlası değil: BAŞI ÖTRELİ, SON HARFİNDEN ÖNCESİ ESRELİ. «اِسْتَعْمَلَ» → «اسْتُعْمِلَ»; aynı iki hareke نَصَرَ'yi نُصِرَ, اِسْتَخْرَجَ'yi اسْتُخْرِجَ yapar — kelime ne kadar uzarsa uzasın."),
  tok("فِيمَا","ma-mawsula","pron",["huruf-jarr","ism-mawsul"],
      "«فِي» حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — كَلِمَةٌ وَاحِدَةٌ فِي الْخَطِّ وَكَلِمَتَانِ فِي الْإِعْرَابِ.",
      "«Fi» is a jarr letter and «ma» a relative noun, fixed in form, in the position of jarr after it — ONE word in writing and TWO in i'rab. The fusion is orthographic only, and every rule that reads the ma must peel the jarr off first or it will never see it.",
      "«فِي» cer harfi, «مَا» ise onunla mahallen mecrûr mebnî ism-i mevsûldür — yazıda tek kelime, i'râbda iki. Birleşme yalnızca imlâdadır; mâyı okuyan her kaide önce cer harfini soymalıdır, yoksa onu hiç göremez.",
      segments=[seg("فِي","fi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("وُضِعَ","wadaa","verb",["naib-al-fail","mithal-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةُ «مَا» الثَّانِيَةِ — وَهُوَ عَيْنُ الْفِعْلِ الَّذِي بُنِيَ عَلَيْهِ بَابُ الْأَقْسَامِ.",
      "A past verb built for the unnamed doer; the clause is the sila of the SECOND «ma». It is the very verb chapter 4 built its definitions on — «what was set down for one meaning». Here the same verb marks off the meaning a word may now be used in.",
      "Meçhûl mâzî fiil; cümle İKİNCİ «مَا»nın sılasıdır. Dördüncü bâbın tariflerini üzerine kurduğu fiilin aynısıdır — «tek bir mânâ için vaz' edilen». Burada aynı fiil, kelimenin şimdi hangi mânâda kullanılabileceğini sınırlar."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«وُضِعَ»، وَالْهَاءُ عَائِدَةٌ عَلَى «مَا» الثَّانِيَةِ.",
      "A jarr-majrur attaching to «was set down», its HA going back to the second «ma» — the returning pronoun that ties that sila to its own relative. Two relatives in one sentence, each with its own clause and its own tie.",
      "«وُضِعَ»ye taalluk eden câr-mecrûr; HÂ ikinci «مَا»ya râcidir — o sılayı kendi mevsûlüne bağlayan âid zamîr. Bir cümlede iki mevsûl; her birinin kendi sılası ve kendi râbıtası var.",
      punct=".", segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
 ],
 "jumal": [J("الْحَقِيقَةُ مَا اسْتُعْمِلَ فِيمَا وُضِعَ لَهُ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("وُضِعَ لَهُ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ الثَّانِي — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the second relative — i'rabless.",
   "İkinci mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the figurative is what has been used in other than what it was set down for, for a relation between the two.",
 "tr": "Mecâz, aralarındaki bir alâka sebebiyle, vaz' edildiğinin gayrısında kullanılandır."},
 "tokens": [
  tok("وَالْمَجَازُ","majaz","noun",["atf-nasaq","mubtada-khabar","haqiqa-majaz"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمَجَازُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the figurative» is the mubtada in raf'.",
      "Atıf vâvı; «الْمَجَازُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمَجَازُ","majaz","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("اسْتُعْمِلَ","istamala","verb",["naib-al-fail","form-x-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ — وَأُعِيدَ بِعَيْنِهِ، فَالْفَرْقُ بَيْنَ الْحَدَّيْنِ فِي كَلِمَةٍ وَاحِدَةٍ: «غَيْرِ».",
      "A past verb built for the unnamed doer; the clause is the sila. The verb is repeated word for word, and ONE word is inserted: غَيْر. That single insertion is the whole difference between the literal and the figurative.",
      "Meçhûl mâzî fiil; cümle sıladır. Fiil aynen tekrarlanmış ve TEK bir kelime eklenmiştir: «غَيْرِ». Hakikat ile mecâz arasındaki bütün fark o tek ilâvedir."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«اسْتُعْمِلَ».",
      "A jarr letter attaching to «has been used».",
      "«اسْتُعْمِلَ»ye taalluk eden cer harfi."),
  tok("غَيْرِ","ghayr","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — وَمُضَافُهُ جُمْلَةٌ مَوْصُولِيَّةٌ بِتَمَامِهَا: «مَا وُضِعَ لَهُ».",
      "In jarr after «fi» and a mudaf — and what is added to it is a whole RELATIVE PHRASE, «what it was set down for». A mudaf ilayh need not be a single noun; a مَا with its sila is one noun as far as the idafa is concerned.",
      "«فِي» ile mecrûr ve muzâf — muzâfun ileyhi ise baştan sona bir MEVSÛL ibaresidir: «مَا وُضِعَ لَهُ». Muzâfun ileyhin tek kelime olması gerekmez; sılasıyla birlikte bir «مَا», izâfet bakımından tek isim hükmündedir."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A relative noun, fixed in form, in the position of jarr as the mudaf ilayh.",
      "Mebnî ism-i mevsûl; muzâfun ileyh olarak mahallen mecrûrdur."),
  tok("وُضِعَ","wadaa","verb",["naib-al-fail","mithal-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ لَا مَحَلَّ لَهَا.",
      "A past verb built for the unnamed doer; the clause is the sila, i'rabless.",
      "Meçhûl mâzî fiil; cümle sıladır ve mahalsizdir."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«وُضِعَ»، وَالْهَاءُ الْعَائِدُ.",
      "A jarr-majrur attaching to «was set down», the HA the returning pronoun.",
      "«وُضِعَ»ye taalluk eden câr-mecrûr; HÂ âid zamîrdir.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("لِعَلَاقَةٍ","alaqa","noun",["huruf-jarr","lam-taleel","anwa-al-majaz"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«اسْتُعْمِلَ»، وَاللَّامُ لِلتَّعْلِيلِ — وَهَذَا الْقَيْدُ هُوَ الَّذِي يَفْصِلُ الْمَجَازَ عَنِ الْغَلَطِ: لَا يَجُوزُ نَقْلُ اللَّفْظِ إِلَى مَعْنًى آخَرَ إِلَّا بِمُنَاسَبَةٍ مَعْلُومَةٍ بَيْنَهُمَا.",
      "A jarr-majrur attaching to «has been used», the LAM giving the reason — and this restriction is what separates a MAJAZ from a MISTAKE. A word may not be carried to another meaning at will: there must be a known relation between the two, and the balagha books count those relations one by one. Calling a brave man a lion is a majaz; calling him a table is an error.",
      "«اسْتُعْمِلَ»ye taalluk eden câr-mecrûr; LÂM ta'lîl içindir — mecâzı YANLIŞtan ayıran kayıt budur. Lafız keyfî olarak başka bir mânâya taşınamaz: aralarında bilinen bir münâsebet bulunmalıdır ve belâgat kitapları bu alâkaları tek tek sayar. Yiğide arslan demek mecâzdır; masa demek hatadır.",
      segments=[seg("لِ","li","prep"), seg("عَلَاقَةٍ","alaqa","noun")]),
  tok("بَيْنَهُمَا","bayna","noun",["maful-fih","idafa-definiteness","al-muthanna"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«هُمَا» ضَمِيرُ الْمُثَنَّى مُضَافٌ إِلَيْهِ — عَائِدٌ عَلَى الْمَعْنَيَيْنِ: الْمَوْضُوعِ لَهُ وَالْمُسْتَعْمَلِ فِيهِ.",
      "A place-adverb in nasb and a mudaf, with the DUAL pronoun «huma» as its mudaf ilayh — going back to the two meanings: the one the word was set down for and the one it is now used in. The dual is exact: a majaz always has two ends, never one and never three.",
      "Mansub mekân zarfı ve muzâf; TESNİYE zamîri «هُمَا» muzâfun ileyhtir — iki mânâya râcidir: vaz' edildiği mânâ ile kullanıldığı mânâ. Tesniye tam yerindedir: mecâzın daima iki ucu vardır, bir değil, üç değil.",
      punct=".", segments=[seg("بَيْنَ","bayna","noun"), seg("هُمَا","pron-3d","pron")]),
 ],
 "jumal": [J("الْمَجَازُ مَا اسْتُعْمِلَ فِي غَيْرِ مَا وُضِعَ لَهُ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And the plain is that whose intended sense shows with an evident showing, from the frequency of its use.",
 "tr": "Sarîh, çok kullanılması sebebiyle murâdı apaçık ortaya çıkandır."},
 "tokens": [
  tok("وَالصَّرِيحُ","sarih","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الصَّرِيحُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the plain» is the mubtada in raf'.",
      "Atıf vâvı; «الصَّرِيحُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الصَّرِيحُ","sarih","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ظَهَرَ","zahara","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — وَهُوَ الْفِعْلُ الَّذِي حُدَّ بِهِ «الظَّاهِرُ» فِي بَابِ الْوُضُوحِ، وَالسُّؤَالُ هُنَا غَيْرُهُ: هُنَاكَ ظُهُورٌ بِنَفْسِ السَّمَاعِ، وَهُنَا ظُهُورٌ بِكَثْرَةِ الِاسْتِعْمَالِ.",
      "A past verb; the clause is the sila. It is the same verb that defined الظَّاهِر in the clarity chapter, but the question is not the same: there the meaning showed by the very hearing of the words, here it shows because the words have been used that way so often. The wording is clear by HABIT, not by nature.",
      "Mâzî fiil; cümle sıladır. Vuzûh bâbında «الظَّاهِر»i tarif eden fiilin aynısıdır, fakat soru başkadır: orada mânâ sırf işitmekle görünüyordu, burada ise o kadar çok öyle kullanıldığı için görünür. Lafız TABİATIYLA değil, ÂDETLE açıktır."),
  tok("الْمُرَادُ","murad","noun",["fail","ism-maful"],
      "فَاعِلٌ مَرْفُوعٌ.", "The fa'il, in raf'.", "Merfû fâil."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ظَهَرَ»، وَالْهَاءُ الْعَائِدُ عَلَى «مَا».",
      "A jarr-majrur attaching to «shows», the HA going back to «that which».",
      "«ظَهَرَ»ye taalluk eden câr-mecrûr; HÂ «مَا»ya râci âid zamîrdir.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("ظُهُورًا","zuhur","noun",["maful-mutlaq","masdar"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرٌ مِنْ لَفْظِ عَامِلِهِ، جِيءَ بِهِ لِيُوصَفَ فَيُبَيِّنَ النَّوْعَ.",
      "A MAF'UL MUTLAQ in nasb — a masdar from the very verb that governs it, brought so that it can be DESCRIBED. A bare maf'ul mutlaq merely confirms; one carrying an adjective tells you what KIND. This is the second in the package after نَقْلًا مُتَوَاتِرًا in chapter 2, and both are there for the adjective's sake.",
      "Mansub MEF'ÛL-Ü MUTLAK — âmilinin lafzından masdardır ve VASIFLANSIN diye getirilmiştir. Çıplak mef'ûl-ü mutlak yalnız te'kîd eder; sıfat taşıyan ise NEVİ bildirir. Pakette ikincisidir — birincisi ikinci bâbdaki «نَقْلًا مُتَوَاتِرًا» — ve ikisi de sıfatı için getirilmiştir."),
  tok("بَيِّنًا","bayyin","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«ظُهُورًا» مَنْصُوبٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَيْعِل مِنْ «بَانَ»، وَأَصْلُهُ «بَيْيِن» فَأُدْغِمَ.",
      "A na't of «a showing», in nasb — a sifa mushabbaha on فَيْعِل from بَانَ, its origin بَيْيِن with the two yas run together. It is the adjective the maf'ul mutlaq was brought to carry.",
      "«ظُهُورًا»ın na'tı, mansub — «بَانَ»dan FEY'İL vezninde sıfat-ı müşebbehe; aslı «بَيْيِن»dir, iki yâ idgâm edilmiştir. Mef'ûl-ü mutlakın taşımak için getirildiği sıfat budur."),
  tok("لِكَثْرَةِ","kathra","noun",["huruf-jarr","lam-taleel","idafa-definiteness","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ظَهَرَ»، وَاللَّامُ لِلتَّعْلِيلِ، وَ«كَثْرَةِ» مُضَافٌ.",
      "A jarr-majrur attaching to «shows», the LAM giving the reason, and «the frequency of» a mudaf.",
      "«ظَهَرَ»ye taalluk eden câr-mecrûr; LÂM ta'lîl içindir, «كَثْرَةِ» muzâftır.",
      segments=[seg("لِ","li","prep"), seg("كَثْرَةِ","kathra","noun")]),
  tok("الِاسْتِعْمَالِ","istimal","noun",["idafa-definiteness","masdar","form-x-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ عَادَ الْبَابُ إِلَى مِعْيَارِهِ الَّذِي فُتِحَ بِهِ.",
      "The mudaf ilayh in jarr — and with it the chapter returns to the ruler it opened with. Everything in it has been measured by USE, and the plain is plain because of how much it has been used.",
      "Mecrûr muzâfun ileyh — bâb, onunla açıldığı ölçüye döner. İçindeki her şey İSTİ'MÂL ile ölçülmüştür; sarîh de ne kadar kullanıldığı için sarîhtir.",
      punct="."),
 ],
 "jumal": [J("ظَهَرَ الْمُرَادُ بِهِ ظُهُورًا بَيِّنًا",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the veiled is that whose intended sense lies hidden, so it is not understood except by an indication.",
 "tr": "Kinâye, murâdı gizli kalan ve ancak bir karîneyle anlaşılandır."},
 "tokens": [
  tok("وَالْكِنَايَةُ","kinaya","noun",["atf-nasaq","mubtada-khabar","kinaya"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْكِنَايَةُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the veiled» is the mubtada in raf'.",
      "Atıf vâvı; «الْكِنَايَةُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْكِنَايَةُ","kinaya","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("اسْتَتَرَ","istatara","verb",["fail","form-viii-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ عَلَى «اِفْتَعَلَ» مِنْ «س ت ر»، وَالْجُمْلَةُ صِلَةٌ — وَالتَّاءُ الثَّانِيَةُ تَاءُ الْوَزْنِ لَا تَاءُ الْأَصْلِ، وَلَمْ تُبْدَلْ لِأَنَّ السِّينَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ.",
      "A past verb on اِفْتَعَلَ from س ت ر; the clause is the sila. Of the two tas you see, the SECOND is the pattern's and the first letter is the root's sin — and the pattern's ta stands unchanged, because sin is not among the letters that force the ibdal. Set it beside اِزْدَادَ and اِطَّلَعَ from chapters 5 and 6: three verbs, one pattern, and the first radical decides what becomes of its ta.",
      "«س ت ر»den «اِفْتَعَلَ» vezninde mâzî fiil; cümle sıladır. Gördüğün iki tâdan İKİNCİSİ veznin tâsıdır, baştaki harf ise kökün sînidir — ve veznin tâsı olduğu gibi durur, zira sîn ibdâl harflerinden değildir. Beşinci ve altıncı bâblardaki «اِزْدَادَ» ve «اِطَّلَعَ» ile yan yana koy: üç fiil, tek vezin; tâsının başına ne geleceğine ilk aslî harf karar verir."),
  tok("الْمُرَادُ","murad","noun",["fail","ism-maful"],
      "فَاعِلٌ مَرْفُوعٌ.", "The fa'il, in raf'.", "Merfû fâil."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«اسْتَتَرَ»، وَالْهَاءُ الْعَائِدُ.",
      "A jarr-majrur attaching to «lies hidden», the HA the returning pronoun.",
      "«اسْتَتَرَ»ye taalluk eden câr-mecrûr; HÂ âid zamîrdir.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("فَلَا","la-nafiya","part",["atf-nasaq","mudari-marfu"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّرْتِيبِ وَالتَّسَبُّبِ، وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "A fa joining in sequence AND in cause — «and so», not merely «and» — with «la» simply denying and governing nothing.",
      "Tertîb ve sebep bildiren âtıfa fâ — sadece «ve» değil, «bu yüzden» — ve amel etmeyen nefy «لَا»sı.",
      segments=[seg("فَ","fa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُفْهَمُ","fahima","verb",["naib-al-fail","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَبِنَاءُ الْمُضَارِعِ لِلْمَجْهُولِ: ضَمُّ أَوَّلِهِ وَفَتْحُ مَا قَبْلَ آخِرِهِ، بِخِلَافِ الْمَاضِي.",
      "A mudari built for the unnamed doer, in raf' — and the present tense is built for it differently from the past: a DAMMA on its first letter, but a FATHA before its last, where the past takes a kasra. اسْتُعْمِلَ against يُفْهَمُ, in one chapter, is the whole pair.",
      "Meçhûl sîgasında merfû muzâri — muzârinin meçhûl binâsı mâzîninkinden farklıdır: başı ÖTRELİ, fakat son harfinden öncesi mâzîdeki gibi esreli değil FETHALIdır. Aynı bâbda «اسْتُعْمِلَ» ile «يُفْهَمُ»: çiftin tamamı."),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ — وَهَذَا الرَّابِعُ فِي خَمْسَةِ أَبْوَابٍ.",
      "The particle of exception, the exception MUFARRAGH — the fourth in five chapters. Four negations, four إِلَّا, and no mustathna minhu named in any of them.",
      "İstisnâ edatı; istisnâ MÜFERRAĞdır — beş bâbda dördüncüsü. Dört nefy, dört «إِلَّا» ve hiçbirinde zikredilmiş bir müstesnâ minh yok."),
  tok("بِقَرِينَةٍ","qarina","noun",["istithna-mufarragh","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُفْهَمُ» — وَهُوَ الْمُسْتَثْنَى الْمُفَرَّغُ، وَبِهِ الْتَقَى هَذَا الْبَابُ بِبَابِ الْأَمْرِ: هُنَاكَ صَرَفَتِ الْقَرِينَةُ الْأَمْرَ عَنِ الْوُجُوبِ، وَهُنَا هِيَ الَّتِي تَفْتَحُ الْمَعْنَى أَصْلًا.",
      "A jarr-majrur attaching to «is understood» — the emptied exception itself. And with it this chapter meets the chapter on the command: there a qarina turned a command aside from obligation, here a qarina is the only thing that opens the meaning at all. One word, two offices, and both of them decisive.",
      "«يُفْهَمُ»a taalluk eden câr-mecrûr — müferrağ müstesnânın kendisi. Bu bâb onunla emir bâbıyla buluşur: orada karîne emri vücûbdan çeviriyordu, burada mânâyı ancak o açıyor. Tek kelime, iki vazife ve ikisi de belirleyici.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("قَرِينَةٍ","qarina","noun")]),
 ],
 "jumal": [J("الْكِنَايَةُ مَا اسْتَتَرَ الْمُرَادُ بِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("فَلَا يُفْهَمُ إِلَّا بِقَرِينَةٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ عَلَى الصِّلَةِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause joined to the sila — i'rabless.",
   "Sılaya ma'tûf fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "istimal":  g("اِسْتِعْمَال", "ع م ل", "noun", "use — what a speaker does with a wording (masdar, Form X)", "isti'mâl; kullanım (masdar)", 4),
 "istamala": g("اِسْتَعْمَلَ", "ع م ل", "verb", "to use, to put to work", "kullanmak", 3),
 "majaz":    g("مَجَاز", "ج و ز", "noun", "the FIGURATIVE — used past its own place, for a relation", "mecâz — alâka sebebiyle kendi yerinin dışında kullanılan", 4),
 "sarih":    g("صَرِيح", "ص ر ح", "noun", "the PLAIN — clear from sheer frequency of use", "sarîh — çok kullanılmakla açık olan", 4),
 "kinaya":   g("كِنَايَة", "ك ن ي", "noun", "the VEILED — understood only by an indication (masdar)", "kinâye — ancak karîneyle anlaşılan (masdar)", 4),
 "alaqa":    g("عَلَاقَة", "ع ل ق", "noun", "the RELATION that licenses a figure of speech", "alâka — mecâzı meşrû kılan münâsebet", 5, plural="عَلَاقَات"),
 "zuhur":    g("ظُهُور", "ظ ه ر", "noun", "a showing, appearing (masdar)", "zuhûr; ortaya çıkma (masdar)", 3),
 "bayyin":   g("بَيِّن", "ب ي ن", "noun", "evident, unmistakable (sifa mushabbaha)", "beyyin; apaçık", 3),
 "kathra":   g("كَثْرَة", "ك ث ر", "noun", "abundance, frequency (masdar)", "kesret; çokluk (masdar)", 3),
 "istatara": g("اِسْتَتَرَ", "س ت ر", "verb", "to lie hidden, to be veiled", "gizlenmek, örtülü kalmak", 4),
 "fahima":   g("فَهِمَ", "ف ه م", "verb", "to understand", "anlamak", 2),
 "pron-3d":  g("هُمَا", None, "pron", "the two of them (dual pronoun)", "onlar ikisi (tesniye zamîri)", 2),
}

def build_morph():
    out = {}
    # اِسْتَعْمَلَ — copied; two packages carry it and they agree.
    s = json.loads((ROOT / "content/samples/kitab-al-waqf/morphology.json").read_text(encoding="utf-8"))
    out["istamala"] = s["verbs"]["istamala"]
    # اِسْتَتَرَ — Form VIII of س ت ر. The sin forces no ibdal, so the pattern's
    # ta stands beside the root's own ta with nothing happening between them.
    out["istatara"] = _sg.derived("بَابُ الِافْتِعَالِ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ",
                                  "اِسْتَتَر", "سْتَتِر", "اِسْتَتِر", "اِسْتِتَار", "مُسْتَتِر",
                                  note="لَمْ تُبْدَلْ تَاءُ الِافْتِعَالِ لِأَنَّ السِّينَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ.")
    # فَهِمَ — sound, bab sami'a. Its passive is the chapter's own second lesson.
    out["fahima"] = _sg.sound1("samia", "فَهِم", "فْهَم", "اِفْهَم", "فَهْم", "فَاهِم",
                               maful="مَفْهُوم", pmz="فُهِمَ", pmd="يُفْهَمُ",
                               note="مِنْ بَابِ سَمِعَ — وَمَجْهُولُ الْمُضَارِعِ يُفْهَمُ بِفَتْحِ مَا قَبْلَ الْآخِرِ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/10.json").write_text(
    json.dumps({"chapter": 10, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 10 for c in man["chapters"]):
    man["chapters"].append({"n": 10, "title": TITLE10})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.10.0"
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة، ثم أقسام اللفظ وضعًا ووضوحًا واستعمالًا، ووجوه البيان",
                   "en": "The opening definitions, the four sources, the wording divided by what it was set down for, how plainly it shows and what it is used for, and the ways a text speaks",
                   "tr": "Açılış tarifleri, deliller, lafzın vaz'ına, vuzûhuna ve isti'mâline göre taksîmi ve beyânın vecihleri"}
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch10:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
