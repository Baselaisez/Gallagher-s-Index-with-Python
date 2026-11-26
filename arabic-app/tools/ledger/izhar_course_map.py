#!/usr/bin/env python3
"""v351-I — content/rules/izhar_map.json: Iẓhār al-Asrār by the book's own count, every cell sourced.

The skeleton is the ledger's (content/rules/coverage_izhar.json, cut from the lithograph by tools/ledger/build_ledger.py):
the sixty ʿāmil (A01–A49 samāʿī, A50–A58 qiyāsī, A59–A60 maʿnawī), the thirty maʿmūl (B01–B30) and the ten signs of iʿrāb by
essence (C01–C10: three ḥarakāt, four letters, three omissions — the count of the suʾāl–cevap's Q83). Each item gets:
  matn      the lithograph line (file + line, verbatim) and the package sentence that carries it (chapter, sentence id, the
            vowelled tokens verbatim, the item's token index)
  tr        the modern-Turkish suʾāl–cevap unit (izhar-sual-cevap-tafsilatli.txt, numbered question → answer, verbatim; the PDF's
            Arabic did not survive extraction, so its runs are elided as «…» and «Đ/đ» — the extraction's İ/ı — restored)
  engine    the ledger's engine rule(s) (carried_by «engine:…») and the ledger's status
  notes     the grammar notes: the ledger's «note:…» and the notes whose Iẓhār examples cite that package sentence
  games     the games hub's rounds that drill it (ids of the hub buttons)
  examples  ≤ 3 corpus tokens (package:chapter:sentence:token) whose AUTHORED line names the item and whose ENGINE line
            (Murib.line over SentenceAnalyzer, in the built page — tools/ledger/izhar_course_probe.js) names it too
  pool      ≤ 12 such tokens for the course's exercises
  ilal      reason ids of content/rules/ilal.json on the item's topic
The writer's rules («يُقَالُ / لَا يُقَالُ»): the book's own allowed and forbidden examples, each the matn's words (the package's
vowelled tokens where the package carries them), with its lithograph line.
usage: python3 tools/ledger/izhar_course_map.py [--no-probe]   (the probe needs NODE_PATH / CHROMIUM_PATH and a built page)
"""
import json, re, os, sys, glob, subprocess, tempfile, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(ROOT, *a)
LITHO = 'research/sources/izhar-al-asrar-matn-lithograph.txt'
TAFS = 'research/sources/izhar-sual-cevap-tafsilatli.txt'
PKG = 'izhar-al-asrar'
OUT = P('content/rules/izhar_map.json')

HAR = re.compile(r'[ً-ْٰـ]')
def H(s): return HAR.sub('', s or '')
def N(s):   # letters only, for matching the unvowelled print against the package
    s = H(s); s = re.sub('[أإآٱ]', 'ا', s); s = s.replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'[^ء-ي ]', ' ', s)
def words(s): return [w for w in N(s).split() if w]

# ── the specs: what an authored line must say for a token to illustrate the item (a), the word itself (w, optional),
#    and what the engine's line must say (e). Regexes on the line with the ḥarakāt stripped.
INNA = '(إن|أن|كأن|لكن|ليت|لعل)'
KANA = '(كان|ليس|صار|أصبح|أمسى|أضحى|ظل|بات|زال|دام|برح|فتئ|انفك|يكون|تكون|يكن|تكن|كانت|كانوا)'
def J(x): return f'مجرور ب«?{x}»?([ ،.]|$)'
SPEC = {
 'I-A01': dict(a='^الباء حرف جر', e='مجرور'), 'I-A02': dict(a=J('من'), e='مجرور'), 'I-A03': dict(a=J('إلى'), e='مجرور'),
 'I-A04': dict(a=J('عن'), e='مجرور'), 'I-A05': dict(a=J('على'), e='مجرور'), 'I-A06': dict(a='^اللام حرف جر', e='مجرور'),
 'I-A07': dict(a=J('في'), e='مجرور'), 'I-A08': dict(a='^الكاف حرف (جر|تشبيه)', e='مجرور'), 'I-A09': dict(a=J('حتى'), e='في محل جر|مجرور'),   # (v353-I) on the letter the engine says «فِي مَحَلِّ جَرٍّ بِهِ» of the maṣdar: the old test wanted «مجرور»
 'I-A10': dict(a=J('رب'), e='مجرور'), 'I-A11': dict(a='^الواو (حرف جر وقسم|حرف قسم|واو القسم)', e='قسم'),
 'I-A12': dict(a='^التاء (حرف جر وقسم|حرف قسم|تاء القسم)', e='قسم'), 'I-A13': dict(a=J('حاشا'), e='مجرور'),
 'I-A14': dict(a=J('مذ'), e='مجرور'), 'I-A15': dict(a=J('منذ'), e='مجرور'), 'I-A16': dict(a=J('خلا'), e='مجرور'),
 'I-A17': dict(a=J('عدا'), e='مجرور'), 'I-A18': dict(a=J('لولا'), e='مجرور'), 'I-A19': dict(a=J('كي'), e='مجرور'),
 'I-A20': dict(a=J('لعل'), e='مجرور'),
 'I-A21': dict(a='^اسم «?إن»? منصوب', e='اسم «?إن'), 'I-A22': dict(a='^اسم «?أن»? منصوب', e='اسم «?أن'),
 'I-A23': dict(a='^اسم «?كأن»? منصوب', e='اسم «?كأن'), 'I-A24': dict(a='^اسم «?لكن»? منصوب', e='اسم «?لكن'),
 'I-A25': dict(a='^اسم «?ليت»? منصوب', e='اسم «?ليت'), 'I-A26': dict(a='^اسم «?لعل»? منصوب', e='اسم «?لعل'),
 'I-A27': dict(a='^اسم «?لا»? (النافية للجنس|مبني)', e='اسم «?لا'), 'I-A28': dict(a='مخففة من الثقيلة', e='مخففة'),
 'I-A29': dict(a='^(اسم|خبر) «?ما»? (العاملة|المشبهة|الحجازية)', e='«?ما»?'),
 'I-A30': dict(a='^(اسم|خبر) «?لا»? (العاملة عمل ليس|المشبهة)', e='«?لا»?'),
 'I-A31': dict(a='^فعل مضارع منصوب ب«?أن»?([ ،.]|$)', e='منصوب'), 'I-A32': dict(a='منصوب ب«?لن»?', e='منصوب'),
 'I-A33': dict(a='منصوب ب«?كي»?|بأن مضمرة بعد (لام )?كي', e='منصوب'), 'I-A34': dict(a='منصوب ب«?إذن»?', e='منصوب'),
 'I-A35': dict(a='مجزوم ب«?لم»?([ ،.]|$)', e='مجزوم'), 'I-A36': dict(a='مجزوم ب«?لما»?', e='مجزوم'),
 'I-A37': dict(a='مجزوم ب(لام الأمر|اللام)', e='مجزوم'), 'I-A38': dict(a='مجزوم ب«?لا»? (الناهية|النهي)', e='مجزوم'),
 'I-A39': dict(a='مجزوم ب«?إن»?', e='مجزوم'),
 'I-A40': dict(a='شرط', w='^(ف|و)?حيثما$', e='شرط'), 'I-A41': dict(a='شرط', w='^(ف|و)?أينما?$', e='شرط'),
 'I-A42': dict(a='شرط', w='^(ف|و)?أنى$', e='شرط'), 'I-A43': dict(a='شرط', w='^(ف|و)?إذما$', e='شرط'),
 'I-A44': dict(a='شرط جازم', w='^(ف|و)?إذا$', e='شرط'), 'I-A45': dict(a='شرط', w='^(ف|و)?متى$', e='شرط'),
 'I-A46': dict(a='شرط', w='^(ف|و)?مهما$', e='شرط'), 'I-A47': dict(a='شرط جازم', w='^(ف|و)?ما$', e='شرط'),
 'I-A48': dict(a='شرط', w='^(ف|و)?أي(ا|ه|هم)?$', e='شرط'), 'I-A49': dict(a='شرط جازم', w='^(ف|و)?من$', e='شرط'),
 'I-A50': dict(a='^مفعول به منصوب', e='مفعول به'), 'I-A51': dict(a='لاسم الفاعل', e='لاسم الفاعل|مفعول به|فاعل'),
 'I-A52': dict(a='لاسم المفعول', e='نائب فاعل|لاسم المفعول'), 'I-A53': dict(a='للصفة المشبهة', e='فاعل|تمييز|شبيه بالمفعول'),
 'I-A54': dict(a='اسم تفضيل', e='تفضيل'), 'I-A55': dict(a='(فاعل|مفعول به) (لل|ب)مصدر', e='مفعول به|فاعل|مضاف إليه'),
 'I-A56': dict(a='^مضاف إليه مجرور', e='مضاف إليه'), 'I-A57': dict(a='^تمييز منصوب', e='تمييز'),
 'I-A58': dict(a='^اسم فعل', e='اسم فعل'), 'I-A59': dict(a='^مبتدأ مرفوع', e='مبتدأ'),
 'I-A60': dict(a='^فعل مضارع مرفوع', e='مرفوع'),
 'I-B01': dict(a='^فاعل مرفوع', e='فاعل'), 'I-B02': dict(a='^نائب (ال)?فاعل', e='نائب فاعل'), 'I-B03': dict(a='^مبتدأ', e='مبتدأ'),
# (v353-I) I-B04: the line must open with the doer — «ذُلُلٌ رِكَابِي» names it only as the Kufan's aside
 'I-B04': dict(a='^(نائب )?فاعل[^—(]*سد مسد الخبر', e='سد مسد الخبر'), 'I-B05': dict(a='^خبر (المبتدأ )?مرفوع|^خبر المبتدأ', e='خبر'),
 'I-B06': dict(a=f'^خبر «?{INNA}»?([ ،.]|$)', e='خبر'), 'I-B07': dict(a=f'^اسم «?{KANA}»?([ ،.]|$)', e='اسم'),
 'I-B08': dict(a='^اسم «?(ما|لا)»? (العاملة|المشبهة|الحجازية)', e='اسم'), 'I-B09': dict(a='^خبر «?لا»?([ ،.]|$)', e='خبر'),
 'I-B10': dict(a='^مفعول مطلق', e='مفعول مطلق'), 'I-B11': dict(a='^مفعول به', e='مفعول به'),
 'I-B12': dict(a='^(مفعول فيه|ظرف (زمان|مكان))', e='ظرف|مفعول فيه'), 'I-B13': dict(a='^مفعول (له|لأجله)', e='مفعول (له|لأجله)'),
 'I-B14': dict(a='^مفعول معه', e='مفعول معه'), 'I-B15': dict(a='^حال ', e='حال'), 'I-B16': dict(a='^تمييز', e='تمييز'),
 'I-B17': dict(a='^مستثنى', e='مستثنى'), 'I-B18': dict(a=f'^خبر «?{KANA}»?([ ،.]|$)', e='خبر'),
 'I-B19': dict(a=f'^اسم «?{INNA}»?([ ،.]|$)', e='اسم'), 'I-B20': dict(a='^اسم «?لا»? (النافية للجنس|مبني)', e='اسم «?لا'),
 'I-B21': dict(a='^خبر «?(ما|لا)»? (العاملة|المشبهة|الحجازية)', e='خبر'), 'I-B22': dict(a='^فعل مضارع منصوب', e='منصوب'),
 'I-B23': dict(a='^(اسم )?مجرور ب', e='مجرور'), 'I-B24': dict(a='^مضاف إليه', e='مضاف إليه'),
 'I-B25': dict(a='^فعل مضارع مجزوم', e='مجزوم'), 'I-B26': dict(a='^(نعت|صفة) ', e='نعت|صفة'),
 'I-B27': dict(a='^((الواو|الفاء) عاطفة، و)?معطوف', e='معطوف'), 'I-B28': dict(a='^(توكيد|تأكيد)', e='توكيد|تأكيد'),
 'I-B29': dict(a='^بدل', e='بدل'), 'I-B30': dict(a='^عطف بيان', e='عطف بيان'),
 'I-C01': dict(a='مرفوع (بالضمة|وعلامة رفعه الضمة)', e='الضمة'), 'I-C02': dict(a='منصوب (بالفتحة|وعلامة نصبه الفتحة)', e='الفتحة'),
 'I-C03': dict(a='مجرور (بالكسرة|وعلامة جره الكسرة)', e='الكسرة'), 'I-C04': dict(a='مرفوع (بالواو|وعلامة رفعه الواو)', e='الواو'),
 'I-C05': dict(a='مرفوع (بالألف|وعلامة رفعه الألف)', e='الألف'), 'I-C06': dict(a='(منصوب|مجرور) (بالياء|وعلامة (نصبه|جره) الياء)', e='الياء'),
 'I-C07': dict(a='ثبوت النون', e='ثبوت النون'), 'I-C08': dict(a='مجزوم (بالسكون|وعلامة جزمه السكون)', e='السكون'),
 'I-C09': dict(a='مجزوم (بحذف حرف العلة|وعلامة جزمه حذف حرف العلة|بحذف (الواو|الياء|الألف))', e='حذف (حرف العلة|الواو|الياء|الألف)'),
 'I-C10': dict(a='(مجزوم|منصوب) (بحذف النون|وعلامة (جزمه|نصبه) حذف النون)', e='حذف النون'),
}
# the suʾāl–cevap question(s) that treat each item (by the file's own numbering)
def rng(a, b, q): return {f'I-A{i:02d}': q for i in range(a, b + 1)}
TRQ = {**rng(1, 20, [9]), **rng(21, 26, [18, 19]), 'I-A27': [24], 'I-A28': [23], 'I-A29': [24], 'I-A30': [24], **rng(31, 33, [25]),
       'I-A34': [26], **rng(35, 49, [25]), 'I-A50': [28, 30], 'I-A51': [35], 'I-A52': [35], 'I-A53': [36], 'I-A54': [37], 'I-A55': [39],
       'I-A56': [40, 41], 'I-A57': [43, 44], 'I-A58': [45], 'I-A59': [46], 'I-A60': [46, 6],
       'I-B01': [53], 'I-B02': [53], 'I-B03': [62], 'I-B04': [62], 'I-B05': [63], 'I-B06': [64], 'I-B07': [64], 'I-B08': [64], 'I-B09': [64],
       'I-B10': [65], 'I-B11': [65], 'I-B12': [66], 'I-B13': [66], 'I-B14': [66], 'I-B15': [67], 'I-B16': [68], 'I-B17': [69, 70],
       'I-B22': [25], 'I-B23': [11], 'I-B24': [41, 42], 'I-B25': [25, 73], 'I-B26': [74], 'I-B27': [79], 'I-B28': [80], 'I-B29': [81], 'I-B30': [81],
       **{f'I-C{i:02d}': [83, 85] for i in range(1, 11)}}
# (v353-I) the book's OWN example for the cells no corpus token fills: the package token of the matn's example (the word the exercise marks),
# the engine line that must name it for the exercise to run on it (None: shown, never exercised — the token is not the unit's reading), and why.
BOOK = {
 'I-A14': ('izhar-al-asrar:5:s4:26', 'في محل جر|مجرور', 'مَا رَأَيْتُهُ مُذْ أَنَّكَ قَائِمٌ — the maṣdar of أَنَّ in jarr by مُذْ'),
 'I-A17': ('izhar-al-asrar:22:s10:23', None, 'جَاءَنِي الْقَوْمُ عَدَا … زَيْدًا — the book\'s عَدَا as a verb («وَيَكُونَانِ فِعْلَيْنِ وَهُوَ الْأَكْثَرُ»); not the jarr reading'),
 'I-A18': ('izhar-al-asrar:2:s5:9', 'مجرور', 'لَوْلَاكَ لَهَلَكَ زَيْدٌ — the pronoun in jarr by لَوْلَا'),
 'I-A19': ('izhar-al-asrar:2:s7:15', 'مجرور', 'كَيْمَهْ عَصَيْتَ — the interrogative mā in jarr by كَيْ'),
 'I-A20': ('izhar-al-asrar:2:s5:13', 'مجرور', 'لَعَلَّ زَيْدٍ قَائِمٌ — جَرٌّ in the dialect of ʿUqayl'),
 'I-A30': ('izhar-al-asrar:6:s4:31', 'اسم «?لا', 'وَلَا رَجُلٌ حَاضِرًا — the ism of lā like laysa'),
 'I-A34': ('izhar-al-asrar:7:s4:14', None, 'إِذَنْ أَظُنُّكَ كَاذِبًا — the book\'s example of إِذَنْ NOT governing (the verb is for the present)'),
 'I-B14': ('izhar-al-asrar:35:s1:13', 'مفعول معه', 'جِئْتُ وَزَيْدًا'),
}
BOOK_NONE = ['I-A13', 'I-A16', 'I-A33', 'I-A40', 'I-A41', 'I-A42', 'I-A43', 'I-A44']   # the matn names them in its lists and gives no example of use
GAMES = {}
for i in range(1, 21): GAMES[f'I-A{i:02d}'] = ['gCase', 'gShop']
for i in range(21, 27): GAMES[f'I-A{i:02d}'] = ['gRole', 'gInna']
for i in range(27, 31): GAMES[f'I-A{i:02d}'] = ['gRole']
for i in range(31, 35): GAMES[f'I-A{i:02d}'] = ['gCase']
for i in range(35, 50): GAMES[f'I-A{i:02d}'] = ['gShart', 'gCase']
for i in range(50, 59): GAMES[f'I-A{i:02d}'] = ['gRole', 'gDuel', 'gTahlil']
GAMES['I-A59'] = GAMES['I-A60'] = ['gRole', 'gCase']
for i in range(1, 31): GAMES[f'I-B{i:02d}'] = ['gRole', 'gDuel', 'gTahlil']
for k in ('I-B22', 'I-B25'): GAMES[k] = ['gCase', 'gShart']
for k in ('I-B23', 'I-B24'): GAMES[k] = ['gCase', 'gShop']
for i in range(1, 11): GAMES[f'I-C{i:02d}'] = ['gSign', 'gHarakat', 'gCase']
NOTE_MORE = {   # the role's own notes where the ledger names none (ids verified against content/grammar at build)
    **{f'I-A{i:02d}': ['al-majzum-wal-shart-wal-jaza', 'in-shartiyya'] for i in range(40, 50)}, 'I-A51': ['ism-fail', 'shurut-amal-ism-al-fail'],
    'I-A52': ['ism-maful', 'ism-al-fail-wal-maful-fil-kafiya'], 'I-A53': ['sifa-mushabbaha', 'al-sifa-al-mushabbaha-fil-kafiya'],
    'I-A59': ['mubtada-khabar', 'al-mubtada-wa-nawah'], 'I-A60': ['mudari-marfu'], 'I-B01': ['fail', 'al-marfuat-al-fail-wa-naibuh'],
    'I-B02': ['naib-al-fail', 'al-marfuat-al-fail-wa-naibuh'], 'I-B06': ['inna-wa-akhawatuha'], 'I-B09': ['la-nafiya-lil-jins'],
    'I-B10': ['maful-mutlaq', 'al-mansubat-al-maful-al-mutlaq'], 'I-B11': ['maful-bihi', 'al-maful-bihi-wa-qismah'], 'I-B14': ['maful-maah'],
    'I-B16': ['tamyiz', 'al-tamyiz-wa-ahkamuh'], 'I-B22': ['nawasib-wa-jawazim-al-mudari'], 'I-B23': ['huruf-jarr', 'al-majrur-bil-harf-wa-bil-idafa'],
    'I-B24': ['al-majrur-bil-harf-wa-bil-idafa', 'al-mudaf-wa-nawa-al-idafa'], 'I-B28': ['tawkid', 'al-tawkid-al-lafzi-wal-manawi'],
    'I-B29': ['badal', 'al-badal-wa-aqsamuh-wa-atf-al-bayan'], 'I-B05': ['khabar-al-mubtada-wa-ahkamuh'], 'I-B03': ['mubtada-khabar'],
    'I-B15': ['hal'], 'I-B17': [], 'I-B07': ['kana-wa-akhawatuha'], 'I-B18': ['kana-wa-akhawatuha'], 'I-B19': ['inna-wa-akhawatuha'],
    'I-B20': ['la-nafiya-lil-jins'], 'I-B08': ['ma-la-mushabbaha'], 'I-B21': ['ma-la-mushabbaha'], 'I-B12': ['maful-fih'], 'I-B13': ['maful-lah'],
}
TOPIC = {**{f'I-A{i:02d}': 'jarr' for i in range(1, 21)}, 'I-A11': 'qasam', 'I-A12': 'qasam', **{f'I-A{i:02d}': 'inna' for i in range(21, 27)},
         'I-A27': 'la-jins', 'I-A29': 'ma-laysa', 'I-A30': 'ma-laysa', **{f'I-A{i:02d}': 'jazm' for i in range(35, 50)}, 'I-A50': 'maful-bih',
         'I-A56': 'idafa', 'I-A57': 'tamyiz', 'I-A59': 'mubtada', 'I-B01': 'fail', 'I-B02': 'fail', 'I-B03': 'mubtada', 'I-B05': 'khabar',
         'I-B06': 'inna', 'I-B07': 'kana', 'I-B08': 'ma-laysa', 'I-B09': 'la-jins', 'I-B11': 'maful-bih', 'I-B14': 'maful-maah', 'I-B15': 'hal',
         'I-B16': 'tamyiz', 'I-B18': 'kana', 'I-B19': 'inna', 'I-B20': 'la-jins', 'I-B21': 'ma-laysa', 'I-B23': 'jarr', 'I-B24': 'idafa',
         'I-B25': 'jazm', 'I-B26': 'naat', 'I-B27': 'atf', 'I-C04': 'signs-dual-plural', 'I-C05': 'signs-dual-plural', 'I-C06': 'signs-dual-plural',
         'I-C07': 'irab-fil', 'I-C10': 'irab-fil', 'I-C08': 'jazm', 'I-C09': 'muqaddar'}
# the writer's rules: the book's said / not-said examples (lithograph line, the matn's words, said?)
WRITER = [
 ('I-19.2', 19, 'مررت بزيد بعمرو', False), ('I-19.2', 19, 'ضربت يوم الجمعة يوم السبت', False),
 ('I-19.2', 19, 'ضربت يوم الجمعة أمام المسجد', True), ('I-19.2', 19, 'أكلت من ثمره من تفاحه', True),
 ('I-17.2', 17, 'صليت دارا', False), ('I-17.2', 17, 'كنت جانب الدار', False),
 ('I-33.2', 33, 'قائما ما زال زيد', False),
 ('I-15.3', 15, 'بزيد مررت', True), ('I-80.0', 80, 'مر بزيد', True), ('I-107.2', 107, 'إن في الدار رجلا', True),
 ('I-128.0', 128, 'أنا زيدا غير ضارب', True), ('I-146.3', 146, 'ضربت أنا وزيد', True), ('I-146.3', 146, 'ضربت اليوم وزيد', True),
 ('I-146.3', 146, 'مررت بك وبزيد', True), ('I-149.0', 149, 'ضرب زيد عمرا وبكر خالدا', True),
 ('I-98.1', 98, 'المسلمون جاؤوا', True), ('I-131.1', 131, 'إن ضربت ضربت', True),
]

def litho():
    return open(P(LITHO), encoding='utf-8').read().split('\n')

def package():
    sens = []
    for f in glob.glob(P('content/samples', PKG, 'chapters', '*.json')):
        c = json.load(open(f, encoding='utf-8'))
        for s in c['sentences']:
            toks = [t['surface']['full'] for t in s['tokens']]
            sens.append(dict(ch=c['chapter'], sid=s['id'], toks=toks, w=[' '.join(words(t)) for t in toks]))
    sens.sort(key=lambda s: (s['ch'], int(re.sub(r'\D', '', s['sid']) or 0)))
    return sens

def find_span(sens, phrase):
    """the matn's words as the package vowels them: the first sentence holding the phrase's words in order (by letters)."""
    pw = words(phrase)
    for s in sens:
        flat = []
        for i, w in enumerate(s['w']):
            for x in w.split(): flat.append((x, i))
        for a in range(len(flat) - len(pw) + 1):
            if all((flat[a + k][0] == pw[k]) or (k == 0 and pw[k] in V(flat[a][0])) for k in range(len(pw))):
                i0, i1 = flat[a][1], flat[a + len(pw) - 1][1]
                # the span's words must be the phrase's words (a proclitic waw/fa outside the phrase is dropped by letter match)
                return dict(ch=s['ch'], sid=s['sid'], from_=i0, to=i1, ar=' '.join(s['toks'][i0:i1 + 1]))
    return None

def V(w):   # a word and its forms without a proclitic (وَمِنْ → من, بِزَيْدٍ → زيد, وَالْبَاءُ → الباء)
    out = {w}
    if len(w) > 2 and w[0] in 'وفبلك': out.add(w[1:])
    if len(w) > 3 and w[:2] in ('وب', 'ول', 'فب', 'فل', 'وك'): out.add(w[2:])
    return out

ANCHOR = {   # where the ledger line's best overlap is not the item's own sentence: (chapter, sentence, the item's word as printed)
    'I-A05': (1, 's18', 'وعلى'), 'I-A07': (1, 's19', 'وفي'), 'I-A12': (1, 's19', 'وتاؤه'), 'I-A22': (4, 's3', 'وأن'),
    'I-A28': (5, 's7', 'المفتوحة'), 'I-A29': (6, 's3', 'ما'), 'I-A30': (6, 's3', 'ولا'), 'I-A31': (7, 's2', 'أن'),
    'I-A33': (7, 's2', 'وكي'), 'I-A34': (7, 's2', 'وإذن'), 'I-A35': (7, 's6', 'لم'), 'I-A36': (7, 's6', 'ولما'),
    'I-A37': (7, 's6', 'ولام'), 'I-A38': (7, 's6', 'ولا'), 'I-A39': (7, 's7', 'إن'), 'I-A53': (12, 's8', 'الصفة'),
    'I-A59': (17, 's2', 'التجرد'), 'I-A60': (17, 's4', 'تجرد'), 'I-B01': (21, 's3', 'الفاعل'), 'I-B05': (29, 's1', 'خبر'),
    'I-B11': (33, 's1', 'المفعول'), 'I-B14': (35, 's1', 'المفعول'), 'I-B20': (40, 's4', 'اسم'), 'I-B25': (43, 's1', 'المجزوم'),
    'I-C07': (54, 's4', 'بالنون'), 'I-C08': (52, 's5', 'الحركة'), 'I-C09': (52, 's5', 'الآخر'), 'I-C10': (52, 's5', 'النون'),
}

def best_sentence(sens, line_ar, item, anchor=None):
    iw = [w for w in words(item) if w not in ('لغه', 'عقيل')]
    if anchor:
        ch, sid, word = anchor
        s = next(x for x in sens if x['ch'] == ch and x['sid'] == sid); ww = ' '.join(words(word))
        hi = next((i for i, w in enumerate(s['w']) if w == ww), None)
        return dict(ch=s['ch'], sid=s['sid'], ar=' '.join(s['toks']), hi=hi, prec=1.0)
    lw = set(); [lw.update(V(w)) for w in words(line_ar)]
    best = None
    for s in sens:
        sw = [x for w in s['w'] for x in w.split()]
        if not sw: continue
        ov = sum(1 for x in sw if V(x) & lw)
        prec = ov / len(sw)
        has = bool(iw) and all(any(y in V(x) for x in sw) for y in iw)
        sc = (has, round(prec, 2) >= 0.6, ov)
        if best is None or sc > best[0]: best = (sc, s)
    if not best or best[0][2] < 3: return None
    s = best[1]; hi = None
    for i, w in enumerate(s['w']):
        if iw and any(iw[0] in V(x) for x in w.split()): hi = i; break
    return dict(ch=s['ch'], sid=s['sid'], ar=' '.join(s['toks']), hi=hi, prec=best[0][1])

MOJ = re.compile(r'[؀-ۿݐ-ݿﭐ-﻿‎‏‪-‮ً-ٟ]|O{2,}|[\]\[`^_|{}~¹£µ×<>¸]')
def clean_tr(line):
    line = line.replace('Đ', 'İ').replace('đ', 'ı')
    out = []
    for t in line.split():
        bad = bool(MOJ.search(t)) or '$' in t or '*' in t or bool(re.fullmatch(r'[A-Z][:;.,]?', t)) or bool(re.search(r'\d', t) and re.search(r'[A-Za-z]', t) and not re.match(r'^\d+[-.)]', t))
        if bad:
            if not out or out[-1] != '…': out.append('…')
        else: out.append(t)
    s = ' '.join(out).strip()
    s = re.sub(r'…(\s*[:;,.()]*\s*…)+', '…', s); s = re.sub(r'\s+([:;,.)])', r'\1', s)
    return '' if re.fullmatch(r'[… .,:;()"*-]*', s) else s

def tr_units():
    L = open(P(TAFS), encoding='utf-8').read().split('\n')
    start = next(i for i, l in enumerate(L) if l.startswith('-----')) + 1
    units, cur, expect = {}, None, 1
    for i in range(start, len(L)):
        l = L[i]
        m = re.match(r'^\s*(\d+)\s*([-–]|\s)', l)
        if m and int(m.group(1)) == expect:
            cur = expect; expect += 1; units[cur] = dict(q=clean_tr(re.sub(r'^\s*\d+\s*[-–]?\s*', '', l)), line=i + 1, a=[]); continue
        if cur is None: continue
        if re.search(r'Sadakat Medresesi|Tafsilatl[ıi] (Đ|İ)ZHAR|^\s*\d+\s*$|MAMÜL BAHS|İRAB BAHS|ĐRAB BAHS', l): continue
        c = clean_tr(l)
        if c: units[cur]['a'].append(c)
    for k, u in units.items():
        txt = ' '.join(u['a'])
        if len(txt) > 1400: txt = txt[:1400].rsplit(' ', 1)[0] + ' …'
        u['a'] = txt; u['end'] = None
    return units

def note_index():
    by_sen, ids = collections.defaultdict(set), set()
    for f in glob.glob(P('content/grammar', '*.json')):
        d = json.load(open(f, encoding='utf-8')); ids.add(d['id'])
        for e in d.get('examples', []) or []:
            if e.get('sourceStory') == PKG and e.get('sentence'):
                by_sen[(str(e.get('chapter', '')), e['sentence'])].add(d['id']); by_sen[('', e['sentence'])].add(d['id'])
    return by_sen, ids

def corpus_tokens():
    out = []
    for man in sorted(glob.glob(P('content/samples', '*', 'manifest.json'))):
        d = os.path.dirname(man); m = json.load(open(man, encoding='utf-8')); pid = m['id']; lvl = m.get('level') or 9
        for f in glob.glob(d + '/chapters/*.json'):
            c = json.load(open(f, encoding='utf-8')); ch = c.get('chapter')
            for s in c['sentences']:
                T = s['tokens']
                for i, t in enumerate(T):
                    ar = H((t.get('irab') or {}).get('ar', ''))
                    if ar: out.append((f'{pid}:{ch}:{s["id"]}:{i + 1}', pid, lvl, len(T), H(t['surface']['full']), ar))
    return out

def candidates(toks):
    C = {}
    for iid, sp in SPEC.items():
        a = re.compile(sp['a']); w = re.compile(sp['w']) if sp.get('w') else None
        hits = [t for t in toks if a.search(t[5]) and (not w or w.search(re.sub('[أإآ]', lambda m: m.group(0), t[4])))]
        # short sentences of the lower levels first, one story after another (no story twice before every story once)
        hits.sort(key=lambda t: (t[3] < 3 or t[3] > 14, t[2], t[3], t[0]))
        by, order = collections.OrderedDict(), []
        for t in hits: by.setdefault(t[1], []).append(t)
        rnd = 0
        while len(order) < 40 and any(len(v) > rnd for v in by.values()):
            for v in by.values():
                if len(v) > rnd: order.append(v[rnd])
            rnd += 1
        C[iid] = dict(n=len(hits), c=[t[0] for t in order[:40]])
    return C

def main():
    led = json.load(open(P('content/rules/coverage_izhar.json'), encoding='utf-8'))['entries']
    LI = litho(); sens = package(); units = tr_units(); nby, nids = note_index()
    EN = json.load(open(P('content/rules/izhar_course_en.json'), encoding='utf-8'))['q']   # our renderings of the questions, pending review
    ilal = json.load(open(P('content/rules/ilal.json'), encoding='utf-8'))['reasons']
    # (v353-I) the owner's own Turkish translation, joined per item by tools/ledger/izhar_tercume.py (meaning, its example, the source lines)
    tp = P('content/rules/izhar_tercume.json')
    TC = {u['id']: u for u in json.load(open(tp, encoding='utf-8'))['units']} if os.path.exists(tp) else {}
    toks = corpus_tokens(); C = candidates(toks)
    probe = {}
    if '--no-probe' not in sys.argv:
        cands = [dict(id=i, k=k, e=SPEC[i]['e']) for i, v in C.items() for k in v['c']] + [dict(id='BOOK:' + i, k=b[0], e=b[1] or '^$') for i, b in BOOK.items()]
        with tempfile.TemporaryDirectory() as td:
            ip, op = os.path.join(td, 'c.json'), os.path.join(td, 'o.json')
            json.dump(cands, open(ip, 'w'), ensure_ascii=False)
            subprocess.run(['node', P('tools/ledger/izhar_course_probe.js'), ip, op], check=True, cwd=ROOT)
            for r in json.load(open(op)): probe[(r['id'], r['k'])] = r
    items = []
    for r in led:
        if r['kind'] not in ('amil', 'mamul', 'irab'): continue
        iid = r['id']; ln = r['line']
        bab = {'amil': 1, 'mamul': 2, 'irab': 3}[r['kind']]
        n = int(iid[3:])
        group = ('samai' if n <= 49 else 'qiyasi' if n <= 58 else 'manawi') if bab == 1 else None
        bs = best_sentence(sens, r['ar'], r['item'], ANCHOR.get(iid))
        engine = [c[7:] for c in r.get('carried_by', []) if c.startswith('engine:')]
        notes = [c[5:] for c in r.get('carried_by', []) if c.startswith('note:') and c[5:] in nids]
        if bs:
            for g in sorted(nby.get((str(bs['ch']), bs['sid']), set()) | set()):
                if g not in notes: notes.append(g)
        for g in NOTE_MORE.get(iid, []):
            if g in nids and g not in notes: notes.append(g)
        trq = [q for q in TRQ.get(iid, []) if q in units]
        tr = [dict(q=q, line=units[q]['line'], ask=units[q]['q'], ans=units[q]['a'], en=EN.get(str(q))) for q in trq]
        ex = [probe.get((iid, k)) for k in C[iid]['c']]
        good = [x for x in ex if x and x['ok']]
        good.sort(key=lambda x: -min(x.get('n', 0), 4))
        seen, exs = set(), []
        for x in good:
            p = x['k'].split(':')[0]
            if p in seen: continue
            seen.add(p); exs.append(x['k'])
            if len(exs) == 3: break
        pool = [x['k'] for x in good[:12]]
        bk = None
        if iid in BOOK and not exs:
            pb = probe.get(('BOOK:' + iid, BOOK[iid][0])) or {}
            bk = dict(k=BOOK[iid][0], ok=bool(BOOK[iid][1] and pb.get('ok')), why=BOOK[iid][2], eng=pb.get('eng'))
        top = TOPIC.get(iid)
        il = [x['id'] for x in ilal if top and x.get('topic') == top][:3]
        items.append(dict(id=iid, bab=bab, group=group, item=r['item'], status=r['status'],
            matn=dict(file=LITHO, line=ln, text=LI[ln - 1].strip() if 0 < ln <= len(LI) else r['ar'], ledger=r['ar']),
            pkg=dict(ch=bs['ch'], sid=bs['sid'], ar=bs['ar'], hi=bs['hi']) if bs else None,
            tr=tr, engine=engine, notes=notes, games=GAMES.get(iid, []),
            spec=dict(a=SPEC[iid]['a'], e=SPEC[iid]['e'], w=SPEC[iid].get('w')), authored=C[iid]['n'],
            checked=sum(1 for x in ex if x), agreeing=len(good), examples=exs, pool=pool, ilal=il, book=bk,
            tc=(lambda u: dict(m=u['meaning_tr'], en=u.get('en'), lines=u['meaning_lines'] + (u['example_lines'] if u.get('example') else []), ex=dict(u['example'], tr=u['example_tr']) if u.get('example') else None)
                if u and u.get('meaning_tr') else None)(TC.get(iid)),
            no_example=iid in BOOK_NONE and not exs))
    writer = []
    for rid, ln, ph, said in WRITER:
        sp = find_span(sens, ph)
        writer.append(dict(rule=rid, line=ln, matn=LI[ln - 1].strip(), phrase=ph, said=said,
                           ar=sp['ar'] if sp else ph, vowelled=bool(sp), at=dict(ch=sp['ch'], sid=sp['sid']) if sp else None))
    cnt = lambda f: sum(1 for x in items if f(x))
    counts = {}
    for b, nm, tot in ((1, 'amil', 60), (2, 'mamul', 30), (3, 'irab', 10)):
        B = [x for x in items if x['bab'] == b]
        counts[nm] = dict(total=len(B), book=tot, matn=sum(1 for x in B if x['matn']['text']), pkg=sum(1 for x in B if x['pkg']),
                          tr=sum(1 for x in B if x['tr'] or x['tc']), tr_sc=sum(1 for x in B if x['tr']), tercume=sum(1 for x in B if x['tc']), tercume_ex=sum(1 for x in B if x['tc'] and x['tc']['ex']), engine=sum(1 for x in B if x['engine']), notes=sum(1 for x in B if x['notes']),
                          games=sum(1 for x in B if x['games']), examples=sum(1 for x in B if x['examples']),
                          examples3=sum(1 for x in B if len(x['examples']) >= 3), ilal=sum(1 for x in B if x['ilal']),
                          complete=sum(1 for x in B if x['matn']['text'] and x['pkg'] and (x['tr'] or x['tc']) and x['engine'] and x['notes'] and x['games'] and (x['examples'] or x['book'])),
                          book_example=sum(1 for x in B if x['book']), book_ex=sum(1 for x in B if x['book'] and x['book']['ok']))
    has = lambda x, k: x[k] or (k == 'examples' and x['book']) or (k == 'tr' and x['tc'])
    missing = [dict(id=x['id'], item=x['item'], lacks=[k for k in ('pkg', 'tr', 'engine', 'notes', 'games', 'examples') if not has(x, k)])
               for x in items if not all(has(x, k) for k in ('pkg', 'tr', 'engine', 'notes', 'games', 'examples'))]
    out = dict(book='Iẓhār al-Asrār (Birgivī)', built_by='tools/ledger/izhar_course_map.py', ledger='content/rules/coverage_izhar.json',
               sources=dict(matn=LITHO, tr=TAFS, package='content/samples/' + PKG, ilal='content/rules/ilal.json'),
               tr_note='the suʾāl–cevap file is a PDF extraction: its Arabic runs are mojibake and are elided as «…»; Đ/đ (the extraction’s İ/ı) restored; otherwise verbatim',
               counts=counts, missing=missing, items=items, writer=writer)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(counts, ensure_ascii=False)); print('missing', len(missing), [(m['id'], m['lacks']) for m in missing][:60])
    print('writer', len(writer), 'vowelled', sum(1 for w in writer if w['vowelled']))

def render(out):
    """research/izhar-course-2026-11-27.md: the map's coverage table and, unit by unit, what it has and lacks."""
    c = out['counts']; L = ['# The Iẓhār course — coverage by the book\'s own count (v351-I, 2026-11-27)', '',
        'Built by `tools/ledger/izhar_course_map.py` → `content/rules/izhar_map.json` (the course page reads it through the Iẓhār story\'s',
        'body). A cell is **complete** when the item has its package sentence, a suʾāl–cevap unit, an engine rule, a note, a game and at least',
        'one corpus example whose authored line and engine line both name it. The lithograph line is present for every item.', '',
        '| bāb | book | items | package line | suʾāl–cevap | engine | note | game | ≥ 1 example | ≥ 3 examples | ʿilal reason | complete |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for k, nm in (('amil', '1 · ʿāmil'), ('mamul', '2 · maʿmūl'), ('irab', '3 · iʿrāb (signs)')):
        x = c[k]; L.append('| %s | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d | **%d** |' % (nm, x['book'], x['total'], x['pkg'], x['tr'], x['engine'], x['notes'], x['games'], x['examples'], x['examples3'], x['ilal'], x['complete']))
    L += ['', 'The ʿāmil split as the matn counts it: samāʿī %d · qiyāsī %d · maʿnawī %d.' % tuple(sum(1 for i in out['items'] if i['group'] == g) for g in ('samai', 'qiyasi', 'manawi')), '',
          '## The missing cells — the next work', '', '| id | item | lacks | why |', '|---|---|---|---|']
    for m in out['missing']:
        it = next(i for i in out['items'] if i['id'] == m['id'])
        why = []
        if 'examples' in m['lacks']: why.append('authored lines naming it: %d; engine agreeing: %d of %d checked' % (it['authored'], it['agreeing'], it['checked']) + ('; the matn names it in a list and gives no example of its use' if it.get('no_example') else ''))
        if 'tr' in m['lacks']: why.append('no question in the suʾāl–cevap')
        if 'engine' in m['lacks']: why.append('ledger status %s' % it['status'])
        L.append('| %s | %s | %s | %s |' % (m['id'], it['item'], ', '.join(m['lacks']), '; '.join(why)))
    L += ['', '## v353-I — the owner\'s translation and the book\'s own examples', '',
          'The «Anlamı / Meaning» card: the meaning in the owner\'s Turkish translation (`research/sources/izhar-tercume-full.txt`, joined by',
          '`tools/ledger/izhar_tercume.py` → `content/rules/izhar_tercume.json`, every string verbatim from its cited lines) — ʿāmil %d / 60, maʿmūl %d / 30,' % (c['amil']['tercume'], c['mamul']['tercume']),
          'signs %d / 10; an example is shown with it only where its broken Arabic equals a package token window as a bag of letters: %d.' % (c['irab']['tercume'], sum(c[k]['tercume_ex'] for k in c)),
          'The suʾāl–cevap cell of B18–B21 is the translation\'s line.', '',
          '| id | item | the book\'s own example (package token) | exercised? | why |', '|---|---|---|---|---|']
    for i in out['items']:
        if i.get('book'): L.append('| %s | %s | %s | %s | %s |' % (i['id'], i['item'], i['book']['k'], 'yes' if i['book']['ok'] else 'no — engine: ' + (i['book'].get('eng') or '')[:50], i['book']['why']))
    L += ['', '## Unit by unit', '', '| id | item | matn l. | story ch:s | Q | engine | notes | examples | exercise items |', '|---|---|---:|---|---|---|---:|---:|---:|']
    for i in out['items']:
        n_ex = len(set(i['examples']) | set(i['pool']))
        L.append('| %s | %s | %d | %s | %s | %s | %d | %d | %d |' % (i['id'], i['item'], i['matn']['line'], ('%s:%s' % (i['pkg']['ch'], i['pkg']['sid'])) if i['pkg'] else '—',
                 ', '.join(str(t['q']) for t in i['tr']) or '—', '; '.join(i['engine'])[:60].replace('|', '/') or '—', len(i['notes']), len(i['examples']), min(6, n_ex)))
    L += ['', '## «يُقَالُ / لَا يُقَالُ» — the writer\'s rules put to the learner', '', '| ledger row | matn l. | the book\'s example | said? | in the story |', '|---|---:|---|---|---|']
    for w in out['writer']:
        L.append('| %s | %d | %s | %s | %s |' % (w['rule'], w['line'], w['ar'], 'يُقَالُ' if w['said'] else 'لَا يُقَالُ', ('%s:%s' % (w['at']['ch'], w['at']['sid'])) if w['at'] else '—'))
    L += ['', 'The Turkish of the suʾāl–cevap is the source\'s (PDF extraction: its Arabic is mojibake and is elided «…»); the English of each',
          'question is ours (`content/rules/izhar_course_en.json`, marked «translation · pending review» in the page); the Turkish answers have',
          'no English rendering yet.', '']
    open(P('research', 'izhar-course-2026-11-27.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

if __name__ == '__main__':
    main()
    render(json.load(open(OUT, encoding='utf-8')))
