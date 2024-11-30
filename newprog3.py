def product_num(num):
    product=1
    for i in num:
        product=product*i
    return product

result=product_num((3,4,5))
print(f"Product of numbers in the list is {result}")