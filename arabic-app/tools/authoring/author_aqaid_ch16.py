# -*- coding: utf-8 -*-
"""Author chapter 16 of aqaid-ahl-al-sunna — the best of mankind, and the order.

Continues the matn after the karamat: the best of mankind after our Prophet
is Abu Bakr al-Siddiq, then Umar al-Faruq, then Uthman Dhu al-Nurayn, then
Ali al-Murtada — and their caliphate ran in this same order.

DIVERGENCE, recorded in the manifest attribution: the supplied transcription
reads «عثمان ذي النورين», with the epithet in jarr. عُثْمَانُ here is a na't of
a marfu' chain running from أَفْضَلُ الْبَشَرِ, so the received grammatical
wording ذُو النُّورَيْنِ is used. The divergence is stated rather than silently
smoothed — the standing rule for this package.
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

TITLE16 = {"ar": "أَفْضَلُ الْبَشَرِ وَتَرْتِيبُ الْخِلَافَةِ",
           "en": "The Best of Mankind, and the Order of the Caliphate",
           "tr": "İnsanların En Faziletlisi ve Hilâfetin Sırası"}

S.append({"id": "s1", "translation": {
 "en": "And the best of mankind after our Prophet is Abu Bakr al-Siddiq,",
 "tr": "Peygamberimizden sonra insanların en faziletlisi Ebû Bekir es-Sıddîk'tir,"},
 "tokens": [
  tok("وَأَفْضَلُ","afdal","noun",["mubtada-khabar","ism-tafdil","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«أَفْضَلُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — اسْمُ تَفْضِيلٍ.",
      "Isti'naf waw; «the best» is the mubtada in raf' and a mudaf — an elative.",
      "İstinâf vâvı; «أَفْضَلُ» merfû mübtedâ ve muzâf — ism-i tafdîldir.",
      segments=[seg("وَ","wa","conj"), seg("أَفْضَلُ","afdal","noun")]),
  tok("الْبَشَرِ","bashar","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَإِضَافَةُ أَفْعَلِ التَّفْضِيلِ إِلَى الْجِنْسِ تُفِيدُ أَنَّهُ مِنْهُ.",
      "The mudaf ilayh in jarr — an elative joined to its KIND says the best is one OF them.",
      "Mecrûr muzâfun ileyh — ism-i tafdîlin cinse izâfeti, onun o cinsten olduğunu bildirir."),
  tok("بَعْدَ","bad","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«أَفْضَلُ».",
      "A time-adverb in nasb and a mudaf, attaching to «the best».",
      "Mansub zaman zarfı ve muzâf; «أَفْضَلُ»ye taalluk eder."),
  tok("نَبِيِّنَا","nabi","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ ثَانٍ.",
      "The mudaf ilayh in jarr, itself a mudaf; «na» is a second mudaf ilayh.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; «نَا» ikinci muzâfun ileyhtir.",
      segments=[seg("نَبِيِّ","nabi","noun"), seg("نَا","pron-1p","pron")]),
  tok("أَبُو","abubakr","propn",["mubtada-khabar","five-nouns","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ.",
      "The khabar in raf' by the WAW — one of the five nouns, and a mudaf.",
      "VÂV ile merfû haber — esmâ-i hamseden ve muzâftır."),
  tok("بَكْرٍ","abubakr","propn",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْعَلَمُ هُنَا مُرَكَّبٌ إِضَافِيٌّ، يُعْرَبُ صَدْرُهُ وَيُجَرُّ عَجُزُهُ.",
      "The mudaf ilayh in jarr — the name is an IDAFA compound: its head declines, its tail stays in jarr.",
      "Mecrûr muzâfun ileyh — alem, izâfî mürekkebdir: baş tarafı i'râb alır, sonu mecrûr kalır."),
  tok("الصِّدِّيقُ","siddiq","noun",["naat-sifa","sighat-mubalagha"],
      "نَعْتٌ لِـ«أَبُو» مَرْفُوعٌ بِالضَّمَّةِ — صِيغَةُ مُبَالَغَةٍ عَلَى فِعِّيلٍ.",
      "A na't of «Abu», in raf' by the damma — an intensive on the wazn فِعِّيل.",
      "«أَبُو»nun na'tı, damme ile merfû — fi''îl vezninde mübâlağa sîgası.", punct="،"),
 ],
 "jumal": [J("وَأَفْضَلُ الْبَشَرِ بَعْدَ نَبِيِّنَا أَبُو بَكْرٍ الصِّدِّيقُ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "then Umar al-Faruq, then Uthman Dhu al-Nurayn, then Ali al-Murtada.",
 "tr": "sonra Ömer el-Fârûk, sonra Osman Zü'n-nûreyn, sonra Ali el-Murtazâ."},
 "tokens": [
  tok("ثُمَّ","thumma","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَهُوَ هُنَا مَوْضِعُ الدَّلَالَةِ عَلَى التَّرْتِيبِ فِي الْفَضْلِ.",
      "A joining letter: in order, with an interval — and THAT is what carries the ranking here.",
      "Tertîb ve terâhî bildiren atıf harfi — buradaki fazilet sıralamasını taşıyan odur."),
  tok("عُمَرُ","umar","propn",["atf-nasaq","mamnu-min-sarf"],
      "مَعْطُوفٌ عَلَى «أَبُو» مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ عَنْ «عَامِر».",
      "Joined to «Abu», in raf' by a damma with NO tanwin — a diptote: a proper name TURNED ASIDE from عَامِر.",
      "«أَبُو»ya ma'tûf, tenvinsiz damme ile merfû — alemlik ve «عَامِر»den udûl sebebiyle gayr-i munsariftir."),
  tok("الْفَارُوقُ","faruq","noun",["naat-sifa","sighat-mubalagha"],
      "نَعْتٌ لِـ«عُمَرُ» مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَاعُولٍ، أَيِ الْفَارِقُ بَيْنَ الْحَقِّ وَالْبَاطِلِ.",
      "A na't of «Umar», in raf' — an intensive on فَاعُول: the one who parts truth from falsehood.",
      "«عُمَرُ»nun na'tı, merfû — fâ'ûl vezninde mübâlağa: hak ile bâtılı ayıran."),
  tok("ثُمَّ","thumma","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.",
      "A joining letter of order.",
      "Tertîb bildiren atıf harfi."),
  tok("عُثْمَانُ","uthman","propn",["atf-nasaq","mamnu-min-sarf"],
      "مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ.",
      "Joined, in raf' by a damma with no tanwin — a diptote: a proper name with the added alif and nun.",
      "Ma'tûf, tenvinsiz damme ile merfû — alemlik ve elif-nûn ziyâdesi sebebiyle gayr-i munsarif."),
  tok("ذُو","dhu","noun",["naat-sifa","five-nouns","idafa-definiteness"],
      "نَعْتٌ لِـ«عُثْمَانُ» مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ وَلَا يُسْتَعْمَلُ إِلَّا مُضَافًا.",
      "A na't of «Uthman», in raf' by the WAW — one of the five nouns, a mudaf, and it is NEVER used except as one.",
      "«عُثْمَانُ»un na'tı, VÂV ile merfû — esmâ-i hamseden, muzâftır ve ancak muzâf olarak kullanılır."),
  tok("النُّورَيْنِ","nur","noun",["idafa-definiteness","al-muthanna"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ — مُثَنًّى ثَبَتَتْ نُونُهُ، لِأَنَّ النُّونَ إِنَّمَا تُحْذَفُ مِنَ الْمُضَافِ لَا مِنَ الْمُضَافِ إِلَيْهِ.",
      "The mudaf ilayh, in jarr by the YA — a dual. Its nun STAYS: the nun drops from a dual that IS a mudaf, and this one is the mudaf ilayh.",
      "Mecrûr muzâfun ileyh, cer alâmeti YÂ — tesniyedir. Nûnu DURUR: nûn, muzâf olan tesniyeden düşer; bu ise muzâfun ileyhtir."),
  tok("ثُمَّ","thumma","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.",
      "A joining letter of order.",
      "Tertîb bildiren atıf harfi."),
  tok("عَلِيٌّ","ali","propn",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ مُنَوَّنٌ، فَلَيْسَ فِيهِ مَا يَمْنَعُ الصَّرْفَ.",
      "Joined, in raf' by the damma — and it KEEPS its tanwin: there is nothing in it to make it a diptote.",
      "Ma'tûf, damme ile merfû — tenvinlidir; onda sarfı men edecek bir şey yoktur."),
  tok("الْمُرْتَضَى","murtada","noun",["naat-sifa","ism-maful","form-viii-verbs","ism-maqsur-manqus"],
      "نَعْتٌ لِـ«عَلِيٌّ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمُ مَفْعُولٍ مِنِ «ارْتَضَى» النَّاقِصِ.",
      "A na't of «Ali», in raf' by a damma ESTIMATED on its alif — the ism maf'ul of the naqis اِرْتَضَى.",
      "«عَلِيٌّ»un na'tı, elifi üzerinde takdîrî damme ile merfû — nâkıs «ارْتَضَى»nın ism-i mef'ûlü.", punct="."),
 ],
 "jumal": [J("ثُمَّ عُمَرُ الْفَارُوقُ ثُمَّ عُثْمَانُ ذُو النُّورَيْنِ ثُمَّ عَلِيٌّ الْمُرْتَضَى",
   "مَعْطُوفَاتٌ عَلَى الْخَبَرِ — لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ إِذْ لَيْسَتْ بِجُمَلٍ.",
   "A chain joined to the khabar — not clauses, so no question of mahall arises.",
   "Habere ma'tûflar — cümle olmadıkları için mahal söz konusu değildir.")]})

S.append({"id": "s3", "translation": {
 "en": "And their caliphate ran in this same order.",
 "tr": "Hilâfetleri de bu sıra üzeredir."},
 "tokens": [
  tok("وَخِلَافَتُهُمْ","khilafa","noun",["mubtada-khabar","idafa-definiteness","masdar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«خِلَافَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Isti'naf waw; «their caliphate» is the mubtada in raf' and a mudaf; the ha is its mudaf ilayh.",
      "İstinâf vâvı; «خِلَافَةُ» merfû mübtedâ ve muzâf; hâ muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("خِلَافَتُ","khilafa","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ الْمُبْتَدَإِ.",
      "A jarr letter; the phrase is the khabar of the mubtada.",
      "Cer harfi; câr-mecrûr mübtedânın haberidir."),
  tok("هَذَا","hadha","pron",["ism-mawsul","huruf-jarr"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِـ«عَلَى».",
      "A demonstrative, fixed, in the position of jarr after «ala».",
      "İsm-i işâret — mebnî, «عَلَى» ile mahallen mecrûr."),
  tok("التَّرْتِيبِ","tartib","noun",["badal","form-ii-verbs","masdar"],
      "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ — مَصْدَرُ «رَتَّبَ»، وَالْبَدَلُ يَتْبَعُ الْمُبْدَلَ مِنْهُ فِي إِعْرَابِهِ.",
      "A badal of the demonstrative, in jarr — the masdar of رَتَّبَ; a badal takes the case of what it replaces.",
      "İsm-i işâretten mecrûr bedel — «رَتَّبَ»nin masdarı; bedel, mübdelün minhin i'râbına tâbi olur.", punct="."),
 ],
 "jumal": [J("وَخِلَافَتُهُمْ عَلَى هَذَا التَّرْتِيبِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "abubakr": g("أَبُو بَكْرٍ", None, "propn", "Abu Bakr", "Ebû Bekir", 1),
 "siddiq":  g("صِدِّيق", "ص د ق", "noun", "the utterly truthful (intensive)", "sıddîk; pek doğru", 3),
 "umar":    g("عُمَرُ", None, "propn", "Umar", "Ömer", 1),
 "faruq":   g("فَارُوق", "ف ر ق", "noun", "the one who parts truth from falsehood", "fârûk; hak ile bâtılı ayıran", 3),
 "uthman":  g("عُثْمَانُ", None, "propn", "Uthman", "Osman", 1),
 "dhu":     g("ذُو", None, "noun", "possessor of (one of the five nouns)", "sahibi (esmâ-i hamseden)", 2),
 "nur":     g("نُور", "ن و ر", "noun", "light", "nûr; ışık", 1),
 "ali":     g("عَلِيّ", "ع ل و", "propn", "Ali", "Ali", 1),
 "murtada": g("الْمُرْتَضَى", "ر ض و", "noun", "the well-pleasing one (ism maf'ul, Form VIII)", "murtazâ; kendisinden razı olunan", 4),
 "khilafa": g("خِلَافَة", "خ ل ف", "noun", "caliphate, succession (masdar)", "hilâfet (masdar)", 3),
 "hadha":   g("هَذَا", None, "pron", "this (masc.)", "bu (eril)", 1),
 "tartib":  g("تَرْتِيب", "ر ت ب", "noun", "order, arrangement (masdar, Form II)", "tertîb; sıra (masdar)", 3),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/16.json").write_text(json.dumps({"chapter": 16, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 16 for c in man["chapters"]):
    man["chapters"].append({"n": 16, "title": TITLE16})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.14.0"
NOTE = ("Ch16 divergence: the supplied transcription reads «عثمان ذي النورين» with "
        "the epithet in jarr; عُثْمَانُ stands in a marfu' chain of ma'tufat, so the "
        "received grammatical wording ذُو النُّورَيْنِ is used here.")
for lang in ("en", "tr"):
    if NOTE not in man["attribution"].get(lang, ""):
        man["attribution"][lang] = man["attribution"].get(lang, "") + " " + NOTE
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch16:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
