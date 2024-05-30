
def max_fruits(N, C, weights):
    max_fruits = 0
    total_weight = 0
    unique_fruits = set()

    for weight in weights:
        if total_weight + weight <= C:
            total_weight += weight
            unique_fruits.add(weight)
            max_fruits = len(unique_fruits)
        else:
            break

    return max_fruits

# Input processing
inputs = input().split()
N, C = int(inputs[0]), int(inputs[1])
weights = [int(x) for x in input().split()]

# Call the function and print the output
result = max_fruits(N, C, weights)
print(result)
```
