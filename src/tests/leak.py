from playwright.sync_api import sync_playwright
import json, re, collections
import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
data = json.load(open(D + "build/data.json"))
ids = [s["id"] for s in data["ecoles"]]
NAV = """([go, arg]) => { const b = document.createElement('button'); b.dataset.go = go; if (arg) b.dataset.arg = arg; b.hidden = true; document.body.appendChild(b); b.click(); b.remove(); }"""
TOK = re.compile(r"\b(MPI|MP|PC|PSI)\b")
out = {}
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 1280, "height": 900})
    pg.route("**/fonts.g*/**", lambda r: r.abort())
    pg.goto("file://" + D + "build/preview.html"); pg.wait_for_timeout(300)
    for fil in ("MP", "PC", "PSI", "MPI"):
        pg.evaluate("f => document.querySelector('.filsw [data-fil=\"' + f + '\"]').click()", fil); pg.wait_for_timeout(200)
        sents = collections.Counter()
        views = [("home", None), ("cote", None), ("guide", None), ("comprendre", None), ("lieu", None), ("specialite", None)] + \
                [("famille", f) for f in ["x", "ens", "mp", "mt", "cs", "inp", "poly", "e3a", "autres"]] + [("ecole", i) for i in ids]
        for go, arg in views:
            pg.evaluate(NAV, [go, arg])
            # ouvrir les « Bon à savoir »
            pg.evaluate("() => document.querySelectorAll('#view details').forEach(d => d.open = true)")
            txt = pg.inner_text("#view")
            for line in txt.split("\n"):
                for s in re.split(r"(?<=[.!?])\s+", line):
                    toks = set(TOK.findall(s))
                    if toks - {fil}:
                        sents[s.strip()[:220]] += 1
        out[fil] = sents
    br.close()
for fil, c in out.items():
    print("=" * 30, fil, len(c))
    for s, n in sorted(c.items(), key=lambda x: -x[1]):
        print(f"{n:4d} | {s}")
