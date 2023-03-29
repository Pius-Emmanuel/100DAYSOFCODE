# with open("./initial test.csv") as initial test:
#     data = initial test.readlines()
#     print(data)
#

# import csv
#
# with open("initial test.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for col in data:
#         if col[1] != "temp":
#             temperatures.append(int(col[1]))
#     print(temperatures)


import pandas as pd

# data = pd.read_csv("initial test.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])

# max_temps = data[data.day == max(data.temp)]
# max_temp = data[data.temp == data.temp.max()]
# print(max_temp)


# monday = data[data.day == "Monday"]
# print(monday.condition)
#
#
# monday = data[data.temp == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)



# Create a dataframe from scratch
data_dict = {
    "students": ["Amy","James", "Angela"],
    "Scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")