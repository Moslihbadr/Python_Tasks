def votrechoix(liste):
    ch = -1
    while ch not in liste:
        ch = int(input("Votre choix : "))
        if ch not in liste:
            print("Choix invalide", end=" ??? ")
        else:
            return ch

def menu():
    print("-"*60)
    print("*** Menu principal ***")
    print("\t 1- Ajouter des valeurs au tableau")
    print("\t 2- Modifier une valeur au tableau")
    print("\t 3- Supprimer une valeur du tableau")
    print("\t 4- Afficher les valeurs au tableau")
    print("\t 5- Trier les valeurs du tableau")
    print("\t 6- Rechercher une valeur dans le tableau")
    print("\t 0- Quitter")
    return votrechoix([0,1,2,3,4,5,6])
liste = []
def Ajouter():
    print("-"*60)
    print("*** Ajouter ***")
    liste.append(input("entrez un element à ajouter : "))

def Modifier():
    pass

def Supprimer():
    pass

def Afficher():
    print("-"*60)
    print("*** Ajouter ***")
    print()

def Trier():
    pass

def Rechercher():
    pass

#programme principal
T, tri, choix = [], False, -1
while choix != 0:
    match menu():
        case 1: Ajouter()
        case 2: Modifier()
        case 3: Supprimer()
        case 4: Afficher()
        case 5: Trier()
        case 6: Rechercher()
        case 0: choix=0
else:
    print("Fin de traitement, à bientôt.")