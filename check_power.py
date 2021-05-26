"""1. Write a Python program to check if a given positive integer is a power of two.  
Input : 4, Output : True
2. Write a Python program to check if a given positive integer is a power of three.  
Input : 9, Output : True
3. Write a Python program to check if a given positive integer is a power of four.  
Input : 4, Output : True
4. Write a Python program to check if a number is a perfect square.  
Input : 9, Output : True
5. Write a Python program to check if an integer is the power of another integer. 
Input : 16, 2, Output : True
6. Write a Python program to check if a number is a power of a given base. 
Input : 128,2, Output : True"""

#The below code will work for exercises 1, 2, 3, 5.
inputnoint=int(input("What number you want to check? > "))
powernoint=int(input("You want to check if it's a power of > "))

resultslist=[]
for number in range(0, inputnoint):
    number=number+1
    resultpw=powernoint**number
    resultslist.append(resultpw)
    if resultpw>inputnoint:
        break

if inputnoint in resultslist:
    print(f"Yes, {inputnoint} is a power of {powernoint}.")
else:
    print(f"No, {inputnoint} is not a power of {powernoint}.")