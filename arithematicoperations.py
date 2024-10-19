'''
Author Name: Athulya A
Date: 19-10-2024
Description: Simple desktop calculator using Python. Only the five basic arithmetic operators.
'''

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
num_sum=num1+num2
print("The sum of num1 and num2 is:",num_sum)
num_sub=num1-num2
print("The difference when num2 is subtracted from num1 is:",num_sub)
num_product=num1*num2
print("The product of num1 and num2 is:",num_product)
num_divide=num1/num2
print("The quotient when num1 is divided by num2 is:",num_divide)
num_modulus=num1%num2
print("The remainder when num1 is divided by num2 is:",num_modulus)
result=(num1+num2)*num3/2
print("The result of (num1 + num2) * num3 / 2 is:",result)