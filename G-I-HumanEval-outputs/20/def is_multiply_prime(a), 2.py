
def is_multiply_prime(a):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, a//3 + 1):
        if a % i == 0 and is_prime(i):
            count += 1
    if count == 3:
        return True
    else:
        return False

# Test the function
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(15))  # Output: False
```
