from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque, defaultdict


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def traverse(A, B):
        if not A and not B:
            return True
        if not A or not B:
            return False
        return A.data == B.data and traverse(A.left, B.right) and traverse(A.right, B.left)
    return traverse(tree, tree)

    levels = defaultdict(list)
    queue = deque([(tree, 0)])
    while queue:
        node, level = queue.popleft()
        levels[level].append(None if not node else node.data)
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    for level in levels.values():
        for i in range(len(level) // 2):
            if level[i] != level[~i]:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
