
from tkinter import *
from tkinter.messagebox import *
from classes.Class import *

# creation d'un classe fenetre principale(main)
class Lecteurtk(object):
    """classe pour la creation d'une fenetre """
    # creation d'une simple fenêtre.
    gest_window_m = Tk()
    gest_window_m.attributes("-fullscreen",False)  # pour metre en fullscreen.
    gest_window_m.geometry('600x350+0+0')  # pour la taille et le positionnement initiale.
    gest_window_m.state('zoomed')  # pour maximiser la fenetre.
    gest_window_m['bg'] = 'bisque'  # pour le background en couleur gris.
    gest_window_m.title("Lecteur")  # pour donner un titre a l'application (title bar).

    # creation du conteneur principale
    contenu = PanedWindow(gest_window_m, orient=VERTICAL, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')

    # creation des cadres principaux
    cadre_entete = Frame(contenu, borderwidth=3, relief=RAISED, bg ='Blue')
    cadre_corp = Frame(contenu, bg='#d8d8d8')
    cadrenumetu = Frame(cadre_corp,bg='#d8d8d8')
    cadrelib = LabelFrame(cadre_corp, text="Informations sur le lecteur", labelanchor="n", padx=20, pady=20, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')
    cadreinfo = Frame(cadrelib, bg='#d8d8d8')
    cadreinfoL = Frame(cadreinfo, bg='#d8d8d8')
    cadreinfoR = Frame(cadreinfo, bg='#d8d8d8')
    cadrecom = Frame(cadrelib, bg='#d8d8d8')
    cadre_ppage = Frame(contenu, bg='#d8d8d8')

    #creation d'etiquettes
    welcome_label = Label(cadre_entete,text="Gestionnaire de lecteur : Ici vous pouvez rechercher un lecteur dans la base de données", bg ='blue')
    numetu_label = Label(cadrenumetu,text="Numero étudiant : ", bg='#d8d8d8')#creation de libellés.

    nom_label = Label(cadreinfoL,text ="Nom : ", bg='#d8d8d8')
    prenom_label = Label(cadreinfoL,text="Prenom : ", bg='#d8d8d8')
    date_naissance_label = Label(cadreinfoL,text="Date de naissance : ", bg='#d8d8d8')
    niveau_etude_label = Label(cadreinfoL,text="Niveau d'étude : ", bg='#d8d8d8')
    num_tel_label = Label(cadreinfoL,text="Numero de telephone : ", bg='#d8d8d8')
    suspension_label = Label(cadreinfoL,text= "Date de suspenion", bg='#d8d8d8')
    commentaire_label = Label(cadrecom,text="Commentaire : ", bg='#d8d8d8')

    # creation de champs
    numetu_champ=Entry(cadrenumetu, textvariable = '' , width=50, justify='center')
    nom_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    prenom_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    date_naissance_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    niveau_etude_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    num_tel_champ=Entry(cadreinfoR,textvariable = '', width=50, state = 'normal')
    suspension_champ=Entry(cadreinfoR,textvariable = '', width=50, state = 'normal')
    commentaire_champ=Text(cadrecom, height=10, width=70, wrap=WORD , state = 'disabled')

    # creation d'un bouton
    bouton_numetu = Button(cadrenumetu, text="Rechercher un lecteur ")
    bouton_quitter=Button(cadre_ppage, text="Quitter", command=gest_window_m.destroy)
    ver_label = Label(cadre_ppage,text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')

    # affichage
    contenu.pack(side=TOP, expand=Y, fill=BOTH, padx=10, pady=10)
    cadre_entete.pack(side=TOP, fill="both", padx=60, pady=10)

    cadre_corp.pack(padx=3, pady=3)
    cadrenumetu.pack(fill="both", expand="yes")
    cadrelib.pack(fill="both", expand="yes")
    cadreinfo.pack(side="left", fill="both", expand="yes", pady=20)
    cadreinfoL.pack(side="left", fill="both", expand="yes")
    cadreinfoR.pack(side="right", fill="both", expand="yes")
    cadrecom.pack(side="right", fill="both", expand="yes", padx=2)
    cadre_ppage.pack(side=BOTTOM, fill="x", padx=3)

    welcome_label.pack(padx=10, pady=10)
    numetu_label.pack(side='left')
    nom_label.pack()
    prenom_label.pack()
    date_naissance_label.pack()
    niveau_etude_label.pack()
    num_tel_label.pack()
    suspension_label.pack()
    commentaire_label.pack()

    numetu_champ.pack(side='left')
    nom_champ.pack(pady=1)
    prenom_champ.pack(pady=1)
    date_naissance_champ.pack(pady=1)
    niveau_etude_champ.pack(pady=1)
    num_tel_champ.pack(pady=1)
    suspension_champ.pack(pady=1)
    commentaire_champ.pack()

    bouton_numetu.pack(side='right')
    bouton_quitter.pack(side=LEFT)
    ver_label.pack(side=RIGHT)

    gest_window_m.mainloop()
