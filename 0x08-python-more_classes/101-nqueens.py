#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a specific position."""
    # Check the row
    if 'Q' in board[row]:
        return False

    # Check the column
    if 'Q' in [board[i][col] for i in range(n)]:
        return False

    # Check upper-left diagonal
    a = 'Q'
    list_1 = range(row, -1, -1)
    list_2 = range(col, -1, -1)
    if a in [board[i][j] for i, j in zip(list_1, list_2)]:
        return False

    # Check upper-right diagonal
    if 'Q' in [board[i][j] for i, j in zip(range(row, -1, -1), range(col, n))]:
        return False

    return True


def solve_nqueens(n):
    """Solve the N-queens puzzle."""
    def recursive_solve(board, row):
        if row == n:
            solutions.append([row[:] for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                recursive_solve(board, row + 1)
                board[row][col] = ' '

    solutions = []
    board = init_board(n)
    recursive_solve(board, 0)
    return solutions


if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for sol in solutions:
        for row in sol:
            print(' '.join(row))
        print()
