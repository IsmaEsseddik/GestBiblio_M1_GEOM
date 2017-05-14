import tkinter as tk
import isbnlib as lib
import datetime as dt # pour les operation sur le temp
from InitialisationBDD import *
import sqlite3
import re
import tkinter.messagebox as msg

class Retour():
    """ constructeur de l'interface graphique relatif a la gestion de la table relation de la base de données
    pour un retour d'exemplaire"""

    def __init__(self, master):
        self.id_exemplaire = tk.StringVar(master, value=None)

        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x600+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'bisque'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Gestionnaire de lecteurs")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='#16eff4')
        self.cadre_corp = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadrecodebar = tk.Frame(self.cadre_corp, bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Retour d'exemplaire", bg='#16eff4')
        self.codebar_label = tk.Label(self.cadrecodebar, text=" Codebar: ", bg='#d8d8d8')  # creation de libellés.
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017",
                                  fg='blue', bg='#d8d8d8')
        # creation de champs
        self.codebar_champ = tk.Entry(self.cadrecodebar, textvariable=self.id_exemplaire, width=50, justify='center')
        # creation boutons
        self.bouton_retour = tk.Button(self.cadre_corp, text='retour', command=self.supprimer_emprunt)
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="top", fill="x", padx=3, pady=10)
        self.cadrecodebar.pack(fill="both", expand="yes")
        self.welcome_label.pack(padx=10, pady=10)
        self.codebar_label.pack()
        self.codebar_champ.pack()
        self.bouton_retour.pack()
        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")

    def exist_idexemp(self):
        """Methode qui verifie l'existance d'un codebar dans la base de donnee et retourne une liste de tuple de contenant
        les valeurs de chaque champ ou NONE si non trouvé."""
        requetesql = """SELECT * FROM exemplaires WHERE codebar = ? """
        param = self.codebar_champ.get(),
        return lecture(requetesql, param)

    def idexemp_checkemprunt(self):
        """Methode qui renvoie l'etat d'emprunt du livre."""
        requetesql = """SELECT emprunt FROM exemplaires WHERE codebar = ? """
        param = self.codebar_champ.get(),
        emprunt = lecture(requetesql, param)
        return bool(emprunt[0][0])

    def supprimer_emprunt(self):
        """Methode qui recherche dans la table exemplaires un codebar et procede au retour, a condition qu'il
        existe dans la base de donnée et qu'il soit emprunté.
        :num_etudiant: numero etudiant a rechercher
        """
        if (self.exist_idexemp() != []):  # si l'exemplaire existe
            if (self.idexemp_checkemprunt() is True):  # si l'exemplaire n'est pas emprunté
                requetesql = """UPDATE exemplaires SET emprunt = 0 WHERE codebar = ? """
                param = self.codebar_champ.get(),
                ecriture(requetesql, param)  # requetesql changement du statut du livre
                requetesql = """DELETE FROM relation WHERE id_exemplaire = ?"""
                param = self.codebar_champ.get(),
                ecriture(requetesql, param)  # requetesql suppression de la relation dans la table
                print("La relation a été supprimée de la base de données")
                self.codebar_champ.delete(0, tk.END)
            else:
                msg.showinfo('Impossible',"exemplaire non emprunté")
                self.codebar_champ.delete(0, tk.END)
        else:
            msg.showinfo('Impossible',"Exemplaire introuvable !")
            self.codebar_champ.delete(0, tk.END)
