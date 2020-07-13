from typing import List
from math import sqrt, ceil

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    '''
    Faster approach. O(nlog(logn)).
    Use a "bit array" of sorts.
    Exclude multiples.
    Proof by induction on the Sieve of Eratosthenes.
    '''
    is_prime_map = [1] * (n + 1)
    # 0 and 1 are not primes by definition.
    is_prime_map[0] = is_prime_map[1] = 0
    i = 2
    while (i * i <= n):
        if is_prime_map[i]:
            for j in range(i * i, n + 1, i):
                is_prime_map[j] = 0
        i += 1
    return [i for i in range(n + 1) if is_prime_map[i]]

    '''
    Slow approach. O(n^2).
    For each number up to n, brute-force the condition.
    Exclude multiples of primes.
    '''
    primes = []
    exclusions = set() # Exclude multiples of primes.
    for i in range(2, n + 1):
        skip_this_number = False
        for e in exclusions:
            if i % e == 0:
                skip_this_number = True
                break
        if skip_this_number:
            continue
        divisors = set()
        for j in range(1, i + 1):
            if i % j == 0:
                divisors.add(j)
        if len(divisors) == 2 and 1 in divisors and i in divisors:
            primes.append(i)
            exclusions.add(i)
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
