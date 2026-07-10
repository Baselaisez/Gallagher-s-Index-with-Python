# Product Spec v0.1 — Arabic Graded-Reader & Audiobook App

Derived from `../research/01-duchinese-competitive-research.md`. Every feature below is tagged
**[MVP]**, **[V1]** (first paid release), or **[LATER]**.

---

## 1. Vision & positioning

**One sentence:** *DuChinese for Arabic* — learn fusha by reading and listening to graded Islamic
stories, with the deepest grammar help in any reading app.

**Primary personas:**
1. **Madrasa/self-study student** (e.g. Turkey, South Asia, Indonesia, Western converts): knows the
   alphabet, some Quran exposure, wants to actually *read*; motivated by Islamic content.
2. **University Arabic student**: needs graded extensive reading + grammar reinforcement mapped to
   what they study (nahw/sarf).
3. **Heritage learner**: speaks a dialect, weak in fusha reading; wants meaningful content, not
   "Ali goes to the market."

**Positioning against the field:** LingQ/Beelinguapp = generic, no Arabic pedagogy. Quranic =
Quran vocabulary only. We own: *graded narrative content + morphology-aware reader + real grammar*.

## 2. Level system

Six named levels (mirroring DuChinese's proven ladder), dual-mapped to CEFR:

| # | Name (EN) | Name (AR) | CEFR | Text profile |
|---|---|---|---|---|
| 1 | Newbie | مبتدئ | A1 | 150–300 core words, full tashkeel, present tense + simple past, 3–6 word sentences |
| 2 | Elementary | أساسي | A2 | ~600 words, full tashkeel, common Form I–IV verbs, idafa, simple إنّ |
| 3 | Intermediate | متوسط | B1 | ~1,500 words, partial tashkeel default, relative clauses, broken plurals |
| 4 | Upper-Int. | فوق المتوسط | B2 | ~3,000 words, partial tashkeel, hollow/defective verbs, passive |
| 5 | Advanced | متقدم | C1 | ~5,000+ words, minimal tashkeel, adapted classical prose |
| 6 | Master | متمكن | C1+ | Original classical texts (light editorial notes only), full i'rab available on demand |

Every word in every story carries its level tag → colored underline in the reader (the Arabic
analogue of DuChinese's HSK color coding). **[MVP]**

## 3. Feature spec

### 3.1 Reader **[MVP]**
- Story page with RTL typography tuned for learners (generous line height, large Naskh font, font-size control).
- **Tashkeel toggle** — per-user: full / smart (only ambiguous words) / none. Three pre-rendered text layers per story (see data model). This is our pinyin-toggle equivalent and a headline feature.
- **Tap-word popup**: gloss (EN + TR at launch), vocalized form, root (جذر), part of speech, word audio, level tag. Buttons: *Save to flashcards*, *Grammar* (if a grammar note is linked).
- Sentence-synced audio: tap a sentence to hear it; karaoke-highlight during playback; speed 0.5×–2.0×.
- Per-story progress (% read, words saved, completed flag). Streaks. **[V1]**
- Offline downloads (premium). **[V1]**

### 3.2 Grammar layer — our #1 differentiator **[MVP, seeded small]**
- Grammar notes are standalone, reusable objects linked from words/phrases in stories.
- Each note: plain-language explanation → 2–3 examples from *actual stories in the library* →
  **"Common mistakes" (أخطاء شائعة)** block: the wrong form learners produce, why it's wrong, the fix.
- First 30 notes seeded from the pilot story's grammar (imperatives, إنّ vs أنّ, idafa definiteness,
  Form II vs IV causatives, لا الناهية vs لن, etc.).
- Grammar notes are browsable as a reference section, filterable by level. **[V1]**

### 3.3 Flashcards & games
- Save words (and grammar patterns **[V1]**) from the reader → personal SRS deck (FSRS or SM-2). **[MVP]**
- Review shows word → (tap) vocalized form → (tap) meaning: stepwise self-testing like DuChinese's redesign. **[MVP]**
- Game modes:
  - **Match** (word ↔ meaning, timed) **[V1]**
  - **Harakat game** — place the vowels on an unvocalized word from your deck **[V1]**
  - **Root family** — sort words by shared root **[LATER]**
  - **Spot the error** — sentence with a planted common mistake; find and fix it. Generated from the common-mistakes database. **[LATER]** (no competitor has this)
- Cards always link back to the sentence/story they came from. **[MVP]**

### 3.4 Audiobooks **[MVP]**
- Every story doubles as an audiobook: background playback, lock-screen controls, chapter list, sleep timer **[V1]**.
- Human-recorded clear fusha narration (studio). Word-level audio may be TTS at launch; story audio is human.

### 3.5 Content & self-updating **[MVP]**
- Server-driven catalog: stories, audio, glossaries, grammar notes are versioned content packages
  fetched at runtime — new content weekly with **no app-store release**.
- "New this week" feed + published cadence promise (target: 3 stories/week at launch levels).
- Serialized multi-chapter stories for retention; same-story-multiple-levels ("read it again as you grow").

### 3.6 Monetization
- **Lite (free):** 2–3 rotating free stories/week per level (rotation = server flag), flashcard deck
  capped at 100 cards, Match game only, no offline. No ads.
- **Premium:** full library, offline, unlimited flashcards + all games, grammar reference section,
  early access. Target price $7–10/mo, ~$60–80/yr, regional pricing from day one (TRY/IDR/PKR tiers).
- **[LATER]** lifetime "supporter" tier, family plan.

### 3.7 Accounts & sync **[MVP]**
Email/Apple/Google sign-in; deck + progress sync across devices.

## 4. MVP cut (what ships first)

**MVP = Reader + tap-word + tashkeel toggle + synced audio + basic SRS deck + 20–30 stories
across levels 1–3 + ~30 grammar notes + lite/premium gating + server-driven catalog.**
Explicitly *out* of MVP: games beyond basic review, levels 5–6 library depth, dialects, speaking,
social features, Android-first-week parity (pick one platform to launch).

## 5. Architecture sketch

- **Client:** Flutter (single codebase iOS/Android, strong RTL support) — decision pending prototype.
- **Backend:** thin API (auth, subscriptions, catalog, sync) + object storage/CDN for content packages.
  Content packages are static JSON + MP3 + alignment files (see data model) → cheap, cacheable, offline-friendly.
- **Content pipeline (editorial, offline):**
  1. Author/adapt story text (per level) →
  2. Morphological analysis & segmentation (CAMeL Tools / Farasa) → human review →
  3. Generate three tashkeel layers →
  4. Record audio → forced alignment to sentences (e.g. MFA / ctc-segmentation) →
  5. Link glossary + grammar notes → validate against JSON schema → publish package to CDN.
- **Payments:** RevenueCat (or store-native) for cross-platform subscription state.

## 6. Content strategy (first 6 months)

- Pilot: **وصية أبي حنيفة ليوسف بن خالد السمتي** at levels 2 / 4 / 6 (same story, three tellings) — the template that exercises every feature.
- Then: prophets' stories (level 1–2), sahaba stories (2–3), Kalila wa-Dimna-style fables (2–4),
  seerah episodes (3–5), adapted classical excerpts — Ibn al-Jawzi, al-Ghazali letters (5–6).
- Editorial rule from research: **beginner stories must be real stories** (arc, stakes, payoff) — the
  documented failure mode of DuChinese's low levels is dullness.
- All texts either public-domain classical works (adapted) or original retellings → clean IP.
- Scholarly review pass on every Islamic text (accuracy of attribution & content) before publishing;
  attribution note shown in-app per story.

## 7. Success metrics

- Activation: % of installs that finish one story in week 1.
- Retention: D7/D30; stories completed per weekly active user.
- Learning proxy: saved-word review completion rate; harakat-game accuracy trend.
- Revenue: lite→premium conversion (benchmark freemium readers: 2–5%), annual-plan share.

## 8. Open decisions

1. Client framework: Flutter vs React Native vs native iOS first (prototype the reader in Flutter first — RTL + custom text layout is the risk area).
2. Gloss languages at launch: EN only vs EN+TR.
3. SRS algorithm: FSRS (modern, open) vs classic SM-2 — lean FSRS.
4. Dialect support: out of scope until fusha library is deep (revisit at V2).
5. App name & brand.
