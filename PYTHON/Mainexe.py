import sqlite3 #importaion de la librairie SQLite3
lien='bdd/bdd_biblio.db'
from classes.Class import *
from InitialisationBDD import *




#ajout_lecteur(num_etu, nom, prenom, date_naissance, niv_etude, num_tel, suspension, commentaire)
#ajout_exemplaire(codebar, isbn)
#supprimer_lecteur(num_etu)
#supprimer_document(codebar)
#Rechercher_lecteur()
#Rechercher_document()
#Modifier_lecteur()
#Modifier_document()
#__________________MAIN EXECUTION______________


if __name__ == '__main__':
    #Initialisation de la base de données
    print ("----------Initialisation de la base de données----------")
    creation_bdd()
    #Creation d'objets.
    print ("----------Creation d'objets----------")
    isbn_essai = InfoDocument("9782746037076", "AJAX", "Ressource informatiques", "Editions ENI, 2007", "005.13 AJA")
    exemp_essai = Exemplaire("0123456789", False, "ceci est une nouvelle aquisition du 08/02/2017",isbn_essai)
    lecteur_essai = Lecteur(11100422, "Esseddik", "Ismael", "15/12/1991", "M1", "0695306360", False, "c'est moi")
    relation_essai = Relation(lecteur_essai, exemp_essai, "09/02/2017","02/04/2017")
    #Affichage des attributs de ces objets.
    print("----------Affichage de leurs attributs---------")
    print(isbn_essai.titre)
    print(exemp_essai.codebar)
    print(lecteur_essai.commentaire)
    print(relation_essai.date_emprunt)
    print(relation_essai.obj_exemp.obj_infodoc.isbn)#(objet)retourne l'isbn d'un  exemplaire emprunté specifiquement.
    #Essai de fonction requête sur la base de donnée.
    print("----------Test de fonction---------")
    print(Reperer_infodoc(isbn_essai))#recherche de l'isbn créé dans la bdd.
    Enregistrer_infodoc(isbn_essai) #ajout dans la bdd.
    print(Reperer_exemp(exemp_essai))#recherche de l'isbn dans la bdd.
    Enregistrer_exemp(exemp_essai)#ajout dans la bdd.
