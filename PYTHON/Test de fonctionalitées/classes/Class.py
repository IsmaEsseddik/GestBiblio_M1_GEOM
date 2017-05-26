import sqlite3  # importation de la librairie SQLite3
import re  # pour les expression regulieres
import datetime  # pour les operation sur le temp
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from InitialisationBDD import *


class InfoDocument(object):
    """Classe définissant un document caractérisée par :
    - son isbn.
    - son titre.
    - son auteur.
    - son editeur.
    - son année d'édition
    - sa cote.
    table de reference : infos_documents
    clef primaire : isbn
    """
    liste_recherche = None

    def __init__(self):  # méthode constructeur
        """Constructeur de la classe. Chaque attribut va être instancié par une valeur
        indiqué en argument."""
        self.isbn = None
        self.titre = None
        self.auteur = None
        self.editeur = None
        self.date_edition = None
        self.cote = None
        self.description = None

    # --------------------Methodes pour requête de contrôle dans la base de données ----------------------------
    def exist_infodoc(self):
        """Methode qui verifie l'existance d' un isbn dans la table infos_documents, retourne une liste de tuple
        contenant les valeurs de chaque champ ou NONE si non trouvé.
        :objet_infodoc: objet dont l'attribut isbn sera recherhé.
        """
        requetesql = """SELECT * FROM infos_documents WHERE isbn = ? """
        param = self.isbn,
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    def exist_isbn_exemp(self):
        """Methode qui verifie l'existance d' un isbn dans la table des exemplaires et retourne une liste de tuple
        contenant les valeurs de chaque champ ou NONE si non trouvé.
        :objet_exemp: objet dont l'attribut isbn sera recherhé.
        """
        requetesql = """SELECT * FROM exemplaires WHERE exemp_isbn = ? """
        param = self.isbn,
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    # -----------Ajout/suppression dans une base de données.---------
    def enregistrer_infodoc(self):
        """Methode qui ajoute une entrée valide dans la table info_documents (si elle n'existe pas déja)
        en remplissant tout les champs.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (self.exist_infodoc() is None and is_isbn13(self.isbn) is True):
            # Si l'isbn est valide et n'existe pas dans sa table
                requetesql = """INSERT INTO infos_documents(isbn, titre, auteur, editeur, date_edition, cote, 
                description) VALUES(?,?,?,?,?,?,?)"""
                param = self.isbn, self.titre, self.auteur, self.editeur, self.date_edition, self.cote, self.description
                ecriture(requetesql, param)
                print("Les informations isbn ont été ajoutés dans la base de données")

        else:
            print("L'isbn existe deja dans la base de données ou est invalide ")

    def supprimer_infodoc(self):
        """Methode qui supprime une entrée (si elle existe) de la table info_documents a condition que l'isbn ne soit
        associé à aucun exemplaire.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (self.exist_infodoc() is not None):  # si l'isbn existe dans sa table
            if (self.exist_isbn_exemp() is None):  # si l'isbn n'existe pas dans la table exemplaires
                requetesql = """DELETE FROM infos_documents WHERE isbn = ?"""
                param = self.isbn,
                ecriture(requetesql, param)
                print("Les informations isbn ont été supprimée de la base de données")

            else:
                print("isbn associé à un ou plusieurs exemplaire(s)")
        else:
            print("isbn inexistant")

    # -----------Modification dans la base de données.---------
    def maj_infodoc(self):
        """Methode qui met a jour tout les champ d'une entrée dans la base de données (si l'isbn y existe)
        de la table info_documents.
        :champ: champ dans lequel sera modifier la valeur
        """
        if (self.exist_infodoc() is not None):  # si l'isbn existe dans sa table
            requetesql = """UPDATE infos_documents SET titre =  ? WHERE isbn = ? """
            param = self.titre, self.isbn,
            ecriture(requetesql, param)
            requetesql = """UPDATE infos_documents SET auteur =  ? WHERE isbn = ? """
            param = self.auteur, self.isbn,
            ecriture(requetesql, param)
            requetesql = """UPDATE infos_documents SET editeur =  ? WHERE isbn = ? """
            param = self.editeur, self.isbn,
            ecriture(requetesql, param)
            requetesql = """UPDATE infos_documents SET date_edition =  ? WHERE isbn = ? """
            param = self.date_edition, self.isbn,
            ecriture(requetesql, param)
            requetesql = """UPDATE infos_documents SET cote =  ? WHERE isbn = ? """
            param = self.cote, self.isbn,
            ecriture(requetesql, param)
            requetesql = """UPDATE infos_documents SET description = ? WHERE isbn = ? """
            param = self.description, self.isbn,
            ecriture(requetesql, param)
            print("Les informations isbn ont été mis a jour dans la base de données")

        else:
            print("isbn inexistant")

    # -----------Recherche & conditionnement de l'objet---------
    def get_liste_BDD(self, valeur, champwhere="isbn"):
        """ Methode qui, selon le champ de recherche specifié en argument, recherche dans la table InfoDocument
        la valeur specifié en argument et stock la reponse sous forme d'une liste de tuple.
        :valeur: la valeur a recherche dans le champ
        :champwhere: le champ a specifier dans lequelle la valeur sera recherché(champ isbn par defaut)
        """
        requetesql = """SELECT * FROM infos_documents WHERE """ + champwhere + """ REGEXP ? """
        param = valeur,
        if (lecture(requetesql, param) == []):
            raise NameError("Aucun resultat(s)")
        else:
            self.liste_recherche = lecture(requetesql, param)
            print(self.liste_recherche)

    def set_from_liste(self, i=0):
        """ Methode qui conditionne l'objet a partir de la liste de tuple obtenu a la derniere recherche.
        :i: numero du tuple dans la liste de recherche (1er occurence par defaut)
        """
        self.isbn = self.liste_recherche[i][0]
        self.titre = self.liste_recherche[i][1]
        self.auteur = self.liste_recherche[i][2]
        self.editeur = self.liste_recherche[i][3]
        self.date_edition = self.liste_recherche[i][4]
        self.cote = self.liste_recherche[i][5]
        self.description = self.liste_recherche[i][6]
        print(self.isbn, self.titre, self.auteur, self.editeur, self.date_edition, self.cote, self.description)

    # -----------Methode API .---------
    def recherche_api(self, numIsbn):
        """Recupere des meta-donnée grace a l'API google a partir de l'isbn et les integre aux attributs de l'objet,
        """
        metadonnees = meta(numIsbn)
        if metadonnees is not None:
            self.isbn = metadonnees['ISBN-13']
            self.titre = metadonnees['Title']
            self.auteur = ", ".join(metadonnees['Authors'])
            self.editeur = metadonnees['Publisher']
            self.date_edition = metadonnees['Year']
            self.description = desc(numIsbn)
        else:
            raise NameError("ISBN introuvable ! Verfier votre connexion)")


class Exemplaire(object):
    """ classe definissant un exemplaire avec :
    - un codebar.
    - un etat d'emprunt.
    - un commentaire.
    - l'isbn de l'exemplaire.
    table de reference : exemplaires
    clef primaire : codebar
    """

    liste_recherche = None

    def __init__(self):  # méthode constructeur
        """Constructeur de la classe. Chaque attribut va être instancié
        d'une valeur passé en argument."""
        self.codebar = None
        self.emprunt = False
        self.exemp_isbn = None
        self.exemp_commentaire = None

    # --------------------Methodes requête de contrôle dans la base de données ----------------------------
    def exist_exemp(self):
        """Methode qui verifie l'existance d'un codebar dans la base de donnee et retourne une liste de tuple contenant
        les valeurs de chaque champ ou NONE si non trouvé.
        """
        requetesql = """SELECT * FROM exemplaires WHERE codebar = ? """
        param = self.codebar,
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    def exist_exempisbn_infodoc(self):
        """Methode qui verifie l'existance d' un l'isbn dans la table infosDocument et retourne une liste de tuple
        contenant les valeurs de chaque champ ou NONE si non trouvé.
        """
        requetesql = """SELECT * FROM infos_documents WHERE isbn = ? """
        param = self.exemp_isbn,
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    def exemp_checkemprunt(self):
        """Methode qui renvoie l'etat d'emprunt du livre.
        """
        requetesql = """SELECT emprunt FROM exemplaires WHERE codebar = ? """
        param = self.codebar,
        emprunt = lecture(requetesql, param)
        return bool(emprunt[0][0])  # retourne la valeur precise du champ

    # -----------Ajout/suppression dans une base de données.---------
    def enregistrer_exemp(self):
        """Methode qui ajoute une entrée dans la table exemplaires (si elle n'existe pas deja) en remplissant tout les
         champs, à condition que l'isbn soit repertorié dans la table info_documents.
        """
        if (self.exist_exemp() is None and re.match(r"(^[0-9])", self.codebar) is not None):
            # Si le codebar n'existe pas deja dans sa table ou n'est pas une serie de chiffres
            if (self.exist_exempisbn_infodoc() is not None):
                # si l'isbn de l'objet infodoc associé existe dans sa table
                requetesql = """INSERT INTO exemplaires(codebar, emprunt, exemp_commentaire, exemp_isbn) 
                VALUES(?,?,?,?)"""
                param = self.codebar, self.emprunt, self.exemp_commentaire, self.exemp_isbn,
                ecriture(requetesql, param)
                print("L'exemplaire a été ajouté dans la base de données")
            else:
                print("isbn non trouvé")
        else:
            print("codebar deja attribué ou invalide")

    def supprimer_exemp(self):
        """Methode qui supprime une entrée (si elle existe) de la table exemplaires a condition que ce dernier ne soit
         pas emprunté.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (self.exist_exemp() is not None):  # si le codebar existe dans sa table
            if (self.exemp_checkemprunt() is False):  # si l'exemplaire n'est pas emprunté
                requetesql = """DELETE FROM exemplaires WHERE codebar = ?"""
                param = self.codebar,
                ecriture(requetesql, param)
                print("L'exemplaire a été supprimée de la base de données")

            else:
                print("exemplaire non rendu")
        else:
            print("exemplaire inexistant")

    # -----------Modification dans la base de données.---------
    def maj_exemp(self):
        """Methode qui met a jour certains champs d'une entrée dans la base de donnée (si le codebar y existe)
        de la table exemplaire.
        :champ: champ dans lequel sera modifier la valeur.
        """
        if (self.exist_exemp() is not None):  # si le codebar existe dans sa table
            requetesql = """UPDATE exemplaires SET exemp_commentaire = ? WHERE codebar = ? """
            param = self.exemp_commentaire, self.codebar,
            ecriture(requetesql, param)
            print("Les informations isbn ont été mis a jour dans la base de données")
        else:
            print("codebar inexistant")

    # -----------Recherche & conditionnement de l'objet---------
    def get_liste_BDD(self, valeur, champwhere="codebar"):
        """ Methode qui, selon le champ de recherche specifié en argument, recherche dans la table exemplaires
        la valeur specifié en argument et stock la reponse sous forme d'une liste de tuple dans un attribut
        static propre a la class.
        :valeur: la valeur a recherche dans le champ
        :champwhere: le champ a specifier dans lequelle la valeur sera recherché(champ  par defaut)
        """
        requetesql = """SELECT * FROM exemplaires WHERE """ + champwhere + """ REGEXP ? """
        param = valeur,
        if (lecture(requetesql, param) == []):
            print("Aucun resultat(s)")
        else:
            self.liste_recherche = lecture(requetesql, param)
            print(self.liste_recherche)

    def set_from_liste(self, i=0):
        """ Methode qui conditionne l'objet a partir d'un tuple de la liste de la derniere recherche
        :i: numero du tuple dans la liste de recherche (1er occurence par defaut)
        """
        self.codebar = self.liste_recherche[i][0]
        self.emprunt = self.liste_recherche[i][1]
        self.exemp_commentaire = self.liste_recherche[i][2]
        self.exemp_isbn = self.liste_recherche[i][3]
        print(self.codebar, self.emprunt, self.exemp_commentaire, self.exemp_isbn)


class Lecteur(object):
    """Classe définissant un lecteur, caractérisée par :
    - un numero étudiant.
    - un nom.
    - un prenom.
    - une date de naissance.
    - un niveau d'étude.
    - un numero de telephone.
    - une suspension.
    - un commentaire.
    table de reference : lecteurs
    clef primaire : num_etudiant
    """
    liste_recherche = None

    def __init__(self):
        """Constructeur de la classe. Chaque attribut va être instancié
        avec une chaine de caractére par défaut."""
        self.num_etudiant = ""
        self.nom = ""
        self.prenom = ""
        self.date_naissance = ""
        self.niveau_etude = ""
        self.num_tel = ""
        self.suspension = None
        self.commentaire = ""

    # --------------------Methodes requête de contrôle dans la base de données ----------------------------
    def exist_Lect(self):
        """Methode qui verifie l'existance d' un num_etudiant dans la base de donnee et retourne une liste de tuple 
        contenant les valeurs de chaque champ ou NONE si non trouvé.
        :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
        """
        requetesql = """SELECT * FROM lecteurs WHERE num_etudiant = ? """
        param = self.num_etudiant,
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    def lect_checkemprunt(self):
        """Methode qui verifie la presence d'un num_etudiant dans la table relation
            :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
        """
        requetesql = """SELECT * FROM relation WHERE id_lecteur = ? """
        param = self.num_etudiant,
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)


    # -----------Ajout/suppression dans une base de données.---------
    def enregistrer_lect(self):
        """Methode qui ajoute une entrée (si elle n'existe pas deja) dans la table exemplaires en remplissant tout les
         champs.
        :objet_exemp: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (self.exist_Lect() is None):  # si le num_etudiant n'existe pas dans sa table
            requetesql = """INSERT INTO lecteurs(num_etudiant, nom, prenom, date_naissance, niveau_etude, num_tel, 
            suspension, commentaire) VALUES(?,?,?,?,?,?,?,?)"""
            param = self.num_etudiant, self.nom, self.prenom, self.date_naissance, self.niveau_etude, self.num_tel, \
                    self.suspension, self.commentaire,
            ecriture(requetesql, param)
            print("Le lecteur a été ajouté dans la base de données")
        else:
            print("Lecteur déjà inscrit")

    def supprimer_lect(self):
        """Methode qui supprime une entrée (si elle existe) de la table lecteurs a condition que ce dernier n'ait pas
         d'emprunt.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (self.exist_Lect() is not None):  # si le lecteur existe dans sa table
            if (self.lect_checkemprunt() is None):  # si le lecteur n'a pas d'emprunt(s) en cours
                requetesql = """DELETE FROM lecteurs WHERE num_etudiant = ?"""
                param = self.num_etudiant,
                ecriture(requetesql, param)
                print("Le lecteur a été supprimée de la base de données")
            else:
                print("un ou plusieurs exemplaire(s) non rendu(s)")
        else:
            print("Lecteur inexistant")

    # -----------Modification dans la base de données.---------
    def maj_lect(self):
        """Methode qui met a jour tout les champ d'une entrée dans la base de donnée (si le numero etudiant y existe)
        de la table exemplaire.
        :champ: champ dans lequel sera modifier la valeur
        """
        if (self.exist_Lect() is not None):  # si le numero etudiant existe dans sa table
            requetesql = """UPDATE lecteurs SET nom = ? WHERE num_etudiant = ? """
            param = self.nom, self.num_etudiant,
            ecriture(requetesql, param)
            requetesql = """UPDATE lecteurs SET prenom = ? WHERE num_etudiant = ? """
            param = self.prenom, self.num_etudiant,
            ecriture(requetesql, param)
            requetesql = """UPDATE lecteurs SET date_naissance = ? WHERE num_etudiant = ? """
            param = self.date_naissance, self.num_etudiant,
            ecriture(requetesql, param)
            requetesql = """UPDATE lecteurs SET niveau_etude = ? WHERE num_etudiant = ? """
            param = self.niveau_etude, self.num_etudiant,
            ecriture(requetesql, param)
            requetesql = """UPDATE lecteurs SET num_tel = ? WHERE num_etudiant = ? """
            param = self.num_tel, self.num_etudiant,
            ecriture(requetesql, param)
            requetesql = """UPDATE lecteurs SET suspension = ? WHERE num_etudiant = ? """
            param = self.suspension, self.num_etudiant,
            ecriture(requetesql, param)
            requetesql = """UPDATE lecteurs SET commentaire = ? WHERE num_etudiant = ? """
            param = self.commentaire, self.num_etudiant,
            ecriture(requetesql, param)
            print("Les informations isbn ont été mis a jour dans la base de données")
        else:
            print("Numero étudiant inexistant")

    # -----------Recherche & conditionnement de l'objet---------
    def get_liste_BDD(self, valeur, champwhere="num_etudiant"):
        """ Methode qui, selon le champ de recherche specifié en argument, recherche dans la table lecteurs la valeur
        specifié en argument et stock la reponse sous forme d'une liste de tuple dans un attribut static propre a la
        classe.
        :valeur: la valeur a recherche dans le champ
        :champwhere: le champ a specifier dans lequelle la valeur sera recherché(num_etudiant  par defaut)
        """
        requetesql = """SELECT * FROM lecteurs WHERE """ + champwhere + """ REGEXP ? """
        param = valeur,
        if (lecture(requetesql, param) == []):
            print("Aucun resultat(s)")
        else:
            self.liste_recherche = lecture(requetesql, param)
            print(self.liste_recherche)

    def set_from_liste(self, i=0):
        """ Methode qui conditionne l'objet a partir d'un tuple de la liste de la derniere recherche
        :i: numero du tuple dans la liste de recherche (1er occurence par defaut)
        """
        self.num_etudiant = self.liste_recherche[i][0]
        self.nom = self.liste_recherche[i][1]
        self.prenom = self.liste_recherche[i][2]
        self.date_naissance = self.liste_recherche[i][3]
        self.niveau_etude = self.liste_recherche[i][4]
        self.num_tel = self.liste_recherche[i][5]
        self.suspension = self.liste_recherche[i][6]
        self.commentaire = self.liste_recherche[i][7]
        print(self.num_etudiant, self.nom, self.prenom, self.date_naissance, self.niveau_etude, self.num_tel,
              self.suspension, self.commentaire)


class Relation(object):
    """Classe definissant une relation entre un lecteur et un document qu'il a empruntée.
    Contient les methodes pour l'emprunt et le retour des exemplaires. elle est caractérisée par :
    - le codebar d'un exemplaire.
    - le numero etudiant d'un lecteur.
    - une date d'emprunt.
    - une date limite de retour.
    table de reference : relation
    clef primaire : id_exemplaire
    """

    def __init__(self):
        self.id_lecteur = None
        self.id_exemplaire = None
        self.date_emprunt = None
        self.date_retour = None
        self.liste_d_emprunt = None

    # --------------------Methodes requête de contrôle dans la base de données ----------------------------
    def exist_idLect(self):
        """Methode qui verifie l'existance d'un num_etudiant dans la table lecteurs et retourne une liste de tuple 
        contenant les valeurs de chaque champ ou NONE si non trouvé.
        """
        requetesql = """SELECT * FROM lecteurs WHERE num_etudiant = ? """
        param = self.id_lecteur,
        return lecture(requetesql, param)

    def idlect_checkSuspension(self):
        """Methode qui retourne la valeur de la suspension d'un lecteur.
        :objet_Lect: objet dont l'attribut codebar sera recherhé.
        """
        requetesql = """SELECT suspension FROM lecteurs WHERE num_etudiant = ? """
        param = self.id_lecteur,
        suspension = lecture(requetesql, param)
        return suspension[0][0]  # retourne la valeur precise du champ

    def idlect_checkemprunt(self):
        """Methode qui recherche et renvoie la liste de tout les emprunt du lecteur depuis la table relation
        :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
        """
        requetesql = """SELECT * FROM relation WHERE id_lecteur = ? """
        param = self.id_lecteur,
        return lecture(requetesql, param)

    def exist_idexemp(self):
        """Methode qui verifie l'existance d'un codebar dans la base de donnee et retourne une liste de tuple contenant
        les valeurs de chaque champ ou NONE si non trouvé."""
        requetesql = """SELECT * FROM exemplaires WHERE codebar = ? """
        param = self.id_exemplaire,
        return lecture(requetesql, param)

    def idexemp_checkemprunt(self):
        """Methode qui renvoie l'etat d'emprunt du livre."""
        requetesql = """SELECT emprunt FROM exemplaires WHERE codebar = ? """
        param = self.id_exemplaire,
        emprunt = lecture(requetesql, param)
        return bool(emprunt[0][0])

    def check_prolongement(self):
        """Methode qui renvoie l'eat du prolongement du livre."""
        requetesql = """SELECT prolongement FROM relation WHERE id_exemplaire = ? """
        param = self.id_exemplaire,
        emprunt = lecture(requetesql, param)
        return bool(emprunt[0][0])

    # -----------Methode pour selectionner un lecteur ---------
    def get_lecteur(self, num_etudiant):
        """Methode qui recherche dans la table lecteurs un num_etudiant, l'affecte a l'attribut "id_lecteur"
        et affecte la liste des exemplaires qu'il a emprunté en affichant les avertissements, a condition que 
        le lecteur existe dans la base de donnée.
        :num_etudiant: numero etudiant a rechercher.
        """
        self.id_lecteur = num_etudiant
        if (self.exist_idLect() != []):
            if (self.idlect_checkSuspension() is not None):
                print("Lecteur suspendu non autorisé a emprunter!")
            if (len(self.idlect_checkemprunt()) >= 5):
                print("Limite d'emprunt atteinte !")
            self.liste_d_emprunt = self.idlect_checkemprunt()
            print(self.liste_d_emprunt)
        else:
            print("Lecteur introuvable !")
            self.id_lecteur = ""

    # -----------Methode pour effectuer un emprunt ---------
    def enregistrer_emprunt(self, id_exemplaire):
        """Methode qui recherche dans la table exemplaires un codebar et procede a l'emprunt, a condition que le
        existe dans la base de donnée.
        :num_etudiant: numero etudiant a rechercher
        """
        self.id_exemplaire = id_exemplaire
        if (self.idlect_checkSuspension() is None):
            if (len(self.idlect_checkemprunt()) < 5):
                if (self.exist_idexemp() != []):  # si l'exemplaire existe
                    if (self.idexemp_checkemprunt() is False):  # si l'exemplaire n'est pas emprunté
                        requetesql = """UPDATE exemplaires SET emprunt = 1 WHERE codebar = ? """
                        param = self.id_exemplaire,
                        ecriture(requetesql, param)  # requetesql changement du statut du livre
                        self.date_emprunt = datetime.date.today()  # attribution de la date du jour
                        self.date_retour = datetime.date.today() + datetime.timedelta(6)
                        # calcul attribution de la date de retour
                        requetesql = """INSERT INTO relation(date_emprunt, date_retour, id_lecteur, id_exemplaire) 
                        VALUES(?,?,?,?)"""
                        param = self.date_emprunt, self.date_retour, self.id_lecteur, self.id_exemplaire,
                        ecriture(requetesql, param)  # requetesql ajout d'un champ
                        self.liste_d_emprunt = self.idlect_checkemprunt()
                        print('exemplaire emprunté')
                    else:
                        print("exemplaire deja emprunté")
                else:
                    print("Exemplaire introuvable !")
            else:
                print("Limite d'emprunt atteinte !")
        else:
            print("Lecteur suspendu non autorisé a emprunter!")

    # -----------Methode pour effectuer un retour---------
    def supprimer_emprunt(self, id_exemplaire):
        """Methode qui recherche dans la table exemplaires un codebar et procede au retour, a condition qu'il
        existe dans la base de donnée et qu'il soit emprunté.
        :num_etudiant: numero etudiant a rechercher
        """
        self.id_exemplaire = id_exemplaire
        if (self.exist_idexemp() != []):  # si l'exemplaire existe
            if (self.idexemp_checkemprunt() is True):  # si l'exemplaire n'est pas emprunté
                requetesql = """UPDATE exemplaires SET emprunt = 0 WHERE codebar = ? """
                param = self.id_exemplaire,
                ecriture(requetesql, param)  # requetesql changement du statut du livre
                requetesql = """DELETE FROM relation WHERE id_exemplaire = ?"""
                param = self.id_exemplaire,
                ecriture(requetesql, param)  # requetesql suppression de la relation dans la table
                print("La relation a été supprimée de la base de données")
                self.id_exemplaire = ""
            else:
                print("exemplaire non emprunté")
                self.id_exemplaire = ""
        else:
            print("Exemplaire introuvable !")
            self.id_exemplaire = ""

    # -----------Methode pour effectuer un prolongement---------
    def prolongement(self):
        """Methode qui effectue un prolongement de six jour sur l'emprunt selectionné
        """
        if (self.idlect_checkSuspension() is None):  # si le lecteur n'est pas suspendu
            if (self.idexemp_checkemprunt() is True):  # si l'exemplaire est emprunté
                if (self.check_prolongement() is False): # si l'exemplaire n'a pas deja été prolongé
                    requetesql = """UPDATE relation SET prolongement = 1 WHERE id_exemplaire = ? """
                    param = self.id_exemplaire,
                    ecriture(requetesql, param)  # requetesql changement du statut du prolongement
                    self.date_retour = datetime.datetime(int(self.date_retour[0:4]), int(self.date_retour[5:7]),
                                                         int(self.date_retour[8:10])) + datetime.timedelta(6)
                    # calcul & attribution de la nouvelle date de retour.
                    requetesql = """UPDATE relation SET date_retour = ? WHERE id_exemplaire = ? """
                    param = self.date_retour, self.id_exemplaire,
                    ecriture(requetesql, param)  # requetesql ajout d'un champ
                else:
                    print("un seul prolongement par emprunt autorisé")
            else:
                print("exemplaire non emprunté")
        else:
            print("Lecteur suspendu non autorisé a prolonger!")

    # -----------Methode pour selectionner un emprunt---------
    def set_from_liste(self, i=0):
        """ Methode qui conditionne l'objet a partir d'un tuple de la liste d'emprunt
        :i: numero du tuple dans la liste de recherche (1er occurence par defaut)
        """
        self.date_emprunt = self.liste_d_emprunt[i][0]
        self.date_retour = self.liste_d_emprunt[i][1]
        self.id_lecteur = self.liste_d_emprunt[i][2]
        self.id_exemplaire = self.liste_d_emprunt[i][3]
        print(self.date_emprunt, self.date_retour, self.id_lecteur, self.id_exemplaire)

