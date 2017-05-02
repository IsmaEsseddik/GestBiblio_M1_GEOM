import sqlite3  # importation de la librairie SQLite3
from isbnlib import *  # importation du package pour les metadonnées et de formatage du numero isbn
from classes.Class import *
from InitialisationBDD import *
import re
import datetime
import tkinter as tk

class Main:
    def __init__(self, master):
        self.master = master # creation d'une simple fenêtre.
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
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Login", padx=20, pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        #creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Bienvenue sur le gestionnaire de bibliotheque (en construction)", bg='bisque')
        self.login_label = tk.Label(self.cadrelib, text="Identifiant", bg='#d8d8d8')
        self.mdp_label = tk.Label(self.cadrelib, text="Mot de passe", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')
        # creation de 2 champs pour le login et mot de passe
        self.login_champ = tk.Entry(self.cadrelib, textvariable='login', width=50)
        self.mdp_champ = tk.Entry(self.cadrelib, textvariable='mdp', show='*', width=50)
        # creation boutons
        self.bouton_login = tk.Button(self.cadrelib, text="S'identifier", command= None)
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        self.boutoninvite = tk.Button(self.cadre_corp, text='Mode Invité', width=25, command = self.new_window)
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

class Menu:
    def __init__(self, master):
        self.master = master # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen",False)  # pour metre en fullscreen.
        self.master.geometry('200x350+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'black'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Menu")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadrelib = tk.LabelFrame(self.contenu, text="Fonctionnalités", padx=20, pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation boutons
        self.bouton_infodoc = tk.Button(self.cadrelib, text="InfoDocument", width=25, command=self.infodoc)
        self.bouton_exemplaire = tk.Button(self.cadrelib, text="Exemplaire", width=25, command='')
        self.bouton_lecteur = tk.Button(self.cadrelib, text='Lecteur', width=25, command=self.lect)
        self.bouton_Emprunt = tk.Button(self.cadrelib, text='Emprunt', width=25, command='')
        self.bouton_Retour = tk.Button(self.cadrelib, text='Retour', width=25, command='')
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
    """def exemp(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Exemp(self.newWindow)
    def relat(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Relat(self.newWindow)"""


class Infodoc:
    def __init__(self, master):
        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x350+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'bisque'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Gestionnaire d'edition")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='purple')
        self.cadre_corp = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadreapi = tk.Frame(self.cadre_corp, bg='#d8d8d8')
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Informations sur l'edition", labelanchor="n", padx=20, pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        self.cadreinfo = tk.Frame(self.cadrelib, bg='#d8d8d8')
        self.cadreinfoL = tk.Frame(self.cadreinfo, bg='#d8d8d8')
        self.cadreinfoR = tk.Frame(self.cadreinfo, bg='#d8d8d8')
        self.cadredesc = tk.Frame(self.cadrelib, bg='#d8d8d8')
        # creation d'un cadre libellée
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Login", padx=20, pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Gestionnaire d'editions : Ici vous pouvez rechercher un isbn via l'api google et enregistrer dans la base de données", bg='purple')
        self.isbn_label = tk.Label(self.cadreapi, text="ISBN : ", bg='#d8d8d8')  # creation de libellés.
        self.titre_label = tk.Label(self.cadreinfoL, text="Titre : ", bg='#d8d8d8')
        self.auteur_label = tk.Label(self.cadreinfoL, text="Auteur : ", bg='#d8d8d8')
        self.editeur_label = tk.Label(self.cadreinfoL, text="Editeur : ", bg='#d8d8d8')
        self.date_edition_label = tk.Label(self.cadreinfoL, text="Date d'edition : ", bg='#d8d8d8')
        self.cote_label = tk.Label(self.cadreinfoL, text="Cote : ", bg='#d8d8d8')
        self.description_label = tk.Label(self.cadredesc, text="Description : ", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')
        # creation de champs
        self.isbn_champ = tk.Entry(self.cadreapi, textvariable='', width=50, justify='center')
        self.mdp_champ = tk.Entry(self.cadrelib, textvariable='mdp', show='*', width=50)
        self.titre_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.auteur_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.editeur_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.date_edition_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.cote_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='normal')
        self.description_champ = tk.Text(self.cadredesc, height=10, width=70, wrap="word", state='disabled')
        # creation boutons
        self.bouton_api = tk.Button(self.cadreapi, text="recherche API ", command='')  # creation d'un bouton recherche api
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="top", fill="x", padx=3, pady=10)
        self.cadrelib.pack(fill="both", expand="yes")
        self.welcome_label.pack(padx=10, pady=10)
        self.isbn_label.pack(side='left')
        self.isbn_champ.pack(side='left')
        self.bouton_api.pack(side='right')

        self.cadreapi.pack(fill="both", expand="yes")
        self.cadrelib.pack(fill="both", expand="yes")
        self.cadreinfo.pack(side="left", fill="both", expand="yes", pady=20)
        self.cadreinfoL.pack(side="left", fill="both", expand="yes")
        self.cadreinfoR.pack(side="right", fill="both", expand="yes")
        self.cadredesc.pack(side="right", fill="both", expand="yes")

        self.titre_label.pack()
        self.titre_champ.pack(pady=1)
        self.auteur_label.pack()
        self.auteur_champ.pack(pady=1)
        self.editeur_label.pack()
        self.editeur_champ.pack(pady=1)
        self.date_edition_label.pack()
        self.date_edition_champ.pack(pady=1)
        self.cote_label.pack()
        self.cote_champ.pack(pady=1)
        self.description_label.pack()
        self.description_champ.pack()

        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")


class Lect:
    """ """
    def __init__(self, master):
        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x350+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('normal')  # pour maximiser la fenetre.
        self.master['bg'] = 'bisque'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Gestionnaire de lecteurs")  # pour donner un titre a l'application (title bar).
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='Blue')
        self.cadre_corp = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadrenumetu = tk.Frame(self.cadre_corp, bg='#d8d8d8')
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Informations sur le lecteur", labelanchor="n", padx=20, pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        self.cadreinfo = tk.Frame(self.cadrelib, bg='#d8d8d8')
        self.cadreinfoL = tk.Frame(self.cadreinfo, bg='#d8d8d8')
        self.cadreinfoR = tk.Frame(self.cadreinfo, bg='#d8d8d8')
        self.cadrecom = tk.Frame(self.cadrelib, bg='#d8d8d8')
        # creation d'un cadre libellée
        self.cadrelib = tk.LabelFrame(self.cadre_corp, text="Login", padx=20, pady=20, borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Gestionnaire de lecteur : Ici vous pouvez rechercher un lecteur dans la base de données", bg='blue')
        self.numetu_label = tk.Label(self.cadrenumetu, text="Numero étudiant : ", bg='#d8d8d8')  # creation de libellés.
        self.nom_label = tk.Label(self.cadreinfoL, text="Nom : ", bg='#d8d8d8')
        self.prenom_label = tk.Label(self.cadreinfoL, text="Prenom : ", bg='#d8d8d8')
        self.date_naissance_label = tk.Label(self.cadreinfoL, text="Date de naissance : ", bg='#d8d8d8')
        self.niveau_etude_label = tk.Label(self.cadreinfoL, text="Niveau d'étude : ", bg='#d8d8d8')
        self.num_tel_label = tk.Label(self.cadreinfoL, text="Numero de telephone : ", bg='#d8d8d8')
        self.suspension_label = tk.Label(self.cadreinfoL, text="Date de suspenion", bg='#d8d8d8')
        self.commentaire_label = tk.Label(self.cadrecom, text="Commentaire : ", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')
        # creation de champs
        self.numetu_champ = tk.Entry(self.cadrenumetu, textvariable='', width=50, justify='center')
        self.nom_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.prenom_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.date_naissance_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.niveau_etude_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='disabled')
        self.num_tel_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='normal')
        self.suspension_champ = tk.Entry(self.cadreinfoR, textvariable='', width=50, state='normal')
        self.commentaire_champ = tk.Text(self.cadrecom, height=10, width=70, wrap="word", state='disabled')
        # creation boutons
        self.bouton_recherche = tk.Button(self.cadrenumetu, text="Rechercher un lecteur", command='')  # creation d'un bouton recherche api
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadrenumetu.pack(fill="both", expand="yes")
        self.cadrelib.pack(fill="both", expand="yes")
        self.cadreinfo.pack(side="left", fill="both", expand="yes", pady=20)
        self.cadreinfoL.pack(side="left", fill="both", expand="yes")
        self.cadreinfoR.pack(side="right", fill="both", expand="yes")
        self.cadrecom.pack(side="right", fill="both", expand="yes")

        self.welcome_label.pack(padx=10, pady=10)
        self.numetu_label.pack(side='left')
        self.nom_label.pack()
        self.prenom_label.pack()
        self.date_naissance_label.pack()
        self.niveau_etude_label.pack()
        self.num_tel_label.pack()
        self.suspension_label.pack()
        self.commentaire_label.pack()

        self.numetu_champ.pack(side='left')
        self.nom_champ.pack(pady=1)
        self.prenom_champ.pack(pady=1)
        self.date_naissance_champ.pack(pady=1)
        self.niveau_etude_champ.pack(pady=1)
        self.num_tel_champ.pack(pady=1)
        self.suspension_champ.pack(pady=1)
        self.commentaire_champ.pack()

        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")

def main():
    creation_bdd()
    maj_suspension()
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
