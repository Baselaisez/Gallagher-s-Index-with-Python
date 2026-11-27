#!/usr/bin/env python3
"""(v360-Sh) Sharḥ Shudhūr al-Dhahab from the web text — the toc of the whole book and the ledger of the half never scanned.

  python3 tools/ledger/shudhur2_ledger.py            # toc + ledger, prove in prototype/reader.html (aqil_prove.js / aqil_probe.js)
  python3 tools/ledger/shudhur2_ledger.py --no-prove # reuse tools/ledger/.shudhur2-proof-cache*.json

Source: research/sources/sharh-shudhur-al-dhahab-src.txt (Shamela 6969, ed. al-Daqr; `web_page` = THAT edition's printed page — the
owner's print pages differ: the owner's scans stop inside «عمل الفعل», which is this edition's p. 455).
- `content/rules/toc_shudhur_sharh.json`: every matn passage («قلت / ثمَّ قلت …», the author's own matn inside his sharḥ) with its bāb,
  web page, Shamela page and first words; the bābs with their page spans («ثمَّ قلت بَاب …»); per bāb the count of rules in the old
  ledger (`shudhur-al-dhahab-qawaid.jsonl`, owner pages mapped by the matn anchors) — the thin ones are named.
- `content/rules/coverage_shudhur_sharh.json` (a SIBLING ledger: the old one's ids «Shudhūr R<n>» stay): one entry per RULE STATEMENT
  of the unread half (web pp. 455–602: عمل الفعل, the ten nouns that work like the verb, tanāzuʿ, ishtighāl, the five tawābiʿ and the
  vocative's follower, the barriers to tanwīn, the numbers) — a sentence of the matn or the sharḥ (not a shāhid line, not an āya alone)
  with a ruling marker AND its example (نحو / تقول / كقولك), cut by aqil_ledger's own markers; the example cut where the commentary
  resumes. Status, in this order (as v352-A):
    joined           — the same rule in the Shudhūr (old) / Qawāʿid / Iẓhār / Kāfiya / Ibn ʿAqīl ledgers (same topic, same example
                       or ≥ 3 shared content words, Jaccard ≥ .3): it inherits that entry's status;
    not-automatable  — poetic licence / rarity, a school's view, a dialect, a matter of meaning (marker in `reason`);
    applied          — the book's example (as printed) through SentenceAnalyzer + Murib.line names the ruling; -offered when the line
                       gives it beside another reading; -vowelled when only our test vowels (`sv`, never shown) read it;
    open ⚠           — the engine misreads the book's example (`got` beside the book's sentence);
    open             — no construction the iʿrāb line names / a single word cited.
  Triage by hand: tools/ledger/shudhur2_overrides.json ({id: {cls, why, probes | status+reason}} — the v355 shape).
"""
import json, os, re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shudhur2_common as C  # noqa: E402
import aqil_ledger as AL  # noqa: E402  (the markers, the example cutter, the join, the named roles)
from aqil_map import B as AQB  # noqa: E402

ROOT = Path(C.ROOT)
REL = 'research/sources/sharh-shudhur-al-dhahab-src.txt'
TOC = ROOT / 'content/rules/toc_shudhur_sharh.json'
OUT = ROOT / 'content/rules/coverage_shudhur_sharh.json'
CACHE, CACHE_SV = HERE / '.shudhur2-proof-cache.json', HERE / '.shudhur2-proof-cache-sv.json'
OVR = json.loads((HERE / 'shudhur2_overrides.json').read_text(encoding='utf-8')) if (HERE / 'shudhur2_overrides.json').exists() else {}
UNREAD_FROM = 455   # this edition's page of «ثمَّ قلت بَاب فِي عمل الْفِعْل» — where the owner's scans stop

# the unread half's passages → the Ibn ʿAqīl bāb whose topics / construction they share (aqil_map.B), by the passage's opening words
SEC = [  # (key of the passage's first words, name, aqil bāb)
    ('ثم قلت باب في عمل الفعل', 'عمل الفعل: اللازم والمتعدي', 'تعدي الفعل ولزومه'),
    ('ثم قلت ولا يجوز حذف مفعول في باب ظن', 'عمل الفعل: حذف المفعول، والإلغاء والتعليق', 'ظن وأخواتها'),
    ('ثم قلت باب الاسماء التي تعمل عمل الفعل', 'الأسماء العاملة: المصدر', 'إعمال المصدر'),
    ('ثم قلت الثاني اسم الفاعل', 'الأسماء العاملة: اسم الفاعل', 'إعمال اسم الفاعل'),
    ('ثم قلت الثالث المثال', 'الأسماء العاملة: أمثلة المبالغة', 'إعمال اسم الفاعل'),
    ('ثم قلت الرابع اسم المفعول', 'الأسماء العاملة: اسم المفعول', 'إعمال اسم الفاعل'),
    ('ثم قلت وشرطهما كاسم الفاعل', 'الأسماء العاملة: اسم المفعول', 'إعمال اسم الفاعل'),
    ('ثم قلت الخامس الصفة المشبهة', 'الأسماء العاملة: الصفة المشبهة', 'الصفة المشبهة باسم الفاعل'),
    ('ثم قلت السادس اسم الفعل', 'الأسماء العاملة: اسم الفعل', 'أسماء الأفعال والأصوات'),
    ('ثم قلت السابع والثامن الظرف والمجرور', 'الأسماء العاملة: الظرف والمجرور المعتمدان', 'حروف الجر'),
    ('ثم قلت التاسع اسم المصدر', 'الأسماء العاملة: اسم المصدر', 'إعمال المصدر'),
    ('ثم قلت العاشر اسم التفضيل', 'الأسماء العاملة: اسم التفضيل', 'أفعل التفضيل'),
    ('ثم قلت واذا كان بال طابق', 'الأسماء العاملة: اسم التفضيل', 'أفعل التفضيل'),
    ('ثم قلت ولا يبني ولا ينقاس هو ولا افعال التعجب', 'التعجب', 'التعجب'),
    ('ثم قلت باب واذا تنازع', 'التنازع', 'التنازع في العمل'),
    ('ثم قلت باب اذا شغل فعلا', 'الاشتغال', 'اشتغال العامل عن المعمول'),
    ('ثم قلت باب يتبع ما قبله', 'التوابع: التوكيد', 'التوكيد'),
    ('ثم قلت الثاني النعت', 'التوابع: النعت', 'التوابع النعت'),
    ('ثم قلت الثالث عطف البيان', 'التوابع: عطف البيان', 'العطف'),
    ('ثم قلت الرابع البدل', 'التوابع: البدل', 'البدل'),
    ('ثم قلت الخامس عطف النسق', 'التوابع: عطف النسق', 'عطف النسق'),
    ('ثم قلت فصل واذا اتبع المنادي', 'التوابع: تابع المنادى', 'النداء'),
    ('ثم قلت باب موانع الصرف', 'موانع الصرف', 'ما لا ينصرف'),
    ('ثم قلت باب العدد', 'العدد', 'العدد'),
]
ROLE_OVR = {'حروف الجر': r'متعلق|ظرف|جار ومجرور|فاعل'}   # the working ẓarf / jārr: its doer or its attachment
SPLIT = re.compile(r' (?=(?:وَ|فَ)?(?:أما|أَما|أمّا|أَحدهَا|الثَّانِي|وَالثَّانِي|الثَّالِث|وَالثَّالِث|الرَّابِع|وَالرَّابِع|الْخَامِس|وَالْخَامِس|'
                   r'وَقَوْلِي|وَاحْترز|واحترزت|وَمِثَال|فَإِن قلت|قلت|وَمن ذَلِك|وَمِنْه|وَمن أَمْثِلَة) )')


def lines():
    """[(shamela, printed, idx_in_page, text)] of the whole web text"""
    out = []
    for sh, pr, sec, ls in C.P():
        for j, l in enumerate(ls):
            out.append((sh, pr, j, l))
    return out


def is_matn(l):
    k = C.key(l)
    return bool(re.match(r'(ثم )?قلت ', k)) or (k.startswith('باب ') and len(k.split()) > 8)   # the e-text drops «ثمَّ قلت» before «بَاب المنصوبات …»


def is_verse(l):
    return l.lstrip().startswith('(') and ('...' in l or '…' in l)


def build_toc(L):
    # the owner's pages of the old jsonl rules → web pages, by the received matn's own anchors (as the v360 quotes were placed)
    jl = [json.loads(x) for x in open(ROOT / 'research/sources/shudhur-al-dhahab-qawaid.jsonl', encoding='utf-8') if x.strip()]
    passages, babs = [], []
    cur = None
    for k, (sh, pr, j, l) in enumerate(L):
        if not is_matn(l):
            continue
        kk = C.key(l)
        w = kk.split(); o = 2 if kk.startswith('ثم ') else 1 if kk.startswith('قلت ') else 0
        if w[o] == 'باب':
            cur = {'bab': ' '.join(w[o:o + 5]), 'from_web_page': pr, 'shamela': sh, 'passages': 0}
            babs.append(cur)
        if cur is None:
            cur = {'bab': 'الكلمة وأقسامها (المقدمة)', 'from_web_page': pr, 'shamela': sh, 'passages': 0}
            babs.append(cur)
        cur['passages'] += 1
        passages.append({'n': len(passages) + 1, 'web_page': pr, 'shamela': sh, 'bab': cur['bab'], 'opens': ' '.join(l.split()[:9]),
                         'reply': kk.startswith('قلت ') and len(passages) > 0})
    for i, b in enumerate(babs):
        b['to_web_page'] = (babs[i + 1]['from_web_page'] if i + 1 < len(babs) else 602)
        b['pages'] = b['to_web_page'] - b['from_web_page'] + 1
        b['unread_half'] = b['from_web_page'] >= UNREAD_FROM
    # old rules per bāb (their quote's web page, set by v360's shudhur2_verbatim.py)
    for b in babs:
        b['old_ledger_rules'] = sum(1 for r in jl if r.get('web_page') and b['from_web_page'] <= r['web_page'] < max(b['to_web_page'], b['from_web_page'] + 1))
        b['rules_per_page'] = round(b['old_ledger_rules'] / max(1, b['pages']), 2)
    thin = [b['bab'] for b in babs if not b['unread_half'] and b['from_web_page'] >= 88 and b['pages'] >= 8 and b['rules_per_page'] < 0.6]   # part one (pp. 15–88) is ledgered by its matn lines (S rows)
    doc = {'book': 'Sharḥ Shudhūr al-Dhahab (Ibn Hishām) — the web text', 'source_file': REL, 'built_by': 'tools/ledger/shudhur2_ledger.py',
           'about': 'Bābs = the «ثمَّ قلت بَاب …» passages; passages = every «قلت / ثمَّ قلت» line (reply = a «قلت» answering «فَإِن قيل», not '
                    'matn). web_page = al-Daqr\'s printed page (NOT the owner\'s print). unread_half = from p. %d, where the owner\'s scans stop. '
                    'old_ledger_rules = rows of shudhur-al-dhahab-qawaid.jsonl whose verbatim quote stands in the bāb\'s span; thin = a bāb of '
                    '≥ 8 pages with < 0.6 old rules a page.' % UNREAD_FROM,
           'counts': {'babs': len(babs), 'passages': len(passages), 'matn_passages': sum(1 for p in passages if not p['reply'])},
           'babs': babs, 'thin_babs': thin, 'passages': passages}
    TOC.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
    return doc


def units(L):
    """the unread half cut into passages: (name, aqil bāb, [(k, line)])"""
    start = next(k for k, x in enumerate(L) if x[1] >= UNREAD_FROM and C.key(x[3]).startswith(SEC[0][0]))
    out, cur = [], None
    for k in range(start, len(L)):
        l = L[k][3]; kk = C.key(l)
        hit = next((s for s in SEC if kk.startswith(s[0])), None) if is_matn(l) else None
        if hit:
            cur = {'name': hit[1], 'aqil': hit[2], 'lines': []}
            out.append(cur)
        cur['lines'].append(k)
    return out


EXM2 = re.compile(r'(?:^|\s)(?:و?نحو|و?كقولك|فتقول|وتقول|تقول|ك(?= [^ ]))\s*:?\s+')   # + the e-text's detached kāf: «ك رطل زيتا»
STOP2 = {'اي', 'فان', 'لان', 'لانه', 'لانها', 'فانه', 'فانها', 'قال', 'وقال', 'واما', 'فاما', 'ولم', 'وكذلك', 'كذلك', 'بخلاف', 'وقوله', 'قوله',
         'والاول', 'والثاني', 'والثالث', 'والرابع', 'والخامس', 'الثاني', 'الثالث', 'ومثله', 'ومنه', 'وذلك', 'فذلك', 'ونحو', 'ونحوه', 'وك',
         'وهذا', 'فهذا', 'وهو', 'وهي', 'فهو', 'فهي', 'اذا', 'واذا', 'الا', 'وانما', 'انما', 'وقد', 'وليس', 'فليس', 'ويجوز', 'ويجب', 'ويمتنع',
         'وتقول', 'فتقول', 'تقول', 'كقولك', 'وكقولك', 'وقولي', 'بالتخفيف', 'بالتشديد', 'بالرفع', 'بالنصب', 'بالجر', 'بالخفض', 'فيمن', 'يريد'}


def cut_ex(seg):
    """the example as the e-text prints it (vowels off), cut where the commentary resumes; an āya {…} is taken whole."""
    seg = seg.strip()
    if seg.startswith('{'):
        e = seg[1:seg.find('}')] if '}' in seg else ''
        return e.strip() or None
    out = []
    for w in seg.split():
        n = AL.A.norm(re.sub(r'[^ء-ي]', '', w))
        if not n:
            break
        if out and (n in STOP2 or AL._bare_tok(n) in AL.TERM or n in ('او', 'ام') or (n[:1] in 'وف' and n[1:] in STOP2)):
            break
        if re.search(r'[{}()\[\]«»]', w):
            break
        out.append(w)
        if len(out) >= 8:
            break
    return ' '.join(out).strip() or None


def examples2(s0):
    out = []
    for m in EXM2.finditer(s0):
        e = cut_ex(s0[m.end():])
        if e and not e.startswith(('قوله', 'قول')) and (len(e.split()) >= 2 or m.group(0).strip() != 'ك'):
            out.append(e)
    return out


def sentences(l):
    if is_verse(l):
        return []
    parts = SPLIT.split(l) if len(l.split()) > 45 else [l]
    return [p.strip() for p in parts if p.strip()]


def cut_entries(L):
    ents = []
    for u in units(L):
        m = AQB[u['aqil']]
        for k in u['lines']:
            sh, pr, j, l = L[k]
            before = len(ents)
            for s in sentences(l):
                ns = AL.A.norm(s)
                s0 = ' '.join(C.HAR.sub('', s).split())   # the e-text's mechanical vowels off: the markers and the examples are read on the letters
                if not AL.RUL.search(ns) or not EXM2.search(s0):
                    continue
                exs = [e for e in examples2(s0) if C.key(e) and C.key(e) in C.key(s)]
                if not exs:
                    continue
                assert s in l
                n = len([e for e in ents if e['shamela'] == sh]) + 1
                ents.append({'id': 'SH%d.%d' % (sh, n), 'section': u['name'], 'aqil_bab': u['aqil'], 'web_page': pr, 'shamela': sh,
                             'matn': is_matn(l), 'ar': s, 'ex': exs, 'topics': m['topics'], 'role': ROLE_OVR.get(u['aqil'], m['role'])})
            if is_matn(l) and len(ents) == before:   # a matn passage with no ruling + example: kept as a statement, for the notes
                n = len([e for e in ents if e['shamela'] == sh]) + 1
                ents.append({'id': 'SH%d.%d' % (sh, n), 'section': u['name'], 'aqil_bab': u['aqil'], 'web_page': pr, 'shamela': sh,
                             'matn': True, 'ar': l, 'ex': [], 'topics': m['topics'], 'role': None})
    return ents


def load_ledgers():
    out = AL.load_ledgers()   # Shudhūr (old) / Qawāʿid / Iẓhār / Kāfiya, with their topics
    d = json.loads((ROOT / 'content/rules/coverage_ibn_aqil.json').read_text(encoding='utf-8'))
    for e in d['entries']:
        if 'joined' in e:
            continue
        st = 'open' if e.get('warn') else e['status']
        txt = e['ar'] + ' ' + ' '.join(p.get('s', '') for p in e.get('probes', []))
        out.append({'book': 'ibn_aqil', 'id': e['id'], 'status': st, 'topics': set(e.get('topics', [])), 'norm': ' '.join(AL.toks(txt)),
                    'words': {w for w in AL.toks(e['ar']) if len(w) >= 3 and w not in AL.FUNC}})
    return out


def main():
    prove = '--no-prove' not in sys.argv
    L = lines()
    toc = build_toc(L)
    ents = cut_entries(L)
    ledgers = load_ledgers()
    probes, svprobes = [], []
    for e in ents:
        if not e['ex'] and not OVR.get(e['id'], {}).get('probes'):
            e['status'], e['reason'] = 'open', 'a matn statement (definition / list) with no example of its own — for the notes, not the probe'
            if OVR.get(e['id'], {}).get('status'):
                e['status'], e['reason'] = OVR[e['id']]['status'], OVR[e['id']]['reason']
            continue
        j = AL.join(e, e['topics'], ledgers)
        ns = AL.A.norm(e['ar'])
        o = OVR.get(e['id'], {})
        if j and not o:
            e['status'], e['joined'] = j[1]['status'], {'book': j[1]['book'], 'id': j[1]['id'], 'by': 'example' if j[0] == 2 else 'words'}
            continue
        na = next((r for rx, r in AL.NA if rx.search(ns)), None)
        if o.get('status'):
            e['status'], e['reason'] = o['status'], o['reason']; e['triage'] = {'cls': o['cls'], 'why': o.get('why', '')}
            continue
        if na and not o.get('probes'):
            e['status'], e['reason'] = 'not-automatable', na
            continue
        if not e['role'] and not o.get('probes'):
            e['status'], e['reason'] = 'open', 'no construction the iʿrāb line names'
            continue
        nm = AL.named_probes(e['ar'], e['ex'])
        multi = [x for x in e['ex'] if len(x.split()) >= 2]
        if not nm and not multi and not o.get('probes'):
            e['status'], e['reason'] = 'open', 'a single word cited — the ruling is on its form, no sentence for the iʿrāb probe'
            continue
        if o.get('probes'):
            e['probes'] = [dict(p) for p in o['probes']]; e['triage'] = {'cls': o['cls'], 'why': o.get('why', '')}
        elif nm:
            ex0 = (multi or e['ex'])[0]
            e['probes'] = [{'s': next((x for x in e['ex'] if w in x.split()), ex0), 'w': w, 're': rg} for w, rg in nm[:3]]
        else:
            e['probes'] = [{'s': multi[0], 'any': e['role']}]
        for p in e['probes']:
            assert o.get('free') or C.key(p['s']) in C.key(e['ar']), (e['id'], p['s'])
            p['_k'] = len(probes)
            probes.append({k: v for k, v in p.items() if k not in ('_k', 'sv')})
            if p.get('sv'):
                p['_kv'] = len(svprobes)
                svprobes.append(dict({k: v for k, v in p.items() if k not in ('_k', '_kv', 'sv')}, s=p['sv']))
    if prove:
        pin = HERE / '.shudhur2-probes.json'
        pin.write_text(json.dumps(probes, ensure_ascii=False), encoding='utf-8')
        subprocess.run(['node', str(HERE / 'aqil_prove.js'), str(pin), str(CACHE)], check=True)
        pin.write_text(json.dumps(svprobes, ensure_ascii=False), encoding='utf-8')
        if svprobes:
            subprocess.run(['node', str(HERE / 'aqil_prove.js'), str(pin), str(CACHE_SV)], check=True)
        pin.unlink()
    res = json.loads(CACHE.read_text(encoding='utf-8'))
    ress = json.loads(CACHE_SV.read_text(encoding='utf-8')) if svprobes else []
    assert len(res) == len(probes) and len(ress) == len(svprobes), 'proof cache is stale: run without --no-prove'
    for e in ents:
        if 'probes' not in e:
            continue
        for p in e['probes']:
            r = res[p.pop('_k')]
            p['ok'], p['got'] = r['ok'], r['got'][:200]
            if r.get('offered'):
                p['offered'] = True
            if '_kv' in p:
                rv = ress[p.pop('_kv')]
                p['svok'], p['svgot'] = rv['ok'], rv['got'][:200]
                if not r['ok'] and rv['ok']:
                    p['vowelled'] = True; p.pop('offered', None)
                    if rv.get('offered'):
                        p['offered'] = True
        if all(p['ok'] or p.get('svok') for p in e['probes']):
            e['status'] = 'applied'
            if any(p.get('offered') for p in e['probes']):
                e['offered'] = True
            if any(p.get('vowelled') for p in e['probes']):
                e['vowelled'] = True
        else:
            e['status'], e['warn'] = 'open', True
    counts, by = Counter(), defaultdict(Counter)
    for e in ents:
        k = 'joined' if 'joined' in e else ('warn' if e.get('warn') else e['status'] + ('-offered' if e.get('offered') else '') + ('-vowelled' if e.get('vowelled') else ''))
        counts[k] += 1; counts['status:' + e['status']] += 1
        by[e['section']][k] += 1; by[e['section']]['entries'] += 1
    for e in ents:
        e.pop('role', None)
    doc = {'book': 'Sharḥ Shudhūr al-Dhahab — the unread half (web text, pp. %d–602)' % UNREAD_FROM, 'source_file': REL,
           'built_by': 'tools/ledger/shudhur2_ledger.py', 'about': __doc__.split('\n\n', 1)[1].strip(),
           'counts': dict(sorted(counts.items())), 'by_section': {k: dict(v) for k, v in by.items()}, 'entries': ents}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
    print('toc:', json.dumps(toc['counts'], ensure_ascii=False), 'thin:', toc['thin_babs'])
    print(len(ents), json.dumps(doc['counts'], ensure_ascii=False))


if __name__ == '__main__':
    main()
