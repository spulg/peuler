from itertools import permutations

pandigital_nums = [''.join(p) for p in permutations("0123456789")]
divisors = [2, 3, 5, 7, 11, 13, 17]

def solve():
    nums = []
    for num in pandigital_nums:
        # leading zeros get removed in the int conversion
        if num[0] != '0':
            if has_property(int(num)):
                nums.append(int(num))
    return nums, sum(nums)


def has_property(n):
    for i in range(1, 8):
        if not int(str(n)[i:i + 3]) % divisors[i - 1] == 0:
            return False
    return True


if __name__ == '__main__':
    print(has_property(1406357289))
    print(solve())
