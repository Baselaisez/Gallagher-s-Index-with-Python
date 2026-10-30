# Qissa — Google Play listing (draft, wave 71)

Everything below is ready to paste into Play Console. Claims are limited to what the build actually does; the
"machine-parsed, under scholarly review" wording is deliberate (APP_STORE_STRATEGY §5) and must stay until a scholar
signs the manifests. Owner's items are marked **OWNER**.

## Identity

| field | value |
|---|---|
| App name | Qissa — Classical Arabic Reader |
| Package | `app.qissa.reader` |
| Category | Education |
| Tags | Arabic, grammar, reading, Islamic texts, language learning |
| Privacy policy URL | `prototype/privacy.html` served from the hosted copy (**OWNER**: the public URL) |
| Contact email | **OWNER** |
| Default language | en-US; tr-TR listing translated below |
| Icon | `prototype/icons/icon-512.png` (512 × 512, the same drawing as the launcher) |
| Feature graphic | `research/store/feature-graphic-{en,tr}.png` (1024 × 500, wave 73, `tools/store_shots.js`) |
| Screenshots | `research/store/{en,tr}/01–06.png` (1080 × 1920, wave 73): the shelf, a story, a word sheet, the tarkīb sheet, the games hub, the workshop — rendered from the live reader by `tools/store_shots.js`; re-run after a design wave |

## Short description (80 chars)

EN: `Read classical Arabic texts with madrasah grammar on every word. Offline.`
TR: `Klasik Arapça metinleri her kelimede medrese grameriyle okuyun. Çevrimdışı.`

## Full description (EN)

Qissa is a graded reader for classical Arabic. Tap any word and the app shows its meaning, its root and scale, its
case ending and why it carries it, and the grammar note that teaches the rule — in English or Turkish.

What's inside
• Twenty-two texts in six levels: the Prophets' stories for beginners; the Waṣiyya of Abū Ḥanīfa, the Nasafī creed,
  Mukhtaṣar al-Manār and Kitāb al-Sulḥ in the middle; the Iẓhār al-Asrār, the Kāfiya, the Talkhīṣ al-Miftāḥ and the
  Amālī qasida complete at the top.
• Every word parsed: the madrasah iʿrāb, written out as a student would write it, with the Kāfiya's sign taxonomy,
  the governor that produced the case, and the clause-level iʿrāb of Ibn Hishām.
• The Workshop: a live conjugator through all thirty-five sarf doors, the iʿlāl rules step by step, the root finder,
  the scale, the numbers engine, the vocative, the pause, the twelve faces of mā, the governors of Jurjānī and
  Birgivī — exact where the rules are exact, a ranked shortlist where the books themselves disagree.
• Twenty drills built from the texts you are reading, with wrong answers that are refuted by name.
• Question-and-answer banks from the classical teaching sheets — 550 questions, each anchored to the line of the
  text that answers it — and a flashcard deck with modern spaced repetition.
• Entirely offline. No account, no ads, no tracking.

Honesty note
The analyses are produced by rule engines and checked against the texts' own parsing; a scholarly review is in
progress and the app says so on every text. Where an engine cannot decide, it says that too.

## Full description (TR)

Qissa, klasik Arapça için seviyeli bir okuma uygulamasıdır. Herhangi bir kelimeye dokunun: anlamı, kökü ve vezni,
irabı ve o irabı neden aldığı, kuralı öğreten gramer notu — Türkçe ya da İngilizce.

İçinde ne var
• Altı seviyede yirmi iki metin: başlangıç için Peygamber kıssaları; ortada Ebû Hanîfe'nin Vasiyyeti, Nesefî
  Akaidi, Muhtasaru'l-Menâr ve Kitâbü's-Sulh; en üstte İzhâru'l-Esrâr, Kâfiye, Telhîsu'l-Miftâh ve Emâlî kasidesi —
  eksiksiz.
• Her kelime tahlil edilmiş: bir talebenin yazacağı gibi yazılmış medrese irabı, Kâfiye'nin alâmet taksimi, irabı
  veren âmil ve İbn Hişâm'ın cümle irabı.
• Atölye: otuz beş sarf babının tamamında canlı bir tasrif, adım adım i'lâl kaideleri, kök bulucu, mîzan, sayı
  motoru, nidâ, vakıf, mâ'nın on iki vechi, Cürcânî ve Birgivî'nin âmilleri — kaidenin kesin olduğu yerde kesin,
  kitapların ihtilâf ettiği yerde sıralı bir kısa liste.
• Okuduğunuz metinlerden kurulan yirmi alıştırma; yanlış şıklar ismen çürütülür.
• Klasik ders sayfalarından soru-cevap bankaları — her biri cevabını veren metin satırına bağlı 550 soru — ve
  modern aralıklı tekrarlı bir kelime kartı destesi.
• Tamamen çevrimdışı. Hesap yok, reklam yok, izleme yok.

Dürüstlük notu
Tahliller kural motorlarınca üretilir ve metinlerin kendi irabıyla karşılaştırılır; ilmî inceleme sürmektedir ve
uygulama bunu her metinde belirtir. Bir motorun karar veremediği yerde bunu da söyler.

## Data safety form (answers)

- Does the app collect or share any of the required user data types? **No.**
- Is all user data encrypted in transit? Not applicable — no data leaves the device.
- Do you provide a way for users to request deletion? Not applicable — clearing the app's storage deletes everything;
  the privacy page says so.
- Third-party SDKs: none (Capacitor core only; no plugins, no analytics, no ads SDK).

## Content rating questionnaire (IARC)

Education app; no user-generated content, no social features, no purchases in the first build, no violence/sexual
content/profanity; religious texts present (classical Islamic creed and law — informational, non-proselytising
reading material). Expected rating: Everyone / PEGI 3.

## Target audience and content

Not designed for children; audience 13+. No ads. The texts are classical Islamic scholarship; the listing may be
shown in the Education category without an "Islamic" tag if the owner prefers.

## Before the first upload (OWNER)

1. Play developer account; identity verification; for a new personal account the closed test (≥ 12 testers, 14 days).
2. The keystore and the three repository secrets (`ANDROID_KEYSTORE_B64`, `ANDROID_KEYSTORE_PASSWORD`,
   `ANDROID_KEY_PASSWORD`); run the "Qissa Android" workflow once; upload the AAB from its artifact.
3. Decide the Qiṣaṣ al-Nabiyyīn licence question (COVERAGE row 40) — the three packages ship flagged «in copyright»
   until a current edition's copyright page is quoted in the manifests.
4. Publish `privacy.html` at a stable URL and paste it into the listing.
