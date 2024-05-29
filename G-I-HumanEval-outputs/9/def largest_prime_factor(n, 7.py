
def largest_prime_factor(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            if is_prime(i):
                largest_prime = max(largest_prime, i)
            if is_prime(n // i):
                largest_prime = max(largest_prime, n // i)
        i += 1

    return largest_prime

print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))    # Output: 2
