#---------------------------------------------------------------
# CODE TEMPLATE
# new_dict = {new_key:new_value  for item in list}
# or
# new_dict  = {new_key:new_value for (key, value) in dict.items}  n.b based on the values in an existing dictionary
# new_dict  = {new_key:new_value for (key, value) in dict.items() if test}  n.b adding an if statement to the previous line
#---------------------------------------------------------------


import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

passed_students = {student: score for (student, score) in student_score.items() if score >= 40}
print(passed_students)