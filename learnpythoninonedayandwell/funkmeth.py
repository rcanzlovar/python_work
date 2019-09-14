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
    if checkIfPrime(var+1):
        print ("prime")
        return ("prime")
    else: 
        print ("not prime") 
        return ("not prime") 

print('x',myfunction(13))
print('y',checkIfPrime(13))

# modules
# methods
