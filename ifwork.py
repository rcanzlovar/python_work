#!/usr/bin/env python3

userInput = input('Enter 1 or 2: ')

if (2==3):
#
#
    if userInput == 1:
        print ("Hello World")
        print ("How are you? ")
    elif userInput == 2:
        print ("Python Rocks")
        print ("I Love python")
    else:
        print ("you did not enter a valid number")
#
    userInput2 = input("Enter a or b: ")
#
    if userInput2=="a":
        print ("Hello World")
        print ("How are you? ")
    elif userInput2=="b":
        print ("Python Rocks")
        print ("I Love python")
    else:
        print ("you did not enter a valid number")
#
#
    # the following code doesn't work. how can i make it work?
    userInput = input('Enter 1 or 2: ')
#
    if userInput=="1":
        print ("Hello World")
        print ("How are you? ")
    elif userInput=="2":
        print ("Python Rocks")
        print ("I Love python")
    else:
        print ("you did not enter a valid number")

num1 = 12 if userInput=="1" else 13
print ("num1 %s" % (num1))