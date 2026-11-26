# Design audit — 2026-11-27 (v351-O)

Screens: the door, the shelf, a story page, the word sheet's tabs (Neden? open and closed), the tarkib (sentence) sheet,
the player bar and the voice sheet, the games hub and a round with feedback, the labs hub and three labs (Jumla, Khilāf,
Ṣarf), a grammar note with «Neden böyle?» and its العلّة cards, Settings, the teacher's review — at 390×844 and 360×740,
in Mürekkep, Gece and İznik, in TR and EN (240 screenshots). Each screen measured by script (`scratchpad/guide351/audit.js`):
elements wider than the viewport, controls under 44 px (v320's rule: an invisible 44 px hit area counts), text under 4.5:1
(3:1 for large text; the v320 measure), Arabic boxes whose content overflows a clipping box, Arabic lines with a line-height
under 1.45 em, an English string in TR or the reverse, «undefined» on screen, layout shift after a real tap. Then read by eye.

Ranked by how much a learner feels it. **Done** = fixed in v351-O (tokens only, nothing removed, no behaviour change).

| # | What is wrong (by name) | Where | Status |
|---|---|---|---|
| 1 | A word printed as «undefined» (TR has no `gGroupVocab`: the first shelf of the games hub is headed «UNDEFINED») | games hub, TR, every theme | **Done** («Kelimeler») |
| 2 | Arabic at 0.7 rem (11 px) — the tarkib sheet's word column prints each word too small to read its harakat | tarkib sheet, everywhere | **Done** (reading face, 1.15 rem, the box holds its vowels) |
| 3 | Targets under 44 px on controls used every session: the back link of every sheet («← Oyunlar», «← Tüm gramer konuları», 15 px tall), the chapter pills (24 px), the root chip (27 px), the tarkib words (14 px), the Khilāf and Ṣarf labs' chips (23 px), the notes' «Kitapların kendi sözleri» row (32 px), the Settings switches (34 px), the Jumla lab's ↗ (26 px) | story page, every sheet, labs, notes, Settings | **Done** (v320's invisible hit area where a row would grow; the row itself where the sheet has room) |
| 4 | Contrast under 4.5:1 in İznik: the «Bu hafta ücretsiz» chip on every free shelf card (3.2:1, the level-3 gold as text), the model's chip (3.2:1), ✓ / ✗ marks and scores of the Jumla lab and the tarkib checks (4.3), a note's common mistakes (4.3) | door, shelf, Jumla lab, tarkib sheet, notes | **Done** (İznik `--ok`/`--danger` one step darker, same hue; the gold mixed toward the ink) |
| 5 | A token that does not exist: `--muted` is used by 50 rules and defined nowhere — every «quiet» label (counts, sources, sub-lines) printed in full ink, so those blocks had no hierarchy; the one with a fallback put #666 on Gece's navy (2.9:1) | notes, labs, khilāf lists, many | **Done** (`--muted` = the theme's soft ink) |
| 6 | Two kinds of sheet header: most sheets open with a title (h3), the games hub and the tarkib sheet with a lone «tab» pill — the tarkib one wraps «تَرْكِيبُ الْجُمْلَة Terkib — cümle kelime kelime» onto two cramped lines inside a pill | games hub, tarkib sheet | **Done** (a lone tab is set as the title) |
| 7 | Two type families competing inside a sheet: interface text set in the reading serif — the governor card («Cümlede âmili», its chips and line), the lab heads («Sarf», «Basra and Kufa», their chips), the labs' search fields and menus, the khilāf rows' chips | word sheet iʿrāb tab, every lab | **Done** (UI face; the serif stays for the text, translations and note titles) |
| 8 | The word sheet's iʿrāb tab has grown block by block: gaps of 8 / 14 / 8 / 8 / 12 / 16 / 8 / 10 px between its parts and three styles of section head (bold serif h4, 600 sans, caps eyebrow) | word sheet, iʿrāb tab | **Done** (the line, its translation, mark and «Neden?» close together; each later section one `--s5` step apart; one head style) |
| 9 | Radii drifting from the tokens: 22 rules with a literal 10 px beside the 12 px `--r-md` cards (governor cards, words, lab tiles, many chips) | across the CSS | **Done** (→ `--r-md`) |
| 10 | A wrapping segmented row drawn as a pill: the Ṣarf lab's bāb numerals and verb rows wrap to 2–3 lines inside a full-radius capsule | Ṣarf lab | **Done** (card corners when it wraps) |
| 11 | The door's title at 360 px («Kütüphane», 162 px at 2.1 rem) ran 6 px under the search button | door, 360 px, TR | **Done** (`min(2.1rem, 8.9vw)`) |
| 12 | At 360 px «Bugünün dersi» is cut to «Bugünün de…» by the three stat chips in the card's head | door, 360 px, TR | Left (the head's chips are v340's pinned layout) |
| 13 | Arabic display lines with a tight line-height that collide when they wrap: a story's title (1.35, wraps on long titles), the rule-of-the-day line on the door (1.25), the Jumla lab's word grid (1.25) | story header, door, Jumla lab | Left (raising the story title's line-height moves the first sentence; wave 72 pins it) |
| 14 | Settings mixes control styles: theme cards, a full-width bar that reads «Kapalı» for the review switch, a full-width button for the voice | Settings | Partly (the switches reach 44 px); a real switch look is left |
| 15 | A game round's «next» and «open the word» sit under the thumb bar until the feedback is scrolled | game round, 390 px | Left (not measured precisely; the sheet scrolls to them) |

Measured and found clean (no fix needed): no element wider than the viewport on any audited screen at 360 or 390 px, in any
theme or language; no Arabic box that clips its harakat (every Arabic box with overflow hidden holds its content); no
English string in TR or Turkish in EN beyond names (the lab name «İ'rab Shop», the second-language gloss under a word, the
theme name «İznik»); after a real tap (story, word, sheet close, games, library, Settings, Atölye) no layout shift arrives
late (0 shifts outside the 500 ms input window). The audit's own shift numbers for programmatic opens are not learner shifts.
