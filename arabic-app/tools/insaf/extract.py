# extract the masa'il table from the source file (run with python3 -I). Output: raw records JSON for review.
import sys, re, json
SRC, OUT = sys.argv[1], sys.argv[2]
lines = open(SRC, encoding='utf-8').read().split('\n')
rows = []
pg = None; inham = False
for l in lines:
    m = re.match(r'^=== p\. (\d+) \((\d:\d+)\) ===$', l)
    if m: pg = (int(m.group(1)), m.group(2)); inham = False; continue
    if l == '--- hashiya ---': inham = True; continue
    # Shamela pp. 335-337 are vol. 1's table of contents (each masala's heading again): not a body
    if pg and not inham and l.strip() and not (335 <= pg[0] <= 337): rows.append((pg[0], pg[1], l))
AR = '٠١٢٣٤٥٦٧٨٩'
def num(s): return int(''.join(str(AR.index(c)) for c in s))
H = '[\u064b-\u0652\u0670]*'
def tol(w): return ''.join(c + H for c in w)
KUF, BAS = tol('الكوفيون'), tol('البصريون')
SCHOOL = '(' + KUF + '|' + BAS + ')'
def school_of(s):
    b = re.sub('[\u064b-\u0652\u0670]', '', s)
    return 'kufa' if 'الكوفيون' in b else 'basra' if 'البصريون' in b else None
heads = [i for i, r in enumerate(rows) if re.match(r'^([٠-٩]+)\s*-?\s*مسألة', r[2])]
recs = []
for hi, i in enumerate(heads):
    j = heads[hi + 1] if hi + 1 < len(heads) else len(rows)
    body = rows[i:j]
    cut = [q for q, r in enumerate(body) if r[2].startswith('[زيادة')]
    if cut: body = body[:cut[0]]
    h = body[0][2]
    n = num(re.match(r'^([٠-٩]+)', h).group(1))
    t = re.sub(r'^[٠-٩]+\s*-?\s*مسألة:?\s*', '', h); t = re.sub(r'\s*[٠-٩]+$', '', t).strip()
    if t[:1] in '["' and t[-1:] in ']"': t = t[1:-1]
    rec = {'n': n, 'extra': body[0][0] >= 665, 'title_ar': t, 'page': {'shamela': body[0][0], 'printed': body[0][1]}, 'head': h}
    k = 1
    while k < len(body) and not re.match(r'^(أما|وأما|فأما) (' + KUF + '|' + BAS + ')', body[k][2]): k += 1
    region = body[1:k]
    rec['region'] = [r[2] for r in region]
    rec['region_pages'] = sorted(set(r[0] for r in region))
    stmts = []
    for r in region:
        txt = r[2]
        # a statement opens at «ذهب / وذهب / فذهب» — never at «وإليه ذهب» (that is agreement, kept inside its sentence's clause list)
        idx = [m.start() for m in re.finditer(r'(?:(?<=^)|(?<=[\s.،؛]))[وف]?ذهب ', txt) if not re.search(r'إليه\s*$', txt[:m.start()])]
        for a_i, a in enumerate(idx):
            b = idx[a_i + 1] if a_i + 1 < len(idx) else len(txt)
            seg = txt[a:b]
            p = seg.find('.')
            if p >= 0: seg = seg[:p + 1]
            seg = seg.rstrip()
            # agreement clauses «، وإليه ذهب …» are split off the statement
            agree = []
            m = re.search(r'[،,]?\s*وإليه ذهب', seg)
            if m:
                agree.append(seg[m.start():].lstrip('،, ').rstrip())
                seg = seg[:m.start()]
            stmts.append({'text': seg.rstrip(' ،؛,'), 'agree': agree, 'page': r[0]})
    rec['stmts'] = stmts
    rec['others'] = []
    for s in stmts:
        m = re.match(r'^[وف]?ذهب ' + SCHOOL + r'(?=\s)', s['text'])
        sc = school_of(m.group(1)) if m else None
        if sc and sc + '_ar' not in rec:
            rec[sc + '_ar'] = s['text']
            for a in s['agree']: rec['others'].append({'ar': a, 'agrees': sc})
        else:
            rec['others'].append({'ar': s['text'], 'agrees': None})
            for a in s['agree']: rec['others'].append({'ar': a, 'agrees': 'prev'})
    full = [r[2] for r in body]
    tj = []
    for kk, l in enumerate(full[len(region):], start=len(region)):
        for m in re.finditer(r'(والصحيح|والمختار|والذي أذهب إليه|والذي نذهب إليه|والأولى|والوجه|وهو الصحيح|وهذا هو الصحيح|والمذهب)', l):
            st = l.rfind('.', 0, m.start()) + 1
            en = l.find('.', m.end()); en = len(l) if en < 0 else en + 1
            tj.append({'ar': l[st:en].strip(), 'line': kk, 'school': school_of(l[st:en])})
    ans = None
    for kk, l in enumerate(full):
        m = re.match(r'^(وأما|أما|فأما|ما) (الجواب|الجوابُ) عن (كلمات|كلما ت|كلمة) (' + tol('الكوفيين') + '|' + tol('البصريين') + ')', l)
        if m and not ans:
            b = re.sub('[\u064b-\u0652\u0670]', '', m.group(4))
            ans = {'kind': 'answer', 'school': 'basra' if b == 'الكوفيين' else 'kufa', 'ar': m.group(0), 'line': kk}
    rec['tj_cands'] = tj; rec['tj_answer'] = ans
    rec['n_lines'] = len(full); rec['pages_all'] = [body[0][0], body[-1][0]]
    recs.append(rec)
json.dump(recs, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('masail', len(recs))
