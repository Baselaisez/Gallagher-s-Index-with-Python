// v356-G — the in-page half of tools/inventory.py: what the BUILT page holds at run time, read from its own globals.
// Evaluated inside prototype/reader.html (tools/inventory_prove.js for a fresh page; the smoke suite on the page it has open).
// Returns plain JSON: {classes, tables, games, labs, shelves, shelfOf, ui}. Read-only: it opens nothing and writes nothing.
// tables: every class's UPPER-CASE static data (arrays, plain objects, Maps, Sets) → {n, ids?}; ids are the rows' id / key /
// name (or the strings themselves, or the object's keys), so a lost rule is NAMED, not only counted. Functions, RegExps and
// scalars are not tables. The class list is read from the page's code script by the same pattern tools/inventory.py uses.
(() => {
  const G = (0, eval);
  const code = [...document.scripts].filter(s => !s.src).map(s => s.text).find(t => t.length < 30e6 && /\bclass GameFactory\b/.test(t)) || '';
  const classes = [...new Set([...code.matchAll(/^\s*class ([A-Za-z_$][\w$]*)/gm)].map(m => m[1]))].sort();
  const cut = s => String(s).slice(0, 60);
  const idOf = r => r && typeof r === 'object' ? (['id', 'key', 'name'].map(k => r[k]).find(v => typeof v === 'string' || typeof v === 'number')) : (typeof r === 'string' ? r : undefined);
  const table = v => {
    if (Array.isArray(v)) { const ids = v.map(idOf); return ids.length && ids.every(x => x !== undefined) ? { n: v.length, ids: [...new Set(ids.map(cut))].sort() } : { n: v.length }; }
    if (v instanceof Map) return { n: v.size, ids: [...new Set([...v.keys()].map(cut))].sort() };
    if (v instanceof Set) { const a = [...v]; return a.every(x => typeof x === 'string' || typeof x === 'number') ? { n: a.length, ids: [...new Set(a.map(cut))].sort() } : { n: a.length }; }
    if (v && typeof v === 'object' && !(v instanceof RegExp) && Object.getPrototypeOf(v) === Object.prototype) { const k = Object.keys(v); return { n: k.length, ids: [...new Set(k.map(cut))].sort() }; }
    return null;
  };
  const tables = {}, missing = [];
  for (const c of classes) {
    let C; try { C = G(c); } catch (e) { missing.push(c); continue; }
    if (typeof C !== 'function') { missing.push(c); continue; }
    const t = {};
    for (const k of Object.getOwnPropertyNames(C).sort()) {
      if (!/^[A-Z][A-Z0-9_]*$/.test(k)) continue;
      let v; try { v = C[k]; } catch (e) { continue; }
      const r = table(v); if (r && r.n) t[k] = r;
    }
    if (Object.keys(t).length) tables[c] = t;
  }
  const get = n => { try { return G(n); } catch (e) { return undefined; } };
  const ids = a => (a || []).map(x => x && x.id).filter(Boolean);
  const GF = get('GameFactory'), LT = get('LAB_TOOLS'), LS = get('LIB_SOURCES'), ST = get('STORIES') || [], L = get('L') || {}, so = get('sourceOf');
  const shelfOf = {}; for (const s of ST) { try { shelfOf[s.id] = (so && so(s)) || ''; } catch (e) { shelfOf[s.id] = ''; } }
  const ui = {}; for (const lang of Object.keys(L).sort()) if (L[lang] && typeof L[lang] === 'object') ui[lang] = Object.keys(L[lang]).sort();
  return { classes, unreachable: missing, tables, games: ids(GF && GF.CATALOGUE), labs: ids(LT), shelves: ids(LS), shelfOf, ui };
})
