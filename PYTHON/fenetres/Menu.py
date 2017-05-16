import tkinter as tk
import isbnlib as lib
from fenetres.Infodoc import *
from fenetres.Exemp import *
from fenetres.Lect import *
from fenetres.Emprunt import *
from fenetres.Retour import *


class Menu:
    def __init__(self, master):
        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('300x350+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'black'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Menu")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadrelib = tk.LabelFrame(self.contenu, text="Fonctionnalités", padx=20, pady=20, borderwidth=3,
                                      relief="sunken", bg='#d8d8d8')
        # creation boutons
        self.bouton_infodoc = tk.Button(self.cadrelib, text="Gestionnaire d'editions", width=25, command=self.infodoc)
        self.bouton_exemplaire = tk.Button(self.cadrelib, text="Gestionnaire d'exemplaire", width=25,
                                           command=self.exemp)
        self.bouton_lecteur = tk.Button(self.cadrelib, text='Gestionnaire de lecteur', width=25, command=self.lect)
        self.bouton_Emprunt = tk.Button(self.cadrelib, text='Faire un emprunt', width=25, command=self.emprunt)
        self.bouton_Retour = tk.Button(self.cadrelib, text='Faire un retour', width=25, command=self.retour)
        self.bouton_quitter = tk.Button(self.contenu, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadrelib.pack(fill="both", expand="yes")
        self.bouton_infodoc.pack()
        self.bouton_exemplaire.pack()
        self.bouton_lecteur.pack()
        self.bouton_Emprunt.pack()
        self.bouton_Retour.pack()
        self.bouton_quitter.pack()

    def infodoc(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Infodoc(self.newWindow)

    def lect(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Lect(self.newWindow)

    def exemp(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Exemp(self.newWindow)

    def emprunt(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Emprunt(self.newWindow)

    def retour(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Retour(self.newWindow)
