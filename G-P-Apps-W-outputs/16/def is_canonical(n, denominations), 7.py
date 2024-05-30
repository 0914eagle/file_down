
def is_canonical(n, denominations):
    # Check if the coin system is canonical or non-canonical
    if n < 2:
        return "non-canonical"
    
    # Check if there exists a counterexample
    for x in range(1, denominations[-1] + denominations[-2]):
        change = [float('inf')] * (x + 1)
        change[0] = 0
        
        for i in range(1, x + 1):
            for j in range(n):
                if denominations[j] <= i:
                    change[i] = min(change[i], change[i - denominations[j]] + 1)
        
        if change[x] > len(bin(x)) - 2:
            return "non-canonical"
    
    return "canonical"


# Read input
n = int(input())
denominations = list(map(int, input().split()))
assert denominations[0] == 1

# Check if the coin system is canonical or non-canonical
result = is_canonical(n, denominations)
print(result)
```
