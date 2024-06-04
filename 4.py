# 4.Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem.

def branch_and_bound(n):
    def is_safe(board, row, col):
        # Check if a queen can be placed at board[row][col]
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve_nqueens(board, row):
        if row == n:
            # All queens are placed, print the solution
            print([[i, board[i]] for i in range(n)])
            return True

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1)
                # Backtrack
                board[row] = -1

    board = [-1] * n
    solve_nqueens(board, 0)

# Backtracking
def backtracking(n):
    def is_safe(board, row, col):
        # Check if a queen can be placed at board[row][col]
        for i in range(row):
            if board[i][col] == 1 or any(board[i][j] == 1 and abs(i - row) == abs(j - col) for j in range(n)):
                return False
        return True

    def solve_nqueens(board, row):
        if row == n:
            # All queens are placed, print the solution
            for row in board:
                print(row)
            print()
            return True

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve_nqueens(board, row + 1)
                # Backtrack
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    solve_nqueens(board, 0)

# Test the implementations
n = 4
print("Branch and Bound:")
branch_and_bound(n)
print("\nBacktracking:")
backtracking(n)

