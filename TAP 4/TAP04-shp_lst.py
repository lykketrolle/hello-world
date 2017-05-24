#!/usr/dev/env python

"""
Name: Kjell Chr. Larsen
Date: 23.05.2017

Make a shopping list program where the user can write in what to add to the list.

Print out the list at the end.

"""

print("This program will take your input and store it in a list. This list can then be \n"
      "used as a shopping list.")

shp_lst = []    # This i an empty list
i = 0           # Here I set the variable to zero
# I choose a while loop to handle the inputs to the list. This makes it possible for the
# user to enter as many or as few items as wanted
while 1:
    i += 1      # Here I make the variable to add values to the variable i
    item = input("Enter item %d: " % i)
    if item == '':          # This if loop will break the loop if the user enters no items
        break
    shp_lst.append(item)    # Here is the function that adds items to the list.

print("This is your shopping list:")
print(shp_lst)
