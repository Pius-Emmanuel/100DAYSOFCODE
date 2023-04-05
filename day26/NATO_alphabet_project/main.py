import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
new_df = {row.letter: row.code for (index, row ) in nato_df.iterrows()}
print(new_df)
word = input("Enter a word: ").upper()
output_list = [new_df[letter] for letter in word]
print(output_list)
