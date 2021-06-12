import pandas

word = input("Please enter a word : ").upper()
nato = pandas.read_csv("Ressources/nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}
dict_letter = [nato_dict[letter] for letter in word]

print(dict_letter)
