import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# DONE 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

alphadict = {value.letter: value.code for key, value in alphabet.iterrows()}
print(alphadict)

# DONE 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_input = input('give me a word to convert: ')
    user_input_list = [word.capitalize() for word in user_input]
    try:
        output = [alphadict[letter] for letter in user_input_list]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        return
    else:
        print(output)


while True:
    generate_phonetic()


