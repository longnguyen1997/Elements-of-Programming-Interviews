from typing import List

from test_framework import generic_test


white, black, visited = 'W', 'B', 'V'


def fill_surrounded_regions(board: List[List[str]]) -> None:

    m, n = len(board), len(board[0])

    def flood(i, j):
        if not (0 <= i < m and 0 <= j < n) or board[i][j] is not white:
            return
        board[i][j] = visited
        # Flood all four neighbors if possible.
        flood(i - 1, j)
        flood(i, j + 1)
        flood(i + 1, j)
        flood(i, j - 1)

    for i in range(m):
        for j in range(n):
            if any([i == 0, j == 0, i == m - 1, j == n - 1]):
                flood(i, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] is visited:
                board[i][j] = white
            else:
                board[i][j] = black


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
