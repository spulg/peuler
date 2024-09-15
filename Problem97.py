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
    result = (2 * result) % m

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