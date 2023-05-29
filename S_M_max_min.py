T1 = []

taille = int(input("entrez la taille de ce liste : "))

for i in range(taille):
    T1.append(float(input("entrez une valeur numérique : ")))

S = 0
for j in T1:
    S += j 
print(f"la somme des valeurs de ce liste est : {S}")

M = S / taille
print(f"la moyenne des valeurs de ce liste est : {M}")


print(f"la valeur maximale dans cette liste est : {max(T1)}")
print(f"la valeur minimale dans cette liste est : {min(T1)}")

