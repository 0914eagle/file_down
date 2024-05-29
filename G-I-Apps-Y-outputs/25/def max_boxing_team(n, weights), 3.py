
def max_boxing_team(n, weights):
    unique_weights = set(weights)
    count = min(len(unique_weights), max(unique_weights) + 1)
    return count

# Read input
n = int(input())
weights = list(map(int, input().split()))

# Call the function and print the result
result = max_boxing_team(n, weights)
print(result)
```
