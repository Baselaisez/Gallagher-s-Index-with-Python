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

---

# Part 2 (v355-V, 2026-11-27): a voice the app can SHIP — natural, commercially usable, reading every vowel

The owner, after hearing v349's two samples: «you find a voice package». The bar for a voice to be made the app's voice:
(1) **commercially clean** by a licence quoted from its source (the app has a paid tier: the generated AUDIO must be usable
commercially, and the model too if the model ships), (2) **obtainable here**, (3) **every written vowel and ending read**, the
emphatics ص ض ط ظ and ق ع ح kept apart, (4) **clearly more natural than eSpeak**. Nobody here can listen: every claim rests on
the instruments of part 1 (the 30-sentence test set, Whisper-small hearing the audio back) and the licence text.

**Where things could be read from.** This container's proxy refused huggingface.co, en.arabicspeechcorpus.com,
catalog.elra.info, ota.bodleian.ox.ac.uk, islrn.org, drive.google.com, openslr.org, zenodo.org, kaggle.com, docs.cloud.google.com,
azure.microsoft.com, aws.amazon.com, elevenlabs.io, openai.com, wikipedia.org, arxiv.org, supertonic3.github.io, k2-fsa.github.io.
It reached raw.githubusercontent.com, github.com pages (fetch tool), GitHub release assets, PyPI, npm, cloud.google.com and
Microsoft Learn. Where a primary page sat on a refused host, the quote below says where it came from instead (a copy, a search
engine's excerpt) — such a quote is evidence, not proof.

## The table

Test-set numbers: Whisper-small int8 (sherpa-onnx, GitHub release asset) letter error rate on the bare letters (CER); the
emphatics/pharyngeals row counts how often each reference letter came back as itself; «vowel overrides seen» counts words where
the recogniser wrote a long-vowel letter (ا و ي) the text does not have — a short vowel said long — calibrated on kareem fed
the app's reading (vowels right by construction), where the same count is the recogniser's own noise (2). RTF: sherpa-onnx
2.0.3 Python, 2 threads, this 4-core container under the other agents' load.

| Candidate | Licence chain (quoted below) | Obtainable here | Test set | Verdict |
|---|---|---|---|---|
| **Supertonic 3** (Supertone; sherpa-onnx `sherpa-onnx-supertonic-3-tts-int8-2026-05-11`, 129 MB, 31 languages incl. ar) | code MIT; model **OpenRAIL-M** (commercial use allowed under use restrictions; Attachment A (e): disclose machine generation) — copy of the LICENSE read from a GitHub release mirror; the primary (huggingface.co) refused | **yes** (GitHub release) | reads TEXT only (no phoneme input; its indexer does carry the harakat U+064B–0652): CER **7.9 %**, emphatics 89/89 heard; **vowel overrides seen 8** (فَرَجَعَ→فراجع, وَقَفَ→وقاف, غَضَبًا→غاضبا, سَمِعَ→سميع, فَرِحَ→فارح, يَتَصَرَّمِ→يتصرام, الدُّنْيَا→الدونيه, وَلِقَوْلِهِ→والقوله); three sentences garbled in the transcript (3, 10, 19); endings and tanwīn audibly read in many (الأسدي, البئري, جوابنا, يومنا); RTF 0.34; 44.1 kHz | **no** — most natural by the recogniser, licence workable, but it overrides written vowels and cannot be given the app's reading |
| **Nabra-82M** (oddadmix; Kokoro/StyleTTS2 fine-tune; sherpa-onnx `nabra-82m-arabic-int8`, 83 MB) | model card «Released under Apache-2.0» (search excerpt; huggingface.co refused); training data not named in what could be read | **yes** (GitHub release) | fed the app's reading as phonemes: CER **13.7 %**; its token set (Kokoro's vocab) has **no ˤ and no ̪**, so ص=س, ض=د, ط=ت, ظ=ذ reach the model as the SAME input (ض heard 1/3, ط→ت, س heard as ص); sherpa 2.0's text front end cannot phonemize Arabic (no eSpeak); RTF 0.60 | **no** — the emphatics cannot be kept apart, by construction |
| Piper `ar_JO-SA_dii-high`, `ar_JO-SA_miro-high`, `ar_JO-SA_miro_V2-high` (OpenVoiceOS phoonnx, in sherpa's list) | README: «This model is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)» · «❌ Commercial use is not allowed at this time»; trained on synthetic datasets (TigreGotico/tts-train-synthetic-*) | yes (GitHub release) | not tested (licence) | **no** (non-commercial) |
| Piper `ar_JO-kareem` low/medium | part 1: lessac-derived, «See URL» | yes | calibration only: fed the app's reading CER 5.1 %, overrides 2 (noise), RTF 0.06 | **no** (non-commercial) |
| `tts_arabic` (nipponjo; FastPitch / MixerTTS ONNX) | code MIT; NOTICE.md: «these mixed-training multi-speaker releases are provided for noncommercial use only unless separate permissions covering the XTTS-derived training material and intended use have been obtained» — three of its four voices are XTTS-v2 output (Coqui Public Model License, non-commercial); the phonetiser «retains its CC BY-NC 4.0 license» | package from GitHub; ONNX weights from huggingface.co (refused) | — | **no** (non-commercial) |
| `tts-arabic-pytorch` single-speaker ASC weights (Tacotron2 / FastPitch + HiFi-GAN trained on the Arabic Speech Corpus only) | the repository has **no LICENSE file** (raw LICENSE / LICENSE.md / COPYING: 404) — no grant at all; weights on drive.google.com | no (drive.google.com refused) | — | **no** (no licence) |
| Arabic Speech Corpus (Nawar Halabi, 1,813 utterances, one male MSA speaker) | **conflicting**: tts_arabic's NOTICE: «Arabic Speech Corpus by Nawar Halabi, licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)»; the corpus site / Oxford Text Archive say CC BY 4.0 and the ISLRN record / Wikipedia say CC BY-NC-SA 4.0, with «MicroLinkPC own an exclusive license to commercialise the corpus»; ELRA offers it «under a Creative Commons Attribution License or under ELRA VAR agreement for commercial use» (all four by search excerpt — every host refused) | hosts refused | — | **unsettled** — written confirmation (or the ELRA commercial licence) needed before any model trained on it is shipped |
| **ArTST TTS / `MBZUAI/speecht5_tts_clartts_ar`** (SpeechT5 fine-tuned on **ClArTTS**, classical Arabic, LibriVox audio) | model card tag MIT and ClArTTS card cc-by-4.0 (search excerpts; huggingface.co refused); the ArTST GitHub repository has no LICENSE file; the paper says «released for research use» | **no** — huggingface.co refused | — | **the best-looking open chain, untested**: ClArTTS is fully vowelled classical Arabic read from public-domain LibriVox recordings; needs huggingface.co allowed + torch/transformers to test |
| Chatterbox Multilingual (Resemble AI, 23 languages incl. Arabic) | Resemble: «Chatterbox V3 is released under the MIT license. Use it in commercial products, modify it, and redistribute it without restriction.» (search excerpt) | **no** — weights only on huggingface.co (`ResembleAI/chatterbox`: `t3_mtl23ls_v2.safetensors`, `s3gen.pt`, `ve.pt`, `grapheme_mtl_merged_expanded_v1.json`, `conds.pt`, `Cangjie5_TC.json`, from the PyPI `chatterbox-tts` 0.1.7 source) | — | untested; an autoregressive 0.5 B model on CPU would not render 16 h of shelf inside a 6-hour Pages job; reads text (whether it honours harakat is unknown) |
| MMS-TTS `ara`, Coqui XTTS-v2 | MMS: CC-BY-NC-4.0 (part 1); XTTS-v2: Coqui Public Model License — non-commercial, «expressly excludes training other models for commercial use» (as tts_arabic's NOTICE summarises it) | — | — | **no** (non-commercial) |
| eSpeak NG + the app's reading (v349, shipped OFF) | GPL tool, output free (part 1) | yes | 30/30, joins 30/30, CER 64.7–69.7 % | correct, robotic, ظ as ذ |

**Hosted services** (build time only; nothing was called — no account was opened, no key exists here). The shelf as sent,
re-counted with `tools/narration_generate.py` today: **102 stories, 7,320 sentences, 798,200 characters (380,589 letters)**.
With the app's reading as SSML phonemes (`tools/voice_azure.py --dry-run`): **5,303,567 billable characters** (Azure bills the
markup inside the voice element).

| Service | Arabic voices | Vowelled input / phonemes | Price for the shelf | Commercial use of the audio |
|---|---|---|---|---|
| **Microsoft Azure AI Speech** | ar-SA Hamed / Zariyah neural (+ 14 other ar locales) | Microsoft Learn, «SSML phonetic alphabets», **ar-EG/ar-SA IPA set**: a aː i iː u uː b d g k t dˤ q tˤ ʔ f h ħ s θ z ðˤ ð ɣ x ʃ sˤ j w l m n r ʕ — the app's reading fits it phone for phone (ج: ar-EG's table gives g; sent as d͡ʒ, configurable); «the service counts optional elements that you use to adjust how the text is converted to speech, like phonemes and pitch, as billable characters» | free tier «0.5 million characters free per month» (search excerpt of the pricing page; the page itself refused, rates not readable here); 5.3 M characters with phonemes, 0.8 M as plain text — at the commonly published neural rate (USD 15 per million, **unverified here**) ≈ USD 80 / ≈ USD 12, once; re-renders only changed chapters | Microsoft Learn (Transparency note): «Microsoft requires its customers to disclose the synthetic nature of text to speech voices to its users.»; appropriate uses include «Accredited educational institutions or educational media» and «audio books» |
| Google Cloud TTS | ar-XA (Standard, WaveNet, Chirp 3 HD) | Chirp 3 HD «now supports speech synthesis using SSML input. Supported SSML tags are: <phoneme>, …» (release note, search excerpt); an Arabic IPA table was not found | cloud.google.com/text-to-speech/pricing (read): Chirp 3 HD «0 to 1 million characters» free, then «US$30 per 1 million characters»; Neural2 1 M free then US$16; WaveNet 4 M free then US$4; Standard 4 M free then US$4; «All Speech Synthesis Markup Language (SSML) tags (except the <mark> tag) are also included in the character count» → the plain shelf (0.8 M) fits one month's Chirp 3 HD free tier | Service Terms (read): only «use … Generated Output to develop a similar or competing product» and model-training uses are barred — nothing against audio in a paid app |
| Amazon Polly | Zeina (standard MSA), Hala / Zayd (neural, Gulf; Hala also MSA with `arb`) | phoneme support for Arabic not established | neural USD 16 or 19.20 per million (two versions of the pricing page in search); 1 M free a month for 12 months | not read (aws.amazon.com refused) |
| ElevenLabs | multilingual models incl. Arabic | whether harakat are honoured: not documented in what was found | per plan (refused) | help centre (search excerpt): «All paid plans include a commercial license, provided you're not using Beta Services»; free-plan output «cannot be used commercially» |
| OpenAI | tts-1, tts-1-hd, gpt-4o-mini-tts (multilingual) | no SSML, no phonemes | tts-1 USD 15 / tts-1-hd USD 30 per million characters; gpt-4o-mini-tts USD 0.60 per million text tokens + USD 12 per million audio tokens (model pages, search excerpts) | not read (openai.com refused) |

**A voice of the owner's own.** (a) **The teacher's studio (v347, exists, free)**: a hoca reads a chapter a few minutes at a time;
his recording always plays first. It is the only voice that reads by the books by definition, and the recordings are his to
license. (b) Azure **professional voice** (Limited Access): «Contributing at least 300 lines for a proof-of-concept voice model
and about 2,000 lines to produce a new voice model for production use»; «it usually takes 20 to 40 compute hours to train a
single-style voice … billed with a cap of 96 compute hours», plus hosting billed per hour while the endpoint is up. (c) Train an
open VITS / Piper voice on the hoca's own studio recordings: (an estimate, not measured here) one to two hours of clean, consented speech (the studio's format
already pairs every sentence with its text) and about a GPU-day of fine-tuning; licence clean because the recordings are the owner's; the result drops into
`voice_app.py` through sherpa-onnx with the same phonemes. The cheapest honest route is (a), then (c) from the same recordings.

## The reasoning

**Why nothing passes today.** The two voices that could be obtained and licensed fail the madrasa bar in opposite ways.
Supertonic 3 is the most natural thing measured (7.9 % letter error against eSpeak's 65–70 %, every emphatic heard), and its
OpenRAIL-M allows commercial use (Attachment A (e) asks that machine-generated content be disclosed — the app already says
«otomatik»). But it reads the LETTERS, and it lengthens short vowels the text writes short (فَرَجَعَ said with a long ā, as a
recogniser hears it), with no way to hand it the app's reading. Nabra takes phonemes, so every ending would be right by
construction — but its symbol set cannot express ˤ: ص ض ط ظ reach it as س د ت ذ. Neither may be made the voice of an app that
teaches reading by the vowels. (Supertonic's 30-second sample of the same Level-1 story is left beside eSpeak's for the owner's
ear — as a measure of what "natural" sounds like, not as a candidate.)

**The decisions, ranked** (each makes the voice work with one step; the adapter for the first is built):
1. **Buy an Azure Speech resource** (Standard S0) and put its key in the repository secret `AZURE_SPEECH_KEY` and the region in
   the variable `AZURE_SPEECH_REGION`; deploy with `app_voice: true`, `voice_engine: azure`. Why first: it is the only option
   whose documented Arabic phone set takes the app's own reading phone for phone — so the endings, the waṣl and the emphatics
   are the app's, not the service's — at a one-time cost of tens of dollars; Microsoft's only condition on the audio is
   disclosure, which the app already makes. Unknown until the first call: whether every phoneme element is honoured for ar-SA
   (a refused sentence falls back to its vowelled text and is counted), and how natural the voice sounds — render the test
   set first (`voice_app.py --engine azure --package content/samples/al-asad-wa-al-far --out /tmp/x`) and listen.
2. **Allow huggingface.co** for this container (files: `MBZUAI/speecht5_tts_clartts_ar` — the model, its tokenizer and config;
   `microsoft/speecht5_hifigan`; one speaker embedding), so the ArTST/ClArTTS voice can be tested and its licence read at the
   source. If its card's MIT and ClArTTS's CC BY 4.0 hold, it is free, open and trained on fully vowelled classical Arabic.
3. **Google Chirp 3 HD** (key + `texttospeech.googleapis.com`): the plain shelf fits a month's free tier; whether Arabic
   phonemes are accepted is undocumented — without them the service reads the letters (the Supertonic risk).
4. **The hoca's recordings** — the honest best voice, and the training data for an owned voice later.
