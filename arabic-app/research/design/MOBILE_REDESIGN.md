# The mobile redesign package (owner's upload, November 2026)

A Claude Design export (`Mobile_app_design_improvement.zip`: `QissaApp.dc.html`, `Qissa Redesign.dc.html`, `Qissa
Prototype.dc.html`, `qissa-data.json`, `support.js`, and an earlier export of the reader it was drawn from). It is a React
prototype of the app on a 390×844 phone frame: three themes × fifteen screens, plus ten screens of features the original
lacked. This file records what it specified and what the reader took from it, so later waves can draw on the rest.

## The three themes (token values, taken verbatim in wave 79)

| token | Mürekkep | Gece | Bahçe |
|---|---|---|---|
| bg / surface / surface-2 | #F3EDE1 / #FBF8F2 / #ECE4D5 | #0E131D / #161D2B / #1F2839 | #F1F4E9 / #FFFFFF / #E6EBDA |
| ink / soft / line | #1E1A16 / #6B6056 / #DED3C0 | #EEE8DA / #9BA3B4 / #283247 | #14251A / #56655A / #D9E0CB |
| accent / on-accent / accent-soft | #A5432B / #FFF8EF / rgba(165,67,43,.10) | #E2B65C / #1B1404 / rgba(226,182,92,.13) | #1F9157 / #FFFFFF / rgba(31,145,87,.12) |
| gold / fire / iʿrāb ink | #B8862F / #C9622A / #8A3A26 | #E2B65C / #F08A4B / #F0C987 | #E5A01A / #F06A36 / #B4472E |
| hero / hero-ink / hero-soft / hero-accent | #2A241F / #F5ECDD / rgba(245,236,221,.16) / #D9A54A | #1D2A45 / #EEE8DA / rgba(238,232,218,.12) / #E2B65C | #1F9157 / #FFFFFF / rgba(255,255,255,.2) / #FFD34D |
| levels 1–4 | #3D7A52 #2D6D8C #B07A1E #A5432B | #6CC3A6 #7FA7F2 #E2B65C #EE8B7B | #1F9157 #2B83C9 #E5A01A #E0533F |
| radius (card / small / button) | 14 / 10 / 12 | 20 / 13 / 16 | 24 / 15 / 18 |
| button shadow | none | 0 8px 22px rgba(226,182,92,.22) | 0 4px 0 #14703F (cards 0 3px 0 #D9E0CB) |
| fonts named | Newsreader + Instrument Sans + Amiri | DM Serif Display + Manrope + Noto Naskh | Bricolage Grotesque + Readex Pro |

The fonts and the Material Symbols icon font are Google-hosted; the reader is self-contained and runs offline and inside
the Android shell, so it keeps its system font stacks and draws the icons as inline SVG (`IconSet`).

## The fifteen screens, and what the reader took

| screen | package | reader (wave) |
|---|---|---|
| Onboarding (welcome, level, daily goal, theme) | 4 steps, dot row, hero tile, one CTA | 3 steps — level (with the hero and three feature lines), goal presets, theme cards (80) |
| Library | date eyebrow, search / streak / avatar, goal ring + XP, hero continue card, level chips, story rows, «add your own text» | goal ring + XP, chips row, hero continue card (79); search and «own text» already exist as the search sheet and the analyzer |
| Reader | back / title / Aa, 3px progress, chapter ornament, numbered sentences, bottom player pill | player pill while Listen runs (80); the rest was already there |
| Word sheet | pos + level pills, gloss big + lemma, Listen + Add to deck, Anlam / Sarf / İʿrab tabs | gloss first in the reader's language (80); tabs and buttons already exist |
| Reading settings (Aa) | mode Easy/Medium/Hard, tashkeel, level lines + legend, translation, size, theme dots, speed | theme dots (79); the rest already exists |
| Deck | flip card with root tiles, four ratings with intervals, done state | not taken — the FSRS deck already grades with four buttons |
| Games hub | daily task, recommended card, 2-column grid by area, lock labels | task card, recommendation, 2 columns on phones (79) |
| In-game | progress bar, hearts, combo, result tiles | not taken yet (the games keep their own result screens) |
| Atölye · Sarf / Çözümle / Gramer / Model | verb chips, conjugation card, root finder, topic sheet, the «Model» tab (toggle the evidence, watch the belief) | the Model tab is wave 81's brief; the rest exists as the workshop's labs |
| Progress | streak hero + week dots + mercy line, three tiles, weekly XP bars, level path, badges | all taken (79) |
| Tab bar | five tabs, filled icon on a pill when active, badge on the deck | taken (79) |
| Search | suggestion chips, results grouped words / stories / topics | partly there (wave 74); chips not taken |
| New: hard mode (tap a sentence for its translation), spot-the-error, find-the-root, find-the-form, listen-and-pick, phrase → Turkish, 60-second round | | the reader has these as games already (Spot, Kök in the workshop, Sarf drill, Ibāra → TR); the 60-second round and listen-and-pick are open ideas |

## Its performance notes

Icon font subset to the 57 glyphs used; font weights trimmed; the data file preloaded and cached once; no blurred tab
bar; transitions on colour and transform only; the reader highlights word by word while listening and, with no Arabic
voice, runs the same highlight on a timer. The reader already does the word highlight from the synthesis boundary events;
the timer fallback is an open idea.
