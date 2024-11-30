def distinct_no(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2
print(distinct_no((1,2,2,3,4,2)))