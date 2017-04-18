import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re
import datetime

# __________________MAIN EXECUTION______________
if __name__ == '__main__':

    print("----------Creation d'une objet Relation--------------")
    relat = Relation()

    print("----------execution d'un emprunt----------")
    relat.validation_lecteur(11100422)
    relat.enregistrer_emprunt('0987654334')
    relat.enregistrer_emprunt('3049586734')
    relat.enregistrer_emprunt('1234567890')
    relat.enregistrer_emprunt('0987654321')
