
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_multiply_prime(a):
    if a < 6:
        return False
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            quotient = a // i
            for j in range(i + 1, a):
                if quotient % j == 0 and is_prime(j) and is_prime(quotient // j):
                    return True
    return False

# Test the function
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(20))  # Output: False
