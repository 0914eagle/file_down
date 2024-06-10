
import math

def prime_factorize(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)
    return prime_factors

def count_odd_numbers_with_exactly_eight_positive_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            prime_factors = prime_factorize(i)
            divisor_count = 1
            for prime_factor in prime_factors:
                divisor_count *= (prime_factors.count(prime_factor) + 1)
            if divisor_count == 8:
                count += 1
    return count

n = int(input())
print(count_odd_numbers_with_exactly_eight_positive_divisors(n))

