# -*- coding: utf-8 -*-
"""Prototype : copie l'interface (index.html, app.css, app.js) et les données dans ../../prototype/.
À lancer après build_data.py (qui produit ../build/data.json)."""
import json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "prototype"))
os.makedirs(OUT, exist_ok=True)
for f in ("index.html", "app.css", "app.js"):
    shutil.copyfile(os.path.join(HERE, f), os.path.join(OUT, f))
def mini(src, dst):
    d = json.load(open(src, encoding="utf-8"))
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, separators=(",", ":"))
    return os.path.getsize(dst)
n1 = mini(os.path.join(HERE, "..", "build", "data.json"), os.path.join(OUT, "data.json"))
n2 = mini(os.path.join(HERE, "..", "geo", "out", "map.json"), os.path.join(OUT, "map.json"))
print("prototype/ :", round(n1 / 1024), "Ko de données,", round(n2 / 1024), "Ko de carte")
