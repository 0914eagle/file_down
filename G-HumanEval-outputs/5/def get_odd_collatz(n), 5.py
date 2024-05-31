
def get_odd_collatz(n):
    result = set()
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            result.add(n)
            n = 3 * n + 1
    result.add(1)
    return sorted(list(result))

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
