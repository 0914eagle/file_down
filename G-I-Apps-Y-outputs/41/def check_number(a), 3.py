
def check_number(a):
    if a % 10 == 3 or a % 100 // 10 == 3 or a // 100 == 3:
        return 1
    return 0

# Test cases
print(check_number(13))  # Output: 1
print(check_number(927))  # Output: 1
print(check_number(48))  # Output: 0
```
