# Installation et administration d'une base de données PostgreSQL

## 1. Installation

    sudo apt update
    sudo apt install postgresql postgresql-contrib

## Gestion du service PostgreSQL

    sudo systemctl start postgresql            # Démarrer le service
    sudo systemctl stop postgresql             # Arrêter le service
    sudo systemctl restart postgresql          # Redémarrer le service
    sudo systemctl status postgresql           # Vérifier l'état du service
    sudo systemctl enable postgresql           # Activer le démarrage automatique du service
    sudo systemctl disable postgresql          # Désactiver le démarrage automatique du service
    
    



## 2. Accès et administration

    sudo -i -u postgres                    # se connecter en tant qu'utilisateur postgres
    psql                                # lancer la commande pour se connecter à la base de données 
    \q                                  # quitter
    \l                                  # lister les bases de données
    \d nom_table                         # afficher les colonnes de la table
    \c nom_base                         # se connecter à une base de données
    \conninfo                           # information sur la connexion
    \?                                  # afficher l'aide

## Création d'une table

    CREATE TABLE nom_table (nom_colonne1 type, nom_colonne2 type, ...);
    
    CREATE TABLE produit
    (
        id_produit     INT            PRIMARY KEY,
        nom_produit    VARCHAR (255)  NOT NULL,
        ref_fournisseur    INT,
        prix_produit       NUMERIC (10, 2) NOT NULL,
        poids_unitaire     DECIMAL (10, 2) NOT NULL,
        couleur_produit    VARCHAR (255) NOT NULL
    );  

    ### Remplissage de la table

        #### Insertions
        INSERT INTO produit (id_produit, nom_produit, ref_fournisseur, prix_produit, poids_unitaire, couleur_produit) VALUES (1, 'Pomme', 1, 1.00, 0.50, 'Rouge'), (2, 'Avocat', 2, 2.00, 1.00, 'Vert');    
            

        #### Copie
        \COPY nom_table(nom_attributs, si la table n'a pas déjà été créée) FROM 'chemin_absolue_du_fichier' WITH (DELIMITER ';', FORMAT CSV, HEADER TRUE);
    

## Modification d'une table existante

    ### A)  Ajout de colonnes
        ALTER TABLE nom_table ADD COLUMN nom_colonne type;  

    ### B) Suppression de colonnes
        ALTER TABLE nom_table DROP COLUMN nom_colonne;  

    ### C) Modification de colonnes
        ALTER TABLE nom_table ALTER COLUMN nom_colonne type;  

    ### D) Modification de la clé primaire 
        ALTER TABLE nom_table DROP CONSTRAINT nom_de_la_clé(souvent nom_de_table_pkey);
        ALTER TABLE nom_table ADD PRIMARY KEY (nom_colonne);       # On définit la nouvelle clé primaire 


## Suppression d'une table

    DROP TABLE nom_table;

## Création d'un schéma

    CREATE SCHEMA nom_schema;
    