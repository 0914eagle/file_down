
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 6 or a >= 100:
        return False

    primes = [i for i in range(2, a) if is_prime(i)]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(31))  # False
