import random

def generate_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines_placed = 0
    while mines_placed < num_mines:
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        if board[x][y] != '*':
            board[x][y] = '*'
            mines_placed += 1
    return board

def print_board(board):
    size = len(board)
    print("   " + "  ".join(str(i) for i in range(size)))
    print("  " + "+---" * size + "+")
    for i in range(size):
        print(str(i) + " | " + " | ".join(board[i]) + " |")
        print("  " + "+---" * size + "+")

def count_adjacent_mines(board, x, y):
    count = 0
    size = len(board)
    for i in range(max(0, x-1), min(size, x+2)):
        for j in range(max(0, y-1), min(size, y+2)):
            if board[i][j] == '*':
                count += 1
    return count

def reveal_cells(board, x, y, revealed):
    size = len(board)
    if revealed[x][y]:
        return
    revealed[x][y] = True
    if board[x][y] != ' ':
        return
    for i in range(max(0, x-1), min(size, x+2)):
        for j in range(max(0, y-1), min(size, y+2)):
            reveal_cells(board, i, j, revealed)

def play_game(size, num_mines):
    board = generate_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    while True:
        print_board([[' ' if not revealed[i][j] else board[i][j] for j in range(size)] for i in range(size)])
        x, y = map(int, input("Enter row and column (separated by space): ").split())
        if board[x][y] == '*':
            print("Game over! You hit a mine.")
            break
        reveal_cells(board, x, y, revealed)
        if all(revealed[i][j] or board[i][j] == '*' for i in range(size) for j in range(size)):
            print_board(board)
            print("Congratulations! You win!")
            break

if __name__ == "__main__":
    size = int(input("Enter the size of the board: "))
    num_mines = int(input("Enter the number of mines: "))
    play_game(size, num_mines)