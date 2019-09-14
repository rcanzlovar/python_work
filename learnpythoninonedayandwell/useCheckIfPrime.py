#!/usr/bin/env python3
import sys
print (sys.path)

if './modules' not in sys.path:
    sys.path.append('.modules')






import primex # this is the one that is in the modules dir
import primes # this is the one that is in the modules dir
from random  import randrange


# swich it up with a random number 
num =  randrange(1, 20)
num=4

answer = primex.checkIfPrime(num)
answer = primes.checkIfPrime(num)
print ("answer for %d is %s" % (num,answer))

