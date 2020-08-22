from typing import Iterator, List

from test_framework import generic_test
from heapq import heappush, heappop


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = []
    sorted = []
    for n in sequence:
        if len(heap) == k + 1:
            sorted.append(heappop(heap))
        heappush(heap, n)
    while heap:
        sorted.append(heappop(heap))
    return sorted


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
