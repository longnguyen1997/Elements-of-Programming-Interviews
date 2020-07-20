from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if not square_matrix:
        return []
    n = len(square_matrix)
    spiral_order = []
    for j in range(n):
        spiral_order.append(square_matrix[0][j])
    for i in range(1, n):
        spiral_order.append(square_matrix[i][n - 1])
    for j in reversed(range(n - 1)):
        spiral_order.append(square_matrix[n - 1][j])
    for i in reversed(range(1, n - 1)):
        spiral_order.append(square_matrix[i][0])
    submatrix = [
        [square_matrix[i][j] for j in range(1, n - 1)]
        for i in range(1, n - 1)
    ]
    return spiral_order + matrix_in_spiral_order(submatrix)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
