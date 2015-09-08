__author__ = 'Reilly'
# This is a simple exercise to find out if a string is a palindrome.

word = raw_input("What is the word?")
is_palindrome = False
reversed_string = ""
for letter in word:
    reversed_string = letter + reversed_string
    if word == str.capitalize(reversed_string)or word == reversed_string:
        is_palindrome = True


if is_palindrome:
     print("yes")
else:
    print("no")