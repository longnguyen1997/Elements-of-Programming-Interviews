from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Cleaner code. O(1) space.
    '''
    head = current = ListNode()
    A, B = L1, L2
    while A and B:
        if A.data < B.data:
            current.next = A; A = A.next
        else:
            current.next = B; B = B.next
        current = current.next
    current.next = A or B
    return head.next
    '''
    Optimized with O(1) space.
    Traverse on a case-by-case basis.
    '''
    if not L1: return L2
    if not L2: return L1
    if L1.data < L2.data:
        current_node = L1; L1 = L1.next
    else:
        current_node = L2; L2 = L2.next
    head = current_node
    while L1 and L2:
        if L1.data < L2.data:
            current_node.next = L1
            L1 = L1.next
        else:
            current_node.next = L2
            L2 = L2.next
        current_node = current_node.next
    current_node.next = L1 or L2
    return head
    
    '''
    Brute force with O(L1 + L2) space.
    '''
    nodes = []
    while L1: nodes.append(L1); L1 = L1.next
    while L2: nodes.append(L2); L2 = L2.next
    if not nodes: return None
    nodes.sort(key=lambda node: node.data)
    nodes.append(None)
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]    
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
