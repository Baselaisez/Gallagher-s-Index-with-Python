# Qissa on Google Play — packaging, launch and revenue strategy

*Written at v214 (October 2026). A working document: decisions marked **DECIDE** are the owner's; everything else is the plan the next waves execute.*

## 0. Where the app stands

- One self-contained web app: `prototype/reader.html` (~26 MB: 22 packages, 7,900+ Iẓhār tokens alone, 284 grammar notes, the engines), a service worker (`sw.js`, cache `qissa-v2xx`) and a web manifest — already an installable PWA.
- Content status: every manifest carries `reviewStatus: pending-scholarly-review`. Nothing the store build says about Arabic grammar may go out as "reviewed" until a scholar signs it off (§5).
- Engines: DabtEngine (iʿrāb of every word, 100.0 on all 66 Iẓhār chapters at v214, corpus sweep WORSE 0), Sarf (35 doors), İzzî, Maqṣūd, Hadhf, Nida, Jam, Mamnu, Sign, Tartib, Tashbih/Majaz/Kinaya/Badi, the games factory (14 games per story), the labs and the Atlas.

## 1. Finish the shelf first (the owner's stated order)

The store build ships only what is finished and reviewed. Remaining work, in the order the coverage audit (`research/COVERAGE.md`) already ranks it:

1. **Stories still to author from the sources on the shelf**
   - `kafiya-ibn-hajib-sual-cevap.txt` — the full Kāfiya matn: **done at v216** (46 chapters, 8,157 tokens, the notebook consumed to its end). Left on the page: the ~115-question review index, a catechism-quiz bank for a later wave.
   - `aqaid-nasafi-matn-full.txt` — the ʿAqāʾid of al-Nasafī: **done at v217** (aqaid-ahl-al-sunna ch25–46, the matn consumed to its end).
   - `wasiyya-samti-arabic.txt`, `emali-qasida-ottoman.txt` — verify the authored packages against these transcriptions cover to cover (the Amālī has 14 chapters; check the qaṣīda's full bayt count).
   - `qatr-al-nada-turkish-cicek.txt` — Qaṭr al-Nadā as a story (its rules are consumed; its matn is not).
   - `molla-cami-sual-cevap.txt` (Molla Jāmī on the Kāfiya) — Ottoman script; transliterate as the Iẓhār was, then author as commentary chapters beside the Kāfiya.
2. **Automations still owed to the engines** (the audit's top ten): the ʿalaqa engine fed by the 70-question bank, مَا's twelve faces as a disambiguator, the taʿalluq rule, the iʿlāl chains of the derived nouns, the catechism quiz game from the ~150 transcribed Q&A (**done at v217**: seven banks, 202 items, gCatechism + the Sual-Cevap lab), the ʿawāmil kinds 2–13 (blocked on the Jurjānī deck pages).
3. **OOP consolidation** — every engine is already a static class; the store wave adds a thin `Lesson` object model (story → chapter → sentence → token → verdicts) so the games, labs and the Atlas read one typed interface instead of the STORIES array directly, and the sync layer (§3) serialises the same model.

## 2. Packaging: how the APK is built, and why it is fast

**Decision: Capacitor (Android), not a Trusted Web Activity.** A TWA needs the site hosted at a public HTTPS origin with asset links and loads over the network; Capacitor ships the files inside the APK, works fully offline on first launch (students in a madrasah dorm have no guaranteed network), and still runs in the device's Chromium WebView — the engines run exactly as in the browser.

Build pipeline (new tool `tools/build_android.py`, wave 61):
1. `tools/pubsplit.py` already splits the 26 MB page into `reader.html` + `data/d1–d3.js`; the Android build uses the same split so the WebView parses the HTML quickly and streams the data files.
2. The split goes into `android/app/src/main/assets/public/`, Capacitor's `capacitor.config.json` points `webDir` there, `server.androidScheme = "https"` (needed for the service worker and IndexedDB), and the Android project is generated once and committed (`android/`).
3. Startup speed, measured in the smoke suite (new gate): the library must paint within 1.5 s on a mid-range device profile (Chromium's CPU throttle ×4). The known costs to remove before release: the games-hub build on the full Iẓhār (~3 s, make it lazy per card) and the game factory's audit (11 s, test-only — keep it out of the app path).
4. The JSON content stays inside the bundle (no server); the service worker is kept for the web build, and on Android the same precache list is simply the asset list.
5. Output: a signed **AAB** for Play (Play requires bundles) and a universal **APK** for direct install; both from `./gradlew bundleRelease assembleRelease` with a keystore kept out of git (`android/keystore.properties` ignored; the owner holds the key).
6. Play's requirements as of 2026: target API 35, 64-bit (the WebView app has no native code, so automatic), a privacy policy URL, the Data-safety form (no data collected unless the sync layer ships), content rating questionnaire (Education, no user-generated content), and for a **new personal developer account a closed test with 12 testers for 14 days before production** — plan this into the calendar.

Size: the AAB will be ~30 MB; Play's limit is 200 MB for the base module, no asset-pack needed.

## 3. Product shape for the store (what is free, what is paid)

**DECIDE — recommended: freemium with a one-time "whole library" unlock, no ads, no tracking.**

- Free forever: the beginner tier (the Prophets' stories part one, the short texts, the first chapters of every matn), all engines on those texts, the drills.
- One-time purchase (Play Billing, "Kütüphane / The Library", suggested 14.99 USD / 299 TRY, regional pricing on): every text, every chapter, the labs' full data, future texts included. Classical-text learners (madrasah students, imams, seminary students) distrust subscriptions; a lifetime key sells.
- Optional later subscription ("Hoca", monthly): the sync layer (progress across devices), teacher dashboards for a class, and the scholarly-review badge updates. Only after the one-time tier has paying users.
- Institutions: a volume licence (madrasas, Qur'an schools, universities with Arabic departments) sold outside Play — invoice, a licence file the app reads. This is the revenue line that can actually pay for scholarly review.
- Never: ads (they break the reading surface and the trust of this audience), selling data.

## 4. Launch sequence

1. **v215–v218 — finish the shelf** (§1) so the library claim is true: "the Iẓhār and the Kāfiya complete, with every word parsed".
2. **v219 — the Android build** (§2) with the startup gate; internal testing track.
3. **Closed test (14 days, ≥12 testers):** recruit from the two audiences the app already serves — Turkish medrese students (the Turkish layer is complete) and English-speaking classical-Arabic learners (the Western "Madinah books"/Qaṣīda audience). In-app feedback sheet (one tap from every page: "this iʿrāb is wrong / this translation is off") that files to a GitHub issue with the story, chapter, sentence and token ids — the same ids the engines use, so a report is reproducible by `tools/` without a conversation.
4. **Scholarly review (§5)** runs during the closed test; the production listing says exactly what has been reviewed.
5. **Production:** staged roll-out 20 % → 100 %, review prompts only after a completed chapter.

## 5. Trust: the review status and the licence status

- `reviewStatus: pending-scholarly-review` on every package must become `reviewed` (reviewer named in the manifest) before the listing may say "verified". Until then the store text says "machine-parsed, under scholarly review" — honest and still a strong claim.
- **Licensing — a blocker to clear before upload:** the classical matns (Iẓhār, Kāfiya, Talkhīṣ, the Waṣiyyas, the Amālī, Nasafī) are public domain. **Qiṣaṣ al-Nabiyyīn (Abū l-Ḥasan ʿAlī al-Nadwī, d. 1999)** — the three packages (107 chapters) are marked «in copyright» in their manifests (`research/COVERAGE.md` row 40). The owner states that Nadwī released the printing rights to all Muslims and that any publisher may print the book anywhere, even simultaneously. A web check at v215 did not confirm a waiver: the scans in circulation are tagged by their uploaders (CC BY-NC-ND and the like, which an uploader cannot grant), one bookseller claims reserved rights, and the Muʾassasat al-Risāla editions carry ordinary imprints. **What settles it:** the copyright page (ḥuqūq al-ṭabʿ) of a current edition — if it reads «ḥuqūq al-ṭabʿ li-kull muslim» or the equivalent, quote it verbatim in the three manifests' attribution and drop the RIGHTS lines; if it reads «maḥfūẓa», the packages cannot ship in a paid build without a licence from the rights holder (the Nadwa / Dār Ibn Kathīr). Until that page is seen, nothing changes in the manifests. **DECIDE:** send the copyright page of the edition the scans were made from; fallback — ship the store build without those packages and keep them in the free web prototype.

## 6. "Best classical Arabic teaching app" — what makes it defensible

The moat is not the texts (anyone can scan a matn) but the engines: an iʿrāb on every word that is derived, graded against the books' own readings, and explained by the rules it fired — with games, drills and labs generated from the same verdicts. The store listing, the screenshots and the first-run tour should show exactly that: tap a word → its iʿrāb, the governor, the rule, the matn note, the game built from this sentence.

Measured claims to put on the listing once reviewed: the number of parsed words, the number of texts, the per-chapter grading floors the release gates enforce, and the agreement figures the smoke suite prints.

## 7. What the next wave does (actionable now)

- ~~Wave 61~~ **DONE in wave 69 (v220)**: `tools/build_android.py`, the committed `android/` Capacitor 8 project, the startup gate (×4 CPU, fresh profile) and the on-demand `qissa-android.yml` workflow that builds the debug APK and, with the keystore secrets, the signed AAB/APK. The lazy hub had already landed (wave 32p). Still the owner's: the keystore (three commands in the tool's docstring), the three repository secrets `ANDROID_KEYSTORE_B64` / `ANDROID_KEYSTORE_PASSWORD` / `ANDROID_KEY_PASSWORD`, then run the workflow once and sideload the debug APK.
- Wave 62–65: the Kāfiya full matn, then the Nasafī creed, then Qaṭr al-Nadā — each with its engine round, sweep and gates as before.
- In parallel (owner): Play developer account, the keystore, the privacy policy page (one static page on the GitHub Pages site), the decision on the Qiṣaṣ licence, and a shortlist of two scholars for the review.
