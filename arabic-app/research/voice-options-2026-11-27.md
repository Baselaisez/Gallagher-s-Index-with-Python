# A voice inside the app — the options, on evidence (v349, 2026-11-27)

The owner: «We have to put a voice within the app — not that consumers have to have it. Optimisation is still one of the
most crucial.» Nobody here can listen, so every claim below rests on something checkable: the PHONEMES an engine says for
a 30-sentence vowelled test set (`tools/voice_testset.txt`, scored by `tools/voice_eval.py`), a speech recogniser hearing
the audio back (Whisper-small, letter error rate), measured bytes and speeds, and the licence text quoted verbatim.

**The app's reading** (the test set's expected column, written by rule from the vowels and checked by hand) is a learner's
reading «وَصْلًا»: every case ending and tanwīn is pronounced — before a comma and at the end of a sentence too — and
hamzat al-waṣl is elided in connected speech (فِي الشَّجَرَةِ → fi ššajarati). A pause (waqf) would drop the ending; the
test set records what it would drop, and an engine that pauses at the end is counted apart ("pausal"), not as a misreading.

## The table

| Candidate | Works here? | Endings right (sentences of 30) | Waṣl joins (of 30) | Heard back (Whisper letter error) | Speed | Bytes | Licence (engine / voice) | Verdict |
|---|---|---|---|---|---|---|---|---|
| eSpeak NG in the page (npm `espeak-ng` 1.0.2, WASM), reading the TEXT | yes (npm) | **17** (182 word endings: 167) | 0 | 64.7 % | RTF ≈ 0.03 (node, 1 thread; ×4 CPU ≈ 0.13) | 18.5 MB wasm (9.2 MB gz), every language embedded | GPL-3.0-or-later (engine and its Arabic rules) | **no** — misreads shadda (بَقِيَ → baqiːa, النَّبِيُّ → nnnbiːuː), never elides the waṣl, robotic; shipping it in a paid app is copyleft |
| Piper `ar_JO-kareem` (medium / low) through Piper's own eSpeak phonemiser (piper-tts 1.8, the voice's training pipeline) | voice: yes, from GitHub release assets (sherpa-onnx `tts-models`); not from huggingface.co (blocked) | **25** (176/182) | 0 | 3.4 % | — | 63 MB onnx (58 MB gz) | engine GPL-3.0 (piper1-gpl); voice: see below | **no** (licence) |
| Piper `ar_JO-kareem` in the page through **sherpa-onnx 2.0.3 WASM** fed the APP'S reading as phonemes | yes (npm + GitHub release) | **30** by construction | 30 | 4.8 % | RTF 0.22 (low) / 0.35 (medium), node 1 thread; ×4 CPU ≈ 0.9 / 1.4 — medium cannot keep up on a slow phone | 15.7 MB wasm (4.4 MB gz) + 63 MB voice (58 MB gz) ≈ 63 MB to download before the first word | engine Apache-2.0 (sherpa-onnx ≥ 2.0 no longer contains eSpeak); voice: lessac chain, not for commercial use | **no** (licence of the voice; and 63 MB) — the engine path is clean and ready if a licensable Arabic voice appears |
| MMS-TTS `ara` (Meta) | no — huggingface.co and dl.fbaipublicfiles.com blocked | — | — | — | — | ~ 145 MB | CC-BY-NC-4.0 (as published by Meta; not re-read here: host blocked) | **no** (non-commercial) |
| piper-plus, kokoro-js, @diffusionstudio/vits-web, piper-tts-web | install (npm) | — | — | — | — | — | MIT / Apache wrappers | no Arabic voice (piper-plus: 8 languages, none Arabic; the Piper wrappers fetch voices from huggingface.co at run time) |
| **eSpeak NG at BUILD time, fed the APP'S reading as phonemes → pre-rendered packs** (`tools/voice_app.py`) | **yes** | **30** (182/182, final 30/30) | **30** | 69.7 % | build: RTF 0.033 (this container, one process); phone: none — it plays a file | no engine; audio AAC 24 kb/s ≈ 0.18 MB a minute: median story 0.61 MB, the shelf 210 MB (16.3 h of audio, 83 stories; largest 27.7 MB) on the server, fetched per chapter | the tool is GPL-3.0-or-later; its OUTPUT is not a covered work (GPLv3 §2, quoted below); no engine ships | **shipped, behind a deploy switch** — correct and licence-clean, but robotic and hard to follow (Whisper hears 70 % of its letters wrong); the owner listens and decides |

(Phoneme error rate against the reference: eSpeak text 8.6 %, Piper's eSpeak 7.4 %, eSpeak fed the app's reading 0.1 % — the
remainder is ظ, which eSpeak's Arabic phoneme set says as ذ.)

## The reasoning

**What the phonemes show.** eSpeak NG's Arabic letter-to-sound rules — and every Piper Arabic voice inherits them, because
Piper's voices are trained on eSpeak's phonemes — fail exactly where a madrasa reader is graded: a vowel after a shadda is
lost in the older build (مُحَمَّدٌ → muħammdun, الثَّعْلَبُ → ʔaθθθʕlabu), yāʾ with its own vowel after a kasra is read as a
long ī (بَقِيَ → baqiːa, النَّبِيُّ → nabiːu), and hamzat al-waṣl is NEVER elided (فِي الشَّجَرَةِ → fiː ʔaʃʃadʒarati,
عَلَيْهَا الْمَاءُ → ʕalajhaː almaːʔu): 0 of 30 joins right in either build. Piper's newer eSpeak fixes the shadda bug
(25/30 sentences with every ending right) but not the waṣl. The cure is not to let the engine read the letters at all:
the app now owns its reading (`tools/voice_eval.py`: the written vowels, the article, the waṣl, tāʾ marbūṭa, madd, stress
by the classical rule) and hands the engine PHONEMES. eSpeak then says 30/30, joins 30/30 (its own `--ipa` report of what
it will say, scored by the same tool). sherpa-onnx 2.0 takes phonemes the same way (`phonemeCodepoints`), so the same
reading would drive a neural voice the day one can be licensed.

**What the licences allow.** The app has a paid tier.
- eSpeak NG (npm `espeak-ng`, LICENSE = GNU GPL v3): «You may convey a covered work in object code form under the terms of
  sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this
  License» — shipping the engine inside the app makes the app's distribution subject to the GPL (a lawyer's question for
  a paid app; not taken). Run as a build tool it is harmless: «The output from running a covered work is covered by this
  License only if the output, given its content, constitutes a covered work.» (GPLv3 §2). The audio is that output.
- sherpa-onnx (Apache License 2.0): «each Contributor hereby grants to You a perpetual, worldwide, non-exclusive,
  no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, …» — fine for a paid
  app; and since 2.0.0 it states «espeak-ng is no longer used by sherpa-onnx».
- Piper `ar_JO-kareem` MODEL_CARD: «Dataset · URL: https://github.com/AliMokhammad/arabicttstrain/ · License: See URL»
  (that repository answers 404 today) and «Training · Finetuned from U.S English lessac voice». Piper's own LICENSING.md:
  «`en_US-lessac-medium` was trained on the Lessac Blizzard 2013 corpus, whose license limits use to "research and
  exploration of speech technologies" and excludes commercial use of the resulting synthesis.» and COMMERCIAL_USE.md lists
  under «Not on this list»: «Everything fine-tuned from lessac or ryan.» and «Voices whose card only says "See URL".» —
  kareem is both. No Arabic voice is on Piper's commercial list.
- Piper engine (piper1-gpl): «The Piper engine is GPL-3.0-or-later.» — not needed: sherpa-onnx runs Piper voices.

**What it costs the phone.** An in-page neural voice is ~63 MB before the first word and runs at 0.9–1.4× real time on a
4×-slowed CPU — on a slow phone the medium voice cannot keep up with itself. eSpeak in the page is 18.5 MB (all
languages embedded; an Arabic-only build needs an Emscripten toolchain this container does not have). Pre-rendered audio
costs the phone nothing until a story is played, then ~0.18 MB a minute of that story, once, offline thereafter — and
no CPU at all. It covers only stored text (a sentence typed in a lab still needs the device voice), which is the trade
the owner's «optimisation is still one of the most crucial» asks for.

**Heard back — the warning.** The phonemes are right, but the SOUND is the weak point: Whisper-small gets 3–5 % of the
letters wrong from the neural kareem voice and 65–70 % wrong from eSpeak, whether eSpeak reads the text or the app's
reading. Whisper is known to do badly on formant synthesis, so this overstates how hard a person finds it — but it is the
one measurement of intelligibility we have, and it says the shipped voice is robotic and hard to follow. The same
phonemes through kareem (4.8 %) show the app's reading itself is sound: a licensable neural voice would fix the sound
without touching anything else. Listen: `sample-app-voice.m4a` / `sample-neural-kareem.m4a` (the session's scratch folder).

**Heard back — method.** Whisper-small (sherpa-onnx, int8, GitHub release asset) transcribed each rendering; the letter error rate
against the sentence's bare letters is in the table. It is a proxy for intelligibility, not for correctness (Whisper
writes no vowels, and it knows Modern Standard Arabic, not a learner's waṣl reading); it is here to show the generated
audio is speech a listener can follow, not noise.

## What the owner can decide

1. **Keep or switch off the shipped voice** (eSpeak, the app's reading): correct by the test set, licence-clean, robotic and
   hard to follow. The Pages workflow renders it at deploy time unless its `app_voice` input is `false`; with it off the
   app behaves as before v349 (device voice, else the silent walk) and says the app's voice is unavailable.
2. **A better-sounding voice**, by one of: (a) a commercially licensed Arabic VITS/Piper voice (none exists in Piper's
   commercial list today; a voice trained on licensed recordings of a hoca reading the shelf would be ideal — the studio
   collects exactly that) — drop it into `voice_app.py` through sherpa-onnx with the app's phonemes, re-render; (b) a paid
   neural TTS provider at build time (778,063 characters sent for the shelf, v347) — needs a key and a host allowed; (c)
   a teacher's recordings (v347's studio), which always play before the app's voice.
3. **Hosts** this container could not reach (for the record): huggingface.co (Piper voices, MMS, Whisper), dl.fbaipublicfiles.com (MMS),
   www.cstr.ed.ac.uk (the lessac licence page), api.github.com, cdn.jsdelivr.net, unpkg.com. GitHub release assets were reachable.
