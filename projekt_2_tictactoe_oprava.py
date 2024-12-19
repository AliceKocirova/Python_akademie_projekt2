
"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: Alice Kočířová
email: a.kocirova@gmail.com
"""



# Creating a playing field
BOARD_SIZE = 9
board = [" " for _ in range(BOARD_SIZE)]
current_player = "O"

# Display the playing field
def display_board():
    print("+---+---+---+")
    for i in range(3):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print("+---+---+---+")


# Victory check
def check_winner():
    winning_combinations = [
        # Horizontally
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Vertically
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonally
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[i] == current_player for i in combo):
            return True
    return False

# Draw game
def is_draw():
    return all(cell != " " for cell in board)

# Another player
def switch_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"

# Player turn
def process_turn():
    while True:
        position = input(f"Player {current_player} | Please enter your move number (1-9): ")
        if not position.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        position = int(position) - 1
        if position < 0 or position >= BOARD_SIZE:
            print("Out of range. Please choose a number between 1 and 9.")
            continue

        if board[position] != " ":
            print("Position already taken. Choose another field.")
            continue

        board[position] = current_player
        break


def play_game():
    print("\n".join([
        "Welcome to Tic Tac Toe",
        "=" * 40,
        "GAME RULES:",
        "Each player can place one mark (or stone) per turn on the 3x3 grid.",
        "The WINNER is the player who succeeds in placing three of their marks",
        "in a horizontal, vertical, or diagonal row.",
        "=" * 40,
        "Let´s start the game"
    ]))

    while True:
        print("=" * 40)
        # Displaying the state of the playing field
        display_board()
        process_turn()

        if check_winner():
            print("=" * 40)
            display_board()
            print(f"Congratulations, the player {current_player} WON!")
            print("=" * 40)
            break

        if is_draw():
            print("=" * 40)
            display_board()
            print("It’s a draw! Well played both players.")
            print("=" * 40)
            break

        switch_player()

# Game
if __name__ == "__main__":
    play_game()
