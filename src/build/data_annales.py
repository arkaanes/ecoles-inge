# Sujets et rapports du jury, épreuve par épreuve.
# Tous les liens viennent des pages officielles des concours (relevé du 3 novembre 2026) :
#   X : https://www.polytechnique.edu/admission-cycle-ingenieur/sujets-et-rapports
#   ENS : https://www.ens.psl.eu/une-formation-d-exception/admission-concours/concours-voie-cpge/concours-voie-cpge-sciences-0
#   X-ENS PSI : https://ens-paris-saclay.fr/admission/concours/concours-pre-master/annales-concours-pre-master
#   Mines-Ponts : https://concoursminesponts.fr/annales/ et https://concoursminesponts.fr/archives/
#   Centrale-Supélec : https://www.concours-centrale-supelec.fr/sujets-rapports
#   CCINP : https://www.concours-commun-inp.fr/fr/epreuves/annales/annales-<filière>.html
#   e3a-Polytech : https://www.e3a-polytech.fr/annales-et-rapport/
# Chaque entrée : [libellé, année, url]. Les clés « e » (écrits) et « o » (oraux) reprennent
# exactement les noms des lignes d'épreuves ; build_data.py vérifie la correspondance.

X = "https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/"
ENS = "https://www.ens.psl.eu/sites/default/files/"
BE = "https://banques-ecoles.fr/cms/wp-content/uploads/2025/11/"
SA = "https://ens-paris-saclay.fr/sites/default/files/CONCOURS/ANNALES_1C/1C_PSI/"
M = "https://concoursminesponts.fr/wp-content/uploads/"
C = "https://www.concours-centrale-supelec.fr/sites/default/files/documents/"
I = "https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2026/"
IO = "https://www.concours-commun-inp.fr/_resource/annales%20oraux/"
E = "https://www.e3a-polytech.fr/wp-content/uploads/2026/"


def S(u, t="Sujet", y=2026):
    return [t, y, u]


def R(u, t="Rapport", y=2026):
    return [t, y, u]


P_X = ["Sujets et rapports de l'X", "https://www.polytechnique.edu/admission-cycle-ingenieur/sujets-et-rapports"]
P_ENS = ["Sujets et rapports des ENS", "https://www.ens.psl.eu/une-formation-d-exception/admission-concours/concours-voie-cpge/concours-voie-cpge-sciences-0"]
P_SA = ["Annales X-ENS PSI (ENS Paris-Saclay)", "https://ens-paris-saclay.fr/admission/concours/concours-pre-master/annales-concours-pre-master"]
P_M = ["Annales Mines-Ponts", "https://concoursminesponts.fr/annales/"]
P_C = ["Sujets et rapports Centrale-Supélec", "https://www.concours-centrale-supelec.fr/sujets-rapports"]
P_E = ["Annales e3a-Polytech", "https://www.e3a-polytech.fr/annales-et-rapport/"]


def P_I(fil):
    return ["Annales CCINP " + fil, "https://www.concours-commun-inp.fr/fr/epreuves/annales/annales-" + fil.lower() + ".html"]


# ---------- X (rapports d'écrit et d'oral 2026 publiés) ----------
X_FR = [S(X + "Fran%C3%A7ais.pdf"), R(X + "All%20Filieres_Fran%C3%A7ais%20OK.pdf")]
X_LV = [S(X + "LVE%20Anglais.pdf", "Sujet d'anglais"), R(X + "All%20filieres_Anglais%20OK.pdf", "Rapport d'anglais")]
X_O_FR = [R(X + "All%20Fili%C3%A8res_Fran%C3%A7ais%20OK.pdf")]
X_O_LV = [R(X + "All%20Fili%C3%A8res_Anglais%20OK.pdf", "Rapport d'anglais")]
X_MA = [S(X + "Maths%20A_0.pdf"), R(X + "MP%2C%20MPI_Maths%20A%20OK.pdf")]
X_MB = [S(X + "Maths%20B.pdf"), R(X + "MP%2C%20MPI_Maths%20B%20OK.pdf")]
X_IA = [S(X + "Info%20A_1.pdf"), R(X + "MP%2C%20MPI_Info%20A_1.pdf")]
X_IC = [S(X + "Info%20C.pdf"), R(X + "MPI_Info%20C%20OK.pdf")]
X_PHMP = [S(X + "Physique%20MP_0.pdf"), R(X + "MP_Physique%20OK%20.pdf")]
X_PC_E = {
    "Mathématiques": [S(X + "Maths%20PC.pdf"), R(X + "PC_Maths%20OK.pdf")],
    "Physique A": [S(X + "Physique%20A.pdf"), R(X + "PC_Physique%20A%20OK.pdf")],
    "Physique B": [S(X + "Physique%20B.pdf"), R(X + "PC_Physique%20B%20OK.pdf")],
    "Chimie": [S(X + "Chimie%20A.pdf"), R(X + "PC_Chimie%20A%20OK.pdf")],
    "Informatique B": [S(X + "Info%20B.pdf")],
    "Français": X_FR, "Langue vivante": X_LV,
}
X_PC_O = {
    "Mathématiques": [R(X + "PC_Maths%20OK_0.pdf")],
    "Physique": [R(X + "PC_%20PhysiqueOK.pdf")],
    "Chimie": [R(X + "PC_Chimie%20OK.pdf")],
    "Analyse de documents scientifiques": [R(X + "PC_%20ADS%20Physique%20OK_0.pdf", "Rapport physique"), R(X + "PC_%20ADS%20Chimie%20OK.pdf", "Rapport chimie")],
    "TP de physique": [R(X + "PC_TP%20physique%20OK.pdf")],
    "TP de chimie": [R(X + "PC_TP%20Chimie%20OK.pdf")],
    "Français": X_O_FR, "Langue vivante": X_O_LV,
}

# ---------- ENS (sujets 2026 ; rapports 2026 des épreuves propres aux ENS pas encore en ligne) ----------
ENS_FR = [S(ENS + "vpubliee_mp_mpi_pc_psi_francais_26.pdf"), X_FR[1]]
ENS_LV = [S(ENS + "vpubliee_mp_mpi_pc_psi_lve_anglais_26.pdf", "Sujet d'anglais"), X_LV[1]]
ENS_MC = [S(ENS + "vpubliee_mp_mpi_maths_c_ulsr_26.pdf"), R(BE + "Rapport_ECRIT_Maths_C_2025.pdf", y=2025)]

# ---------- X-ENS PSI (banque X - ENS Paris-Saclay ; rapports 2026 pas encore en ligne) ----------
SA_MATHS = [S(SA + "2026/2026_PSI_Maths_XUSR.pdf"), R(SA + "2025/Rapports/2025_PSI_RAPPORT_MATHS_Ecrit.pdf", y=2025)]
SA_MOD = [S(SA + "2026/2026_PSI_Mod%C3%A9lisation_XUSR.pdf")]
SA_FR = [S(SA + "2026/2026_PSI_Fran%C3%A7ais_XUSR.pdf")]
SA_LV = [S(SA + "2026/2026_PSI_Anglais_XUSR.pdf", "Sujet d'anglais")]

# ---------- Mines-Ponts / Mines-Télécom (mêmes écrits ; un rapport d'écrit commun) ----------
M_DOCS_MP = [R(M + "2026/09/Rapport-Final-Ecrit-2026-VF.pdf", "Rapport des écrits"), R(M + "2026/10/Rapport-Final-Oral-2026-002.pdf", "Rapport des oraux")]
M_DOCS_MT = [R(M + "2026/09/Rapport-Final-Ecrit-2026-VF.pdf", "Rapport des écrits")]
M_COM = {
    "Informatique (commune)": [S(M + "2026/05/Info-Commune.zip")],
    "Français": [S(M + "2026/04/Francais.pdf")],
    "Langue vivante": [S(M + "2026/04/Langues.pdf")],
}


def mines(f, extra):
    d = {
        "Mathématiques I": [S(M + "2026/04/Maths-" + f + "-1.pdf")],
        "Mathématiques II": [S(M + "2026/04/Maths-" + f + "-2.pdf")],
        "Physique I": [S(M + "2026/05/Physique_" + f + "_1_2026.pdf")],
        "Physique II": [S(M + "2026/05/Physique_" + f + "_2_2026.pdf")],
    }
    d.update(M_COM)
    d.update(extra)
    return d


M_E = {
    "MP": mines("MP", {"Chimie": [S(M + "2026/04/Chimie-MP.pdf")],
                       "Informatique ou sciences de l'ingénieur (option)": [S(M + "2026/04/Info-option-MP.pdf", "Sujet info"), S(M + "2026/05/MP.zip", "Sujet SI")]}),
    "PC": mines("PC", {"Chimie": [S(M + "2026/04/Chimie-PC.pdf")]}),
    "PSI": mines("PSI", {"Chimie": [S(M + "2026/04/Chimie-PSI.pdf")], "Sciences industrielles": [S(M + "2026/05/PSI.zip")]}),
    "MPI": mines("MPI", {"Informatique I": [S(M + "2026/04/MPI_Info_1.pdf")], "Informatique II": [S(M + "2026/04/MPI-Info-2.pdf")]}),
}
del M_E["MPI"]["Informatique (commune)"]

# ---------- Centrale-Supélec (sujets 2026 ; dernier rapport publié : 2025, un par filière) ----------
C_RED = [S(C + "R131_1.pdf")]
C_LV = [S(C + "G079-LV009.pdf")]
C_E = {
    "MP": {"Mathématiques 1": [S(C + "M098.pdf")], "Mathématiques 2": [S(C + "M104.pdf")],
           "Physique-chimie 1": [S(C + "P086.pdf")], "Physique-chimie 2": [S(C + "P097.pdf")],
           "Informatique ou sciences de l'ingénieur": [S(C + "I021.pdf", "Sujet info"), S(C + "S028.pdf", "Sujet SI")],
           "Rédaction (français)": C_RED, "Langue vivante": C_LV},
    "MPI": {"Mathématiques 1": [S(C + "M098.pdf")], "Mathématiques 2": [S(C + "M104.pdf")],
            "Physique-chimie 1": [S(C + "P081.pdf")], "Physique-chimie 2": [S(C + "P093.pdf")],
            "Informatique": [S(C + "I022.pdf")], "Rédaction (français)": C_RED, "Langue vivante": C_LV},
    "PC": {"Mathématiques 1": [S(C + "M077.pdf")], "Mathématiques 2": [S(C + "M089_0.pdf")],
           "Physique 1": [S(C + "P092_0.pdf")], "Physique 2": [S(C + "P075.pdf")], "Chimie": [S(C + "X011_1.pdf")],
           "Rédaction (français)": C_RED, "Langue vivante": C_LV},
    "PSI": {"Mathématiques 1": [S(C + "M103.pdf")], "Mathématiques 2": [S(C + "M096.pdf")],
            "Physique-chimie 1": [S(C + "P104.pdf")], "Physique-chimie 2": [S(C + "P101.pdf")],
            "Sciences industrielles (S2I)": [S(C + "S027.pdf")], "Rédaction (français)": C_RED, "Langue vivante": C_LV},
}
C_DOCS = {
    "MP": [R(C + "Rapports_Jury_2025_MP.pdf", "Rapport du jury", 2025)],
    "MPI": [R(C + "Rapports_Jury_2025_MPI.pdf", "Rapport du jury", 2025)],
    "PC": [R(C + "Rapports_Jury_2025_PC_1.pdf", "Rapport du jury", 2025)],
    "PSI": [R(C + "Rapports_Jury_2025_PSI.pdf", "Rapport du jury", 2025)],
}

# ---------- CCINP (sujets et rapports 2026, épreuve par épreuve) ----------
I_FP = [S(I + "Ep%20communes/2026_FP4.pdf"), R(I + "Ep%20communes/Rapport%20FP%202026.pdf")]
I_LVA = [S(I + "Ep%20communes/2026_LVA6AN.pdf", "Sujet d'anglais"), R(I + "Ep%20communes/LV_ECRIT_2026_05.10.pdf")]
I_LVB = [S(I + "Ep%20communes/2026_LVB6AE.pdf", "Sujet anglais-espagnol")]
I_O_LV = [R(I + "Ep%20communes/LV_ORAL_2026_05.10.pdf")]
I_COM = {"Français-philosophie": I_FP, "Langue vivante A": I_LVA, "Langue vivante B (facultative)": I_LVB}
I_MP_OPT = [S(I + "MP/2026_MP7IN.pdf", "Sujet info"), R(I + "MP/MP_ECRIT_Informatique%202026_30.09.pdf", "Rapport info"),
            S(I + "MP/2026_MP7SI_SUJET.pdf", "Sujet SI"), S(I + "MP/2026_MP7SI_DR.pdf", "Document réponse SI"),
            R(I + "MP/MP_ECRIT_SI_2026_01.10.pdf", "Rapport SI")]
I_MPI_INFO = [S(I + "MPI/2026_MPI5IN.pdf"), R(I + "MPI/MPI_ECRIT_Informatique_2026_FINAL.pdf")]
I_PC_MOD = [S(I + "PC/2026_PC7MO.pdf"), R(I + "PC/CCINP_PC_RAPPORT_MODELISATION_2026.pdf")]
I_PC_INFO = [S(I + "PC/2026_PC5IN_SUJET.pdf"), S(I + "PC/2026_PC5IN_DR.pdf", "Document réponse"), R(I + "PC/CCINP_PC_RAPPORT_INFORMATIQUE_2026.pdf")]
I_PSI_SI = [S(I + "PSI/2026_PSI7SI_SUJET.pdf"), S(I + "PSI/2026_PSI7SI_DR.pdf", "Document réponse"), R(I + "PSI/Rapport%20SI%20PSI%202026.pdf")]
I_PSI_INFO = [S(I + "PSI/2026_PSI5IN_SUJET.pdf"), S(I + "PSI/2026_PSI5IN_DR.pdf", "Document réponse"), R(I + "PSI/Rapport%20Informatique%20PSI%202026.pdf")]
I_O_MP_MATHS = [R(IO + "MP/2026/MP%20MPI%20_%20ORAL_Maths_2026_06.10.pdf")]
I_O_MP_PC = [R(IO + "MP/2026/MP_MPI_ORAL_Physique%20Chimie_2026_29.09.pdf")]
I_E = {
    "MP": dict(I_COM, **{
        "Mathématiques 1": [S(I + "MP/2026_MP1M1.pdf"), R(I + "MP/MP_ECRIT_Maths_1_2026_FINAL.pdf")],
        "Mathématiques 2": [S(I + "MP/2026_MP3M2.pdf"), R(I + "MP/MP_ECRIT_Maths_2_2026_30.07_FINAL.pdf")],
        "Physique": [S(I + "MP/2026_MP5P.pdf"), R(I + "MP/MP_ECRIT_Physique_2026_FINAL.pdf")],
        "Physique-chimie": [S(I + "MP/2026_MP2PC.pdf"), R(I + "MP/MP_ECRIT_PhysiqueChimie_2026_18.09.pdf")],
        "Informatique ou sciences de l'ingénieur": I_MP_OPT}),
    "MPI": dict(I_COM, **{
        "Mathématiques 1": [S(I + "MPI/2026_MPI1M1.pdf"), R(I + "MPI/MPI_ECRIT_Maths_1_2026_FINAL2.pdf")],
        "Mathématiques 2": [S(I + "MPI/2026_MPI3M2.pdf"), R(I + "MPI/MPI_ECRIT_Maths_2_2026_30.07_FINAL.pdf")],
        "Physique-chimie": [S(I + "MPI/2026_MPI2PC.pdf"), R(I + "MPI/MPI_ECRIT_PhysiqueChimie_2026_18.09.pdf")],
        "Informatique": I_MPI_INFO}),
    "PC": dict(I_COM, **{
        "Mathématiques": [S(I + "PC/2026_PC1M.pdf"), R(I + "PC/CCINP_PC_RAPPORT_MATHEMATIQUES_2026.pdf")],
        "Physique": [S(I + "PC/2026_PC2P.pdf"), R(I + "PC/CCINP_PC_RAPPORT_PHYSIQUE_2026.pdf")],
        "Chimie": [S(I + "PC/2026_PC3C.pdf"), R(I + "PC/2026_Rapport%20final_ECRIT_CHIMIE_PC.pdf")],
        "Modélisation de systèmes physiques ou chimiques": I_PC_MOD, "Informatique": I_PC_INFO}),
    "PSI": dict(I_COM, **{
        "Mathématiques": [S(I + "PSI/2026_PSI1M.pdf"), R(I + "PSI/Rapport%20Mathematiques%20PSI%202026.pdf")],
        "Physique-chimie": [S(I + "PSI/2026_PSI2PC.pdf"), R(I + "PSI/Rapport%20Physique-Chimie%20PSI%202026.pdf")],
        "Modélisation et ingénierie numérique": [S(I + "PSI/2026_PSI3MO.pdf"), R(I + "PSI/Rapport%20Modelisation%20PSI%202026.pdf")],
        "Sciences industrielles de l'ingénieur": I_PSI_SI, "Informatique": I_PSI_INFO}),
}
I_O = {
    "MP": {"Mathématiques": I_O_MP_MATHS, "Physique-chimie": I_O_MP_PC, "Langue vivante A": I_O_LV},
    "MPI": {"Mathématiques": I_O_MP_MATHS, "Physique-chimie": I_O_MP_PC, "Langue vivante A": I_O_LV},
    "PC": {"Mathématiques": [R(IO + "PC/2026/CCINP_PC_RAPPORT_MATHEMATIQUES_ORAL_2026.pdf")],
           "Physique ou chimie": [R(IO + "PC/2026/CCINP_PC_RAPPORT_PHYSIQUE_ORAL_2026.pdf", "Rapport physique"),
                                  R(IO + "PC/2026/2026%20Rapport_Final_ORAL_CHIMIE_PC.pdf", "Rapport chimie")],
           "Langue vivante A": I_O_LV},
    "PSI": {"Langue vivante A": I_O_LV},
}

# ---------- e3a-Polytech (maths et physique-chimie propres ; le reste mutualisé avec le CCINP) ----------
def e3a(f, pc_file, pc_rap, pc_cor):
    return {
        "Mathématiques (e3a-Polytech)": [S(E + "07/BAT_IMPRIMEUR_" + f + "-Math-2026.pdf"),
                                         R(E + "07/Rapport_" + f + "_Math_2026.pdf", "Rapport et corrigé")],
        "Physique-chimie (e3a-Polytech)": [S(E + "07/" + pc_file), R(E + "07/" + pc_rap),
                                           R(E + "07/" + pc_cor, "Corrigé")],
        "Français-philosophie": I_FP, "Langue vivante A": I_LVA, "Langue vivante B (facultative)": I_LVB,
    }


E_E = {
    "MP": dict(e3a("MP", "BAT_IMPRIMEUR_MP-Phys_Chimie-2026.pdf", "rapport_MPI_Physique-Chimie_2026.pdf",
                   "CorrIge%C2%B4-MP-Physique-Chimie-2026.pdf"),
               **{"Informatique ou sciences de l'ingénieur": I_MP_OPT}),
    "MPI": dict(e3a("MPI", "BAT_IMPRIMEUR_MPI-Phys_Chimie-2026.pdf", "rapport_MPI_Physique-Chimie_2026-1.pdf",
                    "Corrige%C2%B4-MPI-Physique-Chimie-2026.pdf"),
                **{"Informatique": I_MPI_INFO}),
    "PC": dict(e3a("PC", "BAT_IMPRIMEUR_PC-Phys_Chime-2026.pdf", "rapport_PC_Physique-Chimie_2026.pdf",
                   "Corrige%C2%B4-PC-Physique-Chimie-2026.pdf"),
               **{"Modélisation de systèmes physiques ou chimiques": I_PC_MOD, "Informatique": I_PC_INFO}),
    "PSI": dict(e3a("PSI", "BAT_IMPRIMEUR_PSI-Phys_Chimie-2026.pdf", "rapport_PSI_Physique-chimie_2026.pdf",
                    "Corrige%C2%B4-PSI-Physique-Chimie-2026.pdf"),
                **{"Sciences industrielles": I_PSI_SI, "Informatique": I_PSI_INFO}),
}


def fam(pages, e, o=None, docs=None):
    return {"pages": pages, "e": e, "o": o or {}, "docs": docs or []}


ANNALES = {
    "MP": {
        "x": fam([P_X], {
            "Mathématiques A": X_MA, "Mathématiques B": X_MB, "Physique": X_PHMP, "Informatique A": X_IA,
            "Physique et sciences de l'ingénieur": [S(X + "Phys%20SI.pdf"), R(X + "MP_Phys%20%26%20SI%20OK.pdf")],
            "Informatique B": [S(X + "Info%20B.pdf"), R(X + "MP_Info%20B%20OK.pdf")],
            "Français": X_FR, "Langue vivante": X_LV,
        }, {
            "Mathématiques, 1re interrogation": [R(X + "MP_Math%C3%A9matiques%20OK.pdf")],
            "Mathématiques, 2e interrogation": [R(X + "MP_Math%C3%A9matiques%20OK.pdf")],
            "Physique": [R(X + "MP_Physique%20OK.pdf")],
            "Chimie": [R(X + "MP_Chimie%20OK.pdf")],
            "Analyse de documents scientifiques": [R(X + "MP_ADS%20Math%C3%A9matiques%20OK.pdf", "Rapport maths"),
                                                   R(X + "MP_ADS%20Physique%20OK.pdf", "Rapport physique")],
            "Français": X_O_FR, "Langue vivante": X_O_LV,
        }),
        "ens": fam([P_ENS], {
            "Physique": [S(ENS + "vpubliee_mp_physique_26.pdf"), X_PHMP[1]],
            "Mathématiques C": ENS_MC,
            "Mathématiques D": [S(ENS + "vpubliee_mp_maths_d_u_26.pdf"), R(BE + "Rapport_ECRIT_Maths_D_2025.pdf", y=2025)],
            "Français": ENS_FR, "Langue vivante": ENS_LV,
        }),
        "mp": fam([P_M], M_E["MP"], docs=M_DOCS_MP),
        "mt": fam([P_M], M_E["MP"], docs=M_DOCS_MT),
        "cs": fam([P_C], C_E["MP"], docs=C_DOCS["MP"]),
        "inp": fam([P_I("MP")], I_E["MP"], I_O["MP"]),
        "poly": fam([P_E, P_I("MP")], E_E["MP"]),
        "e3a": fam([P_E, P_I("MP")], E_E["MP"]),
    },
    "MPI": {
        "x": fam([P_X], {
            "Mathématiques A": [S(X + "Maths%20A_1.pdf"), X_MA[1]], "Mathématiques B": X_MB,
            "Informatique C": X_IC,
            "Physique": [S(X + "Physique%20MPI_0.pdf"), R(X + "MPI_Physique%20OK.pdf")],
            "Français": X_FR, "Langue vivante": X_LV,
        }, {
            "Mathématiques": [R(X + "MPI_Maths%20OK.pdf")],
            "Informatique": [R(X + "MPI_Info%20OK.pdf")],
            "Physique": [R(X + "MPI_Physique%20OK_0.pdf")],
            "Analyse de documents scientifiques (maths ou info)": [R(X + "MPI_ADS%20Maths%20OK.pdf", "Rapport maths"),
                                                                   R(X + "MPI_ADS%20info%20OK%20.pdf", "Rapport info")],
            "Français": X_O_FR, "Langue vivante": X_O_LV,
        }),
        "ens": fam([P_ENS], {
            "Mathématiques A": [S(ENS + "vpubliee_mp_mpi_maths_a_26.pdf"), X_MA[1]],
            "Mathématiques C": ENS_MC,
            "Informatique A": [S(ENS + "vpubliee_mp_mpi_info_a_26.pdf"), X_IA[1]],
            "Informatique C": [S(ENS + "vpubliee_mpi_info_c_26.pdf"), X_IC[1]],
            "Informatique fondamentale": [S(ENS + "vpubliee_mp_mpi_info_fond_ulsr_26.pdf")],
            "Français": ENS_FR, "Langue vivante": ENS_LV,
        }),
        "mp": fam([P_M], M_E["MPI"], docs=M_DOCS_MP),
        "mt": fam([P_M], M_E["MPI"], docs=M_DOCS_MT),
        "cs": fam([P_C], C_E["MPI"], docs=C_DOCS["MPI"]),
        "inp": fam([P_I("MPI")], I_E["MPI"], I_O["MPI"]),
        "poly": fam([P_E, P_I("MPI")], E_E["MPI"]),
        "e3a": fam([P_E, P_I("MPI")], E_E["MPI"]),
    },
    "PC": {
        "x": fam([P_X], X_PC_E, X_PC_O),
        "ens": fam([P_ENS], {
            "Mathématiques": [S(ENS + "vpubliee_pc_maths_26.pdf"), X_PC_E["Mathématiques"][1]],
            "Chimie A": [S(ENS + "vpubliee_pc_chimie_a_26.pdf"), X_PC_E["Chimie"][1]],
            "Physique C": [S(ENS + "vpubliee_pc_phys_c_u_26.pdf"), R(ENS + "rapport_jury_ecrit_physique_pc_2025.pdf", y=2025)],
            "Français": ENS_FR, "Langue vivante": ENS_LV,
        }),
        "mp": fam([P_M], M_E["PC"], docs=M_DOCS_MP),
        "mt": fam([P_M], M_E["PC"], docs=M_DOCS_MT),
        "cs": fam([P_C], C_E["PC"], docs=C_DOCS["PC"]),
        "inp": fam([P_I("PC")], I_E["PC"], I_O["PC"]),
        "poly": fam([P_E, P_I("PC")], E_E["PC"]),
        "e3a": fam([P_E, P_I("PC")], E_E["PC"]),
    },
    "PSI": {
        "x": fam([P_SA, P_X], {
            "Mathématiques": SA_MATHS, "Modélisation": SA_MOD,
            "Physique": [S(SA + "2026/2026_PSI_Physique_XSR.pdf"), R(SA + "2025/Rapports/2025_PSI_Rapport_Physique_XSR_Ecrit.pdf", y=2025)],
            "Sciences industrielles": [S(SA + "2026/2026_PSI_SI_XSR.pdf")],
            "Informatique": [S(SA + "2026/2026_PSI_Info_B_XSR.pdf"), R(SA + "2025/Rapports/2025_PSI_rapport_info_Ecrit.pdf", y=2025)],
            "Français": SA_FR, "Langue vivante": SA_LV,
        }, {
            "Mathématiques": [R(X + "PSI_%20Maths%20OK.pdf")],
            "Physique": [R(X + "PSI_%20physique%20OK.pdf")],
            "Analyse de documents scientifiques (physique)": [R(X + "PSI_ADS%20physique%20OK.pdf")],
            "Langue vivante": X_O_LV,
        }),
        "ens": fam([P_ENS, P_SA], {
            "Mathématiques": SA_MATHS,
            "Physique": [S(SA + "2026/2026_PSI_Physique_U.pdf"), R(SA + "2025/Rapports/2025_PSI_Rapport_Physique_ULM_Ecrit.pdf", y=2025)],
            "Modélisation en sciences physiques et SI": SA_MOD,
            "Français": SA_FR, "Langue vivante": SA_LV,
        }),
        "mp": fam([P_M], M_E["PSI"], docs=M_DOCS_MP),
        "mt": fam([P_M], M_E["PSI"], docs=M_DOCS_MT),
        "cs": fam([P_C], C_E["PSI"], docs=C_DOCS["PSI"]),
        "inp": fam([P_I("PSI")], I_E["PSI"], I_O["PSI"]),
        "poly": fam([P_E, P_I("PSI")], E_E["PSI"]),
        "e3a": fam([P_E, P_I("PSI")], E_E["PSI"]),
    },
}


def all_urls():
    seen = set()
    for fil in ANNALES.values():
        for f in fil.values():
            for p in f["pages"]:
                seen.add(p[1])
            for part in ("e", "o"):
                for l in f[part].values():
                    for it in l:
                        seen.add(it[2])
            for it in f["docs"]:
                seen.add(it[2])
    return sorted(seen)


if __name__ == "__main__":
    for u in all_urls():
        print(u)
