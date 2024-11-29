"""
Author: daiji Kuriakose
Date:15-10-2024
Title:Python program to determine the entry ticket fare in a zoo based on age
"""
age=int(input("Enter your age"))
if age<10:
    print("Zoo fee=",7)
elif (age>=10)and(age<60):
    print("Zoo fee=",10)
else:
    print("zoo fee=",5)