#!/usr/bin/env python3

# read two lines, print them
f = open('myfile.txt','r')

firstline = f.readline()
secondline = f.readline()
print (firstline, end='TOTALLY THE END')
print (secondline)

f.close()

# read through the file 
f = open('myfile.txt','r')
for line in f:
    print (line, end='')
f.close()

# add a couple of lines
f = open('myfile.txt','a')
f.write('\nThis senencei will append')
f.write('\nPython is fun')
f.close()