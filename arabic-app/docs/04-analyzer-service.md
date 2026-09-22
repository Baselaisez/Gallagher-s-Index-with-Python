# Analyzer Service & App-Store Architecture v0.1

The "upload your own text" ability: a user uploads 2-3 pages of classical Arabic (fiqh,
hadith, history, adab) and gets the full reader treatment — tashkeel layers, tap-word
glossary (EN/TR), trilingual i'rab, and links into the **same global grammar registry**
(`content/grammar/`) as the embedded stories. Both modes coexist: embedded (editorial,
studio audio, scholarly-reviewed) and ability (on-demand, machine-generated, device TTS).

## What exists today (this repo)

`tools/analyze_text.py` — the pipeline core, runnable from a laptop with an
`ANTHROPIC_API_KEY` (or `ant auth login`):

```
raw .txt ──► chunk by paragraphs (~400 words → chapters)
         ──► Claude (claude-opus-4-8, streaming, structured JSON output)
               • system prompt = Qissa package rules + tashkeel-layer law
               • user msg = global grammar registry (ids+titles) + the text
         ──► post-processing (enforce strip(full)==bare, drop non-registry
               grammar ids → suggested-notes.json)
         ──► content package (manifest/chapters/glossary)
         ──► tools/validate_content.py  (same gate as editorial content)
         ──► optional --build-reader → standalone reader.html
```

Demo output committed at `content/user-uploads/deeds-are-by-intentions/` (hadith
إنما الأعمال بالنيات, generated via the pipeline's mock mode).

Key design decisions:

- **One grammar registry for everything.** The model may only link grammar ids that
  exist in `content/grammar/`; إنّ opens the identical note in every story and every
  upload. Unknown topics come back as `suggestedNotes` — an editorial to-do list that
  grows the registry, never a fork of it.
- **The validator is the contract.** Machine output passes the exact same gate as
  editorial content; the tashkeel-layer law is additionally re-enforced in code after
  the model responds (belt and braces).
- **Honest provenance.** Uploaded packages are stamped
  `reviewStatus: "auto-generated-unreviewed"` and the app shows a "machine-analyzed —
  may contain errors" banner. Embedded content keeps human review.
- **Voice for uploads**: no studio audio exists, so the reader's sentence ▶ falls back
  to Arabic TTS of the fully-vocalized layer (already implemented in the prototype).
  Because the `full` layer carries complete tashkeel, TTS quality is far better than
  reading raw unvocalized text. Server-side neural Arabic TTS (Azure/Google, fusha
  voices) is the V2 upgrade, cached per sentence.

## Production shape (mobile app era)

```
Flutter app ──HTTPS──► Qissa API (auth, quotas, catalog)
                         │
      upload .txt/.pdf ──┤ POST /analyses           (premium-gated)
                         ▼
                   job queue (async; 2-3 pages ≈ 1-3 min)
                         ▼
                   analyzer worker = analyze_text.py logic
                    (Anthropic API, structured outputs, chunked)
                         ▼
                   validate → store package in object storage/CDN
                         ▼
      app polls /analyses/{id} → downloads package → renders in the
      SAME reader component as embedded stories ("My Texts" library)
```

- **Quotas by tier** (drives premium conversion): Lite = 1 short analysis/month
  (≤1 page); Premium = e.g. 30 pages/month; overflow as consumable IAP.
- **Cost model**: 2-3 pages ≈ 700-1000 words ≈ 1300+ tokens in, but the analysis JSON
  is ~30-60× the input (layers, i'rab ×3 languages, glossary) → expect roughly
  30k-80k output tokens per upload. At Opus 4.8 rates ($5/$25 per MTok) that is
  ~$1-2 per upload — fine under a premium quota; `claude-sonnet-5` (~$3/$15, near-Opus
  on structured tasks) is the cost lever if volume demands it. Cache the system prompt
  (`cache_control` is already set in the script) — the registry+rules prefix is
  identical across all uploads.
- **PDF/scan input**: send the PDF pages to Claude as document blocks in a first
  "extract the Arabic text" pass, then run the normal analysis. (The Files API keeps
  re-used uploads cheap.)
- **Safety/robustness**: handle `stop_reason: "refusal"` (surface a friendly message),
  cap input size, moderate user uploads per store policies, and keep the
  suggested-notes stream flowing into the editorial grammar backlog.

## App-store roadmap (long term)

1. **Now → prototype parity in Flutter**: one codebase for Google Play + App Store;
   the reader screen renders the same content packages; `flutter_tts` for device
   Arabic TTS; RevenueCat for cross-store subscriptions (Lite/Premium per spec §3.6).
2. **Backend v1**: catalog + auth + sync (spec §5) plus the analyzer endpoint above.
3. **Store listings**: EN/TR/AR metadata; content rating "Everyone"; the
   auto-generated-content disclosure both stores require for LLM features.
4. **Post-launch**: server TTS for uploads, level-4/6 sibling stories, flashcard games
   (spot-the-error generates from the same grammar registry), teacher/madrasa plans.
