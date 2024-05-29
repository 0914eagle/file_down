
def largest_prime_factor(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_factors(num):
        factors = []
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and is_prime(i):
                factors.append(i)
        return factors

    factors = find_factors(n)
    return max(factors)

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
