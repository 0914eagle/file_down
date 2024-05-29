
def count_weights_of_splits(n):
    weights = set()
    
    for i in range(1, n+1):
        total = n
        count = 1
        
        while total >= i:
            total -= i
            count += 1
            weights.add(count)
        
    return len(weights)

# Reading input
n = int(input().strip())

# Calling the function and printing the output
print(count_weights_of_splits(n))
```
