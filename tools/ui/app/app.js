/* very-ai-product-loops · local console
 *
 * Renders the read model served by tools/ui/serve.py. No build step, no dependencies: a product
 * manager runs `python3 tools/ui/serve.py` and sees their product. The canon is never re-interpreted
 * here — everything shown comes from tools/loops/ (one parser), and this file only lays it out.
 *
 * Interface language follows the instance: `config.yaml` → `language`. Adding a locale means adding
 * one object to STR below — nothing else in this file knows a language exists.
 */
'use strict';

/* ---------------------------------------------------------------- strings */
const STR = {
  en: {
    tabs: { overview: 'Overview', step: 'Step', artifacts: 'Artifacts', registers: 'Registers',
      metrics: 'Metrics', open: 'Open', skills: 'Skills', log: 'Change log', checks: 'Checks' },
    status: 'status', step: 'step', lastPass: 'last pass',
    noState: 'not recorded', theme: 'theme', themeauto: 'auto', themelight: 'light', themedark: 'dark',
    addFolder: 'Add a product folder', addHint: 'add a folder…',
    cascade: 'The cascade', instanceReading: 'How this instance reads', product: 'Product',
    cadence: 'cadence', artifact: 'artifact', filled: 'written',
    gate: 'Gate', gateDone: 'closed', gateOpen: 'open', gateNa: 'n/a', gateDeferred: 'deferred',
    gateUnknown: 'unrecorded', words: 'words', gaps: 'gaps', proposals: 'agent proposals',
    notWritten: 'not written yet', offSkeleton: 'outside the skeleton',
    statusAsks: 'What the active status asks here', emphasised: 'emphasised for this stage',
    fillWith: 'fill through', rows: 'rows',
    hypotheses: 'Hypotheses', risks: 'Risks', metricNodes: 'Metric nodes', readings: 'readings',
    withReadings: 'with readings', csvRows: 'csv rows',
    live: 'live', testing: 'testing',
    toClarify: 'To clarify', openGates: 'Gate items open', inFlight: 'Hypotheses in flight',
    latest: 'Latest readings', series: 'Series', allReadings: 'All readings',
    definedNotMeasured: 'Defined, never measured', notInTree: 'not defined in metric-tree.md',
    vsPrev: 'vs previous', basisNote: 'compared within the same basis',
    nothingOpen: 'Nothing open here.', nothingYet: 'Nothing here yet.', all: 'all',
    search: 'search…', lintTitle: 'Canon linter', healthTitle: 'Instance reading',
    lintClean: 'The linter reports no findings.', healthClean: 'Reads cleanly against the canon.',
    notChecked: 'Checked by neither', notCheckedBody: 'Prose quality, whether register values are true '
      + '(only their enums and ids are checked), prerequisite completeness, adapter fidelity — and '
      + 'nothing here judges product decisions. The console reports; the human decides.',
    changed: 'the folder changed — reloading', readOnly: 'read-only — the agent writes the files, this shows what they say',
    subProducts: 'Sub-products', umbrellaNote: 'This folder is an umbrella: the shared config and sources '
      + 'live here, and each product below keeps its own artifacts, state and registers.',
    openIt: 'open', plane: 'plane', vendored: 'framework', local: 'this product',
    produces: 'produces', usedBy: 'steps', prerequisites: 'prerequisites', reads: 'reads', writes: 'writes',
    inputs: 'inputs', interview: 'interview', fragment: 'section template',
    addSkillHint: 'To add or change a skill, ask the agent — it writes the canon’s anatomy into this '
      + 'product’s own tool-skills folder, and a product-local skill wins over a vendored one of the '
      + 'same name. It appears here on the next read. See EXTENDING.md.',
    handoff: 'handoff', sourcesTab: 'sources', deliverables: 'deliverables',
    whatElse: 'What else is here', nextPass: 'Where the next pass would go',
  },
  ru: {
    tabs: { overview: 'Обзор', step: 'Шаг', artifacts: 'Артефакты', registers: 'Реестры',
      metrics: 'Метрики', open: 'Открытое', skills: 'Скиллы', log: 'Журнал', checks: 'Проверки' },
    status: 'статус', step: 'шаг', lastPass: 'последний проход',
    noState: 'не зафиксирован', theme: 'тема', themeauto: 'авто', themelight: 'светлая', themedark: 'тёмная',
    addFolder: 'Добавить папку продукта', addHint: 'добавить папку…',
    cascade: 'Каскад шагов', instanceReading: 'Как читается инстанс', product: 'Продукт',
    cadence: 'ритм', artifact: 'артефакт', filled: 'заполнено',
    gate: 'Гейт', gateDone: 'закрыто', gateOpen: 'открыто', gateNa: 'не применимо',
    gateDeferred: 'отложено', gateUnknown: 'не зафиксировано', words: 'слов', gaps: 'пробелов',
    proposals: 'предложения агента', notWritten: 'ещё не написано', offSkeleton: 'вне скелета',
    statusAsks: 'Что просит активный статус на этом шаге', emphasised: 'выделено для этой стадии',
    fillWith: 'заполнять через', rows: 'строк',
    hypotheses: 'Гипотезы', risks: 'Риски', metricNodes: 'Узлы метрик', readings: 'показаний',
    withReadings: 'с показаниями', csvRows: 'строк в csv',
    live: 'в работе', testing: 'на проверке',
    toClarify: 'На уточнение', openGates: 'Незакрытые пункты гейта', inFlight: 'Гипотезы в работе',
    latest: 'Последние значения', series: 'Ряды', allReadings: 'Все показания',
    definedNotMeasured: 'Определены, но не измеряются', notInTree: 'нет определения в metric-tree.md',
    vsPrev: 'к предыдущему', basisNote: 'сравнение внутри одного basis',
    nothingOpen: 'Здесь всё закрыто.', nothingYet: 'Пока пусто.', all: 'все',
    search: 'поиск…', lintTitle: 'Линтер канона', healthTitle: 'Чтение инстанса',
    lintClean: 'Линтер не нашёл замечаний.', healthClean: 'Инстанс читается по канону без замечаний.',
    notChecked: 'Не проверяет никто', notCheckedBody: 'Качество текста, правдивость значений в реестрах '
      + '(проверяются только перечисления и идентификаторы), полнота предпосылок, точность адаптеров — '
      + 'и ничто здесь не судит продуктовые решения. Консоль показывает, решает человек.',
    changed: 'папка изменилась — перечитываю',
    readOnly: 'только чтение — файлы пишет агент, здесь видно, что в них',
    subProducts: 'Под-продукты', umbrellaNote: 'Эта папка — «зонтик»: общий конфиг и источники лежат '
      + 'здесь, а у каждого продукта ниже свои артефакты, состояние и реестры.',
    openIt: 'открыть', plane: 'плоскость', vendored: 'фреймворк', local: 'этот продукт',
    produces: 'производит', usedBy: 'шаги', prerequisites: 'предпосылки', reads: 'читает',
    writes: 'пишет', inputs: 'входы', interview: 'интервью', fragment: 'шаблон секции',
    addSkillHint: 'Чтобы добавить или изменить скилл, попроси агента — он создаст каноническую '
      + 'анатомию в папке скиллов этого продукта, и локальный скилл побеждает одноимённый '
      + 'вендоренный. Здесь он появится при следующем чтении. См. EXTENDING.md.',
    handoff: 'хэндовер', sourcesTab: 'источников', deliverables: 'поставляемых',
    whatElse: 'Что ещё здесь есть', nextPass: 'Куда пойдёт следующий проход',
  },
};

/* ---------------------------------------------------------------- state */
const S = {
  model: null, lint: null, instances: [], rev: -1,
  tab: 'overview', step: null, artifact: null, section: null,
  reg: 'hypotheses', regFilter: 'all', regSearch: '',
  skillPlane: 'library', skillPick: null, skillFile: null,
};

const L = () => (S.model && STR[S.model.language]) ? STR[S.model.language] : STR.en;
function t(key) {
  const path = key.split('.');
  const get = o => path.reduce((x, k) => (x || {})[k], o);
  return get(L()) || get(STR.en) || key;
}

/* ---------------------------------------------------------------- theme */
const THEMES = ['auto', 'light', 'dark'];
const theme = () => localStorage.getItem('loops-theme') || 'auto';
function applyTheme(next) {
  if (next) localStorage.setItem('loops-theme', next);
  const v = theme();
  if (v === 'auto') document.documentElement.removeAttribute('data-theme');
  else document.documentElement.setAttribute('data-theme', v);
}
const isDark = () => theme() === 'dark'
  || (theme() === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches);

/* Chart series colors: a validated categorical palette per mode — the house hues fail the
 * colorblind-separation and chroma checks as a categorical set, so they stay in the chrome. */
const SERIES = () => isDark() ? ['#3987e5', '#d95926', '#199e70'] : ['#2a78d6', '#eb6834', '#1baf7a'];

/* ---------------------------------------------------------------- DOM helpers */
function h(tag, attrs, ...kids) {
  const e = document.createElement(tag);
  for (const k in (attrs || {})) {
    const v = attrs[k];
    if (v === null || v === undefined || v === false) continue;
    if (k === 'class') e.className = v;
    else if (k === 'html') e.innerHTML = v;
    else if (k === 'text') e.textContent = v;
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else e.setAttribute(k, v === true ? '' : v);
  }
  for (const kid of kids.flat(9)) {
    if (kid === null || kid === undefined || kid === false) continue;
    e.append(kid instanceof Node ? kid : document.createTextNode(String(kid)));
  }
  return e;
}
const esc = s => String(s === null || s === undefined ? '' : s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const num = n => (n === null || n === undefined || isNaN(n)) ? '—'
  : Math.abs(n) >= 1000 ? Math.round(n).toLocaleString('en-US').replace(/,/g, ' ')
    : String(+(+n).toFixed(2));
const cell = (row, ...names) => {
  for (const n of names) if (row[n] !== undefined && row[n] !== '') return row[n];
  return '';
};
const stripMd = s => String(s || '').replace(/[*`]/g, '').trim();
const shortTitle = s => String(s || '').replace(/^Step \d+ — /, '');

/* ---------------------------------------------------------------- markdown (small, canon-aware) */
function inline(src) {
  const code = [];
  let s = esc(src);
  s = s.replace(/`([^`]+)`/g, (_, c) => { code.push(c); return `\u0000${code.length - 1}\u0000`; });
  s = s.replace(/\[([^\]]+)\]\((#?[^)\s]+)\)/g, (_, x, u) => `<a href="${u}" target="_blank" rel="noopener">${x}</a>`);
  s = s.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>').replace(/(^|[\s(])\*([^*]+)\*/g, '$1<em>$2</em>');
  s = s.replace(/(^|[\s(])_([^_]+)_(?=$|[\s.,;:)])/g, '$1<em>$2</em>');
  s = s.replace(/\[(assumption|sourced|validated|refuted)((?::)([^\]]*))?\]/g,
    (_, kind, __, rest) => `<span class="conf ${kind}">${kind}${rest ? ': ' + rest.trim() : ''}</span>`);
  s = s.replace(/—\s*(to clarify|уточнить)\s*—/g, '<span class="gapmark">— $1 —</span>');
  s = s.replace(/⚙️/g, '<span class="gear">⚙️</span>');
  s = s.replace(/\u0000(\d+)\u0000/g, (_, i) => {
    const c = code[+i];
    const cls = /^H-\d/.test(c) ? 'hyp' : /^R-\d/.test(c) ? 'risk' : /^M-[a-z]/.test(c) ? 'met' : '';
    return cls ? `<code class="rid ${cls}">${c}</code>` : `<code>${c}</code>`;
  });
  return s;
}
function md(src) {
  const lines = String(src || '').split('\n');
  const out = [];
  let i = 0, para = [];
  const flush = () => { if (para.length) { out.push(`<p>${inline(para.join(' '))}</p>`); para = []; } };
  const isDiv = l => /^\s*\|?[\s:|-]+\|?\s*$/.test(l);
  while (i < lines.length) {
    const l = lines[i];
    if (!l.trim()) { flush(); i++; continue; }
    if (l.trim().startsWith('|') && i + 1 < lines.length && isDiv(lines[i + 1])) {
      flush();
      const head = l.trim().replace(/^\||\|$/g, '').split('|').map(c => `<th>${inline(c.trim())}</th>`).join('');
      const rows = [];
      i += 2;
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        rows.push('<tr>' + lines[i].trim().replace(/^\||\|$/g, '').split('|')
          .map(c => `<td>${inline(c.trim())}</td>`).join('') + '</tr>');
        i++;
      }
      out.push(`<div class="tablewrap"><table><thead><tr>${head}</tr></thead><tbody>${rows.join('')}</tbody></table></div>`);
      continue;
    }
    const m = l.match(/^(#{1,4})\s+(.*)$/);
    if (m) { flush(); out.push(`<h${m[1].length + 1}>${inline(m[2].replace(/\{#[a-z0-9-]+\}/, ''))}</h${m[1].length + 1}>`); i++; continue; }
    if (/^\s*>/.test(l)) {
      flush();
      const q = [];
      while (i < lines.length && /^\s*>/.test(lines[i])) { q.push(lines[i].replace(/^\s*>\s?/, '')); i++; }
      out.push(`<blockquote>${md(q.join('\n'))}</blockquote>`);
      continue;
    }
    if (/^\s*([-*+]|\d+\.)\s+/.test(l)) {
      flush();
      const ordered = /^\s*\d+\./.test(l);
      const items = [];
      while (i < lines.length && (/^\s*([-*+]|\d+\.)\s+/.test(lines[i]) || (/^\s{2,}\S/.test(lines[i]) && items.length))) {
        if (/^\s*([-*+]|\d+\.)\s+/.test(lines[i])) items.push(lines[i].replace(/^\s*([-*+]|\d+\.)\s+/, ''));
        else items[items.length - 1] += ' ' + lines[i].trim();
        i++;
      }
      out.push(`<${ordered ? 'ol' : 'ul'}>${items.map(x => `<li>${inline(x)}</li>`).join('')}</${ordered ? 'ol' : 'ul'}>`);
      continue;
    }
    if (/^\s*<!--/.test(l)) { flush(); while (i < lines.length && !/-->/.test(lines[i])) i++; i++; continue; }
    para.push(l.trim());
    i++;
  }
  flush();
  return out.join('\n');
}

/* ---------------------------------------------------------------- tooltip */
const tip = h('div', { class: 'tip' });
document.body.append(tip);
function showTip(html, x, y) {
  tip.innerHTML = html;
  tip.classList.add('on');
  const r = tip.getBoundingClientRect();
  tip.style.left = Math.min(window.innerWidth - r.width - 10, Math.max(8, x + 13)) + 'px';
  tip.style.top = Math.max(8, y - r.height - 11) + 'px';
}
const hideTip = () => tip.classList.remove('on');

/* ---------------------------------------------------------------- charts */
const SVGNS = 'http://www.w3.org/2000/svg';
function svg(tag, attrs) {
  const e = document.createElementNS(SVGNS, tag);
  for (const k in (attrs || {})) if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]);
  return e;
}
const dateOf = r => r.period_end || r.measured_at || '';
const shortDate = d => (d || '').slice(2).replace(/-/g, '.');

function lineChart(groups, opts) {
  const W = 340, H = 150, P = { t: 12, r: 46, b: 22, l: 40 };
  const all = groups.flatMap(g => g.rows);
  const xs = [...new Set(all.map(dateOf))].sort();
  const vals = all.map(r => r.value).filter(v => v !== null);
  if (!xs.length || !vals.length) return null;
  let lo = Math.min(...vals), hi = Math.max(...vals);
  if (lo === hi) { lo = lo === 0 ? -1 : lo - Math.abs(lo) * 0.15; hi = hi + Math.abs(hi) * 0.15 || 1; }
  else { const pad = (hi - lo) * 0.12; lo -= pad; hi += pad; }
  if (lo > 0 && lo < (hi - lo) * 0.6) lo = 0;
  const X = i => P.l + (xs.length === 1 ? (W - P.l - P.r) / 2 : i * (W - P.l - P.r) / (xs.length - 1));
  const Y = v => P.t + (H - P.t - P.b) * (1 - (v - lo) / (hi - lo));
  const s = svg('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img' });

  [lo, (lo + hi) / 2, hi].forEach(v => {
    s.append(svg('line', { x1: P.l, x2: W - P.r, y1: Y(v), y2: Y(v), stroke: 'var(--grid)', 'stroke-width': 1 }));
    const tx = svg('text', { x: P.l - 6, y: Y(v) + 3.5, 'text-anchor': 'end', fill: 'var(--faint)',
      'font-size': 9, 'font-family': 'var(--mono)' });
    tx.textContent = num(hi - lo > 20 ? Math.round(v) : v);
    s.append(tx);
  });
  [0, xs.length - 1].forEach((i, k) => {
    if (xs.length === 1 && k === 1) return;
    const tx = svg('text', { x: X(i), y: H - 6, 'text-anchor': k === 0 ? 'start' : 'end',
      fill: 'var(--faint)', 'font-size': 9, 'font-family': 'var(--mono)' });
    tx.textContent = shortDate(xs[i]);
    s.append(tx);
  });

  const colors = SERIES();
  groups.forEach((g, gi) => {
    const color = groups.length === 1 ? colors[0] : colors[gi % colors.length];
    g.color = color;
    const pts = g.rows.filter(r => r.value !== null)
      .map(r => ({ x: X(xs.indexOf(dateOf(r))), y: Y(r.value), r }));
    if (!pts.length) return;
    if (pts.length > 1) {
      s.append(svg('path', {
        d: 'M' + pts.map(p => `${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' L'),
        fill: 'none', stroke: color, 'stroke-width': 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round',
      }));
      s.append(svg('path', {
        d: `M${pts[0].x.toFixed(1)} ${(H - P.b).toFixed(1)} L`
          + pts.map(p => `${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' L')
          + ` L${pts[pts.length - 1].x.toFixed(1)} ${(H - P.b).toFixed(1)} Z`,
        fill: color, opacity: 0.1, stroke: 'none',
      }));
    }
    const last = pts[pts.length - 1];
    s.append(svg('circle', { cx: last.x, cy: last.y, r: 4, fill: color,
      stroke: 'var(--paper)', 'stroke-width': 2 }));
    const lab = svg('text', { x: last.x + 7, y: last.y + 3.5, fill: 'var(--muted)',
      'font-size': 10, 'font-family': 'var(--mono)' });
    lab.textContent = num(last.r.value) + (groups.length > 1 ? ` ${g.label}` : '');
    s.append(lab);
    pts.forEach(p => {
      const hit = svg('circle', { cx: p.x, cy: p.y, r: 9, fill: 'transparent', style: 'cursor:crosshair' });
      hit.addEventListener('mousemove', ev => showTip(
        `<b>${esc(num(p.r.value))}</b> ${esc(opts.unit || '')}<br>`
        + `<span class="k">${esc(dateOf(p.r))}</span>`
        + (p.r.period_start ? ` <span class="k">(${esc(p.r.period_start)} → ${esc(p.r.period_end)})</span>` : '')
        + (g.label && groups.length > 1 ? `<br><span class="k">basis</span> ${esc(g.label)}` : '')
        + (p.r.source ? `<br><span class="k">source</span> ${esc(p.r.source)}` : '')
        + (p.r.note ? `<br>${esc(p.r.note)}` : ''), ev.clientX, ev.clientY));
      hit.addEventListener('mouseleave', hideTip);
      s.append(hit);
    });
  });
  return s;
}

function ring(done, total) {
  const pct = total ? done / total : 0, R = 22, C = 2 * Math.PI * R;
  const s = svg('svg', { viewBox: '0 0 52 52', class: 'ringsvg' });
  s.append(svg('circle', { cx: 26, cy: 26, r: R, fill: 'none', stroke: 'var(--grid)', 'stroke-width': 5 }));
  s.append(svg('circle', { cx: 26, cy: 26, r: R, fill: 'none', stroke: 'var(--accent)', 'stroke-width': 5,
    'stroke-linecap': 'round', 'stroke-dasharray': `${(C * pct).toFixed(1)} ${C.toFixed(1)}`,
    transform: 'rotate(-90 26 26)' }));
  const txt = svg('text', { x: 26, y: 30, 'text-anchor': 'middle', 'font-size': 14,
    'font-family': 'var(--mono)', fill: 'var(--ink)' });
  txt.textContent = Math.round(pct * 100) + '%';
  s.append(txt);
  return s;
}

/* ---------------------------------------------------------------- shared bits */
const TICK_ORDER = ['done', 'open', 'unknown', 'deferred', 'n/a'];
function gateBar(counts) {
  const total = TICK_ORDER.reduce((a, k) => a + (counts[k] || 0), 0) || 1;
  return h('div', { class: 'bar' }, TICK_ORDER.map(k => {
    const n = counts[k] || 0;
    return n ? h('i', { class: k === 'n/a' ? 'na' : k, style: `width:${(n / total * 100).toFixed(1)}%` }) : null;
  }));
}
const tickLabel = v => ({ done: t('gateDone'), open: t('gateOpen'), deferred: t('gateDeferred'),
  'n/a': t('gateNa'), unknown: t('gateUnknown') }[v] || v);
const tickTag = v => h('span', { class: 'tag ' + (v === 'n/a' ? 'na' : v) }, tickLabel(v));

function gateSummary(step) {
  const c = step.gate_counts || {};
  const parts = [`${c.done || 0}/${step.gate.length} ${t('gateDone')}`];
  if (c.unknown) parts.push(`${c.unknown} ${t('gateUnknown')}`);
  if (c.deferred) parts.push(`${c.deferred} ${t('gateDeferred')}`);
  return parts.join(' · ');
}
const confChips = conf => Object.entries(conf || {}).map(([k, n]) =>
  h('span', { class: 'tag ' + k }, `${k} ×${n}`));
const ridChips = ids => (ids || []).slice(0, 6).map(x => h('span', {
  class: 'tag ' + (/^H-/.test(x) ? 'hyp' : /^R-/.test(x) ? 'risk' : 'met'),
}, x));

function statTile(label, value, sub, onclick) {
  return h(onclick ? 'button' : 'div', { class: 'stat' + (onclick ? ' clickable' : ''), onclick },
    h('div', { class: 'l' }, label),
    h('div', { class: 'v' }, value),
    sub ? h('div', { class: 's' }, String(sub).slice(0, 90)) : null);
}

/* ---------------------------------------------------------------- overview */
function viewOverview() {
  const m = S.model;
  if (m.umbrella) return viewUmbrella();
  const reg = m.registers;
  const openGates = m.steps.reduce((a, s) =>
    a + s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown').length, 0);
  const hStatus = k => reg.hypotheses.rows.filter(r =>
    stripMd(cell(r, 'status', 'статус')).toLowerCase().startsWith(k)).length;
  const risksLive = reg.risks.rows.filter(r =>
    /open|mitigat|открыт|митиг/i.test(stripMd(cell(r, 'status', 'статус')))).length;
  const measured = Object.keys(m.metrics.series).length;
  const nextStep = m.steps.find(s => (s.gate_counts.open || 0) + (s.gate_counts.unknown || 0) > 0);

  const hero = h('div', { class: 'hero' },
    h('div', { style: 'min-width:0' },
      h('div', { class: 'kick' }, t('product')),
      h('h2', { class: 'heroname' }, m.product),
      m.goal ? h('div', { class: 'herogoal' }, m.goal) : null,
      m.scope_note ? h('div', { class: 'small muted clamp3', style: 'margin-top:8px' }, m.scope_note) : null),
    h('div', { class: 'herostats' },
      statTile(t('status'), m.active_status || '—', ''),
      statTile(t('step'), m.current_step ? String(m.current_step) : '—',
        m.last_pass ? `${t('lastPass')} ${m.last_pass}` : t('noState')),
      statTile(t('hypotheses'), String(reg.hypotheses.rows.length),
        `${hStatus('open')} ${t('gateOpen')} · ${hStatus('testing')} ${t('testing')}`,
        () => { S.tab = 'registers'; S.reg = 'hypotheses'; render(); }),
      statTile(t('risks'), String(reg.risks.rows.length), `${risksLive} ${t('live')}`,
        () => { S.tab = 'registers'; S.reg = 'risks'; render(); }),
      statTile(t('metricNodes'), String(reg.metric_tree.rows.length),
        `${measured} ${t('withReadings')} · ${m.metrics.rows} ${t('csvRows')}`,
        () => { S.tab = 'metrics'; render(); }),
      statTile(t('toClarify'), String(m.gaps.length),
        `${openGates} ${t('openGates').toLowerCase()}`, () => { S.tab = 'open'; render(); })));

  const ladder = h('div', { class: 'ladder' }, m.steps.map(s => {
    const written = s.sections.filter(x => x.present).length;
    return h('button', {
      class: 'step' + (m.current_step === s.step ? ' here' : '') + (s.artifact_file ? '' : ' pending'),
      onclick: () => { S.tab = 'step'; S.step = s.step; render(); },
    },
      h('div', { class: 'no' }, s.step),
      h('div', { class: 'stepbody' },
        h('div', { class: 'nm' }, shortTitle(s.title || s.name)),
        h('div', { class: 'meta clamp2' }, s.goal || s.cadence)),
      h('div', { class: 'gate' },
        h('div', { class: 'nums' }, `${written}/${s.sections.length} ${t('filled')}`),
        gateBar(s.gate_counts),
        h('div', { class: 'nums' }, gateSummary(s))));
  }));

  const health = m.health.length ? h('div', { class: 'notes' },
    m.health.slice(0, 3).map(x => h('div', { class: 'note ' + x.level },
      h('span', { class: 'who' }, x.level), h('div', {}, x.message))),
    m.health.length > 3 ? h('button', { class: 'tag', onclick: () => { S.tab = 'checks'; render(); } },
      `+${m.health.length - 3} → ${t('tabs.checks')}`) : null)
    : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('healthClean')));

  return h('div', {},
    hero,
    h('div', { class: 'grid cols-2', style: 'margin-top:18px' },
      h('div', {}, h('div', { class: 'kick' }, t('cascade')), ladder),
      h('div', { class: 'grid', style: 'align-content:start' },
        nextStep ? h('button', { class: 'card accent nextcard',
          onclick: () => { S.tab = 'step'; S.step = nextStep.step; render(); } },
          h('div', { class: 'kick' }, t('nextPass')),
          h('div', { class: 'row', style: 'align-items:center' },
            h('span', { class: 'bignum' }, nextStep.step),
            h('div', { style: 'min-width:0;text-align:left' },
              h('b', {}, shortTitle(nextStep.title || '')),
              h('div', { class: 'small muted clamp2' },
                (nextStep.gate.find(g => g.tick === 'open' || g.tick === 'unknown') || {}).label || '')))) : null,
        h('div', { class: 'card' }, h('div', { class: 'kick' }, t('instanceReading')), health),
        h('div', { class: 'card' },
          h('div', { class: 'kick' }, t('whatElse')),
          h('div', { class: 'items' },
            m.handoff.present ? h('div', { class: 'item' },
              h('span', { class: 'tag' }, t('handoff')),
              h('div', { class: 'txt small' }, 'HANDOFF.md ', m.handoff.updated || '')) : null,
            h('div', { class: 'item' }, h('span', { class: 'tag' }, t('sourcesTab')),
              h('div', { class: 'txt small' }, `${m.sources.files.length} ${t('sourcesTab')}`)),
            m.deliverables.length ? h('div', { class: 'item' },
              h('span', { class: 'tag' }, t('deliverables')),
              h('div', { class: 'txt small' }, m.deliverables.join(' · '))) : null)))));
}

function viewUmbrella() {
  const m = S.model;
  return h('div', {},
    h('div', { class: 'hero' },
      h('div', { style: 'min-width:0' },
        h('div', { class: 'kick' }, t('product')),
        h('h2', { class: 'heroname' }, m.product),
        h('div', { class: 'herogoal' }, t('umbrellaNote')),
        m.scope_note ? h('div', { class: 'small muted clamp3', style: 'margin-top:8px' }, m.scope_note) : null),
      h('div', { class: 'herostats' },
        statTile(t('status'), m.active_status || '—', ''),
        statTile(t('subProducts'), String(m.children.length), m.children.join(' · ')),
        statTile(t('sourcesTab'), String(m.sources.files.length), ''))),
    h('div', { class: 'kick', style: 'margin-top:18px' }, t('subProducts')),
    h('div', { class: 'grid cols-3' }, m.children.map(name => {
      const cand = S.instances.find(i => i.name === name && i.path.startsWith(m.path));
      return h('button', { class: 'card pick', onclick: () => cand && load(cand.path) },
        h('h3', {}, name),
        h('div', { class: 'small muted mono', style: 'margin-top:4px' }, name + '/'),
        h('div', { class: 'btn', style: 'margin-top:10px' }, t('openIt')));
    })));
}

/* ---------------------------------------------------------------- the step canvas */
function viewStep() {
  const m = S.model;
  if (!m.steps.length || !m.artifacts.length && m.umbrella) return h('div', { class: 'empty' }, t('nothingYet'));
  const s = m.steps.find(x => x.step === S.step) || m.steps[0];
  S.step = s.step;
  const perStep = (m.status && m.status.per_step && m.status.per_step[String(s.step)]) || null;
  const emph = new Set((perStep && perStep.tools) || []);
  const written = s.sections.filter(x => x.present).length;
  const gapsHere = s.sections.flatMap(x => (x.gap_lines || []).map(line => ({ line, id: x.id })));

  const picker = h('div', { class: 'steppick' }, m.steps.map(x => h('button', {
    class: x.step === s.step ? 'on' : '', onclick: () => { S.step = x.step; render(); },
  }, h('b', {}, x.step), h('span', {}, shortTitle(x.title || x.name)),
    h('i', { class: 'dot ' + ((x.gate_counts.open || x.gate_counts.unknown) ? 'open' : 'done') }))));

  const head = h('div', { class: 'stephead' },
    h('div', { class: 'no big' }, s.step),
    h('div', { style: 'min-width:0' },
      h('h2', {}, shortTitle(s.title || s.name)),
      s.goal ? h('div', { class: 'goal' }, s.goal) : null,
      h('div', { class: 'row tiny faint', style: 'margin-top:7px' },
        h('span', {}, t('artifact'), ': ', h('code', {}, s.artifact_file || s.output)),
        h('span', {}, t('cadence'), ': ', s.cadence),
        s.artifact_updated ? h('span', {}, s.artifact_updated) : null)),
    h('div', { class: 'stepprog' },
      ring(written, s.sections.length),
      h('div', { style: 'min-width:120px' },
        h('div', { class: 'tiny mono muted' }, `${written}/${s.sections.length} ${t('filled')}`),
        h('div', { class: 'tiny mono muted', style: 'margin:5px 0 5px' }, gateSummary(s)),
        gateBar(s.gate_counts))));

  const canvas = h('div', { class: 'canvas' }, s.sections.map(x => {
    const gate = s.gate.find(g => (g.sections || []).includes(x.id));
    return h('button', {
      class: 'scard' + (x.present ? '' : ' ghost') + (x.gaps ? ' hasgaps' : ''),
      onclick: () => { S.tab = 'artifacts'; S.artifact = s.artifact_file; S.section = x.id; render(); },
    },
      h('div', { class: 'sctop' },
        h('div', { class: 'scname' }, x.title || x.id),
        gate ? tickTag(gate.tick) : (x.off_skeleton ? h('span', { class: 'tag' }, t('offSkeleton')) : null)),
      h('code', { class: 'scid' }, '#' + x.id),
      x.present
        ? h('div', { class: 'scbody' },
          x.lead ? h('div', { class: 'sclead clamp3' }, x.lead) : null,
          (x.bullets || []).length ? h('ul', { class: 'scbul' },
            x.bullets.slice(0, 2).map(b => h('li', { class: 'clamp2' }, b))) : null,
          x.table_rows ? h('div', { class: 'tiny faint' }, `${x.table_rows} ${t('rows')}`) : null)
        : h('div', { class: 'scbody' },
          h('div', { class: 'sclead faint clamp3' }, x.what || t('notWritten')),
          x.tools.length ? h('div', { class: 'tiny faint', style: 'margin-top:6px' },
            `${t('fillWith')}: ${x.tools.join(' · ')}`) : null),
      h('div', { class: 'scfoot' },
        x.present ? h('span', { class: 'tag' }, `${x.words} ${t('words')}`) : null,
        confChips(x.confidence),
        x.gaps ? h('span', { class: 'tag open' }, `${x.gaps} ${t('gaps')}`) : null,
        x.proposals ? h('span', { class: 'tag gear' }, `⚙️ ×${x.proposals}`) : null,
        ridChips(x.ids),
        x.tools.length ? h('span', { class: 'tool' + (x.tools.some(y => emph.has(y)) ? ' emph' : '') },
          x.tools[0]) : null));
  }));

  const rail = h('div', { class: 'grid', style: 'align-content:start' },
    perStep ? h('div', { class: 'card' },
      h('div', { class: 'kick' }, `${t('statusAsks')} · ${m.active_status}`),
      h('ul', { class: 'goals' }, (perStep.goals || []).map(g => h('li', {}, g))),
      (perStep.tools || []).length ? h('div', { class: 'tools', style: 'margin-top:9px' },
        perStep.tools.map(x => h('span', { class: 'tool emph', title: t('emphasised') }, x))) : null) : null,
    gapsHere.length ? h('div', { class: 'card' },
      h('div', { class: 'kick' }, `${t('toClarify')} · ${gapsHere.length}`),
      h('div', { class: 'items' }, gapsHere.slice(0, 8).map(g => h('div', { class: 'item' },
        h('code', { class: 'tag' }, '#' + g.id),
        h('div', { class: 'txt small', html: inline(g.line) }))))) : null,
    h('div', { class: 'card' },
      h('div', { class: 'kick' }, t('gate')),
      h('div', { class: 'items' }, s.gate.map(g => h('div', { class: 'item' },
        tickTag(g.tick),
        h('div', { class: 'txt' }, h('div', { class: 'small' }, g.label),
          h('div', { class: 'why mono tiny' }, (g.targets || []).join(' + ')
            + (g.register ? ` → ${g.register}` : ''))))))));

  return h('div', {}, picker, head, h('div', { class: 'grid cols-canvas' }, canvas, rail));
}

/* ---------------------------------------------------------------- artifacts */
function viewArtifacts() {
  const m = S.model;
  if (!m.artifacts.length) return h('div', { class: 'empty' }, t('nothingYet'));
  const art = m.artifacts.find(a => a.file === S.artifact) || m.artifacts[0];
  S.artifact = art.file;
  const sec = art.sections.find(x => x.id === S.section) || art.sections[0];

  const toc = h('div', { class: 'toc' }, m.artifacts.map(a => [
    h('div', { class: 'file' }, a.file),
    a.sections.map(x => h('button', {
      'aria-current': a.file === art.file && sec && x.id === sec.id,
      onclick: () => { S.artifact = a.file; S.section = x.id; render(); },
    }, h('span', {}, x.title || x.id), h('span', { class: 'dotcol' },
      x.gaps.length ? h('i', { class: 'pip gap', title: `${x.gaps.length} ${t('gaps')}` }) : null,
      x.markers.proposals ? h('i', { class: 'pip gear', title: t('proposals') }) : null,
      !x.words ? h('i', { class: 'pip empty' }) : null))),
  ]));

  const ids = sec ? [].concat(sec.markers.hypotheses, sec.markers.risks, sec.markers.metrics) : [];
  const body = sec ? h('div', {},
    h('div', { class: 'spread' },
      h('h2', {}, sec.title || sec.id),
      h('span', { class: 'row' },
        h('code', { class: 'mono tiny' }, `${art.file}#${sec.id}`),
        confChips(sec.markers.confidence),
        sec.markers.proposals ? h('span', { class: 'tag gear' }, `⚙️ ×${sec.markers.proposals}`) : null)),
    ids.length ? h('div', { class: 'row', style: 'margin:8px 0 2px' }, ridChips(ids)) : null,
    h('hr'),
    h('div', { class: 'md', html: md(sec.body) })) : h('div', { class: 'empty' }, t('nothingYet'));

  return h('div', { class: 'reader' }, toc, h('div', { class: 'card' }, body));
}

/* ---------------------------------------------------------------- registers */
function viewRegisters() {
  const m = S.model;
  const which = S.reg;
  const reg = m.registers[which === 'metrics' ? 'metric_tree' : which];
  const tabs = h('div', { class: 'filters' }, [
    ['hypotheses', `${t('hypotheses')} · ${m.registers.hypotheses.rows.length}`],
    ['risks', `${t('risks')} · ${m.registers.risks.rows.length}`],
    ['metrics', `${t('metricNodes')} · ${m.registers.metric_tree.rows.length}`],
  ].map(([k, lab]) => h('button', {
    'aria-pressed': which === k, onclick: () => { S.reg = k; S.regFilter = 'all'; render(); },
  }, lab)));

  if (!reg.present) return h('div', {}, tabs, h('div', { class: 'empty' }, `${reg.file} — ${t('nothingYet')}`));

  const enums = m.framework.enums;
  const enumCol = which === 'hypotheses' ? ['type', 'тип']
    : which === 'risks' ? ['category', 'категория'] : ['kind', 'вид'];
  const allowed = which === 'hypotheses' ? enums['hypothesis type']
    : which === 'risks' ? enums['risk category'] : enums['metric kind'];
  const statusCols = ['status', 'статус'];
  const facets = [...new Set(reg.rows.map(r => stripMd(cell(r, ...enumCol))).filter(Boolean))];

  const filters = h('div', { class: 'filters' },
    h('button', { 'aria-pressed': S.regFilter === 'all', onclick: () => { S.regFilter = 'all'; render(); } }, t('all')),
    facets.map(v => h('button', { 'aria-pressed': S.regFilter === v, onclick: () => { S.regFilter = v; render(); } }, v)),
    h('input', { type: 'search', placeholder: t('search'), value: S.regSearch,
      oninput: e => { S.regSearch = e.target.value; renderInto('#regtable', regTable()); } }));

  function regTable() {
    const cols = reg.columns;
    const rows = reg.rows.filter(r => {
      if (S.regFilter !== 'all' && stripMd(cell(r, ...enumCol)) !== S.regFilter) return false;
      if (S.regSearch && !Object.values(r).join(' ').toLowerCase().includes(S.regSearch.toLowerCase())) return false;
      return true;
    });
    return h('div', { class: 'tablewrap' }, h('table', {},
      h('thead', {}, h('tr', {}, cols.map(c => h('th', {}, c)))),
      h('tbody', {}, rows.map(r => {
        const val = stripMd(cell(r, ...enumCol));
        const bad = allowed && val && !allowed.includes(val);
        return h('tr', { class: bad ? 'flagged' : '' }, cols.map(c => {
          const v = r[c] || '';
          if (c === 'id') return h('td', { class: 'id' }, h('code', {}, stripMd(v)));
          if (statusCols.includes(c)) {
            return h('td', {}, h('span', { class: 'tag ' + stripMd(v).split(/[\s·]/)[0] }, stripMd(v) || '—'));
          }
          if (enumCol.includes(c)) {
            return h('td', {}, h('span', { class: 'tag ' + (bad ? 'err' : '') }, stripMd(v) || '—'),
              bad ? h('div', { class: 'tiny faint' }, allowed.join(' · ')) : null);
          }
          return h('td', { html: inline(v) });
        }));
      }))));
  }

  return h('div', {}, tabs, filters, h('div', { id: 'regtable' }, regTable()));
}

/* ---------------------------------------------------------------- metrics */
function viewMetrics() {
  const m = S.model;
  const tree = m.registers.metric_tree.rows;
  const series = m.metrics.series;
  const defOf = id => tree.find(r => stripMd(cell(r, 'id')) === id) || {};
  const order = tree.map(r => stripMd(cell(r, 'id'))).filter(Boolean);
  const withReadings = Object.keys(series).sort((a, b) => {
    const ia = order.indexOf(a), ib = order.indexOf(b);
    return (ia < 0 ? 1e6 : ia) - (ib < 0 ? 1e6 : ib) || a.localeCompare(b);
  });
  const undefinedIds = new Set(m.metrics.undefined || []);
  const without = order.filter(id => !series[id]);

  const kpis = h('div', { class: 'kpis' }, withReadings.map(id => {
    const rows = series[id].filter(r => r.value !== null);
    if (!rows.length) return null;
    const last = rows[rows.length - 1];
    const same = rows.filter(r => (r.basis || '') === (last.basis || ''));
    const prev = same.length > 1 ? same[same.length - 2] : null;
    const d = prev && prev.value ? (last.value - prev.value) / Math.abs(prev.value) * 100 : null;
    const def = defOf(id);
    const long = String(num(last.value)).length > 11;
    return h('div', { class: 'kpi' },
      h('div', { class: 'lab clamp3' }, stripMd(cell(def, 'definition', 'определение')).slice(0, 84) || id),
      undefinedIds.has(id) ? h('div', { class: 'tag err' }, t('notInTree')) : null,
      h('div', { class: 'val', style: long ? 'font-size:19px' : null }, num(last.value),
        h('span', { class: 'mono faint', style: 'font-size:12px;margin-left:4px' }, stripMd(cell(def, 'unit')))),
      d === null ? h('div', { class: 'delta flat' }, '—')
        : h('div', { class: 'delta ' + (d > 0.5 ? 'up' : d < -0.5 ? 'down' : 'flat'), title: t('basisNote') },
          `${d > 0 ? '+' : ''}${d.toFixed(1)}% ${t('vsPrev')}`),
      h('div', { class: 'when' }, `${id} · ${dateOf(last)}${last.basis ? ' · ' + last.basis : ''}`));
  }));

  const charts = h('div', { class: 'charts' }, withReadings.map(id => {
    const rows = series[id], def = defOf(id);
    const bases = [...new Set(rows.map(r => r.basis).filter(Boolean))];
    const groups = bases.length > 1 ? bases.map(b => ({ label: b, rows: rows.filter(r => r.basis === b) }))
      : [{ label: bases[0] || '', rows }];
    const chart = lineChart(groups, { unit: stripMd(cell(def, 'unit')) });
    return h('div', { class: 'chart' },
      h('div', { class: 'head' },
        h('div', { class: 't' }, id),
        h('div', { class: 'u' }, `${stripMd(cell(def, 'unit')) || '—'} · ${rows.length} ${t('readings')}`
          + ` · ${stripMd(cell(def, 'instrumentation', 'инструментирование')) || '—'}`)),
      chart || h('div', { class: 'empty' }, '—'),
      groups.length > 1 ? h('div', { class: 'legend' }, groups.map(g =>
        h('span', {}, h('i', { style: `background:${g.color}` }), g.label))) : null);
  }));

  const table = h('div', { class: 'tablewrap' }, h('table', {},
    h('thead', {}, h('tr', {}, ['id', 'period', 'measured_at', 'value', 'basis', 'source', 'note']
      .map(c => h('th', {}, c)))),
    h('tbody', {}, withReadings.flatMap(id => series[id].map(r => h('tr', {},
      h('td', { class: 'id' }, h('code', {}, id)),
      h('td', { class: 'mono tiny' }, r.period_start ? `${r.period_start} → ${r.period_end}` : '—'),
      h('td', { class: 'mono tiny' }, r.measured_at),
      h('td', { class: 'num' }, r.value === null ? r.raw_value : num(r.value)),
      h('td', { class: 'mono tiny' }, r.basis || '—'),
      h('td', { class: 'mono tiny' }, r.source || '—'),
      h('td', { class: 'tiny muted' }, r.note || '')))))));

  return h('div', {},
    withReadings.length ? [h('div', { class: 'kick' }, t('latest')), kpis,
      h('div', { style: 'height:18px' }), h('div', { class: 'kick' }, t('series')), charts,
      h('div', { style: 'height:18px' }), h('div', { class: 'kick' }, t('allReadings')), table]
      : h('div', { class: 'note warn' }, h('span', { class: 'who' }, '—'), h('div', {}, t('nothingYet'))),
    without.length ? [h('div', { style: 'height:18px' }),
      h('div', { class: 'kick' }, `${t('definedNotMeasured')} · ${without.length}`),
      h('div', { class: 'card' }, h('div', { class: 'items' }, without.map(id => {
        const def = defOf(id);
        return h('div', { class: 'item' }, h('code', { class: 'tag met' }, id),
          h('div', { class: 'txt' },
            h('div', { class: 'small', html: inline(stripMd(cell(def, 'definition', 'определение')).slice(0, 200)) }),
            h('div', { class: 'why' }, stripMd(cell(def, 'instrumentation', 'инструментирование')) || '—')));
      })))] : null);
}

/* ---------------------------------------------------------------- open questions */
function viewOpen() {
  const m = S.model;
  const byFile = {};
  m.gaps.forEach(g => { (byFile[g.file] = byFile[g.file] || []).push(g); });
  const openGate = m.steps.flatMap(s => s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown')
    .map(g => ({ step: s, g })));
  const hyp = m.registers.hypotheses.rows.filter(r =>
    /open|testing/i.test(stripMd(cell(r, 'status', 'статус'))));

  return h('div', { class: 'grid cols-2' },
    h('div', {},
      h('div', { class: 'kick' }, `${t('toClarify')} · ${m.gaps.length}`),
      Object.keys(byFile).length ? Object.entries(byFile).map(([file, gs]) =>
        h('div', { class: 'card', style: 'margin-bottom:12px' },
          h('div', { class: 'spread' }, h('h3', {}, file), h('span', { class: 'tag' }, gs.length)),
          h('div', { class: 'items' }, gs.map(g => h('div', { class: 'item' },
            h('button', { class: 'tag', style: 'cursor:pointer',
              onclick: () => { S.tab = 'artifacts'; S.artifact = file; S.section = g.section; render(); } },
              '#' + g.section),
            h('div', { class: 'txt md small', html: inline(g.line) }))))))
        : h('div', { class: 'empty' }, t('nothingOpen')),
      h('div', { class: 'kick', style: 'margin-top:14px' }, `${t('inFlight')} · ${hyp.length}`),
      h('div', { class: 'card' }, h('div', { class: 'items' }, hyp.map(r => h('div', { class: 'item' },
        h('code', { class: 'tag hyp' }, stripMd(cell(r, 'id'))),
        h('div', { class: 'txt' },
          h('div', { class: 'small', html: inline(stripMd(cell(r, 'hypothesis', 'гипотеза')).slice(0, 240)) }),
          h('div', { class: 'why' }, `${stripMd(cell(r, 'type', 'тип'))} · ${stripMd(cell(r, 'status', 'статус'))}`))))))),
    h('div', {},
      h('div', { class: 'kick' }, `${t('openGates')} · ${openGate.length}`),
      h('div', { class: 'card' }, h('div', { class: 'items' }, openGate.map(({ step, g }) =>
        h('div', { class: 'item' },
          h('button', { class: 'tag', style: 'cursor:pointer',
            onclick: () => { S.tab = 'step'; S.step = step.step; render(); } }, step.step),
          tickTag(g.tick),
          h('div', { class: 'txt' }, h('div', { class: 'small' }, g.label),
            h('div', { class: 'why mono tiny' }, (g.targets || []).join(' + ')))))))));
}

/* ---------------------------------------------------------------- skills */
function viewSkills() {
  const m = S.model;
  const skills = m.framework.skills || [];
  const planes = ['library', 'operations', 'adapters'];
  const shown = skills.filter(x => x.plane === S.skillPlane);
  const picked = shown.find(x => x.name === S.skillPick) || null;

  const tabs = h('div', { class: 'filters' },
    planes.map(p => h('button', { 'aria-pressed': S.skillPlane === p,
      onclick: () => { S.skillPlane = p; S.skillPick = null; S.skillFile = null; render(); } },
      `${p} · ${skills.filter(x => x.plane === p).length}`)));

  const grid = h('div', { class: 'skillgrid' }, shown.map(x => h('button', {
    class: 'card pick' + (picked && picked.name === x.name ? ' on' : ''),
    onclick: () => { S.skillPick = x.name; S.skillFile = null; render(); },
  },
    h('div', { class: 'spread' },
      h('h3', {}, x.name),
      h('span', { class: 'tag ' + (x.origin === 'local' ? 'done' : '') },
        x.origin === 'local' ? t('local') : t('vendored'))),
    h('div', { class: 'small muted clamp3', style: 'margin-top:5px' },
      (x.summary || '').replace(/^#+\s*[^\s]*\s*/, '')),
    h('div', { class: 'row tiny', style: 'margin-top:8px' },
      x.kind ? h('span', { class: 'tag' }, x.kind) : null,
      x.used_by_steps.length ? h('span', { class: 'tag' }, `${t('usedBy')} ${x.used_by_steps.join(',')}`) : null,
      x.produces.length && x.plane === 'library' ? h('code', { class: 'tag met' }, x.produces[0].slice(0, 26)) : null,
      x.homeless.length ? h('span', { class: 'tag err' }, 'homeless') : null))));

  const detail = picked ? h('div', { class: 'card' },
    h('div', { class: 'spread' }, h('h2', {}, picked.name),
      h('span', { class: 'row' },
        h('span', { class: 'tag' }, picked.plane),
        h('span', { class: 'tag' }, picked.origin === 'local' ? t('local') : t('vendored')),
        picked.version ? h('span', { class: 'tag' }, 'v' + picked.version) : null)),
    picked.summary ? h('div', { class: 'small muted', style: 'margin-top:6px' },
      picked.summary.replace(/^#+\s*[^\s]*\s*/, '')) : null,
    h('div', { class: 'wiring' }, [
      [t('produces'), picked.produces.join(' · ')],
      [t('usedBy'), picked.used_by_steps.join(', ')],
      [t('prerequisites'), picked.prerequisites.join(' · ')],
      [t('reads'), picked.reads_registers.join(' · ')],
      [t('writes'), picked.writes_registers.join(' · ')],
      [t('inputs'), picked.inputs.join(' · ')],
      ['method basis', picked.method_basis],
    ].filter(([, v]) => v).map(([k, v]) => h('div', { class: 'wrow' },
      h('div', { class: 'wk' }, k), h('div', { class: 'wv' }, v)))),
    h('div', { class: 'row', style: 'margin-top:11px' },
      h('button', { class: 'btn small',
        onclick: () => openSkillFile(picked, picked.plane === 'adapters' ? 'ADAPTER.md' : 'SKILL.md') },
        picked.plane === 'adapters' ? 'ADAPTER.md' : 'SKILL.md'),
      picked.has_fragment ? h('button', { class: 'btn small',
        onclick: () => openSkillFile(picked, 'template-fragment.md') }, t('fragment')) : null,
      picked.has_questions ? h('button', { class: 'btn small',
        onclick: () => openSkillFile(picked, 'questions.yaml') }, t('interview')) : null),
    S.skillFile ? h('div', { class: 'filebox' },
      h('div', { class: 'spread' }, h('code', { class: 'tiny' }, S.skillFile.name),
        h('button', { class: 'tag', style: 'cursor:pointer',
          onclick: () => { S.skillFile = null; render(); } }, '×')),
      h('pre', {}, S.skillFile.text)) : null) : null;

  return h('div', {}, tabs,
    h('div', { class: 'small muted', style: 'margin:0 0 12px' }, t('addSkillHint')),
    detail ? h('div', { class: 'grid cols-2' }, grid, detail) : grid);
}

async function openSkillFile(skill, name) {
  const r = await fetch('/api/file?path=' + encodeURIComponent(skill.dir + '/' + name));
  S.skillFile = { name, text: r.ok ? await r.text() : '—' };
  render();
}

/* ---------------------------------------------------------------- log & checks */
function viewLog() {
  const m = S.model;
  if (!m.timeline.length) {
    return h('div', { class: 'note warn' }, h('span', { class: 'who' }, '—'), h('div', {}, t('nothingYet')));
  }
  return h('div', { class: 'card' }, h('div', { class: 'tl' }, m.timeline.map(e => h('div', { class: 'e' },
    h('div', {}, h('div', { class: 'd' }, e.date), h('div', { class: 'tiny faint mono' }, e.file)),
    h('div', {}, h('div', { class: 's' }, e.summary), h('div', { class: 'b md', html: md(e.body) }))))));
}

function viewChecks() {
  const m = S.model, lint = S.lint;
  const lintBox = !lint ? h('div', { class: 'empty' }, '…')
    : !lint.ok ? h('div', { class: 'note error' }, h('span', { class: 'who' }, 'error'), h('div', {}, lint.error))
      : lint.findings.length ? h('div', { class: 'notes' }, lint.findings.map(f =>
        h('div', { class: 'note ' + f.level },
          h('span', { class: 'who' }, `${f.level} ${f.check}`),
          h('div', {}, f.scope ? h('code', { class: 'tiny' }, f.scope + ' ') : null, f.message))))
        : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('lintClean')));

  return h('div', { class: 'grid cols-2' },
    h('div', {},
      h('div', { class: 'kick' }, `${t('healthTitle')} · `
        + `${m.health.filter(x => x.level === 'error').length} error · `
        + `${m.health.filter(x => x.level === 'warn').length} warn`),
      m.health.length ? h('div', { class: 'notes' }, m.health.map(x => h('div', { class: 'note ' + x.level },
        h('span', { class: 'who' }, x.level), h('div', {}, x.message))))
        : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('healthClean')))),
    h('div', {},
      h('div', { class: 'kick' }, t('lintTitle')), lintBox,
      h('div', { style: 'height:14px' }),
      h('div', { class: 'card' }, h('div', { class: 'kick' }, t('notChecked')),
        h('div', { class: 'small muted' }, t('notCheckedBody')))));
}

const VIEWS = { overview: viewOverview, step: viewStep, artifacts: viewArtifacts, registers: viewRegisters,
  metrics: viewMetrics, open: viewOpen, skills: viewSkills, log: viewLog, checks: viewChecks };

/* ---------------------------------------------------------------- shell */
function renderInto(sel, node) {
  const host = document.querySelector(sel);
  if (host) host.replaceChildren(node);
}
function renderKids(sel, nodes) {
  const host = document.querySelector(sel);
  if (host) host.replaceChildren(...nodes.flat(9).filter(Boolean));
}

function counts() {
  const m = S.model;
  const openGates = m.steps.reduce((a, s) =>
    a + s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown').length, 0);
  const lintN = S.lint && S.lint.findings ? S.lint.findings.filter(f => f.level === 'error').length : 0;
  return {
    artifacts: m.artifacts.length || null,
    registers: m.registers.hypotheses.rows.length + m.registers.risks.rows.length
      + m.registers.metric_tree.rows.length,
    metrics: Object.keys(m.metrics.series).length || null,
    open: m.gaps.length + openGates || null,
    skills: (m.framework.skills || []).length || null,
    log: m.timeline.length || null,
    checks: (m.health.filter(x => x.level === 'error').length + lintN) || null,
  };
}

function writeHash() {
  const parts = [S.tab];
  if (S.tab === 'step' && S.step) parts.push(S.step);
  if (S.tab === 'artifacts' && S.artifact) parts.push(S.artifact, S.section || '');
  if (S.tab === 'registers') parts.push(S.reg);
  if (S.tab === 'skills') parts.push(S.skillPlane, S.skillPick || '');
  const want = '#' + parts.filter(x => x !== '' && x !== null && x !== undefined).join('/');
  if (location.hash !== want) history.replaceState(null, '', want);
}
function readHash() {
  const p = decodeURIComponent(location.hash.replace(/^#/, '')).split('/');
  if (!p[0] || !VIEWS[p[0]]) return;
  S.tab = p[0];
  if (S.tab === 'step' && p[1]) S.step = +p[1];
  if (S.tab === 'artifacts' && p[1]) { S.artifact = p[1]; S.section = p[2] || null; }
  if (S.tab === 'registers' && p[1]) S.reg = p[1];
  if (S.tab === 'skills') { if (p[1]) S.skillPlane = p[1]; if (p[2]) S.skillPick = p[2]; }
}

function render() {
  const m = S.model;
  if (!m) return;
  writeHash();
  document.documentElement.lang = m.language || 'en';
  document.getElementById('product').textContent = m.product;
  document.getElementById('subline').textContent = m.name + ' · ' + m.path;

  const c = counts();
  renderKids('#chips', [
    h('div', { class: 'chip' }, h('b', {}, t('status')), h('div', { class: 'v' }, m.active_status || '—')),
    h('div', { class: 'chip' }, h('b', {}, t('step')),
      h('div', { class: 'v' }, m.current_step ? `${m.current_step} / 6` : t('noState'))),
    h('div', { class: 'chip pick' },
      h('select', { onchange: e => load(e.target.value) },
        S.instances.map(i => h('option', { value: i.path, selected: i.path === m.path },
          `${i.name} · ${i.kind}`)))),
    h('input', { class: 'pathin', placeholder: t('addHint'), title: t('addFolder'),
      onkeydown: e => { if (e.key === 'Enter') addFolder(e.target.value); } }),
    h('button', { class: 'themebtn', title: t('theme'),
      onclick: () => { applyTheme(THEMES[(THEMES.indexOf(theme()) + 1) % 3]); render(); } },
      h('span', { class: 'ico' }, theme() === 'auto' ? '◐' : theme() === 'light' ? '☀' : '☾'),
      t('theme' + theme())),
  ]);

  renderKids('#tabs', Object.keys(VIEWS).map(k => h('button', {
    'aria-current': S.tab === k, onclick: () => { S.tab = k; render(); },
  }, t('tabs.' + k), c[k] ? h('span', { class: 'count' }, c[k]) : null)));

  try {
    renderInto('#view', VIEWS[S.tab]());
  } catch (e) {
    renderInto('#view', h('div', { class: 'note error' }, h('span', { class: 'who' }, 'ui'),
      h('div', {}, `${e.name}: ${e.message}`)));
    throw e;
  }
  document.getElementById('footpath').innerHTML = `<b>${esc(m.path)}</b>`;
  document.getElementById('footrev').textContent = t('readOnly');
}

async function addFolder(raw) {
  if (!raw || !raw.trim()) return;
  const j = await (await fetch('/api/add?path=' + encodeURIComponent(raw.trim()))).json();
  if (j.error) {
    renderInto('#view', h('div', { class: 'note error' }, h('span', { class: 'who' }, 'folder'),
      h('div', {}, j.error)));
    return;
  }
  S.instances = j.instances;
  await load(j.current);
}

async function load(instancePath) {
  const url = '/api/model' + (instancePath ? '?instance=' + encodeURIComponent(instancePath) : '');
  const j = await (await fetch(url)).json();
  if (j.error) {
    renderInto('#view', h('div', { class: 'note error' }, h('span', { class: 'who' }, 'server'),
      h('div', {}, j.error)));
    return;
  }
  const switched = !S.model || S.model.path !== j.model.path;
  S.model = j.model;
  S.rev = j.rev;
  if (switched) {
    if (!S.step) S.step = S.model.current_step || (S.model.steps[0] || {}).step || 1;
    S.skillFile = null;
  }
  render();
  fetch('/api/lint').then(x => x.json()).then(l => { S.lint = l; render(); }).catch(() => {});
}

async function boot() {
  applyTheme();
  readHash();                       // before the first render: writeHash() would overwrite the deep link
  window.addEventListener('hashchange', () => { readHash(); render(); });
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => render());
  const inst = await (await fetch('/api/instances')).json();
  S.instances = inst.instances || [];
  await load();
  if (new URLSearchParams(location.search).get('live') === '0') return;
  const es = new EventSource('/api/events');
  es.onmessage = ev => {
    const rev = +ev.data;
    if (S.rev >= 0 && rev !== S.rev) {
      document.getElementById('footrev').textContent = t('changed');
      load(S.model && S.model.path);
    }
    S.rev = rev;
  };
}

boot();
