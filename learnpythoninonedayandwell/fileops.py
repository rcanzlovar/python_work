#!/usr/bin/env python3
#import os
from os import remove, rename

# read two lines, print them
f = open('myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline, end='TOTALLY THE END')
print(secondline)

f.close()

# read through the file
f = open('myfile.txt', 'r')
for line in f:
    print(line, end='')
f.close()

# add a couple of lines
f = open('myfile.txt', 'a')
f.write('\nThis senencei will append')
f.write('\nPython is fun')
f.close()


busize = 24
inputFile = open('myfile.txt', 'r')
outputFIle = open('myoutfile.txt', 'w')
#msg = inputFile.read()
msg = inputFile.read(busize)
while len(msg):
    outputFIle.write(msg)
    print(msg)
#    msg = inputFile.read(busize)
    msg = inputFile.read()
inputFile.close()
outputFIle.close()
###########################

bufsize = 2400
inputFile = open('eye.jpg', 'rb')
outputFIle = open('myouteye.jpg', 'wb')
msg = inputFile.read(bufsize)
#msg = inputFile.read()
count = 0
while len(msg):
    count = count + 1
    print("X")
    outputFIle.write(msg)
    msg = inputFile.read(bufsize)
#    msg = inputFile.read()
print(count)
inputFile.close()
outputFIle.close()
#########################

remove('myoutfile.old')
rename('myoutfile.txt', 'myoutfile.old')
