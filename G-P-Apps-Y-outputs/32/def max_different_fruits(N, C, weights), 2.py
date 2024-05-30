
def max_different_fruits(N, C, weights):
    total_weight = 0
    fruits_count = 0
    unique_fruits = set()

    for weight in weights:
        if total_weight + weight <= C:
            total_weight += weight
            if weight not in unique_fruits:
                unique_fruits.add(weight)
                fruits_count += 1
        else:
            break

    return fruits_count

# Input parsing
input_str = input()
N, C = map(int, input_str.split())
weights = list(map(int, input().split()))

# Call the function and print the result
result = max_different_fruits(N, C, weights)
print(result)
```
