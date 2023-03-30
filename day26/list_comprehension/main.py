#---------------------------------------------------------------
# FOR LOOP
#---------------------------------------------------------------
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#---------------------------------------------------------------
# COMPREHENSION LIST
#---------------------------------------------------------------
new_list = [n + 1 for n in numbers]

#---------------------------------------------------------------
# STRING LIST
#---------------------------------------------------------------
name = "Emmanuel"
letters_list = [letter for letter in name]

#---------------------------------------------------------------
# RANGE AS LIST
#---------------------------------------------------------------
range_list = [n * 2 for n in range (1,5)]

#---------------------------------------------------------------
# CONDITIONAL LIST COMPREHENSION
#---------------------------------------------------------------

names =["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names_with_uppercase = [name.upper() for name in names if len(name) > 5]
print(long_names_with_uppercase)
