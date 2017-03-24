"""Ce fichier contient les instructions pour afficher une fenetre de gestionnaire.
La fenetre devrait avoir un ecran d'acceuil pour login et mot de passe,
ainsi qu'un ecran de gestion avec un menu lateral et des onglets."""

#On commence par importer les module pour la creation d'interface graphique.
from tkinter import *
from tkinter.messagebox import *
#creation d'un classe fenetre principale(main)
class FenetreM(object):
    """classe pour la creation d'une fenetre
    """
    def Log_invite():#Commande pour se logger en tant qu'invité
        showinfo('Mode invité', "Vous etes connecté en tant qu'invité")

    #creation d'une simple fenêtre.
    gest_window_m = Tk()
    gest_window_m.attributes("-fullscreen",False)#pour metre en fullscreen.
    gest_window_m.geometry('600x350+0+0')#pour la taille et le positionnement initiale.
    gest_window_m.state('zoomed') #pour maximiser la fenetre.
    gest_window_m['bg'] = 'black' #pour le background en couleur gris.
    gest_window_m.title("Gest_Biblio - Ecran d'acceuil")#pour donner un titre a l'application (title bar).

    #creation du conteneur principale
    contenu = PanedWindow(gest_window_m, orient=VERTICAL, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')

    #creation des cadres
    cadre1 = Frame(contenu, borderwidth=3, relief=RAISED, bg ='bisque')
    cadre2 = Frame(contenu, bg='#d8d8d8')
    cadre3 = Frame(contenu, bg='#d8d8d8')

    #creation d'un cadre libellée
    cadrelib = LabelFrame(cadre2, text="Login", padx=20, pady=20, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')

    #creation de libellés.
    welcome_label = Label(cadre1,text="Bienvenue sur le gestionnaire de bibliotheque (en construction)", bg ='bisque')
    login_label = Label(cadrelib,text="Identifiant", bg='#d8d8d8')
    mdp_label = Label(cadrelib,text="Mot de passe", bg='#d8d8d8')
    edition_label = Label(cadre3,text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')


    #creation de 2 champs pour le login et mot de passe
    text_login=StringVar()
    text_mdp=StringVar()
    text_login.set("login")
    text_mdp.set("mot de passe")
    login_champ=Entry(cadrelib, textvariable=text_login, width=50)
    mdp_champ=Entry(cadrelib, textvariable=text_mdp, show='*', width=50)

    def Validation():#Commande pour se logger
        text_login=StringVar()
        print(text_login.get())

    #creation d'un bouton "S'identifier"
    bouton_login = Button(cadrelib, text="S'identifier", command= Validation)

    #bouton pour quitter
    bouton_quitter=Button(cadre3, text="Quitter", command=gest_window_m.destroy)

    #creation d'un bouton "mode invité"
    bouton_login_invite = Button(cadre2, text="Mode Invité", command= Log_invite)


    def __init__(self):#constructeur affichage
        self.contenu.pack(side=TOP, expand=Y, fill=BOTH, padx=10, pady=10)

        self.cadre1.pack(side=TOP, fill="both", padx=60, pady=10)
        self.cadre2.pack(side=TOP, padx=3, pady=3)
        self.cadre3.pack(side=TOP, fill="x", padx=3, pady=10)

        self.welcome_label.pack(padx=10, pady=10)
        self.cadrelib.pack(fill="both", expand="yes")

        self.login_label.pack()
        self.login_champ.pack()
        self.mdp_label.pack()
        self.mdp_champ.pack()
        self.bouton_login.pack()
        self.bouton_login_invite.pack()
        self.bouton_quitter.pack(side=LEFT)
        self.edition_label.pack(side=RIGHT)

        #la fenêtre doit être une boucle qui s'interromp lors de sa fermeture.
        self.gest_window_m.mainloop()
