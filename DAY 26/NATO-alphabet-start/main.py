import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("C:/Users/HP-PC/Desktop/100DOC/Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = (input("Enter any word?  ")).upper()

nato_word = [nato_dict[row] for row in user_input if row in user_input]

print (nato_word)