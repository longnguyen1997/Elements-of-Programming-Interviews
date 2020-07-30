from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    c_to_int = {str(i): i for i in range(10)}
    c_to_int['A'], c_to_int['B'], c_to_int['C'], c_to_int['D'], c_to_int['E'], c_to_int['F'] = \
        10, 11, 12, 13, 14, 15
    int_to_c = {v: k for k, v in c_to_int.items()}

    def convert_to_base_10(num_as_string: str, b: int) -> int:
        n = 0
        num_as_string = num_as_string[::-1]
        for i, c in enumerate(num_as_string):
            n += c_to_int[c] * (b ** i)
        return n

    def convert_to_base_b(num_base_10: int, b: int) -> str:
        if num_base_10 < 0:
            return '-' + convert_to_base_b(-num_base_10, b)
        if num_base_10 < b:
            return int_to_c[num_base_10]
        return convert_to_base_b(num_base_10 // b, b) + int_to_c[num_base_10 % b]

    negative = 1 if num_as_string[0] == '-' else 0
    num_as_string = num_as_string[1:] if num_as_string[0] == '-' else num_as_string

    return ('-' * negative) + convert_to_base_b(convert_to_base_10(num_as_string, b1), b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
