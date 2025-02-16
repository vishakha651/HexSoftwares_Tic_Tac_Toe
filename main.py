# Tic-Tac-Toe Game in Python

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Checks if the board is full (draw condition)."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column: 0 1 or 2 2): ").split())
            if board[row][col] == " ":
                board[row][col] = player
                print_board(board)

                if check_winner(board, player):
                    print(f"Player {player} wins!")
                    break
                if is_full(board):
                    print("It's a draw!")
                    break

                turn += 1
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 0 and 2.")

# Run the game
tic_tac_toe()