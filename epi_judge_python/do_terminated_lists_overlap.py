import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    num_nodes_l0 = num_nodes_l1 = 0
    l0_ptr, l1_ptr = l0, l1
    # Get the node count for both.
    while l0_ptr and l0_ptr.next:
        l0_ptr = l0_ptr.next
        num_nodes_l0 += 1
    while l1_ptr and l1_ptr.next:
        l1_ptr = l1_ptr.next
        num_nodes_l1 += 1
    # If they have the same tail,
    # there must be an intersection node.
    if l0_ptr is l1_ptr:
        # Move the longer list to a starting point.
        if num_nodes_l1 > num_nodes_l0:
            l0, l1 = l1, l0
        for i in range(abs(num_nodes_l0 - num_nodes_l1)):
            l0 = l0.next
        # Advance both until we reach the intersection.
        while l0 and l1 and l0 is not l1:
            l0, l1 = l0.next, l1.next
        return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
