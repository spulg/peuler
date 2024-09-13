def equal_digits(n: int, m: int) -> bool:
    n_digits = set([digit for digit in str(n)])
    m_digits = set([digit for digit in str(m)])
    return n_digits == m_digits

def solve():
    for i in range(100_000, 100_000_000_000):
        multiples = [i * j for j in range(1, 7)]
        bools = [False for j in range(6)]
        for j in range(6):
            bools[j] = equal_digits(i, multiples[j])
        if all(bools):
            print(i)
            break


if __name__ == '__main__':
    # print(equal_digits(125874, 251748))
    solve()


