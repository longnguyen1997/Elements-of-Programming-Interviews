from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    '''
    General strategy: for each element, pick it and recurse
    on the remaining elements. Should yield all permutations.
    '''
    def permute_recurse(A, path, permutations):
        if not A:
            permutations.append(path)
            return permutations
        for i, element in enumerate(A):
            new_path = path[::]
            new_path.append(element)
            permute_recurse(A[:i] + A[i + 1:], new_path, permutations)
        return permutations
    return permute_recurse(A, [], [])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
