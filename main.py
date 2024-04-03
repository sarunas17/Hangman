# Scaled Down Task (maximum score : 7-8):

# Task:
# Create a Hangman Game (terminal version). https://www.youtube.com/watch?v=leW9ZotUVYo

# - Maximum guess attempts: 10.

# - Ability to guess a word or a letter. If a guess is incorrect, user loses 1 life.

# - If user has 0 guesses (lifes) left, game is lost.

# - Ability to guess the word !!

# REQUIREMENTS: 
# ● Create a new GITHUB project, virtual env, README, .gitignore, etc.

# ● Use python functions and/or classes to achieve necessary functionality.

# ● Possible words should be held in a list data structure.

# ● Use type annotations.

# ● Use `print` or logging library to log out information.



# Full task (maximum score 10):

# Create a Hangman Game (GUI/terminal version). https://www.youtube.com/watch?v=leW9ZotUVYo

# - Maximum guess attempts: 10.

# - Ability to guess a word or a letter. If a guess is incorrect, user loses 1 life.

# - If user has 0 guesses (lifes) left, game is lost. (Give options to see all time results or start new game)

# REQUIREMENTS: 
# ● Create a new GITHUB project, virtual env, README, .gitignore, etc.

# ● Use OOP structures (classes, inheritance, dataclasses, modules) to construct game backend logic.

# ● For a front end part you can use CLI, but Flask applicaton is preferible. 

# ● Create user registration (name,surname, email),store it using SQL database.

# ● Use Mongo DB to store all necessary game data data.

# ● At least one of the system part (front-end/back end) should be dockerized.

# ● Use type annotations, error handling thoughout the code.

# ● Use a logging library to log out information (terminal and files).

# ● Unit tests to cover most important functionality.

# ● After the game session, show a table with user information: games played today , games won/lost today, guesses made.
 
# Nice to have:
#  - All system parts should be dockerized
#  - Shell script to run the program automatically
#  - Show TOP 10 performances of all accounts (create a button to see that table from game panel) 
#  - music sounds on good/bad guesses.

import random

game_words = ["sanctuary", "hostility", "hot", "provincial", "knot", "blackmail", "cap", "preparation", "inspiration", "museum", "finger", "regular", "waist", "marketing", "grip", "elapse", "rotate", "court", "sequence"]


class Hangman:
    def __init__(self):
        self.word_to_guess = random.choice(game_words)
        self.max_guesses = 10
        self.incorrect_guesses = 0

    def display_word(self):
        word_to_guess_length = len(self.word_to_guess)
        guessed_letters_display = ['_'] * word_to_guess_length
        display_string = ' '.join(guessed_letters_display)
        print(display_string)
        return self.word_to_guess

    def prompt_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Please enter a single letter.")

hangman_game = Hangman()
word_to_guess = hangman_game.display_word()
print("Word to guess:", word_to_guess)

guess = hangman_game.prompt_guess()
print("Your guess:", guess)

