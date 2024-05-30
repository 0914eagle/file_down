
def check_canonicity(n, denominations):
    if n <= 2:
        return "canonical"
    
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if denominations[i] + denominations[j] <= denominations[n - 1]:
                return "non-canonical"
    
    return "canonical"

# Input
n = int(input())
denominations = list(map(int, input().split()))

# Check canonicity
result = check_canonicity(n, denominations)
print(result)
```
