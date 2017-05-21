import tkinter as tk
import isbnlib as lib
from InitialisationBDD import *
import sqlite3
import re
import tkinter.messagebox as msg


class Exemp:
    """ constructeur de l'interface graphique relatif a la gestion de la la table Exemplaire de la base de données, """
    liste_recherche = None

    def __init__(self, master):
        self.codebar = tk.StringVar(master, value='')
        self.emprunt = tk.StringVar(master, value=bool(False))
        self.exemp_isbn = tk.StringVar(master, value='')
        self.exemp_commentaire = None

        self.master = master  # creation d'une simple fenêtre.
        self.master.attributes("-fullscreen", False)  # pour metre en fullscreen.
        self.master.geometry('800x600+0+0')  # pour la taille et le positionnement initiale.
        self.master.state('zoomed')  # pour maximiser la fenetre.
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
        self.cadraction = tk.Frame(self.cadreinfoR, bg='#d8d8d8')
        self.cadrecom = tk.Frame(self.cadrelib, bg='#d8d8d8')
        # creation de libellés
        self.welcome_label = tk.Label(self.cadre_entete, text="Gestionnaire d'exemplaire : Ici vous pouvez rechercher "
                                                              "un exemplaire dans la base de données", bg='orange')
        self.codebar_label = tk.Label(self.cadrecodebar, text=" Codebar: ", bg='#d8d8d8')  # creation de libellés.
        self.isbn_label = tk.Label(self.cadreinfoL, text="ISBN : ", bg='#d8d8d8')
        self.commentaire_label = tk.Label(self.cadrecom, text="Commentaire : ", bg='#d8d8d8')
        self.ver_label = tk.Label(self.cadre_ppage, text="Esseddik Ismael, M1 Geomatique ENSG, ©2017",
                                  fg='blue', bg='#d8d8d8')
        # creation de champs
        self.codebar_champ = tk.Entry(self.cadrecodebar, textvariable=self.codebar, width=50, justify='center')
        self.isbn_champ = tk.Entry(self.cadreinfoR, textvariable=self.exemp_isbn, width=50, state='normal')
        self.emprunt_label2 = tk.Label(self.cadreinfoR, textvariable=self.emprunt, width=50, state='normal')
        self.commentaire_champ = tk.Text(self.cadrecom, height=10, width=70, wrap="word", state='normal')
        # creation boutons
        self.bouton_recherche = tk.Button(self.cadrecodebar, text="Rechercher un exemplaire", command='',
                                          state='disabled')
        self.bouton_ajout = tk.Button(self.cadraction, text="Ajouter ", command=self.enregistrer_exemp)
        self.bouton_suppr = tk.Button(self.cadraction, text="Supprimer ", command=self.supprimer_exemp)
        self.bouton_maj = tk.Button(self.cadrecom, text="MiseAjour ", command=self.modif_com)
        self.bouton_quitter = tk.Button(self.cadre_ppage, text="Quitter", command=self.master.destroy)
        # affichage
        self.contenu.pack(side="top", expand="y", fill="both", padx=10, pady=10)
        self.cadre_entete.pack(side="top", fill="both", padx=60, pady=10)
        self.cadre_corp.pack(side="top", padx=3, pady=3)
        self.cadre_ppage.pack(side="top", fill="x", padx=3, pady=10)
        self.welcome_label.pack(padx=10, pady=10)
        self.cadrecodebar.pack(fill="both", expand="yes")
        self.codebar_label.pack(side='left')
        self.codebar_champ.pack(side='left')
        self.bouton_recherche.pack(side='right')

        self.cadrelib.pack(fill="both", expand="yes")
        self.cadreinfo.pack(side="left", fill="both", expand="yes", pady=20)
        self.cadreinfoL.pack(side="left", fill="both", expand="yes")
        self.cadreinfoR.pack(side="right", fill="both", expand="yes")
        self.cadraction.pack(side="bottom", fill="both", expand="no")
        self.cadrecom.pack(side="right", fill="both", expand="yes")

        self.isbn_label.pack()
        self.isbn_champ.pack()
        self.commentaire_label.pack()
        self.commentaire_champ.pack()

        self.bouton_ajout.pack(side='left')
        self.bouton_suppr.pack(side='left')
        self.bouton_maj.pack()

        self.ver_label.pack(side='right')
        self.bouton_quitter.pack(side="left")

    # --------------------Methodes requête de contrôle dans la base de données ----------------------------
    def exist_exemp(self):
        """Methode qui verifie l'existance d' un codebar dans la base de donnee et retourne une liste de tuple de contenant
        les valeurs de chaque champ ou NONE si non trouvé.
        """
        requetesql = """SELECT * FROM exemplaires WHERE codebar = ? """
        param = self.codebar_champ.get(),
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    def exist_exempisbn_infodoc(self):
        """Methode qui verifie l'existance d' un l'isbn dans la table infosDocument et retourne une liste de tuple de contenant
        les valeurs de chaque champ ou NONE si non trouvé.
        """
        requetesql = """SELECT * FROM infos_documents WHERE isbn = ? """
        param = lib.EAN13(self.isbn_champ.get()),
        if (lecture(requetesql, param) == []):
            return None
        else:
            return lecture(requetesql, param)

    def exemp_checkemprunt(self):
        """Methode qui renvoie l'etat d'emprunt du livre.
        """
        requetesql = """SELECT emprunt FROM exemplaires WHERE codebar = ? """
        param = self.codebar_champ.get(),
        emprunt = lecture(requetesql, param)
        return bool(emprunt[0][0])  # retourne la valeur precise du champ

    # -----------Ajout/suppression dans une base de données.---------
    def enregistrer_exemp(self):
        """Methode qui ajoute une entrée dans la table exemplaires (si elle n'existe pas deja) en remplissant tout les
         champs, à condition que l'isbn soit repertorié dans la table info_documents.
        """
        if (self.exist_exemp() is None and re.match(r"(^[0-9])", self.codebar_champ.get()) is not None):
            # Si le codebar est une serie de chiffre qui n'existe pas deja dans sa table.
            if (self.exist_exempisbn_infodoc() is not None):
                # si l'isbn de l'objet infodoc associé existe dans sa table
                requetesql = """INSERT INTO exemplaires(codebar, emprunt, exemp_commentaire, exemp_isbn) VALUES(?,?,?,?)"""
                param = self.codebar_champ.get(), 0, self.commentaire_champ.get(1.0, tk.END),\
                        lib.EAN13(self.isbn_champ.get()),
                ecriture(requetesql, param)
                print("L'exemplaire a été ajouté dans la base de données")
            else:
                msg.showinfo('Impossible', "isbn non trouvé", parent=self.master)
        else:
            msg.showinfo('Impossible', "codebar deja attribué ou invalide", parent=self.master)


    def supprimer_exemp(self):
        """Methode qui supprime une entrée (si elle existe) de la table exemplaires a condition que ce dernier ne soit
         pas emprunté.
        :objet_infodoc: objet instancé d'un attribut pour chaque champs de sa table.
        """
        if (self.exist_exemp() is not None):  # si le codebar existe dans sa table
            if (self.exemp_checkemprunt() is False):  # si l'exemplaire n'est pas emprunté
                requetesql = """DELETE FROM exemplaires WHERE codebar = ?"""
                param = self.codebar_champ.get(),
                ecriture(requetesql, param)
                print("L'exemplaire a été supprimée de la base de données")

            else:
                msg.showinfo('Impossible',"exemplaire non rendu", parent=self.master)
        else:
            msg.showinfo('Impossible',"exemplaire inexistant", parent=self.master)

    # -----------Modification dans la base de données.---------
    def modif_com(self):
        """Methode qui met a jour certains champs d'une entrée dans la base de donnée (si le codebar y existe)
        de la table exemplaire.
        :champ: champ dans lequel sera modifier la valeur.
        """
        if (self.exist_exemp() is not None):  # si le codebar existe dans sa table
            requetesql = """UPDATE exemplaires SET exemp_commentaire = ? WHERE codebar = ? """
            param = self.commentaire_champ.get(1.0, tk.END), self.codebar_champ.get(),
            ecriture(requetesql, param)
            print("Le champ com isbn ont été mis a jour dans la base de données")
        else:
            msg.showinfo('Impossible',"codebar inexistant", parent=self.master)

    # -----------Recherche & conditionnement de l'objet---------
    def get_liste_BDD(self, valeur, champwhere="codebar"):
        """ Methode qui, selon le champ de recherche specifié en argument, recherche dans la table exemplaires
        la valeur specifié en argument et stock la reponse sous forme d'une liste de tuple dans un attribut
        static propre a la class.
        :valeur: la valeur a recherche dans le champ
        :champwhere: le champ a specifier dans lequelle la valeur sera recherché(champ  par defaut)
        """
        requetesql = """SELECT * FROM exemplaires WHERE """ + champwhere + """ REGEXP ? """
        param = valeur,
        if (lecture(requetesql, param) == []):
            print("Aucun resultat(s)")
        else:
            self.liste_recherche = lecture(requetesql, param)
            print(self.liste_recherche)

    def set_from_liste(self, i=0):
        """ Methode qui conditionne l'objet a partir d'un tuple de la liste de la derniere recherche
        :i: numero du tuple dans la liste de recherche (1er occurence par defaut)
        """
        self.codebar = self.liste_recherche[i][0]
        self.emprunt = self.liste_recherche[i][1]
        self.exemp_commentaire = self.liste_recherche[i][2]
        self.exemp_isbn = self.liste_recherche[i][3]
        print(self.codebar, self.emprunt, self.exemp_commentaire, self.exemp_isbn)
