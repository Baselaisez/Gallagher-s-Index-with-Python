/// UN-COMPILED SPIKE — design + skeleton only. See docs/05-flutter-architecture.md.
///
/// Maps `<story-id>/morphology.json` — Emsile/Bina-style verb paradigms keyed by
/// `lex`, powering the Sarf (صَرْف) conjugation tab of the word sheet.
/// Field names verified against:
///   content/samples/wasiyyat-abi-hanifa/morphology.json
library;

/// The morphology file: a top-level `comment` (documents cell ordering) plus a
/// `verbs` object mapping `lex` → VerbParadigm.
class Morphology {
  final String comment; // human note on the 14-cell / 6-cell ordering
  final Map<String, VerbParadigm> verbs;

  const Morphology({required this.comment, required this.verbs});

  VerbParadigm? operator [](String lex) => verbs[lex];

  factory Morphology.fromJson(Map<String, dynamic> json) {
    final raw = (json['verbs'] as Map<String, dynamic>?) ?? const {};
    return Morphology(
      comment: json['comment'] as String? ?? '',
      verbs: {
        for (final e in raw.entries)
          e.key: VerbParadigm.fromJson(e.value as Map<String, dynamic>),
      },
    );
  }
}

/// One verb's full paradigm.
///
/// Cell ordering (from the file's `comment`), 14 cells for mazi & mudari:
///   0 هو  1 هما(m)  2 هم  | 3 هي  4 هما(f)  5 هنّ
///   6 أنتَ 7 أنتما(m) 8 أنتم | 9 أنتِ 10 أنتما(f) 11 أنتنّ | 12 أنا  13 نحن
/// Amr is 6 cells: مخاطب (m sing/dual/plural) then مخاطبة (f sing/dual/plural).
class VerbParadigm {
  final String bab; // "مِنْ بَابِ ضَرَبَ يَضْرِبُ" — the verb's chapter/class
  final String wazn; // "فَعَلَ يَفْعِلُ" — the pattern
  final String masdar; // verbal noun, e.g. "رُجُوع"
  final String ismFail; // active participle, e.g. "رَاجِع"   (JSON key: ismFail)
  final String? ismMaful; // passive participle, e.g. "مَرْجُوع"; may be null (JSON key: ismMaful)
  final String? irregularity; // "hollow" | "hollow-wawi" | "defective-yai"; may be absent
  final List<String> mazi; // 14 cells (past)
  final List<String> mudari; // 14 cells (present)
  final List<String> amr; // 6 cells (imperative)
  final String? note; // pedagogical note shown under the table; may be absent

  const VerbParadigm({
    required this.bab,
    required this.wazn,
    required this.masdar,
    required this.ismFail,
    required this.ismMaful,
    required this.irregularity,
    required this.mazi,
    required this.mudari,
    required this.amr,
    required this.note,
  });

  static List<String> _cells(dynamic raw) => (raw as List<dynamic>? ?? const [])
      .map((e) => e == null ? '' : e as String)
      .toList(growable: false);

  factory VerbParadigm.fromJson(Map<String, dynamic> json) {
    return VerbParadigm(
      bab: json['bab'] as String? ?? '',
      wazn: json['wazn'] as String? ?? '',
      masdar: json['masdar'] as String? ?? '',
      ismFail: json['ismFail'] as String? ?? '',
      ismMaful: json['ismMaful'] as String?, // can be JSON null (e.g. takallama)
      irregularity: json['irregularity'] as String?,
      mazi: _cells(json['mazi']),
      mudari: _cells(json['mudari']),
      amr: _cells(json['amr']),
      note: json['note'] as String?,
    );
  }
}
