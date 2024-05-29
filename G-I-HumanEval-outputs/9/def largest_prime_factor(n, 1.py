
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

    factors = get_factors(n)
    prime_factors = [factor for factor in factors if is_prime(factor)]
    return max(prime_factors)

print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
