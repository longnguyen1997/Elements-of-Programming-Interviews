import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0
    '''
    Maintain two pointers for indices into A.
    One tracks the current unique number.
    The other tracks the next largest number in the array.
    '''
    # These are INDEX variables.
    current_number = 0
    next_unique_number = 1
    while next_unique_number < len(A):
        if A[next_unique_number] > A[current_number]:
            current_number += 1
            A[current_number] = A[next_unique_number]
        next_unique_number += 1
    return current_number + 1 # 0-indexed, so add 1.


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
