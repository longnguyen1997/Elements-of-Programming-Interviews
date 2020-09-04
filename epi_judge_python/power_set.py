from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:

    power_set = []

    def explore_subsets(i, subset):
        if i == len(input_set):
            power_set.append(subset)
            return
        explore_subsets(i + 1, subset)
        explore_subsets(i + 1, subset + [input_set[i]])

    explore_subsets(0, [])
    return power_set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
