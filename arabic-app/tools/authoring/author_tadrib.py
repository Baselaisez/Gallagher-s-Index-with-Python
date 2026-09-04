# -*- coding: utf-8 -*-
"""Author content/samples/jumal-al-tadrib — the drill-sentence corpus.

ORIGINAL textbook-style sentences composed editorially in the question-chain
drill style the project owner teaches by («Kâtebe = yazdı, kim? Zeydun…»).
Seven chapters: the verbal sentence, the nominal sentence, inne-vs-enne
(the hamza rule, with the qawl exception), the objects family, condition and
question, the two governing families with tamyiz and istithna, and the vocative. Every token carries full
trilingual i'rab, so the whole package doubles as TRAINING DATA for the
runtime IrabModel — each sentence here is a labeled example the naive Bayes
learns from, which is the package's second job.

FREE access: the drill garden belongs to the Lite tier.
Paradigms: copied where the corpus owns the verb (lemma identity), engine-
built for kataba / qara'a / shahida.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PKG = ROOT / "content/samples/jumal-al-tadrib"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import sarf_gen as _sg

DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)

def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)},
         "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t

def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}

# ---- the recurring i'rab lines, written once so every drill teaches the
# same wording the madrasah recites (and RoleEngine reads them uniformly)
def MADI(lex, full, extra_g=None, **kw):
    return tok(full, lex, "verb", ["thulathi-mujarrad-babs"] + (extra_g or []),
        "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
        "Past verb, built on fatha.",
        "Fetha üzere mebnî mâzî fiil.", **kw)
def FAIL(lex, full, note_ar="", note_en="", note_tr="", **kw):
    return tok(full, lex, "noun", ["fail"],
        "فَاعِلٌ مَرْفُوعٌ." + note_ar,
        "The fa'il, in raf'." + note_en,
        "Merfû fâil." + note_tr, **kw)
def MAFUL(lex, full, **kw):
    return tok(full, lex, "noun", ["maful-bihi"],
        "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
        "Direct object, in nasb.",
        "Mensub mef'ûlün bih.", **kw)
def MUBT(lex, full, **kw):
    return tok(full, lex, "noun", ["mubtada-khabar"],
        "مُبْتَدَأٌ مَرْفُوعٌ.",
        "Mubtada in raf'.",
        "Merfû mübteda.", **kw)
def KHAB(lex, full, extra_g=None, **kw):
    return tok(full, lex, "noun", ["mubtada-khabar"] + (extra_g or []),
        "خَبَرٌ مَرْفُوعٌ.",
        "Khabar in raf'.",
        "Merfû haber.", **kw)
def PREP(lex, full, **kw):
    return tok(full, lex, "prep", ["huruf-jarr"],
        "حَرْفُ جَرٍّ.",
        "A jarr letter.",
        "Cer harfi.", **kw)
def MAJR(lex, full, seg_extra=None, **kw):
    return tok(full, lex, "noun", ["huruf-jarr"],
        "مَجْرُورٌ بِحَرْفِ الْجَرِّ.",
        "In jarr after the preposition.",
        "Cer harfiyle mecrurdur.", segments=seg_extra, **kw)

S1, S2, S3 = [], [], []

# ============ Chapter 1 — the verbal sentence ============
S1.append({"id": "s1", "translation": {
 "en": "Zayd wrote a letter.", "tr": "Zeyd bir mektup yazdı."},
 "tokens": [
  MADI("kataba", "كَتَبَ"),
  FAIL("zayd", "زَيْدٌ"),
  MAFUL("risala", "رِسَالَةً", punct="."),
 ],
 "jumal": [J("كَتَبَ زَيْدٌ رِسَالَةً",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s2", "translation": {
 "en": "The student read the book.", "tr": "Öğrenci kitabı okudu."},
 "tokens": [
  MADI("qaraa", "قَرَأَ"),
  FAIL("talib", "الطَّالِبُ"),
  MAFUL("kitab", "الْكِتَابَ", punct="."),
 ],
 "jumal": [J("قَرَأَ الطَّالِبُ الْكِتَابَ",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s3", "translation": {
 "en": "The teacher entered the mosque.", "tr": "Muallim mescide girdi."},
 "tokens": [
  MADI("dakhala", "دَخَلَ"),
  FAIL("muallim", "الْمُعَلِّمُ"),
  MAFUL("masjid", "الْمَسْجِدَ", punct="."),
 ],
 "jumal": [J("دَخَلَ الْمُعَلِّمُ الْمَسْجِدَ",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s4", "translation": {
 "en": "Zayd came riding.", "tr": "Zeyd binerek (binmiş hâlde) geldi."},
 "tokens": [
  tok("جَاءَ","jaa","verb",["thulathi-mujarrad-babs","hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ مَهْمُوزٌ.",
      "Past verb built on fatha — hollow with a hamza.",
      "Fetha üzere mebnî mâzî fiil — ecvef ve mehmûzdur."),
  FAIL("zayd", "زَيْدٌ"),
  tok("رَاكِبًا","rakib","noun",["hal","ism-fail"],
      "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «رَكِبَ».",
      "A hal in nasb — the ism fa'il of رَكِبَ: in what state? riding.",
      "Mensub hâl — «رَكِبَ» fiilinin ism-i fâili: ne hâlde? binmiş hâlde.", punct="."),
 ],
 "jumal": [J("جَاءَ زَيْدٌ رَاكِبًا",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s5", "translation": {
 "en": "The boy returned to the house.", "tr": "Çocuk eve döndü."},
 "tokens": [
  MADI("rajaa", "رَجَعَ"),
  FAIL("walad", "الْوَلَدُ"),
  PREP("ila", "إِلَى"),
  MAJR("bayt", "الْبَيْتِ", punct="."),
 ],
 "jumal": [J("رَجَعَ الْوَلَدُ إِلَى الْبَيْتِ",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s6", "translation": {
 "en": "The student heard the lesson in the mosque.", "tr": "Öğrenci dersi mescitte dinledi."},
 "tokens": [
  MADI("samia", "سَمِعَ"),
  FAIL("talib", "الطَّالِبُ"),
  MAFUL("dars", "الدَّرْسَ"),
  PREP("fi", "فِي"),
  MAJR("masjid", "الْمَسْجِدِ", punct="."),
 ],
 "jumal": [J("سَمِعَ الطَّالِبُ الدَّرْسَ فِي الْمَسْجِدِ",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s7", "translation": {
 "en": "Zayd did not write a letter.", "tr": "Zeyd bir mektup yazmadı."},
 "tokens": [
  tok("لَمْ","lam-jazima","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "The particle of negation, jazm and time-flip: it turns the mudari's meaning to the past.",
      "Nefiy, cezm ve kalb harfi: muzârinin manasını mâzîye çevirir."),
  tok("يَكْتُبْ","kataba","verb",["lam-jazim","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ»، وَعَلَامَةُ جَزْمِهِ السُّكُونُ.",
      "Mudari in jazm after لَمْ; its sign is the sukun.",
      "«لَمْ» ile meczum muzâri; cezm alâmeti sükûndur."),
  FAIL("zayd", "زَيْدٌ"),
  MAFUL("risala", "رِسَالَةً", punct="."),
 ],
 "jumal": [J("لَمْ يَكْتُبْ زَيْدٌ رِسَالَةً",
   "جُمْلَةٌ فِعْلِيَّةٌ مَنْفِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening negated verbal clause — i'rabless.",
   "İbtidâiyye menfî fiil cümlesi — mahalsizdir.")]})

S1.append({"id": "s8", "translation": {
 "en": "The students left the lesson glad.", "tr": "Öğrenciler dersten sevinçli çıktılar."},
 "tokens": [
  MADI("kharaja", "خَرَجَ"),
  tok("الطُّلَّابُ","tullab","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — جَمْعُ تَكْسِيرٍ لِـ«طَالِب».",
      "The fa'il in raf' — a broken plural of طَالِب.",
      "Merfû fâil — «طَالِب» kelimesinin cem'-i mükesseri."),
  PREP("min", "مِنَ"),
  MAJR("dars", "الدَّرْسِ"),
  tok("فَرِحِينَ","farih","noun",["hal","jam-mudhakkar-salim"],
      "حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ — جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "A hal in nasb, its sign the ya — a sound masculine plural.",
      "Mensub hâl; nasb alâmeti yâdır — cem'-i müzekker-i sâlim.", punct="."),
 ],
 "jumal": [J("خَرَجَ الطُّلَّابُ مِنَ الدَّرْسِ فَرِحِينَ",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

# ============ Chapter 2 — the nominal sentence ============
S2.append({"id": "s1", "translation": {
 "en": "Knowledge is light.", "tr": "İlim nurdur."},
 "tokens": [MUBT("ilm", "الْعِلْمُ"), KHAB("nur", "نُورٌ", punct=".")],
 "jumal": [J("الْعِلْمُ نُورٌ",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s2", "translation": {
 "en": "The book is new.", "tr": "Kitap yenidir."},
 "tokens": [MUBT("kitab", "الْكِتَابُ"), KHAB("jadid", "جَدِيدٌ", punct=".")],
 "jumal": [J("الْكِتَابُ جَدِيدٌ",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s3", "translation": {
 "en": "Zayd's book is new.", "tr": "Zeyd'in kitabı yenidir."},
 "tokens": [
  tok("كِتَابُ","kitab","noun",["mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "Mubtada in raf', itself a mudaf.",
      "Merfû mübteda ve muzâftır."),
  tok("زَيْدٍ","zayd","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir."),
  KHAB("jadid", "جَدِيدٌ", punct="."),
 ],
 "jumal": [J("كِتَابُ زَيْدٍ جَدِيدٌ",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s4", "translation": {
 "en": "The diligent student is beloved.", "tr": "Çalışkan öğrenci sevilendir."},
 "tokens": [
  MUBT("talib", "الطَّالِبُ"),
  tok("الْمُجْتَهِدُ","mujtahid","noun",["naat-sifa","ism-fail","form-viii-verbs"],
      "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ «اجْتَهَدَ».",
      "Na't in raf' — the ism fa'il of اجْتَهَدَ (Form VIII).",
      "Merfû na't — «اجْتَهَدَ» (iftiâl) fiilinin ism-i fâili."),
  tok("مَحْبُوبٌ","mahbub","noun",["mubtada-khabar","ism-maful"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «حَبَّ».",
      "Khabar in raf' — an ism maf'ul.",
      "Merfû haber — ism-i mef'ûldür.", punct="."),
 ],
 "jumal": [J("الطَّالِبُ الْمُجْتَهِدُ مَحْبُوبٌ",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s5", "translation": {
 "en": "In the house there is a man.", "tr": "Evde bir adam vardır."},
 "tokens": [
  tok("فِي","fi","prep",["huruf-jarr","mubtada-khabar"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "Jarr letter; the phrase is a fronted khabar.",
      "Cer harfi; câr-mecrûr öne geçmiş haberdir."),
  tok("الْبَيْتِ","bayt","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "In jarr after فِي.",
      "«فِي» ile mecrurdur."),
  tok("رَجُلٌ","rajul","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.",
      "The delayed mubtada, in raf'.",
      "Sonraya bırakılmış merfû mübteda (mübteda-i muahhar).", punct="."),
 ],
 "jumal": [J("فِي الْبَيْتِ رَجُلٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مِنْ خَبَرٍ مُقَدَّمٍ وَمُبْتَدَإٍ مُؤَخَّرٍ — لَا مَحَلَّ لَهَا.",
   "A nominal clause of fronted khabar and delayed mubtada — i'rabless.",
   "Haber-i mukaddem ile mübteda-i muahhardan kurulu isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s6", "translation": {
 "en": "The mosque is the house of Allah.", "tr": "Mescid, Allah'ın evidir."},
 "tokens": [
  MUBT("masjid", "الْمَسْجِدُ"),
  tok("بَيْتُ","bayt","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "Khabar in raf', itself a mudaf.",
      "Merfû haber ve muzâftır."),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The majestic name — mudaf ilayh in jarr.",
      "Lafza-i celâl — mecrûr muzâfun ileyhtir.", punct="."),
 ],
 "jumal": [J("الْمَسْجِدُ بَيْتُ اللهِ",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s7", "translation": {
 "en": "Truly knowledge is beneficial.", "tr": "Şüphesiz ilim faydalıdır."},
 "tokens": [
  tok("إِنَّ","inna","part",["inna-wa-akhawatuha","inna-am-anna"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، كُسِرَتْ هَمْزَتُهُ لِوُقُوعِهِ فِي صَدْرِ الْكَلَامِ.",
      "The particle of emphasis and nasb; its hamza takes kasra because it opens the speech.",
      "Te'kid ve nasb harfi; söz başında geldiği için hemzesi kesralıdır."),
  tok("الْعِلْمَ","ilm","noun",["inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The ism of إِنَّ, in nasb.",
      "«إِنَّ»nin mensub ismidir."),
  tok("نَافِعٌ","nafi","noun",["inna-wa-akhawatuha","ism-fail"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ — اسْمُ فَاعِلٍ.",
      "The khabar of إِنَّ in raf' — an ism fa'il.",
      "«إِنَّ»nin merfû haberi — ism-i fâildir.", punct="."),
 ],
 "jumal": [J("إِنَّ الْعِلْمَ نَافِعٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مُؤَكَّدَةٌ بِـ«إِنَّ» — لَا مَحَلَّ لَهَا.",
   "A nominal clause emphasized by إِنَّ — i'rabless.",
   "«إِنَّ» ile te'kid edilmiş isim cümlesi — mahalsizdir.")]})

S2.append({"id": "s8", "translation": {
 "en": "The lesson is not difficult.", "tr": "Ders zor değildir."},
 "tokens": [
  tok("لَيْسَ","laysa","verb",["kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ».",
      "Defective past verb of the kana family.",
      "Kâne'nin kardeşlerinden nâkıs fiil."),
  tok("الدَّرْسُ","dars","noun",["kana-wa-akhawatuha"],
      "اسْمُ «لَيْسَ» مَرْفُوعٌ.",
      "The ism of لَيْسَ, in raf'.",
      "«لَيْسَ»nin merfû ismidir."),
  tok("صَعْبًا","sab","noun",["kana-wa-akhawatuha"],
      "خَبَرُ «لَيْسَ» مَنْصُوبٌ.",
      "The khabar of لَيْسَ, in nasb.",
      "«لَيْسَ»nin mensub haberidir.", punct="."),
 ],
 "jumal": [J("لَيْسَ الدَّرْسُ صَعْبًا",
   "جُمْلَةٌ فِعْلِيَّةٌ مَنْسُوخَةٌ بِـ«لَيْسَ» — لَا مَحَلَّ لَهَا.",
   "A clause governed by لَيْسَ — i'rabless.",
   "«لَيْسَ» ile mensuh cümle — mahalsizdir.")]})

# ============ Chapter 3 — inne or enne? ============
def INNA_KASR(why_ar, why_en, why_tr):
    return tok("إِنَّ","inna","part",["inna-wa-akhawatuha","inna-am-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، كُسِرَتْ هَمْزَتُهُ " + why_ar,
        "Particle of emphasis and nasb; the hamza takes KASRA " + why_en,
        "Te'kid ve nasb harfi; hemzesi KESRALIDIR — " + why_tr)
def ANNA_FATH(why_ar, why_en, why_tr):
    return tok("أَنَّ","anna","part",["inna-wa-akhawatuha","inna-am-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، فُتِحَتْ هَمْزَتُهُ " + why_ar,
        "Particle of emphasis and nasb; the hamza takes FATHA " + why_en,
        "Te'kid ve nasb harfi; hemzesi FETHALIDIR — " + why_tr)

# the tail names its OWN governing particle — s1's clause follows قَالَ so
# its particle is إِنَّ, s2's follows عَلِمْتُ so it is أَنَّ; a shared
# string here once mislabeled s2's khabar (caught by the pre-ship review).
def QADIR_TAIL(ptcl):
    return [
      tok("قَادِرٌ","qadir","noun",["inna-wa-akhawatuha","ism-fail"],
          f"خَبَرُ «{ptcl}» مَرْفُوعٌ — اسْمُ فَاعِلٍ.",
          f"The khabar of {ptcl} in raf' — an ism fa'il: able.",
          f"«{ptcl}»nin merfû haberi — ism-i fâil: kâdir."),
      PREP("ala", "عَلَى"),
      tok("كُلِّ","kull","noun",["huruf-jarr","idafa-definiteness"],
          "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ.",
          "In jarr after عَلَى, itself a mudaf.",
          "«عَلَى» ile mecrur ve muzâftır."),
      tok("شَيْءٍ","shay","noun",["idafa-definiteness"],
          "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
          "Mudaf ilayh in jarr.",
          "Mecrûr muzâfun ileyhtir.", punct="."),
    ]

S3.append({"id": "s1", "translation": {
 "en": "Zayd said: truly Allah is able over everything.",
 "tr": "Zeyd, Allah'ın her şeye kâdir olduğunu söyledi (Allah her şeye kâdirdir, dedi)."},
 "tokens": [
  MADI("qala", "قَالَ", extra_g=["hollow-verbs"]),
  FAIL("zayd", "زَيْدٌ"),
  INNA_KASR("لِوُقُوعِهِ بَعْدَ الْقَوْلِ — فَالْمَقُولُ يُحْكَى كَمَا هُوَ.",
            "— it stands after قَالَ: the saying is quoted whole, not melted into a masdar.",
            "«قَالَ»den sonra geldiği için; söz olduğu gibi nakledilir, masdara erimez."),
  tok("اللهَ","allah","noun",["inna-wa-akhawatuha"],
      "لَفْظُ الْجَلَالَةِ اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The majestic name — the ism of إِنَّ, in nasb.",
      "Lafza-i celâl — «إِنَّ»nin mensub ismidir."),
 ] + QADIR_TAIL("إِنَّ"),
 "jumal": [
  J("قَالَ زَيْدٌ...",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
    "An opening verbal clause — i'rabless.",
    "İbtidâiyye fiil cümlesi — mahalsizdir."),
  J("إِنَّ اللهَ قَادِرٌ عَلَى كُلِّ شَيْءٍ",
    "جُمْلَةٌ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "The quoted speech — in nasb position as the maqul al-qawl.",
    "Makûlü'l-kavl — mahallen mensubdur.")]})

S3.append({"id": "s2", "translation": {
 "en": "I knew that Allah is able over everything.",
 "tr": "Allah'ın her şeye kâdir olduğunu bildim."},
 "tokens": [
  tok("عَلِمْتُ","alima","verb",["thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "Past verb; the attached ت is its fa'il.",
      "Mâzî fiil; bitişik tâ zamiri mahallen merfû fâildir.",
      segments=[seg("عَلِمْ","alima","verb"), seg("تُ","pron-1s","pron")]),
  ANNA_FATH("لِأَنَّ مَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ (= عَلِمْتُ قُدْرَةَ اللهِ).",
            "— the clause melts into a masdar (= I knew Allah's ABILITY).",
            "çünkü sonrası masdar hükmündedir (= Allah'ın kudretini bildim: -dığını)."),
  tok("اللهَ","allah","noun",["inna-wa-akhawatuha"],
      "لَفْظُ الْجَلَالَةِ اسْمُ «أَنَّ» مَنْصُوبٌ.",
      "The majestic name — the ism of أَنَّ, in nasb.",
      "Lafza-i celâl — «أَنَّ»nin mensub ismidir."),
 ] + QADIR_TAIL("أَنَّ"),
 "jumal": [
  J("عَلِمْتُ...",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
    "An opening verbal clause — i'rabless.",
    "İbtidâiyye fiil cümlesi — mahalsizdir."),
  J("أَنَّ اللهَ قَادِرٌ عَلَى كُلِّ شَيْءٍ",
    "الْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ «عَلِمَ».",
    "The construed masdar stands in for the objects of عَلِمَ.",
    "Müevvel masdar, «عَلِمَ»nin mef'ûllerinin yerini tutar.")]})

S3.append({"id": "s3", "translation": {
 "en": "I heard that the teacher is ill.", "tr": "Muallimin hasta olduğunu işittim."},
 "tokens": [
  tok("سَمِعْتُ","samia","verb",["thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "Past verb; the attached ت is its fa'il.",
      "Mâzî fiil; bitişik tâ zamiri mahallen merfû fâildir.",
      segments=[seg("سَمِعْ","samia","verb"), seg("تُ","pron-1s","pron")]),
  ANNA_FATH("لِأَنَّ مَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ (= سَمِعْتُ مَرَضَهُ).",
            "— the clause melts into a masdar (= I heard of his ILLNESS).",
            "çünkü sonrası masdar hükmündedir (hasta olduğunu: -dığını)."),
  tok("الْمُعَلِّمَ","muallim","noun",["inna-wa-akhawatuha"],
      "اسْمُ «أَنَّ» مَنْصُوبٌ.",
      "The ism of أَنَّ, in nasb.",
      "«أَنَّ»nin mensub ismidir."),
  tok("مَرِيضٌ","marid","noun",["inna-wa-akhawatuha","sifa-mushabbaha"],
      "خَبَرُ «أَنَّ» مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ.",
      "The khabar in raf' — a sifa mushabbaha.",
      "Merfû haberi — sıfat-ı müşebbehedir.", punct="."),
 ],
 "jumal": [J("أَنَّ الْمُعَلِّمَ مَرِيضٌ",
   "الْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ «سَمِعَ».",
   "The construed masdar is the object of سَمِعَ.",
   "Müevvel masdar, «سَمِعَ»nin mef'ûlüdür.")]})

S3.append({"id": "s4", "translation": {
 "en": "Truly the lesson is easy.", "tr": "Şüphesiz ders kolaydır."},
 "tokens": [
  INNA_KASR("لِوُقُوعِهِ فِي صَدْرِ الْكَلَامِ.",
            "— it opens the speech; nothing before it could absorb a masdar.",
            "söz başında geldiği için."),
  tok("الدَّرْسَ","dars","noun",["inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The ism of إِنَّ, in nasb.",
      "«إِنَّ»nin mensub ismidir."),
  tok("سَهْلٌ","sahl","noun",["inna-wa-akhawatuha"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ.",
      "The khabar of إِنَّ, in raf'.",
      "«إِنَّ»nin merfû haberidir.", punct="."),
 ],
 "jumal": [J("إِنَّ الدَّرْسَ سَهْلٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مُؤَكَّدَةٌ — لَا مَحَلَّ لَهَا.",
   "An emphasized nominal clause — i'rabless.",
   "Te'kidli isim cümlesi — mahalsizdir.")]})

S3.append({"id": "s5", "translation": {
 "en": "The girl said: truly the book is new.", "tr": "Kız, kitap yenidir, dedi."},
 "tokens": [
  tok("قَالَتِ","qala","verb",["thulathi-mujarrad-babs","hollow-verbs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "Past verb; the ت marks the feminine, vowelled kasra to break the two sukuns.",
      "Mâzî fiil; tâ te'nis içindir, iki sâkin karşılaştığı için kesralanmıştır."),
  FAIL("bint", "الْبِنْتُ"),
  INNA_KASR("لِوُقُوعِهِ بَعْدَ الْقَوْلِ.",
            "— it stands after a qawl verb.",
            "kavil fiilinden sonra geldiği için."),
  tok("الْكِتَابَ","kitab","noun",["inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The ism of إِنَّ, in nasb.",
      "«إِنَّ»nin mensub ismidir."),
  tok("جَدِيدٌ","jadid","noun",["inna-wa-akhawatuha"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ.",
      "The khabar of إِنَّ, in raf'.",
      "«إِنَّ»nin merfû haberidir.", punct="."),
 ],
 "jumal": [J("إِنَّ الْكِتَابَ جَدِيدٌ",
   "جُمْلَةٌ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
   "In nasb position — the maqul al-qawl.",
   "Makûlü'l-kavl — mahallen mensubdur.")]})

S3.append({"id": "s6", "translation": {
 "en": "By Allah, truly knowledge is beneficial.", "tr": "Vallahi, ilim elbette faydalıdır."},
 "tokens": [
  tok("وَاللهِ","allah","noun",["huruf-jarr","anwa-al-waw"],
      "الْوَاوُ لِلْقَسَمِ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِهَا.",
      "The oath waw — a jarr letter; the majestic name in jarr after it.",
      "Kasem vâvı — cer harfidir; lafza-i celâl onunla mecrurdur.",
      segments=[seg("وَ","wa","part"), seg("اللهِ","allah","noun")]),
  INNA_KASR("لِوُقُوعِهِ بَعْدَ الْقَسَمِ.",
            "— it stands after the oath.",
            "kasemden sonra geldiği için."),
  tok("الْعِلْمَ","ilm","noun",["inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The ism of إِنَّ, in nasb.",
      "«إِنَّ»nin mensub ismidir."),
  tok("نَافِعٌ","nafi","noun",["inna-wa-akhawatuha","ism-fail"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ.",
      "The khabar of إِنَّ, in raf'.",
      "«إِنَّ»nin merfû haberidir.", punct="."),
 ],
 "jumal": [J("وَاللهِ إِنَّ الْعِلْمَ نَافِعٌ",
   "جُمْلَةُ جَوَابِ الْقَسَمِ — لَا مَحَلَّ لَهَا.",
   "The oath's answer clause — i'rabless.",
   "Kasemin cevap cümlesi — mahalsizdir.")]})

S3.append({"id": "s7", "translation": {
 "en": "I bear witness that Muhammad is the Messenger of Allah.",
 "tr": "Muhammed'in Allah'ın Rasûlü olduğuna şehadet ederim."},
 "tokens": [
  tok("أَشْهَدُ","shahida","verb",["mudari-marfu","thulathi-mujarrad-babs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنَا.",
      "Mudari in raf'; its fa'il is a hidden أَنَا.",
      "Merfû muzâri; fâili gizli «أَنَا» zamiridir."),
  ANNA_FATH("لِأَنَّ مَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ (= أَشْهَدُ بِرِسَالَتِهِ).",
            "— the clause melts into a masdar (= I witness his MESSENGERSHIP).",
            "çünkü sonrası masdar hükmündedir (Rasûl olduğuna: -dığına)."),
  tok("مُحَمَّدًا","muhammad","noun",["inna-wa-akhawatuha"],
      "اسْمُ «أَنَّ» مَنْصُوبٌ.",
      "The ism of أَنَّ, in nasb.",
      "«أَنَّ»nin mensub ismidir."),
  tok("رَسُولُ","rasul","noun",["inna-wa-akhawatuha","idafa-definiteness"],
      "خَبَرُ «أَنَّ» مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "The khabar in raf', itself a mudaf.",
      "«أَنَّ»nin merfû haberi ve muzâftır."),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The majestic name — mudaf ilayh in jarr.",
      "Lafza-i celâl — mecrûr muzâfun ileyhtir.", punct="."),
 ],
 "jumal": [J("أَنَّ مُحَمَّدًا رَسُولُ اللهِ",
   "الْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ «أَشْهَدُ».",
   "The construed masdar is the object of أَشْهَدُ.",
   "Müevvel masdar, «أَشْهَدُ»nün mef'ûlüdür.")]})

S3.append({"id": "s8", "translation": {
 "en": "Zayd did not say that the lesson is difficult.",
 "tr": "Zeyd, ders zordur, demedi."},
 "tokens": [
  tok("لَمْ","lam-jazima","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "The particle of negation, jazm and time-flip.",
      "Nefiy, cezm ve kalb harfi."),
  tok("يَقُلْ","qala","verb",["lam-jazim","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — قَالَ يَقُولُ.",
      "Mudari in jazm; the hollow middle dropped where two sukuns met — قَالَ يَقُولُ.",
      "Meczum muzâri; iki sâkin karşılaşınca ecvefin ortası düşmüştür — قَالَ يَقُولُ."),
  FAIL("zayd", "زَيْدٌ"),
  INNA_KASR("لِوُقُوعِهِ بَعْدَ الْقَوْلِ وَلَوْ مَنْفِيًّا.",
            "— after a qawl verb, even a negated one.",
            "kavil fiilinden sonra geldiği için — fiil menfî olsa da."),
  tok("الدَّرْسَ","dars","noun",["inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The ism of إِنَّ, in nasb.",
      "«إِنَّ»nin mensub ismidir."),
  tok("صَعْبٌ","sab","noun",["inna-wa-akhawatuha"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ.",
      "The khabar of إِنَّ, in raf'.",
      "«إِنَّ»nin merfû haberidir.", punct="."),
 ],
 "jumal": [J("إِنَّ الدَّرْسَ صَعْبٌ",
   "جُمْلَةٌ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
   "In nasb position — the maqul al-qawl.",
   "Makûlü'l-kavl — mahallen mensubdur.")]})

# ---- titles ---------------------------------------------------------------
S4, S5 = [], []

# ============ Chapter 4 — the objects family and the deputy ============
S4.append({"id": "s1", "translation": {
 "en": "The student memorized the Qur'an thoroughly.", "tr": "Öğrenci Kur'ân'ı sağlam bir ezberle ezberledi."},
 "tokens": [
  MADI("hafiza", "حَفِظَ"),
  FAIL("talib", "الطَّالِبُ"),
  MAFUL("quran", "الْقُرْآنَ"),
  tok("حِفْظًا","hifz","noun",["maful-mutlaq","masdar"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرٌ يُؤَكِّدُ فِعْلَهُ.",
      "Absolute object in nasb — the verb's own masdar, emphasizing it.",
      "Mensub mef'ûl-i mutlak — fiilini te'kid eden masdardır.", punct="."),
 ],
 "jumal": [J("حَفِظَ الطَّالِبُ الْقُرْآنَ حِفْظًا",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S4.append({"id": "s2", "translation": {
 "en": "The boy sat in the mosque in the morning.", "tr": "Çocuk sabahleyin mescitte oturdu."},
 "tokens": [
  MADI("jalasa", "جَلَسَ"),
  FAIL("walad", "الْوَلَدُ"),
  PREP("fi", "فِي"),
  MAJR("masjid", "الْمَسْجِدِ"),
  tok("صَبَاحًا","sabah","noun",["maful-fih"],
      "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفُ زَمَانٍ.",
      "Object-of-time in nasb — a zarf of time: when? in the morning.",
      "Mensub mef'ûlün fîh — zarf-ı zamandır: ne zaman? sabahleyin.", punct="."),
 ],
 "jumal": [J("جَلَسَ الْوَلَدُ فِي الْمَسْجِدِ صَبَاحًا",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S4.append({"id": "s3", "translation": {
 "en": "The students stood up out of respect for the teacher.", "tr": "Öğrenciler muallime hürmeten ayağa kalktılar."},
 "tokens": [
  MADI("qama", "قَامَ", extra_g=["hollow-verbs"]),
  tok("الطُّلَّابُ","tullab","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — جَمْعُ تَكْسِيرٍ.",
      "The fa'il in raf' — a broken plural.",
      "Merfû fâil — cem'-i mükesserdir."),
  tok("إِكْرَامًا","ikram","noun",["maful-lah","form-iv-verbs","masdar"],
      "مَفْعُولٌ لَهُ مَنْصُوبٌ — مَصْدَرٌ يُبَيِّنُ عِلَّةَ الْفِعْلِ: لِمَاذَا قَامُوا؟",
      "Object-of-reason in nasb — a masdar naming the verb's motive: why did they stand?",
      "Mensub mef'ûlün leh — fiilin sebebini bildiren masdar: niçin kalktılar?"),
  tok("لِلْمُعَلِّمِ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«إِكْرَامًا».",
      "Preposition + noun attached to إِكْرَامًا.",
      "«إِكْرَامًا» masdarına mütealliḳ câr-mecrûr.",
      segments=[seg("لِ","li","prep"), seg("الْمُعَلِّمِ","muallim","noun")], punct="."),
 ],
 "jumal": [J("قَامَ الطُّلَّابُ إِكْرَامًا لِلْمُعَلِّمِ",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S4.append({"id": "s4", "translation": {
 "en": "The letter was written.", "tr": "Mektup yazıldı."},
 "tokens": [
  tok("كُتِبَتِ","kataba","verb",["naib-al-fail","thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "Past verb in the passive; the ت marks the feminine, vowelled kasra where two sukuns met.",
      "Meçhul mâzî fiil; tâ te'nis içindir, iki sâkin karşılaşınca kesralanmıştır."),
  tok("الرِّسَالَةُ","risala","noun",["naib-al-fail"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.",
      "The deputy of the fa'il, in raf'.",
      "Merfû nâibü'l-fâildir.", punct="."),
 ],
 "jumal": [J("كُتِبَتِ الرِّسَالَةُ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَبْنِيَّةٌ لِلْمَجْهُولِ — لَا مَحَلَّ لَهَا.",
   "A passive verbal clause — i'rabless.",
   "Meçhul fiil cümlesi — mahalsizdir.")]})

S4.append({"id": "s5", "translation": {
 "en": "O boy, enter the house!", "tr": "Ey çocuk, eve gir!"},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.",
      "The vocative particle.",
      "Nidâ harfidir."),
  tok("وَلَدُ","walad","noun",["vocative-munada"],
      "مُنَادًى مُفْرَدٌ مَعْرِفَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.",
      "A single definite munada, built on damm, in nasb position.",
      "Müfred marife münâdâ — zamme üzere mebnî, mahallen mensub.", punct="،"),
  tok("اُدْخُلِ","dakhala","verb",["imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ أَنْتَ.",
      "Imperative built on sukun, vowelled kasra where two sukuns met; the fa'il is a hidden أَنْتَ.",
      "Sükûn üzere mebnî emir fiili; iki sâkin karşılaşınca kesralanmıştır. Fâili gizli «أَنْتَ»dir."),
  MAFUL("bayt", "الْبَيْتَ", punct="!"),
 ],
 "jumal": [J("يَا وَلَدُ اُدْخُلِ الْبَيْتَ",
   "جُمْلَةُ نِدَاءٍ وَجُمْلَةُ أَمْرٍ — لَا مَحَلَّ لَهُمَا.",
   "A vocative clause and an imperative clause — both i'rabless.",
   "Nidâ cümlesi ve emir cümlesi — mahalsizdirler.")]})

S4.append({"id": "s6", "translation": {
 "en": "The boy did not write anything.", "tr": "Çocuk hiçbir şey yazmadı."},
 "tokens": [
  tok("مَا","ma-nafiya","part",[],
      "«مَا» نَافِيَةٌ غَيْرُ عَامِلَةٍ.",
      "The negating ma — it governs nothing.",
      "Nefiy mâsı — amel etmez."),
  MADI("kataba", "كَتَبَ"),
  FAIL("walad", "الْوَلَدُ"),
  MAFUL("shay", "شَيْئًا", punct="."),
 ],
 "jumal": [J("مَا كَتَبَ الْوَلَدُ شَيْئًا",
   "جُمْلَةٌ فِعْلِيَّةٌ مَنْفِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A negated verbal clause — i'rabless.",
   "Menfî fiil cümlesi — mahalsizdir.")]})

S4.append({"id": "s7", "translation": {
 "en": "Allah helped the believers with a mighty help.", "tr": "Allah mü'minlere büyük bir yardımla yardım etti."},
 "tokens": [
  MADI("nasara", "نَصَرَ"),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name — the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("الْمُؤْمِنِينَ","mumin","noun",["maful-bihi","jam-mudhakkar-salim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ — جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "Direct object in nasb, its sign the ya — a sound masculine plural.",
      "Mensub mef'ûlün bih; nasb alâmeti yâdır — cem'-i müzekker-i sâlim."),
  tok("نَصْرًا","nasr","noun",["maful-mutlaq","masdar"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ.",
      "Absolute object in nasb.",
      "Mensub mef'ûl-i mutlaktır."),
  tok("عَظِيمًا","azim","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ مَنْصُوبٌ لِـ«نَصْرًا».",
      "A na't in nasb, describing نَصْرًا.",
      "«نَصْرًا» kelimesinin mensub na'tıdır.", punct="."),
 ],
 "jumal": [J("نَصَرَ اللهُ الْمُؤْمِنِينَ نَصْرًا عَظِيمًا",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S4.append({"id": "s8", "translation": {
 "en": "The lesson was heard in the house.", "tr": "Ders evde işitildi."},
 "tokens": [
  tok("سُمِعَ","samia","verb",["naib-al-fail","thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.",
      "Past verb in the passive.",
      "Meçhul mâzî fiildir."),
  tok("الدَّرْسُ","dars","noun",["naib-al-fail"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.",
      "The deputy of the fa'il, in raf'.",
      "Merfû nâibü'l-fâildir."),
  PREP("fi", "فِي"),
  MAJR("bayt", "الْبَيْتِ", punct="."),
 ],
 "jumal": [J("سُمِعَ الدَّرْسُ فِي الْبَيْتِ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَبْنِيَّةٌ لِلْمَجْهُولِ — لَا مَحَلَّ لَهَا.",
   "A passive verbal clause — i'rabless.",
   "Meçhul fiil cümlesi — mahalsizdir.")]})

# ============ Chapter 5 — condition and question ============
S5.append({"id": "s1", "translation": {
 "en": "If you study, you succeed.", "tr": "Çalışırsan başarırsın."},
 "tokens": [
  tok("إِنْ","in-shartiyya","part",["in-shartiyya"],
      "حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ.",
      "The conditional particle — it puts two verbs in jazm.",
      "Câzim şart harfi — iki fiili cezmeder."),
  tok("تَدْرُسْ","darasa","verb",["in-shartiyya","lam-jazim"],
      "فِعْلُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ أَنْتَ.",
      "The condition verb in jazm, its sign the sukun; the fa'il is a hidden أَنْتَ.",
      "Meczum şart fiili; cezm alâmeti sükûndur. Fâili gizli «أَنْتَ»dir."),
  tok("تَنْجَحْ","najaha","verb",["in-shartiyya","lam-jazim"],
      "جَوَابُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ.",
      "The answer verb in jazm, its sign the sukun.",
      "Meczum cevap fiili; cezm alâmeti sükûndur.", punct="."),
 ],
 "jumal": [J("إِنْ تَدْرُسْ تَنْجَحْ",
   "جُمْلَةُ الشَّرْطِ وَجَوَابُهُ — لَا مَحَلَّ لَهُمَا.",
   "The condition clause and its answer — i'rabless.",
   "Şart cümlesi ve cevabı — mahalsizdirler.")]})

S5.append({"id": "s2", "translation": {
 "en": "Whoever seeks knowledge finds it.", "tr": "Kim ilmi ararsa onu bulur."},
 "tokens": [
  tok("مَنْ","man-shartiyya","pron",["in-shartiyya"],
      "اسْمُ شَرْطٍ جَازِمٌ مُبْتَدَأٌ.",
      "A conditional noun in jazm-government — the mubtada.",
      "Câzim şart ismi — mübtedadır."),
  tok("يَطْلُبِ","talaba","verb",["in-shartiyya","lam-jazim"],
      "فِعْلُ الشَّرْطِ مَجْزُومٌ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "The condition verb in jazm, vowelled kasra where two sukuns met.",
      "Meczum şart fiili; iki sâkin karşılaşınca kesralanmıştır."),
  MAFUL("ilm", "الْعِلْمَ"),
  tok("يَجِدْهُ","wajada","verb",["in-shartiyya","mithal-verbs"],
      "جَوَابُ الشَّرْطِ مَجْزُومٌ — مِثَالٌ حُذِفَتْ وَاوُهُ (وَجَدَ يَجِدُ)، وَالْهَاءُ مَفْعُولٌ بِهِ.",
      "The answer verb in jazm — a mithal whose waw dropped (وَجَدَ يَجِدُ); the ha is its object.",
      "Meczum cevap fiili — misâl fiildir, vâvı düşmüştür (وَجَدَ يَجِدُ); hâ zamiri mef'ûlün bihtir.",
      segments=[seg("يَجِدْ","wajada","verb"), seg("هُ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("مَنْ يَطْلُبِ الْعِلْمَ يَجِدْهُ",
   "جُمْلَتَا الشَّرْطِ وَالْجَوَابِ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَنْ».",
   "The condition and answer clauses stand in raf' position as the khabar of مَنْ.",
   "Şart ve cevap cümleleri, «مَنْ»in haberi olarak mahallen merfûdur.")]})

S5.append({"id": "s3", "translation": {
 "en": "Did you read the book?", "tr": "Kitabı okudun mu?"},
 "tokens": [
  tok("هَلْ","hal-istifham","part",[],
      "حَرْفُ اسْتِفْهَامٍ.",
      "The question particle.",
      "İstifham harfidir."),
  tok("قَرَأْتَ","qaraa","verb",["thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "Past verb; the attached ت is its fa'il: you.",
      "Mâzî fiil; bitişik tâ zamiri mahallen merfû fâildir: sen.",
      segments=[seg("قَرَأْ","qaraa","verb"), seg("تَ","pron-2ms","pron")]),
  MAFUL("kitab", "الْكِتَابَ", punct="؟"),
 ],
 "jumal": [J("هَلْ قَرَأْتَ الْكِتَابَ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِفْهَامِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An interrogative verbal clause — i'rabless.",
   "İstifham bildiren fiil cümlesi — mahalsizdir.")]})

S5.append({"id": "s4", "translation": {
 "en": "What did you hear in the lesson?", "tr": "Derste ne işittin?"},
 "tokens": [
  tok("مَاذَا","madha","pron",[],
      "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.",
      "The question noun — a fronted object in nasb position.",
      "İstifham ismi — öne alınmış mef'ûlün bih olarak mahallen mensubdur."),
  tok("سَمِعْتَ","samia","verb",["thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "Past verb; the attached ت is its fa'il.",
      "Mâzî fiil; bitişik tâ zamiri mahallen merfû fâildir.",
      segments=[seg("سَمِعْ","samia","verb"), seg("تَ","pron-2ms","pron")]),
  PREP("fi", "فِي"),
  MAJR("dars", "الدَّرْسِ", punct="؟"),
 ],
 "jumal": [J("مَاذَا سَمِعْتَ فِي الدَّرْسِ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِفْهَامِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An interrogative verbal clause — i'rabless.",
   "İstifham bildiren fiil cümlesi — mahalsizdir.")]})

S5.append({"id": "s5", "translation": {
 "en": "When the teacher came, the students stood.", "tr": "Muallim gelince öğrenciler ayağa kalktı."},
 "tokens": [
  tok("إِذَا","idha","part",["idha-shartiyya"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "A time-adverb carrying conditional force — it does not put verbs in jazm.",
      "Şart manası taşıyan zaman zarfıdır — fiilleri cezmetmez."),
  MADI("jaa", "جَاءَ", extra_g=["hollow-verbs"]),
  FAIL("muallim", "الْمُعَلِّمُ"),
  MADI("qama", "قَامَ", extra_g=["hollow-verbs"]),
  tok("الطُّلَّابُ","tullab","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "The fa'il, in raf'.",
      "Merfû fâildir.", punct="."),
 ],
 "jumal": [J("إِذَا جَاءَ الْمُعَلِّمُ قَامَ الطُّلَّابُ",
   "جُمْلَةُ الشَّرْطِ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا»، وَجُمْلَةُ الْجَوَابِ لَا مَحَلَّ لَهَا.",
   "The condition clause sits in jarr after إِذَا's idafa; the answer clause is i'rabless.",
   "Şart cümlesi «إِذَا»nın izâfetiyle mahallen mecrur; cevap cümlesi mahalsizdir.")]})

S5.append({"id": "s6", "translation": {
 "en": "Do not write on the wall.", "tr": "Duvara yazma."},
 "tokens": [
  tok("لَا","la-nahiya-p","part",["la-nahiya"],
      "«لَا» النَّاهِيَةُ — تَجْزِمُ الْمُضَارِعَ.",
      "The prohibiting la — it puts the mudari in jazm.",
      "Nehiy lâsı — muzâriyi cezmeder."),
  tok("تَكْتُبْ","kataba","verb",["la-nahiya","lam-jazim"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ، وَالْفَاعِلُ أَنْتَ.",
      "Mudari in jazm after the prohibiting la; the fa'il is a hidden أَنْتَ.",
      "Nehiy lâsıyla meczum muzâri; fâili gizli «أَنْتَ»dir."),
  PREP("ala", "عَلَى"),
  MAJR("jidar", "الْجِدَارِ", punct="."),
 ],
 "jumal": [J("لَا تَكْتُبْ عَلَى الْجِدَارِ",
   "جُمْلَةٌ فِعْلِيَّةٌ نَاهِيَةٌ — لَا مَحَلَّ لَهَا.",
   "A prohibiting verbal clause — i'rabless.",
   "Nehiy bildiren fiil cümlesi — mahalsizdir.")]})

S5.append({"id": "s7", "translation": {
 "en": "Let every student sit in his place.", "tr": "Her öğrenci yerine otursun."},
 "tokens": [
  tok("لِيَجْلِسْ","jalasa","verb",["lam-amr"],
      "اللَّامُ لَامُ الْأَمْرِ، وَالْفِعْلُ مُضَارِعٌ مَجْزُومٌ بِهَا.",
      "The lam of command; the mudari stands in jazm after it.",
      "Lâm, emir lâmıdır; muzâri onunla meczumdur.",
      segments=[seg("لِ","lam-amr-p","part"), seg("يَجْلِسْ","jalasa","verb")]),
  tok("كُلُّ","kull","noun",["fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "The fa'il in raf', itself a mudaf.",
      "Merfû fâil ve muzâftır."),
  tok("طَالِبٍ","talib","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir."),
  PREP("fi", "فِي"),
  tok("مَكَانِهِ","makan","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr, a mudaf; the ha its mudaf ilayh.",
      "Mecrur ve muzâf; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("مَكَانِ","makan","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("لِيَجْلِسْ كُلُّ طَالِبٍ فِي مَكَانِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ طَلَبِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A verbal clause of command — i'rabless.",
   "Talep bildiren fiil cümlesi — mahalsizdir.")]})

S5.append({"id": "s8", "translation": {
 "en": "Where is your book, O boy?", "tr": "Kitabın nerede, ey çocuk?"},
 "tokens": [
  tok("أَيْنَ","ayna","pron",[],
      "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.",
      "The question noun — a fronted khabar in raf' position.",
      "İstifham ismi — öne geçmiş haber olarak mahallen merfûdur."),
  tok("كِتَابُكَ","kitab","noun",["mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "The delayed mubtada in raf'; the kaf is its mudaf ilayh.",
      "Sonraya bırakılmış merfû mübteda; kâf zamiri muzâfun ileyhtir.",
      segments=[seg("كِتَابُ","kitab","noun"), seg("كَ","pron-2ms","pron")]),
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.",
      "The vocative particle.",
      "Nidâ harfidir."),
  tok("وَلَدُ","walad","noun",["vocative-munada"],
      "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.",
      "A munada built on damm, in nasb position.",
      "Zamme üzere mebnî münâdâ — mahallen mensub.", punct="؟"),
 ],
 "jumal": [J("أَيْنَ كِتَابُكَ يَا وَلَدُ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِفْهَامِيَّةٌ وَجُمْلَةُ نِدَاءٍ — لَا مَحَلَّ لَهُمَا.",
   "An interrogative nominal clause and a vocative — both i'rabless.",
   "İstifham bildiren isim cümlesi ve nidâ — mahalsizdirler.")]})

S6 = []

# ============ Chapter 6 — the two families, temyiz and istisna ============
S6.append({"id": "s1", "translation": {
 "en": "The lesson was easy.", "tr": "Ders kolaydı."},
 "tokens": [
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
      "A defective past verb: raf' on its ism, nasb on its khabar.",
      "Nâkıs mâzî fiil: ismini ref, haberini nasbeder."),
  tok("الدَّرْسُ","dars","noun",["kana-wa-akhawatuha"],
      "اسْمُ «كَانَ» مَرْفُوعٌ.",
      "The ism of كَانَ, in raf'.",
      "«كَانَ»nin merfû ismidir."),
  tok("سَهْلًا","sahl","noun",["kana-wa-akhawatuha"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ.",
      "The khabar of كَانَ, in nasb.",
      "«كَانَ»nin mensub haberidir.", punct="."),
 ],
 "jumal": [J("كَانَ الدَّرْسُ سَهْلًا",
   "جُمْلَةٌ فِعْلِيَّةٌ نَاسِخَةٌ — لَا مَحَلَّ لَهَا.",
   "A clause governed by kana — i'rabless.",
   "Kâne ile mensuh cümle — mahalsizdir.")]})

S6.append({"id": "s2", "translation": {
 "en": "Truly the lesson is easy.", "tr": "Şüphesiz ders kolaydır."},
 "tokens": [
  tok("إِنَّ","inna","part",["inna-wa-akhawatuha","inna-am-anna"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — عَكْسُ «كَانَ».",
      "A particle of emphasis: nasb on its ism, raf' on its khabar — the mirror of كَانَ.",
      "Te'kid ve nasb harfi: ismini nasb, haberini ref eder — «كَانَ»nin tam tersi."),
  tok("الدَّرْسَ","dars","noun",["inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ.",
      "The ism of إِنَّ, in nasb.",
      "«إِنَّ»nin mensub ismidir."),
  tok("سَهْلٌ","sahl","noun",["inna-wa-akhawatuha"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ.",
      "The khabar of إِنَّ, in raf'.",
      "«إِنَّ»nin merfû haberidir.", punct="."),
 ],
 "jumal": [J("إِنَّ الدَّرْسَ سَهْلٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مُؤَكَّدَةٌ — لَا مَحَلَّ لَهَا.",
   "An emphasized nominal clause — i'rabless.",
   "Te'kidli isim cümlesi — mahalsizdir.")]})

S6.append({"id": "s3", "translation": {
 "en": "The student became diligent.", "tr": "Öğrenci çalışkan oldu."},
 "tokens": [
  tok("صَارَ","sara","verb",["kana-wa-akhawatuha","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ» لِلتَّحَوُّلِ.",
      "A defective past verb of the kana family, marking a change of state.",
      "Kâne'nin kardeşlerinden nâkıs fiil; hâl değişimi bildirir."),
  tok("الطَّالِبُ","talib","noun",["kana-wa-akhawatuha"],
      "اسْمُ «صَارَ» مَرْفُوعٌ.",
      "The ism of صَارَ, in raf'.",
      "«صَارَ»nin merfû ismidir."),
  tok("مُجْتَهِدًا","mujtahid","noun",["kana-wa-akhawatuha","ism-fail","form-viii-verbs"],
      "خَبَرُ «صَارَ» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنَ «اجْتَهَدَ».",
      "The khabar of صَارَ in nasb — the ism fa'il of اجْتَهَدَ.",
      "«صَارَ»nin mensub haberi — «اجْتَهَدَ» fiilinin ism-i fâili.", punct="."),
 ],
 "jumal": [J("صَارَ الطَّالِبُ مُجْتَهِدًا",
   "جُمْلَةٌ فِعْلِيَّةٌ نَاسِخَةٌ — لَا مَحَلَّ لَهَا.",
   "A clause governed by sara — i'rabless.",
   "Sâre ile mensuh cümle — mahalsizdir.")]})

S6.append({"id": "s4", "translation": {
 "en": "I bought twenty books.", "tr": "Yirmi kitap satın aldım."},
 "tokens": [
  tok("اشْتَرَيْتُ","ishtara","verb",["form-viii-verbs","naqis-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ الْبِنَاءِ، وَالتَّاءُ فَاعِلٌ — «اشْتَرَى» مِنَ الِافْتِعَالِ.",
      "A past verb with a weak last radical; the ta is its fa'il — اشْتَرَى, Form VIII.",
      "Nâkıs binâlı mâzî fiil; tâ zamiri fâildir — «اشْتَرَى», iftiâldendir.",
      segments=[seg("اشْتَرَيْ","ishtara","verb"), seg("تُ","pron-1s","pron")]),
  tok("عِشْرِينَ","ishrin","noun",["tamyiz","jam-mudhakkar-salim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ — مِنْ أَلْفَاظِ الْعُقُودِ.",
      "Direct object in nasb, its sign the ya — one of the decade numerals.",
      "Mensub mef'ûlün bih; nasb alâmeti yâdır — ukud lafızlarındandır."),
  tok("كِتَابًا","kitab","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ — يُفَسِّرُ الْعَدَدَ الْمُبْهَمَ، وَتَمْيِيزُ الْعُقُودِ مُفْرَدٌ مَنْصُوبٌ.",
      "A tamyiz in nasb — it clears up the vague number; the decades take a SINGULAR mansub tamyiz.",
      "Mensub temyiz — kapalı sayıyı açıklar; ukudun temyizi müfred ve mensubdur.", punct="."),
 ],
 "jumal": [J("اشْتَرَيْتُ عِشْرِينَ كِتَابًا",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S6.append({"id": "s5", "translation": {
 "en": "The students came except Zayd.", "tr": "Zeyd hâriç öğrenciler geldi."},
 "tokens": [
  MADI("jaa", "جَاءَ", extra_g=["hollow-verbs"]),
  tok("الطُّلَّابُ","tullab","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "The fa'il, in raf'.",
      "Merfû fâildir."),
  tok("إِلَّا","illa","part",["istithna"],
      "أَدَاةُ اسْتِثْنَاءٍ.",
      "The particle of exception.",
      "İstisnâ edatıdır."),
  tok("زَيْدًا","zayd","noun",["istithna"],
      "مُسْتَثْنًى مَنْصُوبٌ — الْكَلَامُ تَامٌّ مُوجَبٌ فَوَجَبَ النَّصْبُ.",
      "The excepted noun in nasb — the sentence is complete and affirmative, so nasb is obligatory.",
      "Mensub müstesnâ — kelâm tâm ve mûcebdir, bu yüzden nasb vâcibdir.", punct="."),
 ],
 "jumal": [J("جَاءَ الطُّلَّابُ إِلَّا زَيْدًا",
   "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening verbal clause — i'rabless.",
   "İbtidâiyye fiil cümlesi — mahalsizdir.")]})

S6.append({"id": "s6", "translation": {
 "en": "No one came except Zayd.", "tr": "Zeyd'den başkası gelmedi."},
 "tokens": [
  tok("مَا","ma-nafiya","part",[],
      "«مَا» نَافِيَةٌ.",
      "The negating ma.",
      "Nefiy mâsıdır."),
  MADI("jaa", "جَاءَ", extra_g=["hollow-verbs"]),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ حَصْرٍ — الْكَلَامُ نَاقِصٌ مَنْفِيٌّ، فَالِاسْتِثْنَاءُ مُفَرَّغٌ.",
      "A particle of restriction — the sentence is incomplete and negated, so the exception is «emptied».",
      "Hasr edatı — kelâm nâkıs ve menfîdir; istisnâ müferrağdır."),
  tok("زَيْدٌ","zayd","noun",["istithna-mufarragh","fail"],
      "فَاعِلٌ مَرْفُوعٌ — فِي الِاسْتِثْنَاءِ الْمُفَرَّغِ يُعْرَبُ الِاسْمُ بِحَسَبِ مَوْقِعِهِ، لَا مُسْتَثْنًى.",
      "The fa'il in raf' — in an «emptied» exception the noun takes the case its POSITION demands, not the nasb of an excepted noun.",
      "Merfû fâil — müferrağ istisnâda isim, müstesnâ olarak değil, cümledeki yerine göre i'râb alır.", punct="."),
 ],
 "jumal": [J("مَا جَاءَ إِلَّا زَيْدٌ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَنْفِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A negated verbal clause — i'rabless.",
   "Menfî fiil cümlesi — mahalsizdir.")]})

S6.append({"id": "s7", "translation": {
 "en": "The teacher is more knowing than the student.", "tr": "Muallim öğrenciden daha bilgilidir."},
 "tokens": [
  MUBT("muallim", "الْمُعَلِّمُ"),
  tok("أَعْلَمُ","alam-tafdil","noun",["ism-tafdil","mubtada-khabar","mamnu-min-sarf"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ عَلَى «أَفْعَلُ»، مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ.",
      "Khabar in raf' — an ism tafdil on أَفْعَلُ, a diptote for being a description on a verbal pattern.",
      "Merfû haber — «أَفْعَلُ» vezninde ism-i tafdîl; vasıflık ve fiil vezni sebebiyle gayr-i munsariftir."),
  PREP("min", "مِنَ"),
  MAJR("talib", "الطَّالِبِ", punct="."),
 ],
 "jumal": [J("الْمُعَلِّمُ أَعْلَمُ مِنَ الطَّالِبِ",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})

S6.append({"id": "s8", "translation": {
 "en": "Zayd is the best of the students in understanding.", "tr": "Zeyd, anlayışça öğrencilerin en iyisidir."},
 "tokens": [
  MUBT("zayd", "زَيْدٌ"),
  tok("أَفْضَلُ","afdal","noun",["ism-tafdil","mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — اسْمُ تَفْضِيلٍ أُضِيفَ فَلَزِمَ الْإِفْرَادَ.",
      "Khabar in raf', itself a mudaf — an ism tafdil in idafa, which keeps it singular.",
      "Merfû haber ve muzâf — izâfetle gelen ism-i tafdîl müfred kalır."),
  tok("الطُّلَّابِ","tullab","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir."),
  tok("فَهْمًا","fahm","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ — يُبَيِّنُ جِهَةَ التَّفْضِيلِ: أَفْضَلُ مِنْ أَيِّ وَجْهٍ؟",
      "A tamyiz in nasb — it names the respect in which he excels: better in WHAT?",
      "Mensub temyiz — üstünlüğün hangi cihetten olduğunu bildirir: neyce üstün?", punct="."),
 ],
 "jumal": [J("زَيْدٌ أَفْضَلُ الطُّلَّابِ فَهْمًا",
   "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An opening nominal clause — i'rabless.",
   "İbtidâiyye isim cümlesi — mahalsizdir.")]})


S7 = []

# ============ Chapter 7 — the vocative, all five kinds ============
# Every kind of munada the books count, in order, so the NidaEngine's ruling
# can be read against a stored i'rab for each: two FIXED kinds, three really
# mansub, and the way in to a noun that wears the article.
S7.append({"id": "s1", "translation": {
 "en": "Zayd, sit down.", "tr": "Zeyd, otur."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ نَائِبٌ عَنْ «أَدْعُو».",
      "A particle of calling, standing in for «I call».",
      "«Çağırıyorum» fiilinin yerini tutan nidâ harfi."),
  tok("زَيْدُ","zayd","noun",["vocative-munada"],
      "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.",
      "A single proper name: fixed on the damma, in the position of nasb.",
      "Müfred alem: damme üzere mebnî, mahallen mansub."),
  tok("اِجْلِسْ","jalasa","verb",["imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ «أَنْتَ».",
      "An imperative built on sukun; the fa'il is hidden, «you».",
      "Sükûn üzere mebnî emir fiili; fâil müstetir «sen».", punct="."),
 ],
 "jumal": [J("يَا زَيْدُ اِجْلِسْ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ طَلَبِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then an imperative clause — neither takes a case.",
   "Nidâ cümlesi, sonra talebî fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s2", "translation": {
 "en": "Student, write the lesson.", "tr": "Öğrenci, dersi yaz."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("طَالِبُ","talib","noun",["vocative-munada"],
      "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.",
      "No proper name at all, yet MEANT of the one before you: a nakira maqsuda, fixed on the damma just the same.",
      "Hiç alem değil, fakat önündekini KASTEDİYOR: nekire-i maksûde; o da damme üzere mebnîdir."),
  tok("اُكْتُبِ","kataba","verb",["imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "An imperative on sukun, given a kasra where two sakins met.",
      "Sükûn üzere mebnî emir; iki sâkin buluştuğu için kesra verilmiştir."),
  tok("الدَّرْسَ","dars","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "Direct object, in nasb.", "Mansub mef'ûlün bih.", punct="."),
 ],
 "jumal": [J("يَا طَالِبُ اُكْتُبِ الدَّرْسَ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then a verbal clause — neither takes a case.",
   "Nidâ cümlesi, sonra fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s3", "translation": {
 "en": "You two students, write the lesson.", "tr": "Ey iki öğrenci, dersi yazın."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("طَالِبَانِ","talib","noun",["vocative-munada","al-muthanna"],
      "مُنَادًى مُثَنًّى مَبْنِيٌّ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ — يُبْنَى عَلَى مَا يُرْفَعُ بِهِ.",
      "A dual munada: fixed on the ALIF, not the damma — it is built on whatever would RAISE it.",
      "Tesniye münâdâ: damme üzere değil ELİF üzere mebnî — kendisiyle MERFÛ olacağı şey üzere bina edilir."),
  tok("اُكْتُبَا","kataba","verb",["imperative-amr","afal-khamsa"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ.",
      "An imperative built on the DROPPED nun; the dual alif inside it is the fa'il.",
      "Nûnun hazfi üzere mebnî emir; içindeki elif-i isneyn fâildir."),
  tok("الدَّرْسَ","dars","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "Direct object, in nasb.", "Mansub mef'ûlün bih.", punct="."),
 ],
 "jumal": [J("يَا طَالِبَانِ اُكْتُبَا الدَّرْسَ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then a verbal clause — neither takes a case.",
   "Nidâ cümlesi, sonra fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s4", "translation": {
 "en": "Muslims, listen.", "tr": "Ey Müslümanlar, dinleyin."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("مُسْلِمُونَ","muslim","noun",["vocative-munada","jam-mudhakkar-salim"],
      "مُنَادًى جَمْعُ مُذَكَّرٍ سَالِمٌ مَبْنِيٌّ عَلَى الْوَاوِ فِي مَحَلِّ نَصْبٍ.",
      "A sound masculine plural munada: fixed on the WAW — the very letter that raises it.",
      "Cem'-i müzekker-i sâlim münâdâ: onu ref eden harfin ta kendisi olan VÂV üzere mebnî."),
  tok("اِسْمَعُوا","samia","verb",["imperative-amr","afal-khamsa"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَوَاوُ الْجَمَاعَةِ فَاعِلٌ.",
      "An imperative built on the dropped nun; the waw of the group is the fa'il.",
      "Nûnun hazfi üzere mebnî emir; vâv-ı cemâat fâildir.", punct="."),
 ],
 "jumal": [J("يَا مُسْلِمُونَ اِسْمَعُوا",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then a verbal clause — neither takes a case.",
   "Nidâ cümlesi, sonra fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s5", "translation": {
 "en": "Abdullah, enter the house.", "tr": "Abdullah, eve gir."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("عَبْدَ","abd","noun",["vocative-munada","idafa-definiteness"],
      "مُنَادًى مُضَافٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — وَالْمُضَافُ لَا يُبْنَى.",
      "A mudaf munada: really mansub by the fatha — a mudaf is never fixed.",
      "Muzâf münâdâ: fetha ile gerçekten mansub — muzâf mebnî olmaz."),
  tok("اللهِ","allah","propn",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh, in jarr.", "Mecrûr muzâfun ileyh."),
  tok("اُدْخُلِ","dakhala","verb",["imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "An imperative on sukun, given a kasra where two sakins met.",
      "Sükûn üzere mebnî emir; iki sâkin buluştuğu için kesra verilmiştir."),
  tok("الْبَيْتَ","bayt","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "Direct object, in nasb.", "Mansub mef'ûlün bih.", punct="."),
 ],
 "jumal": [J("يَا عَبْدَ اللهِ اُدْخُلِ الْبَيْتَ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then a verbal clause — neither takes a case.",
   "Nidâ cümlesi, sonra fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s6", "translation": {
 "en": "Somebody — anybody — listen.", "tr": "Ey (herhangi) bir adam, dinle."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("رَجُلًا","rajul","noun",["vocative-munada"],
      "مُنَادًى نَكِرَةٌ غَيْرُ مَقْصُودَةٍ مَنْصُوبٌ، وَبَقِيَ تَنْوِينُهُ لِأَنَّهُ نَكِرَةٌ.",
      "An indefinite meant of nobody in particular: really mansub — and it alone KEEPS its tanwin.",
      "Hiç kimseyi kastetmeyen nekire: gerçekten mansub — ve tenvinini KORUYAN yalnız odur."),
  tok("اِسْمَعْ","samia","verb",["imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ «أَنْتَ».",
      "An imperative built on sukun; the fa'il is hidden, «you».",
      "Sükûn üzere mebnî emir fiili; fâil müstetir «sen».", punct="."),
 ],
 "jumal": [J("يَا رَجُلًا اِسْمَعْ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then an imperative clause — neither takes a case.",
   "Nidâ cümlesi, sonra talebî fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s7", "translation": {
 "en": "O student, seek knowledge.", "tr": "Ey talebe, ilmi taleb et."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("أَيُّهَا","ayyuha","noun",["vocative-munada","huruf-tanbih"],
      "«أَيُّ» مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَ«هَا» حَرْفُ تَنْبِيهٍ — وَهُوَ الْوُصْلَةُ إِلَى نِدَاءِ الْمُعَرَّفِ بِـ«الْ».",
      "«ayy» is the munada, fixed on the damma; «ha» is a particle of drawing near — together they are the only way in to calling a noun that wears the article.",
      "Münâdâ «eyy»dir, damme üzere mebnî; «hâ» tenbih harfidir — ال'lı bir isme seslenmenin yegâne yolu budur.",
      segments=[seg("أَيُّ","ayyuha","noun"), seg("هَا","ha-tanbih","part")]),
  tok("الطَّالِبُ","talib","noun",["naat-sifa"],
      "نَعْتٌ لِـ«أَيُّ» مَرْفُوعٌ لَفْظًا.",
      "A na't following «ayy» — and it is raf' on the page, not nasb.",
      "«Eyy»in na'tı — sayfada mansub değil, merfûdur."),
  tok("اُطْلُبِ","talaba","verb",["imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "An imperative on sukun, given a kasra where two sakins met.",
      "Sükûn üzere mebnî emir; iki sâkin buluştuğu için kesra verilmiştir."),
  tok("الْعِلْمَ","ilm","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "Direct object, in nasb.", "Mansub mef'ûlün bih.", punct="."),
 ],
 "jumal": [J("يَا أَيُّهَا الطَّالِبُ اُطْلُبِ الْعِلْمَ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then a verbal clause — neither takes a case.",
   "Nidâ cümlesi, sonra fiil cümlesi — ikisi de mahalsizdir.")]})

S7.append({"id": "s8", "translation": {
 "en": "My teacher, I heard your lesson.", "tr": "Hocam, dersini dinledim."},
 "tokens": [
  tok("يَا","ya-nida","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ.", "A particle of calling.", "Nidâ harfi."),
  tok("مُعَلِّمِي","muallim","noun",["vocative-munada","idafa-definiteness"],
      "مُنَادًى مُضَافٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.",
      "A mudaf to the speaker's ya: still mansub, but by an ESTIMATED fatha — nothing shows on the page.",
      "Mütekellim yâsına muzâf: yine mansub, fakat TAKDÎRÎ fetha ile — sayfada görünen yoktur.",
      segments=[seg("مُعَلِّمِ","muallim","noun"), seg("ي","pron-1s","pron")]),
  tok("سَمِعْتُ","samia","verb",["thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ.",
      "A past verb built on sukun because the ta of the doer joined it; that ta is the fa'il.",
      "Fâil tâsı bitiştiği için sükûn üzere mebnî mâzî; tâ fâildir.",
      segments=[seg("سَمِعْ","samia","verb"), seg("تُ","pron-1s","pron")]),
  tok("دَرْسَكَ","dars","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "Direct object in nasb; the kaf is its mudaf ilayh.",
      "Mansub mef'ûlün bih; kâf muzâfun ileyhtir.",
      segments=[seg("دَرْسَ","dars","noun"), seg("كَ","pron-2ms","pron")], punct="."),
 ],
 "jumal": [J("يَا مُعَلِّمِي سَمِعْتُ دَرْسَكَ",
   "جُمْلَةُ نِدَاءٍ ثُمَّ جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهُمَا.",
   "A vocative, then a verbal clause — neither takes a case.",
   "Nidâ cümlesi, sonra fiil cümlesi — ikisi de mahalsizdir.")]})

TITLES = [
 {"ar": "الْجُمْلَةُ الْفِعْلِيَّةُ", "en": "The Verbal Sentence", "tr": "Fiil Cümlesi"},
 {"ar": "الْجُمْلَةُ الِاسْمِيَّةُ", "en": "The Nominal Sentence", "tr": "İsim Cümlesi"},
 {"ar": "إِنَّ أَمْ أَنَّ؟", "en": "Inna or Anna?", "tr": "İnne mi Enne mi?"},
 {"ar": "الْمَفَاعِيلُ وَالنَّائِبُ", "en": "The Objects Family and the Deputy", "tr": "Mef'ûller ve Nâibü'l-Fâil"},
 {"ar": "الشَّرْطُ وَالِاسْتِفْهَامُ", "en": "Condition and Question", "tr": "Şart ve İstifham"},
 {"ar": "الْعَامِلَانِ وَالتَّمْيِيزُ وَالِاسْتِثْنَاءُ", "en": "The Two Families, Tamyiz and Istithna", "tr": "İki Aile, Temyiz ve İstisnâ"},
 {"ar": "النِّدَاءُ وَأَقْسَامُ الْمُنَادَى", "en": "The Vocative and its Five Kinds", "tr": "Nidâ ve Münâdânın Beş Çeşidi"},
]

# ---- glossary -------------------------------------------------------------
def g(lemma, pos, en, tr, level, root=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    return e

GLOSS = {
 "zayd": g("زَيْد", "noun", "Zayd (the grammar books' everyman)", "Zeyd (gramer kitaplarının meşhur öznesi)", 1),
 "risala": g("رِسَالَة", "noun", "letter, epistle", "mektup; risale", 2, "ر س ل"),
 "talib": g("طَالِب", "noun", "student, seeker", "öğrenci; talebe", 1, "ط ل ب"),
 "tullab": g("طُلَّاب", "noun", "students (broken plural)", "öğrenciler (cem'-i mükesser)", 2, "ط ل ب"),
 "kitab": g("كِتَاب", "noun", "book", "kitap", 1, "ك ت ب"),
 "muallim": g("مُعَلِّم", "noun", "teacher", "muallim; öğretmen", 1, "ع ل م"),
 "masjid": g("مَسْجِد", "noun", "mosque", "mescid", 1, "س ج د"),
 "walad": g("وَلَد", "noun", "boy, child", "çocuk; oğlan", 1, "و ل د"),
 "bayt": g("بَيْت", "noun", "house", "ev", 1, "ب ي ت"),
 "dars": g("دَرْس", "noun", "lesson", "ders", 1, "د ر س"),
 "farih": g("فَرِح", "noun", "glad, joyful", "sevinçli", 2, "ف ر ح"),
 "rakib": g("رَاكِب", "noun", "riding, rider (ism fa'il)", "binici; binmiş (ism-i fâil)", 2, "ر ك ب"),
 "ilm": g("عِلْم", "noun", "knowledge", "ilim", 1, "ع ل م"),
 "nur": g("نُور", "noun", "light", "nur; ışık", 1, "ن و ر"),
 "jadid": g("جَدِيد", "noun", "new", "yeni", 1, "ج د د"),
 "mujtahid": g("مُجْتَهِد", "noun", "diligent (ism fa'il, Form VIII)", "çalışkan; müctehid (ism-i fâil)", 3, "ج ه د"),
 "mahbub": g("مَحْبُوب", "noun", "beloved (ism maf'ul)", "sevilen; mahbub (ism-i mef'ûl)", 2, "ح ب ب"),
 "rajul": g("رَجُل", "noun", "man", "adam", 1, "ر ج ل"),
 "allah": g("الله", "noun", "Allah", "Allah", 1),
 "nafi": g("نَافِع", "noun", "beneficial (ism fa'il)", "faydalı; nâfi (ism-i fâil)", 2, "ن ف ع"),
 "sab": g("صَعْب", "noun", "difficult", "zor", 2, "ص ع ب"),
 "sahl": g("سَهْل", "noun", "easy", "kolay", 2, "س ه ل"),
 "marid": g("مَرِيض", "noun", "ill, sick", "hasta", 2, "م ر ض"),
 "bint": g("بِنْت", "noun", "girl, daughter", "kız", 1, "ب ن ت"),
 "muhammad": g("مُحَمَّد", "noun", "Muhammad ﷺ", "Muhammed ﷺ", 1, "ح م د"),
 "rasul": g("رَسُول", "noun", "messenger", "rasûl; elçi", 1, "ر س ل"),
 "kull": g("كُلّ", "noun", "every, all", "her; bütün", 1, "ك ل ل"),
 "shay": g("شَيْء", "noun", "thing", "şey", 1, "ش ي أ"),
 "qadir": g("قَادِر", "noun", "able, powerful (ism fa'il)", "kâdir; güç yetiren (ism-i fâil)", 2, "ق د ر"),
 # verbs
 "kataba": g("كَتَبَ", "verb", "to write", "yazmak", 1, "ك ت ب"),
 "qaraa": g("قَرَأَ", "verb", "to read, recite", "okumak", 1, "ق ر أ"),
 "dakhala": g("دَخَلَ", "verb", "to enter", "girmek", 1, "د خ ل"),
 "jaa": g("جَاءَ", "verb", "to come", "gelmek", 1, "ج ي أ"),
 "rajaa": g("رَجَعَ", "verb", "to return", "dönmek", 1, "ر ج ع"),
 "samia": g("سَمِعَ", "verb", "to hear, listen", "işitmek; dinlemek", 1, "س م ع"),
 "kharaja": g("خَرَجَ", "verb", "to go out", "çıkmak", 1, "خ ر ج"),
 "alima": g("عَلِمَ", "verb", "to know", "bilmek", 1, "ع ل م"),
 "qala": g("قَالَ", "verb", "to say", "demek; söylemek", 1, "ق و ل"),
 "shahida": g("شَهِدَ", "verb", "to bear witness", "şehadet etmek; tanık olmak", 2, "ش ه د"),
 "laysa": g("لَيْسَ", "verb", "is not (defective)", "değildir (nâkıs fiil)", 2),
 # particles & pronouns
 "ila": g("إِلَى", "prep", "to, toward", "-e; -e doğru", 1),
 "min": g("مِنْ", "prep", "from", "-den", 1),
 "fi": g("فِي", "prep", "in", "-de; içinde", 1),
 "li": g("لِ", "prep", "for, to", "için; -e", 1),
 "ala": g("عَلَى", "prep", "upon, over", "üzerine; -e", 1),
 "inna": g("إِنَّ", "part", "truly (emphasis; nasb on its noun)", "şüphesiz (te'kid; ismini nasb eder)", 2),
 "anna": g("أَنَّ", "part", "that (turns its clause into a masdar)", "-dığı(nı) (cümlesini masdara çevirir)", 3),
 "lam-jazima": g("لَمْ", "part", "did not (jazm + time-flip)", "-medi (cezm eder, manayı mâzîye çevirir)", 2),
 "wa": g("وَ", "part", "and; oath waw", "ve; kasem vâvı", 1),
 "pron-1s": g("ـتُ", "pron", "I (attached subject)", "ben (bitişik fâil zamiri)", 1),
 "pron-2ms": g("ـكَ / ـتَ", "pron", "you / your (attached)", "sen / senin (bitişik zamir)", 1),
 "pron-3ms": g("ـهُ", "pron", "him / his (attached)", "onu / onun (bitişik zamir)", 1),
 "quran": g("الْقُرْآن", "noun", "the Qur'an", "Kur'ân", 1, "ق ر أ"),
 "hifz": g("حِفْظ", "noun", "memorization (masdar)", "hıfz; ezber (masdar)", 2, "ح ف ظ"),
 "sabah": g("صَبَاح", "noun", "morning", "sabah", 1, "ص ب ح"),
 "ikram": g("إِكْرَام", "noun", "honoring (masdar, Form IV)", "ikram; hürmet (masdar)", 2, "ك ر م"),
 "ya-nida": g("يَا", "part", "O! (vocative)", "ey (nidâ)", 1),
 "ayyuha": g("أَيُّ", "noun", "the one addressed (in أَيُّهَا)", "eyy (أَيُّهَا'daki münâdâ)", 3),
 "ha-tanbih": g("هَا (لِلتَّنْبِيهِ)", "part", "ha of drawing attention", "tenbih hâsı", 3),
 "muslim": g("مُسْلِم", "noun", "Muslim, one who submits", "müslüman", 1, "س ل م"),
 "abd": g("عَبْد", "noun", "servant, slave", "kul, köle", 1, "ع ب د"),
 "ma-nafiya": g("مَا (النَّافِيَة)", "part", "not (negating ma)", "değil; -medi (nefiy mâsı)", 2),
 "mumin": g("مُؤْمِن", "noun", "believer", "mü'min", 1, "أ م ن"),
 "nasr": g("نَصْر", "noun", "help, victory (masdar)", "nusret; yardım (masdar)", 2, "ن ص ر"),
 "azim": g("عَظِيم", "noun", "mighty, great", "büyük; azîm", 1, "ع ظ م"),
 "hafiza": g("حَفِظَ", "verb", "to memorize, preserve", "ezberlemek; korumak", 1, "ح ف ظ"),
 "jalasa": g("جَلَسَ", "verb", "to sit", "oturmak", 1, "ج ل س"),
 "qama": g("قَامَ", "verb", "to stand up", "kalkmak; ayağa kalkmak", 1, "ق و م"),
 "nasara": g("نَصَرَ", "verb", "to help", "yardım etmek", 1, "ن ص ر"),
 "in-shartiyya": g("إِنْ", "part", "if (jazm on two verbs)", "eğer (iki fiili cezmeder)", 2),
 "man-shartiyya": g("مَنْ (الشَّرْطِيَّة)", "pron", "whoever (conditional)", "her kim (şart)", 2),
 "darasa": g("دَرَسَ", "verb", "to study", "ders çalışmak; okumak", 1, "د ر س"),
 "najaha": g("نَجَحَ", "verb", "to succeed", "başarmak", 1, "ن ج ح"),
 "talaba": g("طَلَبَ", "verb", "to seek", "aramak; talep etmek", 1, "ط ل ب"),
 "wajada": g("وَجَدَ", "verb", "to find", "bulmak", 1, "و ج د"),
 "hal-istifham": g("هَلْ", "part", "…? (yes/no question)", "mi? (istifham)", 1),
 "madha": g("مَاذَا", "pron", "what?", "ne?", 1),
 "idha": g("إِذَا", "part", "when / if (time-condition)", "-ınca; -dığı zaman (şart zarfı)", 2),
 "la-nahiya-p": g("لَا (النَّاهِيَة)", "part", "do not (jazm)", "-me! (nehiy lâsı, cezmeder)", 2),
 "lam-amr-p": g("لِ (لَامُ الْأَمْرِ)", "part", "let … (lam of command)", "-sın (emir lâmı)", 2),
 "jidar": g("جِدَار", "noun", "wall", "duvar", 2, "ج د ر"),
 "makan": g("مَكَان", "noun", "place", "yer; mekân", 1, "ك و ن"),
 "ayna": g("أَيْنَ", "pron", "where?", "nerede?", 1),
 "kana": g("كَانَ", "verb", "to be, was", "olmak; idi", 1, "ك و ن"),
 "sara": g("صَارَ", "verb", "to become", "olmak; hâline gelmek", 2, "ص ي ر"),
 "ishtara": g("اشْتَرَى", "verb", "to buy", "satın almak", 2, "ش ر ي"),
 "ishrin": g("عِشْرِين", "noun", "twenty", "yirmi", 2, "ع ش ر"),
 "illa": g("إِلَّا", "part", "except; only (after a negation)", "hâriç; ancak (nefiyden sonra)", 2),
 "alam-tafdil": g("أَعْلَم", "noun", "more/most knowing (ism tafdil)", "daha bilgili; en bilgili (ism-i tafdîl)", 3, "ع ل م"),
 "afdal": g("أَفْضَل", "noun", "better, best (ism tafdil)", "daha iyi; en iyi (ism-i tafdîl)", 3, "ف ض ل"),
 "fahm": g("فَهْم", "noun", "understanding", "anlayış; fehim", 2, "ف ه م"),
}

# ---- manifest -------------------------------------------------------------
MANIFEST = {
 "id": "jumal-al-tadrib",
 "storyGroup": "jumal-al-tadrib",
 "title": {"ar": "جُمَلُ التَّدْرِيبِ", "en": "Practice Sentences", "tr": "Alıştırma Cümleleri"},
 "subtitle": {"ar": "قِرَاءَةُ الْإِعْرَابِ جُمْلَةً جُمْلَةً",
              "en": "Reading i'rab sentence by sentence, hoca-style",
              "tr": "Hoca usulü, cümle cümle i'râb okuma"},
 "level": 2,
 "levelName": "Elementary",
 "version": "1.3.0",
 "published": "2026-08-03",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": [],
 "attribution": {
  "ar": "جُمَلٌ تَعْلِيمِيَّةٌ أَصْلِيَّةٌ صِيغَتْ تَحْرِيرِيًّا لِلتَّدْرِيبِ عَلَى الْإِعْرَابِ.",
  "en": ("ORIGINAL textbook-style drill sentences, composed editorially in the "
         "question-chain style supplied by the project owner (Gâle = said, who? "
         "Zeydun…). Nothing here is a quotation of any classical text; the "
         "sentences exist to be parsed. They also serve as labeled training "
         "data for the app's on-device i'rab model."),
  "tr": ("ÖZGÜN ders-kitabı tarzı alıştırma cümleleri; proje sahibinin verdiği "
         "soru-zinciri üslûbuyla (Gâle = dedi, kim? Zeydun…) editoryal olarak "
         "telif edilmiştir. Hiçbir cümle klasik bir metinden iktibas değildir; "
         "cümleler i'râb edilmek için vardır. Aynı zamanda uygulamanın cihaz "
         "içi i'râb modeline etiketli eğitim verisi sağlarlar."),
  "reviewStatus": "pending-scholarly-review"
 }
}

# ---- paradigms ------------------------------------------------------------
def copy_verbs():
    out = {}
    for lex, src in (("qala", "aqaid-ahl-al-sunna"), ("alima", "aqaid-ahl-al-sunna"),
                     ("dakhala", "aqaid-ahl-al-sunna"), ("kharaja", "aqaid-ahl-al-sunna"),
                     ("laysa", "aqaid-ahl-al-sunna"), ("qama", "aqaid-ahl-al-sunna"),
                     ("rajaa", "wasiyyat-abi-hanifa"), ("samia", "wasiyyat-abi-hanifa"),
                     ("jalasa", "wasiyyat-abi-hanifa"),
                     ("hafiza", "kitab-al-waqf"),
                     ("nasara", "wasiyyat-abi-hanifa-samti"),
                     ("talaba", "min-muqaddimat-al-maqsud"),
                     ("wajada", "kitab-al-kaffarat"),
                     ("kana", "aqaid-ahl-al-sunna"), ("sara", "bad-al-amali"),
                     ("ishtara", "kitab-al-buyu"),
                     ("jaa", "yunus-wa-al-hut")):
        verbs = json.loads((ROOT / "content/samples" / src / "morphology.json")
                           .read_text(encoding="utf-8"))["verbs"]
        out[lex] = verbs[lex]
    return out

MORPH = {"verbs": copy_verbs()}
MORPH["verbs"]["kataba"] = _sg.sound1(
    "nasara", "كَتَب", "كْتُب", "اُكْتُب", "كِتَابَة", "كَاتِب",
    "مَكْتُوب", "كُتِبَ", "يُكْتَبُ")
MORPH["verbs"]["qaraa"] = _sg.sound1(
    "fataha", "قَرَأ", "قْرَأ", "اِقْرَأ", "قِرَاءَة", "قَارِئ",
    "مَقْرُوء", "قُرِئَ", "يُقْرَأُ",
    note="مَهْمُوزُ اللَّامِ: تَثْبُتُ هَمْزَتُهُ فِي التَّصْرِيفِ — قَرَأْتُ، يَقْرَأُ.")
MORPH["verbs"]["shahida"] = _sg.sound1(
    "samia", "شَهِد", "شْهَد", "اِشْهَد", "شَهَادَة", "شَاهِد",
    "مَشْهُود", "شُهِدَ", "يُشْهَدُ")
MORPH["verbs"]["darasa"] = _sg.sound1(
    "nasara", "دَرَس", "دْرُس", "اُدْرُس", "دَرْس", "دَارِس",
    "مَدْرُوس", "دُرِسَ", "يُدْرَسُ")
MORPH["verbs"]["najaha"] = _sg.sound1(
    "fataha", "نَجَح", "نْجَح", "اِنْجَح", "نَجَاح", "نَاجِح")

ALL = S1 + S2 + S3 + S4 + S5 + S6 + S7

(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate((S1, S2, S3, S4, S5, S6, S7), 1):
    (PKG / f"chapters/{i}.json").write_text(
        json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")

used = set()
for s in ALL:
    for t in s["tokens"]:
        used.add(t["lex"])
        for sg2 in t.get("segments", []): used.add(sg2["lex"])
dead = set(GLOSS) - used
missing = used - set(GLOSS)
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL),
      "gloss:", len(GLOSS), "dead:", sorted(dead), "missing:", sorted(missing))
