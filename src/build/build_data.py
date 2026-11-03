# -*- coding: utf-8 -*-
"""Assemble and validate the dataset, write data.json."""
import json, sys
from collections import Counter, defaultdict
from data_common import REGIONS, DOMAINES, src, S_SCEI25, S_FRAIS_SCEI, S_CCMP26, S_CMT26, S_CCS26, S_CCINP26, S_E3A26, S_LOIC, S_NAT, S_HAUSSE26, S_FORUM
from data_part1 import SCHOOLS_1
from data_part2 import SCHOOLS_2
from data_part3 import SCHOOLS_3, SCHOOLS_INSA
from data_part4 import SCHOOLS_POLY, SCHOOLS_IND, SCHOOLS_AV, SCHOOLS_IU, SCHOOLS_OTHER
from data_part5 import SCHOOLS_ENS
from data_concours import GROUPES, CONCOURS, FEES, ECRITS, EXCLUS
from data_partA import FAMILLES, REPERE
from data_pc import PC_ACCES, PC_SCHOOLS, FIL_OVER, CONC_PC, CONC_EXTRA, FIL_PC
from data_psi_acces import PSI_ACCES
from data_psi_fil import FIL_PSI, CONC_PSI, FIL_OVER_PSI
from data_mpi_acces import MPI_ACCES
from data_mpi_fil import FIL_MPI, CONC_MPI, FIL_OVER_MPI

schools = SCHOOLS_1 + SCHOOLS_2 + SCHOOLS_3 + SCHOOLS_INSA + SCHOOLS_POLY + SCHOOLS_IND + SCHOOLS_AV + SCHOOLS_IU + SCHOOLS_OTHER + SCHOOLS_ENS
conc = {c["id"]: c for c in CONCOURS}
errors = []

ids = Counter(s["id"] for s in schools)
for k, n in ids.items():
    if n > 1:
        errors.append(f"duplicate id {k}")

for s in schools:
    for d in s["dom"]:
        if d not in DOMAINES:
            errors.append(f"{s['id']}: unknown domain {d}")
    for c in s["campus"]:
        if c["r"] not in REGIONS:
            errors.append(f"{s['id']}: unknown region {c['r']}")
    if not s["acces"]:
        errors.append(f"{s['id']}: no access")
    for a in s["acces"]:
        if a["c"] not in conc:
            errors.append(f"{s['id']}: unknown concours {a['c']}")
        for f in a["fee"]:
            if f not in FEES:
                errors.append(f"{s['id']}: unknown fee {f}")
        if not a["fee"]:
            errors.append(f"{s['id']}: access without fee keys")
    # derived
    s["regs"] = sorted({c["r"] for c in s["campus"]})
    s["idf"] = "idf" in s["regs"]
    s["grp"] = sorted({conc[a["c"]]["g"] for a in s["acces"]})
    meds = [v["med"] for a in s["acces"] for v in a["stats"] if v.get("med") and not v.get("c25") and not v.get("prev")]
    s["bestMed"] = min(meds) if meds else None
    s["p26"] = sum(a["p26"] or 0 for a in s["acces"])
    s["p26mp"] = sum(a["p26"] or 0 for a in s["acces"] if a["scope"] == "MP")

# ---- consistency checks against published totals
def tot(cid, scope=None):
    return sum((a["p26"] or 0) for s in schools for a in s["acces"] if a["c"] == cid and (scope is None or a["scope"] == scope))

checks = {
    "CCMP 2026 (579 attendu)": (tot("ccmp"), 579),
    "CMT 2026 hors IMT-BS (827-15=812 attendu)": (tot("cmt"), 812),
    "CCINP 2026 (1079 attendu)": (tot("ccinp"), 1079),
    "Polytech MP/PC/PSI 2026 (793 attendu)": (tot("e3a_poly"), 793),
    "Avenir MP 2026 hors Casablanca (154-1=153 attendu)": (tot("avenir"), 153),
    "Ingéni'Up 2026 (145 attendu)": (tot("ingeniup"), 145),
}
for k, (got, exp) in checks.items():
    print(("OK  " if got == exp else "DIFF") + f" {k}: {got}")
    if got != exp:
        errors.append(f"total mismatch {k}: {got} vs {exp}")

# e3a independents: sum of MP places listed by L'Étudiant (23 écoles)
ind_mp = tot("e3a_ind")
print("e3a indépendantes MP 2026 (somme):", ind_mp)

# 2025 CCINP MP places by line should sum to 1213 incl. ENAC/ENSMA lines now under CMT
ccinp25 = sum(v["pl"] for s in schools for a in s["acces"] for v in a["stats"]
              if (a["c"] == "ccinp" and not v.get("c25")) or v.get("c25") == "CCINP")
print("CCINP 2025 lignes MP (1213 attendu):", ccinp25)
if ccinp25 != 1213:
    errors.append(f"CCINP 2025 places {ccinp25} != 1213")

cmt25 = sum(v["pl"] for s in schools for a in s["acces"] for v in a["stats"] if a["c"] == "cmt" and not v.get("c25"))
print("CMT 2025 lignes MP hors IMT-BS (780-15=765 attendu):", cmt25)
ccmp25 = sum(v["pl"] for s in schools for a in s["acces"] for v in a["stats"] if a["c"] == "ccmp")
print("CCMP 2025 lignes MP (570 attendu):", ccmp25)

print("Écoles:", len(schools), "| voies:", sum(len(s["acces"]) for s in schools))
print("Par région:", dict(Counter(r for s in schools for r in s["regs"])))
print("Frais non trouvés:", [s["id"] for s in schools if s["frais"]["min"] is None and s["frais"]["ref"] is None])
print("Boursiers à vérifier:", [s["id"] for s in schools if s["bours"]["cat"] == "nd" and not s["statut"].startswith("Privé")])

if errors:
    print("\nERRORS:")
    for e in errors:
        print(" -", e)

S_CAL26 = src("Calendrier SCEI 2026 (L'Étudiant, mis à jour le 7 novembre 2025)",
              "https://www.letudiant.fr/etudes/classes-prepa/ecoles-d-ingenieurs-comment-se-passe-la-procedure-d-inscription.html")
S_CAL = src("Calendrier officiel du SCEI", "https://www.scei-concours.fr/calendrier.html")
S_ENS_NOTICE = src("Notice inter-ENS 2026", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/notice_interens_2026_mise_en_ligne_vf260212.pdf")
S_MAP = src("Contours des régions : IGN Admin Express (Licence ouverte), via france-geojson", "https://github.com/gregoiredavid/france-geojson")
SOURCES = [S_SCEI25, S_FRAIS_SCEI, S_CCMP26, S_CMT26, S_CCS26, S_CCINP26, S_E3A26, S_ENS_NOTICE, S_LOIC, S_NAT, S_HAUSSE26, S_CAL26, S_MAP]
# ---- partie A : contrôle des épreuves (coefficients numériques, totaux annoncés)
def coefs(lignes):
    return sum(float(l[2].replace(",", ".")) for l in lignes if l[2])
for fid, fam in FAMILLES.items():
    for b in fam["blocs"]:
        for part in ("ecrits", "oraux"):
            for l in (b.get(part) or {}).get("l", []):
                if len(l) not in (3, 4) or (l[2] and not l[2].replace(",", "").isdigit()):
                    errors.append(f"{fid}: ligne d'épreuve mal formée {l}")
expected = {"mp": (30, 39), "mt": (30, 30), "cs": (100, 100), "inp": (60, 40), "poly": (34, 8)}
for fid, (e, o) in expected.items():
    b = FAMILLES[fid]["blocs"][0]
    got = (coefs(b["ecrits"]["l"]), coefs(b["oraux"]["l"]))
    print(("OK  " if got == (e, o) else "DIFF") + f" coefficients {fid}: écrits {got[0]:g}, oraux {got[1]:g}")
    if got != (e, o):
        errors.append(f"coefficients {fid}: {got} vs {(e, o)}")
bx = FAMILLES["x"]["blocs"][0]
print("X : oraux", coefs(bx["oraux"]["l"]), "(92 + sport 5 attendus)")

# ---- filière PC : fusion (chaque voie d'accès porte sa filière dans "f")
MAJ_MP = "2026-10-22"
for s_ in schools:
    for k in ("bestMed", "p26", "p26mp"):
        s_.pop(k, None)
    for a in s_["acces"]:
        a["f"] = "MP"
by = {s_["id"]: s_ for s_ in schools}
for sid, acc in PC_ACCES.items():
    if sid not in by:
        errors.append(f"PC: école inconnue {sid}")
        continue
    by[sid]["acces"] += [dict(a, f="PC") for a in acc]
for s_ in PC_SCHOOLS:
    if s_["id"] in by:
        errors.append(f"PC: doublon {s_['id']}")
    s_ = dict(s_, acces=[dict(a, f="PC") for a in s_["acces"]])
    s_["regs"] = sorted({c["r"] for c in s_["campus"]})
    s_["idf"] = "idf" in s_["regs"]
    schools.append(s_)
    by[s_["id"]] = s_
# ---- filière PSI
for sid, acc in PSI_ACCES.items():
    if sid not in by:
        errors.append(f"PSI: école inconnue {sid}")
        continue
    by[sid]["acces"] += [dict(a, f="PSI") for a in acc]
# ---- filière MPI
for sid, acc in MPI_ACCES.items():
    if sid not in by:
        errors.append(f"MPI: école inconnue {sid}")
        continue
    by[sid]["acces"] += [dict(a, f="MPI") for a in acc]
# Ingéni'Up : concours interfilière, mêmes lignes SCEI dans toutes les filières -> on reprend celles de la MP
import copy
for s_ in schools:
    mp_iu = [a for a in s_["acces"] if a["c"] == "ingeniup" and a["f"] == "MP"]
    for a in s_["acces"]:
        if a["c"] == "ingeniup" and a["f"] != "MP":
            m = next((x for x in mp_iu if x.get("lib") == a.get("lib")), None)
            if m is None:
                errors.append(f"Ingéni'Up {s_['id']} {a['f']}: pas de voie MP correspondante")
                continue
            a["stats"] = copy.deepcopy(m["stats"])
            if m.get("note"): a["note"] = m["note"]
            else: a.pop("note", None)
# variantes par filière (descF, domF, noteF) : fusion clé par clé
for overs in (FIL_OVER, FIL_OVER_PSI, FIL_OVER_MPI):
    for sid, over in overs.items():
        for k, v in over.items():
            by[sid][k] = dict(by[sid].get(k) or {}, **v)
all_conc = {c["id"]: c for c in CONCOURS + CONC_EXTRA}
for cid, over in CONC_PC.items():
    all_conc[cid] = dict(all_conc[cid], PC=over)
for cid, over in CONC_PSI.items():
    all_conc[cid] = dict(all_conc[cid], PSI=over)
for cid, over in CONC_MPI.items():
    all_conc[cid] = dict(all_conc[cid], MPI=over)
for s_ in schools:
    s_["grp"] = sorted({all_conc[a["c"]]["g"] for a in s_["acces"]})
    for d in s_["dom"] + [d for v in (s_.get("domF") or {}).values() for d in v]:
        if d not in DOMAINES:
            errors.append(f"{s_['id']}: domaine inconnu {d}")
    for a in s_["acces"]:
        if a["c"] not in all_conc:
            errors.append(f"{s_['id']}: concours inconnu {a['c']}")
        fees = {"MP": FEES, "PC": FIL_PC["fees"], "PSI": FIL_PSI["fees"], "MPI": FIL_MPI["fees"]}[a["f"]]
        for f in a["fee"]:
            if f not in fees:
                errors.append(f"{s_['id']} ({a['f']}): frais inconnus {f}")

def totf(cid, fil):
    return sum((a["p26"] or 0) for s_ in schools for a in s_["acces"] if a["c"] == cid and a["f"] == fil)
mp_checks = {  # places MP 2026 publiées (hors places étrangers et Casablanca)
    "Centrale-Supélec MP 2026 (1053, tableau L'Étudiant ; ESTP recoupé avec Onisep, 506 places au total)": ("ccs", 1053),
}
for k, (cid, exp) in mp_checks.items():
    got = totf(cid, "MP")
    print(("OK  " if got == exp else "DIFF") + f" {k}: {got}")
    if got != exp:
        errors.append(f"MP total {k}: {got}")
pc_checks = {  # places PC 2026 publiées (hors places étrangers, hors campus à l'étranger, hors IMT-BS et contrôleurs aériens)
    "Mines-Ponts PC 2026 (417, notice des écoles)": ("ccmp", 417),
    "Mines-Télécom PC 2026 (453 - IMT-BS 9 = 444)": ("cmt", 444),
    "Centrale-Supélec PC 2026 (784 - étrangers et Casablanca 19 = 765)": ("ccs", 765),
    "CCINP PC-Physique 2026 (555)": ("ccinp", 555),
    "CCINP PC-Chimie 2026 (638)": ("ccinp_chi", 638),
    "Polytech MP/PC/PSI 2026 (793)": ("e3a_poly", 793),
    "Avenir PC 2026 (96 - Casablanca 1 = 95, L'Étudiant)": ("avenir", 95),
    "Banque CCINP PC 2026 (133 PH + 71 CH - ENAC contrôleurs 39 + 3 écoles interfilières 124 = 289)": ("bccinp", 289),
    "Ingéni'Up 2026 (145)": ("ingeniup", 145),
}
for k, (cid, exp) in pc_checks.items():
    got = totf(cid, "PC")
    print(("OK  " if got == exp else "DIFF") + f" {k}: {got}")
    if got != exp:
        errors.append(f"PC total {k}: {got}")
psi_checks = {  # places PSI 2026 publiées (hors places étrangers, hors campus à l'étranger, hors IMT-BS et contrôleurs aériens)
    "X PSI 2026 (56, Onisep)": ("x", 56),
    "Mines-Ponts PSI 2026 (471, notice des écoles)": ("ccmp", 471),
    "Mines-Télécom PSI 2026 (600 - IMT-BS 6 = 594)": ("cmt", 594),
    "Centrale-Supélec PSI 2026 (1172 - étrangers, Casablanca, cycle international 27 = 1145)": ("ccs", 1145),
    "CCINP PSI 2026 (750)": ("ccinp", 750),
    "Banque CCINP PSI 2026 (224 - ENAC contrôleurs 54 + 3 écoles interfilières 124 = 294)": ("bccinp", 294),
    "Polytech MP/PC/PSI 2026 (793)": ("e3a_poly", 793),
    "e3a indépendantes PSI 2026 (446, dont 254 INTER)": ("e3a_ind", 446),
    "Avenir PSI 2026 (176 - Casablanca 1 = 175)": ("avenir", 175),
    "Ingéni'Up 2026 (145)": ("ingeniup", 145),
}
for k, (cid, exp) in psi_checks.items():
    got = totf(cid, "PSI")
    print(("OK  " if got == exp else "DIFF") + f" {k}: {got}")
    if got != exp:
        errors.append(f"PSI total {k}: {got}")
for fid, fam in FIL_PSI["familles"].items():
    for b in fam["blocs"]:
        for part in ("ecrits", "oraux"):
            for l in (b.get(part) or {}).get("l", []):
                if len(l) not in (3, 4) or (l[2] and not l[2].isdigit()):
                    errors.append(f"PSI {fid}: ligne d'épreuve mal formée {l}")
psi_coefs = {"x": (43, 68), "mp": (30, 41), "mt": (30, 30), "cs": (100, 100), "inp": (60, 40), "poly": (34, 8)}
for fid, (e, o) in psi_coefs.items():
    b = FIL_PSI["familles"][fid]["blocs"][0]
    got = (coefs(b["ecrits"]["l"]), coefs(b["oraux"]["l"]))
    print(("OK  " if got == (e, o) else "DIFF") + f" coefficients PSI {fid}: écrits {got[0]:g}, oraux {got[1]:g}")
    if got != (e, o):
        errors.append(f"coefficients PSI {fid}: {got} vs {(e, o)}")
mpi_checks = {  # places MPI 2026 publiées (hors campus à l'étranger et contrôleurs aériens)
    "X MPI 2026 (22, Onisep)": ("x", 22),
    "Mines-Ponts MPI 2026 (143)": ("ccmp", 143),
    "Mines-Télécom MPI 2026 (207)": ("cmt", 207),
    "Centrale-Supélec MPI 2026 (160 - Casablanca 2 = 158)": ("ccs", 158),
    "CCINP MPI 2026 (212)": ("ccinp", 212),
    "Banque CCINP MPI 2026 (49 - ENAC contrôleurs 3 + 2 écoles interfilières 114 = 160)": ("bccinp", 160),
    "Polytech MPI 2026 (99, liste à part)": ("e3a_poly", 99),
    "e3a indépendantes MPI 2026 (86 + 254 INTER = 340)": ("e3a_ind", 340),
    "Avenir MPI 2026 (27 - Casablanca 1 = 26)": ("avenir", 26),
    "Ingéni'Up 2026 (145)": ("ingeniup", 145),
}
for k, (cid, exp) in mpi_checks.items():
    got = totf(cid, "MPI")
    print(("OK  " if got == exp else "DIFF") + f" {k}: {got}")
    if got != exp:
        errors.append(f"MPI total {k}: {got}")
for fid, fam in FIL_MPI["familles"].items():
    for b in fam["blocs"]:
        for part in ("ecrits", "oraux"):
            for l in (b.get(part) or {}).get("l", []):
                if len(l) not in (3, 4) or (l[2] and not l[2].isdigit()):
                    errors.append(f"MPI {fid}: ligne d'épreuve mal formée {l}")
mpi_coefs = {"x": (39, 101), "mp": (30, 41), "mt": (30, 30), "cs": (100, 100), "inp": (60, 40), "poly": (34, 8)}
for fid, (e, o) in mpi_coefs.items():
    b = FIL_MPI["familles"][fid]["blocs"][0]
    got = (coefs(b["ecrits"]["l"]), coefs(b["oraux"]["l"]))
    print(("OK  " if got == (e, o) else "DIFF") + f" coefficients MPI {fid}: écrits {got[0]:g}, oraux {got[1]:g}")
    if got != (e, o):
        errors.append(f"coefficients MPI {fid}: {got} vs {(e, o)}")
print("Écoles MPI :", sum(1 for s_ in schools if any(a["f"] == "MPI" for a in s_["acces"])))
print("Écoles PSI :", sum(1 for s_ in schools if any(a["f"] == "PSI" for a in s_["acces"])))
print("Écoles PC :", sum(1 for s_ in schools if any(a["f"] == "PC" for a in s_["acces"])), "| écoles MP :", sum(1 for s_ in schools if any(a["f"] == "MP" for a in s_["acces"])))
for fid, fam in FIL_PC["familles"].items():
    for b in fam["blocs"]:
        for part in ("ecrits", "oraux"):
            for l in (b.get(part) or {}).get("l", []):
                if len(l) not in (3, 4) or (l[2] and not l[2].replace(" / ", "").replace(",", "").isdigit()):
                    errors.append(f"PC {fid}: ligne d'épreuve mal formée {l}")
from data_annales import ANNALES
FIL_FAMS = {"MP": FAMILLES, "PC": FIL_PC["familles"], "PSI": FIL_PSI["familles"], "MPI": FIL_MPI["familles"]}
n_ann = 0
for fil, fams in ANNALES.items():
    for fid, ann in fams.items():
        fam = FIL_FAMS[fil].get(fid)
        if not fam:
            errors.append(f"annales {fil} {fid}: famille inconnue")
            continue
        for part in ("e", "o"):
            noms = {l[0] for b in fam["blocs"] for l in (b.get({"e": "ecrits", "o": "oraux"}[part]) or {}).get("l", [])}
            for nom, items in ann[part].items():
                n_ann += len(items)
                if nom not in noms:
                    errors.append(f"annales {fil} {fid}: épreuve « {nom} » absente des lignes")
                for it in items:
                    if len(it) != 3 or not isinstance(it[1], int) or not it[2].startswith("https://"):
                        errors.append(f"annales {fil} {fid}: lien mal formé {it}")
        fam["annales"] = ann
print("Annales :", n_ann, "liens d'épreuves")
if errors:
    print("\nERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

data = {"regions": REGIONS, "domaines": DOMAINES, "groupes": GROUPES,
        "concours": list(all_conc.values()), "ecoles": schools, "cal": {"src": S_CAL26, "off": S_CAL},
        "parFil": {"MP": {"familles": FAMILLES, "fees": FEES, "repere": REPERE, "exclus": EXCLUS, "sources": SOURCES, "maj": MAJ_MP},
                   "PC": FIL_PC, "PSI": FIL_PSI, "MPI": FIL_MPI}}
out = sys.argv[1] if len(sys.argv) > 1 else "data.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
print("written", out, round(len(json.dumps(data, ensure_ascii=False)) / 1024), "KB")
