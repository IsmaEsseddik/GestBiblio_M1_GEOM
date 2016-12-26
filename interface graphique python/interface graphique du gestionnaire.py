#Ce fichier contient les instructions pour afficher une fenetre de gestionnaire.
#La fenetre devrait avoir un ecran d'acceuil pour login et mot de passe,
#ainsi qu'un ecran de gestion avec un menu lateral et des onglets.

#         __________________ECRAN D'ACCEUIL______________
#On commence par importer le module pour la creation d'interface graphique.
from tkinter import*

#On aimerait tout d'abord creer un simple fenêtre.
gest_window = Tk()
#Ajoutons maintenant du texte, creation de libellé.
welcome_label = Label(gest_window,text="Bienvenue sur le gestionnaire de bibliotheque (en construction)")
login_label = Label(gest_window,text="Login")
mdp_label = Label(gest_window,text="Mot de passe")


#creation de 2 champs pour le login et mot de passe
text_login=StringVar()
text_mdp=StringVar()
login_champ=Entry(gest_window, textvariable=text_login, width=30)
mdp_champ=Entry(gest_window, textvariable=text_mdp, width=30)

#creation d'un bouton "mode invité"
bouton_invite = Button(gest_window, text="Mode Invité")


welcome_label.pack() #affichage
login_label.pack()
login_champ.pack()
mdp_label.pack()
mdp_champ.pack()
bouton_invite.pack()
#la fenêtre doit être une boucle qui s'interromp lors de sa fermeture.
gest_window.mainloop()
