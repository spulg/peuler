def triangle(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def solve():
    triangles = set()
    pentagons = set()
    hexagons = set()
    for i in range(1, 100000):
        triangles.add(triangle(i))
        pentagons.add(pentagonal(i))
        hexagons.add(hexagonal(i))

    print(triangles.intersection(pentagons).intersection(hexagons))



if __name__ == '__main__':
    solve()



print(triangle(285), pentagonal(165), hexagonal(143))
print(triangle(285) == pentagonal(165) == hexagonal(143))





