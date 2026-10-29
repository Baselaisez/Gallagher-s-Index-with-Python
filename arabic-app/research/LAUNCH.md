# Qissa — launch handover (v222, build 244)

This is the owner's checklist for taking the app to consumers. Everything the project can do by itself is done and
gated; the items marked **OWNER** need an account, a key or a signature only the owner has.

## 1. What ships

| piece | where | state |
|---|---|---|
| The reader (web / PWA) | `prototype/` — `reader.html`, `sw.js` (cache `qissa-v244`), `manifest.webmanifest`, `icons/`, `privacy.html` | release gates green: validator, i18n, canon, 340 browser checks, PWA checks, drills golden file |
| The hosted copy | `python3 tools/pubsplit.py prototype/reader.html <outdir>` → `reader.html` (3.5 MB) + `data/d1–d3.js` | the artifact at claude.ai is this copy (Version 70) |
| The Android project | `android/` (Capacitor 8, appId `app.qissa.reader`), `capacitor.config.json`, `tools/build_android.py` | the on-demand workflow has built it on a GitHub runner (debug APK + unsigned release APK/AAB, 33.9 MB zipped) |
| Store copy and assets | `research/PLAY_LISTING.md`, `research/store/{en,tr}/01–06.png` (1080×1920), `research/store/feature-graphic-{en,tr}.png` (1024×500) | rendered from the live reader by `tools/store_shots.js` |
| Privacy policy | `prototype/privacy.html` (EN/TR) | packaged into the APK and served beside the reader |
| Review bundle | `dist/qissa-review-v244.zip` (`tools/build_review_bundle.py`) | for reviewers: notes on every sentence, export |

Content: 22 texts in six levels, 43,833 parsed tokens, 328 grammar notes, 13 catechism banks (550 questions),
20 drills, the workshop's engines. Every manifest still says `reviewStatus: pending-scholarly-review` (see §5).

## 2. Run it today (no account needed)

- **Web:** open `prototype/reader.html` from disk, or serve `prototype/` from any static host over HTTPS and it installs
  as a PWA (Chrome: ⋮ → Add to Home screen) and works offline. For a host with a page-size limit, serve the split copy
  from `tools/pubsplit.py` instead (same files plus `data/`).
- **Android, sideload:** run the "Qissa Android" workflow in GitHub Actions (Actions → Qissa Android → Run workflow,
  branch `claude/arabic-app-research-ozd58s`), download the `qissa-android` artifact, install
  `app-debug.apk` on a phone (allow "install from unknown sources"). The debug APK is the full app, unsigned for Play.
- **Android, locally:** `npm install` then `python3 tools/build_android.py --gradle` with the Android SDK and Java 21
  installed; outputs under `android/app/build/outputs/`.

## 2b. A public URL for the web app and the privacy policy (OWNER: one setting)

`.github/workflows/qissa-pages.yml` publishes the hosted copy (the split reader, the PWA shell, `privacy.html`) to
GitHub Pages on demand. Once: Settings → Pages → Source → "GitHub Actions". Then Actions → Qissa Pages → Run
workflow; the run's summary shows the URL. The reader is at `<url>/` (also `/reader.html`), the privacy policy at
`<url>/privacy.html` — paste that into the Play listing. Re-run after every release to update the web app; the
service worker's cache name makes installed PWAs fetch the new build on next open.

## 3. Google Play — the signed build (OWNER)

1. Create the upload key once and keep it out of git:
   ```
   keytool -genkeypair -v -keystore qissa-release.jks -alias qissa -keyalg RSA -keysize 2048 -validity 10000
   base64 -w0 qissa-release.jks > qissa-release.jks.b64
   ```
2. In the repository's Settings → Secrets and variables → Actions, add three secrets:
   `ANDROID_KEYSTORE_B64` (the .b64 file's content), `ANDROID_KEYSTORE_PASSWORD`, `ANDROID_KEY_PASSWORD`.
3. Run the "Qissa Android" workflow once more; the artifact now also holds the **signed** `app-release.aab` and
   `app-release.apk`. Upload the AAB to Play Console (Play requires bundles).
4. Version numbers come from the service worker's cache number (`qissa-v244` → versionCode 244, versionName 0.244);
   `python3 tools/release.py` bumps it on every shippable build, so a Play upload is traceable to the exact reader.

## 4. Google Play — the listing (OWNER, copy from research/PLAY_LISTING.md)

- Developer account (identity verification; for a new personal account Play requires a closed test with at least
  12 testers for 14 days before production — plan it in).
- Store listing: the EN and TR texts, the six screenshots per language, the feature graphic, the icon
  (`prototype/icons/icon-512.png`), category Education.
- Privacy policy URL: publish `prototype/privacy.html` at a stable address (the hosted copy's `privacy.html` is one)
  and paste the URL.
- Data safety: "collects no data"; content rating: Education, everyone (answers in PLAY_LISTING.md).
- Staged roll-out 20 % → 100 % after the closed test.

## 5. Two honesty items before the listing says more than it may

- **Scholarly review.** The analyses are rule-derived and checked against the texts' own parsing; the store text says
  "machine-parsed, under scholarly review" and must keep saying so until a reviewer is named in the manifests
  (`reviewStatus: reviewed`). The review bundle (§1) is the tool for that review.
- **Qiṣaṣ al-Nabiyyīn.** The three Nadwī packages ship flagged «in copyright» (the owner's statement that the rights
  were released could not be confirmed online). Before a production listing, quote a current edition's copyright
  page in the three manifests, or hold those three stories back from the first release (they are premium-flagged;
  `storyLocked()` governs access).

## 6. After launch — how updates go out

- Content and engine work follow `AUTHORING.md` and `CLAUDE.md`'s loop: author → validate → build → smoke → release.
  `python3 tools/release.py` is the one command from edited content to a shippable build (bumps the cache number).
- Web: redeploy `prototype/` (or the split copy); the service worker's cache name makes every reader fetch the new
  build on next open.
- Android: run the workflow, upload the new AAB; the version code follows the cache number automatically.
- Feedback: the review bundle's notes export is the channel for reviewers; the GitHub repository's issues for users.

## 7. Known limits, stated plainly

- Startup on a mid-range phone: the self-contained page parses ~2 s of inline data; the shell and the hosted copy use
  the split page (0.7 s). Measured and gated in the smoke suite.
- Read-aloud is the device's own voices; recorded narration exists only where a chapter ships a file.
- No account and no sync: progress and the deck live on the device (export from the deck as TSV).
- iOS: the web app installs as a PWA from Safari; there is no App Store build yet (Capacitor can add `ios/` on a Mac).
