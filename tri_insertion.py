T = [1,3,8,-6,0,88,9]
for i in range(len(T)):
    j=i-1
    while j>=0 and T[j]>T[j+1]:
        T[j],T[j+1]=T[j+1],T[j]
        j-=1

print(T)