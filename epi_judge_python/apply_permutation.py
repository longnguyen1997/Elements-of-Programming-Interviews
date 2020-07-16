from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[str]) -> None:

    '''
    Smarter approach.
    Continously do swaps until you've reached the end
    of the cycle for the current index being swapped.
    Condition for cycle ending: you end back at the original
    index described in the permutation.
    Make sure not to repeat cycles.
    '''
    N = len(A)
    P = perm
    for i in range(N):
        # Cycle including this index already applied.
        if P[i] < 0:
            continue
        current_index, current_val, next_index = i, A[i], perm[i]
        while current_index >= 0 and next_index != i:
            next_val = A[next_index]
            A[next_index] = current_val
            P[current_index] -= N
            current_index, current_val, next_index = next_index, next_val, perm[next_index]
        # Still need to move the last placeholder to the cycle origin.
        A[i] = current_val
        P[current_index] -= N # Mark index right before cycle origin as visited.
    for i in range(N):
        P[i] += N
    return

    '''
    Brute force solution.
    O(n) space, O(n) time.
    Make a new list and iterate through the permutation.
    Apply the permutation to the original list in place.
    '''
    new_data = [0] * len(A)
    for i, j in enumerate(perm):
        new_data[j] = A[i]
    for i, n in enumerate(new_data):
        A[i] = n


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
