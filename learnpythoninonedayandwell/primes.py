import math


def checkIfPrime(numToCheck):
    # check all of them
    top = numToCheck
    # how about half?
    top = int(numToCheck / 2) 
    # technically we just need to go up to square root
    #top = int(math.sqrt(numToCheck)) + 1
    print("top limit = ",top)
    for x in range(2,top):
        if (numToCheck% x == 0):
            return False
        return True

