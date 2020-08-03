from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:

    end = m + n - 1
    i, j = m - 1, n - 1
    while not i < 0 and not j < 0:
        a, b = A[i], B[j]
        if a > b:
            A[end], i = a, i - 1
        else:
            A[end], j = b, j - 1
        end -= 1
    while not j < 0:
        A[end], end, j = B[j], end-1, j-1
    return

    A[m:] = B
    A.sort()


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
