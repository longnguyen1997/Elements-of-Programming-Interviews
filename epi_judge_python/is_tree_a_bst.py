from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:

    '''
    Verify the inorder traversal.
    O(n) time, O(n) space.
    '''
    def inorder_traversal(node: BinaryTreeNode):
        if not node:
            return []
        left = inorder_traversal(node.left)
        left.extend([node.data])
        left.extend(inorder_traversal(node.right))
        return left
    traversal = inorder_traversal(tree)
    for i in range(1, len(traversal)):
        if traversal[i - 1] > traversal[i]:
            return False
    return True

    '''
    Traverse and check invariant.
    O(n) time, O(h) space (recursion stack).
    '''
    def traverse_bst(node: BinaryTreeNode,
                     lower_bound=float('-inf'),
                     upper_bound=float('inf')) -> bool:
        if not node:
            return True
        if not lower_bound <= node.data <= upper_bound:
            return False
        return (traverse_bst(node.left, lower_bound, node.data) and
                traverse_bst(node.right, node.data, upper_bound))
    return traverse_bst(tree)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
