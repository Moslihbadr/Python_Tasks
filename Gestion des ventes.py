# Application de gestion des ventes
# les ventes sont des dictionnaires enregistrés dans une liste
# une vente est caractérisé par : Article, Prix unitaire et Quantité

import os.path

# fonction qui retourne un choix valide d'une valeur de la 'liste'
def votrechoix(liste):
    ch = -1
    while ch not in liste:
        ch = int(input("\t\t==> Votre choix : "))
        if ch not in liste:
            print("\t\tChoix invalide", end=" ? ")
        else:
            return ch

def reponse(message, liste):
    while True:
        rep = input(message).upper()
        if rep in str(liste):
            break
    return rep

# fonction qui affiche un menu de l'application et retourne un choix
def menu():
    print("-"*60)
    print("*"*20,"Gestion des ventes","*"*20)
    print(f"\t 1 - Ajouter une vente\n"
          f"\t 2 - Modifier une vente\n"
          f"\t 3 - Supprimer une vente\n"
          f"\t 4 - Rechercher une vente\n"
          f"\t 5 - Afficher la liste des ventes\n"
          f"\t 6 - Afficher le montant total des ventes\n"
          f"\t 7 - Initialiser la liste des ventes\n"
          f"\t 8 - Enregistrer les ventes\n"
          f"\t 9 - Charger les ventes\n"
          f"\t 0 - Quitter")
    # return votrechoix([0,1,2,3,4,5,6,7,8,9])
    return int(reponse("\t\t==> Votre choix : ", [0,1,2,3,4,5,6,7,8,9]))

# procedure qui permet d'ajouter une vente dans la liste
def ajouter():
    print("*" * 20, "Ajouter des ventes", "*" * 20)
    encore =  True
    while encore:
        print("Enterer les données de la vente  : ")
        a = input("Nom article : ")
        p = float(input("Prix de vente : "))
        q = int(input("Quantité : "))
        vente = dict(article = a, prix = p, quantite  = q )
        listevente.append(vente)
        encore = reponse("Ajouter une autre vente O/N ? ", ["O","N"]) == "O"

# procedure qui permet de modifier une vente dans la liste
def modifier():
    print("*" * 20, "Modifier une vente", "*" * 20)
    if len(listevente) > 0:
        nligne = int(input("Enterer le n° de ligne de l'article à modifier : "))
        if 1 <= nligne <= len(listevente):
            v = listevente[nligne - 1]
            print(f"Article : {v['article']} \nPrix : {v['prix']:.2f} \nQuantité : {v['quantite']}")
            print("Enterer les modifcatiions  : ")
            v['article'] = input("Nom article : ")
            v['prix'] = float(input("Prix de vente : "))
            v['quantite'] = int(input("Quantité : "))
            if reponse("Valider la modification O/N ? ", ["O", "N"]) == "O":
                listevente[nligne - 1] = v
    else:
        print("Liste des ventes vide, aucun article")

# procedure qui permet de supprimer une vente de la liste
def supprimer():
    print("*" * 20, "Supprimer une vente", "*" * 20)
    if len(listevente) > 0:
        nligne = int(input("Enterer le n° de ligne de l'article à supprimer : "))
        if 1 <= nligne <= len(listevente):
            if reponse("valider la suppression O/N ? ", ["O", "N"]) == "O":
                listevente.pop(nligne-1)
                print("Suppression effectuée.")
    else:
        print("Liste des ventes vide, aucun article")

# procedure qui permet de rechercher une vente de la liste
def rechercher():
    print("*" * 20, "Rechercher une vente", "*" * 20)
    if len(listevente) > 0:
        nligne = int(input("Enterer le n° de ligne de l'article à supprimer : "))
    else:
        print("Liste des ventes vide, aucun article")

# procedure qui permet d'afficher la liste des ventes
def listedesventes():
    print("*" * 20, "Liste des ventes", "*" * 20)
    if len(listevente) > 0:
        titre=f"| Ligne | Article              | Prix     | Quantité | Valeur     |"
        print("-"*len(titre), titre, "-"*len(titre), sep="\n")
        i = 0
        for v in listevente:
            i += 1
            print(f"| {i:5} | {v['article']:20} | {v['prix']:8.2f} | {v['quantite']:8} | {(v['prix'] * v['quantite']):10.2f} |")
        print("-" * len(titre))
        montant = 0
        for v in listevente:
            montant += v['prix'] * v['quantite']
        print(f"Montant total des ventes : {montant:.2f}")
    else:
        print("Liste des ventes vide, aucun article")

# procedure  qui permet de calculer le montant total des ventes
def montanttotal():
    print("*" * 20, "Montant total des ventes", "*" * 20)
    if len(listevente) > 0:
        montant = 0
        for v in listevente:
            montant += v['prix'] * v['quantite']
        print(f"Montant total des ventes : {montant:.2f}")
    else:
        print("Liste des ventes vide, aucun article")
# procedure qui permet d'initialiser la liste des ventes
def initialiser():
    print("*" * 20, "Initialiser la liste des ventes", "*" * 20)
    if reponse("Etes-vous sure de vouloir initialiser la liste des ventes O/N ? ", ["O", "N"]) == "O":
        listevente.clear()
        print("Initialisation des ventes effectuée.")
# procedure qui permet d'enregistrer la liste des ventes dans un fichier
def enregistrer():
    print("*" * 20, "Enregistrer les ventes", "*" * 20)
    if len(listevente) > 0:
        if reponse("Enregistrer les ventes sur le fichier O/N ? ", ["O", "N"]) == "O":
            fichier = open("ventes.txt","w")
            for v in listevente:
                fichier.write(f"{v['article']};{v['prix']};{v['quantite']}\n")
            print("Enregistrement des ventes effectué.")
            fichier.close()
        else:
            print("Enregistrement des données dans le fichier abandonné.")
    else:
        print("Liste des ventes vide, impossible d'enregistrer.")

# procedure qui permet de charger la liste des ventes à partir d'un fichier
def charger():
    print("*" * 20, "Charger les ventes", "*" * 20)
    if os.path.exists('ventes.txt'):
        if reponse("Charger la liste des ventes à partir du fichier, "
                   "et ecraser les données de la liste O/N ? ", ["O", "N"]) == "O":
            fichier = open("ventes.txt","r")
            listevente.clear()
            for ligne in fichier.readlines():
                champ = ligne.split(";")
                v = dict(article=champ[0], prix=float(champ[1]), quantite=int(champ[2]))
                listevente.append(v)
            print("Chargement des ventes à partir du fichier effectué.")
            fichier.close()
        else:
            print("Chargement des données du fichier abandonné.")
    else:
        print("Fichier 'ventes.txt' introuvable, impossible de charger les données.")

# --------------------------------------------------------------
# programme principal
quitter = False
listevente = []
while not quitter:
    match menu():
        case 1 : ajouter()
        case 2 : modifier()
        case 3 : supprimer()
        case 4 : rechercher()
        case 5 : listedesventes()
        case 6 : montanttotal()
        case 7 : initialiser()
        case 8 : enregistrer()
        case 9 : charger()
        case _ : quitter = True
else:
    print("*** Fin de traitement. ***")
