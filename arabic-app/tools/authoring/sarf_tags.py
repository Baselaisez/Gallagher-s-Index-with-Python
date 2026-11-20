#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sarf_tags.py — the ṣarf notes of a verb token, computed from its lex and its stored paradigm (v334-N1, backlog F1).

A ṣarf matn recites paradigms and reasons about verbs, and until this wave its verbs pointed only at nahw notes: 969 of
the ʿIzzī's 1,105 verb tokens and 1,147 of the Marāḥ's 1,491 carried no note at all. This module names, for one verb
token, the notes that teach what the token IS:

  its bāb / form      Form I → thulathi-mujarrad-babs · Forms II–VIII and X → form-ii-verbs … form-x-verbs · the forms
                      with no note of their own (اِفْعَلَّ، اِفْعَالَّ، اِفْعَوْعَلَ، اِفْعَوَّلَ) → augmented-babs · every
                      quadriliteral, its augmented bābs and the mulḥaqāt → rubai-babs (the two mulḥaqs of اِحْرَنْجَمَ,
                      which the ʿIzzī counts among the augmented triliterals, take both)
  its class           from the ROOT: muḍāʿaf → doubled-verbs · mithāl → mithal-verbs · ajwaf → hollow-verbs · nāqiṣ and
                      lafīf (whose last radical the ʿIzzī conjugates «مِثْلُ رَمَى») → naqis-verbs · lafīf → lafif-verbs
                      and mahmūz → mahmuz-verbs, both only once those notes exist (the list is filtered by the registry)
  tense / mood / voice  an imperative → imperative-amr · one of the five forms → afal-khamsa · a passive →
                      al-majhul-fil-kafiya
  the nūn of emphasis nun-al-tawkid-fil-kafiya (and nun-tawkid on a muḍāriʿ)

Nothing is hand-tagged and nothing is guessed. A token is tagged only when its written form is VERIFIED against the
stored paradigm of its own lex: an exact cell (in any of the three moods), a cell with the helping vowel of two quiescent
letters (لَمْ يَتَجَاوَزِ الْفَاعِلَ، عَادَتِ الْوَاوُ), a regular person of the stored passive, a form under the nūn of emphasis whose
stem is the paradigm's, the unmerged jussive / imperative of a doubled verb (لَمْ يَمْدُدْ، اُمْدُدْ — read off the women's-nūn
cell) or the pausal imperative (قِهْ، رَهْ). A form the paradigm does not hold — an underlying form the book cites
(يَوْعِدُ، قَوَلَ), a dialect variant (اِصَّبَرَ), a token keyed to a look-alike lemma — gets nothing from here: a near-miss
note is worse than none.

Used by pkg_from_engine.py on every package whose meta sets `cellLines` or `cellRows` (a ṣarf matn), so a regeneration
writes the tags again, and runnable over a shipped package — the tags are a function of the token and the paradigm, and
need no engine pass:

    python3 tools/authoring/sarf_tags.py content/samples/<pkg> [--write] [--list]

Without --write it only reports. The pass ADDS note ids (behind the ones a token already carries) and never removes one.
"""
import json, re, sys, glob, unicodedata, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cell_lines as CL

ROOT = pathlib.Path(__file__).resolve().parents[2]
N = lambda s: unicodedata.normalize("NFC", s or "")
MARKS_RE = re.compile("[ً-ْٰـ]")
SHADDA = "ّ"
HAMZAS = "ءأإؤئآ"
WEAK = "وي"

# ------------------------------------------------------------------------------------------------ the form, off the stored wazn
def _w(s):
    """a wazn word compared without the vowel of its waṣl alif"""
    return CL.fin(N(s))

FORM_OF_WAZN = {_w(k): v for k, v in {
    "فَعَلَ": "I", "فَعِلَ": "I", "فَعُلَ": "I",
    "فَعَّلَ": "II", "فَاعَلَ": "III", "أَفْعَلَ": "IV", "تَفَعَّلَ": "V", "تَفَاعَلَ": "VI", "اِنْفَعَلَ": "VII",
    "اِفْتَعَلَ": "VIII", "اِتَّعَلَ": "VIII", "اِفْعَلَّ": "IX", "اِفْعَلَلَ": "IX", "اِسْتَفْعَلَ": "X",
    "اِفْعَالَّ": "XI", "اِفْعَوْعَلَ": "XII", "اِفْعَوَّلَ": "XIII",
    "فَعْلَلَ": "Q", "فَوْعَلَ": "Q", "فَيْعَلَ": "Q", "فَعْوَلَ": "Q", "فَعْيَلَ": "Q", "فَعْلَى": "Q", "فَعْنَلَ": "Q",
    "تَفَعْلَلَ": "Q", "تَفَعْوَلَ": "Q", "تَفَوْعَلَ": "Q", "تَفَيْعَلَ": "Q", "تَمَفْعَلَ": "Q", "تَفَعْلَى": "Q",
    "اِفْعَنْلَلَ": "Q", "اِفْعَلَلَّ": "Q", "اِفْعَنْلَى": "Q",
}.items()}
MULHAQ_IHRANJAMA = {_w("اِفْعَنْلَى")}   # اِسْلَنْقَى; اِقْعَنْسَسَ is اِفْعَنْلَلَ on a THREE-letter root (decided below)
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}
FORM_NOTE = {"I": "thulathi-mujarrad-babs", "II": "form-ii-verbs", "III": "form-iii-verbs", "IV": "form-iv-verbs", "V": "form-v-verbs",
             "VI": "form-vi-verbs", "VII": "form-vii-verbs", "VIII": "form-viii-verbs", "X": "form-x-verbs",
             "IX": "augmented-babs", "XI": "augmented-babs", "XII": "augmented-babs", "XIII": "augmented-babs", "Q": "rubai-babs"}


def radicals(root):
    return [x for x in N(root or "").split() if x]


def form_of(e, entry):
    """the form the stored paradigm names (its `wazn`), refused when the glossary's own `form` or the length of the māḍī
    contradicts it — two witnesses, or no bāb note"""
    wz = N(e.get("wazn") or "")
    wz = re.sub(r"^\([^)]*\)\s*", "", wz).split(" ")[0] if wz else ""
    f = FORM_OF_WAZN.get(_w(wz))
    if not f: return None
    gf = str((entry or {}).get("form") or "").strip()
    if gf in ROMAN and f in ROMAN and gf != f: return None
    r = radicals((entry or {}).get("root"))
    if f == "Q" and gf in ROMAN: return None
    if f != "Q" and len(r) not in (0, 3): return None
    m0 = MARKS_RE.sub("", N((e.get("mazi") or [""])[0]))
    if f == "I" and len(m0) > 4: return None   # رَأَى، مَدَّ، قَالَ: three letters (a shadda is one); never five
    return f


def bab_notes(e, entry):
    f = form_of(e, entry)
    if not f: return []
    out = [FORM_NOTE[f]]
    if f == "Q":
        wz = _w(re.sub(r"^\([^)]*\)\s*", "", N(e.get("wazn") or "")).split(" ")[0])
        r = radicals((entry or {}).get("root"))
        if wz in MULHAQ_IHRANJAMA or (wz == _w("اِفْعَنْلَلَ") and len(r) == 3): out.append("augmented-babs")
    return out


# ------------------------------------------------------------------------------------------------ the class, off the root
def classes(entry, form, e=None):
    """the verb's classes by its radicals. A quadriliteral (or a mulḥaq, whose third letter is the bāb's, not the root's)
    is left to its own note. A hollow root whose stored māḍī KEEPS its wāw or yāʾ where the note says it turns to alif
    (عَوِرَ، اِسْتَحْوَذَ — the Marāḥ's «مَا لَا يُعَلُّ») is not called hollow here: the note would teach the opposite of the word."""
    r = radicals((entry or {}).get("root"))
    if len(r) != 3 or form in (None, "Q"): return []
    if any(c in "اىآ" for c in r): return []   # a root written with an alif names no radical
    w = [c in WEAK for c in r]; out = []
    if r[1] == r[2] and not w[1] and form not in ("II", "V"): out.append("mudaaf")   # in فَعَّلَ / تَفَعَّلَ the doubling is the bāb's
    if w[1] and w[2]: out.append("lafif-maqrun")
    elif w[0] and w[2]: out.append("lafif-mafruq")
    elif w[0] and w[1]: return []   # يَيْنَ: «لَا يُبْنَى مِنْهُ فِعْلٌ»
    elif w[0]: out.append("mithal")
    elif w[1]:
        u = units((e or {}).get("mazi", [""])[0]) if e else []
        if not (e and form in ("I", "IV", "VII", "VIII", "X") and not (len(u) >= 2 and u[-2][0] in "اآ" and not u[-2][1])): out.append("ajwaf")
    elif w[2]: out.append("naqis")
    if any(c in HAMZAS for c in r): out.append("mahmuz")
    return out

CLASS_NOTES = {"mudaaf": ["doubled-verbs"], "mithal": ["mithal-verbs"], "ajwaf": ["hollow-verbs"], "naqis": ["naqis-verbs"],
               "lafif-maqrun": ["lafif-verbs", "naqis-verbs"], "lafif-mafruq": ["lafif-verbs", "naqis-verbs"], "mahmuz": ["mahmuz-verbs"]}


# ------------------------------------------------------------------------------------------------ the cell
def units(form):
    """a form as [letter, vowel, doubled] units — NFC writes a vowel BEFORE its shadda, so the string's last character is no
    guide to the last vowel"""
    out = []
    for ch in N(form):
        if ch == SHADDA:
            if out: out[-1][2] = True
        elif MARKS_RE.match(ch):
            if out: out[-1][1] = ch
        else: out.append([ch, "", False])
    return out


def join(us):
    return N("".join(l + v + (SHADDA if d else "") for l, v, d in us))

FATHA, DAMMA, KASRA, SUKUN = "\u064e", "\u064f", "\u0650", "\u0652"


def sound_root(entry):
    r = radicals((entry or {}).get("root"))
    return len(r) in (3, 4) and not any(c in WEAK or c in HAMZAS or c in "اىآ" for c in r) and all(r[i] != r[i + 1] for i in range(len(r) - 1))


def derived_passive(e, entry):
    """the 3ms passive of a verb whose paradigm stores none, by the ʿIzzī's own rule (l. 55–61): the māḍī with a ḍamma on
    every vowelled letter before the one before last and a kasra on that one (نُصِرَ، اُسْتُخْرِجَ، تُفُعِّلَ، فُوعِلَ); the muḍāriʿ
    with a ḍamma on its prefix and a fatḥa before the last (يُنْصَرُ، يُسْتَخْرَجُ). ONLY for a root of sound, unlike letters —
    and, for the bare triliteral nāqiṣ, the book's own غُزِيَ / يُغْزَى، يُرْمَى (l. 221, 258)."""
    mz = units((e.get("mazi") or [""])[0]); mu = units((e.get("mudari") or [""])[0])
    r = radicals((entry or {}).get("root"))
    if sound_root(entry) and len(mz) >= 3 and len(mu) >= 4:
        pm = [list(u) for u in mz]
        vow = [i for i, u in enumerate(pm) if u[1] in (FATHA, DAMMA, KASRA)]
        if len(vow) < 3 or vow[-1] != len(pm) - 1 or pm[-1][1] != FATHA: return None, None
        pm[vow[-2]][1] = KASRA
        for i in vow[:-2]: pm[i][1] = DAMMA
        for i in range(1, len(pm)):
            if pm[i][0] == "ا" and not pm[i][1] and pm[i - 1][1] == DAMMA: pm[i][0] = "و"
        pu = [list(u) for u in mu]
        vow = [i for i, u in enumerate(pu) if u[1] in (FATHA, DAMMA, KASRA)]
        if len(vow) < 3 or vow[-1] != len(pu) - 1 or pu[-1][1] != DAMMA or pu[0][0] != "ي": return None, None
        pu[0][1] = DAMMA; pu[vow[-2]][1] = FATHA
        return join(pm), join(pu)
    if len(r) == 3 and r[2] in WEAK and r[0] not in WEAK + HAMZAS and r[1] not in WEAK + HAMZAS and r[0] != r[1] and len(mz) == 3 and len(mu) == 4 and form_of(e, entry) == "I":
        return join([[mz[0][0], DAMMA, False], [mz[1][0], KASRA, False], ["ي", FATHA, False]]), join([["ي", DAMMA, False], [mu[1][0], SUKUN, False], [mu[2][0], FATHA, False], ["ى", "", False]])
    return None, None


def passive_forms(e, entry=None):
    """the persons of the passive that follow from its 3ms by suffix alone: {form → (tense, person, mood)}"""
    out = {}
    pm = N(e.get("majhulMazi") or ""); pu = N(e.get("majhulMudari") or "")
    if not pm and not pu and entry is not None: pm, pu = [x or "" for x in derived_passive(e, entry)]
    def put(us, c): out.setdefault(CL.fin(join(us)), c)
    um = units(pm)
    if len(um) >= 2 and um[-1][1] == FATHA and um[-1][0] not in "اوى":
        st = [list(u) for u in um]
        def with_last(v, tail=""):
            x = [list(u) for u in st]; x[-1][1] = v; return x + units(tail)
        put(with_last(FATHA), ("mazi", 0, None)); put(with_last(FATHA, "ا"), ("mazi", 1, None))
        put(with_last(FATHA, "تْ"), ("mazi", 3, None)); put(with_last(FATHA, "تَا"), ("mazi", 4, None))
        if not st[-1][2] and st[-1][0] not in "يتن" + HAMZAS and not (len(st) >= 2 and st[-2][0] in "اوي" and not st[-2][1]):   # a sound, single last letter behind a vowelled one
            put(with_last(DAMMA, "وا"), ("mazi", 2, None))
            for i, tail in ((5, "نَ"), (6, "تَ"), (7, "تُمَا"), (8, "تُمْ"), (9, "تِ"), (12, "تُ"), (13, "نَا")): put(with_last(SUKUN, tail), ("mazi", i, None))
    uu = units(pu)
    if len(uu) >= 3 and uu[0][0] == "ي" and uu[0][1] == DAMMA:
        hz = uu[1][0] in HAMZAS; last = uu[-1]
        pres = [(0, "ي"), (3, "ت"), (6, "ت"), (13, "ن")] + ([] if hz else [(12, "أ")])
        for i, p in pres:
            f = [[p, DAMMA, False]] + [list(u) for u in uu[1:]]
            put(f, ("mudari", i, "raf"))
            if last[0] in "ىا" and not last[1]:                      # يُسَمَّى، يُعْطَى: rafʿ and naṣb alike, the alif gone in jazm
                put(f, ("mudari", i, "nasb")); put(f[:-1], ("mudari", i, "jazm"))
            elif last[1] == DAMMA and last[0] not in "وي" + HAMZAS:
                g = [list(u) for u in f]; g[-1][1] = FATHA; put(g, ("mudari", i, "nasb"))
                if last[2]: put(g, ("mudari", i, "jazm"))               # لَمْ يُمَدَّ: the merged jussive on its fatḥa
                else:
                    g = [list(u) for u in f]; g[-1][1] = SUKUN
                    if len(g) >= 3 and g[-2][0] == "ا" and not g[-2][1]: g = g[:-2] + [g[-1]]   # يُزَادُ → لَمْ يُزَدْ: the alif falls before the quiescent
                    put(g, ("mudari", i, "jazm"))
        if last[1] == DAMMA and last[0] not in "وي" + HAMZAS:
            for i, p, tail in ((1, "ي", "انِ"), (4, "ت", "انِ"), (7, "ت", "انِ"), (2, "ي", "ونَ"), (8, "ت", "ونَ"), (9, "ت", "ينَ")):
                f = [[p, DAMMA, False]] + [list(u) for u in uu[1:]]
                f[-1][1] = FATHA if tail == "انِ" else DAMMA if tail == "ونَ" else KASRA
                put(f + units(tail), ("mudari", i, "raf"))
                put(f + units("ا" if tail == "انِ" else "وا" if tail == "ونَ" else "ي"), ("mudari", i, "jazm"))
    return out


def fakk_forms(e):
    """the unmerged jussive and imperative of a doubled verb, read off the women's-nūn cells the paradigm stores
    (يَمْدُدْنَ → لَمْ يَمْدُدْ، اُمْدُدْنَ → اُمْدُدْ): {form → (tense, person, mood)}"""
    out = {}
    mu = e.get("mudari") or []; am = e.get("amr") or []
    if len(mu) > 5 and SHADDA in N(mu[0])[-3:] and N(mu[5]).endswith("ْنَ"):
        base = N(mu[5])[:-1][:-1]   # يَمْدُدْ
        if base.endswith("ْ"):
            for i in (0, 3, 6, 12, 13):
                out.setdefault(CL.fin(N(mu[i])[0] + base[1:]), ("mudari", i, "jazm"))
    if len(am) > 5 and SHADDA in N(am[0])[-3:] and N(am[5]).endswith("ْنَ"):
        base = N(am[5])[:-2]
        if base.endswith("ْ"): out.setdefault(CL.fin(base), ("amr", 0, None))
    return out


def tawkid_stem_ok(e, host):
    """is this emphatic form built on a cell of THIS paradigm? → 'amr' / 'mudari' / None (cell_lines.tawkid_kind decides)"""
    return CL.tawkid_kind(e, host)[0]


def host_of(tok):
    """the verb's own written form: the segment keyed to the token's lex where the token is segmented"""
    full = N(tok["surface"]["full"]); lex = tok.get("lex")
    for sg in (tok.get("segments") or []):
        if sg.get("lex") == lex and sg.get("form"): return N(sg["form"])
    return full


def _hosts(host):
    """the form, and the form behind a joining وَ / فَ, the lām of command, the sīn and the lām of the oath"""
    out = [(host, "")]
    m = re.match(r"^[وف]َ", host)
    if m: out.append((host[m.end():], ""))
    for h, _ in list(out):
        m = re.match(r"^ل[ِْ]", h)
        if m: out.append((h[m.end():], "lam"))
        m = re.match(r"^[سل]َ", h)
        if m: out.append((h[m.end():], ""))
    return out


def identify(tok, e, entry=None):
    """what cell of paradigm e the token writes → {"how", "tense", "persons", "moods", "voice", "tawkid"} or None"""
    if not e or e.get("jamid") or not e.get("mazi"): return None
    line = N((tok.get("irab") or {}).get("ar", ""))
    said = "amr" if "فِعْلُ أَمْرٍ" in line else "mazi" if "فِعْلٌ مَاضٍ" in line else "mudari" if "فِعْلٌ مُضَارِعٌ" in line else None
    pas = fakk = None
    full = N(tok["surface"]["full"]); seg = host_of(tok)
    for h, pre in _hosts(full) + ([] if seg == full else _hosts(seg)):   # the whole written word first: a cell that ends in ـِي / ـنَا is no verb + enclitic
        variants = [(h, "cell")]
        if h.endswith("ُو") and seg != full: variants.append((h + "ا", "cell"))                                           # أَخْلَفُوكَ: the alif of the group is not written before an enclitic
        if h.endswith("ا") and len(h) > 2: variants.append((h[:-1] + "ى", "cell"))                                         # يَحْيَا / يَحْيَى: one alif, two spellings
        elif h.endswith("ى"): variants.append((h[:-1] + "ا", "cell"))
        if h.endswith("ِ") and not h.endswith(SHADDA + "ِ"): variants.append((h[:-1] + "ْ", "helping-vowel"))   # لَمْ يَتَجَاوَزِ، عَادَتِ، فَاضْرِبِ
        if h.endswith("وُا"): variants.append((h[:-2] + "ْا", "helping-vowel"))                                           # دَعَوُا اللهَ
        if h.endswith("هْ") and len(MARKS_RE.sub("", h)) == 2: variants.append((h[:-2], "waqf"))                           # قِهْ، رَهْ
        for hv, how in variants:
            cs = CL.candidates(e, hv)
            if how == "waqf": cs = [c for c in cs if c[0] == "amr" and c[1] == 0]
            if pre == "lam": cs = [c for c in cs if c[0] == "mudari" and c[2] in ("jazm", "nasb")]   # the lām of command (لِيَنْصُرْ) or of purpose (لِتَفْصِلَ)
            if said: cs = [c for c in cs if c[0] == said]   # the line names the tense: a homograph of another tense is not this token (تَكَسَّرَا)
            if cs:
                tenses = {c[0] for c in cs}; one = len(tenses) == 1   # a quoted form two tenses write alike keeps its lexeme's notes and takes no tense note
                return {"how": how, "tense": tenses.pop() if one else None, "persons": sorted({c[1] for c in cs}) if one else [], "moods": sorted({c[2] for c in cs if c[2]}) if one else [], "voice": "active", "tawkid": False}
            if pas is None: pas = passive_forms(e, entry)
            c = pas.get(CL.fin(hv))
            if c and (not said or said == c[0]):
                return {"how": "passive" if how == "cell" else "passive+" + how, "tense": c[0], "persons": [c[1]], "moods": [c[2]] if c[2] else [], "voice": "passive", "tawkid": False}
            if fakk is None: fakk = fakk_forms(e)
            c = fakk.get(CL.fin(hv))
            if c and (not said or said == c[0]):
                return {"how": "fakk", "tense": c[0], "persons": [c[1]], "moods": [c[2]] if c[2] else [], "voice": "active", "tawkid": False}
        if CL.tawkid_line(h):
            k = tawkid_stem_ok(e, h)
            if k and (not said or said == k):
                return {"how": "tawkid", "tense": k, "persons": [], "moods": [], "voice": "active", "tawkid": True}
    return None


FIVE = {1, 2, 4, 7, 8, 9, 10}


def tags_for(tok, e, entry, gids):
    """the ordered ṣarf-note ids of one verb token (only ids the registry holds), and the cell they were read from"""
    if tok.get("pos") != "verb" or not e: return [], None
    if entry is not None and entry.get("pos") not in (None, "verb"): return [], None
    cell = identify(tok, e, entry)
    if not cell: return [], None
    out = []
    if cell["tawkid"]:
        out.append("nun-al-tawkid-fil-kafiya")
        if cell["tense"] == "mudari": out.append("nun-tawkid")
    if cell["voice"] == "passive": out.append("al-majhul-fil-kafiya")
    if cell["tense"] == "amr": out.append("imperative-amr")
    line = N((tok.get("irab") or {}).get("ar", ""))
    if cell["tense"] == "mudari" and not cell["tawkid"] and cell["persons"]:
        five = all(i in FIVE for i in cell["persons"])
        if not five and any(i in FIVE for i in cell["persons"]) and ("ثُبُوتُ النُّونِ" in line or "حَذْفُ النُّونِ" in line) and "نُونِ النِّسْوَةِ" not in line: five = True
        if five and "نُونِ النِّسْوَةِ" not in line: out.append("afal-khamsa")
    f = form_of(e, entry)
    for c in classes(entry, f, e): out += CLASS_NOTES[c]
    out += bab_notes(e, entry)
    out = [g for g in dict.fromkeys(out) if g in gids]
    return out, cell


def apply(tok, e, entry, gids):
    """add the token's ṣarf notes behind the ones it carries; → the ids added"""
    add, cell = tags_for(tok, e, entry, gids)
    have = list(tok.get("grammar") or [])
    new = [g for g in add if g not in have]
    if new: tok["grammar"] = have + new
    return new, cell


# ------------------------------------------------------------------------------------------------ over a shipped package
def load_shelf():
    G, M = {}, {}
    for f in sorted(glob.glob(str(ROOT / "content/samples/*/glossary.json"))):
        for k, v in json.load(open(f, encoding="utf-8")).get("entries", {}).items(): G.setdefault(k, v)
    for f in sorted(glob.glob(str(ROOT / "content/samples/*/morphology.json"))):
        for k, v in json.load(open(f, encoding="utf-8")).get("verbs", {}).items(): M.setdefault(k, v)
    return G, M


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv; listing = "--list" in sys.argv
    pkg = pathlib.Path(args[0])
    gids = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
    sarf = {p.stem for p in (ROOT / "content/grammar").glob("*.json") if json.load(open(p, encoding="utf-8")).get("group") == "sarf"}
    G, M = load_shelf()
    Gp = json.load(open(pkg / "glossary.json", encoding="utf-8")).get("entries", {})
    Mp = json.load(open(pkg / "morphology.json", encoding="utf-8")).get("verbs", {})
    verbs = cells = tagged = added = 0; left = []; by = {}
    for f in sorted((pkg / "chapters").glob("*.json"), key=lambda x: int(x.stem)):
        raw = open(f, encoding="utf-8").read(); ch = json.loads(raw); dirty = False
        for sen in ch["sentences"]:
            for i, t in enumerate(sen["tokens"]):
                if t.get("pos") != "verb": continue
                verbs += 1
                e = Mp.get(t.get("lex")) or M.get(t.get("lex")); entry = Gp.get(t.get("lex")) or G.get(t.get("lex"))
                new, cell = apply(t, e, entry, gids)
                if cell: cells += 1
                else: left.append(f"{f.stem}:{sen['id']}:{i} {t['surface']['full']} [{t.get('lex')}]" + ("" if e else " — no paradigm"))
                if any(g in sarf for g in (t.get("grammar") or [])): tagged += 1
                if new:
                    added += 1; dirty = True
                    for g in new: by[g] = by.get(g, 0) + 1
        if write and dirty:
            open(f, "w", encoding="utf-8").write(json.dumps(ch, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""))
    print(f"{pkg.name}: {verbs} verb tokens; {cells} verified as a cell of their paradigm; {tagged} carry a ṣarf note; {added} tokens gained notes" + ("" if write else " — dry run"))
    for g, n in sorted(by.items(), key=lambda x: -x[1]): print(f"   +{n:5d}  {g}")
    print(f"   left untagged (not a verified cell): {len(left)}")
    if listing:
        for x in left: print("     ", x)


if __name__ == "__main__":
    main()
