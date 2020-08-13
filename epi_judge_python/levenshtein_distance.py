from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    '''
    We can substitute, delete, or insert.
    '''
    # DP[i][j] = edit distance between A[:i] and B[:j].
    # DP[0][0] = 0.
    dp = [[0] * (len(B) + 1) for j in range(len(A) + 1)] 
    for i in range(1, len(A) + 1):
        dp[i][0] = i
    for j in range(1, len(B) + 1):
        dp[0][j] = j
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                delete = dp[i -1][j - 1]
                insert_or_substitute_A = dp[i - 1][j]
                insert_or_substitute_B = dp[i][j - 1]
                dp[i][j] = min(delete, insert_or_substitute_A, insert_or_substitute_B) + 1
    return dp[len(A)][len(B)]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
