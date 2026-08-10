# Qissa — the design system

One page. Read it before adding a surface; the app is a single HTML file and
nothing stops you inventing a fifth radius, so the discipline has to be
written down and gated.

The smoke suite enforces what a browser can check: every token below
resolves, a primary action never renders under 44px tall, the front door's
numbers match the deck's own, and **the phone layout is tested at 390×844** —
the thumb bar does not exist at desktop width, which is exactly how a
navigation bug ships unnoticed. The rest is on us.

---

## 1. What we borrowed, and why

The reading apps people keep on their phones for years — Duolingo, DuChinese,
LingQ, Readlang, Anki — do not agree on much. They agree on five things, and
those five are the whole system here.

| What they all do | What Qissa does with it |
|---|---|
| **Destinations under the thumb.** A phone's navigation lives at the bottom, where the hand already is; the top is for context, not for choices. | `.tabbar` below 860px: Library · Deck · Games · Atölye · Progress. Above 860px it is gone and the toolbar is the navigation. |
| **One thing per screen.** The reader reads; the drill drills. No sidebar of options competing with the sentence. | The reader page holds text and nothing else; every tool opens in a sheet over it, and closing the sheet returns you exactly where you were. |
| **Tap is the primitive.** Everything a finger reaches is big, round-cornered, and separated by real space. | `--tap: 44px` is a floor under `.btn`, and the smoke suite measures a live button rather than trusting the rule. |
| **Progress is visible without being asked for.** Streak, due count, what is fading. | The deck badge, the streak row, the fading-words whisper in the games hub, and the model's own accuracy line in the Atölye. |
| **Failure teaches.** A wrong answer is a lesson, not a buzzer. | Every game returns the right answer AND a refutation keyed to the specific wrong pick (`whyNot`). |
| **Restraint in colour.** One accent, one danger, one success; everything else is ink on paper. | The palette is six roles and four level colours. The role-highlighting layer is the only place many colours appear at once, and it is opt-in. |

What we deliberately did **not** borrow: gamified pressure. No hearts, no
lost streaks, no "you're falling behind". The corpus is a madrasah curriculum
and the tone stays a teacher's, not a slot machine's.

---

## 2. Tokens

Defined once on `:root` in `prototype/reader.html`. **These are the only sizes
the app may use.** A literal `padding: .9rem` in a new rule is a bug even if
it looks right.

### Space — a 4px grid

```
--s1 .25rem (4)   --s2 .5rem (8)    --s3 .75rem (12)   --s4 1rem (16)
--s5 1.5rem (24)  --s6 2rem (32)    --s7 3rem (48)
```

`--s2` between related things, `--s3` inside a card, `--s4` between cards,
`--s5`+ between sections. If you want something between two steps, you want
one of the two steps.

### Type — ratio ≈ 1.2

```
--t-xs .72   --t-sm .82   --t-md .94   --t-lg 1.1   --t-xl 1.35   --t-2xl 1.7   (rem)
--lh-tight 1.25   --lh-body 1.6   --track-caps .1em
```

Arabic is **not** on this scale. It rides `--ar-font` at sizes chosen per
surface, because naskh at 0.94rem is unreadable while Latin at 0.94rem is
comfortable — a shared scale across scripts would be a false economy. Arabic
display sizes in this app run 1.05rem (an inline rule) to 1.7rem (a headline
form) and always carry `direction: rtl`.

Small-caps labels (`.k`, `.if-lbl`, `.game-group`) are `--t-xs`, weight 600–700,
`letter-spacing: --track-caps`, `text-transform: uppercase`, `opacity: .55–.6`.
That combination is the app's one "label" voice; do not invent a second.

### Radius

```
--r-sm 8px      inline chips, inset blocks
--r-md 12px     buttons, list rows
--radius 14px   cards (legacy name, still the card radius)
--radius-lg 20px  sheets and large panels
--r-full 999px  pills and toggles
```

### Elevation

```
--e1  hover lift on an interactive card
--e2  a panel that floats over content
--shadow / --shadow-sm  the sheet and the reader header (legacy, theme-aware)
```

Elevation is for *interaction*, never for decoration. A static card gets a
border, not a shadow.

### Motion

```
--dur-fast .12s   colour, border, opacity
--dur-base .2s    transforms, lifts
--dur-slow .34s   sheets, page-level transitions
--ease cubic-bezier(.2, .8, .3, 1)
```

One easing curve for everything. Every transform-based effect sits inside
`@media (prefers-reduced-motion: no-preference)` — nothing that moves is
load-bearing.

### Measure

```
--measure 40rem
```

The reading column. Long enough to carry a matn line without breaking it in
an ugly place, short enough that the eye finds the next line without hunting.
Applied to `#story` only when it is NOT holding library cards — the shelf
wants the full width, the text does not.

### Touch

```
--tap 44px
```

A floor, not a target. `.btn` enforces it with `min-height`. Header chips
(`.tbtn`) sit at 34px by deliberate exception: they are a dense toolbar the
pointer scans, not a primary action a thumb reaches for. Any NEW class a
thumb hits takes the floor.

---

## 3. Components

**Card** — `1px solid var(--line)`, `var(--radius)`, `var(--panel)`,
`padding: var(--s4)`, `--e1` on hover only. Cards never nest more than two
deep; a third level means the content wants its own sheet.

**Sheet** — the app's one modal surface. `--radius-lg`, `--shadow`, a scrim,
and a `.tabs` row at the top when it has more than one view. Everything that
is not reading happens here.

**Verdict block** — an engine's answer: the form large and centred, then
labelled rows underneath (`.nida-verdict`, `.ilal-flow`). Arabic first at
`--t-2xl`, the reading beneath it at `--t-sm`. The pattern is deliberate: the
learner should see the Arabic before the explanation, every time.

**Step list** — a derivation (`.ilal-steps`). Numbered circle in
`--accent-soft`, the forms in Arabic, the rule in Arabic, the gloss in
`--ink-soft`. Used wherever the app shows *work*, not just an answer.

**Shelf heading** — `.game-group`: an Arabic word in `--accent`, a Latin
label in the label voice, and a hairline rule filling the row. Used to break
a long grid into disciplines.

**Stat strip** — `.stat-strip` + `.st-tile`: three tiles at the front door,
never more. An Arabic word in `--accent`, the number at `--t-xl` in tabular
figures, the label in the label voice. Every number is read live from
`deckStats()` / `state.streak`, so the strip cannot disagree with the deck —
the smoke suite compares the two. The whole row is one tap into the deck.

**Thumb bar** — `.tabbar`: five destinations, fixed to the bottom, shown
below 860px. Three rules it must keep. (1) **It owns no behaviour.** Every
button delegates to the toolbar handler that already implements that
destination, so there is one implementation per destination and the two
navigations cannot drift. (2) **No icon-only tabs.** Every tab carries a word
under its glyph; an icon alone is a guessing game, and the smoke suite fails
if a label is empty. (3) **State is derived, never stored.** The active item
is computed from what is actually on screen at paint time, so there is no
"current tab" to go stale. Every destination stays live: Games plays from the
whole library at the front door and from the open story once one is open, so
there is nothing to disable.

**Amil walk** — `.ibara-why` + `.ib-pairs`: the İbare game's reveal. Each row
is one governor/governed pair, Arabic first at `--t-lg`, the naming of the
relation in Arabic beside it, the reading beneath in `--ink-soft`. It is the
Step list pattern applied to syntax rather than morphology: the app shows its
WORK, not just its verdict.

**Scope banner** — `.game-scope`: one line at the top of the games hub saying
what the round will be drawn from — this story, or the whole library. A
learner should never have to start a round to find out what it will ask
about.

**Refutation** — `.game-wrongwhy`: `--role-maful` spine, `--accent-soft`
ground. Only ever holds a sentence explaining why *your* answer fails.

**Workshop rail** — `.tabs.labrail`: the Atölye's tool picker. Ten tools do not
fit a phone as a wrapping row of text buttons — they wrapped to five lines
(248px) and pushed the tool itself below the fold. The rail is one line (53px),
scrolls sideways, snaps, and fades at both edges so a half-visible pill reads as
"there is more" rather than as a clipping bug. **It is the only element in the
app allowed to scroll sideways**, and the smoke suite asserts the page body
never does. Three rules: the selected pill is scrolled into view on open and on
every change (a rail whose selection is off-screen looks like nothing is
selected); every pill clears the 44px thumb floor; and every pill carries a
**word**, not only a glyph — the emoji is the first thing dropped on the
narrowest phones, never the label.

**Two-answer block** — `.mz-ism`: where a surface has both a computed answer and
a learned one, they sit side by side and are **never blended**. Accent rail and
"COMPUTED" on the derived one, amber rail and "LEARNED" plus a percentage on the
model's. A learner must always be able to see which kind of claim they are
reading. Used by the Mizan lab; the pattern generalises to any rule/model pair.

**Builder block** — `.idf-out` + `.idf-steps` + `.idf-refuse`: for engines that
construct rather than describe. The result first and largest, its parts coloured
by role, then role chips **running right-to-left underneath so each chip sits
under the word it names** (left-to-right put the mudaf's chip under the mudaf
ilayh), then a numbered step list of the rules that fired. The refusal is a
sibling, not an error state: `--danger` border, the rule in Arabic, the reason in
prose. A refusal that names its rule is a teaching surface, so it is designed
like one.

**Verdict stack** — `.vlist` / `.vrow`: one card per word, replacing the
analyzer's table. A table of i'rab needs a sideways scroll on a phone, and an
i'rab you must scroll sideways to read is one you do not read; the smoke suite
asserts no card overflows its own width at 390×844. Inside a card the order is
always the same, and it is the order a hoca speaks in: the word (`--t-xl`,
RTL, with its segmentation beside it), then the lemma and its gloss, then the
chips that place it (root, wazn, and `guess` when the surface only inferred),
then the ruling in prose, then the badges that say HOW the ruling was reached.

The 4px rail on the inline-start carries **certainty**, and it is the one
thing you can read from across the room: `--accent` when the engines settled
it, `--lvl3` when they guessed. It is never the only signal — the guessed
cards also carry the word for it in a chip.

**Reading block** — `.vread`: `--accent` border on `--accent-soft`, always
last, always after the verdicts. It holds what the sentence comes out
*meaning* — the thing the learner came for — and beneath it, in `.vnote`, why
the meaning comes out that way. It appears only when the engine can name the
structure; there is no empty state, because a half-guessed translation teaches
worse than none.

---

## 4. Theme

Three palettes, kept verbatim in step: `:root` (light), the
`prefers-color-scheme: dark` media query, and `html[data-theme=...]` for the
manual toggle. **Never define a colour in only one of the three.** The
toggle cycles auto → light → dark, and the smoke suite asserts that an
explicit choice beats the OS.

## 5. Accessibility

- Focus is visible everywhere: `2px solid var(--accent)`, `offset: 2px`.
- Colour is never the only signal — the role layer pairs hue with a legend,
  the games pair right/wrong colour with a ✔ and a written refutation.
- Every string is bilingual EN/TR; the i18n gate fails the release if a key
  exists in one language and not the other.
- Wide content scrolls inside its own container; the body never scrolls
  sideways.

## 6. Adding a surface

1. Sketch it with the tokens above. If you reach for a literal, stop.
2. Arabic first, gloss second, in every block that shows a form.
3. If a finger taps it, give it `min-height: var(--tap)`.
4. If it moves, guard it with `prefers-reduced-motion`.
5. If it teaches, say *why* — the app's whole voice is the reason, not the
   verdict.
