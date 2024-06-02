
def largest_prime_factor(n: int):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
