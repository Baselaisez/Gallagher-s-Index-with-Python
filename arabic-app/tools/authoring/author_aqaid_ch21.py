# -*- coding: utf-8 -*-
"""Author chapter 21 of aqaid-ahl-al-sunna — the imam must be manifest, and of Quraysh.

Follows chapter 20's close of the imam's offices. The matn turns from what the
imam DOES to what he must BE: visible, neither hidden nor awaited; and of
Quraysh, though not confined to Banu Hashim or the children of Ali.

Grammar this chapter is chosen to teach:
  • أَنْ يَكُونَ — «an» masdariyya with a mansub mudari'. The whole clause turns
    into a MASDAR and stands as the fa'il of «يَجِبُ»: «the imam's being
    manifest is obligatory». Turkish says it with -ması/-mesi.
  • بَنِي هَاشِمٍ — the nun of a sound masculine plural dropped for the idafa,
    exactly as the Idafa engine builds it.
  • مُخْتَفِيًا — the ism fa'il of a NAQIS verb on Form VIII: مُخْتَفٍ in raf' and
    jarr, but the ya returns in nasb.

DIVERGENCE, recorded in the manifest attribution: «قُرَيْش» is read here as the
name of the ANCESTOR and so munsarif — مِنْ قُرَيْشٍ with a tanwin, the received
wording. Read instead as the name of the TRIBE it is feminine by sense and
barred from tanwin, which would give مِنْ قُرَيْشَ. Both readings are current;
the app states the disagreement rather than settling it.
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

TITLE21 = {"ar": "شُرُوطُ الْإِمَامِ", "en": "What the Imam Must Be",
           "tr": "İmâmın Şartları"}

S.append({"id": "s1", "translation": {
 "en": "Then the imam must be manifest, not hidden away and not awaited,",
 "tr": "Sonra imâmın zâhir olması vâcibdir; gizlenmiş yahut beklenen biri olması değil,"},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ مَعَ التَّرَاخِي.",
      "A letter of atf giving sequence with an interval.",
      "Terâhî ile tertîb ifade eden atıf harfi."),
  tok("يَجِبُ","wajaba","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ.",
      "A mudari' in raf', nothing governing it.",
      "Nâsıb ve câzimden hâlî olduğu için merfû muzâri fiil."),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya","mudari-marfu"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَ«أَنْ» وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ فَاعِلٍ لِـ«يَجِبُ».",
      "A masdar-making particle that puts the verb after it in NASB — and «an» with what follows is read as a MASDAR standing as the fa'il of «is obligatory»: «the imam's being manifest is obligatory».",
      "Nasb eden masdar harfi — «أَنْ» ve sonrası MASDAR te'vîlindedir ve «يَجِبُ»nün fâilidir: «imâmın zâhir OLMASI vâcibdir»."),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.",
      "A NAQIS mudari' — kana takes an ism in raf' and a khabar in nasb — put in nasb by «an», by the fatha.",
      "«أَنْ» ile fetha üzere mansub NÂKIS muzâri — kâne ismini merfû, haberini mansub kılar."),
  tok("الْإِمَامُ","imam","noun",["kana-wa-akhawatuha"],
      "اسْمُ «يَكُونَ» مَرْفُوعٌ بِالضَّمَّةِ.",
      "The ism of «yakuna», in raf' by the damma.",
      "«يَكُونَ»nin ismi, damme ile merfû."),
  tok("ظَاهِرًا","zahir","noun",["ism-fail","kana-wa-akhawatuha"],
      "خَبَرُ «يَكُونَ» مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ مِنْ «ظَهَرَ» عَلَى فَاعِلٍ.",
      "The khabar of «yakuna», in nasb by the fatha — the ism fa'il of ظَهَرَ on فَاعِل.",
      "«يَكُونَ»nin haberi, fetha ile mansub — «ظَهَرَ»nin FÂİL vezninde ism-i fâili."),
  tok("لَا","la","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلنَّفْيِ — تَنْفِي عَمَّا بَعْدَهَا مَا ثَبَتَ لِمَا قَبْلَهَا.",
      "A joining «la» of NEGATION: it denies of what comes after it what was affirmed of what came before.",
      "Nefiy için atıf «lâ»sı — öncekine sâbit olanı sonrakinden nefyeder."),
  tok("مُخْتَفِيًا","mukhtafi","noun",["ism-fail","form-viii-verbs","naqis-verbs"],
      "مَعْطُوفٌ عَلَى «ظَاهِرًا» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنَ «اخْتَفَى» عَلَى مُفْتَعِلٍ، وَهُوَ مَنْقُوصٌ: يُقَالُ «مُخْتَفٍ» رَفْعًا وَجَرًّا، وَتَعُودُ يَاؤُهُ فِي النَّصْبِ.",
      "Joined to «manifest», in nasb — the ism fa'il of اخْتَفَى on مُفْتَعِل, and a MANQUS: it is written مُخْتَفٍ in raf' and jarr, and the ya comes back in nasb.",
      "«ظَاهِرًا»ya ma'tûf, mansub — «اخْتَفَى»nın MÜFTEİL vezninde ism-i fâili ve MANKŪStur: ref' ve cerde «مُخْتَفٍ» denir, nasbda yâsı geri döner."),
  tok("وَلَا","la","part",["atf-nasaq"],
      "الْوَاوُ لِلْعَطْفِ وَ«لَا» لِتَأْكِيدِ النَّفْيِ.",
      "The waw joins and «la» strengthens the negation.",
      "Vâv atıf, «lâ» nefyi te'kîd içindir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("مُنْتَظَرًا","muntazar","noun",["ism-maful","form-viii-verbs"],
      "مَعْطُوفٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنَ «انْتَظَرَ» عَلَى مُفْتَعَلٍ، وَالْفَرْقُ بَيْنَهُ وَبَيْنَ «مُفْتَعِلٍ» فَتْحَةُ الْعَيْنِ وَكَسْرُهَا.",
      "Another ma'tuf in nasb — the ism maf'ul of انْتَظَرَ on مُفْتَعَل. What separates it from the ism fa'il مُفْتَعِل is one vowel: a fatha on the ayn instead of a kasra.",
      "Mansub ma'tûf — «انْتَظَرَ»nin MÜFTEAL vezninde ism-i mef'ûlü. Onu ism-i fâil olan MÜFTEİLden ayıran tek şey ayn harfinin fethalı yahut kesralı olmasıdır.", punct="،"),
 ],
 "jumal": [J("أَنْ يَكُونَ الْإِمَامُ ظَاهِرًا",
   "الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ» وَالْفِعْلِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ لِـ«يَجِبُ».",
   "The masdar read out of «an» + the verb stands in the position of RAF' as the fa'il of «is obligatory».",
   "«أَنْ» ve fiilden te'vîl edilen masdar, «يَجِبُ»nün fâili olarak mahallen MERFÛdur.")]})

S.append({"id": "s2", "translation": {
 "en": "and that he be of Quraysh — it is not permitted that he be of any other.",
 "tr": "ve Kureyş'ten olması; başkasından olması câiz değildir."},
 "tokens": [
  tok("وَأَنْ","an-masdariyya","part",["atf-nasaq","an-masdariyya"],
      "الْوَاوُ لِلْعَطْفِ، وَ«أَنْ» مَصْدَرِيَّةٌ نَاصِبَةٌ — وَالْمَصْدَرُ مَعْطُوفٌ عَلَى الْمَصْدَرِ الْأَوَّلِ.",
      "The waw joins; «an» is again the masdar-making particle — and this masdar is joined to the first one.",
      "Vâv atıf, «أَنْ» yine nasb eden masdar harfidir — bu masdar, evvelki masdara ma'tûftur.",
      segments=[seg("وَ","wa","conj"), seg("أَنْ","an-masdariyya","part")]),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ»، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ».",
      "A naqis mudari' in nasb after «an»; its ism is a hidden «he».",
      "«أَنْ» ile mansub nâkıs muzâri; ismi müstetir «هُوَ» zamîridir."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلتَّبْعِيضِ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ «يَكُونَ».",
      "A jarr letter of PART-OF; the phrase is the khabar of «yakuna».",
      "Teb'îz için cer harfi; câr-mecrûr «يَكُونَ»nin haberidir."),
  tok("قُرَيْشٍ","quraysh","propn",["mamnu-min-sarf","huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ» بِالْكَسْرَةِ عَلَى أَنَّهُ اسْمُ الْأَبِ فَيَنْصَرِفُ — وَمَنْ جَعَلَهُ اسْمَ الْقَبِيلَةِ مَنَعَهُ لِلتَّأْنِيثِ وَالْعَلَمِيَّةِ فَقَالَ «قُرَيْشَ».",
      "In jarr after «min» by the KASRA, read as the name of the ANCESTOR and so ordinary — but read as the name of the TRIBE it is feminine by sense and a proper name, so it is barred from tanwin and takes a fatha: «قُرَيْشَ». Both readings are current.",
      "«مِنْ» ile KESRA üzere mecrûr — CEDDİN adı sayıldığı için munsariftir. KABÎLE adı sayan ise onu te'nîs ve alemiyyet sebebiyle gayr-i munsarif kılar ve «قُرَيْشَ» der. Her iki okuyuş da mütedâveldir."),
  tok("وَلَا","la","part",["atf-nasaq"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "An isti'naf waw and a negating «la» that governs nothing.",
      "İstinâf vâvı ve amel etmeyen nefiy «lâ»sı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("يَجُوزُ","jaaza","verb",["mudari-marfu","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ وَاوِيٌّ، وَفَاعِلُهُ مَصْدَرٌ مُؤَوَّلٌ مَفْهُومٌ مِنَ السِّيَاقِ.",
      "A mudari' in raf' — a HOLLOW verb with a waw in the middle; its fa'il is a masdar understood from the run of the sentence.",
      "Merfû muzâri — vâvî ECVEFtir; fâili siyâktan anlaşılan müevvel masdardır."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ لِكَوْنٍ مَحْذُوفٍ.",
      "A jarr letter; the phrase is the khabar of an omitted «being».",
      "Cer harfi; câr-mecrûr, mahzûf bir «kevn»in haberidir."),
  tok("غَيْرِهِمْ","ghayr","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ، وَ«هِمْ» مُضَافٌ إِلَيْهِ — وَ«غَيْر» لَا تَتَعَرَّفُ بِالْإِضَافَةِ لِإِيغَالِهَا فِي الْإِبْهَامِ.",
      "In jarr after «min» and a mudaf; «him» is its mudaf ilayh — and «ghayr» never becomes definite by an idafa, however definite what follows it, because its vagueness is incurable.",
      "«مِنْ» ile mecrûr ve muzâf; «هِمْ» muzâfun ileyhtir — «غَيْر», ardındaki ne kadar marife olursa olsun izâfetle marife OLMAZ; ibhâmı köklüdür.",
      punct=".", segments=[seg("غَيْرِ","ghayr","noun"), seg("هِمْ","pron-3mp","pron")]),
 ],
 "jumal": [J("وَلَا يَجُوزُ مِنْ غَيْرِهِمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf verbal clause — i'rabless.",
   "İstinâfî fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And it is not confined to Banu Hashim and the children of Ali, may Allah be pleased with him.",
 "tr": "İmâmet, Benî Hâşim'e ve Ali'nin -Allah ondan razı olsun- evlâdına mahsus değildir."},
 "tokens": [
  tok("وَلَا","la","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ وَ«لَا» نَافِيَةٌ.",
      "A joining waw and a negating «la».",
      "Atıf vâvı ve nefiy «lâ»sı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("يُخْتَصُّ","ikhtassa","verb",["naib-al-fail","form-viii-verbs","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — مِنَ «اخْتَصَّ» عَلَى افْتِعَالٍ، وَهُوَ مُضَاعَفٌ فَأُدْغِمَ.",
      "A mudari' built for the PASSIVE, in raf' — from اخْتَصَّ on افْتِعَال, a doubled verb, so the two identical letters are merged.",
      "Meçhûl bina edilmiş merfû muzâri — «اخْتَصَّ»den, İFTİÂL vezninde; muzâaftır, iki misli harf idgām edilmiştir."),
  tok("بِبَنِي","ibn","noun",["huruf-jarr","jam-mudhakkar-salim","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«بَنِي» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ.",
      "The ba is a jarr letter; «bani» is in jarr by the YA, being annexed to the sound masculine plural — and its NUN has been dropped for the idafa. That is the rule at work: a mudaf sheds the nun exactly where it would have shed a tanwin.",
      "Bâ cer harfidir; «بَنِي» cemi müzekker sâlime mülhak olduğu için YÂ ile mecrûrdur ve NÛNu izâfet sebebiyle düşmüştür. Kaide burada gözle görülür: muzâf, tenvînini düşüreceği yerde nûnunu düşürür.",
      segments=[seg("بِ","ba","prep"), seg("بَنِي","ibn","noun")]),
  tok("هَاشِمٍ","hashim","propn",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.",
      "The mudaf ilayh in jarr by the kasra — a proper name that takes its tanwin.",
      "Kesra ile mecrûr muzâfun ileyh — munsarif alemdir."),
  tok("وَوَلَدِ","walad","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «بَنِي» مَجْرُورٌ وَهُوَ مُضَافٌ — وَ«وَلَد» يَقَعُ عَلَى الْوَاحِدِ وَالْجَمْعِ.",
      "Joined to «bani», in jarr and a mudaf — «walad» covers one child and many alike.",
      "«بَنِي»ye ma'tûf, mecrûr ve muzâf — «وَلَد» hem tekile hem cemîye şâmildir.",
      segments=[seg("وَ","wa","conj"), seg("وَلَدِ","walad","noun")]),
  tok("عَلِيٍّ","ali","propn",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.",
      "The mudaf ilayh in jarr by the kasra.",
      "Kesra ile mecrûr muzâfun ileyh.", punct="."),
 ],
 "jumal": [J("وَلَا يُخْتَصُّ بِبَنِي هَاشِمٍ وَوَلَدِ عَلِيٍّ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "wajaba":   g("وَجَبَ", "و ج ب", "verb", "to be obligatory", "vâcib olmak", 3),
 "zahir":    g("ظَاهِر", "ظ ه ر", "noun", "manifest, out in the open (ism fa'il)", "zâhir; açıkta olan", 2),
 "mukhtafi": g("مُخْتَفٍ", "خ ف ي", "noun", "hidden away (ism fa'il, Form VIII, manqus)", "gizlenmiş (ism-i fâil, mankūs)", 5),
 "muntazar": g("مُنْتَظَر", "ن ظ ر", "noun", "awaited (ism maf'ul, Form VIII)", "beklenen (ism-i mef'ûl)", 4),
 "quraysh":  g("قُرَيْش", None, "propn", "Quraysh", "Kureyş", 2),
 "jaaza":    g("جَازَ", "ج و ز", "verb", "to be permitted", "câiz olmak", 3),
 "ikhtassa": g("اخْتَصَّ", "خ ص ص", "verb", "to be confined to, be proper to", "mahsûs olmak", 4),
 "ibn":      g("ابْن", "ب ن و", "noun", "son; بَنُو = the sons of, a tribe", "oğul; بَنُو = oğulları, kabîle", 1, plural="بَنُونَ"),
 "hashim":   g("هَاشِم", None, "propn", "Hashim", "Hâşim", 2),
 "walad":    g("وَلَد", "و ل د", "noun", "child, offspring (one or many)", "evlât, çocuk (tekil ve cemi)", 1, plural="أَوْلَاد"),
 "la":       g("لَا", None, "part", "not, no", "değil, hayır", 1),
}


def build_morph():
    out = {}
    # وَجَبَ — mithal wawi on bab daraba. The waw of a mithal falls out of the
    # mudari' entirely: يَوْجِبُ → يَجِبُ, because it sits between a kasra and a
    # ya. That elision is the whole reason this verb is worth storing.
    # amr_attach appends the sukun itself, so the stem must NOT carry one.
    out["wajaba"] = _sg.sound1("daraba", "وَجَب", "جِب", "جِب", "وُجُوب", "وَاجِب",
                               maful="مَوْجُوب",
                               note="مِثَالٌ وَاوِيٌّ — حُذِفَتْ فَاؤُهُ فِي الْمُضَارِعِ لِوُقُوعِهَا بَيْنَ كَسْرَةٍ وَيَاءٍ.")
    # جَازَ — ajwaf wawi on bab nasara. Keyed «jaaza», NOT «jaza»: bad-al-amali
    # already owns that lex for the naqis جَزَى, and corpusIndex() spans every
    # package, so the two would have collided and one paradigm would have
    # silently replaced the other.
    # The imperative takes the LONG stem
    # before a vowel-initial ending (جُوزَا، جُوزُوا) and the SHORT one before a
    # sukun (جُزْ)، which is what amr_attach's two arguments are for.
    out["jaaza"] = _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "جَاز", "جُز", "جُوز", "جُز",
                              "جُوز", "جُز", "جَوَاز", "جَائِز",
                              note="أَجْوَفُ وَاوِيٌّ — عَيْنُهُ وَاوٌ، تَظْهَرُ فِي الْمُضَارِعِ وَتُقْلَبُ أَلِفًا فِي الْمَاضِي.")
    # اِخْتَصَّ — Form VIII and DOUBLED at once. The merge is not a spelling
    # choice: it holds only where the second identical letter can stay
    # vowelled, and breaks apart the moment a sukun-initial ending arrives
    # (اِخْتَصَصْتُمَا, not *اِخْتَصّْتُمَا). So both stems are given — merged
    # before vowel-initial endings, split before consonant-initial ones —
    # exactly as the package's other mudaaf verbs are stored.
    out["ikhtassa"] = _sg.entry(
        _sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِخْتِصَاص", "مُخْتَصّ",
        _sg.mazi14("اِخْتَصّ", "اِخْتَصَص"),
        _sg.mudari14("َ", "خْتَصّ", "خْتَصِص"),
        # the amr and the jazm are the ENGINE's own forms. A mudaaf verb may be
        # said either merged or broken apart (اِخْتَصَّ / اِخْتَصِصْ), and the app
        # must be able to regenerate whatever is stored — so the stored one is
        # the engine's, and the alternative lives in the note.
        ["اِخْتَصَّ", "اِخْتَصَّا", "اِخْتَصُّوا", "اِخْتَصِّي", "اِخْتَصَّا", "اِخْتَصِصْنَ"],
        "يَخْتَصَّ", "يَخْتَصَّ", "تَخْتَصَّ",
        maful="مُخْتَصّ", pmz="اُخْتُصَّ", pmd="يُخْتَصُّ",
        note="مُضَاعَفٌ مِنْ بَابِ الِافْتِعَالِ — يُدْغَمُ مَا دَامَ الثَّانِي مُتَحَرِّكًا، وَيُفَكُّ عِنْدَ اتِّصَالِ ضَمِيرٍ سَاكِنٍ. وَيَجُوزُ فِي الْأَمْرِ وَالْجَزْمِ الْفَكُّ: اِخْتَصِصْ وَلْيَخْتَصِصْ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/21.json").write_text(
    json.dumps({"chapter": 21, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 21 for c in man["chapters"]):
    man["chapters"].append({"n": 21, "title": TITLE21})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.19.0"
NOTE = ("Ch21 divergence: «قريش» is set munsarif (مِنْ قُرَيْشٍ) reading it as the "
        "ancestor's name, which is the received wording; read as the tribe's name it is "
        "barred from tanwin and would be مِنْ قُرَيْشَ. Both readings are current and the "
        "i'rab states both.")
for lang in ("en", "tr"):
    if NOTE not in man["attribution"].get(lang, ""):
        man["attribution"][lang] = man["attribution"].get(lang, "") + " " + NOTE
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
# An earlier run of this script keyed جَازَ as «jaza», which collides with
# bad-al-amali's جَزَى across corpusIndex(). Renaming a key does not remove the
# old one — these scripts only ever ADD — so the stale entry is dropped here,
# and the script stays idempotent either way.
mo["verbs"].pop("jaza", None)
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
gl["entries"].pop("jaza", None)
gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch21:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
