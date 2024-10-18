'''
Author Name: Athulya A
Date:18-10-2024
Description:Write a Python program that uses functions from the math module to perform the following operations on a number provided by the user:

    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.
'''

import math
numb=int(input("Enter a number:"))
num_squareroot=math.sqrt(numb)
print("Square root of",numb,":",num_squareroot)
num_factorial=math.factorial(numb)
print("Factorial of",numb,":",num_factorial)
num_power=math.pow(numb,2)
print(numb,"raised to power 2:",num_power)