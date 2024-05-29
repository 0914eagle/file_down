
def is_multiply_prime(a):
    
    if a < 6:  # Checking for numbers less than 6 as they cannot be expressed as product of 3 primes
        return False

    # Using a simple prime check function
    def is_prime_num(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count_primes = 0
    for i in range(2, a):
        if is_prime_num(i) and a % i == 0:
            count_primes += 1
            a = a // i
        if count_primes == 3:
            return True
    return False

# Test cases
print(is_multiply_prime(30))  # Output: True
```
