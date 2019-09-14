#!/usr/bin/env python3
import primes
from random  import randrange


# swich it up with a random number 
num =  randrange(1, 20)
num=3

answer = primes.checkIfPrime(num)
print ("answer for %d is %s" % (num,answer))

