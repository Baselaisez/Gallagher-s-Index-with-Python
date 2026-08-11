// Build the GENERATED drill bank — hundreds of worked examples with their
// i'rab, their conjugation and their meaning, produced by driving the reader's
// own engines rather than by hand.
//
// Why generate rather than write? Two reasons, and both are the project's
// standing doctrine.
//
//   1. NEVER PUBLISH ARABIC WE ARE NOT SURE OF. Every item here is built by an
//      EXACT engine — AlamaEngine, IdafaEngine, sarfDerive, WaznEngine — from a
//      root or a lemma the corpus already carries and a human has already
//      checked. Nothing is invented; the forms are computed, and the explanation
//      is the engine's own step list, not a paraphrase of it.
//   2. AN UNMEASURED CHANGE IS A SUPERSTITION. Because the bank is a pure
//      function of the engines, it is also a GOLDEN FILE: the smoke suite
//      rebuilds it in-page and compares. Any future change to an engine that
//      moves a single cell shows up as a diff on a named item, with the rule
//      that produced it sitting next to the change.
//
// Usage:  node tools/gen_drills.js            (writes content/drills/generated.json)
//         node tools/gen_drills.js --check    (rebuild and diff; exit 1 on drift)
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright-core');

const ROOT = path.resolve(__dirname, '..');
const READER = path.join(ROOT, 'prototype/reader.html');
const OUT = path.join(ROOT, 'content/drills/generated.json');

function findChrome() {
  const c = [];
  if (process.env.CHROMIUM_PATH) c.push(process.env.CHROMIUM_PATH);
  c.push('/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
         '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome');
  for (const p of c) { try { if (p && fs.existsSync(p)) return p; } catch (e) {} }
  throw new Error('no Chromium found — set CHROMIUM_PATH');
}

// The material the bank is built from. Roots and lemmas are taken from words
// the corpus already carries, so nothing here is a word we invented.
const PLAN = {
  // seven ending-classes × three cases, and the hard rows on purpose
  nouns: [
    { w: 'كِتَاب',      root: 'ك ت ب', en: 'a book',            tr: 'kitap' },
    { w: 'الْكِتَاب',    root: 'ك ت ب', en: 'the book',          tr: 'kitap (marife)' },
    { w: 'مَسَاجِد',    root: 'س ج د', en: 'mosques',           tr: 'mescitler', mamnu: true },
    { w: 'فَتًى',       root: 'ف ت ي', en: 'a young man',       tr: 'delikanlı' },
    { w: 'الْفَتَى',     root: 'ف ت ي', en: 'the young man',     tr: 'delikanlı (marife)' },
    { w: 'مَعْنًى',      root: 'ع ن ي', en: 'a meaning',         tr: 'bir mana' },
    { w: 'قَاضِي',      root: 'ق ض ي', en: 'a judge',           tr: 'kadı' },
    { w: 'الْقَاضِي',    root: 'ق ض ي', en: 'the judge',         tr: 'kadı (marife)' },
    { w: 'مَعَانِي',     root: 'ع ن ي', en: 'meanings',          tr: 'manalar' },
    { w: 'خَفَاء',      root: 'خ ف ي', en: 'obscurity',         tr: 'hafâ' },
    { w: 'رَجَاء',      root: 'ر ج و', en: 'hope',              tr: 'recâ' },
    { w: 'صَحْرَاء',     root: 'ص ح ر', en: 'a desert',          tr: 'çöl' },
    { w: 'قُرَّاء',      root: 'ق ر أ', en: 'reciters',          tr: 'kāriler' },
    { w: 'مُسْلِمُونَ',   root: 'س ل م', en: 'Muslims',           tr: 'müslümanlar' },
    { w: 'مُجْتَهِدُونَ',  root: 'ج ه د', en: 'mujtahids',         tr: 'müctehidler' },
    { w: 'كِتَابَانِ',    root: 'ك ت ب', en: 'two books',         tr: 'iki kitap' },
    { w: 'دَفَّتَانِ',    root: 'د ف ف', en: 'two covers',        tr: 'iki kapak' },
    { w: 'مُسْلِمَات',    root: 'س ل م', en: 'Muslim women',      tr: 'müslüman kadınlar' },
    { w: 'الطَّالِبَات',  root: 'ط ل ب', en: 'the female students', tr: 'kız talebeler' },
    { w: 'أَب',        root: 'أ ب و', en: 'a father',          tr: 'baba', mudaf: true },
    { w: 'أَخ',        root: 'أ خ و', en: 'a brother',         tr: 'kardeş', mudaf: true },
    { w: 'ذُو',        root: 'ذ و و', en: 'the possessor of',  tr: 'sahibi', mudaf: true },
    { w: 'دَاعِي',      root: 'د ع و', en: 'one who calls',     tr: 'davet eden' },
    { w: 'جَوَارِي',     root: 'ج ر ي', en: 'flowing things',    tr: 'akanlar' },
    { w: 'هُدًى',       root: 'ه د ي', en: 'guidance',          tr: 'hidayet' },
    { w: 'مُصْطَفَى',    root: 'ص ف و', en: 'the chosen one',    tr: 'seçilmiş' },
    { w: 'اِسْتِعْلَاء',  root: 'ع ل و', en: 'counting oneself above', tr: "isti'lâ" },
    { w: 'دُعَاء',      root: 'د ع و', en: 'a supplication',    tr: 'dua' },
    { w: 'بَيْضَاء',     root: 'ب ي ض', en: 'white (fem.)',      tr: 'beyaz (müennes)' },
    { w: 'أَحْمَد',      root: 'ح م د', en: 'Ahmad (a name)',    tr: 'Ahmed', mamnu: true },
    { w: 'مَفَاتِيح',    root: 'ف ت ح', en: 'keys',              tr: 'anahtarlar', mamnu: true },
    { w: 'مُؤْمِنَات',   root: 'أ م ن', en: 'believing women',   tr: 'mümin kadınlar' },
    { w: 'مُعَلِّمَانِ',  root: 'ع ل م', en: 'two teachers',      tr: 'iki muallim' },
    { w: 'صَالِحُونَ',   root: 'ص ل ح', en: 'the righteous',     tr: 'salihler' },
  ],
  // idafa: a head, a tail and a case — including the ones that refuse
  idafas: [
    ['كِتَابٌ', 'الْوَلَدُ'], ['بَابٌ', 'الْمَسْجِدُ'], ['أَبٌ', 'بَكْرٌ'],
    ['مُسْلِمُونَ', 'الْمَدِينَةُ'], ['مُجْتَهِدُونَ', 'الْأُمَّةُ'],
    ['دَفَّتَانِ', 'الْمُصْحَفُ'], ['كِتَابَانِ', 'وَلَدٌ'],
    ['فَتَى', 'الْقَوْمِ'], ['قِسْمَةٌ', 'غَنَائِمُ'], ['الْكِتَابُ', 'الْوَلَدُ'],
    ['رَجَاءٌ', 'الْمَعْرِفَةُ'], ['مَدَارٌ', 'الْأَحْكَامُ'],
  ],
  // roots × forms: one paradigm each, sampled at the cells that carry rules
  verbs: [
    { root: 'ن ص ر', forms: ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'X'], bab: 1 },
    { root: 'ع ل م', forms: ['I', 'II', 'IV', 'V', 'X'], bab: 4 },
    { root: 'ق و ل', forms: ['I', 'IV', 'VII', 'VIII', 'X'], bab: 1 },
    { root: 'ر م ي', forms: ['I', 'II', 'IV', 'V', 'VIII'], bab: 2 },
    { root: 'م د د', forms: ['I', 'IV', 'VII', 'VIII', 'X'], bab: 1 },
    { root: 'و ع د', forms: ['I', 'II', 'IV', 'VIII', 'X'], bab: 2 },
    { root: 'ص ب ر', forms: ['I', 'VIII'], bab: 2 },
    { root: 'ط ل ع', forms: ['I', 'VIII'], bab: 3 },
    { root: 'ز ي د', forms: ['I', 'VIII'], bab: 2 },
    { root: 'س د د', forms: ['I', 'VII'], bab: 1 },
    { root: 'ق و م', forms: ['I', 'IV', 'X'], bab: 1 },
    { root: 'ح م ل', forms: ['I', 'VIII'], bab: 1 },
    { root: 'ك ت ب', forms: ['I', 'II', 'III', 'IV', 'VIII', 'X'], bab: 1 },
    { root: 'ف ت ح', forms: ['I', 'II', 'VII', 'VIII'], bab: 3 },
    { root: 'ج ه د', forms: ['I', 'III', 'VIII'], bab: 3 },
    { root: 'ش ر ك', forms: ['I', 'III', 'IV', 'VIII'], bab: 2 },
    { root: 'ن ز ل', forms: ['I', 'II', 'IV', 'V', 'X'], bab: 1 },
    { root: 'خ ر ج', forms: ['I', 'II', 'IV', 'X'], bab: 1 },
    { root: 'ب ي ع', forms: ['I', 'IV', 'VII', 'VIII'], bab: 2 },
    { root: 'د ع و', forms: ['I', 'VIII', 'X'], bab: 1 },
    { root: 'ه د ي', forms: ['I', 'IV', 'VIII'], bab: 2 },
    { root: 'ر د د', forms: ['I', 'IV', 'VIII', 'X'], bab: 1 },
    { root: 'ط و ع', forms: ['I', 'IV', 'V', 'X'], bab: 4 },
    { root: 'ع ر ف', forms: ['I', 'II', 'V', 'VIII'], bab: 2 },
    { root: 'س ل م', forms: ['I', 'II', 'IV', 'V', 'X'], bab: 1 },
  ],
  // Whole sentences the corpus has already had a human parse: the engines are
  // run over them and BOTH readings are written down side by side.
  analyseStories: ['mukhtasar-al-manar'],
};

const build = async (page) => page.evaluate((PLAN) => {
  const out = { endings: [], idafa: [], paradigms: [], mizan: [], mizanDropped: [], sentences: [] };
  const CASES = ['raf', 'nasb', 'jarr'];

  // ---- 1. THE ENDINGS. Every class of noun, every case, with the rule.
  PLAN.nouns.forEach(n => {
    const opt = { root: n.root };
    if (n.mamnu) opt.mamnu = true;
    if (n.mudaf) opt.mudaf = true;
    const t = AlamaEngine.table(n.w, opt);
    if (!t) return;
    out.endings.push({
      id: 'end:' + n.w, lemma: n.w, root: n.root, shape: t.shape,
      mamnu: t.mamnu, definite: t.definite, gloss: { en: n.en, tr: n.tr },
      rows: t.rows.map(r => ({
        kase: r.kase, out: r.out, manner: r.manner, sign: r.sign.ar,
        why: { ar: r.steps.map(s => s.ar).join(' '), en: r.steps.map(s => s.en).join(' '),
               tr: r.steps.map(s => s.tr).join(' ') },
      })),
    });
  });

  // ---- 2. THE IDAFA. Built, refused, and in all three cases.
  PLAN.idafas.forEach(([a, b]) => {
    CASES.forEach(k => {
      const r = IdafaEngine.build(a, b, k);
      if (!r) return;
      out.idafa.push(r.ok
        ? { id: `idf:${a}+${b}:${k}`, first: a, second: b, kase: k, out: r.out,
            head: r.head, tail: r.tail, ok: true,
            why: { ar: r.steps.map(s => s.ar).join(' '), en: r.steps.map(s => s.en).join(' '),
                   tr: r.steps.map(s => s.tr).join(' ') } }
        : { id: `idf:${a}+${b}:${k}`, first: a, second: b, kase: k, ok: false,
            why: r.refused });
    });
  });

  // ---- 3. THE PARADIGMS. Root × form, with the cells that carry the rules.
  PLAN.verbs.forEach(v => {
    const cls = nakilClass({ root: v.root });
    if (!cls) return;
    v.forms.forEach(f => {
      const d = sarfDerive(cls, f, v.bab);
      if (!d || !d.ok) return;
      out.paradigms.push({
        id: `sarf:${v.root}:${f}`, root: v.root, type: cls.type, form: f,
        bab: f === 'I' ? v.bab : null, wazn: d.wazn,
        masdar: d.masdar || null, ismFail: d.fail || null, ismMaful: d.maful || null,
        // the cells where a rule shows: he / they-fem (fakk or hadhf) / you-masc,
        // the mudari head and its own they-fem, the bare amr, and the governed pair
        cells: { maziHe: d.mazi[0], maziTheyF: d.mazi[5], maziYouM: d.mazi[6],
                 mudariHe: d.mudari[0], mudariTheyF: d.mudari[5],
                 amr: d.amr[0], amrTheyF: d.amr[5],
                 mansub: d.mansub, majzum: d.majzum },
        note: d.note || null,
      });
      // …and the scale for the participle. A scale is only admitted if it
      // ROUND-TRIPS: put the root letters back into ف ع ل and the word must come
      // out again. Standing a root in the balance is ambiguous exactly when a
      // root letter is also one of the pattern's augments — ن ص ر through
      // اِنْفَعَلَ puts two nuns side by side and the mizan cannot tell which is
      // which. Those are DROPPED rather than committed wrong, and counted, so
      // the gap is visible instead of silent.
      const mz = typeof WaznEngine !== 'undefined' && d.fail
        ? WaznEngine.mizan(d.fail, v.root) : null;
      if (mz) {
        const rs = v.root.split(/\s+/);
        const map = { 'ف': rs[0], 'ع': rs[1], 'ل': rs[2] };
        // ONE pass. Chained replaces cascade — ف→ع then ع→ل turns فَاعِل for
        // ع ل م into مَامِم and calls a perfectly good scale broken.
        const back = mz.replace(/[فعل]/g, ch => map[ch]);
        const flat = s => (s || '').normalize('NFC').replace(/[ً-ْ]/g, '');
        // A scale is UNDECIDABLE when one of the pattern's augment letters is
        // also one of the root's: اِنْفَعَلَ on ن ص ر puts two nuns side by side
        // and nothing in the surface says which is the augment. Both orderings
        // rebuild the same word, so the round-trip cannot catch it — the test
        // has to be on the letters, not on the output.
        const augments = new Set(flat(mz).split('').filter(c => !'فعل'.includes(c)));
        const clash = rs.some(r => augments.has(r));
        const why = flat(back) !== flat(d.fail) ? 'does-not-round-trip'
                  : clash ? 'augment-letter-is-also-a-radical' : null;
        if (!why) out.mizan.push({ id: `mizan:${v.root}:${f}`, word: d.fail, root: v.root, mizan: mz });
        else out.mizanDropped.push({ id: `mizan:${v.root}:${f}`, word: d.fail,
                                     root: v.root, mizan: mz, rebuilt: back, why });
      }
    });
  });
  // ---- 4. THE WORKED SENTENCES. Every sentence of the named stories, with
  // the HUMAN parse the corpus carries and the ENGINES' reading of the same
  // words written next to it. This is the honest shape for an analysis set:
  // the engines produce a SHORTLIST, not a verdict, so their reading is
  // recorded as a claim to be judged against the human one, and the agreement
  // is counted rather than asserted. Where they differ, the row is the lesson.
  (PLAN.analyseStories || []).forEach(sid => {
    const st = STORIES.find(x => x.id === sid);
    if (!st) return;
    st.chapters.forEach(ch => ch.sentences.forEach(sen => {
      const text = sen.tokens.map(t => t.s.full).join(' ');
      let rows = [];
      try { rows = SentenceAnalyzer.analyze(text) || []; } catch (e) { rows = []; }
      const HEAD = { noun: 'noun', 'noun?': 'noun', verb: 'verb', particle: 'part',
                     part: 'part', pron: 'pron', propn: 'noun', conj: 'conj' };
      let agree = 0, judged = 0;
      const tokens = sen.tokens.map((t, i) => {
        const r = rows[i] || {};
        const said = HEAD[r.kind] || r.kind || null;
        const human = t.pos === 'propn' ? 'noun' : t.pos;
        // prep, conj and part are ONE class to the analyzer: it returns
        // «particle» for all three and has never claimed to separate them.
        // Scoring them apart would be scoring it on a question it does not
        // answer, and would report a number that means nothing.
        // …and a PRONOUN is an ism. That is the tradition's own ruling and it
        // is written into CLAUDE.md: هُوَ and مَا are asma, not particles. The
        // corpus tags them `pron` for the reader's sake; scoring them against
        // the analyzer's «noun» as a miss would be marking the engine wrong for
        // agreeing with the books.
        const norm = x => (['conj', 'prep', 'part'].includes(x) ? 'part'
                         : x === 'pron' ? 'noun' : x);
        if (said && human) { judged++; if (norm(said) === norm(human)) agree++; }
        return { w: t.s.full, lex: t.lex,
                 human: { pos: t.pos, grammar: t.grammar || [], irab: t.irab.en },
                 engine: { kind: r.kind || null, lemma: r.lemma || null,
                           root: r.root || null, wazn: r.wazn || null,
                           sure: r.sure === undefined ? null : r.sure },
                 match: said && human ? norm(said) === norm(human) : null };
      });
      out.sentences.push({
        id: `sen:${sid}:${ch.n}:${sen.id}`, story: sid, chapter: ch.n, sentence: sen.id,
        text, translation: sen.translation,
        jumal: (sen.jumal || []).map(j => ({ text: j.text, ar: j.ar, en: j.en })),
        posAgreement: judged ? Math.round(agree / judged * 1000) / 10 : null,
        judged, agree, tokens,
      });
    }));
  });
  return out;
}, PLAN);

(async () => {
  const browser = await chromium.launch({ executablePath: findChrome() });
  const page = await browser.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  await page.goto(pathToFileURL(READER).href);
  const data = await build(page);
  await browser.close();
  if (errs.length) { console.error('page errors:', errs); process.exit(1); }

  const bank = {
    generated: true,
    source: 'tools/gen_drills.js',
    note: {
      en: 'GENERATED, not authored. Every form here was computed by the reader\'s own exact engines from a root or lemma the corpus already carries. It is committed so that any engine change that moves a cell shows up as a diff on a named item. It is not a story and it is not scholarship: it is the engines\' behaviour, written down.',
      tr: 'YAZILMADI, ÜRETİLDİ. Buradaki her şekil, külliyatın hâlihazırda taşıdığı bir kök yahut lemmadan hareketle uygulamanın kendi kat\'î motorlarınca hesaplanmıştır. Bir motor değişikliği tek bir hâneyi oynattığında adı belli bir madde üzerinde fark olarak görünsün diye depoya işlenir. Bu bir metin değildir, ilmî bir eser hiç değildir: motorların davranışının yazıya geçirilmiş hâlidir.',
    },
    counts: { endings: data.endings.length, idafa: data.idafa.length,
              paradigms: data.paradigms.length, mizan: data.mizan.length,
              mizanDropped: data.mizanDropped.length,
              sentences: data.sentences.length,
              sentenceTokens: data.sentences.reduce((n, s2) => n + s2.tokens.length, 0),
              posAgreement: (() => {
                const a = data.sentences.reduce((n, s2) => n + s2.agree, 0);
                const j = data.sentences.reduce((n, s2) => n + s2.judged, 0);
                return j ? Math.round(a / j * 1000) / 10 : null;
              })(),
              rows: data.endings.reduce((n, e) => n + e.rows.length, 0)
                    + data.idafa.length + data.paradigms.length * 9 + data.mizan.length
                    + data.sentences.reduce((n, s2) => n + s2.tokens.length, 0) },
    ...data,
  };
  const text = JSON.stringify(bank, null, 1);

  if (process.argv.includes('--check')) {
    if (!fs.existsSync(OUT)) { console.error('no committed bank to check against'); process.exit(1); }
    const was = fs.readFileSync(OUT, 'utf8');
    if (was.normalize('NFC') !== text.normalize('NFC')) {
      console.error('DRIFT: the generated bank no longer matches the committed one.');
      console.error('Run `node tools/gen_drills.js` and read the diff — an engine changed.');
      process.exit(1);
    }
    console.log(`drill bank unchanged — ${bank.counts.rows} derived rows`);
    return;
  }
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, text, 'utf8');
  console.log(`wrote ${path.relative(ROOT, OUT)}: ${bank.counts.endings} nouns × 3 cases, ` +
              `${bank.counts.idafa} idafas, ${bank.counts.paradigms} paradigms, ` +
              `${bank.counts.mizan} scales — ${bank.counts.rows} derived rows` +
              (bank.counts.mizanDropped ? `; ${bank.counts.mizanDropped} scales dropped as ambiguous` : '') +
              `\n  ${bank.counts.sentences} worked sentences, ${bank.counts.sentenceTokens} tokens ` +
              `— engines agree with the human part-of-speech on ${bank.counts.posAgreement}%`);
})();
