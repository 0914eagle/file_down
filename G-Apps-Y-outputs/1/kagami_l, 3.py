kagami_layers(N, diameters):
    unique_diameters = set(diameters)
    return len(unique_diameters)

# Read input
N = int(input())
diameters = []
for _ in range(N):
    diameters.append(int(input()))

# Calculate and print the result
result = max_kagami_layers(N, diameters)
print(result