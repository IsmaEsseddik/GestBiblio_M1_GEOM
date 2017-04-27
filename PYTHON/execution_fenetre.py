from pythontk.Infodoc import *
import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re
import datetime

#__________________MAIN EXECUTION______________
if __name__ == '__main__':
    print("----------Initialisation de la base de données----------")
    creation_bdd()
    maj_suspension()
    # une fenetre a la fois!! 
    fenetre = Infodoc()
