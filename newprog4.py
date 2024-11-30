def reverse_string(str):
    new_str=""
    str_index=len(str)
    while str_index>0:
        new_str+=str[str_index-1]
        str_index=str_index-1
    return new_str
str=input("Enter a string:")
result=reverse_string(str)
print(f"The reversed string is {result}")




