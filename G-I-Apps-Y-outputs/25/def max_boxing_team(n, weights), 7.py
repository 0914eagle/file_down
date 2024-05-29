
def max_boxing_team(n, weights):
    weights.sort()
    unique_weights = set()
    for weight in weights:
        # Check if weight-1 or weight+1 is not already in the unique_weights set
        if weight-1 not in unique_weights and weight+1 not in unique_weights:
            unique_weights.add(weight)
    
    return len(unique_weights)

n = int(input())
weights = list(map(int, input().split()))

print(max_boxing_team(n, weights))
```
