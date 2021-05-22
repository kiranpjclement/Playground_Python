"""
Welcome a user then ask them for a number between 1 and 1000.
When the user gives you the number, you check if it's odd or even and then you print a message letting them know.
Example:
Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?
"""

print("Welcome to my game! Please choose a number between 1 and 1000! Enter 'done' to exit")

while True:
    number = input("> ")
    if number=="no" or number=="done" or number=="exit" or number=="quit":
        print("Goodbye!")
        break
    try:
        numberint = int(number)
    except:
        print("This is not a number. Please give me a number!")
        continue
    if numberint<1 or numberint>1000:
        print("The number is outside the range 1--1000")
        continue
    if numberint%2==0:
        print("That's an even number! Have another? ")
        continue
    elif numberint%2!=0:
        print("That's an odd number! Have another?")
        continue
    else:
        break