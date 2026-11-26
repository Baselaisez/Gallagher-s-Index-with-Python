#!/usr/bin/env python3
"""narration_pack.py — ship a narration pack into a story package (v347). The developer's one step from a teacher's
recording to everyone's reader.

    python3 tools/narration_pack.py qissa-narration-<story>-ch<N>.zip            # validate, transcode, write, mirror
    python3 tools/narration_pack.py PACK.zip --check                              # validate only, write nothing
    python3 tools/narration_pack.py PACK.zip --package-dir DIR --no-mirror        # an explicit package (tests use a temp copy)
    python3 tools/narration_pack.py PACK.zip --no-transcode                       # keep the WAV (large: ≈2.8 MB a minute)

A pack is what the reader's «Narration studio» exports (or tools/narration_generate.py writes): a zip holding
`narration.json` = {package, chapter, audioFile, reader, recorded, sentences: [{id, audio: [startMs, endMs]}]} and the
audio file it names. This tool:
  1. finds the package whose manifest id is `package` (content/samples, content/user-uploads) and its chapter file;
  2. REFUSES a pack whose sentence ids are not exactly the chapter's ids in order, or whose slices are not ordered,
     non-overlapping, inside the audio file, and one per sentence;
  3. transcodes WAV to AAC (.m4a, mono 48 kb/s ≈ 0.36 MB a minute — plays in every browser, iOS and the Android
     WebView) when ffmpeg is on PATH, else keeps the WAV and says so; AAC's encoder delay (~20 ms) is inside the
     250 ms breath the studio leaves between sentences;
  4. writes the content drop CLAUDE.md describes — the file at `audio/ch<N>.<ext>` inside the package, `audioFile`
     on the manifest's chapter entry, and each sentence's `audio: [startMs, endMs]` — touching no other field and
     keeping each JSON file's own indentation (story text is never edited);
  5. mirrors the audio to prototype/narration/<story>/audio/… — where the page resolves a package-relative audioFile
     (Narr347.url) on the hosted copy, and what tools/build_android.py copies into the APK's assets.
Then: python3 tools/validate_content.py <package> && python3 tools/build_prototype.py. No network, no dependency.
"""
import argparse, io, json, pathlib, shutil, subprocess, sys, tempfile, wave, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
COLLECTIONS = [ROOT / "content/samples", ROOT / "content/user-uploads"]


def fail(msg):
    print("REFUSED:", msg)
    sys.exit(2)


def dump_like(raw, data):
    """Serialise `data` with the indentation the file already uses (every content file round-trips one of these)."""
    for ind in (2, 1, None):
        s = json.dumps(json.loads(raw), ensure_ascii=False, indent=ind)
        if s + "\n" == raw:
            return json.dumps(data, ensure_ascii=False, indent=ind) + "\n"
        if s == raw:
            return json.dumps(data, ensure_ascii=False, indent=ind)
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def audio_ms(name, data):
    if name.lower().endswith(".wav"):
        with wave.open(io.BytesIO(data)) as w:
            return w.getnframes() * 1000.0 / w.getframerate()
    if shutil.which("ffprobe"):
        with tempfile.NamedTemporaryFile(suffix=pathlib.Path(name).suffix) as f:
            f.write(data); f.flush()
            out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f.name],
                                 capture_output=True, text=True)
            try:
                return float(out.stdout.strip()) * 1000.0
            except ValueError:
                pass
    return None


def find_package(pid):
    for coll in COLLECTIONS:
        if not coll.is_dir():
            continue
        for d in sorted(coll.iterdir()):
            m = d / "manifest.json"
            if m.is_file() and json.loads(m.read_text(encoding="utf-8")).get("id") == pid:
                return d
    return None


def validate(man, audio_name, audio, chapter):
    ids = [s["id"] for s in chapter["sentences"]]
    got = [s.get("id") for s in man.get("sentences", [])]
    if got != ids:
        extra = [i for i in got if i not in ids][:3]
        missing = [i for i in ids if i not in got][:3]
        fail(f"sentence ids do not match chapter {man.get('chapter')}: not in the chapter {extra}, not in the pack {missing}"
             + ("" if extra or missing else " (same ids, different order)"))
    dur = audio_ms(audio_name, audio) or man.get("durationMs")
    prev = 0
    for s in man["sentences"]:
        a = s.get("audio")
        if not (isinstance(a, list) and len(a) == 2 and all(isinstance(x, (int, float)) for x in a)):
            fail(f"{s['id']}: audio must be [startMs, endMs]")
        if not (a[0] < a[1]):
            fail(f"{s['id']}: start {a[0]} is not before end {a[1]}")
        if a[0] < prev:
            fail(f"{s['id']}: starts at {a[0]} before the previous sentence ends ({prev})")
        if dur is not None and a[1] > dur + 5:
            fail(f"{s['id']}: ends at {a[1]} ms, past the end of the audio ({round(dur)} ms)")
        prev = a[1]
    return dur


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pack")
    ap.add_argument("--package-dir", help="the package to write into (default: found by the pack's id)")
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--no-transcode", action="store_true")
    ap.add_argument("--no-mirror", action="store_true", help="do not copy into prototype/narration/")
    a = ap.parse_args()

    try:
        z = zipfile.ZipFile(a.pack)
        man = json.loads(z.read("narration.json").decode("utf-8"))
        audio = z.read(man["audioFile"])
    except (OSError, KeyError, ValueError, zipfile.BadZipFile) as e:
        fail(f"not a narration pack ({e})")
    for k in ("package", "chapter", "audioFile", "sentences"):
        if k not in man:
            fail(f"narration.json has no {k!r}")
    pkg = pathlib.Path(a.package_dir) if a.package_dir else find_package(man["package"])
    if not pkg or not (pkg / "manifest.json").is_file():
        fail(f"no package with id {man['package']!r}")
    mraw = (pkg / "manifest.json").read_text(encoding="utf-8")
    manifest = json.loads(mraw)
    if manifest.get("id") != man["package"]:
        fail(f"the package's id is {manifest.get('id')!r}, the pack's is {man['package']!r}")
    entry = next((c for c in manifest.get("chapters", []) if c.get("n") == man["chapter"]), None)
    cfile = pkg / "chapters" / f"{man['chapter']}.json"
    if not entry or not cfile.is_file():
        fail(f"{man['package']} has no chapter {man['chapter']}")
    craw = cfile.read_text(encoding="utf-8")
    chapter = json.loads(craw)
    dur = validate(man, man["audioFile"], audio, chapter)
    mins = (dur or 0) / 60000
    print(f"pack ok: {man['package']} chapter {man['chapter']}, {len(man['sentences'])} sentences, "
          f"{round((dur or 0) / 1000, 1)} s, read by {man.get('reader') or '(unnamed)'}, recorded {man.get('recorded', '?')}")
    if a.check:
        return 0

    ext, data = pathlib.Path(man["audioFile"]).suffix.lower(), audio
    if ext == ".wav" and not a.no_transcode:
        if shutil.which("ffmpeg"):
            with tempfile.TemporaryDirectory() as td:
                src, dst = pathlib.Path(td) / "in.wav", pathlib.Path(td) / "out.m4a"
                src.write_bytes(audio)
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-ac", "1", "-c:a", "aac", "-b:a", "48k",
                                "-movflags", "+faststart", str(dst)], check=True)
                data, ext = dst.read_bytes(), ".m4a"
        else:
            print("note: ffmpeg not found — shipping the WAV as it is (≈2.8 MB a minute; transcode before release)")
    rel = f"audio/ch{man['chapter']}{ext}"
    (pkg / "audio").mkdir(exist_ok=True)
    (pkg / rel).write_bytes(data)
    spans = {s["id"]: [int(round(s["audio"][0])), int(round(s["audio"][1]))] for s in man["sentences"]}
    for s in chapter["sentences"]:
        s["audio"] = spans[s["id"]]
    cfile.write_text(dump_like(craw, chapter), encoding="utf-8")
    entry["audioFile"] = rel
    (pkg / "manifest.json").write_text(dump_like(mraw, manifest), encoding="utf-8")
    print(f"wrote {rel} ({len(data) // 1024} KB, {round(len(data) / 1024 / max(mins, 1e-9))} KB a minute), "
          f"audioFile on chapter {man['chapter']}, {len(spans)} sentence slices")
    if not a.no_mirror:
        dest = ROOT / "prototype/narration" / man["package"] / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"mirrored to {dest.relative_to(ROOT)} (the hosted copy and the Android assets serve it from here)")
    print(f"next: python3 tools/validate_content.py {pkg} && python3 tools/build_prototype.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
