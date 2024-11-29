def add_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_numbers(num1+1,num2-1)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>0 and num2>0:
    result=add_numbers(num1,num2)
    print(f"The sum of two numbers is {result}")
else:
    print("The number you have entered is a negative number")
