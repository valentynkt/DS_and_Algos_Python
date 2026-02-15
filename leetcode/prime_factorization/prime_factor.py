import math


def prime_factors(n):
    primes = []
    while n % 2 == 0:
        n = n // 2
        primes.append(2)
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            primes.append(i)
    if n > 2:
        primes.append(n)
    return primes
