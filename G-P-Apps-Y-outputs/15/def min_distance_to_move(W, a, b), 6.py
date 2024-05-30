
def min_distance_to_move(W, a, b):
    if a <= b <= a+W or b <= a <= b+W:
        return 0
    elif a+W < b:
        return b - (a+W)
    else:
        return a - (b+W)

# Input
W, a, b = map(int, input().split())

# Output
print(min_distance_to_move(W, a, b))
```
