def palindromic(a: str):
    k = len(a) // 2
    for i in range(k):
        if a[i] != a[len(a) - 1 - i]:
            return False
    return True


def solve():
    palindromes10 = []
    palindromes2 = []
    for i in range(10**6):
        if palindromic(str(i)) and palindromic(str(bin(i))[2:]):
            palindromes10.append(i)
            palindromes2.append(str(bin(i))[2:])
    print(palindromes10)
    print(palindromes2)
    print(sum(palindromes10))


if __name__ == '__main__':
    solve()







