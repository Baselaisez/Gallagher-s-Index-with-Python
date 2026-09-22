# -*- coding: utf-8 -*-
"""Author chapter 11 of aqaid-ahl-al-sunna — the sending of the messengers.

Continues the matn where chapter 10 stopped: there is wisdom in sending the
messengers; Allah sent messengers from among men to men, bearing good news
and warning and making plain what people need of this world and of religion;
He strengthened them with miracles that break the customary; the first of the
prophets is Adam and the last is Muhammad.

Verbatim contiguous span, re-vowelled against the received text. The chapter
STOPS EARLY, before «وقد روي بيان عددهم»: the passage on their number, the
verse quoted inside it and the closing «وأفضل الأنبياء» belong together and
will be chapter 12. A span may stop early; it may never skip from the middle.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
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

TITLE11 = {"ar": "النُّبُوَّاتُ — إِرْسَالُ الرُّسُلِ",
           "en": "Prophethood — the Sending of the Messengers",
           "tr": "Nübüvvet — Resullerin Gönderilmesi"}

S.append({"id": "s1", "translation": {
 "en": "And in the sending of the messengers there is wisdom.",
 "tr": "Resullerin gönderilmesinde bir hikmet vardır."},
 "tokens": [
  tok("وَفِي","fi","prep",["huruf-jarr"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«فِي» حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "Isti'naf waw; «fi» is a jarr letter, and the phrase is a FRONTED khabar.",
      "İstinâf vâvı; «فِي» cer harfidir ve câr-mecrûr ÖNE GEÇMİŞ haberdir.",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","prep")]),
  tok("إِرْسَالِ","irsal","noun",["huruf-jarr","idafa-definiteness","form-iv-verbs","masdar"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — مَصْدَرُ «أَرْسَلَ» عَلَى وَزْنِ إِفْعَالٍ.",
      "In jarr after «fi», and a mudaf — the masdar of أَرْسَلَ on the wazn إِفْعَال.",
      "«فِي» ile mecrur ve muzâf — «أَرْسَلَ»nin if'âl vezninde masdarı."),
  tok("الرُّسُلِ","rasul","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «رَسُولٍ» عَلَى فُعُلٍ.",
      "The mudaf ilayh in jarr — the plural of رَسُول on فُعُل.",
      "Mecrûr muzâfun ileyh — «رَسُول»ün فُعُل vezninde cem'i."),
  tok("حِكْمَةٌ","hikma","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَنَكِرَتُهُ سَائِغَةٌ لِتَقَدُّمِ الْخَبَرِ عَلَيْهِ.",
      "The DELAYED mubtada in raf' — an indefinite mubtada is licensed here precisely because its khabar came first.",
      "Sonraya bırakılmış merfû mübtedâ — haberi öne geçtiği için nekire olması câizdir.", punct="."),
 ],
 "jumal": [J("وَفِي إِرْسَالِ الرُّسُلِ حِكْمَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ قُدِّمَ خَبَرُهَا — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause with its khabar fronted — i'rabless.",
   "Haberi öne geçmiş istinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And Allah has indeed sent messengers from among men to men, bearing good news and giving warning,",
 "tr": "Allah, insanlardan insanlara müjdeleyici ve uyarıcı resuller göndermiştir;"},
 "tokens": [
  tok("وَقَدْ","qad","part",["qad-harf"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«قَدْ» حَرْفُ تَحْقِيقٍ مَعَ الْمَاضِي.",
      "Isti'naf waw; «qad» before a past verb affirms that it certainly happened.",
      "İstinâf vâvı; mâzî ile «قَدْ» tahkîk harfidir.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("أَرْسَلَ","arsala","verb",["form-iv-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مِنْ بَابِ الْإِفْعَالِ، مُتَعَدٍّ بِنَفْسِهِ.",
      "Past verb on fatha — Form IV, transitive by itself.",
      "Fetha üzere mebnî mâzî — if'âl bâbından, kendisiyle müteaddîdir."),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name, the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("رُسُلًا","rasul","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — نَكِرَةٌ، وَنَكِرَتُهُ لِلتَّكْثِيرِ.",
      "The direct object in nasb — indefinite, and the indefiniteness carries plenty.",
      "Mansub mef'ûlün bih — nekiredir; nekireliği çokluk bildirir."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ، وَحُرِّكَتْ نُونُهُ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter marking the KIND; its nun took a fatha where two sakins met.",
      "Cinsi beyan için cer harfi; iki sâkin buluştuğu için nûnu fethalanmıştır."),
  tok("الْبَشَرِ","bashar","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ جَمْعٍ لَا وَاحِدَ لَهُ مِنْ لَفْظِهِ.",
      "In jarr by the kasra — a collective noun with no singular of its own shape.",
      "Kesra ile mecrur — kendi lafzından müfredi olmayan ism-i cemdir."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ.",
      "A jarr letter of end-point.",
      "Gayenin sonunu bildiren cer harfi."),
  tok("الْبَشَرِ","bashar","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ — وَتَكْرَارُهُ يُفِيدُ أَنَّ الْمُرْسَلَ وَالْمُرْسَلَ إِلَيْهِ مِنْ جِنْسٍ وَاحِدٍ.",
      "In jarr by the kasra — the repetition makes the point: sender's kind and recipient's kind are one.",
      "Kesra ile mecrur — tekrarı, gönderilenle gönderildiği kimsenin aynı cinsten olduğunu bildirir."),
  tok("مُبَشِّرِينَ","mubashshir","noun",["hal","jam-mudhakkar-salim","ism-fail","form-ii-verbs"],
      "حَالٌ مِنْ «رُسُلًا» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ — جَمْعُ مُذَكَّرٍ سَالِمٌ، اسْمُ فَاعِلٍ مِنْ «بَشَّرَ».",
      "A hal describing «messengers», in nasb by the YA — a sound masculine plural, the ism fa'il of بَشَّرَ (Form II).",
      "«رُسُلًا»dan hâl, YÂ ile mansub — cem'-i müzekker-i sâlim; «بَشَّرَ»nin ism-i fâilidir."),
  tok("وَمُنْذِرِينَ","mundhir","noun",["hal","atf-nasaq","jam-mudhakkar-salim","ism-fail","form-iv-verbs"],
      "مَعْطُوفٌ عَلَى «مُبَشِّرِينَ» مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنْ «أَنْذَرَ».",
      "Joined to «bearing good news», in nasb by the ya — the ism fa'il of أَنْذَرَ (Form IV).",
      "«مُبَشِّرِينَ»e ma'tûf, yâ ile mansub — «أَنْذَرَ»nin ism-i fâilidir.",
      segments=[seg("وَ","wa","conj"), seg("مُنْذِرِينَ","mundhir","noun")], punct="،"),
 ],
 "jumal": [J("وَقَدْ أَرْسَلَ اللهُ رُسُلًا مِنَ الْبَشَرِ إِلَى الْبَشَرِ مُبَشِّرِينَ وَمُنْذِرِينَ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf verbal clause — i'rabless.",
   "İstinâfî fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "and making plain to the people what they need of the affairs of this world and of religion.",
 "tr": "ve insanlara dünya ile din işlerinden muhtaç oldukları şeyi açıklayıcı olarak."},
 "tokens": [
  tok("وَمُبَيِّنِينَ","mubayyin","noun",["hal","atf-nasaq","jam-mudhakkar-salim","ism-fail","form-ii-verbs"],
      "مَعْطُوفٌ عَلَى «مُبَشِّرِينَ» مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنْ «بَيَّنَ»، وَهُوَ عَامِلٌ فِيمَا بَعْدَهُ.",
      "Joined to «bearing good news», in nasb by the ya — the ism fa'il of بَيَّنَ, and it GOVERNS what follows it.",
      "«مُبَشِّرِينَ»e ma'tûf, yâ ile mansub — «بَيَّنَ»nin ism-i fâili; kendinden sonrasına AMEL eder.",
      segments=[seg("وَ","wa","conj"), seg("مُبَيِّنِينَ","mubayyin","noun")]),
  tok("لِلنَّاسِ","nas","noun",["huruf-jarr"],
      "اللَّامُ حَرْفُ جَرٍّ، وَ«النَّاسِ» مَجْرُورٌ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«مُبَيِّنِينَ».",
      "The lam is a jarr letter and «the people» is in jarr after it; the phrase attaches to «making plain».",
      "Lâm cer harfi, «النَّاسِ» onunla mecrur; câr-mecrûr «مُبَيِّنِينَ»e taalluk eder.",
      segments=[seg("لِ","li","prep"), seg("النَّاسِ","nas","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«مُبَيِّنِينَ».",
      "A relative noun, fixed, in the position of nasb as the object of «making plain».",
      "İsm-i mevsûl — mebnî, «مُبَيِّنِينَ»in mef'ûlü olarak mahallen mansub."),
  tok("يَحْتَاجُونَ","ihtaja","verb",["afal-khamsa","form-viii-verbs","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَوَاوُ الْجَمَاعَةِ فَاعِلٌ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A mudari of the five verbs, in raf' by the RETAINED nun; the waw of the group is its fa'il, and the clause is the sila — i'rabless.",
      "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv-ı cemâat fâildir; cümle sıladır, mahalsizdir."),
  tok("إِلَيْهِ","ila","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَحْتَاجُونَ»، وَالْهَاءُ عَائِدُ الصِّلَةِ.",
      "A jarr phrase attaching to the verb; the ha is the pronoun that returns to the relative.",
      "«يَحْتَاجُونَ»e taalluk eden câr-mecrûr; hâ, sılanın âid zamiridir.",
      segments=[seg("إِلَيْ","ila","prep"), seg("هِ","pron-3ms","pron")]),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْبَيَانِ.",
      "A jarr letter of explication.",
      "Beyan için cer harfi."),
  tok("أُمُورِ","amr","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ — جَمْعُ «أَمْرٍ».",
      "In jarr by the kasra, and a mudaf — the plural of أَمْر.",
      "Kesra ile mecrur ve muzâf — «أَمْر»in cem'idir."),
  tok("الدُّنْيَا","dunya","noun",["idafa-definiteness","ism-maqsur-manqus","ism-tafdil"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — وَهُوَ فِي الْأَصْلِ أَفْعَلُ تَفْضِيلٍ مُؤَنَّثٌ مِنَ الدُّنُوِّ.",
      "The mudaf ilayh, in jarr by a kasra ESTIMATED on its alif — originally a feminine elative from «nearness».",
      "Mecrûr muzâfun ileyh; kesra elifi üzerinde takdîr edilir — aslen «dünüv»den müennes ism-i tafdîldir."),
  tok("وَالدِّينِ","din","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الدُّنْيَا» مَجْرُورٌ.",
      "Joined to «this world», in jarr.",
      "«الدُّنْيَا»ya ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("الدِّينِ","din","noun")], punct="."),
 ],
 "jumal": [J("وَمُبَيِّنِينَ لِلنَّاسِ مَا يَحْتَاجُونَ إِلَيْهِ",
   "مَعْطُوفٌ عَلَى الْحَالِ، وَالْحَالُ فِي مَحَلِّ نَصْبٍ.",
   "Joined to the hal, and the hal stands in the position of nasb.",
   "Hâle ma'tûftur; hâl mahallen mansubdur."),
  J("يَحْتَاجُونَ إِلَيْهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause serving as the sila — i'rabless.",
   "Mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And He strengthened them with the miracles that break what is customary.",
 "tr": "Onları, âdetleri bozan mucizelerle destekledi."},
 "tokens": [
  tok("وَأَيَّدَهُمْ","ayyada","verb",["form-ii-verbs","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَيَّدَ» فِعْلٌ مَاضٍ مِنْ بَابِ التَّفْعِيلِ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى اللهِ، وَالْهَاءُ مَفْعُولٌ بِهِ.",
      "Joining waw; «strengthened» is a Form II past verb, its fa'il hidden and returning to Allah, and the ha is the object.",
      "Atıf vâvı; «أَيَّدَ» tef'îl bâbından mâzî, fâili Allah'a dönen müstetir zamir, hâ mef'ûlün bihtir.",
      segments=[seg("وَ","wa","conj"), seg("أَيَّدَ","ayyada","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("بِالْمُعْجِزَاتِ","mujiza","noun",["huruf-jarr","jam-muannath-salim","ism-fail","form-iv-verbs"],
      "الْبَاءُ لِلِاسْتِعَانَةِ، وَ«الْمُعْجِزَاتِ» مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، اسْمُ فَاعِلٍ مِنْ «أَعْجَزَ».",
      "The ba of means; «the miracles» is in jarr by the kasra — a sound feminine plural, the ism fa'il of أَعْجَزَ.",
      "İstiâne bâsı; «الْمُعْجِزَاتِ» kesra ile mecrur — cem'-i müennes-i sâlim, «أَعْجَزَ»nin ism-i fâili.",
      segments=[seg("بِ","bi","prep"), seg("الْمُعْجِزَاتِ","mujiza","noun")]),
  tok("النَّاقِضَاتِ","naqid","noun",["naat-sifa","jam-muannath-salim","ism-fail"],
      "نَعْتٌ لِـ«الْمُعْجِزَاتِ» مَجْرُورٌ بِالْكَسْرَةِ — وَهُوَ اسْمُ فَاعِلٍ عَامِلٌ فِيمَا بَعْدَهُ.",
      "A na't of «the miracles», in jarr by the kasra — an ism fa'il that GOVERNS what follows.",
      "«الْمُعْجِزَاتِ»in na'tı, kesra ile mecrur — kendinden sonrasına amel eden ism-i fâildir."),
  tok("لِلْعَادَاتِ","ada","noun",["huruf-jarr","jam-muannath-salim"],
      "اللَّامُ حَرْفُ جَرٍّ لِلتَّقْوِيَةِ، وَ«الْعَادَاتِ» مَجْرُورٌ — وَهُوَ فِي الْمَعْنَى مَفْعُولُ «النَّاقِضَاتِ».",
      "The lam is a STRENGTHENING jarr letter; «the customs» is in jarr — and in meaning it is the object of «breaking».",
      "Lâm takviye için cer harfidir; «الْعَادَاتِ» mecrur — mana bakımından «النَّاقِضَاتِ»in mef'ûlüdür.",
      segments=[seg("لِ","li","prep"), seg("الْعَادَاتِ","ada","noun")], punct="."),
 ],
 "jumal": [J("وَأَيَّدَهُمْ بِالْمُعْجِزَاتِ النَّاقِضَاتِ لِلْعَادَاتِ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا — لَا مَحَلَّ لَهَا.",
   "A verbal clause joined to what came before — i'rabless.",
   "Öncesine ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the first of the prophets is Adam, upon him be peace.",
 "tr": "Nebîlerin ilki Âdem aleyhisselâmdır."},
 "tokens": [
  tok("وَأَوَّلُ","awwal","noun",["mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«أَوَّلُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "Isti'naf waw; «the first» is the mubtada in raf', and it is a mudaf.",
      "İstinâf vâvı; «أَوَّلُ» merfû mübtedâ ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("أَوَّلُ","awwal","noun")]),
  tok("الْأَنْبِيَاءِ","nabi","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَإِنَّمَا ظَهَرَتِ الْكَسْرَةُ مَعَ كَوْنِهِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ لِأَنَّهُ مُحَلًّى بِـ«الْ».",
      "The mudaf ilayh in jarr by the kasra — a diptote plural shape, yet the kasra SHOWS, because the article restores it.",
      "Mecrûr muzâfun ileyh, kesra ile — müntehe'l-cumû' vezninde olduğu hâlde «ال» ile muhallâ olduğu için kesrası zâhirdir."),
  tok("آدَمُ","adam","propn",["mubtada-khabar","mamnu-min-sarf"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
      "The khabar in raf' by a damma with NO tanwin — a diptote, being a proper name and foreign.",
      "Damme ile merfû haber, tenvinsiz — alemlik ve ucme sebebiyle gayr-i munsariftir."),
  tok("عَلَيْهِ","ala","prep",["huruf-jarr","jumla-mutarida"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا.",
      "A jarr phrase serving as a fronted khabar; the whole is a parenthetic prayer — i'rabless.",
      "Öne geçmiş haber olan câr-mecrûr; cümle mu'teriza duâ cümlesidir, mahalsizdir.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هِ","pron-3ms","pron")]),
  tok("السَّلَامُ","salam","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.",
      "The delayed mubtada, in raf'.",
      "Sonraya bırakılmış merfû mübtedâ.", punct="."),
 ],
 "jumal": [J("وَأَوَّلُ الْأَنْبِيَاءِ آدَمُ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir."),
  J("عَلَيْهِ السَّلَامُ",
   "جُمْلَةٌ اسْمِيَّةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ — لَا مَحَلَّ لَهَا.",
   "A parenthetic nominal clause of prayer — i'rabless.",
   "Mu'teriza duâ cümlesi — mahalsizdir.")]})

S.append({"id": "s6", "translation": {
 "en": "And the last of them is Muhammad, may Allah bless him and grant him peace.",
 "tr": "Sonuncuları ise Muhammed sallallâhu aleyhi ve sellemdir."},
 "tokens": [
  tok("وَآخِرُهُمْ","akhir","noun",["mubtada-khabar","idafa-definiteness","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«آخِرُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joining waw; «the last» is the mubtada in raf' and a mudaf; the ha is its mudaf ilayh.",
      "Atıf vâvı; «آخِرُ» merfû mübtedâ ve muzâf, hâ muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("آخِرُ","akhir","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("مُحَمَّدٌ","muhammad","propn",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The khabar in raf' by the damma.",
      "Damme ile merfû haber."),
  tok("صَلَّى","salla","verb",["jumla-mutarida","naqis-verbs","form-ii-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — نَاقِصٌ مِنْ بَابِ التَّفْعِيلِ.",
      "A past verb built on a fatha ESTIMATED on its alif — a naqis verb of Form II.",
      "Elifi üzerinde takdîr edilen fetha üzere mebnî mâzî — tef'îl bâbından nâkıstır."),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name, the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("عَلَيْهِ","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«صَلَّى».",
      "A jarr phrase attaching to «blessed».",
      "«صَلَّى»ya taalluk eden câr-mecrûr.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هِ","pron-3ms","pron")]),
  tok("وَسَلَّمَ","sallama","verb",["atf-nasaq","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«سَلَّمَ» فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى «صَلَّى»، وَالْفَاعِلُ مُسْتَتِرٌ.",
      "Joining waw; «granted peace» is a past verb joined to «blessed», its fa'il hidden.",
      "Atıf vâvı; «سَلَّمَ» «صَلَّى»ya ma'tûf mâzîdir, fâili müstetirdir.",
      segments=[seg("وَ","wa","conj"), seg("سَلَّمَ","sallama","verb")], punct="."),
 ],
 "jumal": [J("وَآخِرُهُمْ مُحَمَّدٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined nominal clause — i'rabless.",
   "Ma'tûf isim cümlesi — mahalsizdir."),
  J("صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ",
   "جُمْلَةٌ فِعْلِيَّةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ — لَا مَحَلَّ لَهَا.",
   "A parenthetic verbal clause of prayer — i'rabless.",
   "Mu'teriza duâ cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "irsal":       g("إِرْسَال", "ر س ل", "noun", "sending (masdar, Form IV)", "irsâl; gönderme (masdar)", 3),
 "hikma":       g("حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 2),
 "arsala":      g("أَرْسَلَ", "ر س ل", "verb", "to send", "göndermek", 2),
 "bashar":      g("بَشَر", "ب ش ر", "noun", "human beings, mankind", "beşer; insan", 2),
 "mubashshir":  g("مُبَشِّر", "ب ش ر", "noun", "bearer of good news", "müjdeleyici", 3),
 "mundhir":     g("مُنْذِر", "ن ذ ر", "noun", "warner", "uyarıcı; münzir", 3),
 "mubayyin":    g("مُبَيِّن", "ب ي ن", "noun", "one who makes plain", "açıklayıcı; mübeyyin", 3),
 "nas":         g("نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "ihtaja":      g("اِحْتَاجَ", "ح و ج", "verb", "to need", "muhtaç olmak", 3),
 "amr":         g("أَمْر", "أ م ر", "noun", "matter, affair", "iş; emir", 1, "أُمُور"),
 "dunya":       g("الدُّنْيَا", "د ن و", "noun", "this world, the nearer life", "dünya", 1),
 "din":         g("دِين", "د ي ن", "noun", "religion", "din", 1),
 "ayyada":      g("أَيَّدَ", "أ ي د", "verb", "to strengthen, support", "desteklemek; te'yîd etmek", 4),
 "naqid":       g("نَاقِض", "ن ق ض", "noun", "breaking, undoing (ism fa'il)", "bozan; nâkız", 4),
 "nabi":        g("نَبِيّ", "ن ب أ", "noun", "prophet", "nebî; peygamber", 2, "أَنْبِيَاء"),
 "awwal":       g("أَوَّل", "أ و ل", "noun", "first", "ilk; evvel", 1),
 "akhir":       g("آخِر", "أ خ ر", "noun", "last", "son; âhir", 1),
 "salam":       g("سَلَام", "س ل م", "noun", "peace", "selâm", 1),
 "salla":       g("صَلَّى", "ص ل و", "verb", "to bless, pray upon", "salât etmek", 3),
 "sallama":     g("سَلَّمَ", "س ل م", "verb", "to grant peace", "selâm etmek", 3),
 "pron-3mp":    g("هُمْ", None, "pron", "them (attached)", "onları/onların (muttasıl)", 1),
 "bi":          g("بِ", None, "prep", "with, by", "ile", 1),
 "li":          g("لِ", None, "prep", "for, to", "için; -e", 1),
}

def build_morph():
    fil = json.loads((ROOT / "content/samples/ashab-al-fil/morphology.json").read_text(encoding="utf-8"))["verbs"]
    samti = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json").read_text(encoding="utf-8"))["verbs"]
    out = {"arsala": fil["arsala"], "ihtaja": samti["ihtaja"]}
    # أَيَّدَ — sound Form II on أ ي د; the ya doubles, so no i'lal touches it
    out["ayyada"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "أَيَّد", "ؤَيِّد", "أَيِّد",
                                "تَأْيِيد", "مُؤَيِّد", "مُؤَيَّد")
    # سَلَّمَ — plain sound Form II
    out["sallama"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "سَلَّم", "سَلِّم", "سَلِّم",
                                 "تَسْلِيم", "مُسَلِّم", "مُسَلَّم")
    # صَلَّى — Form II of the naqis ص ل و; the lam is doubled and the final
    # weak letter behaves as every naqis Form II does (تَفْعِلَة masdar).
    out["salla"] = _sg.derived_naqis(_sg.B2 + " — نَاقِصٌ", _sg.W2, "ُ",
                                     "صَلَّ", "صَلّ", "i", "صَلّ",
                                     "تَصْلِيَة", "مُصَلٍّ", None, None, None,
                                     "نَاقِصٌ مِنَ التَّفْعِيلِ: صَلَّى يُصَلِّي — تُقَدَّرُ الْحَرَكَةُ عَلَى يَائِهِ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/11.json").write_text(json.dumps({"chapter": 11, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 11 for c in man["chapters"]):
    man["chapters"].append({"n": 11, "title": TITLE11})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.9.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch11:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
