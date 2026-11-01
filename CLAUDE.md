# Outil « Écoles d'ingé »

Outil web sur les écoles d'ingénieurs post-prépa (filières MP, PC, PSI, MPI), fait pour une promo de CPGE. Publié via GitHub Pages depuis `index.html` (branche `main`, racine).

- Sources, reconstruction, tests et liste des points ouverts : `src/README.md`.
- Ne jamais modifier `index.html` à la main : modifier `src/build/`, reconstruire, lancer les tests, puis copier `src/build/ecoles.html` vers `index.html`.
- Chaque chiffre affiché doit venir d'une source citée (notice officielle en priorité) ; ajouter un contrôle de total dans `build_data.py` quand une notice donne un total.
- Interface : pas de légendes ni de textes qui « justifient » l'interface ; l'organisation doit se comprendre d'elle-même.
- Réponses à l'utilisateur en français, courtes et directes.
