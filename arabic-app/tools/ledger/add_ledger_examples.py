#!/usr/bin/env python3
"""v342-S — the ledger's OPEN rule sentences of Marāḥ al-Arwāḥ and Taṣrīf al-ʿIzzī go into the ṣarf note that teaches their chapter, as an
example quoting the book's line VERBATIM (cut from the ledger, which cut it from research/sources) with its line anchor
(`source: <file>:<line> (ص <page>)`) and the story's own translation of that line (the story `marah-al-arwah` / `tasrif-al-izzi` is the
src cut into sentences: every src line has its sentence(s), and their en / tr are joined — nothing is translated here). Marāḥ pp. 145–182
(the raw matn, no story) take the renderings in tools/ledger/matn_renderings.json, marked awaiting review.
Three notes the books need and the shelf lacked are created: mahmuz-verbs, lafif-verbs, ibdal.

    python3 tools/ledger/add_ledger_examples.py [--dry]
Idempotent: an example whose `source` is already in the note is not added twice. Run tools/ledger/sarf_ledger.py after it.
"""
import json, re, glob, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HAR = re.compile('[ؐ-ًؚ-ٰٟـ]')
def B(s): return re.sub(r'[^ء-ي]', '', HAR.sub('', s))

MARAH = {2: 'thulathi-mujarrad-babs', 3: 'masdar', 4: 'masdar', 5: 'masdar', 6: 'masdar', 7: 'thulathi-mujarrad-babs', 8: 'augmented-babs',
         9: 'al-fil-wal-madi-wal-mudari-fil-kafiya', 10: 'al-bariz-al-muttasil', 11: 'al-bariz-al-muttasil', 12: 'al-bariz-al-muttasil',
         13: 'al-marifa-al-mudmarat-wal-alam', 14: 'al-marifa-al-mudmarat-wal-alam', 15: 'al-marifa-al-mudmarat-wal-alam',
         16: 'al-marifa-al-mudmarat-wal-alam', 17: 'al-marifa-al-mudmarat-wal-alam', 18: 'al-fil-wal-madi-wal-mudari-fil-kafiya',
         19: 'al-fil-wal-madi-wal-mudari-fil-kafiya', 20: 'al-fil-wal-madi-wal-mudari-fil-kafiya', 21: 'al-fil-wal-madi-wal-mudari-fil-kafiya',
         22: 'al-fil-wal-madi-wal-mudari-fil-kafiya', 23: 'afal-khamsa', 24: 'imperative-amr', 25: 'imperative-amr', 26: 'imperative-amr',
         27: 'imperative-amr', 28: 'imperative-amr', 29: 'nun-al-tawkid-fil-kafiya', 30: 'nun-al-tawkid-fil-kafiya', 31: 'al-majhul-fil-kafiya',
         32: 'al-majhul-fil-kafiya', 33: 'ism-al-fail-wal-maful-fil-kafiya', 34: 'ism-al-fail-wal-maful-fil-kafiya', 35: 'sifa-mushabbaha',
         36: 'ism-tafdil', 37: 'sighat-mubalagha', 38: 'sighat-mubalagha', 39: 'ism-al-fail-wal-maful-fil-kafiya', 40: 'ism-al-fail-wal-maful-fil-kafiya',
         41: 'ism-al-zaman-wal-makan', 42: 'ism-al-ala', 43: 'doubled-verbs', 44: 'doubled-verbs', 45: 'doubled-verbs', 46: 'doubled-verbs',
         47: 'form-viii-verbs', 48: 'form-viii-verbs', 49: 'form-viii-verbs', 50: 'form-viii-verbs', 51: 'form-v-verbs',
         **{c: 'mahmuz-verbs' for c in range(52, 63)}, **{c: 'mithal-verbs' for c in range(63, 67)}, **{c: 'hollow-verbs' for c in range(67, 77)}}
IZZI = {1: 'thulathi-mujarrad-babs', 2: 'thulathi-mujarrad-babs', 3: 'augmented-babs', 4: 'al-lazim-wal-mutaaddi', 5: 'al-fil-wal-madi-wal-mudari-fil-kafiya',
        6: 'al-fil-wal-madi-wal-mudari-fil-kafiya', 7: 'nawasib-wa-jawazim-al-mudari', 8: 'imperative-amr', 9: 'form-viii-verbs',
        10: 'nun-al-tawkid-fil-kafiya', 11: 'ism-al-fail-wal-maful-fil-kafiya', 12: 'doubled-verbs', 13: 'mithal-verbs', 14: 'hollow-verbs',
        15: 'naqis-verbs', 16: 'lafif-verbs', 17: 'mahmuz-verbs', 18: 'ism-al-zaman-wal-makan', 19: 'ism-al-ala'}
BOOK = {'marah': ('marah-al-arwah', 'marah-al-arwah-src.txt', MARAH), 'izzi': ('tasrif-al-izzi', 'tasrif-al-izzi-src.txt', IZZI)}

def story(pkg):
    out = []
    for cf in glob.glob(os.path.join(ROOT, 'content', 'samples', pkg, 'chapters', '*.json')):
        n = int(os.path.basename(cf)[:-5])
        for s in json.load(open(cf, encoding='utf8'))['sentences']:
            out.append((n, s['id'], B(''.join(t['surface']['full'] for t in s['tokens'])), s.get('translation') or {}))
    return out

def src_line(f, n): return open(os.path.join(ROOT, 'research', 'sources', f), encoding='utf8').read().split('\n')[n - 1]

def new_notes():
    """the three notes the books need — their Arabic titles cut from the books' own headings / lines"""
    M = open(os.path.join(ROOT, 'research', 'sources', 'marah-al-arwah-src.txt'), encoding='utf8').read().split('\n')
    I = open(os.path.join(ROOT, 'research', 'sources', 'tasrif-al-izzi-src.txt'), encoding='utf8').read().split('\n')
    head = lambda L, k: re.match(r'^## %d (\S+)' % k, [l for l in L if l.startswith('## %d ' % k)][0]).group(1)
    ibdal = re.search(r'الْإِبْدَالُ', I[137]).group(0)
    BL = open(os.path.join(ROOT, 'research', 'feeding-backlog-2026-11-19.md'), encoding='utf8').read()
    for w in ('اُأْمُلْ', 'اِأْزِرْ', 'اُومُلْ', 'اِيزِرْ'): assert w in BL or w in '\n'.join(I), w
    assert 'قِهْ' in I[278] and 'اِتَّقَدَ' in M[566] and 'اِوْتَقَدَ' in M[566]
    return {
     'mahmuz-verbs': {'id': 'mahmuz-verbs', 'title': {'ar': head(M, 52), 'en': 'The hamzated verb (mahmūz)', 'tr': 'Mehmûz fiil'}, 'level': 3, 'group': 'sarf',
      'classicalSources': ['تَصْرِيفُ الْعِزِّيِّ — فَصْلٌ فِي الْمَهْمُوزِ (tasrif-al-izzi-src.txt، س 287–327)', 'مَرَاحُ الْأَرْوَاحِ — الْمَهْمُوزُ (marah-al-arwah-src.txt، س 593–686)'],
      'plain': {'en': 'A verb with a hamza among its root letters (أَخَذَ، سَأَلَ، قَرَأَ) is conjugated like a sound verb; the hamza itself may be softened, and two hamzas in one word never stay side by side.',
                'tr': 'Kök harflerinden biri hemze olan fiil (أَخَذَ، سَأَلَ، قَرَأَ) sahih fiil gibi çekilir; hemzenin kendisi hafifletilebilir, bir kelimede iki hemze yan yana kalmaz.'},
      'explanation': {'en': 'The ʿIzzī (ch. 17) and the Marāḥ (ch. 52–62) agree that the hamza is a sound letter: the mahmūz verb takes the sound verb\'s conjugation, and only the hamza\'s own changes are taught. It may be softened — turned to the letter of the vowel before it, dropped with its vowel moved back, or made «between the two». When two hamzas meet in one word and the second is quiescent, the second turns to the letter of the first one\'s vowel (آمَنَ وَأُومِنَ وَإِيمَانٍ; the amr اُومُلْ, ʿIzzī l. 290), and after a joining wāw or fāʾ the hamza comes back (وَأْمُلْ, l. 291). Heard against the rule: خُذْ، كُلْ، مُرْ, and يَرَى with its hamza dropped in the muḍāriʿ and in all of أَرَى. The Sarf lab conjugates any hamzated root by these rules (v334-N3); the examples below are the books\' own sentences, each with its line.',
                      'tr': 'İzzî (17. fasıl) ile Merâh (52–62. bâblar) hemzenin sahih bir harf olduğunda birleşir: mehmûz fiil sahih fiilin çekimini alır, yalnız hemzenin kendine has değişmeleri öğretilir. Hemze hafifletilebilir — öncesindeki harekenin harfine çevrilir, harekesi geri nakledilip düşürülür ya da «beyne beyne» okunur. Bir kelimede iki hemze buluşur ve ikincisi sâkin olursa, ikincisi birincinin harekesinin harfine döner (آمَنَ وَأُومِنَ وَإِيمَانٍ; emir اُومُلْ, İzzî s. 290); vav ya da fâdan sonra hemze geri gelir (وَأْمُلْ, s. 291). Kaideye aykırı olarak işitilenler: خُذْ، كُلْ، مُرْ ve muzârisinde ve bütün أَرَى\'da hemzesi düşen يَرَى. Sarf laboratuvarı her mehmûz kökü bu kurallarla çeker (v334-N3); aşağıdaki misaller kitapların kendi cümleleridir, her biri satırıyla.'},
      'examples': [], 'commonMistakes': [{'wrong': 'اُأْمُلْ', 'right': 'اُومُلْ', 'why': {'en': 'Two hamzas in one word, the second quiescent: the second turns to the letter of the first one\'s vowel (ʿIzzī l. 290). The app\'s own Maqṣūd engine once wrote اُأْمُلْ (feeding backlog F2).', 'tr': 'Bir kelimede iki hemze, ikincisi sâkin: ikincisi birincinin harekesinin harfine döner (İzzî s. 290). Uygulamanın Maksûd motoru bir zamanlar اُأْمُلْ yazıyordu (besleme listesi F2).'}},
                                                     {'wrong': 'اِأْزِرْ', 'right': 'اِيزِرْ', 'why': {'en': 'After a kasra the second, quiescent hamza becomes a yāʾ (ʿIzzī l. 290).', 'tr': 'Kesreden sonra sâkin ikinci hemze yâ olur (İzzî s. 290).'}}],
      'relatedNotes': ['hamzat-al-wasl' if os.path.exists(os.path.join(ROOT, 'content', 'grammar', 'hamzat-al-wasl.json')) else 'imperative-amr', 'thulathi-mujarrad-babs', 'lafif-verbs']},
     'lafif-verbs': {'id': 'lafif-verbs', 'title': {'ar': head(I, 16), 'en': 'The doubly weak verb (lafīf)', 'tr': 'Lefîf fiil'}, 'level': 4, 'group': 'sarf',
      'classicalSources': ['تَصْرِيفُ الْعِزِّيِّ — اللَّفِيفُ (tasrif-al-izzi-src.txt، س 265–286)', 'مَرَاحُ الْأَرْوَاحِ — اللَّفِيفُ (marah-al-arwah-matn.txt، [ص 177]–[ص 182])'],
      'plain': {'en': 'A verb with two weak root letters. Separated (وَقَى): its first letter behaves like the mithāl\'s, its last like the nāqiṣ\'s — so the amr is a single letter, قِ, and in pause قِهْ. Joined (طَوَى): the last letter takes the weakening and the middle one stays.',
                'tr': 'İki kök harfi illetli fiil. Mefrûk (وَقَى): ilk harfi misâlinki, son harfi nâkısınki gibidir — emri tek harftir: قِ, vakıfta قِهْ. Makrûn (طَوَى): i\'lâli son harf alır, ortadaki kalır.'},
      'explanation': {'en': 'The ʿIzzī (ch. 16) and the Marāḥ (pp. 177–182, the raw matn) teach two kinds. The separated lafīf (مَفْرُوق: وَقَى يَقِي) drops its first wāw where the mithāl does and its last letter where the nāqiṣ does, so the amr is one letter and takes the hāʾ of pause (قِ — قِهْ). The joined lafīf (مَقْرُون: طَوَى يَطْوِي، رَوِيَ يَرْوَى) is a nāqiṣ whose ʿayn is kept sound, «so that two weakenings do not meet» (Marāḥ ch. 72, l. 778). The Sarf lab derives both kinds from any root (v334-N3); the Marāḥ\'s raw pages are quoted as printed, and their renderings await the hoca\'s review.',
                      'tr': 'İzzî (16. fasıl) ile Merâh (s. 177–182, ham metin) iki çeşit öğretir. Mefrûk lefîf (وَقَى يَقِي) ilk vâvını misâlin düşürdüğü yerde, son harfini nâkısın düşürdüğü yerde düşürür; emri tek harftir ve vakıf hâsını alır (قِ — قِهْ). Makrûn lefîf (طَوَى يَطْوِي، رَوِيَ يَرْوَى) aynı sahih bırakılmış bir nâkıstır, «iki i\'lâl toplanmasın diye» (Merâh 72. bâb, s. 778). Sarf laboratuvarı her iki çeşidi her kökten türetir (v334-N3); Merâh\'ın ham sayfaları basıldığı gibi alıntılanır, tercümeleri hocanın incelemesini bekler.'},
      'examples': [], 'commonMistakes': [{'wrong': 'قِ', 'right': 'قِهْ', 'why': {'en': 'In pause the one-letter amr takes the hāʾ of silence: «وَيَلْزَمُهُ الْهَاءُ فِي الْوَقْفِ» (ʿIzzī l. 279).', 'tr': 'Vakıfta tek harfli emir sekte hâsını alır: «وَيَلْزَمُهُ الْهَاءُ فِي الْوَقْفِ» (İzzî s. 279).'}}],
      'relatedNotes': ['naqis-verbs', 'mithal-verbs', 'hollow-verbs']},
     'ibdal': {'id': 'ibdal', 'title': {'ar': ibdal, 'en': 'Substitution of letters (ibdāl)', 'tr': 'İbdâl'}, 'level': 4, 'group': 'sarf',
      'classicalSources': ['مَرَاحُ الْأَرْوَاحِ — حروف الإبدال (marah-al-arwah-matn.txt، [ص 162]–[ص 176])', 'مَرَاحُ الْأَرْوَاحِ (marah-al-arwah-src.txt، س 566–573)'],
      'plain': {'en': 'One letter put in place of another. The Marāḥ counts the letters that may replace others in a mnemonic sentence and gives, for each, what it replaces, why, and whether the change is necessary and regular, allowed and regular, or only heard.',
                'tr': 'Bir harfin başka bir harfin yerine konması. Merâh, başkalarının yerine geçebilen harfleri bir hatırlatma cümlesinde sayar ve her biri için neyin yerine geçtiğini, niçin geçtiğini ve değişmenin vâcip ve muttarid mi, câiz ve muttarid mi, yoksa yalnız işitilmiş mi olduğunu söyler.'},
      'explanation': {'en': 'The Marāḥ (pp. 162–176 of the raw matn) names the letters of substitution in one sentence and goes through them one by one. Some changes are NECESSARY AND REGULAR, and the app\'s engines make them: the alif for the wāw and the yāʾ (قال وباع), the hamza for the alif and the weak letter (صحراء، قائل، بائع), the yāʾ for the wāw after a kasra (ميقات), the wāw for the yāʾ after a ḍamma (مُوقِن), the tāʾ and the merge in the iftiʿāl of a wāw (اِتَّقَدَ, src l. 567), the ṭāʾ after the covered letters (اِضْطَرَبَ), the hāʾ of pause for the tāʾ. Others are ALLOWED AND REGULAR (the hamza softened: راس، ذيب، لُوم), and the rest are HEARD — dialects and single words the book quotes (the jīm for the yāʾ in حَجَّتِجْ … بِجْ, the mīm for the lām of the article in امْبِرِّ امصْيَامُ, أُصَيْلاَل). «والموضع الذي لم يقيد فيه من الصور المذكورة يكون جائزاً غيرَ غير مطرد» — where the book sets no condition, the change is allowed but not regular, so no engine makes it. These pages are raw and uncollated; they are quoted as printed, and their renderings await the hoca\'s review.',
                      'tr': 'Merâh (ham metnin 162–176. sayfaları) ibdâl harflerini tek bir cümlede sayar ve onları tek tek ele alır. Bazı değişmeler VÂCİP VE MUTTARİDdir ve uygulamanın motorları onları yapar: vâv ve yânın yerine elif (قال وباع), elif ve illet harfinin yerine hemze (صحراء، قائل، بائع), kesreden sonra vâvın yerine yâ (ميقات), dammeden sonra yânın yerine vâv (مُوقِن), vâvın ifti\'âlinde tâ ve idgâm (اِتَّقَدَ, src s. 567), itbak harflerinden sonra tâ (اِضْطَرَبَ), vakıfta tânın yerine hâ. Bazıları CÂİZ VE MUTTARİDdir (hafifletilmiş hemze: راس، ذيب، لُوم), geri kalanı İŞİTİLMİŞTİR — kitabın alıntıladığı lehçeler ve tek kelimeler. Kitap kayıt koymadığı yerde değişme câizdir ama muttarid değildir; bu yüzden hiçbir motor onu yapmaz. Bu sayfalar ham ve karşılaştırılmamıştır; basıldıkları gibi alıntılanır, tercümeleri hocanın incelemesini bekler.'},
      'examples': [], 'commonMistakes': [{'wrong': 'اِوْتَقَدَ', 'right': 'اِتَّقَدَ', 'why': {'en': 'The wāw before the tāʾ of iftiʿāl becomes a tāʾ and merges into it (Marāḥ src l. 567).', 'tr': 'İfti\'âl tâsından önceki vâv tâya döner ve ona idgâm edilir (Merâh src s. 567).'}}],
      'relatedNotes': ['form-viii-verbs', 'hollow-verbs', 'mahmuz-verbs']},
    }

def main():
    dry = '--dry' in sys.argv
    G = os.path.join(ROOT, 'content', 'grammar')
    notes, created = {}, []
    for nid, n in new_notes().items():
        p = os.path.join(G, nid + '.json')
        if not os.path.exists(p): notes[nid] = n; created.append(nid)
    def note(nid):
        if nid not in notes: notes[nid] = json.load(open(os.path.join(G, nid + '.json'), encoding='utf8'))
        return notes[nid]
    added = {}
    for b, (pkg, f, MAP) in BOOK.items():
        S = story(pkg)
        cov = json.load(open(os.path.join(ROOT, 'content', 'rules', f'coverage_{b}.json'), encoding='utf8'))
        for e in cov['entries']:
            if e['status'] != 'open' or e['kind'] == 'discourse' or e.get('file'): continue
            nid = MAP.get(e['section'])
            if not nid: continue
            ar = re.sub(r'\s*\[print: [^\]]*\]', '', e['ar'])   # the src's editorial note on the print is not the book's text
            bl = B(ar); hit = [s for s in S if s[0] == e['section'] and s[2] and s[2] in bl] or [s for s in S if s[2] and s[2] in bl]
            if not hit: print('no sentence for', e['id']); continue
            hit.sort(key=lambda s: bl.index(s[2]))
            src = f"{f}:{e['line']}" + (f" (ص {e['page']})" if e.get('page') else '')
            N = note(nid)
            if any((x.get('source') or '').split(' ')[0] == src.split(' ')[0] for x in N['examples']): continue
            assert e['ar'] == src_line(f, e['line']).strip()          # verbatim, by line
            ex = {'ar': ar, 'en': ' '.join(h[3].get('en', '') for h in hit).strip(), 'tr': ' '.join(h[3].get('tr', '') for h in hit).strip(),
                  'sourceStory': pkg, 'chapter': hit[0][0], 'sentence': hit[0][1], 'source': src}
            N['examples'].append(ex); added[nid] = added.get(nid, 0) + 1
    # the raw matn, with our renderings
    R = json.load(open(os.path.join(ROOT, 'tools', 'ledger', 'matn_renderings.json'), encoding='utf8'))['units']
    cov = {e['id']: e for e in json.load(open(os.path.join(ROOT, 'content', 'rules', 'coverage_marah.json'), encoding='utf8'))['entries']}
    for eid, r in R.items():
        e = cov.get(eid)
        if not e or e['status'] != 'open': continue
        lines = e.get('lines') or [e['line']]
        part = eid.split('.')[-1] if '.' in eid else '1'
        src = 'marah-al-arwah-matn.txt:' + '–'.join(str(x) for x in ([lines[0], lines[-1]] if len(lines) > 1 else lines)) + f' [{part}]' + (f" (ص {e['page']})" if e.get('page') else '')
        N = note(r['note'])
        if any((x.get('source') or '') == src for x in N['examples']): continue
        raw = open(os.path.join(ROOT, 'research', 'sources', 'marah-al-arwah-matn.txt'), encoding='utf8').read()
        assert all(p in raw for p in e['ar'].split(' ') if p), eid
        N['examples'].append({'ar': e['ar'], 'en': r['en'] + ' [rendering awaiting review]', 'tr': r['tr'] + ' [tercüme inceleme bekliyor]', 'source': src})
        added[r['note']] = added.get(r['note'], 0) + 1
    # a new note needs one example anchored in a story: the book line that states its rule, with the story's translation
    ANCHOR = {'ibdal': ('marah', 567)}
    for nid, (b, ln) in ANCHOR.items():
        if nid not in notes or any(x.get('sourceStory') for x in notes[nid]['examples']): continue
        pkg, f, _ = BOOK[b]; ar = src_line(f, ln).strip(); bl = B(ar); hit = sorted([s for s in story(pkg) if s[2] and s[2] in bl], key=lambda s: bl.index(s[2]))
        notes[nid]['examples'].insert(0, {'ar': ar, 'en': ' '.join(h[3].get('en', '') for h in hit), 'tr': ' '.join(h[3].get('tr', '') for h in hit),
                                          'sourceStory': pkg, 'chapter': hit[0][0], 'sentence': hit[0][1], 'source': f'{f}:{ln}'})
    for eid, r in R.items():
        if eid not in cov or cov[eid]['status'] != 'open': print('rendering not used (not open):', eid, cov.get(eid, {}).get('status'))
    for nid in created:
        if not any(x.get('sourceStory') for x in notes[nid]['examples']): print('WARN no story example', nid)
    print('created', created); print('added', added, sum(added.values()))
    if dry: return
    for nid, n in notes.items():
        json.dump(n, open(os.path.join(G, nid + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=2)
        open(os.path.join(G, nid + '.json'), 'a', encoding='utf8').write('\n')

if __name__ == '__main__':
    main()
