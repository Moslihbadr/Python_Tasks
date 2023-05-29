import datetime
from sqlite3 import Time
# import sys

#printign a date and time 
MyBirthDay = datetime.datetime(2001 , 9 , 29)   #you can add the hour,minute,second values 
print(f"I was born in {MyBirthDay}")

#printign the current date and time 
currentDateTime = datetime.datetime.now()
print(currentDateTime)

#convert date values to string
#strftime.org => for more 
currentDateTime = datetime.datetime.now()
print(currentDateTime.strftime("%a"))
print(currentDateTime.strftime("%A"))
print(currentDateTime.strftime("%b"))
print(currentDateTime.strftime("%B"))
print(currentDateTime.strftime("%A %B %Y"))
print(currentDateTime.strftime("%d %B %Y"))
