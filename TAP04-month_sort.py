#!/usr/bin/python
"""
Name: Kjell Chr. Larsen
Date: 23.05.2017

Make a list of all the month in a year, print out the first letter of each month.
Then sort the month in alphabetic order.

"""

print("There are twelve months in a year. This program will list all twelve, take the \n"
      "first letter and sort in alphabetic order. ")

# First I will make a list that will store all twelve months in a list.
year = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
print(year)

# Then I will print out all the first letters in each month.
print(year[0][0:1])
print(year[1][0:1])
print(year[2][0:1])
print(year[3][0:1])
print(year[4][0:1])
print(year[5][0:1])
print(year[6][0:1])
print(year[7][0:1])
print(year[8][0:1])
print(year[9][0:1])
print(year[10][0:1])
print(year[11][0:1])
# Here I make a new list and sort the first letter of each month in alphabetic order
# Is there another way in doing this easier, or is this repetitive action the way to go?
first_ltr = [year[0][0:1], year[1][0:1], year[2][0:1], year[3][0:1], year[4][0:1], year[5][0:1],
             year[6][0:1], year[7][0:1], year[8][0:1], year[9][0:1], year[10][0:1], year[11][0:1]]

# Here I have two sorted list of the variable YEAR. The second sort, - reverse the sorted list.
print(sorted(year))
print(sorted(year, reverse=True))
print(sorted(first_ltr))
print(sorted(first_ltr, reverse=True))
