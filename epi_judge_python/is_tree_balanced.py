from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def height(node: BinaryTreeNode) -> Tuple[int, bool]:
        if not node:
            return -1, True
        L = height(node.left)
        if not L[1]: return 0, False
        R = height(node.right)
        if not R[1]: return 0, False
        return max(L[0], R[0]) + 1, abs(L[0] - R[0]) <= 1
    return height(tree)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
