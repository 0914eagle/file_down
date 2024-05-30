
# Read input
n = int(input())
mochi_diameters = [int(input()) for _ in range(n)]

# Sort the mochi diameters in descending order
mochi_diameters.sort(reverse=True)

# Count unique diameters to find the maximum number of layers
unique_diameters = set(mochi_diameters)
max_layers = len(unique_diameters)

print(max_layers)
```
