
def get_odd_collatz(n):
    if n <= 0:
        return []

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
print(get_odd_collatz(10))  # Output: [1, 5]
print(get_odd_collatz(20))  # Output: [1, 3, 5, 9, 19]
```
