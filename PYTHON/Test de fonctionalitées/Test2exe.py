import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re
import datetime

# __________________MAIN EXECUTION______________
if __name__ == '__main__':

    print("----------Creation d'une objet Relation--------------")
    emprunt = Relation()
    retour = Relation()
    
    print("----------execution d'emprunt/retour----------")
    emprunt.get_lecteur(12321005)
    emprunt.get_lecteur(11100422)
    emprunt.enregistrer_emprunt('1111111111')
    emprunt.enregistrer_emprunt('3049586734')
    emprunt.enregistrer_emprunt('1234567890')
    emprunt.enregistrer_emprunt('0987654321')
    retour.supprimer_emprunt('0987654321')
    emprunt.get_lecteur('11200232')
    emprunt.enregistrer_emprunt('0987654321')

