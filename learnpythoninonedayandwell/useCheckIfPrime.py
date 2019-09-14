#!/usr/bin/env python3
from random  import randrange
import sys
print (sys.path)

if './modules' not in sys.path:
    sys.path.append('.modules')






import primex # this is the one that is in the modules dir
import primes # this is the one that is in the same dir


# swich it up with a random number 
num =  randrange(1, 20)
num=3

answer = primex.checkIfPrime(num)
answer = primes.checkIfPrime(num)
print ("answer for %d is %s" % (num,answer))

