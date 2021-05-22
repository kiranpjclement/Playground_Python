"""
Calculate the tip
Your goal is to find out exactly how much tip you should give after receiving a service.
In this scenario, ask for the total bill. Then display the tip for 18%, 20% and 25%.
Example:
Prompt: what's the total bill for today, please?
Input: $55.87
Output: 18% tip is $10.06, which brings your total to $65.93
Remember you want to be nice, so don't forget to round up. To push this more,
 ask for the number of people involved, then evenly split the tip and total cost among them.
To go even a step further, split unevenly
(for example, one person pays 70% of the bill while the other pays 30%)
"""

print("What's the total bill for today, please?")
bill=input("> ")
try:
    bill_float=float(bill)
except:
    print("Please enter the bill value as a number!")
#print(f"The bill value is: {bill_float}")

def aroundup(a):
    if a==int(a):
        return a
    else:
        return int(a)+1

#the following 3 lines will show a float sometimes(when there is nothing to roundup)
print(f"18% tip is {bill_float*0.18}, which brings your total to {int(aroundup((bill_float*0.18)+bill_float))}.")
print(f"20% tip is {bill_float*0.20}, which brings your total to {int(aroundup((bill_float*0.20)+bill_float))}.")
print(f"25% tip is {bill_float*0.25}, which brings your total to {int(aroundup((bill_float*0.25)+bill_float))}.")

no_people=input("How many people are involved? \n>")
no_people=int(no_people)
print("If splitted evenly:")
print(f"18% tip is {bill_float*0.18/no_people}/each, which brings your total to {int(aroundup((bill_float+(bill_float*0.18))/no_people))}/each.")
print("If spliteed 30% and 70%:")
print(f"18% tip for the 1st person is {bill_float*0.18*0.3}, which brings your total to {aroundup((bill_float+(0.18*bill_float))*0.3)}.")
print(f"18% tip for the 2nd person is {bill_float*0.18*0.7}, which brings your total to {aroundup((bill_float+(0.18*bill_float))*0.7)}.")