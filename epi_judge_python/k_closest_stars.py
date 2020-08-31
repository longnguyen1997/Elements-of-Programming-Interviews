import functools
import math
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from heapq import *


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    
    heap = []

    for star in stars:
        heappush(heap, (-star.distance, star))
        if len(heap) > k:
            heappop(heap)
    return [star for _, star in heap]

    # Idea: Use a heap to store closest stars, but reverse values.
    # If length of heap exceeds k, pop farthest one (minimum one in reverse).
    for star in stars:
        if heap:
            negative_distance, farthest_star = heap[0]
        if len(heap) == k and negative_distance < -star.distance:
            heappop(heap)
            heappush(heap, (-star.distance, star))
        elif len(heap) < k:
            heappush(heap, (-star.distance, star))
    return [star for _, star in heap]


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
