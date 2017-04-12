import sqlite3 # importation de la librairie SQLite3
from isbnlib import *
# importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re

# __________________MAIN EXECUTION______________
if __name__ == '__main__':
    # Initialisation de la base de données
    print("----------Initialisation de la base de données----------")
    creation_bdd()
    # Creation d'objets.
    
    print("----------Creation d'une liste d'identifiant ISBN----------")
    tableauIsbns = ('ISBN 978-2-74603707-6', '978-2-7071-6574-9', 'num 978-2-10-071679-1', '9782100743674', '9782746712669', '9782091830513', '9782729821760')
    print(tableauIsbns)
    
    print("----------Creation de 7 objets InfoDoc----------")
    a = InfoDocument()
    b = InfoDocument()
    c = InfoDocument()
    d = InfoDocument()
    e = InfoDocument()
    f = InfoDocument()
    g = InfoDocument()
    tab = [a, b, c, d, e, f, g]

    print("----------Attribution de leur metadonnées (API)----------")
    i = 0
    while i < len(tableauIsbns):
        tab[i].Get_meta(tableauIsbns[i])
        print(tab[i].isbn, tab[i].titre, tab[i].auteur, tab[i].editeur, tab[i].date_edition, tab[i].cote, tab[i].description)
        i += 1

    print("----------Enregistrement des 6 objets dans la base de donnée----------")
    i = 0
    while i < len(tableauIsbns)-3:
        tab[i].Enregistrer_infodoc()
        i += 1
    
    # exemp_essai = Exemplaire("0123456789", False, "ceci est une nouvelle aquisition du 08/02/2017",a)
    # lecteur_essai = Lecteur(11100422, "Esseddik", "Ismael", "15/12/1991", "M1", "0695306360", False, "c'est moi")
    # relation_essai = Relation(lecteur_essai, exemp_essai, "09/02/2017","02/04/2017")
    # Affichage des attributs de ces objets.

    print("----------Affichage de leurs attributs---------")
