
def max_fruits_to_eat(N, C, weights):
    total_weight = 0
    unique_fruits = set()
    max_fruits = 0
    for i in range(N):
        if total_weight + weights[i] <= C:
            total_weight += weights[i]
            unique_fruits.add(weights[i])
            max_fruits = max(max_fruits, len(unique_fruits))
        else:
            break
    return max_fruits

# Read input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function and print the result
print(max_fruits_to_eat(N, C, weights))
```
