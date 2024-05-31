
def get_odd_collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            result.append(n)
    return sorted(set(result))

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
