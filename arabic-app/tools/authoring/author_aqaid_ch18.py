# -*- coding: utf-8 -*-
"""Author chapter 18 of aqaid-ahl-al-sunna — the term of the caliphate, and the
necessity of an imam.

Continues the matn where chapter 17 leaves the order of the four: the caliphate
proper is thirty years, and what follows it is kingship and emirate; and the
Muslims cannot do without an imam who carries out their rulings.

The span STOPS EARLY inside the matn's enumeration of the imam's offices — it
takes the first of them (تنفيذ الأحكام) and closes. That is allowed; skipping
from the middle is not.

Grammar this chapter is chosen to teach:
  • ثَلَاثُونَ سَنَةً — the 20–90 rule: the ma'dud is SINGULAR and MANSUB, a
    tamyiz, never a plural in jarr.
  • ثُمَّ بَعْدَهَا مُلْكٌ — a fronted zarf standing as khabar, with the mubtada
    held back behind it.
  • لَا بُدَّ … مِنْ — la denying the whole genus, its khabar omitted, and the
    disputed مِنْ named as disputed rather than settled by fiat.
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

TITLE18 = {"ar": "مُدَّةُ الْخِلَافَةِ وَلُزُومُ الْإِمَامِ",
           "en": "The Term of the Caliphate, and the Necessity of an Imam",
           "tr": "Hilâfetin Müddeti ve İmâmın Lüzûmu"}

S.append({"id": "s1", "translation": {
 "en": "And the caliphate is thirty years,",
 "tr": "Hilâfet otuz senedir,"},
 "tokens": [
  tok("وَالْخِلَافَةُ","khilafa","noun",["mubtada-khabar","masdar","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْخِلَافَةُ» مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — مَصْدَرُ «خَلَفَ».",
      "Isti'naf waw; «the caliphate» is the mubtada in raf' by the damma — the masdar of خَلَفَ.",
      "İstinâf vâvı; «الْخِلَافَةُ» damme ile merfû mübtedâdır — «خَلَفَ»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("الْخِلَافَةُ","khilafa","noun")]),
  tok("ثَلَاثُونَ","thalathun","noun",["jam-mudhakkar-salim","tamyiz","mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.",
      "The khabar in raf', and the sign of its raf' is the WAW — it is annexed to the sound masculine plural (it takes that plural's endings without being one).",
      "VÂV ile merfû haber — cemi müzekker sâlime MÜLHAKtır (o cemin i'râbını alır, kendisi ondan değildir)."),
  tok("سَنَةً","sana","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — وَمَعْدُودُ الْعُقُودِ مِنْ عِشْرِينَ إِلَى تِسْعِينَ مُفْرَدٌ مَنْصُوبٌ أَبَدًا.",
      "A TAMYIZ in nasb by the fatha — from twenty to ninety the counted noun is SINGULAR and MANSUB, always: thirty YEAR, never thirty of years.",
      "Fetha ile mansub TEMYÎZ — yirmiden doksana kadar ma'dûd dâimâ MÜFRED ve MANSUBdur: otuz SENE, «senelerden otuz» değil.", punct="،"),
 ],
 "jumal": [J("وَالْخِلَافَةُ ثَلَاثُونَ سَنَةً",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "then after it comes kingship and emirate.",
 "tr": "ondan sonrası mülk ve emirliktir."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ مَعَ التَّرَاخِي.",
      "A letter of atf giving sequence WITH an interval — not the immediate following of fa.",
      "Tertîb ile birlikte TERÂHÎ (araya zaman girmesi) ifade eden atıf harfi — «fâ»nın peşpeşeliği değildir."),
  tok("بَعْدَهَا","bad","noun",["maful-fih","idafa-definiteness","mubtada-khabar"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«هَا» مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرٌ مُقَدَّمٌ.",
      "A time-adverb in nasb and a mudaf, «ha» its mudaf ilayh — and the adverb stands as a FRONTED khabar.",
      "Mansub zaman zarfı ve muzâf, «هَا» muzâfun ileyh — zarf, MUKADDEM haberdir.",
      segments=[seg("بَعْدَ","bad","noun"), seg("هَا","pron-3fs","pron")]),
  tok("مُلْكٌ","mulk","noun",["mubtada-khabar","masdar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَسَاغَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الظَّرْفِ عَلَيْهَا.",
      "The HELD-BACK mubtada, in raf' by the damma — an indefinite may open a clause once the adverb has gone in front of it.",
      "Damme ile merfû MUAHHAR mübtedâ — zarf öne geçtiği için nekre ile ibtidâ câiz olmuştur."),
  tok("وَإِمَارَةٌ","imara","noun",["atf-nasaq","masdar"],
      "مَعْطُوفٌ عَلَى «مُلْكٌ» مَرْفُوعٌ — وَالْمَعْطُوفُ يَتْبَعُ الْمَعْطُوفَ عَلَيْهِ فِي إِعْرَابِهِ.",
      "Joined to «kingship», in raf' — what is joined takes the case of what it is joined to.",
      "«مُلْكٌ»a ma'tûf, merfû — ma'tûf, ma'tûfun aleyhin i'râbına tâbidir.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("إِمَارَةٌ","imara","noun")]),
 ],
 "jumal": [J("ثُمَّ بَعْدَهَا مُلْكٌ وَإِمَارَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا — لَا مَحَلَّ لَهَا.",
   "A nominal clause joined to the one before it — i'rabless.",
   "Öncesine ma'tûf isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the Muslims cannot do without an imam who carries out their rulings —",
 "tr": "Müslümanların, hükümlerini infâz edecek bir imâma ihtiyâcı zarûrîdir —"},
 "tokens": [
  tok("وَلَا","la-nafiya-lil-jins","part",["la-nafiya-lil-jins"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَا» نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ «إِنَّ».",
      "Isti'naf waw; «la» denies the WHOLE GENUS and governs as «inna» does — its ism in nasb, its khabar in raf'.",
      "İstinâf vâvı; «لَا» CİNSİ nefyeder ve «إِنَّ» gibi amel eder — ismi mansub, haberi merfûdur.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya-lil-jins","part")]),
  tok("بُدَّ","budd","noun",["la-nafiya-lil-jins","anwa-al-khabar"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ تَقْدِيرُهُ «مَوْجُودٌ».",
      "The ism of «la», BUILT on the fatha and in the position of nasb; its khabar is OMITTED — understood as «there is».",
      "«لَا»nın ismi, fetha üzere MEBNÎ ve mahallen mansub; haberi MAHZÛFtur, takdîri «mevcûddur»."),
  tok("لِلْمُسْلِمِينَ","muslim","noun",["huruf-jarr","jam-mudhakkar-salim"],
      "اللَّامُ حَرْفُ جَرٍّ، وَ«الْمُسْلِمِينَ» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "The lam is a jarr letter; «the Muslims» is in jarr by the YA, being a sound masculine plural.",
      "Lâm cer harfidir; «الْمُسْلِمِينَ» cemi müzekker sâlim olduğu için YÂ ile mecrûrdur.",
      segments=[seg("لِ","lam-jarr","prep"), seg("الْمُسْلِمِينَ","muslim","noun")]),
  tok("مِنْ","min","prep",["huruf-jarr","huruf-jarr-nawadir"],
      "حَرْفُ جَرٍّ، وَقَدِ اخْتُلِفَ فِيهِ هُنَا: قِيلَ زَائِدٌ لِتَأْكِيدِ النَّفْيِ، وَقِيلَ لِلتَّبْعِيضِ.",
      "A jarr letter — and grammarians DIFFER over this one: some read it as extra, strengthening the negation; others as partitive. The app states the disagreement rather than settling it.",
      "Cer harfi — burada İHTİLÂF vardır: kimi nefyi te'kîd için ZÂİD sayar, kimi TEB'ÎZ içindir der. Uygulama ihtilâfı kendi kararıyla kapatmaz, olduğu gibi bildirir."),
  tok("إِمَامٍ","imam","noun",["huruf-jarr","naat-sifa"],
      "مَجْرُورٌ بِـ«مِنْ» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ نَكِرَةٌ مَوْصُوفَةٌ بِمَا بَعْدَهَا.",
      "In jarr after «min» by the kasra — an INDEFINITE, and what follows describes it.",
      "«مِنْ» ile kesra üzere mecrûr — NEKREdir ve sonrası onu vasfeder."),
  tok("يَقُومُ","qama","verb",["mudari-marfu","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«إِمَامٍ».",
      "A mudari' in raf' because nothing governs it; its fa'il is a hidden «he» — and the CLAUSE stands in the position of jarr as a na't of «an imam». A clause describing an indefinite is a na't; describing a definite it would be a hal.",
      "Nâsıb ve câzimden hâlî olduğu için merfû muzâri; fâili müstetir «هُوَ» zamîridir — CÜMLE, «إِمَامٍ»in na'tı olarak mahallen mecrûrdur. Nekreyi vasfeden cümle na't, marifeyi vasfeden hâl olur."),
  tok("بِتَنْفِيذِ","tanfidh","noun",["huruf-jarr","masdar","form-ii-verbs","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«تَنْفِيذِ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «نَفَّذَ» عَلَى تَفْعِيلٍ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَقُومُ».",
      "The ba is a jarr letter; «the carrying-out» is in jarr and a mudaf — the masdar of نَفَّذَ on تَفْعِيل, and the phrase attaches to «carries out».",
      "Bâ cer harfidir; «تَنْفِيذِ» mecrûr ve muzâftır — «نَفَّذَ»nin TEF'ÎL vezninde masdarı; câr-mecrûr «يَقُومُ»ya taalluk eder.",
      segments=[seg("بِ","ba","prep"), seg("تَنْفِيذِ","tanfidh","noun")]),
  tok("أَحْكَامِهِمْ","hukm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَ«هِمْ» مُضَافٌ إِلَيْهِ ثَانٍ — وَ«أَحْكَام» جَمْعُ تَكْسِيرٍ لِـ«حُكْم».",
      "The mudaf ilayh in jarr, itself a mudaf; «him» is a second mudaf ilayh — «ahkam» is the broken plural of «hukm».",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; «هِمْ» ikinci muzâfun ileyhtir — «أَحْكَام», «حُكْم»ün cemi teksîridir.",
      punct="—", segments=[seg("أَحْكَامِ","hukm","noun"), seg("هِمْ","pron-3mp","pron")]),
 ],
 "jumal": [J("وَلَا بُدَّ لِلْمُسْلِمِينَ مِنْ إِمَامٍ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir."),
  J("يَقُومُ بِتَنْفِيذِ أَحْكَامِهِمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«إِمَامٍ».",
   "A verbal clause in the position of jarr, a na't of «an imam».",
   "«إِمَامٍ»in na'tı olarak mahallen mecrûr fiil cümlesi.")]})

GLOSS_ADD = {
 "thalathun": g("ثَلَاثُونَ", "ث ل ث", "noun", "thirty", "otuz", 2),
 "sana":      g("سَنَة", "س ن و", "noun", "year", "sene, yıl", 1, plural="سِنُونَ / سَنَوَات"),
 "mulk":      g("مُلْك", "م ل ك", "noun", "kingship, dominion", "mülk; saltanat", 3),
 "imara":     g("إِمَارَة", "أ م ر", "noun", "emirate, command", "emirlik, emâret", 3),
 "budd":      g("بُدّ", "ب د د", "noun", "escape, doing-without (used only after لا)", "çare; kaçınma (yalnız «lâ» ile kullanılır)", 4),
 "muslim":    g("مُسْلِم", "س ل م", "noun", "a Muslim (ism fa'il of أَسْلَمَ)", "müslüman («أَسْلَمَ»nin ism-i fâili)", 1, plural="مُسْلِمُونَ"),
 "imam":      g("إِمَام", "أ م م", "noun", "imam, leader", "imam; önder", 2, plural="أَئِمَّة"),
 "tanfidh":   g("تَنْفِيذ", "ن ف ذ", "noun", "carrying out, execution (masdar, Form II)", "infâz; yerine getirme (masdar)", 4),
 "lam-jarr":  g("لِ", None, "prep", "for, to (jarr letter)", "için, -e (cer harfi)", 1),
 "ba":        g("بِ", None, "prep", "by, with (jarr letter)", "ile, -e (cer harfi)", 1),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/18.json").write_text(
    json.dumps({"chapter": 18, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 18 for c in man["chapters"]):
    man["chapters"].append({"n": 18, "title": TITLE18})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.16.0"
NOTE = ("Ch18: «مِنْ» in «لا بد … من إمام» is recorded as disputed — extra (za'ida, "
        "strengthening the negation) or partitive — rather than settled one way in the i'rab.")
for lang in ("en", "tr"):
    if NOTE not in man["attribution"].get(lang, ""):
        man["attribution"][lang] = man["attribution"].get(lang, "") + " " + NOTE
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch18:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
