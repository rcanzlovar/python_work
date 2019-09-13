#!/usr/bin/env python3

# input() vs raw_input() python3 vs python2



# format methods
# 	("first Hello ", name, 
# 		" you are ", age, 
# 		" years old. ")
#	("second Hello  %s,  you are  %s years old. "
#		% (name, age))
#	("third Hello  {},  you are  {} years old. "
#		.format(name, age))


if (0 == 1):
	name = input("What is your name?")
	age = input("what is your age? ")  # first version
	age = input("hi %s, what is your age: " % (name))  # second version
	age = input(" {}, what about your age: ".format(name))  # third version
#
	print("Hello ", name, " you are ", age, " years old. ")
	print("second Hello  %s,  you are , %s, years old. "
		% (name, age))
	print("third Hello  {},  you are  {} years old. "
		.format(name, age))
#
	print(""" Hello
hello hello hello
Hello """)
#
	print(''' Hello
	hello hello hello
	Hello ''')


# escapes
if (0 == 2):
#
	print("whee's ")  # use different quptes
	print('where "they" ')  # use different quptes
	print('what\'s the deal')  # escape when the same kind of quote
	print(r"hello\tworld")  # raw output, don't interpret escapes
# control flow
# if
# True and False boolean values
	if ((5 > 4) == True):
	 print("this is using True as a boolean ")
# != == < <= > >=
# logical operators
# and or not

	if ((5 > 4 and 3 != 3) == False):
	 print("this is and ")
# else/elif
	if (1 != 2):
		print("first if")
	elif 2 == 2:
		print("second elif")
	else:
		print("its the else")

##########################################
if (2 == 3):
	userInput = input('Enter 1 or 2: ')
	if userInput == 1:
	    print("Hello World")
	    print("How are you? ")
	elif userInput == 2:
	    print("Python Rocks")
	    print("I Love python")
	else:
	    print("you did not enter a valid number")
#
    userInput2 = input("Enter a or b: ")
    if userInput2=="a":
        print ("Hello World")
        print ("How are you? ")
    elif userInput2=="b":
        print ("Python Rocks")
        print ("I Love python")
    else:
        print ("you did not enter a valid number")
#
    # the following code doesn't work. how can i make it work?
    userInput = input('Enter 1 or 2: ')
    if userInput=="1":
        print ("Hello World")
        print ("How are you? ")
    elif userInput=="2":
        print ("Python Rocks")
        print ("I Love python")
    else:
        print ("you did not enter a valid number")
#
	num1 = 12 if userInput=="1" else 13
	print ("num1 %s" % (num1))

##########################################
# for loopo
print " -=0=-"*20

# while loop


# try

# except

