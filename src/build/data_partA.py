# -*- coding: utf-8 -*-
"""Partie A : épreuves, poids des oraux et style de chaque famille de concours (filière MP, session 2026).

Chaque épreuve : [nom, durée, coefficient, précision facultative].
Relevé le 19 octobre 2026 ; les notices 2027 ne sont pas encore publiées.
"""
from data_common import src, S_CCINP26, S_EP26, S_CESI26, S_UT

# ---------- sources ----------
N_X = src("Notice du concours 2026 (École polytechnique)",
          "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Notice%20du%20concours%202026%20publi%C3%A9e.pdf")
N_ENS = src("Notice inter-ENS 2026", "https://www.ens.psl.eu/sites/default/files/vf_notice_interens_2026_v10122025.pdf")
S_ULM = src("Le concours MP de l'ENS (Ulm)",
            "https://www.ens.psl.eu/une-formation-d-exception/admission-concours/concours-voie-cpge/concours-voie-cpge-sciences/le-0")
S_XENS_STRUCT = src("Structure des écrits MP X-ENS 2026", "https://banques-ecoles.fr/cms/wp-content/uploads/2025/12/26_structure_MP_bq.pdf")
N_CCMP = src("Règlement 2026 du concours Mines-Ponts", "https://concoursminesponts.fr/wp-content/uploads/2025/12/reglement-2026-09.12.25.pdf")
N_CMT = src("Notice du concours Mines-Télécom 2026", "https://www.calameo.com/read/0053254304882589d7185")
S_CMT_ORAUX = src("Les épreuves orales (site du concours Mines-Télécom)",
                  "https://www.concours-mines-telecom.fr/le-concours-mines-telecom/les-epreuves-orales/")
S_CMT_LE = src("Mines-Télécom 2026, mode d'emploi (L'Étudiant)",
               "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-mines-telecom-mode-d-emploi.html")
N_CCS = src("Épreuves écrites (site du concours Centrale-Supélec)", "https://www.concours-centrale-supelec.fr/epreuves-ecrites")
S_CCS_LE = src("Centrale-Supélec 2026, mode d'emploi (L'Étudiant)",
               "https://www.letudiant.fr/etudes/ecole-ingenieur/ecoles-d-ingenieurs-post-prepa-le-concours-centrale-supelec-mode-d-emploi.html")
S_CCS_ORAUX = src("Oraux Centrale-Supélec 2026 (Hadamard)", "https://www.hadamard.fr/actualites/oraux-centrale-supelec-modalites-coefficients-2026")
S_COEF_MP = src("Coefficients des écrits MP 2026 (Hadamard)", "https://www.hadamard.fr/actualites/coefficients-concours-x-ens-mines-ponts-centrale-ccinp")
N_CCINP = src("Règlement 2026 du CCINP", "https://www.concours-commun-inp.fr/_resource/R%C3%A8glement_VF_23-06.pdf?download=true")
N_E3A = src("Notice 2026 de la banque e3a-Polytech", "https://esigelec.fr/sites/default/files/2025-12/VF-Notice-2026-Banque-e3a-Polytech.pdf")

R_X = src("Rapport du jury, maths A MP-MPI 2026", "https://fichiers.wikiprepa.fr/data/x-ens_maths-a_mp-mpi_2026_rapport_jury.pdf")
R_X_ORAL = src("Rapport de l'oral de maths MP 2025 (École polytechnique)",
               "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Oral_MP_Maths%20OK.pdf")
R_ENS = src("Rapport du jury, maths C MP 2025 (inter-ENS)", "https://www.doc-solus.fr/prepa/sci/adc/pdf/rapports.pdf/2025/MP_MATHS_ENS_1_2025.rapport.pdf")
R_CCMP = src("Rapport du jury sur les écrits 2025 (Mines-Ponts)", "https://concoursminesponts.fr/wp-content/uploads/2025/10/Rapport-Ecrit-2025-VF.pdf")
R_CCS = src("Rapport du jury, maths 1 PC 2025 (Centrale-Supélec)", "https://bibmath.net/pbs/centrale/centralepc_2025_1_rapport.pdf")
R_CCINP = src("Rapport du jury, maths 1 MP 2024 (CCINP)", "https://doc-solus.fr/prepa/sci/adc/pdf/rapports.pdf/2024/MP_MATHS_CCP_1_2024.rapport.pdf")
R_E3A = src("Rapport du jury, maths MP 2023 (e3a)", "https://www.bibmath.net/pbs/e3a/e3a_2023_mp_rapport.pdf")

# Écrits de Mines-Ponts, repris tels quels par Mines-Télécom
ECRITS_MINES = [["Mathématiques I", "3 h", "4"], ["Mathématiques II", "4 h", "5"], ["Physique I", "3 h", "3"],
                ["Physique II", "3 h", "4"], ["Chimie", "1 h 30", "2"], ["Informatique (commune)", "2 h", "2"],
                ["Informatique ou sciences de l'ingénieur (option)", "3 h", "2"], ["Français", "3 h", "5"],
                ["Langue vivante", "1 h 30", "3"]]

FAMILLES = {
 "x": {
  "insc": ["220 €", "d'inscription, gratuit si boursier"], "inscCourt": "220 €",
  "ecritsCourt": "Communs avec les ENS",
  "poids": 66, "poidsFait": "du classement final vient des oraux, sport non compris", "poidsCourt": "66 %",
  "style": {
   "sujets": "Des sujets progressifs mais longs. En maths A 2026, le jury écrit qu'« il n'était donc pas nécessaire de traiter tout le sujet pour obtenir une très bonne note » : les meilleures copies ont traité avec soin les questions de difficulté intermédiaire, et les phrases trop vagues ont coûté des points.",
   "sujetsSrc": [R_X],
   "oraux": "Les oraux comptent 92 points sur 140 : deux oraux de maths de 50 minutes (16 chacun) et un de physique (20). À l'oral de maths, le jury insiste sur l'autonomie et l'initiative.",
   "orauxSrc": [R_X_ORAL],
   "pourqui": "pour les très bons profils en maths et en physique, qui aiment chercher seuls et défendre leurs idées à l'oral.",
   "mots": "Sujets longs, oraux décisifs"},
  "blocs": [{
   "ecrits": {"quand": "13-17 avril 2026", "l": [
     ["Mathématiques A", "4 h", "8"], ["Mathématiques B", "4 h", "7"], ["Physique", "4 h", "6"],
     ["Informatique A", "4 h", "6", "option informatique ; compte 10 au classement final"],
     ["Physique et sciences de l'ingénieur", "4 h", "6", "option PSI"],
     ["Informatique B", "2 h", "4", "option PSI ; compte seulement pour l'admission"],
     ["Français", "4 h", "6"], ["Langue vivante", "4 h", "6"]],
    "note": "Tu choisis ton option à l'inscription, et chaque option a son propre classement."},
   "adm": {"quand": "le 27 mai en 2026", "txt": "La barre est fixée par le jury sur le total des écrits."},
   "oraux": {"quand": "15 juin - 5 juillet 2026", "l": [
     ["Mathématiques, 1re interrogation", "50 min", "16"], ["Mathématiques, 2e interrogation", "50 min", "16"],
     ["Physique", "50 min", "20"], ["Chimie", "40 min", "9"],
     ["Analyse de documents scientifiques", "40 min", "15", "après 2 h de préparation"],
     ["Français", "30 min", "8", "après 45 min de préparation"],
     ["Langue vivante", "20 min", "8", "après 30 min de préparation"],
     ["Sport : 100 m, 1 000 m et 50 m nage libre", "", "5"]],
    "note": "Pas de TIPE à l'X."},
   "classement": "Écrits (43) + oraux (92) + sport (5) : 140 de coefficients au total.",
   "notice": N_X}]},

 "ens": {
  "insc": ["0 €", "d'inscription"], "inscCourt": "Gratuit",
  "ecritsCourt": "Communs avec l'X",
  "poids": 73, "poidsFait": "du classement vient des oraux à Ulm, option physique", "poidsCourt": "73 % à Ulm (option physique)",
  "style": {
   "sujets": "Des sujets exigeants, de difficulté très inégale : en maths C 2025, la plupart des copies n'ont abordé que la première partie (moyenne 9,7/20). Le jury attend « clarté, précision et rigueur », et apprécie qu'on annonce honnêtement une piste de démonstration.",
   "sujetsSrc": [R_ENS],
   "oraux": "À Ulm, option physique, les oraux font 73 % du total : l'oral de maths I compte à lui seul 30.",
   "orauxSrc": [S_ULM],
   "pourqui": "pour les passionnés de maths ou de physique attirés par la recherche, prêts à creuser une question longtemps.",
   "mots": "Recherche, oraux décisifs"},
  "blocs": [{
   "titre": "Exemple : ENS Ulm, option physique",
   "ecrits": {"quand": "13-17 avril 2026", "l": [
     ["Physique", "4 h", "6"], ["Mathématiques C", "4 h", "4"], ["Mathématiques D", "6 h", "6"],
     ["Français", "4 h", "8", "compte pour l'admission"], ["Langue vivante", "4 h", "3", "compte pour l'admission"]],
    "note": "Les autres ENS, et les options informatique, prennent aussi maths A, informatique A ou informatique fondamentale, avec leurs propres coefficients."},
   "adm": {"quand": "le 27 mai en 2026", "txt": "Chaque ENS fixe sa barre."},
   "oraux": {"quand": "8-27 juin 2026", "l": [
     ["Mathématiques I", "", "30"], ["Mathématiques II", "", "15"], ["Physique", "", "25"], ["Langue vivante", "", "3"]]},
   "classement": "Chaque ENS, et chaque option, a sa propre liste de classement.",
   "notice": N_ENS, "src": [S_ULM, S_XENS_STRUCT]}]},

 "mp": {
  "insc": ["360 €", "d'inscription, gratuit si boursier"], "inscCourt": "360 €",
  "ecritsCourt": "Communs avec Mines-Télécom",
  "poids": 55, "poidsFait": "du classement final vient des oraux", "poidsCourt": "55 %",
  "style": {
   "sujets": "Des sujets longs : en 2025, le jury juge maths I « un peu long » et maths II « très long », le barème en tenant compte. Il exige qu'on vérifie les hypothèses des théorèmes, et rappelle que « les tentatives de bluff n'apportent aucun point ».",
   "sujetsSrc": [R_CCMP],
   "oraux": "Coefficient 39 à l'oral contre 30 à l'écrit : les oraux pèsent plus lourd. Les oraux de maths et de physique, d'environ 1 h 15 chacun, comptent à eux seuls 22.",
   "orauxSrc": [N_CCMP],
   "pourqui": "pour les profils solides en maths et en physique, endurants sur des sujets longs et à l'aise au tableau.",
   "mots": "Sujets longs, oraux lourds"},
  "blocs": [{
   "ecrits": {"quand": "27-30 avril 2026", "l": ECRITS_MINES},
   "adm": {"quand": "le 3 juin en 2026", "txt": "Il faut atteindre deux minimums fixés par le jury : sur le total des écrits, et sur les quatre épreuves de maths et de physique. Moins de 3/20 en français : pas admissible."},
   "oraux": {"quand": "22 juin - 12 juillet 2026 (TIPE jusqu'au 18 juillet)", "l": [
     ["Mathématiques", "≈ 1 h 15", "12", "dont 15 min de préparation"],
     ["Physique", "≈ 1 h 15", "10", "dont 15 min de préparation"],
     ["TIPE", "30 min", "6"], ["Français", "30 min", "6", "après 30 min de préparation"],
     ["Anglais", "20 min", "5", "après 20 min de préparation"]],
    "note": "Admissible aussi à Mines-Télécom ? Tu ne passes que les oraux Mines-Ponts, et Mines-Télécom reprend tes notes."},
   "classement": "Écrits (30) + note d'option comptée une deuxième fois (2) + oraux (39) : 71 de coefficients.",
   "notice": N_CCMP}]},

 "mt": {
  "insc": ["325 €", "d'inscription, gratuit si boursier"], "inscCourt": "325 €",
  "ecritsCourt": "Ceux de Mines-Ponts",
  "poids": 50, "poidsFait": "du classement final vient des oraux", "poidsCourt": "50 %",
  "style": {
   "sujets": "Les mêmes sujets longs que Mines-Ponts, mais une barre d'admissibilité plus basse.",
   "sujetsSrc": [R_CCMP],
   "oraux": "Quatre oraux courts en une journée : maths et physique de 30 minutes sans préparation, anglais, et un entretien de 25 minutes. Moins de 4/20 en anglais ou à l'entretien est éliminatoire.",
   "orauxSrc": [S_CMT_ORAUX],
   "pourqui": "une suite naturelle si tu passes Mines-Ponts : aucun écrit en plus.",
   "mots": "Écrits des Mines, oraux courts"},
  "blocs": [{
   "ecrits": {"quand": "27-30 avril 2026", "l": ECRITS_MINES,
    "note": "Les mêmes copies que Mines-Ponts, avec les mêmes coefficients."},
   "adm": {"quand": "le 4 juin en 2026", "txt": "Une barre plus basse que celle de Mines-Ponts."},
   "oraux": {"quand": "23 juin - 10 juillet 2026", "l": [
     ["Mathématiques", "30 min", "8", "sans préparation"], ["Physique", "30 min", "8", "sans préparation"],
     ["Anglais", "20 min", "7"], ["Entretien", "25 min", "7"]],
    "note": "Pas de TIPE. Admissible aussi à Mines-Ponts : tu passes seulement les oraux Mines-Ponts, et tes notes sont reprises."},
   "classement": "Écrits (30) + oraux (30).",
   "notice": N_CMT, "src": [S_CMT_ORAUX, S_CMT_LE]}]},

 "cs": {
  "insc": ["0 à 140 €", "par école cochée, gratuit si boursier (15 € pour EPF et ESTP)"], "inscCourt": "0 à 140 € par école",
  "ecritsCourt": "Propres au concours",
  "poids": 50, "poidsFait": "du classement final vient des oraux", "poidsCourt": "50 %",
  "style": {
   "sujets": "Des sujets longs, où le soin compte plus que la vitesse : dans son rapport 2025 de maths 1 (filière PC), le jury écrit que « le soin apporté à la qualité des réponses est un facteur plus décisif » que le nombre de questions traitées, et qu'un enchaînement de calculs ne suffit pas comme réponse.",
   "sujetsSrc": [R_CCS],
   "oraux": "Moitié écrit, moitié oral. Deux oraux se passent avec Python, et un TP de physique-chimie dure 3 heures.",
   "orauxSrc": [S_CCS_ORAUX],
   "pourqui": "pour les candidats efficaces en calcul, à l'aise avec Python et en travaux pratiques.",
   "mots": "Sujets longs, Python et TP"},
  "blocs": [{
   "ecrits": {"quand": "4-7 mai 2026", "l": [
     ["Mathématiques 1", "4 h", "19"], ["Mathématiques 2", "4 h", "19"], ["Physique-chimie 1", "4 h", "12"],
     ["Physique-chimie 2", "4 h", "12"], ["Informatique ou sciences de l'ingénieur", "4 h", "10"],
     ["Rédaction (français)", "4 h", "17"], ["Langue vivante", "4 h", "11"]]},
   "adm": {"quand": "début juin en 2026", "txt": "Les « grands admissibles », très bien classés à l'écrit, sont dispensés d'oraux."},
   "oraux": {"quand": "22 juin - 19 juillet 2026", "l": [
     ["Mathématiques", "30 min", "19"], ["Mathématiques et informatique (Python)", "30 min", "19", "après 30 min de préparation"],
     ["Physique-chimie", "30 min", "13"], ["Physique-chimie et informatique", "30 min", "13", "après 30 min de préparation"],
     ["TP de physique-chimie", "3 h", "12"], ["TIPE", "30 min", "11"],
     ["Langue vivante", "20 min", "13", "après 20 min de préparation"]],
    "note": "Coefficients des écoles Centrale, de SupOptique et d'AgroParisTech. Arts et Métiers et les autres écoles du concours ont leurs propres oraux."},
   "classement": "Écrits (100) + oraux (100). Chaque école fait son propre classement.",
   "notice": N_CCS, "src": [S_CCS_LE, S_CCS_ORAUX, S_COEF_MP]}]},

 "inp": {
  "insc": ["240 €", "de dossier, gratuit si boursier ; + 0 à 105 € pour l'INSA ou la banque"], "inscCourt": "240 € + 0 à 105 €",
  "ecritsCourt": "Propres au concours",
  "poids": 41, "poidsFait": "du classement final vient des oraux", "poidsCourt": "41 %",
  "style": {
   "sujets": "Des sujets clairs, faits d'un ou deux exercices et d'un problème qui parcourent le programme. Le jury veut « récompenser les candidats qui auront travaillé leur cours », et exige qu'on précise les hypothèses des théorèmes.",
   "sujetsSrc": [R_CCINP],
   "oraux": "Les oraux comptent 40 sur 98 : maths (14) et physique-chimie (12) d'abord. Grand admissible, tu en es dispensé.",
   "orauxSrc": [N_CCINP],
   "pourqui": "pour les candidats réguliers et rigoureux, qui connaissent bien leur cours.",
   "mots": "Proche du cours"},
  "blocs": [{
   "ecrits": {"quand": "20-23 avril 2026", "l": [
     ["Mathématiques 1", "4 h", "12"], ["Mathématiques 2", "4 h", "12"], ["Physique", "4 h", "7"],
     ["Physique-chimie", "4 h", "7"], ["Informatique ou sciences de l'ingénieur", "4 h", "7"],
     ["Français-philosophie", "4 h", "9"], ["Langue vivante A", "3 h", "4"],
     ["Langue vivante B (facultative)", "1 h", "2", "seuls les points au-dessus de 10 comptent"]]},
   "adm": {"quand": "le 3 juin en 2026", "txt": "La barre est fixée par le jury. Les « grands admissibles » sont dispensés d'oraux, pour les écoles du concours commun seulement."},
   "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [
     ["Mathématiques", "30 min", "14", "après 30 min de préparation"],
     ["Physique-chimie", "30 min", "12", "après 30 min de préparation"],
     ["Langue vivante A", "30 min", "6", "après 30 min de préparation"], ["TIPE", "30 min", "8"]],
    "note": "Groupe INSA : dossier, écrits du CCINP et entretien. Écoles de la banque : écrits du CCINP, puis leurs propres oraux."},
   "classement": "Écrits (58, sans la langue B) + oraux (40) : 98 de coefficients.",
   "notice": N_CCINP, "src": [S_CCINP26]}]},

 "poly": {
  "insc": ["370 €", "dossier CCINP compris, gratuit si boursier"], "inscCourt": "370 €",
  "ecritsCourt": "Maths et physique propres, le reste avec le CCINP",
  "poids": 20, "poidsFait": "du classement final vient du TIPE, le seul oral", "poidsCourt": "20 % (TIPE seul)",
  "style": {
   "sujets": "Les maths et la physique-chimie sont des sujets propres à e3a-Polytech, sans calculatrice ; en maths, trois à cinq exercices indépendants. Le jury attend une justification qui utilise « à bon escient le cours », et préfère qu'on admette clairement un résultat pour avancer.",
   "sujetsSrc": [N_E3A, R_E3A],
   "oraux": "Un seul oral, le TIPE, qui compte 8 sur 40. Pas d'entretien de motivation.",
   "orauxSrc": [N_E3A],
   "pourqui": "pour les candidats réguliers, qui préfèrent des exercices variés à un long problème.",
   "mots": "Exercices, peu d'oral"},
  "blocs": [{
   "ecrits": {"quand": "21-24 avril 2026", "l": [
     ["Mathématiques (e3a-Polytech)", "4 h", "9", "sans calculatrice"],
     ["Physique-chimie (e3a-Polytech)", "4 h", "9", "sans calculatrice"],
     ["Français-philosophie", "4 h", "5", "même copie que le CCINP"],
     ["Langue vivante A", "3 h", "5", "même copie que le CCINP"],
     ["Informatique ou sciences de l'ingénieur", "4 h", "4", "même copie que le CCINP"],
     ["Langue vivante B (facultative)", "1 h", "2", "seuls les points au-dessus de 10 comptent"]]},
   "adm": {"quand": "le 3 juin en 2026", "txt": "La barre est fixée par le jury. Les « grands admissibles » sont dispensés du TIPE."},
   "oraux": {"quand": "22 juin - 18 juillet 2026", "l": [["TIPE", "30 min", "8"]]},
   "classement": "Écrits (32, sans la langue B) + TIPE (8). Les MP sont ensuite classés avec les PC et les PSI sur une liste commune.",
   "notice": N_E3A}]},

 "e3a": {
  "insc": ["240 €", "de dossier CCINP, gratuit si boursier ; + 0 à 65 € selon le concours"], "inscCourt": "240 € + 0 à 65 €",
  "ecritsCourt": "Ceux de Polytech",
  "poids": None, "poidsFait": "", "poidsCourt": "Selon l'école",
  "style": {
   "sujets": "Les mêmes sujets que Polytech : maths et physique-chimie propres à e3a-Polytech, le reste en commun avec le CCINP.",
   "sujetsSrc": [N_E3A],
   "oraux": "Surtout des entretiens, propres à chaque école.",
   "orauxSrc": [N_E3A],
   "pourqui": "pour viser des écoles souvent privées ou spécialisées, où ton projet compte à l'entretien.",
   "mots": "Écrits de Polytech, entretiens"},
  "blocs": [{
   "ecrits": {"quand": "21-24 avril 2026", "l": [
     ["Mathématiques (e3a-Polytech)", "4 h", ""], ["Physique-chimie (e3a-Polytech)", "4 h", ""],
     ["Français-philosophie", "4 h", ""], ["Langue vivante A", "3 h", ""],
     ["Informatique ou sciences de l'ingénieur", "4 h", ""], ["Langue vivante B (facultative)", "1 h", ""]],
    "note": "Coefficients en maths, physique-chimie, informatique ou SI, français et langue A : Avenir Prépas 6, 4, 4, 3, 3 ; Ingéni'Up 6, 6, 2, 3, 2. Chaque école indépendante a les siens."},
   "adm": {"quand": "le 3 juin en 2026", "txt": "Avenir Prépas, Ingéni'Up et chaque école indépendante ont leur propre jury."},
   "oraux": {"quand": "mi-juin - mi-juillet 2026", "l": [],
    "note": "Avenir Prépas : un entretien dans les écoles (coefficient 9). Ingéni'Up : entretiens dans les écoles. Écoles indépendantes : un oral ou un entretien, de coefficient 10 à 28 selon l'école ; l'EIDD et Paoli Tech n'en ont pas."},
   "notice": N_E3A}]},

 "autres": {
  "insc": ["100 €", "EPITA ou CESI ; UT : non trouvé"], "inscCourt": "100 € ; UT : non trouvé",
  "ecritsCourt": "Propres à chaque concours",
  "poids": None, "poidsFait": "", "poidsCourt": "Selon le concours",
  "style": {"mots": "Épreuves propres"},
  "blocs": [
   {"titre": "Concours EPITA-IPSA-ESME",
    "ecrits": {"quand": "avril 2026", "l": [["Mathématiques", "3 h", "6"], ["Anglais", "2 h 30", "3"],
                                         ["Option au choix", "2 h", "5", "en MP, des maths complémentaires sont possibles"]]},
    "oraux": {"quand": "4-14 juin 2026", "l": [["Entretien, en français et en anglais", "30 min", "7"],
                                              ["Oral d'innovation, en groupe", "3 h 30", "6"]]},
    "notice": S_EP26},
   {"titre": "Concours CESI",
    "ecrits": {"quand": "8-9 avril 2026", "l": [["Mathématiques", "", ""], ["Physique", "", ""], ["Anglais", "", ""], ["Français", "", ""]]},
    "oraux": {"quand": "", "l": [["Entretien", "", ""]]},
    "notice": S_CESI26},
   {"titre": "Groupe UT (UTC, UTT, UTBM)",
    "txt": "Sur dossier, puis entretien, en dehors du SCEI : calendrier et démarches à part.",
    "notice": S_UT}]},
}

# Rangs que l'on peut saisir pour le repère (concours à liste unique ; Centrale : listes par école, de taille proche)
REPERE = {"mp": {"cids": ["ccmp"]}, "mt": {"cids": ["cmt"]}, "cs": {"cids": ["ccs"], "approx": True}, "inp": {"cids": ["ccinp"]}}
