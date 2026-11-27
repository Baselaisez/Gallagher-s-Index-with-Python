# -*- coding: utf-8 -*-
"""Author chapter 8 of mukhtasar-al-manar — the COMMAND and the PROHIBITION.

Chapter 7 asked how a ruling is got out of a text. This chapter takes the two
forms that carry most of the rulings there are, defines each in the same frame,
and says what each OBLIGES when nothing qualifies it.

ATTRIBUTION: like chapters 2–7, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach — and almost all of it is a rule an
earlier chapter set up, coming back on a new word:
  • مُوجِبُهُ — the ism fa'il of أَوْجَبَ, the very verb chapter 4 used in أَنْ
    يُوجِبَ. The waw after a damma is a madd and writes no sukun: مُوجِب.
  • الِاسْتِعْلَاء and الْإِبَاحَة — a mamdud whose hamza came from a waw (ع ل و),
    so it keeps its tanwin, and a Form IV masdar of an ajwaf compensating with
    a ta marbuta. Chapters 6 and 7 respectively, on new words.
  • يَرِدُ — a MITHAL whose waw drops in the mudari, and it drops because a
    kasra follows: وَرَدَ يَرِدُ.
  • «افْعَلْ» and «لَا تَفْعَلْ» — the two sighas quoted as sighas, with the
    hamzat al-wasl on one and the jazm of la nahiya on the other.
  • مَا نَابَ عَنْهَا — a sila on an ajwaf, and the phrase that keeps the
    definition from collapsing into a single written shape.
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

TITLE8 = {"ar": "الْأَمْرُ وَالنَّهْي", "en": "The Command and the Prohibition",
          "tr": "Emir ve Nehiy"}

# The definition frame is deliberately identical for both, so its i'rab is
# written once and the two sentences differ only where the matn differs.
JIHA = ("جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُطْلَبُ»، وَ«جِهَةِ» مُضَافٌ — وَالِاسْتِعْلَاءُ أَنْ يَرَى الطَّالِبُ نَفْسَهُ فَوْقَ الْمَطْلُوبِ مِنْهُ.",
 "A jarr-majrur attaching to «is sought», and «the manner of» is a mudaf. ISTI'LA is that the one asking counts himself ABOVE the one asked — and it is the word that keeps a request and an entreaty out of the definition.",
 "«يُطْلَبُ»a taalluk eden câr-mecrûr; «جِهَةِ» muzâftır. İSTİ'LÂ, isteyenin kendini istenilenin ÜSTÜNDE görmesidir — ricâ ile duâyı tarifin dışında bırakan kelime budur.")

S.append({"id": "s1", "translation": {
 "en": "Then the command is an utterance by which the doing of a thing is sought, in the manner of one above.",
 "tr": "Emir, kendisiyle bir fiilin, üstünlük cihetiyle istendiği sözdür."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَبِهِ انْتَقَلَ مِنْ طُرُقِ الدَّلَالَةِ إِلَى صِيَغِ الطَّلَبِ نَفْسِهَا.",
      "A letter of atf giving sequence with an interval — with it the matn steps from the ROUTES a meaning travels to the two forms that carry most of the rulings there are.",
      "Terâhî ile tertîb için atıf harfi — metin onunla mânânın YOLLARINDAN, hükümlerin çoğunu taşıyan iki sîgaya geçer."),
  tok("الْأَمْرُ","amr","noun",["mubtada-khabar","masdar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «أَمَرَ»، وَالْمُرَادُ بِهِ هُنَا الصِّيغَةُ لَا الشَّأْنُ.",
      "The mubtada in raf' — the masdar of أَمَرَ, and what is meant here is the FORM, not the other أَمْر that means an affair or a matter. The same three letters carry both, and the plurals part them: أَوَامِر for this one, أُمُور for that.",
      "Merfû mübtedâ — «أَمَرَ»nin masdarı; burada kastedilen SÎGAdır, «iş, husus» mânâsındaki emir değil. Aynı üç harf ikisini de taşır; cemileri ayırır: bunun cemi أَوَامِر, ötekinin أُمُور."),
  tok("قَوْلٌ","qawl","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَجَاءَ نَكِرَةً لِأَنَّ الْمُرَادَ الْجِنْسُ.",
      "The khabar in raf' with its tanwin, and INDEFINITE because what is meant is the kind, not one particular utterance.",
      "Tenvînli merfû haber; nekredir, zira maksûd cinstir, muayyen bir söz değil."),
  tok("يُطْلَبُ","talaba","verb",["naib-al-fail","jumla-sifa","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«قَوْلٌ» — وَالْجُمْلَةُ بَعْدَ النَّكِرَةِ صِفَةٌ.",
      "A mudari built for the unnamed doer, in raf'; and the clause is in the position of raf' as a NA'T of «an utterance». A clause after an indefinite noun is a description of it — after a definite one it would be a hal. That single rule settles what this whole sentence is doing.",
      "Meçhûl sîgasında merfû muzâri; cümle «قَوْلٌ»un na'tı olarak mahallen merfûdur — nekreden sonraki cümle sıfattır. Marifeden sonra gelseydi hâl olurdu. Bu cümlenin ne iş gördüğünü belirleyen tek kaide budur."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُطْلَبُ»، وَالْهَاءُ عَائِدَةٌ عَلَى «قَوْلٌ» — وَهُوَ الرَّابِطُ بَيْنَ الصِّفَةِ وَمَوْصُوفِهَا.",
      "A jarr-majrur attaching to «is sought», its HA going back to «an utterance» — and that returning pronoun is what ties the description to the thing described. A na't clause without one is not a na't clause.",
      "«يُطْلَبُ»a taalluk eden câr-mecrûr; HÂ «قَوْلٌ»a râcidir — sıfatı mevsûfuna bağlayan âid zamîr odur. Âidsiz sıfat cümlesi olmaz.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("الْفِعْلُ","fil","noun",["naib-al-fail","masdar"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ — وَهُوَ الْمَطْلُوبُ: إِيقَاعُ الْفِعْلِ.",
      "The naib al-fa'il, in raf' — and it is the thing sought: that the act be done.",
      "Merfû nâib-i fâil — istenen şeydir: fiilin yapılması."),
  tok("عَلَى","ala","prep",["huruf-jarr","idafa-definiteness"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("جِهَةِ","jiha","noun",["huruf-jarr","idafa-definiteness"], *JIHA),
  tok("الِاسْتِعْلَاءِ","istila","noun",["idafa-definiteness","masdar","form-x-verbs","ism-mamdud"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «اِسْتَعْلَى» عَلَى اسْتِفْعَالٍ، وَهُوَ مَمْدُودٌ هَمْزَتُهُ مُنْقَلِبَةٌ عَنْ وَاوٍ («ع ل و») فَهُوَ مُنْصَرِفٌ.",
      "The mudaf ilayh in jarr — the masdar of اِسْتَعْلَى on اِسْتِفْعَال, and a MAMDUD whose hamza is the root's own waw (ع ل و) turned into one. So it is munsarif: put it in jarr while indefinite and it takes a kasra with a tanwin, exactly as خَفَاءً did, and not the bare fatha of صَحْرَاءَ.",
      "Mecrûr muzâfun ileyh — «اِسْتَعْلَى»nin İSTİF'ÂL vezninde masdarı; hemzesi kökün kendi vâvından («ع ل و») dönüşmüş MEMDÛDdur. Dolayısıyla munsariftir: nekre iken cerde tenvînli kesra alır — tıpkı «خَفَاءً» gibi, «صَحْرَاءَ»nin çıplak fethası gibi değil.",
      punct="."),
 ],
 "jumal": [J("الْأَمْرُ قَوْلٌ يُطْلَبُ بِهِ الْفِعْلُ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir."),
  J("يُطْلَبُ بِهِ الْفِعْلُ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«قَوْلٌ».",
   "A verbal clause in the position of raf', a na't of «an utterance».",
   "«قَوْلٌ»un na'tı olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s2", "translation": {
 "en": "And what it obliges is obligation, when it comes unqualified; and it may come for recommendation or for permission, with an indication.",
 "tr": "Mutlak geldiğinde îcâb ettiği şey vücûbdur; bir karîneyle nedb yahut ibâha için de gelebilir."},
 "tokens": [
  tok("وَمُوجِبُهُ","mujib","noun",["atf-nasaq","mubtada-khabar","ism-fail","form-iv-verbs","mithal-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«مُوجِبُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ مِنْ «أَوْجَبَ»، وَهُوَ مِثَالٌ وَاوِيٌّ: بَقِيَتِ الْوَاوُ مَدًّا بَعْدَ الضَّمَّةِ فَلَمْ تُكْتَبْ سَاكِنَةً.",
      "A joining waw; «what it obliges» is the mubtada in raf' and a mudaf — the ism fa'il of أَوْجَبَ, the very verb chapter 4 used in أَنْ يُوجِبَ. It is a MITHAL WAWI, and the waw sits after a damma, where it is already a madd letter and carries no sukun: مُوجِب, not *مُوْجِب. Same rule, same root, a different cell of the same paradigm.",
      "Atıf vâvı; «مُوجِبُ» merfû mübtedâ ve muzâftır — «أَوْجَبَ»nin ism-i fâili; dördüncü bâbdaki «أَنْ يُوجِبَ»nin fiilinin aynısı. MİSÂL-İ VÂVÎdir ve vâv dammeden sonradır: orada zaten med harfidir, sükûn taşımaz — مُوجِب, *مُوْجِب değil. Aynı kaide, aynı kök, aynı çekimin başka bir hânesi.",
      segments=[seg("وَ","wa","conj"), seg("مُوجِبُ","mujib","noun"), seg("هُ","pron-3ms","pron")]),
  tok("الْوُجُوبُ","wujub","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ «وَجَبَ» عَلَى فُعُول، وَبَيْنَهُ وَبَيْنَ «مُوجِب» فَرْقُ الْمُطَاوَعَةِ: هَذَا الْأَثَرُ، وَذَاكَ الْمُؤَثِّرُ.",
      "The khabar in raf' — the masdar of وَجَبَ on فُعُول. Set it beside مُوجِب and the pair is a lesson in itself: أَوْجَبَ is what the command DOES, وَجَبَ is what then HOLDS. The one is the cause, the other the effect, and Form IV is the whole difference between them.",
      "Merfû haber — «وَجَبَ»nin FUÛL vezninde masdarı. «مُوجِب» ile yan yana koy, çift kendi başına bir derstir: «أَوْجَبَ» emrin YAPTIĞI, «وَجَبَ» ise bunun üzerine SÂBİT OLANdır. Biri müessir, öteki eser; aradaki bütün fark İF'ÂL bâbıdır."),
  tok("عِنْدَ","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ.",
      "A time-adverb in nasb and a mudaf, hanging on an omitted word that stands as a hal.",
      "Mansub zaman zarfı ve muzâf; mahzûf bir hâle taalluk eder."),
  tok("الْإِطْلَاقِ","itlaq","noun",["idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «أَطْلَقَ» عَلَى إِفْعَالٍ: أَنْ يَرِدَ الْأَمْرُ عَارِيًا مِنْ كُلِّ قَرِينَةٍ.",
      "The mudaf ilayh in jarr — the masdar of أَطْلَقَ on إِفْعَال: that the command should come stripped of every indication. This is the hinge of the whole chapter — everything said here is said of the UNQUALIFIED case.",
      "Mecrûr muzâfun ileyh — «أَطْلَقَ»nin İF'ÂL vezninde masdarı: emrin her türlü karîneden soyulmuş olarak gelmesi. Bâbın menteşesi budur — burada söylenen her şey MUTLAK hâl için söylenmiştir.", punct="،"),
  tok("وَقَدْ","qad","part",["qad-harf","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«قَدْ» مَعَ الْمُضَارِعِ لِلتَّقْلِيلِ — لَا لِلتَّحْقِيقِ كَمَا مَعَ الْمَاضِي.",
      "A joining waw, and «qad» — before a MUDARI it means «sometimes», before a MADI it means «indeed». Same letter, opposite work, and the verb after it decides which.",
      "Atıf vâvı ve «قَدْ» — MUZÂRİden önce «bazen», MÂZÎden önce «muhakkak» demektir. Aynı harf, zıt iş; hangisi olduğuna sonraki fiil karar verir.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يَرِدُ","warada","verb",["mudari-marfu","mithal-verbs","qad-harf"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — مِثَالٌ وَاوِيٌّ: سَقَطَتْ وَاوُهُ لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ، «يَوْرِدُ» ← «يَرِدُ».",
      "A mudari in raf' by the damma — a MITHAL WAWI whose waw has dropped: يَوْرِدُ became يَرِدُ, because the waw stood between a ya and a KASRA. That kasra is the whole cause, which is why يَوْجَلُ, with a fatha after it, keeps its waw.",
      "Damme ile merfû muzâri — vâvı düşmüş MİSÂL-İ VÂVÎ: «يَوْرِدُ» iken «يَرِدُ» olmuştur; zira vâv, yâ ile KESRA arasında kalmıştır. Bütün sebep o kesradır; nitekim ardından fetha gelen «يَوْجَلُ» vâvını korur."),
  tok("لِلنَّدْبِ","nadb","noun",["huruf-jarr","lam-taleel","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَرِدُ»، وَاللَّامُ لِلتَّعْلِيلِ — وَالنَّدْبُ طَلَبٌ غَيْرُ جَازِمٍ.",
      "A jarr-majrur attaching to «may come», the LAM giving the reason — and a nadb is a request that does not bind: doing it earns, leaving it costs nothing.",
      "«يَرِدُ»a taalluk eden câr-mecrûr; LÂM ta'lîl içindir — nedb, bağlayıcı olmayan taleptir: yapan kazanır, terk eden bir şey kaybetmez.",
      segments=[seg("لِ","li","prep"), seg("النَّدْبِ","nadb","noun")]),
  tok("وَالْإِبَاحَةِ","ibaha","noun",["atf-nasaq","masdar","form-iv-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ «أَبَاحَ»، وَهُوَ أَجْوَفُ عُوِّضَ عَنْ عَيْنِهِ فِي الْمَصْدَرِ بِالتَّاءِ: «إِبَاحَة» لَا «إِبْوَاح» — كَـ«إِشَارَة» فِي الْبَابِ السَّابِقِ.",
      "Joined, in jarr — the masdar of أَبَاحَ, a HOLLOW verb whose melted middle is made good in the masdar by a ta marbuta: إِبَاحَة, not *إِبْوَاح. Exactly إِشَارَة in the chapter before. Two chapters, two verbs, one compensation.",
      "Ma'tûf, mecrûr — «أَبَاحَ»nin masdarı; ECVEF olup masdarda ayn harfinin kaybı TÂ ile telâfi edilmiştir: «إِبَاحَة», *«إِبْوَاح» değil — bir önceki bâbdaki «إِشَارَة» gibi. İki bâb, iki fiil, tek telâfi.",
      segments=[seg("وَ","wa","conj"), seg("الْإِبَاحَةِ","ibaha","noun")]),
  tok("بِقَرِينَةٍ","qarina","noun",["huruf-jarr","sifa-mushabbaha"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَرِدُ» — وَبِهِ اسْتَقَامَ الْحَدُّ: الْأَصْلُ الْوُجُوبُ، وَلَا يُتْرَكُ الْأَصْلُ إِلَّا بِدَلِيلٍ.",
      "A jarr-majrur attaching to «may come» — and it is what keeps the definition honest: the default is obligation, and a default is not abandoned without something to abandon it FOR.",
      "«يَرِدُ»a taalluk eden câr-mecrûr — tarifi ayakta tutan kayıttır: asıl olan vücûbdur ve asıl, bir delil olmadan terk edilmez.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("قَرِينَةٍ","qarina","noun")]),
 ],
 "jumal": [J("مُوجِبُهُ الْوُجُوبُ عِنْدَ الْإِطْلَاقِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("قَدْ يَرِدُ لِلنَّدْبِ وَالْإِبَاحَةِ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the prohibition is an utterance by which holding back from a thing is sought, in the manner of one above.",
 "tr": "Nehiy, kendisiyle bir fiilden el çekmenin, üstünlük cihetiyle istendiği sözdür."},
 "tokens": [
  tok("وَالنَّهْيُ","nahy","noun",["atf-nasaq","mubtada-khabar","masdar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«النَّهْيُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «نَهَى»، وَهُوَ نَاقِصٌ يَائِيٌّ.",
      "A joining waw; «the prohibition» is the mubtada in raf' — the masdar of نَهَى, a naqis yai.",
      "Atıf vâvı; «النَّهْيُ» merfû mübtedâdır — «نَهَى»nin masdarı; nâkıs-ı yâîdir.",
      segments=[seg("وَ","wa","conj"), seg("النَّهْيُ","nahy","noun")]),
  tok("قَوْلٌ","qawl","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَالْحَدُّ مَبْنِيٌّ عَلَى قَالَبِ حَدِّ الْأَمْرِ حَرْفًا بِحَرْفٍ.",
      "The khabar in raf' with its tanwin — and the definition is cast in the command's own mould, word for word. Only one phrase inside it changes, and that phrase is the whole difference.",
      "Tenvînli merfû haber — tarif, emrin tarifinin kalıbına harfi harfine dökülmüştür. İçinde yalnız tek bir ibare değişir ve bütün fark odur."),
  tok("يُطْلَبُ","talaba","verb",["naib-al-fail","jumla-sifa","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ نَعْتٌ لِـ«قَوْلٌ» فِي مَحَلِّ رَفْعٍ.",
      "A mudari built for the unnamed doer; the clause is a na't of «an utterance», in the position of raf'.",
      "Meçhûl sîgasında muzâri; cümle «قَوْلٌ»un na'tıdır, mahallen merfûdur."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُطْلَبُ»، وَالْهَاءُ الرَّابِطُ.",
      "A jarr-majrur attaching to «is sought», the HA the tie.",
      "«يُطْلَبُ»a taalluk eden câr-mecrûr; HÂ râbıtadır.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("الْكَفُّ","kaff","noun",["naib-al-fail","masdar","doubled-verbs"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ — مَصْدَرُ «كَفَّ»، وَهَذِهِ هِيَ الْكَلِمَةُ الْوَحِيدَةُ الَّتِي تَغَيَّرَتْ عَنْ حَدِّ الْأَمْرِ: هُنَاكَ «الْفِعْلُ» وَهُنَا «الْكَفُّ».",
      "The naib al-fa'il, in raf' — the masdar of كَفَّ. THIS is the one word that has changed from the command's definition: there the thing sought was الْفِعْلُ, the doing; here it is الْكَفُّ, the holding back. Everything else in the two sentences is identical, and a reader who notices that has understood both at once.",
      "Merfû nâib-i fâil — «كَفَّ»in masdarı. Emrin tarifinden DEĞİŞEN tek kelime budur: orada istenen «الْفِعْلُ», burada «الْكَفُّ»tür. İki cümlenin geri kalanı aynıdır; bunu fark eden okuyucu ikisini birden anlamıştır."),
  tok("عَنِ","an-prep","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ، مُتَعَلِّقٌ بِـ«الْكَفُّ» — وَكُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter of turning away from, attaching to «the holding back» — a masdar governs like its verb, which is why it can take an object of its own. Its nun takes a kasra because two sukuns met.",
      "Mücâveze için cer harfi; «الْكَفُّ»a taalluk eder — masdar fiili gibi amel eder, bu yüzden kendi mütealliki olur. İki sâkin karşılaştığı için nûnu kesra almıştır."),
  tok("الْفِعْلِ","fil","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ بِـ«عَنْ».", "In jarr after «an».", "«عَنْ» ile mecrûr."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("جِهَةِ","jiha","noun",["huruf-jarr","idafa-definiteness"], *JIHA),
  tok("الِاسْتِعْلَاءِ","istila","noun",["idafa-definiteness","masdar","form-x-verbs","ism-mamdud"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَأُعِيدَ بِعَيْنِهِ، فَالْقَيْدُ وَاحِدٌ فِي الطَّلَبَيْنِ.",
      "The mudaf ilayh in jarr, repeated word for word: the same restriction binds both kinds of request. Without it, a prayer would be a command.",
      "Mecrûr muzâfun ileyh; aynen tekrarlanmıştır — kayıt her iki talepte de birdir. O olmasa duâ da emir olurdu.",
      punct="."),
 ],
 "jumal": [J("النَّهْيُ قَوْلٌ يُطْلَبُ بِهِ الْكَفُّ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And what it obliges is forbiddenness, when it comes unqualified; and it may come for mere dislike.",
 "tr": "Mutlak geldiğinde îcâb ettiği şey tahrîmdir; kerâhet için de gelebilir."},
 "tokens": [
  tok("وَمُوجِبُهُ","mujib","noun",["atf-nasaq","mubtada-khabar","ism-fail","form-iv-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«مُوجِبُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ عَائِدَةٌ عَلَى «النَّهْيِ».",
      "A joining waw; «what it obliges» is the mubtada in raf' and a mudaf, its HA going back to «the prohibition» this time.",
      "Atıf vâvı; «مُوجِبُ» merfû mübtedâ ve muzâftır; HÂ bu defa «النَّهْيِ»e râcidir.",
      segments=[seg("وَ","wa","conj"), seg("مُوجِبُ","mujib","noun"), seg("هُ","pron-3ms","pron")]),
  tok("التَّحْرِيمُ","tahrim","noun",["mubtada-khabar","masdar","form-ii-verbs"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ «حَرَّمَ» عَلَى تَفْعِيلٍ، وَهُوَ صَحِيحُ اللَّامِ فَجَاءَ عَلَى أَصْلِهِ، بِخِلَافِ «تَعْدِيَة».",
      "The khabar in raf' — the masdar of حَرَّمَ on تَفْعِيل, and its lam is a SOUND letter, so the pattern stands as it is. Set it against تَعْدِيَة in chapter 3, where the lam was weak and a ta marbuta had to come in. Same wazn, two outcomes, and the root decides.",
      "Merfû haber — «حَرَّمَ»nin TEF'ÎL vezninde masdarı; lâmı SAHÎH olduğu için vezin olduğu gibi durur. Üçüncü bâbdaki «تَعْدِيَة» ile karşılaştır: orada lâm illetliydi ve tâ-i merbûta girmek zorunda kaldı. Aynı vezin, iki ayrı netice; kararı kök verir."),
  tok("عِنْدَ","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "An adverb in nasb, and a mudaf.", "Mansub zarf ve muzâf."),
  tok("الْإِطْلَاقِ","itlaq","noun",["idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْقَيْدُ نَفْسُهُ الَّذِي قُيِّدَ بِهِ الْأَمْرُ.",
      "The mudaf ilayh in jarr — the same restriction the command was given.",
      "Mecrûr muzâfun ileyh — emre konan kaydın aynısı.", punct="،"),
  tok("وَقَدْ","qad","part",["qad-harf","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«قَدْ» لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.",
      "A joining waw, and «qad» for «sometimes» before a mudari.",
      "Atıf vâvı; muzâri ile «قَدْ» taklîl içindir.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يَرِدُ","warada","verb",["mudari-marfu","mithal-verbs","qad-harf"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ سَقَطَتْ وَاوُهُ.",
      "A mudari in raf' — a mithal whose waw has dropped.",
      "Merfû muzâri — vâvı düşmüş misâl."),
  tok("لِلْكَرَاهَةِ","karaha","noun",["huruf-jarr","lam-taleel","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَرِدُ» — وَالْكَرَاهَةُ دُونَ التَّحْرِيمِ، فَالنَّهْيُ يَنْزِلُ دَرَجَةً كَمَا نَزَلَ الْأَمْرُ إِلَى النَّدْبِ.",
      "A jarr-majrur attaching to «may come» — and dislike is a step below forbiddenness, just as the command stepped down to recommendation. The two sentences fall the same distance, which is the point of writing them as a pair.",
      "«يَرِدُ»a taalluk eden câr-mecrûr — kerâhet, tahrîmin bir derece altındadır; emir nedbe indiği gibi nehiy de bir basamak iner. İki cümlenin aynı mesafeyi düşmesi, onları çift yazmanın sebebidir.",
      punct=".", segments=[seg("لِ","li","prep"), seg("الْكَرَاهَةِ","karaha","noun")]),
 ],
 "jumal": [J("مُوجِبُهُ التَّحْرِيمُ عِنْدَ الْإِطْلَاقِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the form of the command is «do», and what stands in its place; and the form of the prohibition is «do not do».",
 "tr": "Emrin sîgası «افْعَلْ» ve onun yerini tutanlardır; nehyin sîgası ise «لَا تَفْعَلْ»dır."},
 "tokens": [
  tok("وَصِيغَةُ","sigha","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«صِيغَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "A joining waw; «the form of» is the mubtada in raf' and a mudaf.",
      "Atıf vâvı; «صِيغَةُ» merfû mübtedâ ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("صِيغَةُ","sigha","noun")]),
  tok("الْأَمْرِ","amr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("افْعَلْ","faala","verb",["imperative-amr","mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ فِي مَحَلِّهِ — لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فَلَا يُعْرَبُ بِحَرَكَةٍ. وَهُوَ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَأَلِفُهُ أَلِفُ وَصْلٍ اجْتُلِبَتْ لِتَعَذُّرِ الِابْتِدَاءِ بِسَاكِنٍ.",
      "The khabar, in the POSITION of raf' — a word QUOTED for its own shape, so it wears no ending of its own. In itself it is an imperative, fixed on a sukun, and its alif is a WASL alif brought in only because Arabic cannot begin on a silent letter. Put anything at all before it and the alif stops being pronounced: وَافْعَلْ.",
      "Mahallen merfû haber — kendi lafzı kastedilerek HİKÂYE edilmiş bir kelimedir, dolayısıyla kendi i'râbını almaz. Kendisi sükûn üzere mebnî emir fiilidir ve elifi VASIL elifidir: Arapça sâkinle başlayamadığı için getirilmiştir. Önüne herhangi bir şey gel, elif okunmaz olur: وَافْعَلْ."),
  tok("وَمَا","ma-mawsula","pron",["atf-nasaq","ism-mawsul"],
      "الْوَاوُ عَاطِفَةٌ، وَ«مَا» اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.",
      "A joining waw, and «ma» a relative noun joined to it, in the position of raf'.",
      "Atıf vâvı; «مَا» ma'tûf ism-i mevsûldür, mahallen merfûdur.",
      segments=[seg("وَ","wa","conj"), seg("مَا","ma-mawsula","pron")]),
  tok("نَابَ","naba","verb",["fail","jumla-sifa","hollow-verbs"],
      "فِعْلٌ مَاضٍ أَجْوَفُ وَاوِيٌّ («ن و ب»)، وَالْجُمْلَةُ صِلَةٌ — وَبِهَذَا الْعَطْفِ لَمْ يَنْحَصِرِ الْأَمْرُ فِي صِيغَةٍ وَاحِدَةٍ: الْمُضَارِعُ الْمَجْزُومُ بِلَامِ الْأَمْرِ يَنُوبُ عَنْهَا، وَكَذَلِكَ الْمَصْدَرُ وَالْخَبَرُ الْمُرَادُ بِهِ الطَّلَبُ.",
      "A past verb, an AJWAF WAWI from ن و ب; the clause is the sila. This little joining is what keeps the command from being trapped in one written shape: a mudari in jazm after the lam of command stands in for it, and so does a masdar, and so does a statement meant as a demand. A definition tied to a single spelling would have been false.",
      "«ن و ب»dan ECVEF-İ VÂVÎ mâzî fiil; cümle sıladır. Bu küçük atıf, emri tek bir yazılı şekle hapsolmaktan kurtarır: lâm-ı emirle meczûm muzâri onun yerini tutar, masdar da tutar, talep kastedilen haber cümlesi de. Tek bir imlâya bağlanan tarif yanlış olurdu."),
  tok("عَنْهَا","an-prep","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«نَابَ»، وَالضَّمِيرُ عَائِدٌ عَلَى «صِيغَةِ».",
      "A jarr-majrur attaching to «stands in», the pronoun going back to «the form».",
      "«نَابَ»ya taalluk eden câr-mecrûr; zamîr «صِيغَةِ»ye râcidir.",
      punct="،", segments=[seg("عَنْ","an-prep","prep"), seg("هَا","pron-3fs","pron")]),
  tok("وَصِيغَةُ","sigha","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«صِيغَةُ» مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "A joining waw, and «the form of» a second mubtada in raf' and a mudaf.",
      "Atıf vâvı; «صِيغَةُ» ikinci merfû mübtedâ ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("صِيغَةُ","sigha","noun")]),
  tok("النَّهْيِ","nahy","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("لَا","la-nahiya","part",["la-nahiya"],
      "«لَا» نَاهِيَةٌ جَازِمَةٌ — وَهِيَ غَيْرُ «لَا» النَّافِيَةِ الَّتِي مَرَّتْ فِي بَابِ الْمُحْكَمِ: تِلْكَ لَا تَعْمَلُ، وَهَذِهِ تَجْزِمُ.",
      "«La» of PROHIBITION, and it puts the verb into jazm — not the plain denying «la» that stood in the chapter on the muhkam. That one governs nothing; this one does. Two letters spelled the same, and only the ending of the verb after them tells you which you are reading.",
      "NEHİY «لَا»sıdır ve fiili cezm eder — muhkem bâbında geçen nefy «لَا»sı değildir: o amel etmez, bu eder. Aynı yazılan iki harf; hangisini okuduğunu ancak sonraki fiilin sonu söyler."),
  tok("تَفْعَلْ","faala","verb",["la-nahiya","imperative-amr"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَا» النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ — وَهُوَ أَيْضًا لَفْظٌ مَحْكِيٌّ، وَالْجُمْلَةُ كُلُّهَا خَبَرٌ فِي مَحَلِّ رَفْعٍ.",
      "A mudari in JAZM after the prohibiting «la», its sign a sukun — and it too is quoted for its own shape, the pair standing as the khabar in the position of raf'. Note the whole lesson of the sentence: the command has its own form, the prohibition borrows the present tense and bends it.",
      "Nehiy «لَا»sı ile meczûm muzâri; cezm alâmeti sükûndur — bu da kendi lafzı kastedilerek hikâye edilmiştir ve ikisi birlikte mahallen merfû haberdir. Cümlenin bütün dersi şudur: emrin kendi sîgası vardır, nehiy ise muzârii ödünç alıp büker.",
      punct="."),
 ],
 "jumal": [J("صِيغَةُ الْأَمْرِ افْعَلْ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("مَا نَابَ عَنْهَا",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "amr":     g("أَمْر", "أ م ر", "noun", "a command (masdar; plural أَوَامِر)", "emir (masdar)", 2, plural="أَوَامِر"),
 "nahy":    g("نَهْي", "ن ه ي", "noun", "a prohibition (masdar)", "nehiy (masdar)", 3),
 "jiha":    g("جِهَة", "و ج ه", "noun", "a side, a manner, a respect", "cihet, yön", 3),
 "istila":  g("اِسْتِعْلَاء", "ع ل و", "noun", "counting oneself above the one addressed (masdar, Form X)", "isti'lâ; kendini üstün görme (masdar)", 5),
 "talaba":  g("طَلَبَ", "ط ل ب", "verb", "to seek, to demand", "istemek, talep etmek", 2),
 "mujib":   g("مُوجِب", "و ج ب", "noun", "what a thing obliges (ism fa'il, Form IV)", "mûcib; îcâb ettiren", 4),
 "wujub":   g("وُجُوب", "و ج ب", "noun", "obligation (masdar)", "vücûb (masdar)", 3),
 "inda":    g("عِنْدَ", None, "noun", "at, in the case of (adverb)", "…-de, …hâlinde (zarf)", 1),
 "itlaq":   g("إِطْلَاق", "ط ل ق", "noun", "coming unqualified, without an indication (masdar, Form IV)", "ıtlâk; kayıtsız gelme (masdar)", 4),
 "warada":  g("وَرَدَ", "و ر د", "verb", "to come, to arrive (of a text)", "vârid olmak, gelmek", 3),
 "nadb":    g("نَدْب", "ن د ب", "noun", "recommendation — a request that does not bind (masdar)", "nedb; bağlayıcı olmayan talep (masdar)", 4),
 "ibaha":   g("إِبَاحَة", "ب و ح", "noun", "permission — leave to do or not do (masdar, Form IV)", "ibâha; serbest bırakma (masdar)", 4),
 "qarina":  g("قَرِينَة", "ق ر ن", "noun", "an indication that qualifies a wording", "karîne; lafzı kayıtlayan delâlet", 4, plural="قَرَائِن"),
 "kaff":    g("كَفّ", "ك ف ف", "noun", "holding back, refraining (masdar)", "kef; el çekme (masdar)", 3),
 "tahrim":  g("تَحْرِيم", "ح ر م", "noun", "forbiddenness (masdar, Form II)", "tahrîm (masdar)", 4),
 "karaha":  g("كَرَاهَة", "ك ر ه", "noun", "dislike — a step below forbiddenness (masdar)", "kerâhet (masdar)", 4),
 # افْعَلْ and تَفْعَلْ are not two words: they are two CELLS of فَعَلَ, the verb
 # the whole science uses as its dummy. Giving them lex keys of their own put
 # two verbs in the glossary with no paradigm behind them — and the suite is
 # right to refuse that. Pointed at فَعَلَ they conjugate, and tapping either one
 # opens the paradigm with its own cell lit.
 "faala":   g("فَعَلَ", "ف ع ل", "verb", "to do — the verb the grammarians conjugate as their model", "yapmak — gramercilerin örnek fiili", 1),
 "naba":    g("نَابَ", "ن و ب", "verb", "to stand in for, to take the place of", "yerini tutmak, niyâbet etmek", 4),
 "la-nahiya": g("لَا (النَّاهِيَة)", None, "part", "do not — the la that puts a verb into jazm", "…-ma (fiili cezm eden nehiy lâsı)", 3),
 # افْعَلْ and تَفْعَلْ are QUOTED shapes, not verbs this package conjugates.
 # `pos: "part"` would be a lie about what they are, so they stay verbs and the
 # validator's "no paradigm" warning is the honest state of affairs: the corpus
 # carries the citation form and nothing else, because nothing else is meant.
 "qad":     g("قَدْ", None, "part", "indeed (with the past); sometimes (with the present)", "muhakkak (mâzî ile); bazen (muzâri ile)", 2),
}

def build_morph():
    out = {}
    # طَلَبَ — copied; three packages carry it and they agree.
    s = json.loads((ROOT / "content/samples/jumal-al-tadrib/morphology.json").read_text(encoding="utf-8"))
    out["talaba"] = s["verbs"]["talaba"]
    # وَرَدَ — MITHAL WAWI, bab daraba. The waw goes because a KASRA follows it
    # in the mudari; يَوْجَلُ, with a fatha, keeps its own.
    out["warada"] = _sg.sound1("daraba", "وَرَد", "رِد", "رِد", "وُرُود", "وَارِد",
                               note="مِثَالٌ وَاوِيٌّ: سَقَطَتِ الْوَاوُ لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ — يَرِدُ.")
    # فَعَلَ — the model verb itself, bab fataha.
    out["faala"] = _sg.sound1("fataha", "فَعَل", "فْعَل", "اِفْعَل", "فِعْل", "فَاعِل",
                              maful="مَفْعُول", pmz="فُعِلَ", pmd="يُفْعَلُ",
                              note="وَهُوَ الْمِيزَانُ الَّذِي تُوزَنُ بِهِ الْكَلِمَاتُ كُلُّهَا.")
    # نَابَ — AJWAF WAWI, bab nasara. Stems go in WITHOUT their sukun, and the
    # amr needs both: the long one for the vowel-initial persons.
    out["naba"] = _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "نَاب", "نُب", "نُوب", "نُب",
                              "نُوب", "نُب", "نِيَابَة", "نَائِب",
                              note="أَجْوَفُ وَاوِيٌّ: نَابَ يَنُوبُ، وَمَصْدَرُهُ نِيَابَةٌ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/8.json").write_text(
    json.dumps({"chapter": 8, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 8 for c in man["chapters"]):
    man["chapters"].append({"n": 8, "title": TITLE8})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.8.0"
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة، ثم أقسام اللفظ ووجوه البيان، ثم الأمر والنهي",
                   "en": "The opening definitions, the four sources, the divisions of the wording, the ways a text speaks, and the command and the prohibition",
                   "tr": "Açılış tarifleri, deliller, lafzın kısımları, beyânın vecihleri ve emir ile nehiy"}
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
# An earlier pass keyed the two quoted sighas as verbs of their own. They are
# cells of فَعَلَ, not words; the keys are cleared so a re-run leaves no verb
# without a paradigm behind it.
for _stale in ("ifal", "tafal"):
    gl["entries"].pop(_stale, None)
gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch8:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
