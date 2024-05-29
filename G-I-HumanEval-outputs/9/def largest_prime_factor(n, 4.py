
def largest_prime_factor(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        factors = []
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
        return factors

    largest_prime = 0
    factors = get_factors(n)
    for factor in factors:
        if is_prime(factor):
            largest_prime = max(largest_prime, factor)

    return largest_prime

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
