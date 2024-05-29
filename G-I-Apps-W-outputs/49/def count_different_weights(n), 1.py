
def count_different_weights(n):
    i = 1
    weights = set()
    
    while i * (i + 1) // 2 <= n:
        left = n - (i * (i + 1) // 2)
        if left % i == 0:
            weights.add(i)
        i += 1
    
    weights.add(n)  # Any number can be considered as being a single element weight
    
    return len(weights)

# Read input
n = int(input().strip())

# Call the function and print the output
print(count_different_weights(n))
```
