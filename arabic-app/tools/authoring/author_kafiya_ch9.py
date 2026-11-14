# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 9: THE DEFINITE AND THE INDEFINITE. The definite defined, its six kinds, the proper name defined (the notebook's own
Arabic), the ranking of the definites (commentary), and the indefinite defined.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~209-213 of the transcription.

  VERBATIM from the notebook's Arabic: s1 (the definite), s3 (the proper name), s5 (the indefinite) and the examples.
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s2.
  COMMENTARY (the notebook's explanation): s4 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch9.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-marifa-wal-nakira-fil-kafiya"
PRON = "al-marifa-al-mudmarat-wal-alam"
TITLE = {"ar": "الْمَعْرِفَةُ وَالنَّكِرَةُ", "en": "The definite and the indefinite", "tr": "Ma'rife ve nekre"}
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
def defn(head_full, head_lex, head_en, head_tr, rest):
    return [W(head_full, head_lex, "noun", ["mubtada-khabar", K], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", head_en + " — the mubtada.", head_tr + " — mübtedâ.", punct=":"),
            W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
            W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail", "al-mustatir-jawazan"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«is coined» — the ṣila, its deputy the ʿāʾid.", "«konulmuş» — sıla; nâibi âid."),
            li_("لِشَيْءٍ", "shay", "noun", [], "شَيْءٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«for a thing».", "«bir şey için».", "شَيْءٍ")] + rest

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The definite: what is coined for a thing in itself.",
 "tr": "Ma'rife: bir şeye bizzat (muayyen olarak) konulmuş olandır."},
 "tokens": defn("الْمَعْرِفَةُ", "marifa", "«the definite»", "«ma'rife»", [
  W("بِعَيْنِهِ", "ayn-thing", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَعَيْنِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: مُعَيَّنٍ.", "«in itself» — a definite, known thing.", "«bizzat» — muayyen, bilinen bir şey.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("عَيْنِ", "ayn-thing", "noun"), pr3msi()])])})

# ----------- s2 (RESTORED): the six kinds
S.append({"id": "s2", "translation": {
 "en": "And it is six: the pronouns, the proper names, the vague nouns, what is made definite by the lām, what is annexed in meaning to one of these, and the called noun." + R_EN,
 "tr": "Altıdır: zamirler, alemler, mübhemler, lâm ile ma'rife olan, bunlardan birine manen muzâf olan ve münâdâ." + R_TR},
 "tokens": [
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هِيَ"),
  W("سِتَّةٌ", "sitta", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«six» — the khabar.", "«altıdır» — haber.", punct=":"),
  W("الْمُضْمَرَاتُ", "mudmar", "noun", ["badal", "jam-muannath-salim", PRON], "بَدَلٌ مِنْ سِتَّةٌ مَرْفُوعٌ — أَعْرَفُ الْمَعَارِفِ.", "«the pronouns» — the first and most definite.", "«zamirler» — ilki ve en ma'rifesi."),
  atf_wa("وَالْأَعْلَامُ", "alam-name", "noun", ["jam-taksir", PRON], "الْأَعْلَامُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the proper names».", "«ve alemler».", "الْأَعْلَامُ"),
  atf_wa("وَالْمُبْهَمَاتُ", "mubham", "noun", ["jam-muannath-salim", "asma-al-ishara", "ism-mawsul"], "الْمُبْهَمَاتُ مَعْطُوفٌ — أَسْمَاءُ الْإِشَارَةِ وَالْمَوْصُولَاتُ.", "«and the vague nouns» — the demonstratives and the relatives.", "«ve mübhemler» — işaret isimleri ve mevsûller.", "الْمُبْهَمَاتُ"),
  atf_wa("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and what».", "«ve ... olan».", "مَا"),
  W("عُرِّفَ", "arrafa", "verb", ["ism-mawsul", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.", "«is made definite».", "«ma'rife kılınan»."),
  W("بِاللَّامِ", "lam-letter", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّامِ مَجْرُورٌ — لَامُ التَّعْرِيفِ.", "«by the lām» — the article.", "«lâm ile» — harf-i tarif.", segments=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  atf_wa("وَالْمُضَافُ", "mudaf", "noun", ["ism-maful", "idafa-definiteness"], "الْمُضَافُ مَعْطُوفٌ مَرْفُوعٌ.", "«and what is annexed».", "«ve muzâf olan».", "الْمُضَافُ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("أَحَدِهَا", "ahad", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهَا مُضَافٌ إِلَيْهِ — إِلَى أَحَدِ الْخَمْسَةِ.", "«one of them» — one of the five.", "«bunlardan birine» — beşten birine.", segments=[seg("أَحَدِ", "ahad", "noun"), pr3fs()]),
  W("مَعْنًى", "mana", "noun", ["tamyiz", "ism-maqsur-manqus", "idafa-definiteness"], "تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — إِضَافَةً مَعْنَوِيَّةً لَا لَفْظِيَّةً.", "«in meaning» — a real annexation, not a merely formal one.", "«manen» — lafzî değil manevî izâfetle.", punct="،"),
  atf_wa("وَالْمُنَادَى", "munada", "noun", ["vocative-munada", "ism-maful"], "الْمُنَادَى مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the called noun».", "«ve münâdâ».", "الْمُنَادَى", punct="."),
 ]})

# ----------- s3 (VERBATIM): the proper name
S.append({"id": "s3", "translation": {
 "en": "The proper name: what is coined for a thing in itself without reaching another by a single coinage — as in Zayd, ʿAmr and Bakr.",
 "tr": "Alem: tek bir vaz' ile başkasını kapsamaksızın bir şeye bizzat konulmuş olandır — Zeyd, Amr ve Bekir gibi."},
 "tokens": defn("الْعَلَمُ", "alam-name", "«the proper name»", "«alem»", [
  W("بِعَيْنِهِ", "ayn-thing", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَعَيْنِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in itself».", "«bizzat».", segments=[seg("بِ", "bi", "prep"), seg("عَيْنِ", "ayn-thing", "noun"), pr3msi()]),
  W("غَيْرَ", "ghayr", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«without» — the ḥāl.", "«-maksızın» — hâl."),
  W("مُتَنَاوِلٍ", "mutanawil", "noun", ["idafa-definiteness", "ism-fail", "form-vi-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ تَنَاوَلَ.", "«reaching» — the participle of تَنَاوَلَ.", "«kapsayan» — tenâvele'nin ism-i fâili."),
  W("غَيْرَهُ", "ghayr", "noun", ["maful-bihi", "idafa-definiteness", "ism-fail"], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another» — the participle's object.", "«başkasını» — ism-i fâilin mef'ûlü.", segments=[seg("غَيْرَ", "ghayr", "noun"), pr3ms()]),
  W("بِوَضْعٍ", "wad-put", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَوَضْعٍ مَجْرُورٌ.", "«by a coinage».", "«bir vaz' ile».", segments=[seg("بِ", "bi", "prep"), seg("وَضْعٍ", "wad-put", "noun")]),
  W("وَاحِدٍ", "wahid", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ — فَرْقُهُ عَنِ الْمُشْتَرَكِ وَالْمُضْمَرِ.", "«single» — what parts it from a homonym and from a pronoun.", "«tek» — onu müşterekten ve zamirden ayıran.", punct="،"),
  nahwu(),
  W("زَيْدٌ", "zayd", "propn", ["idafa-definiteness", PRON], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — عَلَمٌ.", "«Zayd».", "«Zeyd»."),
  atf_wa("وَعَمْرٌو", "amr-name", "propn", [PRON], "عَمْرٌو مَعْطُوفٌ، وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ.", "«and ʿAmr».", "«ve Amr».", "عَمْرٌو"),
  atf_wa("وَبَكْرٌ", "bakr", "propn", [PRON], "بَكْرٌ مَعْطُوفٌ.", "«and Bakr».", "«ve Bekir».", "بَكْرٌ", punct=".")])})

# ----------- s4 (COMMENTARY)
S.append({"id": "s4", "translation": {
 "en": "And the most definite of the definites is the speaker's pronoun, then the addressee's, because the chance of confusion in them is least." + C_EN,
 "tr": "Ma'rifelerin en ma'rifesi mütekellim zamiri, sonra muhâtab zamiridir; çünkü onlarda karışma ihtimali en azdır." + C_TR},
 "tokens": [
  atf_wa("وَأَعْرَفُ", "arafu", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-tafdil"], "أَعْرَفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the most definite of» — the mubtada.", "«ve en ma'rifesi» — mübtedâ.", "أَعْرَفُ"),
  W("الْمَعَارِفِ", "marifa", "noun", ["idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، جُرَّتْ بِالْكَسْرَةِ لِأَجْلِ ال.", "«the definites» — a diptote plural, kasra because of the article.", "«ma'rifelerin» — müntehe'l-cumû'; el aldığı için kesre."),
  W("ضَمِيرُ", "damir", "noun", ["mubtada-khabar", "idafa-definiteness", PRON], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the pronoun of» — the khabar.", "«zamiri» — haber."),
  W("الْمُتَكَلِّمِ", "mutakallim", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker».", "«mütekellim»."),
  W("ثُمَّ", "thumma", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.", "«then».", "«sonra»."),
  W("الْمُخَاطَبِ", "mukhatab", "noun", ["atf-nasaq", "ism-maful"], "مَعْطُوفٌ عَلَى الْمُتَكَلِّمِ مَجْرُورٌ.", "«the addressee's».", "«muhâtabınki».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("احْتِمَالَ", "ihtimal", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar", "form-viii-verbs"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the chance of» — the ism of أَنَّ.", "«ihtimali» — enne'nin ismi."),
  W("الِالْتِبَاسِ", "iltibas", "noun", ["idafa-definiteness", "masdar", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«confusion».", "«karışma»."),
  W("فِيهِمَا", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ.", "«in them».", "«onlarda».", segments=[seg("فِي", "fi", "prep"), seg("هِمَا", "pron-3d", "pron")]),
  W("أَقَلُّ", "aqall", "noun", ["inna-wa-akhawatuha", "ism-tafdil"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is least» — the khabar of أَنَّ.", "«en azdır» — enne'nin haberi.", punct="."),
 ]})

# ----------- s5 (VERBATIM): the indefinite
S.append({"id": "s5", "translation": {
 "en": "The indefinite: what is coined for a thing not in itself — as in «a man» and «a woman».",
 "tr": "Nekre: bir şeye bizzat (muayyen olarak) konulmamış olandır — «bir adam» ve «bir kadın» gibi."},
 "tokens": defn("النَّكِرَةُ", "nakira", "«the indefinite»", "«nekre»", [
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«... olmayan»."),
  W("بِعَيْنِهِ", "ayn-thing", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَعَيْنِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in itself».", "«bizzat».", punct="،", segments=[seg("بِ", "bi", "prep"), seg("عَيْنِ", "ayn-thing", "noun"), pr3msi()]),
  nahwu(),
  W("رَجُلٌ", "rajul", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — نَكِرَةٌ بِالتَّنْوِينِ.", "«a man» — indefinite, with the tanwīn.", "«bir adam» — tenvinle nekre."),
  atf_wa("وَامْرَأَةٌ", "imraa", "noun", [], "امْرَأَةٌ مَعْطُوفٌ.", "«and a woman».", "«ve bir kadın».", "امْرَأَةٌ", punct=".")])})

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
 "mutanawil": need("mutanawil", "مُتَنَاوِل", "ن و ل", "noun", "reaching, taking in (ism fa'il of Form VI تَنَاوَلَ) — غَيْرَ مُتَنَاوِلٍ غَيْرَهُ: not covering another", "kapsayan, alan (tenâvele'nin ism-i fâili) — gayra mütenâvilin gayrahû: başkasını kapsamayan", 5),
 "iltibas": need("iltibas", "الْتِبَاس", "ل ب س", "noun", "confusion, ambiguity (masdar of Form VIII الْتَبَسَ)", "karışma, iltibas (iltebese'nin masdarı)", 4),
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
print("kafiya ch9 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْمَعْرِفَةُ وَالنَّكِرَةُ فِي الْكَافِيَةِ", "en": "The definite and the indefinite in the Kafiya: the six kinds of definite, the proper name's definition, the ranking of the definites", "tr": "Kâfiye'de ma'rife ve nekre: ma'rifenin altı nev'i, alemin tarifi, ma'rifelerin sıralanışı"},
 "level": 3, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المعرفة: ما وضع لشيء بعينه، وهي ستة؛ العلم: ما وضع لشيء بعينه غير متناول غيره بوضع واحد؛ النكرة: ما وضع لشيء لا بعينه", "ضياء صونغور اوغلى — دفتر الكافية: التعريفات الثلاثة بلفظها، أعرف المعارف المتكلم ثم المخاطب"],
 "question": {
  "en": ["What is a DEFINITE noun? One coined for a thing in itself — a known, particular thing. Six kinds: the pronouns, the proper names, the vague nouns (demonstratives and relatives), the noun with the article, the noun annexed in meaning to one of these, and the called noun.",
         "What is a PROPER NAME? Coined for a thing in itself — like the definite — AND reaching no other thing by that one coinage: Zayd names this man and no one else by the same act of naming (a homonym is two coinages; a pronoun covers everyone by one).",
         "Which definite is strongest? The notebook: the speaker's pronoun, then the addressee's — the two in which confusion is least possible; the absent pronoun and the rest follow.",
         "What is an INDEFINITE noun? Coined for a thing not in itself — رَجُلٌ, any man; marked by the tanwīn where the definite wears the article.",
         "Why «annexed in meaning»? Because only a real annexation (غُلَامُ زَيْدٍ) passes definiteness on; a formal one (ضَارِبُ زَيْدٍ, a participle governing its object) leaves the head indefinite.",
         "What does the engine read? The DabtEngine's definiteness test — the article, the annexation to a definite, the proper name, the pronoun — is this list; the Kafiya's six kinds are the IdafaEngine's and the NidaEngine's shared vocabulary."],
  "tr": ["MA'RİFE nedir? Bir şeye bizzat — bilinen, belirli bir şeye — konulmuş isim. Altı nev'i: zamirler, alemler, mübhemler (işaret isimleri ve mevsûller), lâmlı isim, bunlardan birine manen muzâf olan isim ve münâdâ.",
         "ALEM nedir? Ma'rife gibi bir şeye bizzat konulmuş VE o tek vaz' ile başkasına ulaşmayan: Zeyd aynı adlandırma ile yalnız bu adamı adlandırır (müşterek iki vaz'dır; zamir tek vaz' ile herkesi kapsar).",
         "En kuvvetli ma'rife hangisi? Defter: mütekellim zamiri, sonra muhâtab zamiri — karışmanın en az mümkün olduğu ikisi; gâib zamiri ve gerisi onları izler.",
         "NEKRE nedir? Bir şeye bizzat konulmamış olan — رَجُلٌ, herhangi bir adam; ma'rifenin lâm giydiği yerde tenvin taşır.",
         "Neden «manen muzâf»? Çünkü yalnız gerçek izâfet (غُلَامُ زَيْدٍ) ma'rifeliği geçirir; lafzî izâfet (ضَارِبُ زَيْدٍ, mef'ûlünü yöneten ism-i fâil) başı nekre bırakır.",
         "Motor neyi okur? DabtEngine'in ma'rifelik testi — lâm, ma'rifeye izâfet, alem, zamir — bu listedir; Kâfiye'nin altı nev'i IdafaEngine ile NidaEngine'in ortak sözlüğüdür."]},
 "plain": {
  "en": "A definite noun points at a particular thing (I, Zayd, this, the man, Zayd's servant, O man!); an indefinite one at any member of a kind (a man). A proper name is the definite that names one thing and nothing else by a single act of naming.",
  "tr": "Ma'rife belirli bir şeyi gösterir (ben, Zeyd, bu, adam, Zeyd'in kölesi, ey adam!); nekre bir cinsin herhangi bir ferdini (bir adam). Alem, tek bir adlandırma ile bir şeyi ve başka hiçbir şeyi adlandıran ma'rifedir."},
 "explanation": {
  "en": "The Kafiya's three definitions are built on one word, بِعَيْنِهِ, «in itself»: the definite is coined for a thing taken as itself, the indefinite for a thing not taken as itself, and the proper name is the definite with one more clause — the coinage reaches nothing else. That last clause is what separates Zayd from the two neighbours it could be confused with: a shared name like عَيْن (eye, spring) is many coinages, one per meaning, so each is still a proper coinage for its thing; a pronoun like أَنَا is one coinage that every speaker uses of himself, so it reaches everyone. The six kinds are listed in the order the grammarians rank them, and the notebook adds the ranking's reason: definiteness is the absence of possible confusion, and the speaker and the addressee are present to the hearing, so their pronouns are the most definite of all. The sixth kind, the called noun, is definite by the call itself (يَا رَجُلُ), which is why it is built on the ḍamma in the vocative chapter; and «annexed in meaning» excludes the formal annexation of a participle to its object, which carries no definiteness across.",
  "tr": "Kâfiye'nin üç tarifi tek kelime üzerine kuruludur, بِعَيْنِهِ, «bizzat»: ma'rife bizzat alınan bir şeye, nekre bizzat alınmayan bir şeye konulmuştur; alem ise bir kayıt daha taşıyan ma'rifedir — vaz' başka hiçbir şeye ulaşmaz. Bu son kayıt Zeyd'i karıştırılabileceği iki komşusundan ayırır: عَيْن (göz, pınar) gibi müşterek bir ad her mana için ayrı birer vaz'dır, dolayısıyla her biri kendi şeyi için hâlâ bir vaz'dır; أَنَا gibi bir zamir her konuşanın kendisi için kullandığı tek bir vaz'dır, dolayısıyla herkese ulaşır. Altı nev', nahivcilerin sıraladığı sırayla sayılır ve defter sıranın gerekçesini ekler: ma'rifelik, karışma ihtimalinin yokluğudur; mütekellim ile muhâtab işitene hâzırdır, bu yüzden zamirleri en ma'rifedir. Altıncı nev', münâdâ, nidânın kendisiyle ma'rifedir (يَا رَجُلُ); nidâ bâbında damme üzere mebnî olması bu yüzdendir; «manen muzâf» ise ism-i fâilin mef'ûlüne lafzî izâfetini dışarıda bırakır, çünkü o ma'rifelik geçirmez."},
 "examples": [
  {"ar": "الْمَعْرِفَةُ: مَا وُضِعَ لِشَيْءٍ بِعَيْنِهِ", "en": "The definite defined.", "tr": "Ma'rifenin tarifi.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "الْمُضْمَرَاتُ وَالْأَعْلَامُ وَالْمُبْهَمَاتُ وَمَا عُرِّفَ بِاللَّامِ وَالْمُضَافُ إِلَى أَحَدِهَا مَعْنًى وَالْمُنَادَى", "en": "The six kinds.", "tr": "Altı nev'.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "الْعَلَمُ: مَا وُضِعَ لِشَيْءٍ بِعَيْنِهِ غَيْرَ مُتَنَاوِلٍ غَيْرَهُ بِوَضْعٍ وَاحِدٍ", "en": "The proper name defined.", "tr": "Alemin tarifi.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "أَعْرَفُ الْمَعَارِفِ ضَمِيرُ الْمُتَكَلِّمِ ثُمَّ الْمُخَاطَبِ", "en": "The ranking.", "tr": "Sıralama.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "النَّكِرَةُ: مَا وُضِعَ لِشَيْءٍ لَا بِعَيْنِهِ، نَحْوُ رَجُلٌ وَامْرَأَةٌ", "en": "The indefinite defined.", "tr": "Nekrenin tarifi.", "sourceStory": "al-kafiya", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«ضَارِبُ زَيْدٍ ma'rifedir, çünkü ma'rifeye muzâftır»",
   "right": "«ضَارِبُ زَيْدٍ nekredir: izâfet lafzîdir (ism-i fâil mef'ûlüne muzâf); yalnız manevî izâfet ma'rife kılar»",
   "why": {"en": "The Kafiya says «annexed in meaning» on purpose; the formal annexation of a working participle passes no definiteness.", "tr": "Kâfiye bile bile «manen muzâf» der; amel eden ism-i fâilin lafzî izâfeti ma'rifelik geçirmez."}},
  {"wrong": "«عَيْن (göz/pınar) alem değildir, çünkü iki şeye konulmuştur»",
   "right": "«عَيْن müşterektir: her manaya ayrı bir vaz'; alem olmamasının sebebi cins ismi olmasıdır, iki vaz'ı değil»",
   "why": {"en": "The definition's «by a single coinage» excludes a pronoun's one-coinage-for-all, not a homonym's several coinages.", "tr": "Tarifteki «tek bir vaz' ile», bir zamirin herkes için tek vaz'ını dışlar, müşterekin birkaç vaz'ını değil."}},
  {"wrong": "«يَا رَجُلُ — racülü nekredir, tenvinsiz söylenmiştir»",
   "right": "«يَا رَجُلُ — münâdâ nidâ ile ma'rife olur; bu yüzden damme üzere mebnîdir, tenvin almaz»",
   "why": {"en": "The called noun is the sixth kind of definite; the loss of tanwīn is the sign of it.", "tr": "Münâdâ ma'rifenin altıncı nev'idir; tenvinin düşmesi bunun alâmetidir."}}],
 "relatedNotes": [PRON, "idafa-definiteness", "vocative-munada", "asma-al-ishara", "ism-mawsul", "al-kalima-wal-kalam"]}

ADD_EN = (" Chapter 9 (notebook lines ~209-213): the definite, the proper name and the indefinite in the notebook's own Arabic (s1, s3, s5) with its examples; the six "
          "kinds restored from the received matn and marked (s2); the notebook's ranking of the definites as commentary (s4).")
ADD_TR = (" Dokuzuncu bâb (defter satırları ~209-213): ma'rife, alem ve nekre defterin kendi Arapçasıyla (s1, s3, s5) ve örnekleriyle; altı nev' alınan metinden geri yazılmış "
          "ve işaretlenmiştir (s2); defterin ma'rifeleri sıralayışı şerh olarak (s4).")
write_out(9, S, TITLE, ADD_EN, ADD_TR, "209-213", GLOSS_ADD, notes=(NOTE,),
          related=((PRON, [K]), ("idafa-definiteness", [K]), ("vocative-munada", [K])))
report(9, S, GLOSS_ADD, (NOTE,))
