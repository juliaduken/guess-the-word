import random

# Load Words
def load_words(filename="words.txt"):
    with open(filename, "r") as file:
        words = [line.strip().upper() for line in file.readlines()]
    return words
WORD_LIST = load_words()

# Select Secret Word
SECRET_WORD = random.choice(WORD_LIST).upper()