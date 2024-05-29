
def is_multiply_prime(a):
    if a < 2:
        return False

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, 100) if is_prime(i)]

    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True

    return False

print(is_multiply_prime(30))  # Output: True
