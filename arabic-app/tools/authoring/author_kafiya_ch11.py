# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 11: THE FEMININE AND THE MASCULINE. The feminine defined (the notebook's Arabic), its marks (the ta, the short and the
long alif), the real and the verbal feminine (the notebook's Arabic), and the verb's ta of femininity: obligatory for the real feminine
adjoining its verb and for the pronoun of any feminine, optional across a gap and for the apparent non-real feminine, likewise for the
apparent broken plural — and the pronoun of a plural: the rational masculine plural takes the she-form or the they-form, the feminine
and the non-rational plurals the she-form or the they-women form.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~218-219 of the transcription.

  VERBATIM from the notebook's Arabic: s1, s4, s5 (the three definitions) and every example.
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s2, s3, s6, s7, s8, s9, s10, s11.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch11.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-muannath-wal-mudhakkar-fil-kafiya"
MA = "al-muannath-wa-alamatuh"
FT = "al-fail-al-muzhar-wa-tanith-amilih"
JT = "al-jumu-wa-tanith-amiliha"
TITLE = {"ar": "الْمُؤَنَّثُ وَالْمُذَكَّرُ", "en": "The feminine and the masculine", "tr": "Müennes ve müzekker"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def ex_v(verb_full, verb_lex, verb_ar, verb_en, verb_tr, subj_full, subj_lex, subj_pos, subj_ar, subj_en, subj_tr, punct=None, wa=False, mid=None):
    v = (atf_wa("وَ" + verb_full, verb_lex, "verb", ["fail", FT], verb_full + " فِعْلٌ مَاضٍ " + verb_ar, "«and» " + verb_en, "«ve» " + verb_tr, verb_full) if wa
         else W(verb_full, verb_lex, "verb", ["fail", FT], "فِعْلٌ مَاضٍ " + verb_ar, verb_en, verb_tr))
    out = [v] + (mid or []) + [W(subj_full, subj_lex, subj_pos, ["fail", FT], subj_ar, subj_en, subj_tr, punct=punct)]
    return out

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The feminine: what carries the mark of femininity, in wording or by estimation.",
 "tr": "Müennes: lafzan ya da takdîren te'nîs alâmeti taşıyandır."},
 "tokens": [
  W("الْمُؤَنَّثُ", "muannath", "noun", ["mubtada-khabar", MA], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the feminine» — the mubtada.", "«müennes» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr", "ism-mawsul", "khabar-al-mubtada-wa-ahkamuh"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ؛ خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«in which» — the ʿāʾid; the ṣila's fronted khabar.", "«kendisinde» — âid; sılanın öne alınmış haberi.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("عَلَامَةُ", "alama", "noun", ["mubtada-khabar", "idafa-definiteness", MA], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the mark of».", "«alâmeti»."),
  W("التَّأْنِيثِ", "tanith", "noun", ["idafa-definiteness", MA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«femininity».", "«te'nîs»."),
  W("لَفْظًا", "lafz", "noun", ["hal"], "حَالٌ مَنْصُوبٌ — كَامْرَأَةٍ وَنَاقَةٍ.", "«in wording» — like امْرَأَة، نَاقَة.", "«lafzan» — imrae, nâka gibi."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("تَقْدِيرًا", "taqdir", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ مَنْصُوبٌ — كَدَارٍ وَنَارٍ.", "«by estimation» — like دَار، نَار.", "«takdîren» — dâr, nâr gibi.", punct="."),
 ]})

# ----------- s2 (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And the masculine is the opposite of it." + R_EN,
 "tr": "Müzekker onun hilâfınadır." + R_TR},
 "tokens": [
  atf_wa("وَالْمُذَكَّرُ", "mudhakkar", "noun", ["mubtada-khabar"], "الْمُذَكَّرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the masculine» — the mubtada.", "«ve müzekker» — mübtedâ.", "الْمُذَكَّرُ"),
  W("بِخِلَافِهِ", "khilaf", "noun", ["huruf-jarr", "mubtada-khabar", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is the opposite of it» — the khabar.", "«onun hilâfınadır» — haber.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun"), pr3msi()]),
 ]})

# ----------- s3 (RESTORED + the notebook's examples)
S.append({"id": "s3", "translation": {
 "en": "And its mark is the tāʾ, the short alif and the long alif — as in فَاطِمَةُ، حُبْلَى and حَمْرَاءُ." + R_EN,
 "tr": "Alâmeti tâ, maksûr elif ve memdûd eliftir — فَاطِمَةُ، حُبْلَى ve حَمْرَاءُ gibi." + R_TR},
 "tokens": [
  atf_wa("وَعَلَامَتُهُ", "alama", "noun", ["mubtada-khabar", "idafa-definiteness", MA], "عَلَامَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its mark» — the mubtada.", "«ve alâmeti» — mübtedâ.", "عَلَامَتُ", extra_segs=[seg("عَلَامَتُ", "alama", "noun"), pr3ms()]),
  W("التَّاءُ", "ta-letter", "noun", ["mubtada-khabar", MA], "خَبَرٌ مَرْفُوعٌ.", "«the tāʾ» — the khabar.", "«tâ» — haber."),
  atf_wa("وَالْأَلِفُ", "alif-letter", "noun", [MA], "الْأَلِفُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the alif».", "«ve elif».", "الْأَلِفُ"),
  W("مَقْصُورَةً", "maqsur", "noun", ["hal", "ism-maqsur-manqus"], "حَالٌ مَنْصُوبٌ.", "«short».", "«maksûr olarak»."),
  atf_wa("وَمَمْدُودَةً", "mamdud", "noun", ["hal", "ism-mamdud"], "مَمْدُودَةً مَعْطُوفٌ مَنْصُوبٌ.", "«and long».", "«ve memdûd olarak».", "مَمْدُودَةً", punct="،"),
  nahwu(),
  W("فَاطِمَةُ", "fatima", "propn", ["idafa-definiteness", MA, "mamnu-min-sarf"], "فِي مَحَلِّ جَرٍّ — عَلَمٌ بِالتَّاءِ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Fāṭima» — the tāʾ.", "«Fâtıma» — tâ."),
  atf_wa("وَحُبْلَى", "hubla", "noun", [MA, "ism-maqsur-manqus", "mamnu-min-sarf"], "حُبْلَى مَعْطُوفٌ — بِالْأَلِفِ الْمَقْصُورَةِ.", "«and pregnant» — the short alif.", "«ve hâmile» — maksûr elif.", "حُبْلَى"),
  atf_wa("وَحَمْرَاءُ", "hamra", "noun", [MA, "ism-mamdud", "mamnu-min-sarf"], "حَمْرَاءُ مَعْطُوفٌ — بِالْأَلِفِ الْمَمْدُودَةِ.", "«and red (f.)» — the long alif.", "«ve kırmızı (müennes)» — memdûd elif.", "حَمْرَاءُ", punct="."),
 ]})

# ----------- s4 (VERBATIM): the real feminine
S.append({"id": "s4", "translation": {
 "en": "The real feminine: that over against which stands a male among living things — as امْرَأَةٌ against رَجُلٌ and نَاقَةٌ against جَمَلٌ.",
 "tr": "Hakîkî müennes: canlılardan karşısında bir erkeği olan — رَجُلٌ karşısında امْرَأَةٌ, جَمَلٌ karşısında نَاقَةٌ gibi."},
 "tokens": [
  W("الْحَقِيقِيُّ", "haqiqi", "noun", ["mubtada-khabar", MA], "مُبْتَدَأٌ مَرْفُوعٌ — أَيِ: الْمُؤَنَّثُ الْحَقِيقِيُّ.", "«the real one» — the mubtada.", "«hakîkî olanı» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«that which».", "«... olan»."),
  W("بِإِزَائِهِ", "izaa", "noun", ["huruf-jarr", "ism-mawsul", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "الْبَاءُ حَرْفُ جَرٍّ، وَإِزَائِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ؛ خَبَرٌ مُقَدَّمٌ.", "«over against which».", "«karşısında».", segments=[seg("بِ", "bi", "prep"), seg("إِزَائِ", "izaa", "noun"), pr3msi()]),
  W("ذَكَرٌ", "dhakar", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a male».", "«bir erkek»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«among».", "«-den»."),
  W("الْحَيَوَانِ", "hayawan", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«living things».", "«canlılar».", punct="،"),
  nahwu(),
  W("امْرَأَةٌ", "imraa", "noun", ["idafa-definiteness", MA], "فِي مَحَلِّ جَرٍّ.", "«a woman».", "«kadın»."),
  W("بِإِزَاءِ", "izaa", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَإِزَاءِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«against».", "«karşısında».", segments=[seg("بِ", "bi", "prep"), seg("إِزَاءِ", "izaa", "noun")]),
  W("رَجُلٍ", "rajul", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a man».", "«adam».", punct="،"),
  atf_wa("وَنَاقَةٌ", "naqa", "noun", [MA], "نَاقَةٌ مَعْطُوفٌ.", "«and a she-camel».", "«ve dişi deve».", "نَاقَةٌ"),
  W("بِإِزَاءِ", "izaa", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَإِزَاءِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«against».", "«karşısında».", segments=[seg("بِ", "bi", "prep"), seg("إِزَاءِ", "izaa", "noun")]),
  W("جَمَلٍ", "jamal-camel", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a he-camel».", "«erkek deve».", punct="."),
 ]})

# ----------- s5 (VERBATIM): the verbal feminine
S.append({"id": "s5", "translation": {
 "en": "The verbal feminine: that over against which no male stands among living things — as ظُلْمَةٌ and عَيْنٌ.",
 "tr": "Lafzî müennes: canlılardan karşısında bir erkeği olmayan — ظُلْمَةٌ ve عَيْنٌ gibi."},
 "tokens": [
  atf_wa("وَاللَّفْظِيُّ", "lafzi", "noun", ["mubtada-khabar", MA], "اللَّفْظِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the verbal one» — the mubtada.", "«ve lafzî olanı» — mübtedâ.", "اللَّفْظِيُّ", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«that which».", "«... olan»."),
  W("لَيْسَ", "laysa", "verb", ["ism-mawsul", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْجُمْلَةُ صِلَةٌ.", "«there is not».", "«... olmayan»."),
  W("بِإِزَائِهِ", "izaa", "noun", ["huruf-jarr", "kana-wa-akhawatuha", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَإِزَائِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ؛ خَبَرُ لَيْسَ مُقَدَّمٌ.", "«over against which» — the fronted khabar of لَيْسَ.", "«karşısında» — leyse'nin öne alınmış haberi.", segments=[seg("بِ", "bi", "prep"), seg("إِزَائِ", "izaa", "noun"), pr3msi()]),
  W("ذَكَرٌ", "dhakar", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a male» — the ism of لَيْسَ.", "«bir erkek» — leyse'nin ismi."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«among».", "«-den»."),
  W("الْحَيَوَانِ", "hayawan", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«living things».", "«canlılar».", punct="،"),
  nahwu(),
  W("ظُلْمَةٌ", "zulma", "noun", ["idafa-definiteness", MA], "فِي مَحَلِّ جَرٍّ — مُؤَنَّثٌ بِالتَّاءِ، لَا ذَكَرَ لَهُ.", "«darkness» — feminine by the tāʾ, with no male.", "«karanlık» — tâ ile müennes, erkeği yok."),
  atf_wa("وَعَيْنٌ", "ayn-eye", "noun", [MA], "عَيْنٌ مَعْطُوفٌ — مُؤَنَّثٌ تَقْدِيرًا.", "«and an eye» — feminine by estimation.", "«ve göz» — takdîren müennes.", "عَيْنٌ", punct="."),
 ]})

# ----------- s6 (RESTORED): the ta of the verb — obligatory
S.append({"id": "s6", "translation": {
 "en": "And the verb predicated of a feminine takes the tāʾ: obligatorily when the real feminine adjoins it, as in «Hind came», and when it is predicated of the pronoun of any feminine, as in «Hind came» and «the sun rose»." + R_EN,
 "tr": "Müennese isnâd edilen fiil tâ alır: hakîkî müennes bitişik olunca vâciben, «Hind geldi» gibi; ve herhangi bir müennesin zamirine isnâd edilince, «Hind geldi» ve «güneş doğdu» gibi." + R_TR},
 "tokens": [
  atf_wa("وَالْفِعْلُ", "fil", "noun", ["mubtada-khabar", FT], "الْفِعْلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the verb» — the mubtada.", "«ve fiil» — mübtedâ.", "الْفِعْلُ"),
  W("الْمُسْنَدُ", "musnad", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«predicated».", "«isnâd edilen»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-e»."),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a feminine».", "«müennese»."),
  W("بِالتَّاءِ", "ta-letter", "noun", ["huruf-jarr", "mubtada-khabar", FT], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّاءِ مَجْرُورٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is with the tāʾ» — the khabar.", "«tâ iledir» — haber.", punct=":", segments=[seg("بِ", "bi", "prep"), seg("التَّاءِ", "ta-letter", "noun")]),
  W("وُجُوبًا", "wujub", "noun", ["hal", "masdar"], "حَالٌ مَنْصُوبٌ — أَيْ: وَاجِبَةً.", "«obligatorily».", "«vâciben»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-de»."),
  W("الْحَقِيقِيِّ", "haqiqi", "noun", ["huruf-jarr", MA], "مَجْرُورٌ.", "«the real one».", "«hakîkîde»."),
  W("الْمُتَّصِلِ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ — لَا فَاصِلَ بَيْنَهُ وَبَيْنَ فِعْلِهِ.", "«adjoining» — nothing between it and its verb.", "«bitişik» — fiiliyle arasında fâsıla yok.", punct="،"),
  nahwu(),
  *ex_v("جَاءَتْ", "jaa", "وَالتَّاءُ لِلتَّأْنِيثِ.", "«came (she)».", "«geldi».", "هِنْدٌ", "hind", "propn", "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ حَقِيقِيٌّ مُتَّصِلٌ.", "«Hind» — a real feminine adjoining.", "«Hind» — bitişik hakîkî müennes.", punct="،"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and for».", "«ve -de».", "فِي"),
  W("الْمُضْمَرِ", "mudmar", "noun", ["huruf-jarr"], "مَجْرُورٌ — ضَمِيرِ الْمُؤَنَّثِ.", "«the pronoun» — of a feminine.", "«zamirde» — müennesin zamiri."),
  W("مُطْلَقًا", "mutlaqan", "noun", ["hal"], "حَالٌ مَنْصُوبٌ — حَقِيقِيًّا كَانَ أَوْ لَفْظِيًّا.", "«of any kind» — real or verbal.", "«mutlak olarak» — hakîkî ya da lafzî.", punct="،"),
  nahwu(),
  W("هِنْدٌ", "hind", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Hind».", "«Hind»."),
  W("جَاءَتْ", "jaa", "verb", ["mubtada-khabar", "fail", FT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ.", "«came» — predicated of her pronoun.", "«geldi» — zamirine isnâd.", punct="،"),
  atf_wa("وَالشَّمْسُ", "shams", "noun", ["mubtada-khabar"], "الشَّمْسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sun».", "«ve güneş».", "الشَّمْسُ"),
  W("طَلَعَتْ", "talaa", "verb", ["mubtada-khabar", "fail", FT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ.", "«rose» — the verbal feminine's pronoun takes it too.", "«doğdu» — lafzî müennesin zamiri de alır.", punct="."),
 ]})

# ----------- s7 (RESTORED): optional across a gap and for the apparent non-real
S.append({"id": "s7", "translation": {
 "en": "And optionally when something separates them, as in «today Hind came» both ways, and for the apparent non-real feminine, as in «the sun rose» both ways." + R_EN,
 "tr": "Araya fâsıla girince câiz olarak, «bugün Hind geldi» her iki şekilde; ve zâhir gayr-i hakîkî müennes için, «güneş doğdu» her iki şekilde." + R_TR},
 "tokens": [
  atf_wa("وَجَوَازًا", "jawaz", "noun", ["hal", "masdar"], "جَوَازًا حَالٌ مَنْصُوبٌ — مَعْطُوفٌ عَلَى وُجُوبًا.", "«and optionally».", "«ve câiz olarak».", "جَوَازًا"),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("الْفَصْلِ", "fasl", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a gap».", "«fâsıla».", punct="،"),
  nahwu(),
  W("جَاءَتِ", "jaa", "verb", ["fail", FT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«came (she)».", "«geldi»."),
  W("الْيَوْمَ", "yawm", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ — الْفَاصِلُ.", "«today» — the gap.", "«bugün» — fâsıla."),
  W("هِنْدٌ", "hind", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Hind».", "«Hind»."),
  atf_wa("وَجَاءَ", "jaa", "verb", ["fail", FT], "جَاءَ فِعْلٌ مَاضٍ بِلَا تَاءٍ.", "«and came (he-form)».", "«ve geldi (müzekker şekli)».", "جَاءَ"),
  W("الْيَوْمَ", "yawm", "noun", ["maful-fih"], "ظَرْفٌ مَنْصُوبٌ.", "«today».", "«bugün»."),
  W("هِنْدٌ", "hind", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ — جَازَ الْوَجْهَانِ لِلْفَصْلِ.", "«Hind» — both allowed because of the gap.", "«Hind» — fâsıla yüzünden iki şekil de câiz.", punct="،"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and for».", "«ve -de».", "فِي"),
  W("ظَاهِرِ", "zahir", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ — الِاسْمِ الظَّاهِرِ لَا الضَّمِيرِ.", "«the apparent» — the noun, not the pronoun.", "«zâhiri» — zamir değil isim."),
  W("غَيْرِ", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«non-».", "«gayr-i»."),
  W("الْحَقِيقِيِّ", "haqiqi", "noun", ["idafa-definiteness", MA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«real».", "«hakîkî».", punct="،"),
  nahwu(),
  *ex_v("طَلَعَتِ", "talaa", "وَالتَّاءُ لِلتَّأْنِيثِ.", "«rose (she)».", "«doğdu».", "الشَّمْسُ", "shams", "noun", "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ لَفْظِيٌّ ظَاهِرٌ.", "«the sun» — an apparent verbal feminine.", "«güneş» — zâhir lafzî müennes."),
  *ex_v("طَلَعَ", "talaa", "بِلَا تَاءٍ.", "«rose (he-form)».", "«doğdu (müzekker şekli)».", "الشَّمْسُ", "shams", "noun", "فَاعِلٌ مَرْفُوعٌ — جَازَ الْوَجْهَانِ.", "«the sun» — both allowed.", "«güneş» — iki şekil de câiz.", punct=".", wa=True),
 ]})

# ----------- s8 (RESTORED): the apparent broken plural
S.append({"id": "s8", "translation": {
 "en": "And the apparent broken plural is like the apparent non-real feminine — as in «the men came» both ways." + R_EN,
 "tr": "Zâhir cem-i mükesser, zâhir gayr-i hakîkî müennes gibidir — «adamlar geldi» her iki şekilde." + R_TR},
 "tokens": [
  atf_wa("وَظَاهِرُ", "zahir", "noun", ["mubtada-khabar", "idafa-definiteness", JT], "ظَاهِرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the apparent» — the mubtada.", "«ve zâhiri» — mübtedâ.", "ظَاهِرُ"),
  W("جَمْعِ", "jam", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cem-i»."),
  W("التَّكْسِيرِ", "taksir", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«breaking» — the broken plural.", "«mükesser» — kırık çoğul."),
  W("كَظَاهِرِ", "zahir", "noun", ["huruf-jarr", "mubtada-khabar", "idafa-definiteness"], "الْكَافُ حَرْفُ جَرٍّ، وَظَاهِرِ مَجْرُورٌ، وَهُوَ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is like the apparent» — the khabar.", "«zâhiri gibidir» — haber.", segments=[seg("كَ", "ka", "prep"), seg("ظَاهِرِ", "zahir", "noun")]),
  W("غَيْرِ", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَهُوَ مُضَافٌ.", "«non-».", "«gayr-i»."),
  W("الْحَقِيقِيِّ", "haqiqi", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«real».", "«hakîkî».", punct="،"),
  nahwu(),
  *ex_v("جَاءَ", "jaa", "بِلَا تَاءٍ.", "«came».", "«geldi».", "الرِّجَالُ", "rajul", "noun", "فَاعِلٌ مَرْفُوعٌ — جَمْعُ تَكْسِيرٍ ظَاهِرٌ.", "«the men» — an apparent broken plural.", "«adamlar» — zâhir cem-i mükesser."),
  *ex_v("جَاءَتِ", "jaa", "وَالتَّاءُ لِلتَّأْنِيثِ.", "«came (she-form)».", "«geldi (müennes şekli)».", "الرِّجَالُ", "rajul", "noun", "فَاعِلٌ مَرْفُوعٌ — جَازَ الْوَجْهَانِ.", "«the men» — both allowed.", "«adamlar» — iki şekil de câiz.", punct=".", wa=True),
 ]})

# ----------- s9 (RESTORED): the pronoun of the rational masculine plural
S.append({"id": "s9", "translation": {
 "en": "And its pronoun takes the feminine singular or the masculine plural — as in «the men, they (she-form) came» and «the men, they came»." + R_EN,
 "tr": "Zamiri ise müfred müennes ya da cemi müzekker olur — «adamlar geldi (müennes şekli)» ve «adamlar geldiler» gibi." + R_TR},
 "tokens": [
  atf_wa("وَمُضْمَرُهُ", "mudmar", "noun", ["mubtada-khabar", "idafa-definiteness", JT], "مُضْمَرُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — ضَمِيرُ جَمْعِ الْمُذَكَّرِ الْعَاقِلِ.", "«and its pronoun» — the mubtada.", "«ve zamiri» — mübtedâ.", "مُضْمَرُ", extra_segs=[seg("مُضْمَرُ", "mudmar", "noun"), pr3ms()]),
  W("كَالْمُفْرَدَةِ", "mufrad", "noun", ["huruf-jarr", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَالْمُفْرَدَةِ مَجْرُورٌ؛ خَبَرٌ — أَيْ: كَضَمِيرِ الْمُفْرَدَةِ الْمُؤَنَّثَةِ.", "«is like the feminine singular's» — the khabar.", "«müfred müennesinki gibidir» — haber.", segments=[seg("كَ", "ka", "prep"), seg("الْمُفْرَدَةِ", "mufrad", "noun")]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("كَجَمْعِ", "jam", "noun", ["huruf-jarr", "atf-nasaq", "idafa-definiteness"], "الْكَافُ حَرْفُ جَرٍّ، وَجَمْعِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«like the plural of».", "«cemi ... gibi».", segments=[seg("كَ", "ka", "prep"), seg("جَمْعِ", "jam", "noun")]),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine».", "«müzekker».", punct="،"),
  nahwu(),
  W("الرِّجَالُ", "rajul", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the men».", "«adamlar»."),
  W("جَاءَتْ", "jaa", "verb", ["mubtada-khabar", "fail", JT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ، وَالْجُمْلَةُ خَبَرٌ.", "«came (she-form)» — the hidden هِيَ.", "«geldi» — gizli hiye.", punct="،"),
  atf_wa("وَالرِّجَالُ", "rajul", "noun", ["mubtada-khabar"], "الرِّجَالُ مُبْتَدَأٌ.", "«and the men».", "«ve adamlar».", "الرِّجَالُ"),
  W("جَاؤُوا", "jaa", "verb", ["mubtada-khabar", "fail", JT], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَالْجُمْلَةُ خَبَرٌ.", "«came (they)» — the wāw.", "«geldiler» — vâv.", punct="."),
 ]})

# ----------- s10 (RESTORED): the feminine and the non-rational plurals
S.append({"id": "s10", "translation": {
 "en": "And the pronoun of the feminine plural and of the non-rational plural takes the feminine singular or the feminine plural — as in «the women helped» (she-form) and «the women helped» (they-women form), «the springs appeared» both ways." + R_EN,
 "tr": "Cemi müennesin ve gayr-i âkil ceminin zamiri müfred müennes ya da cemi müennes olur — «kadınlar yardım etti» (müennes şekli), «kadınlar yardım ettiler» (cemi müennes şekli), «pınarlar göründü» her iki şekilde." + R_TR},
 "tokens": [
  atf_wa("وَمُضْمَرُ", "mudmar", "noun", ["mubtada-khabar", "idafa-definiteness", JT], "مُضْمَرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the pronoun of».", "«ve zamiri».", "مُضْمَرُ"),
  W("جَمْعِ", "jam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cemi»."),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müennesin»."),
  atf_wa("وَغَيْرِ", "ghayr", "noun", ["idafa-definiteness"], "غَيْرِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the non-».", "«ve gayr-i».", "غَيْرِ"),
  W("الْعَاقِلِ", "aqil", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rational».", "«âkil»."),
  W("كَالْمُفْرَدَةِ", "mufrad", "noun", ["huruf-jarr", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَالْمُفْرَدَةِ مَجْرُورٌ؛ خَبَرٌ.", "«is like the feminine singular's».", "«müfred müennesinki gibidir»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("كَجَمْعِ", "jam", "noun", ["huruf-jarr", "atf-nasaq", "idafa-definiteness"], "الْكَافُ حَرْفُ جَرٍّ، وَجَمْعِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«like the plural of».", "«cemi ... gibi».", segments=[seg("كَ", "ka", "prep"), seg("جَمْعِ", "jam", "noun")]),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müennes».", punct="،"),
  nahwu(),
  W("النِّسَاءُ", "nisa", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the women».", "«kadınlar»."),
  W("نَصَرَتْ", "nasara", "verb", ["mubtada-khabar", "fail", JT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "«helped (she-form)».", "«yardım etti».", punct="،"),
  atf_wa("وَالنِّسَاءُ", "nisa", "noun", ["mubtada-khabar"], "النِّسَاءُ مُبْتَدَأٌ.", "«and the women».", "«ve kadınlar».", "النِّسَاءُ"),
  W("نَصَرْنَ", "nasara", "verb", ["mubtada-khabar", "fail", JT], "فِعْلٌ مَاضٍ، وَالنُّونُ فَاعِلٌ — نُونُ النِّسْوَةِ.", "«helped (they-women)» — the nūn of the women.", "«yardım ettiler» — nisve nûnu.", punct="،"),
  atf_wa("وَالْعُيُونُ", "ayn-spring", "noun", ["mubtada-khabar", "jam-taksir"], "الْعُيُونُ مُبْتَدَأٌ — جَمْعُ غَيْرِ الْعَاقِلِ.", "«and the springs» — a non-rational plural.", "«ve pınarlar» — gayr-i âkil cemi.", "الْعُيُونُ"),
  W("ظَهَرَتْ", "zahara", "verb", ["mubtada-khabar", "fail", JT], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«appeared (she-form)».", "«göründü».", punct="،"),
  atf_wa("وَالْعُيُونُ", "ayn-spring", "noun", ["mubtada-khabar"], "الْعُيُونُ مُبْتَدَأٌ.", "«and the springs».", "«ve pınarlar».", "الْعُيُونُ"),
  W("ظَهَرْنَ", "zahara", "verb", ["mubtada-khabar", "fail", JT], "فِعْلٌ مَاضٍ، وَالنُّونُ فَاعِلٌ.", "«appeared (they-women form)».", "«göründüler».", punct="."),
 ]})

def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "jamal-camel": need("jamal-camel", "جَمَل", "ج م ل", "noun", "a he-camel", "erkek deve", 2, plural="جِمَال"),
 "wujub": need("wujub", "وُجُوب", "و ج ب", "noun", "obligation (masdar of وَجَبَ) — وُجُوبًا: of necessity", "vücûb (vecebe'nin masdarı) — vücûben: zorunlu olarak", 4),
 "jawaz": need("jawaz", "جَوَاز", "ج و ز", "noun", "permissibility (masdar of جَازَ) — جَوَازًا: optionally", "cevâz (câze'nin masdarı) — cevâzen: câiz olarak", 4),
 "taksir": need("taksir", "تَكْسِير", "ك س ر", "noun", "breaking — جَمْعُ التَّكْسِيرِ: the broken plural (masdar of Form II كَسَّرَ)", "kırma — cem-i teksîr: kırık çoğul (kessera'nın masdarı)", 3),
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
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch11 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْمُؤَنَّثُ وَالْمُذَكَّرُ فِي الْكَافِيَةِ", "en": "The feminine and the masculine in the Kafiya: the marks, real against verbal, and when the verb's tāʾ is obligatory, optional, or replaced by a plural pronoun", "tr": "Kâfiye'de müennes ve müzekker: alâmetler, hakîkî ile lafzî, fiilin tâ'sının ne zaman vâcib, ne zaman câiz, ne zaman cemi zamiriyle değişir olduğu"},
 "level": 3, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المؤنث: ما فيه علامة التأنيث لفظا أو تقديرا؛ الحقيقي ما بإزائه ذكر من الحيوان؛ تاء التأنيث في الفعل واجبة وجائزة؛ ضمير الجمع", "ضياء صونغور اوغلى — دفتر الكافية: التعريفات بلفظها، جاءت اليوم هند وجاء اليوم هند، طلعت الشمس وطلع، جاء الرجال وجاءت، النساء نصرت ونصرن، العيون ظهرت وظهرن"],
 "question": {
  "en": ["What is a FEMININE noun? One carrying the mark of femininity in its wording (امْرَأَة, with the tāʾ) or by estimation (دَار, with none written). The masculine is simply the opposite. The marks are three: the tāʾ (فَاطِمَة), the short alif (حُبْلَى), the long alif (حَمْرَاء).",
         "Real or verbal? REAL when a male stands over against it among living things (امْرَأَة against رَجُل, نَاقَة against جَمَل); VERBAL when none does (ظُلْمَة, عَيْن).",
         "When MUST the verb take the tāʾ? When a real feminine follows it directly (جَاءَتْ هِنْدٌ), and whenever the verb is predicated of a feminine's PRONOUN, real or not (هِنْدٌ جَاءَتْ، الشَّمْسُ طَلَعَتْ).",
         "When MAY it? When a word separates verb and doer (جَاءَتِ الْيَوْمَ هِنْدٌ / جَاءَ الْيَوْمَ هِنْدٌ), and when the doer is an apparent non-real feminine (طَلَعَتِ الشَّمْسُ / طَلَعَ الشَّمْسُ). An apparent broken plural is treated the same (جَاءَ الرِّجَالُ / جَاءَتِ الرِّجَالُ).",
         "And a plural's PRONOUN? For rational men: the she-form or the they-form (الرِّجَالُ جَاءَتْ / جَاؤُوا). For women and for non-rational things: the she-form or the they-women form (النِّسَاءُ نَصَرَتْ / نَصَرْنَ، الْعُيُونُ ظَهَرَتْ / ظَهَرْنَ).",
         "What does the engine read? The DabtEngine's doer rules read the verb's tāʾ as the receipt of a feminine doer and accept the he-form before a separated or non-real feminine and before a broken plural; the agreement checks in the games are built from this table."],
  "tr": ["MÜENNES isim nedir? Te'nîs alâmetini lafzında (امْرَأَة, tâ ile) ya da takdîren (دَار, yazılı alâmet yok) taşıyan. Müzekker yalnızca onun tersidir. Alâmet üçtür: tâ (فَاطِمَة), maksûr elif (حُبْلَى), memdûd elif (حَمْرَاء).",
         "Hakîkî mi lafzî mi? Canlılardan karşısında bir erkek varsa HAKÎKÎ (رَجُل karşısında امْرَأَة, جَمَل karşısında نَاقَة); yoksa LAFZÎ (ظُلْمَة, عَيْن).",
         "Fiil tâ'yı ne zaman ALMALI? Hakîkî müennes fiilin hemen ardından gelince (جَاءَتْ هِنْدٌ) ve fiil, hakîkî olsun olmasın, bir müennesin ZAMİRİNE isnâd edilince (هِنْدٌ جَاءَتْ، الشَّمْسُ طَلَعَتْ).",
         "Ne zaman ALABİLİR? Fiil ile fâil arasına bir kelime girince (جَاءَتِ الْيَوْمَ هِنْدٌ / جَاءَ الْيَوْمَ هِنْدٌ) ve fâil zâhir gayr-i hakîkî müennes olunca (طَلَعَتِ الشَّمْسُ / طَلَعَ الشَّمْسُ). Zâhir cem-i mükesser de aynı muameleyi görür (جَاءَ الرِّجَالُ / جَاءَتِ الرِّجَالُ).",
         "Ya ceminin ZAMİRİ? Âkil erkekler için: müennes şekli ya da cemi şekli (الرِّجَالُ جَاءَتْ / جَاؤُوا). Kadınlar ve gayr-i âkil şeyler için: müennes şekli ya da nisve şekli (النِّسَاءُ نَصَرَتْ / نَصَرْنَ، الْعُيُونُ ظَهَرَتْ / ظَهَرْنَ).",
         "Motor neyi okur? DabtEngine'in fâil kuralları fiilin tâ'sını müennes fâilin makbuzu olarak okur; ayrılmış ya da gayr-i hakîkî müennesten ve cem-i mükesserden önce müzekker şekli kabul eder; oyunlardaki uyum denetimleri bu tablodan kurulur."]},
 "plain": {
  "en": "A feminine noun shows its gender by a tāʾ or an alif, or shows nothing and is still feminine. The verb before a feminine doer takes the tāʾ: always for a woman or a she-animal standing right after it, always for a pronoun, but optionally when a word comes between or when the doer is a thing or a broken plural.",
  "tr": "Müennes isim cinsini bir tâ ya da elifle gösterir, ya da hiçbir şey göstermez ve yine müennestir. Müennes fâilden önceki fiil tâ alır: hemen ardından gelen bir kadın ya da dişi hayvan için her zaman, zamir için her zaman; araya kelime girince ya da fâil bir şey ya da kırık çoğul olunca ise isteğe bağlı."},
 "explanation": {
  "en": "The chapter has two halves. The first defines gender by its marks — a feminine noun either shows one (the tāʾ, the short alif, the long alif) or is counted feminine without showing it — and then cuts the feminine in two by a test outside grammar: does a male stand over against it among living things? If yes it is real (a woman, a she-camel); if not, verbal (darkness, an eye). The second half is the rule the division exists for: the verb's tāʾ of femininity. It is obligatory in the two cases where nothing weakens the bond — a real feminine standing directly after its verb, and any feminine's pronoun, because a pronoun has no gender of its own and takes the verb's. It becomes optional where the bond loosens: a word between verb and doer (today), a doer that is feminine only by its wording (the sun), and — the notebook's extension of the same thought — a broken plural standing apparent, which the Arabs treat like a non-real feminine. Even the plural's pronoun keeps a choice: men's plural takes the she-form or the they-form, women's and things' plurals the she-form or the nūn form. The whole table is what the DabtEngine's doer rules encode when they read a tāʾ on the verb as a receipt of what follows and still accept the bare verb before the sun or the men.",
  "tr": "Bâb iki yarımdır. İlki cinsi alâmetleriyle tarif eder — müennes isim ya bir alâmet gösterir (tâ, maksûr elif, memdûd elif) ya da göstermeden müennes sayılır — sonra müennesi nahvin dışından bir ölçüyle ikiye böler: canlılardan karşısında bir erkek var mı? Varsa hakîkîdir (kadın, dişi deve); yoksa lafzî (karanlık, göz). İkinci yarı bu bölünmenin kendisi için var olduğu kuraldır: fiilin te'nîs tâ'sı. Bağı zayıflatan hiçbir şeyin olmadığı iki durumda vâcibdir — fiilinin hemen ardından gelen hakîkî müennes ve herhangi bir müennesin zamiri, çünkü zamirin kendi cinsi yoktur, fiilinkini alır. Bağ gevşeyince câiz olur: fiil ile fâil arasına giren kelime (bugün), yalnız lafzıyla müennes olan fâil (güneş) ve — defterin aynı düşünceyi uzatışı — zâhir duran cem-i mükesser; Araplar onu gayr-i hakîkî müennes gibi görür. Ceminin zamiri bile bir seçim taşır: erkeklerin cemi müennes şeklini ya da cemi şeklini, kadınların ve şeylerin cemileri müennes şeklini ya da nûn şeklini alır. Bütün tablo, DabtEngine'in fâil kurallarının fiildeki tâ'yı ardından gelenin makbuzu olarak okurken güneşten ya da adamlardan önce yalın fiili de kabul etmesinde kodludur."},
 "examples": [
  {"ar": "الْمُؤَنَّثُ: مَا فِيهِ عَلَامَةُ التَّأْنِيثِ لَفْظًا أَوْ تَقْدِيرًا", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "فَاطِمَةُ، حُبْلَى، حَمْرَاءُ", "en": "The three marks.", "tr": "Üç alâmet.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "امْرَأَةٌ بِإِزَاءِ رَجُلٍ — ظُلْمَةٌ وَعَيْنٌ", "en": "Real against verbal.", "tr": "Hakîkî ile lafzî.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "جَاءَتْ هِنْدٌ — هِنْدٌ جَاءَتْ — الشَّمْسُ طَلَعَتْ", "en": "The obligatory tāʾ.", "tr": "Vâcib tâ.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "جَاءَتِ الْيَوْمَ هِنْدٌ / جَاءَ الْيَوْمَ هِنْدٌ — طَلَعَتِ الشَّمْسُ / طَلَعَ الشَّمْسُ", "en": "The optional tāʾ.", "tr": "Câiz tâ.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "الرِّجَالُ جَاءَتْ / جَاؤُوا — النِّسَاءُ نَصَرَتْ / نَصَرْنَ", "en": "The plural's pronoun.", "tr": "Ceminin zamiri.", "sourceStory": "al-kafiya", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«جَاءَ هِنْدٌ — fâil fiilden sonra, tâ gerekmez»",
   "right": "«جَاءَتْ هِنْدٌ — bitişik hakîkî müennes fâil için tâ vâcibdir»",
   "why": {"en": "The he-form is allowed only across a gap or before a non-real feminine; Hind right after her verb demands the tāʾ.", "tr": "Müzekker şekli ancak fâsıla ile ya da gayr-i hakîkî müennesten önce câizdir; fiilinin hemen ardındaki Hind tâ'yı ister."}},
  {"wrong": "«الشَّمْسُ طَلَعَ — güneş lafzî müennestir, tâ câizdir»",
   "right": "«الشَّمْسُ طَلَعَتْ — fiil zamire isnâd edilince tâ her müennes için vâcibdir; cevâz yalnız zâhir için: طَلَعَ الشَّمْسُ»",
   "why": {"en": "The option belongs to the apparent noun after the verb; a pronoun always carries its antecedent's gender into the verb.", "tr": "Seçim fiilden sonraki zâhir isme âittir; zamir, mercîinin cinsini her zaman fiile taşır."}},
  {"wrong": "«الرِّجَالُ جَاءَتْ yanlıştır, adamlar müzekkerdir»",
   "right": "«الرِّجَالُ جَاءَتْ ve الرِّجَالُ جَاؤُوا ikisi de doğrudur: cem-i mükesserin zamiri müfred müennes ya da cemi müzekker olur»",
   "why": {"en": "A broken plural is a collective the Arabs may construe as a single feminine thing — the she-form is the sign of that construal.", "tr": "Cem-i mükesser, Arapların tek bir müennes şey gibi kurabildiği bir topluluktur — müennes şekli bu kuruluşun alâmetidir."}},
  {"wrong": "«الْعُيُونُ ظَهَرُوا — çoğul fâil, vâv ile»",
   "right": "«الْعُيُونُ ظَهَرَتْ ya da ظَهَرْنَ — gayr-i âkil ceminin zamiri müennes şekli ya da nûn şeklidir, vâv değil»",
   "why": {"en": "The wāw of the plural is for rational males only; things and women take the tāʾ or the nūn.", "tr": "Ceminin vâvı yalnız âkil erkekler içindir; şeyler ve kadınlar tâ ya da nûn alır."}}],
 "relatedNotes": [MA, FT, JT, "jam-taksir", "jam-muannath-salim", "ism-mamdud", "ism-maqsur-manqus", "mamnu-min-sarf"]}

ADD_EN = (" Chapter 11 (notebook lines ~218-219): the feminine, the real and the verbal feminine defined in the notebook's own Arabic (s1, s4, s5) with every example "
          "it gives; the masculine, the marks, the obligatory and the optional tāʾ of the verb, the apparent broken plural and the plural's pronoun restored from the "
          "received matn and marked (s2, s3, s6-s10).")
ADD_TR = (" On birinci bâb (defter satırları ~218-219): müennes, hakîkî ve lafzî müennes defterin kendi Arapçasıyla tarif edilir (s1, s4, s5), verdiği her örnekle; "
          "müzekker, alâmetler, fiilin vâcib ve câiz tâ'sı, zâhir cem-i mükesser ve ceminin zamiri alınan metinden geri yazılmış ve işaretlenmiştir (s2, s3, s6-s10).")
write_out(11, S, TITLE, ADD_EN, ADD_TR, "218-219", GLOSS_ADD, notes=(NOTE,),
          related=((MA, [K]), (FT, [K]), (JT, [K])))
report(11, S, GLOSS_ADD, (NOTE,))
