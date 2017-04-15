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
    # exemp_essai = exemplaire("0123456789", False, "ceci est une nouvelle aquisition du 08/02/2017",a)
    # lecteur_essai = lecteur(11100422, "Esseddik", "Ismael", "15/12/1991", "M1", "0695306360", False, "c'est moi")
    # relation_essai = relation(lecteur_essai, exemp_essai, "09/02/2017","02/04/2017")
    # Affichage des attributs de ces objets.
    
