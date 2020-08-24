from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    '''
    DP(i, j) = number of ways to get to (i, j) from (0, 0).
    '''
    DP = [[0] * n for i in range(m)]
    for j in range(n):
        DP[0][j] = 1
    for i in range(m):
        DP[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
    return DP[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
