#!/usr/bin/env python

"""
Made by: Kjell Chr. Larsen
Date: 16.05.2017
"""

print("This program will compare the values you enter with different operators\n"
      "like 'greater than or equal to' operators. The results will be printed "
      "to the terminal\n")


first_value = input("Please enter your first value: ")
second_value = input("Please enter your second value: ")

print()
print("Here is the result of comparing the values with different operators: \n\n")


if first_value == second_value:
    print("Your values are equal, using the '==' operator.")


if first_value != second_value:
    print("Your values are not equal. using the '!=' operator.")


if first_value > second_value or first_value >= second_value:
    print("Your first value is greater than or equal to your second value, \n"
          "using the '>' or '>=' operator.")


if first_value < second_value or first_value <= second_value:
    print("Your first value is less than or equal to your second value. \n"
          "using the '<' or '<=' operator.")
