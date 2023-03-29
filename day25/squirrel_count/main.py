 # figure out how many black, grey, and cinnamon colors are in the primary color
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

primary_color_counts = data['Primary Fur Color'].value_counts()

data_dictionary = {
    "Fur Color": ['Black', 'Gray', 'Cinnamon'],
    "count": [primary_color_counts['Black'], primary_color_counts['Gray'], primary_color_counts['Cinnamon']]
}
df = pd.DataFrame(data_dictionary)
df.to_csv("squirrel_count.csv")

