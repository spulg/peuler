import math
import multiprocessing
import time
from itertools import combinations

goal = int(math.sqrt(10 ** 12))

def generate_slices(s):
    n = len(s)
    for k in range(1, n):
        for breaks in combinations(range(1, n), k):
            slice_list = []
            prev = 0
            for b in breaks:
                slice_list.append(s[prev:b])
                prev = b
            slice_list.append(s[prev:])
            yield slice_list


def solve():
    solution = 0
    for s in map(lambda x: pow(x, 2), range(goal + 1)):
        for _slice in generate_slices(str(s)):
            slice_sum = sum(map(int, _slice))
            if int(math.sqrt(s)) == slice_sum:
                solution += s
                print(f"sqrt({s}) = {slice_sum} = {_slice})")
                break
    return solution

def check_num(num, _sum, target):
    # https://stackoverflow.com/questions/77605058/find-numbers-that-are-the-square-of-the-sum-of-a-partition-of-their-digits-in-ba
    if _sum * _sum > target:
        return False
    if (num + _sum) * (num + _sum) == target:
        print(f"({num}", end='')
        return True
    div = 10
    while num // div > 0:
        if check_num(num // div, num % div + _sum, target):
            print(f" + {num % div}", end='')
            return True
        div *= 10
    return False


def solve2(start=9, step=1):
    solution = 0
    for s in map(lambda x: pow(x, 2), range(start, goal + 1, step)):
        if check_num(s, 0, s):
            print(f") ** 2 = {s}")
            solution += s
    return solution


def solve2_multiprocessed():
    cores = multiprocessing.cpu_count()

    with multiprocessing.Pool(cores) as pool:
        results = pool.starmap(solve2, [(i, cores) for i in range(9, cores + 9)])
    total_solution = sum(results)
    return total_solution

# solution from user pascal, Sat, 12 Dec 2020, 14:30
from math import sqrt

def split(a, b):
    if a == b:
        return True
    d = 10
    while d < b:
        p, q = b // d, b % d
        if 0 < a - q <= p and split(a - q, p):
            return True
        d *= 10
    return False

def euler_719(n):
    c = 0
    for i in range(2, int(sqrt(n)) + 1):
        j = i * i
        if split(i, j):
            c += j
    return c

print(euler_719(10 ** 4))
print(euler_719(10 ** 12))


if __name__ == '__main__':
    execution_time = time.time(); print(solve2_multiprocessed()); print(f"{(time.time() - execution_time)}s")
    execution_time = time.time(); print(solve()); print(f"{(time.time() - execution_time) }s")