
import random

def word_guessing_game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    
    while attempts > 0:
        print(guessed)
        guess = input("Guess a letter: ")
        if guess in word:
            guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
        else:
            attempts -= 1
            print(f"Incorrect! Attempts left: {{attempts}}")
        if guessed == word:
            print("You guessed the word!")
            break

# Example
word_guessing_game()
