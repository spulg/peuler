import sympy


def f(n: int, a: int, b: int):
    return n**2 + a * n + b


if __name__ == '__main__':
    maxA, maxB, maxCount = 0, 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            count = 0
            while sympy.isprime(f(n, a, b)):
                n += 1
                count += 1
            if count > maxCount:
                maxCount = count
                maxA = a
                maxB = b
    print(f'maxCount = {maxCount}, thus producing a prime for values of 0 <= n <= {maxCount - 1}')
    print(f'n² + {maxA}n + {maxB}')
    print(f'a * b = {maxA * maxB}')
