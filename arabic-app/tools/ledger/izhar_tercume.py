#!/usr/bin/env python3
"""v353-I — content/rules/izhar_tercume.json: the owner's own Turkish translation of Iẓhār joined to the course map.

Source: research/sources/izhar-tercume-full.txt (the owner's upload izhar_tercumesi.pdf, modern Turkish, pdftotext; the PDF's
table columns are flattened: for each item the MEANING in Turkish and the Turkish of the translator's example, with that
example's Arabic beside it in broken presentation forms). The other two files were looked at and not used:
izhar-full-corrected.txt is an Ottoman-script (Arabic-letter) commentary, izhar-amil-mamul-irab.txt 20 Ottoman lines of notes.

The JOIN table below was made by hand, reading the file: item id → the file lines of its meaning and of its example's Turkish
(and of the example's broken Arabic). The script cuts each Turkish string VERBATIM from those lines: the lines are joined with one
space and whitespace is folded, and the string must be a substring of that (lines skipped between two cited lines may only be page
numbers, blank or Arabic-script lines — checked). Nothing is composed in Turkish.

The example's ARABIC is never taken from the extraction: the broken Arabic is NFKC-normalised, reduced to bare letters and compared
AS A BAG with every contiguous token window of the Iẓhār package (content/samples/izhar-al-asrar); the pairing is kept only when a
window's bag is equal — then the example is the package's vowelled tokens (chapter, sentence, from–to). Most of the translator's
examples are his own devotional sentences (آمَنْتُ بِاللهِ …), not the matn's, and stay unpaired: the unit then shows the meaning only.

EN: `en` is our one-line rendering of the Turkish meaning, shown marked «translation · pending review».
usage: python3 tools/ledger/izhar_tercume.py      → content/rules/izhar_tercume.json (+ prints coverage)
"""
import json, re, os, glob, unicodedata, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(ROOT, *a)
SRC = 'research/sources/izhar-tercume-full.txt'
OUT = P('content/rules/izhar_tercume.json')

# id: (meaning lines, meaning substring or None for the whole span, example lines, example substring or None, Arabic lines | None, en)
# line spec: 'a-b' or 'a' or 'a-b,c-d' (lines between two ranges must be page numbers / blank / Arabic)
JOIN = {
 # ── bāb 1, samāʿī: the twenty jarr letters (the file's table «CER HARFLERİ», ll. 166–337; its order ب من إلى عن على ل في ك حتى رب و ت
 #    حاشا خلا عدا مذ منذ لولا كي لعل — the matn's, but خلا / عدا before مذ / منذ; each Turkish example sits beside the Arabic line «… :X»)
 'I-A01': ('178-179', None, '180-181', None, '175-176', 'ilṣāq (attaching), cause, accompaniment — “to, at, with”'),
 'I-A02': ('182-183', None, '184', None, '193-194', 'ibtidāʾ (beginning), nearness — “from”'),
 'I-A03': ('185-186', None, '187-188', None, '195-196', 'intihāʾ (the end point), result — “to”'),
 'I-A04': ('189-190', None, '191', None, '197-199', 'buʿd and mujāwaza (moving away) — “from, away from”'),
 'I-A05': ('201', None, '202-203', None, '210-211', 'istiʿlāʾ (being upon) — “on, upon”'),
 'I-A06': ('204', None, '205-206', None, '237', 'taʿlīl (cause, reason) — “for”'),
 'I-A07': ('207', None, '208', None, '240-241', 'ẓarf (containing) — “in, at”'),
 'I-A08': ('213', None, '214-215', None, '229', 'tashbīh (likening) — “like”'),
 'I-A09': ('216', 'Gaye,sonuç, …ye kadar', '217-219', None, '246-247', 'ghāya (the limit), result — “until, up to”'),
 'I-A10': ('220-221', 'Azlık, çokluk, öyleleri var ki, nice…', '222-223', None, '249-252', 'fewness, muchness — “many a …”'),
 'I-A11': ('224', 'Qasem (yemin)', '225-227', None, '253-254', 'qasam (an oath) — “by …”'),
 'I-A12': ('265', None, '266-268', None, '261-263', 'qasam (an oath) — “by …”'),
 'I-A13': ('276', 'İstisna, tenzih', '277', None, '270-274', 'exception, clearing of blame — “except”'),
 'I-A16': ('278', 'İstisna, tenzih', '279-280', None, '293-294', 'exception, clearing of blame — “except”'),
 'I-A17': ('281', 'İstisna, tenzih', '282-283', None, '299-305', 'exception, clearing of blame — “except”'),
 'I-A14': ('284-285', 'Geçmiş zamanda başlangıç,.. den beri, …dan beri.', '286-287', None, '306-307', 'the beginning in past time — “since”'),
 'I-A15': ('288-289', 'Geçmiş zamanda başlangıç,.. den beri, …dan beri.', '290-291', None, '308-310', 'the beginning in past time — “since”'),
 'I-A18': ('315', '….olmasaydı, ….olurdu', '316-319', None, '312-313', '“had it not been for …, … would have”'),
 'I-A19': ('325', 'İçin, ta ki, … e kadar', '326', None, '321-323', '“for, so that” (with interrogative mā: “why?”)'),
 'I-A20': ('334-335', 'Umulur ki, keşke olsa Teracci (ümid)', '336-337', None, '332', 'tarajjī (hope) — “perhaps, would that”'),
 # ── the six letters «İSMİNİ NASB HABERİNİ REF EDEN HARFLER» (ll. 602–665) and lā of the genus
 'I-A21': ('607', None, '608-611', None, '667', 'taḥqīq (making certain) — “indeed”'),
 'I-A22': ('612', None, '613-616,620-621', None, '669-671', 'taḥqīq (making certain) — “that (it is certain that)”'),
 'I-A23': ('622', None, '623', None, '672-674', 'tashbīh (likening) — “as if, like”'),
 'I-A24': ('627', None, '628-630', None, '675-678', 'istidrāk (correcting what went before) — “but”'),
 'I-A25': ('634', None, '635-636', None, '680-682', 'tamannī (wishing) — “would that”'),
 'I-A26': ('640', None, '641-645', None, '683', 'tarajjī (hoping) — “perhaps, it is hoped that”'),
 'I-A27': ('659-660', None, '661-665', None, '692-693', 'denying the whole genus — “there is no … at all”'),
 # ── «İSMİNİ REF HABERİNİ NASB EDEN HARFLER» (ll. 698–721)
 'I-A29': ('701-702', None, '703-707', None, '709-710', 'mā resembling laysa'),
 'I-A30': ('714-715', None, '716-719', None, '721', 'lā resembling laysa'),
 # ── jazm of one verb (ll. 1095–1113): the meanings «Mazide nefy için» (لم لما) and «Talep için» (lām of command, lā of forbidding),
 #    in the order of the Arabic table beside them (l. 1112 «لم لما», l. 1113 «لام الأمر لا في النهي»)
 'I-A35': ('1101', None, '1096-1097', None, '1104', 'negating the past'),
 'I-A36': ('1101', None, '1098', None, '1106', 'negating the past'),
 'I-A37': ('1102', None, '1099', None, '1108-1109', 'requesting (a command)'),
 'I-A38': ('1102', None, '1100', None, '1110-1111', 'requesting (a prohibition)'),
 # ── jazm of two verbs (ll. 1118–1190): the examples beside «… :X»; the meanings as the matn groups them (l. 27: أين وأنى للمكان،
 #    وإذما وإذا ما ومتى للزمان) — «Zaman için» / «Mekan için»; أي «İstifham (soru) için»; من «Mevsul» left out (uncertain)
 'I-A39': (None, None, '1119', None, '1122-1124', None),
 'I-A40': ('1152', None, '1146', None, '1166-1167', 'for place'),
 'I-A41': ('1152', None, '1139', None, '1155-1157', 'for place'),
 'I-A42': ('1152', None, '1142-1143', None, '1159-1160', 'for place'),
 'I-A43': ('1151', None, '1147-1148', None, '1169-1170', 'for time'),
 'I-A44': ('1151', None, '1149-1150', None, '1172-1176', 'for time'),
 'I-A45': ('1151', None, '1140-1141', None, '1158', 'for time'),
 'I-A46': ('1188', None, '1120', None, '1127', '“whatever (thing)”'),
 'I-A47': ('1188', None, '1129-1130', None, '1132', '“whatever (thing)”'),
 'I-A48': ('1153', None, '1144-1145', None, '1161-1164', 'interrogative (question) word'),
 'I-A49': (None, None, '1134', None, '1136-1137', None),
 # ── nasb of the muḍāriʿ (ll. 1063–1093): examples only (the meanings sit in the Arabic column, lost)
 'I-A31': (None, None, '1064-1065', None, '1075-1078', None),
 'I-A32': (None, None, '1066-1067', None, '1081-1082', None),
 'I-A33': (None, None, '1068-1069', None, '1083-1087', None),
 'I-A34': (None, None, '1070-1072', None, '1090-1093', None),
 # ── bāb 1, qiyāsī and maʿnawī: the section's own statement of how it governs
 'I-A50': ('1306-1307', None, '1294-1295', None, '1298-1299', 'every verb takes one doer in rafʿ and one or more objects in naṣb'),
 'I-A51': ('1956-1957', None, '1965', None, '1970-1972', 'works like the active verb: rafʿ of its doer, naṣb of its object'),
 'I-A52': ('1982-1983', None, '1988', None, '1990-1991', 'works like the passive verb: takes a deputy doer in rafʿ'),
 'I-A53': ('2099', None, '2115-2116', None, '2118-2127', 'works like its own verb: rafʿ of its doer'),
 'I-A54': ('2165-2166', None, '2136-2142', None, '2153-2156', 'without conditions it governs a hidden pronoun as doer and naṣb of a ẓarf, ḥāl and tamyīz'),
 'I-A55': ('2314-2317', 'Bu cümlede i’taen mastarı, abdu kelimesini fail almış ref etmiş, fakir ve dirhem kelimelerini de meful alarak nasb etmiştir.', '2312-2314', 'Allah Subhanehu ve Teala, kulunun , kendisi için , bir fakire dirhem vermesini sever.', None, 'governs a doer in rafʿ and objects in naṣb'),
 'I-A56': ('2398-2399', 'İsmi muzaf , kendisnden sonra gelen ve muzafun ileyh diye isimlendirilen kelimeyi cer eder.', '2392-2393', None, '2395-2396', 'puts the word after it, the muḍāf ilayh, in jarr'),
 'I-A57': ('2621-2628', 'İşrune amildir, reka’ten kelimesini nasb etmiştir.', '2618-2620', None, '2654-2658', 'governs: puts the tamyīz after it in naṣb'),
 'I-A58': ('2872-2873', None, None, None, None, 'the verb-nouns do the work of the past verbs whose meaning they carry'),
 'I-A59': ('3055-3061', 'Manevi amil tarafından hem mübteda hem de haber ref edilmişlerdir.', '3044', None, '3048-3052', 'by a governor of meaning both mubtadaʾ and khabar are in rafʿ'),
 'I-A60': ('3094-3096', None, '3045-3046', None, '3053', 'the muḍāriʿ is in rafʿ by a governor of meaning when it is free of the particles of naṣb and jazm'),
 # ── bāb 2: the translation is ordered by ʿāmil; a maʿmūl gets the line where the governing section names it
 'I-B01': ('1306-1309', 'Yani fiillerin merfu mamulleri , onların failleri (özneleri) dir,', None, None, None, 'the verbs’ rafʿ governees are their doers'),
 'I-B11': ('1308-1309', 'mensub mamulleri de onların mefulleri (nesneleri)dir.', None, None, None, 'their naṣb governees are their objects'),
 'I-B03': ('3055-3061', 'Manevi amil tarafından hem mübteda hem de haber ref edilmişlerdir.', None, None, None, 'by a governor of meaning both mubtadaʾ and khabar are in rafʿ'),
 'I-B05': ('3055-3061', 'Manevi amil tarafından hem mübteda hem de haber ref edilmişlerdir.', None, None, None, 'by a governor of meaning both mubtadaʾ and khabar are in rafʿ'),
 'I-B06': ('602', None, None, None, None, 'the letters that put their ism in naṣb and their khabar in rafʿ'),
 'I-B19': ('602', None, None, None, None, 'the letters that put their ism in naṣb and their khabar in rafʿ'),
 'I-B07': ('1766-1768', 'Merfu olan Zeydun kelimesine kane fiilinin ismi,', None, None, None, 'the word in rafʿ is called the ism of kāna'),
 'I-B18': ('1766-1768', 'mensub olan alimen kelimesine , kane fiilinin haberi denilir.', None, None, None, 'the word in naṣb is called the khabar of kāna'),
 'I-B08': ('1018', None, None, None, None, 'these letters put their ism in rafʿ and their khabar in naṣb'),
 'I-B21': ('1018', None, None, None, None, 'these letters put their ism in rafʿ and their khabar in naṣb'),
 'I-B09': ('998-1001', '‘calisun’ kelimesini haber alıp sonunu ref etti.', None, None, None, 'it took «jālisun» as its khabar and put its end in rafʿ'),
 'I-B20': ('998-1001', 'Bu cümlede , Cinsini nefyeden ‘la’ harfi , ‘ğulame’ kelimesini isim alıp, sonunu nasb etti,', None, None, None, 'the lā that denies the genus took «ghulāma» as its ism and put its end in naṣb'),
 'I-B12': ('374-375', '‘fi’ ve ‘fi’ anlamında olanlar , müteallakları için mef’ulu fih olurlar.', None, None, None, '(phrases with) «fī» and what means «fī» are mafʿūl fīhi for what they hang on'),
 'I-B13': ('376-377', '‘Lam’ ve ‘lam’ manasında olanlar, müteallakları için mef’ulu leh olurlar', None, None, None, '(phrases with) «li» and what means «li» are mafʿūl lahu for what they hang on'),
 'I-B16': ('2625-2627', 'Rek’aten kelimesi manası kapalı olan Işrune kelimesini temyiz etmekte, ona açıklık kazandırmaktadır.', None, None, None, '«rakʿatan» makes clear (tamyīz) the vague «ʿishrūna»'),
 'I-B17': ('358', None, None, None, None, 'what the exception letters put in jarr is like the mustathnā of «illā»'),
 'I-B22': ('1063', None, None, None, None, 'the letters that put the muḍāriʿ in naṣb'),
 'I-B23': ('342-344', 'Cer harfleri ; fiil, fiil benzeri ve fiil manasında olan müteallaklarının anlamlarını mecrurlarına ulaştırıp, bitiştirir.', None, None, None, 'the jarr letters carry the meaning of what they hang on — a verb, its like or its meaning — to the word in jarr'),
 'I-B24': ('2398-2399', 'İsmi muzaf , kendisnden sonra gelen ve muzafun ileyh diye isimlendirilen kelimeyi cer eder.', None, None, None, 'the muḍāf puts the word after it, the muḍāf ilayh, in jarr'),
 'I-B25': ('1095', None, None, None, None, 'the letters that put one muḍāriʿ in jazm'),
 # ── bāb 3: the introduction (ll. 46–47) names two signs
 'I-C01': ('46-47', 'zammenin faillik işareti', None, None, None, 'the ḍamma is the sign of being the doer'),
 'I-C02': ('46-47', 'fethanın mefulluk işareti', None, None, None, 'the fatḥa is the sign of being the object'),
}

AR = re.compile('[؀-ۿﭐ-﷿ﹰ-﻿]')
def lines(spec):
    out = []
    for part in spec.split(','):
        a, _, b = part.partition('-'); out += list(range(int(a), int(b or a) + 1))
    return out
def fold(s): return re.sub(r'\s+', ' ', s).strip()
def skip_ok(L, ns):
    """lines skipped between two cited ranges: page numbers, blank, Arabic-script only"""
    bad = []
    for a, b in zip(ns, ns[1:]):
        for k in range(a + 1, b):
            s = L[k - 1].strip()
            if s and not re.fullmatch(r'\d+', s) and not AR.search(s): bad.append(k)
    return bad
def cut(L, spec, sub):
    ns = lines(spec)
    # within a range every line is taken; lines that are only Arabic or a page number are dropped from the Turkish
    use = [n for n in ns if L[n - 1].strip() and not AR.search(L[n - 1]) and not re.fullmatch(r'\d+', L[n - 1].strip())]
    whole = fold(' '.join(L[n - 1] for n in use))
    s = fold(sub) if sub else whole
    assert s in whole, (spec, s, whole)
    # strip a leading row number of the table («9 Gaye…»)
    if not sub: s = re.sub(r'^\d+\s+', '', s)
    assert not skip_ok(L, use), (spec, skip_ok(L, use))
    return s, use

HAR = re.compile(r'[ً-ْٰـ]')
def letters(s):
    s = unicodedata.normalize('NFKC', s); s = HAR.sub('', s)
    s = re.sub('[أإآٱ]', 'ا', s).replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'[^ء-ي]', '', s)
def bag(s): return collections.Counter(letters(s))

def package():
    sens = []
    for f in glob.glob(P('content/samples/izhar-al-asrar/chapters/*.json')):
        c = json.load(open(f, encoding='utf-8'))
        for s in c['sentences']:
            sens.append(dict(ch=c['chapter'], sid=s['id'], toks=[t['surface']['full'] for t in s['tokens']], tr=s.get('translation')))
    sens.sort(key=lambda s: (s['ch'], int(re.sub(r'\D', '', s['sid']) or 0)))
    return sens

def pair(sens, L, spec):
    """the example's Arabic as the package vowels it: a token window whose bare letters are the broken line's, as a bag"""
    raw = []
    for n in lines(spec):
        s = unicodedata.normalize('NFKC', L[n - 1])
        if ':' in s: s = s.split(':')[0]          # «… :X» — the table's label after the colon is the item, not the example
        raw.append(s)
    B = bag(' '.join(raw)); need = sum(B.values())
    if need < 6: return None, need
    hits = []
    for s in sens:
        lt = [letters(t) for t in s['toks']]
        for a in range(len(lt)):
            c = collections.Counter(); n = 0
            for b in range(a, len(lt)):
                c.update(lt[b]); n += len(lt[b])
                if n > need: break
                if n == need and c == B: hits.append(dict(ch=s['ch'], sid=s['sid'], **{'from': a, 'to': b}, ar=' '.join(s['toks'][a:b + 1])))
    return (hits[0] if hits else None), need

def main():
    L = open(P(SRC), encoding='utf-8').read().split('\n')
    m = json.load(open(P('content/rules/izhar_map.json'), encoding='utf-8'))
    ids = [i['id'] for i in m['items']]
    sens = package()
    out = []
    for iid in ids:
        j = JOIN.get(iid)
        if not j: out.append(dict(id=iid, meaning_tr=None, example_tr=None, src_lines=[], en=None, example=None)); continue
        ml, msub, el, esub, al, en = j
        mt, mu = cut(L, ml, msub) if ml else (None, [])
        et, eu = cut(L, el, esub) if el else (None, [])
        ex, need = pair(sens, L, al) if al else (None, 0)
        out.append(dict(id=iid, meaning_tr=mt, example_tr=et, src_lines=sorted(set(mu + eu)),
                        meaning_lines=mu, example_lines=eu, arabic_lines=lines(al) if al else [],
                        en=en if mt else None, example=ex))
    cov = dict(units=len(out), meaning=sum(1 for x in out if x['meaning_tr']), example_tr=sum(1 for x in out if x['example_tr']),
               paired=sum(1 for x in out if x['example']),
               by_bab={b: dict(units=sum(1 for x in out if x['id'][2] == b), meaning=sum(1 for x in out if x['id'][2] == b and x['meaning_tr']),
                               paired=sum(1 for x in out if x['id'][2] == b and x['example'])) for b in 'ABC'})
    doc = dict(source=SRC, built_by='tools/ledger/izhar_tercume.py',
               note='Turkish strings verbatim from the source lines (lines joined, whitespace folded; Arabic-script and page-number lines dropped); '
                    'the example is shown only where its broken Arabic equals, as a bag of bare letters, a token window of the Iẓhār package — '
                    'then the Arabic is the package\'s vowelled tokens; «en» is our rendering, pending review',
               coverage=cov, units=out)
    json.dump(doc, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(cov))
    for x in out:
        if x['example']: print('paired', x['id'], x['example']['ch'], x['example']['sid'], x['example']['ar'])

if __name__ == '__main__':
    main()
