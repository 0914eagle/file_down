
def is_multiply_prime(a):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [x for x in range(2, 100) if is_prime(x)]
    for x in primes:
        for y in primes:
            for z in primes:
                if x * y * z == a:
                    return True
    return False

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(35))  # False
print(is_multiply_prime(17))  # False
