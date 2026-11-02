# -*- coding: utf-8 -*-
"""Prototype : trois habillages d'une même interface, dans ../../prototype/.
  prototype/      neutre
  prototype/b/    « l'énoncé » (maquette B)
  prototype/mix/  maquette B + couleurs du site actuel
À lancer après build_data.py (qui produit ../build/data.json)."""
import json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "prototype"))
FONTS = {
    "b": "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&display=swap",
    "mix": "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;1,6..72,400&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap",
}
tpl = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()
def page(theme):
    base = "" if theme is None else "../"
    head = '<link rel="stylesheet" href="%sapp.css">' % base
    if theme:
        head = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                '<link rel="stylesheet" href="%s">' % FONTS[theme].replace("&", "&amp;")) + head + '<link rel="stylesheet" href="theme.css">'
    return (tpl.replace("{{THEME_ATTR}}", ' data-theme="%s"' % theme if theme else "")
               .replace("{{HEAD}}", head).replace("{{BASE}}", base))
os.makedirs(OUT, exist_ok=True)
for f in ("app.css", "app.js"):
    shutil.copyfile(os.path.join(HERE, f), os.path.join(OUT, f))
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page(None))
for t in ("b", "mix"):
    os.makedirs(os.path.join(OUT, t), exist_ok=True)
    open(os.path.join(OUT, t, "index.html"), "w", encoding="utf-8").write(page(t))
    shutil.copyfile(os.path.join(HERE, "theme-%s.css" % t), os.path.join(OUT, t, "theme.css"))
def mini(src, dst):
    d = json.load(open(src, encoding="utf-8"))
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, separators=(",", ":"))
    return os.path.getsize(dst)
n1 = mini(os.path.join(HERE, "..", "build", "data.json"), os.path.join(OUT, "data.json"))
n2 = mini(os.path.join(HERE, "..", "geo", "out", "map.json"), os.path.join(OUT, "map.json"))
print("prototype/ (+ b/, mix/) :", round(n1 / 1024), "Ko de données,", round(n2 / 1024), "Ko de carte")
