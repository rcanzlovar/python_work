#!/usr/bin/env python3 
from os import remove, rename


def printInstructions(instruction):
    print (instruction)

def getUserScore(userName):
    score = -1
    try:
        f = open ('userScores.txt','r')
        pass
    except IOError:
        f = open ('userScores.txt','w')
        f.close()
        return -1
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass

    for line in f:
        thing = line.split(',')
        if (userName == thing[0]):
            score = thing[1]
            break
    f.close()
    return score

def updateUserScore(newUser, userName, score):
    if (newUser == True):
        f = open ('userScores.txt','a')
        f.write(userName + ", " + str(score) + '\n')
        f.close()
    else:
        f1 = open ('userScores.tmp','w')
        f2 = open ('userScores.txt','r')
        for line in f2:
            content = line.split(',')
            print('len ',len(content))
            if (len(content) == 2):
                outScore = content[1].lstrip()
                if (userName == content[0]):
                    outScore = str(score)  + '\n' 
#                f1.write(content[0] + ', ' + str(outScore) + '\n')
                f1.write(content[0] + ', ' + str(outScore))
        f2.close()
        f1.close()
        remove('userScores.txt')
        rename('userScores.tmp','userScores.txt')

#updateUserScore(False, 'Ann',158)
updateUserScore(False, 'Benny',158)
updateUserScore(True, 'Bob',123)

for user in ['Ann', 'Bob', 'Darren']:

    foo = getUserScore(user)
    if (int(foo) > 0):
        print(user,foo) 
    else: 
        print ("foo",user,foo)
