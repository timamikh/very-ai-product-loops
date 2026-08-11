/* very-ai-product-loops · local console
 *
 * Renders the read model served by tools/ui/serve.py. No build step, no dependencies: a product
 * manager runs `python3 tools/ui/serve.py` and sees their product. The canon is never re-interpreted
 * here — everything shown comes from tools/loops/ (one parser), and this file only lays it out.
 *
 * Three rules this file holds to, because breaking them is what made the earlier version noisy:
 *
 *  1. **Never a cut sentence.** Prose is shown whole, inside something that can be opened and
 *     closed, or it is not shown at all. A card that carries the first 84 characters of a definition
 *     tells the reader nothing and costs them a line of attention.
 *  2. **A number, a label, or a link — pick one per element.** The overview answers "where are we"
 *     in figures and rules; the detail lives one click away, in a table or an accordion.
 *  3. **No glyph we cannot guarantee.** No web fonts, no emoji, no box-drawing: a shared snapshot is
 *     opened on machines we know nothing about, and a missing glyph renders as a tofu box. The
 *     canon's own ⚙️ marker becomes a word in a badge.
 *
 * Interface language follows the instance: `config.yaml` → `language`. Adding a locale means adding
 * one object to STR below — nothing else in this file knows a language exists.
 *
 * The same file renders the exported snapshot: when `window.__SNAPSHOT__` is present the model and
 * the linter's verdict are already embedded, and every fetch, the live reload and the folder picker
 * are switched off. One renderer, two ways in.
 */
'use strict';

/* ---------------------------------------------------------------- strings */
const STR = {
  en: {
    tabs: { overview: 'Overview', step: 'Step', artifacts: 'Artifacts', registers: 'Registers',
      metrics: 'Metrics', open: 'Open questions', sources: 'Sources', skills: 'Skills',
      log: 'Change log', checks: 'Checks' },
    status: 'status', step: 'step', of: 'of', lastPass: 'last pass',
    noState: 'not recorded', theme: 'theme', themeauto: 'auto', themelight: 'light', themedark: 'dark',
    addFolder: 'Add a product folder', addHint: 'add a folder…',
    saveHtml: 'Save as HTML',
    saveHint: 'One self-contained file for this product, frozen at this moment. It carries everything '
      + 'the artifacts carry, so send it only to people who may read them.',
    snapshot: 'Snapshot', snapshotNote: 'a frozen copy — it does not follow the product folder',
    madeOn: 'taken on', readOnlySnap: 'read-only copy',
    cascade: 'The six steps', instanceReading: 'How this instance reads', product: 'Product',
    cadence: 'cadence', artifact: 'artifact', filled: 'written', sections: 'sections',
    sectionsTitle: 'Sections', whatElseCol: 'what it is',
    colType: 'type', colDefinition: 'definition', colStatement: 'statement',
    gate: 'The gate', gateItem: 'gate item', gateDone: 'closed', gateOpen: 'open', gateNa: 'n/a',
    gateDeferred: 'deferred', gateUnknown: 'unrecorded', gateClosed: 'gate closed',
    words: 'words', gaps: 'gaps', proposals: 'agent proposals', proposalMark: 'proposed',
    notWritten: 'not written yet', offSkeleton: 'outside the skeleton', validates: 'validates',
    statusAsks: 'What the active status asks here', emphasised: 'emphasised for this stage',
    fillWith: 'fill through', rows: 'rows', state: 'state',
    hypotheses: 'Hypotheses', risks: 'Risks', metricNodes: 'Metric nodes', readings: 'readings',
    withReadings: 'measured', csvRows: 'csv rows', referencedIn: 'referenced in',
    live: 'live', testing: 'in test', inFlightShort: 'in flight',
    toClarify: 'To clarify', openGates: 'Gate items still open', inFlight: 'Hypotheses in flight',
    latest: 'Latest readings', series: 'Series', allReadings: 'All readings',
    trail: 'trail', trailHint: 'every change-log entry that names this id',
    trailEmpty: 'No change-log entry names this id yet.',
    observedNote: 'a rate is read against observed_n, not the whole population',
    definedNotMeasured: 'Defined, never measured', notInTree: 'not defined in metric-tree.md',
    noReadings: 'No reading has been recorded yet: the nodes are defined, metrics.csv carries no rows. '
      + 'A metric with no reading cannot move a decision.',
    vsPrev: 'vs previous', basisNote: 'compared within the same basis and population',
    nothingOpen: 'Nothing open here.', nothingYet: 'Nothing here yet.', all: 'all',
    search: 'search…', lintTitle: 'Canon linter', healthTitle: 'Instance reading',
    lintClean: 'The linter reports no findings.', healthClean: 'Reads cleanly against the canon.',
    notChecked: 'Checked by neither', notCheckedBody: 'Prose quality, whether register values are true '
      + '(only their enums and ids are checked), prerequisite completeness, adapter fidelity — and '
      + 'nothing here judges product decisions. The console reports; the human decides.',
    changed: 'the folder changed — reloading',
    readOnly: 'read-only — the agent writes the files, this shows what they say',
    subProducts: 'Sub-products', umbrellaNote: 'This folder is an umbrella: the shared config and sources '
      + 'live here, and each product below keeps its own artifacts, state and registers.',
    openIt: 'open', plane: 'plane', vendored: 'framework', local: 'this product',
    produces: 'produces', usedBy: 'steps', prerequisites: 'prerequisites', reads: 'reads', writes: 'writes',
    inputs: 'inputs', interview: 'interview', fragment: 'section template',
    addSkillHint: 'To add or change a skill, ask the agent — it writes the canon’s anatomy into this '
      + 'product’s own tool-skills folder, and a product-local skill wins over a vendored one of the '
      + 'same name. It appears here on the next read. See EXTENDING.md.',
    handoff: 'Session handoff', sourcesTab: 'sources', deliverables: 'Deliverables',
    whatElse: 'What else is in this folder', nextPass: 'Where the next pass goes',
    nextPassNone: 'Every gate item is recorded and closed.',
    goal: 'Goal', scope: 'Scope', audience: 'Audience', directions: 'Directions',
    openSection: 'open', file: 'file', updated: 'updated', role: 'role', indexed: 'in the index',
    sourceIndex: 'The source index', sourceFiles: 'Files in sources/',
    notIndexed: 'not in INDEX.md', changeLog: 'Change log', entries: 'entries',
    openHypotheses: 'open', of6: 'of 6',
    colName: 'skill', colKind: 'kind', origin: 'origin',
  },
  ru: {
    tabs: { overview: 'Обзор', step: 'Шаг', artifacts: 'Артефакты', registers: 'Реестры',
      metrics: 'Метрики', open: 'Открытые вопросы', sources: 'Источники', skills: 'Скиллы',
      log: 'Журнал', checks: 'Проверки' },
    status: 'статус', step: 'шаг', of: 'из', lastPass: 'последний проход',
    noState: 'не зафиксирован', theme: 'тема', themeauto: 'авто', themelight: 'светлая', themedark: 'тёмная',
    addFolder: 'Добавить папку продукта', addHint: 'добавить папку…',
    saveHtml: 'Скачать HTML',
    saveHint: 'Один файл по этому продукту, замороженный на этот момент. В нём есть всё, что есть в '
      + 'артефактах, — отправляйте только тем, кому их можно читать.',
    snapshot: 'Снимок', snapshotNote: 'замороженная копия — за папкой продукта не следит',
    madeOn: 'снят', readOnlySnap: 'копия только для чтения',
    cascade: 'Шесть шагов', instanceReading: 'Как читается инстанс', product: 'Продукт',
    cadence: 'ритм', artifact: 'артефакт', filled: 'написано', sections: 'секций',
    sectionsTitle: 'Секции', whatElseCol: 'что это',
    colType: 'тип', colDefinition: 'определение', colStatement: 'формулировка',
    gate: 'Гейт', gateItem: 'пункт гейта', gateDone: 'закрыто', gateOpen: 'открыто',
    gateNa: 'не применимо', gateDeferred: 'отложено', gateUnknown: 'не зафиксировано',
    gateClosed: 'гейт закрыт',
    words: 'слов', gaps: 'пробелов', proposals: 'предложения агента', proposalMark: 'предложение',
    notWritten: 'ещё не написано', offSkeleton: 'вне скелета', validates: 'проверяет',
    statusAsks: 'Что просит активный статус на этом шаге', emphasised: 'выделено для этой стадии',
    fillWith: 'заполнять через', rows: 'строк', state: 'состояние',
    hypotheses: 'Гипотезы', risks: 'Риски', metricNodes: 'Узлы метрик', readings: 'показаний',
    withReadings: 'измеряется', csvRows: 'строк в csv', referencedIn: 'упоминается в',
    live: 'в работе', testing: 'на проверке', inFlightShort: 'в работе',
    toClarify: 'На уточнение', openGates: 'Незакрытые пункты гейта', inFlight: 'Гипотезы в работе',
    latest: 'Последние значения', series: 'Ряды', allReadings: 'Все показания',
    trail: 'след', trailHint: 'все записи журналов, которые называют этот идентификатор',
    trailEmpty: 'Ни одна запись журнала пока не называет этот идентификатор.',
    observedNote: 'доля считается от observed_n, а не от всей популяции',
    definedNotMeasured: 'Определены, но не измеряются', notInTree: 'нет определения в metric-tree.md',
    noReadings: 'Пока нет ни одного показания: узлы определены, в metrics.csv нет строк. '
      + 'Метрика без показаний не может ничего решить.',
    vsPrev: 'к предыдущему', basisNote: 'сравнение внутри одного basis и одной population',
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
    handoff: 'Передача сессии', sourcesTab: 'источников', deliverables: 'Поставляемое',
    whatElse: 'Что ещё лежит в папке', nextPass: 'Куда идёт следующий проход',
    nextPassNone: 'Все пункты гейтов зафиксированы и закрыты.',
    goal: 'Цель', scope: 'Рамки', audience: 'Аудитория', directions: 'Направления',
    openSection: 'открыть', file: 'файл', updated: 'обновлён', role: 'роль', indexed: 'в индексе',
    sourceIndex: 'Индекс источников', sourceFiles: 'Файлы в sources/',
    notIndexed: 'нет в INDEX.md', changeLog: 'Журнал изменений', entries: 'записей',
    openHypotheses: 'открытых', of6: 'из 6',
    colName: 'скилл', colKind: 'вид', origin: 'происхождение',
  },
};

/* ---------------------------------------------------------------- state */
const S = {
  model: null, lint: null, instances: [], rev: -1, snapshot: null,
  tab: 'overview', step: null, artifact: null, section: null,
  reg: 'hypotheses', regFilter: 'all', regSearch: '', regItem: null,
  skillPlane: 'library', skillPick: null, skillFile: null, logFile: 'all',
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

/* Chart series colors: a validated categorical palette per mode. The house hues (one pure red and a
 * grey scale) cannot separate three series for a colourblind reader, so they stay in the chrome and
 * the plot borrows a set that passes the checks against both surfaces. */
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
  s = s.replace(/`([^`]+)`/g, (_, c) => { code.push(c); return ` ${code.length - 1} `; });
  s = s.replace(/\[([^\]]+)\]\((#?[^)\s]+)\)/g, (_, x, u) => `<a href="${u}" target="_blank" rel="noopener">${x}</a>`);
  s = s.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>').replace(/(^|[\s(])\*([^*]+)\*/g, '$1<em>$2</em>');
  s = s.replace(/(^|[\s(])_([^_]+)_(?=$|[\s.,;:)])/g, '$1<em>$2</em>');
  s = s.replace(/\[(assumption|sourced|validated|refuted)((?::)([^\]]*))?\]/g,
    (_, kind, __, rest) => `<span class="conf ${kind}">${kind}${rest ? ': ' + rest.trim() : ''}</span>`);
  s = s.replace(/—\s*(to clarify|уточнить)\s*—/g, '<span class="gapmark">— $1 —</span>');
  // the canon's agent-proposal marker, rendered as a word: an emoji is a font gamble, and this page
  // is also read as an exported file on a machine whose fonts we know nothing about
  s = s.replace(/⚙️?\s*/g, `<span class="gear">${esc(t('proposalMark'))}</span> `);
  s = s.replace(/ (\d+) /g, (_, i) => {
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
      // Fill under one line only. Two translucent fills over each other make a third colour that
      // belongs to neither series, and the reader has to work out which is on top.
      if (groups.length === 1) {
        s.append(svg('path', {
          d: `M${pts[0].x.toFixed(1)} ${(H - P.b).toFixed(1)} L`
            + pts.map(p => `${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' L')
            + ` L${pts[pts.length - 1].x.toFixed(1)} ${(H - P.b).toFixed(1)} Z`,
          fill: color, opacity: 0.1, stroke: 'none',
        }));
      }
    }
    // A dot on every reading: the line is drawn between measurements, and which points were actually
    // measured is the fact the reader needs — a hover that has to be hunted for does not tell them.
    // The ring is the panel's own colour, so two series crossing stay two dots, not one blob.
    const gap = xs.length > 1 ? (W - P.l - P.r) / (xs.length - 1) : W;
    const dotR = gap < 9 ? 2 : gap < 16 ? 2.6 : 3.2;
    const last = pts[pts.length - 1];
    pts.forEach(p => {
      p.baseR = p === last ? Math.max(dotR + 1.2, 4) : dotR;
      p.dot = svg('circle', { cx: p.x, cy: p.y, r: p.baseR, fill: color,
        stroke: 'var(--paper)', 'stroke-width': dotR < 2.6 ? 1 : 1.5 });
      s.append(p.dot);
    });
    // The last value, and only the value: the basis it was measured on is named once, in the legend.
    // A label that carries it too runs off the panel and gets cut — the one thing the layout forbids.
    const lab = svg('text', { x: last.x + 7, y: last.y + 3.5, fill: 'var(--muted)',
      'font-size': 10, 'font-family': 'var(--mono)' });
    lab.textContent = num(last.r.value);
    s.append(lab);
    pts.forEach(p => {
      const hit = svg('circle', { cx: p.x, cy: p.y, r: 9, fill: 'transparent', style: 'cursor:crosshair' });
      hit.addEventListener('mouseenter', () => p.dot.setAttribute('r', p.baseR + 2));
      hit.addEventListener('mousemove', ev => showTip(
        `<b>${esc(num(p.r.value))}</b> ${esc(opts.unit || '')}<br>`
        + `<span class="k">${esc(dateOf(p.r))}</span>`
        + (p.r.period_start ? ` <span class="k">(${esc(p.r.period_start)} → ${esc(p.r.period_end)})</span>` : '')
        + (g.label && groups.length > 1 ? `<br><span class="k">basis</span> ${esc(g.label)}` : '')
        + (p.r.source ? `<br><span class="k">source</span> ${esc(p.r.source)}` : '')
        + (p.r.note ? `<br>${esc(p.r.note)}` : ''), ev.clientX, ev.clientY));
      hit.addEventListener('mouseleave', () => { p.dot.setAttribute('r', p.baseR); hideTip(); });
      s.append(hit);
    });
  });
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
const gateSummary = s => `${(s.gate_counts || {}).done || 0}/${s.gate.length} ${t('gateDone')}`;
const confChips = conf => Object.entries(conf || {}).map(([k, n]) =>
  h('span', { class: 'tag ' + k }, `${k} ×${n}`));
const ridClass = x => /^H-/.test(x) ? 'hyp' : /^R-/.test(x) ? 'risk' : 'met';
const ridChips = ids => (ids || []).map(x => h('span', { class: 'tag ' + ridClass(x) }, x));

/* A section heading — an eyebrow number, a title, and one line of context on the right. Every block
 * on every tab wears one, so a page reads as a document with parts rather than a wall of cards. */
function secHead(title, opts) {
  const o = opts || {};
  return h('div', { class: 'sechead' },
    h('h2', {}, title),
    o.n ? h('span', { class: 'n' }, o.n) : null,
    o.right ? h('div', { class: 'right' }, o.right) : null);
}
const sec = (title, opts, ...body) => h('section', { class: 'sec' }, secHead(title, opts), ...body);

/* The console's main verb: go and read the thing itself. Every place that names a section offers it. */
function goSection(file, id, label, title) {
  // The chip reads `1#concept`; the tooltip spells out the human section name, so a reader who does
  // not decode the step-number shorthand still learns where the link goes without following it.
  return h('button', {
    class: 'golink', title: title ? `${title} — ${file}#${id}` : `${file}#${id}`,
    onclick: e => { e.stopPropagation(); S.tab = 'artifacts'; S.artifact = file; S.section = id; render(); },
  }, label || t('openSection'));
}
function goStep(n, label) {
  return h('button', {
    class: 'golink',
    onclick: e => { e.stopPropagation(); S.tab = 'step'; S.step = n; render(); },
  }, label || `${t('step')} ${n}`);
}

/* A table, built once and used everywhere: cols is [label, …], rows is [[cell, …], …]. */
function table(cols, rows, opts) {
  const o = opts || {};
  return h('div', { class: 'tablewrap' }, h('table', {},
    h('thead', {}, h('tr', {}, cols.map((c, i) => h('th', { title: (o.titles || [])[i] || null }, c)))),
    h('tbody', {}, rows.length ? rows
      : [h('tr', {}, h('td', { colspan: cols.length, class: 'faint' }, o.empty || t('nothingYet')))])));
}
/* An accordion: whole text, closed by default. The alternative — a card showing the first two lines
 * of it — is what made the old console read as rubble. */
function acc(summaryKids, bodyKids, open) {
  return h('details', { class: 'acc', open: !!open },
    h('summary', {}, ...summaryKids),
    h('div', { class: 'accbody' }, ...bodyKids));
}
const figures = tiles => h('div', { class: 'figs' }, tiles.filter(Boolean));
function fig(label, value, sub, onclick, alert) {
  return h(onclick ? 'button' : 'div', { class: 'fig' + (alert ? ' alert' : ''), onclick },
    h('div', { class: 'l' }, label),
    h('div', { class: 'v' }, value),
    sub ? h('div', { class: 's' }, sub) : null);
}

/* Which artifact section actually holds this step section's text (the step model carries counts, the
 * artifact carries the body — and the body is what a reader wants when they open a row). */
function artSection(file, id) {
  const a = (S.model.artifacts || []).find(x => x.file === file);
  return a ? (a.sections || []).find(x => x.id === id) : null;
}
/* A `— to clarify —` found inside a table comes back as the whole markdown row, pipes and all. Read
 * as prose it is noise; the cells joined by a separator say the same thing and can be read. */
const gapText = line => (/^\s*\|/.test(line)
  ? line.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim()).filter(Boolean).join(' · ')
  : line);
/* `1#concept` — the step number plus the anchor. Short enough for a table cell, and unambiguous:
 * four artifacts have a section called `hypotheses`, and a bare `#hypotheses` names none of them. */
const refLabel = x => `${(x.file.match(/^\d+/) || [''])[0]}#${x.id}`;
/* Every artifact section that names a register id, assembled from the markers the reader already
 * collected — so a hypothesis row can point at the places it is actually argued. */
function refIndex() {
  if (S.model._refs) return S.model._refs;
  const out = {};
  (S.model.artifacts || []).forEach(a => (a.sections || []).forEach(s => {
    const mk = s.markers || {};
    [].concat(mk.hypotheses || [], mk.risks || [], mk.metrics || []).forEach(id => {
      (out[id] = out[id] || []).push({ file: a.file, id: s.id, title: s.title || s.id });
    });
  }));
  Object.keys(out).forEach(k => {
    const seen = new Set();
    out[k] = out[k].filter(x => !seen.has(x.file + x.id) && seen.add(x.file + x.id));
  });
  S.model._refs = out;
  return out;
}

/* ---------------------------------------------------------------- overview */
function viewOverview() {
  const m = S.model;
  if (m.umbrella) return viewUmbrella();
  const reg = m.registers;
  const gateAll = m.steps.reduce((a, s) => a + s.gate.length, 0);
  const gateDone = m.steps.reduce((a, s) => a + (s.gate_counts.done || 0), 0);
  const openGates = m.steps.reduce((a, s) =>
    a + s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown').length, 0);
  const hStatus = k => reg.hypotheses.rows.filter(r =>
    stripMd(cell(r, 'status', 'статус')).toLowerCase().startsWith(k)).length;
  const risksLive = reg.risks.rows.filter(r =>
    /open|mitigat|открыт|митиг/i.test(stripMd(cell(r, 'status', 'статус')))).length;
  const measured = Object.keys(m.metrics.series).length;
  const nextStep = m.steps.find(s => (s.gate_counts.open || 0) + (s.gate_counts.unknown || 0) > 0);
  const nextItem = nextStep && nextStep.gate.find(g => g.tick === 'open' || g.tick === 'unknown');

  // The thesis: what this product is and where the cycle stands, in whole sentences.
  const thesis = h('div', { class: 'sec' },
    h('div', { class: 'kick' }, `${t('product')} · ${m.active_status || '—'}`),
    h('h2', { style: 'font-size:29px;letter-spacing:-.03em;line-height:1.15' }, m.product),
    m.goal ? h('p', { class: 'lead', style: 'margin-top:10px' }, m.goal) : null,
    h('div', { class: 'figs', style: 'margin-top:18px' },
      fig(t('step'), m.current_step ? String(m.current_step) : '—',
        m.current_step ? `${t('of6')}${m.last_pass ? ' · ' + t('lastPass') + ' ' + m.last_pass : ''}`
          : t('noState'),
        m.current_step ? () => { S.tab = 'step'; S.step = m.current_step; render(); } : null),
      fig(t('gateClosed'), `${gateDone}`, `${t('of')} ${gateAll}`),
      fig(t('toClarify'), String(m.gaps.length),
        openGates ? `${openGates} ${t('openGates').toLowerCase()}` : '',
        () => { S.tab = 'open'; render(); }, m.gaps.length > 0),
      fig(t('hypotheses'), String(reg.hypotheses.rows.length),
        `${hStatus('open')} ${t('openHypotheses')} · ${hStatus('testing')} ${t('testing')}`,
        () => { S.tab = 'registers'; S.reg = 'hypotheses'; render(); }),
      fig(t('risks'), String(reg.risks.rows.length), `${risksLive} ${t('live')}`,
        () => { S.tab = 'registers'; S.reg = 'risks'; render(); }),
      fig(t('metricNodes'), String(reg.metric_tree.rows.length),
        `${measured} ${t('withReadings')}`, () => { S.tab = 'metrics'; render(); })));

  const next = h('div', { class: 'panel' },
    h('div', { class: 'kick' }, t('nextPass')),
    nextStep ? h('div', {},
      h('div', { class: 'row', style: 'align-items:baseline' },
        h('span', { style: 'font-family:var(--mono);font-size:30px;font-weight:700;color:var(--brand-ink)' },
          nextStep.step),
        h('b', { style: 'font-size:14px' }, shortTitle(nextStep.title || ''))),
      nextItem ? h('p', { class: 'small muted', style: 'margin-top:8px' }, nextItem.label) : null,
      h('div', { class: 'row', style: 'margin-top:10px' }, goStep(nextStep.step)))
      : h('p', { class: 'small muted' }, t('nextPassNone')));

  const health = m.health.length
    ? h('div', { class: 'notes' }, m.health.slice(0, 4).map(x => h('div', { class: 'note ' + x.level },
      h('span', { class: 'who' }, x.level), h('div', {}, x.message))))
    : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('healthClean')));

  const cascade = table(
    ['#', t('tabs.step'), t('artifact'), t('sections'), t('gate'), ''],
    m.steps.map(s => {
      const written = s.sections.filter(x => x.present).length;
      const here = m.current_step === s.step;
      return h('tr', {},
        h('td', { class: 'id' }, h('b', { style: here ? 'color:var(--brand-ink)' : null }, s.step)),
        h('td', {}, h('div', { style: 'font-weight:650' }, shortTitle(s.title || s.name)),
          h('div', { class: 'tiny muted' }, s.cadence || '')),
        h('td', { class: 'id' }, s.artifact_file
          ? h('code', {}, s.artifact_file)
          : h('span', { class: 'faint' }, s.output || '—')),
        h('td', { class: 'num' }, `${written}/${s.sections.length}`),
        h('td', { style: 'min-width:150px' }, gateBar(s.gate_counts),
          h('div', { class: 'tiny muted', style: 'margin-top:4px' }, gateSummary(s))),
        h('td', { class: 'act' }, goStep(s.step, t('openSection'))));
    }));

  const elseRows = [];
  if (m.handoff.present) {
    elseRows.push(h('tr', {}, h('td', { class: 'id' }, h('code', {}, 'HANDOFF.md')),
      h('td', {}, t('handoff')), h('td', { class: 'id faint' }, m.handoff.updated || '—')));
  }
  elseRows.push(h('tr', {}, h('td', { class: 'id' }, h('code', {}, 'sources/')),
    h('td', {}, `${m.sources.files.length} ${t('sourcesTab')}`),
    h('td', { class: 'act' }, h('button', { class: 'golink',
      onclick: () => { S.tab = 'sources'; render(); } }, t('openSection')))));
  if (m.deliverables.length) {
    elseRows.push(h('tr', {}, h('td', { class: 'id' }, h('code', {}, 'deliverables/')),
      h('td', {}, m.deliverables.join(' · ')), h('td', {})));
  }
  if (m.directions.length) {
    elseRows.push(h('tr', {}, h('td', { class: 'id' }, h('code', {}, 'directions')),
      h('td', {}, m.directions.join(' · ')), h('td', {})));
  }

  return h('div', {},
    thesis,
    h('div', { class: 'grid cols-2' },
      sec(t('cascade'), { right: `${gateDone}/${gateAll} ${t('gateDone')}` }, cascade),
      h('div', { style: 'align-self:start' },
        h('div', { class: 'sec' }, next),
        sec(t('instanceReading'), {}, health))),
    m.scope_note ? sec(t('scope'), {}, h('div', { class: 'panel md', html: md(m.scope_note) })) : null,
    sec(t('whatElse'), {}, table([t('file'), t('whatElseCol'), ''], elseRows)));
}

function viewUmbrella() {
  const m = S.model;
  return h('div', {},
    h('div', { class: 'sec' },
      h('div', { class: 'kick' }, t('product')),
      h('h2', { style: 'font-size:29px;letter-spacing:-.03em' }, m.product),
      h('p', { class: 'lead', style: 'margin-top:10px' }, t('umbrellaNote')),
      m.scope_note ? h('p', { class: 'small muted', style: 'margin-top:10px' }, m.scope_note) : null),
    sec(t('subProducts'), { right: `${m.children.length}` },
      table([t('product'), ''], m.children.map(name => {
        const cand = S.instances.find(i => i.name === name && i.path.startsWith(m.path));
        return h('tr', {}, h('td', {}, h('b', {}, name)),
          h('td', { class: 'act' }, cand ? h('button', { class: 'golink', onclick: () => load(cand.path) },
            t('openIt')) : null));
      }))));
}

/* ---------------------------------------------------------------- the step */
function viewStep() {
  const m = S.model;
  if (!m.steps.length) return h('div', { class: 'empty' }, t('nothingYet'));
  const s = m.steps.find(x => x.step === S.step) || m.steps[0];
  S.step = s.step;
  const perStep = (m.status && m.status.per_step && m.status.per_step[String(s.step)]) || null;
  const emph = new Set((perStep && perStep.tools) || []);
  const written = s.sections.filter(x => x.present).length;
  const gaps = s.sections.reduce((a, x) => a + (x.gaps || 0), 0);
  const proposals = s.sections.reduce((a, x) => a + (x.proposals || 0), 0);

  const head = h('div', { class: 'sec' },
    h('div', { class: 'kick' }, `${t('step')} ${s.step} ${t('of6')} · ${s.cadence || ''}`),
    h('h2', { style: 'font-size:25px;letter-spacing:-.025em' }, shortTitle(s.title || s.name)),
    s.goal ? h('p', { class: 'lead', style: 'margin-top:9px' }, s.goal) : null,
    h('div', { class: 'figs', style: 'margin-top:16px' },
      fig(t('filled'), `${written}`, `${t('of')} ${s.sections.length} ${t('sections')}`),
      fig(t('gateClosed'), `${(s.gate_counts.done || 0)}`, `${t('of')} ${s.gate.length}`),
      fig(t('toClarify'), String(gaps), gaps ? t('gaps') : '', null, gaps > 0),
      fig(t('proposals'), String(proposals), ''),
      s.artifact_file ? fig(t('artifact'), h('span', { style: 'font-size:14px;font-family:var(--mono)' },
        s.artifact_file), s.artifact_updated || '') : null));

  const sections = h('div', {}, s.sections.map(x => {
    const gate = s.gate.find(g => (g.sections || []).includes(x.id));
    const body = x.present ? artSection(s.artifact_file, x.id) : null;
    return acc([
      h('span', { class: 'sumtitle' }, x.title || x.id),
      h('code', { class: 'tag' }, '#' + x.id),
      h('span', { class: 'summeta' },
        x.off_skeleton ? h('span', { class: 'tag' }, t('offSkeleton')) : null,
        x.present ? h('span', { class: 'tag' }, `${x.words} ${t('words')}`)
          : h('span', { class: 'tag unknown' }, t('notWritten')),
        x.gaps ? h('span', { class: 'tag open' }, `${x.gaps} ${t('gaps')}`) : null,
        x.proposals ? h('span', { class: 'gear' }, `${t('proposalMark')} ×${x.proposals}`) : null,
        gate ? tickTag(gate.tick) : null,
        x.present && s.artifact_file ? goSection(s.artifact_file, x.id) : null),
    ], [
      x.present && body
        ? h('div', {},
          h('div', { class: 'row', style: 'margin-bottom:10px' }, confChips(x.confidence), ridChips(x.ids)),
          h('div', { class: 'md', html: md(body.body) }))
        : h('div', {},
          h('p', { class: 'small muted' }, x.what || t('notWritten')),
          x.tools.length ? h('div', { class: 'row', style: 'margin-top:9px' },
            h('span', { class: 'tiny faint mono' }, t('fillWith') + ':'),
            x.tools.map(y => h('span', { class: 'tag' + (emph.has(y) ? ' strong' : '') }, y))) : null),
    ]);
  }));

  // The gate's `targets` are the same sections the links point at, so the link *is* the column: one
  // less column of mono text broken across five lines in a narrow rail.
  const gateTable = table([t('state'), t('gateItem'), t('validates')],
    s.gate.map(g => h('tr', {},
      h('td', {}, tickTag(g.tick)),
      h('td', { class: 'prose', html: inline(g.label) }),
      h('td', { class: 'refs' },
        s.artifact_file ? (g.sections || []).map(id => goSection(s.artifact_file, id, '#' + id)) : null,
        g.register ? h('span', { class: 'tag met' }, g.register) : null))));

  const asks = perStep ? h('div', { class: 'panel' },
    h('div', { class: 'kick' }, `${t('statusAsks')} · ${m.active_status}`),
    h('ul', { style: 'padding-left:18px;font-size:12.5px' },
      (perStep.goals || []).map(g => h('li', { style: 'margin:5px 0' }, g))),
    (perStep.tools || []).length ? h('div', { class: 'row', style: 'margin-top:10px' },
      (perStep.tools || []).map(x => h('span', { class: 'tag strong', title: t('emphasised') }, x))) : null)
    : null;

  // The gate and what the status asks are the frame around the reading, not a companion to it: they
  // are short, they are the same for every section, and standing in a column beside the text they
  // took half the page and left the artifact — sentences, tables, evidence — in a gutter. So they sit
  // across the top, where a frame belongs, and the text below runs the full width of the window.
  const frame = asks
    ? h('div', { class: 'grid cols-2' }, sec(t('gate'), { right: gateSummary(s) }, gateTable),
      h('div', { class: 'sec', style: 'align-self:start' }, asks))
    : sec(t('gate'), { right: gateSummary(s) }, gateTable);

  return h('div', {}, head, frame,
    sec(t('sectionsTitle'), { right: `${written}/${s.sections.length} ${t('filled')}` }, sections));
}

/* ---------------------------------------------------------------- artifacts */
function viewArtifacts() {
  const m = S.model;
  if (!m.artifacts.length) return h('div', { class: 'empty' }, t('nothingYet'));
  const art = m.artifacts.find(a => a.file === S.artifact) || m.artifacts[0];
  S.artifact = art.file;
  const section = art.sections.find(x => x.id === S.section) || art.sections[0];

  const toc = h('div', { class: 'toc' }, m.artifacts.map(a => [
    h('div', { class: 'file' }, a.file),
    a.sections.map(x => h('button', {
      'aria-current': a.file === art.file && section && x.id === section.id,
      onclick: () => { S.artifact = a.file; S.section = x.id; render(); },
    }, h('span', {}, x.title || x.id), h('span', { class: 'dotcol' },
      x.gaps.length ? h('i', { class: 'pip gap', title: `${x.gaps.length} ${t('gaps')}` }) : null,
      x.markers.proposals ? h('i', { class: 'pip gear', title: t('proposals') }) : null,
      !x.words ? h('i', { class: 'pip empty' }) : null))),
  ]));

  const ids = section ? [].concat(section.markers.hypotheses, section.markers.risks, section.markers.metrics) : [];
  const stepOf = m.steps.find(x => x.artifact_file === art.file);
  const body = section ? h('div', {},
    h('div', { class: 'kick' }, `${art.file} · ${art.updated || ''}`),
    h('h2', { style: 'font-size:20px;letter-spacing:-.02em' }, section.title || section.id),
    h('div', { class: 'row', style: 'margin:9px 0 2px' },
      h('code', { class: 'tag' }, '#' + section.id),
      confChips(section.markers.confidence),
      section.markers.proposals ? h('span', { class: 'gear' },
        `${t('proposalMark')} ×${section.markers.proposals}`) : null,
      ridChips([...new Set(ids)]),
      stepOf ? goStep(stepOf.step) : null),
    h('hr'),
    h('div', { class: 'md', html: md(section.body) }))
    : h('div', { class: 'empty' }, t('nothingYet'));

  return h('div', { class: 'reader' }, toc, h('div', { class: 'panel' }, body));
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
    'aria-pressed': which === k,
    onclick: () => { S.reg = k; S.regFilter = 'all'; S.regItem = null; render(); },
  }, lab)));

  if (!reg.present) return h('div', {}, tabs, h('div', { class: 'empty' }, `${reg.file} — ${t('nothingYet')}`));

  const enums = m.framework.enums;
  const enumCol = which === 'hypotheses' ? ['type', 'тип']
    : which === 'risks' ? ['category', 'категория'] : ['kind', 'вид'];
  const allowed = which === 'hypotheses' ? enums['hypothesis type']
    : which === 'risks' ? enums['risk category'] : enums['metric kind'];
  const statusCols = ['status', 'статус'];
  const facets = [...new Set(reg.rows.map(r => stripMd(cell(r, ...enumCol))).filter(Boolean))];
  const refs = refIndex();

  const filters = h('div', { class: 'filters' },
    h('button', { 'aria-pressed': S.regFilter === 'all', onclick: () => { S.regFilter = 'all'; render(); } }, t('all')),
    facets.map(v => h('button', { 'aria-pressed': S.regFilter === v, onclick: () => { S.regFilter = v; render(); } }, v)),
    h('input', { type: 'search', placeholder: t('search'), value: S.regSearch,
      oninput: e => { S.regSearch = e.target.value; renderInto('#regtable', regTable()); } }));

  // The trail of one item, assembled by the reader from the change logs that name its id — no
  // second store, and no journal column anyone has to keep in step (CONVENTIONS → Change logs).
  const history = S.model.history || {};

  // A register is wide — ten columns for a hypothesis — and showing all of them at once produced a
  // table that scrolled sideways and grew rows ten lines tall. So the table carries what a reader
  // scans by (the id, the statement, its type, its state, where it is argued) and the row opens to
  // the rest: every remaining column in full, then the item's trail.
  const mainCol = reg.columns[1] || reg.columns[0];
  const shownCols = new Set(['id', mainCol].concat(enumCol, statusCols));

  function detail(r, rid, span) {
    const es = history[rid] || [];
    const rest = reg.columns.filter(c => !shownCols.has(c) && String(r[c] || '').trim());
    return h('tr', { class: 'trailrow' }, h('td', { colspan: span },
      rest.length ? h('div', { class: 'wiring', style: 'margin-top:0;border-top:0' },
        rest.map(c => h('div', { class: 'wrow' },
          h('div', { class: 'wk' }, c), h('div', { class: 'wv', html: inline(r[c]) })))) : null,
      (refs[rid] || []).length ? h('div', {},
        h('div', { class: 'kick', style: 'margin-top:14px' },
          `${t('referencedIn')} · ${(refs[rid] || []).length}`),
        h('div', { class: 'row' }, (refs[rid] || []).map(x =>
          goSection(x.file, x.id, refLabel(x), x.title)))) : null,
      h('div', { class: 'kick', style: 'margin-top:14px' }, `${t('trail')} · ${rid}`),
      es.length ? h('div', { class: 'tl' }, es.map(e => h('div', { class: 'e' },
        h('div', {}, h('div', { class: 'd' }, e.date), h('div', { class: 'tiny faint mono' }, e.file)),
        h('div', {}, h('div', { class: 's', html: inline(e.summary) })))))
        : h('div', { class: 'tiny faint' }, t('trailEmpty'))));
  }

  function regTable() {
    const cols = ['id', mainCol, enumCol[0], statusCols[0]];
    const heads = [reg.columns.find(c => c === 'id') || 'id', mainCol,
      reg.columns.find(c => enumCol.includes(c)) || enumCol[0],
      reg.columns.find(c => statusCols.includes(c)) || statusCols[0]];
    const rows = reg.rows.filter(r => {
      if (S.regFilter !== 'all' && stripMd(cell(r, ...enumCol)) !== S.regFilter) return false;
      if (S.regSearch && !Object.values(r).join(' ').toLowerCase().includes(S.regSearch.toLowerCase())) return false;
      return true;
    });
    const span = cols.length + 1;
    return h('div', { class: 'tablewrap' }, h('table', {},
      h('thead', {}, h('tr', {}, heads.map(c => h('th', {}, c)), h('th', {}, t('referencedIn')))),
      h('tbody', {}, rows.flatMap(r => {
        const val = stripMd(cell(r, ...enumCol));
        const bad = allowed && val && !allowed.includes(val);
        const rid = stripMd(cell(r, 'id'));
        const open = S.regItem === rid;
        const toggle = () => { S.regItem = open ? null : rid; render(); };
        const main = h('tr', { class: bad ? 'flagged' : '' },
          h('td', { class: 'id' }, h('code', { class: 'rid ' + ridClass(rid) }, rid),
            h('button', { class: 'trailbtn', 'aria-pressed': open, title: t('trailHint'), onclick: toggle },
              open ? '–' : '+')),
          h('td', { class: 'prose', html: inline(r[mainCol] || '') }),
          h('td', {}, h('span', { class: 'tag ' + (bad ? 'err' : '') }, val || '—'),
            bad ? h('div', { class: 'tiny faint' }, allowed.join(' · ')) : null),
          h('td', {}, h('span', { class: 'tag ' + stripMd(cell(r, ...statusCols)).split(/[\s·]/)[0] },
            stripMd(cell(r, ...statusCols)) || '—')),
          h('td', { class: 'refs' }, (refs[rid] || []).slice(0, 2).map(x =>
            goSection(x.file, x.id, refLabel(x), x.title)),
          (refs[rid] || []).length > 2 ? h('button', { class: 'trailbtn', onclick: toggle },
            `+${(refs[rid] || []).length - 2}`) : null));
        return open ? [main, detail(r, rid, span)] : [main];
      }))));
  }

  return h('div', {}, tabs, filters, h('div', { id: 'regtable' }, regTable()));
}

/* ---------------------------------------------------------------- metrics */
// One reading's comparable variant: how it was computed and who was counted. Two readings of the
// same node with different variants are different series, never two points of one line.
const variant = r => [r.basis, r.population].filter(Boolean).join(' · ');

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
    // A delta is only meaningful inside one variant: readings compare across neither a different
    // `basis` (how it was computed) nor a different `population` (who was counted).
    const same = rows.filter(r => variant(r) === variant(last));
    const prev = same.length > 1 ? same[same.length - 2] : null;
    const d = prev && prev.value ? (last.value - prev.value) / Math.abs(prev.value) * 100 : null;
    const def = defOf(id);
    const long = String(num(last.value)).length > 10;
    return h('div', { class: 'kpi' },
      h('div', { class: 'lab' }, id),
      undefinedIds.has(id) ? h('div', { class: 'tag err', style: 'margin-top:4px' }, t('notInTree')) : null,
      h('div', { class: 'val', style: long ? 'font-size:20px' : null }, num(last.value),
        h('small', {}, stripMd(cell(def, 'unit')))),
      d === null ? h('div', { class: 'delta flat' }, '—')
        : h('div', { class: 'delta ' + (d > 0.5 ? 'up' : d < -0.5 ? 'down' : 'flat'), title: t('basisNote') },
          `${d > 0 ? '+' : ''}${d.toFixed(1)}% ${t('vsPrev')}`),
      h('div', { class: 'when' }, `${dateOf(last)}${variant(last) ? ' · ' + variant(last) : ''}`
        + `${last.observed_n ? ` · n=${last.observed_n}` : ''}`));
  }));

  const charts = h('div', { class: 'charts' }, withReadings.map(id => {
    const rows = series[id], def = defOf(id);
    const variants = [...new Set(rows.map(variant).filter(Boolean))];
    const groups = variants.length > 1
      ? variants.map(b => ({ label: b, rows: rows.filter(r => variant(r) === b) }))
      : [{ label: variants[0] || '', rows }];
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

  // The definition of every measured node, whole — an accordion, because a definition is a sentence
  // and half a sentence is worse than none.
  const defs = h('div', {}, withReadings.map(id => {
    const def = defOf(id);
    const text = stripMd(cell(def, 'definition', 'определение'));
    if (!text) return null;
    return acc([h('code', { class: 'tag met' }, id),
      h('span', { class: 'sumtitle' }, stripMd(cell(def, 'name', 'название')) || ''),
      h('span', { class: 'summeta' }, h('span', { class: 'tag' }, stripMd(cell(def, 'unit')) || '—'),
        h('span', { class: 'tag' }, stripMd(cell(def, 'kind', 'вид')) || '—'))],
    [h('div', { class: 'md', html: md(text) }),
      h('div', { class: 'tiny faint mono', style: 'margin-top:8px' },
        stripMd(cell(def, 'instrumentation', 'инструментирование')) || '—')]);
  }));

  const readings = table(
    ['id', 'period', 'measured_at', 'value', 'observed_n', 'population', 'basis', 'source', 'note'],
    withReadings.flatMap(id => series[id].map(r => h('tr', {},
      h('td', { class: 'id' }, h('code', {}, id)),
      h('td', { class: 'mono tiny' }, r.period_start ? `${r.period_start} → ${r.period_end}` : '—'),
      h('td', { class: 'mono tiny' }, r.measured_at),
      // an empty value is canon, not a gap: the outcome was not observable yet (REGISTERS → csv)
      h('td', { class: 'num' }, r.value === null ? (r.raw_value || '—') : num(r.value)),
      h('td', { class: 'num tiny' }, r.observed_n || '—'),
      h('td', { class: 'mono tiny' }, r.population || '—'),
      h('td', { class: 'mono tiny' }, r.basis || '—'),
      h('td', { class: 'mono tiny' }, r.source || '—'),
      h('td', { class: 'tiny muted' }, r.note || '')))),
    { titles: [null, null, null, null, t('observedNote')] });

  return h('div', {},
    withReadings.length ? h('div', {},
      sec(t('latest'), { right: `${withReadings.length} ${t('metricNodes').toLowerCase()}` }, kpis),
      sec(t('series'), {}, charts),
      sec(t('metricNodes'), {}, defs),
      sec(t('allReadings'), { right: `${m.metrics.rows} ${t('csvRows')}` }, readings))
      : sec(t('latest'), {}, h('div', { class: 'note warn' },
        h('span', { class: 'who' }, t('readings')), h('div', {}, t('noReadings')))),
    without.length ? sec(t('definedNotMeasured'), { right: String(without.length) },
      table(['id', t('colDefinition'), 'instrumentation'], without.map(id => {
        const def = defOf(id);
        return h('tr', {}, h('td', { class: 'id' }, h('code', { class: 'rid met' }, id)),
          h('td', { html: inline(stripMd(cell(def, 'definition', 'определение'))) }),
          h('td', { class: 'mono tiny' }, stripMd(cell(def, 'instrumentation', 'инструментирование')) || '—'));
      }))) : null);
}

/* ---------------------------------------------------------------- open questions */
function viewOpen() {
  const m = S.model;
  const openGate = m.steps.flatMap(s => s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown')
    .map(g => ({ step: s, g })));
  const hyp = m.registers.hypotheses.rows.filter(r =>
    /open|testing/i.test(stripMd(cell(r, 'status', 'статус'))));

  const gapsTable = table([t('artifact'), t('toClarify'), ''], m.gaps.map(g => h('tr', {},
    h('td', { class: 'id' }, h('code', {}, g.file.replace(/\.md$/, '') + '#' + g.section)),
    h('td', { class: 'prose', html: inline(gapText(g.line)) }),
    h('td', { class: 'act' }, goSection(g.file, g.section)))), { empty: t('nothingOpen') });

  const gateTable = table(['#', t('state'), t('gateItem'), ''], openGate.map(({ step, g }) => h('tr', {},
    h('td', { class: 'id' }, h('b', {}, step.step)),
    h('td', {}, tickTag(g.tick)),
    h('td', { class: 'prose' }, h('div', { html: inline(g.label) }),
      h('div', { class: 'tiny faint mono wrapid' }, (g.targets || []).join(' + '))),
    h('td', { class: 'act' }, goStep(step.step)))), { empty: t('nothingOpen') });

  const refs = refIndex();
  const hypTable = table(['id', t('colStatement'), t('colType'), t('state'), ''], hyp.map(r => {
    const rid = stripMd(cell(r, 'id'));
    return h('tr', {},
      h('td', { class: 'id' }, h('code', { class: 'rid hyp' }, rid)),
      h('td', { class: 'prose', html: inline(stripMd(cell(r, 'hypothesis', 'гипотеза'))) }),
      h('td', { class: 'tiny' }, h('span', { class: 'tag' }, stripMd(cell(r, 'type', 'тип')) || '—')),
      h('td', { class: 'tiny' }, h('span', { class: 'tag ' + stripMd(cell(r, 'status', 'статус')).split(/[\s·]/)[0] },
        stripMd(cell(r, 'status', 'статус')) || '—')),
      h('td', { class: 'refs' }, (refs[rid] || []).slice(0, 3).map(x =>
        goSection(x.file, x.id, refLabel(x), x.title))));
  }), { empty: t('nothingOpen') });

  // An empty section is good news here — nothing to clarify, no gate open. A full table with a
  // header and a "nothing here" cell dresses that up as content; one quiet line states it and moves on.
  const clear = () => h('div', { class: 'clear' }, t('nothingOpen'));
  return h('div', {},
    sec(t('toClarify'), { right: String(m.gaps.length) }, m.gaps.length ? gapsTable : clear()),
    sec(t('openGates'), { right: String(openGate.length) }, openGate.length ? gateTable : clear()),
    sec(t('inFlight'), { right: String(hyp.length) }, hyp.length ? hypTable : clear()));
}

/* ---------------------------------------------------------------- sources */
function viewSources() {
  const m = S.model, src = m.sources;
  const idx = src.index || [];
  const cols = src.index_columns || [];
  const indexTable = cols.length
    ? table(cols, idx.map(r => h('tr', {}, cols.map(c => h('td', { html: inline(r.cells[c] || '') })))))
    : h('div', { class: 'empty' }, t('nothingYet'));

  const files = table([t('file'), t('role'), t('updated'), t('indexed')], (src.files || []).map(f =>
    h('tr', {},
      h('td', { class: 'id' }, h('code', {}, f.file)),
      h('td', { class: 'tiny' }, h('span', { class: 'tag' }, f.node_type || '—')),
      h('td', { class: 'id faint' }, f.updated || '—'),
      h('td', {}, f.indexed ? h('span', { class: 'tag done' }, 'INDEX.md')
        : h('span', { class: 'tag open' }, t('notIndexed'))))));

  const slots = Object.entries(m.metric_source_slots || {});
  return h('div', {},
    sec(t('sourceIndex'), { right: src.index_present ? 'INDEX.md' : t('nothingYet') }, indexTable),
    sec(t('sourceFiles'), { right: String((src.files || []).length) }, files),
    slots.length ? sec('metric_source_slots', {},
      table(['', ''], slots.map(([k, v]) => h('tr', {},
        h('td', { class: 'id' }, h('code', {}, k)),
        h('td', { class: 'small' }, typeof v === 'string' ? v : JSON.stringify(v)))))) : null,
    m.handoff.present ? sec(t('handoff'), { right: m.handoff.updated || '' },
      h('div', {}, (m.handoff.sections || []).map(x => acc(
        [h('span', { class: 'sumtitle' }, x.title || x.id), h('code', { class: 'tag' }, '#' + x.id)],
        [h('div', { class: 'md', html: md(x.body) })])))) : null);
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

  // A plane holds up to ~30 near-identical skills. A grid of cards for that is the wall this console
  // was built to avoid — so the roster is a compact, searchable table: one line each, the row is the
  // link to its detail. The search filters within the open plane and repaints only the table.
  const search = h('input', { class: 'pathin', type: 'search', placeholder: t('search'),
    value: S.skillSearch || '', oninput: e => { S.skillSearch = e.target.value; renderInto('#skilltable', skillTable()); } });

  function skillTable() {
    const q = (S.skillSearch || '').trim().toLowerCase();
    const rows = shown.filter(x => !q
      || `${x.name} ${x.kind || ''} ${x.used_by_steps.join(',')}`.toLowerCase().includes(q));
    return table([t('colName'), t('colKind'), t('usedBy'), t('origin')],
      rows.map(x => h('tr', {
        class: 'rowlink' + (picked && picked.name === x.name ? ' on' : ''),
        onclick: () => { S.skillPick = x.name; S.skillFile = null; render(); },
      },
        h('td', {}, h('b', {}, x.name),
          x.homeless.length ? h('span', { class: 'tag err', style: 'margin-left:7px' }, 'homeless') : null),
        h('td', {}, x.kind ? h('span', { class: 'tag' }, x.kind) : h('span', { class: 'faint' }, '—')),
        h('td', { class: 'tiny mono' }, x.used_by_steps.length ? x.used_by_steps.join(', ') : '—'),
        h('td', {}, h('span', { class: 'tag ' + (x.origin === 'local' ? 'done' : '') },
          x.origin === 'local' ? t('local') : t('vendored'))))),
      { empty: t('nothingYet') });
  }

  const detail = picked ? h('div', { class: 'panel' },
    h('div', { class: 'spread' }, h('h2', {}, picked.name),
      h('span', { class: 'row' },
        h('span', { class: 'tag' }, picked.plane),
        h('span', { class: 'tag' }, picked.origin === 'local' ? t('local') : t('vendored')),
        picked.version ? h('span', { class: 'tag' }, 'v' + picked.version) : null)),
    picked.summary ? h('p', { class: 'small muted', style: 'margin-top:8px' },
      picked.summary.replace(/^#+\s*[^\s]*\s*/, '')) : null,
    h('div', { class: 'wiring' }, [
      [t('produces'), picked.produces.join(' · ')],
      [t('usedBy'), picked.used_by_steps.join(', ')],
      [t('prerequisites'), picked.prerequisites.join(' · ')],
      [t('reads'), picked.reads_registers.join(' · ')],
      [t('writes'), picked.writes_registers.join(' · ')],
      [t('inputs'), picked.inputs.join(' · ')],
      ['method basis', picked.method_basis],
      ['evidence', picked.evidence_standard],
      ['volume rule', picked.volume_rule && picked.volume_rule !== 'n/a' ? picked.volume_rule : ''],
      ['selection rule', picked.selection_rule && picked.selection_rule !== 'n/a' ? picked.selection_rule : ''],
      ['shows rejects', picked.rejects_shown === 'required' ? 'required' : ''],
    ].filter(([, v]) => v).map(([k, v]) => h('div', { class: 'wrow' },
      h('div', { class: 'wk' }, k), h('div', { class: 'wv' }, v)))),
    S.snapshot ? null : h('div', { class: 'row', style: 'margin-top:12px' },
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
          onclick: () => { S.skillFile = null; render(); } }, 'x')),
      h('pre', {}, S.skillFile.text)) : null) : null;

  return h('div', {}, tabs,
    h('p', { class: 'small muted', style: 'margin:0 0 12px;max-width:80ch' }, t('addSkillHint')),
    h('div', { class: 'filters', style: 'margin-bottom:10px' }, search),
    h('div', { id: 'skilltable' }, skillTable()),
    detail ? h('div', { style: 'margin-top:16px' }, detail) : null);
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
  const files = [...new Set(m.timeline.map(e => e.file))];
  const shown = m.timeline.filter(e => S.logFile === 'all' || e.file === S.logFile);
  const filters = h('div', { class: 'filters' },
    h('button', { 'aria-pressed': S.logFile === 'all', onclick: () => { S.logFile = 'all'; render(); } },
      `${t('all')} · ${m.timeline.length}`),
    files.map(f => h('button', { 'aria-pressed': S.logFile === f, onclick: () => { S.logFile = f; render(); } },
      `${f} · ${m.timeline.filter(e => e.file === f).length}`)));

  return h('div', {}, filters,
    sec(t('changeLog'), { right: `${shown.length} ${t('entries')}` },
      h('div', { class: 'panel' }, h('div', { class: 'tl' }, shown.map(e => h('div', { class: 'e' },
        h('div', {}, h('div', { class: 'd' }, e.date), h('div', { class: 'tiny faint mono' }, e.file)),
        h('div', {}, h('div', { class: 's' }, e.summary),
          h('div', { class: 'b md', html: md(e.body) }))))))));
}

// The read layer emits one finding per file, so a rule every artifact breaks the same way — a missing
// change log — arrives as six identical sentences. That is the wall of repeated text the console is
// meant to kill, not print. Findings that share a level, a code and the same wording once their
// subject (the leading filename or id) is removed collapse into one note that lists the subjects.
function groupHealth(items) {
  const groups = [];
  const byKey = {};
  for (const x of items) {
    const subject = (x.message.match(/^(\S+)\s+/) || [])[1] || '';
    const tail = subject ? x.message.slice(subject.length).trim() : x.message;
    const key = `${x.level}|${x.code || ''}|${tail}`;
    if (!byKey[key]) { byKey[key] = { level: x.level, code: x.code || '', tail, subjects: [], sample: x.message }; groups.push(byKey[key]); }
    byKey[key].subjects.push(subject);
  }
  return groups;
}

function healthNote(g) {
  const many = g.subjects.filter(Boolean).length > 1;
  return h('div', { class: 'note ' + g.level },
    h('span', { class: 'who' }, `${g.level}${g.code ? ' ' + g.code : ''}${many ? ' ×' + g.subjects.length : ''}`),
    many
      ? h('div', {}, h('div', { class: 'mono tiny', style: 'margin-bottom:4px' }, g.subjects.join(' · ')),
        h('div', {}, g.tail))
      : h('div', {}, g.sample));
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
    sec(t('healthTitle'), { right: `${m.health.filter(x => x.level === 'error').length} error · `
      + `${m.health.filter(x => x.level === 'warn').length} warn` },
      m.health.length ? h('div', { class: 'notes' }, groupHealth(m.health).map(healthNote))
        : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('healthClean')))),
    h('div', {},
      sec(t('lintTitle'), {}, lintBox),
      sec(t('notChecked'), {}, h('p', { class: 'small muted' }, t('notCheckedBody')))));
}

const VIEWS = { overview: viewOverview, step: viewStep, artifacts: viewArtifacts, registers: viewRegisters,
  metrics: viewMetrics, open: viewOpen, sources: viewSources, skills: viewSkills, log: viewLog,
  checks: viewChecks };
const TAB_ORDER = ['overview', 'artifacts', 'registers', 'metrics', 'open',
  null, 'sources', 'skills', 'log', 'checks'];

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
    sources: (m.sources.files || []).length || null,
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

function renderRail() {
  const m = S.model;
  renderKids('#rail', (m.steps || []).map(s => {
    const c = s.gate_counts || {};
    const total = s.gate.length || 1;
    const done = c.done || 0;
    return h('button', {
      class: (S.tab === 'step' && S.step === s.step ? 'on ' : '') + (m.current_step === s.step ? 'here' : ''),
      onclick: () => { S.tab = 'step'; S.step = s.step; render(); },
      title: `${s.title || s.name} — ${gateSummary(s)}`,
    },
      h('div', { class: 'rn' }, `${s.step}${m.current_step === s.step ? ' ·' : ''}`),
      h('div', { class: 'rt' }, shortTitle(s.title || s.name)),
      h('div', { class: 'rp' },
        h('i', { style: `width:${(done / total * 100).toFixed(1)}%` }),
        h('i', { class: 'dim', style: `width:${((total - done) / total * 100).toFixed(1)}%` })));
  }));
}

function render() {
  const m = S.model;
  if (!m) return;
  writeHash();
  document.documentElement.lang = m.language || 'en';
  document.getElementById('product').textContent = m.product;
  document.getElementById('subline').textContent = S.snapshot
    ? `${m.name} · ${t('readOnlySnap')}` : `${m.name} · ${m.path}`;

  renderKids('#acts', [
    h('span', { class: 'tag strong' }, `${t('status')} ${m.active_status || '—'}`),
    S.snapshot ? null : h('a', { class: 'btn solid', title: t('saveHint'),
      href: '/api/export?instance=' + encodeURIComponent(m.path) }, t('saveHtml')),
    S.snapshot || S.instances.length < 2 ? null : h('select', {
      class: 'pick', onchange: e => load(e.target.value),
    }, S.instances.map(i => h('option', { value: i.path, selected: i.path === m.path },
      `${i.name} · ${i.kind}`))),
    S.snapshot ? null : h('input', { class: 'pathin', placeholder: t('addHint'), title: t('addFolder'),
      onkeydown: e => { if (e.key === 'Enter') addFolder(e.target.value); } }),
    h('button', { class: 'btn', title: t('theme'),
      onclick: () => { applyTheme(THEMES[(THEMES.indexOf(theme()) + 1) % 3]); render(); } },
      t('theme') + ': ' + t('theme' + theme())),
  ]);

  renderRail();

  const c = counts();
  renderKids('#tabs', TAB_ORDER.map(k => k === null ? h('span', { class: 'sep' })
    : h('button', { 'aria-current': S.tab === k, onclick: () => { S.tab = k; render(); } },
      t('tabs.' + k), c[k] ? h('span', { class: 'count' }, c[k]) : null)));

  try {
    renderInto('#view', VIEWS[S.tab]());
  } catch (e) {
    renderInto('#view', h('div', { class: 'note error' }, h('span', { class: 'who' }, 'ui'),
      h('div', {}, `${e.name}: ${e.message}`)));
    throw e;
  }
  document.getElementById('footpath').innerHTML = S.snapshot
    ? `<b>${esc(m.product)}</b>` : `<b>${esc(m.path)}</b>`;
  document.getElementById('footrev').textContent = S.snapshot ? t('snapshotNote') : t('readOnly');
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
  // lint the instance being shown, not every instance on the machine
  fetch('/api/lint?instance=' + encodeURIComponent(S.model.path))
    .then(x => x.json()).then(l => { S.lint = l; render(); }).catch(() => {});
}

/* The exported snapshot: same renderer, frozen data, nothing to fetch. */
function bootSnapshot(snap) {
  S.snapshot = snap;
  S.model = snap.model;
  S.lint = snap.lint || null;
  S.instances = [];
  // readHash() ran first: a deep link into a step must survive the boot
  if (!S.step) S.step = S.model.current_step || (S.model.steps[0] || {}).step || 1;
  renderInto('#snap', h('div', { class: 'snapbar' },
    h('span', { class: 'sd' }, t('snapshot').toUpperCase()),
    h('b', {}, S.model.product),
    h('span', {}, `${t('madeOn')} ${snap.generated}`),
    h('span', { style: 'margin-left:auto' }, t('snapshotNote'))));
  render();
}

async function boot() {
  applyTheme();
  readHash();                       // before the first render: writeHash() would overwrite the deep link
  window.addEventListener('hashchange', () => { readHash(); render(); });
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => render());
  if (window.__SNAPSHOT__) return bootSnapshot(window.__SNAPSHOT__);
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
