from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mid >= 1 and A[mid - 1] > A[mid]:
            return mid
        if A[mid] < A[right]:
            right = mid - 1
        else:
            left = mid + 1
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
