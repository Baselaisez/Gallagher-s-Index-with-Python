#!/usr/bin/env python3
"""v342-A — the other resources' ledger.

Every file in research/sources/ that the two main-book ledgers (naḥw: Shudhūr, Qawāʿid al-Iʿrāb, Iẓhār, Kāfiya; ṣarf: Marāḥ,
Maqṣūd, ʿIzzī) do not hold is accounted for here, BY SCRIPT from the file itself: one entry per table row, rule, question,
section or page, each with its source line and where the app carries it —

  applied          an engine applies it; PROVED by a probe (aux_probe.js) that `--prove` runs on the built page
  noted            a grammar note quotes or anchors it (the note id is checked to exist and, for a quote, to contain it)
  banked           a question bank (content/catechism/) holds it (the item id is checked)
  shelved          a received text: the source's lines are on the shelf as a package (counted)
  not-automatable  with the reason (unrecoverable bytes, a teaching device, a page of front matter …)
  open             nothing carries it yet — consumed as data, or written into research/engine-gaps-2026-11-27.md

Run:  python3 tools/ledger/aux_ledger.py            (build the entries, keep the last proof results)
      python3 tools/ledger/aux_ledger.py --prove    (also run every probe on prototype/reader.html; needs NODE_PATH/CHROMIUM_PATH)
Writes content/rules/coverage_<source>.json per ledger and research/book-coverage-2026-11-27.aux.md.
A probe that fails demotes its entry: «applied» is never claimed by reading code.
"""
import json, re, subprocess, sys, os, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'research' / 'sources'
OUT = ROOT / 'content' / 'rules'
PROOF = ROOT / 'content' / 'rules' / 'coverage_aux.proof.json'
sys.path.insert(0, str(ROOT / 'tools'))

HARAKAT = re.compile('[ً-ْٰـ]')
TRD = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '01234567890123456789')


def H(s):
    s = HARAKAT.sub('', str(s or '')).replace('‌', '')
    return re.sub('[أإآٱ]', 'ا', s).replace('ى', 'ي')


def HN(s):  # letters only, one space
    return re.sub(r'\s+', ' ', re.sub('[^ء-ي ]', ' ', H(s))).strip()


def lines(name):
    return (SRC / name).read_text(encoding='utf-8', errors='replace').split('\n')


# ---------------------------------------------------------------- the app's carriers
NOTES = {}
for f in sorted((ROOT / 'content' / 'grammar').glob('*.json')):
    d = json.loads(f.read_text(encoding='utf-8'))
    NOTES[d['id']] = d
NOTE_TEXT = {k: HN(json.dumps(v, ensure_ascii=False)) for k, v in NOTES.items()}
BANKS = {}
for f in sorted((ROOT / 'content' / 'catechism').glob('*.json')):
    d = json.loads(f.read_text(encoding='utf-8'))
    BANKS[f.stem] = d
STORIES = {}
for d in sorted((ROOT / 'content' / 'samples').iterdir()):
    if not (d / 'manifest.json').exists():
        continue
    chs = []
    for f in sorted((d / 'chapters').glob('*.json'), key=lambda p: int(re.sub(r'\D', '', p.stem) or 0)):
        c = json.loads(f.read_text(encoding='utf-8'))
        chs.append(c)
    STORIES[d.name] = {'manifest': json.loads((d / 'manifest.json').read_text(encoding='utf-8')), 'chapters': chs,
                       'glossary': json.loads((d / 'glossary.json').read_text(encoding='utf-8')) if (d / 'glossary.json').exists() else {}}


def sentences():
    for sid, st in STORIES.items():
        for c in st['chapters']:
            for s in c['sentences']:
                yield sid, c['chapter'], s


SENT = list(sentences())
STORY_TEXT = {sid: HN(' '.join(t['surface']['full'] for c in st['chapters'] for s in c['sentences'] for t in s['tokens']))
              for sid, st in STORIES.items()}


def sent_text(s):
    return ' '.join(t['surface']['full'] for t in s['tokens'])


def note_quoting(ar, min_len=8):
    """note ids whose text holds the example (letters only)."""
    a = HN(ar)
    if len(a) < min_len:
        return []
    return [k for k, v in NOTE_TEXT.items() if a in v]


def corpus_hits(word_bare, irab_re, limit=1, max_tokens=14):
    """the SHORTEST story sentences whose token (bare letters) is word_bare and whose AUTHORED line matches irab_re —
    a short sentence is the cleanest proof that the engine applies a rule the source states without an example."""
    out = []
    rx = re.compile(irab_re)
    for sid, ch, s in SENT:
        toks = s['tokens']
        if len(toks) > max_tokens:
            continue
        for i, t in enumerate(toks):
            b = re.sub('[^\u0621-\u064A]', '', H(t['surface']['full']))
            if b == word_bare and rx.search(H((t.get('irab') or {}).get('ar', ''))):
                out.append({'s': sent_text(s), 'w': i, 'at': f'{sid}:{ch}:{s["id"]}:{i + 1}', 'n': len(toks)})
                break
    out.sort(key=lambda x: (x['n'], x['at']))
    return out[:limit]


def role_hits(rx, limit=3, max_tokens=10, prev=None):
    """the SHORTEST story sentences with a token whose AUTHORED line opens (first 40 letters) with the role rx (and, with
    prev, whose preceding token's authored line matches prev)."""
    out = []
    for sid, ch, s in SENT:
        if len(s['tokens']) > max_tokens:
            continue
        for i, t in enumerate(s['tokens']):
            if re.search(rx, H((t.get('irab') or {}).get('ar', ''))[:40]) and (not prev or (i and re.search(prev, H((s['tokens'][i - 1].get('irab') or {}).get('ar', ''))))):
                out.append({'s': sent_text(s), 'w': i, 'at': f'{sid}:{ch}:{s["id"]}:{i + 1}', 'n': len(s['tokens'])}); break
    out.sort(key=lambda x: (x['n'], x['at']))
    return out[:limit]


def corpus_count(pred_tok):
    return sum(1 for _, _, s in SENT for t in s['tokens'] if pred_tok(t))


# ---------------------------------------------------------------- entries
LEDGERS = {}  # key -> {book, files, title, group, entries}


def ledger(key, title, files, group, note=''):
    LEDGERS[key] = {'book': key, 'title': title, 'source': files[0], 'files': files, 'group': group, 'note': note, 'entries': []}
    return LEDGERS[key]['entries']


def E(entries, id, line, ar, kind, carried_by=None, status=None, probe=None, reason=None, gap=None):
    e = {'id': id, 'line': line, 'ar': ar, 'kind': kind, 'carried_by': carried_by or []}
    if probe:
        e['probe'] = probe
    if reason:
        e['reason'] = reason
    if gap:
        e['gap'] = gap
    e['claim'] = status  # what the mapping claims; the final status is decided after proof
    entries.append(e)
    return e


def note(ids, how='names'):
    return [{'type': 'note', 'ref': i, 'how': how} for i in ids if i in NOTES]


def bank(bk, n):
    for it in BANKS.get(bk, {}).get('items', []):
        if it['n'] == n:
            return [{'type': 'bank', 'ref': it['id']}]
    return []


def mprobe(s, w, re_, not_=None):
    p = {'s': s, 'w': w, 're': re_}
    if not_:
        p['not'] = not_
    return p


# ================================================================ group 1: the ʿawāmil and the iʿrāb tables
def g_awamil():
    import check_canon as cc
    files = ['awamil-birgivi-tables.txt', 'amil-tablolari-turkce.txt', 'mamul-tablolari-turkce.txt', 'irab-taksimat-tablolari-turkce.txt']
    en = ledger('birgivi-awamil-inventory', "Birgivī's ʿAwāmil — the inventory tables (Ottoman and Turkish)", files, 'awamil',
                'One inventory stated four times (the Ottoman tables, and the Turkish amil / mamul / irab-taksimat sheets): ledgered once.')
    tab = lines('awamil-birgivi-tables.txt')

    def tline(word):
        w = H(word.split(' (')[0])
        for i, l in enumerate(tab, 1):
            if w and w in H(l):
                return i
        return None
    # what an engine line says for each family, and the authored line that proves a corpus sentence is that family
    FAM = {
        'Harf-i cerler (20)': ('حرف جر', 'حرف جر'),
        'İsmini nasb, haberini raf edenler (8)': ('مشبه بالفعل|ناسخ|حرف توكيد|حرف تمن|حرف ترج|حرف استدراك|حرف تشبيه', 'مشبه بالفعل|ناسخ|حرف توكيد ونصب|نفي الجنس'),
        'İsmini raf, haberini nasb edenler (2)': ('ليس|حجازي', 'ليس|حجازي'),
        'Fiil-i muzariyi nasb edenler (4)': ('نصب|مصدري', 'حرف نصب|ناصب'),
        'Cevazim (15)': ('جزم|شرط', 'جزم|جازم'),
    }
    BARE = {'كف (كَـ)': 'ك', 'لام': 'ل', 'فى': 'في', 'الى': 'الي', 'على': 'علي', 'رب': 'رب', 'واو القسم': 'و', 'تاء القسم': 'ت',
            'خلى (خَلَا)': 'خلا', 'عدى (عَدَا)': 'عدا', 'كيمه (كَيْ)': 'كيمه', 'اِن': 'ان', 'لام الأمر': 'ل', 'امر لامى (لام الأمر)': 'ل',
            'نهى لاسى (لا الناهية)': 'لا', 'ما مشابه بليس': 'ما', 'لا مشابه بليس': 'لا', 'كى': 'كي', 'انى': 'اني', 'اى': 'اي',
            'اذاما': 'اذاما', 'اذما': 'اذما'}
    n = 0
    for src, title, items in cc.CANON:
        fam = FAM.get(title)
        for name, ids in items:
            n += 1
            cb = note(ids)
            probe = None
            if fam:
                b = BARE.get(name, H(name).replace(' ', ''))
                # attached letters (ب ل ك و ت) never stand alone in the corpus: look them up with their host
                hits = corpus_hits(b, fam[1], limit=3) if len(b) > 1 else []
                if hits:
                    probe = {'any': [mprobe(h['s'], h['w'], fam[0]) for h in hits], 'at': [h['at'] for h in hits]}
                    cb.append({'type': 'engine', 'ref': 'Murib.line', 'at': hits[0]['at']})
            E(en, f'inv{n:03d}', tline(name) or (src + ':?'), name, 'row', cb, 'applied' if probe else ('noted' if cb else 'open'), probe,
              reason=None if (probe or cb) else 'no note names it')
    # the rows check_canon does not list: the nine marfūʿāt (TABLE 6) and the ten ʿatf letters (TABLE 11), the iʿrāb kinds
    MARFU = [('فاعل', ['al-marfuat-al-fail-wa-naibuh'], 'فاعل'), ('نائب فاعل', ['al-marfuat-al-fail-wa-naibuh'], 'نائب فاعل'),
             ('مُبْتَدَأ', ['al-mubtada-wa-nawah'], 'مبتدا'), ('خبر', ['al-mubtada-wa-nawah'], 'خبر'),
             ('"كَانَ" بابنك اسمى', ['kana-wa-akhawatuha'], 'اسم كان|اسم «كان»|اسمها|اسمه'),
             ('"اِنَّ" بابنك خبرى', ['inna-wa-akhawatuha'], 'خبر ان|خبر «ان»|خبرها'),
             ('جنسينى نفى ايجون اولان "لا"نك خبرى', ['la-nafiya-lil-jins'], 'خبر لا'),
             ('"لَيْسَ"يه مشابه اولان "ما" و "لا"نك اسمى', ['ma-la-mushabbaha'], 'اسم ما|اسم لا'),
             ('نواصب و جوازمدن خالى اولان فعل مضارع', ['mudari-marfu', 'al-amil-al-manawi'], 'فعل مضارع، مرفوع|فعل مضارع مرفوع')]
    ATF = ['وَاوْ', 'فَاء', 'ثُمَّ', 'حَتَّى', 'اَوْ', 'اِمَّا', 'اَمْ', 'لاَ', 'بَلْ', 'لَكِنْ']
    ATFB = {'وَاوْ': 'و', 'فَاء': 'ف', 'اَوْ': 'او', 'اِمَّا': 'اما', 'اَمْ': 'ام', 'لاَ': 'لا', 'بَلْ': 'بل', 'لَكِنْ': 'لكن', 'ثُمَّ': 'ثم', 'حَتَّى': 'حتي'}
    for name, ids, rx in MARFU:
        n += 1
        cb = note([i for i in ids if i in NOTES] or [k for k in NOTES if 'marfu' in k][:1])
        hits = role_hits(rx)
        probe = {'any': [mprobe(h['s'], h['w'], rx) for h in hits], 'at': [h['at'] for h in hits]} if hits else None
        if probe:
            cb.append({'type': 'engine', 'ref': 'Murib.line', 'at': hits[0]['at']})
        E(en, f'inv{n:03d}', tline(name.split('"')[1] if '"' in name else name) or 27, name, 'row', cb, 'applied' if probe else 'noted', probe)
    for a in ATF:
        n += 1
        b = ATFB[a]
        hits = corpus_hits(b, 'حرف عطف', limit=3) if len(b) > 1 else []
        probe = {'any': [mprobe(h['s'], h['w'], 'حرف عطف') for h in hits], 'at': [h['at'] for h in hits]} if hits else None
        cb = note(['al-atf-bil-huruf-wa-ahkamuh'])
        if probe:
            cb.append({'type': 'engine', 'ref': 'Murib.line', 'at': hits[0]['at']})
        E(en, f'inv{n:03d}', 44, a, 'row', cb, 'applied' if probe else 'noted', probe)
    # irab-taksimat-tablolari: the iʿrāb by essence (3), by attribute (3) — SignEngine
    tk = lines('irab-taksimat-tablolari-turkce.txt')
    SIGN = [('Hareke (Zamme, Fetha, Kesre)', 6, "SignEngine.CLASSES.length>=10"), ('Harf (Vav, Ya, Elif, Nun)', 6, "SignEngine.CLASSES.length>=10"),
            ('Hazif (Harekeyi Hazif, Ahiri Hazif, Nunu Hazif)', 6, "SignEngine.CLASSES.length>=10"),
            ("İ'rabı Lâfzî", 10, None), ("İ'rabı Takdiri", 10, None), ("İ'rabı Mahallî", 10, None)]
    for name, ln, _ in SIGN:
        n += 1
        E(en, f'inv{n:03d}', 'irab-taksimat-tablolari-turkce.txt:%d' % ln, name, 'row',
          note(['al-murab-wal-mabni-wal-irab', 'al-irab-wa-taqsimuhu-bil-dhat-wal-mahall']), 'noted')


def g_birgivi_examples():
    en = ledger('awamil-birgivi-ottoman', "Birgivī's ʿAwāmil — the Ottoman lesson sheet: one example per governor and per governed",
                ['awamil-birgivi-ottoman.txt', 'awamil-birgivi-tables.txt'], 'awamil')
    L = lines('awamil-birgivi-ottoman.txt')
    # the definitional lines (6–13) — ʿilm al-naḥw's definition, its aim, its subject, its founder, the book's author
    DEF = {6: 'tarif', 8: 'ghaya', 10: 'mawdu', 12: 'wadi', 13: 'musannif'}
    for ln, k in DEF.items():
        ar = L[ln - 1].strip()
        q = note_quoting(ar.split(':', 1)[-1], 12)
        E(en, f'def-{k}', ln, ar, 'rule', note(q, 'quotes') + bank('jami', 1), 'noted' if q else 'banked')
    # «X: example» pairs on lines 16–36 (and tables l. 11, 13): the book's own example for each governor / governed
    # expected engine wording per label
    EXP = {
        'مِنْ': ('كل', 'مجرور'), 'فِى': ('الجنة', 'مجرور'), 'كف': ('كمثله', 'مجرور|خبر'),
        'اِنَّ': ('الله', 'اسم ان|اسم «ان»|منصوب'), 'كَأَنَّ': ('الحرام', 'اسم كان|منصوب'),
        'مَتَى': ('تحسد', 'مجزوم'), 'لَمْ': ('يلد', 'مجزوم'), 'لَمَّا': ('ينفع', 'مجزوم'),
        'اِسْمْ مُضاَفْ': ('الله', 'مضاف اليه|مجرور'), 'مُطْلَقْ فِعِلْ': ('نزولا', 'مفعول مطلق'),
        'فاعل': ('الله', 'فاعل'), 'مُبْتَدَأ و خَبَرْ': ('محمد', 'مبتدا'), 'مَفْعُولُ بِهْ': ('الله', 'مفعول به'),
        '"اِنَّ" بابنك اسمى': ('السؤال', 'اسم ان|اسم «ان»'), 'حرف جرله مجرور': ('باخلاص', 'مجرور'),
        'صفة': ('العظيم', 'نعت|صفة'), 'بدل': ('حقه', 'بدل'), 'وَاوْ': ('رسوله', 'معطوف'),
        'ماَ': ('الله', 'اسم ما|مبتدا|اسمها'), 'اَنْ': ('اطيع', 'منصوب'), 'لَنْ': ('يضرب', 'منصوب'),
    }
    pairs = []
    for ln in list(range(14, 37)):
        l = L[ln - 1]
        for m in re.finditer(r'([^\s:][^:]{0,24}?):\s+([؀-ۿ][^\t:]*?)(?=\s{3,}|\t|$)', l):
            lab, ex = m.group(1).strip(), m.group(2).strip()
            if not re.search('[ً-ْ]', ex):
                continue
            pairs.append((ln, lab, ex))
    pairs.append((34, 'جوازمدن برى داخل اولان فعل مضارع', L[33].strip()))
    tb = lines('awamil-birgivi-tables.txt')
    for ln in (11, 13):
        for m in re.finditer(r'([^\s:|][^:|]{0,6}?):\s+([؀-ۿ][^\t:|]*?)(?=\s{3,}|\t|$)', tb[ln - 1]):
            pairs.append(('tables:%d' % ln, m.group(1).strip(), m.group(2).strip()))
    for i, (ln, lab, ex) in enumerate(pairs, 1):
        exp = EXP.get(lab) or {HN(k): v for k, v in EXP.items() if k not in ('اَنْ',)}.get(HN(lab))
        if lab == 'جوازمدن برى داخل اولان فعل مضارع':
            exp = ('تخلص', 'مجزوم|شرط')
        q = note_quoting(ex, 10)
        cb = note(q, 'quotes')
        probe = mprobe(ex, exp[0], exp[1]) if exp else None
        if probe:
            cb.append({'type': 'engine', 'ref': 'Murib.line'})
        E(en, f'ex{i:02d}', ln, f'{lab}: {ex}', 'example', cb, 'applied' if probe else ('noted' if q else 'open'), probe,
          reason=None if exp else 'label not mapped')
    # the reasons lines (15, 17–20, 22–25, 28, 37): why each family bears its name
    for ln in (15, 17, 18, 19, 20, 22, 23, 24, 25, 28):
        ar = L[ln - 1].strip()
        fam = 'huruf-jarr' if ln == 15 else 'inna-wa-akhawatuha' if ln < 21 else 'ma-la-mushabbaha' if ln < 25 else 'nawasib-wa-jawazim-al-mudari' if ln == 25 else 'al-amil-al-manawi'
        ids = [fam] if fam in NOTES else []
        E(en, f'why{ln}', ln, ar, 'rule', note(ids), 'noted' if ids else 'open', reason=None if ids else 'no note carries the reason')


def g_edatlar():
    en = ledger('edatlar-irab-soru-testi', 'The iʿrāb question test (Turkish): the question each role answers', ['edatlar-irab-soru-testi.txt'], 'awamil')
    L = lines('edatlar-irab-soru-testi.txt')
    for ln, l in enumerate(L, 1):
        if '=' not in l:
            continue
        lab, qs = l.split('=', 1)
        words = [w.strip() for w in re.split(r',', qs) if w.strip()]
        first = words[0]
        carriers = [k for k, v in NOTES.items() if first in json.dumps(v.get('question', {}), ensure_ascii=False)]
        E(en, f'q{ln}', ln, l.strip(), 'row', note(carriers), 'noted' if carriers else 'open',
          probe={'js': 'Object.values(GRAMMAR).some(n=>JSON.stringify(n.question||{}).includes(%s))' % json.dumps(first, ensure_ascii=False)} if carriers else None)


def q_markers(name, sizes, bank_names):
    """the numbered questions of a sual-cevap file, by script: each «N-» / «﴿N﴾» marker in reading order, assigned to the
    section whose next expected number it is (sub-lists inside an answer restart at 1 and are skipped)."""
    L = lines(name)
    hits = []
    for ln, l in enumerate(L, 1):
        for m in re.finditer(r'(?:﴿\s*([٠-٩۰-۹]+)\s*﴾?|([٠-٩۰-۹]+)\s*[-–])', l):
            hits.append((ln, int((m.group(1) or m.group(2)).translate(TRD))))
    sec, nxt, found = 0, 1, {}
    for ln, n in hits:
        if sec >= len(sizes):
            break
        if n == nxt:
            found[(sec, n)] = ln
            nxt += 1
        elif n == 1 and nxt > sizes[sec] * 0.6:
            sec += 1; nxt = 2
            if sec < len(sizes):
                found[(sec, 1)] = ln
        if sec < len(sizes) and nxt > sizes[sec]:
            sec += 1; nxt = 1
    out = []
    for s, size in enumerate(sizes):
        for n in range(1, size + 1):
            out.append((bank_names[s], n, found.get((s, n))))
    return out


def g_banks():
    for key, title, name, sizes, banks in [
        ('mensubat', 'The Ottoman naḥw notebook (manṣūbāt … ḥarf) — sual-cevap', 'mensubat.txt', None, ['mansubat', 'majrurat', 'tawabi', 'mabni', 'fil', 'harf']),
        ('molla-cami-sual-cevap', "Molla Jāmī's sharḥ — sual-cevap", 'molla-cami-sual-cevap.txt', None, ['jami']),
        ('alaka-suallar', 'The ʿalāqa question sheet (Ottoman)', 'alaka-suallar.txt', None, ['alaka'])]:
        en = ledger(key, title, [name], 'awamil' if key != 'alaka-suallar' else 'balagha')
        sizes = [len(BANKS[b]['items']) for b in banks]
        if key == 'molla-cami-sual-cevap':
            sizes = [29, 26, 25]; banks3 = ['jami'] * 3
            offs = [0, 29, 55]
            marks = q_markers(name, sizes, banks3)
            for (b, n, ln), sec in zip(marks, [0] * 29 + [1] * 26 + [2] * 25):
                pass
            nn = 0
            for idx, (b, n, ln) in enumerate(marks):
                sec = 0 if idx < 29 else 1 if idx < 55 else 2
                gn = offs[sec] + n
                it = [i for i in BANKS['jami']['items'] if i['n'] == gn]
                E(en, f's{sec + 1}q{n}', ln, '', 'question', [{'type': 'bank', 'ref': it[0]['id']}] if it else [], 'banked' if it else 'open')
            continue
        marks = q_markers(name, sizes, banks)
        for b, n, ln in marks:
            E(en, f'{b}-q{n}', ln, '', 'question', bank(b, n), 'banked' if bank(b, n) else 'open')



# ================================================================ prose sources: one entry per page / heading / bullet, carried by topic
def fold(s):
    s = str(s).replace('İ', 'i').replace('I', 'ı').lower()
    for a, b in zip('çğıöşüâîûêô', 'cgiosuaiueo'):
        s = s.replace(a, b)
    return re.sub(r"[’'`ʼ‘\-]", '', s)


BIRG = {  # the Birgivī sheet's own examples (proved in awamil-birgivi-ottoman), re-used as the topic's proof
    'jarr': mprobe('تُبْتُ مِنْ كُلِّ ذَنْبٍ', 'كل', 'مجرور'),
    'jazm': mprobe('لَمْ يَلِدْ وَلَمْ يُولَدْ', 'يلد', 'مجزوم'),
    'shart': mprobe('مَتَى تَحْسُدْ تَهْلُكْ', 'تحسد', 'مجزوم'),
    'fail': mprobe('رَحِمَ اللهُ تَعاَلَى اَلتَّاءِبَ', 'الله', 'فاعل'),
    'mubtada': mprobe('مُحَمَّدٌ خاَتَمُ الْاَنْبِياَءِ عَلَيْهِمُ الصَّلاَةُ وَالسَّلاَمُ', 'محمد', 'مبتدا'),
    'mutlaq': mprobe('وَنَزَلَ الْقُرْأَنُ نُزُولاً', 'نزولا', 'مفعول مطلق'),
    'idafa': mprobe('عِباَدَةُ اللهِ تَعاَلىَ خَيْرٌ', 'الله', 'مضاف اليه|مجرور'),
    'naat': mprobe('اَعْبُدُ اللهَ الْعَظِيمَ', 'العظيم', 'نعت|صفة'),
    'atf': mprobe('اُطِيعُ اللهَ وَ رَسُولَهُ', 'رسوله', 'معطوف'),
}


def cprobe(word, authored, engine=None, limit=3):
    h = corpus_hits(word, authored, limit=limit)
    return {'any': [mprobe(x['s'], x['w'], engine or authored) for x in h], 'at': [x['at'] for x in h]} if h else None


def rprobe(rx, engine=None, prev=None):
    h = role_hits(rx, prev=prev)
    return {'any': [mprobe(x['s'], x['w'], engine or rx) for x in h], 'at': [x['at'] for x in h]} if h else None


def J(expr):
    return {'js': expr}


# topic: (id, regex over the folded unit text, note ids, probe-maker) — a unit is carried by every topic it names
TOPICS = [
    ('nahw-tarif', r'nahiv (ilminin|ilmi)|علم النحو|ilm-?i nahv', ['al-kalima-wal-kalam'], None),
    ('amil', r'\bamil|عامل|عوامل|avamil|sema.?i\b', ['al-amil-wa-aqsamuh'], None),
    ('lazim', r'muteaddi|müteaddi|lazim fiil|\blazim\b|متعدي|لازم', ['al-lazim-wal-mutaaddi', 'al-mutaaddi-wa-afal-al-qulub'], lambda: J("typeof LazimEngine==='function'")),
    ('kalima-kalam', r'\bkelime\b|\bkelam\b|كلمة|الكلام|cumle:|^\s*fiil\b|^\s*harf\b|fiil:|harf:', ['al-kalima-wal-kalam'], None),
    ('jarr', r'harf-?i ?cer|harfi cer|cer harf|حرف جر|حروف الجر|تجر|mecrur|\bjarr\b', ['huruf-jarr', 'huruf-jarr-nawadir', 'al-majrur-bil-harf-wa-bil-idafa'], lambda: BIRG['jarr']),
    ('inna', r'inne|ismini nasb|إن واخوات|ان ve|مشبهة بالفعل|حروف مشبه|elif-?nun|muzahlaka|kesre.?fetha', ['inna-wa-akhawatuha'], lambda: cprobe('ان', 'مشبه بالفعل|ناسخ', 'مشبه بالفعل|ناسخ|توكيد')),
    ('laysa', r'leyse|ليس|ismini ref,? haberini nasb', ['ma-la-mushabbaha', 'ma-la-laysa-wa-la-al-jins'], None),
    ('nawasib', r'nasb ?ed(en|er)|nevasib|نواصب|nasbeden', ['nawasib-wa-jawazim-al-mudari', 'an-masdariyya'], lambda: cprobe('لن', 'نصب', 'نصب|ناصب')),
    ('jawazim', r'cezm|cevazim|cazim|جوازم|meczum', ['nawasib-wa-jawazim-al-mudari', 'lam-jazim', 'al-majzum-wal-shart-wal-jaza'], lambda: BIRG['jazm']),
    ('shart', r'sart edat|şart|\bsart\b|شرط|mucazat|cevab-?i sart|متي ت', ['al-majzum-wal-shart-wal-jaza'], lambda: BIRG['shart']),
    ('qiyasi', r'kiyasi|قياسي|ismi fail|ism-?i fail|ismi meful|ism-?i meful|sifat-?i musebbehe|sifati musebbehe|tefdil|tafdil|masdar', ['al-amil-wa-aqsamuh', 'imal-al-masdar', 'amal-ism-al-tafdil-wal-masdar'], None),
    ('manawi', r'manevi|معنوي|ma.nevi', ['al-amil-al-manawi'], None),
    ('kana', r'\bkane\b|kane ve kardes|nakis fiil|nakise|nevasih|كان واخوات|الافعال الناقصة|كان ve', ['kana-wa-akhawatuha', 'al-fil-al-tamm-wal-naqis'], lambda: cprobe('كان', 'ناقص', 'ناقص')),
    ('fail', r'\bfail\b|فاعل', ['al-marfuat-al-fail-wa-naibuh'], lambda: BIRG['fail']),
    ('naib', r'naib-?i ?fail|naibi fail|نائب', ['al-marfuat-al-fail-wa-naibuh', 'al-majhul-fil-kafiya'], lambda: rprobe('نائب فاعل', prev='مبني للمجهول|مبني لما لم يسم')),
    ('mubtada', r'mubteda|mübteda|مبتدا|haber', ['al-mubtada-wa-nawah', 'mubtada-khabar', 'khabar-al-mubtada-wa-ahkamuh'], lambda: BIRG['mubtada']),
    ('mafulbih', r'meful(u|ü)? ?bih|mefulun bih|مفعول به', ['al-maful-bihi-wa-qismah'], lambda: rprobe('مفعول به')),
    ('mutlaq', r'mutlak meful|mefulu mutlak|meful(u|ü)? ?mutlak|مفعول مطلق', ['al-mansubat-al-maful-al-mutlaq'], lambda: BIRG['mutlaq']),
    ('mafulfih', r'meful(u|ü)? ?fih|zarf|ظرف|مفعول فيه', ['al-maful-fih-wal-maful-lah'], lambda: rprobe('ظرف زمان|ظرف مكان|مفعول فيه')),
    ('mafullah', r'meful(u|ü)? ?leh|مفعول له|مفعول لاجله', ['al-maful-fih-wal-maful-lah'], lambda: mprobe('ضَرَبْتُ زَيْدًا تَأْدِيبًا', 'تاديبا', 'مفعول لاجله|مفعول له')),  # mensubat.txt's own example
    ('mafulmaah', r'meful(u|ü)? ?mea|مفعول معه', ['al-maful-maah-wal-hal'], lambda: rprobe('مفعول معه')),
    ('hal', r'\bhal\b|حال', ['al-maful-maah-wal-hal', 'al-hal-jumla-wa-rabituha'], lambda: rprobe('حال')),
    ('tamyiz', r'temyiz|تمييز', ['al-tamyiz-wa-ahkamuh'], lambda: rprobe('تمييز')),
    ('istithna', r'istisna|mustesna|استثناء|مستثني', ['al-mustathna-wa-nawah-wa-nasbuh', 'al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa'], lambda: rprobe('مستثني')),
    ('lajins', r'cinsini nef|نافية للجنس|لا التي لنفي', ['la-nafiya-lil-jins'], lambda: rprobe('اسم لا النافية للجنس|اسم «لا»')),
    ('munada', r'munada|nida|نداء|منادي|terhim|tarkhim|nudbe|nudba|istigase', ['al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada'], lambda: J("NidaEngine.read('يَا زَيْدُ').ok===true")),
    ('idafa', r'izafet|izafe|muzaf|اضافة|مضاف', ['al-mudaf-wa-nawa-al-idafa', 'al-majrur-bil-harf-wa-bil-idafa'], lambda: BIRG['idafa']),
    ('naat', r'\bsifat\b|\bnaat\b|نعت|صفة', ['jumla-sifa'], lambda: BIRG['naat']),
    ('atf', r'atif|atf|عطف|matuf', ['al-atf-bil-huruf-wa-ahkamuh', 'atf-nasaq', 'atf-bayan'], lambda: BIRG['atf']),
    ('tawkid', r'te.?kid|tekid|توكيد|تأكيد', ['al-tawkid-al-lafzi-wal-manawi'], lambda: rprobe('توكيد')),
    ('badal', r'bedel|بدل', ['al-badal-wa-aqsamuh-wa-atf-al-bayan'], lambda: rprobe('بدل')),
    ('irab', r'irab|i.?rab|اعراب|murab|mureb|mebni|مبني|معرب', ['al-murab-wal-mabni-wal-irab', 'al-irab-wa-taqsimuhu-bil-dhat-wal-mahall'], lambda: J('SignEngine.seedAudit().bad.length===0')),
    ('signs', r'alamet|علامة|esmayi sitte|esma-?i sitte|tesniye|muesenna|cem.?i|cemi muzekker|cemi muennes|muzekker salim|muennes salim|الاسماء الستة', ['al-murab-wal-mabni-wal-irab', 'al-muthanna'], lambda: J('SignEngine.seedAudit().bad.length===0')),
    ('taqdiri', r'takdir|تقدير|teazzur|istiskal|istiskal|munasebet', ['al-taqdiri-al-rabi-ila-al-sadis-al-ya-wal-waw-wal-murab-bil-huruf-qabl-al-sakin', 'al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki'], lambda: rprobe('مقدرة|المقدرة', 'مقدر')),
    ('mahalli', r'mahall|محل', ['al-irab-wa-taqsimuhu-bil-dhat-wal-mahall'], lambda: rprobe('في محل', 'في محل')),
    ('mamnu', r'gayr-?i? ?munsar|gayri munsarif|munsarif|ممنوع من الصرف|غير منصرف|sarfi engelleyen|dokuz sebep', ['mamnu-min-sarf'], lambda: J("MamnuEngine.verdict('أَحْمَدُ').barred===true")),
    ('jumla', r'cumle irab|cumlenin irab|cumleler|الجملة|جملة|mahalli olan cumle|mahalli olmayan', ['anwa-al-jumal'], lambda: mprobe('زَيْدٌ قَامَ أَبُوهُ', 'قام', 'في محل رفع خبر')),
    ('damir', r'zamir|ضمير', ['al-mabni-wal-mudmar', 'al-marifa-al-mudmarat-wal-alam'], lambda: rprobe('ضمير منفصل', 'ضمير')),
    ('ishara', r'isaret|ism-?i isaret|اسم الاشارة|اشارة', ['asma-al-ishara', 'asma-al-ishara-wal-mawsulat'], lambda: cprobe('هذا', 'اشارة', 'اشارة')),
    ('mawsul', r'mevsul|موصول', ['asma-al-ishara-wal-mawsulat'], lambda: cprobe('الذي', 'موصول', 'موصول')),
    ('tanwin', r'tenvin|تنوين', ['kalla-wa-ta-al-tanith-wal-tanwin-fil-kafiya'], None),
    ('afalkhamsa', r'emsile|الافعال الخمسة|ef.?al-?i hamse', ['afal-khamsa'], None),
    ('asmaafal', r'isim fiil|ism-?i fiil|isim-fiil|isim fiil|esma-?i ef.?al|اسم فعل|اسماء الافعال|savt|esvat', ['asma-al-afal-wal-aswat-wal-murakkabat'], None),
    ('marifa', r'marife|nekre|معرفة|نكرة|alem\b|علم', ['al-marifa-wal-nakira-fil-kafiya'], None),
    ('tasgir', r'tasgir|tesgir|تصغير', [], lambda: J("IsmEngine.mughniAudit().bad.length===0")),
    ('nisba', r'nisbe|ism-?i mensup|نسبة|mensup', ['ism-mansub'], lambda: J("IsmEngine.mughniAudit().bad.length===0")),
    ('adad', r'sayi|sayilar|aded|adet|عدد', ['asma-al-adad-fil-kafiya'], lambda: J("AdadEngine.name(125)==='مِائَةٌ وَخَمْسَةٌ وَعِشْرُونَ'")),
    ('muannath', r'muennes|muzekker|مؤنث|مذكر|te.?nis', ['al-muannath-wa-alamatuh'], None),
    ('jam', r'cem.?i mukesser|mukesser|cem.?i kille|jam.? qilla|تكسير|kille', ['al-jumu-wa-tanith-amiliha'], None),
    ('qulub', r'kalp fiil|kulub|zanne|ظن واخوات|ظن ve|افعال القلوب|yakin fiil|bilgi fiil|ilga|talik', ['al-mutaaddi-wa-afal-al-qulub', 'zanna-wa-akhawatuha'], None),
    ('muqaraba', r'mukarebe|mukarabe|reca|şuru|suru fiil|افعال المقاربة|كاد', ['afal-al-muqaraba'], lambda: J("typeof MuqarabaEngine==='function'&&MuqarabaEngine.toString().length>100")),
    ('madh', r'medh|zemm|نعم|بئس|مدح|ذم', ['afal-al-madh-wal-dhamm-fil-kafiya'], None),
    ('taajjub', r'taaccub|taaccüp|teaccub|تعجب', ['fil-al-taajjub-fil-kafiya'], None),
    ('tanazu', r'tenazu|tanazu|تنازع', ['tanazu'], lambda: J('TartibEngine.seedAudit().bad.length===0')),
    ('tartib', r'takdim|tehir|tekaddum|öne gec|one gec|sira|precedence', [], lambda: J('TartibEngine.seedAudit().bad.length===0')),
    ('hadhf', r'hazf|hazif|حذف|istigal|istiğal|tahzir|ishtighal|اشتغال|تحذير|ighra', ['ijaz-al-hadhf', 'hadhf-al-mudaf-wal-mudaf-ilayh'], lambda: J('HadhfEngine.seedAudit().bad.length===0')),
    ('waqf', r'vakf|وقف', [], lambda: J("WaqfEngine.pause('كِتَابًا').ok===true")),
    ('nafy', r'nefy|nefi|نفي|olumsuz', ['la-nafiya'], None),
    ('istifham', r'istifham|soru edat|استفهام', ['al-istifham'], lambda: J("typeof IstifhamEngine==='function'")),
    # ṣarf
    ('sarf-tarif', r'sarf ilm|ilm-?i sarf|علم الصرف|sarfin tarif', ['thulathi-mujarrad-babs'], None),
    ('madi', r'mazi|ماضي|الماضي', ['al-fil-wal-madi-wal-mudari-fil-kafiya'], lambda: J("sarfDerive(nakilClass({root:'ن ص ر'}),'I',1).mazi[0]==='نَصَرَ'")),
    ('mudari', r'muzari|مضارع', ['al-fil-wal-madi-wal-mudari-fil-kafiya', 'mudari-marfu'], lambda: J("sarfDerive(nakilClass({root:'ن ص ر'}),'I',1).mudari[0]==='يَنْصُرُ'")),
    ('amr', r'\bemr\b|emir|emri hazir|امر', ['al-amr-wa-wujuhuh', 'imperative-amr'], lambda: J("sarfDerive(nakilClass({root:'ن ص ر'}),'I',1).amr[0]==='اُنْصُرْ'")),
    ('majhul', r'mechul|meçhul|majhul|مجهول', ['al-majhul-fil-kafiya'], None),
    ('bab', r'\bbab|babi|بابا?|mezid|mücerred|mucerred|ziyade|ruba|مزيد|مجرد', ['thulathi-mujarrad-babs', 'augmented-babs', 'rubai-babs'], lambda: J('Bab35Engine.audit().bad.length===0')),
    ('iftial', r'iftial|ifti.?al|افتعال', [], lambda: J("NAKIL_BABS[4].make('ض','ر','ب','sound')==='اِضْطَرَبَ'")),
    ('tawkidnun', r'nun.?u tekid|nun-u te.?kid|tekid nun|نون التوكيد', ['nun-tawkid'], lambda: J('TawkidNunEngine.seedCheck().every(x=>x.ok)')),
    ('idgham', r'idgam|idğam|ادغام|muzaaf|mudaaf|mudaf fiil', [], lambda: J('IdghamRuleEngine.seedCheck().every(x=>x.ok)')),
    ('mithal', r'misal|مثال|mu.?tell?u.?l.?fa', ['mithal-verbs'], lambda: {'ilal': 'يَوْعِدُ', 'out': 'يَعِدُ'}),
    ('ajwaf', r'ecvef|اجوف|mu.?tell?u.?l.?ayn', ['hollow-verbs'], lambda: {'ilal': 'قَوَلَ', 'out': 'قَالَ'}),
    ('naqis', r'nakis(?! fiil)|ناقص|mu.?tell?u.?l.?lam', ['naqis-verbs'], lambda: {'ilal': 'دُعِوَ', 'out': 'دُعِيَ'}),
    ('lafif', r'lefif|lafif|لفيف', [], None),
    ('mahmuz', r'mehmuz|mahmuz|مهموز|hemze', [], None),
    ('ismfailtab', r'ism-?i fail cekim|ismi fail cekim|ism-?i meful cekim|ismi meful', ['ism-fail', 'ism-maful'], lambda: {'ilal': 'مَقْوُولٌ', 'out': 'مَقُولٌ'}),
    ('ilal', r'i.?lal|iglal|اعلال|kalb|illet', ['hollow-verbs', 'naqis-verbs', 'mithal-verbs'], lambda: {'ilal': 'قَوَلَ', 'out': 'قَالَ'}),
]


def topic_carriers(text):
    f = fold(text) + ' ' + H(text)
    cb, probes, tops = [], [], []
    for tid, rx, ids, mk in TOPICS:
        if re.search(rx, f):
            tops.append(tid)
            cb += [c for c in note([i for i in ids if i in NOTES]) if c not in cb]
            if mk:
                p = PROBE_CACHE.get(tid)
                if p is None:
                    p = PROBE_CACHE[tid] = mk() or False
                if p:
                    probes.append((tid, p))
    return tops, cb, probes


PROBE_CACHE = {}


def prose_entry(en, id, ln, text, kind='section', na=None):
    tops, cb, probes = topic_carriers(text)
    head = re.sub(r'\s+', ' ', text.strip())[:160]
    if na and not tops:
        return E(en, id, ln, head, kind, [], 'not-automatable', reason=na)
    if probes:
        cb.append({'type': 'engine', 'ref': ','.join(t for t, _ in probes), 'topics': tops})
        pr = probes[0][1] if len(probes) == 1 else {'all': [p for _, p in probes][:4]}
        return E(en, id, ln, head, kind, cb, 'applied', pr)
    if cb:
        cb.append({'type': 'topics', 'ref': ','.join(tops)})
        return E(en, id, ln, head, kind, cb, 'noted')
    return E(en, id, ln, head, kind, [], 'open', reason='no topic of the app named on this ' + kind + (' (' + ','.join(tops) + ')' if tops else ''))


def pages(name):
    L = lines(name)
    out, cur, start = [], [], None
    for i, l in enumerate(L, 1):
        m = re.match(r'(?:===== PAGE (\d+) =====|\[page (\d+)\])', l)
        if m:
            if start is not None:
                out.append((pg, start, '\n'.join(cur)))
            pg, start, cur = int(m.group(1) or m.group(2)), i, []
            continue
        if start is not None:
            cur.append(l)
    if start is not None:
        out.append((pg, start, '\n'.join(cur)))
    return out


def g_prose():
    for key, title, name, group in [
        ('avamil-dersi-servet-hayma-2023', 'Avâmil Dersi (Servet Hayma, 2023) — the 44-page lecture', 'avamil-dersi-servet-hayma-2023.txt', 'awamil'),
        ('serhul-mugni-ders-notlari-kisa-1', "Şerhu'l-Muğnî ders notları — kısa 1 (96 pages)", 'serhul-mugni-ders-notlari-kisa-1.txt', 'awamil'),
        ('izzi-sarf-grafikleri', 'İzzî Kitabı Grafikleri (48 infographic pages)', 'izzi-sarf-grafikleri.txt', 'sarf')]:
        en = ledger(key, title, [name], group)
        for pg, ln, txt in pages(name):
            if len(re.sub(r'\s', '', txt)) < 40:
                E(en, f'p{pg}', ln, txt.strip()[:80], 'page', [], 'not-automatable', reason='a near-empty page (a picture or a title)')
                continue
            prose_entry(en, f'p{pg}', ln, txt, 'page')
    # the Kâfiye summary: one entry per (sNsM) heading
    en = ledger('nahiv-kafiye-ozeti-turkce', 'Nahiv — Kâfiye Özeti (14-page Turkish summary keyed to the matn)', ['nahiv-kafiye-ozeti-turkce.txt'], 'awamil')
    L = lines('nahiv-kafiye-ozeti-turkce.txt')
    heads = [i for i, l in enumerate(L, 1) if re.search(r'\(s\d+s\d*\)', l) and i > 15]
    for k, h in enumerate(heads):
        nxt = heads[k + 1] if k + 1 < len(heads) else len(L) + 1
        txt = '\n'.join(L[h - 1:nxt - 1])
        ref = re.search(r'\(s\d+s\d*\)', L[h - 1]).group(0)
        prose_entry(en, f'h{k + 1:03d}{ref}', h, txt, 'rule')
    # Qaṭr al-Nadā (distilled notes): the matn's structure items (· separated) and the cross-check bullets
    en = ledger('qatr-al-nada-turkish-cicek', 'Qaṭr al-Nadā — Turkish rendering (Çiçek 2020), distilled study notes', ['qatr-al-nada-turkish-cicek.txt'], 'awamil')
    L = lines('qatr-al-nada-turkish-cicek.txt')
    blk, n = [], 0
    joined = ' '.join(L[i - 1].strip() for i in range(13, 41))
    for part in joined.split('·'):
        if len(part.strip()) > 8:
            blk.append((13, part))
    for i, l in enumerate(L, 1):
        if l.startswith('- '):
            blk.append((i, l + ' ' + (L[i] if i < len(L) and L[i].startswith('  ') else '')))
    for i, part in blk:
        n += 1
        prose_entry(en, f'b{n:02d}', i, part, 'rule')
    # the Turkish iʿrāb-taksimat: what survives the OLE noise (rows with Turkish words)
    en = ledger('irab-taksimat-turkish', 'İrab taksimatı (Turkish .doc; ~95% OLE noise)', ['irab-taksimat-turkish.txt'], 'awamil',
                'The readable fragments are ledgered one per line; the rest is binary noise (one not-automatable entry).')
    L = lines('irab-taksimat-turkish.txt')
    keep = [(i, l) for i, l in enumerate(L, 1) if len(re.findall(r'[A-Za-zÇĞİÖŞÜçğıöşü]{4,}', l)) >= 3 or len(re.findall('[ء-ي]{3,}', l)) >= 3]
    for i, l in keep:
        prose_entry(en, f'l{i}', i, l, 'row', na='a fragment with no grammar term')
    E(en, 'noise', f'1-{len(L)}', f'{len(L) - len(keep)} lines of OLE binary noise', 'row', [], 'not-automatable', reason='undecodable bytes; a clean .doc is needed')
    # the Jurjānī slide deck: the classification claims (l. 8–15)
    en = ledger('avamil-curcani-slides', "ʿAwāmil of al-Jurjānī — slide deck notes (kind 1 transcribed)", ['avamil-curcani-slides.txt'], 'awamil')
    L = lines('avamil-curcani-slides.txt')
    for i in range(8, 14):
        l = L[i - 1]
        if l.startswith('- '):
            prose_entry(en, f'c{i}', i, l, 'rule')
    E(en, 'walk', 14, L[13].strip(), 'rule', [], 'not-automatable', reason='the per-particle walk is in the PDF (pages 10–80), not in this file')
    E(en, 'rest', 17, L[16].strip(), 'rule', [], 'not-automatable', reason='pages 10–80 of the PDF were never transcribed into the file: nothing in the file to carry')


# ================================================================ group 2: the ṣarf tables and rule sheets
JSN = "const N=s=>IlalEngine.join(IlalEngine.parse(String(s||'').normalize('NFC').replace(/[أإآ]/g,'ا').replace(/(.)اَ/g,'$1ا').replace(/َ(?=ا)/g,'').replace(/ى/g,'ي').replace(/[ًٌٍ]/g,'').replace(/ا$/,'')));"


def g_sarf():
    # 1. the nakil table: 11 model roots × 12 augmented wazns (two transcriptions of one .xls)
    en = ledger('bablara-nakil', 'Bablara nakil — 11 model roots carried through the 12 augmented wazns', ['bablara-nakil-12-wazn.txt', 'bablara-nakil-tablosu.txt'], 'sarf',
                'The second file is the first minus its preamble (cells identical): ledgered once.')
    L = lines('bablara-nakil-12-wazn.txt')
    rows = [[c.strip() for c in L[i].split('|')] for i in range(10, 22)]
    roots = [re.sub('[^ء-ي]', '', H(c))[1:] for c in rows[0][:11]]
    for r, row in enumerate(rows):
        wazn = row[11]
        for k, cell in enumerate(row[:11]):
            rt = ' '.join(roots[k])
            js = ("(()=>{" + JSN + "const c=nakilClass({root:%s});const [f,a,l]=c.rs;const B=NAKIL_BABS[%d];return N(B.make(f,a,l,c.type))===N(%s)})()"
                  % (json.dumps(rt, ensure_ascii=False), r, json.dumps(cell, ensure_ascii=False)))
            E(en, f'{wazn}:{roots[k]}', 11 + r, cell, 'cell', [{'type': 'engine', 'ref': 'NAKIL_BABS[%d].make' % r}], 'applied', {'js': js})
    # 2. the 35 doors
    en = ledger('sarf-35-bab-tablosu', 'İlmi sarfın babları otuzbeştir — the 35 doors with binā and ʿalāma', ['sarf-35-bab-tablosu.txt'], 'sarf',
                'Two sheets of one table (kısa l. 1–39, Türkçe l. 41–85); the full sheet (l. 51–85, 35 rows) is ledgered, the short one is its subset.')
    L = lines('sarf-35-bab-tablosu.txt')
    data = [i for i in range(51, 86) if re.search('[ء-ي]', L[i - 1])]
    for n, ln in enumerate(data, 1):
        cells = [c.strip() for c in L[ln - 1].split('|') if c.strip()]
        ar = [c for c in cells if re.search('[ء-ي]', c)]
        mz, wz = ar[-2:-1], ar[-1:]   # the row reads … mawzūn | wazn
        mawzun = mz[-1] if mz else ''
        lt = lambda c: re.sub('[^\u0621-\u064A]', '', H(c.split()[0].split('-')[0]))
        mazi, pat = lt(mawzun), lt(wz[0]) if wz else ''
        # the radicals stand where the wazn has ف ع ل — and, in a door attached to the quadriliteral, where it has its و / ي
        root = [ch for k, (ch, pc) in enumerate(zip(mazi, pat)) if (pc in 'فعل' and not (pc == 'ع' and 'ع' in pat[:k])) or (n >= 19 and pc in 'وي' and 0 < k < len(pat) - 1)] if len(mazi) == len(pat) else []
        js = ("(()=>{const x=Bab35Engine.derive(%s,%d);const H=s=>stripAr(String(s||'')).replace(/[^ء-ي]/g,'').replace(/[أإآ]/g,'ا').replace(/ى/g,'ي');"
              "return !!x.ok&&H(x.mazi[0])===%s&&Bab35Engine.audit().rows.find(r=>r.n===%d).ok})()"
              % (json.dumps(root, ensure_ascii=False), n, json.dumps(mazi.replace('ى', 'ي'), ensure_ascii=False), n))
        E(en, f'door{n:02d}', ln, ' | '.join(ar), 'row', [{'type': 'engine', 'ref': 'Bab35Engine.door(%d)' % n}], 'applied', {'js': js})
    for ln in range(43, 50):
        E(en, f'tally{ln}', ln, L[ln - 1].strip(' |'), 'row', [{'type': 'engine', 'ref': 'Bab35Engine.byGroup'}], 'applied',
          {'js': "Bab35Engine.DOORS.length===35"})
    # 3. the muhtelife of a ziyade bāb (أَكْرَمَ)
    en = ledger('ziyade-bab-muhtelife-cekimi', 'Ziyade bablardan muhtelife çekimi — the recitation of أَكْرَمَ with its extension rows', ['ziyade-bab-muhtelife-cekimi.txt'], 'sarf')
    L = lines('ziyade-bab-muhtelife-cekimi.txt')
    MAP = {'Fiili mazi': 'Fiil-i mâzî', 'Fiili muzari': 'Fiil-i muzâri', 'Mastar gayri mimi': 'Masdar (gayr-i mîmî)', 'İsmi fail': 'İsm-i fâil',
           'İsmi meful': "İsm-i mef'ûl", 'Cahdı mutlak': 'Cahd-ı mutlak', 'Cahdı müstarak': 'Cahd-ı müstağrak', 'Nefi hal': 'Nefy-i hâl',
           'Nefi istikbal': 'Nefy-i istikbâl', "Te'kidi nefi istikbal": "Te'kîd-i nefy-i istikbâl", 'Emri ğaib': 'Emr-i gâib', 'Nehyi ğaib': 'Nehy-i gâib',
           'emri hazır': 'Emr-i hâzır', 'Nehyi hazır': 'Nehy-i hâzır', 'Mastar mimi, ismi zaman, ismi mekan': 'Masdar-ı mîmî; ism-i zaman ve mekân',
           'Mastar binai merre': 'Binâ-i merre', 'Mastar binai nevi': "Binâ-i nev'", 'İsmi mensup': 'İsm-i mensûb', 'İsmi tefdıl': 'İsm-i tafdîl (şedde ile)',
           'Fiili teaccüp evvel': 'Fiil-i taaccüb-i evvel', 'Fiili teaccüp sani': 'Fiil-i taaccüb-i sânî'}
    for ln in range(9, 23, 2):
        arc = [c.strip() for c in L[ln - 1].split('|')]
        lab = [c.strip() for c in L[ln].split('|')]
        for a, b in zip(arc, lab):
            if b in MAP and a and '…' not in a:
                first = a.split()[0] if b.startswith('Mastar mimi') else a
                js = ("(()=>{" + JSN + "const m=muhtelife(sarfDerive(nakilClass({root:'ك ر م'}),'IV',1));const r=m.find(x=>x.tr===%s);"
                      "return !!r&&N(r.ar.replace(/^(فَهُوَ|وَذَاكَ) /,''))===N(%s.replace(/^(فَهُوَ|وَذَاكَ) /,'').replace(/^وَ /,'وَ'))})()"
                      % (json.dumps(MAP[b], ensure_ascii=False), json.dumps(first, ensure_ascii=False)))
                E(en, MAP[b], ln, f'{b}: {a}', 'cell', [{'type': 'engine', 'ref': 'muhtelife() / ziyadeExt()'}], 'applied', {'js': js})
            elif '…' in a and b:
                E(en, 'none:' + b, ln, f'{b}: {a}', 'cell', [{'type': 'engine', 'ref': 'ziyadeExt() gives no such row'}], 'applied',
                  {'js': "muhtelife(sarfDerive(nakilClass({root:'ك ر م'}),'IV',1)).every(r=>!/alet|bala|tasg|tesg|teşg/i.test(r.tr))"})
    E(en, 'rule-l23', 23, L[22].strip(), 'rule', [{'type': 'engine', 'ref': 'ziyadeExt()'}], 'applied',
      {'js': "muhtelife(sarfDerive(nakilClass({root:'ك ر م'}),'IV',1)).every(r=>!/alet|bala|tasg|tesg|teşg/i.test(r.tr))"})
    # 4. the iʿlāl rule sheet: every «X aslında Y idi» derivation, and the rule sentences
    en = ledger('ilal-kaideleri-turkce', "İ'lal kaideleri — kalb, naql and ḥadhf with worked derivations", ['ilal-kaideleri-turkce.txt'], 'sarf')
    L = lines('ilal-kaideleri-turkce.txt')
    seen = set()
    for i, l in enumerate(L, 1):
        for m in re.finditer(r'([ء-ْ]+)\s*aslında\s*([ء-ْ]+)', l.replace('ـ', '')):
            x, y = m.group(1), m.group(2)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            E(en, f'd{i}-{len(seen)}', i, f'{x} ← {y}', 'derivation', [{'type': 'engine', 'ref': 'IlalEngine.derive'}], 'applied', {'ilal': y, 'out': x})
    for i, l in enumerate(L, 1):
        if re.search(r'(olduğu zaman|kalb olunur|terk edilir|sakin kılınır|idğam olunur|nakledilir)', l) and 'aslında' not in l and i > 10:
            nxt = next((e for e in en if isinstance(e['line'], int) and e['line'] > i and e.get('probe') and ('ilal-kaideleri-turkce', e['id']) not in SLIPS), None)
            E(en, f'rule{i}', i, l.strip(), 'rule', [{'type': 'engine', 'ref': 'IlalEngine.RULES'}], 'applied', nxt['probe'] if nxt else None)
    for i, l in enumerate(L, 1):
        if re.match(r'(Ecvef|Nakıs)', l.strip()) and 'aslında' not in l and len(l.strip()) > 8 and l.strip().endswith(':'):
            E(en, f'head{i}', i, l.strip(), 'section', note(['hollow-verbs', 'naqis-verbs']), 'noted')
    # 5. the mithāl sheet (two files; the second adds Marāḥ / ʿIzzī page citations)
    en = ledger('misal-kaideleri', 'Mithāl rules (Ottoman), with the Marāḥ / ʿIzzī citations', ['misal-kaideleri-mesnedli.txt', 'ilal-misal-ecvef-naqis.txt'], 'sarf',
                'Both files carry the same numbered rules (the first adds «(مراح الارواح، صحيفه N)، (عزى، صحيفه N)»); the first ~150 lines of each are OLE noise.')
    L = lines('misal-kaideleri-mesnedli.txt')
    rules_at = [i for i, l in enumerate(L, 1) if re.match(r'\s*[0-9٠-٩۰-۹]+\s*-\s*\S', l) and re.search('[ء-ي]{3,}', l)]
    for k, i in enumerate(rules_at):
        end = rules_at[k + 1] if k + 1 < len(rules_at) else min(len(L), i + 8)
        blk = '\n'.join(L[i - 1:end - 1])
        pairs = re.findall(r'"([ء-ْ]+)"\s*(?:نك|نڭ)?\s*آصلى[؛:]?\s*"([ء-ًٌٍْ]+)"', blk)
        pairs += [(b, a) for a, b in re.findall(r'آصلى\s*"([ء-ًٌٍْ]+)"\s*در[^"]{0,80}"([ء-ًٌٍْ]+)"', blk)][:0]
        cite = re.findall(r'\((?:مراح الارواح|عزى)[^)]*\)', blk)
        cb = [{'type': 'engine', 'ref': 'IlalEngine.derive'}] if pairs else []
        probe = {'all': [{'ilal': y, 'out': x} for x, y in pairs]} if len(pairs) > 1 else ({'ilal': pairs[0][1], 'out': pairs[0][0]} if pairs else None)
        e = E(en, f'r{k + 1}', i, L[i - 1].strip()[:200], 'rule', cb + note(['mithal-verbs']), 'applied' if probe else ('noted' if 'mithal-verbs' in NOTES else 'open'), probe)
        if cite:
            e['cites'] = cite
    E(en, 'noise', '1-150', 'OLE header bytes', 'row', [], 'not-automatable', reason='undecodable bytes before the text')
    # 6. maṣdar / ṣifa / mubālagha wazns: only the headers survive
    en = ledger('masdar-sifa-mubalagha-vezinleri', 'Samāʿī maṣdar, ṣifa mushabbaha and mubālagha wazns (headers only survive)', ['masdar-sifa-mubalagha-vezinleri.txt'], 'sarf')
    L = lines('masdar-sifa-mubalagha-vezinleri.txt')
    HEADS = {155: ('masdar', None), 156: ('masdar', None), 160: ('sifa', "ISHTIQAQ_LAW.patterns.some(p=>p.roles.includes('sifa'))"),
             720: ('mubalagha', "ISHTIQAQ_LAW.patterns.some(p=>p.roles.includes('mubalagha'))"), 724: ('mubalagha', None)}
    for ln, (k, js) in HEADS.items():
        ids = [i for i in (k, 'masdar', 'sifa-mushabbaha', 'mubalagha') if i in NOTES][:1]
        E(en, f'h{ln}', ln, L[ln - 1].strip(), 'row', note(ids) + ([{'type': 'engine', 'ref': 'ISHTIQAQ_LAW.patterns'}] if js else []),
          'applied' if js else ('noted' if ids else 'open'), {'js': js} if js else None)
    E(en, 'rows', '1-861', 'the wazn rows themselves', 'row', [], 'not-automatable', reason='the data rows are unrecoverable bytes (only the five headers decode)')
    # 7. the ṣifa mushabbaha's 18 wujūh
    en = ledger('sifa-mushabbaha-vezinleri', "Ṣifa mushabbaha — the 18 wujūh of its maʿmūl, with each one's ruling", ['sifa-mushabbaha-vezinleri.txt'], 'sarf')
    L = lines('sifa-mushabbaha-vezinleri.txt')
    sid = [k for k in NOTES if 'sifa-mushabbaha' in k]
    for i in range(3, 12):
        cells = [c.strip() for c in L[i - 1].split('|')]
        for j in range(0, len(cells) - 2, 1):
            if re.search('[ء-ي]', cells[j]) and re.match(r'^\d+\.0$', cells[j + 1] if j + 1 < len(cells) else ''):
                ex, ruling = cells[j], cells[j - 1] if j else ''
                q = [k for k in sid if HN(ex) in NOTE_TEXT[k]]
                E(en, 'w' + cells[j + 1].split('.')[0], i, f'{ex} — {ruling}', 'row', note(q, 'quotes'), 'noted' if q else 'open',
                  reason=None if q else 'the note does not show this wajh')
    for i in range(12, 16):
        q = [k for k in sid if HN(L[i - 1].split('"')[1] if '"' in L[i - 1] else '') in NOTE_TEXT[k]] if sid else []
        E(en, f'rule{i}', i, L[i - 1].strip(), 'rule', note(sid), 'noted' if sid else 'open')
    # 8. the number-name worksheets: every pair is a test of AdadEngine.name
    en = ledger('esmai-aded-worksheets', 'Esmâ-i aded — the number-name worksheets (125–3000)', ['esmai-aded-worksheets.txt'], 'sarf')
    L = lines('esmai-aded-worksheets.txt')
    for i, l in enumerate(L, 1):
        m = re.match(r'^(\d+)\t(.+)$', l.strip())
        if m:
            js = ("(()=>{const H=s=>stripAr(String(s||'')).replace(/[أإآ]/g,'ا').replace(/ى/g,'ي').replace(/[^ء-ي ]/g,'').replace(/\\s+/g,' ').trim();"
                  "return H(AdadEngine.name(%s))===H(%s)})()" % (m.group(1), json.dumps(m.group(2).strip(), ensure_ascii=False)))
            E(en, 'n' + m.group(1), i, l.strip(), 'row', [{'type': 'engine', 'ref': 'AdadEngine.name'}], 'applied', {'js': js})


# ================================================================ group 3: balāgha
BTOPICS = [
    ('fasaha', r'فصاحت|فصاحة|بلاغت|بلاغة|fesahat|belagat', ['al-fasaha-wal-balagha', 'fasaha', 'balagha']),
    ('maani', r'علم معاني|علم المعاني|meani', ['ilm-al-maani']),
    ('khabar', r'خبر|انشا|انشاء|طلب', ['al-khabar-wal-insha', 'khabar-insha', 'aghrad-al-khabar', 'adawat-al-tasawwur', 'al-istifham', 'al-amr-wa-wujuhuh', 'al-nahy-wa-wujuhuh', 'anwa-al-khabar', 'insha-wa-tamanni', 'khabar-fi-mana-al-insha']),
    ('isnad', r'اسناد|مسند اليه|مسند', ['ahwal-al-musnad-ilayh', 'tarif-al-musnad-ilayh', 'taqdim-al-musnad-ilayh', 'wujuh-al-musnad', 'tark-al-musnad', 'majaz-aqli']),
    ('qasr', r'قصر|حصر', ['qasr', 'aqsam-al-qasr', 'turuq-al-qasr']),
    ('wasl', r'فصل|وصل', ['al-fasl-wa-al-wasl', 'muhassin-al-wasl']),
    ('ijaz', r'ايجاز|اطناب|مساوات|مساواة', ['ijaz-itnab-musawat', 'ijaz-al-hadhf', 'asbab-al-itnab', 'ijaz-itnab-nisbi']),
    ('bayan', r'علم بيان|علم البيان|بيان', ['ilm-al-bayan']),
    ('tashbih', r'تشبيه|مشبه', ['tashbih', 'aghrad-al-tashbih', 'arkan-al-tashbih', 'aqsam-al-tashbih']),
    ('haqiqa', r'حقيقت|حقيقة', ['haqiqa-majaz']),
    ('majaz', r'مجاز|علاقه|علاقة|لزوم|ما وضع له|موضوع له', ['haqiqa-majaz', 'majaz-mursal', 'anwa-al-majaz', 'qarinat-al-majaz', 'majaz-aqli', 'majaz-murakkab']),
    ('istiara', r'استعاره|استعارة|مصرحه|مكنيه|مكنيّه|تخييليه|تحقيقيه|تمثيليه|مستعار', ['istiara', 'aqsam-al-istiara', 'istiara-makniyya', 'istiara-tabaiyya', 'arkan-al-istiara']),
    ('kinaya', r'كنايه|كناية|مكني', ['kinaya', 'aqsam-al-kinaya', 'kinaya-qariba-baida', 'farq-al-kinaya-wal-majaz', 'fadl-al-majaz-wal-kinaya']),
    ('badi', r'بديع|جناس|طباق|مقابله|مقابلة|سجع|تورية|توريه|مشاكله|مبالغه|لف ونشر|التفات', ['ilm-al-badi', 'jinas-naqis', 'jinas-mudari-lahiq', 'mubalagha-maqbula']),
    ('sariqa', r'سرقات|سرقة|اقتباس|تضمين|عقد|حل', ['al-iqtibas-wal-tadmin']),
]


def btopics(text):
    h = H(text)
    cb, tops = [], []
    for tid, rx, ids in BTOPICS:
        if re.search(rx, h):
            tops.append(tid)
            cb += [c for c in note([i for i in ids if i in NOTES]) if c not in cb]
    return tops, cb


ALAQA = [  # the ʿalāqas the notes name: (Ottoman name, key in MajazEngine.ALAQA_NAMES or None)
    ('مصدريه', None), ('مظهريه', None), ('مجاوره', 'mujawara'), ('جزئيه', 'juziyya'), ('كليه', 'kulliyya'), ('سببيه', 'sababiyya'),
    ('مسببيه', 'musabbabiyya'), ('كون سابق', None), ('كون لاحق', None), ('محليه', 'mahalliyya'), ('حاليه', 'halliyya'), ('آليه', 'aliyya'),
    ('لازميه', 'lazimiyya'), ('ملزوميه', 'malzumiyya'), ('عموم', 'umum'), ('خصوص', 'khusus'), ('اطلاق', None), ('تقييد', None),
]


def g_balagha():
    # ʿIlm al-bayān notes: two files of one .doc (the second is the raw Word dump: 582 of its 583 text lines are in the first)
    en = ledger('alaka-ilm-bayan', "ʿIlm al-bayān — ḥaqīqa, majāz, kināya and the ʿalāqas (Ottoman notes)", ['alaka-ilm-bayan.txt', 'alaqat-al-majaz-balagha.txt'], 'balagha',
                'RE-MEASURED: `alaqat-al-majaz-balagha.txt` is not unrecoverable (research/COVERAGE.md #3 is stale) — it is the raw Word dump of '
                '`alaka-ilm-bayan.txt`: 582 of the latter\'s 583 text lines stand in it letter for letter, and it holds no Arabic the other lacks. Ledgered once.')
    L = lines('alaka-ilm-bayan.txt')
    paras, cur, st = [], [], None
    for i, l in enumerate(L, 1):
        if i < 10:
            continue
        if l.strip().startswith('(') and cur:
            paras.append((st, '\n'.join(cur))); cur = []
        if l.strip():
            if not cur:
                st = i
            cur.append(l)
    if cur:
        paras.append((st, '\n'.join(cur)))
    prev_cb = []
    for k, (ln, txt) in enumerate(paras, 1):
        tops, cb = btopics(txt)
        if not tops and re.match(r'\(\s*(تركجه مثال|مثلا|نوط|معناسي|ذاته مثال|صفته مثال|حسا)', H(txt.strip())):
            cb = [dict(c, how='continues the paragraph before') for c in prev_cb]
        if not tops and not cb and re.search(r'حمد|صلات|آل:|اوّلين|طيّبين|طاهرين', txt):
            E(en, f'p{k:03d}', ln, re.sub(r'\s+', ' ', txt.strip())[:160], 'section', [], 'not-automatable',
              reason='commentary on the khuṭba (praise, blessing, the Prophet\'s family): no rule to carry'); continue
        if cb:
            prev_cb = cb
        hit = [(a, key) for a, key in ALAQA if a in H(txt)]
        e_cb = list(cb)
        probe = None
        if hit and all(key for _, key in hit):
            probe = {'js': 'Object.values(MajazEngine.ALAQA_NAMES).includes(%s)' % json.dumps(hit[0][1])}
            e_cb.append({'type': 'engine', 'ref': 'MajazEngine.ALAQA_NAMES', 'alaqa': [a for a, _ in hit]})
        status = 'applied' if probe else 'noted' if cb else 'open'
        reason = None
        if hit and not all(key for _, key in hit):
            status = 'noted' if cb else 'open'
            reason = 'MajazEngine names no ʿalāqa «%s»' % '، '.join(a for a, key in hit if not key)
        E(en, f'p{k:03d}', ln, re.sub(r'\s+', ' ', txt.strip())[:160], 'section', e_cb, status, probe, reason=reason,
          gap=reason)
    # Talkhīṣ al-Miftāḥ (the Ottoman lesson notebook that quotes the matn): one entry per page
    en = ledger('talkhis-al-miftah-balagha', 'Talkhīṣ al-Miftāḥ — the Ottoman lesson notebook (Ziya Sungur-oğlu), per page', ['talkhis-al-miftah-balagha.txt'], 'balagha')
    L = lines('talkhis-al-miftah-balagha.txt')
    marks, prev = [], -5
    for i, l in enumerate(L, 1):
        if re.match(r"\s*صحيفه.{0,6}$", l):   # a page break (the notebook prints it twice; the number is often lost)
            if i - prev > 1:
                marks.append((len(marks) + 1, i))
            prev = i
    story = STORY_TEXT.get('talkhis-al-miftah', '')
    swords = set(story.split())
    for k, (n, ln) in enumerate(marks):
        end = marks[k + 1][1] if k + 1 < len(marks) else len(L) + 1
        txt = '\n'.join(L[ln:end - 1])
        runs = [HN(r) for r in re.findall(r'(?:[ء-ي]+[ً-ْ]+[ء-يً-ْ]*\s*){4,}', txt)]
        on = [r for r in runs if len(r) > 15 and (r in story or (len(r.split()) >= 4 and sum(w in swords for w in r.split()) >= 0.9 * len(r.split())))]
        tops, cb = btopics(txt)
        if on:
            E(en, f'page{n}', ln, (on[0])[:120], 'page', [{'type': 'shelf', 'ref': 'talkhis-al-miftah', 'matn_runs': f'{len(on)}/{len(runs)}'}] + cb, 'shelved')
        elif cb:
            E(en, f'page{n}', ln, re.sub(r'\s+', ' ', txt.strip())[:120], 'page', cb + [{'type': 'topics', 'ref': ','.join(tops)}], 'noted')
        elif len(re.sub(r'\s', '', txt)) < 60:
            E(en, f'page{n}', ln, txt.strip()[:80], 'page', [], 'not-automatable', reason='a near-empty page')
        else:
            E(en, f'page{n}', ln, re.sub(r'\s+', ' ', txt.strip())[:120], 'page', [], 'open', reason='no matn run on the shelf and no balāgha topic named')


# ================================================================ group 4: the received texts and the term sheets
TEXTS = [  # ledger key, title, source files (the text first, witnesses after), packages
    ('aqaid-nasafi', "al-ʿAqāʾid al-Nasafiyya — the matn", ['aqaid-nasafi-matn-full.txt'], ['aqaid-ahl-al-sunna']),
    ('emali-qasida', "Badʾ al-Amālī — the qaṣīda (Ottoman commentary quoting it)", ['emali-qasida-ottoman.txt'], ['bad-al-amali']),
    ('usul-al-munifa', "al-Uṣūl al-Munīfa (al-Bayāḍī's riwāya)", ['usul-al-munifa-src.txt'], ['al-usul-al-munifa']),
    ('wasiyya-samti', "Waṣiyyat Abī Ḥanīfa to al-Samtī", ['wasiyya-samti-arabic.txt'], ['wasiyyat-abi-hanifa-samti']),
    ('maqamat-birgivi', "al-Maqāmāt of Birgivī", ['maqamat-birgivi-src.txt'], ['al-maqamat-birgivi']),
    ('siyar-abi-hanifa', "Siyar — Abū Ḥanīfa", ['siyar-abi-hanifa-src.txt'], ['siyar-abi-hanifa']),
    ('siyar-al-shaykh-al-mufid', "Siyar — al-Shaykh al-Mufīd", ['siyar-al-shaykh-al-mufid-src.txt'], ['siyar-al-shaykh-al-mufid']),
    ('siyar-ibn-al-mubarak', "Siyar — Ibn al-Mubārak", ['siyar-ibn-al-mubarak-src.txt', 'siyar-ibn-al-mubarak-witness.txt'], ['siyar-ibn-al-mubarak']),
    ('muhammad-ibn-zayd-wa-al-umawi', "al-Tanūkhī — Muḥammad ibn Zayd and the Umayyad", ['muhammad-ibn-zayd-wa-al-umawi-src.txt', 'muhammad-ibn-zayd-wa-al-umawi-witness.txt'], ['muhammad-ibn-zayd-wa-al-umawi']),
    ('muallaqat-imri-al-qays', "Muʿallaqa of Imruʾ al-Qays", ['muallaqat-imri-al-qays-src.txt'], ['muallaqat-imri-al-qays']),
    ('muallaqat-zuhayr', "Muʿallaqa of Zuhayr", ['muallaqat-zuhayr-src.txt'], ['muallaqat-zuhayr']),
    ('muallaqat-antara', "Muʿallaqa of ʿAntara", ['muallaqat-antara-src.txt'], ['muallaqat-antara']),
    ('muallaqat-labid', "Muʿallaqa of Labīd", ['muallaqat-labid-src.txt', 'muallaqat-labid-zawzani.txt', 'muallaqat-labid-durra.txt'], ['muallaqat-labid']),
    ('muallaqat-tarafa', "Muʿallaqa of Ṭarafa", ['muallaqat-tarafa-src.txt', 'muallaqat-tarafa-tibrizi.txt', 'muallaqat-tarafa-durra.txt'], ['muallaqat-tarafa']),
    ('muallaqat-amr-ibn-kulthum', "Muʿallaqa of ʿAmr ibn Kulthūm", ['muallaqat-amr-ibn-kulthum-src.txt', 'muallaqat-amr-ibn-kulthum-zawzani.txt', 'muallaqat-amr-ibn-kulthum-durra.txt'], ['muallaqat-amr-ibn-kulthum']),
    ('muallaqat-al-harith', "Muʿallaqa of al-Ḥārith ibn Ḥilliza", ['muallaqat-al-harith-src.txt', 'muallaqat-al-harith-durra.txt'], ['muallaqat-al-harith']),
]


def g_texts():
    for key, title, files, pkgs in TEXTS:
        en = ledger(key, title, files, 'texts', 'Received text: one entry per sentence / verse of the package, found in the source files by its words; '
                    'and one entry for the source lines that are not on the shelf (the witnesses: khabar, sharḥ, iʿrāb, notes).')
        src_lines = []
        for f in files:
            for i, l in enumerate(lines(f), 1):
                if not l.startswith('#'):
                    src_lines.append((f, i, HN(l)))
        allw = set(w for _, _, h in src_lines for w in h.split())
        used, elsewhere = set(), []
        for p in pkgs:
            st = STORIES.get(p)
            if not st:
                E(en, 'missing:' + p, '-', p, 'text', [], 'open', reason='package not on the shelf'); continue
            for c in st['chapters']:
                for s in c['sentences']:
                    ws = HN(sent_text(s)).split()
                    if not ws:
                        continue
                    hit = sum(w in allw for w in ws) / len(ws)
                    ln = None
                    if hit >= 0.85:
                        probe = ' '.join(ws[:3])
                        for f, i, h in src_lines:
                            if probe in h:
                                ln = f'{f}:{i}'; used.add((f, i)); break
                    if hit >= 0.85:
                        E(en, f'{p}:{c["chapter"]}:{s["id"]}', ln or '-', sent_text(s)[:90], 'sentence',
                          [{'type': 'shelf', 'ref': f'{p}:{c["chapter"]}:{s["id"]}', 'words_in_source': round(hit, 2)}], 'shelved')
                    else:
                        elsewhere.append(f'{p}:{c["chapter"]}:{s["id"]}')
        rest = [(f, i) for f, i, h in src_lines if len(h.split()) >= 4 and (f, i) not in used]
        pkgw = set(w for p in pkgs if p in STORIES for w in STORY_TEXT[p].split())
        cov = [(f, i) for f, i, h in src_lines if len(h.split()) >= 4 and sum(w in pkgw for w in h.split()) >= 0.9 * len(h.split())]
        if elsewhere:
            LEDGERS[key]['note'] += (f' {len(elsewhere)} package sentence(s) are not from these files (a restored or completing matn, a ḥadīth, '
                                     f'an editorial bridge — named in the manifest): {", ".join(elsewhere[:12])}{" …" if len(elsewhere) > 12 else ""}.')
        for f in files:
            n_all = sum(1 for g, i, h in src_lines if g == f and len(h.split()) >= 4)
            n_cov = sum(1 for g, i in cov if g == f)
            E(en, 'source:' + f, '1-%d' % len(lines(f)), f'{n_cov} of {n_all} Arabic lines (≥4 words) of {f} stand on the shelf by their words', 'text',
              [{'type': 'shelf', 'ref': ','.join(pkgs), 'lines_on_shelf': n_cov, 'arabic_lines': n_all}],
              'shelved' if n_all and n_cov / n_all >= 0.5 else 'not-automatable',
              reason=None if n_all and n_cov / n_all >= 0.5 else 'a witness (commentary, khabar, iʿrāb or Ottoman notes) read for the authoring, not a text to shelve')
    # al-Inṣāf: each masʾala is a row of content/rules/insaf_masail.json (v339-I), read by the lab «الخلاف» and gKhilaf
    en = ledger('insaf-ibn-al-anbari', "al-Inṣāf fī masāʾil al-khilāf (Ibn al-Anbārī)", ['insaf-ibn-al-anbari-src.txt'], 'texts')
    d = json.loads((OUT / 'insaf_masail.json').read_text(encoding='utf-8'))
    for m in d['masail']:
        E(en, f'masala{m["n"]}', m.get('page', '-'), m['title_ar'][:100], 'section', [{'type': 'lab', 'ref': 'INSAF (lab الخلاف, gKhilaf)'}], 'shelved')
    # the term sheets: every term (a heading or «Term:» definition) found in the package's glossary, translations or a note
    for key, title, f, pkg in [('buyu-tarifler', "Beyʿ bahsi tarifler — the sale's terms (Turkish)", 'buyu-tarifler-turkish.txt', 'kitab-al-buyu'),
                               ('keffaretler', 'Keffaretler (Turkish)', 'keffaretler-turkish.txt', 'kitab-al-kaffarat'),
                               ('sulh-fiqh', 'Sulh — the settlement contract (Turkish)', 'sulh-fiqh-turkce.txt', 'kitab-al-sulh'),
                               ('vakif-mali', 'Vakıf malı — Q&A on waqf property (Turkish)', 'vakif-mali-turkce.txt', 'kitab-al-waqf')]:
        en = ledger(key, title, [f], 'texts', 'Term sheet: one entry per term; carried when the term is in the package (glossary, translations, notes).')
        st = STORIES.get(pkg, {})
        hay = fold(json.dumps(st.get('glossary', {}), ensure_ascii=False) + json.dumps([s.get('translation') for c in st.get('chapters', []) for s in c['sentences']], ensure_ascii=False)
                   + json.dumps(st.get('manifest', {}), ensure_ascii=False))
        L = lines(f)
        terms, seen = [], set()
        hdr = max([i for i, l in enumerate(L, 1) if re.match(r'^[=\-]{10,}$', l.strip())] + [0])   # the transcriber's preamble ends at its rule
        for i, l in enumerate(L, 1):
            if re.search('[؀-ۿ]', l) and not re.search('[A-Za-z]', l):
                continue
            if i <= hdr:
                continue
            for m in re.finditer(r"^\s*\d+[.)]\s*([^:]{3,60}):|^([A-ZÇĞİÖŞÜ][^:.]{2,40}):\s*$", l):
                t = (m.group(1) or m.group(2)).strip(" *-")
                if fold(t) not in seen:
                    seen.add(fold(t)); terms.append((i, t))
            for m in re.finditer(r"(?:^|\*)([A-ZÇĞİÖŞÜ][A-Za-zÇĞİÖŞÜçğıöşüâîû’' \-]{2,40}?)\s*[:;]\s", l):
                t = m.group(1).strip(" *-")
                if 2 <= len(t.split()) <= 5 or (len(t) >= 4 and len(t.split()) == 1):
                    if fold(t) not in seen and not re.match(r'(Source|Not|Ornek|Örnek|Soru|Cevap|Mesela|Yani|Bazı|Bu )', t) and len(t.split()) <= 4:
                        seen.add(fold(t)); terms.append((i, t))
            for m in re.finditer(r"([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ’' \-]{5,60})(?=[A-ZÇĞİÖŞÜ][a-zçğıöşü]|\s*\(|$)", l):
                t = m.group(1).strip()
                if len(t.split()) <= 6 and fold(t) not in seen and len(t.split()) + (1 if re.search(r'(KEFF|BEY|SULH|VAKF|TAR)', t) else 0) >= 2:
                    seen.add(fold(t)); terms.append((i, t))
        for k, (i, t) in enumerate(terms, 1):
            core = [w for w in fold(t).split() if len(w) > 3 and w not in ('nedir', 'kisim', 'kisimdir', 'hakkinda', 'olarak', 'nelerdir', 'sartlari')]
            ok = core and any(w[:6] in hay for w in core)
            E(en, f't{k:02d}', i, t, 'term', [{'type': 'shelf', 'ref': pkg, 'how': 'the term in its glossary / translations / manifest'}] if ok else [],
              'noted' if ok else 'open', reason=None if ok else f'the term is not in {pkg}\'s glossary, translations or manifest')
    # Nadwī's leveling notes: a reference (in copyright), not a text
    en = ledger('qisas-al-nabiyyin-nadwi-leveling-notes', "Nadwī's Qaṣaṣ al-Nabiyyīn — the leveling notes", ['qisas-al-nabiyyin-nadwi-leveling-notes.txt'], 'texts')
    L = lines('qisas-al-nabiyyin-nadwi-leveling-notes.txt')
    for i, l in enumerate(L, 1):
        if re.match(r'#\s+-\s', l) or (not l.startswith('#') and len(HN(l).split()) >= 4):
            E(en, f'l{i}', i, l.strip('# ')[:140], 'note', [{'type': 'shelf', 'ref': 'qisas-al-nabiyyin-1,2,4 (the method; the ramp)'}], 'not-automatable',
              reason='a leveling reference: the author\'s method and a short specimen; the volumes are authored as packages, not from this file')


GROUPS = [g_awamil, g_birgivi_examples, g_edatlar, g_banks, g_prose, g_sarf, g_balagha, g_texts]


# ================================================================ proof, status, output
def collect_probes():
    out = []
    for k, L in LEDGERS.items():
        for e in L['entries']:
            if e.get('probe'):
                out.append({'key': f'{k}#{e["id"]}', 'probe': e['probe']})
    return out


def prove(html=None):
    pr = collect_probes()
    tmp = ROOT / 'content' / 'rules' / '.aux_probes.tmp.json'
    tmp.write_text(json.dumps(pr, ensure_ascii=False), encoding='utf-8')
    cmd = ['node', str(ROOT / 'tools' / 'ledger' / 'aux_prove.js'), str(tmp)] + ([html] if html else [])
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    tmp.unlink()
    if r.returncode:
        sys.exit('prove failed: ' + r.stderr[-2000:])
    res = json.loads(r.stdout)
    PROOF.write_text(json.dumps(res, ensure_ascii=False, indent=0), encoding='utf-8')
    return res


SLIPS = {  # (ledger, entry id) -> what the sheet prints wrong; checked by eye against the engine's form and the sheet's own other rows
    ('bablara-nakil', 'اِفْتَعَلَ:وجل'): 'اِتّجّلَ — two stray shaddas; the sheet means اِتَّجَلَ (the waw assimilated to the tāʾ)',
    ('bablara-nakil', 'اِفْعَلَّ:نعم'): 'اِنَعَمَّ — the sukūn of the fāʾ is missing (اِنْعَمَّ, as every other cell of the row)',
    ('bablara-nakil', 'تَفَعَّلَ:فتح'): 'تَفّتَّحَ — a stray shadda on the fāʾ (تَفَتَّحَ)',
    ('bablara-nakil', 'اِسْتَفْعَلَ:ذهب'): 'اِسَتْذْهَبَ — the fatḥa and sukūn of سْتَ swapped (اِسْتَذْهَبَ)',
    ('sifa-mushabbaha-vezinleri', 'w10'): 'وحْهُهُ — ḥāʾ for jīm (the row is الحسنُ وجْهُهُ, as rows 1–9 and the sheet\'s second page show)',
    ('ilal-kaideleri-turkce', 'd45-13'): 'غَِبوَ — the kasra sits on the ghayn with a fatḥa (the origin is غَبِوَ, the rule\'s own words)',
}


SLIPH = {(k, H(i)): v for (k, i), v in SLIPS.items()}


def settle(res):
    for k, L in LEDGERS.items():
        for e in L['entries']:
            claim = e.pop('claim')
            p = e.get('probe')
            r = res.get(f'{k}#{e["id"]}') if p else None
            if p:
                e['proof'] = {'ok': bool(r and r['ok']), 'got': (r or {}).get('got', 'not run')[:200]}
            slip = SLIPS.get((k, e['id'])) or SLIPH.get((k, H(e['id'])))
            if slip and not (r and r['ok']):   # a slip is only ever a cell the engine does NOT reproduce
                e['status'] = 'slip'
                e['reason'] = 'the sheet\'s own typo: ' + slip
            elif claim == 'applied' and not (r and r['ok']):
                e['carried_by'] = [c for c in e['carried_by'] if c['type'] != 'engine']
                has = {c['type'] for c in e['carried_by']}
                e['status'] = 'noted' if 'note' in has else 'banked' if 'bank' in has else 'open'
                e['gap'] = e.get('gap') or 'engine probe fails'
            elif claim == 'noted' and p and not (r and r['ok']):
                e['status'] = 'open'
            else:
                e['status'] = claim


def counts(L):
    c = {}
    for e in L['entries']:
        c[e['status']] = c.get(e['status'], 0) + 1
    return c


def write():
    OUT.mkdir(parents=True, exist_ok=True)
    md = ['# Book coverage — the other resources (v342-A, 2026-11-27)', '',
          'Generated by `tools/ledger/aux_ledger.py --prove` from the source files themselves; one ledger per source (a source stated',
          'twice is one ledger naming both files). «applied» = a probe on the built page passed (the smoke check «v342 — the other',
          "resources' ledger» re-runs every probe); «noted» / «banked» = a grammar note / a question bank item carries it (checked by id,",
          'and a quote by its letters); «shelved» = a received text (or a lab table) on the shelf; «slip» = the sheet\'s own typo, the',
          'engine right; «open» = nothing carries it yet, with the reason. An entry whose engine probe fails keeps its note / bank',
          'carrier but records `gap`; every such gap that needs an engine rule is ranked in `research/engine-gaps-2026-11-27.md`.', '',
          '| ledger | group | files | entries | applied | noted | banked | shelved | slip | not-automatable | open |',
          '|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    tot = {}
    for k, L in LEDGERS.items():
        c = counts(L)
        for s, v in c.items():
            tot[s] = tot.get(s, 0) + v
        md.append(f"| {k} | {L['group']} | {', '.join('`' + f + '`' for f in L['files'])} | {len(L['entries'])} | " +
                  ' | '.join(str(c.get(s, 0)) for s in ('applied', 'noted', 'banked', 'shelved', 'slip', 'not-automatable', 'open')) + ' |')
        doc = {'book': k, 'ledger': 'aux', 'title': L['title'], 'source': 'research/sources/' + L['source'], 'files': ['research/sources/' + f for f in L['files']],
               'group': L['group'], 'note': L['note'], 'counts': c, 'entries': L['entries']}
        (OUT / f'coverage_{k}.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    md.append(f"| **all** | | | {sum(tot.values())} | " + ' | '.join(str(tot.get(s, 0)) for s in ('applied', 'noted', 'banked', 'shelved', 'slip', 'not-automatable', 'open')) + ' |')
    md.append('')
    for k, L in LEDGERS.items():
        md.append(f"## {k} — {L['title']}")
        md.append('')
        if L['note']:
            md.append(L['note']); md.append('')
        opens = [e for e in L['entries'] if e['status'] in ('open', 'not-automatable', 'slip')]
        if opens:
            md.append('| id | line | entry | status | why / where it goes |')
            md.append('|---|---|---|---|---|')
            for e in opens[:400]:
                why = e.get('reason') or e.get('gap') or ''
                if e.get('proof') and not e['proof']['ok']:
                    why = (why + ' — engine says: ' + e['proof']['got'][:90]).strip(' —')
                md.append(f"| {e['id']} | {e['line']} | {str(e['ar'])[:70].replace('|', '/')} | {e['status']} | {why.replace('|', '/')} |")
            md.append('')
        else:
            md.append('Nothing open.'); md.append('')
    (ROOT / 'research' / 'book-coverage-2026-11-27.aux.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    return tot


def main():
    for g in GROUPS:
        g()
    res = prove(sys.argv[2] if len(sys.argv) > 2 else None) if '--prove' in sys.argv else (json.loads(PROOF.read_text()) if PROOF.exists() else {})
    settle(res)
    tot = write()
    print(json.dumps(tot), {k: counts(L) for k, L in LEDGERS.items()})


if __name__ == '__main__':
    main()
