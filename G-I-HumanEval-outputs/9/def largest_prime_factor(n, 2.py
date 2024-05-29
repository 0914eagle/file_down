
def largest_prime_factor(n: int):
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n = n // divisor
        else:
            divisor += 1
    return divisor

print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
