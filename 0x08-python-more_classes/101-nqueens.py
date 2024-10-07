#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""
import sys

# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col):
    # Check column conflicts
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Function to recursively solve the N Queens problem
def solve_nqueens(board, row, n):
    if row == n:
        # Once we place queens in all rows, we store the result
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # Backtrack

# Main program to handle input and print solutions
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize variables
    board = [-1] * N  # Track the column position of the queen in each row
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(board, 0, N)

    # Print each solution
    for solution in solutions:
        print(solution)
