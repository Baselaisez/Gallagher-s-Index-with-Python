# build content/rules/insaf_masail.json from raw.json (extract.py) + the source file (run from arabic-app, python3 -I)
import sys, re, json, importlib.util
from pathlib import Path
RAW, SRC, OUT, REND = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('rend', REND); rend = importlib.util.module_from_spec(spec); spec.loader.exec_module(rend)
raw = json.load(open(RAW, encoding='utf-8')); src = open(SRC, encoding='utf-8').read()
H = '[ً-ْٰ]*'
def bare(s): return re.sub('[ً-ْٰ]', '', s)
def school_of(s):
    b = bare(s)
    k = 'الكوفيون' in b or 'الكوفيين' in b; ba = 'البصريون' in b or 'البصريين' in b
    return 'kufa' if k and not ba else 'basra' if ba and not k else None
BABS = [("usul", "الاشتقاق", "Derivation", "İştikak", [1, 28]),
        ("irab", "الإعراب والبناء", "Iʿrāb and bināʾ", "İ'râb ve binâ", [2, 3, 4, 69, 70, 71]),
        ("marfuat", "المرفوعات", "The marfūʿāt: mubtadaʾ and khabar", "Merfûât: mübtedâ ve haber", [5, 6, 7, 8, 9, 10]),
        ("afal", "الأفعال", "Verbs: governing, niʿma and biʾsa, wonder", "Fiiller: amel, ni'me ve bi'se, taaccüb", [13, 14, 15, 16]),
        ("nawasikh", "النواسخ", "Kāna, inna and their sisters; mā and lā", "Nevâsih: kâne, inne ve kardeşleri; mâ ve lâ", [17, 18, 19, 20, 22, 23, 24, 25, 26, 53, 119]),
        ("mansubat", "المنصوبات", "The manṣūbāt: objects, ẓarf, ḥāl, exception, tamyīz", "Mansûbât: mef'ûller, zarf, hâl, istisnâ, temyîz", [11, 12, 21, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 120]),
        ("adad", "العدد وكم", "Numbers and kam", "Aded ve kem", [40, 41, 42, 43, 44]),
        ("nida", "النداء", "The vocative, tarkhīm and nudba", "Nidâ, terhîm ve nüdbe", [45, 46, 47, 48, 49, 50, 51, 52]),
        ("majrurat", "المجرورات", "Jarr: the particles, the oath, iḍāfa", "Cer: harfler, kasem, izâfe", [54, 55, 56, 57, 59, 60, 61, 121]),
        ("tawabi", "التوابع", "Followers: tawkīd and ʿaṭf", "Tâbiler: tekid ve atıf", [62, 63, 64, 65, 66, 67, 68]),
        ("mudari", "إعراب الفعل", "The verb's iʿrāb: rafʿ, naṣb, jazm", "Fiilin i'râbı: ref', nasb, cezm", [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 91]),
        ("huruf", "الحروف", "Particles", "Harfler", [58, 88, 89, 90, 92]),
        ("damair", "الضمائر والمعارف", "Pronouns, demonstratives, relatives", "Zamirler, işaret isimleri, mevsûller", [95, 96, 97, 98, 99, 100, 101, 102, 103, 104]),
        ("sarf", "الصرف", "Ṣarf: hamza, maqṣūr, weights", "Sarf: hemze, maksûr, vezinler", [93, 94, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118])]
BAB_OF = {n: b[0] for b in BABS for n in b[4]}
assert sorted(BAB_OF) == list(range(1, 122)), sorted(set(range(1, 122)) - set(BAB_OF))
LINKS = {2: ["five-nouns"], 3: ["al-muthanna", "jam-mudhakkar-salim"], 4: ["jam-mudhakkar-salim"], 5: ["mubtada-khabar", "al-amil-al-manawi"], 6: ["mubtada-khabar"],
    7: ["khabar-al-mubtada-wa-ahkamuh"], 9: ["khabar-al-mubtada-wa-ahkamuh"], 10: ["mubtada-khabar"], 11: ["maful-bihi"], 13: ["tanazu"], 14: ["afal-al-madh-wal-dhamm-fil-kafiya"],
    15: ["fil-al-taajjub-fil-kafiya"], 16: ["fil-al-taajjub-fil-kafiya"], 17: ["kana-wa-akhawatuha"], 18: ["kana-wa-akhawatuha"], 19: ["ma-la-mushabbaha"], 20: ["ma-la-mushabbaha"],
    22: ["inna-wa-akhawatuha"], 23: ["inna-wa-akhawatuha"], 24: ["masail-inna-wal-mukhaffafa-fil-kafiya"], 25: ["kaanna-lakinna-layta-laalla-fil-kafiya"], 26: ["kaanna-lakinna-layta-laalla-fil-kafiya"],
    27: ["ism-fil", "ighra-wa-ikhtisas"], 28: ["masdar"], 29: ["zarf-mustaqarr-wa-laghw"], 30: ["maful-maah"], 31: ["hal"], 32: ["hal"], 34: ["istithna"], 35: ["istithna"], 36: ["istithna"], 37: ["istithna"],
    38: ["al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"], 39: ["al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"], 40: ["al-kinayat-wal-zuruf-al-mabniyya"], 41: ["al-kinayat-wal-zuruf-al-mabniyya"],
    42: ["asma-al-adad-fil-kafiya"], 43: ["asma-al-adad-fil-kafiya"], 44: ["asma-al-adad-fil-kafiya"], **{n: ["vocative-munada"] for n in range(45, 53)}, 53: ["la-nafiya-lil-jins"], 54: ["huruf-jarr"],
    55: ["al-lam-wa-rubba-fil-kafiya"], 56: ["an-ala-al-kaf-mudh-wa-huruf-al-istithna-fil-kafiya"], 57: ["huruf-al-qasam-fil-kafiya"], 59: ["huruf-al-qasam-fil-kafiya"], 60: ["al-mudaf-wa-nawa-al-idafa"],
    61: ["al-mudaf-wa-nawa-al-idafa"], 62: ["al-tawkid-al-lafzi-wal-manawi"], 63: ["al-tawkid-al-lafzi-wal-manawi"], **{n: ["atf-nasaq"] for n in range(64, 69)}, 69: ["mamnu-min-sarf"], 70: ["mamnu-min-sarf"],
    72: ["imperative-amr"], 73: ["mudari-marfu"], 74: ["mudari-marfu"], **{n: ["nawasib-wa-jawazim-al-mudari"] for n in range(75, 84)}, **{n: ["al-majzum-wal-shart-wal-jaza"] for n in range(84, 88)},
    88: ["in-shartiyya"], 94: ["nun-tawkid"], 95: ["asma-al-ishara", "ism-mawsul"], 96: ["al-marifa-al-mudmarat-wal-alam"], 97: ["al-marifa-al-mudmarat-wal-alam"], 98: ["al-marifa-al-mudmarat-wal-alam"],
    100: ["damir-fasl"], 101: ["al-marifa-wal-nakira-fil-kafiya"], 102: ["ism-mawsul"], 103: ["asma-al-ishara", "ism-mawsul"], 104: ["ism-mawsul"], 109: ["ism-maqsur-manqus", "ism-mamdud"],
    110: ["ism-maqsur-manqus", "ism-mamdud"], 111: ["al-muannath-wa-alamatuh"], 112: ["mithal-verbs"], 116: ["jam-taksir"], 119: ["kana-wa-akhawatuha", "zanna-wa-akhawatuha"], 120: ["tamyiz"], 121: ["al-lam-wa-rubba-fil-kafiya"]}
notes = {json.loads(f.read_text(encoding='utf-8'))['id'] for f in Path('content/grammar').glob('*.json')}
bad = [(n, i) for n, ids in LINKS.items() for i in ids if i not in notes]; assert not bad, bad
# the masala's own region lines, to cut the split-shape statements from (the opening paragraph)
def region(r): return ' '.join(r['region'])
SPLIT = {  # n: {school: (start marker, end marker-exclusive or None for «to the sentence's full stop»)}
    34: {'kufa': ('اختلف مذهب الكوفيين', '. وذهب البصريون')},
    74: {'kufa': ('اختلف مذهب الكوفيين', '، وذهب البصريون')},
    84: {'basra': ('واختلف البصريون', None)},
    120: {'kufa': ('اختلف الكوفيون', 'من البصريين.'), 'basra': ('وذهب أكثر البصريين', None)},
    77: {'kufa': ('ذهب الكوفيين', None)}, 104: {'kufa': ('ذهب الكوفيين', None)}}
SHAPE = {34: "The book opens with the Kufans' own split («اختلف مذهب الكوفيين»): their pane holds the whole split, not one «ذهب الكوفيون» sentence.",
    74: "The book opens with the Kufans' own split («اختلف مذهب الكوفيين»): their pane holds the whole split.",
    84: "The Basrans' view is a split («واختلف البصريون»): their pane holds the whole split, to al-Māzinī.",
    120: "Both views are reported as splits («اختلف الكوفيون», «وذهب أكثر البصريين»), not as «ذهب الكوفيون/البصريون».",
    77: "The print reads «ذهب الكوفيين» (sic); the statement is kept as printed.", 104: "The print reads «ذهب الكوفيين» (sic); the statement is kept as printed.",
    44: "As printed, both schools say «لا يجوز»; the Kufan sentence is very likely a misprint — kept verbatim, left out of the masked round by the near-identical rule.",
    65: "As printed, the Kufan sentence says «يجب العطف» (likely for «يجوز»); kept verbatim.",
    73: "The Basran sentence runs on into its three proofs; it is cut at the first «؛», after «لثلاثة أوجه».",
    119: "One of three masāʾil the editor gives from some manuscripts only («زيادة ثلاث مسائل في بعض النسخ»).",
    120.5: None}
def cut_span(txt, a, b):
    i = txt.find(a); assert i >= 0, (a,)
    if b is None:
        j = txt.find('.', i); j = len(txt) if j < 0 else j + 1
    else:
        j = txt.find(b, i); assert j >= 0, (b,)
        if b.endswith('.'): j += len(b)
    return txt[i:j].strip().rstrip('،؛ ')
out = []
for r in raw:
    n = r['n']; R = rend.R[n]
    rec = {'n': n, 'bab': BAB_OF[n], 'title_ar': r['title_ar'], 'title_en': R[0], 'title_tr': R[1]}
    reg = region(r)
    for s in ('kufa', 'basra'):
        v = r.get(s + '_ar')
        if n in SPLIT and s in SPLIT[n]: v = cut_span(reg, *SPLIT[n][s])
        if v:
            # a statement that runs into the other school's or its own split is cut there
            for stop in ('، واختلف البصريون', '؛ فذهب', '، واختلف الكوفيون'):
                if stop in v and not (n in SPLIT and s in SPLIT[n]): v = v[:v.find(stop)]
            if len(v) > 300 and '؛' in v and not (n in SPLIT and s in SPLIT[n]): v = v[:v.find('؛')]
            rec[s + '_ar'] = v.rstrip('،؛ ')
            rec[s + '_en'], rec[s + '_tr'] = (R[2], R[3]) if s == 'kufa' else (R[4], R[5])
        else:
            rec[s + '_why_en'] = "The book does not state this school's view in one «ذهب …» sentence here."
            rec[s + '_why_tr'] = "Kitap bu mezhebin görüşünü burada tek bir «ذهب …» cümlesiyle söylemiyor."
    # third views and agreements: verbatim, minus whatever a pane already holds
    oth = []
    for o in r['others']:
        a = o['ar']
        if o['agrees'] is not None and a.startswith('وإليه ذهب') and '،' in a: a = a[:a.find('،')]
        a = a.rstrip('،؛ ')
        if any(a and a.rstrip('.') in rec.get(s + '_ar', '') for s in ('kufa', 'basra')): continue
        if bare(a).startswith(('ذهب الكوفيين', 'وذهب أكثر البصريين')): continue
        oth.append({'ar': a, **({'with': o['agrees']} if o['agrees'] in ('kufa', 'basra') else {})})
    if oth: rec['others'] = oth
    # tarjih: an explicit sentence that names a school wins; else the answer section; else unstated
    exp = [c for c in r['tj_cands'] if re.match(r'^(والصحيح|والذي أذهب إليه|والمختار|وهو الصحيح)', c['ar']) and school_of(c['ar'])]
    ans = r['tj_answer']
    if exp:
        rec['tarjih'], rec['tarjih_ar'], rec['tarjih_src'] = school_of(exp[0]['ar']), exp[0]['ar'], 'explicit'
        if ans and ans['school'] != rec['tarjih']: print('CONFLICT', n, rec['tarjih'], ans['school'])
    elif ans:
        rec['tarjih'], rec['tarjih_ar'], rec['tarjih_src'] = ans['school'], ans['ar'], 'answer'
    else:
        rec['tarjih'] = 'unstated'
    rec['page'] = {'printed': r['page']['printed'], 'shamela': r['page']['shamela']}
    if r.get('extra'): rec['extra'] = True
    if n in SHAPE and SHAPE[n]: rec['shape_note'] = SHAPE[n]
    if n in LINKS: rec['links'] = LINKS[n]
    out.append(rec)
# the guard: every Arabic string is in the source, verbatim
miss = []
def walk(o, at):
    for k, v in o.items():
        if isinstance(v, str) and (k.endswith('_ar') or k == 'ar') and v not in src: miss.append((at, k, v[:60]))
        elif isinstance(v, list): [walk(x, at) for x in v if isinstance(x, dict)]
        elif isinstance(v, dict): walk(v, at)
for rec in out: walk(rec, rec['n'])
assert not miss, miss
doc = {'source': {'book': 'الإنصاف في مسائل الخلاف بين النحويين البصريين والكوفيين', 'author': 'أبو البركات الأنباري (ت ٥٧٧)',
       'editor': 'محمد محيي الدين عبد الحميد — الانتصاف من الإنصاف', 'publisher': 'المكتبة العصرية، ط١ ١٤٢٤ هـ / ٢٠٠٣ م', 'shamela': 7362,
       'file': 'research/sources/insaf-ibn-al-anbari-src.txt', 'fetched': '2026-11-26',
       'note': 'Every _ar field is a verbatim substring of the source file (checked by tools/smoke_test.js, v339). en/tr are renderings awaiting review.'},
       'babs': [{'id': b[0], 'ar': b[1], 'en': b[2], 'tr': b[3]} for b in BABS], 'masail': out}
Path(OUT).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
from collections import Counter
print('masail', len(out), Counter(r['tarjih'] for r in out), Counter(r.get('tarjih_src') for r in out))
print('no kufa', [r['n'] for r in out if 'kufa_ar' not in r], 'no basra', [r['n'] for r in out if 'basra_ar' not in r])
