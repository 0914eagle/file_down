
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    for i in range(2, a):
        if a % i == 0:
            factor1 = i
            factor2 = a // i
            if is_prime(factor1) and is_prime(factor2):
                if is_prime(factor2):
                    factor3 = factor2
                    if is_prime(factor3) and factor1 * factor2 * factor3 == a:
                        return True
    return False

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(10))  # False
