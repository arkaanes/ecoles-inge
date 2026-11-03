# Sources de l'outil « Écoles d'ingé »

Le site publié est `index.html` + `site/` à la racine du dépôt (GitHub Pages : https://arkaanes.github.io/ecoles-inge/). Ils sont générés à partir de ce dossier.

## Reconstruire

```sh
cd src/build
python3 build_data.py data.json   # assemble et vérifie les données → data.json
cd ..
python3 proto/build.py            # site principal (index.html + site/) et prototypes (prototype/, b/, mix/, v2/)
```

`build_data.py` affiche une ligne `OK` ou `DIFF` par contrôle (totaux de places 2026 par concours et par filière, coefficients, sommes des lignes SCEI 2025). Tout doit être `OK`, sans `Error`.

## Tester

```sh
cd src
python3 tests/v2.py site   # site principal : toutes les pages, clair et sombre, téléphone et PC, calculs de l'inscription, export .ics ; doit finir par « pages en défaut : 0 », « contrôles en échec : [] », « errors: [] »
python3 tests/v2.py        # prototype v2, dans les 3 habillages
python3 tests/proto.py     # prototypes de vote (neutre, b, mix)
```

## Organisation

- **Site principal** (https://arkaanes.github.io/ecoles-inge/) : `index.html` + `site/` (`app.js`, `base.css`, `v2.css`, `theme.css`, `data.json`, `map.json`), produits par `src/proto/build.py`. Même interface que le prototype v2, avec l'habillage « actuel » (`src/labo/theme-actuel.css` : crème, terre cuite, Fraunces + Source Sans 3, une couleur par concours, mode sombre).
- `src/labo/` : l'interface (`app.js` : données, routeur, transitions, toutes les pages ; `app.css` : styles des pages v2 ; `index.html` : gabarit ; `theme-actuel.css`).
- `src/proto/` : interface des prototypes de vote (`app.js`, `app.css` = styles de base, `theme-b.css`, `theme-mix.css`) et `build.py`.
- `src/build/data_common.py`, `data_concours.py`, `data_part1.py` … `data_part5.py`, `data_partA.py` : écoles, voies et stats **MP**, concours, calendrier.
- `src/build/data_pc.py` : données **PC** (généré par `tools/extract_pc.py`, puis corrigé à la main).
- `src/build/data_psi_acces.py`, `data_mpi_acces.py` : voies **PSI / MPI** (générées par `tools/build_psi_acces.py` et `tools/build_mpi_acces.py` à partir des relevés SCEI de `psi/` et `mpi/`).
- `src/build/data_psi_fil.py`, `data_mpi_fil.py` : familles, concours, frais et variantes propres à la PSI et à la MPI.
- `src/geo/` : carte des régions (`out/map.json`).
- `src/ancien/` : l'ancien site en une page (`template4.html`, `build_page4.py`) et ses tests, archivés.

Lignes de stats : `lib, pl, int, med, moy, cl|ins, inter, iint, c25, prev`. Ordre des lignes brutes SCEI : nom | Intégrés | F% | 5/2% | Rg médian | Rg moyen | [interfilières] | Places.

## Données

- Places : notices 2026 des concours (et L'Étudiant / Onisep quand la notice n'est pas accessible).
- Stats : SCEI, session 2025 (les stats 2026 étaient encore protégées par mot de passe au 1er novembre 2026).

## Reste à faire

- Dates 2027 encore manquantes : Centrale-Supélec, e3a-Polytech, propositions d'intégration (tableau `CAL` de `src/labo/app.js`) ; remplacer les sources secondaires (X-ENS, CCINP) par les sites officiels.
- Passer aux stats SCEI 2026 dès leur publication (`scei-concours.fr/stat2026/mp.html`, `pc.html`, `psi.html`, `mpi.html`).
- Notices 2027 (places, dates, coefficients), publiées vers décembre.
- ENS : coefficients MPI, postes 2026 de Rennes, de Lyon en MPI, d'Ulm en PC/PSI.
- Frais et bourses école par école (non revérifiés ; `build_data.py` liste les écoles sans frais trouvés).
- Citations de jury en MP : celle de Centrale vient du rapport PC ; CCINP et Polytech citent des rapports 2023-2024.
- Barres d'admissibilité quand elles sont publiées.
