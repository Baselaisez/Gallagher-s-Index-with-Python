# AI pre-check of the critical findings — the verifier's brief

The owner (the reviewing hoca) asked for one verification-and-correction pass over all 1,297 critical findings of the
AI pre-review before the students see them. The earlier review was the same model, so **do not agree with it by
default**: read the sentence yourself, find the rule in the books, and decide.

## Inputs
- `review/ai-precheck/packets/<batch>.json` — your findings. Each has the word, its current line (`current`), the earlier
  suggestion (`suggested`) and reason, the token's whole current iʿrāb (`irab_now`: ar/en/tr), and the sentence:
  every token as `index<TAB>word<TAB>iʿrāb line`, plus its EN/TR translation. `issue_type`/`field` say what is
  being judged (`irab.ar` = the Arabic iʿrāb line; `surface` = the vowelling of the word; `translation.*`, …).
- The books: `research/sources/*.txt` (index and provenance in `research/sources/README.md`). The naḥw shelf:
  `izhar-full-corrected.txt`, `izhar-al-asrar-matn-lithograph.txt`, `izhar-tercume-full.txt`, `izhar-amil-mamul-irab.txt`,
  `kafiya-ibn-hajib-sual-cevap.txt`, `kafiya-internet-digest.txt`, `nahiv-kafiye-ozeti-turkce.txt`,
  `molla-cami-sual-cevap.txt`, `serhul-mugni-ders-notlari-kisa-1.txt` (Mughnī lessons — the fāʾ, the wāw, mā …),
  `qawaid-al-irab-turkish.txt`, `qatr-al-nada-turkish-cicek.txt`, `mensubat.txt`, `irab-taksimat-turkish.txt`,
  `avamil-dersi-servet-hayma-2023.txt`, `shudhur-al-dhahab-src.txt`; the ṣarf shelf: `maqsud-sarf.txt`,
  `maksut-sarf-ottoman.txt`, `marah-al-arwah-matn.txt`, `tasrif-al-izzi-src.txt`, `izzi-sarf-grafikleri.txt`,
  `ilal-kaideleri-turkce.txt`, `ilal-misal-ecvef-naqis.txt`, `sarf-35-bab-tablosu.txt`; balāgha:
  `talkhis-al-miftah-balagha.txt`, `alaqat-al-majaz-balagha.txt`, `alaka-ilm-bayan.txt`. Search with Grep (Arabic is
  stored with or without harakat — try both, and the Turkish term too: «naib-i fail», «cevab-ı emmâ», «hâl» …).

## Verdict per finding (one JSON line each in `review/ai-precheck/verdicts/<batch>.jsonl`)
```json
{"id": "QR-…", "verdict": "AI-ONAY|AI-RET|AI-ŞÜPHELİ",
 "corrected": {"ar": "…", "en": "…", "tr": "…"},
 "source": {"book": "Iẓhār al-Asrār (Birgivî)", "file": "research/sources/izhar-full-corrected.txt",
            "locator": "bāb al-fāʿil / line 1234", "quote": "<copied VERBATIM from the file>"},
 "note_tr": "kısa gerekçe (Türkçe)", "note_en": "short reason"}
```
- **AI-ONAY** — the current value IS wrong. `corrected` is the right value (your own — it may differ from the
  earlier suggestion). For an iʿrāb field give all three lines (ar, en, tr) in the house style of the neighbouring
  lines, so the token stays trilingual and consistent; for `surface` give `{"value": "<vowelled word>"}`; for a
  translation give `{"value": "…"}`. **A source is mandatory**: the book, a locator (chapter/bāb and the line number
  in the file), and a short quote of the RULE copied character for character from that file (12–200 characters).
  `python3 tools/precheck.py check <batch>` looks the quote up in the file; a quote it cannot find turns the
  verdict into AI-ŞÜPHELİ. No citation → not ONAY.
- **AI-RET** — the current value is right and the finding is a false alarm. Say why in `note_tr`; a citation is
  welcome but not required.
- **AI-ŞÜPHELİ** — the books in the repo do not settle it, the grammarians differ, or the case needs the hoca.
  Say exactly what is open.

## Rules
- Read the whole sentence before judging a word; the governor may be several words away. Respect the package's
  deliberate readings (the provenance paragraph of its manifest).
- Do not edit any content file. Write only your verdict file(s).
- After writing, run `python3 tools/precheck.py check <batch>` from `arabic-app/`, fix any quote it could not find
  (copy it again, exactly), and run it again until it reports no downgrades you did not intend.
- Never change an id; one line per finding in the packet, no extras.
