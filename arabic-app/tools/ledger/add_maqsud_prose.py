#!/usr/bin/env python3
"""v345-Q — al-Maqṣūd's open Ottoman units the engines do not apply go into the ṣarf note of their chapter, as an example that quotes
the book VERBATIM: `ar` = the unit as the ledger cut it from research/sources/maqsud-sarf.txt (asserted against the file here), `matn` =
the Arabic words the print vowels inside it, verbatim, `source` = «maqsud-sarf.txt:<line>[–<line>]», and `en` / `tr` = OUR renderings
(tools/ledger/maqsud_renderings.json), each marked as awaiting the hoca's review. Units that are headings, a ḥadīth's meaning or the
teacher's advice go to the plan's not_auto with the reason.

    python3 tools/ledger/add_maqsud_prose.py [--dry]      (idempotent; run tools/ledger/sarf_ledger.py after it)
"""
import json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
G = os.path.join(ROOT, 'content', 'grammar')
EN_MARK, TR_MARK = " [translation · awaiting the hoca's review]", ' [çeviri · hoca onayı bekliyor]'
HAR = re.compile('[ً-ْ]')
def matn_words(t): return [w for w in dict.fromkeys(re.findall(r'[ء-ْٰٱﺏ-ﻼ]+', t)) if len(HAR.findall(w)) >= 2]
def main():
    dry = '--dry' in sys.argv
    R = json.load(open(os.path.join(ROOT, 'tools', 'ledger', 'maqsud_renderings.json'), encoding='utf8'))
    cov = {e['id']: e for e in json.load(open(os.path.join(ROOT, 'content', 'rules', 'coverage_maqsud.json'), encoding='utf8'))['entries']}
    L = open(os.path.join(ROOT, 'research', 'sources', 'maqsud-sarf.txt'), encoding='utf8').read().split('\n')
    notes, added = {}, {}
    for eid, r in R['units'].items():
        e = cov.get(eid)
        if not e: print('no entry', eid); continue
        lines = e.get('lines') or [e['line']]
        assert e['ar'] == '\n'.join(L[n - 1].strip() for n in lines), eid          # verbatim, by line
        src = 'maqsud-sarf.txt:' + (f'{lines[0]}–{lines[-1]}' if len(lines) > 1 else str(lines[0]))
        nid = r['note']; N = notes.get(nid) or notes.setdefault(nid, json.load(open(os.path.join(G, nid + '.json'), encoding='utf8')))
        if any((x.get('source') or '') == src for x in N['examples']): continue
        if e['status'] != 'open': print('not open (left):', eid, e['status']); continue
        ex = {'ar': e['ar'], 'en': r['en'] + EN_MARK, 'tr': r['tr'] + TR_MARK, 'source': src}
        mw = matn_words(e['ar'])
        if mw: ex['matn'] = mw
        N['examples'].append(ex); added[nid] = added.get(nid, 0) + 1
    planp = os.path.join(ROOT, 'content', 'rules', 'sarf_ledger_plan.json'); plan = json.load(open(planp, encoding='utf8'))
    for eid, why in R['not_auto'].items():
        assert eid in cov, eid
        plan.setdefault('not_auto', {})[eid] = why
    print('added', added, sum(added.values()), '; not automatable', len(R['not_auto']))
    if dry: return
    for nid, n in notes.items():
        json.dump(n, open(os.path.join(G, nid + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=2)
        open(os.path.join(G, nid + '.json'), 'a', encoding='utf8').write('\n')
    json.dump(plan, open(planp, 'w', encoding='utf8'), ensure_ascii=False, indent=1); open(planp, 'a', encoding='utf8').write('\n')
if __name__ == '__main__':
    main()
