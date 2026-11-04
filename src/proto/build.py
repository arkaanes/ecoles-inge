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
# Prototype v2 (nouvelles fonctions), isolé des pages de vote : prototype/v2/, données de prototype/.
LABO = os.path.join(HERE, "..", "labo")
os.makedirs(os.path.join(OUT, "v2"), exist_ok=True)
for f in ("index.html", "app.css", "app.js"):
    shutil.copyfile(os.path.join(LABO, f), os.path.join(OUT, "v2", f))
def mini(src, dst):
    d = json.load(open(src, encoding="utf-8"))
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, separators=(",", ":"))
    return os.path.getsize(dst)
n1 = mini(os.path.join(HERE, "..", "build", "data.json"), os.path.join(OUT, "data.json"))
n2 = mini(os.path.join(HERE, "..", "geo", "out", "map.json"), os.path.join(OUT, "map.json"))
print("prototype/ (+ b/, mix/) :", round(n1 / 1024), "Ko de données,", round(n2 / 1024), "Ko de carte")

# Site principal (index.html à la racine) : l'interface v2 avec l'habillage « actuel ».
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SITE = os.path.join(ROOT, "site")
os.makedirs(SITE, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "app.css"), os.path.join(SITE, "base.css"))
shutil.copyfile(os.path.join(LABO, "app.css"), os.path.join(SITE, "v2.css"))
shutil.copyfile(os.path.join(LABO, "theme-actuel.css"), os.path.join(SITE, "theme.css"))
shutil.copyfile(os.path.join(LABO, "theme-neutre.css"), os.path.join(SITE, "theme-neutre.css"))
shutil.copyfile(os.path.join(LABO, "app.js"), os.path.join(SITE, "app.js"))
shutil.copyfile(os.path.join(OUT, "data.json"), os.path.join(SITE, "data.json"))
shutil.copyfile(os.path.join(OUT, "map.json"), os.path.join(SITE, "map.json"))
lab = open(os.path.join(LABO, "index.html"), encoding="utf-8").read()
i0 = lab.index('<link rel="stylesheet" href="../app.css">'); i1 = lab.index("</script>", i0) + len("</script>")
FONT = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap"
head = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="%s">\n<link rel="stylesheet" href="site/base.css">\n<link rel="stylesheet" href="site/v2.css">\n'
        '<link rel="stylesheet" href="site/theme.css" id="st-actuel">\n<link rel="stylesheet" href="site/theme-neutre.css" id="st-neutre">\n'
        # style choisi (bouton Aa) : appliqué avant le premier affichage ; « actuel » par défaut
        '<script>\n(function () {\n  var s = "actuel";\n  try { if (localStorage.getItem("ecoles-style") === "neutre") s = "neutre"; } catch (e) { /* rien */ }\n'
        '  document.documentElement.setAttribute("data-style", s);\n  document.getElementById(s === "actuel" ? "st-neutre" : "st-actuel").media = "not all";\n'
        '  if (s === "neutre") { document.getElementById("tc-l").setAttribute("content", "#FFFFFF"); document.getElementById("tc-d").setAttribute("content", "#0F1115"); }\n'
        '})();\n</script>' % FONT.replace("&", "&amp;"))
main = lab[:i0] + head + lab[i1:]
main = main.replace('<script src="app.js" data-base="../" defer></script>', '<script src="site/app.js" data-base="site/" defer></script>')
main = main.replace('<meta name="theme-color" content="#FFFFFF">', '<meta name="theme-color" id="tc-l" content="#FAF7F2" media="(prefers-color-scheme: light)"><meta name="theme-color" id="tc-d" content="#1F1813" media="(prefers-color-scheme: dark)">')
assert "../" not in main and 'data-base="site/"' in main
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(main)
print("site principal : index.html + site/")
