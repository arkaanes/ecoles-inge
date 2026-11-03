/* Prototype « Écoles d'ingénieurs » : routeur, transitions animées, vraies données (data.json, map.json). */
(function () {
  "use strict";

  /* ---------- outils ---------- */
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function esc(v) { return String(v == null ? "" : v).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function fmt(n) { return n == null ? "—" : Number(n).toLocaleString("fr-FR"); }
  function norm(s) { return String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function plural(n, one, many) { return fmt(n) + " " + (n > 1 ? many : one); }
  function dot(t) { t = String(t || "").trim(); return /[.!?)»]$/.test(t) ? t : t + "."; }
  function lcFirst(t) { return t ? t.charAt(0).toLowerCase() + t.slice(1) : t; }
  var BASE = (document.currentScript && document.currentScript.getAttribute("data-base")) || "";
  var REDUCED = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var SPRING = "cubic-bezier(.16, 1, .3, 1)";
  var IC = {
    back: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
    chev: '<svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>',
    down: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/></svg>',
    map: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2-6-2z"/><path d="M9 4v14M15 6v14"/></svg>',
    grid: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="7" height="7" rx="1.6"/><rect x="13" y="4" width="7" height="7" rx="1.6"/><rect x="4" y="13" width="7" height="7" rx="1.6"/><rect x="13" y="13" width="7" height="7" rx="1.6"/></svg>',
    cal: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>',
    book: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5z"/><path d="M4 19a2 2 0 0 1 2-2h13"/></svg>'
  };

  /* ---------- classe et filière ---------- */
  var FILS = ["MP", "PC", "PSI", "MPI"];
  var CLASSES = { MP: ["MP"], PC: ["PC"], PSI: ["PSI"], MPI: ["MPI"], MPSI: ["MP", "PSI"], MP2I: ["MPI", "MP", "PSI"], PCSI: ["PC", "PSI"] };
  var ST = { classe: "MP", fil: "MP" };
  try {
    var sv = JSON.parse(localStorage.getItem("ecoles-proto") || "null");
    if (sv && CLASSES[sv.classe] && CLASSES[sv.classe].indexOf(sv.fil) !== -1) ST = sv;
    else { var old = localStorage.getItem("ecoles-filiere"); if (CLASSES[old] && CLASSES[old].length === 1) ST = { classe: old, fil: old }; }
  } catch (e) { /* stockage indisponible */ }
  function save() { try { localStorage.setItem("ecoles-proto", JSON.stringify(ST)); } catch (e) { /* rien */ } }
  function firstYear() { return CLASSES[ST.classe].length > 1; }

  /* ---------- familles de concours, regroupées par écrits communs ---------- */
  var FAMS = [
    { id: "x", nom: "X", conc: ["x"], intro: "Le concours de l'École polytechnique. L'ESPCI recrute aussi par ce concours, parmi les candidats admissibles à l'X.",
      PC: "En PC, le concours est commun à l'École polytechnique et à l'ESPCI : mêmes écrits, mais chaque école a ses coefficients et sa liste de classement.",
      PSI: "Le concours de l'École polytechnique. En PSI, l'ESPCI ne recrute pas ; les écrits sont communs avec les ENS.",
      MPI: "Le concours de l'École polytechnique. En MPI, l'ESPCI ne recrute pas ; les écrits sont communs avec les ENS." },
    { id: "ens", nom: "ENS", conc: ["ens"], intro: "Les écoles normales supérieures forment par la recherche. Admis par concours, tu es payé pendant tes études, en échange de 10 ans dans la fonction publique (études comprises)." },
    { id: "mp", nom: "Mines-Ponts", conc: ["ccmp"], intro: "Un concours commun : une seule inscription, une seule liste de classement. Ses écrits servent aussi au concours Mines-Télécom." },
    { id: "mt", nom: "Mines-Télécom", conc: ["cmt"], intro: "Il reprend les écrits de Mines-Ponts, avec une barre d'admissibilité plus basse." },
    { id: "cs", nom: "Centrale-Supélec", conc: ["ccs"], intro: "Des écoles sur les mêmes écrits. Tu paies chaque école que tu coches à l'inscription, et chacune fait son propre classement." },
    { id: "inp", nom: "CCINP", conc: ["ccinp", "ccinp_chi", "insa", "bccinp"], intro: "Le plus grand en nombre d'écoles. Ses écrits servent au concours commun, au Groupe INSA et à une « banque » d'écoles qui font leur propre classement.",
      PC: "Le plus grand en nombre d'écoles. En PC, deux concours sur les mêmes copies, PC-Physique et PC-Chimie, plus le Groupe INSA et une « banque » d'écoles qui font leur propre classement." },
    { id: "poly", nom: "Polytech", conc: ["e3a_poly"], intro: "Le concours Polytech, de la banque e3a-Polytech. MP, PC et PSI y sont classés ensemble.",
      MPI: "Le concours Polytech, de la banque e3a-Polytech. En MPI, une liste à part, sans mélange avec les MP, PC et PSI." },
    { id: "e3a", nom: "e3a", conc: ["e3a_ind", "avenir", "ingeniup"], intro: "Trois concours qui utilisent les écrits e3a-Polytech : les écoles indépendantes, Avenir Prépas et Ingéni'Up." },
    { id: "autres", nom: "Autres concours", conc: ["epita", "cesi", "ut"], intro: "Des concours propres à quelques écoles, et les universités de technologie (UT), qui recrutent sur dossier en dehors du SCEI." }
  ];
  var BLOCS = [
    { id: "xens", nom: "X-ENS", fams: ["x", "ens"], c: "var(--c-xens)" },
    { id: "mines", nom: "Mines", fams: ["mp", "mt"], c: "var(--c-mines)" },
    { id: "cs", nom: "Centrale-Supélec", fams: ["cs"], c: "var(--c-cs)" },
    { id: "inp", nom: "CCINP", fams: ["inp"], c: "var(--c-inp)" },
    { id: "e3a", nom: "e3a-Polytech", fams: ["poly", "e3a"], c: "var(--c-e3a)" },
    { id: "autres", nom: "Hors banques", fams: ["autres"], c: "var(--c-autres)" }
  ];
  var FAM = {}, FAM_OF = {}, BLOC_OF = {};
  FAMS.forEach(function (f) { FAM[f.id] = f; f.conc.forEach(function (c) { FAM_OF[c] = f.id; }); });
  BLOCS.forEach(function (b) { b.fams.forEach(function (f) { BLOC_OF[f] = b; FAM[f].c = b.c; }); });
  var CONC_LINES = { MP: {
    x: "Deux options en MP (informatique ; physique et sciences de l'ingénieur), classées séparément.",
    ens: "Chaque ENS a sa propre liste de classement.",
    ccmp: "Une seule liste de classement pour toutes ses écoles.",
    cmt: "Une liste pour les élèves civils, une autre pour les fonctionnaires.",
    ccs: "Chaque école fait son propre classement, sur les mêmes écrits.",
    ccinp: "Le concours commun : une seule liste de classement.",
    insa: "Sélection sur dossier, écrits CCINP et entretien ; places et classements par domaine.",
    bccinp: "Ces écoles utilisent les écrits du CCINP mais font leur propre classement.",
    e3a_poly: "Une seule liste, commune à MP, PC et PSI.",
    e3a_ind: "Chaque école fait son propre classement.",
    avenir: "Cinq écoles privées, une seule liste.",
    ingeniup: "Écoles privées ; MP, MPI, PC et PSI sont classés ensemble.",
    epita: "Concours commun à l'EPITA, l'IPSA et l'ESME, avec ses propres épreuves.",
    cesi: "Concours propre au CESI : épreuves écrites puis entretien.",
    ut: "Recrutement sur dossier et entretien, en dehors du SCEI." } };
  CONC_LINES.PC = Object.assign({}, CONC_LINES.MP, {
    x: "Concours commun à l'X et à l'ESPCI : chaque école a ses coefficients et sa liste de classement.",
    ens: "Chaque ENS, et chaque option (physique ou chimie), a sa propre liste de classement.",
    ccinp: "Concours PC-Physique : une seule liste de classement, la physique au coefficient 13.",
    ccinp_chi: "Concours PC-Chimie : une seule liste de classement, la chimie au coefficient 13." });
  CONC_LINES.PSI = Object.assign({}, CONC_LINES.MP, {
    x: "Une seule liste de classement pour l'X.",
    ens: "Chaque ENS, et chaque concours (à Paris-Saclay, Physique-PSI et SI-PSI), a sa propre liste de classement." });
  CONC_LINES.MPI = Object.assign({}, CONC_LINES.MP, {
    x: "Une seule liste de classement pour l'X.",
    ens: "Chaque ENS, et chaque option (maths ou info), a sa propre liste de classement.",
    e3a_poly: "Une liste propre à la MPI, séparée des MP, PC et PSI.",
    avenir: "Quatre écoles privées en MPI, une seule liste." });
  var DOM_SHORT = { gen: "Généraliste", info: "Informatique", elec: "Électronique", math: "Maths & data", meca: "Mécanique", energie: "Énergie",
    aero: "Aéro & spatial", btp: "BTP & ville", chimie: "Chimie", physique: "Physique", bio: "Bio & santé", env: "Environnement",
    indus: "Industrie", transport: "Transports", defense: "Défense", rech: "Recherche" };

  /* ---------- données de la filière affichée ---------- */
  var D, MAP, ALL = [], ALLBY = {}, SCH = [], BY = {}, CONC = {}, FIL = "MP", CONC_LINE = {}, MAIN_LIST = {}, SINGLE = {};
  function ownLines(a) { return a.stats.filter(function (v) { return !v.c25 && !v.prev; }); }
  function listKey(v) { return String(v.cl || v.ins || ""); }
  function applyFil(fil) {
    FIL = fil;
    var P = D.parFil[fil];
    D.familles = P.familles; D.fees = P.fees; D.exclus = P.exclus; D.sources = P.sources; D.maj = P.maj;
    CONC = {};
    D.concours.forEach(function (c) { if (c.seul && c.seul !== fil) return; CONC[c.id] = c[fil] ? Object.assign({}, c, c[fil]) : c; });
    SCH = []; BY = {};
    ALL.forEach(function (raw) {
      var acc = raw.acces.filter(function (a) { return a.f === fil; });
      if (!acc.length) return;
      var s = Object.assign({}, raw, { acces: acc });
      if (raw.descF && raw.descF[fil]) s.desc = raw.descF[fil];
      if (raw.domF && raw.domF[fil]) s.dom = raw.domF[fil];
      if (raw.noteF && Object.prototype.hasOwnProperty.call(raw.noteF, fil)) s.note = raw.noteF[fil];
      SCH.push(s); BY[s.id] = s;
    });
    CONC_LINE = CONC_LINES[fil] || CONC_LINES.MP;
    SCH.forEach(function (s) {
      var fams = [];
      s.acces.forEach(function (a) { var f = FAM_OF[a.c]; if (f && fams.indexOf(f) === -1) fams.push(f); });
      s._fams = FAMS.filter(function (f) { return fams.indexOf(f.id) !== -1; }).map(function (f) { return f.id; });
      var parts = [s.nom, s.complet, s.desc].concat(s.alias || []);
      s.campus.forEach(function (c) { parts.push(c.v, c.d, D.regions[c.r]); });
      s._c1 = s.aff ? s.campus.filter(function (c) { return s.aff.y1.indexOf(c.v) !== -1; }) : s.campus;
      s.acces.forEach(function (a) { parts.push(a.lib || "", CONC[a.c] ? CONC[a.c].nom : "", CONC[a.c] ? CONC[a.c].court : ""); a.stats.forEach(function (v) { parts.push(v.lib); }); });
      s.dom.forEach(function (d) { parts.push(DOM_SHORT[d]); parts.push(D.domaines[d]); });
      s._fams.forEach(function (f) { parts.push(FAM[f].nom); });
      s._q = norm(parts.join(" | "));
    });
    MAIN_LIST = {}; SINGLE = {};
    Object.keys(CONC).forEach(function (cid) {
      var lists = {};
      SCH.forEach(function (s) { s.acces.forEach(function (a) {
        if (a.c !== cid) return;
        ownLines(a).forEach(function (v) { if (v.med) { var k = listKey(v); (lists[k] = lists[k] || {})[s.id] = 1; } });
      }); });
      var best = null, bestN = 0;
      Object.keys(lists).forEach(function (k) { var n = Object.keys(lists[k]).length; if (n > bestN) { best = k; bestN = n; } });
      MAIN_LIST[cid] = best; SINGLE[cid] = bestN >= 3;
    });
    document.title = "Écoles d'ingénieurs, " + fil;
  }
  function refLine(s, cid, list) {
    var best = null;
    s.acces.forEach(function (a) {
      if (a.c !== cid) return;
      ownLines(a).forEach(function (v) {
        if (!v.med || (list && listKey(v) !== list)) return;
        if (!best || v.pl > best.pl || (v.pl === best.pl && v.med < best.med)) best = v;
      });
    });
    return best;
  }
  function mainLine(s, cid) { return refLine(s, cid, SINGLE[cid] ? MAIN_LIST[cid] : null) || refLine(s, cid, null); }
  function rankRange(s, cid) {
    var m = [];
    s.acces.forEach(function (a) { if (a.c === cid) ownLines(a).forEach(function (v) { if (v.med) m.push(v.med); }); });
    return m.length ? [Math.min.apply(null, m), Math.max.apply(null, m)] : null;
  }
  function placesIn(s, cids) {
    var p = 0, known = false, scopes = {};
    s.acces.forEach(function (a) { if (cids.indexOf(a.c) === -1) return; scopes[a.scope] = 1; if (a.p26 != null) { p += a.p26; known = true; } });
    return { n: known ? p : null, scopes: Object.keys(scopes) };
  }
  function campusTxt(s) {
    var c = s.campus;
    if (s.aff) return s.aff.y1.join(" ou ") + " en 1re année";
    return c.length > 1 ? c[0].v + ", et " + plural(c.length - 1, "autre campus", "autres campus") : c[0].v;
  }
  function feeText(s) {
    var f = s.frais;
    if (s.bours.cat === "remu") return "Payé pendant les études";
    if (f.min == null && f.ref == null) return "Frais non trouvés";
    if (f.min == null) return "≈ " + fmt(f.ref) + " € par an";
    if (f.max != null && f.max !== f.min) return fmt(f.min) + " à " + fmt(f.max) + " € par an";
    return fmt(f.min) + " € par an";
  }
  function srcLinks(list) { return (list || []).filter(Boolean).map(function (x) { return '<a href="' + esc(x.u) + '" target="_blank" rel="noopener">' + esc(x.t) + "</a>"; }).join(""); }
  function famSchools(f) { return SCH.filter(function (s) { return s._fams.indexOf(f.id) !== -1; }); }
  function famConcs(f) { return f.conc.filter(function (cid) { return CONC[cid] && SCH.some(function (s) { return s.acces.some(function (a) { return a.c === cid; }); }); }); }
  function famPlaces(f, all) {
    var own = 0, shared = 0, unknown = 0;
    all.forEach(function (s) { s.acces.forEach(function (a) {
      if (f.conc.indexOf(a.c) === -1) return;
      if (a.p26 == null) unknown++; else if (a.scope === FIL) own += a.p26; else shared += a.p26;
    }); });
    return { own: own, shared: shared, unknown: unknown };
  }
  function famIntro(f) { return f[FIL] || f.intro; }
  function scopeSentence(a) {
    if (a.p26 == null) return null;
    var n = fmt(a.p26);
    if (a.scope === FIL) return { v: n, s: (a.p26 > 1 ? "places" : "place") + " pour les " + FIL + " en 2026" };
    if (a.scope === "toutes origines") return { v: n, s: "places en 2026, pour tous les profils" };
    if (a.scope === "toutes filières") return { v: n, s: "places en 2026, toutes filières confondues" };
    return { v: n, s: "places en 2026, partagées entre " + a.scope.replace(/\+/g, ", ").replace(/, ([^,]+)$/, " et $1") };
  }
  function line2025(a) {
    var own = ownLines(a), c25 = a.stats.filter(function (v) { return v.c25; }), prev = a.stats.filter(function (v) { return v.prev; });
    if (!a.stats.length) return a.c === "ut" ? "Recrutement sur dossier : pas de rang publié." : "Pas de chiffres " + FIL + " pour 2025 sur cette voie.";
    if (c25.length && !own.length) return "En 2025, l'école recrutait par un autre concours (« " + esc(c25[0].c25) + " ») : ses chiffres ne se comparent pas directement à ceux de 2026.";
    if (prev.length && !own.length) return "Formation nouvelle en 2026. Pour comparaison, voici les chiffres 2025 de l'" + esc(prev[0].prev) + ".";
    if (own.length === 1) {
      var v = own[0], one = "élève de " + FIL + " y est entré", many = "élèves de " + FIL + " y sont entrés";
      if (v.int == null) return "Le SCEI ne publie pas le nombre d'élèves de " + FIL + " entrés par cette voie en 2025." + (v.med ? " Rang médian des admis de la liste commune à plusieurs filières : " + fmt(v.med) + "." : "");
      if (!v.int && v.med) return "En 2025, aucun élève de " + FIL + " n'y est entré. Rang médian des admis de la liste commune à plusieurs filières : " + fmt(v.med) + ".";
      if (!v.int) return "En 2025, aucun élève de " + FIL + " n'y est entré.";
      if (!v.med) return "En 2025, " + plural(v.int, one, many) + " (rang non publié).";
      if (v.inter) return "En 2025, " + plural(v.int, one, many) + ". Rang médian des admis : " + fmt(v.med) + ", sur une liste commune à plusieurs filières.";
      if (v.int === 1) return "En 2025, 1 " + one + ", classé au " + fmt(v.med) + "<sup>e</sup> rang" + (v.cl ? ", sur " + fmt(v.cl) + " candidats de " + FIL + " classés." : (v.ins ? ", sur " + fmt(v.ins) + " inscrits." : "."));
      return "En 2025, " + plural(v.int, one, many) + ". La moitié d'entre eux étaient classés avant le " + fmt(v.med) + "<sup>e</sup> rang" + (v.cl ? ", sur " + fmt(v.cl) + " candidats de " + FIL + " classés." : (v.ins ? ", sur " + fmt(v.ins) + " inscrits." : "."));
    }
    return "Chiffres 2025, voie par voie :";
  }
  function statsTable(stats) {
    var hasMoy = stats.some(function (v) { return v.moy; }), hasCl = stats.some(function (v) { return v.cl; }), hasIns = stats.some(function (v) { return v.ins; });
    var L = { pl: "Places", int: "Intégrés " + FIL, med: "Rang médian", moy: "Rang moyen", cl: "Classés", ins: "Inscrits" };
    var td = function (k, v) { return '<td data-l="' + L[k] + '">' + fmt(v) + "</td>"; };
    var h = '<table class="stats"><thead><tr><th>Voie (2025)</th><th>' + L.pl + "</th><th>" + L.int + "</th><th>" + L.med + "</th>" + (hasMoy ? "<th>" + L.moy + "</th>" : "") + (hasCl ? "<th>" + L.cl + "</th>" : "") + (hasIns ? "<th>" + L.ins + "</th>" : "") + "</tr></thead><tbody>";
    stats.forEach(function (v) {
      var fl = "";
      if (v.inter) fl += '<span class="flag">liste commune à plusieurs filières' + (v.iint != null ? ", " + v.iint + " intégrés toutes filières" : "") + "</span>";
      if (v.c25) fl += '<span class="flag">classement 2025 « ' + esc(v.c25) + " »</span>";
      h += "<tr><td>" + esc(v.lib) + fl + "</td>" + td("pl", v.pl) + td("int", v.int) + td("med", v.med) + (hasMoy ? td("moy", v.moy) : "") + (hasCl ? td("cl", v.cl) : "") + (hasIns ? td("ins", v.ins) : "") + "</tr>";
    });
    return h + "</tbody></table>";
  }
  function niveauTxt(f) {
    var cid = famConcs(f)[0], lines = [];
    if (!cid) return "";
    SCH.forEach(function (s) {
      if (!s.acces.some(function (a) { return a.c === cid; })) return;
      if (SINGLE[cid]) { var v = refLine(s, cid, MAIN_LIST[cid]); if (v) lines.push({ s: s, v: v }); }
      else s.acces.forEach(function (a) { if (a.c === cid) ownLines(a).forEach(function (w) { if (w.med && w.int) lines.push({ s: s, v: w }); }); });
    });
    if (lines.length < 2) return "";
    lines.sort(function (a, b) { return a.v.med - b.v.med; });
    var lo = lines[0], hi = lines[lines.length - 1];
    if (lo.s.id === hi.s.id) return "";
    if (SINGLE[cid]) return "En 2025, la moitié des élèves de " + FIL + " admis à " + lo.s.nom + " étaient classés avant le " + fmt(lo.v.med) + "e rang ; à " + hi.s.nom + ", avant le " + fmt(hi.v.med) + "e" + (lo.v.inter ? ", sur une liste commune à plusieurs filières." : (lo.v.cl ? ", sur " + fmt(lo.v.cl) + " candidats de " + FIL + " classés." : "."));
    return "Chaque école a sa propre liste : les rangs ne se comparent pas d'une école à l'autre.";
  }

  /* ---------- noms partagés entre pages (morphing des titres) ---------- */
  var usedNames = {};
  function vtn(name, extra) {
    var css = extra || "";
    if (!REDUCED && !usedNames[name]) { usedNames[name] = 1; css = "view-transition-name:" + name + ";" + css; }
    return css ? ' style="' + css + '"' : "";
  }
  function vtSafe(id) { return String(id).replace(/[^a-zA-Z0-9_-]/g, "_"); }

  /* ---------- accueil ---------- */
  function classeHTML(inSheet) {
    var h = '<div class="classe">' + (inSheet ? "" : '<span class="classe-h">Ta classe</span>');
    var btn = function (c) { return '<button class="seg" type="button" data-classe="' + c + '" aria-pressed="' + (ST.classe === c) + '">' + c + "</button>"; };
    h += '<div class="classe-row" role="group" aria-label="2e année"><span>2e année</span>' + ["MP", "PC", "PSI", "MPI"].map(btn).join("") + "</div>";
    h += '<div class="classe-row" role="group" aria-label="1re année"><span>1re année</span>' + ["MPSI", "MP2I", "PCSI"].map(btn).join("") + "</div>";
    if (firstYear()) {
      h += '<div class="vue" role="group" aria-label="Filière affichée"><span>Vue en</span>' + CLASSES[ST.classe].map(function (f) {
        return '<button class="seg" type="button" data-fil="' + f + '" aria-pressed="' + (ST.fil === f) + '">' + f + "</button>";
      }).join("") + "</div>";
    }
    return h + "</div>";
  }
  function ecritsDate(fid) {
    var FD = D.familles[fid] || {}, b = (FD.blocs || [])[0];
    var q = b && b.ecrits && b.ecrits.quand;
    return q && /\d/.test(q) ? "Écrits : " + q.replace(/ 20\d\d$/, "") : "";
  }
  function stationHTML(f) {
    var all = famSchools(f);
    if (!all.length) return "";
    var P = famPlaces(f, all), pl = "";
    if (P.own) pl = plural(P.own, "place", "places") + (P.shared ? " + " + fmt(P.shared) + " partagées" : "");
    else if (P.shared) pl = fmt(P.shared) + " places partagées";
    return '<a class="stn" href="#/c/' + f.id + '" data-link style="--fc:var(--f-' + f.id + ')"><span class="dot"></span><span><span class="nm"' + vtn("t-" + f.id) + ">" + esc(f.nom) + '</span><span class="fg"><span>' + plural(all.length, "école", "écoles") + "</span>" + (pl ? "<span>" + pl + "</span>" : "") + "</span></span>" + IC.chev + "</a>";
  }
  function viewHome() {
    var h = '<div class="home"><div class="home-main" style="display:flex;flex-direction:column;gap:22px">';
    var nx = nextStep();
    if (nx) {
      var nn = dayDiff(today(), iso(nx.a));
      h += '<a class="next" href="' + (nx.k === "insc" || nx.k === "pay" ? "#/inscription" : "#/calendrier") + '" data-link style="--fc:' + (nx.fam ? "var(--f-" + nx.fam + ")" : "var(--ink)") + '"><span class="next-k">' + (nn > 0 ? esc(relFr(nn).replace(/^d/, "D")) : "En ce moment") + '</span><b>' + esc(nx.t) + "</b><span>" + esc(rangeFr(nx.a, nx.b)) + "</span>" + IC.chev + "</a>";
    }
    h += classeHTML(false);
    if (firstYear()) h += '<a class="qk wide" href="#/filiere" data-link>' + IC.grid + "Comparer mes filières de 2e année</a>";
    h += '<a class="searchbox" href="#/explorer" data-link>' + IC.search + "Une école, une ville, un domaine</a>";
    h += '<div><div class="net-h"><h1 class="h1" style="margin-top:6px">Les concours</h1><a class="btnlink" href="#/cote" data-link>Tous côte à côte</a></div><div class="net">';
    BLOCS.forEach(function (b, i) {
      var st = b.fams.map(function (fid) { return stationHTML(FAM[fid]); }).filter(Boolean);
      if (!st.length) return;
      if (b.id === "e3a") h += '<div class="joint"><span>écrits en partie communs</span></div>';
      var date = ecritsDate(b.fams[0]);
      h += '<section class="bloc" style="--c:' + b.c + '" aria-label="' + esc(b.nom) + '"><div class="bloc-h"><span class="tag">' + esc(b.nom) + "</span>" + (st.length > 1 ? '<span class="bloc-note">mêmes écrits</span>' : "") + (date ? '<span class="date">' + esc(date) + "</span>" : "") + "</div>";
      h += '<div class="line">' + (st.length > 1 ? '<span class="rail" aria-hidden="true"></span>' : "") + st.join("") + "</div></section>";
    });
    h += "</div></div></div>";
    h += '<aside class="home-side"><div class="quick">';
    h += '<a class="qk" href="#/carte" data-link>' + IC.map + "La carte des écoles</a>";
    h += '<a class="qk" href="#/calendrier" data-link>' + IC.cal + "Le calendrier 2027</a>";
    h += '<a class="qk" href="#/inscription" data-link>' + IC.book + "Préparer mon inscription</a>";
    h += '<a class="qk" href="#/explorer" data-link>' + IC.grid + "Explorer par domaine</a>";
    h += '<a class="qk wide" href="#/comprendre" data-link>' + IC.book + "Comprendre les concours</a>";
    h += '</div><p class="foot">Places : notices des concours 2026. Rangs : statistiques SCEI 2025. <a href="#/comprendre" data-link>Sources et méthode</a></p></aside></div>';
    return h;
  }

  /* ---------- page d'un concours ---------- */
  var TABS = [["ecoles", "Écoles"], ["epreuves", "Épreuves"], ["style", "Le style"], ["inscription", "Inscription"]];
  var ui = { filt: {} };
  function famTabs(f) {
    var FD = D.familles[f.id] || {};
    return TABS.filter(function (t) {
      if (t[0] === "epreuves") return FD.blocs && FD.blocs.length;
      if (t[0] === "style") return FD.style && FD.style.sujets;
      return true;
    });
  }
  function viewConcours(fid, tab) {
    var f = FAM[fid]; if (!f || !famSchools(f).length) return null;
    var b = BLOC_OF[fid], FD = D.familles[fid] || {}, all = famSchools(f), P = famPlaces(f, all);
    var tabs = famTabs(f);
    if (!tabs.some(function (t) { return t[0] === tab; })) tab = "ecoles";
    var h = '<a class="back" href="#/" data-link data-back>' + IC.back + "Les concours</a>";
    var fc = ";--fc:var(--f-" + fid + ")";
    h += '<div class="c-head" style="--c:' + b.c + fc + '"><span class="c-rail" aria-hidden="true"></span><div class="c-id">';
    h += '<div class="c-tag"><span class="tag" style="--c:' + b.c + fc + '">' + esc(b.nom) + "</span>" + (FD.ecritsCourt ? "<span>Écrits : " + esc(lcFirst(FD.ecritsCourt)) + "</span>" : "") + "</div>";
    h += '<h1 class="h1"' + vtn("t-" + fid, "width:max-content;max-width:100%") + ">" + esc(f.nom) + "</h1>";
    h += '<p class="lede">' + esc(famIntro(f)) + "</p></div></div>";
    var f1v, f1s;
    if (P.own) { f1v = fmt(P.own); f1s = "places en " + FIL + (P.shared ? ", + " + fmt(P.shared) + " partagées" : ""); }
    else if (P.shared) { f1v = fmt(P.shared); f1s = "places partagées entre filières"; }
    else { f1v = "—"; f1s = "places non publiées"; }
    var third = FD.poids != null ? [FD.poids + " %", "de la note finale à l'oral"] : [FD.inscCourt || "—", "d'inscription"];
    h += '<div class="facts"><div class="fact"><b class="num">' + f1v + "</b><span>" + esc(f1s) + '</span></div><div class="fact"><b class="num">' + all.length + "</b><span>" + (all.length > 1 ? "écoles" : "école") + '</span></div><div class="fact"><b class="num">' + esc(third[0]) + "</b><span>" + esc(third[1]) + "</span></div></div>";
    h += '<div class="tabs" style="--c:' + b.c + fc + '"><div class="tabs-in" role="tablist" aria-label="' + esc(f.nom) + '">';
    tabs.forEach(function (t) { h += '<button class="tab" type="button" role="tab" id="tab-' + t[0] + '" aria-controls="panel" aria-selected="' + (t[0] === tab) + '" data-tab="' + t[0] + '">' + t[1] + "</button>"; });
    h += '<span class="ind" aria-hidden="true"></span></div></div>';
    h += '<div class="panels" data-fam="' + fid + '" data-cur="' + tab + '" style="--c:' + b.c + fc + '"><div class="panel" id="panel" role="tabpanel" aria-labelledby="tab-' + tab + '">' + panelHTML(fid, tab) + "</div></div>";
    return h;
  }
  function panelHTML(fid, tab) {
    if (tab === "epreuves") return epreuvesHTML(fid);
    if (tab === "style") return styleHTML(fid);
    if (tab === "inscription") return inscriptionHTML(fid);
    return ecolesHTML(fid);
  }
  function ecolesHTML(fid) {
    var f = FAM[fid], all = famSchools(f), st = ui.filt[fid] || (ui.filt[fid] = { reg: "all", dom: "all" });
    var regOk = function (s) { return st.reg === "all" || s._c1.some(function (c) { return c.r === st.reg; }); };
    var domOk = function (s) { return st.dom === "all" || s.dom.indexOf(st.dom) !== -1; };
    var list = all.filter(function (s) { return regOk(s) && domOk(s); });
    var h = "";
    if (all.length > 6) {
      var rc = {}, dc = {};
      all.filter(domOk).forEach(function (s) { var seen = {}; s._c1.forEach(function (c) { if (!seen[c.r]) { seen[c.r] = 1; rc[c.r] = (rc[c.r] || 0) + 1; } }); });
      all.filter(regOk).forEach(function (s) { s.dom.forEach(function (d) { dc[d] = (dc[d] || 0) + 1; }); });
      h += '<div class="filters"><label><span class="sr" hidden>Région</span><select class="sel" data-freg="' + fid + '" aria-label="Région"><option value="all">Toutes les régions</option>' +
        Object.keys(D.regions).filter(function (r) { return rc[r] || st.reg === r; }).sort(function (a, b) { return (rc[b] || 0) - (rc[a] || 0); }).map(function (r) { return '<option value="' + r + '"' + (st.reg === r ? " selected" : "") + ">" + esc(D.regions[r]) + " (" + (rc[r] || 0) + ")</option>"; }).join("") + "</select></label>";
      h += '<label><select class="sel" data-fdom="' + fid + '" aria-label="Domaine"><option value="all">Tous les domaines</option>' +
        Object.keys(DOM_SHORT).filter(function (d) { return dc[d] || st.dom === d; }).sort(function (a, b) { return (dc[b] || 0) - (dc[a] || 0); }).map(function (d) { return '<option value="' + d + '"' + (st.dom === d ? " selected" : "") + ">" + esc(DOM_SHORT[d]) + " (" + (dc[d] || 0) + ")</option>"; }).join("") + "</select></label></div>";
    }
    if (!list.length) return h + '<p class="empty">Aucune école avec ces filtres.</p>';
    var fcs = famConcs(f);
    fcs.forEach(function (cid) {
      var rows = list.filter(function (s) { return s.acces.some(function (a) { return a.c === cid; }); });
      if (!rows.length) return;
      rows.sort(function (a, b) {
        if (SINGLE[cid]) {
          var x = refLine(a, cid, MAIN_LIST[cid]), y = refLine(b, cid, MAIN_LIST[cid]);
          var xa = x ? x.med : Infinity, yb = y ? y.med : Infinity;
          if (xa !== yb) return xa < yb ? -1 : 1;
        }
        return a.nom.localeCompare(b.nom, "fr");
      });
      h += '<section class="cid">';
      h += '<div class="cid-h">' + (fcs.length > 1 ? "<b>" + esc(CONC[cid].nom) + "</b>" : "") + "<span>" + esc(CONC_LINE[cid] || "") + "</span></div>";
      h += '<div class="cols-h" aria-hidden="true"><span style="text-align:left">École</span><span>Places 2026</span><span>Rang médian 2025</span><span></span></div>';
      rows.forEach(function (s) { h += srowHTML(s, cid); });
      h += "</section>";
    });
    return h;
  }
  function srowHTML(s, cid) {
    var pl = placesIn(s, [cid]), h = '<a class="srow" href="#/e/' + esc(s.id) + '" data-link style="--fc:var(--f-' + FAM_OF[cid] + ')">';
    h += '<span><span class="nm"' + vtn("s-" + vtSafe(s.id)) + ">" + esc(s.nom) + '</span><span class="sub">' + esc(campusTxt(s)) + "</span></span>";
    var sc = pl.scopes.length === 1 && pl.scopes[0] !== FIL ? pl.scopes[0].replace(/\+/g, "-") : "";
    h += '<span class="pl num">' + (pl.n != null ? fmt(pl.n) + (sc ? "<small>" + esc(sc) + "</small>" : "") : "—") + "</span>";
    if (cid === "insa") {
      var rr = rankRange(s, cid);
      h += rr ? '<span class="md num">' + fmt(rr[0]) + (rr[1] !== rr[0] ? "<small>à " + fmt(rr[1]) + "</small>" : "") + "</span>" : '<span class="info">Pas de rang</span>';
    } else {
      var v = mainLine(s, cid);
      if (v) h += '<span class="md num">' + fmt(v.med) + (!SINGLE[cid] && v.cl && !v.inter ? "<small>sur " + fmt(v.cl) + "</small>" : "") + "</span>";
      else h += '<span class="info">' + (CONC[cid].g === "hors" ? "Sur dossier" : "Pas de rang") + "</span>";
    }
    return h + IC.chev + "</a>";
  }
  function epRows(l) {
    return l.map(function (e) { return '<div class="eprow"><span>' + esc(e[0]) + (e[3] ? "<small>" + esc(e[3]) + "</small>" : "") + '</span><span class="d">' + esc(e[1] || "") + '</span><span class="c">' + (e[2] ? "× " + esc(e[2]) : "") + "</span></div>"; }).join("");
  }
  function epreuvesHTML(fid) {
    var FD = D.familles[fid] || {}, h = '<div class="ep">';
    (FD.blocs || []).forEach(function (b) {
      var n = 0, step = function (t) { n++; return '<div class="step-h"><i>' + n + "</i>" + t + "</div>"; };
      if (b.titre) h += '<h2 class="ep-t">' + esc(b.titre) + "</h2>";
      if (b.txt) h += '<p style="margin:0;color:var(--ink-2)">' + esc(b.txt) + "</p>";
      var L = "", R = "";
      if (b.ecrits) L += '<div class="step">' + step("Écrits" + (b.ecrits.quand ? ", " + esc(b.ecrits.quand) : "")) + "<div>" + epRows(b.ecrits.l) + "</div>" + (b.ecrits.note ? "<p>" + esc(b.ecrits.note) + "</p>" : "") + "</div>";
      if (b.adm) R += '<div class="step">' + step("Admissibilité") + "<p>Résultats " + esc(b.adm.quand) + "." + (b.adm.txt ? " " + esc(b.adm.txt) : "") + "</p></div>";
      if (b.oraux) R += '<div class="step">' + step("Oraux" + (b.oraux.quand ? ", " + esc(b.oraux.quand) : "")) + (b.oraux.l.length ? "<div>" + epRows(b.oraux.l) + "</div>" : "") + (b.oraux.note ? "<p>" + esc(b.oraux.note) + "</p>" : "") + "</div>";
      if (L || R) h += '<div class="ep-grid"><div class="step-col" style="display:flex;flex-direction:column;gap:20px">' + L + '</div><div class="step-col" style="display:flex;flex-direction:column;gap:20px">' + R + "</div></div>";
      if (b.classement) h += '<div class="step">' + step("Classement final") + "<p>" + esc(b.classement) + "</p></div>";
      if (b.notice) h += '<a class="btnlink" href="' + esc(b.notice.u) + '" target="_blank" rel="noopener">' + esc(b.notice.t) + "</a>";
      if (b.src && b.src.length) h += '<div class="srcs">' + srcLinks(b.src) + "</div>";
    });
    return h + "</div>";
  }
  function styleHTML(fid) {
    var st = (D.familles[fid] || {}).style || {}, niv = niveauTxt(FAM[fid]);
    var h = '<div class="style-g">';
    h += "<div><h3>Les sujets</h3><p>" + esc(st.sujets) + '</p><div class="srcs">' + srcLinks(st.sujetsSrc) + "</div></div>";
    if (st.oraux) h += "<div><h3>Les oraux</h3><p>" + esc(st.oraux) + '</p><div class="srcs">' + srcLinks(st.orauxSrc) + "</div></div>";
    if (niv) h += "<div><h3>Le niveau des admis</h3><p>" + esc(niv) + "</p></div>";
    if (st.pourqui) h += "<div><h3>Pour qui</h3><p>" + esc(st.pourqui) + '</p><p class="small mut" style="margin:0">Un avis, tiré des rapports du jury et du poids des épreuves.</p></div>';
    return h + "</div>";
  }
  function inscriptionHTML(fid) {
    var cs = famConcs(FAM[fid]), h = '<div class="ins">';
    cs.forEach(function (cid) {
      var c = CONC[cid];
      if (cs.length > 1) h += "<h3>" + esc(c.nom) + "</h3>";
      h += "<p><b>Inscription :</b> " + esc(c.frais) + "</p>";
      if (c.savoir && c.savoir.length) h += "<ul>" + c.savoir.map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + "</ul>";
      h += '<div class="srcs">' + srcLinks(c.src) + "</div>";
    });
    return h + "</div>";
  }

  /* ---------- fiche école ---------- */
  function byFilHTML(raw, cid) {
    var rows = [];
    FILS.forEach(function (F) {
      var acc = raw.acces.filter(function (a) { return a.f === F && a.c === cid; });
      if (!acc.length) return;
      var p = 0, known = false, shared = false, best = null;
      acc.forEach(function (a) {
        if (a.p26 != null) { p += a.p26; known = true; if (a.scope !== F) shared = true; }
        ownLines(a).forEach(function (v) { if (v.med && (!best || v.pl > best.pl)) best = v; });
      });
      rows.push({ F: F, p: known ? p : null, shared: shared, v: best });
    });
    if (rows.length < 2) return "";
    var mine = CLASSES[ST.classe];
    var h = '<table class="byfil"><thead><tr><th>Filière</th><th>Places 2026</th><th>Rang médian 2025</th><th>Classés</th></tr></thead><tbody>';
    rows.forEach(function (r) {
      var on = firstYear() ? mine.indexOf(r.F) !== -1 : r.F === FIL;
      h += '<tr class="' + (on ? "on" : "") + '"><td>' + r.F + "</td><td>" + (r.p != null ? fmt(r.p) + (r.shared ? "*" : "") : "—") + '</td><td class="md">' + (r.v ? fmt(r.v.med) : "—") + "</td><td>" + (r.v && r.v.cl ? fmt(r.v.cl) : "—") + "</td></tr>";
    });
    h += "</tbody></table>";
    if (rows.some(function (r) { return r.shared; })) h += '<p class="small mut" style="margin:4px 0 0">* places partagées entre plusieurs filières</p>';
    return h;
  }
  function viewEcole(id) {
    var s = BY[id], raw = ALLBY[id];
    if (!raw) return null;
    var prev = (history.state || {}).prev, pr = prev ? parse(prev) : null;
    var backTo = lastConcours && s && s._fams.indexOf(lastConcours) !== -1 ? lastConcours : (s ? s._fams[0] : null);
    var backHref = pr && pr.v !== "e" ? prev : (backTo ? "#/c/" + backTo : "#/");
    var h = '<a class="back" href="' + esc(backHref) + '" data-link data-back>' + IC.back + esc(labelOf(parse(backHref))) + "</a>";
    if (!s) {
      var others = FILS.filter(function (F) { return F !== FIL && raw.acces.some(function (a) { return a.f === F; }); });
      return h + '<div class="e-head"><h1 class="h1"' + vtn("s-" + vtSafe(id)) + ">" + esc(raw.nom) + '</h1><p class="lede">Pas de voie en ' + FIL + " en 2026." + (others.length ? " Elle recrute en " + others.join(", ").replace(/, ([^,]*)$/, " et $1") + "." : "") + "</p></div>";
    }
    h += '<div class="e-head">';
    h += '<h1 class="h1"' + vtn("s-" + vtSafe(id)) + ">" + esc(s.nom) + "</h1>";
    h += '<p class="lede" style="color:var(--mut)">' + esc(s.campus.map(function (c) { return c.v + " (" + c.d + ")"; }).join(", ")) + ". " + esc(s.statut) + ".</p>";
    h += '<div class="chips">' + s.dom.map(function (d) { return '<span class="chip">' + esc(DOM_SHORT[d]) + "</span>"; }).join("") + "</div></div>";
    h += '<div class="e-grid"><div class="e-main" style="display:flex;flex-direction:column;gap:28px">';
    h += '<section style="display:flex;flex-direction:column;gap:8px"><p class="lede">' + esc(dot(s.desc)) + '</p><p class="small mut" style="margin:0">' + esc(s.complet) + (s.alias && s.alias.length ? ". Aussi appelée " + esc(s.alias.join(", ")) + "." : ".") + "</p>" + (s.note ? '<p class="note">' + esc(s.note) + "</p>" : "") + "</section>";
    h += '<section><h2 class="h2" style="margin-bottom:14px">Pour y entrer</h2>';
    s.acces.forEach(function (a) {
      var fid = FAM_OF[a.c], b = BLOC_OF[fid], sc = scopeSentence(a);
      h += '<div class="voie" style="--c:' + b.c + ';--fc:var(--f-' + fid + ')"><span class="c-rail" aria-hidden="true"></span><div class="voie-c">';
      h += '<a class="c-tag" href="#/c/' + fid + '" data-link style="text-decoration:none"><span class="tag" style="--c:' + b.c + ';--fc:var(--f-' + fid + ')">' + esc(FAM[fid].nom) + "</span><span>" + esc(CONC[a.c].nom) + "</span></a>";
      if (a.lib) h += '<b style="margin-top:-2px">' + esc(a.lib) + "</b>";
      if (sc) h += '<div class="big"><b class="num">' + sc.v + "</b><span>" + esc(sc.s) + "</span></div>";
      else h += "<p><b>Places 2026 :</b> non trouvées" + (a.txt ? ". " + esc(a.txt) : "") + "</p>";
      if (sc && a.txt) h += '<p class="small">' + esc(a.txt) + "</p>";
      h += "<p>" + line2025(a) + "</p>";
      var multi = ownLines(a).length > 1 || (a.stats.length && !ownLines(a).length);
      if (a.stats.length) h += multi ? statsTable(a.stats) : '<details class="det"><summary>Détail des chiffres 2025' + IC.down + "</summary>" + statsTable(a.stats) + "</details>";
      var bf = byFilHTML(raw, a.c);
      if (bf) h += '<div style="margin-top:6px"><h3 style="margin:0 0 4px;font-size:16px;font-weight:800">Selon la filière</h3>' + bf + "</div>";
      if (a.note) h += '<p class="note">' + esc(a.note) + "</p>";
      if (a.src) h += '<div class="srcs">' + srcLinks([a.src]) + "</div>";
      h += "</div></div>";
    });
    h += "</section></div>";
    h += '<aside class="e-side"><section class="cost"><h2 class="h2" style="margin-bottom:10px">Ce que ça coûte</h2>';
    var fz = s.frais;
    if (s.bours.cat === "remu" || (fz.min == null && fz.ref == null)) h += '<div class="big" style="padding-bottom:12px"><b style="font-size:24px">' + esc(feeText(s)) + "</b></div>";
    else h += '<div class="big" style="padding-bottom:12px"><b class="num" style="font-size:32px">' + esc(feeText(s).replace(" par an", "")) + "</b><span>par an" + (fz.an && fz.an !== "?" ? ", " + esc(fz.an) : "") + "</span></div>";
    var bo = { remu: "payé", exo: "0 €", part: "réduction" }[s.bours.cat] || "non précisé";
    h += '<div class="kv"><span>Si tu es boursier</span><b>' + bo + "</b></div>";
    var keys = [];
    s.acces.forEach(function (a) { a.fee.forEach(function (k) { if (keys.indexOf(k) === -1) keys.push(k); }); });
    keys.forEach(function (k) {
      var fe = D.fees[k]; if (!fe) return;
      h += '<div class="kv"><span>Inscription ' + esc(fe[0]) + "</span><b>" + (fe[1] == null ? "?" : fmt(fe[1]) + " €" + (fe[2] != null && fe[2] !== fe[1] ? ", " + (fe[2] === 0 ? "0 €" : fmt(fe[2]) + " €") + " boursier" : "")) + "</b></div>";
    });
    if (s.bours.cat !== "remu") h += '<div class="kv"><span>CVEC</span><b>105 €, 0 € boursier</b></div>';
    h += '<p class="small mut" style="margin:10px 0 8px">' + esc(dot(fz.txt)) + " " + esc(dot(s.bours.txt)) + "</p>";
    if (fz.src && fz.src.length) h += '<div class="srcs">' + srcLinks(fz.src) + "</div>";
    h += "</section></aside></div>";
    return h;
  }

  /* ---------- carte ---------- */
  function regionCounts() {
    var n = {};
    SCH.forEach(function (s) { var seen = {}; s._c1.forEach(function (c) { if (!seen[c.r]) { seen[c.r] = 1; n[c.r] = (n[c.r] || 0) + 1; } }); });
    return n;
  }
  function level(n) { return n >= 26 ? 5 : n >= 18 ? 4 : n >= 10 ? 3 : n >= 5 ? 2 : 1; }
  function rowHTML(s) {
    return '<a class="row" href="#/e/' + esc(s.id) + '" data-link><span><span class="nm"' + vtn("s-" + vtSafe(s.id)) + ">" + esc(s.nom) + '</span><span class="sub"><span>' + esc(campusTxt(s)) + "</span>" +
      s._fams.map(function (f) { return '<span class="sw" style="--c:' + FAM[f].c + ';--fc:var(--f-' + f + ')"><i></i>' + esc(FAM[f].nom) + "</span>"; }).join("") + "</span></span>" + IC.chev + "</a>";
  }
  function viewCarte(reg) {
    if (reg && !D.regions[reg]) reg = null;
    var n = regionCounts();
    var h = '<div class="carte"><div class="carte-map"><h1 class="h1" style="margin-bottom:14px">' + (reg ? esc(D.regions[reg]) : "La carte") + "</h1>";
    h += '<svg class="map" viewBox="' + MAP.vb.join(" ") + '" role="img" aria-label="Carte des régions, avec le nombre d\'écoles dans chacune">';
    Object.keys(MAP.regions).forEach(function (k) {
      h += '<path class="rg' + (reg === k ? " sel" : "") + '" data-region="' + k + '" d="' + MAP.regions[k].d + '" fill="var(--m' + level(n[k] || 0) + ')"><title>' + esc(MAP.regions[k].nom) + " : " + plural(n[k] || 0, "école", "écoles") + "</title></path>";
    });
    var bx = MAP.reuBox;
    h += '<rect class="inset" x="' + bx[0] + '" y="' + bx[1] + '" width="' + bx[2] + '" height="' + bx[3] + '" rx="8"></rect>';
    Object.keys(MAP.labels).forEach(function (k) {
      var p = MAP.labels[k], c = n[k] || 0, r = c >= 10 ? 24 : 20;
      if (k === "reu") p = [bx[0] + bx[2] - 6, bx[1] + 6];
      h += '<g class="badge" aria-hidden="true"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + r + '"></circle><text x="' + p[0] + '" y="' + p[1] + '">' + c + "</text></g>";
    });
    h += "</svg></div><div>";
    h += '<div class="regs">' + Object.keys(D.regions).sort(function (a, b) { return (n[b] || 0) - (n[a] || 0); }).map(function (r) {
      return '<a class="rchip" href="#/carte' + (reg === r ? "" : "/" + r) + '" data-link data-replace aria-current="' + (reg === r) + '">' + esc(D.regions[r]) + "<span>" + (n[r] || 0) + "</span></a>";
    }).join("") + "</div>";
    if (reg) {
      var list = SCH.filter(function (s) { return s._c1.some(function (c) { return c.r === reg; }); }).sort(function (a, b) { return a.nom.localeCompare(b.nom, "fr"); });
      h += '<div id="reglist" style="margin-top:18px"><p class="small mut" style="margin:0 0 4px">' + plural(list.length, "école", "écoles") + " en 1re année</p>" + '<div class="rows">' + list.map(rowHTML).join("") + "</div></div>";
    }
    return h + "</div></div>";
  }

  /* ---------- domaines ---------- */
  function viewDomaines(dom) {
    if (dom && !D.domaines[dom]) dom = null;
    if (dom) {
      var list = SCH.filter(function (s) { return s.dom.indexOf(dom) !== -1; }).sort(function (a, b) { return a.nom.localeCompare(b.nom, "fr"); });
      return '<a class="back" href="#/domaines" data-link data-back>' + IC.back + 'Les domaines</a><h1 class="h1"' + vtn("d-" + dom, "width:max-content;max-width:100%") + ">" + esc(D.domaines[dom]) + '</h1><p class="lede" style="margin:8px 0 10px">' + plural(list.length, "école", "écoles") + " en " + FIL + ".</p><div class=\"rows\">" + list.map(rowHTML).join("") + "</div>";
    }
    var n = {};
    SCH.forEach(function (s) { s.dom.forEach(function (d) { n[d] = (n[d] || 0) + 1; }); });
    var h = '<h1 class="h1" style="margin-bottom:18px">Les domaines</h1><div class="doms">';
    Object.keys(DOM_SHORT).filter(function (d) { return n[d]; }).sort(function (a, b) { return (n[b] || 0) - (n[a] || 0); }).forEach(function (d) {
      h += '<a class="dom" href="#/domaines/' + d + '" data-link><b' + vtn("d-" + d) + ">" + esc(D.domaines[d]) + '</b><span class="num">' + n[d] + "</span></a>";
    });
    return h + "</div>";
  }

  /* ---------- recherche ---------- */
  function searchSchools(q) {
    var words = norm(q).split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    return SCH.filter(function (s) { return words.every(function (w) { return s._q.indexOf(w) !== -1; }); })
      .sort(function (a, b) { var x = norm(a.nom).indexOf(words[0]) === 0 ? 0 : 1, y = norm(b.nom).indexOf(words[0]) === 0 ? 0 : 1; return (x - y) || a.nom.localeCompare(b.nom, "fr"); });
  }
  function resultsHTML(q) {
    if (!q.trim()) return '<div class="chips" style="margin-top:4px">' + ["aéronautique", "informatique", "Lyon", "Toulouse", "chimie", "Île-de-France"].map(function (t) { return '<button class="chip" type="button" data-q="' + esc(t) + '" style="min-height:40px;cursor:pointer">' + esc(t) + "</button>"; }).join("") + "</div>";
    var r = searchSchools(q);
    if (!r.length) return '<p class="empty">Aucune école pour « ' + esc(q) + " ». Essaie un nom de ville ou de domaine.</p>";
    return '<p class="small mut" style="margin:0 0 4px">' + plural(r.length, "école", "écoles") + '</p><div class="rows">' + r.slice(0, 60).map(rowHTML).join("") + "</div>";
  }
  function viewChercher(q) {
    return '<h1 class="h1" style="margin-bottom:16px">Chercher</h1><label class="qbox">' + IC.search + '<input id="q" type="search" enterkeyhint="search" autocomplete="off" placeholder="Une école, une ville, un domaine" aria-label="Chercher une école" value="' + esc(q) + '"></label><div id="res" style="margin-top:16px">' + resultsHTML(q) + "</div>";
  }

  /* ---------- comprendre ---------- */
  function viewComprendre() {
    var h = '<a class="back" href="#/" data-link data-back>' + IC.back + 'Les concours</a><div class="prose"><h1 class="h1">Comprendre les concours</h1>';
    h += "<h2>Concours, banque, liste de vœux</h2><ul>";
    h += "<li><b>Un concours</b> classe les candidats après des écrits, puis des oraux pour les admissibles. Une <b>banque</b> regroupe des écoles qui utilisent les mêmes écrits mais font chacune leur classement.</li>";
    h += "<li>Tu t'inscris sur le site du SCEI en décembre-janvier, puis tu classes tes écoles dans ta <b>liste de vœux</b> jusqu'à fin juillet. Une école que tu mets au-dessus d'une autre passe avant : si elle t'est proposée, tu perds celles d'en dessous.</li>";
    h += "<li>Certains concours partagent leurs écrits : X et ENS, Mines-Ponts et Mines-Télécom, et en partie e3a-Polytech et le CCINP. C'est ainsi que les concours sont regroupés sur l'accueil.</li></ul>";
    h += "<h2>Lire les chiffres</h2><ul>";
    h += "<li><b>Places 2026</b> : places offertes à la session 2026, la dernière publiée. Sinon, elles sont partagées avec d'autres filières.</li>";
    h += "<li><b>Rang médian 2025</b> : la moitié des élèves de " + FIL + " admis en 2025 étaient classés avant ce rang (statistiques du SCEI, les dernières publiées).</li>";
    h += "<li><b>Un rang ne se compare qu'à l'intérieur d'une même liste de classement.</b> Mines-Ponts, le CCINP ou Polytech ont une seule liste : leurs écoles sont triées par rang. À Centrale-Supélec, dans la banque CCINP, aux ENS ou dans les écoles indépendantes d'e3a, chaque école a sa propre liste.</li>";
    h += "<li><b>Peu de places, rangs instables</b> : avec 2 à 6 places, un rang 2025 peut beaucoup bouger en 2026.</li></ul>";
    h += "<h2>Frais et boursiers</h2><ul><li>Frais par an pour un étudiant français, au montant le plus récent trouvé, avec son année. La CVEC (105 €) s'ajoute en général, sauf pour les boursiers.</li>";
    h += "<li>À l'X, aux ENS et dans les écoles militaires, les élèves sont payés pendant leurs études, en échange d'un engagement à servir l'État.</li></ul>";
    h += "<h2>Pas dans cette liste</h2><ul>" + D.exclus.map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + "</ul>";
    h += '<h2>Sources principales</h2><ul>' + D.sources.map(function (x) { return '<li><a href="' + esc(x.u) + '" target="_blank" rel="noopener">' + esc(x.t) + "</a></li>"; }).join("") + "</ul></div>";
    return h;
  }

  /* =====================================================================
     Fonctions du prototype v2 : calendrier, inscription, filière, explorateur, récit.
     ===================================================================== */

  /* ---------- calendrier 2027 (sources citées ; secondaires signalées) ---------- */
  var SRC = {
    x: { t: "École polytechnique, inscription CPGE 2027", u: "https://www.polytechnique.edu/admission-cycle-ingenieur/inscription-cpge" },
    ccmp: { t: "Concours Mines-Ponts, dates 2027", u: "https://concoursminesponts.fr" },
    cmt: { t: "Concours Mines-Télécom, dates clés 2027", u: "https://www.concours-mines-telecom.fr/le-concours-mines-telecom/les-dates-cles/" },
    virage: { t: "ViragePrépa, calendrier 2027 (source non officielle)", u: "https://www.virageprepa.com/articles/calendrier-des-concours-d-ing%C3%A9nieurs-2027-inscriptions-scei-%C3%A9crits-r%C3%A9sultats-oraux" },
    express: { t: "L'Express Éducation, CCINP 2027 (source non officielle)", u: "https://lexpress-education.com/articles/concours-ccinp/" },
    hadamard: { t: "Hadamard, répondre à une proposition SCEI (source non officielle)", u: "https://www.hadamard.fr/actualites/accepter-ou-attendre-proposition-scei" }
  };
  // k : sorte d'étape ; fam : concours concerné (null = tous) ; d1/d2 : dates ISO ; sec : source secondaire.
  var CAL = [
    { k: "insc", t: "Inscriptions sur le SCEI", d1: "2026-12-07", d2: "2027-01-11", h: "du 7 décembre 2026 à 10 h au 11 janvier 2027 à 17 h", src: SRC.x },
    { k: "pay", t: "Paiement et pièces justificatives", d1: "2027-01-11", d2: "2027-01-19", h: "paiement à partir du 11 janvier à 17 h ; paiement et pièces avant le 19 janvier à 17 h", src: SRC.x },
    { k: "voeux", t: "Liste de vœux ouverte", d1: "2027-03-01", d2: "2027-07-23", h: "du 1er mars au 23 juillet 2027 à 12 h", src: SRC.cmt },
    { k: "ecrits", fam: "x", t: "Écrits X-ENS", d1: "2027-04-12", d2: "2027-04-16", src: SRC.virage, sec: true, also: ["ens"] },
    { k: "ecrits", fam: "inp", t: "Écrits CCINP", d1: "2027-04-19", d2: "2027-04-22", src: SRC.express, sec: true },
    { k: "ecrits", fam: "mp", t: "Écrits Mines-Ponts", d1: "2027-04-30", d2: "2027-05-05", h: "30 avril, 3, 4 et 5 mai 2027", src: SRC.ccmp, also: ["mt"] },
    { k: "adm", fam: "x", t: "Admissibilité X", d1: "2027-05-26", src: SRC.virage, sec: true },
    { k: "adm", fam: "mp", t: "Admissibilité Mines-Ponts", d1: "2027-06-02", h: "à 18 h", src: SRC.ccmp },
    { k: "adm", fam: "mt", t: "Admissibilité Mines-Télécom", d1: "2027-06-03", h: "à 18 h", src: SRC.cmt },
    { k: "oraux", fam: "x", t: "Oraux X", fil: { MP: ["2027-06-14", "2027-07-04"], PC: ["2027-06-14", "2027-07-11"], MPI: ["2027-06-07", "2027-06-13"], PSI: ["2027-06-07", "2027-06-13"] }, src: SRC.virage, sec: true },
    { k: "oraux", fam: "mp", t: "Oraux Mines-Ponts", d1: "2027-06-21", d2: "2027-07-17", src: SRC.ccmp },
    { k: "res", fam: "mp", t: "Admission Mines-Ponts", d1: "2027-07-21", h: "à 18 h", src: SRC.ccmp },
    { k: "res", fam: "x", t: "Admission X", d1: "2027-07-23", h: "à 14 h", src: SRC.virage, sec: true }
  ];
  // Pas encore publié pour 2027 : on montre 2026, présenté comme tel.
  var PENDING = [
    { fam: "cs", t: "Centrale-Supélec" },
    { fam: "poly", t: "e3a-Polytech", also: ["e3a"] },
    { fam: null, t: "Propositions d'intégration", y26: "5 propositions, du 28 juillet au 4 septembre 2026", src: SRC.virage }
  ];
  var MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
  var MOIS_C = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."];
  function iso(d) { return new Date(d + "T12:00:00"); }
  function today() { var t = new Date(); t.setHours(12, 0, 0, 0); return t; }
  function dayDiff(a, b) { return Math.round((b - a) / 864e5); }
  function dFr(d, withYear) { var x = iso(d); return (x.getDate() === 1 ? "1er" : x.getDate()) + " " + MOIS[x.getMonth()] + (withYear ? " " + x.getFullYear() : ""); }
  function rangeFr(a, b) {
    if (!b || a === b) return dFr(a);
    var x = iso(a), y = iso(b);
    if (x.getMonth() === y.getMonth()) return (x.getDate() === 1 ? "1er" : x.getDate()) + "-" + y.getDate() + " " + MOIS[y.getMonth()];
    return dFr(a) + " au " + dFr(b);
  }
  function relFr(n) { return n === 0 ? "aujourd'hui" : n === 1 ? "demain" : n > 0 ? "dans " + n + " jours" : n === -1 ? "hier" : "il y a " + (-n) + " jours"; }
  function evDates(e) { if (e.fil) { var r = e.fil[FIL] || e.fil.MP; return [r[0], r[1]]; } return [e.d1, e.d2 || e.d1]; }
  function evFams(e) { return e.fam ? [e.fam].concat(e.also || []) : []; }
  function visibleCal(mine) {
    return CAL.filter(function (e) {
      if (!e.fam) return true;
      var fams = evFams(e).filter(function (f) { return famSchools(FAM[f]).length; });
      if (!fams.length) return false;
      return !mine || fams.some(function (f) { return mine.indexOf(f) !== -1; });
    }).map(function (e) { var d = evDates(e); return Object.assign({}, e, { a: d[0], b: d[1] }); })
      .sort(function (p, q) { return p.a < q.a ? -1 : p.a > q.a ? 1 : 0; });
  }
  function nextStep() {
    var t = today(), best = null;
    visibleCal(null).forEach(function (e) { if (iso(e.b) >= t && (!best || e.a < best.a)) best = e; });
    return best;
  }
  function y26(fid) {
    var b = ((D.familles[fid] || {}).blocs || [])[0];
    return b && b.ecrits && b.ecrits.quand ? "écrits " + b.ecrits.quand : "";
  }

  /* ---------- export vers le calendrier du téléphone (.ics) ---------- */
  function icsDate(d, plus) { var x = iso(d); x.setDate(x.getDate() + (plus || 0)); return x.getFullYear() + String(x.getMonth() + 1).padStart(2, "0") + String(x.getDate()).padStart(2, "0"); }
  function icsEsc(s) { return String(s).replace(/[\\;,]/g, function (c) { return "\\" + c; }).replace(/\n/g, "\\n"); }
  function exportIcs(evs, name) {
    var L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Ecoles d'ingenieurs//Calendrier 2027//FR", "CALSCALE:GREGORIAN"];
    evs.forEach(function (e, i) {
      L.push("BEGIN:VEVENT", "UID:" + e.k + "-" + (e.fam || "scei") + "-" + i + "-2027@ecoles-inge", "DTSTAMP:" + icsDate(new Date().toISOString().slice(0, 10)) + "T000000Z",
        "DTSTART;VALUE=DATE:" + icsDate(e.a), "DTEND;VALUE=DATE:" + icsDate(e.b, 1), "SUMMARY:" + icsEsc(e.t),
        "DESCRIPTION:" + icsEsc((e.h ? e.h + ". " : "") + "Source : " + e.src.t + " " + e.src.u), "END:VEVENT");
    });
    L.push("END:VCALENDAR");
    var blob = new Blob([L.join("\r\n")], { type: "text/calendar;charset=utf-8" }), a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name + ".ics"; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  }

  /* ---------- calendrier : frise + liste ---------- */
  var calMine = false;
  var KIND = { insc: "Inscriptions", pay: "Paiement", voeux: "Vœux", ecrits: "Écrits", adm: "Admissibilité", oraux: "Oraux", res: "Admission" };
  function fristHTML(evs) {
    var t0 = iso("2026-11-01"), t1 = iso("2027-09-30"), span = t1 - t0;
    var pos = function (d) { return Math.max(0, Math.min(100, (iso(d) - t0) / span * 100)); };
    var rows = [], seen = {};
    evs.forEach(function (e) {
      var key = e.fam ? (BLOC_OF[e.fam] ? BLOC_OF[e.fam].id + ":" + e.fam : e.fam) : "scei";
      if (!seen[key]) { seen[key] = { lab: e.fam ? FAM[e.fam].nom : "SCEI", c: e.fam ? "var(--f-" + e.fam + ")" : "var(--ink)", ev: [] }; rows.push(seen[key]); }
      seen[key].ev.push(e);
    });
    var h = '<div class="frise" aria-hidden="true"><div class="fr-months">';
    for (var m = 10; m <= 20; m++) { var mm = m % 12; h += '<span style="left:' + pos((m < 12 ? 2026 : 2027) + "-" + String(mm + 1).padStart(2, "0") + "-01") + '%">' + MOIS_C[mm].replace(".", "") + "</span>"; }
    h += "</div>";
    rows.forEach(function (r) {
      h += '<div class="fr-row"><span class="fr-lab">' + esc(r.lab) + '</span><div class="fr-track">';
      r.ev.forEach(function (e) {
        var a = pos(e.a), b = pos(e.b), w = Math.max(b - a, .9);
        h += '<i class="fr-bar k-' + e.k + '" style="left:' + a + "%;width:" + w + "%;--fc:" + r.c + '"></i>';
      });
      h += "</div></div>";
    });
    var tp = pos(today().toISOString().slice(0, 10));
    h += '<div class="fr-today" style="left:calc(var(--lab-w) + (100% - var(--lab-w)) * ' + (tp / 100) + ')"><span>aujourd\'hui</span></div>';
    return h + "</div>";
  }
  function viewCalendrier() {
    var mine = calMine && INSC.keys().length ? mineFams() : null;
    var evs = visibleCal(mine), t = today();
    var h = '<div class="cal"><div class="cal-head"><h1 class="h1">Le calendrier 2027</h1>';
    h += '<div class="cal-tools"><div class="seg2" role="group" aria-label="Concours affichés"><button type="button" data-calmine="0" aria-pressed="' + !calMine + '">Tous les concours</button><button type="button" data-calmine="1" aria-pressed="' + calMine + '">Mes concours</button></div>';
    h += '<button class="btnp" type="button" data-ics="1">' + IC.cal + "Ajouter à mon calendrier</button></div></div>";
    if (calMine && !INSC.keys().length) h += '<p class="empty" style="padding:8px 0 0">Coche tes concours dans <a href="#/inscription" data-link>Préparer mon inscription</a> : le calendrier ne montrera que les leurs.</p>';
    h += fristHTML(evs);
    var cur = null, placedToday = false;
    h += '<ol class="cal-list">';
    evs.forEach(function (e) {
      var d = iso(e.a), mk = d.getFullYear() + "-" + d.getMonth();
      if (!placedToday && iso(e.b) >= t) { placedToday = true; h += '<li class="cal-now"><span>Aujourd\'hui, ' + dFr(t.toISOString().slice(0, 10)) + "</span></li>"; }
      if (mk !== cur) { cur = mk; h += '<li class="cal-m">' + MOIS[d.getMonth()] + " " + d.getFullYear() + "</li>"; }
      var past = iso(e.b) < t, n = dayDiff(t, d), fc = e.fam ? "var(--f-" + e.fam + ")" : "var(--ink)";
      h += '<li class="cal-ev' + (past ? " past" : "") + '" style="--fc:' + fc + '"><span class="cal-d">' + esc(rangeFr(e.a, e.b)) + '</span><div class="cal-b"><b>' + esc(e.t) + "</b>";
      if (e.h) h += "<span>" + esc(e.h) + "</span>";
      if (!past) h += '<span class="cal-rel">' + (n > 0 ? relFr(n) : "en cours") + "</span>";
      h += '<a class="cal-src" href="' + esc(e.src.u) + '" target="_blank" rel="noopener">' + esc(e.src.t) + "</a></div></li>";
    });
    h += "</ol>";
    var pend = PENDING.filter(function (p) { return !p.fam || (famSchools(FAM[p.fam]).length && (!mine || [p.fam].concat(p.also || []).some(function (f) { return mine.indexOf(f) !== -1; }))); });
    if (pend.length) {
      h += '<section class="cal-pend"><h2 class="h2">Pas encore publié pour 2027</h2><ul>';
      pend.forEach(function (p) { h += "<li><b>" + esc(p.t) + "</b><span>En 2026 : " + esc(p.y26 || y26(p.fam)) + ".</span>" + (p.src ? '<a class="cal-src" href="' + esc(p.src.u) + '" target="_blank" rel="noopener">' + esc(p.src.t) + "</a>" : "") + "</li>"; });
      h += "</ul></section>";
    }
    return h + "</div>";
  }

  /* ---------- préparer mon inscription ---------- */
  var INSC = (function () {
    var st = {};
    try { st = JSON.parse(localStorage.getItem("ecoles-insc") || "{}") || {}; } catch (e) { st = {}; }
    function cur() { return st[FIL] || (st[FIL] = { k: [], b: false }); }
    function save() { try { localStorage.setItem("ecoles-insc", JSON.stringify(st)); } catch (e) { /* rien */ } }
    return {
      keys: function () { return cur().k; },
      bours: function () { return cur().b; },
      setBours: function (v) { cur().b = v; save(); },
      has: function (k) { return cur().k.indexOf(k) !== -1; },
      set: function (ks) { cur().k = ks; save(); }
    };
  })();
  var KEY_LAB = { x: "Concours X", ens: "Concours des ENS", ccmp: "Concours commun Mines-Ponts", cmt: "Concours Mines-Télécom", ccinp: "Dossier CCINP", insa: "Groupe INSA", e3a_poly: "Concours Polytech", avenir: "Avenir Prépas", ingeniup: "Ingéni'Up", epita: "Concours EPITA-IPSA-ESME", cesi: "Concours CESI", ut: "Groupe UT" };
  var GROUP_OF = { ccs_: "Centrale-Supélec, école par école", ind_: "Écoles indépendantes e3a", b_: "Banque CCINP, école par école" };
  function feeModel() {
    var keys = {}, deps = {}, schools = {};
    SCH.forEach(function (s) { s.acces.forEach(function (a) {
      (a.fee || []).forEach(function (k) {
        if (!keys[k]) keys[k] = { k: k, fam: k === "ccinp" ? "inp" : FAM_OF[a.c], n: 0 };
        (schools[k] = schools[k] || {})[s.id] = 1;
        var o = a.fee.filter(function (x) { return x !== k; });
        deps[k] = deps[k] ? deps[k].filter(function (x) { return o.indexOf(x) !== -1; }) : o;
      });
    }); });
    Object.keys(keys).forEach(function (k) { keys[k].n = Object.keys(schools[k]).length; var f = D.fees[k] || [k, null, null]; keys[k].nom = KEY_LAB[k] || f[0].replace(/^.*? : /, ""); keys[k].p = f[1]; keys[k].pb = f[2]; });
    return { keys: keys, deps: deps };
  }
  function prefixOf(k) { var p = Object.keys(GROUP_OF).filter(function (x) { return k.indexOf(x) === 0; })[0]; return p || null; }
  function coverage(sel) {
    var cov = {}, own = 0, shared = 0, fams = {};
    SCH.forEach(function (s) { s.acces.forEach(function (a) {
      if (!a.fee || !a.fee.length || !a.fee.every(function (k) { return sel.indexOf(k) !== -1; })) return;
      cov[s.id] = 1; fams[FAM_OF[a.c]] = 1;
      if (a.p26 != null) { if (a.scope === FIL) own += a.p26; else shared += a.p26; }
    }); });
    return { n: Object.keys(cov).length, own: own, shared: shared, fams: Object.keys(fams) };
  }
  function mineFams() { return coverage(INSC.keys()).fams; }
  function cost(sel, M) {
    var bo = INSC.bours(), t = 0, unk = [];
    sel.forEach(function (k) { var m = M.keys[k]; if (!m) return; var p = bo ? m.pb : m.p; if (p == null) unk.push(m.nom); else t += p; });
    return { t: t, unk: unk };
  }
  function priceTxt(m) { var p = INSC.bours() ? m.pb : m.p; return p == null ? "?" : p === 0 ? "gratuit" : fmt(p) + " €"; }
  function inscItem(m, M) {
    var on = INSC.has(m.k), dep = (M.deps[m.k] || []).map(function (d) { return M.keys[d] ? M.keys[d].nom : d; });
    return '<label class="ins-it' + (on ? " on" : "") + '"><input type="checkbox" data-insc="' + m.k + '"' + (on ? " checked" : "") + '><span class="ins-box" aria-hidden="true"></span><span class="ins-t"><b>' + esc(m.nom) + "</b><small>" + plural(m.n, "école", "écoles") + (dep.length ? ", avec le " + esc(dep.join(", ").replace(/^Dossier/, "dossier")) : "") + '</small></span><span class="ins-p num">' + priceTxt(m) + "</span></label>";
  }
  function viewInscription() {
    var M = feeModel(), sel = INSC.keys().filter(function (k) { return M.keys[k]; });
    var h = '<div class="ins-page"><div class="ins-main"><h1 class="h1">Préparer mon inscription</h1>';
    var ev = CAL[0], n = dayDiff(today(), iso(ev.d1)), n2 = dayDiff(today(), iso(ev.d2));
    h += '<p class="lede" style="margin-top:8px">' + (n > 0 ? "Inscriptions sur le SCEI du 7 décembre au 11 janvier, " + relFr(n) + "." : n2 >= 0 ? "Inscriptions ouvertes sur le SCEI jusqu'au 11 janvier, 17 h." : "Les inscriptions 2027 sont closes.") + "</p>";
    h += '<label class="switch"><input type="checkbox" data-bours="1"' + (INSC.bours() ? " checked" : "") + '><span class="sw-t" aria-hidden="true"></span><span>Je suis boursier</span></label>';
    BLOCS.forEach(function (b) {
      var fams = b.fams.filter(function (f) { return famSchools(FAM[f]).length; });
      if (!fams.length) return;
      fams.forEach(function (fid) {
        var items = Object.keys(M.keys).map(function (k) { return M.keys[k]; }).filter(function (m) { return m.fam === fid; });
        if (!items.length) return;
        var simple = items.filter(function (m) { return !prefixOf(m.k); }), groups = {};
        items.filter(function (m) { return prefixOf(m.k); }).forEach(function (m) { (groups[prefixOf(m.k)] = groups[prefixOf(m.k)] || []).push(m); });
        simple.sort(function (a, c) { return (a.k === "ccinp" ? -1 : 0) - (c.k === "ccinp" ? -1 : 0) || c.n - a.n; });
        h += '<section class="ins-fam" style="--fc:var(--f-' + fid + ')"><h2 class="ins-h"><i></i>' + esc(FAM[fid].nom) + "</h2>";
        simple.forEach(function (m) { h += inscItem(m, M); });
        Object.keys(groups).forEach(function (p) {
          var g = groups[p].sort(function (a, c) { return a.nom.localeCompare(c.nom, "fr"); }), nOn = g.filter(function (m) { return INSC.has(m.k); }).length;
          h += '<details class="ins-grp"' + (nOn ? " open" : "") + '><summary><span class="ins-t"><b>' + esc(GROUP_OF[p]) + "</b><small>" + nOn + " sur " + g.length + " cochée" + (nOn > 1 ? "s" : "") + "</small></span>" + IC.down + '</summary><div class="ins-grp-in"><button class="linkb" type="button" data-inscall="' + p + '">' + (nOn === g.length ? "Tout décocher" : "Tout cocher") + "</button>";
          g.forEach(function (m) { h += inscItem(m, M); });
          h += "</div></details>";
        });
        h += "</section>";
      });
    });
    h += '<p class="small mut" style="margin:18px 0 0">Tarifs 2026 du barème SCEI, ceux de 2027 n\'étant pas encore publiés (le concours X a confirmé 220 € pour 2027). Les frais de déplacement et d\'hébergement aux oraux ne sont pas comptés.</p>';
    h += "</div>" + recapHTML(M, sel) + "</div>";
    return h;
  }
  function recapHTML(M, sel) {
    var c = cost(sel, M), cov = coverage(sel);
    var h = '<aside class="ins-side"><div class="ins-bar"><div><b class="num" id="rc-bar" data-v="' + c.t + '">' + fmt(c.t) + " €</b><span>" + plural(cov.n, "école", "écoles") + '</span></div><button type="button" data-recap="1" style="min-height:40px;padding:0 14px;border:0;border-radius:11px;background:rgba(255,255,255,.14);color:#fff;font-weight:700;font-size:14.5px">Détail</button></div><div class="recap" id="recap"><div class="rc-top"><span class="rc-total num" id="rc-total" data-v="' + c.t + '">' + fmt(c.t) + ' €</span><span class="rc-sub">' + plural(cov.n, "école", "écoles") + ", " + plural(cov.own, "place", "places") + " en " + FIL + (cov.shared ? " + " + fmt(cov.shared) + " partagées" : "") + "</span></div>";
    if (c.unk.length) h += '<p class="small mut" style="margin:0">+ ' + esc(c.unk.join(", ")) + " : montant non trouvé.</p>";
    if (sel.length) {
      h += '<ul class="rc-list">' + sel.map(function (k) { return M.keys[k]; }).filter(Boolean).sort(function (a, b) { return a.fam < b.fam ? -1 : 1; }).map(function (m) { return '<li style="--fc:var(--f-' + m.fam + ')"><i></i><span>' + esc(m.nom) + '</span><b class="num">' + priceTxt(m) + "</b></li>"; }).join("") + "</ul>";
      var evs = visibleCal(cov.fams).filter(function (e) { return e.k === "ecrits"; });
      var pend = PENDING.filter(function (p) { return p.fam && [p.fam].concat(p.also || []).some(function (f) { return cov.fams.indexOf(f) !== -1; }); });
      if (evs.length || pend.length) {
        h += '<h3 class="rc-h">Tes écrits</h3><ul class="rc-ec">' + evs.map(function (e) { return '<li style="--fc:var(--f-' + e.fam + ')"><span>' + esc(rangeFr(e.a, e.b)) + "</span><b>" + esc(e.t.replace("Écrits ", "")) + "</b></li>"; }).join("");
        h += pend.map(function (p) { return '<li class="pend" style="--fc:var(--f-' + p.fam + ')"><span>2027 à venir</span><b>' + esc(p.t) + "</b></li>"; }).join("") + "</ul>";
        h += '<button class="btnp" type="button" data-ics="mine">' + IC.cal + "Ajouter ces dates</button>";
      }
    } else h += '<p class="small mut" style="margin:0">Coche les concours que tu comptes passer.</p>';
    return h + "</div></aside>";
  }
  function toggleKey(k, on) {
    var M = feeModel(), sel = INSC.keys().slice();
    var add = function (x) { if (sel.indexOf(x) === -1) sel.push(x); (M.deps[x] || []).forEach(add); };
    var rem = function (x) { sel = sel.filter(function (y) { return y !== x; }); Object.keys(M.deps).forEach(function (y) { if ((M.deps[y] || []).indexOf(x) !== -1 && sel.indexOf(y) !== -1) rem(y); }); };
    if (on) add(k); else rem(k);
    INSC.set(sel);
    refreshInsc(M);
  }
  function refreshInsc(M) {
    M = M || feeModel();
    var sel = INSC.keys();
    $$("input[data-insc]").forEach(function (i) { var on = sel.indexOf(i.dataset.insc) !== -1; i.checked = on; i.closest(".ins-it").classList.toggle("on", on); });
    $$(".ins-it .ins-p").forEach(function (p) { var k = p.parentNode.querySelector("input").dataset.insc; p.textContent = priceTxt(M.keys[k]); });
    $$(".ins-grp").forEach(function (g) {
      var ins = $$("input[data-insc]", g), n = ins.filter(function (i) { return i.checked; }).length, sm = $("summary small", g), bt = $("[data-inscall]", g);
      sm.textContent = n + " sur " + ins.length + " cochée" + (n > 1 ? "s" : ""); bt.textContent = n === ins.length ? "Tout décocher" : "Tout cocher";
    });
    var side = $(".ins-side"), old = $("#rc-total"), from = old ? +old.dataset.v : 0;
    var tmp = document.createElement("div"); tmp.innerHTML = recapHTML(M, sel);
    side.replaceWith(tmp.firstChild);
    var to = +$("#rc-total").dataset.v;
    if (!REDUCED && from !== to) {
      [$("#rc-total"), $("#rc-bar")].forEach(function (tot) {
        var t0 = performance.now(), dur = 420;
        (function step(t) { var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3); tot.textContent = fmt(Math.round(from + (to - from) * e)) + " €"; if (p < 1) requestAnimationFrame(step); })(t0);
        tot.animate([{ transform: "scale(1.08)" }, { transform: "none" }], { duration: 420, easing: SPRING });
      });
    }
  }

  /* ---------- choisir sa filière (1re année) ---------- */
  function statsFor(fil) {
    var out = {}, tot = { s: {}, own: 0, shared: 0 };
    ALL.forEach(function (raw) { raw.acces.forEach(function (a) {
      if (a.f !== fil) return;
      var fid = FAM_OF[a.c]; if (!fid) return;
      var o = out[fid] || (out[fid] = { s: {}, own: 0, shared: 0 });
      o.s[raw.id] = 1; tot.s[raw.id] = 1;
      if (a.p26 != null) { if (a.scope === fil) { o.own += a.p26; tot.own += a.p26; } else { o.shared += a.p26; tot.shared += a.p26; } }
    }); });
    return { fam: out, tot: tot };
  }
  function viewFiliere() {
    var cl = firstYear() ? ST.classe : "MPSI", fils = CLASSES[cl];
    var S = {}; fils.forEach(function (f) { S[f] = statsFor(f); });
    var max = 1; fils.forEach(function (f) { FAMS.forEach(function (fa) { var o = S[f].fam[fa.id]; if (o) max = Math.max(max, o.own + o.shared); }); });
    var h = '<a class="back" href="#/" data-link data-back>' + IC.back + 'Les concours</a><h1 class="h1">Après la ' + esc(cl) + "</h1>";
    h += '<div class="fil-cl" role="group" aria-label="Ta classe de 1re année">' + ["MPSI", "MP2I", "PCSI"].map(function (c) { return '<button class="seg" type="button" data-classe="' + c + '" aria-pressed="' + (c === cl) + '">' + c + "</button>"; }).join("") + "</div>";
    h += '<div class="fil-tot" style="grid-template-columns:repeat(' + fils.length + ',minmax(0,1fr))">' + fils.map(function (f) {
      var t = S[f].tot;
      return '<div class="fil-c"><span class="fil-n">' + f + '</span><b class="num">' + fmt(t.own) + "</b><span>places propres à la " + f + '</span><span class="mut">+ ' + fmt(t.shared) + " partagées, " + plural(Object.keys(t.s).length, "école", "écoles") + "</span></div>";
    }).join("") + "</div>";
    h += '<div class="fil-tab">';
    BLOCS.forEach(function (b) { b.fams.forEach(function (fid) {
      if (!fils.some(function (f) { return S[f].fam[fid]; })) return;
      h += '<div class="fil-row" style="--fc:var(--f-' + fid + ')"><a class="fil-lab" href="#/c/' + fid + '" data-link><i></i>' + esc(FAM[fid].nom) + "</a>";
      fils.forEach(function (f) {
        var o = S[f].fam[fid], v = o ? o.own + o.shared : 0;
        h += '<div class="fil-cell"><span class="fil-k">' + f + '</span><span class="fil-bar"><i style="width:' + (v / max * 100) + '%"></i></span><span class="fil-v num">' + (o ? fmt(o.own) + (o.shared ? "<small>+" + fmt(o.shared) + "</small>" : "") : "—") + "</span></div>";
      });
      h += "</div>";
    }); });
    h += '</div><p class="small mut" style="margin:14px 0 0">Places 2026 (notices des concours). « + » : places partagées avec d\'autres filières.</p>';
    return h;
  }

  /* ---------- explorateur ---------- */
  var EX = { q: "", fams: [], reg: "", doms: [], pub: false, bours: false }, xOpen = false;
  function exFromHash(qs) {
    var p = {}; (qs || "").split("&").forEach(function (kv) { var i = kv.indexOf("="); if (i > 0) p[kv.slice(0, i)] = decodeURIComponent(kv.slice(i + 1).replace(/\+/g, " ")); });
    EX = { q: p.q || "", fams: p.c ? p.c.split(",") : [], reg: p.r || "", doms: p.d ? p.d.split(",") : [], pub: p.pub === "1", bours: p.b === "1" };
  }
  function exHash() {
    var a = [];
    if (EX.q.trim()) a.push("q=" + encodeURIComponent(EX.q.trim()));
    if (EX.fams.length) a.push("c=" + EX.fams.join(","));
    if (EX.reg) a.push("r=" + EX.reg);
    if (EX.doms.length) a.push("d=" + EX.doms.join(","));
    if (EX.pub) a.push("pub=1");
    if (EX.bours) a.push("b=1");
    return "#/explorer" + (a.length ? "?" + a.join("&") : "");
  }
  function exFilter() {
    var words = norm(EX.q).split(/\s+/).filter(Boolean);
    return SCH.filter(function (s) {
      if (words.length && !words.every(function (w) { return s._q.indexOf(w) !== -1; })) return false;
      if (EX.fams.length && !s._fams.some(function (f) { return EX.fams.indexOf(f) !== -1; })) return false;
      if (EX.reg && !s._c1.some(function (c) { return c.r === EX.reg; })) return false;
      if (EX.doms.length && !s.dom.some(function (d) { return EX.doms.indexOf(d) !== -1; })) return false;
      if (EX.pub && !/^Public/.test(s.statut)) return false;
      if (EX.bours && !(s.bours.cat === "exo" || s.bours.cat === "remu")) return false;
      return true;
    }).sort(function (a, b) {
      if (words.length) { var x = norm(a.nom).indexOf(words[0]) === 0 ? 0 : 1, y = norm(b.nom).indexOf(words[0]) === 0 ? 0 : 1; if (x !== y) return x - y; }
      return a.nom.localeCompare(b.nom, "fr");
    });
  }
  function exRows(r) { return r.length ? r.map(function (s) { return rowHTML(s).replace('<a class="row"', '<a class="row" data-id="' + esc(s.id) + '"'); }).join("") : '<p class="empty">Aucune école avec ces critères. Retire un filtre pour élargir.</p>'; }
  function viewExplorer() {
    var h = '<h1 class="h1" style="margin-bottom:14px">Explorer</h1><label class="qbox">' + IC.search + '<input id="xq" type="search" enterkeyhint="search" autocomplete="off" placeholder="Une école, une ville, un mot" aria-label="Chercher" value="' + esc(EX.q) + '"></label>';
    var nAct = EX.fams.length + EX.doms.length + (EX.reg ? 1 : 0) + (EX.pub ? 1 : 0) + (EX.bours ? 1 : 0), wide = window.matchMedia("(min-width: 860px)").matches;
    h += '<details class="xfd"' + (wide || xOpen ? " open" : "") + '><summary class="xchip xsum"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M7 12h10M10 18h4"/></svg>Filtres<span id="xn">' + (nAct ? " (" + nAct + ")" : "") + "</span></summary>";
    h += '<div class="xf"><div class="xf-row" role="group" aria-label="Concours">' + FAMS.filter(function (f) { return famSchools(f).length; }).map(function (f) {
      return '<button class="xchip" type="button" data-xfam="' + f.id + '" aria-pressed="' + (EX.fams.indexOf(f.id) !== -1) + '" style="--fc:var(--f-' + f.id + ')"><i></i>' + esc(f.nom) + "</button>";
    }).join("") + "</div>";
    h += '<div class="xf-row"><select class="sel" data-xreg="1" aria-label="Région"><option value="">Toutes les régions</option>' + Object.keys(D.regions).sort(function (a, b) { return D.regions[a].localeCompare(D.regions[b], "fr"); }).map(function (r) { return '<option value="' + r + '"' + (EX.reg === r ? " selected" : "") + ">" + esc(D.regions[r]) + "</option>"; }).join("") + "</select>";
    h += '<button class="xchip" type="button" data-xpub="1" aria-pressed="' + EX.pub + '">Public</button><button class="xchip" type="button" data-xbours="1" aria-pressed="' + EX.bours + '">Gratuit si boursier</button></div>';
    h += '<div class="xf-row" role="group" aria-label="Domaines">' + Object.keys(DOM_SHORT).map(function (d) { return '<button class="xchip" type="button" data-xdom="' + d + '" aria-pressed="' + (EX.doms.indexOf(d) !== -1) + '">' + esc(DOM_SHORT[d]) + "</button>"; }).join("") + "</div></div></details>";
    var r = exFilter();
    h += '<p class="small mut" id="xcount" style="margin:16px 0 2px">' + plural(r.length, "école", "écoles") + '</p><div class="rows" id="xres">' + exRows(r) + "</div>";
    return h;
  }
  function exUpdate() {
    var box = $("#xres"); if (!box) return;
    var before = {};
    $$(".row[data-id]", box).forEach(function (el) { before[el.dataset.id] = el.getBoundingClientRect().top; });
    var r = exFilter();
    usedNames = {};
    box.innerHTML = exRows(r);
    $("#xcount").textContent = plural(r.length, "école", "écoles");
    var nAct = EX.fams.length + EX.doms.length + (EX.reg ? 1 : 0) + (EX.pub ? 1 : 0) + (EX.bours ? 1 : 0), xn = $("#xn"); if (xn) xn.textContent = nAct ? " (" + nAct + ")" : "";
    history.replaceState(Object.assign({}, history.state), "", exHash());
    cur = parse(location.hash);
    if (REDUCED || !box.animate) return;
    $$(".row[data-id]", box).forEach(function (el, i) {
      var b = before[el.dataset.id], now = el.getBoundingClientRect().top;
      if (b != null) { var dy = b - now; if (Math.abs(dy) > 1) el.animate([{ transform: "translateY(" + dy + "px)" }, { transform: "none" }], { duration: 480, easing: SPRING }); }
      else if (i < 14) el.animate([{ opacity: 0, transform: "translateY(10px)" }, { opacity: 1, transform: "none" }], { duration: 360, delay: Math.min(i, 10) * 22, easing: SPRING, fill: "backwards" });
    });
  }
  function toggleIn(arr, v) { var i = arr.indexOf(v); if (i === -1) arr.push(v); else arr.splice(i, 1); }

  /* ---------- comprendre : le parcours, en récit ---------- */
  var STEPS = [
    { id: "inscription", t: "Tu t'inscris", when: "7 déc. 2026 → 11 janv. 2027",
      p: ["Une seule inscription sur le site du SCEI, pour tous les concours que tu choisis. Après le 11 janvier à 17 h, plus aucun concours ne peut être ajouté.", "Paiement et pièces justificatives jusqu'au 19 janvier à 17 h : sans eux, le dossier est annulé."],
      link: ["#/inscription", "Préparer mon inscription"], src: [SRC.x, SRC.virage] },
    { id: "ecrits", t: "Les écrits", when: "avril → mai 2027",
      p: ["Chaque concours a sa semaine d'écrits. Certains partagent leurs copies : les mêmes épreuves comptent pour l'X et les ENS, pour Mines-Ponts et Mines-Télécom.", "En 2027 : X-ENS du 12 au 16 avril, CCINP du 19 au 22 avril, Mines-Ponts du 30 avril au 5 mai. Centrale-Supélec et e3a-Polytech n'ont pas encore publié leurs dates."],
      src: [SRC.ccmp, SRC.virage, SRC.express] },
    { id: "adm", t: "L'admissibilité", when: "fin mai → juin 2027",
      p: ["Chaque concours publie la liste de ses admissibles : ceux dont les écrits passent la barre. Seuls eux passent les oraux.", "En 2027 : l'X le 26 mai, Mines-Ponts le 2 juin, Mines-Télécom le 3 juin."],
      src: [SRC.ccmp, SRC.cmt, SRC.virage] },
    { id: "oraux", t: "Les oraux", when: "juin → juillet 2027",
      p: ["Planches de maths et de physique, langues, TIPE. Selon les concours, l'oral pèse de 20 % à plus de 70 % de la note finale : chaque page de concours donne son poids.", "Mines-Ponts : du 21 juin au 17 juillet 2027."],
      src: [SRC.ccmp] },
    { id: "voeux", t: "Ta liste de vœux", when: "1er mars → 23 juillet 2027",
      p: ["Tu classes les écoles où tu veux aller, par ordre de préférence. L'ordre compte : une école placée au-dessus d'une autre passe toujours avant.", "Ne pas établir de liste de vœux vaut démission."],
      src: [SRC.cmt, SRC.virage] },
    { id: "prop", t: "Les propositions", when: "fin juillet → septembre",
      p: ["À chaque phase, le SCEI te propose une école de ta liste. Tu réponds : « Oui définitif » pour t'arrêter là, ou « Oui mais » pour la garder en attendant un vœu mieux placé.", "Une absence de réponse vaut démission de toutes les écoles. En 2026, il y a eu 5 propositions, du 28 juillet au 4 septembre."],
      src: [SRC.hadamard, SRC.virage] }
  ];
  function viewComprendre2() {
    var h = '<div class="story"><div class="story-vis" aria-hidden="true"><div class="sv-in"><span class="sv-n" id="sv-n">1</span><span class="sv-t" id="sv-t">' + esc(STEPS[0].t) + '</span><span class="sv-w" id="sv-w">' + esc(STEPS[0].when) + '</span><ol class="sv-steps">';
    STEPS.forEach(function (s, i) { h += '<li data-i="' + i + '"' + (i === 0 ? ' class="on"' : "") + "><i></i><span>" + esc(s.t) + "</span></li>"; });
    h += '</ol></div></div><div class="story-txt"><h1 class="h1">Comprendre les concours</h1><p class="lede" style="margin-top:10px">De l\'inscription en décembre à l\'école en septembre.</p>';
    STEPS.forEach(function (s, i) {
      h += '<section class="st" data-i="' + i + '" id="st-' + s.id + '"><span class="st-n">' + (i + 1) + '</span><h2 class="h2">' + esc(s.t) + '</h2><span class="st-w">' + esc(s.when) + "</span>" + s.p.map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("");
      if (s.link) h += '<a class="btnlink" href="' + s.link[0] + '" data-link>' + esc(s.link[1]) + "</a>";
      h += '<div class="srcs">' + srcLinks(s.src) + "</div></section>";
    });
    h += '<section class="st-ref"><h2 class="h2">Lire les chiffres</h2><ul>';
    h += "<li><b>Rang médian 2025</b> : la moitié des élèves de " + FIL + " admis en 2025 étaient classés avant ce rang (statistiques du SCEI, les dernières publiées).</li>";
    h += "<li><b>Un rang ne se compare qu'à l'intérieur d'une même liste de classement.</b> Mines-Ponts, le CCINP ou Polytech ont une seule liste ; à Centrale-Supélec, dans la banque CCINP ou aux ENS, chaque école a la sienne.</li>";
    h += "<li><b>Peu de places, rangs instables</b> : avec 2 à 6 places, un rang 2025 peut beaucoup bouger.</li>";
    h += "<li><b>Places 2026</b> : places offertes à la session 2026, la dernière publiée (notices des concours, L'Étudiant, Onisep). Sinon, elles sont partagées avec d'autres filières.</li>";
    if (FIL === "MPI") h += "<li><b>Liste commune à plusieurs filières</b> (Ingéni'Up, certaines écoles indépendantes d'e3a, quelques domaines INSA) : les filières sont classées ensemble ; places et rangs ne sont pas propres à la MPI. Polytech, lui, a une liste MPI à part.</li>";
    else h += "<li><b>Liste commune à plusieurs filières</b> (Polytech, Ingéni'Up, plusieurs domaines INSA) : MP, PC et PSI sont classés ensemble ; places et rangs ne sont pas propres à la " + FIL + ".</li>";
    if (FIL === "PC") h += "<li><b>Deux listes au CCINP</b> : en PC, le CCINP fait deux concours sur les mêmes copies, PC-Physique et PC-Chimie, avec des coefficients inversés. Compare les rangs liste par liste.</li>";
    h += "<li><b>« Classement 2025 … »</b> : en 2025, l'école figurait dans une autre section du SCEI (autre concours ou autre liste) ; son rang ne se compare pas directement à ceux de 2026.</li></ul>";
    h += '<h2 class="h2" style="margin-top:24px">Le style des concours</h2><ul><li>« Les sujets » résume le rapport du jury cité en lien (le dernier publié, en général en maths). « Pour qui » est un avis, déduit de ces rapports et du poids des épreuves : à prendre comme tel.</li></ul>';
    var fee0 = function (s) { var f = s.frais; return s.bours.cat === "remu" && f.min == null ? 0 : (f.min != null ? f.min : (f.ref != null ? f.ref : null)); };
    var own = SCH.filter(function (s) { var v = fee0(s); return /^Public/.test(s.statut) && s.bours.cat !== "remu" && v != null && v > 700; }).sort(function (a, b) { return fee0(a) - fee0(b); });
    h += '<h2 class="h2" style="margin-top:24px">Frais et boursiers</h2><ul><li>Frais par an pour un étudiant français, au montant le plus récent trouvé, avec son année. La CVEC (105 €) s\'ajoute en général, sauf pour les boursiers.</li>';
    if (own.length) h += "<li>La plupart des écoles publiques appliquent le droit national (630 €/an en 2026-2027). " + own.length + " écoles publiques demandent plus, de " + fmt(fee0(own[0])) + " € (" + esc(own[0].nom) + ") à " + fmt(fee0(own[own.length - 1])) + " € (" + esc(own[own.length - 1].nom) + ").</li>";
    h += "<li>À l'X, aux ENS et dans les écoles militaires, les élèves sont payés pendant leurs études, en échange d'un engagement à servir l'État.</li><li>« À vérifier » : source ancienne, non officielle, ambiguë ou absente. Chaque fiche donne ses sources.</li></ul>";
    var pa = SCH.filter(function (s) { return s.acces.some(function (a) { return a.c === "e3a_ind" && a.stats.some(function (v) { return v.c25 === "Puissance Alpha"; }); }); });
    h += '<h2 class="h2" style="margin-top:24px">Ce qui a changé en 2026</h2><ul>';
    h += "<li>ENSTA Paris et ENSTA Bretagne ont fusionné : places à Palaiseau et à Brest via Mines-Ponts, et nouvelle formation défense et sécurité (FIDS), codélivrée avec l'ISAE-SUPAERO, via Mines-Télécom.</li>";
    h += "<li>L'ENAC et l'ISAE-ENSMA ont quitté le CCINP pour Mines-Télécom.</li>";
    if (pa.length) h += "<li>Les écoles de l'ex-concours Puissance Alpha recrutent maintenant les " + FIL + " via e3a-Polytech (" + esc(pa.map(function (s) { return s.nom; }).join(", ")) + ") ; l'ESIEE Paris, via la banque CCINP.</li>";
    h += "<li>Nouvelles venues : Centrale Lyon ENISE (banque CCINP) et Aflokkat MIRA (e3a-Polytech). L'ECE n'est plus dans Avenir Prépas.</li>";
    h += "<li>Noms récents, que la recherche reconnaît aussi sous l'ancien nom : Géodata Paris (ex-ENSG Géomatique), Centrale Méditerranée (ex-Centrale Marseille).</li></ul>";
    h += '<h2 class="h2" style="margin-top:24px">Pas dans cette liste</h2><ul>' + D.exclus.map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + "</ul>";
    h += '<h2 class="h2" style="margin-top:24px">Sources principales</h2><ul>' + D.sources.map(function (x) { return '<li><a href="' + esc(x.u) + '" target="_blank" rel="noopener">' + esc(x.t) + "</a></li>"; }).join("") + "</ul>";
    h += '<p class="small mut">Données ' + FIL + " relevées le " + esc(dFr(D.maj, true)) + ". Places, épreuves et tarifs sont ceux de 2026 tant que les notices 2027 ne sont pas publiées.</p></section></div></div>";
    return h;
  }
  var storyObs = null;
  function storyInit() {
    if (storyObs) { storyObs.disconnect(); storyObs = null; }
    var secs = $$(".st"); if (!secs.length || !("IntersectionObserver" in window)) return;
    var curI = 0;
    storyObs = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = +en.target.dataset.i; if (i === curI) return;
        var dir = i > curI ? 1 : -1; curI = i;
        var s = STEPS[i], n = $("#sv-n"), t = $("#sv-t"), w = $("#sv-w"); if (!n) return;
        $$(".sv-steps li").forEach(function (li) { li.classList.toggle("on", +li.dataset.i === i); li.classList.toggle("done", +li.dataset.i < i); });
        secs.forEach(function (x) { x.classList.toggle("on", x === en.target); });
        var swap = function () { n.textContent = i + 1; t.textContent = s.t; w.textContent = s.when; };
        if (REDUCED || !n.animate) { swap(); return; }
        [n, t, w].forEach(function (el, k) {
          el.animate([{ opacity: 1, transform: "none" }, { opacity: 0, transform: "translateY(" + (-dir * 18) + "px)" }], { duration: 160, delay: k * 30, easing: "ease-in", fill: "forwards" }).finished.then(function () {
            if (k === 0) swap();
            el.animate([{ opacity: 0, transform: "translateY(" + (dir * 22) + "px)" }, { opacity: 1, transform: "none" }], { duration: 460, easing: SPRING, fill: "forwards" });
          });
        });
      });
    }, { rootMargin: "-45% 0px -45% 0px" });
    secs.forEach(function (s) { storyObs.observe(s); });
    secs[0].classList.add("on");
  }

  /* ---------- les concours côte à côte ---------- */
  function viewCote() {
    var h = '<a class="back" href="#/" data-link data-back>' + IC.back + 'Les concours</a><h1 class="h1">Côte à côte</h1><div class="cote">';
    BLOCS.forEach(function (b) { b.fams.forEach(function (fid) {
      var f = FAM[fid], all = famSchools(f); if (!all.length) return;
      var P = famPlaces(f, all), FD = D.familles[fid] || {};
      var pl = fid === "autres" ? "—" : P.own ? fmt(P.own) + (P.shared ? " + " + fmt(P.shared) + " partagées" : "") : P.shared ? fmt(P.shared) + " partagées" : "—";
      h += '<a class="ct" href="#/c/' + fid + '" data-link style="--c:' + b.c + ";--fc:var(--f-" + fid + ')"><span class="ct-h"><i></i><b' + vtn("t-" + fid) + ">" + esc(f.nom) + "</b>" + IC.chev + "</span>";
      [["Écoles", String(all.length)], ["Places en " + FIL + " 2026", pl], ["Inscription", FD.inscCourt || "—"], ["Écrits", FD.ecritsCourt || "—"], ["Poids de l'oral", FD.poidsCourt || "—"], ["Style", (FD.style && FD.style.mots) || "—"]].forEach(function (r) {
        h += '<span class="ct-r"><span>' + r[0] + "</span><b>" + esc(r[1]) + "</b></span>";
      });
      h += "</a>";
    }); });
    return h + '</div><p class="small mut" style="margin:14px 0 0">Sources : notices des concours 2026 et barème du SCEI 2026, détaillés sur chaque page de concours.</p>';
  }

  /* ---------- routeur ---------- */
  var view = $("#view"), hIdx = 0, cur = null, lastConcours = null;
  var LEGACY = { "#comprendre": "#/comprendre", "#sources": "#/comprendre", "#guide": "#/explorer", "#cote": "#/cote" };
  function parse(hash) {
    if (hash && hash.indexOf("#/") !== 0) hash = LEGACY[hash] || "#/";
    var h = String(hash || "").replace(/^#/, ""), parts = h.split("?"), p = parts[0].split("/").filter(Boolean), q = "";
    if (parts[1]) { var m = parts[1].match(/(?:^|&)q=([^&]*)/); if (m) q = decodeURIComponent(m[1].replace(/\+/g, " ")); }
    var r = { v: p[0] || "home", a: p[1] ? decodeURIComponent(p[1]) : null, b: p[2] || null, q: q, qs: parts[1] || "" };
    if (r.v === "chercher") { r.v = "explorer"; }
    if (r.v === "domaines") { r.v = "explorer"; r.qs = r.a ? "d=" + r.a : ""; r.a = null; }
    if (r.v === "c") r.sec = "concours", r.depth = 1;
    else if (r.v === "e") r.sec = null, r.depth = 2;
    else if (r.v === "carte") r.sec = "carte", r.depth = 0;
    else if (r.v === "explorer") r.sec = "explorer", r.depth = 0;
    else if (r.v === "calendrier") r.sec = "calendrier", r.depth = 0;
    else if (r.v === "inscription") r.sec = "inscription", r.depth = 0;
    else if (r.v === "filiere") r.sec = "concours", r.depth = 1;
    else if (r.v === "cote") r.sec = "concours", r.depth = 1;
    else if (r.v === "comprendre") r.sec = "concours", r.depth = 1;
    else r.v = "home", r.sec = "concours", r.depth = 0;
    return r;
  }
  function labelOf(r) {
    if (!r) return null;
    if (r.v === "c" && FAM[r.a]) return FAM[r.a].nom;
    if (r.v === "carte") return r.a && D.regions[r.a] ? D.regions[r.a] : "La carte";
    if (r.v === "explorer") return "Explorer";
    if (r.v === "cote") return "Côte à côte";
    if (r.v === "calendrier") return "Le calendrier";
    if (r.v === "inscription") return "Mon inscription";
    if (r.v === "filiere") return "Après la " + (firstYear() ? ST.classe : "1re année");
    if (r.v === "e" && ALLBY[r.a]) return ALLBY[r.a].nom;
    return "Les concours";
  }
  function render(r) {
    usedNames = {};
    var h = null;
    if (r.v === "c") { h = viewConcours(r.a, r.b); if (h) lastConcours = r.a; }
    else if (r.v === "e") h = viewEcole(r.a);
    else if (r.v === "carte") h = viewCarte(r.a);
    else if (r.v === "explorer") { exFromHash(r.qs); h = viewExplorer(); }
    else if (r.v === "calendrier") h = viewCalendrier();
    else if (r.v === "inscription") h = viewInscription();
    else if (r.v === "filiere") h = viewFiliere();
    else if (r.v === "cote") h = viewCote();
    else if (r.v === "comprendre") h = viewComprendre2();
    if (h == null) { r = parse("#/"); h = viewHome(); }
    view.innerHTML = h;
    cur = r;
    chrome(r);
    afterRender(r);
  }
  var lastSec = "concours";
  function chrome(r) {
    var sec = r.sec || lastSec; lastSec = sec;
    $$("[data-tab]", $("#tabbar")).concat($$("[data-tab]", $("#topnav"))).forEach(function (a) {
      if (a.dataset.tab === sec) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
    var i = ["concours", "carte", "calendrier", "inscription", "explorer"].indexOf(sec);
    var tind = $(".ind", $("#tabbar")); if (tind) tind.style.transform = "translateX(" + (i * 100) + "%)";
    placeInd($("#topnav"), $('[data-tab="' + sec + '"]', $("#topnav")));
    $("#filbtn-cl").innerHTML = firstYear() ? esc(ST.classe) + ' <span style="font-weight:600;color:var(--mut)">' + esc(ST.fil) + "</span>" : esc(ST.classe);
    $("#filbtn").setAttribute("aria-label", "Ta classe : " + ST.classe + (firstYear() ? ", filière affichée " + ST.fil : "") + ". Changer");
  }
  function placeInd(box, el) {
    if (!box) return;
    var ind = $(".ind", box); if (!ind) return;
    if (!el || !el.offsetWidth) { ind.style.opacity = "0"; return; }
    ind.style.opacity = "1";
    ind.style.width = el.offsetWidth + "px";
    ind.style.transform = "translateX(" + el.offsetLeft + "px)";
  }
  function afterRender(r) {
    if (r.v === "c") placeInd($(".tabs-in"), $(".tab[aria-selected=\"true\"]"));
    if (r.v === "explorer") { var q = $("#xq"); if (q && window.matchMedia("(min-width: 860px)").matches) q.focus({ preventScroll: true }); }
    if (r.v === "comprendre") storyInit(); else if (storyObs) { storyObs.disconnect(); storyObs = null; }
  }
  function dirFor(from, to) {
    if (!from) return "fade";
    if (to.depth > from.depth) return "fwd";
    if (to.depth < from.depth) return "back";
    if (from.v !== to.v || (to.sec && from.sec && to.sec !== from.sec)) return "fade";
    return "fade";
  }
  function transition(dir, update, after) {
    var root = document.documentElement;
    if (!REDUCED && document.startViewTransition) {
      root.dataset.dir = dir;
      var t = document.startViewTransition(update);
      t.ready.catch(function () { /* transition interrompue par une autre : sans effet */ });
      t.finished.then(function () { delete root.dataset.dir; if (after) after(); }, function () { delete root.dataset.dir; });
      return;
    }
    update();
    if (!REDUCED && view.animate) {
      var x = dir === "fwd" ? 40 : dir === "back" ? -40 : 0, y = dir === "fade" ? 8 : 0;
      view.animate([{ opacity: 0, transform: "translate(" + x + "px," + y + "px)" }, { opacity: 1, transform: "none" }], { duration: 420, easing: SPRING });
    }
    if (after) after();
  }
  function show(dir, y) {
    var to = parse(location.hash), from = cur;
    dir = dir || dirFor(from, to);
    transition(dir, function () {
      render(to);
      window.scrollTo(0, y || 0);
    }, function () {
      if (to.v === "carte" && to.a && !window.matchMedia("(min-width: 980px)").matches) { var rl = $("#reglist"); if (rl && (y || 0) === 0) rl.scrollIntoView({ behavior: REDUCED ? "auto" : "smooth", block: "start" }); }
    });
  }
  function navigate(href, opts) {
    opts = opts || {};
    if (href === location.hash && !opts.force) { window.scrollTo({ top: 0, behavior: REDUCED ? "auto" : "smooth" }); return; }
    var st = history.state || {}, here = location.hash || "#/";
    history.replaceState(Object.assign({}, st, { i: hIdx, y: window.scrollY }), "", here);
    if (opts.replace) history.replaceState({ i: hIdx, y: 0, prev: st.prev }, "", href);
    else { hIdx++; history.pushState({ i: hIdx, y: 0, prev: here }, "", href); }
    show(opts.dir, 0);
  }
  window.addEventListener("popstate", function (e) {
    var s = e.state || {}, i = s.i || 0;
    var to = parse(location.hash), dir = cur && to.depth === cur.depth ? (i < hIdx ? "back" : "fwd") : null;
    if (cur && to.depth === cur.depth && to.v !== cur.v) dir = "fade";
    hIdx = i;
    show(dir, s.y || 0);
  });

  /* ---------- onglets d'un concours ---------- */
  function switchTab(tab) {
    var wrap = $(".panels"); if (!wrap) return;
    var fid = wrap.dataset.fam, old = wrap.dataset.cur;
    if (tab === old) return;
    var tabs = famTabs(FAM[fid]).map(function (t) { return t[0]; }), d = tabs.indexOf(tab) > tabs.indexOf(old) ? 1 : -1;
    var oldEl = $(".panel", wrap), h0 = wrap.offsetHeight;
    var neu = document.createElement("div");
    neu.className = "panel"; neu.id = "panel"; neu.setAttribute("role", "tabpanel"); neu.setAttribute("aria-labelledby", "tab-" + tab);
    usedNames = {};
    neu.innerHTML = panelHTML(fid, tab);
    oldEl.removeAttribute("id"); oldEl.setAttribute("aria-hidden", "true");
    oldEl.style.position = "absolute"; oldEl.style.left = "0"; oldEl.style.right = "0"; oldEl.style.top = "0";
    wrap.appendChild(neu);
    wrap.dataset.cur = tab;
    $$(".tab", $(".tabs")).forEach(function (b) { b.setAttribute("aria-selected", b.dataset.tab === tab ? "true" : "false"); });
    placeInd($(".tabs-in"), $('.tab[data-tab="' + tab + '"]'));
    history.replaceState(Object.assign({}, history.state, { y: window.scrollY }), "", "#/c/" + fid + (tab === "ecoles" ? "" : "/" + tab));
    cur = parse(location.hash);
    var tabsEl = $(".tabs"), top = tabsEl.getBoundingClientRect().top + window.scrollY - parseInt(getComputedStyle(document.documentElement).getPropertyValue("--top-h"), 10);
    if (window.scrollY > top + 2) window.scrollTo({ top: top, behavior: "auto" });
    if (REDUCED || !wrap.animate) { oldEl.remove(); return; }
    var h1 = neu.offsetHeight;
    oldEl.animate([{ opacity: 1, transform: "none" }, { opacity: 0, transform: "translateX(" + (-d * 48) + "px)" }], { duration: 240, easing: "cubic-bezier(.4,0,.2,1)", fill: "forwards" }).finished.then(function () { oldEl.remove(); });
    neu.animate([{ opacity: 0, transform: "translateX(" + (d * 64) + "px)" }, { opacity: 1, transform: "none" }], { duration: 520, easing: SPRING, delay: 40, fill: "backwards" });
    wrap.animate([{ height: h0 + "px" }, { height: h1 + "px" }], { duration: 520, easing: SPRING });
  }
  function refreshPanel() {
    var wrap = $(".panels"); if (!wrap) return;
    var p = $(".panel", wrap), h0 = wrap.offsetHeight;
    usedNames = {};
    p.innerHTML = panelHTML(wrap.dataset.fam, wrap.dataset.cur);
    if (REDUCED || !p.animate) return;
    var h1 = wrap.offsetHeight;
    p.animate([{ opacity: .2 }, { opacity: 1 }], { duration: 300, easing: SPRING });
    wrap.animate([{ height: h0 + "px" }, { height: h1 + "px" }], { duration: 420, easing: SPRING });
  }
  var sw = null;
  document.addEventListener("touchstart", function (e) {
    var p = e.target.closest(".panels"); if (!p || e.touches.length !== 1) { sw = null; return; }
    sw = { x: e.touches[0].clientX, y: e.touches[0].clientY, t: Date.now() };
  }, { passive: true });
  document.addEventListener("touchend", function (e) {
    if (!sw) return;
    var t = e.changedTouches[0], dx = t.clientX - sw.x, dy = t.clientY - sw.y, fast = Date.now() - sw.t < 600;
    sw = null;
    if (!fast || Math.abs(dx) < 60 || Math.abs(dx) < Math.abs(dy) * 1.6) return;
    var wrap = $(".panels"); if (!wrap) return;
    var tabs = famTabs(FAM[wrap.dataset.fam]).map(function (x) { return x[0]; }), i = tabs.indexOf(wrap.dataset.cur) + (dx < 0 ? 1 : -1);
    if (i >= 0 && i < tabs.length) switchTab(tabs[i]);
  }, { passive: true });

  /* ---------- feuille « Ta classe » ---------- */
  var sheet = $("#sheet"), sheetOpen = false, sheetReturn = null;
  function openSheet() {
    $("#sheet-body").innerHTML = classeHTML(true);
    sheet.hidden = false; sheetOpen = true; sheetReturn = document.activeElement;
    requestAnimationFrame(function () { requestAnimationFrame(function () { sheet.classList.add("open"); $(".sheet-card").focus(); }); });
  }
  function closeSheet() {
    if (!sheetOpen) return;
    sheetOpen = false; sheet.classList.remove("open");
    setTimeout(function () { if (!sheetOpen) sheet.hidden = true; }, REDUCED ? 0 : 420);
    if (sheetReturn && sheetReturn.focus) sheetReturn.focus({ preventScroll: true });
  }
  function setClasse(c, fil) {
    var reach = CLASSES[c];
    ST.classe = c;
    ST.fil = fil && reach.indexOf(fil) !== -1 ? fil : (reach.indexOf(ST.fil) !== -1 && reach.length > 1 ? ST.fil : reach[0]);
    save();
    var y = window.scrollY;
    transition("fade", function () {
      if (FIL !== ST.fil) applyFil(ST.fil);
      render(parse(location.hash));
      window.scrollTo(0, y);
      if (sheetOpen) $("#sheet-body").innerHTML = classeHTML(true);
    });
  }

  /* ---------- événements ---------- */
  document.addEventListener("click", function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var sk = e.target.closest("a.skip");
    if (sk) { e.preventDefault(); var h1 = $("#view h1"); (h1 || view).setAttribute("tabindex", "-1"); (h1 || view).focus(); return; }
    var a = e.target.closest("a[data-link]");
    if (a) {
      e.preventDefault();
      if (a.hasAttribute("data-back")) {
        if ((history.state || {}).prev === a.getAttribute("href") && hIdx > 0) history.back();
        else navigate(a.getAttribute("href"), { dir: "back" });
        return;
      }
      navigate(a.getAttribute("href"), { replace: a.hasAttribute("data-replace"), dir: a.hasAttribute("data-replace") ? "fade" : null });
      return;
    }
    var p = e.target.closest("path[data-region]");
    if (p) { var r = p.dataset.region; navigate(cur && cur.a === r ? "#/carte" : "#/carte/" + r, { replace: true, dir: "fade" }); return; }
    var b = e.target.closest("button");
    if (!b) { if (e.target.closest("[data-close]")) closeSheet(); return; }
    var d = b.dataset;
    if (b.id === "filbtn") { sheetOpen ? closeSheet() : openSheet(); return; }
    if (d.classe) { setClasse(d.classe); if (sheetOpen && CLASSES[d.classe].length === 1) setTimeout(closeSheet, 260); return; }
    if (d.fil) { setClasse(ST.classe, d.fil); return; }
    if (d.tab && b.classList.contains("tab")) { switchTab(d.tab); return; }
    if (d.recap) { var rc = $("#recap"); if (rc) rc.scrollIntoView({ behavior: REDUCED ? "auto" : "smooth", block: "start" }); return; }
    if (d.calmine != null) { calMine = d.calmine === "1"; transition("fade", function () { render(cur); }); return; }
    if (d.ics) {
      var mine2 = d.ics === "mine" || (calMine && INSC.keys().length) ? mineFams() : null;
      exportIcs(visibleCal(mine2), mine2 ? "mes-concours-2027" : "concours-2027"); return;
    }
    if (d.inscall) {
      var M0 = feeModel(), ks = Object.keys(M0.keys).filter(function (k) { return k.indexOf(d.inscall) === 0; });
      var allOn = ks.every(function (k) { return INSC.has(k); });
      ks.forEach(function (k) { toggleKey(k, !allOn); }); return;
    }
    if (d.xfam) { toggleIn(EX.fams, d.xfam); b.setAttribute("aria-pressed", EX.fams.indexOf(d.xfam) !== -1); exUpdate(); return; }
    if (d.xdom) { toggleIn(EX.doms, d.xdom); b.setAttribute("aria-pressed", EX.doms.indexOf(d.xdom) !== -1); exUpdate(); return; }
    if (d.xpub) { EX.pub = !EX.pub; b.setAttribute("aria-pressed", EX.pub); exUpdate(); return; }
    if (d.xbours) { EX.bours = !EX.bours; b.setAttribute("aria-pressed", EX.bours); exUpdate(); return; }
    if (d.q != null) { var q = $("#q"); if (q) { q.value = d.q; q.dispatchEvent(new Event("input", { bubbles: true })); } return; }
  });
  document.addEventListener("toggle", function (e) { if (e.target.classList && e.target.classList.contains("xfd")) xOpen = e.target.open; }, true);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && sheetOpen) { closeSheet(); return; }
    var t = e.target;
    if (t.classList && t.classList.contains("tab") && (e.key === "ArrowRight" || e.key === "ArrowLeft")) {
      var tabs = $$(".tab", $(".tabs")), i = tabs.indexOf(t) + (e.key === "ArrowRight" ? 1 : -1);
      if (tabs[i]) { tabs[i].focus(); switchTab(tabs[i].dataset.tab); e.preventDefault(); }
    }
  });
  document.addEventListener("change", function (e) {
    var t = e.target, d = t.dataset;
    if (d.freg) { ui.filt[d.freg].reg = t.value; refreshPanel(); }
    if (d.fdom) { ui.filt[d.fdom].dom = t.value; refreshPanel(); }
    if (d.insc) { toggleKey(d.insc, t.checked); }
    if (d.bours) { INSC.setBours(t.checked); refreshInsc(); }
    if (d.xreg) { EX.reg = t.value; exUpdate(); }
  });
  var qTimer;
  var xTimer;
  document.addEventListener("input", function (e) {
    if (e.target.id === "xq") { clearTimeout(xTimer); var xv = e.target.value; xTimer = setTimeout(function () { EX.q = xv; exUpdate(); }, 120); return; }
    if (e.target.id !== "q") return;
    clearTimeout(qTimer);
    var v = e.target.value;
    qTimer = setTimeout(function () {
      var res = $("#res"); if (!res) return;
      res.innerHTML = resultsHTML(v);
      history.replaceState(Object.assign({}, history.state), "", "#/chercher" + (v.trim() ? "?q=" + encodeURIComponent(v.trim()) : ""));
      cur = parse(location.hash);
    }, 110);
  });
  window.addEventListener("resize", function () {
    if (!cur) return;
    placeInd($("#topnav"), $('[aria-current="page"]', $("#topnav")));
    if (cur.v === "c") placeInd($(".tabs-in"), $('.tab[aria-selected="true"]'));
  });

  /* ---------- démarrage ---------- */
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  Promise.all([fetch(BASE + "data.json").then(function (r) { return r.json(); }), fetch(BASE + "map.json").then(function (r) { return r.json(); })]).then(function (res) {
    D = res[0]; MAP = res[1];
    ALL = D.ecoles; ALL.forEach(function (s) { ALLBY[s.id] = s; });
    applyFil(ST.fil);
    var h0 = location.hash; if (h0 && h0.indexOf("#/") !== 0) h0 = LEGACY[h0] || "#/";
    history.replaceState({ i: 0, y: 0 }, "", h0 || "#/");
    show("fade", 0);
  }).catch(function () {
    view.innerHTML = '<p class="empty">Les données n\'ont pas pu être chargées. Recharge la page.</p>';
  });
})();
