from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_list(L: ListNode, precursor: ListNode) -> ListNode:
    dummy_head = precursor
    while L:
        dummy_head.next, L.next, L = L, dummy_head.next, L.next
    return dummy_head.next

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if L is None:
        return None
    i, aux_L = 0, ListNode(0, L)
    if start > 1:
        i, aux_L = 1, L
        while i != start - 1:
            aux_L = aux_L.next
            i += 1
    
    
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
