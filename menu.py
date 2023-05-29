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

def ajouter():
    global tri
    tri = False
    print("-"*10," Ajouter des valeurs au tableau ","-"*10)
    print("Entrer les valeurs � ajouter au tableau, * pour terminer")
    v = 0
    while v != "*":
        v = input("Valeur : ")
        if v !="*": T.append(float(v))

def modifier():
    global tri
    tri = False
    print("-" * 10, " Modifier une valeur du tableau ", "-" * 10)
    afficher()
    if len(T) > 0:
        rech = float(input("Entrer la valeur � modifier : "))
        # les exceptions
        try:
            if T.index(rech)>=0:
                rempl = float(input("Entrer la nouvelle valeur : "))
                T[T.index(rech)] = rempl
        except:
            print("Valeur introuvable")

def supprimer():
    global tri
    tri = False
    print("-" * 10, " Supprimer une valeur du tableau ", "-" * 10)
    afficher()
    if len(T) > 0:
        rech = float(input("Entrer la valeur � supprimer : "))
        # les exceptions
        try:
            if T.index(rech)>=0:
                print(f"La valeur {rech} sera supprimer du tableau")
                rep = input("confirmer la suppression O/N: ")
                if rep.upper()=="O":
                    T.remove(rech)
        except:
            print("Valeur introuvable")

def afficher():
    print("-"*10," Afficher les valeurs du tableau ","-"*10)
    if len(T) >0:
        print(f"Les valeurs du tableau : \n {T}")
    else:
        print(f"Le tableau est vide.")

def trier():
    global tri
    tri = True
    T.sort()

def rechercher():
    print("-" * 10, " Rechercher une valeur dans le tableau ", "-" * 10)
    afficher()
    if len(T) > 0:
        rech = float(input("Entrer la valeur � rechercher : "))

        # les exceptions
        try:
            if T.index(rech) >=0 :
                print(f"La valeur {rech} se trouve dans la case {T.index(rech)}")
        except :
            print("Valeur introuvable")

#programme principal
T, tri, choix = [], False, -1
while choix != 0:
    match menu():
        case 1: ajouter()
        case 2: modifier()
        case 3: supprimer()
        case 4: afficher()
        case 5: trier()
        case 6: rechercher()
        case 0: choix=0
else:
    print("Fin de traitement, à bientôt.")