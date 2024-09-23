
def twenty_one_game():
    player_total = 0
    print("Try to reach 21 without going over!")
    
    while player_total < 21:
        num = int(input("Add a number (1-10): "))
        if 1 <= num <= 10:
            player_total += num
            print(f"Current total: {{player_total}}")
        else:
            print("Number must be between 1 and 10.")
        
        if player_total == 21:
            print("Congratulations! You've hit 21.")
        elif player_total > 21:
            print("You've gone over 21! Game over.")
            break

# Example
twenty_one_game()
