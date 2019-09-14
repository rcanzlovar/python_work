#!/usr/bin/env python3
import math


# function
newstring = "Hello world".replace("world", "universe")
print(newstring)


def checkIfPrime(numToCheck):
    top = int(math.sqrt(numToCheck)) + 1
    print(top)
    for x in range(2,top):
        print(x) 
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

print('x',myfunction(13))
print('y',checkIfPrime(13))

def addNumbers(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print (sum)
    return(sum)


print (addNumbers(1, 2, 3, 5))
# modules
# methods
