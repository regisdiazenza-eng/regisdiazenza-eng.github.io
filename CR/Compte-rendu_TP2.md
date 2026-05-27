# Requêtes permettant de répondres aux questions suitavantes:

 Projection, sélection, AS

 1.1 : Liste de tous les adhérents: SELECT * FROM  adherent;
 1.2 : Nom et prénom des auteurs: SELECT nom, prenom FROM auteur;
 1.3 : Liste des adhérents habitant Arras: SELECT * FROM adherent WHERE ville='Arras';
 1.4 : Liste des références d'exemplaires de type Livre et dont le prix est inférieur à 15.00:      SELECT refexemplaire FROM exemplaire WHERE prixachat <15.00 AND typesupport='LIV';
 1.5 : Le nom des auteurs née en 1961 ou 1962: SELECT nom FROM auteur WHERE anneenaissance=1961 ou anneenaissance=1962;
 1.6 : Le titre et la description des oeuvres (résumé renommé en description):      SELECT titre, resume FROM oeuvre;

 LIKE, BETWEEN, LIMIT, ORDER BY
 2.1 : Liste des œuvres dont le nom commence par 'Le':  SELECT numoeuvre, titre FROM oeuvre WHERE titre LIKE 'Le%';
 2.2 : Liste des adhérents dont le nom de ville fini par la lettre 'n':     SELECT * FROM adherent WHERE ville LIKE '%n';
 2.3 : Liste des 10 premiers emprunts de la base:   SELECT * FROM emprunter LIMIT 10;
 2.4 : Liste des 10 emprunts suivants de la question précédente:    SELECT * FROM emprunter LIMIT 10 OFFSET 10;
 2.5 : Liste des exemplaires dont la référence est comprise entre 12 et 21:     SELECT * FROM exemplaire WHERE refexemplaire BETWEEN 12 AND 21 ;
 2.6 : Liste des exemplaires triée par ordre chronologie de date d'achat:   SELECT * FROM exemplaire ORDER BY dateachat;
 2.7 : Liste des 5 exemplaires les plus vieux !:    SELECT * FROM exemplaire ORDER BY dateachat LIMIT 5;
 2.8 : Liste des œuvres triées par date d'écriture:     SELECT * FROM oeuvre ORDER BY dateecriture;

  Calculs en ligne
 3.1 : Afficher les œuvres et le prix TTC (T.V.A. = 19,6%): SELECT titre, prixachat * 1.96 as prixttc from oeuvre, exemplaire WHERE numoeuvre=refexemplaire;
 3.2 : Afficher les auteurs et leur age :   SELECT nom, 2026 - anneenaissance AS age FROM auteur;

  Jointure interne (Père-Fils et Maillée)
 4.1 : Liste des adhérents avec les numéros des cartes qu'ils possèdent:    SELECT nom, numcarte FROM adherent NATURAL JOIN carte;
 4.2 : Liste des œuvres avec les noms et prénoms des auteurs:   SELECT titre, nom, prenom FROM auteur, oeuvre, ecrit WHERE ecrit.numauteur =  auteur.numauteur AND ecrit.numoeuvre = oeuvre.numoeuvre; OU      SELECT titre, nom, prenom FROM (auteur INNER JOIN ecrit ON auteur.numauteur = ecrit.numauteur) INNER JOIN oeuvre ON ecrit.numoeuvre = oeuvre.numoeuvre;
 4.3 : Liste des exemplaires avec le type et la description du support sur lequel il se trouve:   SELECT refexemplaire, typesupport, description FROM exemplaire NATURAL JOIN support;  
 4.4 : Liste de tous les exemplaires avec le numéro des adhérents qui les ont empruntés: SELECT numadherent, refexemplaire FROM adherent NATURAL JOIN carte NATURAL JOIN emprunter;
 4.5 : Liste de tous les responsables ainsi que les amendes qu'on leur a infligées: SELECT nom, prenom, typeamende FROM responsable NATURAL JOIN inflige NATURAL JOIN amende;
 4.6 : Liste des exemplaires empruntés par l'adhérent de numéro de carte 10:    SELECT refexemplaire FROM emprunter WHERE numcarte=10;

  Jointure interne sur plus de 2 tables
 5.1 : Liste des exemplaires avec le nom et prénom de l'adhérent qui les a empruntés:   SELECT refexemplaire, nom, prenom FROM carte NATURAL JOIN emprunter NATURAL JOIN adherent;
 5.2 : Liste des genres écrit par l'auteur numéro 6 (Victor Hugo): SELECT typegenre FROM auteur NATURAL JOIN possede NATURAL JOIN genre NATURAL JOIN genre WHERE auteur.nom='Hugo';
 5.3 : Les noms et prénoms des adhérents qui demandent une réservation (indiquer aussi le titre de l'oeuvre): SELECT nom, prenom, titre FROM proposition NATURAL JOIN adherent NATURAL JOIN oeuvre WHERE typepropose='reserve';