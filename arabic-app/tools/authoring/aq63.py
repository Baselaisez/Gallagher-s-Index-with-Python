# -*- coding: utf-8 -*-
"""Wave 63 — the Nasafi matn continued (aqaid-ahl-al-sunna ch25+). Builders over aqaid_common so a chapter script stays short:
every builder returns a token with a full Arabic i'rab line and EN/TR glosses; the Arabic i'rab is the madrasah wording."""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
from aqaid_common import *
import aqaid_common as _ac
import sarf_gen as _sg
PKG = _ac.PKG
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
def N(s): return unicodedata.normalize("NFC", s)
def need(k, *a, **kw): return None if k in TG else G(k, *a, **kw)
CASE_AR = {"raf": "الرَّفْعِ", "nasb": "النَّصْبِ", "jarr": "الْجَرِّ"}
SIGN_AR = {"raf": "الضَّمَّةُ", "nasb": "الْفَتْحَةُ", "jarr": "الْكَسْرَةُ"}
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, list(tags), ar, en, tr, punct=punct, segments=segments)
def _wa(kind):
    return {"atf": "الْوَاوُ عَاطِفَةٌ، وَ", "isti": "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "hal": "الْوَاوُ حَالِيَّةٌ، وَ",
            "fa-tafsil": "الْفَاءُ لِلتَّفْصِيلِ، وَ", "fa-isti": "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ", "fa-sabab": "الْفَاءُ لِلسَّبَبِيَّةِ، وَ",
            "fa-jawab": "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ", "fa-khabar": "الْفَاءُ دَاخِلَةٌ فِي خَبَرِ الْمُبْتَدَإِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ، وَ", None: ""}[kind]
def _segs(full, lex, pos, wa):
    if not wa: return None
    letter = full[0]; rest = full[2:] if full[1] in "َُِْ" else full[1:]
    return [seg(full[:2] if full[1] in "َُِْ" else letter, "wa" if letter == "و" else "fa", "conj"), seg(rest, lex, pos)]
def MUB(full, lex, en, tr, tags=(), punct=None, wa=None, mudaf=False, pos="noun", extra=""):
    ar = _wa(wa) + "مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + extra + "."
    t = ["mubtada-khabar"] + (["atf-nasaq"] if wa in ("atf",) else []) + (["idafa-definiteness"] if mudaf else []) + list(tags)
    return W(full, lex, pos, t, ar, en, tr, punct=punct, segments=_segs(full, lex, pos, wa))
def KHA(full, lex, en, tr, tags=(), punct=None, mudaf=False, pos="noun", of=None, extra="", wa=None):
    ar = _wa(wa) + "خَبَرٌ" + (f" لِـ«{of}»" if of else "") + " مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + extra + "."
    return W(full, lex, pos, ["mubtada-khabar"] + (["idafa-definiteness"] if mudaf else []) + list(tags), ar, en, tr, punct=punct, segments=_segs(full, lex, pos, wa))
def MUDI(full, lex, en, tr, tags=(), punct=None, mudaf=False, pos="noun", extra="", segs=None):
    ar = "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + extra + "."
    return W(full, lex, pos, ["idafa-definiteness"] + list(tags), ar, en, tr, punct=punct, segments=segs)
def NAT(full, lex, en, tr, of, case, tags=(), punct=None, pos="noun", extra="", wa=None):
    ar = _wa(wa) + f"نَعْتٌ لِـ«{of}» تَابِعٌ لَهُ فِي {CASE_AR[case]}، وَعَلَامَةُ {'رَفْعِهِ' if case=='raf' else 'نَصْبِهِ' if case=='nasb' else 'جَرِّهِ'} {SIGN_AR[case]}" + extra + "."
    return W(full, lex, pos, ["naat-sifa"] + list(tags), ar, en, tr, punct=punct, segments=_segs(full, lex, pos, wa))
def ATF(full, lex, en, tr, of, case, tags=(), punct=None, pos="noun", mudaf=False, extra="", letter="wa", inner=None):
    hur = {"wa": "الْوَاوُ عَاطِفَةٌ", "aw": "«أَوْ» حَرْفُ عَطْفٍ", "thumma": "«ثُمَّ» حَرْفُ عَطْفٍ", "fa": "الْفَاءُ عَاطِفَةٌ"}[letter]
    ar = (hur + "، وَ" if letter in ("wa", "fa") else "") + f"مَعْطُوفٌ عَلَى «{of}» تَابِعٌ لَهُ فِي {CASE_AR[case]}" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + extra + "."
    segs = _segs(full, lex, pos, "atf") if letter in ("wa", "fa") else None
    return W(full, lex, pos, ["atf-nasaq"] + (["idafa-definiteness"] if mudaf else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
def BADAL(full, lex, en, tr, of, case, tags=(), punct=None, pos="noun", wa=None, extra=""):
    ar = _wa(wa) + f"بَدَلٌ مِنْ «{of}» تَابِعٌ لَهُ فِي {CASE_AR[case]}" + extra + "."
    return W(full, lex, pos, ["badal"] + list(tags), ar, en, tr, punct=punct, segments=_segs(full, lex, pos, wa))
def PREP(full, lex, en, tr, tags=(), punct=None, extra=""):
    return W(full, lex, "prep", ["huruf-jarr"] + list(tags), "حَرْفُ جَرٍّ مَبْنِيٌّ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ" + extra + ".", en, tr, punct=punct)
def MAJ(full, lex, en, tr, by, att, tags=(), punct=None, pos="noun", mudaf=False, extra="", segs=None):
    ar = f"اسْمٌ مَجْرُورٌ بِـ«{by}» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + (f"، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«{att}»" if att else "") + extra + "."
    return W(full, lex, pos, ["huruf-jarr", "mahall-al-majrur"] + (["idafa-definiteness"] if mudaf else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
_FUSED = {"بِ": ("الْبَاءُ", "bi", "prep"), "لِ": ("اللَّامُ", "li", "prep"), "كَ": ("الْكَافُ", "ka", "part"), "لَ": ("اللَّامُ", "li", "prep"), "مِنْ": ("«مِنْ»", "min", "prep"), "عَنْ": ("«عَنْ»", "an", "prep"), "فِي": ("«فِي»", "fi", "prep"), "عَلَيْ": ("«عَلَى»", "ala", "prep"), "إِلَيْ": ("«إِلَى»", "ila", "prep")}
def FUSED(full, letter, lex, en, tr, att, tags=(), punct=None, pos="noun", mudaf=False, extra="", wa=None, inner=None, meaning=""):
    name, plex, ppos = _FUSED[letter]
    inner = inner if inner is not None else full[len(letter):]
    if inner.startswith("ل") and letter == "لِ" and full.startswith("لِلْ"): inner = "ا" + full[2:]
    segs = ([seg(full[:2], "wa" if full[0] == "و" else "fa", "conj")] if wa else []) + [seg(letter, plex, ppos), seg(inner, lex, pos)]
    ar = _wa(wa) + f"{name} حَرْفُ جَرٍّ{meaning}، وَ«{inner}» مَجْرُورٌ بِهَا وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + (f"، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ{att}" if att else "") + extra + "."
    return W(full, lex, pos, ["huruf-jarr", "mahall-al-majrur"] + (["idafa-definiteness"] if mudaf else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
def PRON_J(full, letter, en, tr, att, tags=(), punct=None, wa=None, extra="", meaning=""):
    """a jarr letter fused to a pronoun: بِهِ، لَهُ، بِهَا، لَهُمْ"""
    name, plex, ppos = _FUSED[letter]
    pr = full[len(letter):] if not wa else full[2 + len(letter):]
    pl = {"هِ": ("هِ", "pron-3ms"), "هُ": ("هُ", "pron-3ms"), "هَا": ("هَا", "pron-3fs"), "هُمْ": ("هُمْ", "pron-3mp"), "هِمْ": ("هِمْ", "pron-3mp"), "هُمَا": ("هُمَا", "pron-dual"), "هِمَا": ("هِمَا", "pron-dual"), "نَا": ("نَا", "pron-1p")}[pr]
    segs = ([seg(full[:2], "wa" if full[0] == "و" else "fa", "conj")] if wa else []) + [seg(letter, plex, ppos), seg(pl[0], pl[1], "pron")]
    ar = _wa(wa) + f"{name} حَرْفُ جَرٍّ{meaning}، وَالضَّمِيرُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ" + (f"، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ{att}" if att else "") + extra + "."
    return W(full, pl[1], "pron", ["huruf-jarr", "mahall-al-majrur", "al-bariz-al-muttasil"] + list(tags), ar, en, tr, punct=punct, segments=segs)
def ENC(full, lex, en, tr, role_ar, tags=(), punct=None, pos="noun", pr="هِ", wa=None, letter=None, att=None, extra=""):
    """a noun wearing an attached pronoun: بِذَاتِهِ، جُزْئِهِ، رِزْقَهُ — role_ar is the host's i'rab; the pronoun is its mudaf ilayh"""
    pl = {"هِ": "pron-3ms", "هُ": "pron-3ms", "هَا": "pron-3fs", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمَا": "pron-dual", "نَا": "pron-1p"}[pr]
    body = full[(2 if wa else 0):]
    segs = ([seg(full[:2], "wa" if full[0] == "و" else "fa", "conj")] if wa else [])
    if letter:
        name, plex, ppos = _FUSED[letter]; segs.append(seg(letter, plex, ppos)); body = body[len(letter):]
    host = body[:-len(pr)]
    segs += [seg(host, lex, pos), seg(pr, pl, "pron")]
    ar = _wa(wa) + ((_FUSED[letter][0] + " حَرْفُ جَرٍّ، وَ") if letter else "") + role_ar + "، وَهُوَ مُضَافٌ، وَالضَّمِيرُ الْمُتَّصِلُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + (f"، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ{att}" if att else "") + extra + "."
    return W(full, lex, pos, ["idafa-definiteness", "al-bariz-al-muttasil"] + (["huruf-jarr", "mahall-al-majrur"] if letter else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
def MAZI(full, lex, en, tr, fail_ar, tags=(), punct=None, wa=None, extra="", segs=None):
    ar = _wa(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، " + fail_ar + extra + "."
    return W(full, lex, "verb", list(tags), ar, en, tr, punct=punct, segments=segs if segs else _segs(full, lex, "verb", wa))
def MUDA(full, lex, en, tr, fail_ar, tags=(), punct=None, wa=None, extra="", segs=None, sign="الضَّمَّةُ"):
    ar = _wa(wa) + f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ عَنِ النَّاصِبِ وَالْجَازِمِ وَعَلَامَةُ رَفْعِهِ {sign}، " + fail_ar + extra + "."
    return W(full, lex, "verb", ["mudari-marfu"] + list(tags), ar, en, tr, punct=punct, segments=segs if segs else _segs(full, lex, "verb", wa))
def MAFUL(full, lex, en, tr, of, tags=(), punct=None, pos="noun", mudaf=False, extra="", wa=None):
    ar = _wa(wa) + f"مَفْعُولٌ بِهِ لِـ«{of}» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + extra + "."
    return W(full, lex, pos, ["maful-bihi"] + (["idafa-definiteness"] if mudaf else []) + list(tags), ar, en, tr, punct=punct, segments=_segs(full, lex, pos, wa))
HIDDEN_HUWA = "وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هُوَ"
HIDDEN_HIYA = "وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هِيَ"
HIDDEN_NAHNU = "وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ نَحْنُ"
def finish(n, S, TITLE, CAND, ADD_EN, ADD_TR, marker, morph=None, used_check=True):
    used = []
    for s in S:
        for t in s["tokens"]:
            used.append(t["lex"])
            for sg_ in (t.get("segments") or []): used.append(sg_["lex"])
    missing = []
    for k in sorted(set(used)):
        if k in TG or k in CAND: continue
        try: CAND[k] = find_gloss(k)
        except KeyError: missing.append(k)
    if missing: raise SystemExit("no package owns: " + ", ".join(missing))
    GLOSS_ADD = {k: v for k, v in CAND.items() if v}
    mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
    for k, e in (morph or {}).items(): put_morph(mo, k, e)
    for k, v in GLOSS_ADD.items():
        if v.get("pos") == "verb" and k not in mo["verbs"]:
            m = find_morph(k)
            if m: mo["verbs"][k] = m
    for k in set(used):
        if k in mo["verbs"]: continue
        e = TG.get(k) or GLOSS_ADD.get(k)
        if e and e.get("pos") == "verb" and has_morph(k): mo["verbs"][k] = find_morph(k)
    (PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
    write_out(n, S, TITLE, ADD_EN, ADD_TR, marker, GLOSS_ADD)
    print(f"aqaid ch{n}: {len(S)} sentences, {sum(len(x['tokens']) for x in S)} tokens; gloss + {len(GLOSS_ADD)}; morph {len(mo['verbs'])}")
PRON_M = {"هُوَ": ("pron-3ms-munfasil", "الْفَتْحِ"), "هِيَ": ("pron-3fs-munfasil", "الْفَتْحِ"), "هُمَا": ("pron-dual", "السُّكُونِ"), "هُمْ": ("pron-3mp", "السُّكُونِ"), "نَحْنُ": ("pron-1p", "الضَّمِّ")}
def HUWA(full, en, tr, wa=None, role="مُبْتَدَأٌ", tags=(), punct=None, extra=""):
    """a detached pronoun as mubtada (or another raf' seat): هُوَ، وَهُوَ، فَهُوَ"""
    body = full[2:] if wa else full
    lex, bina = PRON_M[body]
    ar = _wa(wa) + f"«{body}» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى {bina} فِي مَحَلِّ رَفْعٍ {role}" + extra + "."
    return W(full, lex, "pron", ["mubtada-khabar", "al-marifa-al-mudmarat-wal-alam"] + list(tags), ar, en, tr, punct=punct, segments=_segs(full, lex, "pron", wa))
W3 = "فَاعَلَ يُفَاعِلُ"; W2 = "فَعَّلَ يُفَعِّلُ"; W4 = "أَفْعَلَ يُفْعِلُ"; W5 = "تَفَعَّلَ يَتَفَعَّلُ"; W6 = "تَفَاعَلَ يَتَفَاعَلُ"; W7 = "اِنْفَعَلَ يَنْفَعِلُ"; W8 = "اِفْتَعَلَ يَفْتَعِلُ"; W10 = "اِسْتَفْعَلَ يَسْتَفْعِلُ"

sarf = _sg
def WALA(en="«and not» — the wāw joins, the lā repeats the negation.", tr="«ve ne de» — vâv atfeder, lâ nefyi tekrarlar.", tags=()):
    return W("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya", "huruf-al-ziyada-fil-kafiya"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ لَا مَحَلَّ لَهَا.", en, tr, segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
def LA(en="«not».", tr="«değil».", tags=(), ar="حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ."):
    return W("لَا", "la-nafiya", "part", ["la-nafiya"] + list(tags), ar, en, tr)
def TAALA(punct=None):
    return W("تَعَالَى", "taala", TG["taala"]["pos"], ["jumla-mutarida", "khabar-insha"], "فِعْلٌ مَاضٍ لِلتَّنْزِيهِ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ لَا مَحَلَّ لَهَا.", "«the Exalted» — a parenthetical sentence of glorification.", "«Teâlâ» — ta'zîm için mu'teriza cümle.", punct=punct)
def LAJINS(en="«no» — the lā that denies the whole genus, governing like إِنَّ.", tr="«hiç … yoktur» — cinsi nefyeden, إِنَّ gibi amel eden lâ."):
    return W("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"], "«لَا» النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ «إِنَّ».", en, tr)
def ISHARA(full, lex, en, tr, role_ar, tags=(), punct=None, bina="الْفَتْحِ"):
    return W(full, lex, "pron", ["asma-al-ishara"] + list(tags), f"اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى {bina} {role_ar}.", en, tr, punct=punct)
def AW(en="«or».", tr="«ya da»."):
    return W("أَوْ", "aw", "conj", ["atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya"], "حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", en, tr)
def FAIL(full, lex, en, tr, tags=(), punct=None, pos="noun", mudaf=False, extra="", wa=None):
    ar = _wa(wa) + "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ" + ("، وَهُوَ مُضَافٌ" if mudaf else "") + extra + "."
    return W(full, lex, pos, ["fail"] + (["idafa-definiteness"] if mudaf else []) + list(tags), ar, en, tr, punct=punct, segments=_segs(full, lex, pos, wa))
def MAWSUL(full, lex, en, tr, role_ar, tags=(), punct=None, wa=None, extra=""):
    body = full[2:] if wa else full
    return W(full, lex, "pron", ["ism-mawsul"] + list(tags), _wa(wa) + f"«{body}» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ {role_ar}" + extra + ".", en, tr, punct=punct, segments=_segs(full, lex, "pron", wa))
def FA_HUWA(of, en, tr, kind="fa-khabar", body="هُوَ"):
    pre = {"fa-khabar": "الْفَاءُ دَاخِلَةٌ فِي خَبَرِ الْمُبْتَدَإِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ", "fa-jawab": "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»"}[kind]
    lex, bina = PRON_M[body]
    tags = ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada" if kind == "fa-khabar" else "amma-tafsiliyya", "al-marifa-al-mudmarat-wal-alam"]
    return W("فَ" + body, lex, "pron", tags, pre + f"، وَ«{body}» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى {bina} فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ ثَانٍ، وَالْجُمْلَةُ خَبَرُ «" + of + "».", en, tr, segments=[seg("فَ", "fa", "conj"), seg(body, lex, "pron")])
def SALAWAT(who="النَّبِيُّ", salat=True):
    """عَلَيْهِ الصَّلَاةُ وَالسَّلَامُ / عَلَيْهِ السَّلَامُ as a parenthetical prayer"""
    out = [PRON_J("عَلَيْهِ", "عَلَيْ", "«upon him» — the opening of a parenthetical prayer; the jarr phrase is its khabar, put first.", "«ona» — mu'teriza dua cümlesinin açılışı; câr-mecrûr öne alınmış haberidir.", "مَحْذُوفٍ خَبَرٌ مُقَدَّمٌ", tags=["jumla-mutarida", "taqdim-al-musnad"], extra=" — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا")]
    if salat:
        out.append(W("الصَّلَاةُ", "salat", "noun", ["mubtada-khabar", "jumla-mutarida", "khabar-insha", "taqdim-al-musnad"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«blessing».", "«salât»."))
        out.append(ATF("وَالسَّلَامُ", "salam", "«and peace».", "«ve selâm».", "الصَّلَاةُ", "raf"))
    else:
        out.append(W("السَّلَامُ", "salam", "noun", ["mubtada-khabar", "jumla-mutarida", "khabar-insha", "taqdim-al-musnad"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«peace».", "«selâm»."))
    return out
