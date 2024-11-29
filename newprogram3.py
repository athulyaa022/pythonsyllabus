def check_number(num):
    if len(num)==10:
        if num[0] in ['9','8','7']:
            print(f"The mobile number {num} is a valid")
        else:
            print(f"The mobile number {num} is invalid ")
    else:
        print(f"The mobile number {num} is  invalid ")
number=input("Enter mobile number:")
check_number(number)