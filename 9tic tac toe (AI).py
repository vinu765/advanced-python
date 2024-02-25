def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[current_player]
        row, col = map(int, input("Player {} enter row and column numbers (1-3): ".format(player)).split())

        if row < 1 or row > 3 or col < 1 or col > 3 or board[row-1][col-1] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row-1][col-1] = player
        print_board(board)

        if check_winner(board, player):
            print("Player {} wins!".format(player))
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()