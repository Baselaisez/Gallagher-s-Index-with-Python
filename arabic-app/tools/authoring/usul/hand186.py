#!/usr/bin/env python3
"""hand186.py — (wave 186) «أَنْ يَتَفَقَّهَ» (al-Uṣūl 2:s3, word 1): the hāʾ is the verb's third radical (ف ق ه), not a pronoun.

The engine had peeled it as the object «هُ», and the token shipped with the segments «يَتَفَقَّ» + «هَ» (pron-3ms). The
line itself was right (a manṣūb muḍāriʿ with a visible fatḥa); only the split was wrong. Wave 186's corpus gate — every
attached third-person pronoun on the shelf wears the vowel the harmony rule gives it — found it: a pronoun «هَ» does
not exist.

Writes `"enc": ""` into fixes.json (so a regeneration keeps the word whole) and, with --apply, drops the segments from
the shipped token. The written vowels and the iʿrāb line are untouched.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "al-usul-al-munifa"
WHERE, BARE = "2:s3:1", "يتفقه"


def main():
    fp = HERE / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
    f[WHERE] = dict(f.get(WHERE, {}), enc="")
    json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(len(f), "fixes in fixes.json")
    if "--apply" not in sys.argv: return
    ch, sid, i = WHERE.split(":"); p = PKG / "chapters" / f"{ch}.json"
    raw = open(p, encoding="utf-8").read(); d = json.loads(raw)
    t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][int(i)]
    assert t["surface"]["bare"] == BARE, t["surface"]["bare"]
    had = t.pop("segments", None)
    out = json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else "")
    open(p, "w", encoding="utf-8").write(out)
    print("segments dropped" if had else "already whole")


if __name__ == "__main__":
    main()
