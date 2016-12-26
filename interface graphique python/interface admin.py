#Ce fichier contient les instructions pour afficher une fenetre de gestionnaire.
#La fenetre devrait avoir un ecran d'acceuil pour login et mot de passe,
#ainsi qu'un ecran de gestion avec un menu lateral et des onglets.

#         __________________ECRAN DE GESTION______________
#On commence par importer le module pour la creation d'interface graphique.
from tkinter import*

#creation de fenêtre.
gest_window2 = Tk()
# creation de libellé.
user_label = Label(gest_window2,text="connecté en tant qu'invité")
Top_menu_frame = Frame(gest_window2, width=700, height=10, borderwidth=1)
bouton_recherche = Button(Top_menu_frame, text="rechercher")
Side_menu_frame = Frame(gest_window2, width=300, height=1000, borderwidth=1)
content_Frame = Frame(gest_window2, width=700, height=1000, borderwidth=1)

entete = Label(Side_menu_frame, text="Menu")




user_label.pack() #affichage
Top_menu_frame.pack()
bouton_recherche.pack()
Side_menu_frame.pack(fill=Y)
entete.pack()
content_Frame.pack()
#la fenêtre doit être une boucle qui s'interromp lors de sa fermeture.
gest_window2.mainloop()
