# Prototype v2 : pages, calculs de l'inscription, calendrier (.ics), explorateur, récit ; 3 habillages ; téléphone et PC.
import json, os, subprocess, sys, time
from playwright.sync_api import sync_playwright
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
data = json.load(open(os.path.join(ROOT, "prototype", "data.json"), encoding="utf-8"))
ids = [s["id"] for s in data["ecoles"]]
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8766", "--bind", "127.0.0.1"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8766/prototype/v2/"
errs, bad, fails = [], [], []
CHECK = """() => {
  const vw = document.documentElement.clientWidth, v = document.getElementById('view');
  const side = [...v.querySelectorAll('*')].filter(e => /auto|scroll/.test(getComputedStyle(e).overflowX) && e.scrollWidth > e.clientWidth + 1).length;
  const names = {}; let dup = null;
  document.querySelectorAll('[style*="view-transition-name"]').forEach(e => { const n = e.style.viewTransitionName; if (names[n]) dup = n; names[n] = 1; });
  return { over: document.documentElement.scrollWidth > vw + 1 || side > 0, bad: (v.innerText.match(/undefined|NaN|\\[object|\\bnull\\b|Invalid Date/) || [null])[0], dup, h1: (v.querySelector('h1') || {}).textContent };
}"""
def ok(cond, msg):
    if not cond: fails.append(msg)
try:
    with sync_playwright() as p:
        br = p.chromium.launch()
        for style in ("", "?style=b", "?style=mix"):
            for w, mob in ((390, True), (1280, False)):
                ctx = br.new_context(viewport={"width": w, "height": 860}, is_mobile=mob, has_touch=mob, accept_downloads=True)
                pg = ctx.new_page()
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "Transition was skipped" not in m.text else None)
                pg.route("**/fonts.g*/**", lambda r: r.abort())
                for classe in (("MP", "MPSI") if not style else ("MP",)):
                    pg.goto(URL + style + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                    pg.evaluate("c => { localStorage.clear(); localStorage.setItem('ecoles-proto', JSON.stringify({classe: c, fil: c === 'MPSI' ? 'MP' : c})); }", classe)
                    pg.goto(URL + style + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                    routes = ["#/", "#/carte", "#/carte/ara", "#/calendrier", "#/inscription", "#/filiere", "#/explorer", "#/explorer?c=mp,cs&r=idf", "#/domaines/info", "#/chercher?q=lyon", "#/comprendre"]
                    routes += ["#/c/" + f + t for f in ("x", "ens", "mp", "mt", "cs", "inp", "poly", "e3a", "autres") for t in ("", "/epreuves", "/style", "/inscription")]
                    routes += ["#/e/" + i for i in (ids if (not style and w == 390) else ids[:25])]
                    for r in routes:
                        pg.evaluate("h => { location.hash = h; }", r)
                        pg.wait_for_timeout(12 if r.startswith("#/e/") else 60)
                        res = pg.evaluate(CHECK)
                        if res["over"] or res["bad"] or res["dup"] or not res["h1"]:
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
                pg.click('[data-calmine="1"]'); pg.wait_for_timeout(600)
                n_mine = pg.evaluate("document.querySelectorAll('.cal-ev').length")
                ok(0 < n_mine < n_all, f"calendrier : {n_all} étapes, {n_mine} pour mes concours")
                with pg.expect_download() as dl:
                    pg.click('[data-ics="1"]')
                ics = open(dl.value.path(), encoding="utf-8").read()
                ok(ics.count("BEGIN:VEVENT") == n_mine and "DTSTART;VALUE=DATE:20270430" in ics, f"ics : {ics.count('BEGIN:VEVENT')} évènements")
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
                if style == "" or w == 390:
                    for r, n in (("#/", "home"), ("#/calendrier", "cal"), ("#/inscription", "insc"), ("#/filiere", "fil"), ("#/explorer", "expl"), ("#/comprendre", "story")):
                        pg.evaluate("h => { location.hash = h; }", r); pg.wait_for_timeout(700)
                        pg.screenshot(path="/home/claude/shots/v2-%s%d-%s.png" % (style.replace("?style=", "") + "-" if style else "", w, n))
                print(style or "neutre", w, "ok")
                ctx.close()
        br.close()
finally:
    srv.terminate()
print("pages en défaut :", len(bad), bad[:6])
print("contrôles en échec :", fails)
print("errors:", [e for e in errs if "ERR_FAILED" not in e][:6], "(polices Google bloquées dans le test : ignorées)")
