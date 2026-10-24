# -*- coding: utf-8 -*-
"""Author chapter 23 of aqaid-ahl-al-sunna — knowing, and able.

Completes chapter 22's list of what the imamate does require: that he be
knowing in governance and in setting up the hudud, able to defend the frontier
of Islam and to get the wronged their due from the wrongdoer.

This chapter is the package's densest run of TA'ALLUQ, which is why it was
written alongside the engine that reads it. Four jarr-majrurs hang off four
different kinds of governor, and between them they cover the whole rule:
  • بِالسِّيَاسَةِ  → عَالِمًا      an ism fa'il governs like its verb
  • عَلَى الذَّبِّ  → قَادِرًا      so does another
  • عَنْ حَوْزَةِ   → الذَّبِّ      and a MASDAR governs like its verb too
  • مِنَ الظَّالِمِ → إِنْصَافِ     …even when the masdar is itself a mudaf
Ibn Hisham's rule in Qawa'id al-I'rab bab 2 is that every jarr-majrur attaches
to a verb or to something carrying a verb's meaning. These four are what that
sentence looks like on the page.
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

TITLE23 = {"ar": "عَالِمًا قَادِرًا", "en": "Knowing, and Able",
           "tr": "Bilen ve Muktedir Olması"}

S.append({"id": "s1", "translation": {
 "en": "knowing in governance and in the setting up of the hudud,",
 "tr": "siyâseti ve hadleri ikāme etmeyi bilen,"},
 "tokens": [
  tok("عَالِمًا","alim","noun",["ism-fail","hal"],
      "حَالٌ مَنْصُوبٌ مِنَ الضَّمِيرِ فِي «يَكُونَ» — اسْمُ فَاعِلٍ، وَهُوَ يَعْمَلُ عَمَلَ فِعْلِهِ فَيَتَعَلَّقُ بِهِ الْجَارُّ بَعْدَهُ.",
      "A hal in nasb from the pronoun inside «yakuna» — an ism fa'il, and an ism fa'il GOVERNS as its verb does, which is why the jarr after it attaches to it.",
      "«يَكُونَ»deki zamîrden mansub hâl — ism-i fâildir; ism-i fâil kendi fiili gibi amel eder, bu yüzden sonrasındaki câr ona taalluk eder."),
  tok("بِالسِّيَاسَةِ","siyasa","noun",["huruf-jarr"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«عَالِمًا».",
      "The ba is a jarr letter; the phrase ATTACHES to «knowing».",
      "Bâ cer harfidir; câr-mecrûr «عَالِمًا»ya TAALLUK eder.",
      segments=[seg("بِ","ba","prep"), seg("السِّيَاسَةِ","siyasa","noun")]),
  tok("وَإِقَامَةِ","iqama","noun",["atf-nasaq","masdar","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «السِّيَاسَةِ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «أَقَامَ».",
      "Joined to «governance», in jarr and a mudaf — the masdar of أَقَامَ.",
      "«السِّيَاسَةِ»ye ma'tûf, mecrûr ve muzâf — «أَقَامَ»nın masdarı.",
      segments=[seg("وَ","wa","conj"), seg("إِقَامَةِ","iqama","noun")]),
  tok("الْحُدُودِ","hadd","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ مَفْعُولٌ بِهِ فِي الْمَعْنَى لِلْمَصْدَرِ قَبْلَهُ.",
      "The mudaf ilayh in jarr — and in MEANING it is the object of the masdar before it: a masdar keeps its verb's appetite for an object.",
      "Mecrûr muzâfun ileyh — MÂNÂ bakımından öncesindeki masdarın mef'ûlüdür: masdar, fiilinin mef'ûl isteğini korur.", punct="،"),
 ],
 "jumal": [J("عَالِمًا بِالسِّيَاسَةِ وَإِقَامَةِ الْحُدُودِ",
   "حَالٌ مُفْرَدٌ مَنْصُوبٌ — لَا جُمْلَةَ فَلَا مَحَلَّ يُسْأَلُ عَنْهُ.",
   "A single-word hal in nasb — not a clause, so the question of a clause's position does not arise.",
   "Müfred mansub hâl — cümle değildir, dolayısıyla cümle mahalli sorusu sorulmaz.")]})

S.append({"id": "s2", "translation": {
 "en": "able to defend the frontier of Islam,",
 "tr": "İslâm'ın sınırını müdâfaaya muktedir,"},
 "tokens": [
  tok("قَادِرًا","qadir","noun",["ism-fail","atf-nasaq","hal"],
      "مَعْطُوفٌ عَلَى «عَالِمًا» مَنْصُوبٌ — اسْمُ فَاعِلٍ يَعْمَلُ عَمَلَ فِعْلِهِ.",
      "Joined to «knowing», in nasb — another ism fa'il, governing as its verb does.",
      "«عَالِمًا»ya ma'tûf, mansub — yine kendi fiili gibi amel eden bir ism-i fâil."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«قَادِرًا».",
      "A jarr letter; the phrase ATTACHES to «able».",
      "Cer harfi; câr-mecrûr «قَادِرًا»ya TAALLUK eder."),
  tok("الذَّبِّ","dhabb","noun",["masdar","huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» — مَصْدَرُ «ذَبَّ»، وَهُوَ بِدَوْرِهِ يَعْمَلُ فَيَتَعَلَّقُ بِهِ مَا بَعْدَهُ.",
      "In jarr after «ala» — the masdar of ذَبَّ, and a masdar governs in its turn, so what comes next attaches to IT rather than reaching back past it.",
      "«عَلَى» ile mecrûr — «ذَبَّ»nin masdarıdır; masdar da kendi sırasında amel eder, bu yüzden sonrası geriye uzanmaz, ONA taalluk eder."),
  tok("عَنْ","an-prep","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِالْمَصْدَرِ «الذَّبِّ» لَا بِـ«قَادِرًا» — لِأَنَّ الْأَقْرَبَ أَوْلَى بِالتَّعَلُّقِ.",
      "A jarr letter; this phrase attaches to the MASDAR «the defending», not back to «able» — the nearer governor has the better claim.",
      "Cer harfi; bu câr-mecrûr «قَادِرًا»ya değil, MASDAR olan «الذَّبِّ»e taalluk eder — taallukta en yakın âmil evlâdır."),
  tok("حَوْزَةِ","hawza","noun",["idafa-definiteness","huruf-jarr"],
      "مَجْرُورٌ بِـ«عَنْ» وَهُوَ مُضَافٌ.",
      "In jarr after «an», and a mudaf.",
      "«عَنْ» ile mecrûr ve muzâftır."),
  tok("الْإِسْلَامِ","islam","noun",["idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «أَسْلَمَ» عَلَى إِفْعَالٍ.",
      "The mudaf ilayh in jarr — the masdar of أَسْلَمَ on إِفْعَال.",
      "Mecrûr muzâfun ileyh — «أَسْلَمَ»nin İF'ÂL vezninde masdarı.", punct="،"),
 ],
 "jumal": [J("قَادِرًا عَلَى الذَّبِّ عَنْ حَوْزَةِ الْإِسْلَامِ",
   "حَالٌ مَعْطُوفٌ مَنْصُوبٌ — مُفْرَدٌ لَا جُمْلَةٌ.",
   "A joined hal in nasb — a single word, not a clause.",
   "Ma'tûf mansub hâl — cümle değil müfreddir.")]})

S.append({"id": "s3", "translation": {
 "en": "and to get the wronged his due from the wrongdoer.",
 "tr": "ve mazlûmun hakkını zâlimden almaya muktedir."},
 "tokens": [
  tok("وَإِنْصَافِ","insaf","noun",["atf-nasaq","masdar","form-iv-verbs","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الذَّبِّ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «أَنْصَفَ» عَلَى إِفْعَالٍ.",
      "Joined to «the defending», in jarr and a mudaf — the masdar of أَنْصَفَ on إِفْعَال.",
      "«الذَّبِّ»e ma'tûf, mecrûr ve muzâf — «أَنْصَفَ»nin İF'ÂL vezninde masdarı.",
      segments=[seg("وَ","wa","conj"), seg("إِنْصَافِ","insaf","noun")]),
  tok("الْمَظْلُومِ","mazlum","noun",["ism-maful","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ «ظَلَمَ»، وَهُوَ مَفْعُولٌ فِي الْمَعْنَى لِلْمَصْدَرِ.",
      "The mudaf ilayh in jarr — the ism maf'ul of ظَلَمَ, and in meaning the object of the masdar.",
      "Mecrûr muzâfun ileyh — «ظَلَمَ»nin ism-i mef'ûlü; mânâ bakımından masdarın mef'ûlüdür."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِالْمَصْدَرِ «إِنْصَافِ».",
      "A jarr letter; the phrase ATTACHES to the masdar «getting-his-due».",
      "Cer harfi; câr-mecrûr, MASDAR olan «إِنْصَافِ»a taalluk eder."),
  tok("الظَّالِمِ","zalim","noun",["ism-fail","huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ» — اسْمُ فَاعِلٍ مِنْ «ظَلَمَ»، وَبِهِ تَمَّ ذِكْرُ الشُّرُوطِ.",
      "In jarr after «min» — the ism fa'il of ظَلَمَ, and with it the conditions are complete.",
      "«مِنْ» ile mecrûr — «ظَلَمَ»nin ism-i fâili; şartların sayımı bununla tamamlanır.", punct="."),
 ],
 "jumal": [J("وَإِنْصَافِ الْمَظْلُومِ مِنَ الظَّالِمِ",
   "مَعْطُوفٌ عَلَى الْمَجْرُورِ قَبْلَهُ — مُفْرَدٌ لَا جُمْلَةٌ.",
   "Joined to the majrur before it — a single word, not a clause.",
   "Öncesindeki mecrûra ma'tûf — cümle değil müfred.")]})

GLOSS_ADD = {
 "siyasa":   g("سِيَاسَة", "س و س", "noun", "governance, management of affairs", "siyâset; işleri idare", 4),
 "dhabb":    g("ذَبّ", "ذ ب ب", "noun", "defending, warding off (masdar)", "def'; müdâfaa (masdar)", 4),
 "hawza":    g("حَوْزَة", "ح و ز", "noun", "domain, frontier held", "havza; elde tutulan bölge", 5),
 "islam":    g("إِسْلَام", "س ل م", "noun", "Islam; submitting (masdar, Form IV)", "İslâm; teslim olma (masdar)", 1),
 "insaf":    g("إِنْصَاف", "ن ص ف", "noun", "getting one his due, doing justice (masdar, Form IV)", "insâf; hakkını verme (masdar)", 4),
 "mazlum":   g("مَظْلُوم", "ظ ل م", "noun", "one wronged (ism maf'ul)", "mazlûm; haksızlığa uğrayan", 3),
 "zalim":    g("ظَالِم", "ظ ل م", "noun", "wrongdoer (ism fa'il)", "zâlim; haksızlık eden", 3),
 "an-prep":  g("عَنْ", None, "prep", "from, away from (jarr letter)", "-den, -dan (cer harfi)", 1),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/23.json").write_text(
    json.dumps({"chapter": 23, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 23 for c in man["chapters"]):
    man["chapters"].append({"n": 23, "title": TITLE23})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.21.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch23:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
