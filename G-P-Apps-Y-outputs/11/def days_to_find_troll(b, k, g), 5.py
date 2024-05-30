
def days_to_find_troll(b, k, g):
    if k % g == 0:
        return b // (k // g)
    else:
        return b // (k // g + 1) + 1

# Read input
b, k, g = map(int, input().split())

# Calculate and print output
print(days_to_find_troll(b, k, g))
```
