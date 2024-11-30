def max_numbers(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
n1=int(input("Enter first number:"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number:"))
result=max_numbers(n1,n2,n3)
print(f"The maximum number among the three numbers is {result}")