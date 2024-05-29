
def largest_prime_factor(n: int):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Find the largest prime factor of n
    i = 2
    while i <= n:
        if n % i == 0:
            if is_prime(n // i):
                return n // i
        i += 1

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
