'''
Author Name: Athulya A
Date: 28-10-2024
Description:Write a program that simulates a simple bank ATM system.
'''

balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance is ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Enter the amount to deposit:"))
        balance_amount=balance_amount+deposit_amount
        print(f"The deposited amount ${deposit_amount} and the current balance ${balance_amount}")
    elif choice==3:
        withdraw_amount=float(input("Enter the amount to withdraw:"))
        if withdraw_amount>balance_amount:
            print("Insufficient balance")
        else:
            balance_amount = balance_amount - withdraw_amount
            print(f"The amount withdrawn from the account ${withdraw_amount} and the current balance ${balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid entry")