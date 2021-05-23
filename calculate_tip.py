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

bill=float(input("What's the total bill for today, please? > "))

def aroundup(a):
    if a==int(a):
        return a
    else:
        return int(a)+1

print(f"18% tip is {bill*0.18}, which brings your total to {int(aroundup((bill*0.18)+bill))}.")
print(f"20% tip is {bill*0.20}, which brings your total to {int(aroundup((bill*0.20)+bill))}.")
print(f"25% tip is {bill*0.25}, which brings your total to {int(aroundup((bill*0.25)+bill))}.")

no_people=int(input("\nHow many people are involved? > "))
print("If split evenly:")
print(f"18% tip is {bill*0.18/no_people}/each, which brings your total to {int(aroundup((bill+(bill*0.18))/no_people))}/each.")
print("If split 30% and 70%:")
print(f"18% tip for the 1st person is {bill*0.18*0.3}, which brings the total to {aroundup((bill+(0.18*bill))*0.3)}.")
print(f"18% tip for the 2nd person is {bill*0.18*0.7}, which brings the total to {aroundup((bill+(0.18*bill))*0.7)}.")