import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    
    '''
    Best approach:
    Take one clever linear-time pass.
    '''
    pivot = A[pivot_index]
    smaller_than = equal_to = 0
    larger_than = len(A)
    while equal_to < larger_than:
        # Consider all three cases at once.
        if A[equal_to] == pivot:
            equal_to += 1
        elif A[equal_to] < pivot:
            A[equal_to], A[smaller_than] = A[smaller_than], A[equal_to]
            # We're now certain of one more smaller element.
            smaller_than += 1
            equal_to += 1 
        else:
            larger_than -= 1
            A[larger_than], A[equal_to] = A[equal_to], A[larger_than]
    return

    '''
    Better approach:
    Take two linear-time passes.
    '''
    # Pointers for efficiency.
    smaller_than, greater_than = 0, len(A) - 1
    pivot = A[pivot_index]
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller_than] = A[smaller_than], A[i]
            smaller_than += 1
    for j in reversed(range(len(A))):
        if A[j] > pivot:
            A[j], A[greater_than] = A[greater_than], A[j]
            greater_than -= 1
    return

    '''
    Naive approach:
    Find all three categories and modify original array.
    '''
    smaller_than = []
    equal_to = []
    greater_than = []
    pivot = A[pivot_index]
    for num in A:
        if num < pivot:
            smaller_than.append(num)
        elif num == pivot:
            equal_to.append(num)
        else:
            greater_than.append(num)
    partitioned = smaller_than + equal_to + greater_than
    for i in range(len(A)):
        A[i] = partitioned[i]
    return

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
