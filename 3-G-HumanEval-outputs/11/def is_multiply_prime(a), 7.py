
def is_multiply_prime(a):
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if a < 2 or a >= 100:
        return False

    primes = [num for num in range(2, a) if is_prime(num)]
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(20))  # False
print(is_multiply_prime(42))  # False
print(is_multiply_prime(2))   # False
