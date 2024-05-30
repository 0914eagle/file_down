
def max_fruits(N, C, weights):
    max_fruits_count = 0
    current_weight = 0
    fruits_count = {}
    
    for weight in weights:
        if current_weight + weight <= C:
            current_weight += weight
            if weight not in fruits_count:
                fruits_count[weight] = 1
                max_fruits_count += 1
        else:
            break
    
    return max_fruits_count

# Read input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function and print the output
print(max_fruits(N, C, weights))
```
