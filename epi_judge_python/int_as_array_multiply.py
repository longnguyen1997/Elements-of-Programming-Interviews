from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    '''
    Optimized approach.
    Imitate the primary school algorithm.
    '''
    sign = 1
    if num1[0] < 0: sign *= -1
    if num2[0] < 0: sign *= -1
    # Invert the sign on both.
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    L1, L2 = len(num1), len(num2)
    output = [0] * (L1 + L2) # Max length possible.
    for i in reversed(range(L1)):
        for j in reversed(range(L2)):
            # + 1 to account for 0-indexing.
            output[i + j + 1] += num1[i] * num2[j]
            output[i + j] += output[i + j + 1] // 10
            output[i + j  + 1] %= 10
    # Find the beginning.
    result_index = 0
    while output[result_index] == 0:
        result_index += 1
        if result_index == len(output):
            return [0]
    output[result_index] *= sign
    return output[result_index:]

    '''
    Naive approach.
    Take both, convert to a number, multip3ly,
    convert back to a list.
    Result will overflow if the product is too big.
    '''
    X = int(''.join([str(n) for n in num1]))
    Y = int(''.join([str(n) for n in num2]))
    return list(str(X + Y))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
