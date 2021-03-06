from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    def transpose(M: List[List[int]]) -> List[List[int]]:
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                M[i][j], M[j][i] = M[j][i], M[i][j]
        return M
    def reflect(M: List[List[int]]) -> List[List[int]]:
        for row in M:
            for j in range(len(row) // 2):
                row[j], row[~j] = row[~j], row[j]
        return M
    def rotate_clockwise_90(M):
        for i in range(len(M) // 2):
            for j in range(i, len(M) - 1 - i):
                M[i][j], M[j][~i], M[~i][~j], M[~j][i] = \
                    M[~j][i], M[i][j], M[j][~i], M[~i][~j]
    # Use both as an illustration.
    # Key takeaway: https://stackoverflow.com/a/35438327.
    reflect(transpose(square_matrix))
    rotate_clockwise_90(square_matrix)
    reflect(transpose(square_matrix))
    rotate_clockwise_90(square_matrix)
    reflect(transpose(square_matrix))


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
