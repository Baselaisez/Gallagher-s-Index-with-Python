"""amthal_common — the shared kit of the proverbs' shelf «الْأَمْثَال» (v348-A).

Each package `mathal-<slug>` is ONE proverb of Abū ʿUbayd's Kitāb al-amthāl with the tale al-Bakrī (or Abū ʿUbayd himself) tells
behind it in «فصل المقال في شرح كتاب الأمثال» (ed. Iḥsān ʿAbbās and ʿAbd al-Majīd ʿĀbidīn, Muʾassasat al-Risāla 1971; Shamela 1025;
research/sources/fasl-al-maqal-bakri-src.txt). The script tools/authoring/author_<slug>.py is the package's source of truth; it writes
the sentences and calls `finish()` here, which resolves every lex key on the shelf by lemma identity, takes every reused verb's paradigm
from the package that owns it, checks every NEW key against every glossary, and writes manifest / chapters / glossary / morphology.

RULES (v333, carried): the e-text is UNVOWELLED, so every vowel is ours and the manifest says so; the text is never retold, re-ordered
or silently corrected — a correction is made only against a named witness and is listed in the attribution; a vowel we cannot settle
from the lexicon and the grammar is LEFT UNWRITTEN and listed «for the hoca». The exact passage is saved first as
research/sources/<slug>-src.txt.
"""
import json, os, pathlib, sys, unicodedata, collections, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *            # noqa: F401,F403 — the house wordings
from story_kit import _pre        # noqa: F401
import sarf_gen as _sg            # noqa: F401
PRE, SG = _pre, _sg               # public names: a star import leaves the underscored ones behind

PRON.update({"هُمُ": "pron-3mp", "هِمُ": "pron-3mp", "هِمْ": "pron-3mp", "هُمْ": "pron-3mp", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms",
             "ي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "كُمُ": "pron-2mp", "نَا": "pron-1p", "نِي": "pron-1s"})
PRON_AR.update({"هُمُ": "هُمْ", "هِمُ": "هُمْ", "هِمْ": "هُمْ", "هُمْ": "هُمْ", "هُمَا": "هُمَا", "هِمَا": "هُمَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ",
                "ي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "كُمُ": "كُمْ", "نَا": "نَا"})

N = lambda s: unicodedata.normalize("NFC", s)
def NOTE(t, ar="", en="", tr=""):
    """append a remark to a kit line, before its closing full stop"""
    for k, v in (("ar", ar), ("en", en), ("tr", tr)):
        if v:
            s = t["irab"][k]
            t["irab"][k] = N((s[:-1] if s.endswith(".") else s) + v + ".")
    return t
def TAG(t, *tags):
    for g in tags:
        if g not in t.setdefault("grammar", []): t["grammar"].append(g)
    return t
def W(*triples):
    out = ["", "", ""]
    for m in triples:
        out = [a + b for a, b in zip(out, m)]
    return dict(note_ar=out[0], note_en=out[1], note_tr=out[2])
def ISTI(t):
    """a waw / fa that opens a new sentence after a full stop resumes; it does not conjoin"""
    for a, b, k in ((WA_AR, "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "ar"), (FA_AR, "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ", "ar"),
                    ("The waw conjoins; ", "The waw resumes; ", "en"), ("The fa conjoins; ", "The fa resumes; ", "en"),
                    ("«ve» + ", "Vâv isti'nâf içindir; ", "tr"), ("«bunun üzerine» + ", "Fâ isti'nâf içindir; ", "tr")):
        if t["irab"][k].startswith(a): t["irab"][k] = N(b + t["irab"][k][len(a):])
    return t
def FA_SABAB(t):
    """a fa that ties a consequence to what came before (sababiyya / taʿqīb) — not a bare conjunction of words"""
    for a, b, k in ((FA_AR, "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَ", "ar"), ("The fa conjoins; ", "The fa conjoins and marks what follows at once; ", "en"),
                    ("«bunun üzerine» + ", "Fâ ta'kîb ile atıf içindir; ", "tr")):
        if t["irab"][k].startswith(a): t["irab"][k] = N(b + t["irab"][k][len(a):])
    return t

MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
MAQUL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekūlü'l-kavl olarak mahallen mansûb")
ATF_CL = (" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "; the clause is conjoined to the one before it", "; cümle öncekine ma'tûftur")
HALCL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause is a hal, in the seat of nasb", "; cümle hâl olarak mahallen mansûb")
KH_KANA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
KH_INNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi olarak mahallen merfû")
KH_MUB_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the clause is the predicate of the mubtada, in the seat of raf'", "; cümle mübtedânın haberi, mahallen merfû")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
LAMMA_SHART = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا إِلَيْهَا", "; the clause is in the seat of jarr, annexed to لَمَّا", "; cümle lemmâ'ya muzâfun ileyh olarak mahallen mecrûr")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
MUNSARIF = (" — عَلَمٌ مُنْصَرِفٌ، فَنُوِّنَ", " — a fully declined proper name, so it takes tanwin", " — munsarif özel isim; bu yüzden tenvin alır")
NO_TANWIN = (" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْن» مُضَافًا إِلَى عَلَمٍ", " — its tanwin drops because the name is followed by «ibn» annexed to another name", " — ardından bir aleme muzâf «ibn» geldiği için tenvini düşer")
DIPT_ALAM_F = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name, barred from tanwin", " — müennes özel isim, gayr-i munsarif")
DIPT_WAZN = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ", " — a proper name on a verb's pattern, barred from tanwin", " — fiil vezninde alem, gayr-i munsarif")
def HID(ar, en, tr):
    """name the referent of a hidden doer / a pronoun"""
    return ("، يَعُودُ عَلَى " + ar, " (" + en + ")", " (" + tr + ")")
def BN(case, of):
    """«ibn» between two names: a naʿt, its alif dropped in writing"""
    full = {"raf": "بْنُ", "nasb": "بْنَ", "jarr": "بْنِ"}[case]
    sign = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
        "نَعْتٌ لِـ«" + of[0] + "» " + sign + "، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
        "An adjective (na't) of «" + of[1] + "», in " + {"raf": "raf'", "nasb": "nasb", "jarr": "jarr"}[case] + " and annexed — its alif is dropped in writing because it stands between two names.",
        "«" + of[2] + "» kelimesinin na'tı, " + {"raf": "merfû", "nasb": "mansûb", "jarr": "mecrûr"}[case] + ", muzâf — iki alem arasında geldiği için elifi yazıda düşer.")
def NM(full, lex, note=("", "", ""), punct=None, sign="بِالْكَسْرَةِ", extra=None):
    """a proper name as the second term of an idafa"""
    return MUDAF_ILAYH(full, lex, "propn", extra=extra, sign=sign, note_ar=note[0], note_en=note[1], note_tr=note[2], punct=punct)
def SAYQ(full, who, punct=":", hidden=True):
    """قَالَ with its hidden doer named"""
    return NOTE(QALA(full, hidden=hidden, punct=punct), " — وَالْقَائِلُ " + who[0], "; the speaker is " + who[1], "; söyleyen: " + who[2])
def QUOTE_NOTE(t):
    """the first word of a quoted proverb"""
    return NOTE(t, " — وَهُوَ أَوَّلُ الْمَثَلِ", " — the first word of the proverb", " — atasözünün ilk kelimesi")
HEAD_CL = (" — وَجُمْلَةُ الْمَثَلِ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the proverb is an opening sentence with no seat of its own", "; atasözü ibtidâiyye cümledir, i'râbdan mahalli yoktur")

# ---- verb shapes the kit lacks ----------------------------------------------------------------------------------------
def WAW_PL(full, lex, extra=None, punct=None, note=("", "", ""), enc=None):
    """a past verb with the waw of the group (and an enclitic object)"""
    p, stem, sg, ar0, en0, tr0 = PRE(full)
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "; the attached pronoun is its object, in the seat of nasb", "; bitişik zamir mef'ûlün bih, mahallen mansûb") if enc else ("", "", "")
    t = VERB_WAW(full, lex, extra, punct)
    return NOTE(t, encs[0] + note[0], encs[1] + note[1], encs[2] + note[2])
def TUM(full, lex, extra=None, punct=None, note=("", "", ""), enc=None, pre=None, lam=False):
    """أَصَبْتُمْ، أَعْطَيْتُمْ: past verb with the tum of the doers (lam=True: the لَ of the answer of لَوْ in front)"""
    p, stem, sg, ar0, en0, tr0 = PRE(full)
    pre_ar, pre_en, pre_tr = pre or (ar0, en0, tr0)
    if lam: sg, stem = seg("لَ", "lam-jawab", "part"), stem[2:]
    segs = [s for s in [sg, seg(stem[:-4], lex, "verb"), seg(stem[-4:], "pron-2mp", "pron")] if s]
    return tok(full, lex, "verb", ["al-bariz-al-muttasil", "fail"] + (extra or []),
        pre_ar + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ الْمُتَحَرِّكِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note[0] + ".",
        pre_en + "past verb built on sukun because a moving raf' pronoun is attached; تُمْ «you (all)» is its doer, in the seat of raf'" + note[1] + ".",
        pre_tr + "harekeli ref zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» (siz) fâildir, mahallen merfû" + note[2] + ".", punct=punct, segments=segs)

# ---- the lexicon: every key by lemma identity from the shelf -------------------------------------------------------------
_DIA = re.compile("[ً-ٰ]")
def _lemma_id(e): return _DIA.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))

def finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE=None, LEMMA_HERE=None, V_NEW=None):
    GLOSS_HERE, LEMMA_HERE, V_NEW = GLOSS_HERE or {}, LEMMA_HERE or {}, V_NEW or {}
    PKG = OUT_ROOT / SLUG
    (PKG / "chapters").mkdir(parents=True, exist_ok=True)
    DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs", "rubai-babs"}
    for S in CHAPS:
        for s in S:
            for t in s["tokens"]:
                if DERIVED & set(t.get("grammar", [])) and "thulathi-mujarrad-babs" in t["grammar"]:
                    t["grammar"].remove("thulathi-mujarrad-babs")
                for sg2 in t.get("segments", []):
                    sg2["form"] = sg2["form"].lstrip("ًٌٍَُِّْ")
    SAMPLES = ROOT / "content/samples"
    PKGS = sorted(d.name for d in SAMPLES.iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
    G = {p: json.loads((SAMPLES / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
    M = {p: (json.loads((SAMPLES / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
             if (SAMPLES / p / "morphology.json").exists() else {}) for p in PKGS}
    def find_entry(k):
        holders = [(p, G[p][k]) for p in PKGS if k in G[p] and not (p.startswith("mathal-") and k in NEW_GLOSS)]
        if not holders: return None, None
        votes = collections.Counter(_lemma_id(e) for p, e in holders)
        best = votes.most_common(1)[0][0]
        group = [(p, e) for p, e in holders if _lemma_id(e) == best]
        if group[0][1].get("pos") == "verb":
            for p, e in group:
                if k in M[p]: return e, p
        gl = collections.Counter(json.dumps(e.get("gloss"), ensure_ascii=False, sort_keys=True) for p, e in group).most_common(1)[0][0]
        for p, e in group:
            if json.dumps(e.get("gloss"), ensure_ascii=False, sort_keys=True) == gl: return e, p
        return group[0][1], group[0][0]
    for k, e in NEW_GLOSS.items():
        # a key is a global claim: only a sibling proverb package may hold it, and only for the same lemma
        hit = [p for p in PKGS if k in G[p] and not (p.startswith("mathal-") and _lemma_id(G[p][k]) == _lemma_id(e))]
        assert not hit, ("a key is a global claim — taken", k, hit, [G[p][k].get("lemma") for p in hit])
    used = set()
    for S in CHAPS:
        for s in S:
            for t in s["tokens"]:
                used.add(t["lex"])
                for sg2 in t.get("segments", []): used.add(sg2["lex"])
    GLOSS, ORIGIN, missing = {}, {}, []
    for k in sorted(used):
        if k in NEW_GLOSS: GLOSS[k] = NEW_GLOSS[k]; continue
        e, p = find_entry(k)
        if e is None: missing.append(k); continue
        GLOSS[k], ORIGIN[k] = json.loads(json.dumps(e)), p
        if k in GLOSS_HERE: GLOSS[k]["gloss"] = {"en": GLOSS_HERE[k][0], "tr": GLOSS_HERE[k][1]}
        if k in LEMMA_HERE:
            assert _lemma_id(GLOSS[k]) == _lemma_id({"lemma": LEMMA_HERE[k]}), k
            GLOSS[k]["lemma"] = LEMMA_HERE[k]
    assert not missing, ("keys with no entry on the shelf and none in NEW_GLOSS", missing)
    assert not [k for k in GLOSS_HERE if k not in GLOSS], [k for k in GLOSS_HERE if k not in GLOSS]
    assert not [k for k in NEW_GLOSS if k not in used], ("unused new keys", [k for k in NEW_GLOSS if k not in used])
    MORPH = {"verbs": dict(V_NEW)}
    V = MORPH["verbs"]
    new_verbs = sorted(k for k, e in NEW_GLOSS.items() if e["pos"] == "verb")
    for k in new_verbs:
        if k not in V:          # a verb a sibling proverb package coined: its paradigm travels with the key
            for p in PKGS:
                if p.startswith("mathal-") and k in M[p]: V[k] = M[p][k]; break
    assert sorted(k for k in V if k in NEW_GLOSS) == new_verbs, ("every new verb gets a paradigm", new_verbs, sorted(V))
    for k, e in GLOSS.items():
        if e.get("pos") != "verb" or k in V: continue
        o = ORIGIN.get(k, "")
        if o in M and k in M[o]: V[k] = M[o][k]
        else:
            for p in PKGS:
                if k in M[p] and _lemma_id(G[p].get(k, {})) == _lemma_id(e): V[k] = M[p][k]; break
    no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in V]
    assert not no_par, ("verbs with no paradigm", no_par)
    MANIFEST = dict(MANIFEST)
    MANIFEST.setdefault("id", SLUG); MANIFEST.setdefault("storyGroup", SLUG)
    MANIFEST["chapters"] = [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)]
    (PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
    for old in (PKG / "chapters").glob("*.json"): old.unlink()
    for i, S in enumerate(CHAPS, 1):
        (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
    (PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
    (PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
    ALL = [s for S in CHAPS for s in S]
    print(SLUG, "sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS),
          "verbs:", len(V), "new:", len(NEW_GLOSS), "->", PKG)
    return PKG

def NP(lemma, en, tr, level=4, **kw): return {"lemma": lemma, "pos": "propn", "gloss": {"en": en, "tr": tr}, "level": level, **kw}
def NN(lemma, root, en, tr, level=4, **kw): return {"lemma": lemma, "root": root, "pos": "noun", "gloss": {"en": en, "tr": tr}, "level": level, **kw}
def NV(lemma, root, form, en, tr, level=4, **kw): return {"lemma": lemma, "root": root, "pos": "verb", "form": form, "gloss": {"en": en, "tr": tr}, "level": level, **kw}

SOURCE_AR = "«فَصْلُ الْمَقَالِ فِي شَرْحِ كِتَابِ الْأَمْثَالِ» لِأَبِي عُبَيْدٍ الْبَكْرِيِّ (ت ٤٨٧ هـ)، بِتَحْقِيقِ إِحْسَانَ عَبَّاس وَعَبْدِ الْمَجِيدِ عَابِدِين، مُؤَسَّسَةُ الرِّسَالَةِ ١٩٧١ (الشَّامِلَةُ ١٠٢٥)"
SOURCE_EN = "«Faṣl al-maqāl fī sharḥ Kitāb al-amthāl» by Abū ʿUbayd al-Bakrī (d. 487 AH), al-Bakrī's commentary on Abū ʿUbayd al-Qāsim ibn Sallām's Book of Proverbs, ed. Iḥsān ʿAbbās and ʿAbd al-Majīd ʿĀbidīn, Muʾassasat al-Risāla, Beirut 1971 (Shamela book 1025)"
SOURCE_TR = "Ebû Ubeyd el-Bekrî'nin (ö. 487) «Faslü'l-makāl fî şerhi Kitâbi'l-emsâl» adlı eseri — Ebû Ubeyd Kāsım b. Sellâm'ın Kitâbü'l-emsâl'ine Bekrî'nin şerhi (thk. İhsan Abbas ve Abdülmecîd Âbidîn, Müessesetü'r-Risâle, Beyrut 1971; Şâmile kitap 1025)"
VOWEL_AR = "الضَّبْطُ: النَّصُّ الْإِلِكْتُرُونِيُّ خَالٍ مِنَ الشَّكْلِ، فَكُلُّ حَرَكَةٍ هُنَا مِنْ ضَبْطِنَا نَحْنُ، وَكَذٰلِكَ عَلَامَاتُ التَّرْقِيمِ وَتَقْطِيعُ الْجُمَلِ؛ وَمَا لَمْ نَقْطَعْ بِضَبْطِهِ تُرِكَتْ حَرَكَتُهُ غَيْرَ مَكْتُوبَةٍ وَذُكِرَ لِلْعَالِمِ الْمُرَاجِعِ. "
VOWEL_EN = "VOWELLING: the e-text is unvowelled, so EVERY vowel in this package is ours (editorial), as are the punctuation and the division into sentences; a vowel we could not settle from the lexicon and the grammar is left UNWRITTEN on the word and listed for the scholar below. "
VOWEL_TR = "HAREKE: elektronik metin harekesizdir; bu paketteki HER hareke bize aittir (editoryal), noktalama ve cümlelere bölme de öyle; sözlük ve nahivle kesinleştiremediğimiz bir hareke kelimenin üzerine YAZILMAMIŞ ve aşağıda hocaya bırakılmıştır. "
REVIEW = "pending-scholarly-review"

LEVEL_NAME = {4: "Upper Intermediate", 5: "Advanced"}
def manifest(SLUG, level, title, subtitle, pages, pages_ar, span_en, span_tr, span_ar, corrections=(), witness_ar="", witness_en="", witness_tr="",
             hoca=(), madrib=None, kept=(), extra_en="", extra_tr="", extra_ar="", published="2026-11-26"):
    """the manifest of a proverb package: the RECEIVED-text attribution in three languages (source, span, vowelling, corrections and
    their witness, what is kept as printed, where the proverb is said if the book says so, and the points left for the hoca)"""
    cor_ar = cor_en = cor_tr = ""
    if corrections:
        lst = "؛ ".join(f"«{a}» ← «{b}»" for a, b in corrections)
        cor_ar = f"التَّصْحِيحُ: صُحِّحَ مِنْ أَخْطَاءِ النَّصِّ الْإِلِكْتُرُونِيِّ مَا يَلِي عَلَى شَاهِدٍ ثَانٍ هُوَ {witness_ar}، وَلَمْ يُصَحَّحْ شَيْءٌ غَيْرُهُ: {lst}. "
        lst = "; ".join(f"«{a}» → «{b}»" for a, b in corrections)
        cor_en = f"CORRECTIONS (e-text → now), each made against a second witness and nothing else — {witness_en}: {lst}. "
        cor_tr = f"DÜZELTMELER (elektronik metin → şimdi); her biri yalnızca ikinci bir şâhide dayanır — {witness_tr}: {lst}. "
    else:
        cor_ar = "وَلَمْ يُصَحَّحْ فِي النَّصِّ شَيْءٌ. "
        cor_en = "NO correction was made to the text. "
        cor_tr = "Metinde HİÇBİR düzeltme yapılmamıştır. "
    kept_ar = ("وَأُبْقِيَ كَمَا طُبِعَ: " + "؛ ".join(k[0] for k in kept) + ". ") if kept else ""
    kept_en = ("KEPT AS PRINTED: " + "; ".join(k[1] for k in kept) + ". ") if kept else ""
    kept_tr = ("BASKIDAKİ GİBİ BIRAKILANLAR: " + "; ".join(k[2] for k in kept) + ". ") if kept else ""
    md_ar = md_en = md_tr = ""
    if madrib:
        md_ar = "وَالْجُمْلَةُ الْأَخِيرَةُ مَضْرِبُ الْمَثَلِ بِلَفْظِ الْكِتَابِ (" + madrib[0] + "). "
        md_en = "The last sentence is where the proverb is said, in the book's own words (" + madrib[1] + "). "
        md_tr = "Son cümle, atasözünün nerede söylendiğini kitabın kendi lafzıyla bildirir (" + madrib[2] + "). "
    else:
        md_ar = "وَلَمْ يَذْكُرِ الْكِتَابُ هُنَا مَضْرِبًا لِلْمَثَلِ بِلَفْظٍ صَرِيحٍ، فَلَمْ يُزَدْ شَيْءٌ. "
        md_en = "The book states no occasion of use for this proverb here in words of its own, so none is added. "
        md_tr = "Kitap burada atasözünün kullanıldığı yeri açıkça söylemez; bu yüzden bir şey eklenmemiştir. "
    hz_en = "LEFT FOR THE SCHOLAR: " + "; ".join(h[0] for h in hoca) + ". " if hoca else ""
    hz_tr = "HOCAYA BIRAKILANLAR: " + "; ".join(h[1] for h in hoca) + ". " if hoca else ""
    hz_ar = "وَتُرِكَ لِلْعَالِمِ الْمُرَاجِعِ " + str(len(hoca)) + " مَوَاضِعَ مَذْكُورَةٌ فِي الْإِنْكِلِيزِيَّةِ وَالتُّرْكِيَّةِ. " if hoca else ""
    return {
     "id": SLUG, "storyGroup": SLUG, "title": title, "subtitle": subtitle,
     "level": level, "levelName": LEVEL_NAME[level], "version": "0.1.0", "published": published, "access": "free",
     "attribution": {
      "ar": "نَصٌّ مَنْقُولٌ بِلَفْظِهِ مِنْ " + SOURCE_AR + "، " + pages_ar + ": " + span_ar + ". " + VOWEL_AR + cor_ar + kept_ar + extra_ar + md_ar + hz_ar
            + "وَالتَّرْجَمَتَانِ الْإِنْكِلِيزِيَّةُ وَالتُّرْكِيَّةُ وَالْإِعْرَابُ مِنْ عَمَلِنَا، وَالنَّصُّ كُلُّهُ يَنْتَظِرُ مُرَاجَعَةَ الْعَالِمِ.",
      "en": "The RECEIVED text, verbatim, from " + SOURCE_EN + ", " + pages + ": " + span_en + ". The exact passage is in research/sources/" + SLUG + "-src.txt. "
            + VOWEL_EN + cor_en + kept_en + extra_en + md_en + hz_en + "The English and Turkish translations and every iʿrāb line are ours; the whole awaits a scholar's review.",
      "tr": "LAFZIYLA AKTARILAN metin: " + SOURCE_TR + ", " + pages + ": " + span_tr + ". Pasajın aynısı research/sources/" + SLUG + "-src.txt dosyasındadır. "
            + VOWEL_TR + cor_tr + kept_tr + extra_tr + md_tr + hz_tr + "İngilizce ve Türkçe tercümeler ile bütün i'râb satırları bize aittir; metnin tamamı bir âlimin incelemesini beklemektedir.",
      "reviewStatus": REVIEW,
     },
    }
