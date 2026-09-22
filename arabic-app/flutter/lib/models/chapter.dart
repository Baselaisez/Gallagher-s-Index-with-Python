/// VERIFIED DATA LAYER — analyzed and exercised against the full content tree
/// by flutter/tool/verify_models.dart (see that file for what is asserted).
///
/// Maps `<story-id>/chapters/<n>.json` — the text body: sentences → tokens, each
/// token carrying the three tashkeel layers, morphology links, and i'rab.
/// Field names verified against:
///   content/samples/wasiyyat-abi-hanifa/chapters/1.json
///   content/samples/yunus-wa-al-hut/chapters/1.json
library;

import 'localized.dart';

/// One chapter file (`chapters/<n>.json`). The root has `chapter` (the number)
/// plus a flat `sentences` list. The chapter *title* lives in the manifest's
/// `chapters[]` (ChapterRef), not here.
class Chapter {
  final int chapter; // JSON key "chapter" — the chapter number
  final List<Sentence> sentences;

  const Chapter({required this.chapter, required this.sentences});

  factory Chapter.fromJson(Map<String, dynamic> json) {
    return Chapter(
      chapter: (json['chapter'] as num?)?.toInt() ?? 0,
      sentences: (json['sentences'] as List<dynamic>? ?? const [])
          .map((e) => Sentence.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
    );
  }
}

/// One entry of `chapter.sentences[]`.
class Sentence {
  final String id; // "s1", "s2", ... — used as the progress key and grammar ref
  final AudioSpan? audio; // [startMs, endMs] against the chapter MP3; may be absent
  final LocalizedText translation; // {en, tr} — no `ar` (the Arabic *is* the tokens)
  final List<Token> tokens;
  // Sentence-level i'rab (Qawa'id al-I'rab): each clause named and given —
  // or denied — its mahall. Empty when the sentence is not yet analysed.
  final List<JumlaNote> jumal;

  const Sentence({
    required this.id,
    required this.audio,
    required this.translation,
    required this.tokens,
    required this.jumal,
  });

  factory Sentence.fromJson(Map<String, dynamic> json) {
    return Sentence(
      id: json['id'] as String,
      audio: AudioSpan.fromJson(json['audio']),
      translation: LocalizedText.fromJson(
          (json['translation'] as Map<String, dynamic>?) ?? const {}),
      tokens: (json['tokens'] as List<dynamic>? ?? const [])
          .map((e) => Token.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
      jumal: (json['jumal'] as List<dynamic>? ?? const [])
          .map((e) => JumlaNote.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
    );
  }
}

/// One clause row of a sentence's i'rab section: the clause itself, its
/// Arabic classification, and the two glosses.
class JumlaNote {
  final String text; // the clause, quoted from the sentence
  final String ar; // the classification, madrasah-style
  final String en;
  final String tr;

  const JumlaNote({
    required this.text,
    required this.ar,
    required this.en,
    required this.tr,
  });

  factory JumlaNote.fromJson(Map<String, dynamic> json) {
    return JumlaNote(
      text: json['text'] as String,
      ar: json['ar'] as String,
      en: json['en'] as String,
      tr: json['tr'] as String,
    );
  }
}

/// The `audio` field on a sentence is a two-element `[startMs, endMs]` array
/// (forced-alignment output — data-model rule 5). Drives karaoke highlight and
/// tap-to-hear against the single chapter MP3.
class AudioSpan {
  final int startMs;
  final int endMs;

  const AudioSpan(this.startMs, this.endMs);

  Duration get start => Duration(milliseconds: startMs);
  Duration get end => Duration(milliseconds: endMs);

  /// Tolerant of the field being absent or malformed (uploaded packages have no
  /// alignment and fall back to TTS — see analyzer doc).
  static AudioSpan? fromJson(dynamic raw) {
    if (raw is List && raw.length >= 2) {
      return AudioSpan(
        (raw[0] as num).toInt(),
        (raw[1] as num).toInt(),
      );
    }
    return null;
  }
}

/// One entry of `sentence.tokens[]` — the unit the reader renders and makes
/// tappable. `surface` holds the three pre-rendered tashkeel layers; the tashkeel
/// toggle just selects one (data-model rule 1). `lex` is the join key into the
/// glossary and morphology maps (rule 3).
class Token {
  final SurfaceForms surface; // { full, smart, bare }
  final String lex; // glossary/morphology key, e.g. "arada"
  final String pos; // "verb" | "noun" | "propn" | "prep" | "part" | "pron" | "conj" | "adv"
  final List<String> grammar; // grammar-note ids, e.g. ["form-iv-verbs","hollow-verbs"]; may be empty
  final LocalizedText? irab; // { ar, en, (tr?) } full classical parsing; may be absent
  final List<Segment> segments; // clitic split (rule 2); empty when not segmented
  final String? punctAfter; // "." "،" ":" — printed after the word, outside the tap target
  final String? quoteBefore; // "«" — printed before the word
  final String? quoteAfter; // "»" — printed after the word
  final PhraseRef? phrase; // idiom marker on the FIRST token of a span; null elsewhere

  const Token({
    required this.surface,
    required this.lex,
    required this.pos,
    required this.grammar,
    required this.irab,
    required this.segments,
    required this.punctAfter,
    required this.quoteBefore,
    required this.quoteAfter,
    required this.phrase,
  });

  bool get hasGrammar => grammar.isNotEmpty;
  bool get hasIrab => irab != null && !irab!.isEmpty;
  bool get hasSegments => segments.isNotEmpty;

  factory Token.fromJson(Map<String, dynamic> json) {
    return Token(
      surface:
          SurfaceForms.fromJson((json['surface'] as Map<String, dynamic>?) ?? const {}),
      lex: json['lex'] as String? ?? '',
      pos: json['pos'] as String? ?? '',
      grammar: (json['grammar'] as List<dynamic>? ?? const [])
          .map((e) => e as String)
          .toList(growable: false),
      irab: json['irab'] == null
          ? null
          : LocalizedText.fromJson(json['irab'] as Map<String, dynamic>),
      segments: (json['segments'] as List<dynamic>? ?? const [])
          .map((e) => Segment.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
      punctAfter: json['punctAfter'] as String?,
      quoteBefore: json['quoteBefore'] as String?,
      quoteAfter: json['quoteAfter'] as String?,
      phrase: json['phrase'] == null
          ? null
          : PhraseRef.fromJson(json['phrase'] as Map<String, dynamic>),
    );
  }
}

/// `token.phrase` — declared on the FIRST token of an idiom span
/// (`{"lex": "bayna-yadayh", "span": 2}`). Every token inside the window
/// belongs to the phrase; the phrase has its own glossary entry, and each
/// word keeps its own i'rab — both layers survive (see CLAUDE.md).
class PhraseRef {
  final String lex; // glossary key of the phrase entry (pos: "phrase")
  final int span; // number of tokens the idiom covers, >= 2

  const PhraseRef({required this.lex, required this.span});

  factory PhraseRef.fromJson(Map<String, dynamic> json) {
    return PhraseRef(
      lex: json['lex'] as String? ?? '',
      span: (json['span'] as num?)?.toInt() ?? 0,
    );
  }
}

/// `token.surface` — the three tashkeel layers (data-model rule 1). Invariant
/// enforced in the pipeline: `strip(full) == bare`.
class SurfaceForms {
  final String full; // "أَرَادَ" — complete tashkeel
  final String smart; // "أَرَادَ" — only disambiguating harakat
  final String bare; // "أراد" — no diacritics

  const SurfaceForms({required this.full, required this.smart, required this.bare});

  /// Select the layer for the reader's tashkeel toggle: "full" | "smart" | "bare".
  /// Mirrors `tok.s[state.layer]` in prototype/reader.html.
  String layer(String which) {
    switch (which) {
      case 'bare':
        return bare;
      case 'smart':
        return smart;
      case 'full':
      default:
        return full;
    }
  }

  factory SurfaceForms.fromJson(Map<String, dynamic> json) {
    final full = json['full'] as String? ?? '';
    return SurfaceForms(
      full: full,
      smart: json['smart'] as String? ?? full,
      bare: json['bare'] as String? ?? full,
    );
  }
}

/// One entry of `token.segments[]` — a clitic split so tap-word can resolve each
/// piece (data-model rule 2), e.g. `لِيُوَدِّعَهُ` → لِ + يُوَدِّعَ + هُ.
class Segment {
  final String form; // display form of the segment, e.g. "لِ"
  final String lex; // glossary key for this piece, e.g. "li-taleel", "pron-3ms"
  final String pos; // part of speech of the piece

  const Segment({required this.form, required this.lex, required this.pos});

  factory Segment.fromJson(Map<String, dynamic> json) {
    return Segment(
      form: json['form'] as String? ?? '',
      lex: json['lex'] as String? ?? '',
      pos: json['pos'] as String? ?? '',
    );
  }
}
