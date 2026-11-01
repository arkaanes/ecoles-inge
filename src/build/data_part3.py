# -*- coding: utf-8 -*-
from data_common import *
from data_part1 import E

CL = 4075  # classés CCINP MP 2025

def cc(lib, pl, it, med, moy):
    return V(lib, pl, it, med, moy, cl=CL)

SCHOOLS_3 = [
# ============================================================ CCINP
E("ensc", "ENSC (Bordeaux INP)", "École nationale supérieure de cognitique (Bordeaux INP)", ["ENSC", "Bordeaux INP", "cognitique"],
  "Public", [C("Talence", "33", "naq")], ["info", "bio"], "Spécialisée", "Cognitique : facteurs humains, IA, interaction humain-machine",
  nat(), B_NAT, [A("ccinp", 10, "MP", None, [cc("ENSC", 10, 12, 3266, 3168)], ["ccinp"], src26=S_CCINP26)]),

E("enseirb", "ENSEIRB-MATMECA", "ENSEIRB-MATMECA (Bordeaux INP)", ["ENSEIRB", "MATMECA", "Bordeaux INP"],
  "Public", [C("Talence", "33", "naq")], ["info", "elec", "math", "meca"], "Spécialisée",
  "Informatique, électronique, télécoms, maths et mécanique",
  nat(), B_NAT, [A("ccinp", 106, "MP", "Toutes filières de l'école (électronique, informatique, maths-méca, télécoms)", [
      cc("Électronique", 26, 22, 2376, 2353), cc("Informatique", 41, 38, 1843, 1828),
      cc("Mathématiques et mécanique", 36, 23, 2062, 1916), cc("Télécommunications", 17, 17, 2492, 2481)], ["ccinp"], src26=S_CCINP26)]),

E("enspima", "ENSPIMA (Bordeaux INP)", "École nationale supérieure pour la performance industrielle et la maintenance aéronautique", ["ENSPIMA", "Bordeaux INP"],
  "Public", [C("Mérignac", "33", "naq")], ["aero", "indus"], "Spécialisée", "Maintenance et performance industrielle aéronautique",
  nat(), B_NAT, [A("ccinp", 4, "MP", None, [cc("ENSPIMA", 4, 5, 2500, 2483)], ["ccinp"], src26=S_CCINP26)]),

E("isima", "ISIMA (Clermont Auvergne INP)", "Institut d'informatique d'Auvergne (Clermont Auvergne INP)", ["ISIMA", "Clermont Auvergne INP"],
  "Public", [C("Aubière (Clermont-Ferrand)", "63", "ara")], ["info", "math"], "Spécialisée", "Informatique, modélisation, data",
  nat(), B_NAT, [A("ccinp", 39, "MP", None, [cc("ISIMA", 42, 29, 2996, 2940)], ["ccinp"], src26=S_CCINP26)]),

E("sigma", "SIGMA Clermont", "SIGMA Clermont (Clermont Auvergne INP)", ["SIGMA", "IFMA", "Clermont Auvergne INP"],
  "Public", [C("Aubière (Clermont-Ferrand)", "63", "ara")], ["meca", "chimie"], "Spécialisée", "Mécanique, chimie",
  nat(), B_NAT, [A("ccinp", 20, "MP", None, [cc("Mécanique", 16, 14, 2865, 2720)], ["ccinp"], src26=S_CCINP26)]),

E("cpe", "CPE Lyon", "École supérieure de chimie physique électronique de Lyon", ["CPE", "ETI"],
  "Privé", [C("Villeurbanne", "69", "ara")], ["elec", "info", "chimie"], "Spécialisée", "Électronique, télécoms, informatique (ETI) ; chimie",
  frais("Environ 8 950 €/an (source non officielle, année non précisée) ; gratuit en apprentissage", 8950, 8950, "?", [src("Diplomeo", "https://diplomeo.com/diplomes/199339")], "Non officiel, à vérifier"),
  B_PRIV,
  [A("ccinp", 15, "MP", None, [cc("Électronique, télécoms, informatique (ETI)", 15, 5, 3315, 3317)], ["ccinp"], src26=S_CCINP26),
   A("bccinp", 5, "MP", None, [V("Apprentissage – physique et systèmes microélectroniques", 5, 0, None, None, cl=14)], ["ccinp", "b_cpe"],
     lib="Apprentissage (banque CCINP)", src26=S_CCINP26)]),

E("cytech", "CY Tech", "CY Tech (CY Cergy Paris Université, ex-EISTI)", ["EISTI", "CY Cergy Paris Université"],
  "Public", [C("Cergy", "95", "idf"), C("Pau", "64", "naq")], ["info", "math", "btp"], "Spécialisée", "Informatique, mathématiques appliquées, génie civil",
  frais("3 658 €/an (2026) ; gratuit en apprentissage", 3658, 3658, "2026", [onisep("https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/val-d-oise/cy-tech-campus-de-cergy-cy-cergy-paris-universite/diplome-d-ingenieur-de-cy-tech-de-cy-cergy-paris-universite-specialite-informatique")]),
  bours("nd", "Tarif boursier non indiqué par Onisep."),
  [A("ccinp", 84, "MP", "Cergy et Pau, toutes spécialités (dont 40 en informatique d'après Onisep)", [
      cc("Génie civil", 10, 4, 3974, 3905), cc("Informatique", 40, 35, 3656, 3596), cc("Mathématiques", 45, 27, 3426, 3462)], ["ccinp"], src26=S_CCINP26,
     note="Le chiffre de 40 places d'Onisep ne concerne que l'informatique : il n'y a pas de contradiction avec les 84 places.")]),

E("engees", "ENGEES", "École nationale du génie de l'eau et de l'environnement de Strasbourg", ["ENGEES"],
  "Public", [C("Strasbourg", "67", "ges")], ["env", "btp"], "Spécialisée", "Eau, environnement, infrastructures",
  frais("1 990 €/an au taux plein (2025) ; fonctionnaires et apprentis : gratuit", 1990, 1990, "2025", [onisep("https://www.onisep.fr/ressources/structures-enseignement/grand-est/bas-rhin/ecole-nationale-du-genie-de-l-eau-et-de-l-environnement-de-strasbourg/diplome-d-ingenieur-de-l-ecole-nationale-du-genie-de-l-eau-et-de-l-environnement-de-strasbourg")]),
  bours("nd", "Non précisé par Onisep (même barème que les écoles du ministère de l'Agriculture, comme AgroParisTech dont les boursiers sont exonérés)."),
  [A("ccinp", 14, "MP", None, [cc("Statut étudiant", 9, 14, 3636, 3324), cc("Fonctionnaires", 4, 3, 3279, 3463), cc("Apprentissage", 1, 1, 4011, 4011)], ["ccinp"], src26=S_CCINP26)]),

E("ensai", "ENSAI", "École nationale de la statistique et de l'analyse de l'information", ["ENSAI", "GENES", "Insee"],
  "Public", [C("Bruz (Rennes)", "35", "bre")], ["math", "info"], "Spécialisée", "Statistique, data science, IA",
  frais("Environ 2 650 €/an (indicatif, Campus France) ; voie fonctionnaire (attachés de l'Insee) à part", 2650, 2650, "?", [src("Campus France, fiche ENSAI", "https://ressources.campusfrance.org/pratique/etablissements/fr/ing_ensai_fr.pdf")], "Secondaire, à vérifier"),
  bours("nd", "Non indiqué."),
  [A("ccinp", 64, "MP", None, [cc("Civils", 45, 47, 1801, 1715), cc("Fonctionnaires (attachés de l'Insee)", 20, 20, 2350, 2221)], ["ccinp"], src26=S_CCINP26)]),

E("enscl", "ENSCL", "École nationale supérieure de chimie de Lille (Centrale Lille Institut)", ["ENSC Lille", "Chimie Lille", "Centrale Lille Institut"],
  "Public", [C("Villeneuve-d'Ascq", "59", "hdf")], ["chimie"], "Spécialisée", "Chimie, génie chimique",
  frais("Non trouvé", None, None, "", [], "À vérifier"), bours("nd", "Non trouvé."),
  [A("ccinp", 2, "MP", None, [cc("ENSC Lille", 2, 0, None, None)], ["ccinp"], src26=S_CCINP26)]),

E("ensgti", "ENSGTI", "École nationale supérieure en génie des technologies industrielles (Université de Pau)", ["ENSGTI", "UPPA"],
  "Public", [C("Pau", "64", "naq")], ["energie", "chimie"], "Spécialisée", "Énergétique, génie des procédés",
  nat(), B_NAT, [A("ccinp", 15, "MP", None, [cc("Énergétique", 15, 15, 3583, 3474)], ["ccinp"], src26=S_CCINP26)]),

E("ensip", "ENSI Poitiers", "École nationale supérieure d'ingénieurs de Poitiers (ENSIP)", ["ENSIP", "Université de Poitiers"],
  "Public", [C("Poitiers", "86", "naq")], ["energie", "env", "btp"], "Spécialisée", "Énergie, eau, génie civil, environnement",
  nat(), B_NAT, [A("ccinp", 25, "MP", None, [cc("Génie de l'eau et génie civil", 8, 6, 3403, 3418), cc("Énergétique et environnement", 17, 16, 3877, 3518)], ["ccinp"], src26=S_CCINP26)]),

E("ensicaen", "ENSICAEN", "École nationale supérieure d'ingénieurs de Caen", ["ENSI Caen"],
  "Public", [C("Caen", "14", "nor")], ["info", "elec", "physique"], "Spécialisée", "Informatique, électronique, génie physique (dont nucléaire), matériaux",
  frais("630 €/an (droit national 2026-2027) + CVEC", 630, 630, "2026-2027", [S_NAT, src("Règlement de scolarité FISE 2026-2027 (ENSICAEN)", "https://www.ensicaen.fr/wp-content/uploads/2026/09/FISE-Reglement-scolarite-FISE-2026-2027-Cursus-ingenieur-FISE.pdf")], "Règle nationale"),
  B_NAT, [A("ccinp", 58, "MP", None, [cc("Génie physique et systèmes embarqués", 26, 26, 2889, 2714), cc("Informatique", 32, 24, 2597, 2530)], ["ccinp"], src26=S_CCINP26)]),

E("ensil", "ENSIL-ENSCI", "ENSIL-ENSCI (Université de Limoges)", ["ENSIL", "ENSCI", "Université de Limoges"],
  "Public", [C("Limoges", "87", "naq")], ["elec", "meca", "physique", "env", "btp"], "Spécialisée",
  "Céramiques, électronique-télécoms, génie civil, eau-environnement, matériaux, mécatronique, photonique",
  nat(), B_NAT, [A("ccinp", 38, "MP", None, [
      cc("Céramique industrielle", 4, 0, None, None), cc("Électronique et télécoms", 10, 8, 3877, 3841), cc("Génie civil", 4, 0, None, None),
      cc("Génie de l'eau et environnement", 8, 1, 4014, 4014), cc("Matériaux", 4, 2, 3736, 3736), cc("Mécatronique", 6, 5, 3183, 3118),
      cc("Photonique", 3, 2, 3502, 3502)], ["ccinp"], src26=S_CCINP26)]),

E("ense3", "Grenoble INP - Ense3", "École nationale supérieure de l'énergie, l'eau et l'environnement (Grenoble INP-UGA)", ["Ense3", "ENSE3", "Grenoble INP"],
  "Public", [C("Grenoble", "38", "ara")], ["energie", "env", "elec"], "Spécialisée", "Énergie (dont nucléaire), eau, environnement, génie électrique",
  nat(), B_NAT, [A("ccinp", 60, "MP", None, [cc("Ense3", 65, 50, 2194, 2129)], ["ccinp"], src26=S_CCINP26)]),

E("ensimag", "Grenoble INP - Ensimag", "École nationale supérieure d'informatique et de mathématiques appliquées (Grenoble INP-UGA)", ["Ensimag", "Grenoble INP"],
  "Public", [C("Saint-Martin-d'Hères (Grenoble)", "38", "ara")], ["info", "math"], "Spécialisée", "Informatique, maths appliquées, finance",
  nat(), B_NAT, [A("ccinp", 110, "MP", None, [cc("Ensimag", 110, 110, 627, 596)], ["ccinp"], src26=S_CCINP26)]),

E("esisar", "Grenoble INP - Esisar", "École nationale supérieure des systèmes avancés et réseaux (Grenoble INP-UGA)", ["Esisar", "Grenoble INP"],
  "Public", [C("Valence", "26", "ara")], ["elec", "info"], "Spécialisée", "Systèmes embarqués, réseaux, cybersécurité",
  nat(), B_NAT, [A("ccinp", 14, "MP", None, [cc("Esisar", 12, 9, 2740, 2560)], ["ccinp"], src26=S_CCINP26)]),

E("pagora", "Grenoble INP - Pagora", "École internationale du papier, de la communication imprimée et des biomatériaux (Grenoble INP-UGA)", ["Pagora", "Grenoble INP"],
  "Public", [C("Saint-Martin-d'Hères (Grenoble)", "38", "ara")], ["chimie", "physique"], "Spécialisée", "Biomatériaux, papier, emballage, impression",
  nat(), B_NAT, [A("ccinp", 10, "MP", None, [cc("Pagora", 10, 5, 3584, 3437)], ["ccinp"], src26=S_CCINP26)]),

E("phelma", "Grenoble INP - Phelma", "École nationale supérieure de physique, électronique, matériaux (Grenoble INP-UGA)", ["Phelma", "Grenoble INP"],
  "Public", [C("Grenoble", "38", "ara")], ["physique", "elec", "energie"], "Spécialisée",
  "Physique, électronique, matériaux, procédés ; filière génie énergétique et nucléaire (GEN) accessible depuis PMP",
  nat(), B_NAT, [A("ccinp", 86, "MP", "PET + PMP", [
      cc("PMP – physique, matériaux, procédés (mène notamment au nucléaire)", 35, 37, 1111, 1047),
      cc("PET – physique, électronique, télécoms", 54, 36, 1767, 1640)], ["ccinp"], src26=S_CCINP26,
     note="Deux voies très différentes en sélectivité : regarde la ligne qui t'intéresse.")]),

E("ensem", "Lorraine INP - ENSEM", "École nationale supérieure d'électricité et de mécanique (Lorraine INP)", ["ENSEM", "Lorraine INP"],
  "Public", [C("Vandœuvre-lès-Nancy", "54", "ges")], ["energie", "elec"], "Spécialisée", "Énergie, génie électrique, systèmes numériques",
  nat(), B_NAT, [A("ccinp", 52, "MP", None, [cc("Énergie", 36, 35, 3440, 3398), cc("Systèmes numériques", 20, 24, 3391, 3280)], ["ccinp"], src26=S_CCINP26)]),

E("ensic", "Lorraine INP - ENSIC", "École nationale supérieure des industries chimiques (Lorraine INP)", ["ENSIC", "Lorraine INP"],
  "Public", [C("Nancy", "54", "ges")], ["chimie"], "Spécialisée", "Génie chimique, procédés",
  nat(), B_NAT, [A("ccinp", 6, "MP", None, [cc("ENSIC", 6, 7, 3499, 3495)], ["ccinp"], src26=S_CCINP26)]),

E("seatech", "SeaTech", "SeaTech (Université de Toulon)", ["SeaTech", "Université de Toulon"],
  "Public", [C("La Garde (Toulon)", "83", "pac")], ["meca", "elec", "physique"], "Spécialisée", "Ingénierie marine : matériaux, mécanique, systèmes",
  nat(), B_NAT, [A("ccinp", 23, "MP", None, [cc("SeaTech", 23, 19, 2889, 2747)], ["ccinp"], src26=S_CCINP26)]),

E("supmicrotech", "SUPMICROTECH-ENSMM", "SUPMICROTECH-ENSMM (École nationale supérieure de mécanique et des microtechniques)", ["ENSMM", "SUPMICROTECH"],
  "Public", [C("Besançon", "25", "bfc")], ["meca", "elec"], "Spécialisée", "Microtechniques, mécanique, mécatronique",
  frais("630 €/an (droit national 2026-2027) + CVEC", 630, 630, "2026-2027", [S_NAT, src("Délibération droits d'inscription 2026-2027 (SUPMICROTECH)", "https://www.supmicrotech.fr/sites/default/files/public/CONTENT/DOCUMENTS/D%C3%A9lib.11-CA20260702-Droits%20inscription%202026-2027.pdf")], "Règle nationale"),
  B_NAT, [A("ccinp", 40, "MP", None, [cc("SUPMICROTECH-ENSMM", 40, 40, 3380, 3213)], ["ccinp"], src26=S_CCINP26)]),

E("n7", "Toulouse INP - ENSEEIHT", "École nationale supérieure d'électrotechnique, d'électronique, d'informatique, d'hydraulique et des télécommunications (Toulouse INP)",
  ["N7", "ENSEEIHT", "Toulouse INP"], "Public", [C("Toulouse", "31", "occ")], ["info", "elec", "energie", "math"], "Spécialisée",
  "Numérique, électronique-énergie-automatique, mécanique des fluides",
  nat(), B_NAT, [A("ccinp", 130, "MP", None, [
      cc("Électronique, énergie, automatique (EEA)", 35, 35, 1455, 1362),
      cc("Mécanique des fluides, énergétique, environnement (MFEE)", 15, 14, 987, 963),
      cc("Sciences du numérique (SN)", 80, 75, 1192, 1187)], ["ccinp"], src26=S_CCINP26)]),

E("ensiacet", "Toulouse INP - ENSIACET", "École nationale supérieure des ingénieurs en arts chimiques et technologiques (Toulouse INP)", ["A7", "ENSIACET", "Toulouse INP"],
  "Public", [C("Toulouse", "31", "occ")], ["chimie", "indus"], "Spécialisée", "Génie des procédés, chimie, matériaux, génie industriel",
  nat(), B_NAT, [A("ccinp", 28, "MP", None, [cc("Génie des procédés", 11, 8, 2695, 2716), cc("Génie industriel", 17, 13, 2455, 2508)], ["ccinp"], src26=S_CCINP26)]),

# ============================================================ Banque CCINP
E("enise", "Centrale Lyon ENISE", "École nationale d'ingénieurs de Saint-Étienne de Centrale Lyon", ["ENISE", "Centrale Lyon"],
  "Public", [C("Saint-Étienne", "42", "ara")], ["meca", "btp", "physique"], "Spécialisée", "Génie mécanique, génie civil, génie physique",
  frais("Non trouvé", None, None, "", [], "À vérifier"), bours("nd", "Non trouvé."),
  [A("bccinp", 10, "MP", None, [], ["ccinp", "b_enise"], src26=S_CCINP26, note="Nouveau en banque CCINP pour les MP en 2026 : pas de ligne dans les stats 2025.")]),

E("air", "École de l'air et de l'espace", "École de l'air et de l'espace (Salon-de-Provence)", ["EAE", "École de l'air", "Salon"],
  "Public (militaire)", [C("Salon-de-Provence", "13", "pac")], ["aero", "defense"], "Spécialisée", "Officier de l'armée de l'air et de l'espace : aéronautique, spatial",
  frais("Gratuit : élève-officier rémunéré", 0, 0, "", [], "Statut militaire"), B_REMU,
  [A("bccinp", 24, "MP", None, [V("Base", 5, 5, 35, 32, cl=75), V("Mécanique", 5, 5, 36, 33, cl=69), V("Pilote", 15, 15, 14, 15, cl=77)], ["ccinp", "b_air"], src26=S_CCINP26,
     note="Épreuves propres (sport, aptitude médicale, entretien) : rangs sur un petit nombre de classés.")]),

E("ensar", "ENSAR (Université de Poitiers)", "École nationale supérieure des sciences applicatives et du risque (ex-ENSRD)", ["ENSAR", "ENSRD", "IRIAF", "Université de Poitiers"],
  "Public", [C("Niort", "79", "naq")], ["math", "info", "env"], "Spécialisée", "Gestion des risques, data, cybersécurité, environnement",
  nat(), B_NAT, [A("bccinp", 3, "MP", None, [V("ENSAR (campus de Niort)", 8, 2, 14, 14, cl=89)], ["ccinp", "b_ensar"], src26=S_CCINP26)]),

E("ensisa", "ENSISA", "École nationale supérieure d'ingénieurs Sud-Alsace (Université de Haute-Alsace)", ["ENSISA", "UHA"],
  "Public", [C("Mulhouse", "68", "ges")], ["info", "elec", "meca", "physique"], "Spécialisée", "Automatique, informatique, mécanique, textile",
  nat(), B_NAT, [A("bccinp", 15, "MP", None, [
      V("Automatique et systèmes embarqués", 3, 6, 97, 89, cl=130), V("Informatique et réseaux", 5, 11, 74, 69, cl=130),
      V("Mécanique", 5, 5, 69, 68, cl=130), V("Textile et fibres", 2, 2, 59, 59, cl=130)], ["ccinp", "b_ensisa"], src26=S_CCINP26)]),

E("eost", "EOST", "École et observatoire des sciences de la Terre (Université de Strasbourg)", ["EOST", "Université de Strasbourg"],
  "Public", [C("Strasbourg", "67", "ges")], ["env", "physique"], "Spécialisée", "Géophysique",
  nat(), B_NAT, [A("bccinp", 12, "MP", None, [V("EOST", 12, 6, 16, 18, cl=44)], ["ccinp", "b_eost"], src26=S_CCINP26)]),

E("esm", "Saint-Cyr Coëtquidan", "École spéciale militaire de Saint-Cyr", ["ESM", "Saint-Cyr"],
  "Public (militaire)", [C("Guer", "56", "bre")], ["defense", "gen"], "Généraliste", "Officier de l'armée de terre",
  frais("Gratuit : élève-officier rémunéré", 0, 0, "", [], "Statut militaire"), B_REMU,
  [A("bccinp", 31, "MP", None, [V("ESM Saint-Cyr", 33, 33, 38, 37, cl=70)], ["ccinp", "b_esm"], src26=S_CCINP26)]),

E("esiee", "ESIEE Paris", "ESIEE Paris (Université Gustave Eiffel)", ["ESIEE", "Université Gustave Eiffel"],
  "Consulaire (CCI), composante de l'Université Gustave Eiffel", [C("Noisy-le-Grand", "93", "idf")], ["info", "elec", "energie"], "Spécialisée",
  "Informatique, électronique, systèmes embarqués, data, énergie",
  frais("8 680 €/an (2026-2027)", 8680, 8680, "2026-2027", [src("Modalités d'admission CPGE (ESIEE Paris)", "https://www.esiee.fr/fileadmin/user_upload/Fichiers/admissions/modalites-admissions-cpge-2025-2026-v1.pdf")], "Officiel (document ESIEE)"),
  bours("part", "Bourse ESIEE couvrant jusqu'à 60 % des frais, cumulable avec la bourse CROUS (document de l'école)."),
  [A("bccinp", 48, "MP", None, [V("ESIEE Paris (via Puissance Alpha en 2025)", 110, 30, 315, None, ins=895, c25="Puissance Alpha"),
                                 V("Filière data, 1 an étudiant + 2 ans apprenti (2025)", 18, 5, 254, None, ins=895, c25="Puissance Alpha")],
     ["ccinp", "b_esiee"], src26=S_CCINP26,
     note="Recrutait via Puissance Alpha en 2025 (places toutes filières) : rangs non comparables. L'école annonce 100 places + 15 en filière data pour 2026, toutes filières confondues.")]),

E("gi_grenoble", "Grenoble INP - Génie industriel", "Grenoble INP - Génie industriel (Grenoble INP-UGA)", ["Génie industriel", "Grenoble INP", "GI"],
  "Public", [C("Grenoble", "38", "ara")], ["indus"], "Spécialisée", "Génie industriel : supply chain, conception, management de production",
  nat(), B_NAT, [A("bccinp", 76, "toutes filières", None, [V("Génie industriel", 76, 27, 117, 147, cl=85, inter=True, iint=77)], ["ccinp", "b_gi"], src26=S_CCINP26)]),

E("eeigm", "Lorraine INP - EEIGM", "École européenne d'ingénieurs en génie des matériaux (Lorraine INP)", ["EEIGM", "Lorraine INP"],
  "Public", [C("Nancy", "54", "ges")], ["physique", "chimie"], "Spécialisée", "Génie des matériaux, formation internationale",
  nat(), B_NAT, [A("bccinp", 10, "toutes filières", None, [V("EEIGM", 10, 2, 22, 23, cl=18, inter=True, iint=11)], ["ccinp", "b_eeigm"], src26=S_CCINP26)]),

E("ensgsi", "Lorraine INP - ENSGSI", "École nationale supérieure en génie des systèmes et de l'innovation (Lorraine INP)", ["ENSGSI", "Lorraine INP"],
  "Public", [C("Nancy", "54", "ges")], ["indus"], "Spécialisée", "Innovation, gestion de projets industriels",
  nat(), B_NAT, [A("bccinp", 38, "toutes filières", None, [V("ENSGSI", 36, 5, 121, 142, cl=68, inter=True, iint=40)], ["ccinp", "b_ensgsi"], src26=S_CCINP26)]),

E("enstib", "Lorraine INP - ENSTIB", "École nationale supérieure des technologies et industries du bois (Lorraine INP)", ["ENSTIB", "Lorraine INP"],
  "Public", [C("Épinal", "88", "ges")], ["meca", "btp", "env"], "Spécialisée", "Bois : construction, matériaux, industrie",
  nat(), B_NAT, [A("bccinp", 6, "MP", None, [V("ENSTIB", 6, 3, 6, 5, cl=14)], ["ccinp", "b_enstib"], src26=S_CCINP26)]),
]

# ============================================================ INSA (banque CCINP)
INSA_P26 = "≈ 400 places pour tout le groupe INSA en 2026 (toutes filières) ; détail par département non publié dans nos sources"
DOM_CL = {"bio": 1019, "ener": 1185, "info": 1486, "ge": 1281, "gc": 1241, "meca": 1426, "phys": 1354}

def ins(lib, dom, pl, it, med, moy, iint=None):
    inter = dom not in ("info", "meca")  # domaines Info-maths et Méca-GI : classement MP seul
    return V(lib, pl, it, med, moy, cl=DOM_CL[dom], inter=inter, iint=iint)

def insa(id, nom, complet, campus, dom, desc, stats, alias=None, profil="Généraliste"):
    return E(id, nom, complet, (alias or []) + ["INSA", "Groupe INSA"], "Public", campus, dom, profil, desc,
             nat(), B_NAT,
             [A("insa", None, "toutes filières", INSA_P26, stats, ["ccinp", "insa"],
                src26=S_CCINP26, note="Sélection sur dossier, écrits CCINP et entretien. Places et classements par domaine : chaque ligne ci-dessous dépend d'une liste de domaine.")])

SCHOOLS_INSA = [
insa("insa_cvl", "INSA Centre Val de Loire", "Institut national des sciences appliquées Centre Val de Loire", [C("Bourges", "18", "cvl"), C("Blois", "41", "cvl")],
     ["info", "indus", "env"], "Sécurité informatique, génie des systèmes industriels, maîtrise des risques", [
     ins("Sécurité et technologies informatiques", "info", 8, 7, 967, 1016), ins("Génie des systèmes industriels", "meca", 4, 1, 1292, 1292),
     ins("Maîtrise des risques industriels", "phys", 20, 1, 2109, 2517, 3)]),
insa("insa_hdf", "INSA Hauts-de-France", "Institut national des sciences appliquées Hauts-de-France", [C("Valenciennes", "59", "hdf")],
     ["info", "elec", "meca", "indus", "btp"], "Informatique, électronique, mécanique, mécatronique, génie industriel, génie civil", [
     ins("Informatique et cybersécurité", "info", 3, 5, 695, 694), ins("Systèmes embarqués et télécoms", "ge", 4, 1, 3632, 3653, 5),
     ins("Informatique industrielle et automatique", "ge", 5, 0, 3775, 3389, 3), ins("Audiovisuel et multimédia", "ge", 4, 0, 3678, 3678, 1),
     ins("Génie civil et bâtiment", "gc", 2, 0, 1155, 1155, 2), ins("Génie industriel", "meca", 3, 3, 1033, 935),
     ins("Mécanique et énergétique", "meca", 5, 4, 931, 973), ins("Mécatronique", "meca", 10, 5, 974, 845)]),
insa("insa_lyon", "INSA Lyon", "Institut national des sciences appliquées de Lyon", [C("Villeurbanne", "69", "ara")],
     ["gen", "info", "elec", "meca", "energie", "btp", "bio", "physique"], "Large éventail de départements (informatique, mécanique, énergie, génie civil, biosciences...)", [
     ins("Biotechnologies et bioinformatique", "bio", 16, 1, 903, 732, 13), ins("Génie énergétique et environnement", "ener", 6, 4, 271, 313, 8),
     ins("Informatique", "info", 3, 3, 123, 131), ins("Télécommunications", "info", 4, 4, 439, 413),
     ins("Génie électrique", "ge", 9, 2, 624, 624, 11), ins("Génie civil et urbain", "gc", 3, 2, 249, 270, 3),
     ins("Génie industriel", "meca", 2, 2, 360, 360), ins("Génie mécanique", "meca", 5, 7, 119, 146),
     ins("Matériaux", "phys", 10, 1, 604, 603, 9)]),
insa("insa_rennes", "INSA Rennes", "Institut national des sciences appliquées de Rennes", [C("Rennes", "35", "bre")],
     ["info", "math", "elec", "meca", "btp", "physique"], "Informatique, maths appliquées, électronique, mécanique, génie civil, matériaux", [
     ins("Informatique", "info", 2, 2, 327, 327), ins("Mathématiques appliquées", "info", 1, 1, 614, 614),
     ins("Électronique et informatique industrielle", "ge", 6, 1, 2420, 2278, 6), ins("Électronique et télécommunications", "ge", 9, 4, 1901, 2222, 9),
     ins("Génie civil et urbain", "gc", 1, 0, 830, 830, 1), ins("Génie mécanique et automatique", "meca", 1, 1, 413, 413),
     ins("Génie physique et matériaux", "phys", 2, 0, 2261, 2261, 2)]),
insa("insa_rouen", "INSA Rouen Normandie", "Institut national des sciences appliquées de Rouen Normandie", [C("Saint-Étienne-du-Rouvray (Rouen)", "76", "nor")],
     ["info", "math", "chimie", "energie", "meca", "btp"], "Informatique, maths, chimie, énergétique, mécanique, génie civil", [
     ins("Chimie et génie chimique", "ener", 5, 0, 1660, 1673, 5), ins("Génie des procédés et gestion des risques", "ener", 4, 1, 3277, 3280, 6),
     ins("Génie énergétique (énergétique et propulsion)", "ener", 6, 0, 2013, 1992, 8), ins("Informatique et technologies de l'information", "info", 6, 9, 942, 975),
     ins("Mathématiques appliquées", "info", 14, 13, 818, 882), ins("Génie civil et urbain", "gc", 2, 2, 1346, 1265, 3),
     ins("Mécanique", "meca", 4, 3, 799, 958)]),
insa("insa_strasbourg", "INSA Strasbourg", "Institut national des sciences appliquées de Strasbourg", [C("Strasbourg", "67", "ges")],
     ["energie", "elec", "btp", "meca"], "Génie thermique et énergétique, génie électrique, génie civil, topographie, mécanique", [
     ins("Génie thermique, énergétique et environnement", "ener", 8, 8, 2775, 2928, 11), ins("Génie électrique", "ge", 11, 1, 2604, 2529, 8),
     ins("Génie civil", "gc", 5, 4, 947, 907, 5), ins("Topographie", "gc", 2, 2, 1604, 1613, 4),
     ins("Génie mécanique", "meca", 2, 3, 473, 473), ins("Plasturgie", "meca", 2, 0, None, None)]),
insa("insa_toulouse", "INSA Toulouse", "Institut national des sciences appliquées de Toulouse", [C("Toulouse", "31", "occ")],
     ["info", "math", "elec", "meca", "chimie", "bio", "physique"], "Informatique, maths appliquées, automatique-électronique, mécanique, procédés, génie physique, biologie", [
     ins("Génie biologique", "bio", 1, 0, 938, 938, 1), ins("Génie des procédés et environnement", "ener", 10, 4, 1560, 1535, 9),
     ins("Informatique et réseaux", "info", 1, 1, 293, 293), ins("Mathématiques appliquées", "info", 2, 2, 238, 238),
     ins("Automatique et électronique", "ge", 4, 0, 1309, 1257, 4), ins("Génie mécanique", "meca", 1, 2, 404, 404),
     ins("Génie physique", "phys", 5, 2, 823, 935, 5)]),
insa("esitech", "ESITech Rouen", "École supérieure d'ingénieurs en technologies innovantes (Université de Rouen), école partenaire INSA", [C("Saint-Étienne-du-Rouvray (Rouen)", "76", "nor")],
     ["physique", "bio"], "Physique pour la santé", [ins("Physique pour la santé", "bio", 4, 0, 2229, 2362, 3)], alias=["ESITech"], profil="Spécialisée"),
insa("isis", "ISIS Castres", "École d'ingénieurs ISIS (INU Champollion), école partenaire INSA", [C("Castres", "81", "occ")],
     ["info", "bio"], "Informatique pour la santé", [ins("Informatique pour la santé", "info", 2, 0, None, None)], alias=["ISIS"], profil="Spécialisée"),
insa("supenr", "Sup'EnR Perpignan", "Sup'EnR (Université de Perpignan Via Domitia), école partenaire INSA", [C("Perpignan", "66", "occ")],
     ["energie"], "Énergétique et énergies renouvelables", [ins("Énergétique et énergies renouvelables", "ener", 3, 0, 3504, 3504, 2)], alias=["Sup EnR"], profil="Spécialisée"),
]
