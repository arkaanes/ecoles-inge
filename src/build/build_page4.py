# -*- coding: utf-8 -*-
"""Inject data.json and map.json into template4.html -> ecoles-mp.html (+ local preview with the publish skeleton)."""
import json
tpl = open("template4.html", encoding="utf-8").read()
def blob(path):
    d = json.load(open(path, encoding="utf-8"))
    return json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "\\u003c!--")
assert tpl.count("/*__DATA__*/") == 1 and tpl.count("/*__MAP__*/") == 1
page = tpl.replace("/*__DATA__*/", blob("data.json")).replace("/*__MAP__*/", blob("../geo/out/map.json"))
open("ecoles.html", "w", encoding="utf-8").write(page)
skeleton = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
            'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
open("preview.html", "w", encoding="utf-8").write(skeleton + page + "</body></html>")
print("ecoles.html", round(len(page.encode("utf-8")) / 1024), "KB")
