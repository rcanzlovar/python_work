#!/usr/bin/env python3
import math


# function
newstring = "Hello world".replace("world", "universe")
print(newstring)

def checkIfPrime(numToCheck):
    top = int(math.sqrt(numToCheck)) + 1
    print(top)
    for x in range(2,top):
        if (numToCheck% x == 0):
            return False
        return True

def myfunction(value):
    var = value**2
    print ("var is ",var)
    if checkIfPrime(var+1):
        print ("prime")
        return ("prime")
    else: 
        print ("not prime") 
        return ("not prime") 


def addNumbers(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print (sum)
    return(sum)

def printMembers (**age):
    for i,j in age.items():
        print("name=%s age=%s" 
            % (i,j))

# mixing fixed args, vriable args and a dictionary
# must be in this order 
def someFunc(farg, *args, **kwargs):
    print ("farg ",farg)
    for i in args:
        print ("args ",i)
    for i,j in kwargs.items():
        print("name=%s age=%s" 
            % (i,j))
    
if (2 == 4):
    print('x',myfunction(13))
    print('y',checkIfPrime(13))

    print (addNumbers(1, 2, 3, 5))

    printMembers(dave=7)
#    printMembers(bob = 57, ran = 29)

someFunc("whee",2,3,5,bob=57,ran=29)


