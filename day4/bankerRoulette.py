"""
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.
"""

import random

test_seed = int(input("Created a seed number: "))
random.seed(test_seed)

names_string = input ("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
random_name = random.randint(0, num_items-1)

bills_on = names[random_name]
print(bills_on + " is going to buy the meal today!")