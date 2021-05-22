"""
Welcome a user then ask them for a number between 1 and 1000.
When the user gives you the number, you check if it's odd or even and then you print a message letting them know.
Example:
Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?
"""
number = input("Welcome to my game. Please choose a number between 1 and 1000: >")

#def num():
    #number = input("Welcome to my game. Please choose a number between 1 and 1000: >")

while True:
    try:
        numberint = int(number)
    except:
        print("This is not a number. Please give me a number!")
    if numberint%2==0:
        print("That's an even number! Have another?")

    elif numberint%2!=0:
        print("That's an odd number! Have another?")

    else:
        break
