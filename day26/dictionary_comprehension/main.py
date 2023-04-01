#---------------------------------------------------------------
# CODE TEMPLATE
# new_dict = {new_key:new_value  for item in list}
# or
# new_dict  = {new_key:new_value for (key, value) in dict.items()}  n.b based on the values in an existing dictionary
# new_dict  = {new_key:new_value for (key, value) in dict.items() if test}  n.b adding an if statement to the previous line
#---------------------------------------------------------------


#---------------------------------------------------------------
# EXERCISE 1:Dictionary comprehension 1
#---------------------------------------------------------------
# You are going to use Dictionary Comprehension to create a
# dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
#---------------------------------------------------------------
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)
print("\n=======================================================================================================")





#---------------------------------------------------------------
# EXERCISE 2:Dictionary comprehension 2
#---------------------------------------------------------------
# You are going to use Dictionary Comprehension to create a dictionary
# called weather_f that takes each temperature in degrees Celsius and
# converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
#---------------------------------------------------------------
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f =  {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
print("\n=======================================================================================================")




#---------------------------------------------------------------
# ITERATING OVER A PANDAS DATAFRAME
#---------------------------------------------------------------
student_dict = {
    "student": ["Emmanuel", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)
print("\n=======================================================================================================")

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
print("\n=======================================================================================================")


#Loop through  a dataframe
for (key, value) in student_data_frame.items():
    print(value)
print("\n=======================================================================================================")

# loop
