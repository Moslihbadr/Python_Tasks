T = []
taille = int(input("entrez la taille du tableau : "))
for i in range(taille):
    T.append(float(input("entrez une valeur : ")))

print(T)

for i in range(taille-1):
    minpos = i
    for j in range(i,taille):
        if T[j]<T[minpos]:
            minpos = j
    T[minpos],T[i] = T[i],T[minpos]

print(T)
