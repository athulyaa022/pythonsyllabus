def count(str):
    lower_count=0
    upper_count=0
    for i in str:
        if i.islower():
            lower_count+=1
        elif i.isupper():
            upper_count+=1
    return(lower_count,upper_count)
str=input("Enter a string:")
result=count(str)
lower_case,upper_case=result
print("The no of lowercase characters is",lower_case)
print("The no of uppercase characters is",upper_case)