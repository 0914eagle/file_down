
def count_split_weights(n):
    weights = set()
    for i in range(1, n + 1):
        remaining_sum = n
        current_weight = 1
        while remaining_sum >= i:
            weights.add(current_weight)
            remaining_sum -= i
            current_weight += 1
    return len(weights)

# Input
n = int(input().strip())

# Output
print(count_split_weights(n))
```
