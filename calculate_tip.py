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
print(f"The bill value is: {bill_float}")

tip18=bill_float*0.18
#tip20=
#tip25=

print(f"18% tip is {tip18}, which brings your total to {bill_float+tip18}")

