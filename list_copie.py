T1 = ["str" , 2.6786 , 3]
T2 = [4 , 5 , False]
# first methode

T1.extend(T2)
print(T1)

# second methode

for i in T2:
    T1.append(i)

print(T1)