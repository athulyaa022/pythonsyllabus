'''
Author Name: Athulya A
Date: 28-10-2024
Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit
'''
while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    choice=int(input("Enter your choice:"))
    if choice==1:
        temp_cels=int(input("Enter temperature in Celsius:"))
        temp_fahren=(temp_cels * 9/5) + 32
        print(temp_cels,"celsius in Fahrenheit is",temp_fahren)
    elif choice==2:
        temp_fahren=int(input("Enter temperature in Fahrenheit:"))
        temp_cels=(temp_fahren - 32) * 5/9
        print(temp_fahren,"fahrenheit in Celsius is",temp_cels)
    elif choice==3:
        break
    else:
        print("Invalid entry")
