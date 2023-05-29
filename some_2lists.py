T1 = [] 
T2 = [] 

taille = int(input("entrez la taille de ce liste : "))

print("remplissage de la première liste : ")
for i in range(taille):
    T1.append(float(input("entrez une valeur numérique : ")))  

print("remplissage de la deuxième  liste : ")
for j in range(taille):
    T2.append(float(input("entrez une valeur numérique : ")))

S1 = 0
S2 = 0
S = 0

for k in T1:
    S1 += k 

for l in T2:
    S2 += l 

S = S1 + S2

print(f"la somme des valeurs de ces deux listes est : {S}")




