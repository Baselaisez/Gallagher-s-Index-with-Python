# -*- coding: utf-8 -*-
"""Author chapter 14 of mukhtasar-al-manar — the PILLARS OF ANALOGY.

Chapter 3 defined qiyas in one line and moved on. Eleven chapters later the
matn comes back and takes it apart: four pillars, each defined, and then the
one pillar that carries the weight — the ʿilla — given a condition of its own.
This is the same move chapter 13 made on the Sunna, and it is how a matn
works: name the term early, dismantle it when the reader can bear it.

ATTRIBUTION: like chapters 2–13, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • لَمْ يَرِدْ — the JAZM of the mithal chapter 8 showed in raf'. يَرِدُ becomes
    يَرِدْ, and the waw that dropped in the mudari stays gone: one weakness does
    not repair another.
  • عُلِّقَ — the MAJHUL of Form II, the fourth passive class in the package
    after Form I, Form V and Form X.
  • أَنْ تَكُونَ ظَاهِرَةً — أَنْ الْمَصْدَرِيَّة over كَانَ, so the nasb falls on the
    verb and the khabar takes its own nasb from كَانَ. Two nasbs, two reasons.
  • لَا تَخْتَلِفُ — a clause standing as a na't of a MANSUB indefinite, which is
    the third position the package has shown a jumla sifa in.
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

TITLE14 = {"ar": "أَرْكَانُ الْقِيَاس", "en": "The Pillars of Analogy",
           "tr": "Kıyâsın Rükünleri"}

S.append({"id": "s1", "translation": {
 "en": "Then the pillars of analogy are four: the root case, the branch case, the ruling of the root, and the cause.",
 "tr": "Kıyâsın rükünleri dörttür: asıl, fer', aslın hükmü ve illet."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَالتَّرَاخِي هُنَا أَحَدَ عَشَرَ بَابًا: عُرِّفَ الْقِيَاسُ فِي الثَّالِثِ وَفُصِّلَ هُنَا.",
      "A letter of atf giving sequence with an interval — and here the interval is eleven chapters. Qiyas was defined in chapter 3 in a single line; it is taken apart only now. The same move chapter 13 made on the Sunna.",
      "Terâhî ile tertîb için atıf harfi — ve buradaki terâhî on bir bâbdır: kıyâs üçüncü bâbda tek satırda tarif edilmiş, ancak burada tafsîl edilmiştir. On üçüncü bâbın sünnete yaptığının aynısı."),
  tok("أَرْكَانُ","arkan","noun",["mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ «رُكْنٍ»، وَالرُّكْنُ مَا لَا يَقُومُ الشَّيْءُ إِلَّا بِهِ، بِخِلَافِ الشَّرْطِ فَإِنَّهُ خَارِجٌ عَنْهُ.",
      "The mubtada in raf' and a mudaf — the plural of «rukn». A PILLAR is what a thing does not stand without and what is part of it; a CONDITION is also required but stands outside. The matn will use both words in this chapter and the distinction is exact.",
      "Merfû mübtedâ ve muzâf — «رُكْن»ün cemi. RÜKÜN, bir şeyin kendisiyle ayakta durduğu ve ONDAN BİR PARÇA olan şeydir; ŞART da gereklidir fakat DIŞINDA kalır. Metin bu bâbda her iki kelimeyi de kullanır ve ayrım tamdır."),
  tok("الْقِيَاسِ","qiyas","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الرَّابِعُ مِنَ الْأَدِلَّةِ، آخِرُ مَا بَقِيَ لِلتَّفْصِيلِ.",
      "The mudaf ilayh in jarr — the fourth of the sources, and the last of them still awaiting its detail.",
      "Mecrûr muzâfun ileyh — delillerin dördüncüsü ve tafsîlini bekleyen sonuncusudur."),
  tok("أَرْبَعَةٌ","arbaa","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — غَيْرُ مُضَافٍ، فَتَنْوِينُهُ ثَابِتٌ.",
      "The khabar in raf' with its tanwin — not a mudaf here, so the tanwin stands. The fourth time this numeral has appeared in the book and the third office it has held.",
      "Tenvînli merfû haber — burada muzâf değildir, bu yüzden tenvîni durur. Bu sayının kitaptaki dördüncü geçişi ve üstlendiği üçüncü vazifedir.", punct="："),
  tok("الْأَصْلُ","asl","noun",["badal"],
      "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ — وَهُوَ الْمَقِيسُ عَلَيْهِ، وَقَدْ عُرِّفَ بِهَذَا الْمَعْنَى فِي بَابِ الْقِيَاسِ.",
      "A badal of detail, in raf' — the case measured AGAINST, already named with this sense in chapter 3.",
      "Merfû tafsîl bedeli — kendisine kıyas edilen taraf; bu mânâda üçüncü bâbda geçmişti."),
  tok("وَالْفَرْعُ","far","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ — وَهُوَ الْمَقِيسُ.",
      "Joined, in raf' — the case being measured.",
      "Ma'tûf, merfû — kıyas edilen taraf.",
      segments=[seg("وَ","wa","conj"), seg("الْفَرْعُ","far","noun")]),
  tok("وَحُكْمُ","hukm","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَهَذَا الرُّكْنُ وَحْدَهُ مُرَكَّبٌ، وَالثَّلَاثَةُ الْبَاقِيَةُ أَلْفَاظٌ مُفْرَدَةٌ.",
      "Joined, in raf' and a MUDAF — and this pillar alone is a phrase, while the other three are single words. A list may hold members of different weight; the atf does not level them.",
      "Ma'tûf, merfû ve MUZÂF — bu rükün tek başına bir terkîbdir, kalan üçü müfred kelimelerdir. Bir liste farklı ağırlıkta üyeler taşıyabilir; atıf onları eşitlemez.",
      segments=[seg("وَ","wa","conj"), seg("حُكْمُ","hukm","noun")]),
  tok("الْأَصْلِ","asl","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَ«الْأَصْلُ» مَذْكُورٌ مَرَّتَيْنِ فِي سَطْرٍ وَاحِدٍ: مَرْفُوعًا بَدَلًا وَمَجْرُورًا مُضَافًا إِلَيْهِ.",
      "The mudaf ilayh in jarr — and «the root» stands twice in one line, once in raf' as a badal and once in jarr as a mudaf ilayh. Same word, two endings, two offices, and no reader who sees that will confuse a list with a phrase again.",
      "Mecrûr muzâfun ileyh — «الْأَصْل» tek satırda iki defa geçer: biri bedel olarak merfû, öteki muzâfun ileyh olarak mecrûr. Aynı kelime, iki son, iki vazife; bunu gören okuyucu bir daha listeyi terkîble karıştırmaz."),
  tok("وَالْعِلَّةُ","illah","noun",["atf-nasaq","doubled-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — وَبِهِ تَمَّتِ الْأَرْكَانُ أَرْبَعَةً، وَهُوَ الرُّكْنُ الَّذِي عَلَيْهِ الْمَدَارُ.",
      "Joined, in raf' — and with it the four pillars are complete. It is the one they all turn on: the other three are given, and finding the ʿilla is the whole labour of the jurist.",
      "Ma'tûf, merfû — rükünler bununla dörde tamamlanır. Üzerinde medâr olan rükün odur: kalan üçü verilidir, illeti bulmak ise müctehidin bütün emeğidir.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("الْعِلَّةُ","illah","noun")]),
 ],
 "jumal": [J("أَرْكَانُ الْقِيَاسِ أَرْبَعَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the root case is that whose ruling the text came with.",
 "tr": "Asıl, hükmüyle nassın geldiği şeydir."},
 "tokens": [
  tok("فَالْأَصْلُ","asl","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْأَصْلُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the root case» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الْأَصْلُ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْأَصْلُ","asl","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("وَرَدَ","warada","verb",["fail","jumla-sifa","mithal-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ — مِثَالٌ وَاوِيٌّ، وَوَاوُهُ ثَابِتَةٌ فِي الْمَاضِي لِأَنَّ الْعِلَّةَ إِنَّمَا تَعْرِضُ فِي الْمُضَارِعِ.",
      "A past verb; the clause is the sila — a MITHAL WAWI, and its waw STANDS in the past. The weakness only shows in the mudari, where a kasra pushes the waw out; nothing pushes it in وَرَدَ. A weak letter is not weak everywhere, only where its surroundings make it so.",
      "Mâzî fiil; cümle sıladır — MİSÂL-İ VÂVÎdir ve vâvı mâzîde DURUR. İllet yalnız muzâride ârız olur; orada bir kesra vâvı iter, «وَرَدَ»de ise iten bir şey yoktur. İlletli harf her yerde illetli değildir, ancak çevresi onu öyle kıldığı yerde."),
  tok("النَّصُّ","nass","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.", "The fa'il, in raf'.", "Merfû fâil."),
  tok("بِحُكْمِهِ","hukm","noun",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«وَرَدَ»، وَ«حُكْمِ» مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ وَهِيَ الْعَائِدُ عَلَى «مَا» — وَالْبَاءُ لِلْمُصَاحَبَةِ: جَاءَ النَّصُّ وَمَعَهُ حُكْمُهُ.",
      "A jarr-majrur attaching to «came», «its ruling» a mudaf with the HA its mudaf ilayh — and that HA is the pronoun tying the sila back to «that which». The BA is of accompaniment: the text arrived and brought the ruling with it. Note where the tie sits this time — not on the verb, not on the object, but inside a possessive two words deep.",
      "«وَرَدَ»ye taalluk eden câr-mecrûr; «حُكْمِ» muzâf, HÂ muzâfun ileyhtir ve sılayı «مَا»ya bağlayan âiddir. BÂ musâhabe içindir: nass geldi ve hükmünü beraberinde getirdi. Râbıtanın bu defa nerede durduğuna dikkat: ne fiilde ne mef'ûlde, iki kelime derinlikte bir izâfetin içinde.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("حُكْمِ","hukm","noun"), seg("هِ","pron-3ms","pron")]),
 ],
 "jumal": [J("وَرَدَ النَّصُّ بِحُكْمِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the branch case is that in which no text came.",
 "tr": "Fer', hakkında nass gelmemiş olandır."},
 "tokens": [
  tok("وَالْفَرْعُ","far","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْفَرْعُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the branch case» is the mubtada in raf'.",
      "Atıf vâvı; «الْفَرْعُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْفَرْعُ","far","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("لَمْ","lam-jazim","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَقَدْ مَرَّ فِي بَابِ الْإِشَارَةِ عَلَى «يَكُنْ»، وَهَا هُوَ عَلَى مِثَالٍ.",
      "A letter that denies, puts into JAZM and turns the time to the past — met in chapter 7 over يَكُنْ, and here over a mithal. The two together show that لَمْ does not care what class the verb belongs to: it takes the ending off whatever it finds.",
      "Nefy, cezm ve kalb harfi — yedinci bâbda «يَكُنْ» üzerinde geçmişti, burada bir misâl üzerindedir. İkisi birlikte «لَمْ»in fiilin sınıfını umursamadığını gösterir: neyi bulursa sonunu alır."),
  tok("يَرِدْ","warada","verb",["lam-jazim","mithal-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ — وَقَابِلْهُ بِـ«يَرِدُ» فِي بَابِ الْأَمْرِ: هُنَاكَ مَرْفُوعٌ بِالضَّمَّةِ وَهُنَا مَجْزُومٌ بِالسُّكُونِ. وَالْوَاوُ سَاقِطَةٌ فِي الْحَالَيْنِ: الْجَزْمُ يَأْخُذُ الْحَرَكَةَ الْأَخِيرَةَ وَلَا يَرُدُّ حَرْفًا ذَهَبَ لِعِلَّةٍ أُخْرَى.",
      "A mudari in JAZM after «lam», its sign a sukun. Set it against يَرِدُ in chapter 8: there in raf' by a damma, here in jazm by a sukun. And the waw is gone in BOTH — the jazm takes the last vowel off and does not bring back a letter that left for another reason entirely. Two weaknesses, two causes, and neither repairs the other.",
      "«لَمْ» ile meczûm muzâri; cezm alâmeti sükûndur. Sekizinci bâbdaki «يَرِدُ» ile karşılaştır: orada damme ile merfû, burada sükûn ile meczûm. Ve vâv HER İKİSİNDE de yoktur — cezm son harekeyi alır, başka bir illetle giden bir harfi geri getirmez. İki zayıflık, iki ayrı sebep; hiçbiri ötekini tamir etmez."),
  tok("فِيهِ","fi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَرِدْ»، وَالْهَاءُ الْعَائِدُ عَلَى «مَا».",
      "A jarr-majrur attaching to «came», the HA the pronoun going back to «that which» — the tie again, and in a third place: on a preposition this time.",
      "«يَرِدْ»e taalluk eden câr-mecrûr; HÂ «مَا»ya râci âiddir — râbıta yine, ve bu defa üçüncü bir yerde: bir cer harfinin üzerinde.",
      segments=[seg("فِي","fi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("نَصٌّ","nass","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ مُنَوَّنٌ — وَجَاءَ نَكِرَةً فِي سِيَاقِ النَّفْيِ فَأَفَادَ الْعُمُومَ: لَا نَصَّ مِنْ أَيِّ نَوْعٍ. وَقَابِلْهُ بِـ«النَّصُّ» مُعَرَّفًا فِي الْحَدِّ السَّابِقِ.",
      "The fa'il in raf' with its tanwin — and INDEFINITE inside a negation, which makes it general: no text of any kind came. Set it against the definite النَّصُّ of the definition before. An indefinite under a negation says «none at all»; a definite one would have said «not THE text», which is a much smaller claim.",
      "Tenvînli merfû fâil — nefy siyâkında NEKREdir ve bu ona umûm kazandırır: hiçbir cinsten nass gelmemiştir. Bir önceki tarifteki marife «النَّصُّ» ile karşılaştır. Nefy altındaki nekre «hiç yok» der; marife olsaydı «o nass değil» derdi ki bu çok daha küçük bir iddiadır.",
      punct="."),
 ],
 "jumal": [J("لَمْ يَرِدْ فِيهِ نَصٌّ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And the cause is the property upon which the ruling was hung.",
 "tr": "İllet, hükmün kendisine bağlandığı vasıftır."},
 "tokens": [
  tok("وَالْعِلَّةُ","illah","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْعِلَّةُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the cause» is the mubtada in raf'.",
      "Atıf vâvı; «الْعِلَّةُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْعِلَّةُ","illah","noun")]),
  tok("الْوَصْفُ","wasf","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ مُعَرَّفٌ — وَلَاحِظِ الْعُدُولَ عَنْ «مَا» الْمَوْصُولَةِ الَّتِي بُنِيَتْ عَلَيْهَا حُدُودُ الْكِتَابِ كُلُّهَا: هُنَا اسْمٌ صَرِيحٌ ثُمَّ «الَّذِي». وَالْمَعْنَى وَاحِدٌ وَالْأُسْلُوبُ أَدَقُّ، لِأَنَّ الْمَقْصُودَ جِنْسٌ مَعْلُومٌ لَا شَيْءٌ مُبْهَمٌ.",
      "The khabar in raf', and DEFINITE. Notice the turn away from the مَا that every other definition in this book is built on: here a plain noun, then الَّذِي. The sense is the same and the wording is sharper, because what is meant is a known kind — a property — and not an unspecified «that which». The matn changes its instrument when the thing being defined has a name.",
      "Marife merfû haber — ve kitaptaki bütün tariflerin üzerine kurulduğu mevsûl «مَا»dan sapmaya dikkat: burada sarîh bir isim, ardından «الَّذِي». Mânâ aynı, üslûp daha keskindir; zira kastedilen bilinen bir cinstir — bir vasıf — mübhem bir «şey» değil. Metin, tarif edilen şeyin adı varsa âletini değiştirir."),
  tok("الَّذِي","alladhi","pron",["ism-mawsul","naat-sifa"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«الْوَصْفُ» — وَجَاءَ الْمَوْصُولُ نَعْتًا لِأَنَّ مَنْعُوتَهُ مَعْرِفَةٌ، وَالْمَوْصُولَاتُ كُلُّهَا مَعَارِفُ.",
      "A relative noun, fixed in form, in the position of raf' as a NA'T of «the property» — and a relative may serve as a na't only because it is itself definite: every mawsul is a definite noun. Chapter 3 showed الَّتِي doing the same work in the feminine.",
      "«الْوَصْفُ»un na'tı olarak mahallen merfû mebnî ism-i mevsûl — mevsûlün na't olabilmesi, kendisinin marife olmasındandır: bütün mevsûller marifedir. Üçüncü bâb aynı işi müennes «الَّتِي» ile göstermişti."),
  tok("عُلِّقَ","allaqa","verb",["naib-al-fail","form-ii-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ عَلَى «فَعَّلَ»، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ — وَبِنَاءُ الْمَاضِي لِلْمَجْهُولِ هُوَ هُوَ فِي كُلِّ بَابٍ: ضَمُّ الْأَوَّلِ وَكَسْرُ مَا قَبْلَ الْآخِرِ. «عَلَّقَ» ← «عُلِّقَ».",
      "A past verb built for the unnamed doer, on فَعَّلَ; the clause is the sila. The rule for the past passive is the same in every bab: a damma on the first letter and a kasra before the last. عَلَّقَ becomes عُلِّقَ. Four passives now stand in this package — Form I, Form II, Form V and Form X — and one rule accounts for all four in the past.",
      "«فَعَّلَ» vezninde meçhûl mâzî fiil; cümle ism-i mevsûlün sılasıdır. Mâzînin meçhûl binâsı her bâbda aynıdır: başı ötreli, son harften öncesi esreli. «عَلَّقَ» → «عُلِّقَ». Bu pakette artık dört meçhûl vardır — birinci, ikinci, beşinci ve onuncu bâblar — ve mâzîde dördünü de tek kaide açıklar."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«عُلِّقَ»، وَالْهَاءُ الْعَائِدُ عَلَى «الَّذِي» — وَالْبَاءُ لِلْإِلْصَاقِ: الْحُكْمُ مُعَلَّقٌ بِالْوَصْفِ كَمَا يُعَلَّقُ الشَّيْءُ بِمِسْمَارِهِ.",
      "A jarr-majrur attaching to «was hung», the HA going back to «which». The BA is of ATTACHMENT, and the image is exact: the ruling hangs on the property as a thing hangs on its nail. Remove the property and the ruling has nothing to hold it — which is the whole warrant for carrying it to another case that has the same nail.",
      "«عُلِّقَ»ye taalluk eden câr-mecrûr; HÂ «الَّذِي»ye râcidir. BÂ ilsâk içindir ve teşbîh tamdır: hüküm, bir şeyin çivisine asılması gibi vasfa asılır. Vasfı kaldır, hükmü tutan bir şey kalmaz — aynı çiviyi taşıyan başka bir tarafa taşınmasının bütün gerekçesi de budur.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("الْحُكْمُ","hukm","noun",["naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ — وَقَدْ وَرَدَ «الْحُكْم» فِي هَذَا الْبَابِ ثَلَاثَ مَرَّاتٍ: مُضَافًا، وَمَجْرُورًا بِالْبَاءِ، وَنَائِبَ فَاعِلٍ.",
      "The naib al-fa'il, in raf' — and الْحُكْم has now stood three times in this chapter alone: as a mudaf, in jarr after a ba, and as a naib al-fa'il. Three endings on one word inside four sentences, each earned by a different office.",
      "Merfû nâib-i fâil — «الْحُكْم» yalnız bu bâbda üç defa geçmiştir: muzâf olarak, bâ ile mecrûr olarak ve nâib-i fâil olarak. Dört cümle içinde tek kelimede üç ayrı son, her biri başka bir vazifeyle hak edilmiş.",
      punct="."),
 ],
 "jumal": [J("عُلِّقَ بِهِ الْحُكْمُ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And its condition is that it be evident and well defined, not varying with varying states.",
 "tr": "Şartı, zâhir ve munzabıt olması; hâllerin değişmesiyle değişmemesidir."},
 "tokens": [
  tok("وَشَرْطُهَا","shart","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«شَرْطُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالشَّرْطُ خَارِجٌ عَنِ الْمَاهِيَّةِ، بِخِلَافِ الرُّكْنِ الَّذِي فُتِحَ بِهِ الْبَابُ.",
      "A joining waw; «its condition» is the mubtada in raf' and a mudaf, the HA its mudaf ilayh — and a CONDITION stands outside the thing it conditions, unlike the PILLAR the chapter opened with. The matn used both words deliberately and one sentence apart, so that the reader could feel the difference rather than be told it.",
      "Atıf vâvı; «شَرْطُ» merfû mübtedâ ve muzâftır, HÂ muzâfun ileyhtir — ve ŞART, şart koştuğu şeyin DIŞINDA durur; bâbın açıldığı RÜKÜNün aksine. Metin iki kelimeyi de kasten ve bir cümle arayla kullandı ki okuyucu farkı anlatılarak değil hissederek öğrensin.",
      segments=[seg("وَ","wa","conj"), seg("شَرْطُ","shart","noun"), seg("هَا","pron-3fs","pron")]),
  tok("أَنْ","an-nasiba","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِمَّا بَعْدَهُ خَبَرُ «شَرْطُ».",
      "A masdar-making letter that puts the mudari into nasb, and the masdar muawwal it forms with what follows is the KHABAR of «its condition» — «its condition is its BEING evident». The same particle chapter 4 used in أَنْ يُوجِبَ, there making a khabar too.",
      "Masdariyye ve nâsıbe harfi; kendisiyle sonrasından çıkan masdar-ı müevvel «شَرْطُ»un HABERİdir — «şartı, zâhir OLMASIdır». Dördüncü bâbdaki «أَنْ يُوجِبَ»in aynı harfi; orada da haber yapıyordu."),
  tok("تَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هِيَ» — وَالْوَاوُ ثَابِتَةٌ هُنَا لِأَنَّ النَّصْبَ لَا يُسْكِنُ الْآخِرَ، بِخِلَافِ «لَمْ يَكُنْ».",
      "A mudari of the incomplete kind, in NASB after «an», its mark the fatha, with a hidden «she» for its ism. And the WAW stands here: nasb puts a fatha on the last letter and leaves the long vowel alone, where jazm silences the last letter and forces the waw out — لَمْ يَكُنْ. The same verb, two governors, and the weak letter survives one and not the other.",
      "«أَنْ» ile mansub nâkıs muzâri; nasb alâmeti fethadır, ismi müstetir «هِيَ»dir. Ve VÂV burada DURUR: nasb son harfe fetha koyar, med harfine dokunmaz; cezm ise son harfi sâkin kılar ve vâvı dışarı atar — «لَمْ يَكُنْ». Aynı fiil, iki âmil; illetli harf birinden sağ çıkar, ötekinden çıkmaz."),
  tok("ظَاهِرَةً","zahir","noun",["kana-wa-akhawatuha","ism-fail"],
      "خَبَرُ «تَكُونَ» مَنْصُوبٌ — وَفِي الْجُمْلَةِ نَصْبَانِ لِسَبَبَيْنِ: نَصْبُ الْفِعْلِ بِـ«أَنْ»، وَنَصْبُ هَذَا الِاسْمِ بِـ«كَانَ».",
      "«Takuna»'s khabar, in nasb — and note that there are TWO nasbs in this clause for two different reasons: the verb is in nasb because أَنْ governs it, and this noun is in nasb because كَانَ governs it. Two accusatives side by side and no relation between their causes.",
      "«تَكُونَ»nin mansub haberi — ve bu cümlede İKİ nasb, iki ayrı sebeple vardır: fiili «أَنْ» nasb etmiştir, bu ismi ise «كَانَ». Yan yana iki mansub ve sebepleri arasında hiçbir bağ yok."),
  tok("مُنْضَبِطَةً","muntabit","noun",["naat-sifa","ism-fail","form-vii-verbs"],
      "نَعْتٌ لِـ«ظَاهِرَةً» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «اِنْضَبَطَ» عَلَى مُنْفَعِلٍ، وَالْمَعْنَى: لَهَا حَدٌّ لَا تَتَجَاوَزُهُ فَيُمْكِنُ ضَبْطُهَا وَقِيَاسُ غَيْرِهَا عَلَيْهَا.",
      "A na't of «evident», in nasb — the ism fa'il of اِنْضَبَطَ on مُنْفَعِل: having a bound it does not exceed, so that it can be pinned down and other cases measured against it. Evident and well-defined are two demands, not one: a property may be plain to see and still too loose to build on.",
      "«ظَاهِرَةً»in na'tı, mansub — «اِنْضَبَطَ»nin MÜNFAİL vezninde ism-i fâili: aşmadığı bir sınırı olan, dolayısıyla zaptedilebilen ve başkasının kendisine kıyas edilebildiği. Zâhir olmak ile munzabıt olmak iki ayrı taleptir: bir vasıf apaçık görünüp yine de üzerine bina edilemeyecek kadar gevşek olabilir."),
  tok("لَا","la-nafiya","part",["mudari-marfu","jumla-sifa"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا، وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِـ«ظَاهِرَةً» — لِأَنَّ الْمَنْعُوتَ نَكِرَةٌ.",
      "«La» simply denying, and the clause after it stands in the POSITION OF NASB as a second na't — because what it describes is an indefinite in nasb. The package has now shown a jumla sifa in raf', in jarr and in nasb: the clause never changes shape, only the noun it hangs on does.",
      "Amel etmeyen nefy «لَا»sı; sonrasındaki cümle, men'ûtu nekre olduğu için «ظَاهِرَةً»in ikinci na'tı olarak MAHALLEN MANSUBdur. Paket artık sıfat cümlesini ref'de, cerde ve nasbda göstermiştir: cümlenin şekli hiç değişmez, yalnız asıldığı isim değişir."),
  tok("تَخْتَلِفُ","ikhtalafa","verb",["mudari-marfu","form-viii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ عَلَى «اِفْتَعَلَ» مِنْ «خ ل ف»، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هِيَ».",
      "A mudari in raf' by the damma, on اِفْتَعَلَ from خ ل ف, with a hidden «she» for its fa'il — the same root that gave مُخْتَلِفَة in chapter 4, there describing meanings and here a property that must NOT do what those meanings did.",
      "«خ ل ف»den «اِفْتَعَلَ» vezninde damme ile merfû muzâri; fâili müstetir «هِيَ»dir — dördüncü bâbdaki «مُخْتَلِفَة»in kökünün aynısı; orada mânâları niteliyordu, burada ise onların yaptığını YAPMAMASI gereken bir vasfı."),
  tok("بِاخْتِلَافِ","ikhtilaf","noun",["huruf-jarr","idafa-definiteness","masdar","form-viii-verbs"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«تَخْتَلِفُ»، وَ«اخْتِلَافِ» مُضَافٌ — مَصْدَرُ الْفِعْلِ نَفْسِهِ الَّذِي تَعَلَّقَ بِهِ. وَاجْتِمَاعُ الْفِعْلِ وَمَصْدَرِهِ فِي مَوْضِعٍ وَاحِدٍ يُفِيدُ الِاسْتِقْصَاءَ: لَا تَخْتَلِفُ بِأَيِّ اخْتِلَافٍ كَانَ.",
      "A jarr-majrur attaching to «varies», and «the varying of» a mudaf — the masdar of the very verb it hangs on. A verb standing beside its own masdar in one clause is a figure of exhaustiveness: it does not vary by ANY variation whatsoever. Compare نَقْلًا مُتَوَاتِرًا in chapter 2, where the same doubling confirmed rather than exhausted.",
      "«تَخْتَلِفُ»a taalluk eden câr-mecrûr; «اخْتِلَافِ» muzâftır — asıldığı fiilin kendi masdarı. Bir fiilin kendi masdarıyla tek bir ibarede birleşmesi istiksâ ifâde eder: HERHANGİ bir değişiklikle değişmez. İkinci bâbdaki «نَقْلًا مُتَوَاتِرًا» ile karşılaştır; orada aynı ikizleme te'kîd ediyordu, burada tüketiyor.",
      segments=[seg("بِ","bi","prep"), seg("اخْتِلَافِ","ikhtilaf","noun")]),
  tok("الْأَحْوَالِ","ahwal","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «حَالٍ»، وَبِهِ خُتِمَ الْبَابُ: الْعِلَّةُ الَّتِي تَتَبَدَّلُ بِتَبَدُّلِ الْأَحْوَالِ لَا يُقَاسُ عَلَيْهَا، لِأَنَّ الْقِيَاسَ نَقْلُ حُكْمٍ، وَمَا لَا يَثْبُتُ لَا يُنْقَلُ.",
      "The mudaf ilayh in jarr — the plural of «hal», and with it the chapter closes. A cause that shifts as circumstances shift cannot be measured against, because analogy is the CARRYING of a ruling, and what will not hold still cannot be carried. The condition and the definition of qiyas in chapter 3 are one thought, twelve chapters apart.",
      "Mecrûr muzâfun ileyh — «حَال»in cemidir ve bâb onunla kapanır. Hâller değiştikçe değişen bir illete kıyas edilemez; zira kıyas bir hükmün TAŞINMASIdır ve durmayan şey taşınmaz. Şart ile üçüncü bâbdaki kıyâs tarifi, on iki bâb arayla tek bir düşüncedir.",
      punct="."),
 ],
 "jumal": [J("أَنْ تَكُونَ ظَاهِرَةً مُنْضَبِطَةً",
   "الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ «شَرْطُهَا».",
   "The masdar muawwal, in the position of raf' as the khabar of «its condition».",
   "Masdar-ı müevvel, «شَرْطُهَا»nın haberi olarak mahallen merfûdur."),
  J("لَا تَخْتَلِفُ بِاخْتِلَافِ الْأَحْوَالِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ.",
   "A verbal clause in the position of nasb, a second na't.",
   "İkinci na't olarak mahallen mansub fiil cümlesi.")]})

GLOSS_ADD = {
 "arkan":     g("أَرْكَان", "ر ك ن", "noun", "pillars — what a thing is made of (plural of رُكْن)", "rükünler", 3),
 "alladhi":   g("الَّذِي", None, "pron", "which, that (masc. relative)", "ki o (müzekker ism-i mevsûl)", 1),
 "allaqa":    g("عَلَّقَ", "ع ل ق", "verb", "to hang a thing on something", "asmak, bağlamak", 4),
 "muntabit":  g("مُنْضَبِط", "ض ب ط", "noun", "well defined — having a bound it does not exceed (ism fa'il, Form VII)", "munzabıt; sınırı belli olan", 5),
 "ikhtalafa": g("اِخْتَلَفَ", "خ ل ف", "verb", "to differ, to vary", "ihtilâf etmek, değişmek", 3),
 "ikhtilaf":  g("اِخْتِلَاف", "خ ل ف", "noun", "variation, difference (masdar, Form VIII)", "ihtilâf; değişme (masdar)", 3),
}

def build_morph():
    out = {}
    # اِخْتَلَفَ — copied after a lemma-identity check.
    s = json.loads((ROOT / "content/samples/kitab-al-sulh/morphology.json").read_text(encoding="utf-8"))
    g_ = json.loads((ROOT / "content/samples/kitab-al-sulh/glossary.json").read_text(encoding="utf-8"))
    assert g_["entries"]["ikhtalafa"]["lemma"] == GLOSS_ADD["ikhtalafa"]["lemma"]
    out["ikhtalafa"] = s["verbs"]["ikhtalafa"]
    # عَلَّقَ — Form II, sound. Its MAJHUL is the chapter's own lesson and is
    # stored, because passives are stored doctrine and not derived.
    out["allaqa"] = _sg.derived("بَابُ التَّفْعِيلِ: فَعَّلَ يُفَعِّلُ", "فَعَّلَ يُفَعِّلُ", "ُ",
                                "عَلَّق", "عَلِّق", "عَلِّق", "تَعْلِيق", "مُعَلِّق",
                                maful="مُعَلَّق", pmz="عُلِّقَ", pmd="يُعَلَّقُ",
                                note="مَجْهُولُ الْمَاضِي: ضَمُّ الْأَوَّلِ وَكَسْرُ مَا قَبْلَ الْآخِرِ — عُلِّقَ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/14.json").write_text(
    json.dumps({"chapter": 14, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 14 for c in man["chapters"]):
    man["chapters"].append({"n": 14, "title": TITLE14})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.14.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch14:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
