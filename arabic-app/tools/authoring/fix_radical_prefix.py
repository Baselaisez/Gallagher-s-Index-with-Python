#!/usr/bin/env python3
"""fix_radical_prefix.py [--write] — a verb's own first radical is not a conjunction (وَجَدَ، وَصَلُوا، فَرِحَ، فَعَلَ).

The story generators (and one path of the engine builder) peeled a leading وَ / فَ off any word and wrote «الْوَاوُ
عَاطِفَةٌ، وَفِعْلٌ مَاضٍ …» with segments [وَ + جَدَ]. Where the WHOLE written word is a cell of the verb's stored māḍī
and the remainder is no cell of it at all, the letter is the root's: the conjunction is taken off the line, the
segments are rejoined, and nothing else in the token is touched. Vowels are compared exactly (NFC) — «ضَعَ» is not the
imperative «ضَعْ» — so a real «وَ + دَعُوا» (an imperative after a wāw) is left alone.

It also re-keys the detached pronoun behind a conjunction that was filed under a noun of the same letters
(وَهُمْ → `hum`, not وَهْم «delusion»; فَهُمَا → `huma`, not فَهْم)."""
import sys, json, glob, os, re, unicodedata, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent / "content"
N = lambda s: unicodedata.normalize("NFC", s)
PRON = {"هم": "hum", "هما": "huma", "هو": "huwa", "هي": "hiya", "هن": "hunna"}
PREF = {"wa": ("الْوَاوُ عَاطِفَةٌ، وَ", "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "الْوَاوُ حَالِيَّةٌ، وَ"), "fa": ("الْفَاءُ عَاطِفَةٌ، وَ", "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ")}
EN_PRE = re.compile(r"^(?:The (?:waw|fa|wāw|fāʾ) (?:conjoins|resumes)[;,] |«and» \+ |«so» \+ |«then» \+ )", re.I)
TR_PRE = re.compile(r"^(?:«ve» \+ |«bunun üzerine» \+ |«de» \+ |Vâv atıf harfi[;,] |Fâ atıf harfi[;,] )")


def cells(m):
    c = set()
    for k in ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2"):
        v = m.get(k)
        for x in (v if isinstance(v, list) else [v]):
            if isinstance(x, str): c.add(N(x))
    for k in ("majhulMazi", "majhulMudari"):
        if isinstance(m.get(k), str): c.add(N(m[k]))
    return c


def main():
    write = "--write" in sys.argv
    pkgs = sorted(glob.glob(str(ROOT / "samples" / "*")) + glob.glob(str(ROOT / "user-uploads" / "*")))
    ALL = {}; GL = {}
    for pk in pkgs:
        try: ALL.update(json.load(open(pk + "/morphology.json", encoding="utf-8")).get("verbs", {}))
        except Exception: pass
        try: GL.update(json.load(open(pk + "/glossary.json", encoding="utf-8")).get("entries", {}))
        except Exception: pass
    nv = npn = 0
    for pk in pkgs:
        try: G = json.load(open(pk + "/glossary.json", encoding="utf-8")); E = G.get("entries", {})
        except Exception: continue
        gdirty = False
        for f in sorted(glob.glob(pk + "/chapters/*.json"), key=lambda x: int(os.path.basename(x)[:-5])):
            d = json.load(open(f, encoding="utf-8")); dirty = False
            for s in d["sentences"]:
                for i, t in enumerate(s["tokens"]):
                    sg = t.get("segments") or []
                    if len(sg) < 2 or sg[0].get("lex") not in ("fa", "wa"): continue
                    where = f"{os.path.basename(pk)} {os.path.basename(f)[:-5]}:{s['id']}:{i} {t['surface']['full']}"
                    # (b) the detached pronoun filed under a noun
                    rest_b = t["surface"]["bare"][1:]
                    if rest_b in PRON and t.get("pos") == "pron" and sg[1].get("lex") != PRON[rest_b] and "ضَمِيرٌ مُنْفَصِلٌ" in t["irab"]["ar"] and (E.get(sg[1].get("lex")) or GL.get(sg[1].get("lex")) or {}).get("pos") not in ("pron", None):   # only where the key is another word's (a noun's) — a package's own pronoun key is left alone
                        key = PRON[rest_b]
                        if key not in E and key not in GL: print("NO KEY", key, where); continue
                        print(f"PRON {where}: {sg[1].get('lex')} → {key}"); npn += 1
                        if key not in E: E[key] = GL[key]; gdirty = True
                        t["lex"] = key; sg[1]["lex"] = key; sg[1]["pos"] = "pron"; dirty = True
                        continue
                    # (a) the radical letter of a māḍī
                    m = ALL.get(sg[1].get("lex"))
                    if not m: continue
                    mz = {N(x) for x in (m.get("mazi") or []) if isinstance(x, str)}; C = cells(m)
                    tail = sg[2:] if len(sg) > 2 else []
                    obj = [g for g in tail if str(g.get("lex", "")).startswith("pron-") and not re.fullmatch(r"[اوُْ]+", N(g["form"]))]   # an object pronoun (ـهُ، ـهَا) — not the doer's وا / ا
                    doer = [g for g in tail if g not in obj]
                    whole = N(sg[0]["form"] + sg[1]["form"] + "".join(g["form"] for g in doer)); rest = N(sg[1]["form"] + "".join(g["form"] for g in doer))
                    ar = t["irab"]["ar"]; pre = next((p for p in PREF[sg[0]["lex"]] if ar.startswith(p)), None)
                    says_mazi = pre is not None and ar[len(pre):].startswith("فِعْلٌ مَاضٍ")
                    if whole not in mz or (rest in mz if says_mazi else rest in C): continue   # the line itself says «مَاضٍ»: then the remainder must be a māḍī cell for the split to stand (وَقَعُوا is no «قَعُوا» in the past)
                    if pre is None: print("LINE?", where, "|", ar[:60]); continue
                    print(f"VERB {where} [{sg[1]['lex']}]\n   - {ar[:100]}\n   + {ar[len(pre):][:100]}"); nv += 1
                    t["irab"] = {"ar": ar[len(pre):], "en": EN_PRE.sub("", t["irab"]["en"]), "tr": TR_PRE.sub("", t["irab"]["tr"])}
                    if re.match(r"^(?:a|an|the) ", t["irab"]["en"]):   # the engine builder lower-cased «A past verb …» behind its prefix; the story kit's lines («past verb built on …») open in lower case natively
                        for k in ("en", "tr"): t["irab"][k] = t["irab"][k][:1].upper() + t["irab"][k][1:]
                    new = [{"form": sg[0]["form"] + sg[1]["form"], "lex": sg[1]["lex"], "pos": sg[1].get("pos", "verb")}] + tail
                    if len(new) == 1: t.pop("segments", None)
                    else: t["segments"] = new
                    dirty = True
            if dirty and write: json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if gdirty and write: json.dump(G, open(pk + "/glossary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{nv} verbs, {npn} pronouns" + ("" if write else " — dry run"))


if __name__ == "__main__":
    main()
