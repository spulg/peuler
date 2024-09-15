import math


def solve():
    count = 0
    for i in range(10000):
        if is_lychrel(i):
            count += 1
        return count


def reverse(s):                         # reverses a string
    temp = ''
    for i in range(1, len(s) + 1):
        temp += s[len(s) - i]
    return temp


def is_lychrel(n):                      # if it can't find a palindrome after 50 reversal-addings it returns True
    temp = n
    for i in range(50):
        temp += int(reverse(str(temp)))
        if is_palindrome(str(temp)):
            return False
    return True


def is_palindrome(s):
    k = 1
    f_length = math.floor(len(s) / 2)       # needed for odd length
    if len(s) % 2 == 0:                     # check if string has even or odd length
        while k < len(s)/2 + 1:             # in a 4 letter word you need to check if 1 and 4 + 2 and 3 are the same
            if s[k - 1] != s[len(s) - k]:
                return False
            k = k + 1
    else:                                   # odd
        while k != f_length+1:              # middle letter | in a 5 letter word you need to check if 1 and 5 + 2 and 4
            if s[k-1] != s[len(s)-k]:       # are the same, the middle letter doesn't matter
                return False
            k = k + 1
    return True


def solve_problem():
    solve()


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve_problem()
    print("runtime: \x1b[1;31m%.1fs\x1b[0m" % (time.time() - start_time))

import profile
profile.run('solve_problem()')






