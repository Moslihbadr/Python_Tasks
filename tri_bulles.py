T = [1,3,8,-6,0,88,9]
inversion = True
while inversion : 
    inversion = False
    for i in range(len(T)-1):
        if T[i]>T[i+1]:
            T[i],T[i+1] = T[i+1],T[i]
            inversion = True

print(T)