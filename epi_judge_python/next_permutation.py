from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    def find_latest_smaller_element(perm):
        for i in reversed(range(len(perm))):
            if perm[i] > perm[i - 1]:
                return i - 1 
        return -1
    def swap_and_reverse_smaller_element_seq(perm, index):
        '''
        Reverse everything after index, then swap index with
        elemnent with next lexicographic number.
        '''
        perm[index + 1:] = reversed(perm[index + 1:])
        j = index + 1
        while perm[j] <= perm[index]:
            j += 1
        perm[index], perm[j] = perm[j], perm[index]
        return perm
    next_lexico_index = find_latest_smaller_element(perm)
    if next_lexico_index == -1:
        return []
    return swap_and_reverse_smaller_element_seq(perm, next_lexico_index)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
