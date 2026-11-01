# Charge les lignes SCEI PSI 2025 relevées (psi/scei_*.txt, poly_raw.txt) dans une structure commune.
import os
D = os.path.join(os.path.dirname(__file__), "..", "psi")
def _i(x):
    x = (x or "").strip()
    return int(x) if x not in ("", "n.d.") else None

def load():
    rows = []  # dict(sec, name, ins, adm, cl, int, iint, pl, med, moy, total)
    for f in ("scei_1.txt", "scei_2.txt", "scei_3.txt", "scei_4.txt"):
        for line in open(os.path.join(D, f), encoding="utf-8"):
            p = line.rstrip("\n").split(";")
            if len(p) < 10: continue
            sec, name = p[0], p[1]
            ins, adm, cl, it, ii, pl, med, moy = map(_i, p[2:10])
            rows.append(dict(sec=sec, name=name, ins=ins, adm=adm, cl=cl, int=it, iint=ii, pl=pl, med=med, moy=moy,
                             total=name.startswith("Concours ")))
    for line in open(os.path.join(D, "poly_raw.txt"), encoding="utf-8"):
        p = line.rstrip("\n").split(";")
        rows.append(dict(sec="POLY", name=p[0], ins=2663, adm=None, cl=None, int=_i(p[1]), med=_i(p[2]), moy=_i(p[3]), iint=_i(p[4]), pl=_i(p[5]), total=False))
    for f in ("scei_6.txt", "scei_7.txt"):
        for line in open(os.path.join(D, f), encoding="utf-8"):
            p = line.rstrip("\n").split(";")
            if p[0] == "S":
                _, sec, name, it, med, moy, ii, pl = p[:8]
                rows.append(dict(sec=sec, name=name, ins=None, adm=None, cl=None, int=_i(it), med=_i(med), moy=_i(moy), iint=_i(ii), pl=_i(pl), total=False))
            else:
                _, sec, name, ins, adm, cl, it, ii, pl = p[:9]
                rows.append(dict(sec=sec, name=name, ins=_i(ins), adm=_i(adm), cl=_i(cl), int=_i(it), iint=_i(ii), pl=_i(pl), med=None, moy=None, total=True))
    # classés manquants : ceux de la ligne « Concours … » qui suit, dans la même rubrique
    pending = []
    for r in rows:
        if r["total"]:
            for q in pending:
                if q["cl"] is None and q["sec"] == r["sec"]:
                    q["cl"] = r["cl"]
            pending = []
        else:
            pending.append(r)
    return rows

ROWS = load()
IDX = {}
for r in ROWS:
    IDX.setdefault((r["sec"], r["name"]), r)

SEC = {"X": "Banque ENS PARIS-SACLAY - ECOLE POLYTECHNIQUE", "CS": "Banque CENTRALE-SUPELEC", "MPo": "Concours Commun MINES-PONTS",
       "MT": "Concours Mines - Télécom", "INP": "Concours Commun INP", "BI": "Banque épreuves CCINP Inter-Filière", "B": "Banque épreuves CCINP",
       "INSA": "Groupe INSA", "POLY": "POLY", "PA": "Puissance Alpha", "AV": "Avenir Prépas", "IU": "Ingeni'Up", "AE": "Autres écoles E3A",
       "EI": "E3A - Inter-Filière", "EP": "EPITA - ESME - IPSA", "CESI": "CESI"}

def row(sec, name):
    k = (SEC.get(sec, sec), name)
    if k not in IDX:
        raise KeyError(f"ligne SCEI introuvable : {k}")
    return IDX[k]
