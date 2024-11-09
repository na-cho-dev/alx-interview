#!/usr/bin/python3
"""
This contains the N queens challemge function
"""
import sys


def main():
    """
    This functions solves the  N queens puzzle challenge
    by placing N non-attacking queens on an N×N chessboard

    Usage: nqueens N
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if arg < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = [[0] * arg for _ in range(arg)]
    column_set = set()
    pri_diag_set = set()
    sec_diag_set = set()
    row = 0

    place_queen(chess_board, arg, row, column_set,
                pri_diag_set, sec_diag_set)


def place_queen(board, n, row, column_set, pri_diag_set, sec_diag_set):
    """
    Recursive function for placing Queens

    args:
        board: An 2d array for the chess board
        n: n number of rows, cols, and queens
        row: Row index of board
        column_set: Set containing occupied col
        pri_diag_set: Set containg pri_diag_set occupied cells
        sec_diag_set: Set containg sec_diag_set occupied cells
    """
    # Obviously checks the base case, but I need to still comment :)
    check_base_case(board, row, n)

    for col in range(n):
        if is_safe(row, col, column_set, pri_diag_set, sec_diag_set):
            # Place Queen by assigning cell to 1 and remians 0 id empty
            board[row][col] = 1
            # Keeps track of cells index to avoid each Queen attacking another
            column_set.add(col)
            pri_diag_set.add(row - col)
            sec_diag_set.add(row + col)

            # Recur to the next row
            place_queen(board, n, row + 1, column_set,
                        pri_diag_set, sec_diag_set)

            # Backtrack
            board[row][col] = 0
            column_set.remove(col)
            pri_diag_set.remove(row - col)
            sec_diag_set.remove(row + col)


def check_base_case(board, row, n):
    """
    Checks the base case of `place_queen` function

    args:
        board: An 2d array for the chess board
        n: n number of rows, cols, and queens
        row: Row index of board
    """
    if row == n:
        # Base case: if row equals n, all queens are placed successfully
        result = []
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    result.append([r, c])
        print(result)
        return


def is_safe(row, col, column_set, pri_diag_set, sec_diag_set):
    """sec_diag_set
    Checks if the placed queen is safe
    args:
        row: Row index
        col: Column index
        column_set: Set containing occupied col
        pri_diag_set: Set containg pri_diag_set occupied cells
        sec_diag_set: Set containg sec_diag_set occupied cells
    """
    # Check if column is already occupied
    if col in column_set:
        return False

    # Check if primary diagonal is already occupied
    if (row - col) in pri_diag_set:
        return False

    # Check if secondary diagonal is already occupied
    if (row + col) in sec_diag_set:
        return False

    return True


if __name__ == "__main__":
    main()
