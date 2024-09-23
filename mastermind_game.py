
import random

def mastermind_game():
    code = [random.randint(1, 6) for _ in range(4)]
    attempts = 10
    
    while attempts > 0:
        guess = list(map(int, input("Enter your 4-number guess (1-6): ").split()))
        if guess == code:
            print("You cracked the code!")
            return
        else:
            correct_pos = sum([1 for i in range(4) if guess[i] == code[i]])
            correct_color = len(set(guess) & set(code)) - correct_pos
            print(f"Correct position: {{correct_pos}}, Correct color but wrong position: {{correct_color}}")
        attempts -= 1
    print(f"Game Over! The correct code was {{code}}")

# Example
mastermind_game()
