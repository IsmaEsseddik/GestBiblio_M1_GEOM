import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re

# __________________MAIN EXECUTION______________
if __name__ == '__main__':
    print("----------Creation d'une liste de code bar que l'on veut enregistrer----------")
    tableaucodebar = ('5749275343', '0987654334', '3049586734', '1234567890',
                    '0987654321', '6789054321', '6543217890','2354435234')
    print(tableaucodebar)
    print("----------Creation d'objets ----------")
    exemp = Exemplaire()    
    print("----------Attribution de metadonnées & Enregistrement d'objets dans la base de donnée ----------")   
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

    print("----------Recherche dans la Base de données et supression----------")
    exemp.get_liste_BDD("9782746037076", "exemp_isbn")
    exemp.set_from_liste()
    exemp.supprimer_exemp()
    exemp.set_from_liste(1)
    exemp.exemp_commentaire = "ceci est une nouvelle aquisition du 08/02/2017"
    exemp.maj_exemp()
    # lecteur_essai = lecteur(11100422, "Esseddik", "Ismael", "15/12/1991", "M1", "0695306360", False, "c'est moi")
    # relation_essai = relation(lecteur_essai, exemp_essai, "09/02/2017","02/04/2017")
    # Affichage des attributs de ces objets.
    
