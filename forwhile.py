#!/usr/bin/env python3

# for loopo
print("=0=-"*12)

# while loop
if (3 == 3):
    userInput = input('Enter 1 or 2: ')
    if userInput=="1":
        print ("Hello World")
        print ("How are you? ")
    elif userInput=="":
        print ("You don't say")
    elif userInput=="2":
        print ("Python Rocks")
        print ("I Love python")
    else:
        print ("you did not enter a valid number")


iterthing = [1, 2, 3, 4, 5]
for a in iterthing:
	print (str(a) + " thing")
