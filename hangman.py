# HANGMAN
# Created by Stevie Barker
# Jetbrains Tutorial 

# Import modules
import random

# Title
print("H A N G M A N")


# Chooses answer randomly from list, stores in answer
# Initializes word
word_list = ["python", "java", "kotlin", "javascript", "ruby", "html"]
word = word_list[(random.randint(0, (len(word_list)-1)))]
letters_needed = []


# Creates max number of attempts, and lists choices
attempts = 8
choices = []
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Creates list of needed letters & counter variable
for letter in word:
    while letter not in letters_needed:
        letters_needed.append(letter)
    letters_missing = len(letters_needed)

# User Menu Prompt

menu_choice = input("Type 'play' to play the game, 'exit' to quit : ")
if menu_choice == "exit":
    exit  # Quits Program
if menu_choice == "play":
    print()  # Line Break
     
# Prints '-' or letter for each letter in word
    while attempts > 0:
        print()
        for letter in word:
            if letter in choices:
                print(letter, sep='', end='')
            else:
                print('-', sep='', end='')
        print()  # Line Break

# Accepts choice as input, records in program
        choice = input("Input a letter: ")
        if choice not in ALPHABET:
            if len(choice) > 1:
                print("You should input a single letter")
            else:
                print("It is not an ASCII lowercase letter")
        elif choice in choices:
            print("You already typed this letter")
        else:
            if choice in letters_needed:
                choices.append(choice)
                letters_missing -= 1
            else:
                print("No such letter in the word")
                choices.append(choice)
                attempts -= 1
                
# End Conditions and Output
    else:
        if letters_missing == 0:
            print(word)
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")

