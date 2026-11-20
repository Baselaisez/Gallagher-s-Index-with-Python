/// VERIFIED DATA LAYER — analyzed and exercised against the full content tree
/// by flutter/tool/verify_models.dart (see that file for what is asserted).
///
/// Maps `<story-id>/manifest.json` — per-story metadata + chapter list.
/// Field names verified against:
///   content/samples/wasiyyat-abi-hanifa/manifest.json
///   content/user-uploads/deeds-are-by-intentions/manifest.json
library;

import 'localized.dart';

/// Story metadata (manifest.json root). The chapter *bodies* live in separate
/// `chapters/<n>.json` files (see Chapter model); this only lists them.
class StoryManifest {
  final String id;
  final String storyGroup;
  final LocalizedText title; // {ar,en,tr}
  final LocalizedText subtitle; // {ar,en} — optional, sometimes absent
  final int level;
  final String levelName;
  final String version;
  final String published; // "YYYY-MM-DD" — the day the story entered the library
  final String access; // "free" | "premium" | "user-upload"
  final List<ChapterRef> chapters;
  final List<StorySibling> siblings; // same story, other levels (may be empty)
  final Attribution attribution;

  const StoryManifest({
    required this.id,
    required this.storyGroup,
    required this.title,
    required this.subtitle,
    required this.level,
    required this.levelName,
    required this.version,
    required this.published,
    required this.access,
    required this.chapters,
    required this.siblings,
    required this.attribution,
  });

  factory StoryManifest.fromJson(Map<String, dynamic> json) {
    return StoryManifest(
      id: json['id'] as String,
      storyGroup: json['storyGroup'] as String? ?? (json['id'] as String),
      title: LocalizedText.fromJson(
          (json['title'] as Map<String, dynamic>?) ?? const {}),
      subtitle: json['subtitle'] == null
          ? LocalizedText.empty
          : LocalizedText.fromJson(json['subtitle'] as Map<String, dynamic>),
      level: (json['level'] as num?)?.toInt() ?? 1,
      levelName: json['levelName'] as String? ?? '',
      version: json['version'] as String? ?? '',
      published: json['published'] as String? ?? '',
      access: json['access'] as String? ?? 'free',
      chapters: (json['chapters'] as List<dynamic>? ?? const [])
          .map((e) => ChapterRef.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
      siblings: (json['siblings'] as List<dynamic>? ?? const [])
          .map((e) => StorySibling.fromJson(e as Map<String, dynamic>))
          .toList(growable: false),
      attribution: Attribution.fromJson(
          (json['attribution'] as Map<String, dynamic>?) ?? const {}),
    );
  }
}

/// One entry of `manifest.chapters[]`. Points at `chapters/<n>.json` and,
/// optionally, the human narration MP3 (spec §3.4 audiobooks).
class ChapterRef {
  final int n; // chapter number; also the filename: chapters/<n>.json
  final LocalizedText title; // {ar,en} or {ar,en,tr}
  /// JSON key `audioFile` — the chapter's recording, package-relative. The
  /// sentences carry their [startMs, endMs] slices of this one file; either
  /// half missing means TTS fallback, never silence (see CLAUDE.md).
  final String? audioFile;

  const ChapterRef({required this.n, required this.title, this.audioFile});

  factory ChapterRef.fromJson(Map<String, dynamic> json) {
    return ChapterRef(
      n: (json['n'] as num).toInt(),
      title: LocalizedText.fromJson(
          (json['title'] as Map<String, dynamic>?) ?? const {}),
      audioFile: json['audioFile'] as String?,
    );
  }
}

/// `manifest.siblings[]` — same story at another level ("read it again as you
/// grow", spec §3.5 / data-model rule 6). Often `status: "planned"`.
class StorySibling {
  final String id;
  final int level;
  final String status; // "planned" | (future) "published"
  final String? note;

  const StorySibling({
    required this.id,
    required this.level,
    required this.status,
    this.note,
  });

  factory StorySibling.fromJson(Map<String, dynamic> json) {
    return StorySibling(
      id: json['id'] as String,
      level: (json['level'] as num?)?.toInt() ?? 0,
      status: json['status'] as String? ?? '',
      note: json['note'] as String?,
    );
  }
}

/// `manifest.attribution` — provenance + the review banner state. The reader
/// shows a "machine-analyzed — may contain errors" banner when
/// reviewStatus == "auto-generated-unreviewed" (analyzer doc, "Honest provenance").
class Attribution {
  final LocalizedText text; // {ar?, en} free-text attribution
  final String reviewStatus; // "pending-scholarly-review" | "auto-generated-unreviewed"

  const Attribution({required this.text, required this.reviewStatus});

  bool get isMachineGenerated => reviewStatus == 'auto-generated-unreviewed';

  factory Attribution.fromJson(Map<String, dynamic> json) {
    // reviewStatus sits alongside ar/en inside the attribution object; strip it
    // out of the localized text bag.
    final text = <String, dynamic>{
      if (json['ar'] is String) 'ar': json['ar'],
      if (json['en'] is String) 'en': json['en'],
      if (json['tr'] is String) 'tr': json['tr'],
    };
    return Attribution(
      text: LocalizedText.fromJson(text),
      reviewStatus: json['reviewStatus'] as String? ?? '',
    );
  }
}
