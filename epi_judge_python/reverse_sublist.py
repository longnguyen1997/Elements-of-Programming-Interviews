from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # Nothing to reverse.
    if start == finish:
        return L
    # Keep the head to return.
    head_placeholder = predecessor = ListNode(next=L)
    # Advance the predecessor to the correct spot.
    for _ in range(1, start):
        predecessor = predecessor.next
    # Start reversing at start node as previous
    # (previous node's next doesn't get affected).
    previous = predecessor.next
    current = previous.next
    for _ in range(finish - start):
        next_temp = current.next
        current.next = previous
        previous, current = current, next_temp
    # Set new successors.
    predecessor.next.next = current
    predecessor.next = previous
    return head_placeholder.next
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
