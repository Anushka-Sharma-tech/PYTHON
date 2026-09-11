#------------------------------------RANDOM MODULE-----------------------------


#importing the random module and using the choice function

import random
coin1=random.choice(["heads","tails"]);
print(coin1)

# using from keyword

from random import choice
coin2=choice(["heads","tails"])
print(coin2)

# using randint(a,b) function

import random
num=random.randint(1,10)
print(num)

# using shuffle(x) function

import random
cards=["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)

#-----------------------------------STATISTICS MODULE------------------------
import statistics
print(statistics.mean([100,400]))

#----------------------------------SYS MODULE--------------------------------

import sys
print("Hello , my name is ",sys.argv[1])   # To execute you would ahve to pass the commandline argument first 

# Handling the index error that might come if we do not give a command line argument

import sys
if len(sys.argv)<2:
    print("Too less arguments...")
elif len(sys.argv)>2:
    print("too many arguments...")
else:
    print("Hello, dear",sys.argv[1])


# SYS.EXIT()

import sys
if len(sys.argv)<2:
    sys.exit("Too less arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")
print("Hello, dear",sys.argv[1])


# Passing multiple arguments

from sys import argv,exit
if len(argv)<3:
    exit("Too less arguments")
for arg in argv[1:-2]:   # slicing the vector
    print("Hello, dear",arg)