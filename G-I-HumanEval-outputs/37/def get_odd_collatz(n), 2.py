
def get_odd_collatz(n):
    
    res = []
    
    while n != 1:
        res.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    res.append(1)
    
    return sorted([num for num in res if num % 2 == 1])

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
