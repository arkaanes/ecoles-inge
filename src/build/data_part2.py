# -*- coding: utf-8 -*-
from data_common import *
from data_part1 import E

B_CENTRALE = bours("exo", "Boursiers exonérés (Planète Grandes Écoles 2026 : « exonérés dans tous les cas » pour les Centrales).")

SCHOOLS_2 = [
# ============================================================ Centrale-Supélec
E("cs", "CentraleSupélec", "CentraleSupélec (Université Paris-Saclay)", ["Centrale Paris", "Supélec", "ECP", "Paris-Saclay", "CS"],
  "Public", [C("Gif-sur-Yvette", "91", "idf"), C("Metz", "57", "ges"), C("Rennes", "35", "bre")], ["gen", "info", "elec", "energie"], "Généraliste",
  "Généraliste ; spécialités à Metz et Rennes (informatique, cybersécurité, électronique, énergie, physique)",
  frais("De 2 500 à 5 000 €/an selon le revenu des parents (entrants 2026)", 2500, 5000, "rentrée 2026",
        [src("CentraleSupélec : droits progressifs 2026 (communiqué)", "https://www.centralesupelec.fr/sites/default/files/communiques-de-presse/CentraleSupelec_251110_CP_Politiquesociale_CoutDesEtudes_VF_0.pdf")]),
  bours("exo", "Boursiers sur critères sociaux exonérés (communiqué de l'école)."),
  [A("ccs", 210, "MP", None, [V("Généraliste, Paris-Saclay (statut étudiant)", 223, 225, 340, 325, cl=995)], ["ccs_cs"], lib="Ingénieur généraliste, Paris-Saclay", src26=S_CCS26),
   A("ccs", 10, "MP", None, [V("Apprentis, campus de Metz", 3, 3, 670, 662, cl=995), V("Apprentis, campus de Rennes", 7, 7, 629, 648, cl=995)], ["ccs_cs"], lib="Ingénieur généraliste, apprentissage (Metz, Rennes)", src26=S_CCS26),
   A("ccs", 10, "MP", None, [V("Spécialité informatique (Metz)", 14, 7, 687, 644, cl=995)], ["ccs_cs"], lib="Spécialité informatique (Metz)", src26=S_CCS26),
   A("ccs", 5, "MP", None, [V("Spécialité physique (Metz)", 6, 4, 734, 712, cl=995)], ["ccs_cs"], lib="Spécialité génie physique (Metz)", src26=S_CCS26),
   A("ccs", 10, "MP", None, [V("Spécialité cybersécurité (Rennes)", 12, 5, 846, 789, cl=995)], ["ccs_cs"], lib="Spécialité cybersécurité (Rennes)", src26=S_CCS26),
   A("ccs", 4, "MP", None, [V("Spécialité électronique (Rennes/Paris-Saclay)", 4, 3, 679, 631, cl=995)], ["ccs_cs"], lib="Spécialité électronique (Rennes, Paris-Saclay)", src26=S_CCS26),
   A("ccs", 5, "MP", None, [V("Spécialité énergie – génie électrique (Rennes)", 6, 3, 743, 651, cl=995)], ["ccs_cs"], lib="Spécialité génie électrique (Rennes)", src26=S_CCS26),
   A("ccs", 10, "MP", None, [V("Spécialité systèmes numériques (Rennes)", 11, 4, 800, 769, cl=995)], ["ccs_cs"], lib="Spécialité systèmes numériques (Rennes)", src26=S_CCS26)]),

E("centralelyon", "Centrale Lyon", "École centrale de Lyon", ["ECL", "École centrale de Lyon"],
  "Public", [C("Écully", "69", "ara")], ["gen"], "Généraliste", "Généraliste",
  frais("De 1 613 à 4 113 €/an selon les revenus de la famille (rentrée 2026 ; 2 613 € en 2025)", 1613, 4113, "rentrée 2026", [S_HAUSSE26]),
  B_CENTRALE,
  [A("ccs", 127, "MP", None, [V("Centrale Lyon", 127, 127, 665, 658, cl=1042)], ["ccs_lyon"], src26=S_CCS26)]),

E("centralelille", "Centrale Lille", "École centrale de Lille (Centrale Lille Institut)", ["ECLi", "Centrale Lille Institut", "École centrale de Lille"],
  "Public", [C("Villeneuve-d'Ascq", "59", "hdf")], ["gen"], "Généraliste", "Généraliste",
  frais("De 1 500 à 4 500 €/an selon les revenus (nouveaux élèves 2026)", 1500, 4500, "rentrée 2026", [S_HAUSSE26]),
  B_CENTRALE,
  [A("ccs", 90, "MP", None, [V("Centrale Lille", 90, 84, 877, 844, cl=1091)], ["ccs_lille"], src26=S_CCS26)]),

E("centralenantes", "Centrale Nantes", "École centrale de Nantes", ["ECN", "École centrale de Nantes"],
  "Public", [C("Nantes", "44", "pdl")], ["gen", "meca", "btp", "energie"], "Généraliste",
  "Généraliste ; points forts en mécanique, génie civil, énergie, robotique, maritime",
  frais("Modulés selon la tranche d'imposition des parents dès 2026 (ex. 4 770 €/an pour une tranche à 30 %) ; 2 613 € en 2025-2026", None, None, "rentrée 2026",
        [src("Centrale Nantes (Hadamard, d'après la grille officielle)", "https://www.hadamard.fr/ecoles/centrale-nantes")], "Secondaire (Hadamard)", ref=4770),
  bours("exo", "Boursiers CROUS et pupilles totalement exonérés."),
  [A("ccs", 110, "MP", None, [V("Centrale Nantes", 110, 110, 802, 774, cl=1160)], ["ccs_nantes"], src26=S_CCS26)]),

E("centralemed", "Centrale Méditerranée", "Centrale Méditerranée (ex-Centrale Marseille)", ["Centrale Marseille", "ECM"],
  "Public", [C("Marseille", "13", "pac"), C("Nice", "06", "pac")], ["gen"], "Généraliste", "Généraliste",
  frais("2 613 €/an en 2025-2026 ; modulés selon les revenus à partir de 2026-2027 (montants non publiés dans nos sources)", 2613, None, "2025-2026",
        [src("Centrale Méditerranée (Hadamard)", "https://www.hadamard.fr/ecoles/centrale-marseille")], "Secondaire (Hadamard)"),
  bours("exo", "Exonération totale pour les boursiers CROUS."),
  [A("ccs", 90, "MP", None, [V("Centrale Méditerranée", 90, 91, 903, 870, cl=1158)], ["ccs_med"], src26=S_CCS26)],
  note="Nouveau nom (ex-Centrale Marseille) ; campus de Nice ouvert en 2023."),

E("ensam", "Arts et Métiers", "Arts et Métiers (École nationale supérieure d'arts et métiers)", ["ENSAM", "Arts et Métiers ParisTech", "Gadzarts", "AM"],
  "Public", [C("Paris 13e", "75", "idf"), C("Aix-en-Provence", "13", "pac"), C("Angers", "49", "pdl"), C("Bordeaux-Talence", "33", "naq"),
             C("Châlons-en-Champagne", "51", "ges"), C("Cluny", "71", "bfc"), C("Lille", "59", "hdf"), C("Metz", "57", "ges")],
  ["meca", "indus", "energie"], "Généraliste", "Génie mécanique, industriel et énergétique ; 8 campus",
  frais("Droit national : 630 €/an en 2026-2027 (618 € en 2024-2025) ; l'école réfléchit à une hausse", 630, 630, "2026-2027",
        [src("Arts et Métiers (Hadamard)", "https://www.hadamard.fr/ecoles/arts-et-metiers"), S_HAUSSE26], "Secondaire + règle nationale"),
  bours("exo", "Boursiers CROUS totalement exonérés. Apprentissage gratuit."),
  [A("ccs", 53, "MP", "53 places MP, étudiants et apprentis, 8 campus confondus", [
      V("Statut étudiant", 53, 50, 649, 609, cl=800), V("Apprentissage", 2, 3, 481, 497, cl=800)], ["ccs_amensea"], src26=S_CCS26)]),

E("ensea", "ENSEA", "École nationale supérieure de l'électronique et de ses applications", ["ENSEA"],
  "Public", [C("Cergy", "95", "idf")], ["elec", "info"], "Spécialisée", "Électronique, informatique, télécoms, systèmes embarqués",
  nat(), B_NAT,
  [A("ccs", 60, "MP", None, [V("ENSEA Cergy", 60, 73, 1327, 1303, cl=1460)], ["ccs_amensea"], src26=S_CCS26,
     note="Inscription couplée avec Arts et Métiers (135 €) ; oraux propres à l'ENSEA.")]),

E("navale", "École navale", "École navale", ["Navale", "EN"],
  "Public (militaire)", [C("Lanvéoc (Brest)", "29", "bre")], ["defense", "transport", "meca", "elec"], "Généraliste",
  "Officier de marine : ingénierie navale, énergie, systèmes",
  frais("Gratuit : élève-officier rémunéré", 0, 0, "", [], "Statut militaire"), B_REMU,
  [A("ccs", 31, "MP", None, [V("École navale", 32, 32, 34, 32, cl=125)], ["ccs_navale"], src26=S_CCS26,
     note="Épreuves propres (oraux, sport, aptitude médicale) : rangs sur un petit nombre de classés.")]),

E("iogs", "SupOptique", "Institut d'Optique Graduate School", ["SupOptique", "IOGS", "Institut d'Optique"],
  "Fondation reconnue d'utilité publique", [C("Palaiseau", "91", "idf"), C("Saint-Étienne", "42", "ara"), C("Bordeaux-Talence", "33", "naq")],
  ["physique"], "Spécialisée", "Optique, photonique ; 1re année à Palaiseau",
  frais("3 200 €/an (UE, 2025-2026)", 3200, 3200, "2025-2026", [src("Institut d'Optique (Hadamard)", "https://www.hadamard.fr/ecoles/institut-optique")], "Secondaire (d'après le PDF officiel 2025-2026)"),
  bours("part", "Tarif réduit de 1 280 à 2 400 € selon l'échelon ; pas d'exonération totale."),
  [A("ccs", 32, "MP", None, [V("SupOptique", 32, 36, 581, 532, cl=752)], ["ccs_iogs"], src26=S_CCS26)]),

E("agroparistech", "AgroParisTech", "AgroParisTech (Institut des sciences et industries du vivant et de l'environnement)", ["AgroParisTech", "INA P-G"],
  "Public", [C("Palaiseau", "91", "idf")], ["bio", "env", "chimie"], "Spécialisée", "Vivant, agronomie, alimentation, environnement",
  frais("1 990 €/an (2025-2026)", 1990, 1990, "2025-2026", [src("AgroParisTech (Hadamard)", "https://www.hadamard.fr/ecoles/agroparistech")], "Officiel (arrêté du 1er août 2025, relayé)"),
  bours("exo", "Boursiers exonérés."),
  [A("ccs", 10, "MP", None, [V("AgroParisTech", 10, 12, 307, 288, cl=346)], ["ccs_agro"], src26=S_CCS26)]),

E("epf", "EPF", "EPF École d'ingénieurs", ["EPF", "École polytechnique féminine"],
  "Privé", [C("Cachan", "94", "idf"), C("Troyes", "10", "ges"), C("Montpellier", "34", "occ"), C("Saint-Nazaire", "44", "pdl")],
  ["gen"], "Généraliste", "Généraliste ; 4 campus",
  frais("9 880 €/an (2026)", 9880, 9880, "2026", [onisep("https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/val-de-marne/epf-ecole-d-ingenieurs-generalistes-site-de-paris-cachan/diplome-d-ingenieur-de-l-epf")]),
  B_PRIV,
  [A("ccs", 51, "MP", "Cachan, Montpellier, Saint-Nazaire et Troyes, statut étudiant ou apprenti", [
      V("Cachan", 8, 8, 191, 184, cl=255), V("Montpellier", 8, 1, 202, 202, cl=255),
      V("Saint-Nazaire", 8, 1, 195, 195, cl=255), V("Troyes", 10, 2, 221, 221, cl=255)], ["ccs_epf"],
     src26=src("Concours Centrale-Supélec 2026, places par filière (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-centrale-supelec-mode-d-emploi.html"),
     note="Oral non scientifique : deux ateliers collectifs et un entretien de motivation, sur une demi-journée (notice Centrale-Supélec 2026).")]),

E("estp", "ESTP", "ESTP, grande école d'ingénieurs de la construction", ["ESTP", "ESTP Paris", "École spéciale des travaux publics"],
  "Privé", [C("Cachan", "94", "idf"), C("Dijon", "21", "bfc"), C("Orléans", "45", "cvl"), C("Troyes", "10", "ges")],
  ["btp"], "Spécialisée", "Construction, BTP, travaux publics",
  frais("9 950 €/an (promotion 2026)", 9950, 9950, "2026", [], "Secondaire (sites agrégateurs, à confirmer)"),
  bours("part", "Réduction de 8 à 50 % selon l'échelon CROUS ; 1re année gratuite pour les mieux classés."),
  [A("ccs", 135, "MP", "Cachan 110, Dijon 10, Orléans 5, Troyes 10", [
      V("Cachan", 100, 97, 606, 590, cl=815), V("Dijon", 10, 6, 592, 624, cl=815),
      V("Orléans", 10, 2, 762, 762, cl=815), V("Troyes", 10, 1, 364, 364, cl=815)], ["ccs_estp"],
     src26=src("Concours Centrale-Supélec 2026, places par filière (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-centrale-supelec-mode-d-emploi.html"))]),
]

# Arts et Métiers : campus de 1re année et règles d'affectation (MP, PC, PSI)
ENSAM_AFF = {'y1': ['Aix-en-Provence', 'Angers'], 'later': '2e ou 3e année, selon le parcours', 'regle': ["Le campus est attribué après l'admission, pas au moment des vœux.", "Les 10 % premiers classés de la filière choisissent leur campus. Pour les autres : places restantes, campus de référence s'il est dans tes 2 premiers vœux, rang, puis vœux.", 'Pas de 1re année à Paris en statut étudiant. En apprentissage, tout le cursus se fait à Angers ou à Paris.', 'Une fois affecté, pas de changement sauf force majeure.'], 'src': [{'t': 'Affectations (Arts et Métiers)', 'u': 'https://artsetmetiers.fr/fr/formation/affectations'}, {'t': 'Campus de 1re année en MP, PC, PSI (Onisep, 2026)', 'u': 'https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/paris/ecole-nationale-superieure-d-arts-et-metiers-campus-arts-et-metiers-de-paris/diplome-d-ingenieur-de-l-ecole-nationale-superieure-d-arts-et-metiers'}]}
for _s in SCHOOLS_2:
    if _s["id"] == "ensam":
        _s["aff"] = ENSAM_AFF
