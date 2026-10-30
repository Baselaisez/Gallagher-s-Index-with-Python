/// UN-COMPILED SPIKE — design + skeleton only. See docs/05-flutter-architecture.md.
///
/// Skeleton of the Reader screen: the one screen that carries the project's #1
/// risk (RTL + custom per-token text layout, spec §8.1). It demonstrates the
/// recommended approach — a single `Text.rich` per sentence, one `TextSpan` per
/// token, each with its own `TapGestureRecognizer`, wrapped in
/// `Directionality(textDirection: TextDirection.rtl)` — rather than laying out
/// tappable words as separate widgets (which breaks Arabic shaping and justification).
///
/// This file intentionally does NOT compile-verify (no Flutter SDK on the build
/// machine). It is the buildable target: `flutter create .`, add the deps in
/// pubspec.yaml, then fill the `// TODO(spike):` points.
library;

import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

import '../models/chapter.dart';
import '../models/glossary.dart';

/// Which tashkeel layer to render: mirrors the prototype's `state.layer`.
enum TashkeelLayer { full, smart, bare }

extension on TashkeelLayer {
  String get key => switch (this) {
        TashkeelLayer.full => 'full',
        TashkeelLayer.smart => 'smart',
        TashkeelLayer.bare => 'bare',
      };
}

/// Maps a word's level (1..4, bucketed) to its underline colour. Real values
/// come from the theme (see architecture doc §"Level underlines"); these mirror
/// the prototype's `--lvl1..4` light-theme tokens.
const Map<int, Color> kLevelColors = {
  1: Color(0xFF2E7D46),
  2: Color(0xFF0E7C74),
  3: Color(0xFFB07A1E),
  4: Color(0xFFB23B3B),
};

int _levelBucket(int level) => level >= 4 ? 4 : level;

/// The reader screen. In the real app this is a `ConsumerWidget` (riverpod) that
/// watches the loaded package + reader settings; here it takes plain data so the
/// layout approach is legible without the state plumbing.
class ReaderScreen extends StatefulWidget {
  final List<Chapter> chapters;
  final Glossary glossary;

  /// Called when a token is tapped — the host opens the WordSheet (Word / Sarf /
  /// I'rab / Grammar tabs). See word_sheet.dart (not in this spike).
  final void Function(Token token) onTapWord;

  /// Called when a sentence's ▶ is tapped — the host plays audio (just_audio for
  /// aligned narration, or flutter_tts of the `full` layer for uploads).
  final void Function(Sentence sentence) onPlaySentence;

  const ReaderScreen({
    super.key,
    required this.chapters,
    required this.glossary,
    required this.onTapWord,
    required this.onPlaySentence,
  });

  @override
  State<ReaderScreen> createState() => _ReaderScreenState();
}

class _ReaderScreenState extends State<ReaderScreen> {
  TashkeelLayer _layer = TashkeelLayer.full;
  bool _underlines = true;
  double _arSize = 26.0; // logical px; prototype default ~1.7rem
  String? _playingSentenceId; // drives the karaoke highlight

  // Recognizers must live for the lifetime of the spans and be disposed, or
  // they leak. We rebuild them whenever the layer/story changes.
  final List<TapGestureRecognizer> _recognizers = [];

  @override
  void dispose() {
    for (final r in _recognizers) {
      r.dispose();
    }
    super.dispose();
  }

  void _resetRecognizers() {
    for (final r in _recognizers) {
      r.dispose();
    }
    _recognizers.clear();
  }

  @override
  Widget build(BuildContext context) {
    // TODO(spike): move layer/underline/size into a riverpod ReaderSettings
    // provider persisted via shared_preferences (keys mirror qissa-layer,
    // qissa-arsize in the prototype).
    _resetRecognizers();
    return Directionality(
      // The whole reading column is RTL. Non-Arabic UI chrome can override
      // locally with its own Directionality if needed.
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('Qissa — Reader (spike)')),
        body: ListView(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          children: [
            for (final chapter in widget.chapters) ...[
              _ChapterHeader(number: chapter.chapter),
              for (final sentence in chapter.sentences)
                _sentenceBlock(context, sentence),
            ],
          ],
        ),
        // The tashkeel toggle / font-size / play-all controls live in a bottom
        // control bar in the real app; omitted from the skeleton.
      ),
    );
  }

  Widget _sentenceBlock(BuildContext context, Sentence sentence) {
    final bool playing = sentence.id == _playingSentenceId;
    return Container(
      margin: const EdgeInsets.only(bottom: 14),
      padding: const EdgeInsets.all(8),
      decoration: BoxDecoration(
        // Karaoke highlight: prototype toggles `.sentence.playing`.
        // ignore: deprecated_member_use
        color: playing
            ? Theme.of(context).colorScheme.primary.withOpacity(0.10)
            : null,
        borderRadius: BorderRadius.circular(10),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _arabicLine(context, sentence),
          const SizedBox(height: 6),
          Row(
            children: [
              IconButton(
                icon: const Icon(Icons.play_arrow),
                tooltip: 'Listen',
                onPressed: () {
                  setState(() => _playingSentenceId = sentence.id);
                  widget.onPlaySentence(sentence);
                  // TODO(spike): clear _playingSentenceId on audio complete;
                  // for just_audio drive it from positionStream vs AudioSpan,
                  // for flutter_tts from the completion handler.
                },
              ),
              // Bilingual translation strip (EN/TR), respects the trans setting.
              Expanded(
                child: Text(
                  sentence.translation.resolve('en'), // TODO(spike): use uiLang
                  style: Theme.of(context).textTheme.bodySmall,
                  textDirection: TextDirection.ltr,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  /// THE CORE OF THE SPIKE: one `Text.rich` for the whole sentence so the Arabic
  /// shaping engine sees a continuous run (correct ligatures, kashida, RTL
  /// bidi), while each token is still an independently tappable + underlinable
  /// span. Rendering tokens as separate Row/Wrap widgets would break shaping and
  /// is explicitly rejected in the architecture doc.
  Widget _arabicLine(BuildContext context, Sentence sentence) {
    final spans = <InlineSpan>[];

    for (var i = 0; i < sentence.tokens.length; i++) {
      final token = sentence.tokens[i];

      // Punctuation / quotation marks are rendered OUTSIDE the tap target so a
      // tap resolves the lexical word, and so the mark keeps neutral-bidi
      // behaviour (prototype appends them as bare text nodes).
      if (token.quoteBefore != null) {
        spans.add(TextSpan(text: token.quoteBefore));
      }

      final entry = widget.glossary[token.lex];
      final level = entry?.level ?? 0;
      final underlineColor =
          (_underlines && level > 0) ? kLevelColors[_levelBucket(level)] : null;

      final recognizer = TapGestureRecognizer()
        ..onTap = () => widget.onTapWord(token);
      _recognizers.add(recognizer);

      spans.add(TextSpan(
        text: token.surface.layer(_layer.key),
        recognizer: recognizer,
        style: TextStyle(
          // TODO(spike): pull the family from the bundled Noto Naskh Arabic
          // (declared in pubspec.yaml); height tuned for tashkeel headroom.
          fontFamily: 'NotoNaskhArabic',
          fontSize: _arSize,
          height: 1.9,
          decoration:
              underlineColor != null ? TextDecoration.underline : TextDecoration.none,
          decorationColor: underlineColor,
          decorationThickness: 2.5,
        ),
      ));

      if (token.punctAfter != null) {
        spans.add(TextSpan(text: token.punctAfter));
      }
      if (token.quoteAfter != null) {
        spans.add(TextSpan(text: token.quoteAfter));
      }
      // Inter-token space (prototype inserts a text node between words).
      if (i < sentence.tokens.length - 1) {
        spans.add(const TextSpan(text: ' '));
      }
    }

    return Text.rich(
      TextSpan(children: spans),
      textDirection: TextDirection.rtl,
      textAlign: TextAlign.right,
      // TODO(spike): consider `strutStyle` to keep line boxes stable across
      // tashkeel layers so toggling doesn't reflow the whole page.
    );
  }
}

class _ChapterHeader extends StatelessWidget {
  final int number;
  const _ChapterHeader({required this.number});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8, top: 4),
      child: Text(
        'الفصل $number', // TODO(spike): show the localized ChapterRef.title too
        style: Theme.of(context).textTheme.titleMedium,
        textDirection: TextDirection.rtl,
      ),
    );
  }
}
