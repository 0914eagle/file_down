
def is_canonical(n, denominations):
    if n < 2:
        return "non-canonical"
    
    for i in range(2, n):
        for j in range(i-1):
            for k in range(j+1):
                if denominations[i] == denominations[j] + denominations[k]:
                    return "non-canonical"
    
    return "canonical"

# Read input
n = int(input())
denominations = list(map(int, input().split()))

# Check if the coin system is canonical or non-canonical
result = is_canonical(n, denominations)
print(result)
```
