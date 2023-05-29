def smaller_num(x,y):

    if x>y:
        number= y
    else:
        number= x
    return number

x = input("Enter first number:-")

y = input("Enter second number:-")

smaller = smaller_num(x,y)

print("The smaller number between " +  str(x) + " and " + str(y) + " is " + str(smaller))