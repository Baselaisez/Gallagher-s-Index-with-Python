# -*- coding: utf-8 -*-
"""Author chapter 6 of content/samples/aqaid-ahl-al-sunna — takwin and ru'ya.

Continues the complete matn (research/sources/aqaid-nasafi-matn-full.txt)
where chapter 5 stopped: takwin as an eternal attribute distinct from the
mukawwan, then the vision of Allah — rationally possible, transmitted as
binding, and seen without place or direction. Verbatim contiguous spans
re-vowelled against the received text; pending-scholarly-review throughout.
Idempotent ADD script in the ch5 mold.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"

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

S = []

# -- s1: takwin is an eternal attribute -------------------------------------
S.append({"id": "s1", "translation": {
 "en": "And takwin (bringing-into-being) is an eternal attribute of Allah the Exalted.",
 "tr": "Tekvîn (var etme), Allah Teâlâ'nın ezelî bir sıfatıdır."},
 "tokens": [
  tok("وَالتَّكْوِينُ","takwin","noun",["mubtada-khabar","masdar","form-ii-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«التَّكْوِينُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «كَوَّنَ».",
      "Isti'naf waw; التَّكْوِين is the mubtada in raf' — the masdar of كَوَّنَ (Form II).",
      "İstinâf vâvı; «التَّكْوِينُ» merfû mübteda — «كَوَّنَ» (tef'îl) fiilinin masdarıdır.",
      segments=[seg("وَ","wa","conj"), seg("التَّكْوِينُ","takwin","noun")]),
  tok("صِفَةٌ","sifa","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "The khabar in raf'.",
      "Merfû haberdir."),
  tok("لِلَّهِ","allah","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٍ لِـ«صِفَةٌ».",
      "Preposition + the majestic name, attached to an elided na't of صِفَة.",
      "«صِفَةٌ»ün mahzuf na'tına mütealliḳ câr-mecrûr.",
      segments=[seg("لِ","li","prep"), seg("لَّهِ","allah","noun")]),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; the clause is parenthetic, for exaltation.",
      "Mâzî fiil; cümle ta'zîm için mu'terizadır."),
  tok("أَزَلِيَّةٌ","azali","noun",["naat-sifa"],
      "نَعْتٌ لِـ«صِفَةٌ» مَرْفُوعٌ.",
      "A na't of صِفَة, in raf'.",
      "«صِفَةٌ»ün merfû na'tıdır.", punct="."),
 ],
 "jumal": [
  J("وَالتَّكْوِينُ صِفَةٌ لِلَّهِ تَعَالَى أَزَلِيَّةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause — i'rabless.",
    "Müste'nefe isim cümlesi — mahalsizdir."),
 ]})

# -- s2: takwin is other than the mukawwan ----------------------------------
S.append({"id": "s2", "translation": {
 "en": "And with us it is other than the mukawwan (the thing brought into being).",
 "tr": "Bize (Mâtürîdîlere) göre o, mükevvenden (var edilenden) başkadır."},
 "tokens": [
  tok("وَهُوَ","pron-3ms-munfasil","pron",["mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«هُوَ» مُبْتَدَأٌ.",
      "Joining waw; هُوَ is the mubtada.",
      "Atıf vâvı; «هُوَ» mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","pron-3ms-munfasil","pron")]),
  tok("غَيْرُ","ghayr","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "The khabar in raf', itself a mudaf.",
      "Merfû haber ve muzâftır."),
  tok("الْمُكَوَّنِ","mukawwan","noun",["idafa-definiteness","ism-maful","form-ii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ «كَوَّنَ»، قَابِلْهُ بِالْمُكَوِّنِ بِالْكَسْرِ.",
      "Mudaf ilayh in jarr — the ism maf'ul of كَوَّنَ; contrast الْمُكَوِّن with kasra, the doer.",
      "Mecrûr muzâfun ileyh — «كَوَّنَ» fiilinin ism-i mef'ûlü; kesralı «الْمُكَوِّن» (yapan) ile karşılaştırın."),
  tok("عِنْدَنَا","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِالْخَبَرِ، وَ«نَا» مُضَافٌ إِلَيْهِ.",
      "An adverbial zarf in nasb attached to the khabar; نَا is its mudaf ilayh.",
      "Habere mütealliḳ mensub zarf; «نَا» muzâfun ileyhtir.",
      segments=[seg("عِنْدَ","inda","noun"), seg("نَا","pron-1p","pron")], punct="."),
 ],
 "jumal": [
  J("وَهُوَ غَيْرُ الْمُكَوَّنِ عِنْدَنَا",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal clause — i'rabless.",
    "Ma'tûf isim cümlesi — mahalsizdir."),
 ]})

# -- s3: the vision — possible in reason, binding by transmission -----------
S.append({"id": "s3", "translation": {
 "en": "And the vision of Allah the Exalted is rationally possible, and made binding by transmission.",
 "tr": "Allah Teâlâ'nın görülmesi aklen câizdir; nakil ile de vâcibdir."},
 "tokens": [
  tok("وَرُؤْيَةُ","ruya","noun",["mubtada-khabar","idafa-definiteness","masdar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«رُؤْيَةُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «رَأَى».",
      "Isti'naf waw; رُؤْيَة is the mubtada in raf', a mudaf — the masdar of رَأَى.",
      "İstinâf vâvı; «رُؤْيَةُ» merfû mübteda ve muzâf — «رَأَى» fiilinin masdarıdır.",
      segments=[seg("وَ","wa","conj"), seg("رُؤْيَةُ","ruya","noun")]),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The majestic name — mudaf ilayh in jarr.",
      "Lafza-i celâl — mecrûr muzâfun ileyhtir."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; the clause is parenthetic, for exaltation.",
      "Mâzî fiil; cümle ta'zîm için mu'terizadır."),
  tok("جَائِزَةٌ","jaiz","noun",["mubtada-khabar","ism-fail","hollow-verbs"],
      "خَبَرٌ أَوَّلُ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ الْأَجْوَفِ «جَازَ»، قُلِبَتْ أَلِفُهُ هَمْزَةً.",
      "First khabar in raf' — the ism fa'il of hollow جَازَ; its alif turned hamza.",
      "Birinci merfû haber — ecvef «جَازَ» fiilinin ism-i fâili; elifi hemzeye dönmüştür."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("الْعَقْلِ","aql","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "In jarr after فِي.",
      "«فِي» ile mecrurdur.", punct="،"),
  tok("وَاجِبَةٌ","wajib","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «وَجَبَ».",
      "Second khabar in raf' — the ism fa'il of وَجَبَ.",
      "İkinci merfû haber — «وَجَبَ» fiilinin ism-i fâilidir."),
  tok("بِالنَّقْلِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«وَاجِبَةٌ».",
      "Preposition + noun attached to وَاجِبَة.",
      "«وَاجِبَةٌ» ismine mütealliḳ câr-mecrûr.",
      segments=[seg("بِ","bi","prep"), seg("النَّقْلِ","naql","noun")], punct="."),
 ],
 "jumal": [
  J("وَرُؤْيَةُ اللهِ تَعَالَى جَائِزَةٌ فِي الْعَقْلِ وَاجِبَةٌ بِالنَّقْلِ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ وَخَبَرُهَا مُتَعَدِّدٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause with multiple khabars — i'rabless.",
    "Haberi müteaddit müste'nefe isim cümlesi — mahalsizdir."),
 ]})

# -- s4: He is seen without place or direction ------------------------------
S.append({"id": "s4", "translation": {
 "en": "So He is seen — not in a place, and not upon a direction.",
 "tr": "O görülür — bir mekânda değil, bir cihet üzere de değil."},
 "tokens": [
  tok("فَيُرَى","raa","verb",["naib-al-fail","naqis-verbs","mudari-marfu"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَ«يُرَى» فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.",
      "The fa of consequence; يُرَى is a passive mudari in raf', its deputy-fa'il a hidden هُوَ.",
      "Tefrî' fâsı; «يُرَى» meçhul merfû muzâridir; nâibü'l-fâili gizli «هُوَ» zamiridir.",
      segments=[seg("فَ","fa","part"), seg("يُرَى","raa","verb")]),
  tok("لَا","la-nafiya","part",[],
      "«لَا» نَافِيَةٌ.",
      "The negating la.",
      "Nefiy lâsıdır."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("مَكَانٍ","makan","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "In jarr after فِي.",
      "«فِي» ile mecrurdur.", punct="،"),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
      "Joining waw; the لا re-affirms the negation.",
      "Atıf vâvı; «لَا» nefyi pekiştirir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("جِهَةٍ","jiha","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى».",
      "In jarr after عَلَى.",
      "«عَلَى» ile mecrurdur.", punct="."),
 ],
 "jumal": [
  J("فَيُرَى لَا فِي مَكَانٍ وَلَا عَلَى جِهَةٍ",
    "جُمْلَةٌ فِعْلِيَّةٌ مُفَرَّعَةٌ عَلَى مَا قَبْلَهَا — لَا مَحَلَّ لَهَا.",
    "A verbal clause following from what precedes — i'rabless.",
    "Öncesinden tefrî' edilmiş fiil cümlesi — mahalsizdir."),
 ]})

TITLE6 = {"ar": "التَّكْوِينُ وَالرُّؤْيَةُ",
          "en": "Takwin and the Vision of Allah",
          "tr": "Tekvîn ve Rü'yetullah"}

GLOSS_ADD = {
 "takwin": {"lemma": "تَكْوِين", "root": "ك و ن", "pos": "noun",
   "gloss": {"en": "bringing-into-being (masdar, Form II)", "tr": "tekvîn; var etme (masdar)"}, "level": 5},
 "mukawwan": {"lemma": "مُكَوَّن", "root": "ك و ن", "pos": "noun",
   "gloss": {"en": "the thing brought into being (ism maf'ul)", "tr": "mükevven; var edilen (ism-i mef'ûl)"}, "level": 5},
 "ruya": {"lemma": "رُؤْيَة", "root": "ر أ ي", "pos": "noun",
   "gloss": {"en": "vision, seeing (masdar)", "tr": "rü'yet; görme (masdar)"}, "level": 4},
 "jaiz": {"lemma": "جَائِز", "root": "ج و ز", "pos": "noun",
   "gloss": {"en": "permissible, possible (ism fa'il)", "tr": "câiz (ism-i fâil)"}, "level": 3},
 "wajib": {"lemma": "وَاجِب", "root": "و ج ب", "pos": "noun",
   "gloss": {"en": "binding, necessary (ism fa'il)", "tr": "vâcib (ism-i fâil)"}, "level": 3},
 "naql": {"lemma": "نَقْل", "root": "ن ق ل", "pos": "noun",
   "gloss": {"en": "transmission (revealed report)", "tr": "nakil (naklî delil)"}, "level": 4},
 "jiha": {"lemma": "جِهَة", "root": "و ج ه", "pos": "noun",
   "gloss": {"en": "direction, side", "tr": "cihet; yön", }, "level": 3},
 "makan": {"lemma": "مَكَان", "root": "ك و ن", "pos": "noun",
   "gloss": {"en": "place", "tr": "mekân; yer"}, "level": 2},
 "pron-1p": {"lemma": "نَا", "pos": "pron",
   "gloss": {"en": "our / us (attached)", "tr": "-imiz / bizi (bitişik)"}, "level": 1},
 "li": {"lemma": "لِ", "pos": "prep",
   "gloss": {"en": "for, belonging to", "tr": "için; -e ait"}, "level": 1},
 "raa": {"lemma": "رَأَى", "root": "ر أ ي", "pos": "verb",
   "gloss": {"en": "to see", "tr": "görmek"}, "level": 2},
}

def build_morph_add():
    amali = json.loads((ROOT / "content/samples/bad-al-amali/morphology.json")
                       .read_text(encoding="utf-8"))["verbs"]
    return {"raa": amali["raa"]}

def main():
    (PKG / "chapters/6.json").write_text(
        json.dumps({"chapter": 6, "sentences": S}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
    if not any(c["n"] == 6 for c in man["chapters"]):
        man["chapters"].append({"n": 6, "title": TITLE6})
    man["chapters"].sort(key=lambda c: c["n"])
    man["version"] = "0.4.0"
    (PKG / "manifest.json").write_text(
        json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
    gl["entries"].update(GLOSS_ADD)
    (PKG / "glossary.json").write_text(
        json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
    mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
    mo["verbs"].update(build_morph_add())
    (PKG / "morphology.json").write_text(
        json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
    ntok = sum(len(s["tokens"]) for s in S)
    print(f"chapter 6 written: {len(S)} sentences, {ntok} tokens; "
          f"glossary +{len(GLOSS_ADD)}, verbs +1; manifest -> {man['version']}")

if __name__ == "__main__":
    main()
