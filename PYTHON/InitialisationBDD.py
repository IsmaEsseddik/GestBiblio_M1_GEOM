# creation de tables : "lecteurs"(importu2.ensg...trombino); "documents" ;"info_documents".
# jointure entre document et infodoc via champ ISBN .
# creation d'une table de jointure "Relation" entre lecteur et documents.
# type de requete sur la base de données

import sqlite3  # importation de la librairie SQLite3
import re  # importation du package des expression regulieres
lien = 'bdd/bdd_biblio.db'


# -----------Creation d'une base de données.---------
def creation_bdd():
    """  fonction qui cree une base de donnée a l'emplacement/nom indiqué en argument si elle n'existe pas deja,
    puis formalise les tables si elle n'existent pas deja.
    :lien: chemin/fichier(.bdd) a specifier pour etablir la connexion
    """

    connexion = sqlite3.connect(lien)
    curseur = connexion.cursor()  # creer un objet curseur pour executer des requetes SQL sur cette base de donnée.
    try:
        curseur.execute("""
        CREATE TABLE IF NOT EXISTS lecteurs(
        num_etudiant VARCHAR(8) PRIMARY KEY,
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
        isbn VARCHAR PRIMARY KEY,
        titre TEXT,
        auteur TEXT,
        editeur TEXT,
        date_edition TEXT,
        cote TEXT,
        description TEXT
        );
        """)

        curseur.execute("""
        CREATE TABLE IF NOT EXISTS exemplaires(
        codebar VARCHAR PRIMARY KEY,
        emprunt BOOLEAN,
        exemp_commentaire TEXT,
        exemp_isbn VARCHAR(13),
        CONSTRAINT ce_isbn FOREIGN KEY (exemp_isbn) REFERENCES infos_documents(isbn)
        );
        """)

        curseur.execute("""
        CREATE TABLE IF NOT EXISTS relation(
        date_emprunt DATE,
        date_retour DATE,
        id_lecteur VARCHAR(8),
        id_exemplaire VARCHAR,
        CONSTRAINT ce_lect FOREIGN KEY (id_lecteur) REFERENCES lecteurs(num_etudiant),
        CONSTRAINT ce_doc FOREIGN KEY (id_exemplaire) REFERENCES exemplaires(codebar)
        );
        """)
        connexion.commit()

    except sqlite3.Error as e:
        print("probleme dans la requete")
        print(e)
    finally:
        connexion.close()


def regexp(expr, item):  # fonctionalité d'expression reguliere pour les requetes sql
    reg = re.compile(expr)
    return reg.search(item) is not None


def lecture(req, param=None):
    """  fonction executant une requete sql indiqué en parametre, ne modifie pas la base de données,
    retourne une liste de tuple de contenant les valeurs de chaque champ
    :req: chaine de caractere.
    :param: contenu a inserer dans la requete a la place des '?'
    """
    connexion = sqlite3.connect(lien)
    connexion.create_function("REGEXP", 2, regexp)  # integration de la fonction regexp dans les requetes sql.
    curseur = connexion.cursor()
    try:
        curseur.execute(req, param)
        reponse = curseur.fetchall()  # récupère l'information et la stock dans un tuple
        return reponse
    except sqlite3.Error as e:
        print("probleme dans la requete")
        print(e)
    finally:
        connexion.close()


def ecriture(req, param=None):
    """ fonction executant une requete sql indiqué en parametre, modifie le contenu de la base de donnée
    :req: chaine de caractere.
    :param: contenu a inserer dans la requete a la place des '?'
    """
    connexion = sqlite3.connect(lien)
    curseur = connexion.cursor()  # creer un objet curseur pour executer des requetes SQL sur cette base de donnée.
    try:
        curseur.execute(req, param)
        connexion.commit()  # enregistrer l'informationdans la base de donnée
    except sqlite3.Error as e:
        print("probleme dans la requete :")
        print(e)

    finally:
        connexion.close()

def Modification(req, param=None):
    """ fonction executant une requete sql indiqué en parametre, modifie le contenu de la base de donnée
    :req: chaine de caractere.
    :param: contenu a inserer dans la requete a la place des '?'
    """
    connexion = sqlite3.connect(lien)
    curseur = connexion.cursor()  # creer un objet curseur pour executer des requetes SQL sur cette base de donnée.
    try:
        curseur.execute(req, param)

    except sqlite3.Error as e:
        print("probleme dans la requete :")
        print(e)

    finally:
        connexion.close()
