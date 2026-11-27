# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 2: the MUʿRAB and the MABNI, the IʿRAB (its definition, its three kinds and what each is the sign of), the ʿAMIL,
and the declension classes with the notebook's example triplets (جَاءَنِي / رَأَيْتُ / مَرَرْتُ بِـ): the single and the broken plural, the sound
feminine plural, the diptote, the six nouns, the sound masculine plural with أُولُو and عِشْرُونَ, the dual with اثْنَانِ and كِلَا.
Source: the Ottoman notebook, lines ~118-160 of the transcription.

  RESTORED (the notebook carries the ruling only in Turkish; the received matn of the Kafiya is written and marked): s1, s5, s6, s11, s13, s15, s17, s18, s20.
  COMMENTARY (the teacher's worked example, not the matn): s3, s10 — marked C_EN/C_TR.
  python3 tools/authoring/author_kafiya_ch2.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-murab-wal-mabni-wal-irab"
K1 = "al-kalima-wal-kalam"
TITLE = {"ar": "الْمُعْرَبُ وَالْمَبْنِيُّ وَالْإِعْرَابُ", "en": "The declinable and the indeclinable, and the iʿrab", "tr": "Mu'reb ve mebnî, ve i'râb"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
B8 = "الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ"; W8 = "اِفْتَعَلَ يَفْتَعِلُ"
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def fi(tag=K): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».")
def ila(tag=K): return tok("إِلَى", "ila", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e».")
def nahwu():
    return tok("نَحْوُ", "nahw", "noun", [K, "mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted sentence.", "«… gibi» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=":")
def jaani(full="جَاءَنِي", wa=False):
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg("جَاءَ", "jaa", "verb"), pr1s()]
    return tok(full, "jaa", "verb", [K, "fail", "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "جَاءَ فِعْلٌ مَاضٍ أَجْوَفُ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me» — the nun of guarding, the ya the object.", "«bana geldi» — vikâye nûnu, yâ mef'ûl.", segments=segs)
def raaytu(): return tok("وَرَأَيْتُ", "raa", "verb", [K, "fail", "maful-bihi", "naqis-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَرَأَى فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ فَاعِلٌ.", "«and I saw» — the ta is the doer.", "«ve gördüm» — tâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْتُ", "raa", "verb")])
def marartu(): return tok("وَمَرَرْتُ", "marra", "verb", [K, "fail", "doubled-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَرَّ فِعْلٌ مَاضٍ مُضَاعَفٌ فُكَّ إِدْغَامُهُ لِلتَّاءِ، وَالتَّاءُ فَاعِلٌ.", "«and I passed» — the doubled verb opened before the ta.", "«ve uğradım» — muzâaf, tâ önünde idgam çözüldü.", segments=[seg("وَ", "wa", "conj"), seg("مَرَرْتُ", "marra", "verb")])
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct="."):
    return tok(full, lex, pos, [K, "huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, segments=[seg("بِ", "bi", "prep"), seg(inner, lex, pos)], punct=punct)
def sign(full, lex, letter_en, letter_tr, punct=None):
    return tok(full, lex, "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالِاسْمُ بَعْدَهَا مَجْرُورٌ — عَلَامَةُ الْإِعْرَابِ.", "«by the " + letter_en + "».", "«" + letter_tr + " ile».", segments=[seg("بِ", "bi", "prep"), seg(full[2:], lex, "noun")], punct=punct)
def passive_pl(full, lex, ar_verb, en, tr, tags, wa=False, dual=False):
    segs = [seg("وَ", "wa", "conj"), seg(full[2:], lex, "verb")] if wa else None
    ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + ar_verb + " مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ " + ("مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ" if dual else "مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ") + ("" if wa else " — وَالْجُمْلَةُ خَبَرٌ") + "."
    return tok(full, lex, "verb", [K, "naib-al-fail"] + tags, ar, en, tr, segments=segs)

# ----------- s1 (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The noun: some of it is declinable and some of it indeclinable." + R_EN,
 "tr": "İsim: bir kısmı mu'reb, bir kısmı mebnîdir." + R_TR},
 "tokens": [
  tok("وَالِاسْمُ", "ism", "noun", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالِاسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the noun» — the mubtada.", "«isim» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الِاسْمُ", "ism", "noun")]),
  tok("مِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ لِمُعْرَبٌ، وَالْجُمْلَةُ خَبَرُ الِاسْمِ.", "«of it» — the fronted khabar of the inner sentence.", "«ondan» — mukaddem haber.", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مُعْرَبٌ", "murab", "noun", [K, "mubtada-khabar", "ism-maful", "form-iv-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ أَعْرَبَ.", "«declinable» — the delayed mubtada.", "«mu'reb» — muahhar mübtedâ."),
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and of it».", "«ve ondan».", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مَبْنِيٌّ", "mabni", "noun", [K, "mubtada-khabar", "ism-maful"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ بَنَى.", "«indeclinable».", "«mebnî».", punct="."),
 ]})

# ----------- s2
S.append({"id": "s2", "translation": {
 "en": "The declinable is the compounded word that does not resemble what is indeclinable by origin.",
 "tr": "Mu'reb, aslen mebnî olana benzemeyen mürekkebdir."},
 "tokens": [
  tok("الْمُعْرَبُ", "murab", "noun", [K, "mubtada-khabar", "ism-maful"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the declinable».", "«mu'reb»."),
  tok("الْمُرَكَّبُ", "murakkab", "noun", [K, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — الْمُرَكَّبُ مَعَ عَامِلِهِ.", "«the compounded» — the khabar: composed with its governor.", "«mürekkeb» — haber: âmiliyle terkib edilmiş."),
  tok("الَّذِي", "alladhi", "pron", [K, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ صِفَةٌ لِلْمُرَكَّبِ.", "«that» — the relative, qualifying the khabar.", "«… olan» — mevsûl, sıfat."),
  tok("لَمْ", "lam-jazima", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — the jussive لَمْ.", "«-medi» — cezm eden lem."),
  tok("يُشْبِهْ", "ashbaha", "verb", [K, "lam-jazim", "form-iv-verbs", "maful-bihi"], "مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ الْمَوْصُولِ.", "«resemble» — jussive after لَمْ.", "«benzemedi» — lem ile meczûm."),
  tok("مَبْنِيَّ", "mabni", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«what is indeclinable» — the object, annexed.", "«mebnîsine» — mef'ûl, muzâf."),
  tok("الْأَصْلِ", "asl", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَبْنِيُّ الْأَصْلِ: الْحَرْفُ وَالْمَاضِي وَالْأَمْرُ.", "«by origin» — the particle, the mazi and the amr.", "«aslen» — harf, mâzî ve emir.", punct="."),
 ]})

# ----------- s3 (COMMENTARY)
S.append({"id": "s3", "translation": {
 "en": "So Zayd in «Zayd struck» is declinable, and «these» in «these stood» is indeclinable, because it resembles the particle." + C_EN,
 "tr": "Öyleyse «Zeyd vurdu»daki Zeyd mu'rebdir; «bunlar kalktı»daki «bunlar» ise harfe benzediği için mebnîdir." + C_TR},
 "tokens": [
  tok("فَزَيْدٌ", "zayd", "propn", [K, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«so Zayd» — the mubtada.", "«öyleyse Zeyd» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("زَيْدٌ", "zayd", "propn")]),
  fi(),
  tok("ضَرَبَ", "daraba", "verb", [K, "huruf-jarr", "fail"], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ بِفِي.", "«“struck» — the quoted sentence after «in».", "«“vurdu» — «-de»den sonra hikâye edilen cümle."),
  tok("زَيْدٌ", "zayd", "propn", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd”».", "«Zeyd”»."),
  tok("مُعْرَبٌ", "murab", "noun", [K, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is declinable».", "«mu'rebdir».", punct="،"),
  tok("وَهَؤُلَاءِ", "haulai", "pron", [K, "mubtada-khabar", "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَهَؤُلَاءِ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and “these”» — a demonstrative built on kasra.", "«ve “bunlar”» — kesre üzere mebnî işaret ismi.", segments=[seg("وَ", "wa", "conj"), seg("هَؤُلَاءِ", "haulai", "pron")]),
  fi(),
  tok("قَامَ", "qama", "verb", [K, "huruf-jarr", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ — جُمْلَةٌ مَحْكِيَّةٌ.", "«“stood».", "«“kalktı»."),
  tok("هَؤُلَاءِ", "haulai", "pron", [K, "fail", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«these”».", "«bunlar”»."),
  tok("مَبْنِيٌّ", "mabni", "noun", [K, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is indeclinable».", "«mebnîdir»."),
  tok("لِأَنَّهُ", "anna", "part", [K, "inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ وَاسْمُهَا.", "«because it».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  tok("أَشْبَهَ", "ashbaha", "verb", [K, "inna-wa-akhawatuha", "form-iv-verbs", "maful-bihi"], "مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«resembles» — the khabar of أَنَّ.", "«benzer» — enne'nin haberi."),
  tok("الْحَرْفَ", "harf", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the particle».", "«harfe».", punct="."),
 ]})

# ----------- s4
S.append({"id": "s4", "translation": {
 "en": "And iʿrab is that by which the end of the word differs, so as to point to the meanings that come over it in turn.",
 "tr": "İ'râb, mu'rebin üzerine sırayla gelen manalara delâlet etmesi için kendisiyle sonunun değiştiği şeydir."},
 "tokens": [
  tok("وَالْإِعْرَابُ", "irab", "noun", [K, "mubtada-khabar", "masdar", "form-iv-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْإِعْرَابُ مُبْتَدَأٌ — مَصْدَرُ أَعْرَبَ.", "«and iʿrab» — the mubtada.", "«i'râb» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْإِعْرَابُ", "irab", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that» — the relative, the khabar.", "«… şey» — mevsûl, haber."),
  tok("اخْتَلَفَ", "ikhtalafa", "verb", [K, "ism-mawsul", "form-viii-verbs", "fail"], "مَاضٍ — صِلَةُ الْمَوْصُولِ؛ افْتَعَلَ.", "«differs» — the relative clause.", "«değişir» — sıla."),
  tok("آخِرُهُ", "akhir", "noun", [K, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: آخِرُ الْمُعْرَبِ.", "«its end» — the doer: the end of the declinable word.", "«sonu» — fâil.", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ إِلَى مَا.", "«by it» — the returning pronoun.", "«onunla» — âid.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("لِيَدُلَّ", "dalla", "verb", [K, "lam-taleel", "doubled-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَيَدُلَّ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْإِعْرَابُ.", "«so as to point» — the lam of cause.", "«delâlet etsin diye» — ta'lîl lâmı.", segments=[seg("لِ", "lam-taleel", "part"), seg("يَدُلَّ", "dalla", "verb")]),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمَعَانِي", "mana", "noun", [K, "huruf-jarr", "jam-taksir", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — جَمْعُ مَعْنًى، مَنْقُوصٌ.", "«the meanings» — the plural of مَعْنًى, a manqus.", "«manalara» — mana'nın cem'i, mankûs."),
  tok("الْمُعْتَوِرَةِ", "mutawir", "noun", [K, "naat-sifa", "ism-fail", "form-viii-verbs"], "صِفَةٌ لِلْمَعَانِي مَجْرُورَةٌ — اسْمُ فَاعِلِ اعْتَوَرَ: تَدَاوَلَ؛ وَهِيَ الْفَاعِلِيَّةُ وَالْمَفْعُولِيَّةُ وَالْإِضَافَةُ.", "«that come over it in turn» — the active participle of اعْتَوَرَ: doerhood, objecthood, annexation.", "«üzerine sırayla gelen» — i'tevere'nin ism-i fâili: fâiliyet, mef'ûliyet, izâfet."),
  tok("عَلَيْهِ", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — عَلَى الْمُعْرَبِ.", "«over it» — the declinable word.", "«onun üzerine» — mu'rebin.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()], punct="."),
 ]})

# ----------- s5 (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "And the kinds of the noun's iʿrab are three: rafʿ, nasb and jarr." + R_EN,
 "tr": "İsmin i'râbının çeşitleri üçtür: ref', nasb ve cer." + R_TR},
 "tokens": [
  tok("وَأَنْوَاعُ", "naw", "noun", [K, "mubtada-khabar", "idafa-definiteness", "jam-taksir"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَنْوَاعُ مُبْتَدَأٌ، مُضَافٌ — جَمْعُ نَوْعٍ.", "«and the kinds of» — the mubtada.", "«çeşitleri» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("أَنْوَاعُ", "naw", "noun")]),
  tok("إِعْرَابِ", "irab", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the iʿrab of».", "«i'râbının»."),
  tok("الِاسْمِ", "ism", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the noun».", "«ismin»."),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«three».", "«üçtür».", punct=":"),
  tok("رَفْعٌ", "raf", "noun", [K, "badal", "masdar"], "بَدَلٌ تَفْصِيلِيٌّ مِنْ ثَلَاثَةٌ مَرْفُوعٌ.", "«rafʿ» — a detailing badal.", "«ref'» — tafsîl bedeli."),
  tok("وَنَصْبٌ", "nasb", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَنَصْبٌ مَعْطُوفٌ مَرْفُوعٌ.", "«nasb».", "«nasb».", segments=[seg("وَ", "wa", "conj"), seg("نَصْبٌ", "nasb", "noun")]),
  tok("وَجَرٌّ", "jarr", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَجَرٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and jarr».", "«ve cer».", segments=[seg("وَ", "wa", "conj"), seg("جَرٌّ", "jarr", "noun")], punct="."),
 ]})

# ----------- s6 (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "Rafʿ is the sign of doerhood, nasb the sign of objecthood, and jarr the sign of annexation." + R_EN,
 "tr": "Ref' fâiliyetin, nasb mef'ûliyetin, cer izâfetin alâmetidir." + R_TR},
 "tokens": [
  tok("فَالرَّفْعُ", "raf", "noun", [K, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالرَّفْعُ مُبْتَدَأٌ.", "«rafʿ» — the mubtada.", "«ref'» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الرَّفْعُ", "raf", "noun")]),
  tok("عَلَمُ", "alam-sign", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — الْعَلَمُ: الْعَلَامَةُ.", "«the sign of» — the khabar.", "«alâmeti» — haber."),
  tok("الْفَاعِلِيَّةِ", "failiyya", "noun", [K, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرٌ صِنَاعِيٌّ مِنَ الْفَاعِلِ.", "«doerhood» — an artificial masdar.", "«fâiliyetin» — masdar-ı sınâî.", punct="،"),
  tok("وَالنَّصْبُ", "nasb", "noun", [K, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالنَّصْبُ مُبْتَدَأٌ.", "«and nasb».", "«nasb».", segments=[seg("وَ", "wa", "conj"), seg("النَّصْبُ", "nasb", "noun")]),
  tok("عَلَمُ", "alam-sign", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the sign of».", "«alâmeti»."),
  tok("الْمَفْعُولِيَّةِ", "mafuliyya", "noun", [K, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«objecthood».", "«mef'ûliyetin».", punct="،"),
  tok("وَالْجَرُّ", "jarr", "noun", [K, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْجَرُّ مُبْتَدَأٌ.", "«and jarr».", "«cer».", segments=[seg("وَ", "wa", "conj"), seg("الْجَرُّ", "jarr", "noun")]),
  tok("عَلَمُ", "alam-sign", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the sign of».", "«alâmeti»."),
  tok("الْإِضَافَةِ", "idafa", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«annexation».", "«izâfetin».", punct="."),
 ]})

# ----------- s7
S.append({"id": "s7", "translation": {
 "en": "As in: Zayd came to me, and I saw Zayd, and I passed by Zayd.",
 "tr": "Meselâ: Zeyd bana geldi, Zeyd'i gördüm, Zeyd'e uğradım."},
 "tokens": [
  nahwu(), jaani(),
  tok("زَيْدٌ", "zayd", "propn", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the doer, its damma the sign.", "«Zeyd» — fâil, damme alâmeti.", punct="،"),
  raaytu(),
  tok("زَيْدًا", "zayd", "propn", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the object, its fatha the sign.", "«Zeyd'i» — mef'ûl, fetha alâmeti.", punct="،"),
  marartu(),
  bi_("بِزَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "زَيْدٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«by Zayd» — jarr, its kasra the sign.", "«Zeyd'e» — mecrûr, kesre alâmeti.", "زَيْدٍ"),
 ]})

# ----------- s8
S.append({"id": "s8", "translation": {
 "en": "And his father came to me, and I saw his father, and I passed by his father.",
 "tr": "Babası bana geldi, babasını gördüm, babasına uğradım."},
 "tokens": [
  jaani("وَجَاءَنِي", wa=True),
  tok("أَبُوهُ", "ab", "noun", [K, "fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ السِّتَّةِ؛ وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the doer, raised by the waw.", "«babası» — fâil, vâv ile merfû.", segments=[seg("أَبُو", "ab", "noun"), pr3ms()], punct="،"),
  raaytu(),
  tok("أَبَاهُ", "ab", "noun", [K, "maful-bihi", "five-nouns", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ.", "«his father» — the object, by the alif.", "«babasını» — mef'ûl, elif ile.", segments=[seg("أَبَا", "ab", "noun"), pr3ms()], punct="،"),
  marartu(),
  tok("بِأَبِيهِ", "ab", "noun", [K, "huruf-jarr", "five-nouns", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَبِيهِ مَجْرُورٌ بِالْيَاءِ.", "«by his father» — jarr by the ya.", "«babasına» — yâ ile mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("أَبِي", "ab", "noun"), pr3msi()], punct="."),
 ]})

# ----------- s9
S.append({"id": "s9", "translation": {
 "en": "And the governor is that by which the meaning that requires the iʿrab comes to stand.",
 "tr": "Âmil, i'râbı gerektiren mananın kendisiyle hâsıl olduğu şeydir."},
 "tokens": [
  tok("وَالْعَامِلُ", "amil", "noun", [K, "mubtada-khabar", "ism-fail"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ.", "«and the governor» — the mubtada.", "«âmil» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْعَامِلُ", "amil", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that».", "«… şey»."),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ، قُدِّمَ عَلَى فِعْلِهِ.", "«by which» — the returning pronoun, fronted.", "«kendisiyle» — âid, öne alınmış.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("يَتَقَوَّمُ", "taqawwama", "verb", [K, "ism-mawsul", "form-v-verbs", "fail"], "مُضَارِعٌ مَرْفُوعٌ — صِلَةُ الْمَوْصُولِ؛ تَفَعَّلَ.", "«comes to stand» — Form V.", "«hâsıl olur» — tefa''ul."),
  tok("الْمَعْنَى", "mana", "noun", [K, "fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«the meaning» — the doer, maqsur.", "«mana» — fâil, maksûr."),
  tok("الْمُقْتَضِي", "muqtadi", "noun", [K, "naat-sifa", "ism-fail", "ism-maqsur-manqus", "form-viii-verbs"], "صِفَةٌ لِلْمَعْنَى مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمُ فَاعِلِ اقْتَضَى، مَنْقُوصٌ.", "«that requires» — the active participle of اقْتَضَى, a manqus.", "«gerektiren» — iktazâ'nın ism-i fâili, mankûs."),
  tok("لِلْإِعْرَابِ", "irab", "noun", [K, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْإِعْرَابِ مَجْرُورٌ.", "«the iʿrab».", "«i'râbı».", segments=[seg("لِ", "li", "prep"), seg("الْإِعْرَابِ", "irab", "noun")], punct="."),
 ]})

# ----------- s10 (COMMENTARY)
S.append({"id": "s10", "translation": {
 "en": "So in «Zayd came to me» the governor is «came», because the meaning of doerhood came about by it." + C_EN,
 "tr": "Öyleyse «Zeyd bana geldi»de âmil «geldi»dir, çünkü fâiliyet manası onunla hâsıl olmuştur." + C_TR},
 "tokens": [
  tok("فَفِي", "fi", "prep", [K, "huruf-jarr"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ خَبَرٌ مُقَدَّمٌ.", "«so in» — the fronted khabar.", "«öyleyse …-de» — mukaddem haber.", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  jaani(),
  tok("زَيْدٌ", "zayd", "propn", [K, "fail"], "فَاعِلٌ — وَالْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«Zayd» — the quoted sentence.", "«Zeyd» — hikâye edilen cümle."),
  tok("الْعَامِلُ", "amil", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the governor» — the delayed mubtada.", "«âmil» — muahhar mübtedâ."),
  tok("جَاءَ", "jaa", "verb", [K, "mubtada-khabar", "hollow-verbs"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ — أَيِ: الْعَامِلُ لَفْظُ جَاءَ.", "«“came”» — the quoted word in the khabar's place.", "«“geldi”» — haber mahallinde hikâye edilen lafız.", punct="،"),
  tok("لِأَنَّ", "anna", "part", [K, "inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  tok("مَعْنَى", "mana", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "اسْمُ أَنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the meaning of» — the noun of أَنَّ.", "«manası» — enne'nin ismi."),
  tok("الْفَاعِلِيَّةِ", "failiyya", "noun", [K, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«doerhood».", "«fâiliyet»."),
  tok("حَصَلَ", "hasala", "verb", [K, "inna-wa-akhawatuha", "fail"], "مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«came about» — the khabar of أَنَّ.", "«hâsıl oldu» — enne'nin haberi."),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — بِجَاءَ.", "«by it».", "«onunla».", segments=[seg("بِ", "bi", "prep"), pr3msi()], punct="."),
 ]})

# ----------- s11 (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "The triptote single noun and the triptote broken plural are raised by the damma, made accusative by the fatha and made genitive by the kasra." + R_EN,
 "tr": "Munsarif müfred ile munsarif cem-i mükesser damme ile ref', fetha ile nasb, kesre ile cer edilir." + R_TR},
 "tokens": [
  tok("فَالْمُفْرَدُ", "mufrad", "noun", [K, "mubtada-khabar", "ism-maful"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمُفْرَدُ مُبْتَدَأٌ.", "«the single» — the mubtada.", "«müfred» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الْمُفْرَدُ", "mufrad", "noun")]),
  tok("الْمُنْصَرِفُ", "munsarif", "noun", [K, "naat-sifa", "ism-fail", "form-vii-verbs"], "صِفَةٌ مَرْفُوعَةٌ — اسْمُ فَاعِلِ انْصَرَفَ: مَا يَقْبَلُ التَّنْوِينَ وَالْكَسْرَةَ.", "«triptote» — what takes the tanwin and the kasra.", "«munsarif» — tenvin ve kesreyi kabul eden."),
  tok("وَالْجَمْعُ", "jam", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْجَمْعُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the plural».", "«ve cemi».", segments=[seg("وَ", "wa", "conj"), seg("الْجَمْعُ", "jam", "noun")]),
  tok("الْمُكَسَّرُ", "mukassar", "noun", [K, "naat-sifa", "ism-maful", "form-ii-verbs", "jam-taksir"], "صِفَةٌ مَرْفُوعَةٌ — اسْمُ مَفْعُولِ كَسَّرَ.", "«broken».", "«mükesser»."),
  tok("الْمُنْصَرِفُ", "munsarif", "noun", [K, "naat-sifa", "ism-fail"], "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ.", "«triptote».", "«munsarif»."),
  passive_pl("يُرْفَعَانِ", "rafaa", "يُرْفَعَانِ", "«are raised» — passive dual, the alif its deputy doer.", "«ref' edilir» — meçhul tesniye.", ["mubtada-khabar", "al-muthanna"], dual=True),
  sign("بِالضَّمَّةِ", "damma", "damma", "damme"),
  passive_pl("وَيُنْصَبَانِ", "nasaba-set", "يُنْصَبَانِ", "«and made accusative».", "«ve nasb edilir».", ["atf-nasaq", "al-muthanna"], wa=True, dual=True),
  sign("بِالْفَتْحَةِ", "fatha", "fatha", "fetha"),
  passive_pl("وَيُجَرَّانِ", "jarra", "يُجَرَّانِ", "«and made genitive» — the doubled verb.", "«ve cer edilir» — muzâaf.", ["atf-nasaq", "al-muthanna", "doubled-verbs"], wa=True, dual=True),
  sign("بِالْكَسْرَةِ", "kasra", "kasra", "kesre", punct="."),
 ]})

# ----------- s12
S.append({"id": "s12", "translation": {
 "en": "As in: Zayd and men came to me, and I saw Zayd and men, and I passed by Zayd and men.",
 "tr": "Meselâ: Zeyd ve adamlar bana geldi; Zeyd'i ve adamları gördüm; Zeyd'e ve adamlara uğradım."},
 "tokens": [
  nahwu(), jaani(),
  tok("زَيْدٌ", "zayd", "propn", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd».", "«Zeyd»."),
  tok("وَرِجَالٌ", "rajul", "noun", [K, "atf-nasaq", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَرِجَالٌ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ مُنْصَرِفٌ.", "«and men» — a triptote broken plural.", "«ve adamlar» — munsarif cem-i mükesser.", segments=[seg("وَ", "wa", "conj"), seg("رِجَالٌ", "rajul", "noun")], punct="،"),
  raaytu(),
  tok("زَيْدًا", "zayd", "propn", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd».", "«Zeyd'i»."),
  tok("وَرِجَالًا", "rajul", "noun", [K, "atf-nasaq", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَرِجَالًا مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and men».", "«ve adamları».", segments=[seg("وَ", "wa", "conj"), seg("رِجَالًا", "rajul", "noun")], punct="،"),
  marartu(),
  bi_("بِزَيْدٍ", "zayd", "propn", [], "زَيْدٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«by Zayd».", "«Zeyd'e».", "زَيْدٍ", punct=None),
  tok("وَرِجَالٍ", "rajul", "noun", [K, "atf-nasaq", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَرِجَالٍ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and men».", "«ve adamlara».", segments=[seg("وَ", "wa", "conj"), seg("رِجَالٍ", "rajul", "noun")], punct="."),
 ]})

# ----------- s13 (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "The sound feminine plural is raised by the damma and made accusative and genitive by the kasra." + R_EN,
 "tr": "Cem-i müennes sâlim damme ile ref', kesre ile nasb ve cer edilir." + R_TR},
 "tokens": [
  tok("وَجَمْعُ", "jam", "noun", [K, "mubtada-khabar", "idafa-definiteness", "jam-muannath-salim"], "الْوَاوُ عَاطِفَةٌ، وَجَمْعُ مُبْتَدَأٌ، مُضَافٌ.", "«and the plural of» — the mubtada.", "«cem'i» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("جَمْعُ", "jam", "noun")]),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, "idafa-definiteness", "ism-maful", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ أَنَّثَ.", "«the feminine».", "«müennesin»."),
  tok("السَّالِمُ", "salim", "noun", [K, "naat-sifa", "ism-fail"], "صِفَةٌ لِجَمْعُ مَرْفُوعَةٌ — سَلِمَ بِنَاءُ وَاحِدِهِ.", "«sound» — qualifying «plural»: its singular's build kept whole.", "«sâlim» — cem'in sıfatı: müfredinin yapısı bozulmamış."),
  passive_pl("يُرْفَعُ", "rafaa", "يُرْفَعُ", "«is raised».", "«ref' edilir».", ["mubtada-khabar"]),
  sign("بِالضَّمَّةِ", "damma", "damma", "damme"),
  passive_pl("وَيُنْصَبُ", "nasaba-set", "يُنْصَبُ", "«and made accusative».", "«ve nasb».", ["atf-nasaq"], wa=True),
  passive_pl("وَيُجَرُّ", "jarra", "يُجَرُّ", "«and genitive».", "«ve cer edilir».", ["atf-nasaq", "doubled-verbs"], wa=True),
  sign("بِالْكَسْرَةِ", "kasra", "kasra", "kesre", punct="."),
 ]})

# ----------- s14
S.append({"id": "s14", "translation": {
 "en": "As in: Muslim women came to me, and I saw Muslim women, and I passed by Muslim women.",
 "tr": "Meselâ: Müslüman kadınlar bana geldi; Müslüman kadınları gördüm; Müslüman kadınlara uğradım."},
 "tokens": [
  nahwu(), jaani(),
  tok("مُسْلِمَاتٌ", "muslima", "noun", [K, "fail", "jam-muannath-salim"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«Muslim women» — the doer.", "«Müslüman kadınlar» — fâil.", punct="،"),
  raaytu(),
  tok("مُسْلِمَاتٍ", "muslima", "noun", [K, "maful-bihi", "jam-muannath-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ.", "«Muslim women» — the object, its kasra standing for the fatha.", "«Müslüman kadınları» — mef'ûl, fetha yerine kesre.", punct="،"),
  marartu(),
  bi_("بِمُسْلِمَاتٍ", "muslima", "noun", ["jam-muannath-salim"], "مُسْلِمَاتٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«by Muslim women».", "«Müslüman kadınlara».", "مُسْلِمَاتٍ"),
 ]})

# ----------- s15 (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "The diptote is raised by the damma and made accusative and genitive by the fatha." + R_EN,
 "tr": "Gayr-i munsarif damme ile ref', fetha ile nasb ve cer edilir." + R_TR},
 "tokens": [
  tok("وَغَيْرُ", "ghayr", "noun", [K, "mubtada-khabar", "idafa-definiteness", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مُبْتَدَأٌ، مُضَافٌ.", "«and the non-» — the mubtada.", "«gayr-i» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("غَيْرُ", "ghayr", "noun")]),
  tok("الْمُنْصَرِفِ", "munsarif", "noun", [K, "idafa-definiteness", "ism-fail", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«triptote» — the diptote.", "«munsarif» — gayr-i munsarif."),
  passive_pl("يُرْفَعُ", "rafaa", "يُرْفَعُ", "«is raised».", "«ref' edilir».", ["mubtada-khabar"]),
  sign("بِالضَّمَّةِ", "damma", "damma", "damme"),
  passive_pl("وَيُنْصَبُ", "nasaba-set", "يُنْصَبُ", "«and made accusative».", "«ve nasb».", ["atf-nasaq"], wa=True),
  passive_pl("وَيُجَرُّ", "jarra", "يُجَرُّ", "«and genitive».", "«ve cer edilir».", ["atf-nasaq", "doubled-verbs"], wa=True),
  sign("بِالْفَتْحَةِ", "fatha", "fatha", "fetha", punct="."),
 ]})

# ----------- s16
S.append({"id": "s16", "translation": {
 "en": "As in: Ahmad came to me, and I saw Ahmad, and I passed by Ahmad.",
 "tr": "Meselâ: Ahmed bana geldi; Ahmed'i gördüm; Ahmed'e uğradım."},
 "tokens": [
  nahwu(), jaani(),
  tok("أَحْمَدُ", "ahmad", "propn", [K, "fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ.", "«Ahmad» — a diptote: proper name on a verb's pattern.", "«Ahmed» — alemiyet ve vezn-i fiilden gayr-i munsarif.", punct="،"),
  raaytu(),
  tok("أَحْمَدَ", "ahmad", "propn", [K, "maful-bihi", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Ahmad».", "«Ahmed'i».", punct="،"),
  marartu(),
  bi_("بِأَحْمَدَ", "ahmad", "propn", ["mamnu-min-sarf"], "أَحْمَدَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«by Ahmad» — the fatha standing for the kasra.", "«Ahmed'e» — kesre yerine fetha.", "أَحْمَدَ"),
 ]})

# ----------- s17 (RESTORED)
S.append({"id": "s17", "translation": {
 "en": "The six nouns, when annexed to other than the speaker's ya, are raised by the waw, made accusative by the alif and genitive by the ya." + R_EN,
 "tr": "Esmâ-i sitte, mütekellim yâsından başkasına muzâf olduğunda vâv ile ref', elif ile nasb, yâ ile cer edilir." + R_TR},
 "tokens": [
  tok("وَالْأَسْمَاءُ", "ism", "noun", [K, "mubtada-khabar", "jam-taksir", "five-nouns"], "الْوَاوُ عَاطِفَةٌ، وَالْأَسْمَاءُ مُبْتَدَأٌ — جَمْعُ اسْمٍ.", "«and the nouns» — the mubtada.", "«esmâ» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْأَسْمَاءُ", "ism", "noun")]),
  tok("السِّتَّةُ", "sitta", "noun", [K, "naat-sifa", "five-nouns"], "صِفَةٌ مَرْفُوعَةٌ — أَبٌ أَخٌ حَمٌ هَنٌ فُو ذُو.", "«six» — ab, akh, ham, han, fu, dhu.", "«altı» — eb, ah, ham, hen, fû, zû."),
  tok("مُضَافَةً", "mudaf", "noun", [K, "hal", "ism-maful"], "حَالٌ مَنْصُوبٌ — اسْمُ مَفْعُولِ أَضَافَ.", "«when annexed» — a hal.", "«muzâf olarak» — hâl."),
  ila(),
  tok("غَيْرِ", "ghayr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«other than».", "«…-dan başkasına»."),
  tok("يَاءِ", "ya-letter", "noun", [K, "idafa-definiteness", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the ya of».", "«yâsı»."),
  tok("الْمُتَكَلِّمِ", "mutakallim", "noun", [K, "idafa-definiteness", "ism-fail", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker».", "«mütekellim»."),
  passive_pl("تُرْفَعُ", "rafaa", "تُرْفَعُ", "«are raised».", "«ref' edilir».", ["mubtada-khabar"]),
  sign("بِالْوَاوِ", "waw-letter", "waw", "vâv"),
  passive_pl("وَتُنْصَبُ", "nasaba-set", "تُنْصَبُ", "«made accusative».", "«nasb».", ["atf-nasaq"], wa=True),
  sign("بِالْأَلِفِ", "alif-letter", "alif", "elif"),
  passive_pl("وَتُجَرُّ", "jarra", "تُجَرُّ", "«and genitive».", "«ve cer edilir».", ["atf-nasaq", "doubled-verbs"], wa=True),
  sign("بِالْيَاءِ", "ya-letter", "ya", "yâ", punct="."),
 ]})

# ----------- s18 (RESTORED)
S.append({"id": "s18", "translation": {
 "en": "The sound masculine plural, ulu, ʿishrun and its sisters are raised by the waw and made accusative and genitive by the ya." + R_EN,
 "tr": "Cem-i müzekker sâlim, ulû, işrûn ve kardeşleri vâv ile ref', yâ ile nasb ve cer edilir." + R_TR},
 "tokens": [
  tok("وَجَمْعُ", "jam", "noun", [K, "mubtada-khabar", "idafa-definiteness", "jam-mudhakkar-salim"], "الْوَاوُ عَاطِفَةٌ، وَجَمْعُ مُبْتَدَأٌ، مُضَافٌ.", "«and the plural of» — the mubtada.", "«cem'i» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("جَمْعُ", "jam", "noun")]),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, "idafa-definiteness", "ism-maful", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ ذَكَّرَ.", "«the masculine».", "«müzekkerin»."),
  tok("السَّالِمُ", "salim", "noun", [K, "naat-sifa", "ism-fail"], "صِفَةٌ لِجَمْعُ مَرْفُوعَةٌ.", "«sound».", "«sâlim»."),
  tok("وَأُولُو", "ulu", "noun", [K, "atf-nasaq", "jam-mudhakkar-salim"], "الْوَاوُ عَاطِفَةٌ، وَأُولُو مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِالْجَمْعِ، جَمْعُ ذُو سَمَاعًا.", "«ulu» — «possessors of», the plural of ذُو by usage, attached to the sound plural.", "«ulû» — zû'nun semâî cem'i, sâlim cem'e mülhak.", segments=[seg("وَ", "wa", "conj"), seg("أُولُو", "ulu", "noun")]),
  tok("وَعِشْرُونَ", "ishrun", "noun", [K, "atf-nasaq", "jam-mudhakkar-salim"], "الْوَاوُ عَاطِفَةٌ، وَعِشْرُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ.", "«twenty».", "«yirmi».", segments=[seg("وَ", "wa", "conj"), seg("عِشْرُونَ", "ishrun", "noun")]),
  tok("وَأَخَوَاتُهَا", "ukht", "noun", [K, "atf-nasaq", "jam-muannath-salim", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَأَخَوَاتُ مَعْطُوفٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — ثَلَاثُونَ إِلَى تِسْعِينَ.", "«and its sisters» — thirty to ninety.", "«ve kardeşleri» — otuzdan doksana.", segments=[seg("وَ", "wa", "conj"), seg("أَخَوَاتُ", "ukht", "noun"), pr3fs()]),
  passive_pl("تُرْفَعُ", "rafaa", "تُرْفَعُ", "«are raised».", "«ref' edilir».", ["mubtada-khabar"]),
  sign("بِالْوَاوِ", "waw-letter", "waw", "vâv"),
  passive_pl("وَتُنْصَبُ", "nasaba-set", "تُنْصَبُ", "«made accusative».", "«nasb».", ["atf-nasaq"], wa=True),
  passive_pl("وَتُجَرُّ", "jarra", "تُجَرُّ", "«and genitive».", "«ve cer edilir».", ["atf-nasaq", "doubled-verbs"], wa=True),
  sign("بِالْيَاءِ", "ya-letter", "ya", "yâ", punct="."),
 ]})

# ----------- s19
S.append({"id": "s19", "translation": {
 "en": "As in: Muslims came to me, and I saw Muslims, and I passed by Muslims.",
 "tr": "Meselâ: Müslümanlar bana geldi; Müslümanları gördüm; Müslümanlara uğradım."},
 "tokens": [
  nahwu(), jaani(),
  tok("مُسْلِمُونَ", "muslim", "noun", [K, "fail", "jam-mudhakkar-salim"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«Muslims» — the doer, by the waw.", "«Müslümanlar» — fâil, vâv ile.", punct="،"),
  raaytu(),
  tok("مُسْلِمِينَ", "muslim", "noun", [K, "maful-bihi", "jam-mudhakkar-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«Muslims» — the object, by the ya.", "«Müslümanları» — mef'ûl, yâ ile.", punct="،"),
  marartu(),
  bi_("بِمُسْلِمِينَ", "muslim", "noun", ["jam-mudhakkar-salim"], "مُسْلِمِينَ مَجْرُورٌ بِالْيَاءِ.", "«by Muslims».", "«Müslümanlara».", "مُسْلِمِينَ"),
 ]})

# ----------- s20 (RESTORED)
S.append({"id": "s20", "translation": {
 "en": "The dual, ithnan and kila when annexed to a pronoun are raised by the alif and made accusative and genitive by the ya." + R_EN,
 "tr": "Tesniye, isnân ve zamire muzâf olan kilâ elif ile ref', yâ ile nasb ve cer edilir." + R_TR},
 "tokens": [
  tok("وَالْمُثَنَّى", "muthanna", "noun", [K, "mubtada-khabar", "al-muthanna", "ism-maful", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالْمُثَنَّى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«and the dual» — the mubtada, maqsur.", "«tesniye» — mübtedâ, maksûr.", segments=[seg("وَ", "wa", "conj"), seg("الْمُثَنَّى", "muthanna", "noun")]),
  tok("وَاثْنَانِ", "ithnan", "noun", [K, "atf-nasaq", "al-muthanna"], "الْوَاوُ عَاطِفَةٌ، وَاثْنَانِ مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ — مُلْحَقٌ بِالْمُثَنَّى.", "«ithnan» — «two», attached to the dual.", "«isnân» — tesniyeye mülhak.", segments=[seg("وَ", "wa", "conj"), seg("اثْنَانِ", "ithnan", "noun")]),
  tok("وَكِلَا", "kila", "noun", [K, "atf-nasaq", "al-muthanna", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَكِلَا مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — لَفْظُهُ مُفْرَدٌ وَمَعْنَاهُ مُثَنًّى.", "«kila» — «both»: single in wording, dual in sense.", "«kilâ» — lafzı müfred, manası tesniye.", segments=[seg("وَ", "wa", "conj"), seg("كِلَا", "kila", "noun")]),
  tok("مُضَافًا", "mudaf", "noun", [K, "hal", "ism-maful"], "حَالٌ مِنْ كِلَا مَنْصُوبٌ.", "«when annexed» — a hal of kila.", "«muzâf olarak» — kilâ'dan hâl."),
  ila(),
  tok("الضَّمِيرِ", "damir", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«a pronoun».", "«zamire»."),
  passive_pl("تُرْفَعُ", "rafaa", "تُرْفَعُ", "«are raised».", "«ref' edilir».", ["mubtada-khabar"]),
  sign("بِالْأَلِفِ", "alif-letter", "alif", "elif"),
  passive_pl("وَتُنْصَبُ", "nasaba-set", "تُنْصَبُ", "«made accusative».", "«nasb».", ["atf-nasaq"], wa=True),
  passive_pl("وَتُجَرُّ", "jarra", "تُجَرُّ", "«and genitive».", "«ve cer edilir».", ["atf-nasaq", "doubled-verbs"], wa=True),
  sign("بِالْيَاءِ", "ya-letter", "ya", "yâ", punct="."),
 ]})

# ----------- s21
S.append({"id": "s21", "translation": {
 "en": "As in: the two came to us, both of them; and we followed the two, both of them; and we worked with the two, both of them.",
 "tr": "Meselâ: ikisi, her ikisi de bize geldi; ikisine, her ikisine de uyduk; ikisiyle, her ikisiyle de çalıştık."},
 "tokens": [
  nahwu(),
  tok("جَاءَنَا", "jaa", "verb", [K, "fail", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ، وَنَا مَفْعُولٌ بِهِ.", "«came to us».", "«bize geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1p()]),
  tok("الِاثْنَانِ", "ithnan", "noun", [K, "fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ.", "«the two» — the doer, by the alif.", "«ikisi» — fâil, elif ile."),
  tok("كِلَاهُمَا", "kila", "noun", [K, "tawkid", "al-muthanna", "idafa-definiteness"], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ بِالْأَلِفِ، وَهُمَا مُضَافٌ إِلَيْهِ — أُعْرِبَ بِالْحَرْفِ لِإِضَافَتِهِ إِلَى الضَّمِيرِ.", "«both of them» — an emphasis by the alif, declined by letter because annexed to a pronoun.", "«her ikisi de» — te'kîd, elif ile; zamire muzâf olduğu için harfle i'râb.", segments=[seg("كِلَا", "kila", "noun"), pr3d()], punct="،"),
  tok("وَاتَّبَعْنَا", "ittabaa", "verb", [K, "fail", "form-viii-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَاتَّبَعَ فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ.", "«and we followed» — Form VIII, نَا the doer.", "«ve uyduk» — iftiâl, nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("اتَّبَعْنَا", "ittabaa", "verb")]),
  tok("الِاثْنَيْنِ", "ithnan", "noun", [K, "maful-bihi", "al-muthanna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«the two» — the object, by the ya.", "«ikisine» — mef'ûl, yâ ile."),
  tok("كِلَيْهِمَا", "kila", "noun", [K, "tawkid", "al-muthanna", "idafa-definiteness"], "تَوْكِيدٌ مَنْصُوبٌ بِالْيَاءِ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«both of them» — by the ya.", "«her ikisine de» — yâ ile.", segments=[seg("كِلَيْ", "kila", "noun"), pr3d()], punct="،"),
  tok("وَعَمِلْنَا", "amila", "verb", [K, "fail", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَعَمِلَ فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ.", "«and we worked».", "«ve çalıştık».", segments=[seg("وَ", "wa", "conj"), seg("عَمِلْنَا", "amila", "verb")]),
  bi_("بِالِاثْنَيْنِ", "ithnan", "noun", ["al-muthanna"], "الِاثْنَيْنِ مَجْرُورٌ بِالْيَاءِ.", "«with the two» — by the ya.", "«ikisiyle» — yâ ile.", "الِاثْنَيْنِ", punct=None),
  tok("كِلَيْهِمَا", "kila", "noun", [K, "tawkid", "al-muthanna", "idafa-definiteness"], "تَوْكِيدٌ مَجْرُورٌ بِالْيَاءِ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«both of them».", "«her ikisiyle de».", segments=[seg("كِلَيْ", "kila", "noun"), pr3d()], punct="."),
 ]})

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "murab": need("murab", "مُعْرَب", "ع ر ب", "noun", "declinable — the noun whose ending changes with its governor (ism maf'ul of Form IV أَعْرَبَ)", "mu'reb — sonu âmiliyle değişen isim (i'râb'ın ism-i mef'ûlü)", 4),
 "mutawir": need("mutawir", "مُعْتَوِر", "ع و ر", "noun", "coming in turn, alternating (ism fa'il of Form VIII اعْتَوَرَ, its waw kept) — الْمَعَانِي الْمُعْتَوِرَة: the meanings that take turns on the word's end", "sırayla gelen, nöbetleşen (i'tevere'nin ism-i fâili) — el-meânî'l-mu'tevire", 6),
 "alam-sign": need("alam-sign", "عَلَم (الْعَلَامَة)", "ع ل م", "noun", "a sign, a mark — عَلَمُ الْفَاعِلِيَّةِ: the sign of doerhood (pl. أَعْلَام)", "alâmet, nişan — alemü'l-fâiliyye: fâiliyet alâmeti (ç. أَعْلَام)", 4, plural="أَعْلَام"),
 "failiyya": need("failiyya", "فَاعِلِيَّة", "ف ع ل", "noun", "doerhood — being the doer (an artificial masdar from فَاعِل)", "fâiliyet — fâil olma (masdar-ı sınâî)", 5),
 "mafuliyya": need("mafuliyya", "مَفْعُولِيَّة", "ف ع ل", "noun", "objecthood — being the object (an artificial masdar from مَفْعُول)", "mef'ûliyet — mef'ûl olma (masdar-ı sınâî)", 5),
 "taqawwama": need("taqawwama", "تَقَوَّمَ", "ق و م", "verb", "to come to stand, to be constituted by (Form V; تَقَوَّمَ يَتَقَوَّمُ بِـ)", "kâim olmak, hâsıl olmak (tefa''ul; tekavveme yetekavvemu bi-)", 5),
 "muqtadi": need("muqtadi", "مُقْتَضٍ (الْمُقْتَضِي)", "ق ض ي", "noun", "requiring, demanding (ism fa'il of Form VIII اقْتَضَى; a manqus)", "gerektiren, iktizâ eden (iktazâ'nın ism-i fâili; mankûs)", 5),
 "hasala": need("hasala", "حَصَلَ", "ح ص ل", "verb", "to come about, to result (حَصَلَ يَحْصُلُ)", "hâsıl olmak (hasale yahsulu)", 3),
 "rafaa": need("rafaa", "رَفَعَ", "ر ف ع", "verb", "to raise; to put in the nominative (رَفَعَ يَرْفَعُ)", "kaldırmak; ref' etmek (rafea yerfeu)", 3),
 "nasaba-set": need("nasaba-set", "نَصَبَ", "ن ص ب", "verb", "to set up; to put in the accusative (نَصَبَ يَنْصُبُ)", "dikmek; nasb etmek (nasabe yansubu)", 3),
 "jarra": need("jarra", "جَرَّ", "ج ر ر", "verb", "to drag; to put in the genitive (doubled; جَرَّ يَجُرُّ)", "çekmek; cer etmek (muzâaf; cerre yecurru)", 3),
 "munsarif": need("munsarif", "مُنْصَرِف", "ص ر ف", "noun", "triptote — a noun that takes the tanwin and the kasra (ism fa'il of Form VII انْصَرَفَ); غَيْرُ مُنْصَرِفٍ: diptote", "munsarif — tenvin ve kesre alan isim (insarafe'nin ism-i fâili); gayr-i munsarif", 4),
 "mukassar": need("mukassar", "مُكَسَّر", "ك س ر", "noun", "broken — جَمْعٌ مُكَسَّر: the broken plural (ism maf'ul of Form II كَسَّرَ)", "mükesser — cem-i mükesser (kessere'nin ism-i mef'ûlü)", 4),
 "damma": need("damma", "ضَمَّة", "ض م م", "noun", "the damma — the u-vowel sign, the sign of rafʿ", "damme — ötre, ref' alâmeti", 2),
 "fatha": need("fatha", "فَتْحَة", "ف ت ح", "noun", "the fatha — the a-vowel sign, the sign of nasb", "fetha — üstün, nasb alâmeti", 2),
 "kasra": need("kasra", "كَسْرَة", "ك س ر", "noun", "the kasra — the i-vowel sign, the sign of jarr", "kesre — esre, cer alâmeti", 2),
 "salim": need("salim", "سَالِم", "س ل م", "noun", "sound, whole (ism fa'il of سَلِمَ) — جَمْعٌ سَالِم: the sound plural", "sâlim, sağlam (selime'nin ism-i fâili) — cem-i sâlim", 3),
 "muannath": need("muannath", "مُؤَنَّث", "أ ن ث", "noun", "feminine (ism maf'ul of Form II أَنَّثَ)", "müennes (ennese'nin ism-i mef'ûlü)", 3),
 "mudhakkar": need("mudhakkar", "مُذَكَّر", "ذ ك ر", "noun", "masculine (ism maf'ul of Form II ذَكَّرَ)", "müzekker (zekkere'nin ism-i mef'ûlü)", 3),
 "muslima": need("muslima", "مُسْلِمَة", "س ل م", "noun", "a Muslim woman (pl. مُسْلِمَات)", "Müslüman kadın (ç. مُسْلِمَات)", 2, plural="مُسْلِمَات"),
 "ahmad": need("ahmad", "أَحْمَد", "ح م د", "propn", "Ahmad — a proper name on the verb pattern أَفْعَل, hence a diptote", "Ahmed — ef'al vezninde alem, bu yüzden gayr-i munsarif", 2),
 "ya-letter": need("ya-letter", "يَاء", "ي ي ي", "noun", "the letter ya — يَاءُ الْمُتَكَلِّمِ: the speaker's ya", "yâ harfi — yâü'l-mütekellim", 2),
 "waw-letter": need("waw-letter", "وَاو", "و و و", "noun", "the letter waw", "vâv harfi", 2),
 "alif-letter": need("alif-letter", "أَلِف", "أ ل ف", "noun", "the letter alif", "elif harfi", 2),
 "ulu": need("ulu", "أُولُو", "أ و ل", "noun", "«possessors of» — the plural of ذُو by usage, declined like the sound masculine plural (أُولُو / أُولِي)", "ulû — «sahipleri»: zû'nun semâî cem'i, cem-i müzekker sâlim gibi i'râb edilir", 5),
 "ishrun": need("ishrun", "عِشْرُونَ", "ع ش ر", "noun", "twenty — declined like the sound masculine plural (عِشْرُونَ / عِشْرِينَ)", "yirmi — cem-i müzekker sâlim gibi i'râb edilir", 3),
 "ukht": need("ukht", "أُخْت", "أ خ و", "noun", "a sister (pl. أَخَوَات) — وَأَخَوَاتُهَا: «and its sisters», the words that behave like it", "kız kardeş (ç. أَخَوَات) — ve ahavâtühâ: «ve kardeşleri»", 2, plural="أَخَوَات"),
 "muthanna": need("muthanna", "مُثَنًّى", "ث ن ي", "noun", "the dual (ism maf'ul of Form II ثَنَّى; a maqsur)", "tesniye (sennâ'nın ism-i mef'ûlü; maksûr)", 3),
 "haulai": need("haulai", "هَؤُلَاءِ", None, "pron", "these (the plural demonstrative, built on kasra)", "bunlar (cemi işaret ismi, kesre üzere mebnî)", 2),
}
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

# ---------------------------------------------------------------- paradigms
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "taqawwama", _sg.derived(_sg.B5, _sg.W5, "َ", "تَقَوَّم", "تَقَوَّم", "تَقَوَّم", "تَقَوُّم", "مُتَقَوِّم", None, None, None, "تَقَوَّمَ الشَّيْءُ بِكَذَا: قَامَ بِهِ وَحَصَلَ — لَازِمٌ."))
put_morph(mo, "hasala", _sg.sound1("nasara", "حَصَل", "حْصُل", "اُحْصُل", "حُصُول", "حَاصِل", None, None, None, "حَصَلَ الشَّيْءُ يَحْصُلُ: وَقَعَ وَتَحَقَّقَ — مِنْ بَابِ نَصَرَ."))
put_morph(mo, "rafaa", _sg.sound1("fataha", "رَفَع", "رْفَع", "اِرْفَع", "رَفْع", "رَافِع", "مَرْفُوع", "رُفِعَ", "يُرْفَعُ", "رَفَعَ يَرْفَعُ: أَعْلَى؛ وَفِي النَّحْوِ: جَعَلَهُ مَرْفُوعًا — مِنْ بَابِ فَتَحَ لِأَجْلِ حَرْفِ الْحَلْقِ."))
put_morph(mo, "nasaba-set", _sg.sound1("nasara", "نَصَب", "نْصُب", "اُنْصُب", "نَصْب", "نَاصِب", "مَنْصُوب", "نُصِبَ", "يُنْصَبُ", "نَصَبَ يَنْصُبُ: أَقَامَ؛ وَفِي النَّحْوِ: جَعَلَهُ مَنْصُوبًا — مِنْ بَابِ نَصَرَ."))
put_morph(mo, "jarra", gem("nasara", "جَرّ", "جَرَر", "جُرّ", "جْرُر", ["جُرَّ", "جُرَّا", "جُرُّوا", "جُرِّي", "جُرَّا", "اُجْرُرْنَ"], "جَرّ", "جَارّ", "مَجْرُور", "جُرَّ", "يُجَرُّ", "جَرَّ يَجُرُّ: سَحَبَ؛ وَفِي النَّحْوِ: جَعَلَهُ مَجْرُورًا — مُضَاعَفٌ مِنْ بَابِ نَصَرَ."))
put_morph(mo, "amila", _sg.sound1("samia", "عَمِل", "عْمَل", "اِعْمَل", "عَمَل", "عَامِل", "مَعْمُول", "عُمِلَ", "يُعْمَلُ", "عَمِلَ يَعْمَلُ: فَعَلَ وَصَنَعَ — مِنْ بَابِ سَمِعَ."))
put_morph(mo, "ittabaa", _sg.derived(B8, W8, "َ", "اِتَّبَع", "تَّبِع", "اِتَّبِع", "اِتِّبَاع", "مُتَّبِع", "مُتَّبَع", "اُتُّبِعَ", "يُتَّبَعُ", "اتَّبَعَهُ يَتَّبِعُهُ: تَبِعَهُ — أَصْلُهُ اِتْتَبَعَ، أُدْغِمَتِ التَّاءَانِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch2 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": K,
 "title": {"ar": "الْمُعْرَبُ وَالْمَبْنِيُّ وَالْإِعْرَابُ", "en": "The declinable and the indeclinable, and the iʿrab: the Kafiya's definitions", "tr": "Mu'reb ve mebnî, ve i'râb: Kâfiye'nin tarifleri"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الاسم منه معرب ومبني؛ المعرب المركب الذي لم يشبه مبني الأصل؛ الإعراب ما اختلف آخره به ليدل على المعاني المعتورة عليه", "الفوائد الضيائية لملا جامي — مسألة الأسماء المعدودة: مبنية عند المصنف، معربة عند الزمخشري"],
 "question": {
  "en": ["What is the MUʿRAB? The compounded word that does not resemble what is indeclinable by origin: الْمُرَكَّبُ الَّذِي لَمْ يُشْبِهْ مَبْنِيَّ الْأَصْلِ. «Compounded» means set into a construction with its governor: Zayd in ضَرَبَ زَيْدٌ is compounded with ضَرَبَ, and it resembles no particle, so it is declinable. هَؤُلَاءِ in قَامَ هَؤُلَاءِ resembles the particle (it points by itself, like a harf), so it is indeclinable.",
         "Molla Jami's question: are the words counted one by one — alif, ba, ta, Zayd, ʿAmr, Bakr — muʿrab or mabni? For the author they are mabni, since they stand in no construction; for Zamakhshari they are muʿrab, since they resemble no mabni and would accept iʿrab the moment they entered a construction.",
         "What is IʿRAB? That by which the end of the word differs, so as to point to the meanings that come over it in turn — مَا اخْتَلَفَ آخِرُهُ بِهِ لِيَدُلَّ عَلَى الْمَعَانِي الْمُعْتَوِرَةِ عَلَيْهِ. The «meanings» are doerhood, objecthood and annexation; the iʿrab is the vowel or the letter that changes at the end to mark which one holds. Its kinds are three: RAFʿ the sign of doerhood, NASB the sign of objecthood, JARR the sign of annexation — really or by ruling (a khabar is raised «by ruling» as if it were a doer).",
         "What is the ʿAMIL? That by which the meaning requiring the iʿrab comes to stand: مَا بِهِ يَتَقَوَّمُ الْمَعْنَى الْمُقْتَضِي لِلْإِعْرَابِ. In جَاءَنِي زَيْدٌ the doerhood that requires the rafʿ came about through جَاءَ, so جَاءَ is the governor.",
         "How do the classes decline? By VOWEL: the triptote single and broken plural (damma / fatha / kasra: زَيْدٌ، رِجَالٌ), the sound feminine plural (damma / kasra / kasra: مُسْلِمَاتٌ), the diptote (damma / fatha / fatha: أَحْمَدُ). By LETTER: the six nouns annexed to other than the speaker's ya (waw / alif / ya: أَبُوهُ), the sound masculine plural with أُولُو and the tens (waw / ya / ya: مُسْلِمُونَ), the dual with اثْنَانِ and كِلَا annexed to a pronoun (alif / ya / ya: الِاثْنَانِ كِلَاهُمَا). The notebook's triplet جَاءَنِي / رَأَيْتُ / مَرَرْتُ بِـ is the test-bench for every class.",
         "What does the engine read? The DabtEngine's case layer is exactly this chapter: it assigns rafʿ / nasb / jarr by the seat (doer, object, annex, after a preposition) and then writes the SIGN by the class — the vowel for the triptote, the kasra-for-fatha of the sound feminine plural, the fatha-for-kasra of the diptote, the waw/alif/ya of the six nouns and the sound masculine plural, the alif/ya of the dual and of كِلَا before a pronoun. The example triplets of s7–s21 are graded against the notebook's own marks."],
  "tr": ["MU'REB nedir? Aslen mebnî olana benzemeyen mürekkeb: الْمُرَكَّبُ الَّذِي لَمْ يُشْبِهْ مَبْنِيَّ الْأَصْلِ. «Mürekkeb», âmiliyle terkibe girmiş demektir: ضَرَبَ زَيْدٌ'deki Zeyd darabe ile terkib edilmiştir ve hiçbir harfe benzemez, öyleyse mu'rebdir. قَامَ هَؤُلَاءِ'deki هَؤُلَاءِ harfe benzer (harf gibi kendi başına işaret eder), öyleyse mebnîdir.",
         "Molla Câmî'nin sorusu: tek tek sayılan kelimeler — elif, bâ, tâ, Zeyd, Amr, Bekr — mu'reb mi mebnî mi? Müellife göre mebnîdir, çünkü terkibde vâki olmamışlardır; Zemahşerî'ye göre mu'rebdir, çünkü mebnîye benzemezler ve terkibe girdikleri an i'râbı kabul ederler.",
         "İ'RÂB nedir? Üzerine sırayla gelen manalara delâlet etmesi için kendisiyle kelimenin sonunun değiştiği şey — مَا اخْتَلَفَ آخِرُهُ بِهِ لِيَدُلَّ عَلَى الْمَعَانِي الْمُعْتَوِرَةِ عَلَيْهِ. «Manalar» fâiliyet, mef'ûliyet ve izâfettir; i'râb sonda değişip hangisinin bulunduğunu gösteren hareke ya da harftir. Çeşitleri üçtür: REF' fâiliyetin, NASB mef'ûliyetin, CER izâfetin alâmeti — hakikaten ya da hükmen (haber, fâil imiş gibi «hükmen» merfûdur).",
         "ÂMİL nedir? İ'râbı gerektiren mananın kendisiyle hâsıl olduğu şey: مَا بِهِ يَتَقَوَّمُ الْمَعْنَى الْمُقْتَضِي لِلْإِعْرَابِ. جَاءَنِي زَيْدٌ'de ref'i gerektiren fâiliyet جَاءَ ile hâsıl olmuştur, öyleyse âmil جَاءَ'dir.",
         "Sınıflar nasıl i'râb alır? HAREKE ile: munsarif müfred ve cem-i mükesser (damme / fetha / kesre: زَيْدٌ، رِجَالٌ), cem-i müennes sâlim (damme / kesre / kesre: مُسْلِمَاتٌ), gayr-i munsarif (damme / fetha / fetha: أَحْمَدُ). HARF ile: mütekellim yâsından başkasına muzâf esmâ-i sitte (vâv / elif / yâ: أَبُوهُ), أُولُو ve onlarla birlikte cem-i müzekker sâlim (vâv / yâ / yâ: مُسْلِمُونَ), اثْنَانِ ve zamire muzâf كِلَا ile tesniye (elif / yâ / yâ: الِاثْنَانِ كِلَاهُمَا). Defterin جَاءَنِي / رَأَيْتُ / مَرَرْتُ بِـ üçlüsü her sınıfın deney tezgâhıdır.",
         "Motor neyi okur? DabtEngine'in hâl katmanı tam bu bâbdır: yere göre (fâil, mef'ûl, muzâfun ileyh, harf-i cerden sonra) ref' / nasb / cer verir, sonra ALÂMETİ sınıfa göre yazar — munsarif için hareke, cem-i müennes sâlimin fetha yerine kesresi, gayr-i munsarifin kesre yerine fethası, esmâ-i sitte ile cem-i müzekker sâlimin vâv/elif/yâsı, tesniyenin ve zamir önündeki كِلَا'nın elif/yâsı. s7–s21'in örnek üçlüleri defterin kendi harekelerine karşı notlanır."]},
 "plain": {
  "en": "A noun is declinable when it sits in a construction and resembles no particle; iʿrab is the changing ending that marks doer (rafʿ), object (nasb) or annex (jarr); the governor is what brings that meaning about. Vowel classes and letter classes each have their own signs.",
  "tr": "İsim, terkibde durup harfe benzemiyorsa mu'rebdir; i'râb, fâili (ref'), mef'ûlü (nasb) ya da muzâfun ileyhi (cer) gösteren değişen sondur; âmil o manayı meydana getirendir. Hareke sınıflarının ve harf sınıflarının kendi alâmetleri vardır."},
 "explanation": {
  "en": "الْمُعْرَبُ الْمُرَكَّبُ الَّذِي لَمْ يُشْبِهْ مَبْنِيَّ الْأَصْلِ. Ibn al-Hajib defines the declinable by two conditions — it must stand in a construction (the tarkib with a governor) and must not resemble the things that are indeclinable by origin (the particle, the mazi, the amr). The iʿrab is then defined by its function: the changing end that points to the meanings that alternate on the word — doerhood, objecthood, annexation — and its three kinds are named as signs (ʿalam) of those meanings. The ʿamil is what makes the meaning come about. The rest of the chapter is the notebook's table of classes: three that decline by vowel (the triptote single and broken plural; the sound feminine plural with its kasra for the fatha; the diptote with its fatha for the kasra) and three that decline by letter (the six nouns; the sound masculine plural with its attached أُولُو and the tens; the dual with اثْنَانِ and كِلَا before a pronoun), each proved by the triplet جَاءَنِي / رَأَيْتُ / مَرَرْتُ بِـ.",
  "tr": "الْمُعْرَبُ الْمُرَكَّبُ الَّذِي لَمْ يُشْبِهْ مَبْنِيَّ الْأَصْلِ. İbnü'l-Hâcib mu'rebi iki şartla tarif eder — terkibde bulunmalı (âmille terkib) ve aslen mebnî olanlara (harf, mâzî, emir) benzememeli. İ'râb ise işleviyle tarif edilir: kelime üzerinde nöbetleşen manalara — fâiliyet, mef'ûliyet, izâfet — delâlet eden değişen son; üç çeşidi bu manaların alâmetleri (alem) olarak adlandırılır. Âmil, manayı meydana getirendir. Bâbın kalanı defterin sınıflar tablosudur: hareke ile i'râb alan üç sınıf (munsarif müfred ve cem-i mükesser; fetha yerine kesresiyle cem-i müennes sâlim; kesre yerine fethasıyla gayr-i munsarif) ve harf ile i'râb alan üç sınıf (esmâ-i sitte; mülhakı أُولُو ve onlarla cem-i müzekker sâlim; اثْنَانِ ve zamir önündeki كِلَا ile tesniye), her biri جَاءَنِي / رَأَيْتُ / مَرَرْتُ بِـ üçlüsüyle ispat edilir."},
 "examples": [
  {"ar": "الْمُعْرَبُ الْمُرَكَّبُ الَّذِي لَمْ يُشْبِهْ مَبْنِيَّ الْأَصْلِ", "en": "The definition of the declinable.", "tr": "Mu'rebin tarifi.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "وَالْإِعْرَابُ مَا اخْتَلَفَ آخِرُهُ بِهِ لِيَدُلَّ عَلَى الْمَعَانِي الْمُعْتَوِرَةِ عَلَيْهِ", "en": "The definition of iʿrab.", "tr": "İ'râbın tarifi.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "فَالرَّفْعُ عَلَمُ الْفَاعِلِيَّةِ، وَالنَّصْبُ عَلَمُ الْمَفْعُولِيَّةِ، وَالْجَرُّ عَلَمُ الْإِضَافَةِ", "en": "The three kinds as signs.", "tr": "Üç çeşit, alâmet olarak.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَالْعَامِلُ مَا بِهِ يَتَقَوَّمُ الْمَعْنَى الْمُقْتَضِي لِلْإِعْرَابِ", "en": "The definition of the governor.", "tr": "Âmilin tarifi.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "جَاءَنِي أَبُوهُ، وَرَأَيْتُ أَبَاهُ، وَمَرَرْتُ بِأَبِيهِ", "en": "The six nouns declined by letter.", "tr": "Esmâ-i sittenin harfle i'râbı.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "جَاءَنَا الِاثْنَانِ كِلَاهُمَا، وَاتَّبَعْنَا الِاثْنَيْنِ كِلَيْهِمَا", "en": "كِلَا before a pronoun declines like the dual.", "tr": "Zamir önündeki kilâ tesniye gibi i'râb alır.", "sourceStory": "al-kafiya", "sentence": "s21"}],
 "commonMistakes": [
  {"wrong": "«Mu'reb, sonu değişen kelimedir; mebnî ise değişmeyen»",
   "right": "«الْمُعْرَبُ الْمُرَكَّبُ الَّذِي لَمْ يُشْبِهْ مَبْنِيَّ الْأَصْلِ — tarif terkib ve benzememe iledir, sonun değişmesi netice»",
   "why": {"en": "The Kafiya defines the declinable by its conditions (construction, no resemblance to the particle), not by the visible change; the change is what follows, and it may even be estimated (عَصًا, قَاضٍ).", "tr": "Kâfiye mu'rebi şartlarıyla (terkib, harfe benzememe) tarif eder, görünen değişmeyle değil; değişme neticedir, hattâ takdîrî olabilir (عَصًا, قَاضٍ)."}},
  {"wrong": "«رَأَيْتُ مُسْلِمَاتًا — cem-i müennes sâlim fetha ile nasb edilir»",
   "right": "«رَأَيْتُ مُسْلِمَاتٍ — nasbı da cerri de kesre iledir»",
   "why": {"en": "The sound feminine plural takes the kasra in place of the fatha; the tanwin stays but the vowel is the kasra.", "tr": "Cem-i müennes sâlim fetha yerine kesre alır; tenvin kalır ama hareke kesredir."}},
  {"wrong": "«مَرَرْتُ بِأَحْمَدٍ — her isim harf-i cerden sonra kesre alır»",
   "right": "«مَرَرْتُ بِأَحْمَدَ — gayr-i munsarifin cerri fetha ile, tenvinsiz»",
   "why": {"en": "The diptote refuses the kasra and the tanwin; its jarr is by the fatha (unless it is annexed or takes the article).", "tr": "Gayr-i munsarif kesreyi ve tenvini kabul etmez; cerri fetha iledir (muzâf olmadıkça ya da lâm almadıkça)."}},
  {"wrong": "«كِلَا her zaman elif ile merfû, yâ ile mansûb ve mecrûrdur»",
   "right": "«جَاءَنِي كِلَا الرَّجُلَيْنِ، وَرَأَيْتُ كِلَا الرَّجُلَيْنِ — zâhir isme muzâf olunca i'râbı takdîrî harekeyledir»",
   "why": {"en": "Only كِلَا annexed to a pronoun declines by letter like the dual; annexed to an overt noun it keeps its alif and its iʿrab is estimated.", "tr": "Yalnız zamire muzâf كِلَا tesniye gibi harfle i'râb alır; zâhir isme muzâf olunca elifi kalır, i'râbı takdîrîdir."}}],
 "relatedNotes": [K1, "fail", "maful-bihi", "huruf-jarr", "five-nouns", "jam-mudhakkar-salim", "jam-muannath-salim", "mamnu-min-sarf", "al-muthanna", "jam-taksir", "tawkid"]}

ADD_EN = (" Chapter 2 (notebook lines ~118-160): the muʿrab and the mabni (s1-s3), the iʿrab's definition (s4), its three kinds and what each signs (s5-s6) "
          "with the notebook's triplets (s7-s8), the ʿamil (s9-s10), and the declension classes — the triptote single and broken plural (s11-s12), the sound "
          "feminine plural (s13-s14), the diptote (s15-s16), the six nouns (s17), the sound masculine plural with أُولُو and عِشْرُونَ (s18-s19), the dual with "
          "اثْنَانِ and كِلَا (s20-s21). Rulings the notebook gives only in Turkish are RESTORED from the received matn and marked; the teacher's worked "
          "examples (s3, s10) are marked as commentary.")
ADD_TR = (" İkinci bâb (defter satırları ~118-160): mu'reb ve mebnî (s1-s3), i'râbın tarifi (s4), üç çeşidi ve her birinin alâmeti (s5-s6) ve defterin "
          "üçlüleri (s7-s8), âmil (s9-s10) ve i'râb sınıfları — munsarif müfred ve cem-i mükesser (s11-s12), cem-i müennes sâlim (s13-s14), gayr-i munsarif "
          "(s15-s16), esmâ-i sitte (s17), أُولُو ve عِشْرُونَ ile cem-i müzekker sâlim (s18-s19), اثْنَانِ ve كِلَا ile tesniye (s20-s21). Defterin yalnız "
          "Türkçe verdiği hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; hocanın işlenmiş örnekleri (s3, s10) şerh olarak işaretlidir.")
write_out(2, S, TITLE, ADD_EN, ADD_TR, "118-160", GLOSS_ADD, notes=(NOTE,),
          related=((K1, [K]), ("five-nouns", [K]), ("jam-mudhakkar-salim", [K]), ("jam-muannath-salim", [K]), ("mamnu-min-sarf", [K]), ("al-muthanna", [K])))
report(2, S, GLOSS_ADD, (NOTE,))
