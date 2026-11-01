# Lignes SCEI MPI 2025 relevées (mpi/raw_*.txt)
import os
D = os.path.join(os.path.dirname(__file__), "..", "mpi")
def _i(x):
    x = (x or "").strip()
    return int(x) if x not in ("", "-", "n.d.") else None
SEC = {"X": "Banque ECOLE POLYTECHNIQUE - interENS", "CS": "Banque CENTRALE-SUPELEC", "MPo": "Concours Commun MINES-PONTS",
       "MT": "Concours Mines - Télécom", "INP": "Concours Commun INP", "BI": "Banque épreuves CCINP Inter-Filière", "B": "Banque épreuves CCINP",
       "POLY": "POLY", "INSA": "INSA", "PA": "PA", "AV": "AV", "AE": "AE", "EI": "EI", "EP": "EP"}
ROWS = []
for f in ("raw_1.txt", "raw_2.txt"):
    for line in open(os.path.join(D, f), encoding="utf-8"):
        p = line.rstrip("\n").split(";")
        if len(p) < 10: continue
        sec, name = p[0], p[1]
        ins, adm, cl, it, ii, pl, med, moy = map(_i, p[2:10])
        total = name.startswith("Concours ")
        if total and it is None and ii is not None:      # total : intégrés rangés par erreur dans « interfilières »
            it, ii = ii, None
        if not total and adm is None and cl is None and it is None and ins is not None:   # ligne d'école : intégrés rangés dans « inscrits »
            it, ins = ins, None
        ROWS.append(dict(sec=sec, name=name, ins=ins, adm=adm, cl=cl, int=it, iint=ii, pl=pl, med=med, moy=moy, total=total))
for f in ("raw_3.txt", "raw_4.txt"):
    for line in open(os.path.join(D, f), encoding="utf-8"):
        p = line.rstrip("\n").split(";")
        if p[0] == "S":
            _, sec, name, it, med, moy, ii, pl = p[:8]
            ROWS.append(dict(sec=sec, name=name, ins=None, adm=None, cl=None, int=_i(it), med=_i(med), moy=_i(moy), iint=_i(ii), pl=_i(pl), total=False))
        elif p[0] == "T":
            _, sec, name, ins, adm, cl, it, ii, pl = p[:9]
            ROWS.append(dict(sec=sec, name=name, ins=_i(ins), adm=_i(adm), cl=_i(cl), int=_i(it), iint=_i(ii), pl=_i(pl), med=None, moy=None, total=True))
pending = []
for r in ROWS:
    if r["total"]:
        for q in pending:
            if q["cl"] is None and q["sec"] == r["sec"]:
                q["cl"] = r["cl"]
        pending = []
    else:
        pending.append(r)
IDX = {}
for r in ROWS:
    IDX.setdefault((r["sec"], r["name"]), r)
def row(sec, name):
    k = (SEC.get(sec, sec), name)
    if k not in IDX:
        raise KeyError(f"ligne SCEI MPI introuvable : {k}")
    return IDX[k]
