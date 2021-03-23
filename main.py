#TODO 1. Create a dictionary in this format:
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row[0]:row[1] for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Type in the word: \n").upper()
answer = [data_dict[letter] for letter in input_word]
print(answer)


