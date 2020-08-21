from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

def reverse_inorder(node, k, nodes):
    if len(nodes) == k:
        return nodes
    if not node:
        return nodes
    reverse_inorder(node.right, k, nodes)
    if len(nodes) == k:
        return nodes
    nodes.append(node.data)
    reverse_inorder(node.left, k, nodes)
    return nodes

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    return reverse_inorder(tree, k, [])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
