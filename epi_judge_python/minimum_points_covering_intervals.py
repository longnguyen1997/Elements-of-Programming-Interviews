import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    if len(intervals) < 2:
        return len(intervals)
    # Sort by start time.
    intervals.sort(key=lambda interval: interval.left)
    # To cover the first element.
    minimum_visits = 1
    current_window = intervals[0]
    for i in range(1, len(intervals)):
        if not (current_window.left <= intervals[i].left <= current_window.right):
            minimum_visits += 1
            current_window = intervals[i]
        else:
            current_window = Interval(max(current_window.left, intervals[i].left),
                                      min(current_window.right, intervals[i].right))
    return minimum_visits


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
