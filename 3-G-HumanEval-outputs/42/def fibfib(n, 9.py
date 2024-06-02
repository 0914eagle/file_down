
def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 0, 1]
        for i in range(3, n+1):
            fib.append(fib[i-1] + fib[i-2] + fib[i-3])
        return fib[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
