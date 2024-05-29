
def max_boxing_team(n, weights):
    weights_set = set(weights)
    max_possible = len(weights_set)
    for weight in weights_set:
        if weight+1 not in weights_set:
            max_possible += 1
    return min(max_possible, len(weights))

# Input processing
n = int(input())
weights = list(map(int, input().split()))

# Output
print(max_boxing_team(n, weights))
```
