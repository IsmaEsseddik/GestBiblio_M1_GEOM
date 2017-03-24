#creation de tables : "lecteurs"(importu2.ensg...trombino); "documents" ;"info_documents".
#jointure entre document et infodoc via champ ISBN .
#creation d'une table de jointure "Relation" entre lecteur et documents.

import sqlite3 #importaion de la librairie SQLite3
lien='bdd/bdd_biblio.db'
#-----------Creation d'une base de données.---------
def creation_bdd():
    """fonction qui cree une base de donnée a l'emplacement/nom indiqué en argument
si elle n'existe pas deja, puis formalise les tables si elle n'existent pas deja.
    :lien: chemin/fichier(.bdd) a specifier pour etablir la connexion
    """
    connexion = sqlite3.connect(lien)
    curseur = connexion.cursor()#creer un objet curseur pour executer des requetes SQL sur cette base de donnée.
    try:
        curseur.execute("""
        CREATE TABLE IF NOT EXISTS lecteurs(
        num_etudiant INTEGER(8) PRIMARY KEY,
        nom VARCHAR(25),
        prenom VARCHAR(25),
        date_naissance DATE,
        niveau_etude VARCHAR,
        num_tel TEXT,
        suspension BOOLEAN,
        commentaire TEXT
        );
        """)


        curseur.execute("""
        CREATE TABLE IF NOT EXISTS infos_documents(
        isbn INTEGER PRIMARY KEY,
        titre TEXT,
        auteur TEXT,
        editeur TEXT,
        date_edition TEXT,
        cote TEXT
        );
        """)

        curseur.execute("""
        CREATE TABLE IF NOT EXISTS exemplaires(
        codebar INTEGER PRIMARY KEY,
        statut BOOLEAN,
        exemp_commentaire TEXT,
        exemp_isbn INTEGER(13),
        CONSTRAINT ce_isbn FOREIGN KEY (exemp_isbn) REFERENCES infos_documents(isbn)
        );
        """)

        curseur.execute("""
        CREATE TABLE IF NOT EXISTS relation(
        date_emprunt DATE,
        date_retour DATE,
        id_lecteur INTEGER(8),
        id_exemplaire INTEGER,
        CONSTRAINT ce_lect FOREIGN KEY (id_lecteur) REFERENCES lecteurs(num_etudiant),
        CONSTRAINT ce_doc FOREIGN KEY (id_exemplaire) REFERENCES exemplaires(codebar)
        );
        """)
        connexion.commit()

    except:
        print("probleme dans la requete")
    finally:
        connexion.close()


#__________________MAIN EXECUTION______________

if __name__ == '__main__':
    creation_bdd() #on lance la fonction qui creer la base de donnée
    essai_recherche() #on test une recherche
