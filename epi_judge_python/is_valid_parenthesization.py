from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    left = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in left:
            stack.append(c)
        elif not stack or left[stack.pop()] != c:
            return False
    return not stack

    right = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in s:
        if not stack:
            if c in right:
                return False
            stack.append(c)
        elif c in right:
            if right[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
