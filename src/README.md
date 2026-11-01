# Sources de l'outil « Écoles d'ingé »

La page publiée est `index.html` à la racine du dépôt (GitHub Pages : https://arkaanes.github.io/ecoles-inge/). Elle est générée à partir de ce dossier.

## Reconstruire

```sh
cd src/build
python3 build_data.py data.json   # assemble et vérifie les données → data.json
python3 build_page4.py            # injecte data.json + ../geo/out/map.json dans template4.html → ecoles.html
cp ecoles.html ../../index.html   # page publiée
```

`build_data.py` affiche une ligne `OK` ou `DIFF` par contrôle (totaux de places 2026 par concours et par filière, coefficients, sommes des lignes SCEI 2025). Tout doit être `OK`, sans `Error`.

## Tester

```sh
cd src
python3 tests/all.py    # Playwright : 4 filières × 3 largeurs (390, 820, 1280), toutes les fiches ; doit finir par errors: []
python3 tests/leak.py   # mentions d'autres filières dans chaque version (relecture manuelle)
```

## Organisation

- `build/template4.html` : l'interface (HTML/CSS/JS), commutateur MP / PC / PSI / MPI.
- `build/data_common.py`, `data_concours.py`, `data_part1.py` … `data_part5.py`, `data_partA.py` : écoles, voies et stats **MP**, concours, calendrier.
- `build/data_pc.py` : données **PC** (généré par `tools/extract_pc.py`, puis corrigé à la main).
- `build/data_psi_acces.py`, `data_mpi_acces.py` : voies **PSI / MPI** (générées par `tools/build_psi_acces.py` et `tools/build_mpi_acces.py` à partir des relevés SCEI de `psi/` et `mpi/`).
- `build/data_psi_fil.py`, `data_mpi_fil.py` : familles, concours, frais et variantes propres à la PSI et à la MPI.
- `geo/` : carte des régions (`out/map.json`).

Lignes de stats : `lib, pl, int, med, moy, cl|ins, inter, iint, c25, prev`. Ordre des lignes brutes SCEI : nom | Intégrés | F% | 5/2% | Rg médian | Rg moyen | [interfilières] | Places.

## Données

- Places : notices 2026 des concours (et L'Étudiant / Onisep quand la notice n'est pas accessible).
- Stats : SCEI, session 2025 (les stats 2026 étaient encore protégées par mot de passe au 1er novembre 2026).

## Reste à faire

- Passer aux stats SCEI 2026 dès leur publication (`scei-concours.fr/stat2026/mp.html`, `pc.html`, `psi.html`, `mpi.html`).
- Notices 2027 (places, dates, coefficients), publiées vers décembre.
- ENS : coefficients MPI, postes 2026 de Rennes, de Lyon en MPI, d'Ulm en PC/PSI.
- Frais et bourses école par école (non revérifiés ; `build_data.py` liste les écoles sans frais trouvés).
- Citations de jury en MP : celle de Centrale vient du rapport PC ; CCINP et Polytech citent des rapports 2023-2024.
- Barres d'admissibilité quand elles sont publiées.
