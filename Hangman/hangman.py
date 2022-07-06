import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():

    word = get_valid_word(words)
    word_letters = set(word.upper())
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word.upper()]
        print("Current word: ", ''.join(word_list))

        guess = input("Guess a letter: ").upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
        elif guess in used_letters:
            print("You already guessed that letter")
        else:
            print("Invalid character")

hangman()