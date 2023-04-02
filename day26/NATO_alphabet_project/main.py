import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
new_df = {row.letter: row.code for (index, row ) in nato_df.iterrows()}
print(new_df)
