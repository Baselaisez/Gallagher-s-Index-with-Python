#!/usr/bin/env python3
"""v360-Sh — make every stored Shudhūr rule the author's own sentence (idempotent).

  python3 tools/ledger/shudhur2_verbatim.py          # apply tools/ledger/shudhur2_quotes.json to the jsonl and the old ledger; report

- research/sources/shudhur-al-dhahab-qawaid.jsonl (OUR extraction, not the received matn): every row gains `quote_ar` (the web text's
  words, segments joined « … », exactly as the e-text gives them), `web_page` / `web_pages` (al-Daqr's printed page) and `shamela`. Where
  the old `rule_ar` was not in the web text letter for letter (or empty), `rule_ar` becomes the quote and the old wording is kept as
  `rule_ar_v1` (ours, superseded); `quote_note` carries the hand judgement (more / less than the book / absent).
- content/rules/coverage_shudhur.json: the R rows' `ar` follows the new `rule_ar` (old kept as `ar_v1`, ids and statuses untouched),
  plus `web_page`; the S rows (the received matn, never changed) gain `web_reading` where the web text reads otherwise (S41, S49, S51).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shudhur2_common as C
R = C.ROOT
JL = os.path.join(R, 'research/sources/shudhur-al-dhahab-qawaid.jsonl')
COV = os.path.join(R, 'content/rules/coverage_shudhur.json')
Q = {o['n']: o for o in json.load(open(os.path.join(R, 'tools/ledger/shudhur2_quotes.json'), encoding='utf-8'))['quotes']}
WEB_READING = {   # the received matn's three readings the web text gives otherwise (letters as the e-text prints them)
    'S41': 'وَألْحق بِهِ اثْنَتَانِ وثنتان مُطلقًا',
    'S49': 'وَأما نَحْو {أتحاجوني} فالمحذوف نون الْوِقَايَة',
    'S51': 'وَنَحْو {إِنَّه من يتق ويصبر} مؤول',
}
raw = open(C.WEB, encoding='utf-8').read()
rows = [json.loads(l) for l in open(JL, encoding='utf-8') if l.strip()]
before = sum(1 for r in rows if (r.get('rule_ar_v1', r['rule_ar'])) and C.is_verbatim_quote(r.get("rule_ar_v1", r["rule_ar"])))
for n, r in enumerate(rows, 1):
    q = Q[n]
    for s in q['segments']: assert s['text'] in raw, (n, s['text'][:40])
    orig = r.get('rule_ar_v1', r['rule_ar'])
    if q['segments']:
        r['quote_ar'] = ' … '.join(s['text'] for s in q['segments'])
        r['web_page'] = q['segments'][0]['web_page']; r['web_pages'] = sorted({s['web_page'] for s in q['segments']})
        r['shamela'] = q['segments'][0]['shamela']
        if not (orig and C.is_verbatim_quote(orig)):
            r['rule_ar_v1'] = orig; r['rule_ar'] = r['quote_ar']
    if q.get('note'): r['quote_note'] = q['note']
with open(JL, 'w', encoding='utf-8') as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')
after = sum(1 for r in rows if r["rule_ar"] and C.is_verbatim_quote(r["rule_ar"]))
cov = json.load(open(COV, encoding='utf-8'))
for e in cov['entries']:
    if e['id'].startswith('R'):
        r = rows[e['jsonl'] - 1]
        new = r['rule_ar'] or ' ، '.join(r['examples'])
        if new != e['ar']:
            e.setdefault('ar_v1', e['ar']); e['ar'] = new
        if 'web_page' in r: e['web_page'] = r['web_page']
    elif e['id'] in WEB_READING:
        assert C.is_verbatim(WEB_READING[e['id']]) or WEB_READING[e['id']] in raw, e['id']
        e['web_reading'] = WEB_READING[e['id']]
json.dump(cov, open(COV, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
ex = [x for r in rows for x in r['examples']]
print('rule_ar verbatim (letters, in the web text): %d of 210 before → %d after; absent %d (%s)' % (
    before, after, sum(1 for q in Q.values() if q['mode'] == 'absent'), ', '.join('R%d' % n for n, q in Q.items() if q['mode'] == 'absent')))
print('ledger R rows ar verbatim: %d of %d; examples verbatim %d of %d (the rest: vowelled cuts / readings, listed in the report)' % (
    sum(1 for e in cov['entries'] if e['id'].startswith('R') and C.is_verbatim_quote(e["ar"])), sum(1 for e in cov['entries'] if e['id'].startswith('R')),
    sum(1 for x in ex if C.is_verbatim(x)), len(ex)))
