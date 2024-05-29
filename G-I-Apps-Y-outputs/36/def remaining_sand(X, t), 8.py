
def remaining_sand(X, t):
    remaining = X - min(X, t)
    return remaining

X, t = map(int, input().split())
print(remaining_sand(X, t))
```
