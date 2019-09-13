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

# for iterates over an iterable
iterthing = [1, 2, 3, 4, 5]
for a in iterthing:
	print (str(a) + " thing")

for a in [1, 2, 3, 4, 5]: print (str(a) + " thoing")

myDict = {'Bob':57, 'Ran':29}
for i,j in myDict.items(): 
    print ("%s is %d\n" % (i,j))
for i in myDict:
    print ("name %s age %d" % (i,myDict[i]))

for i in "Bob Anzlovar":
    print (i)
