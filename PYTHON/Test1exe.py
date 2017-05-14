import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re

# __________________MAIN EXECUTION______________
if __name__ == '__main__':
    # Initialisation de la base de données
    print("----------Initialisation de la base de données----------")
    creation_bdd()
    print("----------Creation d'une liste d'identifiant ISBN----------")
    tableauIsbns = ('ISBN 978-2-74603707-6', '978-2-7071-6574-9', 'num 978-2-10-071679-1', '9782100743674',
                    '9782746712669', '9782091830513', '9782729821760', '9782020350518', '9782707159342')
    print(tableauIsbns)

    print("----------Creation d'objets ----------")
    infodoc = InfoDocument()
    exemp = Exemplaire()
    exemp.codebar
    exemp.emprunt
    exemp.exemp_commentaire

    print("----------Attribution de metadonnées & Enregistrement d'objets dans la base de donnée ----------")
    i = 0
    while i < len(tableauIsbns):
        infodoc.recherche_api(tableauIsbns[i])
        print(infodoc.isbn, infodoc.titre, infodoc.auteur, infodoc.editeur, infodoc.date_edition, infodoc.cote, infodoc.description)
        infodoc.enregistrer_infodoc()
        print('----')
        i += 1

    print("----------Recherche dans la Base de données et supression----------")
    infodoc.get_liste_BDD("socio", "titre")
    infodoc.set_from_liste()
    infodoc.supprimer_infodoc()
    infodoc.set_from_liste(1)
    infodoc.cote='PIJ 472'
    infodoc.description = "pas d'information"
    infodoc.maj_infodoc()
    print("---------- Creation d'une liste de code bar que l'on veut enregistrer ----------")
    tableaucodebar = ('5749275343', '0987654334', '3049586734', '1234567890',
                    '0987654321', '6789054321', '6543217890','2354435234')
    print(tableaucodebar)
    print("---------- Creation d'objet Exemplaire ----------")
    exemp = Exemplaire()
    print("---------- Attribution de metadonnées & Enregistrement d'objets dans la base de donnée ----------")
    i = 0
    while i < len(tableaucodebar):
        exemp.codebar = tableaucodebar[i]
        if (i <= 3):
            exemp.exemp_isbn = "9782746037076"  # 4 exemplaire d'ajax
        else :
            exemp.exemp_isbn = "9782100716791"  # 4 exemplaire d'optique
        print(exemp.codebar, exemp.emprunt, exemp.exemp_commentaire, exemp.exemp_isbn)
        exemp.enregistrer_exemp()
        print('----')
        i += 1

    print("----------Recherche dans la Base de données et supression ----------")
    exemp.get_liste_BDD("9782746037076", "exemp_isbn")
    exemp.set_from_liste()
    exemp.supprimer_exemp()
    exemp.set_from_liste(1)
    exemp.exemp_commentaire = "ceci est une nouvelle aquisition du 08/02/2017"
    exemp.maj_exemp()

    print("----------Creation d'objet Lecteur----------")
    lecteur = Lecteur()
    print("----------Attribution d'infos & Enregistrement des objets dans la base de donnée ----------")
    lecteur.num_etudiant = "11100422"
    lecteur.nom = "ESSEDDIK"
    lecteur.prenom = "Ismaël"
    lecteur.date_naissance = "15/12/1991"
    lecteur.niveau_etude = "M1"
    lecteur.num_tel = "0695306360"
    lecteur.commentaire = "C'est moi"
    print(lecteur.num_etudiant, lecteur.nom, lecteur.prenom, lecteur.date_naissance, lecteur.niveau_etude, lecteur.num_tel, lecteur.suspension, lecteur.commentaire)
    lecteur.enregistrer_lect()
    print('----')

    lecteur.num_etudiant = "11200422"
    lecteur.nom = "Jean"
    lecteur.prenom = "Pierre"
    lecteur.date_naissance = "12/10/1993"
    lecteur.niveau_etude = "L3"
    lecteur.num_tel = ""
    lecteur.commentaire = "ESSAI"
    print(lecteur.num_etudiant, lecteur.nom, lecteur.prenom, lecteur.date_naissance, lecteur.niveau_etude, lecteur.num_tel, lecteur.suspension, lecteur.commentaire)
    lecteur.enregistrer_lect()
    print('----')

    lecteur.num_etudiant = "11200222"
    lecteur.nom = "pierre"
    lecteur.prenom = "paul"
    lecteur.date_naissance = "12/10/1993"
    lecteur.niveau_etude = "L2"
    lecteur.num_tel = ""
    lecteur.commentaire = "ESSAI2"
    print(lecteur.num_etudiant, lecteur.nom, lecteur.prenom, lecteur.date_naissance, lecteur.niveau_etude, lecteur.num_tel, lecteur.suspension, lecteur.commentaire)
    lecteur.enregistrer_lect()
    print('----')

    lecteur.num_etudiant = "11200232"
    lecteur.nom = "Paul"
    lecteur.prenom = "Jacques"
    lecteur.date_naissance = "12/10/1993"
    lecteur.niveau_etude = "L1"
    lecteur.num_tel = ""
    lecteur.commentaire = "ESSAI3"
    print(lecteur.num_etudiant, lecteur.nom, lecteur.prenom, lecteur.date_naissance, lecteur.niveau_etude, lecteur.num_tel, lecteur.suspension, lecteur.commentaire)
    lecteur.enregistrer_lect()
    print('----')
    lecteur.num_etudiant = "12321004"
    lecteur.nom = "lecteur"
    lecteur.prenom = "M."
    lecteur.date_naissance = ""
    lecteur.niveau_etude = ""
    lecteur.num_tel = ""
    lecteur.commentaire = ""
    print(lecteur.num_etudiant, lecteur.nom, lecteur.prenom, lecteur.date_naissance, lecteur.niveau_etude, lecteur.num_tel, lecteur.suspension, lecteur.commentaire)
    lecteur.enregistrer_lect()
    print('----')

    lecteur.num_etudiant = "12321005"
    lecteur.nom = "hannibal"
    lecteur.prenom = "M."
    lecteur.date_naissance = ""
    lecteur.niveau_etude = ""
    lecteur.num_tel = ""
    lecteur.commentaire = ""
    print(lecteur.num_etudiant, lecteur.nom, lecteur.prenom, lecteur.date_naissance, lecteur.niveau_etude, lecteur.num_tel, lecteur.suspension, lecteur.commentaire)
    lecteur.enregistrer_lect()
    print('----')

    print("----------Recherche dans la Base de données et supression----------")
    lecteur.get_liste_BDD("M", "prenom")
    lecteur.set_from_liste()
    lecteur.supprimer_lect()
    lecteur.set_from_liste(1)
    lecteur.suspension = datetime.date(2017, 4, 20)
    lecteur.commentaire = "n'a pas rendu ses livre a temps"
    lecteur.maj_lect()
