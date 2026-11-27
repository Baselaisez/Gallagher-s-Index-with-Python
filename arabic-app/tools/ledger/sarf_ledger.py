#!/usr/bin/env python3
"""v342-S — the ṣarf books' ledger: every rule sentence of Marāḥ al-Arwāḥ, al-Maqṣūd and Taṣrīf al-ʿIzzī, cut BY SCRIPT
from research/sources, with where the app carries it.

    python3 tools/ledger/sarf_ledger.py            # write content/rules/coverage_{marah,maqsud,izzi}.json + the research md
    python3 tools/ledger/sarf_ledger.py --units    # print the cut only (no carriers), for a look

An entry: {id, line, ar (verbatim: the source line, or a slice of it), kind, section, carried_by: [...], status, why?}
  carried_by items:
    {"engine": <code name>, "cite": "<book> L<n>"}   the code cites the line (found in prototype/reader.html's code, not its data)
    {"note": <grammar note id>}                       the note's classicalSources or an example's `source` names the line
    {"bank": <catechism book>, "item": <id>}          a catechism item's src lines include the line
    {"probe": <probe id>}                             a probe (content/rules/sarf_ledger_probes.json) runs the book's own words
                                                      through an engine and the smoke check re-proves it
  status: applied (a probe proves it) · noted (a note or a bank carries it) · not-automatable (why) · open
Nothing here is typed Arabic: every `ar` is cut from the source by line number (and, for the raw matn, by a sentence split).
"""
import json, re, sys, glob, os
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'research', 'sources')
HAR = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def bare(s): return HAR.sub('', s).replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ٱ', 'ا')

BOOKS = {
    'marah': {'title': 'مَرَاحُ الْأَرْوَاحِ', 'files': ['marah-al-arwah-src.txt', 'marah-al-arwah-matn.txt'], 'cite': 'Marāḥ'},
    'maqsud': {'title': 'الْمَقْصُودُ', 'files': ['maqsud-sarf.txt'], 'cite': 'Maqṣūd'},
    'izzi': {'title': 'تَصْرِيفُ الْعِزِّيِّ', 'files': ['tasrif-al-izzi-src.txt'], 'cite': 'ʿIzzī'},
}

def read(f): return open(os.path.join(SRC, f), encoding='utf8').read().split('\n')

# ---------------------------------------------------------------- the cut
def cut_src(book, f):
    """A clean src (Marāḥ to p. 144, the ʿIzzī): one entry per text line; ## N = the chapter, # page N = the page."""
    out, ch, title, page = [], 0, '', None
    for i, l in enumerate(read(f), 1):
        m = re.match(r'^## (\d+) (.*)', l)
        if m: ch, title = int(m.group(1)), m.group(2); continue
        m = re.match(r'^# page (\d+)', l)
        if m: page = int(m.group(1)); continue
        if not l.strip() or l.startswith('#'): continue
        out.append({'file': f, 'line': i, 'ar': l.strip(), 'ch': ch, 'chTitle': title, 'page': page})
    return out

MATN_FROM = 417   # [ص 145]: what the src does not hold (backlog F7)
# a raw page is one long line; it is cut where the book opens a new head: a cell name with its colon, an ibdāl letter
# («الهمزة أبدلت …»), «يقال له», or a sentence stop
MATN_HEADS = r'(?=(?:المستقبل|الأمر|الفاعل|المفعول|الموضع|الآلة|المجهول)\s*:)|(?<=[\s،.])(?=(?:الهمزة|الهاء|الياء|الواو|الميم|الصاد|الألف|اللام|الزاء|الطاءُ|الطاء|التاء|النون|والجيم|الدال|والسين)\s+أبدلت)|(?<=[.])\s+'
def cut_matn(f):
    out, page = [], None
    for i, l in enumerate(read(f), 1):
        if i < MATN_FROM: continue
        m = re.match(r'^\[ص (\d+)\]', l.strip())
        if m: page = int(m.group(1)); continue
        if not l.strip(): continue
        parts = [p.strip() for p in re.split(MATN_HEADS, l) if p and p.strip()]
        for k, p in enumerate(parts):
            out.append({'file': f, 'line': i, 'part': k + 1, 'ar': p, 'ch': 'matn', 'chTitle': '', 'page': page})
    # a fragment of one or two words (a head cut off by the page's end: «التاء» … [ص 166] «أبدلت من الواو») joins the next unit
    j = 0
    while j < len(out) - 1:
        if len(out[j]['ar'].split()) <= 2 and not re.match(r'^(?:المستقبل|الأمر|الفاعل|المفعول|الموضع|الآلة|المجهول)\s*:', out[j]['ar']):
            nx = out[j + 1]; nx['ar'] = out[j]['ar'] + ' ' + nx['ar']
            nx['lines'] = sorted(set([out[j]['line']] + (out[j].get('lines') or []) + [nx['line']]))
            nx['line'], nx['part'] = out[j]['line'], out[j]['part']; out.pop(j); continue
        j += 1
    return out

def cut_maqsud(f):
    """The Maqṣūd: an Ottoman commentary carrying the matn. A unit is a paragraph: lines are joined until one ends a
    sentence, and a new unit starts at a numbered item, a question, an answer, a «nota», an example line or a bāb head."""
    L = read(f)
    starts = re.compile(r'^\s*(\{|﴿|س\s*[؛:]|ج\s*[؛:]|نوط|مثلا|معناسى|فصل|\S+ بابى|\S+ بابنه|ماضى|مضارع|اسم |امر |نهى|حديث)')
    out, cur = [], None
    for i, l in enumerate(L, 1):
        s = l.strip()
        if not s: cur = None; continue
        dens = len(HAR.findall(s)) > 0.5 * max(1, len(re.findall('[\u0621-\u064a]', s)))      # a vowelled Arabic line (a table, a matn) or Ottoman prose
        if cur and cur.get('dens') != dens: cur = None
        if cur and not starts.match(s) and not re.search(r'[.:]\s*$|\}\s*$|﴾\s*$', cur['ar']):
            cur['ar'] += '\n' + s; cur['lines'].append(i); continue
        cur = {'file': f, 'line': i, 'lines': [i], 'ar': s, 'ch': None, 'chTitle': '', 'page': None, 'dens': dens}
        out.append(cur)
    for u in out: u.pop('dens', None)
    return out

# the Maqṣūd's parts, by line (read off the text: the preface, the six derivations, the sound verb's taṣrīf and the bābs,
# the meanings of the bābs, the weak and the doubled and the hamzated, the emsile tables)
MAQSUD_PARTS = [(1, 78, 'preface'), (79, 126, 'divisions'), (127, 309, 'derivations'), (310, 460, 'sahih-babs'),
                (461, 559, 'meanings'), (560, 700, 'ilal'), (701, 750, 'mithal'), (751, 770, 'mudaaf'), (771, 815, 'mahmuz'),
                (816, 99999, 'tables')]
def maqsud_part(n):
    for a, b, k in MAQSUD_PARTS:
        if a <= n <= b: return k

def cut(book):
    if book == 'marah': return cut_src(book, 'marah-al-arwah-src.txt') + cut_matn('marah-al-arwah-matn.txt')
    if book == 'izzi': return cut_src(book, 'tasrif-al-izzi-src.txt')
    U = cut_maqsud('maqsud-sarf.txt')
    for u in U: u['ch'] = maqsud_part(u['line'])
    return U

# ---------------------------------------------------------------- kinds
K_QA = re.compile(r'فان قيل|قلنا|فان قلت|^\s*س\s*[؛:]|^\s*ج\s*[؛:]|سوال')
K_EXC = re.compile(r'الا |شاذ|لا يعل|ولا يعل|لا تعل|لا يجوز|لا يبنى|نادر|سماع|مستثنا|قاعده يه مخالف|على غير قياس|لم يغير|لا يجيء|لا تقلب|لا يقلب|ولا يدغم|لا يدغم|يمتنع|ممتنع|قلب اولونمازلر|ترك ايديلر')
K_COND = re.compile(r'اذا |بشرط|شرط|شروط|ان كان|ان كانت|حتى لا|لئلا|ايسه|اولورسه|زمان')
K_DEF = re.compile(r'يقال له|ويقال له|يسمى|سمي|وهو ما|وهي ما|عبارة|هو الذي|هو الفعل|ما كان|ديرلر|دينير|ديمكدر|عبارتدر|معناسنه')
# the Maqṣūd's teacher's notes carry ḥadīths, their meanings, advice to the students and the citations of his references — no rule
MQ_DISC = re.compile(r'حديث|اولادلرم|روح البيان|نوطلرى|رضاسى|عدم ترقى|ترقيلر|پيغمبر|جنته|بويوردى|^\s*﴿[^﴾]*ص[^﴾]*﴾\s*$|^\s*\{[^}]*ص\s*[؛:][^}]*\}\s*$')
def kind_of(u, book):
    b = bare(u['ar'])
    if book == 'maqsud':
        p = u['ch']
        if p == 'preface': return 'discourse'
        if p == 'tables': return 'paradigm'
    if u['ch'] == 1 and book == 'marah': return 'discourse'
    if book == 'maqsud' and MQ_DISC.search(b): return 'discourse'
    if K_QA.search(b): return 'qa'
    if K_EXC.search(b): return 'exception'
    if K_COND.search(b): return 'condition'
    if K_DEF.search(b): return 'definition'
    return 'rule'

# ---------------------------------------------------------------- carriers
def code_text():
    t = open(os.path.join(ROOT, 'prototype', 'reader.html'), encoding='utf8').read()
    return t[:t.index('// __DATA_START__')] if '// __DATA_START__' in t else t

CITE = re.compile(r"(Marāḥ|Marah|ʿIzzī|Izzi|ʿIzzi|Maqṣūd|Maqsud)[^\n]{0,8}?L ?(\d+)((?:\s*[–-]\s*L?\d+)?)((?:,\s*L\d+(?:\s*[–-]\s*L?\d+)?)*)")
NAME = re.compile(r'^(?:class|const|let|function|async function)\s+([A-Za-z_$][\w$]*)', re.M)   # top level only: a local «const out» owns nothing
def code_cites():
    """{(book, line): set(code names)} — every «Marāḥ L760», «ʿIzzī L146–L150», «Maqṣūd L807–L810, L832» in the code."""
    t = code_text(); names = [(m.start(), m.group(1)) for m in NAME.finditer(t)]
    import bisect; pos = [p for p, _ in names]
    def owner(at):
        k = bisect.bisect_right(pos, at) - 1
        # the nearest CLASS or top-level name wins over a method name when both are close
        return names[k][1] if k >= 0 else '?'
    def cls(at):
        k = t.rfind('\nclass ', 0, at); c = re.match(r'\nclass (\w+)', t[k:k + 80]) if k >= 0 else None
        e = t.find('\n}', k) if k >= 0 else -1
        return c.group(1) if (c and e > at) else None
    out = defaultdict(set)
    for m in CITE.finditer(t):
        b = m.group(1); book = 'marah' if 'Mar' in b else ('izzi' if 'zz' in b else 'maqsud')
        spans = [m.group(2) + m.group(3)] + [x for x in re.split(r',\s*L', m.group(4)) if x.strip()]
        name = cls(m.start()) or owner(m.start())
        for s in spans:
            n = [int(x) for x in re.findall(r'\d+', s)]
            a, z = n[0], (n[1] if len(n) > 1 else n[0])
            if z < a or z - a > 40: z = a
            for x in range(a, z + 1): out[(book, x)].add(name)
    return out

FILE_BOOK = {'marah-al-arwah-src.txt': 'marah', 'marah-al-arwah-matn.txt': 'marah', 'tasrif-al-izzi-src.txt': 'izzi', 'maqsud-sarf.txt': 'maqsud'}
AR_DIG = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '01234567890123456789')
def note_cites():
    """{(file, line): set(note ids)} — a note names a line in its classicalSources («…-src.txt، س 760، 761») or in an
    example's `source` («marah-al-arwah-src.txt:760 (ص 136)»)."""
    out = defaultdict(set)
    for f in glob.glob(os.path.join(ROOT, 'content', 'grammar', '*.json')):
        n = json.load(open(f, encoding='utf8')); nid = n.get('id') or os.path.basename(f)[:-5]
        for s in n.get('classicalSources', []) or []:
            s = s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
            for fn in FILE_BOOK:
                for m in re.finditer(re.escape(fn) + r'[،,]?\s*س\s*([\d٠-٩۰-۹،,\s–-]+)', s):
                    for a, z in re.findall(r'(\d+)(?:\s*[–-]\s*(\d+))?', m.group(1).translate(AR_DIG)):
                        a = int(a); z = int(z) if z else a
                        for x in range(a, (z if 0 <= z - a <= 40 else a) + 1): out[(fn, x)].add(nid)
        for e in n.get('examples', []) or []:
            s = e.get('source') or ''
            for fn in FILE_BOOK:
                for m in re.finditer(re.escape(fn) + r':(\d+)(?:\s*[–-]\s*(\d+))?(?:\s*\[(\d+)\])?', s):
                    a = int(m.group(1)); z = int(m.group(2)) if m.group(2) else a
                    if m.group(3): out[(fn, a, int(m.group(3)))].add(nid); continue   # one unit of a raw matn page
                    for x in range(a, (z if 0 <= z - a <= 40 else a) + 1): out[(fn, x)].add(nid)
    return out

def bank_cites():
    out = defaultdict(set)
    for f in glob.glob(os.path.join(ROOT, 'content', 'catechism', '*.json')):
        b = json.load(open(f, encoding='utf8'))
        for it in b.get('items', []):
            s = it.get('src') or {}
            fn = os.path.basename(s.get('file', '') or '')
            for x in s.get('lines', []) or []: out[(fn, int(x))].add((b.get('book') or os.path.basename(f)[:-5], it.get('id') or it.get('n')))
    return out

# ---------------------------------------------------------------- hand data (reasons; never Arabic)
# not-automatable: a line the app CANNOT apply by an engine, with the reason; the reason is ours, the line is the book's
NOT_AUTO = {
    # (book, kind) defaults
    ('*', 'discourse'): 'not a rule: the preface, a prayer, a ḥadīth or the author\'s life — the story / the bank carries the text',
}
PROBES_FILE = os.path.join(ROOT, 'content', 'rules', 'sarf_ledger_probes.json')
PLAN_FILE = os.path.join(ROOT, 'content', 'rules', 'sarf_ledger_plan.json')
FAILED_FILE = os.path.join(ROOT, 'tools', 'ledger', 'probes_failed_read.json')   # the probes that do not pass, each read by hand (why)

def entry_id(book, u):
    f = u['file']
    tag = {'marah-al-arwah-src.txt': 'src', 'marah-al-arwah-matn.txt': 'matn', 'tasrif-al-izzi-src.txt': 'src', 'maqsud-sarf.txt': 'l'}[f]
    return f"{book}:{tag}{u['line']}" + (f".{u['part']}" if u.get('part') else '')

def build(book, cites, notes, banks, probes, plan):
    units = cut(book); E = []
    for u in units:
        eid = entry_id(book, u); lines = u.get('lines') or [u['line']]
        kind = (plan.get('kind') or {}).get(eid) or kind_of(u, book)
        cb = []
        if u['file'] != 'marah-al-arwah-matn.txt':   # the code cites the src's line numbers (the matn's are its own)
            for x in lines:
                for nm in sorted(cites.get((book, x), ())): cb.append({'engine': nm, 'cite': f"{BOOKS[book]['cite']} L{x}"})
        for nid in sorted(notes.get((u['file'], u['line'], u.get('part')), ())): cb.append({'note': nid, 'line': u['line']})
        for x in lines:
            for nid in sorted(notes.get((u['file'], x), ())): cb.append({'note': nid, 'line': x})
            for bk, iid in sorted(banks.get((u['file'], x), ()), key=str): cb.append({'bank': bk, 'item': iid})
        # de-duplicate
        seen = set(); cb2 = []
        for c in cb:
            k = json.dumps({kk: vv for kk, vv in c.items() if kk != 'line'}, sort_keys=True, ensure_ascii=False)
            if k not in seen: seen.add(k); cb2.append(c)
        cb = cb2
        pr = probes.get(eid) or []
        for p in pr: cb.append({'probe': p['id']})
        why = None
        if kind == 'discourse': pr = []; cb = [c for c in cb if 'probe' not in c]   # a ḥadīth's words are no example of a rule
        if pr: status = 'applied'
        elif any('note' in c or 'bank' in c for c in cb): status = 'noted'
        elif eid in (plan.get('not_auto') or {}): status, why = 'not-automatable', plan['not_auto'][eid]
        elif kind == 'discourse': status, why = 'not-automatable', NOT_AUTO[('*', 'discourse')]
        else: status = 'open'
        e = {'id': eid, 'line': u['line'], 'ar': u['ar'], 'kind': kind, 'section': u['ch'], 'page': u.get('page'), 'carried_by': cb, 'status': status}
        if u.get('lines') and len(u['lines']) > 1: e['lines'] = u['lines']
        if u['file'] != BOOKS[book]['files'][0]: e['file'] = u['file']
        if why: e['why'] = why
        dest = (plan.get('dest') or {}).get(eid)
        if status == 'open' and dest: e['dest'] = dest
        E.append(e)
    return E

# ---------------------------------------------------------------- probe candidates (the runner turns them into probes)
# the model roots the three books conjugate (read off their chapters); RootFinder adds a word's own root beside them
MODEL_ROOTS = ('ن ص ر،ض ر ب،ف ت ح،س م ع،ك ر م،ح س ب،ع ل م،ف ع ل،ق ت ل،د ح ر ج،خ ر ج،م د د،ف ر ر،ع ض ض،ر د د،و ع د،ي س ر،و ج ل،و ه ب،'
               'و ر ث،ق و ل،ب ي ع،خ و ف،ص و ن،ط و ل،ه ي ب،غ ز و،ر م ي،ر ض ي،س ر و،خ ش ي،د ع و،ل ق ي،ط و ي،و ق ي،ر و ي،ح ي ي،ش و ي،'
               'ق و ي،و ج ي،أ م ل،أ خ ذ،أ ك ل،أ م ر،س أ ل،ق ر أ،ر أ ي،ج ي أ،ه ن أ،أ ز ر،أ د ب،أ و ي،ك ي ل،ق و م،ن ي ل،م ي ل').split('،')
STOP = set(bare(x) for x in ('قال يقول تقول قلت قالوا يقال قيل كان يكون تكون كانت صار يصير جاء يجيء يجوز نحو مثل اصله اصلها وهو وهي '
                              'الذي التي لان لانه حتى الا اذا ان لم لن هذا ذلك فيه منه عليه اليه بين عند غير كما ايضا').split())
QUOTE = re.compile(r'«([^»]+)»')
ASL = [re.compile(r'«([^»]+)»\s*(?:وَ)?أَصْلُ(?:هُ|هَا|هُمَا)\s*«([^»]+)»'),                   # Marāḥ: «مِيزَانٌ» أَصْلُهُ «مِوْزَانٌ»
       re.compile(r'([^\s،.:«»]+)\s+(?:وَ)?أَصْلُ(?:هُ|هَا)\s+([^\s،.:«»]+)'),                   # ʿIzzī: … أَصْلُهُ …
       re.compile(r'أصل\s*«([^»]+)»\s*:?\s*([^\s،.:«»]+)'),                                     # matn: أصل «قال»: قَوَلَ (aṣl second)
       re.compile(r'([^\s،.:«»]+)\s+اصلنده\s+([^\s،.:«»]+)')]                                     # Maqṣūd: قَالَ اصلنده قَوَلَ
ARW = re.compile(r'[ء-يٱ][ء-ْٰٱ]*')
def vowelled(w): return len(HAR.findall(w)) >= max(2, len(bare(w)) // 2)
def candidates():
    out = []
    for b in BOOKS:
        for u in cut(b):
            if kind_of(u, b) == 'discourse': continue
            eid = entry_id(b, u); raw = u['file'] == 'marah-al-arwah-matn.txt'; t = u['ar']
            words = []
            if u['file'] == 'marah-al-arwah-src.txt':
                for q in QUOTE.findall(t): words += ARW.findall(q)
            elif raw:
                words = [w for w in ARW.findall(t)]
            else:
                words = [w for w in ARW.findall(t) if vowelled(w)]
            words = [re.sub(r'["“”{}()\[\]]', '', w) for w in words]
            words = [w for w in dict.fromkeys(words) if len(bare(w)) >= 2 and bare(w) not in STOP]
            asl = []
            for k, rx in enumerate(ASL):
                for m in rx.finditer(t):
                    a, z = (re.sub(r'["“”{}()\[\]]', '', x).strip() for x in m.groups())
                    if not ARW.fullmatch(a or '-') or not ARW.fullmatch(z or '-'): continue
                    if not raw and not (vowelled(a) and vowelled(z)): continue
                    asl.append({'w': a, 'asl': z})   # (the word, its aṣl): every form names the aṣl second
            # the Maqṣūd's Ottoman prose is printed bare: a VOWELLED Arabic word inside it is the book's example, as a «…» is the Marāḥ's
            if words or asl: out.append({'lines': u.get('lines') or [u['line']], 'entry': eid, 'raw': raw, 'words': words, 'asl': asl, 'quoted': u['file'] in ('marah-al-arwah-src.txt', 'maqsud-sarf.txt'),
                                         'min': 2 if (raw and not re.match(r'^(?:المستقبل|الأمر|الفاعل|المفعول|الموضع|الآلة|المجهول)\s*:', t)) else 1, 'mq': u['line'] if (b == 'maqsud' and u['ch'] == 'tables') else None})
    mq = [{'entry': entry_id('maqsud', u), 'lines': u.get('lines') or [u['line']]} for u in cut('maqsud')]
    return {'roots': MODEL_ROOTS, 'units': out, 'mqUnits': mq}

# ---------------------------------------------------------------- the research page (research/book-coverage-2026-11-27.sarf.md)
BEFORE = {   # the first full cut of this wave (2026-11-26, before any engine rule or note of v342-S; the probes as first written)
    'marah': {'n': 671, 'applied': 266, 'noted': 74, 'not-automatable': 5, 'open': 326},
    'maqsud': {'n': 651, 'applied': 300, 'noted': 26, 'not-automatable': 54, 'open': 271},
    'izzi': {'n': 278, 'applied': 167, 'noted': 27, 'not-automatable': 0, 'open': 84}}
def render_md(docs, failed):
    O = ['# Book coverage — the ṣarf books (v342-S, 2026-11-26)', '',
         'Cut BY SCRIPT from `research/sources` by `tools/ledger/sarf_ledger.py` (one entry per rule sentence: a src line, a sentence of the raw',
         'matn, a paragraph of the Maqṣūd); the carriers are found, not typed: the code\'s book-line cites, the notes\' `classicalSources` and',
         'example `source` lines, the catechism items\' `src` lines, and the probes of `content/rules/sarf_ledger_probes.json` (the book\'s own',
         'word run through an engine — `sarfDerive` cells with the passive and the emphatic, `IlalEngine.derive` on a «X أَصْلُهُ Y» pair,',
         '`IshtiqaqEngine.read0`, `MaqsudEngine`\'s cells, the 35-door table, `Bab35Engine.meanings`). «applied» = at least one probe on the',
         'entry passes and the smoke check «v342 — the ṣarf ledger of …» re-runs every one; «noted» = a note or a bank quotes or anchors the line.', '']
    O += ['| book | entries | applied | noted | not automatable | open |', '|---|---|---|---|---|---|']
    for b, d in docs.items():
        c = d['counts']; bf = BEFORE[b]
        f = lambda k: f"{bf.get(k, 0)} → **{c.get(k, 0)}**"
        O.append(f"| {d['title']} | {bf['n']} → {len(d['entries'])} | {f('applied')} | {f('noted')} | {f('not-automatable')} | {f('open')} |")
    O += ['', '«before» is the first cut of this wave; the cut itself was refined since (the raw matn\'s page-break fragments joined, the Maqṣūd\'s',
          'paragraphs split where a vowelled table line meets Ottoman prose), so the entry counts differ a little.', '']
    for b, d in docs.items():
        O += [f"## {d['title']} — section by section", '', '| section | entries | applied | noted | n/a | open |', '|---|---|---|---|---|---|']
        sec = {}
        for e in d['entries']:
            k = str(e['section']); sec.setdefault(k, Counter())[e['status']] += 1
        for k, c in sec.items():
            O.append(f"| {k} | {sum(c.values())} | {c.get('applied', 0)} | {c.get('noted', 0)} | {c.get('not-automatable', 0)} | {c.get('open', 0)} |")
        op = [e for e in d['entries'] if e['status'] == 'open']
        if op:
            O += ['', f"**Open ({len(op)})** — the Maqṣūd\'s Ottoman prose: a note can quote it only beside a modern-Turkish rendering, which this wave did not write;",
                  'ranked by part (the parts nearest the engines first):', '']
            for k in ('ilal', 'mahmuz', 'mithal', 'mudaaf', 'meanings', 'sahih-babs', 'derivations', 'divisions', 'tables'):
                ls = [e for e in op if e['section'] == k]
                if ls: O.append(f"- {k} ({len(ls)}): lines " + ', '.join(str(e['line']) for e in ls))
        na = [e for e in d['entries'] if e['status'] == 'not-automatable']
        if na:
            why = Counter(e['why'] for e in na)
            O += ['', f"**Not automatable ({len(na)}):** " + '; '.join(f"{w} ({n})" for w, n in why.items())]
        O.append('')
    if failed:
        O += ['## What the engines still say otherwise than the book (the probes that do not pass)', '',
              'Each is a «X أَصْلُهُ Y» or an example the engine does not reproduce; it is NOT counted as applied, and each is read here:', '']
        for x in failed: O.append(f"- `{x['entry']}` {x.get('asl', '')} → engine «{x.get('got')}», book «{x.get('w', '')}»" + (f" — {x['why']}" if x.get('why') else ''))
        O.append('')
    return '\n'.join(O) + '\n'

def main():
    if '--candidates' in sys.argv:
        json.dump(candidates(), open(sys.argv[-1], 'w', encoding='utf8'), ensure_ascii=False); return
    probes =json.load(open(PROBES_FILE, encoding='utf8')) if os.path.exists(PROBES_FILE) else {}
    plan = json.load(open(PLAN_FILE, encoding='utf8')) if os.path.exists(PLAN_FILE) else {}
    byid = defaultdict(list)
    for p in probes.get('probes', []): byid[p['entry']].append(p)
    if '--units' in sys.argv:
        for b in BOOKS:
            U = cut(b); print(b, len(U), Counter(kind_of(u, b) for u in U))
        return
    cites, notes, banks = code_cites(), note_cites(), bank_cites()
    summary, docs = {}, {}
    for b, meta in BOOKS.items():
        E = build(b, cites, notes, banks, byid, plan)
        C = Counter(e['status'] for e in E)
        doc = {'book': b, 'title': meta['title'], 'source': ['research/sources/' + f for f in meta['files']],
               'generated_by': 'tools/ledger/sarf_ledger.py', 'counts': dict(sorted(C.items())), 'kinds': dict(sorted(Counter(e['kind'] for e in E).items())),
               'entries': E}
        json.dump(doc, open(os.path.join(ROOT, 'content', 'rules', f'coverage_{b}.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        summary[b] = (len(E), dict(C)); docs[b] = doc
        print(b, len(E), dict(C))
    F = json.load(open(FAILED_FILE, encoding='utf8')) if os.path.exists(FAILED_FILE) else []
    open(os.path.join(ROOT, 'research', 'book-coverage-2026-11-27.sarf.md'), 'w', encoding='utf8').write(render_md(docs, F))
    return summary

if __name__ == '__main__':
    main()
