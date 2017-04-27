"""Ce fichier contient les instructions pour afficher une fenetre de gestionnaire.
La fenetre devrait avoir un ecran d'acceuil pour login et mot de passe,
ainsi qu'un ecran de gestion avec un menu lateral et des onglets."""

#On commence par importer les module pour la creation d'interface graphique.
from tkinter import *
from tkinter.messagebox import *
from classes.Class import *

#creation d'un classe fenetre principale(main)
class Infodoc(object):
    """classe pour la creation d'une fenetre """
    obj = InfoDocument()
    def Log_invite():#Commande pour se logger en tant qu'invité
        showinfo('Mode invité', "Vous etes connecté en tant qu'invité")

    def searchapi():
        showinfo(isbn)

    #creation d'une simple fenêtre.
    gest_window_m = Tk()
    gest_window_m.attributes("-fullscreen",False)#pour metre en fullscreen.
    gest_window_m.geometry('600x350+0+0')#pour la taille et le positionnement initiale.
    gest_window_m.state('zoomed') #pour maximiser la fenetre.
    gest_window_m['bg'] = 'bisque' #pour le background en couleur gris.
    gest_window_m.title("ISBN")#pour donner un titre a l'application (title bar).

    #creation du conteneur principale
    contenu = PanedWindow(gest_window_m, orient=VERTICAL, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')

    #creation des cadres principaux
    cadre_entete = Frame(contenu, borderwidth=3, relief=RAISED, bg ='purple')
    cadre_corp = Frame(contenu, bg='#d8d8d8')
    cadre_ppage = Frame(contenu, bg='#d8d8d8')

    cadreapi = Frame(cadre_corp,bg='#d8d8d8')
    isbn_label = Label(cadreapi,text="ISBN : ", bg='#d8d8d8')#creation de libellés.
    isbn_champ=Entry(cadreapi, textvariable = obj.isbn, width=50, justify='center')
    bouton_api = Button(cadreapi, text="recherche API ", command= searchapi)#creation d'un bouton recherche api

    #creation d'un cadre libellée
    cadrelib = LabelFrame(cadre_corp, text="Informations sur l'edition", labelanchor="n", padx=20, pady=20, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')
    cadreinfo = Frame(cadrelib, bg='#d8d8d8')
    cadreinfoL = Frame(cadreinfo, bg='#d8d8d8')
    cadreinfoR = Frame(cadreinfo, bg='#d8d8d8')
    cadredesc = Frame(cadrelib, bg='#d8d8d8')

    welcome_label = Label(cadre_entete,text="Gestionnaire d'editions : Ici vous pouvez rechercher un isbn via l'api google et enregistrer dans la base de données", bg ='purple')

    titre_label = Label(cadreinfoL,text="Titre : ", bg='#d8d8d8')
    auteur_label = Label(cadreinfoL,text="Auteur : ", bg='#d8d8d8')
    editeur_label = Label(cadreinfoL,text="Editeur : ", bg='#d8d8d8')
    date_edition_label = Label(cadreinfoL,text="Date d'edition : ", bg='#d8d8d8')
    cote_label = Label(cadreinfoL,text="Cote : ", bg='#d8d8d8')
    description_label = Label(cadredesc,text="Description : ", bg='#d8d8d8')

    ver_label = Label(cadre_ppage,text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')

    #creation de champs
    titre_champ=Entry(cadreinfoR, textvariable = obj.titre, width=50, state = 'disabled')
    auteur_champ=Entry(cadreinfoR, textvariable = obj.auteur, width=50, state = 'disabled')
    editeur_champ=Entry(cadreinfoR, textvariable = obj.editeur, width=50, state = 'disabled')
    date_edition_champ=Entry(cadreinfoR, textvariable = obj.date_edition, width=50, state = 'disabled')
    cote_champ=Entry(cadreinfoR,textvariable = obj.cote, width=50, state = 'normal')
    description_champ=Entry(cadredesc, textvariable = obj.description, width=50, state = 'disabled')

    #bouton pour quitter
    bouton_quitter=Button(cadre_ppage, text="Quitter", command=gest_window_m.destroy)

    def __init__(self):#constructeur affichage
        self.contenu.pack(side=TOP, expand=Y, fill=BOTH, padx=10, pady=10)

        self.cadre_entete.pack(side=TOP, fill="both", padx=60, pady=10)
        self.cadre_corp.pack(padx=3, pady=3)
        self.isbn_label.pack(side='left')
        self.isbn_champ.pack(side='left')
        self.bouton_api.pack(side='right')

        self.welcome_label.pack(padx=10, pady=10)

        self.cadreapi.pack(fill="both", expand="yes")
        self.cadrelib.pack(fill="both", expand="yes")
        self.cadreinfo.pack(side="left", fill="both", expand="yes", padx=10)
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

        self.bouton_quitter.pack(side=LEFT)

        self.cadre_ppage.pack(side=BOTTOM, fill="x", padx=3, pady=10)
        self.ver_label.pack(side=RIGHT)

        #la fenêtre doit être une boucle qui s'interromp lors de sa fermeture.
        self.gest_window_m.mainloop()
