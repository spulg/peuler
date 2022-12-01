"""
prime generator sieve
"""


def primes():
    sieve = {}
    q = 2
    while True:
        if q not in sieve:
            yield q
            sieve[q * q] = [q]
        else:
            for p in sieve[q]:
                sieve.setdefault(p + q, []).append(p)
            del sieve[q]
        q += 1
