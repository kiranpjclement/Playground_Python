"""
7. Write a Python program to find a missing number from a list. Go to the editor
Input : [1,2,3,4,6,7,8]
Output : 5

8. Write a Python program to find missing numbers from a list. Go to the editor
Input : [1,2,3,4,6,7,10]
Output : [5, 8, 9]
"""

"""
input=[1,2,3,4,6,7,8]
#print(input)
list2=[]
for l in range(1, 9):
    list2.append(l)
#print(list2)
for a in list2:
    if a in list2 and a not in input:
        print(a)
"""

input=[1,2,3,4,6,7,10]
list2=[]
for l in range(1, 11):
    list2.append(l)
print(list2)
output=[]
for a in list2:
    if a in list2 and a not in input:
        output.append(a)

print(output)