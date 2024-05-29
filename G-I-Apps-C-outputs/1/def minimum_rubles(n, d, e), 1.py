
def minimum_rubles(n, d, e):
    min_rubles = float('inf')
    
    for dollar in range(n // d + 1):
        remaining_rubles = n - dollar * d
        euro = remaining_rubles // e
        remaining_rubles -= euro * e
        
        if remaining_rubles < min_rubles:
            min_rubles = remaining_rubles
    
    return min_rubles

# Read input values
n = int(input())
d = int(input())
e = int(input())

# Calculate and print the minimum number of rubles
result = minimum_rubles(n, d, e)
print(result)
```
