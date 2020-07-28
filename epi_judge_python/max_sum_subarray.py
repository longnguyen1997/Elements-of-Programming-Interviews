from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # MaxSum(i) = max(MaxSum(i - 1) + A[i], A[i]),
    # where MaxSum(i) is only for the contiguous
    # subarray ENDING AT i, NO GAPS.
    sums = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        sums[i] = max(sums[i - 1] + A[i - 1], A[i - 1])
    return max(sums)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
