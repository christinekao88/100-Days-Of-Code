#TODO 1. Create a dictionary in this format:

import pandas as pd
data= pd.read_csv(r"100 days\Day_26_NATO-alphabet\nato_phonetic_alphabet.csv")
print (data.to_dict())

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word : ").upper()

name_list = [phonetic_dict[letter] for letter in word ]

print(name_list)