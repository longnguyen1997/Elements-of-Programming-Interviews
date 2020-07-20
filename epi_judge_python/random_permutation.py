import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook
from random import randint
from offline_sampling import random_sampling

def compute_random_permutation(n: int) -> List[int]:

    P = list(range(n))
    random_sampling(n, P)
    return P

    if n == 0:
        return [0]
    P = list(range(n))
    for i in range(n):
        j = randint(i, n - 1)
        P[i], P[j] = P[j], P[i]
    return P
    


@enable_executor_hook
def compute_random_permutation_wrapper(executor, n):
    def compute_random_permutation_runner(executor, n):
        def permutation_index(perm):
            p = copy.deepcopy(perm)
            idx = 0
            n = len(p)
            while p:
                a = p.pop(0)
                idx += a * math.factorial(n - 1)
                for i, b in enumerate(p):
                    if b > a:
                        p[i] -= 1
                n -= 1
            return idx

        result = executor.run(
            lambda: [compute_random_permutation(n) for _ in range(1000000)])

        return check_sequence_is_uniformly_random(
            [permutation_index(perm) for perm in result], math.factorial(n),
            0.01)

    run_func_with_retries(
        functools.partial(compute_random_permutation_runner, executor, n))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_permutation.py',
                                       'random_permutation.tsv',
                                       compute_random_permutation_wrapper))
