# -*- coding: utf-8 -*-
"""Author chapter 7 of mukhtasar-al-manar — the four ways a text SAYS something.

Chapters 5 and 6 measured the wording by how plainly it shows. This chapter
asks a different question about the same text: HOW does a ruling come out of
it? The Hanafi answer is four ways, and they are ranked — عبارة، إشارة، دلالة،
اقتضاء — from what the words were said FOR down to what has to be supplied
before they will stand up at all.

ATTRIBUTION: like chapters 2–6, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • سِيقَ — the majhul of an AJWAF WAWI. سَاقَ has an alif in the middle; the
    passive replaces it with a ya and a kasra before it, exactly as قَالَ gives
    قِيلَ and بَاعَ gives بِيعَ. Three verbs, one rule, and it cannot be read off
    the active form.
  • إِشَارَة — the Form IV masdar of an ajwaf: إِفْعَال cannot stand on a melted
    middle, so a TA MARBUTA comes in to make good the loss — the same
    compensation chapter 3 showed on تَعْدِيَة, now on a different weakness.
  • اقْتِضَاؤُهُ — the hamza takes the seat of the STRONGEST vowel in play, and a
    damma outranks everything, so it rides a waw.
  • لَا يَسْتَقِيمُ الْكَلَامُ إِلَّا بِهِ — a second istithna mufarragh, deliberately
    left to echo chapter 6's. Two chapters, one construction, different verbs.
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

TITLE7 = {"ar": "وُجُوهُ الْبَيَان", "en": "The Four Ways a Text Says a Thing",
          "tr": "Beyânın Vecihleri"}

S.append({"id": "s1", "translation": {
 "en": "Then the ways of setting forth are four: the text's plain wording, its indication, its implication and its requirement.",
 "tr": "Beyânın vecihleri dörttür: nassın ibâresi, işâreti, delâleti ve iktizâsı."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَالسُّؤَالُ هُنَا غَيْرُ سُؤَالِ الْبَابَيْنِ قَبْلَهُ: لَا كَيْفَ يَظْهَرُ اللَّفْظُ، بَلْ كَيْفَ يُسْتَخْرَجُ مِنْهُ الْحُكْمُ.",
      "A letter of atf giving sequence with an interval — and the question has changed. The two chapters before asked how plainly the wording SHOWS; this one asks how a ruling is GOT OUT of it.",
      "Terâhî ile tertîb için atıf harfi — ve soru değişmiştir. Önceki iki bâb lafzın ne kadar açık GÖRÜNDÜĞÜNÜ soruyordu; bu bâb ondan hükmün nasıl ÇIKARILDIĞINI sorar."),
  tok("وُجُوهُ","wujuh","noun",["mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ «وَجْهٍ»، وَقَدْ مَرَّ فِي الْبَابِ السَّابِقِ مُضَافًا إِلَى ضَمِيرٍ فِي «وُجُوهِهِ».",
      "The mubtada in raf' and a mudaf — the plural of «wajh», which the chapter before showed added to a pronoun in وُجُوهِهِ. Same word, same office, a different thing added to it.",
      "Merfû mübtedâ ve muzâf — «وَجْه»in cemidir; bir önceki bâbda «وُجُوهِهِ» içinde zamire muzâf olarak geçmişti. Aynı kelime, aynı vazife, muzâfun ileyhi başka."),
  tok("الْبَيَانِ","bayan","noun",["idafa-definiteness","masdar","form-ii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «بَيَّنَ»، وَالْمُرَادُ بِهِ هُنَا طَرِيقُ اسْتِخْرَاجِ الْمَعْنَى لَا مُجَرَّدُ الْإِيضَاحِ.",
      "The mudaf ilayh in jarr — the masdar of بَيَّنَ; and what is meant here is the ROUTE by which a meaning is got out, not merely making a thing clear.",
      "Mecrûr muzâfun ileyh — «بَيَّنَ»nin masdarı; burada kastedilen, sadece açıklamak değil, mânânın ÇIKARILMA YOLUdur."),
  tok("أَرْبَعَةٌ","arbaa","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — غَيْرُ مُضَافٍ، كَمَا فِي بَابِ الْوُضُوحِ لَا كَمَا فِي بَابِ الْأَقْسَامِ.",
      "The khabar in raf' with its tanwin — not a mudaf, as in the clarity chapter and unlike the divisions chapter. Three chapters now have used this one numeral in two different offices; the tanwin is the tell.",
      "Tenvînli merfû haber — vuzûh bâbındaki gibi muzâf DEĞİLDİR, aksâm bâbındaki gibi değil. Üç bâbdır bu tek sayı iki ayrı vazifede geçiyor; alâmet tenvîndir.", punct="："),
  tok("عِبَارَةُ","ibara","noun",["badal","idafa-definiteness","masdar"],
      "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «عَبَّرَ».",
      "A badal of detail, in raf' and a mudaf — the masdar of عَبَّرَ.",
      "Merfû tafsîl bedeli ve muzâf — «عَبَّرَ»nin masdarı."),
  tok("النَّصِّ","nass","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ «النَّصُّ» نَفْسُهُ الَّذِي مَرَّ فِي مَرَاتِبِ الْوُضُوحِ، مُرَادًا بِهِ هُنَا مُطْلَقُ الْكَلَامِ الْمَنْزَلِ.",
      "The mudaf ilayh in jarr — the very word that was the second rung of the clarity ladder, used here in its wider sense: the revealed wording, whatever its degree.",
      "Mecrûr muzâfun ileyh — vuzûh merdiveninin ikinci basamağı olan kelimenin aynısı; burada daha geniş mânâda kullanılmıştır: derecesi ne olursa olsun, indirilmiş lafız."),
  tok("وَإِشَارَتُهُ","ishara","noun",["atf-nasaq","idafa-definiteness","masdar","form-iv-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «أَشَارَ»، وَهُوَ أَجْوَفُ: لَمَّا أُعِلَّتْ عَيْنُهُ لَمْ يَسْتَقِمْ «إِفْعَال»، فَعُوِّضَ بِالتَّاءِ الْمَرْبُوطَةِ — كَمَا فِي «تَعْدِيَة» سَوَاءً.",
      "Joined, in raf' and a mudaf — the masdar of أَشَارَ, and the verb is HOLLOW: once the middle radical melted, إِفْعَال could not stand, so a TA MARBUTA came in to make good the loss. Exactly the compensation chapter 3 showed on تَعْدِيَة — there for a weak LAM, here for a weak AYN. One remedy, two injuries.",
      "Ma'tûf, merfû ve muzâf — «أَشَارَ»nin masdarı; fiil ECVEFtir: orta harfi i'lâl edilince «إِفْعَال» düzgün olmadı, kayıp TÂ-İ MERBÛTA ile telâfi edildi. Üçüncü bâbdaki «تَعْدِيَة» ile tam aynı: orada lâm illetliydi, burada ayn. Tek çare, iki ayrı kusur.",
      segments=[seg("وَ","wa","conj"), seg("إِشَارَتُ","ishara","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَدَلَالَتُهُ","dalala","noun",["atf-nasaq","idafa-definiteness","masdar"],
      "مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «دَلَّ»، مِنْ «د ل ل» الَّذِي جَاءَ مِنْهُ «الدَّلِيلُ» فِي أَوَّلِ الْكِتَابِ.",
      "Joined, in raf' and a mudaf — the masdar of دَلَّ, from the same root د ل ل that gave الدَّلِيل at the head of the book.",
      "Ma'tûf, merfû ve muzâf — «دَلَّ»in masdarı; kitabın başındaki «الدَّلِيل»in geldiği د ل ل kökündendir.",
      segments=[seg("وَ","wa","conj"), seg("دَلَالَتُ","dalala","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَاقْتِضَاؤُهُ","iqtida","noun",["atf-nasaq","idafa-definiteness","masdar","form-viii-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «اِقْتَضَى» عَلَى افْتِعَالٍ. وَكُتِبَتِ الْهَمْزَةُ عَلَى الْوَاوِ لِأَنَّ حَرَكَتَهَا ضَمَّةٌ، وَالضَّمَّةُ أَقْوَى الْحَرَكَاتِ.",
      "Joined, in raf' and a mudaf — the masdar of اِقْتَضَى on اِفْتِعَال. Its hamza rides a WAW because the vowel on it is a damma, and the damma outranks every other vowel when the seat is chosen. Put the same word in jarr and the seat changes: اقْتِضَائِهِ.",
      "Ma'tûf, merfû ve muzâf — «اِقْتَضَى»nin İFTİÂL vezninde masdarı. Hemze VÂV üzerine yazılmıştır; zira harekesi dammedir ve kürsü seçiminde damme bütün harekelerden kuvvetlidir. Aynı kelimeyi cere koy, kürsü değişsin: اقْتِضَائِهِ.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("اقْتِضَاؤُ","iqtida","noun"), seg("هُ","pron-3ms","pron")]),
 ],
 "jumal": [J("وُجُوهُ الْبَيَانِ أَرْبَعَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the text's plain wording is that for which the speech was uttered.",
 "tr": "Nassın ibâresi, sözün kendisi için sevk edildiği mânâdır."},
 "tokens": [
  tok("فَعِبَارَةُ","ibara","noun",["mubtada-khabar","idafa-definiteness"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«عِبَارَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "A fa joining for detail; «the wording of» is the mubtada in raf' and a mudaf.",
      "Tafsîl için âtıfa fâ; «عِبَارَةُ» merfû mübtedâ ve muzâftır.",
      segments=[seg("فَ","fa","conj"), seg("عِبَارَةُ","ibara","noun")]),
  tok("النَّصِّ","nass","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("سِيقَ","saqa","verb",["naib-al-fail","hollow-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ — وَهُوَ أَجْوَفُ وَاوِيٌّ: «سَاقَ» عَيْنُهُ وَاوٌ، فَلَمَّا بُنِيَ لِلْمَجْهُولِ كُسِرَ مَا قَبْلَ الْعَيْنِ فَانْقَلَبَتْ يَاءً — كَـ«قِيلَ» وَ«بِيعَ».",
      "A past verb built for the unnamed doer; the clause is the sila. It is an AJWAF WAWI: سَاقَ has a waw for its middle radical, and when the verb is built for the passive the letter before that middle takes a KASRA, which turns the waw into a YA. قَالَ gives قِيلَ, بَاعَ gives بِيعَ, سَاقَ gives سِيقَ — one rule, and the active form does not show it.",
      "Meçhûl sîgasında mâzî fiil; cümle sıladır. ECVEF-İ VÂVÎdir: «سَاقَ»in ayn harfi vâvdır; meçhûl bina edilince ayndan önceki harf KESRA alır ve vâv YÂya kalbolur. قَالَ'dan قِيلَ, بَاعَ'dan بِيعَ, سَاقَ'dan سِيقَ — tek kaide, ve ma'lûm sîga bunu göstermez."),
  tok("الْكَلَامُ","kalam","noun",["naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "The naib al-fa'il, in raf'.", "Merfû nâib-i fâil."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«سِيقَ»، وَالْهَاءُ عَائِدَةٌ عَلَى «مَا» — وَهَذَا الْجَارُّ هُوَ الْحَدُّ كُلُّهُ: الْمَعْنَى الَّذِي مِنْ أَجْلِهِ سِيقَ الْكَلَامُ، لَا كُلُّ مَا يُفْهَمُ مِنْهُ.",
      "A jarr-majrur attaching to «was uttered», its HA going back to «that which» — and this little phrase IS the whole definition: the sense the speech was uttered FOR, not everything that can be understood from it.",
      "«سِيقَ»ye taalluk eden câr-mecrûr; HÂ «مَا»ya râcidir — ve bu küçük câr-mecrûr tarifin kendisidir: sözün UĞRUNA sevk edildiği mânâ; ondan anlaşılabilecek her şey değil.",
      punct=".", segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
 ],
 "jumal": [J("سِيقَ الْكَلَامُ لَهُ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And its indication is what is established by the arrangement of the speech as a matter of language, without having been aimed at.",
 "tr": "İşâreti, sözün nazmıyla lugat cihetinden sâbit olan, fakat kastedilmemiş olandır."},
 "tokens": [
  tok("وَإِشَارَتُهُ","ishara","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«إِشَارَتُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A joining waw; «its indication» is the mubtada in raf' and a mudaf, with the HA as its mudaf ilayh.",
      "Atıf vâvı; «إِشَارَتُ» merfû mübtedâ ve muzâftır, HÂ muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("إِشَارَتُ","ishara","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ثَبَتَ","thabata","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ، فَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ.",
      "A past verb with a hidden pronoun for its fa'il, going back to «that which»; the clause is the sila.",
      "Mâzî fiil; fâili «مَا»ya râci müstetir zamîrdir, cümle sıladır."),
  tok("بِنَظْمِ","nazm","noun",["huruf-jarr","idafa-definiteness","masdar"],
      "الْبَاءُ لِلسَّبَبِيَّةِ، وَ«نَظْمِ» مَجْرُورٌ بِهَا وَهُوَ مُضَافٌ — وَالنَّظْمُ تَرْتِيبُ الْأَلْفَاظِ نَفْسُهُ، لَا مَعْنَاهَا.",
      "The BA of cause, and «the arrangement of» in jarr after it and a mudaf. NAZM is the ordering of the words themselves — not what they mean, which is the next definition's business.",
      "Sebebiyye bâsı; «نَظْمِ» onunla mecrûr ve muzâftır. NAZM, lafızların dizilişinin kendisidir — mânâsı değil; o, bir sonraki tarifin işidir.",
      segments=[seg("بِ","bi","prep"), seg("نَظْمِ","nazm","noun")]),
  tok("الْكَلَامِ","kalam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("لُغَةً","lugha","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ — أَيْ مِنْ جِهَةِ اللُّغَةِ، وَبِهِ خَرَجَ مَا ثَبَتَ بِالِاجْتِهَادِ.",
      "A TAMYIZ in nasb: «as a matter of LANGUAGE», and by it whatever is established by a jurist's effort is shut out. Ask «established in what respect?» and this word is the answer.",
      "Mansub TEMYÎZ: «lugat cihetinden» demektir; onunla ictihadla sâbit olan dışarıda kalır. «Hangi cihetten sâbit?» diye sor; cevap bu kelimedir."),
  tok("وَلَمْ","lam-jazim","part",["lam-jazim","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَمْ» حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ: تَجْزِمُ الْمُضَارِعَ وَتَقْلِبُ زَمَانَهُ إِلَى الْمُضِيِّ.",
      "A joining waw, and «lam» — a letter that DENIES, puts into JAZM, and TURNS THE TIME: the verb after it is a mudari in form and a past in meaning.",
      "Atıf vâvı ve «لَمْ» — nefy, cezm ve KALB harfi: kendisinden sonraki muzârii cezm eder ve zamanını mâziye çevirir.",
      segments=[seg("وَ","wa","conj"), seg("لَمْ","lam-jazim","part")]),
  tok("يَكُنْ","kana","verb",["kana-wa-akhawatuha","hollow-verbs","lam-jazim"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ — وَحُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ: «يَكُونْ» ← «يَكُنْ».",
      "A mudari of the incomplete kind, in JAZM after «lam» with a sukun for its sign, its ism a hidden pronoun. The waw is gone: يَكُونْ would put a long vowel against a sukun, and two sukuns will not stand, so the weak letter is the one that gives way. This is the hollow verb's whole story in one cell.",
      "«لَمْ» ile meczûm nâkıs muzâri, cezm alâmeti sükûndur; ismi müstetir zamîrdir. Vâv düşmüştür: «يَكُونْ» med harfini sükûnla karşılaştırır, iki sâkin ise yan yana durmaz; geri çekilen, illetli harftir. Ecvef fiilin bütün hikâyesi bu tek hânededir."),
  tok("مَقْصُودًا","maqsud","noun",["kana-wa-akhawatuha","ism-maful"],
      "خَبَرُ «يَكُنْ» مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ «قَصَدَ»، وَبِهَذَا الْقَيْدِ فَارَقَتِ الْإِشَارَةُ الْعِبَارَةَ: تِلْكَ مَا سِيقَ لَهُ، وَهَذِهِ مَا لَمْ يُسَقْ لَهُ وَثَبَتَ مَعَ ذَلِكَ.",
      "The khabar of «yakun», in nasb — the ism maf'ul of قَصَدَ, and this is the clause that parts the indication from the plain wording: the one is what the speech was said FOR, the other is what it was NOT said for and yet establishes all the same.",
      "«يَكُنْ»un mansub haberi — «قَصَدَ»nin ism-i mef'ûlü; işâreti ibâreden ayıran kayıt budur: biri sözün uğruna sevk edildiği, öteki uğruna sevk edilmediği hâlde yine de sâbit olan.",
      punct="."),
 ],
 "jumal": [J("ثَبَتَ بِنَظْمِ الْكَلَامِ لُغَةً",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("لَمْ يَكُنْ مَقْصُودًا",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ عَلَى الصِّلَةِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause joined to the sila — i'rabless.",
   "Sılaya ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And its implication is what is established by the sense of the arrangement, as a matter of language, not by a jurist's effort.",
 "tr": "Delâleti, nazmın mânâsıyla lugat cihetinden sâbit olandır — ictihadla değil."},
 "tokens": [
  tok("وَدَلَالَتُهُ","dalala","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«دَلَالَتُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A joining waw; «its implication» is the mubtada in raf' and a mudaf, with the HA as its mudaf ilayh.",
      "Atıf vâvı; «دَلَالَتُ» merfû mübtedâ ve muzâftır, HÂ muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("دَلَالَتُ","dalala","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ثَبَتَ","thabata","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — وَتَكْرَارُ «ثَبَتَ» بِعَيْنِهِ مَعَ تَبْدِيلِ الْبَاءِ وَحْدَهَا هُوَ مَوْضِعُ الْفَرْقِ.",
      "A past verb; the clause is the sila. The verb is repeated word for word from the definition before, and ONE phrase after it changes — بِنَظْمِ becomes بِمَعْنَى النَّظْمِ. That single swap is the whole distinction between an indication and an implication.",
      "Mâzî fiil; cümle sıladır. Fiil, önceki tariften harfi harfine tekrarlanır ve ardındaki TEK ibare değişir: «بِنَظْمِ» yerine «بِمَعْنَى النَّظْمِ». İşâret ile delâleti ayıran şey bu tek değişikliktir."),
  tok("بِمَعْنَى","mana","noun",["huruf-jarr","idafa-definiteness","ism-maqsur-manqus"],
      "الْبَاءُ لِلسَّبَبِيَّةِ، وَ«مَعْنَى» مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ وَهُوَ مُضَافٌ — وَلَمْ يُنَوَّنْ لِأَنَّهُ مُضَافٌ، فَاجْتَمَعَ فِيهِ الْمَقْصُورُ وَالْإِضَافَةُ.",
      "The BA of cause, and «the sense of» in jarr by a kasra ESTIMATED on the alif, and a mudaf — so it wears no tanwin, because a mudaf never does. The maqsur has now been seen three ways in this package: indefinite (مَعْنًى), definite by ال (الْمَعْنَى) and definite by idafa (مَعْنَى) — and it is written differently in each.",
      "Sebebiyye bâsı; «مَعْنَى» elif üzerinde takdîrî kesra ile mecrûr ve muzâftır — muzâf olduğu için tenvînlenmez. Bu pakette maksûr artık üç hâlde de görülmüştür: nekre (مَعْنًى), «أَلْ» ile marife (الْمَعْنَى) ve izâfetle marife (مَعْنَى) — ve her birinde başka yazılır.",
      segments=[seg("بِ","bi","prep"), seg("مَعْنَى","mana","noun")]),
  tok("النَّظْمِ","nazm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("لُغَةً","lugha","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ — أُعِيدَ لِيُبْقِيَ الْقَيْدَ قَائِمًا: الثُّبُوتُ لُغَوِيٌّ فِي الْوَجْهَيْنِ.",
      "A tamyiz in nasb, repeated to keep the restriction standing: in BOTH of these ways the thing is established by the language itself.",
      "Mansub temyîz; kaydı ayakta tutmak için tekrarlanmıştır: her iki vecihte de sübût lugavîdir."),
  tok("لَا","la-nafiya","part",["atf-nasaq"],
      "«لَا» عَاطِفَةٌ نَافِيَةٌ — تَنْفِي عَنِ الثَّانِي مَا ثَبَتَ لِلْأَوَّلِ.",
      "«La» joining and denying: it takes back from the second what was granted to the first.",
      "Nefyeden âtıfa «لَا» — birinciye sâbit olanı ikinciden nefyeder."),
  tok("بِاجْتِهَادٍ","ijtihad","noun",["huruf-jarr","masdar","form-viii-verbs"],
      "جَارٌّ وَمَجْرُورٌ مَعْطُوفٌ — مَصْدَرُ «اِجْتَهَدَ» عَلَى افْتِعَالٍ، وَمِنْهُ «الْمُجْتَهِدُونَ» فِي بَابِ الْإِجْمَاعِ.",
      "A joined jarr-majrur — the masdar of اِجْتَهَدَ on اِفْتِعَال, from the same word that gave الْمُجْتَهِدُونَ in the chapter on consensus. What a dalala yields, any competent reader of Arabic can see; it does not wait on a jurist.",
      "Ma'tûf câr-mecrûr — «اِجْتَهَدَ»nin İFTİÂL vezninde masdarı; icmâ bâbındaki «الْمُجْتَهِدُونَ» ile aynı kelimedendir. Delâletin verdiğini Arapçayı bilen herkes görür; müctehidi beklemez.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("اجْتِهَادٍ","ijtihad","noun")]),
 ],
 "jumal": [J("ثَبَتَ بِمَعْنَى النَّظْمِ لُغَةً",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And its requirement is that without which the speech will not stand.",
 "tr": "İktizâsı, kendisi olmadıkça sözün düzgün olmadığı şeydir."},
 "tokens": [
  tok("وَاقْتِضَاؤُهُ","iqtida","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«اقْتِضَاؤُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَالْهَمْزَةُ عَلَى الْوَاوِ لِلضَّمَّةِ.",
      "A joining waw; «its requirement» is the mubtada in raf' and a mudaf — the hamza riding a waw for the damma on it.",
      "Atıf vâvı; «اقْتِضَاؤُ» merfû mübtedâ ve muzâftır — hemze, üzerindeki damme sebebiyle vâv üstündedir.",
      segments=[seg("وَ","wa","conj"), seg("اقْتِضَاؤُ","iqtida","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا — وَهِيَ شَرْطُ الِاسْتِثْنَاءِ الْمُفَرَّغِ الْآتِي.",
      "«La» simply denying, and governing nothing — and it is the condition for the emptied exception coming next.",
      "Amel etmeyen nefy «لَا»sı — ve gelecek olan müferrağ istisnânın şartıdır."),
  tok("يَسْتَقِيمُ","istaqama","verb",["mudari-marfu","form-x-verbs","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ عَلَى «اسْتَفْعَلَ» — أَجْوَفُ وَاوِيٌّ مِنْ «ق و م»: قُلِبَتِ الْوَاوُ يَاءً لِانْكِسَارِ مَا قَبْلَهَا، فَصَارَ «يَسْتَقْوِمُ» ← «يَسْتَقِيمُ».",
      "A mudari in raf' by the damma, on اِسْتَفْعَلَ — an AJWAF WAWI from ق و م. The waw turned into a ya because the letter before it took a kasra: يَسْتَقْوِمُ became يَسْتَقِيمُ. Set it beside سِيقَ in this same chapter and the pair is the i'lal chapter in miniature — a waw becoming a ya, once in the passive and once under a kasra.",
      "«اِسْتَفْعَلَ» vezninde damme ile merfû muzâri — «ق و م»dan ECVEF-İ VÂVÎ: öncesi kesralandığı için vâv yâya kalbolmuş, «يَسْتَقْوِمُ» iken «يَسْتَقِيمُ» olmuştur. Aynı bâbdaki «سِيقَ» ile yan yana koy: ikisi birlikte i'lâl bâbının küçük bir hulâsasıdır — bir vâvın yâya dönüşü, bir kere meçhûlde, bir kere kesra altında."),
  tok("الْكَلَامُ","kalam","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.", "The fa'il, in raf'.", "Merfû fâil."),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ — وَهُوَ الثَّانِي فِي هَذَا الْكِتَابِ بَعْدَ «لَا يُنَالُ … إِلَّا بِالطَّلَبِ».",
      "The particle of exception, the exception MUFARRAGH — the second in this book, after لَا يُنَالُ … إِلَّا بِالطَّلَبِ. Two chapters, one construction, different verbs: that is what a construction looks like once you can see it.",
      "İstisnâ edatı; istisnâ MÜFERRAĞdır — bu kitapta «لَا يُنَالُ … إِلَّا بِالطَّلَبِ»den sonra ikincisidir. İki bâb, tek terkîb, ayrı fiiller: bir terkîbi görmeye başlamak böyle bir şeydir."),
  tok("بِهِ","bi","prep",["istithna-mufarragh","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَسْتَقِيمُ»، وَالْهَاءُ عَائِدَةٌ عَلَى «مَا» — وَهُوَ الْمُسْتَثْنَى الْمُفَرَّغُ.",
      "A jarr-majrur attaching to «will stand», its HA going back to «that which» — and it is the emptied exception itself. Drop إِلَّا and the sentence still parses: يَسْتَقِيمُ الْكَلَامُ بِهِ.",
      "«يَسْتَقِيمُ»a taalluk eden câr-mecrûr; HÂ «مَا»ya râcidir — müferrağ müstesnânın kendisidir. «إِلَّا»yı düşür, cümle yine çözülür: يَسْتَقِيمُ الْكَلَامُ بِهِ.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
 ],
 "jumal": [J("لَا يَسْتَقِيمُ الْكَلَامُ إِلَّا بِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "ibara":    g("عِبَارَة", "ع ب ر", "noun", "the plain wording — what the speech was said FOR (masdar)", "ibâre — sözün uğruna sevk edildiği (masdar)", 4),
 "ishara":   g("إِشَارَة", "ش و ر", "noun", "indication — established by the wording but not aimed at (masdar, Form IV)", "işâret — lafızdan sâbit fakat kastedilmemiş (masdar)", 4),
 "dalala":   g("دَلَالَة", "د ل ل", "noun", "implication — established by the SENSE of the wording (masdar)", "delâlet — lafzın MÂNÂSIYLA sâbit olan (masdar)", 4),
 "iqtida":   g("اقْتِضَاء", "ق ض ي", "noun", "requirement — what must be supplied for the speech to stand (masdar, Form VIII)", "iktizâ — söz düzgün olsun diye takdîr edilen (masdar)", 5),
 "kalam":    g("كَلَام", "ك ل م", "noun", "speech, an utterance", "kelâm, söz", 1),
 # كَانَ has a stored paradigm here, so it needs a glossary entry to match —
 # the validator pairs the two and says so. Kept identical to aqaid's.
 "kana":     g("كَانَ", "ك و ن", "verb", "to be (defective verb)", "olmak (nâkıs fiil)", 2),
 "saqa":     g("سَاقَ", "س و ق", "verb", "to drive, to utter (a text) for a purpose", "sevk etmek", 3),
 "thabata":  g("ثَبَتَ", "ث ب ت", "verb", "to be established, to stand firm", "sâbit olmak", 2),
 "nazm":     g("نَظْم", "ن ظ م", "noun", "the arrangement of the words themselves (masdar)", "nazım; lafızların dizilişi (masdar)", 3),
 "lugha":    g("لُغَة", "ل غ و", "noun", "language; the linguistic side of a thing", "lugat; dil ciheti", 2, plural="لُغَات"),
 "lam-jazim": g("لَمْ", None, "part", "did not (denies, puts into jazm, turns the time to the past)", "…-medi (nefy, cezm ve kalb harfi)", 2),
 "maqsud":   g("مَقْصُود", "ق ص د", "noun", "aimed at, intended (ism maf'ul)", "maksûd; kastedilen", 3),
 "ijtihad":  g("اجْتِهَاد", "ج ه د", "noun", "a jurist's reasoned effort (masdar, Form VIII)", "ictihâd (masdar)", 4),
 "istaqama": g("اِسْتَقَامَ", "ق و م", "verb", "to stand straight, to come out sound", "düzgün olmak, istikāmet üzere olmak", 4),
}

def build_morph():
    out = {}
    # كَانَ — copied; every package that has it agrees, and it is the single
    # most-shared paradigm in the library.
    s = json.loads((ROOT / "content/samples/aqaid-ahl-al-sunna/morphology.json").read_text(encoding="utf-8"))
    out["kana"] = s["verbs"]["kana"]
    # ثَبَتَ — sound, bab nasara.
    # The lam is a TA and so is the suffix, so the two run together: ثَبَتَّ,
    # never *ثَبَتْتَ. sarf_gen keeps that contraction in `idgham`, and a verb
    # whose last radical is ت ن or د needs it put through.
    out["thabata"] = _sg.idgham(_sg.sound1("nasara", "ثَبَت", "ثْبُت", "اُثْبُت", "ثُبُوت", "ثَابِت",
                                note="مِنْ بَابِ نَصَرَ — وَمَصْدَرُهُ ثُبُوتٌ، وَتَاؤُهُ تُدْغَمُ فِي تَاءِ الضَّمِيرِ."))
    # سَاقَ — AJWAF WAWI, bab nasara. Its passive is the chapter's own lesson:
    # the letter before the melted ayn takes a kasra and the waw turns to a ya.
    # Stems go in WITHOUT their sukun — every maker appends its own, and a stem
    # that already carries one ships سُقْْتَ with two.
    out["saqa"] = _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "سَاق", "سُق", "سُوق", "سُق",
                              "سُوق", "سُق", "سَوْق", "سَائِق",
                              maful="مَسُوق", pmz="سِيقَ", pmd="يُسَاقُ",
                              note="أَجْوَفُ وَاوِيٌّ: قِيلَ وَبِيعَ وَسِيقَ عَلَى قِيَاسٍ وَاحِدٍ.")
    # اِسْتَقَامَ — Form X of an ajwaf. The middle melts to an alif in the mazi
    # and comes out a ya under the kasra of the mudari: يَسْتَقِيمُ.
    out["istaqama"] = _sg.derived_hollow("بَابُ الِاسْتِفْعَالِ: اِسْتَفْعَلَ يَسْتَفْعِلُ — أَجْوَفُ",
                                          "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ",
                                          "اِسْتَقَام", "اِسْتَقَم", "سْتَقِيم", "سْتَقِم",
                                          "اِسْتَقِيم", "اِسْتَقِم",
                                          "اِسْتِقَامَة", "مُسْتَقِيم",
                                          note="أَجْوَفُ مِنَ الِاسْتِفْعَالِ: وَعُوِّضَ عَنْ عَيْنِهِ فِي الْمَصْدَرِ بِالتَّاءِ — اِسْتِقَامَةٌ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/7.json").write_text(
    json.dumps({"chapter": 7, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 7 for c in man["chapters"]):
    man["chapters"].append({"n": 7, "title": TITLE7})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.7.0"
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة الأربعة، ثم أقسام اللفظ ووجوه البيان",
                   "en": "The opening definitions, the four sources, the divisions of the wording, and the four ways a text says a thing",
                   "tr": "Açılış tarifleri, dört delil, lafzın kısımları ve beyânın vecihleri"}
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch7:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
