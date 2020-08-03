from typing import List

from test_framework import generic_test
from sorted_arrays_merge import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_arrays = []  # O(N) space.

    ''' —————— SOLUTION A —————— '''
    increasing, decreasing = range(2)
    array = increasing
    start = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or
            A[i - 1] < A[i] and array is decreasing or
                A[i - 1] > A[i] and array is increasing):
            sorted_arrays.append(A[start: i] if array is increasing
                                 else A[i - 1: start - 1: -1])
            start = i
            array = increasing if array is decreasing else increasing
    return merge_sorted_arrays(sorted_arrays)

    ''' —————— SOLUTION B —————— '''
    # Keep 0 in there, since we initially have a 1-increasing array.
    subarray_indices = [0]  # O(K) space.
    for i in range(1, len(A)):
        if A[i - 1] > A[i] and len(subarray_indices) % 2 == 1:
            subarray_indices.append(i)
        if A[i - 1] < A[i] and len(subarray_indices) % 2 == 0:
            subarray_indices.append(i)
    if len(subarray_indices) == 1:
        return A
    subarray_indices.append(len(A))
    for i in range(len(subarray_indices) - 1):
        if len(sorted_arrays) % 2 == 0:
            sorted_arrays.append(A[
                subarray_indices[i]: subarray_indices[i + 1]
            ])
        else:
            sorted_arrays.append(A[
                subarray_indices[i]: subarray_indices[i + 1]
            ][::-1])
    return merge_sorted_arrays(sorted_arrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
