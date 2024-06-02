
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 6 or a > 100:
        return False

    primes = [num for num in range(2, 100) if is_prime(num)]
    for prime1 in primes:
        for prime2 in primes:
            for prime3 in primes:
                if prime1 * prime2 * prime3 == a:
                    return True
    return False

# Test the function
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(20))  # Output: False
