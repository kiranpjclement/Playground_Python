"""
You ask a user to guess a number between 1 and 50.
If they guess outside that range, you prompt with an error
encouraging them to choose a number within the proper range.
Whenever they guess the wrong number you ask if they want
to keep playing or if they'd like to quit.
Finally, when the user eventually guesses the right number
 you congratulate them and show the number of attempts they had.
"""

import random
n=random.randint(1,50)
#print(f"the random number is : {n}")
print("Please guess a number between 1 and 50!")
count=0

while True:
    number = input("> ")
    count=count+1
    if number=="keep playing":
        continue
    elif number=="quit":
        break
    try:
        numberint=int(number)
    except:
        print("Error, this is not a number!")
        continue
    if numberint<1 or numberint>50:
        print("Error, please choose a number within the 1-50 range!")
        continue
    if numberint !=n:
        print("You've guessed the wrong number!")
        print("Do you want to keep playing or would you like to quit?")
        print("Enter 'keep playing' , 'quit', or a number.")
        continue
    elif numberint==n:
        print("Congratulations! You've guessed the number!")
        print(f"You had {count} attempts.")
        break
    else:
        break
