
def sandglass_sand_remaining(X, t):
    return max(0, X - t)

X, t = map(int, input().split())
print(sandglass_sand_remaining(X, t))
```
