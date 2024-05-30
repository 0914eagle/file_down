
# Read input
N = int(input())
mochi_diameters = [int(input()) for _ in range(N)]

# Sort the mochi diameters in descending order
mochi_diameters.sort(reverse=True)

# Count the unique mochi diameters to determine the number of layers
num_layers = len(set(mochi_diameters))

print(num_layers)
```
