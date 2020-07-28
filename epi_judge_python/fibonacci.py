from test_framework import generic_test


def fibonacci(n: int) -> int:
    if n <= 1: return n
    f_2, f_1 = 0, 1
    for i in range(2, n + 1):
        f_i = f_2 + f_1
        f_2, f_1 = f_1, f_i
    return f_1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
