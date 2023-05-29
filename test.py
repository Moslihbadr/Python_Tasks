# loops {while and for}
# tries = 3
# true_password = "moslih2001"
# while tries > 0 :
#     password = input("enter the password : ")
#     tries -= 1
#     print(f"you have { 'No' if tries == 0 else tries} chance left")
#     if password == true_password :
#         print("that's correct ,welcome")


# name = "bbaaadddddr"
# clean_name = ""
# index = 0
# for char in name :
#     index += 1
#     if name[index] == name[index+1] :          ##not completed
#         clean_name += name[index]
# print(clean_name)


# functions

# def say_hello() :
#     name = input ("enter ur name : ")
#     print(f"Hello {name}")

# say_hello()

# def say_hello(name = "unknown" , age = "unknown"  , contry = "unknown") :
#     print(f"hello {name} , your age is : {age} and your contry is : {contry}")

# say_hello("Badr" , 21 , "Morocco")
# say_hello("imad" , 26 )
# say_hello("ayoub")
# say_hello()

### devloped version of the function say_hello ###

# def say_hello(name , age , contry):
#     name = input("enter your name : ")
#     age = input("enter your age : ")
#     contry = input("enter your contry : ")
#     print(f"hello {name} , your age is : {age} and your contry is : {contry}")

# say_hello()
# Python3 program to find date after adding
# given number of days.

# Return if year is leap year or not.
# def isLeap(y):
	
# 	if (y % 100 != 0 and y % 4 == 0 or y % 400 == 0):
# 		return True
# 	return False

# # Given a date, returns number of days elapsed
# # from the beginning of the current year (1st
# # jan).
# def offsetDays(d, m, y):
	
# 	offset = d
# 	switcher = {
# 		10: 30,
# 		9: 31,
# 		8: 30,
# 		7: 31,
# 		6: 31,
# 		5: 30,
# 		4: 31,
# 		3: 30,
# 		2: 31,
# 		1: 28,
# 		0: 31
# 	}
# 	if (isLeap(y) and m > 1):
# 		offset += 1
# 	offset +=switcher.get(m)
# 	return offset


# # Given a year and days elapsed in it, finds
# # date by storing results in d and m.
# def revoffsetDays(offset, y,d, m):
# 	month = [ 0, 31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31 ]
	
# 	if (isLeap(y)):
# 		month[2] = 29
# 	for i in range(1, 13):
# 		if (offset <= month[i]):
# 			break
# 		offset = offset - month[i]
		
# 	d[0] = offset
# 	m[0] = i + 1

# # Add x days to the given date.
# def addDays(d1, m1, y1, x):
	
# 	offset1 = offsetDays(d1, m1, y1)
# 	if isLeap(y1):
# 		remDays = 366 - offset1
# 	else:
# 		remDays = 365 - offset1
		
# 	# y2 is going to store result year and
# 	# offset2 is going to store offset days
# 	# in result year.
# 	if (x <= remDays):
# 		y2 = y1
# 		offset2 = offset1 + x
# 	else:
		
# 		# x may store thousands of days.
# 		# We find correct year and offset
# 		# in the year.
# 		x -= remDays
# 		y2 = y1 + 1
# 		if isLeap(y2):
# 			y2days = 366
# 		else:
# 			y2days = 365
			
# 		while (x >= y2days):
# 			x -= y2days
# 			y2 += 1
# 			if isLeap(y2):
# 				y2days = 366
# 			else:
# 				y2days = 365
		
# 		offset2 = x
		
# 	# Find values of day and month from
# 	# offset of result year.
# 	m2 = [0]
# 	d2 = [0]
# 	revoffsetDays(offset2, y2, d2, m2)
# 	print("d2 = ",*d2,", m2 = ",*m2,", y2 = ",y2,sep="")

# # Driven Program
# d = 14
# m = 3
# y = 2015
# x = 366

# addDays(d, m, y, x)

# # This code is contributed by shubhamsingh10

# def cleanword(word) :
# 	if len(word) == 1 :
# 		return word
# 	if word[0] == word[1] :				#still not working
# 		return cleanword(word[1:])
# 	return word[0] + cleanword(word[1:])

# cleanword("bbbbbaaddr")	

#   function lambda   #

# hello = lambda name : f"hello {name}"
# print(hello("badr"))
# import os

# print(os.getcwd())

# file = open("badr.txt")
T = [1,2]
if len(T)>0:
        for i in range(len(T)):
            print(T[i])