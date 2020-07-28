import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    '''
    Clean.
    '''
    task_durations.sort()
    return [PairedTasks(task_durations[i], task_durations[~i])
            for i in range(len(task_durations) // 2)]

    '''
    Sort, then pair by ends.
    '''
    assignment = []
    task_durations.sort()
    for i in range(len(task_durations) // 2):
        assignment.append(PairedTasks(task_durations[i], task_durations[~i]))
    return assignment

    '''
    Find max and min for each round. Pair them up.
    '''
    assignment = []
    while task_durations:
        smallest_task, largest_task = min(task_durations), max(task_durations)
        assignment.append(PairedTasks(smallest_task, largest_task))
        task_durations.pop(task_durations.index(smallest_task))
        task_durations.pop(task_durations.index(largest_task))
    return assignment


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
