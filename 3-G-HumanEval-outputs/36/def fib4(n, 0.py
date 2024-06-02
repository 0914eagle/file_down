
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    fib_values = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib_values[i % 4] = fib_values[(i-1) % 4] + fib_values[(i-2) % 4] + fib_values[(i-3) % 4] + fib_values[(i-4) % 4]
    
    return fib_values[n % 4]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
