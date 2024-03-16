import random

def choose():
    words = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Kiwi", "Lemon", "Mango"]
    return random.choice(words)

def display(word, guessed):
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose()
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 tries.")

    while tries > 0:
        print("\n" + display(word, guessed_letters))
        guess = input("Enter a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect! You have {} tries left.".format(tries))
            if tries == 0:
                print("Sorry, you ran out of tries. The word was '{}'.".format(word))
                break
        else:
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word '{}'!".format(word))
                break

hangman()
