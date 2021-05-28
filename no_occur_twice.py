"""12. Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5   """


list1=[5, 3, 4, 3, 4]
list2=list1
ouputlist=[]

for i in list1:
    k=0
    for j in list2:
        if i ==j:
            k=k+1
    if k<2:
        oplist.append(i)
print(oplist)
