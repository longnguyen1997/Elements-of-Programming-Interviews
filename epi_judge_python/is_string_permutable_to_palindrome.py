from test_framework import generic_test
from collections import Counter

def can_form_palindrome(s: str) -> bool:

    '''
    Can condense logic from the solution below
    into one condition: at most one odd count.
    '''
    return sum(count % 2 for count in Counter(s).values()) <= 1

    '''
    Criteria:
        1) If the length is even, counts should all be MULTIPLES of 2.
        2) If length is odd, only ONE count should not be mod 2.
    '''
    if len(s) % 2 == 0:
        return all([count % 2 == 0 for count in Counter(s).values()])
    else:
        counts = Counter(s)
        num_odds = 0
        for c in counts.values():
            if c % 2 == 1:
                num_odds += 1
        return num_odds == 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
