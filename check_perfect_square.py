"""4. Write a Python program to check if a number is a perfect square.
Input : 9, Output : True
"""

thenumber=int(input("What number you want to check? > "))

def square(n):
    #n=0
    while n<thenumber:
        n=n+1
        x=n*n
        #print(x)
        if x==thenumber:
            #print(x==thenumber)
            break
        else:
            #print(x==thenumber)
            continue

    print(x == thenumber)

square(0)
