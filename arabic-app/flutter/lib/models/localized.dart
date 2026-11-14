/// VERIFIED DATA LAYER — analyzed and exercised against the full content tree
/// by flutter/tool/verify_models.dart (see that file for what is asserted).
///
/// Shared helper for the `{ "ar": ..., "en": ..., "tr": ... }` localized-string
/// objects that appear all over the content packages (titles, subtitles, glosses,
/// translations, i'rab, grammar explanations). Mirrors the web reader's `T(v)`
/// helper in prototype/reader.html.
library;

/// A bag of language-keyed strings. Not every object carries every language:
/// - manifest `title` has ar/en/tr; `subtitle` has only ar/en.
/// - chapter `title` sometimes has only ar/en, sometimes ar/en/tr.
/// - sentence `translation` has en/tr (no ar — the Arabic *is* the tokens).
/// - token `irab` has ar + en (+ occasionally tr).
/// Callers therefore must tolerate missing keys and fall back.
class LocalizedText {
  final Map<String, String> _byLang;

  const LocalizedText(this._byLang);

  factory LocalizedText.fromJson(Map<String, dynamic> json) {
    return LocalizedText({
      for (final entry in json.entries)
        if (entry.value is String) entry.key: entry.value as String,
    });
  }

  /// Empty localized text (used when a package omits an optional field).
  static const LocalizedText empty = LocalizedText({});

  /// Raw access to a specific language, or null if absent.
  String? maybe(String lang) => _byLang[lang];

  bool get isEmpty => _byLang.isEmpty;

  /// Resolve for a UI/gloss language with the web reader's fallback order:
  /// requested language -> English -> Arabic -> "".
  /// Matches `T(v)` in prototype/reader.html.
  String resolve(String lang) =>
      _byLang[lang] ?? _byLang['en'] ?? _byLang['ar'] ?? '';

  String get ar => _byLang['ar'] ?? '';
  String get en => _byLang['en'] ?? '';
  String get tr => _byLang['tr'] ?? _byLang['en'] ?? '';
}
