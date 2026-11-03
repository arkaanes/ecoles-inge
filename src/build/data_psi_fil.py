# -*- coding: utf-8 -*-
"""Filière PSI : pages concours (épreuves, coefficients, style), variantes des fiches concours, exclusions, sources.
Relevé le 31 octobre 2026 sur les notices et règlements 2026 et les rapports de jury 2025-2026."""
from data_concours import FEES as _FEES_MP

def src(t, u): return {"t": t, "u": u}

S_SCEI = src("Statistiques SCEI PSI 2025", "https://www.scei-concours.fr/stat2025/psi.html")
S_FRAIS = src("Frais de dossier PSI 2026 (SCEI)", "https://www.scei-concours.fr/pdf/frais_PSI2026.pdf")
S_XN = src("Notice du concours 2026 (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Notice%20du%20concours%202026%20publi%C3%A9e.pdf")
S_XE = src("Épreuves écrites PSI (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Epreuves%20%C3%A9crites%20PSI.pdf")
S_XO = src("Rapport de l'oral de maths PSI 2025 (École polytechnique)", "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Oral_PSI_Maths%20OK.pdf")
S_X_ONISEP = src("Fiche Onisep (places 2026 par filière)", "https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/essonne/ecole-polytechnique-institut-polytechnique-de-paris-etablissement-experimental/diplome-d-ingenieur-de-l-ecole-polytechnique-institut-polytechnique-de-paris")
S_ENSN = src("Notice inter-ENS 2026 (banque PSI, p. 17)", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/notice_interens_2026_mise_en_ligne_vf260212.pdf")
S_ENS_SACLAY = src("ENS Paris-Saclay : postes d'élèves ouverts en 2026", "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_postes_eleves_ouverts_ENS_Paris-Saclay.pdf")
S_ENS_ORAL = src("Rapport de l'oral de maths PSI 2025 (ENS)", "https://www.ens.psl.eu/sites/default/files/2025_psi_rapport_maths_oral.pdf")
S_CCMP_N = src("Notice des écoles Mines-Ponts 2026", "https://concoursminesponts.fr/wp-content/uploads/2025/12/notice-des-ecoles-2026-22.12.25.pdf")
S_CCMP_R = src("Règlement 2026 du concours Mines-Ponts", "https://concoursminesponts.fr/wp-content/uploads/2025/12/reglement-2026-09.12.25.pdf")
S_CCMP_J = src("Rapport du jury sur les écrits 2025 (Mines-Ponts)", "https://concoursminesponts.fr/wp-content/uploads/2025/10/Rapport-Ecrit-2025-VF.pdf")
S_CMT = src("Notice Mines-Télécom 2026", "https://cahier-de-prepa.fr/pc-descartes/download?id=260")
S_CMT_O = src("Les épreuves orales (site du concours Mines-Télécom)", "https://www.concours-mines-telecom.fr/le-concours-mines-telecom/les-epreuves-orales/")
S_CCS = src("Notice Centrale-Supélec 2026, filière PSI", "https://www.concours-centrale-supelec.fr/sites/default/files/documents/CCS_2026_PSI.pdf")
S_CCS_J = src("Rapport du jury, maths 1 PSI 2025 (Centrale-Supélec, via BibM@th)", "https://bibmath.net/pbs/centrale/centralepsi_2025_1_rapport.pdf")
S_INP_P = src("Places PSI 2026 (site du CCINP)", "https://www.concours-commun-inp.fr/fr/les-ecoles/les-places-dans-les-ecoles/places-psi.html")
S_INP_R = src("Règlement 2026 du CCINP", "https://www.concours-commun-inp.fr/_resource/R%C3%A8glement_VF_23-06.pdf?download=true")
S_INP_J = src("Maths PSI 2025 du CCINP : sujet et rapport du jury (Hadamard)", "https://www.hadamard.fr/annales/maths-ccinp-psi/2025")
S_E3A = src("Notice 2026 de la banque e3a-Polytech", "https://esigelec.fr/sites/default/files/2025-12/VF-Notice-2026-Banque-e3a-Polytech.pdf")
S_E3A_J = src("Rapport du jury, maths PSI 2025 (e3a-Polytech, via BibM@th)", "https://bibmath.net/pbs/e3a/e3a_2025_psi_rapport.pdf")
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

# Frais : barème PSI 2026 du SCEI. Identique à la MP, sauf l'ENSISA (25 €, 10 € pour les boursiers).
FEES_PSI = {k: list(v) for k, v in _FEES_MP.items()}
FEES_PSI["b_ensisa"] = ["Banque CCINP : ENSISA", 25, 10]

FAMILLES_PSI = {
"x": {
  "insc": ["220 €", "d'inscription, gratuit si boursier"], "inscCourt": "220 €", "ecritsCourt": "Communs avec les ENS",
  "poids": 58, "poidsFait": "du classement final vient des oraux, sport non compris", "poidsCourt": "58 %",
  "style": {
    "sujets": "Cinq écrits pour l'admissibilité, dont deux de 5 h : modélisation, et sciences industrielles. Les maths pèsent le plus (coefficient 10). L'informatique et la langue ne comptent qu'après l'admissibilité.",
    "sujetsSrc": [S_XE],
    "oraux": "Les oraux comptent 64 points, plus 4 de sport, sur 111. À l'oral de maths (50 min, 18), deux exercices au tableau : le jury apprécie qu'on prenne des initiatives et réagisse vite aux indications, et déconseille de faire des impasses sur le programme.",
    "orauxSrc": [S_XN, S_XO],
    "pourqui": "pour les très bons profils en maths et en physique, à l'aise au tableau et en manipulation.",
    "mots": "Maths lourdes, manips"},
  "blocs": [{
    "titre": "École polytechnique",
    "ecrits": {"quand": "13-17 avril 2026", "l": [
      ["Mathématiques", "4 h", "10"], ["Modélisation", "5 h", "5"], ["Physique", "4 h", "6"], ["Sciences industrielles", "5 h", "6"], ["Français", "4 h", "6"],
      ["Informatique", "2 h", "4", "compte seulement pour l'admission"], ["Langue vivante", "4 h", "6", "compte seulement pour l'admission"]],
      "note": "Mêmes copies que les ENS, qui ont leurs propres coefficients."},
    "adm": {"quand": "le 27 mai 2026", "txt": "La barre est fixée par le jury sur le total des écrits d'admissibilité."},
    "oraux": {"quand": "8-14 juin 2026", "l": [
      ["Mathématiques", "50 min", "18"], ["Physique", "50 min", "12"], ["Manipulation de physique", "", "6"],
      ["Manipulation et interrogation de sciences industrielles", "", "6"], ["Analyse de documents scientifiques (physique)", "40 min", "10", "après 2 h de préparation"],
      ["Français", "30 min", "6", "après 45 min de préparation"], ["Langue vivante", "20 min", "6", "après 30 min de préparation"],
      ["Sport : 100 m, 1 000 m et 50 m nage libre", "", "4"]],
      "note": "Pas de TIPE à l'X."},
    "classement": "Écrits (33 + 10 pour l'admission) + oraux (64) + sport (4) : 111 de coefficients.",
    "notice": S_XN, "src": [S_XE, S_CAL]}]},
"ens": {
  "insc": ["0 €", "d'inscription"], "inscCourt": "Gratuit", "ecritsCourt": "Communs avec l'X",
  "poids": 67, "poidsFait": "à Ulm du classement vient des oraux", "poidsCourt": "67 %",
  "style": {
    "sujets": "Les écrits viennent de la banque commune avec l'X, avec les coefficients de chaque ENS ; Ulm ajoute une composition de physique de 6 h. À Paris-Saclay et Rennes, les cinq écrits d'admissibilité ont presque le même poids (5 chacun, 4 pour le français).",
    "sujetsSrc": [S_ENSN],
    "oraux": "À l'oral de maths, le jury évalue surtout « une aptitude à analyser la question » et la réaction aux indications ; il pénalise ceux qui enchaînent vite les premières questions sans aller plus loin.",
    "orauxSrc": [S_ENS_ORAL],
    "pourqui": "pour les passionnés de physique ou de sciences de l'ingénieur attirés par la recherche, prêts à creuser une question longtemps.",
    "mots": "Recherche, raisonnement"},
  "blocs": [{
    "titre": "Exemple : ENS Ulm",
    "ecrits": {"quand": "13-17 avril 2026", "l": [
      ["Mathématiques", "4 h", "9"], ["Physique", "6 h", "12", "épreuve propre aux ENS"], ["Modélisation en sciences physiques et SI", "5 h", "7"],
      ["Français", "4 h", "8", "compte seulement pour l'admission"], ["Langue vivante", "4 h", "3", "compte seulement pour l'admission"]],
      "note": "Paris-Saclay et Rennes prennent maths, physique (4 h), sciences industrielles, modélisation et français (5 chacun, 4 pour le français), puis informatique et langue (2 chacune) pour l'admission."},
    "adm": {"quand": "", "txt": "Chaque ENS fixe sa barre."},
    "oraux": {"quand": "", "l": [
      ["Physique", "", "30"], ["Mathématiques", "", "23"], ["Manipulation de physique", "", "14"], ["TIPE", "", "8"], ["Langue vivante", "", "3"]],
      "note": "Paris-Saclay et Rennes : maths 5, manipulation de sciences industrielles 6, manipulation de physique 3, physique 3, TIPE 4, langue 2."},
    "classement": "Écrits (28 + 11 pour l'admission) + oraux (78) : 117 de coefficients. Chaque ENS a sa propre liste ; Paris-Saclay a deux concours PSI (Physique-PSI et SI-PSI).",
    "notice": S_ENSN, "src": [S_ENS_SACLAY]}]},
"mp": {
  "insc": ["360 €", "d'inscription, gratuit si boursier"], "inscCourt": "360 €", "ecritsCourt": "Communs avec Mines-Télécom",
  "poids": 58, "poidsFait": "du classement final vient des oraux", "poidsCourt": "58 %",
  "style": {
    "sujets": "En 2025, maths 1 portait sur les matrices semblables à leur inverse, maths 2 sur un modèle probabiliste d'épidémie. Le jury pointe des confusions de cours (matrice de symétrie et matrice symétrique, suites et séries de fonctions) et rappelle en physique qu'« il est également indispensable de vérifier l'homogénéité des expressions ».",
    "sujetsSrc": [S_CCMP_J],
    "oraux": "Coefficient 41 à l'oral contre 30 à l'écrit : maths (9) et physique (9), environ 1 h 15 chacun, puis un TP de 3 h 30 tiré au sort, en physique ou en sciences industrielles (6), plus TIPE, français et anglais.",
    "orauxSrc": [S_CCMP_R],
    "pourqui": "pour les profils solides en maths et en physique, rigoureux sur le cours et endurants.",
    "mots": "Programme large, oral tiré au sort"},
  "blocs": [{
    "ecrits": {"quand": "27-30 avril 2026", "l": [
      ["Mathématiques I", "3 h", "4"], ["Mathématiques II", "3 h", "3"], ["Physique I", "3 h", "3"], ["Physique II", "4 h", "4"], ["Chimie", "1 h 30", "2"],
      ["Sciences industrielles", "4 h", "4"], ["Informatique (commune)", "2 h", "2"], ["Français", "3 h", "5"], ["Langue vivante", "1 h 30", "3"]]},
    "adm": {"quand": "le 3 juin 2026", "txt": "Il faut atteindre deux minimums fixés par le jury : sur le total des écrits, et sur les quatre épreuves de maths et de physique. Moins de 3/20 en français : pas admissible."},
    "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [
      ["Mathématiques", "≈ 1 h 15", "9", "dont 15 min de préparation"], ["Physique", "≈ 1 h 15", "9", "dont 15 min de préparation"],
      ["TP de physique ou de sciences industrielles", "≈ 3 h 30", "6", "tiré au sort, avec un compte rendu"],
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
    "oraux": "Quatre oraux courts : maths et sciences industrielles de 30 minutes, anglais, et un entretien de 25 minutes. En PSI, l'oral de sciences industrielles remplace celui de physique.",
    "orauxSrc": [S_CMT],
    "pourqui": "une suite naturelle si tu passes Mines-Ponts : aucun écrit en plus.",
    "mots": "Écrits des Mines, oraux courts"},
  "blocs": [{
    "ecrits": {"quand": "27-30 avril 2026", "l": [
      ["Mathématiques I", "3 h", "4"], ["Mathématiques II", "3 h", "3"], ["Physique I", "3 h", "3"], ["Physique II", "4 h", "4"], ["Chimie", "1 h 30", "2"],
      ["Sciences industrielles", "4 h", "4"], ["Informatique (commune)", "2 h", "2"], ["Français", "3 h", "5"], ["Langue vivante", "1 h 30", "3"]],
      "note": "Les mêmes copies que Mines-Ponts, avec les mêmes coefficients."},
    "adm": {"quand": "le 4 juin 2026", "txt": "Une barre plus basse que celle de Mines-Ponts."},
    "oraux": {"quand": "23 juin - 10 juillet 2026", "l": [
      ["Mathématiques", "30 min", "8"], ["Sciences industrielles", "30 min", "8"], ["Anglais", "20 min", "7"], ["Entretien", "25 min", "7"]],
      "note": "Pas de TIPE. Admissible aussi à Mines-Ponts : tu passes seulement les oraux Mines-Ponts, et tes notes sont reprises."},
    "classement": "Écrits (30) + oraux (30).",
    "notice": S_CMT, "src": [S_CMT_O]}]},
"cs": {
  "insc": ["0 à 140 €", "par école cochée, gratuit si boursier (15 € pour EPF et ESTP)"], "inscCourt": "0 à 140 € par école", "ecritsCourt": "Propres au concours",
  "poids": 50, "poidsFait": "du classement final vient des oraux", "poidsCourt": "50 %",
  "style": {
    "sujets": "En maths 1 2025, un sujet sur le conditionnement d'une matrice, de longueur raisonnable mais qui mobilisait beaucoup de chapitres (normes, réduction, probabilités) ; peu de candidats ont atteint la dernière partie. Le jury exige des définitions précises et rappelle qu'« un majorant n'est pas nécessairement la borne supérieure ».",
    "sujetsSrc": [S_CCS_J],
    "oraux": "Moitié écrit, moitié oral. Deux oraux avec Python (maths et physique-chimie), et deux TP : physique-chimie (3 h) et sciences industrielles (4 h), à 14 chacun.",
    "orauxSrc": [S_CCS],
    "pourqui": "pour les candidats complets, à l'aise avec Python et en TP, notamment en sciences industrielles.",
    "mots": "Deux TP, Python"},
  "blocs": [{
    "ecrits": {"quand": "4-7 mai 2026", "l": [
      ["Mathématiques 1", "4 h", "15"], ["Mathématiques 2", "4 h", "15"], ["Physique-chimie 1", "4 h", "15"], ["Physique-chimie 2", "4 h", "15"],
      ["Sciences industrielles (S2I)", "4 h", "12"], ["Rédaction (français)", "4 h", "17"], ["Langue vivante", "4 h", "11"]],
      "note": "Coefficients de CentraleSupélec. Les autres écoles du concours ont leurs propres coefficients."},
    "adm": {"quand": "début juin 2026", "txt": "Les « grands admissibles », très bien classés à l'écrit, sont dispensés d'oraux."},
    "oraux": {"quand": "22 juin - 19 juillet 2026", "l": [
      ["Mathématiques", "30 min", "12"], ["Mathématiques et informatique (Python)", "30 min", "12", "après 30 min de préparation"], ["Physique-chimie", "30 min", "12"],
      ["Physique-chimie et informatique", "30 min", "12", "après 30 min de préparation"], ["TP de physique-chimie", "3 h", "14"], ["TP de sciences industrielles", "4 h", "14"],
      ["TIPE", "30 min", "11"], ["Langue vivante", "20 min", "13", "après 20 min de préparation"]],
      "note": "Coefficients de CentraleSupélec et de Centrale Lyon. Arts et Métiers, l'ENSEA et les autres écoles du concours ont leurs propres oraux."},
    "classement": "Écrits (100) + oraux (100). Chaque école fait son propre classement.",
    "notice": S_CCS, "src": [S_CS_E, S_CS_O]}]},
"inp": {
  "insc": ["240 €", "de dossier, gratuit si boursier ; + 0 à 105 € pour l'INSA ou la banque"], "inscCourt": "240 € + 0 à 105 €", "ecritsCourt": "Propres au concours",
  "poids": 41, "poidsFait": "du classement final vient des oraux", "poidsCourt": "41 %",
  "style": {
    "sujets": "En maths 2025, un exercice de probabilités puis deux problèmes (séries de Fourier, inégalité de Hadamard sur les déterminants), avec des questions faciles réparties partout. Le jury conseille de sauter une partie trop dure pour traiter la suite, et préfère « Mieux vaut ne rien indiquer » à une affirmation non justifiée.",
    "sujetsSrc": [S_INP_J],
    "oraux": "Les oraux comptent 40 sur 98 : maths (8), physique-chimie (8), un TP de sciences industrielles de 1 h 30 (10), langue et TIPE. Grand admissible, tu en es dispensé.",
    "orauxSrc": [S_INP_R],
    "pourqui": "pour les candidats réguliers et rigoureux, qui connaissent bien leur cours ; les sciences industrielles y pèsent lourd.",
    "mots": "Proche du cours, SI au cœur"},
  "blocs": [{
    "ecrits": {"quand": "20-23 avril 2026", "l": [
      ["Mathématiques", "4 h", "9"], ["Physique-chimie", "4 h", "9"], ["Modélisation et ingénierie numérique", "4 h", "9"], ["Sciences industrielles de l'ingénieur", "4 h", "12"],
      ["Français-philosophie", "4 h", "9"], ["Informatique", "3 h", "6"], ["Langue vivante A", "3 h", "4"],
      ["Langue vivante B (facultative)", "1 h", "2", "seuls les points au-dessus de 10 comptent"]]},
    "adm": {"quand": "le 3 juin 2026", "txt": "La barre est fixée par le jury. Les « grands admissibles » sont dispensés d'oraux, pour les écoles du concours commun seulement."},
    "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [
      ["Mathématiques", "30 min", "8", "après 30 min de préparation"], ["Physique-chimie", "30 min", "8", "après 30 min de préparation"],
      ["TP de sciences industrielles", "1 h 30", "10", "après 30 min de préparation"], ["Langue vivante A", "30 min", "6", "après 30 min de préparation"], ["TIPE", "30 min", "8"]],
      "note": "Groupe INSA : dossier, écrits du CCINP et entretien. Écoles de la banque : écrits du CCINP, puis leurs propres oraux."},
    "classement": "Écrits (58, sans la langue B) + oraux (40) : 98 de coefficients.",
    "notice": S_INP_R, "src": [S_INP_P]}]},
"poly": {
  "insc": ["370 €", "dossier CCINP compris, gratuit si boursier"], "inscCourt": "370 €", "ecritsCourt": "Maths et physique-chimie propres, le reste avec le CCINP",
  "poids": 20, "poidsFait": "du classement final vient du TIPE, le seul oral", "poidsCourt": "20 % (TIPE seul)",
  "style": {
    "sujets": "Les maths et la physique-chimie sont des sujets propres à e3a-Polytech. En maths 2025, trois exercices (séries de fonctions, extremums par diagonalisation, système différentiel) ; le jury rappelle que « toute proposition énoncée dans une copie se doit d'être démontrée » et préfère qu'on admette clairement un résultat pour avancer.",
    "sujetsSrc": [S_E3A_J],
    "oraux": "Un seul oral, le TIPE, qui compte 8 sur 40. Pas d'entretien de motivation.",
    "orauxSrc": [S_E3A],
    "pourqui": "pour les candidats réguliers, qui veulent un concours où l'écrit pèse presque tout.",
    "mots": "Écrit d'abord, peu d'oral"},
  "blocs": [{
    "ecrits": {"quand": "21-24 avril 2026", "l": [
      ["Mathématiques (e3a-Polytech)", "4 h", "6"], ["Physique-chimie (e3a-Polytech)", "4 h", "6"], ["Sciences industrielles", "4 h", "6", "avec le CCINP"],
      ["Français-philosophie", "4 h", "5", "avec le CCINP"], ["Informatique", "3 h", "4", "avec le CCINP"], ["Langue vivante A", "3 h", "5", "avec le CCINP"],
      ["Langue vivante B (facultative)", "1 h", "2", "seuls les points au-dessus de 10 comptent"]]},
    "adm": {"quand": "le 3 juin 2026", "txt": "La barre est fixée par le jury. Les « grands admissibles » sont dispensés du TIPE."},
    "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [["TIPE", "30 min", "8"]]},
    "classement": "Écrits (32, sans la langue B) + TIPE (8). Les PSI sont ensuite classés avec les MP et les PC sur une liste commune.",
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
      ["Mathématiques (e3a-Polytech)", "4 h", ""], ["Physique-chimie (e3a-Polytech)", "4 h", ""], ["Sciences industrielles", "4 h", ""],
      ["Français-philosophie", "4 h", ""], ["Informatique", "3 h", ""], ["Langue vivante A", "3 h", ""], ["Langue vivante B (facultative)", "1 h", ""]],
      "note": "Coefficients en maths, physique-chimie, sciences industrielles, informatique, français et langue A : Avenir Prépas 4, 4, 6, 2, 3, 3 ; Ingéni'Up 4, 4, 3, 3, 3, 2. Chaque école indépendante a les siens."},
    "adm": {"quand": "", "txt": "Avenir Prépas, Ingéni'Up et chaque école indépendante ont leur propre jury."},
    "oraux": {"quand": "", "l": [],
      "note": "Avenir Prépas : un entretien dans les écoles (coefficient 10 en PSI). Ingéni'Up : un entretien (coefficient 7). Écoles indépendantes : un oral ou un entretien, de coefficient 10 à 28 selon l'école ; l'EIDD et Paoli Tech n'en ont pas."},
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

CONC_PSI = {
  "x": {"frais": "220 € (gratuit pour les boursiers).",
        "savoir": ["En PSI, seule l'X recrute par ce concours : l'ESPCI n'a pas de places en PSI.",
                   "Pas de TIPE : aux oraux, une manipulation de physique, une de sciences industrielles et une analyse de documents scientifiques.",
                   "Les ENS utilisent aussi les écrits de cette banque, avec leurs propres coefficients : voir la page ENS."],
        "src": [S_FRAIS, S_XN, S_X_ONISEP]},
  "ens": {"savoir": ["Les ENS sont des écoles de recherche : elles forment surtout de futurs chercheurs, enseignants-chercheurs et professeurs agrégés.",
                     "Une partie des écrits est commune avec l'X ; chaque ENS ajoute ses propres épreuves ou coefficients.",
                     "Admis par concours, tu deviens élève fonctionnaire stagiaire : payé pendant les études, contre un engagement de 10 ans dans la fonction publique, études comprises.",
                     "En PSI, trois ENS recrutent : Paris-Saclay (deux concours, Physique-PSI et SI-PSI, 18 postes chacun en 2026), Rennes et Ulm. L'ENS de Lyon ne recrute pas en PSI.",
                     "Chaque ENS, et chaque concours, a sa propre liste de classement ; les rangs ne comptent que les candidats « fonctionnarisables »."],
          "src": [S_FRAIS, S_ENSN, S_ENS_SACLAY, S_SCEI]},
  "ccmp": {"savoir": ["Concours commun : t'inscrire, c'est t'inscrire à toutes ses écoles. Tu choisis celles que tu gardes dans ta liste de vœux, à arrêter avant fin juillet.",
                      "Double barre d'admissibilité : un minimum sur le total des écrits, un autre sur les quatre épreuves de maths et de physique (règlement 2026).",
                      "En PSI, les sciences industrielles comptent à l'écrit (4 h, coefficient 4) ; à l'oral, une épreuve de physique ou de sciences industrielles est tirée au sort.",
                      "Ses écrits servent aussi au concours Mines-Télécom.",
                      "L'ENSTA (fusion Paris + Brest) propose 34 places PSI à Brest en 2026. Chimie ParisTech n'a que 3 places en PSI."],
           "src": [S_CCMP_N, S_CCMP_R]},
  "cmt": {"savoir": ["Il utilise les écrits de Mines-Ponts, avec une seule barre d'admissibilité, plus basse.",
                     "En PSI, l'oral de sciences industrielles remplace celui de physique.",
                     "Si tu es admissible à Mines-Ponts, tu passes les oraux Mines-Ponts, plus exigeants, et ces notes servent aussi pour Mines-Télécom : un oral raté compte pour les deux (règlement Mines-Ponts 2026).",
                     "2026 : l'ENAC et l'ISAE-ENSMA ont quitté le CCINP pour ce concours ; l'ENSTA y ouvre sa formation défense et sécurité (FIDS)."],
          "src": [S_CMT, S_CCMP_R]},
  "ccs": {"savoir": ["2027 : une seule inscription et une seule barre d'admissibilité pour CentraleSupélec, les quatre Centrale et SupOptique ; le résumé de l'épreuve de rédaction comptera pour l'admissibilité et la dissertation pour l'admission ; en principe, un seul TP par filière aux oraux. Le prix de cette inscription unique n'est pas encore publié.",
                     "En PSI, deux TP aux oraux : physique-chimie et sciences industrielles.",
                     "Les écoles ne partagent pas toutes les mêmes oraux : l'ENSEA et Navale ont les leurs, l'EPF fait passer des ateliers et un entretien non scientifiques, et l'ESTP n'a pas d'oral obligatoire (notice 2026).",
                     "Arts et Métiers ouvre 260 places en PSI en 2026 (53 en MP). Le campus est attribué après l'admission, selon ton rang, et la 1re année se fait en province (Aix-en-Provence ou Angers en PSI)."],
          "src": [S_FRAIS, S_CCS, S_CS_O, src("CentraleSupélec : décisions du conseil d'administration du 18 juin 2025 (concours 2027)", "https://www.centralesupelec.fr/sites/default/files/documents/D%C3%A9lib%C3%A9rations_CA18062025.pdf")]},
  "ccinp": {"savoir": ["Les candidats très bien classés aux écrits peuvent être « grands admissibles » et éviter les oraux, pour les écoles du concours commun (règlement 2026).",
                       "En PSI, les sciences industrielles ont le plus gros coefficient de l'écrit (12), et un TP de sciences industrielles compte 10 aux oraux.",
                       "2026 : l'ENAC et l'ISAE-ENSMA sont parties à Mines-Télécom."],
            "src": [S_INP_P, S_INP_R, S_FRAIS]},
  "bccinp": {"src": [S_INP_P, S_FRAIS]},
  "e3a_poly": {"savoir": ["Français, langues, informatique et sciences industrielles : les mêmes copies que le CCINP. Maths et physique-chimie : des sujets propres à e3a-Polytech.",
                          "Classement commun MP, PC et PSI : les places et les rangs mélangent les filières."],
               "src": [S_E3A, S_FRAIS]},
  "e3a_ind": {"src": [S_E3A, S_FRAIS]},
  "avenir": {"src": [S_E3A, S_FRAIS]},
  "ingeniup": {"savoir": ["Places données pour MP, MPI, PC et PSI ensemble.",
                          "Le SCEI ne publie pas, pour ce concours, le nombre d'intégrés de chaque filière : en 2025, 29 élèves au total, toutes filières confondues, sont entrés dans ses écoles."],
               "src": [S_E3A, S_FRAIS]},
}

# Description, domaines ou note propres à la PSI (fusionnés avec ceux des autres filières)
FIL_OVER_PSI = {
  "ens_ulm": {"descF": {"PSI": "École de recherche : physique (concours PSI)"}, "noteF": {"PSI": None}},
  "ens_saclay": {"descF": {"PSI": "École de recherche (concours Physique-PSI et SI-PSI)"}, "domF": {"PSI": ["rech", "physique", "meca"]}, "noteF": {"PSI": None}},
  "ens_rennes": {"descF": {"PSI": "École de recherche (concours PSI)"}, "noteF": {"PSI": None}},
  "eigsi": {"noteF": {"PSI": "Le campus de Casablanca (1 place PSI) n'est pas listé : hors de France."}},
  "tps": {"noteF": {"PSI": None}},
}

FIL_PSI = {
  "familles": FAMILLES_PSI, "fees": FEES_PSI,
  "repere": {"mp": {"cids": ["ccmp"]}, "mt": {"cids": ["cmt"]}, "cs": {"cids": ["ccs"], "approx": True}, "inp": {"cids": ["ccinp"]}},
  "exclus": ["IMT Business School (concours Mines-Télécom) : école de commerce.",
             "Formation de contrôleur aérien de l'ENAC (banque CCINP) : pas un diplôme d'ingénieur.",
             "Campus hors de France : Centrale Casablanca, EIGSI Casablanca.",
             "Voies réservées aux candidats étrangers (cycle international Centrale-Supélec, places « étrangers » de CentraleSupélec et de SupOptique, places de l'École navale pour les candidats allemands).",
             "ECE : n'apparaît plus dans Avenir Prépas en 2026.",
             "Sans places en PSI en 2026 : ESPCI, AgroParisTech, ENS de Lyon, ENSCL et les écoles de chimie qui ne recrutent qu'en PC."],
  "sources": [S_SCEI, S_FRAIS, S_CCMP_N, S_CCMP_R, S_CMT, S_CCS, S_INP_P, S_INP_R, S_E3A, S_ENSN, S_ENS_SACLAY, S_XN, S_X_ONISEP, S_NAT, S_CAL, S_HAUSSE, S_CAL26, S_MAP],
  "maj": "2026-10-31",
}
