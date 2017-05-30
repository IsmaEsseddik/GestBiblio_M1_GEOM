import datetime  # pour les operation sur le temps
import sqlite3  # importation de la librairie SQLite3
import re  # importation du package des expression regulieres
lien = 'bdd_biblio.db'


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
        suspension DATE,
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
        prolongement BOOLEAN,
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


def maj_suspension():
    """fonction qui met a jour la date de levée de la suspension de chaque lecteurs"""
    date_du_jour = datetime.datetime.today()  # on utilisera la date du jour
    requetesql = """SELECT DISTINCT num_etudiant FROM lecteurs"""
    param = ''
    all_lect = lecture(requetesql, param)
    print(all_lect)
    for i in all_lect:
        requetesql = """SELECT suspension FROM lecteurs WHERE num_etudiant = ? """
        param = i[0],
        reponse = lecture(requetesql, param)[0][0]
        if (reponse is not None):  # formatage de la date de suspension si existante
            suspension = datetime.datetime(int(reponse[0:4]), int(reponse[5:7]), int(reponse[8:10]))
        else:
            suspension = None
        # on a recupéré la valeur de la suspension(date ou None) du lecteur i
        requetesql = """SELECT MIN(date_retour) FROM relation WHERE id_lecteur = ? AND date('now') > date_retour  """
        param = i[0],
        date_retour_min = lecture(requetesql, param)[0][0]
        # on a recupere la date de retour la plus anterieur possible a celle d'aujourd'hui
        # (ou rien si aucun livre n'est en retard)
        if (date_retour_min is not None):  # si il y a une date anterieur
            retardmax = date_du_jour - datetime.datetime(int(date_retour_min[0:4]), int(date_retour_min[5:7]),
                                                         int(date_retour_min[8:10]))
            # calcul et formattage de la date de retour
            if (retardmax > datetime.timedelta(31)):  # si le retard  est superieur a un mois
                retardmax = datetime.timedelta(31)  # on fixe le retard MAX a un mois
            date_suspension_r = date_du_jour + retardmax  # nouvelle date de suspension a remplacer
        else:
            date_suspension_r = None
            # si aucun livre est en retard la valeur a remplacer sera zero(a condition que la date de suspension initial
            # soit passée et que la nouvelle soit superieur a cette derniere)

        requetesql = """UPDATE lecteurs SET suspension = ? WHERE num_etudiant = ?"""
        param = date_suspension_r, i[0],
        if (suspension is None or suspension < date_du_jour or date_suspension_r > suspension):
            # si la date de suspension initial est passé ou nul ou inferieur a celle a remplacer
            ecriture(requetesql, param)
        elif (date_du_jour < suspension):  # si la date de suspension n'est pas encore passée...
            if(date_suspension_r > suspension or date_suspension_r is None):
                # ...ET qu'elle ne represente pas le retard le plus important
                ecriture(requetesql, param)
        else:
            pass
    # fin de la boucle
