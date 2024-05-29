
def fib4(n: int):
    if n == 0:
        return 0
    fib = [0, 0, 2, 0]
    if n < 4:
        return fib[n]

    for i in range(4, n+1):
        fib = [fib[1], fib[2], fib[3], fib[0] + fib[1] + fib[2] + fib[3]]

    return fib[3]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
