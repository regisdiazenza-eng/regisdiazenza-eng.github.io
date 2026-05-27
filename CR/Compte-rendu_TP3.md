## Requêtes SQL:

1. Liste des fabricants : SELECT nom_fabriquant FROM fabricant;

2. Liste des services (code et nom uniquement) : SELECT code_service, nom_service FROM service;

3. Liste des médicaments avec le nom de son fabricant : SELECT nom_medic, nom_fabriquant FROM medicament natural join fabriquant;

4. Liste des médicaments fabriqués en Belgique : SELECT * FROM medicament natural join fabriquant WHERE pays='Belgique';

5 : Liste des sirops : SELECT nom_medic FROM medicament WHERE forme_pharmaceutique='sirop';

6 : Liste des médicaments contenant de la disomectite : SELECT nom_medic FROM est_compose_de NATURAL JOIN molecule WHERE nom_molecule='disomectite';

7 : Liste des fabricants utilisant du diosmectite dans leurs médicaments : SELECT nom_fabriquant FROM fabriquant natural join medicament natural join est_compose_de NATURAL JOIN molecule WHERE nom_molecule='disomectite';

8 : Liste des médicaments sortie pour le service de chirurgie (avec la quantité): SELECT nom_medic, quantite FROM mouvement_stock WHERE code_service='chir';
9 : Liste des mouvements du stock triée par date: SELECT * FROM mouvement_stock ORDER BY date_mouvement;
10 : Liste des médicaments (par ordre alphabétique) avec le nom des molécules qui les composent
ainsi que la concentration: SELECT nom_medic, nom_molecule, concentration FROM medicament NATURAL JOIN molecule NATURAL JOIN est_compose_de ORDER BY nom_medic;
11 : Nombre de services dans l'hôpital: SELECT count(*) FROM service;
12 : Prix moyen d'un médicament: SELECT AVG(prix) FROM medicament;
13 : Prix le plus cher et le moins cher d'un médicament: SELECT MAX(prix), MIN(prix) FROM medicament;
14 : Pour chaque médicament, combien en reste t il en stock: SELECT nom_medic, SUM(quantite) FROM medicament GROUP BY nom_medic;
15 : Pour chaque fabricant, quel est le prix moyen d'un médicament: SELECT nom_fabriquant, AVG(prix) FROM medicament GROUP BY nom_fabriquant;
16 : Quelle est la consommation de chaque service (sauf pour le stock général) en médicaments. (on veut voir apparaître la consommation pour chaque médicament): SELECT nom_service, nom_medic, ABS(quantite) as consommation FROM mouvement_stock NATURAL JOIN service WHERE nom_service <> 'Stock Général' GROUP BY nom_service, nom_medic? quantite;

17 : Faire la facture mensuelle de chaque service (sauf pour le stock général): SELECT nom_service, ABS(SUM(prix*quantite)) AS facture FROM medicament NATURAL JOIN mouvement_stock NATURAL JOIN service <> 'stog' GROUP BY nom_service;
18 : Liste des services ayant coûté plus de 30€: SELECT nom_service, ABS(SUM(prix*quantite)) AS facture FROM medicament NATURAL JOIN mouvement_stock NATURAL JOIN service <> 'stog' GROUP BY nom_service HAVING ABS(SUM(prix*quantite)) > 30;
19 : Quel est le service qui coûte le plus cher en médicaments: SELECT nom_service, ABS(SUM(prix*quantite)) AS facture FROM medicament NATURAL JOIN mouvement_stock NATURAL JOIN service <> 'stog' GROUP BY nom_service ORDER BY facture DESC LIMIT 1;
20 : Quel est l'état du stock à la fin de chaque mois et pour chaque médicament: SELECT DATE_TRUNC('month', date_mouvement) AS mois, nom_medic, SUM(quantite) AS stock FROM mouvement_stock GROUP BY mois, nom_medic ORDER BY mois;
21 : Liste des médicaments dont le prix est inférieur au prix moyen d'un médicament: SELECT nom_medic, prix FROM medicament WHERE prix < (SELECT AVG(prix) FROM medicament);
22 : Liste des molécules utilisés par chaque service (sauf pour le stock général): SELECT nom_service, nom_molecule FROM service NATURAL JOIN mouvement_stock NATURAL JOIN medicament;