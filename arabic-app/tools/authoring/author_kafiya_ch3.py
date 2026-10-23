# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 3: the MABNI and the MUDMAR. The mabni's definition, its ruling, its four names (damm, fath, kasr, waqf) with
the notebook's examples, the eight kinds of mabni; the pronoun's definition (for a speaker, an addressee or an absent one whose mention
preceded in wording, in sense or in ruling), attached and detached, its three cases and five kinds with the notebook's forms, the
concealed marfu' in the madi's third persons, the mudari's speakers / single addressee / third persons and in the sifat, and the rule
that the detached is not used while the attached is possible.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~157-164 of the transcription.

  RESTORED (the notebook carries this ruling only in Turkish; the received matn of the Kafiya is written and marked): s2, s4, s5, s8, s9, s11, s12, s13.
  COMMENTARY (the teacher's worked examples, not the matn): s3, s7, s10 — marked C_EN/C_TR.
  DRY_PKG=<copy of content/samples/al-kafiya> DRY_GR=<copy of content/grammar> python3 tools/authoring/author_kafiya_ch3.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-mabni-wal-mudmar"
K2 = "al-murab-wal-mabni-wal-irab"
PRON = "al-marifa-al-mudmarat-wal-alam"
TITLE = {"ar": "الْمَبْنِيُّ وَالْمُضْمَرُ", "en": "The indeclinable, and the pronoun", "tr": "Mebnî ve muzmar"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"
B8 = "الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ"; W8 = "اِفْتَعَلَ يَفْتَعِلُ"

def N(s): return unicodedata.normalize("NFC", s)
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr1sy(): return seg("ي", "pron-1s", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def wa(form, lex, pos): return [seg("وَ", "wa", "conj"), seg(form, lex, pos)]
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)

# ----------- s1 (matn, vowelled in the notebook)
S.append({"id": "s1", "translation": {
 "en": "The indeclinable: what resembles the indeclinable-by-origin, or stands outside a construction.",
 "tr": "Mebnî: aslen mebnî olana benzeyen ya da terkib dışında vâki olandır."},
 "tokens": [
  W("الْمَبْنِيُّ", "mabni", "noun", ["mubtada-khabar", "ism-maful"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولِ بَنَى.", "«the indeclinable» — the mubtada.", "«mebnî» — mübtedâ."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.", "«that which» — the relative, the khabar in the place of rafʿ.", "«... olan» — ism-i mevsûl, mahallen merfû haber."),
  W("نَاسَبَ", "nasaba", "verb", ["ism-mawsul", "form-iii-verbs", "fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هُوَ يَعُودُ عَلَى مَا، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.", "«resembled» — the ṣila's verb, its doer concealed, returning to مَا.", "«benzedi» — sıla fiili, fâili gizli, mâ'ya râci."),
  W("مَبْنِيَّ", "mabni", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the indeclinable» — the object, annexed.", "«mebnîsine» — mef'ûlün bih, muzâf."),
  W("الْأَصْلِ", "asl", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — مَبْنِيُّ الْأَصْلِ: الْحَرْفُ وَالْمَاضِي وَالْأَمْرُ.", "«of the origin» — the muḍāf ilayh: the particle, the past verb and the imperative are indeclinable by origin.", "«aslın» — muzâfun ileyh: harf, mâzî ve emir aslen mebnîdir."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("وَقَعَ", "waqaa", "verb", ["atf-nasaq", "fail"], "فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى نَاسَبَ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.", "«stood» — joined to نَاسَبَ, its doer concealed.", "«vâki oldu» — nâsebe'ye atıf, fâili gizli."),
  W("غَيْرَ", "ghayr", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«not» — the ḥāl («in a state of not being compounded»), annexed.", "«olmayarak» — hâl, muzâf."),
  W("مُرَكَّبٍ", "murakkab", "noun", ["idafa-definiteness", "ism-maful", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولِ رَكَّبَ.", "«compounded» — the muḍāf ilayh.", "«mürekkeb» — muzâfun ileyh.", punct="."),
 ]})

# ----------- s2 (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And its ruling is that its ending does not differ with the differing of the governors." + R_EN,
 "tr": "Hükmü, sonunun âmillerin değişmesiyle değişmemesidir." + R_TR},
 "tokens": [
  W("وَحُكْمُهُ", "hukm", "noun", ["mubtada-khabar", "idafa-definiteness"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَحُكْمُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its ruling» — the mubtada with its annexed pronoun.", "«ve hükmü» — mübtedâ, zamiri muzâfun ileyh.", segments=[seg("وَ", "wa", "conj"), seg("حُكْمُ", "hukm", "noun"), pr3ms()]),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ، وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْمُبْتَدَإِ.", "«that» — the maṣdar particle; its clause is the khabar.", "«-ması» — masdariyye; cümlesi haberdir."),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«-me-»."),
  W("يَخْتَلِفَ", "ikhtalafa", "verb", ["an-masdariyya", "form-viii-verbs", "fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«differ» — the muḍāriʿ in naṣb after أَنْ.", "«değiş-» — en ile mansûb muzâri."),
  W("آخِرُهُ", "akhir", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end» — the doer.", "«sonu» — fâil.", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  W("بِاخْتِلَافِ", "ikhtilaf", "noun", ["huruf-jarr", "idafa-definiteness", "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَاخْتِلَافِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«with the differing» — the jarr phrase; the maṣdar annexed.", "«değişmesiyle» — cer, masdar muzâf.", segments=[seg("بِ", "bi", "prep"), seg("اخْتِلَافِ", "ikhtilaf", "noun")]),
  W("الْعَوَامِلِ", "awamil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ عَامِلٍ.", "«of the governors» — the muḍāf ilayh.", "«âmillerin» — muzâfun ileyh.", punct="."),
 ]})

# ----------- s3 (COMMENTARY: the teacher's triplet)
S.append({"id": "s3", "translation": {
 "en": "For instance: this one came to me, and I saw this one, and I passed by this one." + C_EN,
 "tr": "Meselâ: bu bana geldi, bunu gördüm, buna uğradım." + C_TR},
 "tokens": [
  nahwu(),
  W("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "ya-al-mutakallim", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me» — the verb, the wiqāya nūn, the yāʾ its object.", "«bana geldi» — fiil, vikâye nûnu, yâ mef'ûl.", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  W("هٰذَا", "hadha", "pron", ["asma-al-ishara", "fail"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this one» — the demonstrative, mabnī, the doer in the place of rafʿ.", "«bu» — ism-i işaret, mahallen merfû fâil.", punct="،"),
  W("وَرَأَيْتُ", "raa", "verb", ["atf-nasaq", "fail", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَأَى فِعْلٌ مَاضٍ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«and I saw» — the verb with the speaker's tāʾ as doer.", "«ve gördüm» — fiil, tâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْ", "raa", "verb"), prT()]),
  W("هٰذَا", "hadha", "pron", ["asma-al-ishara", "maful-bihi"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this one» — the object in the place of naṣb: the ending has not moved.", "«bunu» — mahallen mansûb mef'ûl: sonu değişmedi.", punct="،"),
  W("وَمَرَرْتُ", "marra", "verb", ["atf-nasaq", "fail", "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمَرَّ فِعْلٌ مَاضٍ مُضَاعَفٌ فُكَّ إِدْغَامُهُ، وَالتَّاءُ فَاعِلٌ.", "«and I passed» — the doubled verb with the speaker's tāʾ.", "«ve uğradım» — muzâaf fiil, tâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("مَرَرْ", "marra", "verb"), prT()]),
  W("بِهٰذَا", "hadha", "pron", ["asma-al-ishara", "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«by this one» — the demonstrative in the place of jarr: one form in three seats.", "«buna» — mahallen mecrûr: üç yerde tek şekil.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
 ]})

# ----------- s4 (RESTORED, the notebook's examples)
S.append({"id": "s4", "translation": {
 "en": "And its names: the ḍamm, as in «O Zayd»; the fatḥ, as in «no one»; the kasr, as in «yesterday»; and the waqf, as in «help!»." + R_EN,
 "tr": "Lakapları: damm — «yâ Zeyd» gibi; feth — «lâ ehade» gibi; kesr — «emsi» gibi; vakf — «unsur» gibi." + R_TR},
 "tokens": [
  W("وَأَلْقَابُهُ", "laqab", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَأَلْقَابُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ لَقَبٍ.", "«and its names» — the mubtada.", "«ve lakapları» — mübtedâ.", punct=":", segments=[seg("وَ", "wa", "conj"), seg("أَلْقَابُ", "laqab", "noun"), pr3ms()]),
  W("الضَّمُّ", "damm", "noun", ["mubtada-khabar"], "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ.", "«the ḍamm» — the khabar.", "«damm» — haber."),
  nahwu(punct=None),
  W("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  W("زَيْدُ", "zayd", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Zayd» — the single proper-name munādā, built on the ḍamm.", "«Zeyd» — damm üzere mebnî münâdâ.", punct="،"),
  atf_wa("وَالْفَتْحُ", "fath", "noun", ["mubtada-khabar"], "الْفَتْحُ مَعْطُوفٌ عَلَى الضَّمِّ مَرْفُوعٌ.", "«and the fatḥ».", "«ve feth».", "الْفَتْحُ"),
  nahwu(punct=None),
  W("لَا", "la", "part", ["la-nafiya-lil-jins"], "لَا النَّافِيَةُ لِلْجِنْسِ، حَرْفٌ يَعْمَلُ عَمَلَ إِنَّ.", "«no» — the genus-denying لَا.", "«hiç ... yok» — cins nefyi lâ'sı."),
  W("أَحَدَ", "ahad", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ.", "«one» — the ism of لَا, built on the fatḥ; its khabar dropped.", "«kimse» — lâ'nın ismi, feth üzere mebnî.", punct="،"),
  atf_wa("وَالْكَسْرُ", "kasr", "noun", ["mubtada-khabar"], "الْكَسْرُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the kasr».", "«ve kesr».", "الْكَسْرُ"),
  nahwu(punct=None),
  W("أَمْسِ", "amsi", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ.", "«yesterday» — the time adverb, built on the kasr.", "«dün» — kesr üzere mebnî zarf.", punct="،"),
  atf_wa("وَالْوَقْفُ", "waqf", "noun", ["mubtada-khabar"], "الْوَقْفُ مَعْطُوفٌ مَرْفُوعٌ — الْوَقْفُ هُنَا السُّكُونُ.", "«and the waqf» — the sukūn.", "«ve vakf» — sükûn.", "الْوَقْفُ"),
  nahwu(punct=None),
  W("اُنْصُرْ", "nasara", "verb", ["imperative-amr"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ أَنْتَ.", "«help!» — the imperative, built on the sukūn.", "«yardım et!» — sükûn üzere mebnî emir.", punct="."),
 ]})

# ----------- s5 (RESTORED list)
S.append({"id": "s5", "translation": {
 "en": "And the indeclinables: the pronouns, the demonstratives, the relatives, the compounds, the allusive nouns, the verb-nouns, the sound-words, and some of the adverbs." + R_EN,
 "tr": "Mebnîler: zamirler, işaret isimleri, mevsûller, mürekkebler, kinâyeler, isim-fiiller, savtlar ve bazı zarflardır." + R_TR},
 "tokens": [
  W("وَالْمَبْنِيَّاتُ", "mabni", "noun", ["mubtada-khabar", "jam-muannath-salim"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمَبْنِيَّاتُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and the indeclinables» — the mubtada.", "«ve mebnîler» — mübtedâ.", punct=":", segments=[seg("وَ", "wa", "conj"), seg("الْمَبْنِيَّاتُ", "mabni", "noun")]),
  W("الْمُضْمَرَاتُ", "mudmar", "noun", ["mubtada-khabar", "jam-muannath-salim"], "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ.", "«the pronouns» — the khabar.", "«zamirler» — haber.", punct="،"),
  atf_wa("وَأَسْمَاءُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "أَسْمَاءُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the nouns of» — joined, annexed.", "«ve isimleri» — matuf, muzâf.", "أَسْمَاءُ"),
  W("الْإِشَارَةِ", "ishara", "noun", ["idafa-definiteness", "asma-al-ishara"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«pointing» — the muḍāf ilayh: the demonstratives.", "«işaret» — muzâfun ileyh.", punct="،"),
  atf_wa("وَالْمَوْصُولَاتُ", "mawsul", "noun", ["mubtada-khabar", "ism-mawsul", "jam-muannath-salim"], "الْمَوْصُولَاتُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the relatives».", "«ve mevsûller».", "الْمَوْصُولَاتُ", punct="،"),
  atf_wa("وَالْمُرَكَّبَاتُ", "murakkab", "noun", ["mubtada-khabar", "jam-muannath-salim"], "الْمُرَكَّبَاتُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the compounds».", "«ve mürekkebler».", "الْمُرَكَّبَاتُ", punct="،"),
  atf_wa("وَالْكِنَايَاتُ", "kinaya", "noun", ["mubtada-khabar", "jam-muannath-salim"], "الْكِنَايَاتُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the allusive nouns» (كَمْ، كَذَا، كَيْتَ).", "«ve kinâyeler» (kem, kezâ, keyte).", "الْكِنَايَاتُ", punct="،"),
  atf_wa("وَأَسْمَاءُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "أَسْمَاءُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the nouns of».", "«ve isimleri».", "أَسْمَاءُ"),
  W("الْأَفْعَالِ", "fil", "noun", ["idafa-definiteness", "ism-fil", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَسْمَاءُ الْأَفْعَالِ: رُوَيْدَ وَهَيْهَاتَ.", "«verbs» — the verb-nouns: رُوَيْدَ، هَيْهَاتَ.", "«fiillerin» — isim-fiiller.", punct="،"),
  atf_wa("وَالْأَصْوَاتُ", "sawt", "noun", ["mubtada-khabar", "jam-taksir"], "الْأَصْوَاتُ مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ صَوْتٍ: غَاقِ وَنَخِّ.", "«and the sound-words» (غَاقِ، نَخِّ).", "«ve savtlar» (gâk, nahh).", "الْأَصْوَاتُ", punct="،"),
  atf_wa("وَبَعْضُ", "bad", "noun", ["mubtada-khabar", "idafa-definiteness"], "بَعْضُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and some of».", "«ve bazısı».", "بَعْضُ"),
  W("الظُّرُوفِ", "zarf", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ ظَرْفٍ: إِذْ وَحَيْثُ وَقَبْلُ.", "«the adverbs» (إِذْ، حَيْثُ، قَبْلُ).", "«zarfların» (iz, haysü, kablü).", punct="."),
 ]})

# ----------- s6 (matn, vowelled in the notebook)
S.append({"id": "s6", "translation": {
 "en": "The pronoun: what is coined for a speaker, or an addressee, or an absent one whose mention preceded — in wording, or in sense, or in ruling.",
 "tr": "Muzmar: mütekellim, muhâtab ya da zikri lafzen, manen veya hükmen geçmiş bir gâib için vaz edilen isimdir."},
 "tokens": [
  W("الْمُضْمَرُ", "mudmar", "noun", ["mubtada-khabar", "ism-maful", "form-iv-verbs"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولِ أَضْمَرَ.", "«the pronoun» — the mubtada.", "«muzmar» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the relative, the khabar.", "«... olan» — mevsûl, haber."),
  W("وُضِعَ", "wadaa", "verb", ["naib-al-fail", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ عَلَى مَا، وَالْجُمْلَةُ صِلَةٌ.", "«was coined» — the passive; its deputy concealed, returning to مَا.", "«vaz olundu» — meçhul; nâib-i fâil gizli, mâ'ya râci."),
  W("لِمُتَكَلِّمٍ", "mutakallim", "noun", ["huruf-jarr", "ism-fail"], "اللَّامُ حَرْفُ جَرٍّ، وَمُتَكَلِّمٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«for a speaker».", "«mütekellim için».", segments=[seg("لِ", "li", "prep"), seg("مُتَكَلِّمٍ", "mutakallim", "noun")]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُخَاطَبٍ", "mukhatab", "noun", ["atf-nasaq", "ism-maful"], "مَعْطُوفٌ عَلَى مُتَكَلِّمٍ مَجْرُورٌ.", "«an addressee».", "«muhâtab»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("غَائِبٍ", "ghaib", "noun", ["atf-nasaq", "ism-fail", "naat-sifa"], "مَعْطُوفٌ مَجْرُورٌ، وَجُمْلَةُ تَقَدَّمَ ذِكْرُهُ صِفَةٌ لَهُ.", "«an absent one» — described by the clause after it.", "«gâib» — sonraki cümle sıfatıdır."),
  W("تَقَدَّمَ", "taqaddama", "verb", ["jumla-sifa", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِغَائِبٍ.", "«preceded» — the ṣifa clause's verb.", "«geçmiş» — sıfat cümlesinin fiili."),
  W("ذِكْرُهُ", "dhikr", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ تَعُودُ عَلَى غَائِبٍ.", "«its mention» — the doer; the pronoun returns to the absent one.", "«zikri» — fâil; zamir gâibe râci.", segments=[seg("ذِكْرُ", "dhikr", "noun"), pr3ms()]),
  W("لَفْظًا", "lafz", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«in wording» — the tamyīz.", "«lafzen» — temyîz."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَعْنًى", "mana", "noun", ["atf-nasaq", "ism-maqsur-manqus"], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَقْصُورٌ.", "«in sense» — a maqṣūr, its fatḥa estimated.", "«manen» — maksûr, fethası takdîrî."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("حُكْمًا", "hukm", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«in ruling».", "«hükmen».", punct="."),
 ]})

# ----------- s7 (COMMENTARY: the three mentions)
S.append({"id": "s7", "translation": {
 "en": "For instance: «Zayd beat his slave» — mentioned in wording; and «Be just: it is nearer to piety» — mentioned in sense, the pronoun returning to the justice understood from «be just»; and the pronoun of the matter — mentioned in ruling." + C_EN,
 "tr": "Meselâ: «Zeyd kölesini dövdü» — lafzen zikri geçen; «Âdil olun, o takvâya daha yakındır» — manen zikri geçen, zamir «âdil olun»dan anlaşılan adle râci; şan zamiri — hükmen zikri geçen." + C_TR},
 "tokens": [
  nahwu(),
  W("ضَرَبَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«beat».", "«dövdü»."),
  W("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the doer.", "«Zeyd» — fâil."),
  W("غُلَامَهُ", "ghulam", "noun", ["maful-bihi", "idafa-definiteness", PRON], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَجْرُورٌ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى زَيْدٍ الْمَذْكُورِ لَفْظًا.", "«his slave» — the object; its pronoun returns to Zayd, mentioned in wording.", "«kölesini» — mef'ûl; zamiri lafzen zikri geçen Zeyd'e râci.", punct="،", segments=[seg("غُلَامَ", "ghulam", "noun"), pr3ms()]),
  W("وَاعْدِلُوا", "adala", "verb", ["imperative-amr", "fail", "al-iqtibas-wal-tadmin"], "الْوَاوُ عَاطِفَةٌ، وَاعْدِلُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فَاعِلٌ.", "«and: be just» — the imperative, its wāw the doer (al-Māʾida 5:8).", "«ve: âdil olun» — emir, vâv fâil (Mâide 5:8).", segments=[seg("وَ", "wa", "conj"), seg("اعْدِلُوا", "adala", "verb")]),
  W("هُوَ", "huwa", "pron", ["mubtada-khabar", PRON], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، يَعُودُ عَلَى الْعَدْلِ الْمَفْهُومِ مِنِ اعْدِلُوا — مَذْكُورٌ مَعْنًى.", "«it» — the mubtada, returning to the justice understood from the verb: mentioned in sense.", "«o» — mübtedâ, fiilden anlaşılan adle râci: manen zikri geçen."),
  W("أَقْرَبُ", "aqrab", "noun", ["mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — أَفْعَلُ تَفْضِيلٍ.", "«nearer» — the khabar.", "«daha yakın» — haber."),
  W("لِلتَّقْوَى", "taqwa", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "اللَّامُ حَرْفُ جَرٍّ، وَالتَّقْوَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«to piety» — the maqṣūr in jarr.", "«takvâya» — maksûr, mecrûr.", punct="،", segments=[seg("لِ", "li", "prep"), seg("التَّقْوَى", "taqwa", "noun")]),
  atf_wa("وَضَمِيرُ", "damir", "noun", ["mubtada-khabar", "idafa-definiteness"], "ضَمِيرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the pronoun of» — a new mubtada, annexed.", "«ve zamiri» — mübtedâ, muzâf.", "ضَمِيرُ"),
  W("الشَّأْنِ", "shan", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the matter» — the muḍāf ilayh.", "«şânın» — muzâfun ileyh."),
  W("مَذْكُورٌ", "madhkur", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«is mentioned» — the khabar.", "«zikredilmiştir» — haber."),
  W("حُكْمًا", "hukm", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — إِذْ تُفَسِّرُهُ الْجُمْلَةُ بَعْدَهُ.", "«in ruling» — the clause after it explains it.", "«hükmen» — sonraki cümle onu açıklar.", punct="."),
 ]})

# ----------- s8 (RESTORED)
S.append({"id": "s8", "translation": {
 "en": "And it is attached and detached: the attached is what does not stand by itself, like the tāʾ and the kāf in «I beat you»; and the detached is what stands by itself, like «I» and «me»." + R_EN,
 "tr": "O, muttasıl ve munfasıldır: muttasıl kendi başına durmayandır, «darabtüke»deki tâ ve kâf gibi; munfasıl kendi başına durandır, «ene» ve «iyyâye» gibi." + R_TR},
 "tokens": [
  W("وَهُوَ", "huwa", "pron", ["mubtada-khabar", PRON], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  W("مُتَّصِلٌ", "muttasil", "noun", ["mubtada-khabar", "ism-fail", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«attached» — the khabar.", "«muttasıl» — haber."),
  atf_wa("وَمُنْفَصِلٌ", "munfasil", "noun", ["mubtada-khabar", "ism-fail", "form-vii-verbs"], "مُنْفَصِلٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and detached».", "«ve munfasıl».", "مُنْفَصِلٌ", punct=":"),
  W("فَالْمُتَّصِلُ", "muttasil", "noun", ["mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمُتَّصِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the attached» — the mubtada.", "«muttasıl» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الْمُتَّصِلُ", "muttasil", "noun")]),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the relative, the khabar.", "«... olan» — mevsûl, haber."),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«-me-»."),
  W("يَسْتَقِلُّ", "istaqalla", "verb", ["ism-mawsul", "form-x-verbs", "doubled-verbs", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى مَا، وَالْجُمْلَةُ صِلَةٌ.", "«stands» — the ṣila's verb.", "«müstakil olur» — sıla fiili."),
  W("بِنَفْسِهِ", "nafs", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَفْسِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«by itself».", "«kendi başına».", segments=[seg("بِ", "bi", "prep"), seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  nahwu(punct=None),
  W("التَّاءِ", "ta-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the tāʾ».", "«tâ»."),
  atf_wa("وَالْكَافِ", "kaf-letter", "noun", ["idafa-definiteness"], "الْكَافِ مَعْطُوفٌ مَجْرُورٌ.", "«and the kāf».", "«ve kâf».", "الْكَافِ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("ضَرَبْتُكَ", "daraba", "verb", ["huruf-jarr", "fail", "maful-bihi", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ: ضَرَبَ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — كِلَاهُمَا مُتَّصِلٌ.", "«I beat you» — cited: the tāʾ its doer, the kāf its object, both attached.", "«seni dövdüm» — hikâye: tâ fâil, kâf mef'ûl, ikisi de muttasıl.", punct="،", segments=[seg("ضَرَبْ", "daraba", "verb"), prT(), pr2ms()]),
  atf_wa("وَالْمُنْفَصِلُ", "munfasil", "noun", ["mubtada-khabar"], "الْمُنْفَصِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the detached» — the mubtada.", "«munfasıl» — mübtedâ.", "الْمُنْفَصِلُ"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("يَسْتَقِلُّ", "istaqalla", "verb", ["ism-mawsul", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«stands».", "«müstakil olur»."),
  W("بِنَفْسِهِ", "nafs", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَفْسِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«by itself».", "«kendi başına».", segments=[seg("بِ", "bi", "prep"), seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  nahwu(punct=None),
  W("أَنَا", "ana", "pron", ["idafa-definiteness", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — ضَمِيرٌ مَرْفُوعٌ مُنْفَصِلٌ.", "«I» — the detached rafʿ pronoun, cited.", "«ben» — merfû munfasıl zamir.", ),
  atf_wa("وَإِيَّايَ", "iyya", "pron", ["idafa-definiteness", PRON], "إِيَّايَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — ضَمِيرٌ مَنْصُوبٌ مُنْفَصِلٌ.", "«and me» — the detached naṣb pronoun.", "«ve beni» — mansûb munfasıl zamir.", "إِيَّا", punct=".", extra_segs=[seg("إِيَّا", "iyya", "pron"), pr1sy()]),
 ]})

# ----------- s9 (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "And it is in rafʿ, in naṣb and in jarr; the first two are attached and detached, and the third is attached and nothing else." + R_EN,
 "tr": "O, merfû, mansûb ve mecrûrdur; ilk ikisi muttasıl ve munfasıl, üçüncüsü yalnız muttasıldır." + R_TR},
 "tokens": [
  W("وَهُوَ", "huwa", "pron", ["mubtada-khabar", PRON], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  W("مَرْفُوعٌ", "marfu", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«in rafʿ» — the khabar.", "«merfû» — haber."),
  atf_wa("وَمَنْصُوبٌ", "mansub", "noun", ["mubtada-khabar", "ism-maful"], "مَنْصُوبٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and in naṣb».", "«ve mansûb».", "مَنْصُوبٌ"),
  atf_wa("وَمَجْرُورٌ", "majrur", "noun", ["mubtada-khabar", "ism-maful"], "مَجْرُورٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and in jarr».", "«ve mecrûr».", "مَجْرُورٌ", punct="،"),
  atf_wa("وَالْأَوَّلَانِ", "awwal", "noun", ["mubtada-khabar", "al-muthanna"], "الْأَوَّلَانِ مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«and the first two» — the mubtada, the dual on its alif.", "«ilk ikisi» — mübtedâ, tesniye elifle.", "الْأَوَّلَانِ"),
  W("مُتَّصِلٌ", "muttasil", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — أَيْ كُلٌّ مِنْهُمَا مُتَّصِلٌ وَمُنْفَصِلٌ.", "«attached» — the khabar: each of the two comes attached and detached.", "«muttasıl» — haber: her biri muttasıl ve munfasıl gelir."),
  atf_wa("وَمُنْفَصِلٌ", "munfasil", "noun", ["mubtada-khabar"], "مُنْفَصِلٌ مَعْطُوفٌ.", "«and detached».", "«ve munfasıl».", "مُنْفَصِلٌ", punct="،"),
  atf_wa("وَالثَّالِثُ", "thalith", "noun", ["mubtada-khabar"], "الثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third» — the mubtada.", "«üçüncüsü» — mübtedâ.", "الثَّالِثُ"),
  W("مُتَّصِلٌ", "muttasil", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«attached» — the khabar.", "«muttasıl» — haber."),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«değil»."),
  W("غَيْرُ", "ghayr", "noun", ["al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"], "مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ، فِي مَحَلِّ نَصْبٍ — أَيْ لَا غَيْرَ ذَلِكَ.", "«else» — built on the ḍamm, cut from its annexation.", "«başkası» — izâfetten kesildiği için damm üzere mebnî.", punct="."),
 ]})

# ----------- s10 (COMMENTARY: the notebook's examples of the three cases)
S.append({"id": "s10", "translation": {
 "en": "For instance: «I helped, I myself» — both in rafʿ; «Zayd helped you» and «you alone did Zayd help» — in naṣb; «your pen» and «for you» — in jarr." + C_EN,
 "tr": "Meselâ: «nasartü ene» — ikisi merfû; «nasarake Zeydün» ve «iyyâke nasara Zeydün» — mansûb; «kalemüke» ve «leke» — mecrûr." + C_TR},
 "tokens": [
  nahwu(),
  W("نَصَرْتُ", "nasara", "verb", ["fail", PRON], "فِعْلٌ مَاضٍ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«I helped» — the attached tāʾ is the doer.", "«yardım ettim» — muttasıl tâ fâil.", segments=[seg("نَصَرْ", "nasara", "verb"), prT()]),
  W("أَنَا", "ana", "pron", ["tawkid", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلتَّاءِ.", "«I myself» — the detached pronoun, a tawkīd of the tāʾ: both are rafʿ pronouns.", "«ben» — munfasıl zamir, tâ'nın tekidi: ikisi de merfû zamir.", punct="،"),
  atf_wa("وَنَصَرَكَ", "nasara", "verb", ["fail", "maful-bihi", PRON], "نَصَرَ فِعْلٌ مَاضٍ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«and he helped you» — the attached kāf is the object.", "«ve sana yardım etti» — muttasıl kâf mef'ûl.", "نَصَرَ", extra_segs=[seg("نَصَرَ", "nasara", "verb"), pr2ms()]),
  W("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="،"),
  atf_wa("وَإِيَّاكَ", "iyya", "pron", ["maful-bihi", PRON, "qasr"], "إِيَّاكَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«and you alone» — the detached naṣb pronoun, the fronted object.", "«ve yalnız sana» — munfasıl mansûb zamir, öne alınmış mef'ûl.", "إِيَّا", extra_segs=[seg("إِيَّا", "iyya", "pron"), pr2ms()]),
  W("نَصَرَ", "nasara", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«helped».", "«yardım etti»."),
  W("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="،"),
  atf_wa("وَقَلَمُكَ", "qalam", "noun", ["idafa-definiteness", PRON], "قَلَمُ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«and your pen» — the attached kāf is the muḍāf ilayh.", "«ve kalemin» — muttasıl kâf muzâfun ileyh.", "قَلَمُ", extra_segs=[seg("قَلَمُ", "qalam", "noun"), pr2ms()]),
  atf_wa("وَلَكَ", "li", "prep", ["huruf-jarr", PRON], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ.", "«and for you» — the kāf governed by the letter: only attached pronouns take jarr.", "«ve senin için» — kâf harf-i cerle mecrûr: cer zamiri yalnız muttasıldır.", "لَ", punct=".", extra_segs=[seg("لَ", "li", "prep"), pr2ms()]),
 ]})

# ----------- s11 (RESTORED: the five kinds, the first three persons of each)
S.append({"id": "s11", "translation": {
 "en": "So the attached rafʿ pronoun, as in «I beat», «we beat», «you beat»; the detached, as in «I», «we», «you»; the attached naṣb pronoun, as in «he beat me», «he beat us», «he beat you»; the detached, as in «me», «us», «you»; and the jarr pronoun, as in «my slave», «our slave», «your slave»." + R_EN,
 "tr": "Merfû muttasıl: «darabtü, darabnâ, darabte» gibi; munfasıl: «ene, nahnü, ente» gibi; mansûb muttasıl: «darabenî, darabenâ, darabeke» gibi; munfasıl: «iyyâye, iyyânâ, iyyâke» gibi; mecrûr: «gulâmî, gulâmünâ, gulâmüke» gibi." + R_TR},
 "tokens": [
  W("فَالْمَرْفُوعُ", "marfu", "noun", ["mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمَرْفُوعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the rafʿ one» — the mubtada.", "«merfû» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الْمَرْفُوعُ", "marfu", "noun")]),
  W("الْمُتَّصِلُ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ لِلْمَرْفُوعِ مَرْفُوعَةٌ.", "«attached» — its naʿt.", "«muttasıl» — sıfat."),
  nahwu(punct=None),
  W("ضَرَبْتُ", "daraba", "verb", ["idafa-definiteness", "fail", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالتَّاءُ فَاعِلٌ.", "«I beat» — cited, the tāʾ its doer.", "«dövdüm» — hikâye, tâ fâil.", segments=[seg("ضَرَبْ", "daraba", "verb"), prT()]),
  atf_wa("وَضَرَبْنَا", "daraba", "verb", ["fail", PRON], "ضَرَبْنَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَنَا فَاعِلٌ.", "«and we beat».", "«ve dövdük».", "ضَرَبْ", extra_segs=[seg("ضَرَبْ", "daraba", "verb"), pr1p()]),
  atf_wa("وَضَرَبْتَ", "daraba", "verb", ["fail", PRON], "ضَرَبْتَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَالتَّاءُ فَاعِلٌ.", "«and you beat».", "«ve dövdün».", "ضَرَبْ", punct="،", extra_segs=[seg("ضَرَبْ", "daraba", "verb"), seg("تَ", "pron-2ms", "pron")]),
  atf_wa("وَالْمُنْفَصِلُ", "munfasil", "noun", ["mubtada-khabar"], "الْمُنْفَصِلُ مُبْتَدَأٌ مَرْفُوعٌ، خَبَرُهُ نَحْوُ.", "«and the detached» — the mubtada.", "«munfasıl» — mübtedâ.", "الْمُنْفَصِلُ"),
  nahwu(punct=None),
  W("أَنَا", "ana", "pron", ["idafa-definiteness", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«I».", "«ben»."),
  atf_wa("وَنَحْنُ", "nahnu", "pron", [PRON], "نَحْنُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and we».", "«ve biz».", "نَحْنُ"),
  atf_wa("وَأَنْتَ", "anta", "pron", [PRON], "أَنْتَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and you».", "«ve sen».", "أَنْتَ", punct="،"),
  atf_wa("وَالْمَنْصُوبُ", "mansub", "noun", ["mubtada-khabar"], "الْمَنْصُوبُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the naṣb one» — the mubtada.", "«mansûb» — mübtedâ.", "الْمَنْصُوبُ"),
  W("الْمُتَّصِلُ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«attached».", "«muttasıl»."),
  nahwu(punct=None),
  W("ضَرَبَنِي", "daraba", "verb", ["idafa-definiteness", "maful-bihi", "ya-al-mutakallim"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — ضَرَبَ فِعْلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«he beat me» — the wiqāya nūn, the yāʾ its object.", "«beni dövdü» — vikâye nûnu, yâ mef'ûl.", segments=[seg("ضَرَبَ", "daraba", "verb"), pr1s()]),
  atf_wa("وَضَرَبَنَا", "daraba", "verb", ["maful-bihi", PRON], "ضَرَبَنَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَنَا مَفْعُولٌ بِهِ.", "«and he beat us».", "«ve bizi dövdü».", "ضَرَبَ", extra_segs=[seg("ضَرَبَ", "daraba", "verb"), pr1p()]),
  atf_wa("وَضَرَبَكَ", "daraba", "verb", ["maful-bihi", PRON], "ضَرَبَكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَالْكَافُ مَفْعُولٌ بِهِ.", "«and he beat you».", "«ve seni dövdü».", "ضَرَبَ", punct="،", extra_segs=[seg("ضَرَبَ", "daraba", "verb"), pr2ms()]),
  atf_wa("وَالْمُنْفَصِلُ", "munfasil", "noun", ["mubtada-khabar"], "الْمُنْفَصِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the detached».", "«munfasıl».", "الْمُنْفَصِلُ"),
  nahwu(punct=None),
  W("إِيَّايَ", "iyya", "pron", ["idafa-definiteness", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — ضَمِيرُ نَصْبٍ مُنْفَصِلٌ.", "«me».", "«beni».", segments=[seg("إِيَّا", "iyya", "pron"), pr1sy()]),
  atf_wa("وَإِيَّانَا", "iyya", "pron", [PRON], "إِيَّانَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and us».", "«ve bizi».", "إِيَّا", extra_segs=[seg("إِيَّا", "iyya", "pron"), pr1p()]),
  atf_wa("وَإِيَّاكَ", "iyya", "pron", [PRON], "إِيَّاكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and you».", "«ve seni».", "إِيَّا", punct="،", extra_segs=[seg("إِيَّا", "iyya", "pron"), pr2ms()]),
  atf_wa("وَالْمَجْرُورُ", "majrur", "noun", ["mubtada-khabar"], "الْمَجْرُورُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the jarr one» — the mubtada.", "«mecrûr» — mübtedâ.", "الْمَجْرُورُ"),
  nahwu(punct=None),
  W("غُلَامِي", "ghulam", "noun", ["idafa-definiteness", "ya-al-mutakallim", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — غُلَامِ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my slave» — the yāʾ its muḍāf ilayh.", "«kölem» — yâ muzâfun ileyh.", segments=[seg("غُلَامِ", "ghulam", "noun"), pr1sy()]),
  atf_wa("وَغُلَامُنَا", "ghulam", "noun", ["idafa-definiteness", PRON], "غُلَامُنَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَنَا مُضَافٌ إِلَيْهِ.", "«and our slave».", "«ve kölemiz».", "غُلَامُ", extra_segs=[seg("غُلَامُ", "ghulam", "noun"), pr1p()]),
  atf_wa("وَغُلَامُكَ", "ghulam", "noun", ["idafa-definiteness", PRON], "غُلَامُكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«and your slave».", "«ve kölen».", "غُلَامُ", punct=".", extra_segs=[seg("غُلَامُ", "ghulam", "noun"), pr2ms()]),
 ]})

# ----------- s12 (RESTORED: the concealed marfu')
S.append({"id": "s12", "translation": {
 "en": "And the attached rafʿ pronoun is concealed in the past verb's absent masculine and feminine, as in «he beat» and «she beat»; in the non-past's speakers, its single masculine addressee, its absent masculine and feminine, as in «I beat», «we beat», «you beat», «he beats»; and in the adjectives when they are not predicated of an apparent noun." + R_EN,
 "tr": "Merfû muttasıl zamir mâzînin gâib ve gâibesinde gizlenir, «darabe» ve «darabet» gibi; muzârinin mütekellimlerinde, müfred müzekker muhâtabında, gâib ve gâibesinde, «adribü, nadribü, tadribü, yadribü» gibi; ve zâhir isme isnâd edilmedikleri zaman sıfatlarda." + R_TR},
 "tokens": [
  atf_wa("وَيَسْتَتِرُ", "istatara", "verb", ["fail", "form-viii-verbs"], "يَسْتَتِرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is concealed».", "«ve gizlenir».", "يَسْتَتِرُ"),
  W("الْمَرْفُوعُ", "marfu", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the rafʿ one» — the doer.", "«merfû» — fâil."),
  W("الْمُتَّصِلُ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«attached».", "«muttasıl»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("غَائِبِ", "ghaib", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the absent masculine of».", "«gâibinde»."),
  W("الْمَاضِي", "madi", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the past verb» — a manqūṣ.", "«mâzînin» — mankûs."),
  atf_wa("وَغَائِبَتِهِ", "ghaiba", "noun", ["idafa-definiteness"], "غَائِبَتِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its absent feminine».", "«ve gâibesinde».", "غَائِبَتِ", extra_segs=[seg("غَائِبَتِ", "ghaiba", "noun"), pr3msi()]),
  nahwu(punct=None),
  W("ضَرَبَ", "daraba", "verb", ["idafa-definiteness", "al-mustatir-jawazan"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — فَاعِلُهُ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هُوَ.", "«he beat» — its doer concealed by choice.", "«dövdü» — fâili cevâzen gizli."),
  atf_wa("وَضَرَبَتْ", "daraba", "verb", ["al-mustatir-jawazan"], "ضَرَبَتْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — وَالتَّاءُ لِلتَّأْنِيثِ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "«and she beat» — the tāʾ marks the feminine; the doer concealed.", "«ve dövdü (o kadın)» — tâ tenis içindir; fâil gizli.", "ضَرَبَتْ", punct="،"),
  W("وَفِي", "fi", "prep", ["huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in».", "«ve -de».", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")]),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the non-past».", "«muzâride»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ — بَدَلٌ مِنَ الْأَوَّلِ.", "«in».", "«-de»."),
  W("الْمُتَكَلِّمِ", "mutakallim", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the speaker».", "«mütekellimde»."),
  atf_wa("وَالْمُخَاطَبِ", "mukhatab", "noun", ["huruf-jarr"], "الْمُخَاطَبِ مَعْطُوفٌ مَجْرُورٌ.", "«and the addressee».", "«ve muhâtabda».", "الْمُخَاطَبِ"),
  W("الْمُفْرَدِ", "mufrad", "noun", ["naat-sifa"], "صِفَةٌ لِلْمُخَاطَبِ مَجْرُورَةٌ.", "«single» — its naʿt.", "«müfred» — sıfat."),
  atf_wa("وَالْغَائِبِ", "ghaib", "noun", ["huruf-jarr"], "الْغَائِبِ مَعْطُوفٌ مَجْرُورٌ.", "«and the absent masculine».", "«ve gâibde».", "الْغَائِبِ"),
  atf_wa("وَالْغَائِبَةِ", "ghaiba", "noun", ["huruf-jarr"], "الْغَائِبَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the absent feminine».", "«ve gâibede».", "الْغَائِبَةِ"),
  nahwu(punct=None),
  W("أَضْرِبُ", "daraba", "verb", ["idafa-definiteness", "al-fail-al-mudmar-al-mustatir-wujuban"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — فَاعِلُهُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ أَنَا.", "«I beat» — its doer concealed of necessity.", "«döverim» — fâili vücûben gizli."),
  atf_wa("وَنَضْرِبُ", "daraba", "verb", ["al-fail-al-mudmar-al-mustatir-wujuban"], "نَضْرِبُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — فَاعِلُهُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ نَحْنُ.", "«and we beat».", "«ve döveriz».", "نَضْرِبُ"),
  atf_wa("وَتَضْرِبُ", "daraba", "verb", ["al-fail-al-mudmar-al-mustatir-wujuban"], "تَضْرِبُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — فَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ أَنْتَ أَوْ هِيَ.", "«and you beat» — or «she beats»: one form, the doer concealed.", "«ve döversin» — ya da «döver (o kadın)»: tek şekil, fâil gizli.", "تَضْرِبُ"),
  atf_wa("وَيَضْرِبُ", "daraba", "verb", ["al-mustatir-jawazan"], "يَضْرِبُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — فَاعِلُهُ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هُوَ.", "«and he beats».", "«ve döver».", "يَضْرِبُ", punct="،"),
  W("وَفِي", "fi", "prep", ["huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in».", "«ve -de».", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")]),
  W("الصِّفَاتِ", "sifa", "noun", ["huruf-jarr", "jam-muannath-salim", "ism-fail"], "مَجْرُورٌ بِالْكَسْرَةِ — الصِّفَاتُ: اسْمُ الْفَاعِلِ وَالْمَفْعُولِ وَالصِّفَةُ الْمُشَبَّهَةُ.", "«the adjectives» — the participles and the ṣifa mushabbaha.", "«sıfatlarda» — ism-i fâil, ism-i mef'ûl, sıfat-ı müşebbehe."),
  W("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diği zaman»."),
  W("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me-»."),
  W("تُسْنَدْ", "asnada", "verb", ["lam-jazim", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "«they are predicated» — the passive, jazm'd by لَمْ.", "«isnâd edilmez» — meçhul, lem ile meczûm."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-e»."),
  W("الظَّاهِرِ", "zahir", "noun", ["huruf-jarr", "ism-fail"], "مَجْرُورٌ بِالْكَسْرَةِ — الِاسْمُ الظَّاهِرُ.", "«an apparent noun».", "«zâhir isme».", punct="."),
 ]})

# ----------- s13 (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And the detached is not allowed while the attached is possible, because the pronouns were coined for brevity." + R_EN,
 "tr": "Muttasıl mümkün iken munfasıl câiz olmaz; çünkü zamirler ihtisar için vaz edilmiştir." + R_TR},
 "tokens": [
  W("وَلَا", "la", "part", ["la-nafiya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا حَرْفُ نَفْيٍ.", "«and not».", "«ve -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part")]),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«is allowed».", "«câiz olur»."),
  W("الْمُنْفَصِلُ", "munfasil", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the detached» — the doer.", "«munfasıl» — fâil."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«-ken»."),
  W("إِمْكَانِ", "imkan", "noun", ["idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the possibility of».", "«mümkün olması»."),
  W("الْمُتَّصِلِ", "muttasil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the attached».", "«muttasılın».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الضَّمَائِرَ", "damir", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ ضَمِيرٍ.", "«the pronouns» — the ism of أَنَّ.", "«zamirler» — enne'nin ismi."),
  W("وُضِعَتْ", "wadaa", "verb", ["inna-wa-akhawatuha", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«were coined» — the passive; the clause is the khabar of أَنَّ.", "«vaz edildi» — meçhul; cümle enne'nin haberi."),
  W("لِلِاخْتِصَارِ", "ikhtisar", "noun", ["huruf-jarr", "masdar"], "اللَّامُ حَرْفُ جَرٍّ، وَالِاخْتِصَارِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for brevity».", "«ihtisar için».", punct=".", segments=[seg("لِ", "li", "prep"), seg("الِاخْتِصَارِ", "ikhtisar", "noun")]),
 ]})

# ---------------------------------------------------------------- Qur'an marks (5:8 inside s7)
for _t in S[6]["tokens"]:
    if _t["surface"]["full"] == "وَاعْدِلُوا": _t["quoteBefore"] = "﴿"
    if _t["surface"]["full"] == "لِلتَّقْوَى": _t["quoteAfter"] = "﴾"

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
 "laqab": need("laqab", "لَقَب", "ل ق ب", "noun", "a name, a title (pl. أَلْقَاب) — أَلْقَابُ الْمَبْنِيِّ: the names of the indeclinable's endings", "lakap, unvan (ç. أَلْقَاب) — elkâbü'l-mebnî", 3, plural="أَلْقَاب"),
 "amsi": need("amsi", "أَمْسِ", "أ م س", "noun", "yesterday — a time adverb built on the kasra", "dün — kesre üzere mebnî zaman zarfı", 2),
 "qalam": need("qalam", "قَلَم", "ق ل م", "noun", "a pen (pl. أَقْلَام)", "kalem (ç. أَقْلَام)", 1, plural="أَقْلَام"),
 "adala": need("adala", "عَدَلَ", "ع د ل", "verb", "to be just, to act justly (عَدَلَ يَعْدِلُ)", "âdil olmak, adaletle davranmak (adele ya'dilu)", 3),
 "ikhtisar": need("ikhtisar", "اِخْتِصَار", "خ ص ر", "noun", "brevity, shortening (masdar of Form VIII اِخْتَصَرَ)", "ihtisar, kısaltma (ihtesara'nın masdarı)", 4),
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
put_morph(mo, "adala", _sg.sound1("daraba", "عَدَل", "عْدِل", "اِعْدِل", "عَدْل", "عَادِل", "مَعْدُول", "عُدِلَ", "يُعْدَلُ", "عَدَلَ يَعْدِلُ: أَنْصَفَ وَاسْتَقَامَ — مِنْ بَابِ ضَرَبَ؛ وَعَدَلَ عَنْهُ: مَالَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch3 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": K,
 "title": {"ar": "الْمَبْنِيُّ وَالْمُضْمَرُ", "en": "The indeclinable and the pronoun: the Kafiya's definitions, the five kinds and the concealed doer", "tr": "Mebnî ve muzmar: Kâfiye'nin tarifleri, beş nevi ve gizli fâil"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المبني ما ناسب مبني الأصل أو وقع غير مركب؛ المضمر ما وضع لمتكلم أو مخاطب أو غائب تقدم ذكره لفظا أو معنى أو حكما؛ وهو متصل ومنفصل، مرفوع ومنصوب ومجرور", "ضياء صونغور اوغلى — دفتر الكافية (سؤال وجواب): ألقاب المبني، أقسام الضمائر الخمسة بأمثلتها، مواضع الاستتار"],
 "question": {
  "en": ["What is the MABNI? What resembles the indeclinable-by-origin (the particle, the past verb, the imperative) or stands outside a construction: مَا نَاسَبَ مَبْنِيَّ الْأَصْلِ أَوْ وَقَعَ غَيْرَ مُرَكَّبٍ. Its ruling: the ending does not change with the governor — جَاءَنِي هٰذَا، رَأَيْتُ هٰذَا، مَرَرْتُ بِهٰذَا.",
         "What are its NAMES? Not rafʿ, naṣb and jarr but ḍamm (يَا زَيْدُ), fatḥ (لَا أَحَدَ), kasr (أَمْسِ) and waqf (اُنْصُرْ) — the same vowels, under other names, because they are not put there by a governor.",
         "Which nouns are mabni? The pronouns, the demonstratives, the relatives, the compounds, the allusive nouns (كَمْ، كَذَا), the verb-nouns (رُوَيْدَ), the sound-words (غَاقِ) and some adverbs (إِذْ، حَيْثُ).",
         "What is the PRONOUN? A noun coined for a speaker, an addressee, or an absent one whose mention preceded — in wording (غُلَامَهُ after زَيْدٌ), in sense (هُوَ after اعْدِلُوا, returning to the justice the verb implies), or in ruling (the pronoun of the matter, explained by the sentence after it).",
         "Attached or detached? The attached does not stand by itself (the tāʾ and the kāf of ضَرَبْتُكَ); the detached does (أَنَا، إِيَّايَ). By case there are three kinds; rafʿ and naṣb come both ways, jarr only attached — so there are FIVE sets of fourteen forms.",
         "Where does the rafʿ pronoun hide? In the past verb's third persons (ضَرَبَ، ضَرَبَتْ — by choice), in the non-past's speakers, single masculine addressee and third persons (أَضْرِبُ، نَضْرِبُ، تَضْرِبُ، يَضْرِبُ) and in the adjectives when they are not predicated of an apparent noun.",
         "Why «no detached while the attached is possible»? Pronouns exist for brevity; the longer form is used only where the shorter cannot stand — the chapter that follows lists those places.",
         "What does the engine read? The DabtEngine's pronoun pass splits every clitic into its host and its pronoun and names the pronoun's seat (doer, object, muḍāf ilayh); TaqdirEngine restores the concealed doer the chapter names — هُوَ، هِيَ by choice, أَنَا، نَحْنُ، أَنْتَ of necessity."],
  "tr": ["MEBNÎ nedir? Aslen mebnî olana (harf, mâzî, emir) benzeyen ya da terkib dışında vâki olan: مَا نَاسَبَ مَبْنِيَّ الْأَصْلِ أَوْ وَقَعَ غَيْرَ مُرَكَّبٍ. Hükmü: sonu âmille değişmez — جَاءَنِي هٰذَا، رَأَيْتُ هٰذَا، مَرَرْتُ بِهٰذَا.",
         "LAKAPLARI nelerdir? Ref', nasb ve cer değil; damm (يَا زَيْدُ), feth (لَا أَحَدَ), kesr (أَمْسِ) ve vakf (اُنْصُرْ) — aynı harekeler, başka adlarla; çünkü onları bir âmil koymamıştır.",
         "Hangi isimler mebnîdir? Zamirler, işaret isimleri, mevsûller, mürekkebler, kinâyeler (كَمْ، كَذَا), isim-fiiller (رُوَيْدَ), savtlar (غَاقِ) ve bazı zarflar (إِذْ، حَيْثُ).",
         "ZAMİR nedir? Mütekellim, muhâtab ya da zikri lafzen (زَيْدٌ'den sonra غُلَامَهُ), manen (اعْدِلُوا'dan sonra fiilin ima ettiği adle râci هُوَ) veya hükmen (sonraki cümlenin açıkladığı şan zamiri) geçmiş gâib için vaz edilen isim.",
         "Muttasıl mı munfasıl mı? Muttasıl kendi başına durmaz (ضَرَبْتُكَ'nin tâ'sı ve kâf'ı); munfasıl durur (أَنَا، إِيَّايَ). Hâle göre üç nevi vardır; ref' ve nasb her iki şekilde, cer yalnız muttasıl gelir — böylece on dörder şekilli BEŞ takım olur.",
         "Merfû zamir nerede gizlenir? Mâzînin üçüncü şahıslarında (ضَرَبَ، ضَرَبَتْ — cevâzen), muzârinin mütekellimlerinde, müfred müzekker muhâtabında ve üçüncü şahıslarında (أَضْرِبُ، نَضْرِبُ، تَضْرِبُ، يَضْرِبُ) ve zâhir isme isnâd edilmedikleri zaman sıfatlarda.",
         "Niçin «muttasıl mümkünken munfasıl olmaz»? Zamirler ihtisar içindir; uzun şekil ancak kısasının duramadığı yerde kullanılır — sonraki bâb o yerleri sayar.",
         "Motor neyi okur? DabtEngine'in zamir geçişi her ekli kelimeyi gövdesine ve zamirine ayırır, zamirin yerini (fâil, mef'ûl, muzâfun ileyh) adlandırır; TaqdirEngine bâbın saydığı gizli fâili geri yazar — هُوَ، هِيَ cevâzen, أَنَا، نَحْنُ، أَنْتَ vücûben."]},
 "plain": {
  "en": "A mabni noun keeps one ending whatever governs it, and its endings are called ḍamm, fatḥ, kasr and waqf. The pronoun is the first mabni: it stands for a speaker, an addressee or someone already mentioned; it comes attached or detached, in rafʿ, naṣb or jarr; and it is often hidden inside the verb.",
  "tr": "Mebnî isim, âmili ne olursa olsun tek sonu korur; sonlarına damm, feth, kesr ve vakf denir. Zamir ilk mebnîdir: mütekellim, muhâtab ya da daha önce anılan biri yerine durur; muttasıl ya da munfasıl, merfû, mansûb ya da mecrûr gelir; çoğu zaman fiilin içinde gizlidir."},
 "explanation": {
  "en": "الْمَبْنِيُّ مَا نَاسَبَ مَبْنِيَّ الْأَصْلِ أَوْ وَقَعَ غَيْرَ مُرَكَّبٍ. Ibn al-Hajib defines the mabni as the mirror of the muʿrab: either it resembles the things indeclinable by origin — the particle (one or two letters, no independent meaning), the past verb and the imperative — or it stands in no construction at all (the words counted one by one: alif, bāʾ, Zayd, ʿAmr). Its ruling is that its ending does not differ with the governor — the same هٰذَا after جَاءَنِي, after رَأَيْتُ and after بِـ — and since no governor puts the vowel there, the vowels take other names: ḍamm, fatḥ, kasr and waqf (sukūn). The mabni nouns are eight classes, and the chapter opens the first: the pronoun — coined for a speaker, an addressee, or an absent one whose mention preceded in wording, in sense or in ruling. It is attached (never standing alone: the tāʾ of ضَرَبْتُ, the kāf of ضَرَبَكَ, the yāʾ of غُلَامِي) or detached (أَنَا، أَنْتَ، إِيَّاكَ); and by case rafʿ, naṣb or jarr — the first two both ways, the third attached only, which yields the notebook's five tables of fourteen forms. The rafʿ attached pronoun may hide inside the verb: by choice in the past's third persons, of necessity in أَضْرِبُ، نَضْرِبُ، تَضْرِبُ, and in the adjectives when they are not predicated of an apparent noun. The closing rule governs everything that follows: the detached is never used while the attached is possible, because the pronoun exists to shorten speech.",
  "tr": "الْمَبْنِيُّ مَا نَاسَبَ مَبْنِيَّ الْأَصْلِ أَوْ وَقَعَ غَيْرَ مُرَكَّبٍ. İbnü'l-Hâcib mebnîyi mu'rebin aynası olarak tarif eder: ya aslen mebnî olanlara — harfe (bir iki harf, müstakil manası yok), mâzîye ve emre — benzer, ya da hiç terkibde bulunmaz (tek tek sayılan kelimeler: elif, bâ, Zeyd, Amr). Hükmü, sonunun âmille değişmemesidir — جَاءَنِي'den, رَأَيْتُ'den ve بِـ'den sonra aynı هٰذَا — ve harekeyi oraya bir âmil koymadığı için harekeler başka adlar alır: damm, feth, kesr ve vakf (sükûn). Mebnî isimler sekiz sınıftır ve bâb ilkini açar: zamir — mütekellim, muhâtab ya da zikri lafzen, manen veya hükmen geçmiş gâib için vaz edilmiştir. Muttasıl (asla tek başına durmaz: ضَرَبْتُ'nün tâ'sı, ضَرَبَكَ'nin kâf'ı, غُلَامِي'nin yâ'sı) ya da munfasıldır (أَنَا، أَنْتَ، إِيَّاكَ); hâle göre merfû, mansûb ya da mecrûrdur — ilk ikisi her iki şekilde, üçüncüsü yalnız muttasıl; böylece defterin on dörder şekilli beş cetveli çıkar. Merfû muttasıl zamir fiilin içinde gizlenebilir: mâzînin üçüncü şahıslarında cevâzen, أَضْرِبُ، نَضْرِبُ، تَضْرِبُ'de vücûben ve zâhir isme isnâd edilmeyen sıfatlarda. Kapanış kuralı sonrakilerin hepsini yönetir: muttasıl mümkünken munfasıl asla kullanılmaz; çünkü zamir sözü kısaltmak içindir."},
 "examples": [
  {"ar": "الْمَبْنِيُّ مَا نَاسَبَ مَبْنِيَّ الْأَصْلِ أَوْ وَقَعَ غَيْرَ مُرَكَّبٍ", "en": "The definition of the indeclinable.", "tr": "Mebnînin tarifi.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "وَأَلْقَابُهُ: الضَّمُّ نَحْوُ يَا زَيْدُ، وَالْفَتْحُ نَحْوُ لَا أَحَدَ، وَالْكَسْرُ نَحْوُ أَمْسِ، وَالْوَقْفُ نَحْوُ اُنْصُرْ", "en": "The four names of the mabni's endings.", "tr": "Mebnînin sonlarının dört lakabı.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "الْمُضْمَرُ: مَا وُضِعَ لِمُتَكَلِّمٍ أَوْ مُخَاطَبٍ أَوْ غَائِبٍ تَقَدَّمَ ذِكْرُهُ لَفْظًا أَوْ مَعْنًى أَوْ حُكْمًا", "en": "The definition of the pronoun.", "tr": "Zamirin tarifi.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "نَصَرْتُ أَنَا، وَنَصَرَكَ زَيْدٌ، وَإِيَّاكَ نَصَرَ زَيْدٌ، وَقَلَمُكَ، وَلَكَ", "en": "The three cases in the notebook's examples.", "tr": "Defterin örneklerinde üç hâl.", "sourceStory": "al-kafiya", "sentence": "s10"},
  {"ar": "وَلَا يَجُوزُ الْمُنْفَصِلُ مَعَ إِمْكَانِ الْمُتَّصِلِ، لِأَنَّ الضَّمَائِرَ وُضِعَتْ لِلِاخْتِصَارِ", "en": "The rule of brevity.", "tr": "İhtisar kuralı.", "sourceStory": "al-kafiya", "sentence": "s13"}],
 "commonMistakes": [
  {"wrong": "«يَا زَيْدُ — Zeyd merfûdur, çünkü sonu dammedir»",
   "right": "«يَا زَيْدُ — münâdâ damm üzere MEBNÎDİR, mahallen mansûb»",
   "why": {"en": "The vowel is the same but no governor put it there; the Kafiya therefore calls it ḍamm, not rafʿ, and the word is mabni in the place of naṣb.", "tr": "Hareke aynıdır ama onu bir âmil koymamıştır; Kâfiye bu yüzden ona ref' değil damm der ve kelime mahallen mansûb mebnîdir."}},
  {"wrong": "«ضَرَبَكَ زَيْدٌ — kâf fâildir, çünkü fiile bitişiktir»",
   "right": "«ضَرَبَكَ زَيْدٌ — kâf mansûb muttasıl zamir, MEF'ÛLDÜR; fâil Zeyd'dir»",
   "why": {"en": "Attached pronouns come in all three cases; which seat the kāf fills is decided by the verb that still owes its doer, not by its attachment.", "tr": "Muttasıl zamirler üç hâlde de gelir; kâf'ın hangi yeri doldurduğunu bitişikliği değil, fâilini hâlâ bekleyen fiil belirler."}},
  {"wrong": "«لَكَ — kâf munfasıl zamirdir»",
   "right": "«لَكَ — kâf MUTTASIL mecrûr zamirdir; cer zamirinin munfasılı yoktur»",
   "why": {"en": "The third kind is attached and nothing else: no detached pronoun ever stands after a jarr letter or as a muḍāf ilayh.", "tr": "Üçüncü nevi yalnız muttasıldır: hiçbir munfasıl zamir harf-i cerden sonra ya da muzâfun ileyh olarak durmaz."}},
  {"wrong": "«أَنَا ضَرَبْتُ — ene fâildir»",
   "right": "«أَنَا ضَرَبْتُ — ene mübtedâ, tâ fâildir; ya da ضَرَبْتُ أَنَا'da ene tekiddir»",
   "why": {"en": "The detached pronoun is not used where the attached one can stand; before the verb it is a mubtada, after it a tawkīd of the tāʾ.", "tr": "Muttasılın durabildiği yerde munfasıl kullanılmaz; fiilden önce mübtedâ, sonra tâ'nın tekididir."}}],
 "relatedNotes": [K2, PRON, "al-fail-al-mudmar-al-mustatir-wujuban", "al-mustatir-jawazan", "ya-al-mutakallim", "damir-fasl", "asma-al-ishara", "ism-mawsul", "vocative-munada", "la-nafiya-lil-jins", "imperative-amr"]}

ADD_EN = (" Chapter 3 (notebook lines ~157-164): the mabni's definition (s1), its ruling (s2) with the teacher's triplet (s3), its four names with "
          "the notebook's examples (s4), the eight mabni classes (s5), the pronoun's definition (s6) with the three mentions (s7), attached and detached (s8), "
          "the three cases and the five kinds (s9-s11), the concealed rafʿ pronoun (s12) and the rule of brevity (s13). Rulings the notebook gives only in "
          "Turkish are RESTORED from the received matn and marked; the teacher's worked examples (s3, s7, s10) are marked as commentary; the Qur'anic "
          "words of al-Ma'ida 5:8 in s7 are set as the notebook cites them.")
ADD_TR = (" Üçüncü bâb (defter satırları ~157-164): mebnînin tarifi (s1), hükmü (s2) ve hocanın üçlüsü (s3), defterin örnekleriyle dört lakabı (s4), sekiz "
          "mebnî sınıfı (s5), zamirin tarifi (s6) ve üç zikir (s7), muttasıl ve munfasıl (s8), üç hâl ve beş nevi (s9-s11), gizli merfû zamir (s12) ve "
          "ihtisar kuralı (s13). Defterin yalnız Türkçe verdiği hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; hocanın işlenmiş örnekleri "
          "(s3, s7, s10) şerh olarak işaretlidir; s7'deki Mâide 5:8 âyetinin kelimeleri defterin iktibas ettiği gibi dizilmiştir.")
write_out(3, S, TITLE, ADD_EN, ADD_TR, "157-164", GLOSS_ADD, notes=(NOTE,),
          related=((K2, [K]), (PRON, [K]), ("al-mustatir-jawazan", [K]), ("ya-al-mutakallim", [K])))
report(3, S, GLOSS_ADD, (NOTE,))
