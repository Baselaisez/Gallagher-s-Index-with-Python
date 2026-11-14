# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 15: THE MASDAR. Its definition in the notebook's own Arabic; what «running on the verb» means (confirmation,
number, kind — جَلَسْتُ جُلُوسًا / جَلْسَةً / جِلْسَةً); the mujarrad's masdars heard, the mazid's by rule (إِخْرَاج، اِسْتِخْرَاج); the
masdar governs like its verb in every tense when it is not a maf'ul mutlaq (أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا أَمْسِ…); its governed word never
precedes it and no doer hides in it; annexed to its doer (وَلَوْلَا دَفْعُ اللهِ النَّاسَ) or its object (ضَرْبُ اللِّصِّ الْجَلَّادُ); the
al-masdar seldom governs (لَا يُحِبُّ اللهُ الْجَهْرَ بِالسُّوءِ); and the maf'ul mutlaq — the verb governs, or the two views on سَقْيًا زَيْدًا.
Source: the Ottoman notebook (Ziya Sungur-oglu), line ~255 of the transcription.

  VERBATIM: s1. RESTORED (received matn, marked): s3, s5, s6, s7, s8. COMMENTARY (the notebook's Q&A and explanations): s2, s4, s9, s10.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch15.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-masdar-fil-kafiya"
MN = "masdar"
TITLE = {"ar": "الْمَصْدَرُ", "en": "The maṣdar", "tr": "Masdar"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
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
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
# the running example: أَعْجَبَنِي + maṣdar + doer + object + time
def ajabani(): return W("أَعْجَبَنِي", "ajaba-please", "verb", ["fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«pleased me».", "«hoşuma gitti».", segments=[seg("أَعْجَبَ", "ajaba-please", "verb"), pr1s()])
def masdar_doer(full, lex, ar_m, en, tr, punct=None):
    return [W(full, lex, "noun", ["fail", "idafa-definiteness", MN, "imal-al-masdar"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ عَمَلَ فِعْلِهِ.", en, tr),
            W(ar_m[0], ar_m[1], "propn", ["idafa-definiteness", "imal-al-masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلُ الْمَصْدَرِ فِي الْمَعْنَى.", ar_m[2], ar_m[3], punct=punct)]
def masdar_obj(full, lex, en, tr, punct=None):
    return W(full, lex, "propn", ["maful-bihi", "imal-al-masdar"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", en, tr, punct=punct)

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The maṣdar: the name of the event that runs on the verb.",
 "tr": "Masdar: fiil üzerine cereyan eden hadesin (işin) ismidir."},
 "tokens": [
  W("الْمَصْدَرُ", "masdar-noun", "noun", ["mubtada-khabar", MN], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the maṣdar» — the mubtada.", "«masdar» — mübtedâ.", punct=":"),
  W("اسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the name of» — the khabar.", "«ismi» — haber."),
  W("الْحَدَثِ", "hadath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the event».", "«hadesin»."),
  W("الْجَارِي", "jari", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«that runs» — a manqūṣ ṣifa.", "«cereyan eden» — mankûs sıfat."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الْفِعْلِ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the verb».", "«fiil».", punct="."),
 ]})

# ----------- s2 (COMMENTARY): what «running on the verb» means
S.append({"id": "s2", "translation": {
 "en": "And its running on the verb is its coming after the verb derived from it — to confirm it, as in جَلَسْتُ جُلُوسًا, or to state its number, as in جَلَسْتُ جَلْسَةً, or its kind, as in جِلْسَةً." + C_EN,
 "tr": "Fiil üzerine cereyan etmesi, kendisinden türeyen fiilden sonra gelmesidir — onu tekit için, جَلَسْتُ جُلُوسًا gibi; sayısını bildirmek için, جَلَسْتُ جَلْسَةً gibi; veya nev'ini, جِلْسَةً gibi." + C_TR},
 "tokens": [
  atf_wa("وَجَرْيُهُ", "jary", "noun", ["mubtada-khabar", "idafa-definiteness"], "جَرْيُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its running».", "«ve cereyanı».", "جَرْيُ", extra_segs=[seg("جَرْيُ", "jary", "noun"), pr3ms()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الْفِعْلِ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the verb».", "«fiil»."),
  W("مَجِيئُهُ", "maji", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«is its coming» — the khabar.", "«gelmesidir» — haber.", segments=[seg("مَجِيئُ", "maji", "noun"), pr3ms()]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«sonra»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb».", "«fiilden»."),
  W("الْمُشْتَقِّ", "mushtaqq", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«derived».", "«türeyen»."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«from it».", "«kendisinden».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  li_("لِتَأْكِيدِهِ", "takid", "noun", ["idafa-definiteness"], "تَأْكِيدِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to confirm it».", "«onu tekit için».", "تَأْكِيدِ", segs=[seg("لِ", "li", "prep"), seg("تَأْكِيدِ", "takid", "noun"), pr3msi()]),
  nahwu(),
  cited("جَلَسْتُ", "jalasa", "verb", ["fail", "masdar"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I sat».", "«oturdum».", segments=[seg("جَلَسْ", "jalasa", "verb"), prT()]),
  cited("جُلُوسًا", "julus", "noun", ["maful-mutlaq", MN], "مَفْعُولٌ مُطْلَقٌ مُؤَكِّدٌ لِعَامِلِهِ مَنْصُوبٌ.", "«a sitting» — confirming.", "«oturmakla» — tekit.", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  li_("لِبَيَانِ", "bayan", "noun", ["idafa-definiteness"], "بَيَانِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to state».", "«bildirmek için».", "بَيَانِ"),
  W("عَدَدِهِ", "adad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its number».", "«sayısını».", segments=[seg("عَدَدِ", "adad", "noun"), pr3msi()]),
  nahwu(),
  cited("جَلَسْتُ", "jalasa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I sat».", "«oturdum».", segments=[seg("جَلَسْ", "jalasa", "verb"), prT()]),
  cited("جَلْسَةً", "jalsa", "noun", ["maful-mutlaq", MN], "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلْعَدَدِ — مَصْدَرُ الْمَرَّةِ.", "«one sitting» — the maṣdar of number.", "«bir kez oturmak» — merre masdarı.", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("نَوْعِهِ", "naw", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى عَدَدِهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its kind».", "«nev'ini».", segments=[seg("نَوْعِ", "naw", "noun"), pr3msi()]),
  nahwu(),
  cited("جِلْسَةً", "jilsa", "noun", ["maful-mutlaq", MN], "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ — مَصْدَرُ الْهَيْئَةِ.", "«a manner of sitting» — the maṣdar of kind.", "«bir tür oturuş» — hey'et masdarı.", punct="."),
 ]})

# ----------- s3 (RESTORED): heard and ruled
S.append({"id": "s3", "translation": {
 "en": "And the maṣdars of the bare triliteral are heard; the maṣdars of what is other than it go by rule — as in إِخْرَاجٌ and اِسْتِخْرَاجٌ." + R_EN,
 "tr": "Sülâsî mücerredin masdarları semâîdir; onun dışındakilerin masdarları kıyâsîdir — إِخْرَاجٌ ve اِسْتِخْرَاجٌ gibi." + R_TR},
 "tokens": [
  atf_wa("وَمَصَادِرُ", "masdar-noun", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مَصَادِرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the maṣdars of» — the mubtada.", "«ve masdarları» — mübtedâ.", "مَصَادِرُ"),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the triliteral».", "«sülâsînin»."),
  W("الْمُجَرَّدِ", "mujarrad", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«bare».", "«mücerred»."),
  W("سَمَاعِيَّةٌ", "samai", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ.", "«are heard» — the khabar.", "«semâîdir» — haber.", punct="،"),
  atf_wa("وَمَصَادِرُ", "masdar-noun", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَصَادِرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the maṣdars of».", "«ve masdarları».", "مَصَادِرُ"),
  W("غَيْرِهِ", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what is other than it».", "«onun dışındakilerin».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  W("قِيَاسِيَّةٌ", "qiyasi", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ.", "«go by rule».", "«kıyâsîdir».", punct="،"),
  nahwu(),
  cited("إِخْرَاجٍ", "ikhraj", "noun", ["idafa-definiteness", MN, "form-iv-verbs"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مَصْدَرُ أَخْرَجَ عَلَى إِفْعَالٍ.", "«bringing out» — the maṣdar of أَخْرَجَ.", "«çıkarmak» — ahrace'nin masdarı."),
  cited_wa("وَاسْتِخْرَاجٍ", "istikhraj", "noun", [MN, "form-x-verbs"], "اسْتِخْرَاجٍ مَعْطُوفٌ — مَصْدَرُ اسْتَخْرَجَ عَلَى اسْتِفْعَالٍ.", "«and extracting» — the maṣdar of اسْتَخْرَجَ.", "«ve istihrac» — istahrece'nin masdarı.", "اسْتِخْرَاجٍ", punct="."),
 ]})

# ----------- s4 (COMMENTARY): Sībawayh's count
S.append({"id": "s4", "translation": {
 "en": "And Sībawayh mentioned thirty-two of the triliteral's maṣdars." + C_EN,
 "tr": "Sîbeveyh sülâsînin masdarlarından otuz ikisini zikretmiştir." + C_TR},
 "tokens": [
  atf_wa("وَذَكَرَ", "dhakara", "verb", ["fail", "masdar"], "ذَكَرَ فِعْلٌ مَاضٍ.", "«and mentioned».", "«ve zikretti».", "ذَكَرَ"),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["fail", "al-mabni-wal-mudmar"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَبْنِيٌّ عَلَى الْكَسْرِ.", "«Sībawayh» — the doer, built on the kasra.", "«Sîbeveyh» — fâil, kesre üzere mebnî."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("مَصَادِرِ", "masdar-noun", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the maṣdars of».", "«masdarlarından»."),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the triliteral».", "«sülâsînin»."),
  W("اثْنَيْنِ", "ithnan", "noun", ["maful-bihi", "al-muthanna", "asma-al-adad-fil-kafiya"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى.", "«two» — the object, in naṣb by the yāʾ.", "«iki» — mef'ûl, yâ ile mansûb."),
  atf_wa("وَثَلَاثِينَ", "thalathun", "noun", ["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], "ثَلَاثِينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ.", "«and thirty».", "«ve otuz».", "ثَلَاثِينَ", punct="."),
 ]})

# ----------- s5 (RESTORED): the maṣdar governs like its verb
S.append({"id": "s5", "translation": {
 "en": "And it governs as its verb governs, be it past or other, when it is not an absolute object — as in أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا أَمْسِ, and إِكْرَامُ عَمْرٍو خَالِدًا غَدًا, or الْآنَ." + R_EN,
 "tr": "Masdar, mef'ûl-i mutlak olmadığı zaman, mâzî olsun başkası olsun, fiilinin ameli gibi amel eder — أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا أَمْسِ ve إِكْرَامُ عَمْرٍو خَالِدًا غَدًا veya الْآنَ gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَعْمَلُ", "amila", "verb", ["fail", "imal-al-masdar"], "يَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it governs».", "«ve amel eder».", "يَعْمَلُ"),
  W("عَمَلَ", "amal-work", "noun", ["maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«as … governs» — the absolute object.", "«ameli gibi» — mef'ûl-i mutlak."),
  W("فِعْلِهِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its verb».", "«fiilinin».", segments=[seg("فِعْلِ", "fil", "noun"), pr3msi()]),
  W("مَاضِيًا", "madi", "noun", ["hal", "kana-wa-akhawatuha"], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ.", "«past» — kāna's khabar, fronted.", "«mâzî» — kâne'nin öne alınmış haberi."),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ حَالٌ.", "«be it» — the clause a ḥāl.", "«olsun» — cümle hâl."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("غَيْرَهُ", "ghayr", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى مَاضِيًا مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«other».", "«başkası».", punct="،", segments=[seg("غَيْرَ", "ghayr", "noun"), pr3ms()]),
  W("إِذَا", "idha", "part", ["al-majzum-wal-shart-wal-jaza", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığı zaman»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَكُنْ", "kana", "verb", ["nawasib-wa-jawazim-al-mudari", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِالسُّكُونِ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "«it is».", "«olmadığı»."),
  W("مَفْعُولًا", "maful-object", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«an object».", "«mef'ûl»."),
  W("مُطْلَقًا", "mutlaq", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«absolute».", "«mutlak».", punct="،"),
  nahwu(),
  ajabani(),
  *masdar_doer("ضَرْبُ", "darb", ("زَيْدٍ", "zayd", "«Zayd's» — the doer in sense.", "«Zeyd'in» — mânâca fâil."), "«the striking of».", "«vurması»."),
  masdar_obj("عَمْرًا", "amr-name", "«ʿAmr» — the maṣdar's object.", "«Amr'ı» — masdarın mef'ûlü."),
  W("أَمْسِ", "ams", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ — لِلْمَاضِي.", "«yesterday» — the past.", "«dün» — mâzî.", punct="،"),
  *[cited_wa("وَإِكْرَامُ", "ikram", "noun", ["fail", "idafa-definiteness", MN, "imal-al-masdar"], "إِكْرَامُ مَعْطُوفٌ عَلَى ضَرْبُ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the honouring of».", "«ve ikramı».", "إِكْرَامُ"),
    W("عَمْرٍو", "amr-name", "propn", ["idafa-definiteness", "imal-al-masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلُ الْمَصْدَرِ فِي الْمَعْنَى.", "«ʿAmr's».", "«Amr'ın».")],
  masdar_obj("خَالِدًا", "khalid", "«Khālid».", "«Hâlid'i»."),
  W("غَدًا", "ghadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ — لِلْمُسْتَقْبَلِ.", "«tomorrow» — the future.", "«yarın» — istikbâl."),
  W("أَوِ", "aw", "conj", ["atf-nasaq", "al-mabni-wal-mudmar"], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«veya»."),
  W("الْآنَ", "al-an", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ — لِلْحَالِ.", "«now» — the present.", "«şimdi» — hâl.", punct="."),
 ]})

# ----------- s6 (RESTORED): no fronting, no hidden doer
S.append({"id": "s6", "translation": {
 "en": "And its governed word does not precede it — so one does not say أَعْجَبَنِي عَمْرًا ضَرْبُ زَيْدٍ — and no doer is concealed in it, nor need it be mentioned, as in أَعْجَبَنِي ضَرْبٌ زَيْدًا." + R_EN,
 "tr": "Ma'mûlü ondan öne geçmez — أَعْجَبَنِي عَمْرًا ضَرْبُ زَيْدٍ denmez — onda fâil gizlenmez ve zikri de lâzım gelmez; أَعْجَبَنِي ضَرْبٌ زَيْدًا gibi." + R_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -mez».", "لَا"),
  W("يَتَقَدَّمُ", "taqaddama", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«precedes».", "«öne geçer»."),
  W("مَعْمُولُهُ", "mamul", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governed word».", "«ma'mûlü».", segments=[seg("مَعْمُولُ", "mamul", "noun"), pr3ms()]),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«it».", "«ondan».", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«bu yüzden -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«is it said».", "«denir»."),
  ajabani(),
  cited("عَمْرًا", "amr-name", "propn", ["maful-bihi", "imal-al-masdar"], "مَفْعُولٌ بِهِ مُقَدَّمٌ عَلَى عَامِلِهِ الْمَصْدَرِ — مَمْنُوعٌ.", "«ʿAmr» — fronted before its maṣdar: barred.", "«Amr'ı» — masdarından öne alınmış: memnû."),
  *masdar_doer("ضَرْبُ", "darb", ("زَيْدٍ", "zayd", "«Zayd's».", "«Zeyd'in».", ), "«the striking of».", "«vurması».", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -mez».", "لَا"),
  W("يُضْمَرُ", "admara", "verb", ["naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is concealed».", "«gizlenir»."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("فَاعِلُهُ", "fail-doer", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its doer».", "«fâili».", punct="،", segments=[seg("فَاعِلُ", "fail-doer", "noun"), pr3ms()]),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«nor».", "«ve ne de».", "لَا"),
  W("يَلْزَمُ", "lazima", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is necessary».", "«lâzım gelir»."),
  W("ذِكْرُهُ", "dhikr", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its mention».", "«zikri».", segments=[seg("ذِكْرُ", "dhikr", "noun"), pr3ms()]),
  nahwu(),
  ajabani(),
  W("ضَرْبٌ", "darb", "noun", ["fail", MN, "imal-al-masdar"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرٌ بِلَا فَاعِلٍ مَذْكُورٍ.", "«a striking» — no doer named.", "«bir vurma» — fâili zikredilmemiş."),
  masdar_obj("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd'i» — mef'ûlü.", punct="."),
 ]})

# ----------- s7 (RESTORED): annexed to the doer or the object
S.append({"id": "s7", "translation": {
 "en": "And it is annexed to its doer, as in وَلَوْلَا دَفْعُ اللهِ النَّاسَ, and to its object, as in ضَرْبُ اللِّصِّ الْجَلَّادُ." + R_EN,
 "tr": "Fâiline muzâf olur, وَلَوْلَا دَفْعُ اللهِ النَّاسَ (âyeti) gibi; mef'ûlüne de muzâf olur, ضَرْبُ اللِّصِّ الْجَلَّادُ gibi." + R_TR},
 "tokens": [
  atf_wa("وَيُضَافُ", "adafa", "verb", ["naib-al-fail", "form-iv-verbs", "hollow-verbs"], "يُضَافُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«and it is annexed».", "«ve muzâf olur».", "يُضَافُ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("فَاعِلِهِ", "fail-doer", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its doer».", "«fâiline».", segments=[seg("فَاعِلِ", "fail-doer", "noun"), pr3msi()]),
  nahwu(),
  cited_wa("وَلَوْلَا", "lawla", "part", ["hadhf-wa-taqdir"], "لَوْلَا حَرْفُ امْتِنَاعٍ لِوُجُودٍ.", "«and were it not for».", "«ve olmasaydı».", "لَوْلَا"),
  W("دَفْعُ", "daf-repel", "noun", ["mubtada-khabar", "idafa-definiteness", MN, "imal-al-masdar", "hadhf-wa-taqdir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ، وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا.", "«the repelling of» — the mubtada; its khabar never said.", "«def'i» — mübtedâ; haberi hiç söylenmez."),
  W("اللهِ", "allah", "propn", ["idafa-definiteness", "imal-al-masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلُ الْمَصْدَرِ.", "«God» — the maṣdar's doer.", "«Allah'ın» — masdarın fâili."),
  W("النَّاسَ", "nas", "noun", ["maful-bihi", "imal-al-masdar"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", "«the people» — its object.", "«insanları» — mef'ûlü.", punct="،"),
  atf_wa("وَإِلَى", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ.", "«and to».", "«ve -e».", "إِلَى"),
  W("مَفْعُولِهِ", "maful-object", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its object».", "«mef'ûlüne».", segments=[seg("مَفْعُولِ", "maful-object", "noun"), pr3msi()]),
  nahwu(),
  cited("ضَرْبُ", "darb", "noun", ["mubtada-khabar", "idafa-definiteness", MN, "imal-al-masdar"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the striking of».", "«vurması»."),
  W("اللِّصِّ", "liss", "noun", ["idafa-definiteness", "imal-al-masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَفْعُولُ الْمَصْدَرِ.", "«the thief» — the maṣdar's object.", "«hırsızı» — masdarın mef'ûlü."),
  W("الْجَلَّادُ", "jallad", "noun", ["fail", "imal-al-masdar", "sighat-mubalagha"], "فَاعِلُ الْمَصْدَرِ مَرْفُوعٌ — وَالْخَبَرُ مَحْذُوفٌ.", "«the executioner» — its doer.", "«cellât» — fâili.", punct="."),
 ]})

# ----------- s8 (RESTORED): the al-maṣdar
S.append({"id": "s8", "translation": {
 "en": "And making the maṣdar defined by the lām govern is rare — as in لَا يُحِبُّ اللهُ الْجَهْرَ بِالسُّوءِ, where بِالسُّوءِ is the indirect object of الْجَهْرَ." + R_EN,
 "tr": "Lâm ile ma'rife olan masdara amel ettirmek azdır — لَا يُحِبُّ اللهُ الْجَهْرَ بِالسُّوءِ gibi: بِالسُّوءِ, الْجَهْرَ'nin gayr-i sarîh mef'ûlüdür." + R_TR},
 "tokens": [
  atf_wa("وَإِعْمَالُ", "imal", "noun", ["mubtada-khabar", "idafa-definiteness", MN], "إِعْمَالُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and making … govern» — the mubtada.", "«ve amel ettirmek» — mübtedâ.", "إِعْمَالُ"),
  W("الْمَصْدَرِ", "masdar-noun", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the maṣdar».", "«masdara»."),
  W("الْمُعَرَّفِ", "muarraf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«defined».", "«ma'rife olan»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", [], "اللَّامِ مَجْرُورٌ.", "«by the lām».", "«lâm ile».", "اللَّامِ"),
  W("قَلِيلٌ", "qalil", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is rare».", "«azdır».", punct="،"),
  nahwu(),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«not».", "«-mez»."),
  W("يُحِبُّ", "ahabba", "verb", ["fail", "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«loves».", "«sever»."),
  W("اللهُ", "allah", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«God».", "«Allah»."),
  W("الْجَهْرَ", "jahr", "noun", ["maful-bihi", MN, "imal-al-masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَصْدَرٌ مُعَرَّفٌ بِاللَّامِ عَامِلٌ.", "«the uttering aloud» — an al-maṣdar that governs.", "«açığa vurmayı» — amel eden lâmlı masdar."),
  bi_("بِالسُّوءِ", "su", "noun", ["imal-al-masdar"], "السُّوءِ مَجْرُورٌ — مُتَعَلِّقٌ بِالْجَهْرِ.", "«of evil».", "«kötülüğü».", "السُّوءِ", punct="،"),
  W("فَبِالسُّوءِ", "su", "noun", ["mubtada-khabar", "huruf-jarr"], "الْفَاءُ لِلتَّفْرِيعِ، وَبِالسُّوءِ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«so بِالسُّوءِ» — the mubtada.", "«o hâlde بِالسُّوءِ» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("بِ", "bi", "prep"), seg("السُّوءِ", "su", "noun")]),
  W("مَفْعُولٌ", "maful-object", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is the object».", "«mef'ûldür»."),
  W("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«(direct)».", "«bih».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("غَيْرُ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ مَرْفُوعَةٌ، وَهُوَ مُضَافٌ.", "«not».", "«gayr-i»."),
  W("صَرِيحٍ", "sarih", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«explicit».", "«sarîh»."),
  li_("لِلْجَهْرِ", "jahr", "noun", [], "الْجَهْرِ مَجْرُورٌ.", "«of الْجَهْرَ».", "«el-cehr'in».", "الْجَهْرِ", punct=".", segs=[seg("لِ", "li", "prep"), seg("لْجَهْرِ", "jahr", "noun")]),
 ]})

# ----------- s9 (COMMENTARY): the maf'ul mutlaq
S.append({"id": "s9", "translation": {
 "en": "And when it is an absolute object the government belongs to the verb — as in ضَرَبْتُ ضَرْبًا زَيْدًا: زَيْدًا is the object of ضَرَبْتُ, not of ضَرْبًا." + C_EN,
 "tr": "Mef'ûl-i mutlak olduğunda amel fiilindir — ضَرَبْتُ ضَرْبًا زَيْدًا gibi: زَيْدًا, ضَرْبًا'nın değil ضَرَبْتُ'nün mef'ûlüdür." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["al-majzum-wal-shart-wal-jaza", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve -dığında».", "إِذَا"),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "«it is».", "«olursa»."),
  W("مَفْعُولًا", "maful-object", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«an object».", "«mef'ûl»."),
  W("مُطْلَقًا", "mutlaq", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«absolute».", "«mutlak»."),
  W("فَالْعَمَلُ", "amal-work", "noun", ["mubtada-khabar", "al-majzum-wal-shart-wal-jaza"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَالْعَمَلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«then the government».", "«amel».", segments=[seg("فَ", "fa", "conj"), seg("الْعَمَلُ", "amal-work", "noun")]),
  li_("لِلْفِعْلِ", "fil", "noun", ["mubtada-khabar"], "الْفِعْلِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«belongs to the verb» — the khabar.", "«fiilindir» — haber.", "الْفِعْلِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لْفِعْلِ", "fil", "noun")]),
  nahwu(),
  cited("ضَرَبْتُ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck».", "«vurdum».", segments=[seg("ضَرَبْ", "daraba", "verb"), prT()]),
  W("ضَرْبًا", "darb", "noun", ["maful-mutlaq", MN], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — لَا يَعْمَلُ.", "«a striking» — governs nothing.", "«bir vurma» — amel etmez."),
  W("زَيْدًا", "zayd", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ لِلْفِعْلِ ضَرَبْتُ مَنْصُوبٌ.", "«Zayd» — the verb's object.", "«Zeyd'i» — fiilin mef'ûlü.", punct=":"),
  cited("زَيْدًا", "zayd", "propn", ["mubtada-khabar"], "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«زَيْدًا» — the mubtada.", "«زَيْدًا» — mübtedâ."),
  W("مَفْعُولُ", "maful-object", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the object of».", "«mef'ûlüdür»."),
  cited("ضَرَبْتُ", "daraba", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«ضَرَبْتُ».", "«ضَرَبْتُ'nün».", segments=[seg("ضَرَبْ", "daraba", "verb"), prT()]),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«değil»."),
  W("مَفْعُولُ", "maful-object", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the object of».", "«mef'ûlü»."),
  cited("ضَرْبًا", "darb", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«ضَرْبًا».", "«ضَرْبًا'nın».", punct="."),
 ]})

# ----------- s10 (COMMENTARY): سَقْيًا زَيْدًا
S.append({"id": "s10", "translation": {
 "en": "And if it stands in place of a verb deleted of necessity, as in سَقْيًا زَيْدًا, there are two views: the government is the deleted verb's, since it is the origin — or the maṣdar's, since it stands in the verb's place." + C_EN,
 "tr": "Vücûben hazfedilmiş bir fiilin yerine geçmişse, سَقْيًا زَيْدًا gibi, iki vecih vardır: amel, asıl olduğundan mahzûf fiilindir — veya fiilin makamına kâim olduğundan masdarındır." + C_TR},
 "tokens": [
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["al-majzum-wal-shart-wal-jaza", "nawasib-wa-jawazim-al-mudari"], "إِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«ve eğer».", "إِنْ"),
  W("كَانَ", "kana", "verb", ["al-majzum-wal-shart-wal-jaza", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَاسْمُهَا مُسْتَتِرٌ.", "«it is».", "«olursa»."),
  W("بَدَلًا", "badal", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a substitute».", "«bedel»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  W("فِعْلٍ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«fiil»."),
  W("مَحْذُوفٍ", "mahdhuf", "noun", ["naat-sifa", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«deleted».", "«hazfedilmiş»."),
  W("وُجُوبًا", "wujub", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِعَامِلٍ مَحْذُوفٍ، أَوْ حَالٌ.", "«of necessity».", "«vücûben»."),
  nahwu(),
  cited("سَقْيًا", "saqy", "noun", ["maful-mutlaq", MN, "hadhf-wa-taqdir"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ وُجُوبًا: سَقَيْتُ.", "«a watering» — for the deleted سَقَيْتُ.", "«sulamak» — mahzûf سَقَيْتُ için."),
  W("زَيْدًا", "zayd", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — عَامِلُهُ مُخْتَلَفٌ فِيهِ.", "«Zayd» — its governor disputed.", "«Zeyd'i» — âmili ihtilâflı."),
  W("فَفِيهِ", "fi", "prep", ["al-majzum-wal-shart-wal-jaza", "huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَفِيهِ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«there are in it».", "«onda … vardır».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep"), pr3msi()]),
  W("وَجْهَانِ", "wajh", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two views».", "«iki vecih».", punct=":"),
  W("الْعَمَلُ", "amal-work", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the government».", "«amel»."),
  li_("لِلْفِعْلِ", "fil", "noun", ["mubtada-khabar"], "الْفِعْلِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«belongs to the verb».", "«fiilindir».", "الْفِعْلِ", segs=[seg("لِ", "li", "prep"), seg("لْفِعْلِ", "fil", "noun")]),
  W("الْمَحْذُوفِ", "mahdhuf", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«deleted».", "«mahzûf»."),
  W("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«since it is».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  W("الْأَصْلُ", "asl", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«the origin».", "«asıldır».", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  li_("لِلْمَصْدَرِ", "masdar-noun", "noun", ["atf-nasaq"], "الْمَصْدَرِ مَجْرُورٌ — مَعْطُوفٌ عَلَى لِلْفِعْلِ.", "«the maṣdar's».", "«masdarındır».", "الْمَصْدَرِ", segs=[seg("لِ", "li", "prep"), seg("لْمَصْدَرِ", "masdar-noun", "noun")]),
  li_("لِقِيَامِهِ", "qiyam", "noun", ["idafa-definiteness"], "قِيَامِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — لِلتَّعْلِيلِ.", "«since it stands».", "«kâim olduğundan».", "قِيَامِ", segs=[seg("لِ", "li", "prep"), seg("قِيَامِ", "qiyam", "noun"), pr3msi()]),
  W("مَقَامَهُ", "maqam", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in its place».", "«onun makamına».", punct=".", segments=[seg("مَقَامَ", "maqam", "noun"), pr3ms()]),
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
 "maji": need("maji", "مَجِيء", "ج ي أ", "noun", "coming (maṣdar of جَاءَ)", "gelme (câe'nin masdarı)", 4),
 "jalsa": need("jalsa", "جَلْسَة", "ج ل س", "noun", "one sitting — the maṣdar of number (مَصْدَرُ الْمَرَّةِ) on فَعْلَة", "bir kez oturma — merre masdarı, فَعْلَة vezninde", 4),
 "jilsa": need("jilsa", "جِلْسَة", "ج ل س", "noun", "a manner of sitting — the maṣdar of kind (مَصْدَرُ الْهَيْئَةِ) on فِعْلَة", "oturuş tarzı — hey'et masdarı, فِعْلَة vezninde", 4),
 "istikhraj": need("istikhraj", "اِسْتِخْرَاج", "خ ر ج", "noun", "extraction — the maṣdar of اِسْتَخْرَجَ on اِسْتِفْعَال", "istihrac — istahrece'nin masdarı, اِسْتِفْعَال vezninde", 4),
 "jallad": need("jallad", "جَلَّاد", "ج ل د", "noun", "an executioner, a flogger — an intensive on فَعَّال", "cellât — فَعَّال vezninde mübâlağa", 4),
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
print("kafiya ch15 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْمَصْدَرُ فِي الْكَافِيَةِ", "en": "The maṣdar in the Kafiya: its definition, why it «runs on the verb», heard against ruled, and how it governs — with the five conditions the notebook spells out", "tr": "Kâfiye'de masdar: tarifi, neden «fiil üzerine cereyan eder», semâî ile kıyâsî, ve nasıl amel eder — defterin açtığı beş şartla"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المصدر: اسم الحدث الجاري على الفعل؛ يعمل عمل فعله؛ لا يتقدم معموله عليه ولا يضمر فيه؛ يضاف إلى الفاعل والمفعول؛ إعمال المعرف باللام قليل", "ضياء صونغور اوغلى — دفتر الكافية: معنى الجري على الفعل (التأكيد، العدد، النوع)؛ سماعية الثلاثي (ذكر سيبويه ۳٢)؛ المفعول المطلق لا يعمل؛ سَقْيًا زَيْدًا على وجهين"],
 "question": {
  "en": ["What is a MAṢDAR? The name of the event — the bare «striking», «sitting» — that «runs on the verb»: the verb is derived from it and it follows the verb to confirm it (جَلَسْتُ جُلُوسًا), to count it (جَلْسَةً, once) or to describe it (جِلْسَةً, a manner).",
         "Which maṣdars must be LEARNED? The bare triliteral's: ضَرْب، جُلُوس، سَقْي are heard, not derived (Sībawayh lists thirty-two shapes). Every augmented form's maṣdar follows a rule — أَخْرَجَ → إِخْرَاج, اِسْتَخْرَجَ → اِسْتِخْرَاج — which is why the engine derives those and stores the rest.",
         "When does a maṣdar GOVERN? Whenever it is not itself the absolute object: أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا — ضَرْب takes a doer (زَيْد, in jarr by annexation) and an object (عَمْرًا, in naṣb), yesterday, today or tomorrow.",
         "What may a maṣdar NOT do? Let its governed word precede it (*أَعْجَبَنِي عَمْرًا ضَرْبُ زَيْدٍ is barred) or conceal a doer — a verb always has one, a maṣdar need not: أَعْجَبَنِي ضَرْبٌ زَيْدًا names an object and no doer.",
         "To which is it annexed? To its doer (وَلَوْلَا دَفْعُ اللهِ النَّاسَ — God repels) or to its object (ضَرْبُ اللِّصِّ الْجَلَّادُ — the executioner strikes the thief, who stands in jarr). Only the sense tells which.",
         "Why is ضَرَبْتُ ضَرْبًا زَيْدًا different? There the maṣdar is the absolute object of the verb beside it, and the verb governs everything; the maṣdar is a passenger. In سَقْيًا زَيْدًا the verb is deleted, so the schools split over whether the ghost verb or the maṣdar standing in for it governs زَيْدًا.",
         "What does the engine do? The HadhfEngine restores سَقَيْتُ behind سَقْيًا and the TaalluqEngine hangs بِالسُّوءِ on الْجَهْرَ because the glossary marks it a maṣdar — the «verbal» flag that lets a noun on فَعْل be a governor."],
  "tr": ["MASDAR nedir? Hadesin (olayın) adı — yalın «vurma», «oturma» — «fiil üzerine cereyan eden»: fiil ondan türer, o da fiilin ardından onu tekit (جَلَسْتُ جُلُوسًا), sayısını (جَلْسَةً, bir kez) veya tarzını (جِلْسَةً) bildirmek için gelir.",
         "Hangi masdarlar EZBERLENİR? Sülâsî mücerredinkiler: ضَرْب، جُلُوس، سَقْي semâîdir, türetilmez (Sîbeveyh otuz iki biçim sayar). Mezîd bâbların masdarı kurala bağlıdır — أَخْرَجَ → إِخْرَاج, اِسْتَخْرَجَ → اِسْتِخْرَاج — motorun onları türetip ötekileri saklamasının sebebi budur.",
         "Masdar ne zaman AMEL EDER? Kendisi mef'ûl-i mutlak olmadığı her zaman: أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا — ضَرْب bir fâil (زَيْد, izâfetle mecrûr) ve bir mef'ûl (عَمْرًا, mansûb) alır; dün, bugün ya da yarın.",
         "Masdar neyi YAPAMAZ? Ma'mûlünü önüne alamaz (*أَعْجَبَنِي عَمْرًا ضَرْبُ زَيْدٍ memnûdur) ve fâil gizleyemez — fiilin fâili hep vardır, masdarın olmayabilir: أَعْجَبَنِي ضَرْبٌ زَيْدًا bir mef'ûl söyler, fâil söylemez.",
         "Neye muzâf olur? Fâiline (وَلَوْلَا دَفْعُ اللهِ النَّاسَ — def' eden Allah'tır) veya mef'ûlüne (ضَرْبُ اللِّصِّ الْجَلَّادُ — cellât hırsızı vurur, hırsız mecrûrdur). Hangisi olduğunu yalnız mânâ söyler.",
         "ضَرَبْتُ ضَرْبًا زَيْدًا neden farklıdır? Orada masdar yanındaki fiilin mef'ûl-i mutlakıdır ve her şeyi fiil yönetir; masdar yolcudur. سَقْيًا زَيْدًا'da fiil hazfedilmiştir, bu yüzden زَيْدًا'yı gizli fiilin mi yoksa onun yerine geçen masdarın mı yönettiği ihtilâflıdır.",
         "Motor ne yapar? HadhfEngine سَقْيًا'nın ardındaki سَقَيْتُ'yü geri getirir; TaalluqEngine بِالسُّوءِ'yi الْجَهْرَ'ye bağlar, çünkü sözlük onu masdar diye işaretler — فَعْل veznindeki bir ismin âmil olmasına izin veren «verbal» bayrağı."]},
 "plain": {
  "en": "A maṣdar is the bare name of an action (ضَرْب «striking»). It can govern like its verb — take a doer and an object — unless it is only echoing a verb beside it. Its doer or its object may be tucked in by annexation, and it never carries a hidden doer.",
  "tr": "Masdar bir işin yalın adıdır (ضَرْب «vurma»). Yanındaki bir fiili yankılamıyorsa fiili gibi amel eder — fâil ve mef'ûl alır. Fâili ya da mef'ûlü izâfetle içine alınabilir ve asla gizli fâil taşımaz."},
 "explanation": {
  "en": "The chapter defines the maṣdar by its relation to the verb and then spends every remaining line on that relation. «Running on the verb» means the maṣdar comes after the verb derived from it, and the notebook's three examples give the three reasons it comes: جُلُوسًا confirms, جَلْسَةً counts (the maṣdar of one occurrence on فَعْلَة), جِلْسَةً describes (the maṣdar of manner on فِعْلَة). Then the division that organises the whole sarf shelf: the bare triliteral's maṣdars are heard — Sībawayh's thirty-two shapes are a list, not a rule — while every augmented form's maṣdar is built on a pattern, إِفْعَال for أَفْعَلَ and اِسْتِفْعَال for اِسْتَفْعَلَ. The governing rules follow. A maṣdar governs exactly as its verb does, in any tense the context supplies (أَمْسِ، غَدًا، الْآنَ), on one condition: it must not itself be the absolute object, for then the verb beside it does all the work. It differs from the verb in two ways the notebook makes explicit: its governed word may never stand in front of it, and it never hides a doer — a verb must have one, a maṣdar may do without (أَعْجَبَنِي ضَرْبٌ زَيْدًا). Annexation takes its doer (دَفْعُ اللهِ) or its object (ضَرْبُ اللِّصِّ); the al-maṣdar governs only rarely, and the Qurʾān's الْجَهْرَ بِالسُّوءِ is the received instance. The chapter closes on the two readings of سَقْيًا زَيْدًا, where a deleted verb and the maṣdar that replaced it both have a claim on the object — kept as two views because the books keep them so.",
  "tr": "Bâb masdarı fiille ilişkisi üzerinden tarif eder ve kalan her satırı o ilişkiye harcar. «Fiil üzerine cereyan etmek» masdarın kendisinden türeyen fiilin ardından gelmesidir; defterin üç örneği gelişinin üç sebebini verir: جُلُوسًا tekit eder, جَلْسَةً sayar (فَعْلَة veznindeki merre masdarı), جِلْسَةً tarz bildirir (فِعْلَة veznindeki hey'et masdarı). Sonra bütün sarf rafını düzenleyen taksim: sülâsî mücerredin masdarları semâîdir — Sîbeveyh'in otuz iki biçimi bir listedir, kural değil — mezîd bâbların masdarı ise bir kalıba kurulur, أَفْعَلَ için إِفْعَال, اِسْتَفْعَلَ için اِسْتِفْعَال. Amel kuralları izler. Masdar, bağlamın verdiği her zamanda (أَمْسِ، غَدًا، الْآنَ) tam fiili gibi amel eder; tek şartla: kendisi mef'ûl-i mutlak olmamalıdır, çünkü o zaman bütün işi yanındaki fiil görür. Fiilden defterin açıkça söylediği iki yönde ayrılır: ma'mûlü asla önüne geçemez ve asla fâil gizlemez — fiilin fâili olmak zorundadır, masdar onsuz olabilir (أَعْجَبَنِي ضَرْبٌ زَيْدًا). İzâfet fâilini (دَفْعُ اللهِ) ya da mef'ûlünü (ضَرْبُ اللِّصِّ) alır; lâmlı masdar nadiren amel eder ve Kur'ân'ın الْجَهْرَ بِالسُّوءِ'si alınan örnektir. Bâb, hazfedilmiş fiil ile onun yerine geçen masdarın ikisinin de mef'ûl üzerinde hak iddia ettiği سَقْيًا زَيْدًا'nın iki okunuşuyla kapanır — kitaplar öyle tuttuğu için iki görüş olarak tutulur."},
 "examples": [
  {"ar": "الْمَصْدَرُ: اسْمُ الْحَدَثِ الْجَارِي عَلَى الْفِعْلِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "جَلَسْتُ جُلُوسًا، جَلَسْتُ جَلْسَةً، جِلْسَةً", "en": "Confirmation, number, kind.", "tr": "Tekit, sayı, nevi.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا أَمْسِ", "en": "The maṣdar governs a doer and an object.", "tr": "Masdar fâil ve mef'ûl alır.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "أَعْجَبَنِي ضَرْبٌ زَيْدًا", "en": "An object and no doer.", "tr": "Mef'ûl var, fâil yok.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَلَوْلَا دَفْعُ اللهِ النَّاسَ", "en": "Annexed to the doer.", "tr": "Fâiline muzâf.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "لَا يُحِبُّ اللهُ الْجَهْرَ بِالسُّوءِ", "en": "The al-maṣdar governing, rarely.", "tr": "Lâmlı masdarın nadir ameli.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "سَقْيًا زَيْدًا", "en": "The two views on the deleted verb's maṣdar.", "tr": "Mahzûf fiilin masdarı üzerine iki görüş.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«أَعْجَبَنِي عَمْرًا ضَرْبُ زَيْدٍ»",
   "right": "«أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا — masdarın ma'mûlü ondan önce gelemez»",
   "why": {"en": "A verb's object may be fronted; a maṣdar's may not — the Kafiya states it outright.", "tr": "Fiilin mef'ûlü öne alınabilir; masdarınki alınamaz — Kâfiye bunu açıkça söyler."}},
  {"wrong": "«ضَرَبْتُ ضَرْبًا زَيْدًا — زَيْدًا, ضَرْبًا'nın mef'ûlü»",
   "right": "«زَيْدًا, ضَرَبْتُ'nün mef'ûlüdür; mef'ûl-i mutlak amel etmez»",
   "why": {"en": "When the maṣdar is the absolute object, the verb beside it governs everything.", "tr": "Masdar mef'ûl-i mutlak olunca yanındaki fiil her şeyi yönetir."}},
  {"wrong": "«ضَرْبُ اللِّصِّ الْجَلَّادُ — hırsız cellâdı vurdu»",
   "right": "«cellât hırsızı vurdu: masdar mef'ûlüne muzâf, fâil merfû kaldı»",
   "why": {"en": "The muḍāf ilayh may be the object; the marfūʿ noun that follows is the doer.", "tr": "Muzâfun ileyh mef'ûl olabilir; ardından gelen merfû isim fâildir."}},
  {"wrong": "«جَلْسَةً ve جِلْسَةً aynı masdardır»",
   "right": "«جَلْسَة (فَعْلَة) bir kez; جِلْسَة (فِعْلَة) bir tarz — merre ve hey'et masdarları»",
   "why": {"en": "One vowel on the first letter separates the count from the manner.", "tr": "İlk harfteki tek bir hareke sayıyı tarzdan ayırır."}}],
 "relatedNotes": ["masdar", "maful-mutlaq", "imal-al-masdar", "hadhf-wa-taqdir", "idafa-definiteness", "form-iv-verbs"]}

ADD_EN = (" Chapter 15 (notebook line ~255): the maṣdar defined in the notebook's own Arabic (s1); its running on the verb — confirmation, number, kind — and Sībawayh's count as the notebook's "
          "commentary (s2, s4); the heard and the ruled maṣdars, its government, the two prohibitions, its annexation and the rare al-maṣdar restored from the received matn and marked (s3, s5-s8); "
          "the absolute object and the two views on سَقْيًا زَيْدًا as commentary (s9-s10).")
ADD_TR = (" On beşinci bâb (defter satırı ~255): masdar defterin kendi Arapçasıyla tarif edilir (s1); fiil üzerine cereyanı — tekit, sayı, nevi — ve Sîbeveyh'in sayımı defterin şerhi olarak "
          "(s2, s4); semâî ve kıyâsî masdarlar, ameli, iki yasak, izâfeti ve nadir lâmlı masdar alınan metinden geri yazılmış ve işaretlenmiştir (s3, s5-s8); mef'ûl-i mutlak ve سَقْيًا زَيْدًا "
          "üzerine iki görüş şerh olarak (s9-s10).")
write_out(15, S, TITLE, ADD_EN, ADD_TR, "255", GLOSS_ADD, notes=(NOTE,),
          related=(("masdar", [K]), ("imal-al-masdar", [K]), ("maful-mutlaq", [K])))
report(15, S, GLOSS_ADD, (NOTE,))
