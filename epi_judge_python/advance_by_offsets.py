from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:

    '''
    Linear approach. Take a single pass
    through the array. Keep track of how
    far we can reach after visiting each
    index.
    '''
    reach = 0
    for i in range(len(A)):
        '''
        We NEED the i > reach condition, because
        if the index we traverse to passes the
        maximum reachable index so far, then it's
        not possible to go any further!
        '''
        if i > reach:
            return False
        reach = max(reach, i + A[i])
    return reach >= len(A) - 1

    '''
    Naive approach.
    For each location in the array, try all combinations.
    If you reach the end, break right away.

    Very slow recursion.
    '''
    if not A:
        return False
    if len(A) == 1:
        return True
    if A[0] == 0:
        return False
    for step in range(A[0]):
        if can_reach_end(A[step + 1:]):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
