L = [5 , 19 , 7 , 21]   
L2 = [5 , 4 , 6 , 8]
trouv = False
for i in L :                        #THAT IS NOT CORRECT [YET]
    if i in L2:
        trouv == True
    else:
        trouv == False

if trouv == True:
    print("il y a un  élément commun entre les deux listes")
else:
    print("li y a aucun  élément commun entre les deux listes")
