from typing import List

from test_framework import generic_test
from heapq import heappush, heappop, heapify
from functools import reduce

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    '''
    K sorted arrays. N total elements across all K of them.
    '''

    '''
    Maintain a tracking array A.
    A[i] = Element 0 of sorted_arrays[i].
    While there are still numbers, take the min.
    '''
    output = []
    # O(K).
    heap = [(-sorted_arrays[i].pop(), i) for i in range(len(sorted_arrays))]
    heapify(heap) # O(K) to build a heap.
    # O(NlogK) total, since we need to look at all N elements.
    while heap:
        # O(logK) to pop minimum value.
        value, i = heappop(heap)
        output.append(-value)
        if sorted_arrays[i]:
            heappush(heap, (-sorted_arrays[i].pop(), i))
    # O(N) to reverse and return.
    output.reverse()
    return output
    
    '''
    Get all values and heapify them.
    O(NlogN) time, O(N) space.
    '''
    # O(N).
    all_values = [L[i] for L in sorted_arrays for i in range(len(L))]
    # O(N) (see proof for why this is O(N) and not O(NlogN)).
    heapify(all_values)
    output = []
    # O(NlogN).
    while all_values:
        # Pop (extraction) takes O(logN) at worst
        # if the entire tree needs to be rebalanced.
        output.append(heappop(all_values))
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
