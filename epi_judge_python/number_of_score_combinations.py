from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:

    '''
    Variant: Solve the problem using only O(s) space.
    '''
    S = [0] * (final_score + 1)
    S[0] = 1
    for score in individual_play_scores:
        for subscore in range(score, final_score + 1):
            S[subscore] += S[subscore - score]
    return S[-1]

    '''
    Optimized.
    S[i][all j < score i] = S[i - 1][j].
    S[i][j >= score i] = S[i - 1][j] + S[i - 1][j - score i].
    O(sn) time and space.
    '''
    S = [[1] + [0] * final_score for _ in individual_play_scores]
    for i, score_i in enumerate(individual_play_scores):
        for subscore in range(1, final_score + 1):
            # Base case: only multiples of the first score.
            if i == 0:
                S[i][subscore] = int(subscore % score_i == 0)
            else:
                S[i][subscore] += S[i - 1][subscore]
                if subscore >= score_i:
                    S[i][subscore] += S[i][subscore - score_i]
    return S[-1][-1]

    '''
    S[I][J] -> number of ways to get to score J using I possible scores.
    S[I + 1][J] = S[I][J] + S[I][J - s[i + 1]] + ... + S[I][J - ns[i + 1]] (til <= 0).
    Third loop is O(s), total O(s^2 * n).
    '''
    # Initialize 2D storage.
    S = [[0] * (final_score + 1)
         for _ in individual_play_scores]
    # 1 way to have a score of 0: take none of each.
    for row in S:
        row[0] = 1
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            if i == 0:
                # No previous sums to refer to.
                S[i][j] = int(j % individual_play_scores[i] == 0)
            else:
                for subscore in range(j, -1, -individual_play_scores[i]):
                    S[i][j] += S[i - 1][subscore]
    return S[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
