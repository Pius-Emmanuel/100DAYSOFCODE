"""Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
"""

two_digit_number = input("Type a two digit number: ")
first = two_digit_number[0]
second = two_digit_number[1]

sum_up = int(first) + int(second)
print(sum_up)

