def Menu():
    print("\t1 -Afficher les employés de l'entreprise")
    print("\t2 -Supprimer un employé de l'entreprise")
    print("\t3 -Ajouter un employé de l'entreprise")
    print("\t4 -Modifier un employé de l'entreprise")
    print("\t5 -Sauvegarder les informations des employées de l'entreprise")

T =[]

n = int(input("entrer le nombre de salariés : "))
for i in range(n):
    salarie = {}
    salarie['matricule']=input("entrez le matricule de l'employé : ")
    salarie['nom']=input("entrez le nom de l'employé : ")
    salarie['prenom']=input("entrez le prenom de l'employé : ")
    salarie['salaire']=int(input("entrez le salaire de l'employé : "))
    T.append(salarie)

def Afficher():
    if len(T)>0:
        for i in range(len(T)):
            print(T[i])
    else:
        print("liste est vide")

def Supprimer():
    pass

def Ajouter():
    pass

def Modifier():
    pass

def Sauvegarder():
    pass

Menu()
reponse = int(input("choisissez une option de la menu au dessus : 1,2,3,4 : "))
while reponse>=1 and reponse<=4 :
    match reponse:
        case 1:Afficher()
        case 2:Supprimer()
        case 3:Ajouter()
        case 4:Modifier()
        case 5:Sauvegarder()
