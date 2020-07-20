from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    previous = generate_pascal_triangle(n - 1)
    layer_n = []
    layer_n.append(1)
    for i in range(1, len(previous)):
        layer_n.append(previous[-1][i - 1] + previous[-1][i])
    layer_n.append(1)
    previous.extend([layer_n])
    return previous


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
