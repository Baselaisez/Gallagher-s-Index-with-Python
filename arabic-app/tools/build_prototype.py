#!/usr/bin/env python3
"""Regenerate the embedded data block in prototype/reader.html from content packages.

The prototype is a renderer; the content packages are the source of truth. This script
reads one or more story packages plus the global grammar registry, transforms them into
the JS constants the app shell expects (a STORIES array + shared GRAMMAR), and splices
them between the __DATA_START__ / __DATA_END__ markers.

Usage:
    python3 tools/build_prototype.py                       # discover all packages
    python3 tools/build_prototype.py --package <dir> --html <file>   # standalone build
    python3 tools/build_prototype.py --packages <dir> <dir> ...

Run tools/validate_content.py on each package first — this script refuses obviously
broken input but does not repeat full validation.
"""
import argparse
import json
from pathlib import Path

START = "// __DATA_START__"
END = "// __DATA_END__"

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS = [ROOT / "content/samples", ROOT / "content/user-uploads"]
IRAB_TR = ROOT / "content/i18n/irab-tr.json"


def load_irab_tr():
    """Turkish translation memory for i'rab notes, keyed by the English string.

    Chapters author i'rab as {ar, en}; the Turkish comes from this shared file so
    a phrase repeated across stories is translated once. Missing keys simply fall
    back to English in the reader — run tools/check_irab_tr.py to find them.
    """
    if not IRAB_TR.is_file():
        return {}
    return json.loads(IRAB_TR.read_text(encoding="utf-8")).get("entries", {})


def bilingual(value):
    """Normalize plain strings and {en, tr} objects to {en, tr}."""
    if isinstance(value, dict):
        return {"en": value.get("en", ""), "tr": value.get("tr", value.get("en", ""))}
    return {"en": value or "", "tr": value or ""}


def discover():
    pkgs = []
    for coll in COLLECTIONS:
        if coll.is_dir():
            pkgs += sorted(d for d in coll.iterdir() if (d / "manifest.json").is_file())
    return pkgs


def build_story(pkg: Path, irab_tr=None):
    irab_tr = irab_tr or {}
    manifest = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
    glossary = json.loads((pkg / "glossary.json").read_text(encoding="utf-8"))["entries"]

    morph = {}
    mpath = pkg / "morphology.json"
    if mpath.exists():
        for lex, m in json.loads(mpath.read_text(encoding="utf-8"))["verbs"].items():
            if m.get("jamid"):
                # Incompletely conjugating verbs carry exactly the tenses that
                # exist: لَيْسَ is mazi-only, مَا زَالَ adds a mudari and governed
                # forms but has no amr. The reader renders what is present.
                entry = {"bab": m["bab"], "wazn": m["wazn"], "jamid": True,
                         "mazi": m["mazi"]}
                for key in ("mudari", "mansub", "majzum", "majzum2", "note"):
                    if m.get(key):
                        entry[key] = m[key]
                morph[lex] = entry
                continue
            entry = {"bab": m["bab"], "wazn": m["wazn"], "masdar": m["masdar"],
                     "fail": m["ismFail"], "mazi": m["mazi"], "mudari": m["mudari"],
                     "amr": m["amr"]}
            if m.get("ismMaful"):
                entry["maful"] = m["ismMaful"]
            # Governed mudari' forms feed the Emsile-i Muhtelife table. They are
            # stored, not derived: for hollow/defective verbs the jussive is not a
            # vowel swap (يَقُولُ -> لَمْ يَقُلْ, يَرْمِي -> لَمْ يَرْمِ).
            for key in ("mansub", "majzum", "majzum2",
                        "majhulMazi", "majhulMudari"):
                if m.get(key):
                    entry[key] = m[key]
            if m.get("note"):
                entry["note"] = m["note"]
            morph[lex] = entry

    chapters = []
    for ch in manifest["chapters"]:
        data = json.loads((pkg / "chapters" / f"{ch['n']}.json").read_text(encoding="utf-8"))
        sentences = []
        for sen in data["sentences"]:
            tokens = []
            for tok in sen["tokens"]:
                # pos travels with the token: the reader needs to know whether a
                # word is a nominal before it can quiz its role in the sentence.
                t = {"s": tok["surface"], "lex": tok["lex"]}
                if tok.get("pos"):
                    t["pos"] = tok["pos"]
                for key in ("grammar", "punctAfter", "quoteBefore", "quoteAfter",
                            "irab", "phrase"):
                    if tok.get(key):
                        t[key] = tok[key]
                if t.get("irab") and t["irab"].get("en") and not t["irab"].get("tr"):
                    tr = irab_tr.get(t["irab"]["en"])
                    if tr:
                        t["irab"] = dict(t["irab"], tr=tr)
                if tok.get("segments"):
                    t["segments"] = [{"form": s["form"], "lex": s["lex"]}
                                     for s in tok["segments"]]
                tokens.append(t)
            sentence = {"id": sen["id"], "translation": sen["translation"],
                        "tokens": tokens}
            if sen.get("audio"):
                sentence["audio"] = sen["audio"]  # [startMs, endMs] — forward-prep for real narration
            if sen.get("jumal"):
                # Sentence-level i'rab (Qawa'id al-I'rab): each clause named and
                # given — or denied — its mahall. Authored trilingual in place.
                sentence["jumal"] = sen["jumal"]
            if sen.get("tashbih"):
                sentence["tashbih"] = sen["tashbih"]
            if sen.get("majaz"):
                # the authored majaz frame (wave 16): the word, its literal and intended
                # meanings, the qarina and the 'alaqa — the MajazEngine's answer key
                sentence["majaz"] = sen["majaz"]
            if sen.get("kinaya"):
                # the authored kinaya frame (wave 18): the span, its kind (sifa / mawsuf /
                # nisba), the lazim it stands for and the wasait — the KinayaEngine's answer key
                sentence["kinaya"] = sen["kinaya"]
            if sen.get("badi"):
                # the authored badi frame (wave 18): a tibaq pair with its sub-kind — the BadiEngine's key
                sentence["badi"] = sen["badi"]
            sentences.append(sentence)
        chapter = {"n": ch["n"], "title": ch["title"], "sentences": sentences}
        if ch.get("audioFile"):
            # One recorded file per chapter; sentences carry their [startMs, endMs]
            # slice of it. The reader plays this instead of synthesis wherever
            # both halves exist.
            chapter["audioFile"] = ch["audioFile"]
        chapters.append(chapter)

    return {
        "id": manifest["id"],
        "group": manifest.get("storyGroup", manifest["id"]),
        "title": manifest["title"],
        "subtitle": manifest.get("subtitle", {}),
        "level": manifest.get("level", 1),
        "levelName": manifest.get("levelName", ""),
        # The day the story entered the library — the reader sorts and badges on it.
        "published": manifest.get("published", ""),
        "access": manifest.get("access", "free"),
        "review": manifest.get("attribution", {}).get("reviewStatus", ""),
        # Wave 77: the provenance note ships to the reader (the «About this text» sheet) — what is received text,
        # what is editorial, what is in copyright, what still awaits a scholar. Honesty is a feature of the page.
        "about": {k: v for k, v in manifest.get("attribution", {}).items() if k in ("ar", "en", "tr") and isinstance(v, str) and v.strip()},
        "glossary": glossary,
        "morph": morph,
        "chapters": chapters,
    }


def build_grammar(grammar_dir: Path):
    notes = {}
    for path in sorted(grammar_dir.glob("*.json")):
        g = json.loads(path.read_text(encoding="utf-8"))
        note = {"title": g["title"], "level": g.get("level"),
                "group": g.get("group", "nahw"),
                "explanation": bilingual(g.get("explanation"))}
        # The jargon-free lede the reader meets before the classical account.
        # Only when authored: bilingual(None) is {en:'',tr:''}, which is truthy
        # in JS and would render an empty styled paragraph above the fold.
        if g.get("plain"):
            note["plain"] = bilingual(g["plain"])
        if g.get("amil"):
            note["amil"] = g["amil"]
        if g.get("mamul"):
            note["mamul"] = g["mamul"]
        if g.get("classicalSources"):
            note["sources"] = g["classicalSources"]
        # The interrogative that identifies the role — the madrasah's own way of
        # answering "how do I know which i'rab this is?".
        if g.get("question"):
            note["question"] = g["question"]
        # The worked example carries a TRANSLATED explanation, not just Arabic:
        # under TR UI an English gloss here was the last place the app still
        # spoke English to a Turkish reader.
        note["examples"] = [{"ar": x["ar"],
                             "gloss": bilingual({"en": x.get("en", ""),
                                                 "tr": x.get("tr", "")}),
                             "src": x.get("sourceStory")}
                            for x in g.get("examples", [])]
        note["mistakes"] = [{"wrong": m["wrong"], "right": m["right"],
                             "why": bilingual(m.get("why"))}
                            for m in g.get("commonMistakes", [])]
        # The dependency links the atlas draws — ids only, resolved in the reader.
        if g.get("relatedNotes"):
            note["related"] = list(g["relatedNotes"])
        notes[g["id"]] = note
    return notes


def js(name, value, parse=False):
    """a JS constant. parse=True emits JSON.parse("…") instead of the literal. Node parses the JSON string about a third
    faster (529 vs 747 ms for the 24 MB STORIES), but the whole page in Chromium at 4x CPU throttling booted LATER with it
    (12.6 s vs 10.5 s) and held a larger heap (179 vs 111 MB): the script scanner still walks the 24 MB string and then
    JSON.parse walks it again. Wave 127 measured both and kept the literal; the option stays for a future re-measurement."""
    body = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if not parse:
        return f"const {name} = {body};"
    lit = json.dumps(body, ensure_ascii=False).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return f"const {name} = JSON.parse({lit});"


def lazy_bodies(stories):
    """(wave 148) the story BODIES — chapters and morph, 23 of the 26 MB — ride inside the literal as JSON STRINGS that the
    reader parses on a story's first use (hydrateStories148 installs the getters at boot). The shelf never needs the bodies:
    it reads the precomputed counts (stats) and the new-word key list (lexNew, the token lexes whose glossary level is ≥ 1,
    in first-seen order — exactly what storyNewWords used to walk the tokens for). Boot parses ~3 MB of literal, not 26."""
    for st in stories:
        chs = st.get("chapters") or []
        gl = st.get("glossary") or {}
        sent = toks = 0; seen = []; seenset = set()
        for c in chs:
            for sn in c.get("sentences") or []:
                sent += 1
                for t in sn.get("tokens") or []:
                    toks += 1
                    lx = t.get("lex"); e = gl.get(lx) if lx is not None else None
                    if e and isinstance(e.get("level"), (int, float)) and e.get("level") >= 1 and lx not in seenset:
                        seenset.add(lx); seen.append(lx)
        st["stats"] = {"chapters": len(chs), "sentences": sent, "tokens": toks}
        st["lexNew"] = seen
        st["chapters"] = json.dumps(chs, ensure_ascii=False, separators=(",", ":"))
        if isinstance(st.get("morph"), dict):
            st["morph"] = json.dumps(st["morph"], ensure_ascii=False, separators=(",", ":"))
    return stories


CAT_START = "// __CATALOG_START__"
CAT_END = "// __CATALOG_END__"


def build_shelf_catalog(stories):
    """the one-line-per-story list the shell paints the library from BEFORE the stories are parsed (wave 127)"""
    return [{"id": st["id"], "group": st.get("group"), "title": st["title"], "subtitle": st.get("subtitle"), "level": st.get("level"),
             "levelName": st.get("levelName"), "chapters": len(st.get("chapters") or []),
             "sentences": sum(len(c.get("sentences") or []) for c in (st.get("chapters") or [])),
             "published": st.get("published"), "access": st.get("access")} for st in stories]


def load_catechism():
    """content/catechism/*.json — the madrasah's sual-cevap banks (wave 64): {book, title{en,tr}, source, items[{id, n, q, a, ar[], notes[], story?, chapter?}]}."""
    out = []
    for f in sorted((ROOT / "content/catechism").glob("*.json")) if (ROOT / "content/catechism").is_dir() else []:
        out.append(json.loads(f.read_text(encoding="utf-8")))
    return out


def build_catalog(pkgs):
    """Build a catalog.json index from discovered packages.

    Returns a catalog dict with packages sorted by level then id (stable/diff-friendly).
    Each package entry includes: id, title, level, levelName, version, access,
    storyGroup, reviewStatus, chapters (count).
    """
    catalog_packages = []
    for pkg in pkgs:
        manifest = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
        entry = {
            "id": manifest["id"],
            "title": manifest["title"],
            "level": manifest.get("level", 1),
            "levelName": manifest.get("levelName", ""),
            "version": manifest.get("version", ""),
            "published": manifest.get("published", ""),
            "access": manifest.get("access", "free"),
            "storyGroup": manifest.get("storyGroup", manifest["id"]),
            "reviewStatus": manifest.get("attribution", {}).get("reviewStatus", ""),
            "chapters": len(manifest.get("chapters", [])),
        }
        catalog_packages.append(entry)

    # Sort by level then id for deterministic output
    catalog_packages.sort(key=lambda p: (p["level"], p["id"]))

    return {
        "catalogVersion": "0.1",
        "generatedFrom": "tools/build_prototype.py",
        "packages": catalog_packages,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--package", type=Path, default=None,
                    help="build a standalone reader for a single package")
    ap.add_argument("--packages", type=Path, nargs="*", default=None)
    ap.add_argument("--grammar-dir", type=Path, default=ROOT / "content/grammar")
    ap.add_argument("--html", type=Path, default=ROOT / "prototype/reader.html")
    args = ap.parse_args()

    # Track whether we're doing a full discovery (for catalog write guard)
    is_full_discovery = False
    if args.package:
        pkgs = [args.package]
    elif args.packages:
        pkgs = args.packages
    else:
        pkgs = discover()
        is_full_discovery = True
    if not pkgs:
        raise SystemExit("no packages found")

    irab_tr = load_irab_tr()
    stories = [build_story(p, irab_tr) for p in pkgs]
    grammar = build_grammar(args.grammar_dir)
    catalog_js = js("CATALOG", build_shelf_catalog(stories))   # from the bodies, before they are folded into strings
    lazy_bodies(stories)   # (wave 148)
    block = "\n".join([
        START,
        "// Generated by tools/build_prototype.py — DO NOT EDIT BY HAND.",
        f"// Packages: {', '.join(p.name for p in pkgs)}",
        js("STORIES", stories),
        js("GRAMMAR", grammar),
        js("BAB_MODEL", json.loads((ROOT / "content/models/bab_model.json").read_text(encoding="utf-8")) if (ROOT / "content/models/bab_model.json").exists() else None),
        js("FIGURE_MODEL", json.loads((ROOT / "content/models/figure_model.json").read_text(encoding="utf-8")) if (ROOT / "content/models/figure_model.json").exists() else None),
        # (wave 136) the IrabModel's weights, fitted by tools/gen_irab_model.js and gated against a fresh fit; the reader
        # reads them only when their corpus signature is its own (the single-package hadith reader trains as before)
        js("IRAB_MODEL", json.loads((ROOT / "content/models/irab_model.json").read_text(encoding="utf-8")) if (ROOT / "content/models/irab_model.json").exists() else None),
        js("CATECHISM", load_catechism()),
        # (wave 158) the derivation law table — one JSON, read by the reader's IshtiqaqEngine and by qissa_core alike
        js("ISHTIQAQ_LAW", json.loads((ROOT / "content/rules/ishtiqaq.json").read_text(encoding="utf-8")) if (ROOT / "content/rules/ishtiqaq.json").exists() else None),
        js("REF_GROUPS", [
            {"id": "sarf", "ar": "الصَّرْف",
             "label": {"en": "Morphology — after Emsile & Bina",
                       "tr": "Sarf — Emsile ve Binâ'ya göre"}},
            {"id": "nahw", "ar": "النَّحْو",
             "label": {"en": "Syntax — after al-Kafiya & Qatr al-Nada",
                       "tr": "Nahiv — Kâfiye ve Katru'n-Nedâ'ya göre"}},
            {"id": "awamil", "ar": "الْعَوَامِل",
             "label": {"en": "Governors — after Birgivi's Awamil",
                       "tr": "Âmiller — Birgivî'nin Avâmil'ine göre"}},
            {"id": "arud", "ar": "الْعَرُوض",
             "label": {"en": "Prosody — the metres and the rhyme, after al-Khalil",
                       "tr": "Arûz — bahirler ve kafiye, Halîl'e göre"}},
            {"id": "balagha", "ar": "الْبَلَاغَة",
             "label": {"en": "Rhetoric — after al-Qazwini's Talkhis",
                       "tr": "Belâgat — Kazvînî'nin Telhîs'ine göre"}},
            {"id": "bayan", "ar": "الْبَيَان",
             "label": {"en": "Figuration — the Talkhis, Fann 2: tashbih, majaz, kinaya",
                       "tr": "Beyân — Telhîs'in ikinci fenni: teşbih, mecaz, kinaye"}},
            {"id": "badi", "ar": "الْبَدِيع",
             "label": {"en": "Embellishment — the Talkhis, Fann 3: tibaq, muqabala, jinas",
                       "tr": "Bedî' — Telhîs'in üçüncü fenni: tıbâk, mukabele, cinas"}},
        ]),
        # (wave 127) the data script is the LAST script of the page; this line hands the shell its data
        'if (typeof window.__qissaDataReady === "function") window.__qissaDataReady();',
        END,
    ])

    html = args.html.read_text(encoding="utf-8")
    i, j = html.find(START), html.find(END)
    if i == -1 or j == -1:
        raise SystemExit(f"markers {START} / {END} not found in {args.html}")
    html = html[:i] + block + html[j + len(END):]
    # (wave 127) the catalog at the top of the code script — the skeleton library is drawn from it before the data parses
    ci, cj = html.find(CAT_START), html.find(CAT_END)
    if ci == -1 or cj == -1:
        raise SystemExit(f"markers {CAT_START} / {CAT_END} not found in {args.html} — the reader predates wave 127")
    html = html[:ci] + "\n".join([CAT_START, catalog_js, CAT_END]) + html[cj + len(CAT_END):]
    args.html.write_text(html, encoding="utf-8")
    n_tokens = sum(st["stats"]["tokens"] for st in stories)   # (wave 148) the bodies are strings now
    print(f"Rebuilt {args.html}: {len(stories)} stories, {n_tokens} tokens, "
          f"{len(grammar)} grammar notes")

    # Build and write catalog only on full discovery, not on --package single builds
    if is_full_discovery:
        catalog = build_catalog(pkgs)
        catalog_path = ROOT / "content/catalog.json"
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"Wrote catalog.json: {len(catalog['packages'])} packages")


if __name__ == "__main__":
    main()
