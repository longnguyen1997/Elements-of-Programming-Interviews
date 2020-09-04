from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()
    max_value = 0
    for n in A:
        if n > max_value + 1:
            break
        max_value += n
    return max_value + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
