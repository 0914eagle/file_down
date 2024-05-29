
def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    while x > 1:
        if x % n != 0:
            return False
        x /= n
    return True

# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
```
