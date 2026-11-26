#!/usr/bin/env python3
"""narration_generate.py — the seam for GENERATED narration (v347). A provider-agnostic SKELETON: it calls no service,
needs no key and no dependency. Choosing a neural text-to-speech provider (and paying for it) is the owner's decision.

    python3 tools/narration_generate.py                      # no adapter: what it WOULD send — characters per story and shelf
    python3 tools/narration_generate.py --package DIR        # one package
    python3 tools/narration_generate.py --adapter mymod:synthesize --out packs/   # with an adapter: write narration packs

What it does:
- walks each package's chapters and yields every sentence's SENDABLE text — the stored, fully vowelled text with exactly
  the substitutions of the reader's SEND347 table (prototype/reader.html, Voice347.clean): the verse mark and dashes
  become a pause, tatweel / brackets / the editorial asterisk / Quranic pause marks / the end-of-āya mark and its number
  are dropped, ﷺ and the small honorific signs are spelt out, Western digits become Arabic-Indic. The displayed text is
  never altered. (The smoke suite holds the page's table and this one to the same sample.)
- with an adapter `synthesize(text) -> (audio_bytes, duration_ms)` returning ONE format for every call (WAV is easiest:
  the tool then joins sentences itself; any other format must be joined by the adapter's own means), it writes one
  narration pack per chapter in the studio's format — {package, chapter, audioFile, reader, recorded, sentences:
  [{id, audio: [startMs, endMs]}]} — which tools/narration_pack.py validates and ships like a teacher's recording.
- with NO adapter it prints the character counts (what providers bill by), per story and for the whole shelf.
"""
import argparse, importlib, io, json, pathlib, re, sys, wave, zipfile
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
COLLECTIONS = [ROOT / "content/samples", ROOT / "content/user-uploads"]
SALLA = "صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ"
# the reader's SEND347, row for row (keep the two in step; the smoke check «v347 — what is sent» compares them)
SEND = [
    ("ayah", r"\s*۝\s*[٠-٩0-9]*\s*", "، "),
    ("pause", r"[ۖ-ۜ۞۟-ۤۧۨ۩۪-ۭ]", ""),
    ("salla", r"[ﷺؐ]", " " + SALLA + " "),
    ("jalla", r"ﷻ", " جَلَّ جَلَالُهُ "),
    ("allah", r"ﷲ", "اللَّه"),
    ("alayhi", r"ؑ", " عَلَيْهِ السَّلَامُ "),
    ("rahma", r"ؒ", " رَحْمَةُ اللَّهِ عَلَيْهِ "),
    ("radiya", r"ؓ", " رَضِيَ اللَّهُ عَنْهُ "),
    ("verse", r"\s*•\s*", "، "),
    ("tatweel", r"ـ", ""),
    ("brackets", r"[﴾﴿()\[\]{}⟨⟩«»\"“”*]", ""),
    ("dash", r"\s*[—–…]\s*", "، "),
    ("colon", r"：", ":"),
    ("digits", r"[0-9]", lambda m: "٠١٢٣٤٥٦٧٨٩"[int(m.group(0))]),
    ("controls", r"[​-‏؜‪-‮⁦-⁩]", ""),
]
SEND_RE = [(k, re.compile(p), r) for k, p, r in SEND]


def clean(s):
    for _, rx, to in SEND_RE:
        s = rx.sub(to, s)
    return re.sub(r"\s{2,}", " ", s)


def sendable(sen):
    """The reader's Voice347.sentence(): tokens joined, punctuation attached, the table applied per piece."""
    text, toks = "", sen["tokens"]
    for i, t in enumerate(toks):
        surf = t["surface"]["full"] if isinstance(t["surface"], dict) else t["surface"]
        text += clean(surf).strip()
        p = clean(t.get("punctAfter") or "").strip()
        if p:
            text += ("" if p == "،" or re.fullmatch(r"[.:؛؟!]", p) else " ") + p
        if i < len(toks) - 1:
            text += " "
    return re.sub(r"\s{2,}", " ", text)


def packages(only=None):
    if only:
        yield pathlib.Path(only)
        return
    for coll in COLLECTIONS:
        if coll.is_dir():
            yield from sorted(d for d in coll.iterdir() if (d / "manifest.json").is_file())


def walk(pkg):
    """Yield (manifest, chapter_n, sentence_id, sendable_text) for every sentence of a package, in reading order."""
    m = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
    for ch in m.get("chapters", []):
        d = json.loads((pkg / "chapters" / f"{ch['n']}.json").read_text(encoding="utf-8"))
        for sen in d["sentences"]:
            yield m, ch["n"], sen["id"], sendable(sen)


def wav_join(clips, gap_ms=250):
    """Join WAV clips (one shared format) with a breath of silence; return (wav bytes, [[start, end] ms], total ms)."""
    frames, spans, params, at = [], [], None, 0
    for data in clips:
        with wave.open(io.BytesIO(data)) as w:
            p = (w.getnchannels(), w.getsampwidth(), w.getframerate())
            if params and p != params:
                sys.exit("the adapter returned WAV clips in different formats")
            params, raw = p, w.readframes(w.getnframes())
        rate, width = params[2], params[0] * params[1]
        gap = b"\x00" * (int(rate * gap_ms / 1000) * width)
        frames.append(gap)
        at += gap_ms
        ms = len(raw) / width / rate * 1000
        spans.append([round(at), round(at + ms)])
        frames.append(raw)
        at += ms
    out = io.BytesIO()
    with wave.open(out, "wb") as w:
        w.setnchannels(params[0]); w.setsampwidth(params[1]); w.setframerate(params[2])
        w.writeframes(b"".join(frames) + b"\x00" * (int(params[2] * gap_ms / 1000) * params[0] * params[1]))
    return out.getvalue(), spans, round(at + gap_ms)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--package", help="one package directory (default: the whole shelf)")
    ap.add_argument("--adapter", help="module:function implementing synthesize(text) -> (audio_bytes, duration_ms)")
    ap.add_argument("--out", default="narration-packs", help="where packs are written (with an adapter)")
    ap.add_argument("--voice-name", default="generated", help="the pack's `reader` field (name the provider and voice)")
    ap.add_argument("--json", action="store_true", help="print the counts as JSON")
    a = ap.parse_args()

    synth = None
    if a.adapter:
        mod, _, fn = a.adapter.partition(":")
        synth = getattr(importlib.import_module(mod), fn or "synthesize")

    shelf, rows = {"stories": 0, "sentences": 0, "chars": 0, "letters": 0}, []
    for pkg in packages(a.package):
        per = {}
        for m, n, sid, text in walk(pkg):
            r = per.setdefault(m["id"], {"id": m["id"], "level": m.get("level"), "chapters": set(), "sentences": 0, "chars": 0, "letters": 0})
            r["chapters"].add(n); r["sentences"] += 1; r["chars"] += len(text)
            r["letters"] += len(re.sub(r"[^ء-ي]", "", text))   # letters without the vowel marks: a speech-time proxy
        for r in per.values():
            r["chapters"] = len(r["chapters"]); rows.append(r)
            shelf["stories"] += 1
            for k in ("sentences", "chars", "letters"):
                shelf[k] += r[k]
        if synth:
            by_ch = {}
            for m, n, sid, text in walk(pkg):
                by_ch.setdefault((m["id"], n), []).append((sid, text))
            outdir = pathlib.Path(a.out); outdir.mkdir(parents=True, exist_ok=True)
            for (pid, n), sens in by_ch.items():
                clips = [synth(text)[0] for _, text in sens]
                audio, spans, total = wav_join(clips)
                man = {"package": pid, "chapter": n, "audioFile": f"ch{n}.wav", "reader": a.voice_name,
                       "recorded": date.today().isoformat(), "format": "wav", "durationMs": total,
                       "sentences": [{"id": sid, "audio": sp} for (sid, _), sp in zip(sens, spans)]}
                path = outdir / f"qissa-narration-{pid}-ch{n}.zip"
                with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as z:
                    z.writestr("narration.json", json.dumps(man, ensure_ascii=False, indent=1))
                    z.writestr(man["audioFile"], audio)
                print("wrote", path)

    if a.json:
        print(json.dumps({"shelf": shelf, "stories": rows}, ensure_ascii=False, indent=1))
        return 0
    if not synth:
        print("No adapter configured — nothing is sent anywhere. What WOULD be sent (the sendable text, SEND347):\n")
    print(f"{'story':44} {'lvl':>3} {'ch':>3} {'sent':>5} {'chars':>8} {'letters':>8}")
    for r in sorted(rows, key=lambda r: (r["level"] or 0, r["id"])):
        print(f"{r['id'][:44]:44} {r['level'] or '':>3} {r['chapters']:>3} {r['sentences']:>5} {r['chars']:>8} {r['letters']:>8}")
    print(f"\nshelf: {shelf['stories']} stories, {shelf['sentences']} sentences, {shelf['chars']:,} characters sent "
          f"({shelf['letters']:,} letters without vowel marks).")
    print("Providers bill by characters sent (some count the vowel marks, some do not — ask). "
          "At a careful learner's pace of ~10 letters a second the shelf is roughly "
          f"{round(shelf['letters'] / 10 / 3600, 1)} hours of audio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
