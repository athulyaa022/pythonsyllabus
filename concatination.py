'''
Author name: Athulya A
Date: 19-10-2024
Description: Create, concatenate, and print a string and access a sub-string from a given string.
'''

first_name=input("Enter your first name:")
last_name=input("Enter your second name:")
full_name=first_name +" " +last_name
print(full_name)
first_name_length=len(first_name)
print(full_name[:first_name_length])