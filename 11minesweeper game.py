def is_valid(board, row, col, num):
  """
  Check if placing num in board[row][col] is valid.

  Args:
    board: A 9x9 Sudoku board.
    row: The row index.
    col: The column index.
    num: The number to place.

  Returns:
    True if placing num in board[row][col] is valid, False otherwise.
  """
  for i in range(9):
    if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
      return False
  return True

def solve_sudoku(board):
  """
  Solves a Sudoku board.

  Args:
    board: A 9x9 Sudoku board.

  Returns:
    True if the board is solved, False otherwise.
  """
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        for num in range(1, 10):
          if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
              return True
            board[row][col] = 0
        return False
  return True

# Example usage
board = [
  [3, 0, 0, 0, 0, 0, 0, 0, 4],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 7, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 4, 0, 0, 0, 0, 0, 3]
]

if solve_sudoku(board):
  print("Solved Sudoku:")
  for row in board:
    print(row)
else:
  print("Sudoku cannot be solved.")