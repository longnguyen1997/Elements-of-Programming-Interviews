from typing import List

from test_framework import generic_test
from collections import Counter


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    '''
    Maintain two pointers.
    Keep incrementing the smaller one until >=.
    '''
    duplicates = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i - 1] != A[i]:
                duplicates.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
    return duplicates

    '''
    Get counts > 1.
    '''
    C = list(set(A)) + list(set(B))
    return sorted(v for v, c in Counter(C).items() if c > 1)

    '''
    Brute force. O(MN).
    '''
    duplicates = set()
    for i, u in enumerate(A):
        for j, v in enumerate(B):
            if u == v:
                duplicates.add(u)
    return sorted(list(duplicates))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
