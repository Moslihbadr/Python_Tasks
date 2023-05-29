T1 = ["str" , 2.6786 , 3 , 4 , 5 , False]

position = int(input("entrez la position que vous chercher : "))

indx = position - 1

if indx < len(T1):
    print(f"la position {position} contient la valeur : {T1[indx]}")
    
else:
    print("introuvable !")