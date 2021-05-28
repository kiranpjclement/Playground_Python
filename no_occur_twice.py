"""12. Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5   """


inputlist=[5, 3, 4, 3, 4]
print(f"The input list is: {inputlist}")
resultlist=[]
"""
for i in inputlist:
    #print(i)
    indx=inputlist.index(i)
    print(id(inputlist[indx]))
    popul=inputlist.pop(indx)
    print(popul)
    #print(indx)
    #bbb=inputlist[indx]
    #print(bbb)
    #popul=inputlist.pop(indx)
    #print(popul)
    #bbb=inputlist[indx]
    #print(bbb)
    resultlist.append(popul)
    #print(i)
    #i=i+1

print(resultlist)
print(inputlist)

for j in inputlist:
    inputlist.pop()
    print(inputlist)

print(inputlist)
"""
for i in range(0,len(inputlist)):
    #print(i)
    each_no=inputlist[i]
    print(each_no)
    current_no=inputlist.pop(i)
    print(current_no)
    print(inputlist)
    if current_no in inputlist:
        print(f"{current_no} is twice")
        continue
    else:
        resultlist.append(current_no)

print(inputlist)
print(f" these numbers are only once: {resultlist}")