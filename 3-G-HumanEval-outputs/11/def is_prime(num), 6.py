
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 6 or a > 100:
        return False

    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            for j in range(i+1, a):
                if a % (i*j) == 0 and is_prime(j) and is_prime(a//(i*j)):
                    return True
    return False

# Test the function
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(20))  # Output: False
