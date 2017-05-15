import tkinter as tk
import isbnlib as lib
import datetime as dt  # pour les operation sur le temp
from InitialisationBDD import *
import sqlite3
import re
import tkinter.messagebox as msg


class Emprunt:
    def __init__(self, master):
        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x600+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'bisque'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Gestionnaire de lecteurs")  # pour donner un titre a l'application.
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='#16eff4')
        self.cadre_corp = tk.Frame(self.contenu,  bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadrenumetu = tk.Frame(self.cadre_corp, bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Emprunt d'exemplaire", bg='#16eff4')
        self.numetu_label = tk.Label(self.cadrenumetu, text=" Numero Etudiant: ", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017",
                                  fg='blue', bg='#d8d8d8')
        # creation de champs
        self.numetu_champ = tk.Entry(self.cadrenumetu, textvariable='', width=50, justify='center')
        # creation boutons
        self.bouton_rechercher = tk.Button(self.cadrenumetu, text='recherche')
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="bottom", fill="x", padx=3, pady=10)
        self.cadrenumetu.pack(side='top', fill="both", expand="yes")

        self.welcome_label.pack(padx=10, pady=10)
        self.numetu_label.pack()
        self.numetu_champ.pack()

        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")
