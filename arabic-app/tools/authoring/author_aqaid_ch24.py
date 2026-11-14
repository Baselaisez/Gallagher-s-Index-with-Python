# -*- coding: utf-8 -*-
"""Author chapter 24 of aqaid-ahl-al-sunna — the imam is not unseated, and the prayer stands.

Closes the imamate section. Two rulings the Nasafi creed is known for: that an
imam is not deposed by his own wrongdoing, and that the prayer behind any man,
upright or not, is valid.

Grammar this chapter is chosen to teach:
  • بِالْفِسْقِ — a jarr-majrur hanging on a Form VII verb, which is the plainest
    ta'alluq there is and the engine's baseline case.
  • خَلْفَ كُلِّ بَرٍّ — a zarf that is itself a mudaf, heading a chain, and a
    zarf attaches like a jarr-majrur does.
  • جَائِزَةٌ — a khabar held back behind its own adverb, and an ism fa'il whose
    ta is what makes it agree with الصَّلَاةُ.
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

TITLE24 = {"ar": "لَا يَنْعَزِلُ الْإِمَامُ", "en": "The Imam Is Not Unseated",
           "tr": "İmâm Azledilmez"}

S.append({"id": "s1", "translation": {
 "en": "And the imam is not unseated by open sin or by injustice.",
 "tr": "İmâm, fısk ve cevr sebebiyle azledilmiş olmaz."},
 "tokens": [
  tok("وَلَا","la","part",["atf-nasaq"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "An isti'naf waw and a negating «la» that governs nothing.",
      "İstinâf vâvı ve amel etmeyen nefiy «lâ»sı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("يَنْعَزِلُ","inazala","verb",["form-vii-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِنَ «انْعَزَلَ» عَلَى الِانْفِعَالِ، وَبَابُ الِانْفِعَالِ مُطَاوِعٌ: يَدُلُّ عَلَى قَبُولِ الْأَثَرِ لَا عَلَى إِيقَاعِهِ.",
      "A mudari' in raf' — from انْعَزَلَ on the bab of infi'al, and that bab is MUTAWI': it names the RECEIVING of an act, not the doing of it. «He is not unseated», not «he does not unseat».",
      "Merfû muzâri — «انْعَزَلَ»den, İNFİÂL bâbında; bu bâb MUTÂVAAT bâbıdır: fiilin yapılmasını değil, KABUL edilmesini bildirir. «Azletmez» değil, «azledilmiş olmaz»."),
  tok("الْإِمَامُ","imam","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The fa'il, in raf' by the damma.",
      "Damme ile merfû fâil."),
  tok("بِالْفِسْقِ","fisq","noun",["huruf-jarr","masdar"],
      "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَنْعَزِلُ».",
      "The ba is a jarr letter of CAUSE; the phrase attaches to «is unseated» — the plainest ta'alluq there is, a jarr-majrur on the verb right before it.",
      "Bâ sebebiyyet için cer harfidir; câr-mecrûr «يَنْعَزِلُ»ye taalluk eder — en sade taalluk budur: hemen öncesindeki fiile asılan câr-mecrûr.",
      segments=[seg("بِ","ba","prep"), seg("الْفِسْقِ","fisq","noun")]),
  tok("وَالْجَوْرِ","jawr","noun",["atf-nasaq","masdar"],
      "مَعْطُوفٌ عَلَى «الْفِسْقِ» مَجْرُورٌ — مَصْدَرُ «جَارَ» بِمَعْنَى الْمَيْلِ عَنِ الْحَقِّ.",
      "Joined to «open sin», in jarr — the masdar of جَارَ, swerving from what is right.",
      "«الْفِسْقِ»e ma'tûf, mecrûr — haktan sapma mânâsında «جَارَ»nın masdarı.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("الْجَوْرِ","jawr","noun")]),
 ],
 "jumal": [J("وَلَا يَنْعَزِلُ الْإِمَامُ بِالْفِسْقِ وَالْجَوْرِ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf verbal clause — i'rabless.",
   "İstinâfî fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And the prayer behind every man, upright or given to sin, is valid,",
 "tr": "Her iyi ve kötü kimsenin arkasında namaz kılmak câizdir,"},
 "tokens": [
  tok("وَالصَّلَاةُ","salat","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الصَّلَاةُ» مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "An isti'naf waw; «the prayer» is the mubtada in raf' by the damma.",
      "İstinâf vâvı; «الصَّلَاةُ» damme ile merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الصَّلَاةُ","salat","noun")]),
  tok("خَلْفَ","khalf","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٍ لِـ«الصَّلَاةُ» — وَالظَّرْفُ كَالْجَارِّ وَالْمَجْرُورِ فِي وُجُوبِ التَّعَلُّقِ.",
      "A place-adverb in nasb and a mudaf, attaching to an OMITTED na't of «the prayer» — a zarf must attach to something exactly as a jarr-majrur must.",
      "Mansub mekân zarfı ve muzâf; «الصَّلَاةُ»nun MAHZÛF na'tına taalluk eder — zarf da câr-mecrûr gibi mutlaka bir şeye taalluk etmek zorundadır."),
  tok("كُلِّ","kull","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — حَلْقَةٌ وُسْطَى.",
      "The mudaf ilayh in jarr, and itself a mudaf — a middle link in the chain.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — zincirin orta halkası."),
  tok("بَرٍّ","barr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعْلٍ.",
      "The mudaf ilayh in jarr by the kasra — a settled quality on فَعْل.",
      "Kesra ile mecrûr muzâfun ileyh — FA'L vezninde sıfat-ı müşebbehe."),
  tok("وَفَاجِرٍ","fajir","noun",["atf-nasaq","ism-fail"],
      "مَعْطُوفٌ عَلَى «بَرٍّ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «فَجَرَ».",
      "Joined to «upright», in jarr — the ism fa'il of فَجَرَ.",
      "«بَرٍّ»e ma'tûf, mecrûr — «فَجَرَ»nin ism-i fâili.",
      segments=[seg("وَ","wa","conj"), seg("فَاجِرٍ","fajir","noun")]),
  tok("جَائِزَةٌ","jaiz","noun",["mubtada-khabar","ism-fail"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ فَاعِلٍ، وَالتَّاءُ لِمُطَابَقَةِ «الصَّلَاةُ» فِي التَّأْنِيثِ، وَقَدْ تَأَخَّرَ عَنِ الظَّرْفِ فَلَمْ يَلِ مُبْتَدَأَهُ.",
      "The khabar of the mubtada, in raf' by the damma — an ism fa'il, and its TA is what makes it agree with «the prayer» in gender. It has been held back behind the adverb, so it does not stand next to its own mubtada.",
      "Damme ile merfû haber — ism-i fâildir; TÂsı, «الصَّلَاةُ» ile te'nîste uyum içindir. Zarfın arkasına atılmış, bu yüzden mübtedâsının yanında durmamıştır.", punct="،"),
 ],
 "jumal": [J("وَالصَّلَاةُ خَلْفَ كُلِّ بَرٍّ وَفَاجِرٍ جَائِزَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "and the funeral prayer over every one of them is valid too.",
 "tr": "onların her biri üzerine cenaze namazı kılmak da câizdir."},
 "tokens": [
  tok("وَالصَّلَاةُ","salat","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الصَّلَاةُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the prayer» is the mubtada in raf'.",
      "Atıf vâvı; «الصَّلَاةُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الصَّلَاةُ","salat","noun")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٍ لِـ«الصَّلَاةُ».",
      "A jarr letter; the phrase attaches to an OMITTED na't of «the prayer» — nothing written governs it, so the amil is understood.",
      "Cer harfi; câr-mecrûr «الصَّلَاةُ»nun MAHZÛF na'tına taalluk eder — yazılı hiçbir şey onu amel etmediği için âmil takdîr edilir."),
  tok("كُلِّ","kull","noun",["idafa-definiteness","huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ.",
      "In jarr after «ala», and a mudaf.",
      "«عَلَى» ile mecrûr ve muzâftır."),
  tok("مَيِّتٍ","mayyit","noun",["idafa-definiteness","sifa-mushabbaha"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَيْعِلٍ، وَأَصْلُهُ مَيْوِتٌ فَأُدْغِمَتِ الْوَاوُ فِي الْيَاءِ.",
      "The mudaf ilayh in jarr — a settled quality on فَيْعِل. Its origin is مَيْوِت: the waw was merged into the ya.",
      "Mecrûr muzâfun ileyh — FEY'İL vezninde sıfat-ı müşebbehe. Aslı مَيْوِت'tir; vâv yâya idgām edilmiştir."),
  tok("جَائِزَةٌ","jaiz","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَبِهِ تَمَّ الْكَلَامُ فِي الْإِمَامَةِ.",
      "The khabar in raf' by the damma — and with it the matn's word on the imamate is complete.",
      "Damme ile merfû haber — imâmet bahsi bununla tamamlanır.", punct="."),
 ],
 "jumal": [J("وَالصَّلَاةُ عَلَى كُلِّ مَيِّتٍ جَائِزَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا — لَا مَحَلَّ لَهَا.",
   "A nominal clause joined to the one before it — i'rabless.",
   "Öncesine ma'tûf isim cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "inazala": g("انْعَزَلَ", "ع ز ل", "verb", "to be removed from office (Form VII, mutawi')", "azledilmiş olmak (VII. bâb, mutâvaat)", 4),
 "fisq":    g("فِسْق", "ف س ق", "noun", "open disobedience (masdar)", "fısk; açık günah (masdar)", 4),
 "jawr":    g("جَوْر", "ج و ر", "noun", "injustice, swerving from right (masdar)", "cevr; haktan sapma (masdar)", 4),
 "khalf":   g("خَلْفَ", "خ ل ف", "noun", "behind (adverb of place)", "arkasında (mekân zarfı)", 1),
 "barr":    g("بَرّ", "ب ر ر", "noun", "upright, dutiful", "iyi, itaatkâr", 3),
 "fajir":   g("فَاجِر", "ف ج ر", "noun", "one given to sin (ism fa'il)", "fâcir; günaha dalan", 4),
 "mayyit":  g("مَيِّت", "م و ت", "noun", "dead, a dead person", "meyyit; ölü", 2),
}

def build_morph():
    out = {}
    # انْعَزَلَ — Form VII, the bab of MUTAWA'A: it names the receiving of an act.
    # Sound root, so the paradigm derives without exception.
    out["inazala"] = _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْعَزَل", "نْعَزِل", "اِنْعَزِل",
                                 "اِنْعِزَال", "مُنْعَزِل",
                                 note="بَابُ الِانْفِعَالِ لِلْمُطَاوَعَةِ — يَدُلُّ عَلَى قَبُولِ الْأَثَرِ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/24.json").write_text(
    json.dumps({"chapter": 24, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 24 for c in man["chapters"]):
    man["chapters"].append({"n": 24, "title": TITLE24})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.22.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch24:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
