/// UN-COMPILED SPIKE — design + skeleton only. See docs/05-flutter-architecture.md.
///
/// App entry stub. This wires just enough to show where the pieces plug in; it
/// is NOT runnable until `flutter create .` generates the platform folders and
/// the pubspec.yaml deps are fetched. Do not treat this as a working app.
library;

import 'package:flutter/material.dart';
// TODO(spike): add `flutter_riverpod` and wrap in a ProviderScope (see doc
// §"State management"). Kept out here so the stub reads without the dep.

void main() {
  // TODO(spike): runApp(const ProviderScope(child: QissaApp()));
  runApp(const QissaApp());
}

class QissaApp extends StatelessWidget {
  const QissaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Qissa',
      debugShowCheckedModeBanner: false,
      theme: _buildTheme(Brightness.light),
      darkTheme: _buildTheme(Brightness.dark),
      // The reader lives inside RTL Directionality per-screen; app-level locale
      // covers EN/TR UI chrome (spec §3.1 bilingual gloss).
      // TODO(spike): supportedLocales: [Locale('en'), Locale('tr'), Locale('ar')]
      home: const _SpikeHome(),
    );
  }

  ThemeData _buildTheme(Brightness brightness) {
    return ThemeData(
      brightness: brightness,
      useMaterial3: true,
      // Bundled font — declared in pubspec.yaml, shipped in assets/fonts/.
      fontFamily: 'NotoNaskhArabic',
      colorSchemeSeed: const Color(0xFF0E7C74),
    );
  }
}

/// Placeholder home. The real app routes:
///   Library (LibraryScreen) → Reader (ReaderScreen) → WordSheet
///   plus GrammarReference, Deck/Review, Games — see architecture doc §"Screen map".
class _SpikeHome extends StatelessWidget {
  const _SpikeHome();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Qissa (spike)')),
      body: const Center(
        child: Padding(
          padding: EdgeInsets.all(24),
          child: Text(
            'Qissa Flutter architecture spike.\n'
            'Not a runnable app. See docs/05-flutter-architecture.md and '
            'lib/reader/reader_screen.dart for the tap-word RTL approach.',
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}
