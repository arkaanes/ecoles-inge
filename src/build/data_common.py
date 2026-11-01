# -*- coding: utf-8 -*-
"""Common helpers and constants for the MP engineering-school dataset."""

REGIONS = {
    "idf": "Île-de-France", "ara": "Auvergne-Rhône-Alpes", "bfc": "Bourgogne-Franche-Comté",
    "bre": "Bretagne", "cvl": "Centre-Val de Loire", "cor": "Corse", "ges": "Grand Est",
    "hdf": "Hauts-de-France", "nor": "Normandie", "naq": "Nouvelle-Aquitaine",
    "occ": "Occitanie", "pdl": "Pays de la Loire", "pac": "Provence-Alpes-Côte d'Azur",
    "reu": "La Réunion",
}

DOMAINES = {
    "gen": "Généraliste",
    "info": "Informatique & numérique",
    "elec": "Électronique, télécoms & systèmes",
    "math": "Maths appliquées, data & finance",
    "meca": "Mécanique & conception",
    "energie": "Énergie & nucléaire",
    "aero": "Aéronautique & spatial",
    "btp": "Génie civil, BTP & ville",
    "chimie": "Chimie & procédés",
    "physique": "Physique, optique & matériaux",
    "bio": "Vivant, agro & santé",
    "env": "Environnement, eau & géosciences",
    "indus": "Génie industriel & logistique",
    "transport": "Transports (auto, ferroviaire, naval)",
    "defense": "Défense (écoles militaires)",
    "rech": "Recherche & enseignement (ENS)",
}

# ---------------------------------------------------------------- sources
def src(t, u):
    return {"t": t, "u": u}

S_SCEI25 = src("Statistiques SCEI MP 2025", "https://www.scei-concours.fr/stat2025/mp.html")
S_LOIC = src("Stat concours (loic.website, d'après le SCEI)", "https://loic.website/CPGE/statistique-integration-ecole-d-ingenieur-par-filiere-cpge-post-prepa.php")
S_FRAIS_SCEI = src("Frais de dossier MP 2026 (SCEI)", "https://www.scei-concours.fr/pdf/frais_MP2026.pdf")
S_X = src("Notice X-ESPCI 2026", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Notice%202026%20ESPCI_Fili%C3%A8res%20PC%20et%20MP.pdf")
S_CCMP26 = src("Notice des écoles Mines-Ponts 2026", "https://concoursminesponts.fr/wp-content/uploads/2025/12/notice-des-ecoles-2026-22.12.25.pdf")
S_CCMP_DI = src("Concours Mines-Ponts (Dimension Ingénieur)", "https://www.dimension-ingenieur.com/concours-mines-ponts/246")
S_CMT26 = src("Notice Mines-Télécom 2026", "https://cahier-de-prepa.fr/pc-descartes/download?id=260")
S_CCS26 = src("Concours Centrale-Supélec 2026 (Dimension Ingénieur)", "https://www.dimension-ingenieur.com/concours-centrale-supelec/196")
S_CCINP26 = src("CCINP 2026, mode d'emploi (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-commun-inp-mode-d-emploi.html")
S_E3A26 = src("e3a-Polytech 2026, mode d'emploi (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-e3a-polytech-mode-d-emploi.html")
S_E3A_DI = src("e3a-Polytech 2026 (Dimension Ingénieur)", "https://www.dimension-ingenieur.com/concours-e3a/198")
S_AV26 = src("Avenir Prépas 2026 (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-avenirprepa-mode-d-emploi.html")
S_IU26 = src("Ingéni'Up 2026 (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-ingeni-up-mode-d-emploi.html")
S_EP26 = src("Concours EPITA-IPSA-ESME 2026 (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-cpge-epita-ipsa-esme.html")
S_CESI26 = src("Concours CESI CPGE", "https://www.cesi.fr/concours-cesi-cpge/")
S_NAT = src("Tarifs 2026-2027 de l'ENSSAT (droit national 630 €)", "https://www.enssat.fr/uploads/site/documents/Brochures/Tarifs_2026-2027.pdf")
S_HAUSSE26 = src("Écoles qui augmentent leurs frais à la rentrée 2026 (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/quelles-ecoles-d-ingenieurs-augmentent-leurs-frais-a-la-rentree-et-pourquoi.html")
S_PGE26 = src("Combien coûte une école d'ingénieurs en 2026 (Planète Grandes Écoles)", "https://www.planetegrandesecoles.com/?p=128618")
S_ISAE = src("Le groupe ISAE rejoint le concours Mines-Télécom", "https://isae-supmeca.fr/wp-content/uploads/2024/11/2024-11-13-Groupe-ISAE-CP-integration-Concours-Mines-Telecom.pdf")
S_ENAC_CMT = src("L'ENAC rejoint le concours Mines-Télécom", "https://www.enac.fr/en/node/2926")
S_UT = src("UTC, voies d'admission 2026 (Onisep)", "https://www.onisep.fr/ressources/structures-enseignement/hauts-de-france/oise/universite-de-technologie-de-compiegne/diplome-d-ingenieur-de-l-universite-de-technologie-de-compiegne-specialite-informatique")
S_FORUM = src("Forum Futura-Sciences, « liste d'écoles concours »", "https://forums.futura-sciences.com/cpge/960431-liste-decoles-concours.html")
S_FORUM_INSA = src("Forum Futura-Sciences, « Insa »", "https://forums.futura-sciences.com/cpge/963592-insa.html")

def onisep(u):
    return src("Fiche Onisep", u)

# ---------------------------------------------------------------- fees
def frais(txt, mn=None, mx=None, an="", sources=None, fiab="Officiel", ref=None):
    """Tuition. mn/mx: numeric €/an for filtering (None if unknown). ref: representative value."""
    return {"txt": txt, "min": mn, "max": mx if mx is not None else mn,
            "ref": ref if ref is not None else mn, "an": an,
            "src": sources or [], "fiab": fiab}

def nat(extra=""):
    t = "630 €/an (droit national des écoles publiques, 2026-2027) + CVEC"
    if extra:
        t += ". " + extra
    return frais(t, 630, 630, "2026-2027", [S_NAT], "Règle nationale (montant officiel 2026-2027)")

def bours(cat, txt):
    # cat: exo (exonération totale), remu (gratuit et rémunéré), part (réduction), nd (non trouvé / à vérifier)
    return {"cat": cat, "txt": txt}

B_NAT = bours("exo", "Exonération des droits pour les boursiers (règle des écoles publiques) ; CVEC offerte aussi.")
B_PRIV = bours("nd", "École privée : pas d'exonération automatique ; bourses ou réductions propres à l'école, à vérifier.")
B_REMU = bours("remu", "Scolarité gratuite et élève rémunéré (statut militaire ou fonctionnaire).")

# ---------------------------------------------------------------- stats 2025 lines
def V(lib, pl, it, med=None, moy=None, cl=None, ins=None, inter=False, iint=None, c25=None, prev=None):
    """One 2025 SCEI line. pl places, it MP intégrés, med/moy rangs, cl classés, ins inscrits.
    inter: classement commun à plusieurs filières (places et rangs mélangent MP/PC/PSI...).
    c25: concours de 2025 si différent du concours 2026 de la voie.
    prev: ligne d'une formation précédente (même concours), donnée pour comparaison seulement."""
    d = {"lib": lib, "pl": pl, "int": it, "med": med or None, "moy": moy or None}
    if cl: d["cl"] = cl
    if ins: d["ins"] = ins
    if inter: d["inter"] = True
    if iint is not None: d["iint"] = iint
    if c25: d["c25"] = c25
    if prev: d["prev"] = prev
    return d

def A(c, p26, scope="MP", txt=None, stats=None, fee=None, lib=None, src26=None, note=None):
    """One access route for 2026."""
    d = {"c": c, "p26": p26, "scope": scope, "stats": stats or [], "fee": fee or []}
    if txt: d["txt"] = txt
    if lib: d["lib"] = lib
    if src26: d["src"] = src26
    if note: d["note"] = note
    return d

def C(ville, dept, reg):
    return {"v": ville, "d": dept, "r": reg}
