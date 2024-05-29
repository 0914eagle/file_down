
def remaining_sand(X, t):
    remaining_sand = max(X - t, 0)
    return remaining_sand

X, t = map(int, input().split())
print(remaining_sand(X, t))
```
