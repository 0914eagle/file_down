
def is_multiply_prime(a):
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in range(2, 100) if is_prime(num)]
    
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False

# Test cases
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(31))  # Output: False
