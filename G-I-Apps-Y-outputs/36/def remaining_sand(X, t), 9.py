
def remaining_sand(X, t):
    return max(X - t, 0)

X, t = map(int, input().split())
print(remaining_sand(X, t))
```
