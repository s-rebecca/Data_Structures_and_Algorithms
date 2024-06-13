def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    if col == n:
        # Found a solution, add a copy of the board to the solutions list
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


def print_board(board):
    for row in board:
        print(" ".join(["Q" if col == 1 else "." for col in row]))
    print()


# Test the algorithm for minimum n=4 and maximum n=8
for n in range(4, 9):
    solutions = solve_n_queens(n)
    print(f"Solutions for N={n}:")
    for i in range(min(3, len(solutions))):
        print(f"Solution {i + 1}:")
        print_board(solutions[i])
