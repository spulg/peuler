from peulerlib import primes
from math import sqrt


def is_composite_and_writeable(i):
    for j in range(1, int(sqrt(i))):
        pr = primes()
        for k in range(i // 2):
            p = next(pr)
            if i == p:
                print(f"{i} is prime")
                return True
            elif i == p + 2 * j ** 2:
                print(f"{i} = {p} + 2 x {j}²")
                return True
    print(f"{i} is not writeable as the sum of a prime and twice a square")
    return False


def solve():
    i = 9
    conjecture = True
    while conjecture:
        if is_composite_and_writeable(i):
            i += 2
        else:
            conjecture = False


if __name__ == '__main__':
    solve()
