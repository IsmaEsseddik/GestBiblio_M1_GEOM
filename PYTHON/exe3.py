import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re

# __________________MAIN EXECUTION______________
if __name__ == '__main__':
    print("----------Creation d'objets ----------")
    lecteur = Lecteur()    
    print("----------Attribution d'infos & Enregistrement d'objets dans la base de donnée ----------")   
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
    lecteur.suspension = True
    lecteur.commentaire = "n'a pas rendu ses livre a temps"
    lecteur.maj_lect()

    # relation_essai = relation(lecteur_essai, exemp_essai, "09/02/2017","02/04/2017")
    # Affichage des attributs de ces objets.
    
