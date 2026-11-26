#!/usr/bin/env python3
"""v342-N — the naḥw books' ledger, built by script from the sources.

  python3 tools/ledger/build_ledger.py            # cut the entries, prove every probe in prototype/reader.html, write
                                                  # content/rules/coverage_{shudhur,qawaid_al_irab,izhar,kafiya}.json and
                                                  # research/book-coverage-2026-11-27.nahw.md
  python3 tools/ledger/build_ledger.py --no-prove # reuse the last proof (tools/ledger/.proof-cache.json) — for a quick re-render

Status of an entry (one, in this order): applied — it has probes and every one passes in the page (the engine and rule named in
carried_by); noted — a grammar note quotes it (its example's `source` names this line, or ≥ 5 of its words stand verbatim in the
note's Arabic); not-automatable — the map gives the reason; open — none of these. Headings, fragments of the lecture and cited
verses are counted apart (kind heading / fragment / example). The smoke check «v342 — the ledger …» re-proves every applied entry.
"""
import json, glob, os, re, subprocess, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'research', 'sources')
HERE = os.path.dirname(os.path.abspath(__file__))
HARAKAT = re.compile('[ً-ْٰـ]')
def letters(s): return re.sub('[^ء-ي ]', ' ', HARAKAT.sub('', s or '')).split()
def norm(w): return w.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ى', 'ي').replace('ة', 'ه')

def load_map(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

# ── the notes: anchors and Arabic, for «noted»
NOTES = {}
for f in glob.glob(os.path.join(ROOT, 'content', 'grammar', '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    ex = d.get('examples', []) or []
    NOTES[d['id']] = {
        'sources': [e.get('source', '') for e in ex],
        'stories': [(e.get('sourceStory'), str(e.get('chapter')), e.get('sentence')) for e in ex if e.get('sourceStory')],
        'words': [[norm(w) for w in letters(e.get('ar', ''))] for e in ex],
    }
def noted_by(file, line, ar, story=None, jsonl_n=None, grams_ok=True):
    hit = []
    tag = '%s:%d' % (file, line) if line else None
    for nid, n in NOTES.items():
        ok = False
        for s in n['sources']:
            if tag and re.search(re.escape(tag) + r'(?!\d)', s): ok = True
            if jsonl_n and re.search(r'shudhur-al-dhahab-qawaid\.jsonl:%d(?!\d)' % jsonl_n, s): ok = True
        if story and story in n['stories']: ok = True
        if not ok and grams_ok:
            w = [norm(x) for x in letters(ar)]
            k = 5
            if len(w) >= k:
                grams = {tuple(w[i:i + k]) for i in range(len(w) - k + 1)}
                for ew in n['words']:
                    if any(tuple(ew[i:i + k]) in grams for i in range(len(ew) - k + 1)): ok = True; break
        if ok: hit.append(nid)
    return sorted(hit)

# ── the entries, cut from each source
def shudhur_entries():
    src = open(os.path.join(SRC, 'shudhur-al-dhahab-src.txt'), encoding='utf-8').read().split('\n')
    out = []
    for i, l in enumerate(src[:56], 1):          # part one (bābs 1–7), the matn's own lines
        if l.strip() and not l.startswith('#'):
            out.append({'id': 'S%d' % i, 'line': i, 'ar': l.strip(), 'kind': 'rule', 'file': 'research/sources/shudhur-al-dhahab-src.txt'})
    page_line = {}
    for i, l in enumerate(src, 1):
        m = re.match(r'# page (\d+)(?:-(\d+))?', l)
        if m and i > 56:
            a = int(m.group(1)); b = int(m.group(2) or a)
            j = i
            while j < len(src) and (not src[j].strip() or src[j].startswith('#')): j += 1
            for p in range(a, b + 1): page_line.setdefault(p, j + 1)
    pages = sorted(page_line)
    for n, l in enumerate(open(os.path.join(SRC, 'shudhur-al-dhahab-qawaid.jsonl'), encoding='utf-8'), 1):
        r = json.loads(l); p = r['page']
        near = max([q for q in pages if q <= p] or [pages[0]])
        ar = r['rule_ar'] or ' ، '.join(r['examples'])
        out.append({'id': 'R%d' % n, 'line': page_line[near], 'page': p, 'ar': ar, 'kind': 'rule', 'jsonl': n,
                    'file': 'research/sources/shudhur-al-dhahab-src.txt', 'en': r['rule_en'], 'bab': r['bab'], 'own_example': bool(r['examples']), 'ar_is_examples': not r['rule_ar']})
    return out

def qawaid_entries():
    src = open(os.path.join(SRC, 'qawaid-al-irab-ibn-hisham-matn.txt'), encoding='utf-8').read().split('\n')
    out = []
    for i, l in enumerate(src, 1):
        if i < 28 or i > 453 or not l.strip() or l.startswith('#') or l.startswith('==') or l.startswith('--'): continue
        body = re.sub(r'\[[^\]]*\]', ' ', l).strip()
        if not re.search('[ء-ي]', body): continue
        kind = 'example' if not l.startswith('[') else 'rule'
        out.append({'id': 'Q%d' % i, 'line': i, 'ar': body, 'kind': kind, 'file': 'research/sources/qawaid-al-irab-ibn-hisham-matn.txt'})
    return out

def izhar_entries(M):
    src = open(os.path.join(SRC, 'izhar-al-asrar-matn-lithograph.txt'), encoding='utf-8').read().split('\n')
    def sents(n): return re.split(r'(?<=[.])\s+', re.sub(r'^\[[٠-٩]+\]\s*', '', src[n - 1]))
    out = []
    for k, v in M.items():
        if v['kind'] == 'cond':
            ln, j = map(int, k.split('.')); ar = sents(ln)[j]
        else:
            ln = v['line']; key = [norm(w) for w in letters(v['ar'])]; ar = None
            for s in sents(ln):
                ws = [norm(w) for w in letters(s)]
                if all(any(x == y or x == 'ال' + y or y == 'ال' + x for y in ws) for x in key[:1]): ar = s; break
            ar = ar or sents(ln)[0]
        out.append({'id': 'I-' + k, 'line': v['line'], 'ar': ar.strip(), 'item': v['ar'], 'kind': v['kind'], 'file': 'research/sources/izhar-al-asrar-matn-lithograph.txt'})
    return out

KAF_RE = re.compile(r'(^| )(و|ف)?(شرطه|شرطها|شرط|يجب|يجوز|يمتنع|وجب|جاز|امتنع|يلزم|لزم)( |$)')
KAF_DEF = re.compile(r'^(و)?\S+( \S+)? (ما|وهو ما|هو ما|وهي ما) | ما (يدل|كان|يقبل|اشتمل|وقع|حذف|بني|ذكر)')
def kafiya_entries(DIGEST):
    out = []
    fs = sorted(glob.glob(os.path.join(ROOT, 'content/samples/al-kafiya/chapters/*.json')), key=lambda x: int(re.findall(r'(\d+)\.json', x)[0]))
    for f in fs:
        d = json.load(open(f, encoding='utf-8'))
        for s in d['sentences']:
            b = ' '.join(t['surface']['bare'] for t in s['tokens'])
            kind = 'ruling' if KAF_RE.search(b) else 'definition' if KAF_DEF.search(b) else None
            if not kind: continue
            full = ' '.join(t['surface']['full'] for t in s['tokens'])
            out.append({'id': 'K%d:%s' % (d['chapter'], s['id']), 'line': '%d:%s' % (d['chapter'], s['id']), 'ar': full, 'kind': kind,
                        'file': 'content/samples/al-kafiya/chapters/%d.json' % d['chapter'], 'story': ('al-kafiya', str(d['chapter']), s['id'])})
    dg = open(os.path.join(SRC, 'kafiya-internet-digest.txt'), encoding='utf-8').read().split('\n')
    heads = sorted(DIGEST)
    for n in heads:
        nxt = min([h for h in heads if h > n] or [n + 6]); block = dg[n - 1:min(nxt - 1, n + 7)]
        ar = ' … '.join(m.strip() for l in block for m in re.findall(r'[ء-ي][ء-ْٰ ]*[ء-ْٰ]', l) if len(m.split()) >= 2)
        out.append({'id': 'D%d' % n, 'line': n, 'ar': ar, 'tr': DIGEST[n], 'kind': 'section', 'file': 'research/sources/kafiya-internet-digest.txt'})
    return out

BOOKS = [
    ('shudhur', 'Shudhūr al-Dhahab (Ibn Hishām)', 'research/sources/shudhur-al-dhahab-qawaid.jsonl + shudhur-al-dhahab-src.txt', 'shudhur_map'),
    ('qawaid_al_irab', 'Qawāʿid al-Iʿrāb (Ibn Hishām)', 'research/sources/qawaid-al-irab-ibn-hisham-matn.txt', 'qawaid_map'),
    ('izhar', 'Iẓhār al-Asrār (Birgivī)', 'research/sources/izhar-al-asrar-matn-lithograph.txt', 'izhar_map'),
    ('kafiya', 'al-Kāfiya (Ibn al-Ḥājib)', 'content/samples/al-kafiya (the matn on the shelf) + research/sources/kafiya-internet-digest.txt', 'kafiya_map'),
]
APART = ('heading', 'fragment', 'example')

def mapkey(book, e):
    if book == 'shudhur': return int(e['id'][1:]) if e['id'].startswith('R') else 'p1:%d' % e['line']
    if book == 'qawaid_al_irab': return e['line']
    if book == 'izhar': return e['id'][2:]
    return e['id'][1:] if e['id'].startswith('K') else e['id']

# (v351-I) the writer's rules the Iẓhār course puts to the learner (content/rules/izhar_map.json «writer»): the reader's engine cannot meet a
# rule about what is NOT said, the learner can — the row keeps its status and names the course as a carrier
try: COURSE351 = {w['rule'] for w in json.load(open(os.path.join(ROOT, 'content', 'rules', 'izhar_map.json'), encoding='utf-8')).get('writer', [])}
except Exception: COURSE351 = set()

def main():
    prove = '--no-prove' not in sys.argv
    books = []
    for key, title, srcname, mapname in BOOKS:
        mm = load_map(mapname); M = mm.M
        ents = {'shudhur': shudhur_entries, 'qawaid_al_irab': qawaid_entries}.get(key)
        ents = ents() if ents else izhar_entries(M) if key == 'izhar' else kafiya_entries(mm.DIGEST)
        for e in ents: e['map'] = M.get(mapkey(key, e), {})
        books.append((key, title, srcname, ents))
    probes = [p for _, _, _, ents in books for e in ents for p in e['map'].get('probes', [])]
    cache = os.path.join(HERE, '.proof-cache.json')
    if prove:
        pin = os.path.join(HERE, '.probes.json'); json.dump(probes, open(pin, 'w'), ensure_ascii=False)
        subprocess.run(['node', os.path.join(HERE, 'prove.js'), pin, cache], check=True); os.remove(pin)
    res = json.load(open(cache)); assert len(res) == len(probes), 'proof cache is stale: run without --no-prove'
    k = 0
    for key, title, srcname, ents in books:
        rows = []
        for e in ents:
            m = e.pop('map'); ps = []
            for p in m.get('probes', []): ps.append(dict(p, ok=res[k]['ok'], got=res[k]['got'][:160])); k += 1
            notes = noted_by(e['file'], e['line'] if isinstance(e['line'], int) else None, e['ar'], e.get('story'), e.get('jsonl'), grams_ok=not e.get('ar_is_examples'))
            carried = []
            if ps and all(p['ok'] for p in ps): carried.append('engine:' + m.get('eng', 'Murib.line'))
            carried += ['note:' + n for n in notes]
            if key == 'izhar' and e['id'] in COURSE351: carried.append('course:izhar351 · يُقَالُ / لَا يُقَالُ')   # (v351-I) the learner judges the book's examples
            kind = m.get('kind', e['kind'])
            if kind in APART: status = kind
            elif ps and all(p['ok'] for p in ps): status = 'applied'
            elif notes: status = 'noted'
            elif m.get('na'): status = 'not-automatable'
            else: status = 'open'
            row = {k2: e[k2] for k2 in ('id', 'line', 'ar') }
            row.update({'kind': kind, 'carried_by': carried, 'status': status})
            for k2 in ('page', 'en', 'tr', 'item', 'jsonl'):
                if k2 in e: row[k2] = e[k2]
            if m.get('na'): row['reason'] = m['na']
            if ps: row['probes'] = ps
            if m.get('eng') and status != 'applied': row['engine_hint'] = m['eng']
            rows.append(row)
        counts = {s: sum(1 for r in rows if r['status'] == s) for s in ('applied', 'noted', 'not-automatable', 'open') + APART}
        out = {'book': title, 'source_file': srcname, 'built_by': 'tools/ledger/build_ledger.py', 'counts': counts, 'entries': rows}
        json.dump(out, open(os.path.join(ROOT, 'content', 'rules', 'coverage_%s.json' % key), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(key, counts)
    render(books)

def render(books):
    L = ['# The naḥw books\' ledger — v342-N (2026-11-27)', '',
         'Every rule / section of Shudhūr al-Dhahab, Qawāʿid al-Iʿrāb, Iẓhār al-Asrār and al-Kāfiya, cut by `tools/ledger/build_ledger.py`',
         'from the sources and joined with the maps beside it (`tools/ledger/*_map.py`). **applied** = the book\'s own example (or, where it',
         'prints none, the shortest school phrase) read by the engine named, every probe passing in the built page; **noted** = a grammar note',
         'quotes or anchors it; **not-automatable** = the reason is given; **open** = none of these. The smoke check «v342 — the ledger …»',
         're-proves every applied entry and pins the counts. JSON: `content/rules/coverage_<book>.json`.', '']
    for key, title, srcname, _ in books:
        d = json.load(open(os.path.join(ROOT, 'content', 'rules', 'coverage_%s.json' % key), encoding='utf-8'))
        c = d['counts']; rows = d['entries']
        L += ['## ' + title, '', 'Source: `%s`. Entries: %d — applied **%d**, noted **%d**, not automatable **%d**, open **%d** (headings %d, lecture fragments %d, cited verses %d, counted apart).' % (
            srcname, len(rows), c['applied'], c['noted'], c['not-automatable'], c['open'], c['heading'], c['fragment'], c['example']), '',
            '| id | line | status | carried by / reason | the book |', '|---|---|---|---|---|']
        for r in rows:
            if r['status'] in APART: continue
            why = ', '.join(r['carried_by']) or r.get('reason', '') or ('engine to build: ' + r.get('engine_hint', '') if r.get('engine_hint') else '')
            if r['status'] == 'noted' and any(not p['ok'] for p in r.get('probes', [])):
                bad = [p for p in r['probes'] if not p['ok']][0]
                why += ' — ⚠ the engine still misreads the example: «%s» → %s' % (bad.get('s', bad.get('js', ''))[:50], bad['got'][:60])
            if r['status'] == 'open' and r.get('probes'):
                bad = [p for p in r['probes'] if not p['ok']][:1]
                if bad: why += (' — ' if why else '') + 'probe «%s» → %s' % (bad[0].get('s', bad[0].get('js', ''))[:60], bad[0]['got'][:70])
            ar = (r['ar'] or r.get('tr', ''))[:90].replace('|', '/')
            L.append('| %s | %s | %s | %s | %s |' % (r['id'], r['line'], r['status'], why.replace('|', '/'), ar))
        L.append('')
        if key == 'qawaid_al_irab': L += word_table(rows)
    open(os.path.join(ROOT, 'research', 'book-coverage-2026-11-27.nahw.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

def word_table(rows):
    # bāb 3: the faces the matn counts for each word against WujuhEngine.WORDS (read from the page's code) and the faces the matn's own
    # examples prove in the page (a WujuhEngine probe of this ledger that passes)
    code = open(os.path.join(ROOT, 'prototype', 'reader.html'), encoding='utf-8').read(); code = code[:code.find('// __DATA_START__')]
    W = {m.group(1): (int(m.group(3)), [x.strip().strip('"') for x in m.group(4).split(',') if x.strip()]) for m in re.finditer(r'\n\s+(\w+):\s*\{ ar: "([^"]+)",\s*n: (\d+), faces: \[([^\]]*)\]', code)}
    proved = {}
    for r in rows:
        for p in r.get('probes', []):
            m = re.search(r'x\.key === "(\w+)" && x\.face === "(\w+)"', p.get('js', ''))
            if m: proved.setdefault(m.group(1), {})[m.group(2)] = proved.get(m.group(1), {}).get(m.group(2), False) or p['ok']
    T = load_map('qawaid_map').WORDTABLE
    out = ['### Bāb 3 word by word — the matn\'s count of faces against `WujuhEngine.WORDS`', '',
           '| word | matn lines | faces the matn states | engine n | engine faces | matn examples read right / tried |', '|---|---|---:|---:|---|---|']
    for ar, k, n, ln in T:
        en, fc = W.get(k, (0, []))
        pr = proved.get(k, {})
        out.append('| %s | %s | %d | %d%s | %s | %d / %d %s |' % (ar, ln, n, en, '' if en == n else ' ≠', ', '.join(fc), sum(1 for v in pr.values() if v), len(pr),
                   ('(' + ', '.join(f for f, v in pr.items() if not v) + ' not yet)') if any(not v for v in pr.values()) else ''))
    return out + ['']

if __name__ == '__main__':
    main()
