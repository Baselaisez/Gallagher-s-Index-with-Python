"""khasais_common — the shared kit of the shelf «مِنْ كُتُبِ الْعَرَبِيَّةِ» (v352-K): readings from Ibn Jinnī's al-Khaṣāʾiṣ.

Each package `khasais-<slug>` is ONE passage of Ibn Jinnī's own prose — the opening (or a whole part) of one bāb of «الخصائص»
(ed. Muḥammad ʿAlī al-Najjār, al-Hayʾa al-Miṣriyya al-ʿĀmma li-l-Kitāb, 4th ed., 3 vols; Shamela 9986;
research/sources/al-khasais-ibn-jinni-src.txt), cut at a natural join and never trimmed inside a sentence. The script
tools/authoring/author_<slug>.py is the package's source of truth; it writes the sentences and calls `finish()` here (the
proverbs' finish of amthal_common.py, v348-A, with the sibling prefix `khasais-`).

RULES (v333, carried): the e-text is UNVOWELLED, so every vowel is ours and the manifest says so; the text is never retold,
re-ordered or silently corrected — a correction is made only against a named witness and is listed in the attribution; a vowel
we cannot settle from the lexicon and the grammar is LEFT UNWRITTEN and listed «for the hoca». The exact passage is saved
first as research/sources/<slug>-src.txt.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *        # noqa: F401,F403 — the kit, the proverbs' helpers (NOTE, W, ISTI, MUDAF, SILA_, MAQUL …)
from amthal_common import ROOT, OUT_ROOT, N, PRE, SG
import json, os, unicodedata, collections, re

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
        holders = [(p, G[p][k]) for p in PKGS if k in G[p] and not (p.startswith("khasais-") and k in NEW_GLOSS)]
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
        # a key is a global claim: only a sibling Khaṣāʾiṣ reading may hold it, and only for the same lemma
        hit = [p for p in PKGS if k in G[p] and not (p.startswith("khasais-") and _lemma_id(G[p][k]) == _lemma_id(e))]
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
        if k not in V:          # a verb a sibling Khaṣāʾiṣ reading coined: its paradigm travels with the key
            for p in PKGS:
                if p.startswith("khasais-") and k in M[p]: V[k] = M[p][k]; break
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

# ---- the shelf's own kit -------------------------------------------------------------------------------------------------
PF = {"wa": ("وَ", "wa", "conj"), "fa": ("فَ", "fa", "conj"), "bi": ("بِ", "bi", "prep"), "li": ("لِ", "li", "prep"),
      "ka": ("كَ", "ka", "prep"), "a": ("أَ", "hamza-istifham", "part"), "la": ("لَ", "la-ibtida", "part")}
def X(full, lex, pos, g, ar, en, tr, p=None, pre=(), enc=None, s=None, spos=None):
    """one token; `pre` names its fused prefixes in order (wa, fa, bi, li, ka, a, la), `enc` its attached pronoun, `s`/`spos` the stem's
    lex and part of speech when the token's own lex is the prefix (a jarr letter carries the token, as on the whole shelf)"""
    if not pre and not enc: return tok(full, lex, pos, g, ar, en, tr, punct=p)
    rest, segs = N(full), []
    for k in pre:
        f = PF[k][0]
        if k == "li" and rest.startswith("لِلْ"): segs.append(seg(*PF[k])); rest = "الْ" + rest[4:]; continue
        assert rest.startswith(f), (full, k); segs.append(seg(*PF[k])); rest = rest[len(f):]
    tail = None
    if enc == "نَا" and rest.endswith("نَّا"):          # عَنَّا، مِنَّا: the corpus splits «عَن» + «نَا»
        rest, tail = rest[:-4] + "ن", seg("نَا", "pron-1p", "pron")
    elif enc:
        assert rest.endswith(enc), (full, enc); rest = rest[:-len(enc)]; tail = seg(enc, PRON[enc], "pron")
    segs.append(seg(rest, s or lex, spos or pos))
    if tail: segs.append(tail)
    return tok(full, lex, pos, g, ar, en, tr, punct=p, segments=segs)
def SEN(i, en, tr, toks): return {"id": "s%d" % i, "translation": {"en": en, "tr": tr}, "tokens": toks}

SOURCE_AR = "«الْخَصَائِصُ» لِأَبِي الْفَتْحِ عُثْمَانَ بْنِ جِنِّي (ت ٣٩٢ هـ)، بِتَحْقِيقِ مُحَمَّدِ عَلِي النَّجَّارِ، الْهَيْئَةُ الْمِصْرِيَّةُ الْعَامَّةُ لِلْكِتَابِ، ط ٤ (الشَّامِلَةُ ٩٩٨٦)"
SOURCE_EN = "«al-Khaṣāʾiṣ» by Abū al-Fatḥ ʿUthmān Ibn Jinnī (d. 392 AH), ed. Muḥammad ʿAlī al-Najjār, al-Hayʾa al-Miṣriyya al-ʿĀmma li-l-Kitāb, 4th ed., 3 vols (Shamela book 9986)"
SOURCE_TR = "İbn Cinnî'nin (Ebü'l-Feth Osman, ö. 392) «el-Hasâis» adlı eseri (thk. Muhammed Ali en-Neccâr, el-Hey'etü'l-Mısriyye el-Âmme li'l-Kitâb, 4. bs., 3 cilt; Şâmile kitap 9986)"
LEVEL_NAME = {5: "Advanced", 6: "Master"}

def manifest(SLUG, level, title, subtitle, bab_ar, bab_en, bab_tr, vol, pages, shamela, span_en, span_tr, span_ar, corrections=(), witness_ar="",
             witness_en="", witness_tr="", hoca=(), left_en="", left_tr="", left_ar="", extra_en="", extra_tr="", extra_ar="", published="2026-11-26"):
    """the manifest of a Khaṣāʾiṣ reading: the RECEIVED-text attribution in three languages — the bāb, volume and printed page, the
    span, the vowelling declared ours, the corrections and their witness, what was left of the bāb, and the points left for the hoca"""
    where_ar = f"«{bab_ar}»، الْجُزْءُ {vol}، ص {pages} (الشَّامِلَةُ ص {shamela})"
    where_en = f"the bāb «{bab_ar}» ({bab_en}), vol. {vol}, printed p. {pages} (Shamela p. {shamela})"
    where_tr = f"«{bab_ar}» bâbı ({bab_tr}), cilt {vol}, matbû s. {pages} (Şâmile s. {shamela})"
    if corrections:
        lst = "؛ ".join(f"«{a}» ← «{b}»" for a, b in corrections)
        cor_ar = f"التَّصْحِيحُ: صُحِّحَ مِنْ أَخْطَاءِ النَّصِّ الْإِلِكْتُرُونِيِّ مَا يَلِي عَلَى شَاهِدٍ هُوَ {witness_ar}، وَلَمْ يُصَحَّحْ شَيْءٌ غَيْرُهُ: {lst}. "
        lst = "; ".join(f"«{a}» → «{b}»" for a, b in corrections)
        cor_en = f"CORRECTIONS (e-text → now), each made against a named witness and nothing else — {witness_en}: {lst}. "
        cor_tr = f"DÜZELTMELER (elektronik metin → şimdi); her biri yalnızca adı geçen bir şâhide dayanır — {witness_tr}: {lst}. "
    else:
        cor_ar, cor_en, cor_tr = "وَلَمْ يُصَحَّحْ فِي النَّصِّ شَيْءٌ. ", "NO correction was made to the text. ", "Metinde HİÇBİR düzeltme yapılmamıştır. "
    lf_ar = ("وَمَا تُرِكَ مِنَ الْبَابِ: " + left_ar + ". ") if left_ar else ""
    lf_en = ("LEFT OUT of the bāb: " + left_en + ". ") if left_en else ""
    lf_tr = ("BÂBDAN ALINMAYAN: " + left_tr + ". ") if left_tr else ""
    hz_en = "LEFT FOR THE SCHOLAR: " + "; ".join(h[0] for h in hoca) + ". " if hoca else ""
    hz_tr = "HOCAYA BIRAKILANLAR: " + "; ".join(h[1] for h in hoca) + ". " if hoca else ""
    hz_ar = "وَتُرِكَ لِلْعَالِمِ الْمُرَاجِعِ " + str(len(hoca)) + " مَوَاضِعَ مَذْكُورَةٌ فِي الْإِنْكِلِيزِيَّةِ وَالتُّرْكِيَّةِ. " if hoca else ""
    return {
     "id": SLUG, "storyGroup": SLUG, "title": title, "subtitle": subtitle,
     "level": level, "levelName": LEVEL_NAME[level], "version": "0.1.0", "published": published, "access": "free",
     "attribution": {
      "ar": "نَصٌّ مَنْقُولٌ بِلَفْظِهِ مِنْ " + SOURCE_AR + "، مِنْ بَابِ " + where_ar + ": " + span_ar + ". " + VOWEL_AR + cor_ar + lf_ar + extra_ar + hz_ar
            + "وَالتَّرْجَمَتَانِ الْإِنْكِلِيزِيَّةُ وَالتُّرْكِيَّةُ وَالْإِعْرَابُ مِنْ عَمَلِنَا، وَالنَّصُّ كُلُّهُ يَنْتَظِرُ مُرَاجَعَةَ الْعَالِمِ.",
      "en": "The RECEIVED text, verbatim — Ibn Jinnī's own prose — from " + SOURCE_EN + ", " + where_en + ": " + span_en + ". The exact passage is in research/sources/" + SLUG + "-src.txt. "
            + VOWEL_EN + cor_en + lf_en + extra_en + hz_en + "The English and Turkish translations and every iʿrāb line are ours; the whole awaits a scholar's review.",
      "tr": "LAFZIYLA AKTARILAN metin — İbn Cinnî'nin kendi nesri: " + SOURCE_TR + ", " + where_tr + ": " + span_tr + ". Pasajın aynısı research/sources/" + SLUG + "-src.txt dosyasındadır. "
            + VOWEL_TR + cor_tr + lf_tr + extra_tr + hz_tr + "İngilizce ve Türkçe tercümeler ile bütün i'râb satırları bize aittir; metnin tamamı bir âlimin incelemesini beklemektedir.",
      "reviewStatus": REVIEW,
     },
    }
