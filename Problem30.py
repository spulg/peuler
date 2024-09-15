def solve():
    solution = 0
    for i in range(2, 6 * (9 ** 5)):             # 5 * (9 ** 5)
        _sum = 0
        for c in map(int, str(i)):
            _sum += c ** 5
        if _sum == i:
            # print(i)
            solution += _sum
    return solution

if __name__ == "__main__":
    print(solve())