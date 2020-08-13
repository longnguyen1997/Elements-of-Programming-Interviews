from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    placements = []

    def queen_helper(row_i, placement=[0] * n):
        if row_i == n:
            placements.append(placement.copy())
            return placements
        for position in range(n):
            if all(placement[i] != position
                   and abs(row_i - i) != abs(position - placement[i])
                   for i in range(row_i)):
                placement[row_i] = position
                queen_helper(row_i + 1, placement)
        return placements

    return queen_helper(0)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
