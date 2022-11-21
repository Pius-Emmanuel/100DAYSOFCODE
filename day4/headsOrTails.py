"""
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
"""

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

heads_tails = random.randint(0,1)

if heads_tails ==0:
    print("Tails")
else: 
    print("Heads")