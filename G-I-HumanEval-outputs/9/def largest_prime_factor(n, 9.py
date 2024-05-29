
def largest_prime_factor(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_factor = 2
    while n > 1:
        if n % prime_factor == 0:
            n /= prime_factor
            if is_prime(n):
                return int(n)
        else:
            prime_factor += 1

largest_prime_factor(13195)  # Output: 29
largest_prime_factor(2048)   # Output: 2
```
