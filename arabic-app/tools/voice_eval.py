#!/usr/bin/env python3
"""voice_eval.py — v349: is a synthetic voice reading the WRITTEN vowels? Evidence instead of listening.

    python3 tools/voice_eval.py --make                 # (re)write the expected column of tools/voice_testset.txt by rule
    python3 tools/voice_eval.py --score ENGINE.tsv     # score an engine's phoneme output (id<TAB>ipa) against the set
    python3 tools/voice_eval.py --g2p 'نَصٌّ مُشَكَّلٌ'      # the reference reading of any vowelled text

The reference reading is a learner's reading «وَصْلًا»: every case ending and tanwīn is PRONOUNCED, also before a comma and
at the end of the sentence (the app's explicit choice); the waqf column only says what a pause would drop. Rules applied
(all read from the written marks, nothing guessed): short vowels / tanwīn (-un -an -in; the silent alif after -an); sukūn;
shadda = a doubled consonant; the article — sun letters assimilate (al-shams → aʃʃams), moon letters keep l; hamzat al-waṣl
— elided in connected speech after a vowel (fī l-bayt → fi lbajt: the long vowel before the cluster is shortened), said
ʔa-/ʔi-/ʔu- only after a pause; tāʾ marbūṭa = t (h only at a pause); alif maqṣūra = aː (a before a waṣl cluster); madd —
ا و ي after their vowel, the dagger alif, آ = ʔaː; و after the plural ending + its silent alif; الله = (ʔa)llaːh-.
Tajwīd assimilations (iqlāb, idghām of n) are NOT required of a learner's reading and are not scored.

Scoring: the engine's IPA is normalised (stress, syllable dots, ties dropped; espeak's s̪/t̪ = sˤ/tˤ, χ = x, au/ai = aw/aj)
and aligned with the reference; a word's ENDING is right when its last two phonemes are matched. A sentence is right when
every ending is (the final word counted separately: an engine that pauses there drops it by design — 'pausal').
"""
import argparse, difflib, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
TESTSET = ROOT / "tools/voice_testset.txt"

FA, DA, KA, FN, DN, KN, SH, SK, DAG = "ًٌٍَُِّْٰ"
VOW = {FA: "a", DA: "u", KA: "i"}
TAN = {FN: "a", DN: "u", KN: "i"}
CONS = {"ء": "ʔ", "أ": "ʔ", "إ": "ʔ", "ؤ": "ʔ", "ئ": "ʔ", "ب": "b", "ت": "t", "ث": "θ", "ج": "dʒ", "ح": "ħ", "خ": "x",
        "د": "d", "ذ": "ð", "ر": "r", "ز": "z", "س": "s", "ش": "ʃ", "ص": "sˤ", "ض": "dˤ", "ط": "tˤ", "ظ": "ðˤ", "ع": "ʕ",
        "غ": "ɣ", "ف": "f", "ق": "q", "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w", "ي": "j", "ة": "t"}
SUN = set("تثدذرزسشصضطظلن")
PROCLITIC = set("وفبكل")
LONG = {"aː": "a", "iː": "i", "uː": "u"}


def units(word):
    """[(letter, marks-string)] — the marks that follow each letter, whatever their stored order."""
    out = []
    for ch in word:
        if "ً" <= ch <= "ْ" or ch in (DAG, "ٓ", "ٔ", "ٕ"):
            if out:
                out[-1][1] += ch
        elif "ء" <= ch <= "ي" or ch in "آ":
            out.append([ch, ""])
    return out


def word_core(u):
    """index where the stem starts after short proclitics (وَ فَ بِ كَ لِ + an optional second one)."""
    k = 0
    while k < len(u) - 2 and u[k][0] in PROCLITIC and any(v in u[k][1] for v in (FA, KA)) and SH not in u[k][1]:
        k += 1
    return k


def read_word(word):
    """the word's phonemes in connected speech, with markers: returns (phonemes, starts_with_wasl, wasl_vowel)."""
    u = units(word)
    if not u:
        return [], False, ""
    bare = "".join(c for c, _ in u)
    core = word_core(u)
    ph, wasl, wv = [], False, ""
    m = re.fullmatch(r"([وفبكل]?)(ا?)لله", bare)
    if m:                                   # الله: (ʔa)llaːh + its ending
        pre = m.group(1)
        if pre:
            ph += [CONS[pre], VOW.get(next((x for x in u[0][1] if x in VOW), FA), "a")]
        if m.group(2) and not pre:
            wasl, wv = True, "a"
        end = u[-1][1]
        ph += ["l", "l", "aː", "h"] + ([VOW[x] for x in end if x in VOW][:1]) + (["n"] if any(x in TAN for x in end) else [])
        if any(x in TAN for x in end):
            ph[-2:-1] = [TAN[next(x for x in end if x in TAN)]]
        return ph, wasl, wv
    i = 0
    while i < len(u):
        c, mk = u[i]
        prev = u[i - 1] if i else None
        if c == "ا":
            nxt = u[i + 1] if i + 1 < len(u) else None
            cluster = nxt is not None and (SK in nxt[1] or (nxt[0] == "ل" and not nxt[1]))
            if i == 0 or (i <= core and core > 0 and cluster and not any(v in mk for v in VOW)):
                # hamzat al-waṣl at the head of the word (after proclitics it is silent; at the very head, it is the
                # caller's choice: elided after a vowel, ʔ+vowel after a pause)
                if i == 0:
                    wasl = True
                    wv = VOW.get(next((x for x in mk if x in VOW), ""), "") or (
                        "a" if nxt and nxt[0] == "ل" and (SK in nxt[1] or not nxt[1]) else "i")
                i += 1
                continue
            if prev and FN in prev[1]:
                i += 1; continue                                   # silent alif after -an
            if prev and FA in prev[1] and not any(v in mk for v in VOW):
                if ph and ph[-1] == "a":
                    ph[-1] = "aː"
                else:
                    ph.append("aː")
                i += 1; continue
            i += 1; continue                                       # الِاثْنَيْنِ / plural و + ا : silent
        if c == "آ":
            ph += ["ʔ", "aː"]; i += 1; continue
        if c == "ى" and not any(v in mk for v in list(VOW) + [SK]):
            if ph and ph[-1] == "a":
                ph[-1] = "aː"
            elif DAG in mk:
                ph.append("aː")
            i += 1; continue
        if c in "وي" and not any(v in mk for v in list(VOW) + [SH, SK] + list(TAN)) and ph:
            want = "u" if c == "و" else "i"
            if ph[-1] == want:
                ph[-1] = want + "ː"; i += 1; continue
        # the article: ال + sun letter (shadda) → assimilated; with moon letter → l
        if c == "ل" and i + 1 < len(u) and not mk and (u[i - 1][0] == "ا" if i else False) and SH in u[i + 1][1]:
            i += 1; continue
        if c == "ل" and i + 1 < len(u) and not mk and i == core and core > 0 and u[i - 1][0] == "ل" and SH in u[i + 1][1]:
            i += 1; continue                                       # لِلنَّاسِ: li + (a)n-nās
        p = CONS.get(c, "ʔ" if c in "ءأإؤئ" else "")
        if not p:
            i += 1; continue
        ph.append(p)
        if SH in mk:
            ph.append(p)
        for x in mk:
            if x in VOW:
                ph.append(VOW[x])
            elif x in TAN:
                ph += [TAN[x], "n"]
        if DAG in mk:
            if ph and ph[-1] == "a":
                ph[-1] = "aː"
            else:
                ph.append("aː")
        i += 1
    return ph, wasl, wv


def g2p(text, marks=None):
    """[[phonemes] per word] in a connected learner's reading; punctuation marks a pause (waṣl alif said after it).
    With a list in `marks`, each pause's punctuation is recorded there as (index of the word before it, mark)."""
    words, out, pause = re.findall(r"[^\s،؛؟!.:,]+|[،؛؟!.:,]", text), [], True
    for w in words:
        if re.fullmatch(r"[،؛؟!.:,]", w):
            pause = True
            if marks is not None and out:
                marks.append((len(out) - 1, w))
            continue
        ph, wasl, wv = read_word(w)
        if wasl:
            if pause or not out:
                ph = ["ʔ", wv or "a"] + ph
            else:
                last = out[-1]
                if last and last[-1] in LONG:
                    last[-1] = LONG[last[-1]]                     # fī l- → fi l-
                elif last and last[-1] not in ("a", "i", "u"):
                    # a consonant (sukūn or tanwīn) before the cluster takes a helping vowel: min → mina, -un → -uni
                    last.append("a" if "".join(last) == "min" else ("u" if "".join(last[-2:]) in ("hm", "km", "tm") else "i"))
        out.append(ph)
        pause = False
    return out


VOWELS = ("a", "i", "u", "aː", "iː", "uː")


def syllables(word):
    """split one word's phonemes into syllables (onset + vowel + coda); a leading cluster stays with the first."""
    vs = [k for k, p in enumerate(word) if p in VOWELS]
    if not vs:
        return [word]
    out, start = [], 0
    for n, k in enumerate(vs):
        nxt = vs[n + 1] if n + 1 < len(vs) else None
        end = len(word) if nxt is None else (nxt - 1 if nxt - 1 > k else nxt)
        out.append(word[start:end]); start = end
    return out


def stress(word):
    """the stressed syllable by the classical rule a teacher gives: the last of the final three that is heavy
    (long vowel or closed), counting from the penult; else the antepenult; a one- or two-syllable word: the first."""
    syl = syllables(word)
    n = len(syl)
    if n <= 2:
        return 0
    heavy = lambda x: x[-1] not in VOWELS or x[-1] in ("aː", "iː", "uː")
    last = syl[-1]
    if last[-1] not in VOWELS and (any(p in ("aː", "iː", "uː") for p in last) or last[-2] not in VOWELS):
        return n - 1                                       # superheavy final (CVVC, CVCC): only at a pause
    if heavy(syl[-2]):
        return n - 2
    return n - 3


# eSpeak NG's own Arabic phoneme names (its `-x` output): the app's reading can be handed to it as [[…]] phonemes, so
# the engine's letter-to-sound rules are bypassed and what is said is exactly what the reading above says.
ESPEAK = {"ʔ": "?", "θ": "T", "dʒ": "dZ", "ħ": "H", "x": "X", "ð": "D", "r": "R", "ʃ": "S", "sˤ": "s[", "dˤ": "dH",
          "tˤ": "t[", "ðˤ": "Z", "ʕ": "A", "ɣ": "Q", "aː": "a:", "iː": "i:", "uː": "u:"}


def espeak_phonemes(text):
    """the sentence as eSpeak NG phoneme input: [[…]] per phrase, the stored punctuation between them (it pauses there)."""
    marks = []
    words = g2p(text, marks)
    after = dict(marks)
    out, cur = [], []
    for k, w in enumerate(words):
        syl, st = syllables(w), stress(w)
        cur.append("".join(("'" if j == st and len(syl) > 1 else "") + "".join(ESPEAK.get(p, p) for p in sy) for j, sy in enumerate(syl)))
        if k in after:
            out.append("[[" + " ".join(cur) + "]]" + after[k]); cur = []
    if cur:
        out.append("[[" + " ".join(cur) + "]]")
    return " ".join(out)


def waqf(word_ph):
    """what a pause at this word would say: the short ending and tanwīn drop (-an → -aː), t marbūṭa → h."""
    p = list(word_ph)
    if len(p) >= 2 and p[-1] == "n" and p[-2] in "aui":
        if p[-2] == "a" and not (len(p) > 2 and p[-3] == "t"):
            return p[:-2] + ["aː"]
        p = p[:-2]
    elif p and p[-1] in ("a", "i", "u"):
        p = p[:-1]
    if p and p[-1] == "t" and len(p) > 1 and p[-2] in ("a", "aː"):
        p[-1] = "h"
    return p


def fmt(words):
    return " ".join("".join(w) for w in words)


# ---- engine output → phoneme lists ----
MULTI = ["dʒ", "sˤ", "dˤ", "tˤ", "ðˤ", "aː", "iː", "uː"]


def tokenize_ipa(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"[ˈˌ.‿͡,:;!?،؛؟]", "", s)
    s = s.replace("s̪", "sˤ").replace("t̪", "tˤ").replace("χ", "x").replace("ɡ", "g").replace("ʒ", "ʒ")
    s = s.replace("d ʒ", "dʒ")
    words = []
    for w in s.split():
        toks, k = [], 0
        while k < len(w):
            two = w[k:k + 2]
            if two in MULTI:
                toks.append(two); k += 2
            elif w[k] == "ː" and toks and toks[-1] not in ("a", "i", "u"):
                if not toks[-1].endswith("ː"):
                    toks.append(toks[-1])                          # espeak writes a geminate as C + ː
                k += 1
            elif w[k] in "ːˤ" and toks:
                toks[-1] += w[k]; k += 1
            else:
                toks.append(w[k]); k += 1
        # diphthongs written au / ai
        for j in range(1, len(toks)):
            if toks[j - 1] == "a" and toks[j] in ("u", "i") and (j + 1 == len(toks) or toks[j + 1] not in ("a", "i", "u", "aː", "iː", "uː")):
                toks[j] = "w" if toks[j] == "u" else "j"
        words.append(toks)
    return words


def score(exp_words, got_words):
    """→ (endings right, endings total, final ending right?, per-word misses, PER)"""
    E, G, ends, joins = [], [], [], []
    V = ("a", "i", "u", "aː", "iː", "uː")
    for w in exp_words:
        if E and len(w) > 1 and w[0] not in V and w[1] not in V:
            joins.append(len(E))             # a word that begins with a cluster: hamzat al-waṣl elided here
        E += w + ["#"]
        ends.append(len(E) - 2)              # index of the word's last phoneme
    for w in got_words:
        G += w + ["#"]
    sm = difflib.SequenceMatcher(None, E, G, autojunk=False)
    ok, to_g = set(), {}
    for tag, a1, a2, b1, _ in sm.get_opcodes():
        if tag == "equal":
            ok.update(range(a1, a2))
            to_g.update({a1 + d: b1 + d for d in range(a2 - a1)})
    jr = sum(1 for j in joins if j in to_g and to_g[j] > 0 and G[to_g[j] - 1] == "#")
    right = [e in ok and (e - 1) in ok for e in ends]
    edits = sum(max(a2 - a1, b2 - b1) for t, a1, a2, b1, b2 in sm.get_opcodes() if t != "equal")
    misses = [i for i, r in enumerate(right) if not r]
    return sum(right[:-1]), len(right) - 1, right[-1], misses, edits / max(1, len(E)), jr, len(joins)


def load_set():
    rows = []
    for line in TESTSET.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        f = line.split("\t")
        rows.append({"id": f[0], "tags": f[1], "source": f[2], "text": f[3], "expected": f[4], "waqf": f[5] if len(f) > 5 else ""})
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--make", action="store_true")
    ap.add_argument("--score", nargs="+")
    ap.add_argument("--g2p")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.g2p:
        print(fmt(g2p(a.g2p)))
        return 0
    if a.make:
        head, body = [], []
        for line in TESTSET.read_text(encoding="utf-8").splitlines():
            if line.startswith("#") or not line.strip():
                head.append(line); continue
            f = line.split("\t")[:4]
            ws = g2p(f[3])
            body.append("\t".join(f + [fmt(ws), "".join(waqf(ws[-1]))]))
        TESTSET.write_text("\n".join(head + body) + "\n", encoding="utf-8")
        print(f"wrote {len(body)} expected readings")
        return 0
    if a.score:
        rows = load_set()
        import json
        res = {}
        for path in a.score:
            got = dict(l.split("\t", 1) for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines() if "\t" in l)
            tot = dict(sent=0, sent_nonfinal=0, ends=0, n=0, final=0, per=0.0, joins=0, nj=0, misses=[])
            for r in rows:
                exp = [w for w in r["expected"].split()]
                expw = [tokenize_ipa(w)[0] for w in exp]
                gotw = tokenize_ipa(got.get(r["id"], ""))
                k, n, fin, miss, per, jr, nj = score(expw, gotw)
                tot["joins"] += jr; tot["nj"] += nj
                tot["ends"] += k; tot["n"] += n; tot["final"] += fin; tot["per"] += per / len(rows)
                tot["sent_nonfinal"] += (k == n); tot["sent"] += (k == n and fin)
                if miss:
                    tot["misses"].append((r["id"], [exp[i] for i in miss]))
            res[path] = tot
            print(f"{pathlib.Path(path).stem}: sentences all endings right {tot['sent']}/{len(rows)}; "
                  f"right except a pausal final word {tot['sent_nonfinal']}/{len(rows)}; word endings {tot['ends']}/{tot['n']} "
                  f"(+ final {tot['final']}/{len(rows)}); waṣl joins {tot['joins']}/{tot['nj']}; phoneme error rate {tot['per']:.1%}")
            if not a.json:
                for i, ws in tot["misses"]:
                    print(f"   {i}: {' '.join(ws)}")
        if a.json:
            print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
