#!/usr/bin/ python
"""
Made by: Kjell Chr. Larsen
Date: 18.05.2017
"""
print("This program will compare the values you enter with different operators\n"
      "like 'greater than or equal to' operators. The results will be printed "
      "to the terminal.\n")
print("You can compare numbers against each other in the prompt below.\n")
# The variables that will hold the user input.
x = int(input("Enter a number: "))
y = int(input("Enter the number you want to compare to: "))
print("")
print("Please enter the operand you want to use. The available operands are:\n"
        "<  less than : >  greater than : == equal to : != not equal to\n"
        ">=  greater than or equal to : <=  less than or equal to:\n")

c = input(": ")
p = "First number: ", x, c, "Second number: ", y, "??"
#if c != ('<' or '>' or '==' or '>=' or '<='): # Here I want to try and exit if the input is not valid.

# Here is all the if statements that tests the different operands
# I also wanted to include a print out of the input
if c == '==':
    try:
        if x == y:
            print(p)
            print(True)
            print("You used the equal '==' operand and found the values equal:")
        else:
            print(p)
            print(False)
            print("Your values are not equal:")
    finally:
        print("Please feel free to try another comparison")
elif c == '!=':
    try:
        if x != y:
            print(p)
            print(True)
            print("You used the 'not equal' - '!=' operand and found the values not equal:")
        else:
            print(p)
            print(False)
            print("Your values are equal:")
    finally:
        print("Please feel free to try another comparison")
elif c == '>':
    try:
        if x > y:
            print(p)
            print(True)
            print("Your first value is greater than your second value.")
        else:
            print(p)
            print(False)
            print("Your first value is less than your second value.")
    finally:
        print("Please feel free to try another comparison")
elif c == '<':
    try:
        if x < y:
            print(p)
            print(True)
            print("Your first value is less than your second value")
        else:
            print(p)
            print(False)
            print("Your first value could be greater than your second value")
    finally:
        print("Please feel free to try another comparison")
elif c == '<=':
    try:
        if x <= y:
            print(p)
            print(True)
            print("You used the less than or equal to '<=' operand and found the comparison True.")
        else:
            print(p)
            print(False)
            print("Your first value is greater than and not equal to your second value.")
    finally:
        print("")
elif c == '>=':
    try:
        if x >= y:
            print(p)
            print(True)
            print("You used the greater than or equal operand and found the result to be True:")
        else:
            print(p)
            print(False)
            print("Your first value is less than and not equal to your second value.")
    finally:
        print("Please feel free to try another comparison")
else:
    print("")
    print(c, "is Unknown. Please enter a valid operand.")
