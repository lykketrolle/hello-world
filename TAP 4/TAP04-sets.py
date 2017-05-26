#!/usr/bin/python
"""
Name: Kjell Chr. Larsen
Date: 24.05.2017

Make two different set with fruits, copy the one set in to the other and compare
the two sets for equality and difference.

"""
print("This program will have two sets of fruits. One will then be copied,\n"
      "into the other, then a comparison of the two sets for difference and equality \n"
      "is done to show the operators used and the result produced.\n")

print("A set is an unordered collection with no duplicate elements. Curly braces or the \n"
      "set() function can be used to create sets. Note: to create an empty set, we use the \n"
      "set() and not {} - curly braces, where the latter creates an empty dictionary.\n")

print("Here is a demonstration. A set with duplicate elements: ")

print("""
"basket = {'Banana', 'Apple', 'Banana', 'Apple', 'Pear', 'Orange'}"

Here we see there are duplicate elements, lets see how the printout will be.
""")
test_basket = {'Banana', 'Apple', 'Banana', 'Apple', 'Pear', 'Orange'}

print(test_basket)

print("\nAs we can see, the printout only prints out one of the duplicate elements.\n")

# Here is the sets related to the assignment. Both sets have different and equal values
set1 = {'Grapes', 'Apples', 'Oranges', 'Pear', 'Peaches'}
set2 = {'Blueberry', 'Apricot', 'Avocado', 'Apples', 'Bilberry'}

print("SET1:", set1, "\nSET2:", set2)
print("")
"""
Now I will copy the content from set2 into set1. I do this by using the | operator.
"""
# Here I copy set2 into set1 and then print out the result
cp_set = set1 | set2
print("Here is the result of copying set2 into set1 using ' | ':\n", cp_set)
print("")
# Now I will use the ' - ' operator to check the difference between set1 and set2
diff_set = set1 - set2
print("The difference between set1 and set2: ", diff_set)

print("Now to test difference between the sets. First I test to see if every\n"
      "element is in set1 and set2 by using the ' set.difference() 'operator.\n")

print(set1.difference(set2))
print("This is the difference in the two sets.")
