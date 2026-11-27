#!/usr/bin/env python3
"""v342-N — the open ledger entries that are no matter for an engine go to the grammar notes, the book's own Arabic verbatim.

Each example's Arabic is CUT from its source, never typed: a Shudhūr rule's own example by index from shudhur-al-dhahab-qawaid.jsonl
(gloss = the rule's rule_en / rule_tr), a Shudhūr part-one line from shudhur-al-dhahab-src.txt (gloss = the shelf story's
translation of the same words), a Kāfiya sentence from the al-kafiya story (its own translation, anchored by sourceStory).
Idempotent: an example whose `source` (or story anchor) is already in the note is skipped.  python3 tools/ledger/feed_notes.py
"""
import json, os, re, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = os.path.join(ROOT, 'content', 'grammar')
H = re.compile('[ً-ْٰـ]')
def letters(s): return re.sub('[^ء-ي]', '', H.sub('', s or '').replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ى', 'ي').replace('ٱ', 'ا'))

RULES = [None] + [json.loads(l) for l in open(os.path.join(ROOT, 'research/sources/shudhur-al-dhahab-qawaid.jsonl'), encoding='utf-8') if l.strip()]
QAW = [''] + open(os.path.join(ROOT, 'research/sources/qawaid-al-irab-ibn-hisham-matn.txt'), encoding='utf-8').read().split('\n')
SRC = [''] + open(os.path.join(ROOT, 'research/sources/shudhur-al-dhahab-src.txt'), encoding='utf-8').read().split('\n')
def story_sentences(pkg):
    out = []
    for f in glob.glob(os.path.join(ROOT, 'content/samples', pkg, 'chapters', '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        for s in d['sentences']:
            out.append((d['chapter'], s['id'], ' '.join(t['surface']['full'] for t in s['tokens']), s.get('translation', {})))
    return out
KAF = {(str(c), sid): (ar, tr) for c, sid, ar, tr in story_sentences('al-kafiya')}
SHU = story_sentences('shudhur-al-dhahab')

# (note id, kind, key, example index for a Shudhūr rule)
FEED = [
 # Shudhūr part one: the definitions (src lines) → the notes that teach them
 ('al-kalima-wal-kalam', 'src', 4), ('al-kalima-wal-kalam', 'src', 6), ('al-kalima-wal-kalam', 'src', 8), ('al-kalima-wal-kalam', 'src', 10),
 ('al-kalima-wal-kalam', 'src', 11), ('al-kalima-wal-kalam', 'src', 12), ('al-kalima-wal-kalam', 'src', 14), ('al-kalima-wal-kalam', 'src', 17),
 ('al-kalima-wal-kalam', 'src', 19), ('al-muthanna', 'src', 41), ('jam-mudhakkar-salim', 'src', 45), ('afal-khamsa', 'src', 49),
 # Shudhūr rules that state what may be said or how the books read it — the rule's own example
 ('al-fail-al-muzhar-wa-tanith-amilih', 'rule', 59, 0), ('al-fail-al-muzhar-wa-tanith-amilih', 'rule', 63, 3),
 ('vocative-munada', 'rule', 47, 1), ('vocative-munada', 'rule', 26, 0), ('vocative-munada', 'rule', 25, 2),
 ('al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab', 'rule', 17, 0),
 ('al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab', 'rule', 18, 0),
 ('al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar', 'rule', 8, 0),
 ('jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha', 'rule', 9, 0),
 ('jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha', 'rule', 11, 0),
 ('la-nafiya-lil-jins', 'rule', 13, 0), ('la-nafiya-lil-jins', 'rule', 14, 0), ('la-nafiya-lil-jins', 'rule', 88, 1), ('la-nafiya-lil-jins', 'rule', 12, 2),
 ('asma-al-ishara-wal-mawsulat', 'rule', 28, 0), ('ism-mawsul', 'rule', 23, 1), ('ism-mawsul', 'rule', 43, 0),
 ('huruf-jarr-nawadir', 'rule', 32, 1), ('kana-wa-akhawatuha', 'rule', 72, 0), ('kana-wa-akhawatuha', 'rule', 73, 1),
 ('hadhf-al-jarr', 'rule', 177, 0), ('inna-wa-akhawatuha', 'rule', 145, 0), ('inna-wa-akhawatuha', 'rule', 146, 0), ('innama-kaffa', 'rule', 140, 1),
 ('nawasib-wa-jawazim-al-mudari', 'rule', 150, 2), ('huruf-jarr', 'rule', 173, 3), ('mawadi-kasr-inna', 'rule', 83, 1), ('mawadi-fath-anna', 'rule', 85, 0),
 ('ma-la-mushabbaha', 'rule', 77, 0), ('ma-la-mushabbaha', 'rule', 80, 0), ('ma-la-mushabbaha', 'rule', 81, 0), ('ma-la-mushabbaha', 'rule', 137, 0), ('ma-la-mushabbaha', 'rule', 138, 0),
 ('at-tahdhir', 'rule', 97, 0), ('maful-fih', 'rule', 106, 0), ('mubtada-khabar', 'rule', 66, 0), ('al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya', 'rule', 21, 0),
 ('mafulayn', 'rule', 205, 1), ('mafulayn', 'rule', 210, None), ('al-mudaf-wa-nawa-al-idafa', 'rule', 178, 3),
 # Kāfiya: its definitions and rulings, anchored to the shelf's chapter and sentence
 ('tarifat-daftar-al-kafiya', 'kaf', '1:s5'), ('tarifat-daftar-al-kafiya', 'kaf', '1:s7'), ('tarifat-daftar-al-kafiya', 'kaf', '1:s19'),
 ('tarifat-daftar-al-kafiya', 'kaf', '46:s3'), ('tarifat-daftar-al-kafiya', 'kaf', '46:s5'),
 ('al-muannath-wal-mudhakkar-fil-kafiya', 'kaf', '11:s4'), ('al-muannath-wal-mudhakkar-fil-kafiya', 'kaf', '11:s5'),
 ('jam-al-taksir-fil-kafiya', 'kaf', '14:s2'), ('al-mutaaddi-wa-afal-al-qulub-fil-kafiya', 'kaf', '24:s2'), ('huruf-tanbih', 'kaf', '38:s9'),
 ('kalla-wa-ta-al-tanith-wal-tanwin-fil-kafiya', 'kaf', '44:s7'), ('kalla-wa-ta-al-tanith-wal-tanwin-fil-kafiya', 'kaf', '44:s8'),
 ('jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha', 'kaf', '8:s7'),
 ('afal-al-madh-wal-dhamm-fil-kafiya', 'kaf', '28:s10'), ('kaanna-lakinna-layta-laalla-fil-kafiya', 'kaf', '36:s3'),

 # Qawāʿid al-Iʿrāb: the matn's own plain examples (never an āya: the file's āyāt await the page) for faces the engines do not read yet
 ('anwa-al-jumal', 'qaw', 71, 'إن قاما ويقعدا أخواك', 'A condition with two verbs sharing one doer: the joined verb is jussive though its clause is not yet complete — the condition clause has a seat of jazm.', 'Tek fâili paylaşan iki fiilli şart: cümle tamamlanmadan atfedilen fiil meczumdur — şart cümlesinin cezm mahalli vardır.'),
 ('anwa-al-jumal', 'qaw', 86, 'زيدٌ قام أبوه وقعد أخوه', 'The seventh clause with a seat: a clause joined to a khabar clause shares its seat (raf), or has none if joined to the whole nominal clause.', 'Mahalli olan yedinci cümle: haber cümlesine atfedilen cümle onun mahallini (ref) paylaşır; bütün isim cümlesine atfedilirse mahalli yoktur.'),
 ('anwa-al-jumal', 'qaw', 166, 'زيدٌ الخبزَ يأكلَه', 'An explaining clause: the written verb explains a dropped one that governs the fronted object.', 'Tefsir cümlesi: yazılı fiil, öne alınan mef\'ûlü nasbeden mahzûf fiili açıklar.'),
 ('anwa-ma', 'qaw', 435, 'نعم ما صنعتَ', '«mā» as a noun after «niʿma»: a complete indefinite, or a described one (the matn: two views).', '«Niʿme»den sonra isim olan «mâ»: tam nekre ya da mevsûf nekre (metin: iki görüş).'),
 ('anwa-ma', 'qaw', 431, 'ما أحسن زيدًا!', '«mā» of wonder — for Sībawayh a complete indefinite: «something made Zayd good».', 'Taaccüp «mâ»sı — Sîbeveyh\'e göre tam nekre: «bir şey Zeyd\'i güzel kıldı».'),
 ('anwa-al-waw', 'qaw', 393, 'صِرتُ والنيلَ', 'The wāw of accompaniment: the noun after it is in naṣb (mafʿūl maʿahu).', 'Maiyyet vâvı: ardındaki isim mansubdur (mef\'ûl maah).'),
 ('qad-harf', 'qaw', 373, 'قد يخرُجُ زيدٌ', '«qad» of expectation before a muḍāriʿ: what is awaited.', 'Muzâriden önce tevakku «kad»i: beklenen şey.'),
 ('in-shartiyya', 'qaw', 276, 'إن أحدٌ خيرًا من أحدٍ إلا بالعافية', 'The negating «in» of Ahl al-ʿĀliya, working like «laysa»: its khabar in naṣb.', 'Ehl-i Âliye\'nin «leyse» gibi amel eden nefiy «in»i: haberi mansub.'),
 ('hal-ma-man', 'qaw', 316, 'مررتُ بِمَنْ مُعجِبٍ لك', '«man» as an indefinite described: «I passed by someone who pleases you».', 'Mevsûf nekre «men»: «seni hoşnut eden biriyle karşılaştım».'),
 ('anwa-ma', 'qaw', 201, 'أنشدك الله لما فعلت', '«lammā» meaning «illā» (except): «I ask you by God only that you do it».', '«İllâ» mânâsında «lemmâ»: «Allah aşkına, yalnız şunu yapmanı isterim».'),
 ('insha-wa-tamanni', 'qaw', 358, 'لو تَنْزِلُ عندنا فتُصيبَ راحةً', '«law» of offer (ʿarḍ): its fāʾ-answer in naṣb.', 'Arz «lev»i: fâ ile gelen cevabı mansub.'),
]

def shudhur_src_example(line):
    ar = SRC[line].strip(); L = letters(ar)
    best = None
    for c, sid, sar, tr in SHU:
        if letters(sar) and (letters(sar) in L or L in letters(sar)): best = (c, sid, tr); break
    ex = {'ar': ar, 'source': 'research/sources/shudhur-al-dhahab-src.txt:%d (شذور الذهب، الفصل الأول)' % line}
    if best:
        ex.update({'en': best[2].get('en', ''), 'tr': best[2].get('tr', ''), 'sourceStory': 'shudhur-al-dhahab', 'chapter': best[0], 'sentence': best[1]})
    return ex

GLOSS_SRC = {   # part one has no shelf sentence for these lines: the gloss is ours, the Arabic the book's
 4: ('The word is a single utterance.', 'Kelime müfred bir sözdür.'),
 6: ('It is a noun, a verb or a particle.', 'O isim, fiil ve harftir.'),
 17: ('Speech is a meaningful utterance, meant as such.', 'Kelâm, maksûd ve faydalı bir sözdür.'),
 19: ('It is a statement, a request or a performative.', 'O haber, talep ve inşâdır.'),
}

def main():
    added = 0
    for item in FEED:
        nid, kind, key = item[0], item[1], item[2]
        path = os.path.join(G, nid + '.json'); d = json.load(open(path, encoding='utf-8'))
        ex = d.setdefault('examples', [])
        if kind == 'src':
            e = shudhur_src_example(key)
            if not e.get('en'):
                en, tr = GLOSS_SRC.get(key, (None, None))
                if not en:
                    r = [x for x in RULES[1:] if False]; en, tr = ('Shudhūr al-Dhahab, part one, line %d.' % key, 'Şuzûru\'z-Zeheb, birinci kısım, satır %d.' % key)
                e['en'], e['tr'] = en, tr
            sname = 'شذور الذهب لابن هشام — الفصل الأول'
        elif kind == 'rule':
            r = RULES[key]; idx = item[3]
            ar = r['examples'][idx] if (idx is not None and r['examples']) else r['rule_ar']
            if not ar: continue
            e = {'ar': ar, 'en': r['rule_en'], 'tr': r['rule_tr'], 'source': 'research/sources/shudhur-al-dhahab-qawaid.jsonl:%d (ص %d)' % (key, r['page'])}
            sname = 'شذور الذهب لابن هشام — %s، ص %d' % (r['bab'], r['page'])
        elif kind == 'qaw':
            line = QAW[key]; ar = item[3]
            assert ar in line, (key, ar)   # cut from the matn line, letter for letter
            e = {'ar': ar, 'en': item[4], 'tr': item[5], 'source': 'research/sources/qawaid-al-irab-ibn-hisham-matn.txt:%d (Qawāʿid al-Iʿrāb bāb %d)' % (key, 1 if key < 170 else 3)}
            sname = 'الإعراب عن قواعد الإعراب (ابن هشام) — الباب %s' % ('الأول' if key < 170 else 'الثالث')
        else:
            c, sid = key.split(':'); ar, tr = KAF[(c, sid)]
            e = {'ar': ar, 'en': tr.get('en', ''), 'tr': tr.get('tr', ''), 'sourceStory': 'al-kafiya', 'chapter': int(c), 'sentence': sid}
            sname = 'الكافية لابن الحاجب'
        dup = any((x.get('source') and x.get('source') == e.get('source')) or (x.get('sourceStory') == e.get('sourceStory') == 'al-kafiya' and str(x.get('chapter')) == str(e.get('chapter')) and x.get('sentence') == e.get('sentence')) for x in ex)
        if dup or any(letters(x.get('ar', '')) == letters(e['ar']) for x in ex): continue
        ex.append(e); added += 1
        cs = d.setdefault('classicalSources', [])
        if not any(sname.split(' — ')[0] in s and (kind == 'kaf' or sname.split(' — ')[1].split('،')[0] in s) for s in cs): cs.append(sname)
        json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('examples added:', added)

if __name__ == '__main__':
    main()
