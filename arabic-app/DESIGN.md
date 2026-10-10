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

## 14. The sky that knows what it computes, and the wajh with a shape (wave 15)

**The Atlas grew two overlays and a hand.** Every star is a grammar note;
wave 15 rings the stars an exact engine computes (`QawaidAtlas.ENGINE_OF`
— the note-id family → the lab that owns it) and prints the count above
the sky: *88 of 154 notes are computed by an engine (57%) — the ringed
stars; the rest the app still only teaches.* The ring is the accent
stroke at 1.1px, 2.6px outside the star, so it reads as an orbit rather
than a second star; a toggle (`⚙ engines`) fades everything unringed to
12% and the links to 6%, which turns the sky into a coverage map of the
automation itself. The second overlay is the reader's: a star anchored
in a sentence they have actually read wears a soft amber halo
(`--lvl3` at 22% alpha, radius +5) and an amber stroke — the Progress
page's numbers, seen as constellations. Both overlays are computed at
render from `GRAMMAR` and `state.progress`; nothing is stored. The hand:
hovering or focusing a star adds `.at-focus` to the sky — its links go to
95% and 1.6px, its neighbours keep full opacity and bold labels, the
rest of the sky recedes to 25% (stars) and 5% (lines). Every link carries
`data-a`/`data-b`, so the lighting is a class toggle, no re-render. A
ringed note's sheet grows a second action, **⚙ open in the lab**, which
sets `conjState.lab` and opens the Atölye on that tab — the sky is now a
door into the engines, not only into the notes.

**The tashbih diagram wears the SHAPE of each end.** Under the word in
each box a small `--ink-soft` badge names it — مُفْرَدٌ / مُقَيَّدٌ / مُرَكَّبٌ —
and the wajh line adds «— هَيْئَةٌ» when the spoken wajh is a composite.
The kinds row gains dashed chips for the shapes (dashed = a claim about
form, solid = a claim about presence). In the lab a ruled block,
**أَقْسَامُ وَجْهِ الشَّبَهِ**, lists the six divisions the surface cannot
settle as a two-column shortlist (Arabic term, then the gloss in the UI
language) with the counts line beneath and the note's § — the same
«claimed / not claimed» split as the Sarf ledger, rendered as a list
rather than dressed as a verdict.

**The Ism lab stacks the qiyasi plurals under the diminutive and the
nisba** in the same phrase-and-rule rhythm as the Aded lab: the dual and
its construct forms on one line (small print: «in construct — the nun
dropped»), the feminine plural, the masculine plural or its refusal in
the sarf-note colour. A refusal is a sentence, never a blank.

## 15. The badges of a likening, and the bridge of a majaz (wave 16)

**The tashbih diagram now says how many, and how much is left unsaid.**
Two small labels ride the top edge of the diagram: on the reading side a
**rank ribbon** (`.ts-rank` — أَعْلَى / مُتَوَسِّطُ / أَدْنَى الْمَرَاتِبِ), solid
because it is a claim about what was DROPPED — adat, wajh, or both — and
the highest rank fills with `--accent-soft` so a bare «زَيْدٌ أَسَدٌ» is
visibly the summit; on the far side a **taʿaddud tag** (`.ts-ta`, dashed
`--lvl2` stroke, the dashed = a claim about form convention of §14) that
names مَلْفُوفٌ / مَفْرُوقٌ / تَسْوِيَةٌ / جَمْعٌ. When an end holds several things
the box corner wears a `--accent` count badge (`.ts-num`, ×2, ×3 — the
count is taken off the joined members, never guessed), and the wajh line
adds «— هَيْئَةٌ (تَمْثِيلٌ)» where the wajh is a picture. The chips row
mirrors all of it: rank solid, taʿaddud and tamthil dashed. In the lab
two ruled blocks follow the wajh divisions: **أَقْسَامُ التَّشْبِيهِ وَمَرَاتِبُهُ**
(a two-column legend of the engine's own claims, with its §) and
**أَغْرَاضُ التَّشْبِيهِ** — the eight aims as a shortlist, because why a
speaker likens is knowledge of the speaker, not of the sentence.

**The majaz bridge.** `majazSvg` draws the literal meaning on the right
(الْحَقِيقَةُ, the word itself under it, and beneath the box the QARINA that
bars the literal reading, underlined by a bar in `--lvl3`), the intended
meaning on the left (الْمُرَادُ), and the ʿalaqa as the arch between them —
the same arc as the tashbih adat, dashed when the engine offers the
frame as a candidate rather than a receipt. A frame the AUTHOR wrote and
the engine did not read is still drawn, wearing a dotted «authored»
chip: the answer key is the content, and the panel grades the engine on
it in the open. The Atölye tab **مَجَاز** carries the seeds the books
recite (لَيْسَ كَمِثْلِهِ، وَاسْأَلِ الْقَرْيَةَ، أَنْبَتَ الرَّبِيعُ الْبَقْلَ …) so a
learner can see the four surface-settled kinds fire one after another.

**Density rule, restated for the badges.** Nothing in this wave added a
row to the diagram; every new fact is a badge, a tag or a chip on a
surface that already existed, and each is ≤ 11px SVG text in an existing
colour role. If a badge cannot be read as a *claim* (solid) or a *reading
of form* (dashed) it does not belong on the diagram — it belongs in the
lab's shortlist blocks.

## 16. The istiʿara's badges, and the six-kinds grid (wave 17)

**What the surface settles wears a solid chip; what the chapter names
wears a dashed one.** Under every istiʿara frame on the majaz bridge a
second chip row (`.mj-ist`) carries the IstiaraEngine's reading: the
**lafz** (أَصْلِيَّةٌ / تَبَعِيَّةٌ / مَكْنِيَّةٌ / تَخْيِيلِيَّةٌ) as a rank-style solid
chip, because the lent word's class is the word's own and the engine is
never in doubt about it; the **seat of the clue** («الْقَرِينَةُ فِي الْمَفْعُولِ»)
solid when DabtEngine's own seats settled it, dashed when only the author
named it; the **mulaʾim kind** (مُطْلَقَةٌ / مُجَرَّدَةٌ / مُرَشَّحَةٌ, or both)
solid, since it is read off a stored field table; the **ends** (وِفَاقِيَّةٌ /
عِنَادِيَّةٌ, with تَهَكُّمِيَّةٌ beside it when the contrary table fired) solid only
for the word that does not exist and the verb that mocks; and the
**sensory-mental triple** («حِسِّيٌّ · حِسِّيٌّ · عَقْلِيٌّ» — minhu · lahu · jamiʿ)
always dashed, because two of its three are the reader's knowledge. The
convention is §14's, unchanged: solid = a claim the engine will defend,
dashed = a claim it shows.

**The mulaʾim words are named, not merely counted.** A third row
(`.mj-mulaim`) prints the words the engine ties to the lent word's field
(«مُلَائِمُ الْمُسْتَعَارِ مِنْهُ: لِبَدٌ أَظْفَارُهُ», underlined in `--accent`) and the
words that hang on the lent word without belonging to it («مُلَائِمُ
الْمُسْتَعَارِ لَهُ: شَاكِي السِّلَاحِ مُقَذَّفٍ», dotted `--lvl3`). The two underline
weights are the tarshih and the tajrid made visible: the solid one feeds
the borrowed word with its own sense, the dotted one strips it back
toward the thing meant. They live in the frame rather than on the
sentence itself, so that a bayt with two istiʿaras (Zuhayr's lion beside
the tongue of a state) keeps each set of underlines with its own bridge.

**The six-kinds grid.** The Majaz lab gains a 3 × 2 table
(`.mj-six-grid`, two columns on a phone) — one cell per kind of the
Talkhis's sixfold division by what is sensed: the cell number, the
triple in `--irab-ink`, the lent word large in `--accent`, and the aya
or example under it. Every cell is a seed button: tapping it runs the
sentence through the engine, so the reader moves from the chapter's
table to the engine's reading of the same words in one touch. The grid
follows the seeds, not the frame, because it is a map of the chapter,
not a claim about the sentence typed.

## 17. The kinaya ladder, the tibaq poles, and the ghost layer (wave 18)

**A kinaya is a climb, so it is drawn as one.** Under every kinaya frame in
the sheet and the lab, `kinayaLadderSvg` stands two rails between the SAID
at the foot (الْمَكْنِيُّ بِهِ — the words themselves, in the reading face) and
the MEANT at the top (الْمَكْنِيُّ عَنْهُ — the chapter's `lazim`, in the UI face
on the accent-soft ground), and the chapter's own `wasait` become the
rungs, numbered from the bottom, each carrying its EN/TR gloss. No rung
means the near kinaya, and the space between the rails says so in the ok
colour (قَرِيبَةٌ · near); four rungs is the far one, and the chip row under
the ladder repeats the count and Sakkaki's name for it (إِيمَاءٌ / رَمْزٌ /
تَلْوِيحٌ — solid when the chapter names it, dashed when the count alone
proposes it). The engine never knows the rungs: they are content, and the
ladder is content drawn; what the engine adds is the KIND (a chip in the
Arabic face) and the pronoun test — on the taṣrīḥ frame the sifa carries
its doer folded in, and the ladder shows it as **[هُوَ]** after the head word,
the same glyph the taqdir layer uses, because it is the same fact.

**The tibaq is two poles facing.** `badiHtml` draws the pair as two bordered
words with ⇄ between them; a pole under a negation wears a dashed border
and its particle in the danger colour, so the tibaq of negation is visibly
«the same word, once denied». The chips name the sub-kind, the class
(اسْمَانِ / فِعْلَانِ / حَرْفَانِ / مِنْ نَوْعَيْنِ) and the receipt — the stored table
or the surface alone.

**The doors strip says which of the four bayan doors a sentence opens.**
Above the panels, four small doors (🪞 تَشْبِيه · 🌉 مَجَاز · 🪜 كِنَايَة · ⇄ طِبَاق)
sit in a row; a lit door is solid on the accent-soft ground, an unlit one
dashed and faded. It is computed from the authored frames OR the engines'
reading, at open, on the one sentence — never at render of the page.

**The ghost layer is a toggle, not a mode.** The header button **[هُوَ]**
(`#taqdirToggle`, `qissa-taqdir`) turns `body.taqdir-mode` on, and every
word whose STORED i'rab line names a ghost grows a dashed pill beside it:
the concealed pronoun the line names (هُوَ / هِيَ / أَنْتَ / أَنَا / نَحْنُ), the
deputy, the estimated كَائِنٌ a jarr phrase hangs on, the dropped mudaf
before the word it left. The pills are in the DOM always and shown only
under the toggle — one CSS rule, no re-render — and they come from
`TaqdirEngine.fromLine`, a regex over the human line, never from the
engine: a story renders hundreds of words at once, and the engine's own
ghosts (graded 97.8% against those lines) belong to the sheet and the
lab, where one sentence is analysed. A legend line under the header says
what the dashes mean, in the UI language.

**The Kinaya lab (🪜) has three seed shelves.** The engine's own seeds, the
tibaq seeds, and — new — the chapters' own sentences (مِنَ الْمَتْنِ): a seed
from the corpus is looked up by its bare letters (`KinayaEngine.corpusFrame`)
and its authored frame lends the ladder its rungs, so the lab can show the
far kinaya climbing exactly as the sheet does. The Atlas rings the kinaya
and the tibaq notes now (`ENGINE_OF` → the kinaya lab), and the chip on a
sentence says كِنَايَة or طِبَاق where the authored frame is one.

## 18. Every figure in its own shape, the letters aligned, and the learned layer badged (wave 19)

**A figure of the badiʿ is not a chip — it is a shape.** `badiFrameHtml`
gives each figure its own drawing, and the reader learns to tell them
apart by silhouette before reading a chip: the **tibaq** keeps its two
poles and ⇄; the **muqabala** is two rows with a ⇅ tie under each
counterpart, so «laugh a little / weep much» reads as two columns; the
**laff wa-nashr** is the same two rows with ⇣ ties — and when the spread
runs backwards (Ibn Hayyus: dune, bough, gazelle / glance, figure, haunch)
the ties turn to crossed ⤨ in the danger colour, so «unordered» is seen,
not announced; **muraʿat al-nazir** is a set on one row under a dashed
field label (أَجْرَامُ السَّمَاءِ · the sky), and the **iham al-tanasub** is the
same set with the borrowed member dashed in the accent, its two senses
listed under it (الْمُرَادُ / الْمَعْنَى الْآخَرُ); **tashabuh al-atraf** is a
column of arcs — each closing epithet on the accent ground with ⟵ back to
the clause it answers, numbered in order; the **irsad** is the forecaster
in a dotted border, ⋯⟶, the close on the accent ground; the **mushakala**
shows companion ⟶ word with the word that would have been said hanging
beside it as a dashed ghost (خِيطُوا behind اطْبُخُوا); the **muzawaja** is
two rows, each shart/jaza verb ⟶ its yoke; the **ʿaks** is two rows with ⤭
between them and the two words coloured so the swap is visible; the
**rujuʿ** strikes the retracted word through in the danger colour and lights
بَلَى; the **tawriya** puts the word (and its furnishing companion, dashed)
over two faces, the near sense plain and the far sense — the meant — on the
accent ground; the **istikhdam** chains the word ⟶ its pronouns, each
pronoun pole dashed, the two senses under them. The chip row under every
shape keeps the wave-18 contract (the figure, the sub-kind, the class, the
receipt — table / surface / *the word from the frame, the rest read*), and
the § button opens that figure's own note. A frame the engine did not read
is still drawn, grey, as the chapter's claim; the agree line now counts
(2/2).

**The jinas is drawn letter by letter.** `jinasAlignSvg` lays the two
words in two rows of cells, right to left, a lit cell for a shared letter
with a short link between the rows, a dashed danger cell for the letter
that differs (سَبَإٍ / نَبَإٍ: three lit, one dashed). Nothing is written
that the engine did not compare: the kind chip is what the letters say
(تَامٌّ · مُحَرَّفٌ · مُطَرَّفٌ · مُضَارِعٌ · لَاحِقٌ · قَلْبٌ) and the ishtiqaq what the
roots say, with the root itself as a chip. The panel shows four pairs and
counts the rest — the ishtiqaq is the figure prose lives on, and a
definition sentence can carry six.

**The sajʿ is two clauses with their fawasil ringed.** `sajHtml` prints
the clauses on two lines in the reading face, the last word of each in a
ring on the accent ground, and lifts the rhyme letter out into a dashed
circle at the margin between them (ع for مَرْفُوعَةٌ / مَوْضُوعَةٌ). The chips
give the kind by the fawasil's wazn and the Talkhis's length note (equal
clauses the finest; a longer second allowed; a much shorter second held
ugly).

**Five doors now.** The doors strip gained a fifth: 🔡 لَفْظِيّ, lit when the
sentence carries a jinas other than the plain ishtiqaq or any sajʿ; the
badiʿ door reads ⇄ بَدِيع and lights for any figure of meaning. The chip on
the sentence line names the figure the chapter authored — مُقَابَلَةٌ, إِرْصَادٌ,
عَكْسٌ, تَوْرِيَةٌ — from the same label table the panel uses.

**The Badiʿ lab (✨) and the Learning lab (🧠).** The Badiʿ lab takes any
sentence and shows doors + figures + jinas + sajʿ under it, with four seed
shelves (the figures of meaning, the jinas, the sajʿ, and the chapters'
own sentences, whose authored frames lend the hinted figures their word).
The Learning lab is the one place in the Atolye that is not an exact rule,
and it says so in its first line. Two cards: the **bab of a Form-I root**
— the held-out accuracy, the top-2 and the majority baseline as three stat
pills, a root input whose answer is the same 🧠 badge the Sarf lab shows
when the corpus has no paradigm for a root (two chips: the best bab and
the runner-up with their percentages, and the training size under them);
and the **seats of iʿrab** — a button that trains on this device (half the
stories) and grades on the other half, then prints the exact engine's
accuracy beside the model's, the model's accuracy when ≥85% sure, the
count of seats the rules left undecided that the model would fill, a
per-seat table (rules vs 🧠), and the mined governor→seat rules with their
support and confidence. The badge is the rule of the layer: **wherever a
statistical guess speaks, 🧠 is beside it**, and it never wears the
reading face.

**Four games.** 👻 *The ghost* shows a sentence with one verb marked and
`[؟]` after it, and asks for the concealed pronoun the stored line names;
✨ *Name the figure* shows a Talkhis sentence and asks which figure of the
badiʿ it carries (the distractors are other figures from the same table);
🔡 *Two words, one sound* shows a jinas pair over its sentence and asks the
kind, and the reveal is the letter grid; 🪜 *What is sought?* marks a
kinaya's span and asks sifa / mawsuf / nisba, the reveal naming near or
far. All four ride `runQuiz` and Elo (nahw for the ghost, balagha for the
rest), and the hub cards carry their supply counts like every other game.

## 19. The list figures drawn as shapes, the tajrid that steps out, the mubalagha dial, and a learned shortlist (wave 20)

**A jamʿ is a bracket; a taqsim is arrows; a tafriq is a broken equals.**
The three list figures of chapters 61–62 are the first of the badiʿ whose
whole point is HOW MANY things and HOW MANY rulings, so `badiFrameHtml`
draws the count. The **jamʿ** (الْمَالُ وَالْبَنُونَ زِينَةُ…) sets the gathered
things on one row under a top brace (`.bd-brace`: a rounded top border in
the accent colour, no bottom — the bracket of a tally) and hangs the ONE
ruling beneath it on a ⤵, the ruling pole underlined in the accent
(`.bd-ruling`); the eye reads «two things, one word» before any chip. The
**taqsim** (لِلسَّبْيِ مَا نَكَحُوا وَالْقَتْلِ مَا وَلَدُوا…) reuses the two-row,
tied layout of the laff wa-nashr — the things on the upper row, the
rulings below, a ⇣ under each — because the taqsim IS the laff wa-nashr's
honest cousin (the pairing is written, عَلَى التَّعْيِينِ, not left to the
reader), and the shared silhouette says so. The **tafriq** (مَا نَوَالُ الْغَمَامِ
… كَنَوَالِ الْأَمِيرِ) puts the two annexed phrases either side of a large
accent **≠** (`.bd-neq`); when the two share their head word (نَوَال … نَوَال)
that head is dimmed (`.bd-dim`) on both sides so the difference — the two
annexes — is what stays bright. The **jamʿ with tafriq** in one sentence
(the face and the heart, one fire, two sides) is the brace and the ⤵
ruling, then under it the two things each ⟶ its own side with the ≠
between — the compound is literally the two drawings stacked. The
**compounds across sentences** (a jamʿ then a taqsim in the next sentence,
the three of Hūd 105–108) cannot be drawn on one line, so they are a strip
of double-bordered chips under the frames (`.bd-compounds`: «مُرَكَّب —
جَمْعٌ مَعَ تَقْسِيمٍ · الْجَمْعُ أَوَّلًا · s4 + s5») that the
`BadiEngine.compoundsOf(chapter)` reading produces — every sentence that
takes part in a compound shows the strip, so the reader meets it on either
bayt.

**The tajrid steps out of its own word.** Out of a thing that has a
quality, another like it is drawn — so the drawing is the source pole and,
to its left, the drawn-out pole raised a few pixels and dashed (`.bd-out`:
`translateY(-5px)`, dashed border, the paper colour behind it), with a ⤴
between them and, under the pair, the LETTER that did the drawing (مِنْ,
بِ, فِي) in a dotted pill (`.bd-letter`) — or nothing, for the kind that
uses no letter. صَدِيقٌ stands a step above فُلَانٍ; الْبَحْرَ a step above
بِهِ; دَارُ a step above فِيهَا. The seven ways share one silhouette and
differ only by the pill, which is exactly how the Talkhis lists them.

**The mubalagha is a dial the author sets and a receipt the engine
reads.** Three stops — تَبْلِيغ · إِغْرَاق · غُلُوّ — on one line joined by
short rules (`.bd-dial-stops`, RTL), the authored degree lit (`.bd-stop.on`
on the accent ground) and the others at half opacity; beneath it, when the
engine found one, the RECEIPT of acceptance: the word that carries it
(يَكَادُ, لَوْ, حَتَّى, يُخَيَّلُ, بِالْأَمْسِ) as a pole with a chip naming it. A
one-line note under the dial says plainly that the degree is the author's
judgement of what reason and custom allow and that the engine reads only
the receipt — the honesty of wave 17's «kinds as a shortlist» kept in the
drawing itself.

**The madhhab kalami is a ladder of two rungs and a ∴.** The premise pole
(لَوْ, لَئِنْ, حَلَفْتُ, كَفِعْلِكَ) in the accent border ⟹ the consequence pole
dashed, and a ∴ under them: the shape of an argument, whichever of the
four shapes (the reductio, the oath, the conditional, the analogy) the
engine read.

**A learned shortlist sits above the engine's reading.** In the Badiʿ lab
the `FigurePredictor.badge` — 🧠 and three chips, each a figure's Arabic
name with its probability — appears ABOVE the doors strip and the exact
frames, in the same dashed `learn-badge` box the Sarf lab uses for the
BabModel, so the two learned things look alike and both look unlike a
rule: the badge's meta line names the training size and the held-out
top-3 rate, and the Learning lab gets a third card (top-3 hit, P, R, F1,
held out BY CHAPTER) beside the bab model and the seat model. The engine's
frames below it are still the claim; the shortlist is where to look.

**Three more games, one shape each.** «Hand each its own» (gTaqsim) shows
a taqsim's thing ⇣ ؟ and offers the sentence's rulings; «Which two part
ways?» (gTafriq) offers four «A ≠ B» pairs of the sentence's own words;
«How far is too far?» (gMubalagha) offers the three stops of the dial and
reveals the receipt. All three draw from the authored frames, so a wrong
answer is corrected by the chapter's own analysis, and each card carries
its § to the note.

## 20. The cause-arrow, the exception hinge, the question mark, and the name-chain (wave 21)

**A claimed cause is an arrow pointing backwards.** The ḥusn al-taʿlīl of
chapter 65 says «this quality — because of THAT», and the poet's «that» is
never the real cause, so the card (`.bd-talil`) draws the QUALITY as a
dashed pole (`.bd-quality`, the thing that was already there), a large
accent ⇐ (`.bd-because`), and the CLAIMED CAUSE as the accent-underlined
pole (`.bd-cause`) — the eye reads the arrow the wrong way round on
purpose, because that is what the figure does. Under the arrow two chips:
the kind (fixed / unfixed, possible / impossible, on doubt) and, dotted
(`.bd-rcpt`), the RECEIPT the cause rides on (بِإِنَّمَا, بِلَكِنْ, بِلَوْ,
بِكَأَنَّ, or a fresh sentence). A one-line note says the kind is the
author's judgement and the engine reads the receipt and the cause-word —
the wave-17 honesty, kept on the card. The **tafrīʿ** (`.bd-tafri`) is two
predications one above the other — subject and accent-underlined predicate
(`.bd-pred`) — with the كَمَا hinge between them on ⤷ … ⤶ (`.bd-hinge`):
one ruling, branched.

**An exception is a hinge, and the hinge is coloured by what it confirms.**
Taʾkīd al-madḥ and its mirror (chapter 66) live in the reader's
expectation — the adat promises a fault and hands over a praise — so the
card (`.bd-takid`) sets the first clause, the adat underlined in the
accent (`.bd-hinge-adat`), and the excepted clause on ONE line, with the
poles bordered green for praise (`.bd-praise`) or red for blame
(`.bd-blame`), and the negation that opens the first kind dimmed at the
front. The sub chip names the kind (a praise excepted from a denied blame;
a praise, then the adat and another; مَا … إِلَّا أَنْ) and the dotted chip
the adat (بِغَيْرَ أَنَّ, بِبَيْدَ أَنَّ, بِسِوَى, بِلَكِنَّ, بِإِلَّا). When the frame is
missing and only the shape was read, a note says the polarity is unread.

**A feigned question wears its own mark.** Tajāhul al-ʿārif (`.bd-tajahul`)
puts the question word as the cause-style pole, a large Arabic ؟ (`.bd-q`)
in the accent, and the partner (the أَمْ, the كَأَنَّ) as the dashed pole;
the chips give the AIM (reproach, hyperbole in praise or blame,
bewilderment in love — the author's) and the SHAPE the engine read (the
hamza with أَمْ, a bare أَمْ, لَيْتَ, مَا أَدْرِي, كَأَنَّ). Al-qawl bil-mūjib is
the other's word on the left, ↩, and the same word turned on the right.

**Names run on a chain.** The iṭṭirād (`.bd-ittirad`) is the praised man
and his fathers as accent-underlined poles joined by small grey بْنِ
(`.bd-ibn`) — one unbroken run, exactly as the bayt carries them. Tawjīh
(⇆ on either side of the two-faced word), the jest that means earnest,
istitbāʿ (the spoken praise ⇒ the entailed one) and idmāj (the folded word
alone) are DOC cards: the pole is lit and a note says the frame is the
author's and the engine reads nothing — the figures of meaning are shown,
never claimed.

**Three more games.** «Why does the cloud rain?» marks the quality and asks
for the word that carries the claimed cause (four tokens of the sentence);
«Praise, or blame?» marks the adat and asks what it confirms and how (the
five kinds, polarity in the label); «The knower feigns» marks the question
and asks for its point. Each reveals the frame with its receipt and opens
the note, as the wave-20 games do.

## 21. The jinas by its seat, and the close brought back (wave 22)

**A jinas is named by WHERE the two words differ, and the card says
where.** Chapters 68–69 of the Talkhīṣ cut the jinas by four questions —
one part of speech or two (مُمَاثِل / مُسْتَوْفًى), one word or two (the
jinas of composition: مُتَشَابِه when the script is one, مَفْرُوق when it
parts them), the same letters differently vowelled (مُحَرَّف), one letter
more (نَاقِص: at the front, in the middle, at the end — مُطَرَّف — or two
letters and more, مُذَيَّل), one letter other (مُضَارِع when the two letters
are neighbours in the mouth, لَاحِق when they are not, each at the front,
the middle or the end), the letters in another order (قَلْب: the whole, a
part, or winged at the two ends of a line), and the two mulḥaqs
(derivation, and its look-alike). The wave-19 alignment SVG already drew
the two words letter against letter; wave 22 adds the POSITION chip
(`.ts-shape-chip`, after the kind chip) that names the seat the engine
found — فِي الْأَوَّلِ / فِي الْوَسَطِ / فِي الْآخِرِ, مُمَاثِل / مُسْتَوْفًى,
مُتَشَابِه / مَفْرُوق, قَلْبُ كُلٍّ / قَلْبُ بَعْضٍ / مُجَنَّح — and the
مُزْدَوِج flag when the two stand side by side. The chip is the engine's
own reading (`JinasEngine.read` computes `kind2` from the aligned
letters), so it never disagrees with the picture above it.

**Radd al-ʿajuz is an arc drawn backwards.** The figure (`.bd-radd`) is
the close of a line brought back upon its head, so the card sets the two
words on ONE row, the head as the accent-underlined pole and the close as
the dashed pole, with a large ↶ between them (`.bd-radd-arc`) that reads
right-to-left as the close does — it points at the word it returns to.
Two chips under the arc: the KIND (the same word twice, the two in jinas,
the mulḥaq by derivation) and the SEAT — in prose «the head and the close
of the fiqra»; in verse the five seats of chapter 70 (the head of the
first hemistich, its middle, its end — the ʿarūḍ — or the head of the
second), which `RaddEngine` estimates from the content-word midpoint and
the authored frame confirms. When the engine's seat neighbours the
authored one (the midpoint is an estimate), the frame still agrees; the
card shows the authored seat.

**One more game.** «The close comes back» marks the ʿajuz and asks for the
earlier word it returns to (four tokens of the line); the reveal names
the kind and the seat and opens the note. «Which jinas?» now reveals the
position chip beside the kind.

## 22. The sajʿ on the author's pauses, and the four figures of the last leaf (wave 23)

**A sajʿ is cut where the author breathes, and the card shows the cut.**
Chapters 71–72 of the Talkhīṣ close the lafẓī badīʿ. The sajʿ engine used
to guess its clauses from the wāw joiners alone; wave 23 lets the AUTHOR cut
them — a `،` or `؛` after a token, or the hemistich `*` — and reads the
finest kinds off the clauses' length: equal (الْمُتَسَاوِي), the second longer
(وَالنَّجْمِ إِذَا هَوَى، مَا ضَلَّ صَاحِبُكُمْ وَمَا غَوَى), the third longer
(خُذُوهُ، فَغُلُّوهُ، ثُمَّ الْجَحِيمَ صَلُّوهُ), and the shorter second the books
refuse. The card (`.bd-saj`) sets the two clauses one under the other with
their fāṣilas accent-underlined, the kind chip (مُطَرَّف / مُتَوَازٍ /
مُرَصَّع) and the length chip (`.ts-shape-chip`) after it, and the wazn
strings the engine counted — a wazn is now the MADD letters only, so
لَفْظِهِ and وَعْظِهِ weigh alike and the murassaʿ holds. A one-word clause
is allowed only where the author marked it (فَغُلُّوهُ), never guessed.

**The tashtir is a bayt folded in two.** `.bd-tashtir` draws the two halves
(`.bd-tashtir-half`) on two rows with the hemistich cut (`.bd-tashtir-cut`)
between them, each half carrying its own sajʿ pair in the row's ink and its
rawī chip — and the two rawīs must differ, or the line is one sajʿ, not
two. **The muwazana is an equals sign** (`.bd-muwazana`, `.bd-eq`): the two
fāṣilas set side by side with their wazns printed beneath, equal in wazn
and NOT in rhyme, and the mumāthala chip when half the words or more of
both clauses answer in wazn. **The qalb of the whole is a mirror**
(`.bd-qalb`): the bare letters of the line in a single row and the same
row reversed under it (`.bd-qalb-mirror`), letter over letter, with the
arrow (`.bd-qalb-arrow`) pointing both ways — the reader sees the
palindrome rather than being told of it. **The tashrīʿ is a stop sign**
(`.bd-tashri`, `.bd-stop`): the first rhyme word is marked as a place the
sense may stop, the second as the line's true close, so the two rhymes
read as two exits from one bayt. **Luzum mā lā yalzam lights one letter**
(`.bd-luzum`, `.bd-luzum-l`): the letter before the rawī is boxed in the
accent on every rhyme word, and the peers chip counts the other bayts of
the chapter that keep the same letter — a luzum is a promise kept across
lines, so the card says how many.

**One more game.** «Which sajʿ?» (gSaj, ≈) marks the two fāṣilas of a
sajʿ from the Talkhīṣ and asks for its kind; the reveal prints the
engine's wazn strings for both fāṣilas, so the learner sees WHY the answer
is mutawāzī and not muṭarraf, and opens the note.

## 23. The khātima: the bayt scanned, the taking traced, the received text lit (wave 24)

**A bayt is shown as it is heard.** Chapters 73–76 of the Talkhīṣ are its
khātima — the poets' takings, the Qurʾān and the hadith woven in, and the
three places a speech must be fine — and every ruling there is argued on
BAYTS. So the sentence card grows a bayt card (`.bd-arud`): the two
hemistichs on two rows, each foot (`.arud-foot`) boxed under the syllables
it covers with its name (فَعُولُنْ، مَفَاعِيلُنْ), the baḥr chip after the
line, the ziḥāf marked lighter where the foot deviated, and the rawī of the
rhyme boxed in the accent (`.aq-rawi`) with the qāfiya's letters (the
waṣl, the ridf, the taʾsīs) named in a row beneath. The ArudEngine scans
free text (the taqṭīʿ from the writing itself: the sukūn/ḥaraka string,
the article's wasl, the tanwīn's nūn, the long vowels), tries the sixteen
metres with their licensed ziḥāfāt and ʿilal, and answers with the cheapest
fit — or with «no metre», which the card prints as plainly as a baḥr; a
prose shaṭr never scans. The ʿArūḍ lab takes any bayt, and gBahr asks the
learner for the baḥr with the feet as the reveal.

**A taking is drawn as two lines with the shared words lit.** The sariqa
card (`.bd-sariqa`) prints the taker's line over the source's line
(`.bd-line`), the shared words highlighted on both (`.bd-shared`), the
arrow «taken from» (`.bd-sariqa-from`) naming the source sentence, and
the chips for the book's own kinds: naskh / ighāra / ilmām (the plain
takings, by how much was taken and whether the words came too), and for
the hidden ones tashābuh / naql / ashmal / qalb / ziyāda, with the grade
chip the book pronounces (mamdūḥ / madhmūm / mithl). The engine measures
what it can — the shared bare words, the shared roots, the metre and rawī
kept — and the book's judgement is a hint the card shows as such.

**The received text is lit inside the sentence.** The iqtibas, tadmin,
ʿaqd, ḥall and talmīḥ cards (`.bd-iqtibas`) mark the words of the Qurʾān,
the hadith or the other poet's bayt in the accent's wash (`.bd-received`),
name the source under it («the received text: النَّحْل ٧٧»), and add a
chip when the words were changed for the metre (تَغْيِيرٌ يَسِيرٌ) or the
tadmin was a whole bayt (istiʿāna) or a hemistich (īdāʿ). The fine
opening, the ill omen, the barāʿat al-istihlāl, the takhalluṣ and the
iqtiḍāb, the fasl al-khitāb and the fine close (ch76) wear the same card:
the received bayt is the frame, and the chip says which of the three
places of care it serves.

**Two notes of another science.** The ʿarūḍ note and the qāfiya note are
the first of a new registry group (`arud`), reached from the badīʿ doors
strip and from every bayt card's baḥr chip.

## 24. The declension triplet: one noun, three cases, read by the engines (wave 25)

**The Kāfiya proves every declension class on one triplet** — جَاءَنِي زَيْدٌ،
وَرَأَيْتُ زَيْدًا، وَمَرَرْتُ بِزَيْدٍ — and the app draws that triplet as a card
(`.bd-triplet`) whenever a sentence carries one noun in three case-forms. Three
cells stand in the order the words come (`.tp-row`, RTL), each with the word
large in the Arabic face (`.tp-word`), the CASE above it in small caps
(`.tp-case`: رَفْع · rafʿ), the SIGN under it in the accent (`.tp-sign`:
الضَّمَّة · damma, or الْوَاو · the waw), and BY WHAT it declines in the soft ink
(`.tp-by`: by the vowel / by the letter). A cell that declines by a LETTER is
drawn with a dashed border — the five nouns, the sound masculine plural, the
dual — so the eye sees at once which class the page is teaching. Nothing on the
card is stored: the case is read off the stored iʿrāb line, the sign off the
word's own ending (`caseSignOf`), the manner off `IrabSign.of`; the note under
the card says so. Same restraint as every card in the sheet: the neutral panel,
the accent for the one fact that matters (the sign), no colour of its own.

## 25. The İ'rab Mağazası: four cells per customer, and Birgivī's tree on the Awāmil card (wave 30)

**The Avâmil lesson teaches iʿrāb as a shop**, and the workshop now has that shop
as a lab (`مَغَازَة` on the rail, `conjState.lab === "irabshop"`). A sentence is
typed or taken from the lesson's own seeds (`SHOP_SEEDS`), and every word walks
out as a CARD (`.shop-card`) of four cells in the lesson's order: MÜŞTERİ — the
word large, and under it its declension class (المُفْرَد · the singular, جَمْعُ
الْمُذَكَّرِ السَّالِمُ…); BEDEN — the body it wears (مَرْفُوعٌ … or فِي مَحَلِّ رَفْعٍ for a
mabni that only tries the dress on); ENDAM — the SIGN in the accent face
(الضَّمَّةُ · الْوَاوُ · حَذْفُ النُّونِ), with الْمُقَدَّرَةُ appended and the OBSTACLE named
in italics when the iʿrāb is assumed (التَّعَذُّرُ · الِاسْتِثْقَالُ · الْمُنَاسَبَةُ); and
ETKİ EDEN — the governor, prefixed by the head word when the Dabt engine named
one (الْمُسْلِمُونَ — الْفِعْلُ), with Birgivī's kind under it (lafẓī samāʿī /
qiyāsī / maʿnawī / by following). The cells are a two-column grid on a phone
and one row of four from 700 px up; the customer cell carries the accent as a
left rule, a letter (no seat at all) or a mabni verb is drawn faded
(`.shop-none`). Above the floor the sentence is written once more as a line
(`.shop-line`) with an underline per word that SAYS the manner: solid for a
spoken iʿrāb, dashed for an assumed one, dotted for a mabni's place, none for a
letter. Under the floor a closed `<details>` legend carries the lesson's three
tables — the ten customers with their three signs, the ten signs by what they
are made of (three vowels, four letters, three omissions), the three obstacles
— so the card is read first and the system second. Nothing on a card is parsed
twice: the seat, the governor and the head come from `DabtEngine.vowel()`'s
verdict, the class from `AlamaEngine.shape` and the five-verbs / weak-final
tests, the diptote's causes from the `MamnuEngine` — and a word the engines left
undecided walks out with no body, never with a guessed one.

**Birgivī's tree** (`.bt-tree`) sits under Jurjānī's seventeen letters on the
Awāmil card: three roots — ٦٠ governors, ٣٠ governed, ١٠ signs — each count a
white numeral on an accent pill (`.bt-n`), the branches indented behind a
hairline, every leaf that the app teaches carrying the § button of its note.
The card ends on a door into the shop (`#avShopOpen`). The figure game
(`gShop`, 🧥) asks only what the corpus itself asserts: a word whose authored
iʿrāb line names its sign AND whose sign the shop derived the same way; the
reveal shows the class and the obstacle, then the author's own line.

## 26. The Inna lab: a card per particle, coloured by the hamza its seat decides (wave 31)

**Birgivī's chapter is a decision, so the workshop shows it as one.** The rail
gained `إِنَّ` (`conjState.lab === "inna"`): a sentence is typed, or one of the
chapter's sixteen seeds taken (`INNA_SEEDS` — Birgivī's own examples in the order
he gives them, from إِنَّ زَيْدًا قَائِمٌ to the ṣila of 28:76), and the sentence is
written back once as a line (`.shop-line`, reused from the Mağaza) where every
إِنَّ-shaped word is underlined in the colour of its verdict — green for the
kasra, amber for the fatḥa, a dashed grey where both readings stand. Under the
line, one CARD per particle (`.inna-card`, the colour as a left rule): the word
large (`.inna-w`), the verdict in the accent face with ✓ / ✗ against the hamza
the typist actually wrote (`.inna-h` — so a learner who types أَنَّ where the seat
wants إِنَّ sees the cross at once), and the SEAT in Arabic with its plain
sentence under it (`.inna-seat`: فِي جَوَابِ الْقَسَمِ — the answer of an oath). A
quoted particle (the chapter's own إِنَّ وَأَنَّ لِلتَّحْقِيقِ) is drawn with no verdict
and the note that its hamza is the author's, not a seat's. A closed legend lists
the ten kasr seats, the fath seats and the two that allow both, each a phrase
in Arabic with the plain sentence beside it, and links the `mawadi-kasr-inna`
and `inna-am-anna` notes. Above the legend a one-line TALLY (`.inna-tally`,
tabular numerals) reports the corpus audit — how many authored particles, how
many a seat decided, how many of those agree with the author — so the lab
never claims more than it measured. **The gInna game** (🔑 on the nahw shelf)
blanks the hamza of a corpus particle (`ـنَّ` in the slot) and asks كَسْرٌ أَمْ
فَتْحٌ؟ with three options — kasra · a sentence, fatḥa · a maṣdar, both; only
particles where the engine's seat agrees with the author's letter are asked,
and the reveal names the seat beside the author's iʿrāb line. Phone first: the
cards are a single column, the line wraps, nothing overflows (gated).

## 27. The reviewer's notes: a flag under the sentence, a ledger on Progress, a file that travels back (wave 32)

**A review is a conversation about one sentence, so it starts there.** When
reviewing is on, the sentence's tool row (`.sent-tools`, after ▶) carries a ⚑
(`.rev-btn`, the play button's size and radius; filled in the accent when the
sentence already has a note). It opens a form UNDER the sentence (`.rev-form`:
a dashed accent border, the panel colour, the UI face), not a sheet — the
reviewer keeps the Arabic in view while writing about it. The form is four
rows: the kind as pill chips (`.rev-kinds`: ✓ correct, harakat, i'rab,
translation, word meaning, spelling, other — the lit one in the accent), the
word (a right-to-left select over the sentence's tokens, "the whole sentence"
first), the problem and the correction (two short textareas, `dir=auto` so a
Turkish note and an Arabic correction each sit on their own side), then Save
beside Remove. Saving fills the flag and closes the form after a beat with
"Saved" — the reviewer moves on, the note stays. **The ledger lives on
Progress** (`.rev-ledger`, under the level rows, a rule above it): the title
with the count, one sentence of instructions, the on/off switch and the name
box on one row, and the actions on the next — Export (.json, the accent
button), Copy as text, Import a file…, Delete my notes (the soft style) — then
the notes as cards (`.rev-note`): the Arabic line first in the reading face, the
kind as a small pill (green for ✓), the word in bold, the problem, the
correction in italics after an arrow, a meta line (story · chapter · Mine /
Imported · name), and two small buttons — Open (jumps to the sentence and opens
its form) and Remove (own notes only). An imported friend's notes sit in the
same list, marked, so the owner triages in one place. **The offline bundle**
is the same reader with `REVIEW_BUILD` on: no switch on Progress (reviewing is
the point), every story open, and a README beside it. Phone first: the chips
wrap, the selects and textareas take the full width, the ledger's rows wrap;
nothing in the form or the ledger needs a hover.

## 28. Paint first: the hub shows before it counts, the labs before they measure (wave 32)

**Nothing the learner taps may wait on the corpus.** The Games hub used to count
every drill's supply before it drew a single card — on a phone that was minutes of
white sheet, read as "the games do not open". Now the hub draws all thirty-four
cards at once; a card whose count is still owed shows a faint «…» in the count slot
(`.g-n.g-wait`, 45% ink) and the numbers land one by one over the next second, a
card greying to «nothing here for this story» only when its count says so. The same
shape for the labs: the model and jumla panels paint their input and their intro at
once with a «…» where the score goes, and the sentence fills in a moment later; the
Inna tally likewise. The second visit of anything is a lookup — the counts, the
scores, the trained weights are remembered per build — so the app FEELS faster
each day it is used, which is the consumer promise: relaxed on the surface, the
whole engine room underneath.

## 29. The fifteen kinds as a checklist, and the book's examples as chips (wave 36)

**A classification is shown whole, never as a verdict.** The Ism lab's new panel lists
all fifteen kinds of the Şerḥu'l-Muġnî in the book's order; the kinds that apply to the
typed word are lit (a 3px accent bar on the start edge, full ink) and carry their
sub-kind and the book's definition under them; the rest stay in the list at 45% ink —
so the learner sees the word against the WHOLE map, and learns what it is not as well
as what it is. The panel is a grid of small rows (Arabic name, then the name in the
app's language) that reads on a phone without scrolling sideways. Under the taṣghīr
and nisba output the book's own examples sit as seed chips (`.qw-seed`, the same chip
the Qawāʿid and Inna labs use): a tap fills the input and derives, and a derivation
cut by a Muġnī rule says so in one line under its rule. The two new game cards —
🔬 Tasgîr/nisbet, 🗂️ the kinds — sit in the sarf row of the hub with the same card,
emblem and count slot as every other drill; their answer cards read the rule or the
definition aloud, in Arabic with the English or Turkish beside it.
