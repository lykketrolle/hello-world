#!/usr/bin/python

"""
Name: Kjell Chr. Larsen
Date: 26.05.2017

Make an associating list, use the same structure as in TAP 2, where the user type
in information and is stored in a key-value pair.

            Name: First name Last name
            Street: Street name Street number
            Zip-code: Zip-code State: State
            Phone: phone number
            Email address: Email@address.com

"""
print("Welcome to the Name-address program. Here you will be asked to enter some information\n"
      "relating to your name and address. Please enter as much information as you can and the\n"
      "results will be printed out in a key:value format.\n")

f_name = input("Please enter your first name: ")
l_name = input("Please enter your last name: ")
street = input("Please enter your street name: ")
street_numb = int(input("Please enter your street number: "))
zip_code = int(input("Please enter your ZIP-code: "))
state = input("Please enter your state: ")
phone = int(input("Please enter your phone number: "))
email = input("Please enter your Email address: ")
print("")
address_book = ({'First Name:': f_name, 'Last Name:': l_name,
                'Street:': street, 'Street number:': street_numb,
                'Zip-code:': zip_code, 'State:': state,
                'Phone:': phone,
                'Email: ': email})
# This for loop will iterate through the dictionary and print each key-value pair
for i in address_book:
    print(i, address_book[i])

input("\nPlease press enter to exit.")
