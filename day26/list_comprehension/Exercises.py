#---------------------------------------------------------------
# CODE TEMPLATE
# result = [new_item for item in list]
# or
# result  = [new_item for item in list if test]  n.b this includes conditional statements
#---------------------------------------------------------------



#---------------------------------------------------------------
# EXERCISE 1: SQUARING NUMBERS
#---------------------------------------------------------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)


#---------------------------------------------------------------
# EXERCISE 2: FILTERING EVEN NUMBERS
#---------------------------------------------------------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num%2 == 0]
print(result)

#---------------------------------------------------------------
# EXERCISE 3: DATA OVERLAP
#---------------------------------------------------------------

with open("file1.txt") as file_1:
    file_1_data = file_1.readlines()

with open("file2.txt") as file_2:
    file_2_data = file_2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data ]
print(result)


