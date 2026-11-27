"""v360-Sh — shared reading of the web text of Sharḥ Shudhūr al-Dhahab (research/sources/sharh-shudhur-al-dhahab-src.txt).

LETTERS are the witness (the e-text's vowels are mechanical): `key()` strips the harakat, tatweel, punctuation and folds the hamza
seats of alif (أ إ آ ٱ → ا) and alif maqṣūra (ى → ي) — the e-text drops the hamza of «اذا / الى» where our print writes it.
The e-text sets the kāf of likeness apart («ك زيد»): `find` also tries the query with a word-initial ك split off. Everything else (ة, ؤ, ئ, ء) is compared as written."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(ROOT, 'research', 'sources', 'sharh-shudhur-al-dhahab-src.txt')
HAR = re.compile('[ً-ٰٟـۖ-ۭ]')

def key(s):
    s = HAR.sub('', s or '')
    s = re.sub('[أإآٱ]', 'ا', s).replace('ى', 'ي')
    s = re.sub('[^ء-ي]+', ' ', s)
    return ' '.join(s.split())

def pages():
    """[(shamela, printed, section, text_lines)]"""
    t = open(WEB, encoding='utf-8').read()
    parts = re.split(r'^=== p\. (\d+) \((\d+)\) \[([^\]]*)\] ===$', t, flags=re.M)
    out = []
    for i in range(1, len(parts), 4):
        out.append((int(parts[i]), int(parts[i + 1]), parts[i + 2], [l for l in parts[i + 3].split('\n') if l.strip()]))
    return out

_P = None
def P():
    global _P
    if _P is None: _P = pages()
    return _P

def flat():
    """the whole text as one key string, with a map from char offset → (shamela, printed); lines joined by a space (a sentence may
    run over a page break — the page given is where it starts)."""
    buf, marks = [], []
    pos = 0
    for sh, pr, sec, lines in P():
        k = key(' '.join(lines))
        marks.append((pos, sh, pr)); buf.append(k); pos += len(k) + 1
    return ' '.join(buf), marks

_F = None
def find(s, start_printed=None):
    """all (shamela, printed) where key(s) stands (word-bounded) in the text."""
    global _F
    if _F is None: _F = flat()
    T, marks = _F
    k = key(s)
    if not k: return []
    out = []
    w = k.split(); ks = [i for i, x in enumerate(w) if x.startswith('ك') and len(x) > 2][:6]
    pat = ' '.join(('ك ?' + re.escape(x[1:])) if i in ks else re.escape(x) for i, x in enumerate(w))
    for m in re.finditer(r'(?<![ء-ي])' + pat + r'(?![ء-ي])', T):
        p = m.start(); sh = pr = None
        for a, b, c in marks:
            if a <= p: sh, pr = b, c
            else: break
        out.append((sh, pr))
    return out

def is_verbatim(s): return bool(find(s))

def is_verbatim_quote(s):
    """a stored quote: every « … »-joined segment stands in the web text."""
    segs = [x for x in (s or '').split(' … ') if x.strip()]
    return bool(segs) and all(is_verbatim(x) for x in segs)
