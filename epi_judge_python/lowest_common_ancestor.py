import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from typing import Tuple


def find_targets(tree, node0, node1) -> Tuple[BinaryTreeNode, int]:
    if not tree:
        return None, False
    nodes_found = (tree == node0) + (tree == node1)
    left = find_targets(tree.left, node0, node1)
    if left[0]:
        return left
    right = find_targets(tree.right, node0, node1)
    if right[0]:
        return right
    nodes_found += left[1] + right[1]
    return tree if nodes_found == 2 else None, nodes_found


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    return find_targets(tree, node0, node1)[0]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
