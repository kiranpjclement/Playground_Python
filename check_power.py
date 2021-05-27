"""1. Write a Python program to check if a given positive integer is a power of two.  
Input : 4, Output : True
2. Write a Python program to check if a given positive integer is a power of three.  
Input : 9, Output : True
3. Write a Python program to check if a given positive integer is a power of four.  
Input : 4, Output : True
5. Write a Python program to check if an integer is the power of another integer. 
Input : 16, 2, Output : True
6. Write a Python program to check if a number is a power of a given base. 
Input : 128,2, Output : True"""

#The below code will work for exercises 1, 2, 3, 5, 6.
inputnoint=int(input("What number you want to check? > "))
powernoint=int(input("You want to check if it's a power of > "))

def powercheck():
    resultslist = []
    for number in range(0, inputnoint):
        number=number+1
        resultpw=powernoint**number
        resultslist.append(resultpw)
        if resultpw > inputnoint:
            break
    #print(resultslist)
    print(inputnoint in resultslist)
powercheck()