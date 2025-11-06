import random

# Define snakes and ladders
snakes = {
    99: 54, 70: 55, 52: 42, 25: 2, 95: 72
}
ladders = {
    6: 25, 11: 40, 60: 85, 46: 90, 17: 69
}

# Player positions
player_positions = {"Player 1": 0, "Player 2": 0}

def roll_dice():
    return random.randint(1, 6)

def move_player(player):
    dice = roll_dice()
    print(f"\n{player} rolled a {dice}")

    pos = player_positions[player] + dice
    if pos > 100:
        print(f"{player} needs an exact roll to finish!")
        return

    if pos in snakes:
        print(f"Oh no! {player} got bitten by a snake 🐍 from {pos} to {snakes[pos]}")
        pos = snakes[pos]
    elif pos in ladders:
        print(f"Yay! {player} climbed a ladder 🪜 from {pos} to {ladders[pos]}")
        pos = ladders[pos]
    else:
        print(f"{player} moved to {pos}")

    player_positions[player] = pos

    if pos == 100:
        print(f"\n🎉 {player} wins the game! 🎉")
        return True
    return False

def play_game():
    print("🎲 Welcome to Snakes and Ladders 🎲")
    print("----------------------------------")

    while True:
        for player in player_positions:
            input(f"\n{player}, press Enter to roll the dice...")
            if move_player(player):
                return

if __name__ == "__main__":
    play_game()

