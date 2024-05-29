
def max_boxers(n, weights):
    unique_weights = set(weights)
    
    count = len(unique_weights)
    for weight in unique_weights:
        if weight+1 in unique_weights:
            count += 1
        elif weight-1 in unique_weights:
            count += 1
    
    return count

# Reading input
n = int(input())
weights = list(map(int, input().split()))

# Getting the maximum possible number of boxers in a team
result = max_boxers(n, weights)
print(result)
```
