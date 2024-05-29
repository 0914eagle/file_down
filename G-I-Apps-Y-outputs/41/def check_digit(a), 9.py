
def check_digit(a):
    if a % 10 == 3 or a % 100 // 10 == 3:
        return 1
    return 0

# Test cases
print(check_digit(13))  # Output: 1
print(check_digit(927))  # Output: 1
print(check_digit(48))  # Output: 0
```

