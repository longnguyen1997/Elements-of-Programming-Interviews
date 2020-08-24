import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    '''
    Smarter. Use the end of the array, but to avoid
    overwriting the end of the desired sequence to
    be examined, start from the end instead.
    Once all the elements are filled, write them back
    to the beginning of the array. Done.
    '''
    L = len(s) - 1
    for i in reversed(range(size)):
        if s[i] == 'a':
            s[L] = s[L - 1] = 'd'
            L -= 2
        elif s[i] != 'b':
            s[L] = s[i]
            L -= 1
    new_length = len(s) - L - 1
    s[:new_length] = s[L + 1:]
    return new_length
    '''
    Brute force. Make a new array, put the elements
    desired in, and overwrite the original.
    '''
    characters = []
    for i in range(size):
        if s[i] == 'a':
            characters.extend(['d', 'd'])
        elif s[i] != 'b':
            characters.extend([s[i]])
    for i, c in enumerate(characters):
        s[i] = c
    return len(characters)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
