
import random

def hangman_game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    wrong_guesses = []

    while attempts > 0:
        print(f"Word: {{guessed}}")
        print(f"Wrong guesses: {{', '.join(wrong_guesses)}}")
        guess = input("Guess a letter: ").lower()

        if guess in word:
            guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
        else:
            wrong_guesses.append(guess)
            attempts -= 1

        if guessed == word:
            print(f"Congratulations, you guessed the word: {{word}}")
            break
        if attempts == 0:
            print(f"Game Over! The word was {{word}}.")

# Example
hangman_game()
