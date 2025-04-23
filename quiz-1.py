def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(a, b):
    factors = []
    for i in range(a, b + 1):
        if is_prime(i):
            factors.append(i)
    return factors

print(prime_factors(1, 40))
