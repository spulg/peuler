import sympy as sy


if __name__ == '__main__':
    maxCount = 0
    maxPrime = 0
    limit = 10**6
    primes = list(sy.primerange(2, limit + 1))
    for prime in primes:
        n = 0
        curr_sum = 0
        curr_prime = primes[n]
        while curr_sum < prime:
            n += 1
            curr_sum += curr_prime
            curr_prime = primes[n]

        if curr_sum == prime and n > maxCount:
            maxCount = n
            maxPrime = curr_sum
    print(f'The prime below {limit} that can be written with the most ({maxCount}) terms is {maxPrime}.')
