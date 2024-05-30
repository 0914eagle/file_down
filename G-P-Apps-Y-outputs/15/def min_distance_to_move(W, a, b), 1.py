
def min_distance_to_move(W, a, b):
    if a + W <= b:
        return b - (a + W)
    elif b + W <= a:
        return a - (b + W)
    else:
        return 0

# Input
W, a, b = map(int, input().split())

# Output
print(min_distance_to_move(W, a, b))
```
