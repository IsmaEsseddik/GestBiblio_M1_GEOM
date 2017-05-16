import tkinter as tk
import isbnlib as lib
import datetime as dt  # pour les operation sur le temp
from InitialisationBDD import *
import sqlite3
import re
import tkinter.messagebox as msg
import tkinter.simpledialog as msg2


class Emprunt:
    """ constructeur de l'interface graphique relatif a la gestion de la table relation de la base de données
        pour un emprunt d'exemplaire"""

    def __init__(self, master):
        self.id_lecteur = tk.StringVar(master, value=None)
        self.nom = tk.StringVar(master, value=None)
        self.prenom = tk.StringVar(master, value=None)
        self.id_exemplaire = tk.StringVar(master, value=None)
        self.date_emprunt = None
        self.date_retour = None
        self.liste_d_emprunt = []

        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x600+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('zoomed')  # pour maximiser la fenetre.
        self.master['bg'] = 'bisque'  # pour le background en couleur gris.
        self.master.title("Gest_Biblio - Gestionnaire de lecteurs")  # pour donner un titre a l'application.
        # creation du conteneur principale
        self.contenu = tk.PanedWindow(self.master, orient="vertical", borderwidth=3, relief="sunken", bg='#d8d8d8')
        # creation des cadres
        self.cadre_entete = tk.Frame(self.contenu, borderwidth=3, relief="raised", bg='#16eff4')
        self.cadre_corp = tk.Frame(self.contenu,  bg='#d8d8d8')
        self.cadre_ppage = tk.Frame(self.contenu, bg='#d8d8d8')
        self.cadrenumetu = tk.LabelFrame(self.cadre_corp, text="Etudiant", bg='#d8d8d8')
        self.cadrecodebar = tk.LabelFrame(self.cadre_corp, text='Exemplaire', bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Emprunt d'exemplaire", bg='#16eff4')
        self.numetu_label = tk.Label(self.cadrenumetu, text="Numero Etudiant: ", bg='#d8d8d8')
        self.nom_label = tk.Label(self.cadrenumetu, text="Nom: ", bg='#d8d8d8')
        self.prenom_label = tk.Label(self.cadrenumetu, text="Prenom: ", bg='#d8d8d8')

        self.codebar_label = tk.Label(self.cadrecodebar, text="Codebar", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017",
                                  fg='blue', bg='#d8d8d8')
        # creation de champs
        self.numetu_champ = tk.Entry(self.cadrenumetu, textvariable=self.id_lecteur, width=50, justify='center',
                                     state='disabled')
        self.nom_champ = tk.Entry(self.cadrenumetu, textvariable=self.nom, width=50, justify='center',
                                  state='disabled')
        self.prenom_champ = tk.Entry(self.cadrenumetu, textvariable=self.prenom, width=50, justify='center',
                                  state='disabled')
        self.codebar_champ = tk.Entry(self.cadrecodebar, textvariable=self.id_exemplaire, width=50, justify='center',
                                      state = 'disabled')
        # creation boutons
        self.bouton_codebar = tk.Button(self.cadrecodebar, text='emprunt', command=self.enregistrer_emprunt)
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="bottom", fill="x", padx=3, pady=10)
        self.cadrenumetu.pack(side='top', fill="both", expand="yes")
        self.cadrecodebar.pack(side='top', fill="both", expand="yes")

        self.welcome_label.pack(padx=10, pady=10)
        self.numetu_label.pack(side='left')
        self.numetu_champ.pack(side='left')
        self.nom_label.pack(side='left')
        self.nom_champ.pack(side='left')
        self.prenom_label.pack(side='left')
        self.prenom_champ.pack(side='left')
        self.codebar_label.pack(side='left')
        self.codebar_champ.pack(side='left')
        self.bouton_codebar.pack(side='right')

        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")
        v = msg2.askinteger('Integer', 'Entrer un numero etudiant', parent=master)
        self.id_lecteur.set(v)
        self.get_lecteur()

    # --------------------Methodes requête de contrôle dans la base de données ----------------------------
    def exist_idLect(self):
        """Methode qui verifie l'existance d'un num_etudiant dans la table lecteurs et retourne une liste de tuple 
        contenant les valeurs de chaque champ ou NONE si non trouvé.
        """
        requetesql = """SELECT * FROM lecteurs WHERE num_etudiant = ? """
        param = self.numetu_champ.get(),
        return lecture(requetesql, param)

    def idlect_checkSuspension(self):
        """Methode qui retourne la valeur de la suspension d'un lecteur.
        :objet_Lect: objet dont l'attribut codebar sera recherhé.
        """
        requetesql = """SELECT suspension FROM lecteurs WHERE num_etudiant = ? """
        param = self.numetu_champ.get(),
        suspension = lecture(requetesql, param)
        return suspension[0][0]  # retourne la valeur precise du champ

    def idlect_checkemprunt(self):
        """Methode qui recherche et renvoie la liste de tout les emprunt du lecteur depuis la table relation
        :objet_Lect: objet dont l'attribut num_etudiant sera recherhé.
        """
        requetesql = """SELECT * FROM relation WHERE id_lecteur = ? """
        param = self.numetu_champ.get(),
        return lecture(requetesql, param)

    def exist_idexemp(self):
        """Methode qui verifie l'existance d'un codebar dans la base de donnee et retourne une liste de tuple contenant
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

    # -----------Methode pour selectionner un lecteur ---------
    def get_lecteur(self):
        """Methode qui recherche dans la table lecteurs un num_etudiant, l'affecte a l'attribut "id_lecteur"
        et affecte la liste des exemplaires qu'il a emprunté en affichant les avertissements, a condition que
        le lecteur existe dans la base de données.
        :num_etudiant: numero etudiant a rechercher.
        """
        if (self.exist_idLect() != []):
            if (self.idlect_checkSuspension() is not None):
                msg.showinfo('Information', "Attention, le lecteur est suspendu ", parent=self.master)
            if (len(self.idlect_checkemprunt()) >= 5):
                msg.showinfo('Information', "Attention, Limite d'emprunt atteinte ", parent=self.master)
            self.liste_d_emprunt = self.idlect_checkemprunt()
            print(self.liste_d_emprunt)
            requetesql = """SELECT nom FROM lecteurs WHERE num_etudiant = ? """
            param = self.numetu_champ.get(),
            self.nom.set(lecture(requetesql, param)[0][0])
            requetesql = """SELECT prenom FROM lecteurs WHERE num_etudiant = ? """
            param = self.numetu_champ.get(),
            self.prenom.set(lecture(requetesql,param)[0][0])
        else:
            msg.showinfo('Information', "Lecteur introuvable !", parent=self.master)
            self.id_lecteur.set('')
            self.master.destroy()

    # -----------Methode pour effectuer un emprunt ---------
    def enregistrer_emprunt(self):
        """Methode qui recherche dans la table exemplaires un codebar et procede a l'emprunt, a condition que le
        existe dans la base de donnée.
        :num_etudiant: numero etudiant a rechercher
        """
        if (self.idlect_checkSuspension() is None):
            if (len(self.idlect_checkemprunt()) < 5):
                if (self.exist_idexemp() != []):  # si l'exemplaire existe
                    if (self.idexemp_checkemprunt() is False):  # si l'exemplaire n'est pas emprunté
                        requetesql = """UPDATE exemplaires SET emprunt = 1 WHERE codebar = ? """
                        param = self.codebar_champ.get(),
                        ecriture(requetesql, param)  # requetesql changement du statut du livre
                        self.date_emprunt = datetime.date.today()  # attribution de la date du jour
                        self.date_retour = datetime.date.today() + datetime.timedelta(6)
                        # calcul attribution de la date de retour
                        requetesql = """INSERT INTO relation(date_emprunt, date_retour, id_lecteur, id_exemplaire) 
                        VALUES(?,?,?,?)"""
                        param = self.date_emprunt, self.date_retour, self.numetu_champ.get(), self.codebar_champ.get(),
                        ecriture(requetesql, param)  # requetesql ajout d'un champ
                        self.liste_d_emprunt = self.idlect_checkemprunt()
                        print('exemplaire emprunté')
                    else:
                        msg.showerror('Impossible', "Exemplaire deja emprunté", parent=self.master)
                else:
                    msg.showerror('Impossible', "Exemplaire introuvable !", parent=self.master)
            else:
                msg.showerror('Impossible', "Limite d'emprunt atteinte !", parent=self.master)
        else:
            msg.showerror('Impossible', "Lecteur suspendu non autorisé a emprunter!", parent=self.master)