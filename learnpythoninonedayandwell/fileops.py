#!/usr/bin/env python3

f = open('myfile.txt','r')

firstline = f.readline()
secondline = f.readline()
print (firstline)
print (secondline)

f.close()