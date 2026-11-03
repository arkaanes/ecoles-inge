# -*- coding: utf-8 -*-
"""Filière MPI : pages concours (épreuves, coefficients, style), variantes des fiches concours, exclusions, sources.
Relevé le 31 octobre 2026 sur les notices et règlements 2026 et les rapports de jury 2025."""
from data_concours import FEES as _FEES_MP

def src(t, u): return {"t": t, "u": u}

S_SCEI = src("Statistiques SCEI MPI 2025", "https://www.scei-concours.fr/stat2025/mpi.html")
S_FRAIS = src("Frais de dossier MPI 2026 (SCEI)", "https://www.scei-concours.fr/pdf/frais_MPI2026.pdf")
S_XN = src("Notice du concours 2026 (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Notice%20du%20concours%202026%20publi%C3%A9e.pdf")
S_XE = src("Épreuves écrites MP, MPI, PC (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Epreuves%20%C3%A9crites%20MP%20MPI%20PC.pdf")
S_XO = src("Épreuves orales MP, MPI, PC (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Epreuves%20orales%20MP%20MPI%20PC_1.pdf")
S_XOI = src("Rapport de l'oral d'informatique MPI 2025 (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Oral_MPI_Info%20OK.pdf")
S_X_ONISEP = src("Fiche Onisep (places 2026 par filière)", "https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/essonne/ecole-polytechnique-institut-polytechnique-de-paris-etablissement-experimental/diplome-d-ingenieur-de-l-ecole-polytechnique-institut-polytechnique-de-paris")
S_ENSN = src("Notice inter-ENS 2026 (banque MPI)", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/notice_interens_2026_mise_en_ligne_vf260212.pdf")
S_ENS_SACLAY = src("ENS Paris-Saclay : postes d'élèves ouverts en 2026", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_postes_eleves_ouverts_ENS_Paris-Saclay.pdf")
S_ENS_INFO = src("Rapport de l'oral d'informatique fondamentale 2025 (ENS, MP et MPI)", "https://predoc.di.ens.fr/informatique-ens/annales/2025_Info-rapport.pdf")
S_CCMP_N = src("Notice des écoles Mines-Ponts 2026", "https://concoursminesponts.fr/wp-content/uploads/2025/12/notice-des-ecoles-2026-22.12.25.pdf")
S_CCMP_R = src("Règlement 2026 du concours Mines-Ponts", "https://concoursminesponts.fr/wp-content/uploads/2025/12/reglement-2026-09.12.25.pdf")
S_CCMP_J = src("Rapport du jury sur les écrits 2025 (Mines-Ponts)", "https://concoursminesponts.fr/wp-content/uploads/2025/10/Rapport-Ecrit-2025-VF.pdf")
S_CMT = src("Notice Mines-Télécom 2026", "https://cahier-de-prepa.fr/pc-descartes/download?id=260")
S_CMT_O = src("Les épreuves orales (site du concours Mines-Télécom)", "https://www.concours-mines-telecom.fr/le-concours-mines-telecom/les-epreuves-orales/")
S_CCS = src("Notice Centrale-Supélec 2026, filière MPI", "https://www.concours-centrale-supelec.fr/sites/default/files/documents/CCS_2026_MPI.pdf")
S_CCS_J = src("Maths 1 MPI 2025 de Centrale-Supélec : sujet, statistiques et rapport (Hadamard)", "https://www.hadamard.fr/annales/maths-1-centrale-supelec-mpi/2025")
S_INP_P = src("Places MPI 2026 (site du CCINP)", "https://www.concours-commun-inp.fr/fr/les-ecoles/les-places-dans-les-ecoles/places-mpi.html")
S_INP_R = src("Règlement 2026 du CCINP", "https://www.concours-commun-inp.fr/_resource/R%C3%A8glement_VF_23-06.pdf?download=true")
S_INP_J = src("Informatique MPI 2025 du CCINP : sujet et rapport du jury (Hadamard)", "https://www.hadamard.fr/annales/info-ccinp-mpi/2025")
S_E3A = src("Notice 2026 de la banque e3a-Polytech", "https://esigelec.fr/sites/default/files/2025-12/VF-Notice-2026-Banque-e3a-Polytech.pdf")
S_CAL = src("Calendrier des concours 2026 (Hadamard)", "https://www.hadamard.fr/actualites/calendrier-concours-prepa-2026-x-mines-centrale-ccinp")
S_FORUM = src("Forum Futura-Sciences, « liste d'écoles concours »", "https://forums.futura-sciences.com/cpge/960431-liste-decoles-concours.html")
S_EP26 = src("Concours EPITA-IPSA-ESME 2026 (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-cpge-epita-ipsa-esme.html")
S_CESI = src("Concours CESI CPGE", "https://www.cesi.fr/concours-cesi-cpge/")
S_UT = src("UTC, voies d'admission 2026 (Onisep)", "https://www.onisep.fr/ressources/structures-enseignement/hauts-de-france/oise/universite-de-technologie-de-compiegne/diplome-d-ingenieur-de-l-universite-de-technologie-de-compiegne-specialite-informatique")
S_CS_E = src("Épreuves écrites (site du concours Centrale-Supélec)", "https://www.concours-centrale-supelec.fr/epreuves-ecrites")
S_CS_O = src("Épreuves orales (site du concours Centrale-Supélec)", "https://www.concours-centrale-supelec.fr/epreuves-orales")
S_MAP = src("Contours des régions : IGN Admin Express (Licence ouverte), via france-geojson", "https://github.com/gregoiredavid/france-geojson")
S_CAL26 = src("Calendrier SCEI 2026 (L'Étudiant, mis à jour le 7 novembre 2025)", "https://www.letudiant.fr/etudes/classes-prepa/ecoles-d-ingenieurs-comment-se-passe-la-procedure-d-inscription.html")
S_NAT = src("Tarifs 2026-2027 de l'ENSSAT (droit national 630 €)", "https://www.enssat.fr/uploads/site/documents/Brochures/Tarifs_2026-2027.pdf")
S_HAUSSE = src("Écoles qui augmentent leurs frais à la rentrée 2026 (L'Étudiant)", "https://www.letudiant.fr/etudes/ecole-ingenieur/quelles-ecoles-d-ingenieurs-augmentent-leurs-frais-a-la-rentree-et-pourquoi.html")

# Frais : barème MPI 2026 du SCEI. Comme en MP, sauf l'ENSEA (inscrite seule, 85 €) et l'ENSISA (25 €, 10 € pour les boursiers).
FEES_MPI = {k: list(v) for k, v in _FEES_MP.items()}
FEES_MPI["ccs_ensea"] = ["Centrale-Supélec : ENSEA", 85, 0]
FEES_MPI["b_ensisa"] = ["Banque CCINP : ENSISA", 25, 10]

FAMILLES_MPI = {
"x": {
  "insc": ["220 €", "d'inscription, gratuit si boursier"], "inscCourt": "220 €", "ecritsCourt": "Communs avec les ENS",
  "poids": 69, "poidsFait": "du classement final vient des oraux, sport non compris", "poidsCourt": "69 %",
  "style": {
    "sujets": "Six écrits de 4 h, tous pour l'admissibilité : deux de maths, l'informatique C (le plus gros coefficient, 9), la physique, le français et la langue.",
    "sujetsSrc": [S_XE],
    "oraux": "Les oraux comptent 96 points sur 140 : maths (23), informatique (22) et physique (20), 50 minutes chacun. À l'oral d'informatique, des questions de plus en plus dures sans préparation : le jury note surtout jusqu'où tu vas, et conseille de tester de petits cas plutôt que de deviner.",
    "orauxSrc": [S_XO, S_XOI],
    "pourqui": "pour les très bons profils en maths et en informatique, à l'aise au tableau.",
    "mots": "Info et maths, oraux décisifs"},
  "blocs": [{
    "titre": "École polytechnique",
    "ecrits": {"quand": "13-17 avril 2026", "l": [
      ["Mathématiques A", "4 h", "6"], ["Mathématiques B", "4 h", "6"], ["Informatique C", "4 h", "9"], ["Physique", "4 h", "6"],
      ["Français", "4 h", "6"], ["Langue vivante", "4 h", "6"]],
      "note": "Mêmes copies que les ENS, qui ont leurs propres coefficients."},
    "adm": {"quand": "le 27 mai 2026", "txt": "La barre est fixée par le jury sur le total des écrits."},
    "oraux": {"quand": "8-14 juin 2026", "l": [
      ["Mathématiques", "50 min", "23"], ["Informatique", "50 min", "22"], ["Physique", "50 min", "20"],
      ["Analyse de documents scientifiques (maths ou info)", "40 min", "15", "après 2 h de préparation"],
      ["Français", "30 min", "8", "après 45 min de préparation"], ["Langue vivante", "20 min", "8", "après 30 min de préparation"],
      ["Sport : 100 m, 1 000 m et 50 m nage libre", "", "5"]],
      "note": "Pas de TIPE à l'X."},
    "classement": "Écrits (39) + oraux (96) + sport (5) : 140 de coefficients.",
    "notice": S_XN, "src": [S_XE, S_XO, S_CAL]}]},
"ens": {
  "insc": ["0 €", "d'inscription"], "inscCourt": "Gratuit", "ecritsCourt": "Communs avec l'X",
  "poids": None, "poidsFait": "", "poidsCourt": "Selon l'ENS",
  "style": {
    "sujets": "Les écrits viennent de la banque commune avec l'X ; les ENS ajoutent une épreuve de maths C et une d'informatique fondamentale, avec des coefficients propres à chaque école et à chaque option.",
    "sujetsSrc": [S_ENSN],
    "oraux": "À l'oral d'informatique fondamentale, le jury attend qu'on annonce l'idée d'une preuve ou d'un algorithme avant de l'écrire, qu'on teste sur un petit exemple, et sanctionne « la répétition de ces erreurs de syntaxe ou de typage » en OCaml.",
    "orauxSrc": [S_ENS_INFO],
    "pourqui": "pour les passionnés de maths ou d'informatique attirés par la recherche, prêts à creuser une question longtemps.",
    "mots": "Recherche, info fondamentale"},
  "blocs": [{
    "titre": "Les quatre ENS",
    "ecrits": {"quand": "13-17 avril 2026", "l": [
      ["Mathématiques A", "4 h", ""], ["Mathématiques C", "4 h", ""], ["Informatique A", "4 h", ""], ["Informatique C", "4 h", ""],
      ["Informatique fondamentale", "4 h", ""], ["Physique", "4 h", "", "Ulm et Lyon seulement"], ["Français", "4 h", ""], ["Langue vivante", "4 h", ""]],
      "note": "Chaque ENS, et chaque option (maths ou info), a ses coefficients : voir la notice inter-ENS."},
    "adm": {"quand": "", "txt": "Chaque ENS fixe sa barre."},
    "oraux": {"quand": "", "l": [["Informatique", "", ""], ["Mathématiques", "", ""], ["TP d'algorithmique", "", ""], ["TIPE", "", "", "Lyon, Paris-Saclay et Rennes"], ["Langue vivante", "", ""]],
      "note": "Ulm ajoute un oral de physique."},
    "classement": "Chaque ENS a sa propre liste de classement, et chaque option la sienne.",
    "notice": S_ENSN, "src": [S_ENS_SACLAY]}]},
"mp": {
  "insc": ["360 €", "d'inscription, gratuit si boursier"], "inscCourt": "360 €", "ecritsCourt": "Communs avec Mines-Télécom",
  "poids": 58, "poidsFait": "du classement final vient des oraux", "poidsCourt": "58 %",
  "style": {
    "sujets": "Deux écrits d'informatique. En 2025, informatique 1 demandait des implémentations en C (arbres, ramasse-miettes, listes à enjambements) et informatique 2 mêlait C, SQL et graphes. Le jury rappelle qu'« une copie de concours n'est pas un brouillon personnel » et sanctionne les « idem » à la place de vraies fonctions.",
    "sujetsSrc": [S_CCMP_J],
    "oraux": "Coefficient 41 à l'oral contre 30 à l'écrit : maths (11), physique (7) et un TP d'informatique sur machine (6), plus TIPE, français et anglais.",
    "orauxSrc": [S_CCMP_R],
    "pourqui": "pour les profils solides en maths et en informatique, rigoureux à l'écrit.",
    "mots": "Deux infos, TP sur machine"},
  "blocs": [{
    "ecrits": {"quand": "27-30 avril 2026", "l": [
      ["Mathématiques I", "3 h", "4"], ["Mathématiques II", "4 h", "5"], ["Physique I", "3 h", "3"], ["Physique II", "3 h", "3"],
      ["Informatique I", "3 h", "3"], ["Informatique II", "4 h", "4"], ["Français", "3 h", "5"], ["Langue vivante", "1 h 30", "3"]],
      "note": "Ni chimie ni sciences industrielles en MPI."},
    "adm": {"quand": "le 3 juin 2026", "txt": "La barre est fixée par le jury sur le total des écrits. Moins de 3/20 en français : pas admissible."},
    "oraux": {"quand": "22 juin - 12 juillet 2026 (TIPE jusqu'au 18 juillet)", "l": [
      ["Mathématiques", "≈ 1 h 15", "11", "dont 15 min de préparation"], ["Physique", "≈ 1 h 15", "7", "dont 15 min de préparation"],
      ["TP d'informatique sur machine", "≈ 3 h 30", "6", "avec un compte rendu"],
      ["TIPE", "30 min", "6"], ["Français", "30 min", "6", "après 30 min de préparation"], ["Anglais", "20 min", "5", "après 20 min de préparation"]],
      "note": "Admissible aussi à Mines-Télécom ? Tu ne passes que les oraux Mines-Ponts, et Mines-Télécom reprend tes notes."},
    "classement": "Écrits (30) + oraux (41) : 71 de coefficients.",
    "notice": S_CCMP_R}]},
"mt": {
  "insc": ["325 €", "d'inscription, gratuit si boursier"], "inscCourt": "325 €", "ecritsCourt": "Ceux de Mines-Ponts",
  "poids": 50, "poidsFait": "du classement final vient des oraux", "poidsCourt": "50 %",
  "style": {
    "sujets": "Les mêmes sujets que Mines-Ponts, mais une barre d'admissibilité plus basse.",
    "sujetsSrc": [S_CCMP_J],
    "oraux": "Quatre oraux courts, tous à Paris en MPI : maths et informatique de 30 minutes, anglais, et un entretien de 25 minutes.",
    "orauxSrc": [S_CMT],
    "pourqui": "une suite naturelle si tu passes Mines-Ponts : aucun écrit en plus.",
    "mots": "Écrits des Mines, oraux courts"},
  "blocs": [{
    "ecrits": {"quand": "27-30 avril 2026", "l": [
      ["Mathématiques I", "3 h", "4"], ["Mathématiques II", "4 h", "5"], ["Physique I", "3 h", "3"], ["Physique II", "3 h", "3"],
      ["Informatique I", "3 h", "3"], ["Informatique II", "4 h", "4"], ["Français", "3 h", "5"], ["Langue vivante", "1 h 30", "3"]],
      "note": "Les mêmes copies que Mines-Ponts, avec les mêmes coefficients."},
    "adm": {"quand": "le 4 juin 2026", "txt": "Une barre plus basse que celle de Mines-Ponts."},
    "oraux": {"quand": "23 juin - 3 juillet 2026", "l": [
      ["Mathématiques", "30 min", "8"], ["Informatique", "30 min", "8"], ["Anglais", "20 min", "7"], ["Entretien", "25 min", "7"]],
      "note": "Pas de TIPE. Admissible aussi à Mines-Ponts : tu passes seulement les oraux Mines-Ponts, et tes notes sont reprises."},
    "classement": "Écrits (30) + oraux (30).",
    "notice": S_CMT, "src": [S_CMT_O]}]},
"cs": {
  "insc": ["0 à 140 €", "par école cochée, gratuit si boursier (15 € pour EPF et ESTP)"], "inscCourt": "0 à 140 € par école", "ecritsCourt": "Propres au concours",
  "poids": 50, "poidsFait": "du classement final vient des oraux", "poidsCourt": "50 %",
  "style": {
    "sujets": "Les maths pèsent lourd (18 et 18 sur 100), l'informatique 16. En 2025, maths 1 (commune avec la MP) a eu une moyenne de 9,7/20 ; la synthèse du rapport insiste sur la vérification des hypothèses des théorèmes.",
    "sujetsSrc": [S_CCS_J],
    "oraux": "Moitié écrit, moitié oral : maths (18), maths-informatique avec Python (18), physique-chimie, et deux TP de 3 h, physique-chimie (12) et informatique (16).",
    "orauxSrc": [S_CCS],
    "pourqui": "pour les candidats solides en maths, à l'aise avec Python et en TP d'informatique.",
    "mots": "Maths lourdes, TP d'info"},
  "blocs": [{
    "ecrits": {"quand": "4-7 mai 2026", "l": [
      ["Mathématiques 1", "4 h", "18"], ["Mathématiques 2", "4 h", "18"], ["Physique-chimie 1", "4 h", "10"], ["Physique-chimie 2", "4 h", "10"],
      ["Informatique", "4 h", "16"], ["Rédaction (français)", "4 h", "17"], ["Langue vivante", "4 h", "11"]],
      "note": "Coefficients de CentraleSupélec. Les autres écoles du concours ont leurs propres coefficients."},
    "adm": {"quand": "début juin 2026", "txt": "Les « grands admissibles », très bien classés à l'écrit, sont dispensés d'oraux."},
    "oraux": {"quand": "22 juin - 19 juillet 2026", "l": [
      ["Mathématiques", "30 min", "18"], ["Mathématiques et informatique", "30 min", "18", "après 30 min de préparation"], ["Physique-chimie", "30 min", "12"],
      ["TP de physique-chimie", "3 h", "12"], ["TP d'informatique", "3 h", "16"], ["TIPE", "30 min", "11"], ["Langue vivante", "20 min", "13", "après 20 min de préparation"]],
      "note": "Coefficients de CentraleSupélec. L'ENSEA et les autres écoles du concours ont leurs propres oraux."},
    "classement": "Écrits (100) + oraux (100). Chaque école fait son propre classement.",
    "notice": S_CCS, "src": [S_CS_E, S_CS_O]}]},
"inp": {
  "insc": ["240 €", "de dossier, gratuit si boursier ; + 0 à 105 € pour l'INSA ou la banque"], "inscCourt": "240 € + 0 à 105 €", "ecritsCourt": "Propres au concours",
  "poids": 41, "poidsFait": "du classement final vient des oraux", "poidsCourt": "41 %",
  "style": {
    "sujets": "En informatique 2025, OCaml et C autour de la complexité, des grammaires et des graphes ; le jury reproche de sauter les questions de preuve pour aller directement au code, et relève que « Quelques candidats semblent penser que NP signifie ”non polynomial” ».",
    "sujetsSrc": [S_INP_J],
    "oraux": "Les oraux comptent 40 sur 98 : maths (8), physique-chimie (8), informatique (10), langue et TIPE. Grand admissible, tu en es dispensé.",
    "orauxSrc": [S_INP_R],
    "pourqui": "pour les candidats réguliers et rigoureux, qui connaissent bien leur cours ; l'informatique y pèse lourd.",
    "mots": "Proche du cours, info au cœur"},
  "blocs": [{
    "ecrits": {"quand": "20-22 avril 2026", "l": [
      ["Mathématiques 1", "4 h", "11"], ["Mathématiques 2", "4 h", "11"], ["Physique-chimie", "4 h", "11"], ["Informatique", "4 h", "12"],
      ["Français-philosophie", "4 h", "9"], ["Langue vivante A", "3 h", "4"], ["Langue vivante B (facultative)", "1 h", "2", "seuls les points au-dessus de 10 comptent"]]},
    "adm": {"quand": "le 3 juin 2026", "txt": "La barre est fixée par le jury. Les « grands admissibles » sont dispensés d'oraux, pour les écoles du concours commun seulement."},
    "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [
      ["Mathématiques", "30 min", "8", "après 30 min de préparation"], ["Physique-chimie", "30 min", "8", "après 30 min de préparation"],
      ["Informatique", "30 min", "10", "après 30 min de préparation"], ["Langue vivante A", "30 min", "6", "après 30 min de préparation"], ["TIPE", "30 min", "8"]],
      "note": "Groupe INSA : dossier, écrits du CCINP et entretien. Écoles de la banque : écrits du CCINP, puis leurs propres oraux."},
    "classement": "Écrits (58, sans la langue B) + oraux (40) : 98 de coefficients.",
    "notice": S_INP_R, "src": [S_INP_P]}]},
"poly": {
  "insc": ["370 €", "dossier CCINP compris, gratuit si boursier"], "inscCourt": "370 €", "ecritsCourt": "Maths et physique-chimie propres, le reste avec le CCINP",
  "poids": 20, "poidsFait": "du classement final vient du TIPE, le seul oral", "poidsCourt": "20 % (TIPE seul)",
  "style": {
    "sujets": "Les maths et la physique-chimie sont des sujets propres à e3a-Polytech ; l'informatique, le français et les langues sont les copies du CCINP. En MPI, l'informatique compte autant que les maths (8 chacune).",
    "sujetsSrc": [S_E3A],
    "oraux": "Un seul oral, le TIPE, qui compte 8 sur 40. Pas d'entretien de motivation.",
    "orauxSrc": [S_E3A],
    "pourqui": "pour les candidats réguliers qui veulent un concours où l'écrit pèse presque tout, sur une liste propre à la MPI.",
    "mots": "Liste MPI à part"},
  "blocs": [{
    "ecrits": {"quand": "21-24 avril 2026", "l": [
      ["Mathématiques (e3a-Polytech)", "4 h", "8"], ["Physique-chimie (e3a-Polytech)", "4 h", "6"], ["Informatique", "4 h", "8", "avec le CCINP"],
      ["Français-philosophie", "4 h", "5", "avec le CCINP"], ["Langue vivante A", "3 h", "5", "avec le CCINP"],
      ["Langue vivante B (facultative)", "1 h", "2", "seuls les points au-dessus de 10 comptent"]]},
    "adm": {"quand": "le 3 juin 2026", "txt": "La barre est fixée par le jury. Les « grands admissibles » sont dispensés du TIPE."},
    "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [["TIPE", "30 min", "8"]]},
    "classement": "Écrits (32, sans la langue B) + TIPE (8). Les MPI ont leur propre liste de classement : 99 places en 2026.",
    "notice": S_E3A}]},
"e3a": {
  "insc": ["240 €", "de dossier CCINP, gratuit si boursier ; + 0 à 65 € selon le concours"], "inscCourt": "240 € + 0 à 65 €", "ecritsCourt": "Ceux de Polytech",
  "poids": None, "poidsFait": "", "poidsCourt": "Selon l'école",
  "style": {
    "sujets": "Les mêmes sujets que Polytech : maths et physique-chimie propres à e3a-Polytech, le reste en commun avec le CCINP.",
    "sujetsSrc": [S_E3A],
    "oraux": "Surtout des entretiens, propres à chaque école.",
    "orauxSrc": [S_E3A],
    "pourqui": "pour viser des écoles souvent privées ou spécialisées, où ton projet compte à l'entretien.",
    "mots": "Écrits de Polytech, entretiens"},
  "blocs": [{
    "ecrits": {"quand": "21-24 avril 2026", "l": [
      ["Mathématiques (e3a-Polytech)", "4 h", ""], ["Physique-chimie (e3a-Polytech)", "4 h", ""], ["Informatique", "4 h", ""],
      ["Français-philosophie", "4 h", ""], ["Langue vivante A", "3 h", ""], ["Langue vivante B (facultative)", "1 h", ""]],
      "note": "Coefficients en maths, physique-chimie, informatique, français et langue A : Avenir Prépas 6, 4, 4, 3, 3 ; Ingéni'Up 5, 4, 5, 3, 2. Chaque école indépendante a les siens."},
    "adm": {"quand": "", "txt": "Avenir Prépas, Ingéni'Up et chaque école indépendante ont leur propre jury."},
    "oraux": {"quand": "", "l": [],
      "note": "Avenir Prépas : un entretien dans les écoles (coefficient 9 en MPI). Ingéni'Up : un entretien (coefficient 7). Écoles indépendantes : un oral ou un entretien selon l'école ; l'EIDD n'en a pas."},
    "notice": S_E3A}]},
"autres": {
  "insc": ["100 €", "EPITA ou CESI ; UT : non trouvé"], "inscCourt": "100 € ; UT : non trouvé", "ecritsCourt": "Propres à chaque concours",
  "poids": None, "poidsFait": "", "poidsCourt": "Selon le concours",
  "style": {"mots": "Épreuves propres"},
  "blocs": [
    {"titre": "Concours EPITA-IPSA-ESME",
     "ecrits": {"quand": "avril 2026", "l": [["Mathématiques", "3 h", "6"], ["Anglais", "2 h 30", "3"], ["Option au choix", "2 h", "5"]]},
     "oraux": {"quand": "4-14 juin 2026", "l": [["Entretien, en français et en anglais", "30 min", "7"], ["Oral d'innovation, en groupe", "3 h 30", "6"]]},
     "notice": S_EP26},
    {"titre": "Concours CESI",
     "ecrits": {"quand": "8-9 avril 2026", "l": [["Mathématiques", "", ""], ["Physique", "", ""], ["Anglais", "", ""], ["Français", "", ""]]},
     "oraux": {"quand": "", "l": [["Entretien", "", ""]]},
     "notice": S_CESI},
    {"titre": "Groupe UT (UTC, UTT, UTBM)",
     "txt": "Sur dossier, puis entretien, en dehors du SCEI : calendrier et démarches à part.",
     "notice": S_UT}]},
}

CONC_MPI = {
  "x": {"frais": "220 € (gratuit pour les boursiers).",
        "savoir": ["En MPI, seule l'X recrute par ce concours : l'ESPCI n'a pas de places en MPI.",
                   "Pas de TIPE : aux oraux, maths, informatique et physique (50 min chacun) et une analyse de documents scientifiques.",
                   "Les ENS utilisent aussi les écrits de cette banque, avec leurs propres coefficients : voir la page ENS."],
        "src": [S_FRAIS, S_XN, S_X_ONISEP]},
  "ens": {"savoir": ["Les ENS sont des écoles de recherche : elles forment surtout de futurs chercheurs, enseignants-chercheurs et professeurs agrégés.",
                     "Une partie des écrits est commune avec l'X ; les ENS ajoutent maths C et informatique fondamentale.",
                     "Admis par concours, tu deviens élève fonctionnaire stagiaire : payé pendant les études, contre un engagement de 10 ans dans la fonction publique, études comprises.",
                     "En MPI, les quatre ENS recrutent : Ulm (12 postes en 2026) et Paris-Saclay (14) avec une option maths et une option info, Lyon avec deux concours (maths, info), Rennes en informatique.",
                     "Chaque ENS, et chaque option, a sa propre liste de classement ; les rangs ne comptent que les candidats « fonctionnarisables »."],
          "src": [S_FRAIS, S_ENSN, S_ENS_SACLAY, S_SCEI]},
  "ccmp": {"savoir": ["Concours commun : t'inscrire, c'est t'inscrire à toutes ses écoles. Tu choisis celles que tu gardes dans ta liste de vœux, à arrêter avant fin juillet.",
                      "En MPI, deux écrits d'informatique (3 h et 4 h) et un TP d'informatique sur machine à l'oral ; ni chimie ni sciences industrielles.",
                      "Ses écrits servent aussi au concours Mines-Télécom.",
                      "Pas de places MPI en 2026 sur le campus de Brest de l'ENSTA ni à Chimie ParisTech."],
           "src": [S_CCMP_N, S_CCMP_R]},
  "cmt": {"savoir": ["Il utilise les écrits de Mines-Ponts, avec une seule barre d'admissibilité, plus basse.",
                     "En MPI, l'oral d'informatique remplace celui de physique, et tous les oraux ont lieu à Paris.",
                     "Si tu es admissible à Mines-Ponts, tu passes les oraux Mines-Ponts, plus exigeants, et ces notes servent aussi pour Mines-Télécom : un oral raté compte pour les deux (règlement Mines-Ponts 2026).",
                     "2026 : l'ENAC et l'ISAE-ENSMA ont quitté le CCINP pour ce concours ; l'ENSTA y ouvre sa formation défense et sécurité (FIDS)."],
          "src": [S_CMT, S_CCMP_R]},
  "ccs": {"frais": "École par école : 140 € par Centrale ou SupOptique ; 85 € ENSEA, EPF ou ESTP ; Navale gratuite. Boursiers : gratuit (15 € pour EPF et ESTP).",
          "savoir": ["2027 : une seule inscription et une seule barre d'admissibilité pour CentraleSupélec, les quatre Centrale et SupOptique ; le résumé de l'épreuve de rédaction comptera pour l'admissibilité et la dissertation pour l'admission ; en principe, un seul TP par filière aux oraux. Le prix de cette inscription unique n'est pas encore publié.",
                     "En MPI, deux TP aux oraux : physique-chimie et informatique.",
                     "Arts et Métiers et AgroParisTech ne recrutent pas en MPI. Centrale Lille ouvre aussi 5 places à l'IG2I de Lens (informatique).",
                     "Les écoles ne partagent pas toutes les mêmes oraux : l'ENSEA et Navale ont les leurs, l'EPF fait passer des ateliers et un entretien non scientifiques, et l'ESTP n'a pas d'oral obligatoire (notice 2026)."],
          "src": [S_FRAIS, S_CCS, S_CS_O, src("CentraleSupélec : décisions du conseil d'administration du 18 juin 2025 (concours 2027)", "https://www.centralesupelec.fr/sites/default/files/documents/D%C3%A9lib%C3%A9rations_CA18062025.pdf")]},
  "ccinp": {"savoir": ["Les candidats très bien classés aux écrits peuvent être « grands admissibles » et éviter les oraux, pour les écoles du concours commun (règlement 2026).",
                       "En MPI, l'informatique a le plus gros coefficient de l'écrit (12) et compte 10 aux oraux.",
                       "2026 : l'ENAC et l'ISAE-ENSMA sont parties à Mines-Télécom."],
            "src": [S_INP_P, S_INP_R, S_FRAIS]},
  "bccinp": {"src": [S_INP_P, S_FRAIS]},
  "e3a_poly": {"savoir": ["Français, langues et informatique : les mêmes copies que le CCINP. Maths et physique-chimie : des sujets propres à e3a-Polytech.",
                          "En MPI, une liste séparée de 99 places en 2026 : les MPI ne sont pas classés avec les MP, PC et PSI."],
               "src": [S_E3A, S_FRAIS]},
  "e3a_ind": {"src": [S_E3A, S_FRAIS]},
  "avenir": {"savoir": ["2026 : peu de places en MPI (26), dont 12 à l'ESILV Paris. Builders n'en a pas."], "src": [S_E3A, S_FRAIS]},
  "ingeniup": {"savoir": ["Places données pour MP, MPI, PC et PSI ensemble.",
                          "Le SCEI ne publie pas, pour ce concours, le nombre d'intégrés de chaque filière : en 2025, 29 élèves au total, toutes filières confondues, sont entrés dans ses écoles."],
               "src": [S_E3A, S_FRAIS]},
}

FIL_OVER_MPI = {
  "ens_ulm": {"descF": {"MPI": "École de recherche : maths et informatique (concours MPI)"}, "domF": {"MPI": ["rech", "math", "info"]}, "noteF": {"MPI": None}},
  "ens_saclay": {"descF": {"MPI": "École de recherche (concours MPI, option maths ou info)"}, "domF": {"MPI": ["rech", "math", "info"]}, "noteF": {"MPI": None}},
  "ens_lyon": {"descF": {"MPI": "École de recherche : maths et informatique (deux concours MPI)"}, "domF": {"MPI": ["rech", "math", "info"]}, "noteF": {"MPI": None}},
  "ens_rennes": {"descF": {"MPI": "École de recherche : informatique (concours MPI)"}, "domF": {"MPI": ["rech", "info"]}, "noteF": {"MPI": None}},
  "eigsi": {"noteF": {"MPI": "Le campus de Casablanca (1 place MPI) n'est pas listé : hors de France."}},
  "tps": {"noteF": {"MPI": None}},
}

FIL_MPI = {
  "familles": FAMILLES_MPI, "fees": FEES_MPI,
  "repere": {"mp": {"cids": ["ccmp"]}, "mt": {"cids": ["cmt"]}, "cs": {"cids": ["ccs"], "approx": True}, "inp": {"cids": ["ccinp"]}},
  "exclus": ["Formation de contrôleur aérien de l'ENAC (banque CCINP) : pas un diplôme d'ingénieur.",
             "Campus hors de France : Centrale Casablanca, EIGSI Casablanca.",
             "ECE : n'apparaît plus dans Avenir Prépas en 2026.",
             "Sans places en MPI en 2026 : ESPCI, Arts et Métiers, AgroParisTech, Chimie ParisTech, EIVP, ENSG Géologie, IMT Business School, plusieurs écoles du CCINP (écoles de chimie notamment) et plusieurs écoles indépendantes d'e3a (ENIT, ENSAIT, ESB, ISMANS, Paoli Tech)."],
  "sources": [S_SCEI, S_FRAIS, S_CCMP_N, S_CCMP_R, S_CMT, S_CCS, S_INP_P, S_INP_R, S_E3A, S_ENSN, S_ENS_SACLAY, S_XN, S_X_ONISEP, S_NAT, S_CAL, S_HAUSSE, S_CAL26, S_MAP],
  "maj": "2026-10-31",
}
