import collections
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook
from random import random
from bisect import bisect

def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:
    # O(n) to sum everything up.
    for i in range(1, len(probabilities)):
        probabilities[i] += probabilities[i - 1]
    R = random()
    log_n_find = True
    # O(logn) to search for the bin.
    if log_n_find:
        return values[bisect(probabilities, R)]
    # O(n) to search for the bin.
    for i, p in enumerate(probabilities):
        if R < p:
            return values[i]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda: [
            nonuniform_random_number_generation(values, probabilities)
            for _ in range(N)
        ])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'nonuniform_random_number.py', 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
