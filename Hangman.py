import random

def choose():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango"]
    return random.choice(words)

def display(word, guessed):
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def draw(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
        ,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """
        ,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """
        ,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """
        ,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """
        ,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """
        ,
               
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """
    ]
    return stages[tries]

def play():
    word = choose()
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 tries.")

    while tries > 0:
        print(draw(6 - tries))
        print("\n" + display(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

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
                print(draw(6 - tries))
                print("Sorry, you ran out of tries. The word was '{}'.".format(word))
                break
        else:
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word '{}'!".format(word))
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play()
    else:
        print("Thanks for playing!")

play()


