noDuplicate = []
L = [5 , 19 , 5 , 21 , 5 , 13 , 21, 5]   
for x in L:
    if x not in noDuplicate:
        noDuplicate.append(x)

print("Liste sans éléments dupliqués : " , noDuplicate)