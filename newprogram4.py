def check_triangle():
    sides=[]
    first_side=int(input("Entr first side:"))
    second_side=int(input("Enter second side:"))
    third_side=int(input("Enter third side:"))
    sides.append(first_side)
    sides.append(second_side)
    sides.append(third_side)
    sides.sort()
    if sides[-1]**2==sides[0]**2 + sides[1]**2:
        print("The given triangle is right triangle")
    else:
        print("The given triangle iS not right angle")
check_triangle()