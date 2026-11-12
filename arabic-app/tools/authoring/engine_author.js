// engine_author.js — the engines read a new text so the author does not start from nothing.
//
// Input: a source file in the transcription format used for the owner's scanned uploads —
//   "# …"            a comment / page marker ("# page 7" records the page for the sentences after it)
//   "## N title"     a chapter header (N = chapter number, title = its Arabic title)
//   anything else    one sentence per line, fully vocalised; "[print: …]" notes are stripped and recorded as divergences
// Output: JSON with, per sentence, the ḍabṭ engine's reading of every word (DabtEngine.vowel — the same rule engine the
// Muḥallil runs on a typed sentence: ending, rule, head), the word's lexicon entry when the global glossary knows it
// (its lex KEY, lemma, part of speech, gloss) and the words the lexicon does not know, listed once each at the end so the
// author writes exactly those entries. Nothing here is a built-up AI: the rules decide, the author reviews.
//
//   CHROMIUM_PATH=… NODE_PATH=… READER=<reader.html> node tools/authoring/engine_author.js <src.txt> <out.json>
const fs = require('fs');
const { chromium } = require('playwright-core');
const [src, outPath] = process.argv.slice(2);
if (!src || !outPath) { console.error('usage: engine_author.js <src.txt> <out.json>'); process.exit(2); }
const text = fs.readFileSync(src, 'utf8');
const chapters = []; let cur = null, page = null;
for (const raw of text.split(/\r?\n/)) {
  const line = raw.trim(); if (!line) continue;
  const pm = line.match(/^#\s*page\s+(\d+)/i); if (pm) { page = Number(pm[1]); continue; }
  if (line.startsWith('##')) { const m = line.match(/^##\s*(\d+)\s+(.*)$/); cur = { n: m ? Number(m[1]) : chapters.length + 1, title: m ? m[2].trim() : line.replace(/^#+\s*/, ''), sentences: [] }; chapters.push(cur); continue; }
  if (line.startsWith('#')) continue;
  if (!cur) { cur = { n: 1, title: '', sentences: [] }; chapters.push(cur); }
  const notes = []; const clean = line.replace(/\s*\[print:([^\]]*)\]/g, (_, n) => { notes.push(n.trim()); return ''; }).trim();
  cur.sentences.push({ page, text: clean, notes });
}
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); const p = await b.newPage();
  await p.addInitScript(() => { window.__QISSA_QUIET_OFF = true; });
  await p.goto('file://' + require('path').resolve(process.env.READER)); await p.waitForFunction(() => window.__qissaBootedAt, null, { timeout: 180000 });
  const res = await p.evaluate((chapters) => {
    const N = x => String(x || '').normalize('NFC');
    const bare = x => N(x).replace(/[ً-ْٰـ]/g, '');
    // lemma → lex key, from every shipped glossary (the first package that keys a lemma owns it; the same key is reused everywhere)
    const fold = x => bare(x).replace(/[أإآٱ]/g, 'ا').replace(/^ال/, '');
    const keyOf = new Map(), keyOfBare = new Map(), keyOfPlural = new Map();
    (typeof STORIES === 'undefined' ? [] : STORIES).forEach(st => Object.entries(st.glossary || {}).forEach(([k, e]) => {
      const lm = N(String((e && e.lemma) || '').split(/[()\s]/)[0]); if (!lm) return;
      const rec = { key: k, pos: e.pos, gloss: e.gloss, lemma: e.lemma, plural: e.plural, root: e.root };
      if (!keyOf.has(lm)) keyOf.set(lm, rec);
      const bl = fold(lm); if (bl && !keyOfBare.has(bl)) keyOfBare.set(bl, rec);
      String(e.plural || '').split(/[\/،,]/).map(x => fold(x.trim())).filter(Boolean).forEach(pl => { if (!keyOfPlural.has(pl)) keyOfPlural.set(pl, rec); });
    }));
    const ENC_RE = /(هما|كما|هم|هن|كم|كن|نا|ها|ه|ك|ني|ي)$/;
    const hostsOf = (w, enc) => {
      // the written word, its host without the enclitic, without a وَ/فَ prefix, without a بِ/لِ/كَ clitic — every candidate the lexicon might own
      const out = []; const push = x => { if (x && !out.includes(x)) out.push(x); };
      let h = N(w);
      if (enc) { const b = bare(h); if (b.endsWith(enc)) { let n = enc.length, o = h, k = 0; while (k < n && o) { const ch = o[o.length - 1]; o = o.slice(0, -1); if (!/[\u064B-\u0652\u0670]/.test(ch)) k++; } h = o; } }
      push(h);
      const noPre = /^[وف]\u064e/.test(h) && bare(h).length >= 3 ? h.slice(2) : null; if (noPre) push(noPre);
      [h, noPre].filter(Boolean).forEach(x => { if (/^[بل]\u0650|^ك\u064e/.test(x) && bare(x).length >= 3) { push(x.slice(2)); if (/^ل\u0650ل/.test(x)) push('ا' + x.slice(2)); } });
      return out;
    };
    const lookup = (w, enc) => {
      const out = { key: null, lemma: null, pos: null, gloss: null, via: null };
      for (const cand of hostsOf(w, enc)) {
        try { const e = DabtEngine.lex(cand, true); if (e && e.lemma) { const lm = N(String(e.lemma).split(/[()\s]/)[0]); const h = keyOf.get(lm) || keyOfBare.get(fold(lm)) || keyOfPlural.get(fold(cand)); out.lemma = out.lemma || e.lemma; out.pos = out.pos || e.pos || null; out.gloss = out.gloss || e.gloss || null; if (h) { out.key = h.key; out.pos = h.pos || out.pos; out.gloss = h.gloss || out.gloss; out.via = 'lex'; return out; } } } catch (e) {}
        const h2 = keyOfBare.get(fold(cand)) || keyOfPlural.get(fold(cand)); if (h2) { out.key = h2.key; out.lemma = h2.lemma; out.pos = h2.pos; out.gloss = h2.gloss; out.via = 'bare'; return out; }
      }
      for (const cand of hostsOf(w, enc)) {
        try { const v = RootFinder.find(cand); const lm = v && (v.lemma || (v.entry && v.entry.lemma)); if (lm) { const h = keyOf.get(N(String(lm).split(/[()\s]/)[0])) || keyOfBare.get(fold(String(lm).split(/[()\s]/)[0])); if (h) { out.key = h.key; out.lemma = lm; out.pos = h.pos; out.gloss = h.gloss; out.via = 'verb'; return out; } out.lemma = out.lemma || lm; } } catch (e) {}
      }
      return out;
    };
    const E = (txt) => { DabtEngine._lex24 = null; DabtEngine._pos24 = null; DabtEngine._orig24 = null; DabtEngine._lastGraded26 = null; DabtEngine._carry26 = null; const v = DabtEngine.vowel(txt, 'endings'); const rows = DabtEngine._rows135 || []; return (v.words || []).map((w, i) => { const r = rows[i] || {}; let enc = r.enc || ''; if (!enc) { try { enc = DabtEngine.guessEnc(r, w.w) || ''; } catch (e) { enc = ''; } } const lk = lookup(w.w, enc); return { w: N(w.w), out: N(w.out), k: w.k, rule: w.rule, head: (w.head === undefined ? null : w.head), kind: r.kind || null, enc: enc || null, cell: r.cell ? { tense: r.cell.tense, i: r.cell.i, form: r.cell.form } : null, lemma: r.lemma || lk.lemma, key: lk.key, pos: lk.pos, gloss: lk.gloss, via: lk.via }; }); };
    const unknown = new Map();
    const out = chapters.map(ch => ({ ...ch, sentences: ch.sentences.map(s => { const words = E(s.text); try { const T = WujuhEngine.table(s.text); if (T.rows.length === words.length) T.items.forEach(v => { if (words[v.i] && v.face && v.face !== 'none') words[v.i].wajh = v.face; }); } catch (e) {} words.forEach(w => { if (!w.key && (w.kind !== 'particle' || !w.enc)) { const b = bare(w.w); if (!unknown.has(b)) unknown.set(b, { w: w.w, kind: w.kind, lemma: w.lemma, enc: w.enc || '', n: 0 }); unknown.get(b).n++; } }); return { ...s, words }; }) }));
    return { chapters: out, unknown: [...unknown.entries()].map(([b, v]) => ({ bare: b, ...v })) };
  }, chapters);
  fs.writeFileSync(outPath, JSON.stringify(res, null, 1));
  const nS = res.chapters.reduce((a, c) => a + c.sentences.length, 0), nW = res.chapters.reduce((a, c) => a + c.sentences.reduce((x, s) => x + s.words.length, 0), 0);
  console.log(`chapters ${res.chapters.length} sentences ${nS} words ${nW} unknown ${res.unknown.length}`);
  await b.close();
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
