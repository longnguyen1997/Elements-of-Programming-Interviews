from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    ''' Solution 1 '''
    letter_count = Counter(letter_text)
    for char in magazine_text:
        if char in letter_count:
            letter_count[char] -= 1
    for l, c in letter_count.items():
        if c > 0:
            return False
    return True
    # Shorthand, but uses more space.
    return all([c < 1 for c in letter_count.values()])

    ''' Solution 2 '''
    magazine_count = Counter(magazine_text)
    for letter, count in Counter(letter_text).items():
        if count > magazine_count[letter]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
