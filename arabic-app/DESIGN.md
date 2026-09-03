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

## 7. The statistical voice (wave 7)

Everything the machine-learned layer says wears one visual language, so a
learner recognises "this is the model talking" before reading a word:

- **Belief is a bar.** `.mbar` — role-palette fill, width = probability,
  tabular-nums percentage. Bars are the model's kanaat, never a ruling; a
  runner-up below 3% belief draws no bar at all, because a %0 bar is
  furniture, not honesty.
- **Evidence is a chip row.** `.feat-chip` — the features the word fired,
  each named in plain language. The model never asserts without showing
  what it saw.
- **The model's color is the lvl3 amber** the 🧠/🤖 chips already taught;
  a correct model verdict may relax to `--ok`, but the badge stays.
- **The duel banner** (`.duel-banner`) puts the learner and the model side
  by side: the model's pick, its percentage, its verdict, and the running
  tally — statistics racing a human, with the hand analysis as referee.
- Every surface that quotes the model leads with its **held-out** score,
  never the resubstitution one.

## 8. The balagha door (wave 9)

A sentence carrying a named-clause layer says so where the reader is —
in the margin, not three taps deep:

- **`.jml-chip`** — a quiet pill beside the play/tarkib buttons: `✦ بَلَاغَة`,
  sized to the 1.7rem tool-row rhythm, colored in the tabi hue
  (`--role-tabi`) so it reads as "layer", not "action". It is a DOOR:
  tapping it opens the same tarkib sheet the layer lives in — never a
  second copy of the content.
- Chips render only from data (`sen.jumal`), never from a manifest flag,
  and hide in print with the other tools.
- Restraint rule: one chip per sentence, no count, no color escalation —
  the layer's richness is inside the sheet; the margin only says the
  door exists.

## 9. The joining voice (wave 10)

The frame family now reads by spine color, one hue per discipline of
claim: the shart frames keep the accent, the insha/istifham frames the
teal (`--lvl2`), and the new fasl–wasl frames wear the TABI hue
(`--role-tabi`) — atf is the tawabi' doctrine lifted from words to
jumlas, and the color says so before the title is read. Rule: a new
frame engine picks its spine from the role palette by the DOCTRINE it
teaches, never a novel color.

## 10. The muhaqqiq's red ink (wave 11)

The composed i'rab is a SCHOLAR'S VOICE, and it gets a scholar's color:
`--irab-ink` (#96402F light / #D08A73 dark — the muhaqqiq's red of
critical editions) defined in all six theme blocks, worn by `.murib`
(the Murib's Arabic line), `.murib-x` stays in the soft UI ink, and
`.irab-ar` — the stored human i'rab — now shares the same red, so the
two voices that both speak i'rab read as one register. Rules:

- The red is for I'RAB PROSE only — never for the corpus text, never
  for UI chrome. A third user of the token must be another line that
  states an i'rab.
- `.murib::before` prints «إِعْرَابُهُ:» at 60% — the label is furniture,
  the claim is the content.
- The model's office never enters the red line: it rides after the
  translation as the badged 🧠 chip in the standing amber. Statistics
  keep their color; rules keep theirs.

## 11. The rule ledger, the arc map, and the sky (wave 12)

Three new surfaces, and each one is the app's existing register applied
to a new object, not a new register:

- **The rule ledger** (`.qw-ledger`) lists the nahw rules a sentence
  must keep, one row each: a ✓ in `--ok` or a ✗ in `--danger` on the
  inline-start rail (the same rail the verdict cards use for certainty),
  the word in the Arabic face, the rule's Arabic in the muhaqqiq's red
  (`--irab-ink` — it is i'rab prose, so it wears i'rab's ink), its EN/TR
  gloss in the soft ink, and a `§` pill that opens the grammar note the
  rule cites. A broken row tints its panel 6% toward `--danger` — the
  only place the danger token colours a background, because a broken
  rule is the one thing on this page that must be seen before it is
  read. The seeded errors sit under the ledger as dashed pills: they
  are invitations, not content, and the dashed border says so.
- **The arc map** (`.shajara`) draws the sentence right-to-left as
  rounded boxes on one baseline and every settled relation as an arc
  above them. It is the second thing on the page allowed to scroll
  sideways, and like the rail it scrolls inside its own box. Verbs get
  the accent stroke, particles a dashed one, nouns the line colour; the
  case under each box is red because it is a claim. Arcs are red by
  default, accent for ta'alluq (the Ta'alluq engine's own colour in the
  kernel), and the shart pair wears `--lvl3` — the frame palette's
  standing amber. Arc height grows with the level of nesting, and the
  label sits at the apex; two arcs never share an apex height.
- **The atlas** (`.atlas`) is the reference list as a sky. The four
  level tokens colour the stars exactly as they colour the level chips
  everywhere else; star radius is the number of corpus sentences that
  anchor the note, so an unanchored note is visibly the smallest thing
  on the map; links are the accent at 28%, rings and sector lines the
  line colour, sector names the soft ink. The list/atlas toggle is a
  segmented pair in the sheet's own pill idiom. Nothing on the map is
  placed by hand: a new note takes its seat the day it is authored.

Rule: a diagram is a **restatement**. Every arc, every star size and
every ledger row repeats a verdict some engine already made, so a wrong
picture is a wrong engine, and the gate can say which one.

## 12. The dabt lab, the corrector's red pen, and the engine's own hand (wave 13)

Wave 12 made the engines *say* which rule a sentence obeys. Wave 13 makes
them *write*: the DabtEngine strips a sentence's endings and puts them
back from the governors alone, and the SarfMusahhih rebuilds a wrong verb
from its root. Three surfaces carry that, each in the register the app
already owns:

- **The dabt lab** (`.dabt-line`, `.dabt-w`) sets the sentence right-to-
  left in the Arabic face, large, and underlines every word with the
  colour of the thing that decided it: the accent for **nahw** (a
  governor wrote this ending), `--lvl3` amber for a **paradigm cell**,
  `--lvl2` for the **lexicon** (a stored head-word), the line colour for a
  **closed-class** word kept as it stands, and a dotted soft-ink line for
  a word the rules left **undecided**. The legend under the line repeats
  those five strokes; nothing on the line is coloured by any other logic.
  A tapped word opens a detail card on the accent rail — the word large
  and in the accent, the rule's Arabic in the muhaqqiq's red
  (`--irab-ink`, it is i'rab prose), its EN/TR gloss, «annexed to word n»
  when a chain decided it, and the `§` pill of the grammar note the rule
  cites. When the learner types a sentence WITH its marks, the lab checks
  it: a word whose ending the rules write differently is tinted 12%
  toward `--danger` with the learner's own form struck through beside it,
  and a one-line verdict above the line counts the disagreements — the
  same red pen as the muhaqqiq's, on the learner's page. Two pills switch
  the mode (endings only / every mark) in the sheet's segmented idiom; a
  «grade the engine on the corpus» button writes one bar per story and
  never runs until asked, because a full-corpus grade is work the phone
  should do on request.
- **The corrector** appears in two places and looks the same in both. In
  the Qawaid ledger a ✗ row now ends with «the rules write ‹word›» in
  `--ok` green — the correction is the good news on a bad row, and green
  is the only colour good news wears. In the Sarf ledger a word no
  paradigm owns, or a narration that ends «differs», gets a card on a
  `--danger` rail: the written form struck, an arrow, the rebuilt cell in
  bold `--ok`, one sentence saying WHY (the asl matched — the i'lal was
  skipped — or the nearest buildable cell), and the i'lal steps of that
  cell only, numbered exactly as the I'lal lab numbers them.
- **The tahqiq strip** (`.tq-dabt`) sits under the tahqiq table of every
  corpus sentence: the sentence re-vowelled by the engine, in the dabt
  line's own colours, with the stored ending struck beside any word the
  engine wrote differently, and a «n/N endings rebuilt exactly» line. It
  is the same restatement discipline as the arc map: every underline
  repeats a decision the ledger already lists, so a wrong colour is a bug
  in an engine, never in the strip.

Rule: the engine's hand is **coloured by source, never by verdict**. A
word is not red because it is wrong; it is red only where the learner's
own mark and the rules disagree, and the source colour under it still
says who decided. The learner should always be able to answer «who wrote
this ending?» before asking «is it right?».

## 13. The bayan door: the tashbih diagram (wave 14)

Fann 2 of the Talkhis begins with tashbih, and the app's first bayan
surface is a diagram of its four arkan — drawn, like the arc map, as a
**restatement** of seats the nahw engines already filled:

- **The two ends** are boxes on one baseline, the mushabbah on the
  right (reading direction) in the accent stroke, the mushabbah bihi on
  the left in `--lvl3` amber — the same pair of colours the ḍabṭ line uses
  for «nahw» and «paradigm», because a tashbih is a nahw seat (mubtada,
  majrur, inna's ism and khabar) wearing a bayan name.
- **The adat** is the arc between them, in the muhaqqiq's red
  (`--irab-ink`), its text (كَ، كَأَنَّ، مِثْلُ، the verb) at the apex. Where
  no adat is spoken the arc is dashed in the soft ink and reads «بِلَا
  أَدَاةٍ» — the baligh shape is a likeness with the tool withdrawn, and a
  dashed line is how this app has always drawn a thing understood but not
  written (the arc map's unspoken governors, the dabt line's undecided
  word).
- **The wajh** sits under the arc in `--lvl2`: the shared meaning when it
  is spoken (كَرَمًا، فِي الشَّجَاعَةِ), or «مُجْمَلٌ — وَجْهُ الشَّبَهِ مَحْذُوفٌ» when
  it is not. The kind chips beneath (مُرْسَل/مُؤَكَّد · مُفَصَّل/مُجْمَل ·
  بَلِيغ) are the sheet's pill idiom; the rukn list under them repeats the
  diagram as rows with the four colour dots, for the reader who wants
  words rather than a picture.
- **The authored frame** is the gate. A chapter that teaches tashbih
  stores each likening's arkan by token index; the sheet says in `--ok`
  green when the engine's reading agrees and in `--danger` when it does
  not, and the smoke suite refuses a chapter whose engine and author
  disagree. The ✦ chip in the reader's margin says «تَشْبِيه» instead of
  «بَلَاغَة» on such a sentence — the door is named for what is behind it.
- **The atlas** gained a fifth sector, الْبَيَان, laid out by the same fan
  as the other four; its two first stars (ʿilm al-bayan, the arkan) take
  their seats without a line of layout code.

Rule: the engine never asserts a likeness it cannot ground in a seat. A
fused kaf, كَأَنَّ, an annexed مِثْل, or a verb of likening is a seat; a
bare nominal sentence is one only when the lexicon vouches for the khabar
as a stock likeness (أَسَد، بَحْر، بَدْر…). Everything else is silence, and
the note — not the diagram — teaches the hissi/ʿaqli/khayali/wahmi
sorting, because that sorting is a judgement of the world, not of the
sentence.
