# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 5: THE DEMONSTRATIVES AND THE RELATIVES. The demonstrative defined, its forms by gender and number, the
jumhur's ruling that it is mabni, the ha of alerting before it and the kaf of address after it (the five letters, the twenty-five
forms), the relative defined by its sila and 'a'id, its forms, and مَنْ for the rational against مَا for the rest with the two
ayas the notebook cites (al-Rahman 55:26, al-Nahl 16:96).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~173-175 of the transcription.

  VERBATIM from the notebook's Arabic: s1 (the definition), the form lists of s2-s4, s6-s7, s10-s12 and both ayas.
  RESTORED (the notebook carries the ruling only in Turkish; the received matn of the Kafiya is written and marked): s2, s3, s4, s6, s7, s9, s10, s11, s12.
  COMMENTARY (the notebook's own question and answer, not the matn): s5, s8, s13 — marked C_EN/C_TR.
  The notebook writes the dual relatives اَلَّذَانِ / اَلَّتَانِ; the standard اللَّذَانِ / اللَّتَانِ (al-Nisa 4:16) is set and the notebook's spelling noted here.
  DRY_PKG=<copy> DRY_GR=<copy> python3 tools/authoring/author_kafiya_ch5.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "asma-al-ishara-wal-mawsulat"
K3 = "al-mabni-wal-mudmar"
ISH = "asma-al-ishara"
MWS = "ism-mawsul"
TITLE = {"ar": "أَسْمَاءُ الْإِشَارَةِ وَالْمَوْصُولَاتُ", "en": "The demonstratives and the relatives", "tr": "İşaret isimleri ve mevsûller"}
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
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def fi_raf(punct=None):
    return [W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."), W("الرَّفْعِ", "raf", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«rafʿ».", "«ref'».", punct=punct)]
def fi_nasb_jarr(punct=None):
    return [W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."), W("النَّصْبِ", "nasb", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«naṣb».", "«nasb»."),
            atf_wa("وَالْجَرِّ", "jarr", "noun", ["huruf-jarr"], "الْجَرِّ مَعْطُوفٌ مَجْرُورٌ.", "«and jarr».", "«ve cer».", "الْجَرِّ", punct=punct)]
def mabni_why(first_ar, first_en, first_tr):
    return [
      W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
      W("اخْتِلَافَ", "ikhtilaf", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar", "form-viii-verbs"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the changing of» — the ism of أَنَّ.", "«değişmesi» — enne'nin ismi."),
      W("آخِرِهَا", "akhir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ending».", "«sonunun».", segments=[seg("آخِرِ", "akhir", "noun"), pr3fs()]),
      W("بِالْوَضْعِ", "wad-put", "noun", ["huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْوَضْعِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«is by coinage» — the khabar of أَنَّ: the forms were coined so, not governed into it.", "«vaz' iledir» — enne'nin haberi: şekiller öyle konulmuştur, âmil değiştirmemiştir.", segments=[seg("بِ", "bi", "prep"), seg("الْوَضْعِ", "wad-put", "noun")]),
      W("لَا", "la", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«... değil»."),
      W("بِالْعَامِلِ", "amil", "noun", ["huruf-jarr", "atf-nasaq"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْعَامِلِ مَجْرُورٌ — مَعْطُوفٌ عَلَى بِالْوَضْعِ.", "«by a governor» — the rejected alternative.", "«âmil ile» — reddedilen seçenek.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الْعَامِلِ", "amil", "noun")])]

# ----------- s1 (VERBATIM): the definition
S.append({"id": "s1", "translation": {
 "en": "The demonstrative noun: what is coined for a thing pointed at.",
 "tr": "İşaret ismi: kendisine işaret edilen için konulmuş olandır."},
 "tokens": [
  W("اسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the noun of» — the mubtada.", "«ismi» — mübtedâ."),
  W("الْإِشَارَةِ", "ishara-nahw", "noun", ["idafa-definiteness", ISH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«pointing» — the demonstrative.", "«işaret» — işaret ismi.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the relative, the khabar.", "«... olan» — mevsûl, haber."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail", "al-mustatir-jawazan"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«is coined» — the passive; its concealed deputy is the ʿāʾid.", "«konulmuş» — meçhul; gizli nâibi âiddir."),
  li_("لِمُشَارٍ", "mushar", "noun", ["ism-maful", "ism-maqsur-manqus"], "مُشَارٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ، اسْمُ مَفْعُولٍ.", "«for a thing pointed» — a manqūṣ ism mafʿūl.", "«işaret edilen için» — mankûs ism-i mef'ûl.", "مُشَارٍ"),
  W("إِلَيْهِ", "ila", "prep", ["huruf-jarr", "ism-maful"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ فَاعِلِ اسْمِ الْمَفْعُولِ.", "«at» — the jarr phrase stands as the participle's deputy doer.", "«kendisine» — câr-mecrûr, ism-i mef'ûlün nâibi.", punct=".", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
 ]})

# ----------- s2 (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And it is: ذَا for the masculine singular; ذَانِ in rafʿ and ذَيْنِ in naṣb and jarr for its dual." + R_EN,
 "tr": "Bunlar: müfred müzekker için ذَا; tesniyesi için ref'de ذَانِ, nasb ve cerde ذَيْنِ." + R_TR},
 "tokens": [
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", "هُوَ", punct=":"),
  cited("ذَا", "dha", "pron", ["mubtada-khabar", ISH], "فِي مَحَلِّ رَفْعٍ خَبَرٌ؛ وَهُوَ اسْمُ إِشَارَةٍ مَبْنِيٌّ.", "«ذَا» — the khabar; the demonstrative itself.", "«zâ» — haber; işaret isminin kendisi."),
  li_("لِلْمُفْرَدِ", "mufrad", "noun", ["naat-sifa"], "الْمُفْرَدِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for the singular».", "«müfred için».", "الْمُفْرَدِ", segs=[seg("لِ", "li", "prep"), seg("الْمُفْرَدِ", "mufrad", "noun")]),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["naat-sifa"], "صِفَةٌ لِلْمُفْرَدِ مَجْرُورَةٌ.", "«masculine» — its naʿt.", "«müzekker» — sıfatı.", punct="؛"),
  cited_wa("وَذَانِ", "dhani", "pron", ["mubtada-khabar", ISH, "al-muthanna"], "ذَانِ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ — صِيغَةُ الْمُثَنَّى الْمُذَكَّرِ فِي الرَّفْعِ.", "«and ذَانِ» — the masculine dual's rafʿ form.", "«ve zâni» — müzekker tesniyenin ref' şekli.", "ذَانِ"),
  *fi_raf(),
  cited_wa("وَذَيْنِ", "dhani", "pron", ["mubtada-khabar", ISH, "al-muthanna"], "ذَيْنِ مَعْطُوفٌ — صِيغَةُ النَّصْبِ وَالْجَرِّ.", "«and ذَيْنِ» — its naṣb and jarr form.", "«ve zeyni» — nasb ve cer şekli.", "ذَيْنِ"),
  *fi_nasb_jarr(),
  li_("لِلْمُثَنَّى", "muthanna", "noun", ["ism-maqsur-manqus"], "الْمُثَنَّى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«for the dual» — a maqṣūr.", "«tesniye için» — maksûr.", "الْمُثَنَّى", punct=".", segs=[seg("لِ", "li", "prep"), seg("الْمُثَنَّى", "muthanna", "noun")]),
 ]})

# ----------- s3 (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And تَا، تِي، ذِي and ذِهْ for the feminine singular; تَانِ in rafʿ and تَيْنِ in naṣb and jarr for its dual." + R_EN,
 "tr": "Müfred müennes için تَا، تِي، ذِي ve ذِهْ; tesniyesi için ref'de تَانِ, nasb ve cerde تَيْنِ." + R_TR},
 "tokens": [
  cited_wa("وَتَا", "ta-ishara", "pron", ["mubtada-khabar", ISH], "تَا مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and تَا».", "«ve tâ».", "تَا"),
  cited_wa("وَتِي", "ti-ishara", "pron", [ISH], "تِي مَعْطُوفٌ.", "«and تِي».", "«ve tî».", "تِي"),
  cited_wa("وَذِي", "dhi-ishara", "pron", [ISH], "ذِي مَعْطُوفٌ.", "«and ذِي».", "«ve zî».", "ذِي"),
  cited_wa("وَذِهْ", "dhih-ishara", "pron", [ISH], "ذِهْ مَعْطُوفٌ — بِهَاءِ السَّكْتِ.", "«and ذِهْ» — with the hāʾ of pause.", "«ve zih» — sekte hâ'sıyla.", "ذِهْ"),
  li_("لِلْمُؤَنَّثَةِ", "muannath", "noun", [], "الْمُؤَنَّثَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for the feminine».", "«müennes için».", "الْمُؤَنَّثَةِ", punct="؛", segs=[seg("لِ", "li", "prep"), seg("الْمُؤَنَّثَةِ", "muannath", "noun")]),
  cited_wa("وَتَانِ", "tani-ishara", "pron", [ISH, "al-muthanna"], "تَانِ مَعْطُوفٌ — صِيغَةُ الْمُثَنَّى الْمُؤَنَّثِ فِي الرَّفْعِ.", "«and تَانِ» — the feminine dual in rafʿ.", "«ve tâni» — müennes tesniye, ref'de.", "تَانِ"),
  *fi_raf(),
  cited_wa("وَتَيْنِ", "tani-ishara", "pron", [ISH, "al-muthanna"], "تَيْنِ مَعْطُوفٌ — صِيغَةُ النَّصْبِ وَالْجَرِّ.", "«and تَيْنِ» — in naṣb and jarr.", "«ve teyni» — nasb ve cerde.", "تَيْنِ"),
  *fi_nasb_jarr(),
  li_("لِمُثَنَّاهَا", "muthanna", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُثَنَّا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهَا مُضَافٌ إِلَيْهِ.", "«for its dual».", "«tesniyesi için».", "مُثَنَّا", punct=".", segs=[seg("لِ", "li", "prep"), seg("مُثَنَّا", "muthanna", "noun"), pr3fs()]),
 ]})

# ----------- s4 (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "And أُولَى shortened and أُولَاءِ lengthened for the plural, masculine or feminine." + R_EN,
 "tr": "Cemi için, müzekker olsun müennes olsun, kasr ile أُولَى ve medd ile أُولَاءِ." + R_TR},
 "tokens": [
  cited_wa("وَأُولَى", "ula-qasr", "pron", [ISH, "mubtada-khabar"], "أُولَى مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and أُولَى».", "«ve ulâ».", "أُولَى"),
  W("مَقْصُورًا", "maqsur", "noun", ["hal", "ism-maful"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«shortened» — the ḥāl.", "«maksûr olarak» — hâl."),
  cited_wa("وَأُولَاءِ", "ula-ishara", "pron", [ISH], "أُولَاءِ مَعْطُوفٌ — مَبْنِيٌّ عَلَى الْكَسْرِ.", "«and أُولَاءِ» — built on the kasr.", "«ve ulâi» — kesr üzere mebnî.", "أُولَاءِ"),
  W("مَمْدُودًا", "mamdud", "noun", ["hal", "ism-maful"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«lengthened» — the ḥāl.", "«memdûd olarak» — hâl."),
  li_("لِلْجَمْعِ", "jam", "noun", [], "الْجَمْعِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for the plural».", "«cemi için».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("الْجَمْعِ", "jam", "noun")]),
  W("مُذَكَّرًا", "mudhakkar", "noun", ["hal"], "حَالٌ مِنَ الْجَمْعِ مَنْصُوبٌ.", "«masculine» — the ḥāl of the plural.", "«müzekker olsun» — cemiden hâl."),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ، وَخَبَرُهُ مَحْذُوفٌ — أَيْ: كَانَ مُذَكَّرًا.", "«be it» — kāna with its khabar understood from the ḥāl.", "«olsun» — kâne; haberi hâlden anlaşılır."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُؤَنَّثًا", "muannath", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ عَلَى مُذَكَّرًا مَنْصُوبٌ.", "«feminine».", "«müennes».", punct="."),
 ]})

# ----------- s5 (COMMENTARY)
S.append({"id": "s5", "translation": {
 "en": "And they are mabnī for the majority, because the changing of their ending is by coinage, not by a governor." + C_EN,
 "tr": "Cumhûra göre bunlar mebnîdir; çünkü sonlarının değişmesi âmil sebebiyle değil, vaz' iledir." + C_TR},
 "tokens": [
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and they» — the mubtada.", "«ve bunlar» — mübtedâ.", "هِيَ"),
  W("مَبْنِيَّةٌ", "mabni", "noun", ["mubtada-khabar", "ism-maful", K3], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«mabnī» — the khabar.", "«mebnîdir» — haber."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْجُمْهُورِ", "jumhur", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the majority» — against those who call ذَانِ muʿrab.", "«cumhûr» — zâni'yi mu'reb sayanlara karşı.", punct="،"),
  *mabni_why("", "", ""),
 ]})

# ----------- s6 (RESTORED): the ha of alerting
S.append({"id": "s6", "translation": {
 "en": "And the letter of alerting enters it, as in هٰذَا، هٰذَانِ، هَاتَا، هَاتَانِ and هٰؤُلَاءِ." + R_EN,
 "tr": "Başına tenbih harfi gelir: هٰذَا، هٰذَانِ، هَاتَا، هَاتَانِ ve هٰؤُلَاءِ gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَدْخُلُهَا", "dakhala", "verb", ["fail", "maful-bihi"], "يَدْخُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَهَا مَفْعُولٌ بِهِ.", "«and enters it».", "«ve ona girer».", "يَدْخُلُ", extra_segs=[seg("يَدْخُلُ", "dakhala", "verb"), pr3fs()]),
  W("حَرْفُ", "harf", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letter of» — the doer.", "«harfi» — fâil."),
  W("التَّنْبِيهِ", "tanbih", "noun", ["idafa-definiteness", "huruf-tanbih"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — هَا.", "«alerting» — the هَا.", "«tenbih» — hâ.", punct="،"),
  nahwu(),
  cited("هٰذَا", "hadha", "pron", ["idafa-definiteness", ISH, "huruf-tanbih"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — هَا لِلتَّنْبِيهِ وَذَا اسْمُ إِشَارَةٍ.", "«this» — هَا + ذَا.", "«bu» — hâ + zâ.", segments=[seg("هٰ", "ha-tanbih", "part"), seg("ذَا", "dha", "pron")]),
  cited_wa("وَهٰذَانِ", "dhani", "pron", [ISH, "al-muthanna", "huruf-tanbih"], "هٰذَانِ مَعْطُوفٌ.", "«and these two».", "«ve bu ikisi».", "ذَانِ", ),
  cited_wa("وَهَاتَا", "ta-ishara", "pron", [ISH, "huruf-tanbih"], "هَاتَا مَعْطُوفٌ.", "«and this (f.)».", "«ve bu (müennes)».", "تَا"),
  cited_wa("وَهَاتَانِ", "tani-ishara", "pron", [ISH, "al-muthanna", "huruf-tanbih"], "هَاتَانِ مَعْطُوفٌ.", "«and these two (f.)».", "«ve bu ikisi (müennes)».", "تَانِ"),
  cited_wa("وَهٰؤُلَاءِ", "ula-ishara", "pron", [ISH, "huruf-tanbih"], "هٰؤُلَاءِ مَعْطُوفٌ.", "«and these».", "«ve bunlar».", "أُولَاءِ", punct="."),
 ]})
for _t in S[5]["tokens"][5:]:
    if _t["surface"]["full"] != "هٰذَا":
        _f = _t["surface"]["full"]; _ha = "هٰ" if "هٰ" in _f else "هَا"; _rest = _f[len("وَ") + len(_ha):]
        _t["segments"] = [seg("وَ", "wa", "conj"), seg(_ha, "ha-tanbih", "part"), seg(_rest, _t["segments"][-1]["lex"], "pron")]

# ----------- s7 (RESTORED): the kaf of address
S.append({"id": "s7", "translation": {
 "en": "And the letter of address attaches to it, as in ذَاكَ، ذَاكُمَا، ذَاكُمْ، ذَاكِ، ذَاكُمَا and ذَاكُنَّ." + R_EN,
 "tr": "Sonuna hitap harfi bitişir: ذَاكَ، ذَاكُمَا، ذَاكُمْ، ذَاكِ، ذَاكُمَا ve ذَاكُنَّ gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَلْحَقُهَا", "lahiqa", "verb", ["fail", "maful-bihi"], "يَلْحَقُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَهَا مَفْعُولٌ بِهِ.", "«and attaches to it».", "«ve ona bitişir».", "يَلْحَقُ", extra_segs=[seg("يَلْحَقُ", "lahiqa", "verb"), pr3fs()]),
  W("حَرْفُ", "harf", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letter of».", "«harfi»."),
  W("الْخِطَابِ", "khitab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْكَافُ بِفُرُوعِهَا، حَرْفٌ لَا مَحَلَّ لَهُ.", "«address» — the kāf with its branches, a particle without maḥall.", "«hitap» — dallarıyla kâf; mahalsiz harf.", punct="،"),
  nahwu(),
  cited("ذَاكَ", "dhalika", "pron", ["idafa-definiteness", ISH], "فِي مَحَلِّ جَرٍّ — ذَا وَكَافُ الْخِطَابِ لِلْمُفْرَدِ الْمُذَكَّرِ.", "«that» — the kāf for one man.", "«şu» — bir erkeğe hitap kâfı.", segments=[seg("ذَا", "dha", "pron"), seg("كَ", "kaf-letter", "part")]),
  cited_wa("وَذَاكُمَا", "dhalika", "pron", [ISH], "ذَاكُمَا مَعْطُوفٌ — لِلْمُثَنَّى.", "«and that (to two)».", "«ve şu (ikinize)».", "ذَا"),
  cited_wa("وَذَاكُمْ", "dhalika", "pron", [ISH], "ذَاكُمْ مَعْطُوفٌ — لِلْجَمْعِ الْمُذَكَّرِ.", "«and that (to men)».", "«ve şu (erkeklere)».", "ذَا"),
  cited_wa("وَذَاكِ", "dhalika", "pron", [ISH], "ذَاكِ مَعْطُوفٌ — لِلْمُفْرَدَةِ.", "«and that (to a woman)».", "«ve şu (bir kadına)».", "ذَا"),
  cited_wa("وَذَاكُمَا", "dhalika", "pron", [ISH], "ذَاكُمَا مَعْطُوفٌ — لِلْمُثَنَّى الْمُؤَنَّثِ.", "«and that (to two women)».", "«ve şu (iki kadına)».", "ذَا"),
  cited_wa("وَذَاكُنَّ", "dhalika", "pron", [ISH], "ذَاكُنَّ مَعْطُوفٌ — لِلْجَمْعِ الْمُؤَنَّثِ.", "«and that (to women)».", "«ve şu (kadınlara)».", "ذَا", punct="."),
 ]})
for _t, _k in zip(S[6]["tokens"][5:], ["كُمَا", "كُمْ", "كِ", "كُمَا", "كُنَّ"]):
    _t["segments"] = [seg("وَ", "wa", "conj"), seg("ذَا", "dha", "pron"), seg(_k, "kaf-letter", "part")]

# ----------- s8 (COMMENTARY): five letters, twenty-five forms
S.append({"id": "s8", "translation": {
 "en": "And the letters of address are five, since the two duals are one; so when they are multiplied by the five kinds of demonstrative they come to twenty-five." + C_EN,
 "tr": "Hitap harfleri, iki tesniye bir olduğundan beştir; işaretin beş nev'iyle çarpılınca yirmi beş eder." + C_TR},
 "tokens": [
  atf_wa("وَحُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "حُرُوفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the letters of» — the mubtada.", "«ve harfleri» — mübtedâ.", "حُرُوفُ"),
  W("الْخِطَابِ", "khitab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«address».", "«hitap»."),
  W("خَمْسَةٌ", "khamsa", "noun", ["mubtada-khabar", "tamyiz"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«are five» — the khabar.", "«beştir» — haber."),
  li_("لِاتِّحَادِ", "ittihad", "noun", ["lam-taleel", "idafa-definiteness", "masdar", "form-viii-verbs"], "اتِّحَادِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — اللَّامُ لِلتَّعْلِيلِ.", "«because of the sameness of».", "«bir olması sebebiyle».", "اتِّحَادِ", segs=[seg("لِ", "lam-taleel", "part"), seg("اتِّحَادِ", "ittihad", "noun")]),
  W("الْمُثَنَّيَيْنِ", "muthanna", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — كُمَا لِلْمُذَكَّرِ وَالْمُؤَنَّثِ.", "«the two duals» — كُمَا serves both genders.", "«iki tesniyenin» — kümâ her iki cinse.", punct="،"),
  W("فَإِذَا", "idha", "part", ["idha-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«so when».", "«öyleyse ... -ınca».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  W("ضُرِبَتْ", "daraba", "verb", ["idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "«are multiplied» — the passive, its deputy concealed.", "«çarpılırsa» — meçhul, nâibi gizli."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«ile»."),
  W("أَنْوَاعِ", "naw", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the kinds of».", "«nev'leri»."),
  W("الْإِشَارَةِ", "ishara-nahw", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the demonstrative».", "«işaretin»."),
  W("الْخَمْسَةِ", "khamsa", "noun", ["naat-sifa", "tamyiz"], "صِفَةٌ لِأَنْوَاعِ مَجْرُورَةٌ.", "«five» — the naʿt.", "«beş» — sıfat."),
  W("بَلَغَتْ", "balagha", "verb", ["al-majzum-wal-shart-wal-jaza", "fail"], "فِعْلٌ مَاضٍ، جَوَابُ إِذَا، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "«they come to» — the answer.", "«ulaşır» — cevap."),
  W("خَمْسَةً", "khamsa", "noun", ["maful-bihi", "tamyiz"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«five» — the object.", "«beş» — mef'ûl."),
  atf_wa("وَعِشْرِينَ", "ishrun", "noun", ["tamyiz", "jam-mudhakkar-salim"], "عِشْرِينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ.", "«and twenty» — naṣb by the yāʾ.", "«ve yirmi» — yâ ile mansûb.", "عِشْرِينَ", punct="."),
 ]})

# ----------- s9 (RESTORED): the relative defined
S.append({"id": "s9", "translation": {
 "en": "The relative: what is not complete as a part of speech except with a connecting clause and a returning pronoun." + R_EN,
 "tr": "Mevsûl: bir sıla ve bir âid olmadan cümlenin bir cüz'ü olarak tamamlanmayandır." + R_TR},
 "tokens": [
  W("الْمَوْصُولُ", "mawsul", "noun", ["mubtada-khabar", MWS], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the relative» — the mubtada.", "«mevsûl» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«-maz»."),
  W("يَتِمُّ", "tamma", "verb", ["ism-mawsul", "fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«is complete» — the ṣila, its doer the ʿāʾid.", "«tamamlanır» — sıla; fâili âid."),
  W("جُزْءًا", "juz", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: جُزْءًا مِنَ الْكَلَامِ.", "«as a part» — the ḥāl: a part of the sentence.", "«bir cüz' olarak» — hâl: cümlenin bir cüz'ü."),
  W("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except».", "«ancak»."),
  W("بِصِلَةٍ", "sila", "noun", ["huruf-jarr", MWS], "الْبَاءُ حَرْفُ جَرٍّ، وَصِلَةٍ مَجْرُورٌ.", "«with a ṣila» — the clause after it.", "«bir sıla ile» — sonrasındaki cümle.", segments=[seg("بِ", "bi", "prep"), seg("صِلَةٍ", "sila", "noun")]),
  atf_wa("وَعَائِدٍ", "aid", "noun", [MWS, "ism-fail"], "عَائِدٍ مَعْطُوفٌ مَجْرُورٌ.", "«and an ʿāʾid» — the pronoun in the ṣila pointing back.", "«ve bir âid» — sıladaki geri dönen zamir.", "عَائِدٍ", punct="."),
 ]})

# ----------- s10 (RESTORED)
S.append({"id": "s10", "translation": {
 "en": "And it is: الَّذِي and الَّتِي; اللَّذَانِ and اللَّتَانِ in rafʿ, and اللَّذَيْنِ and اللَّتَيْنِ in naṣb and jarr." + R_EN,
 "tr": "Bunlar: الَّذِي ve الَّتِي; ref'de اللَّذَانِ ve اللَّتَانِ, nasb ve cerde اللَّذَيْنِ ve اللَّتَيْنِ." + R_TR},
 "tokens": [
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هُوَ", punct=":"),
  cited("الَّذِي", "alladhi", "pron", ["mubtada-khabar", MWS], "فِي مَحَلِّ رَفْعٍ خَبَرٌ — لِلْمُفْرَدِ الْمُذَكَّرِ.", "«الَّذِي» — for one masculine.", "«ellezî» — müfred müzekker için."),
  cited_wa("وَالَّتِي", "allati", "pron", [MWS], "الَّتِي مَعْطُوفٌ — لِلْمُفْرَدَةِ.", "«and الَّتِي» — for one feminine.", "«ve elletî» — müfred müennes için.", "الَّتِي", punct="؛"),
  cited_wa("وَاللَّذَانِ", "alladhani", "pron", [MWS, "al-muthanna"], "اللَّذَانِ مَعْطُوفٌ — مُثَنَّى الَّذِي فِي الرَّفْعِ.", "«and اللَّذَانِ» — the dual of الَّذِي in rafʿ.", "«ve ellezâni» — ellezî'nin tesniyesi, ref'de.", "اللَّذَانِ"),
  cited_wa("وَاللَّتَانِ", "allatani", "pron", [MWS, "al-muthanna"], "اللَّتَانِ مَعْطُوفٌ — مُثَنَّى الَّتِي.", "«and اللَّتَانِ».", "«ve elletâni».", "اللَّتَانِ"),
  *fi_raf(punct="،"),
  cited_wa("وَاللَّذَيْنِ", "alladhani", "pron", [MWS, "al-muthanna"], "اللَّذَيْنِ مَعْطُوفٌ — بِالْيَاءِ.", "«and اللَّذَيْنِ» — with the yāʾ.", "«ve ellezeyni» — yâ ile.", "اللَّذَيْنِ"),
  cited_wa("وَاللَّتَيْنِ", "allatani", "pron", [MWS, "al-muthanna"], "اللَّتَيْنِ مَعْطُوفٌ.", "«and اللَّتَيْنِ».", "«ve elleteyni».", "اللَّتَيْنِ"),
  *fi_nasb_jarr(punct="."),
 ]})

# ----------- s11 (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "And الَّذِينَ and الْأُلَى for the masculine plural; اللَّاتِي، اللَّوَاتِي and اللَّائِي for the feminine plural." + R_EN,
 "tr": "Cemi müzekker için الَّذِينَ ve الْأُلَى; cemi müennes için اللَّاتِي، اللَّوَاتِي ve اللَّائِي." + R_TR},
 "tokens": [
  cited_wa("وَالَّذِينَ", "alladhina", "pron", [MWS, "mubtada-khabar"], "الَّذِينَ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى الْفَتْحِ فِي الْأَحْوَالِ كُلِّهَا.", "«and الَّذِينَ» — built on the fatḥ in every case.", "«ve ellezîne» — her hâlde feth üzere mebnî.", "الَّذِينَ"),
  cited_wa("وَالْأُلَى", "al-ula-mawsul", "pron", [MWS], "الْأُلَى مَعْطُوفٌ — عَلَى وَزْنِ عُلَى.", "«and الْأُلَى» — on the pattern عُلَى.", "«ve el-ulâ» — ulâ vezninde.", "الْأُلَى"),
  li_("لِلْجَمْعِ", "jam", "noun", [], "الْجَمْعِ مَجْرُورٌ.", "«for the plural».", "«cemi için».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("الْجَمْعِ", "jam", "noun")]),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«masculine».", "«müzekker».", punct="؛"),
  cited_wa("وَاللَّاتِي", "allati-pl", "pron", [MWS], "اللَّاتِي مَعْطُوفٌ.", "«and اللَّاتِي».", "«ve ellâtî».", "اللَّاتِي"),
  cited_wa("وَاللَّوَاتِي", "allawati", "pron", [MWS], "اللَّوَاتِي مَعْطُوفٌ.", "«and اللَّوَاتِي».", "«ve ellevâtî».", "اللَّوَاتِي"),
  cited_wa("وَاللَّائِي", "allai", "pron", [MWS], "اللَّائِي مَعْطُوفٌ.", "«and اللَّائِي».", "«ve ellâî».", "اللَّائِي"),
  li_("لِلْجَمْعِ", "jam", "noun", [], "الْجَمْعِ مَجْرُورٌ.", "«for the plural».", "«cemi için».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("الْجَمْعِ", "jam", "noun")]),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«feminine».", "«müennes».", punct="."),
 ]})

# ----------- s12 (RESTORED + the two ayas as the notebook cites them)
S.append({"id": "s12", "translation": {
 "en": "And مَنْ for those with reason, and مَا for the rest — as in «Everyone upon it passes away» and «What is with you runs out, and what is with God abides»." + R_EN,
 "tr": "Akıl sahipleri için مَنْ, diğerleri için مَا — «Onun üzerindeki herkes fânîdir» ve «Sizin yanınızdaki tükenir, Allah'ın yanındaki bâkîdir» gibi." + R_TR},
 "tokens": [
  cited_wa("وَمَنْ", "man", "pron", [MWS, "mubtada-khabar"], "مَنْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and مَنْ» — the mubtada.", "«ve men» — mübtedâ.", "مَنْ"),
  li_("لِذَوِي", "dhu", "noun", ["idafa-definiteness", "mubtada-khabar", "jam-mudhakkar-salim"], "ذَوِي مَجْرُورٌ بِالْيَاءِ — جَمْعُ ذُو، مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for those possessed of» — the plural of ذُو, jarr by the yāʾ; the phrase is the khabar.", "«sahipleri için» — zû'nun cem'i, yâ ile mecrûr; haber.", "ذَوِي", segs=[seg("لِ", "li", "prep"), seg("ذَوِي", "dhu", "noun")]),
  W("الْعُقُولِ", "aql", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ عَقْلٍ.", "«reason» — the plural of عَقْل.", "«akıl» — aklın cem'i.", punct="،"),
  cited_wa("وَمَا", "ma-mawsula", "pron", [MWS, "mubtada-khabar", "anwa-ma"], "مَا مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and مَا» — the mubtada.", "«ve mâ» — mübtedâ.", "مَا"),
  li_("لِغَيْرِهِمْ", "ghayr", "noun", ["idafa-definiteness", "mubtada-khabar"], "غَيْرِ مَجْرُورٌ، وَهِمْ مُضَافٌ إِلَيْهِ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the rest» — the khabar.", "«diğerleri için» — haber.", "غَيْرِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("غَيْرِ", "ghayr", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  nahwu(),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness", "al-iqtibas-wal-tadmin"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ (الرَّحْمٰن ٢٦).", "«everyone» — the mubtada (al-Raḥmān 55:26).", "«herkes» — mübtedâ (Rahmân 55:26)."),
  W("مَنْ", "man", "pron", [MWS, "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — لِلْعُقَلَاءِ.", "«who» — the relative for the rational, annexed.", "«kim» — akıllılar için mevsûl, muzâfun ileyh."),
  W("عَلَيْهَا", "ala", "prep", ["huruf-jarr", MWS], "عَلَى حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ صِلَةُ مَنْ.", "«upon it» — the ṣila, a jarr phrase.", "«onun üzerinde» — sıla, câr-mecrûr.", segments=[seg("عَلَيْ", "ala", "prep"), pr3fs()]),
  W("فَانٍ", "fanin", "noun", ["mubtada-khabar", "ism-fail", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ.", "«passes away» — the khabar, a manqūṣ with its yāʾ dropped.", "«fânîdir» — haber, yâ'sı düşmüş mankûs.", punct="،"),
  W("وَمَا", "ma-mawsula", "pron", [MWS, "mubtada-khabar", "anwa-ma", "al-iqtibas-wal-tadmin"], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ (النَّحْل ٩٦).", "«and what» — the relative for the non-rational, the mubtada (al-Naḥl 16:96).", "«ve ... şey» — akılsızlar için mevsûl, mübtedâ (Nahl 16:96).", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  W("عِنْدَكُمْ", "inda", "noun", [MWS, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَكُمْ مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is with you» — the ṣila.", "«sizin yanınızdaki» — sıla.", segments=[seg("عِنْدَ", "inda", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
  W("يَنْفَدُ", "nafida", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ.", "«runs out» — the khabar clause.", "«tükenir» — haber cümlesi."),
  W("وَمَا", "ma-mawsula", "pron", [MWS, "mubtada-khabar", "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا مُبْتَدَأٌ.", "«and what».", "«ve ... şey».", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  W("عِنْدَ", "inda", "noun", [MWS, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةُ مَا.", "«is with».", "«yanındaki»."),
  W("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God».", "«Allah'ın»."),
  W("بَاقٍ", "baqin", "noun", ["mubtada-khabar", "ism-fail", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«abides» — the khabar, a manqūṣ.", "«bâkîdir» — haber, mankûs.", punct="."),
 ]})
for _t in S[11]["tokens"]:
    if _t["surface"]["full"] == "كُلُّ": _t["quoteBefore"] = "﴿"
    if _t["surface"]["full"] == "فَانٍ": _t["quoteAfter"] = "﴾"
    if _t["surface"]["full"] == "بَاقٍ": _t["quoteAfter"] = "﴾"
_i = [j for j, t in enumerate(S[11]["tokens"]) if t["surface"]["full"] == "وَمَا"][1]
S[11]["tokens"][_i]["quoteBefore"] = "﴿"

# ----------- s13 (COMMENTARY)
S.append({"id": "s13", "translation": {
 "en": "And they are mabnī like all the relatives, because the changing of their ending is by coinage, not by a governor." + C_EN,
 "tr": "Bütün mevsûller gibi bunlar da mebnîdir; çünkü sonlarının değişmesi âmil sebebiyle değil, vaz' iledir." + C_TR},
 "tokens": [
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and they».", "«ve bunlar».", "هِيَ"),
  W("مَبْنِيَّةٌ", "mabni", "noun", ["mubtada-khabar", K3], "خَبَرٌ مَرْفُوعٌ.", "«mabnī» — the khabar: اللَّذَانِ and اللَّتَانِ included.", "«mebnîdir» — haber: ellezâni ve elletâni dâhil."),
  W("كَسَائِرِ", "sair-rest", "noun", ["huruf-jarr", "idafa-definiteness"], "الْكَافُ حَرْفُ جَرٍّ، وَسَائِرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«like all».", "«bütün ... gibi».", segments=[seg("كَ", "ka", "prep"), seg("سَائِرِ", "sair-rest", "noun")]),
  W("الْمَوْصُولَاتِ", "mawsul", "noun", ["idafa-definiteness", "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the relatives».", "«mevsûllerin».", punct="،"),
  *mabni_why("", "", ""),
 ]})

# ---------------------------------------------------------------- NFC
def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "ishara-nahw": need("ishara-nahw", "إِشَارَة", "ش و ر", "noun", "pointing — اسْمُ الْإِشَارَةِ: the demonstrative noun, coined for a thing pointed at (masdar of Form IV أَشَارَ)", "işaret — ismü'l-işâre: işaret edilen için konulmuş isim (eşâra'nın masdarı)", 3),
 "mushar": need("mushar", "مُشَار", "ش و ر", "noun", "pointed at (ism maf'ul of Form IV أَشَارَ) — مُشَارٌ إِلَيْهِ: the thing a demonstrative points to", "işaret edilen (eşâra'nın ism-i mef'ûlü) — müşârün ileyh", 4),
 "dhani": need("dhani", "ذَانِ", None, "pron", "these two (masc. dual demonstrative; ذَيْنِ in naṣb and jarr)", "bu ikisi (müzekker tesniye işaret ismi; nasb ve cerde zeyni)", 3),
 "ti-ishara": need("ti-ishara", "تِي", None, "pron", "this (fem. demonstrative, a variant of تَا)", "bu (müennes işaret ismi, tâ'nın bir şekli)", 4),
 "dhi-ishara": need("dhi-ishara", "ذِي", None, "pron", "this (fem. demonstrative, a variant of تَا)", "bu (müennes işaret ismi, tâ'nın bir şekli)", 4),
 "dhih-ishara": need("dhih-ishara", "ذِهْ", None, "pron", "this (fem. demonstrative with the hāʾ of pause)", "bu (sekte hâ'sıyla müennes işaret ismi)", 4),
 "tani-ishara": need("tani-ishara", "تَانِ", None, "pron", "these two (fem. dual demonstrative; تَيْنِ in naṣb and jarr)", "bu ikisi (müennes tesniye işaret ismi; nasb ve cerde teyni)", 3),
 "ula-qasr": need("ula-qasr", "أُولَى", None, "pron", "these (the plural demonstrative in its shortened form; أُولَاءِ lengthened)", "bunlar (cemi işaret isminin kasr ile şekli; medd ile ulâi)", 4),
 "jumhur": need("jumhur", "جُمْهُور", "ج م ه ر", "noun", "the majority (of the grammarians)", "cumhûr, çoğunluk (nahivcilerin)", 4),
 "alladhani": need("alladhani", "اللَّذَانِ", None, "pron", "the two who (masc. dual relative; اللَّذَيْنِ in naṣb and jarr)", "o ikisi ki (müzekker tesniye mevsûl; nasb ve cerde ellezeyni)", 3),
 "allatani": need("allatani", "اللَّتَانِ", None, "pron", "the two who (fem. dual relative; اللَّتَيْنِ in naṣb and jarr)", "o ikisi ki (müennes tesniye mevsûl; nasb ve cerde elleteyni)", 3),
 "al-ula-mawsul": need("al-ula-mawsul", "الْأُلَى", None, "pron", "those who (plural relative on the pattern عُلَى, mostly masculine)", "onlar ki (ulâ vezninde cemi mevsûl; daha çok müzekker)", 5),
 "allati-pl": need("allati-pl", "اللَّاتِي", None, "pron", "those who (fem. plural relative)", "onlar ki (müennes cemi mevsûl)", 3),
 "allawati": need("allawati", "اللَّوَاتِي", None, "pron", "those who (fem. plural relative)", "onlar ki (müennes cemi mevsûl)", 4),
 "allai": need("allai", "اللَّائِي", None, "pron", "those who (plural relative, mostly feminine; also اللَّاءِ and اللَّايِ)", "onlar ki (cemi mevsûl, daha çok müennes; ellâi ve ellâyi de)", 4),
 "ittihad": need("ittihad", "اِتِّحَاد", "و ح د", "noun", "being one, sameness (masdar of Form VIII اِتَّحَدَ)", "bir olma, aynılık (ittehada'nın masdarı)", 4),
 "fanin": need("fanin", "فَانٍ", "ف ن ي", "noun", "passing away, perishing (ism fa'il of فَنِيَ; a manqūṣ)", "fânî, yok olucu (feniye'nin ism-i fâili; mankûs)", 3),
 "nafida": need("nafida", "نَفِدَ", "ن ف د", "verb", "to run out, to be used up (نَفِدَ يَنْفَدُ)", "tükenmek, bitmek (nefide yenfedü)", 3),
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
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "nafida", _sg.sound1("samia", "نَفِد", "نْفَد", "اِنْفَد", "نَفَاد", "نَافِد", "مَنْفُود", "نُفِدَ", "يُنْفَدُ", "نَفِدَ الشَّيْءُ يَنْفَدُ نَفَادًا: فَنِيَ وَذَهَبَ — مِنَ الْبَابِ الرَّابِعِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch5 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": K,
 "title": {"ar": "أَسْمَاءُ الْإِشَارَةِ وَالْمَوْصُولَاتُ فِي الْكَافِيَةِ", "en": "The demonstratives and the relatives in the Kafiya: their forms, the ha of alerting, the kaf of address, the sila and the 'a'id, and why they are mabni", "tr": "Kâfiye'de işaret isimleri ve mevsûller: şekilleri, tenbih hâ'sı, hitap kâfı, sıla ile âid ve neden mebnî oldukları"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — اسم الإشارة: ما وضع لمشار إليه؛ الموصول: ما لا يتم جزءا إلا بصلة وعائد", "ضياء صونغور اوغلى — دفتر الكافية: صيغ الإشارة والموصول، سؤال الإعراب وجواب الجمهور، حروف الخطاب الخمسة والصيغ الخمس والعشرون، الآيتان"],
 "question": {
  "en": ["What is the DEMONSTRATIVE? A noun coined for a thing pointed at: ذَا for one man, ذَانِ / ذَيْنِ for two, تَا تِي ذِي ذِهْ for one woman, تَانِ / تَيْنِ for two, أُولَى / أُولَاءِ for all plurals.",
         "Is ذَانِ muʿrab, since it changes to ذَيْنِ? For the majority no: the change is by coinage (the two forms were coined), not by a governor — which is the whole definition of mabnī.",
         "What enters before it? The hāʾ of alerting (هٰذَا، هٰذَانِ، هَاتَا، هَاتَانِ، هٰؤُلَاءِ). What attaches after it? The kāf of address with its five letters (كَ كُمَا كُمْ كِ كُنَّ — the two كُمَا are one), five letters times five kinds, twenty-five forms: ذَاكَ … ذَاكُنَّ.",
         "What is the RELATIVE? A noun that is not a complete part of speech until a ṣila (the clause after it) and an ʿāʾid (the pronoun inside the ṣila pointing back) complete it: الَّذِي الَّتِي، اللَّذَانِ اللَّتَانِ / اللَّذَيْنِ اللَّتَيْنِ، الَّذِينَ الْأُلَى، اللَّاتِي اللَّوَاتِي اللَّائِي.",
         "مَنْ or مَا? مَنْ for those with reason, مَا for the rest: ﴿كُلُّ مَنْ عَلَيْهَا فَانٍ﴾ — ﴿مَا عِنْدَكُمْ يَنْفَدُ وَمَا عِنْدَ اللهِ بَاقٍ﴾. The ʿāʾid may be a hidden doer (فَانٍ's subject) or the ṣila may be a bare ẓarf (عِنْدَكُمْ).",
         "What does the engine read? The DabtEngine keeps every demonstrative and relative mabnī (no ending to predict), reads the cited forms after نَحْوُ as words in the place of jarr, and finds the manqūṣ khabars فَانٍ and بَاقٍ by their taqdīrī ḍamma."],
  "tr": ["İŞARET İSMİ nedir? İşaret edilen için konulmuş isim: bir erkek için ذَا, iki için ذَانِ / ذَيْنِ, bir kadın için تَا تِي ذِي ذِهْ, iki için تَانِ / تَيْنِ, bütün cemiler için أُولَى / أُولَاءِ.",
         "ذَيْنِ'ye dönüştüğüne göre ذَانِ mu'reb midir? Cumhûra göre hayır: değişme âmille değil vaz' iledir (iki şekil ayrı ayrı konulmuştur) — mebnînin tarifi de budur.",
         "Önüne ne gelir? Tenbih hâ'sı (هٰذَا، هٰذَانِ، هَاتَا، هَاتَانِ، هٰؤُلَاءِ). Sonuna ne bitişir? Beş harfiyle hitap kâfı (كَ كُمَا كُمْ كِ كُنَّ — iki كُمَا birdir); beş harf çarpı beş nev', yirmi beş şekil: ذَاكَ … ذَاكُنَّ.",
         "MEVSÛL nedir? Bir sıla (sonrasındaki cümle) ve bir âid (sıla içinde ona dönen zamir) tamamlamadıkça cümlenin tam bir cüz'ü olmayan isim: الَّذِي الَّتِي، اللَّذَانِ اللَّتَانِ / اللَّذَيْنِ اللَّتَيْنِ، الَّذِينَ الْأُلَى، اللَّاتِي اللَّوَاتِي اللَّائِي.",
         "مَنْ mi مَا mı? Akıl sahipleri için مَنْ, diğerleri için مَا: ﴿كُلُّ مَنْ عَلَيْهَا فَانٍ﴾ — ﴿مَا عِنْدَكُمْ يَنْفَدُ وَمَا عِنْدَ اللهِ بَاقٍ﴾. Âid gizli bir fâil olabilir (فَانٍ'in öznesi), sıla yalın bir zarf olabilir (عِنْدَكُمْ).",
         "Motor neyi okur? DabtEngine her işaret ismini ve mevsûlü mebnî tutar (tahmin edilecek son yoktur), نَحْوُ'dan sonra zikredilen şekilleri cer mahallinde kelime olarak okur ve فَانٍ ile بَاقٍ mankûs haberlerini takdîrî dammeleriyle bulur."]},
 "plain": {
  "en": "A demonstrative points at something; a relative needs the clause after it to say anything. Both have fixed forms for one, two and many, masculine and feminine, and both are mabnī: their forms were coined that way, no governor changes them. مَنْ is for people, مَا for things.",
  "tr": "İşaret ismi bir şeyi gösterir; mevsûl bir şey söylemek için sonrasındaki cümleye muhtaçtır. İkisinin de bir, iki ve çok, müzekker ve müennes için sabit şekilleri vardır ve ikisi de mebnîdir: şekilleri öyle konulmuştur, âmil değiştirmez. مَنْ kişiler, مَا şeyler içindir."},
 "explanation": {
  "en": "Ibn al-Hajib defines the demonstrative by its job — a noun coined for a thing pointed at — and lists its forms by number and gender; the notebook adds the question every student asks at ذَانِ / ذَيْنِ: is it not muʿrab, since the ending moves? The majority's answer is the definition of mabnī turned round: a word is muʿrab only when a GOVERNOR moves its ending, and here the two forms were coined separately, so the change is by coinage. The same answer returns for اللَّذَانِ / اللَّذَيْنِ at the end of the chapter. Two particles frame the demonstrative: the hāʾ of alerting in front (هٰذَا) and the kāf of address behind (ذَاكَ), and the notebook counts the kāf's forms — five letters, because كُمَا serves both duals, against five kinds of pointing, twenty-five words. The relative is defined by what it lacks: it is not a complete part of speech until a ṣila follows and an ʿāʾid inside the ṣila returns to it; its forms run parallel to the demonstrative's. مَنْ and مَا are relatives too, divided by reason, and the two āyas the notebook cites show both a hidden ʿāʾid (the doer of فَانٍ, the subject of يَنْفَدُ) and a ṣila that is nothing but a ẓarf (عِنْدَكُمْ).",
  "tr": "İbnü'l-Hâcib işaret ismini işiyle tarif eder — işaret edilen için konulmuş isim — ve şekillerini sayı ve cinse göre sayar; defter her talebenin ذَانِ / ذَيْنِ'de sorduğu soruyu ekler: sonu değiştiğine göre mu'reb değil midir? Cumhûrun cevabı mebnî tarifinin tersten okunuşudur: bir kelime ancak ÂMİL sonunu değiştirince mu'rebdir; burada iki şekil ayrı ayrı konulmuştur, değişme vaz' iledir. Aynı cevap bâbın sonunda اللَّذَانِ / اللَّذَيْنِ için döner. İşaret ismini iki harf çerçeveler: önde tenbih hâ'sı (هٰذَا), arkada hitap kâfı (ذَاكَ); defter kâfın şekillerini sayar — كُمَا iki tesniyeye birden hizmet ettiğinden beş harf, beş işaret nev'iyle çarpılınca yirmi beş kelime. Mevsûl eksiğiyle tarif edilir: bir sıla gelip içindeki bir âid ona dönmedikçe cümlenin tam bir cüz'ü değildir; şekilleri işaret ismininkine paraleldir. مَنْ ve مَا da mevsûldür, akılla ayrılır; defterin zikrettiği iki âyet hem gizli bir âidi (فَانٍ'in fâili, يَنْفَدُ'nün öznesi) hem de yalnız bir zarftan ibaret sılayı (عِنْدَكُمْ) gösterir."},
 "examples": [
  {"ar": "اسْمُ الْإِشَارَةِ: مَا وُضِعَ لِمُشَارٍ إِلَيْهِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "ذَا، وَذَانِ فِي الرَّفْعِ وَذَيْنِ فِي النَّصْبِ وَالْجَرِّ", "en": "The masculine forms.", "tr": "Müzekker şekiller.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "هٰذَا وَهٰذَانِ وَهَاتَا وَهَاتَانِ وَهٰؤُلَاءِ", "en": "The hāʾ of alerting.", "tr": "Tenbih hâ'sı.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "ذَاكَ وَذَاكُمَا وَذَاكُمْ وَذَاكِ وَذَاكُمَا وَذَاكُنَّ", "en": "The kāf of address.", "tr": "Hitap kâfı.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "الْمَوْصُولُ: مَا لَا يَتِمُّ جُزْءًا إِلَّا بِصِلَةٍ وَعَائِدٍ", "en": "The relative defined.", "tr": "Mevsûlün tarifi.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "كُلُّ مَنْ عَلَيْهَا فَانٍ — مَا عِنْدَكُمْ يَنْفَدُ وَمَا عِنْدَ اللهِ بَاقٍ", "en": "مَنْ for the rational, مَا for the rest (55:26, 16:96).", "tr": "Akıllılar için مَنْ, diğerleri için مَا (55:26, 16:96).", "sourceStory": "al-kafiya", "sentence": "s12"}],
 "commonMistakes": [
  {"wrong": "«ذَانِ mu'rebdir, çünkü nasbda ذَيْنِ olur»",
   "right": "«ذَانِ cumhûra göre mebnîdir: değişme vaz' iledir, âmille değil»",
   "why": {"en": "Only a change made by a governor is iʿrāb; two separately coined forms are not one word declining.", "tr": "Yalnız âmilin yaptığı değişme i'râbdır; ayrı ayrı konulmuş iki şekil, çekimlenen tek kelime değildir."}},
  {"wrong": "«هٰذَا tek kelimedir, hâ işaret isminin parçasıdır»",
   "right": "«هٰذَا = هَا (tenbih harfi) + ذَا (işaret ismi)»",
   "why": {"en": "The hāʾ is a particle that enters the demonstrative; it is why هَاتَا and هٰؤُلَاءِ exist beside تَا and أُولَاءِ.", "tr": "Hâ, işaret isminin önüne giren bir harftir; تَا ve أُولَاءِ yanında هَاتَا ve هٰؤُلَاءِ bu yüzden vardır."}},
  {"wrong": "«الَّذِي tek başına mübtedâ olur: الَّذِي قَائِمٌ»",
   "right": "«الَّذِي جَاءَ قَائِمٌ — mevsûl ancak sılası ve âidiyle tamamlanır»",
   "why": {"en": "A relative without its ṣila is not yet a part of speech; the clause after it, with the pronoun returning to it, is what makes it a mubtada.", "tr": "Sılasız mevsûl henüz cümlenin bir cüz'ü değildir; ona dönen zamiri taşıyan cümle onu mübtedâ yapar."}},
  {"wrong": "«مَا عِنْدَكُمْ'deki مَا nefiy harfidir»",
   "right": "«مَا عِنْدَكُمْ'deki مَا mevsûldür: 'sizin yanınızdaki şey'; sılası عِنْدَكُمْ zarfıdır»",
   "why": {"en": "A negation needs a subject and predicate to work on; here the ẓarf is the whole ṣila and يَنْفَدُ is the khabar of مَا.", "tr": "Nefiy, üzerinde çalışacağı bir özne ve yüklem ister; burada zarf sılanın tamamıdır, يَنْفَدُ ise مَا'nın haberidir."}}],
 "relatedNotes": [ISH, MWS, K3, "huruf-tanbih", "al-muthanna", "ism-maqsur-manqus", "anwa-ma", "al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"]}

ADD_EN = (" Chapter 5 (notebook lines ~173-175): the demonstrative defined (the notebook's own Arabic), its forms, the jumhur's answer on ذَانِ / ذَيْنِ as "
          "commentary (s5), the ha of alerting and the kaf of address with the notebook's lists (s6-s7) and its count of twenty-five forms as commentary (s8), "
          "the relative defined with its forms (s9-s11), مَنْ and مَا with al-Rahman 55:26 and al-Nahl 16:96 as the notebook cites them (s12), and the mabni ruling "
          "repeated for the relatives (s13). The notebook writes the dual relatives اَلَّذَانِ / اَلَّتَانِ; the standard اللَّذَانِ / اللَّتَانِ is set.")
ADD_TR = (" Beşinci bâb (defter satırları ~173-175): işaret isminin tarifi (defterin kendi Arapçası), şekilleri, cumhûrun ذَانِ / ذَيْنِ cevabı şerh olarak (s5), "
          "tenbih hâ'sı ve hitap kâfı defterin listeleriyle (s6-s7) ve yirmi beş şekil hesabı şerh olarak (s8), mevsûlün tarifi ve şekilleri (s9-s11), defterin "
          "iktibas ettiği Rahmân 55:26 ve Nahl 16:96 ile مَنْ ve مَا (s12), mevsûller için tekrarlanan mebnî hükmü (s13). Defter tesniye mevsûlleri اَلَّذَانِ / اَلَّتَانِ "
          "yazar; standart اللَّذَانِ / اللَّتَانِ dizilmiştir.")
write_out(5, S, TITLE, ADD_EN, ADD_TR, "173-175", GLOSS_ADD, notes=(NOTE,),
          related=((ISH, [K]), (MWS, [K]), (K3, [K]), ("huruf-tanbih", [K])))
report(5, S, GLOSS_ADD, (NOTE,))
