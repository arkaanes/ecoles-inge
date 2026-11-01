# -*- coding: utf-8 -*-
from data_common import *

def E(id, nom, complet, alias, statut, campus, dom, profil, desc, fr, bo, acces, note=None, liens=None):
    d = {"id": id, "nom": nom, "complet": complet, "alias": alias, "statut": statut,
         "campus": campus, "dom": dom, "profil": profil, "desc": desc,
         "frais": fr, "bours": bo, "acces": acces, "note": note}
    if liens: d["liens"] = liens
    return d

IMT26 = lambda m: frais(f"{m} €/an pour les élèves entrant en 2026 (hausse décidée par l'IMT)", m, m, "rentrée 2026",
                         [S_HAUSSE26, S_PGE26], "Presse spécialisée (L'Étudiant, mars 2026)")
B_IMT = bours("exo", "Boursiers exonérés (et CVEC) ; réduction de 50 % si les revenus dépassent de peu le plafond des bourses.")

SCHOOLS_1 = [
# ============================================================ X-ENS
E("x", "École polytechnique", "École polytechnique (l'X)", ["X", "l'X", "Polytechnique", "IP Paris"],
  "Public (militaire)", [C("Palaiseau", "91", "idf")], ["gen"], "Généraliste",
  "Généraliste, très orientée sciences fondamentales et recherche",
  frais("Gratuit : statut militaire, élève rémunéré pendant les 3 ans, contre un engagement de servir", 0, 0, "2025", [onisep("https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/essonne/ecole-polytechnique-institut-polytechnique-de-paris-etablissement-experimental/diplome-d-ingenieur-de-l-ecole-polytechnique-institut-polytechnique-de-paris"), S_PGE26]),
  B_REMU,
  [A("x", 163, "MP", "86 option informatique + 77 option physique et sciences de l'ingénieur", [
      V("MP option informatique", 87, 87, 66, 62, cl=141),
      V("MP option physique et sciences de l'ingénieur", 77, 77, 44, 45, cl=90)], ["x"],
     src26=onisep("https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/essonne/ecole-polytechnique-institut-polytechnique-de-paris-etablissement-experimental/diplome-d-ingenieur-de-l-ecole-polytechnique-institut-polytechnique-de-paris"))]),

E("espci", "ESPCI Paris - PSL", "École supérieure de physique et de chimie industrielles de la Ville de Paris",
  ["ESPCI", "PC Paris", "PSL"], "Public (Ville de Paris)", [C("Paris 5e", "75", "idf")], ["physique", "chimie", "bio"], "Spécialisée",
  "Physique, chimie, biologie ; très orientée recherche et innovation",
  frais("879 € de scolarité (2025) + 150 € d'inscription par an", 1029, 1029, "2025", [src("ESPCI : frais de scolarité", "https://prerentree.espci.fr/article136.html")]),
  bours("part", "Les boursiers ne paient pas les 879 € de scolarité (reste 150 € d'inscription)."),
  [A("x", 5, "MP", "5 places MP pour les candidats français, via le concours X", [], ["x"], lib="Concours X-ESPCI",
     src26=S_X, note="Seuls les candidats admissibles à l'X sont classés pour l'ESPCI ; aucun frais en plus de l'inscription au concours X. Pas de ligne MP dans les stats SCEI 2025.")]),

# ============================================================ Mines-Ponts
E("minesparis", "Mines Paris - PSL", "École nationale supérieure des mines de Paris", ["Mines ParisTech", "Mines de Paris", "ENSMP", "PSL"],
  "Public", [C("Paris 6e", "75", "idf")], ["gen"], "Généraliste", "Généraliste ; forte composante recherche",
  frais("4 150 €/an", 4150, 4150, "2026 (notice)", [S_CCMP26]),
  bours("exo", "Boursiers exonérés (« sauf boursiers français ou étrangers », notice Mines-Ponts 2026)."),
  [A("ccmp", 52, "MP", None, [V("Mines Paris", 52, 50, 110, 105, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("ponts", "École des Ponts ParisTech", "École nationale des ponts et chaussées", ["ENPC", "Ponts", "Ponts ParisTech", "École des Ponts"],
  "Public", [C("Champs-sur-Marne", "77", "idf")], ["gen", "btp", "math"], "Généraliste",
  "Généraliste : génie civil, transports, maths appliquées, finance, environnement",
  frais("4 150 €/an pour 2026-2027 (3 800 € en 2025-2026)", 4150, 4150, "2026-2027", [src("Droits de scolarité 2026-2027 de l'École des Ponts", "https://ecoledesponts.fr/sites/default/files/pages/Ecole/Point%2012%20-%20Droits%20de%20scolarit%C3%A9%20de%20la%20formatin%20d'ing%C3%A9nieur%20-%20CMCI%202026-2027.pdf"), S_CCMP26]),
  bours("exo", "Exonération de droit des boursiers (article R719-49 du code de l'éducation, cité par l'école) ; la notice parle de « bourses sur critères sociaux »."),
  [A("ccmp", 82, "MP", None, [V("École des Ponts", 82, 84, 456, 429, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("telecomparis", "Télécom Paris", "Télécom Paris (Institut Mines-Télécom)", ["Télécom ParisTech", "ENST", "IP Paris", "IMT"],
  "Public", [C("Palaiseau", "91", "idf")], ["info", "elec", "math"], "Spécialisée",
  "Numérique : informatique, IA, data, réseaux, électronique",
  IMT26(3600), B_IMT,
  [A("ccmp", 82, "MP", "80 en statut étudiant + 2 en apprentissage", [
      V("Statut étudiant", 84, 74, 773, 700, cl=1580), V("Apprentissage", 2, 1, 909, 909, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("ensta", "ENSTA", "ENSTA, École nationale supérieure de techniques avancées (fusion ENSTA Paris + ENSTA Bretagne)",
  ["ENSTA Paris", "ENSTA Bretagne", "ENSTA ParisTech", "ENSIETA", "IP Paris"], "Public",
  [C("Palaiseau", "91", "idf"), C("Brest", "29", "bre")], ["gen", "energie", "transport", "defense"], "Généraliste",
  "Généraliste : énergie (dont nucléaire), transports et naval, défense, robotique, maths appliquées",
  frais("2 926 €/an (ressortissants UE) ; 0 € en apprentissage", 2926, 2926, "2026 (notice)", [S_CCMP26]),
  bours("exo", "Boursiers CROUS exonérés (notice Mines-Ponts 2026). Voie IETA (FIDS) : statut militaire, rémunéré."),
  [A("ccmp", 53, "MP", "51 en statut étudiant + 2 en apprentissage", [
      V("ENSTA Paris (statut étudiant)", 58, 54, 645, 601, cl=1580), V("ENSTA Paris – apprentissage", 1, 1, 771, 771, cl=1580)],
     ["ccmp"], lib="Campus Paris-Saclay (Palaiseau)", src26=S_CCMP_DI),
   A("ccmp", 26, "MP", None, [], ["ccmp"], lib="Campus de Brest", src26=S_CCMP_DI,
     note="Nouveau sur Mines-Ponts en 2026. En 2025, l'ex-ENSTA Bretagne recrutait via Mines-Télécom (42 places, rang médian 960 sur ce concours)."),
   A("cmt", 14, "MP", None, [V("ex-ENSTA Bretagne, statut étudiant (2025, pour comparaison)", 42, 37, 960, 904, cl=3444, prev="ex-ENSTA Bretagne")],
     ["cmt"], lib="FIDS – ingénieur défense et sécurité (statut étudiant)", src26=S_CMT26,
     note="Nouvelle formation à la rentrée 2026, diplôme codélivré par l'ENSTA et l'ISAE-SUPAERO : 1re année à Brest, puis option à Brest, Paris-Saclay ou Toulouse (communiqué du 10 décembre 2025)."),
   A("cmt", 14, "MP", None, [V("ex-ENSTA Bretagne, statut IETA (2025, pour comparaison)", 13, 13, 1001, 885, cl=3095, prev="ex-ENSTA Bretagne")],
     ["cmt"], lib="FIDS – statut IETA (militaire, rémunéré)", src26=S_CMT26)],
  note="ENSTA Paris et ENSTA Bretagne ont fusionné : les noms et les voies d'accès ont changé en 2026.",
  liens=[src("Communiqué ENSTA / ISAE-SUPAERO sur la formation défense et sécurité (10 décembre 2025)",
             "https://www.isae-supaero.fr/wp-content/uploads/2025/12/CP-ENSTA_-ISAE-SUPAERO_nouvelle-formation-FIDS_10dec2025.pdf")]),

E("ensae", "ENSAE Paris", "École nationale de la statistique et de l'administration économique", ["ENSAE", "IP Paris", "GENES"],
  "Public", [C("Palaiseau", "91", "idf")], ["math"], "Spécialisée",
  "Statistique, data science, économie, finance, actuariat",
  frais("3 500 €/an", 3500, 3500, "2026 (notice)", [S_CCMP26]),
  bours("exo", "Gratuit pour les boursiers (notice Mines-Ponts 2026)."),
  [A("ccmp", 50, "MP", None, [V("ENSAE Paris", 50, 52, 863, 815, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("supaero", "ISAE-SUPAERO", "Institut supérieur de l'aéronautique et de l'espace", ["SUPAERO", "Sup'Aéro", "ISAE"],
  "Public", [C("Toulouse", "31", "occ")], ["aero", "gen"], "Généraliste", "Aéronautique et spatial, formation généraliste",
  frais("2 926 €/an (ressortissants UE)", 2926, 2926, "2026 (notice)", [S_CCMP26]),
  bours("exo", "Gratuit pour les boursiers (notice Mines-Ponts 2026)."),
  [A("ccmp", 63, "MP", None, [V("ISAE-SUPAERO", 63, 59, 689, 604, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("minesnancy", "Mines Nancy", "École nationale supérieure des mines de Nancy (Université de Lorraine)", ["ENSMN", "Mines de Nancy", "Université de Lorraine"],
  "Public", [C("Nancy", "54", "ges")], ["gen"], "Généraliste", "Généraliste",
  frais("2 613 €/an (ressortissants UE)", 2613, 2613, "2026 (notice)", [S_CCMP26]),
  bours("exo", "Boursiers exonérés (notice Mines-Ponts 2026)."),
  [A("ccmp", 46, "MP", None, [V("Mines Nancy", 48, 41, 1033, 1017, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("minesse", "Mines Saint-Étienne (ICM)", "École des mines de Saint-Étienne, cycle ingénieur civil des mines", ["EMSE", "Mines Saint-Etienne", "ICM", "IMT"],
  "Public", [C("Saint-Étienne", "42", "ara")], ["gen"], "Généraliste", "Généraliste",
  IMT26(3600), B_IMT,
  [A("ccmp", 40, "MP", None, [V("Mines Saint-Étienne", 40, 37, 1343, 1310, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

E("imtatlantique", "IMT Atlantique", "IMT Atlantique (ex-Télécom Bretagne + Mines Nantes)", ["Télécom Bretagne", "Mines Nantes", "IMT"],
  "Public", [C("Brest", "29", "bre"), C("Nantes", "44", "pdl"), C("Rennes", "35", "bre")], ["gen", "info", "energie", "elec"], "Généraliste",
  "Généraliste : numérique, énergie (dont nucléaire), environnement",
  IMT26(3600), B_IMT,
  [A("ccmp", 85, "MP", None, [V("IMT Atlantique", 90, 80, 1262, 1242, cl=1580)], ["ccmp"], src26=S_CCMP26)]),

# ============================================================ Mines-Télécom
E("ismin", "Mines Saint-Étienne – ISMIN", "Mines Saint-Étienne, cycle ISMIN (Gardanne)", ["ISMIN", "EMSE", "Mines Saint-Etienne", "IMT"],
  "Public", [C("Gardanne", "13", "pac")], ["elec", "info"], "Spécialisée", "Microélectronique et informatique",
  IMT26(3600), B_IMT,
  [A("cmt", 37, "MP", None, [V("Mines Saint-Étienne – ISMIN", 37, 36, 1856, 1731, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("enm", "École nationale de la météorologie", "École nationale de la météorologie (Météo-France)", ["ENM", "Météo-France"],
  "Public", [C("Toulouse", "31", "occ")], ["env", "math"], "Spécialisée", "Météorologie, climat, modélisation",
  frais("Civils : droit national, 630 €/an en 2026-2027 (618 € en 2024 d'après Onisep) ; fonctionnaires : gratuit et rémunérés", 630, 630, "2026-2027", [onisep("https://www.onisep.fr/ressources/structures-enseignement/occitanie/haute-garonne/ecole-nationale-de-la-meteorologie/diplome-d-ingenieur-de-l-ecole-nationale-de-la-meteorologie")]),
  bours("exo", "Gratuit pour les boursiers (Onisep). Voie fonctionnaire : gratuite et rémunérée."),
  [A("cmt", 3, "MP", None, [V("Non fonctionnaires", 5, 4, 2845, 2813, cl=3444)], ["cmt"], lib="Élèves civils", src26=S_CMT26),
   A("cmt", 11, "MP", None, [V("Fonctionnaires", 14, 14, 2326, 2064, cl=3131)], ["cmt"], lib="Élèves fonctionnaires (rémunérés)", src26=S_CMT26)]),

E("eivp", "EIVP", "École des ingénieurs de la Ville de Paris (Université Gustave Eiffel)", ["EIVP", "Université Gustave Eiffel"],
  "Public (Ville de Paris)", [C("Paris 19e", "75", "idf")], ["btp", "env"], "Spécialisée", "Génie urbain : ville, réseaux, environnement",
  frais("2 095 €/an (2024) ; voie fonctionnaire gratuite et rémunérée", 2095, 2095, "2024", [onisep("https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/paris/ecole-des-ingenieurs-de-la-ville-de-paris-universite-gustave-eiffel/diplome-d-ingenieur-de-l-ecole-des-ingenieurs-de-la-ville-de-paris-specialite-genie-urbain")]),
  bours("part", "Boursiers : 1 047,50 €/an (moitié prix)."),
  [A("cmt", 24, "MP", None, [V("Civils", 24, 23, 2998, 2948, cl=3444)], ["cmt"], lib="Élèves civils", src26=S_CMT26),
   A("cmt", 4, "MP", None, [V("Fonctionnaires", 5, 5, 2515, 2238, cl=3131)], ["cmt"], lib="Élèves fonctionnaires (rémunérés)", src26=S_CMT26)]),

E("ensg_geol", "ENSG Nancy (géologie)", "École nationale supérieure de géologie (Lorraine INP)", ["ENSG", "Géologie Nancy", "Lorraine INP"],
  "Public", [C("Nancy", "54", "ges")], ["env"], "Spécialisée", "Géosciences, ressources, géotechnique, environnement",
  nat(), B_NAT,
  [A("cmt", 2, "MP", None, [V("ENSG Nancy", 2, 2, 2207, 2207, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("ensiie", "ENSIIE", "École nationale supérieure d'informatique pour l'industrie et l'entreprise", ["ENSIIE"],
  "Public", [C("Évry-Courcouronnes", "91", "idf")], ["info", "math"], "Spécialisée", "Informatique, maths appliquées",
  nat("Ancien tarif affiché : 601 €/an"), B_NAT,
  [A("cmt", 67, "MP", None, [V("ENSIIE", 65, 70, 2380, 2281, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("enssat", "ENSSAT", "École nationale supérieure des sciences appliquées et de technologie (Université de Rennes)", ["ENSSAT", "Université de Rennes"],
  "Public", [C("Lannion", "22", "bre")], ["info", "elec", "physique"], "Spécialisée", "Informatique, électronique, photonique",
  frais("630 €/an (2026-2027) + 55 € de frais de gestion + CVEC", 685, 685, "2026-2027", [S_NAT]), B_NAT,
  [A("cmt", 25, "MP", None, [V("ENSSAT", 23, 27, 3308, 3102, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("entpe", "ENTPE", "École nationale des travaux publics de l'État", ["ENTPE"],
  "Public", [C("Vaulx-en-Velin", "69", "ara")], ["btp", "env", "transport"], "Spécialisée",
  "Aménagement, génie civil, transports, environnement",
  frais("Civils : 628 €/an (Onisep 2026) ; fonctionnaires : gratuit et rémunérés", 628, 628, "2026", [onisep("https://www.onisep.fr/ressources/structures-enseignement/auvergne-rhone-alpes/rhone/entpe-lyon/diplome-d-ingenieur-de-l-ecole-nationale-des-travaux-publics-de-l-etat"), S_PGE26]),
  bours("nd", "Exonération des boursiers non précisée par les sources (élèves aidés par l'ENTPE exonérés). Voie fonctionnaire gratuite."),
  [A("cmt", 24, "MP", None, [V("Civils", 24, 23, 2381, 2234, cl=3444)], ["cmt"], lib="Élèves civils", src26=S_CMT26),
   A("cmt", 28, "MP", None, [V("Fonctionnaires", 29, 29, 2466, 2295, cl=3131)], ["cmt"], lib="Élèves fonctionnaires (rémunérés)", src26=S_CMT26)]),

E("eurecom", "EURECOM", "EURECOM (école d'ingénieurs et centre de recherche, Sophia Antipolis)", ["EURECOM", "Eurécom"],
  "GIE (avec l'IMT et des partenaires)", [C("Biot (Sophia Antipolis)", "06", "pac")], ["info", "elec"], "Spécialisée",
  "Numérique : réseaux, data science, sécurité, systèmes",
  frais("Non trouvé dans les sources consultées", None, None, "", [], "À vérifier"),
  bours("nd", "Non trouvé."),
  [A("cmt", 19, "MP", None, [V("EURECOM", 23, 19, 3070, 2823, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("geodata", "Géodata Paris", "Géodata Paris, ex-ENSG Géomatique (École nationale des sciences géographiques)", ["ENSG", "ENSG Géomatique", "IGN", "Université Gustave Eiffel"],
  "Public", [C("Champs-sur-Marne", "77", "idf")], ["info", "env"], "Spécialisée", "Géomatique : information géographique, SIG, télédétection",
  frais("2 240 €/an (2026) ; gratuit pour les fonctionnaires et les boursiers", 2240, 2240, "2026", [onisep("https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/seine-et-marne/geodata-paris-ex-ensg-geomatique-universite-gustave-eiffel/diplome-d-ingenieur-de-l-ecole-nationale-des-sciences-geographiques")]),
  bours("exo", "Gratuit pour les boursiers (Onisep 2026). Voie fonctionnaire gratuite et rémunérée."),
  [A("cmt", 13, "MP", None, [V("Civils", 13, 4, 3128, 3115, cl=3444)], ["cmt"], lib="Élèves civils", src26=S_CMT26),
   A("cmt", 6, "MP", None, [V("Fonctionnaires", 6, 4, 2844, 2783, cl=3131)], ["cmt"], lib="Élèves fonctionnaires (agents de l'IGN, rémunérés)", src26=S_CMT26)],
  note="Nouveau nom depuis 2025 (ex-ENSG Géomatique)."),

E("albi", "IMT Mines Albi", "IMT Mines Albi-Carmaux", ["Mines Albi", "IMT"],
  "Public", [C("Albi", "81", "occ")], ["gen", "chimie", "indus", "energie"], "Généraliste",
  "Généraliste : procédés, matériaux, génie industriel, énergie-environnement",
  IMT26(3200), B_IMT,
  [A("cmt", 54, "MP", None, [V("IMT Mines Albi", 56, 64, 2282, 2193, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("ales", "IMT Mines Alès", "IMT Mines Alès", ["Mines Alès", "EMA", "IMT"],
  "Public", [C("Alès", "30", "occ")], ["gen"], "Généraliste", "Généraliste",
  IMT26(3200), B_IMT,
  [A("cmt", 68, "MP", None, [V("IMT Mines Alès", 68, 68, 1701, 1635, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("imtne", "IMT Nord Europe", "IMT Nord Europe (ex-Mines Douai + Télécom Lille)", ["Mines Douai", "Télécom Lille", "IMT Lille Douai", "IMT"],
  "Public", [C("Douai", "59", "hdf"), C("Villeneuve-d'Ascq", "59", "hdf")], ["gen", "info", "energie", "btp"], "Généraliste",
  "Généraliste : numérique, énergie, environnement, matériaux, génie civil",
  IMT26(3200), B_IMT,
  [A("cmt", 56, "MP", None, [V("IMT Nord Europe", 56, 54, 1891, 1842, cl=3444)], ["cmt"], lib="Élèves civils", src26=S_CMT26),
   A("cmt", 4, "MP", None, [V("Fonctionnaires", 4, 4, 1682, 1504, cl=3131)], ["cmt"], lib="Élèves fonctionnaires", src26=S_CMT26),
   A("e3a_ind", 20, "MP", None, [V("IMT Nord Europe (avec l'ISPA)", 20, 10, 14, None, ins=459)],
     ["ccinp", "ind_imtne"], lib="Formation en partenariat avec l'ISPA (plasturgie)", src26=S_E3A26)]),

E("ensma", "ISAE-ENSMA", "ISAE-ENSMA (École nationale supérieure de mécanique et d'aérotechnique)", ["ENSMA", "ISAE", "Poitiers"],
  "Public", [C("Chasseneuil-du-Poitou (Poitiers)", "86", "naq")], ["aero", "meca", "energie"], "Spécialisée",
  "Aéronautique, mécanique, énergétique",
  nat("601 € affichés pour 2024-2025"), B_NAT,
  [A("cmt", 55, "MP", None, [V("ISAE-ENSMA (via CCINP en 2025)", 55, 59, 1614, 1553, cl=4075, c25="CCINP")], ["cmt"], src26=S_CMT26,
     note="A quitté le CCINP pour Mines-Télécom en 2026 : les rangs 2025 sont des rangs CCINP, pas comparables.")]),

E("supmeca", "ISAE-Supméca", "ISAE-Supméca (Institut supérieur de mécanique de Paris)", ["Supméca", "ISAE"],
  "Public", [C("Saint-Ouen-sur-Seine", "93", "idf")], ["meca", "indus"], "Spécialisée", "Mécanique, conception, mécatronique, production",
  frais("Droit national : 630 €/an en 2026-2027 (628 € en 2025-2026 d'après le tableau de l'école) + CVEC", 630, 630, "2026-2027", [src("ISAE-Supméca : tableau des frais d'inscription", "https://www.isae-supmeca.fr/wp-content/uploads/2025/05/tableau_frais_inscription.pdf")]),
  bours("exo", "0 € pour les boursiers CROUS (tableau officiel de l'école)."),
  [A("cmt", 45, "MP", None, [V("ISAE-Supméca", 45, 43, 2090, 2000, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("telecomnancy", "Télécom Nancy", "Télécom Nancy (Université de Lorraine)", ["ESIAL", "Université de Lorraine"],
  "Public", [C("Villers-lès-Nancy", "54", "ges")], ["info"], "Spécialisée", "Informatique et numérique",
  nat(), B_NAT,
  [A("cmt", 57, "MP", None, [V("Télécom Nancy", 60, 57, 2479, 2400, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("tps", "Télécom Physique Strasbourg", "Télécom Physique Strasbourg (Université de Strasbourg)", ["TPS", "ENSPS", "Université de Strasbourg"],
  "Public", [C("Illkirch-Graffenstaden", "67", "ges")], ["info", "elec", "physique", "bio"], "Spécialisée",
  "Informatique, réseaux, électronique, photonique, technologies pour la santé",
  nat(), B_NAT,
  [A("ccinp", 26, "MP", None, [V("Télécom Physique Strasbourg", 30, 29, 2468, 2304, cl=4075)], ["ccinp"], lib="Cursus via le CCINP", src26=S_CCINP26),
   A("cmt", 20, "MP", None, [V("Informatique et réseaux", 20, 15, 2888, 2772, cl=3444)], ["cmt"], lib="Informatique et réseaux", src26=S_CMT26),
   A("cmt", 12, "MP", None, [V("TI-Santé", 8, 6, 1825, 1887, cl=3444)], ["cmt"], lib="Technologies de l'information pour la santé", src26=S_CMT26)]),

E("telecomse", "Télécom Saint-Étienne", "Télécom Saint-Étienne (Université Jean Monnet)", ["TSE", "Université Jean Monnet"],
  "Public", [C("Saint-Étienne", "42", "ara")], ["info", "elec", "physique"], "Spécialisée", "Numérique, réseaux, image, optique",
  nat(), B_NAT,
  [A("cmt", 33, "MP", None, [V("Télécom Saint-Étienne", 33, 34, 2974, 2863, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("tsp", "Télécom SudParis", "Télécom SudParis (Institut Mines-Télécom, IP Paris)", ["TSP", "INT", "IP Paris", "IMT"],
  "Public", [C("Évry-Courcouronnes", "91", "idf")], ["info", "elec", "math"], "Spécialisée",
  "Numérique : cybersécurité, IA, réseaux, data",
  IMT26(3600), B_IMT,
  [A("cmt", 80, "MP", None, [V("Télécom SudParis", 90, 82, 1149, 1097, cl=3444)], ["cmt"], src26=S_CMT26)]),

E("enac", "ENAC", "École nationale de l'aviation civile", ["ENAC", "IENAC"],
  "Public", [C("Toulouse", "31", "occ")], ["aero", "info", "elec"], "Spécialisée", "Aviation civile : aéronautique, systèmes, trafic aérien",
  frais("Civils : 1 500 €/an (UE, 2025) ; fonctionnaires : gratuit", 1500, 1500, "2025", [onisep("https://www.onisep.fr/ressources/structures-enseignement/occitanie/haute-garonne/ecole-nationale-de-l-aviation-civile-campus-de-toulouse/diplome-d-ingenieur-de-l-ecole-nationale-de-l-aviation-civile")]),
  bours("nd", "Exonération des boursiers non indiquée par Onisep. Voie fonctionnaire gratuite."),
  [A("cmt", 30, "MP", None, [V("Civils (via CCINP en 2025)", 32, 32, 1495, 1387, cl=4075, c25="CCINP")], ["cmt"], lib="Ingénieurs civils", src26=S_CMT26,
     note="A quitté le CCINP pour Mines-Télécom en 2026 : rangs 2025 = rangs CCINP."),
   A("cmt", 7, "MP", None, [V("Fonctionnaires (via CCINP en 2025)", 7, 7, 715, 660, cl=4075, c25="CCINP")], ["cmt"], lib="Ingénieurs fonctionnaires", src26=S_CMT26)],
  note="La formation de contrôleur aérien (banque CCINP) n'est pas un diplôme d'ingénieur : elle n'est pas listée ici."),
]
