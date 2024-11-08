'''
Author Name: Athulya A
Date: 08-11-2024
'''
n=int(input("Enter how many number to  be inputted:"))
n1=int(input("Enter first number:"))
smallest=n1
largest=n1
while n>1:
    num=int(input("Enter next number:"))
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
    n=n-1
print("The largest number is:",largest)
print("The smallest number is:",smallest)




