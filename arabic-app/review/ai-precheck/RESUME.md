# Where the AI pre-check stands (2026-11-17)

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
