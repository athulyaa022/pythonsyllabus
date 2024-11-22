'''
Author Name: Athulya A
Date: 22-11-2024
Description: Program to construct patterns of stars (*), using a nested for loop.
'''
row=int(input("Enter no of rows:"))
print("Increasing Triangle")
for i in range(row):
    for j in range(0,i+1):
        print("*",end=' ')
    print('')

row=int(input("\nEnter no of rows:"))
print("Decreasing Triangle")
for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end=' ')
    print('')

row=int(input("\nEnter no of rows:"))
print("Hill Pattern")
for i in range(1,row):
    for j in range(row-i):
        print(" ",end=' ')
    for k in range(i*2-1):
        print("*",end=' ')
    print('')

row=int(input("\nEnter no of rows:"))
print("Reverse Hill pattern")
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end=' ')
    for k in range(i*2-1):
        print("*",end=' ')

    print('')