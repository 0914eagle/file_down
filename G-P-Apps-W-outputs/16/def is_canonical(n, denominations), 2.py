
def is_canonical(n, denominations):
    if n < 2:
        return "non-canonical"
    
    for i in range(1, n-1):
        for j in range(i+1, n):
            if denominations[i] + denominations[j] <= denominations[-1]:
                return "non-canonical"
    
    return "canonical"

# Input
n = int(input())
denominations = list(map(int, input().split()))

# Check if the coin system is canonical
result = is_canonical(n, denominations)
print(result)
```
