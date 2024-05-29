
def is_simple_power(x, n):
    if x == 1:  # 1 is always a simple power of any n (n**0 = 1)
        return True
    if x < 2 or n < 2:  # Edge cases where x or n is less than 2
        return False
    
    power = n
    while power < x:  # Repeat the power calculation until it exceeds x
        power *= n
    return power == x

# Test cases
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```
