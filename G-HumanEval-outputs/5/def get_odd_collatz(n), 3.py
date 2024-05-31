
def get_odd_collatz(n):
    result = []
    while n != 1:
        if n % 2 == 1:  # if n is odd
            result.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    result.append(1)  # Add 1 to the result
    return sorted(result)

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
