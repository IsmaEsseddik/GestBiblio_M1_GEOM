import tkinter as tk
import isbnlib
import sqlite3
import re
import tkinter.messagebox as msg

class Exemp:
    """"""
    def __init__(self, master):
        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x600+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'bisque'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Gestionnaire de lecteurs")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='orange')
        self.cadre_corp = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadrecodebar = tk.Frame(self.cadre_corp, bg='#d8d8d8')
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Informations sur le lecteur", labelanchor="n", padx=20,
                                      pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        self.cadreinfo = tk.Frame(self.cadrelib, bg='#d8d8d8')
        self.cadreinfoL = tk.Frame(self.cadreinfo, bg='#d8d8d8')
        self.cadreinfoR = tk.Frame(self.cadreinfo, bg='#d8d8d8')
        self.cadrecom = tk.Frame(self.cadrelib, bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Gestionnaire d'exemplaire : Ici vous pouvez rechercher "
                                                              "un exemplaire dans la base de données", bg='orange')
        self.codebar_label = tk.Label(self.cadrecodebar, text=" Codebar: ", bg='#d8d8d8')  # creation de libellés.
        self.isbn_label = tk.Label(self.cadreinfoL, text="ISBN : ", bg='#d8d8d8')
        self.emprunt_label = tk.Label(self.cadreinfoL, text="Emprunt :", bg='#d8d8d8')
        self.commentaire_label = tk.Label(self.cadrecom, text="Commentaire : ", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017",
                                  fg='blue', bg='#d8d8d8')
        # creation de champs
        self.codebar_champ = tk.Entry(self.cadrecodebar, textvariable='', width=50, justify='center')
        self.isbn_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='normal')
        self.emprunt_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='normal')
        self.commentaire_champ = tk.Text(self.cadrecom, height=10, width=70, wrap="word", state='normal')
        # creation boutons
        self.bouton_recherche = tk.Button(self.cadrecodebar, text="Rechercher un exemplaire", command='')
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="top", fill="x", padx=3, pady=10)
        self.cadrecodebar.pack(fill="both", expand="yes")
        self.cadrelib.pack(fill="both", expand="yes")
        self.cadreinfo.pack(side="left", fill="both", expand="yes", pady=20)
        self.cadreinfoL.pack(side="left", fill="both", expand="yes")
        self.cadreinfoR.pack(side="right", fill="both", expand="yes")
        self.cadrecom.pack(side="right", fill="both", expand="yes")

        self.welcome_label.pack(padx=10, pady=10)
        self.codebar_label.pack(side='left')
        self.codebar_champ.pack(side='left')
        self.bouton_recherche.pack(side='right')
        self.isbn_label.pack()
        self.isbn_champ.pack()
        self.emprunt_label.pack()
        self.emprunt_champ.pack(pady=5)
        self.commentaire_label.pack()
        self.commentaire_champ.pack()

        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")
