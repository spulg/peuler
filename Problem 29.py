def solve():
    solution = set()
    for i in range(2, 101):
        for j in range(2, 101):
            solution.add(i ** j)
    print(sorted(solution))
    return len([1 for i in solution])

if __name__ == '__main__':
    print(solve())