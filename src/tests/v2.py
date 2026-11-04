# Prototype v2 : pages, calculs de l'inscription, calendrier (.ics), explorateur, récit ; 3 habillages ; téléphone et PC.
import json, os, subprocess, sys, time
from playwright.sync_api import sync_playwright
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
data = json.load(open(os.path.join(ROOT, "prototype", "data.json"), encoding="utf-8"))
ids = [s["id"] for s in data["ecoles"]]
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8766", "--bind", "127.0.0.1"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
SITE = len(sys.argv) > 1 and sys.argv[1] == "site"
URL = "http://127.0.0.1:8766/" if SITE else "http://127.0.0.1:8766/prototype/v2/"
errs, bad, fails = [], [], []
CHECK = """() => {
  const vw = document.documentElement.clientWidth, v = document.getElementById('view');
  const side = [...v.querySelectorAll('*')].filter(e => /auto|scroll/.test(getComputedStyle(e).overflowX) && e.scrollWidth > e.clientWidth + 1).length;
  const names = {}; let dup = null;
  document.querySelectorAll('[style*="view-transition-name"]').forEach(e => { const n = e.style.viewTransitionName; if (names[n]) dup = n; names[n] = 1; });
  const rgb = c => { const m = (c.match(/[\\d.]+/g) || []).map(Number); if (m.length === 3) m.push(1); return m.length ? m : [0, 0, 0, 0]; };
  const lum = c => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }; return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2]); };
  const over_ = (top, bot) => [0, 1, 2].map(i => top[i] * top[3] + bot[i] * (1 - top[3]));
  const bgOf = e => { const L = [], q = e.getBoundingClientRect(), cx = q.left + q.width / 2, cy = q.top + q.height / 2; for (let x = e; x; x = x.parentElement) { const c = rgb(getComputedStyle(x).backgroundColor), o = x.getBoundingClientRect(); if (x !== document.documentElement && x !== document.body && (cx < o.left || cx > o.right || cy < o.top || cy > o.bottom)) continue; if (c[3] > 0) { L.push(c); if (c[3] >= 1) break; } }
    let col = L.length && L[L.length - 1][3] >= 1 ? L.pop().slice(0, 3) : rgb(getComputedStyle(document.documentElement).colorScheme === 'dark' ? 'rgb(0,0,0)' : 'rgb(255,255,255)').slice(0, 3);
    while (L.length) col = over_(L.pop(), col); return col; };
  const low = [];
  [...document.querySelectorAll('#view *, #top *')].forEach(e => {
    if (![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
    const r = e.getBoundingClientRect(), cs = getComputedStyle(e); if (!r.width || !r.height || cs.visibility === 'hidden' || +cs.opacity === 0) return;
    const fg = rgb(cs.color), bg = bgOf(e), f = over_(fg, bg), a = lum(f), b = lum(bg), k = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    if (k < 3 && low.length < 4) low.push([e.textContent.trim().slice(0, 30), Math.round(k * 100) / 100]);
  });
  return { low: low.length ? low : null, over: document.documentElement.scrollWidth > vw + 1 || side > 0, bad: (v.innerText.match(/undefined|NaN|\\[object|\\bnull\\b|Invalid Date/) || [null])[0], dup, h1: (v.querySelector('h1') || {}).textContent };
}"""
def ok(cond, msg):
    if not cond: fails.append(msg)
try:
    with sync_playwright() as p:
        br = p.chromium.launch()
        for style in (("", "dark", "neutre", "neutre dark") if SITE else ("", "?style=b", "?style=mix")):
            label = style if SITE else (style or "neutre")
            for w, mob in ((390, True), (1280, False)):
                ctx = br.new_context(viewport={"width": w, "height": 860}, is_mobile=mob, has_touch=mob, accept_downloads=True, color_scheme="dark" if "dark" in label else "light")
                if SITE and "neutre" in label: ctx.add_init_script("try { localStorage.setItem('ecoles-style', 'neutre'); } catch (e) {}")
                style = "" if SITE else style
                pg = ctx.new_page()
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "Transition was skipped" not in m.text else None)
                pg.route("**/fonts.g*/**", lambda r: r.abort())
                for classe in (("MP", "MPSI") if label in ("", "neutre") else ("MP",)):
                    pg.goto(URL + style + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                    pg.evaluate("c => { localStorage.clear(); localStorage.setItem('ecoles-proto', JSON.stringify({classe: c, fil: c === 'MPSI' ? 'MP' : c})); }", classe)
                    pg.goto("about:blank"); pg.goto(URL + style + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                    ok(pg.evaluate("JSON.parse(localStorage.getItem('ecoles-proto')).classe") == classe, f"classe {classe} non appliquée")
                    if SITE:
                        want = "neutre" if "neutre" in label else "actuel"
                        st = pg.evaluate("[document.documentElement.dataset.style, document.getElementById('st-actuel').media, document.getElementById('st-neutre').media, getComputedStyle(document.getElementById('stylebtn')).display]")
                        ok(st[0] == want and (st[1] == "not all") == (want == "neutre") and (st[2] == "not all") == (want == "actuel") and st[3] != "none", f"style {label} : {st}")
                    routes = ["#/cote", "#comprendre", "#/", "#/carte", "#/carte/ara", "#/calendrier", "#/inscription", "#/filiere", "#/explorer", "#/explorer?c=mp,cs&r=idf", "#/domaines/info", "#/chercher?q=lyon", "#/comprendre"]
                    routes += ["#/c/" + f + t for f in ("x", "ens", "mp", "mt", "cs", "inp", "poly", "e3a", "autres") for t in ("", "/epreuves", "/style", "/inscription")]
                    routes += ["#/e/" + i for i in (ids if (not style and w == 390) else ids[:25])]
                    for r in routes:
                        pg.evaluate("h => { location.hash = h; }", r)
                        pg.wait_for_timeout(12 if r.startswith("#/e/") else 60)
                        res = pg.evaluate(CHECK)
                        if res["over"] or res["bad"] or res["dup"] or res["low"] or not res["h1"]:
                            bad.append((style, w, classe, r, res))
                # inscription : Mines-Ponts + Polytech (le dossier CCINP doit s'ajouter tout seul)
                pg.evaluate("() => { location.hash = '#/inscription'; }"); pg.wait_for_timeout(500)
                pg.click('label:has(input[data-insc="ccmp"])'); pg.wait_for_timeout(500)
                pg.click('label:has(input[data-insc="e3a_poly"])'); pg.wait_for_timeout(600)
                tot = pg.evaluate("+document.querySelector('#rc-total').dataset.v")
                ccinp = pg.evaluate("document.querySelector('input[data-insc=\"ccinp\"]').checked")
                ok(tot == 360 + 130 + 240 and ccinp, f"total inscription {tot} (attendu 730), ccinp coché : {ccinp}")
                pg.click('label.switch'); pg.wait_for_timeout(600)
                tb = pg.evaluate("+document.querySelector('#rc-total').dataset.v")
                ok(tb == 0, f"total boursier {tb} (attendu 0)")
                pg.click('label.switch'); pg.wait_for_timeout(300)
                pg.click('label:has(input[data-insc="ccinp"])'); pg.wait_for_timeout(500)
                poly = pg.evaluate("document.querySelector('input[data-insc=\"e3a_poly\"]').checked")
                ok(not poly, "décocher le dossier CCINP doit décocher Polytech")
                ec = pg.evaluate("[...document.querySelectorAll('.rc-ec li')].map(l => l.innerText.replace(/\\s+/g,' '))")
                ok(any("30 avril" in x for x in ec), f"écrits Mines-Ponts dans le récap : {ec}")
                # calendrier : mes concours + export .ics
                pg.evaluate("() => { location.hash = '#/calendrier'; }"); pg.wait_for_timeout(500)
                n_all = pg.evaluate("document.querySelectorAll('.cal-ev').length")
                pcs = pg.evaluate("[document.querySelectorAll('.pc-s').length, !!document.querySelector('.cal-top .next'), document.querySelectorAll('.frise').length, (document.querySelector('.pc-s[data-next] .pc-t b') || {}).textContent]")
                ok(pcs[0] == 6 and pcs[1] and pcs[2] == 0 and pcs[3], f"calendrier : parcours {pcs}")
                pg.click('[data-calmine="1"]'); pg.wait_for_timeout(600)
                n_mine = pg.evaluate("document.querySelectorAll('.cal-ev').length")
                ok(0 < n_mine < n_all, f"calendrier : {n_all} étapes, {n_mine} pour mes concours")
                with pg.expect_download() as dl:
                    pg.click('[data-ics="1"]')
                ics = open(dl.value.path(), encoding="utf-8").read()
                ok(ics.count("BEGIN:VEVENT") == n_mine and "DTSTART;VALUE=DATE:20270430" in ics, f"ics : {ics.count('BEGIN:VEVENT')} évènements")
                # sujets et rapports : chaque filière, chaque concours, liens par épreuve
                for fil in ("MP", "PC", "PSI", "MPI"):
                    pg.evaluate("c => localStorage.setItem('ecoles-proto', JSON.stringify({classe: c, fil: c}))", fil)
                    pg.goto("about:blank"); pg.goto(URL + style + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                    shown = pg.evaluate("document.getElementById('filbtn-cl').textContent.trim()")
                    ok(shown == fil, f"filière affichée {shown} au lieu de {fil}")
                    for fid in ("x", "ens", "mp", "mt", "cs", "inp", "poly", "e3a"):
                        pg.evaluate("h => { location.hash = h; }", "#/c/" + fid + "/epreuves"); pg.wait_for_timeout(120)
                        res = pg.evaluate(CHECK)
                        an = pg.evaluate("""() => { const v = document.getElementById('view'), a = [...v.querySelectorAll('.ann a, .an-doc')];
                          return [a.length, a.filter(x => !/^https:/.test(x.href) || x.target !== '_blank').length, v.querySelectorAll('.ann-foot .ann-page').length,
                                  [...v.querySelectorAll('.eprow')].filter(r => r.querySelector('.ann')).length]; }""")
                        if res["over"] or res["bad"] or res["low"]: bad.append((style, w, fil, "#/c/" + fid + "/epreuves", res))
                        ok(an[0] > 3 and an[1] == 0 and an[2] >= 1 and an[3] >= 3, f"annales {fil} {fid} : {an}")
                        if fid == "inp": ok(pg.evaluate("f => !!document.querySelector('#view a[href*=\"annales-' + f + '.html\"]')", fil.lower()), f"annales CCINP de la filière {fil} absentes")
                        ok("Résultats ." not in pg.evaluate("document.getElementById('view').innerText"), f"« Résultats . » sur {fil} {fid}")
                pg.evaluate("() => localStorage.setItem('ecoles-proto', JSON.stringify({classe: 'MP', fil: 'MP'}))")
                pg.goto("about:blank"); pg.goto(URL + style + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                # explorateur : un filtre réduit la liste
                pg.evaluate("() => { location.hash = '#/explorer'; }"); pg.wait_for_timeout(500)
                n0 = pg.evaluate("document.querySelectorAll('#xres .row').length")
                if not pg.evaluate("document.querySelector('.xfd').open"): pg.click(".xsum"); pg.wait_for_timeout(300)
                pg.click('[data-xfam="cs"]'); pg.wait_for_timeout(600)
                n1 = pg.evaluate("document.querySelectorAll('#xres .row').length")
                ok(0 < n1 < n0, f"explorateur : {n0} puis {n1} avec Centrale-Supélec")
                # récit : l'étape active suit le défilement
                pg.evaluate("() => { location.hash = '#/comprendre'; }"); pg.wait_for_timeout(500)
                pg.evaluate("document.querySelector('#st-oraux').scrollIntoView({block:'center'})"); pg.wait_for_timeout(900)
                on = pg.evaluate("[(document.querySelector('.sv-steps li.on') || {dataset:{}}).dataset.i, document.querySelector('#sv-t').textContent]")
                ok(on[0] == "3" and on[1] == "Les oraux", f"récit : étape active {on}")
                if label in ("", "dark", "neutre", "neutre dark") and (label in ("", "dark", "neutre dark") or w == 390):
                    for r, n in (("#/", "home"), ("#/calendrier", "cal"), ("#/inscription", "insc"), ("#/filiere", "fil"), ("#/explorer", "expl"), ("#/comprendre", "story")):
                        pg.evaluate("h => { location.hash = h; }", r); pg.wait_for_timeout(700)
                        pg.screenshot(path="/home/claude/shots/%s-%s%d-%s.png" % ("site" if SITE else "v2", ((label.replace(" ", "-") + "-") if SITE and label else (style.replace("?style=", "") + "-" if style else "")), w, n))
                if SITE and label == "":
                    # bouton de style : bascule, mémorisé après rechargement, puis retour
                    pg.click("#stylebtn"); pg.wait_for_timeout(500)
                    a = pg.evaluate("[document.documentElement.dataset.style, document.getElementById('st-actuel').media, localStorage.getItem('ecoles-style'), document.getElementById('tc-l').content]")
                    pg.goto("about:blank"); pg.goto(URL + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                    b = pg.evaluate("document.documentElement.dataset.style")
                    pg.click("#stylebtn"); pg.wait_for_timeout(500)
                    c = pg.evaluate("[document.documentElement.dataset.style, document.getElementById('st-neutre').media]")
                    ok(a == ["neutre", "not all", "neutre", "#FFFFFF"] and b == "neutre" and c == ["actuel", "not all"], f"bouton de style : {a} {b} {c}")
                print(label or "actuel", w, "ok")
                ctx.close()
        br.close()
finally:
    srv.terminate()
print("pages en défaut :", len(bad), bad[:6])
print("contrôles en échec :", fails)
print("errors:", [e for e in errs if "ERR_FAILED" not in e][:6], "(polices Google bloquées dans le test : ignorées)")
