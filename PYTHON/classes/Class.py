class InfoDocument:
    """Classe définissant un document caractérisée par :
    - son isbn.
    - son titre.
    - son auteur.
    - son edition(&année).
    - sa cote.
    """
    table_ref = 'infos_documents'
    clef_primaire = 'isbn'

    def __init__(self, isbn, titre, auteur, date_edition, cote): # méthode constructeur
        """Constructeur de la classe. Chaque attribut va être instancié par une valeur
        indiqué en argument."""
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.editeur = editeur
        self.date_edition = date_edition
        self.cote = cote

    def Exist_infodoc(self):
        """fonction qui Recherche un isbn dans la table infos_documents, retourne la valeur de chaque champ dans un tuple
        ou NONE si non trouvé.
        :objet_infodoc: objet dont l'attribut isbn sera recherhé.
        """
        requetesql = """SELECT * FROM infos_documents WHERE isbn = ? """
        param = self.isbn,
        return Lecture(requetesql, param)

    def Exist_isbn_exemp(self):
        """fonction qui Recherche un isbn dans la table des exemplaires et retourne la valeur de chaque champ dans un tuple
        ou NONE si non trouvé.
        :objet_exemp: objet dont l'attribut isbn sera recherhé.
        """
        requetesql = """SELECT * FROM exemplaires WHERE exemp_isbn = ? """
        param = self.isbn,
        return Lecture(requetesql, param)

    def Enregistrer_infodoc(self):
        """fonction qui ajoute une entrée dans la table info_documents (si elle n'existe pas deja) en remplissant tout les champs.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (Exist_infodoc(self) == None):#Si l'isbn n'existe pas dans sa table
                requetesql = """INSERT INTO infos_documents(isbn, titre, auteur, edition_annee, cote) VALUES(?,?,?,?,?)"""
                param = self.isbn, self.titre, self.auteur, self.edition_annee, self.cote,
                Ecriture(requetesql, param)
        else:
            print("L'isbn existe deja dans la base de données")

    def Supprimer_isbn(self):
        """fonction qui supprime une entrée (si elle existe) de la table info_documents a condition l'isbn ne soit associé a aucun exemplaire.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (Exist_infodoc(self) != None): #si l'isbn existe dans sa table
            if (Exist_isbn_exemp(self) == None): #si l'isbn n'existe pas dans la table exemplaires
                requetesql = """DELETE FROM infos_documents WHERE isbn = ?"""
                param = self.isbn,
                Ecriture(requetesql, param)
            else:
                print("isbn associé à un ou plusieurs ouvrage(s)")
        else:
            print("isbn inexistant")


class Exemplaire:
    """ classe definissant un exemplaire avec :
    - un codebar.
    - un statut.
    - un commentaire.
    - un isbn (objet de la class InfoDocument).
    """
    table_ref = 'exemplaires'
    clef_primaire = 'codebar'

    def __init__(self, codebar, statut, exemp_commentaire, obj_infodoc): # méthode constructeur
        """Constructeur de la classe. Chaque attribut va être instancié
        d'une valeur passé en argument."""
        self.codebar = codebar
        self.statut = statut
        self.exemp_commentaire = exemp_commentaire
        self.obj_infodoc = obj_infodoc #objet de la class infosDocument.

    def Exist_exemp(self):
        """fonction qui Recherche un codebar dans la base de donnee et retourne la valeur de chaque champ dans un tuple
        ou NONE si non trouvé.
        :objet_exemp: objet dont l'attribut codebar sera recherhé.
        """
        requetesql = """SELECT * FROM exemplaires WHERE codebar = ? """
        param = self.codebar,
        return Lecture(requetesql, param)

    def exemp_checkStatut(self):
        """fonction qui renvoie l'etat d'emprunt du livre.
        :objet_exemp: objet dont l'attribut codebar sera recherhé.
        """
        requetesql = """SELECT statut FROM exemplaires WHERE codebar = ? """
        param = self.codebar,
        statut = Lecture(requetesql, param)
        return statut[0] #retourne la valeur precise du champ

    def Enregistrer_exemp(self):
        """fonction qui ajoute une entrée dans la table exemplaires (si elle n'existe pas deja) en remplissant tout les champs,
        à condition que l'isbn soit repertorié dans la table info_documents.
        :objet_exemp: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (Exist_exemp(self) == None): #Si le codebar n'existe pas dans sa table
            if (Exist_infodoc(self.obj_infodoc) != None): #si l'isbn de l'objet infodoc associé existe dans sa table
                requetesql = """INSERT INTO exemplaires(codebar, statut, exemp_commentaire, exemp_isbn) VALUES(?,?,?,?)"""
                param = self.codebar, self.statut, self.exemp_commentaire, self.obj_infodoc.isbn,
                Ecriture(requetesql, param)
            else:
                print("isbn non trouvé")
        else:
            print("L'exemplaire existe deja dans la base de données")

    def Supprimer_exemp(self):
        """fonction qui supprime une entrée (si elle existe) de la table exemplaires a condition que ce dernier ne soit pas emprunté.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (Exist_exemp(self) != None): #si le codebar existe dans sa table
            if (exemp_checkStatut(self) == False): #si l'exemplaire n'est pas emprunté
                requetesql = """DELETE FROM exemplaires WHERE codebar = ?"""
                param = self.codebar,
                Ecriture(requetesql, param)
            else:
                print("exemplaire non rendu")
        else:
            print("exemplaire inexistant")

class Lecteur:
    """Classe définissant un lecteur, caractérisée par :
    - un numero étudiant.
    - un nom.
    - un prenom.
    - une date de naissance.
    - un niveau d'étude.
    - un numero de telephone.
    - une suspension.
    - un commentaire.
    """
    table_ref = "lecteurs"
    clef_primaire = 'num_etudiant'

    def __init__(self, num_etudiant, nom, prenom, date_naissance, niveau_etude, num_tel, suspension, commentaire): # méthode constructeur
        """Constructeur de la classe. Chaque attribut va être instancié
        avec une chaine de caractére par défaut."""

        self.num_etudiant = num_etudiant
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.niveau_etude = niveau_etude
        self.num_tel = num_tel
        self.suspension = suspension
        self.commentaire = commentaire

    def Exist_Lect(self):
        """fonction qui Recherche un num_etudiant dans la base de donnee et retourne la valeur de chaque champ dans un tuple
        ou NONE si non trouvé.
        :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
        """
        requetesql = """SELECT * FROM lecteurs WHERE num_etudiant = ? """
        param = self.num_etudiant,
        return Lecture(requetesql, param)

    def lect_checkSuspension(self):
        """fonction qui verifie la suspension d'un lecteur.
        :objet_Lect: objet dont l'attribut codebar sera recherhé.
        """
        requetesql = """SELECT suspension FROM lecteurs WHERE num_etudiant = ? """
        param = self.num_etudiant,
        suspension = Lecture(requetesql, param)
        return suspension[0] #retourne la valeur precise du champ

    def Lect_checkemprunt(self):
        """fonction qui verifie la presence d'un num_etudiant dans la table relation
            :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
        """
        requetesql = """SELECT * FROM relation WHERE id_lecteur = ? """
        param = self.num_etudiant,
        return Lecture(requetesql, param)

    def Supprimer_lect(self):
        """fonction qui supprime une entrée (si elle existe) de la table lecteurs a condition que ce dernier n'ait pas d'emprunt.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (Exist_Lect(self) != None): #si le lecteur existe dans sa table
            if (Lect_checkemprunt(self) == None): #si le lecteur n'a pas d'emprunt(s) en cours
                requetesql = """DELETE FROM lecteurs WHERE num_etudiant = ?"""
                param = self.num_etudiant,
                Ecriture(requetesql, param)
            else:
                print("un ou plusieurs exemplaire(s) non rendu(s)")
        else:
            print("Lecteur inexistant")


class Relation:
    """decrit par des attribut une relation entre un lecteur et le/les document(s) qu'il a empruntée(s),
    contient les methodes pour l'emprunt et le retour des exemplaires,
    caractérisée par :
    - un exemplaire(objet).
    - un lecteur.
    - une date d'emprunt.
    - une date de retour.
    - une methode qui effectue l'emprunt (definition des 2 dates+changement des statut).
    - une methode qui effectue le retour (redefinition des 2 dates+changement des statut).
    """
    table_ref = 'relation'
    clef_primaire = 'id_exemplaire'

    def __init__(self, obj_lect, obj_exemp, date_emprunt, date_retour): # méthode constructeur
        self.obj_lect = obj_lect #objet de class Lecteur
        self.obj_exemp = obj_exemp #objet de class Exemplaire
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour

def Validation_Lecteur(self):
    """fonction qui ajoute une entrée dans la table relation (si toutes condition d'emprunt respecté) en remplissant tout les champs.
    :objet_relat: objet instancé d'un attribut pour chaque champs de sa table.
    """
    # A FINIR, ______________________________
    if(Exist_Lect(self.obj_lect)== None):#si le num_etudiant n'existe pas dans sa table
        print("Lecteur inexistant")
    elif(lect_checkSuspension(objet_relat.obj_lect)):#si le lecteur est suspendu
        print("Lecteur suspendu")
    #elif(nbemprunt >= limiteautorisé):#si le lecteur a atteit sa limite d'emprunt
        #print("Limite d’emprunt atteinte!")
    else:
        self.objet_Lect


class Gestionnaire:
    """classe definissant un administrateur avec differentes methodes pour gestion
    de la base de donnée, caractérisée par :
    -un identifiant administrateur.
    -un mot de passe.
    -des methodes?
    """
    def __init__(self): # méthode constructeur
        self.id_utilisateur = ""
        self.mot_de_pass = ""
