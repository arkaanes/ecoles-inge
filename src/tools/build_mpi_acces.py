# -*- coding: utf-8 -*-
"""Voies d'accès MPI 2026 (places) + statistiques SCEI MPI 2025, école par école."""
import sys, json, os, re, pprint
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "build"))
import scei_mpi
from scei_mpi import row
from data_pc import PC_ACCES

def src(t, u): return {"t": t, "u": u}
S_X = src("Fiche Onisep (places 2026 par filière)", "https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/essonne/ecole-polytechnique-institut-polytechnique-de-paris-etablissement-experimental/diplome-d-ingenieur-de-l-ecole-polytechnique-institut-polytechnique-de-paris")
S_ENS = src("Notice inter-ENS 2026 (banque MPI)", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/notice_interens_2026_mise_en_ligne_vf260212.pdf")
S_ENS_SACLAY = src("ENS Paris-Saclay : postes d'élèves ouverts en 2026", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_postes_eleves_ouverts_ENS_Paris-Saclay.pdf")
S_ENS_ULM = src("ENS Ulm : décision du 8 décembre 2025 sur les postes 2026", "https://www.ens.psl.eu/sites/default/files/decision_fixant_le_nombre_de_postes_ouverts_aux_concours_ens_ulm_session_2026_signe.pdf")
S_CCMP = src("Notice des écoles Mines-Ponts 2026", "https://concoursminesponts.fr/wp-content/uploads/2025/12/notice-des-ecoles-2026-22.12.25.pdf")
S_CMT = src("Notice Mines-Télécom 2026", "https://cahier-de-prepa.fr/pc-descartes/download?id=260")
S_CCS = src("Notice Centrale-Supélec 2026, filière MPI", "https://www.concours-centrale-supelec.fr/sites/default/files/documents/CCS_2026_MPI.pdf")
S_INP = src("Places MPI 2026 (site du CCINP)", "https://www.concours-commun-inp.fr/fr/les-ecoles/les-places-dans-les-ecoles/places-mpi.html")
S_E3A = src("Notice 2026 de la banque e3a-Polytech", "https://esigelec.fr/sites/default/files/2025-12/VF-Notice-2026-Banque-e3a-Polytech.pdf")

NOTE_ENS = ("Les classés et intégrés ne comptent que les candidats « fonctionnarisables » (note du SCEI). "
            "Chaque ENS a sa propre liste de classement.")
NOTE_PA = "En 2025, l'école recrutait via Puissance Alpha (places toutes filières) : rangs non comparables à ceux d'e3a-Polytech."
NOTE_INTER = "Places communes à toutes les filières (liste « INTER » de la notice e3a-Polytech)."
INS = {"PA": 169, "AV": 165, "EP": 179}
INS_AE = {"EIJV": 115, "EIL": 50}

def V(sec, name, lib, **extra):
    r = row(sec, name)
    d = {"lib": lib, "pl": r["pl"], "int": r["int"], "med": r["med"] or None, "moy": r["moy"] or None}
    if sec in ("PA", "AV", "EP", "EI", "AE"):
        ins = INS.get(sec) or next((v for k, v in INS_AE.items() if name.startswith(k)), None)
        if ins: d["ins"] = ins
    elif r["cl"]:
        d["cl"] = r["cl"]
    if sec in ("BI", "INSA", "PA") and r.get("iint") is not None:
        d["inter"] = True
        if sec != "PA":
            d["iint"] = r["iint"]
    if sec == "EI":
        d["inter"] = True
    if r["int"] == 0 and not d.get("inter"):   # liste propre à la filière : pas d'admis, pas de rang
        d["med"] = d["moy"] = None
    d.update(extra)
    return d

def A(c, p26, stats, fee, s, scope="MPI", lib=None, txt=None, note=None):
    d = {"c": c, "p26": p26, "scope": scope, "stats": stats, "fee": fee, "src": s}
    if lib: d["lib"] = lib
    if txt: d["txt"] = txt
    if note: d["note"] = note
    return d

ACC = {}
def add(sid, *acc): ACC.setdefault(sid, []).extend(acc)

# ---------------------------------------------------------------- X, ENS
add("x", A("x", 22, [V("X", "ECOLE POLYTECHNIQUE", "École polytechnique")], ["x"], S_X))
add("ens_ulm", A("ens", 12, [V("X", "ENS Ulm", "ENS Ulm MPI")], ["ens"], S_ENS_ULM, lib="Concours MPI (option maths ou option info)", note=NOTE_ENS))
add("ens_saclay", A("ens", 14, [V("X", "ENS Paris-Saclay", "ENS Paris-Saclay MPI")], ["ens"], S_ENS_SACLAY, lib="Concours MPI (option maths ou option info)", note=NOTE_ENS))
add("ens_lyon", A("ens", None, [V("X", "ENS de Lyon - Math", "ENS de Lyon – mathématiques")], ["ens"], S_ENS, lib="Concours mathématiques (MPI)", txt="4 places en 2025",
                  note="Nombre de postes 2026 non trouvé. " + NOTE_ENS),
                A("ens", None, [V("X", "ENS de Lyon - Info", "ENS de Lyon – informatique")], ["ens"], S_ENS, lib="Concours informatique (MPI)", txt="13 places en 2025"))
add("ens_rennes", A("ens", None, [V("X", "ENS Rennes Info.", "ENS Rennes MPI")], ["ens"], S_ENS, lib="Concours MPI (département informatique)", txt="7 places en 2025",
                    note="Nombre de postes 2026 non trouvé. " + NOTE_ENS))

# ---------------------------------------------------------------- Mines-Ponts
F = ["ccmp"]
add("minesparis", A("ccmp", 5, [V("MPo", "MINES Paris", "Mines Paris")], F, S_CCMP))
add("ponts", A("ccmp", 5, [V("MPo", "Ecole Nationale des Ponts et Chaussées", "École des Ponts")], F, S_CCMP))
add("telecomparis", A("ccmp", 46, [V("MPo", "TELECOM Paris", "Statut étudiant"), V("MPo", "TELECOM Paris - Apprentissage", "Apprentissage")], F, S_CCMP,
                      txt="45 en statut étudiant + 1 en apprentissage"))
add("ensta", A("ccmp", 15, [V("MPo", "ENSTA Paris", "ENSTA Paris (statut étudiant)"), V("MPo", "ENSTA Paris - apprentissage", "ENSTA Paris – apprentissage")], F, S_CCMP,
               lib="Campus Paris-Saclay (Palaiseau)", txt="14 en statut étudiant + 1 en apprentissage", note="Pas de places MPI sur le campus de Brest en 2026."))
add("ensae", A("ccmp", 10, [V("MPo", "ENSAE Paris", "ENSAE Paris")], F, S_CCMP))
add("supaero", A("ccmp", 10, [V("MPo", "ISAE - SUPAERO Toulouse", "ISAE-SUPAERO")], F, S_CCMP))
add("minesnancy", A("ccmp", 12, [V("MPo", "MINES de NANCY", "Mines Nancy")], F, S_CCMP))
add("minesse", A("ccmp", 20, [V("MPo", "MINES SAINT-ETIENNE", "Mines Saint-Étienne")], F, S_CCMP))
add("imtatlantique", A("ccmp", 20, [V("MPo", "IMT Atlantique", "IMT Atlantique")], F, S_CCMP))

# ---------------------------------------------------------------- Mines-Télécom
F = ["cmt"]
add("enm", A("cmt", 2, [V("MT", "ECOLE METEOROLOGIE (fonctionnaire)", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (rémunérés)"))
add("enac", A("cmt", 9, [V("INP", "ENAC Toulouse Civil", "Civils (via CCINP en 2025)", c25="CCINP")], F, S_CMT, lib="Ingénieurs civils",
              note="A quitté le CCINP pour Mines-Télécom en 2026 : rangs 2025 = rangs CCINP."),
            A("cmt", 1, [V("INP", "ENAC Toulouse Fonctionnaire", "Fonctionnaires (via CCINP en 2025)", c25="CCINP")], F, S_CMT, lib="Ingénieurs fonctionnaires"))
add("ensiie", A("cmt", 18, [V("MT", "ENSIIE Evry", "ENSIIE")], F, S_CMT))
add("enssat", A("cmt", 16, [V("MT", "ENSSAT Lannion", "ENSSAT")], F, S_CMT))
NOTE_FIDS = next(a["note"] for a in PC_ACCES["ensta"] if a["c"] == "cmt" and a.get("note"))
add("ensta", A("cmt", 4, [V("MT", "ENSTA Bretagne (filière sous statut étudiant)", "ex-ENSTA Bretagne, statut étudiant (2025, pour comparaison)", prev="ex-ENSTA Bretagne")], F, S_CMT,
               lib="FIDS – ingénieur défense et sécurité (statut étudiant)", note=NOTE_FIDS),
             A("cmt", 4, [V("MT", "ENSTA Bretagne (filière sous statut IETA - Direction Générale de l'Armement)", "ex-ENSTA Bretagne, statut IETA (2025, pour comparaison)", prev="ex-ENSTA Bretagne")], F, S_CMT,
               lib="FIDS – statut IETA (militaire, rémunéré)"))
add("entpe", A("cmt", 2, [V("MT", "ENTPE Lyon Civil", "Civils")], F, S_CMT, lib="Élèves civils"),
             A("cmt", 3, [V("MT", "ENTPE Lyon Fonctionnaire", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (rémunérés)"))
add("eurecom", A("cmt", 20, [V("MT", "EURECOM", "EURECOM")], F, S_CMT))
add("geodata", A("cmt", 4, [V("MT", "ENSG-Géomatique Marne la Vallée", "Civils")], F, S_CMT, lib="Élèves civils"),
               A("cmt", 2, [V("MT", "ENSG-Géomatique Marne la Vallée Fonctionnaire", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (agents de l'IGN, rémunérés)"))
add("albi", A("cmt", 4, [V("MT", "IMT Mines Albi", "IMT Mines Albi")], F, S_CMT))
add("ales", A("cmt", 5, [V("MT", "IMT Mines Alès", "IMT Mines Alès")], F, S_CMT))
add("imtne", A("cmt", 5, [V("MT", "IMT Nord Europe", "IMT Nord Europe")], F, S_CMT, lib="Élèves civils"))
add("ensma", A("cmt", 3, [V("INP", "ISAE-ENSMA Poitiers", "ISAE-ENSMA (via CCINP en 2025)", c25="CCINP")], F, S_CMT,
               note="A quitté le CCINP pour Mines-Télécom en 2026 : les rangs 2025 sont des rangs CCINP, pas comparables."))
add("supmeca", A("cmt", 1, [V("MT", "ISAE-Supméca Paris", "ISAE-Supméca")], F, S_CMT))
add("ismin", A("cmt", 5, [V("MT", "Mines Saint Etienne-ISMIN", "Mines Saint-Étienne – ISMIN")], F, S_CMT))
add("telecomnancy", A("cmt", 30, [V("MT", "TELECOM Nancy", "Télécom Nancy")], F, S_CMT))
add("tps", A("cmt", 10, [V("MT", "Télécom Physique Strasbourg Informatique et Réseaux", "Informatique et réseaux")], F, S_CMT, lib="Informatique et réseaux"),
           A("cmt", 4, [], F, S_CMT, lib="Technologies de l'information pour la santé", note="Pas de places MPI en 2025 sur cette formation."))
add("telecomse", A("cmt", 13, [V("MT", "TELECOM St Etienne", "Télécom Saint-Étienne")], F, S_CMT))
add("tsp", A("cmt", 42, [V("MT", "TELECOM SudParis", "Télécom SudParis")], F, S_CMT))

# ---------------------------------------------------------------- Centrale-Supélec
CSL = "CentraleSupélec - "
NO25 = "Pas de places MPI en 2025 sur cette formation."
add("cs",
    A("ccs", 39, [V("CS", CSL + "Ingénieur généraliste - statut étudiant – campus de Paris-Saclay", "Généraliste, Paris-Saclay (statut étudiant)")], ["ccs_cs"], S_CCS, lib="Ingénieur généraliste, Paris-Saclay"),
    A("ccs", 5, [V("CS", CSL + "Ingénieur de spécialité Informatique - campus de Metz", "Spécialité informatique (Metz)")], ["ccs_cs"], S_CCS, lib="Spécialité informatique (Metz)"),
    A("ccs", 5, [V("CS", CSL + "Ingénieur de spécialité Cybersécurité - campus de Rennes", "Spécialité cybersécurité (Rennes)")], ["ccs_cs"], S_CCS, lib="Spécialité cybersécurité (Rennes)"),
    A("ccs", 1, [], ["ccs_cs"], S_CCS, lib="Spécialité génie physique (Metz)", note=NO25),
    A("ccs", 1, [], ["ccs_cs"], S_CCS, lib="Spécialité électronique (Rennes, Paris-Saclay)", note=NO25),
    A("ccs", 1, [], ["ccs_cs"], S_CCS, lib="Spécialité génie électrique (Rennes)", note=NO25),
    A("ccs", 1, [], ["ccs_cs"], S_CCS, lib="Spécialité systèmes numériques (Rennes)", note=NO25))
add("centralelyon", A("ccs", 15, [V("CS", "Centrale Lyon", "Centrale Lyon")], ["ccs_lyon"], S_CCS))
add("centralelille", A("ccs", 10, [V("CS", "Centrale Lille", "Centrale Lille")], ["ccs_lille"], S_CCS),
                     A("ccs", 5, [V("CS", "Centrale Lille - IG2I Lens", "IG2I Lens")], ["ccs_lille"], S_CCS, lib="IG2I, à Lens (spécialité informatique et informatique industrielle)"))
add("centralenantes", A("ccs", 5, [V("CS", "Centrale Nantes", "Centrale Nantes")], ["ccs_nantes"], S_CCS))
add("centralemed", A("ccs", 10, [V("CS", "Centrale Méditerranée", "Centrale Méditerranée")], ["ccs_med"], S_CCS))
add("ensea", A("ccs", 15, [V("CS", "ENSEA Cergy", "ENSEA Cergy")], ["ccs_ensea"], S_CCS))
add("navale", A("ccs", 5, [V("CS", "ECOLE NAVALE Brest", "École navale")], ["ccs_navale"], S_CCS,
                note="Épreuves propres (oraux, sport, aptitude médicale) : rangs sur un petit nombre de classés."))
add("iogs", A("ccs", 8, [V("CS", "Institut d'optique Graduate School (SupOptique)", "SupOptique")], ["ccs_iogs"], S_CCS))
add("epf", A("ccs", 23, [V("CS", "EPF Cachan", "Cachan"), V("CS", "EPF Montpellier", "Montpellier"), V("CS", "EPF Saint Nazaire", "Saint-Nazaire"), V("CS", "EPF Troyes", "Troyes")],
             ["ccs_epf"], S_CCS, txt="Cachan 2 + 2, Troyes 6 + 3, Montpellier 2 + 2, Saint-Nazaire 4 + 2 (le 2e chiffre : apprentissage)"))
add("estp", A("ccs", 9, [V("CS", "ESTP - campus de Cachan", "Cachan"), V("CS", "ESTP - campus de Dijon", "Dijon"), V("CS", "ESTP - campus de d'Orléans", "Orléans"), V("CS", "ESTP - campus de Troyes", "Troyes")],
              ["ccs_estp"], S_CCS, txt="Cachan 3, Troyes 2, Dijon 2, Orléans 2"))

# ---------------------------------------------------------------- CCINP
F = ["ccinp"]
add("ensc", A("ccinp", 5, [V("INP", "Bordeaux INP - ENSC Cognitique", "ENSC")], F, S_INP))
add("enspima", A("ccinp", 1, [V("INP", "Bordeaux INP - ENSPIMA", "ENSPIMA")], F, S_INP))
add("enseirb", A("ccinp", 31, [V("INP", "Bordeaux INP - ENSEIRB-MATMECA Electronique", "Électronique"), V("INP", "Bordeaux INP - ENSEIRB-MATMECA Informatique", "Informatique"),
                               V("INP", "Bordeaux INP - ENSEIRB-MATMECA Mathématiques et Mécanique", "Mathématiques et mécanique"), V("INP", "Bordeaux INP - ENSEIRB-MATMECA Télecom.", "Télécommunications")],
                 F, S_INP, txt="Électronique 2, informatique 18, maths-mécanique 3, télécoms 8"))
add("ensip", A("ccinp", 5, [V("INP", "ENSI Poitiers Energétique et Environnement", "Énergétique et environnement")], F, S_INP))
add("ensicaen", A("ccinp", 7, [V("INP", "ENSICAEN Informatique", "Informatique")], F, S_INP, txt="Informatique 5, génie physique et systèmes embarqués 2"))
add("ensil", A("ccinp", 4, [V("INP", "ENSIL - ENSCI Limoges Electronique et Télécommunications", "Électronique et télécoms"), V("INP", "ENSIL - ENSCI Limoges Mécatronique", "Mécatronique")],
               F, S_INP, txt="Mécatronique 2, électronique et télécoms 2"))
add("ensai", A("ccinp", 11, [V("INP", "ENSAI Rennes Civil", "Civils"), V("INP", "ENSAI Rennes Fonctionnaire (Attaché INSEE)", "Fonctionnaires (attachés de l'Insee)")], F, S_INP,
               txt="8 civils + 3 fonctionnaires"))
add("cytech", A("ccinp", 10, [V("INP", "CY TECH Cergy-Pau - Informatique", "Informatique"), V("INP", "CY TECH Cergy-Pau - Mathématiques", "Mathématiques")], F, S_INP,
                txt="Informatique 6, mathématiques appliquées 4"))
add("isima", A("ccinp", 16, [V("INP", "Clermont Auvergne INP - ISIMA", "ISIMA")], F, S_INP))
add("ense3", A("ccinp", 5, [V("INP", "Grenoble INP - ENSE3", "Ense3")], F, S_INP))
add("ensimag", A("ccinp", 40, [V("INP", "Grenoble INP - ENSIMAG", "Ensimag")], F, S_INP))
add("esisar", A("ccinp", 6, [V("INP", "Grenoble INP - Esisar", "Esisar")], F, S_INP))
add("pagora", A("ccinp", 1, [V("INP", "Grenoble INP - Pagora", "Pagora")], F, S_INP))
add("phelma", A("ccinp", 8, [V("INP", "Grenoble INP - Phelma (Physique Electronique Télécoms)", "PET – physique, électronique, télécoms")], F, S_INP))
add("cpe", A("ccinp", 5, [V("INP", "CPE ETI : Electronique, Télécommunications, Informatique", "Électronique, télécoms, informatique (ETI)")], F, S_INP))
add("ensem", A("ccinp", 6, [V("INP", "Lorraine INP - ENSEM - Spécialité des systèmes numériques", "Systèmes numériques")], F, S_INP))
add("engees", A("ccinp", 2, [V("INP", "École nationale du génie de l'eau et de l'environnement de Strasbourg (ENGEES) - Etudiant", "Statut étudiant")], F, S_INP))
add("tps", A("ccinp", 5, [V("INP", "TELECOM PHYSIQUE Strasbourg", "Télécom Physique Strasbourg")], F, S_INP, lib="Cursus via le CCINP"))
add("seatech", A("ccinp", 2, [V("INP", "SeaTech Toulon", "SeaTech")], F, S_INP))
add("n7", A("ccinp", 40, [V("INP", "Toulouse INP - ENSEEIHT - Electronique-Energie-Automatique (EEA)", "Électronique, énergie, automatique (EEA)"),
                          V("INP", "Toulouse INP - ENSEEIHT - Mécanique des Fluides-Energetique-Environnement (MFEE)", "Mécanique des fluides, énergétique, environnement (MFEE)"),
                          V("INP", "Toulouse INP - ENSEEIHT - Sciences du Numérique", "Sciences du numérique")], F, S_INP, txt="EEA 5, MFEE 5, sciences du numérique 30"))
add("ensiacet", A("ccinp", 2, [V("INP", "Toulouse INP - ENSIACET - Génie Industriel", "Génie industriel")], F, S_INP))

# ---------------------------------------------------------------- Banque CCINP
def B(fee): return ["ccinp", fee]
add("ensisa", A("bccinp", 4, [V("B", "ENSISA Mulhouse Automatique et Systèmes Embarqués", "Automatique et systèmes embarqués"), V("B", "ENSISA Mulhouse Informatique et réseaux", "Informatique et réseaux")],
                B("b_ensisa"), S_INP, txt="Automatique 2, informatique 2"))
add("enstib", A("bccinp", 2, [V("B", "Lorraine INP - ENSTIB", "ENSTIB")], B("b_enstib"), S_INP))
add("enise", A("bccinp", 10, [], B("b_enise"), S_INP, txt="Génie mécanique 2, génie civil 3, génie sensoriel 5", note="Nouvelle dans la banque CCINP : pas de chiffres MPI 2025."))
add("esiee", A("bccinp", 12, [V("PA", "ESIEE Paris", "ESIEE Paris (via Puissance Alpha en 2025)", c25="Puissance Alpha"),
                              V("PA", "ESIEE Paris - filière data - statut étudiant (1 an) + statut apprenti (2 ans)", "Filière data, 1 an étudiant + 2 ans apprenti (2025)", c25="Puissance Alpha")],
               B("b_esiee"), S_INP, txt="Généraliste 10 + filière data 2", note="Recrutait via Puissance Alpha en 2025 (places toutes filières) : rangs non comparables."))
add("eost", A("bccinp", 3, [V("B", "EOST Strasbourg", "EOST")], B("b_eost"), S_INP))
add("ensar", A("bccinp", 6, [], B("b_ensar"), S_INP, txt="Gestion des risques 4, science de la donnée 2", note="Pas de places MPI en 2025."))
add("air", A("bccinp", 4, [], B("b_air"), S_INP, txt="Mécanique 2, base 1, pilotes 1", note="Pas de places MPI en 2025. Épreuves propres (sport, aptitude médicale, entretien)."))
add("esm", A("bccinp", 5, [], B("b_esm"), S_INP, note="Pas de places MPI en 2025. Épreuves propres (sport, aptitude médicale, entretien)."))
add("gi_grenoble", A("bccinp", 76, [V("BI", "Grenoble INP - Génie industriel", "Génie industriel")], B("b_gi"), S_INP, scope="toutes filières"))
add("ensgsi", A("bccinp", 38, [V("BI", "Lorraine INP - ENSGSI", "ENSGSI")], B("b_ensgsi"), S_INP, scope="toutes filières"))

# ---------------------------------------------------------------- INSA
def sentence(s):
    out = []
    for i, w in enumerate(s.strip().split(" ")):
        if i and not (w.isupper() and len(w) > 1):
            w = w.lower()
        out.append(w)
    r = " ".join(out)
    for a, b in (("Energ", "Énerg"), ("energ", "énerg"), ("Electr", "Électr"), ("electr", "électr")):
        r = re.sub(r"\b" + a, b, r)
    return r[:1].upper() + r[1:]
INSA_PREFIX = {"insa_cvl": "INSA Centre Val de Loire ", "insa_lyon": "INSA Lyon ", "insa_rennes": "INSA Rennes ", "insa_rouen": "INSA Rouen Normandie ",
               "insa_strasbourg": "INSA Strasbourg ", "insa_toulouse": "INSA Toulouse ", "esitech": "ESITech Rouen - ", "isis": "ISIS Castres ", "supenr": "Sup'EnR Perpignan "}
insa_rows = [r for r in scei_mpi.ROWS if r["sec"] == "INSA" and not r["total"]]
used = set()
for sid in list(INSA_PREFIX) + ["insa_hdf"]:
    if sid == "insa_hdf":
        rows = [r for r in insa_rows if re.match(r"^INSA Hauts[- ]de[- ]+France ", r["name"])]
        cut = lambda n: re.sub(r"^INSA Hauts[- ]de[- ]+France ", "", n)
    else:
        pre = INSA_PREFIX[sid]
        rows = [r for r in insa_rows if r["name"].startswith(pre)]
        cut = lambda n, pre=pre: n[len(pre):]
    if not rows: continue
    used.update(id(r) for r in rows)
    base = next(a for a in PC_ACCES[sid] if a["c"] == "insa")
    ACC.setdefault(sid, []).append(dict({k: v for k, v in base.items() if k not in ("stats", "scope")}, scope="toutes filières",
                                        stats=[V("INSA", r["name"], sentence(cut(r["name"]))) for r in rows]))
assert len(used) == len(insa_rows), [r["name"] for r in insa_rows if id(r) not in used]

# ---------------------------------------------------------------- Polytech : liste MPI séparée ; places 2026 = « + N en MPI » des fiches MP
MP = json.load(open(os.path.join(HERE, "..", "build", "data.json"), encoding="utf-8"))
sys.path.insert(0, HERE)
import scei_psi
# correspondance nom SCEI -> (école, libellé MP), établie sur la liste PSI (mêmes intitulés SCEI que la MPI)
NAME2 = {}
psi_poly = [r for r in scei_psi.ROWS if r["sec"] == "POLY"]
taken = set()
for e in MP["ecoles"]:
    for a in e["acces"]:
        if a["c"] != "e3a_poly" or a["f"] != "MP": continue
        for v in a["stats"]:
            cands = [r for r in psi_poly if r["pl"] == v["pl"] and (r["med"] or None) == v["med"] and id(r) not in taken]
            if len(cands) > 1:
                key = e["nom"].split(" ")[-1] if e["nom"].startswith("Polytech") else e["nom"].split(" ")[0]
                cands = [r for r in cands if key.lower() in r["name"].lower()]
            assert len(cands) == 1, (e["id"], v["lib"])
            taken.add(id(cands[0]))
            NAME2[cands[0]["name"]] = (e["id"], v["lib"])
poly_rows = [r for r in scei_mpi.ROWS if r["sec"] == "POLY" and not r["total"]]
by_school = {}
for r in poly_rows:
    if r["name"] not in NAME2:
        raise SystemExit("Polytech MPI : intitulé inconnu " + r["name"])
    sid, lib = NAME2[r["name"]]
    by_school.setdefault(sid, []).append(V("POLY", r["name"], lib))
for e in MP["ecoles"]:
    for a in e["acces"]:
        if a["c"] != "e3a_poly" or a["f"] != "MP": continue
        m = re.search(r"\+ (\d+) en MPI", a.get("txt") or "")
        n = int(m.group(1)) if m else 0
        st = by_school.get(e["id"], [])
        if not n and not st: continue
        add(e["id"], A("e3a_poly", n, st, ["ccinp", "e3a_poly"], S_E3A, scope="MPI", txt="Liste propre à la MPI" if n else None,
                       note=None if n else "Pas de places MPI en 2026."))

# ---------------------------------------------------------------- e3a : écoles indépendantes
def IND(sid, p26, stats, fee, inter=False, txt=None, note=None):
    sc = "MP+MPI+PC+PSI" if inter else "MPI"
    n = " ".join(x for x in (note, NOTE_INTER if inter else None) if x) or None
    add(sid, A("e3a_ind", p26, stats, ["ccinp", fee], S_E3A, scope=sc, txt=txt, note=n))
PA = lambda name, lib: V("PA", name, lib, c25="Puissance Alpha")
IND("trois_il", 10, [PA("3iL Ingénieurs Limoges", "3iL")], "ind_3il", note=NOTE_PA)
IND("aflokkat", 20, [], "ind_aflokkat", inter=True, note="Nouvelle école sur e3a-Polytech en 2026 : pas de statistiques 2025.")
IND("efrei", 50, [PA("EFREI Paris", "EFREI Paris")], "ind_efrei", inter=True, note=NOTE_PA + " Les 50 places 2026 couvrent Paris et Bordeaux.")
IND("eia", 1, [V("AE", "EIA Bethune - Génie électrique", "EIA Béthune – génie électrique")], "ind_eia")
IND("eidd", 55, [V("EI", "EIDD Paris", "EIDD Paris")], "ind_eidd", inter=True)
IND("eijv", 7, [V("AE", "EIJV Amiens - Cybersécurité", "Cybersécurité (Amiens)"), V("AE", "EIJV - Technologie de l'Information pour la santé", "Technologies de l'information pour la santé"),
                V("AE", "EIJV Saint Quentin - Logistique innovante", "Logistique innovante (Saint-Quentin)")], "ind_eijv",
    txt="Cybersécurité 4, supply chain et logistique 1, numérique-santé-IA 2")
IND("eil", 17, [V("AE", "EIL Côte d'Opale - Calais (informatique)", "Calais – informatique"), V("AE", "EIL Côte d'Opale - Dunkerque (Génie Energétique et Environnement)", "Dunkerque – génie énergétique et environnement"),
                V("AE", "EIL Côte d'Opale - Saint-Omer (Génie Industriel)", "Saint-Omer – génie industriel"), V("AE", "EIL Côte d'Opale - Boulogne (Agroalimentaire)", "Boulogne – agroalimentaire")], "ind_eil",
    txt="Informatique 5, génie énergétique 5, génie industriel 5, agroalimentaire 2")
IND("elisa", 30, [PA("ELISA Aerospace Bordeaux", "Bordeaux"), PA("ELISA Aerospace Hauts de France", "Hauts-de-France")], "ind_elisa", inter=True, note=NOTE_PA)
IND("esaip", 24, [PA("ESAIP Angers / Aix-en-Provence", "ESAIP Angers / Aix-en-Provence")], "ind_esaip", inter=True, note=NOTE_PA)
IND("eseo", 20, [PA("ESEO Angers - Paris - Dijon", "ESEO Angers – Paris – Dijon")], "ind_eseo", inter=True, note=NOTE_PA)
IND("esiea", 10, [PA("ESIEA Paris - Laval", "ESIEA Paris – Laval")], "ind_esiea", note=NOTE_PA)
IND("estia", 5, [PA("ESTIA Bidart", "ESTIA Bidart")], "ind_estia", note=NOTE_PA)
add("imtne", A("e3a_ind", 5, [V("AE", "IMT Nord Europe (en partenariat avec ISPA)", "IMT Nord Europe (avec l'ISPA)")], ["ccinp", "ind_imtne"], S_E3A,
               lib="Formation en partenariat avec l'ISPA (plasturgie)"))
IND("isen_med", 6, [PA("ISEN Méditerranée Toulon", "ISEN Méditerranée Toulon")], "ind_isenmed", note=NOTE_PA)
IND("isen_ouest", 25, [PA("ISEN Ouest - Brest - Caen - Nantes", "ISEN Ouest Brest – Caen – Nantes")], "ind_isenouest", inter=True, note=NOTE_PA)
IND("isep", 30, [PA("ISEP", "ISEP")], "ind_isep", inter=True, note=NOTE_PA)
IND("hei", 15, [PA("HEI JUNIA – Lille", "HEI JUNIA Lille")], "ind_hei", note=NOTE_PA)
IND("isen_lille", 10, [PA("ISEN JUNIA Lille-BORDEAUX", "ISEN JUNIA Lille – Bordeaux")], "ind_isenlille", note=NOTE_PA)

# ---------------------------------------------------------------- Avenir Prépas
F = ["ccinp", "avenir"]
add("eigsi", A("avenir", 3, [V("AV", "EIGSI La Rochelle", "EIGSI La Rochelle")], F, S_E3A))
add("esigelec", A("avenir", 5, [V("AV", "ESIGELEC Rouen/Poitiers", "ESIGELEC Rouen / Poitiers")], F, S_E3A))
add("esilv", A("avenir", 12, [V("AV", "ESILV Paris", "ESILV Paris"), V("AV", "ESILV Paris FISEA Finance", "ESILV Paris – FISEA finance")], F, S_E3A,
               lib="Campus de Paris-La Défense", txt="10 en statut étudiant + 2 en apprentissage"),
             A("avenir", 2, [V("AV", "ESILV Nantes", "ESILV Nantes")], F, S_E3A, lib="Campus de Nantes"))
add("estaca", A("avenir", 4, [V("AV", "ESTACA Bordeaux - Filière Aéronautique", "Bordeaux – aéronautique")], F, S_E3A, lib="Campus de Bordeaux"))

# ---------------------------------------------------------------- Ingéni'Up, Groupe UT : voies communes (copie de la PC)
for sid in ("ecam_epmi", "ecam_rennes", "icam", "unilasalle", "utc", "utt", "utbm"):
    for a in PC_ACCES[sid]:
        if a["c"] in ("ingeniup", "ut"):
            ACC.setdefault(sid, []).append(json.loads(json.dumps(a)))

# ---------------------------------------------------------------- EPITA-IPSA-ESME, CESI
def epi(sid, rows):
    base = next(a for a in PC_ACCES[sid] if a["c"] == "epita")
    ACC.setdefault(sid, []).append(dict({k: v for k, v in base.items() if k != "stats"}, stats=[V("EP", n, l) for n, l in rows]))
epi("epita", [("EPITA campus Paris", "Paris"), ("EPITA Paris - FISA", "Paris – apprentissage (FISA)"), ("EPITA campus Lyon", "Lyon"),
              ("EPITA campus Rennes", "Rennes"), ("EPITA campus Strasbourg", "Strasbourg"), ("EPITA campus Toulouse", "Toulouse")])
epi("ipsa", [("IPSA Paris", "Paris"), ("IPSA Paris - FISA", "Paris – apprentissage (FISA)"), ("IPSA Toulouse", "Toulouse")])
epi("esme", [("ESME", "ESME"), ("ESME - FISA", "ESME – apprentissage (FISA)")])
cesi = next(a for a in PC_ACCES["cesi"] if a["c"] == "cesi")
ACC["cesi"] = [dict({k: v for k, v in cesi.items() if k != "stats"}, stats=[{"lib": "26 parcours et campus (2025)", "pl": 128, "int": 2, "med": None, "moy": None}],
                    note="Concours propre (maths, physique, anglais, français + entretien). En 2025, 2 élèves de MPI ont intégré le CESI par ce concours.")]

if __name__ == "__main__":
    open(sys.argv[1], "w", encoding="utf-8").write("# -*- coding: utf-8 -*-\n# Généré par tools/build_mpi_acces.py (places MPI 2026 + statistiques SCEI MPI 2025)\n"
                                                   "MPI_ACCES = " + pprint.pformat(ACC, width=170, sort_dicts=False) + "\n")
    print(len(ACC), "écoles,", sum(len(v) for v in ACC.values()), "voies MPI")
