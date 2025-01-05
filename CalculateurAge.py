from tkinter import *
from tkinter.messagebox import *
import datetime


def validate_integer(valeur):
    # Permet d'effacer tout le champ
    if valeur == "":
        return True

    # Vérifie si la valeur est composée uniquement de chiffres
    if valeur.isdigit():
        # Autorise jusqu'à 4 chiffres
        if len(valeur) <= 4:
            # Si 4 chiffres sont saisis, valide l'année
            if len(valeur) == 4:
                annee = int(valeur)
                annee_actuelle = datetime.date.today().year
                # Vérifie la plage de l'année
                if 1900 <= annee <= annee_actuelle:
                    return True
                else:
                    return False  # Bloque si l'année est hors de la plage
            return True  # Autorise la progression jusqu'à 4 chiffres
    return False  # Bloque les entrées non numériques ou dépassant 4 chiffres


def jouer(annee):
    if len(annee) == 4 and annee.isdigit():
        annee = int(annee)
        age = datetime.date.today().year - annee
        showinfo('Votre Age :', f'Votre âge est : {age}')
        if age >= 18 :
            showinfo('Majeur !!', 'Alors, comme ça on est Majeur, petit coquin :) ')
        else:
            AnneeAvantMajorite = 18 - age
            showinfo('Mineur !!', f'Vous êtes majeur dans {AnneeAvantMajorite} ans !! Soyez patient ')
    else:
        showwarning("Error Age", "Entrez une année à partir de 1900 s'il vous plaît !")
    


if __name__ == "__main__":
    # Création de la fenêtre de l'application :
    fenetre = Tk()
    fenetre.title("Calculateur d'Âge")
    fenetre.geometry('350x100')
    fenetre.resizable(False, False)
    
    # Enregistrement de la fonction de verification de la bonne entrée d'un INT :
    validate_command = fenetre.register(validate_integer)
    annee = StringVar()

    
    # Création du panel de la page et des différents entrées de l'application :
    p = PanedWindow(fenetre, orient=VERTICAL)
    p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
    p.add(Label(p, text='Entrez-votre année de naissance : ',  anchor=CENTER))
    EntreeAnneeNaissance = Entry(fenetre, textvariable=annee, validate="key",  validatecommand=(validate_command, '%P'), width=4)
    p.add(EntreeAnneeNaissance)
    p.add(Button(fenetre, text="Calculer",  command=lambda: jouer(annee.get())))
    fenetre.mainloop()