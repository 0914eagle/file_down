
def get_odd_collatz(n):
    result = []
    while n != 1:
        if n % 2 == 1:
            result.append(n)
        n = 3 * n + 1 if n % 2 else n // 2
    result.append(1)
    return sorted(result)

# Test the function with an example
print(get_odd_collatz(5))  # Output: [1, 5]
```
