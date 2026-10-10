# -*- coding: utf-8 -*-
"""Author chapter 16 of aqaid-ahl-al-sunna — why a karama proves a messenger.

Closes the karamat argument that chapter 15 opened, and it belongs HERE: an
earlier pass jumped from «لواحد من أمته» straight to «وأفضل البشر», leaving
this passage out of the story altogether. The chapter numbers were shifted so
the matn runs in its own order — the caliphs are chapter 17 now.

The argument: because the karama makes plain that the man is a friend of
Allah; and he will not be a friend unless he is truthful in his religion; and
his religion is the profession of the messengership of His Messenger.

Verbatim contiguous span, re-vowelled against the received text.
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

TITLE16 = {"ar": "لِمَ كَانَتِ الْكَرَامَةُ مُعْجِزَةً",
           "en": "Why a Karama Proves a Messenger",
           "tr": "Kerâmet Niçin Mu'cizedir"}

S.append({"id": "s1", "translation": {
 "en": "because it makes plain, through her, that he is a friend of Allah;",
 "tr": "çünkü onunla, kendisinin velî olduğu zâhir olur;"},
 "tokens": [
  tok("لِأَنَّهُ","inna","part",["inna-wa-akhawatuha","inna-am-anna","lam-taleel"],
      "اللَّامُ لِلتَّعْلِيلِ، وَ«أَنَّ» حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ — وَفُتِحَتْ هَمْزَتُهَا لِأَنَّهَا مَعَ مَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِاللَّامِ.",
      "The lam gives the REASON; «anna» is a particle like a verb and the ha is its ism, in the position of nasb — and its hamza takes a FATHA because the clause is read as a masdar in jarr after that lam.",
      "Lâm ta'lîl içindir; «أَنَّ» fiile benzeyen harftir, hâ mahallen mansub ismidir — hemzesi FETHALIDIR, zira sonrasıyla birlikte lâm ile mecrûr bir masdar te'vilindedir.",
      segments=[seg("لِ","li","prep"), seg("أَنَّ","inna","part"), seg("هُ","pron-3ms","pron")]),
  tok("يَظْهَرُ","zahara","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "A mudari in raf' by the damma.",
      "Damme ile merfû muzâri."),
  tok("بِهَا","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَظْهَرُ»، وَ«هَا» يَعُودُ عَلَى الْكَرَامَةِ.",
      "A jarr phrase attaching to «becomes plain»; the «ha» returns to the karama.",
      "«يَظْهَرُ»ye taalluk eden câr-mecrûr; «هَا» kerâmete döner.",
      segments=[seg("بِ","bi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("أَنَّهُ","inna","part",["inna-wa-akhawatuha","inna-am-anna","an-masdariyya"],
      "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنْ خَبَرِهَا فَاعِلُ «يَظْهَرُ».",
      "A particle like a verb, the ha its ism — and the masdar read out of it and its khabar is the FA'IL of «becomes plain»: what becomes plain is his being a wali.",
      "Fiile benzeyen harf, hâ ismidir — ondan ve haberinden anlaşılan müevvel masdar, «يَظْهَرُ»in FÂİLİDİR: zâhir olan, onun velî oluşudur.",
      segments=[seg("أَنَّ","inna","part"), seg("هُ","pron-3ms","pron")]),
  tok("وَلِيٌّ","wali","noun",["inna-wa-akhawatuha"],
      "خَبَرُ «أَنَّ» مَرْفُوعٌ بِالضَّمَّةِ.",
      "The khabar of «anna», in raf' by the damma.",
      "«أَنَّ»nin damme ile merfû haberi.", punct="،"),
 ],
 "jumal": [J("لِأَنَّهُ يَظْهَرُ بِهَا أَنَّهُ وَلِيٌّ",
   "الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» وَمَا بَعْدَهَا مَجْرُورٌ بِلَامِ التَّعْلِيلِ — تَعْلِيلٌ لِمَا قَبْلَهُ.",
   "The masdar read out of «anna» and what follows it is in jarr after the lam of cause — it gives the reason for what came before.",
   "«أَنَّ» ve sonrasından anlaşılan müevvel masdar, ta'lîl lâmıyla mecrûrdur — öncesinin sebebini bildirir.")]})

S.append({"id": "s2", "translation": {
 "en": "and he will never be a friend of Allah except that he be truthful in his religion;",
 "tr": "ve o, dininde muhik olmadıkça asla velî olmaz;"},
 "tokens": [
  tok("وَلَنْ","lan","part",["mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَنْ» حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ — تَنْفِي الْمُسْتَقْبَلَ نَفْيًا مُؤَكَّدًا.",
      "Joining waw; «lan» negates, puts the verb in nasb, and throws it into the future — an emphatic never.",
      "Atıf vâvı; «لَنْ» nefiy, nasb ve istikbâl harfidir — geleceği te'kidli olarak nefyeder.",
      segments=[seg("وَ","wa","conj"), seg("لَنْ","lan","part")]),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«لَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَاسْمُهُ مُسْتَتِرٌ «هُوَ».",
      "A defective mudari in nasb by «lan», the fatha its sign; its ism is hidden, «he».",
      "«لَنْ» ile mansub nâkıs muzâri, alâmeti fetha; ismi müstetir «o»."),
  tok("وَلِيًّا","wali","noun",["kana-wa-akhawatuha"],
      "خَبَرُ «يَكُونَ» مَنْصُوبٌ بِالْفَتْحَةِ.",
      "The khabar of «he be», in nasb by the fatha.",
      "«يَكُونَ»nin fetha ile mansub haberi."),
  tok("إِلَّا","illa","part",["istithna"],
      "أَدَاةُ اسْتِثْنَاءٍ — وَالِاسْتِثْنَاءُ هُنَا مُفَرَّغٌ، إِذْ سُبِقَتْ بِنَفْيٍ.",
      "A particle of exception — and the exception is MUFARRAGH here, since a negation came first.",
      "İstisnâ edatı — nefiy geçtiği için istisnâ mufarragdır."),
  tok("وَأَنْ","an-masdariyya","part",["an-masdariyya","inna-am-anna"],
      "الْوَاوُ زَائِدَةٌ لِلتَّأْكِيدِ، وَ«أَنْ» حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَهَمْزَتُهَا مَفْتُوحَةٌ سَاكِنَةُ النُّونِ، فَهِيَ الْمَصْدَرِيَّةُ لَا «أَنَّ».",
      "The waw is extra, for emphasis; «an» is the masdar-maker that puts the verb in nasb — its nun is QUIESCENT, so this is the masdar an, not «anna».",
      "Vâv te'kid için zâiddir; «أَنْ» nasbeden masdar harfidir — nûnu SÂKİNDİR, yani «أَنَّ» değil masdariyyedir.",
      segments=[seg("وَ","wa","conj"), seg("أَنْ","an-masdariyya","part")]),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","hollow-verbs","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ»، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ عَلَى الِاسْتِثْنَاءِ.",
      "A defective mudari in nasb by «an»; the masdar read out of it stands in the position of nasb as the exception.",
      "«أَنْ» ile mansub nâkıs muzâri; müevvel masdar, istisnâ üzere mahallen mansubdur."),
  tok("مُحِقًّا","muhiqq","noun",["kana-wa-akhawatuha","ism-fail","form-iv-verbs","doubled-verbs"],
      "خَبَرُ «يَكُونَ» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «أَحَقَّ» الْمُضَاعَفِ، أَيْ صَاحِبُ حَقٍّ.",
      "The khabar of «he be», in nasb — the ism fa'il of the doubled أَحَقَّ: one who holds the truth.",
      "«يَكُونَ»nin mansub haberi — muzâaf «أَحَقَّ»nin ism-i fâili; hak sahibi."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("دِيَانَتِهِ","diyana","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr by the kasra and a mudaf; the ha is its mudaf ilayh.",
      "Kesra ile mecrur ve muzâf; hâ muzâfun ileyhtir.",
      segments=[seg("دِيَانَتِ","diyana","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
 ],
 "jumal": [J("وَلَنْ يَكُونَ وَلِيًّا إِلَّا وَأَنْ يَكُونَ مُحِقًّا فِي دِيَانَتِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "and his religion is the profession of the messengership of His Messenger.",
 "tr": "Dini ise, Resûlünün risâletini ikrar etmektir."},
 "tokens": [
  tok("وَدِيَانَتُهُ","diyana","noun",["mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«دِيَانَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Isti'naf waw; «his religion» is the mubtada in raf' and a mudaf; the ha is its mudaf ilayh.",
      "İstinâf vâvı; «دِيَانَةُ» merfû mübtedâ ve muzâf; hâ muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("دِيَانَتُ","diyana","noun"), seg("هُ","pron-3ms","pron")]),
  tok("الْإِقْرَارُ","iqrar","noun",["mubtada-khabar","form-iv-verbs","masdar"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — مَصْدَرُ «أَقَرَّ» عَلَى إِفْعَالٍ.",
      "The khabar in raf' by the damma — the masdar of أَقَرَّ on إِفْعَال.",
      "Damme ile merfû haber — if'âl vezninde «أَقَرَّ» masdarı."),
  tok("بِرِسَالَةِ","risala","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«رِسَالَةِ» مَجْرُورٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«الْإِقْرَارُ».",
      "The ba is a jarr letter; «messengership» is in jarr and a mudaf, attaching to «the profession».",
      "Bâ cer harfi; «رِسَالَةِ» mecrur ve muzâf, «الْإِقْرَارُ»a taalluk eder.",
      segments=[seg("بِ","bi","prep"), seg("رِسَالَةِ","risala","noun")]),
  tok("رَسُولِهِ","rasul","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ ثَانٍ يَعُودُ عَلَى اللهِ.",
      "The mudaf ilayh in jarr, itself a mudaf; the ha is a second mudaf ilayh, returning to Allah.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; hâ, Allah'a dönen ikinci muzâfun ileyhtir.",
      segments=[seg("رَسُولِ","rasul","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("وَدِيَانَتُهُ الْإِقْرَارُ بِرِسَالَةِ رَسُولِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "lan":    g("لَنْ", None, "part", "never (negates the future, governs nasb)", "asla (istikbâli nefyeder, nasbeder)", 2),
 "muhiqq": g("مُحِقّ", "ح ق ق", "noun", "one who holds the truth", "muhik; hak sahibi", 4),
 "diyana": g("دِيَانَة", "د ي ن", "noun", "religion, religious profession", "diyânet; din", 3),
 "iqrar":  g("إِقْرَار", "ق ر ر", "noun", "profession, acknowledgement (masdar, Form IV)", "ikrâr (masdar)", 3),
 "risala": g("رِسَالَة", "ر س ل", "noun", "messengership", "risâlet; elçilik", 3),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/16.json").write_text(json.dumps({"chapter": 16, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 16 for c in man["chapters"]):
    man["chapters"].append({"n": 16, "title": TITLE16})
man["chapters"].sort(key=lambda c: c["n"])
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch16:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
