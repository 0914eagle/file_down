
def sandglass_sand_remaining(X, t):
    remaining_sand = X - t
    if remaining_sand < 0:
        return 0
    else:
        return remaining_sand

# Read input from Standard Input
X, t = map(int, input().split())

# Print the result
print(sandglass_sand_remaining(X, t))
```
