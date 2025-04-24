import random
import time

# Dice faces for visual flair
dice_faces = {
    1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
}

# Function to roll a dice
def dice():
    return random.randint(1, 6)

# Function to get valid input between 1 and 6
def get_valid_input(player):
    while True:
        try:
            num = int(input(f"{player}, how many times do you want to roll the dice (1-6): "))
            if 1 <= num <= 6:
                return num
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

# Function for a single player's turn
def player_turn(player_name, rolls):
    rolls_list = []
    for i in range(rolls):
        input(f"{player_name}, press Enter to roll the dice... ")
        time.sleep(0.5)
        result = dice()
        rolls_list.append(result)
        print(f"{player_name} rolled a {result} {dice_faces[result]}")
    return rolls_list

# Main game loop
def play_game():
    player_1_score = 0
    player_2_score = 0
    round_num = 1

    while True:
        print(f"\n--- ROUND {round_num} ---")

        rolls = get_valid_input("Player 1")
        player1_rolls = player_turn("Player 1", rolls)
        player1_total = sum(player1_rolls)

        print()

        rolls = get_valid_input("Player 2")
        player2_rolls = player_turn("Player 2", rolls)
        player2_total = sum(player2_rolls)

        print(f"\nPlayer 1 rolled: {player1_rolls} | Total: {player1_total}")
        print(f"Player 2 rolled: {player2_rolls} | Total: {player2_total}")

        if player1_total > player2_total:
            print("Player 1 wins this round!")
            player_1_score += 1
        elif player2_total > player1_total:
            print("Player 2 wins this round!")
            player_2_score += 1
        else:
            print("This round is a draw!")

        print(f"\nCurrent Score => Player 1: {player_1_score} | Player 2: {player_2_score}")

        again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if again != 'y':
            break

        round_num += 1

    # Final results
    print("\n=== FINAL RESULTS ===")
    print(f"Player 1 Score: {player_1_score}")
    print(f"Player 2 Score: {player_2_score}")

    if player_1_score > player_2_score:
        print("🏆 Player 1 is the overall winner!")
    elif player_2_score > player_1_score:
        print("🏆 Player 2 is the overall winner!")
    else:
        print("It's a draw overall!")

# Start the game
play_game()
