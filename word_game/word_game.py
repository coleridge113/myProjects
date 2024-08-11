import random

file = open('words.txt', 'r')
words_list = [x.rstrip() for x in file.readlines()]
print(words_list)

WORD = random.choice(words_list)
CORRECT_LETTERS = set(WORD)
GUESSED_LETTERS = set()
PLAYER_NAME = ''


def intro():
    print(f"\nHello {PLAYER_NAME}! Let's play a word-guessing game.")
    print("You can guess the letters of the word, and if you guess correctly, they will be displayed.\n")


def outro():
    print(f"\nThe word is '{WORD}'")
    print(f"Congratulations, {PLAYER_NAME}! You've completed the game.")


def display_word():
    for letter in WORD:
        if letter in GUESSED_LETTERS:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def validate_input(letter):
    if letter in WORD and len(letter) == 1:
        GUESSED_LETTERS.add(letter)
        print("Correct!")
    else:
        print("Wrong!")


if __name__ == "__main__":
    PLAYER_NAME = input("Before we start, write your name: ")
    intro()

    while CORRECT_LETTERS != GUESSED_LETTERS:
        display_word()
        print("\n")
        guess = input("Guess a letter: ")
        validate_input(guess)

    outro()


