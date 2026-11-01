from playwright.sync_api import sync_playwright
import json
import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
os.makedirs(D + "tests/screens", exist_ok=True)
BUILD = D + "../index.html"
data = json.load(open(D + "build/data.json"))
ids = [s["id"] for s in data["ecoles"]]
errs = []
CHECK = """() => {
  const vw = document.documentElement.clientWidth;
  const txt = document.getElementById('view').innerText;
  return { over: document.documentElement.scrollWidth > vw + 1, bad: (txt.match(/undefined|NaN|\\[object|\\bnull\\b/) || [null])[0], h1: (document.querySelector('#view h1') || {}).textContent };
}"""
NAV = """([go, arg]) => { const b = document.createElement('button'); b.dataset.go = go; if (arg) b.dataset.arg = arg; b.hidden = true; document.body.appendChild(b); b.click(); b.remove(); }"""
with sync_playwright() as p:
    br = p.chromium.launch()
    for w in (390, 820, 1280):
        mob = {"is_mobile": True, "has_touch": True, "device_scale_factor": 3} if w < 720 else {}
        page = br.new_context(viewport={"width": w, "height": 900}, **mob).new_page()
        page.on("pageerror", lambda e: errs.append(str(e)))
        page.route("**/fonts.g*/**", lambda r: r.abort())
        page.goto("file://" + BUILD); page.wait_for_timeout(300)
        cw = page.evaluate("document.documentElement.clientWidth")
        if cw != w: errs.append(f"largeur de mise en page {cw} au lieu de {w} (balise viewport manquante ?)")
        for fil in ("MP", "PC", "PSI", "MPI"):
            page.evaluate("f => document.querySelector('.filsw [data-fil=\"' + f + '\"]').click()", fil); page.wait_for_timeout(200)
            title = page.title()
            bad = []
            for v in ("home", "cote", "guide", "comprendre", "lieu", "specialite"):
                page.evaluate(NAV, [v, None]); page.wait_for_timeout(80)
                r = page.evaluate(CHECK)
                if r["over"] or r["bad"]: bad.append((v, r))
            for fid in ["x", "ens", "mp", "mt", "cs", "inp", "poly", "e3a", "autres"]:
                page.evaluate(NAV, ["famille", fid]); page.wait_for_timeout(80)
                for inp in page.query_selector_all("input[data-rank]"):
                    inp.fill("800")
                page.wait_for_timeout(80)
                r = page.evaluate(CHECK)
                if r["over"] or r["bad"]: bad.append(("fam-" + fid, r))
            nfiche = nvoie = 0
            for sid in ids:
                page.evaluate(NAV, ["ecole", sid])
                r = page.evaluate(CHECK)
                if "Pas de voie" in page.inner_text("#view"): nvoie += 1
                else: nfiche += 1
                if r["over"] or r["bad"]: bad.append((sid, r))
            print(w, fil, "|", title, "| fiches:", nfiche, "pas de voie:", nvoie, "| problèmes:", bad[:6])
            if w == 1280 or w == 390:
                page.evaluate(NAV, ["famille", "inp"]); page.wait_for_timeout(150)
                page.screenshot(path=D + f"tests/screens/{w}-{fil}-inp.png", full_page=True)
                page.evaluate(NAV, ["ecole", "chimieparistech"]); page.wait_for_timeout(150)
                page.screenshot(path=D + f"tests/screens/{w}-{fil}-chimie.png", full_page=True)
                page.evaluate(NAV, ["home", None]); page.wait_for_timeout(150)
                page.screenshot(path=D + f"tests/screens/{w}-{fil}-home.png")
    br.close()
print("errors:", errs[:6])
