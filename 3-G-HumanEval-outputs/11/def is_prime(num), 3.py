
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 6:
        return False

    for i in range(2, a):
        if is_prime(i):
            for j in range(i, a):
                if is_prime(j):
                    for k in range(j, a):
                        if is_prime(k) and i * j * k == a:
                            return True
    return False

# Test the function
print(is_multiply_prime(30))  # Output: True
