/// UN-COMPILED SPIKE — design + skeleton only. See docs/05-flutter-architecture.md.
///
/// Maps `content/grammar/<note-id>.json` — the GLOBAL, reusable grammar notes
/// (data-model rule 4). The same note object opens from every story and every
/// user upload that links its id. Powers the word sheet's Grammar tab and the
/// standalone Grammar Reference browser (with search + level filter).
/// Field names verified against:
///   content/grammar/inna-wa-akhawatuha.json
///   content/grammar/badal.json
library;

import 'localized.dart';

/// One grammar note.
///
/// FIELD-NAME NOTE: the canonical package keys are `classicalSources` and
/// `commonMistakes` (the prototype's build step renames them to `sources` /
/// `mistakes` in its inlined data — we follow the *package* JSON here).
class GrammarNote {
  final String id; // "inna-wa-akhawatuha"
  final LocalizedText title; // { ar, en, (tr?) }
  final int level; // 1..6
  final String group; // "nahw" | "awamil" | "sarf" — madrasah primer grouping
  final String? amil; // for awamil: what the governor governs; absent otherwise
  final List<String> classicalSources; // Arabic source titles (JSON key: classicalSources)
  final LocalizedText explanation; // { en, tr }
  final List<GrammarExample> examples; // ≥1; some tagged with sourceStory + sentence
  final List<CommonMistake> commonMistakes; // ≥1 (rule 4) (JSON key: commonMistakes)
  final List<String> relatedNotes; // other note ids
  final bool spotTheErrorSeed; // gameSeeds.spotTheError — feeds the Spot-the-error game

  const GrammarNote({
    required this.id,
    required this.title,
    required this.level,
    required this.group,
    required this.amil,
    required this.classicalSources,
    required this.explanation,
    required this.examples,
    required this.commonMistakes,
    required this.relatedNotes,
    required this.spotTheErrorSeed,
  });

  factory GrammarNote.fromJson(Map<String, dynamic> json) {
    final seeds = json['gameSeeds'] as Map<String, dynamic>?;
    return GrammarNote(
      id: json['id'] as String,
      title: LocalizedText.fromJson(
          (json['title'] as Map<String, dynamic>?) ?? const {}),
      level: (json['level'] as num?)?.toInt() ?? 0,
      group: json['group'] as String? ?? '',
      amil: json['amil'] as String?,
      classicalSources: (json['classicalSources'] as List<dynamic>? ?? const [])
          .map((e) => e as String)
          .toList(growable: false),
      explanation: LocalizedText.fromJson(
          (json['explanation'] as Map<String, dynamic>?) ?? const {}),
      examples: (json['examples'] as List<dynamic>? ?? const [])
          .map((e) => GrammarExample.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
      commonMistakes: (json['commonMistakes'] as List<dynamic>? ?? const [])
          .map((e) => CommonMistake.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
      relatedNotes: (json['relatedNotes'] as List<dynamic>? ?? const [])
          .map((e) => e as String)
          .toList(growable: false),
      spotTheErrorSeed: (seeds?['spotTheError'] as bool?) ?? false,
    );
  }
}

/// One entry of `note.examples[]`. When `sourceStory`/`sentence` are present the
/// reader shows a "from this story" tag (reader.html: `x.src === CUR.id`).
class GrammarExample {
  final String ar; // vocalized Arabic example
  final String en; // English rendering + brief parsing note
  final String? sourceStory; // story id, e.g. "wasiyyat-abi-hanifa-L2"
  final String? sentence; // sentence id within that story, e.g. "s7"

  const GrammarExample({
    required this.ar,
    required this.en,
    required this.sourceStory,
    required this.sentence,
  });

  factory GrammarExample.fromJson(Map<String, dynamic> json) {
    return GrammarExample(
      ar: json['ar'] as String? ?? '',
      en: json['en'] as String? ?? '',
      sourceStory: json['sourceStory'] as String?,
      sentence: json['sentence'] as String?,
    );
  }
}

/// One entry of `note.commonMistakes[]` — the "أخطاء شائعة" block. The wrong form
/// learners produce, the correct form, and why. Also the seed corpus for the
/// Spot-the-error game.
class CommonMistake {
  final String wrong; // the erroneous form, e.g. "إنّ العلمُ أمانةٌ"
  final String right; // the corrected form
  final LocalizedText why; // { en, tr } explanation

  const CommonMistake({required this.wrong, required this.right, required this.why});

  factory CommonMistake.fromJson(Map<String, dynamic> json) {
    return CommonMistake(
      wrong: json['wrong'] as String? ?? '',
      right: json['right'] as String? ?? '',
      why: LocalizedText.fromJson(
          (json['why'] as Map<String, dynamic>?) ?? const {}),
    );
  }
}
