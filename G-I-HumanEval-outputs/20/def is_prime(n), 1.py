
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            q = a // i
            for j in range(i + 1, q):
                if q % j == 0 and is_prime(j) and is_prime(q // j):
                    return True
    return False

# Test the function
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(31))  # Output: False
