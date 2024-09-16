import time

# Instead of computing 2 ** 7830457 directly, use modular exponentiation to compute it modulo 10^10
# Then simply multiply that result by 28433 and take it once more mod 10^10

# a^b mod m = (( a mod m) * a^(b-1) mod m)) mod m

a = 2
b = 7830457
m = 10 ** 10

start = time.monotonic()
result = 2

for i in range(b, 1, -1):
    result = (result << 1) % m

print((((28433 * result) % m) + 1) % m)

end = time.monotonic()
print(f"Duration: {(end - start)} s")

start = time.monotonic()
# however, python seems to be able to compute the value as well (while being the fastest)
print((28433 * (2 ** 7830457) + 1) % m)

end = time.monotonic()
print(f"Duration: {(end - start)} s")

# We can also implement the repeated squares algorithm
# https://en.wikipedia.org/wiki/Modular_exponentiation

def repeated_squares(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    for e_prime in range(exponent):
        e_prime += 1
        c = (base * c) % modulus
    return c


start = time.monotonic()

result = repeated_squares(a, b, m)
print((((28433 * result) % m) + 1) % m)

end = time.monotonic()
print(f"Duration: {(end - start)} s")

# maybe we can match the builtin speed by using this version from the project euler forum:

# calculating 2^7830457 by multiplying 2 7830457  times with itself is not quite a fast algoritm.
# E.g to calculate 2^19 you can first calculate 2, 2^2,  2^4, 2^8 and 2^16 by squaring 2 4 times.
# Then calculate 2^19=2^16*2^2*2.
# Which "squares" to multiply follows directly from the binary representation of 19: 10011
# It is quite straightforward the put this into an algoritm.
