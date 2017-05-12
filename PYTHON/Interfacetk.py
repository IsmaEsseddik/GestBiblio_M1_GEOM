from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from fenetres.Menu import *
from InitialisationBDD import *
import re
import datetime
import tkinter as tk

class Main:
    def __init__(self, master):
        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('600x350+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'black'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Ecran d'acceuil")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='bisque')
        self.cadre_corp = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        # creation d'un cadre libellée
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Login", padx=20, pady=20, borderwidth=3, relief="sunken",
                                      bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete,
                                      text="Bienvenue sur le gestionnaire de bibliotheque (en construction)",
                                      bg='bisque')
        self.login_label = tk.Label(self.cadrelib, text="Identifiant", bg='#d8d8d8')
        self.mdp_label = tk.Label(self.cadrelib, text="Mot de passe", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017",
                                  fg='blue', bg='#d8d8d8')
        # creation de 2 champs pour le login et mot de passe
        self.login_champ = tk.Entry(self.cadrelib, textvariable='login', width=50)
        self.mdp_champ = tk.Entry(self.cadrelib, textvariable='mdp', show='*', width=50)
        # creation boutons
        self.bouton_login = tk.Button(self.cadrelib, text="S'identifier", state='disabled', command=None)
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        self.boutoninvite = tk.Button(self.cadre_corp, text='Mode Invité', width=25, command=self.new_window)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="top", fill="x", padx=3, pady=10)
        self.cadrelib.pack(fill="both", expand="yes")
        self.welcome_label.pack(padx=10, pady=10)
        self.login_label.pack()
        self.login_champ.pack()
        self.mdp_label.pack()
        self.mdp_champ.pack()
        self.ver_label.pack(side='right')
        self.bouton_login.pack()
        self.bouton_quitter.pack(side="left")
        self.boutoninvite.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menu(self.newWindow)


def main():
    creation_bdd()
    maj_suspension()
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
