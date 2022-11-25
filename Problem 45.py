import math


def triangle(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


if __name__ == '__main__':
    for i in range(280, 1000):
        for j in range(160, 1000):
            for k in range(140, 1000):
                if triangle(i) == pentagonal(j) == hexagonal(k):
                    print(i, j, k)
                    print(triangle(i), pentagonal(j), hexagonal(k))


print(triangle(285), pentagonal(165), hexagonal(143))
print(triangle(285) == pentagonal(165) == hexagonal(143))





