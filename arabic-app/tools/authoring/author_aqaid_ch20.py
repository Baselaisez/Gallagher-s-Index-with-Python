# -*- coding: utf-8 -*-
"""Author chapter 20 of aqaid-ahl-al-sunna — the last of the imam's offices.

Closes the enumeration chapter 19 left open: accepting the testimonies that
stand upon rights, marrying off the young who have no guardians, and dividing
the spoils. With this the matn's list is complete, so the chapter ENDS the span
rather than stopping early inside it.

Grammar this chapter is chosen to teach:
  • «الَّذِينَ لَا أَوْلِيَاءَ لَهُمْ» — a relative whose sila is itself a la-nafiya
    li-l-jins clause with an omitted khabar. Two engines meet in one phrase.
  • قَبُول on فَعُول as a MASDAR, not an intensive — the wazn wears more offices
    than the app knew, and this chapter is why it learned another.
  • الصَّغَائِر on فَعَائِل, the broken plural of a فَعِيلَة.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
sys.path.insert(0, str(ROOT / "tools/authoring"))
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

TITLE20 = {"ar": "تَمَامُ وَظَائِفِ الْإِمَامِ", "en": "The Last of the Imam's Offices",
           "tr": "İmâmın Vazîfelerinin Tamamı"}

def MATUF(what_ar, what_en, what_tr):
    return ("مَعْطُوفٌ عَلَى «تَنْفِيذِ» مَجْرُورٌ وَهُوَ مُضَافٌ — " + what_ar,
            "Joined to «the carrying-out», in jarr and a mudaf — " + what_en,
            "«تَنْفِيذِ»ye ma'tûf, mecrûr ve muzâf — " + what_tr)

S.append({"id": "s1", "translation": {
 "en": "and accepting the testimonies that stand upon rights,",
 "tr": "haklar üzerine kāim olan şehâdetleri kabul etmek,"},
 "tokens": [
  tok("وَقَبُولِ","qabul","noun",["atf-nasaq","masdar","idafa-definiteness"],
      *MATUF("مَصْدَرُ «قَبِلَ» عَلَى فَعُولٍ — وَفَعُولٌ يَأْتِي مَصْدَرًا كَمَا يَأْتِي صِيغَةَ مُبَالَغَةٍ.",
             "the masdar of قَبِلَ on فَعُول — and فَعُول comes as a MASDAR (قَبُول, وَضُوء, وَقُود) just as it comes as an intensive.",
             "«قَبِلَ»nin FAÛL vezninde masdarı — FAÛL, mübâlağa sîgası olduğu gibi MASDAR da olur (قَبُول, وَضُوء, وَقُود)."),
      segments=[seg("وَ","wa","conj"), seg("قَبُولِ","qabul","noun")]),
  tok("الشَّهَادَاتِ","shahada","noun",["jam-muannath-salim","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "The mudaf ilayh in jarr by the kasra — a sound feminine plural.",
      "Kesra ile mecrûr muzâfun ileyh — cemi müennes sâlim."),
  tok("الْقَائِمَةِ","qaim","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«الشَّهَادَاتِ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «قَامَ» عَلَى فَاعِلٍ، وَأَصْلُهُ قَاوِمٌ فَقُلِبَتِ الْوَاوُ هَمْزَةً لِوُقُوعِهَا بَعْدَ أَلِفِ فَاعِلٍ.",
      "A na't of «the testimonies», in jarr — the ism fa'il of قَامَ on فَاعِل. Its origin is قَاوِم: the waw turned HAMZA because it fell after the alif of فَاعِل.",
      "«الشَّهَادَاتِ»in na'tı, mecrûr — «قَامَ»nın FÂİL vezninde ism-i fâili. Aslı قَاوِم'dir: vâv, fâil elifinden sonra geldiği için HEMZEye kalbolmuştur."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«الْقَائِمَةِ».",
      "A jarr letter; the phrase attaches to «that stand».",
      "Cer harfi; câr-mecrûr «الْقَائِمَةِ»ye taalluk eder."),
  tok("الْحُقُوقِ","haqq","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — جَمْعُ «حَقٍّ» عَلَى فُعُولٍ.",
      "In jarr after «ala» by the kasra — the plural of «haqq» on فُعُول.",
      "«عَلَى» ile kesra üzere mecrûr — «حَقّ»ın FUÛL vezninde cemidir.", punct="،"),
 ],
 "jumal": [J("وَقَبُولِ الشَّهَادَاتِ الْقَائِمَةِ عَلَى الْحُقُوقِ",
   "مَعْطُوفٌ عَلَى «تَنْفِيذِ» — مُفْرَدَاتٌ لَا جُمَلٌ.",
   "Another ma'tuf on «the carrying-out» — single words, not clauses.",
   "«تَنْفِيذِ»ye ma'tûf — cümle değil müfredlerdir.")]})

S.append({"id": "s2", "translation": {
 "en": "and marrying off the young boys and girls who have no guardians,",
 "tr": "velîleri bulunmayan küçük erkek ve kız çocuklarını evlendirmek,"},
 "tokens": [
  tok("وَتَزْوِيجِ","tazwij","noun",["atf-nasaq","masdar","form-ii-verbs","idafa-definiteness"],
      *MATUF("مَصْدَرُ «زَوَّجَ» عَلَى تَفْعِيلٍ.", "the masdar of زَوَّجَ on تَفْعِيل.",
             "«زَوَّجَ»nin TEF'ÎL vezninde masdarı."),
      segments=[seg("وَ","wa","conj"), seg("تَزْوِيجِ","tazwij","noun")]),
  tok("الصِّغَارِ","saghir","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «صَغِيرٍ» عَلَى فِعَالٍ.",
      "The mudaf ilayh in jarr — the plural of «saghir», a small boy, on فِعَال.",
      "Mecrûr muzâfun ileyh — küçük demek olan «صَغِير»in FİÂL vezninde cemidir."),
  tok("وَالصَّغَائِرِ","saghira","noun",["atf-nasaq"],
      "مَعْطُوفٌ عَلَى «الصِّغَارِ» مَجْرُورٌ — جَمْعُ «صَغِيرَةٍ» عَلَى فَعَائِلَ، وَهُوَ مِنْ صِيَغِ مُنْتَهَى الْجُمُوعِ، وَإِنَّمَا انْصَرَفَ هُنَا لِدُخُولِ «أَلْ».",
      "Joined to «the boys», in jarr — the plural of «saghira» on فَعَائِل. That is one of the ultimate-plural patterns, barred from tanwin; the article is what lets a kasra sit on it here.",
      "«الصِّغَارِ»a ma'tûf, mecrûr — «صَغِيرَة»nin FAÂİL vezninde cemi. Sıygā-i müntehe'l-cumû'dandır ve gayr-i munsariftir; buradaki kesrayı mümkün kılan «أَلْ»dir.",
      segments=[seg("وَ","wa","conj"), seg("الصَّغَائِرِ","saghira","noun")]),
  tok("الَّذِينَ","alladhina","pron",["ism-mawsul","jumla-mutarida"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«الصِّغَارِ وَالصَّغَائِرِ».",
      "A relative noun, fixed in form, in the position of jarr as a na't of «the boys and girls».",
      "İsm-i mevsûl — mebnî, «الصِّغَارِ وَالصَّغَائِرِ»in na'tı olarak mahallen mecrûr."),
  tok("لَا","la-nafiya-lil-jins","part",["la-nafiya-lil-jins"],
      "نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ «إِنَّ».",
      "«la» denying the whole genus, governing as «inna» does.",
      "Cinsi nefyeden «lâ»; «إِنَّ» gibi amel eder."),
  tok("أَوْلِيَاءَ","wali","noun",["la-nafiya-lil-jins","mamnu-min-sarf"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — جَمْعُ «وَلِيٍّ» عَلَى أَفْعِلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.",
      "The ism of «la», built on the fatha and in the position of nasb — the plural of «wali» on أَفْعِلَاء, barred from tanwin by the extended alif of the feminine.",
      "«لَا»nın ismi, fetha üzere mebnî ve mahallen mansub — «وَلِيّ»in EF'İLÂ vezninde cemi; elif-i te'nîs-i memdûde sebebiyle gayr-i munsariftir."),
  tok("لَهُمْ","lahum","prep",["huruf-jarr","anwa-al-khabar"],
      "اللَّامُ حَرْفُ جَرٍّ وَ«هُمْ» فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ «لَا».",
      "The lam is a jarr letter and «hum» stands in jarr after it — and the phrase is the khabar of «la».",
      "Lâm cer harfi, «هُمْ» mahallen mecrûr — câr-mecrûr «لَا»nın haberidir.",
      punct="،", segments=[seg("لِ","lam-jarr","prep"), seg("هُمْ","pron-3mp","pron")]),
 ],
 "jumal": [J("لَا أَوْلِيَاءَ لَهُمْ",
   "جُمْلَةٌ اسْمِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal clause, the SILA of the relative — and a sila never has a position in i'rab.",
   "İsm-i mevsûlün SILAsı olan isim cümlesi — sıla cümlesinin i'râbda mahalli olmaz.")]})

S.append({"id": "s3", "translation": {
 "en": "and dividing the spoils.",
 "tr": "ganîmetleri taksim etmek."},
 "tokens": [
  tok("وَقِسْمَةِ","qisma","noun",["atf-nasaq","masdar","idafa-definiteness"],
      *MATUF("مَصْدَرُ «قَسَمَ» عَلَى فِعْلَةٍ، وَفِعْلَةٌ تَدُلُّ عَلَى الْهَيْئَةِ.",
             "the masdar of قَسَمَ on فِعْلَة — and فِعْلَة names the MANNER a thing is done in.",
             "«قَسَمَ»nin Fİ'LE vezninde masdarı — Fİ'LE, işin yapılış HEY'ETini bildirir."),
      segments=[seg("وَ","wa","conj"), seg("قِسْمَةِ","qisma","noun")]),
  tok("الْغَنَائِمِ","ghanima","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «غَنِيمَةٍ» عَلَى فَعَائِلَ، وَبِهَذَا تَمَّ عَدُّ مَا يَقُومُ بِهِ الْإِمَامُ.",
      "The mudaf ilayh in jarr — the plural of «ghanima» on فَعَائِل. With this the count of what the imam stands up to do is complete.",
      "Mecrûr muzâfun ileyh — «غَنِيمَة»nin FAÂİL vezninde cemi. Bununla imâmın kāim olduğu şeylerin sayımı tamamlanmış olur.", punct="."),
 ],
 "jumal": [J("وَقِسْمَةِ الْغَنَائِمِ",
   "آخِرُ الْمَعَاطِيفِ عَلَى «تَنْفِيذِ» — بِهِ تَمَّ التَّعْدَادُ.",
   "The last ma'tuf on «the carrying-out» — the enumeration ends here.",
   "«تَنْفِيذِ»ye son ma'tûf — sayım burada tamamlanır.")]})

GLOSS_ADD = {
 "qabul":     g("قَبُول", "ق ب ل", "noun", "accepting (masdar on فَعُول)", "kabul (FAÛL vezninde masdar)", 3),
 "shahada":   g("شَهَادَة", "ش ه د", "noun", "testimony", "şehâdet; tanıklık", 2, plural="شَهَادَات"),
 "tazwij":    g("تَزْوِيج", "ز و ج", "noun", "marrying off (masdar, Form II)", "tezvîc; evlendirme (masdar)", 4),
 "saghir":    g("صَغِير", "ص غ ر", "noun", "small; a young boy", "küçük; küçük erkek çocuk", 2, plural="صِغَار"),
 "saghira":   g("صَغِيرَة", "ص غ ر", "noun", "a young girl", "küçük kız çocuk", 2, plural="صَغَائِر"),
 "alladhina": g("الَّذِينَ", None, "pron", "those who (masc. plural relative)", "-ler ki (eril çoğul ism-i mevsûl)", 2),
 "lahum":     g("لَهُمْ", None, "prep", "for them, they have", "onlar için; onların vardır", 1),
 "qisma":     g("قِسْمَة", "ق س م", "noun", "dividing, apportioning (masdar)", "kısmet; taksim etme (masdar)", 3),
 "ghanima":   g("غَنِيمَة", "غ ن م", "noun", "spoils of war", "ganîmet", 3, plural="غَنَائِم"),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/20.json").write_text(
    json.dumps({"chapter": 20, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 20 for c in man["chapters"]):
    man["chapters"].append({"n": 20, "title": TITLE20})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.18.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch20:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
