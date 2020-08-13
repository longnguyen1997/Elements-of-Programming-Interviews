from typing import List

from test_framework import generic_test
from itertools import accumulate as running_sum

def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    cumulative_times = list(running_sum(service_times))
    return sum(cumulative_times[:-1])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
