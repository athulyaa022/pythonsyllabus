def sum_list(list1):
    total=0
    for i in list1:
        total=total+i
    return total

result=sum_list((1,2,3))
print(f"Sum of numbers in the list is {result}")
