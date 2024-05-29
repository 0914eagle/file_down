
def max_boxing_team(n, weights):
    unique_weights = set(weights)
    counter = {}
    
    for weight in weights:
        counter[weight] = counter.get(weight, 0) + 1
        
    for weight in counter.keys():
        if counter[weight] > 1:
            if weight - 1 not in unique_weights:
                unique_weights.add(weight - 1)
            elif weight + 1 not in unique_weights:
                unique_weights.add(weight + 1)
    
    return len(unique_weights)

# Input
n = int(input())
weights = list(map(int, input().split()))

# Output
print(max_boxing_team(n, weights))
```
