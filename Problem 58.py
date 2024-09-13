import sympy as sympy

def get_ratio_of_square(n):
    square = []
    for i in range(1, n, 2):
        j = i ** 2
        diagonal_nums = [j + k * (i + 1) for k in range(1, 5)]
        square.append(diagonal_nums)
    # print(square)

    main_diagonal = []  # bottom left to upper right corner
    counter_diagonal = []  # upper left to bottom right corner
    merged = [1]
    for diagonal in square:
        for i in range(0, 4, 2):
            main_diagonal.append(diagonal[i])
            merged.append(diagonal[i])
        for i in range(1, 4, 2):
            counter_diagonal.append(diagonal[i])
            merged.append(diagonal[i])

    num_of_nums = len(merged)
    merged = [num for num in merged if sympy.isprime(num)]
    num_of_primes = len(merged)

    ratio = num_of_primes / num_of_nums
    return ratio


def solve():
    ratio = 1
    i = 1
    num_of_corners = 0
    num_of_prime_corners = 0
    while ratio > 0.1:
        j = i ** 2
        diagonal = [j + k * (i + 1) for k in range(1, 5)]

        num_of_corners += 4
        for num in diagonal:
            if sympy.isprime(num):
                num_of_prime_corners += 1

        ratio = num_of_prime_corners / num_of_corners
        print(ratio)
        i += 2

    print(i)




if __name__ == '__main__':
    solve()


    #k = 7
    #print(get_ratio_of_square(k))
#
    #while get_ratio_of_square(k) > 0.1:
    #    print(get_ratio_of_square(k))
    #    k += 1
#
    #print(k)

