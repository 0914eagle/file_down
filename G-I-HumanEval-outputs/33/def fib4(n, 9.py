
def fib4(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    
    a, b, c, d = 0, 0, 2, 0
    result = 0
    
    for i in range(4, n+1):
        result = a + b + c + d
        a, b, c, d = b, c, d, result
        
    return result

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
