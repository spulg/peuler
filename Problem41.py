import math
import numpy as np
import itertools as it
import time
from bitarray import bitarray
from sympy import isprime


def bit_primes(n):
    # taken directly from https://stackoverflow.com/a/68295105
    bit_sieve = bitarray(n // 3 + (n % 6 == 2))
    bit_sieve.setall(1)
    bit_sieve[0] = False

    for i in range(int(n ** 0.5) // 3 + 1):
        if bit_sieve[i]:
            k = 3 * i + 1 | 1
            bit_sieve[k * k // 3::2 * k] = False
            bit_sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False

    np_sieve = np.unpackbits(np.frombuffer(bit_sieve.tobytes(), dtype=np.uint8)).view(bool)
    return np.concatenate(((2, 3), ((3 * np.flatnonzero(np_sieve) + 1) | 1)))

def is_pandigital(n):
    for i in range(1, len(str(n)) + 1):
        if str(i) not in str(n):
            return False
    return True


def solve():
    solution = 2143
    # Nine-digit numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
    # Eight-digit numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
    for prime in bit_primes(7654321):
        if is_pandigital(prime):
            solution = max(solution, prime)
    return solution


def solve2():
    # check all possible pandigital numbers if they are prime instead of computing all possible primes up to 7654321 and then check if they are pandigital
    solution = 2341
    for i in range(7, 3, - 1):
        for permutation in it.permutations(range(1, i + 1), i):                 # generate all i! permutations from 1..i
            n = int(''.join(map(str, permutation)))                             # convert tuple into num
            if isprime(n):
                solution = max(solution, n)
        if solution != 2341:
            # already found 7 digit prime, can stop the search
            return solution
    return solution


if __name__ == '__main__':
    execution_time = time.time(); print(solve()); print(f"{(time.time() - execution_time) * 1000} ms")
    execution_time = time.time(); print(solve2()); print(f"{(time.time() - execution_time) * 1000} ms")
