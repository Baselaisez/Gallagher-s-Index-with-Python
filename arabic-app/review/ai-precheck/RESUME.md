# Where the AI pre-check stands (2026-11-17, after wave 2)

**Stopped: the Fable 5.2 usage limit was reached before any verdict was written** («resets Nov 19, 3am UTC»).
Nothing in the content has changed on this branch; the student sheets are on hold.

Ready:
- `review/ai-precheck/findings-critical.json` — the 1,297 critical findings (ids, sheet and row unchanged).
- `tools/precheck.py packets` rebuilds the 43 work packets (17 pattern packets D01–D12, then 26 by package,
  engine sources first); `check` enforces the citation rule; `status` prints the resume point.
- `review/ai-precheck/BRIEF.md` — the verifier's brief (verdicts, citation rule, sources).
- `tools/precheck_apply.py` — writes checked AI-ONAY corrections (dry run by default); AI-RET goes to
  `ai-rejections.jsonl` with `confirmed_by_human: false`, which `--learn-from-rejections` ignores.
- `baseline-before.txt` — the gauges before any change: label gauge 90.31 % (32,470 / 35,953), typed gauge 99.92 %
  (1,214 / 1,215), every package validates, drill bank 9,217 rows.

Resume order (once Fable 5.2 answers again):
1. Wave 1 — p-D02-1, p-D02-2, p-D08 + p-D11 + p-D12, p-D03, p-D01-1, p-D01-2.
2. Wave 2 — p-D04-1, p-D04-2, p-D05-1, p-D05-2, p-D06, p-D07.  Wave 3 — p-D09, p-D10-1, p-D10-2.
3. Confirmed patterns → line-level rule passes (taṣrīf/iʿlāl before iʿrāb) through `pkg_from_engine.py` / `polish_pkg.py`,
   rerun on every package, validators + gauges compared with the baseline.
4. The 26 package packets (r01–r26), al-usul-al-munifa first.
5. Sheets 01–17 regenerated with the AI columns; final report.

## Progress (Opus 5.5 by the owner's decision; weekly cap 85 %)

- Wave 1 (D01, D02, D03, D08, D11, D12) and wave 2 (D04, D05, D06, D07) are done: 428 of 1,297 verified.
  Verdicts: see `python3 tools/precheck.py check` (total line). Cost: about 1.5 M + 1.15 M subagent tokens
  (wave 1 moved the weekly meter 67 % → 74 %).
- Next: wave 3 = p-D09, p-D10-1, p-D10-2; then the package packets r01–r26 (al-usul-al-munifa first).
- Rule fixes (from the verifiers' reports): D03, D11, D12 deterministic; D06 deterministic by the glossary lemma;
  D08 for يـ/أ/نـ only; D07 for a bare بْن between names; D02, D04 partial; D01, D05 flag only.
