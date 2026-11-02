# Prototype : toutes les pages, 4 filières et une classe de 1re année, téléphone et PC.
# Vérifie : pas d'erreur JS, pas de « undefined/NaN », pas de défilement horizontal, transitions sans conflit de noms.
import json, os, subprocess, sys, time
from playwright.sync_api import sync_playwright
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
data = json.load(open(os.path.join(ROOT, "prototype", "data.json"), encoding="utf-8"))
ids = [s["id"] for s in data["ecoles"]]
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8765", "--bind", "127.0.0.1"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8765/prototype/"
errs, bad = [], []
CHECK = """() => {
  const vw = document.documentElement.clientWidth, v = document.getElementById('view');
  const side = [...v.querySelectorAll('*')].filter(e => /auto|scroll/.test(getComputedStyle(e).overflowX) && e.scrollWidth > e.clientWidth + 1).length;
  const names = {}; let dup = null;
  document.querySelectorAll('[style*="view-transition-name"]').forEach(e => { const n = e.style.viewTransitionName; if (names[n]) dup = n; names[n] = 1; });
  return { over: document.documentElement.scrollWidth > vw + 1 || side > 0, bad: (v.innerText.match(/undefined|NaN|\\[object|\\bnull\\b/) || [null])[0], dup, h1: (v.querySelector('h1') || {}).textContent };
}"""
try:
    with sync_playwright() as p:
        br = p.chromium.launch()
        for w, mob in ((390, True), (1280, False)):
            ctx = br.new_context(viewport={"width": w, "height": 860}, is_mobile=mob, has_touch=mob)
            pg = ctx.new_page()
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            pg.goto(URL); pg.wait_for_function("document.querySelector('#view h1')")
            assert pg.evaluate("document.documentElement.clientWidth") == w, "viewport"
            for classe in ("MP", "PC", "PSI", "MPI", "MPSI"):
                pg.evaluate("c => { localStorage.setItem('ecoles-proto', JSON.stringify({classe: c, fil: c === 'MPSI' ? 'PSI' : c})); }", classe)
                pg.goto(URL + "#/"); pg.wait_for_function("document.querySelector('#view h1')")
                routes = ["#/", "#/carte", "#/carte/idf", "#/domaines", "#/domaines/info", "#/chercher?q=lyon", "#/comprendre"]
                for f in ("x", "ens", "mp", "mt", "cs", "inp", "poly", "e3a", "autres"):
                    for t in ("", "/epreuves", "/style", "/inscription"):
                        routes.append("#/c/" + f + t)
                routes += ["#/e/" + i for i in ids]
                for r in routes:
                    pg.evaluate("h => { location.hash = h; }", r)
                    pg.wait_for_timeout(15 if r.startswith("#/e/") else 40)
                    res = pg.evaluate(CHECK)
                    if res["over"] or res["bad"] or res["dup"] or not res["h1"]:
                        bad.append((w, classe, r, res))
                # navigation réelle par clics : accueil → concours → école → retour, onglets
                pg.goto(URL + "#/"); pg.wait_for_function("document.querySelector('.stn')")
                pg.click(".stn >> nth=2"); pg.wait_for_timeout(700)
                for tb in pg.query_selector_all(".tab"):
                    tb.click(); pg.wait_for_timeout(600)
                pg.click(".tab >> nth=0"); pg.wait_for_timeout(600)
                pg.click(".srow >> nth=0"); pg.wait_for_timeout(700)
                h1 = pg.evaluate("document.querySelector('#view h1').textContent")
                pg.click(".back"); pg.wait_for_timeout(700)
                back = pg.evaluate("location.hash")
                print(w, classe, "| clics : école", h1, "| retour", back)
                if classe in ("MP", "MPSI"):
                    pg.screenshot(path=os.path.join(ROOT, "src", "tests", "screens", "proto-%d-%s.png" % (w, classe)), full_page=True)
            ctx.close()
        br.close()
finally:
    srv.terminate()
print("pages en défaut :", len(bad), bad[:8])
print("errors:", errs[:8])
