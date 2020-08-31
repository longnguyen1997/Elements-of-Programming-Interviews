from test_framework import generic_test


def square_root(k: int) -> int:
    candidate = -1
    left, right = 0, k
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= k:
            candidate = mid
            left = mid + 1
        elif mid * mid > k:
            right = mid - 1
    return candidate

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
