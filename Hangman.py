import random

print("Hangam")
print("---------------\n")

word_dictionary = [
    "sunflower",
    "apple",
    "Kitchenette",
    "Law",
    "Invest",
    "Jackpot",
    "Ship",
    "Significance",
    "Campus",
    "Carsick",
]

random_word = random.choice(word_dictionary)

for i in random_word:
    print("_", end=" ")


def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


def print_word(guessedletters):
    count = 0
    rightletters = 0
    for char in random_word:
        if char in guessedletters:
            print(random_word[count], end=" ")
            rightletters += 1

        else:
            print(" ", end=" ")
        count += 1
    return rightletters


def printLines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")


length_of_word_to_guess = len(random_word)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
    print("\nWord you guessed before: ")
    for letter in current_letters_guessed:
        print(letter, end=" \n")

    letterGuessed = input("\n=>Please guess new letter: ")

    if random_word[current_guess_index] == letterGuessed:
        print_hangman(amount_of_times_wrong)
        current_guess_index += 1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = print_word(current_letters_guessed)
        printLines()

    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = print_word(current_letters_guessed)
        printLines()

print("Game is over... Thank you for playing :)")
