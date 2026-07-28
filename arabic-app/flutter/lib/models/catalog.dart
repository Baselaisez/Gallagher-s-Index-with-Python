/// VERIFIED DATA LAYER — analyzed and exercised against the full content tree
/// by flutter/tool/verify_models.dart (see that file for what is asserted).
///
/// Maps `content/catalog.json` — the server-driven index the app fetches first
/// (spec §3.5 "self-updating content"). Field names verified against the real
/// file: content/catalog.json.
library;

import 'localized.dart';

/// Top-level catalog index. Fetched from the CDN, then cached (see caching
/// section of the architecture doc). Corresponds to the `catalog.json` root.
class Catalog {
  final String catalogVersion; // "0.1"
  final String generatedFrom; // "tools/build_prototype.py"
  final List<CatalogEntry> packages;

  const Catalog({
    required this.catalogVersion,
    required this.generatedFrom,
    required this.packages,
  });

  factory Catalog.fromJson(Map<String, dynamic> json) {
    return Catalog(
      catalogVersion: json['catalogVersion'] as String? ?? '',
      generatedFrom: json['generatedFrom'] as String? ?? '',
      packages: (json['packages'] as List<dynamic>? ?? const [])
          .map((e) => CatalogEntry.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
    );
  }
}

/// One row in `catalog.packages[]`. NOTE: here `chapters` is an INT (a count),
/// whereas in a manifest `chapters` is a LIST of chapter objects. Do not share
/// a model between the two.
class CatalogEntry {
  final String id; // "wasiyyat-abi-hanifa-L2"
  final LocalizedText title; // {ar,en,tr}
  final int level; // 1..6
  final String levelName; // "Elementary"
  final String version; // "0.1.0"
  final String published; // "YYYY-MM-DD" — the day the story entered the library
  final String access; // "free" | "premium" | "user-upload"
  final String storyGroup; // groups same-story-different-levels siblings
  final String reviewStatus; // "pending-scholarly-review" | "auto-generated-unreviewed"
  final int chapterCount; // JSON key is "chapters" but it is a COUNT here

  const CatalogEntry({
    required this.id,
    required this.title,
    required this.level,
    required this.levelName,
    required this.version,
    required this.published,
    required this.access,
    required this.storyGroup,
    required this.reviewStatus,
    required this.chapterCount,
  });

  /// True for the Lite tier gating: free or currently-rotated stories are
  /// openable without Premium (spec §3.6). Real gating also considers
  bool get isFreeToOpen => access == 'free' || access == 'user-upload';

  factory CatalogEntry.fromJson(Map<String, dynamic> json) {
    return CatalogEntry(
      id: json['id'] as String,
      title: LocalizedText.fromJson(
          (json['title'] as Map<String, dynamic>?) ?? const {}),
      level: (json['level'] as num?)?.toInt() ?? 1,
      levelName: json['levelName'] as String? ?? '',
      version: json['version'] as String? ?? '',
      published: json['published'] as String? ?? '',
      access: json['access'] as String? ?? 'free',
      storyGroup: json['storyGroup'] as String? ?? (json['id'] as String),
      reviewStatus: json['reviewStatus'] as String? ?? '',
      chapterCount: (json['chapters'] as num?)?.toInt() ?? 0,
    );
  }
}
