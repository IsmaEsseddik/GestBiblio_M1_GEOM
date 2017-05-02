from tkinter import *
from tkinter.messagebox import *
from classes.Class import *

#creation d'un classe fenetre principale(main)
class Exemplairetk(object):
    """classe pour la creation d'une fenetre """
    #creation d'une simple fenêtre.
    gest_window_m = Tk()
    gest_window_m.attributes("-fullscreen",False)#pour metre en fullscreen.
    gest_window_m.geometry('600x350+0+0')#pour la taille et le positionnement initiale.
    gest_window_m.state('zoomed') #pour maximiser la fenetre.
    gest_window_m['bg'] = 'bisque' #pour le background en couleur gris.
    gest_window_m.title("Lecteur")#pour donner un titre a l'application (title bar).

    #creation du conteneur principale
    contenu = PanedWindow(gest_window_m, orient=VERTICAL, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')

    #creation des cadres principaux
    cadre_entete = Frame(contenu, borderwidth=3, relief=RAISED, bg ='orange')
    cadre_corp = Frame(contenu, bg='#d8d8d8')
    cadrecodebar = Frame(cadre_corp,bg='#d8d8d8')
    cadrelib = LabelFrame(cadre_corp, text="Informations sur l'exemplaire", labelanchor="n", padx=20, pady=20, borderwidth=3, relief=SUNKEN, bg='#d8d8d8')
    cadreinfo = Frame(cadrelib, bg='#d8d8d8')
    cadreinfoL = Frame(cadreinfo, bg='#d8d8d8')
    cadreinfoR = Frame(cadreinfo, bg='#d8d8d8')
    cadrecom = Frame(cadrelib, bg='#d8d8d8')
    cadre_ppage = Frame(contenu, bg='#d8d8d8')

    #creation d'etiquettes
    welcome_label = Label(cadre_entete,text="Gestionnaire d'exemplaire : Ici vous pouvez rechercher un exemplaire dans la base de données", bg ='orange')
    codebar_label = Label(cadrecodebar,text="Codebar : ", bg='#d8d8d8')#creation de libellés.
    emprunt_label = Label(cadreinfoL,text ="Emprunt : ", bg='#d8d8d8')
    isbn_label = Label(cadreinfoL,text="ISBN : ", bg='#d8d8d8')
    commentaire_label = Label(cadrecom,text="Commentaire : ", bg='#d8d8d8')

    # creation de champs
    codebar_champ=Entry(cadrecodebar, textvariable = '' , width=10, justify='center')
    emprunt_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    date_naissance_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    niveau_etude_champ=Entry(cadreinfoR, textvariable = '', width=50, state = 'disabled')
    isbn_champ=Entry(cadreinfoR,textvariable = '', width=50, state = 'normal')
    suspension_champ=Entry(cadreinfoR,textvariable = '', width=50, state = 'normal')
    commentaire_champ=Text(cadrecom, height=10, width=70, wrap=WORD , state = 'disabled')

    # creation d'un bouton
    bouton_codebar = Button(cadrecodebar, text="Rechercher un exemplaire ")
    bouton_quitter=Button(cadre_ppage, text="Quitter", command=gest_window_m.destroy)
    ver_label = Label(cadre_ppage,text="V.0.0 | Esseddik Ismael, M1 Geomatique ENSG, ©2017", fg='blue', bg='#d8d8d8')

    # affichage
    contenu.pack(side=TOP, expand=Y, fill=BOTH, padx=10, pady=10)
    cadre_entete.pack(side=TOP, fill="both", padx=60, pady=10)

    cadre_corp.pack(padx=3, pady=3)
    cadrecodebar.pack(fill="both", expand="yes")
    cadrelib.pack(fill="both", expand="yes")
    cadreinfo.pack(side="left", fill="both", expand="yes", padx=10)
    cadreinfoL.pack(side="left", fill="both", expand="yes")
    cadreinfoR.pack(side="right", fill="both", expand="yes")
    cadrecom.pack(side="right", fill="both", expand="yes")
    cadre_ppage.pack(side=BOTTOM, fill="x", padx=3, pady=10)

    welcome_label.pack(padx=10)
    codebar_label.pack(side='left')
    emprunt_label.pack(pady=17)
    isbn_label.pack()
    commentaire_label.pack()

    codebar_champ.pack(side='left')
    emprunt_champ.pack(pady=20)
    isbn_champ.pack(pady=1)
    commentaire_champ.pack()

    bouton_codebar.pack(side='right')
    bouton_quitter.pack(side=LEFT)
    ver_label.pack(side=RIGHT)

    def fetch():
        print(list.get(ACTIVE))
    list = Listbox(cadre_corp)
    list.pack(side=TOP)
    Button(cadre_corp, text='fetch', command=fetch).pack()
    
    for index in range(10):
         list.insert(index, 'ligne-' + str(index))

    gest_window_m.mainloop()
