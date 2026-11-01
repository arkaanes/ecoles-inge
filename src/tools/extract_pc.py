# Génère build/data_pc.py à partir des données de la version MP-PC (filière PC uniquement).
import json, re, sys, pprint
pc = json.load(open(sys.argv[1], encoding="utf-8"))
mp_html = open(sys.argv[2], encoding="utf-8").read()
mp = json.loads(re.search(r'<script type="application/json" id="data">(.*?)</script>', mp_html, re.S).group(1))
mpids = {e["id"] for e in mp["ecoles"]}
DERIVED = ("regs", "idf", "grp")
def strip_f(a):
    return {k: v for k, v in a.items() if k != "f"}
pc_acces, new_schools, fil_over = {}, [], {}
for e in pc["ecoles"]:
    acc = [strip_f(a) for a in e["acces"] if a["f"] == "PC"]
    over = {k: e[k] for k in ("domF", "descF", "noteF") if k in e}
    if over: fil_over[e["id"]] = over
    if e["id"] in mpids:
        if acc: pc_acces[e["id"]] = acc
    else:
        s = {k: v for k, v in e.items() if k not in DERIVED and k not in ("domF", "descF", "noteF")}
        s["acces"] = acc
        new_schools.append(s)
conc_pc = {c["id"]: c["PC"] for c in pc["concours"] if "PC" in c}
conc_extra = [c for c in pc["concours"] if c.get("seul")]
fil = pc["parFil"]["PC"]
def dump(name, obj, doc):
    return f"# {doc}\n{name} = " + pprint.pformat(obj, width=160, sort_dicts=False) + "\n\n"
out = ['# -*- coding: utf-8 -*-\n"""Filière PC : voies d\'accès, écoles propres à la PC, variantes des concours et pages concours.\nReprise de la version MP-PC (22 octobre 2026), puis vérifiée."""\n\n']
out.append(dump("PC_ACCES", pc_acces, "Voies d'accès PC des écoles déjà présentes en MP (clé : id de l'école)."))
out.append(dump("PC_SCHOOLS", new_schools, "Écoles qui ne recrutent qu'en PC (dans cet outil)."))
out.append(dump("FIL_OVER", fil_over, "Description, domaines ou note propres à une filière."))
out.append(dump("CONC_PC", conc_pc, "Variantes PC des fiches concours (fusionnées par-dessus la fiche MP)."))
out.append(dump("CONC_EXTRA", conc_extra, "Concours qui n'existent qu'en PC."))
out.append(dump("FIL_PC", fil, "Pages concours, frais, repères, exclusions et sources de la filière PC."))
open(sys.argv[3], "w", encoding="utf-8").write("".join(out))
print(len(pc_acces), "écoles avec voies PC,", len(new_schools), "écoles PC seules,", sum(len(v) for v in pc_acces.values()) + sum(len(s["acces"]) for s in new_schools), "voies PC")
