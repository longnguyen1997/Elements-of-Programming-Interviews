from typing import List

from test_framework import generic_test
from bisect import bisect_left

def search_first_of_k(A: List[int], k: int) -> int:

    '''
    Slight modification to basic binary search.
    '''
    i = -1 # Not found yet.
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] == k:
            hi = mid - 1 # Close this one.
            i = mid # Save this as the temporary answer.
        if A[mid] > k:
            hi = mid - 1
        if A[mid] < k:
            lo = mid + 1
    return i

    '''
    Use built-in solutions.
    '''
    i = bisect_left(A, k)
    not_found  = i == len(A) or A[i] != k
    if not_found:
        return -1
    while i > 0 and A[i - 1] == k:
        i -= 1
    return i


if __name__ == '__main__':
    print(search_first_of_k([5,7,7,8,8,10], 8))
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
