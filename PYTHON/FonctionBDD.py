import sqlite3 #importaion de la librairie SQLite3
lien='bdd/bdd_biblio.db'


#--------------------Types de rquetes ----------------------------
def Lecture(req, param=None):
    """fonction executant une requete sql indiqué en parametre, ne modifie pas la base de données, retoune un tuple de donnée(s)
    :req: chaine de caractere.
    :param: contenu a inserer dans la requete a la place des '?'
    """
    connexion = sqlite3.connect(lien)
    curseur = connexion.cursor()
    try:
        curseur.execute(req, param)
        reponse = curseur.fetchall() #récupère l'information et la stock dans un tuple
        return reponse
    except:
        print("probleme dans la requete")
    finally:
        connexion.close()

def Ecriture(req, param=None):
    """fonction executant une requete sql indiqué en parametre, modifie le contenu de la base de donnée
    :req: chaine de caractere.
    :param: contenu a inserer dans la requete a la place des '?'
    """
    connexion = sqlite3.connect(lien)
    curseur = connexion.cursor() #creer un objet curseur pour executer des requetes SQL sur cette base de donnée.
    try:
        curseur.execute(req,param)
        connexion.commit()#enregistrer l'informationdans la base de donnée
    except:
        print("probleme dans la requete")
    finally:
        connexion.close()



#--------------------Requête de contrôle dans la base de données ----------------------------
def Reperer_infodoc(objet_infodoc):
    """fonction qui Recherche un isbn dans la table infos_documents, retourne la valeur de chaque champ dans un tuple
    ou NONE si non trouvé.
    :objet_infodoc: objet dont l'attribut isbn sera recherhé.
    """
    requetesql = """SELECT * FROM infos_documents WHERE isbn = ? """
    param = objet_infodoc.isbn,
    return Lecture(requetesql, param)

def isbn_checkexemp(objet_infodoc):
    """fonction qui Recherche un isbn dans la table des exemplaires et retourne la valeur de chaque champ dans un tuple
    ou NONE si non trouvé.
    :objet_exemp: objet dont l'attribut isbn sera recherhé.
    """
    requetesql = """SELECT * FROM exemplaires WHERE exemp_isbn = ? """
    param = objet_infodoc.isbn,
    return Lecture(requetesql, param)

def Reperer_exemp(objet_exemp):
    """fonction qui Recherche un codebar dans la base de donnee et retourne la valeur de chaque champ dans un tuple
    ou NONE si non trouvé.
    :objet_exemp: objet dont l'attribut codebar sera recherhé.
    """
    requetesql = """SELECT * FROM exemplaires WHERE codebar = ? """
    param = objet_exemp.codebar,
    return Lecture(requetesql, param)

def exemp_checkStatut(objet_exemp):
    """fonction qui renvoi l'etat d'emprunt du livre.
    :objet_exemp: objet dont l'attribut codebar sera recherhé.
    """
    requetesql = """SELECT statut FROM exemplaires WHERE codebar = ? """
    param = objet_exemp.codebar,
    statut = Lecture(requetesql, param)
    return statut[0] #retourne la valeur precise du champ

def Reperer_Lect(objet_Lect):
    """fonction qui Recherche un num_etudiant dans la base de donnee et retourne la valeur de chaque champ dans un tuple
    ou NONE si non trouvé.
    :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
    """
    requetesql = """SELECT * FROM lecteurs WHERE num_etudiant = ? """
    param = objet_Lect.num_etudiant,
    return Lecture(requetesql, param)

def lect_checkSuspension(objet_Lect):
    """fonction qui verifie la suspension d'un lecteur.
    :objet_Lect: objet dont l'attribut codebar sera recherhé.
    """
    requetesql = """SELECT suspension FROM lecteurs WHERE num_etudiant = ? """
    param = objet_Lect.num_etudiant,
    suspension = Lecture(requetesql, param)
    return suspension[0] #retourne la valeur precise du champ

def Lect_checkemprunt(objet_Lect):
    """fonction qui verifie la presence d'un num_etudiant dans la table relation
        :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
    """
    requetesql = """SELECT * FROM relation WHERE id_lecteur = ? """
    param = objet_Lect.num_etudiant,
    return Lecture(requetesql, param)


#-----------Enregistrement dans une base de données.---------
def Enregistrer_infodoc(objet_infodoc):
    """fonction qui ajoute une entrée dans la table info_documents (si elle n'existe pas deja) en remplissant tout les champs.
    :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
    """
    if (Reperer_infodoc(objet_infodoc) == None):#Si l'isbn n'existe pas dans sa table
            requetesql = """INSERT INTO infos_documents(isbn, titre, auteur, edition_annee, cote) VALUES(?,?,?,?,?)"""
            param = objet_infodoc.isbn, objet_infodoc.titre, objet_infodoc.auteur, objet_infodoc.edition_annee, objet_infodoc.cote,
            Ecriture(requetesql, param)
    else:
        print("L'isbn existe deja dans la base de données")

def Enregistrer_exemp(objet_exemp):
    """fonction qui ajoute une entrée dans la table exemplaires (si elle n'existe pas deja) en remplissant tout les champs,
    à condition que l'isbn soit repertorié dans la table info_documents.
    :objet_exemp: objet instancé d'un attribut pour chaque champs de sa table.
    """
    if (Reperer_exemp(objet_exemp) == None): #Si le codebar n'existe pas dans sa table
        if (Reperer_infodoc(objet_exemp.obj_infodoc) != None): #si l'isbn de l'objet infodoc associé existe dans sa table
            requetesql = """INSERT INTO exemplaires(codebar, statut, exemp_commentaire, exemp_isbn) VALUES(?,?,?,?)"""
            param = objet_exemp.codebar, objet_exemp.statut, objet_exemp.exemp_commentaire, objet_exemp.obj_infodoc.isbn,
            Ecriture(requetesql, param)
        else:
            print("isbn non trouvé")
    else:
        print("L'exemplaire existe deja dans la base de données")

def Enregistrer_Lect(objet_Lect):
    """fonction qui ajoute une entrée (si elle n'existe pas deja) dans la table exemplaires en remplissant tout les champs.
    :objet_exemp: objet instancé d'un attribut pour chaque champs de sa table.
    """
    if (Reperer_Lect(objet_Lect) == None): #si le num_etudiant n'existe pas dans sa table
        requetesql = """INSERT INTO lecteurs(num_etudiant, nom, prenom, date_naissance, niveau_etude, num_tel, suspension, commentaire) VALUES(?,?,?,?,?,?,?,?)"""
        param = objet_Lect.num_etudiant, objet_Lect.nom, objet_Lect.prenom, objet_Lect.date_naissance, objet_Lect.niveau_etude, objet_Lect.num_tel, objet_Lect.suspension, objet_Lect.commentaire,
        Ecriture(requetesql, param)
    else:
        print("Lecteur déjà inscrit")



    print

#-----------Supprimer un enregistrement dans une base de données.---------
def Supprimer_isbn(objet_infodoc):
    """fonction qui supprime une entrée (si elle existe) de la table info_documents a condition l'isbn ne soit associé a aucun exemplaire.
    :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
    """
    if (Reperer_infodoc(objet_infodoc) != None): #si l'isbn existe dans sa table
        if (isbn_checkexemp(objet_infodoc) == None): #si l'isbn n'existe pas dans la table exemplaires
            requetesql = """DELETE FROM infos_documents WHERE isbn = ?"""
            param = objet_infodoc.isbn,
            Ecriture(requetesql, param)
        else:
            print("isbn associé à un ou plusieurs ouvrage(s)")
    else:
        print("isbn inexistant")

def Supprimer_exemp(objet_exemp):
    """fonction qui supprime une entrée (si elle existe) de la table exemplaires a condition que ce dernier ne soit pas emprunté.
    :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
    """
    if (Reperer_exemp(objet_exemp) != None): #si le codebar existe dans sa table
        if (exemp_checkStatut(objet_exemp) == False): #si l'exemplaire n'est pas emprunté
            requetesql = """DELETE FROM exemplaires WHERE codebar = ?"""
            param = objet_exemp.codebar,
            Ecriture(requetesql, param)
        else:
            print("exemplaire non rendu")
    else:
        print("exemplaire inexistant")

def Supprimer_lect(objet_Lect):
    """fonction qui supprime une entrée (si elle existe) de la table lecteurs a condition que ce dernier n'ait pas d'emprunt.
    :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
    """
    if (Reperer_Lect(objet_Lect) != None): #si le lecteur existe dans sa table
        if (Lect_checkemprunt(objet_Lect) == None): #si le lecteur n'a pas d'emprunt(s) en cours
            requetesql = """DELETE FROM lecteurs WHERE num_etudiant = ?"""
            param = objet_Lect.num_etudiant,
            Ecriture(requetesql, param)
        else:
            print("un ou plusieurs exemplaire(s) non rendu(s)")
    else:
        print("Lecteur inexistant")


#Rechercher_lecteur()
#Rechercher_document()
#Modifier_lecteur()
#Modifier_document()
#integrer_isbn
