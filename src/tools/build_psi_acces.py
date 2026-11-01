# -*- coding: utf-8 -*-
"""Voies d'accès PSI 2026 (places) + statistiques SCEI PSI 2025, école par école.
Sources des places 2026 : notices officielles (Mines-Ponts, Mines-Télécom, Centrale-Supélec, CCINP, e3a-Polytech),
ENS Paris-Saclay (postes 2026), Onisep (X)."""
import sys, json, os, re, pprint
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "build"))
from scei_psi import row
from data_pc import PC_ACCES

def src(t, u): return {"t": t, "u": u}
S_X = src("Fiche Onisep (places 2026 par filière)", "https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/essonne/ecole-polytechnique-institut-polytechnique-de-paris-etablissement-experimental/diplome-d-ingenieur-de-l-ecole-polytechnique-institut-polytechnique-de-paris")
S_ENS = src("Notice inter-ENS 2026 (banque PSI, p. 17)", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/notice_interens_2026_mise_en_ligne_vf260212.pdf")
S_ENS_SACLAY = src("ENS Paris-Saclay : postes d'élèves ouverts en 2026", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_postes_eleves_ouverts_ENS_Paris-Saclay.pdf")
S_CCMP = src("Notice des écoles Mines-Ponts 2026", "https://concoursminesponts.fr/wp-content/uploads/2025/12/notice-des-ecoles-2026-22.12.25.pdf")
S_CMT = src("Notice Mines-Télécom 2026", "https://cahier-de-prepa.fr/pc-descartes/download?id=260")
S_CCS = src("Notice Centrale-Supélec 2026, filière PSI", "https://www.concours-centrale-supelec.fr/sites/default/files/documents/CCS_2026_PSI.pdf")
S_INP = src("Places PSI 2026 (site du CCINP)", "https://www.concours-commun-inp.fr/fr/les-ecoles/les-places-dans-les-ecoles/places-psi.html")
S_E3A = src("Notice 2026 de la banque e3a-Polytech", "https://esigelec.fr/sites/default/files/2025-12/VF-Notice-2026-Banque-e3a-Polytech.pdf")

NOTE_ENS = ("Les classés et intégrés ne comptent que les candidats « fonctionnarisables » (note du SCEI). "
            "Chaque ENS a sa propre liste de classement.")
NOTE_PA = "En 2025, l'école recrutait via Puissance Alpha (places toutes filières) : rangs non comparables à ceux d'e3a-Polytech."
NOTE_INTER = "Places communes à toutes les filières (liste « INTER » de la notice e3a-Polytech)."
INS = {"POLY": 2663, "PA": 867, "AV": 1271, "EP": 539, "EI": 507}
INS_AE = {"EIJV": 567, "EIL": 348}

def V(sec, name, lib, **extra):
    r = row(sec, name)
    d = {"lib": lib, "pl": r["pl"], "int": r["int"], "med": r["med"] or None, "moy": r["moy"] or None}
    if sec in ("POLY", "PA", "AV", "EP", "EI", "AE"):
        ins = INS.get(sec) or next((v for k, v in INS_AE.items() if name.startswith(k)), None)
        if ins: d["ins"] = ins
    elif r["cl"]:
        d["cl"] = r["cl"]
    if r.get("iint") is not None and sec not in ("AV", "AE", "EP", "CESI"):
        d["inter"] = True
        if sec not in ("POLY", "PA", "EI"):
            d["iint"] = r["iint"]
    if sec in ("POLY", "EI"):
        d["inter"] = True
    if r["int"] == 0 and not d.get("inter"):   # liste propre à la filière : pas d'admis, pas de rang
        d["med"] = d["moy"] = None
    d.update(extra)
    return d

def A(c, p26, stats, fee, s, scope="PSI", lib=None, txt=None, note=None):
    d = {"c": c, "p26": p26, "scope": scope, "stats": stats, "fee": fee, "src": s}
    if lib: d["lib"] = lib
    if txt: d["txt"] = txt
    if note: d["note"] = note
    return d

ACC = {}
def add(sid, *acc): ACC.setdefault(sid, []).extend(acc)

# ---------------------------------------------------------------- X, ENS
add("x", A("x", 56, [V("X", "ECOLE POLYTECHNIQUE", "École polytechnique")], ["x"], S_X))
add("ens_ulm", A("ens", None, [V("X", "ENS Ulm PSI", "ENS Ulm PSI")], ["ens"], S_ENS, lib="Concours PSI", txt="6 places en 2025",
                 note="Nombre de postes 2026 non trouvé. " + NOTE_ENS))
add("ens_saclay", A("ens", 36, [V("X", "ENS Paris-Saclay", "ENS Paris-Saclay PSI")], ["ens"], S_ENS_SACLAY,
                    lib="Concours Physique-PSI et SI-PSI", txt="18 postes en Physique-PSI + 18 en SI-PSI",
                    note="Depuis 2026, deux concours PSI (Physique-PSI et SI-PSI) : tu peux t'inscrire aux deux et classer tes vœux. En 2025, un seul classement. " + NOTE_ENS))
add("ens_rennes", A("ens", None, [V("X", "ENS Rennes", "ENS Rennes PSI")], ["ens"], S_ENS, lib="Concours PSI", txt="6 places en 2025",
                    note="Nombre de postes 2026 non trouvé. " + NOTE_ENS))

# ---------------------------------------------------------------- Mines-Ponts
F = ["ccmp"]
add("minesparis", A("ccmp", 36, [V("MPo", "MINES Paris", "Mines Paris")], F, S_CCMP))
add("ponts", A("ccmp", 70, [V("MPo", "Ecole Nationale des Ponts et Chaussées", "École des Ponts")], F, S_CCMP))
add("telecomparis", A("ccmp", 32, [V("MPo", "TELECOM Paris", "Statut étudiant"), V("MPo", "TELECOM Paris - Apprentissage", "Apprentissage")], F, S_CCMP,
                      txt="31 en statut étudiant + 1 en apprentissage"))
add("ensta", A("ccmp", 34, [V("MPo", "ENSTA Paris", "ENSTA Paris (statut étudiant)"), V("MPo", "ENSTA Paris - apprentissage", "ENSTA Paris – apprentissage")], F, S_CCMP,
               lib="Campus Paris-Saclay (Palaiseau)", txt="32 en statut étudiant + 2 en apprentissage"),
     A("ccmp", 34, [], F, S_CCMP, lib="Campus de Brest",
       note="Nouveau sur Mines-Ponts en 2026. En 2025, l'ex-ENSTA Bretagne recrutait via Mines-Télécom : voir plus bas pour comparer."))
add("ensae", A("ccmp", 12, [V("MPo", "ENSAE Paris", "ENSAE Paris")], F, S_CCMP))
add("supaero", A("ccmp", 80, [V("MPo", "ISAE - SUPAERO Toulouse", "ISAE-SUPAERO")], F, S_CCMP))
add("minesnancy", A("ccmp", 40, [V("MPo", "MINES de NANCY", "Mines Nancy")], F, S_CCMP))
add("minesse", A("ccmp", 45, [V("MPo", "MINES SAINT-ETIENNE", "Mines Saint-Étienne")], F, S_CCMP))
add("imtatlantique", A("ccmp", 85, [V("MPo", "IMT Atlantique", "IMT Atlantique")], F, S_CCMP))
add("chimieparistech", A("ccmp", 3, [V("MPo", "Chimie ParisTech", "Chimie ParisTech")], F, S_CCMP,
                         note="Très peu de places en PSI : l'école recrute surtout en PC."))

# ---------------------------------------------------------------- Mines-Télécom
F = ["cmt"]
add("eivp", A("cmt", 24, [V("MT", "EIVP Paris Civil", "Civils")], F, S_CMT, lib="Élèves civils"),
            A("cmt", 4, [V("MT", "EIVP Paris Fonctionnaire", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (rémunérés)"))
add("enm", A("cmt", 2, [V("MT", "ECOLE METEOROLOGIE (non fonctionnaire)", "Non fonctionnaires")], F, S_CMT, lib="Élèves civils"),
           A("cmt", 5, [V("MT", "ECOLE METEOROLOGIE (fonctionnaire)", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (rémunérés)"))
add("enac", A("cmt", 29, [V("INP", "ENAC Toulouse Civil", "Civils (via CCINP en 2025)", c25="CCINP")], F, S_CMT, lib="Ingénieurs civils",
              note="A quitté le CCINP pour Mines-Télécom en 2026 : rangs 2025 = rangs CCINP."),
            A("cmt", 6, [V("INP", "ENAC Toulouse Fonctionnaire", "Fonctionnaires (via CCINP en 2025)", c25="CCINP")], F, S_CMT, lib="Ingénieurs fonctionnaires"))
add("ensg_geol", A("cmt", 4, [V("MT", "ENSG Nancy", "ENSG Nancy")], F, S_CMT))
add("ensiie", A("cmt", 20, [V("MT", "ENSIIE Evry", "ENSIIE")], F, S_CMT))
add("enssat", A("cmt", 11, [V("MT", "ENSSAT Lannion", "ENSSAT")], F, S_CMT))
NOTE_FIDS = next(a["note"] for a in PC_ACCES["ensta"] if a["c"] == "cmt" and a.get("note"))
add("ensta", A("cmt", 14, [V("MT", "ENSTA Bretagne (filière sous statut étudiant)", "ex-ENSTA Bretagne, statut étudiant (2025, pour comparaison)", prev="ex-ENSTA Bretagne")], F, S_CMT,
               lib="FIDS – ingénieur défense et sécurité (statut étudiant)", note=NOTE_FIDS),
             A("cmt", 15, [V("MT", "ENSTA Bretagne (filière sous statut IETA - Direction Générale de l'Armement)", "ex-ENSTA Bretagne, statut IETA (2025, pour comparaison)", prev="ex-ENSTA Bretagne")], F, S_CMT,
               lib="FIDS – statut IETA (militaire, rémunéré)"))
add("entpe", A("cmt", 22, [V("MT", "ENTPE Lyon Civil", "Civils")], F, S_CMT, lib="Élèves civils"),
             A("cmt", 25, [V("MT", "ENTPE Lyon Fonctionnaire", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (rémunérés)"))
add("eurecom", A("cmt", 10, [V("MT", "EURECOM", "EURECOM")], F, S_CMT))
add("geodata", A("cmt", 2, [V("MT", "ENSG-Géomatique Marne la Vallée", "Civils")], F, S_CMT, lib="Élèves civils"),
               A("cmt", 2, [V("MT", "ENSG-Géomatique Marne la Vallée Fonctionnaire", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires (agents de l'IGN, rémunérés)"))
add("albi", A("cmt", 54, [V("MT", "IMT Mines Albi", "IMT Mines Albi")], F, S_CMT))
add("ales", A("cmt", 62, [V("MT", "IMT Mines Alès", "IMT Mines Alès")], F, S_CMT))
add("imtne", A("cmt", 52, [V("MT", "IMT Nord Europe", "IMT Nord Europe")], F, S_CMT, lib="Élèves civils"),
             A("cmt", 3, [V("MT", "IMT Nord Europe Fonct.", "Fonctionnaires")], F, S_CMT, lib="Élèves fonctionnaires"))
add("ensma", A("cmt", 58, [V("INP", "ISAE-ENSMA Poitiers", "ISAE-ENSMA (via CCINP en 2025)", c25="CCINP")], F, S_CMT,
               note="A quitté le CCINP pour Mines-Télécom en 2026 : les rangs 2025 sont des rangs CCINP, pas comparables."))
add("supmeca", A("cmt", 52, [V("MT", "ISAE-Supméca Paris", "ISAE-Supméca")], F, S_CMT))
add("ismin", A("cmt", 28, [V("MT", "Mines Saint Etienne-ISMIN", "Mines Saint-Étienne – ISMIN")], F, S_CMT))
add("telecomnancy", A("cmt", 5, [V("MT", "TELECOM Nancy", "Télécom Nancy")], F, S_CMT))
add("tps", A("cmt", 8, [V("MT", "Télécom Physique Strasbourg Informatique et Réseaux", "Informatique et réseaux")], F, S_CMT, lib="Informatique et réseaux"),
           A("cmt", 12, [V("MT", "Télécom Physique Strasbourg TI-Santé", "TI-Santé")], F, S_CMT, lib="Technologies de l'information pour la santé"))
add("telecomse", A("cmt", 23, [V("MT", "TELECOM St Etienne", "Télécom Saint-Étienne")], F, S_CMT))
add("tsp", A("cmt", 42, [V("MT", "TELECOM SudParis", "Télécom SudParis")], F, S_CMT))

# ---------------------------------------------------------------- Centrale-Supélec
CSL = "CentraleSupélec - "
add("cs",
    A("ccs", 132, [V("CS", CSL + "Ingénieur généraliste - statut étudiant – campus de Paris-Saclay", "Généraliste, Paris-Saclay (statut étudiant)")], ["ccs_cs"], S_CCS, lib="Ingénieur généraliste, Paris-Saclay"),
    A("ccs", 14, [V("CS", CSL + "Ingénieur généraliste - statut apprenti - campus de Metz", "Apprentis, campus de Metz"),
                  V("CS", CSL + "Ingénieur généraliste - statut apprenti - campus de Rennes", "Apprentis, campus de Rennes")], ["ccs_cs"], S_CCS, lib="Ingénieur généraliste, apprentissage (Metz, Rennes)"),
    A("ccs", 3, [V("CS", CSL + "Ingénieur de spécialité Informatique - campus de Metz", "Spécialité informatique (Metz)")], ["ccs_cs"], S_CCS, lib="Spécialité informatique (Metz)"),
    A("ccs", 7, [V("CS", CSL + "Ingénieur de spécialité Physique - campus de Metz", "Spécialité physique (Metz)")], ["ccs_cs"], S_CCS, lib="Spécialité génie physique (Metz)"),
    A("ccs", 3, [V("CS", CSL + "Ingénieur de spécialité Cybersécurité - campus de Rennes", "Spécialité cybersécurité (Rennes)")], ["ccs_cs"], S_CCS, lib="Spécialité cybersécurité (Rennes)"),
    A("ccs", 6, [V("CS", CSL + "Ingénieur de spécialité Electronique - campus de Rennes/Paris-Saclay", "Spécialité électronique (Rennes/Paris-Saclay)")], ["ccs_cs"], S_CCS, lib="Spécialité électronique (Rennes, Paris-Saclay)"),
    A("ccs", 8, [V("CS", CSL + "Ingénieur de spécialité Énergie – Génie électrique - campus de Rennes", "Spécialité énergie – génie électrique (Rennes)")], ["ccs_cs"], S_CCS, lib="Spécialité génie électrique (Rennes)"),
    A("ccs", 6, [V("CS", CSL + "Ingénieur de spécialité Systèmes Numériques - campus de Rennes", "Spécialité systèmes numériques (Rennes)")], ["ccs_cs"], S_CCS, lib="Spécialité systèmes numériques (Rennes)"))
add("centralelyon", A("ccs", 82, [V("CS", "Centrale Lyon", "Centrale Lyon")], ["ccs_lyon"], S_CCS))
add("centralelille", A("ccs", 60, [V("CS", "Centrale Lille", "Centrale Lille")], ["ccs_lille"], S_CCS))
add("centralenantes", A("ccs", 85, [V("CS", "Centrale Nantes", "Centrale Nantes")], ["ccs_nantes"], S_CCS))
add("centralemed", A("ccs", 70, [V("CS", "Centrale Méditerranée", "Centrale Méditerranée")], ["ccs_med"], S_CCS))
add("ensam", A("ccs", 260, [V("CS", "Arts et Métiers", "Statut étudiant"), V("CS", "Arts et Métiers - ingénieurs militaires", "Ingénieurs militaires"),
                            V("CS", "Arts et Métiers - voie de l'apprentissage", "Apprentissage")], ["ccs_amensea"], S_CCS,
               txt="260 places PSI, étudiants, apprentis et ingénieurs militaires, 8 campus confondus",
               note="En PSI, Arts et Métiers ouvre 260 places en 2026, contre 53 en MP."))
add("ensea", A("ccs", 70, [V("CS", "ENSEA Cergy", "ENSEA Cergy")], ["ccs_amensea"], S_CCS))
add("navale", A("ccs", 32, [V("CS", "ECOLE NAVALE Brest", "École navale")], ["ccs_navale"], S_CCS,
                note="Épreuves propres (oraux, sport, aptitude médicale) : rangs sur un petit nombre de classés."))
add("iogs", A("ccs", 28, [V("CS", "Institut d'optique Graduate School (SupOptique)", "SupOptique")], ["ccs_iogs"], S_CCS))
add("epf", A("ccs", 69, [V("CS", "EPF Cachan", "Cachan"), V("CS", "EPF Montpellier", "Montpellier"), V("CS", "EPF Saint Nazaire", "Saint-Nazaire"), V("CS", "EPF Troyes", "Troyes")],
             ["ccs_epf"], S_CCS, txt="Cachan 12 + 6, Troyes 12 + 6, Montpellier 10 + 5, Saint-Nazaire 12 + 6 (le 2e chiffre : apprentissage)"))
add("estp", A("ccs", 210, [V("CS", "ESTP - campus de Cachan", "Cachan"), V("CS", "ESTP - campus de Dijon", "Dijon"), V("CS", "ESTP - campus de d'Orléans", "Orléans"), V("CS", "ESTP - campus de Troyes", "Troyes")],
              ["ccs_estp"], S_CCS, txt="Cachan 165, Dijon 15, Orléans 15, Troyes 15"))

# ---------------------------------------------------------------- CCINP (concours commun)
F = ["ccinp"]
add("supmicrotech", A("ccinp", 54, [V("INP", "SUPMICROTECH ENSMM Besançon", "SUPMICROTECH-ENSMM")], F, S_INP))
add("ensc", A("ccinp", 10, [V("INP", "Bordeaux INP - ENSC Cognitique", "ENSC")], F, S_INP))
add("enspima", A("ccinp", 8, [V("INP", "Bordeaux INP - ENSPIMA", "ENSPIMA")], F, S_INP))
add("enseirb", A("ccinp", 74, [V("INP", "Bordeaux INP - ENSEIRB-MATMECA Electronique", "Électronique"), V("INP", "Bordeaux INP - ENSEIRB-MATMECA Informatique", "Informatique"),
                               V("INP", "Bordeaux INP - ENSEIRB-MATMECA Mathématiques et Mécanique", "Mathématiques et mécanique"), V("INP", "Bordeaux INP - ENSEIRB-MATMECA Telecom.", "Télécommunications")],
                 F, S_INP, txt="Par spécialité : 26 + 10 + 21 + 17"))
add("ensai", A("ccinp", 8, [V("INP", "ENSAI Rennes Civil", "Civils"), V("INP", "ENSAI Rennes Fonctionnaire (Attaché INSEE)", "Fonctionnaires (attachés de l'Insee)")], F, S_INP,
               txt="5 civils + 3 fonctionnaires"))
add("ensicaen", A("ccinp", 20, [V("INP", "ENSICAEN Génie Physique et systèmes Embarqués", "Génie physique et systèmes embarqués"), V("INP", "ENSICAEN Informatique", "Informatique")], F, S_INP,
                  txt="Par spécialité : 14 + 6"))
add("cytech", A("ccinp", 24, [V("INP", "CY TECH Cergy - Génie Civil", "Génie civil"), V("INP", "CY TECH Cergy-Pau - Informatique", "Informatique"), V("INP", "CY TECH Cergy-Pau - Mathématiques", "Mathématiques")],
                F, S_INP, txt="Par spécialité : 8 + 10 + 6"))
add("sigma", A("ccinp", 62, [V("INP", "Clermont Auverge INP - SIGMA Clermont  Mécanique", "Mécanique")], F, S_INP, txt="Par spécialité : 58 + 4"))
add("ensil", A("ccinp", 34, [V("INP", "ENSIL - ENSCI Limoges Céramique Industrielle", "Céramique industrielle"), V("INP", "ENSIL - ENSCI Limoges Electronique et Télécommunications", "Électronique et télécoms"),
                             V("INP", "ENSIL - ENSCI Limoges Génie civil", "Génie civil"), V("INP", "ENSIL - ENSCI Limoges Matériaux", "Matériaux"),
                             V("INP", "ENSIL - ENSCI Limoges Mécatronique", "Mécatronique"), V("INP", "ENSIL - ENSCI Limoges Photonique", "Photonique")], F, S_INP,
               txt="Par spécialité : 8 + 4 + 10 + 5 + 4 + 3"))
add("isima", A("ccinp", 7, [V("INP", "Clermont Auvergne INP - ISIMA", "ISIMA")], F, S_INP))
add("ense3", A("ccinp", 80, [V("INP", "Grenoble INP - ENSE3", "Ense3")], F, S_INP))
add("ensimag", A("ccinp", 5, [V("INP", "Grenoble INP - ENSIMAG", "Ensimag")], F, S_INP))
add("esisar", A("ccinp", 12, [V("INP", "Grenoble INP - Esisar", "Esisar")], F, S_INP))
add("pagora", A("ccinp", 6, [V("INP", "Grenoble INP - Pagora", "Pagora")], F, S_INP))
add("phelma", A("ccinp", 70, [V("INP", "Grenoble INP - Phelma (Physique Matériaux Procédés)", "PMP – physique, matériaux, procédés"),
                              V("INP", "Grenoble INP - Phelma (Physique Electronique Télécoms)", "PET – physique, électronique, télécoms")], F, S_INP,
                txt="Par filière : 40 + 30"))
add("cpe", A("ccinp", 5, [V("INP", "CPE ETI : Electronique , Télécommunications, Informatique", "Électronique, télécoms, informatique (ETI)")], F, S_INP))
add("ensem", A("ccinp", 44, [V("INP", "Lorraine INP - ENSEM - Energie", "Énergie"), V("INP", "Lorraine INP - ENSEM - Spécialité des systèmes numériques", "Systèmes numériques")], F, S_INP,
               txt="Par spécialité : 12 + 32"))
add("ensic", A("ccinp", 6, [V("INP", "Lorraine INP - ENSIC", "ENSIC")], F, S_INP))
add("ensgti", A("ccinp", 12, [V("INP", "ENSGTI Pau - Energétique", "Énergétique")], F, S_INP))
add("ensip", A("ccinp", 27, [V("INP", "ENSI Poitiers - Génie de l'Eau et Génie Civil", "Génie de l'eau et génie civil"), V("INP", "ENSI Poitiers Energétique et Environnement", "Énergétique et environnement")],
               F, S_INP, txt="Génie de l'eau et génie civil 7, énergétique et environnement 20"))
add("engees", A("ccinp", 16, [V("INP", "École nationale du génie de l'eau et de l'environnement de Strasbourg (ENGEES) - Etudiant", "Statut étudiant"),
                              V("INP", "École nationale du génie de l'eau et de l'environnement de Strasbourg (ENGEES) - Fonctionnaire", "Fonctionnaires"),
                              V("INP", "École nationale du génie de l'eau et de l'environnement de Strasbourg (ENGEES) - Apprenti", "Apprentissage")], F, S_INP,
                txt="Par statut : 2 + 10 + 4"))
add("tps", A("ccinp", 26, [V("INP", "TELECOM PHYSIQUE Strasbourg", "Télécom Physique Strasbourg")], F, S_INP, lib="Cursus via le CCINP"))
add("seatech", A("ccinp", 30, [V("INP", "SeaTech Toulon", "SeaTech")], F, S_INP))
add("n7", A("ccinp", 82, [V("INP", "Toulouse INP - ENSEEIHT - Electronique-Energie-Automatique (EEA)", "Électronique, énergie, automatique (EEA)"),
                          V("INP", "Toulouse INP - ENSEEIHT - Mécanique des Fluides-Energetique-Environnement (MFEE)", "Mécanique des fluides, énergétique, environnement (MFEE)"),
                          V("INP", "Toulouse INP - ENSEEIHT - Sciences du Numérique", "Sciences du numérique")], F, S_INP, txt="Par département : 38 + 14 + 30"))
add("ensiacet", A("ccinp", 28, [V("INP", "Toulouse INP - ENSIACET - Génie des Procédés", "Génie des procédés"), V("INP", "Toulouse INP - ENSIACET - Génie Industriel", "Génie industriel")], F, S_INP,
                  txt="Par spécialité : 11 + 15 + 2"))

# ---------------------------------------------------------------- Banque CCINP
def B(fee): return ["ccinp", fee]
add("ensisa", A("bccinp", 28, [V("B", "ENSISA Mulhouse Automatique et Systèmes Embarqués", "Automatique et systèmes embarqués"), V("B", "ENSISA Mulhouse Informatique et réseaux", "Informatique et réseaux"),
                               V("B", "ENSISA Mulhouse Mécanique", "Mécanique"), V("B", "ENSISA Mulhouse Textile et Fibres", "Textile et fibres")], B("b_ensisa"), S_INP,
                txt="Automatique 8, informatique 8, mécanique 8, textile 4"))
add("enstib", A("bccinp", 9, [V("B", "Lorraine INP - ENSTIB", "ENSTIB")], B("b_enstib"), S_INP))
add("enise", A("bccinp", 10, [], B("b_enise"), S_INP, txt="Par spécialité : 2 + 3 + 5", note="Nouvelle dans la banque CCINP : pas de chiffres PSI 2025."))
add("cpe", A("bccinp", 5, [V("B", "CPE Lyon - apprentissage - Physique et Systèmes Microélectronique", "Apprentissage – physique et systèmes microélectroniques")], B("b_cpe"), S_INP,
             lib="Apprentissage (banque CCINP)"))
add("eost", A("bccinp", 3, [V("B", "EOST Strasbourg", "EOST")], B("b_eost"), S_INP))
add("esiee", A("bccinp", 39, [V("PA", "ESIEE Paris", "ESIEE Paris (via Puissance Alpha en 2025)", c25="Puissance Alpha"),
                              V("PA", "ESIEE Paris - filière data - statut étudiant (1 an) + statut apprenti (2 ans)", "Filière data, 1 an étudiant + 2 ans apprenti (2025)", c25="Puissance Alpha")],
               B("b_esiee"), S_INP, txt="Généraliste 35 + filière data 4",
               note="Recrutait via Puissance Alpha en 2025 (places toutes filières) : rangs non comparables."))
add("ensar", A("bccinp", 5, [V("B", "ENSAR Poitiers (campus de Niort)", "ENSAR (campus de Niort)")], B("b_ensar"), S_INP, txt="4 + 1"))
add("esm", A("bccinp", 39, [V("B", "ESM Saint-Cyr", "ESM Saint-Cyr")], B("b_esm"), S_INP,
             note="Épreuves propres (sport, aptitude médicale, entretien) : rangs sur un petit nombre de classés."))
add("air", A("bccinp", 32, [V("B", "ECOLE DE L'AIR Base", "Base"), V("B", "ECOLE DE L'AIR Méca", "Mécanique"), V("B", "ECOLE DE L'AIR Pilote", "Pilote")], B("b_air"), S_INP,
             txt="Base 6, mécanique 6, pilotes 20",
             note="Épreuves propres (sport, aptitude médicale, entretien) : rangs sur un petit nombre de classés."))
add("gi_grenoble", A("bccinp", 76, [V("BI", "Grenoble INP - Génie industriel", "Génie industriel")], B("b_gi"), S_INP, scope="toutes filières"))
add("eeigm", A("bccinp", 10, [V("BI", "Lorraine INP - EEIGM", "EEIGM")], B("b_eeigm"), S_INP, scope="toutes filières"))
add("ensgsi", A("bccinp", 38, [V("BI", "Lorraine INP - ENSGSI", "ENSGSI")], B("b_ensgsi"), S_INP, scope="toutes filières"))

# ---------------------------------------------------------------- INSA (copie des voies PC, statistiques PSI)
def sentence(s):
    s = s.strip()
    out = []
    for i, w in enumerate(s.split(" ")):
        if i and not (w.isupper() and len(w) > 1):
            w = w.lower()
        out.append(w)
    r = " ".join(out)
    for a, b in (("Energ", "Énerg"), ("energ", "énerg"), ("Electr", "Électr"), ("electr", "électr")):
        r = re.sub(r"\b" + a, b, r)
    return r[:1].upper() + r[1:]
INSA_PREFIX = {"insa_cvl": "INSA Centre Val de Loire ", "insa_lyon": "INSA Lyon ", "insa_rennes": "INSA Rennes ", "insa_rouen": "INSA Rouen Normandie ",
               "insa_strasbourg": "INSA Strasbourg ", "insa_toulouse": "INSA Toulouse ", "esitech": "ESITech Rouen - ", "isis": "ISIS Castres ", "supenr": "Sup'EnR Perpignan "}
import scei_psi
for sid, pre in list(INSA_PREFIX.items()) + [("insa_hdf", None)]:
    if sid == "insa_hdf":
        rows = [r for r in scei_psi.ROWS if r["sec"] == "Groupe INSA" and not r["total"] and r["name"].replace("-", " ").replace("  ", " ").startswith("INSA Hauts de France")
                or (r["sec"] == "Groupe INSA" and r["name"].startswith("INSA Hauts-de"))]
        cut = lambda n: re.sub(r"^INSA Hauts[- ]de[- ]+France ", "", n)
    else:
        rows = [r for r in scei_psi.ROWS if r["sec"] == "Groupe INSA" and not r["total"] and r["name"].startswith(pre)]
        cut = lambda n, pre=pre: n[len(pre):]
    base = next(a for a in PC_ACCES[sid] if a["c"] == "insa")
    st = [V("INSA", r["name"], sentence(cut(r["name"]))) for r in rows]
    ACC.setdefault(sid, []).append(dict({k: v for k, v in base.items() if k not in ("stats", "scope")}, scope="toutes filières", stats=st))

# ---------------------------------------------------------------- Polytech : mêmes libellés que la MP (liste interfilière : mêmes rangs)
import json as _json
MP = _json.load(open(os.path.join(os.path.dirname(__file__), "..", "build", "data.json"), encoding="utf-8"))
MPBY = {e["id"]: e for e in MP["ecoles"]}
poly_rows = [r for r in scei_psi.ROWS if r["sec"] == "POLY"]
used = set()
for sid, e in MPBY.items():
    for a in e["acces"]:
        if a["c"] != "e3a_poly" or a["f"] != "MP": continue
        pc = next(x for x in PC_ACCES[sid] if x["c"] == "e3a_poly")
        st = []
        for v in a["stats"]:
            cands = [r for r in poly_rows if r["pl"] == v["pl"] and (r["med"] or None) == v["med"] and id(r) not in used]
            if len(cands) > 1:
                key = e["nom"].split(" ")[-1] if e["nom"].startswith("Polytech") else e["nom"].split(" ")[0]
                cands = [r for r in cands if key.lower() in r["name"].lower()]
            if len(cands) != 1:
                raise SystemExit(f"Polytech : correspondance ambiguë pour {sid} / {v['lib']} : {[c['name'] for c in cands]}")
            used.add(id(cands[0]))
            st.append(V("POLY", cands[0]["name"], v["lib"]))
        ACC.setdefault(sid, []).append(dict({k: x for k, x in pc.items() if k != "stats"}, stats=st))
assert len(used) == len(poly_rows), f"lignes Polytech non utilisées : {[r['name'] for r in poly_rows if id(r) not in used]}"

# ---------------------------------------------------------------- e3a : écoles indépendantes
def IND(sid, p26, stats, fee, inter=False, txt=None, note=None):
    sc = "MP+MPI+PC+PSI" if inter else "PSI"
    n = " ".join(x for x in (note, NOTE_INTER if inter else None) if x) or None
    add(sid, A("e3a_ind", p26, stats, ["ccinp", fee], S_E3A, scope=sc, txt=txt, note=n))
PA = lambda name, lib: V("PA", name, lib, c25="Puissance Alpha")
IND("trois_il", 10, [PA("3iL Ingénieurs Limoges", "3iL")], "ind_3il", note=NOTE_PA)
IND("aflokkat", 20, [], "ind_aflokkat", inter=True, note="Nouvelle école sur e3a-Polytech en 2026 : pas de statistiques 2025.")
IND("efrei", 50, [PA("EFREI Paris", "EFREI Paris")], "ind_efrei", inter=True, note=NOTE_PA + " Les 50 places 2026 couvrent Paris et Bordeaux.")
IND("eia", 8, [V("AE", "EIA Bethune - Génie électrique", "EIA Béthune – génie électrique")], "ind_eia")
IND("eidd", 55, [V("EI", "EIDD Paris", "EIDD Paris")], "ind_eidd", inter=True)
IND("eijv", 11, [V("AE", "EIJV Amiens - Cybersécurité", "Cybersécurité (Amiens)"), V("AE", "EIJV - Génie Énergétique et Environnement", "Génie énergétique et environnement"),
                 V("AE", "EIJV - Technologie de l'Information pour la santé", "Technologies de l'information pour la santé"),
                 V("AE", "EIJV Saint Quentin - Logistique innovante", "Logistique innovante (Saint-Quentin)")], "ind_eijv",
    txt="Cybersécurité 1, supply chain et logistique 5, génie énergétique et environnement 3, numérique-santé-IA 2")
IND("eil", 32, [V("AE", "EIL Côte d'Opale - Calais (informatique)", "Calais – informatique"), V("AE", "EIL Côte d'Opale - Dunkerque (Génie Energétique et Environnement)", "Dunkerque – génie énergétique et environnement"),
                V("AE", "EIL Côte d'Opale - Saint-Omer (Génie Industriel)", "Saint-Omer – génie industriel"), V("AE", "EIL Côte d'Opale - Boulogne (Agroalimentaire)", "Boulogne – agroalimentaire")], "ind_eil",
    txt="Informatique 10, génie énergétique 8, génie industriel 12, agroalimentaire 2")
IND("elisa", 30, [PA("ELISA Aerospace Bordeaux", "Bordeaux"), PA("ELISA Aerospace Hauts de France", "Hauts-de-France")], "ind_elisa", inter=True, note=NOTE_PA)
IND("enit", 8, [V("AE", "ENIT Tarbes - UTTOP", "ENIT Tarbes – UTTOP")], "ind_enit")
IND("ensait", 12, [V("AE", "ENSAIT Roubaix", "ENSAIT Roubaix")], "ind_ensait")
IND("esaip", 24, [PA("ESAIP Angers / Aix-en-Provence", "ESAIP Angers / Aix-en-Provence")], "ind_esaip", inter=True, note=NOTE_PA)
IND("esb", 12, [V("AE", "ESB Nantes", "ESB Nantes")], "ind_esb")
IND("eseo", 20, [PA("ESEO Angers - Paris - Dijon", "ESEO Angers – Paris – Dijon")], "ind_eseo", inter=True, note=NOTE_PA)
IND("esiea", 5, [PA("ESIEA Paris - Laval", "ESIEA Paris – Laval")], "ind_esiea", note=NOTE_PA)
IND("estia", 28, [PA("ESTIA Bidart", "ESTIA Bidart")], "ind_estia", note=NOTE_PA)
add("imtne", A("e3a_ind", 20, [V("AE", "IMT Nord Europe (en partenariat avec ISPA)", "IMT Nord Europe (avec l'ISPA)")], ["ccinp", "ind_imtne"], S_E3A,
               lib="Formation en partenariat avec l'ISPA (plasturgie)"))
IND("isen_med", 6, [PA("ISEN Méditerranée Toulon", "ISEN Méditerranée Toulon")], "ind_isenmed", note=NOTE_PA)
IND("isen_ouest", 25, [PA("ISEN Ouest - Brest - Caen - Nantes", "ISEN Ouest Brest – Caen – Nantes")], "ind_isenouest", inter=True, note=NOTE_PA)
IND("isep", 30, [PA("ISEP", "ISEP")], "ind_isep", inter=True, note=NOTE_PA)
IND("ismans", 10, [V("AE", "ISMANS-Groupe CESI Le Mans", "ISMANS-Groupe CESI Le Mans")], "ind_ismans")
IND("hei", 20, [PA("HEI JUNIA – Lille", "HEI JUNIA Lille")], "ind_hei", note=NOTE_PA)
IND("isen_lille", 5, [PA("ISEN JUNIA Lille-BORDEAUX", "ISEN JUNIA Lille – Bordeaux")], "ind_isenlille", note=NOTE_PA)
IND("paolitech", 5, [V("AE", "Paoli Tech", "Paoli Tech")], "ind_paoli")

# ---------------------------------------------------------------- Avenir Prépas
F = ["ccinp", "avenir"]
add("builders", A("avenir", 12, [V("AV", "BUILDERS Caen", "Builders Caen")], F, S_E3A, lib="Campus de Caen"),
                A("avenir", 5, [V("AV", "BUILDERS Lyon", "Builders Lyon")], F, S_E3A, lib="Campus de Lyon"))
add("eigsi", A("avenir", 25, [V("AV", "EIGSI La Rochelle", "EIGSI La Rochelle")], F, S_E3A))
add("esigelec", A("avenir", 20, [V("AV", "ESIGELEC Rouen/Poitiers", "ESIGELEC Rouen / Poitiers")], F, S_E3A))
add("esilv", A("avenir", 67, [V("AV", "ESILV Paris", "ESILV Paris"), V("AV", "ESILV Paris FISEA Finance", "ESILV Paris – FISEA finance")], F, S_E3A,
               lib="Campus de Paris-La Défense", txt="63 en statut étudiant + 4 en apprentissage"),
             A("avenir", 10, [V("AV", "ESILV Nantes", "ESILV Nantes")], F, S_E3A, lib="Campus de Nantes"))
add("estaca", A("avenir", 4, [V("AV", "ESTACA Paris-Saclay - Filière Aéronautique", "Paris-Saclay – aéronautique"), V("AV", "ESTACA Paris-Saclay - Filière Automobile", "Paris-Saclay – automobile"),
                              V("AV", "ESTACA Paris-Saclay - Filière Ferroviaire", "Paris-Saclay – ferroviaire"), V("AV", "ESTACA Paris-Saclay - Filière Spatial", "Paris-Saclay – spatial")],
                F, S_E3A, lib="Campus de Paris-Saclay"),
              A("avenir", 9, [V("AV", "ESTACA Laval - Filière Aéronautique", "Laval – aéronautique"), V("AV", "ESTACA Laval - Filière Automobile", "Laval – automobile"),
                              V("AV", "ESTACA Laval - Filière Naval", "Laval – naval")], F, S_E3A, lib="Campus de Laval"),
              A("avenir", 23, [V("AV", "ESTACA Bordeaux - Filière Aéronautique", "Bordeaux – aéronautique")], F, S_E3A, lib="Campus de Bordeaux"))

# ---------------------------------------------------------------- Ingéni'Up, Groupe UT : voies communes à toutes les filières (copie de la PC)
for sid in ("ecam_epmi", "ecam_rennes", "icam", "unilasalle", "utc", "utt", "utbm"):
    for a in PC_ACCES[sid]:
        if a["c"] in ("ingeniup", "ut"):
            ACC.setdefault(sid, []).append(json.loads(json.dumps(a)))

# ---------------------------------------------------------------- EPITA-IPSA-ESME, CESI
def epi(sid, p26, rows):
    base = next(a for a in PC_ACCES[sid] if a["c"] == "epita")
    ACC.setdefault(sid, []).append(dict({k: v for k, v in base.items() if k != "stats"}, stats=[V("EP", n, l) for n, l in rows]))
epi("epita", 100, [("EPITA campus Paris", "Paris"), ("EPITA Paris - FISA", "Paris – apprentissage (FISA)"), ("EPITA campus Lyon", "Lyon"),
                   ("EPITA campus Rennes", "Rennes"), ("EPITA campus Strasbourg", "Strasbourg"), ("EPITA campus Toulouse", "Toulouse")])
epi("ipsa", 100, [("IPSA Paris", "Paris"), ("IPSA Paris - FISA", "Paris – apprentissage (FISA)"), ("IPSA Toulouse", "Toulouse")])
epi("esme", 50, [("ESME", "ESME"), ("ESME - FISA", "ESME – apprentissage (FISA)")])
cesi = next(a for a in PC_ACCES["cesi"] if a["c"] == "cesi")
ACC["cesi"] = [dict({k: v for k, v in cesi.items() if k != "stats"}, stats=[{"lib": "26 parcours et campus (2025)", "pl": 128, "int": 2, "med": None, "moy": None}],
                    note="Concours propre (maths, physique, anglais, français + entretien). En 2025, 2 élèves de PSI ont intégré le CESI par ce concours.")]

if __name__ == "__main__":
    out = sys.argv[1]
    open(out, "w", encoding="utf-8").write("# -*- coding: utf-8 -*-\n# Généré par tools/build_psi_acces.py (places PSI 2026 + statistiques SCEI PSI 2025)\n"
                                           "PSI_ACCES = " + pprint.pformat(ACC, width=170, sort_dicts=False) + "\n")
    n = sum(len(v) for v in ACC.values())
    print(len(ACC), "écoles,", n, "voies PSI")
