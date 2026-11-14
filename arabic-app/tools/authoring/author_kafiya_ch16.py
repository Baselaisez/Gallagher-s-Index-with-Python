# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 16: THE ISM FA'IL, the intensives, THE ISM MAF'UL. Both definitions in the notebook's own Arabic; the shapes
(فَاعِل / the mudari' shape with a dammed mim and kasra before the last); the conditions of government (present or future sense and
reliance on a sahib, the hamza of question or a negation); the past sense forcing a ma'nawi annexation, al-Kisa'i's dissent and the
hidden verb behind دِرْهَمًا; the al-participle governing with no condition; the intensives (ضَرَّاب، ضَرُوب، مِضْرَاب، عَلِيم، حَذِر and the
notebook's eight); dual and plural like the singular, the nun dropped for lightness (الْمُقِيمِي الصَّلَاةَ); the ism maf'ul mirroring all of it.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~258-261 of the transcription.

  VERBATIM: s1, s12. RESTORED (received matn, marked): s2, s3, s4, s7, s8, s10, s11, s13. COMMENTARY (the notebook): s5, s6, s9, s14.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch16.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "ism-al-fail-wal-maful-fil-kafiya"
IF = "ism-fail"
IM = "ism-maful"
SH = "shurut-amal-ism-al-fail"
MB = "sighat-mubalagha"
TITLE = {"ar": "اِسْمُ الْفَاعِلِ وَاسْمُ الْمَفْعُولِ", "en": "The ism fāʿil and the ism mafʿūl", "tr": "İsm-i fâil ve ism-i mef'ûl"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def atf_aw(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, ["atf-nasaq"] + tags, "مَعْطُوفٌ بِأَوْ — " + ar, en, tr, punct=punct, segments=segments)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "prep"), seg(inner, lex, pos)]))
def AW(): return W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya».")
def ALAN(punct=None): return W("الْآنَ", "al-an", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ — لِلْحَالِ.", "«now».", "«şimdi».", punct=punct)
def GHADAN(punct=None): return W("غَدًا", "ghadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ — لِلِاسْتِقْبَالِ.", "«tomorrow».", "«yarın».", punct=punct)
def AMSI(punct=None): return W("أَمْسِ", "ams", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ — لِلْمَاضِي.", "«yesterday».", "«dün».", punct=punct)
def ZAYD(): return W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — صَاحِبُ اسْمِ الْفَاعِلِ الَّذِي يَعْتَمِدُ عَلَيْهِ.", "«Zayd» — the mubtada the participle relies on.", "«Zeyd» — ism-i fâilin dayandığı mübtedâ.")
def GHULAMUHU(role="fail"): return W("غُلَامُهُ", "ghulam", "noun", [role, "idafa-definiteness", SH], ("فَاعِلٌ لِاسْمِ الْفَاعِلِ" if role == "fail" else "نَائِبُ فَاعِلٍ لِاسْمِ الْمَفْعُولِ") + " مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his servant» — " + ("the participle's doer." if role == "fail" else "the passive participle's deputy doer."), "«hizmetçisi» — " + ("ism-i fâilin fâili." if role == "fail" else "ism-i mef'ûlün nâib-i fâili."), segments=[seg("غُلَامُ", "ghulam", "noun"), pr3ms()])
def AMRAN(punct=None): return W("عَمْرًا", "amr-name", "propn", ["maful-bihi", SH], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«ʿAmr» — the participle's object.", "«Amr'ı» — ism-i fâilin mef'ûlü.", punct=punct)
def DIRHAMAN(ar, en, tr, punct=None): return W("دِرْهَمًا", "dirham", "noun", ["maful-bihi", SH], ar, en, tr, punct=punct)

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The ism fāʿil: what is derived from a verb for the one in whom the event subsists, in the sense of occurrence.",
 "tr": "İsm-i fâil: hudûs mânâsında olmak üzere, hades kendisiyle kâim olan zât için fiilden türetilen isimdir."},
 "tokens": [
  W("اسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", IF], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the noun of» — the mubtada.", "«ism-i» — mübtedâ."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("اشْتُقَّ", "ishtaqqa", "verb", ["ism-mawsul", "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«is derived».", "«türetilen»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("فِعْلٍ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«fiil»."),
  li_("لِمَنْ", "man", "pron", ["ism-mawsul"], "مَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«for the one who».", "«... olan için».", "مَنْ"),
  W("قَامَ", "qama", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْحَدَثُ، وَالْجُمْلَةُ صِلَةٌ.", "«subsists» — its doer the event.", "«kâim olan» — fâili hades."),
  W("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«in him» — the ʿāʾid.", "«onunla» — âid.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ — حَالٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  W("الْحُدُوثِ", "huduth", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«occurrence» — the event comes and goes.", "«hudûs» — gelip geçicilik.", punct="."),
 ]})

# ----------- s2 (RESTORED): the shape
S.append({"id": "s2", "translation": {
 "en": "And its shape from the bare triliteral is on فَاعِلٌ, and from what is other than it on the shape of the muḍāriʿ with a ḍamma on a mīm and a kasra before the last — as in مُخْرِجٌ and مُسْتَخْرِجٌ." + R_EN,
 "tr": "Sîgası sülâsî mücerredden فَاعِلٌ vezni üzeredir; onun dışındakilerden ise mazmûm bir mîm ve sondan öncekinin kesresiyle muzâri sîgası üzeredir — مُخْرِجٌ ve مُسْتَخْرِجٌ gibi." + R_TR},
 "tokens": [
  atf_wa("وَصِيغَتُهُ", "sigha", "noun", ["mubtada-khabar", "idafa-definiteness"], "صِيغَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its shape».", "«ve sîgası».", "صِيغَتُ", extra_segs=[seg("صِيغَتُ", "sigha", "noun"), pr3ms()]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، فُتِحَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the triliteral».", "«sülâsî»."),
  W("الْمُجَرَّدِ", "mujarrad", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«bare».", "«mücerred»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«on» — the khabar.", "«üzere» — haber."),
  cited("فَاعِلٍ", "fail-doer", "noun", ["huruf-jarr", IF], "مَجْرُورٌ — الْوَزْنُ.", "«fāʿil» — the pattern.", "«fâil» — vezin.", punct="،"),
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ.", "«and from».", "«ve -den».", "مِنْ"),
  W("غَيْرِهِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what is other than it».", "«onun dışındakilerden».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: صِيغَتُهُ.", "«on».", "«üzere»."),
  W("صِيغَةِ", "sigha", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the shape of».", "«sîgası»."),
  W("الْمُضَارِعِ", "mudari", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāriʿ».", "«muzârinin»."),
  bi_("بِمِيمٍ", "mim-letter", "noun", [], "مِيمٍ مَجْرُورٌ.", "«with a mīm».", "«bir mîm ile».", "مِيمٍ"),
  W("مَضْمُومَةٍ", "madmum", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«bearing a ḍamma».", "«mazmûm»."),
  atf_wa("وَكَسْرِ", "kasr", "noun", ["idafa-definiteness"], "كَسْرِ مَعْطُوفٌ عَلَى مِيمٍ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and a kasra on».", "«ve kesresiyle».", "كَسْرِ"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what».", "«... olanın»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةُ مَا.", "«is before».", "«öncesinde»."),
  W("الْآخِرِ", "akhir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the last».", "«sonun».", punct="،"),
  nahwu(),
  cited("مُخْرِجٍ", "mukhrij", "noun", ["idafa-definiteness", IF, "form-iv-verbs"], "فِي مَحَلِّ جَرٍّ — اسْمُ فَاعِلِ أَخْرَجَ.", "«one who brings out» — of أَخْرَجَ.", "«çıkaran» — ahrace'nin ism-i fâili."),
  cited_wa("وَمُسْتَخْرِجٍ", "mustakhrij", "noun", [IF, "form-x-verbs"], "مُسْتَخْرِجٍ مَعْطُوفٌ — اسْمُ فَاعِلِ اسْتَخْرَجَ.", "«and one who extracts» — of اسْتَخْرَجَ.", "«ve istihrac eden» — istahrece'nin ism-i fâili.", "مُسْتَخْرِجٍ", punct="."),
 ]})

# ----------- s3 (RESTORED): the conditions of government
S.append({"id": "s3", "translation": {
 "en": "And it governs as its active verb governs, on condition of the sense of the present or the future and of reliance on its ṣāḥib, or on the hamza of the question, or on a letter of negation — as in زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا الْآنَ أَوْ غَدًا." + R_EN,
 "tr": "Hâl veya istikbâl mânâsı ve sâhibine yahut istifhâm hemzesine yahut nefy harfine dayanması şartıyla, ma'lûm fiilinin ameli gibi amel eder — زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا الْآنَ أَوْ غَدًا gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَعْمَلُ", "amila", "verb", ["fail", SH], "يَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it governs».", "«ve amel eder».", "يَعْمَلُ"),
  W("عَمَلَ", "amal-work", "noun", ["maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«as … governs».", "«ameli gibi»."),
  W("فِعْلِهِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its verb».", "«fiilinin».", segments=[seg("فِعْلِ", "fil", "noun"), pr3msi()]),
  W("الْمَعْلُومِ", "malum", "noun", ["naat-sifa", IF], "صِفَةٌ مَجْرُورَةٌ — الْمَبْنِيِّ لِلْفَاعِلِ.", "«active».", "«ma'lûm»."),
  bi_("بِشَرْطِ", "shart", "noun", ["idafa-definiteness", SH], "شَرْطِ مَجْرُورٌ، وَهُوَ مُضَافٌ — حَالٌ.", "«on condition of».", "«şartıyla».", "شَرْطِ"),
  W("مَعْنَى", "mana", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the sense of».", "«mânâsı»."),
  W("الْحَالِ", "hal-state", "noun", ["idafa-definiteness", SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the present».", "«hâl»."),
  atf_wa("وَالِاسْتِقْبَالِ", "istiqbal", "noun", [SH], "الِاسْتِقْبَالِ مَعْطُوفٌ مَجْرُورٌ.", "«or the future».", "«veya istikbâl».", "الِاسْتِقْبَالِ"),
  atf_wa("وَالِاعْتِمَادِ", "itimad", "noun", [SH], "الِاعْتِمَادِ مَعْطُوفٌ عَلَى مَعْنَى مَجْرُورٌ.", "«and reliance».", "«ve dayanması».", "الِاعْتِمَادِ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("صَاحِبِهِ", "sahib", "noun", ["huruf-jarr", "idafa-definiteness", SH], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْمُبْتَدَأُ أَوِ الْمَوْصُوفُ أَوِ الْمَوْصُولُ أَوْ ذُو الْحَالِ.", "«its ṣāḥib» — a mubtada, a described noun, a relative or the owner of a ḥāl.", "«sâhibine» — mübtedâ, mevsûf, mevsûl veya zü'l-hâl.", segments=[seg("صَاحِبِ", "sahib", "noun"), pr3msi()]),
  AW(),
  W("هَمْزَةِ", "hamza-letter", "noun", ["atf-nasaq", "idafa-definiteness", SH], "مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the hamza of».", "«hemzesine»."),
  W("الِاسْتِفْهَامِ", "istifham", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the question».", "«istifhâm»."),
  AW(),
  W("حَرْفِ", "harf", "noun", ["atf-nasaq", "idafa-definiteness", SH], "مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«a letter of».", "«harfine»."),
  W("النَّفْيِ", "nafy", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«negation».", "«nefy».", punct="،"),
  nahwu(),
  ZAYD(),
  W("ضَارِبٌ", "darib", "noun", ["mubtada-khabar", IF, SH], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ عَامِلٌ، مُعْتَمِدٌ عَلَى الْمُبْتَدَإِ.", "«is striking» — the participle, relying on the mubtada.", "«vurucudur» — mübtedâya dayanan ism-i fâil."),
  GHULAMUHU(),
  AMRAN(),
  ALAN(),
  AW(),
  GHADAN(punct="."),
 ]})

# ----------- s4 (RESTORED): the past sense
S.append({"id": "s4", "translation": {
 "en": "And when it is for the past, its annexation to its object by a maʿnawī annexation is obligatory — as in زَيْدٌ ضَارِبُ عَمْرٍو أَمْسِ — against al-Kisāʾī." + R_EN,
 "tr": "Mâzî için olduğunda mef'ûlüne izâfet-i ma'neviyye ile muzâf olması vâcibdir — زَيْدٌ ضَارِبُ عَمْرٍو أَمْسِ gibi — Kisâî'ye muhâlif olarak." + R_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve -dığında».", "إِذَا"),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "«it is».", "«olursa»."),
  li_("لِلْمَاضِي", "madi", "noun", ["kana-wa-akhawatuha", "ism-maqsur-manqus"], "الْمَاضِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«for the past».", "«mâzî için».", "الْمَاضِي", segs=[seg("لِ", "li", "prep"), seg("لْمَاضِي", "madi", "noun")]),
  W("وَجَبَتْ", "wajaba", "verb", ["fail", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — جَوَابُ إِذَا.", "«is obligatory».", "«vâcib olur»."),
  W("إِضَافَتُهُ", "idafa", "noun", ["fail", "idafa-definiteness", "idafa-lafziyya"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its annexation».", "«izâfeti».", segments=[seg("إِضَافَتُ", "idafa", "noun"), pr3ms()]),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("مَفْعُولِهِ", "maful-object", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its object».", "«mef'ûlüne».", segments=[seg("مَفْعُولِ", "maful-object", "noun"), pr3msi()]),
  W("إِضَافَةً", "idafa", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ.", "«by an annexation».", "«bir izâfetle»."),
  W("مَعْنَوِيَّةً", "manawi", "noun", ["naat-sifa", "idafa-lafziyya"], "صِفَةٌ مَنْصُوبَةٌ — لِفَوَاتِ شَرْطِ الْعَمَلِ.", "«maʿnawī» — the condition of government has lapsed.", "«ma'nevî» — amel şartı düşmüştür.", punct="،"),
  nahwu(),
  ZAYD(),
  W("ضَارِبُ", "darib", "noun", ["mubtada-khabar", "idafa-definiteness", IF, "idafa-lafziyya"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ بِمَعْنَى الْمَاضِي لَا يَعْمَلُ.", "«the striker of» — past sense, no government.", "«vuranı» — mâzî mânâlı, amel etmez."),
  W("عَمْرٍو", "amr-name", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَفْعُولُهُ فِي الْمَعْنَى.", "«ʿAmr» — its object in sense.", "«Amr'ı» — mânâca mef'ûlü."),
  AMSI(punct="،"),
  W("خِلَافًا", "khilaf", "noun", ["hal"], "حَالٌ مَنْصُوبٌ، أَوْ مَفْعُولٌ مُطْلَقٌ.", "«against».", "«muhâlif olarak»."),
  li_("لِلْكِسَائِيِّ", "kisai", "propn", [], "الْكِسَائِيِّ مَجْرُورٌ.", "«al-Kisāʾī».", "«Kisâî'ye».", "الْكِسَائِيِّ", punct=".", segs=[seg("لِ", "li", "prep"), seg("لْكِسَائِيِّ", "kisai", "propn")]),
 ]})

# ----------- s5 (COMMENTARY): the Kisāʾī view and the reason
S.append({"id": "s5", "translation": {
 "en": "For al-Kisāʾī the annexation is permitted, not obligatory, and when it occurs it is lafẓī; the annexation is maʿnawī for the others because the condition of government is absent, so the participle is a ṣifa annexed to something other than its governed word." + C_EN,
 "tr": "Kisâî'ye göre izâfet vâcib değil câizdir ve olduğunda lafzîdir; başkalarına göre amel şartı bulunmadığından, muzâf, ma'mûlünden başkasına muzâf bir sıfat olduğu için izâfet ma'nevîdir." + C_TR},
 "tokens": [
  W("فَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَعِنْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«for» — a fronted khabar.", "«... göre» — öne alınmış haber.", segments=[seg("فَ", "fa", "conj"), seg("عِنْدَ", "inda", "noun")]),
  W("الْكِسَائِيِّ", "kisai", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Kisāʾī».", "«Kisâî»."),
  W("الْإِضَافَةُ", "idafa", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the annexation».", "«izâfet»."),
  W("جَائِزَةٌ", "jaiz", "noun", ["mubtada-khabar"], "خَبَرٌ ثَانٍ مَرْفُوعٌ، أَوْ حَالٌ.", "«is permitted».", "«câizdir»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«değil»."),
  W("وَاجِبَةٌ", "wajib", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«obligatory».", "«vâcib».", punct="،"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هِيَ"),
  W("لَفْظِيَّةٌ", "lafzi", "noun", ["mubtada-khabar", "idafa-lafziyya"], "خَبَرٌ مَرْفُوعٌ.", "«lafẓī».", "«lafzîdir».", punct="؛"),
  atf_wa("وَالْإِضَافَةُ", "idafa", "noun", ["mubtada-khabar"], "الْإِضَافَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the annexation».", "«ve izâfet».", "الْإِضَافَةُ"),
  W("مَعْنَوِيَّةٌ", "manawi", "noun", ["mubtada-khabar", "idafa-lafziyya"], "خَبَرٌ مَرْفُوعٌ.", "«is maʿnawī».", "«ma'nevîdir»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("غَيْرِهِ", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the others».", "«başkalarına».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  li_("لِعَدَمِ", "adam", "noun", ["idafa-definiteness"], "عَدَمِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«for the absence of».", "«bulunmadığından».", "عَدَمِ"),
  W("شَرْطِ", "shart", "noun", ["idafa-definiteness", SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the condition of».", "«şartı»."),
  W("الْعَمَلِ", "amal-work", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«government».", "«amel».", punct="،"),
  W("فَالْمُضَافُ", "mudaf", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمُضَافُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the muḍāf».", "«o hâlde muzâf».", segments=[seg("فَ", "fa", "conj"), seg("الْمُضَافُ", "mudaf", "noun")]),
  W("صِفَةٌ", "sifa", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a ṣifa».", "«bir sıfattır»."),
  W("مُضَافَةٌ", "mudaf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«annexed».", "«muzâf»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«other than».", "«başkasına»."),
  W("مَعْمُولِهَا", "mamul", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its governed word».", "«ma'mûlünden».", punct=".", segments=[seg("مَعْمُولِ", "mamul", "noun"), pr3fs()]),
 ]})

# ----------- s6 (COMMENTARY): دِرْهَمًا by a hidden verb
S.append({"id": "s6", "translation": {
 "en": "And in زَيْدٌ مُعْطِي عَمْرٍو دِرْهَمًا أَمْسِ, since the participle in the past sense cannot take دِرْهَمًا as an object, دِرْهَمًا is the object of a supplied verb: أَعْطَاهُ." + C_EN,
 "tr": "زَيْدٌ مُعْطِي عَمْرٍو دِرْهَمًا أَمْسِ'de, mâzî mânâlı ism-i fâil دِرْهَمًا'yı mef'ûl alamayacağından, دِرْهَمًا takdîr edilen أَعْطَاهُ fiilinin mef'ûlüdür." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  ZAYD(),
  W("مُعْطِي", "muti", "noun", ["mubtada-khabar", "idafa-definiteness", IF, "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ بِمَعْنَى الْمَاضِي.", "«the giver of» — a manqūṣ participle, past sense.", "«vereni» — mankûs ism-i fâil, mâzî mânâlı."),
  W("عَمْرٍو", "amr-name", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَفْعُولُهُ الْأَوَّلُ فِي الْمَعْنَى.", "«ʿAmr» — its first object in sense.", "«Amr'a» — mânâca birinci mef'ûlü."),
  DIRHAMAN("مَفْعُولٌ بِهِ مَنْصُوبٌ لِفِعْلٍ مُقَدَّرٍ: أَعْطَاهُ.", "«a dirham» — the object of a supplied verb.", "«bir dirhem» — takdîr edilen fiilin mef'ûlü."),
  AMSI(punct="،"),
  W("لَمَّا", "lamma", "part", ["maful-fih", "al-majzum-wal-shart-wal-jaza"], "ظَرْفٌ بِمَعْنَى حِينَ.", "«since».", "«... -dığından»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَأْخُذْ", "akhadha", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ.", "«takes».", "«alamaz»."),
  W("اسْمُ", "ism", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  W("الْمَاضِي", "madi", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ — أَيِ: الَّذِي لِلْمَاضِي.", "«of the past».", "«mâzî mânâlı»."),
  DIRHAMAN("مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«دِرْهَمًا».", "«دِرْهَمًا'yı»."),
  W("مَفْعُولًا", "maful-object", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«as an object».", "«mef'ûl olarak»."),
  li_("لَهُ", "li", "prep", [], "الْهَاءُ مَجْرُورٌ.", "«to it».", "«kendine».", "هُ", punct="،", segs=[seg("لَ", "li", "prep"), pr3ms()]),
  W("فَدِرْهَمًا", "dirham", "noun", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ لَمَّا، وَدِرْهَمًا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«دِرْهَمًا is» — the mubtada.", "«دِرْهَمًا» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("دِرْهَمًا", "dirham", "noun")]),
  W("مَفْعُولُ", "maful-object", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the object of».", "«mef'ûlüdür»."),
  W("فِعْلٍ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«fiilin»."),
  W("مُقَدَّرٍ", "muqaddar", "noun", ["naat-sifa", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«supplied».", "«takdîr edilen».", punct=":"),
  cited("أَعْطَاهُ", "ata-give", "verb", ["fail", "maful-bihi", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْفِعْلُ الْمُقَدَّرُ.", "«he gave him» — the supplied verb.", "«ona verdi» — takdîr edilen fiil.", punct=".", segments=[seg("أَعْطَا", "ata-give", "verb"), pr3ms()]),
 ]})

# ----------- s7 (RESTORED): with the lām
S.append({"id": "s7", "translation": {
 "en": "And when the lām enters it, it governs without condition — as in مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْدًا أَمْسِ أَوِ الْآنَ أَوْ غَدًا." + R_EN,
 "tr": "Lâm dâhil olduğunda şartsız amel eder — مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْدًا أَمْسِ أَوِ الْآنَ أَوْ غَدًا gibi." + R_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve -dığında».", "إِذَا"),
  W("دَخَلَتْهُ", "dakhala", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«enters it».", "«ona dâhil olursa».", segments=[seg("دَخَلَتْ", "dakhala", "verb"), pr3ms()]),
  W("اللَّامُ", "lam-letter", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ — لَامُ التَّعْرِيفِ.", "«the lām» — the article.", "«lâm» — ta'rif lâmı."),
  W("عَمِلَ", "amila", "verb", ["fail", "al-fa-fi-jawab-al-shart", SH], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — جَوَابُ إِذَا.", "«it governs».", "«amel eder»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا نَافِيَةٌ — اسْمٌ بِمَعْنَى غَيْرٍ مَجْرُورٌ بِالْبَاءِ.", "«without».", "«-sız».", "لَا"),
  W("شَرْطٍ", "shart", "noun", ["huruf-jarr", SH], "مَجْرُورٌ.", "«condition».", "«şart».", punct="،"),
  nahwu(),
  cited("مَرَرْتُ", "marra", "verb", ["fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I passed».", "«uğradım».", segments=[seg("مَرَرْ", "marra", "verb"), prT()]),
  bi_("بِالضَّارِبِ", "darib", "noun", [IF, SH], "الضَّارِبِ مَجْرُورٌ — اسْمُ فَاعِلٍ مُعَرَّفٌ بِاللَّامِ عَامِلٌ بِلَا شَرْطٍ.", "«by the one who struck» — the al-participle.", "«vurana» — lâmlı ism-i fâil.", "الضَّارِبِ"),
  W("أَبُوهُ", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ لِاسْمِ الْفَاعِلِ مَرْفُوعٌ بِالْوَاوِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the doer, by the wāw.", "«babası» — fâil, vâv ile.", segments=[seg("أَبُو", "ab", "noun"), pr3ms()]),
  W("زَيْدًا", "zayd", "propn", ["maful-bihi", SH], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«Zayd» — its object.", "«Zeyd'i» — mef'ûlü."),
  AMSI(),
  W("أَوِ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«veya»."),
  ALAN(),
  AW(),
  GHADAN(punct="."),
 ]})

# ----------- s8 (RESTORED): the intensives
S.append({"id": "s8", "translation": {
 "en": "And the patterns of intensification — as in ضَرَّابٌ, ضَرُوبٌ, مِضْرَابٌ, عَلِيمٌ and حَذِرٌ — are like the ism fāʿil in government and in its conditions." + R_EN,
 "tr": "Mübâlağa vezinleri — ضَرَّابٌ، ضَرُوبٌ، مِضْرَابٌ، عَلِيمٌ ve حَذِرٌ gibi — amelde ve şartlarında ism-i fâil gibidir." + R_TR},
 "tokens": [
  atf_wa("وَأَمْثِلَةُ", "mithal", "noun", ["mubtada-khabar", "idafa-definiteness", MB], "أَمْثِلَةُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the patterns of».", "«ve vezinleri».", "أَمْثِلَةُ"),
  W("الْمُبَالَغَةِ", "mubalagha", "noun", ["idafa-definiteness", MB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«intensification».", "«mübâlağa».", punct="،"),
  nahwu(),
  cited("ضَرَّابٍ", "darrab", "noun", ["idafa-definiteness", MB], "فِي مَحَلِّ جَرٍّ — فَعَّالٌ.", "«a great striker» — فَعَّال.", "«çok vuran» — فَعَّال."),
  cited_wa("وَضَرُوبٍ", "darub", "noun", [MB], "ضَرُوبٍ مَعْطُوفٌ — فَعُولٌ.", "«ḍarūb» — فَعُول.", "«darûb» — فَعُول.", "ضَرُوبٍ"),
  cited_wa("وَمِضْرَابٍ", "midrab", "noun", [MB], "مِضْرَابٍ مَعْطُوفٌ — مِفْعَالٌ.", "«miḍrāb» — مِفْعَال.", "«midrâb» — مِفْعَال.", "مِضْرَابٍ"),
  cited_wa("وَعَلِيمٍ", "alim", "noun", [MB], "عَلِيمٍ مَعْطُوفٌ — فَعِيلٌ.", "«all-knowing» — فَعِيل.", "«çok bilen» — فَعِيل.", "عَلِيمٍ"),
  cited_wa("وَحَذِرٍ", "hadhir", "noun", [MB], "حَذِرٍ مَعْطُوفٌ — فَعِلٌ.", "«ever-wary» — فَعِل.", "«çok sakınan» — فَعِل.", "حَذِرٍ", punct="،"),
  ka_("كَاسْمِ", "ism", "noun", ["idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "اسْمِ مَجْرُورٌ، وَهُوَ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«are like the noun of» — the khabar.", "«ism-i … gibidir» — haber.", "اسْمِ"),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْعَمَلِ", "amal-work", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«government».", "«amel»."),
  atf_wa("وَالشُّرُوطِ", "shart", "noun", [SH], "الشُّرُوطِ مَعْطُوفٌ مَجْرُورٌ — جَمْعُ شَرْطٍ.", "«and the conditions».", "«ve şartlarda».", "الشُّرُوطِ", punct="."),
 ]})

# ----------- s9 (COMMENTARY): the notebook's eight
S.append({"id": "s9", "translation": {
 "en": "And of them: جَهُولٌ (very ignorant), صِدِّيقٌ (ever-truthful), كَذَّابٌ (a great liar), غُفُلٌ (very heedless), يَقُظٌ (ever-wakeful), مِدْرَارٌ (pouring), مِكْثِيرٌ (talking much) and لُعَنَةٌ (ever-cursing)." + C_EN,
 "tr": "Onlardan: جَهُولٌ (çok câhil), صِدِّيقٌ (çok sâdık), كَذَّابٌ (çok yalancı), غُفُلٌ (çok gâfil), يَقُظٌ (çok uyanık), مِدْرَارٌ (çok yağan), مِكْثِيرٌ (çok konuşan) ve لُعَنَةٌ (çok lânet eden)." + C_TR},
 "tokens": [
  atf_wa("وَمِنْهَا", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and of them».", "«ve onlardan».", "مِنْ", extra_segs=[seg("مِنْ", "min", "prep"), pr3fs()], punct=":"),
  cited("جَهُولٌ", "jahul", "noun", ["mubtada-khabar", MB], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — فَعُولٌ.", "«very ignorant» — فَعُول.", "«çok câhil» — فَعُول."),
  cited_wa("وَصِدِّيقٌ", "siddiq", "noun", [MB], "صِدِّيقٌ مَعْطُوفٌ — فِعِّيلٌ.", "«ever-truthful» — فِعِّيل.", "«çok sâdık» — فِعِّيل.", "صِدِّيقٌ"),
  cited_wa("وَكَذَّابٌ", "kadhdhab", "noun", [MB], "كَذَّابٌ مَعْطُوفٌ — فَعَّالٌ.", "«a great liar» — فَعَّال.", "«çok yalancı» — فَعَّال.", "كَذَّابٌ"),
  cited_wa("وَغُفُلٌ", "ghuful", "noun", [MB], "غُفُلٌ مَعْطُوفٌ — فُعُلٌ.", "«very heedless» — فُعُل.", "«çok gâfil» — فُعُل.", "غُفُلٌ"),
  cited_wa("وَيَقُظٌ", "yaquz", "noun", [MB], "يَقُظٌ مَعْطُوفٌ — فَعُلٌ.", "«ever-wakeful» — فَعُل.", "«çok uyanık» — فَعُل.", "يَقُظٌ"),
  cited_wa("وَمِدْرَارٌ", "midrar", "noun", [MB], "مِدْرَارٌ مَعْطُوفٌ — مِفْعَالٌ.", "«pouring» — مِفْعَال.", "«çok yağan» — مِفْعَال.", "مِدْرَارٌ"),
  cited_wa("وَمِكْثِيرٌ", "mikthir", "noun", [MB], "مِكْثِيرٌ مَعْطُوفٌ — مِفْعِيلٌ.", "«talking much» — مِفْعِيل.", "«çok konuşan» — مِفْعِيل.", "مِكْثِيرٌ"),
  cited_wa("وَلُعَنَةٌ", "luana", "noun", [MB], "لُعَنَةٌ مَعْطُوفٌ — فُعَلَةٌ.", "«ever-cursing» — فُعَلَة.", "«çok lânet eden» — فُعَلَة.", "لُعَنَةٌ", punct="."),
 ]})

# ----------- s10 (RESTORED): dual and plural
S.append({"id": "s10", "translation": {
 "en": "And their dual and their plural are like the singular — as in الزَّيْدَانِ ضَارِبَانِ عَمْرًا, and الزَّيْدُونَ ضَارِبُونَ عَمْرًا." + R_EN,
 "tr": "İkisinin tesniyesi ve cemi müfred gibidir — الزَّيْدَانِ ضَارِبَانِ عَمْرًا ve الزَّيْدُونَ ضَارِبُونَ عَمْرًا gibi." + R_TR},
 "tokens": [
  atf_wa("وَتَثْنِيَتُهُمَا", "tathniya", "noun", ["mubtada-khabar", "idafa-definiteness", "al-muthanna"], "تَثْنِيَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ — اسْمُ الْفَاعِلِ وَالْمُبَالَغَةُ.", "«and their dual» — of the participle and the intensive.", "«ve ikisinin tesniyesi» — ism-i fâil ile mübâlağanın.", "تَثْنِيَتُ", extra_segs=[seg("تَثْنِيَتُ", "tathniya", "noun"), pr3d()]),
  atf_wa("وَجَمْعُهُمَا", "jam", "noun", ["idafa-definiteness"], "جَمْعُ مَعْطُوفٌ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and their plural».", "«ve cemi».", "جَمْعُ", extra_segs=[seg("جَمْعُ", "jam", "noun"), pr3d()]),
  ka_("كَالْمُفْرَدِ", "mufrad", "noun", ["khabar-al-mubtada-wa-ahkamuh"], "الْمُفْرَدِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«like the singular».", "«müfred gibidir».", "الْمُفْرَدِ", punct="،"),
  nahwu(),
  cited("الزَّيْدَانِ", "zayd", "propn", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ.", "«the two Zayds».", "«iki Zeyd»."),
  W("ضَارِبَانِ", "darib", "noun", ["mubtada-khabar", "al-muthanna", IF, SH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — اسْمُ فَاعِلٍ مُثَنًّى عَامِلٌ.", "«are striking» — the dual participle governs.", "«vurucudurlar» — tesniye ism-i fâil amel eder."),
  AMRAN(punct="،"),
  cited_wa("وَالزَّيْدُونَ", "zayd", "propn", ["mubtada-khabar", "jam-mudhakkar-salim"], "الزَّيْدُونَ مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ.", "«and the Zayds».", "«ve Zeydler».", "الزَّيْدُونَ"),
  W("ضَارِبُونَ", "darib", "noun", ["mubtada-khabar", "jam-mudhakkar-salim", IF, SH], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — اسْمُ فَاعِلٍ مَجْمُوعٌ عَامِلٌ.", "«are striking» — the plural participle governs.", "«vurucudurlar» — cemi ism-i fâil amel eder."),
  AMRAN(punct="."),
 ]})

# ----------- s11 (RESTORED): the nūn dropped
S.append({"id": "s11", "translation": {
 "en": "And the nūn of the dual and the plural may be dropped for lightness from the one defined by the lām — as in الْمُقِيمِي الصَّلَاةَ on the reading in naṣb; on the reading in jarr its dropping is obligatory, for the annexation." + R_EN,
 "tr": "Lâm ile ma'rife olandan tesniye ve cemi nûnunun hafiflik için hazfi câizdir — nasb kıraatine göre الْمُقِيمِي الصَّلَاةَ gibi; cer kıraatine göre hazfi izâfetten dolayı vâcibdir." + R_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted».", "«ve câizdir».", "يَجُوزُ"),
  W("حَذْفُ", "hadhf", "noun", ["fail", "idafa-definiteness", "hadhf-wa-taqdir"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the dropping of».", "«hazfi»."),
  W("نُونِ", "nun-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnunun»."),
  W("التَّثْنِيَةِ", "tathniya", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dual».", "«tesniye»."),
  atf_wa("وَالْجَمْعِ", "jam", "noun", ["jam-mudhakkar-salim"], "الْجَمْعِ مَعْطُوفٌ مَجْرُورٌ.", "«and the plural».", "«ve cemi».", "الْجَمْعِ"),
  W("تَخْفِيفًا", "takhfif", "noun", ["maful-lah"], "مَفْعُولٌ لَهُ مَنْصُوبٌ.", "«for lightness».", "«hafiflik için»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الْمُعَرَّفِ", "muarraf", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«the one defined».", "«ma'rife olandan»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", [], "اللَّامِ مَجْرُورٌ.", "«by the lām».", "«lâm ile».", "اللَّامِ", punct="،"),
  nahwu(),
  cited("الْمُقِيمِي", "muqim", "noun", ["idafa-definiteness", IF, SH, "jam-mudhakkar-salim"], "فِي مَحَلِّ جَرٍّ — جَمْعٌ حُذِفَتْ نُونُهُ تَخْفِيفًا: الْمُقِيمِينَ.", "«those who establish» — the nūn dropped for lightness.", "«ikâme edenler» — nûnu hafiflik için düşmüş."),
  W("الصَّلَاةَ", "salat", "noun", ["maful-bihi", SH], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«the prayer» — its object.", "«namazı» — mef'ûlü."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«... göre»."),
  W("قِرَاءَةِ", "qiraa", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the reading of».", "«kıraatine»."),
  W("النَّصْبِ", "nasb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naṣb».", "«nasb».", punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "عَلَى حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and on».", "«ve ... göre».", "عَلَى"),
  W("قِرَاءَةِ", "qiraa", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the reading of».", "«kıraatine»."),
  W("الْجَرِّ", "jarr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer»."),
  W("حَذْفُهَا", "hadhf", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its dropping».", "«hazfi».", segments=[seg("حَذْفُ", "hadhf", "noun"), pr3fs()]),
  W("وَاجِبٌ", "wajib", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is obligatory».", "«vâcibdir»."),
  li_("لِلْإِضَافَةِ", "idafa", "noun", [], "الْإِضَافَةِ مَجْرُورٌ — لِلتَّعْلِيلِ.", "«for the annexation».", "«izâfetten dolayı».", "الْإِضَافَةِ", punct=".", segs=[seg("لِ", "li", "prep"), seg("لْإِضَافَةِ", "idafa", "noun")]),
 ]})

# ----------- s12 (VERBATIM): the ism mafʿūl
S.append({"id": "s12", "translation": {
 "en": "The ism mafʿūl: what is derived from a verb for the one on whom it fell.",
 "tr": "İsm-i mef'ûl: fiil kendi üzerine vâki olan zât için fiilden türetilen isimdir."},
 "tokens": [
  W("اسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", IM], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْمَفْعُولِ", "maful-noun", "noun", ["idafa-definiteness", IM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the object».", "«mef'ûl».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("اشْتُقَّ", "ishtaqqa", "verb", ["ism-mawsul", "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.", "«is derived».", "«türetilen»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("فِعْلٍ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«fiil»."),
  li_("لِمَنْ", "man", "pron", ["ism-mawsul"], "مَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«for the one on whom».", "«... olan için».", "مَنْ"),
  W("وَقَعَ", "waqaa", "verb", ["ism-mawsul", "fail", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْفِعْلُ، وَالْجُمْلَةُ صِلَةٌ.", "«fell».", "«vâki olan»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«on him» — the ʿāʾid.", "«üzerine» — âid.", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
 ]})

# ----------- s13 (RESTORED): shape and government
S.append({"id": "s13", "translation": {
 "en": "And its shape from the triliteral is on مَفْعُولٌ, as in مَضْرُوبٌ, and from what is other than it on the shape of the ism fāʿil with a fatḥa before the last, as in مُسْتَخْرَجٌ; and its government is that of its passive verb, under the ism fāʿil's conditions — as in زَيْدٌ مَضْرُوبٌ غُلَامُهُ الْآنَ أَوْ غَدًا." + R_EN,
 "tr": "Sîgası sülâsîden مَفْعُولٌ vezni üzeredir, مَضْرُوبٌ gibi; onun dışındakilerden sondan öncekinin fethasıyla ism-i fâil sîgası üzeredir, مُسْتَخْرَجٌ gibi; ameli, ism-i fâilin şartlarıyla meçhûl fiilinin amelidir — زَيْدٌ مَضْرُوبٌ غُلَامُهُ الْآنَ أَوْ غَدًا gibi." + R_TR},
 "tokens": [
  atf_wa("وَصِيغَتُهُ", "sigha", "noun", ["mubtada-khabar", "idafa-definiteness"], "صِيغَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its shape».", "«ve sîgası».", "صِيغَتُ", extra_segs=[seg("صِيغَتُ", "sigha", "noun"), pr3ms()]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the triliteral».", "«sülâsî»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ.", "«on».", "«üzere»."),
  cited("مَفْعُولٍ", "maful-object", "noun", ["huruf-jarr", IM], "مَجْرُورٌ — الْوَزْنُ.", "«mafʿūl» — the pattern.", "«mef'ûl» — vezin."),
  nahwu(),
  cited("مَضْرُوبٍ", "madrub", "noun", ["idafa-definiteness", IM], "فِي مَحَلِّ جَرٍّ.", "«struck».", "«vurulmuş».", punct="،"),
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ.", "«and from».", "«ve -den».", "مِنْ"),
  W("غَيْرِهِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what is other than it».", "«onun dışındakilerden».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«on».", "«üzere»."),
  W("صِيغَةِ", "sigha", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the shape of».", "«sîgası»."),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  bi_("بِفَتْحِ", "fath", "noun", ["idafa-definiteness"], "فَتْحِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«with a fatḥa on».", "«fethasıyla».", "فَتْحِ"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what».", "«... olanın»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«is before».", "«öncesinde»."),
  W("الْآخِرِ", "akhir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the last».", "«sonun»."),
  nahwu(),
  cited("مُسْتَخْرَجٍ", "mustakhraj", "noun", ["idafa-definiteness", IM, "form-x-verbs"], "فِي مَحَلِّ جَرٍّ — اسْمُ مَفْعُولِ اسْتَخْرَجَ.", "«extracted».", "«istihrac edilmiş».", punct="؛"),
  atf_wa("وَعَمَلُهُ", "amal-work", "noun", ["mubtada-khabar", "idafa-definiteness", SH], "عَمَلُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its government».", "«ve ameli».", "عَمَلُ", extra_segs=[seg("عَمَلُ", "amal-work", "noun"), pr3ms()]),
  W("عَمَلُ", "amal-work", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the government of».", "«amelidir»."),
  W("فِعْلِهِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its verb».", "«fiilinin».", segments=[seg("فِعْلِ", "fil", "noun"), pr3msi()]),
  W("الْمَجْهُولِ", "majhul", "noun", ["naat-sifa", IM], "صِفَةٌ مَجْرُورَةٌ.", "«passive».", "«meçhûl»."),
  bi_("بِشُرُوطِ", "shart", "noun", ["idafa-definiteness", SH], "شُرُوطِ مَجْرُورٌ، وَهُوَ مُضَافٌ — جَمْعُ شَرْطٍ.", "«under the conditions of».", "«şartlarıyla».", "شُرُوطِ"),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâilin».", punct="،"),
  nahwu(),
  ZAYD(),
  W("مَضْرُوبٌ", "madrub", "noun", ["mubtada-khabar", IM, SH], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ عَامِلٌ عَمَلَ الْمَجْهُولِ.", "«is being struck» — the passive participle governs.", "«vurulmaktadır» — ism-i mef'ûl amel eder."),
  GHULAMUHU("naib-al-fail"),
  ALAN(),
  AW(),
  GHADAN(punct="."),
 ]})

# ----------- s14 (COMMENTARY): two objects, and the lām
S.append({"id": "s14", "translation": {
 "en": "And likewise زَيْدٌ مُعْطًى غُلَامُهُ دِرْهَمًا; and with the lām it governs without condition — زَيْدٌ الْمُعْطَى غُلَامُهُ دِرْهَمًا أَمْسِ." + C_EN,
 "tr": "Yine زَيْدٌ مُعْطًى غُلَامُهُ دِرْهَمًا; lâm ile şartsız amel eder — زَيْدٌ الْمُعْطَى غُلَامُهُ دِرْهَمًا أَمْسِ." + C_TR},
 "tokens": [
  atf_wa("وَكَذَا", "kadha", "part", ["huruf-jarr"], "كَذَا: الْكَافُ حَرْفُ جَرٍّ، وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«and likewise».", "«ve yine».", "كَذَا"),
  ZAYD(),
  W("مُعْطًى", "muta", "noun", ["mubtada-khabar", IM, SH, "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمُ مَفْعُولٍ مَقْصُورٌ مِنْ أَعْطَى.", "«is given» — a maqṣūr passive participle.", "«verilmiştir» — maksûr ism-i mef'ûl."),
  GHULAMUHU("naib-al-fail"),
  DIRHAMAN("مَفْعُولٌ بِهِ ثَانٍ لِاسْمِ الْمَفْعُولِ مَنْصُوبٌ.", "«a dirham» — its second object.", "«bir dirhem» — ikinci mef'ûlü.", punct="؛"),
  atf_wa("وَمَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "مَعَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and with».", "«ve ... ile».", "مَعَ"),
  W("اللَّامِ", "lam-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the lām».", "«lâm»."),
  W("يَعْمَلُ", "amila", "verb", ["fail", SH], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«it governs».", "«amel eder»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا بِمَعْنَى غَيْرٍ مَجْرُورٌ بِالْبَاءِ.", "«without».", "«-sız».", "لَا"),
  W("شَرْطٍ", "shart", "noun", ["huruf-jarr", SH], "مَجْرُورٌ.", "«condition».", "«şart».", punct="—"),
  ZAYD(),
  W("الْمُعْطَى", "muta", "noun", ["mubtada-khabar", IM, SH, "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمُ مَفْعُولٍ مُعَرَّفٌ بِاللَّامِ.", "«the one given» — the al-participle.", "«verilen» — lâmlı ism-i mef'ûl."),
  GHULAMUHU("naib-al-fail"),
  DIRHAMAN("مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a dirham».", "«bir dirhem»."),
  AMSI(punct="."),
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
 "huduth": need("huduth", "حُدُوث", "ح د ث", "noun", "occurrence, coming-to-be — the transient sense that separates the ism fāʿil from the ṣifa mushabbaha", "hudûs, meydana gelme — ism-i fâili sıfat-ı müşebbeheden ayıran geçicilik mânâsı", 5),
 "mim-letter": need("mim-letter", "مِيم", None, "noun", "the letter mīm", "mîm harfi", 3),
 "mukhrij": need("mukhrij", "مُخْرِج", "خ ر ج", "noun", "one who brings out — the ism fāʿil of Form IV أَخْرَجَ", "çıkaran — ahrace'nin (IV) ism-i fâili", 4),
 "mustakhrij": need("mustakhrij", "مُسْتَخْرِج", "خ ر ج", "noun", "one who extracts — the ism fāʿil of Form X اِسْتَخْرَجَ", "istihrac eden — istahrece'nin (X) ism-i fâili", 4),
 "mustakhraj": need("mustakhraj", "مُسْتَخْرَج", "خ ر ج", "noun", "extracted — the ism mafʿūl of Form X اِسْتَخْرَجَ, one fatḥa from مُسْتَخْرِج", "istihrac edilmiş — istahrece'nin ism-i mef'ûlü; مُسْتَخْرِج'den bir fetha farklı", 4),
 "kisai": need("kisai", "الْكِسَائِيّ", None, "propn", "al-Kisāʾī (d. 189/805), the Kufan grammarian and reader", "Kisâî (ö. 189/805), Kûfeli nahivci ve kıraat imamı", 5),
 "muti": need("muti", "مُعْطِي", "ع ط و", "noun", "a giver — the manqūṣ ism fāʿil of أَعْطَى", "veren — a'tâ'nın mankûs ism-i fâili", 4),
 "muta": need("muta", "مُعْطًى", "ع ط و", "noun", "given — the maqṣūr ism mafʿūl of أَعْطَى (الْمُعْطَى with the article)", "verilmiş — a'tâ'nın maksûr ism-i mef'ûlü (lâm ile الْمُعْطَى)", 4),
 "darrab": need("darrab", "ضَرَّاب", "ض ر ب", "noun", "a hard hitter — the intensive on فَعَّال", "çok vuran — فَعَّال mübâlağası", 4),
 "darub": need("darub", "ضَرُوب", "ض ر ب", "noun", "a hard hitter — the intensive on فَعُول", "çok vuran — فَعُول mübâlağası", 4),
 "midrab": need("midrab", "مِضْرَاب", "ض ر ب", "noun", "a hard hitter — the intensive on مِفْعَال", "çok vuran — مِفْعَال mübâlağası", 4),
 "hadhir": need("hadhir", "حَذِر", "ح ذ ر", "noun", "ever-wary — the intensive on فَعِل", "çok sakınan — فَعِل mübâlağası", 4),
 "kadhdhab": need("kadhdhab", "كَذَّاب", "ك ذ ب", "noun", "a great liar — فَعَّال", "çok yalancı — فَعَّال", 3),
 "ghuful": need("ghuful", "غُفُل", "غ ف ل", "noun", "very heedless — the intensive on فُعُل", "çok gâfil — فُعُل mübâlağası", 5),
 "yaquz": need("yaquz", "يَقُظ", "ي ق ظ", "noun", "ever-wakeful, alert — فَعُل", "çok uyanık — فَعُل", 5),
 "midrar": need("midrar", "مِدْرَار", "د ر ر", "noun", "pouring abundantly (of rain) — مِفْعَال", "bol bol yağan — مِفْعَال", 5),
 "mikthir": need("mikthir", "مِكْثِير", "ك ث ر", "noun", "one who talks much — مِفْعِيل", "çok konuşan, geveze — مِفْعِيل", 5),
 "luana": need("luana", "لُعَنَة", "ل ع ن", "noun", "one who curses much — فُعَلَة", "çok lânet eden — فُعَلَة", 5),
 "adam": need("adam", "عَدَم", "ع د م", "noun", "absence, non-existence", "yokluk, bulunmama", 3),
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
print("kafiya ch16 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "اسْمُ الْفَاعِلِ وَاسْمُ الْمَفْعُولِ فِي الْكَافِيَةِ", "en": "The ism fāʿil and the ism mafʿūl in the Kafiya: the definitions, the shapes, the conditions of government, the past-sense annexation, the intensives, the dual and plural with the dropped nūn", "tr": "Kâfiye'de ism-i fâil ve ism-i mef'ûl: tarifler, sîgalar, amel şartları, mâzî mânâsında izâfet, mübâlağa vezinleri, nûnu düşen tesniye ve cemi"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — اسم الفاعل: ما اشتق من فعل لمن قام به بمعنى الحدوث؛ يعمل عمل فعله بشرط الحال والاستقبال والاعتماد؛ وإذا كان للماضي وجبت الإضافة؛ وإذا دخله اللام عمل مطلقا؛ أمثلة المبالغة؛ اسم المفعول: ما اشتق من فعل لمن وقع عليه", "ضياء صونغور اوغلى — دفتر الكافية: مُخْرِج ومُسْتَخْرِج؛ زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا الْآنَ أَوْ غَدًا؛ خلاف الكسائي؛ دِرْهَمًا مفعول فعل مقدر؛ جَهُول صِدِّيق كَذَّاب غُفُل يَقُظ مِدْرَار مِكْثِير لُعَنَة؛ الْمُقِيمِي الصَّلَاةَ"],
 "question": {
  "en": ["What is an ISM FĀʿIL? A noun derived from a verb for the one in whom the event subsists — in the sense of OCCURRENCE (حُدُوث), something that comes and goes: ضَارِب is striking now, not a striker by nature. That last clause is what parts it from the ṣifa mushabbaha.",
         "How is it shaped? From the bare triliteral on فَاعِل; from every augmented form, take the muḍāriʿ, replace its prefix by a mīm with ḍamma and give the letter before the last a kasra: يُخْرِجُ → مُخْرِج, يَسْتَخْرِجُ → مُسْتَخْرِج. The ism mafʿūl is the same word with a FATḤA there: مُسْتَخْرَج — and مَفْعُول from the triliteral.",
         "When does it GOVERN like its verb? Two conditions together: it must mean the present or the future, and it must lean on something — its ṣāḥib (a mubtada, a described noun, a relative, the owner of a ḥāl), a question hamza or a negation. زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا: غُلَامُهُ in rafʿ as its doer, عَمْرًا in naṣb as its object.",
         "What happens when it means the PAST? It loses its government and must be annexed to its object by a maʿnawī annexation — زَيْدٌ ضَارِبُ عَمْرٍو أَمْسِ — because a ṣifa annexed to what it does not govern is an ordinary muḍāf. Al-Kisāʾī allows the annexation instead of requiring it, and calls it lafẓī. A further object (دِرْهَمًا) is then the object of an unspoken أَعْطَاهُ.",
         "And with the article? الضَّارِبُ governs with no condition at all: مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْدًا أَمْسِ — past, and still a doer in rafʿ and an object in naṣb. The lām stands for a relative الَّذِي, and a relative's verb has no tense restriction.",
         "What are the INTENSIVES? ضَرَّاب، ضَرُوب، مِضْرَاب، عَلِيم، حَذِر — فَعَّال، فَعُول، مِفْعَال، فَعِيل، فَعِل — and the notebook adds فِعِّيل (صِدِّيق), فُعُل (غُفُل), فَعُل (يَقُظ), مِفْعِيل (مِكْثِير), فُعَلَة (لُعَنَة). They govern exactly as the ism fāʿil does, under the same conditions, as do its dual and plural; the al-plural may drop its nūn for lightness — الْمُقِيمِي الصَّلَاةَ in the naṣb reading.",
         "What does the engine do? The IsmTagger reads مُسْتَخْرِج and مُسْتَخْرَج back to their scales and the kernel marks the one-vowel difference; the TaalluqEngine's VERBAL_WAZN list is this chapter — a noun on فَاعِل or مُفْعِل may take a doer and an object, which is why عَامِل governs in the corpus."],
  "tr": ["İSM-İ FÂİL nedir? Hades kendisiyle kâim olan zât için fiilden türetilen isim — HUDÛS mânâsında, gelip geçici bir şey: ضَارِب şu an vuran biridir, tabiatıyla vurucu değil. Bu son kayıt onu sıfat-ı müşebbeheden ayırır.",
         "Sîgası nasıldır? Sülâsî mücerredden فَاعِل; her mezîd bâbdan muzâri alınır, ön eki mazmûm bir mîm yapılır ve sondan önceki harf kesre alır: يُخْرِجُ → مُخْرِج, يَسْتَخْرِجُ → مُسْتَخْرِج. İsm-i mef'ûl aynı kelimenin oraya FETHA almış hâlidir: مُسْتَخْرَج — sülâsîden ise مَفْعُول.",
         "Ne zaman fiili gibi AMEL EDER? İki şart birlikte: hâl veya istikbâl mânâsında olmalı ve bir şeye dayanmalı — sâhibine (mübtedâ, mevsûf, mevsûl, zü'l-hâl), istifhâm hemzesine ya da nefy harfine. زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا: غُلَامُهُ fâili olarak merfû, عَمْرًا mef'ûlü olarak mansûb.",
         "MÂZÎ mânâsında ne olur? Amelini kaybeder ve mef'ûlüne izâfet-i ma'neviyye ile muzâf olması gerekir — زَيْدٌ ضَارِبُ عَمْرٍو أَمْسِ — çünkü yönetmediği şeye muzâf bir sıfat sıradan bir muzâftır. Kisâî izâfeti vâcib değil câiz sayar ve lafzî der. Fazladan bir mef'ûl (دِرْهَمًا) o zaman söylenmemiş bir أَعْطَاهُ'nun mef'ûlüdür.",
         "Ya lâm ile? الضَّارِبُ hiçbir şartsız amel eder: مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْدًا أَمْسِ — mâzî, ama yine merfû bir fâil ve mansûb bir mef'ûl. Lâm bir الَّذِي mevsûlü yerindedir ve mevsûlün fiilinde zaman kaydı yoktur.",
         "MÜBÂLAĞA vezinleri nelerdir? ضَرَّاب، ضَرُوب، مِضْرَاب، عَلِيم، حَذِر — فَعَّال، فَعُول، مِفْعَال، فَعِيل، فَعِل — defter فِعِّيل (صِدِّيق), فُعُل (غُفُل), فَعُل (يَقُظ), مِفْعِيل (مِكْثِير), فُعَلَة (لُعَنَة) ekler. Aynı şartlarla tıpkı ism-i fâil gibi amel ederler; tesniyesi ve cemi de öyle; lâmlı cemi hafiflik için nûnunu düşürebilir — nasb kıraatinde الْمُقِيمِي الصَّلَاةَ.",
         "Motor ne yapar? IsmTagger مُسْتَخْرِج ile مُسْتَخْرَج'i vezinlerine geri okur ve çekirdek tek hareke farkını işaretler; TaalluqEngine'in VERBAL_WAZN listesi bu bâbdır — فَاعِل veya مُفْعِل veznindeki bir isim fâil ve mef'ûl alabilir; عَامِل'in külliyatta amel etmesinin sebebi budur."]},
 "plain": {
  "en": "The ism fāʿil (ضَارِب «striking») and the ism mafʿūl (مَضْرُوب «struck») are nouns made from verbs. They can act like their verb — take a doer and an object — only when they mean «now or later» and lean on a subject, a question or a negation; with the article they always can. Past-sense ones annex their object instead.",
  "tr": "İsm-i fâil (ضَارِب «vuran») ve ism-i mef'ûl (مَضْرُوب «vurulan») fiilden yapılan isimlerdir. Yalnız «şimdi veya sonra» anlamında olup bir özneye, soruya ya da olumsuzluğa dayandıklarında fiil gibi davranır — fâil ve mef'ûl alırlar; lâm ile her zaman alırlar. Mâzî anlamlı olanlar mef'ûlünü izâfetle alır."},
 "explanation": {
  "en": "The two participles are defined in parallel: the ism fāʿil for the one in whom the event subsists, the ism mafʿūl for the one on whom it falls — and the first definition carries one extra word, حُدُوث, which the next chapter will turn against the ṣifa mushabbaha. The shapes are a single rule each: فَاعِل and مَفْعُول for the bare verb, and for every augmented form the muḍāriʿ with its prefix turned into a mīm of ḍamma, kasra before the last letter for the active and fatḥa for the passive, so that مُسْتَخْرِج and مُسْتَخْرَج differ by one vowel and nothing else. The chapter's weight is on government. A participle governs as its verb does only when it means the present or the future and leans on something that lets it predicate — its ṣāḥib, a question hamza, a negation. The notebook's model sentence carries all of it: زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا الْآنَ أَوْ غَدًا. Take away the time condition and the government goes with it: for the past the participle is annexed to its object by an ordinary maʿnawī annexation, because a ṣifa that does not govern the word it is annexed to is just a muḍāf — this is why the notebook pauses on the Kisāʾī dissent, which keeps the annexation lafẓī and optional, and on دِرْهَمًا, which no past-sense participle can take and which therefore belongs to an unspoken أَعْطَاهُ. The article changes everything: الضَّارِب stands for الَّذِي ضَرَبَ, a relative clause, and governs in every tense without a condition. The intensives, the dual and the plural follow the singular in all of this; the dropped nūn of الْمُقِيمِي الصَّلَاةَ is the only extra licence, and the notebook is careful to tie it to the naṣb reading — in the jarr reading the nūn is gone for a different reason, the annexation, and its absence is then obligatory. The ism mafʿūl closes the chapter by mirroring every rule with the passive verb's government, its object's seat now filled by a deputy doer.",
  "tr": "İki ism paralel tarif edilir: ism-i fâil hadesin kendisiyle kâim olduğu zât için, ism-i mef'ûl üzerine vâki olduğu zât için — ve ilk tarif bir fazla kelime taşır, حُدُوث; sonraki bâb onu sıfat-ı müşebbeheye karşı kullanacaktır. Sîgalar birer kuraldır: mücerred fiil için فَاعِل ve مَفْعُول; her mezîd bâb için ön eki mazmûm mîm olmuş muzâri, ma'lûm için sondan önce kesre, meçhûl için fetha — öyle ki مُسْتَخْرِج ile مُسْتَخْرَج tek harekeyle ayrılır, başka hiçbir şeyle değil. Bâbın ağırlığı ameldedir. Bir ism yalnız hâl ya da istikbâl mânâsında olup yüklem olmasını sağlayan bir şeye dayandığında — sâhibine, istifhâm hemzesine, nefye — fiili gibi amel eder. Defterin örnek cümlesi hepsini taşır: زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا الْآنَ أَوْ غَدًا. Zaman şartını kaldırın, amel de gider: mâzî için ism, mef'ûlüne sıradan bir izâfet-i ma'neviyye ile muzâf olur; çünkü muzâf olduğu kelimeyi yönetmeyen sıfat yalnızca bir muzâftır — defterin izâfeti lafzî ve ihtiyârî tutan Kisâî muhâlefetinde ve hiçbir mâzî mânâlı ismin alamayacağı, dolayısıyla söylenmemiş bir أَعْطَاهُ'ya ait olan دِرْهَمًا'da durmasının sebebi budur. Lâm her şeyi değiştirir: الضَّارِب bir sıla cümlesi olan الَّذِي ضَرَبَ yerindedir ve her zamanda şartsız amel eder. Mübâlağa vezinleri, tesniye ve cemi bunların hepsinde müfrede uyar; الْمُقِيمِي الصَّلَاةَ'nin düşen nûnu tek fazla ruhsattır ve defter onu nasb kıraatine bağlamaya özen gösterir — cer kıraatinde nûn başka bir sebeple, izâfetten gitmiştir ve yokluğu o zaman vâcibdir. İsm-i mef'ûl her kuralı meçhûl fiilin ameliyle aynalayarak bâbı kapatır; mef'ûlünün yerini artık nâib-i fâil doldurur."},
 "examples": [
  {"ar": "اسْمُ الْفَاعِلِ: مَا اشْتُقَّ مِنْ فِعْلٍ لِمَنْ قَامَ بِهِ بِمَعْنَى الْحُدُوثِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "مُخْرِجٌ وَمُسْتَخْرِجٌ", "en": "The augmented shape.", "tr": "Mezîd sîga.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا الْآنَ أَوْ غَدًا", "en": "Government under the conditions.", "tr": "Şartlarla amel.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "زَيْدٌ ضَارِبُ عَمْرٍو أَمْسِ", "en": "The past sense: annexation.", "tr": "Mâzî mânâsı: izâfet.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْدًا أَمْسِ", "en": "The article lifts every condition.", "tr": "Lâm her şartı kaldırır.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "ضَرَّابٌ وَضَرُوبٌ وَمِضْرَابٌ وَعَلِيمٌ وَحَذِرٌ", "en": "The intensives.", "tr": "Mübâlağa vezinleri.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "الْمُقِيمِي الصَّلَاةَ", "en": "The nūn dropped for lightness.", "tr": "Hafiflik için düşen nûn.", "sourceStory": "al-kafiya", "sentence": "s11"},
  {"ar": "زَيْدٌ مَضْرُوبٌ غُلَامُهُ الْآنَ أَوْ غَدًا", "en": "The ism mafʿūl governing.", "tr": "İsm-i mef'ûlün ameli.", "sourceStory": "al-kafiya", "sentence": "s13"}],
 "commonMistakes": [
  {"wrong": "«زَيْدٌ ضَارِبٌ عَمْرًا أَمْسِ»",
   "right": "«زَيْدٌ ضَارِبُ عَمْرٍو أَمْسِ — mâzî mânâlı ism-i fâil amel etmez, mef'ûlüne muzâf olur»",
   "why": {"en": "The present-or-future condition has lapsed; only the article could restore the government.", "tr": "Hâl-istikbâl şartı düşmüştür; ameli yalnız lâm geri getirebilir."}},
  {"wrong": "«مُسْتَخْرِجٌ — istihrac edilmiş»",
   "right": "«مُسْتَخْرِجٌ istihrac EDEN; مُسْتَخْرَجٌ istihrac EDİLMİŞ — kesre fâil, fetha mef'ûl»",
   "why": {"en": "In every augmented form the two participles differ only by the vowel before the last letter.", "tr": "Her mezîd bâbda iki ism yalnız sondan önceki harekeyle ayrılır."}},
  {"wrong": "«ضَارِبٌ cümle başında tek başına amel eder: ضَارِبٌ زَيْدٌ عَمْرًا»",
   "right": "«أَضَارِبٌ زَيْدٌ عَمْرًا؟ / مَا ضَارِبٌ زَيْدٌ عَمْرًا — hemze veya nefye dayanmalı»",
   "why": {"en": "Reliance (iʿtimād) is a condition: a bare participle at the head of a sentence governs nothing.", "tr": "İ'timâd şarttır: cümle başında çıplak bir ism-i fâil hiçbir şeyi yönetmez."}},
  {"wrong": "«الْمُقِيمِي الصَّلَاةِ — nûn hafiflik için düşmüş»",
   "right": "«cer kıraatinde nûn izâfetten dolayı VÂCİBEN düşer; hafiflik ruhsatı nasb kıraatine aittir»",
   "why": {"en": "Two readings, two reasons for one missing nūn; the notebook keeps them apart.", "tr": "İki kıraat, bir eksik nûn için iki sebep; defter ikisini ayrı tutar."}}],
 "relatedNotes": [IF, IM, SH, MB, "idafa-lafziyya", "al-masdar-fil-kafiya", "sifa-mushabbaha"]}

ADD_EN = (" Chapter 16 (notebook lines ~258-261): the ism fāʿil and the ism mafʿūl defined in the notebook's own Arabic (s1, s12); the shapes, the conditions of government, the past-sense annexation, the al-participle, "
          "the intensives, the dual and plural and the dropped nūn restored from the received matn and marked (s2-s4, s7-s8, s10-s11, s13); al-Kisāʾī's dissent, the supplied verb behind دِرْهَمًا, the notebook's eight intensives and the ism mafʿūl's two objects as commentary (s5-s6, s9, s14).")
ADD_TR = (" On altıncı bâb (defter satırları ~258-261): ism-i fâil ve ism-i mef'ûl defterin kendi Arapçasıyla tarif edilir (s1, s12); sîgalar, amel şartları, mâzî mânâsında izâfet, lâmlı ism, mübâlağa vezinleri, "
          "tesniye-cemi ve düşen nûn alınan metinden geri yazılmış ve işaretlenmiştir (s2-s4, s7-s8, s10-s11, s13); Kisâî'nin muhâlefeti, دِرْهَمًا'nın ardındaki takdîrî fiil, defterin sekiz mübâlağa örneği ve ism-i mef'ûlün iki mef'ûlü şerh olarak (s5-s6, s9, s14).")
write_out(16, S, TITLE, ADD_EN, ADD_TR, "258-261", GLOSS_ADD, notes=(NOTE,),
          related=((IF, [K]), (IM, [K]), (SH, [K]), (MB, [K])))
report(16, S, GLOSS_ADD, (NOTE,))
