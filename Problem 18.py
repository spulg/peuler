# linear time dynamic programming for problem 18 / 67

def parse_data():
    lines = []
    with open('p67_data.txt') as file:
        lines = file.readlines()

    triangle = []
    for line in reversed(lines):
        line.strip()
        triangle.append([int(num) for num in line.split(' ')])

    return triangle

def solve(triangle):
    sol_table = triangle.copy()
    n = len(triangle)

    for i in range(1, n):
        for j in range(n - i):
            sol_table[i][j] = sol_table[i][j] + max(sol_table[i - 1][j],  sol_table[i - 1][j + 1])

    # print(sol_table)
    return sol_table[n - 1][0]

if __name__ == "__main__":
    print(solve(parse_data()))
