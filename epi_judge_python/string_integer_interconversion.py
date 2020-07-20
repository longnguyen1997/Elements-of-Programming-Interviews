from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    sign = -1 if x < 0 else 1
    x = abs(x)
    digits = []
    while x > 0:
        digits.append(str(x % 10))
        x //= 10
    if sign == -1:
        digits.append('-')
    return ''.join(reversed(digits))


def string_to_int(s: str) -> int:
    sign = -1 if s[0] == '-' else 1
    s = s[1:] if s[0] in '+-' else s
    result = 0
    for i, v in enumerate(s):
        e = (len(s) - 1 - i) # Invert the power.
        result += int(v) * (10 ** e)
    return sign * result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
