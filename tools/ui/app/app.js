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
 * The chrome is English by design — the framework is an international, English-language project;
 * the *content* (artifact text, register rows) appears in whatever language the instance wrote it.
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
      log: 'Change log', checks: 'Checks', guide: 'Guide' },
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
    whatElseCol: 'what it is',
    colType: 'type', colDefinition: 'definition', colStatement: 'statement',
    gate: 'The gate', gateItem: 'gate item', gateDone: 'closed', gateOpen: 'open', gateNa: 'n/a',
    gateDeferred: 'deferred', gateUnknown: 'unrecorded', gateClosed: 'gate closed',
    gaps: 'gaps', proposals: 'agent proposals', proposalMark: 'proposed', validates: 'validates',
    statusAsks: 'What the active status asks here', emphasised: 'emphasised for this stage',
    stepGoal: 'What this step is for',
    rows: 'rows', state: 'state',
    hypotheses: 'Hypotheses', risks: 'Risks', metricNodes: 'Metric nodes', readings: 'readings',
    features: 'Features', surfaces: 'Surfaces', surfaceBoard: 'The product, by surface',
    surfaceBoardNote: 'each column is a surface; the cards are the features on it, coloured by state',
    noSurfaceCol: 'no surface named', inMust: 'in this sprint’s must', prioNow: 'now',
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
    lintFramework: 'about the framework itself, not this product',
    notChecked: 'Checked by neither', notCheckedBody: 'Prose quality, whether register values are true '
      + '(only their enums and ids are checked), prerequisite completeness, adapter fidelity — and '
      + 'nothing here judges product decisions. The console reports; the human decides.',
    changed: 'the folder changed — reloading',
    readOnly: 'read-only — the agent writes the files, this shows what they say',
    subProducts: 'Sub-products', umbrellaNote: 'This folder is an umbrella: the shared config and sources '
      + 'live here, and each product below keeps its own artifacts, state and registers.',
    openIt: 'open', plane: 'plane', vendored: 'framework', local: 'this product',
    usedBy: 'steps', prerequisites: 'prerequisites', reads: 'reads', writes: 'writes',
    interview: 'interview', fragment: 'section template',
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
    read: 'open', more: 'details', cName: 'competitor',
    boardIdea: 'Product canvas', boardAnalysis: 'Market analysis',
    zCustomer: 'Customer', zProduct: 'Product', zValidation: 'Validation',
    dMarket: 'Market sizing', dCompetitors: 'Competitors', dSubstitutes: 'Substitutes',
    dOpportunity: 'Opportunity', dRisks: 'Niche risks',
    mTam: 'total addressable', mSam: 'serviceable — load-bearing', mSom: 'obtainable ~3 yr', mCagr: 'growth / yr',
    cType: 'type', cPlay: 'how they play', cMoat: 'moat vs us', cPrice: 'price', cDyn: 'dynamics',
    rForce: 'force', rLik: 'likelihood', rImp: 'impact',
    assembledFrom: 'Assembled from the competitor sections below — a dash is “no match”, not zero.',
    gapDash: '— to clarify —',
    expand: 'expand the whole section in place', collapse: 'collapse',
    worklog: 'workings', worklogTip: 'open the worklog this section was worked out in',
    worklogMissing: 'worklog not found',
    confirmed: 'confirmed', pending: 'to confirm', confirmedOn: 'confirmed by a human on',
    pendingTip: 'result not yet confirmed by a human', sectionsShort: 'sections',
    contested: 'returned', contestedTip: 'a human reviewed this and sent it back for rework',
    restsOn: 'foundation unconfirmed', restsTip: 'confirmed, but rests on sections not yet confirmed:',
    daysAgo: 'days ago', daysOld: 'days old',
    wlNewer: 'workings newer',
    wlNewerTip: 'the worklog changed after the artifact was written — the projection may be stale',
    navBack: 'back', navFwd: 'forward', toTop: 'back to top',
    boardStrategy: 'Strategy canvas', boardStratPlan: 'Metrics & economics',
    boardTactical: 'Goals & guardrails', boardSprint: 'Sprint board',
    z3Cascade: 'Strategy cascade', z3Commercial: 'Commercial', z3Product: 'Product',
    z3Bets: 'Bets & risks', z3Open: 'Open',
    z4North: 'North Star & metric tree', z4Econ: 'Economics',
    z4Instr: 'Instrumentation & risk', z4Hyp: 'Hypotheses',
    z5Goals: 'Goals & targets', z5Guard: 'Guardrails', z5Res: 'Resources & market',
    z5Test: 'Tests & blockers',
    z6Commit: 'Committed vs backlog', z6Excluded: 'Excluded — and why', z6Handoff: 'Handoff',
    z6Items: 'Committed — must', z6Backlog: 'Backlog — ranked',
    dirDev: 'Development — Features', dirG2m: 'Go-to-market — Activities',
    dirBo: 'Back-office — Tasks',
    zOther: 'Other sections',
    /* The guide tab — chrome, like every string here: it describes the canon, the canon itself
       lives in the process/ files this text points at. */
    g: {
      how: 'How it works', cycle: 'The six steps', map: 'What lives where',
      legend: 'Legend', ask: 'How to ask for work',
      flowTitle: 'One direction of writing',
      human: 'the human', humanSub: 'decides',
      agent: 'any agent', agentSub: 'runs the loop, writes the files',
      files: 'the instance folder', filesSub: 'markdown — the single source of truth',
      console: 'this console', consoleSub: 'renders what the files say',
      asks: 'asks for work', writes: 'writes', reads: 'read-only', looks: 'is read by',
      noWrite: 'The console has no write path — not a deferred one, an absent one. A section needs '
        + 'its method; a decision needs a dated change-log entry and a reason. Both go through the '
        + 'same door: say it to the agent.',
      loopTitle: 'The operating loop — seven moves, every pass',
      loopSub: 'Every unit of work is one pass of this skeleton; what varies between passes is the '
        + 'card it runs. The full runtime is process/OPERATING-LOOP.md.',
      moves: [
        ['Orient', 'read the active status (config.yaml) and the position (state.yaml)'],
        ['Name the goal', 'find the goal-map row for the trigger, open its card before acting'],
        ['Gather the inputs', 'check prerequisites, announce the read perimeter, size the pass'],
        ['Close the gaps', 'a missing prerequisite or an open decision goes to the human — never a guess'],
        ['Act', 'work in the worklog; the artifact section is its projection, every claim tagged'],
        ['Record', 'a dated change-log entry, gate ticks, register rows, a sign-off proposal'],
        ['Bubble', 'next item — and raise whatever this pass invalidated above or below'],
      ],
      nextPass: 'and the next pass begins at 0',
      philTitle: 'The rules the agent lives by',
      phil: [
        'The agent prepares, the human decides — agent proposals wear the "proposed" badge.',
        'Facts only from sources; missing data is "— to clarify —", never a guess.',
        'Everything is dated, nothing is overwritten — every artifact keeps a change log.',
        'Confidence is explicit: every claim carries a tag.',
        'Gates guide, they do not lock — you can move on with gaps, and they stay flagged.',
        'One writer of the canon: the orchestrating agent; subagents only return text.',
      ],
      nestTitle: 'Nested loops, different cadences',
      nestSub: 'The lower the loop, the more often it turns — and the more it leans on data over '
        + 'interview. Timeframes are indicative, not limits.',
      n12: 'Concept · Analysis — revisited on pivot or major learning',
      n34: 'Strategy · Strategic plan — ~3–12 mo, reviewed ~quarterly',
      n5: 'Tactical plan — ~1–3 mo, stage-gate ~monthly',
      n6: 'Sprint — ~1–2 wk, every sprint',
      feed: 'The loops feed both ways: a sprint can refute a hypothesis and reopen tactics; a metric '
        + 'ceiling can reopen strategy. Each step declares what it invalidates up and down.',
      liveTitle: 'This instance, live',
      homesTitle: 'A value lives in exactly one of three homes',
      wl: 'worklog', wlSub: 'the source of truth — where a method works its inputs, reasoning and numbers out',
      art: 'artifact', artSub: 'the projection of the worklog — the thesis a human reads and signs',
      regs: 'registers', regsSub: 'the shared state: H- / R- / M- ids that flow across steps, cited by id from both sides',
      projection: 'projection',
      mapTitle: 'The folder, tab by tab',
      what: 'what it is', where: 'shown in',
      mapRows: [
        ['config.yaml', 'the human’s decisions: product, active status, language, directions', 'overview'],
        ['state.yaml', 'the position: current step, gate ticks, last pass — agent-written every pass', 'overview'],
        ['1-… 6-….md', 'the six step artifacts — sections, confidence tags, change logs', 'artifacts'],
        ['<step>/<method>.md', 'worklogs — the workings each section is projected from', 'artifacts'],
        ['registers/', 'hypotheses · risks · metric tree; readings land in metrics.csv', 'registers'],
        ['sources/', 'evidence in, with INDEX.md naming each file’s role', 'sources'],
        ['tool-skills/ · skills/', 'the methods, operations and outputs the agent can reach', 'skills'],
        ['HANDOFF.md', 'the session handoff — state to resume from, verified against the files', 'sources'],
      ],
      legConf: 'Confidence — on every claim',
      legConfRows: [
        ['assumption', 'a working guess, awaiting evidence'],
        ['sourced', 'traced to a named source'],
        ['validated', 'checked against reality — data, an experiment'],
        ['refuted', 'checked and found false'],
      ],
      legTicks: 'Gate ticks — the process axis',
      legTickRows: [
        ['done', 'the checklist item is satisfied and recorded'],
        ['open', 'still owed at this step'],
        ['deferred', 'consciously postponed — a decision, not a gap'],
        ['n/a', 'does not apply to this product'],
        ['unknown', 'never recorded — state.yaml is silent about it'],
      ],
      legSign: 'Sign-off — the semantic axis',
      legSignRows: [
        ['confirmed', 'confirmed', 'a human approved this exact version, on the date shown'],
        ['pending', 'to confirm', 'written, not yet reviewed by a human'],
        ['contested', 'returned', 'reviewed and sent back for rework'],
        ['aged', 'aged', 'the sign-off or reading is old enough to be a question again'],
        ['restwarn', 'foundation unconfirmed', 'confirmed, but resting on sections that are not'],
        ['wlnew', 'workings newer', 'the worklog changed after the artifact — the projection may be stale'],
      ],
      legIds: 'Register ids — one colour everywhere',
      legIdRows: [['H-001', 'a hypothesis'], ['R-001', 'a risk'], ['M-nsm', 'a metric node']],
      legMarks: 'Marks',
      legGear: 'an agent proposal awaiting the human’s decision',
      legGap: 'named missing data — the human owes an answer, the agent never fills it',
      legStrip: 'the section’s confidence mix, in the tag colours above',
      legRing: 'outer ring — gate items closed; inner — sections a human confirmed. Health is the '
        + 'rings agreeing; the gap between them is the signal.',
      legTrail: 'opens every change-log entry that names this id',
      askLead: 'The console is a viewer. Each row below is a sentence said to the agent in chat — '
        + 'the agent runs the loop and writes the files; the console shows the result on the next read.',
      askWhen: 'situation', askSay: 'say to the agent',
      askRows: [
        ['a gate item is open', '"Run a pass on step 3 — close the gate item on pricing."'],
        ['a metric was measured', '"Record a reading for M-nsm: 412 weekly editors, measured 2026-08-20, source: analytics."'],
        ['a decision is made', '"Decision: we go with the freemium price. Write it down with the reason."'],
        ['a section reads wrong', '"I contest #segments — the lead segment is stale. Send it back, here is why."'],
        ['a number changed at the source', '"Update the market sizing from the new report in sources/."'],
        ['a new method is needed', '"Add a skill that scores leads the way we do it."'],
        ['starting a session', '"Start work." — the agent orients on the instance and proposes the next pass'],
      ],
      askNote: 'The router from a trigger to the exact card is process/goal-map.md; the rules the '
        + 'agent follows are AGENTS.md and process/OPERATING-LOOP.md.',
    },
  },
};

/* ---------------------------------------------------------------- state */
const S = {
  model: null, lint: null, instances: [], rev: -1, snapshot: null,
  tab: 'overview', step: null, artifact: null, section: null, worklog: null,
  reg: 'hypotheses', regFilter: 'all', regSearch: '', regItem: null,
  skillPlane: 'library', skillPick: null, skillFile: null, logFile: 'all', guideSec: 'how',
  hist: [], histIdx: -1, navigating: false,
};

/* The chrome is English-only (the framework's language); STR keeps the one-home-for-strings shape. */
const L = () => STR.en;
function t(key) {
  const get = o => key.split('.').reduce((x, k) => (x || {})[k], o);
  return get(STR.en) || key;
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
  // A `<!-- comment -->` inside a line (e.g. a trailing card mark) is not content — drop it before
  // escaping, or it would print literally as `&lt;!-- … --&gt;`.
  let s = esc(String(src === null || src === undefined ? '' : src).replace(/<!--[\s\S]*?-->/g, ''));
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
/* Inline markdown, but honour a hard-break newline (a `\n` that card_line / md kept from a markdown
   hard break) as a <br>. Each visual line is inlined on its own: a hard break separates distinct
   items, so an inline span (bold, a link) never straddles one. */
const inlineBr = s => String(s === null || s === undefined ? '' : s).split('\n').map(inline).join('<br>');
function md(src) {
  const lines = String(src || '').split('\n');
  const out = [];
  let i = 0, para = [];
  // A paragraph line ending in `\` or two spaces is a markdown hard break — kept as its own line;
  // an ordinary wrap joins with a space. Same rule card_line uses, so a card and its opened section agree.
  const flush = () => {
    if (!para.length) return;
    let s = '';
    para.forEach((raw, k) => {
      const hard = /(?:\\|\s{2,})$/.test(raw);
      const t = raw.trim().replace(/\s*\\$/, '');
      s += t + (k < para.length - 1 ? (hard ? '\n' : ' ') : '');
    });
    out.push(`<p>${inlineBr(s)}</p>`);
    para = [];
  };
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
    para.push(l);  // raw, so flush() can see a trailing hard break (`\` or two spaces)
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
const ridClass = x => /^H-/.test(x) ? 'hyp' : /^R-/.test(x) ? 'risk'
  : /^F-/.test(x) ? 'feat' : /^S-/.test(x) ? 'surf' : 'met';
const ridChips = ids => (ids || []).map(x => h('span', { class: 'tag ' + ridClass(x) }, x));

/* A section is a thesis the human signs off (CONVENTIONS → Section confirmation). `confirmed` carries
   the date they approved THIS version; absence = pending (⚙️). A gap section (nothing written) shows
   nothing — there is no result to confirm yet. Words, not a glyph, per the house rule. */
const confTag = m => {
  if (!m || !m.present || m.open) return null;   // an open section (inbox) has no result to sign
  if (m.confirmed) {
    // an old sign-off is not wrong, but it is a question again — the tag turns amber past the threshold
    const age = daysSince(m.confirmed);
    const old = age !== null && age > STALE_SIGNED;
    return h('span', { class: 'tag confirmed' + (old ? ' aged' : ''),
        title: t('confirmedOn') + ' ' + m.confirmed + (m.confirmed_by ? ' · ' + m.confirmed_by : '')
          + (old ? ` · ${age} ${t('daysAgo')}` : '') },
      t('confirmed') + ' ' + m.confirmed);
  }
  if (m.contested)   // a human looked and sent it back — distinct from never-reviewed pending
    return h('span', { class: 'tag contested', title: t('contestedTip') }, t('contested'));
  return h('span', { class: 'tag pending', title: t('pendingTip') }, t('pending'));
};
const confCounts = s => {
  const live = (s.sections || []).filter(x => x.present && !x.open);
  return { done: live.filter(x => x.confirmed).length, total: live.length };
};
/* A confirmed thesis that rests on a foundation section not itself confirmed is a quiet staleness
   (CONVENTIONS → Section confirmation): the ground under it moved or was never signed. Shown only on a
   confirmed section — an unconfirmed one resting on unconfirmed is just not-done-yet, not a risk. */
const restTag = s => {
  if (!s || !s.confirmed || !(s.rests_on_unconfirmed || []).length) return null;
  return h('span', { class: 'tag restwarn', title: t('restsTip') + ' ' + s.rests_on_unconfirmed.join(', ') },
    t('restsOn'));
};

/* -- freshness. Age is read against the viewer's clock (also in a snapshot: "how stale is this NOW"
   is the honest question a months-old export should answer). Only staleness is shown — a chip that is
   always present is noise; the thresholds are deliberate round numbers, not tuned per instance. */
const daysSince = iso => {
  const d = Date.parse(String(iso || ''));
  return isNaN(d) ? null : Math.floor((Date.now() - d) / 86400000);
};
const STALE_SIGNED = 60;    // a sign-off older than this is re-shown as a question, not a fact
const STALE_READING = 90;   // a metric KPI whose last reading is older than this gets flagged
/* The worklog is the source of truth and the artifact its projection (CONVENTIONS → Step folders &
   worklogs) — so a worklog dated after the artifact means the projection may no longer say what the
   workings say. Dates are the `updated` frontmatter both sides are obliged to keep. */
function wlNewerTag(step, tool) {
  const stem = step.artifact_file ? step.artifact_file.replace(/\.md$/, '') : '';
  const wl = ((S.model.worklogs || {})[stem] || {})[tool];
  if (!wl || !wl.updated || !step.artifact_updated || wl.updated <= step.artifact_updated) return null;
  return h('span', { class: 'tag wlnew',
    title: `${t('wlNewerTip')} (${wl.updated} > ${step.artifact_updated})` }, t('wlNewer'));
}

/* The step's two axes drawn as one figure: outer ring = gate items closed (the process axis), inner
   ring = sections a human confirmed (the semantic axis). Health is the rings agreeing; the gap
   between them is the signal — a closed gate nobody signed, or signed work with its gate unticked. */
function dualRing(s, size) {
  const gt = s.gate.length, gd = (s.gate_counts || {}).done || 0;
  const cc = confCounts(s);
  const R = size / 2, w = Math.max(2.4, size / 11);
  const el = svg('svg', { viewBox: `0 0 ${size} ${size}`, width: size, height: size,
    class: 'dring', role: 'img' });
  [[R - w / 2 - 0.5, gt ? gd / gt : 0, 'var(--ok)'],
   [R - w * 2 - 1.5, cc.total ? cc.done / cc.total : 0, 'var(--navy)']].forEach(([r, frac, color]) => {
    // the empty track in --line-2, not --grid: an unfilled ring must still read as a ring, or the
    // figure disappears exactly where its message ("nothing closed yet") matters most
    el.append(svg('circle', { cx: R, cy: R, r, fill: 'none', stroke: 'var(--line-2)', 'stroke-width': w }));
    if (frac > 0) {
      const c = 2 * Math.PI * r;
      el.append(svg('circle', { cx: R, cy: R, r, fill: 'none', stroke: color, 'stroke-width': w,
        'stroke-dasharray': `${(c * Math.min(1, frac)).toFixed(2)} ${c.toFixed(2)}`,
        'stroke-linecap': frac < 1 ? 'round' : 'butt', transform: `rotate(-90 ${R} ${R})` }));
    }
  });
  return h('span', { class: 'dringwrap',
    title: `${t('gateClosed')} ${gd}/${gt} · ${t('confirmed')} ${cc.done}/${cc.total}` }, el);
}

/* The section's confidence mix as one thin strip — same classes and colours as the .conf chips, so
   the strip reads with the vocabulary the chips already taught. Nothing tagged → no strip: an
   untagged section has no evidence story to compress. */
const EV_ORDER = ['sourced', 'validated', 'assumption', 'refuted'];
function evStrip(conf, extra) {
  const c = conf || {};
  const total = EV_ORDER.reduce((a, k) => a + (c[k] || 0), 0);
  if (!total) return null;
  return h('div', { class: 'evstrip' + (extra ? ' ' + extra : ''),
    title: EV_ORDER.filter(k => c[k]).map(k => `${k} ×${c[k]}`).join(' · ') },
    EV_ORDER.filter(k => c[k]).map(k =>
      h('i', { class: k, style: `width:${(c[k] / total * 100).toFixed(1)}%` })));
}

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
/* A drill-through from a board block to the worklog it was worked out in. The section names its method
   with `<!-- tool: X -->`, and the worklog is `<step-folder>/X.md` (CONVENTIONS → Step folders &
   worklogs) — the link is derived from that marker, never authored per instance. */
function goWorklog(stem, tool, label) {
  return h('button', {
    class: 'golink wl', title: t('worklogTip'),
    onclick: e => { e.stopPropagation(); S.tab = 'worklog'; S.worklog = stem + '/' + tool; render(); },
  }, label || t('worklog'));
}
/* The worklog a section drills into, resolved from its `<!-- tool: X -->` / `<!-- synthesis -->`
   marker — returned only if the model actually carries that worklog for this step, else null. */
function worklogTool(stem, body) {
  const logs = (S.model.worklogs || {})[stem];
  if (!logs || !body) return null;
  const m = body.match(/<!--\s*tool:\s*([a-z0-9-]+)\s*-->/);
  const tool = m ? m[1] : (/<!--\s*synthesis/.test(body) ? 'synthesis' : null);
  return tool && logs[tool] ? tool : null;
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
    [].concat(mk.hypotheses || [], mk.risks || [], mk.metrics || [],
      mk.features || [], mk.surfaces || []).forEach(id => {
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
function lastPassDate(m) {
  return ((m.last_pass || '').match(/\d{4}-\d{2}-\d{2}/) || [''])[0];
}

function viewOverview() {
  const m = S.model;
  if (m.umbrella) return viewUmbrella();
  const reg = m.registers;
  const gateAll = m.steps.reduce((a, s) => a + s.gate.length, 0);
  const gateDone = m.steps.reduce((a, s) => a + (s.gate_counts.done || 0), 0);
  const openGates = m.steps.reduce((a, s) =>
    a + s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown').length, 0);
  const hStatus = k => reg.hypotheses.rows.filter(r =>
    stripMd(cell(r, 'status')).toLowerCase().startsWith(k)).length;
  const risksLive = reg.risks.rows.filter(r =>
    /open|mitigat|открыт|митиг/i.test(stripMd(cell(r, 'status')))).length;
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
        // one label per element: only the DATE of the last pass — the full move-5 narrative in
        // state.yaml is prose, and inlining it here blew the card up and broke the figs row
        m.current_step ? `${t('of6')}${lastPassDate(m) ? ' · ' + t('lastPass') + ' ' + lastPassDate(m) : ''}`
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
        h('td', { class: 'id' }, h('b', { style: here ? 'color:var(--brand-ink)' : null }, s.step),
          h('span', { style: 'margin-left:9px' }, dualRing(s, 24))),
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
    elseRows.push(h('tr', {}, h('td', { class: 'id' }, h('code', {}, 'export-files/')),
      h('td', {}, m.deliverables.join(' · ')), h('td', {})));
  }
  if (m.directions.length) {
    elseRows.push(h('tr', {}, h('td', { class: 'id' }, h('code', {}, 'directions')),
      h('td', {}, m.directions.join(' · ')), h('td', {})));
  }

  return h('div', {},
    S.snapshot ? snapCover() : null,
    thesis,
    h('div', { class: 'grid cols-2' },
      sec(t('cascade'), { right: `${gateDone}/${gateAll} ${t('gateDone')}` }, cascade),
      h('div', { style: 'align-self:start' },
        h('div', { class: 'sec' }, next),
        sec(t('instanceReading'), {}, health))),
    m.scope_note ? sec(t('scope'), {}, h('div', { class: 'panel md', html: md(m.scope_note) })) : null,
    sec(t('whatElse'), {}, table([t('file'), t('whatElseCol'), ''], elseRows)));
}

/* The exported file's title screen: who this is, where the cycle stands, and the six steps as dual
   rings — so a stakeholder's first screen answers "where are we" before any navigation. Live console
   viewers already have the chrome for that, so the cover renders only inside a snapshot. */
function snapCover() {
  const m = S.model;
  return h('div', { class: 'cover' },
    h('div', { class: 'kick' },
      `very-ai-product-loops · ${t('snapshot')} · ${t('madeOn')} ${S.snapshot.generated}`),
    h('h2', { class: 'covername' }, m.product),
    h('p', { class: 'coversub' }, [
      m.active_status ? `${t('status')} ${m.active_status}` : null,
      m.current_step ? `${t('step')} ${m.current_step} ${t('of6')}` : t('noState'),
    ].filter(Boolean).join(' · ')),
    m.goal ? h('p', { class: 'lead', style: 'margin-top:9px' }, m.goal) : null,
    h('div', { class: 'coversteps' }, m.steps.map(s => h('button', {
      class: 'coverstep',
      onclick: () => { S.tab = 'step'; S.step = s.step; render(); },
    }, dualRing(s, 34), h('span', { class: 'cl' }, `${s.step} · ${shortTitle(s.title || s.name)}`)))));
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

/* ---------------------------------------------------------------- step canvas (per-step visuals)
 * A step's gate is nine or ten section targets — which is to say a canvas of the product. So instead
 * of one gate table repeated for every step, each step can draw its own board: the sections laid out
 * the way that step thinks (a product canvas, a market dashboard, a strategy cascade). The gate tick
 * rides on each card as a badge. Nothing is invented: a card's face is the author's `<!-- card -->`
 * line or no face at all (the console renders the two authored layers, it never composes a third
 * text); expanding a card shows the section itself, whole; a section absent from the instance shows
 * a `— to clarify —`, never filler; a section the canvas does not place lands in a trailing zone. */

/* Plain text out of a markdown fragment: drop emphasis, links (keep their text), confidence tags. */
const plain = s => stripMd(String(s || '')
  .replace(/\[(assumption|sourced|validated|refuted)(?::[^\]]*)?\]/g, '')
  .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
  .replace(/<!--[\s\S]*?-->/g, '')
  .replace(/(^|[\s(])_([^_]+)_(?=$|[\s.,;:)])/g, '$1$2')
  .replace(/⚙️?/g, ''))
  .replace(/\s+/g, ' ').trim();

const CONF_TAG_RE = /\s*\[(assumption|sourced|validated|refuted)(?::[^\]]*)?\]/g;

/* The card's excerpt element. A face exists only where the author marked one — a `<!-- card -->`
   line, shown verbatim (the console never composes a gist of its own: worklog and artifact are the
   only authored layers, and the board is a layout of them, not a third text). A section that is not
   written yet reads muted when it is n/a/deferred (nothing owed) and amber "to clarify" otherwise
   (a gap still owed). */
function cvExcerpt(fd, tick) {
  if (!fd || !fd.text) {
    return (tick === 'n/a' || tick === 'deferred')
      ? h('p', { class: 'cvex cv-muted' }, '—')
      : h('p', { class: 'cvex cv-clar' }, t('gapDash'));
  }
  const full = fd.text.replace(CONF_TAG_RE, '').trim();
  // A marked face laid across hard breaks is an enumeration: the first line leads, each line below is
  // an item, so give every continuation line a bullet where it has none — the tile reads as a list.
  const parts = full.split('\n');
  const html = parts
    .map((ln, k) => inline(k > 0 && !/^\s*[-*•·–—]\s/.test(ln) ? '• ' + ln : ln))
    .join('<br>');
  return h('p', { class: 'cvex', title: full.length > 120 ? plain(full) : null, html });
}
const stripHead = b => String(b || '').replace(/^\s*#{1,6}\s.*\n?/, '');

/* The first markdown table in a body → { head:[…], rows:[[…]] }, or null. */
/* A hidden column key on a header cell — `Price <!--c:price-->` — names what the column *means*, so a
   board can read the column across any language and any reordering instead of guessing from the prose.
   It is the same "mark, don't guess" idea a heading's `{#anchor}` already applies to sections. */
const COL_KEY_RE = /<!--\s*c(?:ol)?:\s*([\w-]+)\s*-->/i;
function firstTable(body) {
  const lines = String(body || '').split('\n');
  let i = 0;
  while (i < lines.length) {
    const l = lines[i].trim(), nx = (lines[i + 1] || '').trim();
    if (l.startsWith('|') && /-/.test(nx) && /^\|?[\s:|-]+\|?$/.test(nx)) {
      const cells = l.replace(/^\||\|$/g, '').split('|').map(c => c.trim());
      const keys = cells.map(c => (c.match(COL_KEY_RE) || [])[1] || null);   // one per column, null if unmarked
      const head = cells.map(c => c.replace(COL_KEY_RE, '').trim());          // display text, the mark stripped
      const rows = [];
      i += 2;
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        rows.push(lines[i].trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
        i++;
      }
      return { head, keys, rows };
    }
    i++;
  }
  return null;
}
/* The index of a column by its stable <!--c:key--> mark on the header (survives translation and
   reordering), or -1 if the table does not carry it. The mark is the only join — no positional
   fallback and no header-prose alias, both being the language traps the key removes — so an instance
   the console reads must key its columns (enforced by linter check O2). */
const colKey = (tbl, key) => (tbl ? (tbl.keys || []).indexOf(key) : -1);
/* A competitor's join key across the four competitor tables: first significant word, lowercased. */
const compKey = s => (plain(s).toLowerCase().split(/[\s(/,]+/).filter(Boolean)[0] || '');
/* An H / M / L cell that carries its own colour, so likelihood and impact read without the header. */
const hlBadge = v => {
  const s = String(v || '').trim();
  const k = /^h/i.test(s) ? 'err' : /^m/i.test(s) ? 'open' : /^l/i.test(s) ? 'done' : 'na';
  return h('span', { class: 'tag ' + k }, s || '—');
};

/* The info dot by a step heading: the block the active status asks, folded into a hover/tap tooltip. */
function tipBelow(html, el) {
  tip.innerHTML = html;
  tip.classList.add('on');
  const w = tip.getBoundingClientRect().width, r = el.getBoundingClientRect();
  tip.style.left = Math.min(window.innerWidth - w - 10, Math.max(8, r.left)) + 'px';
  tip.style.top = (r.bottom + 8) + 'px';
}
function infoDot(html, label) {
  const b = h('span', { class: 'idot', tabindex: '0', role: 'button', 'aria-label': label || t('statusAsks') }, 'i');
  const show = () => tipBelow(html, b);
  b.addEventListener('mouseenter', show);
  b.addEventListener('focus', show);
  b.addEventListener('mouseleave', hideTip);
  b.addEventListener('blur', hideTip);
  b.addEventListener('click', e => { e.stopPropagation(); tip.classList.contains('on') ? hideTip() : show(); });
  return b;
}
function asksTip(perStep, m) {
  const goals = (perStep.goals || []).map(g => `<li>${esc(g)}</li>`).join('');
  const tools = (perStep.tools || []).map(x => `<b>${esc(x)}</b>`).join(' ');
  return `<div class="k">${esc(t('statusAsks'))} · ${esc(m.active_status || '')}</div>`
    + (goals ? `<ul>${goals}</ul>` : '')
    + (tools ? `<div class="asktools"><span class="k">${esc(t('emphasised'))}:</span> ${tools}</div>` : '');
}

/* One canvas card: a section's title, its gate tick, a short excerpt, the verb to open it. A section
   present in the model but empty shows a gap mark; a section the instance does not define is skipped
   (the slot is not invented). The whole card navigates to the section it stands for. */
function cvCard(s, id, opts) {
  const o = opts || {};
  const meta = s.sections.find(x => x.id === id);
  if (!meta) return null;
  const gate = s.gate.find(g => (g.sections || []).includes(id));
  const tick = gate ? gate.tick : null;
  const live = meta.present && s.artifact_file;
  const art = live ? artSection(s.artifact_file, id) : null;
  // The face is the author's `<!-- card -->` line, verbatim — or no face at all: an unmarked section
  // shows just its title and tags. Only an unwritten section shows the gap mark.
  const face = art
    ? (art.card ? cvExcerpt({ text: art.card }, tick) : null)
    : cvExcerpt(null, tick);
  // Interaction: the tile expands in place into the section itself, whole and verbatim (the card is a
  // collapsed section, not a summary of one); it widens to the full row (see .cvcard.expanded). The
  // "details" link is the one thing that leaves, for the section in the artifact.
  const stem = s.artifact_file ? s.artifact_file.replace(/\.md$/, '') : '';
  const wlTool = live && art ? worklogTool(stem, art.body) : null;
  const xpand = h('span', { class: 'cvxpand', 'aria-hidden': 'true' });
  const foot = live ? h('div', { class: 'cvfoot' },
    goSection(s.artifact_file, id, t('more'), meta.title || id),
    wlTool ? goWorklog(stem, wlTool) : null,
    wlTool ? wlNewerTag(s, wlTool) : null, xpand) : null;
  // Two quiet lines above the face: the title with its gate tick (top-right, the process axis), then
  // the sign-off state with the evidence strip stretched beside it (the semantic axis). Splitting the
  // rows keeps a long title from shuffling the tags, and gives the strip a full line to be legible on.
  const conf = confTag(meta);
  const strip = live ? evStrip(meta.confidence) : null;
  const card = h('div', { class: 'cvcard' + (o.hero ? ' cv-hero' : '') + (o.warn ? ' cv-warn' : '')
    + (live ? ' cv-link' + (art ? ' can-expand' : '') : ' cv-gap') },
    h('div', { class: 'cvtop' },
      h('span', { class: 'cvttl' }, meta.title || id),
      tick ? tickTag(tick) : null),
    (conf || strip) ? h('div', { class: 'cvmeta' }, conf, strip) : null,
    face,
    foot);
  if (live && art) {
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
    card.setAttribute('aria-expanded', 'false');
    card.title = t('expand');
    let full = null;
    const toggle = () => {
      // built once, on first open — the section body rendered whole, above the footer
      if (!full) { full = h('div', { class: 'cvfull md', html: md(stripHead(art.body)) }); card.insertBefore(full, foot); }
      card.setAttribute('aria-expanded', card.classList.toggle('expanded') ? 'true' : 'false');
    };
    // A click anywhere on the tile expands/collapses it — except on the "details" link, which navigates.
    card.addEventListener('click', e => { if (!e.target.closest('.golink')) toggle(); });
    card.addEventListener('keydown', e => {
      if ((e.key === 'Enter' || e.key === ' ') && !e.target.closest('.golink')) { e.preventDefault(); toggle(); }
    });
  }
  return card;
}
const cvZone = label => h('div', { class: 'cvzone' }, label);
const bodyOf = (s, id) => {
  const m = s.sections.find(x => x.id === id);
  return m && m.present && s.artifact_file ? artSection(s.artifact_file, id) : null;
};

/* A labelled zone of section cards — the workhorse of every step canvas. Absent sections drop out; an
   empty zone (no card at all) is skipped so a step draws only the zones it actually has. */
function cardZone(s, label, ids) {
  const cards = ids.map(id => cvCard(s, id)).filter(Boolean);
  return cards.length ? [cvZone(label), h('div', { class: 'cvrow' }, cards)] : null;
}
/* A row of cards read as a sequence, with an arrow between each — the Playing-to-Win cascade. */
function cascade(s, ids) {
  const cards = ids.map(id => cvCard(s, id)).filter(Boolean);
  if (!cards.length) return null;
  const row = [];
  cards.forEach((c, i) => {
    if (i) row.push(h('div', { class: 'casc-arrow', 'aria-hidden': 'true' }, '→'));
    row.push(c);
  });
  return h('div', { class: 'cascade' }, row);
}
/* Two sections side by side — the sprint's committed set against its backlog. */
function board2(s, leftId, rightId) {
  const cards = [cvCard(s, leftId), cvCard(s, rightId)].filter(Boolean);
  return cards.length ? h('div', { class: 'board2' }, cards) : null;
}

/* Step 1 — the passport as a product canvas: the concept on top, then the customer, product and
   validation zones. Each card is one gate section. */
function canvasIdea(s) {
  const kids = [
    cvCard(s, 'idea', { hero: true }),   // the template's anchor is {#idea} — 'concept' matched nothing
    cardZone(s, t('zCustomer'), ['segments', 'jtbd', 'problems', 'cjm']),
    cardZone(s, t('zProduct'), ['solution', 'value-defensibility']),
    cardZone(s, t('zValidation'), ['hypotheses', 'to-clarify']),
  ].filter(Boolean).flat();
  return kids.length ? h('div', { class: 'canvas' }, kids) : null;
}
/* Step 3 — the strategy as a Playing-to-Win canvas: the aspiration→where→how cascade on top, then the
   commercial, product and bets zones. */
function canvasStrategy(s) {
  const parts = [];
  const casc = cascade(s, ['winning-aspiration', 'where-to-play', 'how-to-win']);
  if (casc) parts.push(cvZone(t('z3Cascade')), casc);
  [[t('z3Commercial'), ['uvp-cpv', 'pricing', 'channels-expansion']],
   [t('z3Product'), ['product-surface', 'architecture']],
   [t('z3Bets'), ['bets', 'product-risks']],
   [t('z3Open'), ['to-clarify']]].forEach(([lab, ids]) => {
    const z = cardZone(s, lab, ids); if (z) parts.push(...z);
  });
  return parts.length ? h('div', { class: 'canvas' }, parts) : null;
}
/* Step 4 — the strategic plan around its metric tree: the North Star hero on top, then economics,
   instrumentation & risk, and the quantified hypotheses. */
function canvasStrategicPlan(s) {
  const parts = [];
  const hero = cvCard(s, 'metric-tree', { hero: true });
  if (hero) parts.push(cvZone(t('z4North')), hero);
  [[t('z4Econ'), ['unit-economics', 'financial-model', 'retention', 'strategic-targets']],
   [t('z4Instr'), ['architecture-instrumentation', 'risk-mitigation', 'capabilities']],
   [t('z4Hyp'), ['global-hypotheses', 'open-questions']]].forEach(([lab, ids]) => {
    const z = cardZone(s, lab, ids); if (z) parts.push(...z);
  });
  return parts.length ? h('div', { class: 'canvas' }, parts) : null;
}
/* Step 5 — the tactical plan: goals & targets on top, the guardrails as a red-lined band of their own
   (what must not break), then resources & market, tests & blockers. */
function canvasTacticalPlan(s) {
  const parts = [];
  const goals = cardZone(s, t('z5Goals'), ['period-goals', 'goal-targets']);
  if (goals) parts.push(...goals);
  const guard = cvCard(s, 'guardrails', { hero: true, warn: true });
  if (guard) parts.push(cvZone(t('z5Guard')), guard);
  [[t('z5Res'), ['resources', 'market-bundles']],
   [t('z5Test'), ['hypotheses-to-test', 'readouts', 'item-readouts', 'blockers', 'to-clarify']]].forEach(([lab, ids]) => {
    const z = cardZone(s, lab, ids); if (z) parts.push(...z);
  });
  return parts.length ? h('div', { class: 'canvas' }, parts) : null;
}
/* Step 6 — the sprint board. When the must-set parses into items (the template's F-/A-/T- blocks,
   read by the shared layer into model.sprint_items), each item gets a card of its own, grouped by
   direction — a feature shows its Description / Scope / Acceptance / values / stories, an activity
   and a task their own formats, all with the labels the instance actually wrote. The backlog stays
   what it is — a ranked table. An instance whose must-set the parser doesn't recognise falls back
   to the two-section board, so drift degrades, never hides. */
function itemCard(s, it) {
  const lc = k => k.toLowerCase();
  const fields = it.fields || [];
  const get = name => (fields.find(([k]) => lc(k) === name) || [])[1];
  const desc = get('description');
  const groom = get('groom');
  const foot = ['owner', 'estimate'].map(k => get(k)).filter(Boolean);
  const rows = fields.filter(([k]) =>
    !['description', 'owner', 'estimate', 'groom'].includes(lc(k)));
  const dirCls = { development: 'it-dev', 'go-to-market': 'it-g2m', 'back-office': 'it-bo' }[it.direction] || '';
  return h('div', { class: 'itcard ' + dirCls },
    h('div', { class: 'ithead' },
      h('code', { class: 'itid' }, it.id),
      h('b', { class: 'itname' }, it.name),
      groom ? h('span', { class: 'tag ' + (/^spec-ready/i.test(groom) ? 'done' : 'open') },
        plain(groom).slice(0, 28)) : null),
    // the item's feature-register row (model.sprint_items[].feature) joins the head-line links as a
    // chip — the F-… tie is register wiring, not just prose in the Feature field below
    (chips => chips.length ? h('div', { class: 'row', style: 'margin:2px 0 0' },
      ridChips(chips)) : null)(
      (it.links || []).concat(it.feature && !(it.links || []).includes(it.feature) ? [it.feature] : [])),
    desc ? h('div', { class: 'itdesc', html: inline(desc) }) : null,
    rows.length ? h('div', { class: 'wiring itwiring' }, rows.map(([k, v]) =>
      h('div', { class: 'wrow' }, h('div', { class: 'wk' }, k),
        h('div', { class: 'wv md', html: md(v) })))) : null,
    foot.length ? h('div', { class: 'itfoot' }, foot.join(' · ')) : null);
}

function canvasSprintPlan(s) {
  const parts = [];
  const goal = cvCard(s, 'sprint-goal', { hero: true });
  if (goal) parts.push(goal);
  const items = S.model.sprint_items || [];
  if (items.length) {
    const must = s.sections.find(x => x.id === 'must');
    parts.push(h('div', { class: 'cvzone' }, t('z6Items'), confTag(must),
      goSection(s.artifact_file, 'must', t('more'))));
    [['development', t('dirDev')], ['go-to-market', t('dirG2m')], ['back-office', t('dirBo')]]
      .forEach(([key, label]) => {
        const group = items.filter(x => x.direction === key);
        if (!group.length) return;
        parts.push(h('div', { class: 'itdir' }, label),
          h('div', { class: 'itgrid' }, group.map(it => itemCard(s, it))));
      });
    const bl = mdBlock(s, 'backlog');
    if (bl) parts.push(h('div', { class: 'cvzone' }, t('z6Backlog'),
      goSection(s.artifact_file, 'backlog', t('more'))), bl);
  } else {
    const b2 = board2(s, 'must', 'backlog');
    if (b2) parts.push(cvZone(t('z6Commit')), b2);
  }
  const ex = cardZone(s, t('z6Excluded'), ['excluded']);
  if (ex) parts.push(...ex);
  const ho = mdBlock(s, 'delivery', 'callout');   // the template's anchor is {#delivery} — 'handoff' matched nothing
  if (ho) parts.push(cvZone(t('z6Handoff')), ho);
  const open = cardZone(s, t('z3Open'), ['to-clarify']);
  if (open) parts.push(...open);
  return parts.length ? h('div', { class: 'canvas' }, parts) : null;
}

/* Step 2 — the analysis as a market dashboard: sizing tiles, one competitor table assembled from the
   four competitor sections, substitutes on their own, the opportunity as a callout, risks compact. */
function marketBoard(s) {
  const a = bodyOf(s, 'market-sizing');
  const tbl = a ? firstTable(a.body) : null;
  const money = c => (String(c).match(/[$€£]\s?[\d.,]+(?:\s*[–—-]\s*[$€£]?[\d.,]+)?\s*(?:[KMB]|bn|trn|млрд|млн)?/i) || [])[0];
  const est = key => {
    if (!tbl) return null;
    const i = colKey(tbl, 'value');
    const row = tbl.rows.find(r => new RegExp('^' + key, 'i').test(plain(r[0])));
    if (!row) return null;
    const cell = row[i >= 0 ? i : 1] || '';
    const bold = (cell.match(/\*\*([^*]+)\*\*/) || [])[1];
    let v = plain(bold || '') || money(cell) || plain(cell);
    if (v.length > 22) v = v.slice(0, 22).replace(/\s+\S*$/, '') + '…';
    return v || null;
  };
  const cagr = a ? (a.body.match(/CAGR[^0-9]*([0-9][0-9.,]*(?:\s*[–—-]\s*[0-9.,]+)?\s*%)/i) || [])[1] : null;
  const tile = (lab, key, sub, key2) => {
    const v = est(key);
    return h('div', { class: 'mtile' + (key2 ? ' mtile-key' : '') + (v ? '' : ' cv-gap') },
      h('div', { class: 'ml' }, lab),
      h('div', { class: 'mv' }, v || t('gapDash')),
      h('div', { class: 'ms' }, sub));
  };
  const tiles = [
    tile('TAM', 'TAM', t('mTam')),
    tile('SAM', 'SAM', t('mSam'), true),
    tile('SOM', 'SOM', t('mSom')),
    cagr ? h('div', { class: 'mtile' }, h('div', { class: 'ml' }, 'CAGR'),
      h('div', { class: 'mv' }, cagr), h('div', { class: 'ms' }, t('mCagr'))) : null,
  ].filter(Boolean);
  return tiles.length ? h('div', { class: 'mboard' }, tiles) : null;
}
function competitorTable(s) {
  const tbl = id => { const a = bodyOf(s, id); return a ? firstTable(a.body) : null; };
  const base = tbl('competitors');
  if (!base) return null;
  // Each column is read by its stable <!--c:key--> mark (colKey) — no header-prose alias, no positional
  // fallback; the mark is the only join, so it holds in any language.
  const mapBy = (t2, key) => {
    const map = {};
    if (t2) { const ci = colKey(t2, key); if (ci >= 0) t2.rows.forEach(r => { const k = compKey(r[0]); if (k && !(k in map)) map[k] = r[ci]; }); }
    return map;
  };
  const strat = tbl('competitor-strategy'), price = tbl('competitor-pricing'), dyn = tbl('competitor-dynamics');
  const play = mapBy(strat, 'play'),
    moat = mapBy(strat, 'moat'),
    pr = mapBy(price, 'price'),
    dy = mapBy(dyn, 'trend');
  const ti = colKey(base, 'type'),
    oi = colKey(base, 'offer');
  const dash = x => (x && x.trim()) ? inline(x) : '—';
  const rows = base.rows.map(r => {
    const k = compKey(r[0]);
    return h('tr', {},
      h('td', { html: inline(r[0]) }),
      h('td', { html: dash(ti >= 0 ? r[ti] : '') }),
      h('td', { class: 'prose', html: dash(play[k] || (oi >= 0 ? r[oi] : '')) }),
      h('td', { class: 'prose', html: dash(moat[k]) }),
      h('td', { html: dash(pr[k]) }),
      h('td', { class: 'prose', html: dash(dy[k]) }));
  });
  return h('div', {},
    table([t('cName'), t('cType'), t('cPlay'), t('cMoat'), t('cPrice'), t('cDyn')], rows),
    h('p', { class: 'small faint', style: 'margin-top:7px' }, t('assembledFrom')));
}
function mdBlock(s, id, cls) {
  const a = bodyOf(s, id);
  return a ? h('div', { class: cls || '' }, h('div', { class: 'md', html: md(stripHead(a.body)) })) : null;
}
function riskBoard(s) {
  const a = bodyOf(s, 'niche-risks');
  const tbl = a ? firstTable(a.body) : null;
  if (!tbl) return null;
  const ri = colKey(tbl, 'risk'), fi = colKey(tbl, 'force'),
    li = colKey(tbl, 'likelihood'), ii = colKey(tbl, 'impact'),
    idi = colKey(tbl, 'register');
  const rows = tbl.rows.map(r => h('tr', {},
    h('td', { class: 'prose', html: inline(r[ri >= 0 ? ri : 0]) }),
    h('td', { html: inline(fi >= 0 ? r[fi] : '') }),
    h('td', {}, hlBadge(li >= 0 ? plain(r[li]) : '')),
    h('td', {}, hlBadge(ii >= 0 ? plain(r[ii]) : '')),
    h('td', { html: idi >= 0 ? inline(r[idi]) : '' })));
  return table([t('risks'), t('rForce'), t('rLik'), t('rImp'), 'R-…'], rows);
}
function canvasAnalysis(s) {
  const parts = [];
  const stem = s.artifact_file ? s.artifact_file.replace(/\.md$/, '') : '';
  // step 2's custom boards don't go through cvCard, so the worklog drill-through is hung on the zone
  // header here: the primary section `id` behind the board names its method, and goWorklog opens it.
  const push = (label, node, id) => {
    if (!node) return;
    const a = id ? bodyOf(s, id) : null;
    const tool = a ? worklogTool(stem, a.body) : null;
    const meta = id ? s.sections.find(x => x.id === id) : null;
    parts.push(h('div', { class: 'cvzone' }, label, confTag(meta),
      meta ? evStrip(meta.confidence, 'inline') : null,
      tool ? goWorklog(stem, tool) : null,
      tool ? wlNewerTag(s, tool) : null), node);
  };
  push(t('dMarket'), marketBoard(s), 'market-sizing');
  push(t('dCompetitors'), competitorTable(s), 'competitors');
  push(t('dSubstitutes'), mdBlock(s, 'substitutes'), 'substitutes');
  push(t('dOpportunity'), mdBlock(s, 'opportunity', 'callout'), 'opportunity');
  push(t('dRisks'), riskBoard(s), 'niche-risks');
  // the two sections the dashboard widgets don't draw — as ordinary cards, so nothing goes missing
  const hyp = cardZone(s, t('z4Hyp'), ['hypotheses']);
  if (hyp) parts.push(...hyp);
  const open = cardZone(s, t('z3Open'), ['to-clarify']);
  if (open) parts.push(...open);
  return parts.length ? h('div', { class: 'canvas' }, parts) : null;
}
const STEP_CANVAS = {
  1: { fn: canvasIdea, title: 'boardIdea' },
  2: { fn: canvasAnalysis, title: 'boardAnalysis' },
  3: { fn: canvasStrategy, title: 'boardStrategy' },
  4: { fn: canvasStrategicPlan, title: 'boardStratPlan' },
  5: { fn: canvasTacticalPlan, title: 'boardTactical' },
  6: { fn: canvasSprintPlan, title: 'boardSprint' },
};
/* The section ids each canvas above places — mirrored by hand, read only to find leftovers: a
   section the canvas does not know (an instance's own addition, or a template ahead of the console)
   still reaches the board, as a card in a trailing zone. */
const PLACED = {
  1: ['idea', 'segments', 'jtbd', 'problems', 'cjm', 'solution', 'value-defensibility', 'hypotheses', 'to-clarify'],
  2: ['market-sizing', 'competitors', 'competitor-strategy', 'competitor-pricing', 'competitor-dynamics',
    'substitutes', 'opportunity', 'niche-risks', 'hypotheses', 'to-clarify'],
  3: ['winning-aspiration', 'where-to-play', 'how-to-win', 'uvp-cpv', 'pricing', 'channels-expansion',
    'product-surface', 'architecture', 'bets', 'product-risks', 'to-clarify'],
  4: ['metric-tree', 'unit-economics', 'financial-model', 'retention', 'strategic-targets',
    'architecture-instrumentation', 'risk-mitigation', 'capabilities', 'global-hypotheses', 'open-questions'],
  5: ['period-goals', 'goal-targets', 'guardrails', 'resources', 'market-bundles',
    'hypotheses-to-test', 'readouts', 'item-readouts', 'blockers', 'to-clarify'],
  6: ['sprint-goal', 'must', 'backlog', 'excluded', 'delivery', 'to-clarify'],
};

/* ---------------------------------------------------------------- the step */
function viewStep() {
  const m = S.model;
  if (!m.steps.length) return h('div', { class: 'empty' }, t('nothingYet'));
  const s = m.steps.find(x => x.step === S.step) || m.steps[0];
  S.step = s.step;
  const perStep = (m.status && m.status.per_step && m.status.per_step[String(s.step)]) || null;
  const written = s.sections.filter(x => x.present).length;
  const gaps = s.sections.reduce((a, x) => a + (x.gaps || 0), 0);
  const proposals = s.sections.reduce((a, x) => a + (x.proposals || 0), 0);

  // The active status rides next to the step title as a badge, and the two reference texts — the
  // step's framework goal and what the status asks here — fold into info dots beside it: reference,
  // on demand, not a column. The goal dot hugs the title (it describes the step); the asks dot hugs
  // the status badge (it describes the stage).
  const asksHtml = perStep ? asksTip(perStep, m) : null;
  const goalHtml = s.goal
    ? `<div class="k">${esc(t('stepGoal'))}</div><p>${esc(s.goal)}</p>` : null;
  const head = h('div', { class: 'sec' },
    h('div', { class: 'kick' }, `${t('step')} ${s.step} ${t('of6')} · ${s.cadence || ''}`),
    h('div', { class: 'titlerow' },
      dualRing(s, 38),
      h('h2', { style: 'font-size:25px;letter-spacing:-.025em' }, shortTitle(s.title || s.name)),
      goalHtml ? infoDot(goalHtml, t('stepGoal')) : null,
      m.active_status ? h('span', { class: 'tag stagebadge', title: t('status') }, m.active_status) : null,
      asksHtml ? infoDot(asksHtml) : null),
    h('div', { class: 'figs', style: 'margin-top:16px' },
      fig(t('filled'), `${written}`, `${t('of')} ${s.sections.length} ${t('sections')}`),
      fig(t('gateClosed'), `${(s.gate_counts.done || 0)}`, `${t('of')} ${s.gate.length}`),
      (cc => fig(t('confirmed'), `${cc.done}`, `${t('of')} ${cc.total} ${t('sectionsShort')}`,
        null, cc.total > 0 && cc.done < cc.total))(confCounts(s)),
      fig(t('toClarify'), String(gaps), gaps ? t('gaps') : '', null, gaps > 0),
      fig(t('proposals'), String(proposals), ''),
      s.artifact_file ? fig(t('artifact'), h('span', { style: 'font-size:14px;font-family:var(--mono)' },
        s.artifact_file), s.artifact_updated || '') : null));

  // The gate's `targets` are the same sections the links point at, so the link *is* the column: one
  // less column of mono text broken across five lines in a narrow rail.
  const gateTable = table([t('state'), t('gateItem'), t('validates')],
    s.gate.map(g => h('tr', {},
      h('td', {}, tickTag(g.tick)),
      h('td', { class: 'prose', html: inline(g.label) }),
      h('td', { class: 'refs' },
        s.artifact_file ? (g.sections || []).map(id => goSection(s.artifact_file, id, '#' + id)) : null,
        g.register ? h('span', { class: 'tag met' }, g.register) : null))));

  // The board IS the reading: every section is a card (collapsed = title + the author's card line;
  // expanded = the section itself), so there is no duplicate section list underneath. Where a step has
  // a canvas of its own it draws that, with each gate tick riding on its card; otherwise it falls back
  // to the plain gate table. Sections the canvas does not place land in a trailing zone.
  const cv = STEP_CANVAS[s.step];
  const board = cv ? cv.fn(s) : null;
  const left = cv ? cardZone(s, t('zOther'),
    s.sections.map(x => x.id).filter(id => !(PLACED[s.step] || []).includes(id))) : null;
  const frame = board
    ? sec(t(cv.title), { right: gateSummary(s) }, h('div', {}, board, ...(left || [])))
    : sec(t('gate'), { right: gateSummary(s) }, gateTable);

  return h('div', {}, head, frame);
}

/* ---------------------------------------------------------------- artifacts */
/* The reader opens a whole artifact — the projection is one document, and reading it in slices hid
   the through-line. Under the open file the TOC lists its worklogs (worklog = source of truth,
   artifact = projection — three homes), so the drill goes file → workings, not file → slice. A
   section id arriving in the hash or from a cross-link still lands: the page scrolls to it. */
function viewArtifacts() {
  const m = S.model;
  if (!m.artifacts.length) return h('div', { class: 'empty' }, t('nothingYet'));
  const art = m.artifacts.find(a => a.file === S.artifact) || m.artifacts[0];
  S.artifact = art.file;
  const stemOf = f => f.replace(/\.md$/, '');

  const toc = h('div', { class: 'toc' }, m.artifacts.map(a => {
    const open = a.file === art.file;
    const logs = (m.worklogs || {})[stemOf(a.file)] || {};
    const gaps = a.sections.reduce((n, x) => n + x.gaps.length, 0);
    const gears = a.sections.reduce((n, x) => n + (x.markers.proposals || 0), 0);
    return [
      h('button', { 'aria-current': open,
        onclick: () => { S.artifact = a.file; S.section = null; render(); } },
        h('span', { class: 'fname' }, a.file), h('span', { class: 'dotcol' },
          gaps ? h('i', { class: 'pip gap', title: `${gaps} ${t('gaps')}` }) : null,
          gears ? h('i', { class: 'pip gear', title: t('proposals') }) : null)),
      open ? Object.keys(logs).sort().map(tool => h('button', {
        class: 'tocwl', title: logs[tool].file,
        onclick: () => { S.tab = 'worklog'; S.worklog = stemOf(a.file) + '/' + tool; render(); },
      }, h('span', {}, tool), h('span', { class: 'wldate' }, logs[tool].updated || ''))) : null,
    ];
  }));

  const stepOf = m.steps.find(x => x.artifact_file === art.file);
  const stem = stemOf(art.file);
  const secBlocks = art.sections.map(x => {
    const ids = [...new Set([].concat(x.markers.hypotheses, x.markers.risks, x.markers.metrics,
      x.markers.features || [], x.markers.surfaces || []))];
    const tool = worklogTool(stem, x.body);
    return h('div', { class: 'artsec', id: 'sec-' + x.id },
      h('div', { class: 'row', style: 'flex-wrap:wrap;margin:0 0 2px' },
        h('h3', { style: 'font-size:16px;letter-spacing:-.02em;margin:0' }, x.title || x.id),
        h('code', { class: 'tag' }, '#' + x.id),
        confTag({ present: true, confirmed: x.confirmed, confirmed_by: x.confirmed_by,
          contested: x.contested, open: x.open }),
        restTag(x),
        stepOf && tool ? wlNewerTag(stepOf, tool) : null,
        confChips(x.markers.confidence),
        x.markers.proposals ? h('span', { class: 'gear' },
          `${t('proposalMark')} ×${x.markers.proposals}`) : null,
        ridChips(ids)),
      h('div', { class: 'md', html: md(x.body) }));
  });

  const body = h('div', {},
    h('div', { class: 'kick' }, `${art.file} · ${art.updated || ''}`),
    h('div', { class: 'spread' },
      h('h2', { style: 'font-size:20px;letter-spacing:-.02em' }, art.title || art.file),
      h('span', { class: 'row' },
        art.status_stage ? h('span', { class: 'tag' }, art.status_stage) : null,
        art.version ? h('span', { class: 'tag' }, 'v' + art.version) : null,
        stepOf ? goStep(stepOf.step) : null)),
    ...secBlocks);

  // a cross-link or deep link names a section: scroll to it once the DOM is on the page
  if (S.section) requestAnimationFrame(() => {
    const el = document.getElementById('sec-' + S.section);
    if (el) el.scrollIntoView({ block: 'start' });
  });

  return h('div', { class: 'reader' }, toc, h('div', { class: 'panel' }, body));
}

/* ---------------------------------------------------------------- registers */
/* The product, by surface: one column per S-… row, carrying the features that name it — the
   register drawn as the thing it describes. Colour is the row's state (live / planned / retired);
   a feature a current must-item advances is flagged, and a card click opens the feature's row in
   the register table below (its trail and serves-links live there — no second detail view). */
function surfaceBoard(m) {
  const feats = m.registers.features.rows;
  const surfs = m.registers.surfaces.rows;
  if (!feats.length && !surfs.length) return null;
  const mustFeat = new Set((m.sprint_items || []).map(it => it.feature).filter(Boolean));
  const named = new Set();
  const card = f => {
    const fid = stripMd(cell(f, 'id'));
    const state = stripMd(cell(f, 'state')).split(/[\s·]/)[0];
    const prio = stripMd(cell(f, 'priority')).split(/[\s·]/)[0];
    const serves = String(cell(f, 'serves') || '').match(/\b(?:[HRBFS]-\d+|M-[a-z0-9][a-z0-9-]*)\b/g) || [];
    return h('button', { class: 'sfcard sf-' + (state || 'unknown'),
      onclick: () => { S.reg = 'features'; S.regItem = fid; S.regFilter = 'all'; render(); } },
      h('div', { class: 'row' },
        h('code', { class: 'rid feat' }, fid),
        h('span', { class: 'tag ' + (state === 'live' ? 'done' : '') }, state || '—'),
        prio === 'now' ? h('span', { class: 'tag prio-now' }, t('prioNow')) : null,
        mustFeat.has(fid) ? h('span', { class: 'tag must' }, t('inMust')) : null),
      h('div', { class: 'sfname' }, stripMd(cell(f, 'name'))),
      serves.length ? h('div', { class: 'row', style: 'margin-top:4px' }, ridChips(serves)) : null);
  };
  const cols = surfs.map(srow => {
    const sid = stripMd(cell(srow, 'id'));
    const mine = feats.filter(f => stripMd(cell(f, 'surface')).includes(sid));
    mine.forEach(f => named.add(stripMd(cell(f, 'id'))));
    const sstate = stripMd(cell(srow, 'state')).split(/[\s·]/)[0];
    return h('div', { class: 'sfcol' },
      h('div', { class: 'sfhead' },
        h('code', { class: 'rid surf' }, sid),
        h('b', {}, stripMd(cell(srow, 'name'))),
        h('span', { class: 'tag ' + (sstate === 'live' ? 'done' : '') }, sstate || '—')),
      h('div', { class: 'sftype tiny faint' }, stripMd(cell(srow, 'type'))),
      mine.map(card));
  });
  const orphans = feats.filter(f => !named.has(stripMd(cell(f, 'id'))));
  if (orphans.length) cols.push(h('div', { class: 'sfcol sf-orphan' },
    h('div', { class: 'sfhead' }, h('b', {}, t('noSurfaceCol'))), orphans.map(card)));
  return h('div', {},
    h('div', { class: 'kick', style: 'margin-top:14px' }, t('surfaceBoard')),
    h('div', { class: 'tiny faint', style: 'margin:2px 0 8px' }, t('surfaceBoardNote')),
    h('div', { class: 'sfboard' }, cols));
}

function viewRegisters() {
  const m = S.model;
  const which = S.reg;
  const reg = m.registers[which === 'metrics' ? 'metric_tree' : which];
  const tabs = h('div', { class: 'filters' }, [
    ['hypotheses', `${t('hypotheses')} · ${m.registers.hypotheses.rows.length}`],
    ['risks', `${t('risks')} · ${m.registers.risks.rows.length}`],
    ['metrics', `${t('metricNodes')} · ${m.registers.metric_tree.rows.length}`],
    ['features', `${t('features')} · ${m.registers.features.rows.length}`],
    ['surfaces', `${t('surfaces')} · ${m.registers.surfaces.rows.length}`],
  ].map(([k, lab]) => h('button', {
    'aria-pressed': which === k,
    onclick: () => { S.reg = k; S.regFilter = 'all'; S.regItem = null; render(); },
  }, lab)));

  if (!reg.present) return h('div', {}, tabs, h('div', { class: 'empty' }, `${reg.file} — ${t('nothingYet')}`));

  const enums = m.framework.enums;
  // Each register column is addressed by its stable key (`reg.col_keys`, from the header `<!--c:key-->`
  // marks), so the console finds Type / Тип / Tipo the same way — the register version of the
  // section `{#anchor}`. A not-yet-keyed register falls back to the language aliases. `byKey` maps a
  // canonical key to the header prose it actually carries; `colOf` resolves key → header, alias last.
  const byKey = {};
  (reg.col_keys || []).forEach((k, i) => { if (k && reg.columns[i]) byKey[k] = reg.columns[i]; });
  const colOf = key => byKey[key] || key;   // key → the header prose it carries; no header-name fallback
  const idHeader = colOf('id');
  // Per register: the facet column the filter buttons cut by (enum-guarded where the canon closes
  // it — a feature's direction and a surface's type are instance vocabulary, not enums), and the
  // state column. Status/state is a state machine (REGISTERS → the four-sign test), so it earns the
  // enum guard — a stale or mistyped value would otherwise render silently.
  const SPEC = {
    hypotheses: { facet: 'type', facetEnum: 'hypothesis type', state: 'status', stateEnum: 'hypothesis status' },
    risks: { facet: 'category', facetEnum: 'risk category', state: 'status', stateEnum: 'risk status' },
    metrics: { facet: 'kind', facetEnum: 'metric kind', state: 'status', stateEnum: null },
    features: { facet: 'direction', facetEnum: null, state: 'state', stateEnum: 'feature state' },
    surfaces: { facet: 'type', facetEnum: null, state: 'state', stateEnum: 'surface state' },
  }[which] || { facet: 'kind', facetEnum: null, state: 'status', stateEnum: null };
  const enumHeader = colOf(SPEC.facet);
  const statusHeader = colOf(SPEC.state);
  const allowed = SPEC.facetEnum ? enums[SPEC.facetEnum] : null;
  const statusAllowed = SPEC.stateEnum ? enums[SPEC.stateEnum] : null;
  const facets = [...new Set(reg.rows.map(r => stripMd(cell(r, enumHeader))).filter(Boolean))];
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
  const shownCols = new Set([idHeader, mainCol, enumHeader, statusHeader]);

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
    const heads = [idHeader, mainCol, enumHeader, statusHeader];
    const rows = reg.rows.filter(r => {
      if (S.regFilter !== 'all' && stripMd(cell(r, enumHeader)) !== S.regFilter) return false;
      if (S.regSearch && !Object.values(r).join(' ').toLowerCase().includes(S.regSearch.toLowerCase())) return false;
      return true;
    });
    const span = heads.length + 1;
    return h('div', { class: 'tablewrap' }, h('table', {},
      h('thead', {}, h('tr', {}, heads.map(c => h('th', {}, c)), h('th', {}, t('referencedIn')))),
      h('tbody', {}, rows.flatMap(r => {
        const val = stripMd(cell(r, enumHeader));
        const bad = allowed && val && !allowed.includes(val);
        const rid = stripMd(cell(r, idHeader));
        const open = S.regItem === rid;
        const toggle = () => { S.regItem = open ? null : rid; render(); };
        const main = h('tr', { class: bad ? 'flagged' : '' },
          h('td', { class: 'id' }, h('code', { class: 'rid ' + ridClass(rid) }, rid),
            h('button', { class: 'trailbtn', 'aria-pressed': open, title: t('trailHint'), onclick: toggle },
              open ? '–' : '+')),
          h('td', { class: 'prose', html: inline(r[mainCol] || '') }),
          h('td', {}, h('span', { class: 'tag ' + (bad ? 'err' : '') }, val || '—'),
            bad ? h('div', { class: 'tiny faint' }, allowed.join(' · ')) : null),
          (() => {
            const sval = stripMd(cell(r, statusHeader));
            const sbad = statusAllowed && sval && !statusAllowed.includes(sval.split(/[\s·]/)[0]);
            return h('td', {}, h('span', { class: 'tag ' + (sbad ? 'err' : sval.split(/[\s·]/)[0]) }, sval || '—'),
              sbad ? h('div', { class: 'tiny faint' }, statusAllowed.join(' · ')) : null);
          })(),
          h('td', { class: 'refs' }, (refs[rid] || []).slice(0, 2).map(x =>
            goSection(x.file, x.id, refLabel(x), x.title)),
          (refs[rid] || []).length > 2 ? h('button', { class: 'trailbtn', onclick: toggle },
            `+${(refs[rid] || []).length - 2}`) : null));
        return open ? [main, detail(r, rid, span)] : [main];
      }))));
  }

  return h('div', {}, tabs,
    which === 'surfaces' ? surfaceBoard(m) : null,
    filters, h('div', { id: 'regtable' }, regTable()));
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
        + `${last.observed_n ? ` · n=${last.observed_n}` : ''}`),
      // a reading this old steers nothing — the age rides the KPI so the staleness is read first
      (age => age !== null && age > STALE_READING
        ? h('div', { style: 'margin-top:6px' }, h('span', { class: 'tag aged' }, `${age} ${t('daysOld')}`))
        : null)(daysSince(dateOf(last))));
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
          + ` · ${stripMd(cell(def, 'instrumentation')) || '—'}`)),
      chart || h('div', { class: 'empty' }, '—'),
      groups.length > 1 ? h('div', { class: 'legend' }, groups.map(g =>
        h('span', {}, h('i', { style: `background:${g.color}` }), g.label))) : null);
  }));

  // The definition of every measured node, whole — an accordion, because a definition is a sentence
  // and half a sentence is worse than none.
  const defs = h('div', {}, withReadings.map(id => {
    const def = defOf(id);
    const text = stripMd(cell(def, 'definition'));
    if (!text) return null;
    return acc([h('code', { class: 'tag met' }, id),
      h('span', { class: 'sumtitle' }, stripMd(cell(def, 'name')) || ''),
      h('span', { class: 'summeta' }, h('span', { class: 'tag' }, stripMd(cell(def, 'unit')) || '—'),
        h('span', { class: 'tag' }, stripMd(cell(def, 'kind')) || '—'))],
    [h('div', { class: 'md', html: md(text) }),
      h('div', { class: 'tiny faint mono', style: 'margin-top:8px' },
        stripMd(cell(def, 'instrumentation')) || '—')]);
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
          h('td', { html: inline(stripMd(cell(def, 'definition'))) }),
          h('td', { class: 'mono tiny' }, stripMd(cell(def, 'instrumentation')) || '—'));
      }))) : null);
}

/* ---------------------------------------------------------------- open questions */
function viewOpen() {
  const m = S.model;
  const openGate = m.steps.flatMap(s => s.gate.filter(g => g.tick === 'open' || g.tick === 'unknown')
    .map(g => ({ step: s, g })));
  const hyp = m.registers.hypotheses.rows.filter(r =>
    /open|testing/i.test(stripMd(cell(r, 'status'))));

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
      h('td', { class: 'prose', html: inline(stripMd(cell(r, 'hypothesis'))) }),
      h('td', { class: 'tiny' }, h('span', { class: 'tag' }, stripMd(cell(r, 'type')) || '—')),
      h('td', { class: 'tiny' }, h('span', { class: 'tag ' + stripMd(cell(r, 'status')).split(/[\s·]/)[0] },
        stripMd(cell(r, 'status')) || '—')),
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
  const planes = ['library', 'operations', 'outputs'];
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
      || `${x.name} ${x.kind || ''} ${x.output_kind || ''} ${(x.steps || []).join(',')}`.toLowerCase().includes(q));
    return table([t('colName'), t('colKind'), t('usedBy'), t('origin')],
      rows.map(x => h('tr', {
        class: 'rowlink' + (picked && picked.name === x.name ? ' on' : ''),
        onclick: () => { S.skillPick = x.name; S.skillFile = null; render(); },
      },
        h('td', {}, h('b', {}, x.name),
          (x.homeless || []).length ? h('span', { class: 'tag err', style: 'margin-left:7px' }, 'homeless') : null),
        h('td', {}, (x.kind || x.output_kind) ? h('span', { class: 'tag' }, x.kind || x.output_kind)
          : h('span', { class: 'faint' }, '—')),
        h('td', { class: 'tiny mono' }, (x.steps || []).length ? x.steps.join(', ') : '—'),
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
      [t('writes'), (picked.writes || []).join(' · ')],
      [t('reads'), (picked.reads || []).join(' · ')],
      [t('usedBy'), (picked.steps || []).join(', ')],
      [t('prerequisites'), (picked.prerequisites || []).join(' · ')],
      ['surfaces', (picked.surfaces || []).join(' · ')],
      ['method basis', picked.method_basis],
      ['evidence', picked.evidence_standard],
      ['volume rule', picked.volume_rule && picked.volume_rule !== 'n/a' ? picked.volume_rule : ''],
      ['selection rule', picked.selection_rule && picked.selection_rule !== 'n/a' ? picked.selection_rule : ''],
      ['shows rejects', picked.rejects_shown === 'required' ? 'required' : ''],
      ['opinionated', picked.opinionated || ''],
    ].filter(([, v]) => v).map(([k, v]) => h('div', { class: 'wrow' },
      h('div', { class: 'wk' }, k), h('div', { class: 'wv' }, v)))),
    S.snapshot ? null : h('div', { class: 'row', style: 'margin-top:12px' },
      h('button', { class: 'btn small',
        onclick: () => openSkillFile(picked, 'SKILL.md') }, 'SKILL.md'),
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
  // a finding with no [scope] is about the FRAMEWORK (canon word budget, template wiring), not
  // this product — a PM reading their product's checks must not inherit the vendor's housekeeping
  const own = lint && lint.ok ? lint.findings.filter(f => f.scope) : [];
  const fw = lint && lint.ok ? lint.findings.filter(f => !f.scope) : [];
  const note = f => h('div', { class: 'note ' + f.level },
    h('span', { class: 'who' }, `${f.level} ${f.check}`),
    h('div', {}, f.scope ? h('code', { class: 'tiny' }, f.scope + ' ') : null, f.message));
  const lintBox = !lint ? h('div', { class: 'empty' }, '…')
    : !lint.ok ? h('div', { class: 'note error' }, h('span', { class: 'who' }, 'error'), h('div', {}, lint.error))
      : own.length ? h('div', { class: 'notes' }, own.map(note))
        : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('lintClean')));
  const fwBox = fw.length
    ? h('details', { class: 'small' },
      h('summary', { class: 'small muted' }, `${t('lintFramework')} (${fw.length})`),
      h('div', { class: 'notes', style: 'margin-top:8px' }, fw.map(note)))
    : null;

  return h('div', { class: 'grid cols-2' },
    sec(t('healthTitle'), { right: `${m.health.filter(x => x.level === 'error').length} error · `
      + `${m.health.filter(x => x.level === 'warn').length} warn` },
      m.health.length ? h('div', { class: 'notes' }, groupHealth(m.health).map(healthNote))
        : h('div', { class: 'note ok' }, h('span', { class: 'who' }, 'ok'), h('div', {}, t('healthClean')))),
    h('div', {},
      sec(t('lintTitle'), {}, lintBox, fwBox),
      sec(t('notChecked'), {}, h('p', { class: 'small muted' }, t('notCheckedBody')))));
}

/* The worklog reader — the file a board block drilled into (CONVENTIONS → Step folders & worklogs).
   Same md renderer as any section; a back link returns to the artifact it is projected into. Reached
   only by a link, never a tab, so it is absent from TAB_ORDER. */
function viewWorklog() {
  const m = S.model;
  const key = S.worklog || '';
  const cut = key.indexOf('/');
  const stem = cut < 0 ? key : key.slice(0, cut);
  const tool = cut < 0 ? '' : key.slice(cut + 1);
  const wl = ((m.worklogs || {})[stem] || {})[tool];
  if (!wl) return h('div', { class: 'empty' }, t('worklogMissing'));
  const artFile = stem + '.md';
  const back = h('button', {
    class: 'golink', title: artFile,
    onclick: e => { e.stopPropagation(); S.tab = 'artifacts'; S.artifact = artFile; S.section = null; render(); },
  }, '‹ ' + artFile);
  const aside = h('div', { class: 'wlnav' },
    back,
    h('div', { class: 'row', style: 'margin:12px 0 2px;flex-wrap:wrap' },
      h('code', { class: 'tag' }, 'worklog'),
      confChips(wl.markers.confidence)));
  const doc = h('div', { class: 'panel' }, h('div', {},
    h('div', { class: 'kick' }, `${wl.file} · ${wl.updated || ''}`),
    h('h2', { style: 'font-size:20px;letter-spacing:-.02em' }, wl.title),
    h('hr'),
    h('div', { class: 'md', html: md(wl.body) })));
  return h('div', { class: 'reader' }, aside, doc);
}

/* ---------------------------------------------------------------- guide
 * Chrome, not content: this tab explains the canon — the schemas, the vocabulary, how to ask for
 * work — so the console can be handed to someone who never opened process/. Everything here is a
 * *description*; the canon itself lives in the files the strings point at. Nothing is read from the
 * instance except the live six-step row, which reuses the model already loaded — so the tab renders
 * identically inside an exported snapshot. Diagrams are plain HTML on the house tokens: no image,
 * no web asset, nothing a frozen file could fail to carry. */
const GUIDE_SECS = ['how', 'cycle', 'map', 'legend', 'ask'];

const gNode = (name, sub, cls) => h('div', { class: 'gnode' + (cls ? ' ' + cls : '') },
  h('b', {}, name), sub ? h('span', {}, sub) : null);
const gArrow = label => h('div', { class: 'garrow', 'aria-hidden': 'true' },
  h('span', {}, label), h('i', {}, '→'));

function guideHow() {
  // the write cycle: human → agent → files → console → human. The last node is the first one
  // again (dashed): the loop closes through the human reading, never through the console writing.
  const flow = h('div', { class: 'gflow' },
    gNode(t('g.human'), t('g.humanSub')), gArrow(t('g.asks')),
    gNode(t('g.agent'), t('g.agentSub')), gArrow(t('g.writes')),
    gNode(t('g.files'), t('g.filesSub'), 'gfiles'), gArrow(t('g.reads')),
    gNode(t('g.console'), t('g.consoleSub')), gArrow(t('g.looks')),
    gNode(t('g.human'), t('g.humanSub'), 'ghost'));
  const moves = h('div', { class: 'gmoves' },
    L().g.moves.map((mv, i) => h('div', { class: 'gmove' },
      h('span', { class: 'gnum' }, String(i)),
      h('div', {}, h('b', {}, mv[0]), h('div', { class: 'small muted' }, mv[1])))),
    h('div', { class: 'gmove gloop' }, h('span', { class: 'gnum' }, '0'),
      h('div', { class: 'small muted' }, t('g.nextPass'))));
  return h('div', {},
    sec(t('g.flowTitle'), {}, flow,
      h('div', { class: 'note warn', style: 'margin-top:12px' },
        h('span', { class: 'who' }, 'read-only'), h('div', {}, t('g.noWrite')))),
    sec(t('g.loopTitle'), {},
      h('p', { class: 'small muted', style: 'margin-bottom:12px;max-width:80ch' }, t('g.loopSub')),
      h('div', { class: 'panel' }, moves)),
    sec(t('g.philTitle'), {}, h('div', { class: 'panel' },
      h('ol', { class: 'gphil' }, L().g.phil.map(x => h('li', {}, x))))));
}

function guideCycle() {
  const m = S.model;
  const ring = (label, kid) => h('div', { class: 'gring' },
    h('div', { class: 'grlab' }, label), kid);
  const nest = h('div', { class: 'gnest' },
    ring(t('g.n12'), ring(t('g.n34'), ring(t('g.n5'), ring(t('g.n6'), null)))));
  const live = (m.steps || []).length ? h('div', { class: 'coversteps' }, m.steps.map(s =>
    h('button', {
      class: 'coverstep', title: gateSummary(s),
      onclick: () => { S.tab = 'step'; S.step = s.step; render(); },
    }, dualRing(s, 34), h('span', { class: 'cl' }, `${s.step} · ${shortTitle(s.title || s.name)}`)))) : null;
  return h('div', {},
    sec(t('g.nestTitle'), {},
      h('p', { class: 'small muted', style: 'margin-bottom:12px;max-width:80ch' }, t('g.nestSub')),
      nest,
      h('p', { class: 'small muted', style: 'margin-top:12px;max-width:80ch' }, t('g.feed'))),
    live ? sec(t('g.liveTitle'), {}, h('div', { class: 'panel' }, live)) : null);
}

function guideMap() {
  const homes = h('div', {},
    h('div', { class: 'gflow' },
      gNode(t('g.wl'), t('g.wlSub')), gArrow(t('g.projection')),
      gNode(t('g.art'), t('g.artSub'))),
    h('div', { class: 'gflow', style: 'margin-top:10px' },
      gNode(t('g.regs'), t('g.regsSub'), 'gwide')));
  const rows = L().g.mapRows.map(r => h('tr', {},
    h('td', { class: 'id' }, h('code', {}, r[0])),
    h('td', {}, r[1]),
    h('td', { class: 'act' }, r[2] ? h('button', { class: 'golink',
      onclick: () => { S.tab = r[2]; render(); } }, t('tabs.' + r[2])) : null)));
  return h('div', {},
    sec(t('g.homesTitle'), {}, homes),
    sec(t('g.mapTitle'), {}, table([t('file'), t('g.what'), t('g.where')], rows)));
}

function guideLegend() {
  const row = (chip, text) => h('div', { class: 'glegrow' },
    h('div', { class: 'glchip' }, chip), h('div', { class: 'small' }, text));
  const conf = L().g.legConfRows.map(([k, txt]) => row(h('span', { class: 'conf ' + k }, k), txt));
  const ticks = L().g.legTickRows.map(([k, txt]) => row(tickTag(k), txt));
  const sign = L().g.legSignRows.map(([cls, lab, txt]) => row(h('span', { class: 'tag ' + cls }, lab), txt));
  const ids = L().g.legIdRows.map(([id, txt]) => row(h('code', { class: 'rid ' + ridClass(id) }, id), txt));
  const marks = [
    row(h('span', { class: 'gear' }, t('proposalMark')), t('g.legGear')),
    row(h('span', { class: 'gapmark' }, t('gapDash')), t('g.legGap')),
    row(evStrip({ sourced: 3, validated: 2, assumption: 4, refuted: 1 }, 'inline'), t('g.legStrip')),
    row(dualRing({ gate: [0, 0, 0, 0], gate_counts: { done: 3 }, sections: [] }, 26), t('g.legRing')),
    row(h('span', { class: 'trailbtn' }, '+'), t('g.legTrail')),
  ];
  return h('div', { class: 'glegend' },
    sec(t('g.legConf'), {}, h('div', { class: 'panel' }, conf)),
    sec(t('g.legTicks'), {}, h('div', { class: 'panel' }, ticks)),
    sec(t('g.legSign'), {}, h('div', { class: 'panel' }, sign)),
    sec(t('g.legIds'), {}, h('div', { class: 'panel' }, ids)),
    sec(t('g.legMarks'), {}, h('div', { class: 'panel' }, marks)));
}

function guideAsk() {
  const rows = L().g.askRows.map(r => h('tr', {},
    h('td', { style: 'min-width:170px' }, r[0]),
    h('td', { class: 'prose' }, h('em', { class: 'muted' }, r[1]))));
  return sec(t('g.ask'), {},
    h('p', { class: 'small muted', style: 'margin-bottom:12px;max-width:80ch' }, t('g.askLead')),
    table([t('g.askWhen'), t('g.askSay')], rows),
    h('p', { class: 'small faint', style: 'margin-top:10px;max-width:80ch' }, t('g.askNote')));
}

function viewGuide() {
  const subs = h('div', { class: 'filters' }, GUIDE_SECS.map(k => h('button', {
    'aria-pressed': S.guideSec === k,
    onclick: () => { S.guideSec = k; render(); },
  }, t('g.' + k))));
  const body = { how: guideHow, cycle: guideCycle, map: guideMap, legend: guideLegend, ask: guideAsk };
  return h('div', {}, subs, (body[S.guideSec] || guideHow)());
}

const VIEWS = { overview: viewOverview, step: viewStep, artifacts: viewArtifacts, registers: viewRegisters,
  metrics: viewMetrics, open: viewOpen, sources: viewSources, skills: viewSkills, log: viewLog,
  checks: viewChecks, worklog: viewWorklog, guide: viewGuide };
const TAB_ORDER = ['overview', 'artifacts', 'registers', 'metrics', 'open',
  null, 'sources', 'skills', 'log', 'checks', 'guide'];

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
      + m.registers.metric_tree.rows.length + m.registers.features.rows.length
      + m.registers.surfaces.rows.length,
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
  if (S.tab === 'worklog' && S.worklog) parts.push(S.worklog);
  if (S.tab === 'registers') parts.push(S.reg);
  if (S.tab === 'skills') parts.push(S.skillPlane, S.skillPick || '');
  if (S.tab === 'guide') parts.push(S.guideSec);
  const want = '#' + parts.filter(x => x !== '' && x !== null && x !== undefined).join('/');
  if (location.hash !== want) history.replaceState(null, '', want);
}
function readHash() {
  const p = decodeURIComponent(location.hash.replace(/^#/, '')).split('/');
  if (!p[0] || !VIEWS[p[0]]) return;
  S.tab = p[0];
  if (S.tab === 'step' && p[1]) S.step = +p[1];
  if (S.tab === 'artifacts' && p[1]) { S.artifact = p[1]; S.section = p[2] || null; }
  if (S.tab === 'worklog' && p[1]) S.worklog = p.slice(1).join('/');
  if (S.tab === 'registers' && p[1]) S.reg = p[1];
  if (S.tab === 'skills') { if (p[1]) S.skillPlane = p[1]; if (p[2]) S.skillPick = p[2]; }
  if (S.tab === 'guide' && GUIDE_SECS.includes(p[1])) S.guideSec = p[1];
}

/* In-app history. The page is one hash-routed document, so the browser's own back/forward would leave
   the site; these buttons walk a stack the app keeps itself, so navigation stays inside the console.
   A location is only the "where", not the theme — toggling theme re-renders but adds no history step. */
const LOC_KEYS = ['tab', 'step', 'artifact', 'section', 'worklog', 'reg', 'skillPlane', 'skillPick', 'guideSec'];
const locSnap = () => LOC_KEYS.reduce((o, k) => (o[k] = S[k], o), {});
const locKey = () => JSON.stringify(LOC_KEYS.map(k => S[k]));
function pushHistory() {
  const key = locKey();
  const top = S.hist[S.histIdx];
  if (top && top.key === key) return;          // same place (e.g. a theme re-render) — not a step
  S.hist = S.hist.slice(0, S.histIdx + 1);      // a new move discards any forward tail
  S.hist.push({ key, loc: locSnap() });
  S.histIdx = S.hist.length - 1;
}
function navGo(delta) {
  const i = S.histIdx + delta;
  if (i < 0 || i >= S.hist.length) return;
  S.histIdx = i;
  Object.assign(S, S.hist[i].loc);
  S.navigating = true;                          // restore, don't record
  render();
  S.navigating = false;
  window.scrollTo({ top: 0 });
}
function navBtns() {
  const b = (delta, disabled, key, glyph) => h('button', {
    class: 'navbtn', title: t(key), 'aria-label': t(key), disabled,
    onclick: () => navGo(delta),
  }, glyph);
  return h('div', { class: 'navpair' },
    b(-1, S.histIdx <= 0, 'navBack', '‹'),
    b(1, S.histIdx >= S.hist.length - 1, 'navFwd', '›'));
}

function renderRail() {
  const m = S.model;
  renderKids('#rail', (m.steps || []).map(s => {
    const c = s.gate_counts || {};
    const total = s.gate.length || 1;
    const done = c.done || 0;
    const cc = confCounts(s);
    return h('button', {
      class: (S.tab === 'step' && S.step === s.step ? 'on ' : '') + (m.current_step === s.step ? 'here' : ''),
      onclick: () => { S.tab = 'step'; S.step = s.step; render(); },
      title: `${s.title || s.name} — ${gateSummary(s)} · ${t('confirmed')} ${cc.done}/${cc.total}`,
    },
      h('div', { class: 'rn' }, `${s.step}${m.current_step === s.step ? ' ·' : ''}`),
      h('div', { class: 'rt' }, shortTitle(s.title || s.name)),
      h('div', { class: 'rp' },
        h('i', { style: `width:${(done / total * 100).toFixed(1)}%` }),
        h('i', { class: 'dim', style: `width:${((total - done) / total * 100).toFixed(1)}%` })),
      // the second axis under the first: gate progress (red) above, human sign-offs (navy) below
      cc.total ? h('div', { class: 'rp rp2' },
        h('i', { style: `width:${(cc.done / cc.total * 100).toFixed(1)}%` }),
        h('i', { class: 'dim', style: `width:${((cc.total - cc.done) / cc.total * 100).toFixed(1)}%` })) : null);
  }));
}

function render() {
  const m = S.model;
  if (!m) return;
  if (!S.navigating) pushHistory();
  writeHash();
  document.documentElement.lang = 'en';   // the chrome is English; content keeps its own language inline
  document.getElementById('product').textContent = m.product;
  document.getElementById('subline').textContent = S.snapshot
    ? `${m.name} · ${t('readOnlySnap')}` : `${m.name} · ${m.path}`;

  renderInto('#hnav', navBtns());
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
  const tt = document.getElementById('totop');
  if (tt) { tt.title = t('toTop'); tt.setAttribute('aria-label', t('toTop')); }
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

/* Build the header chrome and the back-to-top button, creating any piece the page skeleton lacks.
   serve.py renders the skeleton once in its own process, so a server started before these pieces
   existed would ship without them; making them here means the chrome is right whether the skeleton is
   current or stale, and the same in the offline export. Idempotent — an up-to-date skeleton is left be. */
function setupChrome() {
  const header = document.querySelector('header.top');
  if (header) {
    const brand = header.querySelector('.brand') || header;
    if (!document.getElementById('hnav')) {
      const hn = document.createElement('div');
      hn.id = 'hnav'; hn.className = 'hnav';
      brand.insertBefore(hn, brand.firstChild);
    }
    const mark = header.querySelector('.mark');
    if (mark) mark.remove();                        // the old top-left wordmark → now the right corner
    if (!document.querySelector('.wordmark')) {
      const wm = document.createElement('div');
      wm.className = 'wordmark'; wm.textContent = 'very-ai-product-loops';
      header.appendChild(wm);
    }
  }
  let tt = document.getElementById('totop');
  if (!tt) {
    tt = document.createElement('button');
    tt.id = 'totop'; tt.className = 'totop'; tt.type = 'button'; tt.textContent = '↑';
    document.body.appendChild(tt);
  }
  tt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  const onScroll = () => tt.classList.toggle('on', window.scrollY > 300);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

async function boot() {
  applyTheme();
  setupChrome();
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
