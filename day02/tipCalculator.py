"""
if the bill was $150.00 split between 5 people, with 12% tip.
Each persons should pay (150.00 / 5) *1.12
Round the numbers to two decimal place = 33.60
"""
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total Bill? $"))
percentage_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))


tip = (percentage_tip/100) * total_bill
bill_plus_tip = tip + total_bill
each_pays = round(bill_plus_tip/ num_of_people, 2)
final_amount = "{:.2f}".format(each_pays)
print(f"Each person should pay: ${final_amount}")