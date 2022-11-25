import itertools


def permutations(digits: str):
    """returns list of all numbers (as strings) that are a permutation of the digits"""
    result = []
    for digit in itertools.permutations(digits):
        result.append(''.join(digit))
    return result


def three_split(num: str):
    """The problem is solved by first generating all numbers containing the digits [1-9] and then splitting each
    number into all possible 3-splits, while forming the product of the first 2 splits and checking whether it equals
    the third. If you do not put an upper bound to this (obviously the product cannot be a number with fewer digits
    than the multiplicand or multiplicator), a 9-digit number has 36 partitions denoted by the triangle numbers. """
    n = len(num)
    valid_triples = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            multiplicand, multiplicator, product = int(num[0:i]), int(num[i:j]), int(num[j:])
            triple = [multiplicand, multiplicator, product]
            print(triple)
            if multiplicator * multiplicand == product:
                valid_triples.append(triple)
    return valid_triples


def solve():
    result = []
    for permutation in permutations('123456789'):
        spl = three_split(permutation)
        if spl:
            result.append(spl)
    print(result)

    """The solution not only calls for unique solutions in the sense of the order of multiplicand/multiplicator but
    also for the product itself to be unique"""

    products = set()
    for i in range(len(result)):
        products.add(result[i][0][2])
    print(sum(products))


if __name__ == '__main__':
    three_split('123456')
