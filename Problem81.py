import time
import numpy as np

def parse():
    with open("0081_matrix.txt") as file:
        m = file.readlines()

    numerical_matrix = []
    for line in m:
        numerical_line = []
        nums = line.split(',')
        for num in nums:
            numerical_line.append(int(num))
        numerical_matrix.append(numerical_line)

    return numerical_matrix

def parse2():
    return np.loadtxt("0081_matrix.txt", delimiter=',', dtype=int)


def solve():
    matrix = parse()
    n = len(matrix)
    solution = [[0] * n for _ in range(n)]
    solution[n - 1][n - 1] = matrix[n - 1][n - 1]

    def compute_min(x, y):
        return matrix[y][x] + min(
            solution[y + 1][x] if y + 1 <= n - 1 else solution[y][x + 1],
            solution[y][x + 1] if x + 1 <= n - 1 else solution[y + 1][x]
        )

    for x in reversed(range(n - 1)):
        for y in reversed(range(x, n)):
            solution[y][x] = compute_min(x, y)
            if x != y:
                solution[x][y] = compute_min(y, x)

    return solution[0][0]


def solve2():
    matrix = parse2()
    n = matrix.shape[0]
    solution = np.zeros((n, n), dtype=int)
    solution[n - 1, n - 1] = matrix[n - 1, n - 1]

    def compute_min(x, y):
        return matrix[y, x] + np.minimum(
            solution[y + 1, x] if y + 1 <= n - 1 else solution[y, x + 1],
            solution[y, x + 1] if x + 1 <= n - 1 else solution[y + 1, x]
        )

    for x in reversed(range(n - 1)):
        for y in reversed(range(x, n)):
            solution[y, x] = compute_min(x, y)
            if x != y:
                solution[x, y] = compute_min(y, x)

    return solution[0, 0]

if __name__ == '__main__':
    start = time.monotonic()
    print(solve())
    end = time.monotonic()
    print(f"Duration: {(end - start) * 1_000} ms")

    start = time.monotonic()
    print(solve2())
    end = time.monotonic()
    print(f"Duration: {(end - start) * 1_000} ms")

