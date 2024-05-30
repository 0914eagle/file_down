
def max_kagami_mochi_layers(N, mochi_diameters):
    mochi_diameters.sort(reverse=True)
    unique_diameters = set(mochi_diameters)
    return len(unique_diameters)

# Read input
N = int(input())
mochi_diameters = [int(input()) for _ in range(N)]

# Calculate and print the result
print(max_kagami_mochi_layers(N, mochi_diameters))
```
