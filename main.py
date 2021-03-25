import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row[0]:row[1] for (index, row) in data.iterrows()}

def run():
    input_word = input("Type in the word: \n").upper()
    try:
        answer = [data_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry alphabets only")
        run()
    else:
        print(answer)

run()

