# Qissa — Flutter client (data layer VERIFIED; screens still a spike)

> **Status: split.** The `lib/models/` data layer is now REAL, verified Dart:
> `dart analyze` clean, and `tool/verify_models.dart` parses the entire content
> tree through the production `fromJson`s — every package, every chapter, every
> grammar note — and re-asserts the core invariants (tashkeel law, lex/grammar
> resolution, phrase spans, paradigm sizes) from the Dart side. Run it with any
> plain Dart SDK, no Flutter needed:
>
> ```sh
> dart analyze flutter/lib/models flutter/tool
> dart flutter/tool/verify_models.dart content     # from arabic-app/
> ```
>
> The `main.dart` / `reader/` screens remain a DESIGN SPIKE: they import
> Flutter, which is not on this machine, and have never been type-checked. The
> boundary is marked by the file headers.

This is the Flutter port of the web prototype at `../prototype/reader.html`,
rendering the same content packages described in `../docs/03-content-data-model.md`.
The full architecture rationale is in **`../docs/05-flutter-architecture.md`** —
read that first.

## What exists here

```
flutter/
  README.md                     # you are here
  pubspec.yaml                  # deps + Noto Naskh Arabic font (NOT locked)
  lib/
    main.dart                   # app entry stub (not runnable)
    models/                     # data layer — faithful fromJson for every package file
      localized.dart            #   {ar,en,tr} helper (mirrors reader.html T())
      catalog.dart              #   catalog.json
      manifest.dart             #   <story>/manifest.json
      chapter.dart              #   <story>/chapters/<n>.json  (Sentence, Token, ...)
      glossary.dart             #   <story>/glossary.json
      morphology.dart           #   <story>/morphology.json  (verb paradigms)
      grammar_note.dart         #   grammar/<id>.json  (global, reusable)
    reader/
      reader_screen.dart        # THE spike: RTL Text.rich + per-token tap targets
```

Not yet written (scoped out of the spike; mapped in the architecture doc):
the Library, WordSheet, GrammarReference, Deck/Review and Games screens, the
repository/networking layer, the riverpod providers, and the audio service.

## Turning this into a running app

1. **Install Flutter** (3.22+) and confirm `flutter doctor` is green.
2. From this directory, generate the platform folders around the existing `lib/`:
   ```
   flutter create .
   ```
   `flutter create` will not overwrite existing `lib/` or `pubspec.yaml`.
3. **Add the font**: drop `NotoNaskhArabic-Regular.ttf` and `-Bold.ttf` into
   `assets/fonts/` (already declared in `pubspec.yaml`). Get them from Google Fonts
   (Noto Naskh Arabic, OFL).
4. `flutter pub get` to resolve deps and generate `pubspec.lock`.
5. Wire the widgets: feed `ReaderScreen` a parsed package. A quick smoke test is
   to bundle one sample package (e.g. `../content/samples/wasiyyat-abi-hanifa/`)
   as a dev asset, parse it with the `models/`, and push `ReaderScreen`.
6. Work through the `// TODO(spike):` markers (concentrated in `reader_screen.dart`
   and `main.dart`).

## IMPORTANT: the root `.gitignore` will hide `lib/`

The repository root `.gitignore` is the standard **Python** template and contains
a bare `lib/` rule (under "Distribution / packaging"). That pattern matches
`arabic-app/flutter/lib/` too, so **these Dart source files are git-ignored by
default** and will silently not be committed.

Before committing this spike, the maintainer must un-ignore it — e.g. append to
the root `.gitignore`:

```gitignore
# Flutter client sources live under lib/ — the Python lib/ rule above must not hide them
!arabic-app/flutter/lib/
!arabic-app/flutter/lib/**
```

(Verify with `git check-ignore -v arabic-app/flutter/lib/main.dart`.) Once
`flutter create .` runs, also confirm the generated `flutter/.gitignore` is
present so build artifacts — `build/`, `.dart_tool/`, `pubspec.lock` policy per
app-vs-package — are handled the Flutter way.

## Parity target

Every prototype feature and the `reader.html` function that implements it is
mapped to a Flutter approach in the architecture doc's screen/widget table. This
skeleton implements only the reader's core text-layout risk; the rest is design.
