# -*- coding: utf-8 -*-
"""Inject data.json and map.json into template4.html -> ecoles.html (page publiée) et preview.html (identique, pour les tests)."""
import json
tpl = open("template4.html", encoding="utf-8").read()
def blob(path):
    d = json.load(open(path, encoding="utf-8"))
    return json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "\\u003c!--")
assert tpl.count("/*__DATA__*/") == 1 and tpl.count("/*__MAP__*/") == 1
page = tpl.replace("/*__DATA__*/", blob("data.json")).replace("/*__MAP__*/", blob("../geo/out/map.json"))
# Squelette complet (doctype + viewport) : sans lui, un téléphone affiche la page à 980 px de large, dézoomée.
skeleton = ('<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
            'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
full = skeleton + page + "</body></html>"
open("ecoles.html", "w", encoding="utf-8").write(full)
open("preview.html", "w", encoding="utf-8").write(full)
print("ecoles.html", round(len(page.encode("utf-8")) / 1024), "KB")
