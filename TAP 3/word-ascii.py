#!/usr/bin/env python

"""
Made by: Kjell Chr. Larsen
Date: 16.05.2017
"""

print("\
Make a program that let the user type in a letter and find the ASCII code for the \
letter. \nContinue to implement a way to let the user type in a number (ASCII code)\
and print out the correct symbol.")
print("")
print("")
x = input("Please enter the character you want to know the ASCII value of: ")
print("")
print("The ASCII value of ' " + x + " ' is '", ord(x), "'.")

print()

c = chr(int(input("Please enter the character you want to know the ASCII value of: ")))
print("")
print("The ASCII character ' " + c + " ' has an ASCII number of '", ord(c), "'.")

print()
print("'End of program.'")
