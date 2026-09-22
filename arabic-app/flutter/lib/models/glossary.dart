/// VERIFIED DATA LAYER — analyzed and exercised against the full content tree
/// by flutter/tool/verify_models.dart (see that file for what is asserted).
///
/// Maps `<story-id>/glossary.json` — the story-scoped lexicon keyed by `lex`.
/// Every token's `lex` resolves here for the tap-word sheet, the level-colored
/// underline, and flashcard creation (data-model rule 3).
/// Field names verified against:
///   content/samples/wasiyyat-abi-hanifa/glossary.json
///   content/samples/yunus-wa-al-hut/glossary.json
library;

import 'localized.dart';

/// The glossary file: a single `entries` object mapping `lex` → GlossaryEntry.
/// NOTE: `entries` is a JSON object (map), not an array.
class Glossary {
  final Map<String, GlossaryEntry> entries;

  const Glossary(this.entries);

  GlossaryEntry? operator [](String lex) => entries[lex];

  factory Glossary.fromJson(Map<String, dynamic> json) {
    final raw = (json['entries'] as Map<String, dynamic>?) ?? const {};
    return Glossary({
      for (final e in raw.entries)
        e.key: GlossaryEntry.fromJson(e.key, e.value as Map<String, dynamic>),
    });
  }
}

/// One lexicon entry. Particles/pronouns omit `root`, `form`, `plural`, `audio`;
/// only verbs carry `form` (the Roman-numeral verb form, e.g. "IV").
class GlossaryEntry {
  final String lex; // the map key, carried in for convenience
  final String lemma; // vocalized dictionary form, e.g. "أَرَادَ"
  final String? root; // "ر و د" — absent for particles/pronouns/proper nouns
  final String pos; // "verb" | "noun" | "propn" | "prep" | "part" | "pron" | "conj" | "adv"
  final String? form; // verb form as a Roman numeral string: "I".."VIII"; verbs only
  final String? plural; // broken plural, e.g. "مُدُن"; nouns only
  final LocalizedText gloss; // { en, tr } — NOTE: no `ar`
  final int level; // 0..6; 0 = proper nouns/pronouns (no underline)
  final String? audio; // "audio/words/arada.mp3"; may be absent (TTS fallback)

  const GlossaryEntry({
    required this.lex,
    required this.lemma,
    required this.root,
    required this.pos,
    required this.form,
    required this.plural,
    required this.gloss,
    required this.level,
    required this.audio,
  });

  /// Reader underlines only levels 1..4 (levelBucket in reader.html caps at 4);
  /// level 0 (names, pronouns) gets none.
  bool get showsUnderline => level > 0;

  factory GlossaryEntry.fromJson(String lex, Map<String, dynamic> json) {
    return GlossaryEntry(
      lex: lex,
      lemma: json['lemma'] as String? ?? '',
      root: json['root'] as String?,
      pos: json['pos'] as String? ?? '',
      form: json['form'] as String?,
      plural: json['plural'] as String?,
      gloss: LocalizedText.fromJson(
          (json['gloss'] as Map<String, dynamic>?) ?? const {}),
      level: (json['level'] as num?)?.toInt() ?? 0,
      audio: json['audio'] as String?,
    );
  }
}
