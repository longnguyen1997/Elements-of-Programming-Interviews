from typing import List

from test_framework import generic_test
from collections import Counter


def get_row(M, x, y):
    return [M[x][y] for y in range(9) if M[x][y] > 0]


def get_column(M, x, y):
    return [row[y] for row in M if row[y] > 0]


def get_subgrid(M, x, y):
    r = (x // 3) * 3
    c = (y // 3) * 3
    return [M[i][j] for i in range(r, r + 3)
            for j in range(c, c + 3) if M[i][j] > 0]


def validate(m):
    return len(m) == len(set(m))


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    M = partial_assignment
    for i in range(9):
        for j in range(9):
            if M[i][j] == 0:
                continue
            R = get_row(M, i, j)
            C = get_column(M, i, j)
            S = get_subgrid(M, i, j)
            if not all((validate(R), validate(C), validate(S))):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
