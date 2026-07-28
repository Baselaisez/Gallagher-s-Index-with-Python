/// Conformance proof for the Flutter data layer.
///
/// The models in ../lib/models were originally authored without an SDK and
/// carried an "UN-COMPILED SPIKE" banner. This harness is what retires that
/// banner: it parses the REAL content tree — the catalog, every package's
/// manifest/chapters/glossary/morphology, and every grammar note — through the
/// production `fromJson` constructors, then re-asserts the content invariants
/// from the Dart side. If the Dart models and the Python validator ever
/// disagree about the schema, this is where it shows.
///
///   dart run flutter/tool/verify_models.dart [content-root]
///
/// Exit 0 = every file parsed and every invariant held. Any failure prints the
/// file and the reason and exits 1. Run from arabic-app/ (default content root:
/// ./content). Pure Dart on purpose — no Flutter SDK needed to keep this green.
library;

import 'dart:convert';
import 'dart:io';

import '../lib/models/catalog.dart';
import '../lib/models/chapter.dart';
import '../lib/models/glossary.dart';
import '../lib/models/grammar_note.dart';
import '../lib/models/manifest.dart';
import '../lib/models/morphology.dart';

// Same range the Python validator strips: tanwin/harakat/shadda/sukun,
// the common quranic marks, dagger alif.
final _diacritics = RegExp('[ً-ٰ]');
String stripTashkeel(String s) => s.replaceAll(_diacritics, '');

int failures = 0;
void fail(String where, String msg) {
  failures++;
  stderr.writeln('FAIL $where — $msg');
}

Map<String, dynamic> readJson(File f) =>
    jsonDecode(f.readAsStringSync()) as Map<String, dynamic>;

void main(List<String> args) {
  final root = Directory(args.isNotEmpty ? args[0] : 'content');
  if (!root.existsSync()) {
    stderr.writeln('content root not found: ${root.path}');
    exit(2);
  }

  // ---------- the grammar registry ----------
  final noteDir = Directory('${root.path}/grammar');
  final noteIds = <String>{};
  var notesWithQuestion = 0;
  for (final f in noteDir.listSync().whereType<File>().toList()
    ..sort((a, b) => a.path.compareTo(b.path))) {
    if (!f.path.endsWith('.json')) continue;
    final note = GrammarNote.fromJson(readJson(f));
    noteIds.add(note.id);
    final where = 'grammar/${note.id}';
    if (note.title.ar.isEmpty || note.title.en.isEmpty) {
      fail(where, 'title must carry ar and en');
    }
    // The plain lede is REQUIRED and bilingual — the first thing a reader sees.
    if (note.plain.en.isEmpty || note.plain.tr.isEmpty) {
      fail(where, 'plain lede missing a language');
    }
    if (note.explanation.en.isEmpty || note.explanation.tr.isEmpty) {
      fail(where, 'explanation missing a language');
    }
    if (note.examples.isEmpty) fail(where, 'no examples');
    if (note.commonMistakes.isEmpty) fail(where, 'no commonMistakes');
    const groups = {'sarf', 'nahw', 'awamil', 'balagha'};
    if (!groups.contains(note.group)) fail(where, 'bad group ${note.group}');
    final q = note.question;
    if (q != null) {
      notesWithQuestion++;
      // The two lists correspond index-by-index; unequal lengths would pair
      // a Turkish question with the wrong English one.
      if (q.tr.isEmpty || q.tr.length != q.en.length) {
        fail(where, 'question lists must be non-empty and equal length');
      }
    }
  }

  // ---------- the catalog ----------
  final catalog =
      Catalog.fromJson(readJson(File('${root.path}/catalog.json')));
  final pkgDirs = <Directory>[];
  for (final coll in ['samples', 'user-uploads']) {
    final d = Directory('${root.path}/$coll');
    if (!d.existsSync()) continue;
    pkgDirs.addAll(d
        .listSync()
        .whereType<Directory>()
        .where((p) => File('${p.path}/manifest.json').existsSync()));
  }
  if (catalog.packages.length != pkgDirs.length) {
    fail('catalog.json',
        '${catalog.packages.length} entries but ${pkgDirs.length} packages on disk');
  }
  final publishedRe = RegExp(r'^\d{4}-\d{2}-\d{2}$');
  for (final e in catalog.packages) {
    if (!publishedRe.hasMatch(e.published)) {
      fail('catalog:${e.id}', 'published not YYYY-MM-DD: "${e.published}"');
    }
  }

  // ---------- every package ----------
  var stories = 0, tokens = 0, phrases = 0, recordedChapters = 0;
  for (final pkg in pkgDirs..sort((a, b) => a.path.compareTo(b.path))) {
    final pkgName = pkg.path.split('/').last;
    final manifest =
        StoryManifest.fromJson(readJson(File('${pkg.path}/manifest.json')));
    stories++;
    if (!publishedRe.hasMatch(manifest.published)) {
      fail(pkgName, 'manifest.published not a date: "${manifest.published}"');
    }
    if (!{'free', 'premium', 'user-upload'}.contains(manifest.access)) {
      fail(pkgName, 'unknown access "${manifest.access}"');
    }

    final glossary =
        Glossary.fromJson(readJson(File('${pkg.path}/glossary.json')));

    final morphFile = File('${pkg.path}/morphology.json');
    if (morphFile.existsSync()) {
      final morph = Morphology.fromJson(readJson(morphFile));
      morph.verbs.forEach((lex, v) {
        final where = '$pkgName/morphology:$lex';
        if (glossary[lex] == null) fail(where, 'verb lex not in glossary');
        if (v.mazi.length != 14) fail(where, 'mazi has ${v.mazi.length} cells');
        if (v.mudari.length != 14) {
          fail(where, 'mudari has ${v.mudari.length} cells');
        }
        if (v.amr.length != 6) fail(where, 'amr has ${v.amr.length} cells');
        // Half a passive is worse than none: the table would show a past with
        // no present or the reverse.
        if ((v.majhulMazi == null) != (v.majhulMudari == null)) {
          fail(where, 'half-authored passive pair');
        }
      });
    }

    for (final ref in manifest.chapters) {
      final chFile = File('${pkg.path}/chapters/${ref.n}.json');
      if (!chFile.existsSync()) {
        fail('$pkgName/ch${ref.n}', 'declared in manifest but file missing');
        continue;
      }
      if (ref.audioFile != null) recordedChapters++;
      final chapter = Chapter.fromJson(readJson(chFile));
      for (final sen in chapter.sentences) {
        if (sen.translation.en.isEmpty || sen.translation.tr.isEmpty) {
          fail('$pkgName/${sen.id}', 'translation missing a language');
        }
        final a = sen.audio;
        if (a != null && a.startMs >= a.endMs) {
          fail('$pkgName/${sen.id}', 'audio span start >= end');
        }
        for (var ti = 0; ti < sen.tokens.length; ti++) {
          final tok = sen.tokens[ti];
          final where = '$pkgName/${sen.id}[$ti]';
          tokens++;
          // The tashkeel-layer law, re-proven from the Dart side.
          if (stripTashkeel(tok.surface.full) != tok.surface.bare) {
            fail(where,
                'strip(full) "${stripTashkeel(tok.surface.full)}" != bare "${tok.surface.bare}"');
          }
          if (glossary[tok.lex] == null) {
            fail(where, 'lex "${tok.lex}" not in glossary');
          }
          for (final gid in tok.grammar) {
            if (!noteIds.contains(gid)) {
              fail(where, 'grammar id "$gid" not in registry');
            }
          }
          for (final seg in tok.segments) {
            if (glossary[seg.lex] == null) {
              fail(where, 'segment lex "${seg.lex}" not in glossary');
            }
          }
          final ph = tok.phrase;
          if (ph != null) {
            phrases++;
            if (ph.span < 2) fail(where, 'phrase span ${ph.span} < 2');
            if (ti + ph.span > sen.tokens.length) {
              fail(where, 'phrase span runs past the sentence');
            }
            if (glossary[ph.lex] == null) {
              fail(where, 'phrase lex "${ph.lex}" not in glossary');
            }
          }
        }
      }
    }
  }

  stdout.writeln('parsed: $stories stories, $tokens tokens, '
      '${noteIds.length} grammar notes ($notesWithQuestion with a question test), '
      '$phrases phrase-marked tokens, $recordedChapters recorded chapters');
  if (failures > 0) {
    stderr.writeln('\n$failures failure(s)');
    exit(1);
  }
  stdout.writeln('the Dart models parse the entire content tree — no drift');
}
