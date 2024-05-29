
def sandglass_sand_remaining(X, t):
    remaining_sand = max(0, X - t)
    return remaining_sand

# Read input
X, t = map(int, input().split())

# Calculate remaining sand
result = sandglass_sand_remaining(X, t)
print(result)
```
