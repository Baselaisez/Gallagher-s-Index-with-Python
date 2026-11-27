#!/usr/bin/env python3
"""voice_azure.py — v355: the ADAPTER for a hosted neural voice (Microsoft Azure AI Speech), prepared so that ONE decision —
the owner buys a Speech resource and puts its key in the repository's secrets — makes a natural voice the app's voice.
Nothing here runs by itself: no key is in the repository, and no test makes a network call.

    python3 tools/voice_azure.py --selftest            # no network: SSML well-formed, every phone in Azure's ar phone set,
                                                        #   synthesize() refuses without a key BEFORE opening any connection
    python3 tools/voice_azure.py --dry-run             # no network: billable characters for the test set and the whole shelf
    python3 tools/voice_azure.py --ssml "نَصٌّ"          # print the SSML one sentence would send
    # with a key (the owner's step; build time only):
    AZURE_SPEECH_KEY=… AZURE_SPEECH_REGION=westeurope python3 tools/voice_app.py --engine azure --out DIR
    AZURE_SPEECH_KEY=… python3 tools/narration_generate.py --adapter voice_azure:synthesize --out packs/

What it sends: the app's OWN reading (tools/voice_eval.py — every written vowel and case ending, hamzat al-waṣl elided, the
article assimilated, stress by the classical rule), word by word, as SSML `<phoneme alphabet="ipa" ph="…">word</phoneme>`
in Azure's documented Arabic IPA phone set (learn.microsoft.com, «SSML phonetic alphabets», ar-EG/ar-SA: a aː i iː u uː,
b d g k t dˤ q tˤ ʔ f h ħ s θ z ðˤ ð ɣ x ʃ sˤ j w l m n r ʕ). So the service's own letter-to-sound rules — which may
«correct» a vowel — are not used where the phoneme element is honoured. ج: the documented table is ar-EG's (g); ar-SA's
ج is sent as AZURE_TTS_JIM (default d͡ʒ). If the service rejects a sentence's phonemes (HTTP 400), the sentence is sent
again as its plain vowelled text and counted in FALLBACKS (said at the end of a render) — never silently.

Environment (never in the repository): AZURE_SPEECH_KEY (the Speech resource's key), AZURE_SPEECH_REGION (e.g. westeurope;
the host is <region>.tts.speech.microsoft.com), AZURE_TTS_VOICE (default ar-SA-HamedNeural; ar-SA-ZariyahNeural is the
female voice), AZURE_TTS_JIM (default d͡ʒ).
Terms (quoted in research/voice-options-2026-11-27.md, part 2): Microsoft «requires its customers to disclose the synthetic
nature of text to speech voices to its users» — the app labels the voice «otomatik / automatic» everywhere it plays.
"""
import argparse, html, io, json, os, pathlib, sys, time, wave

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import voice_eval as ve                  # noqa: E402  (the reading)

PHONES = set("a aː i iː u uː b d g k t dˤ q tˤ ʔ f h ħ s θ z ðˤ ð ɣ x ʃ sˤ j w l m n r ʕ".split())
VOICE_ID = "azure355"
FALLBACKS = []                            # sentences sent as plain text because the service refused their phonemes


def voice_name():
    return os.environ.get("AZURE_TTS_VOICE", "ar-SA-HamedNeural")


def ipa_word(w):
    """one word of the reading → Azure IPA: syllables split by '.', the stressed one marked ˈ (Azure: mark every syllable)."""
    jim = os.environ.get("AZURE_TTS_JIM", "d͡ʒ")
    syl, st = ve.syllables(w), ve.stress(w)
    out = []
    for j, sy in enumerate(syl):
        s = "".join(jim if p == "dʒ" else p for p in sy)
        out.append(("ˈ" if j == st and len(syl) > 1 else "") + s)
    return ".".join(out)


def pieces(text):
    """(written word or punctuation, IPA or None) in order — the written words as SENT, beside the reading's words."""
    marks = []
    words = ve.g2p(text, marks)
    import re
    toks = re.findall(r"[^\s،؛؟!.:,]+|[،؛؟!.:,]", text)
    out, k = [], 0
    for t in toks:
        if re.fullmatch(r"[،؛؟!.:,]", t):
            out.append((t, None))
        else:
            out.append((t, ipa_word(words[k]))); k += 1
    return out


def ssml(text, phonemes=True):
    body = []
    for t, ph in pieces(text):
        if ph is None:
            body.append(html.escape(t))
        elif phonemes:
            body.append(f' <phoneme alphabet="ipa" ph="{html.escape(ph)}">{html.escape(t)}</phoneme>')
        else:
            body.append(" " + html.escape(t))
    lang = voice_name()[:5]
    return (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{lang}">'
            f'<voice name="{voice_name()}">{"".join(body).strip()}</voice></speak>')


def billable(s):
    """Azure bills every character of the SSML body except the <speak> and <voice> tags (learn.microsoft.com, «Billable characters»)."""
    import re
    return len(re.sub(r"</?speak[^>]*>|</?voice[^>]*>", "", s))


def _post(body):
    import urllib.request, urllib.error
    key, region = os.environ.get("AZURE_SPEECH_KEY"), os.environ.get("AZURE_SPEECH_REGION")
    if not key or not region:
        raise RuntimeError("AZURE_SPEECH_KEY and AZURE_SPEECH_REGION must be set (the owner's Speech resource) — nothing was sent")
    req = urllib.request.Request(f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1", data=body.encode("utf-8"),
                                 method="POST", headers={"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/ssml+xml",
                                                         "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm", "User-Agent": "qissa-voice"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 400:
                raise ValueError("HTTP 400")
            if e.code in (429, 500, 502, 503, 504) and attempt < 5:
                time.sleep(2 ** attempt); continue
            raise


def synthesize(text):
    """narration_generate's adapter contract: text → (WAV bytes, duration ms). The app's reading as phonemes; on a 400 the
    plain vowelled text (recorded in FALLBACKS)."""
    try:
        data = _post(ssml(text, True))
    except ValueError:
        FALLBACKS.append(text)
        print(f"voice_azure: phonemes refused, sent as text: {text[:60]}", file=sys.stderr)
        data = _post(ssml(text, False))
    with wave.open(io.BytesIO(data)) as w:
        ms = round(w.getnframes() * 1000 / w.getframerate())
    return data, ms


def selftest():
    import xml.dom.minidom
    rows, bad = ve.load_set(), set()
    for r in rows:
        s = ssml(r["text"])
        xml.dom.minidom.parseString(s)                                  # well-formed
        for t, ph in pieces(r["text"]):
            if ph:
                for p in ve.tokenize_ipa(ph.replace(".", "").replace("ˈ", "").replace("d͡ʒ", "dʒ"))[0]:
                    if p not in PHONES and p != "dʒ":
                        bad.add(p)
    saved = {k: os.environ.pop(k, None) for k in ("AZURE_SPEECH_KEY", "AZURE_SPEECH_REGION")}
    try:
        synthesize("نَصٌّ."); refused = False
    except RuntimeError:
        refused = True
    finally:
        for k, v in saved.items():
            if v is not None:
                os.environ[k] = v
    sample = ssml(rows[0]["text"])
    print(json.dumps({"sentences": len(rows), "phones_outside_azure_ar_set": sorted(bad), "refuses_without_key": refused,
                      "testset_billable_chars": sum(billable(ssml(r["text"])) for r in rows), "sample": sample}, ensure_ascii=False))
    return 0 if not bad and refused else 1


def dry_run():
    import narration_generate as ng
    plain = ph = n = 0
    for pkg in ng.packages():
        for m, ch, sid, text in ng.walk(pkg):
            plain += billable(ssml(text, False)); ph += billable(ssml(text, True)); n += 1
    print(json.dumps({"sentences": n, "billable_chars_with_phonemes": ph, "billable_chars_plain_text": plain}))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true"); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--ssml")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.dry_run:
        return dry_run()
    if a.ssml:
        print(ssml(a.ssml)); return 0
    ap.print_help(); return 0


if __name__ == "__main__":
    sys.exit(main())
