
# Function to solve the kagami mochi problem
def max_kagami_layers(N, diameters):
    unique_diameters = set(diameters)
    return len(unique_diameters)

# Input processing
N = int(input())
diameters = [int(input()) for _ in range(N)]

# Call the function and print the result
print(max_kagami_layers(N, diameters))
```
