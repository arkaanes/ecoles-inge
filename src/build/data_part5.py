# -*- coding: utf-8 -*-
"""Les 4 ENS en filière MP (écoles de recherche, concours de la banque X-ENS)."""
from data_common import *
from data_part1 import E

S_ENS_ULM26 = src("ENS Ulm : décision du 8 décembre 2025 sur les postes 2026",
                  "https://www.ens.psl.eu/sites/default/files/decision_fixant_le_nombre_de_postes_ouverts_aux_concours_ens_ulm_session_2026_signe.pdf")
S_ENS_SACLAY26 = src("ENS Paris-Saclay : postes d'élèves ouverts en 2026",
                     "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_postes_eleves_ouverts_ENS_Paris-Saclay.pdf")
S_ENS_LYON = src("ENS de Lyon : concours sciences (entrants 2026)",
                 "https://www.ens-lyon.fr/formation/admission/procedures-dadmission/concours-sciences-exactes-et-experimentales")
S_ENS_RENNES = src("ENS Rennes : concours MP 2026",
                   "https://www.ens-rennes.fr/admission/concours1a/mp")
S_ENS_NOTICE = src("Notice inter-ENS 2026 (statut des élèves, p. 3)",
                   "https://www.ens.psl.eu/sites/default/files/vf_notice_interens_2026_v10122025.pdf")
S_ENS_STATUT = src("Statuts à l'ENS (Diplomeo, octobre 2024)",
                   "https://diplomeo.com/actualite-statuts_etudiants_ecoles_normales_superieures")

def ens_frais():
    return frais("Élève fonctionnaire stagiaire, payé pendant les études (environ un SMIC par mois d'après Diplomeo). "
                 "Droits d'inscription aux diplômes préparés : à vérifier auprès de l'école",
                 None, None, "2026", [S_ENS_NOTICE, S_ENS_STATUT], "À vérifier (montant des droits non trouvé)")

B_ENS = bours("remu", "Payé pendant les études en tant qu'élève fonctionnaire stagiaire (citoyens de l'UE), "
                      "contre un engagement de 10 ans dans la fonction publique, années d'études comprises (notice inter-ENS 2026).")

NOTE_ENS = ("Les classés et intégrés ne comptent que les candidats « fonctionnarisables » (note du SCEI). "
            "Chaque ENS a sa propre liste de classement.")

SCHOOLS_ENS = [
E("ens_ulm", "ENS Ulm (PSL)", "École normale supérieure – PSL, rue d'Ulm",
  ["ENS Paris", "ENS", "Ulm", "Normale sup", "PSL"], "Public", [C("Paris 5e", "75", "idf")],
  ["rech", "physique"], "Recherche",
  "École de recherche : mathématiques et physique (groupe MP)",
  ens_frais(), B_ENS,
  [A("ens", 38, "MP", None, [V("ENS Ulm", 38, 38, 35, 34, cl=98)], ["ens"],
     lib="Groupe mathématiques-physique", src26=S_ENS_ULM26, note=NOTE_ENS)],
  note="En informatique, l'ENS Ulm recrute par la filière MPI (12 postes en 2026), pas par la MP."),

E("ens_saclay", "ENS Paris-Saclay", "École normale supérieure Paris-Saclay",
  ["ENS Cachan", "Cachan", "ENS", "Normale sup", "Paris-Saclay"], "Public", [C("Gif-sur-Yvette", "91", "idf")],
  ["rech"], "Recherche",
  "École de recherche (concours MP)",
  ens_frais(), B_ENS,
  [A("ens", 21, "MP", None, [V("ENS Paris-Saclay MP", 18, 18, 128, 118, cl=166)], ["ens"],
     lib="Concours MP", src26=S_ENS_SACLAY26, note=NOTE_ENS)],
  note="Le concours MPI (14 postes en 2026) est réservé à la filière MPI."),

E("ens_lyon", "ENS de Lyon", "École normale supérieure de Lyon",
  ["ENS Lyon", "ENS", "Normale sup"], "Public", [C("Lyon 7e", "69", "ara")],
  ["rech", "info"], "Recherche",
  "École de recherche : mathématiques et informatique (deux concours en MP)",
  ens_frais(), B_ENS,
  [A("ens", None, "MP", "17 entrants en 2026", [V("ENS de Lyon – mathématiques", 16, 16, 85, 79, cl=154)], ["ens"],
     lib="Concours M-MP (mathématiques)", src26=S_ENS_LYON,
     note="Nombre de postes 2026 non repris ici ; 17 élèves sont entrés en 2026 par ce concours (ENS de Lyon). " + NOTE_ENS),
   A("ens", None, "MP", "8 entrants en 2026", [V("ENS de Lyon – informatique", 9, 9, 10, 11, cl=36)], ["ens"],
     lib="Concours I-MP (informatique)", src26=S_ENS_LYON,
     note="Peu d'inscrits en 2025 (147 candidats de MP), d'où des rangs très petits.")]),

E("ens_rennes", "ENS Rennes", "École normale supérieure de Rennes",
  ["ENS Rennes", "ENS", "Ker Lann", "Normale sup"], "Public", [C("Bruz (Rennes)", "35", "bre")],
  ["rech"], "Recherche",
  "École de recherche : mathématiques (groupe MP)",
  ens_frais(), B_ENS,
  [A("ens", None, "MP", "10 places en 2025", [V("ENS Rennes MP", 10, 10, 170, 170, cl=241)], ["ens"],
     lib="Concours MP (département de mathématiques)", src26=S_ENS_RENNES,
     note="Nombre de postes 2026 non trouvé. " + NOTE_ENS)],
  note="En informatique, l'ENS Rennes recrute par la filière MPI."),
]
