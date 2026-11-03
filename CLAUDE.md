# Outil « Écoles d'ingé »

Outil web sur les écoles d'ingénieurs post-prépa (filières MP, PC, PSI, MPI), fait pour une promo de CPGE. Publié via GitHub Pages depuis `index.html` + `site/` (branche `main`, racine). Prototypes dans `prototype/` (vote de style : `prototype/`, `b/`, `mix/` ; nouvelles fonctions : `v2/`).

- Sources, reconstruction, tests et liste des points ouverts : `src/README.md`.
- Ne jamais modifier `index.html`, `site/` ni `prototype/` à la main : modifier `src/build/` (données), `src/labo/` ou `src/proto/` (interface), lancer `python3 src/proto/build.py`, puis les tests (`src/README.md`).
- Chaque chiffre affiché doit venir d'une source citée (notice officielle en priorité) ; ajouter un contrôle de total dans `build_data.py` quand une notice donne un total.
- Interface : pas de légendes ni de textes qui « justifient » l'interface ; l'organisation doit se comprendre d'elle-même.
- Réponses à l'utilisateur en français, courtes et directes.
