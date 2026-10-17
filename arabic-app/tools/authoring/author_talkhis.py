# -*- coding: utf-8 -*-
"""Build content/samples/talkhis-al-miftah — al-Qazwini's TALKHIS AL-MIFTAH,
the opening of FANN 1, ʿILM AL-MAʿANI.

The Talkhis has been the app's primary balagha source since the badiʿ notes
were written, and roughly half of it — the whole of ʿilm al-maʿani — has been
sitting unread in research/sources/talkhis-al-miftah-balagha.txt. That file is
an Ottoman-Turkish sharh, but the MATN it comments on is quoted inside it in
Arabic and fully vowelled, which is the only reason this package can exist at
all: the definitions below are lifted from those quotations, not translated
back out of the Turkish.

ATTRIBUTION, line by line:
  • ch1 s2, s3, s4 are VERBATIM from the supplied file's own Arabic (lines 161,
    198, 219 of the transcription).
  • ch1 s1, s5 and ch2 s1–s5 are the RECEIVED matn of the Talkhis, where the
    supplied page carries only the Ottoman rendering. Every one of them is a
    sentence the whole balagha tradition quotes; none is composed here.
  • Nothing in this package is an original composition.

Why these ten sentences and not others: they are the book's own opening
DEFINITIONS, they are short, they are parallel to each other, and — the reason
this is a graded reader and not an anthology — the second chapter's definition
of ʿilm al-maʿani is built on the same frame as Mukhtasar al-Manar's definition
of usul al-fiqh, word for word. Two disciplines, two centuries apart, defining
themselves with one sentence shape. A reader who has done the Manar can read
that line before it is explained to them, and that is what a graded library is
for.
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

CH1, CH2 = [], []

# ================================================================ CHAPTER 1
CH1.append({"id": "s1", "translation": {
 "en": "Fasaha is predicated of the single word, of the utterance, and of the speaker.",
 "tr": "Fesâhat ile müfred, kelâm ve mütekellim vasıflanır."},
 "tokens": [
  tok("الْفَصَاحَةُ","fasaha","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «فَصُحَ» مِنْ بَابِ كَرُمَ، وَأَصْلُهُ الظُّهُورُ وَالْخُلُوصُ، وَمِنْهُ «أَفْصَحَ الصُّبْحُ» إِذَا ظَهَرَ.",
      "The mubtada in raf' — the masdar of فَصُحَ of the bab of كَرُمَ, whose root sense is CLEARNESS: أَفْصَحَ الصُّبْحُ, «the morning came clear». The whole discipline begins from a word about daylight.",
      "Merfû mübtedâ — kerume bâbından «فَصُحَ»in masdarı; kök mânâsı AÇIKLIKtır: «أَفْصَحَ الصُّبْحُ» — «sabah aydınlandı». Bütün ilim, gün ışığına dair bir kelimeden başlar."),
  tok("يُوصَفُ","wasafa","verb",["naib-al-fail","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «الْفَصَاحَةُ».",
      "A mudari built for the unnamed doer, in raf' — and the clause stands in the position of raf' as the khabar of «fasaha». WHO does the predicating is left unsaid because it does not matter: this is a statement about the word's range, not about anyone's usage.",
      "Meçhûl sîgasında merfû muzâri — ve cümle, «الْفَصَاحَةُ»in haberi olarak mahallen merfûdur. Vasfeden KİM olduğu söylenmez, çünkü mühim değildir: bu, birinin kullanımına dair değil, kelimenin sahasına dair bir hükümdür."),
  tok("بِهَا","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُوصَفُ»، وَالضَّمِيرُ عَائِدٌ عَلَى الْفَصَاحَةِ.",
      "A jarr-majrur attaching to «is predicated», the pronoun going back to fasaha. Note that the jarr phrase is NOT the naib al-fa'il here: the deputy is the marfu' noun that follows.",
      "«يُوصَفُ»a taalluk eden câr-mecrûr; zamir fesâhate râcidir. Dikkat: buradaki câr-mecrûr NÂİB-İ FÂİL değildir; nâib, ardından gelen merfû isimdir.",
      segments=[seg("بِ","bi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("الْمُفْرَدُ","mufrad","noun",["naib-al-fail"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — وَهُوَ الْكَلِمَةُ الْوَاحِدَةُ، وَسَيُحَدُّ وَصْفُهُ فِي الْجُمْلَةِ التَّالِيَةِ.",
      "The naib al-fa'il in raf' — the single word, whose fasaha the next sentence defines. Three subjects are named here and the book will define the first two and leave the third to be inferred: a speaker is fasih when his speech is.",
      "Merfû nâib-i fâil — tek kelime; fesâhati bir sonraki cümlede tarif edilecek. Burada üç mevzu anılır; kitap ilk ikisini tarif eder, üçüncüsünü çıkarıma bırakır: mütekellim, kelâmı fasîh olduğunda fasîhtir."),
  tok("وَالْكَلَامُ","kalam","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ — وَهُوَ الْمُرَكَّبُ الْمُفِيدُ.",
      "Joined, in raf' — the composed utterance that conveys a complete sense.",
      "Ma'tûf, merfû — faydalı mürekkeb, yani tam mânâ ifade eden söz.",
      segments=[seg("وَ","wa","conj"), seg("الْكَلَامُ","kalam","noun")]),
  tok("وَالْمُتَكَلِّمُ","mutakallim","noun",["atf-nasaq","ism-fail","form-v-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «تَكَلَّمَ» عَلَى مُتَفَعِّلٍ.",
      "Joined, in raf' — the ism fa'il of تَكَلَّمَ on مُتَفَعِّل. The kasra under the ʿayn is what makes it the SPEAKER and not the thing spoken; مُتَكَلَّم with a fatha would be the latter, and the two are one dot of vowel apart.",
      "Ma'tûf, merfû — «تَكَلَّمَ»nin MÜTEFA'İL vezninde ism-i fâili. Ayn harfindeki kesra, onu KONUŞAN yapan şeydir, konuşulan değil; fethalı «مُتَكَلَّم» ikincisi olurdu ve ikisi tek bir hareke farkıyla ayrılır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَكَلِّمُ","mutakallim","noun")], punct="."),
 ],
 "jumal": [J("يُوصَفُ بِهَا الْمُفْرَدُ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
   "A verbal clause in the position of raf', the khabar of the mubtada.",
   "Mübtedânın haberi olarak mahallen merfû fiil cümlesi.")]})

CH1.append({"id": "s2", "translation": {
 "en": "The fasaha of a single word is its being free of harshness between its letters, of strangeness, and of departure from the rule.",
 "tr": "Müfredin fesâhati; tenâfür-i hurûftan, garâbetten ve mühâlefetü'l-kıyâstan hâlî olmasıdır."},
 "tokens": [
  tok("فَفَصَاحَةُ","fasaha","noun",["mubtada-khabar","idafa-definiteness"],
      "الْفَاءُ لِلتَّفْصِيلِ، وَ«فَصَاحَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "The fa opens the detailing of what was just listed, and «the fasaha of» is the mubtada in raf' and a mudaf. Three subjects were named; the book now takes them one at a time, and the fa is what says so.",
      "Fâ tafsîl içindir; «فَصَاحَةُ» merfû mübtedâ ve muzâftır. Üç mevzu anıldı; kitap şimdi onları teker teker ele alır ve bunu söyleyen harf fâdır.",
      segments=[seg("فَ","fa","conj"), seg("فَصَاحَةُ","fasaha","noun")]),
  tok("الْمُفْرَدِ","mufrad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyh."),
  tok("خُلُوصُهُ","khulus","noun",["mubtada-khabar","masdar","imal-al-masdar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ وَهُوَ فَاعِلُ الْمَصْدَرِ مَعْنًى — مَصْدَرُ «خَلَصَ» وَهُوَ لَازِمٌ، فَلَا يَنْصِبُ مَفْعُولًا وَإِنَّمَا يَتَعَدَّى بِـ«مِنْ».",
      "The khabar in raf' and a mudaf, the ha its mudaf ilayh and the masdar's FA'IL in meaning. خَلَصَ is intransitive, so this masdar puts nothing in nasb and reaches what it is free OF through a min — the same lesson chapter 16 of the Manar drew from الْعِلْمُ بِالْكِتَابِ: a masdar inherits its verb's habits exactly, and nothing more.",
      "Merfû haber ve muzâf; hâ muzâfun ileyhtir ve mânen masdarın FÂİLİdir. «خَلَصَ» lâzımdır; bu yüzden bu masdar hiçbir şeyi nasb etmez ve hâlî olduğu şeye «مِنْ» ile ulaşır — Menâr'ın on altıncı bâbının «الْعِلْمُ بِالْكِتَابِ»den çıkardığı dersin aynısı: masdar, fiilinin âdetini aynen miras alır, fazlasını değil.",
      segments=[seg("خُلُوصُ","khulus","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«خُلُوصُ» — وَهِيَ لِلْمُجَاوَزَةِ.",
      "A jarr letter attaching to «being free», naming the thing departed FROM.",
      "«خُلُوص»a taalluk eden cer harfi — mücâveze içindir; kendisinden uzaklaşılan şeyi bildirir."),
  tok("تَنَافُرِ","tanafur","noun",["idafa-definiteness","masdar","form-vi-verbs"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ — مَصْدَرُ «تَنَافَرَ» عَلَى تَفَاعُلٍ، وَبِنَاءُ التَّفَاعُلِ لِلْمُشَارَكَةِ: الْحُرُوفُ يَنْفِرُ بَعْضُهَا مِنْ بَعْضٍ.",
      "Majrur by «min» and a mudaf — the Form VI masdar of تَنَافَرَ. Form VI is the pattern of MUTUAL action, and that is the whole content of the term: it is not that a letter is hard, but that letters shy away from one another. مُسْتَشْزِرَات is the tradition's example, and every one of its letters is ordinary on its own.",
      "«مِنْ» ile mecrûr ve muzâf — «تَنَافَرَ»nin TEFÂUL vezninde masdarı. Tefâul, MÜŞÂREKET kalıbıdır ve terimin bütün muhtevâsı budur: bir harfin ağır olması değil, harflerin birbirinden ürkmesidir. Geleneğin misâli «مُسْتَشْزِرَات»tır ve harflerinin her biri tek başına sıradandır."),
  tok("الْحُرُوفِ","harf","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «حَرْفٍ».",
      "The mudaf ilayh in jarr — the plural of حَرْف.",
      "Mecrûr muzâfun ileyh — «حَرْف»in cemi."),
  tok("وَالْغَرَابَةِ","gharaba","noun",["atf-nasaq","masdar"],
      "مَعْطُوفٌ مَجْرُورٌ — وَهِيَ أَنْ تَكُونَ الْكَلِمَةُ وَحْشِيَّةً لَا يَظْهَرُ مَعْنَاهَا.",
      "Joined, in jarr — a word being so out of use that its sense does not show. Note where the fault is placed: not in the hearer's learning but in the word's own obscurity.",
      "Ma'tûf, mecrûr — kelimenin, mânâsı ortaya çıkmayacak kadar vahşî olmasıdır. Kusurun nereye konduğuna dikkat: dinleyenin bilgisine değil, kelimenin kendi kapalılığına.",
      segments=[seg("وَ","wa","conj"), seg("الْغَرَابَةِ","gharaba","noun")]),
  tok("وَمُخَالَفَةِ","mukhalafa","noun",["atf-nasaq","masdar","form-iii-verbs","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «خَالَفَ» عَلَى مُفَاعَلَةٍ.",
      "Joined and majrur, itself a mudaf — the Form III masdar of خَالَفَ on مُفَاعَلَة, the same root the Manar's last chapters used for «contrary to analogy».",
      "Ma'tûf, mecrûr ve muzâf — «خَالَفَ»nin MÜFÂALE vezninde masdarı; Menâr'ın son bâblarının «kıyâsa muhâlif» için kullandığı kökün aynısı.",
      segments=[seg("وَ","wa","conj"), seg("مُخَالَفَةِ","mukhalafa","noun")]),
  tok("الْقِيَاسِ","qiyas","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْمُرَادُ بِهِ هُنَا قِيَاسُ الصَّرْفِ لَا قِيَاسُ الْأُصُولِ: الْأَجْلَلِ فِي الْبَيْتِ الْمَشْهُورِ لَمْ يُدْغَمْ وَحَقُّهُ الْإِدْغَامُ.",
      "The mudaf ilayh in jarr — and «the rule» here means the rule of SARF, not the analogy of usul. The tradition's example is الْأَجْلَل, left unassimilated where the language requires اَلْأَجَلّ. The same Arabic word names two different disciplines' methods, and a reader coming from the Manar has to notice the switch.",
      "Mecrûr muzâfun ileyh — ve buradaki «kıyâs», usûlün kıyâsı değil SARF kâidesidir. Geleneğin misâli, idgâmı vâcib iken idgâm edilmemiş «الْأَجْلَل»dir. Aynı Arapça kelime iki ayrı ilmin usûlünü adlandırır ve Menâr'dan gelen okuyucunun bu geçişi fark etmesi gerekir.",
      punct="."),
 ],
 "jumal": [J("فَفَصَاحَةُ الْمُفْرَدِ خُلُوصُهُ مِنْ تَنَافُرِ الْحُرُوفِ",
   "جُمْلَةٌ اسْمِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, with no position in i'rab.",
   "İsim cümlesi; i'râbdan mahalli yoktur.")]})

CH1.append({"id": "s3", "translation": {
 "en": "And the fasaha of an utterance is its being free of weak composition, of harshness between its words, and of obscurity — together with their own fasaha.",
 "tr": "Kelâmın fesâhati; kelimelerinin fasîh olmasıyla birlikte, za'f-ı te'lîften, tenâfür-i kelimâttan ve ta'kîdden hâlî olmasıdır."},
 "tokens": [
  tok("وَفَصَاحَةُ","fasaha","noun",["mubtada-khabar","idafa-definiteness","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«فَصَاحَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَالتَّرْكِيبُ نَفْسُهُ الَّذِي فِي الْجُمْلَةِ قَبْلَهَا حَرْفًا بِحَرْفٍ.",
      "A joining waw, and «the fasaha of» is the mubtada in raf' and a mudaf — the SAME construction as the sentence before it, letter for letter. A matn that defines two things in one shape is teaching the shape as well as the things.",
      "Atıf vâvı; «فَصَاحَةُ» merfû mübtedâ ve muzâftır — bir öncekiyle harfi harfine AYNI terkîb. İki şeyi tek kalıpta tarif eden bir metin, şeylerle birlikte kalıbı da öğretiyordur.",
      segments=[seg("وَ","wa","conj"), seg("فَصَاحَةُ","fasaha","noun")]),
  tok("الْكَلَامِ","kalam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الثَّانِي مِنَ الثَّلَاثَةِ.",
      "The mudaf ilayh in jarr — the second of the three.",
      "Mecrûr muzâfun ileyh — üçün ikincisi."),
  tok("خُلُوصُهُ","khulus","noun",["mubtada-khabar","masdar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "The khabar in raf' and a mudaf, the ha its mudaf ilayh — and it is the same word, in the same office, as the sentence before.",
      "Merfû haber ve muzâf; hâ muzâfun ileyhtir — ve bir öncekiyle aynı kelime, aynı vazifede.",
      segments=[seg("خُلُوصُ","khulus","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«خُلُوصُ».",
      "A jarr letter attaching to «being free».",
      "«خُلُوص»a taalluk eden cer harfi."),
  tok("ضَعْفِ","daf","noun",["idafa-definiteness","masdar"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ — وَضَعْفُ التَّأْلِيفِ مُخَالَفَةُ قَوَاعِدِ النَّحْوِ، كَـ«ضَرَبَ غُلَامُهُ زَيْدًا» لِعَوْدِ الضَّمِيرِ عَلَى مُتَأَخِّرٍ لَفْظًا وَرُتْبَةً.",
      "Majrur by «min» and a mudaf — and weak composition means going against the rules of NAHW, as in ضَرَبَ غُلَامُهُ زَيْدًا, where a pronoun points forward to a noun that comes later both in words and in rank. Notice the division of labour: the first sentence's fault was in SARF, this one's is in nahw, and balagha begins only after both are satisfied.",
      "«مِنْ» ile mecrûr ve muzâf — za'f-ı te'lîf, NAHİV kâidelerine muhâlefettir; «ضَرَبَ غُلَامُهُ زَيْدًا» gibi: zamir, hem lafzan hem rütbeten sonra gelen bir isme dönmüştür. İş bölümüne dikkat: birinci cümlenin kusuru SARFtaydı, bunun ki nahivdedir; belâgat ise ancak ikisi de sağlandıktan sonra başlar."),
  tok("التَّأْلِيفِ","talif","noun",["idafa-definiteness","masdar","form-ii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «أَلَّفَ» عَلَى تَفْعِيلٍ، أَيْ ضَمُّ الْكَلِمَاتِ بَعْضِهَا إِلَى بَعْضٍ.",
      "The mudaf ilayh in jarr — the Form II masdar of أَلَّفَ: the putting of words together. The word is about ASSEMBLY, so a fault in it is a fault of joinery, not of vocabulary.",
      "Mecrûr muzâfun ileyh — «أَلَّفَ»nin TEF'ÎL vezninde masdarı: kelimeleri birbirine katmak. Kelime BİRLEŞTİRMEye dairdir; öyleyse ondaki kusur, kelime hazinesinin değil, marangozluğun kusurudur."),
  tok("وَتَنَافُرِ","tanafur","noun",["atf-nasaq","masdar","form-vi-verbs","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ وَهُوَ مُضَافٌ — وَهُوَ التَّنَافُرُ نَفْسُهُ الْمَذْكُورُ فِي الْمُفْرَدِ، إِلَّا أَنَّهُ هُنَا بَيْنَ الْكَلِمَاتِ لَا بَيْنَ الْحُرُوفِ.",
      "Joined and majrur, itself a mudaf — the very same tanafur named for the single word, except that here it is between WORDS and there between letters. One term, two scales, and the matn marks the difference only by what it annexes the word to.",
      "Ma'tûf, mecrûr ve muzâf — müfredde anılan tenâfürün ta kendisi; şu farkla ki burada harfler arasında değil KELİMELER arasındadır. Tek terim, iki ölçek; ve metin farkı yalnız kelimeyi neye izâfe ettiğiyle gösterir.",
      segments=[seg("وَ","wa","conj"), seg("تَنَافُرِ","tanafur","noun")]),
  tok("الْكَلِمَاتِ","kalima","noun",["idafa-definiteness","jam-muannath-salim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "The mudaf ilayh, majrur by the kasra — a sound feminine plural, whose jarr looks exactly like a singular's.",
      "Kesra ile mecrûr muzâfun ileyh — cem'-i müennes sâlim; cerri müfredin cerri gibi görünür."),
  tok("وَالتَّعْقِيدِ","taqid","noun",["atf-nasaq","masdar","form-ii-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ «عَقَّدَ» عَلَى تَفْعِيلٍ، وَسَيُحَدُّ فِي الْجُمْلَةِ التَّالِيَةِ.",
      "Joined, in jarr — the Form II masdar of عَقَّدَ, «to knot», and the next sentence defines it. Three faults are listed and only the third is given a definition, because only the third is not obvious from its name.",
      "Ma'tûf, mecrûr — «عَقَّدَ»nin TEF'ÎL vezninde masdarı, «düğümlemek»; bir sonraki cümle onu tarif eder. Üç kusur sayılır ve yalnız üçüncüsü tarif edilir; zira yalnız üçüncüsü adından anlaşılmaz.",
      segments=[seg("وَ","wa","conj"), seg("التَّعْقِيدِ","taqid","noun")]),
  tok("مَعَ","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«خُلُوصُ».",
      "A zarf in nasb and a mudaf, attaching to «being free» — and this one word is the hinge of the definition: an utterance is not fasih merely by escaping the three faults, but by escaping them WHILE its words are themselves fasih. A sound sentence made of obscure words is still not fasih.",
      "Zarfiyyet üzere mansub zarf ve muzâf; «خُلُوص»a taalluk eder — ve bu tek kelime tarifin menteşesidir: kelâm, yalnız üç kusurdan kurtulmakla fasîh olmaz; kelimeleri de fasîh OLDUĞU HÂLDE kurtulmakla olur. Kapalı kelimelerden kurulmuş sağlam bir cümle yine fasîh değildir."),
  tok("فَصَاحَتِهَا","fasaha","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ عَائِدٌ عَلَى «الْكَلِمَاتِ» — وَجَمْعُ غَيْرِ الْعَاقِلِ يُعَامَلُ مُعَامَلَةَ الْمُفْرَدَةِ الْمُؤَنَّثَةِ.",
      "The mudaf ilayh in jarr and itself a mudaf, the ha annexed to it — and that ha goes back to «the WORDS», three words earlier, not to the utterance beside it. A plural of what does not reason is referred to as a feminine singular, which is why a ها and not a هُنَّ, and why the antecedent is easy to lose.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf; hâ ona izâfe edilmiştir — ve o hâ, yanındaki kelâma değil, üç kelime öncesindeki «الْكَلِمَات»a râcidir. Âkil olmayanın cemi, müfred müennes muâmelesi görür; «هُنَّ» değil «هَا» olmasının ve merciin kolayca kaybedilmesinin sebebi budur.",
      segments=[seg("فَصَاحَتِ","fasaha","noun"), seg("هَا","pron-3fs","pron")], punct="."),
 ],
 "jumal": [J("وَفَصَاحَةُ الْكَلَامِ خُلُوصُهُ مِنْ ضَعْفِ التَّأْلِيفِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

CH1.append({"id": "s4", "translation": {
 "en": "And obscurity is that the utterance should not be clear in pointing to what was meant, through a flaw either in the ordering or in the passage of thought.",
 "tr": "Ta'kîd; ya nazımdaki ya da intikaldeki bir bozukluk sebebiyle, kelâmın murâda delâletinin açık olmamasıdır."},
 "tokens": [
  tok("وَالتَّعْقِيدُ","taqid","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«التَّعْقِيدُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A resuming waw, and «obscurity» is the mubtada in raf'.",
      "İsti'nâf vâvı; «التَّعْقِيد» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("التَّعْقِيدُ","taqid","noun")]),
  tok("أَنْ","an-nasiba","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْمُبْتَدَإِ.",
      "A masdar-making letter putting the verb into nasb, and the masdar it forms is the khabar. Defining a term with أَنْ + a verb rather than with a noun is how a book defines a STATE rather than a thing.",
      "Masdariyye ve nâsıbe harfi; teşkil ettiği masdar-ı müevvel, mübtedânın haberidir. Bir terimi isimle değil «أَنْ» + fiil ile tarif etmek, bir kitabın bir ŞEYİ değil bir HÂLİ tarif etme biçimidir."),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا — وَالنَّاصِبُ «أَنْ» لَا «لَا»، فَـ«يَكُونَ» مَنْصُوبٌ بِمَا قَبْلَ النَّافِيَةِ.",
      "A bare negation — and note whose nasb the verb wears: «an» is the governor and «la» merely negates between them, so the fatha on «yakuna» reaches across the negation to the particle before it. A governor is not blocked by a word that governs nothing.",
      "Amel etmeyen nefiy — ve fiilin nasbı kimden: âmil «أَنْ»dır, «لَا» yalnız aralarında nefyeder; öyleyse «يَكُونَ»nin fethası, nefiy harfinin üzerinden aşıp öncesindeki edata ulaşır. Âmil, hiçbir şeye amel etmeyen bir kelimeyle engellenmez."),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْوَاوُ ثَابِتَةٌ لِأَنَّ النَّصْبَ لَا يُسْكِنُ الْآخِرَ.",
      "An incomplete mudari in nasb after «an», its mark the fatha — and the waw stands, because nasb puts a vowel on the last letter and leaves the long vowel alone. Under jazm the same verb would be لَمْ يَكُنْ and the waw would be gone.",
      "«أَنْ» ile mansub nâkıs muzâri; alâmeti fethadır — ve vâv durur, zira nasb son harfe hareke koyar, med harfine dokunmaz. Cezm altında aynı fiil «لَمْ يَكُنْ» olur ve vâv gider."),
  tok("الْكَلَامُ","kalam","noun",["kana-wa-akhawatuha"],
      "اسْمُ «يَكُونَ» مَرْفُوعٌ.",
      "The ism of «yakuna», in raf'.",
      "«يَكُونَ»nin merfû ismi."),
  tok("ظَاهِرَ","zahir","noun",["kana-wa-akhawatuha","idafa-lafziyya","ism-fail","idafa-definiteness"],
      "خَبَرُ «يَكُونَ» مَنْصُوبٌ وَهُوَ مُضَافٌ — وَهَذِهِ إِضَافَةٌ لَفْظِيَّةٌ لَا تُفِيدُ تَعْرِيفًا، لِأَنَّ الْمُضَافَ اسْمُ فَاعِلٍ أُضِيفَ إِلَى فَاعِلِهِ.",
      "The khabar of «yakuna», in nasb and a MUDAF — and this is an idafa LAFZIYYA: it makes nothing definite. The mudaf is an ism fa'il annexed to its own fa'il, so the annexation only saves a tanwin; the phrase stays indefinite, which is exactly what a khabar needs to be. Read it as ظَاهِرًا دَلَالَتُهُ and nothing changes but the tidiness.",
      "«يَكُونَ»nin mansub haberi ve MUZÂF — ve bu bir izâfet-i LAFZİYYEdir: hiçbir şeyi marife yapmaz. Muzâf, kendi fâiline izâfe edilmiş bir ism-i fâildir; öyleyse izâfet yalnız bir tenvin tasarrufudur, terkîb nekre kalır — ki haberin olması gereken şey tam da budur. «ظَاهِرًا دَلَالَتُهُ» diye okuyun; derli topluluktan başka hiçbir şey değişmez."),
  tok("الدَّلَالَةِ","dalala","noun",["idafa-definiteness","idafa-lafziyya"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فَاعِلُ «ظَاهِرَ» مَعْنًى: الدَّلَالَةُ هِيَ الَّتِي تَظْهَرُ.",
      "The mudaf ilayh in jarr — and the fa'il of «clear» in meaning: it is the POINTING that is clear or not. The same double reading the Manar's بَذْلُ الْفَقِيهِ carried, on a participle instead of a masdar.",
      "Mecrûr muzâfun ileyh — ve mânen «ظَاهِرَ»in fâilidir: açık olan yahut olmayan, DELÂLETtir. Menâr'ın «بَذْلُ الْفَقِيهِ»inin taşıdığı çift okuyuşun aynısı; masdarda değil ism-i fâilde."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«الدَّلَالَةِ» — وَالدَّلَالَةُ تَتَعَدَّى بِعَلَى دَائِمًا.",
      "A jarr letter attaching to «the pointing» — and دَلَالَة always reaches its object with an ʿala. A jarr letter hanging on a masdar, once more.",
      "«الدَّلَالَة»e taalluk eden cer harfi — ve «delâlet» mef'ûlüne dâimâ «عَلَى» ile ulaşır. Yine bir masdara asılmış câr-mecrûr."),
  tok("الْمُرَادِ","murad","noun",["huruf-jarr","ism-maful","form-iv-verbs"],
      "مَجْرُورٌ بِـ«عَلَى» — اسْمُ مَفْعُولٍ مِنْ «أَرَادَ» عَلَى مُفْعَل، وَأَصْلُهُ «مُرْوَد»، نُقِلَتْ حَرَكَةُ الْوَاوِ إِلَى السَّاكِنِ قَبْلَهَا ثُمَّ قُلِبَتْ أَلِفًا.",
      "Majrur by «ala» — the ism maf'ul of أَرَادَ on مُفْعَل, whose origin is مُرْوَد: the waw's vowel moved back onto the silent letter before it and the waw itself turned alif. A hollow root's participle carries its i'lal on its face.",
      "«عَلَى» ile mecrûr — «أَرَادَ»nin MUF'AL vezninde ism-i mef'ûlü; aslı «مُرْوَد»dır: vâvın harekesi öncesindeki sâkine nakledilmiş, sonra vâv elife kalbolmuştur. Ecvef bir kökün ism-i mef'ûlü, i'lâlini yüzünde taşır."),
  tok("لِخَلَلٍ","khalal","noun",["huruf-jarr","maful-lah"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ظَاهِرَ»، وَاللَّامُ لِلتَّعْلِيلِ — وَتَنْكِيرُ «خَلَلٍ» لِلْعُمُومِ: أَيُّ خَلَلٍ كَانَ.",
      "A jarr-majrur attaching to «clear», the lam naming the CAUSE — and «a flaw» is indefinite on purpose: any flaw at all. The same use of the tanwin the Manar made of لِعُذْرٍ.",
      "«ظَاهِرَ»e taalluk eden câr-mecrûr; lâm ta'lîl içindir — ve «خَلَلٍ»in nekreliği umûm içindir: herhangi bir bozukluk. Menâr'ın «لِعُذْرٍ»de yaptığı tenvin kullanımının aynısı.",
      segments=[seg("لِ","li","prep"), seg("خَلَلٍ","khalal","noun")]),
  tok("إِمَّا","imma","part",["atf-nasaq"],
      "حَرْفُ تَفْصِيلٍ وَتَخْيِيرٍ، وَلَا بُدَّ مِنْ تَكْرَارِهَا.",
      "A letter of DETAILING — it splits what came before into named cases, and it never comes alone: an إِمَّا always has a second إِمَّا answering it. The pair is one word doing one job in two places.",
      "Tafsîl ve tahyîr harfi — kendisinden öncekini isimli hâllere ayırır ve asla yalnız gelmez: bir «إِمَّا»nın mutlaka kendisine cevap veren ikinci bir «إِمَّا»sı vardır. Bu çift, tek bir vazifeyi iki yerde gören tek kelimedir."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِمَحْذُوفٍ صِفَةٍ لِـ«خَلَلٍ» — أَيْ خَلَلٍ كَائِنٍ فِي النَّظْمِ.",
      "A jarr letter attaching to something UNSAID — a description of «a flaw»: a flaw that IS in the ordering. Nothing hangs in the air, so where no governor is written the grammarians supply one, and naming what was supplied is part of the i'rab.",
      "SÖYLENMEMİŞ bir şeye taalluk eden cer harfi — «خَلَلٍ»in sıfatı: nazımda BULUNAN bir bozukluk. Hiçbir şey boşlukta durmaz; âmil yazılmamışsa nahivciler onu takdîr eder ve takdîr edileni adlandırmak i'râbın bir parçasıdır."),
  tok("النَّظْمِ","nazm","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي» — وَهُوَ تَرْتِيبُ الْأَلْفَاظِ، وَالْخَلَلُ فِيهِ هُوَ التَّعْقِيدُ اللَّفْظِيُّ.",
      "Majrur by «fi» — the ORDERING of the words, and a flaw in it is the LAFZI kind of obscurity: something has come between two words that belong together.",
      "«فِي» ile mecrûr — lafızların tertîbi; ondaki bozukluk, LAFZÎ ta'kîddir: birbirine ait iki kelimenin arasına bir şey girmiştir."),
  tok("وَإِمَّا","imma","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ وَ«إِمَّا» الثَّانِيَةُ — وَبِهَا تَمَّتِ الْقِسْمَةُ.",
      "The waw joins and this is the SECOND «imma» — and with it the division is complete. A reader who met the first one has been waiting for this word since four words ago.",
      "Vâv atfeder ve bu İKİNCİ «إِمَّا»dır — onunla taksîm tamamlanır. Birincisini gören okuyucu, dört kelimedir bu kelimeyi beklemektedir.",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِمَا تَعَلَّقَ بِهِ الْأَوَّلُ.",
      "A jarr letter attaching where the first one attached.",
      "Birincisinin taalluk ettiği yere taalluk eden cer harfi."),
  tok("الِانْتِقَالِ","intiqal","noun",["huruf-jarr","masdar","form-viii-verbs"],
      "مَجْرُورٌ بِـ«فِي» — مَصْدَرُ «اِنْتَقَلَ» عَلَى اِفْتِعَالٍ، وَالْمُرَادُ انْتِقَالُ الذِّهْنِ مِنَ الْمَعْنَى الْأَوَّلِ إِلَى الْمَقْصُودِ، وَالْخَلَلُ فِيهِ هُوَ التَّعْقِيدُ الْمَعْنَوِيُّ.",
      "Majrur by «fi» — the Form VIII masdar of اِنْتَقَلَ, and what is meant is the mind's PASSAGE from the first sense to the one intended; a flaw there is the MAʿNAWI kind of obscurity. The tradition's example is لِتَجْمُدَا: the poet wanted joy and the hearer's mind travels to dry eyes. Nothing is wrong with the ordering at all, and the line still fails.",
      "«فِي» ile mecrûr — «اِنْتَقَلَ»nin İFTİÂL vezninde masdarı; kastedilen, zihnin ilk mânâdan maksûda GEÇİŞİdir ve ondaki bozukluk MÂNEVÎ ta'kîddir. Geleneğin misâli «لِتَجْمُدَا»dır: şâir sevinci kastetmiştir, dinleyenin zihni ise kurumuş gözlere gider. Nazımda hiçbir kusur yoktur ve mısra yine de başarısızdır.",
      punct="."),
 ],
 "jumal": [J("أَنْ لَا يَكُونَ الْكَلَامُ ظَاهِرَ الدَّلَالَةِ",
   "الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ «التَّعْقِيدُ».",
   "The masdar muawwal, in the position of raf' as the khabar of «obscurity».",
   "Masdar-ı müevvel, «التَّعْقِيد»in haberi olarak mahallen merfûdur.")]})

CH1.append({"id": "s5", "translation": {
 "en": "And obscurity is of two kinds: of the wording, and of the sense.",
 "tr": "Ta'kîd iki kısımdır: lafzî ve ma'nevî."},
 "tokens": [
  tok("وَالتَّعْقِيدُ","taqid","noun",["mubtada-khabar","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«التَّعْقِيدُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw, and «obscurity» is the mubtada in raf' — the term is named three times in three consecutive sentences: listed, defined, divided. That is the matn's standard order and it is worth recognising as a shape.",
      "Atıf vâvı; «التَّعْقِيد» merfû mübtedâdır — terim üç ardışık cümlede üç defa anılır: sayılır, tarif edilir, taksîm edilir. Metnin mutâd sırası budur ve bir kalıp olarak tanınmaya değer.",
      segments=[seg("وَ","wa","conj"), seg("التَّعْقِيدُ","taqid","noun")]),
  tok("ضَرْبَانِ","darb","noun",["mubtada-khabar","al-muthanna"],
      "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى — وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الْمُفْرَدِ.",
      "The khabar in raf', and its sign is the ALIF because it is a dual — i'rab by a LETTER, not by a vowel. The nun that follows stands in for the singular's tanwin, which is why it drops the moment the word becomes a mudaf.",
      "Merfû haber; ref' alâmeti, tesniye olduğu için ELİFtir — hareke ile değil HARF ile i'râb. Ardındaki nûn, müfredin tenvîninden bedeldir; kelime muzâf olur olmaz düşmesinin sebebi budur.",
      punct="："),
  tok("لَفْظِيٌّ","lafzi","noun",["badal"],
      "بَدَلٌ مِنْ «ضَرْبَانِ» مَرْفُوعٌ، أَوْ خَبَرُ مُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «أَحَدُهُمَا» — اسْمٌ مَنْسُوبٌ إِلَى اللَّفْظِ.",
      "A badal of «two kinds», in raf' — or the khabar of an unspoken mubtada, «one of the two is…». Both readings are given by the commentaries and neither changes the case. A nisba noun built on لَفْظ: the doubled ya is the mark of relation and the kasra before it is required by it.",
      "«ضَرْبَانِ»den merfû bedel — yahut takdîri «أَحَدُهُمَا» olan mahzûf bir mübtedânın haberi. Şârihler her iki okuyuşu da verir ve hiçbiri i'râbı değiştirmez. «لَفْظ»a nisbet edilmiş isim: şeddeli yâ nisbet alâmetidir, öncesindeki kesra da onun gereğidir."),
  tok("وَمَعْنَوِيٌّ","manawi","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمٌ مَنْسُوبٌ إِلَى الْمَعْنَى، وَأَصْلُهُ «مَعْنَيِيٌّ»، فَقُلِبَتِ الْيَاءُ الْأُولَى وَاوًا لِأَنَّ الْأَلِفَ الْمَقْصُورَةَ ثَالِثَةٌ فَصَاعِدًا تُقْلَبُ فِي النِّسْبَةِ.",
      "Joined, in raf' — a nisba built on مَعْنًى, and its origin is مَعْنَيِيّ: a maqsur alif standing third or later turns WAW when the nisba is made. That is why the two halves of this pair do not look alike, and the difference is entirely a rule of sarf, not of meaning.",
      "Ma'tûf, merfû — «مَعْنًى»ya nisbet; aslı «مَعْنَيِيّ»dir: üçüncü ve sonrasında bulunan elif-i maksûre, nisbette VÂVa kalbolur. Bu çiftin iki yarısının birbirine benzememesinin sebebi budur ve fark tamamen bir sarf kâidesidir, mânâ farkı değil.",
      segments=[seg("وَ","wa","conj"), seg("مَعْنَوِيٌّ","manawi","noun")], punct="."),
 ],
 "jumal": [J("وَالتَّعْقِيدُ ضَرْبَانِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

# ================================================================ CHAPTER 2
CH2.append({"id": "s1", "translation": {
 "en": "And balagha in an utterance is its conforming to what the situation calls for, together with its own fasaha.",
 "tr": "Kelâmda belâgat; fesâhatiyle birlikte, muktezâ-yı hâle mutâbık olmasıdır."},
 "tokens": [
  tok("وَالْبَلَاغَةُ","balagha-n","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْبَلَاغَةُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «بَلُغَ» مِنْ بَابِ كَرُمَ، وَأَصْلُهُ الْوُصُولُ وَالِانْتِهَاءُ.",
      "A resuming waw, and «balagha» is the mubtada in raf' — the masdar of بَلُغَ of the bab of كَرُمَ, whose root sense is ARRIVAL. Speech that has balagha is speech that has got there.",
      "İsti'nâf vâvı; «الْبَلَاغَة» merfû mübtedâdır — kerume bâbından «بَلُغَ»in masdarı; kök mânâsı ULAŞMAKtır. Belâgati olan söz, varması gereken yere varmış sözdür.",
      segments=[seg("وَ","wa","conj"), seg("الْبَلَاغَةُ","balagha-n","noun")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْبَلَاغَةُ» — أَيِ الْبَلَاغَةُ مُعْتَبَرَةً فِي الْكَلَامِ.",
      "A jarr letter attaching to an unsaid word — «balagha, TAKEN in respect of an utterance». The phrase is there because balagha is about to be defined twice, once for each of the two things it may be predicated of.",
      "SÖYLENMEMİŞ bir kelimeye taalluk eden cer harfi — «kelâmda İTİBAR EDİLDİĞİNDE belâgat». Bu ibare oradadır, çünkü belâgat iki defa tarif edilecektir: vasıflandığı iki şeyin her biri için bir defa."),
  tok("الْكَلَامِ","kalam","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "Majrur by «fi».",
      "«فِي» ile mecrûr."),
  tok("مُطَابَقَتُهُ","mutabaqa","noun",["mubtada-khabar","masdar","form-iii-verbs","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ فَاعِلُ الْمَصْدَرِ مَعْنًى — مَصْدَرُ «طَابَقَ» عَلَى مُفَاعَلَةٍ، وَبِنَاءُ الْمُفَاعَلَةِ لِلْمُشَارَكَةِ.",
      "The khabar in raf' and a mudaf, the ha its mudaf ilayh and the masdar's fa'il in meaning — the Form III masdar of طَابَقَ on مُفَاعَلَة. Form III is the pattern of two parties meeting, and the choice is deliberate: the utterance and the situation are made to FIT one another, not one imposed on the other.",
      "Merfû haber ve muzâf; hâ muzâfun ileyhtir ve mânen masdarın fâilidir — «طَابَقَ»nin MÜFÂALE vezninde masdarı. Müfâale, iki tarafın buluşma kalıbıdır ve seçim kasıtlıdır: kelâm ile hâl birbirine UYDURULUR; biri ötekine dayatılmaz."),
  tok("لِمُقْتَضَى","muqtada","noun",["huruf-jarr","ism-maful","ism-maqsur-manqus","form-viii-verbs","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«مُطَابَقَتُهُ»، وَ«مُقْتَضَى» مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ وَهُوَ مُضَافٌ — اسْمُ مَفْعُولٍ مِنْ «اِقْتَضَى».",
      "A jarr-majrur attaching to «its conforming», and «what is called for» is majrur by a kasra ESTIMATED on the alif, which cannot bear one, and is itself a mudaf. It is the ism maf'ul of اِقْتَضَى — a maqsur noun, so all three cases are estimated on it and the word looks identical in every one.",
      "«مُطَابَقَتُهُ»a taalluk eden câr-mecrûr; «مُقْتَضَى», taşıyamadığı için elif üzerinde MUKADDER kesra ile mecrûr ve kendisi de muzâftır — «اِقْتَضَى»nin ism-i mef'ûlü. Maksûr bir isimdir; üç hâlin üçü de üzerinde mukadderdir ve kelime hepsinde aynı görünür.",
      segments=[seg("لِ","li","prep"), seg("مُقْتَضَى","muqtada","noun")]),
  tok("الْحَالِ","hal","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَ«مُقْتَضَى الْحَالِ» هُوَ الِاصْطِلَاحُ الَّذِي يَدُورُ عَلَيْهِ الْفَنُّ كُلُّهُ.",
      "The mudaf ilayh in jarr — and «what the situation calls for» is the technical term the entire discipline turns on. Every chapter of ʿilm al-maʿani after this one is an account of some situation and of what it calls for.",
      "Mecrûr muzâfun ileyh — ve «muktezâ-yı hâl», bütün fennin üzerinde döndüğü ıstılahtır. Bundan sonraki her bâb, bir hâlin ve o hâlin gerektirdiğinin beyânıdır."),
  tok("مَعَ","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«مُطَابَقَتُهُ».",
      "A zarf in nasb and a mudaf, attaching to «its conforming» — the same hinge word that held the definition of an utterance's fasaha together, doing the same work one level up: balagha is not instead of fasaha but on top of it.",
      "Zarfiyyet üzere mansub zarf ve muzâf; «مُطَابَقَتُهُ»a taalluk eder — kelâmın fesâhati tarifini bir arada tutan menteşe kelimenin aynısı; bir kat yukarıda aynı işi görür: belâgat, fesâhatin yerine değil üstüne gelir."),
  tok("فَصَاحَتِهِ","fasaha","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ عَائِدَةٌ عَلَى «الْكَلَامِ» — وَهِيَ مُذَكَّرَةٌ هُنَا وَمُؤَنَّثَةٌ فِي الْبَابِ الْأَوَّلِ، لِاخْتِلَافِ الْمَرْجِعِ.",
      "The mudaf ilayh in jarr and itself a mudaf, the ha going back to «the utterance» — MASCULINE here, where chapter 1's identical phrase had a feminine ha going back to «the words». Same three letters, different antecedent, and the gender is the only thing that says so.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf; hâ «الْكَلَام»a râcidir — burada MÜZEKKER, birinci bâbdaki aynı ibarede ise «الْكَلِمَات»a râci müennes. Aynı üç harf, farklı merci; ve bunu söyleyen tek şey cinsiyettir.",
      segments=[seg("فَصَاحَتِ","fasaha","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("وَالْبَلَاغَةُ فِي الْكَلَامِ مُطَابَقَتُهُ لِمُقْتَضَى الْحَالِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed nominal sentence, with no position in i'rab.",
   "İsti'nâfî isim cümlesi; i'râbdan mahalli yoktur.")]})

CH2.append({"id": "s2", "translation": {
 "en": "And in a speaker it is a settled faculty by which he is able to compose an utterance that has balagha.",
 "tr": "Mütekellimde ise; kendisiyle belîğ bir kelâm te'lîfine muktedir olduğu bir melekedir."},
 "tokens": [
  tok("وَفِي","fi","prep",["huruf-jarr","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ وَ«فِي» حَرْفُ جَرٍّ — وَحُذِفَ الْمُبْتَدَأُ لِدَلَالَةِ مَا قَبْلَهُ عَلَيْهِ.",
      "A joining waw and a jarr letter — and the mubtada «al-balagha» has been DROPPED, because the sentence before it has already said the word. An ellipsis is licensed exactly when what is left out is recoverable, and this is the cleanest kind: the missing word is four words behind.",
      "Atıf vâvı ve cer harfi — ve mübtedâ «الْبَلَاغَة» HAZFEDİLMİŞTİR; zira önceki cümle kelimeyi zaten söylemiştir. Hazif, ancak düşenin geri getirilebildiği yerde câizdir ve bu en temiz nevidir: eksik kelime dört kelime geridedir.",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","prep")]),
  tok("الْمُتَكَلِّمِ","mutakallim","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي» — وَهُوَ الثَّانِي مِنَ الِاثْنَيْنِ اللَّذَيْنِ تُوصَفُ بِهِمَا الْبَلَاغَةُ.",
      "Majrur by «fi» — the second of the two things balagha is predicated of. The single word was left out of this list deliberately: the Arabs were never heard to call one word baligh.",
      "«فِي» ile mecrûr — belâgatin vasıflandığı ikinin ikincisi. Müfred bu listeden kasten çıkarılmıştır: Arapların tek bir kelimeye «belîğ» dedikleri işitilmemiştir."),
  tok("مَلَكَةٌ","malaka-n","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ لِمُبْتَدَإٍ مَحْذُوفٍ — وَالْمَلَكَةُ صِفَةٌ رَاسِخَةٌ فِي النَّفْسِ، لَا فِعْلٌ يُفْعَلُ مَرَّةً.",
      "The khabar in raf' with its tanwin, for the dropped mubtada — and a MALAKA is a settled disposition of the soul, not an act performed once. The definition of the speaker is therefore not «one who has spoken well» but «one who can», and the difference is the whole reason the discipline is taught rather than admired.",
      "Hazfedilmiş mübtedânın tenvinli merfû haberi — ve MELEKE, nefiste yerleşmiş bir sıfattır; bir defa işlenen bir fiil değil. Öyleyse mütekellimin tarifi «güzel söylemiş olan» değil «söyleyebilen»dir; ve bu fark, bu ilmin hayranlıkla seyredilmek yerine öğretilmesinin bütün sebebidir."),
  tok("يَقْتَدِرُ","iqtadara","verb",["mudari-marfu","jumla-sifa","form-viii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«مَلَكَةٌ» لِأَنَّهَا نَكِرَةٌ.",
      "A mudari in raf' with a hidden «he» — and the clause stands in the POSITION OF RAF' as a na't of «a faculty», because what it describes is indefinite. A clause after an indefinite is its description; after a definite it would be a hal. That one rule decides dozens of readings.",
      "Merfû muzâri; fâili müstetir «هُوَ»dur — ve cümle, nekre olduğu için «مَلَكَةٌ»un na'tı olarak MAHALLEN MERFÛdur. Nekreden sonraki cümle sıfattır; marifeden sonra gelseydi hâl olurdu. Bu tek kâide, onlarca okuyuşu tayin eder."),
  tok("بِهَا","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَقْتَدِرُ»، وَالضَّمِيرُ عَائِدٌ عَلَى «مَلَكَةٌ» — وَهُوَ الرَّابِطُ بَيْنَ النَّعْتِ وَمَنْعُوتِهِ.",
      "A jarr-majrur attaching to «is able», the pronoun going back to «a faculty» — and that pronoun is the LINK between the description and what it describes. A clause standing as a na't must contain something returning to its noun, exactly as a sila must.",
      "«يَقْتَدِرُ»a taalluk eden câr-mecrûr; zamir «مَلَكَةٌ»a râcidir — ve o zamir, sıfat ile mevsûfu arasındaki RÂBITAdır. Sıfat olan bir cümle, tıpkı sıla gibi, mevsûfuna dönen bir şey taşımak zorundadır.",
      segments=[seg("بِ","bi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يَقْتَدِرُ» — وَ«اِقْتَدَرَ» يَتَعَدَّى بِعَلَى.",
      "A jarr letter attaching to «is able» — اِقْتَدَرَ reaches what it is able to do through an ʿala, and the paradigm's own preposition is part of knowing the verb.",
      "«يَقْتَدِرُ»a taalluk eden cer harfi — «اِقْتَدَرَ» muktedir olduğu şeye «عَلَى» ile ulaşır; fiilin kendi harf-i cerri, o fiili bilmenin bir parçasıdır."),
  tok("تَأْلِيفِ","talif","noun",["huruf-jarr","masdar","imal-al-masdar","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ، أُضِيفَ إِلَى مَفْعُولِهِ.",
      "Majrur by «ala» and a mudaf — a WORKING masdar, this time annexed to its OBJECT: what is composed is the utterance. The Manar's بَذْلُ الْفَقِيهِ was annexed to its doer; this is the other of the two shapes, and the app has now met both in real text.",
      "«عَلَى» ile mecrûr ve muzâf — AMEL EDEN bir masdar; bu defa MEF'ÛLÜNE izâfe edilmiştir: te'lîf edilen şey kelâmdır. Menâr'ın «بَذْلُ الْفَقِيهِ»i fâiline izâfe edilmişti; bu, iki şeklin ötekisidir ve uygulama artık ikisini de gerçek metinde görmüştür."),
  tok("كَلَامٍ","kalam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُنَوَّنٌ — وَتَنْكِيرُهُ مَقْصُودٌ: أَيَّ كَلَامٍ بَلِيغٍ كَانَ.",
      "The mudaf ilayh in jarr with its tanwin — and the indefiniteness is deliberate: ANY utterance that has balagha. A faculty is not a faculty if it works on one text only.",
      "Tenvinli mecrûr muzâfun ileyh — ve nekreliği kasıtlıdır: belîğ HERHANGİ bir kelâm. Yalnız tek bir metinde işleyen şey meleke değildir."),
  tok("بَلِيغٍ","balig","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«كَلَامٍ» مَجْرُورٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ مِنْ «بَلُغَ».",
      "A na't of «an utterance», in jarr — a sifa mushabbaha on فَعِيل from بَلُغَ. The pattern names a quality that HOLDS rather than an act that happened, which is the same point the word مَلَكَة made about the speaker three words earlier. The sentence says the same thing twice, once about the man and once about his speech.",
      "«كَلَامٍ»in na'tı, mecrûr — «بَلُغَ»den FA'ÎL vezninde sıfat-ı müşebbehe. Vezin, olup biten bir fiili değil DEVAM EDEN bir vasfı adlandırır — üç kelime önce «مَلَكَة»in mütekellim hakkında söylediğinin aynısı. Cümle aynı şeyi iki defa söyler: bir defa adam için, bir defa sözü için.",
      punct="."),
 ],
 "jumal": [J("يَقْتَدِرُ بِهَا عَلَى تَأْلِيفِ كَلَامٍ بَلِيغٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«مَلَكَةٌ».",
   "A verbal clause in the position of raf', a na't of «a faculty».",
   "«مَلَكَةٌ»un na'tı olarak mahallen merfû fiil cümlesi.")]})

CH2.append({"id": "s3", "translation": {
 "en": "And the science of maʿani is a science by which the states of Arabic wording are known — those states by which it conforms to what the situation calls for.",
 "tr": "İlm-i meânî; Arapça lafzın, muktezâ-yı hâle mutâbık olmasını sağlayan hâllerinin kendisiyle bilindiği ilimdir."},
 "tokens": [
  tok("وَعِلْمُ","ilm","noun",["mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«عِلْمُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "A resuming waw, and «the science of» is the mubtada in raf' and a mudaf.",
      "İsti'nâf vâvı; «عِلْمُ» merfû mübtedâ ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("عِلْمُ","ilm","noun")]),
  tok("الْمَعَانِي","maani","noun",["idafa-definiteness","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — مَنْقُوصٌ مُعَرَّفٌ، فَيَاؤُهُ ثَابِتَةٌ. وَهُوَ صِيغَةُ مُنْتَهَى الْجُمُوعِ، فَلَوْ نُكِّرَ لَمُنِعَ مِنَ الصَّرْفِ وَحُذِفَتْ يَاؤُهُ: «مَعَانٍ».",
      "The mudaf ilayh, majrur by a kasra ESTIMATED on the ya for heaviness — a manqus made definite, so its ya stands. And it is a sighat muntaha al-jumu', so had it been left indefinite it would have been barred from tanwin AND lost its ya: مَعَانٍ. Two facts about one word that pull in different directions, and the app's own ending engine is gated on exactly this row.",
      "Sıklet sebebiyle yâ üzerinde MUKADDER kesra ile mecrûr muzâfun ileyh — marife bir menkūstur, bu yüzden yâsı durur. Ve sîga-i müntehe'l-cumû'dur; nekre bırakılsaydı hem gayr-i munsarif olur hem yâsı düşerdi: «مَعَانٍ». Tek kelime hakkında birbirini çeken iki hakikat; ve uygulamanın son harf motoru tam da bu satırla imtihan edilir."),
  tok("عِلْمٌ","ilm","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَهَذَا الْقَالَبُ نَفْسُهُ افْتُتِحَ بِهِ «مُخْتَصَرُ الْمَنَارِ»: عِلْمٌ يُعْرَفُ بِهِ أَحْوَالُ الْأَدِلَّةِ.",
      "The khabar in raf' with its tanwin — and this is the SAME FRAME that opens Mukhtasar al-Manar: «a science by which the states of the evidences are known». Two disciplines, two centuries apart, defining themselves with one sentence shape: a science is named by what it lets you know about the states of something.",
      "Tenvinli merfû haber — ve bu, «Muhtasaru'l-Menâr»ı açan kalıbın TA KENDİSİdir: «عِلْمٌ يُعْرَفُ بِهِ أَحْوَالُ الْأَدِلَّةِ». İki ilim, iki asır arayla, kendilerini tek bir cümle kalıbıyla tarif eder: bir ilim, bir şeyin hâlleri hakkında bildirdiğiyle adlandırılır."),
  tok("يُعْرَفُ","arafa","verb",["naib-al-fail","jumla-sifa","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«عِلْمٌ» لِأَنَّهُ نَكِرَةٌ.",
      "A mudari built for the unnamed doer, in raf' — and the clause stands in the position of raf' as a na't of «a science», because that noun is indefinite. Identical in form and in office to the same verb in the Manar's opening line.",
      "Meçhûl sîgasında merfû muzâri — ve cümle, nekre olduğu için «عِلْمٌ»un na'tı olarak mahallen merfûdur. Menâr'ın açılış satırındaki aynı fiille hem şeklen hem vazifeten aynıdır."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُعْرَفُ»، وَالضَّمِيرُ عَائِدٌ عَلَى «عِلْمٌ» وَهُوَ الرَّابِطُ.",
      "A jarr-majrur attaching to «are known», the pronoun going back to «a science» and serving as the link between the na't and its noun.",
      "«يُعْرَفُ»a taalluk eden câr-mecrûr; zamir «عِلْمٌ»a râcidir ve sıfat ile mevsûfu arasındaki râbıtadır.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("أَحْوَالُ","hal","noun",["naib-al-fail","idafa-definiteness"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ «حَالٍ».",
      "The naib al-fa'il in raf' and a mudaf — the plural of حَال. What is known is not the wording but its STATES, and that is why the discipline is not lexicography.",
      "Merfû nâib-i fâil ve muzâf — «حَال»in cemi. Bilinen şey lafzın kendisi değil HÂLLERİdir; bu ilmin lügat ilmi olmamasının sebebi budur."),
  tok("اللَّفْظِ","lafz","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyh."),
  tok("الْعَرَبِيِّ","arabi","noun",["naat-sifa"],
      "نَعْتٌ لِـ«اللَّفْظِ» مَجْرُورٌ — اسْمٌ مَنْسُوبٌ، وَالْقَيْدُ مَقْصُودٌ: هَذَا الْفَنُّ مَبْنِيٌّ عَلَى خَصَائِصِ الْعَرَبِيَّةِ نَفْسِهَا.",
      "A na't of «the wording», in jarr — a nisba noun, and the restriction is deliberate: this discipline is built on the properties of Arabic itself. Its rules are not claimed for language in general, and a book that says so in its own definition is being careful rather than narrow.",
      "«اللَّفْظ»in na'tı, mecrûr — nisbet ismi; ve kayıt kasıtlıdır: bu fen, bizzat Arapçanın hususiyetleri üzerine kurulmuştur. Kâideleri umûmen dil için iddia edilmez; bunu kendi tarifinde söyleyen bir kitap, dar değil dikkatlidir."),
  tok("الَّتِي","allati","pron",["ism-mawsul","naat-sifa"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«أَحْوَالُ» — وَجَمْعُ غَيْرِ الْعَاقِلِ يُوصَفُ بِمَا يُوصَفُ بِهِ الْمُفْرَدَةُ الْمُؤَنَّثَةُ.",
      "A relative noun, fixed in form, in the position of RAF' as a na't of «the states» — and a plural of what does not reason is described exactly as a feminine singular is, which is why الَّتِي and not اللَّاتِي. The same rule that made chapter 1's ها feminine.",
      "Mebnî ism-i mevsûl; «أَحْوَال»in na'tı olarak MAHALLEN MERFÛdur — ve âkil olmayanın cemi, müfred müennes gibi vasıflanır; «اللَّاتِي» değil «الَّتِي» olmasının sebebi budur. Birinci bâbdaki «هَا»yı müennes yapan kâidenin aynısı."),
  tok("بِهَا","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُطَابِقُ» وَقَدْ قُدِّمَ عَلَيْهِ، وَالضَّمِيرُ عَائِدٌ عَلَى «الَّتِي» وَهُوَ الْعَائِدُ.",
      "A jarr-majrur attaching to «conforms» and PUT BEFORE it, the pronoun going back to «which» — and that pronoun is the sila's ʿaid. Written out at last: here the returning pronoun is on the page, where the Manar's was hidden inside a verb and dropped after another.",
      "«يُطَابِقُ»a taalluk eden ve onun ÖNÜNE geçmiş câr-mecrûr; zamir «الَّتِي»ye râcidir ve sılanın ÂİDİdir. Nihayet yazılı: burada dönen zamir sayfadadır; Menâr'da biri fiilin içinde gizliydi, öteki bir fiilden sonra düşmüştü.",
      segments=[seg("بِ","bi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("يُطَابِقُ","tabaqa","verb",["mudari-marfu","jumla-sifa","form-iii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» يَعُودُ عَلَى «اللَّفْظِ» — وَالْجُمْلَةُ صِلَةُ «الَّتِي» لَا مَحَلَّ لَهَا.",
      "A mudari in raf' with a hidden «he» going back to «the wording» — and the clause is the sila of «which», with no position in i'rab. Note the two pronouns: the hidden one is the wording, the written one is the states. Losing either loses the sentence.",
      "Merfû muzâri; fâili, «اللَّفْظ»a râci müstetir «هُوَ»dur — ve cümle «الَّتِي»nin sılasıdır, mahalli yoktur. İki zamire dikkat: gizli olan lafız, yazılı olan hâllerdir. Birini kaybetmek cümleyi kaybetmektir."),
  tok("مُقْتَضَى","muqtada","noun",["maful-bihi","ism-maqsur-manqus","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ وَهُوَ مُضَافٌ — وَهُوَ نَفْسُ الْكَلِمَةِ الَّتِي جَاءَتْ مَجْرُورَةً فِي أَوَّلِ الْبَابِ.",
      "The maf'ul bihi, in nasb by a fatha ESTIMATED on the alif, and a mudaf — and it is the very word that stood MAJRUR at the head of this chapter. A maqsur noun looks the same in all three cases, so the reader has now seen one word take two different cases without changing a letter. There is no better demonstration that i'rab is a fact about position and not about spelling.",
      "Taazzür sebebiyle elif üzerinde MUKADDER fetha ile mansub mef'ûlün bih ve muzâf — ve bu bâbın başında MECRÛR olarak gelen kelimenin ta kendisidir. Maksûr isim üç hâlde de aynı görünür; öyleyse okuyucu artık tek bir kelimenin, tek harf değiştirmeden iki ayrı hâl aldığını görmüştür. İ'râbın imlâya değil mevkiye dair bir hakikat olduğunun bundan iyi bir ispatı yoktur."),
  tok("الْحَالِ","hal","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ تَمَّ حَدُّ الْفَنِّ.",
      "The mudaf ilayh in jarr — and with it the definition of the discipline is complete.",
      "Mecrûr muzâfun ileyh — ve onunla fennin haddi tamamlanır.",
      punct="."),
 ],
 "jumal": [J("يُعْرَفُ بِهِ أَحْوَالُ اللَّفْظِ الْعَرَبِيِّ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«عِلْمٌ».",
   "A verbal clause in the position of raf', a na't of «a science».",
   "«عِلْمٌ»un na'tı olarak mahallen merfû fiil cümlesi."),
  J("بِهَا يُطَابِقُ مُقْتَضَى الْحَالِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

CH2.append({"id": "s4", "translation": {
 "en": "And a report is what admits, in itself, of being true and of being false.",
 "tr": "Haber; zâtı itibarıyla doğruluğa ve yalanlığa ihtimâli olan sözdür."},
 "tokens": [
  tok("وَالْخَبَرُ","khabar","noun",["mubtada-khabar","khabar-insha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْخَبَرُ» مُبْتَدَأٌ مَرْفُوعٌ — وَهَذَا مُصْطَلَحُ الْبَلَاغَةِ لَا مُصْطَلَحُ النَّحْوِ: هُنَاكَ خَبَرٌ مُقَابِلُ الْمُبْتَدَإِ، وَهُنَا خَبَرٌ مُقَابِلُ الْإِنْشَاءِ.",
      "A resuming waw, and «the report» is the mubtada in raf' — and this is the BALAGHA sense of the word, not the nahw sense. In nahw a khabar is what a mubtada takes; here it is what an insha is not. One Arabic word, two disciplines, two definitions, and a reader who has done nahw first must put the old one down.",
      "İsti'nâf vâvı; «الْخَبَر» merfû mübtedâdır — ve bu kelimenin BELÂGATtaki mânâsıdır, nahivdeki değil. Nahivde haber, mübtedânın aldığı şeydir; burada ise inşânın olmadığı şeydir. Tek Arapça kelime, iki ilim, iki tarif; ve önce nahiv okumuş olan, eskisini bir kenara bırakmak zorundadır.",
      segments=[seg("وَ","wa","conj"), seg("الْخَبَرُ","khabar","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَهُوَ قَالَبُ الْحُدُودِ نَفْسُهُ: مُبْتَدَأٌ مَعْرِفَةٌ ثُمَّ «مَا» ثُمَّ فِعْلٌ.",
      "A relative noun, fixed on sukun, in the position of raf' as the khabar — and this is the definitional frame the whole library is written in: a definite mubtada, then «ma», then a verb. The Manar used it sixteen chapters running; here is another book, another century, another discipline, using it identically.",
      "Sükûn üzere mebnî ism-i mevsûl; haber olarak mahallen MERFÛdur — ve bu, bütün kütüphanenin yazıldığı tarif kalıbıdır: marife mübtedâ, sonra «مَا», sonra fiil. Menâr onu on altı bâb boyunca kullandı; işte başka bir kitap, başka bir asır, başka bir ilim — aynı kalıbı kullanıyor."),
  tok("احْتَمَلَ","ihtamala","verb",["fail","jumla-sifa","form-viii-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» عَائِدٌ عَلَى «مَا» — عَلَى اِفْتَعَلَ مِنْ «ح م ل»، وَبِنَاءُ الِافْتِعَالِ هُنَا لِلْمُطَاوَعَةِ.",
      "A mazi on the fatha with a hidden «he» returning to the «ma» — on اِفْتَعَلَ from ح م ل, and Form VIII here carries the sense of ADMITTING: not that the report bears truth, but that it will take either. The pattern is doing the definitional work.",
      "Fetha üzere mebnî mâzî; fâili, «مَا»ya râci müstetir «هُوَ»dur — «ح م ل»den İFTİÂL vezninde; ve iftiâl burada MUTÂVAAT mânâsı taşır: haberin doğruyu taşıması değil, ikisinden birini KABUL ETMESİ. Tarifi yapan şey vezindir."),
  tok("الصِّدْقَ","sidq","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.",
      "The maf'ul bihi in nasb by the fatha.",
      "Fetha ile mansub mef'ûlün bih."),
  tok("وَالْكَذِبَ","kadhib","noun",["atf-nasaq","maful-bihi"],
      "مَعْطُوفٌ مَنْصُوبٌ — وَالْعَطْفُ بِالْوَاوِ هُنَا لِلْجَمْعِ لَا لِلتَّخْيِيرِ: الْخَبَرُ يَحْتَمِلُهُمَا مَعًا، ثُمَّ يَقَعُ أَحَدُهُمَا.",
      "Joined, in nasb — and the waw here gathers rather than offers a choice: a report admits BOTH at once as possibilities, and then one of them turns out to be the case. Had the matn written أَوْ it would have said something else and something false.",
      "Ma'tûf, mansub — ve buradaki vâv tahyîr için değil CEM' içindir: haber, ihtimâl olarak ikisini BİRDEN taşır; sonra biri vâki olur. Metin «أَوْ» yazsaydı başka ve yanlış bir şey söylemiş olurdu.",
      segments=[seg("وَ","wa","conj"), seg("الْكَذِبَ","kadhib","noun")]),
  tok("لِذَاتِهِ","dhat","noun",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«احْتَمَلَ»، وَ«ذَاتِ» مُضَافٌ — وَهَذَا الْقَيْدُ هُوَ الْحَدُّ كُلُّهُ: خَبَرُ اللهِ وَخَبَرُ رَسُولِهِ لَا يَحْتَمِلَانِ الْكَذِبَ لِخَارِجٍ، وَيَحْتَمِلَانِهِ لِذَاتِ الصِّيغَةِ، فَيَدْخُلَانِ فِي الْحَدِّ.",
      "A jarr-majrur attaching to «admits», with «itself» a mudaf — and THIS restriction is the whole definition. God's report and His Messenger's cannot be false, but that is a fact about them from OUTSIDE, not about the form of the sentence; considered in itself the form admits both, so they fall inside the definition. Drop these two words and the definition excludes revelation, which is the one thing a book of balagha cannot afford.",
      "«احْتَمَلَ»a taalluk eden câr-mecrûr; «ذَاتِ» muzâftır — ve tarifin tamamı BU kayıttadır. Allah'ın ve Resûlü'nün haberi yalan ihtimâli taşımaz; fakat bu, sîganın kendisine değil DIŞARIDAN bir sebebe dair bir hakikattir; zâtı itibarıyla sîga ikisini de taşır ve bu yüzden tarife dâhil olurlar. Bu iki kelimeyi düşürün, tarif vahyi dışarıda bırakır — ki bir belâgat kitabının göze alamayacağı tek şey budur.",
      segments=[seg("لِ","li","prep"), seg("ذَاتِ","dhat","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("احْتَمَلَ الصِّدْقَ وَالْكَذِبَ لِذَاتِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

CH2.append({"id": "s5", "translation": {
 "en": "And an insha is what does not admit the two of them.",
 "tr": "İnşâ ise, o ikisini taşımayandır."},
 "tokens": [
  tok("وَالْإِنْشَاءُ","insha","noun",["mubtada-khabar","khabar-insha","masdar","form-iv-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْإِنْشَاءُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «أَنْشَأَ» عَلَى إِفْعَالٍ، أَيِ الْإِيجَادُ: الْإِنْشَاءُ يُوجِدُ مَعْنَاهُ بِالتَّلَفُّظِ بِهِ وَلَا يُخْبِرُ عَنْ شَيْءٍ سَابِقٍ.",
      "A joining waw, and «insha» is the mubtada in raf' — the Form IV masdar of أَنْشَأَ, «to bring into being». That is the whole doctrine in the word: an insha BRINGS ABOUT its meaning by being uttered, where a report tells of something that was already there. «Stand up» makes a command exist; «he stood up» does not make a standing exist.",
      "Atıf vâvı; «الْإِنْشَاء» merfû mübtedâdır — «أَنْشَأَ»nın İF'ÂL vezninde masdarı: îcâd etmek. Doktrinin tamamı kelimenin içindedir: inşâ, mânâsını söylenmekle VAR EDER; haber ise zaten var olandan haber verir. «Kalk» bir emri var eder; «kalktı» bir kalkmayı var etmez.",
      segments=[seg("وَ","wa","conj"), seg("الْإِنْشَاءُ","insha","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَالْقَالَبُ نَفْسُهُ لِلْمَرَّةِ الثَّانِيَةِ فِي جُمْلَتَيْنِ مُتَتَابِعَتَيْنِ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar — the same frame for the second time in two consecutive sentences. A pair of terms defined in one shape is a pair the matn wants read against each other.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur — iki ardışık cümlede ikinci defa aynı kalıp. Tek kalıpta tarif edilen bir çift, metnin birbirine karşı okunmasını istediği bir çifttir."),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا، وَالْجُمْلَةُ بَعْدَهَا صِلَةُ الْمَوْصُولِ.",
      "A bare negation, and the clause after it is the sila of the relative. The whole definition of the second term is the first term with one letter of negation in front of it — which is what a genuine dichotomy looks like.",
      "Amel etmeyen nefiy; sonrasındaki cümle ism-i mevsûlün sılasıdır. İkinci terimin bütün tarifi, birincinin önüne tek bir nefiy harfi konmuş hâlidir — hakiki bir ikili taksîm böyle görünür."),
  tok("يَحْتَمِلُهُمَا","ihtamala","verb",["mudari-marfu","maful-bihi","al-muthanna","form-viii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ»، وَ«هُمَا» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالتَّثْنِيَةُ عَائِدَةٌ عَلَى الصِّدْقِ وَالْكَذِبِ فِي الْجُمْلَةِ قَبْلَهَا.",
      "A mudari in raf' with a hidden «he» for its fa'il, and «huma» is an attached pronoun in the position of NASB as its maf'ul bihi — a DUAL, reaching back to «truth and falsehood» in the sentence before. Two nouns became one word of two letters, and the sentence cannot be read at all without the one before it. That is not economy; it is the matn stating that these two terms are one division.",
      "Merfû muzâri; fâili müstetir «هُوَ»dur ve «هُمَا», mef'ûlün bih olarak MAHALLEN MANSUB muttasıl zamirdir — bir önceki cümledeki «doğruluk ve yalanlığa» dönen bir TESNİYE. İki isim, iki harflik tek kelimeye dönüşmüştür ve cümle, kendisinden önceki olmadan hiç okunamaz. Bu bir tasarruf değildir; metnin, bu iki terimin tek bir taksîm olduğunu söyleyişidir.",
      segments=[seg("يَحْتَمِلُ","ihtamala","verb"), seg("هُمَا","pron-3d","pron")], punct="."),
 ],
 "jumal": [J("لَا يَحْتَمِلُهُمَا",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS = {
 "wa":  g("وَ", None, "conj", "and", "ve", 0),
 "fa":  g("فَ", None, "conj", "so, then; and so", "böylece; -ınca", 1),
 "fi":  g("فِي", None, "prep", "in", "-de, içinde", 0),
 "min": g("مِنْ", None, "prep", "from, of", "-den", 0),
 "ala": g("عَلَى", None, "prep", "upon, over", "üzerine", 0),
 "bi":  g("بِ", None, "prep", "by, with", "ile", 0),
 "li":  g("لِ", None, "prep", "for, to", "için, -e", 0),
 "maa": g("مَعَ", None, "noun", "with, together with", "ile; beraber", 1),
 "la-nafiya": g("لَا (النَّافِيَة)", None, "part", "not (bare negation)", "değil, -mez (nefiy)", 1),
 "an-nasiba": g("أَنْ", None, "part", "that (masdar-maker; puts the mudari in nasb)", "-mesi (masdariyye; muzâriyi nasbeder)", 3),
 "imma": g("إِمَّا", None, "part", "either … or (a letter of detailing; it never comes alone)", "ya … ya (tafsîl harfi; asla yalnız gelmez)", 4),
 "ma-mawsula": g("مَا (المَوْصُولَة)", None, "pron", "that which, what", "o şey ki", 2),
 "allati": g("الَّتِي", None, "pron", "which, that (fem. relative)", "ki o (müennes ism-i mevsûl)", 1),
 "pron-3ms": g("ـهُ", None, "pron", "his, him, it (masc.)", "onun, onu (müzekker)", 0),
 "pron-3fs": g("ـهَا", None, "pron", "her, it (fem.)", "onun, onu (müennes)", 0),
 "pron-3d":  g("ـهُمَا", None, "pron", "the two of them", "o ikisini", 2),
 # ---- the discipline's own vocabulary
 "fasaha":  g("فَصَاحَة", "ف ص ح", "noun", "fasaha — clearness of wording (masdar)", "fesâhat — lafzın açıklığı (masdar)", 4),
 "balagha-n": g("بَلَاغَة", "ب ل غ", "noun", "balagha — speech reaching its mark (masdar)", "belâgat — sözün maksada ulaşması (masdar)", 4),
 "balig":   g("بَلِيغ", "ب ل غ", "noun", "having balagha (sifa mushabbaha)", "belîğ (sıfat-ı müşebbehe)", 4),
 "mufrad":  g("مُفْرَد", "ف ر د", "noun", "a single word, taken alone", "müfred; tek kelime", 3),
 "kalam":   g("كَلَام", "ك ل م", "noun", "speech, an utterance that conveys a full sense", "kelâm; tam mânâ ifade eden söz", 2),
 "kalima":  g("كَلِمَة", "ك ل م", "noun", "a word", "kelime", 1, plural="كَلِمَات"),
 "mutakallim": g("مُتَكَلِّم", "ك ل م", "noun", "the speaker (ism fa'il, Form V)", "mütekellim; konuşan (ism-i fâil, tefe''ul)", 3),
 "khulus":  g("خُلُوص", "خ ل ص", "noun", "being free of a thing (masdar)", "hulûs; bir şeyden hâlî olma (masdar)", 4),
 "tanafur": g("تَنَافُر", "ن ف ر", "noun", "mutual harshness — parts shying away from one another (masdar, Form VI)", "tenâfür — parçaların birbirinden ürkmesi (masdar, tefâul)", 5),
 "harf":    g("حَرْف", "ح ر ف", "noun", "a letter", "harf", 1, plural="حُرُوف"),
 "gharaba": g("غَرَابَة", "غ ر ب", "noun", "strangeness — a word too far out of use to be understood", "garâbet — anlaşılmayacak kadar kullanımdan uzak olma", 5),
 "mukhalafa": g("مُخَالَفَة", "خ ل ف", "noun", "departure from, going against (masdar, Form III)", "muhâlefet (masdar, müfâale)", 4),
 "qiyas":   g("قِيَاس", "ق ي س", "noun", "the rule, the regular pattern (here: of sarf)", "kıyâs; kâide (burada: sarf kâidesi)", 3),
 "daf":     g("ضَعْف", "ض ع ف", "noun", "weakness", "za'f, zayıflık", 3),
 "talif":   g("تَأْلِيف", "أ ل ف", "noun", "composition, the putting of words together (masdar, Form II)", "te'lîf; kelimeleri birleştirme (masdar, tef'îl)", 4),
 "taqid":   g("تَعْقِيد", "ع ق د", "noun", "obscurity — lit. knotting (masdar, Form II)", "ta'kîd — lügatte düğümleme (masdar, tef'îl)", 5),
 "khalal":  g("خَلَل", "خ ل ل", "noun", "a flaw, a gap", "halel; bozukluk, aralık", 4),
 "nazm":    g("نَظْم", "ن ظ م", "noun", "the ordering of words", "nazım; lafızların tertîbi", 3),
 "intiqal": g("اِنْتِقَال", "ن ق ل", "noun", "passage, the mind's move from one sense to another (masdar, Form VIII)", "intikāl; zihnin bir mânâdan ötekine geçişi (masdar, iftiâl)", 4),
 "darb":    g("ضَرْب", "ض ر ب", "noun", "a kind, a sort", "nevi, kısım", 2),
 "lafzi":   g("لَفْظِيّ", "ل ف ظ", "noun", "of the wording (nisba)", "lafzî (nisbet)", 4),
 "manawi":  g("مَعْنَوِيّ", "ع ن ي", "noun", "of the sense (nisba)", "ma'nevî (nisbet)", 4),
 "lafz":    g("لَفْظ", "ل ف ظ", "noun", "the wording, the uttered form", "lafız; söylenen şekil", 2),
 "arabi":   g("عَرَبِيّ", "ع ر ب", "noun", "Arabic (nisba)", "Arabî, Arapça (nisbet)", 2),
 "dalala":  g("دَلَالَة", "د ل ل", "noun", "pointing, indication (masdar)", "delâlet; gösterme (masdar)", 3),
 "murad":   g("مُرَاد", "ر و د", "noun", "what is meant (ism maf'ul, Form IV)", "murâd; kastedilen (ism-i mef'ûl, if'âl)", 3),
 "zahir":   g("ظَاهِر", "ظ ه ر", "noun", "clear, apparent (ism fa'il)", "zâhir; açık (ism-i fâil)", 2),
 "mutabaqa": g("مُطَابَقَة", "ط ب ق", "noun", "conforming, fitting one another (masdar, Form III)", "mutâbakat; birbirine uygun düşme (masdar, müfâale)", 5),
 "muqtada": g("مُقْتَضَى", "ق ض ي", "noun", "what a thing calls for (ism maf'ul, Form VIII; maqsur)", "mukteza; gerektirdiği şey (ism-i mef'ûl, iftiâl; maksûr)", 5),
 "hal":     g("حَال", "ح و ل", "noun", "state, situation", "hâl, durum", 2, plural="أَحْوَال"),
 "malaka-n": g("مَلَكَة", "م ل ك", "noun", "a settled faculty of the soul", "meleke; nefiste yerleşmiş kābiliyet", 5),
 "ilm":     g("عِلْم", "ع ل م", "noun", "knowledge; a science", "ilim; bilgi", 1),
 "maani":   g("مَعَانِي", "ع ن ي", "noun", "meanings (plural of مَعْنًى)", "meânî; mânâlar (ma'nânın cemi)", 3),
 "khabar":  g("خَبَر", "خ ب ر", "noun", "a report — speech that may be true or false", "haber — doğru yahut yalan olabilen söz", 2),
 "insha":   g("إِنْشَاء", "ن ش أ", "noun", "insha — speech that brings its meaning about (masdar, Form IV)", "inşâ — mânâsını var eden söz (masdar, if'âl)", 4),
 "sidq":    g("صِدْق", "ص د ق", "noun", "truth, being true", "sıdk, doğruluk", 2),
 "kadhib":  g("كَذِب", "ك ذ ب", "noun", "falsehood, being false", "kizb, yalanlık", 2),
 "dhat":    g("ذَات", "ذ و ت", "noun", "self, essence", "zât, kendisi", 3),
 # ---- verbs
 "wasafa":   g("وَصَفَ", "و ص ف", "verb", "to describe, to predicate of", "vasfetmek", 2, form="I"),
 "arafa":    g("عَرَفَ", "ع ر ف", "verb", "to know, to recognise", "bilmek, tanımak", 1, form="I"),
 "kana":     g("كَانَ", "ك و ن", "verb", "to be", "olmak", 1, form="I"),
 "ihtamala": g("اِحْتَمَلَ", "ح م ل", "verb", "to admit of, to bear (a possibility)", "ihtimâl taşımak", 4, form="VIII"),
 "tabaqa":   g("طَابَقَ", "ط ب ق", "verb", "to conform to, to match", "mutâbık olmak", 4, form="III"),
 "iqtadara": g("اِقْتَدَرَ", "ق د ر", "verb", "to be able, to have power over", "muktedir olmak", 4, form="VIII"),
}

def build_morph():
    out = {}
    # COPIED after a lemma-identity assert — a lex key is global, and two
    # spellings of one verb in two packages is the collision this project has
    # been bitten by before.
    for pkg, lex in [("aqaid-ahl-al-sunna", "wasafa"),
                     ("aqaid-ahl-al-sunna", "kana"),
                     ("mukhtasar-al-manar", "arafa"),
                     ("mukhtasar-al-manar", "ihtamala")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))
        assert g_["entries"][lex]["lemma"] == GLOSS[lex]["lemma"], lex
        out[lex] = m["verbs"][lex]
    # طَابَقَ — Form III sound. Its masdar is the matn's own word مُطَابَقَة.
    out["tabaqa"] = _sg.derived("بَابُ الْمُفَاعَلَةِ: فَاعَلَ يُفَاعِلُ", "فَاعَلَ يُفَاعِلُ", "ُ",
                                "طَابَق", "طَابِق", "طَابِق", "مُطَابَقَة", "مُطَابِق",
                                maful="مُطَابَق",
                                note="بِنَاءُ الْمُفَاعَلَةِ لِلْمُشَارَكَةِ: طَابَقَ الْكَلَامُ الْحَالَ وَطَابَقَهُ الْحَالُ.")
    # اِقْتَدَرَ — Form VIII sound. The ta of iftial is NOT changed: the qaf is not
    # one of the letters that colour it.
    out["iqtadara"] = _sg.derived("بَابُ الِافْتِعَالِ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ",
                                  "اِقْتَدَر", "قْتَدِر", "اِقْتَدِر", "اِقْتِدَار", "مُقْتَدِر",
                                  note="لَمْ تُبْدَلْ تَاءُ الِافْتِعَالِ لِأَنَّ الْقَافَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ.")
    return out

MANIFEST = {
 "id": "talkhis-al-miftah",
 "title": {"ar": "تَلْخِيصُ الْمِفْتَاح: عِلْمُ الْمَعَانِي — الْفَصَاحَةُ وَالْبَلَاغَة",
           "en": "Talkhis al-Miftah: The Science of Maʿani — Fasaha and Balagha",
           "tr": "Telhîsu'l-Miftâh: İlm-i Meânî — Fesâhat ve Belâgat"},
 "subtitle": {"en": "Al-Qazwini's definitions of clear speech, of eloquence, and of the science that studies them.",
              "tr": "Kazvînî'nin fesâhat, belâgat ve bunları inceleyen ilmin tarifleri."},
 "level": 6,
 "levelName": "Master",
 "access": "premium",
 "published": "2026-08-12",
 "chapters": [
   {"n": 1, "title": {"ar": "الْفَصَاحَة", "en": "Fasaha", "tr": "Fesâhat"}},
   {"n": 2, "title": {"ar": "الْبَلَاغَةُ وَعِلْمُ الْمَعَانِي", "en": "Balagha and the Science of Maʿani",
                      "tr": "Belâgat ve İlm-i Meânî"}},
 ],
 "attribution": {
  "en": ("The matn of Talkhis al-Miftah by Jalal al-Din al-Qazwini (d. 739/1338), the opening of "
         "Fann 1, ʿilm al-maʿani. SOURCE: research/sources/talkhis-al-miftah-balagha.txt, an "
         "Ottoman-Turkish commentary that quotes its matn in vowelled Arabic. Chapter 1 sentences "
         "2, 3 and 4 are VERBATIM from that file's own Arabic. Chapter 1 sentences 1 and 5, and all "
         "of chapter 2, are the RECEIVED matn of the Talkhis, restored where the supplied page "
         "carries only the Ottoman rendering; every one of them is a sentence the balagha tradition "
         "quotes in this wording. NOTHING in this package is an original composition. Vowelling is "
         "editorial where the source left a word bare. Awaiting scholarly review."),
  "tr": ("Celâleddîn el-Kazvînî'nin (ö. 739/1338) Telhîsu'l-Miftâh matni; 1. Fen olan ilm-i meânînin "
         "başlangıcı. KAYNAK: research/sources/talkhis-al-miftah-balagha.txt — matni harekeli Arapça "
         "olarak aktaran Osmanlıca bir şerh. Birinci bâbın 2, 3 ve 4. cümleleri o dosyanın kendi "
         "Arapçasından AYNEN alınmıştır. Birinci bâbın 1 ve 5. cümleleri ile ikinci bâbın tamamı, "
         "verilen sayfanın yalnız Osmanlıca tercümesini taşıdığı yerlerde Telhîs'in MERVÎ matnından "
         "getirilmiştir; her biri, belâgat geleneğinin bu lafızla naklettiği cümlelerdir. Bu pakette "
         "HİÇBİR telif cümle yoktur. Kaynağın harekesiz bıraktığı yerlerde hareke editöryeldir. "
         "İlmî tashih beklemektedir."),
  "ar": ("مَتْنُ تَلْخِيصِ الْمِفْتَاحِ لِلْخَطِيبِ الْقَزْوِينِيِّ — أَوَّلُ الْفَنِّ الْأَوَّلِ، عِلْمِ الْمَعَانِي. "
         "لَيْسَ فِي هَذِهِ الْحُزْمَةِ جُمْلَةٌ مُؤَلَّفَةٌ، وَإِنَّمَا هُوَ الْمَتْنُ الْمَرْوِيُّ."),
  "reviewStatus": "pending-scholarly-review",
 },
}

PKG.mkdir(parents=True, exist_ok=True)
(PKG / "chapters").mkdir(exist_ok=True)
(PKG / "chapters/1.json").write_text(
    json.dumps({"chapter": 1, "sentences": CH1}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "chapters/2.json").write_text(
    json.dumps({"chapter": 2, "sentences": CH2}, ensure_ascii=False, indent=1), encoding="utf-8")
MANIFEST["version"] = "0.2.0"
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(
    json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(
    json.dumps({"verbs": build_morph()}, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis:", len(CH1) + len(CH2), "sentences,",
      sum(len(x["tokens"]) for x in CH1 + CH2), "tokens; gloss", len(GLOSS))
