__author__ = 'Reilly'
# This is a simple exercise to find all the consonants in a string.

string = raw_input("What state do you live in?")
consonant = True

for letter in string:
    if letter == "a":
        consonant = False
    elif letter == "e":
        consonant = False
    elif letter == "i":
        consonant = False
    elif letter == "o":
        consonant = False
    elif letter == "u":
        consonant = False
    elif letter:
        print(letter)




