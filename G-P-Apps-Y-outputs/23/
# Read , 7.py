
# Read input
N = int(input())
mochi_diameters = [int(input()) for _ in range(N)]

# Sort the mochi diameters in descending order
mochi_diameters.sort(reverse=True)

# Count unique mochi diameters to determine the number of layers
unique_diameters = set(mochi_diameters)
max_layers = len(unique_diameters)

print(max_layers)
```
