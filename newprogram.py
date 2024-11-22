'''
Author Name: Athulya A
Date: 22-11-2024
Description: Input two list from the user. Merge these lists into a third list such that in the merged list, all even
numbers occurs first followed by odd number. Both the even number and odd number be in sorted order.
'''
list1=[1,5,3,2,4]
list2=[22,14,23,4,10]
print("First list:",list1)
print("Second list:",list2)
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("Merged list:",merged_list)